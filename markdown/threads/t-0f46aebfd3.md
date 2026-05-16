[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

_5 messages · 3 participants · 1999-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7s18st$o9n@dfw-ixnews10.ix.netcom.com>`

```
Because of all the recent discussions (in comp.lang.cobol), I have created
(and tested) a sample COBOL program that demonstrates the ONLY (and QUITE
OBSCURE) difference between how the '85 Standard works and how the draft of
the next Standard works.

NOTE WELL:
  As discussed in previous parts of this discussion, it appears that most
(possibly ALL) current '85 compilers work in the "new" way and not according
to the "letter-of-the-law" of the '85 Standard.  Furthermore, I think that
MOST (possibly all) of the readers have indicated that they "like" the new
way rather than what the '85 Standard (erroneously?) required.  If, however,
you (for some really PERVERSE reason) have a need or desire to get a "fully
conforming" '85 Standard compiler (that will NOT work the same way in the
future), then you can use this sample code to contact the support group of
your compiler vendor.  (Although this is an issue with how the '85 Standard
defines "EVALUATE," the only time that it really shows up is with the
Intrinsic Function "RANDOM".  Therefore, if you have an '85 compiler without
intrinsic functions - e.g. VS COBOL II for IBM - I don't know of any way to
"legally" test this.)

So much for "preface" - code follows:

  Identification Division.
  Program-ID. EvalRand.
*  See "Substantive Change 27 in CD 1.6 of the latest draft of the next
COBOL
*  Standard to see what this tests and how it should work in the '85
Standard
*  versus how it should work in the next COBOL Standard.
  Data Division.
  Working-Storage Section.
  01  Num-Fields.
      05  Outside-Eval Pic S9V9(17).
      05  Test-Num  Pic S9V9(17) Value 1.
      05 Save-Num  Pic S9V9(17).
      05 Save-2nd-Random Pic S9V9(17).
      05 Save-4th-Random Pic S9V9(17).
  01 NumEd-Fields.
      05 Disp-Num1  Pic +9.9(17).
      05 Disp-Num2  Pic +9.9(17).
  Procedure Division.
      Perform Verify-Random-Order
      If Test-Num = Zero
          Perform Test-Evaluate
      End-If
      Stop Run
       .
  Verify-Random-Order.
      Compute Save-Num = Function Random (1)
      Compute Save-2nd-Random = Function Random
      Perform 2 times
         Compute Save-4th-Random = Function Random
      End-Perform
      Compute Save-4th-Random = Function Random
      If   (Save-Num Not = Save-2nd-Random)
       and (Save-Num Not = Save-4th-Random)
       and (Save-2nd-Random Not = Save-4th-Random)
          Display "Random works as expected"
          Move Zero to Test-Num
      Else
          Display "Random does NOT work as expected"
          Display "  The rest of this program won't work either"
          Display "Using another seed value MIGHT work - but I doubt it"
      End-If
       .
  Test-Evaluate.
      Compute Outside-Eval = Function Random (1)
      Move Outside-Eval to Save-Num
      Evaluate Test-Num
        When Zero
          Display "Get's correct EVALUATE response, but ..."
        When Function Random
          Display "Never"
        When Function Random
          Display "Never"
        When Other
          Display "Never"
        End-Evaluate
      Compute Outside-Eval = Function Random
      If Outside-Eval = Save-2nd-Random
          Display "Does not conform to ANSI'85 Standard - but to CD 1.6"
      Else
          If Outside-Eval = Save-4th-Random
              Display "Conforms completely to ANSI'85 Standard"
          Else
              Display "Doesn't conform to ANYTHING"
          End-IF
      End-IF
       .
```

#### ↳ Re: Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7s5r27$sus@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7s18st$o9n@dfw-ixnews10.ix.netcom.com>`

```
Sorry people - I can't count.
To make the "attached" program correct, please change part of paragraph
 >   Verify-Random-Order

from
>       Perform 2 times
>          Compute Save-4th-Random = Function Random
>       End-Perform

to
>       Compute Save-4th-Random = Function Random

or REMOVE the compute that comes right after this.
```

##### ↳ ↳ Re: Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<37e82981.74408212@news1.ibm.net>`
- **References:** `<7s18st$o9n@dfw-ixnews10.ix.netcom.com> <7s5r27$sus@dfw-ixnews4.ix.netcom.com>`

