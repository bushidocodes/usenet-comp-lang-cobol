[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need assistance with CICS to HP PCL printer problem

_3 messages · 3 participants · 1999-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Need assistance with CICS to HP PCL printer problem

- **From:** slider_rj@my-dejanews.com
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b51fc$4et$1@nnrp1.dejanews.com>`

```
I need to change my CICS COBOL program to print a document on an HP 4 Plus
Laser.	It currently prints the document on an old IBM 4019 laser.  I removed
the old IBM PCL (hexadecimal) string (which worked fine) and replaced it with
the HP PCL (hexadecimal) string to access the lower paper tray.  It appears
that the HP did not recognize the string or the PCL command was garbled up
somehow as it passed thru CICS---> VTAM (DRS,VPS) ---> HP printer.  The
printer appears to print the PCL string rather than execute the desired
command.

Note:  I'm using PCL found in an HP LaserJect 4Si Printer User's Reference
Manual.  I'm assuming that the HP 4 Plus LaserJet uses the same PCL code. . .
. Right???

The set up I used in my CICS program is as follows:

WS-TRAY    PIC   X(5)   VALUE   X'1B266C3448'     (Lower Tray PCL Hex Code)
WS-TRAY-LENGTH   PIC  S9(04)  COMP VALUE +5

EXEC CICS SEND TEXT
    FROM (WS-TRAY)
    LENGTH(WS_TRAY_LENGTH)
    ACCUM
    PAGING
    RESP (RESPONSE CODE)
END-EXEC.

Any assistance or suggestions as to why the HP PCL string doesn't work would
be greatly appreciated.

Thanks in advance.

Kathy

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Need assistance with CICS to HP PCL printer problem

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36d61c2b.92844609@news1.ibm.net>`
- **References:** `<7b51fc$4et$1@nnrp1.dejanews.com>`

```
On Fri, 26 Feb 1999 02:38:37 GMT, slider_rj@my-dejanews.com wrote:

>I need to change my CICS COBOL program to print a document on an HP 4 Plus
>Laser.	It currently prints the document on an old IBM 4019 laser.  I removed
…[7 more quoted lines elided]…
>

Sounds like the ESC character X"1b" on the PC is being lost.  Can you
check your ASCII/EBCDIC translation to ensure that the proper EBCDIC
character is being used and translated into X"1b" in ascii?
```

##### ↳ ↳ Re: Need assistance with CICS to HP PCL printer problem

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D93AD8.1AC6B38C@zip.com.au>`
- **References:** `<7b51fc$4et$1@nnrp1.dejanews.com> <36d61c2b.92844609@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On Fri, 26 Feb 1999 02:38:37 GMT, slider_rj@my-dejanews.com wrote:
…[14 more quoted lines elided]…
> character is being used and translated into X"1b" in ascii?

Spot on:  ESC character in EBCDIC is Hex 27.  Be careful to use the
character based commands, do not use hex strings.

01 PCL-select-tray.
  10 filler  pic x(01) value x'27'.
  10 filler  pic x(04) value '&l4H'.

ampersand, lowercase l, 4 and Capital H.   I am assuming that the hex
strings were correct.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
