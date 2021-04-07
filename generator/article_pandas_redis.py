# Acceleration of frequently accessed constant multidimensional values in Python using REDIS
import datetime
import crinita as cr

lead = """One of the common challenges in data processing is to provide quick access to constants (or map of constants) stored in tables. This structure is typically useful to store multidimensional look-up tables (LUT). One of the most user-friendly (or rather programmer-friendly) ways how to store multidimensional (generally 2D) objects in Python is to use Pandas library and DataFrames objects."""

content = """One of the common challenges in data processing is to provide quick access to constants (or map of constants) stored in tables. This structure is typically useful to store multidimensional look-up tables (LUT). One of the most user-friendly (or rather programmer-friendly) ways how to store multidimensional (generally 2D) objects in Python is to use Pandas library and DataFrames objects. This article is about performance optimization of access to these data using the REDIS in-memory database system.

<h2>Using of Pandas' DataFrame</h2>
<p>DataFrames in Pandas library represents a suitable way how to store 2D structures in Python. There is a simple way how to index data using column and row indices. Pandas library is also deeply related to NumPy library and data from DataFrame can be easily converted to NumPy and vice versa. The simplest 2D DataFrame can be created in the following logic:</p>
<pre class="code"><code>import pandas as pd
df = pd.DataFrame(data=NUMPY_ARRAY, 
                  columns=[col1, col2, ...], 
                  index=[row1,row2,...])
</code></pre>
<p>
where NUMPY_ARRAY is a 2D array in NumPy (or just in plain Python), columns argument defines columns descriptor, and index argument defines row descriptors. For storing of multidimensional data (more than 2D), there is a simple construct in Pandas called MultiIndex. Consider following (simple) example:
</p>
<pre class="code"><code>df = pd.DataFrame(
    data=NUMPY_ARRAY, 
    columns=[col1, col2, ...], 
    index=[[row1,row2,...], [idx1, idx2,...]]
)
</code></pre>
<p>
Data here are accessible using column key and set of 2-row keys (which is technically 3D). In this way, it is possible to use as many dimensions as required. The more sophisticated way how to index data is to use MultiIndex class directly, which offers a lot of possibilities.
</p>
<h2>Performance issue</h2>
<p>The critical question is how to access stored data quickly, especially when they are repeatedly accessed in key infrastructure. To do this there is a simple way how to store the content of the DataFrame using serialization technology called MSG. This approach is currently the fastest native way of how to serialize large DataFrame objects. It is roughly 10 times faster than using Pickle which is another native way how to serialize objects in Python. Another issue when Pickle is used is that it does not support different output streams, but you can only save the output in a file.</p>
<p>
A typical way where to store the serialized object is on the local drive. The disadvantage of this when it is used in high-performance applications is evident. To avoid these delays, we suggest using the REDIS in-memory database for storing the serialized DataFrames.  There is also a lot of other advantages when the values are stored in the in-memory system rather than on hard disk - typically the throughput of the system is higher (data can be accessed more frequently).
</p>
<h3>Using REDIS in-memory database</h3>
<p>For accelerating access to stored data, it is generally speaking convenient to store them in memory. The REDIS system offers the possibility of a fast distributed in-memory database. The way how to use REDIS with MSG is straight-forward. </p>

<p>For storing the data use following logic:</p>
<pre class="code"><code>import redis
import pandas as pd
# ... code
# Connect to redis:
connector = redis.StrictRedis(host="?", 
                              port=?, 
                              password="?")
connector.set("key-in-redis", dataframe.to_msgpack())
</code></pre>
<p>
For reading the data use following logic:</p>
<pre class="code"><code>import redis
import pandas as pd
# After connecting to the REDIS (described above):
data_frame = connector.get("key-in-redis")</code></pre>
<p>
These examples illustrate the simplest way of how to store data in REDIS and access them. It is possible to use every other method in REDIS as well to work with the binary stream from MSG.
</p>
<h3>Performance analysis</h3>
<p>We performed some basic measurement of time that is required for fetching data from memory and deserialize them back to the DataFrame object. The processor Intel Xeon CPU E5-2673 v4 @ 2.30 GHz has been used during measurement. Data are depicted in the following table:</p>

<table>
<tr><th style="padding-right: 20px">Number of entities </th><th style="padding-right: 20px"> Time [s] </th><th> Standard deviation of time [s]</th></tr>
<tr><td style="padding-right: 20px">100,000 </td><td style="padding-right: 20px"> 0.003 </td><td> 0.002</td></tr>
<tr><td style="padding-right: 20px">500,000  </td><td style="padding-right: 20px"> 0.016  </td><td> 0.005</td></tr>
<tr><td style="padding-right: 20px">1,000,000  </td><td style="padding-right: 20px"> 0.034  </td><td> 0.012</td></tr>
<tr><td style="padding-right: 20px">5,000,000  </td><td style="padding-right: 20px">0.369  </td><td>0.037</td></tr>
<tr><td style="padding-right: 20px">10,000,000  </td><td style="padding-right: 20px">0.860  </td><td> 0.021</td></tr>
<tr><td style="padding-right: 20px">50,000,000  </td><td style="padding-right: 20px"> 4.324  </td><td> 0.041</td></tr>
</table>

<p>The first column in this table represents the number of entities in a DataFrame (is equal to the number of rows multiplied by the number of columns). The second column is the most important one - represents the time that is needed to fetching and deserializing values from REDIS back to the DataFrame. The third column is the standard deviation of the measured values. For every case,  exactly ten measurements are done.</p>
<p>
It is evident that up to one million entities, there is no significant delay in the overall process. On selected technology, this is also a cutting edge for the optimal size of the stored tables. It means that below this value user experience is not affected by the long time needed for receiving values.
</p>

<h2>The general use-case for REDIS</h2>
<p>The biggest drawback of the presented example is the time that is needed for serialization and deserialization. This can be overcome if you use some native formats - like nD symmetric numeric arrays - which can be natively serialized to REDIS. Although REDIS does not support n-dimensional arrays, you can simply overcome this issue by mapping it to a 1D array (as the physical representation in memory is always a one-dimension array). Though languages like Java, Go or C/C++ are much better for serving this purposes, you can achieve the same effect (it means fast serialization) in Python as well.</p> 
<p>If it comes to the special case of geospatial data - be aware of the potentially bigger size of these data sets. It can be a big hurdle in the successful speeding up of your system using the in-memory database approach. Technically, you can achieve slightly bigger performance for prices that are many times bigger. It is thought necessary to thoroughly test the requirements for your system. Do not believe that you can easily leave a broker-consumer approach by deploying in-memory databases. Even having all needed in memory does not necessarily make things many times faster - many other things have to be taken into an account. Particularly, having the correct dimension order of your data is especially important if it comes to performance.</p> 
<p>Also, another thing that might be potentially critical, is the correct infrastructure. If your REDIS instance runs somewhere distantly - be prepared that the performance increase might be very low (in many cases much lower than when a monolithic approach with a fast disk is used). To make the most of this logic - memory has to be on the same machine as your processing scripts. That is potentially a big hurdle when many instances are deployed (as you need to replicate data for each of them). </p>

<h2>Conclusions and further research</h2>
<p>This article proves that storing a map of constants using REDIS in-memory database and Pandas DataFrame in Python is a suitable way how to accelerate the overall performance of the system. It is also shown that the cutting value of the table size is one million elements for Intel Xeon CPU E5-2673 v4 @ 2.30 GHz processor. Above this value, user-experience could be affected. Accordingly, it is meaningful to split larger tables to tables of this size. It would be useful to check the behaviour of other in-memory database systems (such as Memcached) and compare the performance behaviour of all among others.
</p>
"""

ENTITY = cr.Article(
    title="Acceleration of frequently accessed constant multidimensional values in Python using REDIS",
    url_alias='acceleration-of-frequently-accessed-constant-multidimensional-values-in-python-using-redis',
    large_image_path="images/frequency_big.jpg",
    small_image_path="images/frequency_small.jpg",
    date=datetime.datetime(2019, 2, 3),
    tags=[cr.Tag('Pandas', 'pandas'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('REDIS', 'redis')],
    content=content,
    lead=lead
)


