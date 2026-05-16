[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable Length Input File

_59 messages · 16 participants · 2006-12 → 2007-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Variable Length Input File

- **From:** manubay@pacbell.net
- **Date:** 2006-12-21T09:08:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`

```
Is there a way in Cobol to handle an input file that has variable
LRECL?  If there is, how would it be defined in the FD section?  Thank
you.
```

#### ↳ Re: Variable Length Input File

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-21T17:56:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emeht0$cdh$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`

```
In article <1166720886.579682.68830@42g2000cwt.googlegroups.com>,
 <manubay@pacbell.net> wrote:
>Is there a way in Cobol to handle an input file that has variable
>LRECL?

Yes.

>If there is, how would it be defined in the FD section?

The way the manual tells it usually works.

>Thank you.

You're quite welcome.

DD
```

##### ↳ ↳ Re: Variable Length Input File

- **From:** manubay@pacbell.net
- **Date:** 2006-12-21T10:16:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166725014.449314.160860@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<emeht0$cdh$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com>`

```
Will it work on MVS COB 370 compiler?  How should i define the PIC
clause?  Unfortunately, I don't have a manual.  Thanks again.

Regards,
Greg



docdwarf@panix.com wrote:
> In article <1166720886.579682.68830@42g2000cwt.googlegroups.com>,
>  <manubay@pacbell.net> wrote:
…[13 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-21T18:22:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emejdb$bl9$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com>`

```
In article <1166725014.449314.160860@i12g2000cwa.googlegroups.com>,
 <manubay@pacbell.net> wrote:
>Will it work on MVS COB 370 compiler?

I've had no troubles in that environment.

>How should i define the PIC
>clause?

That depends on the file.

>Unfortunately, I don't have a manual.

This might help:

<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/IGY3LR10/CCONTENTS?DT=20020920180651>

>Thanks again.

You're quite welcome.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 4)_

- **From:** manubay@pacbell.net
- **Date:** 2006-12-21T11:00:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166727602.664630.95240@48g2000cwx.googlegroups.com>`
- **In-Reply-To:** `<emejdb$bl9$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com>`

```
I think I didn't explain my problem well.  Maybe it'll be better with
an example.  Let's say, I have file called TESTA.  TESTA doesn't always
have the same LRECL.  Sometime TESTA will be defined in the JCL with
LRECL=30.  Other times, it will be have LRECL=70.  And so on.  My
problem is how should TESTA be represented in FD?

Regards,
Greg

docdwarf@panix.com wrote:
> In article <1166725014.449314.160860@i12g2000cwa.googlegroups.com>,
>  <manubay@pacbell.net> wrote:
…[19 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-21T19:22:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ememt4$s3g$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com>`

```
In article <1166727602.664630.95240@48g2000cwx.googlegroups.com>,
 <manubay@pacbell.net> wrote:
>I think I didn't explain my problem well.  Maybe it'll be better with
>an example.  Let's say, I have file called TESTA.  TESTA doesn't always
>have the same LRECL.  Sometime TESTA will be defined in the JCL with
>LRECL=30.  Other times, it will be have LRECL=70.  And so on.  My
>problem is how should TESTA be represented in FD?

That depends on the DCB for TESTA.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-21T22:36:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y%Dih.135011$X52.28057@fe03.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com>`

```
Are you saying that the input file isn't always the SAME input file?  Does it 
always have the same fields in it?

What are the characteristics of the file?

COBOL does NOT handle well cases where the input may be one file today and 
another (differently defined) file tomorrow.  It does handle well cases where 
the same RECFM=V is used and different length records appear in the file.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 5)_

- **From:** "P. Raulerson" <paul.rl@raulersons.com>
- **Date:** 2006-12-21T18:58:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65Gih.13245$RR4.7129@newsfe22.lga>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com>`

```
Wow -that's a slightly different animal than what I took you to originally 
mean. Each run is essentially brand new file, huh?

The simple answer is to define the dataset as variable with the largest 
possible record size set as the Max, then just use standard variable records 
in COBOL.

That's a non-trivial challenge.

-Paul

<manubay@pacbell.net> wrote in message 
news:1166727602.664630.95240@48g2000cwx.googlegroups.com...
>I think I didn't explain my problem well.  Maybe it'll be better with
> an example.  Let's say, I have file called TESTA.  TESTA doesn't always
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 6)_

- **From:** Alex Flinsch <avflinsch@att.net>
- **Date:** 2006-12-22T11:08:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.12.22.11.07.20.959975@att.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga>`

```
On Thu, 21 Dec 2006 18:58:39 -0600, P. Raulerson wrote:

> Wow -that's a slightly different animal than what I took you to originally 
> mean. Each run is essentially brand new file, huh?
…[7 more quoted lines elided]…
> 

2 ways to go about it I can think of before more coffee --

The first is to set the record size in the program to the maximum, and the
record type to fixed. Then have a conversion step before executing the
program which uses a utility to convert the file to the lrecl used in the
program

The other is to set the record size in the program to the maximum and use
a record type of undefined.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 7)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-22T04:35:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166790950.351244.67040@42g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<pan.2006.12.22.11.07.20.959975@att.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net>`

```

Alex Flinsch wrote:
> On Thu, 21 Dec 2006 18:58:39 -0600, P. Raulerson wrote:
>
…[19 more quoted lines elided]…
> a record type of undefined.


ALTERNATIVELY (and I like this one): set the FD to contain a record of
one character length fixed blocked and read repeatedly, building the
record in working storage.

I can't believe that no-one came up with that one before me.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-22T12:57:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emgkns$hcb$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com>`

