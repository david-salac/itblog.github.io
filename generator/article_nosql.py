# Most common use cases for NoSQL databases
import datetime
import crinita as cr

lead = """This article presents some most popular use-cases and technologies related to NoSQL databases. These types of databases have become more and more popular. Furthermore, each presented technology provides some advantages for the specific use case (for example, graph databases can help effectively select objects based on relations constraints). Therefore, it is becoming essential to know these technologies and be capable of using them."""

content = """This article presents some most popular use-cases and technologies related to NoSQL databases. These types of databases have become more and more popular. Furthermore, each presented technology provides some advantages for the specific use case (for example, graph databases can help effectively select objects based on relations constraints). Therefore, it is becoming essential to know these technologies and be capable of using them.
<p>It is vital to notice that some NoSQL databases do not consider data consistency as their primary goal (which is the opposite of relational databases). For example, MongoDB is optimized for distribution among many nodes, making it easier to access data and change data values quickly (but all nodes do not always have to be synchronized). There is a well-known trade-off between durability, accessibility and consistency. Either you can have your data quickly available or have them consistent.</p>
<h2>Document databases</h2>
<p>Document databases present an interesting option for storing data with many advantages. Unlike their relational counterpart, they usually do not require strict validation of input data (nor any structure of such input). Also, creating tables (called collection) is a straightforward process - so the creation of the collection itself can play an important role in application design. Finally, document databases can be beneficial when storing data series that do not always follow any reasonable structure.</p>
<h3>Example of video sequence classification</h3>
<p>Imagine that you want to classify frames (as images) in some video. If you have a known set of classes (to that each frame is classified) in advance, the problem is simple. You can create a simple relational database table that has columns equal to your classes. But what to do in a situation when your set of classes is not known (for example, you want to allow having some custom-defined classes).</p>
<p>This use case is optimal for using a document database (MongoDB) that does not require any prior knowledge about data structure. Technically, each video can have its table (called collection in MongoDB). </p>
<p>For this example, your document can follow the structure:</p>
<pre class="code"><code>{
    "_id": "39f49177-27f6-47a3-9ffe-c4c7a952b1b9",
    "video_stamp": 0.598,
    "classification": {
        "some_class": {
            "certainty": 0.8,
            "classified": true
        },
        "another_class": {
            "certainty": 0.63,
            "classified": false
        }
    }
}</code></pre>

<p>Regarding this structure, the certainty field indicates how sure the classification algorithm is with the classification to a concrete class (close to 1 means that title probably belongs to this class, close to zero that it does not).</p> 
<p>MongoDB is probably the most popular document database solution. Unfortunately, some changes in the license agreement make it a very commercial solution (which is still open-source).</p>
<h2>In-memory databases</h2>
<p>Databases like REDIS and Memcached are prevalent solutions for caching data. In addition, many applications like Celery (using REDIS for both task queue and storing of results) use in-memory databases (Django can use Redis for implementing channels and caching). It is very common to use in-memory databases for storing data that cannot be returned on-demand (for example, because of long latency problems).</p> 
<h3>Storing of results from workers in a publish-subscribe pattern</h3>
<p>A common challenge when using a publish-subscribe pattern is to make data accessible after their computation. For example, if you use Celery, you can return the task ID to the user's request. Users can then periodically hit some end-point with this task ID to check if the computation is finished and fetch results afterwards.</p>
<p>The most common approach to deal with the issue is to store data in an in-memory database (like REDIS) and make them accessible from it. It is also more common not to repeatedly hit any end-point to validate if the computation has finished but to use some notification. The most common way to notify a user about change is through web sockets (if your client is a web browser).</p> 
<p>REDIS is arguably the most popular in-memory database solution. It is open-source and available under a friendly BSD licence.</p>
<h2>Key-value databases</h2>
<p>These databases are beneficial in the authorization and authentication process. For example, they can help store things like authentication tokens, or generally tokens of various types (like toke for resetting passwords). In addition, some key-value databases support multiple keys (like Memcached, which is both in-memory and key-value database).</p>
<p>Generally, key-value datasets act as a dictionary (or map) returning some stored value for a given key. Solutions like Memcached allows you to store almost every type as a value, and requirements for the key are also not strict.</p>
<h2>Time series databases</h2>
<p>This form is practically identical to a traditional relational database, but the primary key is usually time series. This feature makes it helpful for storing some real-time observations (like some physical time dependant variables). The most common use-case is monitoring systems (monitoring traffic, temperature, bandwidth and other features in time). Time series (with data) can then be easily transformed (with some different binning, etc.) and shown in some graph. Tools like Graphana works precisely on this principle.</p>
<p>The most popular solution for time-series databases is InfluxDB. Some rudimentary form is available under MIT license - advanced application is proprietary software.</p>
<h2>Graph databases</h2>
<p>These databases are crucial when the relation between objects is being analyzed. There are many use-cases for this type of database. Arguably the most common are smart suggestions - showing product suggestions (for example, on some e-shop) based on the product you are currently analyzing. Another widespread use case is the relation between roles, groups and users (for authentication and security purposes). An optimized graph can make queries for such data much more effective than standard trees in a relational database. Analyzing relations between entities is also an underpinning principle of social networks.</p> 
<p>A prevalent solution for graph databases is neo4j (source codes are available, but technically, it is proprietary software). Also, from 2019 there is a standard for querying these databases (Graph Query Language).</p> 

<h2>Summary</h2>
<p>The most popular technology for document databases is MongoDB. Document databases are helpful when you need to store the whole structure (like JSON file) with minimal restrictions. In-memory databases are significant if it comes to caching. They allow the effective implementation of task queues or cache results from workers.  Key-value databases act as optimized mapping structure, that allows to store values with some key (or many keys) and load this value in optimized time. Key-value databases are often in-memory databases (which is the case of Memcache). Time-series databases help store observations and monitoring outputs (like some physical variables). Finally, graph databases are very important if you need to select objects based on a set of relations.</p>
"""

ENTITY = cr.Article(
    title="Most common use cases for NoSQL databases",  # noqa: E501
    url_alias='most-common-use-cases-for-nosql-databases',  # noqa: E501
    large_image_path="images/bigdata_big.jpg",
    small_image_path="images/bigdata_small.jpg",
    date=datetime.datetime(2021, 7, 18),
    tags=[cr.Tag('NoSQL', 'nosql'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="This article analyzes the most common use cases for well-known NoSQL databases (like document, in-memory, key-value, time-series and graph database solutions)."  # noqa: E501
)
