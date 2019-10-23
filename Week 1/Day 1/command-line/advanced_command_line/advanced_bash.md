# Advanced Command Line Techniques

This file will be a fairly quick run-through of many more advanced command
line techniques that I've found to be useful throughout the years. If you
follow along, we'll be creating a series of files, then manipulating them with
bash scripts, sed commands, etc... so this will sort of assume you've done
things in order. Note, this is not exhaustive, I'm just showing you some of
the tools I've found handy throughout my time doing things.

Before we get started run:

```bash
echo $SHELL
```

and make sure that it says something like `/bin/bash` (or really anything that
ends in `bash`. There are other command line interfaces, but we'll be using
BASH for our scripting.


## Getting Data

Let's get some data to play with. If you're on mac you can use:

```bash
curl
https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
> data.txt
```

This grabs the data from https location, and downloads it to your machine. Now
if you don't put the ` > file_name_here`, then it just displays the file in 
the terminal. The arrow says, "put this into whatever file name I give you."

In linux you can do:
```bash
wget
https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
> data.txt
```

for the same effect. 

## Manipulating Data with `sed`

`sed` is a great tool for doing large scale manipulations on files. For now,
let's start by trying to change every instance of the word "honda" in our
dataset to the word "OHYEAH".

`sed` uses a certain style of expression to do stream manipulations. So let's
see how that works before we get crazy with files.

Try doing this:

```
echo "oh hey there" | sed s/oh/yep/g
```

`sed` takes the stream and does a substitution (that's the `s/` thing),
replacing all instances of the expression 'oh' with the expression 'yep'. The
`/g` means "do this globally across the whole stream. Note that the
expressions that are being replaces CAN be RegEx's if you set the appropriate
flags in the sed call. Now let's do that on a file.

```
sed s/honda/OHYEAH/g data.txt
```

Now scroll through the output. Note that every instance of the word "honda" is
now replaced with the word "OHYEAH". Maybe we don't want that to just print to
the terminal though? We can tell `sed` make this edit in place but to also create a backup of our original dataset.

```
sed -i .TEST s/honda/OHYEAH/g data.txt
```

This creates a new file called `data.txt.TEST` that is made up of our original version of data.txt. If we want to store the changes in the same file as it
was before WITHOUT creating a backup, we can just do:

```
sed -i '' s/honda/OHYEAH/g data.txt
```

Now this seems fairly silly in this context, but this can be super handy for
doing bulk replacement of NaN's and cleaning up errors that occur across whole
datasets. Let's see how this can work by building out first bash script.

## Getting data in a script

Let's go ahead and load many copies of this same data to test with. To do
that, we'll use a BASH script that does some for looping. Let's see it in
action. Start by opening a file called `load_data_batches.sh` and adding:

```bash
#!/bin/bash

for i in `seq 0 10`;
do
  curl https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data > data$i.txt
done
```
> Heads up: You may have to swap in `wget` for `curl` in your version

The first line tells the terminal to execute this as a BASH script. This is called a 'shebang' for reasons I have no idea about. Then this code loops through 10 times (`seq 0 10` is sequence from 0 to 10), and does whatever is in the `do`-`done` loop. In this case, it runs a `curl` and pushes the data into a text file. Note the `data$i.txt`. The dollar sign is BASH for "thi  is a variable name I want you to unpack."

If I run this with `bash load_data_batches.sh`, then I run `ls` and see that I
have data in 11 different files now!

Cool. So what if I want to clean up all the files? Let's do another BASH
script.

I notice in the data that we have several `?` hanging out. Python doesn't know
how to handle the `?`, but can easily handle `nan`. So we're going to swap out
all the `?` with `nan`. Let's create a file called `clean_data.sh`.

```bash
#!/bin/bash

for filename in $( ls data{0..10}.txt );
do
  echo "Cleaning $filename"
  sed -i "" s/'?  '/nan/g $filename
done
```

This `for` is a bit different. It's not iterating through a range, it's
iterating through the return of another bash call. So we asked it to show us
all files that have the name `data##.txt` where `##` is in the range 0-10.
That's another bash thing. Try it on your terminal, just type `ls
data{0..10}.txt` and you should see all of the files. By wrapping this inside
of a `$( )`, we're telling bash to treat this as a stand alone to command and
then use the output of that as something to unpack.

Then we go into the loop, and run `sed` to change the `?` to `nan`. Note that
I actually changed `?  ` into `nan` in order to preserve some spacing stuff
incase I later need to split on spaces or something.

This has more about [BASH
loops](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html).

## `rsync` - it's a less terrible `cp`

We've got our data, now what if we want to copy it to a different place? We
could always use `cp` and `scp` to move either locally or across the
internets, respectively. However there's a downside there... if the connection
breaks, or if there is a weird glitch, there's no recovery. We just have to
start over the whole transfer. `rsync` can pickup where it left off, as well
as also being able to do things like, "has this file changed since the last
time I copied? If not, I'll just skip recopying it. However, it does rely
explicitly on two things:

1. For the internet transfers, you must use SSH
2. Both the start and endpoint have to have `rsync` installed. However, it's
   so common that it's rarely a worry now-a-days.

Example code:

```bash
mkdir test
rsync data3.txt test/.
```

This would be for a local transfer. You can also use `-r` to mean "move the
directory" just like with `cp`. If you wanted to do a a remote trasnfer, you'd
do a similar thing, you'd just tell it about your SSH connections with the
`-e` flag.

```bash
rsync -e "ssh -i /path/to/key.pem" data.txt username@IP_Address:/path/here
```

Even better, you could consider setting up your ssh config (usually stored at
`~/.ssh/config`) and using that as your -e flag. The internet can tell you
more about that.

## CRON jobs

There are many repeated actions that need to happen all the time in business.
Some examples:

* Everynight, go to the database of "today's sales" and move them into the
"long-term storage database"
* Prepare a weekly report by querying the database in the same way every week
* Do model/code testing on a regular interval to make sure the model is
responding as expected.

To handle this, the command line has a tool called CRON which allows us to
schedule when something should happen. 

So let's imagine we wanted to download data and clean it every day, I could
create a script called, `job_manager.sh` that does this:

```bash
bash load_data_batches.sh
bash clean_data.sh
```

Then I can do to my terminal and ask it to load the cron scheduler like so:

```bash
crontab -e
```

This will open a vim editor where I can specify my job using the following
syntax.

![CRON Scheduler
Method](https://smhttp-nex.nexcesscdn.net/803313/static/images/blog/2014-01-30/cron-job.png)

So inside my editor I might put

```bash
59 23 * * * job_manager.sh
```

Where the stars mean "don't specify on this." So this would work at 23:59,
every day, of every month and would run the `job_manager.sh` script we just
wrote.

You can see a more thorough discussion here: https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800

## The `find` command

`find` is great for identifying lots of specific things about a file. For
instance, what if I want to look through a bunch of files and find only the
ones that have changed in the last 10 days? Not easy to do with `ls` or other tools. `find`
has that as a built in method though. Let's see.

```bash
find ./folder_name/*  -type f -mtime +9 -print
```

This checks all the files inside of `folder_name` if they are not directories
(`-type f`) and if their last moodified time is more than 9 days `-mtime +9`
and then prints them. You can chain this with other things and modify just
those files that pass this find command using a pipe. So for instance if I
want to find files older than 9 days that contain the word "steve":

```bash
find ./folder_name/*  -type f -mtime +9 | grep "steve"
```

`find` also allows you to check things like file size, check to see if a file
is inside of any of the folders in this directory, use regex file name
matching, and many other things. It's a powerful tool that regularly
outperforms most OS file searches.

## Running things in the background

I often find myself in need of running the same script on many different
datasets. When I want to do that, I often rely on background execution.
Normally when I want to run a python job I just do this:

```bash
python my_script.py
```

That works, but it seizes the terminal until it's done running. I don't want
that, because I want to launch lots of jobs. So what I can do instead is this
(where I'm assuming my python script will allow the argument that points to
the data file to process):

```bash
python my_script.py data_to_process.txt > logFile.txt &
```

The arrow pushes the output into a log file, and the `&` says, "run this
process, but don't seize my terminal... just make it a background thing." Now,
I don't want to do this when I'm testing things, because it's harder to see if
the process is crashing or not, and to kill it if it gets stuck in a loop.
However, when I'm ready to actually run the job, this spawns the process and
puts it in the background to run. I can see it by checking things like:

```bash
ps -ef | grep python
```

which will show me all of the processes that are running that have python in
the name. 

So if I want to run over a bunch of files I could do something like a bash
script:

```bash
#!/bin/bash

for filename in $( ls data{0..10}.txt );
do
  python my_script.py $filename > $filename_log.txt &
done
```

This will run all of the data through the script in individual processes that
don't have to run sequentially, because they are all allowed to spawn as
individual processes. They will then claim resources as they come available
and run themselves, writing out their log files to the logs I've specified.
It's a great way to do batch processing. The `screen` command can also be used
for this.  It's less ideal because it involves a lot of simulating tabs and
  is messier, but some people do that.


## General Discussion of when I use the command line

I'm a command line junkie. I love it. It's super fast, doesn't have all the
overhead of Python or compilation of C++. It's great. That said, it does have
its limits. So these are some examples of when I tend to use command
line/BASH scripts:

* The task involves manipulating a lot of files
* The task involves changing the same thing over and over in a file, so `sed`
will work well
* I want to repeat the same job many times, so I write a BASH script
* I want to put chains of things together, so do X, then when X finishes do Y,
then when Y finishes do Z... I can use a bash script to manage those
processes.
* I want to do hyperspecific file finding/manipulation
* I want to check out what's inside of a file without having to load the whole
thing
* I write a log file and use `tail -f` to have the log file print to my screen
in real time
* I want to talk to a database, but don't want to have all of the overhead of
loading up the full version of python or `psql`
* I want to launch a bunch of jobs independently, so "run a python job on each
of these files." I then use a bash script to start a python instance on each
one.

# Other cool command line tools I didn't mention yet

* [Screen](https://www.gnu.org/software/screen/manual/screen.html)
* [awk](https://linux.die.net/man/1/awk)
* [time](https://linux.die.net/man/1/time)
* [ifconfig](https://en.wikipedia.org/wiki/Ifconfig)
* [du](https://linux.die.net/man/1/du)
* [df](https://linux.die.net/man/1/df)
* The things here: https://www.tecmint.com/useful-linux-commands-for-newbies/


# There's now a whole book on this with a free access page!

https://www.datascienceatthecommandline.com/
