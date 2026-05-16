[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Length of Dynamic SQL in COBOL pgm

_2 messages · 2 participants · 1998-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Length of Dynamic SQL in COBOL pgm

- **From:** "Blair McDonald" <bmcdonald@qquest.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** bit.listserv.db2-l,comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<70ku42$527$1@news0-alterdial.uu.net>`

```
Apologies if I've posted twice...

I'm working on developing a COBOL program for OS/390 on DB2 version 5 that
uses dynamic SQL. On the PREPARE statement, I'm getting an SQL error -134,
which implies that my host variable containing the built SQL string is too
long. Messages and Codes says that this error means that the host variable
can't be over 254 characters long.

I can't believe that there's no way for me to build an SQL statement over
254 characters and dynamically execute it. Can anyone give me a hint about
what I might be doing wrong? Could this be some "installation"-set limit
that I'm running into? Has anyone built dynamic SQL that was, say, 1000
characters long?

Please reply here or email me at:
bmcdonald@qquest.com
```

#### ↳ Re:Length of Dynamic SQL in COBOL pgm

- **From:** Duane Lee - ATCX <DLee@mail.maricopa.gov>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44C2247EAFF4D011B0BD00805F85B09C0CBD85CF@news.maricopa.gov>`
- **References:** `<70ku42$527$1@news0-alterdial.uu.net>`

```
It appears you have some other problem.  If you look at Appendix A of
the SQL Reference manual you will see that the limit on an SQL statement
is 32765 bytes (page 467). You need to check your code for some other
possible problem.  A CHAR defined string has a limit of 254 (page 465)
so check your variables.

Good luck.
Duane

> -----Original Message-----
> From:	Blair McDonald [SMTP:bmcdonald@qquest.com]
…[30 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
