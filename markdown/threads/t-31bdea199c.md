[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FUNCTION's LOCALE-(DATE/TIME)

_48 messages · 10 participants · 2007-03_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### FUNCTION's LOCALE-(DATE/TIME)

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T10:17:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esgn79$uik$02$1@news.t-online.com>`

```
Not a question about implementation, more a question
of expected results for eg. America
(Locale "en_US")

LOCALE-DATE
Let's take March 2 1963
Would that be :
3/2/1963
or :
03/02/1963
(General european is clear - 02.03.1963, eg. for de_DE)

LOCALE-TIME
Let's take 23:30:12
Would that be :
11:30:12 PM

or does America generally work on 24-hour clock ?

Roger
```

#### ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-05T10:57:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WISGh.90460$lb3.32244@fe08.news.easynews.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com>`

```
Roger,
   I am not certain what the "expectations" are  (for NON C-typle Locale), but 
you might want to look at what IBM provides for defaults in their "language 
environment services" at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3130/A.0

That does show:
   ZH:MI:SS AP   (for time - which means it is using the 12 hour clock with AM / 
PM, and the leading "Z" means "zero-suprresion")

and
  MM/DD/YY (which means ALWAYS use a 2-digit value - even with leading zeroes)
```

##### ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T12:25:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esgunf$dv8$03$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:WISGh.90460$lb3.32244@fe08.news.easynews.com...
> Roger,
>   I am not certain what the "expectations" are  (for NON C-typle Locale), 
…[7 more quoted lines elided]…
> AM / PM, and the leading "Z" means "zero-suprresion")

OK. Seems reasonable. That's what OC gets under Win and Linux/Unix.

>
> and
>  MM/DD/YY (which means ALWAYS use a 2-digit value - even with leading 
> zeroes)
>

This is interesting. Linux/unix does exactly that with en_US locale.
Windows does not; it does zero suppression (with equivalent of en_US, -
Locale ID 0x0409)

Roger

> -- 
> Bill Klein
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-05T07:21:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com>`
- **In-Reply-To:** `<esgunf$dv8$03$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com>`

```
Roger While wrote:
> "William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
> news:WISGh.90460$lb3.32244@fe08.news.easynews.com...
…[6 more quoted lines elided]…
> Locale ID 0x0409)

I've found that a lot of things use the actual settings in Windows.  Try 
going into Regional settings, and change the "short date" to include the 
leading zeroes - you may find that you'll get them then.  (This may or 
may not be an acceptable way to fix the problem, but it would identify 
where the format may be being changed.)
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T16:51:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eshe9s$q50$01$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> schrieb im Newsbeitrag 
news:htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com...
> Roger While wrote:
>> "William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
…[14 more quoted lines elided]…
>

That was an excellent idea. Indeed, English/USA is per default
set to zero-suppression.
Now I wonder if I can influence that at the C level.

I suppose it all depends on "typical" usage.
Annoying that in this respect Win gives (per default)
different results to Linux/Unix.

Roger
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-05T09:32:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173115927.324096.235450@c51g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<eshe9s$q50$01$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com>`

```
On Mar 6, 4:51 am, "Roger While" <s...@sim-basis.de> wrote:
> "LX-i" <lxi0...@netscape.net> schrieb im Newsbeitragnews:htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com...

> Annoying that in this respect Win gives (per default)
> different results to Linux/Unix.

Standard practice for Microsoft. Change (or ignore) what everyone else
does then claim that the Microsoft way _is_ the standard and everyone
else is wrong.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 6)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-05T19:53:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eshoul$nir$00$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> schrieb im Newsbeitrag 
news:1173115927.324096.235450@c51g2000cwc.googlegroups.com...
> On Mar 6, 4:51 am, "Roger While" <s...@sim-basis.de> wrote:
>> "LX-i" <lxi0...@netscape.net> schrieb im 
…[7 more quoted lines elided]…
> else is wrong.

Well, some info -
Windows (before Vista) does not know about a locale
name, it only knows about locale "ID's".
Now Linux/unix have had locale names since ....

So, support for LOCALE.

Logically, we would use something like
de_DE@euro.

Win (before Vista) does not know about these things.
(And even with vista, is then "de-DE")
(Note the dash, underline difference)

