[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol II vs Cobol for MVS and rounding

_5 messages · 4 participants · 1999-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol II vs Cobol for MVS and rounding

- **From:** kthompson@netexas.net (Kevin)
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.net>`

```
We're recompiling a VS Cobol II program under Cobol for MVS on the
mainframe.  The program has the following logic:

COMPUTE FIELD-A ROUNDED = FIELD-B * FIELD-C.

where FIELD-A is PIC S9(7)V99,
FIELD-B is PIC S9(7)V99 with a value of 11.25, and
FIELD-C is PIC 9V9(4) with value of 0.1000

11.25 * .10 = 1.125 so the result should be 1.13

1.13 is the result we get in VS Cobol II
1.12 is the result we get in Cobol for MVS

Has anyone else seen this problem or any documentation on Cobol for
MVS rounded differences??

Cheers,
Kevin
```

#### ↳ Re: Cobol II vs Cobol for MVS and rounding

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798fjs$q8k$1@juliana.sprynet.com>`
- **References:** `<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.net>`

```
Kevin,

    First, compare your compile options. Could you possibly generate and
post the ASSEMBLER expansion for both COBOL's for this COMPUTE so we can
have a look? Use compile options LIST,NOOFFSET. Sounds intriguing....

WOB,
Atlanta

Kevin wrote in message
<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.ne
t>...
>We're recompiling a VS Cobol II program under Cobol for MVS on the
>mainframe.  The program has the following logic:
…[16 more quoted lines elided]…
>Kevin
```

#### ↳ Re: Cobol II vs Cobol for MVS and rounding

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bRRt2.2450$fz.8409516@storm.twcol.com>`
- **References:** `<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.net>`

```
>Has anyone else seen this problem or any documentation on Cobol for
>MVS rounded differences??


Just a geuss, but it may be the TRUNC compiler option. Verify that the same
option is used in both. If different make them the same. If you can't change
them in JCL, override with the PROCESS or CBL statements.

I am geussing the compiler option is truncating the intermediate fields used
by the COMPUTE statement to make them the same as the receiving field
FIELD-A or possibly even FIELD-B.
```

#### ↳ Re: Cobol II vs Cobol for MVS and rounding

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798rco$4hd@dfw-ixnews6.ix.netcom.com>`
- **References:** `<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.net>`

```
You don't show us your full field definitions.  Is there any chance that one
(or more) of them is NOT usage DISPLAY?  (for example COMP?)  If so, then my
guess is that (as pointed out in another post) you may have a difference in
which TRUNC compiler option was used.  HOWEVER, having said that, my
"usually reliable source" told me the following,

"  I just ran this testcase, and I get 1.13 with VS COBOL II R4,
COBOL for MVS & VM, and COBOL for OS/390 & VM."
```

##### ↳ ↳ Re: Cobol II vs Cobol for MVS and rounding

- **From:** kthompson@netexas.net (Kevin)
- **Date:** 1999-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8C39944644CD07E9.CF370F081D1C7015.D2C0289B30F16258@library-proxy.airnews.net>`
- **References:** `<8276434713368D4D.DC0EE79EBD25C065.88BC70B42D1048CA@library-proxy.airnews.net> <798rco$4hd@dfw-ixnews6.ix.netcom.com>`

```
Thanks for the help on the rounded question and I was unaware of the
TRUNC option on the compiler.  I'm spoiled by assuming the system
folks setting compiler options up at installation.   

We found the problem was a production problem with the design of the
client's system.  One of the values is pulled off a DB2 table.  We're
running VS Cob II in one region and Cob For MVS in another region with
duplicate data.  I found we were getting different data.

A select was done on the DB2 table with an "order by" clause but all
the columns in the "order by" were zero.  One system had been re-orged
but not the other - the results may never be duplicated.
Hmmm....wonder how many people have been incorrectly billed over the
years? 

Cheers,
Kevin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
