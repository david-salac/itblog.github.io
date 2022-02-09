# Virtual environments in Python language
import datetime
import crinita as cr

lead = """Virtual environments are a beneficial concept that makes your coding much more accessible. There are many tools in Python for creating and managing virtual environments. This article analyses the native virtual environment created using the venv command on Linux and Windows. Another simplified and more user-friendly approach is to use Anaconda software (using command conda) or using IDE like PyCharm directly."""

content = """<p class="lead">Virtual environments are a beneficial concept that makes your coding much more accessible. There are many tools in Python for creating and managing virtual environments. This article analyses the native virtual environment created using the venv command on Linux and Windows. Another simplified and more user-friendly approach is to use Anaconda software (using command conda) or using IDE like PyCharm directly.</p>

<h2>What are virtual environments?</h2>
<p>One of the crucial issue for Python developers is called virtual environment. Basically, it is helpful when you need to install (in order to run or use) Python's packages without affecting the system packages. Typically for testing or developing some applications. Managing of the virtual environment is typically one of the common features of the IDE (e.g. JetBrains <strong>PyCharm</strong> deal with this issue in a very efficient way). However, it is helpful to know how to manage it directly from the command line.</p>

<h2>What is the rationale for using virtual environments?</h2>
<p>One of the crucial issues every Python developer needs to know about is the management of virtual environments. A virtual environment is helpful when you need to install (to run or use) Python's packages without affecting the system package repository, typically when testing or developing some applications. As every Python engineer knows, almost every package has its sub-dependencies. </p>
<p>These dependencies are other Python libraries (programs) required to run the desired application or library. Generally, the application's dependencies (or requirements) are enumerated in the requirements.txt file in the codebase. It is also essential to know the default source for external packages. They are downloaded from the PyPi repository (available on pypi.org). However, you can also specify your own private Python package repositories - which might be helpful when creating proprietary software.</p>
<p>It is helpful to avoid affecting system packages because many other applications can depend on them (in a specific version). So if any application requires an update or downgrade of the system's package version - which is a very common operation - it can (and often does) have severe effects. Another similar reason is to separate dependencies between different Python non-system applications and libraries. </p>
<p>If one application needs a different set of dependencies than another application, it does not make sense to provide a bunch of dependencies to all of them. Furthermore, virtual environments can help if you need to find the minimal set of requirements for a particular application - a particularly helpful operation when cleaning codebase before releasing. Finally, sometimes dependencies are built based on values in environmental variables - in these situations, using a virtual environment is the only way to proceed.</p>
<p>Managing the virtual environment is typically one of the standard features of the IDE (e.g. JetBrains PyCharm deal with this issue in a very efficient way). However, it is helpful to know how to manage environments directly from the command line.</p>

<h2>Native virtual environment (command venv)</h2>
<p>Using the venv command is the simplest (and oldest) approach for managing virtual environments. It is also the first choice if you need to install something quickly or in production. However, it has its cons as well. For example, many (even frequently used) packages require system-level dependencies. A typical example is a famous package called pyplot that provides helpful tools for plotting various types of graphs. In these cases, the situation is quite problematic, as you need to install the system package separately on a global level. That contradicts the rationale for using virtual environments, as the new system-level dependency is shared with all applications. Unfortunately, there is not too much that can be done.</p>

<h3>How to install venv on Linux</h3>
<p>It depends on the machine you are using. For the Ubuntu, use just:</p>
<pre class="code"><code>sudo apt install python3-virtualenv</code></pre>

<h3>How to use native venv command on Linux</h3>
<p>To use a virtual environment on Linux, use the following manual:</p>
<ol>
<li><p>The virtual environment has to be created. Use the command:</p>
<pre class="code"><code>python3 -m venv PATH</code></pre>
<p>Where the <strontg>PATH</strontg> argument is typically equal to '.' (current folder).</p>
</li>
<li><p>After the creation, you have to activate it. Go to the folder where the virtual environment is located and write:</p>
<pre class="code"><code>. bin/activate</code></pre>
</li>
<li>
<p>If the terminal is now displaying something like:</p>
<pre class="code"><code>(testvenv) USER@MACHINE:~/PATH_TO_ENV$ </code></pre>
<p>You can start to use your virtual environment.</p>

<p>Your typical first command in the virtual environment would be to install some requirements.</p> <p>Use, for example:</p>
<pre class="code"><code>pip3 install -r requirements.txt</code></pre>
<p>For installing requirements from the requirements.txt file (standard approach). Or you can simply install system packages using the pip command directly:</p>
<pre class="code"><code>pip3 install NAME_OF_PACKAGE
# Or alternatively:
pip install -r requirements.txt
</code></pre>
</li>
<li>
<p>If you want to deactivate the virtual environment, use the commend:</p>
<pre class="code"><code>deactivate</code></pre>
<p>You should see the standard terminal window now.</p>
</li>
</ol>

<p>It is helpful to know that the virtual environment has the same name as the folder where it was created. You can also use the activated environment in any other folder. The best approach is to use a dedicated sub-folder of the Python project for the virtual environment. When using some version control system, be sure that you ignore the folder with the virtual environment (in the case of Git, add its content to the .gitignore file) - as it typically contains a lot of useless files that have nothing to do with your application (which can be platform-specific and not working on another computer as expected).</p>

<h3>How to work on Windows</h3>
<p>If your system is Windows, use the following logic and run the following commands in Windows Power Shell:</p>
<ol>
<li><strong>Run Windows Power Shell as Administrator (right-click on it and run it with required privileges)</strong></li>
<li><code>pip install virtualenv</code></li>
<li><code>pip install virtualenvwrapper-win</code></li>
<li><code>mkvirtualenv 'PATH_TO_VENV'</code></li>
<li><code>cd PATH_TO_VENV</code></li>
<li><code>Set-ExecutionPolicy AllSigned</code> <em>(press Y and Enter)</em></li>
<li><code>Set-ExecutionPolicy RemoteSigned</code> <em>(press Y and Enter)</em></li>
<li><code>.\\Scripts\\activate</code> <em>(this activate your virtual environment)</em></li>
<li><strong>use the virtual environment as needed now...</strong></li>
<li><code>deactivate</code> <em>(to exit)</em></li>
</ol>

<p>Using Python interpreter is otherwise the same for Windows for Linux (be aware of using different slashes). So once you are in a Virtual Environment, you can proceed as when you were on your deployment machine.</p>

<h3>Ubuntu on Windows (WSL)</h3>
<p>Another approach to deal with virtual environments on Windows is to use WSL - technically a simulation of Ubuntu Linux console on Windows. It is freely available on Windows starting in version 10. This approach is beneficial, as Python is a more native tool for Linux than Windows. Many IDEs are also required to have WSL installed. Managing virtual environments in WSL is identical to managing environments on Linux (described above).</p>

<h2>Anaconda (command conda)</h2>
<p>Anaconda presents a simplified way of how to manage system packages. It also provides functionality to install many popular packages without installing system dependencies first. As a result, the Anaconda is one of the most popular tools for data scientists (because most data science tools require system-level packages).</p>
<p>Technically speaking, Anaconda is a distribution of Python (it uses the native CPython interpreter, which you can easily install on your system). However, be aware that the Anaconda is proprietary software (there are commercial and free versions available).</p>

<h2>Virtual environments in IDE</h2>
<p>Your life will be much easier when you choose to use some good IDE for your coding work. One great IDE is JetBrains PyCharm (freely available on all platforms, including Windows, Linux, macOS). There is a straightforward way to manage an interpreter's dependencies, among other helpful things. You can manage your dependencies in PyCharm when you go File &#8594; Settings then in tab Project: NAME &#8594; Python Interpreter. Here you can see a list of installed dependencies (with their versions). Click on the plus (+) sign on the bottom to add a new dependency. You can easily find and install any dependency (in whatever version) you need. Internally, PyCharm uses the PyPi repository for finding packages.</p>

<figure>
    <img src="images/venv_pycharm.gif" alt="Figure 1: Screen of the PyCharm requirements window.">
    <figcaption>Figure 1: Screen of the PyCharm requirements window.</figcaption>
</figure>

<p>If you use a different IDE, the exact way to manage dependencies might differ - but the logic is always the same. For example, another popular IDE in the Python community is called Visual Studio Code. It is also available on all platforms and, similarly to PyCharm, provides a simple integrated way of managing dependencies.</p>

<h2>Summary</h2>
<p>A virtual environment is a fundamental concept in Python. The main goal is to separate Python's application dependencies. There are many ways for managing virtual environments - the most straightforward way is to use native command venv. That requires a system application that allows running venv - there is a simple way to install it on most Linux distributions and a slightly cumbersome way on Windows. Another way is to use Anaconda, which allows installing packages requiring system dependencies without installing anything on the system level. The most popular way in Python software engineering is to use the built-in support for virtual environments in IDE. Every popular IDE for Python supports virtual environments in some way.</p>

"""

ENTITY = cr.Article(
    title="Virtual environments in Python language",
    url_alias='virtual-environments-in-python-language',
    large_image_path="images/python_venv_big.jpg",
    small_image_path="images/python_venv_small.jpg",
    date=datetime.datetime(2020, 8, 14),
    tags=[cr.Tag('Virtual Environment', 'virtual-environment'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Python', 'python'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="Virtual environments in Python are the fundamental concept that makes developing of application much easier and cleaner. There is a simple way of managing it."
)
