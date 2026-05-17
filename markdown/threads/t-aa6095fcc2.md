[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need some intuition here --- sections in the procedure division

_78 messages · 12 participants · 2018-09 → 2018-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-26T23:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
Hello:

Can any cobol guru provide some insights into sections in the procedure division: I don't see them used much in any of the cobol textbooks I own or any of the cobol code I see, and I'd like to understand why. They do have some interesting properties, and I can think of several reasons why I might want to use them. On the other hand, I can't imagine why people would avoid them. Can anyone suggest some reasons?

Thanks,

Mayer
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2018-09-27T09:17:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On Wed, 26 Sep 2018 20:29:12 -0700 (PDT), Mayer Goldberg
wrote:

› Hello:
›
› Can any cobol guru provide some insights into sections in the procedure division: I don't see them used much in any of the cobol textbooks I own or any of the cobol code I see, and I'd like to understand why. They do have some interesting properties, and I can think of several reasons why I might want to use them. On the other hand, I can't imagine why people would avoid them. Can anyone suggest some reasons?

Back in the days before virtual storage when there was limited memory
(for example I had fewer than 20,000 characters on the RCA 301 to work
with) this was a way of doing segmentation so that code could be
overlaid by specifying a high enough number on the section header
(over 50 could be overlaid). This way initialization processing could
be overlaid by end of job processing. Also initially SORT input and
output procedures had to be sections. For current day programs, my
opinion is that SECTIONS have little if any net value.

Clark Morris
›
› Thanks,
›
› Mayer
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "kerry.liles" <ua-author-7511031@usenetarchives.gap>
- **Date:** 2018-09-27T09:27:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On 9/26/2018 11:29 PM, Mayer Goldberg wrote:
› Hello:
› 
…[5 more quoted lines elided]…
› 

Not a guru but old enough to remember... hehe
As far as I recall, Procedure Division Sections were most often used to
facilitate the creation of 'overlays' (discreet chunks of code - think
of it as separate chunks created by the linker). These overlays could be
specified to map to the same area of memory (since they were sections
they were by definition not interconnected by GO TO or PERFORM or other
such connections).

This was all done to permit otherwise too large programs to run on all
of the memory-starved machines... For example, the initialization and
setup "section" could be separated from all the rest of the code and
once that section was completed, the memory it would otherwise occupy
and hold down was overlaid by subsequent sections of code. Arranging all
the code into 'sections' was a bit of an art in the sense that you had
to pre-arrange all of the Procedure division code into the appropriate
chunks based on use case etc: phase 1 (initializing stuff and getting
files open and workareas primed and ready), phase 2 (reading the input
file(s) and creating a perhaps temporary workfile for the next phase),
phase 3 (reading the workfile to create the report everyone was waiting
for).

I do recall spending a LOT of time in the early 70's manipulating large
programs into sections and fiddling with the DOS linker to make sure the
entire mess would run in a 64K (?) partition... those were the days all
right.

A lot of the point of this (memory conservation and management) went
away when machines started to have a decent amount of memory and
partitions were no longer so small... similar changes in real life
occurred when the amount of available disk space increased significantly
- sorting on tape was replaced by using disk work/output files etc. and
no more intermediate temporary files etc.

If there were other uses of Sections I am drawing a blank on that...
perhaps others will know. The above recollections are from using COBOL
on IBM DOS in the late 1960's and much of the 1970's on machines like
the IBM /360-30 /360-40. Others experience on other hardware might be
different.

Using SECTIONS these days is pretty much unheard of as near as I can
tell :) [still running COBOL on VSE under VM on a BC12 IBM z/OS machine]
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-27T14:51:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p3@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap>`

```
On Friday, September 28, 2018 at 1:27:57 AM UTC+12, Kerry Liles wrote:

›
› If there were other uses of Sections I am drawing a blank on that...

Apart from overlays, sections were used to enable the use of GO TO within a PERFORMed procedure. The PERFORM of a section lasted until the end of the section was reached, which was just before the next section header or end of program. There could be paragraph labels within the section so that GO TO could be used to jump around in any way the programmer thought of. You could also do PERFORM section THRU section if you really wanted to complexify your code.

By eliminating sections and THRU the use of GO TO is easily avoided.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-27T17:42:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p4@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap>`

```
Thanks to all who replied! This was very helpful to me!

The relationship between GO TO and sections in the procedure division is one of the reasons I thought of using sections. Another reason has to do with grouping related pieces of code (paragraphs), and in fact, stating that the internal paragraphs should not be accessed directly, and rather the entire section should be taken as a "black box".

Mayer

On Thursday, September 27, 2018 at 9:51:35 PM UTC+3, Richard wrote:
› On Friday, September 28, 2018 at 1:27:57 AM UTC+12, Kerry Liles wrote:
› 
…[5 more quoted lines elided]…
› By eliminating sections and THRU the use of GO TO is easily avoided.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-27T21:34:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p5@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap>`

```
In article ,
Mayer Goldberg wrote:
› Thanks to all who replied! This was very helpful to me!
›
› The relationship between GO TO and sections in the procedure division is
› one of the reasons I thought of using sections.

Any decent, sane, well-educated and properly-experienced COBOL programmer
will have learned that GO TO is permitted under three, and only three,
conditions:

1) Up to the paragraph-name which contains the GO TO being executed.

2) Down to the -EXIT paragraph THRU which any PERFORM refers. (note that
this also requires rigid adherance to PERFORM para-name THRU
para-name-exit)

3) To the program's ABEND routine.

There are no other acceptable uses for GO TO and attempts to employ GO TO
in any manner other than these three will cause your code to fail Prod
Review.

› Another reason has to do
› with grouping related pieces of code (paragraphs), and in fact, stating
› that the internal paragraphs should not be accessed directly, and rather
› the entire section should be taken as a "black box".

This is exactly a reason not to use SECTIONs. Code is written to be
maintained and anything that requires 'black boxing' - for example, the
calculation of compound interest - should be neither a paragraph nor a
SECTION.

(whoever dares to ask 'if it's neither a paragraph nor a SECTION then how
does the code get executed?' is brave)

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-28T01:47:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p6@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap> <gap-aa6095fcc2-p6@usenetarchives.gap>`

```
On Friday, September 28, 2018 at 1:34:12 PM UTC+12, doc··.@pa··x.com wrote:

› Any decent, sane, well-educated and properly-experienced COBOL programmer
› will have learned that GO TO is permitted under three, and only three,
› conditions:

That is 3 more than I would permit!
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-28T10:24:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p7@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap> <gap-aa6095fcc2-p6@usenetarchives.gap> <gap-aa6095fcc2-p7@usenetarchives.gap>`

```
On Friday, September 28, 2018 at 8:47:38 AM UTC+3, Richard wrote:
› On Friday, September 28, 2018 at 1:34:12 PM UTC+12, doc··.@pa··x.com wrote:
› 
…[4 more quoted lines elided]…
› That is 3 more than I would permit!

A go to to the top of the current paragraph (which doc permits :-) ) is useful for optimizing tail-recursive calls, which isn't something normally done in cobol, but which is useful, e.g., if you were to solve e.g., the towers of hanoi problem in cobol.

To optimize tail-calls in general, and not necessarily tail-recursive calls, would require a go to to other paragraphs (which doc does not permit), so I guess I'll just skip that optimization... Anyway, it's not very important in business programming.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 7)_

- **From:** "0robert.jones" <ua-author-14501639@usenetarchives.gap>
- **Date:** 2018-09-28T10:49:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p8@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap> <gap-aa6095fcc2-p6@usenetarchives.gap> <gap-aa6095fcc2-p7@usenetarchives.gap> <gap-aa6095fcc2-p8@usenetarchives.gap>`

```
On Friday, 28 September 2018 15:24:17 UTC+1, Mayer Goldberg wrote:
› On Friday, September 28, 2018 at 8:47:38 AM UTC+3, Richard wrote:
›› On Friday, September 28, 2018 at 1:34:12 PM UTC+12, doc··.@pa··x.com wrote:
…[9 more quoted lines elided]…
› To optimize tail-calls in general, and not necessarily tail-recursive calls, would require a go to to other paragraphs (which doc does not permit), so I guess I'll just skip that optimization... Anyway, it's not very important in business programming.

I should add that if GO TO is used within a section, it is highly inadvisable for it to be used to transfer control outside that section.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 8)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-28T10:57:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p9@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap> <gap-aa6095fcc2-p6@usenetarchives.gap> <gap-aa6095fcc2-p7@usenetarchives.gap> <gap-aa6095fcc2-p8@usenetarchives.gap> <gap-aa6095fcc2-p9@usenetarchives.gap>`

```
On Friday, September 28, 2018 at 5:49:44 PM UTC+3, 0ro··.@gm··l.com wrote:
› On Friday, 28 September 2018 15:24:17 UTC+1, Mayer Goldberg  wrote:
›› On Friday, September 28, 2018 at 8:47:38 AM UTC+3, Richard wrote:
…[12 more quoted lines elided]…
› I should add that if GO TO is used within a section, it is highly inadvisable for it to be used to transfer control outside that section.

Right. This makes perfect sense.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 8)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-28T14:54:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p9@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p3@usenetarchives.gap> <gap-aa6095fcc2-p4@usenetarchives.gap> <gap-aa6095fcc2-p5@usenetarchives.gap> <gap-aa6095fcc2-p6@usenetarchives.gap> <gap-aa6095fcc2-p7@usenetarchives.gap> <gap-aa6095fcc2-p8@usenetarchives.gap> <gap-aa6095fcc2-p9@usenetarchives.gap>`

```
On Saturday, September 29, 2018 at 2:49:44 AM UTC+12, 0ro··.@gm··l.com wrote:

› I should add that if GO TO is used within a section, it is highly inadvisable for it to be used to transfer control outside that section.

FTFY ;-)
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-27T21:21:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p12@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
In article <6e8ba507-d0be-4915-86be-e55··e@goo··s.com>,
Mayer Goldberg wrote:
› Hello:
› 
› Can any cobol guru provide some insights into sections in the procedure
› division: I don't see them used much in any of the cobol textbooks I own
› or any of the cobol code I see, and I'd like to understand why.

Short reason: there's no need for them (except when Site Standards require
their use, in which case my hourly rate just went up).

Longer reason: since code should be written so that it is maintainable and
fewer maintenance programmers are being trained in the use of Sections
then the use of Sections should be avoided.

› They do
› have some interesting properties, and I can think of several reasons why
› I might want to use them. On the other hand, I can't imagine why people
› would avoid them. Can anyone suggest some reasons?

