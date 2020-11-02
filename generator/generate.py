from pathlib import Path
import shutil
from typing import List, Union
import pkgutil

import crinita as cr

# Iterate through all entities
ENTITIES: List[Union[cr.Page, cr.Article]] = []
for single_file in pkgutil.walk_packages(['.']):
    try:
        if single_file.name == 'generate':
            continue
        pack = __import__(single_file.name)
        ENTITIES.append(pack.ENTITY)
    except:  # noqa
        continue

sites = cr.Sites(ENTITIES)
# ========= CONFIGURATION =========
# Path to outputs
output_directory: Path = Path('../websites/')
# Resource directory
resource_directory: Path = Path('RESOURCES')

# Add template path:
cr.Config.templates_path = Path('templates')
# Configure blog name
cr.Config.site_title = "IT Blog"
cr.Config.site_logo_text = "IT Blog"
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
# =================================

# Remove existing content
if output_directory.exists():
    shutil.rmtree(output_directory)
output_directory.mkdir()

# Generate sites
sites.generate_pages(output_directory)

# Add resources
shutil.copytree(resource_directory, output_directory, dirs_exist_ok=True)
