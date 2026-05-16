[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT-RETURN not referenced

_25 messages · 14 participants · 1998-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Tutorials, books, learning`](../topics.md#learning)

---

### SORT-RETURN not referenced

- **From:** patbean@help.worldnet.att.net
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
I am a college student taking advanced business programming ... my
class has been working on the same program since the beginning of
september and we are all getting the same error message and no one
seems to be able to help us solve the problem ... I hope someone can
help us ... I am attqcheing a part of the program .... and the error
messages we get ... if you need more information please email me or
let me know and I will try and provide the needed information
....please take help out of address if you would like to email me...


19.17.37 JOB09546  IEF677I WARNING MESSAGE(S) FOR JOB C05060G  ISSUED
 19.17.38 JOB09546  $HASP373 C05060G  STARTED - INIT    1 - CLASS H -
SYS MVS1
 19.17.41 JOB09546  +IGZ026I The SORT-RETURN special register was
never referenc
                             current content indicated the sort or
merge operati
                             program 'CHECKOUT' on line number '339'
was unsucce
 19.17.42 JOB09546  $HASP395 C05060G  ENDED
0------ JES2 JOB STATISTICS ------
-  13 NOV 1998 JOB EXECUTION DATE
-          623 CARDS READ
-          925 SYSOUT PRINT RECORDS
-            0 SYSOUT PUNCH RECORDS
-           49 SYSOUT SPOOL KBYTES
-         0.07 MINUTES EXECUTION TIME
1        1 //C05060G JOB 77103,'BEAN',CLASS=H,MSGLEVEL=(2,0)
           /*JOBPARM ROOM=USER
           /*ROUTE PRINT AKRONVM.C05060
           /*ROUTE PRINT AKRONVM.C05060
           /*ROUTE PUNCH AKRONVM.C05060
           //*
         2 //DEBUG     EXEC COB85
        17 //SYSIN     DD *               GENERATED STATEMENT
        18 //LOADGO         EXEC GOCOB DMAP=,PMAP=
        39 //GO.INPUT    DD   DSN=USER.R1RLM1.COB93,DISP=SHR
        40 //TRANSRPT  DD   SYSOUT=A
        41 //SRTRPT    DD   SYSOUT=A
        42 //ERRPT     DD   SYSOUT=A
        43 //
 
1
  STMT NO. MESSAGE
         2 IEFC001I PROCEDURE COB85 WAS EXPANDED USING SYSTEM LIBRARY
ACAD.PROCL
        18 IEFC001I PROCEDURE GOCOB WAS EXPANDED USING SYSTEM LIBRARY
ACAD.PROCL
        42 IEF686I DDNAME REFERRED TO ON DDNAME KEYWORD IN PRIOR STEP
WAS NOT RE
 IEF142I C05060G COB2 DEBUG - STEP WAS EXECUTED - COND CODE 0000
 IEF373I STEP /COB2    / START 98317.1917
 IEF373I STEP /COB2    / START 98317.1917
 IEF374I STEP /COB2    / STOP  98317.1917 CPU    0MIN 00.22SEC SRB
0MIN 00.02
 IGZ026I The SORT-RETURN special register was never referenced but
         current content indicated the sort or merge operation in
         program 'CHECKOUT' on line number '339' was unsuccessful.
 IEF142I C05060G GO LOADGO - STEP WAS EXECUTED - COND CODE 0000
 IEF373I STEP /GO      / START 98317.1917
 IEF374I STEP /GO      / STOP  98317.1917 CPU    0MIN 00.30SEC SRB
0MIN 00.02
 IEF375I  JOB /C05060G / START 98317.1917
 IEF376I  JOB /C05060G / STOP  98317.1917 CPU    0MIN 00.52SEC SRB
0MIN 00.04
1PP 5668-958 IBM VS COBOL II Release 4.0 09/15/92     

*******************************************************************************************

 000337                000-MAIN-CONTROL.
   000338                    DISPLAY 'MAIN CONTROL PARAGRAPH FOUND'.
   000339                    SORT SORT-FILE
   000340                        ON ASCENDING KEY SWR-HOME-PHONE-1
SWR-REC-TYPE-
   000341                        INPUT PROCEDURE IS
100-VALIDATE-BEFORE-SORT
   000342                        OUTPUT PROCEDURE IS
500-VALIDATE-AFTER-SORT.
   000343                        DISPLAY 'END OF SORT STATEMENT'.
   000344
   000345                    STOP RUN.
   000346
   000347
   000348                100-VALIDATE-BEFORE-SORT SECTION.
   000349
   000350                110-VALIDATE-MAIN.
   000351                    DISPLAY 'ENTERED INPUT PROCEDURE'.
   000352                    OPEN INPUT  INPUT-FILE
   000353                         OUTPUT TRANS-REPORT
   000354                         OUTPUT ERROR-REPORT.
   000355
   000356                    PERFORM 120-PROCESS-IN-RECORD
   000357                        UNTIL THERE-ARE-NO-MORE-RECORDS.
   000358                    PERFORM 190-CLOSE-FILES
   000359                    GO TO 400-EXIT.
   000360
   000361                120-PROCESS-IN-RECORD.
   000362                    DISPLAY 'PROCESS NEXT RECORD ENTERED'.
   000363                    PERFORM 125-READ-INPUT.
   000364                    IF RECORD-TYPE-IN-1 = '1'
   000365      1                  THEN PERFORM 121-REC1-PROC
   000366                         ELSE
   000367      1                       PERFORM 126-REC2-PROC
   000368                    END-IF.
   000369
   000370                    IF LISTING-LINES >= MAX-LINES
   000371      1                  THEN PERFORM 200-LISTING-HDGS
   000372                         ELSE
   000373      1                       WRITE LISTING-RECORD FROM
LISTING-DL
   000374      1                       AFTER ADVANCING LISTING-LINES
   000375                     END-IF.
   000376
   000377                125-READ-INPUT.
   000378
   000379                    READ INPUT-FILE
   000380                         AT END
   000381      1                      MOVE 'NO' TO
ARE-THERE-MORE-RECORDS-WS.
   000382
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72inoq$1ub@sjx-ixn8.ix.netcom.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
A few comments (interspersed within your post)

patbean@help.worldnet.att.net wrote in message
<364dd7d1.5327538@netnews.worldnet.att.net>...
>I am a college student taking advanced business programming ... my
>class has been working on the same program since the beginning of
…[39 more quoted lines elided]…
>

   shouldn't your JCL have
         //GO.TRANSRPT  DD   SYSOUT=A
         //GO.SRTRPT    DD   SYSOUT=A
         //GO.ERRPT     DD   SYSOUT=A

but much more importantly, where are you sending your DISPLAY and SORT
output to?  What is your OUTDD compiler option set to? (probably the default
of SYSOUT)  If so, does your GOCOB already allocate it? (If not, you
should - although some software releases will do this for you).   You
probably need a SORTOUT DD card as well - and when you look at that, you
will see why your SORT is failing (or at least get a better clue).



>1
>  STMT NO. MESSAGE
…[23 more quoted lines elided]…
>***************************************************************************
****************
>
> 000337                000-MAIN-CONTROL.
…[7 more quoted lines elided]…
>500-VALIDATE-AFTER-SORT.

  You aren't showing us the 500-VALIDATE... output procedure.   My guess (as
discussed in another recent thread) is that you are not executing your
OUTPUT logic in a "full loop" so the AT END of your RETURN isn't being
executed - but that is just a guess without seeing the full code.

>   000343                        DISPLAY 'END OF SORT STATEMENT'.
>   000344
…[22 more quoted lines elided]…
>   000367      1                       PERFORM 126-REC2-PROC

    Does this routine ever do a RELEASE (or does anything)?


>   000368                    END-IF.
>   000369
…[14 more quoted lines elided]…
>   000382
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72io7g$o1e@dfw-ixnews10.ix.netcom.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72inoq$1ub@sjx-ixn8.ix.netcom.com>`

```
(Just a warning, I may have mixed up my RELEASES and RETURNS in my comments.
I always have to look those up when I go to code them.)

William M. Klein wrote in message <72inoq$1ub@sjx-ixn8.ix.netcom.com>...
>A few comments (interspersed within your post)
>
…[51 more quoted lines elided]…
>output to?  What is your OUTDD compiler option set to? (probably the
default
>of SYSOUT)  If so, does your GOCOB already allocate it? (If not, you
>should - although some software releases will do this for you).   You
…[30 more quoted lines elided]…
>>**************************************************************************
*
>****************
>>
…[10 more quoted lines elided]…
>  You aren't showing us the 500-VALIDATE... output procedure.   My guess
(as
>discussed in another recent thread) is that you are not executing your
>OUTPUT logic in a "full loop" so the AT END of your RETURN isn't being
…[49 more quoted lines elided]…
>
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** patbean@help.worldnet.att.net
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364ee4c8.8647469@netnews.worldnet.att.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72inoq$1ub@sjx-ixn8.ix.netcom.com>`

```
here is the entire program .. it is going to be written to three
different reports ...  I was trying to post the parts that I thought
were needed ....


000333                PROCEDURE DIVISION.
   000334
   000335                A-000-MAIN SECTION.
   000336
   000337                000-MAIN-CONTROL.
   000338                    DISPLAY 'MAIN CONTROL PARAGRAPH FOUND'.
   000339                    SORT SORT-FILE
   000340                        ON ASCENDING KEY SWR-HOME-PHONE-1
SWR-REC-TYPE-
   000341                        INPUT PROCEDURE IS
100-VALIDATE-BEFORE-SORT
   000342                        OUTPUT PROCEDURE IS
500-VALIDATE-AFTER-SORT.
   000343                        DISPLAY 'END OF SORT STATEMENT'.
   000344
   000345                    STOP RUN.
   000346
   000347
   000348                100-VALIDATE-BEFORE-SORT SECTION.
   000349
   000350                110-VALIDATE-MAIN.
   000351                    DISPLAY 'ENTERED INPUT PROCEDURE'.
   000352                    OPEN INPUT  INPUT-FILE
   000353                         OUTPUT TRANS-REPORT
   000354                         OUTPUT ERROR-REPORT.
   000355
   000356                    PERFORM 120-PROCESS-IN-RECORD
   000357                        UNTIL THERE-ARE-NO-MORE-RECORDS.
   000358                    PERFORM 190-CLOSE-FILES
   000359                    GO TO 400-EXIT.
   000360
   000361                120-PROCESS-IN-RECORD.
   000362                    DISPLAY 'PROCESS NEXT RECORD ENTERED'.
   000363                    PERFORM 125-READ-INPUT.
   000364                    IF RECORD-TYPE-IN-1 = '1'
   000365      1                  THEN PERFORM 121-REC1-PROC
   000366                         ELSE
   000367      1                       PERFORM 126-REC2-PROC
   000368                    END-IF.
   000369
   000370                    IF LISTING-LINES >= MAX-LINES
   000371      1                  THEN PERFORM 200-LISTING-HDGS
   000372                         ELSE
   000373      1                       WRITE LISTING-RECORD FROM
LISTING-DL
   000374      1                       AFTER ADVANCING LISTING-LINES
   000375                     END-IF.
   000376
   000377                125-READ-INPUT.
   000378
   000379                    READ INPUT-FILE
   000380                         AT END
   000381      1                      MOVE 'NO' TO
ARE-THERE-MORE-RECORDS-WS.
   000382
   000383
   000384
   000385                121-REC1-PROC.
0  000386                    DISPLAY 'VALIDATE RECORD 1'.
   000387                    MOVE INPUT-REC1 TO HLD-REC1
   000388                    INSPECT HOME-PHONE-IN-1 TALLYING
WS-REC1-SP-CTR
   000389                         FOR ALL SPACES.
   000390
   000391                    IF WS-REC1-SP-CTR GREATER THAN ZERO
   000392      1                  THEN PERFORM 210-WRITE-REC1-ERROR
   000393      1                  MOVE 0 TO WS-REC1-SP-CTR
   000394                        ELSE
   000395      1                     PERFORM 240-RELEASE-REC1
   000396                    END-IF.
   000397
   000398
   000399                126-REC2-PROC.
   000400                    DISPLAY 'VALIDATE RECORD 2'.
   000401                    MOVE INPUT-REC2 TO HLD-REC2
   000402                    INSPECT HOME-PHONE-IN-2 TALLYING
WS-REC2-SP-CTR
   000403                         FOR ALL SPACES.
   000404                    IF WS-REC2-SP-CTR GREATER THAN ZERO
   000405      1                  THEN PERFORM 211-WRITE-REC2-ERROR
   000406      1                  MOVE 0 TO WS-REC2-SP-CTR
   000407      1                     PERFORM 250-RELEASE-REC2
   000408                    END-IF.
   000409                    DISPLAY 'VALIDATE RECORD TYPE 2'.
   000410
   000411                190-CLOSE-FILES.
   000412                    DISPLAY 'CLOSE FILES PARAGRAPH'.
   000413                    CLOSE INPUT-FILE.
   000414
   000415                200-LISTING-HDGS.
   000416
   000417                    WRITE LISTING-RECORD FROM
ALL-REC-HEAD-LINE1-WS
   000418                          AFTER ADVANCING PAGE.
   000419                    WRITE LISTING-RECORD FROM
ALL-REC-HEAD-LINE2-WS
   000420                          AFTER ADVANCING 2 LINES.
   000421
   000422                    MOVE 3 TO LISTING-LINES.
   000423                    MOVE 2 TO LS-SPACING-WS.
   000424
   000425                210-WRITE-REC1-ERROR.
   000426                    MOVE SPACE TO ERROR-RPT-DETAIL-LINE
   000427                    MOVE HLD-HOME-PHONE-1 TO HOME-PHONE-EM-DL
   000428                    MOVE HLD-LAST-NAME    TO LAST-NAME-EM-DL
   000429                    MOVE HLD-FIRST-NAME   TO FIRST-NAME-EM-DL
   000430                    MOVE SPC-HOME-PHONE-EM TO
ERROR-MESSAGE-DL
   000431
   000432                    WRITE ERROR-RECORD FROM
ERROR-RPT-DETAIL-LINE
   000433                        AFTER ADVANCING 1 LINE.
   000434                        ADD 1 TO ERR-LINE-COUNT-WS.
   000435
   000436                211-WRITE-REC2-ERROR.
   000437                    MOVE SPACES TO ERROR-RPT-DETAIL-LINE
   000438                    MOVE HLD-HOME-PHONE-2 TO HOME-PHONE-EM-DL
   000439                    MOVE SPACES TO LAST-NAME-EM-DL
   000440                    MOVE SPACES TO FIRST-NAME-EM-DL
0  000441                    MOVE SPC-HOME-PHONE-EM TO
ERROR-MESSAGE-DL
   000442
   000443                    WRITE ERROR-RECORD FROM
ERROR-RPT-DETAIL-LINE
   000444                        AFTER ADVANCING 1 LINE.
   000445                        ADD 1 TO ERR-LINE-COUNT-WS.
   000446
   000447                240-RELEASE-REC1.
   000448                    DISPLAY 'RELEASE REC 1'.
   000449                    RELEASE WS-REC1 FROM HLD-REC1.
   000450
   000451                250-RELEASE-REC2.
   000452                    DISPLAY 'RELEASE REC 2'.
   000453                    RELEASE WS-REC2 FROM HLD-REC2.
   000454
   000455                400-EXIT.
   000456
   000457                    EXIT.
   000458
   000459                500-VALIDATE-AFTER-SORT SECTION.
   000460
   000461                301-OUTPUT-PROCEDURE.
   000462
   000463                    RETURN SORT-FILE
   000464      1             AT END MOVE 'NO' TO
ARE-THERE-MORE-SORT-REC-WS.
   000465
   000466                    IF 1ST-RECORD-IN EQUAL TO 'Y' AND
   000467                    SWR-REC-TYPE-1 EQUAL TO REC-TYPE-HLD
   000468
   000469      1             MOVE SWR-HOME-PHONE-1 TO HOME-PHONE-HLD
   000470      1             MOVE SWR-REC-TYPE-1 TO REC-TYPE-HLD
   000471
   000472      1             PERFORM 310-VALIDATE-RECORD
   000473      1                 UNTIL THERE-ARE-NO-MORE-SORT-RECORDS
   000474
   000475                        ELSE
   000476      1                     MOVE SWR-HOME-PHONE-1 TO
HOME-PHONE-DL
   000477      1
HOME-PHONE-HLD
   000478      1                     MOVE SWR-REC-TYPE-1 TO
REC-TYPE-HLD
   000479
   000480      1                     MOVE 2ND-REC-EM TO
ERROR-MESSAGE-DL
   000481      1                     MOVE 'N' TO 1ST-RECORD-IN
   000482      1                     PERFORM 610-ERROR-REPORT.
   000483
   000484                    PERFORM 710-CLOSE-FILES.
   000485                    GO 810-EXIT.
   000486
   000487                310-VALIDATE-RECORD.
   000488
   000489                    RETURN SORT-FILE
   000490      1                 AT END MOVE 'NO' TO
ARE-THERE-MORE-SORT-REC-WS.
   000491
   000492                    IF SWR-REC-TYPE-1 EQUAL REC-TYPE-HLD
   000493                        OR SWR-REC-TYPE-2 EQUAL TO
REC-TYPE-HLD
   000494      1                 PERFORM 311-RECORD-TYPE-EQUAL
   000495
0  000496                        ELSE
   000497      1                     PERFORM 312-COMPARE-TYPE.
   000498
   000499                311-RECORD-TYPE-EQUAL.
   000500
   000501                    IF SWR-REC-TYPE-1 EQUAL TO 1
   000502      1                 MOVE HOME-PHONE-HLD TO
HOME-PHONE-EM-DL
   000503      1                 MOVE LAST-NAME-HLD  TO
LAST-NAME-EM-DL
   000504      1                 MOVE FIRST-NAME-HLD TO
FIRST-NAME-EM-DL
   000505      1                 MOVE 1ST-REC-EM TO ERROR-MESSAGE-DL
   000506      1                 MOVE RECORD-TYPE-IN-1 TO REC-TYPE-HLD
   000507      1                 MOVE HOME-PHONE-IN-1 TO
HOME-PHONE-HLD
   000508      1                 MOVE LAST-NAME-IN TO LAST-NAME-HLD
   000509      1                 MOVE FIRST-NAME-IN TO FIRST-NAME-HLD
   000510      1                 PERFORM 610-ERROR-REPORT
   000511
   000512                        ELSE
   000513      1                     MOVE SWR-REC-TYPE-2 TO
REC-TYPE-HLD
   000514      1                     MOVE SWR-HOME-PHONE-2 TO
HOME-PHONE-HLD
   000515      1
HOME-PHONE-EM-DL
   000516      1                     MOVE 2ND-REC-EM TO
ERROR-MESSAGE-DL
   000517      1                     PERFORM 610-ERROR-REPORT.
   000518
   000519                312-COMPARE-TYPE.
   000520
   000521                    IF SWR-REC-TYPE-1 LESS THAN REC-TYPE-HLD
   000522      1                 MOVE SPACES TO HOLD-FIELDS
   000523      1                 MOVE SWR-REC-TYPE-1 TO REC-TYPE-HLD
   000524      1                 MOVE SWR-HOME-PHONE-1 TO
HOME-PHONE-HLD
   000525      1                 MOVE LAST-NAME-IN TO LAST-NAME-HLD
   000526      1                 MOVE FIRST-NAME-IN TO FIRST-NAME-HLD
   000527      1                 MOVE CALL-CHARGE-IN TO
CALL-CHARGE-HLD
   000528      1                 PERFORM 310-VALIDATE-RECORD
   000529      1                    UNTIL
THERE-ARE-NO-MORE-SORT-RECORDS
   000530
   000531
   000532                        ELSE
   000533      1                     PERFORM 313-HOME-PHONE-CHECK.
   000534
   000535                313-HOME-PHONE-CHECK.
   000536
   000537                    IF SWR-HOME-PHONE-2 NOT EQUAL
HOME-PHONE-HLD
   000538
   000539      1                 MOVE HOME-PHONE-HLD   TO
HOME-PHONE-EM-DL
   000540      1                 MOVE LAST-NAME-HLD    TO
LAST-NAME-EM-DL
   000541      1                 MOVE FIRST-NAME-HLD   TO
FIRST-NAME-EM-DL
   000542      1                 MOVE HOME-PHONE-EM    TO
ERROR-MESSAGE-DL
   000543      1                 MOVE RECORD-TYPE-IN-2 TO REC-TYPE-HLD
   000544      1                 MOVE HOME-PHONE-IN-2  TO
HOME-PHONE-HLD
   000545
   000546      1                 PERFORM 610-ERROR-REPORT
   000547
   000548                        ELSE
   000549
   000550      1                     PERFORM 400-PRINT-DETAIL-LINE.
0  000551
   000552                610-ERROR-REPORT.
   000553
   000554               *    IF ERR-LINE-COUNT-WS IS NOT < MAX-LINES
   000555               *        PERFORM 700-PRINT-ERR-RPT-HEADINGS.
   000556
   000557                        WRITE ERROR-RECORD FROM
ERROR-RPT-DETAIL-LINE
   000558                            AFTER ADVANCING ERR-SPACING-WS.
   000559                            ADD ERR-SPACING-WS TO
ERR-LINE-COUNT-WS.
   000560                            MOVE 1 TO ERR-SPACING-WS.
   000561                            MOVE SPACES TO
ERROR-RPT-DETAIL-LINE.
   000562
   000563                            PERFORM 310-VALIDATE-RECORD
   000564                                UNTIL
THERE-ARE-NO-MORE-SORT-RECORDS.
   000565
   000566                400-PRINT-DETAIL-LINE.
   000567
   000568                    IF DL-LINE-COUNT-WS IS NOT < MAX-LINES
   000569      1                 PERFORM 410-PRINT-DL-HEADINGS.
   000570                        MOVE HOME-PHONE-HLD    TO
HOME-PHONE-DL.
   000571                        MOVE LAST-NAME-HLD     TO
LAST-NAME-DL.
   000572                        MOVE FIRST-NAME-HLD    TO
FIRST-NAME-DL.
   000573                        MOVE STREET-ADDRESS-IN TO
STREET-ADD-DL.
   000574                        MOVE CITY-IN           TO CITY-DL.
   000575                        MOVE STATE-IN          TO STATE-DL.
   000576                        MOVE ZIP-IN            TO ZIP-DL.
   000577                        MOVE CALL-CHARGE-HLD   TO
CALL-CHRG-DL.
   000578                        ADD CALL-CHARGE-HLD    TO
TOTAL-CHARGES-WS.
   000579
   000580                        WRITE TRANSACTION-RECORD FROM
TRANS-DETAIL-LINE
   000581                            AFTER ADVANCING DL-SPACING-WS.
   000582
   000583                        ADD DL-SPACING-WS TO
DL-LINE-COUNT-WS.
   000584                        ADD 1 TO DL-SPACING-WS.
   000585                        MOVE SPACES TO TRANS-DETAIL-LINE-WS.
   000586
   000587                        PERFORM 310-VALIDATE-RECORD.
   000588
   000589                410-PRINT-DL-HEADINGS.
   000590
   000591                    WRITE TRANSACTION-RECORD FROM
TRANS-HEAD-LINE1-WS
   000592                          AFTER ADVANCING PAGE.
   000593                    WRITE TRANSACTION-RECORD FROM
TRANS-HEAD-LINE2-WS
   000594                          AFTER ADVANCING 2 LINES.
   000595
   000596                    MOVE 3 TO DL-LINE-COUNT-WS.
   000597                    MOVE 2 TO DL-SPACING-WS.
   000598
   000599
   000600                710-CLOSE-FILES.
   000601
   000602                    CLOSE INPUT-FILE
   000603                          TRANS-REPORT
   000604                          ERROR-REPORT
   000605                          LISTING-REPORT.
0  000606
   000607                810-EXIT.
   000608
   000609                    EXIT.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72j0td$l0l@sjx-ixn10.ix.netcom.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72inoq$1ub@sjx-ixn8.ix.netcom.com> <364ee4c8.8647469@netnews.worldnet.att.net>`

```

patbean@help.worldnet.att.net wrote in message
<364ee4c8.8647469@netnews.worldnet.att.net>...
>here is the entire program .. it is going to be written to three
>different reports ...  I was trying to post the parts that I thought
>were needed ....
>
>
   <program snipped>

A *cursory* glance at your program shows no obvious problems.  My
suggestions are:

A) Make certain that you have a SORTOUT DD allocated and look at what the
sort messages are.  (If you don't understand them, post them here)

B) Put a DISPLAY of the SORT-RETURN register (with a literal to tell you
where you are)
    Before and after the SORT statement
    Before and after each RELEASE statement
    Before and after each RETURN statement

Once you know exactly where the SORT is having its problem, it should help
you locate the problem.

P.S.  Does your college let you use any "interactive" debugger (such as
COBTEST, Xpediter, SmarTest, etc?).  If so, this too may help you.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 4)_

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3654dd0c.14974311@news3.ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72inoq$1ub@sjx-ixn8.ix.netcom.com> <364ee4c8.8647469@netnews.worldnet.att.net> <72j0td$l0l@sjx-ixn10.ix.netcom.com>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:


>
>B) Put a DISPLAY of the SORT-RETURN register (with a literal to tell you
…[4 more quoted lines elided]…
>

There's no point in doing this. SORT does not return intermediate
result codes. The SORT-RETURN special register is only set at the end
of the sort. The only valid reference to SORT RETURN during the sort
isthat a sort can be told to terminate at any time by using 
"MOVE 16 TO SORT-RETURN-CODE." 

		Scott Peterson.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364D9AD9.B980C3A0@ix.netcom.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72inoq$1ub@sjx-ixn8.ix.netcom.com> <364ee4c8.8647469@netnews.worldnet.att.net>`

```
There are several problems with the  program. First, at lines 466/467, if
the condition is not met, you will not process anything, then execution
will continue at line 484. Without seeing your data, this is the most
likely cause of your run-time error.

Your code is also processing your input file after & SORT-REC after EOF.
Basically, when you read/return a record, having reached end of file, your
record area is undefined. You then continue to use the record area. The
UNTIL THERE-ARE-NO-MORE-RECORDS will not be tested until the PERFORM
evaluates it. This is done either at the beginning (the default) or the
end (WITH TEST AFTER).
This change will correct this problem:
copy line 363 before 356 :
     000363                    PERFORM 125-READ-INPUT.
     000356                    PERFORM 120-PROCESS-IN-RECORD
     000357                        UNTIL THERE-ARE-NO-MORE-RECORDS.

move 363  after line 375.
Same issue in  310-VALIDATE-RECORD.

patbean@worldnet.att.net wrote:

> here is the entire program .. it is going to be written to three
> different reports ...  I was trying to post the parts that I thought
> were needed ....
> [snip]

>    000355
>    000356                    PERFORM 120-PROCESS-IN-RECORD
…[27 more quoted lines elided]…
>

> 000459                500-VALIDATE-AFTER-SORT SECTION.
>    000460
…[186 more quoted lines elided]…
>    000609                    EXIT.
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72iv9v$o91$1@juliana.sprynet.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
    Check the SORT-RETURN Special-Register at the start of your Output
Procedure for a non-zero value. If you've tested the RETURN-CODE
Special-Register before, you'll know the proper syntax. If I remember
correctly, a value of 16 indicates an unsuccessful Sort/Merge. Check the
appropriate manual for other non-zero values, their meanings and severity
levels. It looks like one aspect of this exercise is for the student to
react properly in an unsuccessful Sort scenario. If this were a Job Stream
with 100 steps and this error occurred during step 002, consider the impact
this could have on the next days business should the SORT-RETURN be
non-zero.

    FYI, the SORT-RETURN Special-Register in an IBM Mainframe environment is
actually the Register 15 value returned by DFSORT or some other third-party
Sort/Merge. RETURN-Code is also a value returned by a Called Sub-Program to
the Calling Program. Please note that although registers are inherently
4-bytes, both of the above Special-Registers are viewed by COBOL as 2-bytes,
halfword-binary.

    Good Luck....

WOB,
Atlanta

patbean@help.worldnet.att.net wrote in message
<364dd7d1.5327538@netnews.worldnet.att.net>...
>I am a college student taking advanced business programming ... my
>class has been working on the same program since the beginning of
>september and we are all getting the same error message and no one
>seems to be able to help us solve the problem ...

<Rest Snipped>
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** Frank Yaeger <fyaeger@ibm.net>
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364DBC06.1A823B75@ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72iv9v$o91$1@juliana.sprynet.com>`

```
WOB wrote:

>     Check the SORT-RETURN Special-Register at the start of your Output
>
…[6 more quoted lines elided]…
> levels.

Some comments from a DFSORT guy:

You can find all of the DFSORT return codes in "DFSORT Messages, Codes
and Diagnosis Guide", online at URL:

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/ICECM104/CCONTENTS

If you want to make sure you see the DFSORT messages from a COBOL
program, add the following to your JCL:

//SORTDIAG DD DUMMY
//DFSPARM DD *
   OPTION MSGDDN=MYOUT
/*
//MYOUT DD SYSOUT=*

SORTDIAG tells DFSORT to write all messages, including diagnostic
messages.  This makes sure the messages are written even if some other
parameter has been used to suppress them.

DFSPARM can be used to supply additional or overriding control
statements to DFSORT.  You can even overrride the SORT statement.  The
name DFSPARM may have been changed at your site via the ICEMAC MSGDDN
parameter.  You can use ICETOOL DEFAULTS to list all of your site's
defaults, including MSGDDN, as explained at URL:

http://www.storage.ibm.com/storage/software/sort/srtmadfl.htm

MSGDDN=MYOUT tells DFSORT to write its messages to MYOUT.  The default
for DFSORT's message data set name is SYSOUT, not SORTOUT as some people
have suggested.  SORTOUT is the default for DFSORT's output data set
name.    The  SYSOUT DD might also be used for COBOL messages, so using
the MSGDDN DD makes sure the DFSORT messages are separated from the
COBOL messages.  (If COBOL messages are not going to the SYSOUT DD, you
can just put in a SYSOUT DD and not use MSGDDN=name.)

MYOUT DD  will show the DFSORT messages.  If DFSORT passed RC=16 to the
calling program, you'll see an ICExxxA error message.  You can look it
up online in "DFSORT Messages, Codes and Diagnosis Guide" using the URL
above.

For more information about DFSORT, visit the DFSORT home page at URL:

http://www.ibm.com/storage/dfsort/

Frank Yaeger - DFSORT Team (Specialties: Y2K, Symbols, ICETOOL, OUTFIL
:-)
fyaeger@vnet.ibm.com
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

- **From:** Frank Yaeger <fyaeger@ibm.net>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364EE6C9.FC8CC16D@ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <72iv9v$o91$1@juliana.sprynet.com> <364DBC06.1A823B75@ibm.net>`

```
Frank Yaeger wrote:

> DFSPARM can be used to supply additional or overriding control
> statements to DFSORT.  You can even overrride the SORT statement.  The
…[5 more quoted lines elided]…
> http://www.storage.ibm.com/storage/software/sort/srtmadfl.htm

Oops.  That should read "PARMDDN" instead of "MSGDDN".  PARMDDN is the
parameter for changing the DFSPARM name. MSGDDN is the parameter for
changing the message data set name.  Sorry if I confused anyone.

Frank Yaeger - DFSORT Team (Specialties: Y2K, Symbols, ICETOOL, OUTFIL
:-)
fyaeger@vnet.ibm.com
DFSORT/MVS is on the World Wide Web at URL:
     http://www.ibm.com/storage/dfsort/
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** "Ryan Roberts" <ryanr@fgi.net>
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72lhui$qt8$1@supernews.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
Although I'm not sure if it will fix your problem, I find the placement of
your "close files" statement somewhat unusual.  With that in mind, I
recommend moving line 358 'perform 190-close files' to about line 344,
placing it just above your 'stop run' statement.  Although your program
should automatically handle opening and closing your sort file, your
placement of a "close files" statement in your input procedure may be
affecting the sort file.

Additionally, even though they're not listed below, I'll assume you have
properly used and placed your 'release' (to sort file) and 'return' (from
sort file) statements.  Be sure to check these.

-Ryan-
____________________
ryanr@fgi.net
____________________


patbean@help.worldnet.att.net wrote in message
<364dd7d1.5327538@netnews.worldnet.att.net>...
>I am a college student taking advanced business programming ... my
>class has been working on the same program since the beginning of
…[65 more quoted lines elided]…
>***************************************************************************
****************
>
> 000337                000-MAIN-CONTROL.
…[49 more quoted lines elided]…
>   000382
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** "Thane Hubbell" <redsky@ibm.net>
- **Date:** 1998-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be0f91$b7160220$99bc48a6@default>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```


patbean@help.worldnet.att.net wrote in article
<364dd7d1.5327538@netnews.worldnet.att.net>...
> I am a college student taking advanced business programming ... my
> class has been working on the same program since the beginning of
…[5 more quoted lines elided]…
> ....please take help out of address if you would like to email me...


Isn't it funny how these things come in GROUPS?   Wierd I say, WIERD!


This was JUST DISCUSSED in this group in detail.  The messages should still
be on your news server, but if not, go to dejanews.com and search for
SORT-RETURN in comp.lang.cobol.  

Wierd I tell you!  WIERD!
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** docdwarf@clark.net ()
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72q7ve$clv$1@callisto.clark.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <01be0f91$b7160220$99bc48a6@default>`

```
In article <01be0f91$b7160220$99bc48a6@default>,
Thane Hubbell <redsky@ibm.net> wrote:
>
>
…[12 more quoted lines elided]…
>Isn't it funny how these things come in GROUPS?   Wierd I say, WIERD!

Not too weird... professors tend to construct their courses along the same
lines, neh?

DD
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981115132604.07525.00000998@ng154.aol.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
patbean@help.worldnet.att.net
On 14 Nov 1998 01:34:46 GMT

posted
>>
I am a college student taking advanced business programming ... my
class has been working on the same program since the beginning of
september and we are all getting the same error message and no one
seems to be able to help us solve the problem ... ...
<<

Did you say "advanced"? I mean seriously! We are glad to help. Really! It IS a
privilege. 

But are you actually saying that you have a problem with an internal sort for
more than five weeks,and as a student in an 'advanced' class,  you can't even
begin to think of a way to get the stingy old machine to cough up as much as a
hint about the problem?

Well, okay then. Lets pretend. Let us assume that you have this kind of problem
in the real world. You take the source code to the nearest senior programmer.
What will she say?

We can only imagine, since all of this is so difficult. But she might say
something like, "You have I/O statements in this program. You have not coded
FILE STATUS for thosse files. Code FILE STATUS for those files.  After each I/O
statement, I know this is hard, ... I will help you, because I care, ... after
EACH, that is E-A-C-H I/O statement test the status code."

She may then proceed to add, "I am a busy person, but I will mention to you
that when I took INTRODUCTORY programming, they encouraged me to test the
status code after EACH I/O statement. ... this habit really helped when I moved
into those absolutely awesome rocket science access methods like SQLs, IMS and
CICS, ... I mean it was RAD, we could actually catch an error right there when
it happened, rather than later on when it would be confusing."

And she might add as she tossed the boring listing back at you, "OPEN is an I/O
statement. Check the status code aftrer every I/O statement. CLOSE is an I/O
statement. Check the status code after every I/O statement. Junior programmers
operate under the incredibly expensive assumption that coding status code
checks takes longer ... " there could then be the possibility that a light
would go on within your brain as she risisted filling the pause with derisive
laughter and adds ... "it is usually not a good idea to close a file twice." 

After such an encounter, it might be reasonable to believe that not all
problems were identified for you.  But it would be reasonable to believe that
you can find all I/O problems if you test the FILE STATUS after every I/O verb.
If you code a status code check after every I/O statement you write, you will
save a great deal of time. 

And naturally you should display (or dump to an error file) any unexpected
status code. The structure of a procedure division in COBOL is mostly just a
reflection of the file access relationships and I/O status code driven
exception handling.  The movement of the data and the manipulation of values is
minor work.

Business data processing is I/O processing. The shape and surface of the
procedure division is dominated by I/O status management. 

SORT and MERGE are I/O verbs.  A procedure division withou a check of
SORT-RETURN should be assumed to be an error,  until proven otherwise. A
procedure division with OPENs, READs, WRITEs, and CLOSEs which do not have
immediate status code checking, is not really worthy of review. Perhaps a
beginning student might beleive that is reasonable, but not a beginning
professional.  

So, do you want to look forward or backward at this 'advanced' stage? Think
about what you are doing.  It is like you are in your car, you have a problem
and you are not even willing to look at the instrument panel. I mean all those
lights and dials: Gosh that is rough stuff!

In a prefessional environment you can not wait five weeks to possibly, maybe
find some indicator readout.  When the problem happens, that day, that night,
that very minute, millions are at stake. You most resolve problems NOW, not
five weeks from now.

Exactly how is it, that you can have a teacher who allows you to think you are
doing something 'advanced', and you have not been instructed to test the status
codes? What is that?

It blows my mind! You have I/O statements and you are not even checking to see
that they work before you proceed. What did y'all do thar' in yer beginers'
class?

Before you advance to the PROCEDURE DIVISION, have a look at the ENVIRONMENT
DIVISION. It is part of a 'complete' program.

Hope your next five weeks are more enlightening.















Robert Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364f28a5.623716@news3.ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <19981115132604.07525.00000998@ng154.aol.com>`

```
On 15 Nov 1998 18:26:04 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:


>But are you actually saying that you have a problem with an internal sort for
>more than five weeks,and as a student in an 'advanced' class,  you can't even
>begin to think of a way to get the stingy old machine to cough up as much as a
>hint about the problem?
... the rest was snipped away

Robert,

thanks a lot - you DID hit the nail right on the head - You wrote exactly what I was
thinking....


with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72nenq$hue$1@news.igs.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <19981115132604.07525.00000998@ng154.aol.com>`

```
Come on now ... you know that correct academic methodology
involves changing the problem to fit the preconceived solution,
not the other way around ...

A properly designed course material program is *not* supposed
to work.  It is supposed to make it appear that business does not
know what it is doing, so that the professor can get a grant to
solve the problem that s/he just invented.

RKRayhawk wrote in message <19981115132604.07525.00000998@ng154.aol.com>...
>patbean@help.worldnet.att.net
>On 14 Nov 1998 01:34:46 GMT
…[9 more quoted lines elided]…
>Did you say "advanced"? I mean seriously! We are glad to help. Really! It
IS a
>privilege.
>
>But are you actually saying that you have a problem with an internal sort
for
>more than five weeks,and as a student in an 'advanced' class,  you can't
even
>begin to think of a way to get the stingy old machine to cough up as much
as a
>hint about the problem?
>
>Well, okay then. Lets pretend. Let us assume that you have this kind of
problem
>in the real world. You take the source code to the nearest senior
programmer.
>What will she say?
>
>We can only imagine, since all of this is so difficult. But she might say
>something like, "You have I/O statements in this program. You have not
coded
>FILE STATUS for thosse files. Code FILE STATUS for those files.  After each
I/O
>statement, I know this is hard, ... I will help you, because I care, ...
after
>EACH, that is E-A-C-H I/O statement test the status code."
>
>She may then proceed to add, "I am a busy person, but I will mention to you
>that when I took INTRODUCTORY programming, they encouraged me to test the
>status code after EACH I/O statement. ... this habit really helped when I
moved
>into those absolutely awesome rocket science access methods like SQLs, IMS
and
>CICS, ... I mean it was RAD, we could actually catch an error right there
when
>it happened, rather than later on when it would be confusing."
>
>And she might add as she tossed the boring listing back at you, "OPEN is an
I/O
>statement. Check the status code aftrer every I/O statement. CLOSE is an
I/O
>statement. Check the status code after every I/O statement. Junior
programmers
>operate under the incredibly expensive assumption that coding status code
>checks takes longer ... " there could then be the possibility that a light
>would go on within your brain as she risisted filling the pause with
derisive
>laughter and adds ... "it is usually not a good idea to close a file
twice."
>
>After such an encounter, it might be reasonable to believe that not all
>problems were identified for you.  But it would be reasonable to believe
that
>you can find all I/O problems if you test the FILE STATUS after every I/O
verb.
>If you code a status code check after every I/O statement you write, you
will
>save a great deal of time.
>
>And naturally you should display (or dump to an error file) any unexpected
>status code. The structure of a procedure division in COBOL is mostly just
a
>reflection of the file access relationships and I/O status code driven
>exception handling.  The movement of the data and the manipulation of
values is
>minor work.
>
…[11 more quoted lines elided]…
>about what you are doing.  It is like you are in your car, you have a
problem
>and you are not even willing to look at the instrument panel. I mean all
those
>lights and dials: Gosh that is rough stuff!
>
>In a prefessional environment you can not wait five weeks to possibly,
maybe
>find some indicator readout.  When the problem happens, that day, that
night,
>that very minute, millions are at stake. You most resolve problems NOW, not
>five weeks from now.
>
>Exactly how is it, that you can have a teacher who allows you to think you
are
>doing something 'advanced', and you have not been instructed to test the
status
>codes? What is that?
>
>It blows my mind! You have I/O statements and you are not even checking to
see
>that they work before you proceed. What did y'all do thar' in yer beginers'
>class?
>
>Before you advance to the PROCEDURE DIVISION, have a look at the
ENVIRONMENT
>DIVISION. It is part of a 'complete' program.
>
…[18 more quoted lines elided]…
>
```

#### ↳ Re: SORT-RETURN not referenced

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0jK32.4101$FY5.10858514@storm.twcol.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net>`

```
From what it looks like you simply have and error with your sort.

Due to what I perceive as complexity in your program I recommend the
following:

1) Verify all DDNAMEs manually. This probably isnt the problem...but if
COBOL references a DD which is not defined in the JCL it will dynamically
allocate a temp DDNAME and DSN which will delete itself after the JCL/PROC
step completes.

2) Place a display statements after each paragraph label. Run program.
Manually follow code through program. 9 times out of 10 this solves problems
for me.

3) if possible, convert sort to an externale sort. EXTRACT FILTER SORT
REPORT. 4 STEPS TO EASIER PROGRAMMING.
- step 1 should extract all information into a flat file with little or no
selection criteria rformatting as necessary, usually COBOL program.
- step 2 should filter off uneeded information, typically I use SORT
- step 3 should sort the information into the order(s) you need
- step 4 should generate a report. simple reports can be done with sort,
more complex would use COBOL or EZtrieve or DYL280
****see DFSORT/SYNCSORT manual referencing SECTIONS/HEADER/TRAILER
statements for reporting. See OUTFIL statement for generating more than 1
report from 1 input file


I am not trying to be insulting, just trying to help simplify the problem.
```

##### ↳ ↳ Re: SORT-RETURN not referenced

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364f843b.4703513@news3.ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com>`

```
"Jeff" <a@a.com> wrote:


>3) if possible, convert sort to an externale sort. EXTRACT FILTER SORT
>REPORT. 4 STEPS TO EASIER PROGRAMMING.
…[5 more quoted lines elided]…
>more complex would use COBOL or EZtrieve or DYL280