So, how to get from a locale name to a locale ID.
Well, MS have a "DownLocal..whatever"" which
a) requires an extra library to be installed from MS
and
b) Is only applicable to Win XP Sp2
:-(

So, to implement this in OC, we reproduce the
complete (from MS) table name->id
(and do a string compare from the (truncated at any
 non-alphanum character), noting that we use the Linux/Unix name
 with underline)
and use the Win GetDateFormat/GetTimeFormat.

Geez.

Note this still does not solve how to get the (Cobol correct?)
format

Roger
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-05T19:03:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xs-dnca6pL-FUXHYnZ2dnUVZ_hynnZ2d@comcast.com>`
- **In-Reply-To:** `<eshoul$nir$00$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <eshoul$nir$00$1@news.t-online.com>`

```
Roger While wrote:
> Well, some info -
> Windows (before Vista) does not know about a locale
> name, it only knows about locale "ID's".
> Now Linux/unix have had locale names since ....

You mentioned what you could do for XP SP2 - does Vista actually return 
what you expect?

The only experience I had with this was when I changed the date/time 
formats on a server, and some code that parsed the date broke.  :)  I 
think it was ASP, though it might have been PHP.  I had to change it back.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 8)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-06T07:17:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esj12j$vrr$01$1@news.t-online.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <eshoul$nir$00$1@news.t-online.com> <Xs-dnca6pL-FUXHYnZ2dnUVZ_hynnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> schrieb im Newsbeitrag 
news:Xs-dnca6pL-FUXHYnZ2dnUVZ_hynnZ2d@comcast.com...
> Roger While wrote:
>> Well, some info -
…[6 more quoted lines elided]…
>

No, because the system date settings for en_US remain the same as in
XP.
The only thing Vista has in this area is extra library functions to accept
a locale name instead of a locale id.
eg. GetDateFormatEx/GetTimeFormatEx


> The only experience I had with this was when I changed the date/time 
> formats on a server, and some code that parsed the date broke.  :)  I 
> think it was ASP, though it might have been PHP.  I had to change it back.
>

Ouch.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-05T19:22:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12upgigd0cjkqab@news.supernews.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com>`

```
Richard wrote:
> On Mar 6, 4:51 am, "Roger While" <s...@sim-basis.de> wrote:
>> "LX-i" <lxi0...@netscape.net> schrieb im
…[7 more quoted lines elided]…
> else is wrong.

Flash! This just in! If 90%+ agree on a convention, that IS the de facto 
standard.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-06T08:17:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb1ru2pm5u2l9ughc44v7jtqbjmjsfplth@4ax.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com>`

```
On Mon, 5 Mar 2007 19:22:24 -0600, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>> Standard practice for Microsoft. Change (or ignore) what everyone else
>> does then claim that the Microsoft way _is_ the standard and everyone
…[3 more quoted lines elided]…
>standard. 

When businesses choose to accept a standard that excludes 10% of their
customers - they lose.    It is possible to create interfaces that
work with Microsoft & everybody else.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-06T11:24:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173209080.174684.121440@q40g2000cwq.googlegroups.com>`
- **In-Reply-To:** `<12upgigd0cjkqab@news.supernews.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com>`

```
On Mar 6, 2:22 pm, "HeyBub" <heybubNOS...@gmail.com> wrote:
> Richard wrote:
> > On Mar 6, 4:51 am, "Roger While" <s...@sim-basis.de> wrote:
…[11 more quoted lines elided]…
> standard.

Nobody 'agreed' to it, it was shoved down their throat by Microsoft
without a choice. Most are too stupid to know there is a difference.
Those that care have to hack workarounds.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-07T14:31:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<556j0iF23kl6uU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1173209080.174684.121440@q40g2000cwq.googlegroups.com...
> On Mar 6, 2:22 pm, "HeyBub" <heybubNOS...@gmail.com> wrote:
>> Richard wrote:
…[18 more quoted lines elided]…
>
Guess the answer is not to care... :-)

I agree with Howard that it is possible to have interfaces which work for 
everybody, but, I guess, this comes down to cost effectiveness.

If Howard is right and businesses that exclude 10% of their cuistomer base 
will suffer long term, then MicroSoft should be suffering about now...

The fact is that the people who are upset by this are not "MS friendly" 
anyway and so there is no incentive for MS to try and be more embracing.

Not being axperienced with Linux or Unix I confess to not understanding what 
Roger's problem is or why he has to "hack a workaround".  In a Windows 
environment, locales seem to be handled pretty well (my experience extends 
as far as Control Panel... :-))and the whole world is running Windows in 
their native languages...

Is this really such a big deal?

Pete.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-06T19:39:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com>`
- **In-Reply-To:** `<556j0iF23kl6uU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net>`

```
Pete Dashwood wrote:
[snip]
> 
> Is this really such a big deal?

Well, if you provide a compiler a locale, and then use LOCALE-DATE, 
you'd expect the same thing to come back no matter where your program is 
executing.  That it doesn't is causing Mr. While some extra work.  Not 
something that can't be overcome, but I can understand his frustration...
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-07T17:17:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<556sm4F23aj2oU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com...
> Pete Dashwood wrote:
> [snip]
…[8 more quoted lines elided]…
>
Ah, I see. Thanks for the clarification.

