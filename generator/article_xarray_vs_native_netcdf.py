# Pros and Cons of using xarray when accessing NetCDF files
import datetime
import crinita as cr

lead = """Famous library xarray is more or less standard in the data analyst branch. During the last few years, it has become incredibly popular. It has been deployed in many projects often without any careful decision if it is needed or if there is any other way how to treat the issue. One of the essential xarray functionality is the reading and writing to the NetCDF files. This is also a focus of this article."""

content = """Famous library xarray is more or less standard in the data analyst branch. During the last few years, it has become incredibly popular. It has been deployed in many projects often without any careful decision if it is needed or if there is any other way how to treat the issue. One of the essential xarray functionality is the reading and writing to the NetCDF files. This is also a focus of this article where at the end you should be capable of making the inform decision whether or not use xarray.

<h2>Pros of the xarray</h2>
<p>One of the fundamental pros of xarray is how it handles dimensions. If you have ever used default driver (Python package NetCDF4) you know exactly how clumsy you have to deal with this issue. Consider the following code that read from the NetCDF4 variable with unknown dimension order (having dimension longitude, latitude, time):</p>

<pre class="code"><code>import xarray
file = xarray.open_dataset("FILE_PATH.nc")
value = file['var'].sel(lon=3, lat=2, time="2016-12-30 00:00:00").values</code></pre>

<p>
As you can see, you do not have to care about the dimension order inside the NetCDF variable (which can easily vary from file to file). All the values are also correctly interpreted (as you can see in the 'time' axes).</p>

<p>
For the comparison, if you want to achieve the same effect using only the native Python NetCDF4 driver, you have to follow the logic:</p>

<pre class="code"><code>import netCDF4
file = netCDF4.Dataset("FILE_PATH.nc")
expected_dim_order = ('lon', 'lat', 'time')
current_dim_order = file['var'].dimensions
permutation_formula = [expected_dim_order.index(dim) for dim in current_dim_order]
desired_index = [3, 2, 1]
file_index = tuple(desired_index[i] for i in permutation_formula)
value = file['var'][file_index]</code></pre>

<p>
This is the minimal code that is dimension order blind when the native driver is used. You can easily notice the much bigger complexity to receive the same effect. If you also wanted to have the smart reading on the time dimension, code would be much more complicated than this. Reading of the time series in some reasonable format (currently only pandas.DatetimeIndex) is also a problem. When the native driver is used, arguably the easiest way is the following one:</p>

<pre class="code"><code>import pandas as pd
import netCDF4
import cftime
nc = netCDF4.Dataset("FILE_PATH.nc")
time_series = pd.to_datetime(cftime.num2pydate(nc['time'][:], nc['time'].units), utc=True)</code></pre>

<p>
If you do not have a UTC, you have to adjust it afterwards. Consider how elegant is the same code when xarray is used:</p>

<pre class="code"><code>import xarray
import pandas as pd
file = xarray.open_dataset("FILE_PATH.nc")
time_series = pd.DatetimeIndex(file['time'].values, tz="UTC")</code></pre>

<p>
Described examples are arguably the most famous ones. In both cases, xarray is the winner if it comes to simplicity and code readability.</p>


<h2>If it is so, what is the problem? (Cons of xarray)</h2>
<p>So far, so good, except that nothing is good. Despite a lot of nice features, xarray is actually very problematic. A few of the problems related to xarray are mentioned in this section.</p>

<h3>Memory leaks</h3>
<p>You open you nice dataset in xarray, do a few operations, close it. Nothings seems to be a problem. But there is one. Noone can be sure that the garbage collector will really collect reminders after your variable. This problem is especially problematic if you read and write to the NetCDF file inside some web application. Memory usage of the web-application expands more and more until the time when it is reset. That is, of course, very problematic (not only because of security). You can find some ways how to circumvent this issue (like using a separate process). But one way or another it is a very inconvenient feature of xarray.</p>

<h3>Chunking</h3>
<p>Whenever you work on the machine with limited resources (practically always outside the data-analysis world), you need to read variables in some reasonable-sized chunks. There are generally two ways how to treat this issue. The more complex one is read (or write) from (to) variable using Dask (or xarray running on Dask). This approach is useful if you process massive datasets, and if you exactly know what to expect inside each variable (and is good only for experienced professional). Another approach is to read the variable in slices. In these cases, xarray is basically useless because you absolutely cannot really on it, consider the following example:</p>

<pre class="code"><code>value = file['var'].sel(lon=0, lat=0, time=slice(100, 1100)).values</code></pre>

<p>
You would expect that memory usage cannot exceed the value of memory usage for that 1000 items that you actually read. Reality is that xarray reads the whole variable into memory and slice it afterwards. That is unacceptable. Equivalent code that uses native driver works correctly:</p>

<pre class="code"><code>value = file['var'][0, 0, slice(100, 1100)]</code></pre>

<p>In this case, it is good to know that the keyword slice returns you an object that can be used for re-shuffling the dimension order described above.</p>

<h3>Appending to the file</h3>
<p>If it comes to writing in chunks to some variable, it is good to know that none xarray and the native driver does support multidimensional variables having one dimension unlimited. The native driver supports unlimited dimensions only in the 1D variables (xarray does not) and does not support unlimited dimension for any ND variables (N > 1). Unlimited dimensions are especially helpful if you need to append data to the file. Appending mode itself is currently not supported in xarray at all (native driver works without any problems in the 'a' mode).</p>

<h3>Other inconveniences</h3>
<p>There is also a lot of different things. One of the most famous ones is that you always have to be careful what you receive at the end if you use xarray. Sometimes it is a Dask object, and sometimes it can be a Numpy object. This is very inconvenient, and you have to read the documentation very carefully to avoid it. If it comes to types, you also cannot be sure how strings as "1" and other number literals (having type string) will be interpreted in the xarray world.</p>

<p>It is also good to bear in mind that xarray does not interpret the value until you explicitly ask for it. This can lead to a very long pipeline that can cause memory and performance issues.</p>

<p>Last but not least issue is related to a number of dependencies that are installed together with xarray. By default, it is six dependencies and many others, depending on what purpose you want to use it.</p>

<h2>Summary</h2>
<p>As xarray provides a lot of incredible features that can save time in development, it also contains a lot of pitfalls you have to be aware. Only a few of them are presented here (memory leaks, troubles with chunking, no possibility of appending to file, type misinterpretation, etc.). Generally speaking,  none of the described issues is critical enough to make xarray useless. On the other hand, it is good to make an inform decision before you choose to deploy anything relying on it. There is a lot of other tools that, combined together provides a safer alternative.</p>
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