```
On Mon, 20 Sep 1999 12:31:08 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:
Here are some real world test results from your program:


DEC COBOL V2.4-863 

Random works as expected
Get's correct EVALUATE response, but ...
Does not conform to ANSI'85 Standard - but to CD 1.6

--------------------

IBM COBOL for OS/390 & VM  2.1.1 

Options in effect:   
    NOADATA          
      ADV            
    NOANALYZE        
      APOST          
    NOAWO            
      BUFSIZE(4096)  
    NOCMPR2          
    NOCOMPILE(S)     
    NOCURRENCY       
      DATA(31)       
    NODATEPROC       
    NODBCS           
    NODECK           
    NODLL             
    NODUMP            
    NODYNAM           
    NOEXIT            
    NOEXPORTALL       
      FASTSRT         
      FLAG(W,W)       
    NOFLAGMIG         
    NOFLAGSTD         
    NOIDLGEN          
      INTDATE(ANSI)   
      LANGUAGE(EN)    
      LIB             
      LINECOUNT(60)   
    NOLIST            
    NOMAP             
      NAME(NOALIAS)   
    NONUMBER          
      NUMPROC(NOPFD)  
      OBJECT          
      OFFSET          
      OPTIMIZE(FULL)  
      OUTDD(SYSOUT)   
      PGMNAME(COMPAT) 
      RENT            
      RMODE(AUTO)     
      SEQUENCE        
      SIZE(MAX)       
      SOURCE          
      SPACE(1)        
    NOSSRANGE         
    NOTERM            
    NOTEST            
      TRUNC(STD)      
    NOTYPECHK            
    NOVBREF              
    NOWORD               
      XREF(FULL)         
      YEARWINDOW(1900)   
      ZWB                


Random works as expected                               
Get's correct EVALUATE response, but ...               
Does not conform to ANSI'85 Standard - but to CD 1.6
```

#### ↳ WARNING long post Re: Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<37E9C0D2.8F0A5B66@att.net>`
- **References:** `<7s18st$o9n@dfw-ixnews10.ix.netcom.com>`

