[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading a Cobol file in C

_10 messages · 9 participants · 2000-05_

---

### Reading a Cobol file in C

- **From:** Carmel Ryan <carmel.ryan@comit.ie>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391BE590.91CCDCD7@comit.ie>`

```
Hello all,
I'm trying to process a cobol file created on a mainframe (not sure
exactly what machine).  I'm reading it through a C program in a Pentium
3 pc.
Based on following definitions how many bytes will be used -
S9(5) COMP-3  - (2.5 or 3 bytes?)
S9(3) COMP-3 -   (1.5 or 2 bytes?)
S9(9)V99 COMP-3 -  (5.5 or 6 bytes or what?)

I could do with some help fairly urgently,
Thanks in advance,
Carmel Ryan
```

#### ↳ Re: Reading a Cobol file in C

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ju1T4.3291$2j.1362653@news1.mco>`
- **References:** `<391BE590.91CCDCD7@comit.ie>`

```
Here's the RULE:

FOR PACKED-DECIMAL / COMP-3
    start with 1 ('SIGN' - no such thing as a P-D w/o sign)
    add up all the '9' positions INCLUDING any after 'V' or '.'

IF ODD , ADD 1
END-IF
DIVIDE SIZE by 2
(COBOL has no 1/2 byte concept)

SO  PIC S9(5) COMP-3 is
                1  + 5 = 6  is even so 6/3 = 2
       PIC S9(9)V99  COPM-3 is
               1+ 9 + 2 = 12 ,even so 12/2 = 6

       PIC S9(8)V99 COMP-3 is
                1 + 8 + 2 = 11 is ODD so 11 + 1 = 12, /2 = 6

Carmel Ryan <carmel.ryan@comit.ie> wrote in message
news:391BE590.91CCDCD7@comit.ie...
> Hello all,
> I'm trying to process a cobol file created on a mainframe (not sure
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Reading a Cobol file in C

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fi9i2$jtr$1@slb1.atl.mindspring.net>`
- **References:** `<391BE590.91CCDCD7@comit.ie> <Ju1T4.3291$2j.1362653@news1.mco>`

```
In case anyone is not clear on this (and particularly for those who find it
via www.deja.com):

The "attached" is true of many (possibly even MOST) environments where COBOL
runs.  It is *not* universally true.  There are COBOLs that "correctly"
handle unsigned Packed-Decimal items (with an even number of digits in the
PICTURE).  There have been (I don't know if there still are) implementations
that DO handle "half-bytes".

To the best of my knowledge (and I could be mistaken in this) what was posted
in the "attached" *is* true wherever USAGE COMP-3 = USAGE PACKED-DECIMAL.
(Most of these implementations either are - or historically have tried to
emulate - the IBM mainframe world and its "older" COBOLs.)
```

###### ↳ ↳ ↳ Re: Reading a Cobol file in C

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<my4T4.6014$XT2.53263@typhoon.austin.rr.com>`
- **References:** `<391BE590.91CCDCD7@comit.ie> <Ju1T4.3291$2j.1362653@news1.mco> <8fi9i2$jtr$1@slb1.atl.mindspring.net>`

```

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8fi9i2$jtr$1@slb1.atl.mindspring.net...
> In case anyone is not clear on this (and particularly for those who find
it
> via www.deja.com):
>
> The "attached" is true of many (possibly even MOST) environments where
COBOL
> runs.  It is *not* universally true.  There are COBOLs that "correctly"
> handle unsigned Packed-Decimal items (with an even number of digits in the
> PICTURE).  There have been (I don't know if there still are)
implementations
> that DO handle "half-bytes".

There are some (e.g. GCOS8) that don't have to, because a byte is 9 (NINE)
bits, so they have room for the sign in the last data byte.

All those calculations of how many bytes something takes are
platform dependent and not universal.
```

###### ↳ ↳ ↳ Re: Reading a Cobol file in C

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fil51$p5t$1@slb0.atl.mindspring.net>`
- **References:** `<391BE590.91CCDCD7@comit.ie> <Ju1T4.3291$2j.1362653@news1.mco> <8fi9i2$jtr$1@slb1.atl.mindspring.net> <my4T4.6014$XT2.53263@typhoon.austin.rr.com>`

```
To the person who sent me private email on this.

1) All comp-n data types are ABSOLUTELY non-Standard and therefore, totally
unportable.

2) Check Micro Focus (among others) for "COMP-6" where there is no
sign-nibble allocated for the "packed" fields.

3) What I said is true and there implementations where:

    Pic 99 Packed-Decimal takes one byte
                   and others (more common) where it takes two bytes

4) As for implementations with "half-byte support," I believe that if you
check www.deja.com for this topic, you will find a few.  My memory is that
this includes earlier versions of ICL products.  This allows (among other
things - assuming Comp-3 is packed) for

     01 Group1.
            05   Elem1 S99 Comp-3.
            05   Elem2 S99 Comp-3.

to have Group1 stored in 3 bytes, not  4.
```

###### ↳ ↳ ↳ Re: Reading a Cobol file in C

_(reply depth: 5)_

- **From:** Charles F Hankel <nieuws@hankel.freedombird.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ojaoisch92clt9q9gvn65craju4mg26c5q@4ax.com>`
- **References:** `<391BE590.91CCDCD7@comit.ie> <Ju1T4.3291$2j.1362653@news1.mco> <8fi9i2$jtr$1@slb1.atl.mindspring.net> <my4T4.6014$XT2.53263@typhoon.austin.rr.com> <8fil51$p5t$1@slb0.atl.mindspring.net>`

```
In an idle moment, "William M. Klein" <wmklein@nospam.ix.netcom.com>
wrote:

>4) As for implementations with "half-byte support," I believe that if you
>check www.deja.com for this topic, you will find a few.  My memory is that
…[7 more quoted lines elided]…
>to have Group1 stored in 3 bytes, not  4.

