[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL memofields

_1 message · 1 participant · 1994-12_

---

### COBOL memofields

- **From:** "xylo..." <ua-author-921084@usenetarchives.gap>
- **Date:** 1994-12-16T00:05:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cr76i$coc@newsbf01.news.aol.com>`

```
I am using Microsoft COBOL version 4.0 and trying to create a full
screen text field. While I can input to the full length of the text, if
I start to insert and delete characters from the center of the 1600
byte field I begin to lose text. I have been able to do this in BASIC
and in C, but I really need to do this in COBOL. Anybody have any
suggestions?


identification division.
program-id. memofield.
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
DATA DIVISION.
FILE SECTION.
WORKING-STORAGE SECTION.
01 memo-field pic x(1600).
PROCEDURE DIVISION.
Start-up.
display (1, 1) memo-field.
accept (1, 1) memo-field with update.
stop run.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
