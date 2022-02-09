# Optimizing database queries (not only) in Django ORM
import datetime
import crinita as cr

lead = """One of the traditional arguments on avoiding using ORM is the lack of performance. Although it is generally speaking correct, there are many ways to write queries in your application. Some of them are better (faster and more efficient) than others. There is almost always a way to significantly increase the performance of an application without avoiding the ORM approach. We anticipate some preliminary knowledge of Django and SQL here (so make sure you understand basic concepts before continuing)."""

content = """<p class="lead">One of the traditional arguments on avoiding using ORM is the lack of performance. Although it is generally speaking correct, there are many ways to write queries in your application. Some of them are better (faster and more efficient) than others. There is almost always a way to significantly increase the performance of an application without avoiding the ORM approach. We anticipate some preliminary knowledge of Django and SQL here (so make sure you understand basic concepts before continuing).</p>

<h2>The general problem of selecting data</h2>
<p>Many typical rules are worth following when querying a database. Typically, you want to hit the database as little as possible, which means it is meaningful to write queries that fetch you all the data at once. So it is good to avoid a series of small queries. Another typical rule (that is not the opposite of the previous one) is to write queries that fetch you as much data as you need, but not any more (fetch just enough). It means if you need data from one or two columns in the table, you should select precisely these columns and ignore others. All this goes hand in hand with the general rule: write the SQL queries in a way that affects as few tables as they can and is as simple as possible. Following these rules can have a significant impact on application performance.</p>

<h2>Selecting data in Django land</h2>
<p>It is unquestionably true that the degree of freedom provided by default ORM tools is much lower than when you use raw queries. But that does not mean that it is not sufficient for almost all applications. Many valuable tools in Django can help you with performance optimization. The following sections present some of them.</p>
<h3>Classes F and Q</h3>
<p>Classes <code>F</code> and <code>Q</code> are the tools of Django for optimizing selection conditions. You can import both classes from <code>django.db.models</code> module. The logic of <code>Q</code> is to abstract standard conditions. So you can effectively use conditions with all logical operators (negation, and, or). On the other hand, the <code>F</code> class allows you to write context-aware conditions.</p>
<p>Say that we have some imaginary table storing information about people (day of registration, day of birth, hair colour). If we want to select some non-blond people born before 1990 who registered themselves before their 30th birthday, the query can look like this:</p>
<pre class="code"><code>from datetime import datetime, timedelta
from django.db.models import Q, F

selection = person.objects.filter(
    # Registered when younger than 30
    Q(registered__lte=timedelta(30) + F('dob')),  
    ~Q(hair_color='blond')  # Non-blond
    & Q(dob__lte=datetime(1990))  # born before 1990
)</code></pre>
<p>This example is an academic one. But it shows how valuable these classes are. It can save you a lot of database hits compared to the naive approach when you check these conditions in the for-loop.</p>

<h3>Selection of specific columns</h3>
<p>The typical situation when selecting data is that you do not need all of them. Typically the application logic requires just a few columns out of many. Say, for example, that we have our table storing information about people enriched with the following columns: name, weight, shoe size, favourite colour, etc. If the only purpose of your selection is to have names of people matching specific conditions, then other columns are useless. What is worse, they make the whole operation of fetching data slower. There is, fortunately, a method in Django that can solve this problem. It is called values_list, and it is a method directly in the QuerySet class. After applying this method, our optimized query can look like this:</p>
<pre class="code"><code>only_names = selection.values_list('name', flat=True)</code></pre>
<p>In this case, the list of values is fetched (flatten version, so it has just one dimension). If you instead need the dictionary (for example, if you select multiple columns), a function called value works similarly but returns a dictionary instead of a list.</p>

<h3>Application logic optimization</h3>
<p>The two approaches above can make almost every query faster. But they are not sufficient if the logic of the application is incorrect. Unfortunately, there is no simple manual on designing application logic in the best way. It is always dependant on your particular application. It is always necessary to design tables and selection logic to follow all the principles mentioned above (fetch all that is needed with interacting to the minimal number of tables) in one query.</p> 
<p>There are, on the other hand, some common mishaps. One of the popular is the repetitive selection of values from the database based on conditions known in advance. In this case, the only correct approach is to fetch all the data in one query (instead of calling multiple queries).</p> 
<p>To demonstrate such an inefficient example, consider our table storing information about people. Say, for example, that we want to have lists of all males and females in the system. The naive approach can look like this:</p>

<pre class="code"><code>males = [male.name for male in 
    person.objects.filter(gender='male')]
females = [female.name for female in 
    person.objects.filter(gender='female')]</code></pre>
<p>What is wrong with this example? You filter twice (and hit database twice) even though you know what you want to fetch in advance. The optimized query (implementing the same) would look like:</p>
<pre class="code"><code>males = []
females = []
for person in person.objects.all():
    if person.gender == 'female':
        females.append(person.name)
    else:
        males.append(person.name)</code></pre>
<p>As you can see in this case, you hit the database just one when selecting all the rows (by the way, you should again reduce the column scope here, as discussed above).</p>

<h3>Tests of database models Django</h3>
<p>Django provides many helpful tools for testing your application. One of the best tools is the class <code>TransactionTestCase</code> (in package <code>django.test</code>). It allows you to test models in a very efficient way. More than that, it contains a method called <code>assertNumQueries</code>. The method allows you to test a number of queries executed in your test case. This method is particularly helpful for optimizing application performance.</p>

<h3>Using fields specific to DBMS</h3>
<p>Another way to optimize performance is to use specific fields dedicated to the particular DBMS provider, most commonly PostgreSQL. For example, it is possible to use fields such as arrays of a specific type or nested JSON structures. These fields are optimized in a way that you can query them efficiently. Also, many proprietary providers provide support for Django ORM - it is always helpful to study specific options and optimize as much as possible when designing tables.</p>

<h2>Other ORMs</h2>
<p>Many other ORM tools are available, including ORM tools in different languages. But described principles are more or less generally true. The most popular ORM in Python (besides Django ORM) is SQLAlchemy. This ORM is much more low-lever than the Django version. It allows querying the database almost as efficiently as the raw SQL. That is a considerable advantage when performance matters. But it is simultaneously a significant disadvantage to safety, and it is not user-friendly ORM from the programmer point of view.</p>

<h2>Summary</h2>
<p>There are many ways how to optimize the performance of your application. One of them is to find the optimal way of accessing data in the database. Django ORM offers many vital tools to help you achieve this goal. Some of the most important are classes F and Q that can allow you to apply intelligent filters for your queries. Another essential function is QuerySet.values(COLUMNS) that can allow you to select just the correct number of columns in a query. There are also beneficial tools for testing models in Django contained in class TransactionTestCase, among others function assertNumQueries that check the number of database hits in the test case. In the end, there are some general rules for how to make an application faster (not dependant on Django).</p>
"""

ENTITY = cr.Article(
    title="Optimizing database queries (not only) in Django ORM",
    url_alias='optimizing-database-queries-not-only-in-django-orm',
    large_image_path="images/database_big.jpg",
    small_image_path="images/database_small.jpg",
    date=datetime.datetime(2020, 12, 6),
    tags=[cr.Tag('Web application', 'web-application'),
          cr.Tag('Design', 'design'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Python', 'python')],
    content=content,
    lead=lead,
    description="Technical analysis presenting ways for effective querying of the database using Django ORM like reducing the number of selected columns or using F or Q class."  # noqa: E501
)