I don't think this suggestion is doing anyone a favor. There is no
'programming efficiency' in parsing data 4 times to extract and
produce a report. This approach was generally used either by people
who didn't trust COBOL sorts (often justified back in COBOL "D" or "F"
days) or were extremely limited on memory. Then the tradeoff was
sometimes justified. 

In any version of IBM COBOL later than VS-COBOL the I/O efficiency is
so much better for a COBOL SORT  that with any significant amount of
data this read/write/read/write/read/write/read/report that you
suggest is simply wasteful. Worst case, do the extract and sort in one
step and then the reporting if you want to use a different
language...or write the whole thing using E15/E35 sort exits and let
sort do most of the work for you. All you have to write is a couple
little subroutines. 

                            Scott Peterson
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8C242.4342$FY5.11548957@storm.twcol.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net>`

```

>
>I don't think this suggestion is doing anyone a favor. There is no
>'programming efficiency' in parsing data 4 times to extract and


Nowhere did I say it was more efficient. Efficiency is needed on slow
computers with limited memory. IBM mainframes are neither of these.

I said simpler because obviously these ADVANCED COBOL students were having
serious problems. When a problem becomes too complex ONE SUGGESTED way of
solving it is to simplify the program.

>In any version of IBM COBOL later than VS-COBOL the I/O efficiency is
>so much better for a COBOL SORT  that with any significant amount of
>data this read/write/read/write/read/write/read/report that you
>suggest is simply wasteful. Worst case, do the extract and sort in one
>step and then the reporting if you want to use a different

