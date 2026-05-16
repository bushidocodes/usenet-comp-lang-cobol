[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and uni-SPF - migration to HP-UX

_2 messages · 2 participants · 2005-08 → 2007-10_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### COBOL and uni-SPF - migration to HP-UX

- **From:** "Pedro Machado" <pmm@log.pt>
- **Date:** 2005-08-16T09:55:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124211312.952806.16030@g44g2000cwa.googlegroups.com>`

```
Hi you all,

I'am try to migrate applications write in COBOL language from the IBM
mainframe environment to HP-UX. This aplications use uni-SPF to run.

In one of COBOL programs, is used the "ISPLINK" to compiled language
dialogs use the call format to invoke a dialog management service.

When I compile the COBOL program "teste.pco", I have the following
output:

****************************************************************************
Pro*COBOL: Release 9.2.0.5.0 - Production on Tue Aug 16 17:11:44 2005

Copyright (c) 1982, 2002, Oracle Corporation.  All rights reserved.

System default option values taken from:
/opt/DITIC/oracle/product/9.2.0/precomp/admin/pcbcfg.cfg

Cobol program "ISPLINK" undefined. Assuming it will be dynamically
loaded.
Cobol program "slcdfree" undefined. Assuming it will be dynamically
loaded.
Cobol program "slcdalloc" undefined. Assuming it will be dynamically
loaded.
Cobol program "ISPLINK" undefined. Assuming it will be dynamically
loaded.
Cobol program "slcdfree" undefined. Assuming it will be dynamically
loaded.
Cobol program "slcdalloc" undefined. Assuming it will be dynamically
loaded.
1 seconds
****************************************************************************

This compilation create the file "teste.so".
The "ISPLINK" is not defined when I try to compile the program and this
assuming it will be dynamically loaded, but when I try to run the
program with uni-SPF ("ispf 'PGM(teste)'") nothing happen.

The "ISPLINK" is define in the file "spfPGM.h" and is located in the
"inc" directory of the uni-SPF distribution, and the compiled language
dialogs must include this header file that defines the application
program interface.

I don't know what I have to do, to add this header file in the
compilation of COBOL program, ir order the "ISPLINK" to be recognized
in the compilation.

The file with the directives and options from the compilation files
that I'am to use is the following:
******************************************************************************
# COB MicroFocus
export COBCPY=/usr/local/transform/proj/DITIC/transformedauto/COBCOPY
# the -C nolist was on a cobopt file!...
cob32 -C PERFORM-TYPE=COB370 -C IBMCOMP -C nolist -U -C progid-comment
-C assign=external -C SQL -x -o $2.bin $1.cob -L${ORACLE_HOME}/lib32/
${ORACLE_HOME}/precomp/lib32/cobsqlintf.o -lclntsh `cat
${ORACLE_HOME}/lib32/ldflags`   `cat ${ORACLE_HOME}/lib32/sysliblist`
-lm

# make the .so
cob32 -C PERFORM-TYPE=COB370 -C IBMCOMP -C nolist -C progid-comment -C
assign=external -C SQL -U -g -z $1.cob -L${ORACLE_HOME}/lib32/
${ORACLE_HOME}/precomp/lib32/cobsqlintf.o  `cat
${ORACLE_HOME}/lib32/ldflags`   `cat ${ORACLE_HOME}/lib32/sysliblist`
-lm -lclntsh
*******************************************************************************

Can you help, please?

Best Regards,
Pedro Machado
```

#### ↳ Re: COBOL and uni-SPF - migration to HP-UX

- **From:** "jcfdez" <jcfernan55@yahoo.es>
- **Date:** 2007-10-06T02:48:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6cf02936f666bf5dc64e504d11b12de@localhost.talkaboutprogramming.com>`
- **References:** `<1124211312.952806.16030@g44g2000cwa.googlegroups.com>`

```
I am on the same situation, has any body found a solution ???

Thanks in advance
Juan Carlos
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
