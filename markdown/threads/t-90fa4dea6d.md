[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL PIC 9 comparison problem.

_6 messages · 3 participants · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL PIC 9 comparison problem.

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk>`

```
Does anybody know of a MF setting that would alter the way that PIC 9 fields
would be processed?

I've always understood that comparing 2 PIC 9 fields would always do a
numeric comparison regardless of the length.  However I have had a bug
reported in MF Cobol that doesn't do this. E.g.  We have a structure which
in part looks something like this:

01  WS02-FIELDS.
       05  WS02-OCCURS OCCURS 350.
             10  WS02-DECIMALS        PIC 9(01).
             10  WS02-FLD-SIZE           PIC 9(02).


With code  like:

IF WS02-FLD-SIZE (SUB1) < WS02-DECIMALS (SUB1)
        PERFORM FLD-SIZE-ERROR.

We get an error condition whenever the first byte of the PIC 9(02) field is
less than the PIC 9(1) field so 14 is considered less than 2, i.e. it seems
to be doing a character compare not a numeric one.

Can anybody explain this?  Is there a known rule in COBOL or Micro Focus
COBOL

The identical code works fine in AS400 and WANG COBOL.

In the meantime I'm arranging additional tests.

BTW we have been using AS400 COBOL for c 9 years, WANG COBOL for c 18 years
and MF COBOL for c 5 years but we have recently changed our MF version from
3.0 to 4.0.  Also the MF Cobol is running on hp unix.

TIA

Rick
```

#### ↳ Re: MF COBOL PIC 9 comparison problem.

- **From:** "Gary Roush" <support@adtools.com>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77ofqu$4au$1@remarQ.com>`
- **References:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk>`

```
Rick,

I think it works on the mainframe because the processing of data is
different where data on the PC is use differently so you have to do things a
little differently and more specific.

You may have to redefine so that you are comparing one-byte or two byte
fields instead of comparing 2 bytes to a 1 byte field, especially when it is
numeric.

If you want a sample, e-mail me and I'll give you one.

Regards,
Gary

Rick Price wrote in message
<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk>...
>Does anybody know of a MF setting that would alter the way that PIC 9
fields
>would be processed?
>
…[35 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF COBOL PIC 9 comparison problem.

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a01021.92235500@news1.ibm.net>`
- **References:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk> <77ofqu$4au$1@remarQ.com>`

```
On Fri, 15 Jan 1999 15:38:40 -0700, "Gary Roush" <support@adtools.com>
wrote:

>Rick,
>
…[7 more quoted lines elided]…
>

This is not correct.  Reguardless of compiler and platform PIC 9 and
PIC 99 fields should compare for value properly.
```

#### ↳ Re: MF COBOL PIC 9 comparison problem.

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a00f90.92090332@news1.ibm.net>`
- **References:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk>`

```
On Fri, 15 Jan 1999 18:01:18 -0000, "Rick Price"
<rick@hpdi.demon.co.uk> wrote:

>Does anybody know of a MF setting that would alter the way that PIC 9 fields
>would be processed?
…[16 more quoted lines elided]…
>

Can you post the ACTUAL if?  and the Fields?  What I suspect - an old
(pre 3.2.5) version of MF COBOL - compiled as a GNT where the table
crosses a segment boundary.  Move the table to the top of working
storage and see what happens.  

Second possibility - Field being treated as reference modified -
that's why I wanted to see the actual compare.


>We get an error condition whenever the first byte of the PIC 9(02) field is
>less than the PIC 9(1) field so 14 is considered less than 2, i.e. it seems
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF COBOL PIC 9 comparison problem.

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<916765871.5512.0.nnrp-07.9e98b131@news.demon.co.uk>`
- **References:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk> <36a00f90.92090332@news1.ibm.net>`

```
Thane

Thanks for your 2 replies.  Apologies.  I've probably wasted your time.  I
got this thrown at me Friday night after being out of the office for a
couple of days and I didn't have the full facts from the developer.  In fact
the compare always failed when the 2 digit value was < 10 i.e. when it
started with zero.  E.g. it would  say 09 was less than 2 but would always
know that a 2 digit number 10 or above was higher than a 1 digit number
(which of cource it always is so it doen't really mean that the compile was
working in this case).  However if I'd known this I would have suspected a
compile bug.

In fact you are right  about the GNT.  When we tested it using the INT then
everything was hunky dory.  However the compiler version is MF COBOL for
unix 4.0 not pre 3.2.5.  We did move the table to the top of working storage
but that didn't correct things.

We wrote simple programs to try to isolate the problem but they always
worked.  In fact we tried so many things that the programmer  finally
swapped the IF statement
from IF 2digits < 1digit to if 1digit > 2digits.  This worked in both the
INT and GNT versions and recognised 9 as > 08 and 8 < 09.

All very worrying.  We will plod on.

Thanks again for your help

Rick


Thane Hubbell wrote in message <36a00f90.92090332@news1.ibm.net>...
>On Fri, 15 Jan 1999 18:01:18 -0000, "Rick Price"
><rick@hpdi.demon.co.uk> wrote:
>
>>Does anybody know of a MF setting that would alter the way that PIC 9
fields
>>would be processed?
>>
…[26 more quoted lines elided]…
>>We get an error condition whenever the first byte of the PIC 9(02) field
is
>>less than the PIC 9(1) field so 14 is considered less than 2, i.e. it
seems
>>to be doing a character compare not a numeric one.
>>
…[7 more quoted lines elided]…
>>BTW we have been using AS400 COBOL for c 9 years, WANG COBOL for c 18
years
>>and MF COBOL for c 5 years but we have recently changed our MF version
from
>>3.0 to 4.0.  Also the MF Cobol is running on hp unix.
>>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF COBOL PIC 9 comparison problem.

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a53b09.78499096@news1.ibm.net>`
- **References:** `<916423848.26012.0.nnrp-10.9e98b131@news.demon.co.uk> <36a00f90.92090332@news1.ibm.net> <916765871.5512.0.nnrp-07.9e98b131@news.demon.co.uk>`

```
On Tue, 19 Jan 1999 17:14:01 -0000, "Rick Price"
<rick@hpdi.demon.co.uk> wrote:


>In fact you are right  about the GNT.  When we tested it using the INT then
>everything was hunky dory.  However the compiler version is MF COBOL for
>unix 4.0 not pre 3.2.5.  We did move the table to the top of working storage
>but that didn't correct things.
>

I've seen this behavior more than once between INT and GNT's.  (MF
swears the end results are the same though).  Sometimes it's the other
way around - the INT fails and the GNT works <G>.  The software where
I used to work was a mishmash of INT's and GNTs.  We were continually
fighting problems where we had a problem in the GNT so decided to make
the program an INT from them on.  Well, if you issue a CALL "PROGRAM"
and you don't specify INT or GNT - it loads the GNT first.  So
leftover GNT's would kill us sometimes.  What a mess.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
