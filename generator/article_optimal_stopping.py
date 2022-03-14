# Optimal stopping: pure mathematics in real life
import datetime
import crinita as cr

lead = """The optimal stopping is one of the most important topics in pure (theoretical) mathematics with many impacts in real life. It gives you an optimal pattern of how to approach many situations. It includes hiring a new employee, renting a flat, selling a house, finding your next love or just searching for a parking place. Despite the horrendous name, the underpinning logic is relatively simple."""

content = r"""<p class="lead">The optimal stopping is one of the most important topics in pure (theoretical) mathematics with many impacts in real life. It gives you an optimal pattern of how to approach many situations. It includes hiring a new employee, renting a flat, selling a house, finding your next love or just searching for a parking place. Despite the horrendous name, the underpinning logic is relatively simple.</p>

<h2>Explore and exploit dilemma</h2>
<p>This dilemma is the core of our class of problems. Imagine the following problem: you want to rent a new flat. But, as things are, you have to decide right after the viewing if you're going to rent it or not. In other words, you cannot visit, say ten flats and decide which one is the best and then rent it - because someone else has already taken it. If you live in a bigger city, this usually is the case. So there is a big dilemma - how many flats should you view to have some comparison (exploring phase) and when should you start with renting (exploiting phase).</p> 

<h2>No-information games (aka Games of Incomplete Information)</h2>
<p>The example above represents precisely this class of problems. You do not have any objective measurement to define how good the flat is - you can only say if any flat is better than another one. If this is the case (no objective measurement of how good a thing is but only the comparison of two things is available), the explore/exploit dilemma is called a no-information game.</p>

<h3>Use-cases</h3>
<p>There are many slightly different examples:</p>
<ol>
    <li>Searching for the new employee: say that you have many candidates that are roughly the same. You want to find the optimal one. How many of them should you interview and reject before hiring someone?</li> 
    <li>Searching for the flat as described above.</li>
    <li>Searching for a high wage job (when should you stop searching and take the next offer, which is at least as good as the best one so far).</li>
    <li>Dating - yes, finding an optimal partner is in this set of problems.</li>
    <li>Searching the parking place - how long should you mess around, and when is the optimal time to choose a parking place.</li>
</ol>

<h3>The simplest case: as known as the 37 per cent rule</h3>
<p>This section describes the simplest case. Say that you want to rent the flat as described above - you reserve ten viewings. When is the optimal time to start considering renting one? It is right after you visit 37 per cent of envisioned viewings (in this case, after the fourth viewing). It means, after you assess the fourth flat, take the first one, which is at least as good as the best of these four. This strategy represents the optimal one. You have a 37 per cent chance of finding the best flat available - this seems to be a small number - but it is the best available strategy (there is solid mathematical proof for this claim). In this case, we are considering the optimal case - you do not lose anything if you reject, simultaneously the landlord cannot reject you. Also, you cannot revoke your decision once you reject the offer. These additional conditions are important as changing them changes the whole system.</p>

<h3>Special case: what if I can be rejected? Follow the 25 per cent rule.</h3>
<p>Slightly different is the situation when you can be rejected. Say on some date - you never know if your potential better half decide to reject you. Say, for example, that you expect the probability of rejection to be fifty per cent. It changes a lot. You have to stop exploring after you analyse the first 25 per cent of envisioned samples. In other words, if you want to date twelve people, you have to choose the first one after the third person that is at least as good as the best one of the first three people.</p> 

<h3>Another special case: what if I can propose twice?</h3>
<p>Slightly different is the situation if there is some probability of acceptance after your first rejection. It means you reject someone, but you can return and ask a second time (and there is some probability that your second offer will be accepted). Say that we have another special case: the probability of acceptance for the first time is 100 per cent and for the second time 50 per cent. This increases your likelihood of success. You should explore the first 61 per cent. Then you should take the first one who is better than the best so far - if you fail to find such a sample - go back and ask the best one from the whole set (if you are refused, then the second one etc.). This is the typical case when looking for the optimal parking place (as you can return and take place if it is still available, which it often is).</p>

<h2>Full information game (aka Complete information)</h2>
<p>This case differs from the previous one. We have another advantage - some measurement of how good something is (it means we can do more than compare two things) - and we also need to know the distribution of these results in population. For example, if we want to sell our house, we want to earn as much money as possible - so there is some measurement.</p>

<h3>Use-cases</h3>
<p>There are many slightly different examples:</p>
<ol>
    <li>Selling something: the most common example (you want to earn as much as you can).</li>
    <li>Hiring someone based on some score in the test they had to pass.</li>
    <li>Renting your house: in this case, you want to rent it to someone as soon as possible, as there is some cost for having an empty flat.</li>
</ol>
<h3>The simplest case: no penalty</h3>
<p>Suppose that we want to hire the best candidate based on his score on the test. And (importantly) we are in no rush in this process (it means there is no price if we reject any candidate). Importantly, we cannot change our decision later once we reject a candidate. Then, if you envision interviewing 30 candidates, follow the pattern:</p>
<ol>
<li>Hire the first candidate if his score is better than 96.666 per cent <span class="math">(1&nbsp;-&nbsp;1/30)</span><!-- LATEX $ \left( 1 - \frac{1}{30} \right) $ LATEX --></li>
<li>Hire the second candidate if his score is better than 96.665 per cent <span class="math">(1&nbsp;-&nbsp;1/29)</span><!-- LATEX $ \left( 1 - \frac{1}{29} \right) $ LATEX --></li>
<li>Generally, hire the <em class="equation">n</em>-th candidate (indexed from zero) if his score is better than <span class="math">1&nbsp;-&nbsp;1/(30&nbsp;-&nbsp;<em>n</em>)</span><!-- LATEX $ 1 - \frac{1}{30 - n} $ LATEX -->.</li>
</ol>
<p>As you can see, the general rule for <em class="equation">n</em>-th candidate (indexed from zero, so the first one is <span class="math"><em>n</em> = 0</span><!-- LATEX $ n=0 $ LATEX -->) out of <em class="equation">K</em> envisioned candidate (<em class="equation">K</em> is our number 30 in the example above) is: hire the <em class="equation">n</em>-th candidate if his score is better than <span class="math">1&nbsp;-&nbsp;1&nbsp;/&nbsp;(<em>K</em>&nbsp;-&nbsp;<em>n</em>)</span><!-- LATEX $ 1 - \frac{1}{K - n} $ LATEX -->.</p>

<h3>More complicated situation: there is a potential penalty</h3>
<p>This is the most common case - say that you want to rent your house. Objective (measured) criteria here are defined by the monthly rent your tenant is willing to pay. But there is also some penalty - the longer you search for a tenant, the more you pay for an empty house (for example, if you have a mortgage or utility bills).</p>
<p>This make things complicated - you have to subtract your potential loss from each candidate's offer before you choose to continue. After that, the rest is the same.</p>

<h3>Bomb Squad dilemma (aka burglar dilemma)</h3>
<p>Suppose that we have the following problem: a burglar knows that the probability that someone catches him is about 20 per cent. So how many houses can he pick to have a likelihood of being caught below 50 per cent?</p>
<p>As you can see in this problem, you know everything needed. The only thing is, how many places can a burglar visit? The solution is the maximal n in the equation:</p>
<p class="center math">(1 - 0.2)<sup><em>n</em></sup> > 0.5</p>
<!-- LATEX $$ \left(1 - 0.2\right)^n > 0.5 $$ LATEX -->
<p>In other words, if the probability that someone catches burglar is <em class="equation">p</em> (our 20 per cent) and the desired probability of being cached is <em class="equation">q</em> (our 50 per cent), the equation has the form:</p>
<p class="center math">(1 - <em>p</em>)<sup><em>n</em></sup> > <em>q</em></p>
<!-- LATEX $$ (1-p)^n > q $$ LATEX -->
<p>To solve this issue you can use a simple logarithm (or just try all options). The solution has the form:</p>
<p class="center math"><em>n</em> = floor(log(<em>q</em>) / log(1 - <em>p</em>)))</p>
<!-- LATEX $$ n = \left\lfloor \frac{\log(q)}{\log (1-p)} \right\rfloor $$ LATEX -->
<p>The floor function is the lowest part of the number (rounding down). For our case, it gives <span class="math"><em>n</em>&nbsp;=&nbsp;3</span><!-- LATEX $ n = 3 $ LATEX -->, which means that bulgar can rob three houses with a probability of 50 per cent of being caught.</p>
<h2>Summary</h2>
<p>This article discusses a fascinating problem called optimal stopping. It demonstrates the most common use-cases. The most common case is searching for a new employee (aka secretary problem or 37 per cent rule), then there is some generalisation presented (for example searching for a flat). Another class of problems is also discussed - the significant difference for this case is that we have a norm (we can measure how good something is in an absolute way, not just by comparison to another entity). Another interesting problem related to optimal stopping is a burglar dilemma (or Bomb Squad dilemma). It is about the number of secure attempts in some risky activity that can be performed.</p>
"""


ENTITY = cr.Article(
    title="Optimal stopping: pure mathematics in real life",  # noqa: E501
    url_alias='optimal-stopping-pure-mathematics-in-real-life',  # noqa: E501
    large_image_path="images/opt_stop_big.jpg",
    small_image_path="images/opt_stop_small.jpg",
    date=datetime.datetime(2021, 1, 17),
    tags=[cr.Tag('Mathematics', 'mathematics'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="The article discusses a very interesting problem called optimal stopping. It demonstrates the most common use-cases. The most common case is searching for a new employee."  # noqa: E501
)
