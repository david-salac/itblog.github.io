# How to replace GDAL with more efficient tools?
import datetime
import crinita as cr

lead = """Library GDAL (developed by OSGeo) is more or less standard for processing geospatial data. However, although it implements almost all the tools needed for this purpose, it is notoriously known for many operational problems. Mainly, it is practically impossible to install it quickly (as it requires many system-level dependencies), API is obsolete (designed in the late nineties), and it is not difficult to find unexpected behaviours, etc. So it is not surprising that many developers actively started to seek different tools. This post presents some possibilities for the most common issues (mainly focused on Python users)."""

content = """<p class="lead">Library GDAL (developed by OSGeo) is more or less standard for processing geospatial data. However, although it implements almost all the tools needed for this purpose, it is notoriously known for many operational problems. Mainly, it is practically impossible to install it quickly (as it requires many system-level dependencies), API is obsolete (designed in the late nineties), and it is not difficult to find unexpected behaviours, etc. So it is not surprising that many developers actively started to seek different tools. This post presents some possibilities for the most common issues (mainly focused on Python users).</p>

<h2>Reading GeoTIFF files </h2>
<p>GeoTIFF is still a popular standard. It is mainly used for storing raster layers (like map tiles). GDAL naturally provides functionality for reading GeoTIFF files - but it is traditionally hard to use. Typically GeoTIFF file follows some logic - data inside are correctly georeferenced and are stored in one band. If this is the case, the easiest way to read such a file is to use a library called rasterstats (https://pypi.org/project/rasterstats/). It provides a simple way to read data from a GeoTIFF file using various geometry definitions (WTK, GeoJSON, etc.) and many ways to process that data (compute the mean of data inside geometry maximal, minimal values and many others). An example of such code can follow the logic:</p>

<pre class="code"><code>from rasterstats import zonal_stats
zonal_stats(
    geometry_definition,
    path_to_file,
    stats="mean"  # or others
)
>>> [{'mean': 6.337481869210442}]</code></pre>

<p>Particularly helpful is also the simplified way of reading point values:</p>

<pre class="code"><code>from rasterstats import point_query
point_query(
    geometry_definition,
    path_to_file
)
>>> [[7.370820, 5.5437, 6.15254, None, 7.3708]]</code></pre>

<p>If the value is None - the point is outside of GeoTIFF geometry (so no Exception is raised).</p>

<p>There are many dependencies installed together with the library rasterstats. The most important ones are shapely, fiona and rasterio. All these libraries provide helpful functionality that can replace GDAL.</p>

<p>One of such requests can be to check if the geometry is inside of the GeoTIFF boundary box:</p>

<pre class="code"><code>import rasterio
from shapely.geometry import shape, box
boundaries = box(*rasterio.open(path_to_file).bounds)
if not boundaries.contains(shape(geometry_definition)):
    # If outside of boundary box
    pass
else:
    # if inside
    pass</code></pre>

<p>This example uses only the dependencies of rasterstats (so it does not require installing anything else).</p>

<h2>Reading NetCDF (and HDF) files</h2>
<p>NetCDF (in version 4) is another standard for storing big geospatial data (like earth-observation data, weather forecasts and similar). It provides many advanced functionalities (such as storing data in multidimensional variables, using a group of variables, defining compression, chunking and others). If the NetCDF (version 4) file does not contain any groups, it is also compatible with the definition of the HDF file (accordingly, the NetCDF4 driver can handle both standards). The most advanced driver for processing netCDF files is called netCDF4 (https://pypi.org/project/netCDF4/). GDAL and other tools like xarray internally use it to process NetCDF files. But there is no reason not to use it directly. Library netCDF4 is also available for C++ programming language in excellent condition (in sharp contrast to GDAL).</p>
<p>Reading of some NetCDF4 content can follow the logic:</p>

<pre class="code"><code>import netCDF4
ds = netCDF4.Dataset(wdp_path, 'r')
# Read variable (returns numpy masked array):
variable_content = ds['VAR_NAME'][:] 
# Read global attribute
atr_content = ds.ATTRIBUTE_NAME
# Read variable attribute
attr_var = ds['VAR_NAME'].ATRIBUTE_NAME
</code></pre>

<p>To see what is inside the netCDF file, a free tool called Panoply netCDF, HDF and GRIB Data Viewer (developed by NASA) is available. In addition, some typical use cases (like reading time variables) are described in the article <em class="text">Pros and Cons of using xarray when accessing NetCDF files</em>.</p>

<h2>Shapefiles</h2>
<p>Last but not least in the series of essential file types is the shapefile (*.shp). This file helps define some geometry boundaries (incredibly helpful for non-polygonial geometries). It is also one of the most popular formats in geospatial engineering. The typical use case, in this instance, is to check if some geometry has an intersection with the geometry defined by the file. A handy library to proceed with such validation is called geopandas (which offers many other tools as well and is incredibly helpful).</p>
<p>The code for doing so can follow the logic:</p>

<pre class="code"><code>import geopandas
cell_def = geopandas.read_file(path_to_file)
# Coordinates of intersecting indices
intersection = cell_def.intersects(geometry_definition)
if not (any(intersection)):
    # If there is no intersection
    pass
else:
    # To have array of cells that intersects:
    cells_in_intersection = cell_def[intersection]
</code></pre>

<p>Another helpful tool for dealing with shapefiles is a library called Fiona (discussed below). It covers all the functionality needed for generating shapefiles.</p>

<h2>What is not yet available outside GDAL?</h2>
<p>There are a few applications of GDAL where there is no other sufficient product available. One of the very common applications is geospatial coordinates transformation (for example, from EPSG:4326 to EPSG:3856). There are some ways to circumvent this issue using the underpinning library of QGIS - but this treatment is maybe worse than a disease (as installing QGIS is in many ways more difficult than installing GDAL). For these specific purposes, GDAL is a very helpful tool. Also, it is good to be aware that many libraries mentioned above use GDAL internally (it is just intelligently wrapped so that you can install a library in a user-friendly way).</p> 
<p>Another library worth mentioning is Fiona - even though it uses GDAL internally, it can be easily installed using PIP. It is beneficial for creating custom shapefiles and the processing of shapefiles generally. Moreover, Fiona is performance-optimized (working faster than library GeoPandas which can also be used in some limited way for this purposes).</p>

<h2>Tools influenced by GDAL</h2>
<p>Many tools use GDAL internally. The most typical example is GeoServer - it is a trendy tool for providing map tiles (and layers) developed again by OSGeo. Unfortunately, it has many disadvantages. Similarly to GDAL, the quality of code is deficient. In addition, the application is written as a single server monolithic application - definitely not a small service that is simple to scale (scaling is generally very difficult), which causes challenges for DevOps engineers. Also, recovery processes often files, which makes GeoServer challenging to use.</p>
<p>GDAL also influenced many other tools, for example, PDAL. It processes point cloud data and uses similar logic as GDAL. The most common use case is the processing of LiDAR data. Similarly to GDAL, it is available under the BSD licence.</p>

<h2>Summary</h2>
<p>This article presents some of the most common use cases for dealing with geospatial data and tools for dealing with these cases (that are quickly accessible and easy to use and install). All these tools can help to replace GDAL in most applications. Furthermore, these tools are libraries in Python simply installable via PIP - namely: rasterstats, rasterio, shapely, Fiona, netCDF4, geopandas, xarray. So it is worth spending some time studying these tools. First, however, it is good to be aware that many of these tools use GDAL internally (but that makes installation easier).</p>
"""

ENTITY = cr.Article(
    title="How to replace GDAL with more efficient tools?",
    url_alias='how-to-replace-gdal-with-more-efficient-tools',
    large_image_path="images/gdal_replacement_big.jpg",
    small_image_path="images/gdal_replacement_small.jpg",
    date=datetime.datetime(2020, 10, 28),
    tags=[cr.Tag('GDAL', 'gdal'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Python', 'python'),
          cr.Tag('Geospatial', 'geospatial'),
          cr.Tag('NetCDF', 'netcdf')],
    content=content,
    lead=lead,
    description="Python library GDAL for processing of geospatial data has become a synonym of obsoleteness and inefficiency. There are fortunately better tools to replace it."  # noqa: E501
)
