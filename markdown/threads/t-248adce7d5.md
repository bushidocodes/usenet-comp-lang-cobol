[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# powercobol compile all directory projects

_12 messages · 6 participants · 2007-04_

---

### powercobol compile all directory projects

- **From:** "ramzenit" <mbazan@tin.it>
- **Date:** 2007-04-09T09:20:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com>`

```
Hello,
I need compile all powercobol program into my programs directory.
How to compile all program with a bat command ?
Thanks
RamZenit
```

#### ↳ Re: powercobol compile all directory projects

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2007-04-09T15:34:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176154568_21@sp12lax.superfeed.net>`
- **In-Reply-To:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com>`

```
ramzenit wrote:
> Hello,
> I need compile all powercobol program into my programs directory.
…[3 more quoted lines elided]…
> 

There is a "Rebuild All" button on the tool bar. It will re-compile
all of the source files in the project's (program's) directory.

I don't know how to structure a .BAT command file to do this.

Jeff

----== Posted via Newsfeeds.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

##### ↳ ↳ Re: powercobol compile all directory projects

- **From:** "ramzenit" <mbazan@tin.it>
- **Date:** 2007-04-10T02:46:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176198378.044937.253850@n59g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<1176154568_21@sp12lax.superfeed.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net>`

```
Thanks Jeff,
but my problem is different, I would like to compile all the ppj  in
the directory without calling them one to one back.


Jeff Campbell ha scritto:

> ramzenit wrote:
> > Hello,
…[15 more quoted lines elided]…
> ----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-10T08:19:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fOdnT8joIlAHYbbnZ2dnUVZ_vPinZ2d@golden.net>`
- **In-Reply-To:** `<1176198378.044937.253850@n59g2000hsh.googlegroups.com>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net> <1176198378.044937.253850@n59g2000hsh.googlegroups.com>`

```
ramzenit wrote:
> Thanks Jeff,
> but my problem is different, I would like to compile all the ppj  in
…[22 more quoted lines elided]…
> 

A batch file is pretty simple if you have projects set up. Each program 
in the project will have a corresponding make file.  Simply use nmake on 
each.  You will also need to check for errors after each.

Donald
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-10T09:11:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GrednVznCOlyEYbbnZ2dnUVZ_q-vnZ2d@golden.net>`
- **In-Reply-To:** `<1176198378.044937.253850@n59g2000hsh.googlegroups.com>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net> <1176198378.044937.253850@n59g2000hsh.googlegroups.com>`

```
ramzenit wrote:
> Thanks Jeff,
> but my problem is different, I would like to compile all the ppj  in
> the directory without calling them one to one back.

Further to my previous post ... the following batch program compiles a 
number of PRJ files.
M:
CD\LIBRARY\PROJECTS
NMAKE SCREENH.MAK
if errorlevel 1 goto done
NMAKE SETUPD.MAK
if errorlevel 1 goto done
NMAKE PRINTERT.MAK
if errorlevel 1 goto done
NMAKE TICKFILE.MAK
if errorlevel 1 goto done
NMAKE TICKREPS.MAK
if errorlevel 1 goto done
NMAKE TICKHIGH.MAK
if errorlevel 1 goto done
NMAKE TICKMAIN.MAK
if errorlevel 1 goto done
NMAKE TICKEXES.MAK
if errorlevel 1 goto done
CD\LIBRARY\MISC
CALL SETUP
CD\LIBRARY\PROJECTS
goto exit
:done
PAUSE ERROR
:exit

SCREENH, SETUPD, etc. are each PRJ files. If any has an error, it hits 
the pause at the end, else it completes.

Donald
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-11T04:13:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<581rc4F2fb08lU1@mid.individual.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net> <1176198378.044937.253850@n59g2000hsh.googlegroups.com> <GrednVznCOlyEYbbnZ2dnUVZ_q-vnZ2d@golden.net>`

```

