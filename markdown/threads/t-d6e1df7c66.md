[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus ignoring initcall when using cobsql?

_2 messages · 2 participants · 2004-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus ignoring initcall when using cobsql?

- **From:** psacha@web.de (Philipp Sacha)
- **Date:** 2004-02-04T05:37:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53a9c2bd.0402040537.44fc2436@posting.google.com>`

```
Hi,

i am trying to access an oracle 9i database from mf cobol. I have
created the shared library and tried to use with initcall"rdbmslib"
but the initcall statement seemed to be ignored:

cob -v -C 'INITCALL"rdbmslib" preprocess(cobsql) CSQLT=ORACLE' -o
sqltest1.o -k sqltest1.cbl
cob32 -C nolist -v -C INITCALL"rdbmslib" preprocess(cobsql)
CSQLT=ORACLE -o sqltest1.o -k sqltest1.cbl
* Micro Focus Server Express         V4.0 revision 000          
Compiler
* Copyright (C) 1984-2003 Micro Focus International Ltd. URN
RXCTZ/AA0/00000L
* Accepted - verbose
* Accepted - nolist
* Accepted - INITCALL"rdbmslib"
* Accepted - preprocess(cobsql) CSQLT(ORACLE)

* Micro Focus COBSQL Integrated Preprocessor with ASCII/EBCDIC Support
* Version 1.2.37 Copyright (C) 1993-1999 Micro Focus International
Ltd.
* URN AAAPA/ZZ0/00065
* Compiling sqltest1.cbl
* CSQL-I-006: Rejected CSQLT(ORACLE)
* CSQL-I-003: COBSQLTYPE is incorrect defaulting to Oracle
* CSQL-I-018: Invoking ORACLE8 Precompiler/Translator
* CSQL-I-020: Processing output of ORACLE8 Precompiler
* CSQL-I-001: Cobsql has finished returning to the Checker
* Total Messages:     0
* Data:        1104     Code:         752


When i do a nm to the resulting sqltest1.o i see that a lot of symbols
are missing:

nm sqltest1.o
         U SQLADR
         U SQLBEX
00000000 T SQLTEST1
         U _mFgAE
         U _mFgF805
         U _mFgF806
         U _mFginitdat
         U _mFgprogchain
         U _mFgprogcheckexit
         U _mFgprogunchain
         U _mFgtypecheck
         U _mFldhandle
         U realbncoblib
00000000 T sqltest1


Even when giving an inexistent file to initcall like initcall"foo" the
compiler says that it accepts it.

Any hints?

Regards
Philipp Sacha
```

#### ↳ Re: Microfocus ignoring initcall when using cobsql?

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2004-02-04T14:10:26
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvr0u8$mbg$1@hyperion.microfocus.com>`
- **References:** `<53a9c2bd.0402040537.44fc2436@posting.google.com>`

```
Hi Philipp.

From a quick glance at the command-line you've used :

cob -v -C 'INITCALL"rdbmslib" preprocess(cobsql) CSQLT=ORACLE' -o
sqltest1.o -k sqltest1.cbl

You are, by default, creating an int code module. If you really intend to
create an object file, you must pass -xc to the cob command line.

The INITCALL directive will effectively force a load of "rdbmslib" at
execution-time, rather than at compile-time, so a non-existant file will
only be detected when you execute your application.

In addition, to pass CSQLT=ORACLE from the cob command line, you must
specify == rather than =, as the shell may misinterpret the equals sign.

Hope this helps.

SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
