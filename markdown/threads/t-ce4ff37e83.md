[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to EXEC PROC in a JCL

_13 messages · 9 participants · 2004-01 → 2004-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How to EXEC PROC in a JCL

- **From:** andre.queiroz@netcabo.pt (Andr? Queiroz)
- **Date:** 2004-01-21T08:34:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e571c199.0401210834.3fe6a584@posting.google.com>`

```
Hello,
 I have a JCL step like:

//XXXPRG   EXEC PROC=MYLIB,PG=PGM2,COND=(0,NE)                    
//FICH1    DD DSN=AAA.DS100.RESULT,                
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(TRK,(50,50),RLSE),                               
//            DCB=(RECFM=FB,LRECL=128)

 Is there any way of knowing where are the libraries defined by
MYLIB?? I need to know because my system has several PGM2 and I don't
know wich is being used in my JCL execution.

 Thanks in advance,

Andre Queiroz
```

#### ↳ Re: How to EXEC PROC in a JCL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-01-21T16:39:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040121113917.26428.00000577@mb-m07.aol.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com>`

```
Andre Queiroz writes ...

>Hello,
> I have a JCL step like:
…[10 more quoted lines elided]…
>

Look at the JCL listing after submitting the job?

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: How to EXEC PROC in a JCL

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2004-01-21T14:40:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0401211440.1174575c@posting.google.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <20040121113917.26428.00000577@mb-m07.aol.com>`

```
Bottom posting

scomstock@aol.com (S Comstock) wrote in message news:<20040121113917.26428.00000577@mb-m07.aol.com>...
> Andre Queiroz writes ...
> 
…[14 more quoted lines elided]…
> Look at the JCL listing after submitting the job?


> 
> Kind regards,
…[9 more quoted lines elided]…
> USA

Hello Andre,

Further to Steve's suggestion, you could put TYPRUN=SCAN on the JOB
card so that the system only expands the JCL to give a listing rather
than running the programs.

cheers Robert
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

- **From:** andre.queiroz@netcabo.pt (Andr? Queiroz)
- **Date:** 2004-01-22T04:28:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e571c199.0401220428.49447913@posting.google.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <20040121113917.26428.00000577@mb-m07.aol.com> <fcd09c56.0401211440.1174575c@posting.google.com>`

```
robert@jones0086.freeserve.co.uk (Robert Jones) wrote in message news:<fcd09c56.0401211440.1174575c@posting.google.com>...
> Bottom posting
> 
…[39 more quoted lines elided]…
> cheers Robert

Those are nice suggestions but that's my problem, I can't execute the JCL.
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-01-22T08:00:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<buohhh$nk3$1@panix1.panix.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <20040121113917.26428.00000577@mb-m07.aol.com> <fcd09c56.0401211440.1174575c@posting.google.com> <e571c199.0401220428.49447913@posting.google.com>`

```
In article <e571c199.0401220428.49447913@posting.google.com>,
Andr? Queiroz <andre.queiroz@netcabo.pt> wrote:
>robert@jones0086.freeserve.co.uk (Robert Jones) wrote in message news:<fcd09c56.0401211440.1174575c@posting.google.com>...

[snip]

>> Further to Steve's suggestion, you could put TYPRUN=SCAN on the JOB
>> card so that the system only expands the JCL to give a listing rather
…[4 more quoted lines elided]…
>Those are nice suggestions but that's my problem, I can't execute the JCL.

I do not understand.  What are the results when you submit the job with a 
TYPRUN=SCAN card?  (that will not execute it, you know)

DD
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 5)_

- **From:** Merlin43PhD@netscape.net (=D=)
- **Date:** 2004-01-22T20:10:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9d3c0262.0401222010.68d3d876@posting.google.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <20040121113917.26428.00000577@mb-m07.aol.com> <fcd09c56.0401211440.1174575c@posting.google.com> <e571c199.0401220428.49447913@posting.google.com> <buohhh$nk3$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<buohhh$nk3$1@panix1.panix.com>...

> [snip]
> 
> >> Further to Steve's suggestion, you could put TYPRUN=SCAN on the JOB

> >> cheers Robert
> >
…[5 more quoted lines elided]…
> DD
One thing I have not seen mentioned is that the MSGLEVEL needs to be
(1,1) or, at least (1,0) in order to see the expanded JCL, even if
execution is prevented by the TYPRUN.

If, by "I can't execute the JCL", he means physically has no way to
submit it, then, without knowing what PROCLIB to look into, he is SOL.
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-01-23T08:09:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bur6f3$7l0$1@panix1.panix.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <e571c199.0401220428.49447913@posting.google.com> <buohhh$nk3$1@panix1.panix.com> <9d3c0262.0401222010.68d3d876@posting.google.com>`

```
In article <9d3c0262.0401222010.68d3d876@posting.google.com>,
=D= <Merlin43PhD@netscape.net> wrote:
>docdwarf@panix.com wrote in message news:<buohhh$nk3$1@panix1.panix.com>...
>
…[13 more quoted lines elided]…
>execution is prevented by the TYPRUN.

Odd... in my 'standard jobcard(s)' that I carry from one site to the next 
I have:

 //JOBNAM00 JOB (XXXX,999,X,9999,999),'TEXT STRING FOR ID'
 //*            TYPRUN=SCAN,
 //*            RESTART=STEPNAM,
 //*            REGION=4M
 
... and with appropriate uncommenting and added comma it scans just fine.

>
>If, by "I can't execute the JCL", he means physically has no way to
>submit it, then, without knowing what PROCLIB to look into, he is SOL.

Agreed... *almost*.  If his site has !jck or a JCLCheck someplace there 
might be hope... but first things first, I am still curious as to what is 
found when the job is sub'd with SCAN.

DD
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 7)_

- **From:** Merlin43PhD@netscape.net (=D=)
- **Date:** 2004-01-29T09:38:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9d3c0262.0401290938.44774400@posting.google.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <e571c199.0401220428.49447913@posting.google.com> <buohhh$nk3$1@panix1.panix.com> <9d3c0262.0401222010.68d3d876@posting.google.com> <bur6f3$7l0$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<bur6f3$7l0$1@panix1.panix.com>...
[snip]
> >One thing I have not seen mentioned is that the MSGLEVEL needs to be
> >(1,1) or, at least (1,0) in order to see the expanded JCL, even if
…[11 more quoted lines elided]…
> 
Yep, but the system programmer (or JES administrator) has set the
default MSGLEVEL to (1,1) probably, (1,0) less likely, so you don't
have to.  I got into the habit of setting my systems to (2,0) (as
Thane can attest), so that production jobs with 1500 lines or so of
JCL and disposition data did not use up so much SPOOL space or printer
paper.  If a job craters, it sets the last step disposition to 1
anyway, so who needs to see all the trash if the job runs correctly? 
COND codes are still reported, even at (2,0), and those using some
third-party utility (something I never found useful) to do checking
don't need to see the JCL for a successful run.  With a default of
(2,0), or even (1,0), you need to over-ride it on the JOB "card" to a
(1,1) if you want to see the expanded proc.  This is one of those "not
quite enough info' for a definitive answer in the first post"
situations!

Best regards from =DrD= to =DD=
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-01-29T13:10:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvbib7$j1d$1@panix1.panix.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <9d3c0262.0401222010.68d3d876@posting.google.com> <bur6f3$7l0$1@panix1.panix.com> <9d3c0262.0401290938.44774400@posting.google.com>`

```
In article <9d3c0262.0401290938.44774400@posting.google.com>,
=D= <Merlin43PhD@netscape.net> wrote:
>docdwarf@panix.com wrote in message news:<bur6f3$7l0$1@panix1.panix.com>...
>[snip]
…[16 more quoted lines elided]…
>have to.

What a fortuitous coincidence!

>I got into the habit of setting my systems to (2,0) (as
>Thane can attest), so that production jobs with 1500 lines or so of
>JCL and disposition data did not use up so much SPOOL space or printer
>paper.  If a job craters, it sets the last step disposition to 1
>anyway, so who needs to see all the trash if the job runs correctly? 

Ahem... well, a shop I once worked in delighted in using uncatalogued
datasets... so a job would 'run correctly' when it was fed
FDMSD.TR1882F.SAM0P21B.QTR1YTD.IOUIUPDT,VOL=SER=99125 and then incorrect
results determined (and fixed) by reading the SYSOUT and knowing that this 
was *last* year's tape and that this year's was 
FDMSD.TR1882F.SAM0P21B.QTR1YTD.IOUIUPDT,VOL=SER=98924.

>COND codes are still reported, even at (2,0), and those using some
>third-party utility (something I never found useful) to do checking
>don't need to see the JCL for a successful run.

All-zero RETURN CODEs do not a 'successful run' make... and an 
unsuccessful one can remain undetected for weeks.

>With a default of
>(2,0), or even (1,0), you need to over-ride it on the JOB "card" to a
>(1,1) if you want to see the expanded proc.  This is one of those "not
>quite enough info' for a definitive answer in the first post"
>situations!

Speaking of 'not quite enough info'... is it my imagination or did the 
original inquirer get very, *very* silent when asked what happened with a 
TYPRUN=SCAN submission?

DD
```

###### ↳ ↳ ↳ Re: How to EXEC PROC in a JCL

_(reply depth: 9)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-01-30T07:08:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0401300708.263c74bd@posting.google.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <9d3c0262.0401222010.68d3d876@posting.google.com> <bur6f3$7l0$1@panix1.panix.com> <9d3c0262.0401290938.44774400@posting.google.com> <bvbib7$j1d$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<bvbib7$j1d$1@panix1.panix.com>...

Doc wrote:

> Speaking of 'not quite enough info'... is it my imagination or did the 
> original inquirer get very, *very* silent when asked what happened with a 
> TYPRUN=SCAN submission?
> 
> DD

Yo Andre(an)! You still out there?
```

#### ↳ Re: How to EXEC PROC in a JCL

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-23T14:52:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<burcg9$okg$1@peabody.colorado.edu>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com>`

```
There is a chance that your needs may be met by adding a not quite so ancient
JCL command.

 // JCLLIB ORDER=(UMS.D44201.PROC,UMS.STG1TEST.PROC)


I suspect not - but thought I would mention it.
```

#### ↳ Re: How to EXEC PROC in a JCL

- **From:** Howard Hess <hmhess1-nospam@yahoo.com>
- **Date:** 2004-01-27T16:45:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kh1d101qq2pvar9asdi3b9umo5ese4f0sj@4ax.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com>`

```
On 21 Jan 2004 08:34:18 -0800, andre.queiroz@netcabo.pt (Andr?
Queiroz) wrote:

>Hello,
> I have a JCL step like:
…[13 more quoted lines elided]…
>Andre Queiroz
Andre,

If I were looking for the library that contains load module PGM2
(which is how I interpreted your question),  I'd do the following:

1) Check for a STEPLIB DD statement in the body of the MYLIB proc and
in the JCL invoking the MYLIB proc. If one is present, check those
libraries, in the sequence specified by the DD concatenation, for a
load module or alias PGM2.

