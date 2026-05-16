[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is COBOL Dying?

_4 messages · 4 participants · 2001-03 → 2001-04_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### Re: Is COBOL Dying?

- **From:** "Editor" <Editor@aboutlegacycoding.com>
- **Date:** 2001-03-19T09:45:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IQot6.13$Ow1.173@client>`
- **References:** `<1103_983741242@micron-450> <98eit0$dk7$1@slb6.atl.mindspring.net> <3AAE877E.7F8A52EA@home.com> <fm50btsc1thvj5und03bo8l2quh5ha0nqq@4ax.com>`

```
I think the hardware you are referring to (with the Pentium Chip) is
probably the Unisys ClearPath machine.  It has a "mainframe" side and an NT
side closely married in the same box.
Their most recent hardware is all NT with an emulator for the Mainframe
side.

I agree with other posts in this forum pointing out that there are some
systems where the number of transactions and the size of the data really
can't be handled by anything other than a "mainframe" system today.
However, there are a HUGE number of companies out there, with really well
written COBOL programs that would run just fine on a large Unix or NT
system.  In most cases, when those systems were written, years ago, the
Mainframe was chosen because it was the only option.  In many cases these
systems also don't really need five nines of uptime - they are batch jobs
that could wait a few minutes if an NT box has to be rebooted (Oh, but wait,
NT boxes never have to be rebooted - I forgot :-).

But over time, the cost of maintaining their "big iron" hardware (HW and SW
maintenance, facilities, AC, power, 24/7 operators, etc.) became huge
comparied to maintaining a smaller Unix box.  And a Unix or NT box now has
more than enough horsepower to get the job done.

My company has largely made an entire service business out of porting
systems from mainframes to Unix or NT systems.  We are in process of bidding
on a job right now with a large Insurance Company.  Their ROI on moving the
code is about 18 months and getting shorter all the time as the Mainframe
manufacturer sticks them with higher and higher maintenance fees the older
the box gets.

So no - COBOL isn't dying - it's just going to move to less expenisve
hardware where appropriate.
It's the hardware that's dying.  And did any of us expect it to live forever
anyway?

Buddy Ray
The Progeni Corporation
www.progeni.com

"G Moore" <gvwmoore@spam.ix.netcom.com> wrote in message
news:fm50btsc1thvj5und03bo8l2quh5ha0nqq@4ax.com...
> "David A. Cobb" <superbiskit@home.com> wrote:
>
…[3 more quoted lines elided]…
> >such "unromantic" applications which live or die by their
COBOL-programmed
> >support can afford to shut off the mainframes for a few years while we
replace
> >all our old junk with newer and much more fragile junk.  Then COBOL can
die
> >in piece.
>
…[36 more quoted lines elided]…
> nonesofar
```

#### ↳ Re: Is COBOL Dying?

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-03-27T01:00:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABFE58E.44E33FCC@istar.ca>`
- **References:** `<1103_983741242@micron-450> <98eit0$dk7$1@slb6.atl.mindspring.net> <3AAE877E.7F8A52EA@home.com> <fm50btsc1thvj5und03bo8l2quh5ha0nqq@4ax.com> <IQot6.13$Ow1.173@client>`

```
Ray:

If the company in question got an IBM Multiprise 3000 (60 - 120 mips),
would it be an appropriate size box?  If so, depending on what they are
currently running, they MIGHT be able to save on hardware, software and
environmental costs.  Also the current IBM COBOL compilers have some
really interesting optimizations.

Clark Morris, CFM Technical Programming Services Inc.

Editor wrote:
> 
> I think the hardware you are referring to (with the Pentium Chip) is
…[88 more quoted lines elided]…
> > nonesofar
```

#### ↳ Re: Is COBOL Dying?

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2001-04-09T14:13:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j36fau8tkmdfp46bf217qglcs0q9loojil@4ax.com>`
- **References:** `<1103_983741242@micron-450> <98eit0$dk7$1@slb6.atl.mindspring.net> <3AAE877E.7F8A52EA@home.com> <fm50btsc1thvj5und03bo8l2quh5ha0nqq@4ax.com> <IQot6.13$Ow1.173@client>`

```
"Editor" <Editor@aboutlegacycoding.com> wrote:

>Their ROI on moving the
>code is about 18 months and getting shorter all the time as the Mainframe
>manufacturer sticks them with higher and higher maintenance fees the older
>the box gets.

whats roi?

reply to email gvwmoore@spam.ix.netcom.com 
remove the spam

points in agreement snipped

spambots pick up these spambots addys

nonesofar
```

##### ↳ ↳ Re: Is COBOL Dying?

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-11T12:30:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad3a8a7_1@my.newsfeeds.com>`
- **References:** `<1103_983741242@micron-450> <98eit0$dk7$1@slb6.atl.mindspring.net> <3AAE877E.7F8A52EA@home.com> <fm50btsc1thvj5und03bo8l2quh5ha0nqq@4ax.com> <IQot6.13$Ow1.173@client> <j36fau8tkmdfp46bf217qglcs0q9loojil@4ax.com>`

```
Return On Investment

Pete.

G Moore wrote in message ...

>
>whats roi?
>




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
