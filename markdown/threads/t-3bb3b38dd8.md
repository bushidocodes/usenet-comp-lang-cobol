[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Page Eject ( using a PC- and HP inkjet printer)

_5 messages · 5 participants · 1998-01_

---

### Page Eject ( using a PC- and HP inkjet printer)

- **From:** "lap..." <ua-author-904956@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34d1f98c.34804326@news.pcpros.net>`

```

Hi:

I am currently learning the COBOL language in College. I have
been trying (unsucessfully) to force a page eject from my HP printer.
NO one seems to know how to do such a simple task. Would anyone out
there be able to help me.
Here's a program that I have been using to write a file to the
printer, and then cause the output file to print and eject. The file
prints (only after I manually hit the printer eject a page button)
-----------------------------------------------------------------------

IDENTIFICATION DIVISION.
PROGRAM-ID. SAMPLE.
AUTHOR. Dave J LaPore.
DATE-COMPILED. 1/27/98.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT EMPLOYEE-DATA-FILE
ASSIGN TO DISK
ORGANIZATION IS LINE SEQUENTIAL.
SELECT PAYROLL-LISTING-FILE
ASSIGN TO PRINTER.
DATA DIVISION.
FILE SECTION.
FD EMPLOYEE-DATA-FILE
RECORD CONTAINS 26 CHARACTERS
LABEL RECORDS ARE STANDARD
VALUE OF FILE-ID IS 'D:¥PCOBWIN¥ZSTORAGE¥Sample.DAT'.
01 EMPLOYEE-RECORD.
05 EMPLOYEE-NAME-IN PIC X(20).
05 HOURS-WORKED-IN PIC 9(2).
05 HOURLY-RATE-IN PIC 99V99.
FD PAYROLL-LISTING-FILE
LABEL RECORDS ARE OMITTED.
01 PRINT-LINE.
05 PIC X(20).
05 NAME-OUT PIC X(20).
05 PIC X(10).
05 HOURS-OUT PIC 9(2).
05 PIC X(8).
05 RATE-OUT PIC 99.99.
05 PIC X(6).
05 WEEKLY-WAGES-OUT PIC 9999.99.
WORKING-STORAGE SECTION.
01 ARE-THERE-MORE-RECORDS PIC XXX VALUE 'YES'.
PROCEDURE DIVISION.
100-MAIN-MODULE.
OPEN INPUT EMPLOYEE-DATA-FILE
OUTPUT PAYROLL-LISTING-FILE.
** This sets laser printer *
** MOVE X'1B45' TO PRINT-LINE.
** WRITE PRINT-LINE.

** THIS TURNS ON TOP MARGIN TO 0 LINES
** MOVE X'1B266B3045' TO PRINT-LINE.
** WRITE PRINT-LINE.

** THIS changes to compressed *
** MOVE X'1B266B3253' TO PRINT-LINE.
** WRITE PRINT-LINE.

** THIS TURNS PERF SKIP OFF *
** MOVE X'1B266C304C' TO PRINT-LINE.
** WRITE PRINT-LINE.

** THIS SETS VMI FOR 66 LINES *
** MOVE X'1B266C372E3237323743' TO PRINT-LINE.
** WRITE PRINT-LINE.

PERFORM UNTIL ARE-THERE-MORE-RECORDS = 'NO '
READ EMPLOYEE-DATA-FILE
AT END
MOVE 'NO ' TO ARE-THERE-MORE-RECORDS
NOT AT END
PERFORM 200-WAGE-ROUTINE
END-READ
END-PERFORM
CLOSE EMPLOYEE-DATA-FILE
PAYROLL-LISTING-FILE.
* EJECT A PAGE.
MOVE X'1B266C304868' TO PRINT-LINE.
WRITE PRINT-LINE.
STOP RUN.


200-WAGE-ROUTINE.
MOVE SPACES TO PRINT-LINE.
MOVE EMPLOYEE-NAME-IN TO NAME-OUT
MOVE HOURS-WORKED-IN TO HOURS-OUT.
MOVE HOURLY-RATE-IN TO RATE-OUT.
MULTIPLY HOURS-WORKED-IN BY HOURLY-RATE-IN
GIVING WEEKLY-WAGES-OUT.
WRITE print-line.
** DISPLAY print-line.
-------------------------------------------------------------------------

Note: I took this line from the net. Hewlett Packerd's web
site. It doesn't work. I get an error with it.

Could anyone offer some sugesstions on how to do this.

Thanks

Dave LaPorte (lap··.@pcp··s.net)
```

#### ↳ Re: Page Eject ( using a PC- and HP inkjet printer)

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bb3b38dd8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34d1f98c.34804326@news.pcpros.net>`
- **References:** `<34d1f98c.34804326@news.pcpros.net>`

```

Dave,

For the last print line of the report you can use:

MOVE x"0C" TO PRINT-LINE.
WRITE PRINT-LINE BEFORE ADVANCING 0.

x"0C" is a CONTROL-L(decimal 12). The famous form feed.

The code above is a better option than:

MOVE SPACES TO PRINT-LINE.
WRITE PRINT-LINE BEFORE ADVANCING PAGE.

because it avoids printing an extra line before the form feed.
This can avoid an extra blank page at the end of a report.

Hope this helps,
Dan Maltes
Applied Systems Technology


Here is the COBOL-85 WRITE statement standard syntax:

The WRITE statement adds a record to a file.

General Format
Format 1

WRITE record-name [ FROM source ]

[ {BEFORE} ADVANCING { number [LINE ] } ]
{AFTER } { [LINES] }
{ PAGE }

[ AT {END-OF-PAGE} statement-1 ]
{EOP }

[ NOT AT {END-OF-PAGE} statement-2 ]
{EOP }

[ END-WRITE ]

Format 2

WRITE record-name [ FROM source ]

[ INVALID KEY statement-1 ]

[ NOT INVALID KEY statement-2 ]

[ END-WRITE ]

Format 3

WRITE record-name [ FROM source ] WITH NO CONTROL

Syntax Rules

1. Record-name is the name of a record associated with a file described in
the File Section of the Data Division. The associated file may not be a
sort file.
2. Source is a data item or literal. It may not share any storage area with
record-name.
3. Number is an integer numeric literal or data item. It must be
nonnegative.
4. Statement-1 and statement-2 are imperative statements.
5. A Format 1 WRITE statement must be associated with a sequential file. A
Format 2 WRITE statement must be associated with a relative or indexed file.

6. The words END-OF-PAGE and EOP are equivalent.
7. If the END-OF-PAGE phrase is used, the file description entry containing
record-name must have a LINAGE clause.
8. The ADVANCING PAGE and END-OF-PAGE phrases cannot both be used in the
same WRITE statement.
9. A Format 3 WRITE statement must be associated with a sequential file.

Dan Maltes
Applied Systems Technology

Dave LaPorte wrote in message <34d··.@new··s.net>...
› Hi:
› 
…[102 more quoted lines elided]…
› Dave LaPorte (lap··.@pcp··s.net)
```

#### ↳ Re: Page Eject ( using a PC- and HP inkjet printer)

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bb3b38dd8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34d1f98c.34804326@news.pcpros.net>`
- **References:** `<34d1f98c.34804326@news.pcpros.net>`

```

Dave LaPorte wrote:

›            CLOSE EMPLOYEE-DATA-FILE
›                  PAYROLL-LISTING-FILE.
›       *    EJECT A PAGE.
›             MOVE X'1B266C304868' TO PRINT-LINE.
›             WRITE PRINT-LINE.

I'm not familiar with this platform, but it would make more sense to
write the page eject code to the printer *before* closing the file.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ Can you solve it before the 28th term:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: Page Eject ( using a PC- and HP inkjet printer)

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bb3b38dd8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34d1f98c.34804326@news.pcpros.net>`
- **References:** `<34d1f98c.34804326@news.pcpros.net>`

```

All of a sudden, lap··.@pcp··s.net (Dave LaPorte) wrote:


›      *    EJECT A PAGE.
›            MOVE X'1B266C304868' TO PRINT-LINE.  
›            WRITE PRINT-LINE.
›           STOP RUN.

Try
MOVE X'0C' to PRINT-LINE.
WRITE PRINT-LINE BEFORE ADVANCING 0 LINES.
STOP RUN.

The x'0c' is a form feed, and writing after advancing 0 lines will
help you avoid writing an extra line, and potentially an extra
page....

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: Page Eject ( using a PC- and HP inkjet printer)

- **From:** "frederick pierz" <ua-author-17072432@usenetarchives.gap>
- **Date:** 1998-01-30T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bb3b38dd8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34d1f98c.34804326@news.pcpros.net>`
- **References:** `<34d1f98c.34804326@news.pcpros.net>`

```

The simplest way to eject a page in cobol is to go to head of form like
this:
MOVE SPACES TO PRINT-LINE.
WRITE PRINT-LINE BEFORE PAGE.
this will finish off the page and go to head of form on the next page.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