```
In article <1166790950.351244.67040@42g2000cwt.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>
>Alex Flinsch wrote:
…[3 more quoted lines elided]…
>> > mean. Each run is essentially brand new file, huh?

[snip]

>ALTERNATIVELY (and I like this one): set the FD to contain a record of
>one character length fixed blocked and read repeatedly, building the
>record in working storage.
>
>I can't believe that no-one came up with that one before me.

Perhaps they did, Mr Maclean, and discarded it as being of... questionable 
utility on an IBM-style mainframe.  Given:

FILE-CONTROL.                             
    SELECT INFILE                         
           ASSIGN TESTA                   
           ORGANIZATION SEQUENTIAL.       
DATA DIVISION.                            
FILE SECTION.                             
FD  INFILE.                               
01  INREC                       PIC X(01).
WORKING-STORAGE SECTION.                  
PROCEDURE DIVISION.                       
                                          
    OPEN INPUT INFILE.                    
THE-READ.                                 
    READ INFILE.                          
    CLOSE INFILE.                         
THE-GOBACK.                               
    GOBACK.                               

... compiled with IBM Enterprise COBOL for z/OS and OS/390 3.2.1 and my 
sites's usual compiler invocation parms...

... and a TESTA dataset defined (via IEFBR14) as

//TESTA    DD DSN=USERID1.TESTA,               
//            DISP=(,CATLG,CATLG),             
//            UNIT=SYSDA,                      
//            SPACE=(TRK,(1,1),RLSE),          
//            DCB=(RECFM=FB,LRECL=30,BLKSIZE=27990)

... and run-JCL of:

//STEP020  EXEC PGM=SKELPROG                   
//TESTA     DD  DSN=USERID.TESTA,DISP=SHR      
//SYSPRINT  DD  SYSOUT=*                       
//SYSOUT    DD  SYSOUT=*                       
//SYSUDUMP  DD  SYSOUT=*                       
//SYSABOUT  DD  SYSOUT=*                       

... the job ABENDs with IEF450I WSXSKEL0 STEP020 - ABEND=S000 U4038 
REASON=00000001 and the following messages in the SYSOUT:

IGZ0201W A file attribute mismatch was detected. File INFILE in program 
SKELPROG had a record length of 1 and the file specified in the ASSIGN 
clause had a record length of 30.
IGZ0035S There was an unsuccessful OPEN or CLOSE of file TESTA in program 
SKELPROG at relative location X'0358'. Neither FILE STATUS nor an ERROR 
declarative were specified. The status code was 39. From compile unit 
SKELPROG at entry point SKELPROG at statement 19 at compile unit offset 
+00000358 at entry offset +00000358 at address 000082C8.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-23T05:44:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166881498.301512.7030@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<emgkns$hcb$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <emgkns$hcb$1@reader2.panix.com>`

```

docdwarf@panix.com wrote:
> In article <1166790950.351244.67040@42g2000cwt.googlegroups.com>,
> Alistair <alistair@ld50macca.demon.co.uk> wrote:
…[68 more quoted lines elided]…
> DD

How about over-riding the DCB?
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-23T15:33:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emji8c$ll6$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <emgkns$hcb$1@reader2.panix.com> <1166881498.301512.7030@i12g2000cwa.googlegroups.com>`

```
In article <1166881498.301512.7030@i12g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>
>docdwarf@panix.com wrote:
>> In article <1166790950.351244.67040@42g2000cwt.googlegroups.com>,
>> Alistair <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>> >ALTERNATIVELY (and I like this one): set the FD to contain a record of
>> >one character length fixed blocked and read repeatedly, building the
…[5 more quoted lines elided]…
>> utility on an IBM-style mainframe.

[snip]

>> ... the job ABENDs with IEF450I WSXSKEL0 STEP020 - ABEND=S000 U4038
>> REASON=00000001 and the following messages in the SYSOUT:
…[10 more quoted lines elided]…
>How about over-riding the DCB?

I'm not quite sure what technique you might use to accomplish this, Mr 
Maclean.  If you would be so kind as to post an example it might help 
clarify the matter.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 11)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2006-12-24T00:39:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lairo250619raljqhu1d545id7c5rbsan0@4ax.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <emgkns$hcb$1@reader2.panix.com> <1166881498.301512.7030@i12g2000cwa.googlegroups.com> <emji8c$ll6$1@reader2.panix.com>`

```
On Sat, 23 Dec 2006 15:33:32 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <1166881498.301512.7030@i12g2000cwa.googlegroups.com>,
>Alistair <alistair@ld50macca.demon.co.uk> wrote:
…[36 more quoted lines elided]…
>DD

Assuming that you have BLOCK 0 and RECORD VARYING FROM 1 TO 32760 (or
maximum record size expected) in the COBOL program and assuming the
file is actually VB or VBS (RECORDING S needed in the COBOL program),
you would then code RECFM=VB,LRECL='cobol TO LENGTH +4' in the JCL and
thus be able to read any file regardless of length.  For FB code the
maximum size 01 level expected for the FD and RECORD 0 in addition to
BLOCK 0 and the actual record length will be determined at run time.
Unfortunately this only works for INPUT.  I don't think that you can
use RECORD 0 VARYING DEPENDING ON for fixed length records.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-24T01:13:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emkk86$m9a$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1166881498.301512.7030@i12g2000cwa.googlegroups.com> <emji8c$ll6$1@reader2.panix.com> <lairo250619raljqhu1d545id7c5rbsan0@4ax.com>`

```
In article <lairo250619raljqhu1d545id7c5rbsan0@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Sat, 23 Dec 2006 15:33:32 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[42 more quoted lines elided]…
>thus be able to read any file regardless of length.

No problems with that, Mr Morris... that's part of the nature of VB 
datasets on Big Iron.  I noticed that the original poster has yet to 
respond to questions about the DCB; it might be that the time 
for this assignment has gone past 'due date'.

>For FB code the
>maximum size 01 level expected for the FD and RECORD 0 in addition to
>BLOCK 0 and the actual record length will be determined at run time.
>Unfortunately this only works for INPUT.  I don't think that you can
>use RECORD 0 VARYING DEPENDING ON for fixed length records.  

I'm not sure how this 'over-rides the DCB', as Mr Maclean suggested... but 
perhaps sometime next week, if I remember, I'll cobble together some code 
and see if this flies.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 13)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2006-12-24T13:39:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1166881498.301512.7030@i12g2000cwa.googlegroups.com> <emji8c$ll6$1@reader2.panix.com> <lairo250619raljqhu1d545id7c5rbsan0@4ax.com> <emkk86$m9a$1@reader2.panix.com>`

