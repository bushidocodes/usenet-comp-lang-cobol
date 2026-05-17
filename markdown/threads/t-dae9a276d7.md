[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP : VISUALAGE FOR COBOL/ODBC

_1 message · 1 participant · 1997-07_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### HELP : VISUALAGE FOR COBOL/ODBC

- **From:** "glo..." <ua-author-17072784@usenetarchives.gap>
- **Date:** 1997-07-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33d23452.209173926@news.innet.be>`

```

I'm currently evaluating IBMs Visualage for COBOL ver 2 on W 95 and
W/NT.

I try to compile and link the IBM short ODBC sample with the following
result.

E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLERROR@32" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "__cobentry@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLFREEENV@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLCONNECT@28" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLALLOCENV@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLFREESTMT@8" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLALLOCSTMT@8" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLDISCONNECT@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_IWZODBCLICINFO@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLFREECONNECT@4" : unresolved external
E:¥IBMCOBW¥SAMPLES¥ODBC¥odbcsamp.obj(e:¥ibmcobw¥samples¥odbc¥odbcsamp.cbl)
: error LNK2029: "_SQLALLOCCONNECT@8" : unresolved external

ODBC32.LIB is in the current directory with all the references.

Anyone got any ideas?

Claude
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
