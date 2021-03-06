# More about some useful concepts in Python language
import datetime
import crinita as cr

lead = """Cache represents a way how you can make your algorithm (whatever it is) work faster. Basically, it stores some outputs of your algorithm for some specific inputs (based on its policy) and when you ask your algorithm for something, it first checks if that information is stored in a memory (cache) so it can return it without performing any computations. If this logic succeeds (information is in memory) it is called a cache hit."""

content = """Cache represents a way how you can make your algorithm (whatever it is) work faster. Basically, it stores some outputs of your algorithm for some specific inputs (based on its policy) and when you ask your algorithm for something, it first checks if that information is stored in a memory (cache) so it can return it without performing any computations. If this logic succeeds (information is in memory) it is called a cache hit. On the other hand, if the information is not in memory, it is called a cache miss.
<p>
Naturally, you intend to have the highest cache hit ratio. The way how you can achieve it is determined by the size of memory that is dedicated to cache and cache replacement policy. There are other aspects in place as well (for example how fast cache memory is), but these theoretical aspects are typically something that you cannot change from the perspective of high-level programming.
</p>
<h2>Cache replacement policies</h3>
<p>Let's go a bit more to theory. There are many policies on how to cache your data (meaning what data you want to save in a particular context). The most important cache policies are LRU and MRU - there are many other policies, as you can find in this brilliant piece on <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies">Wikipedia (HERE)</a> (where I copied the following definitions).</p>
<h3>Least recently used (LRU)</h3>
<p>Discards the least recently used items first. This algorithm requires keeping track of what was used when - that is expensive if one wants to make sure the algorithm always discards the least recently used item. General implementations of this technique require keeping "age bits" for cache-lines and track the "Least Recently Used" cache-line based on age-bits. In such an implementation, every time a cache-line is used, the age of all other cache-lines changes. LRU is rather a family of caching algorithms.</p>
<h3>Most recently used (MRU)</h3>
<p>Discards, in contrast to LRU, the most recently used items first. For example, when a file is being repeatedly scanned in a (Looping Sequential) reference pattern, MRU is the best replacement algorithm. Also for random access patterns and repeated scans over large datasets (sometimes known as cyclic access patterns) MRU cache algorithms have more hits than LRU due to their tendency to retain older data. MRU algorithms are most useful in situations where the older an item is, the more likely it is to be accessed.</p> 
<h2>Practical usage of cache in Python language</h2>
<p>The good news is that there is a simple way how you can impose cache on some function in Python. But before we dive into this issue, let's briefly introduce decorators in Python.</p>
<h3>Decorator of function/method in Python</h3>
<p>Decorators are a helpful construct in Python. They allow you to modify the behaviour of some function or method (in Python 3.x also class). User-defined decorators are typically helpful for logging functionality or doing some pre/after-commit work.</p> 
<p>Consider the following example (of the most complex) decorator:</p>
<pre class="code"><code>def decorator_factory(argument):
    print(f"decorator_factory called with: {argument}")
    def decorator(function):
        print(f"decorator for fn: {function.__name__}")
        def wrapper(*args, **kwargs):
            print("wrapper start")
            # For example, modify parameters
            args = (args[0] + 1, args[1] + 2)
            # Call wrapped function:
            result = function(*args, **kwargs)
            print("wrapper end")
            return result
        return wrapper
    return decorator

@decorator_factory("whatever")
def some_function(x, y):
    print(f"some_function ({x}, {y})")

# Call our decorated function
some_function(2, 3)
some_function(6, 7)

# OUTPUTS:
# >>> decorator_factory called with: whatever
# >>> decorator created for fn: some_function
# >>> wrapper start
# >>> some_function (3, 5)
# >>> wrapper end
# >>> wrapper start
# >>> some_function (7, 9)
# >>> wrapper end</code></pre>
<p>This example is the most complex decorator you can create. It has its arguments, and you can as well modify the function behaviour (and its arguments).</p> 
<p>As you probably already know, there are many build-in decorators in Python, as well as many decorators created in Python's libraries.</p>
<h3>Decorator <code>lru_cache</code> in <code>functools</code> package</h3>
<p>Decorator for function <code>lru_cache</code> in <code>functools</code> package (this package is a system package, so you do not have to install anything) is the easy-to-use implementation of LRU cache. The decorator itself takes a few parameters. The most important one is maxsize that defines the size of the cache. It also provides some additional functionality that can be called on function (as to object) to see some statistics (<code>cache_info</code>) or to clean cache(<code>cache_clear</code>). The following example demonstrates everything you need to know:</p>
<pre class="code"><code>import functools
import random  # To test if cache works

@functools.lru_cache(maxsize=128)
def some_function(attr):
    return random.randint(0, 100) * attr

print(some_function(4))  # Some random output
print(some_function(5))  # Some random output
print(some_function(4))  # Same output as above (OK)
print(some_function(5))  # Same output as above (OK)

# Print statistics
print(some_function.cache_info())
# >>> CacheInfo(hits=2, misses=2, maxsize=128, currsize=2)

# Clear cache
some_function.cache_clear()
print(some_function.cache_info())
# >>> CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
print(some_function(4))  # A totally new output</code></pre>
<p>The important note is: you can use <code>lru_cache</code> from <code>functools</code> only to stand-alone functions and the static method of a class. Never to standard class methods. The reason why you cannot use <code>functools</code>' <code>lru_cache</code> decorator for a standard method is that it is related to the whole class and not to an instance. This can cause memory leaks and unexpected behaviour. Consider the following example:</p>
<pre class="code"><code>import functools
import random

class SomeClass(object):
    @functools.lru_cache(maxsize=3)
    def some_method(self, argument):
        return random.randint(0, 500) * argument

obj_a = SomeClass()
print(obj_a.some_method(4))
obj_b = SomeClass()
print(obj_b.some_method(4))
print(obj_b.some_method.cache_info())
# >>> CacheInfo(hits=0, misses=2, maxsize=3, currsize=2)
# => See a problem here: currsize=2 instead of 1 !!!</code></pre>
<p>As you can see in this example, attribute <code>currsize</code> has value 2 after a call on a totally different object. This is unexpected behaviour because you would normally expect value 1 (as you want to have cache on method related to instance but not to the whole class).</p> 
<h3>Decorator <code>lru_cache</code> in <code>methodtools</code> package</h3>
<p>Fortunately, there is a simple fix for this memory-leaking <code>lru_cache</code> decorator from <code>functools</code>. That is to use a different library called <code>methodtools</code>. This library is not a system package, so you have to install it (simply using <code>pip install methodtools</code>). The behaviour of this function in <code>methodtools</code> library is exactly the same as in <code>functools</code>. The only difference is that it works correctly. Consider the following example:</p>
<pre class="code"><code>import methodtools
import random

class SomeClass(object):
    @methodtools.lru_cache(maxsize=3)
    def some_method(self, argument):
        return random.randint(0, 500) * argument

obj_a = SomeClass()
print(obj_a.some_method(4))
obj_b = SomeClass()
print(obj_b.some_method(4))
print(obj_b.some_method.cache_info())
# >>> CacheInfo(hits=0, misses=2, maxsize=3, currsize=1)
# => Great!!! Now it works correctly.</code></pre>

<p>The drawback of <code>methodtools</code> library is that it contains quite a few sub-dependencies (which can generally speaking cause issues).</p>

<h2>Summary</h2>
<p>The article presents some theory behind caching and then practical examples of caching in Python language using <code>functools</code> and <code>methodtools</code> <code>lru_cache</code> decorator. Caching is generally helpful for making your code run faster. Of course, it is convenient to have some support functionality on the language level. It is good to know about the unexpected behaviour of <code>lru_cache</code> in <code>functools</code> (memory leaks) and the way how to overcome it. You can always easily implement your cache logic as well (as the key for dictionaries can be almost everything) and not rely on available tools.</p>
"""

ENTITY = cr.Article(
    title="A bit more about cache and the way how to implement it in Python",
    url_alias='a-bit-more-about-cache-and-the-way-how-to-implement-it-in-python',
    large_image_path="images/cache_big.gif",
    small_image_path="images/cache_small.gif",
    date=datetime.datetime(2021, 3, 27),
    tags=[cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="The article presents some theory behind caching and then practical examples of caching in Python language using functools and methodtools lru_cache decorator."  # noqa: E501
)
