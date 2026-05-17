[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol II question

_5 messages · 5 participants · 1995-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Cobol II question

- **From:** "ainco..." <ua-author-17086364@usenetarchives.gap>
- **Date:** 1995-12-15T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4auhhp$fo8@newsbf02.news.aol.com>`

```
Here's a basic cobol ii question, I hope someone can help with? It seems
simple but is driving us crazy; please help.

If I pass a one byte comp-3 data element from a VS Cobol program to a
Cobol II release 4 module and than set the field to zero via a move or
init statement; I am getting an OC7 abend on return to the VS Cobol module
when I access the data element. The field returned is x'F0' rather than
x'0C'. Simple or am I completely off the wall...please, please help. I
believe I have done this before at another site with no problem. Is there
some sort of compiler option I am missing??? Thanks.
```

#### ↳ Re: Cobol II question

- **From:** "scom..." <ua-author-2666089@usenetarchives.gap>
- **Date:** 1995-12-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f22f7f1bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4auhhp$fo8@newsbf02.news.aol.com>`
- **References:** `<4auhhp$fo8@newsbf02.news.aol.com>`

```
On 15 Dec you write:

› Here's a basic cobol ii question, I hope someone can help with?  It seems
› simple but is driving us crazy; please help.
 
› If I pass a one byte comp-3 data element from a VS Cobol program to a
› Cobol II release 4 module and than set the field to zero via a move or
…[6 more quoted lines elided]…
› some sort of compiler option I am missing???  Thanks.

My first thought was a compiler option, but on second reading I would
first check your called program definition of the passed field. It looks
like you are declaring the field like this:

Linkage-section.
01 Passed-field pic x.

Then, if you Move Zeros to Passed-field, you will have a character zero in
the field on return to the calling program. Try changing your definition
to something like this:

Linkage-section.
01 Passed-field pic s9 packed-decimal.

Then, Move Zeros to Passed-field will put a packed-decimal zero (X'0C')
into the field.

Regards,



Steve Comstock
Denver, Colorado
USA

telephone: 800-993-8716
or: 303-393-8716
fax: 303-393-8718
e-mail: sco··.@a··.com
```

#### ↳ Re: Cobol II question

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1995-12-15T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f22f7f1bc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4auhhp$fo8@newsbf02.news.aol.com>`
- **References:** `<4auhhp$fo8@newsbf02.news.aol.com>`

```
I beleive that Steve's response is correct. VS COBOL II can do strange
things with decimal data (comp-3 and display), both of which can be
affected by NUMPROC and ZWB options, but this does not sound like one of
the case.

If the Steve's suggestion does not deal witb the problem, post the source
code fragments - calling program data and CALL, receiving program linkage
section and procedure devision header.

One other thought that has yeilded strange results. Use of multiple entry
points in the CALLed routine, and entering at the incorrect one.
```

#### ↳ Re: Cobol II question

- **From:** "wein..." <ua-author-15050514@usenetarchives.gap>
- **Date:** 1995-12-16T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f22f7f1bc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4auhhp$fo8@newsbf02.news.aol.com>`
- **References:** `<4auhhp$fo8@newsbf02.news.aol.com>`

```
It almost sounds like the subroutine defines the field as PIC 9(01) [USAGE IS DISPLAY]. Then
the MOVE ZERO TO .... would initialize the field to x'F0'. Better check it out.

Howard D. Weiner
Chief Technologist and Imagineer
The Number Company, Inc.

wei··.@the··o.com
www.thenumberco.com
```

#### ↳ Re: Cobol II question

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1995-12-16T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f22f7f1bc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4auhhp$fo8@newsbf02.news.aol.com>`
- **References:** `<4auhhp$fo8@newsbf02.news.aol.com>`

```
ain··.@a··.com (AIncorvaia) wrote:

› Here's a basic cobol ii question, I hope someone can help with? It seems
› simple but is driving us crazy; please help.

you didn't describe the picture of the call'ed module.(mixing
languages versions make the linker very happy also)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
