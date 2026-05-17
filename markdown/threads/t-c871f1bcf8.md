[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# An interesting point.

_14 messages · 5 participants · 2018-03 → 2018-04_

---

### An interesting point.

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-03-21T23:05:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhgkr6Fc77fU1@mid.individual.net>`

```
In a recent thread here someone complained that he has to keep upgrading
his COBOL compiler as new versions of Windows are released.

Most of the compilers currently available for PCs generate 32 bit native
8086 code.

Fujitsu NetCOBOL Version 12 can generate 64 bit code and the various
(pretty expensive) compilers that generate CIL (Common Intermediate
Language - which is JIT compiled to CLR at run time - this would be the
".Net COBOL" or "NetCOBOL for .Net" group) can usually generate for 32
or 64 bit target environments.

So, mostly, it shouldn't be a problem. (At least you can salvage your
existing treasure, even if you may bitch about being forced to buy an
expensive compiler upgrade because the OS changed.)

But what has happened is that Windows OS has "evolved" away from its
original 16 bit native roots. .Net came along (first as a separate
"Framework") but increasingly as an integral part of the OS itself, and
we have the current situation where the .Net framework supports 32 bit
applications and 64 bit applications side by side on the same platform.

In effect, it is as if the OS would "prefer" 64 bit apps but recognizes
that you have a big investment in 32 bit stuff so it runs it for you at
great trouble to itself, but completely transparently to you (until you
inadvertently break one of the "rules"... like calling a 64 bit process
from a 32 bit thread, and it cannot reasonably do anything about
that...except stop)

Old-timers (like me) might be reminded of when 32 bit became available
and we were all terrified about what would happen to our many 16 bit
apps... Compatibility was provided, but eventually, it became necessary
to grasp the nettle and migrate. For most COBOL shops, that meant a
compiler upgrade and re-compiling everything.

Today, it would be inconceivable to develop and market a commercial 16
bit application (except for very unusual niche markets).

We are seeing movement by MS towards more embracing platforms (UWP) so
that various devices can run the same OS and this makes me wonder how
long they will continue to provide support for 32 bit applications.

Life would be much easier for them if they didn't have to, and I'm
fairly sure there will be pressure on Developers to move to 64 bit
during the next few years.

There will be support for 32 bit, of course, but that support will
diminish as time goes by. That, coupled with all the neat new features
that will become available as support for 64 bit increases, means that
most computer users will want 64 bit apps and 32 bit will be seen as
"quaint" or "obsolete".

COBOL developers will either buy a .NET compiler (did I mention they are
very expensive?...maybe the price will drop as more people adopt it...),
or they'll buy a less expensive (but still not cheap) upgrade for native
code generation in 64 bits.

(Those of us who migrated off COBOL to Java or C# will not be affected
because our compilers and IDEs are free, and they support 32 or 64 bit...)

So, for most COBOL shops it will just mean spending more money, and they
are quite used to that.

But, here's the "interesting point"... People who chose to use Fujitsu
PowerCOBOL, CANNOT upgrade their compiler and development IDE because
there is no sign of a 64 bit PowerCOBOL environment on the horizon. A
search of the GTS web site reveals no reference to PowerCOBOL, or even
the fact that they sell it.

These Fujitsu users are probably feeling much like the Micro Focus users
who went with VISOC...

(If you are one of them, and haven't already done so, you should look at
migrating to WinForms and .Net NOW. PRIMA has a solution for this that
costs much less than a .Net OR a native code COBOL Compiler:
https://primacomputing.co.nz/PRIMAMetro/PwrCOBMigration.aspx ...AND you
can continue using COBOL in the new .Net environment if you want to,
WITHOUT having to buy COBOL for .Net...)

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: An interesting point.

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2018-04-18T22:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<fhgkr6Fc77fU1@mid.individual.net>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net>`

```
On Thursday, March 22, 2018 at 2:05:13 PM UTC+11, pete dashwood wrote:
› In a recent thread here someone complained that he has to keep upgrading
› his COBOL compiler as new versions of Windows are released.