I often combine the extract and the sort, but I was trying to simplify the
problem, not complicate it. All of these steps could be written in COBOL and
all with small easily maintained and easily understood programs.

>language...or write the whole thing using E15/E35 sort exits and let
>sort do most of the work for you. All you have to write is a couple
>little subroutines.


When talking about waste and efficiency you have to remember that the work
at some point in the future must be completed. That is the project must end
with a functional, not necessarily 100% efficient. I agree my process may be
inefficient, but once the basic procedures are broken down to their basics
they are much easier to develop, maintain, and implement. This is what we
are supposed to do.

The question was to help find a solution to a problem. Critiquing my
suggestion does not help solve the problem. Obviously you are more concerned
with criticizing my style rather than solving the problem.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 4)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uIs$vqcE#GA.153@upnetnews03>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net> <8C242.4342$FY5.11548957@storm.twcol.com>`

```

Jeff wrote in message <8C242.4342$FY5.11548957@storm.twcol.com>...
>
>>
…[18 more quoted lines elided]…
>problem, not complicate it. All of these steps could be written in COBOL
and
>all with small easily maintained and easily understood programs.
>
…[7 more quoted lines elided]…
>with a functional, not necessarily 100% efficient. I agree my process may
be
>inefficient, but once the basic procedures are broken down to their basics
>they are much easier to develop, maintain, and implement. This is what we
…[3 more quoted lines elided]…
>suggestion does not help solve the problem. Obviously you are more
concerned
>with criticizing my style rather than solving the problem.
>

Learning from constructive criticism should be one of the primary goals of
the c.l.c. newsgroup.  One of the benefits of a properly organized design
and development process should be some measure of refinement and
simplification of the initial project design outline. Some rookie COBOL
programmers (and there do seem to be more and more of them lately) regularly
lurking in this ng might seize upon your outline of one possible solution as
an itemized gospel of the way these things MUST or SHOULD be done.  Reading
later rebuttals, refinements and philosophical discussions on a particular
problem in a given thread can lead to expanded thinking and better
programming practices among the regular lurkers here in c.l.c.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 4)_

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365e79f7.24391983@news3.ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net> <8C242.4342$FY5.11548957@storm.twcol.com>`

