# More about some useful concepts in Python language
import datetime
import crinita as cr

lead = """The optimal stopping is one of the most important topics in pure (theoretic) mathematic if it comes to real-life applications. It gives you an optimal pattern of how to approach many situations. It includes things like hiring a new employee, renting a flat, selling a house, finding your next love or just searching for a parking place. Despite the horrendous name, the actual logic is simple."""

content = """
The optimal stopping is one of the most important topics in pure (theoretic) mathematic if it comes to real-life applications. It gives you an optimal pattern of how to approach many situations. It includes things like hiring a new employee, renting a flat, selling a house, finding your next love or just searching for a parking place. Despite the horrendous name, the actual logic is simple.

<h2>Explore & exploit dilemma</h2>
<p>This dilemma is the core of our class of problems. Imagine the following problem: you want to rent a new flat. But, as things are, you have to decide right after the viewing if you want to rent it or not. In other words, you cannot visit say ten flats and decide which one is the best and then rent it - because someone else has already taken it. This gives you a big dilemma - how many flats should you view to have some comparison (exploring phase) and when should you start with renting (exploiting phase).</p> 

<h2>No-information games (aka Games of Incomplete Information)</h2>
<p>The example above represents exactly this class of problems. You do not have any objective measurement to define how good the flat is - you can just say if the flat is better than another one. If this is the case (no objective measurement of how good a thing is but only the comparison of two things is available) the explore/exploit dilemma is called a no-information game.</p>

<h3>Use-cases</h3>
<p>There are many slightly different examples:</p>
<ol>
<li>Searching for the new employee: say that you have many candidates that are roughly the same. You want to find the optimal one. How many of them should you just interview and reject?</li> 
<li>Searching for the flat as described above.</li>
<li>Searching for a high wage job (when should you stop searching and take the next offer which is at least as good as the best one so far).</li>
<li>Dating - yes even finding an optimal partner is in this set of problems.</li>
<li>Searching the parking place - for how long should you just mess around and when is the optimal time to choose some parking place.</li>
</ol>
<h3>The simplest case: 37 per cent rule</h3>
<p>This is the simplest case. Say that you want to rent the flat as described above - you reserve 10 viewings. When is the optimal time to start considering renting one? It is exactly after you visit 37 per cent of envisioned viewings (in this case after the fourth viewing). It means, after you visit the fourth flat, take the first one which is at least as good as the best of these four. This strategy represents the optimal one. You have a 37 per cent chance that you find the best flat available - this seems to be a small number - but it is the best strategy available. In this case, we are considering the optimal case - you do not lose anything if you reject and you cannot be rejected by a landlord. Also, once you reject the offer - you cannot revoke your decision.</p>

<h3>Special case: what if I can be rejected?</h3>
<p>Slightly different is the situation when you can be rejected. Say on some date - you never know if your potential better half decide to reject you. Say for example, that you expect the probability of rejection to be fifty per cent. It changes a lot, you have to stop exploring after you analyse the first 25 per cent of samples.</p> 
<h3>Another special case: what if I can propose twice?</h3>
<p>Slightly different is the situation if there is some probability of acceptance after your first rejection. It means, you reject someone, but you can come back again and ask a second time (and there is some probability that your second offer will be accepted). Say that we have another special case: the probability of acceptance for the first time is 100&nbsp;% and for the second time 50 per cent. This increases your probability of success. You should explore the first 61 per cent, then you should take the first one who is better than the best so far - if you fail to find such a sample - go back and ask the best one from the whole set (if you are refused then the second one etc.). This is the typical case when you are looking for the optimal parking place.</p>

<h2>Full information game (aka Complete information)</h2>
<p>This case differs from the previous one. We have another advantage - some measurement of how good something is (it means we can do more than compare two things) - and we also need to know the distribution of these results in population. For example, if we want to sell our house, we want to earn as much money as possible - so there is some measurement.</p>
<h3>Use-cases</h3>
<p>There are many slightly different examples:</p>
<ol>
<li>Selling something: the most common example (you want to earn as much as you can).</li>
<li>Hiring someone based on some score in the test they had to pass.</li>
<li>Renting your house: in this case, you want to rent it to some person as soon as possible, as there is some cost for having an empty flat.</li>
</ol>
<h3>The simplest case: no penalty</h3>
<p>Suppose that we want to hire the best candidate based on his score in some test. And (importantly) we are in no rush in this process (it means, there is no price if we reject any candidate). Then, if you envision interviewing 30 candidates, follow the pattern:</p>
<ol>
<li>Hire the first candidate if his score is better than 96.666 per cent (1&nbsp;-&nbsp;1/30)</li>
<li>Hire the second candidate if his score is better than 96.665 per cent (1&nbsp;-&nbsp;1/29)</li>
<li>Generally, hire the <em>n</em>-th candidate (indexed from zero) if his score is better than 1&nbsp;-&nbsp;1/(30&nbsp;-&nbsp;<em>n</em>).</li>
</ol>
<p>As you can see, the general rule for <em>n</em>-th candidate (indexed from zero, so the first one is <em>n</em> = 0) out of <em>K</em> envisioned candidate (<em>K</em> is our number 30 in the example above) is: hire the <em>n</em>-th candidate if his score is better than 1&nbsp;-&nbsp;1&nbsp;/&nbsp;(<em>K</em>&nbsp;-&nbsp;<em>n</em>).</p>

<h3>More complicated situation: there is some penalty</h3>
<p>This is the most common case - say that you want to rent your house. Objective (measured) criteria here is defined by the monthly rent that your tenant is willing to pay. But there is also some penalty - the longer you are searching for a tenant - the more you pay for an empty house (for example, if you have a mortgage, or for utility bills).</p>
<p>This make things complicated - you have to subtract your potential lost from each candidate before you choose to continue. The rest is the same.</p>

<h3>Bomb Squad dilemma (aka burglar dilemma)</h3>
<p>Suppose that we have the following problem: a burglar knows that the probability that someone catches him is about 20 per cent. How many houses can he pick to have a probability of being caught below 50 per cent?</p>
<p>As you can see in this problem, you know all that is needed. The only thing is how many places can a burglar visit? The solution is the maximal <em>n</em> in the equation:</p>
<p>(1 - 0.2)<sup><em>n</em></sup> < 0.5</p>
<p>In other words, if the probability that someone catches burglar is <em>p</em> (our 20 per cent) and the desired probability of not being cached is <em>q</em> (our 50 per cent), the equation has the form:</p>
<p>(1 - <em>p</em>)<sup><em>n</em></sup> < <em>q</em></p>
<p>To solve this issue you can use a simple logarithm (or just try all options). The solution has the form:</p>
<p><em>n</em> = floor(log(<em>q</em> / (1 - <em>p</em>)))</p>
<p>Where the floor function is the lowest whole part of the number (rounding down).</p>
<h2>Summary</h2>
<p>This article discusses a very interesting problem called optimal stopping. It demonstrates the most common use-cases. The most common case is searching for a new employee (aka secretary problem or 37 per cent rule), then there is some generalisation presented (for example searching for a flat). Another class of problems is also discussed - the major difference for this case is that we have a norm (we can measure how good something is in an absolute way, not just by comparison to another entity). Another interesting problem related to optimal stopping is known as a burglar dilemma (or Bomb Squad dilemma). It is about the number of secure attempts which can be performed.</p>
"""

ENTITY = cr.Article(
    title="Optimal stopping: a pure mathematics in real life",
    url_alias='optimal-stopping-a-pure-mathematics-in-real-life',
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
    description="The article discusses a very interesting problem called optimal stopping. It demonstrates the most common use-cases. The most common case is searching for a new employee."
    # noqa: E501
)
