[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCobol - Acu4GL installation Problem

_1 message · 1 participant · 2001-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### AcuCobol - Acu4GL installation Problem

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2001-05-29T17:10:19+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eve59$54g@newshost.fujitsu.com.au>`

```
Hi,

I have contacted our official suppliers about this question but was hoping
for a really quick responce (as I'm already 2 days late delivering my
project!)

I'm hoping someone might have come across the following error when using
Acu4GL for MS SQL (5.1) on MS SQL server 2000 on Windows 2000 Server.

Everything seems to install OK but when I try to run the sql.acu sample
program
I get an error 9D,11.  The trace file displays an error that sp_AcuInit
storted
procedure does not exist.  Checking the database this is true.  It does not
exist
in the database.
Checking ms_inst.cmd (and ms_inst.sql) confirms that the stored procedure
sp_AcuInit
is not attempted to be added to the database. There is no reference anywhere
of sp_AcuInit.

My question is ... how does the stored procedure sp_AcuInit get added to the
database
as the standard installation process (ms_inst.cmd and ms_inst.sql) does not
add it to the
database.  other sp_Acu stored procedures and tables have been added to the
database.

Thanks,

Ray Smith.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
