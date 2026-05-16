[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# locking down a VSAM file

_6 messages · 5 participants · 1999-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### locking down a VSAM file

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-10-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
I have a job that, among other things, builds a flat file, deletes and 
defines a VSAM file, then repros the flat file to the vsam file using
IDCAMS.

Last night on the IDCAMS step, it returned CC=12 on the delete, define, and
repro saying file is in use by another user, "TRY AGAIN LATER" (how nice).
The job continued on.  Needless to say the VSAM file was not updated because
another job was producing contention.

I exhausted the IBM manuals on SHAREOPTIONS, etc.  I couldn't find anything
to make IDCAMS wait for the dataset.  So I put a return code check in the
next step to call a user abend program, and marked the opdocs with restart
instructions (wait 5 mins and try again).

There has to be a better way.  I thought maybe a call an IEFBR14 in the
preceding step so that it will wait until the dataset frees up.  That's the
only other way I could think of.

Needless to say, I made the 'guys across the hall' push their job up later
on CA7.

Later,
Jeff
```

#### ↳ Re: locking down a VSAM file

- **From:** Scott Peterson <scottp4.removethis@mindspring.com>
- **Date:** 1999-10-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rn8WOBNeqI4SYpRqnAep5rX+WM8P@4ax.com>`
- **References:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
"Jeff Baynard" <union27@macconnect.com> wrote:

>I have a job that, among other things, builds a flat file, deletes and 
>defines a VSAM file, then repros the flat file to the vsam file using
…[11 more quoted lines elided]…
>
A lot depends on what else is using the file.  If it's another batch
job, how about DISP=OLD on the DD statement in the JCL. It's always
better not to let a job start than get half way through and try to
figure out what happened. 

If it's allocated to an online system for update like CICS or IMS,
then it's a coordination issue. You could write a very simple COBOL
program  that does an OPEN IO on the file.  If the return code from
the OPEN is not zero, then either set a return code and blow up or you
could invoke an assembler routine that issues a wait for five minutes
and then retries the OPEN.  What you also need to do is get a message
displayed somewhere, either UCC7 or a console about why your job is
waiting. 

Another alternative is split the IDCAMS into two job steps.  Do the
DELETE in one and the DEFINE/REPRO in a second that only runs on
condition code 0 from the delete step. Then your actual processing
only runs on cc=0 from both previous steps. ]

You can actually do this in IDCAMS if you want using the IF statement
in it, but I prefer JCL for production as it's easier for the
production control people to follow up and rerun the job properly. 
                         
                         		Scott Peterson


Madness takes its toll.  
Please have exact change.
```

#### ↳ Re: locking down a VSAM file

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38178E51.5E35@saif.com>`
- **References:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
Jeff Baynard wrote:
> 
> I have a job that, among other things, builds a flat file, deletes and
…[21 more quoted lines elided]…
> Jeff

Because of this sort of problem, we have a shop standard that you always
have a DISP=OLD against the target dataset in your JCL.

e.g.
//REPRO EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//INFILE   DD whatever
//OUTFILE  DD whatever,DISP=OLD
//SYSIN    DD *
 REPRO INFILE(INFILE) OUTFILE(OUTFILE)

Pete
```

#### ↳ Re: locking down a VSAM file

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3816732f.184735768@news1.attglobal.net>`
- **References:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
The Delete/Define won't wait.  But you could have a COBOL program that
opened the file I/O then closes it.  (Share option 2 needs to be
defined for the file, multiple read single update).  In that case the
job will wait with "Waiting for datasets".  The reason IEFBR14 doesn't
work is that it doesn't open the file for update.




On Tue, 26 Oct 1999 20:39:19 -0400, "Jeff Baynard"
<union27@macconnect.com> wrote:

>I have a job that, among other things, builds a flat file, deletes and 
>defines a VSAM file, then repros the flat file to the vsam file using
…[21 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: locking down a VSAM file

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3816755e.185295288@news1.attglobal.net>`
- **References:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
The Delete/Define won't wait.  But you could have a COBOL program that
opened the file I/O then closes it.  (Share option 2 needs to be
defined for the file, multiple read single update).  In that case the
job will wait with "Waiting for datasets".  The reason IEFBR14 doesn't
work is that it doesn't open the file for update.




On Tue, 26 Oct 1999 20:39:19 -0400, "Jeff Baynard"
<union27@macconnect.com> wrote:

>I have a job that, among other things, builds a flat file, deletes and 
>defines a VSAM file, then repros the flat file to the vsam file using
…[21 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: locking down a VSAM file

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3816BC5E.27182EDC@nbnet.nb.ca>`
- **References:** `<7v5hjk$16l8@enews2.newsguy.com>`

```
One way to guarantee that you have the file exclusively is to code a DD
statement with DISP=OLD for the file in the preceding step and have a
DISP=OLD on all other DD statements referring to the file.  There may be
a slight window where this won't be true in a JES2 environment and it
will be true in a JES3 environment.  If you are using VM or VSE I don't
know if there is a comparable solution.

Clark Morris, CFM Technical Programming Services,  morrisc@nbnet.nb.ca 

Jeff Baynard wrote:
> 
> I have a job that, among other things, builds a flat file, deletes and
…[21 more quoted lines elided]…
> Jeff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
