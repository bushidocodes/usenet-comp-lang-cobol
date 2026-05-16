[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Determingin LE Runtime options currently in force

_4 messages · 4 participants · 1999-06_

---

### Determingin LE Runtime options currently in force

- **From:** "Ian Reid" <reid.ian@pmintl.ch>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** bit.listserv.cics-l,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<01beb713$e8ef6fa0$3000810a@pmecheew0267>`

```
Hello all,

I'm in a bit of a fix - 

Does anyone have a utility to *list* the current default LE runtime options
in use on a 
CICS system  ?

Also, what about a utility that will list any LE runtime options compiled
into CICS or 
Batch programs ?

Here's hoping

Ian Reid 
```

#### ↳ Re: Determingin LE Runtime options currently in force

- **From:** willjamu@mindspring.com (James A. Williams)
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** bit.listserv.cics-l,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<37662864.382114050@news.mindspring.com>`
- **References:** `<01beb713$e8ef6fa0$3000810a@pmecheew0267>`

```
"Ian Reid" <reid.ian@pmintl.ch> wrote:

IPCS has a VERBX called LEDATA that you can use if you have a dump.

For CICS its IP VERBX LEDATA  'CAA(XXXXXX) ALL'  I believe where
XXXXXX is from REG12 and has a valid CEECAA eye catcher. In batch you
have the RPTOPTS(ON) option that you can use. For batch you can also
specify LEDATA and the CAA is found automatically. IBM has said they
may create a CICS transaction to get the options in the future. If you
go to the LE www site there is a PDF file on debugging LE
applications.
>Hello all,
>
…[16 more quoted lines elided]…
>the same taken as individuals or companies
```

#### ↳ Re: Determingin LE Runtime options currently in force

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** bit.listserv.cics-l,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<7k5id4$l7m$1@nnrp1.deja.com>`
- **References:** `<01beb713$e8ef6fa0$3000810a@pmecheew0267>`

```
In article <01beb713$e8ef6fa0$3000810a@pmecheew0267>,
  "Ian Reid" <reid.ian@pmintl.ch> wrote:
> Hello all,
>
…[10 more quoted lines elided]…
> Ian Reid

AFAIK, there is no utility, but you can create your own options-module
and link it to an existing and running program. That options-module has
just one statement: RPTOPTS=ON. You the run the program and have a look
at the output:

In batch and IMS/TM, look at DD-name SYSOUT. If SYSOUT is not coded in
JCL, the file is allocated dynamically to SYSOUT=*.

In CICS, the report is written to transient data queue CESE. It is
prefixed with terminal-name, transaction-name and the current
timestamp, it may look like:

AE72AM02 19990615143232 Installation default      ABPERC(NONE)
AE72AM02 19990615143232 Installation default      ABTERMENC(ABEND)
AE72AM02 19990615143232 Installation default    NOAIXBLD
.....

You can use the following JCL to create a options-module into a
'&&-file' and link it to the application. You may need to change every
line marked with '+++++'. And... don't forget to replace the CEEUOPT if
you don't need the report anymore!

//* assemble the options-module:
//STEP1 EXEC PGM=ASMA90,PARM='DECK,NOOBJECT'
//SYSPRINT DD SYSOUT=*
//SYSUT1 DD UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT2 DD UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT3 DD UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSPUNCH DD DSN=&&TEMPOBJ(CEEUOPT),DISP=(,PASS),UNIT=SYSDA,
// SPACE=(TRK,(1,1,1)),DCB=(BLKSIZE=3120,LRECL=80,DSORG=PO)
//SYSLIB DD DSN=SCEE.SCEEMAC,DISP=SHR               +++++
//       DD DSN=SYS1.MACLIB,DISP=SHR                +++++
//SYSIN DD *
CEEUOPT  CSECT
CEEUOPT  AMODE ANY
CEEUOPT  RMODE ANY
         CEEXOPT RPTOPTS=(ON)
         END
/*
//  IF RC <= 4 THEN
//* link the options-module to the existing main-program
//STEP2    EXEC  PGM=IEWL,
//         PARM='NCAL,RENT,LIST,XREF,LET,MAP,SIZE=(9999K,96K)'
//SYSPRINT DD  SYSOUT=*
//SYSUT1   DD  UNIT=SYSDA,SPACE=(TRK,(5,5))
//SYSLMOD  DD  DSNAME=>>yourloadlib>>,DISP=SHR      +++++
//SYSLIB   DD  DSN=&&TEMPOBJ,DISP=(OLD,PASS)
//SYSLIN   DD  *
 REPLACE CEEUOPT
 INCLUDE SYSLMOD(>>yourmodule<<)                    +++++
 INCLUDE SYSLIB(CEEUOPT)
 ENTRY >>yourentry<<                                +++++
 NAME >>yourmodule<<(R)                             +++++
// ENDIF
```

##### ↳ ↳ Re: Determingin LE Runtime options currently in force

- **From:** "Dave" <saltaire@ix.netcom.com>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** bit.listserv.cics-l,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<7kif6n$ii0@dfw-ixnews3.ix.netcom.com>`
- **References:** `<01beb713$e8ef6fa0$3000810a@pmecheew0267> <7k5id4$l7m$1@nnrp1.deja.com>`

```
My notes on the subject are at work, but as I recall I used a simpler method
to list LE options in effect - at least for batch, not CICS.
I wrote a COBOL program which did nothing but a STOP RUN in the PROCEDURE
DIVISION. Ie,
   PROCEDURE DIVISION.
   STOP RUN.
Then I executed it and included LE runtime parameters in the EXEC card:
  //RUN        EXEC PGM=DUMPROG,PARM='/RPTOPTS(ON)'
  //STEPLIB  DD  DSN=MYLIB,DISP=SHR
  //               DD  DSN=CEE.SCEERUN,DISP=SHR       LE RUNTIME LIB
  //SYSOUT  DD SYSOUT=*
  //

This gave me a listing of the LE runtime options in SYSOUT.

Dave Morton
marspyrs@aol.com  (<== the only Email location I check)

Daniel Jacot wrote in message <7k5id4$l7m$1@nnrp1.deja.com>...
>In article <01beb713$e8ef6fa0$3000810a@pmecheew0267>,
>  "Ian Reid" <reid.ian@pmintl.ch> wrote:
…[77 more quoted lines elided]…
>Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
