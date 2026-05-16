[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Why isn't my program working?

_7 messages · 6 participants · 2003-04_

---

### Why isn't my program working?

- **From:** "GoldenWing" <great1gw@hotmail.com>
- **Date:** 2003-04-28T13:48:48-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,fj.comp.lang.cobol
- **Message-ID:** `<vaqqbv2fb85p4b@corp.supernews.com>`

```
Im haveing some trouble with this program  after the SSN is written for the
person,  it attempts to write part of the first name in what should be blank
space.  Im not sure how to fix this.  I realize i am quite new to cobol but
im trying to learn as best I can. Please Help.  Thanks



Program
                               below
==============================================================
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT TAX-FILE-I          ASSIGN TO
            'W:\cobol class\cobol assign 6\A6_TAX_I.TXT'
                                      ORGANIZATION LINE SEQUENTIAL.
           SELECT TAX-FILE-O          ASSIGN TO
            'W:\cobol class\cobol assign 6\TAX-FILE-0.TXT'
                                      ORGANIZATION LINE SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD TAX-FILE-I.
       01  TAX-REPORT.
           02  I-SSN                PIC X(09).
           02  I-NAME.
               03  I-FIRST-NAME         PIC X(10).
               03  I-LAST-NAME          PIC X(10).
           02  I-TAX-INCOME         PIC 9(8)V9(2).
           02  I-TAX-REFUND         PIC 9(8)V9(2).
           02  FILLER               PIC X(31).

       FD TAX-FILE-O.
       01 PRINT-RECORD            PIC X(80).

       WORKING-STORAGE SECTION.
       01  WS-VARIABLES.
           02  EOF                 PIC X(01) VALUE SPACES.
           02  P-COUNTER           PIC 9     VALUE 0.
           02  L-COUNTER           PIC 9(03) VALUE 0.

       01  TAX-RECORD-O.
          02  O-SSN                PIC X(11).
          02  FILLER               PIC 9(04).
          02  O-NAME               PIC X(20).
          02  FILLER               PIC X(02) VALUE SPACES.
          02  O-TAX-INCOME         PIC $$$,$$$,$$9.9(02).
          02  FILLER               PIC X(04) VALUE SPACES.
          02  O-TAX-REFUND         PIC $$$,$$$,$$9.9(02).
          02  FILLER               PIC X(03) VALUE SPACES.
          02  O-PERCENT            PIC Z9.99.
          02  FILLER               PIC X     VALUE '%'.

       01 WS-CURRENT-DATE.
           05 WS-YEAR              PIC X(04).
           05 WS-MONTH             PIC X(02).
           05 WS-DAY               PIC X(02).
           05 WS-HOUR              PIC X(02).
           05 WS-MIN               PIC X(02).
           05 FILLER               PIC X(04).

       01 HEADING-1.
           03 FILLER           PIC X(05) VALUE 'DATE:'.
           03 H1-MONTH         PIC 99    VALUE ZEROS.
           03 FILLER           PIC X     VALUE '/'.
           03 H1-DAY           PIC 99    VALUE ZEROS.
           03 FILLER           PIC X     VALUE '/'.
           03 H1-YEAR          PIC 9999  VALUE ZEROS.
           03 FILLER           PIC X(19) VALUE SPACES.
           03 FILLER           PIC X(10) VALUE
               'Tax Report'.
           03 FILLER           PIC X(05) VALUE SPACES.
           03 FILLER           PIC X(05) VALUE 'PAGE:'.
           03 C-PAGE           PIC Z9    VALUE ZERO.
           03 FILLER           PIC X(05) VALUE SPACES.

       01 HEADING-2.
           03 FILLER           PIC X(05) VALUE 'TIME:'.
           03 H2-HOUR          PIC Z9    VALUE SPACES.
           03 FILLER           PIC X     VALUE ':'.
           03 H2-MIN           PIC 99    VALUE ZEROS.
           03 FILLER           PIC X(15) VALUE SPACES.
           03 FILLER           PIC X(40) VALUE
                'By: Kevin Gereau, BIS 228, Section 14608'.
           02 FILLER           PIC X(18) VALUE SPACES.

       01 HEADING-3.
           03 FILLER           PIC X(80) VALUES SPACES.

       01 HEADING-4.
           03 FILLER           PIC X(03) VALUE 'SSN'.
           03 FILLER           PIC X(16) VALUE SPACES.
           03 FILLER           PIC X(04) VALUE 'Name'.
           03 FILLER           PIC X(18) VALUE SPACES.
           03 FILLER           PIC X(14) VALUE 'Taxable Income'.
           03 FILLER           PIC X(08) VALUE SPACES.
           03 FILLER           PIC X(03) VALUE 'Tax'.
           03 FILLER           PIC X(07) VALUE SPACES.
           03 FILLER           PIC X(07) VALUE 'Percent'.

       01 HEADING-5.
           03 FILLER           PIC X(80) VALUE ALL '='.



       01 STUFF.
           03   T-INCOME           PIC 9(08)V9(02).
           03   LK-TAX-REFUND      PIC 9(09)V9(02).
           03   LK-RATE            PIC 9(02)V9(01).

      **************************************************
      *        PROCEDURE DIVISION                      *
      **************************************************
       PROCEDURE DIVISION.
       000-START.
           PERFORM 100-INITIALIZE.
           PERFORM 300-PROCESS-REPORT UNTIL EOF = 'Y'.
           PERFORM 900-TERMINATE.
           STOP RUN.
       000-EXIT.
           EXIT.

      **************************************************
      *        100-INITIALZE                           *
      **************************************************
       100-INITIALIZE.
           OPEN    INPUT   TAX-FILE-I,
                   OUTPUT  TAX-FILE-O.

           MOVE FUNCTION CURRENT-DATE  TO WS-CURRENT-DATE.
           MOVE WS-YEAR                TO H1-YEAR.
           MOVE WS-MONTH               TO H1-MONTH.
           MOVE WS-DAY                 TO H1-DAY.
           MOVE WS-HOUR                TO H2-HOUR.
           MOVE WS-MIN                 TO H2-MIN.

           ADD 1                 TO      P-COUNTER.
           MOVE P-COUNTER        TO      C-PAGE.
           MOVE HEADING-1        TO      PRINT-RECORD.
           WRITE PRINT-RECORD    FROM    HEADING-1.
           MOVE HEADING-2        TO      PRINT-RECORD.
           WRITE PRINT-RECORD    FROM    HEADING-2.
           MOVE HEADING-3        TO      PRINT-RECORD.
           WRITE PRINT-RECORD    FROM    HEADING-3.
           MOVE HEADING-4        TO      PRINT-RECORD.
           WRITE PRINT-RECORD    FROM    HEADING-4
           MOVE HEADING-5        TO      PRINT-RECORD.
           WRITE PRINT-RECORD    FROM    HEADING-5.


       100-EXIT.
           EXIT.

      **************************************************
      *        300-PROCESS-REPORT                      *
      **************************************************

       300-PROCESS-REPORT.
           READ    TAX-FILE-I   INTO TAX-RECORD-O
               AT END MOVE 'Y'  TO EOF
                   NOT AT END
                   PERFORM 310-REPORT
           END-READ.
       300-EXIT.
           EXIT.

      **************************************************
      *    310-REPORT                                  *
      **************************************************
       310-REPORT.

           MOVE I-SSN (1:3)      TO    O-SSN (1:3).
           MOVE '-'              TO    O-SSN (4:1).
           MOVE I-SSN (4:2)      TO    O-SSN (5:2).
           MOVE '-'              TO    O-SSN (7:1).
           MOVE I-SSN (6:4)      TO    O-SSN (8:4).


           MOVE SPACES TO O-NAME.
               STRING I-FIRST-NAME DELIMITED BY SPACE
               ' ' DELIMITED BY SIZE
               I-LAST-NAME DELIMITED BY SPACE
               INTO O-NAME.


           PERFORM 320-TAX



           MOVE I-TAX-INCOME      TO      T-INCOME.
           MOVE T-INCOME          TO      O-TAX-INCOME.

           MOVE LK-TAX-REFUND     TO      O-TAX-REFUND.
           MOVE LK-RATE           TO      O-PERCENT.


           WRITE PRINT-RECORD     FROM    TAX-RECORD-O.


       310-EXIT.
           EXIT.

      **************************************************
      *    320-TAX                                     *
      **************************************************
       320-TAX.

           EVALUATE I-TAX-INCOME
               WHEN > 0 AND <= 27050
               COMPUTE LK-TAX-REFUND = 0 + I-TAX-INCOME * .015
               MOVE 15.00 TO LK-RATE

               WHEN > 27050 AND <= 65550
               COMPUTE
               LK-TAX-REFUND = 4057.5 + (I-TAX-INCOME - 27050) * .275
               MOVE 27.50 TO LK-RATE

               WHEN > 65550 AND <= 136750
               COMPUTE
               LK-TAX-REFUND = 36361 + (I-TAX-INCOME - 136750) * .305
               MOVE 30.50 TO LK-RATE

               WHEN > 136750 AND <= 297350
               COMPUTE
               LK-TAX-REFUND = 36361 + (I-TAX-INCOME - 136750) * .355
               MOVE 35.50 TO LK-RATE

               WHEN > 297350
               COMPUTE
               LK-TAX-REFUND = 93374 + (I-TAX-INCOME - 297350) * .391
               MOVE 39.10 TO LK-RATE

           END-EVALUATE.



       320-EXIT.
           EXIT.

      **************************************************
      *    900-TERMINATE                               *
      **************************************************

       900-TERMINATE.
           CLOSE   TAX-FILE-I, TAX-FILE-O.
       900-EXIT.
           EXIT.

====================================================================





 Output file below


====================================================================
DATE:04/28/2003                   Tax Report     PAGE: 1
TIME:13:40

SSN                Name                  Taxable Income        Tax
Percent
============================================================================
====
563-02-9749hn  John Smith    00050000    $50,000.00        $10,368.75
27.50
429-09-2391acy Stacy Roberts 01053800 $1,053,800.00       $389,145.95
39.10
529-10-1468e   Joe Freeman   00030000    $30,000.00         $4,868.75
27.50
348-33-0124y   May Finn      00078000    $78,000.00        $18,442.25
30.50
390-09-9234nry Henry Carson  00025429    $25,429.91           $381.44
15.00
453-92-1483thurArthur Carpenter291849   $291,849.30        $91,421.25
35.50
109-93-9102tt  Matt Watson   10038290$10,038,290.19     $3,902,081.61
39.10
291-83-0488nny Kenny Welsh   30292849$30,292,849.03    $11,821,614.12
39.10
289-09-1939ssa Tessa Wells   00039281    $39,281.72         $7,421.22
27.50
435-67-2345thy Cathy Weiss   00076485    $76,485.90        $17,980.44
30.50
245-19-0983ris Chris Orr     10294840$10,294,840.23     $4,002,392.67
39.10
432-93-8573lliaWilliam O'Neil09283749 $9,283,749.29     $3,607,056.12
39.10
498-20-9234lie Julie Olson   40293420$40,293,420.98    $15,731,837.75
39.10
139-27-3049chaeMichael Owens 09234909 $9,234,909.39     $3,587,959.72
39.10
392-03-9484charRichard Packard0002398     $2,398.58            $35.97
15.00
485-93-0293san Susan Thomas  00029347    $29,347.73         $4,689.37
27.50
124-34-5543ry  Mary Jones    00000032        $32.34             $0.48
15.00
232-10-9484rma Norma Keefer  00000123       $123.39             $1.85
15.00
323-44-5023rnesEarnest Kent  00001029     $1,029.49            $15.44
15.00
129-48-5372len Ellen Kerr    00004502     $4,502.93            $67.54
15.00
239-48-2834ishaTrisha Lee    00005693     $5,693.83            $85.40
15.00
328-37-6528y   Joy Phillips  00007382     $7,382.73           $110.74
15.00
348-27-3948ke  Mike July     00000283       $283.94             $4.25
15.00
120-93-8373ul  Paul Gill     00394820   $394,820.39       $131,484.92
39.10
120-93-8483drewAndrew Charles00076382    $76,382.73        $17,948.98
30.50
342-93-8473ry  Gary Scott    00124393   $124,393.82        $32,592.36
30.50
234-56-4323ria Maria Gibbons 00002348     $2,348.28            $35.22
15.00
302-98-1748andyBrandy Goba   00029384    $29,384.72         $4,699.54
27.50
945-83-9749bertAlbert Smith  00009482     $9,482.70           $142.24
15.00
429-29-1051hn  John Flowers  00650294   $650,294.00       $231,375.10
39.10
302-95-8763b   Bob McBride   01097436 $1,097,436.60       $406,207.86
39.10
444-59-3124m   Jim Marsh     00078043    $78,043.66        $18,455.56
30.50
349-09-9223m   Tim Lawens    00204939   $204,939.91        $60,568.41
35.50
249-23-9542lliaWilliam Kyser 00002980     $2,980.19            $44.70
15.00
309-82-0488ggy Peggy Welsh   00092239    $92,239.00        $22,785.14
30.50
329-04-5939y   Amy Law       00002281     $2,281.72            $34.22
15.00
432-07-2445chaeMichael Harris00176582   $176,582.00        $50,501.36
35.50
420-38-4783ris Chris Hall    00039200    $39,200.23         $7,398.81
27.50
432-99-0817dy  Andy Hamilton 00004983     $4,983.20            $74.74
15.00
204-98-7324dy  Judy Narman   00093420    $93,420.98        $23,145.64
30.50
339-27-2329ck  Jack Owens    00034909    $34,909.39         $6,218.83
27.50
402-93-8484ch  Rich Hanks    00012393    $12,393.48           $185.90
15.00
353-23-0293arleCharles Thomas00029347    $29,347.73         $4,689.37
27.50
420-91-2739ank Frank Scott   02003942 $2,003,942.58       $760,651.69
39.10
363-36-5543yce Joyce Fox     00021942    $21,942.34           $329.13
15.00
402-90-9484wardEdward Richards0043225$10,043,225.39     $3,904,011.27
39.10
422-78-5372len Allen Hood    00026702    $26,702.93           $400.54
15.00
120-58-2834vid David Lee     00042653    $42,653.83         $8,348.55
27.50
452-76-6528llisMellisa Kelly 00024582    $24,582.73           $368.74
15.00
321-09-4948ke  Mike Fox      00024553    $24,553.94           $368.30
15.00
209-82-7373th  Ruth Gill     00024853    $24,853.39           $372.80
15.00
291-87-8483mes James Fussman 00002984     $2,984.53            $44.76
15.00
204-98-8473ry  Gary Green    00127643   $127,643.82        $33,583.61
30.50
028-71-4323ria Maria Nelson  01469448 $1,469,448.28       $551,664.42
39.10
356-24-1748al  Neal Myers    00001987     $1,987.72            $29.81
15.00
```

#### ↳ Re: Why isn't my program working?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T18:16:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b8jr57$hnb$1@peabody.colorado.edu>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com>`

```
I don't know your compiler nor environment - but I am wondering about the filler
in TAX-RECORD-O.   Why do you have a filler with PIC 9(04)?   Could it be filled
with low values?   If so, does your output environment squeeze over nulls?

Try giving TAX-RECORD-O a value of spaces and let us know what happens.


Also, I don't see any reason for reference modification here.  It think it is
clearer to break up your SSN into 04 levels such as O-SSN-FIRST-FOUR.
```

#### ↳ Re: Why isn't my program working?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-04-28T22:02:34+03:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,fj.comp.lang.cobol
- **Message-ID:** `<9juqavs1a1an6esssofbp4tmq4ms3v7akr@4ax.com>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com>`

```
On Mon, 28 Apr 2003 13:48:48 -0400 "GoldenWing" <great1gw@hotmail.com> wrote:

   [ snipped ]

:>          02  FILLER               PIC 9(04).

Quite unusual for a FILLER, wouldn't you say?

:>           READ    TAX-FILE-I   INTO TAX-RECORD-O

Think about this statement.

   [ snipped ]
```

#### ↳ Re: Why isn't my program working?

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-04-28T16:46:15-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,fj.comp.lang.cobol
- **Message-ID:** `<3EADA127.2090104@Knology.net>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com>`

```
GoldenWing wrote:
> Im haveing some trouble with this program  after the SSN is written for the
> person,  it attempts to write part of the first name in what should be blank
> space.  Im not sure how to fix this.  I realize i am quite new to cobol but
> im trying to learn as best I can. Please Help.  Thanks

I've distilled this for you...

>        FD TAX-FILE-I.
>        01  TAX-REPORT.
…[6 more quoted lines elided]…
>            02  FILLER               PIC X(31).

...

>        01  TAX-RECORD-O.
>           02  O-SSN                PIC X(11).
…[8 more quoted lines elided]…
>           02  FILLER               PIC X     VALUE '%'.

...

>        300-PROCESS-REPORT.
>            READ    TAX-FILE-I   INTO TAX-RECORD-O
…[3 more quoted lines elided]…
>            END-READ.

...

>            WRITE PRINT-RECORD     FROM    TAX-RECORD-O.

When you Read .. Into (at least with my implementation), your FD does 
not get filled.  And, since you have a mismatch in how the file is 
described and how the working-storage variable is defined, you're 
getting the extra stuff from your read...into.  I would just do the 
"Read", then move the data from the I- record to the -O record (which 
looks like what you're doing anyway - just take the into clause off and 
see what happens.)
```

##### ↳ ↳ READ INTO (was: Why isn't my program working?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-28T17:07:50-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,fj.comp.lang.cobol
- **Message-ID:** `<b8k8o5$b10$1@slb6.atl.mindspring.net>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com> <3EADA127.2090104@Knology.net>`

```
"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
news:3EADA127.2090104@Knology.net...
> GoldenWing wrote:
<snip>
>
> >            WRITE PRINT-RECORD     FROM    TAX-RECORD-O.
>
> When you Read .. Into (at least with my implementation), your FD does
> not get filled.

If you have a compiler that does NOT "fill in" the records under an FD when
you do a READ INTO, then you have a compiler that does NOT conform to the
ANSI ('85 or 2002) COBOL Standards. From page 497 of the 2002 Standard (and
the '85 Standard has similar wording),

"4) The result of the successful execution of a READ statement with the INTO
phrase is equivalent to the application of the following rules in the order
specified:

     a) The same READ statement without the INTO phrase is executed.
     b) The current record is moved from the record area to the area
specified by identifier-1 according to the rules for the MOVE statement
without the CORRESPONDING phrase. The size of the current record is
determined by rules specified in the RECORD clause. If the file description
entry contains a RECORD IS VARYING clause, the implied move is an
alphanumeric group move. Item identification of the data item referenced by
identifier-1 is done after the record has been read and immediately before
it is moved to the data item. The record is available in both the record
area and the data item referenced by identifier-1.

If the execution of a READ statement with the INTO phrase is unsuccessful,
the content of the data item referenced by identifier-1 is unchanged and
item identification of the data item referenced by identifier-1 is not
done."
```

###### ↳ ↳ ↳ Re: READ INTO (was: Why isn't my program working?

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-04-28T20:27:30-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,fj.comp.lang.cobol
- **Message-ID:** `<3EADD502.8080609@Knology.net>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com> <3EADA127.2090104@Knology.net> <b8k8o5$b10$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> "LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
> news:3EADA127.2090104@Knology.net...
…[13 more quoted lines elided]…
> ANSI ('85 or 2002) COBOL Standards.

Interesting, but understandable, since I cut my teeth (and, 
coincidentally, the last time I did a read..into) was COBOL 74...  :) 
Thanks for the information.
```

###### ↳ ↳ ↳ Re: READ INTO (was: Why isn't my program working?

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-29T08:53:10-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b8m756$vj2$1@si05.rsvl.unisys.com>`
- **References:** `<vaqqbv2fb85p4b@corp.supernews.com> <3EADA127.2090104@Knology.net> <b8k8o5$b10$1@slb6.atl.mindspring.net> <3EADD502.8080609@Knology.net>`

```

"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
news:3EADD502.8080609@Knology.net...

> > If you have a compiler that does NOT "fill in" the records under an FD
when
> > you do a READ INTO, then you have a compiler that does NOT conform to
the
> > ANSI ('85 or 2002) COBOL Standards.
>
> Interesting, but understandable, since I cut my teeth (and,
> coincidentally, the last time I did a read..into) was COBOL 74...  :)
> Thanks for the information.

Level 2 feature in the '68 standard; moved to Level (base level of SEQ, REL,
INX modules) in the '74 standard.

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
