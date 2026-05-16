[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Determining Non-Empty Files

_15 messages · 10 participants · 1999-03 → 1999-04_

---

### Determining Non-Empty Files

- **From:** akent@seanet.com (Arthur M. Kent)
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akent-3003991951030001@i30.dialup.seanet.com>`

```
An application which I perform enhancements on has a COBOL II program
which simply checks whether an input file is empty or not.  If it is
empty, a simple one line message is put on a report for the users to look
at.  I've been tasked to clone this program into another step within
another job, and perform the same function on a series of files.  The
current program, of course, has the exact number of Select clauses for the
same number of DD statements in the JCL.  Unfortunately, whenever a new
file is added to the step in the job, the program needs to be modified,
both in the Data and Procedure Divisions.  Although simple, this is a
maintenance nightmare.

I am wondering if it is at all possible to have a table consisting of the
file names to be "looked at".  The COBOL II program would open the table
and read each record, which of course consists of the file name.  Without
having the DD name in the step which the program is executing in, is it
possible for the COBOL program to "find the file", open it, see if it is
empty or not, close the file, read the table again, obtain the name of the
next file to be looked at, etc.?  I am in an IBM MVS/JCL environment,
using COBOL II.  Also, each file named in the table has the same record
length.

Any advice/information etc. would be appreciated.

Thanks,
Arthur M. Kent
```

#### ↳ Re: Determining Non-Empty Files

- **From:** "Lanny Levine" <llevine@sprint.ca>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nHhM2.54127$Mb.24731360@newscontent-02.sprint.ca>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com>`

```
I think a REXX exec would be a good solution. You would also certainly be
able to do this with an Assembler program but I think most would agree that
this would be an effort of a different magnitude compared to REXX.

Please let us know what implementation you eventually decide to use.

Lanny


Arthur M. Kent wrote in message ...
>An application which I perform enhancements on has a COBOL II program
>which simply checks whether an input file is empty or not.  If it is
…[22 more quoted lines elided]…
>Arthur M. Kent
```

#### ↳ Re: Determining Non-Empty Files

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37021BD2.5F6220B1@zip.com.au>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com>`

```
Arthur M. Kent wrote:
> 
> An application which I perform enhancements on has a COBOL II program
…[4 more quoted lines elided]…
> current program, of course, has the exact number of Select clauses for the

Dynamic allocation is really easy in C programming.  If you have the C
compiler then call a C routine that does a DYNALLOC to a specific DD
with share and FREE (free on close).  When you are back in your cobol
program open the file, check it and close it again.  The free
automatically deallocates.

You can do the same in an assembler routine but it is hard to set up if
you do not have one already.  There should be one if you query share but
some shops are funny about using 'free software'.

Just had a thought, what about listing a series of the same DDNAME with
FREE=CLOSE in the JCL, repeatadly openning and closing the file should
walk you through the list.  When the open fails you are out of files. 
Interesting thought, probably wont work though.
```

#### ↳ Re: Determining Non-Empty Files

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3702301C.2E0CD32B@NOSPAMhome.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com>`

```
I'm thinking there's a way to do this in JCL.  If you could find a
utility which gives a non-zero return code if a file is empty, then you
could create a proc which accepts a file's symbolic and an input data
line.  After checking the return code, it could append the data line to
a file or not.

Can someone think of JCL utility which will do this?

Of course REXX will do it, and maybe CLISTs (I have written the former
but not the latter).

Another way to do this is to have a called COBOL program for each file
you're interested in.  Then use a table to pick which one to call.

Arthur M. Kent wrote:
> 
> An application which I perform enhancements on has a COBOL II program
…[23 more quoted lines elided]…
> Arthur M. Kent
```

##### ↳ ↳ Re: Determining Non-Empty Files

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dtm6j$dkm$1@callisto.clark.net>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com>`

```
In article <3702301C.2E0CD32B@NOSPAMhome.com>,
Howard Brazee  <brazee@NOSPAMhome.com> wrote:
>I'm thinking there's a way to do this in JCL.  If you could find a
>utility which gives a non-zero return code if a file is empty, then you
…[4 more quoted lines elided]…
>Can someone think of JCL utility which will do this?

IDCAMS... given the SYSIN line of something like:

REPROFILE IFILE (IDD) OFILE (ODD) COUNT (1)

... If one uses, say, 

//IDD   DD DSN=&FILNAM001,DISP=SHR
//ODD   DD SYSOUT=*

... there's little damage that can be done, few resources burned up and a
lovely COND CODE 0004 returned for an empty file.

DD

>Arthur M. Kent wrote:
>> 
…[24 more quoted lines elided]…
>> Arthur M. Kent
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7du3it$rlu@netnews1.apci.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com> <7dtm6j$dkm$1@callisto.clark.net>`

```
Here's a program I wrote several years ago in COBOL to handle this
situation.  Note the use of "BLOCK CONTAINS 0 RECORD CONTAINS 0" which
enables the program to handle a sequential file of any record size.

       ID DIVISION.
       PROGRAM-ID. A5C610.
      *AUTHOR. A RUSSELL.
      *    SET COND-CODE FOR EMPTY FILE.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT IN-FILE ASSIGN TO INFILE.
       DATA DIVISION.
       FILE SECTION.
       FD  IN-FILE LABEL STANDARD
           BLOCK CONTAINS 0 RECORD CONTAINS 0.
       01  IN-REC                      PIC X(80).
       PROCEDURE DIVISION.
           OPEN INPUT IN-FILE.
           MOVE 0 TO RETURN-CODE
           READ IN-FILE
               AT END MOVE 16 TO RETURN-CODE.
           CLOSE IN-FILE.
           STOP RUN.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer

docdwarf@clark.net wrote in message <7dtm6j$dkm$1@callisto.clark.net>...
>In article <3702301C.2E0CD32B@NOSPAMhome.com>,
>Howard Brazee  <brazee@NOSPAMhome.com> wrote:
…[26 more quoted lines elided]…
>>> empty, a simple one line message is put on a report for the users to
look
>>> at.  I've been tasked to clone this program into another step within
>>> another job, and perform the same function on a series of files.  The
>>> current program, of course, has the exact number of Select clauses for
the
>>> same number of DD statements in the JCL.  Unfortunately, whenever a new
>>> file is added to the step in the job, the program needs to be modified,
…[3 more quoted lines elided]…
>>> I am wondering if it is at all possible to have a table consisting of
the
>>> file names to be "looked at".  The COBOL II program would open the table
>>> and read each record, which of course consists of the file name.
Without
>>> having the DD name in the step which the program is executing in, is it
>>> possible for the COBOL program to "find the file", open it, see if it is
>>> empty or not, close the file, read the table again, obtain the name of
the
>>> next file to be looked at, etc.?  I am in an IBM MVS/JCL environment,
>>> using COBOL II.  Also, each file named in the table has the same record
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370299B5.1904C0E@NOSPAMhome.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com> <7dtm6j$dkm$1@callisto.clark.net> <7du3it$rlu@netnews1.apci.com>`

```
What version of COBOL are you using?  I thought COBOL for MVS required
correct record and block lengths.  Or is it that it disallows anything
except correct and zero?

Alan Russell wrote:
> 
> Here's a program I wrote several years ago in COBOL to handle this
…[90 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990331231731.10121.00000405@ngol05.aol.com>`
- **References:** `<370299B5.1904C0E@NOSPAMhome.com>`

```
In article <370299B5.1904C0E@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes:

>
>What version of COBOL are you using?  I thought COBOL for MVS required
…[9 more quoted lines elided]…
>

This works fine for mainframe COBOL for MVS / ADCycle\370.
It is restricted to INPUT files only that can be defined in this manner.
This allows for any record length up to the largest 01 level. and lets the
system handle the BLOCK buffering.
Output files can use BLOCK CONTAINS 0 to get the optimum blocksize 
on NEW files.
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 4)_

- **From:** "Lanny Levine" <llevine@sprint.ca>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0VAM2.55622$Mb.25424564@newscontent-02.sprint.ca>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com> <7dtm6j$dkm$1@callisto.clark.net> <7du3it$rlu@netnews1.apci.com>`

```
Alan,

    Did you never get into trouble even though you're not setting the return
code (register 15) just before the GOBACK? Is it not possible, for instance,
that the CLOSE could set register 15 to zero after it had been set to 16
because the file was empty?

    Lanny


Alan Russell wrote in message <7du3it$rlu@netnews1.apci.com>...
>Here's a program I wrote several years ago in COBOL to handle this
>situation.  Note the use of "BLOCK CONTAINS 0 RECORD CONTAINS 0" which
…[73 more quoted lines elided]…
>>>> file names to be "looked at".  The COBOL II program would open the
table
>>>> and read each record, which of course consists of the file name.
>Without
>>>> having the DD name in the step which the program is executing in, is it
>>>> possible for the COBOL program to "find the file", open it, see if it
is
>>>> empty or not, close the file, read the table again, obtain the name of
>the
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 5)_

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dvq7j$m8l@netnews1.apci.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com> <7dtm6j$dkm$1@callisto.clark.net> <7du3it$rlu@netnews1.apci.com> <0VAM2.55622$Mb.25424564@newscontent-02.sprint.ca>`

```
The reserved word RETURN-CODE is for a memory location which COBOL will use
to populate register 15 before it terminates at a STOP RUN or GOBACK. It is
also the area where COBOL puts the contents of register 15 when a CALLed
subroutine returns control back to the calling program.  Other  COBOL verbs
never put anything in this memory location.