```
"Jeff" <a@a.com> wrote:

>

>Nowhere did I say it was more efficient. Efficiency is needed on slow
>computers with limited memory. IBM mainframes are neither of these.
>
Bad programming practices are bad programming practices. I've  spent
far too much time helping programmers unlearn techniques learned when
people trained on a couple of hundred records and then used the same
techniques on a million plus records.  

>I said simpler because obviously these ADVANCED COBOL students were having
>serious problems. When a problem becomes too complex ONE SUGGESTED way of
>solving it is to simplify the program.
>

Another is to examine the environment and read the error messages
before rewriting the program. 

>
>When talking about waste and efficiency you have to remember that the work
…[5 more quoted lines elided]…
>

Within reason. However, I challenge the idea that in the hands of a
competent programmer that your methodology would truly be easier to
develop, maintain or implement.  It may harken back to some of the old
modular programming ideas, but maintainability is more a function of
lines of code than anything else. 

>The question was to help find a solution to a problem. Critiquing my
>suggestion does not help solve the problem. Obviously you are more concerned
>with criticizing my style rather than solving the problem.
>

As stated above, the concern should be with debugging methodology
rather than redesign. There are apparently a couple of logic errors in
the original program, combined with a severe lack of knowledge of sort
workings. Neither requires your approach for resolution.  In fact,
your approach ignores the problem by coding around it rather than
resolving it.

As far as criticizing your style, it deserved criticism.  Deal with
it. 

			Scott Peterson
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 5)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OMM42.283$QZ5.168345@storm.twcol.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net> <8C242.4342$FY5.11548957@storm.twcol.com> <365e79f7.24391983@news3.ibm.net>`

