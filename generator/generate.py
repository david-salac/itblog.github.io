from pathlib import Path
import shutil
import datetime
from typing import List, Union
import pkgutil
from os import listdir
from urllib import parse

import crinita as cr

# Iterate through all entities
ENTITIES: List[Union[cr.Page, cr.Article]] = []
for single_file in pkgutil.walk_packages(['.']):
    try:
        if single_file.name == 'generate':
            continue
        pack = __import__(single_file.name)
        # Check if the URL does not contains anything wrong
        checked_url = pack.ENTITY.url_alias
        if parse.quote(checked_url) != checked_url.lower():
            raise ValueError("URL contains prohibited characters {}".format(
                checked_url
            ))
        ENTITIES.append(pack.ENTITY)
    except ValueError as e:
        raise e
    except:  # noqa
        continue

sites = cr.Sites(ENTITIES)
# ========= CONFIGURATION =========
# Path to outputs
output_directory: Path = Path('../docs/')
# Resource directory
resource_directory: Path = Path('RESOURCES')

# Add template path:
cr.Config.templates_path = Path('templates')
# Configure blog name
cr.Config.site_title = "IT Blog"
cr.Config.site_logo_text = "IT Blog"
cr.Config.site_title_homepage = "Personal blog"
cr.Config.append_to_menu = (
    {'title': 'HOME', 'url': '__HOME_PAGE__', 'menu_position': 0},
    {'title': 'My GitHub', 'url': 'https://www.github.com/david-salac/', 'menu_position': 30},
)
cr.Config.text_sections_in_right_menu = (
    {
        'header': 'About',
        'content': f'Professional blog about interesting issues in software and data engineering, data science and other similar topics related to IT created by David Salac.<p>Generated using <a href="http://www.crinita.com/">Crinita</a> in version {cr.__version__}.</p>'
    },
)
cr.Config.default_meta_description = "Professional blog about interesting issues in software and data engineering, data science and other similar topics related to IT created by David Salac."
cr.Config.default_meta_meta_author = "David Salac"
cr.Config.default_meta_keywords = "Professional blog, Information Technologies, Data Science, Data Engineering, Software Engineering"
cr.Config.site_home_url = "/"
cr.Config.site_map_url_prefix = "https://itblog.uk/"
cr.Config.robots_txt = """User-agent: *
Allow: /
Sitemap: https://itblog.uk/sitemap.xml"""
cr.Config.footer = '<p><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" src="images/creative_commons.png"></a><br>All the content is licensed under a <br><a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</p>'
cr.Config.resources_path = resource_directory
# =================================

# Remove existing content
if output_directory.exists():
    if output_directory.joinpath('images').exists():
        shutil.rmtree(output_directory.joinpath('images'))
    if output_directory.joinpath('styles.css').exists():
        shutil.rmtree(output_directory.joinpath('styles.css'))
    onlyfiles = [f for f in listdir(output_directory) if output_directory.joinpath(f).is_file() and cr.Config.site_file_suffix in f]
    for file in onlyfiles:
        output_directory.joinpath(file).unlink()
    if output_directory.joinpath("robots.txt").exists():
        output_directory.joinpath("robots.txt").unlink()
    if output_directory.joinpath("sitemap.xml").exists():
        output_directory.joinpath("sitemap.xml").unlink()
    if output_directory.joinpath("style.css").exists():
        output_directory.joinpath("style.css").unlink()

# Generate sites
sites.generate_pages(output_directory)

# Back-up sites
sites.archive(
    Path(f"../backup/backup_{datetime.datetime.now().strftime('%Y-%m-%d')}")
)
