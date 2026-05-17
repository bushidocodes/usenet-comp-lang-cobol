[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is ANSI 85 COBOL the most common version in Y2K projects ?

_5 messages · 5 participants · 1997-12_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Is ANSI 85 COBOL the most common version in Y2K projects ?

- **From:** "jim gallagher" <ua-author-2020628@usenetarchives.gap>
- **Date:** 1997-12-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6715dh$g7$1@newsfep3.sprintmail.com>`

```

In systems that require Y2K work - is COBOL 74 or COBOL 85 the most common.
What are your experiences ?

Please Email me.

Thanks

Jim G.

jim··.@fre··l.us
```

#### ↳ Re: Is ANSI 85 COBOL the most common version in Y2K projects ?

- **From:** "steve" <ua-author-10786@usenetarchives.gap>
- **Date:** 1997-12-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc8768a3ff-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6715dh$g7$1@newsfep3.sprintmail.com>`
- **References:** `<6715dh$g7$1@newsfep3.sprintmail.com>`

```


Jim Gallagher wrote:

› In systems that require Y2K work - is COBOL 74 or COBOL 85 the most common.
› What are your experiences ?

NEITHER! Y2K projects generally use the SAME languageas the problem code,
although some convert to a totally different language.

MOST Y2K problems have NOTHING to do with the language. They are program code
that is wrong. Storing or entering 2 digit years, for example. Some programs
tie directly to SQL type databases(most hopefully WON'T have the problem), and
so conversions should be easier(if even needed). VB is a good example of one
such language.

The way to correct it? That can vary greatly even in the same company.

› 
› 
…[6 more quoted lines elided]…
› jim··.@fre··l.us
```

#### ↳ Re: Is ANSI 85 COBOL the most common version in Y2K projects ?

- **From:** "willy weisz" <ua-author-6589000@usenetarchives.gap>
- **Date:** 1997-12-14T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc8768a3ff-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6715dh$g7$1@newsfep3.sprintmail.com>`
- **References:** `<6715dh$g7$1@newsfep3.sprintmail.com>`

```

The right version of COBOL for tackling the Y2K problems is COBOL 85
with
the ISO/ANSI standard "Intrinsic Functions" extensions. There are
already
compilers around incorporating those.

Regards

Willy

Jim Gallagher wrote:
› 
› In systems that require Y2K work - is COBOL 74 or COBOL 85 the most common.
…[8 more quoted lines elided]…
› jim··.@fre··l.us

------------------------------------------------------------------------------
Willy Weisz

Technische Universitaet Wien         Vienna University of Technology
EDV-Zentrum                          Computing Services
Hochleistungsrechnen                 High Performance Computing

                       Wiedner Hauptstrasse 8-10
                       A-1040 Wien

Tel: (+43 1) 588 01 - 5818                  Fax: (+43 1) 587 42 11
                     e-mail: we··.@edv··c.at
```

#### ↳ Re: Is ANSI 85 COBOL the most common version in Y2K projects ?

- **From:** "troxle..." <ua-author-8415077@usenetarchives.gap>
- **Date:** 1997-12-14T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc8768a3ff-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6715dh$g7$1@newsfep3.sprintmail.com>`
- **References:** `<6715dh$g7$1@newsfep3.sprintmail.com>`

```

"Jim Gallagher" wrote:

› In systems that require Y2K work - is COBOL 74 or COBOL 85 the most common.
› What are your experiences ?
›

Cobol LE/370 (Language Environment for MVS & VM) is the ONLY version
of IBM Cobol (for MVS and VM) that it is touting as Y2K compliant by
IBM.

IBM will patch users of Cobol II ('85) to be Y2K compliant, but are
not guarenteeing compliancy.


Tim Oxler
TEO Computer Technologies Inc.
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

#### ↳ Re: Is ANSI 85 COBOL the most common version in Y2K projects ?

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc8768a3ff-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6715dh$g7$1@newsfep3.sprintmail.com>`
- **References:** `<6715dh$g7$1@newsfep3.sprintmail.com>`

```

In article <6715dh$g7$1.··.@new··l.com>, "Jim Gallagher"
writes:

› In systems that require Y2K work - is COBOL 74 or COBOL 85 the most
› common. What are your experiences ?

In the IBM VSE/ESA arena, the VS COBOL _compiler_ ("FCOBOL", the '74 standard)
is not supported past December 31, 1999. Even the COBOL II _compiler_ ('85
standard, without the intrinsic library) is not officially supported after
December 31, 1999. The object code, from what I can decipher from the
announcements, will be supported if they were compiled using the RES option
(for COBOL II) and the Languange Envirnment ("LE") libraries are installed.

The only IBM VSE/ESA COBOL _compiler_ that will be supported after December 31,
1999, as far as I can tell from the announcements and teleconferences, will be
COBOL for VSE with the LE libraries. And even today one cannot order the VS
COBOL compiler, and the COBOL II compiler is either not orderable or soon will
be.

Since the older announcements implied that even the object code wouldn't be
supported after December 31, 1999, we had decided that our COBOL code would be
changed to COBOL for VSE. Now that IBM had said they will support object code
from the other compilers, but not the compilers themselves, our decision to go
with COBOL for VSE is unchanged because it is likely that we will have at least
a few programs that we will end up recompiling after December 31, 1999, if for
no other reasons, because of changing business requirements.

The COBOL for VSE compiler includes the optional intrinsic library support and
full support for the Language Environment, both of which provide some tools
that are not available under the previous COBOLs (e.g., getting 4-digit years
via either FUNCTION CURRENT-DATE or a LE call; sliding windows implementation
via LE calls).

We have two major software vendors who are likewise moving to COBOL for VSE and
COBOL for MVS & VM for similar reasons, plus they apparently don't want to cut
off new sales. (E.g., if their code isn't compilable with COBOL for VSE, and a
shop doesn't have a COBOL compiler, they would be locked out of a vendor that
has only the old COBOL compiler compatible code.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
