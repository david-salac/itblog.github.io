# Helpful commands for Linux terminal with a quick introduction to Unix shell
import datetime
import crinita as cr

lead = """If one chooses to do a software developer, he will sooner or later find out that there is a lot of need-to-know things. Among them are the commands of the bash shell (and the shell itself). It can save you a lot of time in the future if you learn them now. This post presents the most commonly used commands and use-cases for them. They are helpful not only for software developers but to everyone who works in IT."""

content = """<p class="lead">If one chooses to do a software developer, he will sooner or later find out that there is a lot of need-to-know things. Among them are the commands of the bash shell (and the shell itself). It can save you a lot of time in the future if you learn them now. This post presents the most commonly used commands and use-cases for them. They are helpful not only for software developers but to everyone who works in IT.</p>

<h2>Most helpful commands</h2>
<p>Knowing how questionable it is to say that a particular command is helpful and another is not, some of the most popular commands are present here. It is unquestionably true that if someone wants to work professionally in any IT branch, it is necessary to know them. Unfortunately, there is a lot of commands missing inside the list.</p>

<h3>Elementary commands cd, pwd, ls, mkdir, touch, nano, rm, echo, mv, cp, mc</h3>
<p>These commands are elementary, and probably every reader knows them. Command <code>cd</code> allows you to change directory, <code>pwd</code> writes you the absolute path of the current directory, <code>ls</code> list of all entities inside a directory, <code>mkdir</code> creates a new directory, <code>touch</code> creates a new empty file, <code>nano</code> allows you to edit this file, <code>rm</code> deletes entity (and <code>rm -R</code> removes directory). Command <code>echo</code> prints its argument - typically the value of a variable. Command <code>mv</code> moves a file to another destination, command <code>cp</code> copy file. Finally, command <code>mc</code> provides a helpful interface for managing files (similar to programs like Total Commander).</p>

<pre class="code"><code>usr@host:~/Temp$ mkdir testing  # Create directory 'testing'
usr@host:~/Temp$ cd testing  # Go to directory 'testing'
usr@host:~/Temp/testing$ touch smth.txt  # Create a file
usr@host:~/Temp/testing$ pwd  # Return current absolute path
/home/david/Temp/testing
usr@host:~/Temp/testing$ ls  # list of entities in directory
smth.txt
usr@host:~/Temp/testing$ cd ..  # Go one directory up
usr@host:~/Temp$ rm -r testing  # Remove directory 'testing'
usr@host:~/Temp$ nano report.txt  # Edit the file report.txt
usr@host:~$ echo $USER  # Print the username of current user
david
usr@host:~$ cp file_source file_target  # copy file
usr@host:~$ mv file_source file_target  # move file</code></pre>

<h3>Command date</h3>
<p>Returns the current date and time, and time-zone installed on the computer. It is often helpful to know the hardware time on your machine (and what time-zone OS uses), primarily if you work on a remote machine.</p>
<pre class="code"><code>usr@host:~/Documents$ date
Sun 15 Nov 12:54:18 GMT 2020</code></pre>

<h3>Command man</h3>
<p>Acronym of manual - provides helpful information (manual) about other commands (what they do, how to use them). Technically shows you the manual written for a given application by its developers.</p>
<pre class="code"><code>usr@host:~/Temp$ man ls  # manual of ls command
LS(1)                 User Commands                LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current di‐
       rectory by default).  Sort entries alphabetically
       if none of -cftuvSUX nor --sort is specified.</code></pre>

<h3>Command ps and ps -e</h3>
<p>Command <code>ps</code> is helpful to show you information about currently running processes. The command is particularly helpful with signal <code>-e</code>, which shows all currently running processes with their IDs.</p>
<pre class="code"><code>usr@host:~$ ps -e|grep firefox  # Find the 'firefox'
24875 tty2     02:32:33 firefox  # Process firefox has ID 24875</code></pre>
<p>To know the ID of a process is helpful if you need to terminate (aka kill) an application (for example, when it is not responding).</p>

<h3>Command grep and especially grep -rn 'SOMETHING'</h3>
<p>Utility <code>grep</code> helps find strings in some text. What is particularly helpful is grep with signals <code>rn</code> that finds the given string in all files in the current directory (and its subdirectories) and print it with the line number. If you add signal <code>i</code>, it becomes case insensitive.</p>
<pre class="code"><code>usr@host:~/PycharmProjects/crinita$ grep -rn "Site"
crinita/config.py:139:    # Site map template
crinita/config.py:148:Sitemap: sitemap.xml
crinita/__init__.py:6:from .sites import Sites  # noqa
crinita/sites.py:89:class Sites(object):</code></pre>

<h3>Commands find and locate</h3>
<p>Help you to find a file in (sub)directories. Print the path to matching files relative to the current position in the file system. Command <code>locate</code> does the same but has a simpler syntax.</p>
<pre class="code"><code># Finds 'setup.py' file in current dir and all subdirectories
usr@host:~/PycharmProjects/crinita$ find . -name setup.py
./setup.py
# Find 'sites.py' only in subdirectory 'crinita'
usr@host:~/crinita$ find crinita -name sites.py
crinita/sites.py
usr@host:~$ locate sdf.xlsx
/home/david/Temp/sdf.xlsx</code></pre>

<h3>Commands less, head, tail, cat</h3>
<p>These are elementary commands for browsing the file content. If you quickly need to see the content of a file, you can use <code>cat FILE_NAME</code> - it writes you the content of the file as it is. If the file content is too big (e. g., bigger than your screen), you can use smarter command <code>less FILE_NAME</code> that allows you to scroll the content. Command <code>head</code> prints just the first few lines of the file and <code>tail</code> the last few lines (you can set how many lines you want by signal <code>-n NUMBER</code>).</p>
<pre class="code"><code># Print whole file LICENCE
usr@host:~/PycharmProjects/crinita$ cat LICENSE
MIT License
Copyright (c) 2020 David Salac

# Last five lines of generate.py file
usr@host:~/PycharmProjects/itblog_uk/$ tail -5 generate.py
sites.generate_pages(output_directory)
shutil.copytree(resource_directory, output_directory, dirs_exist_ok=True)

# First five lines of generate.py file
usr@host:~/PycharmProjects/itblog_uk/$ head -5 generate.py
from pathlib import Path
import shutil
from typing import List, Union
import pkgutil
from os import listdir</code></pre>

<h3>Commands df and du</h3>
<p>Command <code>df</code> provides information about the usage of volumes (disks, etc.). For example, it is helpful to know how many per cent is available on your disk. On the other hand, command <code>du</code> provides you with information about the sizes of each (sub)directory. The most common signal for both is <code>-h</code> that recomputes provided information from bytes to something more human-readable (using GB, MB etc. and not just bytes). Another helpful signal for the <code>du</code> command is <code>--max-depth=NR</code> that scan subdirectories only in specified depth.</p>
<pre class="code"><code># Sizes of all (sub)directories in the directory 'Documents'
usr@host:~/Documents$ du --max-depth=1 -h
532K	./Prediction
2.8M	./Article
100K	./DataSources
48K	./Personal
64K	./DocumentAPI
56M	.  # Size of 'Documents' itself

# Disk usage
usr@host:~/Documents$ df -h
Filesystem                   Size  Used Avail Use% Mounted on
udev                         7.8G     0  7.8G   0% /dev
tmpfs                        1.6G  2.3M  1.6G   1% /run
/dev/mapper/ubuntu--vg-root  467G  324G  120G  74% /
tmpfs                        7.8G  1.6G  6.3G  21% /dev/shm
tmpfs                        5.0M  4.0K  5.0M   1% /run/lock
tmpfs                        7.8G     0  7.8G   0% /sys/fs/cgroup</code></pre>

<h3>Command ln source_file target_file</h3>
<p>Command <code>ln</code> allows you to create links to files (or directories). It creates a symbolic link (just a pointer) or hard links (behaves like the targeted file itself). In addition, you can configure ln to create other types of links (see the manual).</p> 
<pre class="code"><code># Creates a symbolic link to local.env and rewrite existing if exist
usr@host:~/Documents$ ln -sf local.env .env</code></pre>

<h3>Commands top and htop</h3>
<p>These commands provide you with interactive visualisation of CPU and memory usage. They are handy for analysing what is slowing down your system. Command <code>htop</code> is better but is not always available.</p>

<pre class="code"><code>usr@host:~/Documents$ htop
 Mem[||||      1.05G/24.9G]   Tasks: 13, 33 thr; 1 running
 Swp[             0K/7.00G]   Load average: 0.00 0.01 0.00 
                              Uptime: 5 days, 00:32:44

 PID USER  PRI  NI  VIRT   RES  SHR S CPU% MEM%   TIME+  Command
   6 root   20   0   908   520  468 S  0.0  0.0  0:00.00 /init
   1 root   20   0   908   520  468 S  0.0  0.0  0:00.01 /init
 111 root   20   0   900    80   20 S  0.0  0.0  0:00.00 /init
 112 root   20   0   900    80   20 S  0.0  0.0  0:00.00 /init
 114 root   20   0 1567M 32056 2840 S  0.0  0.1  0:00.68 /mnt/ws
 115 root   20   0 1567M 32056 2840 S  0.0  0.1  0:01.59 /mnt/ws
 116 root   20   0 1567M 32056 2840 S  0.0  0.1  0:01.35 /mnt/ws
 117 root   20   0 1567M 32056 2840 S  0.0  0.1  0:01.61 /mnt/ws
 118 root   20   0 1567M 32056 2840 S  0.0  0.1  0:00.00 /mnt/ws</code></pre>

<h3>Command kill</h3>
<p>This command terminates the process. One crucial signal, <code>-9</code> literally (insecurely) terminates any process as soon as possible (if you do not have to use it, try to avoid it). The argument of <code>kill</code> command is the ID of the process. You can get it, for example, by using the <code>ps -e</code> command.</p>
<pre class="code"><code>usr@host:~$ ps -e|grep firefox  # Find the ID of firefox process
24875 tty2     02:48:19 firefox
usr@host:~$ kill -9 24875  # Terminate firefox (per force)</code></pre>

<h3>Command export, printenv</h3>
<p>The command <code>export</code> is helpful to create an environmental variable of the session. The command <code>printenv</code> displays all environmental variables available.</p>
<pre class="code"><code>usr@host:~$ export SUPER_VARIABLE=11
usr@host:~$ export | grep SUPER_VARIABLE
declare -x SUPER_VARIABLE="11"
usr@host:~$ printenv
LANG=en_GB.UTF-8
DISPLAY=:0
GNOME_SHELL_SESSION_MODE=ubuntu
USERNAME=david
XDG_VTNR=2
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
MANDATORY_PATH=/usr/share/gconf/ubuntu.mandatory.path
XDG_SESSION_ID=2
USER=david
DESKTOP_SESSION=ubuntu</code></pre>
<p>This command is essential if some application (or another command) requires specific environmental variables having some value (widespread in the Linux world).</p>

<h3>Commands sudo and su</h3>
<p>Command <code>sudo</code> allows you to run another command as a root user (just this particular command). Command <code>su</code> allows you to switch to a different user (by default to the root user).</p>
<pre class="code"><code>usr@host:~$ sudo apt update  # update system (requires root)
usr@host:~$ su root  # switch user to root user
usr@host:~$ sudo passwd  # setup new password for root user</code></pre>

<h3>Commands passwd and pwgen</h3>
<p>Command <code>passwd</code> allows you to change the password on your current account. Utility <code>pwgen</code> (which is not always available) allows you to generate random passwords (quite a helpful tool).</p>
<pre class="code"><code>usr@host:~$ pwgen -s 10  # generate 10 characters passwords
eISx1P6FfU O1zdMR3Sm8 SDj6xINoho Wbk57eijTR 5QrjjXkw0K
A23E6VqttH fny7U2gBD5 AIEHt2WDqF UGapu3GQSG YijtaeGj4S</code></pre>

<h3>Command uname</h3>
<p>Returns you helpful information about the system. The most important signal is <code>-a</code> (an acronym for all).</p>
<pre class="code"><code>usr@host:~$ uname -a
Linux david 5.4.0-52-generic #57~18.04.1-Ubuntu SMP
# Thu Oct 15 14:04:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux</code></pre>

<h3>Internet commands whois, dig, curl, ping, ssh</h3>
<p>These commands are incredibly helpful if you develop websites (or manage servers). Command <code>whois</code> returns you informations about the domain owner. Command <code>dig</code> provides you info about DNS configuration, and the command <code>curl</code> downloads you the given URL. Command <code>ping</code> is the command that tests if some remote IP (or URL) is accessible. Finally, command <code>ssh</code> allows you to connect to the external system (you need to know an address and port - and also the external station has to allow remote access and have public IP).</p>
<pre class="code"><code>usr@host:~$ whois crinita.com
   Domain Name: CRINITA.COM
   Registry Domain ID: 2569613732_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.regtons.com
   Registrar URL: http://regtons.com
   # ...
>>> Last update of whois database: 2020-11-15T18:01:07Z <<<

usr@host:~$ dig crinita.com
; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> crinita.com
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;crinita.com.			IN	A

;; ANSWER SECTION:
crinita.com.		900	IN	A	185.199.109.153
crinita.com.		900	IN	A	185.199.110.153
crinita.com.		900	IN	A	185.199.111.153
crinita.com.		900	IN	A	185.199.108.153

usr@host:~$ ping google.com
PING google.com (216.58.211.174) 56(84) bytes of data.
6 bytes from dub.net (4.58.11.17): icmp_seq=1 ttl=117 time=8.3 ms
6 bytes from dub.net (4.58.11.17): icmp_seq=2 ttl=117 time=7.5 ms
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 18.300/20.406/22.513/2.111 ms</code></pre>

<h3>Commands chown and chmod</h3>
<p>Command <code>chown</code> allows you to change the owner of some file/folder. If the file owner is someone else, you need to run it with <code>sudo</code> (as you do not have privileges to modify privileges to files owned by someone else if you are not root). Command <code>chmod</code> allows you to set up privileges that the owner/group has (typically, it is helpful when you want to make some script executable). Finally, when you want to see the file owner and the file mode (permission that group/owner has), use the command <code>ls -l</code>.</p>
<pre class="code"><code>usr@host:~/Temp$ chown $USER:$USER something.txt
usr@host:~/Temp$ ls -la
total 12164
drwxr-xr-x 20 david david    4096 Nov 17 15:20 .
drwxr-xr-x 48 david david    4096 Nov 17 14:42 ..
-rw-r--r--  1 david david       0 Nov 17 15:20 something.txt

# Makes file executable:
usr@host:~/Temp$ chmod +x something.txt
usr@host:~/Temp$ ls -la
total 12164
drwxr-xr-x 20 david david    4096 Nov 17 15:20 .
drwxr-xr-x 48 david david    4096 Nov 17 14:42 ..
-rwxr-xr-x  1 david david       0 Nov 17 15:20 something.txt</code></pre>

<h3>Command finger, w, whoami</h3>
<p>Provide information about the user that is now logged in. Command <code>finger</code> is more detailed. And command <code>w</code> is more technical.</p>
<pre class="code"><code>usr@host:~$ finger
Login   Name     Tty   Idle  Login Time   Office  Office Phone
david   david   *:0          Nov 16 12:22 (:0)

usr@host:~$ whoami
david

usr@host:~$ w
 15:27:30 up 1 day,  3:05,  1 user,  load average: 4.7, 4.4, 3.4
USER   TTY    FROM    LOGIN@   IDLE   JCPU   PCPU WHAT
david  :0     :0      Mon12   ?xdm?  57:02   0.02s /usr/lib/g</code></pre>

<h3>Command free</h3>
<p>Provides details about system memory usage (not disk usage - there are commands <code>df</code>, <code>du</code> for this purposes).</p> 
<pre class="code"><code>usr@host:~$ free
         total   used      free   shared  buff/cache  available
Mem:   1632668  97740    575804   335264     5805124    2676156
Swap:   100516  12816    840700</code></pre>

<h3>Command lsblk</h3>
<p>Provides you with the list of available devices and end-points where they are mounted (directory path).</p>
<pre class="code"><code>usr@host:~$ lsblk
NAME                   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                      8:0    0   477G  0 disk
├─sda1                   8:1    0   512M  0 part  /boot/efi
├─sda2                   8:2    0   732M  0 part  /boot
└─sda3                   8:3    0 475.7G  0 part
  └─sda3_crypt         253:0    0 475.7G  0 crypt
    ├─ubuntu--vg-root  253:1    0 474.8G  0 lvm   /
    └─ubuntu--vg-swap_1
                       253:2    0   980M  0 lvm   [SWAP]</code></pre>

<h3>Command diff</h3>
<p>Compares the differences in the content of the two files. It's incredibly helpful to compare what has changed (on what line and character).</p>
<pre class="code"><code>usr@host:~/Temp$ diff something_1.txt something_2.txt
1c1
< Hello world!
---
> Hello wolldd!</code></pre>

<h3>System-level commands shutdown, mount, service</h3>
<p>It is good to know about them, but it is slightly out of the scope of this article to describe them carefully. Simply <code>shutdown</code> allows you to shut down (or restart) the computer, the <code>mount</code> allows you to mount the external volume (or network location), and the <code>service</code> command allows you to manage system services.</p>
<pre class="code"><code># List of all services available on your machine
usr@host:~$ service --status-all
 [ + ]  acpid
 [ - ]  alsa-utils
 [ - ]  anacron
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd</code></pre>

<h3>Command dd</h3>
<p>The <code>dd</code> command is useful if you want to create a bootable disk.</p>

<h3>Command sed</h3>
<p>Allows you to replace a string in the file (or stream) with a different string.</p>

<pre class="code">usr@host:~$ cat xyz.txt
hello there
usr@host:~$ # Now replace 'hello' with 'cao':
usr@host:~$ sed 's/hello/cao/' xyz.txt
cao there<code></code></pre>

<h2>Some other helpful things</h2>
<p>It is, of course, not possible to describe the full capability of a Unix shell in one article. However, here are some other everyday things that are good to know.</p>

<h3>How to run a file</h3>
<p>If you want to run some script, it must be executable (see <code>chmod</code> command above). To run a file located directly in the current folder, use the command <code>./file-name</code>. If it is located somewhere else, use just the <code>path/to/the/file</code>.</p> 

<h3>What to do with spaces</h3>
<p>If you need to access some file that has spaces in its name, use backslash symbol before it, for example: <code>some\ file\ with\ spaces.sh</code></p>

<h3>Pressing tabulator</h3>
<p>If you want to make your life easier, you can often press the tabulator after writing a few starting characters of your file - the system automatically fills the remaining part. If there is some conflict (more than one file matches), press tabulator twice, and you will see the list of options.</p>

<h3>Pipeline</h3>
<p>The pipeline is a useful concept in Unix. It makes the output of one command be passed as the input of another. It is characterised by the '|' symbol. The typical example is:</p>
<pre class="code"><code>ps -e | grep "firefox"</code></pre>
<p>This example prints all the system processes and then finds those with the name "firefox" using the grep command.</p>

<h3>Print to file and append to file</h3>
<p>If you want to print the output of a command to the file, use the '>' symbol. For appending to the existing file, use '>>'.</p>
<pre class="code"><code>ls -la > list_of_files.txt</code></pre>
<p>This example creates a file list_of_files.txt with a list of all entities in the directory.</p>
<h2>Summary</h2>
<p>This article describes the most popular Unix commands. The list is naturally not complete but covers the most important ones. These commands are as general as they can be. They are typically available on all Linux distributions, and some of them are also on the Mac terminal (as Mac is technically the Unix). If you spend some time searching other articles, you can find a lot of other helpful tools that are available.</p>
"""

ENTITY = cr.Article(
    title="Helpful commands for Linux terminal with a quick introduction to Unix shell",
    url_alias='helpful-commands-for-linux-terminal-with-a-quick-introduction-to-unix-shell',
    large_image_path="images/terminal_big.jpg",
    small_image_path="images/terminal_small.jpg",
    date=datetime.datetime(2020, 7, 17),
    tags=[cr.Tag('Linux', 'linux'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Essentials', 'essentials'),
          cr.Tag('Terminal', 'terminal'),
          cr.Tag('Administration', 'administration')],
    content=content,
    lead=lead
)
