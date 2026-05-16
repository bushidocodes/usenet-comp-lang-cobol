[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tables

_7 messages · 5 participants · 1999-05_

---

### Tables

- **From:** "Rana S Alexander" <JOSHNYA@prodigy.net>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com>`

```
Can someone give me an explanation how to set up a 3 x 2 table without hard
coding it?????  Then how do I reference it for computation.

   Example:
                 High          Low
           20
           30
           40
```

#### ↳ Re: Tables

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gn01e$blb@dfw-ixnews11.ix.netcom.com>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com>`

```
I am not positive what you mean by "not hard coding it".  My guess is that
you are in an introductory COBOL course and need to look at (learn) the
topics related to
   - The OCCURS clause
   - Subscripting and indexing

If these are terms that you really do know already - but that you want to
"avoid" for some reason, then the same functionality (with a lot less
clarity IMHO) can be achieved by "reference modification".  The start
position of reference modification can be an arithmetic expression (as can
the length) - so you could "compute" your way thru the table.  Again, as
anything other than a fairly obscure academic exercise, I wouldn't recommend
this approach - but it CAN be done.
```

#### ↳ Re: Tables

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fXDX2.4038$Nn6.821242@news3.mia>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com>`

```
Rana S Alexander wrote:
>Can someone give me an explanation how to set up a 3 x 2 table without hard
>coding it?????  Then how do I reference it for computation.

Rana, below is a post I recently made on the subject.  Perhaps you will find
it helpful.

Think of a table (any item which contains an OCCURS clause) to be several
copies of that item, all with the same name.  Because they all have the
same name, you must have another way to differentiate between them.  This
is done by appending a 'subscript' (or 'index', see below) to references
to the item.  The term 'subscript' is taken from math, where variables of
the same name but different incarnations are indicated by subscripts.

   a    = (a  + (n / a )) / 2
    i+1     i         i

A subscript is always an integer that indicates which one of the items
of the same name are being referenced.  Since computer languages (with
the notable exception of APL) are usually written using plain text,
true subscript fonts are not available, so COBOL uses parenthesis (C
and Pascal use square brackets) to designate the subscript.  You can
think of the table as a row of boxes, each with the same name, and the
subscript designates which of the boxes is being referenced.  In this
example:

   03  MY-ITEM   OCCURS 20 TIMES ...

   MOVE MY-ITEM(subscript) TO ...

The value of (subscript) determines which of the 20 MY-ITEM elements is
being referenced.  'subscript' can be a numeric literal, a numeric data
item, a numeric data item +/- a numeric literal, or an index, or an
index +/- a numeric literal.  It must always evaluate to an integer
between 1 and the limit in the OCCURS clause (20 in this example).
Indexes are a special type of subscript.  Indexes are associated with,
and must be used only with, a particular table, and are defined by the
INDEXED BY clause on that table:

   03  MY-ITEM   OCCURS 20 TIMES INDEXED BY MY-INDEX ...

This creates an index named MY-INDEX associated with the table MY-ITEM.
The specific internal format of indexes is left to the implementor, but
the general idea is that an index can be in a form other than an integer
representing the 'occurrence number' of the entry in the table.  It is
essentially a construct for permitting a form which can be manipulated
more efficiently by the CPU.  The details vary by implementation, and
are not important here.  There are a few differences in the way indexes
are used, as opposed to subscripts.  One is that you must use the SET
verb to change the contents of an index.  Instead of

   MOVE 1 TO MY-INDEX
   ADD 1 TO MY-INDEX
   SUBTRACT 2 FROM MY-INDEX

you would use, respectively

   SET MY-INDEX TO 1
   SET MY-INDEX UP BY 1
   SET MY-INDEX DOWN BY 2

You can also set and change the value of an index by using the VARYING
clause of the PERFORM or SEARCH statements.

   PERFORM ... VARYING MY-INDEX FROM 1 BY 1 UNTIL MY-INDEX > 20

If you declare a table with an index you can also use the SEARCH verb
to search the table.

   SET MY-INDEX TO 1.
   SEARCH MY-ITEM
      AT END ...
      WHEN MY-ITEM(MY-INDEX) = ...

If your table is completely populated and the values are in ascending or
descending order, you can use the SEARCH ALL syntax (see ASCENDING and
DESCENDING clauses of OCCURS), which may do a non-linear search (such as
binary search) of the table, resulting in much faster execution.  You
also do not have to set the initial value for the index before executing
SEARCH ALL.

Note that when you reference an individual table element, you must use
a subscript or index to indicate which element you refer to.  But when
you reference the table as a whole, such as in the SEARCH statement,
you do not use a subscript or index.

The power and usefulness of tables and subscripting is best understood
in the context of loops.  It is the use of these two concepts together
which permits writing one set of code which can operate on a number of
different elements.  Consider a program that tested some sort of code
to be valid, and there were 500 different codes.  Without the use of
subscripts, you would probably need to individually code 500 IF tests,
or 500 EVALUATE ... WHEN clauses.  What if there were 5000 different
codes?  What about 50,000?  With a table, you can load all the values
into the table, either through VALUE clauses in Working Storage if the
table is static, or from a data file.  Then just use a short SEARCH
statement or loop to test the codes against the values in the table.

If your table has subordinate entries like this

   03  MY-ITEM   OCCURS 20 TIMES INDEXED BY MY-INDEX ...
       05  MY-SUB-ITEM-1 ...
       05  MY-SUB-ITEM-2 ...

Then each of the subordinate items MY-SUB-ITEM-1 and MY-SUB-ITEM-2 are
referenced using subscripts or indexes in exactly the same way as the
item MY-ITEM.  The difference is that you may not reference any of the
subordinate items as the object of the SEARCH verb.  You can reference
subordinate items in the WHEN clauses of a SEARCH.

Two dimensional tables merely carry subscripting one step farther.

   03  MY-ITEM   OCCURS 20 TIMES ...
       05  MY-ITEM-A
       05  MY-ITEM-B  OCCURS 10 TIMES ...

Each of the 20 copies of MY-ITEM contains one MY-ITEM-A and 10 copies
of MY-ITEM-B.  There are 200 total copies of MY-ITEM-B in the entire
structure.  A reference to MY-ITEM or MY-ITEM-A is resolved by the use
of one subscript.  But if you reference MY-ITEM-B, you must use two
subscripts, the first to designate which of the 20 MY-ITEMS, and a
second to designate which of the MY-ITEM-B entries is intended within
that MY-ITEM.  Both subscripts are enclosed in the same parenthesis,
optionally separated by a comma.

   MY-ITEM-B(14, 6)
or
   MY-ITEM-B(14 6)

This references the 6th MY-ITEM-B, inside the 14th MY-ITEM.  You can
think of this as a grid of boxes, with the first subscript indicating
the row and the second subscript indicating the column.

Additional levels of subscripting merely carry this concept farther.

   03  MY-ITEM   OCCURS 20 TIMES ...
       05  MY-ITEM-A ...
       05  MY-ITEM-B  OCCURS 10 TIMES ...
           05  MY-ITEM-B1  OCCURS 5 TIMES ...
           05  MY-ITEM-B2 ...

   MY-ITEM-B1(14, 6, 3)

References 3rd MY-ITEM-B1, in 6th MY-ITEM-B, in 14th MY-ITEM.  You can
think of this as a 3D rectangle of boxes, with the first subscript
indicating the row, the second subscript indicating the column, and the
third subscript representing the level.  There are 20 * 10 * 5 = 1000
total copies of MY-ITEM-B1 in the structure, and 20 * 10 = 200 copies
of MY-ITEM-B2.

Two dimensional tables are used occasionally, three dimensional tables
are pretty rare, and you almost never see four or more dimensions.  I
won't even attempt to describe a method for visualizing a table with
more than three dimensions. ;-)  Thane Hubbell describes an interesting
way in chapter 12 of his book "Teach Yourself COBOL in 24 Hours", from
Sams.
```

##### ↳ ↳ Re: Tables

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gntrp$25g$1@news.ses.cio.eds.com>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com> <fXDX2.4038$Nn6.821242@news3.mia>`