'Interesting' is the very last reason to write a piece of code in a given
manner. Bulletproof code is boring. Write boring code.

DD
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-27T21:46:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p13@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
› Short reason: there's no need for them (except when Site Standards
› require their use, in which case my hourly rate just went up).
 
› Are they marked off as deprecated?
 
› Longer reason: since code should be written so that it is
› maintainable and fewer maintenance programmers are being trained in
› the use of Sections then the use of Sections should be avoided.

Not many programmers are being trained to use cobol, so by that reasoning...

Anyway, I'm trying to understand the language feature: Why it was introduced, how it was used, etc. I have old cobol books and already in the 1974 standard they're not used; They just appear in the syntax tables at the end of the book. So I was curious.

› 'Interesting' is the very last reason to write a piece of code in a
› given manner. Bulletproof code is boring. Write boring code.

I'm trying to learn. Thank you for your help.

Mayer

On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-30T01:38:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p13@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p13@usenetarchives.gap>`

```
In article <42513400-62e8-4a72-845a-263··6@goo··s.com>,
Mayer Goldberg wrote:
›› Short reason: there's no need for them (except when Site Standards
›› require their use, in which case my hourly rate just went up).
› 
› Are they marked off as deprecated?
 
› That's answered by the Standard.  Please do your own homework.
 
› 
›› Longer reason: since code should be written so that it is
…[3 more quoted lines elided]…
› Not many programmers are being trained to use cobol, so by that reasoning...

... the ones not being trained to use COBOL aren't being trained in the
use of SECTIONs, either.

[snip]

›› 'Interesting' is the very last reason to write a piece of code in a
›› given manner. Bulletproof code is boring. Write boring code.
›
› I'm trying to learn.

What you are trying to learn and what is best learnt might not be the same
things. What you have been taught here is 'there's no need for SECTIONs
(outside of some SORT involvements) and anyone whose site standard demands
SECTIONs will earn you more money.'

See how valuable?

› Thank you for your help.

You're most welcome.

DD
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-27T21:55:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p15@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
›› Another reason has to do with grouping related pieces of code
›› (paragraphs), and in fact, stating that the internal paragraphs
›› should not be accessed directly, and rather the entire section
›› should be taken as a "black box".
 
› This is exactly a reason not to use SECTIONs. Code is written to be
› maintained and anything that requires 'black boxing' - for example,
…[4 more quoted lines elided]…
› does the code get executed?' is brave)

I don't get this "brave" stuff, sorry: I'm here to learn, I'm not playing ego games, I asked a simple question in a relevant forum: What is the rationale for having a specific language feature (sections in the procedure division). The answer ought to be the rationale. Admonitions do not address the question.

Black boxing is never required for the code to function. It's a way of organizing code so that some parts are available for use but not for change. My question centers around the rationale behind the language feature, and I was trying to guess at and imagine what it could be useful for. I've seen many cobol books, but few of them give any kind of rationale as to why the standard is defined the way it is, so it would seem to me that falling back on the collective memory of experienced programmers would be the way to proceed.

The calculation of compound interest involves a simple formula. I don't know whether there is a function for raising numbers to a power, but if there isn't, then logarithms and the exponential function would be the way to go. A-priori, this seems to me like something I'd like to perform in a single COMPUTE statement, but you may have other ideas.

Mayer

On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "kerry.liles" <ua-author-7511031@usenetarchives.gap>
- **Date:** 2018-09-28T09:55:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p15@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap>`

```
On 9/27/2018 9:55 PM, Mayer Goldberg wrote:
››› Another reason has to do with grouping related pieces of code
››› (paragraphs), and in fact, stating that the internal paragraphs
…[12 more quoted lines elided]…
› 

Don't worry... DOC is just being DOC - he often plays the part of a
crusty curmudgeon but he has some very strong beliefs... hehe (and often
he is in fact correct).

› Black boxing is never required for the code to function. It's a way of organizing code so that some parts are available for use but not for change. My question centers around the rationale behind the language feature, and I was trying to guess at and imagine what it could be useful for. I've seen many cobol books, but few of them give any kind of rationale as to why the standard is defined the way it is, so it would seem to me that falling back on the collective memory of experienced programmers would be the way to proceed.
›
…[3 more quoted lines elided]…
›

COBOL supports the ** operator (exponentiation), so for example,
square root becomes A ** 0.5 and etc.


› On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
›› Hello:
…[6 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-28T10:30:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p16@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p16@usenetarchives.gap>`

```
› COBOL supports the ** operator (exponentiation), so for example,
› square root becomes A ** 0.5 and etc.

Right! I forgot this, but re-learned it last night.

I'm basically re-learning cobol, which I picked up for fun during my school days. Never used it for much but I was always attracted to its more eclectic features.

I do understand that cobol is a business language, and that this forum is filled with serious people for whom cobol is a tool and means of livelihood, and for whom someone who takes a curious liking to the language is annoying and irrelevant: Kind of like a kid who likes to play with a concrete mixer... I accept this with love, just as I accept cobol's lack of closures, higher-order functions, first-order continuations, and monads... â˜º and I am grateful for your help and insights in learning and re-learning this language.

Mayer




On Friday, September 28, 2018 at 4:55:26 PM UTC+3, Kerry Liles wrote:
› On 9/27/2018 9:55 PM, Mayer Goldberg wrote:
›››› Another reason has to do with grouping related pieces of code
…[38 more quoted lines elided]…
››
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-30T01:47:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p15@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap>`

```
In article ,
Mayer Goldberg wrote:
››› Another reason has to do with grouping related pieces of code
››› (paragraphs), and in fact, stating that the internal paragraphs
…[15 more quoted lines elided]…
› do not address the question.

The question was addressed, clearly and unambiguously, with 'there's no
need for them'. This might not have been the answer you expected... but
that's what Real Learning's about, not re-learning something you already
know.

› 
› Black boxing is never required for the code to function. It's a way of
› organizing code so that some parts are available for use but not for
› change.
 
› Code is written in response to a need. Needs change, code must change.
 
› My question centers around the rationale behind the language
› feature, and I was trying to guess at and imagine what it could be
› useful for.

They aren't useful. Stay away from them. Stay away from shops that have a
standard that demand you use them.

You've just been given valuable, applicable, professional advice. It isn't
what you expected. Such is Life.

› I've seen many cobol books, but few of them give any kind of
› rationale as to why the standard is defined the way it is, so it would
› seem to me that falling back on the collective memory of experienced
› programmers would be the way to proceed.
 
› The way to proceed is: Don't Use Sections.
 
› 
› The calculation of compound interest involves a simple formula. I don't
…[3 more quoted lines elided]…
› in a single COMPUTE statement, but you may have other ideas.

I have a few ideas born of experiences and those experiences include
working in shops where compound interest is calculated. It's different
from other calculations.

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-30T22:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p18@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap>`

```
On 30/09/2018 6:47 PM, doc··f@pa··x.com wrote:
› In article ,
› Mayer Goldberg   wrote:
…[60 more quoted lines elided]…
› 
Sorry Doc,

Nothwithstanding the high regard I have for you personally and the
respect for your experience, I strongly disagree.

SECTIONs are fine and serve several useful purposes.

So now the OP has two conflicting opinions from two people well
qualified to have an opinion...

Makes it hard, doesn't it?

Perhaps some independent thought and considering on the part of the OP
will be called for... :-)

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-30T22:38:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p19@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 30/09/2018 6:47 PM, doc··f@pa··x.com wrote:
›› In article ,
…[65 more quoted lines elided]…
› respect for your experience, I strongly disagree.

Two professionals with over a half-century experience between them don't
come to the same conclusions? Who could have heard of such a thing...
certainly not the King of England.

›
› SECTIONs are fine and serve several useful purposes.

Outside of the various SORT manipulations... is there any kind of
processing of which you are aware that can be performed by use of SECTIONs
and nothing else?

› 
› So now the OP has two conflicting opinions from two people well 
…[5 more quoted lines elided]…
› will be called for... :-)

What comes next... asking folks to do their own homework?

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-30T23:07:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p20@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap>`

```
On 1/10/2018 3:38 PM, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[79 more quoted lines elided]…
› 

No.

(leaving segmentation out of the argument as being obsolete...)

Is there any kind of computer processing YOU are aware of that can be
performed by use of COBOL and nothing else?

It's a loaded question, just like yours... :-)

›› 
›› So now the OP has two conflicting opinions from two people well
…[7 more quoted lines elided]…
› What comes next... asking folks to do their own homework?

Oh, I can't imagine ANYONE saying that in a friendly, helpful, forum
like this one...

Pete.


I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-10-01T09:26:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p21@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p21@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 1/10/2018 3:38 PM, doc··f@pa··x.com wrote:
›› In article ,
›› pete dashwood   wrote:
 
›› [snip]
 
››› SECTIONs are fine and serve several useful purposes.
›› 
…[5 more quoted lines elided]…
› No.
 
› Most gracious of you to contradict yourself so readily, Mr Dashwood.
 
› 
› (leaving segmentation out of the argument as being obsolete...)
› 
› Is there any kind of computer processing YOU are aware of that can be 
› performed by use of COBOL and nothing else?

When someone posts that 'COBOL is fine and serves several useful purposes'
this might be addressed.

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 7)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-10-01T09:39:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p22@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p21@usenetarchives.gap> <gap-aa6095fcc2-p22@usenetarchives.gap>`

```
On 10/01/2018 09:26 AM, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[25 more quoted lines elided]…
› 

It is and it does.

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 7)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-01T22:13:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p22@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p21@usenetarchives.gap> <gap-aa6095fcc2-p22@usenetarchives.gap>`

```
On 2/10/2018 2:26 AM, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[16 more quoted lines elided]…
› 
Most foolish of you to see a contradiction where none exists.

The fact that SECTIONS are not the ONLY way does not gainsay the
assertion that "SECTIONS are fine and serve several useful purposes".

I use SECTIONS to logically group my thoughts (and code) into localized
related "areas" of code. I like doing it like that but it certainly is
not a REQUIREMENT in order to reach a solution.

Rick pointed out that DECLARATIVES (which are far from obsolete) require
SECTIONs (I had forgotten about that...) but both of you have only
considered the use of SECTION as an instrument in COBOL code.

I see it more as the CODASYL committee described it when they proposed
it; a useful way of collecting related functions (paragraphs?) in COBOL.

Obviously, no minds are going to be changed here, and that's fine, but
please don't ascribe contradiction to me where there is none.

For me, writing SECTIONed code in COBOL adds value in a number of ways:

