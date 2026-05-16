[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Length of Dynamic SQL string in COBOL pgm

_3 messages · 3 participants · 1998-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Databases and SQL`](../topics.md#databases)

---

### Length of Dynamic SQL string in COBOL pgm

- **From:** "Blair McDonald" <bmcdonald@qquest.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** bit.listserv.db2-l,comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<70ktp6$4l4$1@news0-alterdial.uu.net>`

```
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

#### ↳ Re: Length of Dynamic SQL string in COBOL pgm

- **From:** "Ed Zell" <ewzell@imonline.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** bit.listserv.db2-l,comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<70l5nr$ii6$1@sol.pdnt.net>`
- **References:** `<70ktp6$4l4$1@news0-alterdial.uu.net>`

```
>I can't believe that there's no way for me to build an SQL statement over
>254 characters and dynamically execute it. Can anyone give me a hint about
…[4 more quoted lines elided]…
>


Hi Blair,

  I can't speak for DB/2 OS/390, but on DB/2 for VM and VSE, we do this
  all the time.  Here is a bit of code from one of our COBOL programs:


 01  DYNAMICSQL.
     49  DYNAMIC-SELECT-LENGTH   PIC S9(4)  COMP VALUE +300.
     49  DYNAMIC-SELECT-DATA        PIC X(300).


............................................................................
.......................


        MOVE 'PREPARE   ' TO SQL-EYECATCH.
        EXEC SQL PREPARE ALPHASELECT
                 FROM :DYNAMICSQL
                 END-EXEC.

        IF SQLCODE NOT = ZERO
           PERFORM 9999-UNEXPECTED-SQL-ERROR.


  I also check several other programs, and in one of them we use 1500
characters
  for the host variable used in the prepare.  Must be something else that is
wrong
  because my manuals say 8k is the max size of the SQL statement to be
prepped.


Ed Zell
Illinois Mutual Life
ewzell@imonline.com
```

#### ↳ Re: Length of Dynamic SQL string in COBOL pgm

- **From:** "Svein Gr���e" <graee@online.no>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** bit.listserv.db2-l,comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<70l5v5$bct$1@readme.online.no>`
- **References:** `<70ktp6$4l4$1@news0-alterdial.uu.net>`

```
Try this definition of your variable contaning the statement.

       01 selstmt.
           49 selstmt-length     pic s9(4) comp-5 value 0.
           49 stmt                     pic x(2000).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
