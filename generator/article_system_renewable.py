# Software engineering perspective of the system for renewable energy prediction
import datetime
import crinita as cr

lead = """This article is focused on the design and implementation details of the system for the prediction of renewable energy. I am talking here about the web application (not about the desktop app). Some helpful information from the project management perspective is also mentioned (including costs of the project). This article can be helpful for you to decide if you want to choose this path and to save your time. """

content = """This article is focused on the design and implementation details of the system for the prediction of renewable energy. I am talking here about the web application (not about the desktop app). Some helpful information from the project management perspective is also mentioned (including costs of the project). This article can be helpful for you to decide if you want to choose this path and to save your time. 

<h2>What is the best programming language?</h2> 
<p>In theory, there are multiple good options. Strictly speaking, the main languages that are worth considering are Python, Go, C++ and Java. It probably does not make any sense to start any new project in Java, so let's exclude it (shame on you, Oracle).</p> 
<p>Probably the first choice would be Python (in version 3.6 or higher). There are many helpful libraries in Python (mainly: GDAL, Shapely, GeoPandas, NumPy/Pandas, Django, pvlib, xarray, Celery and others). All you need is implemented - you just need to put these building blocks together. And here start the first problem - as you develop something continuously, versions of your (sub)dependencies change, and this causes problems (as the main dependency stops working when its sub dependency is updated). Often you spend days chasing what went wrong to find out that some sub-sub-dependency was updated and it is no longer backwards compatible.</p> 
<p>There is also another well-known problem of Python - performance. Python still keeps GIL that disallows you to use a standard multithreading approach. As you are processing big data sets (often tens of GBs in size), this is a very significant limitation. Plus it is interpreted language which is generally worse in performance. Just some practical data (the most common use-case), if you have some scenario composed of 10 generators (like wind turbines, solar PVs), and you need to simulate their behaviour on ten years of weather data (with resolution 10 minutes) - you need to expect running time around an hour (using all hardware resources you have).</p>
<p>Another option would be the Go language. It is modern, simple and quite similar to Python - it also does not suffer from performance. So what is the problem? The problem is that there are no libraries that you need. No PVLIB, no GDAL, no Shapely, etc. That makes work with geospatial data very difficult (as you need to implement everything on your own). It's a shame that Google hasn't yet published codes that would make work with Go simpler. On the other hand, it's fair to say, that even this problem can be overcome (as it's not tremendously difficult to build some libraries that would make these computations). </p>
<p>The last option can be C++. Well, all things that you need are available there. The only problem is that GDAL (which is the only reasonable tool for work with geospatial data in C++) is implemented in Cpp98 standard and there is no will to update it - that technically exclude the possibility of using the latest version of C++ and makes your code particularly vulnerable (to memory leaks and other unexpected errors).</p> 
<p>Other languages, like C#, are intentionally excluded, as it's difficult to assess how much they differ from the mentioned ones. Particularly C# is not a very popular choice for processing geospatial data.</p>

<h2>So we choose Python, what next (system design)?</h2>
<p>The first thing you need to know is the overall design of your system - what are the main components and how they are mutually related. Generally, it might be helpful to write some standardized System Design Document (aka SDD) and the Requirements Document plus the Algorithm Description Document (describing the mathematical and algorithmic side of the problem). It should include UML diagrams (including use-cases, database design, estimates).</p> 
<p>If it comes to main (functional) components:</p>

<ul>
<li>Gateway: using Ngnix or similar technology.</li>
<li>Web Application (framework): you would probably choose to implement it using Python/Django combination.</li> 
<li>Relational database: in this case probably PostgreSQL (you can choose also some commercial DB solution, but it's useless)</li>
<li>In-memory database: probably Redis (or Memcached). </li>
<li>Map-tile server: probably GeoServer (unfortunately, still the only available simple ready-made solution).</li>
<li>Message broker: probably using Celery.</li>
<li>Front-end solution: probably based on the Vue.js framework.</li>
<li>Storage solution: in cloud probably using Amazon S3 bucket.</li>
</ul>

<p>Regarding Gateway you do not have to expect anything unexpected - it can be helpful to have some special routes accessing some "big" data directly - but the rest is just a standard system.</p> 
<p>If it comes to the web application (in the strict sense web framework) you have two options. The caveman approach would be to use Flask/FastAPI or a similar light-weighted framework. The more sophisticated one is to use Django. Each approach has its pros and cons. I would suggest using Django (as you save a lot of time implementing trivial utilities). On the other hand Flask or FastAPI code is easier to maintain.</p>
<p>Regarding the relational database, the reasonable option is PostgreSQL - it is free, opensource and of very high quality (plus continuously maintained). It is also good to avoid using MySQL - as its quality deteriorated in the past ten years (and because of well-known errors like restricted primary key size). Also, be sure that you keep the database technology the same for development and production stack, it can prevent many unexpected errors.</p>
<p>The in-memory database is typically helpful just as an external service for other applications (like for Celery asynchronous task queue), or sub-dependencies of Django like django-axes (for logging and preventing attacks users account). You can use it directly as well for some reasonable caching.</p>
<p>If it comes to the map-tile server it is good to design your system in a way that allows you to have some home-made solution. Currently, the only reasonable full-scale solution is GeoServer. But this Java-based application is based on code written around the year 2006. So it is an absolute hell to deploy it in the cloud environment. Plus you have to expect strange behaviour (when it fails to serve one task properly, it switch its state and does not work any more - very inconvenient for production). So, consider having some own solution to avoid using GeoServer if possible.</p>
<p>A message broker is an essential part of the system - as you cannot address computations directly (because of the risk of timeouts - typical computation can take you more than an hour without any problems). If you use Django, there is a very well integrated message broker called Celery (based on Redis or RabitMQ, prefer Redis if you can as it is more popular and used by many other dependencies applications as well). You can use it immediately by adding just two dependencies to your requirements - but despite how nice it sounds, expect many problems with Celery. Like unexpected behaviour, not the best documentation, a lot of refactoring from its source code. But yes, it is usable and no, there is nothing significantly better than that.</p>
<p>If it comes to frond-end solution - I am not a real expert in this realm. Without doubts, the front-end should be completely separated from the back-end - using some restful API access data (use the Django REST framework for implementation). A very popular, modern and simple solution for the front-end can be based on the Vue.js framework.</p> 
<p>The storage solution is something that you have to consider carefully at the beginning. As you will have many hundreds of gigabits of data (or rather terabytes). You have to expect astronomical prices for cloud-based solutions in production. But, for an archive of data for data science purposes, you can use some cheaper cloud solution - like Dropbox. Dropbox can work as a cheap lake for your data from which you can pull them to your local machine - there is also an interface in Python for work with Dropbox (it is slightly difficult, but it works).</p>

<h3>Some general remarks regarding the development</h3>
<p>It is helpful if you fixed versions of your dependencies in the requirementes.txt file. But do not believe that it saves you any trouble (as many sub-dependencies do not have a fixed version and you cannot change this). Also, expect a lot of unexplainable behaviour - as many dependencies are not of the highest quality (for example, when you use xarray it rarely works like you want to). Also, in the design phase think carefully about backup and restore procedures (you need to implement them in a working and complete way). Frequently you will also need to profile your code for performance and memory issues (so read about some libraries and tools designed for this purposes which can save you a lot of time).</p>

<h2>Infrastructure</h2>
<p>A lot of things can be said about infrastructure. One of them can be: do not believe you can stay cloud-agnostic for long. Also, do not believe there is a significant difference between cloud providers (AWS, G-Cloud, Azure are more or less the same). It probably makes sense to use some infrastructure as a code approach (for example using Terraforms). Regarding deployment in the cloud you need to be aware of the astronomical prices - expect at least £1000 bill per month (really, per month!) plus some other costs related to operational work - you can easily hire a full-time DevOps engineer who will be busy enough.</p>
<p>It is also perfectly meaningful to have a powerful local machine for data science computations. Be aware of the fact that if you use Python you cannot rely on multithreading (because of GIL). So it is better to have a machine with a good Turbo Boost rather than with many cores.</p> 
<h2>Team and budget</h2>
<p>Generally, it does not make any sense to start your project if you cannot hire at least five full-time employees for at least two (or rather three) years. You will need at least one or two people dedicated to the data science engineering part. One or two people dedicated to back-end development and the same for front-end development. Above that, it is helpful to have some applied meteorologist and a full-time project manager. If it comes to the organisation of people, SCRUM/agile is arguably the only possible way to success.</p>
<p>All these things are necessary to consider when you are preparing a budget. Also, be aware that geospatial data are very expensive (free data are almost useless for any practical purposes).</p>
"""

ENTITY = cr.Article(
    title="Software engineering perspective of the system for renewable energy prediction",
    url_alias='software-engineering-perspective-of-the-system-for-renewable-energy-prediction',
    large_image_path="images/system_ren_big.jpg",
    small_image_path="images/system_ren_small.jpg",
    date=datetime.datetime(2021, 4, 2),
    tags=[cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Renewable energy', 'renewable-energy'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('Web application', 'web-application')],
    content=content,
    lead=lead,
    description="Article focused on the design and implementation details of the system for the prediction of renewable energy with some project management perspective."  # noqa: E501
)
