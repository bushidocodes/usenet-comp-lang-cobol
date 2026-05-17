[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Compiler Directives?

_5 messages · 4 participants · 1995-11 → 1995-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Compiler Directives?

- **From:** "dbma..." <ua-author-1810562@usenetarchives.gap>
- **Date:** 1995-11-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49jd93$rrk@news.onramp.net>`

```
I am using the Windows version of MicroFocus Cobol and I am attempting to
understand how the MF Workbench and the Windows (Visual) MF Workbench get
thier compiler directives. I know that the standard Workbench program
gets the directives from the '*.DIR' files. The reason I need to know
this is the standard Workbench compiler will compile a program w/out
errors, but the visual version generates 100+ errors.

I am compiling the program using VS COBOL(4).

The version of WB I am using is 3.2.46.
```

#### ↳ Re: MF Compiler Directives?

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-11-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea340b59ed-p2@usenetarchives.gap>`
- **In-Reply-To:** `<49jd93$rrk@news.onramp.net>`
- **References:** `<49jd93$rrk@news.onramp.net>`

```
In article <49jd93$r.··.@new··p.net>, dbm··.@onr··p.net says...
› 
› I am using the Windows version of MicroFocus Cobol and I am attempting to 
…[6 more quoted lines elided]…
› I am compiling the program using VS COBOL(4).

Bear with me, this gets complicated to explain....

On the standard character workbench menu system, the VS COBOL(4) setting only
sets the directive vsc2(4) which provides most of the compatibility with VS
COBOL II but isn't completely mainframe perfect.

There is a 'Mainframe Development Environment' (MDE) menu system which
provides stricter adherance than just syntax checking. If not installed as
default, try typing WB MDE.

Under MDE, a directive file called 'WB.DIR' is used if you have one. Normally
this just has a line in it that points to one of the dialect specific
directives files. ie. the WBxxx.DIR files where 'xxx' is the particular
dialect. In your case WBVSC24.DIR.

So WB.DIR may look like this

use(wbvsc24.dir)

The settings in WBVSC24.DIR are altered using a program called the 'Compiler
Options Selections Aid' or COMPOPT for short. This allows a subset of
directives specific to VSC24 to be altered. The full set are stored in a
library and shouldn't be altered. In the case of VSC24, MFVSC24.DIR in the
COBCLI.LBR Library file. To override the settings in MFVSC24.DIR, an
intermediate file, DFVSC24.DIR can be used.

So, to recap you have....

WB.DIR which points to
WBVSC24.DIR which contains user configurable settings and points to
DFVSC24.DIR which contins non-user configurable via COMPOPT directives, a
good place for site wide defaults incidentally, which points
to....
MFVSC24.DIR which contains the full set of directives which MF thinks best
emulates VSC2 4 behaviour and shouldn't be altered and is
hidden away in a library so you can't get at it easily.


When using the graphical product, if you specify the COMPOPT directive on the
tool or project icon COMPOPT (the program) is also used. The check and the
Edit+Animate tool have COMPOPT on by default. The difference with the
graphical side however is that instead of WB.DIR, it uses COMPOPT.DIR. The
other directives files used follow the same pattern. COMPOPT.DIR and the
WBxxx.DIR files should not be edited by hand as COMPOPT overwrites these each
time new settings are ok'd.

Top Tip: If you want project specific directives, put each project in a
seperate directory, copy the COMPOPT.DIR and WBxxx.DIR to the project's
directory. Delete the the same .DIR files from $COBDIR. COMPOPT will pick
up the local .DIR files from the project.

The reason they follow the same pattern is that you're running the same
COMPOPT program. It either runs in character emulation mode of GUI mode. It's
a Panels2 application.

On the GUI side there is also a main dialog box at the start before you get to
the dialect specific directives that lets you pick which dialect, listing
preferences, IMS, CICS, SQL etc settings.


So, to sum up, your directives should be the same between the character MDE
Menu system and the GUI system. If you're using the standard VSC2(4) directive
from the 'normal' character WB menu, you may not be compatible between the
two.

There's a chapter in the workbench manuals (System Reference I think) that
explains how COMPOPT works but if you have any further questions, ask me. I'm
the programmer behind COMPOPT btw. Don't ask me about individual directive
settings for compatibility with VSC2 or whatever though as that's someone
elses job thankfully. ;-)

Shaun C. Murray                               | s.··.@mfl··o.uk (work)
Micro Focus Ltd, UK. http://www.mfltd.co.uk   | s.··.@doo··o.uk (home)
```

#### ↳ Re: MF Compiler Directives?

- **From:** "david james" <ua-author-17271@usenetarchives.gap>
- **Date:** 1995-12-06T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea340b59ed-p3@usenetarchives.gap>`
- **In-Reply-To:** `<49jd93$rrk@news.onramp.net>`
- **References:** `<49jd93$rrk@news.onramp.net>`

```
dbm··.@onr··p.net (david martin) wrote:
› I am using the Windows version of MicroFocus Cobol and I am attempting to 
› understand how the MF Workbench and the Windows (Visual) MF Workbench get 
…[8 more quoted lines elided]…
› 
When you drop your project on the Edit & Animate tool the default options
of the tool show a Compiler directive button. You click on this to set
your directives. Micro Focus I believe then creates a compopt.dir that
points to a particular directive file in an lbr file. If you look
around in the directories you'll find directive files like cobol.dir
and default.dir. These are used sometimes too. These files also
point to other directives files. (I'm not real sure that this is exactly
the way it does it, but it is something like this). There is a utility
you can run from DOS that gives you the sequence and contents of the
directive files used.
A way that we have found easier is to make your own directive file and
tell your program to use that one with a $SET USE statement. This takes
the quesswork out of knowing which directives your getting.
```

##### ↳ ↳ Re: MF Compiler Directives?

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-12-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea340b59ed-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ea340b59ed-p3@usenetarchives.gap>`
- **References:** `<49jd93$rrk@news.onramp.net> <gap-ea340b59ed-p3@usenetarchives.gap>`

```
In article <4a6nq5$6.··.@mav··s.com>, plh··.@e··.com says...
› 
› When you drop your project on the Edit & Animate tool the default options 
› of the tool show a Compiler directive button.  You click on this to set 
› your directives. Micro Focus I believe then creates a compopt.dir that 
› points to a particular directive file in an lbr file.  

That's the gist of it. It depends on which dialect of compiler you wish to
emulate as to which file it points at. The GUI off of the 'Compiler Options'
button also lets you alter a subset of the dialects specific directives as
well as allowing listings, preprocessors etc.

› If you look 
› around in the directories you'll find directive files like cobol.dir 
› and default.dir. These are used sometimes too.  These files also 
› point to other directives files.  (I'm not real sure that this is exactly 
› the way it does it, but it is something like this).  

The only files that concern the GUI user really are the compopt.dir file and
those that it points too using nested USE() directives. Don't worry about the
others. cobol.dir is for command-line compiles. default.dir only provides a
default cobol.dir during the install I think. It's not used directly.

› There is a utility
› you can run from DOS that gives you the sequence and contents of the
› directive files used.

That would be VCOMPOPT. In the 4.0 product you just click on the 'View Report'
button from the GUI and it gives you a scrolly window to view the VCOMPOPT
output in. A lot of people weren't aware that VCOMPOPT existed. This should be
in one of the 3.2 update disks too.

› A way that we have found easier is to make your own directive file and
› tell your program to use that one with a $SET USE statement. This takes
› the quesswork out of knowing which directives your getting.

That's ok if you aren't going to change directives often.



I think you'll like the 4.0 products Advanced Organiser. It keeps a database
of directives set with each individual program rather than a global
compopt.dir file so you can just click on all the programs you want, select
compile from the pop up menu and each file is compiled with it's own set of
directives switching on CICS, IMS, SQL etc as and when it's needed. In the
shops v. soon now.



Shaun C. Murray                               | s.··.@mfl··o.uk (work)
Micro Focus Ltd, UK. http://www.mfltd.co.uk   | s.··.@doo··o.uk (home)
```

#### ↳ Re: MF Compiler Directives?

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-12-06T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea340b59ed-p5@usenetarchives.gap>`
- **In-Reply-To:** `<49jd93$rrk@news.onramp.net>`
- **References:** `<49jd93$rrk@news.onramp.net>`

```
To get good VS COBOL II R4 emulation, you probably want to use a
directive of

USE(WBVSC24)

instead of just using

VSC2(4)

The former gets a "bunch" of directives while the latter just
sets the reserved word list.

Let me know if this doesn't help.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