There are 2 ways to deal with this.
1. Stick with the existing version of Windows.
2. Upgrade to the latest version of Windows.

Some of us realised that the "upgrades" are to make money for the vendor,
aka M$.

There's an old saying, "if it works, don't fix it."

Some of us are obliged to keep using older versions of Windows
on account of the fact that printers or other devices & compilers
do not work on later versions of the OS.

Some of us realised that with every new version of M$ Windows,
there are still the old bugs (which never get fixed) plus new ones.

So, I run DOS + Windows 3.1 with Word 1.1a for almost all documents;
Windows 95 and Word 6 with special printer;
Windows 98 with certain compiler;
Windows XP with various printers, and internet.
Windows 10 for internet. Pretty well useless with anything else. A WOFTAM.
Fortunately, I have a printer that runs with XP and 10.
No doubt another version of Windows will come that won't support
that printer ....

› Most of the compilers currently available for PCs generate 32 bit native 
› 8086 code.
…[72 more quoted lines elided]…
› WITHOUT having to buy COBOL for .Net...)
```

##### ↳ ↳ Re: An interesting point.

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-04-19T17:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p2@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap>`

```
In article <93a87cbe-d672-413a-b06e-5e3··8@goo··s.com>,
wrote:
› On Thursday, March 22, 2018 at 2:05:13 PM UTC+11, pete dashwood wrote:
›› In a recent thread here someone complained that he has to keep upgrading 
…[25 more quoted lines elided]…
› that printer ....

As shown above, with grace and elegance... if it isn't changed one gets
saddled with a set of environments and skills that become increasingly
expensive to support. If I recall correctly there are licenses that
Microsoft has with the governments of the UK and Denmark for whatever
Windows version will still allow Internet Explorer Version 6 to run.

Is it a matter of 'if it ain't broke, don't fix it' or 'no matter what the
environment does We Will Not Evolve'? Printers are hardware, hardware is
made by companies, companies wither and vanish on the summer's breeze...
if you don't build your systems with certain Facts o' Business in mind
you're building your systems with an inherent brittleness.

Ignoring the software - which nobody ever understands, anyhow - every so
often it is good to take a tour of a Museum of Computing Equipment. (a
fellow I know runs one in Seattle, WA, USA and the trips are informative.)
The stuff I know is, of course, all in the back... and looking at the Wall
of Language Evolution is like reading the names off a monument to Those
Fallen in the Great War.

But... look at the more recent hardware. For some readers here, you've
owned it, you've run it, you've made it sing polyphony... and it's in a
museum. Any business depending on that particular piece of kit depends on
something which has been offered for preservation in a Temple of the
Muses... in the USA, the hardware gets fully depreciated for tax purposes
in three years. A simple folding-chair, if used regularly, will
eventually break and a CPU or a GPU is no different.

Granted that some Truths withstand the test of the aeons... such as
Compound-Interest Calculations. What machine a business uses is not such
a Truth and locking a company into a fatal embrace with a particular set
of wires is a strategy nigh guaranteed to cause agita with every upgrade
cycle.

DD
```

###### ↳ ↳ ↳ Re: An interesting point.

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-20T00:37:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p3@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p3@usenetarchives.gap>`

```
On 20/04/2018 9:14 AM, doc··f@pa··x.com wrote:
› In article <93a87cbe-d672-413a-b06e-5e3··8@goo··s.com>,
›    wrote:
…[36 more quoted lines elided]…
› environment does We Will Not Evolve'? 

I absolutely endorse this and could not have expressed it better. So
many times in my career I have seen companies brought to a standstill by
this kind of thinking.

Computer systems (hardware and software) are NOT motorcycles or similar
mechanical devices where the aphorism might have some applicable value.

Printers are hardware, hardware is
› made by companies, companies wither and vanish on the summer's breeze...
› if you don't build your systems with certain Facts o' Business in mind
› you're building your systems with an inherent brittleness.
 
› Yep... 100%.
› 
…[8 more quoted lines elided]…
› owned it, you've run it, you've made it sing polyphony...