"donald tees" <donald@execulink.com> wrote in message 
news:GrednVznCOlyEYbbnZ2dnUVZ_q-vnZ2d@golden.net...
> ramzenit wrote:
>> Thanks Jeff,
…[34 more quoted lines elided]…
> Donald

Using NMAKE is a pretty cool idea, Donald.

Will it accept wildcard operands... ?
NMAKE *.MAK > LPT1:

...could be useful. Instead of a pause when a build screws up, check the 
listing and see if they all completed successfully...

Unfortunately the machine I'm writing this on doesn't have NMAKE on it, and 
the COBOL machine is powered down and in a different location, so I can't 
check it.

Pete.
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

_(reply depth: 5)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-10T12:37:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2KqdncrVwazcIIbbnZ2dnUVZ_jidnZ2d@golden.net>`
- **In-Reply-To:** `<581rc4F2fb08lU1@mid.individual.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net> <1176198378.044937.253850@n59g2000hsh.googlegroups.com> <GrednVznCOlyEYbbnZ2dnUVZ_q-vnZ2d@golden.net> <581rc4F2fb08lU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> Using NMAKE is a pretty cool idea, Donald.
…[13 more quoted lines elided]…
> 
NMAKE is used by Fujitsu Cobol, and the MAK files are created by the
project manager.  I notice that when I run it, it says copyright by MS.
I do not know if it was installed at window installation, or as part
of the Fujitsu install.  Regardless, the standard Cobol "IDE"(Pstaff) 
from Fujitsu use it to do the build when you hit the Compile button. 
All it really does is put the output into a window.

I do not like Pstaff much, and usually end up with six or seven 
different pstaff projects within a real project. The batch program is a 
way of doing a complete project build, and makes it a lot faster to 
test.  Generally, I run my install program as the last step of the batch 
program.

If you put the output into different areas by using a CBI file, then a 
forced full rebuild can be done by simply erasing the area. I removed 
the CD \LIBRARY\OBJECT, ERASE *.* in the sample batch program for 
clarity. Since that asks for confirmation, the choice happens when you 
run it. The CBI files for the projects in the shown batch file all look 
like:

[Compile Options]
COPY=Yes
OBJECT=Yes \LIBRARY\OBJECT
PRINT=Yes \LIBRARY\LISTINGS
REP=\library\OBJECT
SOURCE=Yes
TRUNC=No


Donald
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

_(reply depth: 5)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-10T12:49:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t6CdnbKhI6eCXYbbnZ2dnUVZ_oytnZ2d@golden.net>`
- **In-Reply-To:** `<581rc4F2fb08lU1@mid.individual.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <1176154568_21@sp12lax.superfeed.net> <1176198378.044937.253850@n59g2000hsh.googlegroups.com> <GrednVznCOlyEYbbnZ2dnUVZ_q-vnZ2d@golden.net> <581rc4F2fb08lU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Will it accept wildcard operands... ?
> NMAKE *.MAK > LPT1:
> 
Do not know, as I have never tried it.  However, I can see two problem 
doing it the way you suggest.

First of all, the entire point of the batch file is to do things in a 
specific order. The first project creates rep files and object libraries 
required for the second, etc.  That is the main problem with Pstaff. 
The damed thing sorts into alphabetical order, and there is no way to 
force a specific order except doing it manually, one DLL at a time.
The approach is fubar for OOP stuff, as inheritance levels etc. are 
completely discarded. Thus I split the main project up into 
sub-projects, and compile them in order.

Secondly, I do that when I am testing ... if the compile finishes, I 
proceed to the install step, and sometimes even end the batch file with 
a CD to the run area and execution.

NMAKE *.mak may work for a small collection of independent programs, 
though.  I'll try it later.

Donald
```

#### ↳ Re: powercobol compile all directory projects

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-04-10T12:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spLSh.7613$u03.6883@newssvr21.news.prodigy.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com>`

