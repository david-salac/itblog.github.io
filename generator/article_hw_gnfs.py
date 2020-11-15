# The acceleration of public–key cryptanalysis methods using Xilinx Zynq-7000
import datetime
import crinita as cr

lead = """The Xilinx Zynq-7000 SoC provides new possibilities for increase of efficiency of cryptanalysis methods for public–key systems such as RSA or Diffie–Hellman key exchange algorithm. These cryptosystems are based on the discrete logarithm and integer factorization problem. After brief introduction to numerical methods for solving of these problems there is an introduction to the distributed system that aims to solving of these problems."""

content = """The Xilinx Zynq-7000 SoC provides new possibilities for increase of efficiency of cryptanalysis methods for public&#8211;key systems such as RSA or Diffie&#8211;Hellman key exchange algorithm. These cryptosystems are based on the discrete logarithm and integer factorization problem. After brief introduction to numerical methods for solving of these problems there is an introduction to the distributed system that aims to solving of these problems. Distributed system consists of master nod that manage the distribution of the tasks and slave nods that computes one of the most time consuming part of the selected numerical methods called sieving. Afterward the slave nod is designed on Xilinx Zynq-7000 SoC consists of ARM processor for analyzing of the problem and some custom IP cores running on FPGA for increasing of the efficiency of algorithm. The capabilities of distributed system is also measured and analyzed afterward.

<h2>Article</h2>
The whole article about this issue is available <a href="https://github.com/david-salac/public-key-cryptanalysis-methods-using-Xilinx/blob/master/SALAC_conf.pdf">HERE on GitHub</a>. It cannot be published here because it contains a lot of LaTeX formulas. 

<h2>Conclusions</h2>
<p>This paper represents the possibilities of Zynq-7000 SoC in
the cryptanalysis of integer factorization problem and discrete
logarithm problem based cryptosystems. It has been shown
that using of custom IP cores could accelerate so called sieving
part of modern numeric methods for solving of these problems.
The sieving unit (or the slave nod of distributed system) is
composed of four major parts, the random number generator
IP, the IP for checking of smoothness over rational factor base
and algebraic factor base and the ARM processor for managing
of the process. Paper also discussed the possibilities of parallel
approach in this process and also other improvements of used
numerical methods for solving of integer factorization and
discrete logarithm. The measurement shown that the relation
between bit size of input and the time for sieving is almost
exponential (that has been presumed) and the relation between
number of nods in the system and time spent for sieving is
linear (that also has been presumed).</p>

<h2>References</h2>
<p>
[1] L. H. Crockett, R. A. Elliot, M. A. Enderwitz and R. W. Stewart, The
Zynq Book, Strathclyde Academic Media, 2014, pp. 1-46. ISBN: 978-
0992978709<br>
[2] H. Delfs and H. Knebl, Introduction to Cryptography, 3rd ed. Springer,
Berlin, Heidelberg, 2015, pp. 49-112. doi: 10.1007/978-3-662-47974-2<br>
[3] V. P. Hoang, Integer factorization with the general number field sieve,
Rovaniemi University of Applied Sciences, 2008, pp. 39-58. ISBN: 978-
952-5153-78-1<br>
[4] G. d. Meulenaer, F. Gosset, G. M. d. Dormale and J. J. Quisquater,
&#8221;Integer Factorization Based on Elliptic Curve Method: Towards Better
Exploitation of Reconfigurable Hardware&#8221;, doi: 10.1109/FCCM.2007.12<br>
[5] P. Nguyen, &#8221;A Montgomery-like square root for the Number Field
Sieve&#8221;, Buhler J.P. (eds) Algorithmic Number Theory. ANTS 1998. Lec-
ture Notes in Computer Science, Vol. 1423. Springer, Berlin, Heidelberg<br>
[6] I. Niven, An Introduction to the Theory of Numbers, 5th ed. Wiley, 1991,
pp. 110-115. ISBN: 0-471-62546-9<br>
[7] G. Pandey and S. K. Pal, &#8221;Polynomial selection in number field sieve for
integer factorization&#8221;, Perspectives in Science, Vol. 8, 2016, pp. 101-103,
doi: 10.1016/j.pisc.2016.04.007.<br>
[8] Y. Y. Song, 2017, Computational Number Theory and Modern
Cryptography, Higher Education Press, 2017, pp. 191-260. doi:
10.1002/9781118188606.ch5<br>
[9] L. T. Yang, Ying Huang, J. Feng, Q. Pan and C. Zhu, &#8221;An improved
parallel block Lanczos algorithm over GF(2) for integer factorization&#8221;,
Information Sciences, doi: 10.1016/j.ins.2016.09.052.<br>
[10] L. T. Yang, G. Huang, J. Feng and L. Xu, &#8221;Parallel GNFS algorithm
integrated with parallel block Wiedemann algorithm for RSA security in
cloud computing&#8221;, Information Sciences, doi: 10.1016/j.ins.2016.10.017.</p>
"""

ENTITY = cr.Article(
    title="The acceleration of public–key cryptanalysis methods using Xilinx Zynq-7000",
    url_alias='the-acceleration-of-public-key-cryptanalysis-methods-using-xilinx-zynq-7000',
    large_image_path="images/hardware_big.jpg",
    small_image_path="images/hardware_small.jpg",
    date=datetime.datetime(2018, 11, 5),
    tags=[cr.Tag('Security', 'security'),
          cr.Tag('FPGA', 'FPGA'),
          cr.Tag('Hardware', 'hardware'),
          cr.Tag('Design', 'design'),
          cr.Tag('Cryptosystem', 'cryptosystem')],
    content=content,
    lead=lead
)
