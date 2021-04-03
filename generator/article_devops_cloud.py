# More about some useful concepts in Python language
import datetime
import crinita as cr

lead = """There are many common challenges related to systems that process large data sets (like big netCDF or GRIB files). One of the most important decision is whether to deploy infrastructure on some cloud service or if it is better to use an on-premises solution. If the cloud appeals to you then other challenges arise, which provider would be the best one, how to deploy - use infrastructure as a code. """

content = """There are many common challenges related to systems that process large data sets (like big netCDF or GRIB files). One of the most important decision is whether to deploy infrastructure on some cloud service or if it is better to use an on-premises solution. If the cloud appeals to you then other challenges arise, which provider would be the best one, how to deploy - use infrastructure as a code, or just some simple solution etc.
 
<h2>What systems do we analyse?</h2>
<p>This article is mainly focused on systems that operate with satellite images (and similar very big data sets). The common feature of these systems is that just a single data file can have many gigabytes (or tens of gigabytes) and it needs many of them to operate. The typical example might be a system for the prediction of energy of renewable resources (like solar photovoltaic panels, wind turbines or wave devices). These generators require a long data series of various variables (like wind speed, irradiance, temperature) to correct prediction in a fine resolution (like ten years in resolution ten minutes), also a spatial resolution should be very high. The same challenge is to predict doses of irradiance for a system designed to protect from sunburns. There are also many other applications.</p>
<h2>What is the common challenge?</h2>
<p>We need to have data quickly available, store them as cheaply as possible and optimally on some distributed system. As you can guess, it is technically not possible to have all these properties simultaneously. You can always have just two of these options. The cloud-based solution offers you a quickly available distributed interface - but it is certainly not cheap. If you have an on-premises solution - it is cheap and quick (but not available - distributed).</p>


<figure>
    <img src="images/cloud_dilema.png" alt="Figure 1: The challenge of the system">
    <figcaption>Figure 1: The challenge of the system - always only two of these three requirements are available</figcaption>
</figure>

<h2>Local and production stack</h2>
<p>One of the challenges when deploying your code is the difference between local and production (or staging) stack. Some people tend to use different technologies on the local stack and the production one - that is not a good idea. Especially the database technology should be the same on both. If all your containers should be the same in production as they are on your local machine. If you use Kubertness for your deployment stack and Docker Swarm on the local one can also make a difference (although in this case tolerable one).</p>

<h2>Cloud-based solution</h2>
<p>Let's start with a selection of cloud services provider. Without any impudence I dare myself to say that it almost does not matter - the difference is very subtle. Both price and the quality of services will be similar no matter if you chose Amazon, G-Cloud, Azure (having experience with all of them). It is though reasonable to spend some time studying the possibilities of each provider - as practically impossible to stay cloud-agnostic for a long time.</p>
<p>The best practical approach is infrastructure as code - by deploying Terraforms or Kubertness with Docker. It will save you a lot of time in the future. Optimally, use environmental variables to determining the difference between local and production stack.</p>
<p>If it comes to price calculation of your cloud-based solution - be aware of a few things. Among them is the fact that most of the expensive parts of your stack can be off for most of the time (that saves money - as the price of services is lower when they are not running). Also, surprisingly a quite expensive part of your system will be the storage place (as you will need many terabytes of data). It can be helpful to study the optimal way how to store data for each provider (for example MS Azure provides different tiers for storing data regarding how quickly you need to access them).</p> 
<p>Regarding the practical experience with a system that was designed for renewable energy prediction with a few active users and about 1TB of data - expect a price of around £1000 per month (in 2020 price levels). The same price level was in the system designed for processing satellite data for healthcare purposes.</p>

<h2>On-premises solution</h2>
<p>An on-premises solution (meaning servers that you really own) provides you with a cheaper solution. The disadvantages compared to the cloud-based solution are quite clear. You need to spend a lot of time maintaining devices. On the other hand - do not believe that cloud-based solution works without any intervention. You will probably have one dedicated DevOps person for your systems one way or another (so all the savings go nowhere).</p>
<p>The local solution is a perfect thing from a data science perspective - for testing and pre-processing of data. Mainly doing some filtration of input images and their classification (or other numerically difficult computations). You can save a lot of money this way. Similarly, the on-premises solution does not suffer from expensive storage spaces - as disks are quite cheap.</p>

<h2>Dropbox (or similar technologies) for storage</h2>
<p>There are some surprising ways how to save many and stay on the cloud. One of them is to use external storages for your big data sets. One such solution is Dropbox (from Google). There is a Python API for accessing it and it is quite cheap (compared to cloud-based storages). There are of course many other similar technologies. Using them, you can save many hundreds of pounds every month without losing any advantage of a cloud-based environment.</p>

<h2>Dockerizing your entities</h2>
<p>The structure of your system will probably be the same no matter what your application specifically does. It is however good to be aware that dockerizing most of the containers is a trivial task - however, the remaining few per cent will cause you a massive headache. For example, GeoServer, an application for providing map tires is a total disaster - an old fashion big (state-full) server. The traditional Pareto principle applies here (spend 80 per cent of your time with something that provides you less than 20 per cent of outcomes). One thing is also important to bear in mind if you decide to deploy in the cloud - try to use cloud services for things like databases as much as you can (it can save you a lot of time and also money).</p>

<h2>Summary</h2>
<p>There are many other things regarding operational tasks for systems processing environmental data. If it comes to the decision where your infrastructure runs - there is no simple pattern to follow. The on-premises solution has many pros and cons as does a cloud-based solution. Generally, it makes sense to have the production part on the cloud and the data (pre)processing part running locally. However, if you decide to run everything on your machines it is a fully legitimate approach as well.</p>
"""

ENTITY = cr.Article(
    title="DevOps challenges in system processing satellite environmental data",
    url_alias='devops-challenges-in-system-processing-satellite-environmental-data',
    large_image_path="images/devops_big.jpg",
    small_image_path="images/devops_small.jpg",
    date=datetime.datetime(2020, 3, 7),
    tags=[cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('DevOps', 'devops'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('Web application', 'web-application')],
    content=content,
    lead=lead,
    description="There are many common challenges related to systems that process large data sets. The most important decision is if to deploy on a cloud service or locally."  # noqa: E501
)
