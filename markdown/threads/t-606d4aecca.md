[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convert COBOL to COBOL II

_2 messages · 2 participants · 1997-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Convert COBOL to COBOL II

- **From:** "casey..." <ua-author-994183@usenetarchives.gap>
- **Date:** 1997-02-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970218035100.WAA27386@ladder01.news.aol.com>`

```

Hi COBOL Experts,

I am in the process of converting a COBOL program to COBOL II that has
report writer code in it. I wanted to know a few things: (1). Is there
a document containing the changes made from COBOL to COBOL II?; (2). I
have removed the RD code (commented out) and replaced it with FD in the
linkage section, but does it require more work than this? ; (3). I will
change generate to WRITE statements.; (4) I have COLUMN commands that I
will change to FILLERs. Last, do you have any tips on removing report
write code and replacing it with FD linkage section code? (conforming to
the COBOL II standard).

Thanks, Casey.

Here is an abstract of the source code in question:

[It is in withe LINKAGE section of the source code.
You will notice the original code commented out (*).
I have made the following changes: ]

*REPORT SECTION.
005710 *RD ACDEL-COMB

005720 * CONTROLS ARE FINAL
005730 * PAGE LIMIT IS 66 LINES, FIRST DETAIL 19, LAST DETAIL 62

005740 * FOOTING 64.

005750 FD R-ACDEL-COMB
005760 BLOCK CONTAINS 0 RECORDS
005770 RECORD CONTAINS 136 CHARACTERS
005780 LINKAGE IS 66 LINES
005790 WITH FOOTING AT 64
005800 LINES AT TOP MARGIN 19
005810 LINES AT BOTTOM MARGIN 62.
005820 01 TYPE PAGE HEADING.
005830 02 LINE PLUS 5.
005840 03 COLUMN 11 PIC X(2) SOURCE RTN-MO.
005850 03 COLUMN 15 PIC X(2) SOURCE RTN-YR.
005860 03 COLUMN 18 PIC X(3) SOURCE RTN-PDC.
005870 03 COLUMN 58 PIC X(8) SOURCE
005880 RTN-SHIP-TO-ACCT.
005890 03 COLUMN 68 PIC X(2) SOURCE RTN-RGN.

Computer Consultant: FoxPro 2.6 for Windows, MSC++ 7.0a SDK, Visual BASIC, COBOL-85, and others. INET: cas··.@a··.com
```

#### ↳ Re: Convert COBOL to COBOL II

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1997-02-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-606d4aecca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970218035100.WAA27386@ladder01.news.aol.com>`
- **References:** `<19970218035100.WAA27386@ladder01.news.aol.com>`

```

cas··.@a··.com (Casey99298) wrote:

› Hi COBOL Experts,
 
› I am in the process of converting a COBOL program to COBOL II that has
› report writer code in it.  I wanted to know a few things: 
 
› (1).  Is there
› a document containing the changes made from COBOL to COBOL II?;

You probably won't have to make a lot of changes. Some changes you
won't have to make but will eventually want to. Such as replacing
some massive IF Stmts with the Evaluate verb, or initialization
routines with the Initialize verb.

Heres the list of dropped verbs:

Identification Division
Remarks (use * or / in column 7)

Environment Division
Processing mode clause

Procedure Division
READY TRACE
NOTE
EXHIBIT (use DISPLAY)
EXAMINE (use INSPECT)
CURRENT-DATE (use ACCEPT WS-DATE FROM DATE)
TIME-OF-DAY (use ACCEPT WS-TIME FROM TIME)
TRANSFORM (use INSPECT)
ON statement (use IF...ELSE or EVALUATE)
Write after/before positioning (use just 'WRITE' , drop positioning.

Additions in Cobol II

Scope terminators for verbs:
END-ADD, END-CALL, END-COMPUTE, END-DIVIDE, END-EVALUATE, END-IF,
END-MULTIPLY, END-PERFORM, END-READ, END-SEARCH

CONTINUE verb use instead of NEXT SENTENCE
NEXT SENTENCE means go to next period
CONTINUE means go to the next scope terminator

INITIALIZE
Will whole copybooks and fields with cascading levels to spaces or
numerics depending on PIC value.

EVALUATE
Uses case structure to replace the use of massive
IF...ELSE...IF....ELSE statements.

There is more, and variations of the above additions and deletions,
along with a few feature changes, and a few inconsistencies between
Cobol and Cobol II, but this will get you going.

› (2). I
› have removed the RD code (commented out) and replaced it with FD in the
› linkage section, but does it require more work than this? ;

I've successfully avoided coding report writer. Creating strait
sysout reports, you must have your FD defined in the Data Division.
It probably already is. You probably just need to delete the REPORT
IS R-ACDEL-COMB stmt.

Delete REPORT-SECTION, get rid of all control breaks, TYPE IS, and
line indicators. Put what's left into working storage. You should
have 01 level's for each header line and sub headers and an 01 level
for the detail line. You might also need an 01 level for totals.
Each 01 level should have a cascade of lower levels with fields that
defines how each line looks. Make each line 132 positions long in
w/s. And change your FD in the Data Division to:
01 RPT-REC.
05 RPT-CC PIC X.
05 RPT-LINE PIC X(132).

› (3). I will change generate to WRITE statements.;

You will need to do more that just this. A WRITE stmt will write to
sysout what is in the 01 level that you state, but now you have to
move values to all of those fields under each 01 level. The SOURCE
stmt in the REPORT SECTION won't work. Then, move your w/s line to
RPT-LINE and WRITE RPT-REC AFTER 1 LINES. Or 2 LINES for double
spacing.

You will also need a counter for detail lines written, so that when
the counter reaches the maximum lines per page (you define, usually 55
to 60), you will perform a header routine, and reset the counter to 0.

Any totals, you have to accumulate.


TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
