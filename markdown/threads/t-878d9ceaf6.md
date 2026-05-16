[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 6.1 and XP Pro

_25 messages · 9 participants · 2003-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu 6.1 and XP Pro

- **From:** "Theo Charalambous" <westleylodge@optusnet.com.au>
- **Date:** 2003-04-08T20:06:48+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```
Hi there

Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze up on
me. As a result I had to reformat the hard drive. I had backups of all of my
software. However when it came to re-installing Fujitsu V6.1 it meant that I
had to get an activation key again from Fujitsu.

I emailed the necessary details to Fujitsu, and to my surprise I received an
email back saying that V6.1 will not work in Win XP, and that I HAD TO
UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.

Firstly, I checked the Fujitsu site to see if there were any issues about
V6.1 running on WIN  XP and found nothing about it.

Secondly I have been using it in "evaluation" mode for two weeks without a
glitch on XP, running all of my previous programs that I've developed (and
some new ones as well) without any issues. I must admit I only have one use
for it, and that is to develop simple maintenance COBOL programs to VSAM
files, which I compile into a DLL. I then use these DLLs as functions in my
VB programs to do the data access

Did anyone else EVER have any issues with V6.1 and XP?

Rgds

TC
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-08T11:23:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e929d3d$1_1@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```
Theo,

I can't believe you were given that advice.

I can confirm that V6.1 runs flawlesly under Windows XP Professional. I am
using both COBOL97 and PowerCOBOL every day, am writing components and CGI
and ISAPI code and have no problems whatsoever. In fact, it is a superb
product.

Somebody in Fujitsu Marketing may have got their wires crossed...

Pete.

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message
news:3e929f38$0$20113$afc38c87@news.optusnet.com.au...
> Hi there
>
> Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze up
on
> me. As a result I had to reformat the hard drive. I had backups of all of
my
> software. However when it came to re-installing Fujitsu V6.1 it meant that
I
> had to get an activation key again from Fujitsu.
>
> I emailed the necessary details to Fujitsu, and to my surprise I received
an
> email back saying that V6.1 will not work in Win XP, and that I HAD TO
> UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.
…[6 more quoted lines elided]…
> some new ones as well) without any issues. I must admit I only have one
use
> for it, and that is to develop simple maintenance COBOL programs to VSAM
> files, which I compile into a DLL. I then use these DLLs as functions in
my
> VB programs to do the data access
>
…[6 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-08T06:25:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<baCcnckMH_dfLA-jXTWJiw@giganews.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message
news:3e929f38$0$20113$afc38c87@news.optusnet.com.au...
> Hi there
>
> Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze up
on
> me. As a result I had to reformat the hard drive. I had backups of all of
my
> software. However when it came to re-installing Fujitsu V6.1 it meant that
I
> had to get an activation key again from Fujitsu.
>
> I emailed the necessary details to Fujitsu, and to my surprise I received
an
> email back saying that V6.1 will not work in Win XP, and that I HAD TO
> UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.

Well, 6.1 and XP work here.

Here's how you can trick the system:

1. Install 6.1 on a spare Win98 machine and get the unlock key for that
configuration.

2. Transfer the license to the XP machine.

Post the email asserting incompatibility 'twixt 6.1 and XP - we'd like to
see it.

On another matter, XP works ever so much better on a clean install (which
you ultimately did) than as an upgrade.
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-08T07:12:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304080612.1a1df0b@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```
Theo - there are sporadic problems with Fujitsu COBOL 6.1 under XP,
specifically installation issues and problems inside PowerCOBOL with
certain underlying ActiveX controls and COM servers used by Fujitsu
PowerCOBOL.  To work around some of these issues, Fujitsu released a
patched version 6.1a, which I think would work for you, but I would
not be suprised to find that they are only distributing version 7 at
this point.  This is akin to trying to get help from Microsoft for
Visual Basic 5.0 - they would tell you to upgrade to 6 or VB .NET.

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message news:<3e929f38$0$20113$afc38c87@news.optusnet.com.au>...
> Hi there
> 
…[23 more quoted lines elided]…
> TC
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-08T07:15:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304080615.6795992e@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```
Oh - A PS to my last message.  If your maintenance is current, you can
get version 7 for no additional charge.  If you are not on
maintenance, I think you are out of luck, as they won't (and SHOULD
NOT) give you support if you have not paid the fee.  So after thinking
about it, I don't see why their suggesting version 7 is at all out of
line.

