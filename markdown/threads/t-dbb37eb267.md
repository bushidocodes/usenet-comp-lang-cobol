[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic allocations in COBOL

_7 messages · 4 participants · 2001-11_

---

### Dynamic allocations in COBOL

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2001-11-09T06:35:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bebcd8a$1_4@news.newzpig.com>`

```
Someone asked this at work and I have never heard of it so maybe the
comp.lang.cobol can help.

It is my understanding that there is a way to dynamically allocate files
from inside a Cobol program. For example, Lets say I have an input that
needs to be split into a varying number of outputs. Rather than having
hardcoded DD statements for every possible output file, the DDs can be
allocated dynamically from the program itself. On one day there may be
10 output DDs and the next may have 30 output DDs based on the input?

COBOL in use is COBOL II and COBOL for MVS

This message has also been posted on the Mainframe Forum
www.mainframeforum.com
```

#### ↳ Re: Dynamic allocations in COBOL

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2001-11-09T08:08:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bebe357_5@news.newzpig.com>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com>`

```
Thanks Steve this is a big help. I am not sure at what point we will go
ot COBOL OS/390 2.2. but this is good idea should we ever get there.
```

#### ↳ Re: Dynamic allocations in COBOL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-11-09T14:29:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011109092948.23316.00001681@mb-ck.aol.com>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com>`

```
COBOLMAN writes...

>Someone asked this at work and I have never heard of it so maybe the
>comp.lang.cobol can help.
…[12 more quoted lines elided]…
>

Well, yes and no. 

The general case is: yes, you can do dynamic allocation by calling a subroutine
that does SVC 99 type stuff; you were asking, I presume, about doing this
without calling a subroutine.

To do dynamic allocation directly in IBM mainframe COBOL requires COBOL for
OS/390, V2R2. Example:

.
.
.
          select persnnl assign to people.
.
.
.
 01  file-stuff.
      02  file-ptr      pointer.
      02  file-name.
            03                 pic x(12) value 'PEOPLE=DSN('.
            03  dsname   pic x(54) value spaces.
            03  disp         pic x(05) value ' SHR '.
      02  rc    pic s9(9) binary value 0.
.
.
.
 linkage section.
 01  in-name  pic x(54).
 procedure division using in-name.
      string in-name delimited by space
                  ')'        delimited by size into dsname
      set file-ptr to address of file-name
      call 'putenv' using by value file-ptr returning rc
      open input persnnl
.
.
.


If the file name is passed to this program from a calling program, and if at
run-time you do _NOT_ supply a dd statement named PEOPLE, then this code will
dynamically allocate the passed file name to the file name 'persnnl'.

<ad>
There are details not discussed in this short post. This, and a lot more, is
included in our two-day course "Beyond COBOL II", which brings COBOL
programmers up to date in the language facilities of COBOL from COBOL II V2R3
up through the latest release of COBOL for OS/390 & VM.

Details on this course can be found at
http://www.trainersfriend.com/d204descr.htm

</ad>


Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Dynamic allocations in COBOL

- **From:** "Albert W. Paul" <alpaul@mindspring.com>
- **Date:** 2001-11-09T10:18:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9sgrt0$9fp$1@slb6.atl.mindspring.net>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com>`

```

The following email is a copy of the documentation for Dynam. It does
exactly what you
are looking for. You can have a program that uses all kinds of files that do
not have any defined assignments or references in the JCL.

It could drive the operators and tech support crazy as they can not change
anything in the job stream.

If I can be of further assistance in how to use it, let me know.


"COBOLMAN" <member@mainframeforum.com> wrote in message
news:3bebcd8a$1_4@news.newzpig.com...
> Someone asked this at work and I have never heard of it so maybe the
> comp.lang.cobol can help.
…[18 more quoted lines elided]…
> www.MainFrameForum.com USENET Gateway
```

##### ↳ ↳ Re: Dynamic allocations in COBOL

- **From:** "Albert W. Paul" <alpaul@mindspring.com>
- **Date:** 2001-11-09T10:20:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9sgs0r$rft$1@nntp9.atl.mindspring.net>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com> <9sgrt0$9fp$1@slb6.atl.mindspring.net>`

```
DYNAM

Dynamic Allocation Interface


INTRODUCTION
DYNAM provides an interface between a high level language such as COBOL or
PLI, and SVC 99, the system dynamic allocation  routine.  It allows the user
to acquire system resources as the need arises and free them when they are
no longer required.  DYNAM takes simple parameters consisting of character
strings and translates them into the text units required by SVC 99.  In
addition, a special information retrieval function can be called to provide
all the information available about a particular allocation.  This
information is returned in a fixed format data structure.  For more
information about SVC 99 refer to the IBM manual:

OS/VS2 MVS SYSTEM PROGRAMMING LIBRARY: JOB MANAGEMENT GC28-0627-2


WORK AREA
The first parameter to DYNAM is a work area.  This work area can be supplied
by the user or can be obtained for the user by DYNAM. If obtained by DYNAM
it can be used by subsequent calls to DYNAM and freed later, or can be
acquired and freed on the same call.  If the user supplies a work area, the
first word of the work area must contain the length in bytes.

 FORTRAN
  INTEGER WORK(500)/2000/
  CALL DYNAM (WORK, . . .)

 PLI
  DCL 1 WORK AREA,
  2 WA_LENGTH   FIXED BIN (31) INIT (2000),
  2 FILLER      CHAR (2000);
  CALL DYNAM (WORK, . . .)

 COBOL
  01  WORK.
         02  WORK-LEN  PIC S9(9) COMP SYNC VALUE +2000.
         02  WORK-AREA PIC X(2000).
  . . .
  CALL 'DYNAM' USING WORK . . .

If DYNAM is to supply its own work area, this can be done explicitly by
coding:

 DCL WORK    FIXED BIN(31) INIT(0);
 CALL DYNAM (WORK, 'INIT')

WORK then becomes a reference to the acquired work area and must be
specified on all subsequent calls to DYNAM as the first parameter.  The work
area can later be free by coding:

 CALL DYNAM (WORK, 'END')

If DYNAM is to acquire a work area to be used only during one invocation,
the work area is implicitly acquired by coding:

 CALL DYNAM (0, . . .)

This is used when the programmer only wants to perform one dynamic
allocation and then continue with his program.


OPERATIONS
The second parameter to DYNAM describes the operation you wish to perform.
There are two different  types of operations, those that have to do with
dynamic allocation and those that have to do with the interface itself.

 Interface Operations
 INIT  acquire a work area
 END  free the work area previously acquired by INIT

 Allocation Operations
 ALLOC  allocate a data set
 UNALLOC unallocate a data set
 CONCAT concatenate 2 or more DD names
 UNCONCAT unconcatenate previously concatenated DD names.
 REMOVE remove in-use attribute
 DDALLOC allocate a DD name
 INFO  retrieve information about an allocation


OPERANDS
The third and subsequent parameters supply operands needed to perform
dynamic allocation.  Only one operand parameter is required but it is
sometimes convenient to use a larger number, for example when obtaining
allocation parameters from a user at a terminal in an interactive manner.
Normal OS linkage conventions flag the last parameter in a parameter list so
a variable number of parameters is easily allowed if the high level host
language supports it.  Operand parameters must be delimited on the right by
a semicolon. Operands consist of a keyword and an optional value. if a value
is present it is separated from the keyword by an equals (=)  sign.
Operands are separated from each other by one of more spaces and an operand
string is delimited on the right by a semicolon.  If a keyword requires a
list of values, the values in the list are separated by a comma. Keywords
may be abbreviated by specifying enough of the keyword so that it is
unambiguous.  In cases where an entire keyword is  the same as the first few
letters of a longer keyword, ambiguity is resolved by picking the first
keyword.  In describing DYNAM keywords below the  unambiguous portion of the
keyword is written in uppercase.  An attempt has been made to minimize the
number of key words that require values.


ALLOC

This operation is equivalent to data set allocation during job step
initialization; the parameter list  to DYNAM is
 equivalent to a DD statement.   You can request most of the JCL services
that you can code on a DD statement.  In addition you can specify data set
passwords which do not have a JCL equivalent.  The following is a list of
JCL parameters and the equivalent DYNAM keyword.

 DD card parameter   DYNAM keyword

 COPIES=num    COPies=num
 DCB=(*.ddname)   DCBDD=ddname
 DCB=(dsname)    DCBDS=dsname
 DCB=(BLKSIZE=num)   BLKsize=num
 DCB=(BUFALN=key)   BUFAln=key  (key = D�F)
 DCB=(BUFIN=num)   BUFIN=num
 DCB=(BUFL=num)   BUFL=num
 DCB=(BUFMAX=num)   BUFMAX=num
 DCB=(BUFNO=num)   BUFNo=num
 DCB=(BUFOFF=num)   BUFOFf=num
 DCB=(BUFOUT=num)   BUFOUt=num
 DCB=(BUFRQ=num)   BUFRq=num
 DCB=(BUFSIZE=num)   BUFSize=num
 DCB=(BUFTEK=key)   BUFTEK=key  (key = A E R S)
 DCB=(CODE=key)   CODe=key  (key = A B C F I N T)
 DCB=(DEN=2)    D800
 DCB=(DEN=3)    D1600
 DCB=(DEN=4)    D6250
 DCB=(DIAGNS=TRACE)  TRAce
 DCB=(DSORG=key)   DSORG=key  (key = CX DA DAU GS
              PO PS PSU TQ
              TX TCAM VSAM)
 DCB=(EROPT=ABE)   ABE
 DCB=(EROPT=ACC)   ACC
 DCB=(EROPT=SKP)   SKp
 DCB=(KEYLEN=num)   KEYlen=num
 DCB=(LIMCT=num)   LImct=num
 DCB=(LRECL=num)   LRecl=num
 DCB=(MODE=key)   MODE=key  (key = C CO CR E EO ER)
 DCB=(NCP=num)   NCP=num
 DCB=(OPTCD=key)   OPTCD=key  (see note 1 below)
 DCB=(PRTSP=key)   PRTsp=key  (key = 0 1 2 3)
 DCB=(RECFM=key)   RECFM=key  (see note 2 below)
 DCB=(RECFM=F)   F
 DCB=(RECFM=FA)   FA
 DCB=(RECFM=FAS)   FAS
 DCB=(RECFM=FB)   FB
 DCB=(RECFM=FBA)   FBA
 DCB=(RECFM=FBAS)   FBAS
 DCB=(RECFM=FBM)   FBM
 DCB=(RECFM=FBS)   FBMS
 DCB=(RECFM=FM)   FM
 DCB=(RECFM=FMS)   FMS
 DCB=(RECFM=FS)   FS
 DCB=(RECFM=U)   U
 DCB=(RECFM=V)   V
 DCB=(RECFM=VA)   VA
 DCB=(RECFM=VAS)   VAS
 DCB=(RECFM=VB)   VB
 DCB=(RECFM=VBA)   VBA
 DCB=(RECFM=VBAS)   VBAS
 DCB=(RECFM=VBM)   VBM
 DCB=(RECFM=VBMS)   VBMS
 DCB=(RECFM=VBS)   VBS
 DCB=(RECFM=VM)   VM
 DCB=(RECFM=VMS)   VMS
 DCB=(RECFM=VS)   VS
 DCB=(STACK=num)   STACK=num
 DCB=(TRTCH=key)   TRTch=key  (key = C E ET T)
 DISP=(MOD)    MOD
 DISP=(NEW)    NEW
 DISP=(OLD)    OLD
 DISP=(SHR)    SHr
 DISP=(,CATLG)    CAtlg
 DISP=(,DELETE)   DElete
 DISP=(,KEEP)    KEEp
 DISP=(,UNCATLG)   UNCatlg
 DISP=(,,CATLG)   CCatlg
 DISP=(,,DELETE)   CDelete
 DISP=(,,KEEP)    CKeep
 DISP=(,,UNCATLG)   CUncatlg
 DSN=(name)    MEmber=name
 DSN=dsname    DSN=dsname
 DUMMY    DUMMY
 FCB=(name)    FORms=name
 FCB=(,ALIGN)    ALIgn
 FCB=(,VERIFY)    VERIFYF
 FREE=CLOSE    CLose
 HOLD=YES    Hold
 LABEL=(num)    DSSeq=num
 LABEL=(EXPDT=yyddd)   Expdt=yyddd
 LABEL=(RETPD=num)   RETpd=num
 LABEL=(,AL)    AL
 LABEL=(,AUL)    AUL
 LABEL=(,BLP)    BLP
 LABEL=(,LTM)    LTM
 LABEL=(,NL)    NL
 LABEL=(,NSL)    NSL
 LABEL=(,SL)    SL
 LABEL=(,SUL)    SUL
 LABEL=(,,IN)    Input
 LABEL=(,,NOPWREAD)   PASSWRite
 LABEL=(,,OUT)    OUTput
 LABEL=(,,PASSWORD)   PASSRead
 MSVGP=name    MSVGP=name
 OUTLIM=num    OUTLim=num
 QNAME=name    QNAME=name
 SPACE=(num)    BLOck=num
 SPACE=(CYL)    CYL
 SPACE=(TRK)    TRK
 SPACE=(,(num))    PRIMary=num
 SPACE=(,(,num))   SECondary=num
 SPACE=(,(,,num))   DIRectory=num
 SPACE=(,,RLSE)   RLse
 SPACE=(,,,ALX)    ALX
 SPACE=(,,,CONTIG)   CONtig
 SPACE=(,,,MXIG)   MXIG
 SPACE=(,,,,ROUND)   ROund
 SYSOUT=name    SYSOUt=name
 SYSOUT=(,name)   SYSOUProg=name
 SYSOUT=(,,name)   SYSOUForms=name
 TERM=TS    TErmfile
 UCS=(,FOLD)    FOLdmode
 UCS=(,,VERIFY)   VERIFYC
 UNIT=name    UNIT=name
 UNIT=(,num)    UNITCount=num
 UNIT=(,P)    PARallel
 VOL=(,,num)    VOLSeq=num
 VOL=(,,,num)    VOLCount=num
 VOL=(,,,,REF=name)   VOLRef=name
 VOL=(,,,,SER=(name))   VOLume=name
 VOL=(PRIVATE)   PRIVate

note 1:  For a complete listing of possible values for the  OPTCD parameter
refer  to the  IBM manual
OS/VS2 JCL.
note 2:  In  addition to the stand alone keywords for Fixed, Undefined,  and
Variable record formats others may be coded by using the RECFM=key key-word.
For a complete listing refer to the IBM manual OS/VS2 JCL.

 Others       DYNAM keyword
 DDNAME on DD card     DD=name
 PASSWORD      PASSWOrd=password
 /*ROUTE dest      REMOTE=dest
 assign the permanently allocated attribute to this resource PERManent
 assign the convertible attribute to this resource  CONVert

note:  For a complete explanation of the permanently allocated attribute and
the convertible attribute refer to SPL: JOB MANAGEMENT.


ALLOCR
This operation is the same as ALLOC except that information about the
allocation is to be returned to the caller.  The third parameter to DYNAM is
a data  area into which information is to be placed.  The fourth and
subsequent parameters are the same as the third and subsequent parameters
for the ALLOC operation.

The information data area has the following format:

 DCL 1 RETURN_AREA UNALIGNED,
      2 DDNAME  CHAR (8),
      2 DSNAME  CHAR (44),
      2 DSORG  BIT (16),
      2 VOLSER  CHAR (6);

 DDNAME, DSNAME, and VOLSER are self explanatory.
   DSORG is one of:
  x'0000' dsorg cannot be determined
  x'0004' TR
  x'0008' VSAM
  X'0020' TQ
  X'0040' TX
  X'0080'  GS
  X'0200'  PO
  X'0300'  POU
  X'0400'  MQ
  X'0800'  CQ
  X'1000'  CX
  X'2000'  DA
  X'2100'  DAU
  X'4000'  PS
  X'4100'  PSU
  X'8000'  IS
  X'8100'  ISU


UNALLOC
This operation unallocates a data set by DD name or data-set name.  The
following is a list of JCL parameters and the equivalent DYNAM keyword.

 DD card parameter     DYNAM keyword
 DISP=(,CATLG)      CAtlg
 DISP=(,DELETE)     DElete
 DISP=(,KEEP)      KEEp
 DISP=(,UNCATLG)     UNCatlg
 DSN=...(name)      MEmber=name
 DSN=dsname      DSN=dsname

 Others        DYNAM keyword
 DDNAME on DD card     DD=name
 change SYSOUT class     NEWClass=name
 put SYSOUT output into the hold queue   NEWHold
 take SYSOUT output out of the hold queue   NEWNohold
 change SYSOUT routing     NEWRemote=name
 unallocate the resource even if permanently allocated  UNAlloc
 remove the in-use attribute even if permanently allocated REMOVe


CONCAT AND UNCONCAT
These two operations concatenate and unconcatenate data-sets.  The data sets
can only be identified by using DD names of data sets currently allocated so
therefore the only key-word needed in the third parameter to DYNAM is
DD=name.  To concatenate you provide a list of DD names, e.g.
DD=SYSLIB,FILE2,FILE3.  The contention is then identified by the  first DD
name in the list.  To unconcatenate just provide DD=name.


INFO
This operation requests information retrieval.  The third parameter to DYNAM
is a data area into which information will be placed.  The fourth and
subsequent parameters are operands that specify the allocations about which
information is to be retrieved.

 The information data area has the following format:
 DCL 1 INFORMATION UNALIGNED,
    2 DDNAME  CHAR (8),
    2 DSNAME  CHAR (44),
    2 MEMBER  CHAR (8),
    2 STATUS  BIT (8),
    2 DISP  BIT (8),
    2 COND_DISP  BIT (8),
    2 DSORG  BIT (16),
    2 LIMIT  FIXED BIN (15),
    2 ATTRIBUTE  BIT (8),
    2 LAST_ENTRY BIT (8),
    2 TYPE  BIT (8);

DDNAME DSNAME and MEMBER are self explanatory.  If no member is allocated
then the contents of MEMBER will be unchanged.

STATUS, DISP and COND_DISP are the same respectively as those specified in
the DISP operand in JCL.

 STATUS is one of:
      X'01'  OLD
      X'02'  MOD
      X'04'  NEW
      X'08'  SHR

 DISP is one of:
      X'01'  UNCATLG
      X'02'  CATLG
      X'04'  DELETE
      X'08'  KEEP
      X'10'  PASS

 COND_DISP is one of:
      X'01'  UNCATLG
      X'02'  CATLG
      X'04'  DELETE
      X'08'  KEEP

 DSORG is one of:
      x'0000' dsorg cannot be determined
      x'0004' TR
      x'0008' VSAM
      X'0020' TQ
      X'0040' TX
      X'0080' GS
      X'0200' PO
      X'0300' POU
      X'0400' MQ
      X'0800' CQ
      X'1000' CX
      X'2000' DA
      X'2100' DAU
      X'4000' PS
      X'4100' PSU
      X'8000' IS
      X'8100' ISU

LIMIT is the number of allocations that must be freed before a new
allocation can be made.
 ATTRIBUTE is one of:
      X'80'  permanently concatenated attribute
      X'40'  in-use attribute
      X'20'  permanently allocated attribute
      X'10'  convertible attribute
      X'08'  dynamically allocated attribute

LAST_ENTRY indicates if this is the last entry in the list of allocations
for  this job.  It has the values:
      X'80'  if last entry
      X'00'  otherwise

TYPE is one of:
      X'80'  DUMMY data set
      X'40'  terminal
      X'00'  otherwise

The following DYNAM keywords are supported:
 Purpose     DYNAM keyword
 select an allocation by DD name  DD=name
 select an allocation by DSN name  DSN=name
 select an allocation by a relative number RELNO=num


EXCEPTIONAL CONDITIONS
DYNAM returns a condition code in registers 15 and 0 as well as in the
second word of the work area if one is provided.  The use of register 15
allows a COBOL program to interrogate the return code through the COBOL
special register RETURN-CODE and allows the same for PLI through the use of
the pseudo function PLIRETV.  The use of register 0 allows FORTRAN and
PASCAL to call DYNAM as a function that returns an integer result.  If the
actual allocation fails, then messages are written to the job log and the
return code from SVC 99 is returned to the user.  If DYNAM itself fails,
then the return code is a DYNAM return code.

SVC 99 Return Codes
 00 successful allocation
 04 environment, resource, or system routine failure
 08 request denied by installation validation routine
 12 invalid SVC 99 parameter list

DYNAM Return Codes
 16 invalid verb (parameter 2)
 20 invalid keyword (parameter 3)
 24 work area overflow
 28 invalid value keyword


LANGUAGE CONSIDERATIONS
In PLI remember to put in:
 DCL DYNAM  ENTRY OPTIONS(ASM,RETCODE);
 FETCH DYNAM;  /* JUST FETCH DYNAM ONCE */

In FORTRAN and PASCAL remember to link edit DYNAM into the load module you
wish to produce.  This is done by adding SYS1.LINKUMW to the SYSLIB data
sets at link edit or loader time.


EXAMPLES

1) In PLI allocate a new data set:
 DCL WORK    FIXED BIN(31) INIT(0);
 DCL PLIRETV BUILTIN;
 DCL DYNAM   ENTRY OPTIONS (ASSEMBLER,RETCODE);
 FETCH DYNAM;
 CALL DYNAM(WORK, 'INIT ');
 CALL DYNAM(WORK, 'ALLOC ', 'DSN=USERID.DATA NEW CATLG;',
  'VOL=USER01;',
  'TRK PRIMARY=1 SECONDARY=1;',
  'LRECL=80 BLKSIZE=6080 FB;')
 IF PLIRETV = 0 THEN
     code to execute upon success of allocation
   ELSE
     code to execute upon failure of allocation

