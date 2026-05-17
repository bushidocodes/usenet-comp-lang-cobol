[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Finding Variable-Length Record Length

_8 messages · 6 participants · 1998-09_

---

### Finding Variable-Length Record Length

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-09-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`

```


Is there any way to determine the length of a variable length input
record in COBOL without using any Assembler calls?

A colleague has the task of converting a PL/I program which does a
rather simple record selection. But he does not know the file
contents well enough to write the selected records to the correct
size. (I agree he *should* but...)

Any ideas appreciated.
```

#### ↳ Re: Finding Variable-Length Record Length

- **From:** "fujitsu software" <ua-author-6589312@usenetarchives.gap>
- **Date:** 1998-09-04T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ec791d7a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`

```
Paul,

The following should provide you with a sample program to customize:

000010*****************************************************************
000020*
000030* Copyright (c) 1998 Fujitsu Software Corporation.
000040*
000050* All rights reserved. No part of this program or publication
000060* may be reproduced, transmitted, transcribed, stored in a
000070* retrieval system, or translated into any language or computer
000080* language, in any form or by any means, electronic, mechanical,
000090* magnetic, optical, chemical, manual or otherwise, without the
000100* prior written permission of:
000110*
000120* Fujitsu Software Corporation
000130* Developer Tools Group
000140* 3055 Orchard Drive
000150* San Jose, California 95134-2022, United States
000160* Phone: (408) 428-0500
000170* FAX: (408) 428-0600
000180* EMAIL: co··.@adt··s.com
000190*
000200*
000210* Source Module: SEQCOPY.CBL
000220*
000230* Last Modified: 12 February 1998
000240*
000250* Author: TAY
000260*
000270* Change Log
000280*
000290*****************************************************************
000300
000310 IDENTIFICATION DIVISION.
000320 PROGRAM-ID. SEQCOPY.
000330 AUTHOR. Todd A. Yancey 02/10/98.
000340 INSTALLATION. Fujitsu COBOL (Generic).
000350 SECURITY. Copyright (C) 1998 Fujitsu Software Corporation.
000360
000370*-----------------------------------------------------------------
000380 ENVIRONMENT DIVISION.
000390 CONFIGURATION SECTION.
000400 SOURCE-COMPUTER. Fujitsu.
000410 OBJECT-COMPUTER. Fujitsu.
000420
000430 INPUT-OUTPUT SECTION.
000440 FILE-CONTROL.
000450 SELECT INPUT-LINE-SEQUENTIAL-FILE
000460 ASSIGN TO INPUT-FILENAME
000470 ORGANIZATION LINE SEQUENTIAL
000480 FILE STATUS IS FILE-STATUS.
000490
000500 SELECT OUTPUT-LINE-SEQUENTIAL-FILE
000510 ASSIGN TO OUTPUT-FILENAME
000520 ORGANIZATION LINE SEQUENTIAL
000530 FILE STATUS IS FILE-STATUS.
000540
000550*-----------------------------------------------------------------
000560 DATA DIVISION.
000570
000580 FILE SECTION.
000590
000600 FD INPUT-LINE-SEQUENTIAL-FILE
000610 RECORD IS VARYING IN SIZE DEPENDING ON INPUT-RECORD-LENGTH.
000620 01 INPUT-RECORD PIC X(128).
000630
000640 FD OUTPUT-LINE-SEQUENTIAL-FILE
000650 RECORD IS VARYING IN SIZE DEPENDING ON OUTPUT-RECORD-LENGTH.
000660 01 OUTPUT-RECORD PIC X(128).
000670
000680
000690 WORKING-STORAGE SECTION.
000700
000710 77 VAL-FALSE PIC 9(4) COMP VALUE ZERO.
000720 77 VAL-TRUE PIC 9(4) COMP VALUE 1.
000730
000740 *> File I/O Operators
000750 77 VAL-OPEN PIC X(4) VALUE "OPEN".
000760 77 VAL-CLOSE PIC X(5) VALUE "CLOSE".
000770 77 VAL-READ PIC X(4) VALUE "READ".
000780 77 VAL-WRITE PIC X(5) VALUE "WRITE".
000790 77 VAL-REWRITE PIC X(7) VALUE "REWRITE".
000800 77 VAL-DELETE PIC X(6) VALUE "DELETE".
000810
000820 01 INPUT-FILENAME PIC X(256) VALUE SPACES.
000830 01 INPUT-RECORD-LENGTH PIC 9(4) COMP VALUE ZERO.
000840 01 INPUT-FILE-ACTION PIC X(7) VALUE "CLOSE".
000850 01 INPUT-FILE-STATUS PIC 9(4) COMP VALUE ZERO.
000860 88 INPUT-FILE-AT-END VALUE 1.
000870
000880 01 OUTPUT-FILENAME PIC X(256) VALUE SPACES.
000890 01 OUTPUT-RECORD-LENGTH PIC 9(4) COMP VALUE ZERO.
000900 01 OUTPUT-FILE-ACTION PIC X(7) VALUE "CLOSE".
000910
000920 01 FILE-STATUS.
000930 88 IO-SUCCESSFUL VALUE "00".
000940 88 END-OF-FILE VALUE "10".
000950 88 FILE-NOT-FOUND VALUE "35".
000960 05 FILE-STATUS-1 PIC X VALUE ZERO.
000970 05 FILE-STATUS-2 PIC X VALUE ZERO.
000980
000990*-----------------------------------------------------------------
001000 PROCEDURE DIVISION.
001010
001020 DISPLAY "Fujitsu COBOL Copy File Sample"
001030 DISPLAY SPACES
001040
001050 *> Create INPUT/OUTPUT Files Names
001060 MOVE "OUTFILE.SEQ" TO OUTPUT-FILENAME
001070 MOVE "INFILE.SEQ" TO INPUT-FILENAME
001080
001090 PERFORM OPEN-INPUT-SEQUENTIAL-FILE
001100 PERFORM OPEN-OUTPUT-SEQUENTIAL-FILE
001110
001120 PERFORM UNTIL INPUT-FILE-AT-END
001130 PERFORM READ-INPUT-SEQUENTIAL-FILE
001140 IF NOT INPUT-FILE-AT-END
001150 MOVE INPUT-RECORD TO OUTPUT-RECORD
001160 MOVE INPUT-RECORD-LENGTH TO OUTPUT-RECORD-LENGTH
001170 PERFORM WRITE-OUTPUT-SEQUENTIAL-FILE
001180 END-IF
001190 END-PERFORM
001200
001210 PERFORM CLOSE-OUTPUT-SEQUENTIAL-FILE
001220 PERFORM CLOSE-INPUT-SEQUENTIAL-FILE
001230
001240 DISPLAY "Copy Complete".
001250
001260
001270 EXIT PROGRAM.
001280
001290
001300*-----------------------------------------------------------------
001310 OPEN-INPUT-SEQUENTIAL-FILE.
001320
001330 IF INPUT-FILE-ACTION = VAL-CLOSE
001340 OPEN INPUT INPUT-LINE-SEQUENTIAL-FILE WITH LOCK
001350 END-IF
001360 IF FILE-STATUS = ZERO
001370 MOVE VAL-OPEN TO INPUT-FILE-ACTION
001380 MOVE VAL-FALSE TO INPUT-FILE-STATUS
001390 ELSE
001400 DISPLAY "ERROR: Opening Input File"
001410 END-IF.
001420
001430
001440*-----------------------------------------------------------------
001450 OPEN-OUTPUT-SEQUENTIAL-FILE.
001460
001470 IF OUTPUT-FILE-ACTION = VAL-CLOSE
001480 OPEN OUTPUT OUTPUT-LINE-SEQUENTIAL-FILE WITH LOCK
001490 END-IF
001500 IF FILE-STATUS = ZERO
001510 MOVE VAL-OPEN TO OUTPUT-FILE-ACTION
001520 ELSE
001530 DISPLAY "ERROR: Opening Output File"
001540 END-IF.
001550
001560
001570*-----------------------------------------------------------------
001580 CLOSE-INPUT-SEQUENTIAL-FILE.
001590
001600 IF INPUT-FILE-ACTION NOT = VAL-CLOSE
001610 CLOSE INPUT-LINE-SEQUENTIAL-FILE
001620 MOVE VAL-CLOSE TO INPUT-FILE-ACTION
001630 END-IF.
001640
001650
001660*-----------------------------------------------------------------
001670 CLOSE-OUTPUT-SEQUENTIAL-FILE.
001680
001690 IF OUTPUT-FILE-ACTION NOT = VAL-CLOSE
001700 CLOSE OUTPUT-LINE-SEQUENTIAL-FILE
001710 MOVE VAL-CLOSE TO OUTPUT-FILE-ACTION
001720 END-IF.
001730
001740
001750*-----------------------------------------------------------------
001760 READ-INPUT-SEQUENTIAL-FILE.
001770
001780 IF NOT INPUT-FILE-AT-END
001790 READ INPUT-LINE-SEQUENTIAL-FILE
001800 AT END
001810 SET INPUT-FILE-AT-END TO TRUE
001820 MOVE SPACES TO INPUT-RECORD
001830 END-READ
001840 *> Replace all TAB bytes (x'09) in the INPUT-RECORD
001850 INSPECT INPUT-RECORD REPLACING ALL X"09" BY SPACE
001860 END-IF.
001870
001880
001890*-----------------------------------------------------------------
001900 WRITE-OUTPUT-SEQUENTIAL-FILE.
001910
001920 *> Find Last Non-space character
001930 MOVE FUNCTION LENG( OUTPUT-RECORD )
001940 TO OUTPUT-RECORD-LENGTH
001950 PERFORM UNTIL OUTPUT-RECORD( OUTPUT-RECORD-LENGTH : 1 )
001960 NOT = SPACE
001970 OR OUTPUT-RECORD-LENGTH = 1
001980 SUBTRACT 1 FROM OUTPUT-RECORD-LENGTH
001990 END-PERFORM
002000 WRITE OUTPUT-RECORD
002010 IF FILE-STATUS NOT = ZERO
002020 DISPLAY "ERROR: Writing Output File"
002030 END-IF.
002040
002050*-----------------------------------------------------------------
002060 END PROGRAM SEQCOPY.
002070*-----------------------------------------------------------------

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: http://www.adtools.com


Paul Knudsen wrote in message <35f··.@new··m.net>...
› 
› 
…[8 more quoted lines elided]…
› Any ideas appreciated.
```

##### ↳ ↳ Re: Finding Variable-Length Record Length

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-09-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ec791d7a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1ec791d7a-p2@usenetarchives.gap>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net> <gap-d1ec791d7a-p2@usenetarchives.gap>`

```
Thanks Todd, but I should have mentioned that this is for MVS COBOL
II. I don't think the input-record-length is provided there (but
will check when I'm back in the office on Tuesday).


On Sat, 5 Sep 1998 04:45:39 -0700, "Fujitsu Software"
wrote:

› Paul,
›
› The following should provide you with a sample program to customize:
```

###### ↳ ↳ ↳ Re: Finding Variable-Length Record Length

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-09-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ec791d7a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1ec791d7a-p3@usenetarchives.gap>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net> <gap-d1ec791d7a-p2@usenetarchives.gap> <gap-d1ec791d7a-p3@usenetarchives.gap>`

```
Use the NOCMPR2 compiler option and then

FD ....
Record Varying in Size depending on ...

Is most CERTAINLY supported by VS COBOL II (any release after Release 3.0).

(Also it is supported by the newer IBM compilers as well - as it is a part
of the ANS'85 Standard)

Paul Knudsen wrote in message <35f··.@new··m.net>...
› Thanks Todd, but I should have mentioned that this is for MVS COBOL
› II.   I don't think the input-record-length is provided there (but
…[9 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Finding Variable-Length Record Length

_(reply depth: 4)_

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-09-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ec791d7a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1ec791d7a-p4@usenetarchives.gap>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net> <gap-d1ec791d7a-p2@usenetarchives.gap> <gap-d1ec791d7a-p3@usenetarchives.gap> <gap-d1ec791d7a-p4@usenetarchives.gap>`

```
Well thanks, Bill! My colleague and manager will be pleased.


On Sun, 6 Sep 1998 13:30:33 -0500, "William M. Klein"
wrote:

› Use the NOCMPR2 compiler option and then
› 
…[6 more quoted lines elided]…
› of the ANS'85 Standard)
```

#### ↳ Re: Finding Variable-Length Record Length

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ExXi45TkedGY@Dwight_Miller.iix.com>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`

```
On Sat, 5 Sep 1998 16:34:27, Paul_Knudsen@ibm.net (Paul Knudsen) 
wrote:

> 
> 
…[8 more quoted lines elided]…
> Any ideas appreciated.


Function Length
```

#### ↳ Re: Finding Variable-Length Record Length

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1998-09-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ec791d7a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`
- **References:** `<35f56717.5477962@news-s01.ny.us.ibm.net>`

```
Assuming both input and output files have variable length records, the files
should be described in the FD's as RECORD VARYING DEPENDING ON INPUT-SIZE and
RECORD VARYING DEPENDING ON OUTPUT-SIZE where INPUT-SIZE and OUTPUT-SIZE are
PIC 9(9) BINARY working storage fields. When a record is selected move
INPUT-SIZE to OUTPUT-SIZE and then WRITE OUTPUT-RECORD FROM INPUT-RECORD (1 :
INPUT-SIZE)

›  
› On Sat, 5 Sep 1998 16:34:27, Pau··.@i··.net (Paul Knudsen)  
…[16 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at mor··.@nbn··b.ca
```

#### ↳ Re: Finding Variable-Length Record Length

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tk60v$4m1$1@garnet.nbnet.nb.ca>`
- **References:** `<Jl0PnHJ5PvPd-pn2-ExXi45TkedGY@Dwight_Miller.iix.com> <35f56717.5477962@news-s01.ny.us.ibm.net>`

```
Assuming both input and output files have variable length records, the files   
should be described in the FD's as RECORD VARYING DEPENDING ON INPUT-SIZE and   
RECORD VARYING DEPENDING ON OUTPUT-SIZE where INPUT-SIZE and OUTPUT-SIZE are   
PIC 9(9) BINARY working storage fields.  When a record is selected move   
INPUT-SIZE to OUTPUT-SIZE and then WRITE OUTPUT-RECORD FROM INPUT-RECORD (1 :   
INPUT-SIZE)  
 
>  
> On Sat, 5 Sep 1998 16:34:27, Paul_Knudsen@ibm.net (Paul Knudsen)  
…[16 more quoted lines elided]…
> 

Clark F. Morris, Jr. 
CFM Technical Programming Services 
Bridgetown, Nova Scotia, Canada 
cmorris@fox.nstn.ca 
on assignment at morrisc@nbnet.nb.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
