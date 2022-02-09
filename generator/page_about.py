import crinita as cr

html_code = """<p class="lead">This blog covers interesting issues in software engineering and data analysis. It mainly contains articles about issues that the author finds interesting. It would be great if all the readers leave some feedback to me (either in discussion or by email) - it is always great to have some motivation to continue.</p>
<h2>About author</h2>
<p>My name is David Salac. I have a master degree in mathematics and computer science. I have more than ten years of practical experience in these fields.</p>
<p>If you want to know more about mee, you can visit my <a href="https://www.linkedin.com/in/david-salac-12618b187/">LinkedIn profile (https://www.linkedin.com/in/david-salac-12618b187/)</a>. <em>In order to see my profile, you have to be log-in to LinkedIn due to privacy reasons.</em></p>
<h2>Licence</h2>
<p><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" src="https://i.creativecommons.org/l/by/4.0/88x31.png" style="border-width:0" /></a><br />All the articles on this blog are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</p>
<p>Some images here are the subject of the Pixabay licence (all of the photos are downloaded from the Pixabay.com, see more about the <a href="https://pixabay.com/service/license/">licence here</a>).</p>
<h2>GitHub</h2>
<p>If you want to see some of my coding work, you can visit my <a href="https://github.com/david-salac">GitHub profile (https://www.github.com/david-salac)</a>.</p>"""

ENTITY = cr.Page(
    title="About",
    url_alias='about',
    large_image_path="images/blog_big.jpg",
    content=html_code,
    menu_position=20
)
