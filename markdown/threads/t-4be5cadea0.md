[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How would you do this?

_26 messages · 10 participants · 2007-03_

---

### How would you do this?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-10T19:13:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```
to: comp.lang.cobol *and*  IBM-MAIN

IBM has (relatively) recently created an LE callable service, CEE3INF, that 
returns a "32-bit map" with information about what environment a program is 
running in.  See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.9

Now, my question is how various "experienced" COBOL programmers would handle 
such information (either in an IBM mainframe environment OR in other COBOL 
environments for those who see this note and don't work in IBM mainframe 
environments - but do get "bit maps")

1) Call a non-COBOL program to decode this map (e.g.. Assembler, C, PL/I or any 
other language that can easily handle "bits")

2)  Do a "division" loop to figure out which bits are turned on?

3) Use 88-levels with hex literals to check for which bits were turned on?

4) Use the LE (or comparable) "bit manipulation" routines?

5) Not use CEE3INF from COBOL?

6) Other?

  ***

Although I wouldn't LIKE it, I can imagine doing this in any of these ways. 
Obviously, when/if a COBOL compiler supports the '02 Standard Bit/Boolean 
features, this becomes "trivial".  However, as few (if any) compilers do this 
yet, I was wondering how programmers would handle this requirement.
```

#### ↳ Re: How would you do this?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-10T21:12:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v6pek1atd1a64@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:rrDIh.242220$k82.140284@fe07.news.easynews.com...
> to: comp.lang.cobol *and*  IBM-MAIN
>
> IBM has (relatively) recently created an LE callable service, CEE3INF,
that
> returns a "32-bit map" with information about what environment a program
is
> running in.  See:
>
>
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.9
>
> Now, my question is how various "experienced" COBOL programmers would
handle
> such information (either in an IBM mainframe environment OR in other COBOL
> environments for those who see this note and don't work in IBM mainframe
> environments - but do get "bit maps")
>
> 1) Call a non-COBOL program to decode this map (e.g.. Assembler, C, PL/I
or any
> other language that can easily handle "bits")
>
…[12 more quoted lines elided]…
> Although I wouldn't LIKE it, I can imagine doing this in any of these
ways.
> Obviously, when/if a COBOL compiler supports the '02 Standard Bit/Boolean
> features, this becomes "trivial".  However, as few (if any) compilers do
this
> yet, I was wondering how programmers would handle this requirement.

There are a lot of "reserved" bits in the four full-words.
While some of these may become assigned, it seems
unlikely that any would be moved. As new bits become
assigned, a routine that processes all bits, such as a
"division loop" would, I believe, be more sensitive to
maintenance than one that extracts the bit fields directly.
Also one need not extract more than is desired.

Extracting these bit fields directly seems a rather
straight-forward process with intrinsic functions. The
exponents below are 31 minus the low-order bit number
of the field.

-----
compute c-bit = function mod
    (function integer (member-id / (2 ** 28)) 2)
compute cobol-bit = function mod
    (function integer (member-id / (2 ** 26)) 2)
compute amode = function mod
    (function integer (env-info / (2 ** 17)) 4)
compute product-number = function integer
    (gpid / (2 ** 24))
compute version = function mod
    (function integer (gpid / (2 ** 16)) 256)
compute releasse = function mod
    (function integer (gpid / (2 ** 8)) 256)
compute modification = function mod
    (gpid 256)
-----
```

##### ↳ ↳ Re: How would you do this?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-11T04:21:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MsLIh.6139$pj4.2291@fe09.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com>`

```
Richard,
   Are you assuming that "Moded fields" are USAGE BINARY-CHAR - or a "BINARY" 
(with non-ANSI "notrunc" behavior). Otherwise, I don't know how you are 
processing them.  This is part of my problem in "solving" this problem. 
Standard COBOL (pre- USAGE BINARY-CHAR) has no way to define a numeric field as 
"binary" without truncation.
```

###### ↳ ↳ ↳ Re: How would you do this?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-11T04:31:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v7j5rd1ec59cd@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <MsLIh.6139$pj4.2291@fe09.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:MsLIh.6139$pj4.2291@fe09.news.easynews.com...
> Richard,
>    Are you assuming that "Moded fields" are USAGE BINARY-CHAR - or a
"BINARY"
> (with non-ANSI "notrunc" behavior). Otherwise, I don't know how you are
> processing them.  This is part of my problem in "solving" this problem.
> Standard COBOL (pre- USAGE BINARY-CHAR) has no way to define a numeric
field as
> "binary" without truncation.

