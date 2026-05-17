[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initiation of a batch job from COBOL code

_8 messages · 7 participants · 1996-05_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### Initiation of a batch job from COBOL code

- **From:** "judy laforce" <ua-author-17086699@usenetarchives.gap>
- **Date:** 1996-05-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4moeg1$t7l@doc.zippo.com>`

```

I would like to initiate a batch job from inside a COBOL program. I am using COBOL II on IBM.
Is there anyone that has done this?
```

#### ↳ Re: Initiation of a batch job from COBOL code

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4moeg1$t7l@doc.zippo.com>`
- **References:** `<4moeg1$t7l@doc.zippo.com>`

```

Judy, LaForce wrote:
›
› I would like to initiate a batch job from inside a COBOL program. I am using COBOL II on IBM.
› Is there anyone that has done this?

It depends on what you mean by initiate, if you are going to construct JCL within your program, then
you should write it out to an 80 byte file, and follow your programs execution with an Iebgener or
similar to the internal reader, whose DD name I cannot remember but I will look up.
```

##### ↳ ↳ Re: Initiation of a batch job from COBOL code

- **From:** "wbla..." <ua-author-620238@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a1b89e4da-p2@usenetarchives.gap>`
- **References:** `<4moeg1$t7l@doc.zippo.com> <gap-6a1b89e4da-p2@usenetarchives.gap>`

```

On Wed, 08 May 1996 00:34:16 -0400, Keith Farndon
wrote:

› Judy, LaForce wrote:
›› 
…[5 more quoted lines elided]…
› similar to  the internal reader, whose DD name I cannot remember but I will look up.

IEFRDR, and you don't need a separate GENER step, you can set it up as
an output file directly from the COBOL program. I've done it, and it
works like a charm.

Regards,
Bill
```

###### ↳ ↳ ↳ Re: Initiation of a batch job from COBOL code

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a1b89e4da-p3@usenetarchives.gap>`
- **References:** `<4moeg1$t7l@doc.zippo.com> <gap-6a1b89e4da-p2@usenetarchives.gap> <gap-6a1b89e4da-p3@usenetarchives.gap>`

```

William Blakemore wrote:
› 
› On Wed, 08 May 1996 00:34:16 -0400, Keith Farndon
…[16 more quoted lines elided]…
› Bill

Thanks for the memory jog Bill, just one thing, I would be a little
reticent in writing straight to the internal reader from the program, I
would get nervous about loops and things clogging up JES with millions
of lines of JCL. Writing to file has the advantage of, If something
goes wrong I will blow up with a space abend before going near the
reader. Also gives you the advantage of being able to resubmit the job
with out rerunning the program, especially if updates have taken place
in the generating program which are not present for a rerun.
```

#### ↳ Re: Initiation of a batch job from COBOL code

- **From:** "david_..." <ua-author-3348436@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4moeg1$t7l@doc.zippo.com>`
- **References:** `<4moeg1$t7l@doc.zippo.com>`

```

In article <4moeg1$t.··.@doc··o.com>, JudyLaForce says...
› 
› I would like to initiate a batch job from inside a COBOL program.  I am 
› using CO
› BOL II on IBM.  
› Is there anyone that has done this?

You could write the jcl to a file that is set up as an internal
reader - //anyname dd sysout=(a,intrdr).

More details are in mvs jcl and jes books.
```

#### ↳ Re: Initiation of a batch job from COBOL code

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-05-08T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4moeg1$t7l@doc.zippo.com>`
- **References:** `<4moeg1$t7l@doc.zippo.com>`

```

In article <4moeg1$t.··.@doc··o.com>, JudyLaForce says...
›
› I would like to initiate a batch job from inside a COBOL program. I am
› using COBOL II on IBM.
› Is there anyone that has done this?


It is very simple to do. The sample program below will initiate a
JCL batch run from with Cobol. A sample run JCL to run the program is
also provided. Note that the only thing different is that the DD
statement directs the AUTORUN output file (JCL statements) to INTRDR,
which is how the job get initiated from with Cobol--Simple!

Change the 01 JCL-DATA items to fit your needs before running.

000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. AUTOJCL.
001030****************************************************************
001031* THIS PROGRAM DEMONSTRATES CREATING AND INITIATING A BATCH JOB*
001032* JCL STREAM FROM WITHIN A COBOL PROGRAM. ALL JCL ARE WRITTEN *
001033* TO A DD WRITTEN AS //AUTORUN DD SYSOUT=(A,INTRDR). THIS FORM*
001034* OF A DD AUTOMATICALLY INVOKES THE JOB. *
001035* NOTE - (A, INTRDR) WHERE A = JOB CLASS *
001036****************************************************************
001037
001040 ENVIRONMENT DIVISION.
001050 CONFIGURATION SECTION.
001060 SOURCE-COMPUTER. IBM-MVS.
001070 OBJECT-COMPUTER. IBM-MVS.
001080 SPECIAL-NAMES.
001090 INPUT-OUTPUT SECTION.
001100
001110 FILE-CONTROL.
001120 SELECT AUTORUN-FILE ASSIGN TO AUTORUN
001160 ACCESS IS SEQUENTIAL
001180 ORGANIZATION IS SEQUENTIAL.
001190
001200 DATA DIVISION.
001210
001220 FILE SECTION.
001230
001280
001290 FD AUTORUN-FILE
001300 LABEL RECORDS STANDARD
001301 RECORDING MODE IS F
001310 BLOCK CONTAINS 00000 CHARACTERS
001320 RECORD CONTAINS 80 CHARACTERS.
001330 01 JCL-RECORD PIC X(80).
001340
001450
001460 WORKING-STORAGE SECTION.
001470
001471 01 JCL-DATA.
001472 03 JCL-01 PIC X(56) VALUE
001473 "//MS10J JOB (000150T),'MIKE DODAS',CLASS=A,NOTIFY=MS10,".
001474
001475 03 JCL-02 PIC X(56) VALUE
001476 "// MSGCLASS=X ".
001477
001478 03 JCL-03 PIC X(56) VALUE
001479 "//COPY EXEC PGM=IDCAMS,REGION=512K ".
001480
001481 03 JCL-04 PIC X(56) VALUE
001482 "//INPUT DD DSN=MS10.SOURCE.COBOL(AUTOJCL),DISP=SHR ".
001483
001484 03 JCL-05 PIC X(56) VALUE
001485 "//OUTPUT DD DUMMY,DCB=(BLKSIZE=2300) ".
001486
001487 03 JCL-06 PIC X(56) VALUE
001488 "//SYSPRINT DD SYSOUT=X ".
001489
001490 03 JCL-07 PIC X(56) VALUE
001491 "//SYSIN DD * ".
001492
001493 03 JCL-08 PIC X(56) VALUE
001500 " REPRO INFILE(INPUT) OUTFILE(OUTPUT) ".
001501
001502 03 JCL-09 PIC X(56) VALUE
001503 "/* ".
001504
003430
003440 PROCEDURE DIVISION.
003480 OPEN OUTPUT AUTORUN-FILE.
003490 START-PROCESSING.
003500 PERFORM
003510 WRITE JCL-RECORD FROM JCL-01
003511 WRITE JCL-RECORD FROM JCL-02
003512 WRITE JCL-RECORD FROM JCL-03
003513 WRITE JCL-RECORD FROM JCL-04
003514 WRITE JCL-RECORD FROM JCL-05
003515 WRITE JCL-RECORD FROM JCL-06
003516 WRITE JCL-RECORD FROM JCL-07
003517 WRITE JCL-RECORD FROM JCL-08
003518 WRITE JCL-RECORD FROM JCL-09
003520 END-PERFORM.
003530 CLOSE AUTORUN-FILE.
003550 STOP RUN.
005180



JCL to run AUTOJCL:

//AUTOJCL JOB (000150T),'MY JOB',MSGCLASS=X,CLASS=A
//JOBLIB DD DSN=MY.LOADLIB,DISP=SHR
//AUTOJCL EXEC PGM=AUTOJCL,REGION=512K
//AUTORUN DD SYSOUT=(A,INTRDR)
//


Hope this helps.

Mike Dodas
```

#### ↳ Re: Initiation of a batch job from COBOL code

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1996-05-08T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p7@usenetarchives.gap>`
- **In-Reply-To:** `<4moeg1$t7l@doc.zippo.com>`
- **References:** `<4moeg1$t7l@doc.zippo.com>`

```

In <4moeg1$t.··.@doc··o.com>, Judy LaForce writes:
› I would like to initiate a batch job from inside a COBOL program. I am using COBOL II on IBM.
› Is there anyone that has done this?
I did this with an other programming language but it should also work with
COBOL. Just add the following to your JCL

//INTRDR DD SYSOUT=(A,INTRDR)

Within your COBOL programm define a sequential file named INTRDR with RECL 80
and write your JCL lines to this file.
The Job is submitted as soon as you close the file.

Peter
```

##### ↳ ↳ Re: Initiation of a batch job from COBOL code

- **From:** "michael lhevan" <ua-author-17087293@usenetarchives.gap>
- **Date:** 1996-05-12T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a1b89e4da-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a1b89e4da-p7@usenetarchives.gap>`
- **References:** `<4moeg1$t7l@doc.zippo.com> <gap-6a1b89e4da-p7@usenetarchives.gap>`

```

Can you please send me some COBOL Infon please.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