1. Easy to locate code connected with a particular function.
2. A consistent use of PERFORM. (I ALWAYS PERFORM a SECTION...)
3. Clarifying the relationship between mainline and supporting
subroutines. (see the sample in my original post...)

SECTIONS are fine and serve several useful purposes.
(BUT, they are not the ONLY way to do things...)

In the same way that you COULD write a book without chapters, you most
certainly CAN write a COBOL program without SECTIONs. But the choice of
whether you do or not is down to you.

If the desired results are obtained either way, then the program is
serving its purpose.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 8)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-10-01T22:34:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p24@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p21@usenetarchives.gap> <gap-aa6095fcc2-p22@usenetarchives.gap> <gap-aa6095fcc2-p24@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 2/10/2018 2:26 AM, doc··f@pa··x.com wrote:
›› In article ,
…[18 more quoted lines elided]…
› Most foolish of you to see a contradiction where none exists.

That's what a lot of the poopie-heads say... some day I'll find out the
process of reasoning behind it.

›
› The fact that SECTIONS are not the ONLY way does not gainsay the
› assertion that "SECTIONS are fine and serve several useful purposes".

Methods other than SECTIONs accomplish the same ends. What four reasons
can be givenn to justify writing the code in a different way that a) works
the same and b) comes out with the same results?

› Rick pointed out that DECLARATIVES (which are far from obsolete) require
› SECTIONs (I had forgotten about that...) but both of you have only
› considered the use of SECTION as an instrument in COBOL code.

One step at a time, Mr Dashwood... the original poster asked about
Procedure Division SECTIONs.

[snip]

› If the desired results are obtained either way, then the program is
› serving its purpose.

Of course... after all, the code will never need modification... and I am
the King of England.

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-10-01T06:54:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p20@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 10:38:10 PM UTC-4, doc··.@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
 
› [snip]
 
›› SECTIONs are fine and serve several useful purposes.
› 
› Outside of the various SORT manipulations... is there any kind of 
› processing of which you are aware that can be performed by use of SECTIONs 
› and nothing else?

DECLARATIVES require sections, can't work without them.

The requirement for SORT input and output procedures to be in sections was removed in COBOL 85.

Segmentation was removed in COBOL 2002.

Declaratives are all that remain.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-10-01T09:28:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p26@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p26@usenetarchives.gap>`

```
In article <06d6987b-fcaa-4ec5-af78-fb1··8@goo··s.com>,
Rick Smith wrote:
› On Sunday, September 30, 2018 at 10:38:10 PM UTC-4, doc··.@pa··x.com wrote:
›› In article ,
…[13 more quoted lines elided]…
› was removed in COBOL 85.
 
› Well, that's only thirty-some years ago... must'nt be hasty.
 
› 
› Segmentation was removed in COBOL 2002.
 
› Barely two decades! These modern kids...
 
› 
› Declaratives are all that remain.

Greatly appreciated, Mr Smith.

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-10-01T07:26:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p20@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap>`

```
On 09/30/2018 10:38 PM, doc··f@pa··x.com wrote:
›
›
› What comes next... asking folks to do their own homework?

One thing is certain. Given the nearsightedness of academia
no one asking a question about COBOL here is looking for help
with their homework.

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-10-01T09:30:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p28@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p28@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:
› On 09/30/2018 10:38 PM, doc··f@pa··x.com wrote:
›› 
…[5 more quoted lines elided]…
› with their homework.

I use 'homework' in the sense of
https://www.dictionary.com/browse/homework?s=t , 3: Thorough preparatory
study of a subject.

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 7)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-10-01T09:41:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p29@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap> <gap-aa6095fcc2-p20@usenetarchives.gap> <gap-aa6095fcc2-p28@usenetarchives.gap> <gap-aa6095fcc2-p29@usenetarchives.gap>`

```
On 10/01/2018 09:30 AM, doc··f@pa··x.com wrote:
› In article ,
› Bill Gunshannon   wrote:
…[12 more quoted lines elided]…
› 

Sorry, on USENET that usually refers to someone looking for someone
else to do their school assignments for them. A rather common practice
at one point in time. :-)

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T22:52:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p19@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p15@usenetarchives.gap> <gap-aa6095fcc2-p18@usenetarchives.gap> <gap-aa6095fcc2-p19@usenetarchives.gap>`

```
On Monday, October 1, 2018 at 3:31:25 PM UTC+13, pete dashwood wrote:

›
› SECTIONs are fine and serve several useful purposes.
›

In environment division, data division, sure, very useful.

In procedure division sections were required for various items: segmentation, sort procedures, perhaps a few others, but this is probably no longer so. They may be useful as descriptive headers for a group of related procedures, but no more so than a comment.

So in procedure division the only "useful purpose" is to allow GO TO when the section is performed. I don't find this "useful" and, in fact, find it quite the opposite.
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "0robert.jones" <ua-author-14501639@usenetarchives.gap>
- **Date:** 2018-09-28T10:19:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p32@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On Thursday, 27 September 2018 04:29:14 UTC+1, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer

They were particularly useful before the adoption of the COBOL 85 standard with its scope delimiters such as END-IF and END-PERFORM to avoid the perform para thru para construct. They are used to compartment related groups of paragraphs and statements into higher level logical elements with meaningful names for those logical groups for easier comprehension. It is not advisable to use them in a program already written with perform thru statements, where subsequent amendments may be made by programmers that do not remember that sections only end when another section is specified.
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-28T10:34:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p32@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap>`

```
I was SURE sections in the procedure division were used for grouping code! But then doc wrote that this wasn't a good enough reason to use them, which may be the case. I really have no idea. As weird as this seems to sound to some people here, I really do take a liking to this language and really do try to understand it, knowing full well that hardly anyone is ever going to use and modify the code I write in it.

Mayer

On Friday, September 28, 2018 at 5:19:09 PM UTC+3, 0ro··.@gm··l.com wrote:
› On Thursday, 27 September 2018 04:29:14 UTC+1, Mayer Goldberg  wrote:
›› Hello:
…[7 more quoted lines elided]…
› They were particularly useful before the adoption of the COBOL 85 standard with its scope delimiters such as END-IF and END-PERFORM to avoid the perform para thru para construct.  They are used to compartment related groups of paragraphs and statements into higher level logical elements with meaningful names for those logical groups for easier comprehension.  It is not advisable to use them in a program already written with perform thru statements, where subsequent amendments may be made by programmers that do not remember that sections only end when another section is specified.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-09-28T21:52:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p33@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap>`

```
On 9/28/2018 9:34 AM, Mayer Goldberg wrote:
› I was SURE sections in the procedure division were used for grouping code! But then doc wrote that this wasn't a good enough reason to use them, which may be the case. I really have no idea. As weird as this seems to sound to some people here, I really do take a liking to this language and really do try to understand it, knowing full well that hardly anyone is ever going to use and modify the code I write in it.
›
› Mayer
›

The reason few people use sections for code overlays is that modern
hardware has far more memory available, so there is no need to page in
or page out sections of your procedure division in order to fit into 64K
bytes of memory.

The whole point of COBOL is that it is a business accounting language.
Code is expected to be modified. Tax laws change every year. Business
rules change every year. Therefore, having code that (in theory) is
easy to read and understand would make it easier for a different author
to modify the code.

One problem for anyone learning COBOL is that it's difficult to find
good, free samples of COBOL code to read. Businesses generally consider
their COBOL code to be proprietary, and don't like to just share it.

Here are some resources for example programs in COBOL:


https://open-cobol.sourceforge.io/faq/index.html

https://open-cobol.sourceforge.io/faq/gcfaq.html#rosetta-code

http://rosettacode.org/wiki/Category:COBOL

https://open-cobol.sourceforge.io/faq/gcfaq.html#what-about-gnucobol-and-benchmarks

http://speleotrove.com/decimal/telco.html

Kind Regards,


https://www.arnoldtrembley.com/

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-28T22:32:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p34@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap>`

```
Arnold Trembley wrote:

› On 9/28/2018 9:34 AM, Mayer Goldberg wrote:
›› I was SURE sections in the procedure division were used for grouping
…[12 more quoted lines elided]…
› bytes of memory.
IIRC, 52K; the other 8K was taken up by OS/360. :->
Leslie
› 
› The whole point of COBOL is that it is a business accounting language.
…[25 more quoted lines elided]…
› 

JLT
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-09-29T09:06:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p34@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap>`

```
On 09/28/2018 09:52 PM, Arnold Trembley wrote:
›
›
…[3 more quoted lines elided]…
›

Which is, of course, also the reason people get to spread the myth
that COBOL is dead. Just because no one announces they are using
it doesn't make it so. I know of at least one whole OS that has
the same quandary.

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T09:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p34@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap>`

```
Thanks for the code samples! This will be very helpful.

Mayer

On Saturday, September 29, 2018 at 4:52:37 AM UTC+3, Arnold Trembley wrote:
› On 9/28/2018 9:34 AM, Mayer Goldberg wrote:
›› I was SURE sections in the procedure division were used for grouping code! But then doc wrote that this wasn't a good enough reason to use them, which may be the case. I really have no idea. As weird as this seems to sound to some people here, I really do take a liking to this language and really do try to understand it, knowing full well that hardly anyone is ever going to use and modify the code I write in it.
…[40 more quoted lines elided]…
› https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T20:08:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p38@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p37@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap> <gap-aa6095fcc2-p37@usenetarchives.gap>`

```
On 30/09/2018 1:09 AM, Mayer Goldberg wrote:
› Thanks for the code samples! This will be very helpful.
›
› Mayer

It has been my experience across many different programming languages
and platforms that examining examples and reading conceptual background
can only take you so far...

The best way to come to grips with a new language or programming
paradigm is to change some code written in it or to start writing your
own simple programs.

(Programming success, like many things in life, requires intangibles
like confidence as well as practical skills... Confidence comes from
action rather than thought...)

