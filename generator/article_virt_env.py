# Virtual environments in Python language
import datetime
import crinita as cr

lead = """Virtual environments are an incredibly helpful concept that makes your coding much easier. There are many tools in Python for creating and managing virtual environments. This article tends to analyze the native virtual environment (created using the venv command). Another simplified and more user-friendly approach is to use Anaconda software (using command conda)."""

content = """Virtual environments are an incredibly helpful concept that makes your coding much easier. There are many tools in Python for creating and managing virtual environments. This article tends to analyze the native virtual environment (created using the venv command). Another simplified and more user-friendly approach is to use Anaconda software (using command conda). 

<h2>What are the virtual environments? </h2>
<p>One of the crucial issue for Python developers is called virtual environment. Basically, it is helpful when you need to install (in order to run or use) Python's packages without affecting the system packages. Typically for testing or developing some applications. Managing of the virtual environment is typically one of the common features of the IDE (e.g. JetBrains <strong>PyCharm</strong> deal with this issue in a very efficient way). However, it is helpful to know how to manage it directly from the command line.</p>

<h2>What is the rationale for using virtual environments?</h2>
<p>The main reason is to separate dependencies between different Python applications. If one application does need a different set of dependencies than another application - it does not make sense to provide a whole bunch of dependencies to all of them. It can cause an error if one package in a particular application is required in a version that differs from a requirement in another application. It is also a good practice to provide your code with a valid requirements.txt file (defining the minimal set of requirements that the application needs) - virtual environments can help you to run your code cleanly (using strictly what is needed). Also, you can use environments for creating requirements lists. In many cases, you can encounter a situation where when you install requirements with some set of environmental variables it differs differently than when you install it with a different set - in this case, virtual environments presents the only way how to deal with this issue.</p>
<p>Another thing is are the requirements installed on the system level. It is a good practice to keep the list of requirements as small as possible. Mainly because you want to avoid some unexpected interference with local dependencies (as described above). So, pay extra attention to installing packages using PIP (ensure where exactly do you install them).</p>

<h2>Native virtual environment (command venv)</h2>
<p>This is the simplest (and oldest) approach for managing virtual environments. It is also the first choice option if you need something really simple. However, it has its cons as well. Many (even frequently used) packages require system-level dependencies. A typical example is a famous package called pyplot that provides helpful tools for plotting various types of graphs. It is though necessary to understand it - as it is often the only available tool (for example, if you are on some remote development machine or when you need to test something quickly).</p>

<h3>How to install virtualenv</h3>
<p>Depends on the machine you are using. For the Ubuntu, use just:</p>
<pre class="code"><code>sudo apt install python3-virtualenv</code></pre>
<p><em>Manual for Windows is below this section.</em></p>
<h3>How to use native venv command (on Linux)</h3>
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
<p>For installing requirements from the requirements.txt file (standard approach). Or you can simply install system packages using pip command directly:</p>
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

<p>It is helpful to know that the virtual environment has the same name as the folder where it is located. You can also use the activated environment in any folder you need. The best approach is to use a dedicated sub-folder of the Python project for the virtual environment. If you are using some version control system, be sure that you ignore the folder with the virtual environment (for GIT add its content to the .gitignore file) - as it typically contains a lot of useless files that has nothing to do with your application (which can be platform-specific and not working on another computer as expected).</p>
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

<p>Using Python interpreter is otherwise the same for Windows as it is for Linux (be aware of using different slashes). So once you are in a Virtual Environment you can proceed as when you were on your deployment machine.</p>

<h2>Anaconda (command conda)</h2>
<p>Anaconda presents a simplified way of how to manage system packages. It also provides functionality to install many popular packages without installing system dependencies first. Anaconda is one of the most popular tools for data scientists.</p>
<p>Technically speaking, Anaconda is a distribution of Python (it uses the native CPython interpreter which you can easily install on your system). Be aware of the fact, that the Anaconda is proprietary software (there are commercial and free versions available).</p>

<h2>A virtual environment in IDE</h2>
<p>When you chose to use some reasonable IDE for your coding work your life will be much easier. We recommend using JetBrains PyCharm (freely available on all platforms including Windows, Linux, macOS). Among other helpful things, there is a very simple way of how to manage an interpreter's dependencies. You can manage your dependencies in PyCharm when you go File -> Settings then in tab Project: NAME -> Python Interpreter. Here you can see a list of installed dependencies (with their versions). To add a new dependency click on the plus (+) sign on the bottom. You can easily find and install any dependency (in whatever version) you need.</p>
<p>If you use a different IDE, the exact way how to manage dependencies might differ - but the logic is always the same. Another popular IDE in the Python community is called Visual Studio Code. It is also available on all platforms and similarly to PyCharm provides a simple integrated way of managing dependencies.</p>

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