Lanny Levine wrote in message
<0VAM2.55622$Mb.25424564@newscontent-02.sprint.ca>...
>Alan,
>
>    Did you never get into trouble even though you're not setting the
return
>code (register 15) just before the GOBACK? Is it not possible, for
instance,
>that the CLOSE could set register 15 to zero after it had been set to 16
>because the file was empty?
…[73 more quoted lines elided]…
>>>>> same number of DD statements in the JCL.  Unfortunately, whenever a
new
>>>>> file is added to the step in the job, the program needs to be
modified,
>>>>> both in the Data and Procedure Divisions.  Although simple, this is a
>>>>> maintenance nightmare.
…[7 more quoted lines elided]…
>>>>> having the DD name in the step which the program is executing in, is
it
>>>>> possible for the COBOL program to "find the file", open it, see if it
>is
…[3 more quoted lines elided]…
>>>>> using COBOL II.  Also, each file named in the table has the same
record
>>>>> length.
>>>>>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 6)_

- **From:** akent@seanet.com (Arthur M. Kent)
- **Date:** 1999-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akent-0104991952350001@g2.dialup.seanet.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com> <3702301C.2E0CD32B@NOSPAMhome.com> <7dtm6j$dkm$1@callisto.clark.net> <7du3it$rlu@netnews1.apci.com> <0VAM2.55622$Mb.25424564@newscontent-02.sprint.ca> <7dvq7j$m8l@netnews1.apci.com>`

```
I want to thank everyone who provided some thoughful idesa in response to
my request.  Mr. Sven Schneider sent me (via EMail) an actual coding
example of how to accomplish this.  Once I adapt it to our environment and
test it, I'll post the results here.

