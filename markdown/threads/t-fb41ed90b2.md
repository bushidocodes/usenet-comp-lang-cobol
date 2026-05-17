[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ? Very weird MF problem

_3 messages · 1 participant · 1995-07_

---

### ? Very weird MF problem

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3v41da$ep5@news0.cybernetics.net>`

```
Here's a strange on (using MF COBOL v 3.2 under AIX 3.2.5)

-----
program-id. buggy.

01 str1 pic x(79).
01 odl.
05 filler pic x(11) value " ordered:".
05 odl-ordered pic zzzzz9 value 12.

procedure division.
display odl at line 3 column 1

move odl to str1
display str1 at line 5 column 1
.
-----
Output:


12

ordered: 12

-----

Anyone else having this problem, or know the cause?
```

#### ↳ Re: ? Very weird MF problem

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb41ed90b2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3v41da$ep5@news0.cybernetics.net>`
- **References:** `<3v41da$ep5@news0.cybernetics.net>`

```
Greg Granger (ggr··.@cyb··s.net) wrote:
Here is a reply sent to me by a very kind MF person.

:From k.··.@mfl··o.uk Wed Jul 26 08:21:39 1995
:Date: Wed, 26 Jul 1995 13:23:55 +0100
:From: Kev Digweed
:To: ggr··.@cyb··s.net (Greg Granger)
:Subject: Re: ? Very weird MF problem
:
:Sorry, I'm having difficulty posting at the moment so I'll answer this directly
:(feel free to post this answer for me - thanks).
:
:In article <3v41da$e.··.@new··s.net>, you write:
:> Here's a strange on (using MF COBOL v 3.2 under AIX 3.2.5)
:>
:> -----
:> program-id. buggy.
:>
:> 01 str1 pic x(79).
:> 01 odl.
:> 05 filler pic x(11) value " ordered:".
:> 05 odl-ordered pic zzzzz9 value 12.
:>
:> procedure division.
:> display odl at line 3 column 1
:>
:> move odl to str1
:> display str1 at line 5 column 1
:> .
:> -----
:> Output:
:>
:>
:> 12
:>
:> ordered: 12
:>
:> -----
:>
:> Anyone else having this problem, or know the cause?
:
:Quoting from the Language Reference Manual (Issue 13/April 1993) Chapter 4
:(Program Definition), PROCEDURE DIVISION Section, The DISPLAY Statement
:(p 4-343).
:
:Format 3.
:18. If is a group item, and no MODE IS BLOCK phrase exists,
: those elementary items which have names other than FILLER are displayed.
: [....]
:
:It has always been this way, as far as I can remember (the old forms2 screen
:painter used it, as I recall).
:
:Cheers,
:Kev.
:
:--
:Kevin. Micro Focus, Newbury, UK. (k.··.@mfl··o.uk)
:These views are strictly my own.
:I doubt very much that anyone else would want them.
```

#### ↳ Re: ? Very weird MF problem

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fb41ed90b2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3v41da$ep5@news0.cybernetics.net>`
- **References:** `<3v41da$ep5@news0.cybernetics.net>`

```
Eric Raskin (lis··.@clo··9.net) wrote:
: On 26 Jul 1995, Greg Granger wrote:

: > Here's a strange on (using MF COBOL v 3.2 under AIX 3.2.5)
: > ...
: > 01 odl.
: > 05 filler pic x(11) value " ordered:".
: > 05 odl-ordered pic zzzzz9 value 12.
: >
: > procedure division.
: > display odl at line 3 column 1

: It's not a bug -- it's a feature :-). According to the Display Statement
: manual pages, this is a Format 3 Display Statement. Paragraph 18 (in my
: manual) in the General Rules section states:

: 18. If identifier-1 is a group item and no MODE IS BLOCK phrase
: exists, those elementary subordinate items which have names
: other than FILLER are displayed.....

Yes, thanks, I just figured out why it was done this way and it REALLY IS
A FEATURE! Very handy for putting up a 'template' screen then using
displays to just update the named fields ... nice.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
