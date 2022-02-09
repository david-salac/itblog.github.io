# Practical aspects of asynchronous programming in Python
import datetime
import crinita as cr

lead = r"""Multitasking and multiprocessing are the two main components of parallel programming. There is native support for these features in Python (CPython). But there are some limits specific to Python that have to be considered. The main problem is called GIL (Global Interpreter Lock) - which significantly reduces the number of use cases for applications in Python (mainly for creating asynchronous pipelines)."""

content = r"""<p class="lead">Multitasking and multiprocessing are the two main components of parallel programming. There is native support for these features in Python (CPython). But there are some limits specific to Python that have to be considered. The main problem is called GIL (Global Interpreter Lock) - which significantly reduces the number of use cases for applications in Python (mainly for creating asynchronous pipelines).</p>

<h2>What is asynchronous programming?</h2>
<p>Asynchronous programming is based on an important concept of using threads. Thread is basically a lightweight task. The difference between task and thread is more or less formal - the operating system creates tasks as a separate entity with its own memory space while it creates threads with the shared memory. It means that the allocation and running of a thread are generally faster and less resource-hungry than the running of the task. On the other hand, tasks can be more helpful for complex algorithms (they essentially behaves as a separate program).</p>
<p>Many programming languages provide the standard interface for dealing with tasks and threads. Python is not an exception. There are multiple ways how to deal with asynchronous programming - either by using the standard libraries like multiprocessing (process-based parallelism) and threading (for thread-based parallelism), or you can use an improved version for thread-based parallelism called asyncio (there is a complete interface for using asyncio with many new keywords).</p>

<h2>Global Interpreter Lock (GIL) and pipelines</h2>
<p>The GIL is a famous limitation for asynchronous programming in Python. It practically means that the CPython interpreter imposes a lock on every variable that is used by the particular thread. Lock basically means that only one thread can use the given (locked) variable at the moment. It practically makes standard multithreading programming in Python (based on CPython) useless - with one important exception. This exception is the implementation of pipelines.</p>
<p>Asynchronous pipelines are an important concept (not only for Python). They are helpful if you can split your task (algorithm) into multiple sub-tasks (sub-algorithms) and process them separately. The most common use case is processing some massive datasets that have to be fetched somewhere from the network, processed and then pushed back. In this case, you have a pipeline composed of three steps (fetching, processing, pushing). Such a pipeline is a very common use case in the data processing world.</p> 
<p>But back to the GIL - you cannot do the standard operations, like processing one big array by multiple threads (as the array is locked by each thread and another thread have to wait until the lock is released).</p>

<h2>Library asyncio</h2>
<p>The library asyncio provides a simple interface for dealing with thread-based parallelism in Python. It allows you to create parallel threads and implement pipelines.</p>
<p>If you want to run some function concurrently (using asyncio), you need to declare it as async function. It behaves otherwise exactly the same as a standard function in the algorithm - such a function is called coroutine. You also have to define an event loop - that is basically another function declared as async - it is responsible for calling other coroutines. Note that you cannot run coroutine from a standard code - each coroutine has to be called from either another coroutine or event loop. Suppose you want to call the event loop from your application. In that case, asyncio has an embedded function asyncio.run that accepts coroutine (or event-loop) with its arguments (it looks like a standard call).</p> 
<p>You must use the keyword await to synchronously call a coroutine from another coroutine (or event loop). If you need to call your function asynchronously, you must create a task as a first step. There is a function asyncio.create_task for this purpose.</p>

<h3>Example with pipelines</h3>
<p>As mentioned above - there are two main use cases for asynchronous tasks in Python. The first is the simple task where you do not care much about the outputs (or you have many mutually unique tasks that do not share any data). Another case is a pipeline. A pipeline is composed of multiple steps. The output of each step is an input of the next step. The example below demonstrate these most common use cases:</p>

<pre class="code"><code>import asyncio
import time


# Coroutine
async def some_function(x):
    if x is None:
        return
    # Sleep to one second (runs synchronously)
    await asyncio.sleep(1)
    return x * 7


# The event loop (for some simple example)
async def simple_example():
    # This run some_function synchronously
    await some_function(9)

    # To run some_function concurrently
    task_1 = asyncio.create_task(some_function(8))
    task_2 = asyncio.create_task(some_function(9))

    # Wait until it finishes and fetch the results
    result_1 = await task_1
    result_2 = await task_2
    print(result_1, result_2)


# The event loop (with pipeline)
async def pipeline():
    time_start = time.time()  # to measure elapse time

    # Input for the first step
    pipe_in = [9, 10, 11, 12]
    # Input for the second step
    in_2 = None
    # Input for the third step
    in_3 = None
    # Final result
    pipe_outputs = []

    for idx in range(len(pipe_in) + 2):  # 3 steps of pipeline
        # Create input for the pipeline
        in_1 = None
        if len(pipe_in) > idx:
            in_1 = pipe_in[idx]
        # Create and run all steps simultaneously
        task_step_1 = asyncio.create_task(some_function(in_1))
        task_step_2 = asyncio.create_task(some_function(in_2))
        task_step_3 = asyncio.create_task(some_function(in_3))

        # Fetch results from each step
        #   result of each step is input of the next step
        in_2 = await task_step_1
        in_3 = await task_step_2
        pipe_outputs.append(await task_step_3)

    print(pipe_outputs)
    # >>> [None, None, 3087, 3430, 3773, 4116]

    print(f"Elapse time: {time.time() - time_start} s")
    # Is around 6 seconds => it really runs concurrently


# Start the event loop
asyncio.run(simple_example())
asyncio.run(pipeline())</code></pre>

<p>Although this example is rather artificial - it shows everything you need to know about asynchronous development in Python (when using asyncio library).</p>

<h2>Multithreading using threading library</h2>
<p>Another way to achieve the same effect is to use a threading library. This is a built-in Python library motivated by Java. The important functional difference between threading and asyncio is that asyncio threads never give up control, which makes sharing resources a bit safer (particularly helpful if you need to read some data from a network connection). When using a threading library, you can achieve the same effect. Still, it requires locks, making code fragile.</p>
<p>The following example that uses a threading library is artificial. However, it shows how threads are created and typical use-case (when shared variables are class members). If you are familiar with languages like Java, this code might seem familiar to you.</p>
<pre class="code"><code>import threading
import time


class AsyncCounter(object):
    def __init__(self, val):
        self.val = val

    def increment_val(self, nr):
        # Force to wait for 1 sec
        time.sleep(1)
        # Increment the value
        self.val += nr


cnt = AsyncCounter(3)
# Create the thread object
thr = threading.Thread(
    # Reference to method / function
    target=cnt.increment_val,
    # Arguments for call
    args=(4, )
)
# Trigger the thread
thr.start()
# Check the thread status
print(thr.is_alive())  # >>> True (running)
# Print all threads related to program
print(threading.enumerate())
# >>> [<_MainThread(MainThread, started 26116)>,
#      <Thread(Thread-1 (increment_val), started 26456)>]
# Print the number of active threads
print(threading.active_count())  # >>> 2
# Wait till the thread finishes
thr.join()
# Check the thread status
print(thr.is_alive())  # >>> False (finished)
# Print the incremented value
print(cnt.val)</code></pre>

<p>In the example, you can see many basic classes and methods of the threading library. Obviously, the most important class is Thread itself. It encapsulates a thread. There are many helpful methods related to the Thread object - the most important is the start method (which triggers the thread), another method (is_alive) tells you whether the thread is still running. To synchronize threads, you can use the method join. Other functions from the threading library are helpful to monitor threads related to the program - like active_count (returning number of concurrently running threads) or enumerate (returning Thread's objects directly).</p>

<h3>Triggering multiple threads simultaneously</h3>
<p>If you aim to start multiple threads simultaneously, wait till they finish their work and then fetch results, there are two options. You can either use an array of Thread objects, start them, or call the join method. Or you can use class ThreadPoolExecutor in the concurrent.futures package. The typical usage looks like this:</p>
<pre class="code"><code>import time
from concurrent.futures import ThreadPoolExecutor


def some_fn(val):
    time.sleep(1)
    # Process the value value
    print(val, end=' ')


with ThreadPoolExecutor(max_workers=3) as ex:
    ex.map(some_fn, [1, 2, 3])

print("end")
# >>> 2 1 3 end</code></pre>
<p>As you can see, the context decorator joins all threads in the end.</p>

<h3>Multithreading and library queue</h3>
<p>The essential concept related to multithreading is asynchronous event handling. Python has a library queue that can act as a container for events (the program can asynchronously add objects to the Queue object). The logic is that a thread monitors the queue's content, and whenever it is not empty, it processes items inside it.</p>
<p>The example below shows the simple event processing where events are added into the queue asynchronously during the processing of the first event.</p>
<pre class="code"><code>import threading
import time
import queue


class EventDefinition(object):
    def __init__(self, val):
        self.val = val

    def event_operation(self, nr):
        # Force to wait for 1 sec
        time.sleep(1)
        # Increment the value
        self.val += nr


q = queue.Queue()
# Add the first item into the queue
q.put(EventDefinition(0))


def event_handler(nr: int):
    # The loop can be replaced with:
    # while True:
    while not q.empty():
        # Fetch object from queue
        obj: EventDefinition = q.get()
        # Perform operation
        obj.event_operation(nr)
        print(obj.val)
        # Report the end
        q.task_done()


thr = threading.Thread(
    target=event_handler,
    args=(3,)
)
thr.start()
# Fill the queue with events for processing
for _val in range(10):
    # This represents some asynchronously
    #   coming events
    q.put(EventDefinition(_val))

thr.join()</code></pre>
<p>The event handler method contains an infinite loop in practice. Also, tasks are usually added to the queue at a random time.</p>

<h2>Process-based parallelism</h2>
<p>The main disadvantage of process-based parallelism is the overhead of creating the process (and fetching results from the process). This makes processes helpful almost exclusively only for very long-running algorithms (such that it takes a lot of time to process) or for special use cases (publish-subscribe pattern).</p> 
<p>The native Python contains a built-in library called multiprocessing. That contains all tools needed to create multiple processes (especially queues and encapsulation of processes as tasks). But generally speaking, this library is a bit fragile (in terms of portability), and unless you know what you are doing, it is better to avoid it.</p>
<p>Another approach is to use permanent workers that are idling and waiting for some task sent from the master process. This is an example of a publish-subscribe pattern. The typical use case is some web application that does some computations that consumes a lot of resources (or just take a lot of time). In this case, you need to separate them from the main platform (as you cannot afford to wait because of the risk of timeouts).</p>
<p>Arguably the most popular tool for this purpose is called Celery. It allows you to use queues in a very native way. Celery is perfect for simple applications - like sending an email or doing some time-consuming queries on a database. However, if you want to use Celery for more complex applications, you have to expect troubles (especially when you want to spin up multiple workers based on requirements dynamically).</p>


<h2>Summary</h2>
<p>This article presents the most important features of asynchronous programming in Python. Namely, the libraries asyncio and threading (and explain differences). It allows you to implement simple multithreading tasks and complex pipelines. Limits for multiprocessing in Python (CPython) related to GIL (Global Interpreter Lock) are also presented. Some other approaches are discussed as well (like multiprocessing and how to implement the publish-subscribe pattern using Celery).</p>
"""

ENTITY = cr.Article(
    title="Practical aspects of asynchronous programming in Python",
    url_alias='practical-aspects-of-asynchronous-programming-in-python',
    large_image_path="images/asyncio_big.jpg",
    small_image_path="images/asyncio_small.jpg",
    date=datetime.datetime(2021, 5, 16),
    tags=[cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="Asynchronous programming in Python has some specific. A developer is limited by GIL and effectively the only reasonable application is using the pipeline logic."  # noqa: E501
)
