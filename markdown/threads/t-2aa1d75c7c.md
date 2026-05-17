[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accucobol notes

_3 messages · 3 participants · 1996-07_

---

### Accucobol notes

- **From:** "ferr..." <ua-author-17086290@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ra0n0$gm@star.epix.net>`

```

1. Could someone supply a telephone number in
the US for Accucobol (sp?)...


2. I have an application developed with RM/COBOL 85
under SCO UNIX that will be moved to Acucobol under
UNIX (not SCO, but some other x86-unix). Having
just completed moving the same application from RM
to MicroFocus (under MSDOS), I am concerned about
differences in ACCEPT/DISPLAY handling. MF handled
this by allowing me to set up my preferences in their
ADISCTRL file.

How does Acucobol allow me to set ACCEPT/DISPLAY
action to mimick Ryan/McFarland?

How does Acucobol set screen foreground/background
colors? Can this syntax be mixed with other RM-style
statements in the same program?

This became a problem
for me with the MF-conversion, because the RM-compatible
mode for the MF compiler does not appear to accept any
type of screen color statements.

I eventually moved the color-set statements to a separate
program, which used only MF syntax. That program was
compiled separately, but then linked with the RM-compatible
code.

Any comments will be appreciated.

don
```

#### ↳ Re: Accucobol notes

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-07-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2aa1d75c7c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4ra0n0$gm@star.epix.net>`
- **References:** `<4ra0n0$gm@star.epix.net>`

```

fer··.@ep··x.net (don ferrario) wrote:
› This became a problem
› for me with the MF-conversion, because the RM-compatible
…[6 more quoted lines elided]…
› code.

Hi. Can you give an example of the colour statements that were not working ?
Cheers, Kev.

PS. I believe ACU`s address is in the c.l.cobol FAQ.
PPS. Given that you`ve already converted to MF once, is there a reason why
you can`t just use MF on the new platform rather than putting in even
more development time ?
```

#### ↳ Re: Accucobol notes

- **From:** "jland..." <ua-author-4999378@usenetarchives.gap>
- **Date:** 1996-07-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2aa1d75c7c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4ra0n0$gm@star.epix.net>`
- **References:** `<4ra0n0$gm@star.epix.net>`

```

Dear Don:
You found the right person, First take note of Acucobol phone:
1-800-262-6585.
I was a RM/COBOL/85 developer for years under MS-DOS and SCO XENIX, but
later I switch to Acucobol/85. I just recompiled the RM source code in
Acucobol using the option -Cr (RM/COBOL compatibility mode) and thats it !
you are on the road !

Another good features in Acucobol is the use of split alternate keys, and
by the way Acucobol/85 data files don't get corrupted so easy as in
RM/cobol.

But if you really want to be admired as a programmer and be more
productive, stop using native ACCEPT, DISPLAY statements either in RM or
ACUCOBOL, instead get a good screen interface like COBOL SPII from flexus
(WWW.FLEXUS.COM), I've been using it for 5 years, it is portable across
many compilers and operating systems, Dos, Unix, VMS, Etc. so the same
screen design and functions made in RM/COBOL will work with no changes in
ACUCOBOL, in fact I converted a RM application that had COBOL SPII as
screen interface to ACUCOBOL-85 with only a few or no changes at all.

Good luck ! JAIME
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
