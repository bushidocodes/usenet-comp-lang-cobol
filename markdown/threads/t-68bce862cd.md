[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol compile can't locate db2

_1 message · 1 participant · 2000-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Cobol compile can't locate db2

- **From:** iboyes@ibcs.co.nz (Ian Boyes)
- **Date:** 2000-10-21T00:00:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<39f16b14.6927594@news.clear.net.nz>`

```
Hi

I have an AIX 4.3.3 system with ibm cobol using db2 connect 6.1 and
when I try to compile with this command

cob2  -c -x -o AICM020.o -I/app/rptst/db2adm4/sqllib/include/cobol_a
-I/app/rptst/src/copy -I/usr/mqm/inc -qpgmname\(mixed\) -qlib
-q"SQL('database "dsna" COLLECTION "AIX" datetime eur')"  AICM020.cbl

I get an error indicating db2 isn't there like this

 IGYDS0220-S   Unable to locate the DB2 product.  Install the DB2
 product then recompile. All "EXEC SQL" statements will be discarded.


If I use the db2 prep statement and bind it manually, the program
compiles fine. What is it looking for that gives the error?

 I have thousands of lines of code to change so using the bind
manually so it is not an option. The strange thing is all I am doing
is moving from an F50 system to an H80 with (supposedly) the same
versions of all the software. 

The only difference I can see is that the F50 has db2_06_01.xlic
(Extended license support for UDB) installed rather than the H80 which
has db2_06_01.clic (Connect license support). 

Any help would be much appreciated
Ian Boyes
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