Ah, you've heard the 1403 printer doing "Anchors Aweigh" then... :-)
(Getting this to happen is considerably more difficult than playing it
on an Amiga or Sinclair spectrum, for instance, and modern platforms are
designed to make music if you want them to, just as easily as they make
documents.)
and it's in a
› museum.  Any business depending on that particular piece of kit depends on
› something which has been offered for preservation in a Temple of the
› Muses... in the USA, the hardware gets fully depreciated for tax purposes
› in three years. 

It's 5 years here and in the UK... :-) (We are probably less consumer
orientated than the USA.)

A simple folding-chair, if used regularly, will
› eventually break and a CPU or a GPU is no different.
›
Even though the CPU and GPU have no moving parts (except at a Quantum
level), you are still correct; eventually things fail.

› Granted that some Truths withstand the test of the aeons... such as
› Compound-Interest Calculations.  What machine a business uses is not such
…[3 more quoted lines elided]…
› 

Spot on, Doc. It's like arguing with a mirror... :-)

Pete.



I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-04-20T13:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p4@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p3@usenetarchives.gap> <gap-c871f1bcf8-p4@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 20/04/2018 9:14 AM, doc··f@pa··x.com wrote:
 
› [snip]
 
›› Granted that some Truths withstand the test of the aeons... such as
›› Compound-Interest Calculations.  What machine a business uses is not such
…[5 more quoted lines elided]…
› Spot on, Doc. It's like arguing with a mirror... :-)

Which one's got it backwards?

DD
```

##### ↳ ↳ Re: An interesting point.

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-20T01:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p2@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap>`

```
On 19/04/2018 2:29 PM, rob··s@gm··l.com wrote:
› On Thursday, March 22, 2018 at 2:05:13 PM UTC+11, pete dashwood wrote:
›› In a recent thread here someone complained that he has to keep upgrading
…[4 more quoted lines elided]…
› 2. Upgrade to the latest version of Windows.

OR... move off COBOL. (I realize that may not be an option for some, but
it certainly worked for me...)

However, the problem being referenced here is not just about languages
and OSes; it is about the whole use of and life expectancy of any given
computer system.

›
› Some of us realised that the "upgrades" are to make money for the vendor,
› aka M$.

Given that the upgrades are generally free from MS, and given that the
OP was complaining about having to upgrade his COBOL compiler (which
isn't even sold by MS) you might be being a little unfair here.
›
› There's an old saying, "if it works, don't fix it."

You have no idea how much I HATE that expression... :-)

I have seen it cost companies large amounts unnecessarily.

When you develop a computer system you should plan what it's effective
life is to be. In many cases, it will last way beyond that (see the
thread about the US IRD in this forum). You should also look at what
possible ongoing costs may be involved... new peripheral devices and
drivers, etc. If there is an OS upgrade and your existing peripherals
won't work because it can't run the old drivers, then that's a fact of
life... You either stay with what you have or you replace the
peripheral, or you find(write) a new driver...

It's all part of the joy of computing. :-)



›
› Some of us are obliged to keep using older versions of Windows
› on account of the fact that printers or other devices & compilers
› do not work on later versions of the OS.

That's hardly the fault of the OS vendor. They have a moral duty to get
as much backward compatibility as they can, but you cannot expect them
not to continue developing their software because a small percentage of
their user base are in love with a 15 year old printer/scanner that is
now obsolete...

The point that the expression above does not address, is that there is
no progress without change.

›
› Some of us realised that with every new version of M$ Windows,
› there are still the old bugs (which never get fixed) plus new ones.

Sure, you should talk to Android and OS/x developers...

Windows is far from perfect in this regard, but neither is anyone else.

› 
› So, I run DOS + Windows 3.1 with Word 1.1a for almost all documents;
…[3 more quoted lines elided]…
› Windows 10 for internet. Pretty well useless with anything else. A WOFTAM.

You could argue that ANY and ALL computer systems can be considered a
WOFTAM at some point...

I am staggered (and very impressed... :-)) by your list above.

› Fortunately, I have a printer that runs with XP and 10.
› No doubt another version of Windows will come that won't support
› that printer ....

Yes, that's highly likely. And it would probably be the same if you were
running Linux or a Mac. It is up to the device manufacturer to provide
driver support for their devices. OS vendors give them months before a
new version is launched, so they can do this.

› 
›› Most of the compilers currently available for PCs generate 32 bit native
…[73 more quoted lines elided]…
›› WITHOUT having to buy COBOL for .Net...)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: An interesting point.

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-04-20T05:21:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p6@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap>`

