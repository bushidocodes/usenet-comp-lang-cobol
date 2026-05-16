[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# y2k rant

_48 messages · 19 participants · 1998-09 → 1998-10_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### y2k rant

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3603105D.97AF18FB@mindspring.com>`

```
i'm no professional and will probably be flamed to hell for this, but...

why were 2 extra digits such a big deal in the first place?  this could
not have been an unforseen occurrence!  even if the computer in question
was a commodore 64, 64k on those machines was put to incredible usage. 
remember "vorpal"?  vorpal loaded stuff as fast as windows loads a pgm
now.  not that i ever grasped it, but i know it worked like crazy.
point is:  are we all writing now to stave off the y3k crisis?  lol
```

#### ↳ Re: y2k rant

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tvk50$me8$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com>`

```

skidmike wrote in message <3603105D.97AF18FB@mindspring.com>...
>i'm no professional and will probably be flamed to hell for this, but...
>
>why were 2 extra digits such a big deal in the first place?  this could
>not have been an unforseen occurrence!  even if the computer in question
>was a commodore 64, 64k on those machines was put to incredible usage.


Well, I have code that goes back a lot further than a commodore 64.  That is
quite a recent computer.  Some of this code goes back to when 64k was worth
about 50 grand.

Secondly, you are forgetting manpower, which has always been expensive. I
have
people entering a date every 7 to 8 seconds.  Two extra keystrokes adds up
to a lot more than it costs to change the programs.  My code is set to
change
to four digits two weeks before the millennium, then to change back the day
after.
```

##### ↳ ↳ Re: y2k rant

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360435BC.60AB@sprynet.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net>`

```
Donald Tees wrote:
> 
> skidmike wrote in message <3603105D.97AF18FB@mindspring.com>...
…[16 more quoted lines elided]…
> after.

The first reason may be valid, but the second surely is not.  If you want to save
data entry time let them enter the two-digit year, but your program should be
smart enough to be able to tack on a reasonable century.
```

###### ↳ ↳ ↳ Re: y2k rant

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u1hin$oeb$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com>`

```

Frank Swarbrick wrote in message <360435BC.60AB@sprynet.com>...

>The first reason may be valid, but the second surely is not.  If you want
to save
>data entry time let them enter the two-digit year, but your program should
be
>smart enough to be able to tack on a reasonable century.
>--

Oh it is.  The point is that for a specific window, they are going
to have to ENTER the two digit century. That is necessary
for only a short period of time.  There are many cases where
the problems caused as Y2 are small enough that it is
still valid to use a two digit date.

On my own receivables, for example, I am not going to
fix anything.  So my ageing is inaccurate for 35-40 days.
I glance at it, mentally correct it, and thats it.  By the
end of the month, everything will work again.  I like
everything the way it is, and see no reason whatsoever
to have a full four digit year on everything.  It looks silly,
is more work, etc. etc. etc.

For the rest, my year end will take care of it with
opening balances for the first day of the millennium.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36049020.F4E9DC51@att.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1hin$oeb$1@news.igs.net>`

```
Donald Tees wrote:
> 
(snip)
> On my own receivables, for example, I am not going to
> fix anything.  So my ageing is inaccurate for 35-40 days.
…[4 more quoted lines elided]…
> is more work, etc. etc. etc.

This is one of the bases for making software Y2K compliant - internal
dates used in calculations/decision making must have 4-character years
(by windowing, entry, magic, etc.). Dates on screens, reports, etc., are
read and understood by humans and have no ambiguity (not in my area,
anyway). We decided this more than a year ago when we started making our
application software Y2K compliant.

Now, here's the kicker, I'm working on a major extension to one of our
systems - we're extending the system (securities movement & control) to
permit the entry of instructions by clients. I set up three new screens
with the (formerly) standard MM/DD/YY in the upper right. I was told to
display the date as MM/DD/YYYY, "to show the system is Y2K compliant" (I
kid you not). It's as much marketing, now, as compliance. I updated my
screens, of course.

Bill Lynch
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u2n64$jp4$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1hin$oeb$1@news.igs.net> <36049020.F4E9DC51@att.net>`

```

Bill Lynch wrote in message <36049020.F4E9DC51@att.net>...

>permit the entry of instructions by clients. I set up three new screens
>with the (formerly) standard MM/DD/YY in the upper right. I was told to
>display the date as MM/DD/YYYY, "to show the system is Y2K compliant" (I
>kid you not). It's as much marketing, now, as compliance. I updated my
>screens, of course.


Yes, it has become a bandwagon.  It would be silly, of course, to
say that the problem does not exist.  Unfortunately, there is
also a lot of "the sky is falling" involved too.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 5)_

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3605164C.211A@netbox.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1hin$oeb$1@news.igs.net> <36049020.F4E9DC51@att.net>`

```
Bill Lynch wrote:
> Now, here's the kicker, I'm working on a major extension to one of our
> systems - we're extending the system (securities movement & control) to
…[3 more quoted lines elided]…
> kid you not). It's as much marketing, now, as compliance. 

Perception is stronger than Truth.  applies to much in life.

Bob
```

###### ↳ ↳ ↳ Re: y2k rant

- **From:** "Mark Coulter" <mcoulter@mail.quik.com>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u1up0$k121@ns4.quik.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com>`

```
The biggest reason was punched card.  You only had 80 char. records.

Mark


Frank Swarbrick wrote in message <360435BC.60AB@sprynet.com>...
>Donald Tees wrote:
>>
…[7 more quoted lines elided]…
>> Well, I have code that goes back a lot further than a commodore 64.  That
is
>> quite a recent computer.  Some of this code goes back to when 64k was
worth
>> about 50 grand.
>>
>> Secondly, you are forgetting manpower, which has always been expensive. I
>> have
>> people entering a date every 7 to 8 seconds.  Two extra keystrokes adds
up
>> to a lot more than it costs to change the programs.  My code is set to
>> change
>> to four digits two weeks before the millennium, then to change back the
day
>> after.
>
>The first reason may be valid, but the second surely is not.  If you want
to save
>data entry time let them enter the two-digit year, but your program should
be
>smart enough to be able to tack on a reasonable century.
>--
>Frank Swarbrick
>home: infocat@sprynet.com
>work: frank.swarbrick@1stbank.com
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u2nge$jqc$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com>`

```

Mark Coulter wrote in message <6u1up0$k121@ns4.quik.com>...
>The biggest reason was punched card.  You only had 80 char. records.
>
>Mark


While I used lots of cards, I have never seen a program that
still exists where the 80 columns was the reason.  The
biggest reason was/is data entry efficiency.

Back in the 70's/80's there were scads
of people around that spent the day counting keystrokes and
finding ways to eliminate them.  Typing a "1" then a "9" several
hundred times per day was an easy one.

Whether the data was entered on a screen or a card was
quite irrelevant.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 5)_

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360900e6.1988096@news.teo-computer.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net>`

```
"Donald Tees" <donald@willmack.com> wrote:

>
>Mark Coulter wrote in message <6u1up0$k121@ns4.quik.com>...
…[8 more quoted lines elided]…
>

True.  Many people still haven't figured out that there are a huge
number of Excel spreadsheets that have been recording year fields as
two digits, because the data entry operator didn't want to continuely
have to redundantly start with "19".  When 2000 comes, the sort for
these fields won't work correctly, and if date calculations are part
of the spreadsheet, the calculations won't work properly.

Applications developed from Hollerith cards did primarily consider
resource and data entry efficiency.  And these apps have probably been
all replaced.  But I think, there is where a lot of the problem is.
So many times, the application is rewritten, but the data remains the
same.  This is a major mistake.  No longer are space resources
problems.  Even data entry efficiency isn't an issue anymore, because
of barcoding, other data feeds, smarter applications and systems,
etc., but the data isn't reformulated to meet the current needs.
Project management cuts out file conversions to save time to meet
project due dates.

In this scenerio, IMO it wasn't the people who wrote the original
punch card app the ones who created the problem, it was the project
manager in 1985 who was in charge of rewritting the app.


Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QNbO1.1212$_G3.989391@news2.mia.bellsouth.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com>`

```
I have this vision of a punched card program written 35 years ago, still
running using a virtual card reader, running on an emulator, which is
emulated on a later machine, which is emulated on a still later machine,
and so on.  I have seen close to this scenario, but it has been a while.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 7)_

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360997A4.F609DE08@mindspring.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net>`

```
but think of all the money the management bean-counter pukes saved on
upgrading!