1 - new customers will get v7 when they order.
2 - Existing customers can get v7

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message news:<3e929f38$0$20113$afc38c87@news.optusnet.com.au>...
> Hi there
> 
…[23 more quoted lines elided]…
> TC
```

##### ↳ ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** "Theo Charalambous" <westleylodge@optusnet.com.au>
- **Date:** 2003-04-09T10:34:37+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e936a9a$0$21006$afc38c87@news.optusnet.com.au>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <bfdfc3e8.0304080615.6795992e@posting.google.com>`

```
Thane

I wanted to point one thing out. I am not on the "hunt" for the product. I
merely wanted to know if V6.1 has had issues WXP like I was advised. I've
found from the group that this may be the case but NOT always.
However I believe that from the emails that I've received, there are a lot
of issues with the licensing scheme Fujitsu is using.

Two points to your response

Firstly
I agree with most of the things you say.  However I disagree that they
SHOULD NOT send me an activation key to make the package work correctly. I
would imagine that NOT everybody had a maintenance agreement when they
bought the package. So if this people ever had a crash on their computer,
would that meant that the thousands of dollars they paid for their software
has gone down the drain? I am sure that's not the case. I looked for my
product license to have a read about it, and clear this issue out, but I
couldn't find it.

In any case (for me) it doesn't matter any more. I will use V5.

Secondly
I just want to clear one thing: Despite of all the complaints and issues
with the licensing, the Fuji product is by far the best COBOL product out
there...

Rgds

TC


"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0304080615.6795992e@posting.google.com...
> Oh - A PS to my last message.  If your maintenance is current, you can
> get version 7 for no additional charge.  If you are not on
…[8 more quoted lines elided]…
> "Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message
news:<3e929f38$0$20113$afc38c87@news.optusnet.com.au>...
> > Hi there
> >
> > Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze
up on
> > me. As a result I had to reformat the hard drive. I had backups of all
of my
> > software. However when it came to re-installing Fujitsu V6.1 it meant
that I
> > had to get an activation key again from Fujitsu.
> >
> > I emailed the necessary details to Fujitsu, and to my surprise I
received an
> > email back saying that V6.1 will not work in Win XP, and that I HAD TO
> > UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.
> >
> > Firstly, I checked the Fujitsu site to see if there were any issues
about
> > V6.1 running on WIN  XP and found nothing about it.
> >
> > Secondly I have been using it in "evaluation" mode for two weeks without
a
> > glitch on XP, running all of my previous programs that I've developed
(and
> > some new ones as well) without any issues. I must admit I only have one
use
> > for it, and that is to develop simple maintenance COBOL programs to VSAM
> > files, which I compile into a DLL. I then use these DLLs as functions in
my
> > VB programs to do the data access
> >
…[4 more quoted lines elided]…
> > TC
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** "Teamcast" <Teamcast@temcast.com>
- **Date:** 2003-04-08T17:12:18+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jyCka.561$Sa3.821383@newsserver.ip.pt>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```

THE GREAT PROBLEM OF FUJITSU IS TO USE AN ARCHAIC SYSTEM OF LICENSING.

I ALREADY HAD SEVERAL PROBLEMS WITH THE SAME .

But it works well in XP

Tay



"Theo Charalambous" <westleylodge@optusnet.com.au> escreveu na mensagem
news:3e929f38$0$20113$afc38c87@news.optusnet.com.au...
> Hi there
>
> Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze up
on
> me. As a result I had to reformat the hard drive. I had backups of all of
my
> software. However when it came to re-installing Fujitsu V6.1 it meant that
I
> had to get an activation key again from Fujitsu.
>
> I emailed the necessary details to Fujitsu, and to my surprise I received
an
> email back saying that V6.1 will not work in Win XP, and that I HAD TO
> UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.
…[6 more quoted lines elided]…
> some new ones as well) without any issues. I must admit I only have one
use
> for it, and that is to develop simple maintenance COBOL programs to VSAM
> files, which I compile into a DLL. I then use these DLLs as functions in
my
> VB programs to do the data access
>
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Fujitsu 6.1 and XP Pro-Final

