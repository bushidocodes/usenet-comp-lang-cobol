[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to read printer report file in COBOL 85?

_2 messages · 2 participants · 1998-02_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### How to read printer report file in COBOL 85?

- **From:** "beard..." <ua-author-2541310@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980225165501.LAA11373@ladder02.news.aol.com>`

```

Hi. I've got an annoying problem. I have a need to read in report files
(variable length lines, cr/lf delimiting at end, occassional form feeds) and
parse data out of the report and produce input files for another system.

I was hoping this would be a straight forward conversion but I can't get the
files to open. My target system is a MicroVAX, and I'm staging my development
on Windows 95 using Fujitsu's compiler. A C license is not available on the
target system so I can't go to that level of access.

Will I be forced to use accept? Or byte at a time assemble a record?

I keep getting open errors with file status 39 (file doesn't match
specification). The Fujitsu runtime reports invalid delimiter error. Joy!

Here's some code snippets:

INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT PLOG-REPORT-FILE ASSIGN TO 'PLOGSHF1.DAT'
ORGANIZATION IS SEQUENTIAL
ACCESS MODE IS SEQUENTIAL
RECORD DELIMITER IS STANDARD-1
FILE STATUS IS RMS-FILE-STAT.
DATA DIVISION.
FILE SECTION.
FD PLOG-REPORT-FILE
LABEL RECORDS ARE STANDARD
RECORD IS VARYING IN SIZE FROM 1 TO 256 CHARACTERS
DEPENDING ON CURRENT-RECORD-SIZE.
01 PLOG-REPORT-RECORD.
05 FILLER PIC X(256).
WORKING-STORAGE SECTION.
01 ASSORTED-MIXED-FIELDS.
05 CURRENT-RECORD-SIZE PIC 9(4) USAGE COMP VALUE 0.
05 RMS-FILE-STAT PIC 99.
05 EOF-SWITCH PIC X VALUE 'N'.

Anyway, HELP!!!!!

Thanks in advance for any help.

Troy.
```

#### ↳ Re: How to read printer report file in COBOL 85?

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6b92db45cc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980225165501.LAA11373@ladder02.news.aol.com>`
- **References:** `<19980225165501.LAA11373@ladder02.news.aol.com>`

```

BeardedEgl wrote:
› 
› Hi. I've got an annoying problem. I have a need to read in report
…[4 more quoted lines elided]…
› system.

Is the other system going to reside on the MicroVAX? Or are you just
wanting to run the conversion on the MicroVAX then move the data? If
so, there may be other means to get at the data you are trying to get
out of the report.

› 
› I was hoping this would be a straight forward conversion but I can't
…[11 more quoted lines elided]…
› Joy!


This is probably one area in which cross development will have no
benefit whatsoever. The environments (VAX/RMS vs Windows/byte stream)
are just too different, and your problem is directly related to the
environment.

The trick is to make the COBOL description match, in all details, the
attributes that RMS is maintaining about the file (especially blocking,
if any, and variable vs fixed record length). I am not enough of a VAX
expert to tell you the RMS command that you should type to get the
attributes, but if you are compiling a COBOL program on the MicroVAX,
you probably know, or can look it up. If you have difficulty
understanding which COBOL clause affects which RMS parameter, you can
experiment with COBOL files by using OPEN OUTPUT.

I could tell you how to do this in RM/COBOL, but that won't do you any
good. I hope this is helpful, and I also hope you receive a better
answer than mine!
Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
