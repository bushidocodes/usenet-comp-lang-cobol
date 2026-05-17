[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help I need to be able to identify sys user name or JobID in COBOL or PLI

_5 messages · 3 participants · 1998-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help I need to be able to identify sys user name or JobID in COBOL or PLI

- **From:** "bob..." <ua-author-91503@usenetarchives.gap>
- **Date:** 1998-05-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<356073f9.7095751@news.erols.com>`

```

Help I need to be able to identify sys user name or JobID in
COBOL or PLI.
```

#### ↳ Re: Help I need to be able to identify sys user name or JobID in COBOL or PLI

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68e75a8ee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<356073f9.7095751@news.erols.com>`
- **References:** `<356073f9.7095751@news.erols.com>`

```

Can you tell us what operating system and compiler(s) you are using? There
is no portable/standard way to do this, but many specific products to
provide such a capability.
```

##### ↳ ↳ Re: Help I need to be able to identify sys user name or JobID in COBOL or PLI

- **From:** "bob..." <ua-author-91503@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68e75a8ee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d68e75a8ee-p2@usenetarchives.gap>`
- **References:** `<356073f9.7095751@news.erols.com> <gap-d68e75a8ee-p2@usenetarchives.gap>`

```

On Tue, 19 May 1998 08:30:41 -0700, "William M. Klein"
wrote:

› Can you tell us what operating system and compiler(s) you are using?  There
› is no portable/standard way to do this, but many specific products to
› provide such a capability.
 
› bob··.@er··s.com wrote in message <356··.@new··s.com>...
› Help I need to be able to identify sys user name or JobID in
› COBOL or PLI.
Sorry after rejoining the mainframe world after avoiding them for 15
years, I was acting as if there was nothing but mainframes (at least with
COBOL). Shame on me.

IBM 3090 OS/MVS

need to filter out some features except for those few with "God" status.

Either the 6 character account/user ID or the 8 character JOBID (which
contains the user ID) is good.

bob hunt
```

###### ↳ ↳ ↳ Re: Help I need to be able to identify sys user name or JobID in COBOL or PLI

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68e75a8ee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d68e75a8ee-p3@usenetarchives.gap>`
- **References:** `<356073f9.7095751@news.erols.com> <gap-d68e75a8ee-p2@usenetarchives.gap> <gap-d68e75a8ee-p3@usenetarchives.gap>`

```

bob··.@er··s.com wrote:
› 
› On Tue, 19 May 1998 08:30:41 -0700, "William M. Klein"
…[20 more quoted lines elided]…
› bob hunt

I have a CALLable Asm routine, which I wrote just 6 months ago, so my
new date routine would have access to this info. I could email it to
you, if you're interested.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Help I need to be able to identify sys user name or JobID in COBOL or PLI

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68e75a8ee-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d68e75a8ee-p3@usenetarchives.gap>`
- **References:** `<356073f9.7095751@news.erols.com> <gap-d68e75a8ee-p2@usenetarchives.gap> <gap-d68e75a8ee-p3@usenetarchives.gap>`

```

Bob,

Here's the source I promised. The 9 comments immediately before the END
statement are the SDSF output, i.e., Displays, from the COBOL program
calling it (I think I have disguised anything which *might* relate to my
employer):

------------------- begin sample code ------------------------

SAMP503 Title 'Determine CALLing Program'
*--------------------------------------------------------------------*
* Program Narrative: *
* SAMP503 is a simple batch Assembler program which locates *
* the name of the CALLing program and returns it. *
*--------------------------------------------------------------------*
* SAMP503 must be called statically to return the right *
* program name (it doesn't sift thru RBs)????? *
*--------------------------------------------------------------------*
space 1
*--------------------------------------------------------------------*
* ProgramAttributes: *
* AMODE(ANY) *
* RMODE(24) *
* HLASM *
* Not RENT *
* Uses macros from 'SYS1.AMODGEN' *
*--------------------------------------------------------------------*
space 1
SAMP503 CSECT *
space 1
SAMP503 CSECT *
SAMP503 AMODE ANY *
SAMP503 RMODE 24 *
SAVE (14,12) *
LA BASER,0(,R15) *
USING SAMP503,BASER *
B GO *
PROGID DC C'SAMP503 &SYSDATC &SYSTIME '
GO DS 0H *
L R2,0(,R1) * A(WS-PGM)
Using PGMDSECT,R2 * addressability
L R4,CVTPTR *
Using CVT,R4 *
L R5,CVTTCBP *
L R6,4(,R5) *
Drop R4 * lose this
Using TCB,R6 *
L R7,TCBRBP * A(RB)
Drop R6 * lose this
Using RBBASIC,R7 *
L R8,RBCDE * A(CDE)
Drop R7 * lose this
Using CDENTRY,R8 *
MVC CALLER,CDNAME *
Drop R8 * lose this
space 1
*--------------------------------------------------------------------*
* collect MVS JOB info - 971216 *
*--------------------------------------------------------------------*
L R15,548 * A(ASCB)
Using ASCB,R15 *
L R14,ASCBASXB * A(ASXB)
MVC USERID,192(R14) * userid to msg
L R1,ASCBASSB * A(ASSB)
Using ASSB,R1 *
L R1,ASSBJSAB * A(JSAB)
Using JSAB,R1 *
MVC JOB_NO,JSABJBID * job no.
MVC JOB_NAME,JSABJBNM * job name
Drop R1,R15 * lose these
space 1
Return (14,12) * Goback
title 'Constants && Workareas'
LTORG *
space 1
RSA DC 18F'0' * our RSA
space 1
PGMDSECT DSECT *
CALLER DS CL8 *
USERID DS CL8 *
JOB_NO DS CL8 *
JOB_NAME DS CL8 *
title 'Communication Vector Table'
CVT LIST=YES,DSECT=YES
title 'Task Control Block'
IKJTCB LIST=YES
title 'Request Block'
IHARB LIST=YES,DSECT=YES
title 'Contents Directory Entry'
IHACDE *
title 'Address Space Control Block'
IEFZB4D2
Title 'IAZJSAB Macro for Job Scheduler Info'
IAZJSAB LIST=YES
Title 'IHAASCB Macro to Map ASCB'
IHAASCB LIST=YES
Title 'IAAASSB Macro to Map ASSB'
IHAASSB LIST=YES
title 'Registers && Equates'
R0 EQU 0 *
R1 EQU 1 *
R2 EQU 2 *
R3 EQU 3 *
R4 EQU 4 *
R5 EQU 5 *
R6 EQU 6 *
R7 EQU 7 *
R8 EQU 8 *
R9 EQU 9 *
R10 EQU 10 *
R11 EQU 11 *
R12 EQU 12 *
R13 EQU 13 *
R14 EQU 14 *
R15 EQU 15 *
space 1
BASER EQU R3 *
HSA EQU 4 *
LSA EQU 4 *
space 2
* SDSF OUTPUT DISPLAY TESTWL1B JOB07356 LINE 0 COLUMNS 02- 81
* COMMAND INPUT ===>+ _SCROLL ==>+PAGE_
* ********************* TOP OF DATA *****************************
* MVS Job/Step Info:
* Program TABTCB
* Userid TESTWL1
* Job No. JOB07356
* Job Name TESTWL1B
* ******************* BOTTOM OF DATA ****************************
space 2
END SAMP503 *

-------------------- end of sample code --------------------

Re: calling it statically - it works fine when the program is invoked
by
the "// EXEC" statement. I haven't tested it's being called by a called
program; thus, my note about calling it statically (I assume it won't
work).

HTH,
Bill Lynch

bob··.@er··s.com wrote:
› 
› On Tue, 19 May 1998 08:30:41 -0700, "William M. Klein"
…[20 more quoted lines elided]…
› bob hunt
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