- **From:** "Theo Charalambous" <westleylodge@optusnet.com.au>
- **Date:** 2003-04-09T07:41:03+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9341ec$0$21006$afc38c87@news.optusnet.com.au>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```
All

Thanks for the responses. I have basically found what I was after. There may
or may not be any problems with V6.1 and WXP. In my situation in using the
real thing in "evaluation" mode gives me NO trouble.

In regards with the issue of Fujitsu not supplying me with an activation
key, it's stupid, but it's the fact. I did not renew my maintenance and as a
result I would imagine it means that I cannot EVER get the activation key
unless I buy V7. Right or wrong I don't know. What I do know is that V5
works just as fine, so I will go back to that.

Thanks for your responses

Rgds

TC

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message
news:3e929f38$0$20113$afc38c87@news.optusnet.com.au...
> Hi there
>
> Halfway through my WIN2000 upgrade to WIN XP Pro, the dumb think froze up
on
> me. As a result I had to reformat the hard drive. I had backups of all of
my
> software. However when it came to re-installing Fujitsu V6.1 it meant that
I
> had to get an activation key again from Fujitsu.
>
> I emailed the necessary details to Fujitsu, and to my surprise I received
an
> email back saying that V6.1 will not work in Win XP, and that I HAD TO
> UPGRADE to V7.  Now, I found this a bit odd for a couple of reasons.
…[6 more quoted lines elided]…
> some new ones as well) without any issues. I must admit I only have one
use
> for it, and that is to develop simple maintenance COBOL programs to VSAM
> files, which I compile into a DLL. I then use these DLLs as functions in
my
> VB programs to do the data access
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fujitsu 6.1 and XP Pro-Final

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-08T20:27:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304081927.63592404@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <3e9341ec$0$21006$afc38c87@news.optusnet.com.au>`

```
"Theo Charalambous" <westleylodge@optusnet.com.au> wrote

> Thanks for the responses. I have basically found what I was after. There may
> or may not be any problems with V6.1 and WXP. In my situation in using the
…[6 more quoted lines elided]…
> works just as fine, so I will go back to that.

I purchased Fujitsu 6.1 _without_ any annual maintenance, I would be
most upset if they didn't resupply an activation code if I had a
genuine loss of a hard drive by some means.  There is no relationship
between a licence to use the product, which is in perpetuity, and an
annual maintenance agreement which is for the supply of updates and
for support.

Given that without an activation code the product is inoperable then
this may constitute a breach of the licence to use on their part - you
should ask for your money back or for specific performance (ie supply
of key).
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro-Final

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T10:38:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93ea2f_1@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <3e9341ec$0$21006$afc38c87@news.optusnet.com.au> <217e491a.0304081927.63592404@posting.google.com>`

```
I agree 100% with your take on this, Richard.

I also believe that Fujitsu would, too.

It is fair and reasonable. It seems to me that the information has come from
an over-zealous Marketing department.

Pete.

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304081927.63592404@posting.google.com...
> "Theo Charalambous" <westleylodge@optusnet.com.au> wrote
>
> > Thanks for the responses. I have basically found what I was after. There
may
> > or may not be any problems with V6.1 and WXP. In my situation in using
the
> > real thing in "evaluation" mode gives me NO trouble.
> >
> > In regards with the issue of Fujitsu not supplying me with an activation
> > key, it's stupid, but it's the fact. I did not renew my maintenance and
as a
> > result I would imagine it means that I cannot EVER get the activation
key
> > unless I buy V7. Right or wrong I don't know. What I do know is that V5
> > works just as fine, so I will go back to that.
…[11 more quoted lines elided]…
> of key).




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-04-19T20:29:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2785441.1050784167@dbforums.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```

