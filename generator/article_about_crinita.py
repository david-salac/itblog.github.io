# Suitable ways how to generate complex static websites in Python
import datetime
import crinita as cr

lead = """How to effectively generate a static website is a common problem that each developer has to solve at some point. Static websites can be helpful for many purposes like for web composed of a few static pages, documentation or either a complex blog with tags and many articles. The most commons reasons why to prefer static website are security, cheap infrastructure, and fast deployment. But what are the suitable tools in Python for this purpose?"""

content = """How to effectively generate a static website is a common problem that each developer has to solve at some point. Static websites can be helpful for many purposes like for web composed of a few static pages, documentation or either a complex blog with tags and many articles. The most commons reasons why to prefer static website are security, cheap infrastructure, and fast deployment. But what are the suitable tools in Python for this purpose?

<h2>The rationale behind this article</h2>
<p>Once it happened that this blog was running on the Blogger (system for blogs maintained by Google). But it was very soon palpable that to choose Blogger was one of the worst decision that could be made. It is difficult to say what is the worst feature of the Blogger platform if it is absolutely no friendliness towards Google search engine (how paradox), weak technical implementation (many bugs and many weak features - like inserting code to blog), poor WYSIWYG that deformed any code etc. Simply, Blogger (despite its obvious popularity) is a very poor choice.</p> 
<p>So what are other choices if you want to run a blog? There are many commercial services (like Wix, Medium) that allow you to do so. But generally speaking, they are quite expensive. Another option is to run a blog on your own. The first option is naturally WordPress. But after a few seconds of searching, you can find what the cons of this idea are. WordPress is a security hell and very weak in back-up and restore procedures.</p> 
<p>At the end of the day, it is not difficult to find that the optimal solution is to have some good generator of static pages and host your blog on GitHub. Just to emphasize it, GitHub is now offering an interface for making your repository operates as an infrastructure for static websites. That is convenient for many purposes - you have whole git machinery that back-up your work and also the quick way for publishing it (on your own domain). What is remaining is to select the optimal technology that can do all the work that is required.</p>

<h2>What is available in Python?</h2>
<p>There are dozens of different tools for these purposes. Some of them are well known (like Sphinx), others are unknown. The only problem is that there is not any tool that would represent what is needed if you need functionality similar to the Blogger one (tags, static pages, list of posts, and blog posts) with some additional functionality (generating of sitemaps and possibility to redefine metatags for each page). More precisely, some existing tools can be modified to work in this way - but it takes a lot of time that does not pay off.</p>
<p>So it was quite meaningful to create a new application that would deal with this issue. It is called Crinita, and it fits exactly to this purpose (it means to allow someone to quickly and easily run out of the Blogger to something better).</p>

<h2>About static websites generator Crinita</h2>
<p>It is basically a wrapper for the popular python library called Jinja2 (that allows you to generate varying HTML code from template). As it happens, Jinja2 is also the only requirements of Crinita. Because of it, it can be very easily installed using PIP.</p>
<p>The paramount importance was to have something simple to use, and that is ready to make websites deployable on GitHub. Crinita is precisely the application for these purposes. You can simply add a new page or article to the system, and the rest is generated for you (including tag clouds, pagination functionality, and all other details).</p>
<p>There are many demos available that can allow you to learn how to deploy your block as quickly as possible (and mainly, in much better quality than was possible on Blogger).</p> 
<h3>What is good to know before you choose Crinita</h3>
<p>As things are, Crinita requires to have some knowledge of Python and HTML coding. That can hinder some users, but it was a necessary condition for achieving the best result. On the other hand, available demos can lead your hand so straightforwardly that it is quite simple to overcome this issue. Another thing that is good to mention is that when you have websites composed of just a few static pages - the simplest way is to use Jinja2 directly (as it allows you to have much higher flexibility).</p>
"""

ENTITY = cr.Article(
    title="Suitable ways how to generate complex static websites using Python language",
    url_alias='suitable-ways-how-to-generate-complex-static-websites-using-python-language',
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
