[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Testing for optional COMP-3 fields.

_18 messages · 9 participants · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Testing for optional COMP-3 fields.

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```
On programs we use to read switch data, we found a set of four fields
which, as a set, may or may not be present in any one record.  These
records are part of a (more or less) standard variable block/record data
set so we can assume the record descriptor word is accurate and we can
get to the next record in the block.  The fields following the optional
set contain COMP-3 data we are interested in, but are of different
lengths.

03  OPTIONAL-FIELD-1    PIC S9(3) COMP-3.
03  OPTIONAL-FIELD-2    PIC S9(7) COMP-3.
03  OPTIONAL-FIELD-3    PIC S9(3) COMP-3.
03  OPTIONAL-FIELD-4    PIC S9(7) COMP-3.
03  REAL-LEGITIMATE-FIELD     PIC S9(5) COMP-3.

Using RM (AccuCobol), we don't have a numeric class test for valid
COMP-3 data.

The question:  How do we test for these fields?  TIA
```

#### ↳ Re: Testing for optional COMP-3 fields.

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bhvqa$t59$1@server.cntfl.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```

Warren Porter wrote in message <36DACB3C.D88809C@ASPMnetdoor.com>...
>On programs we use to read switch data, we found a set of four fields
>which, as a set, may or may not be present in any one record.  These
…[18 more quoted lines elided]…
>

Extract the code from the following program. It assumes the typical
IBM format that is used by Micro Focus and some others. I used
MF WB 3.2 and intrinsic functions.

It only validates signed fields but could be modified to validate
unsigned fields.
---------------
       identification division.
       program-id. valid-c3.
       data division.
       working-storage section.
       01  sample-data.
           03 OPTIONAL-FIELD-1 PIC S9(3) COMP-3 value +999.
           03 OPTIONAL-FIELD-2 PIC S9(7) COMP-3 value +9999999.
           03 OPTIONAL-FIELD-3 PIC S9(3) COMP-3 value -999.
           03 OPTIONAL-FIELD-4 PIC S9(7) COMP-3 value -9999999.

      * user supplies vc3-length and vc3-field
      * result is in vc3-valid-flag
       01  validate-comp-3-work.
           03  vc3-length pic s9(4) comp.
           03  vc3-ord pic s9(4) comp.
           03  vc3-left pic s9(4) comp.
           03  vc3-right pic s9(4) comp.
           03  vc3-x pic s9(4) comp.
           03  vc3-valid-flag pic x.
               88 vc3-valid value "y".
               88 vc3-invalid value "n".
           03  vc3-field pic x(10).
       procedure division.

      * fields are valid initially
           perform validate-fields

      * make the fields invalid
           move spaces to sample-data
           perform validate-fields

      * make the fields valid again
           initialize sample-data
           perform validate-fields

           stop run
           .
       validate-fields.
           perform validate-field-1
           perform validate-field-2
           perform validate-field-3
           perform validate-field-4
           .
       validate-field-1.
           compute vc3-length = function length (OPTIONAL-FIELD-1)
           move OPTIONAL-FIELD-1 (1:vc3-length) to vc3-field
           perform validate-comp-3-field
           if vc3-invalid
               display "OPTIONAL-FIELD-1 is Invalid"
           else
               display "OPTIONAL-FIELD-1 is Valid"
           end-if
           .
       validate-field-2.
           compute vc3-length = function length (OPTIONAL-FIELD-2)
           move OPTIONAL-FIELD-2 (1:vc3-length) to vc3-field
           perform validate-comp-3-field
           if vc3-invalid
               display "OPTIONAL-FIELD-2 is Invalid"
           else
               display "OPTIONAL-FIELD-2 is Valid"
           end-if
           .
       validate-field-3.
           compute vc3-length = function length (OPTIONAL-FIELD-3)
           move OPTIONAL-FIELD-3 (1:vc3-length) to vc3-field
           perform validate-comp-3-field
           if vc3-invalid
               display "OPTIONAL-FIELD-3 is Invalid"
           else
               display "OPTIONAL-FIELD-3 is Valid"
           end-if
           .
       validate-field-4.
           compute vc3-length = function length (OPTIONAL-FIELD-4)
           move OPTIONAL-FIELD-4 (1:vc3-length) to vc3-field
           perform validate-comp-3-field
           if vc3-invalid
               display "OPTIONAL-FIELD-4 is Invalid"
           else
               display "OPTIONAL-FIELD-4 is Valid"
           end-if
           .
       validate-comp-3-field.
      * this routine assumes 8 bit characters
      * and the sign in the least significant 4 bits of the field
           set vc3-valid to true
      * for each pair of digits
           perform varying vc3-x from 1 by 1
             until vc3-x > vc3-length
                 or vc3-invalid
      * get the binary value
               compute vc3-ord
                   = function ord (vc3-field(vc3-x:1)) - 1
      * separate the values for the left and right halves
               divide 16 into vc3-ord
                   giving vc3-left
                   remainder vc3-right
      * check the left half digit
               if vc3-left > 9
                   set vc3-invalid to true
               else
                   if vc3-x = vc3-length
      * check for valid sign, assumes x"C" and x"D" are valid
                       if vc3-right not = 12 and 13
                           set vc3-invalid to true
                       end-if
                   else
      * check the right half digit
                       if vc3-right > 9
                           set vc3-invalid to true
                       end-if
                   end-if
               end-if
           end-perform
           .
---------------
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

#### ↳ Re: Testing for optional COMP-3 fields.

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ZSC2.31858$rs2.9336482@client.news.psi.net>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```
Perhaps others might not feel the same way, but I found the problem
description a bit too terse.

Can you expand?  For example, using RM/COBOL the term "record descriptor
word" does not mean anything; I assume that you are reading some sort of
file produced outside the "COBOL world" the structure of which is not given
in the example.

Given enough of the problem, I think I can help you with a solution in
RM/COBOL.

Regards,
Tom Morrison
Liant Software Corporation

Warren Porter wrote in message <36DACB3C.D88809C@ASPMnetdoor.com>...
>On programs we use to read switch data, we found a set of four fields
>which, as a set, may or may not be present in any one record.  These
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Testing for optional COMP-3 fields.

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RqUC2.3844$w57.1386458@news3.mia>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```
If somebody really designed a record layout like that and did not
provide a code in the record to tell you which format it is, they
should be locked up, immediately.
```

##### ↳ ↳ Re: Testing for optional COMP-3 fields.

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DC67BE.5B0E222F@ASPMnetdoor.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <RqUC2.3844$w57.1386458@news3.mia>`

```
Judson McClendon wrote:

> If somebody really designed a record layout like that and did not
> provide a code in the record to tell you which format it is, they
> should be locked up, immediately.

If only life were that simple.  Phone switches can be configured to do a
number of different things and files from various switches may be combined
before our program sees it.  The fields may not have those fields if they
were sent over a modem but would be included if the switch has to write a
tape.  If I had been asked early enough I would have the same opinion as you,
but (alas & alack) I wasn't asked at all.

>
> --
…[25 more quoted lines elided]…
> >Warren Porter
```

#### ↳ Re: Testing for optional COMP-3 fields.

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bh8js$qjb$1@client2.news.psi.net>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```
I have been communicating privately with Warren Porter about a solution to
his problem.

This post is to clarify this particular assertion:


Warren Porter wrote in message <36DACB3C.D88809C@ASPMnetdoor.com>...
[snip problem description]
>
>Using RM (AccuCobol), we don't have a numeric class test for valid
>COMP-3 data.


RM/COBOL does indeed have a numeric class test; always has.  And it works
for COMP-3 fields.  Indeed, the sign representation is configurable to
accommodate various sign conventions.

I can make no representation for AcuCOBOL.

Regards,
Tom Morrison
Liant Software Corporation
```

##### ↳ ↳ Re: Testing for optional COMP-3 fields.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bha6j$b18@dfw-ixnews6.ix.netcom.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net>`

```
And the good new (my usual plug) is that the next Standard will include the
IF NUMERIC test for Packed-Decimal (and other types of non-Display) numeric
data.  Obviously, this will work for the ANSI/ISO "USAGE Packed-Decimal" but
I assume that any vendor that does support Usage Comp-3 as "packed data"
will also implement this for that USAGE as well.
```

##### ↳ ↳ Re: Testing for optional COMP-3 fields.

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DC39E8.9B7F982F@ASPMnetdoor.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net>`

```
Tom Morrison wrote:

> I have been communicating privately with Warren Porter about a solution to
> his problem.

Thank you.

> This post is to clarify this particular assertion:
>
…[10 more quoted lines elided]…
> I can make no representation for AcuCOBOL.

I tried the following test:
    35         01 PACK-TABLE PIC X(8) VALUE X"012C45678C00000C".
    36         01 FILLER REDEFINES PACK-TABLE.
    37            05 FIELD1   PIC S999 COMP-3.
    38            05 FIELD2   PIC S9(5) COMP-3.
    39            05 FIELD3   PIC S9(3) COMP-3.
    40            05 FIELD4   PIC S9    COMP-3.
----------------------------------------------------------
   101             IF FIELD1 IS NUMERIC DISPLAY "1 NUMERIC"
   102               ELSE DISPLAY "1 FAILED".
with similar code for each field.  Field3 should have failed since it doesn't
have a sign, but each field passed.

It appears I will have to test for sign bytes by moving them to the low end of
a binary field, dividing by 16, and testing the remainder for > 9.  That was a
last resort though, I was hoping something in COBOL could handle it.

Thanks for looking at it though.
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bho4d$1l$1@client2.news.psi.net>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com>`

```

Warren Porter wrote in message <36DC39E8.9B7F982F@ASPMnetdoor.com>...
>Tom Morrison wrote:
>
[snip]
>>
>> RM/COBOL does indeed have a numeric class test; always has.  And it works
…[15 more quoted lines elided]…
>with similar code for each field.  Field3 should have failed since it
doesn't
>have a sign, but each field passed.
>
>It appears I will have to test for sign bytes by moving them to the low end
of
>a binary field, dividing by 16, and testing the remainder for > 9.  That
was a
>last resort though, I was hoping something in COBOL could handle it.


Well I gave it a go with RM/COBOL with the following results:
===
RM/COBOL-85 Runtime - Version 6.10.00 for DOS 3.3+.
Copyright (c) 1985, 1986-1996 by Liant Software Corp.  All rights reserved.


1 NUMERIC
2 NUMERIC
3 FAILED
4 NUMERIC

COBOL STOP RUN at line 21 in TEST (C:\TEMP\TEST.COB).
===

This also worked with the 6.5 version for Windows.  What version of RM/COBOL
failed?  I need to get an defect report in ASAP.

Regards,
Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 4)_

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ojKnZGARpa32IwHm@rcav8r.demon.co.uk>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com> <7bho4d$1l$1@client2.news.psi.net>`

```
In article <7bho4d$1l$1@client2.news.psi.net>, Tom Morrison
<t.morrison@liant.com> writes
>
>Well I gave it a go with RM/COBOL with the following results:
…[9 more quoted lines elided]…
>4 NUMERIC

