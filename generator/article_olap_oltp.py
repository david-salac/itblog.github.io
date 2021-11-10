# Two universes in the big data environment
import datetime
import crinita as cr

lead = """It is more than ordinary that organizations that work with big data have two absolutely separated teams - one team responsible for processing data (data scientists) and another for writing and designing applications for end-users (that formally should use that data). It is equally common that problems of people in one universe are incomprehensible to people in another one. Not very surprisingly, the split leads to many problems."""

content = """It is more than ordinary that organizations that work with big data have two absolutely separated teams - one team responsible for processing data (data scientists) and another for writing and designing applications for end-users (that formally should use that data). It is equally common that problems of people in one universe are incomprehensible to people in another one. Not very surprisingly, the split leads to many problems.

<h2>OLAP and OLTP</h2>
<p>The header of this subsection should probably be OLAP vs OLTP - but that would only emphasize the schism (when, in theory, there should not be any). So let's clarify the terms for better understanding.</p> 

<p><strong>OLAP</strong> is the acronym of Online Analytical Processing - that is what data people do. The main feature of this approach for processing data is that some large datasets are processed (for example, many terabytes). Therefore, the time required for processing (analysis) this data is not the most critical metric. Typical operations are aggregations and statistics performed on column space in the database. So, technologies optimizing these operations are the usual choice. It includes databases based on the Dynamo storage system (Casandra, DynamoDB) or the Hadoop distributed file system technologies (Apache Hive, Spark, etc.).</p> 

<p>The typical OLAP query would look like this: give me the top products frequently sold and have a high margin or the optimal commercials for a particular user group. The data query itself is the whole application (usually, only a little additional logic is required).</p>

<p><strong>OLTP</strong> is the acronym of Online Transaction Processing - that is what software engineers do. The main feature of OLTP is that the lowest possible response time is required. Also, the data set is relatively small (for example, the number of items in a shopping basket or the number of products on one page for the browser window). The most common technologies for storing data are standard relational databases (like PostgreSQL, MS SQL, others) and derived technologies (NoSQL databases like MongoDB, REDIS, Neo4J etc.). In addition, data queries are usually embedded in some larger applications that play a significant role (like Django-based web services).</p> 

<p>Each of these terms is relatively old and has been around for a while.</p> 

<h2>What is the problem?</h2>
<p>Members of data teams usually prepare a solution and do not see any problem with deploying that solution for end-users (for example: if we manage to do it in one week, you can deploy it next sprint). But, on the other hand, a software engineer that needs an application that responds quickly re-estimates the time for implementation from one week to many months (and multiply budget by factor ten).</p> 

<p>The fact that the solution is much more time/money consuming is caused by the simple fact that the user needs to see a response quickly. So developers need to cache as much as they can (that incurs overhead related to updating of cache), store data in a more reasonable way (or rather multiple ways, including different dimension orders for various problems, etc.). That all entails additional overhead (updating records in multiple databases, synchronization problems, dealing with race condition issues, distribution to many clusters).</p>

<h2>How to deal with it?</h2>
<p>Many problems can be anticipated in the design phase. First, you should understand the data flows (and time/resources required for each computation) and design a suitable solution. For example, it is not always necessary to respond immediately to every user request. Not every user is supposed to have an immediate response from the application (for example, paying customers should have different treatment than others). Often, to save a considerable amount of money, you can slightly reduce the functionality of the application or slightly change the logic. These are the business solution (not technical).</p> 

<p>From the technical point of view, it is also possible to merge these two approaches (OLAP and OLTP) - so that the OLAP process runs continuously in the background and save results to a fast cache (or, generally, to some optimized database). There are generally two ways to deal with it - either you periodically process some relatively big chunk of data, or you use the stream of data (usually events that describe changes). Many technologies are ready-made to save you a vast amount of time when implementing either of these approaches (the whole Hadoop ecosystem, Apache Kafka).</p> 

<p>The drawback of these solutions is that the user does not necessarily have the newest data (items stored in data warehouses are often quite old). When you design an application, this has to be considered (there are standardised ways of analysing risks). But an impact on the overall price of the project is very significant. Many times, this is the only way how to proceed.</p> 

<p>Unfortunately, many organizations do not have the resources to design their systems carefully. This process requires seasonal management (capable of making the right decisions and foresee/being aware of potential problems) and highly-skilled engineers (capable of designing a system appropriately). Both are often missing. Plus, there is still the mindset: we need to proceed quickly; there is no space for design.</p> 

<h2>Typical use-cases and suggested technologies</h2>
<p>The most common use-case for OLTP is managing users and access management. The most common solution for storing information about a user's profile is a relational database accessed through ORM (Object-relational mapping) of a web framework. The typical combination is PostgreSQL accessed through Django. This can be combined with an in-memory database for managing sessions or with the graph database to validate complex relations (and prevent frauds). But generally speaking, we are talking about standard transactional processing.</p>
<p>On the other hand, we have analytical processing with all available tools. The most typical use case is analysing customers' orders in an e-shop. You need to know things like how many items you have sold in a specific period and the average margin. You can also do more complex analysis, like how many minutes the average customer spends on the website with one particular product. All these things are essential, but you usually do not need to have immediate feedback. The technical solution for described problems would be a database solution based on a Hadoop system (like Apache HBase, Druid, or Kudu). Using HDFS, you can easily store a massive dataset as files and process using some SQL interface.</p>

<h2>Where to get information?</h2>
<p>People often wonder how they could know all these essential things. Maybe there wasn't anybody who would share it. Also, people are often highly selfish - they need to prove that they are necessary for their employer - the simplest way to achieve it is not to share any knowledge (no one can replace you if they do not know how to deal with problems). Unfortunately, mindsets like this are prevalent (especially in start-up environments).</p> 

<p>Online courses are also often not sufficient - not every lecture is highly competent in this issue, or they are paid to advertise one concrete technology. Also, every acceptable course needs to be based on some simple example that does not cover all use-cases (it is not easy to deduce all possible use-cases for a particular technology).</p> 

<p>Similar problems are if it comes to literature. There are, however, a few exceptions. For example, one of the very interesting books about data processing issues is Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems (author: Martin Kleppmann). I strongly recommend this book to everyone who wants to deal with applications based on big data.</p>

<h2>Summary</h2>
<p>There are two ways to process data - OLAP and OLTP. Online Analytical Processing (OLAP) is the approach for processing big data sets - mainly used to answer complex analytical queries. On the other hand, software engineers use Online Transaction Processing when they develop applications (response from database has to be quickly returned to the user). Each of these approaches has its challenges (and suit of technologies). Differences can cause tunnel vision for their users, leading to practical problems (either too expensive or too slow applications). It is important to reflect these problems in the design phase of the project.</p>
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


