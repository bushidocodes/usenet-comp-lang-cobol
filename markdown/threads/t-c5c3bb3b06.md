[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# calling TSO-Commands from COBOL

_8 messages · 8 participants · 2000-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### calling TSO-Commands from COBOL

- **From:** michael_schaffler@my-deja.com
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85cmto$2i9$1@nnrp1.deja.com>`

```
Hello Cobol programmers,

in our programs often the situation arises, that a TSO-command has to
be called out of a Cobol programm. I once found a Cobol program, where
this was done by calling a program called "TSOLNK".

Does anyone have further information about that program "TSOLNK" Where
can I find documentation for it?
Do you know other ways of calling a TSO-Command out of COBOL-Programs?

Michael Schaffler
mailto:michael_schaffler@my-deja.com


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: calling TSO-Commands from COBOL

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85d52e$dsm$1@nnrp1.deja.com>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com>`

```
I'm not sure about TSOLNK, but TSO has some programming services that
are available as called subroutines, that will allow you to execute TSO
commands.  Find the documentation in this manual: TSO/E Programming
Services.  Here is the link:
http://www.s390.ibm.com/bookmgr-
cgi/bookmgr.cmd/BOOKS/IKJ3B702/CCONTENTS?SHELF=IKJOSE04

The subroutines are:
IKJTSOEV - initialize the TSO environment
IKJEFTSR - execute a TSO command.

-Art

In article <85cmto$2i9$1@nnrp1.deja.com>,
  michael_schaffler@my-deja.com wrote:
> Hello Cobol programmers,
>
> in our programs often the situation arises, that a TSO-command has to
> be called out of a Cobol programm. I once found a Cobol program, where
> this was done by calling a program called "TSOLNK".


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: calling TSO-Commands from COBOL

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85e7u4$9e9$1@nnrp1.deja.com>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com> <85d52e$dsm$1@nnrp1.deja.com>`

```
In article <85d52e$dsm$1@nnrp1.deja.com>,
  Art Perry <eowynfuzz@my-deja.com> wrote:
> I'm not sure about TSOLNK, but TSO has some programming services that
> are available as called subroutines, that will allow you to execute
TSO
> commands.  Find the documentation in this manual: TSO/E Programming
> Services.  Here is the link:
…[8 more quoted lines elided]…
>

<Rest Snipped>

Be aware that when using IKJEFTR that authorised commands ( such as
ALTER ) are NOT supported.

But the above page should be helpful. Also, refer to Bill Klein's reply
regarding Gilbert Saint-Flour's Page.

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: calling TSO-Commands from COBOL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000111125228.15825.00001660@ng-fo1.aol.com>`
- **References:** `<85d52e$dsm$1@nnrp1.deja.com>`

```
Art Perry writes...

>I'm not sure about TSOLNK, but TSO has some programming services that
>are available as called subroutines, that will allow you to execute TSO
…[8 more quoted lines elided]…
>

Our course Advanced TSO REXX Programming discusses these techniques and more
(and it's multilingual):

* IKJCT441 to access REXX variables from compiled programs in TSO environments

* IRXEXCOM to access REXX variables from compiled programs in both TSO and
non-TSO environments

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: calling TSO-Commands from COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85d58j$5ba$1@nntp9.atl.mindspring.net>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com>`

```
Check out

   http://members.home.net/gsf/tools/cob2tso.txt

I think it is exactly what you are looking for.

(Thank you as always to Gilbert Saint-flour)
```

#### ↳ Re:(How to) calling TSO-Commands from COBOL

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a%we4.1745$WV3.23969@news4.mia>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com>`

```
Here for the Group I am Posting this info:
(Manual Info)
COVER Book Cover
--------------------------------------------------------------------------
OS/390

TSO/E
Programming Services

Document Number SC28-1971-01

Program Number
5647-A01

File Number S370/390-39


---------------------------------



3.8.3 JCL for COBOL and Assembler Program Invocation

Figure 3-10 shows sample JCL to run the COBOL program.  The program
ENVCOBRX resides in IBMUSER.LOAD.  Because neither the program nor the
REXX exec that the program executes requires input, the JCL allocates
SYSTSIN to a dummy data set.  TSO/E uses the SYSTSPRT file to output
messages issued by the REXX exec.  Program DISPLAY statements send program
error messages to the SYSOUT file.

--------------------------------------------------------------------------

  file://IBMUSERA JOB 'IKJTSOEV SAMPLE1',MSGLEVEL=(1,1),TIME=2,
  //           CLASS=A,MSGCLASS=H
  file://*
  file://DOTSO    EXEC PGM=ENVCOBRX
  file://STEPLIB  DD   DSN=IBMUSER.LOAD,DISP=SHR
  file://SYSPROC  DD   DSN=IBMUSER.TSOENV.CLIST,DISP=SHR
  file://SYSTSPRT DD   SYSOUT=*
  file://SYSTSIN  DD   DUMMY
  file://SYSOUT   DD   SYSOUT=*


--------------------------------------------------------------------------
Figure  3-10. Execution JCL for the COBOL Program


Figure 3-11 shows sample JCL to run the assembler program.  The program
ENVTSCMD resides in IBMUSER.LOAD.  Because the program does not use
SYSTSIN for input, the JCL allocates SYSTSIN to a dummy data set.  The
program redirects output for the TSO/E command invocation to MYPRTDD,
which is allocated to a data set.  The program sends all other TSO/E
output is sent to the SYSTSPRT file.

--------------------------------------------------------------------------

  file://IBMUSERA JOB 'IKJTSOEV SAMPLE1',MSGLEVEL=(1,1),TIME=2,
  //           CLASS=A,MSGCLASS=H
  file://*
  file://DOTSO    EXEC PGM=ENVTSCMD
  file://STEPLIB  DD   DSN=IBMUSER.LOAD,DISP=SHR
  file://SYSPROC  DD   DSN=IBMUSER.TSOENV.CLIST,DISP=SHR
  file://SYSTSPRT DD   SYSOUT=*
  file://SYSTSIN  DD   DUMMY
  file://MYPRTDD  DD   SYSOUT=*
  file://SYSOUT   DD   SYSOUT=*


--------------------------------------------------------------------------
Figure  3-11. Execution JCL for the Assembler Program



3.8.1 COBOL

In Figure 3-6, a COBOL program calls IKJTSOEV to establish a TSO/E
environment.  The COBOL program then verifies that the environment has
been initialized successfully by checking the return code from the TSO/E
environment service.  If an error occurs, program DISPLAY statements write
error messages to the SYSOUT file, and the program ends.  After IKJTSOEV
successfully creates a TSO/E environment, the program invokes a TSO/E REXX
exec named 'TEST1' (Figure 3-7) using the TSO/E service facility.  TSO/E
writes the output from the REXX exec to the SYSTSPRT file.  Finally, the
program verifies successful invocation of the REXX exec by checking the
return code from the call to the TSO/E service facility.

--------------------------------------------------------------------------

  IDENTIFICATION DIVISION.
  PROGRAM-ID. ENVCOBRX.


****************************************************************************
  * THIS IS A SAMPLE COBOL PROGRAM TO DEMONSTRATE THE USE OF THE TSO/E
  * ENVIRONMENT SERVICE.  FIRST, THE PROGRAM CALLS IKJTSOEV TO ESTABLISH
  * A TSO/E ENVIRONMENT.  NEXT, THE PROGRAM CALLS THE TSO SERVICE FACILITY
  * (IKJEFTSR) TO INVOKE A REXX EXEC CALLED 'TEST1'.  AFTER THE REXX EXEC
  * IS INVOKED, THE PROGRAM DISPLAYS THE RETURN, REASON, AND ABEND CODES
  * FROM THE CALL TO THE TSO SERVICE FACILITY.

****************************************************************************

  EJECT
  ENVIRONMENT DIVISION.
  INPUT-OUTPUT SECTION.
  FILE-CONTROL.
  I-O-CONTROL.
  DATA DIVISION.
  FILE SECTION.
  WORKING-STORAGE SECTION.

    01 TSOEV-PARM1          PIC S9(9) VALUE +0   COMP-4.
    01 TSOEV-RETURN-CODE    PIC S9(9) VALUE +0   COMP-4.
    01 TSOEV-REASON-CODE    PIC S9(9) VALUE +0   COMP-4.
    01 TSOEV-ABEND-CODE     PIC S9(9) VALUE +0   COMP-4.
    01 TSOEV-CPPL-ADDR      PIC S9(9) VALUE +0   COMP-4.

    01 TSF-PARM1            PIC S9(9)            COMP-4.
    01 TSF-PARM2            PIC X(80).
    01 TSF-PARM3            PIC S9(9) VALUE +80  COMP-4.
    01 TSF-PARM4            PIC S9(9) VALUE +0   COMP-4.
    01 TSF-PARM5            PIC S9(9) VALUE +0   COMP-4.
    01 TSF-PARM6            PIC S9(9) VALUE +0   COMP-4.

    01 UNAUTH               PIC S9(9) VALUE +0   COMP-4.
    01 REQUEST-DUMP         PIC S9(9) VALUE +256 COMP-4.
    01 INVOKE-REXX          PIC S9(9) VALUE +1   COMP-4.


  EJECT
  PROCEDURE DIVISION.
  MAIN PROGRAM.

****************************************************************************
  * MAIN PROGRAM - INVOKE THE TSO/E ENVIRONMENT SERVICE TO INITIALIZE A
TSO/E
  *                ENVIRONMENT.
  *
  * TSOEV-RETURN-CODE IS A FULLWORD THAT WILL CONTAIN THE RETURN CODE FROM
  *          THE TSO/E ENVIRONMENT SERVICE.
  *
  * TSOEV-REASON-CODE IS A FULLWORD THAT WILL CONTAIN THE REASON CODE FROM
  *          THE TSO/E ENVIRONMENT SERVICE.
  *
  * TSOEV-CPPL-ADDR IS A FULLWORD THAT WILL CONTAIN THE ADDRESS OF THE CPPL
  *          ON RETURN FROM THE TSO/E ENVIRONMENT SERVICE.

****************************************************************************

       CALL 'IKJTSOEV' USING TSOEV-PARM1
                             TSOEV-RETURN-CODE
                             TSOEV-REASON-CODE
                             TSOEV-ABEND-CODE
                             TSOEV-CPPL-ADDR.


****************************************************************************
  * NOW THAT WE'RE BACK FROM THE TSO/E ENVIRONMENT SERVICE, CHECK THE
  * RETURN CODE.
  *
  * IF THE RETURN CODE WAS ZERO, ISSUE IKJEFTSR TO INVOKE A REXX EXEC.
  * IF THE RETURN CODE WAS NON-ZERO, DISPLAY AN ERROR MESSAGE.

****************************************************************************

       IF RETURN-CODE = 0 THEN
          PERFORM EXEC-REXX THROUGH EXEC-REXX-EXIT
       ELSE
          PERFORM DISPLAY-MESSAGE THROUGH DISPLAY-MESSAGE-EXIT.

       STOP RUN.



****************************************************************************
  * EXEC-REXX  - EXECUTE THE REXX EXEC 'TEST1' USING THE TSO SERVICE
FACILITY
  *
  * PARM1 WILL INDICATE THAT A TSO/E COMMAND, CLIST, OR REXX EXEC IS BEING
  *       INVOKED AND A DUMP SHOULD BE PRODUCED IF AN ABEND OCCURS.
  *
  * PARM2 WILL CONTAIN THE NAME OF THE REXX EXEC - 'TEST1'
  *
  * PARM3 WILL CONTAIN THE RETURN CODE FROM THE INVOCATION OF THE REXX
  *       EXEC 'TEST1'.
  *
  * PARM4 WILL CONTAIN THE RETURN CODE FROM THE TSO SERVICE FACILITY
  *
  * PARM5 WILL CONTAIN THE REASON CODE FROM THE TSO SERVICE FACILITY
  *
  * PARM6 WILL CONTAIN THE ABEND CODE FROM THE TSO SERVICE FACILITY
  *

****************************************************************************

  * INITIALIZE PARM1
       MOVE 0 TO TSF-PARM1.
       ADD UNAUTH TO TSF-PARM1.
       ADD REQUEST-DUMP TO TSF-PARM1.
       ADD INVOKE-REXX TO TSF-PARM1.

  * INITIALIZE PARM2
       MOVE SPACES TO TSF-PARM2.
       MOVE 'EXEC TEST1' TO TSF-PARM2.

  * INVOKE THE TSO SERVICE FACILITY
       CALL 'TSOLNK' USING TSF-PARM1
                           TSF-PARM2
                           TSF-PARM3
                           TSF-PARM4
                           TSF-PARM5
                           TSF-PARM6.

       DISPLAY 'IKJEFTSR RETURNED THE FOLLOWING:'
       DISPLAY '  FUNCTION RETURN CODE - ' TSF-PARM4.
       DISPLAY '  RETURN CODE          - ' TSF-PARM6.
       DISPLAY '  REASON CODE          - ' TSF-PARM5.
       DISPLAY '  ABEND CODE           - ' TSF-PARM6.

  EXEC-REXX-EXIT.



****************************************************************************
  * DISPLAY MESSAGE - DISPLAY THE RETURN, REASON, AND ABEND CODES FROM
  *                   IKJTSOEV.

****************************************************************************
  DISPLAY-MESSAGE.

       DISPLAY 'IKJTSOEV RETURNED THE FOLLOWING:'
       DISPLAY '  RETURN CODE          - ' TSOEV-RETURN-CODE.
       DISPLAY '  REASON CODE          - ' TSOEV-REASON-CODE.
       DISPLAY '  ABEND CODE           - ' TSOEV-ABEND-CODE.

  DISPLAY-MESSAGE-EXIT.


--------------------------------------------------------------------------
Figure  3-6. Sample COBOL Routine

--------------------------------------------------------------------------

  /* REXX */
  SAY HI, IN TEST1


--------------------------------------------------------------------------
Figure  3-7. REXX Exec 'TEST1' Executed by COBOL

--------------------------------------------------------------------------

  HI, IN TEST1


--------------------------------------------------------------------------
Figure  3-8. Output From the Invocation of 'TEST1'



23.6.1.2 COBOL

For calls in COBOL the format for invoking the TSO/E service facility from
functions by using TSOLNK is:

  CALL 'TSOLNK' USING PARM1 PARM2 PARM3 PARM4 PARM5 PARM6.

In COBOL programs, you should include the following:

--------------------------------------------------------------------------

  * DEFINE STORAGE FOR PARMS
  *    PARM1 IS DECIMAL VALUE OF FLAGS
  *    PARM2 IS COMMAND TEXT
  *    PARM3 IS COMMAND LENGTH (SET TO 80)
  *    PARM4 IS FUNCTION RETURN CODE VALUE FROM TSOLNK
  *    PARM5 IS TSF REASON CODE VALUE FOR ABEND FROM TSOLNK
  *    PARM6 IS FUNCTION ABEND CODE VALUE FROM TSOLNK

   01  PARM1 PICTURE S9(9) COMP.
   01  PARM2 PICTURE X(80).
   01  PARM3 PICTURE S9(9) VALUE +80 COMP.
   01  PARM4 PICTURE S9(9) VALUE +0 COMP.
   01  PARM5 PICTURE S9(9) VALUE +0 COMP.
   01  PARM6 PICTURE S9(9) VALUE +0 COMP.


--------------------------------------------------------------------------
Figure 23-11. Format of the Parameter List Written in COBOL


23.7.11 COBOL Program Using TSOLNK to Invoke a Program

--------------------------------------------------------------------------

   ID DIVISION.
   PROGRAM-ID.   TSOSVR.
  *     THIS COBOL PROGRAM ISSUES THE IEBCOPY PROGRAM IN TSO/E AND
  *     THEN PRINTS OUT THE COMMAND BUFFER  AND THE RETURN, REASON
  *     AND ABEND CODES RESULTING FROM THE EXECUTION OF THE TSO
  *     SERVICE FACILITY.  TO USE THE EXAMPLE THE USER MUST ALLOCATE
  *     THE FOLLOWING FILES:
  *          ALLOC F(SYSPRT) DSN(*)
  *          ALLOC F(SYSIN) DSN(YOUR.SYSIN)
  *          ALLOC F(SYSPRINT) DSN(*)
  *          ALLOC F(INDD) DSN(YOUR.INPDS)
  *          ALLOC F(OUTDD) DSN(YOUR.OUTPDS)
  *     THE EXAMPLE REQUIRES THE FOLLOWING CARD IN YOUR.SYSIN FILE:
  *          EXAMPLE    COPY  OUTDD=OUTDD,INDD=INDD
  *
  * THIS PROGRAM WILL RUN ON THE OS/VS COBOL COMPILER RELEASE 3 OR
  * HIGHER

   ENVIRONMENT DIVISION.
   INPUT-OUTPUT SECTION.
   FILE-CONTROL.

  *    DEFINE OUTPUT DEVICE

       SELECT TRMPRT ASSIGN TO UT-S-SYSPRT.
   DATA DIVISION.
   FILE SECTION.

       DEFINE OUTPUT FILE

   FD  TRMPRT
       LABEL RECORDS ARE OMITTED
       RECORD CONTAINS 133 CHARACTERS.

  *    DEFINE OUTPUT RECORD

   01  OUTREC.
       02 OUT-LINE     PICTURE X(133).


   WORKING-STORAGE SECTION.

  *    DEFINE OUTPUT RECORD FORM

   01  OUT-RECORD.
       02 CONTROL-CHAR PICTURE X VALUE SPACE.
       02 COMMENT      PICTURE X(25).
       02 OUT-VALUE    PICTURE +++++++++9.
       02 FILLER       PICTURE X(111) VALUE SPACES.

  *    DEFINE COMMENT VALUES FOR OUTPUT RECORD FORM

   01  RETURN-COMMENT PICTURE X(25) VALUE 'FUNCTION RETURN CODE IS  '.
   01  REASON-COMMENT PICTURE X(25) VALUE '     TSF REASON CODE IS '.
   01  ABEND-COMMENT  PICTURE X(25) VALUE 'FUNCTION ABEND  CODE IS  '.


  *    DEFINE FLAGS TO BE FULL WORDS WITH APPROPRIATE BITS ON

   01  FLAG1-ON  PICTURE S9(9) VALUE +16777216 COMP.
   01  FLAG2-ON  PICTURE S9(9) VALUE +65536 COMP.
   01  FLAG3-ON  PICTURE S9(9) VALUE +256 COMP.
   01  FLAG4-ON  PICTURE S9(9) VALUE +2 COMP.
   01  FLAG1-OFF PICTURE S9(9) VALUE +0 COMP.
   01  FLAG2-OFF PICTURE S9(9) VALUE +0 COMP.
   01  FLAG3-OFF PICTURE S9(9) VALUE +0 COMP.
   01  FLAG4-OFF PICTURE S9(9) VALUE +1 COMP.


  * DEFINE STORAGE FOR PARMS
  *    PARM1 IS DECIMAL VALUE OF FLAGS
  *    PARM2 IS FUNCTION TEXT
  *    PARM3 IS FUNCTION LENGTH (SET TO 80)
  *    PARM4 IS FUNCTION RETURN CODE VALUE FROM TSOLNK
  *    PARM5 IS TSF REASON CODE VALUE FROM TSOLNK
  *    PARM6 IS FUNCTION ABEND CODE VALUE FROM TSOLNK

   01  PARM1 PICTURE S9(9) COMP.
   01  PARM2 PICTURE X(80).
   01  PARM3 PICTURE S9(9) VALUE +80 COMP.
   01  PARM4 PICTURE S9(9) VALUE +0 COMP.
   01  PARM5 PICTURE S9(9) VALUE +0 COMP.
   01  PARM6 PICTURE S9(9) VALUE +0 COMP.


   PROCEDURE DIVISION.

  *    MOVE DESIRED FUNCTION TO PARM2

   READY-COMMAND.
       MOVE SPACES TO PARM2.
       MOVE 'IEBCOPY' TO PARM2.

  *    SET FLAGS BY ADDING APPROPRIATELY VALUED FLAG VARIABLES


   READY-FLAGS.
       MOVE 0 TO PARM1.

  *    RESERVED FLAG

       ADD FLAG1-OFF TO PARM1.

  *    RESERVED FLAG

       ADD FLAG2-OFF TO PARM1.

  *    FLAG3-ON TO REQUEST ABEND WITH DUMP

       ADD FLAG3-ON  TO PARM1.

  *    FLAG4-OFF TO REQUEST A TSO/E PROGRAM (NOT A COMMAND) BE INVOKED

       ADD FLAG4-ON TO PARM1.

  *    CALL TSOLNK


   CALL-TSOLNK.
       CALL 'TSOLNK' USING PARM1 PARM2 PARM3 PARM4 PARM5 PARM6.

  *    PRINT RESULTS

   PRINT-COMMENTS.
       OPEN OUTPUT TRMPRT.

  *    PRINT THE FUNCTION RETURN CODE

       MOVE RETURN-COMMENT TO COMMENT.
       MOVE PARM4 TO OUT-VALUE.
       WRITE OUTREC FROM OUT-RECORD.

  *    PRINT THE TSF REASON CODE

       MOVE REASON-COMMENT TO COMMENT.
       MOVE PARM5 TO OUT-VALUE.
       WRITE OUTREC FROM OUT-RECORD.

  *    PRINT THE FUNCTION ABEND CODE

       MOVE ABEND-COMMENT TO COMMENT.
       MOVE PARM6 TO OUT-VALUE.
       WRITE OUTREC FROM OUT-RECORD.

       CLOSE TRMPRT.
       STOP RUN.


--------------------------------------------------------------------------
Figure 23-24. COBOL Program Demonstrating the Use of TSOLNK to Invoke a
              Program


<michael_schaffler@my-deja.com> wrote in message
news:85cmto$2i9$1@nnrp1.deja.com...
> Hello Cobol programmers,
>
…[13 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: calling TSO-Commands from COBOL

- **From:** "Kevin A. Howard" <khoward@asacomp.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85p19u$qal$1@news.asacomp.com>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com>`

```
Michael:

This sounds like a home grown program, or perhaps an alias entry for
IKJEFT01...without the program, I cannot be sure.

Another method to try:

WORKING STORAGE
01  WS-IKJEFT01      PIC X(08) VALUE 'IKJEFT01'.

Have your program open/write to/close file SYSTSIN with the TSO command(s)
you want to execute.  Then CALL WS-IKJEFT01.  You shouldn't need a steplib
because TSO should be in the linklist.

The reason for the working storage variable is to ensure that you get a
dynamic link and don't have to recompile or relink your program every time
your sys prog installs maintenance or a newer version of TSO.  As long as
you have all of the necessary DD statements in your JCL, it should work.
Look at your TSO logon proc or issue command: LISTA HISTORY,STATUS,SYSNAMES
from a TSO ready or command entry prompt.

I have never had the need to do this, but it should work.

I hope this info helps.
-Kevin Howard


<michael_schaffler@my-deja.com> wrote in message
news:85cmto$2i9$1@nnrp1.deja.com...
> Hello Cobol programmers,
>
…[13 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: calling TSO-Commands from COBOL

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3880ac0a$1$tfs$mr2ice@news>`
- **References:** `<85cmto$2i9$1@nnrp1.deja.com> <85p19u$qal$1@news.asacomp.com>`

```
On 15 Jan 2000 at 00:41, "Kevin A. Howard" <khoward@asacomp.com> said:
>Another method to try:
> WORKING STORAGE
…[3 more quoted lines elided]…
>You shouldn't need a steplib because TSO should be in the linklist.

Don't bother trying this, because IKJEFT01 must run authorized and your
program probably isn't.  All you'll get is an S047 abend or such.

To create a TSO environment in COBOL and execute commands, use the sample
program called COB2TSO that's on my Web page.

 Gilbert Saint-flour
 http://members.home.net/gsf/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
