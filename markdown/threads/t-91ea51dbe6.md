[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Language-Environment Cobol for MVS&VM zOS 1.2?

_3 messages · 3 participants · 2002-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** Andreas Lerch <andreaslerch@t-online.de>
- **Date:** 2002-07-24T18:08:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020724.18084264@04307839700-0001.dialin.t-online>`

```
Hallo,

this is the second time, IBM ist doing something unpleasent changes.

The first, some years ago, verifies the recordlengt at open, 
validating the dcb. If i Code some korrekt rule:

FD Input recording mode v.
01 min-rec pic (200).
01 mac-rec pic x(220).

IBM is checking the dcb for 224 bytes recordlength. This is stupid 
because in MVS you only need a buffer to hold the longest record in 
the dataset. Is the RDW greater 220 bytes, an abend s0c1 occurs. So i 
must change all my JCL to produce the recordlength of 220 bytes?

If i code this in JCL, only for QSAM-Files:

// (IEBGENER-Step)
//SYSUT2 DD DSN=NEWDS,DISP=NEW,DCB=(LRECL=224,RECFM=VB)

// (My -Step)
//INPUT DD 	DSN=NEWDS,DISP=SHR
// 		DSN=ANYDSN,DCB=(LRECL=any-record-length-i want,RECFM=VB)

I can do my work, IBM is only checking the first file, but this 
solution is stupid.

a. VB-Datasets belongs a lot of changetime to increase decres the 
recordlength
b. mild migration, first change the jcl, then change programms are 
impractiable.

The same checking is done to VSAM-Files: Maximum and Average - this is 
the badest check i ever found.

This ist the worst case one.


The second, the modules are all going into the cobpack IGZCPAC. I use 
some programs as subroutines in CICS environment. They are designed:

	If CICS
	then 
	 <perform CICS-part>
	 exec cics read...
	 exec cics write...
	else
	 <perform batch-part>
	 open file
	 read file
	 close file
	end-if

Dokumentation: never use FD OPEN READ CLOSE in a CICS environment. *I 
DO SO*

i have coded this operations but i dont use them in CICS.

Cobol now, is stupid again. The programm-header tells, there will be 
some file-code inside the programm. Flags. LE is loading the modules 
IGZCV** for VSAM-processing, these modules are now inside the cobpack 
- *and will never be used* - where is the batch restriction, that i 
cant use EXEC-CICS in a batch program. Now i must change a 
single-program-logik in a two-program-logik:

	If CICS
	then 
	 <perform CICS-part>
	 exec cics read...
	 exec cics write...
	else
	 <perform batch-part>
	 call suproutine containing batch OPEN,CLOSE,READ and so on
	end-if

thats stupid too.

This ist the worst case two.

These two things are very expensive, because the migration of datasets 
(case 1) must be a dot-landing (german: Punktlandung) all changes must 
be done to the same time. No safe way - step by step and the changing 
of program-logic (case 2), everytime i must change two programms to 
keep the logik korrekt.

Some words in german: das ist frustrierend, so bevormundet zu werden. 
Ich bin ein erwachsener Mensch, der weiss was er macht!

Thank you all to hear my words, I must say this, i thing, now, after 
this, i can sleep well.

The next time, IBM changes something, which surprise comes?????

have a nice day
Andreas
```

#### ↳ Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-25T14:41:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahpk8j$89a$1@slb7.atl.mindspring.net>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online>`

```
First, never try and do a COBOL or an LE "migration" without reading
CAREFULLY the IBM "Migration Guides".  These clearly document what changes
occur.  (and in many cases how to avoid them - such as "odd" file attribute
problems)

Second, the requirement for "fixed file attribute" checking at OPEN time
came from ANSI and ISO - not from IBM.  Complain to the German Standards
body - not IBM.  See:

    Germany (DIN)
    Address        DIN Deutsches Institut f�r Normung
                        Burggrafenstrasse 6
                        DE-10787 Berlin

Postal Address
DE-10772 Berlin

Tel+49 30 26 01-0
Fax+49 30 26 01 12 31
E-mail directorate.international@din.de
Webhttp://www.din.de

   ***

Finally, as to what LE modules are and are not loaded at run-time, Assuming
you are using a "current" compiler (with RES behavior as the default) -
there is no "real" loading of modules at run-time.  If you are experiencing
an unexpected performance problem, contact your IBM support team - as this
should NOT happen.
```

##### ↳ ↳ Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2002-07-27T15:29:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020727.15292772@04307839700-0001.dialin.t-online>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <ahpk8j$89a$1@slb7.atl.mindspring.net>`

```
>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 25.07.02, 19:41:06, schrieb "William M. Klein"
<wmklein@nospam.ix.netcom.com> zum Thema Re: Language-Environment Cobol
for MVS&VM zOS 1.2?:

hello


> First, never try and do a COBOL or an LE "migration" without reading
> CAREFULLY the IBM "Migration Guides".  These clearly document what
changes
> occur.  (and in many cases how to avoid them - such as "odd" file
attribute
> problems)

oh no - never change a running system - thats not the intention i
have.

I want to write good programms to do the work they must do. first i am
online, second batch, third i have ims-databases and then udm.

I can use ims-databases in any system (cics, ims/dc, ims/db) with the
same interface. Dynamic call!

Db2 i mus have different loadmodules - source can be identical, becaus
i have to link different hll-interfaces.

Now i must have different sources to handle the same request in batch
and cics. That is what i want to say.


> Second, the requirement for "fixed file attribute" checking at OPEN
time
> came from ANSI and ISO - not from IBM.  Complain to the German
Standards
> body - not IBM.  See:

for fixed files - i can live whith this test
for variable files - which can this test preserve?

15 years ago i write a programm to handle qsam-files like vsamio (i
you know this product) now i use this programm to convert vb-file from
download to fix files. So i can work with thist handicap.

> Finally, as to what LE modules are and are not loaded at run-time,
Assuming
> you are using a "current" compiler (with RES behavior as the default)
-
> there is no "real" loading of modules at run-time.  If you are
experiencing
> an unexpected performance problem, contact your IBM support team - as
this
> should NOT happen.

I am not shure whats happend. We use the same subprogramms in batch
and in cics dynamic calls and language-environment are good. I can use
callable services like ceeloct in all runtime environments.

Your final point is not easy, our host is served by a supporter who
primary works with assembler and c - he is the connector to ibm, and
it is not his intention to support a language, the dont use often. So
they do with cics. And they dont understand, whats my problem is. They
say: read the manual, if they write you can use, you can use - if they
write not - you cant use it!

My host must support the following:
batch, cics, ims-db, db2, cobol and some assembler also a little rexx

if i say i have a problem with cobol and cics, they say cics, thats
not my world. Cobol, whats that?

Thank you to talk with me - i dont want to change anything, i only
want to know someone else which reaction some actions can start

have a nice day

Andreas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
