[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL - BIT MANIPULATION

_5 messages · 5 participants · 1996-02_

---

### COBOL - BIT MANIPULATION

- **From:** "jac..." <ua-author-17086468@usenetarchives.gap>
- **Date:** 1996-02-07T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fcvib$n82@tst.hk.super.net>`

```

Hello all,

Someone tells me today that Cobol can now manipulate low level storage -
bits. However, my knowledge of Cobol is that this language can only
support byte level manipulation. In some cases, half byte when dealing
with internal representation of numbers using a series of MOVE statements
+ carefully PICTURE Redefines.

I am from IBM MVS Cobol background. Could anyone out there tell me which
diaclet of Cobol can play around with bits (which in fact I do not
believe I will do) ?

Thank you in advance !
```

#### ↳ Re: COBOL - BIT MANIPULATION

- **From:** "cbat..." <ua-author-8582281@usenetarchives.gap>
- **Date:** 1996-02-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cfd4cd474-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4fcvib$n82@tst.hk.super.net>`
- **References:** `<4fcvib$n82@tst.hk.super.net>`

```
jac··.@new··r.net (Mr Jacky Ho) wrote:


› Hello all,
 
› [snip]
 
› I am from IBM MVS Cobol background.  Could anyone out there tell me which 
› diaclet of Cobol can play around with bits (which in fact I do not 
› believe I will do) ?

I just took a COBOL class last semester after having taken both 2
semesters of C++ and one semester of assembly, and asked if COBOL
could do bit manipulation of data. My instructor had been a
programmer for some company out of Texas (which is unimportant), but
he claims to have done such things with COBOL-74. I didn't want to
know how because I didn't see an easy way to implement it, nor did I
need to use bit manipulation for the projects required in the class.

So, I guess I'm not much help, but good luck.

Craig Bateman
cba··.@bco··a.us
```

##### ↳ ↳ Re: COBOL - BIT MANIPULATION

- **From:** "r..." <ua-author-12494308@usenetarchives.gap>
- **Date:** 1996-02-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cfd4cd474-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5cfd4cd474-p2@usenetarchives.gap>`
- **References:** `<4fcvib$n82@tst.hk.super.net> <gap-5cfd4cd474-p2@usenetarchives.gap>`

```
cba··.@bco··a.us (Craig Bateman) writes:

› jac··.@new··r.net (Mr Jacky Ho) wrote:
 
 
›› Hello all,
 
› [snip]
 
› I am from IBM MVS Cobol background.  Could anyone out there tell me which 
› diaclet of Cobol can play around with bits (which in fact I do not 
› believe I will do) ?

REALIA COBOL can play with bits (MLI_OR / MLI_AND) but in nearly every
dialect you have COMP-5 variables, so you can redefine PIC XXX as
PIC S9(6) COMP-5, extract the bits in the last two byts by dividing (you
cant do it with PIC XX and S9(4) COMP-5, 'cause you have'nt the full range
up to 16384 then) into a array and do the manipulations by yourself.

Not the best way, but I'm sure it works ...

Cu, Ralf.
--------------------------------------------------------------------------------
Ralf Draeger          Megacom EDV-Loesungen GmbH 
r.··.@meg··m.de        Zur Heupresse 4
r.··.@tn··t.de           82140 Olching                     No clever qoutes yet ...
```

#### ↳ Re: COBOL - BIT MANIPULATION

- **From:** "szh..." <ua-author-17086494@usenetarchives.gap>
- **Date:** 1996-02-11T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cfd4cd474-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4fcvib$n82@tst.hk.super.net>`
- **References:** `<4fcvib$n82@tst.hk.super.net>`

```
jac··.@new··r.net (Mr Jacky Ho) wrote:

› Someone tells me today that Cobol can now manipulate low level storage -
› bits.


Bit manipulation in COBOL is (and always was!) very easy on a Unisys
2200-platform (ex Sperry Univac). It exists a picture definition there
that represents 1 bit.


---------------------------------------
Schweizerische Bankgesellschaft
EZIU/EUBA-DPP
```

#### ↳ Re: COBOL - BIT MANIPULATION

- **From:** "dan yates" <ua-author-17086085@usenetarchives.gap>
- **Date:** 1996-02-11T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cfd4cd474-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4fcvib$n82@tst.hk.super.net>`
- **References:** `<4fcvib$n82@tst.hk.super.net>`

```
Micro Focus allows bit manipulation to define the drive
letters in the PC_FIND_DRIVES routine. Drive_Info is an
elementary data item defined as pic x(4) comp-x.

On exit from a call the drive_info data item will contain the
26 least-significant bits corresponding to drives A: thru Z:.
A: is represented by bit 0 and Z: by bit 25. a corresponding
bit is set for each drive that is present.

this is taken from the COBOL System Reference Volume 1.

I have an example of this very call. E-mail yat··.@u··.edu
if you would like a copy of the program.

Dan Yates
University of Illinois @ Spfld.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