```
On Sun, 24 Dec 2006 01:13:42 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <lairo250619raljqhu1d545id7c5rbsan0@4ax.com>,
>Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
…[59 more quoted lines elided]…
>and see if this flies.

If RECORD 0 is coded, then filling in of the field in the DCB is
deferred to the OPEN.  Since LRECL in the program's DCB normally
overrides both JCL supplied LRECL and tape or disk label DCB, the
coding of RECORD 0 allows the program to use an external source for
the record length and eliminates the need for checking the program
supplied value against the external source.
>
>DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-26T13:26:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emr7ue$r19$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <lairo250619raljqhu1d545id7c5rbsan0@4ax.com> <emkk86$m9a$1@reader2.panix.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>`

```
In article <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Sun, 24 Dec 2006 01:13:42 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <lairo250619raljqhu1d545id7c5rbsan0@4ax.com>,
>>Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:

[snip]

>>>For FB code the
>>>maximum size 01 level expected for the FD and RECORD 0 in addition to
…[13 more quoted lines elided]…
>supplied value against the external source.

Hmmmmm... perhaps I am doing something wrong, Mr Morris... given

FILE-CONTROL.                                 
    SELECT INFILE                             
           ASSIGN TESTA                       
           ORGANIZATION SEQUENTIAL.           
DATA DIVISION.                                
FILE SECTION.                                 
FD  INFILE                                    
    RECORD CONTAINS 0                         
    BLOCK CONTAINS 0.                         
01  INFILE-RECORD               PIC X(32767). 
WORKING-STORAGE SECTION.      
PROCEDURE DIVISION.           
    OPEN INPUT INFILE.        
THE-READ.                     
    READ INFILE.              
    CLOSE INFILE.             
THE-GOBACK.                   
    GOBACK.                   

... compiled with IBM Enterprise COBOL for z/OS and OS/390 3.2.1 and my 
sites's usual compiler invocation parms...

... and a TESTA dataset defined (via IEFBR14) as 


//TESTA    DD DSN=USERID1.TESTA,               
//            DISP=(,CATLG,CATLG),             
//            UNIT=SYSDA,                       
//            SPACE=(TRK,(1,1),RLSE),           
//            DCB=(RECFM=FB,LRECL=30,BLKSIZE=27990) 


... and run-JCL of: 


//STEP020  EXEC PGM=SKELPROG                   
//TESTA     DD  DSN=USERID.TESTA,DISP=SHR       
//SYSPRINT  DD  SYSOUT=*                       
//SYSOUT    DD  SYSOUT=*                       
//SYSUDUMP  DD  SYSOUT=*                       
//SYSABOUT  DD  SYSOUT=*                       

... ... the job ABENDs with IEF450I WSXSKEL0 STEP020 - ABEND=S000 U4038 
REASON=00000001 and the following messages in the SYSOUT: 

IGZ0002S WSXSKEL0,STEP020 ,0797,D,TESTA   ,GET   
,WRNG.LEN.RECORD,00000006000D00,QSAM

From compile unit SKELPROG at entry point SKELPROG at statement 24 at 
compile unit offset +00000382 at entry offset +00000382 at address 
0000829A.

This differs slightly from the first run attempted... but it is an ABEND 
nontheless; a bit farther down in the dump I find:

14 INFILE FILE SPECIFIED AS: ORGANIZATION=QSAM SEQUENTIAL, ACCESS 
MODE=SEQUENTIAL, RECFM=FIXED BLOCKED.  CURRENT STATUS OF FILE IS: OPEN 
STATUS=INPUT, FILE STATUS CODE=30.

... which indicates to me that the load module is not very happy with what 
it was told to process as the INFILE.

Would you be so kind as to point out what you see as being the errors I've 
made in attempting to implement your suggestion?

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 15)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2006-12-26T12:19:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<db00b$45915999$d066072d$11570@FUSE.NET>`
- **In-Reply-To:** `<emr7ue$r19$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <lairo250619raljqhu1d545id7c5rbsan0@4ax.com> <emkk86$m9a$1@reader2.panix.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>,
> Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
…[90 more quoted lines elided]…
> 
Just to get something to you quickly, in case Clark is otherwise occupied...

Just how did you expect to get VARIABLE length records when you 
explicitly created the file as FIXED length?
	 DCB=(RECFM=FB,LRECL=30,BLKSIZE=27990)
The DCB option:
	RECFM=FB says FIXED BLOCKED.
You need:
	RECFM=VB for VARIABLE BLOCKED.

You should also add:
	RECORDING MODE V
See the Enterprise COBOL LRM for specifics about how the compiler 
determines the recording mode if you do not specify it.

Carl
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-26T17:39:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emrmnv$n8$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <db00b$45915999$d066072d$11570@FUSE.NET>`

```
In article <db00b$45915999$d066072d$11570@FUSE.NET>,
CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
>docdwarf@panix.com wrote:
>> In article <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>,
…[11 more quoted lines elided]…
>>>>> Unfortunately this only works for INPUT.

[snip]

>> //TESTA    DD DSN=USERID1.TESTA,               
>> //            DISP=(,CATLG,CATLG),             
>> //            UNIT=SYSDA,                       
>> //            SPACE=(TRK,(1,1),RLSE),           
>> //            DCB=(RECFM=FB,LRECL=30,BLKSIZE=27990) 

[snip]

>> ... ... the job ABENDs with IEF450I WSXSKEL0 STEP020 - ABEND=S000 U4038 
>> REASON=00000001 and the following messages in the SYSOUT: 

[snip]

>> Would you be so kind as to point out what you see as being the errors I've 
>> made in attempting to implement your suggestion?
…[4 more quoted lines elided]…
>explicitly created the file as FIXED length?

I didn't expect to get VB records; as per Mr Morris' assertion above, the 
solution is for FB.

Dealing with a VB dataset with different-length records has not presented, 
at least to me, very much of a problem... the difficulty is, I believe, in 
dealing with a fixed length dataset which has different-length records.  I 
had been taught, e'er-so-long ago, that a compiled COBOL module does not 
readily enjoy having to deal with a fixed-length dataset which contains 
record-lengths differing from those specified before the compile... and so 
far all examples I've been able to come up with appear to demonstrate this 
behavior.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 17)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2006-12-26T16:53:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2cafe$459199e9$d066072d$978@FUSE.NET>`
- **In-Reply-To:** `<emrmnv$n8$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <db00b$45915999$d066072d$11570@FUSE.NET>,
> CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
…[50 more quoted lines elided]…
> 
???? > fixed length dataset which has different-length records. ????

That is a total contradiction!  Either the file has FIXED LENGTH records 
or the records VARY in length.  Possibly some other platform can resolve 
this contradiction, but you indicated you are using the Enterprise COBOL 
compiler.  Therefore, pick FIXED or pick VARYING...

Bye...
Carl
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-26T23:11:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emsa6g$n0j$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET>`