2) In COBOL allocate an existing data set to ddname SYSIN:
 01  DY-STUFF.
      02  DY-WORK PIC S9(9) COMP SYNC VALUE +0.
      02  DY-WORK PIC X(5) VALUE 'INIT '.
      02  DY-ALLOC PIC X(6) VALUE 'ALLOC '.
      02  DY-TEXT  PIC X(100).
      . . .
 PROCEDURE DIVISION.
      CALL 'DYNAM' USING DY-WORK DY-INIT.
      . . .
      MOVE 'DSN=A0011.AA.T999D DD=SYSIN SHR;' TO DY-TEXT.
      CALL 'DYNAM' USING DY-WORK DY-ALLOC DY-TEXT.
      IF RETURN-CODE = ZERO THEN
          whatever
        ELSE
          do something to recover gracefully.

3) In PLI allocate a concatenation:
 . . .
 CALL DYNAM(WORK, 'INIT ');
 . . .
 CALL DYNAM(WORK, 'ALLOC ', 'DSN=SYS1.USERLINK;', 'DD=SYSLIB SHR;');
 CALL DYNAM(WORK, 'ALLOC ', 'DSN=SYS1.LINKUMW;', 'DD=FILE2 SHR;');
 CALL DYNAM(WORK, 'CONCAT ', 'DD=SYSLIB,FILE2;');

