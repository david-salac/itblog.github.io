# Organizing work in software engineering project (Agile, SCRUM and Waterfall)
import datetime
import crinita as cr

lead = """Frameworks for organizing work - you cannot avoid it whenever you decide to manage a project in IT. What is the most effective way for organizing the work of your team? Probably none of the issues related to project management is covered by so many posts, videos on YouTube, articles in scientific journals. This article is about one concrete human perspective on project organization. It can help you decide how to run your project, consider available frameworks (particularly Waterfall, Agile and SCRUM frameworks), and present management tools."""

content = """<p class="lead">Frameworks for organizing work - you cannot avoid it whenever you decide to manage a project in IT. What is the most effective way for organizing the work of your team? Probably none of the issues related to project management is covered by so many posts, videos on YouTube, articles in scientific journals. This article is about one concrete human perspective on project organization. It can help you decide how to run your project, consider available frameworks (particularly Waterfall, Agile and SCRUM frameworks), and present management tools.</p>

<h2>Waterfall</h2>
<p>A waterfall is a straightforward approach when you follow the path of your project step by step. Before starting the next step, the previous one has to be finished. Usually, there is no need to split the project into many small tasks. Instead, there are a few big ones (typically, each assigned to one person).  Each project phase is characterized by a small number of bigger tasks - before entering the next phase, finishing each of these tasks is required - often, people need to wait for others to complete their tasks which cause problems.</p>
<figure>
    <img alt="Figure 1: Overall logic of the waterfall approach." src="images/prj_waterfall.png">
    <figcaption>Figure 1: Overall logic of the waterfall approach.</figcaption>
</figure>
<p>It is fair to say that there are many pros related to the waterfall approach. The most important one is continuity. Your team can stay focused on one task for a long time - there are (in the optimal world) no interruptions. Unfortunately, this huge advantage is simultaneously the most apparent drawback. It is because people tend to lose motivation when working on one particular task for a long time. The project manager can also quickly lose track of the task's difficulty.</p> 
<p>The waterfall is helpful at the beginning of your project - up until that phase when you have something tangible. It also represents arguably the simplest way to quickly achieve something concrete - which is particularly helpful at the start (as you need to have feedback from real customers as soon as possible). Plus, many projects are not suitable for Agile-like frameworks - most notoriously projects in research and development (where it often takes many months of monotonous work to have some results). Another example can be a small project - it can easily be a waste of time to deploy anything agile if you can finish the whole project in two weeks. But the general rule is, try to avoid waterfall whenever you easily can as its cons overweight the pros.</p>

<h2>Agile frameworks</h2>
<p>The agile frameworks differ substantially from the waterfall one as they prefer having many tasks (if possible with minimal overlapping) and mixing phases of a project. Also, in theory, a team member needs to have competencies to work on every available task. So it practically means that each team member is replaceable. Also, the time scale differs - agile prefers working with fixed sprints (in size of about two weeks) instead of large waterfall phases.</p>
<figure>
    <img alt="Figure 2: Overall logic of the agile approach." src="images/prj_agile.png">
    <figcaption>Figure 2: Overall logic of the agile approach.</figcaption>
</figure>
 
<p>A typical sprint usually has around two weeks. Before each sprint, there has to be a sprint planning meeting - the project owner (or manager) has to describe each task in the sprint, so everyone understands them. Before this meeting, the product owner must prepare a tasks board. Then, after each sprint, there usually is a bigger meeting dedicated to reflection - the subject of discussion is what went good or bad. Each of these meetings usually takes many hours (like three or so) - so consider this in your business plan. </p> 
<p>As mentioned, tasks need to be distributed among each team member equally. None of the team members should have dedicated access to one type of task. This approach has two advantages: a) none of your team members become a T-shaped person if it comes to skills (knowing a lot in one part and nothing in others), b) if any of your teammates choose to leave, it does not destroy the whole project. It is legitimate to have multiple teams in one project (like front-end, back-end, data science). Or each of these teams can then have its separate agile sprint - it is then the project manager role to organize cooperation between groups.</p>
<p>Planning and distributing tasks often require a whole person - do not believe that anybody can manage everything in an organization (the day has just 24 hours). This note is important because it has a massive impact on the business plan (and budget). Also, it is optimal to deploy something agile-based (mostly SCRUM) as soon as possible (as discussed above, it is good to have tangible outputs already).</p>

<h2>SCRUM framework</h2>
<p>The SCRUM framework represents the concrete implementation of agile. It provides terminology for all critical parts of the process (like Sprint, Backlog, Board, Epic and so on). In addition, a new concept of stand-up meetings is introduced to increase communication between team members. They should take place daily (or in a similarly short period). It is a short meeting where people discuss what they did a day before (in terms of what task) and what they want to do today. Team members can also briefly discuss any difficulties or their plans on stand-up.</p> 
<p>An essential idea in SCRUM is called a backlog. It is a list of task from which (typically) the project manager (or product owner) construct the next sprint. The crucial thing is that everyone can add tasks into the backlog - developers typically add bug-fixing tasks, project managers add tasks related to new features. Another thing to notice is Story splitting to epics - which means that you should break a time-consuming task (aka Story) into multiple subtasks, which are part of an entity called Epic. It helps you monitor performance and progress.</p>
<p>The board's composition is also crucial for success (the board is that part where the developer chooses a new task). It typically has four columns:</p>
<ol>
    <li>To do tasks: waiting to be selected as a new task by a developer.</li>
    <li>In progress: already selected by a developer who should be working on them.</li>
    <li>Quality Assurance: this column is not standard but is highly desirable. After the developer finishes developing, he moves the task here to review.</li> 
    <li>Done: after the review (and the result approved), the task can be closed as finished.</li>
</ol>

<p>There can also be other improvements to your board - but this is the most simple working concept. Practically, you will invariably implement a modification of SCRUM in your organization - as a pure SCRUM is too restrictive for practical usage. It might be more than helpful to improvise slightly in project management and see the outcomes.</p> 

<h2>Available tools</h2>
<p>Many helpful tools are available - some for free, some paid. All these make the project management process significantly easier. This section presents the most popular tools currently - it though not difficult to find many others (and it might be beneficial to do so).</p>

<h3>JIRA</h3>
<p>The most popular one is called JIRA (developed by Atlassian). However, it is good to mention that even though JIRA represents a gold standard in software development, it is also not user-friendly and contains many technical weaknesses (for example, memory requirements are massive), and it is relatively expensive. Therefore it is worth considering alternatives for project management.</p>

<figure>
    <img src="images/jira_board.gif" alt="Figure 3: A concrete example of JIRA board">
    <figcaption>Figure 3: A concrete example of JIRA board</figcaption>
</figure>

<p>Generally, be sure that you do not duplicate your work by describing your tasks in some presentation. You will need to do your work twice (once on your slides and then in JIRA). Just copying tasks for one sprint can take up to half of your day, so be practical. </p>

<h3>GitHub</h3>
<p>A new, freely available option for a smaller project is available in GitHub. Technically, it is a sufficient tool for project management - however, interconnected with GitHub. If you use GitHub as a git management tool, this option is worth considering.</p>

<figure>
    <img src="images/prj_github.gif" alt="Figure 4: A concrete example of GitHub project board">
    <figcaption>Figure 4: A concrete example of GitHub project board</figcaption>
</figure>
<p>GitHub developers did significant updates in project management in late 2021 - now there is support for backlogs, link to GitHub Issues, and many other exciting features that makes this feature suitable even for large projects.</p>

<h3>Zenhub</h3>
<p>Zenhub represents an extension of GitHub. Compared to native GitHub projects, it allows many additional features - like adding epics, monitoring performance, and others. However, this solution is a bit clumsy compared to JIRA - the way Zenhub deals with epics is ineffective. Also, there is no clear split between sprints - the whole task set is always on board - this makes the last column very big (and the entire board does not look clean). Rather than using Zenhub, it is worth considering other alternatives.</p>

<h2>Summary</h2>
<p>There are many ways for managing a project. For example, most frameworks use agile logic, splitting each project into smaller tasks and splitting the time frame into sprints. An opposite is a waterfall approach, where things are done step by step using bigger tasks. SCRUM is currently the most popular agile framework. It has its rituals and naming convention. Many tools can help deal with project management. Arguably the most popular is paid service called JIRA. However, it has many flaws. That is why many other tools have recently emerged - like Zenhub and GitHub projects. It is worth doing some testing before choosing the right project management tool for your project.</p>

"""

ENTITY = cr.Article(
    title="Organizing work in software engineering projects (Agile, SCRUM and Waterfall)",
    url_alias='organizing-work-in-software-engineering-projects-agile-scrum-and-waterfall',
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