PIC 9(9) BINARY

The call to CEE3INF, as I understand it, will return the
values untruncated. Since truncation occurs when the
COBOL program stores the result of a calculation, I
don't see truncation, from the COMPUTE statements,
as a problem.

The worrisome case appears to be getting bit 0 of a field,
such as, the CICS bit from sys/subsys; since this would
involve division by +2147483648 (2 ** 31).

compute cics-bit = function mod
    (function integer (sys-subsys / (2 ** 31)) 2)

This statement correctly returns either +1 or +0 with
ANSI truncation (the default) in effect, on Micro Focus
COBOL 3.2.24.

-----
      $set ibmcomp vsc2 arithmetic"vsc2"
       identification division.
       program-id. test3inf.
       working-storage section.
       01 sys-subsys pic 9(9) binary value 0.
       01 cics-bit pic s9(4) binary value +0.
       procedure division.
       begin.
           move x"80000000" to sys-subsys (1:4)
           compute cics-bit = function mod
               (function integer (sys-subsys / (2 ** 31)) 2)
           if cics-bit = +1
               display "CICS bit is on"
           end-if
           goback.
-----

> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:12v6pek1atd1a64@corp.supernews.com...
…[7 more quoted lines elided]…
> >> returns a "32-bit map" with information about what environment a
program
> > is
> >> running in.  See:
> >>
> >>
> >
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.9
> >>
> >> Now, my question is how various "experienced" COBOL programmers would
> > handle
> >> such information (either in an IBM mainframe environment OR in other
COBOL
> >> environments for those who see this note and don't work in IBM
mainframe
> >> environments - but do get "bit maps")
> >>
> >> 1) Call a non-COBOL program to decode this map (e.g.. Assembler, C,
PL/I
> > or any
> >> other language that can easily handle "bits")
…[3 more quoted lines elided]…
> >> 3) Use 88-levels with hex literals to check for which bits were turned
on?
> >>
> >> 4) Use the LE (or comparable) "bit manipulation" routines?
…[9 more quoted lines elided]…
> >> Obviously, when/if a COBOL compiler supports the '02 Standard
Bit/Boolean
> >> features, this becomes "trivial".  However, as few (if any) compilers
do
> > this
> >> yet, I was wondering how programmers would handle this requirement.
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-11T10:53:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dRIh.197862$Wn.83634@fe06.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <MsLIh.6139$pj4.2291@fe09.news.easynews.com> <12v7j5rd1ec59cd@corp.supernews.com>`

```
You may be right (but I am still not certain) for IBM mainframes.  According to:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/2.4.54

"TRUNC(STD) applies only to USAGE BINARY receiving fields in MOVE statements and 
arithmetic expressions."

but it then goes on to say,
  "When TRUNC(STD) is in effect, the final result of an arithmetic expression, 
..., is truncated"

So I am not certain where in your compute statement the truncation would occur 
(if at all), i.e. for the "arithmetic expression" (evaluation) or in the FINAL 
move to the receiving field.  I don't (easily) have an Enterprise COBOL system 
to test with, so I can't tell for sure.  (I just "in general" HATE to rely on 
any stage of USAGE BINARY items where the data is larger than the PICTURE).

P.S.  If you haven't ever seen exactly what IBM does (and it IS different from 
Micro Focus), you might want to look at the examples at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/2.4.54.1

and

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/2.4.54.2

some of the results are truly "mind boggling"
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-12T15:38:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vbb2osu0gkmf1@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <MsLIh.6139$pj4.2291@fe09.news.easynews.com> <12v7j5rd1ec59cd@corp.supernews.com> <6dRIh.197862$Wn.83634@fe06.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:6dRIh.197862$Wn.83634@fe06.news.easynews.com...
> You may be right (but I am still not certain) for IBM mainframes.
According to:
>
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/2.4.54
[I used <
http://publib.boulder.ibm.com/infocenter/pdthelp/v1r1/index.jsp?topic=/com.i
bm.entcobol4.doc/up4060.htm >.]
>
> "TRUNC(STD) applies only to USAGE BINARY receiving fields in MOVE
statements and
> arithmetic expressions."

"receiving fields"; not "sending fields"!

> but it then goes on to say,
>   "When TRUNC(STD) is in effect, the final result of an arithmetic
expression,
> ..., is truncated"

And continues with "to the number of digits in the
PICTURE clause of the BINARY receiving field."

