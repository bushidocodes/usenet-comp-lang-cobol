[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "D" in the 7th Column

_5 messages · 5 participants · 1997-10_

---

### "D" in the 7th Column

- **From:** "ganesh kudva" <ua-author-13908158@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`

```

Hi,

Can anybody tell me about the use of "D" in the 7th Column ?

I know it is used for Debugging. I couldn't get the details.
Is the statement with "D" in the seventh column ignored while compiling ?
Is it treated as comment line ? While compiling, I am not getting an error
message for a line with an undefined variable which has
"D" in the 7th column.

Can anybody explain ?

Thanks in advance,

Ganesh Kudva.
```

#### ↳ Re: "D" in the 7th Column

- **From:** "lars bjerges" <ua-author-6588782@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9ad71a33fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`
- **References:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`

```

"With debugging mode"

i.e "SOURCE-COMPUTER. xxx WITH DEBUGGING MODE.

Activates a compile-time switch for debugging lines written in the source.

A debugging line is compiled ONLY when the switch is activated.
To specify a debugging line, code "D" in col 7.
Debugging lines can be coded in ENVIRONMENT, DATA or PROCEDURE
divisions.

Lars

Ganesh Kudva skrev i inlï¿½gg
<61itgf$7.··.@sio··h.de>...
› Hi,
› 
…[3 more quoted lines elided]…
› Is the statement with "D" in the seventh column ignored while compiling ?
 
› Is it treated as comment line ?  While compiling, I am not getting an
› error
…[10 more quoted lines elided]…
›
```

#### ↳ Re: "D" in the 7th Column

- **From:** "lookin'" <ua-author-915283@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9ad71a33fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`
- **References:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`

```

On Thu, 9 Oct 1997 21:05:51 +0530, "Ganesh Kudva"
wrote:
[...]
› Can anybody tell me about the use of "D" in the 7th Column ?
› 
…[4 more quoted lines elided]…
› "D" in the 7th column.
[...]

The debugging module in ANSI COBOL (74 and above) consists of several
related items. Briefly, they are as follows:

1. The WITH DEBUGGING MODE clause can be included in the
SOURCE-COMPUTER paragraph of the Environment Division. If so, any
debugging declarative procedures and the debugging data item are
included in the compiled program, and debugging lines (D in column 7)
are also included in the compiled program.

2. Lines coded with a D in column 7 are debugging lines. If the
debugging features are activated (1, above), debugging lines are
included in the compiled program. If not, then lines with D in column
7 are treated as comments. Some implementors prohibit debugging lines
from appearing in the source file at any point before the
SOURCE-COMPUTER paragraph; some others treat such lines as always
being comments.

3. The debug data item is provided by COBOL when debugging features
are activated. There is one such item per program, and it is
typically defined as follows (All fields are USAGE DISPLAY, all
FILLERs contain SPACE, all signed fields are SIGN LEADING SEPARATE.):
01 DEBUG-ITEM.
02 DEBUG-LINE PIC X(06).
02 FILLER PIC X.
02 DEBUG-NAME PIC X(30).
02 FILLER PIC X.
02 DEBUG-SUB-1 PIC S9(04).
02 FILLER PIC X.
02 DEBUG-SUB-2 PIC S9(04).
02 FILLER PIC X.
02 DEBUG-SUB-3 PIC S9(04).
02 FILLER PIC X.
02 DEBUG-CONTENTS PIC X(nn). (Length depends on item DEBUGged.)
The debug data item is useful within debugging declarative procedures.

4. The declarative debugging procedures may be defined by using the
USE FOR DEBUGGING statement within the DECLARATIVES portion of the
Procedure Division. Formats are USE FOR DEBUGGING ON ALL PROCEDURES,
...ON ALL REFERENCES OF , and ...ON , among
others. You will have to consult your implementor's reference manual
for specifics.

5. A run-time switch is provided to turn on and off the debugging
declarative procedures; it has no effect on statements with D in
column 7. The switch's method of activation is implementor dependent.
Again, consult your implementor's reference manual.

I hope this information helps to unravel COBOL debugging. Good luck.

Reply Addr:-->WDavid dot Simon at ATL dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

#### ↳ Re: "D" in the 7th Column

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9ad71a33fb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`
- **References:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`

```

On Thu, 9 Oct 1997 21:05:51 +0530, "Ganesh Kudva"
wrote:
› Can anybody tell me about the use of "D" in the 7th Column ?
› 
…[4 more quoted lines elided]…
› "D" in the 7th column.

D in column 7 is normally treated as a comment.

To cause the D lines to compile, specify the source computer as:

SOURCE-COMPUTER. anycomputer WITH DEBUGGING MODE.

Many compilers/operating systems provide other ways to cause this to
happen, but this should always work.

George Trudeau
```

#### ↳ Re: "D" in the 7th Column

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9ad71a33fb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`
- **References:** `<61itgf$7vd@sioux.fr.internet.bosch.de>`

```

"Ganesh Kudva" wrote:

› Hi,
› 
…[14 more quoted lines elided]…
› 
USED TO BE:......

Different compilers had directives related to 'WITH DEBUG ON'
A 'D' in column 7 was treated as a comment line UNLESS debug was
triggered, usually for the whole compile (but not always).
The debug was in a PARM or a $ directive and, in an old compiler, in
the environment division.

Nice way to leave diagnostic code in a job for 'regression' testing.

JR
and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
