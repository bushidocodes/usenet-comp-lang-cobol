[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM mainframe COBOLs and TRUNCation

_1 message · 1 participant · 1999-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM mainframe COBOLs and TRUNCation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7oa2gg$cab@dfw-ixnews8.ix.netcom.com>`

```
Given some recent threads, I thought I would show the whole NG 2 quotes
related to IBM mainframe COBOL TRUNC compiler options.  The bottom-line is
that ONLY when you use ANSI/ISO Standard truncation (i.e. believe the
PICTURE clause) can you expect your programs to be portable (even with the
same vendor from release to release).

QUOTE 1:

"MOVE Statement - Binary Value and Display Value

Although the IBM COBOL TRUNC(OPT) compiler option is recommended for
compatibility with the OS/VS COBOL NOTRUNC compiler option, you might
receive different results involving moves of fullword binary items (USAGE
COMP with Picture 9(5) thru Picture 9(9)).

For example:

               WORKING-STORAGE SECTION.
                 01 WK1 USAGE COMP-4 PIC S9(9).
                 .
               PROCEDURE DIVISION.
                 .
                 MOVE 1234567890 to WK1
                 DISPLAY WK1.
                 GOBACK.

This example actually shows invalid COBOL coding, since 10 digits are being
moved into a 9-digit item.

For example, the results are as follows when compiled with the following
compiler options:

                     OS/VS COBOL NOTRUNC        IBM COBOL TRUNC(OPT)
    Binary
    Value         x'499602D2'
x'0DFB38D2'

    Display
    Value         234567890                                     234567890

For OS/VS COBOL, the binary value contained in the binary data item is not
the same as the display value. The display value is based on the number of
digits in the PICTURE clause and the binary value is based on the size of
the binary data item, in this case, 4 bytes. The actual value of the binary
data item in decimal digits is 1234567890.

For IBM COBOL, the binary value and the display value are equal because the
truncation that occurred was based on the number of digits in the PICTURE
clause."

  ***************************************************

QUOTE 2:

"2.3.3.49.1 TRUNC Example 1

        01  BIN-VAR     PIC 99 USAGE BINARY.
              .
            MOVE 123451 to BIN-VAR

                              Decimal                      Hex
Display

    Sender              123451               00|01|E2|3B              123451

    Receiver                    51                   00|33
51
     TRUNC(STD)

    Receiver                -7621                 E2|3B
2J
      TRUNC(OPT)

    Receiver                -7621                 E2|3B
762J
     TRUNC(BIN)


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
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
