[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# user abends and job termination

_5 messages · 5 participants · 2006-06_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### user abends and job termination

- **From:** michalosada@gmail.com
- **Date:** 2006-06-20T07:37:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com>`

```
I always thought that after an abend (any abend - including so called
"user") job terminates - following steps are not performed. I have a
job that did something different.

I have a question - does user abend is an ABEND? Does calling ILBOABN0
from COBOL program stops the job?

grateful for any piece of advice
Michael Osada
```

#### ↳ Re: user abends and job termination

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-06-20T16:43:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NAVlg.258277$Az2.225543@fe10.news.easynews.com>`
- **References:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com>`

```
Whether or not following steps are executed in an (IBM) z/OS environment is 
determined by the COND parameter on each step and/or "conditional" IF JCL 
statements.

Yes,  ILBOABN0 (or CEE3ABD) cause "full" ABEND processing.

HOWEVER,  some people get confused with "return codes".  Setting the RETURN-CODE 
special register does NOT cause an ABEND, only a non-zero RC.
```

##### ↳ ↳ Re: user abends and job termination

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-20T10:57:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1150826234.967665.35850@y41g2000cwy.googlegroups.com>`
- **In-Reply-To:** `<NAVlg.258277$Az2.225543@fe10.news.easynews.com>`
- **References:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com> <NAVlg.258277$Az2.225543@fe10.news.easynews.com>`

```

William M. Klein wrote:
> Whether or not following steps are executed in an (IBM) z/OS environment is
> determined by the COND parameter on each step and/or "conditional" IF JCL
…[9 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

IIRC, you can also check for abending codes and perform your own
processing in zOS JCL


> <michalosada@gmail.com> wrote in message
> news:1150814239.994822.203420@i40g2000cwc.googlegroups.com...
…[9 more quoted lines elided]…
> >
```

##### ↳ ↳ Re: user abends and job termination

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-06-20T11:44:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UIWdneWDUduZ3wXZnZ2dnUVZ_uWdnZ2d@adelphia.com>`
- **In-Reply-To:** `<NAVlg.258277$Az2.225543@fe10.news.easynews.com>`
- **References:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com> <NAVlg.258277$Az2.225543@fe10.news.easynews.com>`

```
William M. Klein wrote:
> Whether or not following steps are executed in an (IBM) z/OS environment is 
> determined by the COND parameter on each step and/or "conditional" IF JCL 
…[7 more quoted lines elided]…
>   
I'm fuzzy on the details, but I recall that once when we updated the 
operating system and probably the compiler, too, the installation 
options got changed from what we were used to having.  This resulted in 
an error condition that always previously had caused an abend to change 
to generating an error message and a return code.  This may very well be 
the option ABTERMENC in Language Environment run time options.

Also, if you specify FILE STATUS items on your files, but do not check 
them, or check them incorrectly or incompletely, you may end up not 
getting an abend when a problem occurs.  Omitting the FILE STATUS item 
tells the compiler to send errors to an error handler, which might give 
you, for example, a S013-nn abend on an OPEN error.  But specifying FILE 
STATUS says you want to handle the problem, and then if you don't, you 
may end up doing something like trying to execute a READ, and getting a 
different abend because the file is not open.
```

#### ↳ Re: user abends and job termination

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-06-20T22:28:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60481$4498aee3$d066072d$20384@FUSE.NET>`
- **In-Reply-To:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com>`
- **References:** `<1150814239.994822.203420@i40g2000cwc.googlegroups.com>`

```
michalosada@gmail.com wrote:
> I always thought that after an abend (any abend - including so called
> "user") job terminates - following steps are not performed. I have a
…[7 more quoted lines elided]…
> 
There are two different situations that can be tested in JCL to 
determine if a step should or should not be executed:

1)  If you want to check the Condition Code [a.k.a., Return Code] from 
an earlier step, use the COND option on the EXEC statement as indicated 
in the following from the IBM JCL Reference:

> //STEP6  EXEC PGM=DISKUTIL,COND=(4,GT,STEP3)
> 
…[4 more quoted lines elided]…
> step abnormally terminates.
The default, with no COND option, is to execute the step.

2)  If you want to check for a previous ABEND, you use COND=EVEN or 
COND=ONLY sub-options.  Note that, if you specify EVEN or ONLY alone, 
the Return/Condition code is not tested from any previous step.  Also 
from the JCL Reference manual:
	
> EVEN
> Specifies that this job step is to be executed even if a preceding
…[3 more quoted lines elided]…
> Specifies that this job step is to be executed only if a preceding step abnormally terminated. 

But, you can use combinations of Return Code values and EVEN or ONLY. 
An example:

> //TEST2  EXEC PGM=DUMPINT,COND=((16,GE),(90,LE,STEP1),ONLY)
> 
…[16 more quoted lines elided]…
>     * The return code from STEP1 is 90 or greater.

Now, with this introduction, you really need to just go RTFM to 
understand all the other variations that can be used.

Good luck,
Carl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