Part of my job across the years has been to effect "skills transfer".
(What this really means is that people who are paying serious money for
my time, actually want to extract something tangible that remains after
I've gone... :-)) In my early years I trained as a teacher so you'd
think I wouldn't have any trouble passing knowledge on to others.

But, everybody is different and people learn differently. Some people
respond really well to pictures and charts, others struggle with it
until you show them a code snippet and then the light goes on.

If you found the code helpful then the time to write it was well spent.

I wish you well with your COBOL programming.



Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T07:20:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p39@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p38@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap> <gap-aa6095fcc2-p37@usenetarchives.gap> <gap-aa6095fcc2-p38@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 3:08:37 AM UTC+3, pete dashwood wrote:
› On 30/09/2018 1:09 AM, Mayer Goldberg wrote:
›› Thanks for the code samples! This will be very helpful.
…[34 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

Most of my time is spent on actual programming. But when I study a language I like to compare it to languages I already know and think hard about the differences. So I'll explain why I seem obsessive about sections in the procedure division --- this is something I've been thinking about, on and off, since I first noticed this in the 1980's, when I took my first cursory look at cobol: People criticise cobol for being in the spaghetti business for supposedly misusing GO TO with reckless abandon. :-) I don't need to tell you, in a forum of other cobol programmers, that this hasn't been true for years, and that cobol programming practices, more than in other languages, are rigidly controlled/policed on the grounds that the code must be understood by others, be easy to debug, etc. So in fact, cobol programs written for the 1985 standard or later, tend to be relatively free of unrestricted GO TOs. But what I realized was that GO TO to sections actually RETURNED at the end of the section. This means that GO TO to sections were not really unconditional jumps in the Dijkstra sense, but rather curious control operators that are more similar to PERFORM ... THRU for paragraphs. Now I don't use PERFORM ... THRU, so I won't be using GO TO to sections. But the similarity was curious. The books I read just laid out the standard, censored a bit for "bad practices", and gave no reasoning as to the design issues. Most cobol programmers I knew at the time had no idea that go to to a section returned at the end of the section... In fact, they had never heard of sections in the procedure division, or have heard but have never used them. So I knew there's an issue here, that there's some rationale I'm not getting.

So to wrap things up, I think it's important to know one's tools: If I see this little button over here, and I ask "what's it for" and I get the answer "oh, just ignore that button; we don't use it", OF COURSE I'm not going to be satisfied, no matter how good the advice, until I know what this little button is for... This does not mean that I'm eager to press it... In fact, I find the question itself, as to why I'm interested in this button, to be curious and raise more questions than simply to give a direct answer.

But in the end, I think that cobol is quaint and subtle, with many "interesting buttons" that do surprising things. I'm happy to learn this, and many people, especially in the academia, seem to be ignorant of this.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 7)_

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-09-30T14:01:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p40@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p39@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p34@usenetarchives.gap> <gap-aa6095fcc2-p37@usenetarchives.gap> <gap-aa6095fcc2-p38@usenetarchives.gap> <gap-aa6095fcc2-p39@usenetarchives.gap>`

```
On Sun, 30 Sep 2018 04:20:17 -0700 (PDT), Mayer Goldberg
wrote:



› But what I realized was that GO TO to sections actually RETURNED at the end of the section.
› This means that GO TO to sections were not really unconditional jumps in the Dijkstra sense, but rather curious control operators that are more similar to PERFORM ... THRU for paragraphs. Now I don't use PERFORM ... >THRU, so I won't be using GO TO to sections.



My understanding is that if you PERFORM a section, it returns at the
end of the section or when EXIT SECTION is executed.

If you GO TO a section, I don't think it returns; I believe it would
continue to the next section, if any. So don't GO TO a section. :)

I'm ready to stand corrected.

Louis
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-30T01:50:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p41@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p33@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap>`

```
In article <97d64a9a-b76d-4aef-b148-296··1@goo··s.com>,
Mayer Goldberg wrote:
› I was SURE sections in the procedure division were used for grouping
› code!

Your certainty might have been based on faulty reasoning. How did you come
to the conclusion?

DD
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T06:54:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p42@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p41@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 8:50:18 AM UTC+3, doc··.@pa··x.com wrote:
› In article <97d64a9a-b76d-4aef-b148-296··1@goo··s.com>,
› Mayer Goldberg   wrote:
…[6 more quoted lines elided]…
› DD

Here is my reasoning:

(1) Not knowing of overlays in cobol, they seem like a grouping mechanism because of the unique way GO TO works within section.

(2) Having learned about overlays, I discovered that only sections marked with priority number >= 50 are used for overlays. Others are not. This means there needs to be some purpose to having them.

(3) Today I found out that the Codasyl committee actually spelled out its reasoning:


"Although it is not mandatory, the Procedure Division for a source program is usually written as a consecutive group of sections, each of which is composed of a series of closely related operations that are designed to collectively perform a particular function. However s when segmentation is used, the entire Procedure Division must be in sections. In addition, each section must be classified as belonging either to the fixed portion or to one of the independent segments of the object program. Segmentation in no way affects the need for qualification of procedure-names to insure uniqueness."


[The source is the Codasyl Journal, p 331, section 8.1.2.1 "Program Segments"]

(4) I actually have Sammet's book on the history of programming languages, but I seem to have missed or not understood at the time the following comment by her:


The storage allocation is handled automatically by the compiler. The prime unit for allocating executable code is a group of sections called a segment. The programmer combines sections be specifying a priority number with each section's name. ... The compiler is required to see that the proper control transfers are provided so that control among segments which are not stored simultaneously can take place.


So there you have it --- Sections were intended as a mechanism for grouping related paragraphs. Such groups were intended to be loaded into memory as a group, so as to ensure efficient execution (in case of overlays).

The thing that caught my eyes back in the 1980's, when I first took a look at cobol, was that a GO TO to a section RETURNED at the end of the section. This means that go to to sections, rather than paragraphs, are NOT THE SAME as the goto statements referred to in e.g., Dijkstra's [in]famous admonotion, and that GO TO to a section really behaves like a PERFORM ... THRU.

The question as to whether I'll use these is not interesting to me at this point, even though you insist it's good for me to receive instruction on this. The question that does interest me is what is the meaning and intended purpose of sections in the procedure division. By now, with the help of the members here, and some digging around, I think I was able to obtains a sufficiently clear answer that explains the intention behind the standard. So a hearty Thank You goes to all who have responded, and now we can happily move on to programming and learning additional things.

Mayer
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:07:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p43@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p42@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap> <gap-aa6095fcc2-p42@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 11:54:23 PM UTC+13, Mayer Goldberg wrote:

›
› The thing that caught my eyes back in the 1980's, when I first took a look at cobol, was that a GO TO to a section RETURNED at the end of the section. This means that go to to sections, rather than paragraphs, are NOT THE SAME as the goto statements referred to in e.g., Dijkstra's [in]famous admonotion, and that GO TO to a section really behaves like a PERFORM ... THRU.
›

THAT IS NOT TRUE AT ALL.

A GO TO _TO_ A SECTION WILL _NOT_ RETURN.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T14:20:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p44@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p43@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap> <gap-aa6095fcc2-p42@usenetarchives.gap> <gap-aa6095fcc2-p43@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 9:07:28 PM UTC+3, Richard wrote:
› On Sunday, September 30, 2018 at 11:54:23 PM UTC+13, Mayer Goldberg wrote:
›  
…[6 more quoted lines elided]…
› A GO TO _TO_ A SECTION WILL _NOT_ RETURN.

I just checked this in gnu cobol, which is the only cobol I have at the moment, and you seem to be correct. I don't remember how and on what system I checked this on back then... :-( Thanks for your correction (same goes to Louis), which prompted me to re-test.

Mayer
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "0robert.jones" <ua-author-14501639@usenetarchives.gap>
- **Date:** 2018-09-30T14:21:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p45@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p43@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap> <gap-aa6095fcc2-p42@usenetarchives.gap> <gap-aa6095fcc2-p43@usenetarchives.gap>`

```
On Sunday, 30 September 2018 19:07:28 UTC+1, Richard wrote:
› On Sunday, September 30, 2018 at 11:54:23 PM UTC+13, Mayer Goldberg wrote:
›  
…[6 more quoted lines elided]…
› A GO TO _TO_ A SECTION WILL _NOT_ RETURN.

Also a go to out of a section does not terminate a performed section, problems would occur should the section be invoked while it still thinks it is being invoked. A section only terminates when it is exited properly, i.e. when there are no more statements in it to be executed. The end of a section is when a following section name defining a section is encountered or the end of the program is reached.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-09-30T17:44:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p46@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p43@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap> <gap-aa6095fcc2-p42@usenetarchives.gap> <gap-aa6095fcc2-p43@usenetarchives.gap>`

```
On 09/30/2018 02:07 PM, Richard wrote:
› On Sunday, September 30, 2018 at 11:54:23 PM UTC+13, Mayer Goldberg wrote:
›   
…[8 more quoted lines elided]…
› 

I've worked with a lot of different languages over my lifetime
and I have never seen a language that returned from a GOTO.

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-30T22:38:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p47@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p42@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p32@usenetarchives.gap> <gap-aa6095fcc2-p33@usenetarchives.gap> <gap-aa6095fcc2-p41@usenetarchives.gap> <gap-aa6095fcc2-p42@usenetarchives.gap>`

```
On 30/09/2018 11:54 PM, Mayer Goldberg wrote:
› On Sunday, September 30, 2018 at 8:50:18 AM UTC+3, doc··.@pa··x.com wrote:
›› In article <97d64a9a-b76d-4aef-b148-296··1@goo··s.com>,
…[18 more quoted lines elided]…
› "Although it is not mandatory, the Procedure Division for a source program is usually written as a consecutive group of sections, each of which is composed of a series of closely related operations that are designed to collectively perform a particular function.

How spookily similar to the code sample I posted... :-)

I remember reading the CODASYL standard soon after it was published....

However s when segmentation is used, the entire Procedure Division
must be in sections. In addition, each section must be classified as
belonging either to the fixed portion or to one of the independent
segments of the object program. Segmentation in no way affects the need
for qualification of procedure-names to insure uniqueness."
› 
› 
…[10 more quoted lines elided]…
› The thing that caught my eyes back in the 1980's, when I first took a look at cobol, was that a GO TO to a section RETURNED at the end of the section. 

I don't think it does.

Please show me a version of COBOL that behaves in this way...


This means that go to to sections, rather than paragraphs, are NOT THE
SAME as the goto statements referred to in e.g., Dijkstra's [in]famous
admonotion, and that GO TO to a section really behaves like a PERFORM
... THRU.

Not in my experience. (Although, to be fair, I have NEVER coded a GO TO
...SECTION.)
›
› The question as to whether I'll use these is not interesting to me at this point, even though you insist it's good for me to receive instruction on this. The question that does interest me is what is the meaning and intended purpose of sections in the procedure division. By now, with the help of the members here, and some digging around, I think I was able to obtains a sufficiently clear answer that explains the intention behind the standard. So a hearty Thank You goes to all who have responded, and now we can happily move on to programming and learning additional things.
…[3 more quoted lines elided]…
›

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T01:36:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p48@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On 27/09/2018 3:29 PM, Mayer Goldberg wrote:
› Hello:
› 
…[5 more quoted lines elided]…
› 
I thought this might be a troll because the use of SECTIONs in COBOL
is an old chestnut that has provoked passionate protest and support in
the past, but as I glanced through the thread I see that some
respectable posters here have stated their opinions.

There are a number of good arguments for NOT using SECTIONS and you have
seen them here.

When I first learned COBOL (1967) we always wrote PERFORM... THRU so
that the scope of the PERFORM was specifically stated. Very much the way
that Doc suggested and using the rules he laid down.

However, as time went on and I was exposed to many different
implementations of COBOL around the World, I came to realize that there
is actually nothing wrong with using SECTIONS to group paragraphs and
functions together logically, PROVIDED you observe some simple rules to
keep it consistent.

If you ONLY PERFORM a SECTION and never use THRU, then it can work
pretty well.

(Of course, it would be fatal to mix this approach with someone else's
code where they DON'T do that...).

It's kind of "nice" to structure your code into SECTIONS so you get
things like...

PROCEDURE DIVISION.
MAIN SECTION.
start-main.
perform initialize-it
perform do-the-biz
perform close-down.
end-main.
exit program.
INITIALIZE-IT SECTION.
start-init.
perform open-files
perform set-working-storage
...
end-init.
exit. *> if you REALLY need to GO TO this for some reason...
DO-THE-BIZ SECTION.
start-processing.
...
end-processing.
exit. *> if you REALLY need to GO TO this for some reason...
CLOSE-DOWN SECTION.
start-close.
perform close=files
perform clean-up
.
end-close.
exit. *> if you REALLY need to GO TO this for some reason...

*>=========SUBROUTINES ACTIVATED FROM THE ABOVE MAINLINE CODE
OPEN-FILES SECTION.
start-open.
open... etc.
...
end-open.
exit. *> if you REALLY need to GO TO this for some reason...
SET-WORKING-STORAGE SECTION.

... and so on.

It's a simple, clear, structure with each function easily locatable in
its own SECTION.

The rules are (all 2 of them...):

1. Avoid using GO TO and if you do so, the ONLY permissible target is
the exit from the SECTION YOU ARE IN.

2. You must only PERFORM a SECTION (or use a scope delimited inline
PERFORM.)

Pretty simple.

I have coded COBOL like this for well over 30 years now and nobody ever
complained about maintaining my code... :-)

However, for me, the best spinoff from this is that when you move to OO
COBOL, what used to be a SECTION, now becomes a Method and it gets
INVOKED instead of PERFORMED. The whole paradigm shift is made easier if
the original COBOL was already separated by function and, for me at
least, using SECTIONS facilitates that.

Obviously, the way in which you code is a choice for each individual
programmer and there will always be pros and cons of any approach. Use
what you feel comfortable with but be aware that others will have other
styles and that doesn't mean they are "wrong"... a "good" programmer can
understand and accommodate any style that complies with the language
syntax being used.

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-09-29T09:04:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p49@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p48@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap>`

```
On 09/29/2018 01:36 AM, pete dashwood wrote:
› 
› 
…[11 more quoted lines elided]…
› complained about maintaining my code... :-)