Wouldn't it be up to the compiler supplier to ensure it worked consistently 
on the platforms they have stated their compiler supports?

Pete
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-06T21:47:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com>`
- **In-Reply-To:** `<556sm4F23aj2oU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com...
…[12 more quoted lines elided]…
> on the platforms they have stated their compiler supports?

I can see both sides on this particular issue...  If the function is 
supposed to get the locale information that's built into the OS, then 
they would probably get grief from one camp or the other for tweaking 
it.  If it's supposed to be the same, then they'd have to provide their 
own locale look-up and format - then, every time someone worldwide 
changed something, they'd have to update their library and get it 
deployed to all their customers.

My opinion - I'd rather rely on facilities inherent in the OS.  Take the 
upcoming DST change, for example.  If you had your own routine, you'd be 
having to crank out some serious code.  (Well, that should already be 
done at this point, as the change happens in 5 days!)  If you rely on 
the OS, then it will more than likely be updated - and, if not, at least 
you're consistent with the other apps on the system.

I'm not sure how tough it would be in Roger's case to convert the pieces 
to ensure consistency - probably an unstring/re-string would do it. 
But, if you're trying to make routines that work consistently across 
locales, even that would be a challenge.  Do you split on "-", "/", " ", 
or something else?

And, while this may seem trivial to some (and I'm *not* implying that 
you see it that way), I do see his point that he shouldn't have to jump 
through those hoops.  Making a program locale-aware is a good thing, 
IMO.  :)
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-07T23:48:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<557jk4F22pmuaU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[22 more quoted lines elided]…
> customers.

OK...
>
> My opinion - I'd rather rely on facilities inherent in the OS.  Take the 
…[5 more quoted lines elided]…
>

Yes, very good point.

> I'm not sure how tough it would be in Roger's case to convert the pieces 
> to ensure consistency - probably an unstring/re-string would do it. But, 
…[7 more quoted lines elided]…
> :)

I don't see it as trivial (I don't think anything that causes programmers 
grief is trivial), but, due to my lack of understanding,  just couldn't see 
whether it is a major problem or not.

I am now much better informed :-)

Thanks.

Pete.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-07T07:47:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com>`

```
On Tue, 06 Mar 2007 21:47:54 -0700, LX-i <lxi0007@netscape.net> wrote:

>My opinion - I'd rather rely on facilities inherent in the OS.  Take the 
>upcoming DST change, for example.  If you had your own routine, you'd be 
…[3 more quoted lines elided]…
>you're consistent with the other apps on the system.

I just bought a clock radio this January.  It has buttons to press to
indicate my time zone and whether or not I'm under daylight savings
time.    I suspect it will fail to spring ahead this weekend, but will
do so a couple of weeks late.   But the company should have been
warned when the feds have futzed with daylight savings time in the
past.

Why can't we set up clock radios to synchronize with the radio station
of our choice?
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-07T16:41:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esmpv4$ar2$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com>`

```
In article <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>Why can't we set up clock radios to synchronize with the radio station
>of our choice?

You can buy clock-radios that synchronise with the NIST atomic clock that 
drives WWV... you just need to pay for them.

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 14)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-07T10:08:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173290902.078364.121120@64g2000cwx.googlegroups.com>`
- **In-Reply-To:** `<esmpv4$ar2$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com> <esmpv4$ar2$1@reader2.panix.com>`

```
On Mar 8, 5:41 am, docdw...@panix.com () wrote:
> In article <8tjtu2pgpqsbn8h443mi65j5nabilur...@4ax.com>,
> Howard Brazee  <how...@brazee.net> wrote:
…[7 more quoted lines elided]…
> drives WWV... you just need to pay for them.

.. and move to a place where the time is broadcast that way.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-07T15:03:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12uu6m39m390054@corp.supernews.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com> <esmpv4$ar2$1@reader2.panix.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1173290902.078364.121120@64g2000cwx.googlegroups.com...
> On Mar 8, 5:41 am, docdw...@panix.com () wrote:
> > In article <8tjtu2pgpqsbn8h443mi65j5nabilur...@4ax.com>,
…[7 more quoted lines elided]…
> > You can buy clock-radios that synchronise with the NIST atomic clock
that
> > drives WWV... you just need to pay for them.
>
> .. and move to a place where the time is broadcast that way.

Since "you" seems to refer to Mr Brazee, he would not
need to move at all. The WWV broadcast facility is
located at Fort Collins, Colorado, within 100 miles of
where he lives.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-07T14:29:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<049uu2pq720qfj9mk8tp0u2jc5ksj02kvn@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com> <esmpv4$ar2$1@reader2.panix.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <12uu6m39m390054@corp.supernews.com>`

```
On Wed, 7 Mar 2007 15:03:04 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>> > You can buy clock-radios that synchronise with the NIST atomic clock
>that
…[7 more quoted lines elided]…
>where he lives.

