[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS & Batch MVS Subroutines

_4 messages · 4 participants · 1995-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS & Batch MVS Subroutines

- **From:** "lar..." <ua-author-28870@usenetarchives.gap>
- **Date:** 1995-07-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3tflei$mkq@maureen.teleport.com>`

```
Has anyone had any luck sharing subroutines between CICS and batch MVS
regions? If so, how did you do it? We're attempting to develop common
routines that --ideally-- can be shared in either environment. Thanks
```

#### ↳ Re: CICS & Batch MVS Subroutines

- **From:** "massimo rainato" <ua-author-17088097@usenetarchives.gap>
- **Date:** 1995-07-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed15d00cdd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3tflei$mkq@maureen.teleport.com>`
- **References:** `<3tflei$mkq@maureen.teleport.com>`

```
Hi, Larry.

You (lar··.@tel··t.com) wrote:
› Has anyone had any luck sharing subroutines between CICS and batch MVS
› regions? If so, how did you do it? We're attempting to develop common
› routines that --ideally-- can be shared in either environment. Thanks
›
>From an italian cobol programmers, (so i hope no mistakes with english)

Can be the solution to be insert as copy the main program section,
except for the interface with external world (cics or batch), with a
single modification we mantain aligned the twin-routines. Yes, also
the interface with archive is in copy, a ''read in vsam'' or a find in
db2-table are made with the respective copy, ...

I hope this help, otherwise...
...+.*..1....+....2....+....3....+....4
ADD ONE-MAIL TO MY-MAILBOX.
* ;-)
--Max
```

#### ↳ Re: CICS & Batch MVS Subroutines

- **From:** "jco..." <ua-author-11185940@usenetarchives.gap>
- **Date:** 1995-07-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed15d00cdd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3tflei$mkq@maureen.teleport.com>`
- **References:** `<3tflei$mkq@maureen.teleport.com>`

```
Larry Tan (lar··.@tel··t.com) wrote:
: Has anyone had any luck sharing subroutines between CICS and batch MVS
: regions? If so, how did you do it? We're attempting to develop common
: routines that --ideally-- can be shared in either environment. Thanks

We developed a small assembler routine which is able to check whether the
current program is executing under 'DFHSIP' or not, and return a flag
accordingly. Our common sub-routines all call this module (which is
statically linked into them) and then manipulate the passed parameter
addresses depending on whether DFHEIBLK and DFHCOMMAREA are to be expected
or not.

All the subroutines are compiled and linked for CICS. These load modules
can then be executed in both CICS and Batch MVS.

John Cooper
"May the Farce be with you" -- Oldie One Gone Mouldie
```

#### ↳ Re: CICS & Batch MVS Subroutines

- **From:** "needcrew" <ua-author-17087950@usenetarchives.gap>
- **Date:** 1995-07-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed15d00cdd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3tflei$mkq@maureen.teleport.com>`
- **References:** `<3tflei$mkq@maureen.teleport.com>`

```
You can statically link the routines in under CICS. Taht way you compile
them as TSO but they can be accessed via an online stub program.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
