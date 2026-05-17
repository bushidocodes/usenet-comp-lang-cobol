[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# JCL

_6 messages · 6 participants · 1996-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### JCL

- **From:** "umbergb1" <ua-author-17086715@usenetarchives.gap>
- **Date:** 1996-09-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32489A54.36C4@fast.net>`

```

I am a CIS senior in a continuing education program. I interviewed and
found out I need some JCL knowledge. Can anyone recommend some material
and is there anything good online?

Please help,
Bill U
```

#### ↳ Re: JCL

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-09-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b1d1efb126-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32489A54.36C4@fast.net>`
- **References:** `<32489A54.36C4@fast.net>`

```

Since you mention JCL, I must assume that your target environment is an
IBM MVS mainframe environment.

One can get the MVS JCL guide and reference manuals. Very dry, but
contain the bottom line.

A better alternative is to get a copy of the ... Programmers Guide ...
manual for OS/VS COBOL, VS COBOL II, COBOL/370, or COBOL for MVS and VM
for the combination of COBOL technology and target environment.

These books typically complement the basic JCL information as it relates
to COBOL. Details are then found in the MVS books.

All of these books can be found on a set of CD's, SK2T0710.

These CD's are issued 4 times per year at $100 per set, containing 3000 or
more books. A few pennies per book, complete with a book reader for OS/2,
Dos and Windoze.

Back levels of the CD's can usually be mooched or found cheap. I saw a 6
month old set for $10 or $15 at the Dayton Hamvention back in may.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: JCL

- **From:** "soft..." <ua-author-6881452@usenetarchives.gap>
- **Date:** 1996-09-26T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b1d1efb126-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32489A54.36C4@fast.net>`
- **References:** `<32489A54.36C4@fast.net>`

```

Umbergb1 (umb··.@fa··t.net) wrote:
: I am a CIS senior in a continuing education program. I interviewed and
: found out I need some JCL knowledge. Can anyone recommend some material
: and is there anything good online?

I've never seen any good information on JCL anywhere -- it seems to be
something passed down from programmer to programmer. I think there
was one JCL file written a long time ago, and every other one since
then has been a modification of it. The syntax is utterly baffling,
and this is coming from someone who knows regular expressions!

Anyone want to prove me wrong and post some sources for info?

On the other hand, if I wrote a book like MVS For Dummies, would anyone
buy it? I wished I'd had it when I was thrown into the mainframe
world.

Scott
```

##### ↳ ↳ Re: JCL

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-09-26T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b1d1efb126-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b1d1efb126-p3@usenetarchives.gap>`
- **References:** `<32489A54.36C4@fast.net> <gap-b1d1efb126-p3@usenetarchives.gap>`

```

sof··.@mer··h.com (Scott McMahan - Softbase Systems)
wrote:

› I've never seen any good information on JCL anywhere -- it seems to be
› something passed down from programmer to programmer.
 
› Anyone want to prove me wrong and post some sources for info?

I take it you haven't looked at the library. There have been many
books written on the subject of JCL or Job Control Language. Work on
looking at your local well-stocked library for either of those two
subjects.
```

##### ↳ ↳ Re: JCL

- **From:** "dl..." <ua-author-12492979@usenetarchives.gap>
- **Date:** 1996-09-26T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b1d1efb126-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b1d1efb126-p3@usenetarchives.gap>`
- **References:** `<32489A54.36C4@fast.net> <gap-b1d1efb126-p3@usenetarchives.gap>`

```

Scott McMahan - Softbase Systems (sof··.@mer··h.com) wrote:
:...
: On the other hand, if I wrote a book like MVS For Dummies, would anyone
: buy it? I wished I'd had it when I was thrown into the mainframe
: world.

Well it does help show how far we've come ... I mean it use to be that you
had to spend 20 mins in a 5 inch thick book to determine the solution to
your problem was "Programmer error fix and resubmit" ... now we can get a
bright dialog box telling us that our system is corrupt and asking if it's
ok to reboot (like we have a choice) ...

;-)
```

##### ↳ ↳ Re: JCL

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b1d1efb126-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b1d1efb126-p3@usenetarchives.gap>`
- **References:** `<32489A54.36C4@fast.net> <gap-b1d1efb126-p3@usenetarchives.gap>`

```

sof··.@mer··h.com (Scott McMahan - Softbase Systems)
wrote:

› Umbergb1 (umb··.@fa··t.net) wrote:
› : I am a CIS senior in a continuing education program.  I interviewed and
› : found out I need some JCL knowledge.  Can anyone recommend some material
› : and is there anything good online?
 
› I've never seen any good information on JCL anywhere -- it seems to be
› something passed down from programmer to programmer. I think there
› was one JCL file written a long time ago, and every other one since
› then has been a modification of it. The syntax is utterly baffling,
› and this is coming from someone who knows regular expressions!
 
› Anyone want to prove me wrong and post some sources for info?
 
› On the other hand, if I wrote a book like MVS For Dummies, would anyone
› buy it? I wished I'd had it when I was thrown into the mainframe
› world.

Scott,

The best book for JCL is SYSTEM 390 Job Control Language, by Gary
DeWard Brown.

I bought the book back when it was known as SYSTEM 370 Job Control
Language, by Gary DeWard Brown. It's all taped up now to keep from
falling apart, and my name is written all over it, so no one will
steal it!

I don't think much has changed between the 370 and 390 versions. JCL
sucks, pure and simple.

The best way I can describe the syntax is reverse polish notation:
"If value X is greater than condition code, do NOT execute"

And that's the simplest example. Try figuring out the multiple
conditions. Best way to know for sure is test, test, test.

Tim Oxler




TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/â€¾troxler
http://users.aol.com/TEOcorp
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
