[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS: GETMAIN / FREEMAIN

_7 messages · 4 participants · 2000-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MVS: GETMAIN / FREEMAIN

- **From:** shine98@my-deja.com
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8do0tp$ick$1@nnrp1.deja.com>`

```
How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch program.
All the references I see do a 'EXEC CICS'. Code samples appreciated.

~shine


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: GETMAIN / FREEMAIN

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ff8cd3_4@news1.prserv.net>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com>`

```
You can do this via an assembler program - I like the STORAGE macro,
which allows you to OBTAIN and RELEASE memory.  It also allows you to
specify above / below the line storage, and boundary alignments.

***********************************************************************
* OBTAIN STORAGE FOR THE REQUESTED LENGTH:                            *
***********************************************************************
OBTSTG   MVC   FULLWORD,PARMSLEN       LOAD LENGTH TO FULLWORD
         L     R6,FULLWORD             LOAD REQUESTED STORAGE LENGTH
         MVC   PARMADDR,=F'0'          INIT PARM ADDRESS
         STORAGE OBTAIN,LENGTH=(R6),ADDR=STGADDR,COND=YES,             X
               LOC=BELOW,BNDRY=DBLWD
         LTR   R15,R15                 GOOD STORAGE OBTAIN?
         BZ    OBTGOOD                 YES - BRANCH AROUND ERR PROCESS

and to release storage:

***********************************************************************
* RELEASE STORAGE STARTING AT THE GIVEN ADDRESS FOR REQUESTED LENGTH: *
***********************************************************************
RELSTG   MVC   STGADDR,PARMADDR        LOAD REQUESTED STORAGE ADDRESS
         MVC   FULLWORD,PARMSLEN       LOAD LENGTH TO FULLWORD
         L     R6,FULLWORD             LOAD REQUESTED STORAGE LENGTH
         STORAGE RELEASE,LENGTH=(R6),ADDR=STGADDR,COND=YES
         LTR   R15,R15                 GOOD STORAGE RELEASE?
         BZ    RELGOOD                 YES - BRANCH AROUND ERR PROCESS


Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net


<shine98@my-deja.com> wrote in message
news:8do0tp$ick$1@nnrp1.deja.com...
> How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch program.
> All the references I see do a 'EXEC CICS'. Code samples appreciated.
…[5 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: GETMAIN / FREEMAIN

- **From:** 4485@my-deja.com
- **Date:** 2000-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dqses$i47$1@nnrp1.deja.com>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com> <38ff8cd3_4@news1.prserv.net>`

```
In article <38ff8cd3_4@news1.prserv.net>,
  "Lucas, Todd" <todd.lucas@ibm.net> wrote:
> You can do this via an assembler program - I like the STORAGE macro,
> which allows you to OBTAIN and RELEASE memory.  It also allows you to
> specify above / below the line storage, and boundary alignments.
>
>
***********************************************************************
> * OBTAIN STORAGE FOR THE REQUESTED LENGTH:
*
>
***********************************************************************
> OBTSTG   MVC   FULLWORD,PARMSLEN       LOAD LENGTH TO FULLWORD
>          L     R6,FULLWORD             LOAD REQUESTED STORAGE LENGTH
>          MVC   PARMADDR,=F'0'          INIT PARM ADDRESS
>          STORAGE OBTAIN,LENGTH=
(R6),ADDR=STGADDR,COND=YES,             X
>                LOC=BELOW,BNDRY=DBLWD
>          LTR   R15,R15                 GOOD STORAGE OBTAIN?
…[4 more quoted lines elided]…
>
***********************************************************************
> * RELEASE STORAGE STARTING AT THE GIVEN ADDRESS FOR REQUESTED LENGTH:
*
>
***********************************************************************
> RELSTG   MVC   STGADDR,PARMADDR        LOAD REQUESTED STORAGE ADDRESS
>          MVC   FULLWORD,PARMSLEN       LOAD LENGTH TO FULLWORD
…[10 more quoted lines elided]…
> > How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch
program.
> > All the references I see do a 'EXEC CICS'. Code samples appreciated.
> >
…[4 more quoted lines elided]…
> > Before you buy.

The February 2000 edition of Enterprise System Journal had an article
about Language Environment. The article contained information, and code
examples, about getting and freeing storage in a COBOL program.

www.esj.com/fullarticle.asp?ID=3140051654PM








Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: MVS: GETMAIN / FREEMAIN

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8do5vs$nvu$1@nnrp1.deja.com>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com>`

```
In article <8do0tp$ick$1@nnrp1.deja.com>,
  shine98@my-deja.com wrote:
> How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch program.
> All the references I see do a 'EXEC CICS'. Code samples appreciated.
…[5 more quoted lines elided]…
>

        YREGS                           MVS REGISTER-MACRO
        STM	R14,R1,REGSAVE		SAVE R14 THRU R1
        L 	R0,=A(L'STGAREA)	LOAD STORAGE LENGTH
        GETMAIN RU,LV=(0),LOC=ANY	GET STORAGE, ANY LOCATION
        LR	R9,R1		        STORAGE ADDRESSABILITY
        USING	STGDSECT,R9		INFORM ASSEMBLER
        ST      R9,R9SAVE		SAVE STORAGE ADDRESS
        LR      R0,R9			LOAD 'RECVING' ADDRESS
        L       R1,=A(L'STGAREA)	LOAD 'RECVING' LENGTH
        SR      R14,R14			LOAD 'SENDING' ADDRESS
        LA      R15,X'40'               LOAD 'SENDING' LENGTH
        SLL     R15,24                  SHIFT TO HIGH-ORDER
        MVCL    R0,R14			INITIALIZE STORAGE TO SPACES
        LM      R14,R1,REGSAVE		RESTORE R14 THRU R1
        XC      REGSAVE(72),REGSAVE	CLEAR REGISTER SAVEAREA
********
******** SOME PROCESSING IS DONE HERE
********
        STM	R0,R1,REGSAVE 		SAVE R0 AND R1
        L 	R0,=A(L'STGAREA)	LOAD STORAGE LENGTH
        L	R1,R9SAVE		LOAD STORAGE ADDRESS
        FREEMAIN RU,LV=(0),A=(1)	FREE THE STORAGE
        LM	R0,R1,REGSAVE		RESTORE R0 AND R1
        XC	REGSAVE(72),REGSAVE	CLEAR REGISTER SAVEAREA
        SR	R9,R9			CLEAR FORMER DSECT BASE

REGSAVE	DS	18F
R9SAVE  DS      F
STGDSECT DSECT
STGAREA	DS	CL32768

HTH....

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: MVS: GETMAIN / FREEMAIN

- **From:** shine98@my-deja.com
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dpkdq$7af$1@nnrp1.deja.com>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com> <8do5vs$nvu$1@nnrp1.deja.com>`

```
In article <8do5vs$nvu$1@nnrp1.deja.com>,
  WOB Consulting <wobconsult@my-deja.com> wrote:
> In article <8do0tp$ick$1@nnrp1.deja.com>,
>   shine98@my-deja.com wrote:
> > How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch
program.
> > All the references I see do a 'EXEC CICS'. Code samples appreciated.
> >
…[18 more quoted lines elided]…
>         MVCL    R0,R14			INITIALIZE STORAGE TO
SPACES
>         LM      R14,R1,REGSAVE		RESTORE R14 THRU R1
>         XC      REGSAVE(72),REGSAVE	CLEAR REGISTER SAVEAREA
…[22 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: MVS: GETMAIN / FREEMAIN

- **From:** shine98@my-deja.com
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dpkvq$7t8$1@nnrp1.deja.com>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com> <8do5vs$nvu$1@nnrp1.deja.com>`

```
I really appreciate your response but I was thinking something more in
the line of: call 'GETMAIN' using this that the-other. Is this possible?
Could I assemble your code into a subroutine that I could call? I'll
have to admit that this is a little out of my usual relm, I just an
inquisitive COBOL coolie sweating down in the data paddies.

Thanks

~shine

In article <8do5vs$nvu$1@nnrp1.deja.com>,
  WOB Consulting <wobconsult@my-deja.com> wrote:
> In article <8do0tp$ick$1@nnrp1.deja.com>,
>   shine98@my-deja.com wrote:
> > How would one do a 'GETMAIN' and 'FREEMAIN' from a MVS batch
program.
> > All the references I see do a 'EXEC CICS'. Code samples appreciated.
> >
…[18 more quoted lines elided]…
>         MVCL    R0,R14			INITIALIZE STORAGE TO
SPACES
>         LM      R14,R1,REGSAVE		RESTORE R14 THRU R1
>         XC      REGSAVE(72),REGSAVE	CLEAR REGISTER SAVEAREA
…[22 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: MVS: GETMAIN / FREEMAIN

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dqeim$3h9$1@nnrp1.deja.com>`
- **References:** `<8do0tp$ick$1@nnrp1.deja.com> <8do5vs$nvu$1@nnrp1.deja.com> <8dpkvq$7t8$1@nnrp1.deja.com>`

```
In article <8dpkvq$7t8$1@nnrp1.deja.com>,
  shine98@my-deja.com wrote:
> I really appreciate your response but I was thinking something more in
> the line of: call 'GETMAIN' using this that the-other. Is this
possible?
> Could I assemble your code into a subroutine that I could call? I'll
> have to admit that this is a little out of my usual relm, I just an
…[5 more quoted lines elided]…
>

Two things:

01) There is a slight Boo-Boo in my FREEMAIN MACRO coding. Instead of
loading R1 with the R9SAVE fullword, just code A=R9SAVE (no parenthesis
around R9SAVE as it is NOT a register). If you use R1 in my example,
you'll get a S0C4, because the MACRO expansion clears R1 BEFORE issuing
the SVC 120. This is what happens when you go by your memory (what's
that ?) :-)

02) Are you running "LE" (Language Environment)? If so, check out the
Callable Service Routine "CEEGTST" (Get Heap Storage). Refer to Book
Manager at:

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/library, Book CEEA3020
(SC28-1940-08)

========================================================================

If you just need storage for a STEP, an implicit FREEMAIN is done when
you're STEP completes. It would be mucho overhead to CALL the sub-
program numerous times to Get/Free Storage. I would imagine, you'd call
the sub-program once, get the storage address and return it to your
COBOL program ? Unless I don't understand, COBOL2 (or greater) Working-
Storage should be able to handle large chunks of data, unless this
request has some unique requirements. I trust you're NOT using this
storage for CICS ?

Rather than clutter up C.L.C. with ASSEMBLER stuff, E-Mail me off-line,
explaining exactly what you want to do with this storage. I'll try to
give you an answer sometime next week after Easter.

Regards,

WOB,
Atlanta


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
