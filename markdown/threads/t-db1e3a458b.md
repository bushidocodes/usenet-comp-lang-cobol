[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hasp problem

_8 messages · 6 participants · 1999-12_

---

### Hasp problem

- **From:** "Yiannis Patrikiadis" <yiannis@arion.gr>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84agvo$8l6$1@newssrv.otenet.gr>`

```
I do have a damaged hasp that is not making the Cobol run properly. Early
version 3.1.41. What should I do to make it work again? any Idea?
```

#### ↳ Re: Hasp problem

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OmlLh9XU$GA.284@cpmsnbbsa03>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr>`

```
HASP stands for Houston Automatic Spooling Program (or something close to
that).  It is the predecessor to IBM's MVS component JES2 (Job Entry
Subsystem2).  HASP has not been the official name of the JES2 product for
something like 30 years.  How old is the machine you're running?

And if we are talking about JES2 being somehow damaged or corrupted, that's
a red, white, and blue warning signal to contact both your site's sysprogs
immediately (and they may soon be on the line to IBM technical support).

If we're not talking about JES2 being damaged or corrupted, then I also
can't see how it would specifically prevent COBOL from working without
affecting anything else.  JES2 is such a major component of MVS that if
anything happened to it, the Console Operators would be on the line to their
sysprogs right away.  Something as innocent as typing "$P" at the system
console would pretty much lock the mainframe in short order (depending on
overall system load), and that command does nothing more than tell JES2 to
stop accepting new work.

Please, can you more clearly explain your problem?  Please post the sysout
of the error messages (or extract of the syslog or SMF records).


Yiannis Patrikiadis <yiannis@arion.gr> wrote in message
news:84agvo$8l6$1@newssrv.otenet.gr...
> I do have a damaged hasp that is not making the Cobol run properly. Early
> version 3.1.41. What should I do to make it work again? any Idea?
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Hasp problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84bgl0$o2e$1@nntp9.atl.mindspring.net>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03>`

```
Chris,
 I am glad you asked for "clarification".  I remember "HASP" (in long unused
brain-storage) - but I was trying to figure out what was meant by "Cobol ...
Early version 3.1.41".  I can't think of any IBM mainframe COBOL with that
release number.  Perhaps this is some totally OTHER meaning of "HASP" - but
we do need to know what the poster means by both "HASP" and the COBOL release
in question.
```

###### ↳ ↳ ↳ Re: Hasp problem

- **From:** francois millet <francois.millet@dial.oleane.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VA.0000007b.004b4454@francoim>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03> <84bgl0$o2e$1@nntp9.atl.mindspring.net>`

```
In article <84bgl0$o2e$1@nntp9.atl.mindspring.net>, William M. Klein wrote:
> From: "William M. Klein" <wmklein@nospam.netcom.com>
> Newsgroups: comp.lang.cobol
…[9 more quoted lines elided]…
> in question.

 I also remember HASP (used it in 1972...).
 
 But the HASP was also the name of a dongle (made by Aladdin?) distributed by 
Microfocus in some european countries, where their Cobol was protected. I think 
they now use Rainbow dongles.
 
> --
> Bill Klein
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Hasp problem

_(reply depth: 4)_

- **From:** joarmc@linux2.johnmckown.net (John McKown)
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn86lhdr.8c2.joarmc@linux2.johnmckown.net>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03> <84bgl0$o2e$1@nntp9.atl.mindspring.net> <VA.0000007b.004b4454@francoim>`

```

On Wed, 29 Dec 1999 06:38:06 +0100, francois millet
<francois.millet@dial.oleane.com> wrote:

<big snip>
Wow, a bunch of old mainframers (myself included). In this particular "HASP"
is a copy protection device which attaches to a PC's printer port. I believe
this person is saying that he bought a PC COBOL compiler which uses this
device (aka "dongle"). I have NO idea how to replace one of these things.

John McKown
```

###### ↳ ↳ ↳ Re: Hasp problem

_(reply depth: 4)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#CJy18jU$GA.323@cpmsnbbsa03>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03> <84bgl0$o2e$1@nntp9.atl.mindspring.net> <VA.0000007b.004b4454@francoim>`

```
francois millet <francois.millet@dial.oleane.com> wrote in message
news:VA.0000007b.004b4454@francoim...
> In article <84bgl0$o2e$1@nntp9.atl.mindspring.net>, William M. Klein
wrote:
> > From: "William M. Klein" <wmklein@nospam.netcom.com>
> > Newsgroups: comp.lang.cobol
…[4 more quoted lines elided]…
> >  I am glad you asked for "clarification".  I remember "HASP" (in long
unused
> > brain-storage) - but I was trying to figure out what was meant by "Cobol
...
> > Early version 3.1.41".  I can't think of any IBM mainframe COBOL with
that
> > release number.  Perhaps this is some totally OTHER meaning of "HASP" -
but
> > we do need to know what the poster means by both "HASP" and the COBOL
release
> > in question.
>
>  I also remember HASP (used it in 1972...).
>
>  But the HASP was also the name of a dongle (made by Aladdin?) distributed
by
> Microfocus in some european countries, where their Cobol was protected. I
think
> they now use Rainbow dongles.

  This may be it.  It fits the original poster's statement of "damaged" and
the use of HASP in small case, as if it weren't an acronym.
```

###### ↳ ↳ ↳ Re: Hasp problem

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84emo5$gf6$1@nntp3.atl.mindspring.net>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03> <84bgl0$o2e$1@nntp9.atl.mindspring.net> <VA.0000007b.004b4454@francoim> <#CJy18jU$GA.323@cpmsnbbsa03>`

```
I have received private email from the original poster - and they were
talking about Micro Focus COBOL and its (now unsupported) dongle.  I referred
them to MERANT - but indicated that I didn't think they would be able to help
much with this problem.
```

##### ↳ ↳ Re: Hasp problem

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sZda4.1083$wd2.30345@dfiatx1-snr1.gtei.net>`
- **References:** `<84agvo$8l6$1@newssrv.otenet.gr> <OmlLh9XU$GA.284@cpmsnbbsa03>`

```
You might also want to post your problem over at www.mvshelp.com in the JCL
section.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