> So I am not certain where in your compute statement the truncation would
occur
> (if at all), i.e. for the "arithmetic expression" (evaluation) or in the
FINAL
> move to the receiving field.

Let me emphasize "receiving field".

>  I don't (easily) have an Enterprise COBOL system
> to test with, so I can't tell for sure.  (I just "in general" HATE to rely
on
> any stage of USAGE BINARY items where the data is larger than the
PICTURE).

And IBM recognizes your concern:

"Recommendations: TRUNC(BIN) is the recommended
option for programs that use binary values set by other
products. Other products, such as IMS, DB2, C/C++,
FORTRAN, and PL/I, might place values in COBOL
binary data items that do not conform to the PICTURE
clause of the data items."

[snip]
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:12v7j5rd1ec59cd@corp.supernews.com...
[snip]
> > PIC 9(9) BINARY
> >
…[33 more quoted lines elided]…
> > -----
[snip]
```

###### ↳ ↳ ↳ Re: How would you do this?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-03-11T14:12:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%6UIh.5195$FG1.4453@newssvr27.news.prodigy.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <MsLIh.6139$pj4.2291@fe09.news.easynews.com>`

```
01 SYS-SUSBSYS  PIC S9(09) USAGE BINARY

  CALL 'CEE3INF' USING BY REFERENCE SYS-SUBYS .....

  DIVIDE SYS-SUBSYS BY 2 GIVING X REMAINDER BIT-0


(You can just 'ladder' DIVIDE by 2 and keeping remainders; the remainders 
will be the bits)

MCM
```

##### ↳ ↳ Re: How would you do this?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-12T13:51:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55jmglF25132bU1@mid.individual.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12v6pek1atd1a64@corp.supernews.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
…[74 more quoted lines elided]…
>
Excellent! Great stuff, Rick.

Pete.
```

###### ↳ ↳ ↳ Re: How would you do this?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-12T02:36:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v9ta2pe1l8k54@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <55jmglF25132bU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:55jmglF25132bU1@mid.individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:12v6pek1atd1a64@corp.supernews.com...
[snip]
> > Extracting these bit fields directly seems a rather
> > straight-forward process with intrinsic functions. The
…[20 more quoted lines elided]…
> Excellent! Great stuff, Rick.

Thank you for your kind words, here and elsewhere.

This is little more than the implementation, in COBOL,
of a few assembler instructions. The use of powers of 2
translates to logical "shift" and "and". For IBM, the inline
instruction sequence, for those with both functions (and
this could be used for all), is:
    L
    SRL
    N
    STH

Any who are truly uncomfortable with using COBOL
to extract bit fields could write an equivalent assembler
routine and call it.
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-03-13T15:12:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1fdv2dj0d6pngsu05vkoj0onbmqkk8m1t@4ax.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v6pek1atd1a64@corp.supernews.com> <55jmglF25132bU1@mid.individual.net> <12v9ta2pe1l8k54@corp.supernews.com>`

```
On Mon, 12 Mar 2007 02:36:10 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[45 more quoted lines elided]…
>
When you take into account the inter module calling overhead on IBM z
series, especially with the DYNAM option the following conversion from
a bit switch to a byte-switch is probably quickest.  I am assuming
that the field descriptions in the data division are obvious from the
code.  I had a nice assembler routine that used UNPK - unpack, NC -
and character and TR to get the switch bytes but the savings in the
routine itself were eaten up by the overhead.

MOVE bit-switch TO binary-field-low-order-character.
MOVE ZERO TO switch-bytes
IF binary-field > 127
  SUBTRACT 128 FROM binary-field
  MOVE '1' TO switch-byte (1)
END-IF
IF binary-field > 63
  SUBTRACT 64 FROM binary-field
  MOVE '1' TO switch-byte (2)
END-IF
IF binary-field > 31
  SUBTRACT 32 FROM binary-field
  MOVE '1' TO switch-byte (3)
END-IF
IF binary-field > 15
  SUBTRACT 16 FROM binary-field
  MOVE '1' TO switch-byte (4)
END-IF
IF binary-field > 7
  SUBTRACT 8 FROM binary-field
  MOVE '1' TO switch-byte (5)
END-IF
IF binary-field > 3
  SUBTRACT 4 FROM binary-field
  MOVE '1' TO switch-byte (6)
END-IF
IF binary-field > 1
  SUBTRACT 2 FROM binary-field
  MOVE '1' TO switch-byte (7)
END-IF
IF binary-field = 1
  MOVE '1' TO switch-byte (8)
END-IF
```

