[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# address exception in Windows in OpenCobol attempting to commit to DB2 database

_2 messages · 2 participants · 2010-10_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source) · [`Databases and SQL`](../topics.md#databases)

---

### address exception in Windows in OpenCobol attempting to commit to DB2 database

- **From:** William Lightner <user@compgroups.net/>
- **Date:** 2010-10-14T00:00:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8-dnbjybrP_EyvRnZ2dnUVZ_sSdnZ2d@giganews.com>`

```
OpenCobol 1.0

At least a couple queries (including an update) succeed before the error.

Precompile script:
SET P1=ACTION REPLACE 
SET P2=BINDFILE
SET P3=PACKAGE USING JBHBAT
SET P4=TARGET ANSI_COBOL
SET P5=OWNER ALIUPDT
SET P6=EXPLAIN YES
SET P7=STRDEL APOSTROPHE
SET P8=DISCONNECT EXPLICIT
SET P9=ISOLATION CS
SET PA=RELEASE COMMIT
SET PB=SYNCPOINT NONE
SET PC=VALIDATE BIND

SET OPTIONS=%P1% %P2% %P3% %P4% %P5% %P6% %P7% %P8% %P9% %PA% %PB% %PC%

DB2 PRECOMPILE %1 %OPTIONS%

OpenCobol compiler options:
-cx -fimplicit-init -fdebugging-line -fstack-check -fstatic-linkage -fdebug -fstatic-call
```

#### ↳ Re: address exception in Windows in OpenCobol attempting to commit to DB2 database

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-15T06:05:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8horioFhl5U1@mid.individual.net>`
- **References:** `<a8-dnbjybrP_EyvRnZ2dnUVZ_sSdnZ2d@giganews.com>`

```
William Lightner wrote:
> OpenCobol 1.0
>
…[24 more quoted lines elided]…
> -fdebug -fstatic-call

Specifying the Isolation level to be CS (Cursor stability) means that all 
reads are with lock (Committed Read).  This may be conflicting with a 
previous lock (you said you had done an update).

Was the update to a row that will be returned by the cursor? Did you specify 
WITH LOCK before getting it? Check for a row that is known to the cursor or 
will be part of the set fetched by the cursor, and is also being accessed 
independently of the cursor.

The problem is more likely to be with DB2 than with Open COBOL in this 
instance.

Is there transactional processing going on with the cursor?

Did the problem occur on a COMMIT (explicit) or was it on a different 
operation (implicit COMMIT)?

Need much more information to be of help here.

If it were me I'd try a synch point of say, 10 records and see if the 
problem recurs...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
