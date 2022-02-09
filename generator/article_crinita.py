# Suitable ways to generate complex static websites in Python
import datetime
import crinita as cr
import html

lead = """There are many interesting use-cases for generating static websites. They reach from a specific website (like documentation) to a general-purpose application (like cached images of e-shops, blogs, etc.). The main advantage of a static website is the simplicity of the product, almost no requirements to infrastructure (even GitHub can host them) and security. Many technologies help to generate static websites, from complex frameworks to simple generators."""

example_template = html.escape(r"""<!DOCTYPE html>
<html lang="{{ language }}">
    <head>
        <title>{{ title }}</title>
        <meta charset="UTF-8">
        <meta name="keywords" content="{{ keywords }}" />
        <meta name="description" content="{{ description }}">
    </head>
    <body>
        {% include 'menu.template' %}
        <div class="content">
            {# INCLUDE CONTENT HERE #}
            {% if url != 'HOME' %}
            {% include 'drop_nav.template' %}
            {% endif %}
            {% include content_file %}
            {# GENERATED CONTENT #}
            {{ content }}
        </div>
        {# INCLUDE FOOTER HERE #}
        {% include 'footer.template' %}
    </body>
</html>""")

script_example = html.escape(r"""import jinja2
import pathlib

# Set paths to directoris
PATH_TEMPL = pathlib.Path(path_to_template_dir)
PATH_OUTPUT = pathlib.Path(path_for_output_dir)

# Parse template in file 'page.templ'
with PATH_TEMPL.joinpath('page.templ').open('r') as tem_han:
    # Parse template from file
    template = jinja2.Environment(
        loader=jinja2.FileSystemLoader(PATH_TEMPL)
    ).from_string(tem_han.read())
    # Content as HTML code
    html_str = template.render(
        # Set variables of template file
        language="en",  # {{ language }} in template
        title="My Super Page",  # {{ title }} in template
        keywords="what",  # {{ keywords }} in template
        description="desc",  # {{ description }} in template
        content="<h1>Hello</h1>",  # {{ content }} in template
        url="HOME"  # External variable in template
    )
    # Write content to output file
    with PATH_OUTPUT.joinpath('page.html').open('w') as fp:
        fp.write(html_str)""")

crinita_json = html.escape(r"""{
  "tag_cloud_template": "__DEFAULT__",
  "menu_template": "__DEFAULT__",
  "recent_posts_template": "__DEFAULT__",
  "text_sections_in_right_menu_template": "__DEFAULT__",
  "layout_template": "__DEFAULT__",
  "list_of_entities": [
    {
      "object_type": "Page",
      "template": "__DEFAULT__",
      "description": null,
      "keywords": null,
      "url_alias": "about",
      "title": "About",
      "large_image_path": "images/blog_big.jpg",
      "content": "<p>About page content</p>",
      "menu_position": 20
    },
    {
      "object_type": "Article",
      "template": "__DEFAULT__",
      "description": null,
      "keywords": "kw_1, kw_2",
      "url_alias": "some-article",
      "title": "Some article",
      "tags": [
        {"name": "Some tag", "url_alias": "some-tag"}
      ],
      "date": "2021-12-17T00:00:00",
      "lead": "Article lead.",
      "content": "<p>Article content</p>",
      "large_image_path": "path/to/file.jpg",
      "small_image_path": "path/to/file.jpg"
    }
  ]
}""")