#### ↳ Re: How would you do this?

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-03-10T21:25:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v71184hr69581@corp.supernews.com>`
- **In-Reply-To:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```
William M. Klein wrote:
> to: comp.lang.cobol *and*  IBM-MAIN
> 
…[12 more quoted lines elided]…
> other language that can easily handle "bits")

I'd consider writing a C routine that would explode the bitmaps into 
tables of 32 integers (PIC 9 COMP or PIC 9 DISPLAY or whatever works). 
You'd have to make sure you knew how the table would be laid out in 
memory, so you might consider sacrificing memory and speed for 
portability.  The 32-bit word with four 8-bit fields could be split into 
four PIC 99 fields.

The good thing is that the C code wouldn't have to know what any of the 
bits meant, and you wouldn't have to do anything fancy in COBOL to get 
the information you need.

Louis
```

##### ↳ ↳ Re: How would you do this?

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-03-10T22:37:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v759g1fol3fcf@corp.supernews.com>`
- **In-Reply-To:** `<12v71184hr69581@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12v71184hr69581@corp.supernews.com>`

```
Louis Krupp wrote:
> William M. Klein wrote:
>> to: comp.lang.cobol *and*  IBM-MAIN
…[21 more quoted lines elided]…
> four PIC 99 fields.

Oops.  Make that PIC 9(3).

Louis
```

#### ↳ Re: How would you do this?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-12T13:50:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55jmepF25hgrfU1@mid.individual.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:rrDIh.242220$k82.140284@fe07.news.easynews.com...
> to: comp.lang.cobol *and*  IBM-MAIN
>
…[4 more quoted lines elided]…
> http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.9

I had a bit of spare time after a heavy weekend so I checked your link above 
and then downloaded the z/OS COBOL manual to see what you can actually DO... 
I note with regret that PIC 1 (Binary) is missing... :-)  (Now, THAT's 
something that would be much more useful in the COBOL standard than embedded 
XML...)

Anyway, having faced this problem in the Client/Server environment some 
years back I am satisifed that the problem is NOT about what bits mean what, 
it is about being able to reference bits from COBOL at all.

You mentioned the traditional approaches and I've given my opinions below.


>
> Now, my question is how various "experienced" COBOL programmers would 
…[5 more quoted lines elided]…
> or any other language that can easily handle "bits")

No. I looked at doing it in Java and then invoking the Java class from z/OS 
but it would have taken more time than I was prepared to spend on it to 
fully investigate and code the solution.(If I was working in a mainframe 
environment, I'd simply invest the time and do it this way. Java is fully 
transportable and so should COBOL be, if that is important to you. (It is a 
consideration for me, but not a show stopper...)

This approach has the advantages that it is OO, encapsulated, and 
transportable.

>
> 2)  Do a "division" loop to figure out which bits are turned on?

Yeah, brute force. Effective but inelegant.
>
> 3) Use 88-levels with hex literals to check for which bits were turned on?

Imaginative, but a bit ugly.
>
> 4) Use the LE (or comparable) "bit manipulation" routines?

Certainly that was the approach I opted for in the MicroFocus environment 
many years ago. They provided bit conversion routines that were callable 
from COBOL, but of course, as soon as you use them, any hope of platform 
transportability is gone...

>
> 5) Not use CEE3INF from COBOL?
>

Seems a bit drastic :-)

> 6) Other?
>

Given that the real problem is converting bits to bytes so COBOL can address 
them, it seemed to me that the Java option is the one I would go for. 
However, I then read Rick's post and it is simple and elegant. I understand 
you have some reservations about it working with mainframe TRUNC options but 
I'd simply try it out as quickly as possible.

Given that it worked, I'd go with that. The intrinsic MOD function it uses 
is available on every platform I've seen that supports intrinsic 
functions...

I reckon this is imagnative simple and direct.

Definitely gets my vote.

Pete.
```

#### ↳ Re: How would you do this?

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2007-03-11T22:26:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET>`
- **In-Reply-To:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```
William M. Klein wrote:
> to: comp.lang.cobol *and*  IBM-MAIN
> 
…[30 more quoted lines elided]…
> 
Bill,
Since you are already using LE Callable Services, why not use:

> CEESITST:  Bit test
> *  CEESITST selectively tests a bit in its parm1 input to determine if
…[21 more quoted lines elided]…
>     Bits are counted from the right.
     Ref:  Language Environment Programming Reference
	  Chapter 5:  Bit manipulation routines
           SA22-7562-08  [z/OS V1.8]
Carl
```

