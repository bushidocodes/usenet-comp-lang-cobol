[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# working storage addresses

_11 messages · 7 participants · 2000-09_

---

### working storage addresses

- **From:** cd <cdolny@my-deja.com>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
Hi folks,

COBOL is not my native language, so I'm hoping someone can point me in
the right direction.  I need to call an Assembly language program from
a COBOL program.  The Assembly language program takes one parameter, a
structure containing three pointers.  I have the following in my
WORKING-STORAGE SECTION.
    01  ASM-PGM-PARM.
        05  P1        USAGE IS POINTER.
        05  P2        USAGE IS POINTER.
        05  P3        USAGE IS POINTER.

These pointers need to point to other items in my WORKING-STORAGE
SECTION.  For example, I have the following in my WORKING-STORAGE.
    01  INTERFACE-STRUC-1.
        05  OPERATION        PIC X(8).
        etc. etc.   More Level-05 fields...

The following gives me an error message at compile time:
    SET ADDRESS OF INTERFACE-STRUC-1 TO P1 OF ASM-PGM-PARM.
The following doesn't work either:
    SET P1 OF ASM-PGM-PARM TO ADDRESS OF INTERFACE-STRUC-1.
Pointer P1 needs to be set to the address of different items depending
on parameter values that this COBOL program was called with.

I am using COBOL for MVS & VM V1R2.

What is the correct way to set a pointer to an address in working
storage?  Where is this documented in the manuals?

Thanks much.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: working storage addresses

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KcSz5.2579$bK5.13682@news2.mia>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
Here's the manual:
COVER Book Cover
--------------------------------------------------------------------------
COBOL for OS/390 & VM
COBOL Set for AIX
VisualAge COBOL

Language Reference

Document Number SC26-9046-01

And here's the text:
A data item defined with USAGE IS POINTER is a pointer data item.  A pointer
data item is a 4-byte
elementary item,

You can use pointer data items to accomplish limited base addressing.
Pointer data items can be compared for equality or moved to other pointer
items.

A pointer data item can only be used:

   In a SET statement (Format 5 only)
    In a relation condition
    In the USING phrase of a CALL statement, an ENTRY statement, or the
Procedure Division header.

The USAGE IS POINTER clause can be written at any level except level 88. If
a group item is described with the USAGE IS POINTER clause, the elementary
items within the group are pointer data items; the group itself is not a
pointer data item and cannot be used in the syntax where a pointer data item
is allowed.  The  USAGE clause of an elementary item cannot contradict the
USAGE clause of a group to which the item belongs.

Pointer data items can be part of a group that is referred to in a MOVE
statement or an input/output
statement.  However, if a pointer data item is part of a group, there is no
conversion of values when the
statement is executed.

A pointer data item can be the subject or object of a REDEFINES clause.

SYNCHRONIZED can be used with USAGE IS POINTER to obtain efficient use of
the pointer data item.

A VALUE clause for a pointer data item can contain only NULL or NULLS.

A pointer data item cannot be a conditional variable.

A pointer data item does not belong to any class or category.

The DATE FORMAT, JUSTIFIED, PICTURE, and BLANK WHEN ZERO clauses cannot be
used to describe group or elementary items defined with the USAGE IS POINTER
clause.

Pointer data items are ignored in CORRESPONDING operations.

A pointer data item can be written to a data set, but, upon subsequent
reading of the record containing the  pointer, the address contained can no
longer represent a valid pointer.

Note:  USAGE IS POINTER is implicitly specified for the ADDRESS OF special
register.  For more information  see the IBM COBOL Programming Guide for
your platform.


So to use it:

6.2.33.5 Format 5: SET for USAGE IS POINTER Data Items

When this form of the SET statement is executed, the current value of the
receiving field is replaced by the address value contained in the sending
field.

+--- Format 5--SET (USAGE IS POINTER Data Items) ------------------------+
�                                                                        �
�          <------------------------------+                              �
� >>--SET------identifier-4--------------------------------------------> �
�            +-ADDRESS OF--identifier-5-+                                �
�                                                                        �
� >--TO----identifier-6----------------------------------------------->< �
�        +-ADDRESS OF--identifier-7-�                                    �
�        +-NULL---------------------�                                    �
�        +-NULLS--------------------+                                    �
�                                                                        �
+------------------------------------------------------------------------+
identifier-4
    Receiving fields.

    Must be described as USAGE IS POINTER.

ADDRESS OF identifier-5
    Receiving fields.

    identifier-5 must be level-01 or level-77 items defined in the Linkage
Section.  The addresses of these
    items are set to the value of the operand specified in the TO phrase.

    Identifier-5 must not be reference-modified.

identifier-6
    Sending field.

    Must be described as USAGE IS POINTER.

    Cannot contain an address within the program's own Working-Storage,
File, or Local-Storage Section.

ADDRESS OF identifier-7
    Sending field.

     PICTURE 302 Under AIX, OS/2, and Windows, it must name an item in
either the Linkage Section or the
    Working-Storage Section of level 01, 77, or 02-49. PICTURE 303

     PICTURE 304 For OS/390 and VM, it must name an item in the Linkage
Section of any level except 66 or
    88.  ADDRESS OF identifier-7 contains the address of the identifier, and
not the content of the identifier.
    PICTURE 305

NULL
NULLS
    Sending field.

    Sets the receiving field to contain the value of an invalid address.


Table 49shows valid combinations of sending and receiving fields in a Format
5 SET statement.

+---------------------------------------------------------------------------
+
� Table 49. Sending and Receiving Fields for Format 5 SET Statement
�
+---------------------------------------------------------------------------
�
�               �                      Receiving Field
�
� Sending Field
+-----------------------------------------------------------�
�               �  USAGE IS POINTER �     ADDRESS OF    �     NULL/NULLS
�
+---------------+-------------------+-------------------+-------------------
�
�    USAGE IS   �       Valid       �       Valid       �         -
�
�    POINTER    �                   �                   �
�
+---------------+-------------------+-------------------+-------------------
�
�   ADDRESS OF  �       Valid       �       Valid       �         -
�
+---------------+-------------------+-------------------+-------------------
�
�   NULL/NULLS  �       Valid       �       Valid       �         -
�
+-------------------------------------------------------------

SO TO MAKE A LONG STORY SHORT, you've got it BACKWARDS.!!
You want the POINTER to hold the Address of  INTERFACE-STRUC-1.
Not the other way around.

Think of it just Like 'C' or BASIC, put the address of 'INTERFACE-STRUC-1'
into
PTR-1.




cd <cdolny@my-deja.com> wrote in message news:8qnqf4$ls8$1@nnrp1.deja.com...
> Hi folks,
>
…[32 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: working storage addresses

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CFD93D.7139DAB8@worldnet.att.net>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
cd wrote:
> 
> Hi folks,
…[29 more quoted lines elided]…
> Thanks much.

The correct syntax should be:
SET pointer-name TO ADDRESS OF linkage-section-record

IBM mainframe COBOL does not allow you to take the address of a
working-storage item (you already have addressability to it, so why do
you need it's address?).  At least this was true in VS COBOL II, and I'm
not sure that it's different even in COBOL for OS/390 & VM.

This topic has been discussed in comp.lang.cobol before, but not for
several months.

One creative solution I have seen is to write a very short nested COBOL
subprogram.  Pass it the working-storage item and a pointer variable. 
In the nested subprogram, SET the pointer variable to the ADDRESS OF the
linkage section item (your original working-storage item in your calling
program) and return.

The nested subprogram might look something like this:

IDENTIFICATION DIVISION.
PROGRAM-ID.  WS-ADDR.
ENVIRONMENT DIVISION.
DATA DIVSION.
LINKAGE SECTION.
01  WS-RECORD   PIC X(80).
01  WS-POINTER  USAGE IS POINTER.
PROCEDURE DIVISION USING WS-RECORD, WS-POINTER.
GET-ADDRESS-OF-WS-RECORD.
    SET WS-POINTER TO ADDRESS OF WS-RECORD
    GOBACK.
END PROGRAM WS-ADDR.

The nested subprogram would be embedded inside your main COBOL program
right before its END PROGRAM statement.

Then you should be able to get your pointers in the main program by
calling the subprogram:

CALL "WS-ADDR" USING INTERFACE-STRUC-1, P1 OF ASM-PGM-PARM
CALL "WS-ADDR" USING INTERFACE-STRUC-2, P2 OF ASM-PGM-PARM
CALL "WS-ADDR" USING INTERFACE-STRUC-3, P3 OF ASM-PGM-PARM     

This gets around the restriction in IBM COBOL that prevents you from
directly saving the address of a working-storage item.  I haven't
verified the syntax of the nested subprogram, so you may have to do some
experimentation on your own.  

I hope that helps!
```

##### ↳ ↳ Re: working storage addresses

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sdSz5.2580$bK5.13527@news2.mia>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com> <39CFD93D.7139DAB8@worldnet.att.net>`

```
No, COBOL for OS390 AKA MVSVM does allow it.

Arnold Trembley <arnold.trembley@worldnet.att.net> wrote in message
news:39CFD93D.7139DAB8@worldnet.att.net...
> cd wrote:
> >
…[82 more quoted lines elided]…
> http://arnold.trembley.home.att.net/
```

#### ↳ Re: working storage addresses

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qomji$l45$1@slb6.atl.mindspring.net>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
You can do it one at a time and then you can expand this example. Each time
the first parameter must change. There is no "SET ADDRESS OF" for WS fields
in IBM COBOL2 and greater. After returning from the caller, WS-POINTER will
contain the address of the first parameter, in this example, WS-DATA.

In ASSEMBLER, it would be:

GETADDR    CSECT
                        USING    *,15
                        LM           7,8,0(1)
                        ST            7,0(,R8)
                        BR            14
                        END

In COBOL, it would be:

PROGRAM-ID. GETADDR.
WORKING-STORAGE SECTION.
LINKAGE SECTION.
01    LS-PARM-AREA        PIC X(01).
01    LS-PARM-POINTER POINTER.
PROCEDURE DIVISION USING LS-PARM-AREA, LS-PARM-POINTER.
        SET LS-PARM-POINTER TO ADDRESS OF LS-PARM-AREA.
        GOBACK.

In both cases, the syntax would be:

CALL "GETADDR" USING WS-AREA, WS-POINTER.

The WS definitions in the calling program looks like this:

        03    WS-DATA        PIC  X(1024).
        03    WS-POINTER  POINTER.

You can get into redefining the pointer as a fullword, then you can
arithmetically increment/decrement the pointer, but I'll leave that as an
exercise.

HTH....

Cheers,

Bill,
Atlanta

"cd" <cdolny@my-deja.com> wrote in message
news:8qnqf4$ls8$1@nnrp1.deja.com...
> Hi folks,
>
…[32 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: working storage addresses

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-09-26T00:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CFE65A.8832B10@worldnet.att.net>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com> <8qomji$l45$1@slb6.atl.mindspring.net>`

```
WOB wrote:
> 
> You can do it one at a time and then you can expand this example. Each time
…[39 more quoted lines elided]…
> Cheers,

My apologies for misspelling DIVSION in my earlier example!

In my normal working environment, I use the following COBOL compiler:
PP 5688-197 IBM COBOL for MVS & VM   1.2.2    

I verified by experimentation that this compiler will not allow you to
SET a pointer TO a working-storage address.  So I coded up an example
program named "GETADDR" with a nested subprogram named "WS-ADDR":

 IDENTIFICATION DIVISION.                                      
 PROGRAM-ID.     GETADDR.                                      
*AUTHOR.         ARNOLD J. TREMBLEY.                           
*DATE-WRITTEN.   MON-25-SEP-2000.                              
 ENVIRONMENT DIVISION.                                         
 DATA DIVISION.                                                
 WORKING-STORAGE SECTION.                                      
 01  200-RECORD  PIC X(80)  VALUE                              
     'THIS IS A TEST DATA RECORD'.                             
 01  800-POINTERS.                                             
     05  800-POINTER     USAGE IS POINTER VALUE NULL.          
     05  800-POINTER-N   REDEFINES 800-POINTER PIC S9(9) COMP. 
 PROCEDURE DIVISION.                                           
 0000-MAINLINE.                                                
     DISPLAY '800-POINTER-N BEFORE = ' 800-POINTER-N           
     CALL 'WS-ADDR' USING 200-RECORD, 800-POINTER              
     DISPLAY '800-POINTER-N AFTER  = ' 800-POINTER-N           
     GOBACK.                                                   
 IDENTIFICATION DIVISION.                                      
 PROGRAM-ID.     WS-ADDR.                         
 ENVIRONMENT DIVISION.                            
 DATA DIVISION.                                   
 LINKAGE SECTION.                                 
 01  WS-RECORD   PIC X(80).                       
 01  WS-POINTER  USAGE IS POINTER.                
 PROCEDURE DIVISION USING WS-RECORD, WS-POINTER.  
 GET-ADDRESS-OF-WS-RECORD.                        
     SET WS-POINTER TO ADDRESS OF WS-RECORD       
     GOBACK.                                      
 END PROGRAM WS-ADDR.                             
 END PROGRAM GETADDR.

It compiled cleanly, and when executed gave the following results:

800-POINTER-N BEFORE = 000000000     
800-POINTER-N AFTER  = 210768784     

The length of WS-RECORD in the WS-ADDR subprogram does not matter if the
only thing you are going to do is SET the pointer and return.

I hope this example is more helpful.

With kindest regards,
```

#### ↳ Re: working storage addresses

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qrkul$geopo$1@ID-39920.news.cis.dfn.de>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```

cd <cdolny@my-deja.com> wrote in message news:8qnqf4$ls8$1@nnrp1.deja.com...
> Hi folks,
>
…[9 more quoted lines elided]…
>
How exactly is your assembler program accessing the pointers?  It sounds to
me like it is expecting a standard call area.
I.E.

        L   R2,0(R1)       ADDRESS PARM AREA 1
        L   R3,4(R1)       ADDRESS PARM AREA 2
        L   R4,8(R1)       ADDRESS PARM AREA 3

(or, of course, any version of this same concept).

If this is the case, then it is a simple call from the COBOL program...

CALL asm-program USING INTERFACE-STRUC-1, INTERFACE-STRUC-2,
INTERFACE-STRUC-3.

As for setting a pointer to an address, you can do the following:

SET WS-PTR1 TO ADDRESS OF LINKAGE-AREA-ITEM where ws-ptr1 is in your working
storage (or linkage area, for that matter, as long as it is addressed and
defined as usage pointer) and linkage-area-item is in your linkage area.

Hope this helps....

Dave
```

#### ↳ Re: working storage addresses

- **From:** "Armin Zerfas" <A.Zerfas@telekom.de>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qpjjp$s8r3@mailgate1b.telekom.de>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
You are looking in the wrong direction: you need a simple call to your
assembler-program like
call CALL 'ASM-PROG' USING INTERFACE-STRUC-1 INTERFACE-STRUC-2 ...
and COBOL will be happy to create the Parameterlist and pass its address.

regards
A. Zerfas
cd schrieb in Nachricht <8qnqf4$ls8$1@nnrp1.deja.com>...
>Hi folks,
>
…[32 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: working storage addresses

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lf41tssvnjpi0fjp5du67dt8us18a6mks5@4ax.com>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
On Mon, 25 Sep 2000 15:20:28 GMT cd <cdolny@my-deja.com> wrote:

:>COBOL is not my native language, so I'm hoping someone can point me in
:>the right direction.  I need to call an Assembly language program from
:>a COBOL program.  The Assembly language program takes one parameter, a
:>structure containing three pointers.  I have the following in my
:>WORKING-STORAGE SECTION.
:>    01  ASM-PGM-PARM.
:>        05  P1        USAGE IS POINTER.
:>        05  P2        USAGE IS POINTER.
:>        05  P3        USAGE IS POINTER.

:>These pointers need to point to other items in my WORKING-STORAGE
:>SECTION.  For example, I have the following in my WORKING-STORAGE.
:>    01  INTERFACE-STRUC-1.
:>        05  OPERATION        PIC X(8).
:>        etc. etc.   More Level-05 fields...

:>The following gives me an error message at compile time:
:>    SET ADDRESS OF INTERFACE-STRUC-1 TO P1 OF ASM-PGM-PARM.
:>The following doesn't work either:
:>    SET P1 OF ASM-PGM-PARM TO ADDRESS OF INTERFACE-STRUC-1.
:>Pointer P1 needs to be set to the address of different items depending
:>on parameter values that this COBOL program was called with.

:>I am using COBOL for MVS & VM V1R2.

:>What is the correct way to set a pointer to an address in working
:>storage?  Where is this documented in the manuals?

Somehow I doubt your ASM subprogram wants a structure like that. It is more
likely that it wants a standard parmlist where R1 points to a list of
addresses, i.e.,
      LM   R3,R5,0(R1)  
at entry would load the addresses of the three parameters.

If my assumption is correct, you would use
       CALL 'subroutine' USING STRUCT-1, STRUCT-2, STRUCT-3

Of course, if the ASM subprogram does use a second level of addressing, you
will need to write another subprogram to get the addresses.
```

#### ↳ Re: working storage addresses

- **From:** cd <cdolny@my-deja.com>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qq84u$gqt$1@nnrp1.deja.com>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
Many thanks to everyone who responded.  I have a better understanding
of pointers in COBOL now.  We still cannot find our paper manuals for
COBOL for MVS & VM here, but at least we have Book Manager...

Thanks again.

     cd

In article <8qnqf4$ls8$1@nnrp1.deja.com>,
  cd <cdolny@my-deja.com> wrote:
> Hi folks,
>
…[32 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: working storage addresses

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r38ml$ona$1@nnrp1.deja.com>`
- **References:** `<8qnqf4$ls8$1@nnrp1.deja.com>`

```
In article <8qnqf4$ls8$1@nnrp1.deja.com>,
  cd <cdolny@my-deja.com> wrote:
> Hi folks,
>
…[32 more quoted lines elided]…
>

I wanted to mention that if you pass a single WS parameter to a given
subprogram and this subprogram attempts to get fancy and return the
ADDRESS of this parameter in R15 (COBOL RETURN-CODE Special Register),
the Caller will be in for a surprise. Regardless whether the subprogram
is COBOL or ASSEMBLER, COBOL treats this Special Register internally as
a HALFWORD, S9(04) BINARY. Therefore, you WILL lose the high-order (2-
bytes) of R15 and have a bogus address. The use of a Special "Register"
does NOT necessarily translate to a FULLWORD value, so be careful.

Just wanted you to be aware of this if it is ever suggested.

Cheers,

Bill,
WOB Consulting, Inc.
Atlanta


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