Judson McClendon wrote:
> 
> I have this vision of a punched card program written 35 years ago, still
…[7 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uc711$9vn$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net>`

```

Judson McClendon wrote in message ...
>I have this vision of a punched card program written 35 years ago, still
>running using a virtual card reader, running on an emulator, which is
>emulated on a later machine, which is emulated on a still later machine,
>and so on.  I have seen close to this scenario, but it has been a while.


God<sorry Jud, it slipped out>, it happened to me with one of my own
creations.  I came across this hacked together with wire-wrap computer
loaded down with PROM code, circa about 1979, and realized that *I*
had built it.  I was terrified that the guy would find out I designed and
built
it and ask me to fix it.  Or worse yet, to change a function. I don't even
remember what CPU it was, let alone the assembler for it.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 7)_

- **From:** Francis A. Ney, Jr <croaker@access.digex.net>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VA.00001175.0012726d@access.digex.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net>`

```
> From: "Judson McClendon" <judmc123@bellsouth.net>
> Date: Wed, 23 Sep 1998 19:16:00 GMT
…[4 more quoted lines elided]…
> and so on.  I have seen close to this scenario, but it has been a while.

It's called the Internal Revenue Service.


Frank Ney  N4ZHG  WV/EMT-B  VA/EMT-A  LPWV  NRA(L)  GOA  CCRKBA  JPFO
Are you ready for Y2K?  Read "Time Bomb 2000" by Ed Yourdon
Abuses by the BATF  http://www.access.digex.net/~croaker/batfabus.html
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 8)_

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36102A1F.6E6C844C@mindspring.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net>`

```
(i can't believe i started this thread.  cut me some slack, i was
inebriated)
you're probably right.  the original source was for punch cards (i've
never even seen one!) and over the years, low-wage entry-level
programmers came and went; each modifying the source to accomodate 20th
century innovations like keyboards and monitors.  the programmers went
on to glory and the "system" plugged on, the users at least happy that
they didn't have to learn an entirely new system.  well, looks like the
moral is to satisfy the customer.  did you do that?
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uq6en$9g1$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com>`

```
skidmike wrote in message <36102A1F.6E6C844C@mindspring.com>...
>(i can't believe i started this thread.  cut me some slack, i was
>inebriated)
…[3 more quoted lines elided]…
>century innovations like keyboards and monitors.  the programmers went


Hey, why do you think the screen was invented with 80 columns?
*Everything* is historic ...
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 10)_

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3610d050.1618410@news.teo-computer.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net>`

```
"Donald Tees" <donald@willmack.com> wrote:

>skidmike wrote in message <36102A1F.6E6C844C@mindspring.com>...
>>(i can't believe i started this thread.  cut me some slack, i was
…[9 more quoted lines elided]…
>

Maybe a better word would be *legacy*.


Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 11)_

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn7125jp.66o.cadams@cadams-ntw.acucorp.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com>`

```
On 29 Sep 1998 05:21:46 PDT, Tim Oxler <tim.oxler@NOSPAMteo-computer.com>
wrote:
>>Hey, why do you think the screen was invented with 80 columns?  *Everything*
>>is historic ...

>Maybe a better word would be *legacy*.

Apparently some people decided that wasn't polite enough and started using
"heritage".

As an example of how this works out, consider
http://www.iprg.nokia.com/~pn/standards.html - now that's a legacy standard!

----
The opinions above are my own and may or may not match those of my employer.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 11)_

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361163CE.EBA237F7@mindspring.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com>`

```
came up with another analogy on a test drive today.
someone bought a 57 chevy new 41 years ago.
over the years, the bias-ply tires and 5" wide steel wheels were
replaced with 7" wide aluminum wheels with radial tires.
the single-circuit drum brake system got a dual-circuit master cylinder
and front discs.
single exhaust became duals.
the generator was replaced with an alternator (usually that means the
"generator" light stays on until the bulb burns out)
but for those 41 years, it remained a 57 chevy.  it goes from point a to
point b (yes just as fast as you want), seats as many passengers as 1998
models it's size, if properly maintained the gas mileage is acceptable.
the little old lady who owns it doesn't want to spend money on a new car
because she just doesn't want to spend the money.
same for the "emulator on an emulator..."  the user has something they
are comfortable with and think they are saving money by not upgrading.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 11)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uqsac$rdh$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com>`

```

