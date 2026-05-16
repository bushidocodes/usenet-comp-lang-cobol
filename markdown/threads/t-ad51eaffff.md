[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# convert cobol

_2 messages · 2 participants · 2001-06_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Re: convert cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-06T18:02:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1E6212.EACC265E@Azonic.co.nz>`

```
> It may be outdated for the customers, but not for me. I am not going
> to convert a 300,000 line package for someone who is love with their
> Macintosh or Web-TV or PalmPilot or PDP-8 or garage-door opener.

That's OK no one is going to ask you to (except, possibly, your
customers).

It may well be that you have yourself locked in to your platform.

However, you seem to have totally missed the point about 'cross platform
portability'.  There is no 'convert 300,000 lines'.  With, say, AcuCobol
(which I don't actually use) or even MF with Application Server, there
is no 'convert' there is not even 'recompile', and as long as some rules
have been followed and the code is competent there may not even be a
need to 'retest'.

I develop under Multiuser-DOS (because I like it and it does everything
I need without crashing) doing the code-compile-test cycle, then I
export it to SCO where it gets recompiled (though I actually could just
send .int) and from there sent to Linux if required.  If necessary it
gets put on a Windows machine and runs there (because I use SP2 it can
work as a Windows application).

When I first put one of my systems to Unix I had it running in half a
day and that included recoding some of the grubby stuff such as listing
files for selection.
 
> We don't make a product for the masses; our software costs
> significantly more than the hardware it runs on.

Then a few hundred dollars in run-time fees wouldn't hurt your market
much.  Or, more importantly, won't hurt your competitors much.
 
> When we get an inquiry (fortunately rare) about whether our software
> runs on a Mac, the prospect gets the same reaction as a car buyer
> would get from a Corvette dealership when he says: "Hey, I already own
> these truck tires. Can you make me a sports car that fits 'em? I want
> sumthin' com-pat-a-bly with my pickup!"

That, of course, is a nonsense analogy, and you seem to have it the
wrong way around.  You are making the customer buy the hardware (car) to
fit your software (tires) regardless of how compatible it is/isn't with
_anything_ he may already have.

But that's OK, if you don't need the market or want it then someone else
will fit the requirement using a cross-platform solution perhaps.

But, I can't recall that anyone here actually asked you to convert to
cross-platform, so why are you being so defensive about it ?

Just as long as you aren't insisting that we shouldn't be doing that
(which you come close to sometimes by saying it isn't valuable).
```

#### ↳ Re: convert cobol

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-06T22:49:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IryT6.280501$ho6.16980357@news5.aus1.giganews.com>`
- **References:** `<3B1E6212.EACC265E@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B1E6212.EACC265E@Azonic.co.nz...
> > It may be outdated for the customers, but not for me. I am not
going
> > to convert a 300,000 line package for someone who is love with
their
> > Macintosh or Web-TV or PalmPilot or PDP-8 or garage-door opener.
>
> That's OK no one is going to ask you to (except, possibly, your
> customers).

No, my 'customers' don't ask. Occasionaly a prospect will ask.

>
> It may well be that you have yourself locked in to your platform.

Yep. Sure have.

>
> However, you seem to have totally missed the point about 'cross
platform
> portability'.  There is no 'convert 300,000 lines'.  With, say,
AcuCobol
> (which I don't actually use) or even MF with Application Server,
there
> is no 'convert' there is not even 'recompile', and as long as some
rules
> have been followed and the code is competent there may not even be a
> need to 'retest'.

'Rules' to some means 'Restrictions' to others.

>
> I develop under Multiuser-DOS (because I like it and it does
everything
> I need without crashing) doing the code-compile-test cycle, then I
> export it to SCO where it gets recompiled (though I actually could
just
> send .int) and from there sent to Linux if required.  If necessary
it
> gets put on a Windows machine and runs there (because I use SP2 it
can
> work as a Windows application).

Hey, way cool.

>
> When I first put one of my systems to Unix I had it running in half
a
> day and that included recoding some of the grubby stuff such as
listing
> files for selection.

Excellent. If your business model includes Unix, not only did you
accomplish the 'conversion' in half a day (at not much cost), but you
now have a product you can offer to other Unix users. And I'm really,
really glad it works for you. I, on the other hand, have never
knowingly been in the same room with Unix and I never will.

>
> > We don't make a product for the masses; our software costs
> > significantly more than the hardware it runs on.
>
> Then a few hundred dollars in run-time fees wouldn't hurt your
market
> much.  Or, more importantly, won't hurt your competitors much.

We don't use runtime fees. And even if we were oblidged to do so, you
are correct: it would not hurt our market much. We don't have
competitors. Oh, there are some companies that have a primitive
version of what we do but it's like comparing a text editor to MSWord.

>
> > When we get an inquiry (fortunately rare) about whether our
software
> > runs on a Mac, the prospect gets the same reaction as a car buyer
> > would get from a Corvette dealership when he says: "Hey, I already
own
> > these truck tires. Can you make me a sports car that fits 'em? I
want
> > sumthin' com-pat-a-bly with my pickup!"
>
> That, of course, is a nonsense analogy, and you seem to have it the
> wrong way around.  You are making the customer buy the hardware
(car) to
> fit your software (tires) regardless of how compatible it is/isn't
with
> _anything_ he may already have.

Yeah, I guess the analogy works both ways. Point is, a thinking
prospect will focus on the desired solution - a combination of
hardware and software - and will obtain the combination that
accomplishes the task. To insist on a hardware restriction may (in our
case, certainly) limit the prospect's reaching his goal.

>
> But that's OK, if you don't need the market or want it then someone
else
> will fit the requirement using a cross-platform solution perhaps.

I'm not worried. If a competitor sprang up with that business plan,
I'd love it. In fact one of our competitors (I just found out) is
abandoning their text-based QNX system and intend to develop in (wait
for it now...) Linux. I almost died trying to stifle a Beaufort Force
VII giggle when they told me.

>
> But, I can't recall that anyone here actually asked you to convert
to
> cross-platform, so why are you being so defensive about it ?

Sigh. I know. I'm cursed with the compulsion to point out the Emperor
Has No Clothes.

>
> Just as long as you aren't insisting that we shouldn't be doing that
> (which you come close to sometimes by saying it isn't valuable).
>

No, no, no, I'm not insisting anyone do anything! I'm just forcefully
presenting facts sufficiently strong in themselves to compel a
rational mind to the certain conclusions.

If some developers want to take a different tack, I say "Go for it!"

I've always loved the slogan: "Unleash the Power of ConcurrentDOS!"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