```
On Fri, 20 Apr 2018 17:41:33 +1200, pete dashwood
wrote:

› On 19/04/2018 2:29 PM, rob··s@gm··l.com wrote:
› 
…[8 more quoted lines elided]…
› now obsolete...


There's a circular argument here: A piece of hardware becomes
"obsolete" when it's no longer supported by the latest software and
the authors of the software no longer support the hardware because
it's "obsolete." I suspect the truth is that software vendors test
their products on more recent hardware and if the older stuff happens
not to work, that's life. Testing is expensive, and with new hardware
being sold all the time, I would guess that there's relatively little
benefit to maintaining compatibility with hardware that hasn't been
sold for a while.

A few years ago, I had to replace a perfectly good laser printer after
I upgraded from XP to Windows 7 because I could no longer find a PCL6
driver for it (PCL6 seemed to be necessary for automatic duplexing).

There didn't seem to be a good reason for it, but then there didn't
have to be. We're fools to complain when this happens, but we delude
ourselves when we pretend that it always makes sense.

Louis
```

###### ↳ ↳ ↳ Re: An interesting point.

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-20T07:36:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p6@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap>`

```
On 04/20/2018 01:41 AM, pete dashwood wrote:
› On 19/04/2018 2:29 PM, rob··s@gm··l.com wrote:
›› On Thursday, March 22, 2018 at 2:05:13 PM UTC+11, pete dashwood wrote:
…[8 more quoted lines elided]…
› it certainly worked for me...)

Or another option. Dump MS entirely and move your application to
Linux and GNU COBOL. I have tested programs ranging from IBM
Mainframe COBOL to MicroFocus and old Ryan-MacFarland COBOL and
have not run into any show stoppers or even challenges. As a
matter of fact, if the programs are pure COBOL (that means no
additions like CICS) all I have ever had to do was massage
SELECT statements to allow for differences in file naming conventions.

› 
› However, the problem being referenced here is not just about languages 
…[7 more quoted lines elided]…
› Given that the upgrades are generally free from MS, 

Since when? As each of my XP and Vista systems has been EOLed I have
been forced to move off of Windows entirely because the only other
solution is to BUY a new OS. Not even a discount offered for the
old one. And Windows Server versions the same. I still have a copy
of 2012 running but it. too, will be the last.

› and given that the
› OP was complaining about having to upgrade his COBOL compiler (which
› isn't even sold by MS) you might be being a little unfair here.

One can upgrade to new versions og GNU COBOL for the same price as the
original copy. :-)

››
›› There's an old saying, "if it works, don't fix it."
…[3 more quoted lines elided]…
› I have seen it cost companies large amounts unnecessarily.

On this, we agree, with a caveat. Change for the sake of change is
never a good idea.

› 
› When you develop a computer system you should plan what it's effective 
…[6 more quoted lines elided]…
› peripheral, or you find(write) a new driver...

I have been involved in a discussion on this in another group. People
who have had a 20 year warning that something they were using was dead
and would eventually be officially deprecated but did nothing and are
now complaining that it may be removed from an OS and they have all
these applications using it.

› 
› It's all part of the joy of computing. :-)
 
› Remember when they told us computing would make life so much easier? :-)
 
 
› 
› 
…[13 more quoted lines elided]…
› no progress without change.