When I moved here, I bought a shareware that synchronized my computer
with the National Atmospheric Center here in Boulder.   That's no
longer needed, but I just installed an add-on to my Firefox, showing
the NCAR temperature - in Boulder.   

But consider a car radio that has a button on it - you press that
button and it synchronizes its time to whatever station it is tuned
to.   Or a travel alarm that checks the time with the radio station
that it is tuned to before turning on in the morning.

Of course when you pay hundreds of dollars for a car radio that loses
its settings when you replace your car battery - I wonder if anybody
in that industry thinks about consumers.

My phone and computer set themselves.   Now I have a clock in my iPod
that could be easy to forget.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-07T22:16:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esndkg$ku9$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <12uu6m39m390054@corp.supernews.com> <049uu2pq720qfj9mk8tp0u2jc5ksj02kvn@4ax.com>`

```
In article <049uu2pq720qfj9mk8tp0u2jc5ksj02kvn@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>But consider a car radio that has a button on it - you press that
>button and it synchronizes its time to whatever station it is tuned
>to.   Or a travel alarm that checks the time with the radio station
>that it is tuned to before turning on in the morning.

Consider a market survey that would assist in determining if such a device 
would generate a profit... and that's what Business is all about.

>
>Of course when you pay hundreds of dollars for a car radio that loses
>its settings when you replace your car battery - I wonder if anybody
>in that industry thinks about consumers.

Of *course* they do... it's a Free Market, where everyone is constantly 
innovating so that they will gain a competetive advantage over others.  
Don't you think that one of the Bright Boys of Blaupunkt has already gone 
through this and realised that the Public Just Doesn't Want It, in the 
same way that anonymous 'focus groups' tell tissue companies that 
consumers want rolls with fewer sheets, thinner paper and higher prices?

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-07T22:11:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esndao$e92$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com> <esmpv4$ar2$1@reader2.panix.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com>`

```
In article <1173290902.078364.121120@64g2000cwx.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>On Mar 8, 5:41 am, docdw...@panix.com () wrote:
>> In article <8tjtu2pgpqsbn8h443mi65j5nabilur...@4ax.com>,
…[10 more quoted lines elided]…
>.. and move to a place where the time is broadcast that way.

I believe that place is called 'earth', Mr Plinston.  While WWV, 
specifically, is located in Fort Collins, Colorado, USA its signal has 
been received in a variety of places.  Are the Antipodes beyond its - or a 
similar station's - broadcast radius?

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 16)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-07T16:51:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173315060.361919.72910@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<esndao$e92$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com> <esmpv4$ar2$1@reader2.panix.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com>`

```
On Mar 8, 11:11 am, docdw...@panix.com () wrote:
> In article <1173290902.078364.121...@64g2000cwx.googlegroups.com>,
>
…[15 more quoted lines elided]…
> I believe that place is called 'earth', Mr Plinston.

I have noticed a tendancy for USAmericans to equate USA == Earth.

> While WWV,
> specifically, is located in Fort Collins, Colorado, USA its signal has
> been received in a variety of places.

"""The WWVB broadcasts are used by millions of people throughout North
America to synchronize ... """

> Are the Antipodes beyond its - or a
> similar station's - broadcast radius?

There is a page of coverage maps at http://tf.nist.gov/timefreq/stations/wwvbcoverage.htm


>From http://tufi.alphalink.com.au/time/time_hf.html :

"""Since the closure of VNG on 31 December 2002, the SW time signals
available in the South Pacific have to travel from Hawaii, mainland
USA, Canada or China.  The received signal strength in New Zealand and
Australia is lower and more variable than that from VNG, making
reliable reception more difficult. """

While radio time signals were suitable in the 1920s through to the 70s
it is more reliable to get the time using the internet. Most also have
mechanisms to correct for propagation delays making them more
accurate.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-08T02:02:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esnqsj$juf$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com>`

```
In article <1173315060.361919.72910@s48g2000cws.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>On Mar 8, 11:11 am, docdw...@panix.com () wrote:
>> In article <1173290902.078364.121...@64g2000cwx.googlegroups.com>,
…[18 more quoted lines elided]…
>I have noticed a tendancy for USAmericans to equate USA == Earth.

I have noticed a variety of tendencies among a variety of folks, Mr 
Plinston... but I try to judge individuals as individuals first and not 
according to stereotypes, unlike certain intellectually lazy folks I've 
met.