4)  Other  sample programs are  available in a  PDS called
SYS4.DYNAM.SAMPLES.  The programs included are:   DYASM an assembler program
to test DYNAM
 DYLISTA an assembler program to list allocated data sets
 DYCOB  a COBOL program that allocates COBOL data sets
 DYPLI  a PLI program to test DYNAM
 DYFORT a FORTRAN program


"Albert W. Paul" <alpaul@mindspring.com> wrote in message
news:9sgrt0$9fp$1@slb6.atl.mindspring.net...
>
> The following email is a copy of the documentation for Dynam. It does
> exactly what you
> are looking for. You can have a program that uses all kinds of files that
do
> not have any defined assignments or references in the JCL.
>
…[32 more quoted lines elided]…
>
```

#### ↳ Re: Dynamic allocations in COBOL

- **From:** Daniel Jacot<daniel.jacot@winterthur.ch>
- **Date:** 2001-11-09T16:49:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oOTG7.19025$xS6.30740@www.newsranger.com>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com>`

```
On 9 Nov 2001 06:35:22 -0600, in article <3bebcd8a$1_4@news.newzpig.com>,
COBOLMAN stated...
>
>Someone asked this at work and I have never heard of it so maybe the
…[10 more quoted lines elided]…
>

Do you like the TSO syntax? If you do, you may use BPXWDYN. It's an IBM 'Tools &
Toys' program which is  free and should reside in your SYS1.LINKLIB. If is is
not there, you can download it from the net. The program works in all OS/390
releases.

The 'Tools & Toys' homepage is at:
http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1ty2.html
Download the program from:
ftp://ftp.software.ibm.com/s390/zos/tools/bpxwdyn/bpxwdyn.unload
The documenttion is  here:
ftp://ftp.software.ibm.com/s390/zos/tools/bpxwdyn/bpxwdyn.html

There are samples in C, REXX and PL/I, but it works with COBOL as well. Want a
small sample?

IDENTIFICATION DIVISION.                                       
PROGRAM-ID. DYNALLOC.                                        
DATA DIVISION.                                                 
WORKING-STORAGE SECTION.                                      
01 BPXWDYN       PIC X(8) VALUE 'BPXWDYN'.                   
01 ALLOC-STRING.                                             
05 ALLOC-LENGTH PIC S9(4) BINARY VALUE 100.                
05 ALLOC-TEXT   PIC X(100) VALUE                           
'ALLOC DD(INFILE) DSN(''LEM.JCL.CNTL(JICOBT20)'') SHR'.  
PROCEDURE DIVISION.                                            
CALL BPXWDYN USING ALLOC-STRING                            
IF RETURN-CODE NOT = ZERO                                  
THEN DISPLAY 'ALLOC FAILED, RETURN-CODE WAS ' RETURN-CODE 
ELSE DISPLAY 'ALLOC OK'                                   
END-IF                                                     
GOBACK.                                                    
END PROGRAM DYNALLOC.                                          

-------------------------------------------------
With kind regards
Daniel Jacot
-------------------------------------------------
visit us at: http://www.winterthur.com
```

#### ↳ Re: Dynamic allocations in COBOL

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2001-11-14T07:25:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bf270e5$1_1@news.newzpig.com>`
- **References:** `<3bebcd8a$1_4@news.newzpig.com>`

```
Dan, Thanks for the post. This subject gets more interesting all the
time. Our shop just went to OS390 R2.9. BTW, I just wanted to thank
everyone for the posts to this thread.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
