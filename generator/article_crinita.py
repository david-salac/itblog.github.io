# Suitable ways how to generate complex static websites in Python
import datetime
import crinita as cr
import html

lead = """How to effectively generate a static website is a common problem that each developer has to solve at some point. Static websites can be helpful for many purposes like for web composed of a few static pages, documentation or either a complex blog with tags and many articles. The most commons reasons why to prefer static website are security, cheap infrastructure, and fast deployment. But what are the suitable tools in Python for this purpose?"""

example_template = """<!DOCTYPE html>
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
</html>"""

script_example = """import jinja2
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
        fp.write(html_str)"""

content = """How to effectively generate a static website is a common problem that each developer has to solve at some point. Static websites can be helpful for many purposes like for web composed of a few static pages, documentation or either a complex blog with tags and many articles. The most commons reasons why to prefer static website are security, cheap infrastructure, and fast deployment. But what are the suitable tools in Python for this purpose?

<h2>The rationale behind this article</h2>
<p>This article is a warning against Blogger (a system for blogs maintained by Google). It is difficult to say what is the worst feature of the current Blogger platform - if it is no friendliness towards Google search engine (how paradox), weak technical implementation (many bugs and many weak features - like inserting code to blog), poor WYSIWYG that deformed any input etc. Simply, Blogger (despite its obvious popularity) is a very bad choice.</p>
<p>So what are other choices if you want to run a blog? There are many commercial services (like Wix, Medium) that allow you to do so. But generally speaking, they are quite expensive. Another option is to run a blog on your own. The first option is naturally WordPress. But after a few seconds of searching, you can find what the cons of this idea are. WordPress is a security hell and very weak in backup and restore procedures.</p>
<p>Arguably the optimal solution is to have some good generator of static pages and host your blog on GitHub. Just to emphasize it, GitHub is now capable of making your repository operates as hosting for static websites. That is convenient for many purposes - you have whole git machinery that does back-up your work and also offers a quick way for publishing it (including the possibility of publishing on your domain). What is remaining is to select the optimal technology that can do all the work that is required.</p>

<h2>What is available in Python?</h2>
<p>There are dozens of different tools for these purposes. Some of them are well known (like Sphinx), others are unknown. The only problem is that there is not any tool that would represent what is needed if you need functionality similar to the Blogger one (tags, static pages, list of posts, and blog posts) with some additional functionality (generating of sitemaps and possibility to redefine metatags for each page). More precisely, some existing tools can be modified to work in this way - but it takes a lot of time that does not pay off.</p>
<p>So it was quite meaningful to create a new application that would deal with this issue. It is called Crinita, and it fits exactly to this purpose (it means to allow someone to quickly and easily run out of the Blogger to something better).</p>

<h3>About static websites generator Crinita</h3>
<p>Technically, it is a wrapper for the popular python library called Jinja2 (that allows you to generate varying HTML code from template). Template engine Jinja2 is also the only requirements (dependency) of Crinita. Therefore you can very easily install Crinita using PIP command.</p>
<p>The paramount importance was to have something simple to use, and that is ready to make websites deployable on GitHub. Crinita is precisely the application for these purposes. You can simply add a new page or article to the system, and the rest is generated for you (including tag clouds, pagination functionality, and all other details).</p>
<p>There are many demos available that can allow you to learn how to deploy your block as quickly as possible (and mainly, in much better quality than was possible on Blogger).</p>

<h3>What is good to know before you choose Crinita</h3>
<p>As things are, Crinita requires to have some knowledge of Python and HTML coding - also it is very helpful to understand the concept of the Jina2 template engine (described below). This required knowledge can stop some users, but it was a necessary condition for achieving the best result. Also, many available demos can help you to overcome this issue.</p> 
<p>In the new version of Crinita, there is a helpful feature that allows you easily backup and restore your products (it allows creating a ZIP file with all the content). This is particularly convenient, as your results can be stored in multiple places.</p>

<h2>Using Jinja2 directly</h2>
<p>Jinja2 represents a very simple and effective way for generating websites content. Technically, it is a template engine - meaning that you can code things as frequently repeated sections of pages (menus, etc.) in one place and just insert them to code. It also implements some frequently used functionality (for example if/else statements - very convenient if you want to emphasize selected item in menu). By the way, Jinja2 is used by many frameworks as their default template engine (like Django, Flask and others) - so, notable, it means that it is fast enough to be used even in a dynamic application (for just in time content generation).</p>
<p>Some example of simple web layouts created using Jinja2 template follows:</p>

<pre class="code"><code>{}</code></pre>

<p>As you can see in the example, there is a different kind of blocks, some of them are required to be set from Python script (like title, description), others blocks are just included files (other templates), like the template for a menu.</p>
<p>Actual Python script that generates a page based on this template might look like:</p>

<pre class="code"><code>{}</code></pre>

<p>In this example, a template using Jinja2 logic is saved in some directory (with name 'page.templ') together with other templates for footer etc. This example presents the standard approach for generating sites. Naturally, normally you would have to generate multiple pages (but the logic will be the same). It is probably obvious that the output file can be everything (for example XML sitemap) - this makes Jinja2 very powerful.</p>

<h2>Other template engines</h2>
<p>There are many (maybe more than a hundred) template engines that work similarly to Jinja2 does. You can easily find many of them in Python documentation references (just search for Templating in Python). The greatest advantage of Jinaj2 is its simplicity (it is trivial to learn it) and yet it implements everything needed and it is very simple to install it (you can use just pip command). Also, you can find a lot of ready-made templates for Jinja2 (it can save a lot of time).</p>
<p>One template engine that is worth mentioning is Templite+. It can be very effective for small websites composed of several sub-pages. It also contains advanced features (like if/else statements) and the possibility of including other files - which is mostly all the functionality that is needed.</p>
""".format(html.escape(example_template), html.escape(script_example))

ENTITY = cr.Article(
    title="Suitable ways how to generate complex static websites in Python",
    url_alias='suitable-ways-how-to-generate-complex-static-websites-in-python',
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