This seems to match with a hazy memory of mine - also something to do
with the ICL1900 operating on a 24-bit word and everything centred on
the word rather than the byte, which was not in the ICL vocabulary.
However, I could be completely and utterly wrong.
```

###### ↳ ↳ ↳ Re: Reading a Cobol file in C

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391DE9DC.B02FA8E@zip.com.au>`
- **References:** `<391BE590.91CCDCD7@comit.ie> <Ju1T4.3291$2j.1362653@news1.mco> <8fi9i2$jtr$1@slb1.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> In case anyone is not clear on this (and particularly for those who
…[12 more quoted lines elided]…
> "older" COBOLs.)

I thought that there were PC implementations that did not require the
sign all the time.

to be absolutely clear:

PIC 9(6) Packed   = 4 byes in MVS
PIC 9(7) Packed   = 4 bytes in MVS

This is not necessarily true of PC and Unix implementations:

PIC 9(6) Packed   = 3 bytes.
PIC s9(6) Packed  = 4 bytes.
PIC 9(7) Packed   = 4 bytes.  

As far as I understand, I have not really worked in these
environments. This is why there is a tendency to define an odd number
of digits in packed fields (no point wasting a half byte is there).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Reading a Cobol file in C

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W9SS4.49$jC.15062@dfiatx1-snr1.gtei.net>`
- **References:** `<391BE590.91CCDCD7@comit.ie>`

```
Free text and graphics tutorial on COBOL data types:
http://www.flexus.com/softwaredownload.html

Free HTML document to read on ASCII-EBCDIC and IEEE-COBOL datatype
conversions:
http://www.flexus.com/ebd2asc.html

Free Windows (32-bit) DLL to convert COBOL datatypes to IEEE datatypes (what
C uses) and do EBCDIC-ASCII conversions: write to me at address below.
Include one-paragraph summary of the application and a promise to let me
know how it works out.
```

#### ↳ Re: Reading a Cobol file in C

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fhcvj$a1s$1@news.inet.tele.dk>`
- **References:** `<391BE590.91CCDCD7@comit.ie>`

```
For odd length, divide by 2 rounded (2 digits per byte and a half-byte for
the sign).
The answers are 3, 2, 6. You will never see half-bytes.
You can call Merants filehandler from C - look at www.merant.com
Regards
Ib
Carmel Ryan skrev i meddelelsen <391BE590.91CCDCD7@comit.ie>...
>Hello all,
>I'm trying to process a cobol file created on a mainframe (not sure
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Reading a Cobol file in C

- **From:** "The Riddler" <riddler_cubed@nospam.yahoo.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fgquu$cme$1@news.cis.ohio-state.edu>`
- **References:** `<391BE590.91CCDCD7@comit.ie>`

```
With a COMP-3 number, add 1 to the size of the definition, divide by 2 (and
round-up if you have to, in which case there is a leading zero added).

It will only be a full number of bytes.

So it is 3, 2 and 6 bytes. The V takes up no space, it is an implied decimal
place.

The last half-byte will be for a sign (with EBCDIC it will be C for
positive, D for negative and F for unsigned - not sure about ASCII. The 'S'
means you're number is signed). That's why you add 1 before dividing by 2.

"Carmel Ryan" <carmel.ryan@comit.ie> wrote in message
news:391BE590.91CCDCD7@comit.ie...
> Hello all,
> I'm trying to process a cobol file created on a mainframe (not sure
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
