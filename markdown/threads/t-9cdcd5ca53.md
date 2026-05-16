[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-3 fields with Fujitsu Cobol 6.1

_6 messages · 5 participants · 2003-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### COMP-3 fields with Fujitsu Cobol 6.1

- **From:** "Giorgio" <gcoli@hotmail.com>
- **Date:** 2003-03-13T16:04:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4q6bg$ski$1@fata.cs.interbusiness.it>`

```
Hi,
I'm not able to resolve this:
I have a file with several fields correctly defined USAGE COMP-3, but when I
read this file, the values of the fields are all wrong.
When I see the output of the DISPLAY statement the values are not correct,
even if the values in the file are (hex):
01 23 4C 98 76 5C 0D 0A
The output of the DISPLAY statement shows correctly only the first 2 bytes
of the first field and then wrong data.
I'm using Fujitsu Cobol 6.1 on Windows 2000 Professional.
Somebody can help me?

I put here the program:

       ID DIVISION.
       PROGRAM-ID.  XTEST.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FILEIN
           ASSIGN        TO    FILE001
           ORGANIZATION IS    LINE SEQUENTIAL.
      *
       DATA DIVISION.
       FILE SECTION.
       FD  FILEIN
       01  P91CS100-REC       PIC X(6).
      *
       WORKING-STORAGE SECTION.
      *
       01  P91CS100-REC-X.
           10 P91CS100-0010       PIC S9(5) USAGE COMP-3.
           10 P91CS100-1054       PIC S9(5) USAGE COMP-3.
       01  CTR-IN     PIC 9(3) VALUE ZERO.
       01  FF-IN      PIC X    VALUE "N".
      *------------------*
       PROCEDURE DIVISION.
      *------------------*
       ML-010.
           DISPLAY "PROGRAM XTEST".
       ML-020.
           OPEN INPUT FILEIN.
           DISPLAY "FILE OPEN".
       ML-050.
           READ FILEIN INTO P91CS100-REC-X
              AT END MOVE "Y" TO FF-IN.
           ADD 1 TO CTR-IN.
           DISPLAY 'NELLA-PERFORM-ML-050'.
           DISPLAY 'P91CS100-0010 = ' P91CS100-0010.
           DISPLAY 'P91CS100-1054 = ' P91CS100-1054.
       ML-060.
           READ FILEIN  INTO P91CS100-REC-X
              AT END MOVE "Y" TO FF-IN.
           DISPLAY 'P91CS100-0010 = ' P91CS100-0010.
           DISPLAY 'P91CS100-1054 = ' P91CS100-1054.
           IF FF-IN NOT = "S"
              ADD 1 TO CTR-IN
              GO TO ML-060.
       ML-080.
           DISPLAY "RECORDS N.   " CTR-IN.
           CLOSE FILEIN.
           DISPLAY "FILE CLOSED".
           DISPLAY "END XTEST".
           MOVE ZERO TO RETURN-CODE.
       ML-100.
           GOBACK.
```

#### ↳ Re: COMP-3 fields with Fujitsu Cobol 6.1

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-13T10:15:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C0ednZR54cJeMu2jXTWckw@giganews.com>`
- **References:** `<b4q6bg$ski$1@fata.cs.interbusiness.it>`

```

"Giorgio" <gcoli@hotmail.com> wrote in message
news:b4q6bg$ski$1@fata.cs.interbusiness.it...
> Hi,
> I'm not able to resolve this:
> I have a file with several fields correctly defined USAGE COMP-3, but when
I
> read this file, the values of the fields are all wrong.
> When I see the output of the DISPLAY statement the values are not correct,
…[60 more quoted lines elided]…
>            GOBACK.

Assuming your goal is to display the values correctly---

Move the COMP-3 items to a display field before displaying and see what
happens:

01  EDIT-6   PIC -----9.

MOVE P91CS100-0010 TO EDIT-6.
DISPLAY 'P91CS100-0010= ' EDIT-6.

Hint: You'll be better off in the long run if you cultivate the habit of
using display fields for external media, that is, don't define file fields
as anything other than display (no COMP-3, BINARY, COMP-5, etc.).
```

##### ↳ ↳ Re: COMP-3 fields with Fujitsu Cobol 6.1

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-03-13T17:36:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4qc12$cn1$1@reader11.wxs.nl>`
- **References:** `<b4q6bg$ski$1@fata.cs.interbusiness.it> <C0ednZR54cJeMu2jXTWckw@giganews.com>`

```
Been struggling with the same thing when I started out with Fujitsu. I can
only agree with Jerry. Steer clear of comp-3 and comp-6 declarations and
you'll have no trouble at all. When explicitly naming the SIGN TRAILING
SEPARATE in fields like S9(09)v99 you even have a file system compatible
with RM/Cobol (version 0 not 2!).

"JerryMouse" <nospam@bisusa.com> schreef in bericht
news:C0ednZR54cJeMu2jXTWckw@giganews.com...
>
> "Giorgio" <gcoli@hotmail.com> wrote in message
…[3 more quoted lines elided]…
> > I have a file with several fields correctly defined USAGE COMP-3, but
when
> I
> > read this file, the values of the fields are all wrong.
> > When I see the output of the DISPLAY statement the values are not
correct,
> > even if the values in the file are (hex):
> > 01 23 4C 98 76 5C 0D 0A
> > The output of the DISPLAY statement shows correctly only the first 2
bytes
> > of the first field and then wrong data.
> > I'm using Fujitsu Cobol 6.1 on Windows 2000 Professional.
…[71 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COMP-3 fields with Fujitsu Cobol 6.1

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e711b0c.314205584@news.optonline.net>`
- **References:** `<b4q6bg$ski$1@fata.cs.interbusiness.it> <C0ednZR54cJeMu2jXTWckw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>Hint: You'll be better off in the long run if you cultivate the habit of
>using display fields for external media, that is, don't define file fields
>as anything other than display (no COMP-3, BINARY, COMP-5, etc.).

It is refresning to see a voice of reason in CLC. You got that one right.
```

#### ↳ Re: COMP-3 fields with Fujitsu Cobol 6.1

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-14T06:02:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303140602.bdf8786@posting.google.com>`
- **References:** `<b4q6bg$ski$1@fata.cs.interbusiness.it>`

```
Contrary to other follow up postings - there is absolutely nothing
wrong with the Fujitsu implementation of COMP-3 - which in Fujitsu is
Packed Decimal.  I use this data type for transport of data between
MicroFocus COBOL programs on the PC, Fujitsu COBOL programs on the PC
and data from and to an IBM Mainframe.  The implementation is
identical.

The PROBLEM here is writing the data to a LINE SEQUENTIAL file.  The
data values < X"20" are going to get dropped, compressed, etc.  Change
your definition to SEQUENTIAL and add two bytes to the record, where
you place X"0D0A" and I think you will find your problem of data
representation in the file will go away.

Now - as to the OTHER advice here to steer clear - I fully agree 100%
- use Usage Display with Sign Separate for external data over which
you have control.


"Giorgio" <gcoli@hotmail.com> wrote in message news:<b4q6bg$ski$1@fata.cs.interbusiness.it>...
> Hi,
> I'm not able to resolve this:
…[63 more quoted lines elided]…
>            GOBACK.
```

##### ↳ ↳ Re: COMP-3 fields with Fujitsu Cobol 6.1

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-14T11:42:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<haScnYlko4Efj--jXTWcig@giganews.com>`
- **References:** `<b4q6bg$ski$1@fata.cs.interbusiness.it> <bfdfc3e8.0303140602.bdf8786@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com>
>
> The PROBLEM here is writing the data to a LINE SEQUENTIAL file.  The
…[4 more quoted lines elided]…
>

Good catch. But I don't think Fujitsu is the one dropping, compressing, or
mashing on the data. Fujitsu configures and composes the data correctly but
the PRINTER (or screen driver) is going nuts.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
