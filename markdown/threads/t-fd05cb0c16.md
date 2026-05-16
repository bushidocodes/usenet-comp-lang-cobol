[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling subprogram

_6 messages · 6 participants · 2000-04 → 2000-05_

---

### Calling subprogram

- **From:** stang93gt@hotmail.com
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e3g0q$e2i$1@nnrp1.deja.com>`

```
I am attempting to call a subprogram from my main program. I keep
getting an error saying the subprogram is not in the current drive or
directory. I have tried putting the subprogram in both the C and A
drives. The PROGRAM-ID of the subprogram is SALESTAB. I am using the
Personal Microfocus. Any help would be appreciated. I have included
partial coding:



ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT CUST-ORDER-FILE  ASSIGN TO 'A:ORDER.DAT'.
           SELECT SALES-REPORT     ASSIGN TO 'A:SALESREP.DAT'.

       DATA DIVISION.

       FILE SECTION.
       FD  CUST-ORDER-FILE     RECORD CONTAINS 11 CHARACTERS
                               BLOCK CONTAINS 10 RECORDS.
       01  CUST-ORDER-RECORD   PIC X(11).

       FD  SALES-REPORT.
       01  REPORT-LINE-1       PIC X(132)  VALUE SPACES.

       WORKING-STORAGE SECTION.

       01  WS-SWITCH.
           05  EOF                     PIC X   VALUE 'N'.

       01  CUST-ORDER-RECORD-IN.
           05  ORDER-NUM-IN            PIC X(4).
           05  ORDER-WEIGHT-IN         PIC 9(5).
           05  SHIP-DIST-IN            PIC X.
           05  CLASS-IN                PIC X.

       PROCEDURE DIVISION.

       100-MAIN-ROUTINE.
           OPEN INPUT CUST-ORDER-FILE
                OUTPUT SALES-REPORT
           CALL 'SALESTAB'
           READ CUST-ORDER-FILE INTO CUST-ORDER-RECORD-IN
               AT END MOVE 'Y' TO EOF
           END-READ
           PERFORM 200-VALIDITY-CHECK
               UNTIL EOF IS EQUAL TO 'Y'
           CLOSE CUST-ORDER-FILE
                 SALES-REPORT
           GOBACK.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Calling subprogram

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000425100107.09031.00001240@nso-cc.aol.com>`
- **References:** `<8e3g0q$e2i$1@nnrp1.deja.com>`

```
In article <8e3g0q$e2i$1@nnrp1.deja.com>, stang93gt@hotmail.com writes:

>
>I am attempting to call a subprogram from my main program. I keep
…[5 more quoted lines elided]…
>

Have you checked the placement of the SALESTAB.DLL sub-program?
It must be in a directory that is on your search path.   The easiest placement
is in the same directory as the executable.
```

#### ↳ Re: Calling subprogram

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8w7O4.9023$A75.1865193@news1.mco>`
- **References:** `<8e3g0q$e2i$1@nnrp1.deja.com>`

```
Just before you execute the program if in dos batch mode,
execute following
'PATH >\oldpath.bat'
'PATH=%PATH%;(my new path to called module)'
run program
'OLDPATH.BAT'

<stang93gt@hotmail.com> wrote in message news:8e3g0q$e2i$1@nnrp1.deja.com...
> I am attempting to call a subprogram from my main program. I keep
> getting an error saying the subprogram is not in the current drive or
…[51 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Calling subprogram

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eb742$ddl$1@news.inet.tele.dk>`
- **References:** `<8e3g0q$e2i$1@nnrp1.deja.com>`

```
Enter ".;" (dot semicolon) in front of your path. Then your current
directory is always "in the path".
Regards
Ib
stang93gt@hotmail.com skrev i meddelelsen <8e3g0q$e2i$1@nnrp1.deja.com>...
>I am attempting to call a subprogram from my main program. I keep
>getting an error saying the subprogram is not in the current drive or
…[51 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Calling subprogram

- **From:** "Simon R Hart" <s.hart@mdfs.co.uk>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ejpij$aqt$1@neptunium.btinternet.com>`
- **References:** `<8e3g0q$e2i$1@nnrp1.deja.com> <8eb742$ddl$1@news.inet.tele.dk>`

```

Ib Tanding wrote in message <8eb742$ddl$1@news.inet.tele.dk>...
>Enter ".;" (dot semicolon) in front of your path. Then your current
>directory is always "in the path".
>Regards
>Ib


Useful tip lb, I did'nt know that!

Simon.

>stang93gt@hotmail.com skrev i meddelelsen <8e3g0q$e2i$1@nnrp1.deja.com>...
>>I am attempting to call a subprogram from my main program. I keep
…[54 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Calling subprogram

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_4rR4.2483$XK.5712@news.swbell.net>`
- **References:** `<8e3g0q$e2i$1@nnrp1.deja.com> <8eb742$ddl$1@news.inet.tele.dk> <8ejpij$aqt$1@neptunium.btinternet.com>`

```
And dot-dot is the parent directory of the one you're in. And
dot-dot-dot is the grandparent. and so on.
For example, the following (DOS) commands:

CD dot-dot, and
CD dot-dot-dot

work as expected.

Simon R Hart <s.hart@mdfs.co.uk> wrote in message
news:8ejpij$aqt$1@neptunium.btinternet.com...
>
> Ib Tanding wrote in message <8eb742$ddl$1@news.inet.tele.dk>...
…[10 more quoted lines elided]…
> >stang93gt@hotmail.com skrev i meddelelsen
<8e3g0q$e2i$1@nnrp1.deja.com>...
> >>I am attempting to call a subprogram from my main program. I keep
> >>getting an error saying the subprogram is not in the current drive
or
> >>directory. I have tried putting the subprogram in both the C and A
> >>drives. The PROGRAM-ID of the subprogram is SALESTAB. I am using
the
> >>Personal Microfocus. Any help would be appreciated. I have
included
> >>partial coding:
> >>
…[51 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
