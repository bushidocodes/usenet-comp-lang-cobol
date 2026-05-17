[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-COBOL Question - DB2 & MTS

_2 messages · 2 participants · 1995-02 → 1995-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### MF-COBOL Question - DB2 & MTS

- **From:** "dbsb..." <ua-author-16946849@usenetarchives.gap>
- **Date:** 1995-02-22T01:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ielgh$84d@raffles.technet.sg>`

```

I'm having some difficulty compiling a DB2-CICS/COBOL program which
I am downsizing from MVS-DB2-CICS/COBOL-II to Microfocus MTS.

I'm running DB2/6000 with MF-Toolbox and Transaction System for AIX.
Compiling DB2 batch programs work fine, as well as compiling CICS
programs.

However, when I try to compile a DB2-CICS program, first with the
native 'dfhdev' utility that comes with MTS, I get an error that says
no compiler 'SQL' directive available. I've then tried compiling with:

cob -P -u -C "SQL SQLBIND() SQLDB(dbname)
CICS DIR($TXDIR/files/sys/tx!gnt.dir)"

which gave me the message 'SQL Precompiler not active' when it encountered
EXEC SQL statements in the procedure division. EXEC SQL INCLUDE in
data division was however correctly included.

Does anyone have an idea to what I've done wrong ?
```

#### ↳ Re: MF-COBOL Question - DB2 & MTS

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-03-06T09:39:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ef3cf592bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3ielgh$84d@raffles.technet.sg>`
- **References:** `<3ielgh$84d@raffles.technet.sg>`

```
dbs··.@tec··t.sg (Linus Tham) wrote:
› 
› 
…[19 more quoted lines elided]…
› 

Linus, I've been given this response to pass on to you (the delay was
my news server down not the response):

The error message of "no SQL preprocessor active" is generated when the
preprocessor encounters a SQL statement and has not been told to invoke
the appropriate SQL preprocessor. In DFHDEV, you must set the SQL Support
tag to 'Y'.
DB2/6000.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
