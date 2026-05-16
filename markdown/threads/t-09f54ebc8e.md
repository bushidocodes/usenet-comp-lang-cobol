[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File declarations in the Environment and Data division

_16 messages · 10 participants · 2006-02_

---

### File declarations in the Environment and Data division

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-06T22:13:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9SPFf.181914$km.172504@edtnps89>`

```
Let's say I have a COBOL program like this:

IDENTIFICATION DIVISION.
PROGRAM-ID. Test.
AUTHOR: Oliver Wong.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
  SELECT FileA ASSIGN "FileA.dat"
    ORGANIZATION IS LINE SEQUENTIAL
    ACCESS MODE IS SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD FileA.
01 RecordA.
  88 EndOfFileA VALUE HIGH VALUES.
  02 RecordID   PIC X(7).
  02 Contents   PIC X(23)

PROCEDURE DIVISION.
BEGIN
  OPEN INPUT FileA
* etc.

    I'm assuming the fact that the "FileA" in the SELECT clause of the 
FILE-CONTROL paragraph matches the "FileA" in the file description entry in 
the FILE section is significant (as opposed to coincidental), and that these 
two things are "linked" somehow.

    Are either of these things optional? That is to say, would it be 
meaningful to have "FileA" mentioned in the file description entry and not 
in the SELECT clause, or vice versa? If so, what kind of "defaults" would 
the compiler typically assume for such an ommision?

    - Oliver
```

#### ↳ Re: File declarations in the Environment and Data division

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-02-06T16:23:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ufj3eqc24o2a9@news.supernews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89>`

```
Oliver Wong wrote:
> Let's say I have a COBOL program like this:
>
…[27 more quoted lines elided]…
> coincidental), and that these two things are "linked" somehow.

Correct.

>
>    Are either of these things optional?

No.

> That is to say, would it be
> meaningful to have "FileA" mentioned in the file description entry
> and not in the SELECT clause, or vice versa? If so, what kind of
> "defaults" would the compiler typically assume for such an ommision?

Absent either, the compiler would default to an error message.
```

##### ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-06T14:39:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ds8j68$ho$1@si05.rsvl.unisys.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <11ufj3eqc24o2a9@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:11ufj3eqc24o2a9@news.supernews.com...
> Oliver Wong wrote:
>> Let's say I have a COBOL program like this:
…[42 more quoted lines elided]…
> Absent either, the compiler would default to an error message.

I'd go one step further.  Given that "For each file-name specified in a 
SELECT clause, there shall be a file description entry or a sort-merge 
description entry in the file section of ... the program in which the SELECT 
clause is specified" can be found in ISO/IEC 1989:2002, and given that every 
standard for COBOL as far back as I can determine has had similar wording, I 
would suggest that a compiler that did anything *but* complain loudly if 
either SELECT or FD was missing for a given file-name would be violating a 
rule that has been fundamental to COBOL for close to half a century, if not 
longer.

Stated a different way, there are languages that do not require that there 
be both a SELECT and an FD/SD, and that there be a one-to-one correspondence 
between each SELECT and one, and only one, FD/SD.

Such languages are not readily-recognizable dialects of what reasonably 
might be called "COBOL".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-07T01:36:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UQSFf.86547$Mg.43980@fe01.news.easynews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <11ufj3eqc24o2a9@news.supernews.com> <ds8j68$ho$1@si05.rsvl.unisys.com>`

```
I believe (but won't swear to it) that I *have* seen an extension that allows 
the Select/Assign (Environment Division) entry to be omitted for an SD (not an 
FD).  I *know* have seen implementations where the value in the ASSIGN clause of 
the Select/Assign statement for an SD is "ignored" (i.e. has no relationship to 
any "physical" sort-merge file).

Obviously, I agree with Chuck's statements about what the current, past, and 
proposed STANDARDS require.
```

##### ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2006-02-07T19:29:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LMbGf.61$na4.18@fe07.lga>`
- **In-Reply-To:** `<11ufj3eqc24o2a9@news.supernews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <11ufj3eqc24o2a9@news.supernews.com>`

```
HeyBub wrote:
> Oliver Wong wrote:
> 
…[50 more quoted lines elided]…
> 
I think when you say "access mode is sequential" that that is the 
default and is not necessary.  I never use line sequential, but I have 
some examples in a little binder on my desk.  Usually when you say line 
sequential it means a line-return is at the end of each record.

When you say select xyz assign to "", xyz is the programmer assigned key 
word that you use to describe the file.  So you have to use that for the 
  FD because you just told the compiler you were going to use it.  If 
you dont use it and use something else you will get two errors.  You 
will get an error for having an assign clause and not referrring to the 
file and you may get an error for using an FD with no assign clause. 
Plus every field in your file description will get an error also.  Then 
every time you refer to the fields in the procedure division it will be 
like the fields do not exist.  Everything is connected.  The select 
statement has to do with what device has the file, and the FD is the 
Logical description of the file.  If the select statement is wrong you 
can get hundredes of errors in a program.
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-02-08T12:02:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D5lGf.23037$Jd.8070@newssvr25.news.prodigy.net>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <11ufj3eqc24o2a9@news.supernews.com> <LMbGf.61$na4.18@fe07.lga>`

```
"Last Boy Scout" <eggbtr@ezl.com> wrote in message
news:LMbGf.61$na4.18@fe07.lga...
> HeyBub wrote:
> > Oliver Wong wrote:
…[6 more quoted lines elided]…
> >>   ACCESS MODE IS SEQUENTIAL.

> I think when you say "access mode is sequential" that that is the
> default and is not necessary.

Just as a 'principle' thing, I'd always include it on the theory that both
for portability and understandability by the 'next maintainer' you never
omit a setting because it happens to be (today's) default.

MCM
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-08T09:16:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dsd90q$2pg8$1@si05.rsvl.unisys.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <11ufj3eqc24o2a9@news.supernews.com> <LMbGf.61$na4.18@fe07.lga>`

```

"Last Boy Scout" <eggbtr@ezl.com> wrote in message 
news:LMbGf.61$na4.18@fe07.lga...

> You will get an error for having an assign clause and not referrring to 
> the file and you may get an error for using an FD with no assign clause.

Probably.

> Plus every field in your file description will get an error also.

I don't see why that's an absolute fact, nor do I see why that's necessary 
or even useful.

> Then every time you refer to the fields in the procedure division it will 
> be like the fields do not exist.

That depends on how good a job the compiler does in figuring out what's 
wrong.  Once the compiler has figured out that there's a problem and what 
that problem is, it can "pretend" whatever will allow it to do the best job 
of catching the most errors elsewhere.  The fact that a file description 
isn't "attached" to a particular SELECT statement has nothing whatever to do 
with the syntactic validity of a record description taken on its own merit. 
It's reasonable for the compiler to assume that a record description located 
in the FILE SECTION can be expected to describe a record in memory, and thus 
use of its various fields can be permitted without regard to where the 
information in that record might have come from.

> Everything is connected.  The select statement has to do with what device 
> has the file, and the FD is the Logical description of the file.  If the 
> select statement is wrong you can get hundredes of errors in a program.

In my case, I think in general I'd expect the compiler to note the *first* 
error as an error (and thereby preventing the *saving* of the generated 
object code), make some sort of reasonable assumption as to the most likely 
intent (as, for example, record descriptions in the file section can be 
presumed to describe records in memory), and continue to go through all the 
motions of compilation (including the process of code generation, even 
though the generated code will ultimately be discarded).

I don't even think it'd be necessary for the compiler to issue syntax errors 
on I/O statements for such a file, whether the file name used in the I/O 
statement was in the SELECT or in the FD.  If a given user-defined name was 
used in an I/O statement and in either a SELECT or an FD, I think it's 
reasonable for the compiler to assume (on the basis that two out of three 
agree) that the user-defined name was supposed to be a file-name.   Issuing 
a syntax error on the I/O statement after having issued it on the SELECT 
and/or the FD doesn't strike me as providing the user with information I 
would regard as particularly useful.

It appears that my expectations would not be met with the compilers with 
which you are familiar.

    -Chuck Stevens
```

#### ↳ Re: File declarations in the Environment and Data division

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-07T03:49:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3NUFf.578031$ki.493696@pd7tw2no>`
- **In-Reply-To:** `<9SPFf.181914$km.172504@edtnps89>`
- **References:** `<9SPFf.181914$km.172504@edtnps89>`

```
Oliver Wong wrote:
> Let's say I have a COBOL program like this:
> 
…[35 more quoted lines elided]…
> 
You've already got your answer. Just to extend it a bit :-

(a) Mainframes - don't know :-) - Presumably they control location of 
the storage device via JCL cards ???

(b) As you are primarily thinking PCs, depends upon compiler, but 
usually the default directory *should* find your 'FileA.dat'. From day 
one in COBOL I always had to contend with different data sets and common 
filenames, so :-

Petro Canada Jumping Pound Creek Plant = PECAN44
Amoco Canada Waterton Plant = AMOCO23

    SELECT Vessels-File
    ASSIGN to ws-filename
    ORGANIZATION IS LINE SEQUENTIAL
    ACCESS MODE IS SEQUENTIAL.

Working-Storage Section.

01 ws-Filename pic x(100).

So to the program I might pass lnk-Filename =

	"c:\Corrosion-Testing\Data\AMOCO23Vessels.dat".

OK - so I've switched to SQL since the above - but I'm still looking for 
different data sets, i.e. AMOCO23.mdb, PECAN44.mdb etc.

-----------------
One thing though, I noticed it looks like you have picked up your EOF 
flag technique from U. of Limerick examples (??? :-) ).

It's OK I suppose, but not an approach I'm thrilled about. I prefer as a 
separate field :-

01 FileFlag		pic 9 value 0.
    88 FileFinished	value 1.
    88 FileNotFinished	value 0.

I suppose my observation is - why have a flag/condition in a record when 
the flag applies to the file as a whole ? (What happens if he, (Mr. 
Coughlin at U of L), has RecordA, RecordB and RecordC for the same file 
?). No harm done in his approach - just a question of preference.

Jimmy
```

##### ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-02-07T07:20:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<3NUFf.578031$ki.493696@pd7tw2no>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no>`

```


James J. Gavan wrote:
> (snip) 
> You've already got your answer. Just to extend it a bit :-
> 
> (a) Mainframes - don't know :-) - Presumably they control location of 
> the storage device via JCL cards ???

In OS/360 and its successors (MVS, OS/390, z/OS) the file is specified 
in the JCL (Job Control Language) and is external to the program.  I 
suppose one could argue this is a more "object-oriented" way of doing 
things, because you can re-use the program and direct it to any 
compatible file simply by executing the program in a different JCL 
script.  Or you could change the JCL in an existing script to point to 
a different file (assuming compatible DCB structure, DSORG, LRECL, and 
BLKSIZE).  The SELECT statement actually uses an "external name" to 
refer to the file:

SELECT SYS001-INPUT-FILE ASSIGN TO SYS001.

SYS001 is the external name.  It must match the DDNAME in the JCL, 
which would look something like this:

//STEP010 EXEC PGM=MYPROG
//SYS001 DD DSN=PROD.BILLING.DETAIL.FILE,DISP=SHR

In this case the external name from the COBOL SELECT statement refers 
to the DDNAME in the JCL.  The Operating System then locates the file 
in a catalog, which points to an entry in a VTOC (Volume Table of 
Contents) on a physical disk volume.

It's more complicated for an output file:

SELECT SYS201-REPORT-FILE ASSIGN TO SYS201.

//SYS201 DD DSN=PROD.BILLING.DETAIL.REPORT,DISP=(NEW,CATLG,DELETE),
//          SPACE=(CYL,(50,20),RLSE),
//          DCB=(RECFM=FB,LRECL=145,BLKSIZE=0)

In this example, since the file is being created by the job, the JCL 
needs to specify the space allocation for the file, and the record 
format (fixed-block), record length (145), and leaves the blocksize to 
be determined by the system.  We no longer specify the physical volume 
name where the file will be stored, because everyone should be using 
SMS (System Managed Storage) to automagically assign disk space from a 
class of available volumes.  The VTOC entry will be created when the 
file is cataloged.  If the job step abends (terminates abnormally), 
the file will be deleted.  Space will be allocated with an initial 
extent of 50 Cylinders (about 42 megabytes on a logical 3390 volume), 
with secondary extents of 20 cylinders each, and any unused cylinders 
will be Released when the file is cataloged.

Both of the above examples would default to QSAM (Queued Sequential 
Access Method) which will be flat files on the mainframe.  It's a 
little bit different if you use ESDS VSAM (Entry Sequenced Data Set, 
Virtual Storage Access Method), where the SELECT clause must have an 
additional specifier pre-pended to the external name:

SELECT SYS003-CHECK-REGISTER-FILE ASSIGN TO AS-SYS003.

//SYS003 DD DSN=PROD.VSAM.CHECK.REGISTER,DISP=SHR

It gets more complicated for variable record length files, and in the 
IBM mainframe world the "shape" of the file is stored in the VTOC 
entry.  Your COBOL program will abend if the record length in the FD 
entry does not match the record length in the VTOC or the DCB of the 
JCL that creates the file.

JCL would probably be easier to work with if it wasn't tied to a 40 
year old legacy design, but it's still quite flexible in the sense 
that your COBOL program can be used with any compatible files (format 
and record length) without recompilation.

> 
> (b) As you are primarily thinking PCs, depends upon compiler, but 
…[18 more quoted lines elided]…
>     "c:\Corrosion-Testing\Data\AMOCO23Vessels.dat".

I've seen things similar to this in Realia COBOL for the PC, but IBM 
mainframe COBOL does not support "ASSIGN TO variable-ws-filename".

The only drawback I see is that a PC COBOL program would need 
additional procedural code to receive the real filename from some 
source in order to update the "variable-ws-filename" for the SELECT 
statment.  But once that's done, your COBOL program does not need to 
be recompiled in order to use a file with a different name.

With kindest regards,
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-07T17:42:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y_4Gf.461206$2k.132161@pd7tw1no>`
- **In-Reply-To:** `<SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no> <SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> In OS/360 and its successors (MVS, OS/390, z/OS) the file is specified 
> in the JCL (Job Control Language) and is external to the program.<snip>

Thanks Arnold - we truly do live in different worlds, mainframe and PC :-)

Jimmy
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-02-07T18:16:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11uie2qpkr73t8c@news.supernews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no> <SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net> <y_4Gf.461206$2k.132161@pd7tw1no>`

```
James J. Gavan wrote:
> Arnold Trembley wrote:
>>
…[5 more quoted lines elided]…
> PC :-)

Not really if you but consider a mainframe to be merely the most expensive 
peripheral you can connect to your PC.
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-08T08:02:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3v1ku1p5shefqd45jlj496v42b431mmpev@4ax.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no> <SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net> <y_4Gf.461206$2k.132161@pd7tw1no> <11uie2qpkr73t8c@news.supernews.com>`

```
On Tue, 7 Feb 2006 18:16:30 -0600, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>Not really if you but consider a mainframe to be merely the most expensive 
>peripheral you can connect to your PC. 

I bet the WWW was more expensive.    But I didn't pay for the
mainframe nor for the WWW.
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

_(reply depth: 5)_

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-02-08T18:01:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nJGdnVrTKPwbP3feRVn-oA@adelphia.com>`
- **In-Reply-To:** `<11uie2qpkr73t8c@news.supernews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no> <SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net> <y_4Gf.461206$2k.132161@pd7tw1no> <11uie2qpkr73t8c@news.supernews.com>`

```
HeyBub wrote:

>James J. Gavan wrote:
>  
…[19 more quoted lines elided]…
>
Or, is the PC the smartest dumb terminal you can connect to your mainframe?
```

###### ↳ ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-07T22:37:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ji9Gf.12994$544.12113@fe06.news.easynews.com>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no> <SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net>`

```
"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:SSXFf.15710$fM1.11003@bgtnsc04-news.ops.worldnet.att.net...
> James J. Gavan wrote:
<mch snippasge ... see below>

>> Petro Canada Jumping Pound Creek Plant = PECAN44
>> Amoco Canada Waterton Plant = AMOCO23
…[16 more quoted lines elided]…
>

Recent IBM mainframe COBOL compilers have supported a "dynamic allocation" 
facility (not to be confused with CBLQDA) which allows for a program to use the 
POSIX "putenv" facility to set all the DSN, DCB, etc facitilities "within" the 
program.  However, I don't think this is widely used and still doesn't use the 
common PC/Unix facility or the newly defined ANSI/ISO 2002 "Select/ ASSIGN 
USING" facility.  Interestingly enough, VM has allowed for one to omit "filedef" 
statements for as long as I am aware of.  It is only MVS (and I think VSE) that 
ever required "exgternal" allocations.
```

##### ↳ ↳ Re: File declarations in the Environment and Data division

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-07T14:52:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_u2Gf.180716$6K2.22972@edtnps90>`
- **References:** `<9SPFf.181914$km.172504@edtnps89> <3NUFf.578031$ki.493696@pd7tw2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:3NUFf.578031$ki.493696@pd7tw2no...
> Oliver Wong wrote:
[snip]
>> DATA DIVISION.
>> FILE SECTION.
…[5 more quoted lines elided]…
>>
[snip]
>
> -----------------
> One thing though, I noticed it looks like you have picked up your EOF flag 
> technique from U. of Limerick examples (??? :-) ).

    Yes.

>
> It's OK I suppose, but not an approach I'm thrilled about. I prefer as a 
…[9 more quoted lines elided]…
> ?). No harm done in his approach - just a question of preference.

    The original program, which I've simplified to the bare essentials 
before posting my question, was essentially a manual implementation of the 
MERGE operation. It's a toy program where the files contained a student ID 
of the form X(7), and then some data about the student in the form X(23). 
There were two files, each containing multiple records, sorted by student 
ID, and the program was to merge the two files together, with the resulting 
file still sorted on student ID.

    So there was an EVALUATE TRUE statement whiched used the fact that when 
the end of the file was reached, StudentID would be set to HIGH-VALUE, so 
that sorting would behave properly.

    - Oliver
```

#### ↳ Re: File declarations in the Environment and Data division

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-07T14:53:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gv2Gf.180717$6K2.99060@edtnps90>`
- **References:** `<9SPFf.181914$km.172504@edtnps89>`

```
"Oliver Wong" <owong@castortech.com> wrote in message 
news:9SPFf.181914$km.172504@edtnps89...
> Let's say I have a COBOL program like this:

[snip]

    Thanks everyone for your responses.

    - Oliver
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