This is, by far, the most important comment. I can say the same
thing. I remember stopping by the shop at West Point for a visit
where I did a lot of COBOL programming more than 20 years after
I had left. When one of the few people remaining from my days
there introduced me to one of the newer programmers he looked
up from the listing he was pondering and asked, "Is he the
William Gunshannon who wrote this program?" What better
compliment can there be then to see your work still in use
after more than two decades. It also strongly attacks the myth
of code written unintelligibly for job security.



› 
› However, for me, the best spinoff from this is that when you move to OO 
…[3 more quoted lines elided]…
› least, using SECTIONS facilitates that.

And if the code was already working just fine for some unspecified
length of time, what, exactly, does one gain by rewriting it in OO?

› 
› Obviously, the way in which you code is a choice for each individual 
…[4 more quoted lines elided]…
› syntax being used.

And a bad paradigm can obfuscate even the best of code.

bill
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T19:52:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p50@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p49@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p49@usenetarchives.gap>`

```
On 30/09/2018 1:04 AM, Bill Gunshannon wrote:
› On 09/29/2018 01:36 AM, pete dashwood wrote:
›› 
…[14 more quoted lines elided]…
› This is, by far, the most important comment.
 
› Thanks bill... :-)
 
› I can say the same
› thing. I remember stopping by the shop at West Point for a visit
…[9 more quoted lines elided]…
› 
Yes, I found some code I wrote for a site in Auckland, NZ, nearly 30
years later, was still in production. (I doubt that it is now, though...)

Useful functions like the String2Num feature which you still can't run
on the PRIMA site (you CAN download it) get different incarnations like
moving out of IBM mainframe COBOL into Fujitsu and Micro Focus, so they
can have an extended life, but I'm not sure that counts... :-)
› 
›› 
…[7 more quoted lines elided]…
› length of time, what, exactly, does one gain by rewriting it in OO?

I wasn't suggesting rewriting in OO, although I'd have no problem with
converting standard COBOL to OO if I needed to. (In fact I have written
tools to do this...) My comment was intended for programmers who are
extending their vision and adding OO to their toolbox, starting with
COBOL. (I did this myself before finally moving to C# which is what I
mostly use now.)

I don't want to debate the use of OO right here, but one possible answer
to your question could be:

"Because I need multiple instances of the function running
simultaneously across a network under a single control program."

The advantages of OO when it comes to network software are huge and I
covered the arguments for it (in my opinion) at:

https://primacomputing.co.nz/PRIMAMetro/ObjectsAndLayers.aspx

There are 3 pages. If you read them and want to disagree I'll be happy
to discuss (without hostility or flaming) any comments you have in a new
thread in this forum.
› 
›› 
…[7 more quoted lines elided]…
› And a bad paradigm can obfuscate even the best of code.

No, the paradigms we use don't obfuscate the code we write; it is left
to programmers to do that. :-)

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T09:40:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p51@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p48@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap>`

```
Re trolling, that would have to be one hell of a troll to learn enough to ask a specific question like that. :-)

I have a thought that perhaps you're not the only person who thinks I'm a troll, so let me give you, and by extension, everyone else, an introduction and an explanation:

When I was a student, cobol was literally a dirty word: The one instructor who used to teach cobol was ignored or made fun of to his face, until finally the dept stopped teaching cobol as a service course, and he packed his bags and left elsewhere. I knew of him, but cobol was an introductory course offered to non-majors, and I was an MSc and PhD student, so I had no real reason to interact with him. When I did get to know him, it was something like 2-3 months before he left: He was one of the nicer guys at the dept. Very friendly, and very happy to answer questions. People actually snickered when they saw me visit his office.

Now there's something contrarian about my personality, and when I got fed up with cobol jokes at the dept (told by people who didn't know any cobol), I started looking at the language. I didn't have access to any real cobol, so I went to this instructor for advice. He gave me an old copy of RM Cobol for DOS that used to be handed out to students. In fact, he gave me like 10 copies :-) It was not a nice system compared to the programming environments I was familiar with, but pretty soon I discovered the student edition of MF Cobol for DOS, which was inexpensive, and came with some nice documentation. So I picked up a bit of cobol back in the 1980's. And then, as I moved to the Mac, and later to linux, I simply didn't have a cobol to play with, and didn't want to use DOS under emulation (DOS Box), so I forgot my cobol. I forgot the syntax, but remembered some of the ideas.

Now I do know that cobol is a business language, and that people here are all serious about the business programming culture, etc. Well, I'm an outsider: I'm not looking for work in business programming, and whatever I write in cobol will probably never be seen by anyone other than myself. But I study the ideas behind programming languages, and here is where I find cobol interesting. I know what people in the academia think about cobol (I myself am an academician), but I'm not interested in opinions from people who don't know the language and have little or no insights into it.

In some sense, cobol is actually a difficult language to learn: There's a lot of syntax, the semantics is generally simple until it becomes really tricky, and a lot of the pragmatics of the language (how best to use it) does not appear in any book, but is passed on in the culture of cobol programming. That's why I'm here. I have no interest in trolling, and hope to learn from people who spent the better part of their programming careers writing in cobol.

Re go to... As you can imagine, I am familiar with Dijksta's paper on the goto statement being considered harmful... :-) I don't think it's one of his better papers, and there are many ways to make spaghetti, goto being just one of them. If you follow his advice, you'll avoid the goto, invest in structured programming, and create your spaghetti code in other ways... This is one discussion I'm not going to get into. :-)

But since you brought up PERFORM ... THRU, I'll say that I can't imagine I'd ever use this statement. The idea that a specific sub-sequence of contiguous paragraphs will be executed in sequence, just because somewhere in the code there is a PERFORM ... THRU that ranges over them is a scary thought: You can add paragraphs wherever you like EXCEPT in the middle of such a sequence of paragraphs... This means that when you need to add a paragraph, you must first make sure that wherever you plan on sticking it is not in the middle of a PERFORM ... THRU sequence. To me, this seems like courting dissaster. Nothing in cobol scares me more than a PERFORM ... THRU: Not GO TO, not ALTER, not MOVE ... CORRESPONDING. Nothing.



On Saturday, September 29, 2018 at 8:36:13 AM UTC+3, pete dashwood wrote:
› On 27/09/2018 3:29 PM, Mayer Goldberg wrote:
›› Hello:
…[104 more quoted lines elided]…
› I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-29T14:24:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p52@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p51@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 1:40:44 AM UTC+12, Mayer Goldberg wrote:

›
› Re go to... As you can imagine, I am familiar with Dijksta's paper on the goto statement being considered harmful... :-) I don't think it's one of his better papers, and there are many ways to make spaghetti, goto being just one of them. If you follow his advice, you'll avoid the goto, invest in structured programming, and create your spaghetti code in other ways... This is one discussion I'm not going to get into. :-)
›
› But since you brought up PERFORM ... THRU, I'll say that I can't imagine I'd ever use this statement. The idea that a specific sub-sequence of contiguous paragraphs will be executed in sequence, just because somewhere in the code there is a PERFORM ... THRU that ranges over them is a scary thought: You can add paragraphs wherever you like EXCEPT in the middle of such a sequence of paragraphs... This means that when you need to add a paragraph, you must first make sure that wherever you plan on sticking it is not in the middle of a PERFORM ... THRU sequence. To me, this seems like courting dissaster. Nothing in cobol scares me more than a PERFORM ... THRU: Not GO TO, not ALTER, not MOVE ... CORRESPONDING. Nothing.
›

