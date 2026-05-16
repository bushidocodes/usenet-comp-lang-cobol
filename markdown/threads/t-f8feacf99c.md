[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Time from 24 hr to US

_11 messages · 6 participants · 2000-12_

---

### Re: Time from 24 hr to US

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 2000-12-08T13:17:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a30e139$0$78095$a05e1490@news.netdirect.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com>`

```
In article <90nah7$3944$1@newssvr06-en0.news.prodigy.com>, "Terry Heinze" <terryheinze@prodigy.net> wrote:
>If you're asking how to convert 24 hour time to AM/PM time, let's say you
>start out with HH:MM in 24 hour time.  If HH < 12, it's AM, otherwise, it's
>PM.  In addition, if HH > 12, subtract 12 from it.
>
Sorry, that is not correct.

0000 = 12:00 PM (midnight)
0001 = 12:01 AM
..
1159 = 11:59 AM
1200 = 12:00 AM (noon)
1201 = 12:01 PM
..
2359 = 11:59 PM
```

#### ↳ Re: Time from 24 hr to US

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-12-08T21:47:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XFcY5.4294$wo2.79622@typhoon.austin.rr.com>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net>`

```

Doug Miller <dxmixxer@netdirect.net> wrote in message
news:3a30e139$0$78095$a05e1490@news.netdirect.net...
> In article <90nah7$3944$1@newssvr06-en0.news.prodigy.com>, "Terry Heinze"
<terryheinze@prodigy.net> wrote:
> >If you're asking how to convert 24 hour time to AM/PM time, let's say you
> >start out with HH:MM in 24 hour time.  If HH < 12, it's AM, otherwise,
it's
> >PM.  In addition, if HH > 12, subtract 12 from it.
> >
…[9 more quoted lines elided]…
> 2359 = 11:59 PM

just to show how hard (and silly) this is. I think that 12:00 PM is noon
(at least that's what I just saw on CNN - some ruling to come at 12PM)
and that 12:00 AM is midnight.
or maybe people don't really know and the "dictionary" rules are
not always being followed.
```

#### ↳ Re: Time from 24 hr to US

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-12-08T23:50:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net>`

```

"Doug Miller" <dxmixxer@netdirect.net
>
> 0000 = 12:00 PM (midnight)
…[7 more quoted lines elided]…
>

Mygawdalmighty no!

1200 hours is NOT 12:00 AM (ante meridian - before noon).

1200 hours is NOT 12:00 PM (post meridian - after noon).

1200 hours is 12:00 NOON.

On the other hand, 0000 hours is 12:00 AM or 12:00 PM - take your
pick.

While we're at it: it's 100 B.C. or A.D 1492 - NOT 1492 A.D.
```

##### ↳ ↳ Re: Time from 24 hr to US

- **From:** dlmiller@netdirect.net (Doug Miller)
- **Date:** 2000-12-09T16:12:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a325bc2$0$1510$7ea90a65@news.netdirect.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net>`

```
In article <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net>, "Jerry P" <jerryp@bisusa.com> wrote:
>
>"Doug Miller" <dxmixxer@netdirect.net
…[13 more quoted lines elided]…
>1200 hours is NOT 12:00 AM (ante meridian - before noon).
False.
>1200 hours is NOT 12:00 PM (post meridian - after noon).
True.
>1200 hours is 12:00 NOON.
Also true.
>
>On the other hand, 0000 hours is 12:00 AM or 12:00 PM - take your
>pick.
False. 0000 is 12:00 PM or 12:00 midnight, but not under any circumstances is 
it 12:00 AM -- that's noon.

Guess you weren't paying too much attention in grade school.
```

###### ↳ ↳ ↳ Re: Time from 24 hr to US

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-12-09T17:46:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eeuY5.5356$U4.554026@newsread1.prod.itd.earthlink.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net> <3a325bc2$0$1510$7ea90a65@news.netdirect.net>`

```

"Doug Miller" <dlmiller@netdirect.net

> >
> >On the other hand, 0000 hours is 12:00 AM or 12:00 PM - take your
> >pick.

> False. 0000 is 12:00 PM or 12:00 midnight, but not under any
circumstances is
> it 12:00 AM -- that's noon.
>
> Guess you weren't paying too much attention in grade school.

Actually, I was so smart I skipped grade school. Sorry about yours.

P.M. = post merdiem = after noon.
A.M. = ante merdiem = before noon.

0000 hours is, therefore, 12 hours 'post merdiem'- after noon or 12
hours 'ante merdiem' - before noon. Take your pick. But if you do
choose one over the other, half your readers will be confused. Better
to use "12:00 midnight".
```

###### ↳ ↳ ↳ Re: Time from 24 hr to US

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-12-09T15:45:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90u5kp$2clt$1@news.hitter.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net> <3a325bc2$0$1510$7ea90a65@news.netdirect.net>`

```

Doug Miller wrote in message
<3a325bc2$0$1510$7ea90a65@news.netdirect.net>...
>In article <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net>,
"Jerry P" <jerryp@bisusa.com> wrote:
[...]
>>On the other hand, 0000 hours is 12:00 AM or 12:00 PM - take your
>>pick.

>False. 0000 is 12:00 PM or 12:00 midnight, but not under any circumstances
is
>it 12:00 AM -- that's noon.
>
>Guess you weren't paying too much attention in grade school.

The following was copied from Microsoft Bookshelf 98. Please
read the Usage Note, below.
=========
an�te me�rid�i�em
an�te me�rid�i�em (�n�t� me-r�d��-em) adverb & adjective
Abbr. A.M., a.m., A.M.
Before noon. Used chiefly in the abbreviated form to specify
the hour: 10:30 A.M.; an A.M. appointment.

[Latin ante, before + meridiem, accusative of meridi�s, noon.]

Usage Note: Strictly speaking, 12 A.M. denotes midnight, and
12 P.M. denotes noon, but there is sufficient confusion over
these uses to make it advisable to use 12 noon and 12 midnight
where clarity is required.
-----------
Excerpted from The American Heritage(r) Dictionary of the
English Language, Third Edition  (c) 1996 by Houghton Mifflin
Company. Electronic version licensed from INSO Corporation;
further reproduction and distribution in accordance with the
Copyright Law of the United States. All rights reserved.
========
Apparently, neither the author of the usage note, nor I, attended
the same grade school as you or Jerry P.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Time from 24 hr to US

_(reply depth: 4)_

- **From:** dlmiller@netdirect.net (Doug Miller)
- **Date:** 2000-12-10T23:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a34127e$0$2548$7ea90a65@news.netdirect.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net> <3a325bc2$0$1510$7ea90a65@news.netdirect.net> <90u5kp$2clt$1@news.hitter.net>`

```
In article <90u5kp$2clt$1@news.hitter.net>, "Rick Smith" <ricksmith@aiservices.com> wrote:
>
>Doug Miller wrote in message
…[14 more quoted lines elided]…
>read the Usage Note, below.

Considering the known egregious errors for which Microsoft's "reference" works 
have justifiably become the subject of much ridicule worldwide, anything they 
publish can hardly be regarded as authoritative.
```

###### ↳ ↳ ↳ Re: Time from 24 hr to US

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-12-10T22:20:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<911h23$4ue$1@news.hitter.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net> <3a325bc2$0$1510$7ea90a65@news.netdirect.net> <90u5kp$2clt$1@news.hitter.net> <3a34127e$0$2548$7ea90a65@news.netdirect.net>`

```
See < http://sciastro.astronomy.net/sci.astro.3.FAQ >. This is
Part 3 of Frequently Asked Questions of < news:sci.astro >.

An excerpt of that FAQ is shown below.

"Subject: C.02 What are all those different kinds of time?
Author: Paul Schlyter <pausch@saaf.se>,
Markus Kuhn <Markus.Kuhn@cl.cam.ac.uk>,
Paul Eggert <eggert@twinsun.com>

"...  (In strict English construction, 12:00 cannot be given
either an A.M. = ante meridiem or P.M. = post meridiem
designation, but it has become common to use  12 A.M
to mean midnight and 12 P.M. to mean noon.  In traditional
English, 12 M. = meridies means _noon_; nowadays one
is just as likely to see 12 M. = midnight and 12 N. = noon.)"
------------------
Rick Smith

