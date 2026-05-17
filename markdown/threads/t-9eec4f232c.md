[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PL/I to COBOL conversion

_4 messages · 4 participants · 1996-04_

---

### PL/I to COBOL conversion

- **From:** "fisp..." <ua-author-17086976@usenetarchives.gap>
- **Date:** 1996-04-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kqsu6$95s@hasle.sn.no>`

```
I am looking for a tool that converts PL/I code to COBOL. The PL/I
code in question has been poorly maintained over the years and is pure
spaghetti. The purpose of the conversion is to be able to generate
structure charts for the code. Hopefully that will aid the
documentation of the system and the porting to an RS6000 / AIX /
Oracle7.x environment.

The PL/I platform is IBM3090 / MVS / DB2

Can anyone help?

Chris.
```

#### ↳ Re: PL/I to COBOL conversion

- **From:** "r..." <ua-author-9511235@usenetarchives.gap>
- **Date:** 1996-04-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eec4f232c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4kqsu6$95s@hasle.sn.no>`
- **References:** `<4kqsu6$95s@hasle.sn.no>`

```
fis··.@s··.no (Fis/P -Felles) writes:

>I am looking for a tool that converts PL/I code to another high-level
>language such as C or COBOL. The PL/I code in question has been poorly
…[3 more quoted lines elided]…
>porting to an RS6000 / AIX / Oracle7.x environment.

>The PL/I platform is IBM3090 / MVS / DB2
>Can anyone help?
>Chris.

---You might find that there are tools to produce structure
charts directly from PL/I. Have you contacted Leverage
Technologies?
Robin

---------------------------------------------------------------------------

PL/I Analyzer

---------------------------------------------------------------------------

The interactive, extensible PL/I reengineering workbench

PL/I Analyzer is the first truly customizable reverse engineering and
reengineering tool for PL/I. PL/I Analyzer is used by software engineers to
understand, evaluate, document, and reengineer existing PL/I systems.

PL/I Analyzer has built-in functionality for generating interactive
graphical views of PL/I code such as structure charts, control flow
diagrams, data flow diagrams, and cross reference tables. With an
easy-to-use graphical interface based on the industry standard X Window
System, software engineers can immediately apply PL/I Analyzer to help
untangle large PL/I systems. Since PL/I Analyzer works directly on existing
code, there is no new methodology to learn.

Once PL/I Analyzer has analyzed your PL/I system, you can export the design
information to Software Through Pictures or ObjectMaker, analysis and
design tools from Interactive Development Environments and Mark V Systems
respectively. These tools can then be used to maintain, enhance, and
document the system using state-of-the-art CASE technology.

Unlike other reengineering tools, PL/I Analyzer doesn't limit you to a
fixed set of reengineering capabilities. Instead, PL/I Analyzer comes with
a fully documented reengineering API so you can add capabilities and modify
existing ones using Software Refinery, the worlds premier development
environment for reengineering tools. For example, you can add your own
coding and design standards and software metrics for software quality
assurance; or you can build translation and rehosting tools.

Key Features

Easy to Use
PL/I Analyzer uses a pull-down menu interface familiar to workstation
and personal computer users. Each menu has online help that is
displayed dynamically as the menus are used. You can browse several
views of a program simultaneously using multiple windows.

Graphical Views of Code
PL/I analyzer analyzes PL/I programs and produces a database of
information about variables, units, types, calls, files, control flow,
set/use of variables, and more. PL/I analyzer generates detailed
graphical reports that display this information using a variety of
diagrams and tables. You can navigate from reports to source code with
a single mouse click.

Exports to CASE Tools
PL/I Analyzer can export the design information it extracts from your
program to populate the repositories of Software Through Pictures or
ObjectMaker, forward-engineering CASE tools.

Interactive Display and PostScript Printing
Design information that PL/I Analyzer extracts from your PL/I code can
be browsed graphically online, saved in an ASCII format, or printed on
a PostScript printer to produce high-quality hardcopy.

Extensible
PL/I Analyzer comes with a fully documented reengineering API so you
can modify it to meet your reengineering requirements. The
reengineering API includes both a schema for the internal
representation of PL/I code and a set of functions for parsing,
printing, and analyzing systems.

Copyright 1994 Leverage Technologists, Inc. All rights reserved. Restricted
Rights Legend.

---------------------------------------------------------------------------
Leverage Technologists Inc. | 6701 Democracy Blvd., Suite 324, Bethesda, MD
20817 | (301)309-8783
in··.@lev··h.com
```

##### ↳ ↳ Re: PL/I to COBOL conversion

- **From:** "fle..." <ua-author-1063345@usenetarchives.gap>
- **Date:** 1996-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eec4f232c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9eec4f232c-p2@usenetarchives.gap>`
- **References:** `<4kqsu6$95s@hasle.sn.no> <gap-9eec4f232c-p2@usenetarchives.gap>`

```
› I am looking for a  tool that converts PL/I code to another high-level
› language such as C or COBOL. The PL/I code in question has been poorly
…[7 more quoted lines elided]…
› 
You may want to have a look at the Micro Focus product Revolve. It'll do the
analysis and documentation of your PL/I code without conversion. You may need
to download the source to a PC or LAN, but don't quote me. Contact the
Raleigh office of Micro Focus 1-610-992-3400 (Sorry, I don't recall the 1-800
number :-)

Graham Fletcher
```

#### ↳ Re: PL/I to COBOL conversion

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-04-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eec4f232c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4kqsu6$95s@hasle.sn.no>`
- **References:** `<4kqsu6$95s@hasle.sn.no>`

```
Fis/P -Felles wrote:
: I am looking for a tool that converts PL/I code to COBOL.

If you're doing this in order to study and restructure the code, I
strongly recommend that you work out some techniques to do the study and
analysis in the original PL/I. Any automatic conversion will (1) be even
uglier code than the original PL/I; (2) probably require an understanding
of the original program in order to make it work! And any manual
conversion will require some knowledge of the program, unless you follow a
learn-while-converting approach such as I suggest below.

Badly maintained PL/I code is scarey stuff, because there are all sorts of
side-effects and defaults which may apply. And PL/I has some features
which may not translate in a general way to another language; for example,
PUT LIST more or less shoots from the hip, depending on width of the data,
etc. If you must duplicate this behavior, you may need to write a special
module to emulate what PL/I would have done.

My experience in many inter-program conversions has been that a few
semi-automatic transformations produce a good intermediate form, from
which I can easily produce the target-language program to do something
between what the old program did and what I really want.

But I sat down with a good text editor more than once and converted PL/I
into COBOL or C, and it went rather swiftly. For example, you start out
by replacing all CHAR(nn) with pic x(nn), etc. Review your varying-length
fields to find out if they really need to vary; if so, you have to set up
the whole OCCURS DEPENDING business; but you may make them fixed and then
output them with STRING DELIMITED SPACES, etc.

Another step in converting PL/I spaghetti into COBOL spaghetti could be to
convert all PL/I procedures to COBOL paragraph names, and also convert
every DO and BEGIN and END (etc.) to a cleverly-generated paragraph
name.... this retains some tracks back into the PL/I and you can actually
refer to these labels if needed.

of course if you're going to COBOL your data division converts very nicely
but your procedure division will be a breech delivery. Parameters to
procedures will require very careful crafting of COBOL sub-programs which
of course must not do any recursive calls.

If you're going to C, your data division is a taffy-pull, but the procedural
code will convert rather directly and you won't have much problem with
parameters or recursion. So the character of the programs you are converting
should guide you towards an appropriate targe language, or perhaps a mix of
languages (COBOL for some procedures, C for others).

I don't know Pascal well, but if it's an acceptable target language you
might find it closer to PL/I than either COBOL or C.

Good luck!

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
