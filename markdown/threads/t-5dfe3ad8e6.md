[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol85 Problem

_4 messages · 3 participants · 2003-10_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Cobol85 Problem

- **From:** Greg Good <member46468@dbforums.com>
- **Date:** 2003-10-30T20:28:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3543767.1067563715@dbforums.com>`

```

I've just downloaded Cobol85.  I am able to compile link and execute.  I
wrote a program that reads a file with records 1200 bytes long.  I can
read the records and write them to an output file ok.  When I try to
break the input record down in working storage I am getting bad results.
The data in working storage is loosing the data on the right end of the
field at the rate of 1 character per record.  Anybody have any ideas?



The Program:

000010 IDENTIFICATION DIVISION.

000020  PROGRAM-ID. Chk810tst.

000030*

000040 ENVIRONMENT DIVISION.

000050 INPUT-OUTPUT SECTION.

000060 FILE-CONTROL.

000070     SELECT 810-FILE

000080     ASSIGN       TO  infile

000090     ORGANIZATION IS  SEQUENTIAL.

000100

000110     SELECT 810fix-FILE

000120     ASSIGN       TO  OUTFILE

000130     ORGANIZATION IS  SEQUENTIAL.

000140*

000150 DATA DIVISION.

000160 FILE SECTION.

000170 FD  810-FILE.

000180 01  810-RECORD                pic x(1201).

000190

000200

000210 FD  810fix-FILE.

000220 01  810fix-RECORD             pic x(50).

000230

000240 WORKING-STORAGE SECTION.

000250 01  recid-hold                pic x(5).

000260 01  rec-count                 pic 9(5).

000270 01  HdrRec-Info               pic x(50).

000280

000290 01  wk-RECORD.

000300     02  wk-HdrRec-info.

000310       03  wk-recid            pic x(5).

000320       03  filler              pic x(45).

000330     02  filler                pic x(1151).

000340

000350 PROCEDURE DIVISION.

000360      OPEN INPUT  810-fILE.

000370      OPEN OUTPUT 810fix-FILE.

000380      move 0 to rec-count.

000390*

000400 Read-input.

000410      READ 810-FILE AT END GO TO End-Prog.

000420      move 810-record to wk-record.

000430      move wk-HdrRec-info to 810fix-record.

000440

000450      WRITE 810fix-record.

000460      add 1 to rec-count.

000470      if rec-count > 10 then

000480        go to end-prog

000490      end-if.

000500

000510      GO TO Read-input.

000520*

000530 End-Prog.

000540      CLOSE  810-FILE 810fix-FILE.

000550 END PROGRAM Chk810tst.

000560



Help Please,

Greg Good
```

#### ↳ Re: Cobol85 Problem

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-10-30T21:39:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vq3mc1pifodm06@corp.supernews.com>`
- **In-Reply-To:** `<3543767.1067563715@dbforums.com>`
- **References:** `<3543767.1067563715@dbforums.com>`

```
Greg Good wrote:
> I've just downloaded Cobol85.  I am able to compile link and execute.  I
> wrote a program that reads a file with records 1200 bytes long.  I can
…[3 more quoted lines elided]…
> field at the rate of 1 character per record.  Anybody have any ideas?
...
> 000170 FD  810-FILE.
> 
> 000180 01  810-RECORD                pic x(1201).

If this is actually reading the file byte by byte, and the records are 
1200, the FD is your problem.  The first read would get the 1200 bytes 
from record 1, and the first byte from record 2.  Then, the 2nd read 
would get bytes 2-1200 of record 2, and 2 bytes of record 3; the 3rd 
read gets 3-1200 of record 3 and 1-3 of record 4; you get the idea. 
Since you're only writing the first 50 bytes of the record, it's 
gradually shifting over.
```

#### ↳ Re: Cobol85 Problem

- **From:** "Dan" <deacondan25@N.O.S.P.A.M.hotmail.com>
- **Date:** 2003-10-31T02:01:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vq45ln2hd3re14@corp.supernews.com>`
- **References:** `<3543767.1067563715@dbforums.com>`

```

"Greg Good" <member46468@dbforums.com> wrote in message
news:3543767.1067563715@dbforums.com...
>
> I've just downloaded Cobol85.  I am able to compile link and execute.  I
…[4 more quoted lines elided]…
> field at the rate of 1 character per record.  Anybody have any ideas?

I seem to remember having this problem when I converted to Unix. You seem to
be trying to account for the LF character at the end of the record.
Change
01  810-RECORD                pic x(1201).
back to
01  810-RECORD                pic x(1200).

and use
    SELECT FILE-NAME    ASSIGN TO 'filename'
       ORGANIZATION IS LINE SEQUENTIAL.

Instead of Organization is Sequential.

If I remember correctly, that's all we had to do.

--Dan
```

#### ↳ Re: Cobol85 Problem

- **From:** Greg Good <member46468@dbforums.com>
- **Date:** 2003-10-31T11:52:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3546003.1067619134@dbforums.com>`
- **References:** `<3543767.1067563715@dbforums.com>`

```

Dan,

Thank you for your suggestion about adding LINE to Sequence.  That did
the trick.

Greg Good
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
