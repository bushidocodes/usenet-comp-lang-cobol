[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How many files to open at once?

_3 messages · 3 participants · 2000-02_

---

### Re: How many files to open at once?

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1q1q4.3327$QK6.42366@news4.mia>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca>`

```
What Platform?

MS/PC-Dos is about 3 UNLESS the config.sys  is edited:
FILES=nn
BUFFERS=nn

Windows is much higher
MVS/OS-390
Unlimited except by available system memory, user / partition memory, Job
memory

Ranjithkumar Nadarajah <rnadaraj@ecexh.uwaterloo.ca> wrote in message
news:889qd6$fkg$1@watserv3.uwaterloo.ca...
> Does anyone knowknow how many files that we can open concurrently in a
COBOL program?  How many at once?
>
> ANy help will be appreciated.
>
```

#### ↳ Re: How many files to open at once?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88aog1$q4g$1@nntp1.atl.mindspring.net>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <1q1q4.3327$QK6.42366@news4.mia>`

```
James King <mangogwr@bellsouth.net> wrote in message
news:1q1q4.3327$QK6.42366@news4.mia...
> What Platform?
>
 <snip>
> MVS/OS-390
> Unlimited except by available system memory, user / partition memory, Job
> memory
>

James,
  Are you certain of that?  I know that there used to be a 255 DDNames per
step limit (or maybe it was 1024 - I know that it was some power-of-2 type
number).  I remember it getting "expanded," but I don't remember it being
eliminated completely.

OTOH, I don't know of any COBOL program that actually ever hit the limit.

FYI - the current IBM LRM shows a limit of 65,535 SELECT statements, so I
think that is the current *theoretical* limit (at least outside CICS) that a
program could address (have open) at one time.  Again, I don't know of any
program running into this limit, but it isn't QUITE "unlimited".
```

##### ↳ ↳ Re: How many files to open at once?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38AA9C14.E5A320E9@zip.com.au>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <1q1q4.3327$QK6.42366@news4.mia> <88aog1$q4g$1@nntp1.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> > MVS/OS-390
…[9 more quoted lines elided]…
> 

I think that it was 255 but this was changed in OS-390.  There might
still be a limit but it is much higher.

I would hate to maintain the JCL though.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
