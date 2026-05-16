[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student Question

_4 messages · 2 participants · 1999-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Re: Student Question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<GF_r2.40$Mk.105952@news3.mia>`
- **References:** `<36AFCB26.325377D2@yahoo.com> <rURr2.3657$oi.3907686@news3.mia> <36AFF9A8.B506BAAE@yahoo.com>`

```
NG Profile wrote:
>
>Thanks for the advice Judson.  That is why I would like to find maybe some
…[7 more quoted lines elided]…
>I left my "eureka."  Thanks again.

I wrote a brief introductory tutorial on arrays for use in QBasic, and have
posted it several times for people in QBasic newsgroups.  I'll take a stab
at modifying it for COBOL.  You also may want to obtain an excellent COBOL
tutorial "Teach Yourself COBOL in 24 Hours" by Thane Hubbell.  Thane is a
great guy who frequents these COBOL newsgroups, and who worked hard on the
table handling section of the book.  For a more advanced text, you might try
"COBOL Unleashed" by Jon Wessler and several other authors, including Thane,
myself, and several other contributors to the COBOL newsgroups.

Data items are referenced by using their data name, such as STREET-ADDRESS,
CUSTOMER-NAME, etc.  You can think of a table as a mechanism for having a
number of data items, all with the same name.  This collection of data items,
all with the same name, is called a 'table'.  You can create a table in COBOL
using the OCCURS clause of a data declaration.

    03  COUNT    PIC  9(06)  OCCURS 20 TIMES.

This creates a table of 20 data items, all named COUNT.  In COBOL 85 the first
element in a table is always 1, and the last element is defined in the OCCURS.
Sometimes that maximum number is determined at runtime by the contents of
another numeric data item specified in the OCCURS.  For example:

    03  MAX      PIC  9(02)  VALUE 15.
    03  COUNT    PIC  9(06)  OCCURS 1 TO 20 TIMES DEPENDING ON MAX.

In this example, as the value of MAX is changed in the program, it will
be as if the OCCURS clause was simultaneously changed to the same value.

Because each data item has the same data name, each time you reference the
table, you must somehow indicate which of the several data items you are
referring to.  To do this we use what is called a 'subscript', as in
mathematical notation.  Since most programming languages use straight text,
and do not support the tiny fonts used in printed subscripts, the subscript
is typically enclosed in parenthesis () following the data name.

    COUNT(1)     Data name COUNT, #1
    COUNT(2)     Data name COUNT, #2
    COUNT(12)    Data name COUNT, #12

In some programming languages (e.g. C/C++), subscripts are enclosed in square
brackets [] instead of parenthesis (), but they do the same thing.

Tables and subscripting, along with loops, are some of the most powerful
features of programming languages.  They allow you to write one set of
instructions which can be applied over and over to different data.  This is
accomplished by using a numeric data item instead of a numeric literal as a
subscript into the table, like this:

    COUNT(SUB)   Data name COUNT, # contained in SUB

Obviously, SUB must be a numeric data item, and the value must be an integer
within the valid subscript range.  To add 5 to each data item COUNT in the
table, you could code a simple loop like this:

    PERFORM VARYING SUB FROM 1 BY 1 UNTIL SUB > 5
        ADD 1 TO COUNT(SUB).

The data item in the table may be any normal COBOL data item, even a group
item.  For example:

    03  FRIEND-TABLE        OCCURS 100 TIMES.
        05  FRIEND-NAME         PIC  X(20).
        05  FRIEND-STREET       PIC  X(20).
        05  FRIEND-CITY-ST      PIC  X(20).
        05  FRIEND-ZIP          PIC  9(05).

The OCCURS clause may not be used on a level 01, 66, 77 or 88 item, but only
on levels 02 through 49.  You may not REDEFINE an item containing an OCCURS
clause, but you may REDEFINE an item subordinate to an item containing an
OCCURS clause.

Tables with one subscript are very useful, but sometimes there are situations
when we need more.  For example, say you have divided your city into a 10x20
grid, and you want to store the population of each grid square into a table.
You could do this:

    03  CITY-GRID-X      OCCURS 10 TIMES.
        05  CITY-GRID-Y      OCCURS 20 TIMES.
            07  CITY-POP         PIC  9(06).

This creates a table with 200 data items named CITY-POP, but now when you
reference it, you must specify two subscripts, one for each dimension:

    CITY-POP(1, 1)              CITY-POP grid at X=1, Y=1
    CITY-POP(3, 5)              CITY-POP grid at X=3, Y=5
    CITY-POP(10, 20)            CITY-POP grid at X=10, Y=20
    CITY-POP(SUBX, SUBY)        CITY-POP grid at SUBX, SUBY

If you wanted to store the population of each grid square for ten cities
you could do this:

    03  CITY-CITY        OCCURS 10 TIMES.
        05  CITY-GRID-X      OCCURS 10 TIMES.
            07  CITY-GRID-Y      OCCURS 20 TIMES.
                09  CITY-POP         PIC  9(06).

This creates a table with 2000 data items named CITY-POP, but when you
reference it, you must specify three subscripts, one for the city and one
for each dimension.  To sum the population of all the cities, you could
code this:

    03  TOTAL-POP        PIC  9(08).
    03  CITY             PIC  9(02).
    03  SUBX             PIC  9(02).
    03  SUBY             PIC  9(02).

    MOVE ZERO TO TOTAL-POP.
    PERFORM VARYING CITY FROM 1 BY 1 UNTIL CITY > 10
        AFTER VARYING SUBX FROM 1 BY 1 UNTIL SUBX > 10
            AFTER VARYING SUBY FROM 1 BY 1 UNTIL SUBY > 20
                ADD CITY-POP(CITY, SUBX, SUBY) TO TOTAL-POP.

As a matter of form, I prefer to indent my PIC and other clauses four more
spaces with each level of OCCURS.  This provides a clear visual cue when
you are scanning a record definition.

In addition to subscripting, COBOL provides a feature called 'indexing'.
Indexing works very similarly to subscripting, but there are differences.
First, an 'index' is defined as part of the table with which it is
associated, by using the INDEXED BY phrase of the OCCURS clause.  The city
table above could have been defined like this:

    03  TEMP             PIC  9(02).
    03  CITY-CITY        OCCURS 10 TIMES INDEXED BY CITY.
        05  CITY-GRID-X      OCCURS 10 TIMES INDEXED BY SUBX.
            07  CITY-GRID-Y      OCCURS 20 TIMES INDEXED BY SUBY.
                09  CITY-POP         PIC  9(06).

The above PERFORM would work on this table in the same way.  But if you want
to change the value of an index you normally must use the SET verb.  For
example:

    SET SUBX TO 4.
    SET SUBX UP BY 1.
    SET SUBX DOWN BY 2.
    SET TEMP TO SUBX.
    SET SUBY TO TEMP.
    SET SUBX TO SUBY.

Using indexes instead of subscripts can have advantages.  One is that you can
often write faster code using indexes, and the other is that you can use the
COBOL SEARCH verb on tables which have indexes declared.  But those are beyond
the scope of this brief introduction.
```

#### ↳ Re: Student Question

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<36b09551.10117198@news>`
- **References:** `<36AFCB26.325377D2@yahoo.com> <rURr2.3657$oi.3907686@news3.mia> <36AFF9A8.B506BAAE@yahoo.com> <GF_r2.40$Mk.105952@news3.mia>`

```
Great tutorial, it makes for excellent review.  We've covered and used these concepts
for 2  1/2 quarters now, but reading it again, so well presented, is a great study
device.  Do you think you'll present us with a similar guide to indexed tables and
perhaps search mechanisms?  We have not hit these quite as hard, as they are used
just a bit less often, tho our instructor has given lectures on each several times
with sample programs.  Thanks again, TS

On Thu, 28 Jan 1999 14:40:38 GMT ""Judson McClendon" <judmc123@bellsouth.net>" posted
to "comp.lang.cobol" about: "Re: Student Question" :

-->NG Profile wrote:
-->>
-->>Thanks for the advice Judson.  That is why I would like to find maybe some
-->>readings on the subject of tables to jar that switch.  I have a lot going
-->>on, 5 other classes, 4 kids, full-time job, so I know that is part of the
-->>problem.  I am a "visual" learner and know that once I get this thing worked
-->>out "visually" I will get beyond the hurdle.  This is what I love about
-->>computing in general.  These machines will constantly kick the crap out of
-->>you, but if you keep hammering away at it, the "eureka" experience will
-->>come.  When it comes to COBOL and tables I just need to find where the heck
-->>I left my "eureka."  Thanks again.
-->
-->I wrote a brief introductory tutorial on arrays for use in QBasic, and have
-->posted it several times for people in QBasic newsgroups.  I'll take a stab
-->at modifying it for COBOL.  You also may want to obtain an excellent COBOL
-->tutorial "Teach Yourself COBOL in 24 Hours" by Thane Hubbell.  Thane is a
-->great guy who frequents these COBOL newsgroups, and who worked hard on the
-->table handling section of the book.  For a more advanced text, you might try
-->"COBOL Unleashed" by Jon Wessler and several other authors, including Thane,
-->myself, and several other contributors to the COBOL newsgroups.

<snop: tutorial, excellent>

-->Judson McClendon      judmc123@bellsouth.net  (remove numbers)


TS  Atlanta, GA
```

##### ↳ ↳ Re: Student Question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Gb4s2.56$OS5.138618@news3.mia>`
- **References:** `<36AFCB26.325377D2@yahoo.com> <rURr2.3657$oi.3907686@news3.mia> <36AFF9A8.B506BAAE@yahoo.com> <GF_r2.40$Mk.105952@news3.mia> <36b09551.10117198@news>`

```
Thank you.  I don't have any plans to write anything else right now.
I usually write such posts when prompted by a particular request which
strikes me while in a writing mood. :-)
```

###### ↳ ↳ ↳ Re: Student Question

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<36b1d40a.4115750@news>`
- **References:** `<36AFCB26.325377D2@yahoo.com> <rURr2.3657$oi.3907686@news3.mia> <36AFF9A8.B506BAAE@yahoo.com> <GF_r2.40$Mk.105952@news3.mia> <36b09551.10117198@news> <Gb4s2.56$OS5.138618@news3.mia>`

```
On Thu, 28 Jan 1999 20:58:14 GMT ""Judson McClendon" <judmc123@bellsouth.net>" posted
to "comp.lang.cobol" about: "Re: Student Question" :

-->Thank you.  I don't have any plans to write anything else right now.
-->I usually write such posts when prompted by a particular request which
-->strikes me while in a writing mood. :-)
-->--
-->Judson McClendon      judmc123@bellsouth.net  (remove numbers)
-->Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
-->"For God so loved the world that He gave His only begotten Son, that
-->whoever believes in Him should not perish but have everlasting life."


Hey, I know what you mean.  I try to write on hardware topics, an area where I can,
occasionally, integrate some useful but moderately esoteric knowledge--usually in the
PC arena.  It just often strikes me!  TS


"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
*********No generalization is wholly true, not even this one**********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