In fact there is nothing wrong with GO TO. When a GO TO is encountered when examining code it is very clear what happens, the logic is obvious.

The problem with using GO TO in programs is that there must be a label that is the target. This means that every label is potentially the target of a GO TO. When examining code (written by someone else) then, when a label is encountered, the whole program must be scanned to see if the logic flow can arrive at that label from elsewhere.

By eliminating GO TO in all its forms and the structures that enable it: PERFORM section and PERFORM THRU; only allowing PERFORM paragraph, then all procedure logic is local. Every label terminates the perform of the paragraph above and is only accessible by a PERFORM which, in turn, is terminated by the next label. New procedures can be added anywhere before an existing label knowing that this will never break existing logic. This allows simplification of code by breaking deep logic into performed procedures that are close by without the overhead of searching for a location where they won't break existing code, setting up a section or thru, giving it a level number. Just cut and copy code to the end of the paragraph, give it a new label, and perform it.

Getting rid of the overhead and clutter encourages simpler procedures, smaller paragraphs that are easier to understand and maintain.

Other languages enforce this by having different types of labels: subroutine and method labels cannot be the target of a goto; this enforced localization of logic. COBOL introduced mechanisms that also enforced logic localization: nested procedures and OO with methods; but these have been generally ignored.

As Pete says: OO was a revelation; but it was so (IMHO) in relation to his PERFORM THRU structure because methods enforced the localization that was achievable by elimination of THRU, sections and GO TO in COBOL-85.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-29T14:54:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p53@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p52@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p52@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 7:24:23 AM UTC+13, Richard wrote:
› On Sunday, September 30, 2018 at 1:40:44 AM UTC+12, Mayer Goldberg wrote:
›
››
›› But since you brought up PERFORM ... THRU, I'll say that I can't imagine I'd ever use this statement. The idea that a specific sub-sequence of contiguous paragraphs will be executed in sequence, just because somewhere in the code there is a PERFORM ... THRU that ranges over them is a scary thought: You can add paragraphs wherever you like EXCEPT in the middle of such a sequence of paragraphs... This means that when you need to add a paragraph, you must first make sure that wherever you plan on sticking it is not in the middle of a PERFORM ... THRU sequence. To me, this seems like courting dissaster. Nothing in cobol scares me more than a PERFORM ... THRU: Not GO TO, not ALTER, not MOVE ... CORRESPONDING. Nothing.
››

Further to my rant, many years ago I made a proposal to 'fix' COBOL by adding qualifiers to procedure labels. I can't recall all the exact details but the qualifiers limited the way that labels could be used. For example they were: PERFORMED, FROM ABOVE (dropped into), GONETO, ALTERED, ... If an attempt were made to use the label in a way not in the qualifier list then it would generate an error (or a warning depending on some option) at compile time and/or run time.

This would, hopefully, cater for warning the programmer about how the label was being used and/or assure them that there would be no surprises in their understanding of how the program worked.

It would also eliminate the sort of errors that I have seen where an 'exit label' has been misnumbered (in the form: 9010-EXIT.) and the PERFORM THRU incorporated the next procedure accidentally.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-29T17:34:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p54@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p52@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p52@usenetarchives.gap>`

```
Richard wrote:

› On Sunday, September 30, 2018 at 1:40:44 AM UTC+12, Mayer Goldberg wrote:
› 
…[22 more quoted lines elided]…
› when examining code it is very clear what happens, the logic is obvious.
Quite so; just like FORTRAN's famous COMEFROM statement.
https://www.fortran.com/come_from.html
:-D

Leslie
› 
› The problem with using GO TO in programs is that there must be a label
…[28 more quoted lines elided]…
› achievable by elimination of THRU, sections and GO TO in COBOL-85.

JLT
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T17:38:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p55@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p54@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p52@usenetarchives.gap> <gap-aa6095fcc2-p54@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 12:34:25 AM UTC+3, J Leslie Turriff wrote:
› Richard wrote:
› 
…[63 more quoted lines elided]…
› JLT

Fortran doesn't really have COME FROM! :-) The article said it would demonstrate COME FROM using fortran syntax. In fact, COME FROM is Intercal (https://en.wikipedia.org/wiki/INTERCAL) and there actually was a compiler for it at some point.

Fortran is too serious a language to will have added tongue-in-cheek constructs just to get laughs... :-)
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-29T21:31:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p56@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p55@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p52@usenetarchives.gap> <gap-aa6095fcc2-p54@usenetarchives.gap> <gap-aa6095fcc2-p55@usenetarchives.gap>`

```
Mayer Goldberg wrote:

› Fortran doesn't really have COME FROM! :-) The article said it would
› demonstrate COME FROM using fortran syntax. In fact, COME FROM is Intercal
…[4 more quoted lines elided]…
› constructs just to get laughs... :-)
Sure, but the article itself is funny, which proves that FORTRAN
users, supposedly serious-minded scientists, etc., aren't much different
from the rest of us.
I particularly like the explanation of the final example: "The code is
self-explanatory." :-D
JLT
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-09-29T16:56:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p57@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p51@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap>`

```
On Sat, 29 Sep 2018 06:40:42 -0700 (PDT), Mayer Goldberg
wrote:


› But since you brought up PERFORM ... THRU, I'll say that I can't imagine I'd ever use this statement. The idea that a specific sub-sequence of contiguous paragraphs will be executed in sequence, just because somewhere in the code there is a PERFORM ... THRU that ranges over them is a scary thought: You can add paragraphs wherever you like EXCEPT in the middle of such a sequence of paragraphs... This means that when you need to add a paragraph, you must first make sure that wherever you plan on sticking it is not in the middle of a PERFORM ... THRU sequence. To me, this seems like courting dissaster. Nothing in cobol scares me more than a PERFORM ... THRU: Not GO TO, not ALTER, not MOVE ... CORRESPONDING. Nothing.
›

Like anything else, PERFORM THRU is OK as long as it's used carefully
and consistently, as in:

...
perform 0200-do-something thru 0299-do-something-end.
...
stop run.

0200-do-something.
...
...
if error then
...
go to 0299-do-something-end.
...
...
0299-do-something-end.
exit.

If I recall correctly, there were versions of COBOL that didn't have
EXIT PARAGRAPH, and PERFORM THRU with a branch to an "end" paragraph
was one way of allowing a quick return to the caller.

If paragraph sequences are kept short and simple, there shouldn't be
much temptation to add paragraphs in the middle. And the inline
PERFORM makes it easier to code loops without adding new paragraphs.

Please post your reply below the dashes; it keeps us old folks happy,
or at least happier...

Louis

----------------------------------------------------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-29T18:31:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p58@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p57@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p57@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 9:58:25 AM UTC+13, Louis Krupp wrote:
› On Sat, 29 Sep 2018 06:40:42 -0700 (PDT), Mayer Goldberg
›  wrote:
…[37 more quoted lines elided]…
› ----------------------------------------------------------------------------------------------------------------------

There _are_ several problems that I find with your style.

Have you not heard of 'ELSE' ?

The first is that a PERFORM added without the THRU would likely work and could pass all the tests _until_ an error occurred and then there would be complete garbage that would be difficult to diagnose.

Then there is the problem - which I have seen - where the wrong exit was used in the GO TO. Again it is difficult to diagnose.

I is difficult to verify that code has the correct THRU and the correct GO TO labels without a specific program that goes through the text to check these. Whereas if section, THRU and GO TO are disallowed a simple text search will validate this.

The other issue that I disagree with is the use of numbering. This would have been really useful when programming was done using card packs and lineflow listings, but that disappeared, for me, in the mid 70s. All that the numbering does now is increase the overhead when it should be easy to split a paragraph into two or more for code sharing or reducing indent levels. With numbering and THRU, and especially if the numbering insists that the levels of perform are required to be echoed in where procedures are located in the code, there is an incentive to _not_ break the code into simpler pieces. This can result in ramblingly long paragraphs.

On another note, I never* put a full stop at the end of a line, it is too easy to overlook it. Use END-IF and only have a full stop at the end of a paragraph and it simplifies cut and pasting a block of code to a new paragraph (immediately after current one) and replacing it with a PERFORM so that it can be shared or simply to make the code more readable.




* I haven't actually written any serious COBOL code for many years.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-09-30T03:16:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p59@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p58@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p57@usenetarchives.gap> <gap-aa6095fcc2-p58@usenetarchives.gap>`

```
On Sat, 29 Sep 2018 15:31:40 -0700 (PDT), Richard
wrote:

› On Sunday, September 30, 2018 at 9:58:25 AM UTC+13, Louis Krupp wrote:
›› On Sat, 29 Sep 2018 06:40:42 -0700 (PDT), Mayer Goldberg
…[57 more quoted lines elided]…
› * I haven't actually written any serious COBOL code for many years.

I haven't written any COBOL code of any kind for many years.

I have written code using PERFORM THRU, and I was trying to illustrate
the method to the madness. As I said, being careful and consistent is
part of it.

That said, your points are well taken and in the unlikely event that I
were to write something of any length in COBOL in the future, I
wouldn't use PERFORM THRU. And I hope I would remember what you said
about periods.

Louis
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-29T17:25:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p60@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p51@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap>`