I have had a trouble when i was  upgrading OS from Win2k to WinXp
Professional...
Before to upgrade the operating system is needed to "transfer out" the
license, otherwise once WinXp is installed you will not be able to use
the product for some reasons, because WinXp changes some registry item
used by Caspar protection scheme and it can be dangerous.

For the rest, Fujitsu v6.1 run fine on WinXp Professional, without
any problem.

When v6.1 has been released, i have had THREE hard disk crashes and
Fujitsu Support team had given me a new activation key, saying only: The
next time you will require a new activation key, you have to purchase a
new product..I had an annual maintenance support...

Gianni

P.S. sorry for my english, i'm trying to improve it, but i need
     more time..:o)
```

##### ↳ ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-19T23:30:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304192230.10a615c4@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2785441.1050784167@dbforums.com>`

```
gmspano <member9303@dbforums.com> wrote 

> When v6.1 has been released, i have had THREE hard disk crashes and
> Fujitsu Support team had given me a new activation key, saying only: The
> next time you will require a new activation key, you have to purchase a
> new product..I had an annual maintenance support...

I consider that I have purchased a permanent 'right to use' the
product. The activation mechanism is part of Fujitsu's own protection
and is not part of my 'right to use'.

If they have an attitude that they may not provide another key when
required due to genuine loss, then I may suggest that a 'back up'* be
taken of the installation so that recovery can be done independantly
of obtaining a new activation.


* 'back up' should be considered only for fair use.  Description of
any mechanisms that may arrive at a usable back up, even when fair
use, may be illegal in some countries.
```

#### ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-04-20T18:20:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2786779.1050862827@dbforums.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au>`

```

Hello Richard

I totally agree with your opinions.

One of my first requests to Fujitsu was to provide some mechanism to
preserve the activation key for "backup" purpose only. Nothing to do!!

Caspar protection scheme is not more difficult to reproduce.
I know there are some programmers who are using the same license in two
or more machine applying a sort of "backup" mechanism.
I know how it can be done, but i don't agree with this method, because
all of us we are programmers and don't like to see our software
installed on different machine without sell our licenses...The same
thing is for Fujitsu.

I think Fujitsu must follow the way to fall down their  prices.
The most part of peoples in this forum are indipendent  developers and
sometime we have money troubles to purchase a good product, but we are
unable to do this for the reason exposed above.

In my personal opinion Fujitsu has a GREAT product (Netcobol for
Windows) and there aren't other companies who are offering a similar
product with the same performances..But, it needs to be improved adding
some other tools, like grids (not only table), calendars, planning and a
series of useful gadgets, that can help us to improve our development.
In pratice an ALL IN ONE product.

I don't know how is the situation in the USA or other world parts, but
here in Italy, there are more software houses or independent developers
who would like to use Fujitsu products for their software development.
The reason: the prices are still considered more high.

Gianni
```

##### ↳ ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** "euromercante" <euromercante@clix.pt>
- **Date:** 2003-04-21T16:46:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bqUoa.1365$Vr6.2215980@newsserver.ip.pt>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com>`

```
Hi,
We've already had problems
with the licenses when we want to install another OS or upgrade the Fujitsu
version.
When I made the update of the version 6 for 7 it was necessary to ask 5
licenses  to Fujitsu because I had  problems
of installation of Cobol .
 Now I'm using Fujitsu version 7, and if possible could you tell me how
this "backup mechanism" works, because I want to install XP Pro in my
computer and we don�t have the Fujitsu Support and I want to be independent
from Fujitsu in these situations.

Very thanks,



"gmspano" <member9303@dbforums.com> escreveu na mensagem
news:2786779.1050862827@dbforums.com...
>
> Hello Richard
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-21T14:07:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304211307.16b4a3f0@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt>`

```
"euromercante" <euromercante@clix.pt> wrote

> if possible could you tell me how
> this "backup mechanism" works,

No, I can't tell you anything like that, even if I knew, for legal
reasons in the US.

>  we want to install another OS or upgrade

