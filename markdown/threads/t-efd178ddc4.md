[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Do I have a valid date?

_1 message · 1 participant · 1999-01_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Re: Do I have a valid date?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-23T00:00:00
- **Newsgroups:** comp.software.year-2000,alt.cobol,comp.lang.cobol
- **Message-ID:** `<78c1u3$f21@dfw-ixnews9.ix.netcom.com>`
- **References:** `<78adcv$6dd$1@nnrp1.dejanews.com>`

```
Note: The following assumes that from the reference to COBOL and CICS, that
you are running on an IBM mainframe.  I am even writing it for OS/390 or
MVS - but think there are comparable VSE solutions also.

I provided one solution (using the new IBM extension of a DateVal intrinsic
function) to this problem if you have the MLE add-on to COBOL for
this-and-that - but there is another option that you can use - assuming you
have the LE run-time libraries available (this will even work if your
program is compiled with VS COBOL II - I think)

Please see
  http://www2.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/ceea305/3%2e5%2e24
for complete reference material on the CEEDAYS callable routine.

Special notes for those wondering if 01-02-2000 is Jan 2 or Feb 1 - by
"simply" switching the LE VString-PICSTR, you can easily change the mapping
of your input data - without actually having to "reformat" your input.


Given Working-Storage

01  Full-Date-in.
    05   MM-in   Pic 9(02).
    05                Pic X(01) Value "-".
    05   DD-in   Pic 9(02).
    05                 Pic X(01) Value "-".
    05   YY-in     Pic 9(04).

01   LE-Parameters.
    05    Dynamic-Call-Name     Pic X(07)   Value "CEEDAYS".
    05    LILIAN-Date                  PIC S9(9) BINARY.
     05 FC.
                10  Condition-Token-Value.
                COPY  CEEIGZCT.
                    15  Case-1-Condition-ID.
                        20  Severity    PIC S9(4) BINARY.
                        20  Msg-No      PIC S9(4) BINARY.
                    15  Case-2-Condition-ID
                              REDEFINES Case-1-Condition-ID.
                        20  Class-Code  PIC S9(4) BINARY.
                        20  Cause-Code  PIC S9(4) BINARY.
                    15  Case-Sev-Ctl    PIC X.
                    15  Facility-ID     PIC XXX.
                10  I-S-Info            PIC S9(9) BINARY

01    VString-Date-In.
                02  Vstring-length-DI      PIC S9(4) BINARY.
                02  Vstring-text-DI.
                    03  Vstring-char-DI    PIC X
                                OCCURS 0 TO 256 TIMES
                                DEPENDING ON Vstring-length-DI.
01     VString-PICSTR.
                02  Vstring-length-PS      PIC S9(4) BINARY.
                02  Vstring-text-PS.
                    03  Vstring-char-PS    PIC X
                                OCCURS 0 TO 256 TIMES
                                DEPENDING ON Vstring-length-PS.

      ...
Procedure Division.
   ....

    Move 10 to Vstring-length-PS
    Move "MM-DD-YYYY" to Vstring-char-PS
    Move 10 to Vstring-length-DI
    Move Full-Date-In to Vstring-text-DI
    Call Dynamic-Call-Name
          Using     VString-PICSTR
                         VString-Date-In
                        LILIAN-Date
                        FC

*  Note when running under CICS, change the following DISPLAY statements to
*  appropriate CICS commands

          On Exception Display "Are you Certain that you are running under
LE?"
          Not On exception
                If Not CEE000
                    Display "This was an invalid Date"
                Else
                    Display "Date was valid with a Lilian value of "
Lilian-Date
                End-IF
    End-Call
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