True, but then, the opposite is also true. There is no change without
progress. As another note, it is amazing how much old hardware (stuff
that the company did not plan on even existing at this point) that
still works under Linux. Parallel printers (if you can find a machine
with a parallel port :-) I guess the biggest question I would have
for people running these old printers is where do you get your ink
cartridges? :-)

› 
›› 
…[5 more quoted lines elided]…
› Windows is far from perfect in this regard, but neither is anyone else.

No OS is perfect. A recent find in OpenVMS was a bug/feature that had
been in the OS for at least 20 years undiscovered.

› 
›› 
…[10 more quoted lines elided]…
› I am staggered (and very impressed... :-)) by your list above.

Only makes me wonder why he isn't just using a typewriter or, for
that matter, a pencil and paper. Don;t need those dang computer
things to write a letter or do my financial reckonen'. :-)

› 
›› Fortunately, I have a printer that runs with XP and 10.
…[4 more quoted lines elided]…
› running Linux or a Mac. 

Can't speak for MAC. I expect you need an Apple printer for them
but for Linux, you would be amazed at how much really old hardware
is still supported. I expect the hardware will become extinct before
OS and application support stops. I still use the very first scanner
I ever got. A SCSI HP flatbed. Still works fine and is supported by
SANE. The only printers I have had to get rid of were the ones I
could no longer buy ink or toner for.

› It is up to the device manufacturer to provide
› driver support for their devices. OS vendors give them months before a
› new version is launched, so they can do this.

Only in the Windows world. I am not aware of any printer or scanner
vendor who provided a Linux (or Unix) driver. They were always done
by the OS maintainers often with no help from the hardware vendor at
all.

› 
›› 
…[7 more quoted lines elided]…
››› or 64 bit target environments.

GNU COBOL can do 32 and 64 bit as well.

bill
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-20T22:40:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p8@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap>`

```
On 20/04/2018 11:36 PM, Bill Gunshannon wrote:
› On 04/20/2018 01:41 AM, pete dashwood wrote:
›› On 19/04/2018 2:29 PM, rob··s@gm··l.com wrote:
…[18 more quoted lines elided]…
› SELECT statements to allow for differences in file naming conventions.

If GNU COBOL cannot do what you need it to (handle objects and COM
components, in my case...) then that is not an option.

If the programs are "pure COBOL" as you refer to it, and the compiler is
producing Native Code, then you wouldn't need to upgrade your compiler
with MS either.

My original point, and I stick to it, is that the OS vendor is NOT
responsible for your COBOL implementation.
› 
›› 
…[13 more quoted lines elided]…
› solution is to BUY a new OS.

Two points:

1. XP was available as a free upgrade from Win 98 for several months
after it was released. Win 10 was free to both XP AND Windows 7 users
for about a year after it was released. (People who used Vista were
unlucky, I guess...)

2. You seriously believe that rather than spend $100 or so on the new
OS, it was actually cheaper to move everything off Windows? OK, that's
your option and your opinion, but, if you are developing software for
other people to use, you HAVE to have a Windows version, so it makes
sense to use Windows yourself.



  Not even a discount offered for the
› old one.  And Windows Server versions the same.  I still have a copy
› of 2012 running but it. too, will be the last.
…[6 more quoted lines elided]…
› original copy.  :-)
 
› Assuming GNU COBOL can do what you need it to.
› 
…[8 more quoted lines elided]…
› never a good idea.

Agreed. It is also important to realize that not ALL change represents
progress... Nevertheless, there cannot be progress without change.

› 
›› 
…[18 more quoted lines elided]…
› Remember when they told us computing would make life so much easier? :-)
 
› "Modern life" (whatever that means...) would be impossible without it.
 
› 
› 
…[18 more quoted lines elided]…
› progress.  

Huh!?

I have seen many changes that caused disaster and retrograde steps...


