# Organizing work in software engineering project (Agile, SCRUM and Waterfall)
import datetime
import crinita as cr

lead = """You cannot avoid it whenever you decide to manage some project in IT. What is the most effective way for organizing the work of your team? Probably none of the issues in project management is covered by so many posts, videos on YouTube, articles in scientific journals as this one. This article is about one concrete human perspective on project organization. It can help you to decide how to run your project."""

content = """You cannot avoid it whenever you decide to manage some project in IT. What is the most effective way for organizing the work of your team? Probably none of the issues in project management is covered by so many posts, videos on YouTube, articles in scientific journals as this one. This article is about one concrete human perspective on project organization. It can help you to decide how to run your project. This might help you to decide how to organise work in your project by presenting available frameworks (particularly Waterfall, Agile and SCRUM frameworks).

<h2>Waterfall</h2>
<p>A waterfall is an approach when you follow the path of your project step by step. Before you start the next step, the previous one has to be finished. Technically you do not have many small tasks but rather few big tasks (typically for one person). Each phase/cycle of a project is determined by the outcomes of the previous step.</p>
<p>Most people feel awkward even when they have to say this word - that is not my case. There are many pros related to the waterfall approach - but the solely most important one is continuity. Your team can be fully focused on one task for a long time - there are (in the optimal world) no interruptions. Unfortunately, the most obvious pros of this approach are its most glaring drawback as well. People lose motivation if they have to work on one particular task for a long time. The project manager also loses the idea of how difficult any task is.</p> 
<p>The waterfall is particularly good at the beginning of your project. Until that phase when you have something tangible. It represents arguably the simplest way how to quickly achieve something concrete (and allow to use of other project management techniques). Also, many projects are not suitable for Agile-like frameworks - most notoriously projects in research and development (where it often takes many months of monotonous work to have some results). But the general rule is, try to avoid Waterfall whenever you easily can as its cons overweight pros.</p>

<h2>Agile frameworks</h2>
<p>The agile framework differs substantially from the Waterfall one. It prefers to have multiple tasks (if possible with minimal overlapping). So each team member is kind of replaceable (as everyone can work on one task or another). Also, the time scale differs - it prefers to have fixed iterations (in size of about 2 weeks).</p> 
<p>It is optimal to deploy something agile-based (mostly SCRUM) as soon as reasonably possible (as discussed above, it is good to have some tangible outputs already). The optimal sprint should take around two weeks. After this time, the big meeting should be called. At this meeting, you need to briefly discuss the previous sprint and carefully plan the next sprint (the meeting usually takes about 5 hours). You also need to have some basic tasks definitions already available (on some board).</p> 
<p>It is also good to mention that tasks should be distributed among each member of your team equally. None of the team members should have dedicated access to one type of task. This approach has two advantages: a) none of your team members become a T-shaped person if it comes to sills (knowing a lot in part and nothing in others), b) if any of your teammates choose to leave, it does not destroy the whole project. </p>
<p>Planning and distributing tasks often require the whole person - do not believe that you can manage everything in your company (the day has just 24 hours). It is legitimate to have multiple teams in one project (like front-end, back-end, data science). Each of these teams can then have its separate agile sprint - it is then the project manager role to organise cooperation between teams.</p>

<h2>SCRUM framework</h2>
<p>The scrum framework represents the concrete implementation of agile. It provides terminology for all key parts of the process (like Sprint, Backlog, Board, and so on). There is also a new concept that enforces communication between team members - stand-up meeting. It should be organised daily - basically, it's a quite short meeting where people discuss what they did (in terms of what task) a day before and what they want to do today.</p> 
<p>An important concept in SCRUM is called a backlog. It is a list of task from which (typically) the project manager (or product owner) construct the next sprint. Everyone can add some task (developers typically add bug-fixing tasks, project manager developing tasks). Another thing to notice is Story Splitting - which means that you should split a time-consuming task (aka Story) into multiple subtasks that can be done separately - it helps you monitor performance.</p>
<p>The composition of the board is also crucial for success (the board is that part where the developer chooses a new task). It typically has four columns:</p>
<ol>
<li>To do tasks: waiting to be selected as a new task by a developer.</li>
<li>In progress: already selected by a developer who should be working on them.</li>
<li>Quality Assurance: this column is not common, but is highly desirable. After the developer finishes his developing part, it should be moved here to review the process.</li> 
<li>Done: after the review is finished (and the result approved), the task can be closed as finished.</li>
</ol>
<p>There can also be some other improvements to your board - but this is the most simple working concept.</p>
<p>Practically, you will always have some own implementation of SCRUM in your organisation - as pure SCRUM definition is too restrictive for practical usage. It might be more than helpful to improvise slightly in project management and see the outcomes.</p> 

<h2>Available tools</h2>
<p>It is probably not a big surprise that there are already available tools that can make your project management work much simpler. The most popular one is called JIRA (developed by Atlassian). It is good to mention that even though JIRA represents a gold standard in software development, it is also a not very user-friendly piece of software. Therefore it is worth considering alternatives for project management (the author will not give you any hints as there are too many things available).</p>
<p>Generally, be sure that you do not duplicate your work - for example by describing your tasks in some presentation. You will need to do your work twice (once on your slides, and then in JIRA). Just copying task for one sprint can take up to half of your day - so try to be effective. </p>
<p>By the way, for managing some very small (open-source) project, there is also one simple free alternative. It is using GitHub project management tools. It is available as a tab when you open your project detail (you must be the admin of that particular project to have this feature available).</p>
"""

ENTITY = cr.Article(
    title="Organizing work in software engineering project (Agile, SCRUM and Waterfall)",
    url_alias='organizing-work-in-software-engineering-project-agile-scrum-and-waterfall',
    large_image_path="images/team_big.jpg",
    small_image_path="images/team_small.jpg",
    date=datetime.datetime(2020, 6, 12),
    tags=[cr.Tag('Project Management', 'project-management'),
          cr.Tag('Design', 'design'),
          cr.Tag('Essentials', 'essentials'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Administration', 'administration')],
    content=content,
    lead=lead,
    description="This might help you to decide how to organise work in your project by presenting available frameworks (particularly Waterfall, Agile and SCRUM frameworks)."  # noqa: E501
)
