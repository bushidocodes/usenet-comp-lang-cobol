[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen colors with RM/85

_4 messages · 3 participants · 1996-06_

---

### Screen colors with RM/85

- **From:** "ferr..." <ua-author-17086290@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oteg2$mjm@star.epix.net>`

```

What is the syntax (if it there is one at all) to
specify screen foreground and background colors
with RM/COBOL 85? If it makes any difference,
I am running under SCO UNIX.

thanks,
don
```

#### ↳ Re: Screen colors with RM/85

- **From:** "uwe baemayr" <ua-author-6588910@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-57fe6eccfa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4oteg2$mjm@star.epix.net>`
- **References:** `<4oteg2$mjm@star.epix.net>`

```

don ferrario wrote:

› What is the syntax (if it there is one at all) to
› specify screen foreground and background colors
› with RM/COBOL 85?  If it makes any difference,
› I am running under SCO UNIX.

Colors are specified with the FCOLOR and BCOLOR keywords
in the ACCEPT or DISPLAY control phrases:

DISPLAY "HOWDY", CONTROL "FCOLOR=GREEN,BCOLOR=RED".

Valid color names are BLACK, BLUE, GREEN, CYAN, RED, MAGENTA,
BROWN, and WHITE. However, under UNIX, color output is available
only on non-visible attribute terminals, and the terminfo
entry contains the set_foreground and set_background strings,
or the termcap database contains Sb and St sequences (if you're
using termcap instead of terminfo).

Alternatively, if your terminal supports ISO SGR (Set Graphics
Rendition) sequences, you can force the runtime to use these
sequences by specifying TERM-ATTR USE-COLOR=Y in your runtime
configuration file.

This is described on pg 8-10 ("ACCEPT and DISPLAY statements")
and page 10-29 ("Configuration Records: TERM-ATTR") of the
RM/COBOL V6 for Netware, UNIX, and Windows User's Guide.

I hope you find this helpful.

------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Ryan McFarland Corporation | or: jea··.@ccw··s.edu |
| -- a division of Liant Software | Compuserve: 74774,47 / GO LIANT |
------------------------------------------------------------------------
```

#### ↳ Re: Screen colors with RM/85

- **From:** "ferr..." <ua-author-17086290@usenetarchives.gap>
- **Date:** 1996-06-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-57fe6eccfa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4oteg2$mjm@star.epix.net>`
- **References:** `<4oteg2$mjm@star.epix.net>`

```

In article <4oteg2$m.··.@sta··x.net>, fer··.@ep··x.net says...
› 
› What is the syntax (if it there is one at all) to
…[4 more quoted lines elided]…
› 

Oh, I forgot...

If RM/85 does not support screen colors,
what is the syntax in later versions.

I am porting programs from RM/85 to MF, but I
need to add screen colors (which MF supports).
If I leave the RM-compiler switch on, the compiler
rejects MF color accept/display style statements.

I don't have documentation for later versions of
RM/cobol, but I would suspect a later RM syntax
would be supported by MF using the RM-compiler
directive.

I have considered recoding to straight MF syntax,
but this appears to involve considerable difference
in syntax - especially in accept/display areas.

CALLING all you RM programmers - please help
with screen color syntax!

thanks,
don
```

#### ↳ Re: Screen colors with RM/85

- **From:** "juan manuel urraburu" <ua-author-17084485@usenetarchives.gap>
- **Date:** 1996-06-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-57fe6eccfa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4oteg2$mjm@star.epix.net>`
- **References:** `<4oteg2$mjm@star.epix.net>`

```

Check the CONTROL in the DISPLAY statement, you can select Forecolor and
Backcolor.

Juan Manuel Urraburu
pro··.@adi··m.uy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
