[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# POINTERS

_5 messages · 5 participants · 2002-11_

---

### POINTERS

- **From:** "Maximo Ricardo Boettner" <max.boettner@t-online.de>
- **Date:** 2002-11-02T08:31:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<apvv40$fj3$04$1@news.t-online.com>`

```
Anybody that know work with POINTERS in cobol.
I need an litle example.
nax
```

#### ↳ Re: POINTERS

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-11-02T14:15:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-l51jDMOhqYg7@h24-82-204-17.wp.shawcable.net>`
- **References:** `<apvv40$fj3$04$1@news.t-online.com>`

```
On Sat, 2 Nov 2002 07:31:57 UTC, "Maximo Ricardo Boettner" 
<max.boettner@t-online.de> wrote:

> Anybody that know work with POINTERS in cobol.
> I need an litle example.
> nax
> 
> 

define some buffer

01  some-buffer.
  02  buff-bits pic x(4000).

define the pointer

01  the-pointer usage pointer.

in the procedures

set the-pointer to address of some-buffer.

call "someprogram" using
  by value the-pointer

is equivalent to

call "someprogram" using
  by reference some-buffer
```

##### ↳ ↳ Re: POINTERS

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-11-02T16:01:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0211021601.16cb833c@posting.google.com>`
- **References:** `<apvv40$fj3$04$1@news.t-online.com> <ZpzG4UNLyRNq-pn2-l51jDMOhqYg7@h24-82-204-17.wp.shawcable.net>`

```
Hi Max,

If you're an IBM/MVS pgmr, here are some code snippets that illustrate
the use of pointers to access system control blocks.
It's a tad dated but the pointer concepts are still valid.

Regards, Jack.

PROGRAM-ID.    RUNINFO.
**************************************************
*  DISPLAYS THE FOLLOWING RUN INFO FOR THE 
*  CALLING PROGRAM:
     
*       ~   PGM/JOB/JOBSTEP/PROCSTEP NAMES  
*       ~   ENTRY/LOAD/END POINTS AND LENGTH OF
*           PROGRAM 

*  FOR COBOL II PROGRAMS ALSO DISPLAYS 4 BYTES OF 
*  HEX INDICATORS SHOWING THE COMPILE OPTIONS
*  SELECTED AT COMPILE TIME.
**************************************************

**************************************************
 WORKING-STORAGE                 SECTION.
**************************************************

 01  WS-TCB-ADDR-01.
     10  WS-TCB-ADDR             POINTER.
 .
 .
 .

 /
**************************************************
 LINKAGE                         SECTION.
**************************************************

 01  LK-TCB-ADDR                 POINTER.
  .
  .
  .
*-------------------------------------------------
*===&gt; T A S K   C O N T R O L   B L O C K
*-------------------------------------------------
 01  LK-TCB.
     10  FILLER                  PIC  X(012).
     10  LK-TIOT-ADDR            POINTER.
     10  FILLER                  PIC  X(028).
     10  LK-LAST-CDE-ADDR        POINTER.

*-------------------------------------------------
*===&gt;     T A S K   I/O   T A B L E
*-------------------------------------------------
 01  LK-TIOT.
     10  LK-JOB-NAME             PIC  X(008).
     10  LK-JSTP-NAME            PIC  X(008).
     10 LK-PSTP-NAME             PIC  X(008).

*-------------------------------------------------
*===&gt; C O N T E N T S    D I R E C T O R Y    
*===&gt;             E N T R Y
*-------------------------------------------------
 01  LK-CDE.
     10  LK-PREV-CDE-ADDR        POINTER.
     10  FILLER                  PIC  X(004).
     10  LK-PGM-NAME             PIC  X(008).
     10  LK-EP-ADDR              PIC  X(004).
     10  LK-EXTENT-LST-ADDR      POINTER.

*-------------------------------------------------
*===&gt;         E X T E N T    L I S T
*-------------------------------------------------
 01  LK-EXTENT-LST.
     10  FILLER                  PIC  X(009).
     10  LK-PGM-LEN              PIC  X(003).
     10  LK-LP-ADDR              PIC  X(004).
     10  REDEFINES  LK-LP-ADDR.
     15  LK-LP-ADDR-BIN          PIC  9(009) COMP.
     10  REDEFINES  LK-LP-ADDR.
     15  LK-LP-ADDR-PTR          POINTER.

**************************************************
 01  LK-COMPILER-INFO.
**************************************************
     05  LK-VSCOB-INFO.
         10 FILLER               PIC  X(020).
         10 LK-TYPE-VS           PIC  X(002).
            88 LK-VSCOBOL             VALUE "VS".
         10 FILLER               PIC  X(001).
         10 LK-VSREL-NBR         PIC  X(001).
         10 FILLER               PIC  X(112).
         10 LK-VSTIME            PIC  X(008).
         10 LK-VSMO-DAY          PIC  X(008).
         10 LK-VSYEAR            PIC  X(004).
     05  REDEFINES  LK-VSCOB-INFO.
     10  LK-COBII-INFO.
         20 FILLER               PIC  X(014).
         20 LK-TYPE-II           PIC  X(002).
         20 FILLER               PIC  X(001).
         20 LK-IIREL-NBR         PIC  X(006).
         20 LK-IIMON-DAY-YR      PIC  X(009).
         20 LK-IITIME            PIC  X(008).
         20 FILLER               PIC  X(004).
         20 LK-IIOPT-BYTES       PIC  X(004).

**************************************************
 PROCEDURE DIVISION.
**************************************************

 000-MAINLINE.
*-------------------------------------------------
*===&gt;  ESTABLISH ADDRESSABILITY FOR TIOT
*-------------------------------------------------
     MOVE X"0000021C" TO  WS-TCB-ADDR-01
     SET  ADDRESS OF LK-TCB-ADDR TO  WS-TCB-ADDR
     SET  ADDRESS OF LK-TCB      TO  LK-TCB-ADDR
     SET  ADDRESS OF LK-TIOT     TO  LK-TIOT-ADDR

*-------------------------------------------------
*===&gt;  SET UP STEP NAMES FOR DISPLAY
*-------------------------------------------------
     IF LK-JSTP-NAME = SPACES
        AND
        LK-PSTP-NAME = SPACES
        GO TO 000-CONTINUE
     END-IF
     IF LK-PSTP-NAME = SPACES
        MOVE LK-JSTP-NAME TO WS-JSTP-NAME
     ELSE
        MOVE LK-PSTP-NAME TO WS-JSTP-NAME
        MOVE LK-JSTP-NAME TO WS-PSTP-NAME
     END-IF
     .
 000-CONTINUE.
*-------------------------------------------------
*===&gt;  SET UP PGM NAME FOR DISPLAY
*-------------------------------------------------
     SET ADDRESS OF LK-CDE TO LK-LAST-CDE-ADDR
     PERFORM WITH TEST BEFORE 
       UNTIL LK-PREV-CDE-ADDR = NULLS
             SET ADDRESS OF LK-CDE 
              TO  LK-PREV-CDE-ADDR
     END-PERFORM
     MOVE LK-PGM-NAME TO WS-PN-DISPLAY
     .
     .



lsunley@mb.sympatico.ca wrote in message news:<ZpzG4UNLyRNq-pn2-l51jDMOhqYg7@h24-82-204-17.wp.shawcable.net>...
> On Sat, 2 Nov 2002 07:31:57 UTC, "Maximo Ricardo Boettner" 
> <max.boettner@t-online.de> wrote:
…[26 more quoted lines elided]…
>   by reference some-buffer
```

#### ↳ Re: POINTERS

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-02T13:35:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211021335.29e49570@posting.google.com>`
- **References:** `<apvv40$fj3$04$1@news.t-online.com>`

```
"Maximo Ricardo Boettner" <max.boettner@t-online.de> wrote

> Anybody that know work with POINTERS in cobol.
> I need an litle example.

In standard Cobol the STRING and UNSTRING have 'WITH POINTER var-n'
clauses which are very useful. for example to unstring one value at a
time:

       MOVE 1      TO current-position
       PERFORM 
           WITH TEST AFTER           
           UNTIL current-terminator = "'"

           MOVE SPACES      TO Work-string
           UNSTRING EDIFACT-Segment
               DELIMITED BY "'" OR "+" OR ":"
               INTO Work-string
               DELIMITER IN current-terminator
               WITH POINTER current-position
           IF ( ... )
               blah blah
           END-IF
       END-PERFORM    Note: an EDIFACT segment ends with an "'" and
the values are separated by + and :.

However, I doubt that this is what you actually mean.  You probably
want to use raw machine addresses in an entirely low-level language
way.  Cobol is a high level language and avoids such grubby and
error-prone mechanisms.
Some compilers do have extensions to the language which can cater for
some uses that require dealing with raw addresses.  For example it is
possible (in some implementations) to take the address of an object
using:

            SET My-raw-address     TO ADDRESS OF My-record-area

also if an address is passed into a Cobol program it is possible to
de-reference this by having a declaration of its structure in linkage
section and then using SET to associate the declaration with the
address:

       LINKAGE SECTION.
       01  Passed-in-area.
           03  Passed-item-1          PIC S9(8) COMP-5.
           etc

           SET ADDRESS OF Passed-in-area   TO My-raw-address

then you can access Passed-in-... fields because they will map over
the data area in the program that gave you the address (probably).

See the specific details of this in the manuals of the version you
use.
```

#### ↳ Re: POINTERS

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-11-03T02:48:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c282e3$78426740$ca95f243@chottel>`
- **References:** `<apvv40$fj3$04$1@news.t-online.com>`

```
//JOBNAME JOB (ACCT,'ROOM-NBR'),'HOTTEL COBPTR',MSGCLASS=S,CLASS=K         
    
//PROCLIB JCLLIB ORDER=USERID.DVL.PROC                                     
    
//        SET TITLE1='XXX.COB00010'                                        
    
//OUTPUT INCLUDE MEMBER=DESTCH                                             
    
//*-------------------------------------------------------------------*    
    
//*        COBOL II COMPILE                                           *    
    
//*-------------------------------------------------------------------*    
    
//STEP01   EXEC  COB3CLG,LIBRARY='DVL.SOURCE.LIBMAST',PROG=IEFBR14,        
    
//    LOPT='AMODE=31,RMODE=ANY'                                            
    
//COMP.SYSIN DD  *                                                         
    
       ID DIVISION.                                                        
    
       PROGRAM-ID.   COBPTR.                                               
    
       AUTHOR.       CHARLIE HOTTEL.                                       
    
       DATE-WRITTEN. 08/22/01.                                             
    
       DATE-COMPILED.                                                      
    
      *---------------------------------------------------------------*    
    
      *    VS COBOL II POINTER FEATURE EXAMPLE                        *    
    
      *    USING MVS CONTROL BLOCKS                                   *    
    
      *---------------------------------------------------------------*    
    
      *    BASED ON ARTICLE: "THE POINTER FEATURE OF VS COBOL II" BY  *    
    
      *    ANNE PETICOLAS IN ENTERPRISE SYSTEMS JOURNAL, MARCH 1991.  *    
    
      *---------------------------------------------------------------*    
    
       ENVIRONMENT DIVISION.                                               
    
       INPUT-OUTPUT SECTION.                                               
    
       FILE-CONTROL.                                                       
    
           SELECT TEST-FILE ASSIGN TO DD1.                                 
    
       DATA DIVISION.                                                      
    
       FILE SECTION.                                                       
    
       FD  TEST-FILE                                                       
    
           LABEL RECORDS STANDARD                                          
    
           RECORDING MODE IS F                                             
    
           BLOCK CONTAINS 0 RECORDS                                        
    
           DATA RECORD IS TEST-REC.                                        
    
       01  TEST-REC PIC X(80).                                             
    
      /                                                                    
    
       WORKING-STORAGE SECTION.                                            
    
                                                                           
    
TEST***01  WS-TEST                            PIC S9(9) COMP VALUE ZERO.   
    
       01  WS-WORK                             PIC S9(9) COMP.             
    
       01  WS-RIGHT-HEX-DIGIT                  PIC S9(4) COMP.             
    
       01  WS-LEN                              PIC S9(4) COMP.             
    
       01  WS-LENGTH REDEFINES WS-LEN          PIC X(02).                  
    
       01  WS-FLAG                             PIC S9(4) COMP.             
    
       01  WS-FLAG1 REDEFINES WS-FLAG          PIC X(02).                  
    
                                                                           
    
       01  WS-TCB-ADDRESS-POINTER.                                         
    
           05  WS-TCB-ADDR-POINTER             USAGE IS POINTER.           
    
                                                                           
    
       01  WS-TIOT-SEG-POINT.                                              
    
           05  WS-TIOT-SEG-POINTER             USAGE IS POINTER.           
    
           05  WS-TIOT-SEG-PNT REDEFINES WS-TIOT-SEG-POINTER               
    
                                               PIC S9(9) COMP.             
    
                                                                           
    
       01  WS-JFCB-POINT.                                                  
    
           05  WS-JFCB-POINTER                 USAGE IS POINTER.           
    
           05  WS-JFCB-PTR REDEFINES WS-JFCB-POINTER                       
    
                                               PIC S9(9) COMP.             
    
           05  WS-JFCB-POINT-RED REDEFINES  WS-JFCB-PTR.                   
    
               07  FILLER                      PIC X.                      
    
               07  WS-JFCB-LOW-3               PIC X(3).                   
    
                                                                           
    
       01  WS-POINT.                                                       
    
           05  WS-POINTER                      USAGE IS POINTER.           
    
           05  WS-PTR REDEFINES WS-POINTER                                 
    
                                               PIC S9(9) COMP.             
    
           05  WS-POINT-RED REDEFINES WS-PTR.                              
    
               07  FILLER                      PIC X.                      
    
               07  WS-LOW-3                    PIC X(3).                   
    
                                                                           
    
       01  WS-SWA-POINT.                                                   
    
           05  WS-SWA-POINTER                  USAGE IS POINTER.           
    
           05  WS-SWA-PTR REDEFINES WS-SWA-POINTER                         
    
                                               PIC S9(9) COMP.             
    
           05  WS-SWA-POINT-RED REDEFINES WS-SWA-PTR.                      
    
               07  FILLER                      PIC X.                      
    
               07  WS-SWA-LOW-3                PIC X(3).                   
    
                                                                           
    
       01  WS-QMAT-POINT.                                                  
    
           05  WS-QMAT-POINTER                 USAGE IS POINTER.           
    
           05  WS-QMAT-PTR REDEFINES WS-QMAT-POINTER                       
    
                                               PIC S9(9) COMP.             
    
      /                                                                    
    
       01  WS-UCB-POINT.                                                   
    
           05  WS-UCB-POINTER                  USAGE IS POINTER.           
    
           05  WS-UCB-POINT-RED REDEFINES WS-UCB-POINTER.                  
    
               07  FILLER                      PIC X.                      
    
               07  WS-UCB-LOW-3                PIC X(3).                   
    
                                                                           
    
       01  WS-DEB-POINT.                                                   
    
           05  WS-DEB-POINTER                  USAGE IS POINTER.           
    
           05  WS-DEB-POINT-RED REDEFINES WS-DEB-POINTER.                  
    
               07  FILLER                      PIC X.                      
    
               07  WS-DEB-LOW-3                PIC X(3).                   
    
                                                                           
    
       01  WS-DCB-POINT.                                                   
    
           05  WS-DCB-POINTER                  USAGE IS POINTER.           
    
           05  WS-DCB-POINT-RED REDEFINES WS-DCB-POINTER.                  
    
               07  FILLER                      PIC X.                      
    
               07  WS-DCB-LOW-3                PIC X(3).                   
    
                                                                           
    
       01  WS-CVT-ADDRESS-POINTER.                                         
    
           05  WS-CVT-ADDR-POINTER             USAGE IS POINTER.           
    
                                                                           
    
       01  WS-ASCB-ADDRESS-POINTER.                                        
    
           05  WS-ASCB-ADDR-POINTER            USAGE IS POINTER.           
    
                                                                           
    
       01  WS-ASSB-ADDRESS-POINTER.                                        
    
           05  WS-ASSB-ADDR-POINTER            USAGE IS POINTER.           
    
                                                                           
    
       01  WS-JSAB-ADDRESS-POINTER.                                        
    
           05  WS-JSAB-ADDR-POINTER            USAGE IS POINTER.           
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      * PUT THE STATEMENTS BELOW IN AN ASSEMBLER PROGRAM TO LOCATE    *    
    
      * THE DISPLACEMENTS OF THE SYMBOLS.  THESE LINES WERE SHIFTED   *    
    
      * TO THE RIGHT TO MAKE COBOL COMMENTS.  SHIFT THEM BACK TO THE  *    
    
      * LEFT SO THAT THE WORD 'TITLE' IS IN COLUMN 10.                *    
    
      *---------------------------------------------------------------*    
    
      *              TITLE 'PREFIX STORAGE AREA'                      *    
    
      *              IHAPSA LIST=YES                                  *    
    
      *              TITLE 'TASK CONTROL BLOCK'                       *    
    
      *              IKJTCB LIST=YES                                  *    
    
      *              TITLE 'SECONDARY TASK CONTROL BLOCK'             *    
    
      *              IHASTCB LIST=YES                                 *    
    
      *              TITLE 'DATA EXTENT BLOCK'                        *    
    
      *              IEZDEB LIST=YES                                  *    
    
      *              TITLE 'DATA CONTROL BLOCK'                       *    
    
      *     DCBDS    DSECT                                            *    
    
      *              DCBD  DSORG=PS                                   *    
    
      *              TITLE 'UNIT CONTROL BLOCK'                       *    
    
      *     UCBDS    DSECT                                            *    
    
      *              IEFUCBOB                                         *    
    
      *              TITLE 'TASK I/O TABLE'                           *    
    
      *     TIOTDS   DSECT                                            *    
    
      *              IEFTIOT1                                         *    
    
      *              TITLE 'JOB FILE CONTROL BLOCK'                   *    
    
      *     JFCBDS   DSECT                                            *    
    
      *              IEFJFCBN LIST=YES                                *    
    
      *              TITLE 'COMMUNICATION VECTOR TABLE'               *    
    
      *              CVT DSECT=YES,LIST=YES                           *    
    
      *              TITLE 'SUBSYSTEM COMMUNICATION VECTOR TABLE'     *    
    
      *              IEFJSCVT                                         *    
    
      *              TITLE 'JOB STEP CONTROL BLOCK'                   *    
    
      *              IEZJSCB                                          *    
    
      *              TITLE 'SWA QUEUE AREA'                           *    
    
      *              IEFQMNGR                                         *    
    
      *              TITLE 'JES COMMUNICATION TABLE'                  *    
    
      *              IEFJESCT                                         *    
    
      *              TITLE 'JSAB'                                     *    
    
      *              IAZJSAB DSECT=YES,LIST=YES                       *    
    
      *              TITLE 'ASCB'                                     *    
    
      *              IHAASCB DSECT=YES,LIST=YES                       *    
    
      *              TITLE 'ASSB'                                     *    
    
      *              IHAASSB LIST=YES                                 *    
    
      *              TITLE 'VSAM ACB'                                 *    
    
      *              IFGACB DSECT=YES                                 *    
    
      *              TITLE 'REMOTE AREAS'                             *    
    
      *---------------------------------------------------------------*    
    
      /                                                                    
    
       LINKAGE SECTION.                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IHAPSA)  X'21C' = DECIMAL 540                  *    
    
      *                         X'224' = DECIMAL 548                  *    
    
      *---------------------------------------------------------------*    
    
       01  PSA.                                                            
    
           05  FILLER             PIC X(540).                              
    
           05  TCB-PTR                      USAGE IS POINTER.              
    
           05  FILLER             PIC X(04).                               
    
           05  ASCB-PTR                     USAGE IS POINTER.              
    
       01  PSA-ASM REDEFINES PSA.                                          
    
           05  FILLER             PIC X(540).                              
    
           05  PSATOLD                      USAGE IS POINTER.              
    
           05  FILLER             PIC X(04).                               
    
           05  PSAAOLD                      USAGE IS POINTER.              
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IKJTCB)  HAS A 32 BYTE PREFIX AREA             *    
    
      *---------------------------------------------------------------*    
    
       01  TCB-POINTER                      USAGE IS POINTER.              
    
       01  TCB.                                                            
    
           05  FILLER             PIC X(08).                               
    
           05  DEB-ADDR                     USAGE IS POINTER.              
    
           05  TIOT-POINTER                 USAGE IS POINTER.              
    
           05  FILLER             PIC X(164).                              
    
           05  JSCB-POINTER                 USAGE IS POINTER.              
    
           05  FILLER             PIC X(128).                              
    
           05  STCB-POINTER                 USAGE IS POINTER.              
    
       01  TCB-ASM REDEFINES TCB.                                          
    
           05  FILLER             PIC X(08).                               
    
           05  TCBDEB                       USAGE IS POINTER.              
    
           05  TCBTIO                       USAGE IS POINTER.              
    
           05  FILLER             PIC X(164).                              
    
           05  TCBJSCB                      USAGE IS POINTER.              
    
           05  FILLER             PIC X(128).                              
    
           05  TCBSTCB                      USAGE IS POINTER.              
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(CVT)                                           *    
    
      *---------------------------------------------------------------*    
    
       01  CVT-POINTER                      USAGE IS POINTER.              
    
       01  CVT.                                                            
    
           05  FILLER             PIC X(296).                              
    
           05  JESCT-POINTER                USAGE IS POINTER.              
    
       01  CVT-ASM REDEFINES CVT.                                          
    
           05  FILLER             PIC X(296).                              
    
           05  CVTJESCT                     USAGE IS POINTER.              
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEFJESCT)                                      *    
    
      *---------------------------------------------------------------*    
    
       01  JESCT.                                                          
    
           05  FILLER             PIC X(24).                               
    
           05  JESSSCVT-POINTER             USAGE IS POINTER.              
    
       01  JESCT-ASM REDEFINES JESCT.                                      
    
           05  FILLER             PIC X(24).                               
    
           05  JESSSCT                      USAGE IS POINTER.              
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEFJSCVT)                                      *    
    
      *---------------------------------------------------------------*    
    
       01  SSCVT.                                                          
    
           05  SSCVT-EYE-CATCHER  PIC X(04).                               
    
           05  NEXT-SSCVT                   USAGE IS POINTER.              
    
           05  SUBSYSTEM-NAME     PIC X(04).                               
    
       01  SSCVT-ASM  REDEFINES SSCVT.                                     
    
           05  SSCTID             PIC X(04).                               
    
           05  SSCTSCTA                     USAGE IS POINTER.              
    
           05  SSCTSNAM           PIC X(04).                               
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEFTIOT1)                                      *    
    
      *---------------------------------------------------------------*    
    
       01  TIOT.                                                           
    
           05  JOB-NAME           PIC X(08).                               
    
           05  JOB-PROC           PIC X(08).                               
    
           05  JOB-STEP           PIC X(08).                               
    
       01  TIOT-ASM REDEFINES TIOT.                                        
    
           05  TIOCSTPN           PIC X(08).                               
    
           05  TIOCPSTN           PIC X(08).                               
    
           05  TIOCSJSTN          PIC X(08).                               
    
                                                                           
    
       01  TIOT-SEG.                                                       
    
           05  TIO-LEN            PIC X.                                   
    
           05  FILLER             PIC X(03).                               
    
           05  DD-NAME            PIC X(08).                               
    
           05  SWA-V-ADDR         PIC X(03).                               
    
           05  FILLER             PIC X(02).                               
    
           05  UCB-ADDR           PIC X(03).                               
    
       01  TIOENTRY REDEFINES TIOT-SEG.                                    
    
           05  TIOELNGH           PIC X.                                   
    
           05  FILLER             PIC X(03).                               
    
           05  TIOEDDNM           PIC X(08).                               
    
           05  TIOEJFCB           PIC X(03).                               
    
           05  FILLER             PIC X(02).                               
    
           05  TIOEFSRT           PIC X(03).                               
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEFJFCBN)                                      *    
    
      *---------------------------------------------------------------*    
    
       01  JFCB.                                                           
    
           05  DS-NAME            PIC X(44).                               
    
           05  FILLER             PIC X(74).                               
    
           05  VOL-SER            PIC X(06).                               
    
       01  JFCB-ASM REDEFINES JFCB.                                        
    
           05  JFCBDSNM           PIC X(44).                               
    
           05  FILLER             PIC X(74).                               
    
           05  JFCBVOLS           PIC X(06).                               
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEZDEB)  DEB HAS A 36 BYTE PREFIX AREA         *    
    
      *---------------------------------------------------------------*    
    
       01  DEB.                                                            
    
           05  FILLER             PIC X(05).                               
    
           05  NEXT-DEB-ADDR      PIC X(03).                               
    
           05  FILLER             PIC X(17).                               
    
           05  DCB-ADDR           PIC X(03).                               
    
       01  DEB-ASM REDEFINES DEB.                                          
    
           05  FILLER             PIC X(05).                               
    
           05  DEBDEBB            PIC X(03).                               
    
           05  FILLER             PIC X(17).                               
    
           05  DEBDCB             PIC X(03).                               
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(DCBD)                                          *    
    
      *---------------------------------------------------------------*    
    
       01  DCB.                                                            
    
           05  FILLER             PIC X(17).                               
    
           05  DEVICE-TYPE        PIC X.                                   
    
               88  DISK-3380-X2E  VALUE X'2E'.                             
    
               88  DISK-3390-X2F  VALUE X'2F'.                             
    
           05  FILLER             PIC X(08).                               
    
           05  DSORG              PIC X(02).                               
    
           05  FILLER             PIC X(08).                               
    
           05  RECFM              PIC X(02).                               
    
           05  FILLER             PIC X(02).                               
    
           05  DDNAME             PIC X(08).                               
    
           05  FILLER             PIC X(14).                               
    
           05  BLKSIZE            PIC S9(4) COMP.                          
    
           05  FILLER             PIC X(18).                               
    
           05  LRECL              PIC S9(4) COMP.                          
    
       01  DCB-ASM REDEFINES DCB.                                          
    
           05  FILLER             PIC X(17).                               
    
           05  DCBDEVT            PIC X.                                   
    
           05  FILLER             PIC X(08).                               
    
           05  DCBDSORG           PIC X(02).                               
    
           05  FILLER             PIC X(08).                               
    
           05  DCBRECFM           PIC X(02).                               
    
           05  FILLER             PIC X(02).                               
    
           05  DCBDDNAM           PIC X(08).                               
    
           05  FILLER             PIC X(14).                               
    
           05  DCBBLKSI           PIC S9(4) COMP.                          
    
           05  FILLER             PIC X(18).                               
    
           05  DCBLRECL           PIC S9(4) COMP.                          
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEZJSCB)                                       *    
    
      *---------------------------------------------------------------*    
    
       01  JSCB.                                                           
    
           05  FILLER             PIC X(244).                              
    
           05  QMPL-POINTER       USAGE IS POINTER.                        
    
       01  JSCB-ASM REDEFINES JSCB.                                        
    
           05  FILLER             PIC X(244).                              
    
           05  JSCBQMPI           USAGE IS POINTER.                        
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IEFQMNGR)                                      *    
    
      *---------------------------------------------------------------*    
    
       01  QMPL.                                                           
    
           05  FILLER             PIC X(24).                               
    
           05  QMAT-POINTER       USAGE IS POINTER.                        
    
       01  QMPL-ASM REDEFINES QMPL.                                        
    
           05  FILLER             PIC X(24).                               
    
           05  QMADD              USAGE IS POINTER.                        
    
                                                                           
    
       01  QMAT.                                                           
    
           05  FILLER             PIC X(12).                               
    
           05  QMAT-NEXT-POINTER  USAGE IS POINTER.                        
    
                                                                           
    
       01  SWA.                                                            
    
           05  JFCB-ADDR          USAGE IS POINTER.                        
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MODGEN(IHASTCB)                                       *    
    
      *---------------------------------------------------------------*    
    
       01  STCB.                                                           
    
           05  FILLER             PIC X(188).                              
    
           05  JSAB-POINTER       USAGE IS POINTER.                        
    
       01  STCB-ASM REDEFINES STCB.                                        
    
           05  FILLER             PIC X(188).                              
    
           05  STCBJSAB           USAGE IS POINTER.                        
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IAZJSAB)                                       *    
    
      *---------------------------------------------------------------*    
    
       01  JSAB.                                                           
    
           05  JSAB-EYE-CATCHER   PIC X(04).                               
    
           05  JSAB-NEXT-PTR      USAGE IS POINTER.                        
    
           05  FILLER             PIC X(05).                               
    
           05  JSAB-FLAG1         PIC X.                                   
    
           05  FILLER             PIC X(02).                               
    
           05  COMPONENT          PIC X(04).                               
    
           05  JOB-ID             PIC X(08).                               
    
           05  JOB-NBR            PIC X(08).                               
    
           05  FILLER             PIC X(08).                               
    
           05  USERID             PIC X(08).                               
    
       01  JSAB-ASM REDEFINES JSAB.                                        
    
           05  JSABID             PIC X(04).                               
    
           05  JSABNEXT           USAGE IS POINTER.                        
    
           05  FILLER             PIC X(05).                               
    
           05  JSABFLG1           PIC X.                                   
    
           05  FILLER             PIC X(02).                               
    
           05  JSABSCID           PIC X(04).                               
    
           05  JSABJBID           PIC X(08).                               
    
           05  JSABJBNM           PIC X(08).                               
    
           05  FILLER             PIC X(08).                               
    
           05  JSABUSID           PIC X(08).                               
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IHAASCB)                                       *    
    
      *---------------------------------------------------------------*    
    
       01  ASCB-POINTER                     USAGE IS POINTER.              
    
       01  ASCB.                                                           
    
           05  FILLER             PIC X(336).                              
    
           05  ASSB-POINTER       USAGE IS POINTER.                        
    
       01  ASCB-ASM REDEFINES ASCB.                                        
    
           05  FILLER             PIC X(336).                              
    
           05  ASCBASSB           USAGE IS POINTER.                        
    
      /                                                                    
    
      *---------------------------------------------------------------*    
    
      *    SYS1.MACLIB(IHAASSB)                                       *    
    
      *---------------------------------------------------------------*    
    
       01  ASSB.                                                           
    
           05  FILLER             PIC X(168).                              
    
           05  JSAB-POINTER       USAGE IS POINTER.                        
    
       01  ASSB-ASM REDEFINES ASSB.                                        
    
           05  FILLER             PIC X(168).                              
    
           05  ASSBJSAB           USAGE IS POINTER.                        
    
      /                                                                    
    
       PROCEDURE DIVISION.                                                 
    
           PERFORM JOB-STEP-NAME.                                          
    
           PERFORM SUBSYSTEM-NAMES.                                        
    
           PERFORM JFCB-INFO.                                              
    
           PERFORM DCB-INFO.                                               
    
           PERFORM JSAB-INFO.                                              
    
                                                                           
    
           GOBACK.                                                         
    
      /                                                                    
    
       JOB-STEP-NAME.                                                      
    
      *---------------------------------------------------------------*    
    
      *    JOB NAME AND STEP NAME                                     *    
    
      *      PSA + X'21C' -> TCB -> TIOT                              *    
    
      *---------------------------------------------------------------*    
    
           MOVE X'0000021C' TO WS-TCB-ADDRESS-POINTER.                     
    
           SET ADDRESS OF TCB-POINTER TO WS-TCB-ADDR-POINTER.              
    
           SET ADDRESS OF TCB TO TCB-POINTER.                              
    
           SET ADDRESS OF TIOT TO TIOT-POINTER.                            
    
           DISPLAY 'JOB NAME=' JOB-NAME                                    
    
                   '  JOB PROC=' JOB-PROC                                  
    
                   '  JOB STEP=' JOB-STEP.                                 
    
           DISPLAY '         '.                                            
    
      /                                                                    
    
       SUBSYSTEM-NAMES.                                                    
    
      *---------------------------------------------------------------*    
    
      *    DISPLAY SUBSYSTEM NAMES FROM SSCVT CHAIN                   *    
    
      *    CVT -> JSECT -> SSCVT                                      *    
    
      *---------------------------------------------------------------*    
    
           MOVE X'00000010' TO WS-CVT-ADDRESS-POINTER.                     
    
           SET ADDRESS OF CVT-POINTER TO WS-CVT-ADDR-POINTER.              
    
           SET ADDRESS OF CVT TO CVT-POINTER.                              
    
           SET ADDRESS OF JESCT TO JESCT-POINTER.                          
    
           SET ADDRESS OF SSCVT TO JESSSCVT-POINTER.                       
    
           DISPLAY 'SUBSYSTEM NAME=' SUBSYSTEM-NAME.                       
    
           PERFORM UNTIL NEXT-SSCVT IS = NULL                              
    
               SET ADDRESS OF SSCVT TO NEXT-SSCVT                          
    
               DISPLAY 'SUBSYSTEM NAME=' SUBSYSTEM-NAME                    
    
           END-PERFORM.                                                    
    
           DISPLAY '         '.                                            
    
      /                                                                    
    
       JFCB-INFO.                                                          
    
      *---------------------------------------------------------------     
    
      *    FIND DDNAMES AND ASSOCIATED DSNAMES                             
    
      *    PSA+X'21C' -> TCB -> TIOT -> TIOT SEG -> SWAREQ(SVA) -> JFCB    
    
      *---------------------------------------------------------------     
    
           MOVE X'0000021C' TO WS-TCB-ADDRESS-POINTER.                     
    
           SET ADDRESS OF TCB-POINTER TO WS-TCB-ADDR-POINTER.              
    
           SET ADDRESS OF TCB TO TCB-POINTER.                              
    
           SET ADDRESS OF TIOT TO TIOT-POINTER.                            
    
           SET WS-TIOT-SEG-POINTER TO TIOT-POINTER.                        
    
           ADD 24 TO WS-TIOT-SEG-PNT.                                      
    
           SET ADDRESS OF TIOT-SEG TO WS-TIOT-SEG-POINTER.                 
    
           PERFORM UNTIL TIO-LEN = LOW-VALUES                              
    
               MOVE ALL LOW-VALUES TO WS-POINT                             
    
               MOVE ALL LOW-VALUES TO WS-JFCB-POINT                        
    
               MOVE ALL LOW-VALUES TO WS-SWA-POINT                         
    
               MOVE SWA-V-ADDR TO WS-SWA-LOW-3                             
    
               PERFORM SWAREQ                                              
    
               SET ADDRESS OF JFCB TO  WS-POINTER                          
    
               DISPLAY 'DDNAME=' DD-NAME                                   
    
               DISPLAY 'DSNAME=' DS-NAME                                   
    
               DISPLAY 'VOL=SER=' VOL-SER                                  
    
               DISPLAY '********************************************'      
    
               MOVE ZERO TO WS-LEN                                         
    
               MOVE TIO-LEN TO WS-LENGTH(2:1)                              
    
               ADD WS-LEN TO WS-TIOT-SEG-PNT                               
    
               SET ADDRESS OF TIOT-SEG TO WS-TIOT-SEG-POINTER              
    
           END-PERFORM.                                                    
    
      /                                                                    
    
       SWAREQ.                                                             
    
           DIVIDE WS-SWA-PTR BY 16                                         
    
               GIVING WS-WORK                                              
    
               REMAINDER WS-RIGHT-HEX-DIGIT.                               
    
                                                                           
    
           IF WS-RIGHT-HEX-DIGIT NOT = 15                                  
    
               COMPUTE WS-PTR = WS-SWA-PTR + 16                            
    
           ELSE                                                            
    
               MOVE X'0000021C' TO WS-TCB-ADDRESS-POINTER                  
    
               SET ADDRESS OF TCB-POINTER TO WS-TCB-ADDR-POINTER           
    
               SET ADDRESS OF TCB TO TCB-POINTER                           
    
               SET ADDRESS OF JSCB TO JSCB-POINTER                         
    
               SET ADDRESS OF QMPL TO QMPL-POINTER                         
    
               SET ADDRESS OF QMAT TO QMAT-POINTER                         
    
               SET WS-QMAT-POINTER TO QMAT-POINTER                         
    
               PERFORM UNTIL WS-SWA-PTR <= 65536                           
    
                   SET WS-QMAT-POINTER TO QMAT-NEXT-POINTER                
    
                   SET ADDRESS OF QMAT TO QMAT-NEXT-POINTER                
    
                   COMPUTE WS-SWA-PTR = WS-SWA-PTR - 65536                 
    
               END-PERFORM                                                 
    
               COMPUTE WS-PTR = WS-SWA-PTR + WS-QMAT-PTR + 1               
    
               SET ADDRESS OF SWA TO WS-POINTER                            
    
               SET WS-POINTER TO JFCB-ADDR                                 
    
               COMPUTE WS-PTR = WS-PTR + 16                                
    
            END-IF.                                                        
    
      /                                                                    
    
       DCB-INFO.                                                           
    
      *---------------------------------------------------------------*    
    
      *    DISPLAY DCB INFORMATION                                    *    
    
      *    PSA+X'21C' - > TCB -> DEB -> DCB                           *    
    
      *---------------------------------------------------------------*    
    
           OPEN INPUT TEST-FILE.                                           
    
           MOVE ALL LOW-VALUES TO WS-DEB-POINT.                            
    
           MOVE X'0000021C' TO WS-TCB-ADDRESS-POINTER.                     
    
           SET ADDRESS OF TCB-POINTER TO WS-TCB-ADDR-POINTER.              
    
           SET ADDRESS OF TCB TO TCB-POINTER.                              
    
           SET WS-DEB-POINTER TO DEB-ADDR.                                 
    
           PERFORM UNTIL WS-DEB-POINTER IS = NULL                          
    
               SET ADDRESS OF DEB TO WS-DEB-POINTER                        
    
               MOVE ALL LOW-VALUES TO WS-DCB-POINT                         
    
               MOVE DCB-ADDR TO WS-DCB-LOW-3                               
    
               SET ADDRESS OF DCB TO WS-DCB-POINTER                        
    
