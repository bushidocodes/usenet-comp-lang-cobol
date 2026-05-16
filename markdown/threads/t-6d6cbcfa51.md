[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# zcobol - first COBOL compiler supporting ANSI/ISO 754 Decimal Floating Point

_1 message · 1 participant · 2009-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### zcobol - first COBOL compiler supporting ANSI/ISO 754 Decimal Floating Point

- **From:** "don@higgins.net" <don@higgins.net>
- **Date:** 2009-04-14T05:28:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f37da7d7-75fc-4e01-9327-636a8505097e@e37g2000vbe.googlegroups.com>`

```
zcobol v1.5.00b now supports ANSI/ISO 754 Decimal Floating Point (DFP)
plus ANSI/ISO 754 Binary Floating Point (BFP) .

zcobol supports the new explicit COBOL USAGE types defined in the
draft COBOL 2008 standard: FLOAT-DECIMAL-7, FLOAT-DECIMAL-16, FLOAT-
DECIMAL-34, FLOAT-BINARY-7, FLOAT-BINARY-16, FLOAT-BINARY-34.  In
addition the IBM mainframe default standard Hexadecimal Floating Point
(HFP) is supported using FLOAT-HEX-7, FLOAT-HEX-15, and FLOAT-HEX-30.
The COBOL 2002 standard generic floating point usage types FLOAT-
SHORT, FLOAT-LONG, and FLOAT-EXTENDED default to DFP, but can be
reassigned to any of the 3 types using zcobol option FLOAT(HEX), FLOAT
(BINARY), or the default FLOAT(DECIMAL).  The default for COMP-1 and
COMP-2 in zcobol is HFP for IBM mainframe compatibility.

In addition to the floating point extended data types, zcobol now also
supports the following COMP fields: half word S9(4), full word S9(9),
double word S9(18), and quad word S9(39) and also packed decimal and
zoned decimal up to S9(31).

The zcobol verbs MOVE, ADD, SUBTRACT, MULTIPLY, DIVIDE, IF, and
DISPLAY support the above data types in any combination.  zcobol
generates HLASM IBM mainframe compatible code which can be run at
native speed on IBM z9/z10 mainframes or the code can be compiled,
linked, and executed on any J2SE platform including Windows and Linux
using z390.  The InstallShield download for z390 and zcobol which is
open source is available on www.z390.org.  For more information on
zcobol visit www.zcobol.org.  The download includes demos and new
regression tests for the new data types.  The demo zcobol\demo
\powers.cbl displays powers of 2 up to 126 using the new COMP S9(39)
128 bit integer support.  The 3 regression tests zcobol\test
\TESTHFP1.CBL, TESTBFP1, and TESTDFP1 using FLOAT(HEX), FLOAT(BINARY),
and the default FLOAT(DECIMAL) respectively illustrate the new
floating point code generation and execution capabilities.

Finally you can define a decimal floating point fraction such as 0.1
in COBOL and have it result in exactly 0.1000000 using DFP short
versus 0.09999999 for HFP or BFP short due to irrational result in
base 2 versus base 10.

Don Higgins
Don@higgins.net
Don-Higgins.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