```
In article <2cafe$459199e9$d066072d$978@FUSE.NET>,
CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Dealing with a VB dataset with different-length records has not presented, 
>> at least to me, very much of a problem... the difficulty is, I believe, in 
>> dealing with a fixed length dataset which has different-length records.

[snip]

>???? > fixed length dataset which has different-length records. ????
>
>That is a total contradiction!  Either the file has FIXED LENGTH records 
>or the records VARY in length.

You might want to inform the person who started this thread about that... 
but the last heard was from that account in this thread seems to have been 
as follows.  From 
<http://groups.google.com/group/comp.lang.cobol/msg/e2bd0f47c45850c8?dmode=source>

--begin quoted text:

I think I didn't explain my problem well.  Maybe it'll be better with
an example.  Let's say, I have file called TESTA.  TESTA doesn't always
have the same LRECL.  Sometime TESTA will be defined in the JCL with
LRECL=30.  Other times, it will be have LRECL=70.  And so on.  My
problem is how should TESTA be represented in FD? 

--end quoted text

I was able to find the entire thread beginning at 
<http://groups.google.com/group/comp.lang.cobol/browse_thread/thread/5f5078dee2ab20f1/1418ce24a2de8ee3?q=%22BLOCK+0+and+the+actual+record+length%22&lnk=ol&>

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-27T12:54:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vdr12F1botahU1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com>`

```
I have a question, please, Doc.

(It is many years since I worked in this environment (actually, it was an 
environment LIKE this one because this environment was not then available, 
if you catch my drift...))

I have retained enough of what I learned there to understand the 
comprehensive samples you posted, and note in passing that nothing much 
appears to have changed as far as JCL is concerned...

I too, would have expected RECFM=VB, but I understand why you didn't put 
that.

My question is this (and forgive my ignorance if there is some obvious 
reason that I simply haven't tumbled to):

If the JCL specifies a block size of  27990 (nicely divisible by 30, 933 
times), and the COBOL program is specifying a block/record size of 32767, 
wouldn't this be likely to cause an IO error when the dataset is opened?

Just a thought...

Pete.

TOP POST - nothing more below

<docdwarf@panix.com> wrote in message news:emsa6g$n0j$1@reader2.panix.com...
> In article <2cafe$459199e9$d066072d$978@FUSE.NET>,
> CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 20)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-27T00:56:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emsgci$spv$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <4vdr12F1botahU1@mid.individual.net>`

```
In article <4vdr12F1botahU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>I have a question, please, Doc.

[snip]

>If the JCL specifies a block size of  27990 (nicely divisible by 30, 933 
>times), and the COBOL program is specifying a block/record size of 32767, 
>wouldn't this be likely to cause an IO error when the dataset is opened?

I thought there would be some kind of error as well, Mr Dashwood, hence my 
testing... but both of our thinkings appear to be contrary to Mr Morris' 
assertion that 'For FB code the maximum size 01 level expected for the FD 
and RECORD 0 in addition to BLOCK 0 and the actual record length will be 
determined at run time.  Unfortunately this only works for INPUT.'

I posted code which I believed was in accordance with this - it is a new 
technique for me and I'm not quite sure I got it right - and, likewise, 
posted the results (an ABEND).  If there's something else I should be 
doing then, by all means, post the code - both COBOL and JCL - and I'll be 
more than happy to compile it and show the results.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-27T23:50:22+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vf1ffF1c13jbU1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <4vdr12F1botahU1@mid.individual.net> <emsgci$spv$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:emsgci$spv$1@reader2.panix.com...
> In article <4vdr12F1botahU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[20 more quoted lines elided]…
> DD

As I don't have access to this environment I can't do it myself, but I'd be 
very interested to see what happens if the Picture of the 01 following the 
FD was made the same as the LRECL size...

Not wishing to impose, but perhaps, if you had time...? (all other things 
remaining as you have them...)

Pete.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-27T13:07:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emtr65$6b5$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <4vdr12F1botahU1@mid.individual.net> <emsgci$spv$1@reader2.panix.com> <4vf1ffF1c13jbU1@mid.individual.net>`

```
In article <4vf1ffF1c13jbU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:emsgci$spv$1@reader2.panix.com...
…[8 more quoted lines elided]…
>>>wouldn't this be likely to cause an IO error when the dataset is opened?

[snip]

>> I posted code which I believed was in accordance with this - it is a new
>> technique for me and I'm not quite sure I got it right - and, likewise,
…[6 more quoted lines elided]…
>FD was made the same as the LRECL size...

Therein lies the difficulty, Mr Dashwood... as I understand the original 
poster's request the LRECL of TESTA changes from one run to the next; 
there is no *the* LRECL size.  Once again, from 
<http://groups.google.com/group/comp.lang.cobol/msg/e2bd0f47c45850c8?dmode=source>

--begin quoted text:

TESTA doesn't always have the same LRECL.  Sometime TESTA will be defined 
in the JCL with LRECL=30.  Other times, it will be have LRECL=70.  And so 
on.  My problem is how should TESTA be represented in FD?

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 23)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-27T23:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2lDkh.167701$7G.139752@fe08.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <4vdr12F1botahU1@mid.individual.net> <emsgci$spv$1@reader2.panix.com> <4vf1ffF1c13jbU1@mid.individual.net> <emtr65$6b5$1@reader2.panix.com>`

