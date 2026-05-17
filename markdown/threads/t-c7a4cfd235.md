[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NUMBER FACTORIAL COMPUTING

_3 messages · 3 participants · 1997-01_

---

### NUMBER FACTORIAL COMPUTING

- **From:** "10623..." <ua-author-17073582@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5avu7q$3jc$1@mhafc.production.compuserve.com>`

```

Does anybody knows how to compute the factorial of a number in
COBOL?.

Is there any COBOL compiler with such arithmetic function? or ...

Should one write its own routine?.

Thanks.

Luis Gomez
106··.@Com··e.Com
```

#### ↳ Re: NUMBER FACTORIAL COMPUTING

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7a4cfd235-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5avu7q$3jc$1@mhafc.production.compuserve.com>`
- **References:** `<5avu7q$3jc$1@mhafc.production.compuserve.com>`

```

On 8 Jan 1997 10:51:38 GMT, Luis Gomez Mira
<106··.@Com··e.COM> wrote:

› Does anybody knows how to compute the factorial of a number in
› COBOL?.

Is this a do-my-homework or I didn't do the research thing?

n! is all the whole numbers from 1 to n multiplied together. For
example, 4! is 1 * 2 * 3 * 4. If you can't come up with a routine, I
see something wrong somewhere.
```

#### ↳ Re: NUMBER FACTORIAL COMPUTING

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7a4cfd235-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5avu7q$3jc$1@mhafc.production.compuserve.com>`
- **References:** `<5avu7q$3jc$1@mhafc.production.compuserve.com>`

```

Luis Gomez Mira wrote:
› 
› Does anybody knows how to compute the factorial of a number in
…[8 more quoted lines elided]…
› --

Any modern standard-conforming COBOL compiler has the intrinsic
function FACTORIAL. This was added to the language in 1989. Like
'COMPUTE whatever = FUNCTION FACTORIAL (the-number)'. However, IBM
COBOL II does not have functions, so if you are stuck on that you are
out of luck.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