```
"William M. Klein" suggested the logic in the tiny program shown below
as a way to see if the IBM VS COBOL II ver. 4 compiler if '85
conforming. I'm willing to bet both Bills were surprised! This source
generated one IGY... warning (right before the Binder mao.

Bill Lynch

1PP 5668-958 IBM VS COBOL II Release 4.0
09/15/92                           Date 09/22/99  Time 19:34:36  
Page     1
0Invocation parameters:
 NOEXIT,LANGUAGE(EN)
0PROCESS(CBL) statements:
  CBL NOADV,APOST,NOAWO,BUFSIZE(23552),NOCMPR2,COMPILE,DATA(24),NODBCS
  CBL NODECK,NODUMP,DYNAM,FASTSRT,NOFDUMP,FLAG(I,E),NOFLAGMIG,NOFLAGSAA
  CBL NOFLAGSTD,LIB,LINECOUNT(60),LIST,MAP,NONAME,NONUMBER
  CBL NUMPROC(NOPFD),OBJECT,NOOFFSET,OPTIMIZE,OUTDD(SYSOUT),RENT
  CBL RESIDENT,NOSEQUENCE,SIZE(MAX),SOURCE,SPACE(1),SSRANGE,TERM,NOTEST
  CBL TRUNC(OPT),NOVBREF,NOWORD,XREF(FULL),ZWB
0Options in effect:
     NOADV
       APOST
     NOAWO
       BUFSIZE(23552)
     NOCMPR2
       COMPILE
       DATA(24)
     NODBCS
     NODECK
     NODUMP
       DYNAM
     NOEXIT
       FASTSRT
     NOFDUMP
       FLAG(I,E)
     NOFLAGMIG
     NOFLAGSAA
     NOFLAGSTD
       LANGUAGE(EN)
       LIB
       LINECOUNT(60)
       LIST
       MAP
     NONAME
     NONUMBER
       NUMPROC(NOPFD)
       OBJECT
     NOOFFSET
       OPTIMIZE
       OUTDD(SYSOUT)
       RENT
       RESIDENT
     NOSEQUENCE
       SIZE(MAX)

       SOURCE
       SPACE(1)
       SSRANGE
       TERM
     NOTEST
       TRUNC(OPT)
     NOVBREF
     NOWORD
       XREF(FULL)
       ZWB
1PP 5668-958 IBM VS COBOL II Release 4.0 09/15/92                
WKLEIN    Date 09/22/99  Time 19:34:36   Page     2
   LineID  PL SL 
----+-*A-1-B--+----2----+----3----+----4----+----5----+----6----+----7-|--+----8 
Map and Cross Reference
0  000001                ID                Division.
   000002
   000003                Program-ID.       WKLEIN.
   000004
   000005               *Author.           William Lynch.
   000006
   000007               *Language.         Cobol II.
   000008
   000009               *Date-Written.     Sept, 1999.
   000011
   000012                DATE-COMPILED. 09/22/99.

   000014              
*---------------------------------------------------------------*
   000015               *  ---------------  Maintenance History 
---------------------  *
   000016              
*---------------------------------------------------------------*
   000017               * 990922  WL   Exactly how does EVALUATE
work?                  *
   000018              
*---------------------------------------------------------------*
   000019
   000020                Environment       Division.
   000021                Configuration     Section.
   000022                Source-Computer.  IBM-3090.
   000023                Object-Computer.  IBM-3090.
1Working Storage                                                 
WKLEIN    Date 09/22/99  Time 19:34:36   Page     3
   LineID  PL SL 
----+-*A-1-B--+----2----+----3----+----4----+----5----+----6----+----7-|--+----8 
Map and Cross Reference
   000025                Data              Division.
   000026                Working-Storage   Section.
   000027
   000028              
*---------------------------------------------------------------*
   000029               *    Bill's
W-S                                                 *
   000030              
*---------------------------------------------------------------*
   000031                01 
Num-Fields.                                                           
BLW=0000+000         0CL4
   000032                    05  NF1  Pic
9.                                                       
BLW=0000+000,0000000 1C
   000033                    05  Tabl occurs 3
times.                                              
BLW=0000+001,0000001 0CL1
   000034                        10 Elem  Pic
9.                                                   
BLW=0000+001,0000001 1C
1Procedure Division - Mainline Code                              
WKLEIN    Date 09/22/99  Time 19:34:36   Page     4
   LineID  PL SL 
----+-*A-1-B--+----2----+----3----+----4----+----5----+----6----+----7-|--+----8 
Map and Cross Reference
   000036                Procedure         Division.
   000037                0000-MAINLINE.
   000038              
*---------------------------------------------------------------*
   000039               *    Validate
EVALUATE                                          *
   000040              
*---------------------------------------------------------------*
   000041                    MOVE  3                     TO 
NF1                                    32
   000042                    Move  Zero                  to  Elem
(3)                               IMP 34

   000043                    Evaluate                   
NF1                                        32
   000044                    When                        3
   000045      1                 Display 'Does not follow the "letter of
the law"'
   000046                    When Elem                   (NF1 +
1)                                  34 32
   000047      1                 Display
   000048      1                     'You should get an SSRANGE error
before getting here'
   000049                    End-Evaluate
   000050
   000051                    GoBack
   000052                .
   000054                End Program 
WKLEIN.                                                       3
1Maps, Cross-References & Diagnostics                            
WKLEIN    Date 09/22/99  Time 19:34:36   Page    14
0                   *** TGT MEMORY MAP ***
                    TGTLOC

                    000000  72 BYTE SAVE AREA
                    ...
                    000048  TGT IDENTIFIER
                    000138  PERFORM SAVE CELLS
                    00013C  INTERNAL PROGRAM CONTROL BLOCKS
                    000150  TEMPORARY STORAGE-2
 TGT      WILL BE ALLOCATED FOR 00000160 BYTES
 WRK-STOR WILL BE ALLOCATED FOR 00000004 BYTES
 SPEC-REG WILL BE ALLOCATED FOR 00000031 BYTES
0CONSTANT GLOBAL TABLE FOR DYNAMIC STORAGE INITIALIZATION AT LOCATION
0001C8
0INITD CODE FOR DYNAMIC STORAGE INITIALIZATION BEGINS AT LOCATION 0002F8
FOR LENGTH 000088
1Maps, Cross-References & Diagnostics                            
WKLEIN    Date 09/22/99  Time 19:34:36   Page    16
0LineID  Message code  Message text

     46  IGYOP3091-W   Code from "WHEN (LINE 46.01)" to "DISPLAY (LINE
47.01)" can never be executed and was therefore discarded.

-Messages    Total    Informational    Warning    Error    Severe   
Terminating
0Printed:       1                          1
-* Statistics for COBOL program WKLEIN:
 *    Source records = 54
 *    Data Division statements = 4
 *    Procedure Division statements = 6
0End of compilation 1,  program WKLEIN,  highest severity 4.
0Return code 4
1
  DFSMS/MVS LINKAGE EDITOR   19:34:39  WED  SEP 22, 1999
  JOB ASPAWL1N   STEP WKLEIN     PROCEDURE LKED
  INVOCATION PARAMETERS - XREF,LIST,RENT,AMODE=31,RMODE=ANY
  ACTUAL SIZE=(317440,79872)
  OUTPUT DATA SET BASP.TEST.LOADLIB IS ON VOLUME RN2006
 IEW0000      SETSSI 99265193
 IEW0000      NAME   WKLEIN(R)
0
0                                                CROSS REFERENCE TABLE

0  CONTROL SECTION                       ENTRY
0    NAME    ORIGIN  LENGTH                NAME   LOCATION     NAME  
LOCATION     NAME   LOCATION     NAME   LOCATION
   WKLEIN        00     380
   IGZEBST *    380     450
                                         IGZEBS2      638
   CEEBETBL*    7D0      28
   CEESG005*    7F8      18
   CEESTART*    810      80
   CEEBINT *    890       8
   CEEBLLST*    898      60
                                         CEELLIST     8A8
   CEEBPUBT*    8F8      70
   CEEBTRM *    968      B0

0
0  LOCATION  REFERS TO SYMBOL  IN CONTROL SECTION             LOCATION 
REFERS TO SYMBOL  IN CONTROL SECTION

        6C            IGZEBST         IGZEBST                     
3AC            CEESTART        CEESTART
       3B0            CEEBETBL        CEEBETBL                    
79C            IGZETUN        $UNRESOLVED(W)
       7A0            IGZEOPT        $UNRESOLVED(W)               
7D4            CEEBXITA       $UNRESOLVED(W)
       7D8            CEEBINT         CEEBINT                     
7DC            CEEBLLST        CEEBLLST
       7E0            CEEUOPT        $UNRESOLVED(W)               
7E4            CEEBTRM         CEEBTRM
       7EC            CEEBPUBT        CEEBPUBT                    
7F0            IEWBLIT        $UNRESOLVED(W)
       83C            CEEMAIN        $UNRESOLVED(W)               
878            CEEFMAIN       $UNRESOLVED(W)
       884            CEEBETBL        CEEBETBL                    
888            CEEROOTA       $UNRESOLVED(W)
       8A8            CEESG000       $UNRESOLVED(W)               
8AC            CEESG001       $UNRESOLVED(W)
       8B0            CEESG002       $UNRESOLVED(W)               
8B4            CEESG003       $UNRESOLVED(W)
       8B8            CEESG004       $UNRESOLVED(W)               
8BC            CEESG005        CEESG005
       8C0            CEESG006       $UNRESOLVED(W)               
8C4            CEESG007       $UNRESOLVED(W)
       8C8            CEESG008       $UNRESOLVED(W)               
8CC            CEESG009       $UNRESOLVED(W)
       8D0            CEESG010       $UNRESOLVED(W)               
8D4            CEESG011       $UNRESOLVED(W)
       8D8            CEESG012       $UNRESOLVED(W)               
8DC            CEESG013       $UNRESOLVED(W)
       8E0            CEESG014       $UNRESOLVED(W)               
8E4            CEESG015       $UNRESOLVED(W)
       8E8            CEESG016       $UNRESOLVED(W)               
9D4            CEEBPUBT        CEEBPUBT

   LOCATION    84C REQUESTS CUMULATIVE PSEUDO REGISTER LENGTH
  ENTRY ADDRESS       00
0 TOTAL LENGTH       A18
  ** WKLEIN   REPLACED AND HAS AMODE 31
1
  ** LOAD MODULE HAS RMODE ANY
  ** AUTHORIZATION CODE IS         0.
 **MODULE HAS BEEN MARKED REENTERABLE, AND REUSABLE.
```

##### ↳ ↳ Re: WARNING long post Re: Evaluate - The "definitive" example of what is different between '85 and draft (CD 1.6) COBOLs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7scigi$bff@dfw-ixnews21.ix.netcom.com>`
- **References:** `<7s18st$o9n@dfw-ixnews10.ix.netcom.com> <37E9C0D2.8F0A5B66@att.net>`

```
From one Bill to Another -
   (I think that this compiler message gives you a good clue of the answer,
but ...)

If you still want to test it without getting that message, change OPT to
NOOPT and it will leave the code in (and probably still not execute it).

FYI,
  If you didn't see it, Thane tried it with IBM COBOL for this-and-that
using FUNCTION RANDOM (not available with VS COBOL II) and did "prove" that
it was working according to the "new" (next Standard) rules and not to the
existing rules.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
