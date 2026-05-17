[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Determning length of varable length string

_20 messages · 9 participants · 1995-02 → 1995-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Determning length of varable length string

- **From:** "gt..." <ua-author-2476667@usenetarchives.gap>
- **Date:** 1995-02-16T18:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3i0o89$nia@newsbf02.news.aol.com>`

```
Does anyone know how to determine the length of a string passed into a
COBOL
program?

The string can be any where from a couple of bytes to several thousand. I
am
using VS COBOL II so I cann't use the Length function and I want to say
ANSI
so i can't use the Length of Register. The string will be pass in a var
that is
allocated to the largest string that could be possibily returned. The
string will
can contain more than 2 spaces between words and almost any character. I
would like to be able to find the length of the string to the last
nonspace character, the string will be padded with spaces at the end.
thanks,
GT
```

#### ↳ Re: Determning length of varable length string

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-02-17T12:20:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3i0o89$nia@newsbf02.news.aol.com>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com>`

```
GTT1 (gt··.@a··.com) wrote:
: Does anyone know how to determine the length of a string passed into a
: COBOL
: program?

: The string can be any where from a couple of bytes to several thousand. I
: am
: using VS COBOL II so I cann't use the Length function and I want to say
: ANSI
: so i can't use the Length of Register. The string will be pass in a var
: that is
: allocated to the largest string that could be possibily returned. The
: string will
: can contain more than 2 spaces between words and almost any character. I
: would like to be able to find the length of the string to the last
: nonspace character, the string will be padded with spaces at the end.
: thanks,
: GT

Write a routine:

01 String.
02 Str-Char PIC X OCCURS 2000 TIMES.
77 NUM4 PIC 9999.


PERFORM Routine VARYING NUM4 FROM 2000 BY -1 UNTIL
NUM4 < 1 OR Str-Char(NUM4) > SPACE.

Routine.
Do something useless.
```

##### ↳ ↳ Re: Determning length of varable length string

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-02-17T17:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p2@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p2@usenetarchives.gap>`

```
fr··.@M··.COM (Lawrence Free/ A.F. Software Services) wrote:

Or (ANS COBOL 85):

01 String PIC X(2000).
01 NUM4 PIC S9(4) BINARY.

PERFORM
VARYING NUM4
FROM 2000
BY -1
UNTIL NUM4 < 1
OR String(NUM4:1) > SPACE
END-PERFORM

-----Burton
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "john m perry" <ua-author-17087542@usenetarchives.gap>
- **Date:** 1995-02-18T03:43:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p3@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p2@usenetarchives.gap> <gap-f264fe72eb-p3@usenetarchives.gap>`

```

cobols i use don't allow any empty perform
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

_(reply depth: 4)_

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-02-18T12:50:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p4@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p2@usenetarchives.gap> <gap-f264fe72eb-p3@usenetarchives.gap> <gap-f264fe72eb-p4@usenetarchives.gap>`

```
John M Perry wrote:

› cobols i use don't allow any empty perform

So dump a CONTINUE in there. I don't have my standard at home, so
I can't check. With the CONTINUE, it's clearly legal and any '85
compiler should swallow it happily.

-----Burton
```

#### ↳ Re: Determning length of varable length string

- **From:** "john m perry" <ua-author-17087542@usenetarchives.gap>
- **Date:** 1995-02-17T16:55:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3i0o89$nia@newsbf02.news.aol.com>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com>`

```
gt··.@a··.com (GTT1) wrote:
›
› Does anyone know how to determine the length of a string passed into a
…[3 more quoted lines elided]…
›


perform dummy varying pointer from maximum by -1
until maximum zero
or string-x(pointer) not = space

pointer, string, maximum are variables
dummy is a section merely containing the verb exit

it always worked for me
```

#### ↳ Re: Determning length of varable length string

- **From:** "zpr..." <ua-author-17086607@usenetarchives.gap>
- **Date:** 1995-02-25T00:12:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3i0o89$nia@newsbf02.news.aol.com>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com>`

```
› GTT1 (gt··.@a··.com) wrote:
› : Does anyone know how to determine the length of a string passed into 
› a
› : COBOL 
› : program?
Several responses included the standard perform loop for determining
the length of the string, but if this routine will be performed often and
if the string will typically be much less than the maximum allowable
length, I would first test to see if the last half of the data item is
all spaces, and if so, start my perform routine from the halfway point
downward. You could carry this concept (you could next test if last 3/4
of item is blank, etc) as far as justified by the profile of the typical
data and performance sensitivity.
-
DANIEL THOMAS (Dan) ZPR··.@pro··y.com
Louisville, KY
```

##### ↳ ↳ Re: Determning length of varable length string

- **From:** "john m perry" <ua-author-17087542@usenetarchives.gap>
- **Date:** 1995-02-25T02:06:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p7@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap>`

```
ZPR··.@pro··y.com (Daniel Thomas) wrote:
› I would first test to see if the last half of the data item is
› all spaces, and if so, start my perform routine from the halfway point
› downward.
›

is this any quicker?
```

##### ↳ ↳ Re: Determning length of varable length string

- **From:** "zpr..." <ua-author-17086607@usenetarchives.gap>
- **Date:** 1995-02-26T02:30:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p7@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap>`

```
John M Perry wrote:
› 
› ZPR··.@pro··y.com (Daniel Thomas) wrote:
›› I would first test to see if the last half of the data item is 
›› all spaces, and if so, start my perform routine from the halfway point 
 
›› downward. 
›› 
› 
› is this any quicker?
› 
Certainly! Whenever the length of the data item is less than half
the maximum possible size, then you'll save almost have the time (time
required to perform the initial test to see if last half = spaces is
trivial). Even though the paragraph performed is empty, processing time
is spent decrementing the subscript. You could expand this idea and test
to see if the last 3/4 of the data item is spaces and save much more time.

