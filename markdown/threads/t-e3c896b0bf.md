[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus v4.1 & Oracle (on AIX) - Cannot run the program

_1 message · 1 participant · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### MicroFocus v4.1 & Oracle (on AIX) - Cannot run the program

- **From:** Aspi Engineer <aspi_engineer@striderite.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36911372.B9EAE9B3@striderite.com>`

```
Hi All,

We are currently running Microfocus COBOL V4.0, revision 005 on AIX
v4.2.1. This works fine. However when we made a migration to Microfocus
COBOL v4.1, revision 005 on the same AIX platform, I am unable to create
an executable that works. The executable has embedded SQL and the DBMS
is ORACLE 8.0.5.

Simple COBOL programs (no SQL) work fine, however Pro*COBOL files just
abort when it encounters the SQL CONNECT call, with no error messages at
all.

If I copy the Oracle provided "rtsora" as "$COBDIR/rts32", even the
compile fails with the error message
Load error : file 'clmf_get_tty'
error code: 173, pc=0, call=4, seg=0
173     Called program file not found in drive/directory

Any suggestions,

Thx,
Aspi
aspi_engineer@striderite.com


PS: Does anyone have any instructions for creating an RTS on AIX which
is MQSeries and Oracle enabled. If yes, then please send it to me.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
