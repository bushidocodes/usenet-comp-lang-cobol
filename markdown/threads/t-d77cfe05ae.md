[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating PDS members from a batch program

_5 messages · 5 participants · 1998-10_

---

### Creating PDS members from a batch program

- **From:** don_weigend@email.com (Donald Weigend)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103_907704975@hen.arinet.com>`

```
Greetings All,

Does anyone have any COBOL code examples that create members in a PDS as output. I would like to enhance a 
program that generates JCL for several batch jobs. This program currently stores all the JCL together in a single 
sequential file, I then have to split these jobs up manually. I would appreciate any help anyone can give.

Donald Weigend
SPR Inc.
```

#### ↳ Re: Creating PDS members from a batch program

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O1xS1.253$Ex.2816277@storm.twcol.com>`
- **References:** `<1103_907704975@hen.arinet.com>`

```
>Does anyone have any COBOL code examples that create members in a PDS as
output. I would like to enhance a
>program that generates JCL for several batch jobs. This program currently
stores all the JCL together in a single
>sequential file, I then have to split these jobs up manually. I would
appreciate any help anyone can give.


If you wish to do it in REXX batch it would be a simple matter. I have never
done anything like that in COBOL. The REXX would go something like this:

/* REXX */
ARG FLAT_FILE_IN PDS_OUT
"ALLOC FI(JCLIN) DA('"FLAT_FILE"') SHR REUSE"
"EXECIO * DISKR JCLIN (STEM JCLIN.L. FINIS"
"FREE FI(JCLIN)"
"ALLOC FI(JCLOUT) DA('"PDS_OUT"(DUMMY)') SHR REUSE"
DO A=1 TO JCLIN.L.0
    PARSE VALUE JCLIN.L.A WITH PRE'//'JOBNAME' JOB 'SUFF
    JOBNAME=STRIP(JOBNAME)
    IF PRE=''&LENGTH(JOBNAME<=8)&LENGTH(JOBNAME)>0 THEN DO
       "EXECIO 0 DISKW JCLOUT (FINIS"
       "FREE FI(JCLOUT)"
       "ALLOC FI(JCLOUT) DA('"PDS_OUT"("JOBNAME")') SHR REUSE"
    END
    JCLOUT.L.1=JCLIN.L.A
    "EXECIO 1 DISKW JCLOUT (STEM JCLOUT.L."
END
"EXECIO 0 DISKW JCLOUT (FINIS"
"FREE FI(JCLOUT)"
RETURN


This REXX  could be placed in a control card library and could be executed
with JCL like this:

<<<<<standard jobcard>>>>>
//*******************************************************************
//PARMTEST  EXEC PGM=IKJEFT01,
//      PARM=('MAKEMEMS XXX.FLAT.FILE.IN XXX.PDS.OUT')
//SYSEXEC   DD DSN=XXX.CONTROL.LIB,DISP=SHR
//SYSTSPRT  DD SYSOUT=*
//SYSTSIN   DD DUMMY

This will run the REXX contained in XXX.CONTROL.LIB member name MAKEMEMS
passing XXX.FLAT.FILE and XXX.PDS.OUT as the values for the above ARGuments
FLAT_FILE_IN and PDS_OUT. The members created by the REXX will be the
jobnames on the job card statement: //X1234567 JOB .... would create member
X1234567, all lines following the jobcard will be output to that member
until EOF or another jobcard is found.

Hope this helps.
```

#### ↳ Re: Creating PDS members from a batch program

- **From:** nullify@aol.com (Nullify)
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981007174144.15208.00007508@ng144.aol.com>`
- **References:** `<1103_907704975@hen.arinet.com>`

```

Donald,

You can do this with IEBUPDTE, after minor modification to your COBOL source.

Your COBOL program can continue to write multiple output members to a single
sequential file, but you also write an IEBUPDTE control statement before each
member.

You then use the sequential file as SYSIN input to IEBUPDTE, which uses the
control statements and JCL records to create multiple members on the SYSUT2
PDS. The PDS can be new or already in existence. There's an example of this in
the DFSMS Utilities Manual (MVS Utilities as was).

We had a similar requirement ourselves, and this proved to be the ideal
solution.

Julian Smailes
```

#### ↳ Re: Creating PDS members from a batch program

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361F75EF.66DC0A7E@zip.com.au>`
- **References:** `<1103_907704975@hen.arinet.com>`

```
If you have a known number of JCL's then just use separate DD names and
PDS(MEMNAME) on the DD or am I missing something.

IEBCOPY will allow you to 'backup' a PDS into a sequential file and then
'restore' it.  The way it does this is use a special line between each
member.  If you read the manual or do a backup it would be simple to
create the nessecary lines and then run it through IEBCOPY, no special
code and a standard utility.

HTH
Ken

Donald Weigend wrote:
> 
> Greetings All,
…[6 more quoted lines elided]…
> SPR Inc.
```

##### ↳ ↳ Re: Creating PDS members from a batch program

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F0tsDB.411.0.bloor@torfree.net>`
- **References:** `<1103_907704975@hen.arinet.com> <361F75EF.66DC0A7E@zip.com.au>`

```
: Donald Weigend wrote:
: 
: Does anyone have any COBOL code examples that create members in a PDS as
: output. I would like to enhance a
: program that generates JCL for several batch jobs. This program currently
: stores all the JCL together in a single
: sequential file, I then have to split these jobs up manually. I would
: appreciate any help anyone can give.

I think that by using Rexx it will be much easier than through COBOL. 
Rexx will allocate the members and insert your JCL code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
