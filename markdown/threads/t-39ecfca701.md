[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I would like to know how to call a member of PDS from a Cobol program!

_7 messages · 5 participants · 2006-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### I would like to know how to call a member of PDS from a Cobol program!

- **From:** "tenalirama" <tenalirama2005@gmail.com>
- **Date:** 2006-07-11T03:09:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com>`

```
Hello Everyone,
         I have an assembler program that accesses data from a member
of PDS. I would like know if this can be achieved by a Cobol program.
Examples with sample code would be highly appreciated.

Thanks,
tenalirama.
```

#### ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-11T11:48:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xeMsg.63755$fb2.9085@newssvr27.news.prodigy.net>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com>`

```
"tenalirama" <tenalirama2005@gmail.com> wrote in message
news:1152612568.152123.297510@p79g2000cwp.googlegroups.com...
> Hello Everyone,
>          I have an assembler program that accesses data from a member
> of PDS. I would like know if this can be achieved by a Cobol program.
> Examples with sample code would be highly appreciated.

I don't know to what the reference to "call" in your title refers, so can't
help you there.....

.. but as for "accessing data," a member of PDS can be specified as "data"
in JCL easily enough...

SELECT INPUT-FILE... ASSIGN TO THEDATA

//THEDATA    DD DSN=THE.LIBRARY(MEMBER),DISP=...

...but if you really mean you want COBOL code to do what the assembler code
does, the answer is, "probably, but that depends on exactly what it is
doing."

So, are you "calling,"  "data-ing" or "coding?"

MCM
```

##### ↳ ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** "tenalirama" <tenalirama2005@gmail.com>
- **Date:** 2006-07-11T22:58:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152683900.711689.143830@b28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<xeMsg.63755$fb2.9085@newssvr27.news.prodigy.net>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com> <xeMsg.63755$fb2.9085@newssvr27.news.prodigy.net>`

```
I have two concatenated PDS's under one DDNAME in the JCL. The 1st PDS
has 3 members and one of the member data is what is being accessed by
the Assembler program using the entry name of the PDS member and DDNAME
is also hard coded in the Assembler macro. It is loaded to WORKDCB that
is defined as a variable in the assembler program and using variables
in assembler program opening and closing the PDS is performed. I need
to convert the existing assembler program to Cobol and without changing
the JCL as the chain of programs that it calls may be using members of
the PDS.

Michael Mattias wrote:
> "tenalirama" <tenalirama2005@gmail.com> wrote in message
> news:1152612568.152123.297510@p79g2000cwp.googlegroups.com...
…[21 more quoted lines elided]…
> MCM
```

###### ↳ ↳ ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-12T09:36:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e92fqr$r3p$1@reader2.panix.com>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com> <xeMsg.63755$fb2.9085@newssvr27.news.prodigy.net> <1152683900.711689.143830@b28g2000cwb.googlegroups.com>`

```
In article <1152683900.711689.143830@b28g2000cwb.googlegroups.com>,
tenalirama <tenalirama2005@gmail.com> wrote:
>I have two concatenated PDS's under one DDNAME in the JCL. The 1st PDS
>has 3 members and one of the member data is what is being accessed by
…[6 more quoted lines elided]…
>the PDS.

As this seems to be presented, then... does it translate, at present, into 
JCL that looks something like:

//STEP010  EXEC  PGM=ASMPRG
//INFILE   DD    DSN=FIRST.PDS.NAME,DISP=SHR
//         DD    DSN=SCND.PDS.NAME,DISP=SHR

... where FIRST.PDS.NAME contains three members and ASMPRG is hardcoded to 
always use the same one of these three?

DD
```

###### ↳ ↳ ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-12T12:46:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pa6tg.171207$F_3.99128@newssvr29.news.prodigy.net>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com> <xeMsg.63755$fb2.9085@newssvr27.news.prodigy.net> <1152683900.711689.143830@b28g2000cwb.googlegroups.com>`

```
"tenalirama" <tenalirama2005@gmail.com> wrote in message
news:1152683900.711689.143830@b28g2000cwb.googlegroups.com...
> I have two concatenated PDS's under one DDNAME in the JCL. The 1st PDS
> has 3 members and one of the member data is what is being accessed by
…[6 more quoted lines elided]…
> the PDS.

I don't think this is do-able 'as written' . While there probably is 'some
way' to access the directories of the PDSs from a COBOL program, I can
guarantee you it's not with any verbs in your COBOL manual.

But if the only constraint is that the PDS datasets might be used later in
the job, that's no big deal... you can leave them in the job step with the
same DDNAME even if they are not used.

Best guess from Southeast Wisconsin is you will be adding at least one step
to that JCL, even if it is just a couple of IDCAMS/IEBGENER steps to extract
the required members of the PDS into discrete (temporary) datasets upon
which your COBOL program will operate.

I think I'd look at what the current assembler program does now and what it
is required to do (I assume there is some feature to be added or why bother
replacing it?), concentrate on the COBOL program requirements, and deal with
the JCL ramifications only after you have the actual application
specifications.

MCM
```

#### ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2006-07-11T20:09:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<decfc$44b43d8c$4f9c60a$15620@DIALUPUSA.NET>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com>`

```

"tenalirama" <tenalirama2005@gmail.com> wrote in message 
news:1152612568.152123.297510@p79g2000cwp.googlegroups.com...
> Hello Everyone,
>         I have an assembler program that accesses data from a member
…[6 more quoted lines elided]…
>
You can process a  PDS member from a COBOL program as a sequential  dataset 
i.e. via QSAM.

From assembler you can do more things with a PDS via the BPAM access method 
e.g. access the directory of members. Generally you cannot do these same 
things from COBOL as the IBM COBOL compiler does not support BPAM.

There are IBM utilities that can unload members to a sequential dataset that 
you could then process via a COBOL program. Generally it is easier to 
operate on the members with some scripting language such as , TSO CLISTs, 
REXX  execs or ROSCOE RPFs.
```

##### ↳ ↳ Re: I would like to know how to call a member of PDS from a Cobol program!

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-12T20:20:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Qctg.122231$YR4.109787@fe10.news.easynews.com>`
- **References:** `<1152612568.152123.297510@p79g2000cwp.googlegroups.com> <decfc$44b43d8c$4f9c60a$15620@DIALUPUSA.NET>`

```
There are examples on the web of how to "read" a PDS (not PDSE) directory from a 
COBOL program.  (It requires a little "telling COBOL fibs" to get it to work). 
If you then obtain the "member names" you can call such a member via a

   Call identifier

statement.

However, this is NOT something that I would recommend (especially to someone 
asking how to do it in COBOL).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
