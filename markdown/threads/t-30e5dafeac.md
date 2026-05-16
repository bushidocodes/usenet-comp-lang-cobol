[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# b-color & f-color in Fujitsu

_7 messages · 5 participants · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### b-color & f-color in Fujitsu

- **From:** "GARWIG Ruddy" <ruddy.garwig@skynet.be>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78emq3$mdc$1@news0.skynet.be>`

```
In the screen-section, I use a variable (b-color) after the instruction
background-color and foreground-color.
This variable (b-color) is declared pic S9(4) binary.
The diagnostic message is JMN 1121-S syntax of background-color clause is
invalide or symbolic constant b-color is undefined.

Why?
```

#### ↳ Re: b-color & f-color in Fujitsu

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xmEq2.1416$oi.1437810@news3.mia>`
- **References:** `<78emq3$mdc$1@news0.skynet.be>`

```
GARWIG Ruddy wrote:
>In the screen-section, I use a variable (b-color) after the instruction
>background-color and foreground-color.
…[4 more quoted lines elided]…
>Why?

The phrase "symbolic constant b-color" is your clue.  Fujitsu apparently
requires a symbolic constant here, not a variable.  Check your manual or
help.  Next time, paste the actual code with error message in your post,
and we can give you a better response.  As it is, I have no clue as to
whether you may have made a syntax error of some kind, which is the other
possibility from the error message.  And don't 'tell' us how you declared
the variables, post the COBOL code.  Many errors are perceptual errors,
when you look right at the code and see what you expect to see, instead
of what is actually there.  Every experienced programmer is very familiar
with this phenomenon. :-)
```

#### ↳ Re: b-color & f-color in Fujitsu

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78ffet$mgv$1@news.igs.net>`
- **References:** `<78emq3$mdc$1@news0.skynet.be>`

```
You cannot set your colour dynamically in the screen section,
so the syntax is incorrect. The colour can be defined with a
*digit* or a symbolic constant, not a variable.

GARWIG Ruddy wrote in message <78emq3$mdc$1@news0.skynet.be>...
>In the screen-section, I use a variable (b-color) after the instruction
>background-color and foreground-color.
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: b-color & f-color in Fujitsu

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78g9dm$nv5@sjx-ixn5.ix.netcom.com>`
- **References:** `<78emq3$mdc$1@news0.skynet.be> <78ffet$mgv$1@news.igs.net>`

```
FYI,
  In the draft of the next COBOL Standard (as with several existing
compilers - but apparently not Fujitsu) there ARE ways to change
foreground/background color dynamically.  However, if you are using Fujitsu,
stick with what you have (as documented in your LRM)

NOTE: I have NOT verified that this isn't supported (yet) by Fujitsu, but am
assuming that Donald is correct.
```

###### ↳ ↳ ↳ Re: b-color & f-color in Fujitsu

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78gdtk$a4d$1@news.igs.net>`
- **References:** `<78emq3$mdc$1@news0.skynet.be> <78ffet$mgv$1@news.igs.net> <78g9dm$nv5@sjx-ixn5.ix.netcom.com>`

```
There are ways to change the colour with many of the compilers
that I have used, but I have never yet used one that allowed
the "background color IDENTIFIER-NAME" methodology in
the screen section. I always thought it rather annoying, to
tell the truth.  The most current version of MF I have is 4,
and it does not, the Liant that I have says you cannot, though
I have not tried it, and the Fujitsu gives you an error message
when you try it, so I assume that is the case (you cannot look
it up, because the online documents ... ah shit ... nine books,
no index, no global search, no way of using any cross references
except paper and pen, and if you do spend three hours searching
and finding every occurrence of the word "colour", you then have to
go back and do the same for "color" and even then it will not
be there ...

Can you tell I have been doing a lot of Fujitsu work lately?
;<)


William M. Klein wrote in message <78g9dm$nv5@sjx-ixn5.ix.netcom.com>...
>FYI,
>  In the draft of the next COBOL Standard (as with several existing
>compilers - but apparently not Fujitsu) there ARE ways to change
>foreground/background color dynamically.  However, if you are using
Fujitsu,
>stick with what you have (as documented in your LRM)
>
>NOTE: I have NOT verified that this isn't supported (yet) by Fujitsu, but
am
>assuming that Donald is correct.
>
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: b-color & f-color in Fujitsu

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78ggvb$s7@sjx-ixn5.ix.netcom.com>`
- **References:** `<78emq3$mdc$1@news0.skynet.be> <78ffet$mgv$1@news.igs.net> <78g9dm$nv5@sjx-ixn5.ix.netcom.com> <78gdtk$a4d$1@news.igs.net>`

```
Donald,
   When it comes to Accept/Display screen stuff, I always get confused which
is supported by X/Open, which is in the draft of the next Standard, and
which is in Micro Focus (all of which I have worked with).  I don't know
Fujitsu's support (although I do have a copy of their compiler in-house),
but you might look for one of the following:

1) Do you use a Screen Section entry with the Foreground/Background-Color
clause?  The next Standard will allow this to point to an identifier, not
just a literal, so you can change it from DISPLAY to DISPLAY or ACCEPT to
ACCEPT.
 (see also comment about MF below - in the middle of your comments)

2) Micro Focus (V4 is what I have an LRM handy for) only has integers for
FOREGROUND and BACKGROUND-COLOR on the DISPLAY statement *BUT* it includes
(format 3) a CONTROL is identifier phrase - which can "dynamically" modify
all the attributes specified in the CONTROL data-item described in the data
division section. (This includes - I think - colors)

3)  The draft Standard also has a new format of the SET statement which can
modify screen description attributes.  In the draft that I looked at
quickly, this did NOT include colors - but I don't know if this is
intentional or not (or the way the current draft looks).

   ***

I hope one of these provides you with some guidance where to look in the
Fujitsu documentation.
```

###### ↳ ↳ ↳ Re: b-color & f-color in Fujitsu

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36abd604.511455660@news1.ibm.net>`
- **References:** `<78emq3$mdc$1@news0.skynet.be> <78ffet$mgv$1@news.igs.net> <78g9dm$nv5@sjx-ixn5.ix.netcom.com> <78gdtk$a4d$1@news.igs.net> <78ggvb$s7@sjx-ixn5.ix.netcom.com>`

```
On Sun, 24 Jan 1999 19:21:40 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:


>2) Micro Focus (V4 is what I have an LRM handy for) only has integers for
>FOREGROUND and BACKGROUND-COLOR on the DISPLAY statement *BUT* it includes
…[3 more quoted lines elided]…
>

Microfocus V 3.x products allow this use of CONTROL.  I used it
extensively to modify things like "PROTECT" and colors and highlight
etc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
