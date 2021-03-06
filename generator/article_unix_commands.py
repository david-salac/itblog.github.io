# The acceleration of public–key cryptanalysis methods using Xilinx Zynq-7000
import datetime
import crinita as cr

lead = """If one chooses to do a software developer, he will sooner or later find out that there is a lot of need-to-know things. Among them are the commands of the bash shell (and the shell itself). It can save you a lot of time in the future if you learn them now. This post presents the most commonly used commands and use-cases for them. They are helpful not only for software developers but to everyone who works in IT."""

content = """If one chooses to do a software developer, he will sooner or later find out that there is a lot of need-to-know things. Among them are the commands of the bash shell (and the shell itself). It can save you a lot of time in the future if you learn them now. This post presents the most commonly used commands and use-cases for them. They are helpful not only for software developers but to everyone who works in IT.

<h2>Most helpful commands</h2>
<p>Knowing how questionable it is to say that some particular command is helpful and other is not, some of the most popular commands are present here. It is unquestionably true that if someone wants to work professionally in any IT branch, it is necessary to know them. There is a lot of commands missing in this list.</p>

<h3>Elementary commands cd, pwd, ls, mkdir, touch, nano, rm, echo, mv, cp, mc</h3>
<p>These commands are elementary, and probably all of you knows them. Command cd allows you to change directory, pwd writes you the absolute path of the current directory, ls list of all entities inside a directory, mkdir creates a new directory, touch creates a new empty file, nano allows you to edit this file, rm deletes entity (and rm -R removes directory). Command echo prints what its argument - typically the value of some variable - is. Command mv moves a file to another destination, command cp copy file. Command mc provides a helpful interface for managing files (similar to programs like Total Commander).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~/Temp$ mkdir testing  # Create directory 'testing'
david@david-PORTEGE-Z30-C:~/Temp$ cd testing  # Go to directory 'testing'
david@david-PORTEGE-Z30-C:~/Temp/testing$ touch smth.txt  # Create a file
david@david-PORTEGE-Z30-C:~/Temp/testing$ pwd  # Return current absolute path
/home/david/Temp/testing
david@david-PORTEGE-Z30-C:~/Temp/testing$ ls  # list of entities in directory
smth.txt
david@david-PORTEGE-Z30-C:~/Temp/testing$ cd ..  # Go one directory up
david@david-PORTEGE-Z30-C:~/Temp$ rm -r testing  # Remove directory 'testing'
david@david-PORTEGE-Z30-C:~/Temp$ nano report.txt  # Edit the file report.txt
david@david-PORTEGE-Z30-C:~$ echo $USER  # Print the username of current user
david
david@david-PORTEGE-Z30-C:~$ cp file_source file_target  # copy file
david@david-PORTEGE-Z30-C:~$ mv file_source file_target  # move file</code></pre>

<h3>Command date</h3>
<p>Returns the current date and time and time-zone installed on the computer. It is often helpful to know what the hardware time on your machine is (and what time-zone OS uses).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~/Documents$ date
Sun 15 Nov 12:54:18 GMT 2020</code></pre>

<h3>Command man</h3>
<p>Acronym of manual - provides helpful information (manual) about other commands. Technically shows you the manual written for a given application by its developers.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~/Temp$ man ls  # manual of ls command
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.
 Manual page ls(1) line 1 (press h for help or q to quit)</code></pre>

<h3>Command ps and ps -e</h3>
<p>Command ps is helpful to show you information about currently running processes. The command is particularly helpful with signal '-e' which shows you all currently running processes with its IDs.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ ps -e|grep firefox  # Find the 'firefox'
24875 tty2     02:32:33 firefox  # Process firefox has ID 24875</code></pre>
<p>To know the ID of a process is helpful if you need to kill some application (for example, when it is not responding).</p>

<h3>Command grep and especially grep -rn 'SOMETHING'</h3>
<p>Utility grep helpful for finding strings in some text. What is particularly helpful is grep with signals '-rn' that finds the given string in all files in the current directory (and its subdirectories) and print it with line number.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~/PycharmProjects/crinita$ grep -rn "Site"
crinita/config.py:139:    # Site map template
crinita/config.py:148:Sitemap: sitemap.xml
crinita/__init__.py:6:from .sites import Sites  # noqa
crinita/sites.py:89:class Sites(object):</code></pre>

<h3>Commands find and locate</h3>
<p>Helps you to find a file in the (sub)directories. Print the path to matching files relative to the current position in the file system. Command locate does the same but has a simpler syntax (but cannot find executable files).</p>
<pre class="code"><code># Finds 'setup.py' file in current directory and all subdirectories
david@david-PORTEGE-Z30-C:~/PycharmProjects/crinita$ find . -name setup.py
./setup.py
# Find 'sites.py' only in subdirectory 'crinita'
david@david-PORTEGE-Z30-C:~/crinita$ find crinita -name sites.py
crinita/sites.py
david@david-PORTEGE-Z30-C:~$ locate sdf.xlsx
/home/david/Temp/sdf.xlsx</code></pre>

<h3>Commands less, head, tail, cat</h3>
<p>Are elementary commands for browsing of the file content. If you quickly need to see what the content of some file you can use cat FILE_NAME - it writes you the content of the file as it is. If the file content is big (bigger than your screen) you can use smarter command less FILE_NAME that allows you to scroll the content. Command head prints you just first few line of file and tail last few lines of file.</p>
<pre class="code"><code># Print whole file LICENCE
david@david-PORTEGE-Z30-C:~/PycharmProjects/crinita$ cat LICENSE
MIT License
Copyright (c) 2020 David Salac

# Last five lines of generate.py file
david@david-PORTEGE-Z30-C:~/PycharmProjects/itblog_uk/$ tail -5 generate.py
sites.generate_pages(output_directory)
shutil.copytree(resource_directory, output_directory, dirs_exist_ok=True)

# First five lines of generate.py file
david@david-PORTEGE-Z30-C:~/PycharmProjects/itblog_uk/$ head -5 generate.py
from pathlib import Path
import shutil
from typing import List, Union
import pkgutil
from os import listdir</code></pre>

<h3>Commands df and du</h3>
<p>Command df provides information about the usage of volumes (disks, etc.). It is helpful to know how many per cent is available on your disk. On the other hand, command du provides you with information about the sizes of each (sub)directory. The most common signal is '-h' that recomputes provided information from bytes to something more human-readable (GB, MB etc.). Another helpful signal for the du command is '--max-depth=NR' that scan subdirectories only specified depth.</p>
<pre class="code"><code># Sizes of all (sub)directories in the directory 'Documents'
david@david-PORTEGE-Z30-C:~/Documents$ du --max-depth=1 -h
532K	./Prediction
2.8M	./Article
100K	./DataSources
48K	./Personal
64K	./DocumentAPI
56M	.  # Size of 'Documents' itself

# Disk usage
david@david-PORTEGE-Z30-C:~/Documents$ df -h
Filesystem                   Size  Used Avail Use% Mounted on
udev                         7.8G     0  7.8G   0% /dev
tmpfs                        1.6G  2.3M  1.6G   1% /run
/dev/mapper/ubuntu--vg-root  467G  324G  120G  74% /
tmpfs                        7.8G  1.6G  6.3G  21% /dev/shm
tmpfs                        5.0M  4.0K  5.0M   1% /run/lock
tmpfs                        7.8G     0  7.8G   0% /sys/fs/cgroup</code></pre>

<h3>Command ln source_file target_file</h3>
<p>Command ln allows you to create links to files (or directories). It allows creating a symbolic link (just a pointer) or hard links (behaves like targeted file itself).</p> 
<pre class="code"><code># Creates a symbolic link to local.env and rewrite existing if exist
david@david-PORTEGE-Z30-C:~/Documents$ ln -sf local.env .env</code></pre>

<h3>Commands top and htop</h3>
<p>These commands provide you interactive visualisation of CPU and memory usage. They are incredibly useful for analysing what is slowing down your system. Command htop is better but is not always available.</p>

<figure>
    <img src="images/htop_example.png" alt="Figure 1: Example of htop command">
    <figcaption>Figure 1: Command htop allows you to visualise running processes</figcaption>
</figure>

<h3>Command kill</h3>
<p>This command terminates the process. There is one crucial signal '-9' that literally (insecurely) terminates any process as soon as possible (if you do not have to use it, try to avoid it). The argument of kill command is the ID of the process. You can get it for example by using ps -e command.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ ps -e|grep firefox
24875 tty2     02:48:19 firefox  # Find the ID of firefox process
david@david-PORTEGE-Z30-C:~$ kill -9 24875  # Terminate firefox (per force)</code></pre>

<h3>Command export, printenv</h3>
<p>Export variable and makes it to behave like an environmental variable.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ export SUPER_VARIABLE=11
david@david-PORTEGE-Z30-C:~$ export | grep SUPER_VARIABLE
declare -x SUPER_VARIABLE="11"
david@david-PORTEGE-Z30-C:~$ printenv
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
<p>This command is essential to use if some application requires to have environmental variables to be set-up for some value (widespread in the Linux world).</p>
<p>Command printenv prints all environmental variables that are currently available. </p>

<h3>Commands sudo and su</h3>
<p>Command sudo allows you to run some other command as a root user (just this particular command). Command su allows you to switch to a different user.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ sudo apt update  # update system (requires root)
david@david-PORTEGE-Z30-C:~$ su root  # switch user to root user
david@david-PORTEGE-Z30-C:~$ sudo passwd  # setup new password for root user</code></pre>

<h3>Commands passwd and pwgen</h3>
<p>Command passwd allows you to change password. Utility pwgen (which is not always available) allows you to generate some random passwords (quite a helpful tool).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ pwgen -s 10  # generate 10 characters passwords
eISx1P6FfU O1zdMR3Sm8 SDj6xINoho Wbk57eijTR 5QrjjXkw0K QTo3V8b1jE 4G6PbasYSO
A23E6VqttH fny7U2gBD5 AIEHt2WDqF UGapu3GQSG YijtaeGj4S 5QtTpLYFc6 4fXrZux4CG</code></pre>

<h3>Command uname</h3>
<p>Returns you helpful information about the system. The most important signal is '-a'.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ uname -a
Linux david-PORTEGE-Z30-C 5.4.0-52-generic #57~18.04.1-Ubuntu SMP
# Thu Oct 15 14:04:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux</code></pre>

<h3>Internet commands whois, dig, curl, ping, ssh</h3>
<p>These commands are incredibly helpful if you develop websites. Command whois returns you informations about domain owner. Command dig provides you info about DNS configuration, and the command curl downloads you the given URL. Command ping is the command that tests if some remote IP (or URL) is accessible. Command ssh allows you to connect to the external system (you need to know an address and port - and also the external station has to allow remote access and have public IP).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ whois crinita.com
   Domain Name: CRINITA.COM
   Registry Domain ID: 2569613732_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.regtons.com
   Registrar URL: http://regtons.com
   # ...
>>> Last update of whois database: 2020-11-15T18:01:07Z <<<

david@david-PORTEGE-Z30-C:~$ dig crinita.com
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

david@david-PORTEGE-Z30-C:~$ ping google.com
PING google.com (216.58.211.174) 56(84) bytes of data.
64 bytes from dub08s01-in-f14.1e100.net (216.58.211.174): icmp_seq=1 ttl=117 time=18.3 ms
64 bytes from dub08s01-in-f14.1e100.net (216.58.211.174): icmp_seq=2 ttl=117 time=22.5 ms
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 18.300/20.406/22.513/2.111 ms</code></pre>

<h3>Commands chown and chmod</h3>
<p>Command chown allows you to change the owner of some file/folder. If the owner of the file is someone else, you need to run it with sudo (as you do not have privileges to modify privileges to files owned by someone else if you are not root). Command chmod allows you to set up privileges that owner/group has (typically it is helpful when you want to make some script executable). If you want to see who is the owner of the file and what is the file mode (permission that group/owner has), use command <code>ls -l</code>.</p>
<pre class="code"><code>
david@david-PORTEGE-Z30-C:~/Temp$ chown $USER:$USER something.txt
david@david-PORTEGE-Z30-C:~/Temp$ ls -la
total 12164
drwxr-xr-x 20 david david    4096 Nov 17 15:20 .
drwxr-xr-x 48 david david    4096 Nov 17 14:42 ..
-rw-r--r--  1 david david       0 Nov 17 15:20 something.txt

# Makes file executable:
david@david-PORTEGE-Z30-C:~/Temp$ chmod +x something.txt
david@david-PORTEGE-Z30-C:~/Temp$ ls -la
total 12164
drwxr-xr-x 20 david david    4096 Nov 17 15:20 .
drwxr-xr-x 48 david david    4096 Nov 17 14:42 ..
-rwxr-xr-x  1 david david       0 Nov 17 15:20 something.txt</code></pre>

<h3>Command finger, w, whoami</h3>
<p>Provide information about the user that is now log in. Command finger is more detailed. And command w is more technical.</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ finger
Login     Name       Tty      Idle  Login Time   Office     Office Phone
david     david     *:0             Nov 16 12:22 (:0)
david@david-PORTEGE-Z30-C:~$ whoami
david
david@david-PORTEGE-Z30-C:~$ w
 15:27:30 up 1 day,  3:05,  1 user,  load average: 4.72, 4.46, 3.49
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
david    :0       :0               Mon12   ?xdm?  57:02   0.02s /usr/lib/gdm3/g</code></pre>

<h3>Command free</h3>
<p>Provides details about the usage of system memory (not disk usage - there are commands df, du for this purposes).</p> 
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ free
              total        used        free      shared  buff/cache   available
Mem:       16328668     9947740      575804     3385264     5805124     2676156
Swap:       1003516      162816      840700</code></pre>

<h3>Command lsblk</h3>
<p>Provides you with the list of available devices and end-points where they are mounted (path to directory).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~$ lsblk
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
<p>Compares the differences in the content of two files. It's incredibly helpful to compare what has changed (and on which line and character).</p>
<pre class="code"><code>david@david-PORTEGE-Z30-C:~/Temp$ diff something_1.txt something_2.txt
1c1
< Hello world!
---
> Hello wolldd!</code></pre>

<h3>System-level commands shutdown, mount, service</h3>
<p>It is good to know about them, but it is slightly out of the scope of this article to describe them carefully. Simply shutdown allows you to shut down (or restart) the computer, the mount allows you to mount the external volume (or network location), and service allows you to manage system services.</p>
<pre class="code"><code># List of all services available on your machine
david@david-PORTEGE-Z30-C:~$ service --status-all
 [ + ]  acpid
 [ - ]  alsa-utils
 [ - ]  anacron
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd</code></pre>

<h3>Command dd</h3>
<p>The dd command is useful if you want to create a bootable disk.</p>

<h3>Command sed</h3>
<p>Allows you to replace some characters in the file (or stream).</p>

<h2>Some other helpful things</h2>
<p>It is of course not possible to describe the full capability of a Unix shell in one article. Here are some other common things that are good to know.</p>

<h3>How to run a file</h3>
<p>If you want to run some script, it has to be executable (see chmod command above). To run file located directly in the current folder, use the command <code>./file-name</code>. If it is located somewhere else, use just the <code>path/to/the/file</code>.</p> 

<h3>What to do with spaces</h3>
<p>If you need to access some file that has spaces in its name, use backslash symbol before it, for example: <code>some\ file\ with\ spaces.sh</code></p>

<h3>Pressing tabulator</h3>
<p>Often, if you want to make your life easier, you can press tabulator after writing a few starting characters of your file - system automatically fills the remaining part. If there is some conflict (more than one file matches), press tabulator twice and you will see the list of options.</p>

<h3>Pipeline</h3>
<p>The pipeline is a useful concept in Unix. It makes the output of one command to be passed as the input of another. It is characterised by the '|' symbol. The typical example is:</p>
<pre class="code"><code>ps -e | grep "firefox"</code></pre>
<p>This example prints all the processes in the system and then find the one with the name "firefox" using grep command.</p>

<h3>Print to file and append to file</h3>
<p>If you want to print the output of a command to the file, use the '>' symbol, for appending to existing file use '>>'.</p>
<pre class="code"><code>ls -la > list_of_files.txt</code></pre>
<p>This example creates a file list_of_files.txt with a list of all entities in the directory.</p>
<h2>Summary</h2>
<p>This article describes the most popular Unix commands. The list is naturally not complete but covers the most important ones. These commands are as general as they can be. They are typically available on all Linux distributions and some of them also on Mac terminal (as Mac is technically the Unix). If you find your favourite command missing here, please drop me a message.</p>
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
