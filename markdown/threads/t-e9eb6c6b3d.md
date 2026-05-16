[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# newbie needs to learn

_2 messages · 2 participants · 2006-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### newbie needs to learn

- **From:** "bd2bowl" <davisb@njit.edu>
- **Date:** 2006-01-20T16:50:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1137804605.191847.293490@z14g2000cwz.googlegroups.com>`

```
How do I convert this compressed ascii format to straight ascii?
I need to put in new layout. Both are prvided below.
I am really new ... take me slow.


NEW LAYOUT

HEADER RECORD
1-20	RECONCILIATIONHEADER (literal)			20
21-24	BANK NUMBER (0075)				 4
25-37	ACCOUNT NUMBER					13
38-49	TOTAL DOLLAR (without decimal)			12
50-54	TOTAL ITEM COUNT OF FILE		 05
55-150	FILLER						96

DETAIL RECORD
01-13	ACCOUNT NUMBER					13
14-23	CHECK NUMBER					10
24-33	CHECK AMOUNT 					10
34-41	ISSUE DATE (YYYYMMDD)				 8
42	VOID INDICATOR					 1
43-72	FILLER (not applicable)				30
73-80	FILLER						 8
81-130  PAYYEE NAME (from VCFILE)			50
131-150 FILLER						20

----------------------------------------------------------------------------------------------------------------------

FD  RECON-TAPE   RECORD CONTAINS 46 CHARACTERS
                 LABEL RECORDS ARE STANDARD
                 DATA RECORD IS RECON-RECORD.
01  RECON-RECORD.
    04  RECON-BANK-NO       PIC S99       COMP-3.
    04  RECON-BATCH-NO      PIC S9999     COMP-3.
    04  RECON-TP-ACCT-NO    PIC S9(13)    COMP-3.
    04  RECON-TP-CHEK-NO    PIC S9(8)     COMP-3.
    04  RECON-TP-CHEK-AMT   PIC S9(9)V99  COMP-3.
    04  RECON-TP-DATE       PIC 9(6)      COMP-3.
    04  RECON-MISC-DATA     PIC X(19).
*
FD  APCHK-FILE   RECORD CONTAINS 60 CHARACTERS
                 LABEL RECORDS ARE STANDARD
                 DATA RECORD IS VC-RECORD.
01  VC-RECORD.
    03  VC-KEY.
        05  VC-BANK                 PIC X(02).
        05  VC-CHECK-NO             PIC X(06).
    03  VC-DROP                     PIC X(01).
    03  VC-VOID                     PIC X(01).
    03  VC-VENDOR-NO                PIC X(11).
    03  VC-DATE-PAID-CC             PIC 9(02).
    03  VC-DATE-PAID                PIC 9(06).
    03  VC-AMOUNT                   PIC S9(11)V99    COMP-3.
    03  FILLER                      PIC X(08).
    03  VC-CC                       PIC X(02).
    03  FILLER                      PIC X(14).
*
SD  SORT-FILE          RECORD CONTAINS 46 CHARACTERS
                       DATA RECORD IS SORT-RECORD.
01  SORT-RECORD.
    04  SRT-BANKNO     PIC S999       COMP-3.
    04  SRT-BATCHNO    PIC S9999      COMP-3.
    04  SRT-ACCTNO     PIC S9(13)     COMP-3.
    04  SRT-CHEKNO     PIC S9(8)      COMP-3.
    04  SRT-CHEKAMT    PIC S9(9)V99   COMP-3.
    04  SRT-CHEK-DATE  PIC S9999999   COMP-3.
    04  SRT-VENDOR-NO  PIC X(11).
    04  SRT-VOID-DROP  PIC X(05).
    04  SRT-FILLER     PIC X(03).
```

#### ↳ Re: newbie needs to learn

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-21T01:16:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dqs20o$6ht$1@reader2.panix.com>`
- **References:** `<1137804605.191847.293490@z14g2000cwz.googlegroups.com>`

```
[posted and emailed]

In article <1137804605.191847.293490@z14g2000cwz.googlegroups.com>,
bd2bowl <davisb@njit.edu> wrote:
>How do I convert this compressed ascii format to straight ascii?

Either by writing the code yourself or paying someone who knows what they 
are doing to do so... isn't that simple?

>I need to put in new layout.

Now you're in trouble... a lot of people who do it, or so I am told, don't 
'need to', they just do it for fun.

>Both are prvided below.
>I am really new ... take me slow.

No problem... please post the code you have already attempted to use to 
perform this task that hasn't worked and I'm sure someone will take it 
from there.

(you didn't expect someone to just jump up and Do Your Job, did you?)

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
