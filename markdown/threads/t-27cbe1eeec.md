[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# level numbers 77/78

_12 messages · 8 participants · 1999-01 → 1999-02_

---

### Re: level numbers 77/78

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36AE0DC5.69844F77@home.com>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com>`

```
Harish Murthy wrote:
 >
 > HI
…[3 more quoted lines elided]…
 > - Harish

That is an odd question.  Are you trying to learn COBOL without a
reference manual?

Now if you asked if we use 77 (or 66), that would probably get a fair
amount of answers and discussion.
```

#### ↳ Re: level numbers 77/78

- **From:** fneale@no1.com.au
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78s4fe$6tb$1@nnrp1.dejanews.com>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com>`

```
In article <36AE0DC5.69844F77@home.com>,
  Howard Brazee <NOSPAMbrazee@home.com> wrote:
> Harish Murthy wrote:
>  >
…[11 more quoted lines elided]…
>

Actually, that raises a point of curiosity. Does anyone out there actually
use level 66?

In fact, does anyone still use level 77?

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: level numbers 77/78

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B1C317.3780000@ASPMnetdoor.com>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com>`

```
fneale@no1.com.au wrote:

> In article <36AE0DC5.69844F77@home.com>,
>
…[7 more quoted lines elided]…
> In fact, does anyone still use level 77?

I used 77 in regularly until about 10 years ago although it still is created
in a generated shell our shop uses.  Only use level 66 for an "after the fact"
redefinition of usually related fields necessary for debugging.  The record
layout is in a copy statement and the 66 level can be easily removed when a
program goes back into production.  My only occasion to use 78 is to hold a
count of the number of entries in a table defined later in the code.
```

###### ↳ ↳ ↳ Re: level numbers 77/78

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b5e828.538780956@news.freeserve.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com> <36B1C317.3780000@ASPMnetdoor.com>`

```
On Fri, 29 Jan 1999 08:17:59 -0600, Warren Porter
<warrenp@ASPMnetdoor.com> wrote:


>  My only occasion to use 78 is to hold a
>count of the number of entries in a table defined later in the code.

Under which compiler. 78 in Micro Focus terminology is a constant like
you'd use #define in C. You couldn't use it 'hold' anything as it's
replaced at compile time.
```

###### ↳ ↳ ↳ Re: level numbers 77/78

_(reply depth: 4)_

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B5F7DD.B07432E2@ASPMnetdoor.com>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com> <36B1C317.3780000@ASPMnetdoor.com> <36b5e828.538780956@news.freeserve.net>`

```
Shaun C. Murray wrote:

> >  My only occasion to use 78 is to hold a
> >count of the number of entries in a table defined later in the code.
…[3 more quoted lines elided]…
> replaced at compile time.

It's AcuCobol85.  Also I use it just like the #define in C since I will never
change the contents of the table or number of entries while the program is
running.  If I add or remove a table entry, I change the value of the 78 level
and in only one place.

78  TABLE-SIZE   VALUE 32.
----
     05 TABLE-ENTRY OCCURS TABLE-SIZE.
----
       PERFORM  VARYING SUB1 FROM 1 BY 1 UNTIL SUB1 > TABLE-SIZE ... .
```

###### ↳ ↳ ↳ Re: level numbers 77/78

_(reply depth: 5)_

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b62d23.556440298@news.freeserve.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com> <36B1C317.3780000@ASPMnetdoor.com> <36b5e828.538780956@news.freeserve.net> <36B5F7DD.B07432E2@ASPMnetdoor.com>`

```
On Mon, 01 Feb 1999 12:52:14 -0600, Warren Porter
<warrenp@ASPMnetdoor.com> wrote:


>
>78  TABLE-SIZE   VALUE 32.


That's a relief. Exactly the same as Micro Focus COBOL.

Must say, 78 is one of my favourite extensions. Especially useful on
the PC.
```

##### ↳ ↳ Re: level numbers 77/78

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7Njs2.46$Fs.108988@news4.mia>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com>`

```
fneale@no1.com.au wrote:
>
>Actually, that raises a point of curiosity. Does anyone out there
>actually use level 66?

Very infrequently.

>In fact, does anyone still use level 77?

Yes.  Although 01 is sufficient, most compilers I use handle an 01
level differently for storage and alignment purposes.  The Unisys
A Series stores 77 entries in the stack and 01 entries as an array.
On those machines, using a 77 is more efficient.  Other than that,
it is mostly a matter of habit; I prefer using 77 for autonomous
data items with a picture, and 01 for group items.  This provides
a visual clue which I like, and that was what they were created to
be.  I see no advantage in using 01 over 77 for autonomous data
items with a picture.
```

##### ↳ ↳ Re: level numbers 77/78

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-JzcTsEiBdtRe@Dwight_Miller.iix.com>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com>`

```
On Fri, 29 Jan 1999 11:02:09, fneale@no1.com.au wrote:

> In article <36AE0DC5.69844F77@home.com>,
>   Howard Brazee <NOSPAMbrazee@home.com> wrote:
…[18 more quoted lines elided]…
> In fact, does anyone still use level 77?

I don't use 77 - but I have use 66 more than once recently - it comes 
in very handy for Y2K remediation.
```

##### ↳ ↳ Re: level numbers 77/78

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b1a319.258958222@news.freeserve.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com>`

```
On Fri, 29 Jan 1999 11:02:09 GMT, fneale@no1.com.au wrote:

>
>Actually, that raises a point of curiosity. Does anyone out there actually
…[3 more quoted lines elided]…
>

No.


(and never have)
```

##### ↳ ↳ Re: level numbers 77/78

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b36ef5.845666@news3.ibm.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com>`

```
rOn Fri, 29 Jan 1999 11:02:09 GMT, fneale@no1.com.au wrote:

>In article <36AE0DC5.69844F77@home.com>,
>  Howard Brazee <NOSPAMbrazee@home.com> wrote:
…[16 more quoted lines elided]…
>use level 66?
Yes, bur rather seldomly (When I cannot change a copy book, e.g.)


>
>In fact, does anyone still use level 77?

Yes, always (that is, when the data  item is not subdivided)  If the compiler doesn't make
a differencebetween  01 and 77, why shouldn't I use 77?  And if the compiler DOES make a
difference, I definitely SHOULD use 77 -: This implies: USE 77 levels whenever allowed


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: level numbers 77/78

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b5e8c8.538940876@news.freeserve.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com> <36b36ef5.845666@news3.ibm.net>`

```
On Sat, 30 Jan 1999 20:46:27 GMT, vbandke@ibm.net (Volker Bandke)
wrote:


>
>Yes, always (that is, when the data  item is not subdivided)  If the compiler doesn't make
>a differencebetween  01 and 77, why shouldn't I use 77?  And if the compiler DOES make a
>difference, I definitely SHOULD use 77 -: This implies: USE 77 levels whenever allowed
>

A valid answer but some compilers optimize better with group items and
it's not uncommon for programmers to have to think about the alignment
structure in memory on PC's. Particularly if you are using windows
API's or talking to foreign languages. A group item works better for
this than seperate 01's or 77's. 

You can also group items of a similar size together too for
compactness in memory and speed of access.
```

###### ↳ ↳ ↳ COBOL FIX...y2k, etc...FREE

_(reply depth: 4)_

- **From:** Jodi <marble@tds.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C88784.155B0739@tds.net>`
- **References:** `<36AD9C41.578CD49B@SPAM-NO.thewatercooler.com> <36AE0CE8.6E38BD9A@home.com> <36AE0DC5.69844F77@home.com> <78s4fe$6tb$1@nnrp1.dejanews.com> <36b36ef5.845666@news3.ibm.net> <36b5e8c8.538940876@news.freeserve.net>`

```
Free download available at:

http://www.vnsinc.com/Y2K
 it's quick, and easy....call for a password and use, that's
it!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