##### ↳ ↳ Re: How would you do this?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-12T17:29:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55k39jF25hnt2U1@mid.individual.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET>`

```

"CG" <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote in message 
news:9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET...
> William M. Klein wrote:
>> to: comp.lang.cobol *and*  IBM-MAIN
…[65 more quoted lines elided]…
> Carl

That looks fine Carl and was the approach I adopted about 9 years ago when I 
first had this problem. (Use callable bit manipulation routines provided in 
the environment.)

I have a few reservations (although I agree it is a perfectly valid solution 
in the stated environment):

1. If you are looking for a general solution (for cases where you AREN'T 
calling  CEE3INF for example... you just need to "interpret" a bit 
string...) this becomes less attractive.  Calling either of these routines 
ties you to a specific environment.

2. Rick's solution will work in almost any environment and is very few lines 
of code without having to worry about CALL and parameters. It is solid COBOL 
and should work in any COBOL environment where they support intrinsic 
functions.

3. If you are going to call anything, it would be better to call a 
non-environment specific module or object. Java presents itself here as a 
prime candidate.

4. I was surprised the routine above returns a binary number that is 1 or 0; 
in the IBM environment I would have expected a byte, which is much more 
amenable to CLC and CLI, instructions without requiring any conversion. I 
suspect that collating sequences other than just plain EBCDIC are being 
considered here...

Left to my own devices, I would've opted for the Java/COBOL mix and made it 
an OO Class, invokable from COBOL. I like Rick's solution much better.

Pete.

PS I don't hink it is fair for this thread to refer to this process as "bit 
mapping". This term has a specific meaning and connotation in other 
environments. What is happening here is interpretation (deriving meaning 
from), or analysis of,  a bit string.
```

###### ↳ ↳ ↳ Re: How would you do this?

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2007-03-12T01:09:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55953$45f4e0a0$4275fbdb$18078@FUSE.NET>`
- **In-Reply-To:** `<55k39jF25hnt2U1@mid.individual.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "CG" <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote in message 
> news:9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET...
…[104 more quoted lines elided]…
> from), or analysis of,  a bit string.

First, an obvious point:  The reason this approach is applicable is 
because it means that the programmer/user does not have to do anything 
special other than use the service provided...  It's part of the system.

As you would probably expect, please consider that Bill's question was 
very specific to his objection to the implementation of CEE3INF.  This 
service is not only explicit to LE, but the '3' in the name makes it 
even more specific to the "S/390" [read mainframe, OS/390, MVS, z/OS, et 
al] environment.  Therefore, there is no situation where someone using 
CEE3INF would not also have clear access to the Bit Manipulation 
services that I suggested.  [There are, BTW, a set of four services for 
setting, clearing, shifting and testing bits.]

I don't find the binary returned value objectionable because it is 
highly unlikely that you would ever actually translate the value to 
anything, much less a character.  You test it with a relatively fast 
compare and get on with the logic.

Certainly, if you want to broaden the subject to include all situations 
of bit mangling, then native language [IMHO] is the only way to go. 
And, if you are in control of the application design and know you are 
lacking such language, change the design to match the features you do have.

Finally, your objection to 'bit mapping' is noted, but a FIND in the 
message text returned your use of the word 'mapping' as the only instance.

Carl
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-12T09:32:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<579Jh.240693$_X1.83265@fe05.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET>`

```
Of course the "odd" thing is how you need to create the parms for a call to 
CEESITST.  The simple fact is that COBOL does *NOT* have (before the '02 
Standard and IBM hasn't implemented USAGE BINARY-CHAR or any other BINARY-xxx 
usage) a way to specify a

   32-bit integer

The best (non-Standard) way to do this in Enterprise COBOL is to say
   05 32Int  Pic S9(9) Comp-5.

but even THEN it is hard to test the "high-level" bit.  In reality, you would 
PROBABLY end up passing
    Pic X(4)
fields to CEESITST (in COBOL) and use hex-literals to set bits that you want to 
test, The following is how I *guess* that CEESITST would actually be used in 
COBOL (you should note that there is NO "usage" example any where in the 
existing LE manuals).

  05 Parm1  Pic S9(9) Comp-5
 05 Parm2  Pic X(4)
 05 Reslt  Pic S9(9) Comp-5
       ....