Again, many thanks.

In article <7dvq7j$m8l@netnews1.apci.com>, "Alan Russell"
<RUSSELAH@apci.com> wrote:

> The reserved word RETURN-CODE is for a memory location which COBOL will use
> to populate register 15 before it terminates at a STOP RUN or GOBACK. It is
…[120 more quoted lines elided]…
> >
```

#### ↳ Re: Determining Non-Empty Files

- **From:** sven_schneider@my-dejanews.com
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dtkse$47i$1@nnrp1.dejanews.com>`
- **References:** `<akent-3003991951030001@i30.dialup.seanet.com>`

```
In article <akent-3003991951030001@i30.dialup.seanet.com>,
  akent@seanet.com (Arthur M. Kent) wrote:
> An application which I perform enhancements on has a COBOL II program
> which simply checks whether an input file is empty or not.  If it is
> empty, a simple one line message is ...

<snip>

> Thanks,
> Arthur M. Kent
>


Hi Arthur,

take a look to the thread 'dynamic assign'. There is described a way to use
one 'select input-file assign ddname' - statement with multiple 'ddname'. But
it only works with non-VSAM datasets. if you need - i can send you a
cobol-example.





Sven Schneider
BEKO Informatik GmbH

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Determining Non-Empty Files

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990331150238.10291.00000363@ng-ch1.aol.com>`
- **References:** `<7dtkse$47i$1@nnrp1.dejanews.com>`

```
I think your best bet is using REXX to run a JCL/Proc combo that reads a value
from a Sequential file, replaces the symbolic in the JCL with the "file name"
and runs the JCL, and keeps doing it until you reach EOF.

This way your JCL only has one step and REXX does the controlling.

Good Luck,

TW
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37028B16.7D5EA208@NOSPAMhome.com>`
- **References:** `<7dtkse$47i$1@nnrp1.dejanews.com> <19990331150238.10291.00000363@ng-ch1.aol.com>`

```
Twymer wrote:
> 
> I think your best bet is using REXX to run a JCL/Proc combo that reads a value
…[7 more quoted lines elided]…
> TW

Rexx is a very nice tool - if your programmers are familiar with it. 
Plus it works with any IBM environment.

Using an IDCAMS utility is more familiar, and easier to maintain.  But
if you wish to make it into a proc, it uses 3 files.  I wouldn't go to a
C program unless you're in a C shop.  My vote would be to go with
whichever method is likely to be understood by other programmers with
the least amount of work.
```

###### ↳ ↳ ↳ Re: Determining Non-Empty Files

_(reply depth: 4)_

- **From:** bfetml@aol.com (BFETML)
- **Date:** 1999-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990401012555.08322.00000549@ng-fx1.aol.com>`
- **References:** `<37028B16.7D5EA208@NOSPAMhome.com>`

```
hi,
interesting topic, recently I had to determine if  1 file only was empty  in a
job stream. Spoke to some colleagues, since we had easytrieve on our system, I
was able to use easytrieve to determine whether I had an empty file or not  and
set the condition code to 
whatever I wanted it to be.   I don't have the code with me at home, but if
anyone is interested let me know i will post it. In fact using easytrieve I
could set a return code if I had no records or any number of records I wanted. 
ps. does anyone know how I can check for an empty file using fileaid?

eric
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
