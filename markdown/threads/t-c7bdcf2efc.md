[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Every Shop Has Some Assembler Somewhere" - course update

_27 messages · 12 participants · 2004-07_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### "Every Shop Has Some Assembler Somewhere" - course update

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-07-07T18:32:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040707143232.11581.00001180@mb-m11.aol.com>`

```
[Tune for subject line quote: "Everybody Loves Somebody Sometime"]

Well, it's true, every shop does have some Assembler code somewhere.

And I have just finished updating my Assembler course "z/OS
Assembler for applications Programmers" (3 days) to include
the new hardware instructions recently announced as well as
z/OS V1.5 and HLASM V1.5 changes.

While I promote our Assembler series as being for applications
programmers, systems programmers can often get a good running
start by attending some or all of these courses. Here is how
the curriculum is designed:

OS/390 Assembler Language: Classic (5 days) - the first
       course for someone new to Assembler, includes all
       the original S/360 instruction set plus S/370
       and some later instructions

OS/390 Assembler Language: Interfaces (3 days) - the
       natural follow on, covering static and dynamic
       linkages, I/O macros, basic dump reading, and
       some other commonly used macros (e.g.: WTO,
       TIME, etc.)

OS/390 Assembler Language: Update (1 day) - for new
       assembler programmers who have taken the above
       sequence, and experienced Assembler programmers
       who have not had a chance to learn the major
       changes in the Assembler and hardware instructions
       prior to z/Architecture

z/OS Assembler for Applications Programmers (3 days)
       for new or experienced assembler programmers who
       need to pick up the hardware and Assembler info
       introduced by z/Archicture and z/OS.

The Assembler gurus in your shop are probably your sharpest
technical employees, and keeping them current pays back to
your bottom line in many ways (performance, debugging,
even morale and enthusiasm). If you are losing your
Assembler gurus to retirement, downsizing, outsourcing, etc., 
you should consider growing some replacements by a carefully
thought-out training program.

Go to our page about our Assembler curriculum:

    http://www.trainersfriend.com/assemcurric.htm

there you will find more information, including links
to the detail information for each Assembler course we
offer (and, at the bottom of that page, links to courses
we teach that are mulit-lingual and include Assembler).

Kind regards,

-Steve Comstock
The Trainer's Friend, Inc.
303-393-8716 - from anywhere
800-993-8716 - toll free from in the States
```

#### ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-12T08:42:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccubh0$2t98$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com>`

```

"S Comstock" <scomstock@aol.com> wrote in message
news:20040707143232.11581.00001180@mb-m11.aol.com...

> Well, it's true, every shop does have some Assembler code somewhere.

I think this statement might be a bit -- umm ... provincial.   It's true so
long as you summarily ignore any environment in which it's false, and there
are environments in which it is not only false today but has been false for
something over four decades.

I'd be hard-pressed to find any assembler code in your average Unisys MCP
shop.  There's none in the operating system, the support libraries, the
application support stuff (like the data base access routines), or the
compilers, and Unisys not only doesn't provide, but actively discourages the
third-party development of, assemblers for the system.

    -Chuck Stevens
```

##### ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-12T16:36:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com>`

```
To clarify,  I think that Steve's course offering are intended ONLY for IBM
mainframe shops.  I know this post went (primarily) to such forums (fora?).  I
am not certain whether they are even particularly relevant in these days to VM
or VSE - even though the HLASM product *is* portable across such systems.

Much of what he offers for COBOL would *probably* be usable for other COBOL
environments, but (as far as I know) are certainly NOT tailored (targeted?) for
such.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-12T10:25:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccuhhl$31bt$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net...

> To clarify,  I think that Steve's course offering are intended ONLY for
IBM
> mainframe shops.

That much I was able to glean much later in the posting.  The quotes I was
addressing were the subject line and the first line of the message, "Well,
it's true, every shop does have some Assembler code somewhere."

It may be true that every shop *to which he might market his software* has
some Assembler code.  It may also be true that every shop *in which he has
any interest* has some Assembler code.

But I have to admit discouragement that contributors to comp.lang.cobol are
so quick to dismiss the relevance not only of Unisys' (and Burroughs' and
Sperry Univac's) contributions to the history of COBOL over nearly the last
five decades but also the continuing presence of Unisys MCP and Unisys
OS2200 environments not just in the US but worldwide.  I'm not as familiar
with the marketplace of the OS2200 environments, but I can say that Unisys
MCP systems running applications written in COBOL represent a significant
presence worldwide, probably most prominently in the financial marketplace.


> Much of what he offers for COBOL would *probably* be usable for other
COBOL
> environments, but (as far as I know) are certainly NOT tailored
(targeted?) for
> such.

Well, that's my point.  I have no objection to the product, nor do I intend
to denigrate in any way the value of his product *to those shops to whom it
would be useful*.  However, that set of shops is not *every shop*.

I don't even mind sloganeering, but repetition of the slogan as *universal*
truth rather than clarifying the context in the repetition is a tacet
dismissal of any possible counterexample shops from outside the "every shop"
set.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 4)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-12T13:06:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NMt8ApHpvKOY092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com>`

```
Here in comp.lang.cobol,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>I'm not as familiar with the marketplace of the OS2200 environments,
>but I can say that Unisys MCP systems running applications written in
>COBOL represent a significant presence worldwide, probably most
>prominently in the financial marketplace.

I've seen A-series boxes in the strangest places.  Two of my more recent
interviews were with companies which were fairly small, but which still
heavily used COBOL on an MCP box to run a number of key applications.

I wish more OS2200 shops existed, though.  :-)  At least locally, the
only two I know of are Unisys itself and NWA, and neither one of them
seem to be hiring (the latter for obvious reasons).
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-12T13:46:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccutaq$7of$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com>`

```
"Richard Steiner" <rsteiner@visi.com> wrote in message
news:NMt8ApHpvKOY092yn@visi.com...

> I wish more OS2200 shops existed, though.  :-)  At least locally, the
> only two I know of are Unisys itself and NWA, and neither one of them
> seem to be hiring (the latter for obvious reasons).

 The Unisys home page has links to case studies for ClearPath and
ClearPathPlus servers that appear to me to be pretty evenly distributed
between OS2200 and MCP environments, although I can't really address their
geographic distribution, nor do I have access to a larger list of OS2200
clients (or how that list compares in either number or "basic average shop
size" to the MCP list)!

The MCP systems have historically covered a very wide object-code-compatible
range of performance; indeed, I believe that range is wider than any of its
competition, covering everything from extremely powerful enterprise servers
to laptop-based demonstration and development systems and everything in
between.   These systems also were actively marketed as upgrade paths for
ex-Burroughs-architecture systems such as the B1000, B2/3/4000, and V Series
systems occupying the small-to-medium enterprise environments (and in the
case of B4000 and V series, some pretty large ones too!).

The OS2200 has been, and I believe remains, popular in the powerful
enterprise server market.  I don't think it's had as much impact in the
medium-sized and smaller shops, and part of that may have been simply
because I don't think Unisys (or Univac) marketed it as a replacement
architecture for any other product offerings (for example, the ex-RCA
architectures or even the 418 series).  Part of the reason such marketing
opportunities weren't pursuied as actively for the OS2200 architecture may
have had to do with the complexities of dealing with 8-bit bytes on a
36-bit-word system, but my opinion on this may be based on obsolete
information (I last worked on an 1108 in about 1970) or simple ignorance
(I've been working on Burroughs systems and their direct descendance pretty
much exclusively since 1974 and will admit some prejudice in their favor!).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 6)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-12T16:42:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MXw8ApHpvOgG092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com>`

```
Here in comp.lang.cobol,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>The OS2200 has been, and I believe remains, popular in the powerful
>enterprise server market.

All I know is that airlines like NWA and UAL still use them, and some
other large organizations like NASDAQ did not long ago (whether or not
they still do I have no idea).

>Part of the reason such marketing opportunities weren't pursuied as
>actively for the OS2200 architecture may have had to do with the
>complexities of dealing with 8-bit bytes on a 36-bit-word system, but

I don't think so (see below).  I think it was more a corporate culture
thing -- Sperry was more an engineering company than a marketing one
from what I've heard (I didn't join Unisys until 1988 so all I know is
what my betters told me <g>).

>my opinion on this may be based on obsolete information (I last worked
>on an 1108 in about 1970) or simple ignorance (I've been working on
>Burroughs systems and their direct descendance pretty much exclusively
>since 1974 and will admit some prejudice in their favor!).

I really like what I've seen of the MCP environment, although I must
admit CANDE took a little getting used to.  :-)  Not a bad editor for
its time, and considerably better than some of the stuff I've seen on
the 2200 side (though I wish a multiwindowed fullscreen editor like
UEDIT existed for the A; if it does, the shop that I worked in didn't
have a copy).

Anyway...  ASCII data on a 2200 is typically stored in quarter words
(9-bits per byte), but it usually isn't a factor for the applications
programmer, though that does somewhat depend on the specific language
being used.  As Fortran 66 programmers with no CHARACTER data type we
tended to care a lot.  :-)  But a 2200 COBOL programmer uses PICTURE
clauses for most things which look just the same as anywhere else.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-13T14:15:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd1jdo$21ri$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com>`

```

"Richard Steiner" <rsteiner@visi.com> wrote in message
news:MXw8ApHpvOgG092yn@visi.com...
> Here in comp.lang.cobol,

> I don't think so (see below).  I think it was more a corporate culture
> thing -- Sperry was more an engineering company than a marketing one
> from what I've heard (I didn't join Unisys until 1988 so all I know is
> what my betters told me <g>).

Well, I understand your point, but what Burroughs/Unisys did with the Large
System was make the hardware and software *more attractive* to the users of
machines from which they wanted people to migrate -- Burroughs Small
(page-mode editing in CANDE, changes to COMS, some new utilities and new
features to existing ones inter pluribus alii) and Medium (an entire utility
and product -- EVA -- devoted to conversion of COBOL programs, and STOQ and
CRCR support in both the MCP and in languages come to mind) Systems.  When
the descendants of the Univac 9000 series and the RCA Spectra/70 rode off
into the sunset, my understainding is that they were directed toward the A
Series (and, in fact, I seem to remember that the "last gasp" of this
architecture was a Burroughs B5900 with different microcode; if that wasn't
the case, I do remember an effort in that direction!).   These weren't just
marketing exercises; *significant* engineering effort went into them.

There may have been corporate culture involved, but it's a lot easier to
migrate software that "thinks" in 8-bit bytes onto a machine that "thinks"
in 8-bit bytes than to one that gives you a choice between 9-bit and 6-bit
characters!   Whether that presented a *real* engineering challenge or not,
I think it presented psychological difficulties at the time, and I think the
Burroughs architecture was deemed a more suitable platform for making
migrations easy than the Univac big-iron -- from an engineering standpoint.

> I really like what I've seen of the MCP environment, although I must
> admit CANDE took a little getting used to.  :-)  Not a bad editor for
…[3 more quoted lines elided]…
> have a copy).

There are some products like that available; check out Programmer's
Workbench; it's our latest and greatest in this area.  Runs on a PC,
connects to the MCP system, interfaces with the interactive debugger, the
whole bit.  It's intended to provide the functionality of the best of the
source handling software available on PC's.

I've been using OBJECT/ED (=SYSTEM/EDITOR) for decades, and in my view it's
a lot better than "page-mode CANDE".  I don't know for sure, but this may
have grown out of the need to provide suitable migration paths for B1000
users, who had a somewhat similar single-user utility called TEXT/EDITOR.
SYSTEM/EDITOR came out around the time the pricing structure went from
"bundled" to "unbundled", and CANDE remained "bundled", so I think user
management balked at paying a high price for EDITOR when their programmers
had been coping perfectly well with CANDE for some decades.  Unisys could
have marketed this product much more effectively, I think.

> Anyway...  ASCII data on a 2200 is typically stored in quarter words
> (9-bits per byte), but it usually isn't a factor for the applications
…[3 more quoted lines elided]…
> clauses for most things which look just the same as anywhere else.

Yeah, I understand -- but I don't know what the 2200 does for *8-bit*
EBCDIC.  What I seem to remember is that you actually do end up with
four-and-a-half-byte words, and I think both management and engineering
found the concepts of mapping bytes from another architecture into
four-and-a-half-byte words a bit daunting!   Six-byte words in the same
character set is difficult enough!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 8)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-13T17:46:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8YG9ApHpvWbF092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com>`

```
Here in comp.lang.cobol,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>"Richard Steiner" <rsteiner@visi.com> wrote in message
>news:MXw8ApHpvOgG092yn@visi.com...
…[9 more quoted lines elided]…
>EBCDIC.

Neither do I.

We never dealt with EBCDIC directly in the 2200 systems that I've worked
with; all character data was either 9-bit ASCII or 6-bit FIELDATA, and
anything originating from an external system was translated to one of
those two long before we got a chance to see it on the applications side
of life.  EBCDIC simply wasn't used.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-14T09:04:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd3li2$d8h$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com>`

```

"Richard Steiner" <rsteiner@visi.com> wrote in message
news:8YG9ApHpvWbF092yn@visi.com...

> We never dealt with EBCDIC directly in the 2200 systems that I've worked
> with; all character data was either 9-bit ASCII or 6-bit FIELDATA, and
> anything originating from an external system was translated to one of
> those two long before we got a chance to see it on the applications side
> of life.  EBCDIC simply wasn't used.

Well, that's part of my point.  Unisys MCP systems could handle EBCDIC and
ASCII with equanimity.  The machines it was targeted to replace were
primarily EBCDIC -- including Burroughs' own Small and Medium systems as
well as the Univac 90 series.  There was even a big project a good while
back to make the A Series attractive to (and perhaps even virtually
transparent to) IBM s/34/36/38 shops, with lots of changes to the RPG and
SORT compilers as well as a number of MCP changes to improve job initiation;
unfortunately this did not prove a commercial success.

The point here is that the Unisys MCP platform itself was deemed more
suitable, on technical grounds, to provide compatibility for a wider range
of other architectures than the Unisys OS2200 platform -- the efforts to
make the OS2200 platform more attractive as a near-plug-in substitute for
the user of, say, an Arbitrary Computer were deemed more costly than similar
efforts on the MCP platform.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 10)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-15T02:07:46-05:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<C1i9ApHpvWZf092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com>`

```
[Note: comp.sys.unisys added to the Newsgroups list in the hope of
 obtaining authoritative input with regard to the storage/manupulation
 of EBCDIC data on 2200 systems]

Here in comp.lang.cobol,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>"Richard Steiner" <rsteiner@visi.com> wrote in message
>news:8YG9ApHpvWbF092yn@visi.com...
…[8 more quoted lines elided]…
>and ASCII with equanimity.

I'm speaking outside my experience, since I've never worked with EBCDIC
data on a 2200 system, but it doesn't strike me as a difficult task to
create facilities on a 2200 to handle EBCDIC in an efficient manner.

If the 2200 could handle ASCII data (which is normally handled as 8-bit
bytes on other systems), another 8-bit code could surely be handled on
the 2200 using a similar mechanism.

That's why I suspect that one of the following is actually true:

 (1) Unisys 2200 systems could handle EBCDIC data in a graceful manner. 
 (2) There wasn't much actual demand for 2200's to handle EBCDIC data.

I guess both of the above could also be true.  :-)

I've crossposted this thread to comp.sys.unisys for additional comment.
The questions being posed are (roughly) as follows:

  How important was the presence or absence of EBCDIC compatibilty in
  the marketing of 1100/2200 systems?

  Did its importance change over time?

  Did A-series systems gain a marketing advantage when talking to IBM
  shops (for example) because they used EBCDIC natively?
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-15T09:32:56-07:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<cd6bjp$26o4$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com>`

```

"Richard Steiner" <rsteiner@visi.com> wrote in message
news:C1i9ApHpvWZf092yn@visi.com...

>   How important was the presence or absence of EBCDIC compatibilty in
>   the marketing of 1100/2200 systems?

Just to be sure I'm not misquoted or misinterpreted:  This seems to me to
misstate my point in a fairly significant way.  The *only* part of the
marketing of 1100/2200 systems I intended in any way to address was "the
development of new features in software and hardware for the 1100/2200
systems for the express purpose of attracting existing users from other
architecturally-different, competitive, obsolescent or obsolete systems
while providing an operating environment that would be familiar to users of
those systems."

If the average 1100/2200 user is expecting his files and his data to be in
FIELDATA or in ASCII, it's not a matter of being able to handle EBCDIC on
the 1100/2200, it's a matter of being able to make the 1100/2200 "act like"
its native character set is EBCDIC instead of ASCII or FIELDATA, to the
programmer and to the end user of the Arbitrary Target System.

The question doesn't seem to me to be about marketing as such, it's about
the cost (and cost effectiveness) of providing the software and software
changes that marketing feels would assist them in selling the machine to
existing users of another system.  That's a relatively minor subset of
"marketing", and has a whole lot more to do with "engineering" -- would it
be *easier* to provide a source-compatible System/36 RPG soup-to-nuts
(including sort control record formats) implementation under OS2200 or under
MCP?  How 'bout B1000 RPG?  Medium Systems DMS?  Enough compatible
infrastructure existed to provide these capabilities in the MCP environment;
I suspect strongly that doing the same in the OS2200 environment would have
required the development of significantly more infrastructure!

Personally, despite the fact that the standard collating sequence is EBCDIC
in our COBOLs I think that ASCII is more universal than EBCDIC, and people'd
better get used to UNICODE.  The issue here is that if you're trying to sell
management on the painlessness of migration from an EBCDIC environment
(including the examples of Univac 90, Burroughs Small and Medium Systems,
and the IBM small systems of the past) to Your Whizbang Machine, it's a lot
less painful migration if Your Whizbang Machine can say "I'm just as EBCDIC
as you".

The context I'm talking about is very limited; it's the *reengineering* of
the system, or of a part of the system, specifically to make it attractive
to a particular competitive market segment.

>   Did its importance change over time?

My guess is it's less today; UNICODE is becoming increasingly important, and
I think ASCII is more univerally accepted.  That doesn't help the user whose
current record ordering schemes are satisfactorily based on an EBCDIC
collating sequence, though!

>   Did A-series systems gain a marketing advantage when talking to IBM
>   shops (for example) because they used EBCDIC natively?

That wasn't a significant priority to the management types that marketers
talked to; it might have played a part in demonstrations of
ease-of-migration, however.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 12)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-16T19:10:44-05:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<E6G+ApHpv+aF092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <cd6bjp$26o4$1@si05.rsvl.unisys.com>`

```
Here in comp.sys.unisys,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>"Richard Steiner" <rsteiner@visi.com> wrote in message
>news:C1i9ApHpvWZf092yn@visi.com...
…[5 more quoted lines elided]…
>misstate my point in a fairly significant way.

Sorry, I obviously missed the direction you were heading.  :-(

Thanks for clarifying.  :-)
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 11)_

- **From:** andrew.williams@t-online.de (andrew williams)
- **Date:** 2004-07-15T10:07:09-07:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<995f2314.0407150907.4c34cf43@posting.google.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com>`

```
COBOL (both ACOB and UCOB) can handle EBCDIC tapes without any
problems.
AFAIK, there are no other circumstances where 2200 systems expect to
see EBCDIC.

For UCOB look at 7831 0455-011 (the newest version of UCS COBOL Volume
2) and check chapter 14 - 'Processing IBM Tapes'.
ACOB has it documented as well but since there is only one ACOB
Programmer's Reference, anyone who wants to can look it up in the
index.



rsteiner@visi.com (Richard Steiner) wrote in message news:<C1i9ApHpvWZf092yn@visi.com>...
> [Note: comp.sys.unisys added to the Newsgroups list in the hope of
>  obtaining authoritative input with regard to the storage/manupulation
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 11)_

- **From:** "Stephen Fuld" <s.fuld@PleaseRemove.att.net>
- **Date:** 2004-07-15T17:11:48+00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com>`

```

"Richard Steiner" <rsteiner@visi.com> wrote in message
news:C1i9ApHpvWZf092yn@visi.com...
> [Note: comp.sys.unisys added to the Newsgroups list in the hope of
>  obtaining authoritative input with regard to the storage/manupulation
…[8 more quoted lines elided]…
> >> We never dealt with EBCDIC directly in the 2200 systems that I've
worked
> >> with; all character data was either 9-bit ASCII or 6-bit FIELDATA, and
> >> anything originating from an external system was translated to one of
> >> those two long before we got a chance to see it on the applications
side
> >> of life.  EBCDIC simply wasn't used.
> >
…[22 more quoted lines elided]…
>   the marketing of 1100/2200 systems?

I can't speak to the whole market, but at a site I used to work at, the
ability to read tapes created on an IBM system, that is, in EBCDIC, with IBM
standard tape labels, was critical.  The ability to translate EBCDIC to then
fieldata, now ASCII is provided by the harware and we wrote local code to
handle the differences between IBM and ANSI standard labels.  I believe that
current products provide all of this natively. Once the data gets into the
system, there was no need to handle EBCDIC.  Its only advantage over ASCII
is some additional very odd and very infrequently used graphic characters,
which we happily did without.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-15T11:36:43-07:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<cd6irr$2eic$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net>`

```

"Stephen Fuld" <s.fuld@PleaseRemove.att.net> wrote in message
news:oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net...

> Once the data gets into the
> system, there was no need to handle EBCDIC.  Its only advantage over ASCII
> is some additional very odd and very infrequently used graphic characters,
> which we happily did without.

That's true if you've done a full-on conversion.  However, if your users,
and your applications, are used to numbers being higher in the collating
sequence than letters, you're not going to be able to take an existing
sort-report sequence expecting the data to be in EBCDIC order in the report
without *some* modifications!   If X contains "ABC" and Y contains "1BC",
whether the information is recorded in EBCDIC or ASCII can make a
significant difference to the application when that application asks "IF X
IS GREATER THAN Y ..." .   That applies not just to COBOL explicit
comparisons but to sorts and indexed-sequential key handling as well.

To a user used to running on System A that does its *processing* in EBCDIC,
that encoding indeed *does* offer a significant advantage over ASCII -- 
there is no need to rewrite the program to account for the differences
between the collating sequences of the two encodings so that the comparisons
are done correctly.

It is entirely reasonable that once you have read the System-A-generated
tape and translated it into ASCII on your System-B ASCII-based machine you
have no further need to know that the data was originally in EBCDIC,
particularly in programs that were and are native to that ASCII-based
machine.

But if you are attempting to read and manipulate that data using a
System-A-native program that has been "ported" to a System-B, it may require
a good deal of work on the application to get it to produce acceptable
results.  If the goal was to "port" the System-A program to System-B with
only automated changes, with minimum manual changes, or with no changes at
all, that goal may be a bit difficult to achieve if System-A "thinks" in
EBCDIC and System-B "thinks" in ASCII, particularly so if System-B is not
capable of "thinking" directly in EBCDIC.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 13)_

- **From:** "Stephen Fuld" <s.fuld@PleaseRemove.att.net>
- **Date:** 2004-07-16T04:16:21+00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<pEIJc.261880$Gx4.31402@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net> <cd6irr$2eic$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:cd6irr$2eic$1@si05.rsvl.unisys.com...
>
> "Stephen Fuld" <s.fuld@PleaseRemove.att.net> wrote in message
…[3 more quoted lines elided]…
> > system, there was no need to handle EBCDIC.  Its only advantage over
ASCII
> > is some additional very odd and very infrequently used graphic
characters,
> > which we happily did without.
>
…[3 more quoted lines elided]…
> sort-report sequence expecting the data to be in EBCDIC order in the
report
> without *some* modifications!

True.  But in our case, I guess it was a combination of only newly written
programs and people not really caring whether numbers collated higher or
lower than letters.

snip

> But if you are attempting to read and manipulate that data using a
> System-A-native program that has been "ported" to a System-B, it may
require
> a good deal of work on the application to get it to produce acceptable
> results.  If the goal was to "port" the System-A program to System-B with
…[3 more quoted lines elided]…
> capable of "thinking" directly in EBCDIC.

Having been involved in porting some programs from IBM COBOL to now totally
obsolete Univac COBOL (Fieldata COBOL, for those with sufficient gray hairs
to remember), the different character set was among the least of the
problems.  A truely automated conversion, much less a "no source code
changes" conversion was virtually impossible.  I suspect it is easier now,
but still probably difficult.  For one thing, both vendors have vendor
unique extensions to the standard and programmers tend to use them as they
don't generally plan on portability when writing COBOL.  Second, a pure
batch, non database program is somewhat of a rarity these days and the
conversion of say CICS into TIP dwarfs anything we have talked about so far.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 13)_

- **From:** "Colin Zealley" <colin.zealley@unisys.com>
- **Date:** 2004-07-16T22:11:25+01:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<cd9g9t$2foo$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net> <cd6irr$2eic$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:cd6irr$2eic$1@si05.rsvl.unisys.com...
>
> "Stephen Fuld" <s.fuld@PleaseRemove.att.net> wrote in message
> news:oVyJc.258907$Gx4.140491@bgtnsc04-news.ops.worldnet.att.net...
>
[snip]

> To a user used to running on System A that does its *processing* in
EBCDIC,
> that encoding indeed *does* offer a significant advantage over ASCII -- 
> there is no need to rewrite the program to account for the differences
> between the collating sequences of the two encodings so that the
comparisons
> are done correctly.

There is a COLLATING SEQUENCE clause (or something like that) in the
CONFIGURATION SECTION  of a COBOL program since 1974 standard. This will
allow you to make the program work in EBCDIC if you really want to.

The OS2200 compilers will also handle IBM COBOL pretty neatly in other ways;
for instance, they can handle COMP-3 data in those EBCDIC tapes correctly,
and there's a whole scud of other features to make porting IBM COBOL pretty
much a cinch ... as long as we were talking batch processing. As has already
been mentioned elsewhere in this thread, though, once you get to TP systems
any significant likelihood of simple conversion goes out of the window.

The only way I know to get more or less transparently off of an IBM
mainframe onto an ASCII-based encironment is via the Micro Focus (Merant)
toolkit, which offers what is to all intents and purposes a CICS-cmpatible
environment under Windows.

>
[snip]
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 11)_

- **From:** hans <jkkrutgers@wanadoo.nl>
- **Date:** 2004-07-19T23:46:52+02:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<40FC414C.8080702@wanadoo.nl>`
- **In-Reply-To:** `<C1i9ApHpvWZf092yn@visi.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com>`

```
Richard Steiner wrote:
> The questions being posed are (roughly) as follows:
> 
…[7 more quoted lines elided]…
> 

The 1100 system was designed to make this kind of details 
"transparant". Programmers should not have to care about it.

So any EBCDIC tape was converted by the tape unit hardware 
into ascii. The application wasn't aware of this.

To be able to handle EBCDIC was very imported for univac, in 
fact it was vital to be IBM compatible. Of course COBOl was 
essential here, so COBOl and all of its aspect as IBM tape 
handling were made compatible.

On the 1100 for an assembler programmer it doesn't matter 
whether it is ascii of fieldata , the internal calls could 
handle that for you.
And when writing to tape it was put back in EBCDIC by the 
hardware translator.

People will have little experience with it, because it was 
handled automatically and nobody had to care.


I have no idea if A series had an advantage over IBM in any 
aspect. Are you referring to s36 or s38 as400 ?

I can't believe that EBCDIC was important, marketing wise. 
So why do you ask??
regards
hans
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 12)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-19T18:41:46-05:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<10fon1t5blshn55@corp.supernews.com>`
- **In-Reply-To:** `<40FC414C.8080702@wanadoo.nl>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <40FC414C.8080702@wanadoo.nl>`

```
hans wrote:
> Richard Steiner wrote:
> 
…[15 more quoted lines elided]…
> The application wasn't aware of this.

A co-worker of mine said that they used to use the 1100 to do tape 
conversions for other organizations.  I forget the name of the product 
they use, but all you had to do was describe the format of the tape 
coming in, the format of the tape going out (or the disk file you wanted 
written), and it would do it flawlessly.

I wish I could remember the name of that product - it sounded cool.  Of 
course, it's been years and years since we've had to handle anything 
other than a Unisys tape.  :)
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 13)_

- **From:** Tim Cain <tcain+Usenet@unisys.com>
- **Date:** 2004-07-20T12:42:36+00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<Xns952C4E6E49926fooblaunisyscom@192.61.239.93>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <40FC414C.8080702@wanadoo.nl> <10fon1t5blshn55@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote in
news:10fon1t5blshn55@corp.supernews.com: 

> A co-worker of mine said that they used to use the 1100 to do tape
> conversions for other organizations.  I forget the name of the
…[8 more quoted lines elided]…
> 

Perhaps it was UCAP/FTS (File Transition Software)?  This product was 
supported out of the Eagan Marketing Support Center back in the early 
1980's (Sperry days...).  Its main purpose was to convert *any* other 
vendors tapes to "1100 ASCII".
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 14)_

- **From:** hans <jkkrutgers@wanadoo.nl>
- **Date:** 2004-07-21T23:52:18+02:00
- **Newsgroups:** comp.lang.cobol,comp.sys.unisys
- **Message-ID:** `<40FEE592.7010801@wanadoo.nl>`
- **In-Reply-To:** `<Xns952C4E6E49926fooblaunisyscom@192.61.239.93>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com> <NMt8ApHpvKOY092yn@visi.com> <ccutaq$7of$1@si05.rsvl.unisys.com> <MXw8ApHpvOgG092yn@visi.com> <cd1jdo$21ri$1@si05.rsvl.unisys.com> <8YG9ApHpvWbF092yn@visi.com> <cd3li2$d8h$1@si05.rsvl.unisys.com> <C1i9ApHpvWZf092yn@visi.com> <40FC414C.8080702@wanadoo.nl> <10fon1t5blshn55@corp.supernews.com> <Xns952C4E6E49926fooblaunisyscom@192.61.239.93>`

```
Tim Cain wrote:>
> 
> Perhaps it was UCAP/FTS (File Transition Software)?  This product was 
…[3 more quoted lines elided]…
> 

Ah, you do remember me of the day when I wrote a nice 
interactive tape reader program in @ASM.
I read Secure tapes, nobody wanted to use @Secure.
Their format was close to furpur format copy,g.

Coversion was very simple since the OS did everything,
it was just a matter of the right choice of options on the 
@ASG,options command.

I stil have a few interesting tapes, but where can I read 
them?????
One of them contains Colossal Cave and Space War (1975 
versions) Ah! those where the days.

thank you for the memory
hans
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-12T21:06:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10f6gtcqqqc994d@corp.supernews.com>`
- **In-Reply-To:** `<ccuhhl$31bt$1@si05.rsvl.unisys.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <l6zIc.152$mL5.148@newsread1.news.pas.earthlink.net> <ccuhhl$31bt$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> But I have to admit discouragement that contributors to comp.lang.cobol are
> so quick to dismiss the relevance not only of Unisys' (and Burroughs' and
…[5 more quoted lines elided]…
> presence worldwide, probably most prominently in the financial marketplace.

Of course, the 2200 side still releases MASM, and even has extended-mode 
support for it.  The subject line, for us anyway, is true - we've got a 
couple of pieces of MASM that are pretty important in our system.  (I'm 
sure Mr. Comstock's lesson plans don't include dealing with 36-bit 
words, though...  ;>  )
```

##### ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-07-12T17:09:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040712130958.25491.00001604@mb-m29.aol.com>`
- **References:** `<ccubh0$2t98$1@si05.rsvl.unisys.com>`

```
Chuck Stevens writes ...

>
>"S Comstock" <scomstock@aol.com> wrote in message
…[13 more quoted lines elided]…
>third-party development of, assemblers for the system.

Well, you're right, of course. As Bill Klein says, I'm pretty much a z/OS
applications guy, some knowledge about VM and VSE (long time since I worked on
it), and no knowledge about what some of us ex-IBM'ers call "brand x" [i.e.:
anything other than big blue iron]. 

So, that's my bias, what I was "raised with", and I know it is not the whole
world, and I recognize and even appreciate the presence of brand x stuff, and
your contributions, particularly, to this newsgroup have certainly been
appreciated, even by me.

Regarding Bill's comments about my COBOL classes: at one time I used to include
platform-specific information about every platform I could find docs on, but I
had no interest from customers in the non-IBM stuff (not surprising,
considering the circles I tend to hang around in, so it's sort of a
self-fullfilling prophecy). Last week another instructor was teaching one of my
COBOL debugging courses for an OS/390 customer and even the labs setups would
not run without extensive mods: they are a Librarian and Roscoe shop and my
setups are all written in TSO REXX / Dialog Manager. The point of all this is
that the reality is, even my pseudo-generic COBOL stuff really is designed for
the z/OS environment and a non-IBM user would quickly become aware of that and
feel at least somewhat out of synch.

Once upon a time, one could be a generalist in this field and keep track of it
all. That time is long since gone for me, although there are some people on
this list (and some other lists) who seem to have a pretty solid handle on a
wide range of platforms. All we can do is all we can do, and ya' gotta' keep
learning new stuff, and there is never enough time to learn it all anymore.

Kind regards,



-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2004-07-13T02:03:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GpHIc.61752$iJ4.20985@twister.nyroc.rr.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com>`

```
As an fyi for OS2200 systems - I think you'll find some assembler code on
many of those systems, particularly if they still run a lot of basic-mode
ACOB (COBOL 74) code. In the extended mode environment, Unisys has done a
much better job of removing the need for most assembler code. The manuals
even go so far as to say that user written extended-mode assembler code is
essentially unsupported (although it can be done of course). Many of the
previously common needs for assembler have native language CALL interfaces
and other bits can now be accomplished using UC and doing interlanguage
calls. One could argue that something like the UCSGENERAL$ interface to
basic mode ERs isn't much above assembler coding though. You still need to
get the ER manual and figure out what the register usages are, etc.

In my particular circumstance, I would say that in the ACOB arena we
probably had something between 30-40 assembler routines around. With UCOB, I
have had to create only one so far and that is a fairly esoteric situation
that is likely site-dependent. The others are now provided with UCOB or were
creatable using either UCOB or UC.

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:ccubh0$2t98$1@si05.rsvl.unisys.com...
>
> "S Comstock" <scomstock@aol.com> wrote in message
…[4 more quoted lines elided]…
> I think this statement might be a bit -- umm ... provincial.   It's true
so
> long as you summarily ignore any environment in which it's false, and
there
> are environments in which it is not only false today but has been false
for
> something over four decades.
>
…[3 more quoted lines elided]…
> compilers, and Unisys not only doesn't provide, but actively discourages
the
> third-party development of, assemblers for the system.
>
>     -Chuck Stevens
>
>
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

- **From:** ggray@gta.ga.gov (George Gray)
- **Date:** 2004-07-16T09:12:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4f51e4a.0407160812.32219469@posting.google.com>`
- **References:** `<20040707143232.11581.00001180@mb-m11.aol.com> <ccubh0$2t98$1@si05.rsvl.unisys.com> <GpHIc.61752$iJ4.20985@twister.nyroc.rr.com>`

```
I think that Stephen Fuld addressed most of the issues around
1100/2200 handling of EBDCIC, though with respect to Chuck's point
about collating sequence, 2200 COBOL has the facility (which we have
used here) to specify an alternate (such as EBCDIC) collating sequence
for sorting.

On the more historical issues:

(1) Sperry's preferred migration path for the large sites among former
RCA customers was to go to the 1100 Series.  Sperry built the attached
virtual processor (AVP) which plugged into an 1100 central complex as
a migration tool.  It could run the RCA instruction set and share
peripherals with the 1100 processor(s).  A good number of the big
sites did switch to the 1100, such as Westchester County. These
conversions took place in the early 1980s prior to the merger with
Burroughs. The smaller RCA sites and Sperry's own 9000 series
customers continued to use the OS/3 based machines until the early
1990s when the preferred migration path was to UNIX (hopefully the
Unisys U6000).

(2) Sperry did have a large number of medium and small 1100/2200
customers during the 1970s and 1980s.  Models such as the 1100/10, the
2200/200, and 2200/100 were targeted to these sites.  Another group of
small site customers was picked up with the advent of MAPPER in the
early 1980s.  However, these customers (both old-time and MAPPER) are
now mostly converted to non-Unisys Unix or Windows.  I just spoke with
a city utility in Missouri which is now on that path.  Some continue
to use MAPPER on other platforms. In general, the 1100/2200
programming development environment of the 1970s & 1980s was about as
user-friendly as any of the others in that era and considerably more
friendly than that of IBM.
```

###### ↳ ↳ ↳ Re: "Every Shop Has Some Assembler Somewhere" - course update

_(reply depth: 4)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-07-16T16:26:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040716122646.11526.00001326@mb-m23.aol.com>`
- **References:** `<c4f51e4a.0407160812.32219469@posting.google.com>`

```
Hey, Chuck,

For a thread that started out talking about IBM Assembler you got a lot of
Unisys mileage, eh?

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
