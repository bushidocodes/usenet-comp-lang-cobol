[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# multiple occurs depending on clauses in a single working storage variable

_3 messages · 3 participants · 2001-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### multiple occurs depending on clauses in a single working storage variable

- **From:** vijay_kg007@yahoo.com (vijay)
- **Date:** 2001-08-14T11:24:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a340067e.0108141024.4aa39719@posting.google.com>`

```
i have defined a working storage variable of the type

01 ws-var.
   05 ws-header.
   05 ws-array1 occurs 1 to n times
      depending on sub1.
      10  ws-var2   pic X(10).
      10  ws-array2 occurs 1 to m times
          depending upon sub2.
          15 
 
      10  ws-var3   pic X(2).
    note*** ws-var3 is actually a sort of delimiter*****
now my programs writes this ws-var in a flat file
the program manipulates sub1 and sub2 in such a way that
the max length of rec ws-var does not exceed a fixed limit
say 2000 bytes .
when the record is written a peculiar thing happens
first instance of array is written the ws-var3 occupies the place next
to
ws-var2 thereby overwritting some part of the ws-array2's first
instance
then the second instance of array1 is written ws-var2(next instance)
occupies the place next to ws-var3 therby overwritting the rec
and this goes on and on....

output looks somewhat like this
ws-var2ws-var3ws-var2ws-var3......   and so on(instances of array2
being overwritten each time) 
where it should be something of this type
ws-var2array2ws-var3ws-var2array2ws-var3......

can anyone tell why does the array1 instances get written from
the above positions.....
has this something to do with with depending upon clause
```

#### ↳ Re: multiple occurs depending on clauses in a single working storage variable

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-08-14T13:52:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lbs36$97s$1@slb6.atl.mindspring.net>`
- **References:** `<a340067e.0108141024.4aa39719@posting.google.com>`

```
Having *any* fields following an Occurs Depending On data item - within the
same 01-level - regardless of what SECTION (linkage, Working-Storage, etc)
it is in - is an extension to the ANSI and ISO Standard.  Furthermore, it is
one "extension" that is syntactically allowed in a variety of
implementations but has SIGNIFICANTLY different semantics.
\
Even within the same compiler, it often has different semantics (for example
with Micro
Focus, the ODOSLIDE directive determines how it works).

When you actually have the "object" of the ODO (occurs depending on OBJECT)
in the same 01-level - but after the ODO, then behavior becomes even more
unpredictable (or at least un-portable).

Can you tell comp.lang.cobol which compiler (and operating system) you are
using?  Also check your documentation to see if any compiler
options/directives are described as impacting this behavior.
```

#### ↳ Re: multiple occurs depending on clauses in a single working storage variable

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-08-14T19:54:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B79827F.848928C1@home.com>`
- **References:** `<a340067e.0108141024.4aa39719@posting.google.com>`

```


vijay wrote:

> i have defined a working storage variable of the type
>
…[32 more quoted lines elided]…
> has this something to do with with depending upon clause

First things first - (a) your 05 ws-header appears to serve no purpose.
(b) your Level 15 doesn't seem to be doing anything either, (c) if your
ws-var3 is and end of record delimiter, shouldn't it be a Level 05 along
with ws-var1.

I make modest use of n-dimensional tables, so I gave it a crack :-

       01 ws-var.
          05 ws-array1 occurs 1 to 50 times
             depending on sub1.
             10  ws-array2 occurs 1 to 100 times
                 depending on sub2.
                 15 ws-var2    pic x(10).

          05 ws-var3   pic X(2).

The compiler NO LIKEE (Net Express) and gave error "OCCURS DEPENDING
subsidiary to OCCURS only allowed with ODOSLIDE". Now if you haven't got
ODOSLIDE, I would suggest you are in trouble ! I'm not clear if this is
what you are trying to achieve, but the following works :-

*>--------------------------------------------------------------------------

$set ODOSLIDE

 Program-id. arraytest.

 Working-storage section.
 01 sub1                     pic 9(03).
 01 sub2                     pic 9(03).
 01 ws-var.
    05 ws-array1 occurs 1 to 50 times
       depending on sub1.
       10  ws-array2 occurs 1 to 100 times
           depending on sub2.
           15 ws-var2    pic x(10).

    05 ws-var3   pic X(2).

 Procedure Division.

  move 10 to sub1
  move 20 to sub2
  initialize ws-var
  move "Apples"        to ws-var2(1,    6)
  move "Bananas"     to ws-var2(2,   17)
  move "Mangoes"    to ws-var2(10, 20)
  move "Pears"         to ws-var2(1,     7)
  move "Grapefruit"  to ws-var2(4,   18)

  display ws-var2(1,    6)
  display ws-var2(1,    7)
  display ws-var2(2,  17)
  display ws-var2(4,  18)
  display ws-var2(10, 20)

  STOP RUN.
*>------------------------------------------------------------------------------

What you have indicated that you are trying to do is 'expand' and
'contract' the table to suit current circumstances. I believe I'm correct
in saying that regardless of your 'elasticity,' memory will be allocated,
(using my example above) for the possibility of a table with 50 x 100
elements. If you haven't got ODOSLIDE - can you arrive at an 'optimum'
number for either ws-array1 or ws-array2 that is 'fixed' instead of
'occurs' - then it should work for you.

Bill - care to comment. Does the new standard introduce any new relevant
rules for OCCURS DEPENDING ?

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
