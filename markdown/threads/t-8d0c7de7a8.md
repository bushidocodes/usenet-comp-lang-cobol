[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading Backwards

_4 messages · 2 participants · 2014-02_

---

### Reading Backwards

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-02-04T21:41:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bldmm8Fn3hdU1@mid.individual.net>`

```
After dealing with some slightly different COBOL implementations I'd like to
know what the "correct" (COBOL 85 standard) behaviour is for the following:

Can I reasonably expect the record previous to where I am currently
positioned to be returned by the following?

1. START REVERSED (with KEY = to current position) followed by READ NEXT
2. START REVERSED (with KEY = to current position) followed by READ
PREVIOUS

3. START (with KEY = to current position) (without REVERSED) followed by
READ PREVIOUS
4. READ PREVIOUS (without START of any kind)

Opinions and documentation seem to differ on this so I'd appreciate any
comments.

(Yes, I have run tests, but the results are not consistent across different
implementations...)

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Reading Backwards

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2014-02-05T03:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d0c7de7a8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<bldmm8Fn3hdU1@mid.individual.net>`
- **References:** `<bldmm8Fn3hdU1@mid.individual.net>`

```
On Tuesday, February 4, 2014 9:41:10 PM UTC-5, Pete Dashwood wrote:
› After dealing with some slightly different COBOL implementations I'd like to 
› know what the "correct" (COBOL 85 standard) behaviour is for the following:
…[16 more quoted lines elided]…
› implementations...)

Neither START REVERSED nor READ PREVIOUS are standard in COBOL 85.

COBOL 2002 added READ PREVIOUS or START ... KEY IS LESS THAN current-key
... followed by READ NEXT as means to access the preceding record.

START REVERSED was not added and, therefore, not likely to have broad
support.
```

##### ↳ ↳ Re: Reading Backwards

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-02-05T07:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d0c7de7a8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8d0c7de7a8-p2@usenetarchives.gap>`
- **References:** `<bldmm8Fn3hdU1@mid.individual.net> <gap-8d0c7de7a8-p2@usenetarchives.gap>`

```
Rick Smith wrote:
› On Tuesday, February 4, 2014 9:41:10 PM UTC-5, Pete Dashwood wrote:
›› After dealing with some slightly different COBOL implementations I'd
…[28 more quoted lines elided]…
› support.

Thank you SO much for that Rick.

It explains much. :-)


(All 4 of the above WILL return the previous record from the current
position as far as DAL is concerned, and subsequent READ NEXT or READ
PREVIOUS will descend through the result set, as expected.)

START ... KEY IS LESS THAN current-key ... followed by READ NEXT could
return anything in some implementations because they don't always guarantee
that the record positioned to will be the next one in descending sequence...
all it guarantees is that the key will be less than the current position.
Subsequent READ NEXTs are similarly undefined. There is a place for both
START REVERSED and READ PREVIOUS. (The latter can be issued without a
preceding START and will retrieve records descending from the current
position.)

I seem to remember preparing a truth table for backward reading for a client
some time ago when the COBOL DAL was developed. I'll try and find it and
make sure that LINQ implements in the same way.

Many Thanks,

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Reading Backwards

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-02-05T22:20:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d0c7de7a8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8d0c7de7a8-p3@usenetarchives.gap>`
- **References:** `<bldmm8Fn3hdU1@mid.individual.net> <gap-8d0c7de7a8-p2@usenetarchives.gap> <gap-8d0c7de7a8-p3@usenetarchives.gap>`

```
Pete Dashwood wrote:
› Rick Smith wrote:
›› On Tuesday, February 4, 2014 9:41:10 PM UTC-5, Pete Dashwood wrote:
…[51 more quoted lines elided]…
› find it and make sure that LINQ implements in the same way.

I found the table but I'm pretty sure this will be garbled when I post it.

Never mind, any one who's interested can reconstruct it using the vertical
and horizontal separators...
======================= start of quoted table
========================================
I am looking at the design changes to support START/READ NEXT/PREVIOUS in
the way that you folks use it.
There is a fair bit to it, but mostly it will involve some changes to the
control logic within some of
the DAL methods. We cannot realistically support unlimited concurrent
cursors in a single DAL instance,
but I can offer the following:

NOTE: There can only ever be ONE cursor, FORWARD or BACKWARD, current at any
given moment, for any given Tableset.
When you issue a START (or START REVERSED) a cursor will be opened against
the Database. If you issue another
START on the same stem, the previous cursor is closed and the new one is
opened.

Here's a summary of the proposed implementation (KOR = Key of Reference):
--------------------------------------------------------------------------------------------------------
Cursor is running |
|
(START succeeded) | READ NEXT |
READ PREV
--------------------------------------------------------------------------------------------------------
FORWARDS | Returns NEXT record in KOR sequence | Returns the record
in previous KOR Sequence
| from the LAST record retrieved
| to the record key passed in the interface buffer.
…[3 more quoted lines elided]…
|
-------------------------------------------------------------------------------------------------------------
BACKWARDS | Returns PREVIOUS record in KOR | Returns the
record in previous KOR
| sequence from the LAST record retrieved |
Sequence to the record key passed in the
| successfully.
| interface buffer. IT DOES NOT AFFECT
…[19 more quoted lines elided]…
|
--------------------------------------------------------------------------------------------------------------
NO CURSOR RUNNING | Not supported. We COULD make it get the | Returns the
record in previous KOR Sequence
| next record in KOR sequence
from the | to the record key passed in the interface buffer.
| record passed in the
interface, but you |
| need to discuss it and let us
know. I'm |
| not keen to support this
because it is |
| inefficient, but we'll do it
if you want. |
------------------------------------------------------------------------------------------------------------------
Most people seem to use START purely for skip sequential processing. We have
a couple of people who used READ PREV to get time sequence data, but we
haven't encountered anyone who uses READ NEXT/PREV without having a
preceding START. Obviously, you can run a cursor and still go off and do
random things (FCRUD) without losing position on it. To implement this in
SQL involves a SQL cursor and this is not best practice, but it works pretty
well.

I think we need to look at more samples of legacy and see what the best fit
is.
============================= end quoted table
========================================================
›
› Many Thanks,
›
› Pete.

"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
