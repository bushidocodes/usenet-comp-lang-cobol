[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF lock_mode 0/2 - HP Unix

_8 messages · 3 participants · 1999-05 → 1999-06_

---

### MF lock_mode 0/2 - HP Unix

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk>`

```
Does anybody know how MF COBOL lock_mode 0 works?   I thought I did know and
that it locks by record number instead of using standard unix locking
(lock_mode 2).

We are using MF COBOL 4.0.  The files are indexed.  We were using lock_mode
2 (the default on this version) but then hit a problem with a client who had
large shared files.  If these grew larger than 1GB, any locks on data after
the 1GB mark were not released and finally blew the number of locks allowed
on the system.

We then found that if we changed to lock_mode 0, (the mode in our old
versions of MF) this problem went away and  records were successfully locked
and unlocked after the 1GB mark.

However we have just (over the weekend) hit a problem at our clients using
lock_mode 0.   They have a file that grew larger after importing lots of
data.  Suddenly this started not being able to unlock records and finally
blew the number of locks allowed on the system.

The file size is 942,027,248 and the number of records is 923,556. It uses
IDXFORMAT4.

We then tried processing this file using lock_mode 2 and it worked.

So we have a file > 1GB with approximately 600,000 records which can only be
processed using lock_mode 0 and a file of  < 1GB which can only be processed
using lock_mode 2.

Ha ha I thought, maybe the no of records allowed by lock_mode 0 is less than
expected.  So we created a file of a million small records (total size 10MB)
and processed that using lock_mode 0 to try to find the record number that
started causing the problem.  There were no problems.

So the number of records doesn't seem to be the problem.  But the file size
doesn't seem to be the problem either.

Which brings me back to the question, does any body know how lock_mode 0
works?

I was basing my assumptions on a document I have seen which I don't really
understand but which states for lock_mode 0:

'max record number that can be locked is <cut>  approx .25GB.'

I assumed from this that locking was by record number and it allowed for
approximately 250 million (rather short) records in theory.

BTW we think we will have to start splitting files up for this large client
but we thought that file_mode 0 would give us a safety net when files did
temporarily grow > 1 GB.

Regards
Rick
```

#### ↳ Re: MF lock_mode 0/2 - HP Unix

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-nQ0IfTpx6dUb@Dwight_Miller.iix.com>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk>`

```
On Mon, 24 May 1999 17:07:30, "Rick Price" <rick@hpdi.demon.co.uk> 
wrote:

> So we have a file > 1GB with approximately 600,000 records which can only be
> processed using lock_mode 0 and a file of  < 1GB which can only be processed
> using lock_mode 2.
> 


Rick, 

Is it possible that you only experience the problem when records are 
locked both above and below 1 gig?  

Hence the reproduction failure.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: MF lock_mode 0/2 - HP Unix

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<927617715.17754.0.nnrp-11.9e98b131@news.demon.co.uk>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk> <Jl0PnHJ5PvPd-pn2-nQ0IfTpx6dUb@Dwight_Miller.iix.com>`

```
No Thane.  The problem is on the file with < 1GB using lock_mode 0.

Also the files are compiled to only allow one lock at a time.


Thane Hubbell wrote in message ...
>On Mon, 24 May 1999 17:07:30, "Rick Price" <rick@hpdi.demon.co.uk>
>wrote:
>
>> So we have a file > 1GB with approximately 600,000 records which can only
be
>> processed using lock_mode 0 and a file of  < 1GB which can only be
processed
>> using lock_mode 2.
>>
…[17 more quoted lines elided]…
>http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF lock_mode 0/2 - HP Unix

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-LGDFlBr2ij3Y@Dwight_Miller.iix.com>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk> <Jl0PnHJ5PvPd-pn2-nQ0IfTpx6dUb@Dwight_Miller.iix.com> <927617715.17754.0.nnrp-11.9e98b131@news.demon.co.uk>`

```
On Tue, 25 May 1999 07:36:48, "Rick Price" <rick@hpdi.demon.co.uk> 
wrote:

> No Thane.  The problem is on the file with < 1GB using lock_mode 0.
> 
> Also the files are compiled to only allow one lock at a time.
> 
> 

Sorry, I wasn't clear.  I meant the large file failures you see under 
Lock Mode 2, but were unable to reproduce based on record counts.  I 
expect that perhaps the problem occurs using lock mode 2, with larger 
files, when one process has a record locked toward the "lower" end and
another process has a record locked toward the "higher" end.

Possible?  Sorry I don't have a solution!


> Thane Hubbell wrote in message ...
> >On Mon, 24 May 1999 17:07:30, "Rick Price" <rick@hpdi.demon.co.uk>
…[27 more quoted lines elided]…
> 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF lock_mode 0/2 - HP Unix

_(reply depth: 4)_

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<927653485.27749.0.nnrp-04.9e98b131@news.demon.co.uk>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk> <Jl0PnHJ5PvPd-pn2-nQ0IfTpx6dUb@Dwight_Miller.iix.com> <927617715.17754.0.nnrp-11.9e98b131@news.demon.co.uk> <Jl0PnHJ5PvPd-pn2-LGDFlBr2ij3Y@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Tue, 25 May 1999 07:36:48, "Rick Price" <rick@hpdi.demon.co.uk>
>wrote:
…[15 more quoted lines elided]…
>

In fact I wasn't very clear in my original message.  We know why this
happens.  Lock_mode=2 uses standard unix locking.  The basic unix file
system doesn't like shared use of files > 1GB.  It, or MF Cobol,  just
weren't very well behaved about it hence the runaway locks.  That's why we
went to lock_mode=0 which allows (or seems to) shared use of files <=2GB.

We now think we know what is causing the problem I was raising.  I've sent
an update to the newsgroup.

Thanks Thane

Rick


>> Thane Hubbell wrote in message ...
>> >On Mon, 24 May 1999 17:07:30, "Rick Price" <rick@hpdi.demon.co.uk>
>> >wrote:
>> >
>> >> So we have a file > 1GB with approximately 600,000 records which can
only
>> be
>> >> processed using lock_mode 0 and a file of  < 1GB which can only be
…[32 more quoted lines elided]…
>http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: MF lock_mode 0/2 - HP Unix - Update

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<927652301.27052.0.nnrp-04.9e98b131@news.demon.co.uk>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk>`

```
We think we have found the cause of the problem after various tests.   At
the moment it seems that lock_mode=0 and IDXFORMAT4 are incompatible above a
certain file size c500MB.  At least in our environment.

Rick

Rick Price wrote in message
<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk>...
>Does anybody know how MF COBOL lock_mode 0 works?   I thought I did know
and
>that it locks by record number instead of using standard unix locking
>(lock_mode 2).
>
>We are using MF COBOL 4.0.  The files are indexed.  We were using lock_mode
>2 (the default on this version) but then hit a problem with a client who
had
>large shared files.  If these grew larger than 1GB, any locks on data after
>the 1GB mark were not released and finally blew the number of locks allowed
…[3 more quoted lines elided]…
>versions of MF) this problem went away and  records were successfully
locked
>and unlocked after the 1GB mark.
>
…[10 more quoted lines elided]…
>So we have a file > 1GB with approximately 600,000 records which can only
be
>processed using lock_mode 0 and a file of  < 1GB which can only be
processed
>using lock_mode 2.
>
>Ha ha I thought, maybe the no of records allowed by lock_mode 0 is less
than
>expected.  So we created a file of a million small records (total size
10MB)
>and processed that using lock_mode 0 to try to find the record number that
>started causing the problem.  There were no problems.
…[24 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF lock_mode 0/2 - HP Unix - Update

- **From:** "Sean Brooke-Hughes" <sean@oldhippy.demon.co.uk>
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928784523.1732.0.nnrp-08.c1ed3c81@news.demon.co.uk>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk> <927652301.27052.0.nnrp-04.9e98b131@news.demon.co.uk>`

```
Just a thought. There is a bit of an issue with MF-ISAM type 4 files being
opened in shared / unshared mode. Standard MF COBOL only allows files to be
accessed/created etc up to 2GB if opened unshared. If opened in shared mode
this drops to 1GB. Now I know that if you are using fileshare, this acts as
the unshared/exclusive file handler so you get 2GB. On later versions of
COBOL (4.1 on AIX) you have the ability to specify that lock files are
separate and you can, again, open/create 2GB files in shared mode, albeit
with a .lck file for locks.

I also know through a long and troubled history of using MF-ISAM that the
file handler (extfh) has had some really nasty bugs in the past. I'm not
that familiar with the HP version of MF-COBOL (Solaris + aix mainly), but I
know Object COBOL 4.1 is available for most platforms and file handling is
(a bit) more reliable in this ver... Just checked MF's product matrix and
4.1 is out for HP.

Cheers,
Sean.
```

###### ↳ ↳ ↳ Re: MF lock_mode 0/2 - HP Unix - Update

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928830416.21787.0.nnrp-09.9e98b131@news.demon.co.uk>`
- **References:** `<927565561.24755.0.nnrp-02.9e98b131@news.demon.co.uk> <927652301.27052.0.nnrp-04.9e98b131@news.demon.co.uk> <928784523.1732.0.nnrp-08.c1ed3c81@news.demon.co.uk>`

```
Thanks for this Sean.

FYI The run time tuneable lock_mode=0 allows files up to 2GB to be processed
in shared mode.  However we've discovered that the extfh doesn't handle this
lock_mode properly and seems to go haywire on the later part of files >
c0.5GB.  So it only seems to work with files that use the modified C-ISAM.
This is all unix by the way.

We think we've solved this in the file that gave us problems by making the
duplicate keys unique, which is a pain but the only way we can continue to
use lock_mode=0.

I'm interested in the ability to have separate lock files.  I somehow
thought that this was only available on PC, not on unix.  We'll have to
check this out.  I thought the only extra option available in 4.1 on unix
was file striping, which is a sledgehammer to crack a nut in this case.

I believe that the next version of MF Cobol will be able to use unix large
file processing, which should simplify things for us.

Regards and thanks again

Rick

Sean Brooke-Hughes <sean@oldhippy.demon.co.uk> wrote in message
news:928784523.1732.0.nnrp-08.c1ed3c81@news.demon.co.uk...
> Just a thought. There is a bit of an issue with MF-ISAM type 4 files being
> opened in shared / unshared mode. Standard MF COBOL only allows files to
be
> accessed/created etc up to 2GB if opened unshared. If opened in shared
mode
> this drops to 1GB. Now I know that if you are using fileshare, this acts
as
> the unshared/exclusive file handler so you get 2GB. On later versions of
> COBOL (4.1 on AIX) you have the ability to specify that lock files are
…[5 more quoted lines elided]…
> that familiar with the HP version of MF-COBOL (Solaris + aix mainly), but
I
> know Object COBOL 4.1 is available for most platforms and file handling is
> (a bit) more reliable in this ver... Just checked MF's product matrix and
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
