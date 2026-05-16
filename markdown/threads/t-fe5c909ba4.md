[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL and Unicode

_1 message · 1 participant · 2006-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL and Unicode

- **From:** sgbojo@gmail.com
- **Date:** 2006-09-18T13:57:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1158613037.010214.9470@e3g2000cwe.googlegroups.com>`

```
I have an example of COBOL from IBM dealing with national data. I am
inexperienced when dealing with the IBM compiler on Aix 5L 5.2.

I am using this command line:
cob CODEPAGE=00037 ibm1.cbl

I recieve this error: Function argument must be between 1 and collating
sequence length

Here is my program:
       IDENTIFICATION DIVISION.
       PROGRAM-ID.                      ibm1.
       INSTALLATION.                    comment-entry.
       DATE-WRITTEN.                    1999/XX/XX - 99:99:99.
       DATE-COMPILED.                   1999/XX/XX - 00:00:00.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER.                 computer-name.
       OBJECT-COMPUTER.                 computer-name.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 Chinese-EBCDIC pic X(16) value 'Chinese text'.
       01 Chinese-GB18030-String pic X(16).
       01 UnicodeString pic N(14).
       PROCEDURE DIVISION.
       Main Section.
           Move function National-of(Chinese-EBCDIC, 1388)
                to UnicodeString.
           Move function Display-of(UnicodeString, 1388)
                to Chinese-GB18030-String.
           Exit Program.
           Stop Run.

Suggestions welcomed. Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
