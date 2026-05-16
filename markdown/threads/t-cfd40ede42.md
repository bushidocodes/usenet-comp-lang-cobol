[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CMD file to compile Cobol

_13 messages · 8 participants · 2007-09_

---

### CMD file to compile Cobol

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-09-16T21:00:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com>`

```
Hello,
This is a CMD file question so why am I here - well I use DOS CMD
files to compile Cobol programs, so I might be safe:-) ?

The short question is 'how does one pass a variable, a return code or
more than one varibale from a call'ed CMD file' back to a parent CMD
file?

More lucidly(?), in a DOS CMD window I submit:

C:\>uexec pgm017 conrad

where the uexec.cmd file looks like: 

stuff
call step1 %1
call step2 %2
more stuff

where step1 and step2 contain a variety of activities such as compile,
translate, Rexx's, If Exist'ses etc), any one of which could go wrong.

So I would like to say after each activity in step1.cmd something
like:
if errorlevel GEQ 1 set errorfl=1; goto abend
if errorlevel GEQ 1 set errorfl=2; goto abend
if errorlevel GEQ 1 set errorfl=3; goto abend

and when returning to master.cmd, my master.cmd might hopefully be
coded as:

stuff
call step1 %1
if errorfl 1 goto step1compile
if errorfl 2 goto step1link
rem if reaching here then master.cmd continues
call step2 %2
if errorfl 1 goto step2rexx1
if errorfl 2 goto step2rexx2
if errorfl 3 goto step2rexx3
more stuff

Any help appreciated. Thanks.
Graham Hobbs
```

#### ↳ Re: CMD file to compile Cobol

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-16T20:13:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13erl3e47h7eqda@news.supernews.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com>`

```
Graham Hobbs wrote:
> Hello,
> This is a CMD file question so why am I here - well I use DOS CMD
…[38 more quoted lines elided]…
> more stuff

Dunno.

How about you take control of the whole enchilada by writing a small file 
with intra-program status/commands. Each program checks the contents and 
does what the contents indicate.
```

##### ↳ ↳ Re: CMD file to compile Cobol

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-17T06:51:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13esqf4l2bjmc9e@news.supernews.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <13erl3e47h7eqda@news.supernews.com>`

```
HeyBub wrote:
>
> Dunno.
…[3 more quoted lines elided]…
> contents and does what the contents indicate.

Disregard this post; I was thinking about the proper number of holes needed 
for a 27" shoelace.
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-17T19:38:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eu3u8hgtl976b@corp.supernews.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <13erl3e47h7eqda@news.supernews.com> <13esqf4l2bjmc9e@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:13esqf4l2bjmc9e@news.supernews.com...
> HeyBub wrote:
>>
…[8 more quoted lines elided]…
>

Don't think about a pink elephant!
```

#### ↳ Re: CMD file to compile Cobol

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T20:53:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com>`

```
On Sun, 16 Sep 2007 21:00:11 -0400, Graham Hobbs <ghobbs@cdpwise.net> wrote:

>Hello,
>This is a CMD file question so why am I here - well I use DOS CMD
…[41 more quoted lines elided]…
>Graham Hobbs

You're doing it the hard way. You should be using MAKE.
```

##### ↳ ↳ Re: CMD file to compile Cobol

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-09-17T13:21:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com>`

```
On Sun, 16 Sep 2007 20:53:51 -0500, Robert <no@e.mail> wrote:

>On Sun, 16 Sep 2007 21:00:11 -0400, Graham Hobbs <ghobbs@cdpwise.net> wrote:
>
…[45 more quoted lines elided]…
>You're doing it the hard way. You should be using MAKE.

In a CMD window I tried MAKE /? and got nothing.
What is MAKE ?
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-17T17:34:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcmdro$ed5$1@reader1.panix.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com> <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com>`

```
In article <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com>,
Graham Hobbs  <ghobbs@cdpwise.net> wrote:
>On Sun, 16 Sep 2007 20:53:51 -0500, Robert <no@e.mail> wrote:
>
…[4 more quoted lines elided]…
>>>files to compile Cobol programs, so I might be safe:-) ?

[snip]

>>>Any help appreciated. Thanks.
>>
…[3 more quoted lines elided]…
>What is MAKE ?

The help (in the sense of 'assistance') Mr Wagner was offering, Mr Hobbs, 
seems to be telling you that you need to use an entirely different 
operating system.

DD
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

_(reply depth: 4)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-09-17T14:13:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com> <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com> <fcmdro$ed5$1@reader1.panix.com>`

```
On Mon, 17 Sep 2007 17:34:48 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com>,
>Graham Hobbs  <ghobbs@cdpwise.net> wrote:
…[21 more quoted lines elided]…
>DD

Oh, I see! But not a practical solution to my problem. For curiosity,
what OS is MAKE from?
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-17T14:42:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13etioal9kuae25@corp.supernews.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com> <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com> <fcmdro$ed5$1@reader1.panix.com> <epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com>`

```

