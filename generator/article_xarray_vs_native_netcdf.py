# Pros and Cons of using xarray when accessing NetCDF files
import datetime
import crinita as cr

lead = """The famous library xarray is more or less standard in the data analyst branch. During the last few years, it has become prevalent. It has been deployed in many projects, often without any careful decision if it is needed or if there is any other way to treat the issue. One of the essential xarray functionality is the reading and writing of the NetCDF files. This is also a focus of this article where at the end, you should be capable of making the informed decision whether or not to use xarray."""

content = """<p class="lead">The famous library xarray is more or less standard in the data analyst branch. During the last few years, it has become prevalent. It has been deployed in many projects, often without any careful decision if it is needed or if there is any other way to treat the issue. One of the essential xarray functionality is the reading and writing of the NetCDF files. This is also a focus of this article where at the end, you should be capable of making the informed decision whether or not to use xarray.</p>

<h2>Pros of the xarray</h2>
<p>One of the fundamental pros of xarray is how it handles dimensions. If you have ever used the default driver (Python package netCDF4), you know how clumsy you have to deal with this issue. For example, consider the following code that read from the NetCDF4 variable with unknown dimension order (having dimension longitude, latitude, time):</p>

<pre class="code"><code>import xarray
file = xarray.open_dataset("FILE_PATH.nc")
value = file['var'].sel(
    lon=3, lat=2, time="2016-12-30 00:00:00"
).values</code></pre>

<p>As you can see, you do not have to care about the dimension order inside the NetCDF variable (which can easily vary from file to file). All the values are correctly interpreted (as you can see in the 'time' axes).</p>

<p>For the comparison, if you want to achieve the same effect using only the native Python NetCDF4 driver, you have to follow the logic:</p>

<pre class="code"><code>import netCDF4
file = netCDF4.Dataset("FILE_PATH.nc")
expected_dim_order = ('lon', 'lat', 'time')
current_dim_order = file['var'].dimensions
permutation_formula = [
    expected_dim_order.index(dim) for dim in current_dim_order
]
desired_index = [3, 2, 1]
file_index = tuple(
    [desired_index[i] for i in permutation_formula]
)
value = file['var'][file_index]</code></pre>

<p>This example represents the minimalistic dimension order blind file reading code using the native NetCDF driver. You can quickly notice the much bigger complexity to have the same effect. If you also wanted to have the smart reading on the time dimension, code would be more complicated than this. Reading the time series in some reasonable format (probably pandas.DatetimeIndex) is also a problem. In the case of the native driver, arguably the easiest way is the following one:</p>

<pre class="code"><code>import pandas as pd
import netCDF4
import cftime
nc = netCDF4.Dataset("FILE_PATH.nc")
time_series = pd.to_datetime(
    cftime.num2pydate(nc['time'][:], nc['time'].units
), utc=True)</code></pre>

<p>If you do not have a UTC, you have to adjust it afterwards. Consider how elegant is the same code in the case of xarray:</p>

<pre class="code"><code>import xarray
import pandas as pd
file = xarray.open_dataset("FILE_PATH.nc")
time_series = pd.DatetimeIndex(
    file['time'].values, tz="UTC"
)</code></pre>

<p>Described examples are arguably the most famous ones. In both cases, xarray is the winner for simplicity and code readability.</p>


<h2>If it is so, what is the problem? (Cons of xarray)</h2>
<p>So far, so good, except that nothing is good. Despite a lot of excellent features, xarray is very problematic. This section discusses a few of the problems related to xarray.</p>

<h3>Memory leaks</h3>
<p>Imagine that you open your nice dataset in xarray, do a few operations, and close it. Nothings seems to be a problem. But there is one. There is no guarantee that the garbage collector collects reminders of your variable (and operations). This problem is especially problematic if you read and write to the NetCDF file inside some web application simply because memory usage expands more and more until the system crashes. Such a crash can have many very problematic outcomes - mainly, it threatens the system's security. Of course, you can find ways to circumvent this issue (like using a separate process). But one way or another, it is a very inconvenient feature of xarray.</p>

<h3>Chunking</h3>
<p>Consider that you need to read variables in reasonable-sized chunks when working on a machine with limited resources (an extremely common problem when dealing with satellite images). There are generally two ways how to treat this issue. The more complex one is to read (or write) from (to) variable using Dask (or xarray running on Dask). This approach is helpful if you process massive datasets and know what to expect inside each variable (knowing format and sizes in advance) and is suitable only for experienced professionals. Another approach is to read the variable in slices. In these cases, xarray is useless because you absolutely cannot really on it. Consider the following example:</p>

<pre class="code"><code>value = file['var'].sel(
    lon=0, lat=0, time=slice(100, 1100)
).values</code></pre>

<p>You would expect that memory usage cannot exceed the value of memory usage for that 1000 items that you actually read. Unfortunately, the reality is that xarray reads the whole variable into memory and then slices it afterwards. That is unacceptable (as it can easily cause a crash). Equivalent code that uses native driver works correctly:</p>

<pre class="code"><code>value = file['var'][0, 0, slice(100, 1100)]</code></pre>

<p>In this case, it is good to know that the keyword slice returns you an object suitable for re-shuffling the dimension order described above.</p>

<h3>Appending to the file</h3>
<p>When writing in chunks to some variable, it is useful to know that none xarray and the native driver support multidimensional variables having one dimension unlimited in size. The native driver supports unlimited dimensions only for 1D variables (xarray does not) but does not support unlimited dimensions for any nD variables (n > 1). Unlimited dimensions are especially helpful if you need to append data into the file. Furthermore, appending mode itself is currently not supported in xarray (native driver works without any problems in the 'a' mode).</p>

<h3>Other inconveniences</h3>
<p>There is also a lot of other things. One of the most famous is that you always have to be careful what you receive at the end of the operation chain (if you use xarray). Sometimes it is a Dask object, and sometimes it can be a Numpy object. This is very inconvenient, and you have to read the documentation very carefully to avoid it. Regarding types, you cannot be sure how strings as "1" and other number literals (having type string) are interpreted in the xarray world.</p>

<p>It is also good to remember that xarray does not interpret the value until you explicitly ask for it. This can lead to a very long pipeline that can cause memory and performance issues. Therefore, it is necessary to run the pipeline from time to time explicitly - technically, it means breaking a big pipeline into smaller ones.</p>

<p>Another issue is the number of dependencies that are installed together with xarray. By default, it is six dependencies and many others, depending on what purpose you want to use it. The number of sub-dependencies can cause common problems when sub-dependencies are not compatible with their previous version - which can cause a crash of the system. Everyone who has ever maintained any larger Python application is very familiar with this issue.</p>

<h2>Summary</h2>
<p>As xarray provides many incredible features that can save time in development, it also contains a lot of pitfalls you have to consider before moving to production. This article describes some of the most common problems like memory leaks, troubles with chunking, no possibility of appending to file, type misinterpretation, etc. Generally speaking, none of the described issues is critical enough to make xarray useless. On the other hand, it is essential to make an informed decision before deploying to production. Many alternatives are working with a safe native driver that, combined, provides a safer alternative to xarray.</p>
"""

ENTITY = cr.Article(
    title="Pros and Cons of using xarray when accessing NetCDF files",
    url_alias='pros-and-cons-of-using-xarray-when-accessing-netcdf-files',
    large_image_path="images/globe_big.jpg",
    small_image_path="images/globe_small.jpg",
    date=datetime.datetime(2020, 4, 10),
    tags=[cr.Tag('xarray', 'xarray'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Python', 'python'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('NetCDF', 'netcdf')],
    content=content,
    lead=lead
)