2) Check the JCL that invokes MYLIB for a JOBLIB  DD statements. Check
those libraries.

3) Contact my systems programmer to learn the default load library
concatenation configured for the job class in which this job runs. If
I can't get any system programmer support, I *could* go scrounging
through the appropriate JES documents to re-learn where all of that is
specified, but I'd hope that wasn't necessary.
```

##### ↳ ↳ Re: How to EXEC PROC in a JCL

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-02-09T08:24:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-9A81C2.08244809022004@corp.supernews.com>`
- **References:** `<e571c199.0401210834.3fe6a584@posting.google.com> <kh1d101qq2pvar9asdi3b9umo5ese4f0sj@4ax.com>`

```
In article <kh1d101qq2pvar9asdi3b9umo5ese4f0sj@4ax.com>,
 Howard Hess <hmhess1-nospam@yahoo.com> wrote:

> On 21 Jan 2004 08:34:18 -0800, andre.queiroz@netcabo.pt (Andr?
> Queiroz) wrote:
…[34 more quoted lines elided]…
> specified, but I'd hope that wasn't necessary.

If PGM2 is not in your STEPLIB (1st) or JOBLIB (2nd) then...

If you have ISPF available, use the ISRDDN tool (invoke via "TSO ISRDDN" 
or "ISRDDN" if in your command table).

Once in the tool, use the command "LOAD PGM2", you will either get a not 
found error or it will tell you whereabouts in the link list it loaded 
from.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