```
>Bad programming practices are bad programming practices. I've  spent
>far too much time helping programmers unlearn techniques learned when
>people trained on a couple of hundred records and then used the same
>techniques on a million plus records.

I regulary use this method on hundreds of thousands of records with
significant decease in CPU usage when compared to internal sorts. I have
developed this over several years in the work place. Granted there may be
better ways of doing this but I am not familiar with them.

If you are referring to their style...that is another story.


>Another is to examine the environment and read the error messages
>before rewriting the program.
>


I did examine error messages, but without data files and JCL error messages
don't get you very far.

>As stated above, the concern should be with debugging methodology
>rather than redesign. There are apparently a couple of logic errors in
…[3 more quoted lines elided]…
>resolvig it.

The first 2 suggestions were based on DEBUGGING METHODOLOGY within the
information that was given. I have never tried to rewrite a program in this
manner. But the program they wrote and most of the programs I have ever
worked on are very different. They obviously have alot of time to waste and
suggesting a rewrite when you have the time is often a better solution.

Without seeing the data files, JCL, and knowing the specifics of the rest of
the job process these were the geusses I gave. Having these things makes a
problem such as this much easier to solve. Specifically using display
statements, if a dbugger is not available. I fully expected one of the first
two suggestions to solve the problem. Rewriting an entire program is clearly
a last resort. I simply suggested a process which has proven time and time
again the shortest and easiest way for me to develop a report generating
program.

I may have overemphasised it as the EASIEST, maybe I should have said
EASIEST time and time agin for me to program a report generating program.

>
>As far as criticizing your style, it deserved criticism.  Deal with
>it.


If you offerred constructive criticism I would agree, but there is little
constructive criticism in your comments. Just ridicule. Anyone can ridicule
anothers work. Offer a better solution or don't say anything at all.

Obviously you think you had a better solution, but you failed to offer it.
Your other posting simply criticized anothers suggetion.

So what would you suggest they do?
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 6)_

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3654a32f.3836977@news3.ibm.net>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net> <8C242.4342$FY5.11548957@storm.twcol.com> <365e79f7.24391983@news3.ibm.net> <OMM42.283$QZ5.168345@storm.twcol.com>`

