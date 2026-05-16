[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VM detection from COBOL

_20 messages · 7 participants · 2011-01 → 2011-02_

---

### VM detection from COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-31T13:35:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qmef5FhkvU1@mid.individual.net>`

```
An increasing number of people are getting involved with Virtual Machines.

They've been around now for quite some time but for many people it is just 
starting to become clear how useful these devices can be.

The latest release of ORACLE's VirtualBox is the best so far and I can 
recommend it to people who want to have a look at Virtual Computing.

Typically, I run Virtual Images for various versions of COBOL under Win XP, 
several test platforms where I can test new software deployment under Win 7 
and XP, and 1 or 2 "clean" machines with just a version of  the OS and not 
much else. Within the LAMP community some people run virtual images of 
different Linux distros and a Windows machine. It is an amazingly simple and 
useful way to test stuff (you can snapshot an image of the Virtual Machine 
with one click).

MS obviously figured it was going to be of interest because Win 7 comes with 
its own VM.(Virtual PC) I haven't tried it because the ORACLE product meets 
all my needs.

I run all these images on an attached 500GB external drive, which leaves my 
"real" machine free for "real" work. Performance is excellent, and the 
Virtual Machines are configured to join my wireless LAN so moving stuff 
betwen them is a breeze.

But, like most technologies, VM has a downside.

It is pretty easy to install licensed software to a Virtual Machine and then 
you can take the image anywhere, copy it, or pass it on. Even complex 
systems like Alchemy's (previously Fujitsu) CASPER registration where you 
are allocated a licence on a server at the vendor site, are not immune to 
this. (True at time of version 7; they may have plugged the hole since... 
don't know because I no longer have any dealings with them.) In fact, MOST 
software can be "pirated" (I use the term loosely, sometimes you may just 
want a backup copy for your own use or you may want to run something you 
have bought and paid for on a different laptop. As a software developer 
myself, I tend to avoid pirating other people's software. My point is that 
Virtualization means you CAN.), IF the said software can be installed to a 
Virtual Machine.

Obviously, concerned developers are starting to wake up to this and some of 
them have modified their deployment process so that it refuses to install to 
a VM. The problem is that it is VERY HARD to detect if the machine is 
virtual or not; as you might expect, the whole point of a Virtual Machine is 
to appear as "real" as possible. Furthermore, as there are a number of 
Virtual Machines available, and they implement virtualization in different 
ways, there is no "one size fits all" method of detecting if your software 
is being installed to, or is running on, a Virtual Machine.

I have recently completed a component that DOES do this and it actually does 
around a dozen checks of different kinds (based on other people's code in 
C++ and Assembler, then modified by me to suit my own purposes), which 
currently has 100% track record for detecting VMs. (The only one it hasn't 
been tested with is the MS VM in Win 7, but I have every reason to believe 
it will detect that too, and, if it doesn't, I'll fix it so it does... :-)

So, I have a component that can be called from most languages and it 
returns: yes, this is a VM; no, this is a real machine, or (extremely 
rarely) it is impossible to tell, due to hardware virtualization.

But for myself, I reckon people SHOULD be able to install software to a 
Virtual Machine and I should STILL be able to protect it from piracy. The 
recent PRIMA Product, RAV,  (Remote Application Validation) CAN do this. It 
doesn't matter whether RAV protected software is installed to a Virtual 
Machine or a real machine, it remains protected. Without any need for serial 
numbers and product codes (which can be cracked).

If anyone needs to detect a Virtual Machine from COBOL, and you don't want 
to re-invent a very large and complex wheel, contact me privately.

Pete.
```

#### ↳ Re: VM detection from COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-31T12:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ii688m$s51$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net>`

```
In article <8qmef5FhkvU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>An increasing number of people are getting involved with Virtual Machines.

[snip]

>If anyone needs to detect a Virtual Machine from COBOL, and you don't want 
>to re-invent a very large and complex wheel, contact me privately.

Your offer, Mr Dashwood, seems generous... but it made me smile.  Remember 
how, all those decades back, one of the goals of COBOL was to be as 
platform-independent as possible?  As the Anciente Riddle had it:

'How many programmers does it take to change a lightbulb?'

DD
```

##### ↳ ↳ Re: VM detection from COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-02-01T12:40:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qovjeF1j9U1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8qmef5FhkvU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
> DD

Sorry Doc, this is too obtuse for a simple mind like mine.

I have no idea what you are saying here.

Clues, please?

Pete.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-01T00:51:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ii7le3$50n$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net>`

```
In article <8qovjeF1j9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8qmef5FhkvU1@mid.individual.net>,
…[21 more quoted lines elided]…
>Clues, please?

As I understood it, Mr Dashwood, you were offering a way to determine the 
particular platform a COBOL program was running on; this struck me as a 
wry reversal (try saying that several times fast) of the intentions of the 
Oldene Dayse of making COBOL platform-independent... no need to know what 
platform one is running on.

As for the riddle the answer I was taught is 'None... that's a hardware 
problem.'

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-02-01T21:23:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qpu7lFupjU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8qovjeF1j9U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[33 more quoted lines elided]…
> hardware problem.'

Yes, that is the answerI was given when I first heard it but it was so long 
ago, I had forgotten... Nevertheless, good to revive an oldie but a goodie 
and I smiled when I saw your answer. :-)
>
> DD