```
Anyone interested in things related to "FS=39" in an IBM z/OS environment (with 
a currently supported compiler) may want to look at:

 "APPENDIX1.8 Appendix H. Preventing file status 39 for QSAM files"

    at

    http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3MG31/APPENDIX1.8

As mentioned earlier, if you have (historically) used RECFM=U to handle some of 
these issues, you should also read:

     http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3MG31/3.5.4
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-28T14:39:41+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vglitF1cepuaU1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <4vdr12F1botahU1@mid.individual.net> <emsgci$spv$1@reader2.panix.com> <4vf1ffF1c13jbU1@mid.individual.net> <emtr65$6b5$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:emtr65$6b5$1@reader2.panix.com...
> In article <4vf1ffF1c13jbU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[3 more quoted lines elided]…
>>> In article <4vdr12F1botahU1@mid.individual.net>,
<snip>

>>As I don't have access to this environment I can't do it myself, but I'd 
>>be
…[14 more quoted lines elided]…
> --end quoted text

Ah, yes...I had overlooked that. Thanks for clarifying. It looks to me like 
RECFM=VB has to be a requisite (maybe RECFM=U, though I've not had any 
experience with that...). If it CAN be done with RECFM=FB, it'll be very 
interesting to see how...

Thanks for your time.

Pete.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-28T10:14:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<en05e7$qmf$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <4vf1ffF1c13jbU1@mid.individual.net> <emtr65$6b5$1@reader2.panix.com> <4vglitF1cepuaU1@mid.individual.net>`

```
In article <4vglitF1cepuaU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:emtr65$6b5$1@reader2.panix.com...

[snip]

>> Therein lies the difficulty, Mr Dashwood... as I understand the original
>> poster's request the LRECL of TESTA changes from one run to the next;
…[17 more quoted lines elided]…
>Thanks for your time.

You're most welcome, Mr Dashwood... would that the originator of this 
thread might be equally as gracious but... perhaps the due-date for this 
particular homework assignment has passed.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 25)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-12-29T06:50:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<en2abs$it4$01$1@news.t-online.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <4vf1ffF1c13jbU1@mid.individual.net> <emtr65$6b5$1@reader2.panix.com> <4vglitF1cepuaU1@mid.individual.net> <en05e7$qmf$1@reader2.panix.com>`

```
Doesn't help for mainframe presumably but MicroFocus
(also OpenCOBOL) have CBL_OPEN_FILE, CBL_READ_FILE,
CBL_WRITE_FILE, CBL_CLOSE_FILE calls to manipulate files at the
"raw" level without any SELECT/FD's.
The length is passed as a parameter to read any specific chunk.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 20)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-01-01T23:47:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u6jp29e9p4324g1d9rokj7t8q8otipbb6@4ax.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <4vdr12F1botahU1@mid.individual.net>`

```
On Wed, 27 Dec 2006 12:54:09 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I have a question, please, Doc.
>
…[35 more quoted lines elided]…
>>>> dealing with a fixed length dataset which has different-length records.

I (Clark Morris) interpreted the request as one that dealt with an
input file that was fixed block but depending on the day could have
different record lengths.  RECORD 0, BLOCK 0 handles that for input
with the interesting caveat that there must be  something in the data
that defines how long the actual record is (records with "A" in
position 1 are always 80 bytes while records with "B" in position 1
are always 3000 bytes).  When doing this the code must never attempt
to address parts of the record that are not there.  If the actual
record is only 80 bytes, the code actually working with that record
must not address the 200th byte.

>>
>> [snip]
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 19)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2006-12-26T19:57:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18530$4591c500$d066072d$7705@FUSE.NET>`
- **In-Reply-To:** `<emsa6g$n0j$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <2cafe$459199e9$d066072d$978@FUSE.NET>,
> CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
…[31 more quoted lines elided]…
> <http://groups.google.com/group/comp.lang.cobol/browse_thread/thread/5f5078dee2ab20f1/1418ce24a2de8ee3?q=%22BLOCK+0+and+the+actual+record+length%22&lnk=ol&>

Sorry, I jumped in based on your examples and the "Subject" line...
The 'input file' then, contains FIXED length records, but the program 
needs to anticipate the length of those differing fixed length files. 
[Hmmm, easy to handle in PL/I.]  Unless the records are somehow 
self-defining so ODO can be used in a single record definition, I think 
COBOL is going to always assume V format if it sees multiple, different 
length record definitions. [Ref back to Bill Klein's post on 12/21/06 
05:36 pm.]

I'll butt out...
CG
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 20)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-27T01:11:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emsh8d$j8m$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <18530$4591c500$d066072d$7705@FUSE.NET>`

```
In article <18530$4591c500$d066072d$7705@FUSE.NET>,
CG  <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> wrote:
>docdwarf@panix.com wrote:
>> In article <2cafe$459199e9$d066072d$978@FUSE.NET>,
…[38 more quoted lines elided]…
>needs to anticipate the length of those differing fixed length files. 

This is what I believe to be the case, aye... once again, the original 
poster's comments are few and far between.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 19)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-27T11:57:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rctkh.2714$sR.1230@newssvr29.news.prodigy.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com>`

```
> --begin quoted text:
>
…[6 more quoted lines elided]…
> --end quoted text

Sorry to be jumping in so late, and I apologize if this has already been 
suggested, but the answer is, "TESTA should not require definition in a 
COBOL FD."

Add an IDCAMS, IEBGENER or synsort/dfsort job step prior to this program to 
copy the file to a DISP=NEW (temp?) dataset ... with LRECL and BLKSIZE which 
***IS*** a known constant (in this case, probably VB) and therefore *can* be 
represented in a COBOL 01/FD. These utility programs should handle the 
multiple possible input formats transparently.

MCM
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 20)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-27T13:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emtrt6$an3$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net>`

