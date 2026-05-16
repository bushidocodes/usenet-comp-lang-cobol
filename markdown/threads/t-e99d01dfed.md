[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Network sharing with XP/Win 7

_6 messages · 3 participants · 2012-07_

---

### Network sharing with XP/Win 7

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-07-03T16:14:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5f9tsFbdtU1@mid.individual.net>`

```
I was wondering if anyone has had problems sharing Win 7 machines with XP 
machines across the LAN?

My new 64 Bit (Windows 7 Ultimate) machine would not play nicely with the XP 
machines on my LAN, although it was quite happy to talk to a Win 7 VM...

(I reckon it's snobbery... Windows 7 is just so snooty...)

After a number of hours of investigation, I have a solution and was thinking 
about wrapping it as Freeware if other people have the same problem.

And no, it's not off-topic... my COBOL server is an XP machine :-)

Pete.
```

#### ↳ Re: Network sharing with XP/Win 7

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2012-07-03T00:33:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m805v7p1bi8jeoibme0kqpudvej19fps2r@4ax.com>`
- **References:** `<a5f9tsFbdtU1@mid.individual.net>`

```
On Tue, 3 Jul 2012 16:14:50 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I was wondering if anyone has had problems sharing Win 7 machines with XP 
>machines across the LAN?
…[9 more quoted lines elided]…
>And no, it's not off-topic... my COBOL server is an XP machine :-)


A common issue is that Win7 defaults to using a new network protocol
called "HomeGroup", which XP (and Vista) don't support.  HomeGroup
makes connecting Win7 machines easier, but leads to issues with older
machines.

Anyway, the basic procedure is to switch the Win7 machine back to
Workgroup style networking, and to make sure all the machine have the
right workgroup name.

Anyway, it's been a while since I've had to fix that problem, but
there are many articles on the web on the issue.
```

##### ↳ ↳ Re: Network sharing with XP/Win 7

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-07-03T22:34:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5g04rF92uU1@mid.individual.net>`
- **References:** `<a5f9tsFbdtU1@mid.individual.net> <m805v7p1bi8jeoibme0kqpudvej19fps2r@4ax.com>`

```
Robert Wessel wrote:
> On Tue, 3 Jul 2012 16:14:50 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
>
That is just the beginning... :-) There are at least 5 other factors  (and 
many variations on them...) which must also be in place before Win 7 can 
actually access your shares.

It is very frustrating. I had done everything MS recommend, ticked all the 
boxes and the Win 7 machine was showing me the shared folders on a XP 
machine. However, as soon as I tried to open one of those folders, I 
received permission denied. BUT, only on SOME of the folders!

You'd think that would make it easy... just make sure everything matches the 
ones that work, right? Nope.

It was hours of bad advice on the Internet and combing specialist sites 
before I was finally able to share things properly and have it remain 
stable. (Some people succeeded in sharing OK but it  denied access a day 
later...) The difference now is that I understand WHY it didn't work, so all 
the swearing and sweating was not in vain. It also means that I can now 
write my new-found understanding into a C# program and forget about this 
problem for future additions to the network.


> Anyway, it's been a while since I've had to fix that problem, but
> there are many articles on the web on the issue.

Yes, the Homegroup is a no-no for mixed machines. And yes, there are 
thousands of people requesting help with this on the Web, but most of the 
solutions don't work... I spent hours poring over this and searching the 
web. That's why I thought an encapsulated solution might be useful. Making 
the manual adjustments you need to is fine if you are only sharing a couple 
of folders but if you have many it is really tedious.

I am going to write a utility where you simply give it a computer name and 
it shows you all the shares defined for that machine with a check box. You 
can check all (or whatever...) and then it will make the security changes 
needed on each folder automatically.

I have one machine with over 100 shares on it; I don't plan to make each of 
them visible to Win 7 manually...

If there is interest, I'll share the solution. But it is in a stack of 
priorities so how quickly it trickles up depends on what interest there is.

Pete.
```

#### ↳ Re: Network sharing with XP/Win 7

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2012-07-03T20:38:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ff33c2f$0$294$14726298@news.sunsite.dk>`
- **References:** `<a5f9tsFbdtU1@mid.individual.net>`

```
Pete Dashwood wrote:

> I was wondering if anyone has had problems sharing Win 7 machines with
> XP machines across the LAN?

Last time I checked no Win machines on the LAN here, sometimes an Apple
laptop (but that's also Unix, isn't it?).

> After a number of hours of investigation, I have a solution and was
> thinking about wrapping it as Freeware if other people have the same
> problem.

You should be applauded for that. BTW, freeware with or without source
code available?
```

##### ↳ ↳ Re: Network sharing with XP/Win 7

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-07-04T12:47:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5hi4hFtpcU1@mid.individual.net>`
- **References:** `<a5f9tsFbdtU1@mid.individual.net> <4ff33c2f$0$294$14726298@news.sunsite.dk>`

```
Fred Mobach wrote:
> Pete Dashwood wrote:
>
…[11 more quoted lines elided]…
> code available?

Gooid point Fred.

As it is dealing with security it is probably right and proper that source 
code should be available. When I get round to doing it, I'll make the 
utility AND the cource code downloadable from either COBOL21 or PRIMA sites.

Pete.
```

#### ↳ SUPPLEMENTAL: Re: Network sharing with XP/Win 7

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-07-05T01:31:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5iut4FmevU1@mid.individual.net>`
- **References:** `<a5f9tsFbdtU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I was wondering if anyone has had problems sharing Win 7 machines
> with XP machines across the LAN?
…[11 more quoted lines elided]…
> Pete.

There is an existing tool in Windows MMC that can do all the permissions at 
once. (Plus a lot more...)

I had the idea of applying multiple settings through a security policy in 
either Global Policies or Local Policies. When I went to look at this in 
more detail I found the security templates (in particular: Securews.inf) 
which can do this through the repair directory.

Although these things are tricky to learn and not user friendly, they do the 
job very well.

Interested parties should consult: 
http://technet.microsoft.com/library/Bb742512

(Fairly dry, but useful...)

OR...

http://www.utilizewindows.com/xp-menu/security/271-security-templates-in-xp

(Much more basic and good if you haven't done any of this stuff before... I 
think the author has English as a second language but it is still well 
written to inform...)

I probably won't write my own tool now...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
