[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 132 column display

_9 messages · 7 participants · 1996-08_

---

### 132 column display

- **From:** "pat lynch" <ua-author-4340081@usenetarchives.gap>
- **Date:** 1996-08-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<320C146A.3829@mail.cis.ufl.edu>`

```

Does anyone out there know how to change a pc monitor's display from 80
column mode to 132 column mode. I am sending COBOL reports to the screen
and have some that require 132 columns. I am interested in changing the
mode right before the report is output and then returning to the 80
column mode after the report is complete.

Any suggestions or information leading to the solution means you are a
swell person.
```

#### ↳ Re: 132 column display

- **From:** "richard smith" <ua-author-515531@usenetarchives.gap>
- **Date:** 1996-08-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<320C146A.3829@mail.cis.ufl.edu>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu>`

```

Pat Lynch wrote:
› 
› Does anyone out there know how to change a pc monitor's display from 80
…[6 more quoted lines elided]…
› swell person.

I believe you can get a 132 column display using an XGA display.
Regards,
Richard
r.··.@mfl··o.uk
```

#### ↳ Re: 132 column display

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-08-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<320C146A.3829@mail.cis.ufl.edu>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu>`

```

Pat Lynch wrote:
› 
› Does anyone out there know how to change a pc monitor's display from 80
…[6 more quoted lines elided]…
› swell person.

Possibly of no great use to you (but someone might be thinking of doing the
same thing, so I'll say it anyway) is the facility on Unix versions of Micro
Focus COBOL of doing this using the "cobterminfo" call. It`s supposed to be
called from C, but of course, as Micro Focus COBOL allows you to call any C
function easily, that`s not a problem.
You need a terminfo entry for your terminal type with a "-w" suffix, I believe,
in order for this to work.

Cheers,
Kev.
```

##### ↳ ↳ Re: 132 column display

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-08-09T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf84dc6b1e-p3@usenetarchives.gap>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu> <gap-bf84dc6b1e-p3@usenetarchives.gap>`

```

Kevin Digweed, in a moment of blind panic, wrote:
›
› Possibly of no great use to you (but someone might be thinking of doing the
› same thing, so I'll say it anyway) is the facility on Unix versions of Micro
› Focus COBOL of doing this using the "cobterminfo" call.

Duh! I meant the "cobtermmode" call. There is no "cobterminfo" call.

Apologies,
Kev.
```

#### ↳ Re: 132 column display

- **From:** "jaime rezola clemente" <ua-author-6589443@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<320C146A.3829@mail.cis.ufl.edu>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu>`

```

Pat Lynch wrote:
› Does anyone out there know how to change a pc monitor's display from 80 
› column mode to 132 column mode.  I am sending COBOL reports to the screen 
…[5 more quoted lines elided]…
› swell person.

This is just a suggestion, I do not know if it is possible.

There probably is a escape sequence to change 80 to 132 column mode for
a PC monitor if you loaded ANSI.SYS at start-up.

I am not sure of that, I do not have the table for ANSI codes and I do
not know how to do that from COBOL. Anyway, I hope it can be an useful
lead.
```

##### ↳ ↳ Re: 132 column display

- **From:** "james s. huggins" <ua-author-6588675@usenetarchives.gap>
- **Date:** 1996-08-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf84dc6b1e-p5@usenetarchives.gap>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu> <gap-bf84dc6b1e-p5@usenetarchives.gap>`

```

if you are talking about a dos terminal, you are out of luck. 25 lines
by 80 characters.

if you are talking about a dos session in windows, you are out of luck.
80 characters max.

if you are talking about windows, it is different completely.
```

###### ↳ ↳ ↳ Re: 132 column display

- **From:** "gber..." <ua-author-8474860@usenetarchives.gap>
- **Date:** 1996-08-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf84dc6b1e-p6@usenetarchives.gap>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu> <gap-bf84dc6b1e-p5@usenetarchives.gap> <gap-bf84dc6b1e-p6@usenetarchives.gap>`

```

In <321··.@com··c.com>, "James S. Huggins" writes:
› if you are talking about a dos terminal, you are out of luck. 25 lines
› by 80 characters.
Not necessarily. Some emulators read the current "mode" settings
and adjust accordingly. The mode can be set (depending on the VGA
adapter) via the DOS MODE command. Most VGA cards come with utilities
for setting the various supported VGA modes.
There is a free utility that comes with the VPIC shareware package
called WHICHVGA. It will tell you what VGA chipset you have (or
freeze your system). Then get the utility from the appropriate
manufacturer.
But first try: MODE CO132 or MODE CO132,43 or some other combination.
If the DOS screen gets messed up, restore it to 80 collumns via MODE CO80

The OS/2 MODE command seems to work well for the few systems I've seen.


Regards,
Gary
Advanced Debugging System for CICS
CICS Tips & Tricks at: http://www.castle.net/~gbergman
```

#### ↳ Re: 132 column display

- **From:** "bke..." <ua-author-7426165@usenetarchives.gap>
- **Date:** 1996-08-16T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p8@usenetarchives.gap>`
- **In-Reply-To:** `<320C146A.3829@mail.cis.ufl.edu>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu>`

```

› Pat Lynch  wrote:
 
›› Does anyone out there know how to change a pc monitor's display from 80 
›› column mode to 132 column mode.  I am sending COBOL reports to the screen 
›› and have some that require 132 columns.  I am interested in changing the 
›› mode right before the report is output and then returning to the 80 
›› column mode after the report is complete.
 
›› Any suggestions or information leading to the solution means you are a 
›› swell person.

With a PC, the ability to switch to 132 column display normaly rests
with your dispaly adaptor. The software utilities supplied with the
card normally include a way to set the display to 132 column mode.
```

#### ↳ Re: 132 column display

- **From:** "bke..." <ua-author-7426165@usenetarchives.gap>
- **Date:** 1996-08-16T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf84dc6b1e-p9@usenetarchives.gap>`
- **In-Reply-To:** `<320C146A.3829@mail.cis.ufl.edu>`
- **References:** `<320C146A.3829@mail.cis.ufl.edu>`

```

› Pat Lynch  wrote:
 
›› Does anyone out there know how to change a pc monitor's display from 80 
›› column mode to 132 column mode.  I am sending COBOL reports to the screen 
›› and have some that require 132 columns.  I am interested in changing the 
›› mode right before the report is output and then returning to the 80 
›› column mode after the report is complete.
 
›› Any suggestions or information leading to the solution means you are a 
›› swell person.

With a PC, the ability to switch to 132 column display normaly rests
with your dispaly adaptor. The software utilities supplied with the
card normally include a way to set the display to 132 column mode.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