Tim Oxler wrote in message <3610d050.1618410@news.teo-computer.com>...
>"Donald Tees" <donald@willmack.com> wrote:
>>*Everything* is historic ...
>Maybe a better word would be *legacy*.
>
Why is that?
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 12)_

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361127a8.23981919@news.teo-computer.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net>`

```
"Donald Tees" <donald@willmack.com> wrote:

>
>Tim Oxler wrote in message <3610d050.1618410@news.teo-computer.com>...
…[6 more quoted lines elided]…
>

Legacy means: Something handed down by predecessor. The word is more
accurate.

Historic, means something famous or important in history.  Admittedly,
monitors were a vast improvement from cardpunch and line readers
(BTDT), and *historic* to the programmers at that time.   But, I
wouldn't go as far as to say the 80 column design was *historic*.


Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 13)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6urhcf$pds$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com>`

```
Tim Oxler wrote in message <361127a8.23981919@news.teo-computer.com>...
>"Donald Tees" <donald@willmack.com> wrote:
>>>Maybe a better word would be *legacy*.
…[6 more quoted lines elided]…
>wouldn't go as far as to say the 80 column design was *historic*.


At the risk of getting into a "how many angels can dance<g>" type of
argument, I would disagree.  "Legacy" implies legality.  In fact, my
dictionary gives it's main definition as money or property given over
by a will. Historic, on the other hand, simply refers to something
important from the past.  As "importance" is governed by influence
on the present,  I would submit that the 80 column figure is of historic
influence, rather than a "legacy" from the past.

Unless, of course, you inherited your computer, in which case it
is a legacy.  Or you are a lawyer, in which case words are meant
to impress without commitment.  Or a programmer, in which case
you have to look them up in a symbol table.

In the final analysis, only the caterpillar knows.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 14)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611C641.73FD1C10@att.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <6urhcf$pds$1@news.igs.net>`

```
Donald Tees wrote:
> 
(snip)
> 
> Unless, of course, you inherited your computer, in which case it
> is a legacy.  Or you are a lawyer, in which case words are meant
> to impress without commitment.  Or a programmer, in which case
> you have to look them up in a symbol table.

My Webster's CD had the following for "legacy":

legacy (lege se) pl. -cies n.

1	money or property left to someone by a will; bequest

2	anything handed down from, or as from, an ancestor

Etymology [ME legacie < OFr < ML legatia < L legatus: see legate]

(C)1995 Zane Publishing, Inc.   (C)1994, 1991, 1988 Simon & Schuster,
Inc."

Wouldn't no. 2 apply here?

Bill Lynch

PS: What caterpillar? :-\
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 15)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ut390$n8e$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net>`

```

Bill Lynch wrote in message <3611C641.73FD1C10@att.net>...
>Donald Tees wrote:

>PS: What caterpillar? :-\

The one in Alice in Wonderland, who said (in reply to"don't
you mean ...")  "My words mean exactly what I mean them
to mean, nothing more and nothing less."

Upon reflection, however, perhaps I will recant.  Historical
would have been a better choice than historic.

;<)
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 16)_

- **From:** traveler <Hbp1@cris.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SUN.4.01.9809300811140.11923-100000@galileo.cris.com>`
- **References:** `<6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net> <6ut390$n8e$1@news.igs.net>`

```
   Perhaps  HYSTERICAL  would be more  appropriate to this silly semantic
discussion.
       harlow pease





On Wed, 30 Sep 1998, Donald Tees wrote:

> 
> Bill Lynch wrote in message <3611C641.73FD1C10@att.net>...
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 16)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utd6u$pkg$1@clarknet.clark.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net> <6ut390$n8e$1@news.igs.net>`

```
In article <6ut390$n8e$1@news.igs.net>,
Donald Tees <donald@willmack.com> wrote:
>
>Bill Lynch wrote in message <3611C641.73FD1C10@att.net>...
…[6 more quoted lines elided]…
>to mean, nothing more and nothing less."

