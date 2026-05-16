[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cob: errors in assembling

_2 messages · 2 participants · 1999-09_

---

### cob: errors in assembling

- **From:** "Geert Soenen" <gsoenen@infosoft.be>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s59g6$d7m$1@news3.Belgium.EU.net>`

```
Hello;

We have MF-Cobol V3.2 running on AIX V4.3. When compiling our cobol programs
with the '-c' option to product object (.O) modules, we always get the
following strange error message:

$ cob -cx INTERF.cbl
* Micro Focus COBOL for UNIX         V3.2 revision 020 Compiler
* Copyright (C) 1984-1994 Micro Focus Ltd.     URN 2XCLY/ZZ0/00000C
* Accepted - verbose
* Accepted - osvs
* Compiling INTERF.cbl
* Total Messages:     0
* Data:        1744     Code:        1442
Assembler:
/tmp/cob19794/INTERF.s: line 52: 1252-142 Syntax error.
cob: error(s) in assembling /tmp/cob19794/INTERF.s

Can anyone help me on this???

Bye
Geert Soenen
```

#### ↳ Re: cob: errors in assembling

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s874l$f1h$1@nnrp1.deja.com>`
- **References:** `<7s59g6$d7m$1@news3.Belgium.EU.net>`

```
In article <7s59g6$d7m$1@news3.Belgium.EU.net>,
  "Geert Soenen" <gsoenen@infosoft.be> wrote:
> Hello;
>
> We have MF-Cobol V3.2 running on AIX V4.3. When compiling our cobol
programs
> with the '-c' option to product object (.O) modules, we always get the
> following strange error message:
…[18 more quoted lines elided]…
>
(Just a guess as I don't have access to the documentation anymore).
There is a reference w/in the program which is valid within COBOL (for
example: CALL x) through compilation but which is unresolved at the
point of producing the .O  Been a while but check "Dynamic"(?) in your
MF Doc index.
-trblshtr-
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
