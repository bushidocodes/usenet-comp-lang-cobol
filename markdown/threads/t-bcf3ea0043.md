[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Just a question

_4 messages · 4 participants · 1998-01_

---

### Just a question

- **From:** "dan jezek" <ua-author-1256453@usenetarchives.gap>
- **Date:** 1998-01-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34CAB19F.DF062343@pixi.com>`

```

What would be a reasonable starting rate for a recent college graduate
with no working experience in the COBOL field, but knowledge in the
following:

Writing structured COBOL programs on the MVS/ESA Mainframe
JCL
TSO
VSAM Files
CICS

-- Dan
dan··.@pi··i.com
http://www.pixi.com/~danjezek/index.html
```

#### ↳ Re: Just a question

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcf3ea0043-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34CAB19F.DF062343@pixi.com>`
- **References:** `<34CAB19F.DF062343@pixi.com>`

```

Dan Jezek wrote:
› 
› What would be a reasonable starting rate for a recent college graduate
…[11 more quoted lines elided]…
› http://www.pixi.com/~danjezek/index.html

I copied the following from "MVS JCL Reference", "Coding Symbols in
JCL", 5.4.3 (doc no. IEA1B601), on IBM's online doc site:

"Rules for Coding Symbols in JCL: Follow these rules when coding symbols
in JCL:

1. Do not code EXEC statement parameter and subparameter keywords as
names for JCL symbols.

Example: Do not code ®ION=200K or REGION=®ION correctly code
REGION=&SIZE.

2. Do not code DD or JOB statement keywords as JCL symbols in procedures
or jobs that are started by a START command from the operator console.
This rule includes the following obsolete keywords:

AFF
SEP
SPLIT
SUBALLOC

| This rule also includes DCB subparameters. For example, do not
use
| the following DCB subparameters as symbol values:

| BFALN

| LRECL

| For a complete list of DCB subparameters, see "DCB Subparameters"
in
| topic 12.20.5"

You're right, SEP= is obsolete. I started with the following link,
http://www.s390.ibm.com/os390/bkserv/os390/bop1_srch.html, which takes
you to a search of IBM online doc.

HTH,
Bill Lynch
```

##### ↳ ↳ Re: Just a question

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcf3ea0043-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bcf3ea0043-p2@usenetarchives.gap>`
- **References:** `<34CAB19F.DF062343@pixi.com> <gap-bcf3ea0043-p2@usenetarchives.gap>`

```

Dan, don't worry about the cryptic nature of Bill's "answer" to
your question. He meant it as a reply to Paul Knudsen's post:

› This isn't a homework question, just something I'm curious about....
› 
…[5 more quoted lines elided]…
› latest JCL reference.  Is it obselete


With any luck it (Bill's post) will stick around Deja News for
millennia for the amusement of all.

TschÃ¼s!
Rick Anderson
Seattle
ricka Â»atÂ« pobox Â»fullstopÂ« com

=============================================================
On Sun, 25 Jan 1998 00:44:16 -0500, Bill Lynch
wrote:

› Dan Jezek wrote:
›› 
…[52 more quoted lines elided]…
› Bill Lynch
```

#### ↳ Re: Just a question

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcf3ea0043-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34CAB19F.DF062343@pixi.com>`
- **References:** `<34CAB19F.DF062343@pixi.com>`

```

All of a sudden, Dan Jezek wrote:

› What would be a reasonable starting rate for a recent college graduate
› with no working experience in the COBOL field, but knowledge in the
…[10 more quoted lines elided]…
› http://www.pixi.com/~danjezek/index.html
I think that really depends on where you are located. In the midwest,
you should be in the neighborhood of $35k/yr (give or take, but that
should be close). In a bigger market, it should be a bit more...

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