I believe that was Humpty Dumpty, not the Caterpillar.

DD
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 17)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uvo2l$k2a$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net> <6ut390$n8e$1@news.igs.net> <6utd6u$pkg$1@clarknet.clark.net>`

```
docdwarf@clark.net wrote in message <6utd6u$pkg$1@clarknet.clark.net>...

>>The one in Alice in Wonderland, who said (in reply to"don't
>>you mean ...")  "My words mean exactly what I mean them
>>to mean, nothing more and nothing less."
>
>I believe that was Humpty Dumpty, not the Caterpillar.


Naw, it was the caterpiller.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 17)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298273.12844.19012@kcbbs.gen.nz>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net>`

```
In message <<6utd6u$pkg$1@clarknet.clark.net>> docdwarf@clark.net  writes:
> >
> >The one in Alice in Wonderland, who said (in reply to"don't
…[6 more quoted lines elided]…
> 

Humpty Dumpty ?  in WonderLand ?  You are very confused.

I can't quite remember if it was TweedleDee or TweedleDum
though.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 18)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3614230B.16A5@swbell.net>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz>`

```
Richard Plinston wrote:
> 
> In message <<6utd6u$pkg$1@clarknet.clark.net>> docdwarf@clark.net  writes:
…[13 more quoted lines elided]…
> though.

Through the Looking-Glass, chapter VI (with italics in the original
rendered by bracketing asterisks):

	"But 'glory' doesn't mean 'a nice knock-down argument," Alice
	objected.

	"When *I* use a word," Humpty Dumpty said, in rather a scornful
	tone, "it means just what I choose it to mean--neither more
	nor less."

	"The question is," said Alice, "whether you *can* make words
	mean so many different things."

	"The question is," said Humpty Dumpty, "which is to be master--
	that's all."

Michael C. Kasten	mc9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 19)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v2hpi$7im$1@news.igs.net>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz> <3614230B.16A5@swbell.net>`

```

Michael C. Kasten wrote in message <3614230B.16A5@swbell.net>...
>Richard Plinston wrote:

> "When *I* use a word," Humpty Dumpty said, in rather a scornful
> tone, "it means just what I choose it to mean--neither more
> nor less."
>
Thanks, saved me a trip to the library, as I don't have a copy. I
could have sworn it was the caterpillar ...
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 20)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v2n41$rht$1@callisto.clark.net>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz> <3614230B.16A5@swbell.net> <6v2hpi$7im$1@news.igs.net>`

```
In article <6v2hpi$7im$1@news.igs.net>,
Donald Tees <donald@willmack.com> wrote:
>
>Michael C. Kasten wrote in message <3614230B.16A5@swbell.net>...
…[7 more quoted lines elided]…
>could have sworn it was the caterpillar ...

... which is why I, personally, save swearing for times of Great Distress.

DD
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 18)_

