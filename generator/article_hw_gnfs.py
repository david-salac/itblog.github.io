# The concept for an acceleration of public-key cryptanalysis methods
import datetime
import crinita as cr

lead = """The Xilinx Zynq-7000 SoC provides new possibilities for increasing the efficiency of cryptanalysis methods for the public-key systems such as RSA or Diffie-Hellman key exchange algorithm. These cryptosystems are based on the discrete logarithm and integer factorization problem. After a brief introduction to numerical methods for solving these problems, there is an introduction to the distributed system that aims to solve these problems."""

content = r"""<p class="lead">The Xilinx Zynq-7000 SoC provides new possibilities for increasing the efficiency of cryptanalysis methods for the public-key systems such as RSA or Diffie-Hellman key exchange algorithm. These cryptosystems are based on the discrete logarithm and integer factorization problem. After a brief introduction to numerical methods for solving these problems, there is an introduction to the distributed system that aims to solve these problems. A distributed system consists of master nodes that manage the distribution of the tasks and slave nodes that compute one of the most time-consuming parts of the selected numerical methods called sieving. Afterwards, the slave node is designed on Xilinx Zynq-7000 SoC consisting of an ARM processor for analyzing the problem and some custom IP cores running on FPGA to increase the algorithm's efficiency. The capabilities of the distributed system are also measured and analyzed afterwards.</p>

<h2>Introduction</h2>
<p>With the increasing computational potential of FPGA and the new approach of designing the specialized hardware, the security of public-key cryptosystems arises. This paper aims to analyze the possibilities of Xilinx Zynq-7000 SoC in solving integer factorization and discrete logarithm problems. It means it explores its potential on implementation of cryptanalysis methods for solving of mentioned problems.</p>  

<h2>Security of public-key cryptosystems</h2>
<p>There are many cyphers and protocols in a branch of public-key cryptography. But only methods based on the principle of simple integer factorization and discrete logarithm are relevant in this paper.</p>

<h3>Integer factorization problem</h3>
<p>An example of a cypher based on the principle of integer factorization problem is RSA cryptosystem that uses public-key <em class="equation">n</em> of format <em class="equation">n = pq</em> for some large prime numbers <em class="equation">p</em> and <em class="equation">q</em> and some integer <em class="equation">e</em> such that <span class="math"><em>e</em> ∤ <em>φ</em>(<em>n</em>)</span><!-- LATEX $e \nmid \varphi(n)$ LATEX -->, where <span class="math"><em>φ</em>(<em>n</em>)</span><!-- LATEX $\varphi(n)$ LATEX --> represents Euler's totient function. The security of this cypher is based on the toughness of finding numbers <em class="equation">p</em> and <em class="equation">q</em> for given number <em class="equation">n</em> that could be afterwards used to compute <span class="math"><em>φ</em>(<em>n</em>)</span><!-- LATEX $\varphi(n)$ LATEX --> and the value of private key <em class="equation">d</em>.</p>
<p>In general, integer factorization problem could be defined as searching for the decomposition of given positive integer <em class="equation">n</em> to the following format:</p>
<p class="center math"><em>n</em> = Π<sub><em>i</em> = 1</sub><sup>r</sup> <em>p</em><sub><em>i</em></sub><sup><em>a</em><sub>i</sub></sup></p>
<!-- LATEX $$ n = \prod_{i = 1}^r p_i^{a_i} $$ LATEX -->

<p>Where <span class="math"><em>p</em><sub><em>i</em></sub></span><!-- LATEX $p_i$ LATEX --> is a prime number and <span class="math"><em>a</em><sub><em>i</em></sub></span><!-- LATEX $a_i$ LATEX --> is a natural number (for each <span class="math"><em>i</em> = 1,2, ... ,<em>r</em></span><!-- LATEX $ i = 1,2, \cdots, r $ LATEX -->).</p>
<p>There are no known effective algorithms for solving this problem in polynomial time (except Shor's algorithm for quantum computers). The best-known algorithms for solving the integer factorization problem for large integers are:</p>
<ul>
    <li>Quadratic Sieve - for integers of size less than approximately <span class="math">10<sup>100</sup></span><!-- LATEX $ 10^{100} $ LATEX -->.</li>
    <li>General Number Field Sieve - for integers of length greater than approximately <span class="math">10<sup>100</sup></span><!-- LATEX $ 10^{100} $ LATEX -->.</li>
</ul>
<h3>Discrete logarithm problem</h3>
<p>The security of public-key cryptosystems could also be based on the discrete logarithm problem. For example, suppose that there is prime number <em class="equation">p</em> and the primitive root mod <em class="equation">p</em> - integer <em class="equation">g</em> and the random integer number <span class="math"><em>a</em> ∈ ℤ<sub><em>p</em></sub></span><!-- LATEX $ a \in \mathbb{Z}_p $ LATEX -->. Then, the discrete logarithm problem is searching for the value of integer <em class="equation">k</em> in the following congruence:</p>
<p class="center math"><em>g</em><sup><em>k</em></sup> ≡ <em>a</em> mod <em>p</em></p>
<!-- LATEX $$ g^k \equiv a \pmod{p} $$ LATEX -->
<p>There is no known effective algorithm (except Shor's algorithm for quantum computers). Therefore, numerical methods for solving this problem are usually based on a combination of the following methods: </p>
<ul>
    <li>Pohlig-Hellman algorithm: that could simplify the congruence.</li>
    <li>Index Calculus is the standard method (and the most effective one) for solving a discrete logarithm problem.</li>
</ul>
<p>The well-known public-key protocol based on this principle is Diffie-Hellman key exchange.</p>

<h3>Other approaches in public-key cryptography</h3>
<p>There are also many other public-key cryptosystems based on different principles. Especially the elliptic curve cryptography is well known. Many quantum-resistant algorithms based on some NP-complete problems are also available. Numerical methods for cryptanalysis of these algorithms are not the subject of this paper.</p>

<h2>A practical approach in cryptanalysis</h2>
<p>The only way how to succeed in solving some real cryptanalysis integer factorization or discrete logarithm problem is to use some of the mentioned numerical methods and parallel approaches for this purpose. The possibility of using the FPGA for accelerating some parts of mentioned numerical methods is discussed below.</p>
<h3>The parallel approach in integer factorization problem</h3>
<p>Each of the currently used methods for integer factorization is similar to (or based on) Dixon's Random Square Method. This method consists of two steps; the first one is called sieving the other is called matrix processing. Each of these steps could be distributed for many computational nodes.</p>

<p>The sieving part of the algorithm consists of searching for some smooth integers over some factor base <em class="equation">F</em> (that usually contains prime numbers, most typically, first <em class="equation">|F|</em> prime numbers). The method tries to find a set of integers <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX --> such that <span class="math"><em>n</em><sup>0.5</sup> ≤ <em>x</em><sub>i</sub> ≤ <em>n</em></span><!-- LATEX $ n^{0.5} \leq x_i \leq n $ LATEX --> and the value (<span class="math"><em>x</em><sub>i</sub><sup>2</sup> mod <em>n</em></span><!-- LATEX $ x_i^2 \pmod{n} $ LATEX -->) is smooth over a set <em class="equation">F</em>. It means that there exists the following decomposition:</p>
<p class="center math"><em>x</em><sub><em>i</em></sub><sup>2</sup> mod <em>n</em> = Π<sub><em>p</em><sub><em>j</em></sub> ∈ <em>F</em>, <em>e</em><sub><em>ij</em></sub> ∈ ℤ<sup>+</sup> </sub> <em>p<sub>j</sub></em><sup><em>e<sub>ij</sub></em></sup></p>
<!-- LATEX $$ x_i^2 \mod n = \prod_{p_j \in F, e_{ij} \in \mathbb{Z}^+} p_j^{e_{ij}}  $$ LATEX -->
<p>The algorithm has to find at least (<span class="math"><em>|F|</em> + 1</span><!-- LATEX $ |F| + 1 $ LATEX -->) of such integers <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX -->. This process could be easily distributed to as many nodes as possible. Each node generates the random value <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX --> and checks the smoothness of <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX --> over the factor base <em class="equation">F</em>. Other algorithms (especially General Number Field Sieve and Quadratic Sieve) have a sieving part equivalent to the represented ones. The sieving part of the algorithm is usually the slower one, and it is susceptible to selecting the correct value of the method's parameters. </p>
<p>The matrix processing part of the algorithm consists of computing the null space of a matrix of the exponents <span class="math"><em>e<sub>ij</sub></em></span><!-- LATEX $ e_{ij} $ LATEX --> found in step over finite <span class="math">ℤ<sub>2</sub></span><!-- LATEX $ \mathbb{Z}_2 $ LATEX --> field (because only the parity of exponents is relevant). Because of the sparsity of the given matrix, the block Lanczos algorithm could be used in this process as the most effective serial (single node) option. The size of the matrix in the realistic example is about <span class="math">10<sup>6</sup></span><!-- LATEX $ 10^6 $ LATEX --> rows and columns (for <span class="math"><em>n</em> > 2<sup>512</sup></span><!-- LATEX $ n > 2^{512} $ LATEX -->). The other method for computing the null space of a sparse matrix is the Wiedemann algorithm, which could be distributed to many computational nodes.</p>
<p>After the matrix processing part, the values of integers <em class="equation">x</em> and <em class="equation">y</em> are found such that:</p>

<p class="center math"><em>x</em><sup>2</sup> ≡ <em>y</em><sup>2</sup> mod <em>n</em> ∧ <em>x</em> ≢ ± y mod <em>n</em></p>
<!-- LATEX $$ x^2 \equiv y^2 \pmod{n} \land x \not\equiv \pm y \pmod{n} $$ LATEX -->

<p>The value GCD(<span class="math"><em>x</em> ± <em>y</em>, <em>n</em></span><!-- LATEX $ x \pm y, n $ LATEX -->) could be a non-trivial divider of a given composed integer <em class="equation">n</em>.</p>

<h3>The parallel approach in discrete logarithm problem</h3>
<p>The Pohlig-Hellman algorithm contains the step in which the value (<span class="math"><em>p</em> - 1</span><!-- LATEX $ p - 1 $ LATEX -->) is factorized (usually using some of the mentioned methods). In fact, the Pohling-Hellman algorithm could only be helpful when dealing with special cases, usually in case of security errors during implementation (like improperly selected keys).</p>

<p>Index Calculus method is the universal one. It also contains the sieving part and the matrix processing part. The sieving part is the same as the sieving part of Dixon's factorization method. The algorithm works with factor base <em class="equation">F</em> (usually composed of first <span class="math">|<em>F</em>|</span><!-- LATEX $ |F| $ LATEX --> prime numbers) and checks the smoothness of values (<span class="math"><em>g</em><sup><em>x<sub>i</sub></em></sup> mod <em>p</em></span><!-- LATEX $ g^{x_i} \pmod{p} $ LATEX -->) over factor base <em class="equation">F</em> (for some random integer <span class="math"><em>x<sub>i</sub></em> ∈ ℤ<sub><em>p</em> - 1</sub></span><!-- LATEX $ x_i \in \mathbb{Z}_p $ LATEX -->). For example, the value could be expressed in the following way:</p>

<p class="center math"><em>g</em><sup><em>x<sub>i</sub></sup></em> mod <em>p</em> = Π<sub><em>p</em><sub><em>j</em></sub> ∈ <em>F</em>, <em>e</em><sub><em>ij</em></sub> ∈ ℤ<sup>+</sup> </sub> <em>p<sub>j</sub></em><sup><em>e<sub>ij</sub></em></sup></p>
<!-- LATEX $$ g^{x_i} \mod p = \prod_{p_j \in F, e_{ij} \in \mathbb{Z}^+ } p_j^{e_{ij}} $$ LATEX -->

<p>This part of the algorithm could be easily distributed to many nodes, which is similar to the sieving part of the integer factorization problem methods. First, index calculus has to find the set of integers <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX --> of cardinality <span class="math">|<em>F</em>|</span><!-- LATEX $ |F| $ LATEX --> such that the matrix composed of exponents <span class="math"><em>e<sub>ij</sub></em></span><!-- LATEX $ e_{ij} $ LATEX --> that fits the equation above is regular in the <span class="math">ℤ<sub><em>p</em> - 1</em></sub></span><!-- LATEX $ \mathbb{Z}_{p-1} $ LATEX --> ring.</p>

<p>The matrix processing part of the Index Calculus algorithm differs significantly. The most significant difference is that it works on ring <span class="math">ℤ<sub>φ(<em>p</em></sub></span><!-- LATEX $ \mathbb{Z}_{\varphi(p)} $ LATEX --> (where <span class="math">φ(<em>p</em>)=<em>p</em> - 1</span><!-- LATEX $ \varphi(p) = p-1 $ LATEX --> is the value of Euler's totient function of prime number <em class="equation">p</em>). Unfortunately, this ring is not the field as the value <span class="math"><em>p</em> - 1</span><!-- LATEX $ p-1 $ LATEX --> is always a composite number for large primes (in opposite to <span class="math">ℤ<sub>2</sub></span><!-- LATEX $ \mathbb{Z}_2 $ LATEX -->) which means that there is no effective algorithm for solving this equation set. Practically, only a variation of the Gaussian elimination can be used in this situation.</p>

<h3>Improvements of considered algorithms</h3>
<p>There is also a possibility of improvement of a particular numerical method itself. Many enhancements of each numerical method have been presented since 1990. It leads to an increase in the efficiency of each method. The most remarkable improvement has been noticed in the GNFS method (because it is the only effective method for larger integers). The most critical improvement (relatively to this paper) has been achieved in selecting a polynomial for the GNFS method. The runtime of methods depends especially on the choice of good polynomial pairs. Another essential part of the GNFS method is computing the square root value, which has also been improved.</p>

<h2>The design of a distributed system</h2>
<p>The distributed system has been designed to improve the sieving part of the General number field sieve algorithm and other methods (especially Index Calculus). It is composed of one master node that distributes the task to each slave node used for computing. </p>

<h3>The master nod</h3>
<p>The principal purpose of master node is specified in the following enumeration:</p>
<ul>
<li>Analyze of given cryptanalysis problem.</li>
<li>Preprocessing of the assigned task and computing of the parameters of selected numerical methods.</li>
<li>Managing the network of slave nodes.</li>
<li>Postprocessing, especially the matrix processing problem.</li>
<li>Representing of the results in some acceptable form.</li>
</ul>
<p>The system has to analyze whether the given problem fits some pattern. Especially whether given number <em class="equation">n</em> that should be factorized is an odd composed number that is not <em class="equation">k</em>-smooth for some relatively small value of <em class="equation">k</em> or whether given modulus <em class="equation">p</em> in discrete logarithm problem is a prime number and the generator <em class="equation">g</em> is a primitive root mod <em class="equation">p</em>.</p>
<figure>
    <img src="images/hw_masterslave.png" alt="The composition of distributed application">
    <figcaption>Figure 1: The composition of distributed application</figcaption>
</figure>

<p>Pre-processing of input is another crucial part of the algorithm. For example, the discrete logarithm analysis contains the factorization of (<span class="math"><em>p</em> - 1</span><!-- LATEX $ p - 1 $ LATEX -->) that could be used in the Pohlig-Hellman algorithm. Moreover, the computation of all other parameters of numerical methods is an essential part of this step. It includes finding the suitable composition of each factor base (rational factor base is composed of prime numbers, and in the case of GNFS method, there is also algebraic factor base with similar composition) and other relevant parameters (for example, searching for proper value coefficients of the polynomial in GNFS method). </p>
<p>Another important function of the master node is to handle network communication. It consists of distributing current tasks and parameters of numerical methods. A master node also has to fetch computed values (smooth over the given factor base) from slave nodes, check them and save them for the matrix processing part.</p>
<p>A master node also implements Montgomery's block Lanczos algorithm for computing of null space of found matrix over the <span class="math">ℤ<sub>2</sub></span><!-- LATEX $ \mathbb{Z}_2 $ LATEX --> field (in case of the integer factorization problem) and Gaussian elimination method over <span class="math">ℤ<sub><em>p</em> - 1</sub></span><!-- LATEX $ \mathbb{Z}_{p-1} $ LATEX --> ring (in case of the discrete logarithm problem). After the sequence of computations, it also has to verify computed results (and skip or repeat some previous steps if the result is wrong).</p>
<p>Last but not least function of the master node is to save found values or represent results in some human-readable form.</p>
<h3>The slave nod</h3>
<p>The most crucial feature of slave node is to compute values of the sieving process. This process is slightly different in each numerical method:</p>
<ul>
    <li><strong>Quadratic Sieve:</strong> method works with factor base of the form <span class="math">{<em>n</em> mod <em>p</em> / <em>p</em>} = 1</span><!-- LATEX $ \left( \frac{n \mod p}{p} \right) = 1 $ LATEX --> for each <span class="math"><em>p</em> ∈ <em>F</em></span><!-- LATEX $ p \in F $ LATEX --> (where <span class="math">{<em>a</em> / <em>p</em>}</span><!-- LATEX $ \left( \frac{a}{p} \right) $ LATEX --> is a Legendre symbol) and computes the smoothness of <span class="math"><em>x<sub>i</sub></em></span><!-- LATEX $ x_i $ LATEX --> inversely from <span class="math"><em>p</em> ∈ <em>F</em></span><!-- LATEX $ p \in F $ LATEX --> using Tonelli-Shanks algorithm.</li>
    <li><strong>GNFS:</strong> method works with three different factor bases called algebraic factor base (composed of first degree prime ideals in integer pair representation), rational factor base (consisting of prime numbers), and quadratic characteristic factor base (to verify smoothness). Slave node computes only values that are smooth over rational and algebraic factor base. Quadratic characteristic values are calculated afterwards separately.</li>
    <li><strong>Index Calculus:</strong> method works with standard factor base composed of prime numbers.</li>
</ul>

<p>This process requires the fast generator of random numbers and some fast algorithm for computing reminders after dividing the given random number and the prime number in the factor base. Another essential feature of the algorithm is effective working with large numbers (typically bigger than <span class="math">10<sup>100</sup></span><!-- LATEX $ 10^{100} $ LATEX -->). </p>
<p>Another essential feature of slave node is periodically fetching commands from a master node and sending results back to master nod.</p>

<h2>The FPGA approach</h2>
<p>The suitable way for implementation of the slave node is to use Zynq-7000 SoC. It contains an ARM-based processor with programmable FPGA. Program running on processor implements the interface for communication with a master node and manages custom IP cores' properties. The IP cores created on FPGA implement the functionality relevant for the selected method. There are the following relevant IP cores in the system:</p>
<ul>
    <li><strong>Random number generator IP:</strong> generates relevant random numbers and checks their properties (for example, the GNFS method operates with two coprime numbers, while other methods operate with one random integer in some interval). </li>
    <li><strong>Rational smoothness checking IP:</strong> that verifies whether a given integer is smooth over some factor base, consists of integers (rational factor base in GNFS method).</li>
    <li><strong>Algebraic smoothness checking IP:</strong> checks whether an input is smooth over some algebraic factor base (only GNFS operates with this concept).</li>
</ul>
<figure>
    <img src="images/hw_processor.png" alt="Scheme of IP cores of the Zynq system">
    <figcaption>Figure 2: Scheme of IP cores of the Zynq system</figcaption>
</figure>

<p>The scheme in the picture above is simplified, but it presents the principle aptly. Many other cores are practically used in the system (for example, the core for ethernet communication). </p>
<p>Rational smoothness checking on FPGA has been the subject of many improvements. For example, there is a possibility of checking whether the given input is <em class="equation">k</em>-smooth for some relatively small integer <em class="equation">k</em> using the Elliptic Curve Method that has already been implemented on FPGA.</p>
<h2>Results of measurement</h2>
<p>After the implementation of the distributed system, the measurement of its features has been performed.</p>
<h3>Integer factorization problem</h3>
<p>It is reasonable to presume that the dependency of numbers of nodes (slaves) in the system and the time required for solving the task is approximately (<span class="math"><em>T</em><sub>0</sub> / <em>S</em></span><!-- LATEX $ \frac{T_0}{S} $ LATEX -->) where <span class="math"><em>T</em><sub>0</sub></span><!-- LATEX $ T_0 $ LATEX --> is the time required by a single node and <em class="equation">S</em> is the number of nodes connected to the system. By using exponential regression following pattern for computing of <span class="math"><em>T</em><sub>0</sub></span><!-- LATEX $ T_0 $ LATEX --> has been found:</p>
<p class="center math"><em>T</em><sub>0</sub> = 0.31 · 10<sup>-3</sup> · exp(0.05 · <em>N</em>)</p>
<!-- LATEX $$ T_0 = 0.31 \cdot 10^{-3} \cdot \exp(0.05 \cdot N) $$ LATEX -->
<p>Where <em class="equation">N</em> represents the bit size of the input (<span class="math"><em>T</em><sub>0</sub></span><!-- LATEX $ T_0 $ LATEX --> in seconds), measured results are shown in the graph below.</p>
<figure>
    <img src="images/hw_rsa.png" alt="Dependency of time to bit size of the input (integer factorization problem)">
    <figcaption>Figure 3: Dependency of time to bit size of the input (integer factorization problem)</figcaption>
</figure>
<p>The presumption of dependency of numbers of nodes (slaves) in the system and the time required for solving the task has also been confirmed (<span class="math"><em>t</em> = <em>T</em><sub>0</sub> / <em>S</em></span><!-- LATEX $ t = \frac{T_0}{S} $ LATEX -->).</p>
<h3>Discrete logarithm problem</h3>
<p>Methods for solving the discrete logarithm problem are less effective than the methods for solving the integer factorization problem. This leads to working with input of size smaller than in previous measurements. However, general presumptions, if it comes to vertical scalability, are the same as above.</p>
<figure>
    <img src="images/hw_dh.png" alt="Dependency of time to bit size of the input (discrete logarithm problem)">
    <figcaption>Figure 4: Dependency of time to bit size of the input (discrete logarithm problem)</figcaption>
</figure>
<p>Exponential regression of measured values returns the following result:</p>
<p class="center math"><em>T</em><sub>0</sub> = 8.85 · 10<sup>-7</sup> · exp(0.38 · <em>N</em>)</p>
<!-- LATEX $$ T_0 = 8.85 \cdot 10^{-7} \cdot \exp(0.38 \cdot N) $$ LATEX -->

<p>Where <em class="equation">N</em> represents the bit size of the input (<span class="math"><em>T</em><sub>0</sub></span><!-- LATEX $ T_0 $ LATEX --> in seconds). The presumption of dependency of numbers of nodes (slaves) in the system and the time required for solving the task has also been confirmed as <span class="math"><em>t</em> = <em>T</em><sub>0</sub> / <em>S</em></span><!-- LATEX $ t= \frac{T_0}{S} $ LATEX -->.</p>
<h2>Conclusions</h2>
<p>This paper represents the possibilities of Zynq-7000 SoC in the cryptanalysis of the integer factorization problem and discrete logarithm problem-based cryptosystems. It has been shown that using custom IP cores could accelerate the sieving part of modern numeric methods for solving these problems. The sieving unit (or the slave node of a distributed system) comprises four major components: the random number generator IP, the IP for checking smoothness over rational factor base and algebraic factor base, and the ARM processor for managing the process. The paper also discussed the possibilities of a parallel approach in this process and other improvements of used numerical methods for solving integer factorization and discrete logarithm. The measurement shows that the relation between the bit size of the input and the time for sieving is almost exponential (that had been presumed). On the other hand, the relation between the number of nodes in the system and time spent for sieving is linear (also had been assumed).</p>

<h2>References</h2>
<p>
[1] L. H. Crockett, R. A. Elliot, M. A. Enderwitz and R. W. Stewart, The
Zynq Book, Strathclyde Academic Media, 2014, pp. 1-46. ISBN: 978-
0992978709</p><p>
[2] H. Delfs and H. Knebl, Introduction to Cryptography, 3rd ed. Springer,
Berlin, Heidelberg, 2015, pp. 49-112. doi: 10.1007/978-3-662-47974-2</p><p>
[3] V. P. Hoang, Integer factorization with the general number field sieve,
Rovaniemi University of Applied Sciences, 2008, pp. 39-58. ISBN: 978-
952-5153-78-1</p><p>
[4] G. d. Meulenaer, F. Gosset, G. M. d. Dormale and J. J. Quisquater,
"Integer Factorization Based on Elliptic Curve Method: Towards Better
Exploitation of Reconfigurable Hardware";, doi: 10.1109/FCCM.2007.12</p><p>
[5] P. Nguyen, ";A Montgomery-like square root for the Number Field
Sieve";, Buhler J.P. (eds) Algorithmic Number Theory. ANTS 1998. Lec-
ture Notes in Computer Science, Vol. 1423. Springer, Berlin, Heidelberg</p><p>
[6] I. Niven, An Introduction to the Theory of Numbers, 5th ed. Wiley, 1991,
pp. 110-115. ISBN: 0-471-62546-9</p><p>
[7] G. Pandey and S. K. Pal, ";Polynomial selection in number field sieve for
integer factorization";, Perspectives in Science, Vol. 8, 2016, pp. 101-103,
doi: 10.1016/j.pisc.2016.04.007.</p><p>
[8] Y. Y. Song, 2017, Computational Number Theory and Modern
Cryptography, Higher Education Press, 2017, pp. 191-260. doi:
10.1002/9781118188606.ch5</p><p>
[9] L. T. Yang, Ying Huang, J. Feng, Q. Pan and C. Zhu, ";An improved
parallel block Lanczos algorithm over GF(2) for integer factorization";,
Information Sciences, doi: 10.1016/j.ins.2016.09.052.</p><p>
[10] L. T. Yang, G. Huang, J. Feng and L. Xu, ";Parallel GNFS algorithm
integrated with parallel block Wiedemann algorithm for RSA security in
cloud computing";, Information Sciences, doi: 10.1016/j.ins.2016.10.017.</p>
"""

ENTITY = cr.Article(
    title="The concept for an acceleration of public-key cryptanalysis methods",
    url_alias='the-concept-for-an-acceleration-of-public-key-cryptanalysis-methods',
    large_image_path="images/hardware_big.jpg",
    small_image_path="images/hardware_small.jpg",
    date=datetime.datetime(2018, 11, 5),
    tags=[cr.Tag('Security', 'security'),
          cr.Tag('FPGA', 'FPGA'),
          cr.Tag('Hardware', 'hardware'),
          cr.Tag('Design', 'design'),
          cr.Tag('Cryptosystem', 'cryptosystem')],
    content=content,
    lead=lead,
    description="This article presents a new way of dealing with integer factorization and discrete logarithm problems from a custom hardware perspective with Zynq-7000 as SoC FPGA."  # noqa: E501
)
