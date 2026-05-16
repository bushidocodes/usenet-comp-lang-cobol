[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Love and Hate

_20 messages · 8 participants · 2005-06 → 2005-07_

---

### Love and Hate

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-24T15:05:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11boprjfpnrkcff@news.supernews.com>`

```
Our COBOL application runs at several hundred sites.

A few of our users report the same symptoms: Upon entry to a drop-down box 
field, the program locks up. This happens to some users several times a 
day - maybe 10% of the times they enter the field.

We've torn the code apart, imbedded diagnostics, prayed. No joy.

Then, in a turn-around from how most programmers feel about users, one of 
our clients performed an experiment. They turned off Norton AV Shield on all 
the computers on their network.

It's been a week with no lock-ups when they were used to five or more per 
day.

It is unlikely we would have EVER caught this, um, "bug," since we use AVG 
from Grisoft.com instead of Norton's Anti-Virus.

You gotta love SOME users. And despise Norton.
```

#### ↳ Re: Love and Hate

- **From:** epc8@juno.com
- **Date:** 2005-06-25T14:00:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119733224.352936.311900@o13g2000cwo.googlegroups.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com>`

```
The OP wrote:

Our COBOL application runs at several hundred sites.

A few of our users report the same symptoms: Upon entry to a drop-down
box
field, the program locks up. This happens to some users several times a

day - maybe 10% of the times they enter the field. [snip] They turned
off Norton AV Shield on all the computers on their network. It's been a
week with no lock-ups ....

Reply:

Anti virus programs that run in the background are a known source of
trouble. It's too bad that some corporate standards mandate anti-virus
software and so called "software firewalls" that do more harm than
good.

I once had to deal with a vexing series of crashes involving Citrix.
One office could not install the terminal client so they installed a
browser client - which crashed. Of course corporate knew nothing of the
local set-up.... It turns out that this office was still on dial-up and
was sharing the connection via "WinProxy". The problem went away after
they went to DSL. The moral - software conflicts can be a real bear to
find and fix.
```

#### ↳ Re: Love and Hate

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-25T22:46:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9kmsd$pu8$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com>`

```

"HeyBub" (heybubNOSPAM@gmail.com) writes:
> 
> It is unlikely we would have EVER caught this, um, "bug," since we use AVG 
> from Grisoft.com instead of Norton's Anti-Virus.
> 
> You gotta love SOME users. And despise Norton. 

I've never had a problem with Norton Anti-virus. Macaffee, to the contrary
got replaced with Norton after we got tired of waiting 5-10 minutes
to boot on Dell Optiplex PCs after Macaffee was installed. Without Macaffee
the same PC would be booted by the time I had finished changing my voice
mail to include the current date.
 
On the other hand, Norton Internet Security 2004 and 2005 don't work
on my home machine unless I include Parental Control. That is, the
machine crashes several times a day if NIS is running without Parently
Control. Running it with Parental Control installed but disabled isn't 
at option because it insists on downloading huge PC updates even though
I have it disabled. The Parental Control updates are bloated, take way too
long to download and apply, and are useless to me. Symantec was unable to
provide any resolution, so I've given up on NIS.

NIS hadn't reported anything for several years anyway, so I decided it
was time to give up on NIS and Microsoft Internet Connection sharing, 
buying a Firewall Router. Should have done that a while back anyway.
 
Norton gets very upset when I tell it not to bother doing anti-spam.
 
I've already got double spam filtering on my home e-mail, one via IEEE's
e-mail alias server and a second level of filtering at my ADSL provider.

Giving Norton a chance to flag spam is actually counter-productive. If
I preview my inbox from web mail I can identify at least 99% of spam
from the subject and from lines, flagging it for reporting as spam
without ever opening it or receiving it onto my home nework.
```

##### ↳ ↳ Re: Love and Hate

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-25T16:49:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119743361.903446.86200@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d9kmsd$pu8$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <d9kmsd$pu8$1@theodyn.ncf.ca>`

```
> buying a Firewall Router.

"buying" ???

Use an old 486 or P100 box and install Freesco or Smoothwall Express.
These can be headless (no monitor) after install as they are controlled
from a browser.

Freesco (http://freesco.org) needs 6-8 MByte of RAM on a 386/20 or more
with a floppy to boot from, no hard disk required which makes it
extremely reliable and quiet, but it can be loaded to HD if you want to
use additional addons.

Smoothwall Express (http://sourceforge.net/projects/smoothwall/)
requires a 486, 16Mb,  400Mb HD.

Both need 2 or 3 Network cards (or NIC and external modem) which are a
few dollars each but otherwise will recycle machines that otherwise get
junked even though they work.
```

###### ↳ ↳ ↳ Re: Love and Hate

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-27T03:29:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9nrre$nnj$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <d9kmsd$pu8$1@theodyn.ncf.ca> <1119743361.903446.86200@g44g2000cwa.googlegroups.com>`

```

"Richard" (riplin@Azonic.co.nz) writes:
>> buying a Firewall Router.
> 
…[16 more quoted lines elided]…
> junked even though they work.

I found a new D-LINK firewall router for under CDN $50, so why bother
going to so much trouble?
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-26T23:09:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119852588.752286.318590@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<d9nrre$nnj$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119743361.903446.86200@g44g2000cwa.googlegroups.com> <d9nrre$nnj$1@theodyn.ncf.ca>`

```
> so why bother going to so much trouble?

And others may have an old 486/P100 that they don't want to pollute the
environment with and may ask 'why bother hunting for and paying $50+
for another unit'.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 5)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-27T16:24:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9p97k$hkk$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com>`

```

"Richard" (riplin@Azonic.co.nz) writes:
>> so why bother going to so much trouble?
> 
> And others may have an old 486/P100 that they don't want to pollute the
> environment with and may ask 'why bother hunting for and paying $50+
> for another unit'.

I already have several obsolete wintel boxes around. How much pollution is
generated to produce the power needed to run these? Even in standy by mode
they consume a surprising amount of power and as active firewalls they would
not be in standby. Does the power management software even work with the
confuguration you suggested? 

My oldest compaq never did go into true standby after I upgraded to win 95,
using the Compaq supplied upgrade and applying all available maintenance.
The most I could do was to get it to go into screen saver mode.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-27T12:06:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119899187.350607.187980@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d9p97k$hkk$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca>`

```
> as active firewalls they would not be in standby

Correct. As a replacement for 'Internet Connection Sharing' for other
computers they allow the existing large machine to shut down because it
is no longer the proxy.

> The most I could do was to get it to go into screen saver mode.

As the old machines will run headless there is no need to bother with
any screen saver, though they do actually blank the screen if they have
one.  Freesco without a Hard drive doesn't need standby mode for that
either.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 7)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-27T19:25:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11c166rmkt5i492@news.supernews.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com>`

```
Richard wrote:
>> as active firewalls they would not be in standby
>
…[9 more quoted lines elided]…
> that either.

It's STILL going to pull 100+ watts just sitting there (compared to maybe 10 
watts for a router). In a year the extra cost of power would have paid for 
the router.

And you will NOT be harming the environment if you leave the old machine in 
a school yard playground at night.

I swear to God, I'm going to take advantage of the "kitten syndrome" as 
applied to obsolete computers. Bring your old machine to my "adpotion 
center," pay me $40 for "shots," er, "refurbishing," and I PROMISE you I 
will find loving, caring, people who will welcome this piece of shit, er, 
vintage machinery into their homes, caring for it tenderly in its golden 
years.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 8)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-28T03:12:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9qf6p$8sf$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com>`

```

"HeyBub" (heybubNOSPAM@gmail.com) writes:
> 
> And you will NOT be harming the environment if you leave the old machine in 
…[7 more quoted lines elided]…
> years. 

Good for you. Leaving them by the side of the road doesn't seem to work
reliably. I drove my wife out to the ferry on a Friday evening so she could
visit a old friend in Vancouver. Spotted what looked like the same model of
Compaq we bought in 1998 by the side of the road, with it's CD and floppy
drives still in place. Still there when I drove home and again 2 days later
when I went to the ferry again and brought her back on Sunday. This was
only a 2 lane road, but it is one of the 3 main north south routes in a
built up urban area. Nobody seemed to want an 8 year old PC, even for 
parts.

Apple fanatics claim that "Sanitation Engineers" swear that they never 
see people throwing out Apples in the trash, only wintel boxes. OTOH,
there are up to 30 times as many wintels bought or replaced in a given
year as Apples. Small wonder more end up in the trash.

Value Village and other flea markets are full of them, with few takers.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 9)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-27T22:24:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11c1gndb1did1b6@news.supernews.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca>`

```
Kelly Bert Manning wrote:
> "HeyBub" (heybubNOSPAM@gmail.com) writes:
>>
…[18 more quoted lines elided]…
> Nobody seemed to want an 8 year old PC, even for parts.

Sloan-Kettering Clinic replaces about 75 PCs a year. They used to donate 
them to Boy Scouts, etc., they tried giving them away to employees. Finally 
converged on putting them obsolete PCs the curb for the Urban Faeries.

>
> Apple fanatics claim that "Sanitation Engineers" swear that they never
> see people throwing out Apples in the trash, only wintel boxes. OTOH,
> there are up to 30 times as many wintels bought or replaced in a given
> year as Apples. Small wonder more end up in the trash.

Sheer numbers are not the answer.

Would you expect someone who knits cozies for the computer, remembers its 
birthday (complete with noisemakers, games, and silly hats), and takes it 
for walks, to simply put it in the trash when it died? Would you do that to 
a beloved pet or member of YOUR family?

You have no compassion.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 9)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-06-28T23:23:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca>`

```
In article <d9qf6p$8sf$1@theodyn.ncf.ca>,
 bo774@FreeNet.Carleton.CA (Kelly Bert Manning) wrote:

> Good for you. Leaving them by the side of the road doesn't seem to work
> reliably. I drove my wife out to the ferry on a Friday evening so she could
…[11 more quoted lines elided]…
> year as Apples. Small wonder more end up in the trash.

That is funny.  It isn't because there are 30 times as many bought, it 
is because the Compaqs, Dells and various other wintel brands tend to be 
junk that will not last.  They remind me of the 'planned obsolescence' 
that Detroit used to do.  Even if you do buy the greatest box in the 
world, Micro$oft is going to make it useless when it releases the 
'revolutionary new OS' that it releases every other year.

I'm using a circa 1999 Apple as my primary box -- a dual G4/450mhz.  All 
I've added is enough hard drive space (using the pre-cabled bays and the  
RAID software built into the MacOS) to hold my extensive CD collection.  
It still performs wonderfully compared with todays wintel machines.

This is only a year younger than the piece of junk that nobody wanted in 
the Wintel version.  And I expect to get a few more years out of this 
one as well.

To top it off, my PowerMac DP G4/450 still sells on the used market for 
about $600.  Can you do that with any wintel from 1998 or 1999?  Can you 
even sell a wintel from last year?

There is an old saying -- you get what you pay for.

Sadly, Apples new slogan is "Think the Same" -- they are going to Intel 
chips next year...
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-28T20:45:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120016705.374779.262620@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com>`

```
> Micro$oft is going to make it useless when it releases the
> 'revolutionary new OS'

Certainly there is usually a usually a need to buy a new box for the
next version of Windows, but I quite often find that Windows users
complain about how slow their machines are even if they bought a new
one recently. Running Adaware or similar shows why this is: the
machines get bogged down with spyware, viruses and zombies just by
being on the Internet with IE and/or using Outlook Express.

The machines grind to a halt and so they buy a new machine with the
latest 3.x MHz CPU and this is now really zippy so they are happy ...
for a few months until the accumulation of collected junkware brings it
to its knees once again.

Microsoft don't want this fixed, nor do Dell or Gateway, they get to
sell lots more and profit.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 11)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-29T08:26:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11c58co5s89ml63@news.supernews.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com> <1120016705.374779.262620@g49g2000cwa.googlegroups.com>`

```
Richard wrote:
>> Micro$oft is going to make it useless when it releases the
>> 'revolutionary new OS'
…[6 more quoted lines elided]…
> being on the Internet with IE and/or using Outlook Express.

Same with AIDS: The incidence is very low among the celibate.

>
> The machines grind to a halt and so they buy a new machine with the
…[5 more quoted lines elided]…
> sell lots more and profit.

Not so. Micros~1 would like this fixed inasmuch as Micros~1 doesn't sell 
speed - it sells features.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-29T12:32:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120073524.897411.204310@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<11c58co5s89ml63@news.supernews.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com> <1120016705.374779.262620@g49g2000cwa.googlegroups.com> <11c58co5s89ml63@news.supernews.com>`

```
>> just by being on the Internet with IE and/or using Outlook Express.

> Same with AIDS: The incidence is very low among the celibate.

So your advice seems to be: don't use IE or Outlook.

>> Microsoft don't want this fixed, nor do Dell or Gateway, they get to
>> sell lots more and profit.

> Not so. Micros~1 would like this fixed inasmuch as Micros~1 doesn't sell
> speed - it sells features.

MS doesn't want it fixed in the _current_ system, it wants it fixed
(allegedly) in the next one (Longhorn) so that there will be a reason
for people to buy that. In fact people may even think that buying into
DRM and 'Trusted Computing' sounds like what they will need to fix the
malware, only it won't be.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-07-02T20:07:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cede$42c73a2d$45491c57$5867@KNOLOGY.NET>`
- **In-Reply-To:** `<1120016705.374779.262620@g49g2000cwa.googlegroups.com>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com> <1120016705.374779.262620@g49g2000cwa.googlegroups.com>`

```
Richard wrote:
> The machines grind to a halt and so they buy a new machine with the
> latest 3.x MHz CPU and this is now really zippy so they are happy ...
> for a few months until the accumulation of collected junkware brings it
> to its knees once again.

I've noticed that this new laptop I've got runs better under Linux than 
Windows, performance-wise.  One reason, I'm sure, is that the Linux is 
64-bit (which works better with the 64-bit chip) than Windows XP.  I can 
  even tell a difference in the temperature - I can leave the machine on 
all night under Windows, and it's pretty warm.  Under Linux, it's much 
cooler.

(I know enough about Windows (and firewalls) to keep the XP box spyware 
/ adware free - which is good...)
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-06-29T13:30:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9u7pa$de2$1@peabody.colorado.edu>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com>`

```

On 28-Jun-2005, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> That is funny.  It isn't because there are 30 times as many bought, it
> is because the Compaqs, Dells and various other wintel brands tend to be
…[3 more quoted lines elided]…
> 'revolutionary new OS' that it releases every other year.

I haven't bought a new computer because the computer nor the OS stopped working
as well as it used to.   I've bought new computers because I ran more and bigger
applications.    This is not exclusively a Wintell thing - Apples, Unix boxes,
mainframes, and even Crays have the same path.

Actually the Windows environment makes it difficult to upgrade, especially for
people who buy applications on-line which get registered in the registry.   I
know people who want to buy new computers, but are afraid that they will lose
stuff.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 11)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-06-29T17:59:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3igqusFlli3jU1@individual.net>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119852588.752286.318590@o13g2000cwo.googlegroups.com> <d9p97k$hkk$1@theodyn.ncf.ca> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <11c166rmkt5i492@news.supernews.com> <d9qf6p$8sf$1@theodyn.ncf.ca> <joe_zitzelberger-9753E4.23233728062005@ispnews.usenetserver.com> <d9u7pa$de2$1@peabody.colorado.edu>`

```
I've had a Gateway brand (well, Gateway 2000 at the time!) 200 MHz Pentium
PC since 1997.

It came with Windows 95 and I upgrade a few years later to Windows 98, which
I am still running today.
I upgraded the hard drive, buying a 40GB at about the same time, though I
still have the original 4GB HD, which has Linux on it now.
I've been through several monitors and keyboards, but the computer itself is
just fine.  A bit slow, maybe, but then I haven't bought any new software
since Windows 98 either.  Well, I guess I do have a fairly recent version of
Netscape.

I have bought parts this week and will "build" (put together) my new
computer.  But just for fun (?!).

I plan to re-install all of my applications, rather than "upgrading" them to
the new PC, but again that's just "for fun", and to start with a clean
slate.  There's a lot of junk I don't use on my current PC.  I'll keep it
around (or the HD, at least) just in case I want to access something I
haven't used in ages.

>>> Howard Brazee<howard@brazee.net> 6/29/2005 7:30:17 AM >>>

On 28-Jun-2005, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> That is funny.  It isn't because there are 30 times as many bought, it
> is because the Compaqs, Dells and various other wintel brands tend to be
…[3 more quoted lines elided]…
> 'revolutionary new OS' that it releases every other year.

I haven't bought a new computer because the computer nor the OS stopped
working
as well as it used to.   I've bought new computers because I ran more and
bigger
applications.    This is not exclusively a Wintell thing - Apples, Unix
boxes,
mainframes, and even Crays have the same path.

Actually the Windows environment makes it difficult to upgrade, especially
for
people who buy applications on-line which get registered in the registry.  
I
know people who want to buy new computers, but are afraid that they will
lose
stuff.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 7)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-28T02:46:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9qdl8$7vc$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119899187.350607.187980@g47g2000cwa.googlegroups.com>`

```

"Richard" (riplin@Azonic.co.nz) writes:
> 
> As the old machines will run headless there is no need to bother with
> any screen saver, though they do actually blank the screen if they have
> one.  Freesco without a Hard drive doesn't need standby mode for that
> either.

Booting from a CD are you?
 
Let's see, circa 1998 Compaq 2.5 amps at 100 volts, separate monitor
           circa 2000 Aptiva 4.0 amps at 100 volts, separate monitor
           circa 1995 Compaq with integrated monitor 3 amps at 100 volts
D-Link firewall router 2.4 amps at 5 volts.
 
Let's do the aritmetic, at 16 hours/day and $.06 per killowatt hour that
comes close to $100/year for 1,700 killowatt hours. Did I get the correct
result?

Even if you cut that by 75% you are still talking $25/year just in excess
power use. If you pay more than 6� per kwh or don't turn it off while
you sleep the loss goes higher.
```

###### ↳ ↳ ↳ Re: Love and Hate

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-27T22:59:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119938348.359634.86790@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d9qdl8$7vc$1@theodyn.ncf.ca>`
- **References:** `<11boprjfpnrkcff@news.supernews.com> <1119899187.350607.187980@g47g2000cwa.googlegroups.com> <d9qdl8$7vc$1@theodyn.ncf.ca>`

```
>> Freesco without a Hard drive doesn't need standby mode
>>  for that either.

> Booting from a CD are you?

No. The whole thing fits on a single 1.44 floppy and boots from that.
It runs Linux, is a firewall/gateway/router has a DHCP server and a
httpd server for control panel and for other services.  Not much room
left for web pages on the 1.44 though.

Of course one can boot from and/or run from CD if one has modern enough
equipment.

> Let's see, circa 1998 Compaq 2.5 amps at 100 volts,

Actually, an old 486 or P1xx takes _much_ less than that, especially
with no HD. You are merely taking the _maximum_ figures that the power
supply can output and assuming that is what it actually draws.
Typically a low power CPU, even an Intel one, will use 20 watts, a few
more for the RAM.

> separate monitor circa 2000 Aptiva 4.0 amps at 100
> volts, separate monitor circa 1995 Compaq with
> integrated monitor 3 amps at 100 volts

Perhaps you didn't understand the term 'headless'.

> Did I get the correct result?

I am sure that you get exactly the results that you intended to.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
