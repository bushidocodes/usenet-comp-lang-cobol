[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hello, My name is Vladimir

_3 messages · 3 participants · 1998-02_

---

### Hello, My name is Vladimir

- **From:** "vladimir borovicka" <ua-author-17075331@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34EFC6B6.BFB32B37@hotmail.com>`

```

//VLADIMIR JOB C606,'Hello, My name is Vladimir',
// CLASS=A,NOTIFY=UNT6786,MSGCLASS=H,MSGLEVEL=(0,0)
/*JOBPARM TIME=1,LINES=3
/*ROUTE PRINT HOLD
//***************************************************
//STEP1 EXEC COB2GENER
//SYSIN DD DSN=HELLO.COBOL,DISP=SHR
//GO.OLD DD DSN=HELLO.OLD.DATA,DISP=OLD
//GO.NEW DD DSN=HELLO.NEW,DATA,DISP=(NEW,CATLG,DELETE),
// UNIT=IERGTN,SPACE=(CYL,(8),RLSE),DCB=(LRECL=80,RECFM=VB)
//GO.SYSPRINT DD SYSOUT=*
//***************************************************
//STEP2 EXEC PGM=IEBGENER,COND=(8,GE,STEP1)
//SYSPRINT DD SYSOUT=*
//SYSUT1 DD DSN=VLADIMIR.HELLO.NEW.DATA,DISP=SHR
//SYSUT2 DD SYSOUT=*
//SYSIN DD DUMMY
//
```

#### ↳ Re: Hello, My name is Vladimir

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d18fdedb55-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34EFC6B6.BFB32B37@hotmail.com>`
- **References:** `<34EFC6B6.BFB32B37@hotmail.com>`

```

Vladimir Borovicka wrote in message <34E··.@hot··l.com>...
› //VLADIMIR  JOB C606,'Hello, My name is Vladimir',
› //  CLASS=A,NOTIFY=UNT6786,MSGCLASS=H,MSGLEVEL=(0,0)
…[15 more quoted lines elided]…
› //

Vladimir Borovicka?? Can you please restate THAT in something worth the
while, like VSE JCL or DCL or, even, CL... not all of us are into them weird
MVS "//" things...
```

#### ↳ Re: Hello, My name is Vladimir

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-02-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d18fdedb55-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34EFC6B6.BFB32B37@hotmail.com>`
- **References:** `<34EFC6B6.BFB32B37@hotmail.com>`

```

Vladimir Borovicka wrote:
› 
› //VLADIMIR  JOB C606,'Hello, My name is Vladimir',
…[16 more quoted lines elided]…
› //

Vladimir,

Sorry folk, your job ABENDed and got the following message after the
submit,

IAT6108 JOB VLADIMIR (JOB12345) ENDED, COMP CD=S222|U0000 CN(INTERNAL)
IAT6108 JOB VLADIMIR STEP=STEP1 ,PROC=NONE CN(INTERNAL)
IAT6108 JOB VLADIMIR (JOB12345) CANCELLED BY OPERATOR CN(INTERNAL)
IAT6108 JOB VLADIMIR (JOB12345) SECURITY VIOLATION TO SUBMIT JUNK MAIL
TO COMP.LANG.COBOL
***

Rgds,
Chip Ling
chi··.@sym··o.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
