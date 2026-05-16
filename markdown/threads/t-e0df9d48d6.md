[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# running rm cobol in a cron job

_18 messages · 7 participants · 2006-11 → 2007-01_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Compilers and vendors`](../topics.md#compilers)

---

### running rm cobol in a cron job

- **From:** lbaker@sboa.in.gov
- **Date:** 2006-11-30T06:49:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`

```
I have RM Cobol 7.1 running with Flexgen on AIX 4.2.1.  I have the
following bat file that I have scheduled to run in the cron at a
certain time of day.

RUNPATH=/flextmp/fg4:/flextmp/fg4/fg4bin:
export RUNPATH
TERM=vt100
export TERM
runcobol REP-WEB3.COB K
ftp -n ftppublish.ai.org </flextmp/fg4/ftpweb2.txt
rm /flextmp/fg4/repweb.txt

When I run this bat file logged in as root on the system terminal, it
runs without any errors or problems.  After it runs from the cron job,
it doesn't work and I got this error message in the root mail:

Window Manager not loaded, window status: 305

then it displays some cobol errors,

Cobol I/O error 10 at line 7639 in FG4-WIO, .....

Does anyone have any idea what this means or why if runs fine manually,
but not from the cron?

Thank you.
```

#### ↳ Re: running rm cobol in a cron job

- **From:** Donald Tees <donald_tees@donald-tees.ca>
- **Date:** 2006-11-30T10:03:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ekmrs5$t82$1@aioe.org>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`

```
When you run it manually, are you running it from a terminal, or from 
something like KDE?  It sounds to me like it needs to be run from a GUI 
terminal lke Konsol or RXvt. Note that this is a WAG, I do not use RM 
Cobol under Linux.

Donald
```

##### ↳ ↳ Re: running rm cobol in a cron job

- **From:** lbaker@sboa.in.gov
- **Date:** 2006-11-30T08:48:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1164905323.503690.256700@n67g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<ekmrs5$t82$1@aioe.org>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org>`

```
I am running it from a dumb terminal.

I don't know why it would need GUI to run a job overnight.

Donald Tees wrote:
> When you run it manually, are you running it from a terminal, or from
> something like KDE?  It sounds to me like it needs to be run from a GUI
…[3 more quoted lines elided]…
> Donald
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

- **From:** "P. Raulerson" <paul.rl@raulersons.com>
- **Date:** 2006-11-30T23:25:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Zfch.3601$Ka4.666@newsfe14.lga>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com>`

```
It may not need a graphical terminal, but it does indeed need a terminal, 
which I am afraid you do not have from Cron. You might want to check with 
Liant to see if you can just do something like redirect STDOUT and STDERR 
and get it to work the way you wish.

-Paul

<lbaker@sboa.in.gov> wrote in message 
news:1164905323.503690.256700@n67g2000cwd.googlegroups.com...
>I am running it from a dumb terminal.
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 4)_

- **From:** lbaker@sboa.in.gov
- **Date:** 2006-12-05T05:40:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1165326029.921510.115510@80g2000cwy.googlegroups.com>`
- **In-Reply-To:** `<3Zfch.3601$Ka4.666@newsfe14.lga>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga>`

```
Thanks for the suggestions.  I will check on some of these things.

Linda
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 4)_

- **From:** lbaker@sboa.in.gov
- **Date:** 2006-12-21T11:49:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166730595.744395.186620@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3Zfch.3601$Ka4.666@newsfe14.lga>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga>`

```
I would like the batch file below to run automatically in a cron job.
When I am logged in and run it, without the >all.out 2>error.out, it
displays the message that I normally see that the report is sorting and
works fine.  But it was not working in the cron overnight.  When I
added the >all.out and 2>error.out and run it when I am logged in, it
runs for a while and nothing happens.  I hit CTRL-C to cancel it and in
the all.out file, I get

Window Status: 305
 Window Manager not Loaded

and in the error.out file, I get

COBOL operator requested termination at line 7639 in FG4-WIO
(/flextmp/fg4/fg4bin/FG4-WIO.COB) compiled 2001/07/27 11:34:15.
COBOL traceback at line 1277 in REP-WEB3.COB
(/flextmp/fg4/REP-WEB3.COB)
compiled 2006/11/17 17:08:32

Does anyone know what else I need or what I am doing wrong?

Thanks.

RUNPATH=/flextmp/fg4:/flextmp/fg4/fg4bin:
export RUNPATH
TERM=vt100
export TERM
runcobol REP-WEB3.COB >all.out 2>error.out K
ftp -n ftppublish.ai.org </flextmp/fg4/ftpweb2.txt
rm /flextmp/fg4/repweb.txt


P. Raulerson wrote:
> It may not need a graphical terminal, but it does indeed need a terminal,
> which I am afraid you do not have from Cron. You might want to check with
…[18 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-12-21T13:59:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166738367.048452.219850@42g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<1166730595.744395.186620@i12g2000cwa.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com>`

```

lbaker@sboa.in.gov wrote:
> I would like the batch file below to run automatically in a cron job.
> When I am logged in and run it, without the >all.out 2>error.out, it
> displays the message that I normally see that the report is sorting and
> works fine.

> RUNPATH=/flextmp/fg4:/flextmp/fg4/fg4bin:
> export RUNPATH
…[4 more quoted lines elided]…
> rm /flextmp/fg4/repweb.txt

In a cron job almost nothing is set for you. It may be the PATH or some
other that you require, or it may be that all you need is a cd to the
correct directory.

Try logging in an do a: set >logged.set

add to the cron job: set >cron.set

and then compare them adding differences to the cron until the problem
is fixed.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 6)_

- **From:** lbaker@sboa.in.gov
- **Date:** 2006-12-22T07:29:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166801380.556896.171300@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1166738367.048452.219850@42g2000cwt.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com>`

```
I changed my bat file to this:

TERM=vt100
export TERM
PATH=./:/usr/ucb:/bin:/usr/bin:/usr/local/bin:/usr/sbin:/usr/lpp/X11/bin:/usr/rn
RUNPATH=/flextmp/fg4:/flextmp/fg4/fg4bin:
export PATH RUNPATH
export ENV=$HOME/.kshrc
set -o vi
set >cron.set
runcobol REP-WEB3.COB K
ftp -n ftppublish.ai.org </flextmp/fg4/ftpweb2.txt
rm /flextmp/fg4/repweb.txt

When it runs, I get this error in the root mail and there is not a
cron.set file to check:

Window Status: 305
 Window Manager not Loaded

COBOL I/O error 10 at line 7639 in FG4-WIO
(/flextmp/fg4/fg4bin/FG4-WIO.COB)
compiled 2001/07/27 11:34:15.
COBOL traceback at line 1277 in REP-WEB3.COB
(/flextmp/fg4/REP-WEB3.COB)
compiled 2006/11/17 17:08:32.repweb.txt: A file or directory in the
path name d.
Local directory now /flextmp/fg4
rm: /flextmp/fg4/repweb.txt: A file or directory in the path name does
not exis.

Thanks.

Richard wrote:
> lbaker@sboa.in.gov wrote:
> > I would like the batch file below to run automatically in a cron job.
…[21 more quoted lines elided]…
> is fixed.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-12-22T11:57:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166817451.745364.167460@42g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<1166801380.556896.171300@i12g2000cwa.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com> <1166801380.556896.171300@i12g2000cwa.googlegroups.com>`

```

lbaker@sboa.in.gov wrote:

> When it runs, I get this error in the root mail and there is not a
> cron.set file to check:

So the cron job is in the root user ?  You will probably find cron.set
in the root user's home directory. You may also find that $HOME is not
an appropriate setting.

Why aren't you running this cron under your normal user ?

> Local directory now /flextmp/fg4

That implies that the program changed it.  Running cron as user may
help but also do a specific cd to this before starting the program.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 8)_

- **From:** lbaker@sboa.in.gov
- **Date:** 2007-01-02T11:14:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167765259.046830.63520@a3g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1166817451.745364.167460@42g2000cwt.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com> <1166801380.556896.171300@i12g2000cwa.googlegroups.com> <1166817451.745364.167460@42g2000cwt.googlegroups.com>`

```
I assume the root user is runing the cron.  How do you run a cron job
under your normal user?

Richard wrote:
> lbaker@sboa.in.gov wrote:
>
…[12 more quoted lines elided]…
> help but also do a specific cd to this before starting the program.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-01-02T11:43:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167767002.713744.54100@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<1167765259.046830.63520@a3g2000cwd.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com> <1166801380.556896.171300@i12g2000cwa.googlegroups.com> <1166817451.745364.167460@42g2000cwt.googlegroups.com> <1167765259.046830.63520@a3g2000cwd.googlegroups.com>`

```

lbaker@sboa.in.gov wrote:
> I assume the root user is runing the cron.  How do you run a cron job
> under your normal user?

What I do is log in as required user and run 'crontab -e' to
create/edit the cron file. You may need to edit the cron file
separately and then 'crontab filename' while logged in as the user.

See your system's documentation, or 'man crontab'.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 10)_

- **From:** lbaker@sboa.in.gov
- **Date:** 2007-01-02T11:59:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167767940.110530.108800@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<1167767002.713744.54100@v33g2000cwv.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com> <1166801380.556896.171300@i12g2000cwa.googlegroups.com> <1166817451.745364.167460@42g2000cwt.googlegroups.com> <1167765259.046830.63520@a3g2000cwd.googlegroups.com> <1167767002.713744.54100@v33g2000cwv.googlegroups.com>`

```
So are you saying that whatever user you are logged in as when you edit
the cron tab file is the one that is logged in when it runs the job?

I didn't know that.

I will try editing the crontab logged in as my normal user and see if
that makes any difference.

thanks.

Richard wrote:
> lbaker@sboa.in.gov wrote:
> > I assume the root user is runing the cron.  How do you run a cron job
…[6 more quoted lines elided]…
> See your system's documentation, or 'man crontab'.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-01-02T15:45:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167781532.778535.171290@k21g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1167767940.110530.108800@v33g2000cwv.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com> <1166738367.048452.219850@42g2000cwt.googlegroups.com> <1166801380.556896.171300@i12g2000cwa.googlegroups.com> <1166817451.745364.167460@42g2000cwt.googlegroups.com> <1167765259.046830.63520@a3g2000cwd.googlegroups.com> <1167767002.713744.54100@v33g2000cwv.googlegroups.com> <1167767940.110530.108800@v33g2000cwv.googlegroups.com>`

```

lbaker@sboa.in.gov wrote:

> So are you saying that whatever user you are logged in as when you edit
> the cron tab file is the one that is logged in when it runs the job?

Actually each user has their own cron file, at least on Linux and
UnixWare it does. The actual cron files are in /var/spool/cron/ with a
file for each user.

> I will try editing the crontab logged in as my normal user and see if
> that makes any difference.

You won't edit *the* crontab, you will need to create a new one for
that user and edit the root cron file to remove lines.
```

###### ↳ ↳ ↳ Re: running rm cobol in a cron job

_(reply depth: 5)_

- **From:** "P. Raulerson" <paul.rl@raulersons.com>
- **Date:** 2006-12-22T18:38:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6U_ih.20$923.5@newsfe17.lga>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <ekmrs5$t82$1@aioe.org> <1164905323.503690.256700@n67g2000cwd.googlegroups.com> <3Zfch.3601$Ka4.666@newsfe14.lga> <1166730595.744395.186620@i12g2000cwa.googlegroups.com>`

```
Ah-- that WIO error indicates that your program is trying to open a window 
to do some I/O to. I believe in particular, that is a GUI window.

Check your program and make sure you are not writing to anything but 
standard in and standard out.

-Paul

<lbaker@sboa.in.gov> wrote in message 
news:1166730595.744395.186620@i12g2000cwa.googlegroups.com...
>I would like the batch file below to run automatically in a cron job.
> When I am logged in and run it, without the >all.out 2>error.out, it
…[53 more quoted lines elided]…
>
```

#### ↳ Re: running rm cobol in a cron job

- **From:** NotSure <bodieblue27@YAHOO.COM>
- **Date:** 2006-12-01T13:05:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<is90n2t06m5253aaquirbtangibopi6sln@4ax.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`

```
On 30 Nov 2006 06:49:10 -0800, lbaker@sboa.in.gov wrote:

>I have RM Cobol 7.1 running with Flexgen on AIX 4.2.1.  I have the
>following bat file that I have scheduled to run in the cron at a
…[23 more quoted lines elided]…
>Thank you.

The I/O error 10 suggests that a read is not finding a file it
expects.

Are you sure you are setting _all_ the environmental variables in the
batch file as are set when you log into a dumb terminal?  Perhaps a
path to a configuration file or some such?
```

#### ↳ Re: running rm cobol in a cron job

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2006-12-02T15:41:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccmdnUdpfb5aA-zYRVnytg@pipex.net>`
- **In-Reply-To:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`

```
Top post.

Cron jobs need extra work to ensure the environment is set as 
you want it - typically, I think, you get pretty well nothing 
set up - no .profile, .login or whatever doing it as for a 
'manual' user.

Hope that helps.

Michael

lbaker@sboa.in.gov wrote:
> I have RM Cobol 7.1 running with Flexgen on AIX 4.2.1.  I have the
> following bat file that I have scheduled to run in the cron at a
…[24 more quoted lines elided]…
>
```

#### ↳ Re: running rm cobol in a cron job

- **From:** "RobH" <r.heady-no-spam@liant.com>
- **Date:** 2006-12-27T20:26:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GFAkh.2785$sR.1968@newssvr29.news.prodigy.net>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com>`

```

<lbaker@sboa.in.gov> wrote in message 
news:1164898150.541415.57560@l12g2000cwl.googlegroups.com...
>I have RM Cobol 7.1 running with Flexgen on AIX 4.2.1.  I have the
> following bat file that I have scheduled to run in the cron at a
…[24 more quoted lines elided]…
>

My best guess is that the terminal database that you are using does not 
contain enough information to display a pop-up window.  I see where you are 
setting the TERM=vt100 but I don't think that is what you are really 
getting.  Perhaps it cannot find the terminfo database.  For an experiment, 
set your RUNPATH and then set TERM=dumb and run the program from the command 
line.  I'll bet you get the same "Window Manager not loaded" error.

Is there an ACCEPT statement at line 7639 in FG4-WIO?  My guess is that this 
code is probably getting executed because of the 305 Window status.

Hope this helps.

Robert Heady
Liant Software Corp.
```

##### ↳ ↳ Re: running rm cobol in a cron job

- **From:** lbaker@sboa.in.gov
- **Date:** 2007-01-02T11:04:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167764691.967890.139850@h40g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<GFAkh.2785$sR.1968@newssvr29.news.prodigy.net>`
- **References:** `<1164898150.541415.57560@l12g2000cwl.googlegroups.com> <GFAkh.2785$sR.1968@newssvr29.news.prodigy.net>`

```
I was getting a different error before I put the TERM=vt100 in.

I am using the Flexgen cobol generator, so I just have a simple program
in flexgen using the LIST command to print a report and then I send the
output to a file
(MOVE "F" TO LST--PRTMOD.) instead of a printer.  I have used the
SUPRESS command to suppress the window which says in the manual that it
suppress the run window to produce a batch output with no operator
input.  So I am not sure what commands are at those different line
numbers since the flexgen has created the COBOL automatically.

When I run the program manually from Unix, it does display a message
(the same as when I run it from Flexgen directly), that says "Report in
Progress" or something like that.  I am wondering if that is what it is
trying to display and if I could suppress that from displaying if that
would correct the problem.  I thought the SUPPRESS WINDOW command would
cause it to not display, but it dosn't seem to make any difference.

If there is not a way to suppress that from displaying, then I guess I
do need to do something such as a different terminal type to get it to
work.

Someone else mentioned logging in as another user to run the cron job,
but I don't know how to do that either.  I assume when the cron runs it
is logged in as root.

I thought this would be a common thing to do (run an automated job) and
I didn't think it would be this difficult to get it to work.

Thanks.

Linda

RobH wrote:
> >
>
…[13 more quoted lines elided]…
> Liant Software Corp.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
