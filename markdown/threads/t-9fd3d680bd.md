[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Fileshare V2 - Unix.

_5 messages · 3 participants · 1999-11_

---

### MF Fileshare V2 - Unix.

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81mgks$gqc$1@starburst.uk.insnet.net>`

```
As far as I can see from reading the manuals the answer to the following
questions is no, but just in case.  BTW this is all on hp unix and aix using
MF Cobol 4.1.

Is there any way for an application set up for transaction processing to
tell that it isn't  running as a FileShare Client?   The only way I can
think of is to check for the environment variable FHREDIR but its absence
doesn't necessarily mean we are not running as a FS Client.

A corollary question is, is there any programmable way to see if the
FileShare Server is running?

Finally is there any way to tell the I/O to wait 'until available' or for a
certain time, when trying to read a record locked by another user?   At the
moment, on a file status 9-068 I keep retrying the read for a period of
time.  This seems likely to be a resource user.

TIA
Rick
```

#### ↳ Re: MF Fileshare V2 - Unix.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81mou6$i6f$1@news.igs.net>`
- **References:** `<81mgks$gqc$1@starburst.uk.insnet.net>`

```
I'd suggest just putting a "sleep" call into the read loop.  That should
make sure that it does not become a resource hog with minimal code changes.

Rick Price wrote in message <81mgks$gqc$1@starburst.uk.insnet.net>...
>As far as I can see from reading the manuals the answer to the following
>questions is no, but just in case.  BTW this is all on hp unix and aix
using
>MF Cobol 4.1.
>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: MF Fileshare V2 - Unix.

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81n07u$qhi$1@nntp2.atl.mindspring.net>`
- **References:** `<81mgks$gqc$1@starburst.uk.insnet.net>`

```
Does your version of the MF compiler have the RETRYLOCK compile directive?
If, it specifies that when a READ statement finds that a record is locked
the read operation is to be retried repeatedly until the record is
available. If the record is locked, control is not returned to you until it
is available...

Don't know of a way to see if fileshare is running or not...Maybe try
opening and closing a dummy file you know can only be found via
fileshare...Problem there is there is a 2 minute timeout...

hope this helps some...

kenmullins


Rick Price <rick@hpd.co.uk> wrote in message
news:81mgks$gqc$1@starburst.uk.insnet.net...
> As far as I can see from reading the manuals the answer to the following
> questions is no, but just in case.  BTW this is all on hp unix and aix
using
> MF Cobol 4.1.
>
…[8 more quoted lines elided]…
> Finally is there any way to tell the I/O to wait 'until available' or for
a
> certain time, when trying to read a record locked by another user?   At
the
> moment, on a file status 9-068 I keep retrying the read for a period of
> time.  This seems likely to be a resource user.
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF Fileshare V2 - Unix.

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81tish$rni$1@starburst.uk.insnet.net>`
- **References:** `<81mgks$gqc$1@starburst.uk.insnet.net> <81n07u$qhi$1@nntp2.atl.mindspring.net>`

```
Thanks.   I'm not sure about RETRYLOCK.  It waits forever but that might be
OK.  However according to my manual it doesn't take effect if there is a
specific declarative for a file which could be a problem.  I think I'll put
a short sleep in the loop as suggested by Donald Tees and hope it doesn't
affect interactive responses too badly.  This is pretty easy for us to do as
our 'non standard' file status checks for all files are dealt with in a sub
routine.
I'm not sure how big a problem this loop is.   I only really thought about
it when testing FileShare with trace and holding a record on purpose.   The
trace went haywire on the retry loop (obviously) and made me think about
what might happen in real life situations.

Ken Mullins <KenMullins@mindspring.com> wrote in message
news:81n07u$qhi$1@nntp2.atl.mindspring.net...
> Does your version of the MF compiler have the RETRYLOCK compile directive?
> If, it specifies that when a READ statement finds that a record is locked
> the read operation is to be retried repeatedly until the record is
> available. If the record is locked, control is not returned to you until
it
> is available...
>
…[10 more quoted lines elided]…
> news:81mgks$gqc$1@starburst.uk.insnet.net...
<snip>
> > Finally is there any way to tell the I/O to wait 'until available' or
for
> a
> > certain time, when trying to read a record locked by another user?   At
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF Fileshare V2 - Unix.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81tume$m34$1@news.igs.net>`
- **References:** `<81mgks$gqc$1@starburst.uk.insnet.net> <81n07u$qhi$1@nntp2.atl.mindspring.net> <81tish$rni$1@starburst.uk.insnet.net>`

```
I have been coding my file waits that way for several years with minimal
problems.  I would suggest one other thing, though, and that is some sort of
screen indication when the lock is in place and the delay takes place.  In
most of my code, in the past, I updated the screen clock once on each retry,
and put the status byte beside it.  That allowed me to see what was
happening if there ended up being a "permanent" file lock for some reason.

The only real problem that causes is that it makes the screen I-O and the
file I-O co-dependent.  That has caused some problems on the latest
conversion of some code to GUI.  Now that I can effectively code to any
size, I am removing that and placing the file screen indicators into their
own window.  IE-on file lock, open a window, show the lock, delay, close the
window, repeat.  That is very CPU intensive for the local machine
experiencing the lock, but what the heck, it cannot do anything until the
lock is done anyway.  Eventually, I will trap keystrokes in that loop so the
user can break out of it gracefully.



Rick Price wrote in message <81tish$rni$1@starburst.uk.insnet.net>...
>Thanks.   I'm not sure about RETRYLOCK.  It waits forever but that might be
>OK.  However according to my manual it doesn't take effect if there is a
>specific declarative for a file which could be a problem.  I think I'll put
>a short sleep in the loop as suggested by Donald Tees and hope it doesn't
>affect interactive responses too badly.  This is pretty easy for us to do
as
>our 'non standard' file status checks for all files are dealt with in a sub
>routine.
…[7 more quoted lines elided]…
>> Does your version of the MF compiler have the RETRYLOCK compile
directive?
>> If, it specifies that when a READ statement finds that a record is locked
>> the read operation is to be retried repeatedly until the record is
…[31 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
