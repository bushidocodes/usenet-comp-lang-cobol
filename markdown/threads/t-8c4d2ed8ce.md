[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read flat file field +123.45 in Cobol2 - How please ?

_8 messages · 5 participants · 2004-11_

---

### Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-11-12T05:38:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10p94r9422h7q20@corp.supernews.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0411112218.19c4598f@posting.google.com...
> "Rick Smith" <ricksmith@mfi.net> wrote
>
…[13 more quoted lines elided]…
> An 'SC07' does not seem to be called for at all.

Nor did I say that it was. I mentioned "SC07 [sic]" in the
context of implying "IBM VS COBOL II."  Mr Plinston,
my criticism of what you actually said was in your referring
to Micro Focus and to intrinsic functions, both of which
seemed unlikely in the context implied.

You may be interested in the new rules for incompatible
data for a de-editing MOVE statement. It would seem
that, given the value "-012.00," the picture +999.99 is
compatible, while the picture ++++.99 is not. If Nice4
(who admitted, "Working with Cobol for about 2 years")
used the latter (or a similar) picture, as suggested by
Mr Wagner, it is possible that the program will fail when
the compiler is updated, since "the content of that data
item is not a possible result" when -12.00 is moved to
that data item.

----- quotes from the FDIS
FDIS, page 398, 14.5.12.2 Incompatible data
Incompatible data exists when the content of a sending
operand is not valid only in the following cases:
...
2) When a numeric-edited data item is the sending
operand of a de-editing MOVE statement and the content
of that data item is not a possible result for any editing
operation in that data item, the result of the MOVE
operation is undefined and an
EC-DATA-INCOMPATIBLE exception condition is set
to exist.

FDIS, page 817ff, Annex F.1 Substantive changes
potentially affecting existing programs.

24) Incompatible data. The conditions that cause the
incompatible data condition are specified explicitly. They
are limited to boolean, numeric, and numeric-edited
sending operands.

Justification:
In the previous COBOL standard, the rules for incompatible
data stated that when the content of a data item was
referenced and the content of that data item was not
compatible with the class specified by its PICTURE clause,
then the result of that reference was undefined. There were
no rules specifying when the content of a data item was
referenced or when this caused the incompatible data
condition. This determination was left to each implementor
and the incompatible data condition may have been given
in circumstances different from those now specified..

This International Standard defines when incompatible data
is detected, thereby increasing the degree of program
portability. The EC-DATA-INCOMPATIBLE exception
condition, which is part of the new common exception
processing, gives programmers control over the handling of
the exception.

This change was made as a result of a request for an
interpretation of the previous COBOL standard. It is believed
that few, if any, programs will be affected by this change.
----- end of quotes from the FDIS
```

#### ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-12T13:09:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411121309.63856263@posting.google.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote 

> Mr Plinston,
> my criticism of what you actually said was in your referring
> to Micro Focus and to intrinsic functions, both of which
> seemed unlikely in the context implied.

Your criticism appears to be that my experience in MVS matters is
lacking. Certainly I neither know nor care what MVS something or other
is or does, Bill does that bit, but I will note for future reference
that it may be retarded in not offering intrinsic functions.

The actual point of my message (not that you seem to care about that)
was that the de-editing is required to be aligned by Cobol '85. The
reference to MF was that this has an exception, which may be of
interest to the wider audience.

> You may be interested in the new rules for incompatible
> data for a de-editing MOVE statement. 

Perhaps, at the point that the 'new rules' apply, intrinsic functions
may also be available, making the issue moot.

> It would seem
> that, given the value "-012.00," the picture +999.99 is
> compatible, while the picture ++++.99 is not. 

The only point that I was making is that the data be aligned, which is
the requirement of the current rule.

> If Nice4
> (who admitted, "Working with Cobol for about 2 years")
> used the latter (or a similar) picture, as suggested by
> Mr Wagner,

Then I suggest that you take this up with Robert, who, in fact, was
quite specific that it should be done with "the edit picture that was
was used to create the printable file", and that his was only an
example of how he might do that.

> it is possible that the program will fail when the compiler is updated,

It seems to me that Robert's 'use original picture' and my 'data be
correctly aligned in the field' should have been sufficient to avoid
any problems, now or in the future.

Perhaps you should lecture Robert on 'How to re-create PICTUREs from
sample data correctly'.
```

#### ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-13T03:24:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com>`

```
On Fri, 12 Nov 2004 05:38:55 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:
>You may be interested in the new rules for incompatible
>data for a de-editing MOVE statement. It would seem
…[7 more quoted lines elided]…
>that data item.

My freshly minted Standard says on page 322:

6) Floating insertion editing
The currency symbol and the editing sign control symbols '+' and '-'
are used as the floating insertion symbols.
Floating insertion editing is indicated by specifying a string of at
least two identical floating insertion editing
symbols. 

Where am I wrong?
```