However I _can_ tell you that Partition Manager is a wonderful tools
for many things including helping when, say, installing a new
operating system.  With it you can resize partitions, and for example
take a copy of your C: partition to another partition.  Then if the
installation of the new OS goes wrong you can recover your old C:
drive partition back to exactly as it was.

You should be careful about this because if you have installed, or
uninstalled, software, or moved it to another machine, between taking
a copy of the C: drive and restoring it then that change is lost.

I have found that sometimes the partition sizes don't match exactly on
a restore due to it taking the space available and it needs a little
fiddling to get the size spot on, but I don't have the latest version.
 It is also best if you have a smaller C: partition (say 2Gb) for
software and a larger (16Gb) D: for data and stuff, then a backup
partition only needs 2Gb.
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 4)_

- **From:** "Theo Charalambous" <westleylodge@optusnet.com.au>
- **Date:** 2003-04-25T08:12:49+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea86164$0$16258$afc38c87@news.optusnet.com.au>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com>`

```
I wonder if all this trouble is worth it...

I beleive that most of the people on this group (like me) develop in more
than one language...
Ever since I  had the trouble and reported it to the group, I reverted back
to V5. For what I want to use it for (data back end), I believe COBOL does a
great job. But for front end programming no matter how exciting it is to do
GUI devt with COBOL, it still seriously lacks behind tools like VB, Delphi
and many others...

Of late I am a privateer. This means I need to develop applications in the
shortest possible time, that are not very expensive, and use a tool that can
provide a TOTAL integration of all components (DEVT, FRONT END, BACK END,
INTERNET, INTRANET ETC). As much as I like coding in COBOL it's now a
sentimental issue.

For myself, I decided to use WINDEV, a French product. I've done some
researching in the last couple of weeks after someone from the group let me
now about it (see previous thread msg ), and I was so impressed I bought the
package. In fact I am programming the darn thing (actually it does most if
it), within 2 days of receiving it....

Vive La France...!


"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304211307.16b4a3f0@posting.google.com...
> "euromercante" <euromercante@clix.pt> wrote
>
…[24 more quoted lines elided]…
> partition only needs 2Gb.
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-25T11:57:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b89tod$rdn$1@aklobs.kc.net.nz>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au>`

```
Theo Charalambous wrote:

> I believe COBOL
> does a great job. But for front end programming no matter how exciting it
> is to do GUI devt with COBOL, it still seriously lacks behind tools like
> VB, Delphi and many others...

Fujitsu has PowerCobol for Windows.

Flexus SP/2 runs with many varieties of Cobol on several operating systems 
and includes a Thin Client system for remote clients.

Many others also exist.
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 6)_

- **From:** "Theo Charalambous" <westleylodge@optusnet.com.au>
- **Date:** 2003-04-25T10:41:24+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea88436$0$16257$afc38c87@news.optusnet.com.au>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <b89tod$rdn$1@aklobs.kc.net.nz>`

```
I know about that. I've been using Fujitsu for a number of years... However
it is very VERY trivial in what it can do. If you are performing serious
devt, the more you use it, the more its weakness and inability to perform
certain things get in the way

... comparing it with something like (say) VB or WINDEV... well really there
is no comparison...

Fujitsu is a good COBOL package. Better than any other ones I used... but
still limited inits GUI functionality... I haven't used COBOL for .NET.
Maybe that's better.. time will tell

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b89tod$rdn$1@aklobs.kc.net.nz...
> Theo Charalambous wrote:
>
> > I believe COBOL
> > does a great job. But for front end programming no matter how exciting
it
> > is to do GUI devt with COBOL, it still seriously lacks behind tools like
> > VB, Delphi and many others...
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-25T21:39:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea90270_1@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <b89tod$rdn$1@aklobs.kc.net.nz> <3ea88436$0$16257$afc38c87@news.optusnet.com.au>`

```