TEST***********DISPLAY 'DCB-PTR=' WS-DCB-POINTER                           
    
               DISPLAY ' DDNAME=' DDNAME                                   
    
               DISPLAY '  DSORG=' DSORG                                    
    
               DISPLAY '  RECFM=' RECFM                                    
    
               DISPLAY 'BLKSIZE=' BLKSIZE                                  
    
               DISPLAY '  LRECL=' LRECL                                    
    
               IF DISK-3380-X2E                                            
    
                   DISPLAY 'DEVICE-TYPE=3380'                              
    
                   DISPLAY '**************************************'        
    
               ELSE IF DISK-3390-X2F                                       
    
                       DISPLAY 'DEVICE-TYPE=3390'                          
    
                       DISPLAY '**************************************'    
    
                    ELSE                                                   
    
                       DISPLAY 'DEVICE-TYPE=????'                          
    
                       DISPLAY 'DEVICE-TYPE=' DEVICE-TYPE                  
    
                       DISPLAY '**************************************'    
    
                    END-IF                                                 
    
               END-IF                                                      
    
TEST***********DIVIDE WS-LEN BY WS-TEST GIVING WS-WORK                     
    
               MOVE NEXT-DEB-ADDR TO WS-DEB-LOW-3                          
    
           END-PERFORM.                                                    
    
           CLOSE TEST-FILE.                                                
    
      /                                                                    
    
       JSAB-INFO.                                                          
    
           SET WS-JSAB-ADDR-POINTER TO NULL.                               
    
      *---------------------------------------------------------------*    
    
      *    DISPLAY JSAB INFORMATION                                   *    
    
      *    PSA+X'21C' - > TCB -> STCB -> JSAB                         *    
    
      *---------------------------------------------------------------*    
    
           MOVE X'0000021C' TO WS-TCB-ADDRESS-POINTER.                     
    
           SET ADDRESS OF TCB-POINTER TO WS-TCB-ADDR-POINTER.              
    
           SET ADDRESS OF TCB TO TCB-POINTER.                              
    
           SET ADDRESS OF STCB TO STCB-POINTER.                            
    
           IF JSAB-POINTER OF STCB IS NOT = NULL                           
    
               SET ADDRESS OF JSAB TO JSAB-POINTER OF STCB                 
    
               SET WS-JSAB-ADDR-POINTER TO JSAB-POINTER OF STCB            
    
           END-IF.                                                         
    
      *---------------------------------------------------------------*    
    
      *    PSA+X'224' - > ASCB -> ASSB -> JSAB                        *    
    
      *---------------------------------------------------------------*    
    
           IF WS-JSAB-ADDR-POINTER IS = NULL                               
    
               MOVE X'00000224' TO WS-ASCB-ADDRESS-POINTER                 
    
               SET ADDRESS OF ASCB-POINTER TO WS-ASCB-ADDR-POINTER         
    
               SET ADDRESS OF ASCB TO ASCB-POINTER                         
    
               IF ASSB-POINTER IS NOT = NULL                               
    
                   SET ADDRESS OF ASSB TO ASSB-POINTER                     
    
                   SET WS-ASSB-ADDR-POINTER TO ASSB-POINTER                
    
                   IF JSAB-POINTER OF ASSB IS NOT = NULL                   
    
                       SET ADDRESS OF JSAB TO JSAB-POINTER OF ASSB         
    
                       SET WS-JSAB-ADDR-POINTER TO JSAB-POINTER OF ASSB    
    
                   END-IF                                                  
    
               END-IF                                                      
    
           END-IF.                                                         
    
      *---------------------------------------------------------------*    
    
      *    IF JSAB-FLAG1 > 127 THE JSAB IS INVALID                    *    
    
      *---------------------------------------------------------------*    
    
           IF WS-JSAB-ADDR-POINTER IS = NULL                               
    
               CONTINUE                                                    
    
           ELSE                                                            
    
               MOVE ZERO TO WS-FLAG                                        
    
               MOVE JSAB-FLAG1 TO WS-FLAG1(2:1)                            
    
               PERFORM UNTIL WS-FLAG <= 127 OR                             
    
                             WS-JSAB-ADDR-POINTER IS = NULL OR             
    
                             JSAB-EYE-CATCHER NOT = 'JSAB'                 
    
                   SET WS-JSAB-ADDR-POINTER TO JSAB-NEXT-PTR               
    
                   SET ADDRESS OF JSAB TO WS-JSAB-ADDR-POINTER             
    
                   MOVE ZERO TO WS-FLAG                                    
    
                   MOVE JSAB-FLAG1 TO WS-FLAG1(2:1)                        
    
               END-PERFORM                                                 
    
           END-IF.                                                         
    
                                                                           
    
           IF WS-JSAB-ADDR-POINTER IS NOT = NULL                           
    
               DISPLAY 'EYE-CATCHER=' JSAB-EYE-CATCHER                     
    
               DISPLAY '  COMPONENT=' COMPONENT                            
    
               DISPLAY '     JOB ID=' JOB-ID                               
    
               DISPLAY ' JOB NUMBER=' JOB-ID                               
    
               DISPLAY '     USERID=' USERID                               
    
           ELSE                                                            
    
               DISPLAY 'JSAB INFORMATION NOT FOUND'                        
    
           END-IF.                                                         
    
//LKED.SYSLIB  DD                                                          
    
//             DD                                                          
    
//             DD DSN=PREFIX.DVL.BATLOAD,DISP=SHR                          
    
//LKED.SYSLMOD DD DSN=&&LOADLIB(COBPTR),DISP=(OLD,PASS)                    
    
//LKED.SYSIN DD *                                                          
    
  NAME COBPTR(R)                                                           
    
//GO.SYSUDUMP DD SYSOUT=*                                                  
    
//GO.SYSPRINT DD SYSOUT=*                                                  
    
//GO.SYSOUT   DD SYSOUT=*                                                  
    
//GO.SYSDBOUT DD SYSOUT=*                                                  
    
//GO.DD1      DD DSN=USERID.TEMP80,DISP=SHR                                
    




Maximo Ricardo Boettner <max.boettner@t-online.de> wrote in article
<apvv40$fj3$04$1@news.t-online.com>...
> Anybody that know work with POINTERS in cobol.
> I need an litle example.
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