>
>> While WWV,
…[19 more quoted lines elided]…
>reliable reception more difficult. """

So the answer would seem to be 'yes, the received signal strength, while 
lower and more variable, are in the Antipodes' broadcast reception 
radius.'

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 18)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-07T18:46:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173321972.353124.166850@p10g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<esnqsj$juf$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com>`

```
On Mar 8, 3:02 pm, docdw...@panix.com () wrote:
> In article

> >> Are the Antipodes beyond its - or a
> >> similar station's - broadcast radius?

> So the answer would seem to be 'yes,

You seem to have the right answer, but to the wrong question.

According the the coverage maps, yes, we are beyond the broadcast
radius. According to other information provided there is no longer a
similar station.

> the received signal strength, while
> lower and more variable, are in the Antipodes' broadcast reception
> radius.'

If you had read the article you may have noticed that it may be
somewhat usable for radio enthusiasts with specialised aerials but ,
in fact, it is nowhere near the signal strength required for 'clock-
radios' and the like.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 19)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-08T07:26:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v03nvlm858gaf@news.supernews.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com>`

```
Richard wrote:
>> the received signal strength, while
>> lower and more variable, are in the Antipodes' broadcast reception
…[5 more quoted lines elided]…
> radios' and the like.

Maybe NZ government could set up a "mirror" clock?

While some US cars have atomic-clock-synchronized timepieces, vehicles in 
other places have calendars.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 20)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-08T09:02:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173373344.740685.134240@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<12v03nvlm858gaf@news.supernews.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <12v03nvlm858gaf@news.supernews.com>`

```
On Mar 9, 2:26 am, "HeyBub" <heybubNOS...@gmail.com> wrote:
> Richard wrote:
> >> the received signal strength, while
…[11 more quoted lines elided]…
> other places have calendars.

Who cares ? Sunup, morning, middleofday, afternnon, sundown is good
enough around here.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 21)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-03-08T15:09:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12v0uss6ehb1h21@news.supernews.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173290902.078364.121120@64g2000cwx.googlegroups.com> <esndao$e92$1@reader2.panix.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <12v03nvlm858gaf@news.supernews.com> <1173373344.740685.134240@h3g2000cwc.googlegroups.com>`

```
Richard wrote:
>> Maybe NZ government could set up a "mirror" clock?
>>
…[4 more quoted lines elided]…
> enough around here.

Sex on such a rigid schedule! Must be the hemisphere.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-08T17:15:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<espgbp$qu9$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com>`

```
In article <1173321972.353124.166850@p10g2000cwp.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>On Mar 8, 3:02 pm, docdw...@panix.com () wrote:
>> In article
…[6 more quoted lines elided]…
>You seem to have the right answer, but to the wrong question.

That might be the appearance to a sloppy researcher prone towards bad 
editing and midsentence interruptions, Mr Plinston.

>
>According the the coverage maps, yes, we are beyond the broadcast
>radius. According to other information provided there is no longer a
>similar station.

According to other information provided elsewhere - someplace that someone 
interested in an actual Answer, rather than a bit of post-Empiric 
whingeing, might have looked, coverage, frequencies and times are posted:

From http://tufi.alphalink.com.au/time/time_hf.html :

--begin quoted text:

There is an excellent up-to-date Time Signal Stations Frequency List by 
Klaus Betke. [note - dead link]  Also refer to David Mills' excellent site 
Information on Time and Frequency Services.  [note - dead link].

WWVH (Hawaii) and WWV (Colorado)
WWVH and WWV broadcast on the international time standard frequencies of   
2.5,  5,  10,  15  and 20 (WWV only) MHz.  In New Zealand and Australia 5 
and 10 are the best at night, 10 and 15 (on rare occasions also 20 MHz) in 
the daytime and early evening.  Mostly, WWVH is received at the best 
signal strength, with WWV faintly in the background, but at times WWV is 
almost as good.

(Currently, in 2002 - 2002, there is a severe interference problem in 
Western Australia with many Indonesian fishing vessels using 10 MHz as 
their communication channel, ignoring international regulations.  This 
"chatter" is noticeable as far as South Eastern Australia, but WWVH is 
mostly still "usable" there.)

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-09T09:42:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55baphF24ancmU1@mid.individual.net>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:espgbp$qu9$1@reader2.panix.com...
> In article <1173321972.353124.166850@p10g2000cwp.googlegroups.com>,
> Richard <riplin@Azonic.co.nz> wrote:
…[13 more quoted lines elided]…
>

I use the internet to find out what the time is, so I have no intention of 
entering the debate around this.

I would note in passing that from a purely rhetorical perspective, citing a 
5 year old source that is nowhere near where we live, probably doesn't help 
to support any argument being made.

The distance from here to Western Australia (after doing a quick check with 
Google Earth) is about the same as from New York to Casablanca.

Hardly what you might call "in the neigbourhood"...

Pete.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 21)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-08T15:59:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173398376.829921.56830@64g2000cwx.googlegroups.com>`
- **In-Reply-To:** `<55baphF24ancmU1@mid.individual.net>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173315060.361919.72910@s48g2000cws.googlegroups.com> <esnqsj$juf$1@reader2.panix.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net>`

```
On Mar 9, 9:42 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <docdw...@panix.com> wrote in messagenews:espgbp$qu9$1@reader2.panix.com...
> > In article <1173321972.353124.166...@p10g2000cwp.googlegroups.com>,
…[24 more quoted lines elided]…
> Hardly what you might call "in the neigbourhood"...

One time when I was dealing with Microfocus they suggested I deal with
their agent in Melbourne.  I pointed out that was the same distance
from me as Moscow is from Reading.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 21)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-09T00:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esqb5s$frg$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net>`

```
In article <55baphF24ancmU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:espgbp$qu9$1@reader2.panix.com...
…[20 more quoted lines elided]…
>to support any argument being made.

Mr Dashwood, the source says 'it can be found here'... perhaps someone in 
those environs who is interested in verification might take action.

>
>The distance from here to Western Australia (after doing a quick check with 
>Google Earth) is about the same as from New York to Casablanca.

... and in Casablanca, Mr Dashwood, one can receive, at night, AM radio 
signals from 50,000 watt stations in New York.

>
>Hardly what you might call "in the neigbourhood"...

That might depend, Mr Dashwood, on what one has seen demonstrated of the 
propogation of radio-waves... have you ever heard tales of a lad sitting 
up, late at night, fiddling about with a home-made crystal radio set, 
tuned with a 'cat's whisker', pulling in signals from thousands of miles 
away... out of the aether, fuzz and buzz... and then something sounding 
like a rhythmic mud-fight in a paper bag, must be music... and then a 
voice, usually a clear, ringing baritone, announcing the call-letters of a 
station in a far-off city...

... sorry, got carried back a bit there.

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 22)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-08T17:29:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173403782.935157.249600@64g2000cwx.googlegroups.com>`
- **In-Reply-To:** `<esqb5s$frg$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com>`

```
On Mar 9, 1:53 pm, docdw...@panix.com () wrote:
> In article <55baphF24anc...@mid.individual.net>,
>
…[47 more quoted lines elided]…
> station in a far-off city...

You've almost convinced me that is how I should get my clock-radio to
have the exact time down to the nearest nanosecond, or at least to
within whatever the propagation delay might be tonight.

Nope, I'll stick with the cat patting me in the face around 6am
because the neighbour's cat has been in an eaten all his food.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-09T21:50:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55cleqF24h842U1@mid.individual.net>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <1173403782.935157.249600@64g2000cwx.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1173403782.935157.249600@64g2000cwx.googlegroups.com...
> On Mar 9, 1:53 pm, docdw...@panix.com () wrote:
>> In article <55baphF24anc...@mid.individual.net>,
…[62 more quoted lines elided]…
>

Yep, you can't stroke an alarm clock :-)

The alarm cat is an infinitely superior solution...with many other fringe 
benefits... like purring you to sleep when you can't... :-)

Pete.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 23)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-09T08:34:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kcv2v2hn10kcrn55n18r9spvsagbaerfhv@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <1173403782.935157.249600@64g2000cwx.googlegroups.com>`

```
On 8 Mar 2007 17:29:43 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>You've almost convinced me that is how I should get my clock-radio to
>have the exact time down to the nearest nanosecond, or at least to
…[3 more quoted lines elided]…
>because the neighbour's cat has been in an eaten all his food.

People use clock-radios because they want to wake up at a particular
time.   They don't want the clock-radio springing ahead at the old
daylight savings time date.

But more useful is the car radio that contains a clock in a vehicle
that crosses time zones.   They should have the ability to tune to a
local station, you press a button and your clock is on local time.

Cell phones adjust.  Computers adjust.   (Although Outlook tries to
out-guess you whether your appointment will be a teleconference or a
face-to-face conference while setting up your calendar).
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 24)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-09T18:24:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ess57o$mr3$00$1@news.t-online.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <1173403782.935157.249600@64g2000cwx.googlegroups.com> <kcv2v2hn10kcrn55n18r9spvsagbaerfhv@4ax.com>`

```
What was the original Q ?
:-)
Thanks Bill, :-)
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 24)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-03-09T11:12:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1173467559.754304.204120@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<kcv2v2hn10kcrn55n18r9spvsagbaerfhv@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <1173403782.935157.249600@64g2000cwx.googlegroups.com> <kcv2v2hn10kcrn55n18r9spvsagbaerfhv@4ax.com>`

```
On Mar 10, 4:34 am, Howard Brazee <how...@brazee.net> wrote:

> People use clock-radios because they want to wake up at a particular
> time.   They don't want the clock-radio springing ahead at the old
> daylight savings time date.

I suspect that in the states you will have considerable problems due
to your government shifting the goalposts..

> But more useful is the car radio that contains a clock in a vehicle
> that crosses time zones.   They should have the ability to tune to a
> local station, you press a button and your clock is on local time.

If you were to attempt to drive across a timezone in a car from here
then knowing the time will be the least of your problems.

I always found that when flying somewhere it was best to set the
destination time when boarding the plane and stick to that regardless
of what the airline staff wanted to do.  But then most of my
travelling has been a 12 hour timeshift on a 26 to 30 hour travelling
time.

Once I lost a complete day, but it was a Friday the 13th so no loss.
We crossed the dateline at 11:45 pm on thursday and, due to daylight
saving still being in force went to 12:45am saturday.

> Cell phones adjust.  Computers adjust.   (Although Outlook tries to
> out-guess you whether your appointment will be a teleconference or a
> face-to-face conference while setting up your calendar).

I have heard bad things about outlook, yes.  One of the reasons that I
dislike microsoft products is that I want things done _my_ way and not
have them changed randomly to what some ms programmer thinks they
should be.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 25)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-03-09T12:30:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iad3v21nfgj7159g7f7r7c2j0oavii77i4@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <1173403782.935157.249600@64g2000cwx.googlegroups.com> <kcv2v2hn10kcrn55n18r9spvsagbaerfhv@4ax.com> <1173467559.754304.204120@s48g2000cws.googlegroups.com>`

```
On 9 Mar 2007 11:12:39 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>I have heard bad things about outlook, yes.  One of the reasons that I
>dislike microsoft products is that I want things done _my_ way and not
>have them changed randomly to what some ms programmer thinks they
>should be.

My son-in-law was an hour late to a meeting with his boss in Seattle -
arriving when Outlook told him in Denver the meeting was.

But Apple tends to be even more "do things my way".
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-09T21:20:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55cjn8F24rk0iU1@mid.individual.net>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esqb5s$frg$1@reader2.panix.com...
> In article <55baphF24ancmU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[53 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-09T21:46:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55cl75F24beigU1@mid.individual.net>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <1173321972.353124.166850@p10g2000cwp.googlegroups.com> <espgbp$qu9$1@reader2.panix.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:esqb5s$frg$1@reader2.panix.com...
> In article <55baphF24ancmU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[36 more quoted lines elided]…
> signals from 50,000 watt stations in New York.

Possibly... but I thnk the point is they have trouble receiving them in 
Western Australia...:-)

 I was using a realistic analogy (that might be readily perceivable by one 
domiciled in New York)  to try and demonstrate that Western Australia is a 
very long way from New Zealand, so there is really no basis for concluding 
that radio reception there will be the same as in Aotearoa. It really has 
nothing to do with radio reception in Casablanca, where I'm quite sure they 
enjoy American programming along with other content.

>
>>
…[10 more quoted lines elided]…
>

Yes, and happy times they were too :-). When quite young, I too had a 
crystal set, and put the headphones on after lights out so I could search 
the ether... I remember soldering extra connection points into the coil for 
my crocodile clip, so I could instantly get my favourite local stations as 
well as shortwave... (Kids today don't know what they're missing with their 
iPods... :-) )

And yes, there were those rare and exciting occasions when  one would 
frantically scratch the crystal to try and get a better "spot" for the cat's 
whisker, because we were onto something really exotic :-)... sometimes it 
helped, sometimes it didn't but either way it made you feel like you were 
involved in something much bigger than the immediate backyard.

However, propagation of radio waves aside, it was never solid and consistent 
and you could go back the next night to the same spot and find nothing... 
Fact is, that propagation depends on many factors and some of them are 
wildly variable. Certainly the energy of the transmitter is a major factor, 
but even a high multi Megawatt transmitter can be stymied by ionic 
interference, sunspots, inversion layers and a host of other factors. (It 
was this very problem that was a major impetus towards establishing 
geo-stationary satellites...)


> ... sorry, got carried back a bit there.

Not at all :-)

Happy memories of a bygone time...

Pete.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 23)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-03-09T17:27:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ess5eo$4ah$1@reader2.panix.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <55baphF24ancmU1@mid.individual.net> <esqb5s$frg$1@reader2.panix.com> <55cl75F24beigU1@mid.individual.net>`

```
In article <55cl75F24beigU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:esqb5s$frg$1@reader2.panix.com...
…[40 more quoted lines elided]…
>Western Australia...:-)

Pardon my attempt to generate an a fortiriori argument, Mr Dashwood... 
sometimes they take a bit of work to unravel, or so I've seen.

>
> I was using a realistic analogy (that might be readily perceivable by one 
>domiciled in New York)  to try and demonstrate that Western Australia is a 
>very long way from New Zealand, so there is really no basis for concluding 
>that radio reception there will be the same as in Aotearoa.

Mr Dashwood, once again... the assertion's been made and there are 
sufficient data given to attempt to verify.  To ignore this in the face of 
analogies, realistic or not, might not assist in arriving at a 
reproducible phenomenon as actually Doing The Work might.

[snip]

>And yes, there were those rare and exciting occasions when  one would 
>frantically scratch the crystal to try and get a better "spot" for the cat's 
>whisker, because we were onto something really exotic :-)... sometimes it 
>helped, sometimes it didn't but either way it made you feel like you were 
>involved in something much bigger than the immediate backyard.

Perhaps what's been given here, Mr Dashwood, might allow someone a chance 
for similar sensations.

>
>However, propagation of radio waves aside, it was never solid and consistent 
>and you could go back the next night to the same spot and find nothing... 
>Fact is, that propagation depends on many factors and some of them are 
>wildly variable.

If one knew the results ahead of time, Mr Dashwood, it might be more of a 
reproduction and less of an experiment.

DD
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-07T17:49:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hL2dnbSL9cNbwHLYnZ2dnUVZ_vHinZ2d@comcast.com>`
- **In-Reply-To:** `<8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com>`
- **References:** `<esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net> <C7WdnU2lUY3R2XPYnZ2dnUVZ_sSmnZ2d@comcast.com> <8tjtu2pgpqsbn8h443mi65j5nabilur8q0@4ax.com>`

```
Howard Brazee wrote:
> 
> Why can't we set up clock radios to synchronize with the radio station
> of our choice?

You probably could, if they were coded that way.  :)  I think I've seen 
some that are supposed to synchronize somehow, but I don't know how it 
works (phone, internet, etc...)
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-07T06:28:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lYsHh.199683$ff2.84678@fe02.news.easynews.com>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net>`

```
But Pete,
   Roger *IS* the compiler supplier (he is doing much of the work on "Open 
COBOL" - which is why he is asking HOW to implement this '02 Standard feature.
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-07T23:44:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<557jd1F232jagU1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net> <lYsHh.199683$ff2.84678@fe02.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:lYsHh.199683$ff2.84678@fe02.news.easynews.com...
> But Pete,
>   Roger *IS* the compiler supplier (he is doing much of the work on "Open 
> COBOL" - which is why he is asking HOW to implement this '02 Standard 
> feature.
>

Yes, of course... slipped my memory. Sorry Roger.

Pete
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 11)_

- **From:** Donald Tees <donald_tees@donald-tees.ca>
- **Date:** 2007-03-07T09:11:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esmh5t$ofs$1@aioe.org>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com...
…[16 more quoted lines elided]…
> 

If the OS changes in unpredictable ways, how does a compiler supplier 
conform?

I just had to change ISP's (and my entire mail setup) because my ISP 
went to something that denies mail access to non-MSN systems. The techy 
at the ISP told me he was unable to help with Email unless he could 
install and use a rootkit on my XP computer, and no other OS could be 
used. I told him to fuck himself, and got a new ISP.

Donald
```

###### ↳ ↳ ↳ Re: FUNCTION's LOCALE-(DATE/TIME)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-03-08T09:32:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<558lrcF22p6c5U1@mid.individual.net>`
- **References:** `<esgn79$uik$02$1@news.t-online.com> <WISGh.90460$lb3.32244@fe08.news.easynews.com> <esgunf$dv8$03$1@news.t-online.com> <htKdnR5FA7QzunHYnZ2dnUVZ_qTinZ2d@comcast.com> <eshe9s$q50$01$1@news.t-online.com> <1173115927.324096.235450@c51g2000cwc.googlegroups.com> <12upgigd0cjkqab@news.supernews.com> <1173209080.174684.121440@q40g2000cwq.googlegroups.com> <556j0iF23kl6uU1@mid.individual.net> <k_GdnSxVef-nu3PYnZ2dnUVZ_qzinZ2d@comcast.com> <556sm4F23aj2oU1@mid.individual.net> <esmh5t$ofs$1@aioe.org>`

```

"Donald Tees" <donald_tees@donald-tees.ca> wrote in message 
news:esmh5t$ofs$1@aioe.org...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[30 more quoted lines elided]…
>
Good for you. I would've done the same.

To answer your question... (And I stress this is a personal opinion...)

1. If I provide an application which I claim runs under a certain OS, and 
then that OS changes so that my application is compromised, I would make a 
fix available from a downloadable source, and notify everyone using the 
application.

(Application calls to OS dependent facilities should be layered through an 
API. If the OS Changes, the API protects the application from needing 
amendment. If the API changes, then the OS vendor has to provide details of 
the new API and application developers can update their applications.)

2. I would expect a compiler vendor to do exactly that. I should be able to 
download a patch and apply it to my compiler.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