Just for completeness (since Acucobol was mentioned earlier in
the thread) I tried it under Acucobol-GT and got exactly the same
results as Tom.

Nigel 
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 5)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdwD2.5$bg2.13502@client.news.psi.net>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com> <7bho4d$1l$1@client2.news.psi.net> <ojKnZGARpa32IwHm@rcav8r.demon.co.uk>`

```
Nigel Eaton wrote in message ...
[snip]
>Just for completeness (since Acucobol was mentioned earlier in
>the thread) I tried it under Acucobol-GT and got exactly the same
…[3 more quoted lines elided]…
>Nigel Eaton - Acucorp Systems Engineering, posting from home.


Nigel, Warren was using AcuCOBOL ver 2.4.1, which gave a false positive.  He
then tested with -GT and got correct results as you have confirmed.  I
presume that 2.4.1 has been superceded by -GT.

Regards,
Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 4)_

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990303091229.12874.00002126@ng-fi1.aol.com>`
- **References:** `<7bho4d$1l$1@client2.news.psi.net>`

```
That is really interesting since in COBOL II (and prior versions) a numeric
check is only valid on Alphanumeric fields.  How does RM Cobol get around this?

Tom Wymer
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bk4el$4ro@dfw-ixnews11.ix.netcom.com>`
- **References:** `<7bho4d$1l$1@client2.news.psi.net> <19990303091229.12874.00002126@ng-fi1.aol.com>`

```
I assume that by "COBOL II" you mean the IBM product "VS COBOL II".  If so,
you are not correct.  I think every IBM (mainframe) compiler has supported
this for years.  The following is a direct quote from the most current LRM,