"Theo Charalambous" <westleylodge@optusnet.com.au> wrote in message
news:3ea88436$0$16257$afc38c87@news.optusnet.com.au...
> I know about that. I've been using Fujitsu for a number of years...
However
> it is very VERY trivial in what it can do. If you are performing serious
> devt, the more you use it, the more its weakness and inability to perform
> certain things get in the way
>
> ... comparing it with something like (say) VB or WINDEV... well really
there
> is no comparison...
>

Interested to hear you say that, Theo. I completely disagree. I've used
PowerCOBOL for serious development and found there is nothing I can do with
VB that I CAN'T do with Fujitsu, for things I would WANT to do...(There are
a number of things I can do in VB that are really just a recipe for
disaster...<G>). (In fact, for building ActiveX/COM components, PowerCOBOL
is second to none... (this is what I mainly use it for...)).

After reading your previous post I went off to the Web and had a look at
WINDEV. Although French is my third language I understood enough to see what
is being claimed. I still wouldn't want to have full documentation in French
and rely on French language forums for help and advice.

> Fujitsu is a good COBOL package. Better than any other ones I used... but
> still limited inits GUI functionality... I haven't used COBOL for .NET.
> Maybe that's better.. time will tell
>

I'd be very interested to know precisely what "limitations" you are
referring to...???

However, I agree with you totally about the Fujitsu protection scheme. It
has done more damage to Fujitsu's product than it has good, even though it
is NOT so bad as everybody thinks. I transferred my 6.1 license to a floppy
disk and then to my new XP Pro machine with no problem at all (after
receiving clear advice from Fujitsu). Nevertheless, it is unwieldy and error
prone, and no-one likes to think they are dependent on a vendor in the
middle of the night when the backup has failed... There was a huge debate
about it here some years ago when it was first released. To Fujitsu's
credit, at least they don't charge a runtime fee....

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-24T19:53:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304241853.6e2e93a@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au>`

```
"Theo Charalambous" <westleylodge@optusnet.com.au> wrote 

> Vive La France...!

Well _I_ still haven't forgiven them for the terrorist attack that
they made on this country, also know as the Rainbow Warrior affair.
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-25T22:13:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea90a5b_1@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <217e491a.0304241853.6e2e93a@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304241853.6e2e93a@posting.google.com...
> "Theo Charalambous" <westleylodge@optusnet.com.au> wrote
>
…[3 more quoted lines elided]…
> they made on this country, also know as the Rainbow Warrior affair.

_I_ still haven't forgiven them for the attack on the "Fri" (in the 60s)
when
it sailed in International waters close to Mururoa atoll where the French
were testing their bombs. French naval commandos boarded the sailing ship,
beat up some friends of mine (one of whom was pregnant) threw their cameras
overboard, and threatened to sink the ship if it didn't depart their
arbitrarily imposed test zone immediately. This was nothing short of piracy,
carried out by a "friendly" nation against a defenceless merchant vessel.
They tested their bombs despite protests from all the nations of the Pacific
rim from Japan to Chile, we had strontium 90 falling on our pastures and
destroying the dairy industry (which was our second industry after wool at
that time), and they NEVER apologized or entertained claims for
compensation. (Instead, they shafted us by blocking the entry of NZ lamb to
our traditional market when the UK joined the Common Market. Heath was such
a wimp he rolled over and let them get away with it.)

(I believe that Greenpeace was formed as an organization by some of the
people who sailed on the "Fri".)

The Americans offered to share their underground facilities with them (they
were part of NATO at that time but withdrew in 65 (I think it was)) and/or
provide them with the data from the USA's own underground tests. But no.
Their arrogance demanded that they have their OWN nuclear deterrent and they
weren't about to test it in their OWN back yard...

Instead they destroyed part of paradise in the pursuit of their own
aggrandisement.

