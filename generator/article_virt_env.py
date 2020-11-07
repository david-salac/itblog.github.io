# Virtual environments in Python language
import datetime
import crinita as cr

lead = """There are many tools in Python for creating and managing virtual environments. This article tends to analyze native virtual environment (created using venv command). Another simplified and more user-friendly approach is to use Anaconda software (using command conda)."""

content = """There are many tools in Python for creating and managing virtual environments. This article tends to analyze native virtual environment (created using venv command). Another simplified and more user-friendly approach is to use Anaconda software (using command conda).

<h2>What are the virtual environments? </h2>
<p>One of the crucial issue for Python developers is called virtual environment. Basically, it is helpful when you need to install (in order to run or use) Python's packages without affecting the system packages. Typically for testing or developing some applications. Managing of the virtual environment is typically one of the common features of the IDE (e.g. JetBrains <strong>PyCharm</strong> deal with this issue in a very efficient way). However, it is helpful to know how to manage it directly from the command line.</p>

<h2>Native virtual environment (command venv)</h2>
<p>This is the oldest approach for managing virtual environments. It is also the first choice option if you need something really simple. However, it has its cons as well. Many (even frequently used) packages require system-level dependencies. A typical example is a famous package called pyplot that provides helpful tools for plotting of various types of graphs.</p>

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
<pre class="code"><code>pip3 install NAME_OF_PACKAGE</code></pre>
</li>
<li>
<p>If you want to deactivate the virtual environment, use the commend:</p>
<pre class="code"><code>deactivate</code></pre>
<p>You should see the standard terminal window now.</p>
</li>
</ol>

<p>It is helpful to know that the virtual environment has the same name as the folder where it is located. You can also use the activated environment in any folder you need. The best approach is to use dedicated sub-folder of the Python project for the virtual environment (and add its content to the .gitignore file).</p>
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

<h2>Anaconda (command conda)</h2>
<p>Anaconda presents a simplified way of how to manage system packages. It also provides functionality to install many popular packages without installing system dependencies first. Anaconda is one of the most popular tools for data scientists.</p>

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
