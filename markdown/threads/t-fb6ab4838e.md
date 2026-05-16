[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL (OS/390) and VB-Files / Short Blocks

_3 messages · 2 participants · 2001-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL (OS/390) and VB-Files / Short Blocks

- **From:** Beat Gossweiler <beat.gossweiler@dp-solutions.ch>
- **Date:** 2001-10-24T03:15:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD62434.CDD3F2E4@dp-solutions.ch>`

```
Maybe anybody (OS/390 DFSMS-/COBOL-People) can help me with this:

I am writing a variable-blocked file with a cobol program under OS/390.
I can do this
with two methods, but I have the same problem with both methods, both
follow at the end of this entry:

My blocks are all too short The symptoms are:
================================

- Without specifying a LRECL/BLKSIZE/RECFM in JCL (DISP=NEW), the
dataset gets created with LRECL=27994, BLKSIZE=27998, RECFM=VB, which is

correct.
- But the blocks written all contain 1 (ONE) record at 96 (or 100 with
RDW) bytes only. 100 records give 100 blocks.
- If i increase the blocksize in JCL to e.g. 32760, the blocks are
filled up to approx. 12KB, then the next block is written.

My suspicion:
Whoever writes (or fills) the blocks does the following:
- move data into block
- if rest of block is < LRECL then write block
In the case of LRECL=BLKSIZE-4, this results in 1 block per record,
independant of the actual record-size written.
But this assumption would be wrong, since the next record written might
very well be smaller than LRECL.

Can anybody explain please.

Method1:

       FILE SECTION.
      *=============
       FD  DDOUT            BLOCK CONTAINS 0 RECORDS
                                       RECORDING MODE V.
       01  DDOUT-RECORD.
           05  DDOUT-BYTE              PIC X OCCURS 27990
                                       DEPENDING ON DDOUT-LRECL.
       WORKING-STORAGE SECTION.
      *========================
       01  DDOUT-LRECL                 PIC 9(08) COMP.
       PROCEDURE DIVISION.
      *===================
               MOVE 96 TO DDOUT-LRECL
               MOVE 'ABC' TO DDOUT-RECORD(1:100)
               WRITE DDOUT-RECORD


Method2:

       FILE SECTION.
      *=============
       FD  DDOUT                       BLOCK CONTAINS 0 RECORDS
                                       RECORD VARYING
                                       FROM 1 TO 27990 CHARACTERS
                                       DEPENDING ON DDOUT-LRECL
                                       RECORDING MODE V
                                       LABEL RECORDS STANDARD.

       01  DDOUT-RECORD                PIC X(27990).
       WORKING-STORAGE SECTION.
      *========================
       01  DDOUT-LRECL                 PIC 9(08) COMP.
       PROCEDURE DIVISION.
      *===================
               MOVE 96 TO DDOUT-LRECL
               MOVE 'ABC' TO DDOUT-RECORD
               WRITE DDOUT-RECORD

Thanks
Beat Gossweiler
DP Solutions AG
Zurich, Switzerland
```

#### ↳ Re: COBOL (OS/390) and VB-Files / Short Blocks

- **From:** Beat Gossweiler <beat.gossweiler@dp-solutions.ch>
- **Date:** 2001-10-24T08:45:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD671B4.492ABF1D@dp-solutions.ch>`
- **References:** `<3BD62434.CDD3F2E4@dp-solutions.ch>`

```
The problem has been solved using APPLY WRITE-ONLY or AWO compiler-option.

Beat Gossweiler wrote:

> Maybe anybody (OS/390 DFSMS-/COBOL-People) can help me with this:
>
…[70 more quoted lines elided]…
> Zurich, Switzerland
```

#### ↳ Re: COBOL (OS/390) and VB-Files / Short Blocks

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-10-24T11:23:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ro1dttkfq6bl082djsuh2kg69qirct59q0@4ax.com>`
- **References:** `<3BD62434.CDD3F2E4@dp-solutions.ch>`

```
On Wed, 24 Oct 2001 03:15:16 +0100 Beat Gossweiler
<beat.gossweiler@dp-solutions.ch> wrote:

:>Maybe anybody (OS/390 DFSMS-/COBOL-People) can help me with this:

:>I am writing a variable-blocked file with a cobol program under OS/390.
:>I can do this
:>with two methods, but I have the same problem with both methods, both
:>follow at the end of this entry:

:>My blocks are all too short The symptoms are:
:>================================

:>- Without specifying a LRECL/BLKSIZE/RECFM in JCL (DISP=NEW), the
:>dataset gets created with LRECL=27994, BLKSIZE=27998, RECFM=VB, which is
:>correct.
:>- But the blocks written all contain 1 (ONE) record at 96 (or 100 with
:>RDW) bytes only. 100 records give 100 blocks.
:>- If i increase the blocksize in JCL to e.g. 32760, the blocks are
:>filled up to approx. 12KB, then the next block is written.

:>My suspicion:
:>Whoever writes (or fills) the blocks does the following:
:>- move data into block
:>- if rest of block is < LRECL then write block
:>In the case of LRECL=BLKSIZE-4, this results in 1 block per record,
:>independant of the actual record-size written.
:>But this assumption would be wrong, since the next record written might
:>very well be smaller than LRECL.

:>Can anybody explain please.

1.2.2.3.2 APPLY WRITE-ONLY Clause
 
The APPLY WRITE-ONLY clause makes optimum use of buffer and device space when
creating a sequential file with blocked V-mode records.  With APPLY WRITE-ONLY
specified, a buffer is truncated only when the next record does not fit in the
unused remainder of the buffer.  Without APPLY WRITE-ONLY specified, a buffer
is truncated when not enough space remains in it to accommodate the maximum
size record.
 
The AWO compiler option applies the APPLY WRITE-ONLY clause to all eligible
files.  The NOAWO compiler option has no effect on files that have the APPLY
WRITE-ONLY clause specified.
 
The APPLY WRITE-ONLY clause has meaning only when the file has standard
sequential organization.
 
Use of the APPLY-WRITE ONLY clause can cause input files to use a record area
rather than process the data in the buffer.  This might affect INPUT file
processing as well as OUTPUT file processing.

   [ snipped ]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