content = f"""<p class="lead">There are many interesting use-cases for generating static websites. They reach from a specific website (like documentation) to a general-purpose application (like cached images of e-shops, blogs, etc.). The main advantage of a static website is the simplicity of the product, almost no requirements to infrastructure (even GitHub can host them) and security. Many technologies help to generate static websites, from complex frameworks to simple generators.</p>
<h2>Analyzing the complexity of your product</h2>
<p>When deciding what static website generator to use, it is always crucial to analyze the complexity of your website first. There are simple tools called template engines for simple applications, like a website composed of a few pages. The template engine is not a framework - it just works on the principle of inserting common tags (components) into a website. Each programming language has some of these - in Python, the most popular is Jinja2.</p>
<p>Then there is a middle-ground for relatively elaborate static applications like blogs or documentation. These are precisely those cases for complex static website generators. Technically, each generator uses some template engine internally for generating multiple components following some patterns. Then, there is a need to have a source database containing all data (like blog posts or product descriptions) - that is usually a file database. Some static website generators contain tools for dealing with JSON, Markdown files or similar - but the data content is in these files - therefore, the logic uses a file database.</p>
<p>The last option - mainly helpful for large scale applications (like e-shops) - is to use front-end frameworks (like Vue.JS). The advantage of front-end frameworks is that they allow you a high level of flexibility - ultimately, there is no limit for application. The disadvantage of this approach is that output is often JavaScript-based and resource hungry. There is also a possibility of using the front-end framework and static website generator for generating the back-end. If you are familiar with REST logic, front-end frameworks receive data via GET requests. But the request can easily read static content (not calling any framework like Django). So, instead of generating websites, JSON structure is generated in a static website generator and provided to the front-end framework.</p>
<p>Ultimately, deciding what approach to select depends on your experiences. Unfortunately, for many applications, there is no clear optimal way. </p>
<h2>What is available in Python?</h2>
<p>A few interesting technologies (frameworks) for static website generation are available for Python. Usually, they internally use the Jinja2 template engine and a Markdown interpreter. The most popular one is Pelican, then there is a lot of others, like Crinita.</p>
<h3>Static website generator Pelican</h3>
<p>Pelican is a standard for static website generation in Python. It provides a user-friendly interface, has comprehensible documentation and a large community. Internally, it uses the Jinja2 template engine for content generation. It also supports a development environment in which changes in content are immediately reflected on the local server - making development a lot easier as you can access sites continuously from a browser.</p>
<h3>Static website demo generated by Pelican</h3>
<p>First, you need to install Pelican. Using an IDE that supports virtual environments (like PyCharm) is convenient. To install Pelican supporting Markdown language, commit the command in the virtual environment console: <code>pip install pelican [markdown]</code>.</p>
<p>After installation (which should run smoothly), use the quick start by committing the command: <code>pelican-quickstart</code>. Many convenient options are available in the quick start console (read the documentation to know more).</p>

<pre class="code"><code>(venv) usr@grp:~/path$ pelican-quickstart
Welcome to pelican-quickstart v4.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can
generate the files needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Demo page
> Who will be the author of this web site? David Salac
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? (Y/n) n
> Do you want to enable article pagination? (Y/n) n
> What is your time zone? [Europe/Rome] UTC
> Do you want to generate a tasks.py/Makefile 
  to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using
  Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) N
Done. Your new project is available at /PATH</code></pre>

<p>The quick start script generates a standard file structure. The most important folder is <code>./content</code> - a placeholder for all MD files with website content.</p>
<p>You can easily add new MD files. Each one should start with a metadata section (well documented). For example:</p>

<pre class="code"><code>Title: Welcome page
Date: 2021-12-30 10:20
Modified: 2021-12-31 19:30
Category: Something
Tags: demo, example
Slug: welcome-page
Authors: David Salac
Summary: This is a short description of page.

Here comes the standard content.

# Some header
Whatever you want.</code></pre>

<p>This generates a post called 'Welcome page' with defined tags (demo, example), authors, etc. </p>
<p>To run the local server and see the results, use the command:</p>
<pre class="code"><code>make devserver</code></pre>
<p>Then you should be capable of accessing the website at the URL displayed in the log of command.</p>
<h3>Using Jinja2 directly</h3>
<p>Jinja2 represents a straightforward and effective way of generating websites content. Technically, it is a template engine - meaning that you can define things as frequently repeated sections of pages (menus, etc.) in one place and insert them into the code of other pages. Moreover, it implements some frequently used functionality (for example, if/else statements or for-loop). Also, many frameworks internally use Jinja2 as their default template engine (like Django, Flask and others) - it means that it is fast enough to be used even in a dynamic application (for just-in-time content generation).</p>
<p>Some example of simple web layouts created using the Jinja2 template follows:</p>
<pre class="code"><code>{example_template}</code></pre>
<p>This example includes almost everything that you need to start. There are different kinds of blocks - some use external content passed by a Python script (e.g., title, description), others define the template's logic (see the menu).</p>
<p>Actual Python script that generates a page based on this template might look like:</p>
<pre class="code"><code>{script_example}</code></pre>
<p>In this example, templates for pages based on Jinja2 logic are in one directory with a name (path) defined in variable <code>PATH_TEMPL</code>. This example presents the standard approach for generating simple static sites. It is important to note that the output file can be everything (for example, XML sitemap or JSON structure), making Jinja2 very powerful.</p>
<p>Many other important functional blocks are available for Jinja2, so please read the documentation to see more.</p>
<h3>Static website generator Crinita</h3>
<p>Another less popular option is to use the static website generator Crinita. However, it is not a standard framework that would allow you to use things like the development environment, yet it contains everything needed. The motivation for creating Crinita was to have a simple way for migration from the Blogger.com platform to a static website hosted on GitHub. That is also why the default template uses many features characteristic for this platform.</p>
<p>The most significant advantage of Crinita is that it can handle JSON serialized posts. The disadvantage is that it requires knowledge of Python. Plus, there is no live version (development environment) reflecting changes immediately.</p>
<h3>A demo that uses Crinita</h3>
<p>The simplest way to generate a website using Crinita is to use JSON format. For example, the defining structure can look like the following:</p>
<pre class="code"><code>{crinita_json}</code></pre>
<p>The script that would generate sites can look like this:</p>
<pre class="code"><code>import pathlib

import crinita as cr

cr.Config.site_title = "Some blog"

sites = cr.Sites.sites_from_json(
    # Defining JSON string
    open("source.json").read()
)

sites.generate_pages(
    # Output path
    pathlib.Path("./demo")
)</code></pre>

<p>There are many configuration options that you can find in documentation (or on the project's GitHub repository).</p>
<p>To generate a website, install Crinita locally (<code>pip install crinita</code>) and run the Python script defined above. The output is the set of HTML files that can be easily uploaded to some static website hosting (like GitHub pages).</p>

<h2>Summary</h2>
<p>There are multiple ways to generate static websites. The simplest way for smaller applications is to directly use a template engine (like Jinja2). For more complex applications like blogs, there are ready-made frameworks like Pelican or Crinita (in Python). They use Jinja2 internally and implement many useful additional features. Another option is to use a front-end framework like Vue.JS - this option allows the biggest flexibility, but it has cons like resource-hungry outputs. The third way is to combine a static website generator with a front-end framework. This article discusses only the most popular Python frameworks and template engines.</p>
"""

ENTITY = cr.Article(
    title="Suitable ways to generate complex static websites in Python",
    url_alias='suitable-ways-to-generate-complex-static-websites-in-python',
    large_image_path="images/blog_big.jpg",
    small_image_path="images/blog_small.jpg",
    date=datetime.datetime(2020, 11, 3),
    tags=[cr.Tag('Web application', 'web-application'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Crinita', 'crinita')],
    content=content,
    lead=lead,
    description="Generators of static pages present a suitable way for the effective creation of secure and compact websites. Crinita is highly efficient Python generator."  # noqa: E501
)