```
In article <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
>> --begin quoted text:
>>
…[10 more quoted lines elided]…
>COBOL FD."

Now, now, Mr Mattias... saying 'This question is invalid' isn't always the 
best way to get a good grade on one's homework assignment, is it?

('Given the initial masses, positions and velocities and using Newton's 
Law of Gravity and Laws of Motion, determine the subsequent motions of 
three bodies.  Use both sides of the paper, if necessary.')

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 21)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-27T13:30:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Azukh.41497$wP1.30896@newssvr14.news.prodigy.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net> <emtrt6$an3$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote in message news:emtrt6$an3$1@reader2.panix.com...
> In article <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[13 more quoted lines elided]…
>> ... [straightforward solution to problem]...

> Now, now, Mr Mattias... saying 'This question is invalid' isn't always the
> best way to get a good grade on one's homework assignment, is it?

You sure have a strange way of saying, "Damn, I wish I had thought of that!"

(See also: today's post from yours truly in the "interview" thread re what 
consultants are actually paid to do).

MCM
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-27T13:58:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<emtu6l$plb$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net> <emtrt6$an3$1@reader2.panix.com> <Azukh.41497$wP1.30896@newssvr14.news.prodigy.net>`

```
In article <Azukh.41497$wP1.30896@newssvr14.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:emtrt6$an3$1@reader2.panix.com...
>> In article <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net>,
…[19 more quoted lines elided]…
>You sure have a strange way of saying, "Damn, I wish I had thought of that!"

So strange, Mr Mattias, that I've never posted it to this newsgroup.

>
>(See also: today's post from yours truly in the "interview" thread re what 
>consultants are actually paid to do).

I barely know what *I* have been paid to do, Mr Mattias, let alone 
'consultants'... now, has your own drum ceased misbehaving or do you see 
further need to beat it?

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 23)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-27T14:31:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctvkh.25607$Gr2.23388@newssvr21.news.prodigy.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <Rctkh.2714$sR.1230@newssvr29.news.prodigy.net> <emtrt6$an3$1@reader2.panix.com> <Azukh.41497$wP1.30896@newssvr14.news.prodigy.net> <emtu6l$plb$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote in message news:emtu6l$plb$1@reader2.panix.com...
> . now, has your own drum ceased misbehaving or do you see
> further need to beat it?

It had just been so long since I had posted I felt obliged to contribute.

Now if that contribution turns into a piece of shameless self-promotion, 
well... I guess it's not just the Irish who have luck, it's also the Polish 
kids from the South Side of Milwaukeee...... then again... 
http://www.friggatriskaidekaphobia.com/quotes.html

MCM
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-27T08:44:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2455p25b0d7efq4tg4k8bdrd1o6d3qa3ih@4ax.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com>`

```
Shops I was with used to use variable length files quite a bit until
around a couple of decades ago - when they switched to files with
header and detail records for variable data - which dominated for a
decade or so until they switched to external databases for the same
kind of data.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-28T14:43:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vglqlF1bn7ndU1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <db00b$45915999$d066072d$11570@FUSE.NET> <emrmnv$n8$1@reader2.panix.com> <2cafe$459199e9$d066072d$978@FUSE.NET> <emsa6g$n0j$1@reader2.panix.com> <2455p25b0d7efq4tg4k8bdrd1o6d3qa3ih@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:2455p25b0d7efq4tg4k8bdrd1o6d3qa3ih@4ax.com...
> Shops I was with used to use variable length files quite a bit until
> around a couple of decades ago - when they switched to files with
> header and detail records for variable data - which dominated for a
> decade or so until they switched to external databases for the same
> kind of data.

Yes, that is certainly my approach; let the DBMS sort it out...

Pete
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 15)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-01-01T23:38:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <lairo250619raljqhu1d545id7c5rbsan0@4ax.com> <emkk86$m9a$1@reader2.panix.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com>`

```
On Tue, 26 Dec 2006 13:26:38 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com>,
>Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
…[22 more quoted lines elided]…
>>supplied value against the external source.

This only works for input files. Since the WRITE statement refers to
records, it won't work for output.
>
>Hmmmmm... perhaps I am doing something wrong, Mr Morris... given
…[66 more quoted lines elided]…
>DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-02T02:13:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<encf48$kvk$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com>`

```
In article <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Tue, 26 Dec 2006 13:26:38 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[13 more quoted lines elided]…
>>>>>use RECORD 0 VARYING DEPENDING ON for fixed length records.  

[snip]

>>>If RECORD 0 is coded, then filling in of the field in the DCB is
>>>deferred to the OPEN.  Since LRECL in the program's DCB normally
…[6 more quoted lines elided]…
>records, it won't work for output.

>>
>>Hmmmmm... perhaps I am doing something wrong, Mr Morris... given
…[47 more quoted lines elided]…
>>,WRNG.LEN.RECORD,00000006000D00,QSAM

Mr Morris, in the code shown above the file is not addressed with a WRITE 
and encounters its ABEND based solely on input functions (OPEN INPUT and 
READ).  Also note the GET specified in the IGZ0002S message.

Second request, then:  Would you be so kind as to point out what you see 
as being the errors I've made in attempting to implement your 
suggestion? 

DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-01-02T07:02:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yrnmh.224296$0t1.104686@fe04.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com> <encf48$kvk$1@reader2.panix.com>`

```
DD,
  I wasn't one of the people who suggested this code (or approach) but do you 
get the same ABEND if your run-time JCL has:

//TESTA     DD  DSN=USERID.TESTA,DISP=SHR,DCB=(LRECL=32767,BLKSIZE=32767)

I *know* that your IEFBR14 created it with

//            DCB=(RECFM=FB,LRECL=30,BLKSIZE=27990)

but I *do* have a vague memory of being able to override LRECL via a DCB for an 
INPUT file.  If this approach DOES work, then the next question would be if it 
would work with a "real" input file rather than just a "marker" file created 
with IEFBR14.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 18)_

- **From:** "coot_jg" <breany@csc.com>
- **Date:** 2007-01-02T07:25:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167751524.129289.7460@n51g2000cwc.googlegroups.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com> <encf48$kvk$1@reader2.panix.com> <Yrnmh.224296$0t1.104686@fe04.news.easynews.com>`

