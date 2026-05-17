[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bit Logical Arithmatic in COBOL/2

_3 messages · 3 participants · 1997-02_

---

### Bit Logical Arithmatic in COBOL/2

- **From:** "thakker..." <ua-author-7089904@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e05u6$1qd@tribune.mayo.edu>`

```

I am interested in finding out about testing bit(s) of a pic x(1) item.
Does VS Cobol II of IBM provide instruction(s) to examine bits?

Thanks,

-Bakulesh Thakker
```

#### ↳ Re: Bit Logical Arithmatic in COBOL/2

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-02-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-238bfcdc8b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5e05u6$1qd@tribune.mayo.edu>`
- **References:** `<5e05u6$1qd@tribune.mayo.edu>`

```

Bakulesh Thakker wrote:
› 
› I am interested in finding out about testing bit(s) of a pic x(1) item.
…[4 more quoted lines elided]…
› -Bakulesh Thakker

The answer to your question is No. But if you don't mind doing some tedious
coding it is possible to determine which bits are on. Basically, you must
coerce the byte into a binary number, and then you can play some games with
it.

01 WORK-FIELD.
05 FILLER PIC X(1) VALUE LOW-VALUE.
05 WORK-BYTE PIC X(1) VALUE LOW-VALUE.
01 COMP-FIELD REDEFINES WORK-FIELD PIC S9(4) USAGE IS BINARY.

MOVE BYTE-IN-QUESTION TO WORK-BYTE.

Now at this point you could subtract out powers-of-two. You would probably
want to table them up and loop through them to make it easier. Basically, if
COMP-FIELD is greater than +128, then the left-most bit is ON (subtract 128
and go to the next test) otherwise the bit is OFF. If COMP-FIELD is greater
than +64 the next bit is on, et cetera.

Needless to say, this method is not very portable. But if you really need
to, you can figure out which bits are on. If you need to test bits a lot,
you should build a general routine to expand bits to bytes so you can re-use
it.

Another technique that would work faster (but takes more memory) is to build
a table of 256 entries like this:

01 BIT-TABLE-DATA.
O5 FILLER PIC X(8) VALUE '00000000'.
05 FILLER PIC X(8) VALUE '00000001'.
05 FILLER PIC X(8) VALUE '00000010'.
...
O5 FILLER PIC X(8) VALUE '11111110'.
05 FILLER PIC X(8) VALUE '11111111'.
01 BYTE-TABLE REDEFINES BIT-TABLE-DATA.
O5 BYTE-MAP OCCURS 256 TIMES.
10 BIT-SWITCH OCCURS 8 TIMES PIC X(1).

Now you can MOVE BYTE-IN-QUESTION TO WORK-BYTE then add 1 to WORK-FIELD,
and use work-field as a subscript to get your BYTE-MAP. So if you want to
know if the third bit from the left is on, you can say:

IF BYTE-MAP (WORK-FIELD,3) = '1'

There's more than one way to solve this problem. I'm sure someone else can
post an even slicker way to do it.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: Bit Logical Arithmatic in COBOL/2

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-02-17T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-238bfcdc8b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-238bfcdc8b-p2@usenetarchives.gap>`
- **References:** `<5e05u6$1qd@tribune.mayo.edu> <gap-238bfcdc8b-p2@usenetarchives.gap>`

```

Arnold Trembley wrote:

› Bakulesh Thakker wrote:
›› 
…[5 more quoted lines elided]…
›› -Bakulesh Thakker
 
› The answer to your question is No.  But if you don't mind doing some tedious 
› coding it is possible to determine which bits are on.  Basically, you must 
› coerce the byte into a binary number, and then you can play some games with 
› it.
 
› 01  WORK-FIELD.
›    05  FILLER        PIC X(1) VALUE LOW-VALUE.
›    05  WORK-BYTE     PIC X(1) VALUE LOW-VALUE.
› 01  COMP-FIELD    REDEFINES WORK-FIELD PIC S9(4) USAGE IS BINARY.
 
› MOVE BYTE-IN-QUESTION TO WORK-BYTE.
 
› Now at this point you could subtract out powers-of-two.  You would probably 
› want to table them up and loop through them to make it easier.  Basically, if 
› COMP-FIELD is greater than +128, then the left-most bit is ON (subtract 128 
› and go to the next test) otherwise the bit is OFF.  If COMP-FIELD is greater 
› than +64 the next bit is on, et cetera.
 
› Needless to say, this method is not very portable.  But if you really need 
› to, you can figure out which bits are on.  If you need to test bits a lot, 
› you should build a general routine to expand bits to bytes so you can re-use
› it.
 
› Another technique that would work faster (but takes more memory) is to build 
› a table of 256 entries like this:
 
› 01  BIT-TABLE-DATA.
›    O5  FILLER  PIC X(8) VALUE '00000000'.
…[7 more quoted lines elided]…
›        10   BIT-SWITCH  OCCURS 8 TIMES PIC X(1).
 
› Now you can MOVE BYTE-IN-QUESTION TO WORK-BYTE then add 1 to WORK-FIELD, 
› and use work-field as a subscript to get your BYTE-MAP.  So if you want to 
› know if the third bit from the left is on, you can say:
 
› IF BYTE-MAP (WORK-FIELD,3) = '1'
 
› There's more than one way to solve this problem.  I'm sure someone else can 
› post an even slicker way to do it.
 
› Arnold Trembley
› Software Engineer I (just a job title, still a programmer)
› MasterCard International
› St. Louis, Missouri

While VS COBOL 2 (or even COBOL/370) cannot check at the bit level
without the above ideas, and they are very good; it can use and check
at the hex level:

01 HEX-DATA PIC X(01).
88 HEX-CHECK-ZERO VALUE X"00"
THRU X"0F".
88 HEX-CHECK-THREE VALUE X"30"
THRU X"3F". --- group to check high-order bits.
88 HEX-LOW-CHK-ZERO VALUE X"00"
X"10"
X"20"
...
X"F0". --- you get the idea on checking low-order bits.
88 HEX-LOW-CHK-ONE VALUE X"01"
X"11"
X"21"
...
X"F1".

To check (using the supplied example):

MOVE BYTE-IN-QUESTION TO HEX-DATA
IF HEX-CHECK-THREE
...

You can get fancy and check high- and low-order patterns:

IF HEX-CHECK-THREE
AND HEX-LOW-CHK-ONE
...

Mind you, this is dependent on the collating sequence you're using
(EBCIDIC or ASCII) and the programmer is responsible for establishing
what hex patterns to search for. Hex programming is handy for those
PC COBOL 2 programs that need to display ASCII characters on the
screen what would be hard to do otherwise. Pop quiz, can one perform
hex, or bit, operations in OCTAL?

Just my two cents worth, adjusted for inflation,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
