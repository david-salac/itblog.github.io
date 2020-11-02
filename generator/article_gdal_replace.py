# How to replace GDAL with more efficient tools?
import datetime
import crinita as cr

lead = """Library GDAL (developed by OSGeo) is more or less standard for the processing of geospatial data. Although it implements almost all the tools needed for this purposes, it is notoriously known for many operational problems. Mainly, it is practically impossible to install it quickly (as it requires many system-level dependencies), API is obsolete (designed in the late nineties) etc."""

content = """Library GDAL (developed by OSGeo) is more or less standard for the processing of geospatial data. Although it implements almost all the tools needed for this purposes, it is notoriously known for many operational problems. Mainly, it is practically impossible to install it quickly (as it requires many system-level dependencies), API is obsolete (designed in the late nineties), and it is not difficult to find unexpected behaviours, etc. So it is not surprising that many developers started to seek for different tools actively. This post presents some possibilities for the most common issues (and is mainly focused on Python users).
<h2>Reading GeoTIFF files </h2>
<p>GeoTIFF is still a popular standard. It is mainly used for storing raster layers (like map tiles). GDAL naturally provides functionality for reading GeoTIFF files - but it is traditionally hard to use. Typically GeoTIFF file follows some logic - data inside are correctly georeferenced and are stored in one band. If this is the case, the easiest way how to read such file is to use a library called rasterstats (https://pypi.org/project/rasterstats/). It provides a simple way how to read data from a GeoTIFF file using various geometry definitions (using WTK, GeoJSON, etc.) and many ways how to process that data (compute mean of data inside geometry, maximal, minimal values and many others). Example of such code can follow the logic:</p>

<pre class="code"><code>from rasterstats import zonal_stats
zonal_stats(
    geometry_definition,
    path_to_file,
    stats="mean"  # or others
)
>>> [{'mean': 6.337481869210442}]
</code></pre>

<p>Particularly helpful is also the simplified way of reading point values:</p>

<pre class="code"><code>from rasterstats import point_query
point_query(
    geometry_definition,
    path_to_file
)
>>> [[7.370820, 5.5437, 6.15254, None, 7.3708]]
</code></pre>

<p>If the value is None - the point is outside of GeoTIFF geometry (so no Exception is raised).</p>

<p>There are many dependencies installed together with the library rasterstats. The most important ones are shapely, fiona and rasterio. All these libraries provide helpful functionality that can replace GDAL. </p>

<p>One of such requests can be to check if the geometry is inside of the GeoTIFF boundary box:</p>

<pre class="code"><code>import rasterio
from shapely.geometry import shape, box
boundaries = box(*rasterio.open(path_to_file).bounds)
if not boundaries.contains(shape(geometry_definition)):
    # If outside of boundary box
    pass
else:
    # if inside
    pass
</code></pre>

<p>
This example uses only the dependencies of rasterstats (so it does not require to install anything else).
</p>

<h2>Reading NetCDF (and HDF) files</h2>
<p>NetCDF (in version 4) is another standard for storing of big geospatial data (like earth-observation data, weather forecasts and similar). It provides many advanced functionalities (such as storing data in multidimensional variables, using a group of variables, defining compression, chunking and others). If netCDF (version 4) file does not contain any groups, it is also compatible with the definition of the HDF file (accordingly the NetCDF4 driver can be used for both standards). The most advanced driver for processing of netCDF files is called netCDF4 (https://pypi.org/project/netCDF4/). It is also used by GDAL and by other tools like xarray if it comes to the processing of these files. But there is no reason for not using it directly. Library netCDF4 is also available for C++ programming language is an excellent condition (in sharp contrast to GDAL).</p>
<p>Reading of some netCDF4 content can follow the logic:</p>

<pre class="code"><code>import netCDF4
ds = netCDF4.Dataset(wdp_path, 'r')
# Read variable:
variable_content = ds['VAR_NAME'][:]  # Return numpy masked array
# Read global attribute
atr_content = ds.ATTRIBUTE_NAME
# Read variable attribute
attr_var = ds['VAR_NAME'].ATRIBUTE_NAME
</code></pre>

<p>To see what is inside the netCDF file, a free tool called Panoply netCDF, HDF and GRIB Data Viewer (developed by NASA) is available. Some typical use cases (like reading time variables) are described in the article <em>Pros and Cons of using xarray when accessing NetCDF files</em> (on this blog).</p>
<h2>Shapefiles</h2>
<p>Last but not least in the series of essential file types is the shapefile (*.shp). This file helps define some geometry boundaries (incredibly helpful for non-rectangular geometries). It is also one of the most popular formats in geospatial engineering. The typical use case, in this instance, is to check if some geometry has an intersection with the geometry defined by the file. Handy library to proceed such validation is called geopandas (which offers many other tools as well and is incredibly helpful).</p>
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

<p>Another helpful tool for dealing with shapefiles is a library called fiona (https://pypi.org/project/Fiona/). It covers all the functionality needed for generating of shapefiles.</p>

<h2>Summary</h2>
<p>This article tends to present some of the most common use cases for dealing with geospatial data and tools for dealing with these cases (that are quickly accessible and easy to use and install). All these tools can help to replace GDAL in most applications. All these tools are library in Python simply installable via PIP - namely: rasterstats, rasterio, shapely, fiona, netCDF4, geopandas, xarray. It is definitely worth to spend some time to study these tools.</p>
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
    lead=lead
)
