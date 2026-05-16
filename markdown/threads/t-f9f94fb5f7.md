[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to call Btrieve Funktion in FSC V3

_7 messages · 4 participants · 1998-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to call Btrieve Funktion in FSC V3

- **From:** TKS-Schmitteck@t-online.de (Paul Schmitteck)
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t07jq$ekg$2@news02.btx.dtag.de>`

```
Hello Everybody,
       I have a question.. I have an application which uses brieve
functions via "_BTRV" requester supplied by MicroFocus cobol. Now we are
converting the program from MicroFocus Cobol to Fujitsu Cobol 3.0. 

Can anybody help me know how to call btrieve functions for accessing the
files in btrieve from the Windows environment ? Please include a sample
program if it is possible. It is very Urgent.

Thanks.
PAUL SCHMITTECK.
```

#### ↳ Re: How to call Btrieve Funktion in FSC V3

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t13v0$8g0$1@news01.btx.dtag.de>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de>`

```
Paul Schmitteck schrieb:

> Hello Everybody,
>        I have a question.. I have an application which uses brieve
…[11 more quoted lines elided]…
> PAUL SCHMITTECK.

   You don't have to...

just write in your SELECT-clause the file-name (like ART.BTR) a comma
and the word BTRV (...ART.BTR,BTRV) and the file is a BTRIEVE-file,
nice, uhh (if you whant the same in MF, try my BTRV.EXE, a file-handler
for MF-Cobol using BTRIEVE)
```

##### ↳ ↳ Re: How to call Btrieve Funktion in FSC V3

- **From:** TKS-Schmitteck@t-online.de (Paul Schmitteck)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t2iqg$dmn$1@news00.btx.dtag.de>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de> <6t13v0$8g0$1@news01.btx.dtag.de>`

```
Sorry
in our program there isï¿½nt a SELECT Clause.

How can i use the btrieve functions:

get position
get direct
create supplement index
get version

using a Select clause?

TIA Paul
```

###### ↳ ↳ ↳ Re: How to call Btrieve Funktion in FSC V3

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t2mh5$aqm$3@news02.btx.dtag.de>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de> <6t13v0$8g0$1@news01.btx.dtag.de> <6t2iqg$dmn$1@news00.btx.dtag.de>`

```
Paul Schmitteck schrieb:

> Sorry
> in our program there isï¿½nt a SELECT Clause.
…[10 more quoted lines elided]…
> TIA Paul

   Ohh, that doesn't work, you have to code an DLL-File
that will call by your routine but...

why do you need "GET DIRECT" or "GET POSITION"
in a cobol-environment??????

I think you only need it to reorganize the file!
(or, at a special reason an create supplemental,
you can do it by calling BUTIL -SINDEX ...
via the EXECute shell)

regards

Andreas Strzoda
```

###### ↳ ↳ ↳ Re: How to call Btrieve Funktion in FSC V3

_(reply depth: 4)_

- **From:** TKS-Schmitteck@t-online.de (Paul Schmitteck)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t30lb$fq4$1@news00.btx.dtag.de>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de> <6t13v0$8g0$1@news01.btx.dtag.de> <6t2iqg$dmn$1@news00.btx.dtag.de> <6t2mh5$aqm$3@news02.btx.dtag.de>`

```
with get direkt you need only a 4 byte pointer to read a record again. We
store this 4 byte pointer into an array.

Andreas Strzoda schrieb in Nachricht <6t2mh5$aqm$3@news02.btx.dtag.de>...
>Paul Schmitteck schrieb:
>
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: How to call Btrieve Funktion in FSC V3

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mvbJ1.511$cE5.718189@news2.mia.bellsouth.net>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de> <6t13v0$8g0$1@news01.btx.dtag.de> <6t2iqg$dmn$1@news00.btx.dtag.de> <6t2mh5$aqm$3@news02.btx.dtag.de>`

```
Andreas Strzoda wrote:
>Paul Schmitteck schrieb:
>
…[18 more quoted lines elided]…
>in a cobol-environment??????


You need it to avoid excess index searching when accessing a record,
accessing other records, then re-accessing the first record.  In some
contexts, saving off the direct key to get back to a record can make
a very large difference in speed of execution.
```

#### ↳ Re: How to call Btrieve Funktion in FSC V3

- **From:** "Fujitsu Software" <cobol@adtools.com>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t3qae$kpr$1@nntp2.ba.best.com>`
- **References:** `<6t07jq$ekg$2@news02.btx.dtag.de>`

```
Paul,

The following provides a sample for calling Btrieve functions from Fujitsu
COBOL on 32-bit Windows 95/98/NT:

000010*****************************************************************
000020*
000030*  Copyright (c) 1998 Fujitsu Software Corporation.
000040*
000050*  All rights reserved.  No part of this program or publication
000060*  may be reproduced, transmitted, transcribed, stored in a
000070*  retrieval system, or translated into any language or computer
000080*  language, in any form or by any means, electronic, mechanical,
000090*  magnetic, optical, chemical, manual or otherwise, without the
000100*  prior written permission of:
000110*
000120*  Fujitsu Software Corporation
000130*  Developer Tools Group
000140*  3055 Orchard Drive
000150*  San Jose, California 95134-2022, United States
000160*  Phone: (408) 428-0500
000170*  FAX:   (408) 428-0600
000180*  EMAIL: cobol@adtools.com
000190*
000200*
000210*  Source Module: FJ2BTRV.CBL
000220*
000230*  Last Modified: 26 February 1998
000240*
000250*  Author:  TAY
000260*
000270*  Change Log
000280*
000290*****************************************************************
000300
000310 IDENTIFICATION DIVISION.
000320 PROGRAM-ID.    FJ2BTRV.
000330 AUTHOR.        Todd A. Yancey  02/25/98.
000340 INSTALLATION.  Fujitsu COBOL (Generic).
000350 SECURITY.      Copyright (C) 1998 Fujitsu Software Corporation.
000360
000370*-----------------------------------------------------------------
000380 ENVIRONMENT DIVISION.
000390 CONFIGURATION SECTION.
000400 SOURCE-COMPUTER. Fujitsu.
000410 OBJECT-COMPUTER. Fujitsu.
000420 SPECIAL-NAMES.
000430
000440     SYMBOLIC CONSTANT
000450        *> Basic TRUE/FALSE Constants
000460        VAL-FALSE                          IS 0
000470        VAL-TRUE                           IS 1
000480
000490        *>  Btrieve OP Codes
000500        BTRIEVE-OPEN                       IS 0
000510        BTRIEVE-CLOSE                      IS 1
000520        BTRIEVE-INSERT                     IS 2
000530        BTRIEVE-UPDATE                     IS 3
000540        BTRIEVE-DELETE                     IS 4
000550        BTRIEVE-GET-EQUAL                  IS 5
000560        BTRIEVE-GET-NEXT                   IS 6
000570        BTRIEVE-GET-PREVIOUS               IS 7
000580        BTRIEVE-GET-GREATER-THAN           IS 8
000590        BTRIEVE-GET-LESS-THAN-OR-EQUAL     IS 9
000600        BTRIEVE-GET-FIRST                  IS 12
000610        BTRIEVE-GET-LAST                   IS 13
000620        BTRIEVE-CREATE                     IS 14
000630        BTRIEVE-START                      IS 15
000640        BTRIEVE-EXTEND                     IS 16
000650        BTRIEVE-SET-DIRECTORY              IS 17
000660        BTRIEVE-GET-DIRECTORY              IS 18
000670        BTRIEVE-BEGIN-TRANSACTION          IS 19
000680        BTRIEVE-CONCURRENT-TRANSACTION     IS 1019
000690        BTRIEVE-END-TRANSACTION            IS 20
000700        BTRIEVE-ABORT-TRANSACTION          IS 21
000710        BTRIEVE-GET-POSITION               IS 22
000720        BTRIEVE-GET-DIRECT-CHUCK           IS 23
000730        BTRIEVE-GET-DIRECT-RECORD          IS 23
000740        BTRIEVE-STEP-NEXT                  IS 24
000750        BTRIEVE-STOP                       IS 25
000760        BTRIEVE-VERSION                    IS 26
000770        BTRIEVE-UNLOCK                     IS 27
000780        BTRIEVE-RESET                      IS 28
000790        BTRIEVE-SET-OWNER                  IS 29
000800        BTRIEVE-CLEAR-OWNER                IS 30
000810        BTRIEVE-CREATE-INDEX               IS 31
000820        BTRIEVE-DROP-INDEX                 IS 32
000830        BTRIEVE-STEP-FIRST                 IS 33
000840        BTRIEVE-STEP-LAST                  IS 34
000850        BTRIEVE-STEP-PREVIOUS              IS 35
000860        BTRIEVE-GET-NEXT-EXTENDED          IS 36
000870        BTRIEVE-GET-PREVIOUS-EXTENDED      IS 37
000880        BTRIEVE-STEP-NEXT-EXTENDED         IS 38
000890        BTRIEVE-STEP-PREVIOUS-EXTENDED     IS 39
000900        BTRIEVE-INSERT-EXTENDED            IS 40
000910        BTRIEVE-CONTINUOUS-OPERATION       IS 42
000920        BTRIEVE-GET-BY-PERCENTAGE          IS 44
000930        BTRIEVE-FIND-PERCENTAGE            IS 45
000940        BTRIEVE-GET-KEY                    IS 50
000950        BTRIEVE-UPDATE-CHUNK               IS 53
000960        BTRIEVE-START-EXTENDED             IS 65
000970        BTRIEVE-SINGLE-RECORD-WAIT         IS 100
000980        BTRIEVE-SINGLE-RECORD-NO-WAIT      IS 200
000990        BTRIEVE-MULTI-RECORD-WAIT          IS 300
001000        BTRIEVE-MULTI-RECORD-NO-WAIT       IS 400
001010        BTRIEVE-NO-WAIT-PAGE-LOCK          IS 500
001020
001030        *> Btrieve Open Modes
001040        VAL-OPEN-NORMAL                    IS 0
001050        VAL-OPEN-ACCELERATED               IS -1
001060        VAL-OPEN-READ-ONLY                 IS -2
001070        VAL-OPEN-VERIFY                    IS -3
001080        VAL-OPEN-EXCLUSIVE                 IS -4
001090        VAL-OPEN-SINGLE-ENGINE             IS -32
001100        VAL-OPEN-MULTI-ENGINE              IS -64
001110
001120        *> Btrieve File Flag Values
001130        VAL-VARIABLE-LENGTH-RECORDS        IS 1
001140        VAL-BLANK-TRUNCATION               IS 2
001150        VAL-PAGE-PREALLOCATION             IS 4
001160        VAL-DATA-COMPRESSION               IS 8
001170        VAL-KEY-ONLY-FILE                  IS 16
001180        VAL-BALANCED-INDEX                 IS 32
001190        VAL-FREE-10-PERCENT                IS 64
001200        VAL-FREE-20-PERCENT                IS 128
001210        VAL-FREE-30-PERCENT                IS 192
001220        VAL-RESERVE-DUPLICATE-POINTERS     IS 256
001230        VAL-INCLUDE-SYSTEM-DATA            IS 512
001240        VAL-DO-NOT-INCLUDE-SYSTEM-DATA     IS 4608
001250        VAL-KEY-NUMBER                     IS 1024
001260        VAL-USE-VATS                       IS 2048
001270
001280        *> Btrieve Key Flag Values
001290        VAL-LINKED-DUPLICATES              IS 1
001300        VAL-MODIFABLE-KEY-VALUES           IS 2
001310        VAL-OLD-STYLE-BINARY-DATA-TYPE     IS 4
001320        VAL-OLD-STYLE-STRING-DATA-TYPE     IS 0
001330        VAL-NULL-KEY-ALL-SEGMENTS          IS 8
001340        VAL-SEGMENTED-KEY                  IS 16
001350        VAL-USE-DEFAULT-ACS                IS 32
001360        VAL-USE-NUMBERED-ACS-FILE          IS 1056
001370        VAL-USE-NAMED-ACS                  IS 3104
001380        VAL-DESCENDING-SORT-ORDER          IS 64
001390        VAL-REPEATING-DUPLICATES           IS 128
001400        VAL-USE-EXTENDED-DATA-TYPE         IS 256
001410        VAL-NULL-KEY-ANY-SEGMENT           IS 512
001420        VAL-CASE-INSENSITIVE-KEY           IS 1024
001430
001440        *> Btrieve Extended Data Types
001450        VAL-BTRIEVE-STRING                 IS 0
001460        VAL-BTRIEVE-INTEGER                IS 1
001470        VAL-BTRIEVE-FLOAT                  IS 2
001480        VAL-BTRIEVE-DATE                   IS 3
001490        VAL-BTRIEVE-TIME                   IS 4
001500        VAL-BTRIEVE-DECIMAL                IS 5
001510        VAL-BTRIEVE-MONEY                  IS 6
001520        VAL-BTRIEVE-LOGICAL                IS 7
001530        VAL-BTRIEVE-NUMERIC                IS 8
001540        VAL-BTRIEVE-BFLOAT                 IS 9
001550        VAL-BTRIEVE-LSTRING                IS 10
001560        VAL-BTRIEVE-ZSTRING                IS 11
001570        VAL-BTRIEVE-UNSIGNED-BINARY        IS 14
001580        VAL-BTRIEVE-AUTOINCREMENT          IS 15
001590        VAL-BTRIEVE-NUMERICSTS             IS 17
001600        VAL-BTRIEVE-NUMERICSA              IS 18
001610        VAL-BTRIEVE-CURRENCY               IS 19
001620        VAL-BTRIEVE-TIMESTAMP              IS 20.
001630
001640*-----------------------------------------------------------------
001650 DATA DIVISION.
001660
001670 WORKING-STORAGE SECTION.
001680
001690 01  BTRIEVE-OPERATION-CODE           PIC 9(4) COMP-5 VALUE ZERO.
001700 01  BTRIEVE-POSITION-BLOCK           PIC X(128) VALUE SPACES.
001710 01  BTRIEVE-DATA-BUFFER.
           05  FILLER                       PIC X(1) VALUE SPACES
                                            OCCURS 1 TO 33455 TIMES
                                            DEPENDING ON
                                            BTRIEVE-DATA-BUFFER-LENGTH.
001720 01  BTRIEVE-DATA-BUFFER-LENGTH       PIC 9(4) COMP-5 VALUE ZERO.
001730 01  BTRIEVE-KEY-BUFFER               PIC X(256) VALUE SPACES.
001740 01  BTRIEVE-KEY-NUMBER               PIC 9(4) COMP-5 VALUE ZERO.
001750 01  BTRIEVE-STATUS-CODE              PIC 9(4) COMP-5 VALUE ZERO.
001760     88  BTRIEVE-IO-SUCCESSFUL           VALUE 0.
001770     88  BTRIEVE-INVALID-OPERATION       VALUE 1.
001780     88  BTRIEVE-IO-ERROR                VALUE 2.
001790     88  BTRIEVE-FILE-NOT-OPEN           VALUE 3.
001800     88  BTRIEVE-CANNOT-FIND-KEY-VALUE   VALUE 4.
001810     88  BTRIEVE-DUPLICATE-KEY-VALUE     VALUE 5.
001820     88  BTRIEVE-INVALID-KEY-PARAMETER   VALUE 6.
001830     88  BTRIEVE-KEY-NUMBER-CHANGED      VALUE 7.
001840     88  BTRIEVE-INVALID-POSITIONING     VALUE 8.
001850     88  BTRIEVE-END-OF-FILE             VALUE 9.
001860     88  BTRIEVE-KEY-NOT-MODIFIABLE      VALUE 10.
001870     88  BTRIEVE-FILENAME-INVALID        VALUE 11.
001880     88  BTRIEVE-CANNOT-FIND-FILE        VALUE 12.
001890     88  BTRIEVE-MICROKERNEL-INACTIVE    VALUE 20.
001900     88  BTRIEVE-FILE-ACCESS-DENIED      VALUE 46.
001910     88  BTRIEVE-RECORD-PAGE-LOCKED      VALUE 84.
001920     88  BTRIEVE-FILE-TABLE-FULL         VALUE 86.
001930     88  BTRIEVE-HANDLE-TABLE-FULL       VALUE 87.
001940     88  BTRIEVE-INCOMPATIBLE-MODE       VALUE 88.
001950     88  BTRIEVE-NO-CACHE-BUFFERS        VALUE 100.
001960
001970 01  BTRIEVE-FILE-NAME                PIC X(260) VALUE SPACES.
001980
001990 01  BTRIEVE-CLIENT-ID.
002000     05  FILLER                       PIC X(12) VALUE ZERO.
002010     05  BTRIEVE-SERVICE-AGENT-ID     PIC X(2) VALUE SPACES.
002020     05  BTRIEVE-CLIENT-IDENTIFIER    PIC 9(4) COMP-5 VALUE ZERO.
002030
002040 01  BTRIEVE-CREATE-DATA-BUFFER.
002050     05  BTRIEVE-FILE-SPECIFICATION.
002060         10  BTRIEVE-LOGICAL-RECORD-LENGTH PIC 9(4) COMP-5 VALUE ZERO.
002070         10  BTRIEVE-PAGE-SIZE             PIC 9(4) COMP-5 VALUE ZERO.
002080             88  BTRIEVE-512-PAGE-SIZE     VALUE 512.
002090             88  BTRIEVE-1024-PAGE-SIZE    VALUE 1024.
002100             88  BTRIEVE-1536-PAGE-SIZE    VALUE 1536.
002110             88  BTRIEVE-2048-PAGE-SIZE    VALUE 2048.
002120             88  BTRIEVE-2560-PAGE-SIZE    VALUE 2560.
002130             88  BTRIEVE-3072-PAGE-SIZE    VALUE 3072.
002140             88  BTRIEVE-3584-PAGE-SIZE    VALUE 3584.
002150             88  BTRIEVE-4096-PAGE-SIZE    VALUE 4096.
002160         10  BTRIEVE-NUMBER-OF-INDEXES     PIC 9(4) COMP-5 VALUE ZERO.
002170         10  FILLER                        PIC X(4) VALUE SPACES.
002180         10  BTRIEVE-FILE-FLAGS            PIC 9(4) COMP-5 VALUE ZERO.
002190         10  BTRIEVE-NUMBER-OF-DUPLICATE   PIC X VALUE X"00".
002200         10  FILLER                        PIC X VALUE SPACE.
002210         10  BTRIEVE-ALLOCATION            PIC 9(4) COMP-5 VALUE ZERO.
002220     05  BTRIEVE-KEY-SPECIFICATION.
002230         10  BTRIEVE-KEY-POSITION          PIC 9(4) COMP-5 VALUE ZERO.
002240         10  BTRIEVE-KEY-LENGTH            PIC 9(4) COMP-5 VALUE ZERO.
002250         10  BTRIEVE-KEY-FLAGS             PIC 9(4) COMP-5 VALUE ZERO.
002260         10  FILLER                        PIC X(4) VALUE SPACE.
002270         10  BTRIEVE-EXTENDED-DATA-TYPE    PIC X VALUE X"00".
002280             88  BTRIEVE-STRING            VALUE X"00".
002290             88  BTRIEVE-INTEGER           VALUE X"01".
002300             88  BTRIEVE-FLOAT             VALUE X"02".
002310             88  BTRIEVE-DATE              VALUE X"03".
002320             88  BTRIEVE-TIME              VALUE X"04".
002330             88  BTRIEVE-DECIMAL           VALUE X"05".
002340             88  BTRIEVE-MONEY             VALUE X"06".
002350             88  BTRIEVE-LOGICAL           VALUE X"07".
002360             88  BTRIEVE-NUMERIC           VALUE X"08".
002370             88  BTRIEVE-BFLOAT            VALUE X"09".
002380             88  BTRIEVE-LSTRING           VALUE X"0A".
002390             88  BTRIEVE-ZSTRING           VALUE X"0B".
002400             88  BTRIEVE-UNSIGNED-BINARY   VALUE X"0E".
002410             88  BTRIEVE-AUTOINCREMENT     VALUE X"0F".
002420             88  BTRIEVE-NUMERICSTS        VALUE X"11".
002430             88  BTRIEVE-NUMERICSA         VALUE X"12".
002440             88  BTRIEVE-CURRENCY          VALUE X"13".
002450             88  BTRIEVE-TIMESTAMP         VALUE X"14".
002460         10  BTRIEVE-NULL-VALUE            PIC X VALUE X"00".
002470         10  FILLER                        PIC X(2) VALUE SPACES.
002480         10  BTRIEVE-ASSIGNED-KEY-NUMBER   PIC X VALUE X"00".
002490         10  BTRIEVE-ACS-NUMBER            PIC X VALUE X"00".
002500     05  BTRIEVE-ACS-NUMBER-0              PIC X(256) VALUE SPACES.
002510
002520
002530
002540*-----------------------------------------------------------------
002550 PROCEDURE DIVISION.
002560
002570     DISPLAY "Fujitsu COBOL -- Btrieve Interface Sample"
002580     DISPLAY SPACES
002590
002600     *> Open Btrieve File
002610     MOVE ZERO TO BTRIEVE-DATA-BUFFER-LENGTH
002620     MOVE ZERO TO BTRIEVE-KEY-NUMBER
002630     MOVE "TEST.BTR" TO BTRIEVE-FILE-NAME
002640     MOVE BTRIEVE-OPEN TO BTRIEVE-OPERATION-CODE
002650     PERFORM CALL-BTRIEVE
002660     IF BTRIEVE-STATUS-CODE = ZERO
002670        DISPLAY "Btrieve Open Successful"
002680     ELSE
002690        DISPLAY "Error Opening file. Status=" BTRIEVE-STATUS-CODE
002700     END-IF
002710
002720     *> Get First Record
002730     MOVE 40 TO BTRIEVE-DATA-BUFFER-LENGTH
002740     MOVE ZERO TO BTRIEVE-KEY-NUMBER
002750     MOVE BTRIEVE-GET-FIRST TO BTRIEVE-OPERATION-CODE
002760     PERFORM CALL-BTRIEVE
002770     IF BTRIEVE-STATUS-CODE = ZERO
002780        DISPLAY "Btrieve Record: " BTRIEVE-DATA-BUFFER( 1 : 40 )
002790     ELSE
002800        DISPLAY "Error Getting First Record. Status="
BTRIEVE-STATUS-CODE
002810     END-IF
002820
002830     *> Close Btrieve File
002840     MOVE ZERO TO BTRIEVE-DATA-BUFFER-LENGTH
002850     MOVE ZERO TO BTRIEVE-KEY-NUMBER
002860     MOVE BTRIEVE-CLOSE TO BTRIEVE-OPERATION-CODE
002870     PERFORM CALL-BTRIEVE
002880     IF BTRIEVE-STATUS-CODE = ZERO
002890        DISPLAY "Btrieve Close File Successful"
002900     ELSE
002910        DISPLAY "Error Closing Btrieve File. Status="
BTRIEVE-STATUS-CODE
002920     END-IF
002930
002940     EXIT PROGRAM.
002950
002960
002970*-----------------------------------------------------------------
002980 CALL-BTRIEVE.
002990
003000     CALL "BTRCALL" WITH STDCALL USING BTRIEVE-OPERATION-CODE
003010                                       BTRIEVE-STATUS-CODE
003020                                       BTRIEVE-POSITION-BLOCK
003030                                       BTRIEVE-DATA-BUFFER
003040                                       BTRIEVE-DATA-BUFFER-LENGTH
003050                                       BTRIEVE-FILE-NAME
003060                                       BTRIEVE-KEY-NUMBER
003070     END-CALL.
003080
003090
003100*-----------------------------------------------------------------
003110*CALL-BTRIEVE-CLIENT.
003120
003130
003140*-----------------------------------------------------------------
003150 END PROGRAM FJ2BTRV.
003160*-----------------------------------------------------------------

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX:    (408) 428-0600
Email:  cobol@adtools.com
Web:   http://www.adtools.com


Paul Schmitteck wrote in message <6t07jq$ekg$2@news02.btx.dtag.de>...
>Hello Everybody,
>       I have a question.. I have an application which uses brieve
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
