[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HOW TO GET DATA FROM ONE HOST TO ANOTHER.

_1 message · 1 participant · 1995-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HOW TO GET DATA FROM ONE HOST TO ANOTHER.

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-01-30T19:16:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<17336E4F5...@LMSC5.IS.LMSC.LOCKHEED.COM>`

```
I have read alot about converting data in this new group. I have a
suggestion to get around the various sign conventions. Use
a seperate field for sign when going between hosts. I.E.

01 GOLD-RECORD.
05 GOLD-AMOUNT PIC S9(4) SIGN IS TRAILING SEPERATE.

Which can be seen on the other machine as:
01 GOLD-RECORD.
05 GOLD-AMOUNT PIC 9(4).
05 The-sign-of-our-times PIC X(1).

Where the-sign-of-our-times contains + for positive and - for those
nebobs o' negativism...

This way you won't have to mess with messy ascii to ebcdic problems.



Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
