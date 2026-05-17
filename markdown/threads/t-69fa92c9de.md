[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# It's virtually impossible...

_8 messages · 4 participants · 2017-08 → 2018-09_

---

### It's virtually impossible...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-22T20:33:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f040rkFifi3U1@mid.individual.net>`

```
... to run older versions of COBOL on modern Windows platforms, without
getting any problems. (the keyword here is "virtually"; more in a minute...)

We have been getting clients who are bitterly disappointed when they try
and port their old Micro Focus NetExpress or Fujitsu NetCOBOL COBOL
compilers to Windows 10. I had similar experiences myself.

NetCOBOL version 6 (and 7) does NOT implement well in Windows 10. This
is really fair enough, because GTS provide a COBOL compiler that DOES
work fine in that environment.(Version 10)

I see the following options:

1. Move away from these compilers (GNU COBOL - unfortunately doesn't
provide what is needed for us: COM support and OO COBOL)

2. Upgrade to the latest COBOL compilers from either of these vendors.
(Expensive...)

3. Move on from COBOL altogether and download free compilers for C#
and/or VB.NET. Instead of spending significant money, you invest
significant time in going round the learning curve for a new language,
but EVERYTHING (including immediate online support and tuition) is FREE!
In my opinion, it is very well worth the time, and the rewards far
exceed staying with COBOL. This is what I did. Never regretted it (You
don't "unlearn" COBOL when you learn C#, but you do have to adjust some
attitudes...)

4. If you don't want to make more heavy investment into COBOL (both
Micro Focus and Fujitsu products, although excellent, are expensive...),
and you feel you are too old a dog to learn new tricks, then give what
you have what it needs; provide an XP Windows environment to run COBOL.

I STRONGLY RECOMMEND using a virtual XP machine to run your Windows
COBOL on, IF you are using older versions of the compilers.

OK, so there are no regular updates anymore and you will need a good
anti-virus if you expose your VM to the Internet, but I've been running
just such a VM for over 5 years now and had NO problems.

The VM software we use at PRIMA is Oracle's Virtual Box. Over the years
it has become better and better and it is free... The current version is
truly excellent and we have never had a fail caused by the Virtual
Machine(s).

You may be a bit intimidated by the idea (I was...) but it really is
very easy and simple, and today they have streamlined everything to make
it a no-brainer. You can do all your COBOL on the virtual machine (VM)
and everything runs fine. Copy your output results to whatever machine
you want it running on. (I have automated this for PRIMA and we use WMI
scripting to automate remote COBOL access from any machine on the LAN,
but you don't need to go that far; you can easily manually copy/move
compiled code to wherever you want it.)

Each VM, although it may be hosted on a single laptop or computer,
appears on your LAN as a separate machine, just as you would expect, and
it is easy to forget that these "machines" are not "real"...

Set it up once then you can "virtually" forget about it... :-)

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: It's virtually impossible...

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-23T01:42:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p2@usenetarchives.gap>`
- **In-Reply-To:** `<f040rkFifi3U1@mid.individual.net>`
- **References:** `<f040rkFifi3U1@mid.individual.net>`

```
On 8/22/2017 7:33 PM, pete dashwood wrote:
› ... to run older versions of COBOL on modern Windows platforms, without 
› getting any problems. (the keyword here is "virtually"; more in a 
…[9 more quoted lines elided]…
› (snip)

Just for my curiosity, are there similar problems porting Micro Focus
NetExpress and Fujitsu NetCOBOL compiles to Windows Vista, 7, or 8?

Using a Windows XP virtual machine seems like a very good solution.
Would a Windows 7 virtual machine also work?

Windows 7 is still supported for a few more years...


http://www.arnoldtrembley.com/
```

##### ↳ ↳ Re: It's virtually impossible...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-25T19:52:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-69fa92c9de-p2@usenetarchives.gap>`
- **References:** `<f040rkFifi3U1@mid.individual.net> <gap-69fa92c9de-p2@usenetarchives.gap>`

```
On 23/08/2017 5:42 PM, Arnold Trembley wrote:
› On 8/22/2017 7:33 PM, pete dashwood wrote:
›› ... to run older versions of COBOL on modern Windows platforms, 
…[20 more quoted lines elided]…
› 
I know of one site that is running Win 7 on a VM and they were
originally using Fujitsu NetCOBOL version 7. They did experience some
problems with it and moved up to version 9. Since then everything seems
to be OK.

At PRIMA we use a VM running XP as the "COBOL server" and it is
primarily Fujitsu NetCOBOL version 9 and PowerCOBOL that we use for
looking at client stuff. There are NO problems with this and it works
just like it did when it was running on a real XP machine. The lack of
updates is not a problem either; in fact, this platform remains stable
because it is not being "messed with"...

The OBJECT (native) code produced by compiling code generated by our
tools, runs fine on Windows 10.

This whole area of running managed (CIL) or unmanaged (native) code is
something that is next on my list of priorities.

For the new PowerCOBOL migration tool we are generating a NetCOBOL OO
Class for the code-behind, that compiles to 32 bit native code, just
like the current scriptlets do. The code runs on all windows platforms
using the InterOP services of .Net (which was designed by MS
specifically for running legacy native code as "unmanaged" under .Net)
and we have no problems with it.

I would like to compile it to 64 bit but I don't have a COBOL compiler
that can do that. The obvious one would be "NetCOBOL for .Net" which
compiles to 64 bit managed code. It is very expensive and I already have
a C# compiler that compiles to 64 bit managed code (if I want that) so I
am not inclined to fork out for the COBOL equivalent.

Obviously, I could rewrite the generated code-behind into C# but that
requires more time than I have available at the moment. The tool already
generates the new Form definitions in C# so THEY can be 32 or 64 bit, no
problem.

When the new web site is complete and launched, I'll then look at the
whole business of getting 64 bit code-behind for migrated PowerCOBOL Forms.

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: It's virtually impossible...

- **From:** "rtwolfe78" <ua-author-14501825@usenetarchives.gap>
- **Date:** 2017-08-30T13:59:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-69fa92c9de-p2@usenetarchives.gap>`
- **References:** `<f040rkFifi3U1@mid.individual.net> <gap-69fa92c9de-p2@usenetarchives.gap>`

```
On Wednesday, August 23, 2017 at 1:42:34 AM UTC-4, Arnold Trembley wrote:
› On 8/22/2017 7:33 PM, pete dashwood wrote:
›› ... to run older versions of COBOL on modern Windows platforms, without 
…[22 more quoted lines elided]…
› http://www.arnoldtrembley.com/

Arnold:

GT Software does work with Flexus to migrate Micro Focus COBOL applications using the Flexus ReFocus Automated migration service to various versions of Fujitsu NetCOBOL for Windows or Fujitsu NetCOBOL for .NET:

DISPLAY/ACCEPT to NetCOBOL GUI using COBOL sp2
Screen Section to NetCOBOL GUI using COBOL sp2
Micro Focus Dialog System to NetCOBOL using Flexus sp2 Script
Micro Focus Dialog System to NetCOBOL GUI using C# and WinForms

Bob Wolfe
Flexus
rtw··e@fle··s.com
www.flexus.com
```

###### ↳ ↳ ↳ Re: It's virtually impossible...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-30T20:49:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-69fa92c9de-p4@usenetarchives.gap>`
- **References:** `<f040rkFifi3U1@mid.individual.net> <gap-69fa92c9de-p2@usenetarchives.gap> <gap-69fa92c9de-p4@usenetarchives.gap>`

```
On 31/08/2017 5:59 AM, Bob Wolfe wrote:
› On Wednesday, August 23, 2017 at 1:42:34 AM UTC-4, Arnold Trembley wrote:
›› On 8/22/2017 7:33 PM, pete dashwood wrote:
…[38 more quoted lines elided]…
› 
Hi Bob,

Is "NetCOBOL GUI" a standard Fujitsu offering, or something offered by
GTS, or something that is offered from Flexus? I never heard of it and
am worried that I might have missed something... :-)

We just spent a huge amount of time and effort to get PowerCOBOL into C#
and Winforms. If there is a standard product that we missed and which
could have helped, I'd really like to know about it.

Cheers,

Pete.

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: It's virtually impossible...

_(reply depth: 4)_

- **From:** "rtwolfe78" <ua-author-14501825@usenetarchives.gap>
- **Date:** 2017-08-31T06:50:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-69fa92c9de-p5@usenetarchives.gap>`
- **References:** `<f040rkFifi3U1@mid.individual.net> <gap-69fa92c9de-p2@usenetarchives.gap> <gap-69fa92c9de-p4@usenetarchives.gap> <gap-69fa92c9de-p5@usenetarchives.gap>`

```
On Wednesday, August 30, 2017 at 8:49:52 PM UTC-4, pete dashwood wrote:
› On 31/08/2017 5:59 AM, Bob Wolfe wrote:
›› On Wednesday, August 23, 2017 at 1:42:34 AM UTC-4, Arnold Trembley wrote:
…[62 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

Pete,

No. It's not a special product from Fujitsu or GT Software. Fujitsu also supports a Linux version of NetCOBOL which does not provide any screen handling whatsoever. We support that product as well with:
1. Our character mode user interface tools for a terminal-based user interface;
2. Use of NetCOBOL for Linux for the purpose of creating a server-based COBOL application that utilizes our Thin Client software for the creation of remote Windows interfaces (across a TCP/IP network); and
3. Use of NetCOBOL for Linux for the purpose of creating a server-based COBOL application that utilizes our Web Client/X, HTML/Javascript/JASON/AJAX based interface that displays the user interface on remote web browsers.

I used the term GUI simply to differentiate a graphical user interface implementation using NetCOBOL versus a character mode interface or a remote Thin Client or Web Browser user interface using our other tools.

My apologies for the confusion.
```

###### ↳ ↳ ↳ Re: It's virtually impossible...

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-31T20:59:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-69fa92c9de-p6@usenetarchives.gap>`
- **References:** `<f040rkFifi3U1@mid.individual.net> <gap-69fa92c9de-p2@usenetarchives.gap> <gap-69fa92c9de-p4@usenetarchives.gap> <gap-69fa92c9de-p5@usenetarchives.gap> <gap-69fa92c9de-p6@usenetarchives.gap>`

```
On 31/08/2017 10:50 PM, Bob Wolfe wrote:
>>>
›› Hi Bob,
…[25 more quoted lines elided]…
› My apologies for the confusion.

No apology necessary (it was I who was confused... :-))

Thanks for the clarification.

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: It's virtually impossible...

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-25T01:43:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-69fa92c9de-p8@usenetarchives.gap>`
- **In-Reply-To:** `<f040rkFifi3U1@mid.individual.net>`
- **References:** `<f040rkFifi3U1@mid.individual.net>`

```
pete dashwood wrote:

› ... to run older versions of COBOL on modern Windows platforms, without
› getting any problems. (the keyword here is "virtually"; more in a
…[42 more quoted lines elided]…
› Machine(s).
Seems to me that this is just kicking the problem farther down the
(time) line. Eventually whatever backlevel version of OS, or even VM tool,
that you use will become unsupported and/or no longer understood by new
staff, and you'll be back where you started, but with an even higher curb
to climb in migrating your applications. That would leave three viable (if
painful) options, in order of pain level: :-) 1) Migrate to a different
dialect of COBOL, 2) Migrate to an entirely different language, or 3)
migrate to an entirely different platform.
› 
› You may be a bit intimidated by the idea (I was...) but it really is
…[14 more quoted lines elided]…
› Pete.

JLT
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