- **From:** dlparker@dlpinc00.com (Dave Parker)
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F05Atz.CEE.0.uw@dlpinc00.com>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz>`

```
Richard Plinston (riplin@kcbbs.gen.nz) wrote:
: In message <<6utd6u$pkg$1@clarknet.clark.net>> docdwarf@clark.net  writes:
: > >
: > >The one in Alice in Wonderland, who said (in reply to"don't
: > >you mean ...")  "My words mean exactly what I mean them
: > >to mean, nothing more and nothing less."
: > 
: > I believe that was Humpty Dumpty, not the Caterpillar.
: > 
: > DD
: > 

: Humpty Dumpty ?  in WonderLand ?  You are very confused.

Maybe.  But he WAS there.  But I already know I'm confused.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 18)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v05ee$2c4$1@callisto.clark.net>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz>`

```
In article <3298273.12844.19012@kcbbs.gen.nz>,
Richard Plinston <riplin@kcbbs.gen.nz> wrote:
>In message <<6utd6u$pkg$1@clarknet.clark.net>> docdwarf@clark.net  writes:
>> >
…[9 more quoted lines elided]…
>Humpty Dumpty ?  in WonderLand ?  You are very confused.

No, Humpty was Through The Looking-Glass, true... but also it was he who
issued this pronouncement on language, if my porous memory serves.

>
>I can't quite remember if it was TweedleDee or TweedleDum
>though.

Substance for another thread, perhaps.

DD
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 18)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3613a891.14261505@news.enter.net>`
- **References:** `<6utd6u$pkg$1@clarknet.clark.net> <3298273.12844.19012@kcbbs.gen.nz>`

```
riplin@kcbbs.gen.nz (Richard Plinston) wrote:

>In message <<6utd6u$pkg$1@clarknet.clark.net>> docdwarf@clark.net  writes:
>> >
…[13 more quoted lines elided]…
>

Are you sure that it didn't occur at the Mad Hatter's Tea Party...I
believe that the dialog went something like this when the Mad Hatter
asked Alice to solve a riddle:


`Do you mean that you think you can find out the answer to it?' said
the March Hare. 

`Exactly so,' said Alice. 

`Then you should say what you mean,' the March Hare went on. 

`I do,' Alice hastily replied; `at least--at least I mean what I
say--that's the same thing, you know.' 

`Not the same thing a bit!' said the Hatter. `You might just as well
say that "I see what I eat" is the same thing as
"I eat what I see"!' 

`You might just as well say,' added the March Hare, `that "I like what
I get" is the same thing as "I get what I
like"!' 

`You might just as well say,' added the Dormouse, who seemed to be
talking in his sleep, `that "I breathe when I
sleep" is the same thing as "I sleep when I breathe"!' 

`It IS the same thing with you,' said the Hatter, and here the
conversation dropped, and the party sat silent for a
minute, while Alice thought over all she could remember about ravens
and writing-desks, which wasn't much. 



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 15)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ut5i6$qrb$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net>`

```
Bill Lynch wrote in message <3611C641.73FD1C10@att.net>...
>Donald Tees wrote:
>1 money or property left to someone by a will; bequest
>2 anything handed down from, or as from, an ancestor
>Wouldn't no. 2 apply here?


PS.  Nope<s>.  You see, Bill, I am over fifty.  My ancestors
did not use computers at all, I was the first generation. The
number 80(as a data size), is simply an accident of history,
or, if you will, a historical number. (hysterical?)

"Legacy" is just a way for the young guys to absolve themselves
of any responsibility.  I have not fixed any "legacy" Y2 code
either.  I have changed *my own* code that would "break"
in the year 2000 so that it will not.  I just changed the data names
containing "YEAR"  to "NEW-YEAR", then went through
all the syntax errors that it caused, and checked the code.
As I found other pertinent two digit names, I did the same.
Got it all done last year. To my mind, it is no different than
any other change in spec.

I write code to last about ten years, as a rule. If it lasts longer
than that, then it will need an overhaul for new platforms, etc.
before the ten years is up.  When I do that, I try to ensure it
will work for another ten years or  so.

Did you ever notice that all Y2 problems occur in "other"
people's code? One would think from the language used that
no bugs exist in any code written after 1902, and all bugs
that do exist are traceable to programmers that died two
hundred years back.  "Legacy" my ass.  Lawyer talk.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 15)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ut692$rs0$1@news.igs.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <6urhcf$pds$1@news.igs.net> <3611C641.73FD1C10@att.net>`

```

Bill Lynch wrote in message <3611C641.73FD1C10@att.net>...
>PS

PPS.  There.  I have had my morning coffee, and my daily rant.
Now if I can find a junior programmer to kick, I will be ready to
start writing code.
;<)
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 13)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611C569.18C750B6@att.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com>`

```
Tim Oxler wrote:
> 
(snip)
> Legacy means: Something handed down by predecessor. The word is more
> accurate.
…[4 more quoted lines elided]…
> wouldn't go as far as to say the 80 column design was *historic*.

Not arguing with "legacy", but would "historical" also be acceptable?

Bill Lynch
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 14)_

- **From:** dlparker@dlpinc00.com (Dave Parker)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F03Gz9.32v.0.uw@dlpinc00.com>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net> <3610d050.1618410@news.teo-computer.com> <6uqsac$rdh$1@news.igs.net> <361127a8.23981919@news.teo-computer.com> <3611C569.18C750B6@att.net>`

```
Bill Lynch (wblynch@att.net) wrote:
: Tim Oxler wrote:
: > 
: (snip)
: > Legacy means: Something handed down by predecessor. The word is more
: > accurate.
: > 
: > Historic, means something famous or important in history.  Admittedly,
: > monitors were a vast improvement from cardpunch and line readers
: > (BTDT), and *historic* to the programmers at that time.   But, I
: > wouldn't go as far as to say the 80 column design was *historic*.

: Not arguing with "legacy", but would "historical" also be acceptable?

Not to overwork the many varied and creative uses of the non-sequiter
exhibited in this highly entertaining ng, but:

Given the benefits of our 20-20 hindsight that we've all exercised
throughout this thread, how about 'hysterical'??  Not that those of us
now benefitting financially from the (largely) managerial
short-sightedness have any reason to quibble over semantics...
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 10)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611C4EE.937C1A5F@att.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com> <6tvk50$me8$1@news.igs.net> <360435BC.60AB@sprynet.com> <6u1up0$k121@ns4.quik.com> <6u2nge$jqc$1@news.igs.net> <360900e6.1988096@news.teo-computer.com> <QNbO1.1212$_G3.989391@news2.mia.bellsouth.net> <VA.00001175.0012726d@access.digex.net> <36102A1F.6E6C844C@mindspring.com> <6uq6en$9g1$1@news.igs.net>`

```
Donald Tees wrote:
> 
(snip)
> 
> Hey, why do you think the screen was invented with 80 columns?
> *Everything* is historic ...

Not all screens were born with 80 columns, e.g., the 3270 Model 1 (long
forgotten, and rightly so) was 40 columns wide (I'm concluding it had
only 12 lines, as I recall the buffer size as 480). Anyone here recall
the specs for a 2260?

Bill Lynch
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 11)_

- **From:** fboll@aol.com (FBoll)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980930135001.22896.00003416@ng78.aol.com>`
- **References:** `<3611C4EE.937C1A5F@att.net>`

```

>Not all screens were born with 80 columns, e.g., the 3270 Model 1 (long
>forgotten, and rightly so) was 40 columns wide (I'm concluding it had
…[3 more quoted lines elided]…
>

The mind boggles to think  that when I got into programming the Second Gen
folks (7074) used to call me a "Young Tirk" 
Frank J. Boll
Computer Solutions
This message printed on recycled disk space
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 12)_

- **From:** fboll@aol.com (FBoll)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980930135516.22896.00003417@ng78.aol.com>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com>`

```

Make that "Young TURK"
Frank J. Boll
Computer Solutions
This message printed on recycled disk space
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com> <19980930135516.22896.00003417@ng78.aol.com>`

```
FBoll wrote:
>
>Make that "Young TURK"


That's okay, it could have been worse. :-)
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 14)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utvg0$d8b$1@callisto.clark.net>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com> <19980930135516.22896.00003417@ng78.aol.com> <BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net>`

```
In article <BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net>,
Judson McClendon <judmc123@bellsouth.net> wrote:
>FBoll wrote:
>>
…[3 more quoted lines elided]…
>That's okay, it could have been worse. :-)

How much wirse?

DD
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xovQ1.1242$2P.1802112@news2.mia.bellsouth.net>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com> <19980930135516.22896.00003417@ng78.aol.com> <BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net> <6utvg0$d8b$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:
>Judson McClendon wrote:
>>FBoll wrote:
…[5 more quoted lines elided]…
>How much wirse?


He could have mistyped the 'K'.  That could be pretty wirse.
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 16)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uu29p$o2$1@clarknet.clark.net>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com> <BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net> <6utvg0$d8b$1@callisto.clark.net> <xovQ1.1242$2P.1802112@news2.mia.bellsouth.net>`

```
In article <xovQ1.1242$2P.1802112@news2.mia.bellsouth.net>,
Judson McClendon <judmc123@bellsouth.net> wrote:
>docdwarf@clark.net wrote:
>>Judson McClendon wrote:
…[9 more quoted lines elided]…
>He could have mistyped the 'K'.  That could be pretty wirse.

Hmmmm... on a qwerty keyboard the usual typos for 'K' are things like 'L'
or 'I'... not often 'D'.

DD
```

###### ↳ ↳ ↳ Re: y2k rant

_(reply depth: 17)_

- **From:** "Art Perry" <arthur.perry@eds88.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uua9r$6no$1@news.ses.cio.eds.com>`
- **References:** `<19980930135001.22896.00003416@ng78.aol.com> <BNuQ1.1230$2P.1780790@news2.mia.bellsouth.net> <6utvg0$d8b$1@callisto.clark.net> <xovQ1.1242$2P.1802112@news2.mia.bellsouth.net> <6uu29p$o2$1@clarknet.clark.net>`

```

docdwarf@clark.net wrote in message <6uu29p$o2$1@clarknet.clark.net>...
-snip-
>Hmmmm... on a qwerty keyboard the usual typos for 'K' are things like 'L'
>or 'I'... not often 'D'.

If you are ambidextrous, it could happen...      ;)
```

###### ↳ ↳ ↳ Re: y2k rant

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980927232040.06325.00000891@ngol02.aol.com>`
- **References:** `<360435BC.60AB@sprynet.com>`

