# The security perspective of RSA cryptosystem
import datetime
import crinita as cr

lead = """Currently, the most popular public-key cryptosystem is still RSA. It is despite the fact that more sophisticated and secure systems are available (including quantum resistant ones). It is probably due to the relative simplicity of the algorithm, long history and available technical support. On the other hand, considering advancement in quantum computers development as well as in programmable hardware, the security of this cryptosystem is becoming more and more questionable."""

content = """Currently, the most popular public-key cryptosystem is still RSA. It is despite the fact that more sophisticated and secure systems are available (including quantum resistant ones). It is probably due to the relative simplicity of the algorithm, long history and available technical support. On the other hand, considering advancement in quantum computers development as well as in programmable hardware, the security of this cryptosystem is becoming more and more questionable. This article tends to analyze possibilities of direct attack to the RSA algorithm in 2019.

        <h2>The RSA cryptosystem</h2>
        <p>The logic of the RSA cypher is straightforward. Let <em>p</em>, <em>q</em> are random large numbers (at least 512 bits of size). Then let <em>n = pq</em> represents the public key. Euler totient function of n is φ(<em>n</em>) = (<em>p</em>-1)(<em>q</em>-1). Then choose some (typically small) number <em>e</em> that has no non-trivial common divider with φ(<em>n</em>) - this is another public-key. Then compute <em>d</em>, such that <em>de</em> &#8801; 1 (mod φ(<em>n</em>)): to find is extended Euler algorithm could be used.</p>

        <p>For encryption of message <em>m</em> follow the logic:</p>
        <p><em>c</em> &#8801; <em>m<sup>e</sup></em> (mod <em>n</em>)</p>

        <p>For decryption of cypher <em>c</em> follow the logic:</p>
        <p><em>d</em> &#8801; <em>c<sup>d</sup></em> (mod <em>n</em>)</p>

        <p>Current security standards define the bit size of the public-key <em>n</em> to be at least 1024 bits. </p>

        <h2>The way of attacking the cypher</h2>
        <p>The cypher could be attacked by finding the value of prime numbers <em>p</em>, <em>q</em> (which is a problem called integer factorization) or by finding the value of private key <em>d</em> (a problem called discrete logarithm). Both of these issues are computationally challenging. </p>

        <p>The typical way how to successfully attack (which means decrypt some message without knowing the private key) cypher is to exploit implementation errors. The RSA cryptosystem is very susceptible to many implementation errors. Many publicly available implementations have weaknesses that lead to the correct guess of private key prime numbers. This weaknesses are well known and could possibly be avoided using correct design. </p>

        <p>Besides of exploiting the implementation error there two practically available methods. First, use the Shor's algorithm running on the quantum computers and another one using the conventional methods for integer factorization &#8211; typically some quick implementation of GNFS (General Number Field Sieve) method.</p>

        <h3>The perspective of Shor's algorithm</h3>
        <p>Shor's algorithm requires a universal quantum computer. In an original paper, Peter Shor shows that for the correct factorization (as well as for solving of discrete logarithm problem) of the <em>N</em> bit integer (modulus) you need at least <em>N</em> quantum bit machine. During the past 30 years, there has been an enormous development in this area. The current record (2019) in a quantum computer is the <em>Q System One</em> designed by IBM which has 20 quantum bits. This is still not sufficient for the attack of the 1024 bit RSA. On the other hand, it is useful to consider that just eight years ago (2010) only 2 qubits universal quantum computer had been revealed as an absolute science miracle. We can expect an exponential increase in the power of quantum machines in consecutive years. Many well-known companies (Google, Microsoft, IBM) are currently running their engineering projects to build more and more powerful quantum computer machines. </p>

        <p>It is true that quantum computers can in nearby future represents a suitable way how to attack RSA successfully. But it is not the object of this article to speculate when the 1024 qubit universal quantum computer will be available or whether it will be available at all. </p>

        <p>It is also important to say that quantum computers threats not only RSA but almost all currently available public-key cryptosystems. Simply because nearly everything besides RSA is based on discrete logarithm or elliptic-curve discrete logarithm problem, both can be solved effectively using Shor's algorithm.</p>

        <h2>The perspective of the GNFS method on custom's devices</h2>
        <p>Another approach is to use GNFS factorization method. GNFS (acronym of the General Number Field Sieve) is the most effective way how to solve integer factorization (for big numbers, up to 100 decimal digit) on standard (non-quantum) computers. There was a huge progression in this field at the beginning of the century (up to the year 2010). Nowadays the popularity of the fast implementation of GNFS has plummeted (considering the number of new scientific articles on this issue). On the other hand, the current state of research shows promising possibilities. </p>

        <p>In principle, GNFS is an enhancement of Dixon's random square factorization method. The enhancement is the using of the algebraic number fields structures. Former Dixon's method is based on the logic that a suitable way how to factorize number <em>n</em> is to find two integers <em>x</em>, <em>y</em> such that: </p>

        <p><span style="padding-right: 20px">(1)</span> <em>x</em><sup>2</sup> &#8801; <em>y</em><sup>2</sup> (mod <em>n</em>)</p>

        <p>In this case, there is a high probability that numbers (<em>x</em>-<em>y</em>) or (<em>x</em>+<em>y</em>) are non-trivial dividers of <em>n</em>.</p>

        <p>Finding of such numbers (<em>x</em>, <em>y</em>) is computationally much easier than using brute force to factorize <em>n</em>. The logic is based on the process called sieving. It technically works in a way that there is some set <em>F</em> (composed of first <em>k</em> integers with some reasonably high value of <em>k</em>) and an algorithm generates random integers <em>z</em> and compute factorization of <em>z</em> over factor base <em>F</em>. If <em>z</em> is smooth over <em>F</em>, values of exponents are saved as a vector. In the end, if there are at least |<em>F</em>| + 1 values generated, there is some linear combination that can create a combination for equation (1). The sieving is the most time-consuming part of the algorithm. The enhancement of the GNFS is that it uses slightly different factor base and slightly different inputs, but overall logic is the same.</p>

        <h3>Current situation of GNFS implementations</h3>
        <p>There is competition called RSA Factoring Challenge where anyone can see current milestones in attacks to RSA. The last one is from August 2018 when Samuel S. Gross successfully factorized the 762 bits large number. Number with 768 bits was factorized too in 2009 (it had been factorized previously probably because of prize that authors could win).</p>

        <p>Each of these challenges has been done on GPU chips. The interesting fact is that there is no suitable implementation of GNFS method on custom's hardware (FPGA). There was an attempt in the COPACOBANA project in 2007. Alas, it was far from being completed. New FPGA chips offer a great possibility of how to implement effective numerical methods and increase algorithm efficiency. </p>

        <p>Despite this successful attempt, there is still a lot to be done before factorization of 1024 bits RSA can be done. On the other hand, it is meaningful to say that 1024-RSA could be considered as endangered and should not be used for critical infrastructure. There are many replacements for RSA that does not represent a security risk including quantum resistant algorithms (i. g. Lattice-based cryptography). </p>

        <h2>Conclusions</h2>
        <p>Even though there is currently no known method of how to successfully attack RSA with 1024 bit key, it is probable that such a method can be created in the nearby future. There are two main threats to RSA security. First one is represented by quantum computers and another one by the fast implementation of GNFS factorization method. We can expect advancement in both in the nearby future. Quantum computers are the subject of intensive research by large companies such as Google, IBM, Microsoft. GNFS factorization method can now be implemented in a highly effective form on customer's devices (FPGA), which now has more significant potential than ever before. Due to these facts, it is highly recommended to update your systems from RSA to different cryptosystems, optimally quantum resistant ones, or at least increase modulus size to 4096 bites. </p>
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