Doug Miller wrote in message
<3a34127e$0$2548$7ea90a65@news.netdirect.net>...
>In article <90u5kp$2clt$1@news.hitter.net>, "Rick Smith"
<ricksmith@aiservices.com> wrote:
>>
>>Doug Miller wrote in message
…[7 more quoted lines elided]…
>>>False. 0000 is 12:00 PM or 12:00 midnight, but not under any
circumstances
>>is
>>>it 12:00 AM -- that's noon.
…[6 more quoted lines elided]…
>Considering the known egregious errors for which Microsoft's "reference"
works
>have justifiably become the subject of much ridicule worldwide, anything
they
>publish can hardly be regarded as authoritative.
```

###### ↳ ↳ ↳ Re: Time from 24 hr to US

_(reply depth: 5)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-12-12T04:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B2iZ5.14139$U4.1318106@newsread1.prod.itd.earthlink.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net> <3a325bc2$0$1510$7ea90a65@news.netdirect.net> <90u5kp$2clt$1@news.hitter.net> <3a34127e$0$2548$7ea90a65@news.netdirect.net>`

```

"Doug Miller" <dlmiller@netdirect.net>
>
> Considering the known egregious errors for which Microsoft's
"reference" works
> have justifiably become the subject of much ridicule worldwide,
anything they
> publish can hardly be regarded as authoritative.

The world will come around to Microsoft's way. It's only a matter of
when.
```

##### ↳ ↳ Re: Time from 24 hr to US

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-11T07:58:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A34EB7C.EB14A3C8@brazee.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net> <fteY5.50424$II2.4538054@newsread2.prod.itd.earthlink.net>`

```
Jerry P wrote:

> Mygawdalmighty no!
>
…[7 more quoted lines elided]…
> pick.

12:00 MM (mid meridian) is the term I have read.  But why not skip the
latin and call it 12:00 midnight?


> While we're at it: it's 100 B.C. or A.D 1492 - NOT 1492 A.D.

Interesting that we mix languages here, or does B.C. have the same
initials in latin?
```

#### ↳ Re: Time from 24 hr to US

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-11T07:53:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A34EA5E.77F8FB1@brazee.net>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com> <90nah7$3944$1@newssvr06-en0.news.prodigy.com> <3a30e139$0$78095$a05e1490@news.netdirect.net>`

```
Doug Miller wrote:

> Sorry, that is not correct.
>
…[7 more quoted lines elided]…
> 2359 = 11:59 PM

So how do you decide that 12:00 ante meridian (before noon) is noon, and 12:00 Post Meridian (after noon) is
midnight?

If I had to set an alarm for noon, I will set it for 11:59 instead to make sure my assumptions and the clock's
assumptions agree.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
