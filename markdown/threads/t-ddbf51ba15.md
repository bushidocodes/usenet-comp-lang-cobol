[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call compiler from within an application?

_19 messages · 10 participants · 2005-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Call compiler from within an application?

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-01-11T12:32:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`

```
I know that from with a COBOL app, you can use something like:

CALL "SYSTEM" USING Z"cob ..."

I know its out there, but I am wondering if its even possible, does
anyone knows of a way for a cobol application to directly invoke the
compiler?
```

#### ↳ Re: Call compiler from within an application?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-11T23:25:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zfZEd.596656$lR6.94764@news.easynews.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`

```
Probably possible.  What compiler?  What operating system?
```

#### ↳ Re: Call compiler from within an application?

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-01-11T18:06:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41E469EE.AFDB2564@mb.sympatico.ca>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`

```
Chris wrote:
> 
> I know that from with a COBOL app, you can use something like:
…[5 more quoted lines elided]…
> compiler?

I don't know about Cobol, but my experiences with PROGRESS, which does
allow compile-on-the-fly, lead me to believe that there is never a case
where this is a good idea.



PL
```

#### ↳ Re: Call compiler from within an application?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-11T19:09:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105499381.483979.119210@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`

```
> CALL "SYSTEM" USING Z"cob ..."

> I know its out there, but I am wondering if its even possible, does
> anyone knows of a way for a cobol application to directly invoke the
> compiler?

What would be different between your example invoking 'cob' (the
compiler) and 'directly invoking the compiler' ?

Were you wanting a program to get itself recompiled in a way that then
carried on in the newly recompiled version ?
```

##### ↳ ↳ Re: Call compiler from within an application?

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-01-12T17:52:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iLiFd.678$813.397@fe40.usenetserver.com>`
- **In-Reply-To:** `<1105499381.483979.119210@z14g2000cwz.googlegroups.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105499381.483979.119210@z14g2000cwz.googlegroups.com>`

```
Richard wrote:
>>CALL "SYSTEM" USING Z"cob ..."
> 
…[10 more quoted lines elided]…
> carried on in the newly recompiled version ?

It could be a COBOL program that's part of a CM system, and is 
responsible for kicking off compiles for other programs.  I wrote one 
for ours at work that checks the listing for errors, and if it doesn't 
find any, moves the new executable around to where it needs to be.

There was one process that we couldn't do from within the program, so 
the program writes a sequence of commands to a file, "add"s it to the 
run (which means it starts executing when this program stops), and 
finishes.  The last statement in the file re-executes the checker to 
check that final process.

That may not be what he's trying to do - but, I could see a need for a 
COBOL program to invoke it's compiler.  :)
```

#### ↳ Re: Call compiler from within an application?

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-01-12T07:32:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105543930.201422.14130@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com>`

```
Sorry for not providing the usual details: HP-UX 11i & MF Server
Express 4.0 SP1

Also, I'm not trying to recompile the running program, I'm attempting
to write an application that will have the ability to "build" other
applications on the fly. The only reason for asking whether or not I
could invoke the compiler from within the rts is simply because I felt
that it would provide me with the easiest method of obtaining the
feedback.

I know I could parse the results of a SYSTEM call or an input pipe
file, but that seems tedious and gives me no way to interrogate the
return status of the compile command itself.

In all actuality, I'll probably end up using the SYSTEM call, since I
would then be able to "build" applications other than COBOL from with
the MF rts. I was more curious if anyone had ever been able to
accomplish this before.

Thanks again for the responses - this is a very bright group of
individuals.
```

##### ↳ ↳ Re: Call compiler from within an application?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-12T08:59:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105549153.881172.280160@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1105543930.201422.14130@f14g2000cwb.googlegroups.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com>`

```
> I know I could parse the results of a SYSTEM call or an input pipe
> file, but that seems tedious and gives me no way to interrogate the
> return status of the compile command itself.

I suspect that 'cob' is written in Cobol, much of the MF compiler suite
is. So it should be possible to call the compiler and get the result,
but then you may never know what this result actually means.

I would have thought that using some sort of 'make' would be more
useful than writing your own.  One of the dependent actions could be to
signal somehow that it completed correctly.

eg:

YourProgram:
writes makefile
writes resultfile with 'failed' in it
call "SYSTEM" using z"make ...."
reads resultfile
if result-record = 'failed'
.....

Makefile:
prog: prog.cbl ....
cob ... prog.cbl ...
echo "success" > resultfile

if 'cob' fails then it should not run echo.

Alternately delete the executable before call "SYSTEM" ... and see if
one exists after then it worked.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

- **From:** "Simon Tobias" <Simon.Tobias@microfocus.com>
- **Date:** 2005-01-12T17:19:10
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs3mra$95q$1@hyperion.microfocus.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <1105549153.881172.280160@z14g2000cwz.googlegroups.com>`

```
Chris,

It's probably best if you either post directly to the Micro Focus forum
under http://www.cobolportal.com or contact Micro Focus SupportLine
directly.

Cob -- which isn't COBOL, by the way -- will return a zero return-code is
the compilation is successful, so I would *assume* that the return-code will
trickle back down from a CALL "SYSTEM" to the calling COBOL app.

SimonT.
```

##### ↳ ↳ Re: Call compiler from within an application?

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-12T18:54:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com>`

```
On 12 Jan 2005 07:32:10 -0800, "Chris" <ctaliercio@yahoo.com> wrote:

>Sorry for not providing the usual details: HP-UX 11i & MF Server
>Express 4.0 SP1
…[15 more quoted lines elided]…
>accomplish this before.

Call SYSTEM to run a script containing two entries: make followed by
export rc=$?
Then you can interrogate rc to get the compiler's return code.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-12T11:24:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105557849.144740.145520@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com>`

```
> Call SYSTEM to run a script containing two entries: make followed by
> export rc=$?
> Then you can interrogate rc to get the compiler's return code.

No, you cannot do that, it will not and does not work.

The 'system' call creates a new shell below the current one.  Any
'export' only changes what is in that new shell and this is destroyed
before the 'system' returns to the program.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 4)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-13T10:32:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com>`

```
On 12 Jan 2005 11:24:09 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> Call SYSTEM to run a script containing two entries: make followed by
>> export rc=$?
…[6 more quoted lines elided]…
>before the 'system' returns to the program.

It can be easily tested. At a Unix prompt, type:

ksh
export test=xyz
exit
echo $test

I'd post the result if I had access to a Unix machine.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-13T07:33:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs5pqb$4c5$1@panix5.panix.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`

```
In article <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 12 Jan 2005 11:24:09 -0800, "Richard" <riplin@Azonic.co.nz> wrote:
>
…[17 more quoted lines elided]…
>I'd post the result if I had access to a Unix machine.

panix5:[/net/u/1/d/docdwarf] ksh
$ export test=xyz
$ exit
panix5:[/net/u/1/d/docdwarf] echo $test
test: Undefined variable.
panix5:[/net/u/1/d/docdwarf]

DD
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 6)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-13T15:02:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qc3du0hkbdfusmoqthdknu5nratgj2qvhe@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com> <cs5pqb$4c5$1@panix5.panix.com>`

```
On 13 Jan 2005 07:33:15 -0500, docdwarf@panix.com wrote:

>In article <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>,
>Robert Wagner  <spamblocker-robert@wagner.net> wrote:
…[26 more quoted lines elided]…
>panix5:[/net/u/1/d/docdwarf]

Thank you. 

I could swear on a stack of manuals I've done it many times.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-13T10:59:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs65ti$lo1$1@panix5.panix.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com> <cs5pqb$4c5$1@panix5.panix.com> <qc3du0hkbdfusmoqthdknu5nratgj2qvhe@4ax.com>`

```
In article <qc3du0hkbdfusmoqthdknu5nratgj2qvhe@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 13 Jan 2005 07:33:15 -0500, docdwarf@panix.com wrote:
>
…[32 more quoted lines elided]…
>I could swear on a stack of manuals I've done it many times. 

That might show the value of your oath, Mr Wagner, when compared with an 
experiment.

DD
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-13T11:35:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105644928.943779.254630@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<qc3du0hkbdfusmoqthdknu5nratgj2qvhe@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com> <cs5pqb$4c5$1@panix5.panix.com> <qc3du0hkbdfusmoqthdknu5nratgj2qvhe@4ax.com>`

```
> I could swear on a stack of manuals I've done it many times.

Which is probably why you have a reputation of being a mine of
misinformation.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-13T11:19:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105643972.845696.33660@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`

```
>> No, you cannot do that, it will not and does not work.

>> The 'system' call creates a new shell below the current one. Any
>> 'export' only changes what is in that new shell and this is
destroyed
>> before the 'system' returns to the program.

> It can be easily tested. At a Unix prompt, type:

> ksh

on Linux:
[riplin@Man91 EMail]$ ksh
bash: ksh: command not found

on SCO Unixware:
$ ksh
$ export test=xyz
$ exit
$ echo $test
<- blank
$

I actually tested _before_ I posted by having a Cobol program execute a
script and try to retrieve the result of an export in the script.  It
failed to do so, as I had already predicted from my knowledge of Unix
and shells.

To illustrate how far off the mark you are:

$ test=old
$ ksh
$ export test=xyz
$ echo $test
xyz
$ exit
$ echo $test
old
$

This is _why_ they are called 'shells'.
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-01-13T21:09:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3KGFd.2502$813.2460@fe40.usenetserver.com>`
- **In-Reply-To:** `<9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <lhsau0dgoag96i6ljvtfst62lpb4v7jika@4ax.com> <1105557849.144740.145520@c13g2000cwb.googlegroups.com> <9hjcu05uvr1sbfv7b9hu572rid7kr32uid@4ax.com>`

```
Robert Wagner wrote:
> On 12 Jan 2005 11:24:09 -0800, "Richard" <riplin@Azonic.co.nz> wrote:
> 
…[18 more quoted lines elided]…
> 

And that gets you...

[summersd@daniel summersd]$ ksh
$ export test=xyz
$ exit
[summersd@daniel summersd]$ echo $test

[summersd@daniel summersd]$
```

##### ↳ ↳ Re: Call compiler from within an application?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2005-01-13T00:18:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87jFd.63302$6l.9305@pd7tw2no>`
- **In-Reply-To:** `<1105543930.201422.14130@f14g2000cwb.googlegroups.com>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com>`

```
Chris wrote:

>Sorry for not providing the usual details: HP-UX 11i & MF Server
>Express 4.0 SP1
…[21 more quoted lines elided]…
>
Come on Donald - you are are one who has expressed an interest in 
compiling on the fly. Care to give Chris some of your thoughts 
("expanded") ? Have you had a shot yet with either F/J or M/F ? It's not 
Friday yet, so you aren't into a stogie or fiddling :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Call compiler from within an application?

- **From:** Donald Tees <donald@sympatico.ca>
- **Date:** 2005-01-13T09:34:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UFvFd.30773$b64.919778@news20.bellglobal.com>`
- **In-Reply-To:** `<87jFd.63302$6l.9305@pd7tw2no>`
- **References:** `<1105475559.668451.308500@c13g2000cwb.googlegroups.com> <1105543930.201422.14130@f14g2000cwb.googlegroups.com> <87jFd.63302$6l.9305@pd7tw2no>`

```
James J. Gavan wrote:
> Chris wrote:
> 
…[29 more quoted lines elided]…
> Jimmy, Calgary AB

I cannot see the difference between calling a cobol compiler and calling 
any other application.  A program is a program is a program. You have to 
also call the linker, of course.

As Richard said a post or two back, the easiest way is to call a 
makefile, rather than wading through all the options and stuff.  The FJ 
Gui(PSTAFF) will even write the makefile out for you, based on the project.

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