##### ↳ ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-13T05:25:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sVgld.4957910$6p.805772@news.easynews.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com> <q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com>`

```
Given the picture
   ++++.99

and a "value" of
   "-012.00

the "output" (to be compatible data) - or the input for DEFINED '85 Standard 
de-editing would have to be
   " -12.00"   *> leading space
and not
   "-012.00"

Does that answer your question
  "Where am I wrong?"
```

###### ↳ ↳ ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-13T20:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r1ocp05aif66lo8b8c9m7716h7v3tun0ff@4ax.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com> <q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com> <sVgld.4957910$6p.805772@news.easynews.com>`

```
On Sat, 13 Nov 2004 05:25:44 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Given the picture
>   ++++.99
…[11 more quoted lines elided]…
>  "Where am I wrong?"

Yes. Sorry about the error.
```

##### ↳ ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-11-13T00:29:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10pb711i89thic8@corp.supernews.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com> <q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com>`

```

"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
news:q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com...
> On Fri, 12 Nov 2004 05:38:55 -0500, "Rick Smith" <ricksmith@mfi.net>
> wrote:
…[20 more quoted lines elided]…
> Where am I wrong?

-----
FDIS, page 322, 13.16.38.4 (PICTURE clause) Editing rules,
6) Floating insertion editing,
...
There are two ways of representing floating insertion editing:

a) one way is to represent any or all of the leading numeric
    character positions to the left of the decimal point position
    by the same insertion symbol. The result is that a single
    occurrence of the replacement character(s) is (are) placed
    into the character position(s) immediately preceding
    whichever of the following is encountered first:

    - the first non-zero numeric character in the item
    - the first character position for which no floating insertion
         editing is specified
    - the decimal point position.

    Any character positions preceding this (these) insertion
    character(s) will contain the space character.
-----

Given the picture clauses +999.99 and ++++.99, the result of
moving -12.00 to each is -012.00 and b-12.00, respectively,
where "b" is a space character. With floating insertion editing,
it is not possible for the zero character to appear after the sign.

-----
FDIS, page 398, 14.5.12.2 Incompatible data
2) When a numeric-edited data item is the sending operand of
    a de-editing MOVE statement and the content of that data
    item is not a possible result for any editing operation in that
    data item, the result of the MOVE operation is undefined
    and an EC-DATA-INCOMPATIBLE exception condition
    is set to exist.
-----

With the picture clauses given above, I take "incompatible data"
to mean that the content of x, where -099.99 <= x <= +099.99,
is compatible for the picture +999.99; but incompatible for the
picture ++++.99; due to the missing leading zero characters
required by floating insertion editing.. While the content of x,
where x <= -100.00 or x >= +100.00, is compatible for both;
since no leading zero characters are involved.
```

###### ↳ ↳ ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-11-13T06:11:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10pbr3dlmm1hh83@corp.supernews.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <10p7m2af2a8c063@corp.supernews.com> <217e491a.0411112218.19c4598f@posting.google.com> <10p94r9422h7q20@corp.supernews.com> <q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com> <10pb711i89thic8@corp.supernews.com>`

```
[Correction]
"Rick Smith" <ricksmith@mfi.net> wrote in message
news:10pb711i89thic8@corp.supernews.com...
[snip]
> ...  due to the missing leading zero characters
> required by floating insertion editing. ...

Should be: "...  due to the missing leading zero characters
removed by floating insertion editing. ..."
```

##### ↳ ↳ Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-13T07:48:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Kl0o2ReflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <10p94r9422h7q20@corp.supernews.com> <q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com>`

```
.    On  13.11.04
  wrote  spamblocker-robert@wagner.net (Robert Wagner)
     on  /COMP/LANG/COBOL
     in  q9tap0dbd88dlok8p1rqu9k82q7b8kru3l@4ax.com
  about  Re: Read flat file field  +123.45 in Cobol2 - How please ?


>> data for a de-editing MOVE statement. It would seem
>> that, given the value "-012.00," the picture +999.99 is
…[6 more quoted lines elided]…
>> that data item.

RW> My freshly minted Standard says on page 322:
RW>
RW> 6) Floating insertion editing
RW> The currency symbol and the editing sign control symbols '+' and '-'
RW> are used as the floating insertion symbols.
RW> Floating insertion editing is indicated by specifying a string of at
RW> least two identical floating insertion editing
RW> symbols.
RW>
RW> Where am I wrong?


    OK, by example:

    01 WithPicFixed       PIC +999.99 .
    01 WithPicFloat       PIC ++++.99 .


    MOVE 12.00 TO WithPicFixed
    MOVE 12.00 TO WithPicFloat

    DISPLAY WithPicFixed
      *> should result in (quotes added): "+012.00"
    DISPLAY WithPicFload
      *> should result in (quotes added): " +12.00"


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Belehrung findet man ï¿½fter in der Welt als Trost.  -G.C.Lichtenberg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
