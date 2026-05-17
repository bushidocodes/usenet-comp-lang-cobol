[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multi-Level FD in RM-COBOL

_4 messages · 4 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Multi-Level FD in RM-COBOL

- **From:** "wmyeung" <ua-author-17086651@usenetarchives.gap>
- **Date:** 1996-12-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`

```

I have a problem about FD in Multi-Level 01 in RM-COBOL 6.00.

For example :

004900 FD DAYTRAN
005000 RECORD CONTAINS 21 TO 58 CHARACTERS
005100 LABEL RECORDS ARE STANDARD
005200 BLOCK CONTAINS 512 CHARACTERS.
005300*
005400*
005500 01 DAYTRAN-RECORD-1.
005600 02 DAYTRAN-KEY.
005700 03 DTC PIC 99.
005800 03 DCRT PIC 9.
005900 03 DSEQ1 PIC 9(3).
006000 03 DSEQ2 PIC 99.
006100 03 DFMT PIC 9.
006200 02 DCMPY1 PIC X.
006300 02 DTENANT1 PIC X(5).
006400 02 DDNNO1 PIC X(8).
006500 02 DRECDATE PIC X(8).
8612IT
006600 02 DAMOUNT1 PIC S9(7)V99 COMP-3.
006700 02 DFULLPAY PIC X.
006800 02 DTC04DESC.
006900 03 DTC04DESC-1 PIC X(17).
8612IT
007000 03 DTC04DESC-2 PIC X.
8612IT
007100*
007200*
007300 01 DAYTRAN-RECORD-2.
007400 02 FILLER PIC X(9).
007500 02 DDNNO2 PIC X(8).
007600 02 DCHRGCODE2 PIC 99.
007700 02 DAREA2 PIC X(9).
007800 02 DAMOUNT2 PIC S9(7)V99 COMP-3.
007900 02 DPAYCODE PIC X.
008000 02 DPAYDAY PIC 99 COMP-6.
008100 02 DPAYBANK PIC X(5).
008200*
008300*
008400 01 DAYTRAN-RECORD-3.
008500 02 FILLER PIC X(9).
008600 02 DCMPY3 PIC X.
008700 02 DTENANT3 PIC X(5).
008800 02 DDNNO3 PIC X(8).
008900 02 DCHRGCODE3 PIC 99.
009000 02 DAREA3 PIC X(9).
009100 02 DDRCR PIC X.
009200 02 DAMOUNT3 PIC S9(7)V99 COMP-3.
009300 02 DTC07DESC.
009400 03 DTC07DESC-1 PIC X(17).
8612IT
009500 03 DTC07DESC-2 PIC X.
8612IT
009600*
009700*
009800 01 DAYTRAN-LABEL.
009900 02 FILLER PIC X(9).
010000 02 DCRT0 PIC 9(3).
010100 02 DCRT1 PIC 9(3).
010200 02 DCRT2 PIC 9(3).
010300 02 DCRT3 PIC 9(3).
010400/

Could anyone help me, I want to know how the cobol data file structure. It
was because it is a varity lenght data file. Inside the data file how can I
determine what
type of FD 01 created.

Thankyou for all your attention.
```

#### ↳ Re: Multi-Level FD in RM-COBOL

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1996-12-16T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e74fe8ec2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`
- **References:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`

```

wmyeung wrote:
› 
› I have a problem about FD in Multi-Level 01 in RM-COBOL 6.00.
…[70 more quoted lines elided]…
› Thankyou for all your attention.

If your compiler supports it, the best solution would look like this:
FD DAYTRAN
RECORD IS VARYING IN SIZE FROM 21 TO 58 CHARACTERS
DEPENDING ON WS-DAYTRAN-LENGTH
BLOCK CONTAINS 512 CHARACTERS.

You would need to define WS-DAYTRAN-LENGTH in the working-storage section as
an unsigned numeric variable. The length of the record would be placed there
following a successful READ or RETURN statement. You would place the
explicit length to write in WS-DAYTRAN-LENGTH before executing a WRITE or
RELEASE statement.

This method works in IBM VS COBOL II and higher, and also in CA-Realia COBOL
4.2 and higher.

There are other ways to figure out the length of a record, but they are more
complicated than this. I hope it helps.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Multi-Level FD in RM-COBOL

- **From:** "ta..." <ua-author-17071811@usenetarchives.gap>
- **Date:** 1996-12-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e74fe8ec2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`
- **References:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`

```


DAYTRAN-RECORD-2, DAYTRAN-RECORD-3 and DAYTRAN-LABEL
contain a FILLER PIC X(9) as first field. This Filler is DAYTRAN-KEY.
Just ask for the value of DAYTRAN-KEY, i.e:
IF DTC = ZERO (then I use DAYTRAN-RECORD-1)
IF DTC = 2 (then I use DATRAN-RECORD-2)
etc.
(If you can, change this file to fixed length records)

tasio.
```

#### ↳ Re: Multi-Level FD in RM-COBOL

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-12-16T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e74fe8ec2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`
- **References:** `<01bbebbc$93e666f0$b9867fc0@wmyeung>`

```

In message <<01bbebbc$93e666f0$b9867fc0@wmyeung>> "wmyeung" writes:
› 
› 005600     02  DAYTRAN-KEY.
…[9 more quoted lines elided]…
› type of FD 01 created. 

I would hazard a guess that DFMT means Daily-Transaction-Format
and is the record type indicator. But then DCRT may mean
DayTran-Csomething-Record-Type.

I hate it when people use obscure codes for field names and
then add comments because it is not quite obvious what the
names mean, or even worse they then *don't* add comments.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