Another item not previously mentioned, is that there is a
performance difference in most versions of Cobol between table
subscripting and indexing, one of which is required for this routine.
When using subscripting, some versions of Cobol perform differently
depending upon how the subscript is defined (DISPLAY, COMP-6, etc).
I'm sure with a little thought, we could come up with some really
exotic routines (maybe use reference modification to test larger chunks
of the field at once?) to solve this problem. I wouldn't normally waste
this much thought on such a trivial task, but if a part of a program is
performance sensitive then it is worthwhile to get a little creative.
-
DANIEL THOMAS (Dan) ZPR··.@pro··y.com
Louisville, KY
```

##### ↳ ↳ Re: Determning length of varable length string

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-02-26T12:05:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p7@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap>`

```
I do not understand Daniel Thomas' comment about testing the last half of
a string for being blank, the "standard perform loop" should generate
optimal code for testing for the length of the string, and attempts like
this to hand optimize the code may in fact pessimize it.
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-02-27T23:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p10@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p10@usenetarchives.gap>`

```
On 26 Feb 1995 12:05:09 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› I do not understand Daniel Thomas' comment about testing the last half of
› a string for being blank, the "standard perform loop" should generate
› optimal code for testing for the length of the string, and attempts like
› this to hand optimize the code may in fact pessimize it.

Damn it! There is no "pessimize" in the English language.
Nevertheless, Dewar is correct here when he states that such attempts
at hand optimisation of COBOL code are often futile. That is because
it forces certain assumptions about what the compiler is going to do.
And that will vary from one machine to another.
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

_(reply depth: 4)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-01T10:52:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p11@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p10@usenetarchives.gap> <gap-f264fe72eb-p11@usenetarchives.gap>`

```
Joseph says:

"Damn it! There is no "pessimize" in the English language."

First, there is little point in complaining about something that is in common
usage. Second, if you do want to complain, you should probably take the
trouble to make sure that your pronouncements on language are correct.

>From the OED, edition II

(volume XI, page 622)

Pessimize ... "to make the worst of"
There are two citations, one from 1862, and one from 1873. THe OED calls it
rare, but not archaic. Its use in the current context seems perfectly
justified (and is common in compiler technology discussions).

For those who distrust edition II, this same entry appears unchanged in
edition I of the OED, of which I only have the irritating compact version,
where it appears in volume II on page 2145.

I think I will take the OED as an authority over Joseph on this issue :-)

In fact the analogy to optimize is clear, and it is quite useful to have
a convenient term for this common phenomenon of user code being damaged
by inappropriate attempts to optimize.
```

##### ↳ ↳ Re: Determning length of varable length string

