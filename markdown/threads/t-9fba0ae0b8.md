[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# S0C4???

_6 messages · 6 participants · 1998-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### S0C4???

- **From:** "michael" <ua-author-11118@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35055D87.3B62@somewhere.com>`

```

Bob Wolfe wrote:
› 
› "rom reeves"  wrote:
…[25 more quoted lines elided]…
› 

You forgot the most important question:

What is a S0C4?

A. To keep your foot warm.


Sorry. I couldn't resist.

Mike
```

#### ↳ Re: S0C4???

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9fba0ae0b8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35055D87.3B62@somewhere.com>`
- **References:** `<35055D87.3B62@somewhere.com>`

```

Michael wrote:
› 
› Bob Wolfe wrote:
…[11 more quoted lines elided]…
› Mike

What?!? You mean I've been wrong all these years? I thought it was
special footware for alien beings....
```

##### ↳ ↳ Re: S0C4???

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9fba0ae0b8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9fba0ae0b8-p2@usenetarchives.gap>`
- **References:** `<35055D87.3B62@somewhere.com> <gap-9fba0ae0b8-p2@usenetarchives.gap>`

```

All of a sudden, Joe Zitzelberger
wrote:

› Michael wrote:
›› 
…[15 more quoted lines elided]…
› special footware for alien beings....

Oh no. That's changed (part of the year 2000 conversion)....

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

##### ↳ ↳ Re: S0C4???

- **From:** "sink..." <ua-author-13506402@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9fba0ae0b8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9fba0ae0b8-p2@usenetarchives.gap>`
- **References:** `<35055D87.3B62@somewhere.com> <gap-9fba0ae0b8-p2@usenetarchives.gap>`

```

In article <350··.@not··s.com>, joe··.@not··s.com wrote:
› Michael wrote:
›› 
…[15 more quoted lines elided]…
› special footware for alien beings....

A s0C4 is like a GPF (general protection fault) in personal computer terms.
A program has attempt to execute in an area of memory which is reserved by the
operating system for other programs and/or processes; such as the operating
system itself.


Gerald P. Sinkiewicz
E-mail sin··.@ti··c.net
```

###### ↳ ↳ ↳ Re: S0C4???

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9fba0ae0b8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9fba0ae0b8-p4@usenetarchives.gap>`
- **References:** `<35055D87.3B62@somewhere.com> <gap-9fba0ae0b8-p2@usenetarchives.gap> <gap-9fba0ae0b8-p4@usenetarchives.gap>`

```

Gerry Sinkiewicz wrote:
(snip)
special footware for alien beings....

› A s0C4 is like a GPF (general protection fault) in personal computer terms.
› A program has attempt to execute in an area of memory which is reserved by the
› operating system for other programs and/or processes; such as the operating
› system itself.

(I'm winging this without any doc to check - apologies in advance if I have it
twisted) Trying to alter someone else's memory causes a protection exception, S0C5,
rather than a S0C4. Referencing unallocated virtual storage causes a S0C4.

HTH,
Bill Lynch


›
›
› Gerald P. Sinkiewicz
› E-mail sin··.@ti··c.net
```

###### ↳ ↳ ↳ Re: S0C4???

_(reply depth: 4)_

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9fba0ae0b8-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9fba0ae0b8-p5@usenetarchives.gap>`
- **References:** `<35055D87.3B62@somewhere.com> <gap-9fba0ae0b8-p2@usenetarchives.gap> <gap-9fba0ae0b8-p4@usenetarchives.gap> <gap-9fba0ae0b8-p5@usenetarchives.gap>`

```

On Wed, 11 Mar 1998 21:02:28 -0500 Bill Lynch
wrote:

:>Gerry Sinkiewicz wrote:
:>(snip)
:>special footware for alien beings....

:>> A s0C4 is like a GPF (general protection fault) in personal computer terms.
:>> A program has attempt to execute in an area of memory which is reserved by the
:>> operating system for other programs and/or processes; such as the operating
:>> system itself.

:>(I'm winging this without any doc to check - apologies in advance if I have it
:>twisted) Trying to alter someone else's memory causes a protection exception, S0C5,
:>rather than a S0C4. Referencing unallocated virtual storage causes a S0C4.

Geek Alert:

A S0C4 is one of the following: a PIC04, PIC10 or PIC11:

PIC04 - Storage exists, but current key does not allow fetch/store. Also may
occur with low memory protection even in key 0.

PIC11 - Page is not in real storage. If page does not exist, the control
program will generate an S0C4.

PIC10 - Segment is not in real storage. If segment does not exist, the control
program will generate an S0C4.

A S0C5 is a PIC05 which will only occur in real mode where the referenced
storage address does not exist. In MVS all virtual addresses exist. Will not
occur in a COBOL program.

An illegal attempt to modify storage owned by another job in MVS will either
fail with a PIC04 if the offending job has authorization to access some
storage in the target job or will fail with one of the various exceptions
while attempting to connect to target job.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
