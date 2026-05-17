[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TRUNC - Here a TRUNC; There a TRUNC; Everywhere a TRUNC,TRUNC

_1 message · 1 participant · 1998-03_

---

### TRUNC - Here a TRUNC; There a TRUNC; Everywhere a TRUNC,TRUNC

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f6e4g$t9e@dfw-ixnews6.ix.netcom.com>`

```

If you are not using or interested in an IBM COBOL product, please skip all
of this (you probably have your own truncation problems). This note is
fairly long, so you may want to print it or read it off-line - if it is off
interest to you. It does have some URL references, so you may want to save
it instead.

I have been asked to provide some details on the current - what I call
"NewBOL" COBOL compiler options of TRUNC(OPT), TRUNC(STD), and TRUNC(BIN).
The following applies to all IBM mainframe, OS/2, WindowsNT (but not OS/400)
compilers since VS COBOL II, Release 2.

The following are three quotes from the IBM source material on the
differences between the various TRUNC options. The first two are examples
from the programming guide and the final one is an analysis from a tuning
paper. I have done minor editing to help with newsgroup viewing. Please
see the full IBM documentation for exact details. (If the "tables" don't
show up correctly in your newsgroup viewer, I suggest that you "jump" to the
actual IBM documentation)

>From the Programming Guide, see

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYPG201/2.3.3
..48.1

2.3.3.48.1 TRUNC Example 1

01 BIN-VAR PIC 99 USAGE BINARY.
.
.
MOVE 123451 to BIN-VAR

________________________________________________________________________
| Figure 97. Values of the Data Items after the MOVE
|
|_________________ __________________ _________________
_________________|
| | Decimal | Hex | Display
|

|_________________|__________________|_________________|_________________|
| Sender | 123451 | 00|01|E2|3B | 123451
|

|_________________|__________________|_________________|_________________|
| Receiver | 51 | 00|33 | 51
|
| TRUNC(STD) | | |
|

|_________________|__________________|_________________|_________________|
| Receiver | -7621 | E2|3B | 2J
|
| TRUNC(OPT) | | |
|

|_________________|__________________|_________________|_________________|
| Receiver | -7621 | E2|3B | 762J
|
| TRUNC(BIN) | | |
|

|_________________|__________________|_________________|_________________|


A halfword of storage is allocated for BIN-VAR. The result of this MOVE
statement if the program is compiled with the TRUNC(STD) option is 51; the
field is truncated to conform to the PICTURE clause.
If the program is compiled with the TRUNC(BIN) option, the result of the
MOVE statement is -7621. The reason for the unusual looking answer is that
nonzero high-order digits were truncated. Here, the generated code sequence
would merely move the lower halfword quantity X'E23B' to the receiver.
Because the new truncated value overflowed into the sign bit of the binary
halfword, the value becomes a negative number.

This MOVE statement should not be compiled with the TRUNC(OPT) option
because 123451 has greater precision than the PICTURE clause for BIN-VAR. If
TRUNC(OPT) was used, however, the results again would be -7621. This is
because the best performance was gained by not doing a decimal truncation. "

>From the Programming Guide, see

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYPG201/2.3.3
..48.2

"2.3.3.48.2 TRUNC Example 2

01 BIN-VAR PIC 9(6) USAGE BINARY
.
.
MOVE 1234567891 to BIN-VAR

________________________________________________________________________
| Figure 98. Values of the Data Items after the MOVE
|
|_________________ __________________ _________________
_________________|
| | Decimal | Hex | Display
|

|_________________|__________________|_________________|_________________|
| Sender | 1234567891 | 49|96|02|D3 | 1234567891
|

|_________________|__________________|_________________|_________________|
| Receiver | 567891 | 00|08|AA|53 | 567891
|
| TRUNC(STD) | | |
|

|_________________|__________________|_________________|_________________|
| Receiver | 567891 | 53|AA|08|00 | 567891
|
| TRUNC(OPT) | | |
|

|_________________|__________________|_________________|_________________|
| Receiver | 1234567891 | 49|96|02|D3 | 1234567891
|
| TRUNC(BIN) | | |
|

|_________________|__________________|_________________|_________________|


When TRUNC(STD) is specified, the sending data is truncated to six integer
digits to conform to the PICTURE clause of the BINARY receiver.
When TRUNC(OPT) is specified, the compiler assumes the sending data is not
larger than the PICTURE clause precision of the BINARY receiver. The most
efficient code sequence in this case performed truncation as if TRUNC(STD)
had been specified.

When TRUNC(BIN) is specified, no truncation occurs because all of the
sending data will fit into the binary fullword allocated for BIN-VAR. "

>From the tuning paper, see
http://www.software.ibm.com/ad/cobol/cobpf120.pdf

"TRUNC - BIN, STD, or OPT
When using the TRUNC(BIN) compiler option, all binary (COMP) sending fields
are treated as either
halfword, fullword, or doubleword values, depending on the PICTURE clause,
and code is generated to
truncate all binary receiving fields to the corresponding halfword,
fullword, or doubleword boundary (base 2
truncation). The full content of the field is significant. This can add a
significant amount of degradation
since typically some data conversions must be done, which may require the
use of some library subroutines.
BIN is usually the slowest of the three sub options for TRUNC.
When using the TRUNC(STD) compiler option, the final intermediate result of
an arithmetic expression, or
the sending field in the MOVE statement, is truncated to the number of
digits in the PICTURE clause of
the binary (COMP) receiving field (base 10 truncation). This can add a
significant amount of degradation
since typically the number is divided by some power of ten (depending on the
number of digits in the
PICTURE clause) and the remainder is used; a divide instruction is one of
the more expensive instructions.
| TRUNC(STD) behaves the same was as TRUNC in OS/VS COBOL.
However, with TRUNC(OPT), the compiler assumes that the data conforms to the
PICTURE and USAGE
specifications and manipulates the result based on the size of the field in
storage (halfword, fullword or
| doubleword). TRUNC(OPT) behaves the same was as NOTRUNC in OS/VS COBOL.
TRUNC(STD) conforms to the ANSI and SAA standards, whereas TRUNC(BIN) and
TRUNC(OPT) do
not. TRUNC(OPT) is provided as a performance tuning option and should be
used only when the data in
the application program conforms to the PICTURE and USAGE specifications.
For performance sensitive
applications, the use of TRUNC(OPT) is recommended when possible.
Performance considerations using TRUNC:
| On the average, TRUNC(OPT) was 27% faster than TRUNC(BIN), with a range of
92% faster to
| equivalent.
| On the average, TRUNC(STD) was 26% faster than TRUNC(BIN), with a range of
88% faster to
| equivalent.
| On the average, TRUNC(OPT) was 5% faster than TRUNC(STD), with a range of
49% faster to
| equivalent.
|(COB PG: pp 278-280, 431, 464)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
