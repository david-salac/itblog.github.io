# Prediction of renewable energy from the software engineering perspective
import datetime
import crinita as cr

lead = """Many open-source tools can help with the prediction of renewable energy production. For example, the Python library PVLIB for computation of production solar of photovoltaic panels implements essential scientific methods. However, if it comes to predicting energy from wind turbines, there is no similar library - but the computation itself is sufficiently simple - so everyone can write their methods. There is also a question of how precise predictions are, which requires a probabilistic approach."""

content = """<p class="lead">Many open-source tools can help with the prediction of renewable energy production. For example, the Python library PVLIB for computation of production solar of photovoltaic panels implements essential scientific methods. However, if it comes to predicting energy from wind turbines, there is no similar library - but the computation itself is sufficiently simple - so everyone can write their methods. There is also a question of how precise predictions are, which requires a probabilistic approach.</p>

<h2>Production of the solar photovoltaic installation</h2>
<p>To predict the energy production of the solar panel, you need to know the panel's parameters. The manufacturer of the photovoltaic panel usually provides this information. Also, you need to know the parameters characteristic of concrete installation. Typical installation parameters are:</p>
<ol>
    <li><span class="math"><em>A<sub>t</sub></em></span><!-- LATEX $ A_t $ LATEX -->: tilt angle [degrees].</li>
    <li><span class="math"><em>A<sub>a</sub></em></span><!-- LATEX $ A_a $ LATEX -->: azimuth angle [degrees].</li>
    <li><em class="text">lon</em>: longitude - position of installation on earth [degrees].</li>
    <li><em class="text">lat</em>: latitude - position of installation on earth [degrees].</li>
</ol>
<p>Note that longitude and latitude are essential for predicting solar zenith and azimuth angle together with time - usually a dimension of weather product.</p>

<p>Regarding panel's parameters, parameters are:</p>
<ol>
    <li><span class="math"><em>G<sub>s</sub></em></span><!-- LATEX $ G_s $ LATEX -->: linear coefficient of efficiency decrease when 1 K temperature increase happens [unitless].</li>
    <li><span class="math"><em>T<sub>opt</sub></em></span><!-- LATEX $ T_{opt} $ LATEX -->: operational temperature of installation [degree of Celsius].</li>
    <li><span class="math"><em>E<sub>std</std></em></span><!-- LATEX $ E_{std} $ LATEX -->: standard irradiance [<span class="math">W⋅m<sup>-2</sup></span><!-- LATEX Wm$^{-2} $ LATEX -->].</li>
    <li><span class="math"><em>T<sub>std</std></em></span><!-- LATEX $ T_{std} $ LATEX -->: standard temperature [degree of Celsius].</li>
    <li><em class="equation">P</em>: panel's DC capacity - maximal power production in optimal conditions [W].</li>
</ol>
<p>All these parameters are essential for prediction. Although some might slightly change as panels get older, they are also invariant. Another crucial input for prediction is the weather condition. Mainly following variables:</p>

<ol>
    <li><em class="text">GHI</em> (Global Horizontal Irradiance) - describes solar activity at a given time - unit is <span class="math">W⋅m<sup>-2</sup></span><!-- LATEX Wm$^{-2}$ LATEX -->.</li>
    <li><em class="equation">T</em> (Temperature) - is the temperature in altitude around two meters in degrees Celsius.</li>
    <li><span class="math"><em>α</em></span><!-- LATEX $ \\alpha $ LATEX --> (Ground Albedo): Describe reflectance of the surface around the installation [unitless].</li>
</ol>

<p>The source of these weather variables is usually a weather forecast or weather data products - like satellite images (from ERA5, EMCWF, etc.). These satellite images' spatial and temporal resolution has the most significant impact on the prediction precision. Usually, you need at least ten years of data with a temporal resolution of about ten minutes and spatial resolution below one kilometre. It is also important to note that there are some open sources of these datasets - however, they typically are not accurate enough. In addition, the commercial licenses for high-resolution satellite images are usually costly - reaching thousands of American dollars annually (on 2021 price level).</p>

<h3>Library PVLIB</h3>
<p>One of the best libraries available for predicting the energy from photovoltaic installation is PVLIB (Python library, opensource, commercial-friendly license), developed and maintained by the US Industry and National Laboratory (government organisation). It includes all crucial algorithms, like Solar Azimuth Angle and Solar Zenith Angle computation, Erb's decomposition model, isotropic sky model to determine diffuse irradiance (and many more complex models like the Perez model).</p>

<p>PVLIB library is an industrial standard for modelling photovoltaic power production. If it is necessary to use different languages than Python, it is usually simple to rewrite concrete PVLIB's functions in other languages. Some algorithms, like SZA and SAA computations for other languages, can be found in the links below.</p>

<h3>Computation of energy production from PV installation</h3>
<p>When you have all the variables needed for computation, the actual process is simple. For example, you can use this code:</p>

<pre class="code"><code>from typing import Tuple
from datetime import datetime

import pvlib


def solar(
    E_ghi: float, T: float, R: float, t: datetime, *,
    A_t: float, A_a: float, P_lon_lat: Tuple[float, float],
    G_s: float, T_opt: float, E_std: float, 
    T_std: float, P: float
) -> float:
    \"\"\"
    Predict the photovoltaic power production.

    :param E_ghi: global horizontal irradiance
    :param T: temperature
    :param R: ground albedo (reflectance of the ground around)
    :param t: calendar time with precision up to seconds, in UTC
    :param A_t: tilt angle
    :param A_a: azimuth angle
    :param P_lon_lat: longitude and latitude of the location
    :param G_s: linear coefficient of efficiency decrease
    :param T_opt: operational temerature of installation
    :param E_std: standard irradiance
    :param T_std: standard temperature
    :param P: capacity of installation

    :return: The power prediction of installation in Watts.
    \"\"\"
    # Compute the Solar Zenith Angle and Solar Azimuth Angle
    sza_saa = pvlib.solarposition.get_solarposition(
        t, P_lon_lat[1], P_lon_lat[0]
    )
    # Extract SZA and SAA
    A_sza, A_saa = sza_saa['zenith'], sza_saa['azimuth']
    # Compute DHI and DNI (Direct Normal Irradiance and
    # Diffuse Horizontal Irradiance) using Erbs model
    dhi_dni = pvlib.irradiance.erbs(E_ghi, A_sza, t)
    # Extract DHI and DNI
    E_dhi, E_dni = dhi_dni['dhi'], dhi_dni['dni']
    # Computes the total irradiance
    irr = pvlib.irradiance.get_total_irradiance(
        A_t, A_a, A_sza, A_saa, E_dni, E_ghi, E_dhi, albedo=R
    )
    # Extract total irradiance
    E_irr = irr['poa_global'].to_numpy().squeeze()

    # Normalized temperature
    T_n = T + E_irr * (T_opt - 20.0) / 800.0

    # Predict the power:
    return (E_irr / E_std) * (1.0 + G_s) * (T_n - T_std) * P


# EXAMPLE
power = solar(
    E_ghi=800.0, T=23.5, R=0.25, t=datetime(2020, 5, 12, 10, 30),
    A_t=30.0, A_a=30.0, P_lon_lat=(-0.12795, 51.50774),
    G_s=-0.004, T_opt=47.0, E_std=1000.0, T_std=43.0, P=1000.0
)</code></pre>

<p>As you can see, the last line of the function returns actual power production. Note that this algorithm is a deterministic prediction - you receive just one value without any error bars.</p>

<h2>Production of the wind energy converter (aka wind turbine)</h2>
<p>Mathematically speaking, predicting energy outcomes from wind turbines is a much easier problem. Regarding the installation parameters, there are just two:</p>
<ol>
    <li><em class="equation">H</em> (height of the installation): altitude of the rotor centre from the ground [m].</li>
    <li><span class="math"><em>P</em>(<em>v</em>)</span><!-- LATEX $ P(v) $ LATEX --> is a power curve - mapping from wind speed to power production [W]. It usually follows the form <span class="math"><em>P</em>(<em>v</em>) = <em>v</em><sup>3</sup></span><!-- LATEX $ P(v) = v^3 $ LATEX --> (cube of the wind speed) and become saturated from a certain wind speed. Then there is typically a drop for high wind speeds.</li>
</ol>
<p>Regarding environmental (weather data) variables, there is only one:</p>
<ol>
    <li><span class="math"><em>v<sub>w</sub></em></span><!-- LATEX $ v_w $ LATEX --> (wind speed): is the wind speed at a certain altitude [<span class="math">m⋅s<sup>-1</sup></span><!-- LATEX $ ms^{-1} $ LATEX -->].</li>
</ol>
<p>There are, however, a few constants usually packed with weather data products:</p>
<ol>
    <li><span class="math"><em>D<sub>a</sub></em></span><!-- LATEX $ D_a $ LATEX --> (air density): represents the air density (usually averaged value) at the point [<span class="math">kg⋅m<sup>-3</sup></span><!-- LATEX $ kg\cdot m^{-3} $ LATEX -->].</li>
    <li><span class="math"><em>A<sub>r</sub></em></span><!-- LATEX $ A_r $ LATEX --> (referential altitude): altitude of wind speed used in weather dataset [m].</li>
    <li><em class="equation">L</em>: coefficient for height transformation, used for calibrating wind speed when an altitude of weather data set differs from height of installation [unitless].</li>
</ol>
<p>From the computational point of view, mentioned constants can be considered variables (time series), but they are usually not available in this form.</p>
<p>The same holds for weather datasets as mentioned above - they are either insufficient (but free) or expensive (but precise).</p>

<h3>Computation of energy production of wind turbine installation</h3>
<p>As mentioned above, the actual computation is simple, as you can see in the following example:</p>
<pre class="code"><code>from typing import Callable
import numpy as np


def wind(
    v_w: float, D_a: float, A_r: float, L: float,
    *, H: float, C: Callable[[float], float], P: float
) -> float:
    \"\"\"
    Predict the power production of the wind turbine.

    :param v_w: wind speed
    :param D_a: air density
    :param A_r: referential altitude
    :param L: coefficient for height tranformation
    :param H: height (from ground up to the center of rotor)
    :param C: mapping from wind speed to efficiency
    :param P: capacity of the installation
    :return: power prediction for given conditions.
    \"\"\"
    # Calibrate wind speed (measured for given altitude)
    #   to the height
    v_w *= (H / A_r) ** L

    # Calibrate wind speed to density of air
    #    (divided by referential one)
    # referential density is 1.225 based on the value
    #   defined by International Standard Atmosphere organization
    v_w *= (D_a / 1.225) ** (1.0 / 3.0)
    return P * C(v_w)


# EXAMPLE
# 1) define power curve:
def power_curve(v_s) -> float:
    # Provided by vendor
    curve = {2.0: 0.0, 3.0: 0.0, 4.0: 0.02727,
             5.0: 0.7208, 6.0: 0.13368, 7.0: 0.21711,
             8.0: 0.32513, 9.0: 0.45454, 10.0: 0.5925,
             11.0: 0.7176, 12.0: 0.8117, 13.0: 0.8673,
             14.0: 0.8941, 15.0: 0.9048, 16.0: 0.9080,
             17.0: 0.9090, 18.0: 0.9090, 19.0: 0.9090,
             20.0: 0.9090, 21.0: 0.9090, 22.0: 0.9090,
             23.0: 0.9090, 24.0: 0.9090, 25.0: 0.9090}
    c_w = np.fromiter(curve.keys(), dtype=float)
    c_p = np.fromiter(curve.values(), dtype=float)
    # linear interpolation + extrapolates to zeros elsewhere
    return np.interp(v_s, c_w, c_p, left=0.0, right=0.0)


# 2) compute power:
power = wind(v_w=10.0, D_a=1.250, A_r=10.0, L=0.1431,
             H=30, C=power_curve, P=1250000)</code></pre>

<p>The most challenging part is to map the wind speed to production. Usually, tables provided by turbine vendors are used for this purpose. This code uses AC power capacity instead of actual power production, making prediction easier when dealing with larger installations. Still, the logic is the same - only it uses a portion of the capacity for the power curve instead of production itself.</p>
<h2>Other renewable generators</h2>
<p>There are many other renewable energy generators as well. For example, a traditional bagasse-fired power station is the standard thermal power station that uses bagasse (or other biomass) instead of coal. Although it is questionable whether this type of generator should be called renewable - authorities of most countries do consider it to be a renewable source. Also, when predicting the energy production of these power generators, there is nothing special about them (all that is valid for coal-fired power stations is valid for biomass-based ones). The most critical parameter is the energy density of biomass (typically bagasse) in unit J/kg that defines how much energy is in one kilogram of bagasse (biomass).</p>
<p>Another popular energy generator is the solar thermal electric one. It is a set of mirrors that focuses sunlight on one place. The rest is the same as in the case of the thermal power station. There are many disputes about how ecological this source of power is - mainly because of its massive impact on the environment (for example - many birds die every day because they flew in the wrong place). Technically the only suitable place for this type of generator is some desert as they need direct sunlight. The most important parameters are global irradiance (as in the case of photovoltaic installations) and liquid parameters.</p>
<p>Another, mainly experimental, power source is the wave device. It transfers power hidden in waves to electric power. The most important input parameters for predicting energy for a wave device are <em class="equation">T</em> [units: seconds], representing the energy period and <em class="equation">H</em> [units: meters], representing the spectral significant wave height. The energy produced by this device is equal to <span class="math"><em>C⋅T⋅H</em><sup>2</sup></span><!-- LATEX $ CTH^2 $ LATEX --> for some device-specific constant <em class="equation">C</em> (these devices are still not commercially available).</p>
<h2>Error prediction</h2>
<p>Deterministic prediction using the algorithm described above is essential - but it provides the estimated value without error bounds. But many investors, banks and insurance companies are interested in the worst-case scenarios. Something that happens in probabilistic quantile like 0.9 or similar. The typical error is modelled using Gaussian multivariate distribution, reflecting spatial and temporal covariances. Large weather datasets with the high temporal resolution are required for accurate results - usually at least ten years with a resolution of ten minutes. Also, it is necessary to have some ground measurements from existing installations to predict errors.</p>

<h2>Summary</h2>

<p>There are many tools for predicting renewable energy from various types of installation. This post is focused only on predicting the energy from wind turbines and photovoltaic installations. The most important library for photovoltaic installation is called PVLIB. And the most important source of weather data (for long-term forecast) is ERA5. If it comes to wind turbines (aka wind energy converter), there is no comprehensive library like PVLIB, and you have to rely on basic formulas. The essential weather data source is again ERA5 (for long-term forecast). Often, it is also vital to know the error distribution of prediction. That is not always simple as the ground-based measurements from existing installations is required for modelling.</p>

<h2>Useful links</h2>
<!-- LATEX \\begin{flushleft} LATEX -->
<ol>
    <li>ERA-5 at EMCWF, available at <a href="https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5">ERA5 archive</a></li>
    <li>Copernicus Global Land Service, Surface Albedo, available at <a href="https://land.copernicus.eu/global/products/sa">Copernicus Surface Albedo</a></li>
    <li>Fast SZA and SAA computation, available at <a href="https://github.com/david-salac/Fast-SZA-and-SAA-computation">Fast SZA and SAA computation</a></li>
    <li>Jupyter Notebook with codes for predicting energy, available at <a href="https://github.com/david-salac/Renewable-energy-prediction">Energy prediction Jupyter Notebook</a></li>
</ol>
<!-- LATEX \\end{flushleft} LATEX -->
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
    lead=lead,
    description="Renewable energy sources become more efficient and mainly more available. It also becomes crucial to understand how to predict the energy which we describe."  # noqa
)