Ah, thanks for the clarification.

I see what you're saying now. It shows how many platforms COBOL HAS 
permeated that it is even able to run on a Virtual Machine (that is NOT a 
mainframe - it was running on mainframe Virtual Machines  nearly 4 decades 
ago...).

The problem is not with COBOL it is with the fact that people can steal 
software once they have a Virtual Image of it. (Whether said software is 
written in COBOL or some other language.)

If you are a COBOL vendor charging thousands of dollars for a .Net compiler, 
for example, and someone can take a Virtual image of it and in doing so 
bypass all of your registration and licensing, it kind of makes a mockery of 
why you didn't protect it properly in the first place...Just because a 
protection system is complex (CASPER is the most unnecessarily complex 
system I have seen and I remember a number of furious posts about it in this 
forum when Fujitsu first announced it with NetCOBOL version 6; it alienated 
the customer base and it didn't even work because it could be easily 
circumvented...), doesn't make it invulnerable.

As the number of people doing this (and I would stress that I am NOT one of 
them; I have no interest in a .Net COBOL compiler and already turned down 
the offer of one for free) increases, I imagine there will be more care 
exercised by vendors.

PRIMA is finding that some of our clients also have HUGE investment in their 
software packages. (Some of these packages took years of COBOL development 
to make and contain assets and knowledge that is hard to put a value on....) 
We were asked for a solid protection solution that wouldn't cost an arm and 
a leg and the result is RAV. I haven't officially announced it yet but it is 
currently in beta on a customer site. I expect to have all the PRIMA 
products protected by it by the end of March.

I personally spent nearly 3 months looking at existing packages and their 
strengths and weaknesses and then designing a new approach from scratch.

I am confident it will do the trick and don't expect RAV protected software 
to be compromised, but time will tell :-)

During my reckless career I was tasked to do an IT security check on the 
internal systems of a major Bank in the U.K. One of the things I learned is 
that as long as there is legitimate access (and there obviously has to 
be...)  then NOTHING is secure. The best you can hope for is to know who 
took what, from where, and when, and get that notification as soon as 
possible after the event. In other words make sure the stable door gets 
closed as ssoon as possible after the horse is gone, or better yet, if at 
all possible, while they are stealing the horse... I've sat in meetings 
listening to snake oil salesmen promising data security and code security 
and application security and I've never heard one that wasn't flawed. 
(Sometimes they get quite petulant when you describe a scenario "outside the 
box" which renders their solution ineffective. You'd think they'd be glad... 
:-))

So I'm not going to be too arrogant about RAV. :-)

All I can say is it's the best I can do; if it does get broken, I'll fix it.

Meantime, I'm happy to make the VM detection component (which is a 
"spin-off") available to anyone who might find it useful.

Pete.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-01T12:39:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ii8uug$l11$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net>`

```
In article <8qpu7lFupjU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8qovjeF1j9U1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>>> docdwarf@panix.com wrote:
>>>> In article <8qmef5FhkvU1@mid.individual.net>,

[snip]

>>>> 'How many programmers does it take to change a lightbulb?'
>>>
>>> Sorry Doc, this is too obtuse for a simple mind like mine.
>>>
>>> I have no idea what you are saying here.

[snip]

>> As I understood it, Mr Dashwood, you were offering a way to determine
>> the particular platform a COBOL program was running on; this struck
…[10 more quoted lines elided]…
>and I smiled when I saw your answer. :-)

They say that... *something* is the first to go but I can't remember what.

>Ah, thanks for the clarification.
>
…[3 more quoted lines elided]…
>ago...).