Move to-be-tested to Parm1
Move 17 to Parm1
Call "CEESITST" Using Parm1 Parm2 FC Reslt
If Reslt = 1
    Display "bit 17 - in a way that COBOL never counts - is ON
Else
  Display "bit 17 is off"
End-If

  ****

As there is NO example of how to use this callable service, I am not POSITIVE 
this is correct, but I think it is.
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-03-12T13:40:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45F55862.6F0F.0085.0@efirstbank.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET> <579Jh.240693$_X1.83265@fe05.news.easynews.com>`

```
Here's some real life code I have that actually uses this:
01 CHR-USER-RECORD.
    10  CHR-SPCLFGS         PIC X(04).

77  REISSUE-DISALLOW-BIT    PIC S9(8) BINARY VALUE 12.
77  REISSUE-DISALLOWED      PIC S9(8) BINARY.         

CALL 'CEESITST'  USING CHR-SPCLFGS                   
                       REISSUE-DISALLOW-BIT          
                       FC                            
                       REISSUE-DISALLOWED            
IF REISSUE-DISALLOWED = 1                            
    MOVE 'N'                TO RISS-ALLOW OF CARD-DTL
ELSE                                                 
    MOVE 'Y'                TO RISS-ALLOW OF CARD-DTL
END-IF                                               

I don't see the need to worry about using PIC X(4) versus PIC S9(9) COMP
other than in the field to be tested (which shouldn't really be thought of
as a number in the first place).  The maximum value of parm2 is +31 and the
maximum value of result is +1.
Also, you can't test more than one bit per call.

I used this in this particular situation just because it's available.  But
generally we use an assembler program to 'expand' the bits to bytes.  We
then use COBOL subscripting to test the bytes for a value of '0' or '1'.

Another caveat to using the LE routine is that it counts right to left and
from 0.  In the above example I am testing 'bit 12'.  If I used our
bits-to-bytes routine I would check "byte 21".

Then there's the EZACIC06 routine which also does a 'bits to bytes'
expansion, but also reorders things so that they have almost the same
reference as with CEESITST, except that they are 1 - 32 instead of 0 - 31.

If you can make any sense I've what I just said I can only assume you
already know what I'm talking about.  :-)

Frank


n 3/12/2007 at 3:32 AM, in message
<579Jh.240693$_X1.83265@fe05.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
> Of course the "odd" thing is how you need to create the parms for a call 
> to 
…[40 more quoted lines elided]…
> this is correct, but I think it is.
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-12T21:57:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61kJh.245355$_X1.187876@fe05.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET> <579Jh.240693$_X1.83265@fe05.news.easynews.com> <45F55862.6F0F.0085.0@efirstbank.com>`

```
Frank,
   When I posted my example, I thought about the fact that the actual parms with 
"numbers" could only be up to 32, so "truncation" with a PIC S9(9) COMP (or 
BINARY) field would NOT occur.  Furthermore, I know that COMP-5 still isn't 
available on VSE.  However, for Z/OS, I think that COMP-5 should be used for ALL 
"binary" fields passed to LE - just because one never knows "what it will do 
with it".
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-13T12:28:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55m609F25cccdU1@mid.individual.net>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET>`

```

"CG" <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote in message 
news:55953$45f4e0a0$4275fbdb$18078@FUSE.NET...
> Pete Dashwood wrote:
>> "CG" <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote in message 
…[109 more quoted lines elided]…
> special other than use the service provided...  It's part of the system.

So is Java ... :-)

>
> As you would probably expect, please consider that Bill's question was 
…[6 more quoted lines elided]…
> shifting and testing bits.]

No, I understand that, my reservation was about the case where the bit 
string interpretation might be required for cases OTHER than the one Bill 
raised.

I wasn't aware he was "objecting" ... seems to me he simply asked what 
people would do.

>
> I don't find the binary returned value objectionable because it is highly 
> unlikely that you would ever actually translate the value to anything, 
> much less a character.  You test it with a relatively fast compare and get 
> on with the logic.

Sure. It wasn't an objection; just something I noted in passing.
>
> Certainly, if you want to broaden the subject to include all situations of 
> bit mangling, then native language [IMHO] is the only way to go.

Certainaly that is an arguable option.

> And, if you are in control of the application design and know you are 
> lacking such language, change the design to match the features you do 
> have.