```
Mayer Goldberg wrote:

› Re trolling, that would have to be one hell of a troll to learn enough to
› ask a specific question like that. :-)
…[13 more quoted lines elided]…
› actually snickered when they saw me visit his office.
When I worked in IT Support at the local university, which at the time was
still using IBM Mainframe technology, there was one professor in the College
of Business who still taught COBOL; he told me that every year he received
requests from the business community in Kansas City for COBOL support
candidates; they could never find enough COBOL programmers. I'm sure that
the problem has only become more acute as the existing pool ages, and since
the university moved to Windows and Linux machines and dropped their support
of COBOL. The modern IT community (outside of those businesses who rely on
COBOL) treat it with disdain, and every year we see predictions that COBOL
is dead (just like FORTRAN :-) ); they don't (want to?) understand how much
infrastructure depends on large systems written in COBOL, and how much work
would be involved in migrating to a "modern" language.
Just recently, in an interesting article in Linux Format magazine about
using statistical analysis to recognize the acts of serial murderers, I read
this gratuitous bit of COBOL-bashing there:
"The data collected by MAP* from the FBI is user unfriendly. Written
in Cobol, it comes with some oddities and complexities that impact on
its
accessibility, but it's the language that was common when the FBI
started
assembling the data."
which of course is nonsense. The data is not written in COBOL, obviously;
it is almost surely stored in a format dictated by the storage medium of the
day, the 5081 punch card; but for whatever reason, the author of the article
felt compelled to blame COBOL instead. :-(
*MAP is the software system that the article is written about.
› 
› Now there's something contrarian about my personality, and when I got fed
…[21 more quoted lines elided]…
› into it.
My last job was with the State of Missouri, working on a COBOL-based
system
that was originally written somewhere around the 1970s, and had never been
modernized because this department promoted its IT staff from the personnel
who used the system. They received no formal IT training, and so their
programming technique was frozen in the pre-structured programming paradigm,
entirely spaghetti code, with GO TOs everywhere. All of the IT folks who
had any idea of the technicalities of the system had retired and were now
working as contractors, but they were disappearing fast. It was a scary
environment to work in, because if anything really serious happened, there
was nobody who really knew how the system worked available to fix it.
› 
› In some sense, cobol is actually a difficult language to learn: There's a
…[5 more quoted lines elided]…
› careers writing in cobol.
When I worked as a contractor for the Bonneville Power Administration
we weren't allowed to use the SEARCH ALL command because the BPA staff
programmers didn't understand how it worked; but I saw several instances
where they had written their own binary search routines instead!
› 
› Re go to... As you can imagine, I am familiar with Dijksta's paper on the
…[15 more quoted lines elided]…
› ... THRU: Not GO TO, not ALTER, not MOVE ... CORRESPONDING. Nothing.
PERFORM THROUGH is, like SECTION, an obsolescent artifact which has been
superceded by the PERFORM ... END-PERFORM construct.

Leslie
› 
› 
…[113 more quoted lines elided]…
›› I used to write COBOL; now I can do anything...

JLT
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T20:52:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p61@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p51@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap>`

```
On 30/09/2018 1:40 AM, Mayer Goldberg wrote:
› Re trolling, that would have to be one hell of a troll to learn enough to ask a specific question like that. :-)
›
› I have a thought that perhaps you're not the only person who thinks I'm a troll, so let me give you, and by extension, everyone else, an introduction and an explanation:

Let me assure you that, had I decided you were a troll, I would not have
responded. On inspection I saw that your interest was genuine.
›
› When I was a student, cobol was literally a dirty word: The one instructor who used to teach cobol was ignored or made fun of to his face, until finally the dept stopped teaching cobol as a service course, and he packed his bags and left elsewhere. I knew of him, but cobol was an introductory course offered to non-majors, and I was an MSc and PhD student, so I had no real reason to interact with him. When I did get to know him, it was something like 2-3 months before he left: He was one of the nicer guys at the dept. Very friendly, and very happy to answer questions. People actually snickered when they saw me visit his office.

Yes, I have encountered similar prejudices in industry during the late
1990s and the first decade of this century, where the COBOL guys were
"only" maintaining the "legacy" as the hot-shot Java people implemented
the Brave New World... :-)

One way I found to overcome this was to take an interest in the Java
stuff and talk/listen to the programmers (I taught myself Java at this
time).

Then produce some COBOL code that did what they were doing and elicited
responses like: "I didn't know you could do that in COBOL...", "Wow!
that's really cool... and in COBOL too..."

Once the "Class culture" between first and second class programmers was
resolved and some mutual respect for both the languages and people was
established, things generally progressed much more easily.

(It was around this time that I wrote the article on Cretaceous COBOL
and Jurassic Java, which was primarily aimed at Java programmers and
Managers who get their information from in-flight magazines...
https://dzone.com/articles/cretaceous-cobol-can-spawn
More than 16000 people have read this article and nobody "like"d it...
:-) (Given that the audience are mainly Java guys, I count that as a
success... :-))


› 
› Now there's something contrarian about my personality, and when I got fed up with cobol jokes at the dept (told by people who didn't know any cobol), I started looking at the language. I didn't have access to any real cobol, so I went to this instructor for advice. He gave me an old copy of RM Cobol for DOS that used to be handed out to students. In fact, he gave me like 10 copies :-) It was not a nice system compared to the programming environments I was familiar with, but pretty soon I discovered the student edition of MF Cobol for DOS, which was inexpensive, and came with some nice documentation. So I picked up a bit of cobol back in the 1980's. And then, as I moved to the Mac, and later to linux, I simply didn't have a cobol to play with, and didn't want to use DOS under emulation (DOS Box), so I forgot my cobol. I forgot the syntax, but remembered some of the ideas.
› 
› Now I do know that cobol is a business language, and that people here are all serious about the business programming culture, etc. Well, I'm an outsider: I'm not looking for work in business programming, and whatever I write in cobol will probably never be seen by anyone other than myself. But I study the ideas behind programming languages, and here is where I find cobol interesting. I know what people in the academia think about cobol (I myself am an academician), but I'm not interested in opinions from people who don't know the language and have little or no insights into it.
 
› This is a "proper" attitude and makes you welcome here, Mayer.
› 
…[5 more quoted lines elided]…
› 
Amen to that!

(I am probably the ONLY person here who has ever defended the use of
ALTER but I believe it is like everything else: if you find a construct
in a language that is potentially disastrous, don't ban it in the local
standards, teach people to understand it and use it responsibly.

It's kind of sad (IMO) that the vendors bowed to pressure from the User
Groups and dropped it from the language. I remember using it in a system
in the late 1960s where it was a lot like switching points in a Railway
marshalling yard... and it was MUCH more efficient on the platform where
it was running (Burroughs B500) than a COBOL IF...)



Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-29T21:28:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p62@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p61@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p61@usenetarchives.gap>`

```
pete dashwood wrote:

› Amen to that!
› 
…[3 more quoted lines elided]…
› standards, teach people to understand it and use it responsibly.
Yes, if only that were the common response; but more often than not
its presence was ignored, or taken advantage of to promote "job security."
When I first entered the industry, the organizations I worked for were
sincere in their efforts at providing training for the IT staff, but as
the years went by that changed more and more toward lip-service; and even
as the training available became more organized and reliable, the number
of participants seemed to diminish in inverse proportion. In any case,
the only teaching I've ever seen in regards to ALTERed GO TOs was to either
never use it, or at best to leave of the paragraph name in the target of
the ALTER statement so that it was clearly an ALTERed GO TO. Training in
the use of computed GOTOs in FORTRAN was treated much the same way.
› 
› It's kind of sad (IMO) that the vendors bowed to pressure from the User
…[8 more quoted lines elided]…
› 

JLT
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T06:58:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p63@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p61@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p61@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 3:52:46 AM UTC+3, pete dashwood wrote:
› On 30/09/2018 1:40 AM, Mayer Goldberg wrote:
›› Re trolling, that would have to be one hell of a troll to learn enough to ask a specific question like that. :-)
…[65 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

Some years ago, I actually wrote an exam question for a compilers course, that asked about how ALTER can be implemented, i.e., translated into assembly language, and what are the advantages and disadvantages of either approach, both for older architectures and modern ones... Even though my students didn't know cobol, this was a great question, IMO.

Mayer
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2018-10-01T16:09:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p64@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p61@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p48@usenetarchives.gap> <gap-aa6095fcc2-p51@usenetarchives.gap> <gap-aa6095fcc2-p61@usenetarchives.gap>`

```
On Sun, 30 Sep 2018 13:52:39 +1300, pete dashwood
wrote:

›› much snipped
› 
…[3 more quoted lines elided]…
› standards, teach people to understand it and use it responsibly.

AS someone who used ALTER extensively to replace PERFORM statements on
DOS 360 COBOL I found two major uses for it.

The first to replace the use of PERFORM by creating ALTER
desired-processing-switch-paragraph TO PROCEED TO next-paragraph GO TO
desired-processing-paragraph. I used paragraph numbering so that
people had an idea of where to look in a multi-page listing and
prefixed switch paragraph names with SW. This was done to fit into
16K partitions on IBM DOS360 model 30 machines because the ALTER ...
GO TO sequence took 10 bytes and PERFORM (THRU) took 24 bytes.
Needless to say that larger memory and much improved code generation
made this practice obsolete and definitely NOT worth the complexity it
causes. The other use for ALTER could be to create a utility program
where based on control information the processing path could be set so
that the testing for whether or not a specific portion of the code
should executed for each set of inputs could be avoided. Frankly I
don't think COBOL is well suited for creating utility programs.
› 
› It's kind of sad (IMO) that the vendors bowed to pressure from the User 
…[3 more quoted lines elided]…
› it was running  (Burroughs B500) than a COBOL IF...)

This seems like the type of utility that I mentioned above. The IF
statement execution time and code size costs would still be greater
than use of ALTER on even today's computers but would anyone other
than nerds like me notices the difference?

CLark Morris
›
›
›
› Pete.
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T15:13:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p65@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
I use GO TO for one and only one purpose: To implement the tail-call optimization. So I never get "spaghetti code" because my use is very rigid. If you're not trying to simulate recursion or higher-order programming in cobol 85, then there's no need for this, and it will only annoy and confuse others. The point, by the way, is not just the optimization per se, but rather the management of control through tail-calls. Later versions of cobol support user-defined functions, recursion, and objects, so the compiler will probably manage the optimization and relieve the programmer from having to worry about it.

Go to to a label is just half the problem. If you add to it "computed goto", as in fortran, algol60, and some basic implementations, you complicate things even further...

On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T17:42:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p66@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer

If anything, cobol makes it very easy to process data efficiently, because it encourages a highly-structured, tabular form, as opposed to the free-form output that most other programming languages allow programmers to generate. Cobol programs can of course generate any format, but then processing such format would be computationally intensive and require parsing.
```

#### ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T17:46:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p67@usenetarchives.gap>`
- **In-Reply-To:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com>`

```
On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
› Hello:
› 
…[4 more quoted lines elided]…
› Mayer

There's something here I don't get. First off, you have a rigid numbering convention, so you're performing from 200-something to 299-something... This is already one hint to the programmer, not to insert paragraphs in the numbered paragraphs unless they plan them to be a part of this sequence. So if you program like this, you're right, it's less confusing. On the other thand, what do you do with a joker that has perform 200-something thru 299-something, and then perform 241-something thru 276-something, and then perform 239-something thru 299-something, etc. Now you have multiple entry points and multiple exit points, and the code is as hard to figure out as anything else you could write. So obviously, you must have some additional conventions that would preclude this kind of programming.
```

##### ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-09-29T18:15:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p68@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p67@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap>`