Not *quite*, Mr Dashwood... I'm saying that decades ago a driving force 
behind COBOL was platform-independence, the ability to compile the same 
source code on different machines or under different operating systems and 
still get the same results from the data.

As a result there wasn't a need for applications-coders to have the 
facility your object offer offers; if the code ran the same way under all 
systems then why bother to find out what system it is on?

>
>The problem is not with COBOL it is with the fact that people can steal 
>software once they have a Virtual Image of it. (Whether said software is 
>written in COBOL or some other language.)

That's 'the problem' with a lot of stuff, Mr Dashwood... 'if you have 
something, you have something that you can lose'.

[snip]

>PRIMA is finding that some of our clients also have HUGE investment in their 
>software packages. (Some of these packages took years of COBOL development 
>to make and contain assets and knowledge that is hard to put a value on....) 
>We were asked for a solid protection solution that wouldn't cost an arm and 
>a leg and the result is RAV.

Not an uncommon problem, Mr Dashwood... the market for someone's product 
changes or the hardware-base on which the product run changes/expands and 
all of a sudden things become more easily stolen.  I hear that some rather 
advanced universities and such offer courses that specialise in just such 
things but, of course, they're always busy fighting the last war.

Me?  I code apps.

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-02-02T11:36:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qrg6sFsjaU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net> <ii8uug$l11$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8qpu7lFupjU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
>

I think you may have missed the point here, Doc. I probably wasn't clear 
enough.

The reason you might want to know if your software is running in a Virtual 
environment is because you may NOT want it to.

I guess an analogy might be:

1. You develop a COBOL app for, say, Hewlett Packard platforms.
2. All of your customers use that platform.
3. If the software can detect it is NOT running on a Hewlett Packard 
platform, then somebody is running an illegal copy of it and you may want it 
to close.

>>
>> The problem is not with COBOL it is with the fact that people can
…[4 more quoted lines elided]…
> something, you have something that you can lose'.

Truly, Glasshopper, ownership is indeed an illusion. But that illusion is 
part of the Dharma and we must deal with it before we can transcend it. In 
the game of business commerce "ownership" is to be protected; in the game of 
life it is to be discarded. The frog cannot own the lilypad and the lotus 
cannot own the water, yet both can enjoy these things. :-)

Pete.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-01T23:15:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iia46v$784$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <8qpu7lFupjU1@mid.individual.net> <ii8uug$l11$1@reader1.panix.com> <8qrg6sFsjaU1@mid.individual.net>`

```
In article <8qrg6sFsjaU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8qpu7lFupjU1@mid.individual.net>,
…[26 more quoted lines elided]…
>to close.

Almost there, Mr Dashwood... except back in the days of the '68 standard 
(and earlier) I recall things as being exactly the opposite; if the shop 
was running on one set of hardware and the folks in the Corner Office 
decided to switch to another the intention was to load in the source-code, 
compile and be on one's merry way.

Platform-independent.  'Changing the light bulb' was a hardware issue, not 
one that the software was supposed to be concerned about.

>
>>>
…[7 more quoted lines elided]…
>Truly, Glasshopper, ownership is indeed an illusion.

Oh, I *cannot* resist... further response might be merited were one to, 
after making such an assertion...

... own up to it.

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-02-02T09:23:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iibpev01qjh@news2.newsguy.com>`
- **In-Reply-To:** `<8qpu7lFupjU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> I see what you're saying now. It shows how many platforms COBOL HAS 
> permeated that it is even able to run on a Virtual Machine (that is NOT a 
> mainframe - it was running on mainframe Virtual Machines  nearly 4 decades 
> ago...).

For that matter, it was running on non-mainframe virtual machines (in
this sense) since at least 1999, when VMWare Workstation was released.
It was likely running on non-mainframe virtual machines before then; I
don't recall ever seeing MF COBOL running under the PC emulator that
was available for AIX 3.2 on the RS/6000, for example, but it would
have if anyone tried it.

Virtualized x86 systems are pretty old hat these days.

(And, of course, COBOL has been running on a "virtual machine" in the
Computer Science sense since at least the first MF COBOL runtime that
compiled to "intermediate code". But that's quite another matter,
despite the confusing terminology.)

> The problem is not with COBOL it is with the fact that people can steal 
> software once they have a Virtual Image of it. (Whether said software is 
> written in COBOL or some other language.)

