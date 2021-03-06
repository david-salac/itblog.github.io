# Design of the system for on-demand processing of the large datasets
import datetime
import crinita as cr

lead = """One of the common challenges of on-demand large datasets processing is the time required for data processing. The naive approach is to compute the operations on the same unit that serves results (and horizontally scale the system when it is overloaded). The more complex (and generally speaking the only right) approach is to use some asynchronous task queue based on distributed message passing (message broker)."""

content = """One of the common challenges of on-demand large datasets processing is the time required for data processing. The naive approach is to compute the operations on the same unit that serves results (and horizontally scale the system when it is overloaded). The more complex (and generally speaking the only right) approach is to use some asynchronous task queue based on distributed message passing (message broker).

<h2>The rationale behind this article</h2>
<p>As usually, developing web applications processing big data sets has its specifics. It is good to be aware of them, especially when you come from a different field of software engineering (like the development of desktop applications or web applications based on a relatively fast relational database). Often, when developers come from projects that mainly operate with small pieces of data (typically some information systems), they tend to use the most straightforward approach. It means to process all data and return the result in one call (by accessing some GET route in your system). That is in many cases acceptable - if you just access some database (or even file) that is perfectly optimized - you do not risk any timeouts (or some bad user experience). But, generally speaking, this approach is absolutely not acceptable if it comes to the processing of big data sets.</p>
<p>It is not rare to see a good developer who does not know the way how to deal with this issue. Often, even a time is a factor - create one route is much simpler than the whole asynchronous interface. So, even though your work is conceptually wrong, you accept this technological debt and publish it. In many start-ups companies that often do not attract the best candidates - using the mentioned incorrect approach can destroy your business. Your application becomes more or less useless as the number of users increases. It is though very helpful to know how to correctly proceed and what (ready-made) technologies to use to avoid this bitter scenario. Knowing how weird it might sound, it is important to start your project (even if it is just a proof of concept) using the correct approach. Often, it might be helpful to carefully study available open-source projects before you proceed to designing and implementing your solution. Also, it is good to study available for some most common tasks (like GeoServer, Celery, Apache Kafka and others).</p>

<h2>Why not use the naive approach? </h2> 
<p>The naive approach is schematically represented in the picture below. As you can see, the crucial part of the naive approach is the load balancer that distributes the tasks to workers, and returns in the same relation return the results back to users.</p>

<figure>
    <img alt="Figure 1: Naive approach" src="images/naive_approach.png">
    <figcaption>Figure 1: Naive approach</figcaption>
</figure>

<p>The bottle-neck of this approach is that response time is determined by the task complexity. For example, if you ask for processing of some large data (typically want to create some map), you have to wait till the computation is finished. This can cause significant trouble related to the connection (server connection timeout errors, etc.) and also increase the complexity of the logic running on the user side. No user can also connect to the worker during the computation, which reduces system throughput (and the number of users that can be connected simultaneously accordingly). To keep such a system, alieve is extremely expensive (the number of workers has to be increased linearly to the number of users).</p>

<p>The naive approach can, generally speaking, be considered as an anachronism and a flawed design approach. </p>

<h2>What is the correct approach? To use the task queues and message passing. </h2>
<p>The logic of the task queue approach is shown in the picture below (this figure is simplified). </p>

<figure>
    <img alt="Figure 2: Task queue approach" src="images/task_queues.png">
    <figcaption>Figure 2: Task queue approach</figcaption>
</figure>

<p>The logic is that there is just one (or a small number) light-weighted "front" worker (typically some web-application). This front-worker (interface) does not do any computations. It only handles requirements from the user. If a user wants to compute anything, all that front-worker does is that it creates a message (command/instruction) defining the task that is passed to the task queue (principally the traditional message broker). The task queue is just a queue of these instructions that are passed asynchronously to the workers (typically immediately after the worker finish the previous job). After the worker finishes the computation, results are stored in the database (typically some fast in-memory database) and the user is notified. Notification is typically sent separately by another entity (it can just send an email or some advanced notification, e. g. for the iOS system). When the user wants to see the results (after receiving the notification), it just asks the front-worker to fetch it (that is the simple task that can be done quickly and does not require any computation time).</p>

<h3>Pros of the task queue approach </h3>
<p>The main advantage of the presented approach is that front-worker is just a simple interface (web-application). This has a significant impact on the throughput of the system. User can connect whenever wanted and always receives the response. Another advantage is that tasks from the queue are passed asynchronously to the hard-workers that are accordingly always bussy (at least maximally busy). This again increases the throughput. Last but not least advantage is that system is more secure because the part exposed to the user is simpler.</p>
<h3>Available technologies </h3>
<p>It all depends on the solution that you choose. In the Python land, the simpler approach is to use Celery based (hard)-workers and RabbitMQ based task queues. Both are under open licences and use free and widely supported technologies for storing/accessing data (Redis / Memcached). The more heavy-weighted solution (mainly for the Java developers) is Apache Kafka that can operate as a standard message broker. Listeners (workers) can run some simple web framework (like Tomcat) for accepting the messages and Kafka offers the deserialization interface for accepted messages.</p>
<h2>Summary </h2>
<p>Two ways of dealing with big-data processing are presented here. One is using the naive approach with one heavy-weighted worker, and another one is to use a message broker (task queue) approach. The naive approach is not suitable for the practical problems (can only be used for proof of the concept work). Task queues approach is initially more difficult for implementation but is more flexible, and throughput of the system is bigger (as well as the security of the system). Even the price for deploying such a system is lower.</p>
"""

ENTITY = cr.Article(
    title="Design of the system for on-demand processing of the large datasets",
    url_alias='design-of-the-system-for-on-demand-processing-of-the-large-datasets',
    large_image_path="images/emails_big.jpg",
    small_image_path="images/emails_small.jpg",
    date=datetime.datetime(2020, 4, 26),
    tags=[cr.Tag('Task Queue', 'task-queue'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Performance', 'performance')],
    content=content,
    lead=lead
)