```

> Two dimensional tables are used occasionally, three dimensional
tables
> are pretty rare, and you almost never see four or more dimensions.
I
> won't even attempt to describe a method for visualizing a table with
> more than three dimensions. ;-)  Thane Hubbell describes an
interesting
> way in chapter 12 of his book "Teach Yourself COBOL in 24 Hours",
from
> Sams.

I don't know how Thane did it, but I describe multi-dimensional tables
like this.

Imagine a cube or a dice, a small one.  Line up a row of 10 of them,
and you have a 10 element 1 dimension table (in COBOL, each cube can
hold an entire record layout, limited only by memory).  Line up nine
more rows of 10 cubes, and you have a 10,10 two dimensional table.
Stack nine more sets of 10,10 cube sets on top of the first, and you
have a 10,10,10 three dimensional table.  Set nine more such
super-cubes up in a row, and you have a 10,10,10,10 four dimensional
table with 10,000 entries.  This scales up conceptually as far as you
want.  The next step goes to 100,000 entries, then 1,000,000 for the
six dimensional table.  If each cube held just a 100 byte record
layout, that would require 100 megs of RAM, at least.

Why would you want to?  That's a different story . . .
```

##### ↳ ↳ Re: Tables

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7go9do$ks2$1@news.igs.net>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com> <fXDX2.4038$Nn6.821242@news3.mia>`

```
Judson McClendon wrote in message ...