- **From:** "zpr..." <ua-author-17086607@usenetarchives.gap>
- **Date:** 1995-03-03T20:51:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p7@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap>`

```
de··.@cs.··u.edu (Robert Dewar) wrote:
› 
› I do not understand Daniel Thomas' comment about testing the last half 
…[4 more quoted lines elided]…
› this to hand optimize the code may in fact pessimize it.
I'm sorry, but I sure don't know what Cobol compiler you could be
thinking of. I benchmarked this on my system and the results were as I
described. How could a compiler come up with anything to perform the
check any faster, when the string could contain a different number of
characters each time? Do you think the routines previously described are
going to be interpreted by the compiler as a routine to check the length
of a variable and be magically transformed into a single call to return
the length? If the maximum possible size of the field is 2000 characters
and the actual length of the field is 1 character, then the original
method everyone proposed will perform the test for each position of the
string a character at a time 2000 times. My routine would perform 1 test
for characters 1001-2000 and determine that it is all spaces, and then
perform the single test 1000 times, performing 1001 operations instead of
2000. If you think that doesn't save time, then I don't think you have
done much benchmarking. As a reminder to those that didn't read my
response, I didn't propose that as the perfect solution but just a
simplistic approach (and I also suggested further ways to improve the
algorithm) to saving execution time, if indeed that particular function
was worth optimizing. If my response is still not making this clear, and
anyone is interested, then I can post the actual code, although I have to
admit I am pretty lame when it comes to "cutting" the code from my Cobol
editor into this posting.


-
DANIEL THOMAS (Dan) ZPR··.@pro··y.com
Louisville, KY
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "sbpa..." <ua-author-17087481@usenetarchives.gap>
- **Date:** 1995-03-04T04:51:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p13@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap>`

```
Daniel Thomas (ZPR··.@pro··y.com) wrote:
: string a character at a time 2000 times. My routine would perform 1 test
: for characters 1001-2000 and determine that it is all spaces, and then
: perform the single test 1000 times, performing 1001 operations instead of
: 2000.

Where did the 1000 operations to test characters 1001-2000 go?

Your performance difference is probably explained by the fact that there
is an i86 CPU instruction (REPE CMPS - find non-matching bytes) for examining
N characters "at once". The compiler is likely generating this instruction
for the all-spaces check.

Regards,
Douglas Parker
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

_(reply depth: 4)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-05T16:22:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p14@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap> <gap-f264fe72eb-p14@usenetarchives.gap>`

```
"Your performance difference is probably explained by the fact that there
is an i86 CPU instruction (REPE CMPS - find non-matching bytes) for examining
N characters "at once". The compiler is likely generating this instruction
for the all-spaces check."

