[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NEWBIE PROBLEM

_24 messages · 15 participants · 1999-08_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### NEWBIE PROBLEM

- **From:** "Calatis" <nmourapires@mail.pt>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
Hello,

i am a newbie using cobol under MVS system.
I have this problem: i have 4 input files that i want to work and 1 output
file.

The name of this files depend on the date. Here is an exemple of the name of
the file:  SLP.SIN.SPOUT.D990830.T2233.

My problem is how to open a file that i don't know the name before i execute
the program.

Can anyone help me? Some code would be useful.

Thank in advanced.

Nuno
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37AEF9F6.C53567A0@NOSPAMhome.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
Calatis wrote:
> 
> Hello,
…[6 more quoted lines elided]…
> the file:  SLP.SIN.SPOUT.D990830.T2233.

First, the recommended way of using the Web to ask for help is to think
of a Subject line which keys others into your problem.  "Newbie problem"
doesn't get scanners to stop and read your request.  You mentioned your
operating system - that was needed, but for COBOL problems, you should
also mention your compiler.

I don't have a Cobol solution for your problem.

The simplest solution is to have the operator or whomever submits the
job, pass a symbolic override for that portion of the file name.

A more complicated method is to have two jobs.  The first job creates
the either the JCL or a proc or a JCL copy member with the file name in
it (This can be a COBOL program).  The second job is the one with the
modified JCL or proc.  

I suspect there's a more direct solution using JES CA7.
```

##### ↳ ↳ Re: NEWBIE PROBLEM: File with date component

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rqLr3.1038$Co3.11032@news1.mia>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AEF9F6.C53567A0@NOSPAMhome.com>`

```
CA7 does NOT have a solution.

Either have REXX write the info as a proc (not likely you'll be allowed to
do this)
or you need an assembler subroutine that DYNAMICALLY ALLOCATES the files.

If your site doesn't have one, I have one I wrote and use (24 and 31 bit
versions: the
24 bit can be invoked directly via JCL to read SYSIN and DELETE / CREATE a
file)
also the COBOL COPYBOOKS to CALL it and verify results.

I'd be willing to license it to your company for a reasonable price ( I
wrote it for myself)
Let me know if your interested.

Howard Brazee wrote in message <37AEF9F6.C53567A0@NOSPAMhome.com>...
>Calatis wrote:
>>
…[3 more quoted lines elided]…
>> I have this problem: i have 4 input files that i want to work and 1
output
>> file.
>>
>> The name of this files depend on the date. Here is an exemple of the name
of
>> the file:  SLP.SIN.SPOUT.D990830.T2233.
>
…[16 more quoted lines elided]…
>I suspect there's a more direct solution using JES CA7.
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** jdeez@my-deja.com
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7on5po$q9d$1@nnrp1.deja.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
There really isn't a way to declare the actual file name in cobol.  The
JCL contains this information as you have seen from the other posts.

In the MVS environment there is a great file management system called
Generation Data Sets.  If you can get the system folks to build the
base and the rest of the system to agree this would eliminate the
dependancy on the date in the file name.

Otherwise the job will have to be modified each run to get the date in
the file name.  See other posts for this method.

> I have this problem: i have 4 input files that i want to work and 1
output
> file.
>
> The name of this files depend on the date. Here is an exemple of the
name of
> the file:  SLP.SIN.SPOUT.D990830.T2233.
>
> My problem is how to open a file that i don't know the name before i
execute
> the program.
>
…[6 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: NEWBIE PROBLEM

- **From:** "Ralph Coleman" <rocolema@home.com>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A0FDF5951E2E1C89.10A9015D7905273F.49DBDEC8BA4C77F5@lp.airnews.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <7on5po$q9d$1@nnrp1.deja.com>`

```
You will be able to do this in the next iteration of COBOL (probably due out
within the next decade).
<jdeez@my-deja.com> wrote in message news:7on5po$q9d$1@nnrp1.deja.com...
> There really isn't a way to declare the actual file name in cobol.  The
> JCL contains this information as you have seen from the other posts.
…[31 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7on8c5$oah@netnews1.apci.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <7on5po$q9d$1@nnrp1.deja.com> <A0FDF5951E2E1C89.10A9015D7905273F.49DBDEC8BA4C77F5@lp.airnews.net>`

```
The file name given as an example looks suspiciously like one that has been
assigned by the operating system in the first place.
SLP.SIN.SPOUT.D990830.T2233 is a file that was created in proc SLP, step
SIN, ddname SPOUT which was interpreted by the initiator on 990830 time
2233.  If step SIN is a previous step in the job containing the program you
are trying to run, why not just declare access to it as:
//FILEIN DD DSN=*.SIN.SPOUT,DISP=(OLD,DELETE,KEEP)
and then process the file FILEIN in your COBOL program?

Ralph Coleman wrote in message ...
>You will be able to do this in the next iteration of COBOL (probably due
out
>within the next decade).
><jdeez@my-deja.com> wrote in message news:7on5po$q9d$1@nnrp1.deja.com...
…[35 more quoted lines elided]…
>
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37AEE29C.680C5F43@zip.com.au>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
Calatis wrote:
> 
> Hello,
…[15 more quoted lines elided]…
> Nuno

The simple answer is that you cannot.

Now the hard answer.

1.  You can tune up your assembler and write an exit to SVC99 to
allocate a DD name that the cobol program knows about (not recommended
too unsupportable I have done it and it confuses most operators).

2.  You can write a program that writes a JCL out and use
SYSOUT=(,INTRDR) on that DD.  This automatically submits the built
JCL. Consider using ISPF and file tailoring to do it.

3.  Get the scheduling package that you own to do it.  These are add
ons and have names like OPC, JCLTRAC, etc.  Check you Ops division.

Ken
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37AFAF97.3043FD1@earthlink.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
Nuno,

COBOL is not designed to address this kind of processing. You need a
language with a macro processor, e.g. PL/I or SAS. It is unlikely that you
have PL/I in your org, which is infortunate, since as a general programming
language, PL/I is unbeatable. However, you should definitely have SAS;
virtually any MVS shop has it, if not for production data processing at
large, then for processing SMF records. The latter, because of their
complexity, are never attempted to process in anything but SAS, whose
input/output flexibility far exceeds that of _any_ existing programming
language. What I am saying is, COBOL is a venerable and great (for what it
can do right) programming language, but your task is out of its league.

//<job card and stuff>
// EXEC SAS,OPTIONS='ERRORABEND'
//SYSIN DD *,DLM='$$'
/* Assign ddname to file with current date */
FILENAME FILE1 "SLP.SIN.SPOUT.D%SYSFUNC(DATE(),YYMMDD6.).T2233" DISP=SHR;

/*.....Similar for the rest of the files.....*/
/* Now you can use FILE1-FILE4 as you would ddnames in the program */
/* Say you want to copy FILE1 to the output file */
/* Next 2 statements do the same iefbr14 would */ 
/* The 3d allocates output. Do it all in JCL if you wish */ 
FILENAME OUTPUT "NUNO.OUTPUT" DISP=(MOD,DELETE);
FILENAME OUTPUT CLEAR;
FILENAME OUTPUT "NUNO.OUTPUT" DISP=(NEW,CATLG,DELETE) RECFM=FB LRECL=100
BLKSIZE=0 SPACE=(CYL,(5,10),RLSE) UNIT=3390;
/* Copy FILE1 to OUTPUT */
DATA _NULL_;
   INFILE FILE1;
   INPUT;
   FILE OUTPUT;
   PUT _INFILE_;
RUN;

The example is simplistic but gives you an idea why, when it comes to MVS,
SAS programmers run circles around it. This is just the tip of a giant SAS
iceberg. Let's admit it, a well tuned COBOL program  would run faster than
SAS code doing the same job (usually, at the expense of zillion times more
lines of code), but a fairly dumb SAS guy would be done with the kind of
problem you are asking for long before the brightest COBOL guru would merely
sift through possibilities, and this thread corroborates it. 
A friend of mine, one of the best big iron guys I know, has a notion of a
"proficient mainframe programmer": one cannot be proficient without being
proficient in COBOL _and_ SAS. 

Kind regards,
=====================
Paul M. Dorfman
Jacksonville, FL
=====================           
  
            

Calatis wrote:
> 
> Hello,
…[15 more quoted lines elided]…
> Nuno
```

##### ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37AFBCAA.E7BC598C@home.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net>`

```
Paul M. Dorfman wrote:
> 
> Nuno,
…[10 more quoted lines elided]…
> can do right) programming language, but your task is out of its league.

Paul, 

Don't dispute your statement because I just don't know. Has somebody the
patience to put this in non-mainframe talk ? Do you mainframers agree
with Paul. Don't forget if you answer, don't put it in
mainframe-gobbledygook. Just seems depressing that this should be a
problem for COBOL - back to Standards if you like - what is COBOL as a
language missing to achieve this - or is this a problem related solely
to a specific operating platform ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com>`

```
On Tue, 10 Aug 1999 05:39:00 GMT, "James J. Gavan" <jjgavan@home.com>
enlightened us:

>Paul M. Dorfman wrote:
>> 
…[23 more quoted lines elided]…
>Jimmy, Calgary AB

Can't answer specifically because I didn't see the question that Paul
answered.  However, given his answer I can say there are certain
things that Cobol cannot do, but there are pre-processors that format
those things for Cobol.  For example CICS Commands and SQL commands.

Also Paul neglected to include Assembler in his list which also has
the ability to process macroes.  And it appears he is a PL/1 bigot
anyway since he stated that as a general programming language it is
unbeatable.  I think the debate about that and Cobol has been waged in
this newsgroup more than once and is not worth rehashing here.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Some days your the dog.  Some days your the hydrant.


 Steve
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 4)_

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B0AD00.8C06B2B7@earthlink.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net>`

```
SkippyPB wrote:
> 
> On Tue, 10 Aug 1999 05:39:00 GMT, "James J. Gavan" <jjgavan@home.com>
…[32 more quoted lines elided]…
> those things for Cobol.  For example CICS Commands and SQL commands.

Right. I never said this cannot be done by external means. But processing
files with data driven names is a quite common business DP task, and if the
principal business-oriented language does not provide a non-convoluted way
of accomplishing the task internally, it is an omission, to put it mildly.
     
> Also Paul neglected to include Assembler in his list which also has
> the ability to process macroes. 

Why should I compare apples to oranges? COBOL is a 3GL. 

> And it appears he is a PL/1 bigot anyway

No more than that of COBOL, SAS, COBOL, FORTRAN, C, or whatever else gets
the job done.   

> anyway since he stated that as a general programming language
> it is unbeatable.

To me, PL/I strikes the best balance between COBOL as too wordy and C as too
cryptic. Plethora of features and the macro processor (the reason it was
mentioned in the first place) give it an extra leverage. "Unbeatable" is
probably too strong a word but, frankly, no stronger than "bigot".  

>Cobol has been waged in this newsgroup more than once and is not worth rehashing here.

Couldn't agree more.

Kind regards,
+++++++++++++++++
Paul M. Dorfman
Jacksonville, FL
+++++++++++++++++
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B17948.7890A747@NOSPAMhome.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net>`

```
> > anyway since he stated that as a general programming language
> > it is unbeatable.
…[4 more quoted lines elided]…
> probably too strong a word but, frankly, no stronger than "bigot".

With the thousands of languages out there, it would be an assumption if
it was "unbeatable" using those criteria.  Other criteria, such as
availablity of programmers for now and in the future and how much access
to the nitty gritty you want programmers to have could also make it a
compromise ("strikes the best balance") between COBOL and C as well.
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 5)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net>`

```
On Tue, 10 Aug 1999 18:51:44 -0400, "Paul M. Dorfman"
<sashole@earthlink.net> enlightened us:

>SkippyPB wrote:
>> 
…[39 more quoted lines elided]…
>     

I'm not sure what you mean about processing files with data driven
names.  It was probably in the original post which I didn't see.
However, if it means what I think it means, in my company we developed
a data dictionary that is accessible from Cobol and has file
definitions as well as element definitions and record layouts.  Maybe
this is not the same.

>> Also Paul neglected to include Assembler in his list which also has
>> the ability to process macroes. 
…[15 more quoted lines elided]…
>
Right.  I should have said biased.  The problem with PL/1 is that
there just aren't as many programmers that know it or shops that use
it.  IBM didn't market it well and many colleges didn't pick it up to
teach it.  I've programmed in it and had to learn it just by reading
code.  Since it is farily close to Cobol, that wasn't too dificult.
But I still prefer Cobol.

>>Cobol has been waged in this newsgroup more than once and is not worth rehashing here.
>
…[6 more quoted lines elided]…
>+++++++++++++++++

Cheers
          ////
         (o o)
-oOO--(_)--OOo-

Some days your the dog.  Some days your the hydrant.


 Steve
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7osmf2$hf2@dfw-ixnews10.ix.netcom.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net> <084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net>`

```
SkippyPB <swiegand@neo.rr.com> wrote in message
  <snip>
> >
> Right.  I should have said biased.  The problem with PL/1 is that
…[4 more quoted lines elided]…
> But I still prefer Cobol.

Interestingly enough - like Paragraphs versus Sections - this is a
"continental" thing. (Gross oversimplification - but mostly true.)  PL/I
(IBM's - not ANSI/ISO conforming) is really almost as common as COBOL in
large European IBM mainframe shops. (In some areas, it is MORE common.)  On
the other hand, in the US, it really is less common (but hardly unusual).
In "yet bad olde days" - when IBM tried to "market" SAA, the fact that RPG
was an SAA language - but PL/I was NOT caused various fits of humor and
dismay.

Having said that, I will say "let's NOT get into another language war" in
this NG.
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 7)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A7E9B75FFF1F944.F1BB79B0B418F9F2.8AA2E4E70A423583@lp.airnews.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net> <084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net> <7osmf2$hf2@dfw-ixnews10.ix.netcom.com>`

```
On Wed, 11 Aug 1999 15:30:39 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> enlightened us:

>SkippyPB <swiegand@neo.rr.com> wrote in message
>  <snip>
…[16 more quoted lines elided]…
>

Absolutely right.  In fact it was while I was working in Europe that I
had to learn PL/1.  Before that I had only heard about it but had
never actually seen it.  After that I heard about about many whole
systems running in Europe that were in PL/1.


>Having said that, I will say "let's NOT get into another language war" in
>this NG.

Amen to that brother!

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I finally got my head together, now my body is falling apart.


 Steve
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 6)_

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B1ED45.DB38223@earthlink.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net> <084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net>`

```
SkippyPB wrote:
> 
> On Tue, 10 Aug 1999 18:51:44 -0400, "Paul M. Dorfman"
…[41 more quoted lines elided]…
> this is not the same.

I mean that the name(s) and/or other characteristic(s) of output file(s)
(such as type, DCB, disposition, space, unit, layout) are determined at the
run-time. They may depend on data contained in the input, obtained as a
result of input processing, computations, etc. The simplest case, an output
file name comprising a date (system or computed) as its part, was the
subject of the original posting.

The most versatile package I know of that makes all such things elementary,
is SAS. In addition, one can issue any operating system commands, run any
utilities (e.g. IDCAMS, etc., SyncSort, you name it) straight from within
the program. However, it may have a dangerous effect on performance in the
hands of one approaching SAS as a user (as opposite to a programmer). In the
days of yore, it was possible to augment it by writing custom SAS procs in
PL/I (since SAS itself was written in PL/I; it is C now). That was a real
godsend.           

> >To me, PL/I strikes the best balance between COBOL as too wordy and C as too
> >cryptic. Plethora of features and the macro processor (the reason it was
…[8 more quoted lines elided]…
> But I still prefer Cobol.

Kind regards,
=================
Paul M. Dorfman
Jacksonville, FL 
=================
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 7)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4518A43649DC8AD1.7A20B440EFEF8C37.EC8B63BCC1A65E7B@lp.airnews.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net> <084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net> <37B1ED45.DB38223@earthlink.net>`

```
On Wed, 11 Aug 1999 17:38:13 -0400, "Paul M. Dorfman"
<sashole@earthlink.net> enlightened us:

>SkippyPB wrote:
>> 
…[50 more quoted lines elided]…
>
As was pointed out in another thread, this can be done from Cobol by
invoking TSO/E services in MVS.  The problem I see of this being a
native thing in Cobol is that the language would have to be tied to
closely to the operating system.  If you look at Cobol written for VSE
and Cobol written for MVS, there are very few differences.  In fact
off the top of my head the only differences I can think of are in the
Data Division and Configuration Section.  


>The most versatile package I know of that makes all such things elementary,
>is SAS. In addition, one can issue any operating system commands, run any
…[6 more quoted lines elided]…
>
Not knowing SAS it is hard to comment, but are those things
accomplished through native SAS verbs or through calls to other
services?  Regardless, while not native in Cobol, all those things can
be accomplished by calls from Cobol to other services or Assembler sub
routines.



>> >To me, PL/I strikes the best balance between COBOL as too wordy and C as too
>> >cryptic. Plethora of features and the macro processor (the reason it was
…[14 more quoted lines elided]…
>=================

          ////
         (o o)
-oOO--(_)--OOo-

I finally got my head together, now my body is falling apart.


 Steve
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 8)_

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B77217.BEFC4941@earthlink.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net> <084CF0E874F71BCA.DB24EC40A6417818.B685FA5E8724D46D@lp.airnews.net> <37B1ED45.DB38223@earthlink.net> <4518A43649DC8AD1.7A20B440EFEF8C37.EC8B63BCC1A65E7B@lp.airnews.net>`

```
SkippyPB wrote:
> 
> On Wed, 11 Aug 1999 17:38:13 -0400, "Paul M. Dorfman"
…[77 more quoted lines elided]…
> 

They are accomplished through native SAS constructs: Either FILENAME
statement in the open code, or FILENAME function in the DATA step and Macro
Language. There are also DSNEXIST statement and functions FILEEXIST and
FEXIST verifying the existence of a file based either on its physical name
or DD name (for all the above environments). There are functions that
interrogate the attributes of the file, and so on. However, if one prefers
to do all these things using TSO (or UNIX shell, or Windows) commands, they
can be issued from anywhere (but procs) as X-statement, SYSTEM statement,
SYSTEM call routine, TSO statement (if MVS) - the choice is yours. OS
Utilities can be run from a SAS program in the same manner SAS procs are.
SAS log issues messages informing what program external to SAS has executed.
Consequently, _everything_ that can be done in JCL can be done from within a
SAS program on the fly, of course, including writing to the internal reader.

Kind regards,
===================
Paul M. Dorfman
Jacksonville, Fl
===================
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM (Enlighten me)

_(reply depth: 5)_

- **From:** Lawrence Allen Free <free@mcs.com>
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p7n6o$15b$1@Nntp1.mcs.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <37AFAF97.3043FD1@earthlink.net> <37AFBCAA.E7BC598C@home.com> <2F5E6CB0FB7EC20B.A32B7500D3CDF652.E966BBD9ED1450BA@lp.airnews.net> <37B0AD00.8C06B2B7@earthlink.net>`

```
In non-mainframe COBOL's such as MF/ACU/RM where you can
name the file in the program using a variable, one can simply search
a sequence of file names by attempting OPENs and checking status
codes.  It is not efficient, but it does work.  In the mainframe 
environment, I believe you must specify the name in JCL prior to
entering the program.  This is not really a COBOL issue as it is an
operating platform issue.

In article 37B0AD00.8C06B2B7@earthlink.net,
	"Paul M. Dorfman" <sashole@earthlink.net> said:
>
>SkippyPB wrote:
…[99 more quoted lines elided]…
>
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7opb6j$b2a$1@nnrp1.deja.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
In article <7om98n$cjl$1@pthp35.telecom.pt>,
  "Calatis" <nmourapires@mail.pt> wrote:
> My problem is how to open a file that i don't know the name before i
execute the program.

You may dynamically allocate a file with a dataset name of your choice
using the TSO/E programming services IKJTSOEV and IKJEFTSR.

The IKJTSOEV subroutine may be called once to set up the TSO/E
environment, and then  IKJEFTSR can be called as often as you like to
perform TSO commands.  The command you would use is ALLOCATE.

Let me know if you would like a sample program.

-Art


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: NEWBIE PROBLEM

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B107EF.8184BA67@att.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <7opb6j$b2a$1@nnrp1.deja.com>`

```
Art Perry wrote:
> 
(snip)
> 
> You may dynamically allocate a file with a dataset name of your choice
…[6 more quoted lines elided]…
> Let me know if you would like a sample program.

Don't know about the original poster, but I sure would.

TIS,
Bill Lynch

(delete "spam." if you want to use my reply address)
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7os6q5$dka$1@nnrp1.deja.com>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <7opb6j$b2a$1@nnrp1.deja.com> <37B107EF.8184BA67@att.net>`

```
In article <37B107EF.8184BA67@att.net>,
  WBLynch@att.spam.net wrote:
> Art Perry wrote:
> > Let me know if you would like a sample program.
>
> Don't know about the original poster, but I sure would.

This is a post from the IBM-MAIN mailing list from several months ago:

Gilbert Saint-flour <gsf@ibm.net> wrote:
You don�t need an assembler sub-routine to perform dynamic allocations
in COBOL.  You can issue the TSO ALLOCATE command directly from your
COBOL program; please see:
http://x14.dejanews.com/[ST_rn=ps]/getdoc.xp?AN=444695526
Gilbert Saint-flour <gsf@ibm.net>

Here is a sample COBOL program that invokes the TSO ALLOCATE command to
dynamically allocate a SYSOUT data set.  You could use the same
technique
to dynamically allocate permanent data sets.Hope this helps.
Gilbert Saint-flour <gsf@ibm.net> //IBMUSERJ JOB (ACCT#),COB2TSO,
 // NOTIFY=&SYSUID, // CLASS=A,MSGCLASS=X,COND=(0,NE)
 //*--------------------------------------------------------------------
*
 //*
*
 //*   This sample program illustrates how to invoke TSO
*
 //*   commands from a COBOL program.  The TSO services used
*
 //*   are documented in the TSO/E Programming Services manual.
*
 //*
*
 //*--------------------------------------------------------------------
*
 //COB2 EXEC PGM=IGYCRCTL  CBL NOLIB,APOST,NODECK,OBJECT,NOSEQ,BUF
(32760),DYNAM
  CBL NOMAP,NOLIST,NOOFFSET,NOXREF         Identification Division.
          Program-ID. CB2TSOEV.
          Author. Gilbert Saint-flour <gsf@ibm.net>.         Data
Division.
         Working-Storage Section.          01 Filler.
            05 ws-dummy        Pic s9(8) Comp.
            05 ws-return-code  Pic s9(8) Comp.
            05 ws-reason-code  Pic s9(8) Comp.
            05 ws-info-code    Pic s9(8) Comp.
            05 ws-cppl-address Pic s9(8) Comp.
            05 ws-flags        Pic X(4) Value X'00010001'.
            05 ws-buffer       Pic X(256).
            05 ws-length       Pic s9(8) Comp Value 256.
        Procedure Division.             CALL 'IKJTSOEV' Using ws-dummy
                                  ws-return-code
                                  ws-reason-code
                                  ws-info-code
                                  ws-cppl-address.
            IF ws-return-code > zero
              DISPLAY 'IKJTSOEV Failed, Return-code=' ws-return-code
                                      ' Reason-code=' ws-reason-code
                                      'Info-code='    ws-info-code
              MOVE ws-return-code to Return-code              STOP RUN.
            MOVE 'ALLOCATE DD(SYSPUNCH) SYSOUT HOLD' to ws-buffer.
            CALL 'IKJEFTSR' Using ws-flags
                                  ws-buffer
                                  ws-length
                                  ws-return-code
                                  ws-reason-code
                                  ws-dummy.            IF ws-return-
code > zero
              DISPLAY 'IKJEFTSR Failed, Return-code=' ws-return-code
                                      ' Reason-code=' ws-reason-code
              MOVE ws-return-code to Return-code              STOP RUN.
            DISPLAY 'ALLOCATE Worked ! ' Upon Syspunch.
STOP RUN. /*
 //SYSPRINT DD SYSOUT=* //SYSUT1 DD UNIT=VIO,SPACE=(TRK,1)
 //SYSUT2 DD UNIT=VIO,SPACE=(TRK,1) //SYSUT3 DD UNIT=VIO,SPACE=(TRK,1)
 //SYSUT4 DD UNIT=VIO,SPACE=(TRK,1) //SYSUT5 DD UNIT=VIO,SPACE=(TRK,1)
 //SYSUT6 DD UNIT=VIO,SPACE=(TRK,1) //SYSUT7 DD UNIT=VIO,SPACE=(TRK,1)
 //SYSLIN DD UNIT=VIO,SPACE=(TRK,1),DISP=(,PASS),BLKSIZE=3200 //*
 //GO    EXEC PGM=LOADER,PARM=NOPRINT
 //SYSLIN DD DISP=(OLD,PASS),DSN=*.COB2.SYSLIN //SYSOUT DD SYSOUT=*
 //SYSLIB DD DISP=SHR,DSN=CEE.SCEELKED


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

###### ↳ ↳ ↳ Re: NEWBIE PROBLEM

_(reply depth: 4)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B256C4.1682A399@att.net>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt> <7opb6j$b2a$1@nnrp1.deja.com> <37B107EF.8184BA67@att.net> <7os6q5$dka$1@nnrp1.deja.com>`

```
Thanks very much, Art.

Bill Lynch
```

#### ↳ Re: NEWBIE PROBLEM

- **From:** Clifton Ivy <clif@purdue.edu>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B1BF52.56D33336@purdue.edu>`
- **References:** `<7om98n$cjl$1@pthp35.telecom.pt>`

```
After looking at the responses to this question, I believe we are being
too literal in trying to answer the stated question, instead of trying
to solve the problem that causes the question.

I think we need to ask Calatis what he is trying to accomplish by
reading a file where the date is part of the Data Set Name (DSN).

Are you trying to process the file that was just created, and you are
using the date to differentiate between files created at different times
(so maybe you can keep all the files)? If so, other posts have suggested
DSN referbacks (DSN=*.STEP.DDNAME), and Generation Data Groups (GDGs).
Either of these could work, depending on what you are trying to
accomplish in total.

Do you need to process all the data files that have been created since
the last time you processed? GDGs can help here, also.

Are you trying to variably process data that was created on (?applies
to?) a particular date? Adding a date field to the record, and keeping
all the records in a single file would work until the bulk of the data
gets out of hand.

You know, sooner or later, your user is going to ask to run Process X
TWICE in a day, and probably have some very good reason why it is a good
idea -- and using the date may create problems in this case. 

Or, they may ask to skip Process X "for tonight", so that the work they
do today can be added to the work they do tomorrow and it be processed
as a single "day". They will have good business reasons for doing this,
also.

For these reasons, the best solutions may not be the first ones that
occur to you -- they may be the ones you are forced to after a few "You
want to do WHAT???" questions!

So, what are you trying to accomplish in total?

Thanks!

Calatis wrote:
> 
> Hello,
…[15 more quoted lines elided]…
> Nuno
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