Sounds a bit like the tail wagging the dog... :-) Nevertheless, I agree it 
is a bit pointless designing stuff that cannot be implemented with the 
materials and tools at hand.
>
> Finally, your objection to 'bit mapping' is noted, but a FIND in the 
> message text returned your use of the word 'mapping' as the only instance.

Hmmm... I checked each message I have posted to this thread and I can't find 
that. Are you sure it wasn't quoted within a message from me?  It doesn't 
really matter anyway; again it was an observation in passing.

Pete.
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-13T01:20:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8%mJh.289464$ff2.83789@fe02.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET> <55m609F25cccdU1@mid.individual.net>`

```
Just a point of clarification (and explanation)

 Carl is aware of my OBJECTION to the way that CEE3INF returns its information 
(from other ways that we communicate).

As far as the comp.lang.cobol thread goes, I really was interested in exactly 
HOW experienced COBOL programmers (both in and out of an IBM LE environment) 
would handle the requirement to "decode" the bits within a 1 byte (or larger) 
string of bits.  I was also interested in how this would be solved in situations 
where one is interested in only the single value of a single bit vs the case 
where one might want to see the entire "layout" of the string of bits.

I have been interested in responses that were related specially to the LE 
environment (z/OS *or* VSE).  However, I have also been interested in responses 
that represent other (possibly more portable) solutions to the general problem.
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2007-03-13T04:10:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uupJh.64692$as2.11483@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<8%mJh.289464$ff2.83789@fe02.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET> <55m609F25cccdU1@mid.individual.net> <8%mJh.289464$ff2.83789@fe02.news.easynews.com>`

```
Bill,

I just looked a COBOL program in my shop that uses a table with 256 
entries.  The entries look something like this:

01  BYTE-TABLE-DATA.
     05  FILLER    PIC X(08) VALUE '00000001'.
     05  FILLER    PIC X(08) VALUE '00000010'.
     05  FILLER    PIC X(08) VALUE '00000011'.
     05  FILLER    PIC X(08) VALUE '00000100'.
And so forth, up to
     05  FILLER    PIC X(08) VALUE '11111111'.

01  BYTE-TABLE  REDEFINES BYTE-TABLE-DATA.
     05  DECODED-BYTE    OCCURS 256 TIMES  PIC X(08).

Then you simply take the byte you want to expand, coerce it into a PIC 
  S9(4) COMP field (or BINARY or COMP-5), add +1 to it, and use it as 
an index to retrieve the 8 byte field that contains ones and zeros.

05  BYTE-SUB    PIC S9(4) COMP VALUE ZERO.
05  FILLER      REDEFINES BYTE-SUB.
     10  FILLER          PIC X(01).
     10  BIT-MAP-BYTE    PIC X(01).

MOVE ZERO      TO BYTE-SUB
MOVE SOME-BYTE TO BIT-MAP-BYTE
ADD +1         TO BYTE-SUB
MOVE DECODED-BYTE (BYTE-SUB) TO ....

I haven't benchmarked this, but I suspect it ought to be faster than 
division.  It is relatively easy to understand and implement.

I'm not saying this is the best way, or the most efficient way.  But 
it is one way to do it entirely in COBOL.

With kindest regards,


