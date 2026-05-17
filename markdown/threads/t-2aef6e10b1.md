[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Where to get COMP3 format definition? (Need to use with C)

_4 messages · 4 participants · 1997-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Where to get COMP3 format definition? (Need to use with C)

- **From:** "timo lappalainen" <ua-author-17071328@usenetarchives.gap>
- **Date:** 1997-02-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<330AF7E9.BBF@utu.fi>`

```

We need to handle COBOL fields directly with C code. I need
COBOL format definitions or C code to convert ex. COMP3 to
string. We probably need other formats later.

Timo Lappalainen
```

#### ↳ Re: Where to get COMP3 format definition? (Need to use with C)

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2aef6e10b1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<330AF7E9.BBF@utu.fi>`
- **References:** `<330AF7E9.BBF@utu.fi>`

```

Timo Lappalainen (lap··.@u··.fi) wrote:
: We need to handle COBOL fields directly with C code. I need
: COBOL format definitions or C code to convert ex. COMP3 to
: string. We probably need other formats later.
: Timo Lappalainen
----------------------------------------------------

COMP-3 consists of two digits per byte except for the right end. It
contains a digit and a sign.

If the value contains an even number of digits then the left-most
digit position in the COMP-3 item is zeroed.

The signs depend on the brand of computer. On IBM mainframes, the
signs are hex a thru f. An item that contains the result of a prev-
ious math operation has a hex c (if positive) or a hex d (if negative).
A hex f sign is considered positive and appears as a result of packing
an EBCDIC item.

Examples:
Value PIC 9(7) COMP-3

2,345,678 23 45 67 8c (or 23 45 67 8f)
-2,345,678 23 45 67 8d
-345,678 03 45 67 8d
1 00 00 00 1c (or 00 00 00 1f)

The PIC definition always contains an odd number of digits.
```

#### ↳ Re: Where to get COMP3 format definition? (Need to use with C)

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2aef6e10b1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<330AF7E9.BBF@utu.fi>`
- **References:** `<330AF7E9.BBF@utu.fi>`

```

We are starting to see a lot of this.

Timo Lappalainen wrote in article
<330··.@u··.fi>...
› We need to handle COBOL fields directly with C code. I need 
› COBOL format definitions or C code to convert ex. COMP3 to 
…[3 more quoted lines elided]…
› 

COMP-3 is not easily converted to a C numeric field. It would be better to
convert that with a COBOL program. Using CA-Realia COBOL on the PC and MF
COBOL on the PC,
PIC S9(4) COMP-5 is the same as an INT in C, and PIC S9(9) COMP-5 is the
same as
a LONG INT. I am different than most in that my experience has been
working on a BBS system written in C, for which I wrote a lot of routines
in COBOL. If converting data stored in what is better termed a MAINFRAME
style rathar than a COBOL style (COMP-3 being packed decimal and not
limited to use in COBOL), I would change it to a display field and use the
C function to move a string to a number (atoi?).
```

#### ↳ Re: Where to get COMP3 format definition? (Need to use with C)

- **From:** "chai..." <ua-author-2228828@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2aef6e10b1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<330AF7E9.BBF@utu.fi>`
- **References:** `<330AF7E9.BBF@utu.fi>`

```

Unfortunately, all the various COMPUTATIONAL field options vary from compiler to compiler. The best place to find out the specific definition is by "reading the manuals." Traditionally, the descriptions of the COMP fields can be difficult to follow. Be patient and take heart, though, if you are persistent the answers will come.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
