[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Oracle - Embedded SQL - WHERE Clause Failure

_1 message · 1 participant · 1998-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Oracle - Embedded SQL - WHERE Clause Failure

- **From:** "dps..." <ua-author-17084483@usenetarchives.gap>
- **Date:** 1998-07-31T16:16:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pt8ms$dq5$1@nnrp1.dejanews.com>`

```
We are attempting to update a couple of columns within a table from a host
array that has been loaded from the same table, and then updated. The WHERE
clause is seeking to match the rows WHERE A = :B -- A is a column in the table
defined at CHAR(4) and :B is a host variable defined as PIC X(4). At the
current time, all rows in the table have column A set to 'ABC ' (4th character
is a space). All :B entries in the host variable array are set to 'ABC '.
When the precompiler modes is set to ORACLE, no matches are found. When the
mode is set to ANSI, the matches are found. Unfortunately, we can't use the
ANSI option because of other considerations.

We are on Oracle Pro*Cobol precompiler version 1.7, but Oracle tells us there
was a problem with version 1.5 where the compiler converted the host variable
to VARCHAR2 before the comparison and used a non-blank padded technique to
compare against the CHAR field. This results in no match being found.
However this same problem isn't supposed to be found the 1.7. Oracle
suggested and we tried to use the EXEC SQL VAR B IS CHARF(4000) END-EXEC (4
characters x 1000 entries), but this hasn't worked either (we've also tried
CHAR instead of CHARF).

We did do a RPAD(:B,4) in the WHERE clause, and this works, so it obviously
has something to do with the 4th character failing the comparison when
MODE=ORACLE and working with MODE=ANSI.

The real SQL is as follows:

UPDATE EMPBPLAN
SET ELIG_CODE = :UPD-EMPBPLAN-ELIG-CODE,
ELIG_DATE =
TO_DATE(:UPD-EMPBPLAN-ELIG-DATE,'YYYYMMDD')
WHERE PERSON_ID = :UPD-EMPBPLAN-PERSON-ID
AND COMPANY = :UPD-EMPBPLAN-COMPANY
AND BPLAN_CODE = :UPD-EMPBPLAN-BPLAN-CODE
AND TYPE_CODE = :UPD-EMPBPLAN-TYPE-CODE

The :UPD-EMPBPLAN-COMPANY is the host varible giving us the problem.

Any ideas or help would sincerely be appreciated!!

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
