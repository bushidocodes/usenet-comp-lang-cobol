[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help converting a copylib

_12 messages · 11 participants · 1998-05_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Help requests and how-to`](../topics.md#help)

---

### Help converting a copylib

- **From:** "rwal..." <ua-author-7393964@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

Hello,

I am writing a conversion program that reads one version of a record
and writes it as another. I am recieving a data exception error using
the following approach.

Data:

01 INPUT.
05 INPUT-DATA PIC X(100).

05 MONTHS-TABLE OCCURS 24 TIMES INDEXED BY MONTH-X
10 MONTH-DATA COMP-3 PIC S9(7).

01 OUTPUT.
05 OUTPUT-DATA PIC X(100).

05 MONTH-TABLE-OUT OCCURS 24 TIMES INDEXED BY MONTH-X
10 MONTH-DATA-OUT COMP-3 PIC S9(9). <-----increased in size


Logic:


MOVE INPUT-DATA TO OUTPUT-DATA.
PERFORM 1000-MONTH-MOVE THRU 1000-EXIT.
VARYING MONTH-X FROM 1 BY 1
UNTIL MONTH-X > 24

1000-MONTH-MOVE.
MOVE MONTH-DATA (MONTH-X) TO
MONTH-DATA-OUT (MONTH-X).

1000-EXIT.
EXIT.

I recieve a data exception when it performs the 1000 paragraph. Is
this correct or should it be done differently? Thank in advance.
Rich
```

#### ↳ Re: Help converting a copylib

- **From:** "bobh" <ua-author-514237@usenetarchives.gap>
- **Date:** 1998-05-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

rwa··.@nyc··r.com wrote:
› 
› Hello,
…[35 more quoted lines elided]…
› Rich

Normally Data Exception is when you tty to shove something other than
COMP-3 data into a COMP-3 (Pack Sign) field (my moving/calculation).
My rule of thumb is to set numeric flds to a value (i.e. 0). What if
MONTH-DATA only had 12 values?
```

#### ↳ Re: Help converting a copylib

- **From:** "aacin..." <ua-author-17071800@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

Rich writes :
<<<
Hello,

I am writing a conversion program that reads one version of a record
and writes it as another. I am recieving a data exception error using
the following approach.

Data:

01 INPUT.
05 INPUT-DATA PIC X(100).

05 MONTHS-TABLE OCCURS 24 TIMES INDEXED BY MONTH-X
10 MONTH-DATA COMP-3 PIC S9(7).

01 OUTPUT.
05 OUTPUT-DATA PIC X(100).

05 MONTH-TABLE-OUT OCCURS 24 TIMES INDEXED BY MONTH-X
10 MONTH-DATA-OUT COMP-3 PIC S9(9). <-----increased in size


Logic:


MOVE INPUT-DATA TO OUTPUT-DATA.
PERFORM 1000-MONTH-MOVE THRU 1000-EXIT.
VARYING MONTH-X FROM 1 BY 1
UNTIL MONTH-X > 24

1000-MONTH-MOVE.
MOVE MONTH-DATA (MONTH-X) TO
MONTH-DATA-OUT (MONTH-X).

1000-EXIT.
EXIT.

I recieve a data exception when it performs the 1000 paragraph. Is
this correct or should it be done differently? Thank in advance.
Rich

›››

Try defining an index with a different name on the second table. What you
posted should generate a compiler error but some COBOL's ( Cobol II comes to
mind) will actually allow you to use an index defined on one table against
another ( is it a bug or a feature? Only Bill Gates knows). Since an index is
a displacement based on the row size of the table if you use one accross two
tables of different sizes BANG! 0C7.

Hope this helps,
Jim Castro
```

#### ↳ Re: Help converting a copylib

- **From:** "in..." <ua-author-17074430@usenetarchives.gap>
- **Date:** 1998-05-13T11:44:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

On Wed, 13 May 1998 01:36:41 GMT, rwa··.@nyc··r.com wrote:
› 
›     05 MONTHS-TABLE      	OCCURS 24 TIMES INDEXED BY MONTH-X
…[6 more quoted lines elided]…
› 10 MONTH-DATA-OUT   COMP-3 PIC S9(9).  <-----increased in size

The only thing I can see is the similar name used for the indexes of
both tables. Most manuals forbid this outright and only the very
lenient compilers might let this through.

Try and give the two indexes different names...
Johan Potgieter
www.choicetraining.com
in··.@cho··g.com
```

##### ↳ ↳ Re: Help converting a copylib

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7c40fe7acf-p4@usenetarchives.gap>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com> <gap-7c40fe7acf-p4@usenetarchives.gap>`

```

Johan Potgieter wrote:
› 
› On Wed, 13 May 1998 01:36:41 GMT, rwa··.@nyc··r.com wrote:
…[14 more quoted lines elided]…
› Try and give the two indexes different names...

The pointer could be the problem. But did't he say data exception, and
not protection exception. Could it be as simple as non numeric data in
the input table fields?
```

###### ↳ ↳ ↳ Re: Help converting a copylib

- **From:** "jim k" <ua-author-718715@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7c40fe7acf-p5@usenetarchives.gap>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com> <gap-7c40fe7acf-p4@usenetarchives.gap> <gap-7c40fe7acf-p5@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Johan Potgieter wrote:
…[20 more quoted lines elided]…
› the input table fields?

It could be. However, an index register contains a value equal to the
offset in the table, not an occurrence number.

When you set an index register to a value, it computes this offset as
the length of one occurrence times the occurrence number, minus the
length of one occurrence. It then points to the beginning of the area
desired.

In the above example, you might assume that index register will be
computed for the first specification of month-x as an index register.
The length of the occurrence for the first table is 4 bytes. The length
of the occurrence for the second table is 5 bytes. S9(7) comp-3 = 4
bytes, S9(9) comp-3 = 5 bytes.

If month-x takes its settings from the first table, accessing anything
after the first occurrence in the second table would result in an '0C7'.


Jim K.

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"The important thing is to stop lying to yourself.  A man 
 who lies to himself, and believes his own lies, becomes 
 unable to recognize the truth, either in himself or in 
 anyone else, and he ends up losing respect for himself 
 as well as for others.  When he has no respect for anyone, 
 he can no longer love and, in order to divert himself, 
 having no love in him, he yields to his impulses, indulges 
 in the lowest forms of pleasure, and behaves in the end 
 like an animal, in satisfying his vices. 
 And it all comes from lying -- lying to others and to yourself."

        --Feodor Mikhailovich Dostoyevsky from his 1880 work, 
          "The Brothers Karamazov"


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

###### ↳ ↳ ↳ Re: Help converting a copylib

- **From:** "in..." <ua-author-17074430@usenetarchives.gap>
- **Date:** 1998-05-13T15:32:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7c40fe7acf-p5@usenetarchives.gap>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com> <gap-7c40fe7acf-p4@usenetarchives.gap> <gap-7c40fe7acf-p5@usenetarchives.gap>`

```

On Wed, 13 May 1998 11:39:45 -0500, Thane Hubbell
wrote:


›› Try and give the two indexes different names...
› 
› The pointer could be the problem.  But did't he say data exception, and
› not protection exception.  Could it be as simple as non numeric data in
› the input table fields?
Thane, you could very well be right. Or something illegal he does wih
the indexes. Difficult to say. I get suspicious and uncomfortable
when I see code where there are periods missing - as in his 1st
PERFORM. Then I almost want to see the full code first....
Johan Potgieter
www.choicetraining.com
in··.@cho··g.com
```

#### ↳ Re: Help converting a copylib

- **From:** "bhkr..." <ua-author-17084303@usenetarchives.gap>
- **Date:** 1998-05-13T23:18:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p8@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

In article <355··.@new··r.com>,
rwa··.@nyc··r.com wrote:
› 
› Hello,
…[36 more quoted lines elided]…
› 

Hi, Rich.

Couple of things - how many times is it going through the loop before it
bombs? If it's the first time, check your input data. Also, is this the
exact code you're using? If it is, the period at the end of your Perform ..
Through is going to cause you grief. The Index will never be set before it
gets into the 1000 loop.

Good luck.

Bernie Krause
Winnipeg, MB

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: Help converting a copylib

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7c40fe7acf-p8@usenetarchives.gap>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com> <gap-7c40fe7acf-p8@usenetarchives.gap>`

```

Dennis J. Minette wrote (and I snipped the irrelevants):

› The regular posters seem to be an exceptionally experienced group of master
› coders.

:))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

A Frog, with a ten feet smile
```

#### ↳ Re: Help converting a copylib

- **From:** "hca..." <ua-author-6878906@usenetarchives.gap>
- **Date:** 1998-05-15T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p10@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

rwa··.@nyc··r.com wrote:

› Hello,
› 
…[36 more quoted lines elided]…
› Rich

First of all, I don't think you can vary an index in a perform varying
statement. Indexes have to be set. I believe the logic statement
should be:

SET MONTH-X TO 1.
PERFORM 1000-MONTH-MOVE UNTIL MONTH-X > 24.

1000-MONTH-MOVE.
MOVE...
SET MONTH-X UP BY 1.

Also I'd probably be happier with two different indexes.

Harry Carter
hca··.@clu··s.net - finger for PGP key
Home Page: http://www.mcs.net/~hcarter

"Make no little plans; they have no magic to stir men's blood."
Daniel Burnham
```

##### ↳ ↳ Re: Help converting a copylib

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7c40fe7acf-p10@usenetarchives.gap>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com> <gap-7c40fe7acf-p10@usenetarchives.gap>`

```

There have been lots of other replies to this thread (some of them likely -
some not so likely) - but just so there is no confusion,

Standard COBOL fully supports VARYING an index-name (the thing in an
INDEXED BY phrase) in a PERFORM statement.

P.S. but as many have pointed out, it does NOT support a period in the
middle of a PERFORM VARYING statement. However, it would be really odd if
this "error" would cause a run-time error and not a compile-time error. I
hope the original poster tells the group what actually turned out to be the
problem.
```

#### ↳ Re: Help converting a copylib

- **From:** "james walker" <ua-author-838022@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7c40fe7acf-p12@usenetarchives.gap>`
- **In-Reply-To:** `<3558f0a0.8695640@news.nycap.rr.com>`
- **References:** `<3558f0a0.8695640@news.nycap.rr.com>`

```

try using a different index name, follow the rules, keep names unique-don't
duplicate.

rwa··.@nyc··r.com wrote in article
<355··.@new··r.com>...
› Hello,
› 
…[37 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
