[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Strange Problem with Fujitsu 6.1 Command Shell

_8 messages · 4 participants · 2001-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Strange Problem with Fujitsu 6.1 Command Shell

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-07-20T02:51:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com>`

```
Good evening,

I've written a Fujitsu PowerCOBOL 6.1 program that seems to be having a
rather strange problem and I'm wondering if anyone else has run into
something like this.  The program is running under NT 4.0 service pack 5.
And I really don't expect the problem to be with Fujitsu per se, but I'm
kind of lost at the moment, so we'll start there.

The program basically uses the timer control and every 60 seconds it looks
for a file on our mainframe using a mapped drive to the mainframe and the
CBL_CHECK_FILE_EXIST library routine.

If it sees that the file is present, it reformats the file into what the
customer requires and calls a ftp batch command via the "INVOKE CmDDE1
Execute  USING  Command-Line" option which sends the file to the appropriate
server based on a table file that is read in at beginning of job.

We never know how many files per day we are going to process, so some days
it could be 10 and some days it could be 30.  But the hard part is, some
days everything works fine and some days it doesn't.  I can't really get a
handle on if it's only on busy days that this happens.  It really seems to
be purely random, but as a long, long time programmer, deep inside, I know
better.  Sometimes, the "cmd.exe" prompt stays on the task bar, never closes
out and never FTP's the file.  However, if I exit the PowerCOBOL program and
restart it, it usually runs just fine and FTP's all files.

I'm suspecting a memory leak or a stack file problem that goes away when I
restart the program, but how in the heck can I:

a. Trace what is going on?
b. Fix the problem once I figure out what it is, especially if it's a stack
problem and NT doesn't do stacks?

I love these intermittent problems.  That's part of the reason I have so
much gray hair!!!

Thanks in advance,

Denny
```

#### ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-07-20T21:17:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com>`

```
Can't help with your immediate problem, but for sure you should use:

CBL_CHECK_FILE_EXIST2

which handles imbedded spaces in the directory names.

The other trick we've tried in situations similar is to have the
program write a brief note as to what it's doing to a log file.

Good luck.




"Denny Brouse" <denden@prodigy.net> wrote in message
news:d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com...
> Good evening,
>
> I've written a Fujitsu PowerCOBOL 6.1 program that seems to be
having a
> rather strange problem and I'm wondering if anyone else has run into
> something like this.  The program is running under NT 4.0 service
pack 5.
> And I really don't expect the problem to be with Fujitsu per se, but
I'm
> kind of lost at the moment, so we'll start there.
>
> The program basically uses the timer control and every 60 seconds it
looks
> for a file on our mainframe using a mapped drive to the mainframe
and the
> CBL_CHECK_FILE_EXIST library routine.
>
> If it sees that the file is present, it reformats the file into what
the
> customer requires and calls a ftp batch command via the "INVOKE
CmDDE1
> Execute  USING  Command-Line" option which sends the file to the
appropriate
> server based on a table file that is read in at beginning of job.
>
> We never know how many files per day we are going to process, so
some days
> it could be 10 and some days it could be 30.  But the hard part is,
some
> days everything works fine and some days it doesn't.  I can't really
get a
> handle on if it's only on busy days that this happens.  It really
seems to
> be purely random, but as a long, long time programmer, deep inside,
I know
> better.  Sometimes, the "cmd.exe" prompt stays on the task bar,
never closes
> out and never FTP's the file.  However, if I exit the PowerCOBOL
program and
> restart it, it usually runs just fine and FTP's all files.
>
> I'm suspecting a memory leak or a stack file problem that goes away
when I
> restart the program, but how in the heck can I:
>
> a. Trace what is going on?
> b. Fix the problem once I figure out what it is, especially if it's
a stack
> problem and NT doesn't do stacks?
>
> I love these intermittent problems.  That's part of the reason I
have so
> much gray hair!!!
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-07-24T01:32:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Qe477.385$G_4.65866988@newssvr17.news.prodigy.com>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com> <Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net>`

```
Jerry,

We've kept all directory file names space free.  We are writing out a log
file that indicates that the "file exist" part of the software is working
OK.  The shell part is the part that is "iffy".

I really appreciate your input!!

Denny

"Jerry P" <jerryp@bisusa.com> wrote in message
news:Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net...
> Can't help with your immediate problem, but for sure you should use:
>
…[75 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-07-24T02:18:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jW477.9174$Px1.1048793@newsread2.prod.itd.earthlink.net>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com> <Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net> <Qe477.385$G_4.65866988@newssvr17.news.prodigy.com>`

```

"Denny Brouse" <denden@prodigy.net> wrote in message
news:Qe477.385$G_4.65866988@newssvr17.news.prodigy.com...
> Jerry,
>
> We've kept all directory file names space free.

I'm sure you do. We do too! Windows itself uses imbedded spaces in
some folders ("Program Files," "Temporary Internet Files," etc.) and
in some filenames. We can't always anticipate or control these uses -
such as the Get Temp Directory API.

Further, we've found that some users can get awfully frisky if given
an opportunity to name something ("The Melancholy House Of
Usher.DAT").

So, what the heck, it don't cost us any more to use the more robust
command.
```

###### ↳ ↳ ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-07-24T15:39:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VEg77.5278$ar1.13938@www.newsranger.com>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com> <Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net> <Qe477.385$G_4.65866988@newssvr17.news.prodigy.com>`

```
I sent Denny some code for ShellExecute.  Hopefully it will be more reliable.


In article <Qe477.385$G_4.65866988@newssvr17.news.prodigy.com>, Denny Brouse
says...
>
>Jerry,
…[90 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

_(reply depth: 4)_

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-07-25T00:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OEo77.1805$Co5.329052337@newssvr17.news.prodigy.com>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com> <Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net> <Qe477.385$G_4.65866988@newssvr17.news.prodigy.com> <VEg77.5278$ar1.13938@www.newsranger.com>`

```
Thane,

I won't be able to compile your code into the program and test it until
Friday, but with all the result codes your routine offers, even if it
doesn't work, it looks like I could get a much better handle on what
problems are occurring.

My last conversion from MF COBOL to Fujitsu is a program that does the same
"File Exist" routine, but when it sees a file, it automatically "prints" the
file to Winfax Pro using DDE, which in turn, automatically faxes the file to
the customer.  So if I can get a handle on this situation here, I'll feel
much more comfortable with the fax program.

Thanks very much for allowing me to use the code.  I'll post back the
results once I get it into production.  It's hard for me to duplicate the
situation in testing.

Denny
```

###### ↳ ↳ ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

_(reply depth: 5)_

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-07-25T03:50:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tlr77.6059$ar1.18209@www.newsranger.com>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com> <Dd167.1368$Px1.146551@newsread2.prod.itd.earthlink.net> <Qe477.385$G_4.65866988@newssvr17.news.prodigy.com> <VEg77.5278$ar1.13938@www.newsranger.com> <OEo77.1805$Co5.329052337@newssvr17.news.prodigy.com>`

```
Thanks for the update Denny.  I'll be anxious to hear how you make out.


In article <OEo77.1805$Co5.329052337@newssvr17.news.prodigy.com>, Denny Brouse
says...
>
>Thane,
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Strange Problem with Fujitsu 6.1 Command Shell

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-07-21T01:28:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jaed1$t8p$1@newsg2.svr.pol.co.uk>`
- **References:** `<d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com>`

```
Could it be that you are trying to process the file from the windows side
while it is still being processed by the mainframe ?

"Denny Brouse" <denden@prodigy.net> wrote in message
news:d1N57.2427$DC3.337563825@newssvr17.news.prodigy.com...
> Good evening,
>
…[12 more quoted lines elided]…
> Execute  USING  Command-Line" option which sends the file to the
appropriate
> server based on a table file that is read in at beginning of job.
>
…[5 more quoted lines elided]…
> better.  Sometimes, the "cmd.exe" prompt stays on the task bar, never
closes
> out and never FTP's the file.  However, if I exit the PowerCOBOL program
and
> restart it, it usually runs just fine and FTP's all files.
>
…[4 more quoted lines elided]…
> b. Fix the problem once I figure out what it is, especially if it's a
stack
> problem and NT doesn't do stacks?
>
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
