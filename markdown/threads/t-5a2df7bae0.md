[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Replacement for JCL on a (Windows) server

_7 messages · 6 participants · 2003-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Replacement for JCL on a (Windows) server

- **From:** "The COBOL Frog" <Huib.Klink.Spam@Blocker.MicroFocus.com>
- **Date:** 2003-07-21T10:08:44+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfg72d$a2h$1@news.hccnet.nl>`

```
I'm involved in migrating a batch application to a Windows 2000
server environment. Now, important part of the deployment was
(on the mainframe) and still will be, of course, Job Control and
a JOB scheduler.

Are there tools available to do these things on a server?
Compose JOBs, schedule, JOB dependencies, triggering, you know
the stuff ...

Any rating what's the best JCL-replacing product?

I would very much appreciate to hear names, web site URL's,
experiences etc.

Thanks, regards,

+------------------------------------------------------+
| H.M. (Huib) Klink  also known as  * The COBOL Frog * |
|------------------------------------------------------|
| Mail me @ the address below, remove the spam blocker |
|------------------------------------------------------|
| Huib.Klink.Spam@Blocker.MicroFocus.com               |
+------------------------------------------------------+

P.S: The app. has been written in COBOL, but I think that's not
so important for this question.
```

#### ↳ Re: Replacement for JCL on a (Windows) server

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-21T21:20:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f1bb0f0_6@news.athenanews.com>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl>`

```
Huib,

all of the behaviour obtained by JCL (and RPFs and REXX) on the mainframe
can be achieved by scripting on the PC. The only thing is that it requires
some different approaches.

It is no good trying to "think mainframe" and "translate" JCL.

You need to "think functional" and this easily translates into equivalent
functions in Windows scripting. It is certainly possible to set up jobs to
run in batch and check condition codes and execute other jobs depending on
what happened...even at the most basic level of Batch Procedures using DOS
commands.

Having said that, there are implementations of REXX that run on the PC...

You need to look at Batch files for the PC and or Windows Scripting (try
MSDN).

Good Luck!

Pete.

"The COBOL Frog" <Huib.Klink.Spam@Blocker.MicroFocus.com> wrote in message
news:bfg72d$a2h$1@news.hccnet.nl...
> I'm involved in migrating a batch application to a Windows 2000
> server environment. Now, important part of the deployment was
…[25 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Replacement for JCL on a (Windows) server

- **From:** "The COBOL Frog" <Huib.Klink.Spam@Blocker.MicroFocus.com>
- **Date:** 2003-07-22T22:11:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfm0g7$c17$1@news.hccnet.nl>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl> <3f1bb0f0_6@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote #
in message news:3f1bb0f0_6@news.athenanews.com...
| Huib,
|
| all of the behaviour obtained by JCL (and RPFs and REXX) on
the mainframe
| can be achieved by scripting on the PC. The only thing is that
it requires
| some different approaches.
|
| It is no good trying to "think mainframe" and "translate" JCL.
|
| You need to "think functional" 8<

  8<.

|
| Good Luck!
…[3 more quoted lines elided]…
| "The COBOL Frog" <Huib.Klink.Spam@Blocker.MicroFocus.com>
wrote in
| message news:bfg72d$a2h$1@news.hccnet.nl...
| > I'm involved in migrating a batch application to a Windows
2000
| > server environment. Now, important part of the deployment
was
| > (on the mainframe) and still will be, of course, Job Control
and
| > a JOB scheduler.
| >
| > Are there tools available to do these things on a server?
| > Compose JOBs, schedule, JOB dependencies, triggering, you
know
| > the stuff ...

  8<

All,

Thanks for all your answers. I summarised all feedback I got
(including
from sources outside CLC) at the bottom of this message.

Pete,

I am fully aware of the need to a mind shift when moving from
one type
of platform to another. Some things that are "usual" or come in
"handy"
have to be done (although functionally still required) in a way
that
applies and is more "at home" on the target platform. It is a
matter
of changing the "how" (i.e. the implementation), not the "what"
(i.e the
functionality). Insofar (is that good English?) I agree with
you.

However, still the "what" remains for this batch app. on the new
Win2K
machine: (1) the need to run "jobs" (related series of programs)
and
(2) the need to schedule these jobs.

Composing jobs can indeed easily and effectively be done via
shell
scripting, in the form of batch files (*.bat or *.cmd, whatever
one
likes). Scheduling however requires some more tooling than is
available
in a Windows OS. Using the native AT command one could schedule
at
times and dates, but job-dependencies are not easily set-up by
AT and
other native DOS-like commands. Running a job (only) when a
previous one
succeeded, another (only) in case the first one abended, firing
a job
at the moment a triggering file is created and closed by a
preceding job
(etc. etc.) is a whole other type of thing. It needs a scheduler
tool /
program that enables to setup such (more or less complex)
schemes of
batches and that enables to execute your jobs as defined.

Of course one could write this myself (in COBOL f.e.) but it's
not
easily done and probably more effective to be bought.

One of my colleagues answered my question by starting of with
the
sentence: "You're right, that is a key area to all IBM migration
tasks".
I believe him, especially when huge mainframe applications have
to be
migrated (batch oriented).

In other words, translating single jobs to scripts
(bat/cmd-files) is
one relatively simple step, but a full-functional scheduling is
still
needed and not that easy made. Better buy, I think.

At last the promised collection of answers I got:

1) - Get the cgywin UNIX compatibility layer and a bash shell.
2) - UC4   - http://www.uc4.com/
3) - TIDAL - http://www.tidalsoft.com/
4) - MKS   - http://www.mkssoftware.com/ (UNIX scripts on
Windows)
5) - "Launchpad" of Cypress Technologies
http://www.cypressnet.com/
6) - Some person mailed me privately (after reading my initial
     question here in CLC):
     "Hi Huib,
      I saw your posting in Comp.Lang.Cobol. We have a parser
that
      converts JCL into MSDos Batch files for one of our
clients.
      It must be ok because they've gone live on it.
      If you want any further details please get in touch."
     Not knowing his reasons not to share this with all of us in
CLC,
     I deliberately left out his name/company here. When he
wants to,
     he'll no doubt post a reply when he reads this.

I shared all this results with our customer. Thank you all.

P.S: I hope 1) my use of 'one' and 'you' is correct and 2) my
     generalizations are no source of huge reply-threads like
others
     recently posted to CLC. Apologies beforehand :))

Regards,

+------------------------------------------------------+
| H.M. (Huib) Klink  also known as  * The COBOL Frog * |
|------------------------------------------------------|
| Mail me @ the address below, remove the spam blocker |
|------------------------------------------------------|
| Huib.Klink.Spam@Blocker.MicroFocus.com               |
+------------------------------------------------------+
```

###### ↳ ↳ ↳ Re: Replacement for JCL on a (Windows) server

- **From:** "JC" <Kaos_Theory99@hotmail.com>
- **Date:** 2003-07-23T18:42:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfmkvh$6ol$1@hercules.btinternet.com>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl> <3f1bb0f0_6@news.athenanews.com> <bfm0g7$c17$1@news.hccnet.nl>`

```
The COBOL Frog <Huib.Klink.Spam@Blocker.MicroFocus.com> wrote in message
news:bfm0g7$c17$1@news.hccnet.nl...
>
> 6) - Some person mailed me privately (after reading my initial
…[13 more quoted lines elided]…
>
Didn't want to be accused of spamming
```

#### ↳ Re: Replacement for JCL on a (Windows) server

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-21T06:18:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhnj1230ktvh44@corp.supernews.com>`
- **In-Reply-To:** `<bfg72d$a2h$1@news.hccnet.nl>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl>`

```
The COBOL Frog wrote:

> I'm involved in migrating a batch application to a Windows 2000
> server environment. Now, important part of the deployment was
…[5 more quoted lines elided]…
> the stuff ...

You've got several options.  You can write a .cmd (.bat) file and 
actually "shell it" (open a command-line shell and start it) - this 
might be the best for dynamic processes.  You can also set up "Scheduled 
Tasks" on the box itself - these are good for your hourly/daily/etc. 
processes.

Depending on what relational database you're using with this product, 
you can write database procedures, and either schedule them on a 
recurring basis, or execute them dynamically through an application program.

> Any rating what's the best JCL-replacing product?

Unless someone knows of an "emulator" or sorts, I'd have to say, for 
Windows 2000 Server, it's DOS.

> I would very much appreciate to hear names, web site URL's,
> experiences etc.

I don't have web sites (although I'm sure http://msdn.microsoft.com is a 
good place to start), but I can share an experience.  One of our 
requirements is to back up the database and web site daily.  On the 1st 
and 15th, we make a special copy that gets burned to CD.  We have a 
batch file that utilizes WinZip's Command-Line interface (WZZIP - free 
to download from http://www.winzip.com ) to ZIP directories of files 
into one file.  This batch file is kicked off by a scheduled task on the 
server.  We also have scheduled database tasks in SQL Server that do the 
actually database backup for us.

There are a lot of automation tools out there by default (I haven't even 
touched on Windows Scripting Host).  You should be able to come up with 
something pretty easily.  :)  Hope that helps...
```

#### ↳ Re: Replacement for JCL on a (Windows) server

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-21T09:18:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-550332.09183921072003@corp.supernews.com>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl>`

```
In article <bfg72d$a2h$1@news.hccnet.nl>,
 "The COBOL Frog" <Huib.Klink.Spam@Blocker.MicroFocus.com> wrote:

> I'm involved in migrating a batch application to a Windows 2000
> server environment. Now, important part of the deployment was
…[23 more quoted lines elided]…
> so important for this question.

The easy answer is to use the DOS shell COMMAND.COM with .bat or .cmd 
files to replace your procs and jobs.

As an alternative, you might want to get your hands on the cgywin unix 
compatibility layer and a bash shell.  It is much more functional so you 
should not lack for JCL work-alike concepts.

You can schedule with the native AT command or buy/build/develop a 
scheduler reasonably easily.
```

#### ↳ Re: Replacement for JCL on a (Windows) server

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-07-21T16:40:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-M-dnXcusPxdwIGiXTWQlg@giganews.com>`
- **References:** `<bfg72d$a2h$1@news.hccnet.nl>`

```
A pretty good scheduler I've used is "Launchpad" from
Cypress Technologies. www.cypressnet.com   It has more
features than the simple Windows task scheduler such as
starting a task based on the presence of a file and many
others. I used it quite a bit on my last job. It worked
flawlessly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