```

William M. Klein wrote:
> DD,
>   I wasn't one of the people who suggested this code (or approach) but do you
…[12 more quoted lines elided]…
>

   Just out of curiosity, we were previously able to solve this - but I
am not aware as to whether the solution is still implementable.  The
input file records were created as fixed - (no leading length attribute
on each record/block) - and all records within a particular file had an
identical length, so we asked the console (or a parameter file/card)
for the required length(s). Prior to issuing an "OPEN" for the FD, we
issued a "CALL" to the COBOL program "TAMPER", passing the FD name  and
the record length(s) as  parameters.
   The "TAMPER" routine received a pointer to the DCB of the calling
program as it's first parameter, and was able to set the parameters
within that DCB to match the record length/block sizes to the expected
values, and pass the modified DCB back to the calling program for a
successful "OPEN".

    If this isn't valid anymore, I'd be curious as to the reason.

Thanx in advance.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-01-02T19:35:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vuymh.244742$6O4.69602@fe09.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <nf0to21l7sn57s6qjkocj493emf0bgfiv4@4ax.com> <emr7ue$r19$1@reader2.panix.com> <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com> <encf48$kvk$1@reader2.panix.com> <Yrnmh.224296$0t1.104686@fe04.news.easynews.com> <1167751524.129289.7460@n51g2000cwc.googlegroups.com>`

```
"coot_jg" <breany@csc.com> wrote in message 
news:1167751524.129289.7460@n51g2000cwc.googlegroups.com...
>
> William M. Klein wrote:
<snip>
>   Just out of curiosity, we were previously able to solve this - but I
> am not aware as to whether the solution is still implementable.  The
…[15 more quoted lines elided]…
>

As an IBM extension, one may pass the FD-name to a subroutine *IF* the file is a 
"QSAM" (I think this also works for SAM on VSE, but won't swear to it) file. 
This passes the address of the DCB, so a subprogram (usually - but not required 
to be - Assembler) can "play" with the attributes.  With OS/VS COBOL, one could 
also pass the FD-name of a VSAM file to get the ACB accessed in a subprogram. 
This is NO LONGER valid syntax (and will get a compile error) with all IBM 
compilers since VS COBOL II.

I think I suggested this approach early on (when we still thought the original 
poster was paying attention <G>)
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-02T16:33:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ene1g3$hih$1@reader2.panix.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com> <encf48$kvk$1@reader2.panix.com> <Yrnmh.224296$0t1.104686@fe04.news.easynews.com>`

```
In article <Yrnmh.224296$0t1.104686@fe04.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>DD,
>  I wasn't one of the people who suggested this code (or approach) but do you 
>get the same ABEND if your run-time JCL has:
>
>//TESTA     DD  DSN=USERID.TESTA,DISP=SHR,DCB=(LRECL=32767,BLKSIZE=32767)

JCL error.  Given:

//TESTA    DD DSN=USERID.TESTA,              
//            DISP=(SHR),                     
//            DCB=(LRECL=32767,BLKSIZE=32767) 

... I get:

IEF638I SPECIFIED NUMERIC EXCEEDS MAXIMUM ALLOWED IN THE LRECL 
SUBPARAMETER OF THE DCB FIELD

[snip]

><docdwarf@panix.com> wrote in message news:encf48$kvk$1@reader2.panix.com...
>> In article <6p6jp2drgef3s0503ku600qmer9hnu9jqh@4ax.com>,
…[89 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-22T09:47:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12onvfo5m3vhv58@news.supernews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com>`

```
Alistair wrote:
>
> ALTERNATIVELY (and I like this one): set the FD to contain a record of
…[3 more quoted lines elided]…
> I can't believe that no-one came up with that one before me.

I did this once. The overhead was incredible.

We deal with this problem routinely. Here's how.

1. Set the starting byte to 0.
2. Do a physical read of the disk at START-BYTE for MAX-LENGTH.
3. Examination of the buffer tells us what kind of type to process and that 
type determines the length of the record. For example, the record consists 
of everything from START-BYTE to, and including, a trailing double-tab or 
smiley-face. Whatever.
4. Add that length to START-BYTE.
5. Repeat steps 1-4 until coffe break time.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-22T21:04:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZLXih.85351$Ea5.58813@fe05.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <12onvfo5m3vhv58@news.supernews.com>`

```
Remember, the original question indicated the input was on TAPE.  I don't think 
this will work
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 10)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-22T18:08:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12oosspc73k9td1@news.supernews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <12onvfo5m3vhv58@news.supernews.com> <ZLXih.85351$Ea5.58813@fe05.news.easynews.com>`

```
William M. Klein wrote:
> Remember, the original question indicated the input was on TAPE.  I
> don't think this will work
>

Right. Add a step 0, viz:

0. Copy tape file to disk.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-23T05:47:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166881635.109514.15430@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<12onvfo5m3vhv58@news.supernews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <12onvfo5m3vhv58@news.supernews.com>`

```

HeyBub wrote:
> Alistair wrote:
> >
…[6 more quoted lines elided]…
> I did this once. The overhead was incredible.

I expected that. Perhaps I should have put an emoticon showing tongue
firmly implanted in cheek? Just for curiosity, what order of magnitude
difference did it make?

>
> We deal with this problem routinely. Here's how.
…[8 more quoted lines elided]…
> 5. Repeat steps 1-4 until coffe break time.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-23T09:35:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4v2ts1F1a8t10U1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1166790950.351244.67040@42g2000cwt.googlegroups.com...
>
> Alex Flinsch wrote:
…[32 more quoted lines elided]…
>
Merry Xmas, Alistair!

Pleased to see you haven't lost your sense of humour... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-23T05:50:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166881842.951192.324380@42g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<4v2ts1F1a8t10U1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <4v2ts1F1a8t10U1@mid.individual.net>`

```

Pete Dashwood wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1166790950.351244.67040@42g2000cwt.googlegroups.com...
…[11 more quoted lines elided]…
> Pete.

Sense of humour? What sense of humour? I'm just a miserable old git
with an occasional need to misdirect others.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-22T21:07:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rOXih.64130$0t1.37143@fe04.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com>`

```
Again, I don't think this will work for TAPE input.  Also, remember that IBM 
processing of "RECFM U" *has* changed in recent years.  See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3MG31/3.5.4
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-23T05:55:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166882146.914548.50570@80g2000cwy.googlegroups.com>`
- **In-Reply-To:** `<rOXih.64130$0t1.37143@fe04.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <rOXih.64130$0t1.37143@fe04.news.easynews.com>`