```
On Sat, 29 Sep 2018 14:46:16 -0700 (PDT), Mayer Goldberg
wrote:

› On Thursday, September 27, 2018 at 6:29:14 AM UTC+3, Mayer Goldberg wrote:
›› Hello:
…[7 more quoted lines elided]…
› There's something here I don't get. First off, you have a rigid numbering convention, so you're performing from 200-something to 299-something... This is already one hint to the programmer, not to insert paragraphs in the numbered paragraphs unless they plan them to be a part of this sequence. So if you program like this, you're right, it's less confusing. On the other thand, what do you do with a joker that has perform 200-something thru 299-something, and then perform 241-something thru 276-something, and then perform 239-something thru 299-something, etc. Now you have multiple entry points and multiple exit points, and the code is as hard to figure out as anything else you could write. So obviously, you must have some additional conventions that would preclude this kind of programming.

There are two key words in there: "Rigid" and "joker."

In a COBOL shop, the paragraph numbering convention is rigid, the
entire coding standard is often rigid, and sometimes even the dress
code is rigid. Jokers and people with wide ties are generally not made
to feel welcome.

C++ shops, on the other hand, are consensus-driven places where people
and ideas are always judged on their merit. Yes, I'm joking.

Louis
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T18:23:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p69@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p68@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 1:17:41 AM UTC+3, Louis Krupp wrote:
› On Sat, 29 Sep 2018 14:46:16 -0700 (PDT), Mayer Goldberg
›  wrote:
…[22 more quoted lines elided]…
› Louis

Ok. Very good: Now please tell me what textbook on cobol will teach me coding conventions. I know they'll change from one shop to the next, but please recommend a document that will have naming and numbering conventions, as well as other conventions --- the kind of stuff without which it's impossible to write large systems, and with these it's actually doable. :-)

BTW: I studied at Aarhus University, where Stroustrup got his BSc, and the good folks over there don't have many positive things to say about C++, and neither do I. :-)
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-29T18:46:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p70@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p69@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p69@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 11:23:24 AM UTC+13, Mayer Goldberg wrote:

› Ok. Very good: Now please tell me what textbook on cobol will teach me coding conventions. I know they'll change from one shop to the next, but please recommend a document that will have naming and numbering conventions, as well as other conventions --- the kind of stuff without which it's impossible to write large systems, and with these it's actually doable. :-)
›
› BTW: I studied at Aarhus University, where Stroustrup got his BSc, and the good folks over there don't have many positive things to say about C++, and neither do I. :-)

I have never used any 'numbering convention' because I have never used numbering. It would have been useful in the days of punch cards and lineflow in the 60s (which is where I started - 50 years this month!) and where programs ran to thousands of lines of code. My large systems were based on CALL CANCEL to modularize them and didn't need the bureaucracy (or tyranny) of performed sections, perform thru and the need to lay these out by perform level.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T18:51:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p71@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p70@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p69@usenetarchives.gap> <gap-aa6095fcc2-p70@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 1:46:21 AM UTC+3, Richard wrote:
› On Sunday, September 30, 2018 at 11:23:24 AM UTC+13, Mayer Goldberg wrote:
› 
…[4 more quoted lines elided]…
› I have never used any 'numbering convention' because I have never used numbering. It would have been useful in the days of punch cards and lineflow in the 60s (which is where I started - 50 years this month!) and where programs ran to thousands of lines of code. My large systems were based on CALL CANCEL to modularize them and didn't need the bureaucracy (or tyranny) of performed sections, perform thru and the need to lay these out by perform level.

Perhaps I don't understand: Is call for external subroutines that are linked with the executable, or for external programs that need to invoked as with the fork/pipe/dup/exec mechanism in C/linux?
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:44:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p72@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p71@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p69@usenetarchives.gap> <gap-aa6095fcc2-p70@usenetarchives.gap> <gap-aa6095fcc2-p71@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 11:51:34 AM UTC+13, Mayer Goldberg wrote:
› On Sunday, September 30, 2018 at 1:46:21 AM UTC+3, Richard wrote:
›› On Sunday, September 30, 2018 at 11:23:24 AM UTC+13, Mayer Goldberg wrote:
…[7 more quoted lines elided]…
› Perhaps I don't understand: Is call for external subroutines that are linked with the executable, or for external programs that need to invoked as with the fork/pipe/dup/exec mechanism in C/linux?

CALL is to a COBOL subroutine which can be nested in the program, can be external but statically linked, or can be dynamically linked and loaded at run time in which case a CANCEL will unload the routine and free the memory that it used.

There are usually vendor supplied mechanisms for invoking other programs, such as CALL "SYSTEM" USING command-line.

Apart from not having to load the whole system (static linked) into memory at start up - which would have been impossible on the multi-user machines I, and my clients, were using in the 80s and 90s, dynamic systems have many other advantages.

For example the CALL is by text string name and resolved at run-time. This allows variations in which program is actually called. I developed bespoke modules for each client so that the base system could be common but a control file directed the specific module to be called. These might, in turn, CALL common modules for certain functions.

It also meant that distributing updated modules did not require the whole system to be linked and re-tested, the updates could be loaded into the machine even if users were running the system and they would get the newer version of the module the next time it was needed.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T21:05:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p73@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p70@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p69@usenetarchives.gap> <gap-aa6095fcc2-p70@usenetarchives.gap>`

```
On 30/09/2018 11:46 AM, Richard wrote:
› On Sunday, September 30, 2018 at 11:23:24 AM UTC+13, Mayer Goldberg wrote:
› 
…[7 more quoted lines elided]…
› 
I just wanted to endorse what Richard said here.

There are NO COBOL numbering conventions that are laid down by the
language (except the one about columns 1 - 6 being reserved for line
numbers...).

I worked on many different sites in many different countries and found
that whenever numbered paragraphs or sections were encountered it was a
system known ONLY to the guy who wrote it. (And he usually assumed it
was axiomatic to anyone else who would maintain his code...)

Personally, I don't use them, but I don't have a problem maintaining
programs that do.

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 6)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T15:08:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p74@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p73@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p69@usenetarchives.gap> <gap-aa6095fcc2-p70@usenetarchives.gap> <gap-aa6095fcc2-p73@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 2:05:30 PM UTC+13, pete dashwood wrote:

›
› There are NO COBOL numbering conventions that are laid down by the
› language (except the one about columns 1 - 6 being reserved for line
› numbers...).

Which was really useful when the source code moved from trays of punched cards to source libraries on mag tape. Then you could get the source renumbered to, say, hundreds, and then working from a lineflow listing you could write new or replaced lines using the numbers and have the computer merge these cards into the main source without needed to laboriously merge them into the card tray yourself.

Oh! the wonders of modern machinery. Of course we couldn't used the disk drives, there would never be enough disk space.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-29T18:54:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p75@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p68@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 11:17:41 AM UTC+13, Louis Krupp wrote:

› In a COBOL shop, the paragraph numbering convention is rigid, the
› entire coding standard is often rigid, and sometimes even the dress
› code is rigid. Jokers and people with wide ties are generally not made
› to feel welcome.

I was contracted to do work in P&O in London a couple of decades ago where they did have a dress code. I haven't owned a suit for 35 years and haven't worn business shirts and tie either. I was approached and informed that there was a dress code. I just answered: "It's OK, I'm from New Zealand" and he wandered off and nothing more was said.

Fortunately, my contract was with someone fairly high up in the organization and it was my code that was being implemented for them.
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-29T18:57:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p76@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p75@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p75@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 1:54:02 AM UTC+3, Richard wrote:
› On Sunday, September 30, 2018 at 11:17:41 AM UTC+13, Louis Krupp wrote:
›  
…[7 more quoted lines elided]…
› Fortunately, my contract was with someone fairly high up in the organization and it was my code that was being implemented for them.

Ahh, a Kiwi! :-) Katherine Mansfield is my favourite poet! :-)
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T21:41:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p77@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p76@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p75@usenetarchives.gap> <gap-aa6095fcc2-p76@usenetarchives.gap>`

```
On 30/09/2018 11:57 AM, Mayer Goldberg wrote:
› On Sunday, September 30, 2018 at 1:54:02 AM UTC+3, Richard wrote:
›› On Sunday, September 30, 2018 at 11:17:41 AM UTC+13, Louis Krupp wrote:
…[11 more quoted lines elided]…
› 
Speaking as another Kiwi,(and a devoted lover of the English language)
I'd say that, while Katherine Mansfield wrote some great short stories
(read "The Fly") and did produce some good poems (I like "Camomile
Tea"), there are other Kiwis who are at least as good.

See what you think of "Secular Litany" (my favourite Kiwi poem because
it makes me smile every time I read it... It is a brilliant parody of
the Post War New Zealand I grew up in.)

Here's a link:

https://www.eastonbh.ac.nz/2007/08/secular-litany-by-m-k-joseph/

Enjoy!

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Need some intuition here --- sections in the procedure division

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-29T21:21:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa6095fcc2-p78@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa6095fcc2-p75@usenetarchives.gap>`
- **References:** `<6e8ba507-d0be-4915-86be-e558c8e7f1de@googlegroups.com> <gap-aa6095fcc2-p67@usenetarchives.gap> <gap-aa6095fcc2-p68@usenetarchives.gap> <gap-aa6095fcc2-p75@usenetarchives.gap>`

```
On 30/09/2018 11:54 AM, Richard wrote:
› On Sunday, September 30, 2018 at 11:17:41 AM UTC+13, Louis Krupp wrote:
›   
…[8 more quoted lines elided]…
› 
LOL!

Great story, Richard... :-)

(I too found that working in London was more rigid than in say, Madrid
or Duesseldorf, but they kind of cut me slack because I was a foreigner.

(they seem to assign you the special Class of "guest" so they can relate
to you within the Class system... :-)

The best example I have of this was from a contract in Leeds where I was
hauled onto the red carpet with a chinless wonder double-barrelled
"Manager" who got the job because of the schools he went to and the Club
his father belonged to.

His beef was that I was in the local pub at lunch time. I thought maybe
they had rules about alcohol (although there were many staff in the bar
I was in), but when I queried him he said:

"Oh no, we all go to the pub at lunch time. But you were in the WRONG bar."

Apparently I was "Management" and had been drinking with the "Shop
Floor" and that was unacceptable...

I leave it to readers' imaginations to picture my response. He never
called me out again and I continued building a working relationship with
the people who I was there to help.

POSTSCRIPT:

I worked in Europe from 1975 until the early part of this century,
around 30 years. During that time I did see some eroding of the stupid
class system that has held England back for over a century. By the time
I finished my tour it was becoming more usual to see people like the
manager described above being replaced by people who were being promoted
on merit (including (dare I say it...) ... women.)

I believe that UK industry in 2018 is a far cry from what it was in 1975
and I hope that further progress will continue to be made.

Pete.
I used to write COBOL; now I can do anything...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
