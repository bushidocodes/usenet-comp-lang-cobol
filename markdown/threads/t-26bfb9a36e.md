[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing to Printer IBM PC

_4 messages · 4 participants · 1995-03_

---

### Printing to Printer IBM PC

- **From:** "cvv..." <ua-author-1142103@usenetarchives.gap>
- **Date:** 1995-03-10T23:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`

```
I could print to a file and screen but can't print to my printer. I am a
new student of Cobol so any help would be appreciated.

I have try the following as suggested before but this doesn't work.

Select Print-File
Assign Print "Printer"
Status Print-Stat.

FD Print-File.

01 Prt-Rec PIC X(132).

Like I said any help?
```

#### ↳ Re: Printing to Printer IBM PC

- **From:** "t..." <ua-author-15731627@usenetarchives.gap>
- **Date:** 1995-03-11T12:20:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26bfb9a36e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`
- **References:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`

```
In article <3jr7r2$1c··.@use··y.com>, CVV··.@pro··y.com (Pedro Baez jr) says:
› 
› I could print to a file and screen but can't print to my printer. I am a
…[13 more quoted lines elided]…
› 

I have never seen Assign print "printer". Sounds rather mainframey.
Here is the select that I use:

SELECT PRINT-FILE
ASSIGN TO "LPT1:"
ORGANIZATION IS LINE SEQUENTIAL
FILE STATUS IS PRINT-STAT.

The FD looks fine though.


OPEN OUTPUT PRINT-FILE
MOVE "AAA" TO PRINT-REC
WRITE PRINT-REC
CLOSE PRINT-FILE.

If this doesn't work, post the error message you get.
Your problem might not be with the COBOL but with your printer connection or setup.
```

#### ↳ Re: Printing to Printer IBM PC

- **From:** "georg..." <ua-author-506257@usenetarchives.gap>
- **Date:** 1995-03-11T19:02:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26bfb9a36e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`
- **References:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`

```

Try creating a file, then download and print it.

Be sure to make the file "FB" not "FBA" else you will
see strange results unless its connected/defined to the mainframe.

Also "COPY" & "PASTE" it to the clipboard or a word processor.
I do this one frequently


Good luck

George
======================================================
George Lewycky
GEO··.@a··.com OR
lew··.@a··.org
```

#### ↳ Re: Printing to Printer IBM PC

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-03-15T12:17:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26bfb9a36e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`
- **References:** `<3jr7r2$1c2q@usenetw1.news.prodigy.com>`

```
Pedro Baez jr (CVV··.@pro··y.com) wrote:
: I could print to a file and screen but can't print to my printer. I am a
: new student of Cobol so any help would be appreciated.

: I have try the following as suggested before but this doesn't work.

: Select Print-File
: Assign Print "Printer"
: Status Print-Stat.

: FD Print-File.

: 01 Prt-Rec PIC X(132).

: Like I said any help?

If the above doesn't work, it sounds like a configuration problem. Two areas
need to be looked at. (The original post mentioned a PC environment).

1 - If the MS/DOS command: Copy textfile prn: doesn't output the textfile
onto the printer, then you have a DOS setup problem or hardware problem.

2 - If the above works, check to see if your COBOL uses a configuration file.
If it does, then it may need to be modified.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
