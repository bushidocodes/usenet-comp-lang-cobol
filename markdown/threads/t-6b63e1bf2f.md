[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trying to recreate problem of multi-user lockout

_6 messages · 3 participants · 2003-01_

---

### Trying to recreate problem of multi-user lockout

- **From:** renfrewthejust@yahoo.com (Renfrew)
- **Date:** 2003-01-29T05:00:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6e1fab7.0301290500.28d19529@posting.google.com>`

```
With sincerest thanks to JerryMouse, I am now convinced that 
Google is the holy grail of information mining on Usenet. 
If anyone knows of an even better way to research these 
archives, please break the news to me slowly, as I am not sure 
that my heart would stand the shock.  

Our system has been plagued with multi-user lockouts and index 
file corruptions for years.  Recently as a result of 
researching these problems I was quite delighted to discover 
what should be a solution to our problem, namely, to disable 
new file sharing and locking semantics in each workstation.  
We are currently using MF COBOL 3.4 (16-bit) and we will soon 
be moving up to Net Express (32-bit).  It is my understanding 
from what I have read in the archives that the same problem & 
solution apply to both products.

What I am trying to find out now is how to specifically 
recreate the problem.  The incidence of this problem for 
us has always been sporadic, making it too difficult for 
us to pinpoint an actual chain of events to recreate it.  
Does anyone have any suggestions on how I could set up a 
scenario between two users sharing one isam file to 
dependably cause a lockout and/or index corruption?  If 
we could do this then we could prove (and subsequently 
convince our system support folks) how turning off 
opportunistic locking will resolve our problem.  

I deeply appreciate any suggestions.  

Thanks,
DaveM
```

#### ↳ Re: Trying to recreate problem of multi-user lockout

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-29T08:43:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eLicnWOHvOeSdKqjXTWckQ@giganews.com>`
- **References:** `<d6e1fab7.0301290500.28d19529@posting.google.com>`

```

"Renfrew" <renfrewthejust@yahoo.com> wrote in message
news:d6e1fab7.0301290500.28d19529@posting.google.com...
> With sincerest thanks to JerryMouse, I am now convinced that
> Google is the holy grail of information mining on Usenet.
> If anyone knows of an even better way to research these
> archives, please break the news to me slowly, as I am not sure
> that my heart would stand the shock.

Our lesson for today is Google Groups:

Does the fact that the world knows about your query regarding breadcrumbs on
rec.food.cooking come as a shock? Or "Living in Sin?"

Let that be a lesson for all of us.

Bonus Lesson--

One of Google's new activities is still in beta: froogle.com. It purports to
ferret out the best prices on anything.
```

##### ↳ ↳ OT: Google Holy Grail (was:Trying to recreate problem of multi-user lockout)

- **From:** renfrewthejust@yahoo.com (Renfrew)
- **Date:** 2003-01-29T12:33:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6e1fab7.0301291233.7e2b4885@posting.google.com>`
- **References:** `<d6e1fab7.0301290500.28d19529@posting.google.com> <eLicnWOHvOeSdKqjXTWckQ@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<eLicnWOHvOeSdKqjXTWckQ@giganews.com>...
> "Renfrew" <renfrewthejust@yahoo.com> wrote in message
> news:d6e1fab7.0301290500.28d19529@posting.google.com...
…[12 more quoted lines elided]…
> 

Shocked?  No.  I must admit that I am rather clueless about what your
lesson really is about.  Please forgive me if I am misinterpreting
your intent, but if I had any reason to hide any of my postings then I
would have used an alternate id.

Nonetheless, I am still quite grateful.  I have tried unsuccessfully
for a very long time now to get our system support staff to give me an
outside modem line at work so that I could get to Usenet via my own
ISP, but this is no longer needed because Google provides an excellent
searching mechanism that also happens to be web-based.  No personal
ISP needed!  My holy grail remarks were made in complete sincerity.

DaveM
```

#### ↳ Re: Trying to recreate problem of multi-user lockout

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-29T08:10:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E37FCFA.1030803@Sympatico.ca>`
- **References:** `<d6e1fab7.0301290500.28d19529@posting.google.com>`

```
Renfrew wrote:
> With sincerest thanks to JerryMouse, I am now convinced that 
> Google is the holy grail of information mining on Usenet. 
…[13 more quoted lines elided]…
 >
I'm sorry that I did not notice this earlier, as we had
that problem and that solution for years now.  We use Fujitsu
though, so it did not twig that it could be the same problem.

I simply wrote a lock test program ... lock and leave it locked,
and set it up on several machines in my office. It did not
take long to prove that the file locking did NOT work without
disabling the new locking semantics on the server, particularly.

On the work stations, it did not seem to be critical for Fujitsu,
but then I do it as a matter of course on all PC's running Cobol.

Donald

> 
> What I am trying to find out now is how to specifically 
…[13 more quoted lines elided]…
> DaveM
```

##### ↳ ↳ Re: Trying to recreate problem of multi-user lockout

- **From:** renfrewthejust@yahoo.com (Renfrew)
- **Date:** 2003-01-29T12:03:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6e1fab7.0301291203.1d49180c@posting.google.com>`
- **References:** `<d6e1fab7.0301290500.28d19529@posting.google.com> <3E37FCFA.1030803@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote in message news:<3E37FCFA.1030803@Sympatico.ca>...
> Renfrew wrote:
> > Our system has been plagued with multi-user lockouts and index 
…[23 more quoted lines elided]…
> > DaveM

> I'm sorry that I did not notice this earlier, as we had
> that problem and that solution for years now.  We use Fujitsu
…[10 more quoted lines elided]…
> Donald

Could I ask you to describe more specifically what your lock test 
program does?  Am not asking you to write the program for me,
of course, but may I presume that you are doing something like
read-with-lock followed by an unanswered accept?  If so, then 
this is considerably simpler than what I had mentally pictured, 
which was something like iteratively
read-with-lock/pause-a-moment/chg-key-value/rewrite,   or,  
iteratively read-with-lock/pause-a-moment/delete/write.  I will go
ahead with the simple read-with-lock presumption for now.

If I am way off base here from what you were really trying to say, 
could you maybe send me a code snippet from your procedure div?

Many thanks for your help,
DaveM
```

###### ↳ ↳ ↳ Re: Trying to recreate problem of multi-user lockout

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-29T15:43:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E386713.90505@Sympatico.ca>`
- **References:** `<d6e1fab7.0301290500.28d19529@posting.google.com> <3E37FCFA.1030803@Sympatico.ca> <d6e1fab7.0301291203.1d49180c@posting.google.com>`

```
I simply opened a file, wrote out a hundred records, then set it up in a 
loop ... open,lock, add one to a counter in the record and re-write 
without releasing, delay 2 seconds, add one to second counter in the 
record, rewrite close, unlock. Ran that on four terminals, 
simultaneously, overnight. If the two counters (in each record) are 
equal at the end, then you are ok.  Of course, that method requires that 
you manually lock the record, rather than use locking is automatic. If 
you insert a re-read and re-lock after the first re-write and before the 
delay though, it should work with automatic locking as well.

If I remember correctly (it was a couple of years back), I tested it 
BEFORE applying the fix, to ensure that it would fail if record locking 
was NOT working, then ran it again with the fix on the second night. I 
was not really sure that record locking was the problem. That was back 
in win95, and I got enough failures on the first run (none on the 
second) to make me confident I had nailed it.  You might want to play 
with the delay a bit, but I just sat in a loop looking at current time. 
The granularity of the two second delay plus the small file should give 
you enough conflicts for it to work.  The keys I used were just the loop 
counter.

What I would do is use the select statements and read/write statements 
out of the original code, and use the first test to ensure that file 
locking is indeed the problem.  You can test it with file locking turned 
off, to make sure the code works. I simply looked at the file with my 
editor to see the problems ... wrote the code quick and dirty.

Donald

Renfrew wrote:
> Donald Tees <Donald_Tees@Sympatico.ca> wrote in message news:<3E37FCFA.1030803@Sympatico.ca>...
> 
…[58 more quoted lines elided]…
> DaveM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