```

In article <360435BC.60AB@sprynet.com>, Frank Swarbrick <infocat@sprynet.com>
writes:

>f you want to save
>data entry time let them enter the two-digit year, but your program should be
>smart enough to be able to tack on a reasonable century.

If you are running a program. Many of our data structures started out as master
card decks that were processed on tabulating machines (yes, the kind that were
"programmed" by running wires on a patch panel). When our shop moved over to a
computer, the same record layouts were kept so that, if necessary, it would be
easy to move from the computer back to the tabulating machine. So then we had
programs processing 80-column master files. And from then, on, it was easier to
write additional programs without changing the layout of the master files. It
was later that the master decks became disk files (SAM, some ISAM, and now lots
of VSAM), but in each case it was easier to preserve the existing record
layouts than to alter the record layouts _and_ change all the programs that
accessed those layouts. Record layouts were grown but, again, it was easier to
preserve the layout of the existing fields rather than change the existing
fields and dig into each program that uses the changed fields. This progression
is what Harlain has referred to as "Ever depening ruts."

The original patch panels and the old programs are long gone, but the ruts from
the data structure lived on because we were told that "There will be pleanty of
time to change it later" and "We don't want to take the time to change it now."

Likewise, when we have talked about moving to a more modern data repository
(e.g., DB/2, IBM's mainframe SQL database), there has been a lot of reluctance
to allow us to change existing data because of the time required to restructure
the data (rather than just take those modified card images from the tabulating
machine days and dumping them into unnormalized tables). We have started
analyzing and normalizing our data structures, but there is no way that will be
completed before the year 00, so we have added windowing logic to many of our
existing programs. (Some of our date fields already have 4-digit years: many
"future effective date" transactions, birth dates, registration refund data, as
well as the application we have already moved into SQL.)


Mark A. Young
```

#### ↳ Re: y2k rant

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V%LM1.2705$kN6.3030438@news2.mia.bellsouth.net>`
- **References:** `<3603105D.97AF18FB@mindspring.com>`

```
skidmike wrote:
>i'm no professional and will probably be flamed to hell for this, but...
>
…[5 more quoted lines elided]…
>point is:  are we all writing now to stave off the y3k crisis?  lol

No, it certainly was foreseen.  But those who only got into the computer
business in the last 15 years or so simply cannot understand how tight
memory and CPU resources were, 20 to 30 years ago.  Also, what was *not*
clear before 1980 was that computer systems written in COBOL would have
such longevity.  COBOL wasn't even 20 years old yet, the pace of change
was unprecedented, and there was no precedent to indicate that systems
written then would still be in use over 20 years later.  And it is one
thing to foresee a problem, it is quite another to have the resources to
avoid it, 20 or 30 years ahead of time.  No, given the conditions at the
time, using two digit year *was* the correct decision.  The error was in
not correcting the problem after the mid 80's (when we *did* have 20 year
old systems), and to continue to use two digit year for new systems well
into the 90's.  The former was mostly a management failure.  The latter,
when it occurred, was a shared failure of programmers and management.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