```
> I need compile all powercobol program into my programs directory.
> How to compile all program with a bat command ?

The batch command will be something like..

FOR %F IN  (*.cbl) DO compilername.exe  %F options

Get exact syntax by looking up help for CMD files;  from a command prompt 
type   "help for"

Still unsure? try one of the newsgroups which are dedicated to batch/command 
files. Some of those guys are incredibly imaginative.
```

#### ↳ Re: powercobol compile all directory projects

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-04-10T12:17:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131nhkdqhv1i63a@news.supernews.com>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com>`

```
ramzenit wrote:
> Hello,
> I need compile all powercobol program into my programs directory.
> How to compile all program with a bat command ?
> Thanks
> RamZenit

How about:

PowerCOB {/build | /rebuild} [/Debug | /Release]
   [/cbi: "OPTION-FILE-NAME"]
   "PROJECT-FILE-NAME"

with the results being placed in the "(projectname).blg" file.

Example:

powercob /build "C:\myprojects\proj1.ppj"

The PCV6 documentation even has a sample bat file to rebuild a whole passle 
of programs while concatenating the results files into one big file for 
review.

I might even modify the supplied bat file using the FOR command to suck up 
everything in the folder.

I did. Here's my batch file, COMPILE.BAT

C:
CD \C-SOURCE
ECHO BEGIN > RESULT.TXT
FOR %%A IN (*.PPJ) DO POWERCOB /Rebuild /Release %%A
FOR %%A IN (*.BLG) DO TYPE %%A >> RESULT.TXT
FOR %%A IN (*.BLG) DO DEL %%A
TYPE RESULT.TXT

You might want to gussy it up some, but it's a start.
```

##### ↳ ↳ Re: powercobol compile all directory projects

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-04-11T11:47:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131q493n5m1v578@news.supernews.com>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <131nhkdqhv1i63a@news.supernews.com>`

```
HeyBub wrote:
> ramzenit wrote:
>> Hello,
…[34 more quoted lines elided]…
> You might want to gussy it up some, but it's a start.

So, I gussied it up:

(COMPILE.BAT)

@ECHO OFF
C:
CD \C-SOURCE
IF EXIST == RESULT.TXT DEL RESULT.TXT
IF EXIST == *.BLG DEL *.BLG
ECHO BEGIN COMPILATION BATCH > RESULT.TXT
FOR %%A IN (*.PPJ) DO call compile2.bat %%A
TYPE RESULT.TXT

(COMPILE2.BAT)

@ECHO OFF
ECHO Compile %1
echo === BEGIN %1  >> RESULT.TXT
POWERCOB /REBUILD %1
IF ERRORLEVEL 1 GOTO FAIL
GOTO OK

:FAIL
ECHO . >> RESULT.TXT
ECHO !!!  E R R O R  I N   %1    !!! >> RESULT.TXT
ECHO . >> RESULT.TXT

:OK
TYPE *.BLG >> RESULT.TXT
DEL *.BLG /Q
echo === END %1 >> result.txt
ECHO =============================== >> RESULT.TXT
ECHO =============================== >> RESULT.TXT
ECHO . >> RESULT.TXT
ECHO . >> RESULT.TXT
```

###### ↳ ↳ ↳ Re: powercobol compile all directory projects

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-12T11:25:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<585938F2f6558U1@mid.individual.net>`
- **References:** `<1176135636.430721.249170@w1g2000hsg.googlegroups.com> <131nhkdqhv1i63a@news.supernews.com> <131q493n5m1v578@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:131q493n5m1v578@news.supernews.com...
> HeyBub wrote:
>> ramzenit wrote:
…[73 more quoted lines elided]…
>
Cool! (in a 1980s kind of way...:-))

These days it should be a WSH script, but, Hey, if it works...and it 
obviously does. I hope the OP takes the trouble to acknowledge your efforts, 
Jerry.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
