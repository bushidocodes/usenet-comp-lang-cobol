[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed files in Cobol

_11 messages · 6 participants · 2003-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed files in Cobol

- **From:** ZeroCartin <member28650@dbforums.com>
- **Date:** 2003-04-24T17:19:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2803057.1051204765@dbforums.com>`

```

Well, it appears I'm having some trouble. When I try to REWRITE or just
open and indexed file as I-O (input-output) , i get some errors running
the program. There's a pop-up window that says:
"JMP03301I-I STATEMENT SEQUENCE ERROR. STM=READ. FILE Est2.idx. 'POS
ERROR'. PGM SHEETACT ADR=00401516"
And as you know, it did't rewrite in the file. I'll post the code of
that part for u guys to help me pinpoint the problem.

 ID DIVISION.
 PROGRAM-ID. ACTUALIZAR IS COMMON.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        77 ROW          PIC 99.
        77 COL          PIC 99.
        77 X            PIC 99.
        77 MAXROW   PIC 99.
 PROCEDURE   DIVISION.
 INICIO.
                MOVE POW-ROWS OF TABLE2 TO MAXROW.
                OPEN I-O ESTUDIANTES.
                MOVE 0 TO E-CARNE EOF-ESTUDIANTES.
                MOVE POW-SELSTRING OF CCODIGO TO E-CUR.
                START ESTUDIANTES KEY IS = CURSOCARNE
                        INVALID KEY MOVE 1 TO EOF-ESTUDIANTES.
                CALL "LEER-ESTUDIANTES".
                PERFORM VARYING ROW FROM 1 BY 1 UNTIL ROW > MAXROW
                  PERFORM VARYING X FROM 1 BY 1 UNTIL X >
                  E-NUMNOTASCURSO
                        ADD 2 TO X GIVING COL
                        MOVE POW-NUMERIC(ROW COL) OF TABLE2 TO
                        E-NOTAS(X)
                  END-PERFORM
                  MOVE POW-NUMERIC(ROW 11) OF TABLE2 TO E-NOTAFIN
                  REWRITE R-ESTUDIANTES
                  CALL "LEER-ESTUDIANTES"
                END-PERFORM.
                MOVE POW-ON TO POW-ENABLE OF BORDCAR.
                MOVE POW-ON TO POW-ENABLE OF BORDNOM.
                CLOSE ESTUDIANTES.
        END PROGRAM ACTUALIZAR.
```

#### ↳ Re: Indexed files in Cobol

- **From:** ZeroCartin <member28650@dbforums.com>
- **Date:** 2003-04-24T17:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2803369.1051205823@dbforums.com>`
- **References:** `<2803057.1051204765@dbforums.com>`

```

oh, btw, heres the FileControl

      SELECT CURSOS ASSIGN TO "CURSOS.DAT"
         ORGANIZATION IS SEQUENTIAL.

                 SELECT ESTUDIANTES ASSIGN TO "Est2.idx"
                        ORGANIZATION IS INDEXED
                        ACCESS MODE IS DYNAMIC
                        RECORD KEY IS CURSOCARNE
                    ALTERNATE RECORD KEY IS E-NOMBRE WITH DUPLICATES
                        ALTERNATE RECORD KEY IS E-CARNE WITH DUPLICATES
                        ALTERNATE RECORD KEY IS E-CUR E-NOMBRE
                        FILE STATUS IS STATUS-EST.
```

#### ↳ Re: Indexed files in Cobol

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-04-24T20:45:13+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798gavo82r4c5fo0tndun9hi3q4h57firc@4ax.com>`
- **References:** `<2803057.1051204765@dbforums.com>`

```
On Thu, 24 Apr 2003 17:19:25 +0000 ZeroCartin <member28650@dbforums.com>
wrote:

:>Well, it appears I'm having some trouble. When I try to REWRITE or just
:>open and indexed file as I-O (input-output) , i get some errors running
:>the program. There's a pop-up window that says:
:>"JMP03301I-I STATEMENT SEQUENCE ERROR. STM=READ. FILE Est2.idx. 'POS
:>ERROR'. PGM SHEETACT ADR=00401516"
:>And as you know, it did't rewrite in the file. I'll post the code of
:>that part for u guys to help me pinpoint the problem.

From the segment you are posting it would appear that you are processing the
file sequentially by reading the file into a tables and then attempting to
rewrite all the records at once from the table. 

1. That will not work unless ACCESS IS DYNAMIC.

2. You must set the record key before the rewrite.

At any rate the error message indicates the problem is with a read. And a
different program name. But I digress.
```

##### ↳ ↳ Re: Indexed files in Cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-24T19:52:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JfXpa.3166$%_3.2515912@newssrv26.news.prodigy.com>`
- **References:** `<2803057.1051204765@dbforums.com> <798gavo82r4c5fo0tndun9hi3q4h57firc@4ax.com>`

```
If  a file is ACCESS DYNAMIC, you use 'READ filename NEXT [INTO xxx] ', not
'READ filename [INTO xxx] ' after a
START.

MCM

> On Thu, 24 Apr 2003 17:19:25 +0000 ZeroCartin <member28650@dbforums.com>
> wrote:
…[5 more quoted lines elided]…
> :>ERROR'. PGM SHEETACT ADR=00401516"
```

#### ↳ Re: Indexed files in Cobol

- **From:** "marti" <martinez@sapengineering.it>
- **Date:** 2003-04-24T19:48:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b897p5$et9$1@fata.cs.interbusiness.it>`
- **References:** `<2803057.1051204765@dbforums.com>`

```
You have not  readfile ESTUDIANTES before rewrite or you have a invalid key
in START and not tested  EOF-ESTUDIANTES before rewrite.
```

#### ↳ Re: Indexed files in Cobol

- **From:** ZeroCartin <member28650@dbforums.com>
- **Date:** 2003-04-24T20:14:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2803928.1051215288@dbforums.com>`
- **References:** `<2803057.1051204765@dbforums.com>`

```

Well, first off, the file Est2.idx IS Dynamic..

SELECT ESTUDIANTES ASSIGN TO "Est2.idx"
ORGANIZATION IS INDEXED
ACCESS MODE IS DYNAMIC

BINYAMIN: What do u mean set the record key before the start?

Michael: I AM reading as READ filename NEXT, declared on the procedure:

 ID DIVISION.
        PROGRAM-ID. LEER-ESTUDIANTES IS COMMON.
 PROCEDURE DIVISION.
                READ ESTUDIANTES NEXT AT END MOVE 1 TO EOF-ESTUDIANTES.
        END PROGRAM LEER-ESTUDIANTES.

Still cant figure out whats wrong....
```

##### ↳ ↳ Re: Indexed files in Cobol

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-24T20:36:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA84717.1FD2C9F2@shaw.ca>`
- **References:** `<2803057.1051204765@dbforums.com> <2803928.1051215288@dbforums.com>`

```


ZeroCartin wrote:

> Well, first off, the file Est2.idx IS Dynamic..
>
…[5 more quoted lines elided]…
> <snip>

I don't *do* Fujitsu, so I can't really help. BUT - check the file status
to see if the explanation of the file status code gives you a clue. Check
you F/J on-line help for file status codes.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Indexed files in Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-24T19:49:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304241849.7d0a735f@posting.google.com>`
- **References:** `<2803057.1051204765@dbforums.com> <2803928.1051215288@dbforums.com>`

```
ZeroCartin <member28650@dbforums.com> wrote

>  ID DIVISION.
>         PROGRAM-ID. LEER-ESTUDIANTES IS COMMON.
…[4 more quoted lines elided]…
> Still cant figure out whats wrong....

You are not checking the result of any of your file actions.

An OPEN can fail because the file doesn't exist or for many other
reasons.  You need to check the File Status after the OPEN.

That START may fail and take the INVALID KEY which sets EOF-~ to 1,
but you carry on and ignore this.

The READ also may reach AT END and set EOF which sets EOF-~, but you
ignore this, it is likely that the error message is telling you that
you have tried to READ after the end of file or after the START
failed.

Your program is written as if you expect it to work perfectly, this is
why you can't figure it out.

Write your programs as if you expect everything to fail and be
surprised when it works.

> START ESTUDIANTES KEY IS = CURSOCARNE
>     INVALID KEY 
          MOVE 1 TO EOF-ESTUDIANTES
      NOT INVALID KEY
>         CALL "LEER-ESTUDIANTES"
>         PERFORM VARYING ROW FROM 1 BY 1 
            UNTIL ROW > MAXROW
                OR EOF-ESTUDIANTES = 1
            ....

Alternately you may want to WRITE records when the READ has failed to
get one.
```

#### ↳ Re: Indexed files in Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-25T08:49:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b89iml$mtp$1@aklobs.kc.net.nz>`
- **References:** `<2803057.1051204765@dbforums.com>`

```
ZeroCartin wrote:

> Well, it appears I'm having some trouble. When I try to REWRITE or just
> open and indexed file as I-O (input-output) , i get some errors running
> the program. There's a pop-up window that says:
> "JMP03301I-I STATEMENT SEQUENCE ERROR. STM=READ. FILE Est2.idx. 'POS
> ERROR'. PGM SHEETACT ADR=00401516"

Do we have to guess which compiler you are using ?  I'd say Fujitsu 3.

> And as you know, it did't rewrite in the file. I'll post the code of
> that part for u guys to help me pinpoint the problem.
> 
>  ID DIVISION.
>  PROGRAM-ID. ACTUALIZAR IS COMMON.

This isn't 'PGM SHEETACT' as given in the error message.

>         DATA DIVISION.
>         WORKING-STORAGE SECTION.
…[7 more quoted lines elided]…
>                 OPEN I-O ESTUDIANTES.

You appear to be missing the SELECT and the FD.  Is this a nested program 
and these are global in the outer program ?

>                 MOVE 0 TO E-CARNE EOF-ESTUDIANTES.
>                 MOVE POW-SELSTRING OF CCODIGO TO E-CUR.
…[17 more quoted lines elided]…
>         END PROGRAM ACTUALIZAR.

I see no READ at all.  The message complians about STM=READ 
(statement=READ) and indicates 'Statement sequence error'.

A REWRITE should follow a READ.  If these are new records then you should 
use WRITE.
```

#### ↳ Re: Indexed files in Cobol

- **From:** ZeroCartin <member28650@dbforums.com>
- **Date:** 2003-04-24T22:36:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2804710.1051223776@dbforums.com>`
- **References:** `<2803057.1051204765@dbforums.com>`

```

hehe, nevermind guys, i found my mistake... i was putting REWRITE
R-ESTUDIANTES, when the filename is ESTUDIANTES... hehehe, sorry bout
that, and thanks anyways
```

##### ↳ ↳ Re: Indexed files in Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-25T11:28:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b89s0l$qnc$1@aklobs.kc.net.nz>`
- **References:** `<2803057.1051204765@dbforums.com> <2804710.1051223776@dbforums.com>`

```
ZeroCartin wrote:

> hehe, nevermind guys, i found my mistake... i was putting REWRITE
> R-ESTUDIANTES, when the filename is ESTUDIANTES... hehehe, sorry bout
> that, and thanks anyways

It is READ file, WRITE/REWRITE record.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