"The NUMERIC test cannot be used with an identifier described as alphabetic
or as a group item that contains one or more signed elementary items.

For numeric data items, the identifier being tested can be described as
USAGE DISPLAY, (or as IBM extensions) USAGE COMPUTATIONAL-3, or USAGE
PACKED-DECIMAL. "

See,
  "6.1.6.2 Class Condition"
at

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYLR201/6.1.6
..2
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DD2EC7.F15D8BF2@zip.com.au>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com>`

```
Warren Porter wrote:
> 
.. lot's of stuff about comp-3 snipped ...

Warren,

I just started with a Telco and had the 'joy' of working out how they
decoded these records.  TBCD is like packed but has an 'A' instead of
zero so that Nulls are end of number (if you dial 911 you get X'9110' or
here in Aus we dial 000 X'AAA0'.  Anyway the packed number had to be
interpreted half byte by half byte.  Here is my basic solution (you
would not want the way the real one was coded).  Assume a 9(4) COMP
field is two bytes (you will have to work out endian's)

05  number pic 9(4) comp.
05 filler redefines number.
   10  filler pic x(01).
   10  Byte   pic x(01).

move input-byte to byte.

divide byte by 16 giving top-nyble
		  remainder bottom-nyble.

Ok take it from there.  If the bottom nible is not 0-9 then it is a
short integer.

Wait until you have to extract the but flags out of the record.....

Ken
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 4)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R4wD2.4$bg2.11612@client.news.psi.net>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com> <36DD2EC7.F15D8BF2@zip.com.au>`

```

Ken Foskey wrote in message <36DD2EC7.F15D8BF2@zip.com.au>...
>Warren Porter wrote:
[snip]
>
>divide byte by 16 giving top-nyble
>   remainder bottom-nyble.


If speed is an issue, one should consider a OCCURS 256 table.  A subscripted
lookup on a one dimension table will likely be faster than a
DIVIDE...REMAINDER.  Even with hardware divide support, both methods should
be tested.

Tom Morrison
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 5)_

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DEA339.C5B2357C@ASPMnetdoor.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com> <36DD2EC7.F15D8BF2@zip.com.au> <R4wD2.4$bg2.11612@client.news.psi.net>`

```
Tom Morrison wrote:

> Ken Foskey wrote in message <36DD2EC7.F15D8BF2@zip.com.au>...
> >Warren Porter wrote:
…[8 more quoted lines elided]…
> be tested.

Will look into that.  I recall that was exactly how IBM checked for a COMP-3
numeric class test: a table used by the TRanslate & Test contained zero for DD,
a 1 for DS {D = 0-9, S = A-F}, and 2 for SD or SS.

To save an extra post, Ken Fosley said:
>I just started with a Telco and had the 'joy' of working out how they
>decoded these records.  TBCD is like packed but has an 'A' instead of
>zero so that Nulls are end of number (if you dial 911 you get X'9110' or
>here in Aus we dial 000 X'AAA0'.  Anyway the packed number had to be
>interpreted half byte by half byte.

The first byte of a "structure" (on USA switches anyway) is x"AA" if the switch
properly recorded the call. We check it by comparing it to X"AA" if that was
what you were talking about. The IBM UNPK command wasn't susceptible to
data exceptions, perhaps its equivalent on other platforms works the same way.
Might be worth a test?!?
```

###### ↳ ↳ ↳ Re: Testing for optional COMP-3 fields.

_(reply depth: 6)_

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DEAAD1.79401831@ASPMnetdoor.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com> <7bh8js$qjb$1@client2.news.psi.net> <36DC39E8.9B7F982F@ASPMnetdoor.com> <36DD2EC7.F15D8BF2@zip.com.au> <R4wD2.4$bg2.11612@client.news.psi.net> <36DEA339.C5B2357C@ASPMnetdoor.com>`

```
Warren Porter wrote:

> The IBM UNPK command wasn't susceptible to
> data exceptions, perhaps its equivalent on other platforms works the same way.
> Might be worth a test?!?

Just did
       01 PACK-TABLE PIC X(8) VALUE X"012C45678C0C000C".
        01  NEW-TEST.
          05  NEW-PACKED        PIC S9(9) COMP-3.
          05  FILLER            PIC X.
       01  NEW-DISPLAY.
          05  NEW-NUM          PIC S9(9) VALUE ZERO.
--------------
           MOVE PACK-TABLE(1:6) TO NEW-TEST.
           stop 1.
           MOVE NEW-PACKED TO NEW-NUM.
Looking at NEW-DISPLAY in a debugging session showed 012<4567, but that would only
work on an ASCII machine.  A compiler with a usage for unsigned packed might show
the same result but wouldn't need the filler at the end and would have an even
number of digits at each end.
```

#### ↳ Re: Testing for optional COMP-3 fields.

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990301220851.07557.00002200@ng-fa1.aol.com>`
- **References:** `<36DACB3C.D88809C@ASPMnetdoor.com>`

```
let say you can move this fields to regular numeric fields, defined in ws
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
