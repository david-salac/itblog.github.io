import crinita as cr

html_code = """<p class="lead">If you have any queries regarding the content of these websites, feel free to contact me. The simplest way is to raise the issue on GitHub page for this page (available <a href="https://github.com/david-salac/itblog.github.io">HERE</a>). I typically react as soon as possible.</p>
<p>I would be glad if you let me know about any bug that you find either on these sites or on my GitHub projects. Also, I would appreciate if you propose any interesting issue in software engineering that I can cover by some post on this blog.</p>
<h2>Acknowledgement</h2>
<p>So far, this website has been visited more than ten thousand times. For me, it is a great impetus. I do really appreciate that readers consider this website useful. Also, I have already received some suggestions for improvements that are all reflected. Thank you for that.</p>
"""

ENTITY = cr.Page(
    title="Contact",
    url_alias='contact',
    large_image_path="images/contact_big.jpg",
    content=html_code,
    menu_position=25
)
