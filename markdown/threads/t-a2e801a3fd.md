[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Simple? DISPLAY Question

_7 messages · 4 participants · 2006-06 → 2006-07_

---

### Simple? DISPLAY Question

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2006-06-29T11:06:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com>`

```
PLATFORM: HP-UX 11i
COMPILER: MF SE 4.0 SP2

First off - I can assure you all this is NOT a homework question. LOL

I know this will be a simple question for the experienced folks in this
group, but its been a long time since I've done this without simply
making use of the screen section. However, I've inherited some older
code that I've been asked to modify.

Given this code snip:

           DISPLAY

             SPACES
               AT    LINE 01  COL 01
               WITH  FOREGROUND-COLOR 4

             "Line 1"
               AT    LINE 01  COL 01
               WITH  FOREGROUND-COLOR 4

             "Line 2"
               AT    LINE 02  COL 01
               WITH  FOREGROUND-COLOR 4

           END-DISPLAY.

Isn't there a way to simplify this so that the foreground and/or
background color is specified only once? I was under the impression
(based on what I have read in the documentation) that if you simply
specified the colors with the "SPACES AT LINE 01 COL 01" that those
colors would become the default, but that is NOT happening in practice.
When I remove the WITH clause from the second two display items they go
back to whatever the original default was (in my case white fg on black
bg).

I'm looking for something like this (knowing FULL WELL that the
following syntax will/does not work):

           DISPLAY

             SPACES
               AT      LINE 01  COL 01

             "Line 1"
               AT  LINE 01  COL 01

             "Line 2"
               AT  LINE 02  COL 01

             ALL WITH FOREGROUND-COLOR 4

           END-DISPLAY.


Any ideas?

Thanks in advance,
Chris
```

#### ↳ Re: Simple? DISPLAY Question

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-06-29T15:12:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12a89klbm9dac4c@corp.supernews.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com>`

```

"Chris" <ctaliercio@yahoo.com> wrote in message
news:1151604386.498873.187800@y41g2000cwy.googlegroups.com...
> PLATFORM: HP-UX 11i
> COMPILER: MF SE 4.0 SP2
[snip]
> Isn't there a way to simplify this so that the foreground and/or
> background color is specified only once? I was under the impression
…[5 more quoted lines elided]…
> bg).

This works with Micro Focus COBOL 3.2.24 for MS-DOS
and displays red on white.

           display space at 0101 with
               foreground-color 4
               background-color 15
               blank screen
             "Line 1" at 0101
             "Line 2" at 0201

It is the use of BLANK SCREEN with FOREGROUND-COLOR
or BACKGROUND-COLOR that sets the default colors for each,
according to the LRM.
```

##### ↳ ↳ Re: Simple? DISPLAY Question

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2006-06-29T12:27:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151609269.962405.245380@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<12a89klbm9dac4c@corp.supernews.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com> <12a89klbm9dac4c@corp.supernews.com>`

```
Rick,

I agree with you - this is how I thought it was supposed to work
myself.

Unfortunately it doesn't work on my system.

I still get the entire screen displayed with the specified colors, but
the subsequent items following the spaces go back to the previous
default (white on black).

With or without the BLANK SCREEN clause I get the same behavior.

Thanks,
Chris




Rick Smith wrote:
> "Chris" <ctaliercio@yahoo.com> wrote in message
> news:1151604386.498873.187800@y41g2000cwy.googlegroups.com...
…[24 more quoted lines elided]…
> according to the LRM.
```

###### ↳ ↳ ↳ Re: Simple? DISPLAY Question

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-29T20:01:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qkWog.108087$Mn5.91944@pd7tw3no>`
- **In-Reply-To:** `<1151609269.962405.245380@i40g2000cwc.googlegroups.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com> <12a89klbm9dac4c@corp.supernews.com> <1151609269.962405.245380@i40g2000cwc.googlegroups.com>`

```
Chris wrote:
> Rick,
> 
…[14 more quoted lines elided]…
> 
Well Chris, if you believe you have got it right - time to ask M/F - 
check-in at the Forum under SE for clarification.

Jimmy
```

###### ↳ ↳ ↳ Re: Simple? DISPLAY Question

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-06-29T15:33:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151620417.678146.99410@p79g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<1151609269.962405.245380@i40g2000cwc.googlegroups.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com> <12a89klbm9dac4c@corp.supernews.com> <1151609269.962405.245380@i40g2000cwc.googlegroups.com>`

```

Chris wrote:

> Unfortunately it doesn't work on my system.

I found that a lot when I was doing stuff that would run on various
systems.  Just because it work on an IBM PC with DOS does not mean that
it will run the same everywhere. A couple of decades ago I built some
routines that do work on several systems, in fact it is still running
on a few sites, only one still using DOS, the rest on Linux though it
will still work on others.

You can do several display items at one time by displaying an 01 level
in which there are named fields which will display and fillers which
won't:

          01  Line-Bits.
                03  Line01         PIC X(6)   VALUE "Line 1".
                03  FILLER        PIC X(74).
                03  Line02        PIC X(6)  VALUE "Line 2".

                DISPLAY Line-Bits AT 0101  .... colors etc ...

will put 'Line 1' at 0101 and 'Line 2' at 0201 and not change anything
else on the screen, ie it will leave the rest of line 01 as it is.
```

#### ↳ Re: Simple? DISPLAY Question

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-06-29T15:40:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151620825.489434.65770@d56g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com>`

```

Chris wrote:

> specified the colors with the "SPACES AT LINE 01 COL 01" that those
> colors would become the default, but that is NOT happening in practice.

You may need to lookup the ADIS calls which should have a function to
change the default colours and also do some neat things such as forcing
upper case on input.

In fact, checking my ancient routines for DOS terminals reveals that I
use CALL x"A7" with function 16 for setting default colours.
```

#### ↳ Re: Simple? DISPLAY Question

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2006-07-05T11:45:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152125109.197876.287470@m73g2000cwd.googlegroups.com>`
- **References:** `<1151604386.498873.187800@y41g2000cwy.googlegroups.com>`

```
As usual, Jimmy was right on the mark.

I took the issue to MF, and here is their tech's response:

---

I have raised a bug report for this issue as the docs clearly state the
following:

If the FOREGROUND-COLOR option is specified, then the specified color
becomes the default foreground color if and only if the entire screen
is cleared by this display. The entire screen is cleared either when
the BLANK SCREEN option is specified or when literal-1 is SPACES and
the DISPLAY starts at line 1 column 1.

In this case the default foreground color should be changed...

I have tried it under Windows under NetExpress and it works as
documented.

I will let you know as soon as I hear anything.

---

It's good to know that I am not losing my marbles - I'll post again
when MF offers a resolution.

Thanks for the feedback!

Chris


Chris wrote:
> PLATFORM: HP-UX 11i
> COMPILER: MF SE 4.0 SP2
…[57 more quoted lines elided]…
> Chris
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
