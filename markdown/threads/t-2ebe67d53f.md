[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Tutorial, Identification Division

_1 message · 1 participant · 1995-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### COBOL Tutorial, Identification Division

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-02-22T17:28:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1734DCB9E...@LMSC5.IS.LMSC.LOCKHEED.COM>`

```
This is the first posting which is intended to help students learn
COBOL, the language.

We shall begin at the beginning, the IDENTIFICATION DIVISION.

The IDENTIFICATION division has many paragraph entries that have
evolved into comments about the program. Here is a sample ID division:

IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.
AUTHOR. CHRIS MASON.
DATE-WRITTEN. FEBRUARY 22 1995.
DATE-COMPILED.
INSTALLATION. BATTERIES NOT INCLUDED.
SECURITY. THIS IS NOT SECURED.
*REMARKS. DEMO COBOL PROGRAM EXAMPLE 1. HELLO.CBL
* COMMENTS BEGIN BY PUTTING AN ASTERISK IN COLUMN 7.
The paragraph named PROGRAM-ID contains the program name.
It is actually used on many systems as the name the operating system
calls. The author field states the culprit programmer. Date-written
shows when the program was coded. Date-compiled shows up on the listing
from the compiler with the compile date. The installation is your
company name, or an opportunity for a bad pun. Security is yet another
comment field about the secrecy of the source code. Remarks is an
OS/VS (IBM cobol 74) extension that isn't universally supported.
The REMARK entry was intended for some documentation on the program.
It is a good idea to have some comments on the program, and you
can comment out this feature if it isn't supported and continue to use it.
I can't resist codeing enough of the remainder to make the above
a runnable program:
ENVIRONMENT DIVISION.
SOURCE-COMPUTER. IBM.
OBJECT-COMPUTER. IBM.
DATA DIVISION.
FILE SECTION.
WORKING-STORAGE SECTION.
PROCEDURE DIVISION.
A0000-MAIN.
DISPLAY 'HELLO WORLD'.
STOP RUN.
LATER, AND GOOD CODEING!!!


Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
