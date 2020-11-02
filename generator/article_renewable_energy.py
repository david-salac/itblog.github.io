# Prediction of renewable energy from the software engineering perspective
import datetime
import crinita as cr

lead = """A lot of things has been said in the past two decades about the possibilities of renewable energy. Many researchers probe the possibilities of power prediction in all horizons (short-term, mid-term and long-term). What is still an open question is what tools and datasets are now available for required computations. Especially what open-source tools are available."""

content = """A lot of things has been said in the past two decades about the possibilities of renewable energy. Many researchers probe the possibilities of power prediction in all horizons (short-term, mid-term and long-term). What is still an open question is what tools and datasets are now available for required computations. Especially what open-source tools are available.
<h2>Predicting of the solar photovoltaic installation.</h2>
<p>In order to predict energy production of the solar panel, you need to know the panel's parameters (like operational cell temperature, power capacity = maximal production in optimal conditions, etc.), and following environmental variables (all are related to the geographical position of the installation):</p>
<ol>
<li><strong>Global Horizontal Irradiance (GHI)</strong> in units W&#8901;m<sup>-2</sup>. Is the most important environmental variable. It describes solar activity at a given time. There are many sources, usable is, for example, ERA-5 from EMCWF (see <em>link 1</em> below article).</li>
<li><strong>Temperature (T)</strong> in units degree C. Temperature at the time of prediction (is typically available as a time series). There are many sources, usable is, for example, ERA-5 from EMCWF (see <em>link 1</em> below article).</li>
<li><strong>Ground albedo (α)</strong>, in units 1 (unitless). Describe reflectance of the surface around the installation, is available e. g. on CGLS (see <em>link 2</em> below article). It is typically not available as a time series, but as a year average.</li>
</ol>

<p>If it comes to prediction itself, there are many algorithms available. You need to compute the solar zenith and azimuth angles (aka SZA and SAA, you can use a simple algorithm that is available 
<a href="https://github.com/david-salac/Renewable-energy-prediction">HERE</a> 
 - it is written in Python on few lines and is sufficiently precise). Then you can perform computation with installation parameters - a simple algorithm is described  
<a href="https://github.com/david-salac/Fast-SZA-and-SAA-computation">HERE</a> 
 with description (written in Python / Jupyter Notebook), again it is sufficiently precise.</p>

<h2>Library PVLIB</h2>
<p>One of the best libraries available for prediction of the energy from photovoltaic installation is called PVLIB (Python library, opensource, commercial-friendly license) which is developed and maintained by the US Industry and National Laboratory (government organisation). </p>

<p>Although the aim of this post is not to do an advertisement for PVLIB, it is fair to say that it covers everything you need to perform precise energy prediction (including very helpful tools like clear sky irradiance predicting, very precise SZA and SAA computation, Erb's decomposition model, etc.). Library PVLIB should certainly your starting point for the predicting of solar energy.
Predicting energy from wind energy converter (wind turbines).</p>

<p>For predicting outputs of wind energy converters, the situation is much easier than in the case of the solar photovoltaic installation. You need far fewer parameters to do so. There are two important parameters: </p>
<ol>
<li><strong>Height of the installation</strong> - from the rotor centre to ground</li>
<li><strong>Power curve</strong> - function mapping from wind speed to power production. It typically follows the logic <em>P = v<sup>3</sup></em>, where <em>P</em> is power produced, and <em>v</em> is the wind speed. Typically, the curve becomes saturated at some point and then sharply drop from some critical wind speed (it can also be negative because you can consume energy to slow turbine down).</li>
</ol>

<p>If it comes to the environmental variables, you need to know two of them:</p>
<ol>
<li><strong>Wind speed (<em>v<sub>s</sub></em>)</strong>, units m&#8901;s<sup>-1</sup> at some referential height <em>s</em>. Typically available as a time series. There are many sources, usable is, for example, ERA-5 from EMCWF (see <em>link 1</em> below article)</li>
<li><strong>Air density (ϱ)</strong>, units kg&#8901;m<sup>-3</sup>). Typically computed just once based on some empirical relations and then used for each time.</li>
</ol>

<p>To perform computations, you can follow the link 
<a href="https://github.com/david-salac/Renewable-energy-prediction">HERE</a> 
(that provides sufficiently precise algorithm). All you need to create is the power curve (that is typically available from your vendor). There is no such complex library for predicting the energy from the wind energy converters like PVLIB in the case of a photovoltaic installation.</p>

<h2>Processing of datasets</h2>

<p>Separated issue from the prediction (very important one though) is how to treat datasets with weather variables that you download. Typically (if you are lucky) it is the NetCDF (version 4) file that can be treated using xarray or native driver in Python (the issue is described in one of the previous posts on this blog). If you are less lucky, you can spend an incredible amount of time by dealing with it. It is strongly recommended to convert all other formats to NetCDF4, which is now an industrial standard.</p>

<h2>Summary</h2>
<p>There are many tools for predicting of renewable energy from various type of installation. This post is focused only on predicting the energy from wind turbines and photovoltaic installations. The most important library for the photovoltaic installation is called PVLIB. And the most important source of weather data (for long-term forecast) is called ERA-5. If it comes to the wind turbines (aka wind energy converter), there is no such a comprehensive library like PVLIB, and you have to rely on basic formulas. The most important source of weather data is again ERA-5 (for long-term forecast). There is also plenty of commercial tools that offer the same and companies focused just on this purpose (one of them is called RE-SAT and is developed by the University of Reading).</p>

<h2>Useful links</h2>
<ol>
<li>ERA-5 at EMCWF, available at <a href="https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5">https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5</a></li>
<li>Copernicus Global Land Service, Surface Albedo, available at <a href="https://land.copernicus.eu/global/products/sa">https://land.copernicus.eu/global/products/sa</a></li>
</ol>
"""

ENTITY = cr.Article(
    title="Prediction of renewable energy from the software engineering perspective",
    url_alias='prediction-of-renewable-energy-from-the-software-engineering-perspective',
    large_image_path="images/solar_panel_big.jpg",
    small_image_path="images/solar_panel_small.jpg",
    date=datetime.datetime(2020, 5, 25),
    tags=[cr.Tag('Data Visualisation', 'data-visualisation'),
          cr.Tag('Renewable energy', 'renewable-energy'),
          cr.Tag('Python', 'python'),
          cr.Tag('Big Data', 'big-data'),
          cr.Tag('Geospatial', 'geospatial')],
    content=content,
    lead=lead
)