"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message
news:epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com...
> On Mon, 17 Sep 2007 17:34:48 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
> >>>On Sun, 16 Sep 2007 21:00:11 -0400, Graham Hobbs <ghobbs@cdpwise.net>
wrote:
> >>>
[snip]
> >>>>Any help appreciated. Thanks.
> >>>
…[11 more quoted lines elided]…
> what OS is MAKE from?

Unix; but it has been available for DOS and Windows.
Microsoft has shipped 'make' and 'nmake' with some
of their development products, at least since the late '80s.
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-17T11:50:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190055024.624827.218930@o80g2000hse.googlegroups.com>`
- **In-Reply-To:** `<epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com> <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com> <fcmdro$ed5$1@reader1.panix.com> <epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com>`

```
On Sep 18, 6:13 am, Graham Hobbs <gho...@cdpwise.net> wrote:
> On Mon, 17 Sep 2007 17:34:48 +0000 (UTC), docdw...@panix.com () wrote:
> >In article <oqdte318tqknd921uhp48rokcvs7kko...@4ax.com>,
…[25 more quoted lines elided]…
> what OS is MAKE from?

make was originally developed on Unix type machines but is available
for all OSes. Microsoft's make may be called NMAKE.EXE if they still
distribute it.

http://msdn2.microsoft.com/en-us/library/dd9y37ha(VS.71).aspx

make requires a makefile which references the targets and the
dependencies and has the commands that make one from the other.
```

###### ↳ ↳ ↳ Re: CMD file to compile Cobol

_(reply depth: 6)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-09-17T16:04:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbnte3dbfosf0v4biirssejaec2kva2uvj@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <qfnre3toag105pqbjlrdo2s9l8kaqkonnl@4ax.com> <oqdte318tqknd921uhp48rokcvs7kkoep0@4ax.com> <fcmdro$ed5$1@reader1.panix.com> <epfte3h1jqi4in1ksruv52qotoc5s1jq1o@4ax.com> <1190055024.624827.218930@o80g2000hse.googlegroups.com>`

```
On Mon, 17 Sep 2007 11:50:24 -0700, Richard <riplin@Azonic.co.nz>
wrote:

>On Sep 18, 6:13 am, Graham Hobbs <gho...@cdpwise.net> wrote:
>> On Mon, 17 Sep 2007 17:34:48 +0000 (UTC), docdw...@panix.com () wrote:
…[37 more quoted lines elided]…
>
Will look into that and thanks.
```

#### ↳ Re: CMD file to compile Cobol

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2007-09-17T13:23:34+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46ee0f7a$0$11180$a82e2bb9@reader.athenanews.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com>`

```

"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
news:1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com...
> Hello,
> This is a CMD file question so why am I here - well I use DOS CMD
…[45 more quoted lines elided]…
>

You could always ask in alt.msdos.batch.nt ;)

STEPn.BAT begins

set errorfl=0
compile compileparameters
if errorlevel 1 set errorfl=1&goto :eof
translate translateparameters
if errorlevel 1 set errorfl=2&goto :eof
rexx rexxparameters
if errorlevel 1 set errorfl=3&goto :eof
if exist badfilename set errorfl=4&goto :eof
if not exist hastoexistfilename set errorfl=5&goto :eof

STEPn.BAT ends

Then in MASTER.BAT

MASTER.BAT begins

call STEP1 %1
if %errorfl%==1 goto step1compile
if %errorfl%==2 goto step1link
:: if reaching here, MASTER.BAT continues
call step2 %2
if %errorfl%==1 goto step2rexx1
if %errorfl%==2 goto step2rexx2
if %errorfl 3% goto step2rexx3
more stuff

MASTER.BAT ends

Notes:
filename.BAT is normally used; there are academic differences between 
filename.BAT and filename.CMD that should not worry the vast majority of 
users.
"&" is used as a command-separator
:eof (with the colon!) means "end-of-this-batchfile"
ERRORLEVEL is established by every executable, and IF errorlevel number is 
true if ERRORLEVEL is number OR GREATER (just like JES)
You could use IF %varname% GEQ value if you wish. The compare-opcodes are 
EQU NEQ LSS LEQ GTR and GEQ which should be obvious in meaning. (See IF /? 
from the prompt for more....)
You could also use

set errorfl=

in STEPn

to undefine the environment variable and then in MASTER.BAT

IF [not] defined errorfl

setting errorfl only if there is an exception, if you wish.
```

##### ↳ ↳ Re: CMD file to compile Cobol

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-09-17T13:45:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ncete3d71ip1god5ri8q1t0nf87ta5bpjc@4ax.com>`
- **References:** `<1nire3dtvldu2c9j71qsv66f20lcfu1q3n@4ax.com> <46ee0f7a$0$11180$a82e2bb9@reader.athenanews.com>`

```
On Mon, 17 Sep 2007 13:23:34 +0800, "billious"
<billious_1954@hotmail.com> wrote:

>
>"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
…[105 more quoted lines elided]…
>
What you wrote was very informative, some bits of which my book (1995)
does not describe. Will look into your suggestion.
 
Was also happy to hear about the alt.msdos.batch group - will update
my groups since I don't seem to have the .nt group. Will also do what
you suggest about posting there.

In the meantime, my thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
