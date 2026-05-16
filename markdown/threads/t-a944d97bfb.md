[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fixed and variable length record file under fujitsu

_6 messages · 5 participants · 2005-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### fixed and variable length record file under fujitsu

- **From:** "ari" <unikoski@yahoo.com>
- **Date:** 2005-09-05T09:11:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com>`

```
Using fujitsu .net cobol I am trying to create 2 files - a fixed length
data file and a variable length data file. The code sample is below:

000190 DATA DIVISION.
000200
000210 FILE SECTION.
000220
000230 FD  TEST-FILE
000240
000250     LABEL RECORDS STANDARD
000260
000280     RECORD 30
000290     BLOCK CONTAINS 0.
000300
000310 01  TST-REC.
000320
000330     05 TST-KUKU        PIC X(10).
000340
000350     05 TST-DATA        PIC X(20).
000360
000230 FD  TEST-FILEV
000240
000250     LABEL RECORDS STANDARD
000260
000290     BLOCK CONTAINS 0.
000300
000310 01  TST-RECV.
           05  VAR-TXT.
               10  PIC X OCCURS 0 TO 100 DEPENDING ON VAR-LEN.
   .
   .
   .


000610     OPEN OUTPUT TEST-FILEV.
           MOVE 5 TO VAR-LEN
           MOVE 'HELLO' TO VAR-TXT.
           WRITE TST-RECV.
           SUBTRACT 1 FROM VAR-TXT.
           WRITE TST-RECV.
000690     CLOSE TEST-FILEV.
000590
000600
000610     OPEN OUTPUT TEST-FILE.
000620
000630     MOVE 'KUKU' TO TST-KUKU.
000640
000650     MOVE 'STUM' TO TST-DATA.
000660
000670     WRITE TST-REC.
000630     MOVE 'KUKU' TO TST-DATA.
000640
000650     MOVE 'STUM' TO TST-KUKU.
000660
000670     WRITE TST-REC.
000680


A number of strange things are happening as a result:

a/ On both output files I receive a very strange extra 3 bytes at the
beginning of the file. The hexadecimal values of these bytes are: EF BB
BF.

b/ I am getting an extra 0D 0A at the end of every record.

Any ideas on how to avoid this?
```

#### ↳ Re: fixed and variable length record file under fujitsu

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-09-05T17:56:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54uoh1pseuhus2avkhf4nefq7439viptfh@4ax.com>`
- **References:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com>`

```
On 5 Sep 2005 09:11:39 -0700, "ari" <unikoski@yahoo.com> wrote:

>Using fujitsu .net cobol I am trying to create 2 files - a fixed length
>data file and a variable length data file. The code sample is below:
Please add the SELECT bit as this is of MAJOR importance for your
problem.


>
>000190 DATA DIVISION.
…[62 more quoted lines elided]…
>Any ideas on how to avoid this?


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: fixed and variable length record file under fujitsu

- **From:** "ari" <unikoski@yahoo.com>
- **Date:** 2005-09-05T10:04:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125939868.185272.104620@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<54uoh1pseuhus2avkhf4nefq7439viptfh@4ax.com>`
- **References:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com> <54uoh1pseuhus2avkhf4nefq7439viptfh@4ax.com>`

```
Thanks for you reply, and sorry for missing the "SELECT" (silly me!)-
it is:

000110 FILE-CONTROL.
000120
000130     SELECT  TEST-FILE
000140
000150     ORGANIZATION LINE SEQUENTIAL
           ASSIGN TO MYFILE.

000130     SELECT  TEST-FILEV
000140
000150     ORGANIZATION LINE SEQUENTIAL
           ASSIGN TO MYFILEV.
```

###### ↳ ↳ ↳ Re: fixed and variable length record file under fujitsu

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-05T18:17:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CY%Se.229867$w74.49682@fe03.news.easynews.com>`
- **References:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com> <54uoh1pseuhus2avkhf4nefq7439viptfh@4ax.com> <1125939868.185272.104620@g14g2000cwa.googlegroups.com>`

```
LINE SEQUENTIAL files are neither "fixed" nor "variable" in the normal (ANSI/ISO 
Standard) files are.
```

###### ↳ ↳ ↳ Re: fixed and variable length record file under fujitsu

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-05T11:54:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125946440.354412.72080@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1125939868.185272.104620@g14g2000cwa.googlegroups.com>`
- **References:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com> <54uoh1pseuhus2avkhf4nefq7439viptfh@4ax.com> <1125939868.185272.104620@g14g2000cwa.googlegroups.com>`

```
>  000150     ORGANIZATION LINE SEQUENTIAL

Line sequential files are like text editor files.  The Carriage Return
(x0D) and Line Feed (x0A) at the end of each line are the line
terminators.  The trailing spaces should have been stripped from the
record, but this may need an environment variable to tell it to do so.

I have no idea what the EF BB BF are.

You may want these files to be SEQUENTIAL (ie without LINE).  For
variable length sequential files you will get file and record headers
because _something_ has to tell where the records start and end.
```

#### ↳ Re: fixed and variable length record file under fujitsu

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-09-05T15:45:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11hpbja98qvr39@news.supernews.com>`
- **References:** `<1125936699.866482.140530@g14g2000cwa.googlegroups.com>`

```
ari wrote:
> Using fujitsu .net cobol I am trying to create 2 files - a fixed
> length data file and a variable length data file. The code sample is
…[65 more quoted lines elided]…
> Any ideas on how to avoid this?

The '0D0A' is easy. That's Carriage-return/Line-feed which is appended to 
the end of every record whose SELECT statement contains "ORGANIZATION IS 
LINE SEQUENTIAL"

Take out the following stuff:

LABEL RECORDS STANDARD
BLOCK CONTAINS 0
RECORD nnn
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
