[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Universal record size

_6 messages · 4 participants · 2002-10_

---

### Re: Universal record size

- **From:** "Bj���rn Sune Andersen" <bsa@post2.tele.dk>
- **Date:** 2002-10-29T06:07:30+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org>`

```
What I mean is to write something that can operate like SORT - SORT can use
files with different record lenghts as input (I'm not suggesting
concatenation!).


Bj�rn

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.00000287.053afe3b@ieee.org...
> Bj�rn,
>
> > The should be able to read files with fixed variable
> > record sizes, ie. every time the program is executed the input is a
fixed
> > recordlength file, but the record length may vary from execution to
> > execution (eg. 80 characters and 132 characters).
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Universal record size

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-10-29T12:14:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<sYuv9.2232$mN6.645976@newssrv26.news.prodigy.com>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org> <3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk>`

```
ENVIRONMENT DIVISION

            SELECT FIXED-LENGTH-VARIABLE-FILE
             ORGANIZATION SEQUENTIAL
             ACCESS SEQUENTIAL
            ASSIGN TO  whatever

FILE SECTION.
FD FIXED-LENGTH-VARIABLE-FILE
  RECORD IS VARYING IN SIZE FROM n1 TO n2 CHARACTERS
     DEPENDING ON FLV-LENGTH
01 DATA         PIC X(N2).

WORKING-STORAGE SECTION.
01 FLV-LENGTH  PIC 9(04) USAGE COMP.

(Syntax might be slightly off but it's close).

FLV-LENGTH will contain record length after each successful READ. (And must
be set to correct value before doing any WRITE).
```

##### ↳ ↳ Re: Universal record size

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-10-30T00:25:01+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<01c27faa$c62cfc40$4d95f243@chottel>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org> <3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk> <sYuv9.2232$mN6.645976@newssrv26.news.prodigy.com>`

```
If you understand Cobol pointers you could use them to point to the DCB for
the file.  The layout/map/DSECT for the DCB can be found in the assembler
macro  DCBD DSORG=PS.  You want the displacement to the DCBLRECL field. You
can use this record length to set FLV-LENGHT in Mike's sample code.  Here
is a sample program that use pointers. Look for the part that addresses the
DCB:

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
    




Michael Mattias <michael.mattias@gte.net> wrote in article
<sYuv9.2232$mN6.645976@newssrv26.news.prodigy.com>...
> ENVIRONMENT DIVISION
> 
…[16 more quoted lines elided]…
> FLV-LENGTH will contain record length after each successful READ. (And
must
> be set to correct value before doing any WRITE).
> 
…[26 more quoted lines elided]…
> > > In that case, it's not fixed. How do you know the length of the
record?
> > >
> > > ---
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Universal record size

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-10-30T00:31:22+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<01c27fab$ac08fac0$4d95f243@chottel>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org> <3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk> <sYuv9.2232$mN6.645976@newssrv26.news.prodigy.com> <01c27faa$c62cfc40$4d95f243@chottel>`

```
I forgot to mention you should open the file before you access the DCBLRECL
field for the length.

<snip>
```

###### ↳ ↳ ↳ Re: Universal record size - Found the answer

- **From:** "Bj���rn Sune Andersen" <bsa@post2.tele.dk>
- **Date:** 2002-10-30T13:42:23+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3dbfd3d0$0$97631$edfadb0f@dspool01.news.tele.dk>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org> <3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk> <sYuv9.2232$mN6.645976@newssrv26.news.prodigy.com> <01c27faa$c62cfc40$4d95f243@chottel>`

```
FD Some-file
   RECORD CONTAINS 0 CHARACTERS
   BLOCK CONTAINS 0 CHARACTERS
   DATA RECORD IS Some-record

01 Some-record    PIC X(Some-length)

Because:

COBOL for MVS Language Reference

When running under MVS, BLOCK CONTAINS 0 can be specified for QSAM files;
the block size is determined at run time from the DD parameters or the data
set label.
If the RECORD CONTAINS 0 CHARACTERS clause is specified, and the BLOCK
CONTAINS 0 CHARACTERS clause is specified (or omitted), the block size is
deter-mined at run time from the DD parameters or the data set label of the
file. For output data sets, with either of the above conditions, the DCB
used by Language Environment will have a zero block size value. If you do
not specify a block size value, the operating system might select a System
Determined Block Size (SDB). See the operating system specifications for
further information on SDB.

Thanks for the input.


Bj�rn
```

#### ↳ Re: Universal record size

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2002-10-29T20:24:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000288.0a62a168@ieee.org>`
- **References:** `<3dbd8c6b$0$28830$edfadb0f@dspool01.news.tele.dk> <VA.00000287.053afe3b@ieee.org> <3dbe1790$0$97659$edfadb0f@dspool01.news.tele.dk>`

```
Bjï¿½rn,

> What I mean is to write something that can operate like SORT - SORT can use
> files with different record lenghts as input (I'm not suggesting
> concatenation!).

On MVS, the largest slab of SORT code is to do with input-output - sorting is 
relatively trivial.

Generally, you use BLOCK CONTAINS 0 and let the JCL sort it out in the DCB 
statement. So your Cobol program doesn't have to know what the record or 
block size is.

If you have one record per block, then you can use RECFM=U in the JCL and it 
will read in every block and hand it over to the program as a single record. 
But record formatting can be complex - I'd have a look at what you can 
achieve with JCL.


---

Doug

dwscott@ieee.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