Or in many, many other ways. Software copy protection is an arms race;
all you can do is increase the work factor for the attacker, in the
hope that it becomes (perceived as) more costly than purchasing a
legitimate copy. (And working against this is the intangible reward
many people apparently feel from illegally copying software - the
frisson of "getting away with it", etc. The "hacker rush" justifies,
in the economic sense, additional cost in breaking copy protection.)

In many cases, it's likely that the effort spent in copy protection,
plus the cost of annoying legitimate customers, is greater than the
profit reclaimed by reducing illegal copying.

> As the number of people doing this (and I would stress that I am NOT one of 
> them; I have no interest in a .Net COBOL compiler and already turned down 
> the offer of one for free) increases, I imagine there will be more care 
> exercised by vendors.

Running a COBOL compiler on a virtual machine is a perfectly
legitimate use of the product, and an important market. Eliminating
that possibility would cost far more in profit than it would recoup.

That said, what you've written is no doubt a nice piece of work, and I
hope people find it useful. I'm personally dubious that copy
protection is a productive use for it in most cases, but that's a
choice each vendor needs to make.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-02-02T15:40:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qtc6kFe3hU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net> <iibpev01qjh@news2.newsguy.com>`

```
In article <iibpev01qjh@news2.newsguy.com>,
	Michael Wojcik <mwojcik@newsguy.com> writes:
> Pete Dashwood wrote:
>> 
…[10 more quoted lines elided]…
> have if anyone tried it.

What's so magic about the PC?  I have been using COBOL compliers on non-
mainframe systems since at least the early 80's.  And without VM!!

M68K -- XENIX OS
Z80  -- CP/M, TRS-DOS
PDP-11 -- RT-11, RSTS, RSX
M6809 -- OS9

Probably others, but I can't remember them off the top of my head.

bill
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-02-03T08:10:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iiebuo0h33@news2.newsguy.com>`
- **In-Reply-To:** `<8qtc6kFe3hU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net> <iibpev01qjh@news2.newsguy.com> <8qtc6kFe3hU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <iibpev01qjh@news2.newsguy.com>,
> 	Michael Wojcik <mwojcik@newsguy.com> writes:
…[13 more quoted lines elided]…
> mainframe systems since at least the early 80's.  And without VM!!

This thread is specifically about COBOL on non-mainframe virtual
machines. I assume most people here know that COBOL implementations
have long existed for a wide variety of platforms.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-02-03T11:19:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qu3isFm5kU1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <8qovjeF1j9U1@mid.individual.net> <ii7le3$50n$1@reader1.panix.com> <8qpu7lFupjU1@mid.individual.net> <iibpev01qjh@news2.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[33 more quoted lines elided]…
> profit reclaimed by reducing illegal copying.

Hear! Hear! I would be much more concerned about annoying legitimate 
customers than in losing a few copies to piracy. Fortunately, these are not 
mutually exclusive choices if you implement RAV.
>
>> As the number of people doing this (and I would stress that I am NOT
…[11 more quoted lines elided]…
> choice each vendor needs to make.

Thanks for your post, Michael. Interesting as always.

I don't dispute any of the points you make.

The interesting things for me about this exercise  have been as follows:

1. I had to look at a lot of protection systems and decide what was good and 
bad about them.

2. I needed to do a lot of homework on the fundamentals of  VM piracy, and 
read some really excellent papers by various people. I followed this up with 
code analysis (mostly C++ and Assembler) and learned much, although some of 
that process was quite painful for me (How people work with the esoteric 
directives in C++ is beyond me but I guess it is all about what you're used 
to... :-) )

3. Having obtained some basic understandings of the problem I was then able 
to sit down and consider solutions from a completely fresh persective.

4. There has to be a certain amount of "inconvenience" if a web service is 
involved, because it has to be set up and not every developer is a web 
master.  I addressed this by getting all the "inconvenient" stuff into a 
one-time setup, that is as automated as we can make it.

5. It seemed to me that anything which relied on serial numbers or product 
codes was not an option. (They are far too easily hacked).

6. The best way for a vendor to maintain security on expensive software is 
to know who he sold or leased it to and develop a business relationship with 
that customer.  (There are other benefits in doing this which go way beyond 
software protection...)

7. A server which maintains licences and allows them to be transferred in 
and out (like CASPER) is just far too unwieldy and unnecessary. The process 
of moving stuff is a pain in the butt to customers. RAV can allow individual 
machines to be licensed, but generally we recommend site licensing.

The relationship is with a customer, not a given machine at his site.