```

William M. Klein wrote:
> Again, I don't think this will work for TAPE input.  Also, remember that IBM
> processing of "RECFM U" *has* changed in recent years.  See:
>
>  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3MG31/3.5.4
>

Bill, the initiator's four posts on this subject do not mention TAPE.
Where did you get the idea that he is referring to tape?
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-23T19:28:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wrfjh.82583$b%6.4029@fe10.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <rOXih.64130$0t1.37143@fe04.news.easynews.com> <1166882146.914548.50570@80g2000cwy.googlegroups.com>`

```
I must have been mixing it up (in my mind) with another post.  Sorry about that.
```

###### ↳ ↳ ↳ Re: Variable Length Input File

_(reply depth: 11)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-12-23T14:54:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1166914455.419452.290080@48g2000cwx.googlegroups.com>`
- **In-Reply-To:** `<Wrfjh.82583$b%6.4029@fe10.news.easynews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <emeht0$cdh$1@reader2.panix.com> <1166725014.449314.160860@i12g2000cwa.googlegroups.com> <emejdb$bl9$1@reader2.panix.com> <1166727602.664630.95240@48g2000cwx.googlegroups.com> <65Gih.13245$RR4.7129@newsfe22.lga> <pan.2006.12.22.11.07.20.959975@att.net> <1166790950.351244.67040@42g2000cwt.googlegroups.com> <rOXih.64130$0t1.37143@fe04.news.easynews.com> <1166882146.914548.50570@80g2000cwy.googlegroups.com> <Wrfjh.82583$b%6.4029@fe10.news.easynews.com>`

```

William M. Klein wrote:
> I must have been mixing it up (in my mind) with another post.  Sorry about that.

No problem, I just thought that I was missing the obvious. Thanks.




>
> --
…[14 more quoted lines elided]…
> >
```

#### ↳ Re: Variable Length Input File

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-12-29T03:25:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167391514.358575.44820@i12g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`

```

manubay@pacbell.net wrote:
> Is there a way in Cobol to handle an input file that has variable
> LRECL?  If there is, how would it be defined in the FD section?  Thank
> you.

I wrote a program in 1979 with the folowing input FDs, on an IBM
mainframe, presumably with OS/VS2 COBOL.


* fixed length record FD
FD  FILE1
    RECORDING MODE IS F
    LABEL RECORDS ARE STANDARD
    BLOCK CONTAINS 0 RECORDS
    RECORD CONTAINS 0 CHARACTERS.
01  IFAREC.
    03  IFABYTE             PIC X           OCCURS 10000.
    SKIP3
* variable length record FD
FD  VILE1
    RECORDING MODE IS V
    LABEL RECORDS ARE STANDARD
    BLOCK CONTAINS 0 RECORDS
    RECORD CONTAINS 0 CHARACTERS.
01  IVAREC.
    03  IVABYTE             PIC X           OCCURS 10000.
    SKIP3

It was still working in the late 1980s.

It is quite likely that it would still work, though the current
standard and maybe the 1985 one too, has made the RECORDING MODE
clause obsolete (as well as the LABEL clause), thereby apparently
making it impossible for the compiler to usefully detect whether the
mode is fixed or variable in these cases. However,  IBM still permits
their use as an extension, but for how long and whether with the same
effect, I don't know.

A format 3 RECORD clause (aa per 2002 standard) might do the trick
depending on the compiler (as the standard says that it is implementor
defined how it is actually implemented with respect to some of hte
details)
i.e.

RECORD CONTAINS integer-4 TO integer-5 CHARACTERS, where integer-4 must
be greater than or equal to zero (anyone like to tell me how to
detect/write a zero length record, when it doesn't have a 4byte RDW and
what its use might be!) and integer-5 must be greater than integer-4.
This construct might make it possible for the same FD statement to read
either fixed or variable record length files for some implementors.


Robert
```

#### ↳ Re: Variable Length Input File

- **From:** "Vivian" <vsaegesser@infogix.com>
- **Date:** 2006-12-29T08:01:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167408108.184588.285750@79g2000cws.googlegroups.com>`
- **In-Reply-To:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com>`

```

manubay@pacbell.net wrote:
> Is there a way in Cobol to handle an input file that has variable
> LRECL?  If there is, how would it be defined in the FD section?  Thank
> you.

.........
The problem is all inside your head
She said to me
The answer is easy if you
Take it logically
I'd like to help you in your struggle
........

Sorry, the song got stuck in my head while reading through this
one......

The answer is to find yourself a real veteran, do it in assembler on
the mainframe, and call the assembler routine from your cobol program.
```

##### ↳ ↳ Re: Variable Length Input File

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-12-30T12:56:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vlo9hF1coksiU1@mid.individual.net>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1167408108.184588.285750@79g2000cws.googlegroups.com>`

```

"Vivian" <vsaegesser@infogix.com> wrote in message 
news:1167408108.184588.285750@79g2000cws.googlegroups.com...
>
> manubay@pacbell.net wrote:
…[17 more quoted lines elided]…
>

It's really not my habit to intrude
Furthermore, I hope my meaning won't be lost or misconstrued
But speaking as such a veteran
And not meaning to be rude,

I wouldn't use Assembler as a solution.

Check out the post from Michael Matthias on this (MCM), 28/12/2006 in this 
thread.

As for you, Vivian, get over it... there's more than 50 ways :-)

Pete.
```

##### ↳ ↳ Re: Variable Length Input File

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-12-29T19:18:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12pbfjk4ikjkf9@news.supernews.com>`
- **References:** `<1166720886.579682.68830@42g2000cwt.googlegroups.com> <1167408108.184588.285750@79g2000cws.googlegroups.com>`

```
Vivian wrote:
>
> The answer is to find yourself a real veteran, do it in assembler on
> the mainframe, and call the assembler routine from your cobol program.

I remember when we our company read (appx. it varies) 250,000 byte records, 
spilling them to disk, demultiplexing, and applying binary gain, on a 
machine with only 64K of core.

It was done with channel programming by a "veteran." He was paid (in today's 
dollars) about $100/minute.

Some don't have the resources to devote to a piddly problem like a maverick 
tape file issue.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
