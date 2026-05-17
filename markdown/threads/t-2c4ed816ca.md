[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Paragraphs vs. Sections - Performance under DEC COBOL/VMS

_2 messages · 2 participants · 1995-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Paragraphs vs. Sections - Performance under DEC COBOL/VMS

- **From:** "jbu..." <ua-author-17087951@usenetarchives.gap>
- **Date:** 1995-08-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4234e0$h29@clarknet.clark.net>`

```
We are in the process of tuning several programs written in DEC COBOL 5.0
under OpenVMS/VAX. I was informed by a colleague that using sections
instead of paragraphs will reduce the working set requirements of the
program, which is one of the performance goals we are trying to achieve.

I am getting ready to profile two programs which are identical except
that one is written with paragraphs, while the other is written with
sections. However, I am looking for any kind of information that
will help validate (or invalidate) the earlier statement made by my
colleague (and maybe save me some time).

Thanks in advance!
```

#### ↳ Re: Paragraphs vs. Sections - Performance under DEC COBOL/VMS

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-08-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2c4ed816ca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4234e0$h29@clarknet.clark.net>`
- **References:** `<4234e0$h29@clarknet.clark.net>`

```
In article <4234e0$h.··.@cla··k.net>
jbu··.@cl··k.net (Joseph Anthony Bunag) writes:

› 
› We are in the process of tuning several programs written in DEC COBOL 5.0
…[10 more quoted lines elided]…
› Thanks in advance!
I would caution you NOT to use sections, because of the possible
fall thru logic traps. (violates structured programming principle
of one entry, one exit...

Sections supercede paragraphs. Sections contain Paragraphs while
para contain statements.

Suppose you mix paragraphs (or forget to put SECTION keyword)
And you perform the following:

Perform my-favorite-sect.

my-favorite-sect section.

move stuff to ws-stuff.
add 1 to ws-counter.
....

ten-worst-abends-para.
open file-again-erroneously.

Yet-another section.

The perform of my-favorite-sect section grinds thru to ten-worst-abends-para
(not what I intended). I used to run into this when sorts required sections.
Ending up doing perform thru's and dummy sections...

Ugly.
Just say know to fall-thru code...


Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
