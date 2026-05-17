[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Static storage? String statment ?

_4 messages · 4 participants · 1995-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Static storage? String statment ?

- **From:** "gt..." <ua-author-2476667@usenetarchives.gap>
- **Date:** 1995-02-07T18:31:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3h8vsq$699@newsbf02.news.aol.com>`

```
Does Cobol or some dialect of it have Static Storage, like PL/I?

Can you use a structure 01 Level in the String Statement?
String A into .......

if you can would this structure:

01 A.
05 B pic x
05 C pic x
07 D pic x
07 E pic x
05 F pic x
look like ABCDEF in the recieving field?
```

#### ↳ Re: Static storage? String statment ?

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-02-08T05:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cd5c68d3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3h8vsq$699@newsbf02.news.aol.com>`
- **References:** `<3h8vsq$699@newsbf02.news.aol.com>`

```

In article <3h8vsq$6.··.@new··l.com>, gt··.@a··.com (GTT1) writes:
› Does Cobol or some dialect of it have Static Storage, like PL/I?
› 
…[11 more quoted lines elided]…
› look like          ABCDEF     in the recieving field?

Hi. Your question is a little confusing, however I *think* I know what you're
getting at.
Consider the following structure, based upon yours above.

01 A.
05 B PIC X VALUE "B".
05 C.
07 D PIC X VALUE "D".
07 E PIC X VALUE "E".
05 F PIC X VALUE "F".

All group items (A and C in this case) are of type ALPHANUMERIC, and their size
is the sum of the sizes of their subordinate fields, including any padding
characters that might be included by the compiler (none in most cases including
this one, but if you see definitions with "SYNC" or "SYNCHRONIZED" clauses,
then there may be some). You can see therefore that your definition of C (as
pic X) is illegal - being a group field, the type is predetermined and the size
is calculated by the compiler based on subordinate fields.

Therefore, we end up with :
A - Alphanumric, size 4, value "BDEF".
B - Alphanumric, size 1, value "B".
C - Alphanumric, size 2, value "DE".
D - Alphanumric, size 1, value "D".
E - Alphanumric, size 1, value "E".
F - Alphanumric, size 1, value "F".

Does this help ?? If not please ask again and give a fuller example of what
you are trying to achieve.

Cheers,
Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

#### ↳ Re: Static storage? String statment ?

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-02-08T19:27:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cd5c68d3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3h8vsq$699@newsbf02.news.aol.com>`
- **References:** `<3h8vsq$699@newsbf02.news.aol.com>`

```
In article <3h8vsq$6.··.@new··l.com>
gt··.@a··.com (GTT1) writes:

›
› Does Cobol or some dialect of it have Static Storage, like PL/I?
›
Well, if you mean storage that retains value between calls, within
a subroutine, the answer is yes.

I've been burned on this before. For example, the main calling program
ABC11 calls subprogram DEF12. The working storage variables modified
during the first call will remain with those values unless you do
a "cancel" call command. The value clause of your fields is only true
after a cancel or an initial call.

› Can you use a structure 01 Level in the String Statement?
› String A into .......
…[5 more quoted lines elided]…
›     05   C                 pic x
This record layout won't compile.
05 C can't have a pic clause if the sub field has a pic clause.
›            07  D           pic x
›            07  E           pic x
›     05   F                  pic x
› look like          ABCDEF     in the recieving field?
If we write the above like this:
01 A.
05 B PIC X(1) value 'B'.
05 C.
07 D pic x(1) value 'D'.
07 E pic x(1) value 'E'.
05 F pic x(1) value 'F'.

The above seems to indicate some confusion between variable names
and the actual contents of the fields.
Some string statements using above would include
string A delimited by size
B delimited by size
C ..
etc.
into WS-silly-string
where Ws-silly-string would then contain
BDEFBDEDEF

That is because COBOL defines the memory layout as follows:
Storage location named 'A' contains four characters
values BDEF.
B contains one character value of 'B'.
C contains two characters values of DE.
D contains one character value of D.
E contains one character value of E.
And of course F contains F.

Pretty confusing huh?
The larger numbers of the subfields indicate they are subsets of
the smaller level numbers.
For example, the 01 level field named A is divided into
the subfields B,C and F. C is in turn divided into D and E.


Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

#### ↳ Re: Static storage? String statment ?

- **From:** "rdn..." <ua-author-17073928@usenetarchives.gap>
- **Date:** 1995-02-09T20:39:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cd5c68d3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3h8vsq$699@newsbf02.news.aol.com>`
- **References:** `<3h8vsq$699@newsbf02.news.aol.com>`

```

› 01  A.
›     05   B                 pic x
…[5 more quoted lines elided]…
› 


If you value B as "B", C as "C", and so on, it would display as "BCDEF".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
