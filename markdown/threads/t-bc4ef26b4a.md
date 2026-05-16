[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# USE FOR DEBUGGING

_8 messages · 5 participants · 2005-01_

---

### USE FOR DEBUGGING

- **From:** "ralf" <ralf@cwi.nl>
- **Date:** 2005-01-11T06:04:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com>`

```
I wonder whether the paragraph from a
declaratives section with USE FOR DEBUGGING ON xyz
has any chance to know that it is intercepting xyz?

I mean can the paragraph access xyz via a data name or otherwise?

This is clearly a good idea since we might want to
reuse a generic paragraph from a copy book. Also we might
want to intercept all procedures in which case we would
really want to know what procedure we are handling.

Reading through '85 material, I can't find hints at the
expected style of finding out these things. I know that
USE FOR DEBUGGING is gone in Cobol 2002, but USE FOR
DEBUGGING is quite interesting from an AOP point of view,
as I learnt via helpful comments from Barry Tauber.

That is, USE FOR DEBUGGING provides procedure interceptors.
However, what I can't find is any join-point reflection
(in AOP terms), i.e., as described above, say _a way to
determine the name of the intercepted procedure within
the handling paragraph_.

Likewise, when deploying an error handler such as

USE AFTER ERROR ON INPUT
*> handler statements follow

can I somehow access the file name that was accessed by
the offending file I/O statement?

For more background; see below.

Any help greatly appreciated.
I really just try to get Cobol's history right.

Ralf

http://www.cwi.nl/~ralf/AspectCobol/

What does aspect-oriented programming mean to Cobol?

Ralf Laemmel and Kris De Schutter

We study AOP in the context of business programming with Cobol. We
face the following questions: What are join points in Cobol programs?
What is advice? Does classic Cobol provide any constructs that hint at
AOP?  (Yes!) What are typical crosscutting concerns in the Cobol
world? How do otherwise typical crosscutting concerns make sense for
Cobol? How does AOP for Cobol align with classic re-engineering
transformations for Cobol? We deliver an AOP language design for
Cobol. Codename: AspectCobol. While we adopt several ideas from
AspectJ and friends, we also devise original techniques for join-point
identification and context capture. We briefly discuss a prototypical
implementation of AspectCobol.
```

#### ↳ Re: USE FOR DEBUGGING

- **From:** "ralf" <ralf@cwi.nl>
- **Date:** 2005-01-11T06:32:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105453937.758872.92770@f14g2000cwb.googlegroups.com>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com>`

```
I should have added that I also wonder how the typical program run for
a program that was compiled WITH DEBUGGING MODE would look like (for
some mainstream compiler). My guess is that runtime systems produces a
log of the program run, while this log definitely contains the names of
intercepted procedures (and line numbers for debugging lines, i.e.,
lines with "D" in column 7), but this "free" information would be
interleaved with output that is produced by the programmer-provided
handler paragraphs, if any.

Does anyone recollect whether this guess is in alignment with reality?
Thanks,
Ralf
```

##### ↳ ↳ Re: USE FOR DEBUGGING

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-11T14:59:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mRREd.574287$O24.88083@news.easynews.com>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com> <1105453937.758872.92770@f14g2000cwb.googlegroups.com>`

```
The answer is that using "WITH DEBUG MODE" is a compile-time issue.  The 
run-time is impacted by the "debug" (not specified in the Standard) option.

IMHO, there is no "typical" output of such programs as (for several decades now) 
"interactive debuggers" have taking over MOST of the (previous) uses of the 
(obsolete) DEBUG lines and USE FOR DEBUGGING features.
```

##### ↳ ↳ Re: USE FOR DEBUGGING

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-01-11T15:10:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs0qb5$lj5$1@peabody.colorado.edu>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com> <1105453937.758872.92770@f14g2000cwb.googlegroups.com>`

```

On 11-Jan-2005, "ralf" <ralf@cwi.nl> wrote:

> I should have added that I also wonder how the typical program run for
> a program that was compiled WITH DEBUGGING MODE would look like (for
…[7 more quoted lines elided]…
> Does anyone recollect whether this guess is in alignment with reality?

I'm not sure I understand.    When I compile WITH DEBUGGING MODE, lines with D
in column 6 are treated as thought there was a space in column 6.   Otherwise,
those lines are treated as though there was an * in column 6.   It's as if you
went with a pencil and eraser and changed the "D" to either a space or an
asterisk and then compiled the resulting program.

My IDMS pre-compiler doesn't know squat about WITH DEBUGGING MODE, so I can't
use it with IDMS commands.
```

###### ↳ ↳ ↳ Re: USE FOR DEBUGGING

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-11T17:03:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Ofz-yj9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com> <1105453937.758872.92770@f14g2000cwb.googlegroups.com> <cs0qb5$lj5$1@peabody.colorado.edu>`

```
.    On  11.01.05
  wrote  howard@brazee.net (Howard Brazee)
     on  /COMP/LANG/COBOL
     in  cs0qb5$lj5$1@peabody.colorado.edu
  about  Re: USE FOR DEBUGGING


HB> When I compile WITH DEBUGGING MODE, lines with D in column 6 are
HB> treated as thought there was a space in column 6.   Otherwise,
HB> those lines are treated as though there was an * in column 6.
HB> It's as if you went with a pencil and eraser and changed the "D"
HB> to either a space or an asterisk and then compiled the resulting
HB> program.


   To put it differently -- it is just a conditional compilation with  
just two possibilities: with or without debugging mode.

   A full COBOL-2002 would offer more choices for conditional  
compilation.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Die Superklugheit ist eine der verï¿½chtlichsten Arten von Unklugheit. -G.C.Lichtenberg
```

#### ↳ Re: USE FOR DEBUGGING

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-11T14:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2PREd.574212$O24.88042@news.easynews.com>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com>`

```
Check for the DEBUG-ITEM special register.  It provides some information. I 
can't tell exactly what you are asking for, but it may provide it.
```

##### ↳ ↳ Re: USE FOR DEBUGGING

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-11T08:16:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs0u4a$21ce$1@si05.rsvl.unisys.com>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com> <2PREd.574212$O24.88042@news.easynews.com>`

```
Note that what you *do* with the DEBUG-ITEM is up to you as a programmer.
For example, you could set up a file (assigned to printer?) and all the
necessary OPENs and CLOSEs and WRITEs and MOVEs to get the information from
the special register to the end user, using "D" in Column 7 for all the
statements and declarations.

If the program isn't compiled WITH DEBUGGING MODE, the statements and
declarations "disappear".

If the program isn't executed with the appropriate option, the statements
are bypassed and the declarations unreferenced at execution time.

    -Chuck Stevens

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:2PREd.574212$O24.88042@news.easynews.com...
> Check for the DEBUG-ITEM special register.  It provides some information.
I
> can't tell exactly what you are asking for, but it may provide it.
>
…[62 more quoted lines elided]…
>
```

##### ↳ ↳ Re: USE FOR DEBUGGING

- **From:** "ralf" <ralf@cwi.nl>
- **Date:** 2005-01-11T08:36:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105461408.292721.257130@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<2PREd.574212$O24.88042@news.easynews.com>`
- **References:** `<1105452282.859292.252480@f14g2000cwb.googlegroups.com> <2PREd.574212$O24.88042@news.easynews.com>`

```
Yes, thanks,
DEBUG-ITEM is perfect!
Ralf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
