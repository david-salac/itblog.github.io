# Dimension order problem when storing of the big data
import datetime
import crinita as cr

lead = """One of the traditional arguments on why to avoid using ORM is the lack of performance. Although it is generally speaking correct, there are many ways how to write queries in your application. Some of them are better than others. There is almost always the way how to significantly increase the performance of application without avoiding the ORM approach."""

content = """One of the traditional arguments on why to avoid using ORM is the lack of performance. Although it is generally speaking correct, there are many ways how to write queries in your application. Some of them are better than others. There is almost always the way how to significantly increase the performance of application without avoiding the ORM approach.
<h2>The general problem of selecting data</h2>
<p>Many typical rules are worth to follow when querying a database. Typically you want to hit the database as less as you can. This means that it is meriting to write queries that fetch you all the data at once. So it is good to avoid many small queries. Another typical rule (that is not the opposite of the previous one) is to write queries that fetch you as much data as you need (and not any more). It means if you need data from one or two columns in the table, you should select precisely these columns and ignore others. All this goes hand by hand with the general rule, write the SQL queries in a way that affects as little tables as they can and is as simple as they can be. Following these rules can have a significant impact on application performance.</p>
<h2>Selecting data in Django land</h2>
<p>It is unquestionably true that the degree of freedom provided by default ORM tools is much lower than when you use raw queries. But that does not mean that it is not sufficient to almost all applications. Many useful tools in Django can help you with performance optimization. Following sections present some of them.</p>
<h3>Classes F and Q</h3>
<p>Classes F and Q are the tools of Django for optimizing selection conditions. You can import both classes from django.db.models module. The logic of Q is to abstract standard conditions. So you can effectively use conditions with all logical operators (negation, and, or). On the other hand, the F class allows you to write context-aware conditions.</p>
<p>Say that we have some imaginary table storing information about people (day of registration, day of birth, the colour of hair). If we want to select some non-blond people  born before 1990 who registered themselves before 30th birthday, the query can look like:</p>
<pre class="code"><code>from datetime import datetime, timedelta
from django.db.models import Q, F

selection = person.objects.filter(
    Q(registered__lte=timedelta(30) + F('dob')),  # Registered before 30
    ~Q(hair_color='blond')  # Non-blond
    & Q(dob__lte=datetime(1990))  # born before 1990
)</code></pre>
<p>This example is an academical one. But it shows how useful these classes are. It can safe you a lot of database hits, compared to the naive approach when you check these conditions in a for a loop.</p>
<h3>Selection of specific columns</h3>
<p>The typical situation when selecting data is that you do not need all of them. Typically the application logic requires just a few columns out of many. Say, for example, that we have our table storing information about people enriched with the following columns: name, weight, shoe size, favourite colour, etc. If the only purpose of your selection is to have names of people matching specific conditions, then other columns are useless. What is worse, they make the whole operation of fetching data slower. There is, fortunately, a method in Django that can solve this problem. It is called values_list, and it is a method directly in the QuerySet class. After applying this method, our optimized query can look like:</p>
<pre class="code"><code>only_names = selection.values_list('name', flat=True)</code></pre>
<p>In this case, the list of values is fetched (flatten version, so it has just one dimension). If you instead need the dictionary (for example if you select multiple columns), there is a function called value, that works in the same way but returns dictionary instead of a list.</p>
<h3>Application logic optimization</h3>
<p>The two approaches above can make almost every query faster. But they are not sufficient if the logic of the application is incorrect. Unfortunately, there is no simple manual on how to design application logic in the best way. It is always dependant on your particular application. Broadly speaking, it is always necessary to design tables and selection logic in a way that follows all the principles mentioned above (fetch in one query all that is needed with interacting to the minimal number of tables).</p> 
<p>There are, on the other hands, some commons mishaps. One of the popular is the repetitive selection of values from the database based on some conditions that are known in advance. In this case, the only correct approach is to fetch all the data in one query (instead of calling multiple queries).</p> 
<p>To demonstrate such an inefficient example, consider our table storing information about people. Say, for example, that we want to have lists of all males and females in the system. The naive approach can look like:</p>
<pre class="code"><code>males = [male.name for male in person.objects.filter(gender='male')]
females = [female.name for female in person.objects.filter(gender='female')]</code></pre>
<p>What is wrong with this example? You filter twice (and hit database twice) even though you know in advance what do you want to fetch. The optimized query (implementing the same) would look like:</p>
<pre class="code"><code>males = []
females = []
for person in person.objects.all():
    if person.gender == 'female':
        females.append(person.name)
    else:
        males.append(person.name)</code></pre>
<p>As you can see in this case, you hit the database just one when selecting all the rows (by the way, you should again reduce the column scope here as discussed above).</p>
<h3>Tests of database models Django</h3>
<p>Django provides many helpful tools for testing your application. One of the best tools is the class TransactionTestCase (in package django.test). It allows you to test models in a very efficient way. More than that, it contains a method called assertNumQueries. The method allows you to test a number of queries that are executed in your test case. This method is particularly helpful for optimizing application performance.</p>

<h2>Summary</h2>
<p>There are many ways how to optimize the performance of your application. One of them is to find the optimal way of accessing data in the database. Django ORM offers many vital tools that can help you to achieve this goal. Among the most important are classes F and Q that can allow you to apply smart filters for your queries. Another essential function is QuerySet.values(COLUMNS) that can allow you to select just the right number of columns in a query. There are also very helpful tools for testing of models in Django contained in class TransactionTestCase, among others function assertNumQueries that check the number of database hits in the test case. In the end, there are some general rules for how to make an application faster (not dependant on Django).</p>
"""

ENTITY = cr.Article(
    title="Optimizing database queries (not only) in Django ORM",
    url_alias='optimizing-database-queries-not-only-in-django-orm',
    large_image_path="images/database_big.jpg",
    small_image_path="images/database_small.jpg",
    date=datetime.datetime(2020, 11, 6),
    tags=[cr.Tag('Web application', 'web-application'),
          cr.Tag('Design', 'design'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Python', 'python')],
    content=content,
    lead=lead
)
