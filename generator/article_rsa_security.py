# The security perspective of RSA cryptosystem
import datetime
import crinita as cr

lead = """Currently, the most popular public-key cryptosystem is still RSA. It is even though more sophisticated and secure systems are available (including quantum-resistant ones). It is probably due to the relative simplicity of the algorithm, long history and general technical support. On the other hand, considering the advancement in quantum computers development and programmable hardware, the security of this cryptosystem is becoming more and more questionable."""

content = """<p class="lead">Currently, the most popular public-key cryptosystem is still RSA. It is even though more sophisticated and secure systems are available (including quantum-resistant ones). It is probably due to the relative simplicity of the algorithm, long history and general technical support. On the other hand, considering the advancement in quantum computers development and programmable hardware, the security of this cryptosystem is becoming more and more questionable. Therefore, this article tends to analyse possibilities of direct attack to the RSA algorithm in 2019.</p>

<h2>The RSA cryptosystem</h2>
<p>The logic of the RSA cypher is straightforward. Let <em>p</em>, <em>q</em> be random large numbers (at least 512 bits of size). Then let <em>n</em> = <em>pq</em> represent the public key. Euler totient function of n is φ(<em>n</em>) = (<em>p</em> - 1)(<em>q</em> - 1). Then choose some (typically small) number e with no non-trivial common divider with φ(n) - this is another public key. Then compute <em>d</em>, such that <em>de</em> ≡ 1 (mod φ(<em>n</em>)): the extended Euler algorithm could be used to find these values.</p>

<p>For encryption of message <em>m</em> follow the logic:</p>
<p class="center"><em>c</em> &#8801; <em>m<sup>e</sup></em> (mod <em>n</em>)</p>

<p>For decryption of cypher <em>c</em> follow the logic:</p>
<p class="center"><em>d</em> &#8801; <em>c<sup>d</sup></em> (mod <em>n</em>)</p>

<p>Current security standards define the bit size of the public-key <em>n</em> to be at least 1024 bits.</p>

<h2>The way of attacking the cypher</h2>
<p>The cypher could be attacked by finding the value of prime numbers p, q (a problem called integer factorization) or by finding the value of private key d (a problem called discrete logarithm). The last option is to guess the message. Fortunately for security, all these issues are computationally challenging.</p>

<p>The typical way how to successfully attack (which means decrypting some message without knowing the private key) cypher is to exploit implementation errors. Unfortunately, the RSA cryptosystem is very susceptible to many implementation errors. Many publicly available implementations have weaknesses that lead to the correct guess of private key prime numbers. These weaknesses are well known and could be avoided using the correct design.</p>

<p>Besides exploiting the implementation error, there are two practically available methods. First, use Shor's algorithm running on the quantum computers and another one using the conventional techniques for integer factorization – typically some quick implementation of GNFS (General Number Field Sieve) method.</p>

<h3>The perspective of Shor's algorithm</h3>
<p>Shor's algorithm requires a universal quantum computer. In an original paper, Peter Shor shows that you need at least an <em>N</em> quantum bit machine for the correct factorization (as well as for solving the discrete logarithm problem) of the <em>N</em> bit integer (modulus). During the past 30 years, there has been an enormous development in this area. The current record (2019) in a quantum computer is the Q System One, designed by IBM, with 20 quantum bits. This is still not sufficient for the attack of the 1024-bit RSA.</p>

<p>On the other hand, it is useful to consider that just eight years ago (2010), only two qubits universal quantum computer were revealed as an absolute science miracle. Therefore, we can expect an exponential increase in the power of quantum machines in consecutive years. Furthermore, many well-known companies (Google, Microsoft, IBM) are currently running their engineering projects to build more powerful quantum computer machines.</p>

<p>Quantum computers can indeed represent a suitable way to attack RSA successfully soon. But it is not the object of this article to speculate when the 1024 qubit universal quantum computer will be available or whether it will be available at all. The author is quite sceptical that there will be much progress in the next 20 years - but nobody knows.</p>

<p>It is also important to say that quantum computers threaten RSA and almost all currently wide-spread public-key cryptosystems. Shor's algorithm can efficiently solve discrete logarithm problems, an underpinning principle to practically all wide-spread public-key algorithms (like Diffie-Hellman key exchange, Elliptic curves-based algorithm, and RSA).</p>

<h2>The perspective of the GNFS method on custom's devices</h2>
<p>Another approach is to use the GNFS factorization method. GNFS (acronym of the General Number Field Sieve) is the most effective way how to solve integer factorization (for big numbers, up to 100 decimal digits) on standard (non-quantum) computers. There was a considerable progression in this field at the beginning of the century (up to the year 2010). Nowadays, the popularity of the fast implementation of GNFS has fallen (considering the number of new scientific articles on this issue). On the other hand, the current state of research shows promising possibilities.</p>

<p>In principle, GNFS is an enhancement of Dixon's random square factorization method. The enhancement is the use of the algebraic number fields structures. Former Dixon's method is based on the logic that a suitable way how to factorize number <em>n</em> is to find two integers <em>x</em>, <em>y</em> such that:</p>

<p class="center"><span style="padding-right: 20px">(1)</span> <em>x</em><sup>2</sup> &#8801; <em>y</em><sup>2</sup> (mod <em>n</em>)</p>

<p>In this case, there is a high probability that numbers (<em>x</em>-<em>y</em>) or (<em>x</em>+<em>y</em>) are non-trivial dividers of <em>n</em>.</p>

<p>Finding such numbers (<em>x</em>, <em>y</em>) is computationally much easier than using brute force to factorize <em>n</em>. The logic is based on the process called sieving. It technically works so that there is some set <em>F</em> (composed of first <em>k</em> integers with some reasonably high value of <em>k</em>), and an algorithm generates random integers <em>z</em> and computes factorization of <em>z</em> over factor base <em>F</em>. If <em>z</em> is smooth over <em>F</em>, values of exponents are saved as a vector. In the end, if there are at least |<em>F</em>| + 1 values generated, there is some linear combination that can create a combination for equation (1). The sieving is the most time-consuming part of the algorithm. The enhancement of the GNFS is that it uses a slightly different factor base and slightly different inputs, but the overall logic is the same.</p>

<h3>Current situation of GNFS implementations</h3>
<p>There is a competition called RSA Factoring Challenge, where anyone can see current milestones in attacks to RSA. The last one is from August 2018, when Samuel S. Gross successfully factorized the 762 bits large number. The number with 768 bits was factorized too in 2009 (it had been factorized previously probably because of a prize that authors could win).</p>

<p>Each of these challenges has been done on GPU chips. Interestingly, there is no suitable implementation of the GNFS method on custom's hardware (FPGA). There was an attempt at the COPACOBANA project in 2007. Alas, it was far from being completed. New FPGA chips offer a great possibility of how to implement effective numerical methods and increase algorithm efficiency.</p>

<p>Despite this successful attempt, there is still a lot to be done before factorizing 1024 bits RSA can be done. On the other hand, it is meaningful that 1024-RSA could be considered endangered and should not be used for critical infrastructure. Many replacements for RSA do not represent a security risk, including quantum-resistant algorithms (i. g., Lattice-based cryptography).</p>

<h3>Possible improvements to GNFS implementation</h3>
<p>The sieving process (the most time-consuming step of the algorithm) can be improved on custom hardware. It is to check the divisibility of the input first, rather than to divide. Checking divisibility with fixed modulus differs from division itself and can be mathematically optimized - the underpinning principle based on divisibility rules. </p>
<p>In principle, each number written in any numeral system can be rewritten in the format like this:</p>
<p class="center">167 = (10100111)<sub>2</sub> = 1 ⋅ 2<sup>0</sup> + 1 ⋅ 2<sup>1</sup> + 1 ⋅ 2<sup>2</sup> + 0 ⋅ 2<sup>3</sup> + 0 ⋅ 2<sup>4</sup> + 1 ⋅ 2<sup>5</sup> + 0 ⋅ 2<sup>6</sup> + 1 ⋅ 2<sup>7</sup></p>
<p>in this case, we rewrite the binary number 10100111 as a sum of the multiplication of each digit with an exponent of its position.</p>
<p>If you rewrite the number in this format, what is interesting is its behaviour towards some fixed modulus. As mentioned above, you need to test whether the number is divisible by the set of known prime numbers (in the sieving process of GNFS). So, these divisors (in this case, modulus) are known in advance. If you had the number theory lesson, you would know what congruence means. Say that we want to express divisibility by number 5:</p>
<p class="center">
167 &#8801; 
(10100111)<sub>2</sub> &#8801; 
1 ⋅ 2<sup>0</sup> + 1 ⋅ 2<sup>1</sup> + 1 ⋅ 2<sup>2</sup> + 0 ⋅ 2<sup>3</sup> + 0 ⋅ 2<sup>4</sup> + 1 ⋅ 2<sup>5</sup> + 0 ⋅ 2<sup>6</sup> + 1 ⋅ 2<sup>7</sup> &#8801; 
1 ⋅ 1 + 1 ⋅ 2 + 1 ⋅ 4 + 0 ⋅ 3 + 0 ⋅ 1 + 1 ⋅ 2 + 0 ⋅ 4 + 1 ⋅ 3 &#8801;
12 (mod 5)
</p>

<p>As you can see, we just rewrote numbers on the right side in its form modulo 5 (all exponents of two recomputed as their value module 5). This would work for every modulus. But this is a game-changer. The number on the right side is much smaller than the number on the left side. Also, an algorithm for multiplication is straightforward and fast (compared to division) from the hardware perspective. You can also apply this rule recursively. So, after you minimize the number sufficiently, you can check the divisibility simply by division with a reminder (dividing small numbers is fast enough).</p>
<p>The presented way provides a good base for the optimization of the GNFS algorithm. You can also use the feature of the new FPGA that allows re-programming its content based on a specific condition (for example, check the divisibility of some input chunk of integers towards some subset of factor base in each step). Also, you can use the pipeline logic to optimize throughput.</p>

<h2>Optimizations on the client-side</h2>
<p>As mentioned above, it is critically important to implement RSA correctly on the client-side. However, there are many problems related to successful implementation. Arguably the most crucial issue is the random number generation. It is not trivial to generate truly random numbers on the deterministic device (which means all computers, terminals and similar). This is also the reason why random numbers are called pseud-random in the branch of information technologies. It is therefore essential to follow standards and avoid custom implementation whenever possible. If you are forced to use some custom solution, pay extra attention to random integer generation.</p>
<p>Another problem related to implementation is verifying whether an input is a prime number or not (a critical feature from the security point of view). The only correct approach is to use a combination of some quick algorithm (like the Euler pseudoprime test) and AKS test (that can answer whether the input is prime with 100% confidence). The logic for this split is that the Euler pseudoprime test is much faster than AKS - so you can quickly sieve inputs before using the AKS test. It is also worth noting that many developers (and mathematicians) are still not aware that the prime test can be done with absolute confidence with a deterministic algorithm working in polynomial time. Mentioned AKS test (Agrawal, Kayal, Saxena primality test) was presented in 2002 (so it's still a relatively new algorithm). There are many implementations already available (and worth using).</p>

<h2>Conclusions</h2>
<p>Even though there is no known method of successfully attacking RSA with 1024 bit key, such a method can probably be created shortly. There are two main threats to RSA security. The first one is represented by quantum computers and the fast implementation of the GNFS factorization method. We can expect advancement in both shortly. Quantum computers are the subject of intensive research by large companies such as Google, IBM, Microsoft. GNFS factorization method can now be implemented in a highly effective form on customer's devices (FPGA), which now has more significant potential than ever before. Due to these facts, it is highly recommended to update your systems from RSA to different cryptosystems, optimally quantum-resistant ones, or increase modulus size to 4096 bites.</p>
"""

ENTITY = cr.Article(
    title="The security perspective of RSA cryptosystem",
    url_alias='the-security-perspective-of-rsa-cryptosystem',
    large_image_path="images/security_big.jpg",
    small_image_path="images/security_small.jpg",
    date=datetime.datetime(2019, 1, 22),
    tags=[cr.Tag('Security', 'security'),
          cr.Tag('Web application', 'web-application'),
          cr.Tag('RSA', 'rsa'),
          cr.Tag('Design', 'design'),
          cr.Tag('Cryptosystem', 'cryptosystem')],
    content=content,
    lead=lead
)
