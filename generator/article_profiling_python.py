# Helpful tools for code profiling in Python
import datetime
import crinita as cr

lead = """Code profiling is one of the most important parts of the code optimisation process. Generally speaking, it is the program analysis where we are mainly interested in memory usage and time complexity of the program (or each of its part). We can also be interested in how often we use some function (or how often we call it, what's the duration). There are a lot of principles and tools to perform these tasks."""

content = """Code profiling is one of the most important parts of the code optimisation process. Generally speaking, it is the program analysis where we are mainly interested in memory usage and time complexity of the program (or each of its part). We can also be interested in how often we use some function (or how often we call it, what's the duration). There are a lot of principles and tools to perform these tasks. This article is mainly focused on stack tracing, line-by-line code analysis tools, and function call graphs.

<h2>Stack trace (aka stack backtrace or backtrace) sampling</h2>
<p>Stack trace sampling represents one of the fundamental principles of program profiling. The basic principle is that the algorithm sample program's stack (stack trace) in some reasonable frequency. In the end, we can analyse the running time of each block and its memory usage.</p>
<p>Consider the following code (which is massively ineffective):</p>
<pre class="code"><code>def c(input):
    out = 0
    for i in range(4000):
        out += i * 7 * input
    return out


def b(input):
    out = 0
    for i in range(4000):
        out += i * 5 * input
    out += 5 * c(input)
    return out


def a(input):
    out = 0
    for i in range(8000):
        out += i * 3
    out += i * 3 * b(input)
    return out
</code>
</pre>
<p>Simplified stack of the program (that calls the function 'a') would follow the logic:</p>
<pre class="code"><code>[() <- beginning of the code]
[(a) <- function 'a' is called]
[(a, b) <- function 'a' call the function 'b']
[(a, b, c) <- function 'b' call the function 'c']
[(a, b) <- function 'c' returns the result to 'b']
[(a) <- function 'b' returns the result to 'a']
[() <- function 'a' returns a result]
</code></pre>
<p>This stack is simplified because there is also a lot of other operations (arithmetic operators, print statements, loops etc.), but it captures the main purpose of the stack.</p>

<h3>Visualisation of the stack trace sampling (for running time)</h3>
<p>If we are interested in the performance optimisation, we need to see the time consumption of each block. The figure typically looks like this:</p>

<figure>
    <img src="images/profile_abc.png" alt="Figure 1: Logic of stack-trace">
    <figcaption>Figure 1: Logic of stack-trace</figcaption>
</figure>

<p>where there is a time on the horizontal axis and the stack depth on the vertical one (in this case going down).</p>

<h3>How to plot figures like this in Python (cProfile, snakeviz, vprof)</h3>
<p>Python has a built-in profiler called cProfile. This profiler documents the running time of each block in the program (alas not the memory usage). It can be called directly using the command:</p>
<code>python -m cProfile -o {OUTPUT}.dat {PROGRAM}.py</code>
<p>where the {OUTPUT} should be replaced by the path to the output data file and the {PROGAM} is the script that is the subject of the profiling.</p>
<p>There are many tools for visualisation of the outputs. Arguably the most popular one is called snakeviz. It can be installed using pip (pip install snakeviz). It is a web application that visualises the profiler output (received by cProfile) as an interactive graph. To call the SnakeViz, use simply the command:</p>
<code>snakeviz {OUTPUT}.dat</code>
<p>Output window of the SnakeViz looks like:</p>

<figure>
    <img src="images/snakeviz.png" alt="Figure 2: Snakeviz output">
    <figcaption>Figure 2: Snakeviz output</figcaption>
</figure>

<p>Another very popular tool that does the same is called vprof. It can be again simply installed using pip (pip install vprof) and called using logic:</p>
<code>vprof -c cmh "{PROGRAM}.py"</code>
<h3>What do we want to achieve?</h3>
<p>Our main objective during the optimisation process is to shrink all the blocks as much as we possibly can.</p>

<h3>Memory stack trace sampling</h3>
If it comes to memory profiling, there is currently no equivalent tool in Python for visualisation of the memory usage in the stack trace sampling logic. The only option is to use the line-by-line analysis. Closest to this is the package guppy3 presented bellow.

<h2>Line-by-line analysis</h2>
<p>This type of analysis is a kind of cavemen approach. We basically measure the memory usage and the running time of each line in our code. In this case, one has to be aware of the impact that measuring itself has on the measured data (line-by-line analysis is susceptible). The output of memory profiling is typically just a table containing line number and matching value.</p>
[Memory profiler output example]
<pre class="code"><code>Line #    Mem usage    Increment   Line Contents
================================================
     5     14.3 MiB     14.3 MiB   @memory_profiler.profile
     6                             def profiled_fn():
     7     14.3 MiB      0.0 MiB       a(9)
</code></pre>

<h3>Memory profiling in Python (package memory-profiler)</h3>
<p>The output of line-by-line memory profiling is the vector that contains the value of used memory for each line of measured code. In Python, there is a library called memory-profiler that can be easily installed by pip (pip install memory-profiler). The simplest model is to profile concrete function using the decorator "profile":</p>
<pre class="code"><code>import memory_profiler

from application import a

@memory_profiler.profile
def profiled_fn():
    a(9)


if __name__ == '__main__':
    profiled_fn()
</code></pre>

<p>The output of this profiling is the table shown above.</p>

<p>Slightly more complex usage of the memory-profiler (usable for further processing) is to use the method "memory_usage":</p>
<pre class="code"><code>import memory_profiler

from application import a, b, c


def measured_function(arg):
    print(a(arg))
    print(b(arg))
    print(c(arg))


# Measure the memory usage
mem_usage: list = memory_profiler.memory_usage((measured_function, (5, )))
</code></pre>
<p>This function returns an array that contains memory usage of each line (indexed from 0). Using the memory_usage function is incredibly helpful for analysing the code memory requirements for different inputs.</p>
<p>It is good to know that there is some mandatory memory usage about 100 MB required by Python (this has to be considered as a constant). Memory usage accepts two parameters, one is the pointer to the function, and another one is the tuple of arguments.</p>

<h3>Visualisation of the line-by-line memory profiling in Python</h3>
<p>After you receive the vector with values, you can use all standard approaches for plotting graphs in Python (like pyplot). Slightly more complex visualisation is available in the vprof (described above). If you choose to use vprof, you, unfortunately, cannot scale the problem by any argument (it just shows you the memory consumption line by line of script that you have called).</p>

<h3>Package guppy3 for advanced memory profiling</h3>
<p>Package guppy3 (installable via PIP: pip install guppy3) represents a slightly more sophisticated approach for analysing of the program memory usage. It shows a more in-depth analysis of the heap state, including data types of the objects there (unfortunately, only the basic type are reflected). You can as well use the complex API to access all measured values. To use guppy3 follow the logic:</p>
<pre class="code"><code>import guppy

from application import a, b

# Do some logic
a(9)
# Create a point for the analysis
point_0 = guppy.hpy()
# Do different logic
b(7)
# Creates another point:
point_1 = guppy.hpy()

# Print the analysis
print(point_0.heap())
print(point_1.heap())
</code></pre>
where "<code>point_0 = hpy()</code>" creates you a point where the analysis of the heap is committed. For printing the analysis, you can call the function "<code>point_0.heap()</code>" on the object (or you can use deeper analysis tools described in the <a href="https://github.com/zhuyifei1999/guppy3">documentation on GitHub</a>). Typical output looks like:
<pre class="code"><code>Partition of a set of 39738 objects. Total size = 4574417 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10694  27   976147  21    976147  21 str
     1   9808  25   718032  16   1694179  37 tuple
     2    557   1   456456  10   2150635  47 type
     3   2441   6   352832   8   2503467  55 types.CodeType
     4   4854  12   336978   7   2840445  62 bytes
     5   2304   6   313344   7   3153789  69 function
     6    557   1   268024   6   3421813  75 dict of type
     7    248   1   184800   4   3606613  79 dict (no owner)
     8     99   0   183152   4   3789765  83 dict of module
     9    288   1    96256   2   3886021  85 set
<115 more rows. Type e.g. '_.more' to view.></code></pre>
As you can see, guppy3 covers everything available in memory_profile package plus offers slightly deeper inside.

<h2>Function dynamic call graphs</h2>
<p>A call graph (aka call multigraph) shows the flow of the application. Basically, it visualises what each function call based on a given input. It is an incredibly helpful tool for simplifying of the code (reducing the number of function calls). The typical flow looks like this:</p>

<figure>
    <img src="images/call_graph.png" alt="Figure 3: Call-graph example">
    <figcaption>Figure 3: Call-graph output example</figcaption>
</figure>

<h3>Creating the call graph figure in Python</h3>
<p>Although it seems to be a trivial task (which it surprisingly is not), there is currently no robust tools that can create a call graph. The closest to this goal is the package called pycallgraph2 (pip install pycallgraph2). To make it work it also requires system package called graphviz (on Debian installable via apt install graphviz).</p>

<p>To create the graph, you need to commit:</p>
<code>pycallgraph graphviz -- {PROGRAM}.py</code>
<p>The script generates the PNG file (pycallgraph.png) that looks like the graph illustrated in the figure above. Another way how to use pycallgraph is to use it inside the source code. </p>
<pre class="code"><code>from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

from application import a

with PyCallGraph(output=GraphvizOutput()):
    # Code to profile:
    a(9)
</code></pre>

<p>Real problems are typically so complicated that generated figure is not easily readable (generated objects are massive). The script is also very susceptible and cannot handle many useful things (multithreading and multitasking, a lot of external libraries, etc.).</p>

<h2>Summary</h2>
<p>There are many similar tools for code profiling. It is, however, always good to bear in mind that measuring itself changes a code behaviour (always true). This article summarises some essential tools available in Python for code profiling. For the performance (run time) profiling it is cProfile + snakeviz or vprof. For the profiling of memory usage, it is the package memory-profiler and guppy3. If it comes to the dynamic call graphs, it is mainly the package pycallgraph2. All presented packages are available through PIP (the pycallgraph2 also requires one system package). </p>

<h2>Related GIT repo</h2>
<p>All used source codes are available in the REPO: <a href="https://github.com/david-salac/python-memory-profiling">GIT repo</a></p>

"""

ENTITY = cr.Article(
    title="Helpful tools for code profiling in Python",
    url_alias='helpful-tools-for-code-profiling-in-python',
    large_image_path="images/profiling_big.jpg",
    small_image_path="images/profiling_small.jpg",
    date=datetime.datetime(2020, 4, 16),
    tags=[cr.Tag('Data Visualisation', 'data-visualisation'),
          cr.Tag('Profiling', 'profiling'),
          cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Performance', 'performance')],
    content=content,
    lead=lead
)