As another note, it is amazing how much old hardware (stuff
› that the company did not plan on even existing at this point) that
› still works under Linux.  Parallel printers (if you can find a machine
…[3 more quoted lines elided]…
› 

Linux provides some excellent generic drivers, but, as noted above, it
is not really the responsibility of the OS vendor to support your
devices; it is properly the duty of the device vendor to provide drivers
for the OSes you wish to use.

(BTW, it is not terribly hard to write a device driver if you need to.
Anyone with understanding of Assembler and OS interrupt vectors can do
it. You DO need proper documentation from the device vendor if you wish
to avoid a lot of trial and error...)



›› 
››› 
…[28 more quoted lines elided]…
› 
I am a firm believer in people doing what they find comfortable as far
as computer use goes. But I have to admit, I was a bit rocked when I saw
this... :-)

›› 
››› Fortunately, I have a printer that runs with XP and 10.
…[21 more quoted lines elided]…
› all.

I would not in any way disparage the efforts of the people who work on
Linux. The fact that most vendors have not provided Linux versions of
drivers for their device, is purely based on commercial reality, where
they expect the majority of their customers to be running Windows.

It is therefore necessary for Linux engineers to provide these drivers.
I think that might change in the next few years as we see more
acceptance of Linux in commercial environments.
› 
›› 
…[11 more quoted lines elided]…
› GNU COBOL can do 32 and 64 bit as well.

As it generates C, I would hope so... :-)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-21T09:07:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p9@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap> <gap-c871f1bcf8-p9@usenetarchives.gap>`

```
On 04/20/2018 10:40 PM, pete dashwood wrote:
› On 20/04/2018 11:36 PM, Bill Gunshannon wrote:
›› On 04/20/2018 01:41 AM, pete dashwood wrote:
…[22 more quoted lines elided]…
› components, in my case...) then that is not an option.

Well, luckily, most COBOL isn't that it is COBOL as COBOL was
intended to be. :-)

›
› If the programs are "pure COBOL" as you refer to it, and the compiler is
› producing Native Code, then you wouldn't need to upgrade your compiler
› with MS either.

Tell that to the compiler vendors who refuse to continue support
on older compilers. Or did you think that after the first year
bugs cease to exhibit?

›
› My original point, and I stick to it, is that the OS vendor is NOT
› responsible for your COBOL implementation.

I agree, but the OS vendor can also force a change when the upgrade
breaks the compiler.

›› 
››› 
…[20 more quoted lines elided]…
› unlucky, I guess...)

Well, I certainly don;t remember any free upgrades and we were using
Windows since the days of WfW3.11. And, anyway, I was one of those
Vista users. Much better than XP ever was.

› 
› 2. You seriously believe that rather than spend $100 or so on the new 
…[3 more quoted lines elided]…
› sense to use Windows yourself.

Well, I guess I was thinking of principals rather than developers.
Personally, I don't know why any business is still using MS products.
Offers no advantage at an exceptional cost.

› 
› 
…[12 more quoted lines elided]…
› Assuming GNU COBOL can do what you need it to.
 
› For the majority of real world COBOL, it can.
 
›› 
›››› 
…[10 more quoted lines elided]…
› progress... Nevertheless, there cannot be progress without change.
 
› Now, how do we convince all the MS users about that.  :-)
 
› 
›› 
…[21 more quoted lines elided]…
› "Modern life" (whatever that means...) would be impossible without it.
 
› "Modern life" has a lot more disadvantages, too.
 
› 
›› 
…[23 more quoted lines elided]…
› I have seen many changes that caused disaster and retrograde steps...

I guess I was thinking positive change. It is true that change for
changes sake does not necessarily imply progress.

› 
› 
…[11 more quoted lines elided]…
› for the OSes you wish to use.

Maybe, but I think the more important concept is that Linux has proven
that unless the vendor (hardware or OS) went out of his may to make
things obtuse special drivers are really not necessary

› 
› (BTW, it is not terribly hard to write a device driver if you need to. 
› Anyone with understanding of Assembler and OS interrupt vectors can do 
› it. You DO need proper documentation from the device vendor if you wish 
› to avoid a lot of trial and error...)
 
› Especially if the vendor chose to make things difficult.
 
› 
› 
…[13 more quoted lines elided]…
› Thank you.
 
› Your welcome.  what did I do?
 