William M. Klein wrote:
> Just a point of clarification (and explanation)
> 
…[13 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: How would you do this?

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-13T04:35:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JSpJh.224278$PW4.151954@fe03.news.easynews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <9fdc5$45f4ba41$4275fbdb$21645@FUSE.NET> <55k39jF25hnt2U1@mid.individual.net> <55953$45f4e0a0$4275fbdb$18078@FUSE.NET> <55m609F25cccdU1@mid.individual.net> <8%mJh.289464$ff2.83789@fe02.news.easynews.com> <uupJh.64692$as2.11483@bgtnsc05-news.ops.worldnet.att.net>`

```
Actually, it might be interesting to put the "source" for such a problem in a 
COPYBOOK and then do a COPY into a NESTED program with the code (where you 
"pass" to it the byte you want to "decode" and pass back the decoded
PIC X(8) field.

If you did a COPY SUPPRESSING (IBM extension), you wouldn't even need to see all 
the 256 FILLER definitions.
```

#### ↳ Re: How would you do this?

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-12T08:43:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vam7smnj5dmd8@news.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com>`

```
William M. Klein wrote:
> Now, my question is how various "experienced" COBOL programmers would
> handle such information (either in an IBM mainframe environment OR in
> other COBOL environments for those who see this note and don't work
> in IBM mainframe environments - but do get "bit maps")

By reducing the problem to one that's already been solved?

From the ETK collection of nifty subroutines:

-------
Summary: Provides bit manipulations of up to 32 bits. Can get, set, clear, 
test, and pack bits.

How to use: Instead of non-portable redefinitions to access bits packed in 
numeric variables, use BITPK's get operation to convert a number into a 
string of 32 characters each with values "0" or "1". You can then easily 
test or otherwise manipulate these character values. The pack operation 
packs the character values back into a number.

Limitations: At most 32 bits can be handled at a time.

To call BITPK, define BITPK-CONTROL as follows:

              01  BITPK-CONTROL.
                  02  BITPK-TASK-ID           PIC X(4) .
                  02  BITPK-OPERATION         PIC X(1) .
                  02  BITPK-FEEDBACK          PIC X(1) .
                  02  BITPK-NUMBER            PIC 9(10).
                  02  BITPK-BITS.
                      03  BITPK-BIT           PIC X(1)  OCCURS 32 TIMES.
Define CALL-BITPK as follows:
              CALL-BITPK.
                  CALL "BITPK"
                        USING BITPK-CONTROL
              .
BITPK supports the following operations:

  a.. G (get)
  Get the bits of BITPK-NUMBER interpreted as an unsigned 32-bit number. If 
the number is larger than 32 bits a (R)ANGE feedback is returned and the bit 
string is all zeroes.

  b.. P (pack)
  The reverse operation of get. Builds the 32-bit number having the bit 
string given in BITPK-BITS.

  c.. S (set)
  For each bit of the bit string given that is a one, set the corresponding 
bit in BITPK-NUMBER. This is the binary OR operation.

  d.. A (and)
  For each bit of the bit string given that is a one, set the corresponding 
bit in BITPK-NUMBER if that bit is also a one, otherwise clear the bit. This 
is the binary AND operation.

  e.. X (xor)
  For each bit of the bit string given that is different from the 
corresponding bit in BITPK-NUMBER, set that bit in BITPK-NUMBER, otherwise 
clear the bit. This is the binary XOR operation.

  f.. C (clear)
  For each bit of the bit string given that is a one, clear the 
corresponding bit in BITPK-NUMBER.

  g.. 1 (test for 1)
  For each bit of the bit string given that is a one, test if the 
corresponding bit in BITPK-NUMBER is a one. Return an (A)LL feedback if all 
bits tested were ones, a (N)ONE feedback if none of the bits were ones, or a 
(S)OME feedback if only some of them were.

  h.. 0 (test for 0)
  For each bit of the bit string given that is a one, test if the 
corresponding bit in BITPK-NUMBER is a zero. Return an (A)LL feedback if all 
bits tested were zeroes, a (N)ONE feedback if none of the bits were zeroes, 
or a (S)OME feedback if only some of them were.
BITPK returns these feedbacks: a space means there were no errors. An "O" 
means that the specified operation was invalid. An "R" means that the number 
given was too large. An "A", "N", or "S" means that either All, None, or 
Some bits met the condition.

-------
```

##### ↳ ↳ Re: How would you do this?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-12T14:05:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vb5n41hesrf29@corp.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12vam7smnj5dmd8@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
news:12vam7smnj5dmd8@news.supernews.com...
> William M. Klein wrote:
> > Now, my question is how various "experienced" COBOL programmers would
…[4 more quoted lines elided]…
> By reducing the problem to one that's already been solved?

I thought about recommending ETKPAK, as well;
but rejected it as "overkill" and my feeling that it
did not solve the problem of obtaining the values
of multi-bit fields.

> From the ETK collection of nifty subroutines:
[snip]
>                   02  BITPK-NUMBER            PIC 9(10).

Be aware that this field is has usage COMP in the
linkage section of the called program.
```

###### ↳ ↳ ↳ Re: How would you do this?

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-12T14:08:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vb98up3e49na4@news.supernews.com>`
- **References:** `<rrDIh.242220$k82.140284@fe07.news.easynews.com> <12vam7smnj5dmd8@news.supernews.com> <12vb5n41hesrf29@corp.supernews.com>`

```
Rick Smith wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
> news:12vam7smnj5dmd8@news.supernews.com...
…[13 more quoted lines elided]…
>

Well not directly, it doesn't. It takes a 32-bit value and maps it to 32 
one-byte fields which can be individually tested. The rest is left as an 
exercise for the reader.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
