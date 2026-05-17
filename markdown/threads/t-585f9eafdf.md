[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS Cobol & rounding

_13 messages · 8 participants · 1998-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MVS Cobol & rounding

- **From:** "saint" <ua-author-38667@usenetarchives.gap>
- **Date:** 1998-04-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`

```

Given:
field-a pic 9(3) value 0.
field-b pic 9(7) value 2600.
field-c pic 9(7) value 3094.

The following code produces an incorrect result:

compute field-a rounded = (field-b / field-c) * 100

The result should be 84, but the above code gives a value to field-a of 80.

The line below gives a correct result:

compute field-a rounded = 100 * field-b / field-c.

I suspect a compiler issue. In the first example, it appears from the
generated assembler code that the program is rounding (SRP) before dividing
(DP). In the second, MP takes place first, then SRP, then DP.

Any ideas?

P.
```

#### ↳ Re: MVS Cobol & rounding

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`

```

Assuming you are using an IBM compiler, you need to read the appendix on
"intermediate results" - which can lead to some VERY strange (but
documented) results. The most famous one is that if you have

compute integer-field - (7 / 4) * 4

You will get an answer of 4 and not 7 (Well documented, fully ANSI
conforming - and most certainly NOT what you would expect)
```

##### ↳ ↳ Re: MVS Cobol & rounding

- **From:** "saint" <ua-author-38667@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p2@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p2@usenetarchives.gap>`

```

Agreed; but that's because the field is defined as integer, and the
fraction is being dropped. In my example, the intermediate result is
0.840330. Everything after the "0.8" is being lost, not the whole
fraction.

compute A rounded = (2600/3094) * 100
= (.840330) * 100
= 84
where A is pic 9(3).

But my result is 80 not 84.

William M. Klein wrote in article
<6hdpqn$a.··.@sjx··m.com>...
› Assuming you are using an IBM compiler, you need to read the appendix on
› "intermediate results" - which can lead to some VERY strange (but
…[6 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: MVS Cobol & rounding

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p3@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p2@usenetarchives.gap> <gap-585f9eafdf-p3@usenetarchives.gap>`

```



Saint wrote in message <6hemk4$l.··.@bgt··t.net>...
› Agreed; but that's because the field is defined as integer, and the
› fraction is being dropped.  In my example, the intermediate result is
…[9 more quoted lines elided]…
› 

I am curious, what makes you think that the IBM compiler will "save" 6
places to the right of the decimal point? The results seem to indicate that
it is storing 1, but no more. Again, the rules on "intermediate results"
are fairly complex - I don't know them by heart, but I don't know WHY you
think it will save 6 decimal places.

P.S. The rule that I think is impacting you is that none of your fields are
defined with ANY decimal points - so the intermediate result would normally
have none - but because you have specified ROUNDED, this increases to 1.

Try doing the same code with

compute A rounded = (2600.000 / 3094.000) * 100

and I think you MIGHT get the result you want/expect.


› William M. Klein  wrote in article
› <6hdpqn$a.··.@sjx··m.com>...
…[9 more quoted lines elided]…
›
```

#### ↳ Re: MVS Cobol & rounding

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-04-18T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`

```

Saint wrote:
› 
› Given:
…[16 more quoted lines elided]…
› (DP).  In the second, MP takes place first, then SRP, then DP.

Ooooo, this looks *tasty*... when I get into the shop on Monday I'll
fire off a few compiles and see. What are you using, IKFCBL00 or
IGYCTCRL? Any special PARMs?

DD
```

##### ↳ ↳ Re: MVS Cobol & rounding

- **From:** "saint" <ua-author-38667@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p5@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p5@usenetarchives.gap>`

```

The Goobers wrote in article
<353··.@er··s.com>...
› Ooooo, this looks *tasty*... when I get into the shop on Monday I'll
› fire off a few compiles and see.  What are you using, IKFCBL00 or
› IGYCTCRL?  Any special PARMs?
› 
› DD

IGYCRCTL

OPTIONS IN EFFECT:
NOADATA
NOADV
APOST
AWO
BUFSIZE(31744)
NOCMPR2
NOCOMPILE(E)
NOCURRENCY
DATA(31)
NODBCS
NODECK
NODUMP
DYNAM
NOEXIT
FASTSRT
FLAG(W,E)
NOFLAGMIG
NOFLAGSTD
NOIDLGEN
INTDATE(ANSI)
LANGUAGE(UE)
LIB
LINECOUNT(59)
NOLIST
MAP
NONAME
NONUMBER
NUMPROC(NOPFD)
OBJECT
OFFSET
OPTIMIZE(STD)
OUTDD(SYSOUT)
PGMNAME(COMPAT)
RENT
RMODE(AUTO)
NOSEQUENCE
SIZE(4194304)
SOURCE
SPACE(1)
NOSSRANGE
TERM
NOTEST
TRUNC(BIN)
NOTYPECHK
NOVBREF
NOWORD
XREF(FULL)
ZWB
```

#### ↳ Re: MVS Cobol & rounding

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`

```
Sure, code it right. The compute statement uses
field-a for
it's intermediate answers ... it does not have a
decimal place.







Sure, code it right.Â  The compute statement
uses field-a for
it's intermediate answers ... it does not have a
decimal place.
```

##### ↳ ↳ Re: MVS Cobol & rounding

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p7@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p7@usenetarchives.gap>`

```

Donald Tees wrote in message <6hffa5$qms$1.··.@new··s.net>...
Sure, code it right. The compute statement uses field-a for
it's intermediate answers ... it does not have a decimal place.

Then surely the answer would have been 0 ???
As the first number divided by the second was 0.84.....
Surely this would have been truncated to 0.

Mike.







Â 

Donald Tees wrote in message <6hffa5$qms$1.··.@new··s.net>...
Sure, code it right.Â  The compute
statement uses field-a for
it's intermediate answers ... it does not
have a decimal place.
Â 
Then surely the answer would have been 0
???
As the first number divided by the second
was 0.84.....
Surely this would have been truncated to
0.
Â 
Mike.
```

###### ↳ ↳ ↳ Re: MVS Cobol & rounding

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p8@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p7@usenetarchives.gap> <gap-585f9eafdf-p8@usenetarchives.gap>`

```

On Mon, 20 Apr 1998 17:15:48 +0200, "Mike Rochford"
wrote:

Â« all snippo !! Â»

Michael, my man! What I have caused to go away is why there are
those of us who think that anybody who would use:

X-Newsreader: Microsoft Outlook Express 4.72.2106.4
X-Mimeole: Produced By Microsoft MimeOLE V4.72.2106.4

is totally and completely fucked!!

GET OUT OF THIS DISGUSTING HABIT!

Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: MVS Cobol & rounding

_(reply depth: 4)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p9@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p7@usenetarchives.gap> <gap-585f9eafdf-p8@usenetarchives.gap> <gap-585f9eafdf-p9@usenetarchives.gap>`

```

Richard Anderson wrote:
› 
› On Mon, 20 Apr 1998 17:15:48 +0200, "Mike Rochford"
…[12 more quoted lines elided]…
› GET OUT OF THIS DISGUSTING HABIT!

(ear defenders off>
How do you have a problem reading that? I didn't have a problem with
Nutscrape. And it looks very pretty. Hasn't Agent moved with the
times? I thought it had.


Charles F Hankel, Wirral, UK
Freelance Systems Professional
Surfing through this life on the Y2K wave
-----------------------------------------
Antispam: take away my breakfast to reply
```

###### ↳ ↳ ↳ Re: MVS Cobol & rounding

_(reply depth: 5)_

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p10@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p7@usenetarchives.gap> <gap-585f9eafdf-p8@usenetarchives.gap> <gap-585f9eafdf-p9@usenetarchives.gap> <gap-585f9eafdf-p10@usenetarchives.gap>`

```

On Tue, 21 Apr 1998 23:11:12 +0100, Charles F Hankel
wrote:

› Richard Anderson wrote:
 
›› GET OUT OF THIS DISGUSTING HABIT!
› 
…[3 more quoted lines elided]…
› times?  I thought it had.

Agent, bless its heart, has indeed moved with the times. I,
however, amidst a senior moment, instructed the beloved program to
display messages in such a fashion that I would become vexed. It
worked beyond my wildest imagination. Sigh!
Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: MVS Cobol & rounding

_(reply depth: 4)_

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-585f9eafdf-p9@usenetarchives.gap>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net> <gap-585f9eafdf-p7@usenetarchives.gap> <gap-585f9eafdf-p8@usenetarchives.gap> <gap-585f9eafdf-p9@usenetarchives.gap>`

```


Richard Anderson wrote in message <6hhgbh$b.··.@dfw··m.com>...
› On Mon, 20 Apr 1998 17:15:48 +0200, "Mike Rochford"
› wrote:
…[16 more quoted lines elided]…
› anderson aatt pobox fullstop com

Rick, my boy, perhaps you should get hold of Donald (to whom I replied and
let him know). My news reader responded in the format of the posting to
which I replied !!!

Sorry, I'll try not to do it again !!!


Mike.
```

#### ↳ Re: MVS Cobol & rounding

- **From:** "clif ivy" <ua-author-17073774@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-585f9eafdf-p13@usenetarchives.gap>`
- **In-Reply-To:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`
- **References:** `<6hdj64$oig@bgtnsc03.worldnet.att.net>`

```

Everyone's points about needing to check the documentation to see how
many decimal places are defined for intermediate results are right on
the money to figure out **why** you are getting the results you are.

I particularly liked the note about the documentation explaining why you
get a result of "4" from the calculation x = (7 / 4) * 4.

HOWEVER, it is less important to know why you get wrong results than it
is to know how to get right results.

Any calculation method that depends on the number of decimal places
calculated for intermediate results can have problems depending on whose
assumptions are followed to set the number of places. If you were doing
the 2600/3094 calculation with pencil and paper, you would probably stop
with "0.84", once you saw the next digit would be zero. In another
message from you in this string, you show a result of ".840330". My
trusty $3 8-digit calculator gives (with no effort for the extra
decimals) "0.8403361".

All three answers are more or less right; they are just carried out to
different numbers of decimal places. You would probably be satisfied
with any of them for your own calculations, because you would be
following your own assumptions about how many decimal places to use in
your intermediate calculation (first doing 2600/3094, and then
multiplying that result by 100).

However, using COBOL or any sort of advanced language puts you at the
mercy of the assumptions of the people who wrote the compiler you are
using, on top of the assumptions of the people who wrote the
specifications for the language.

The REAL answer, as you have discovered in your second example, is to
rearrange the calculations so that the number of decimal places defined
for intermediate results has little or no impact on your final result.
Specifically, this means making the divide the last operation.

Apply what you have done to this specific problem to *all* your
calculations where you have divides followed by multiplication. Use
some 8th grade algebra to work out the calculation so that the division
comes *last*.

If you have programmers in your shop who won't immediately understand
why your COBOL reads:
compute field-a rounded = 100 * field-b / field-c.
when the specification reads:
"calculate field-a as field-b / field-c, times 100; round the result",
then put in a comment explaining that the calculation has been
rearranged to minimize rounding errors.

If your auditors don't understand that ((a/b)*c)=((a*c)/b), then you've
got **real** problems.

Friends don't let friends make assumptions about decimal places...

Saint wrote:
› 
› Given:
…[20 more quoted lines elided]…
› P.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
They're just my opinions...
Clifton Ivy, Mgmt Info, Purdue University
cl··.@pur··e.edu
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