yes, and of course the compiler should also generate this instruction for
an INSPECT (Realia certainly does), and even for a written out loop using
VARYING (my version of Realia doesn't do that, but it should).

Actually, I would guess that on the P6, one should stay away from this
CISC instruction in any case. On the P6, and even on the Pentium and 486,
you often find that the fancy instructions run slower than a written out
stream of simple instructions -- this is typical of RISC implementaions,
and the only reason that these chips still have the junk CISC instructions
on them is for compatibility with old code.

So actually, you may well find that on the P6, the specific test for the
second half being all blanks does indeed pessimize the code and make it
run slower than the VARYING loop!
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

_(reply depth: 4)_

- **From:** "jea..." <ua-author-17073875@usenetarchives.gap>
- **Date:** 1995-03-06T21:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p14@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap> <gap-f264fe72eb-p14@usenetarchives.gap>`

```
In <3j9d7i$t.··.@hob··a.edu>, sbp··.@moe··a.edu (Sheila B.
Parker) writes:

› Your performance difference is probably explained by the fact that there
› is an i86 CPU instruction (REPE CMPS - find non-matching bytes) for examining
› N characters "at once". The compiler is likely generating this instruction
› for the all-spaces check.

Actually, the i86 scan instruction is SCAS, not CMPS. The latter
compares two buffers.

--------------------------------------------------------------------------
= Uwe Baemayr = Internet: u.··.@li··t.com =
= Principal Programmer = or: jea··.@hue··s.edu =
= Liant Software Corporation = Compuserve: 74774,47 =
--------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

_(reply depth: 5)_

- **From:** "sbpa..." <ua-author-17087481@usenetarchives.gap>
- **Date:** 1995-03-07T18:13:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p16@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap> <gap-f264fe72eb-p14@usenetarchives.gap> <gap-f264fe72eb-p16@usenetarchives.gap>`

```
Uwe Baemayr (jea··.@hue··s.edu) wrote:
[snip]
: Actually, the i86 scan instruction is SCAS, not CMPS. The latter
: compares two buffers.

Oops.
Thanks for the correction.
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-05T11:02:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p13@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap>`

```
Daniel, at the machine level, there is no such thing as a "single test" for
1000 characters being blank. It is a loop (explicit at the machine code level
in a RISC machine, or implicit at the microcode level in a CISC machine).
If you write an explicit loop at the source level, it should be transformed
into exactly the same code as the "single" test you are talking about.

Of course I realize a lot of COBOL compilers generate rubbish code that is
very poorly optimized, but I think it is unwise to *assume* that your
compiler generates poor code and to second guess it. I am confident the
Wang compiler would generate the same code for both cases, and I would
be surprised it the Dec Alpha COBOL compiler would not generate the same
code in both cases.

THe fact that your measurements for one particular compiler show that it is
not doing a good job of code optimization does not speak for COBOL, or for
all COBOL compilers, and I *still* think that it is a bad idea to do this
kind of hand optimization unless you have performance requirements that can
be met in no other way.
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-05T11:05:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p13@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap>`

```
I just ran a test using INSPECT, and certainly an ancient version of the
Realia compiler (from back in the days when I worked on it) generates
essentially optimal x86 code for this test using INSPECT, which in COBOL
is the most natural way to write a loop.

Realia does NOT generate good code if the loop is made explicit using
PERFORM VARYING. This is because at that time it did no loop optimizations.
We always talked of doing loop optimizations, but our code was already
faster than any other compiler we looked at (yes, Daniel, I have done
*quite* a bit of COBOL benchmarking :-)

Perhaps by now, the good folks at Realia have tuned things up and the
code is indeed optimized by now, I don't know. Anyway INSPECT is really
the natural way to write this test in COBOL in any case.
```

###### ↳ ↳ ↳ Re: Determning length of varable length string

- **From:** "zpr..." <ua-author-17086607@usenetarchives.gap>
- **Date:** 1995-03-05T14:21:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f264fe72eb-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f264fe72eb-p13@usenetarchives.gap>`
- **References:** `<3i0o89$nia@newsbf02.news.aol.com> <gap-f264fe72eb-p7@usenetarchives.gap> <gap-f264fe72eb-p13@usenetarchives.gap>`

```
sbp··.@moe··a.edu (Sheila B. Parker) wrote:
› 
› Daniel Thomas (ZPR··.@pro··y.com) wrote:
› : string a character at a time 2000 times.  My routine would perform 1 
› test 
› : for characters 1001-2000 and determine that it is all spaces, and then 
 
› : perform the single test 1000 times, performing 1001 operations instead 
› of 
…[13 more quoted lines elided]…
› Douglas Parker
My english language description of my routine must not have been very
good because no one has responded that seemed to understand my point. My
example dealt with a variable length string with a maximum size of 2000
characters. My point was that if the string would often be less than
1000 characters, then performance could be improved by adding an
additional test. This was the most rudimentary example and could easily
be improved. Here is some sample code:
01 USENET-VAR.
02 WS-SUB
PIC 9(4) COMP-6.
02 VAR-LENGTH-STRING PIC X(2000).

02 VAR-LENGTH-ARRAY REDEFINES VAR-LENGTH-STRING.
05 VAR-LENGTH-POS PIC X
OCCURS 2000 TIMES.
* (I recommend adding following data items)
02 VAR-LENGTH-STRING-2 REDEFINES VAR-LENGTH-STRING.
05 VAR-LENGTH-STRING-A PIC X(1000).

05 VAR-LENGTH-STRING-B PIC X(1000).

.......
100-ORIGINAL-METHOD.
PERFORM NULL-PARAGRAPH
VARYING WS-SUB
FROM 2000 BY -1
UNTIL VAR-LENGTH-POS (WS-SUB) > SPACES.
*
NULL-PARAGRAPH.
*
.......
200-IMPROVED-METHOD.
IF VAR-LENGTH-STRING-B = SPACES
* (above is test for characters 1001-2000 and is a single
operation)
PERFORM NULL-PARAGRAPH
WS-SUB
FROM 2000 BY -1
UNTIL VARY-LENGTH-POS (WS-SUB) > "
"
ELSE
PERORM 100-ORIGINAL-METHOD.
.....
Another option in many Cobol dialects (Cobol 85), would replace
IF VAR-LENGTH-STRING-B = SPACES
with
IF VAR-LENGTH-STRING (1000:1000)
which uses a new capability called reference modification


-
DANIEL THOMAS (Dan) ZPR··.@pro··y.com
Louisville, KY
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