(There are mutated turtles on Mururoa which head inland instead of to the
Ocean when they hatch. As a result, they are now an endangered species...
The French reckoned they had cleaned it up by the 90s and were going to
build a holiday camp there... I could see people queueing up for that...at
least they wouldn't have to light it; the place glows in the dark....)

For me, the Rainbow Warrior incident was just the little tin hat on it.
(Don't start me on that one. I am impressed that Richard, who wasn't even
born here, understands and feels, like most Kiwis, how dreadful this was...)

To this day, I don't use French products.  When in Europe, I fill my car
with gas in Dover, drive off the hovercraft at Boulogne or Calais, and drive
until I get to Belgium. Not even a cup of tea in their God-forsaken
country...

Logic tells me there must be some very nice French people but I am probably
never going to meet them. As a nation, I wouldn't give them a push off the
side...bastards!

Now, about WINDEV....<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-25T13:29:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304251229.18fc42f0@posting.google.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <217e491a.0304241853.6e2e93a@posting.google.com> <3ea90a5b_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> _I_ still haven't forgiven them for the attack on the "Fri" (in the 60s)

Ooops, it looks like I opened a can of worms, or perhaps a can of frogs legs.

> As a nation, I wouldn't give them a push off the side...bastards!

Just as long as you don't get emotional about it then   ;-)
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-26T12:56:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea9d95b_2@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <217e491a.0304241853.6e2e93a@posting.google.com> <3ea90a5b_1@127.0.0.1> <217e491a.0304251229.18fc42f0@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304251229.18fc42f0@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > _I_ still haven't forgiven them for the attack on the "Fri" (in the 60s)
>
> Ooops, it looks like I opened a can of worms, or perhaps a can of frogs
legs.
>
> > As a nation, I wouldn't give them a push off the side...bastards!
>
> Just as long as you don't get emotional about it then   ;-)

Hahaha! Touche...still, it ISN'T computer programming, so I CAN get
emotional (and, regrettably, did...)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-25T17:58:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-DFD1BE.17584525042003@corp.supernews.com>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <217e491a.0304241853.6e2e93a@posting.google.com>`

```
In article <217e491a.0304241853.6e2e93a@posting.google.com>,
 riplin@Azonic.co.nz (Richard) wrote:

> "Theo Charalambous" <westleylodge@optusnet.com.au> wrote 
> 
…[3 more quoted lines elided]…
> they made on this country, also know as the Rainbow Warrior affair.

France actually attacked somebody?
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 and XP Pro

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-26T13:11:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea9dcdb_2@127.0.0.1>`
- **References:** `<3e929f38$0$20113$afc38c87@news.optusnet.com.au> <2786779.1050862827@dbforums.com> <bqUoa.1365$Vr6.2215980@newsserver.ip.pt> <217e491a.0304211307.16b4a3f0@posting.google.com> <3ea86164$0$16258$afc38c87@news.optusnet.com.au> <217e491a.0304241853.6e2e93a@posting.google.com> <joe_zitzelberger-DFD1BE.17584525042003@corp.supernews.com>`

```

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-DFD1BE.17584525042003@corp.supernews.com...
> In article <217e491a.0304241853.6e2e93a@posting.google.com>,
>  riplin@Azonic.co.nz (Richard) wrote:
…[8 more quoted lines elided]…
> France actually attacked somebody?

Well, it was an undefended boat moored in Auckland so they were pretty safe
really... Unfortunately there was a photographer asleep on it so when they
blew it up and it sank, the poor guy was killed. The amazing thing about
this was that the French Agents who did it were actually caught by the Kiwi
cops and brought to book. (Seems they had forgotten NZ is a series of
islands and, unlike Europe, there is nowhere to run to...Not only that, but
with a population which just reached 4 million yesterday, a couple of people
in trench coats with heavy French accents were not too hard to find...)

Despite not being the sharpest tools in the 007 toolbox these two agents
were "sold" back to France for $NZ8,000,000 on the understanding that they
would complete the prison terms imposed by the NZ courts. Instead, they were
treated as national heroes, decorated by the President and pardoned... The
ship they attacked (the Greenpeace owned "Rainbow Warrior") was raised,
towed to a point off the tip of the North Island and sunk again, where it is
now part of an underwater National Park and provides an artificial reef for
fish. This incident has scarred the psyche of New Zealanders and most of us
feel VERY strongly about it...

(Bottom line...if you meet a Kiwi at a party and are having a good time,
don't mention the Rainbow Warrior...<G>)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
