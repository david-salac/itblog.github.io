# Dimension order problem when storing big data
import datetime
import crinita as cr

lead = """One of the common challenges when dealing with big multidimensional data sets is how effectively store them. There are many problems to deal with, but maybe the most important is choosing the proper dimension order. Although typically, the selection of the optimal dimensional order does not impact the size of the output file (if you use some compression situation that may differ), it has a profound effect on the response time when accessing stored data."""

content = """<p class="lead">One of the common challenges when dealing with big multidimensional data sets is how effectively store them. There are many problems to deal with, but maybe the most important is choosing the proper dimension order. Although typically, the selection of the optimal dimensional order does not impact the size of the output file (if you use some compression situation that may differ), it has a profound effect on the response time when accessing stored data.</p>

<h2>What is the optimal rule to follow when choosing the dimension order?</h2>
<p>Note that this section considers only dealing with multidimensional data (at least two or three dimensions). In that case, there often is a simple rule to follow. First of all, you need to know the form of your typical selecting (or writing) request in advance. Then, there are a few things to consider:</p>
<ol>
    <li>Do you often select just one point most of the time?</li>
    <li>Do you often select the data series only at one dimension?</li>
    <li>Do you follow any pattern when selecting data in more than one dimension?</li>
</ol>
<p>Generally, the first case is the best one as it almost does not matter what dimension order you choose. More precisely, the most convenient thing is to select the dimension order equivalent to the input (usually something in the memory you want to store) - it makes writing fast without affecting the reading rate (win-win strategy on each side).</p>
<p>The second case is the most common one. Typically, it is equivalent to selecting a point data time series - where one dimension varies, but others are on a specific fixed value. A typical case would be selecting temperature time series on the sequence of two-dimensional maps (each defined by longitude, latitude, and time) - a usual source could be a large netCDF file with the weather forecast. There are three dimensions in this case: time (varying dimension), longitude (fixed for selection), latitude (fixed for selection). A similar example could be the selection of values in columns in the database for analytical processing (like computing averages or sums). </p>
<p>There is a simple rule in these cases: keep the varying dimension as the last one when writing data. The rationale for this choice is simple. When storing data (say on the hard drive or sending them via network), the system has to serialize them as a one dimensional series of bytes - which is always the ultimate way data are stored. So technically, when you are selecting, you choose just the proper slice of this one-dimensional data - the system interprets the reading command in the way: fetch the data (say on disk) from address x to address y. That means, if your most varying dimension is in the wrong position, the system has to either read the whole block of data into memory and then pick the correct elements or repeatedly access the device (disk or network) to ask for every point of the series. The first can cause memory issues; the second has a significant performance impact when considering latencies (it always takes some time when accessing stored data).</p>
<p>Unfortunately, writing data where source dimension order differs from the desired one is slow and potentially memory-hungry. If you are lucky and know the size and composition of the data set in advance, there is a place for optimization. For example, you can reduce memory requirements by serializing data continuously in chunks. However, if the source is a stream of data, you might quickly run out of memory.</p>
<p>The third case is the most problematic one. There is only one rule: keep the order of the dimensions from the least varying to the most varying. The rationale for this is the same as described above (data are in the end just a one-dimensional series). However, there are many exceptional cases when even this rule is not the best to follow (see use case bellow).</p>

<h2>How are data stored technically?</h2>
<p>As mentioned above, data are technically stored in just one dimension. This raises the question of how it is possible to store multidimensional data to just one dimension and reconstruct them? The answer is simpler than one might think. Suppose you have just three dimensions of sizes (<em>l</em><sub>1</sub>, <em>l</em><sub>2</sub>, <em>l</em><sub>3</sub>). Then each point <em>P</em> has coordinates (<em>p</em><sub>1</sub>, <em>p</em><sub>2</sub>, <em>p</em><sub>3</sub>) - always indexed from 0 to <em>l</em><sub>i</sub> (right excluded). You can easily map these three coordinates to just one coordinate, say <em>q</em>, by using the relation:</p>
<p class="center">
    <em>q</em> = <em>p</em><sub>1</sub> + <em>l</em><sub>1</sub> &#8901; <em>p</em><sub>2</sub> + <em>l</em><sub>1</sub> &#8901; <em>l</em><sub>2</sub> &#8901; <em>p</em><sub>3</sub>
</p>
<p>draw a cube and try it practically if you do not believe it. And a similar relation is usable for the inverse mapping (from one dimension to three dimensions):</p>
<p class="center">
    <em>p</em><sub>3</sub> = FLOOR(<em>q</em> / (<em>l</em><sub>1</sub> &#8901; <em>l</em><sub>2</sub>))<br>
    <em>p</em><sub>2</sub> = FLOOR((<em>q</em> - <em>p</em><sub>3</sub> &#8901; <em>l</em><sub>1</sub> &#8901; <em>l</em><sub>2</sub>) / <em>l</em><sub>1</sub>)<br>
    <em>p</em><sub>1</sub> = <em>q</em> - <em>p</em><sub>3</sub> &#8901; <em>l</em><sub>1</sub> &#8901; <em>l</em><sub>2</sub> - <em>p</em><sub>2</sub> &#8901; <em>l</em><sub>1</sub>
</p>
<p>where FLOOR is the floor function (take just the integer part, ignore the decimal one).</p>
<p>The same logic can be used for any number of dimensions. Although it can be quite problematic for more than three dimensions, there is no simple way to imagine that problem geometrically.</p>

<h2>Use case</h2>
<p>The typical problem that one can imagine is the time series of maps. For example, say that you want to monitor irradiance at some location from the satellite. You have a 2D map of irradiance (the third dimension is time itself). So the dimensions are longitude, latitude and time. These maps are practically crucial for the prediction of solar panels' productions.</p>
<p>The following request for selecting data are the most common ones:</p>
<ol>
    <li>Select the irradiance time series at some geographical location (to analyze average values, peaks, etc.).</li>
    <li>Select some polygon on the map and compute the average irradiance in each time-step (and return just 1D time series of this average values). This step is crucial when building large solar installations (you do not have just one point).</li>
</ol>
<p>The first problem is the simple one; the best approach is to have a time dimension in the last place.</p>
<p>On the other hand, the second use case is quite problematic. The optimal dimension order has to be determined by the average size of polygons. If your polygons are big enough, having a time series in the first place is the best option (and having in the last place is the worst). This is due to the computation that is performed at each time step. If you have a big polygon and time dimension in the first place, you can very swiftly compute the average value at each time step. On the other hand, if the time dimension is in the last place, you must read each column (in geometric representation) separately, which is slow.</p>

<h2>Column-oriented data stores (and DBMS)</h2>
<p>There is one surprising place where the dimension order matters a lot. That is the environment of Apache Hadoop based databases (or similar proprietary environments). Technically, the database table is just a two-dimensional array. And again, the order of dimensions matters. Typically, rows are the last index when data are serialized. That is meaningful because the typical request is to select rows based on some condition. However, when doing analytical processing (OLAP), the standard request might look very different. For example, if you mainly count sums, averages or select the whole series of columns, the optimal order would be to have columns on the last dimension. There are analytical tools (in the Hadoop environment) that take this into account - like Apache Kudu - that implements precisely this logic. Many other database systems are also available (not only based on HDFS) - like time-series databases (most commonly InfluxDB).</p> 
<p>The typical example for storing massive datasets of data is telemetry deployed on a large e-shop. Business analysts often need to analyze how many items have been sold, the average price of the package, the weight of items, check how many things are in your stock, and many others. These are the typical examples of analytical queries primarily performed on columns space. They also require a lot of time to be performed (if you have more than a million items), so the optimization makes perfect sense.</p>
<h2>Read vs write trade-off</h2>
<p>Again, it is important to know that if your data are coming in some specific dimension order, it is not that trivial to store them in a different order. It is always important to be aware of the trade-off between fast reading and fast writing. So, if you write data just for archive (and do not expect frequent processing), it is handier to write them as they are not to permutate any dimensions. The problem of dimension permutation is even more challenging if you write a massive amount of data (that cannot be stored in operational memory). In this case, the chunking of data should take place. Generally, there is no simple manual for dealing with this issue - you have to use your common sense.</p>
<h2>Remarks and summary</h2>
<p>Suppose you are lucky enough and have some simple problem that fits the above categories. In that case, you can achieve a significant performance overhaul by swapping the dimension order of your data. In many cases, unfortunately, there is no simple solution. You may often need more than one data source to optimize performance (each having different dimension order). The trade-off between writing data in changed dimension order (which is slow) and reading them must also be considered. Do not feel afraid to use your common sense when dealing with this issue, as there is generally no precise manual for your problem.</p>
"""

ENTITY = cr.Article(
    title="Dimension order problem when storing big data",
    url_alias='dimension-order-problem-when-storing-big-data',
    large_image_path="images/dim_orders_big.jpg",
    small_image_path="images/dim_orders_small.jpg",
    date=datetime.datetime(2020, 9, 26),
    tags=[cr.Tag('Dimensions', 'dimension'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('NetCDF', 'netcdf')],
    content=content,
    lead=lead,
    description="Presents general rules for selecting the optimal order of dimension when storing big multidimensional data. The correct dimension order makes reading faster."  # noqa: E501
)
