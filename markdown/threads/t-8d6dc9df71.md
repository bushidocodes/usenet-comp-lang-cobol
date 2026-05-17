[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Extracting COBOL compiler options from a load module

_3 messages · 3 participants · 1997-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Extracting COBOL compiler options from a load module

- **From:** "igor gindler" <ua-author-17071923@usenetarchives.gap>
- **Date:** 1997-10-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63arrq$a12@mid.way.com>`

```

Recently I wrote a REXX procedure to extract CSECTs and
compiler options from Cobol 2, Cobol/370, and Cobol for
MVS&VM load modules, but my boss asked me to do the same
against OS VS Cobol 1 modules. (The reason is we have
a lot of old Cobol 1 programs still in production, but
must migrate to Cobol for MVS).

The problems are:
1. As I remember, the internal structure of Cobol 1 object
modules are based on so ancient ideas, and may not
contain compiler options.
2. 15-20 years old IBM manuals are unavailabe.
3. There are no such thing like Nelsons's book "COBOL 1" or
Bookman's book "COBOL 1".

I'll be glad to get any suggestions/comments.

Regards,

Igor
```

#### ↳ Re: Extracting COBOL compiler options from a load module

- **From:** "scottp4-remove..." <ua-author-2777696@usenetarchives.gap>
- **Date:** 1997-10-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d6dc9df71-p2@usenetarchives.gap>`
- **In-Reply-To:** `<63arrq$a12@mid.way.com>`
- **References:** `<63arrq$a12@mid.way.com>`

```

Igor Gindler wrote:

› Recently I wrote a REXX procedure to extract CSECTs and 
› compiler options from Cobol 2, Cobol/370, and Cobol for 
…[12 more quoted lines elided]…
› 

Two suggestions. Rather than extract the CSECTS, etc. just relink the
module and the parse the linkage editor map.

As far as VS-COBOL versions 1 and 2, there was a control block that
contained the some of the compile options that had run-time issues.
After this long I have no idea what it was. You might look around.
Up to VS-COBOL 2.3 source and logic manuals were available that
documented these control blocks. Someone might have a copy you could
look at.

Scott Peterson
```

#### ↳ Re: Extracting COBOL compiler options from a load module

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-10-31T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d6dc9df71-p3@usenetarchives.gap>`
- **In-Reply-To:** `<63arrq$a12@mid.way.com>`
- **References:** `<63arrq$a12@mid.way.com>`

```

Why re-invent the wheel. The Edge Portfolio Analyzer does this for you.
Look for details at http://www.edge-information.com

Lots of variation in these old compilers, especially when combined with
various optimizers and other add-ons.

About 66% of the signficant options are normally recoverable. Several
signficant ones are not currently recoverable by any known technique. One
of the more interesting is the TRUNC option. With olde compilers, no bit
is left around to indicate the presence of the option. Object code
analysis can not be done conclusively, since one verb with TRUNC could
produce identical results / code for multiple verbs with NOTRUNC specified.

01 TARGET PIC S999 COMP.
01 RESULT PIC S9(8) COMP.

MOVE +999 TO RESULT
ADD +1 TO RESULT GIVING TARGET
DIVIDE TARGET BY 1000 REMAINDER TARGET

The ADD with TRUNC will generate the same code as the ADD and DIVIDE with
NOTRUNC.
Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
