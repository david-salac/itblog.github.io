# Two universes in the big data environment
import datetime
import crinita as cr

lead = """It is more than ordinary that organizations that work with big data have two absolutely separated teams - one team responsible for processing data (data scientists) and another for writing and designing applications for end-users (that formally should use that data). It is equally common that technical problems in one universe are incomprehensible to people in another one. Not very surprisingly, the split leads to many problems."""

content = """<p class="lead">It is more than ordinary that organizations that work with big data have two absolutely separated teams - one team responsible for processing data (data scientists) and another for writing and designing applications for end-users (that formally should use that data). It is equally common that technical problems in one universe are incomprehensible to people in another one. Not very surprisingly, the split leads to many problems.</p>

<h2>OLAP and OLTP</h2>
<p>The header of this subsection should probably be OLAP vs OLTP - but that would only emphasize the schism (when, in theory, there should not be any). Maybe it is time to clarify the terms for better understanding.</p> 

<p><strong>OLAP</strong>  is the acronym of Online Analytical Processing - that is what data people do. The main feature of this approach for processing data is that some large datasets are processed (for example, many terabytes). Therefore, the time required for processing (analysis) of these datasets is not the most critical metric. Typical operations are aggregations and statistics performed on column space in the database and training of some models. So, technologies optimizing these operations are the usual choice. It includes databases based on the Dynamo storage system (Casandra, DynamoDB) or the Hadoop distributed file system technologies (Apache Hive, Spark, HBase, etc.).</p> 

<p>The typical OLAP query would look like this: give me the top products frequently sold and have a high margin or the optimal commercials for a particular user group. The data query itself is the whole application - usually, only a little additional logic is required.</p>

<p><strong>OLTP</strong> is the acronym of Online Transaction Processing - that is what software engineers do. The main feature of OLTP is that the lowest possible response time (request's latency) is required. Also, the dataset is relatively small (for example, the number of items in a shopping basket or the number of products on one page for the browser window). The most common technologies for storing data are standard relational databases (like PostgreSQL, MS SQL, others) and similar database technologies (NoSQL databases like MongoDB, Neo4J, REDIS etc.). In addition, data queries are usually embedded in some larger applications that play a significant role (like Django-based web services).</p> 

<p>Each of these terms is relatively old (already established in the 1980s) and has been around for a while.</p> 

<h2>What is the problem?</h2>
<p>Members of data teams usually prepare a solution and do not see any problem with deploying that solution for end-users (for example: if we manage to prepare it in one week, you can deploy it in the next sprint). But, on the other hand, a software engineer that needs an application that responds quickly re-estimates the time for implementation from one week to many months (and multiply budget by factors like ten).</p> 

<p>The fact that the solution is much more time/money consuming is caused by the simple fact that the user needs to see a response quickly. So developers need to cache as much as they can (that incurs overhead related to updating of cache), store data in a more reasonable way (or rather multiple ways, including different dimension orders for various multidimensional variables, etc.). That all entails additional overhead (updating records in multiple databases, synchronization problems, dealing with race condition issues, distribution to many clusters). Naturally, as a solution is presented for end-users, the system must be carefully tested, which also costs a lot of time.</p>

<h2>How to deal with it?</h2>
<p>Many problems can be anticipated in the design phase. First, you should understand the data flows (and time/resources required for each computation), expected number of customers, maximal acceptable latency for requests (on some probability quantile), and then design a suitable solution. For example, it is not always necessary to respond immediately to every user request - some requests are more important than others. Also, the application is not always supposed to respond immediately to every user's request - for example, paying customers can have different treatment. Often, to save a considerable amount of money, you can slightly reduce the application's functionality or slightly change the logic. These are the business solution. However, management needs to have good technical background to make them.</p> 

<p>Technically, it is also possible to merge these two approaches (OLAP and OLTP) - so that the OLAP process runs continuously in the background and save results to a cache (or, generally, to some optimized database). There are generally two ways to deal with it - either you periodically process some relatively big chunk of data, or you use the stream of data (usually events that describe changes). Many technologies are ready-made to save you a vast amount of time when implementing either of these approaches (the whole Hadoop ecosystem, Apache Kafka).</p> 

<p>The drawback of this approach is that the user does not necessarily have the newest data (items stored in data warehouses are often quite old). This has to be considered when you design an application (there are standardized ways of analyzing risks). But an impact on the overall price of the project is very significant. Nevertheless, many times, this is the only way how to proceed. For example, products like LinkedIn use this approach regularly when creating feeds for user's boards. Technically, there is often a space for combining methods to process critical data in OLTP mode and others in OLAP. This is also a way companies like Twitter or LinkedIn proceed - tweets from some users are considered more important than others (therefore, are reflected immediately).</p> 

<p>Unfortunately, many organizations do not have the resources to design their systems carefully. This process requires seasonal management (capable of making the right decisions and foresee/being aware of potential problems) and highly-skilled engineers (capable of designing a system appropriately). Both are often missing. Plus, there is still the mindset: we need to proceed quickly; there is no space for design.</p> 

<h2>Typical use-cases and suggested technologies</h2>
<p>The most common use-case for OLTP is managing users and access management. The most common solution for storing information about a user's profile is a relational database accessed through ORM (Object-relational mapping) of a web framework. The typical combination is PostgreSQL accessed through Django. This can be combined with an in-memory database for managing sessions or the graph database to analyze users favourite products and their relations. But generally speaking, we are talking about standard transactional processing.</p>

<p>On the other hand, we have analytical processing with all available tools. The most typical use case is analyzing customers' orders in an e-shop. You need to know how many items you have sold in a specific period and the average margin. You can also do more complex analysis, like how many minutes the average customer spends on the website with one particular product. All these things are essential, but you usually do not need immediate feedback. The technical solution for described problems would be a database solution based on a Hadoop system (like Apache HBase, Druid, or Kudu). Using HDFS, you can easily store a massive dataset as files and process using some SQL interface.</p>

<h2>Where to get information?</h2>
<p>People often wonder how they could know all these essential things. Maybe there has not been anybody who would share it so far. Also, some people are often selfish - they need to prove that they are necessary for their employer - the simplest way to achieve it is not to share any knowledge - no one can replace you if nobody knows how to deal with problems. Unfortunately, mindsets like this are prevalent (especially in start-up environments).</p> 

<p>Online courses are also often not sufficient - not every lecturer is highly competent in this issue, or they are paid to advertise one concrete technology. Also, every acceptable course needs to be based on some simple example that does not cover all use-cases (it is not easy to deduce all possible use-cases for a particular technology).</p> 

<p>Similar problems are when it comes to literature. There are, however, a few exceptions. For example, one of the very interesting books about data processing issues is Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems (author: Martin Kleppmann). I strongly recommend this book to everyone who deals with applications based on big data.</p>

<h2>Summary</h2>
<p>There are two ways to process data - OLAP and OLTP. Online Analytical Processing (OLAP) is the approach for processing big data sets - mainly used to answer complex analytical queries. On the other hand, software engineers use Online Transaction Processing when they develop applications (response from database has to be quickly returned to the user). Each of these approaches has its challenges (and suit of technologies). Differences can cause tunnel vision for engineers, leading to practical problems (either too expensive or too slow applications). Therefore, it is important to reflect these problems in the project's design phase.</p>
"""

ENTITY = cr.Article(
    title="Two universes in the big data environment",  # noqa: E501
    url_alias='two-universes-in-the-big-data-environment',  # noqa: E501
    large_image_path="images/bd_new_big.jpg",
    small_image_path="images/bd_new_small.jpg",
    date=datetime.datetime(2021, 10, 2),
    tags=[cr.Tag('Database', 'database'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="There are two ways to process data - OLAP and OLTP. Online Analytical Processing (OLAP) is the approach for processing big data sets in analytical queries."  # noqa: E501
)


