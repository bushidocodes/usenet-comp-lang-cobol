[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Record Locking - Who has locked it

_7 messages · 6 participants · 1999-10_

---

### Record Locking - Who has locked it

- **From:** spanna2000@my-deja.com
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ungfs$9sj$1@nnrp1.deja.com>`

```
We're using Microfocus COBOL under SCO Unix. When a file is record is
locked it would be useful to know which user has the record locked. We
have a problem whereby an operator in a multiuser system can lock a
record out whilst they change the record. They forget what they're
doing go off to lunch and leave the record locked. If this is a
commonly used record it can cause havoc.

Does anyone have a way to tell which user account has the record
locked, either via MF's EXTFH or via the operating system's lock
tables?

Regards

Mark


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Record Locking - Who has locked it

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380F5A5A.87D749D7@home.com>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com>`

```


spanna2000@my-deja.com wrote:
> 
> We're using Microfocus COBOL under SCO Unix. When a file is record is
…[13 more quoted lines elided]…
>

Mark,

What you are doing is as NO-NO. Not the answer to your question but
check out the previous thread "Record Locking while validating records".
As you will see - your situation occurred with a system in Australia !

I think Randall Bart made the best point - put a time-stamp on records
and perhaps use that same-time stamp to clear/unlock  the record if the
user is not responding in a suitable timescale. If you have diffculty
picking up the thread check it out on deja.com.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Record Locking - Who has locked it

- **From:** spanna2000@my-deja.com
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7updom$kn3$1@nnrp1.deja.com>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com> <380F5A5A.87D749D7@home.com>`

```
Ok. I take the point of that thread i.e. by application design there
are other ways to track multiple users working with the same but...

This system is getting into it's 20th year and doesn't have the benefit
of CICS or any other transaction processing environment. We're not
going to rewrite it - it mostly does the job - very well in fact, it's
fast reliable and _usually_ easy to maintain.

However, operator X (out of a possible 9999) has locked the customer
account record. The system won't allow any further access to that
record. Operator X has gone walkabout.

The operating system or EXTFH knows which operator has the lock, if we
could just find out who has the lock we could send somebody round to
unlock the process.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Record Locking - Who has locked it

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VTYP3.38$pD5.2793@dfiatx1-snr1.gtei.net>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com> <380F5A5A.87D749D7@home.com> <7updom$kn3$1@nnrp1.deja.com>`

```
We recently had a loooong thread on this "locking a record during lunch
break" issue, which might be worth reviewing.

What was not covered was using a logical lock. If the application used a
logical lock (i.e., wrote a marker into the file indicating an "in use"
status) there's no reason you could not store the user-ID who currently has
locked the record, too.

Solves many problems at once.

My $0.02
```

###### ↳ ↳ ↳ Re: Record Locking - Who has locked it

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uqh18$99n$1@aklobs.kc.net.nz>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com> <380F5A5A.87D749D7@home.com> <7updom$kn3$1@nnrp1.deja.com>`

```
spanna2000@my-deja.com wrote:

: The operating system or EXTFH knows which operator has the lock, if we
: could just find out who has the lock we could send somebody round to
: unlock the process.

You are making an unwarranted assumption that 'the operating
system or EXTFH' _knows_ which operator has the lock.

Certainly they know what is locked and when an unlock is
requested they probably can confirm that it is the same
process that requested the lock in the first place, but that
does _not_ mean that they store the process id let alone
the operator.

It may be, for example, that when a lock is obtained the
system (eg EXTFH) returns a token that is used in the
rewrite or unlock.  It is unlikely, but this is a viable
mechanism that aoids knowing the actual process.
```

###### ↳ ↳ ↳ Re: Record Locking - Who has locked it

_(reply depth: 4)_

- **From:** "Gerald Moull" <gerald@moull.freeserve.co.uk>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uvt22$35r$1@news5.svr.pol.co.uk>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com> <380F5A5A.87D749D7@home.com> <7updom$kn3$1@nnrp1.deja.com> <7uqh18$99n$1@aklobs.kc.net.nz>`

```
Somebody (or something) somewhere knows because RM has a call to get the PID
for locks.


Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7uqh18$99n$1@aklobs.kc.net.nz...
> spanna2000@my-deja.com wrote:
>
…[19 more quoted lines elided]…
> --
```

##### ↳ ↳ Re: Record Locking - Who has locked it

- **From:** Randall Bart <Barticus@usa.spam.net>
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hAoQOHtkk8SONMhXBPMhgtppRqVQ@4ax.com>`
- **References:** `<7ungfs$9sj$1@nnrp1.deja.com> <380F5A5A.87D749D7@home.com>`

```
The venerable "James J. Gavan" <jjgavan@home.com> bestowed upon
comp.lang.cobol on Thu, 21 Oct 1999 18:16:06 GMT these words:

>I think Randall Bart made the best point - put a time-stamp on records
>and perhaps use that same-time stamp to clear/unlock  the record if the
>user is not responding in a suitable timescale. If you have diffculty
>picking up the thread check it out on deja.com.

As Yogi Berra said, "I didn't really say all the things I said."  It
happens in other nesgroups and on the job as well.  Once at work a
co-worker asked a question, I replied that I was ignorant and proceded
to tell him several points I was ignorant about.  The next day he
said, "You were exactly right."

In this case, here is the message where "Randall Bart made the best
point":

>The venerable Arn Burkhoff <arnb@myself.com> bestowed upon
>comp.lang.cobol on Sat, 16 Oct 1999 08:45:27 -0400 these words:
…[9 more quoted lines elided]…
>This is the correct technique for most online database applications.

Keep at it, Arn.  Once you get a sage reputation you'll get credit for
other people's wisdom, too.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
