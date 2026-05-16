[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: (sort-of) Selecting a server

_2 messages · 2 participants · 1998-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Off-topic and spam`](../topics.md#spam)

---

### OT: (sort-of) Selecting a server

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70tg5d$59o@dfw-ixnews4.ix.netcom.com>`
- **References:** `<006501bdfd33$1f570d00$0300000a@atomsmasher.netin.com>`

```
I thought I might start an interesting "flame war" by passing on this post
from the IBM-MAIN listserver to my COBOL friends.

"Hi all,

this is not really an MVS question, but somebody might give me a hint.

If i compare OS/390, various UNIX (like the SUN E 10000) and Windows NT
Enterprise Edition (on big SMP machines)  for doing server type of
operation, what are the BIG pro's and con's of OS/390 ? What comes to
mind ?

Any ideas are welcome - please don't shoot me for the question; but i
need some high level answers to this from a big group of mainframers.

Ciao, B. Kunrath (calling from the wild south of germany)

Chris Craddock wrote in message
<006501bdfd33$1f570d00$0300000a@atomsmasher.netin.com>...
>This is a good question, but the answers will be mystifying to proponents
of
>Unix and/or NT for two reasons;
>
…[10 more quoted lines elided]…
>However, a big OS/390 box could be a 10 way IBM 9672, or a 12 way Amdahl,
or an
> 8 way HDS Skyline. Any of those puppies is (ballpark) 1000 mips, but then
you
> could couple up to 32 of them in a data sharing parallel sysplex without
> changing a line of application code.
>
>So, in comparison with SMP systems from other vendors, the main advantages
of
> OS/390 as a server platform are...
>
>1. Scalability. You can run exactly the same applications (and system
> software!!) on anything from a tiny 4 mips P/390 to a monster parallel
sysplex
> with roughly 30 thousand mips. In many cases you can add capacity without
> disrupting service.
>
>2. Reliability. In common usage it just doesn't break - at least not in the
ways
> that you are familiar with. There's no such thing as a kernel panic or the
> "blue screen of death".
>
>3. Security. Unlike any other platform. There are no security holes. There
are
> no "superusers". There are no viruses. Period.
>
>4. Availability. You can leave it up indefinitely. You don't have to take
it
> down to do housekeeping functions such as data backups. You never have to
take
> it down at all unless you are upgrading the operating system itself and
even
> then you can do it in a sysplex without disrupting service.
>
>5. Serviceability. The most robust diagnostics and corrective service
mechanisms
> on the planet. You can selectively apply program maintenance. The hardware
has
> its own builtin diagnostics and automatically calls the service center
> when its feeling ill. Often the first time you will know you have a
problem
>is when the CE walks in the door and tells you about it.
>
>6. Manageability. Much of the system's operation is completely automatic
and
>there are rich tools from IBM and other vendors to cover the areas that are
>not already covered by the operating system.
>
>7. Software. This is the platform that has the best database and
transaction
>processing software. In addition, it supports all of the communication
>protocols, it includes Unix functionality, Java, Web servers etc. Nothing
…[4 more quoted lines elided]…
>their promotional literature. They ALWAYS compare themselves with
"MAINFRAME
>CLASS" capabilities. These days, the prices are so competitive, the
>reasonable question to ask is "Why not buy the real thing?".
…[19 more quoted lines elided]…
>>
```

#### ↳ Re: OT: (sort-of) Selecting a server

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36356e04.1222136@nntp.ix.netcom.com>`
- **References:** `<006501bdfd33$1f570d00$0300000a@atomsmasher.netin.com> <70tg5d$59o@dfw-ixnews4.ix.netcom.com>`

```
On Sat, 24 Oct 1998 16:06:45 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>If i compare OS/390, various UNIX (like the SUN E 10000) and Windows NT
>Enterprise Edition (on big SMP machines)  for doing server type of
>operation, what are the BIG pro's and con's of OS/390 ? What comes to
>mind ?

hmm. i don't know enough about unix, but i know as400 has a few neat
things that windows 3.11 doesn't have. multiple armature usage, disk
mirroring, built-in database. also, as400 and its security is made so
that you don't need multiple passwords. PCs on the other hand, have a
security feature for bootup in the bios, one in the OS, and a key on
top of that.


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
