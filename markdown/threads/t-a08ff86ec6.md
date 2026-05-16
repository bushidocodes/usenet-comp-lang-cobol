[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# My Homework

_8 messages · 6 participants · 1998-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### My Homework

- **From:** The Chameleon <sarvec@letterbox.com>
- **Date:** 1998-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36464FBF.70A0@letterbox.com>`

```
I know a lot of you guys don't want to help a poor college student do
his homework but I need help in understanding tables.
I reason a table to be like a street with boxes. One name, differnet
numbers.
If anyone has a better way of explaining loading tables etc I'd be glad
to hear from you.
I want to wow the instructor by writing simple, compact code.
Thanks.
Casey.
```

#### ↳ Re: My Homework

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10b0233b307a2d0098968a@news.earthlink.net>`
- **References:** `<36464FBF.70A0@letterbox.com>`

```
In article <36464FBF.70A0@letterbox.com>, sarvec@letterbox.com says...
> I know a lot of you guys don't want to help a poor college student do
> his homework but I need help in understanding tables.
…[7 more quoted lines elided]…
> 

Casey,

   The best way to "wow" your instructor is by developing 
your own simple, compact code to load tables. That way when
you get asked to explain it your instructor might actually 
belive that you did the work your self. <g>
```

##### ↳ ↳ Re: My Homework

- **From:** The Chameleon <sarvec@letterbox.com>
- **Date:** 1998-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36466EB0.1166@letterbox.com>`
- **References:** `<36464FBF.70A0@letterbox.com> <MPG.10b0233b307a2d0098968a@news.earthlink.net>`

```
Jeff Farkas wrote:
> 
> In article <36464FBF.70A0@letterbox.com>, sarvec@letterbox.com says...
…[30 more quoted lines elided]…
> {Crow from MST3K}


Sure but that doesn't help me understand tables  <g>
```

###### ↳ ↳ ↳ Re: My Homework

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3646ffec.0@news1.ibm.net>`
- **References:** `<36464FBF.70A0@letterbox.com> <MPG.10b0233b307a2d0098968a@news.earthlink.net> <36466EB0.1166@letterbox.com>`

```

The Chameleon wrote in message <36466EB0.1166@letterbox.com>...
>Jeff Farkas wrote:
>>
…[6 more quoted lines elided]…
>> belive that you did the work your self. <g>

>Sure but that doesn't help me understand tables  <g>

Ok, by separate e-mail I'm sending your a chapter (80 pages)
on tables from the ETK Programmer's Reference manual.
```

###### ↳ ↳ ↳ Re: My Homework

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10b04767d350cdf498968c@news.earthlink.net>`
- **References:** `<36464FBF.70A0@letterbox.com> <MPG.10b0233b307a2d0098968a@news.earthlink.net> <36466EB0.1166@letterbox.com>`

```
[This followup was posted to comp.lang.cobol and a copy was sent to the 
cited author.]

In article <36466EB0.1166@letterbox.com>, sarvec@letterbox.com says...
> Jeff Farkas wrote:
> > 
…[35 more quoted lines elided]…
> 

If you can either send me a couple of questions or some code
then I will be glad to help you out.
```

#### ↳ Re: My Homework

- **From:** "Thane Hubbell" <redsky@ibm.net>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be0ba0$ca877360$86bc48a6@default>`
- **References:** `<36464FBF.70A0@letterbox.com>`

```
That tears it.  I'm going to tell Sams to put up the Table chapter of my
book for the preview.  I found (What I consider) a really ingeneous and
simple way to explain tables.

I guess we'll find out if it's any good!

The Chameleon <sarvec@letterbox.com> wrote in article
<36464FBF.70A0@letterbox.com>...
> I know a lot of you guys don't want to help a poor college student do
> his homework but I need help in understanding tables.
…[7 more quoted lines elided]…
>
```

#### ↳ Re: My Homework

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981109005317.14590.00000519@ngol07.aol.com>`
- **References:** `<36464FBF.70A0@letterbox.com>`

```

In article <36464FBF.70A0@letterbox.com>, The Chameleon <sarvec@letterbox.com>
writes:

>I reason a table to be like a street with boxes. One name, differnet
>numbers.

The way I draw diagrams to show tables, it usually more look like floors of a
building, ground floor being floor 1, and increasing floor numbers or
increasing subscript/index as one works towards the top of the page.

Mark A. Young
```

#### ↳ Re: Unbderstanding tables in COBOL

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KSC12.39$RM6.52559@news2.mia.bellsouth.net>`
- **References:** `<36464FBF.70A0@letterbox.com>`

```
The Chameleon wrote:
>I know a lot of you guys don't want to help a poor college student do
>his homework but I need help in understanding tables.

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
more than three dimensions. ;-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