››› 
›››› 
…[48 more quoted lines elided]…
› they expect the majority of their customers to be running Windows.

Or, it could be based on the fact that Linux doesn't require special
drivers for most devices, like printers. Printers are pretty much
generic. Serial, parallel, USB or ethernet for the interface. The
majority use PS or PCL for rendering. (At least most laser printers.)

› 
› It is therefore necessary for Linux engineers 
 
› engineers?  :-)
 
›                                                 to provide these drivers. 
› I think that might change in the next few years as we see more 
› acceptance of Linux in commercial environments.

I doubt it. The only change I think likely is the printers will
become more generic than they already are. The odd man out now
is the inkjet and as the price of color laser drops I see them
fading away just like dot matrix.

›› 
››› 
…[14 more quoted lines elided]…
› As it generates C, I would hope so... :-)

People seem to disparage GNU COBOL because it generates C and
then compiles it (totally transparently to the user). How is
that any different from compilers that generate CIL or RTL or
any other form of intermediate language?

It's kinda like Ada, I guess. Ada advocates early on were some of
the strongest C detractors I knew. And yet the first Ada (non-
certified) compilers generated C from the Ada and then compiled
the C. Which told me that there was nothing Ada could do that
could not be done in C.


bill


bill
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 6)_

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2018-04-24T21:05:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p10@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap> <gap-c871f1bcf8-p9@usenetarchives.gap> <gap-c871f1bcf8-p10@usenetarchives.gap>`

```
On Saturday, April 21, 2018 at 11:08:00 PM UTC+10, Bill Gunshannon wrote:

› I doubt it.  The only change I think likely is the printers will
› become more generic than they already are.  The odd man out now
› is the inkjet and as the price of color laser drops I see them
› fading away just like dot matrix.

Unlikely to happen any time soon.
The prices of inkjet printers has been dropping too.

While the price of color laser printers has decreased over the years,
the price of printer cartridges has increased markedly.
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-04-21T22:27:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p9@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap> <gap-c871f1bcf8-p9@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:

[snip]

› (BTW, it is not terribly hard to write a device driver if you need to. 
› Anyone with understanding of Assembler and OS interrupt vectors can do 
› it. You DO need proper documentation from the device vendor if you wish 
› to avoid a lot of trial and error...)

Doing something is not terribly hard. Doing something well...

DD
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 4)_

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2018-04-21T07:12:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p8@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap>`

```
On Friday, April 20, 2018 at 9:36:27 PM UTC+10, Bill Gunshannon wrote:
› On 04/20/2018 01:41 AM, pete dashwood wrote:
›› On 19/04/2018 2:29 PM, r..··.@gm··l.com wrote:
 
› Only makes me wonder why he isn't just using a typewriter or, for
› that matter, a pencil and paper.  Don;t need those dang computer
› things to write a letter or do my financial reckonen'.  :-)

At early computer sites, it was not uncommon to see an abacus
in a glass case, with the instructions,
"in emergency, break glass".
```

###### ↳ ↳ ↳ Re: An interesting point.

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-21T09:09:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c871f1bcf8-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c871f1bcf8-p13@usenetarchives.gap>`
- **References:** `<fhgkr6Fc77fU1@mid.individual.net> <gap-c871f1bcf8-p2@usenetarchives.gap> <gap-c871f1bcf8-p6@usenetarchives.gap> <gap-c871f1bcf8-p8@usenetarchives.gap> <gap-c871f1bcf8-p13@usenetarchives.gap>`

```
On 04/21/2018 07:12 AM, rob··s@gm··l.com wrote:
› On Friday, April 20, 2018 at 9:36:27 PM UTC+10, Bill Gunshannon wrote:
›› On 04/20/2018 01:41 AM, pete dashwood wrote:
…[9 more quoted lines elided]…
› 

I still have several slide rules within easy reach. Including a
blackboard slide rule I saved from a trip to the dumpster.

You can have my Picket trig/log/log when you pry it from my cold
dead hands. :-)

bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