(It is possible to limit the number of machines concurrently active if the 
software is installed to a server, but if it is installed to individual 
workstations they can run as many as they like. The attitude is that you are 
selling them the software to enjoy. Let them enjoy it. Stepped licensing 
schemes are really about marketing; we see a different approach. As long as 
the software cannot be moved off-site (and it can't)  there are benefits for 
both the vendor and the customer if free unfettered access to the software 
is available.

This is not the perceived wisdom and is arguable as a marketing strategy, 
however, I have discussed this model with people interested in RAV and the 
reaction has been very positive. If you are seen to be a vendor that DOESN'T 
hassle your customer base, that supports their use of your products, they 
have every incentive to maintain the relationship- and are probably in the 
running for upgrades and new products. This is part of the "small company" 
philosophy that PRIMA is based on. Your client base are not the enemy; treat 
them as friends. (But make sure that illegal copies of the software will not 
run.)

As noted elsewhere, it is very early days yet and it remains to be seen how 
we do. Nevertheless, I am very confident that we have a fair, and robust 
protection system, that requires minimal hassle to implement, and that 
hassle is isolated to some one-off processses.

Pete.
```

##### ↳ ↳ Re: VM detection from COBOL

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-02-02T07:01:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com>`

```
On Mon, 31 Jan 2011 12:00:22 +0000 (UTC), docdwarf@panix.com () wrote:

>>If anyone needs to detect a Virtual Machine from COBOL, and you don't want 
>>to re-invent a very large and complex wheel, contact me privately.
…[3 more quoted lines elided]…
>platform-independent as possible?  

Yep.

But a large part of my career has been in converting CoBOL systems to
different machines and databases.

>As the Anciente Riddle had it:
>>
>>'How many programmers does it take to change a lightbulb?'

I'm waiting with bated breath (having not yet read all of the replies
in this thread).
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-02T14:06:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iibodl$s4s$3@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com>`

```
In article <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 31 Jan 2011 12:00:22 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[10 more quoted lines elided]…
>different machines and databases.

Goals are not always reached, aye.

>
>>As the Anciente Riddle had it:
…[4 more quoted lines elided]…
>in this thread).

Pfawgh... been snacking at the the cheese-balls you've been using as bait?

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-02-02T15:54:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com> <iibodl$s4s$3@reader1.panix.com>`

```
On Wed, 2 Feb 2011 14:06:46 +0000 (UTC), docdwarf@panix.com () wrote:

>>I'm waiting with bated breath (having not yet read all of the replies
>>in this thread).
>
>Pfawgh... been snacking at the the cheese-balls you've been using as bait?

I like a Diet of Worms...
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-02T23:38:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iicpuc$ppl$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com> <iibodl$s4s$3@reader1.panix.com> <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com>`

```
In article <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 2 Feb 2011 14:06:46 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>I like a Diet of Worms...

That was all the rage, at one point... but it seems to await re-opening, 
having gotten canned.

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-02-03T12:54:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iuqlk65f6k7qjqcljpar7rfd4bodnv27o2@4ax.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com> <iibodl$s4s$3@reader1.panix.com> <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com> <iicpuc$ppl$1@reader1.panix.com>`

```
On Wed, 2 Feb 2011 23:38:52 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com>,
>Howard Brazee  <howard@brazee.net> wrote:
…[12 more quoted lines elided]…
>DD

Then there is the Imperial Diet of Worms.

Regards,
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-02-03T18:49:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iietc8$qpf$1@reader1.panix.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com> <iicpuc$ppl$1@reader1.panix.com> <iuqlk65f6k7qjqcljpar7rfd4bodnv27o2@4ax.com>`

```
In article <iuqlk65f6k7qjqcljpar7rfd4bodnv27o2@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
>On Wed, 2 Feb 2011 23:38:52 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <m5ojk6ll9nl2oce12b2lqiaq3jnchohmj6@4ax.com>,
>>Howard Brazee  <howard@brazee.net> wrote:

[snip]

>>>I like a Diet of Worms...
>>
…[3 more quoted lines elided]…
>Then there is the Imperial Diet of Worms.

Someone tried to wriggle that one past the King of England... We were not 
amused.

DD
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-02-03T03:39:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32ee7b78-96c3-4941-84e9-da8a98495e2f@g10g2000vbv.googlegroups.com>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com>`

```
On Feb 2, 2:01 pm, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 31 Jan 2011 12:00:22 +0000 (UTC), docdw...@panix.com () wrote:
> >>If anyone needs to detect a Virtual Machine from COBOL, and you don't want
…[23 more quoted lines elided]…
> - James Madison

Try these:
"How many Prolog programmers does it take to change a lightbulb?"
"No."

How many programmers does it take to change a light bulb?
None. If it is not broken don’t mess with it.

How many contract programmers does it take to change a light bulb?
Two, one always leaves halfway through the project.

How many windows programmers does it take to change a light bulb?
472. One to write WinGetLightBulbHandle, one to write
WinQueryStatusLightBulb, one to write WinGetLightSwitchHandle…

How many C++ programmers does it take to change a light bulb?
You’re still thinking procedurally. A properly designed light bulb
object would inherit a change method from a generic light bulb class,
so all you would have to do is send it a bulb change message.



For Doc Dwarf:
How many senior managers does it take to change a light bulb?
We’ve formed a task force to study the problem of why light bulbs burn
out and to figure out what, exactly, we as managers can do to make the
light bulbs work smarter, not harder.



And because this one mentions female programmers:
Q: How many internet mail list subscribers does it take to
change a light bulb?

A: 1,331:

1 to change the light bulb and to post to the mail list that
the light bulb has been changed

14 to share similar experiences of changing light bulbs and
how the light bulb could have been changed differently.

7 to caution about the dangers of changing light bulbs.

27 to point out spelling/grammar errors in posts about
changing light bulbs.

53 to flame the spell checkers

156 to write to the list administrator complaining about the
light bulb discussion and its inappropriateness to this mail
list.

41 to correct spelling in the spelling/grammar flames.

109 to post that this list is not about light bulbs and to
please take this email exchange to alt.lite.bulb

203 to demand that cross posting to alt.grammar,
alt.spelling and alt.punctuation about changing light bulbs
be stopped.

111 to defend the posting to this list saying that we are
all use light bulbs and therefore the posts **are** relevant
to this mail list.

306 to debate which method of changing light bulbs is
superior, where to buy the best light bulbs, what brand of
light bulbs work best for this technique, and what brands
are faulty.

27 to post URLs where one can see examples of different
light bulbs.

14 to post that the URLs were posted incorrectly, and to
post corrected URLs.

3 to post about links they found from the URLs that are
relevant to this list which makes light bulbs relevant to
this list.

33 to concatenate all posts to date, then quote them
including all headers and footers, and then add "Me Too."

12 to post to the list that they are unsubscribing because
they cannot handle the light bulb controversy.

19 to quote the "Me Too's" to say, "Me Three."

4 to suggest that posters request the light bulb FAQ.

1 to propose new alt.change.lite.bulb newsgroup.

47 to say this is just what alt.physic.cold_fusion was meant
for, leave it here.

143 votes for alt.lite.bulb.

plus:
10 to explain the etiology of the term 'light bulb' in Old English and
medieval French, with extra points for Ancient Languages.

20 to flame, then killfile, the poster as a hopeless idiot.

2 to defend the poster against these unwarranted attacks.

10 from college students changing their first light bulb, asking the
'pros' for advice, then being told to 'do your own homework, nitwit'.

1 demand to 'post your rates for lighting maintenance.'

100 forays into tangentally related topics such as lighting
appropriate to a dinner table or LCD
screen.

2 references to obscure movies directed by Max Ophuls and Bud
Boettecher, in which lighting
played an important part.

1 posting by a female programmer claiming she looks good in any
light.

200 followups to a posting where someone says 'you cannot illuminate
a ...'  in which they quibble over what what the original message said
after it has rolled off.

2 authoritative posts by COBOL experts reporting that neither LIGHT
nor LIGHTBULB are reserved words, never have been, but may be allowed
by 'vendor extensions'.
```

###### ↳ ↳ ↳ Re: VM detection from COBOL

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-02-04T10:34:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r0lasFvj0U1@mid.individual.net>`
- **References:** `<8qmef5FhkvU1@mid.individual.net> <ii688m$s51$1@reader1.panix.com> <hqoik69l41mp5a9mf8umlbqoil7gsib182@4ax.com> <32ee7b78-96c3-4941-84e9-da8a98495e2f@g10g2000vbv.googlegroups.com>`

```
Alistair Maclean wrote:
> On Feb 2, 2:01 pm, Howard Brazee <how...@brazee.net> wrote:
>> On Mon, 31 Jan 2011 12:00:22 +0000 (UTC), docdw...@panix.com ()
…[155 more quoted lines elided]…
> by 'vendor extensions'.

LOL!

It's a treasure, Alistair.

And spookily familiar to users of this group...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
