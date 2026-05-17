[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# !!! URGENT !!! - DLL problem with MicroFocus ESQL

_1 message · 1 participant · 1997-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### !!! URGENT !!! - DLL problem with MicroFocus ESQL

- **From:** "stefan schreyer" <ua-author-16657536@usenetarchives.gap>
- **Date:** 1997-03-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5gmd0j$2u7@news.Informatik.Uni-Oldenburg.DE>`

```

We are porting a big COBOL application (300 Files) to NT. We use one
EXE file 'MENUE.EXE' that calls different DLL files, but on exiting
the EXE file with STOP RUN we get an error so that an application
which calls the EXE file crashes!!! :-(

We see the following error message:
Execution error: file 魹ｽMENUE魹ｽ
Error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 11)

If we do the same with one big EXE file (instead of using DLLs) there
is no error, but this workaround is not acceptable, too big!!!
When using GNT-Files we get no error, too.

We use (MF=MicroFocus):
SQL Server 6.00.121
MF Object COBOL 4.0.16
MF ESQL-Toolkit for MS SQL-Server, version 2.1

Stefan Schreyer, Oldenburg, Germany, Planet Earth
E-Mail: mailto:Ste··.@Inf··g.DE
WWW : http://www.informatik.uni-oldenburg.de/‾shumway
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