```
"Jeff" <a@a.com> wrote:

>I regulary use this method on hundreds of thousands of records with
>significant decease in CPU usage when compared to internal sorts. I have
>developed this over several years in the work place. Granted there may be
>better ways of doing this but I am not familiar with them.
>

There are many other measures than CPU usage. In fact,by itself, it's
very misleading. You need to look at a number of measures. But
regardless of your claim above, there is no way that passing the data
four times with COBOL I/O routines feeding an external sort will match
the efficiency of one pass of the data with an internal sort unless
the number of records is minimal.

>
>I did examine error messages, but without data files and JCL error messages
>don't get you very far.
>
I did and other people did find enough to make suggestions...and I
wasn't referring to JCL error messages. I was referring to SORT error
messages which were included. 

>
>The first 2 suggestions were based on DEBUGGING METHODOLOGY within the
>information that was given. I have never tried to rewrite a program in this
>manner. 

Not a good one from any viewpoint I've ever seen.

>But the program they wrote and most of the programs I have ever
>worked on are very different. They obviously have alot of time to waste and
…[10 more quoted lines elided]…
>

There is a need for external sort at times. But the reaons for those
are primarily based on limited resources (as previously mentioned). I
will tontinue to disagree with you that this is an appropriate
generalized way to develop code in the late ninties.  

>I may have overemphasised it as the EASIEST, maybe I should have said
>EASIEST time and time agin for me to program a report generating program.
>
That's a different issue. Lots of times reports are better generated
in a different language. But that doesn't force the use of an external
sort. To me, this sounds like someone who found a technique that works
and just uses it over and over regardless of applicability. 

>
>
…[8 more quoted lines elided]…
>
The first suggestions I would have made have already been suggested.by
others. Fix the logic errors and then see what happens. Their
fundamental concept is not in error. 

Second, the point of what I wrote was not adddressed to their problems
but to the problems I see in your proposed solution which I regard as
even more incorrect. Display statements are one thing, but the rest,
no way. 

			Scott Peterson
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

_(reply depth: 7)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UD452.48$NF5.240662@storm.twcol.com>`
- **References:** `<364dd7d1.5327538@netnews.worldnet.att.net> <0jK32.4101$FY5.10858514@storm.twcol.com> <364f843b.4703513@news3.ibm.net> <8C242.4342$FY5.11548957@storm.twcol.com> <365e79f7.24391983@news3.ibm.net> <OMM42.283$QZ5.168345@storm.twcol.com> <3654a32f.3836977@news3.ibm.net>`

