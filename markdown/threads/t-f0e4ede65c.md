[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Seeking control break example

_6 messages · 5 participants · 1997-11_

---

### Seeking control break example

- **From:** "tmuel..." <ua-author-17071609@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64drbn$qd4$1@news.campus.mci.net>`

```

I am a beginning COBOL student and could use some help. I have an assignment
to write a program with 3 control breaks, totals at each break and a final
total. Can anyone point me to someplace where I could find an example, code
or pseudocode, of this type of program?
```

#### ↳ Re: Seeking control break example

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e4ede65c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<64drbn$qd4$1@news.campus.mci.net>`
- **References:** `<64drbn$qd4$1@news.campus.mci.net>`

```

Tim Mueller wrote:
› I am a beginning COBOL student and could use some help.  I  have an
› assignment 
…[3 more quoted lines elided]…
› or pseudocode, of this type of program?

Sorry, I don't have a pseudo code version, or a program stripped down to the
essentials, and I don't have time to create one right now. But below is a
fairly small report program with 3 level control breaks. At the top I
included the report tamplate, which is 80 columns to print on regular paper.
You will see several 'FIND' commands, they are just reads of database files
using Unisys DMS. They do not affect the control break logic in this
program. For brevity, I stripped out the routine to build the work file,
which is also not involved in the control break logic.

I like this method of doing control breaks because it is straightforward to
use, and you can easily implement code in the LEVEL X break to do stuff
before and after calling the LEVEL X+1 break.

Sorry for such a long post, but maybe others will find it helpful too.
```

#### ↳ Re: Seeking control break example

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e4ede65c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<64drbn$qd4$1@news.campus.mci.net>`
- **References:** `<64drbn$qd4$1@news.campus.mci.net>`

```

tmu··.@uc.··i.net (Tim Mueller) wrote:

› I am a beginning COBOL student and could use some help.  I  have an assignment 
› to write a program with 3 control breaks, totals at each break and a final 
› total.  Can anyone point me to someplace where I could find an example, code 
› or pseudocode, of this type of program?

There are two major opinions on this subject, depending from who's
book you studied from: nested-IF's and nested-PERFORM's. I prefer
nested-PERFORM's since it's easy to extrapolate the coding pattern to
the n'th level.

The best book covering my perfered method is "Structured COBOL 74/85:
Fundamentals and Style, 3rd ed." by Tyler Welburn and Wilson Price.
ISBN 0-07-069166-5. Here's a quick psudocode of the method for
multi-level:

000-MAINLINE.
1. open the files
2. Initialize the variable fields
3. do a priming read
4. perform 200-PROCESS-MAJOR-GROUP UNTIL END-OF-FILE
5. print the report totals
6. close the files
7. stop run

200-PROCESS-MAJOR-GROUP.
1. move the major control field of the current record to the
previous major control field
2. move zeros to the major control-totals
3. perform 210-PROCESS-INTERMEDIATE-GROUP
UNTIL END-OF-FILE
OR the current major control field is not equal to the previous
major control field
4. perform 330-PRINT-MAJOR-TOTAL

210-PROCESS-INTERMEDIATE-GROUP.
1. move the intermediate control field of the current record to the
previous intermediate control field
2. move zeros to the intermediate control-totals
3. perform 220-PROCESS-MINOR-GROUP
UNTIL END-OF-FILE
OR the current major control field is not equal to the previous
major control field
OR the current intermediate control field is not equal to the
previous intermediate control field
4. perform 320-PRINT-INTERMEDIATE-TOTAL

220-PROCESS-MINOR-GROUP.
1. move the minor control field of the current record to the
previous minor control field
2. move zeros to the minor control-totals
3. perform 300-PRINT-DETAIL-LINE
UNTIL END-OF-FILE
OR the current major control field is not equal to the previous
major control field
OR the current intermediate control field is not equal to the
previous intermediate control field
OR the current minor control field is not equal to the
previous minor control field
4. perform 310-PRINT-MINOR-TOTAL

300-PRINT-DETAIL-LINE.
1. if end-of-page then print report headings
2. format the detail line
3. print the detail line
4. set the line-spacing indicator for the next detail line
5. accumulate the minor control-totals
5. read the next record

310-PRINT-MINOR-TOTAL
1. format the minor total line
2. set the line spacing indicator for the total line
3. print the total line
4. set the line spacing indicator for the next detail line
5. roll the minor control-totals into the intermediate control-totals

The rest is left as an excersize.

The nested IF format is something like this (paraphrased from
"Advanced Structured COBOL: Batch, On-line and Data-base concepts" by
Tyler Welburn: ISBN 0-87484-558-0):

000-MAINLINE
1. open the files
2. Initialize the variable fields
3. perform 200-PROCESS-INPUT-RECORD UNTIL END-OF-FILE
4. print the report totals
5. close the files
6. stop run

200-PROCESS-INPUT-RECORD.
1. read the next record
2. if first-record
move the minor control field of the current record to the
previous minor control field
move the intermediate control field of the current record to
the previous intermediate control field
move the major control field of the current record to the
previous major control field
set first-record to 'no'
endif
3. if current major control field is not equal to previous major
control field
perform 220-PRINT-MINOR-TOTAL
perform 230-PRINT-INTERMEDIATE-TOTAL
perform 240-PRINT-MAJOR-TOTAL
else
if current intermediate control field is not equal to previous
intermediate control field
perform 220-PRINT-MINOR-TOTAL
perform 230-PRINT-INTERMEDIATE-TOTAL
else
if current minor control field is not equal to previous
minor control field
perform 220-PRINT-MINOR-TOTAL
endif
endif
endif
4. if not END-OF-FILE
perform 210-PRINT-DETAIL-LINE
endif

210-PRINT-DETAIL-LINE
1. if end-of-page then print report headings
2. format the detail line
3. print the detail line
4. set the line-spacing indicator for the next detail line
5. accumulate the minor control-totals

220-PRINT-MINOR-TOTAL
1. format the minor total line
2. set the line spacing indicator for the total line
3. print the total line
4. set the line spacing indicator for the next detail line
5. roll the minor control-totals into the intermediate control-totals
6. zero the minor control-totals
7. move the minor control field of the current record to the
previous minor control field

The rest is left as an excersize.

I've shown both methods so take your choice. Use the one that's easy
to understand, code, debug, run and present to your instructor (who's
grading this after all). And expect a minor religious battle as to
which method is better (I still stand by the nested PERFORM as the
best).

Hope this helps,

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

##### ↳ ↳ Re: Seeking control break example

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e4ede65c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0e4ede65c-p3@usenetarchives.gap>`
- **References:** `<64drbn$qd4$1@news.campus.mci.net> <gap-f0e4ede65c-p3@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
› tmu··.@uc.··i.net (Tim Mueller) wrote:
…[5 more quoted lines elided]…
› 
Tim,
Personally I find the examples posted here, while all valid (at first glance)
unnecessarily complex. Consider the following pseudocode, which may look a
little repetative, but IMHO is very straightforward. I must point out that
there's a million ways to accomplish the same task and each method is more a
matter of personal style or preference than anything else (this is how I like to
do it):

WORKING-STORAGE SECTION.

05 prev-hi-level-key pic x(..)
05 prev-mid-level-key pic x(..)
05 prev-lo-level-key pic x(..)

PROCEDURE DIVISION.

PERFORM INITIALIZATION-ROUTINE
PERFORM PROCESS-ROUTINE
PERFORM FINISH-ROUTINE

INITIALIZATION-ROUTINE.

initialize whatever
open files

perform read paragraph or do initial read

MOVE hi-level-key TO prev-hi-level-key
MOVE mid-level-key TO prev-mid-level-key
MOVE lo-level-key TO prev-lo-level-key

PROCESS-ROUTINE

EVALUATE TRUE
WHEN hi-level-key NOT = prev-hi-level-key
PERFORM LO-LEVEL-BREAK
PERFORM MID-LEVEL-BREAK
PERFORM HI-LEVEL-BREAK
MOVE hi-level-key TO prev-hi-level-key
MOVE mid-level-key TO prev-mid-level-key
MOVE lo-level-key TO prev-lo-level-key
WHEN mid-level-key NOT = prev-mid-level-key
PERFORM LO-LEVEL-BREAK
PERFORM MID-LEVEL-BREAK
MOVE mid-level-key TO prev-mid-level-key
MOVE lo-level-key TO prev-lo-level-key
WHEN lo-level-key NOT = prev-lo-level-key
PERFORM LO-LEVEL-BREAK
MOVE lo-level-key TO prev-lo-level-key
WHEN OTHER
check line counter if creating report and page break if necessary
END-EVALUATE.

do other 'detail' processing here

perform read paragraph or do next read

......
other paragraphs here
......

FINISH-ROUTINE.

PERFORM LO-LEVEL-BREAK
PERFORM MID-LEVEL-BREAK
PERFORM HI-LEVEL-BREAK

close files and go home
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

###### ↳ ↳ ↳ Re: Seeking control break example

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e4ede65c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0e4ede65c-p4@usenetarchives.gap>`
- **References:** `<64drbn$qd4$1@news.campus.mci.net> <gap-f0e4ede65c-p3@usenetarchives.gap> <gap-f0e4ede65c-p4@usenetarchives.gap>`

```

Ah yes, I'll keep the EVALUATE trick in mind. It'll save me from
having to indent too far.

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

##### ↳ ↳ Re: Seeking control break example

- **From:** "tom mcfarland" <ua-author-3012834@usenetarchives.gap>
- **Date:** 1997-11-16T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0e4ede65c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0e4ede65c-p3@usenetarchives.gap>`
- **References:** `<64drbn$qd4$1@news.campus.mci.net> <gap-f0e4ede65c-p3@usenetarchives.gap>`

```

Somebody finally got it right. I vote for the perform method.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
