[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM mainframe COBOL - how to close an output file and reopen it with a different DSN

_3 messages · 2 participants · 1998-08 → 1998-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: IBM mainframe COBOL - how to close an output file and reopen it with a different DSN

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<35EAB5A5.8C8D3914@zip.com.au>`
- **References:** `<6s0p5r$4v0$1@holly.prod.itd.earthlink.net> <6s7dfq$31b$1@ash.prod.itd.earthlink.net> <6s9f25$cin@dfw-ixnews10.ix.netcom.com> <35ea94fc.773118@news.pnc.com.au>`

```
This is from the proposed standard and not in the currect MVS release.

Here is a generic description on how to do it without the standard
changes.

In MVS a DDName is a generic name that is associated with a real
filename (dataset name).  It is indeed static and for writing can only
really be one dataset.  In order to get the Dataset name to apparently
change to the cobol program there is an assembler trick that calls
dynalloc (look up your assembler modules book).

Your cobol program would look something like this (assuming you have two
assembler routines allocate and dealloc)

perform until all files processed

   call allocate using ddname, dataset
   open output ddname
      do your thing...
   close ddname
   call dealloc using ddname
end-perform

You do not actually need the dealloc if you use free=close (but it is
all done in assembler).

Has anyone got a copy of alloc and dealloc that they are prepared to
share. Mine are truly awful versions that only just work!

Hope this helps
Ken

Engelbrecht Computer Services Pty Ltd wrote:
> 
> Do you have an example of this dynamic name change.  How does this
…[5 more quoted lines elided]…
>
```

#### ↳ Re: IBM mainframe COBOL - how to close an output file and reopen it with a different DSN

- **From:** zberger@ldl.net
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<6sf16g$848$1@nnrp1.dejanews.com>`
- **References:** `<6s0p5r$4v0$1@holly.prod.itd.earthlink.net> <6s7dfq$31b$1@ash.prod.itd.earthlink.net> <6s9f25$cin@dfw-ixnews10.ix.netcom.com> <35ea94fc.773118@news.pnc.com.au> <35EAB5A5.8C8D3914@zip.com.au>`

```
Ok, this is from memory so don't beat me up when the names don't line up
perfectly:

01 MY-FILE-NAME.
  05 PIC X(??)VALUE 'MYDSN.XX'.
  05 MFN-9 999 VALUE 001.
  05 PIC X(??) VALUE 'WHATEVER'.
...
CALL 'COBDYNAL' USING MY-FILE-NAME
...
CSECT COBDYNAL
  SHOP_STANDARD_ENTRY_MACRO,ENTRY=MAIN
*
MYDDNAMA ACB ** YOUR ACB OR DCB HERE **
MYDDNAMR RPL ** YOUR RPL IF NEEDED **
MYDDNAMX EXLST ** YOUR EXLST IF NEEDED **
*
S99ARA DS CL500
AL_DDNAME DC   AL2(DALDDNAM)
  DC    X'0001'
  DC    X'0008'
  DC    CL8'MYDDNAME'
AL_DSNNAME DC  AL2(DALDSNAM)
  DC    X'0001'
ALDSNLL  DC    X'002C'
ALDSN    DC    CL44'MYDSN.XX001.WHATEVER'
AL_STAT   DC   AL2(DALSTATS)
  DC    X'0001'
  DC    X'0001'
  DC    X'08' SHR
  IEFZB4D0
  IEFZB4D2
S99ERBLN EQU   (S99RBEND-S99RB)
MAIN  EQU *
  XR    R15,R15
  USING S99RBP,R1
  LA    R14,S99RBPTR+4
  USING S99RB,R14
  ST    R14,S99RBPTR
  OI    S99RBPTR,S99RBPND
  XC    S99RB(S99ERBLN),S99RB
  MVI   S99RBLN,S99ERBLN
  MVI   S99VERB,S99VRBUN
  LA    R15,S99RB+S99ERBLN
  USING S99TUPL,R15
  ST    R15,S99TXTPP
  LA    R2,AL_DDNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  OI    S99TUPTR,S99TUPLN
  DYNALLOC
  LR    R1,0(R1)
  MVC   ALDSN,0(44,R1)
  XR    R15,R15
  LA    R1,AL_AREA
  XC    0(256,R1),0(R1)
  XC    0(L'AL_AREA-256,R1),256(R1)
  USING S99RBP,R1
  LA    R14,S99RBPTR+4
  USING S99RB,R14
  ST    R14,S99RBPTR
  OI    S99RBPTR,S99RBPND
  XC    S99RB(S99ERBLN),S99RB
  MVI   S99RBLN,S99ERBLN
  MVI   S99VERB,S99VRBAL
  LA    R15,S99RB+S99ERBLN
  XR    R15,R15
  USING S99TUPL,R15
  ST    R15,S99TXTPP
  LA    R2,AL_DDNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  LA    R2,AL_DSNNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  LA    R2,AL_STAT
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  OI    S99TUPTR,S99TUPLN
  DYNALLOC
  SHOP_STANDARD_EXIT_ROUTINE
  END   COBDYNAL

In article <35EAB5A5.8C8D3914@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:
> This is from the proposed standard and not in the currect MVS release.
>
…[39 more quoted lines elided]…
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: IBM mainframe COBOL - how to close an output file and reopen it with a different DSN

- **From:** zberger@ldl.net
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<6sf170$84i$1@nnrp1.dejanews.com>`
- **References:** `<6s0p5r$4v0$1@holly.prod.itd.earthlink.net> <6s7dfq$31b$1@ash.prod.itd.earthlink.net> <6s9f25$cin@dfw-ixnews10.ix.netcom.com> <35ea94fc.773118@news.pnc.com.au> <35EAB5A5.8C8D3914@zip.com.au>`

```
Ok, this is from memory so don't beat me up when the names don't line up
perfectly:

01 MY-FILE-NAME.
  05 PIC X(??)VALUE 'MYDSN.XX'.
  05 MFN-9 999 VALUE 001.
  05 PIC X(??) VALUE 'WHATEVER'.
...
ADD +1 TO MFN-9
CALL 'COBDYNAL' USING MY-FILE-NAME
...
CSECT COBDYNAL
  SHOP_STANDARD_ENTRY_MACRO,ENTRY=MAIN
*
MYDDNAMA ACB ** YOUR ACB OR DCB HERE **
MYDDNAMR RPL ** YOUR RPL IF NEEDED **
MYDDNAMX EXLST ** YOUR EXLST IF NEEDED **
*
S99ARA DS CL500
AL_DDNAME DC   AL2(DALDDNAM)
  DC    X'0001'
  DC    X'0008'
  DC    CL8'MYDDNAME'
AL_DSNNAME DC  AL2(DALDSNAM)
  DC    X'0001'
ALDSNLL  DC    X'002C'
ALDSN    DC    CL44'MYDSN.XX001.WHATEVER'
AL_STAT   DC   AL2(DALSTATS)
  DC    X'0001'
  DC    X'0001'
  DC    X'08' SHR
  IEFZB4D0
  IEFZB4D2
S99ERBLN EQU   (S99RBEND-S99RB)
MAIN  EQU *
  XR    R15,R15
  USING S99RBP,R1
  LA    R14,S99RBPTR+4
  USING S99RB,R14
  ST    R14,S99RBPTR
  OI    S99RBPTR,S99RBPND
  XC    S99RB(S99ERBLN),S99RB
  MVI   S99RBLN,S99ERBLN
  MVI   S99VERB,S99VRBUN
  LA    R15,S99RB+S99ERBLN
  USING S99TUPL,R15
  ST    R15,S99TXTPP
  LA    R2,AL_DDNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  OI    S99TUPTR,S99TUPLN
  DYNALLOC
  LR    R1,0(R1)
  MVC   ALDSN,0(44,R1)
  XR    R15,R15
  LA    R1,AL_AREA
  XC    0(256,R1),0(R1)
  XC    0(L'AL_AREA-256,R1),256(R1)
  USING S99RBP,R1
  LA    R14,S99RBPTR+4
  USING S99RB,R14
  ST    R14,S99RBPTR
  OI    S99RBPTR,S99RBPND
  XC    S99RB(S99ERBLN),S99RB
  MVI   S99RBLN,S99ERBLN
  MVI   S99VERB,S99VRBAL
  LA    R15,S99RB+S99ERBLN
  XR    R15,R15
  USING S99TUPL,R15
  ST    R15,S99TXTPP
  LA    R2,AL_DDNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  LA    R2,AL_DSNNAME
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  LA    R2,AL_STAT
  ST    R2,S99TUPTR
  LA    R15,4(R15)
  OI    S99TUPTR,S99TUPLN
  DYNALLOC
  SHOP_STANDARD_EXIT_ROUTINE
  END   COBDYNAL

In article <35EAB5A5.8C8D3914@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:
> This is from the proposed standard and not in the currect MVS release.
>
…[39 more quoted lines elided]…
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