```

>That's a different issue. Lots of times reports are better generated
>in a different language. But that doesn't force the use of an external
>sort. To me, this sounds like someone who found a technique that works
>and just uses it over and over regardless of applicability.


Once again you are stretching what I said into one more ridicule. Saying a
process works for me time and again never implies that I use it "over and
over regardless of applicability. Any descent programmer finds things which
work and uses them. To be successful you have to know when to use what
technique. You have stretched my general technique into a strict policy
which I would never recommend. No set process works for every situation in
programming. All situations are slightly different. A good programmer knows
when to stop making generalizations and look at the details and figure out
what is the best way given a particular situation, regardles of what is his
or her favorite way of doing things.
```

###### ↳ ↳ ↳ Re: SORT-RETURN not referenced

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981116145338.04161.00001517@ng155.aol.com>`
- **References:** `<364f843b.4703513@news3.ibm.net>`

```

Okay, Class. 
Class.
Class!!!!

Now it is agreed, we will use advanced COBOL, EZtrieve as well as DYL280, and
naturally there will be an external sort with full exploitation of Exit Fifteen
and Exit Thrity-Five on your final exam. But now ...

Now a pop quiz!

We have an external sorts, that's right, sort_s plural, jammed between two
pairs of COBOL programs.  SORT#1 must transform a fixed length input file to a
variable length output file, and SORT#2 has to transform a variable length
input file to a fixed length output file.

Got it?! Good!!!!  Now for extra credit why is one more advanced than the
other?

Worst Wishes, 


Robert Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