>Two dimensional tables are used occasionally, three dimensional tables
>are pretty rare, and you almost never see four or more dimensions.  I
>won't even attempt to describe a method for visualizing a table with
>more than three dimensions. ;-)  Thane Hubbell describes an interesting
>way in chapter 12 of his book "Teach Yourself COBOL in 24 Hours", from


A multi-node tree is really a infinitely dimensioned array.
```

###### ↳ ↳ ↳ Re: Tables

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZiXX2.1744$3f2.544463@news2.mia>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com> <fXDX2.4038$Nn6.821242@news3.mia> <7go9do$ks2$1@news.igs.net>`

```
Donald Tees wrote:
>
>A multi-node tree is really a infinitely dimensioned array.

                                                     ^
                                                   sparse  :-)
```

#### ↳ Re: Tables

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gn3j3$f6o$1@news.ses.cio.eds.com>`
- **References:** `<7gms7d$50j6$1@newssvr04-int.news.prodigy.com>`

```
Rana S Alexander <JOSHNYA@prodigy.net> wrote in message
news:7gms7d$50j6$1@newssvr04-int.news.prodigy.com...
> Can someone give me an explanation how to set up a 3 x 2 table
without hard
> coding it?????  Then how do I reference it for computation.
>
…[5 more quoted lines elided]…
>

Rana S Alexander <JOSHNYA@prodigy.net> wrote in message
news:7gms7d$50j6$1@newssvr04-int.news.prodigy.com...
> Can someone give me an explanation how to set up a 3 x 2 table
without hard
> coding it?????  Then how do I reference it for computation.
>
…[5 more quoted lines elided]…
>

Ditto what William Klein said: What do you mean by "without hard
coding it?????"

Setting up a table involves writing out its definition in working
storage, that could be viewed as a form of hardcoding.

As to how you reference a table, you use either subscripts or indexes,
and there must certainly be code to do that.

Do you mean: Without using literal values for the subscripts?
"Some-Table-Name (1)" versus "Some-Table-Name (Some-Table-Index)"
where Some-Table-Index is a value you control in your program so you
can refer to the portion of the table you need to as the program
progresses through its logic?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
