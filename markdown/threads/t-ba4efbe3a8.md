[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for COBOL Datatype Definition

_8 messages · 7 participants · 1998-08_

---

### Looking for COBOL Datatype Definition

- **From:** "michael donner" <ua-author-7121249@usenetarchives.gap>
- **Date:** 1998-08-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35C6C050.47C8@zedat.fu-berlin.de>`

```
Hello

I got a data set description of a client (I am programmer) wich is like:

Field Content Places/Bytes Fieldtype
abc Number x 7/4 P packed(Comp-3)
def Number y 2/2 Numeric

The only additional thing I got from my client is the information
particle
that these fieldtypes are COBOL datatypes.

Because I have no in depth binary desriptions of the data types
"P packed(Comp-3)" and "Numeric" I searched in the net but did not find
anything satisfactory binary description.

Could anybody help me and guide me to a good information source ?

Thank you forward
Michael
```

#### ↳ Re: Looking for COBOL Datatype Definition

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-08-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35C6C050.47C8@zedat.fu-berlin.de>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de>`

```

Michael Donner wrote in message <35C··.@zed··n.de>...
› I got a data set description of a client (I am programmer) wich is like:
› Field   Content         Places/Bytes    Fieldtype
…[4 more quoted lines elided]…
› anything satisfactory binary description.


This has been discussed at great length.
Go to this URL
http://www.dejanews.com/

enter comp-3
and click on search.
```

#### ↳ Re: Looking for COBOL Datatype Definition

- **From:** "ra..." <ua-author-8450795@usenetarchives.gap>
- **Date:** 1998-08-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35C6C050.47C8@zedat.fu-berlin.de>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de>`

```
Any introductory COBOL book would give you these.

Assuming these are mainframe EBCDIC & not some other machine with
ASCII:

abc is nnnnnnns where n's are digits & s is the sign (c or f = +, d =
-)

def is FnFn where n's are digits (if this is an unsigned field)
def is Fnsn where n's are digits & s is the sign (if this is an
unsigned field)
You really need to find out if this is a signed or unsigned numeric
field.

Rae

On Tue, 04 Aug 1998 01:03:28 -0700, Michael Donner
wrote:

› Hello
› 
…[18 more quoted lines elided]…
› 

Rae B. Creedle
Ra··.@roa··i.net

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Old mainframe programmers never die . . .
They just get Warped.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

##### ↳ ↳ Re: Looking for COBOL Datatype Definition

- **From:** "trbl..." <ua-author-17074344@usenetarchives.gap>
- **Date:** 1998-08-04T08:48:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba4efbe3a8-p3@usenetarchives.gap>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de> <gap-ba4efbe3a8-p3@usenetarchives.gap>`

```
abc PIC 9(7) COMP-3 or S9(7) COMP-3 with former more likely since spec did
not indicate sign (sign may or may not be separate, may or may not be an
overstrike, may be on either left or right nibble depending upon the COBOL
used) def PIC 99

(various snips below)
In article <35c··.@new··i.net>,
Ra··.@roa··i.net (Rae B. Creedle) wrote:
› Any introductory COBOL book would give you these.
› Assuming these are mainframe EBCDIC & not some other machine with
…[20 more quoted lines elided]…
› 

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: Looking for COBOL Datatype Definition

- **From:** "timothy klenke" <ua-author-17075211@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<35C6C050.47C8@zedat.fu-berlin.de>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de>`

```
Michael,

I am having a similar problem with finding the definition for COMP-5.
This is a bit harder to find than COMP-3. If you or anyone else could help
me out I would appreciate it.

For COMP-3, it is the same as that Binary Coded Decimal (BCD) system.
Search the net on BCD for more info. Basically it is a hex conversion only
the digits A through F are invalid.

-Timothy Klenke
tim··.@ps··l.com



Michael Donner wrote in message <35C··.@zed··n.de>...
› Hello
› I got a data set description of a client (I am programmer) wich is like:
› Field   Content         Places/Bytes    Fieldtype
› abc     Number x        7/4             P packed(Comp-3)
› def     Number y        2/2             Numeric
```

##### ↳ ↳ Re: Looking for COBOL Datatype Definition

- **From:** "as-..." <ua-author-17074031@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba4efbe3a8-p5@usenetarchives.gap>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de> <gap-ba4efbe3a8-p5@usenetarchives.gap>`

```
Timothy Klenke schrieb:

› Michael,
› 
…[5 more quoted lines elided]…
› 

COMP-5 is the same as BINARY, so the internal representation is like
Integer resp. Word or LongWord (depending on the number of 9'th). In 16
environment a COMP-5 field with the PIC 99 it would be one byte, PIC
9999 is a word (two byte) and PIC 9(8) is a LongWord (four byte). In a
INTEL environment the order is reversed.
```

#### ↳ Re: Looking for COBOL Datatype Definition

- **From:** "timothy klenke" <ua-author-17075211@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p7@usenetarchives.gap>`
- **In-Reply-To:** `<35C6C050.47C8@zedat.fu-berlin.de>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de>`

```
Michael,

I am having similar troubles. I am looking for the datatype definition
for COMP-5. It is a bit harder to find than COMP-3.

As to your question, I believe COMP-3 is the same as Binary Coded
Decimal (BCD). Basically (for an unsigned number) if you have a two digit
number is decimal say 56, this would be converted to one byte. The five is
represented as 0101 and the six as 0110. Put them together and you get
01010110 or 56 in hex. The hex digits A through F are invalid. A four
digit example would be 4930 (decimal) => 0100 1001 0011 0000 (binary) =>
4930 (hex). Search the net for BCD for more info.

-Timothy Klenke
tim··.@ps··l.com


Michael Donner wrote in message <35C··.@zed··n.de>...
› Hello
› I got a data set description of a client (I am programmer) which is like:
› Field   Content         Places/Bytes    Fieldtype
› abc     Number x        7/4             P packed(Comp-3)
› def     Number y        2/2             Numeric
```

##### ↳ ↳ Re: Looking for COBOL Datatype Definition

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba4efbe3a8-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba4efbe3a8-p7@usenetarchives.gap>`
- **References:** `<35C6C050.47C8@zedat.fu-berlin.de> <gap-ba4efbe3a8-p7@usenetarchives.gap>`

```
Timothy Klenke wrote:
›
› Michael,
›
› I am having similar troubles. I am looking for the datatype definition
› for COMP-5. It is a bit harder to find than COMP-3.

Hi Timothy.

In Micro Focus COBOL, at least, COMP-5 means "native order" binary.
Additionally, you can specify the picture in X's rather than 9's to
get that many bytes of storage.

ie:

01 A PIC XX COMP-5.
01 B REDEFINES A.
03 BYTE1 PIC X COMP-5.
03 BYTE2 PIC X COMP-5.

MOVE 256 TO A
DISPLAY BYTE1
DISPLAY BYTE2.

This might print 1, 0 and it might print 0, 1 depending on your
machine architecture. Because of this, properly aligned COMP-5 items
(if in doubt make them 01 levels and the compiler will align them for
you) are the fastest computational items.

You certainly need to use them if you are doing mixed language
programming and whole structures/records are being passed between
COBOL and languages which operate on native-order integers etc.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
