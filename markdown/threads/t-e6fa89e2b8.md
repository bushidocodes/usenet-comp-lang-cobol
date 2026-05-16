[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tab delimited

_10 messages · 4 participants · 2002-03_

---

### Tab delimited

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-11T16:02:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ky4j8.159$kH5.904@castor.casema.net>`

```
Anyone an idea to how to read a tab delimited file and fill 3 fields with
the data out off the record?

Situation 1:
          SELECT IMP ASSIGN TO RANDOM, IMP-ACNM
              ORGANIZATION IS LINE SEQUENTIAL
              FILE STATUS IS IMP-STATUS.

       FD  IMP                             LABEL RECORDS ARE STANDARD.
       01  IMP-REC.
           03  IMP-INH                     PIC X(50).

      01  AH-TAB.
           03  TAB-AH                  PIC 9(5) COMP-1 VALUE 2338.
       01  AH-TAB-R REDEFINES AH-TAB.
           03  TABJE                   PIC X.
           03  FILLER                  PIC X.

        UNSTRING IMP-REC DELIMITED BY TABJE INTO  FIELD1  FIELD2 FIELD3.
 due to line sequential there is no tab anymore so just field1 is filled.

Situation 2:
         SELECT IMP ASSIGN TO RANDOM, IMP-ACNM
              ORGANIZATION IS BINARY SEQUENTIAL
              FILE STATUS IS IMP-STATUS.

       FD  IMP                             LABEL RECORDS ARE STANDARD.
       01  IMP-REC.
           03  IMP-INH                     PIC X(50).

      01  AH-TAB.
           03  TAB-AH                  PIC 9(5) COMP-1 VALUE 2338.
       01  AH-TAB-R REDEFINES AH-TAB.
           03  TABJE                   PIC X.
           03  FILLER                  PIC X.

        UNSTRING IMP-REC DELIMITED BY TABJE INTO  FIELD1  FIELD2 FIELD3
works for the first record but due to binary sequential i'm getting too much
data in imp-rec so my second record is corrupted
```

#### ↳ Re: Tab delimited

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-03-11T18:05:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6m6j8.64984$uW4.2140113946@newssvr30.news.prodigy.com>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net>`

```

"ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message
news:Ky4j8.159$kH5.904@castor.casema.net...
> Anyone an idea to how to read a tab delimited file and fill 3 fields with
> the data out off the record?
[snip]
The answer will require knowledge of the compiler you are using...

Best regards,
Tom Morrison
Liant Software Corporation
```

#### ↳ Re: Tab delimited

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-03-11T18:33:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net>`

```
[Ronald replied via private email that this was for RM/COBOL v 6.06.  I am
replying to comp.lang.cobol for the "historical record"]

Ronald:

To eliminate or modify tab stop processing on line sequential files on
RM/COBOL, use a configuration file.  This is described in Chapter 10 of the
User's Guide.

Your configuration file can be built with any text editor.  It should
contain the record:

RUN-SEQ-FILES TAB-STOPS=0

You direct the runtime to process a configuration file using the C option on
the runcobol command.  For example:

runcobol program.cob C=config.txt

On later versions of RM/COBOL, configuration files may be automatically
located by the runtime without the use of the C option.

Best regards,
Tom Morrison
Liant Software Corporation
```

##### ↳ ↳ Re: Tab delimited

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-11T19:45:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4P7j8.244$kH5.1616@castor.casema.net>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com>`

```
Tom,

It still doesn't work with tab-stops on 0.

I'm starting my menu with:
runcobol fmenu -c/usr/cobol/terminfo.ldh
and one of the lines in the terminfo is:
RUN-SEQ-FILES tab-stops=0

         SELECT IMP ASSIGN TO RANDOM, IMP-ACNM
               ORGANIZATION IS LINE SEQUENTIAL
               FILE STATUS IS IMP-STATUS.
ws:
      01  AH-TAB.
           03  TAB-AH                  PIC 9(5) COMP-1 VALUE 2338.
       01  AH-TAB-R REDEFINES AH-TAB.
           03  TABJE                   PIC X.
           03  FILLER                  PIC X.

procedure:
          UNSTRING IMP-REC DELIMITED BY TABJE INTO
               veldje ING-REKNR-VAN-A ING-REKNR-NAAR-A9.
          display veldje            line 10 position 1.
          display ING-REKNR-VAN-A   line 11 position 1.
          display ING-REKNR-NAAR-A9 line 12 position 1.
          display Imp-rec           line 13 position 1.
          accept dummy.

RESULT:
22     10000   1234567  (LINE 10)


22     10000   1234567 (LINE 13)

Regards, Ronald Leenheer
```

###### ↳ ↳ ↳ Re: Tab delimited

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-03-11T20:40:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AC8j8.10689$%94.2397838475@newssvr11.news.prodigy.com>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com> <4P7j8.244$kH5.1616@castor.casema.net>`

```

"ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message
news:4P7j8.244$kH5.1616@castor.casema.net...
> Tom,
>
> It still doesn't work with tab-stops on 0.
 [snip]

Ronald:

I will need more information to diagnose what is happening.

Let us take this to private email, where you can send me a copy of the
configuration file, the IMP file, and the test program you are using.  I
want to get this solved for you as soon as possible, but I need that
additional information.

Thanks,
Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Tab delimited

_(reply depth: 4)_

- **From:** merhottin@aol.com (Merhottin)
- **Date:** 2002-03-11T23:18:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020311181837.05656.00001032@mb-co.aol.com>`
- **References:** `<AC8j8.10689$%94.2397838475@newssvr11.news.prodigy.com>`

```
Its been awhile since I had to read a Tab delimited file, but I use to define
the tab field :

01  TAB-DELIM     PIC X  VALUE X'09'

(I think Tab hex is X'09')

Then:

Read IN-FILE INTO RECORD-HOLD.
UNSTRING RECORD-HOLD DELIMITED BY TAB-DELIM INTO
FIELD-1,
FIELD-2,
FIELD-3,
FIELD-4.

That was with a 16 bit Realia Compiler.  I wouldn't think the compiler would
make a difference, but I may be wrong.  Hope that helps.
```

##### ↳ ↳ Re: Tab delimited

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-11T20:33:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gw8j8.273$kH5.1921@castor.casema.net>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com>`

```
Tom,

It still doesn't work with tab-stops on 0.

at:
RM/COBOL-85 Runtime - Version 6.06.01 for Sun4c OS 5.4 Solaris 2.4.
Configured for 32 users.
Copyright (c) 1985, 1986-1995 by Liant Software Corp.  All rights reserved.

The sun is my main machine. I compiled the program on the sun and ftped it
back to my pc.
And guess what is works with:

RM/COBOL-85 Runtime - Version 6.10.00 for DOS 3.3+.
Configured for 001 user.
Copyright (c) 1985, 1986-1996 by Liant Software Corp.  All rights reserved.
Registration Number: NY-0000-07668-01

Oops found a problem in the sunversion of RM??

Regards, Ronald Leenheer
```

###### ↳ ↳ ↳ Re: Tab delimited

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2002-03-12T02:34:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0203120234.4141cbbc@posting.google.com>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com> <Gw8j8.273$kH5.1921@castor.casema.net>`

```
"ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message news:<Gw8j8.273$kH5.1921@castor.casema.net>...
> Tom,
> 
…[18 more quoted lines elided]…
> Regards, Ronald Leenheer

Since Mr. Morrison is taking care of the problem, probably I shouldn't
be posting this, but what you are trying to do, I've done LOTS of
times.
The main diferences are:
- Normaly I would cicle thru the record eg.:

WS: 01           TAB-CHAR         PIC X VALUE H"09".
    01           S-CURSOR         PIC 9(3).

PROCEDURE:

...
    PARSE-RECORD.
           MOVE 1 TO CURSOR
           INITIALIZE veldje ING-REKNR-VAN-A ING-REKNR-NAAR-A9
           UNSTRING IMP-REC DELIMITED BY TAB-CHAR INTO veldje POINTER
S-CURSOR
           UNSTRING IMP-REC DELIMITED BY TAB-CHAR INTO ING-REKNR-VAN-A
POINTER S-CURSOR
           UNSTRING IMP-REC DELIMITED BY TAB-CHAR INTO
ING-REKNR-NAAR-A9 POINTER S-CURSOR
            .
... proceed with logic

I've done this with various RM/Cobol versions (5, 6 and 7) on Windows,
DOS, Linux, Unix System V, SCO Unix, HP/UX, (but not on Solaris).

regards,
Paulo Vieira
```

###### ↳ ↳ ↳ Re: Tab delimited

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-03-12T14:11:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E0oj8.1348$5H.680379555@newssvr12.news.prodigy.com>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com> <Gw8j8.273$kH5.1921@castor.casema.net>`

```

"ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message
news:Gw8j8.273$kH5.1921@castor.casema.net...
> Tom,
>
> It still doesn't work with tab-stops on 0.
[snip]
> Oops found a problem in the sunversion of RM??

FWIW and FYI

Indeed, Ronald's version (6.0x, about 7 years old) had a regression in this
area that was fixed in the next version.  For other versions of RM/COBOL,
tab-stops=0 in the configuration file works fine.

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Tab delimited

_(reply depth: 4)_

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-12T22:11:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2vj8.312$V52.2580@castor.casema.net>`
- **References:** `<Ky4j8.159$kH5.904@castor.casema.net> <WL6j8.10664$vc1.2385628219@newssvr11.news.prodigy.com> <Gw8j8.273$kH5.1921@castor.casema.net> <E0oj8.1348$5H.680379555@newssvr12.news.prodigy.com>`

```
Tom,

Thanks for the support, my customer will have to swich over to
CSV format ( delimited with a ';')

Regards Ronald Leenheer

"Tom Morrison" <t.morrison@liant.com> schreef in bericht
news:E0oj8.1348$5H.680379555@newssvr12.news.prodigy.com...
>
> "ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message
…[9 more quoted lines elided]…
> Indeed, Ronald's version (6.0x, about 7 years old) had a regression in
this
> area that was fixed in the next version.  For other versions of RM/COBOL,
> tab-stops=0 in the configuration file works fine.
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
