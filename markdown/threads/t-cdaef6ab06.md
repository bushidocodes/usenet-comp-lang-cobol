[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Color Change

_2 messages · 2 participants · 1998-09 → 1998-10_

---

### Color Change

- **From:** "Patrick Lykins" <lynkins@access.mountain.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3612dbaa.0@news.mountain.net>`

```
I have one last question, is their anyway to change color in CoBOL?

Thank you
Patrick L. Lykins
```

#### ↳ Re: Color Change

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298273.14757.23647@kcbbs.gen.nz>`
- **References:** `<3612dbaa.0@news.mountain.net>`

```
In message <<3612dbaa.0@news.mountain.net>> "Patrick Lykins" <lynkins@access.mountain.net> writes:
> 
> I have one last question, is their anyway to change color in CoBOL?

That will depend entirely on what is required to have its 
colour changed: printouts ? the programmer ? the source
code ?

If it is Cobol DISPLAYs to screen then there are several
ways to do it and this depends on the environment and the
compiler used.

With MicroFocus (or MS Cobol) you can do it with SCREEN
SECTION, with DISPLAY .... FOREGROUND-COLOUR BACKGROUND-COLOUR
(or even COLOR), or with CBL_WRITE_SCR_CHARS_ATTR (or
similar). or CALL x"A7", or configuring the ADIS 
routines.

In some environments you can send control sequences to
the screen to effect the colour changes.

Or you can provide a configuration file withh appropriate
settings.

Other compilers may have similar facilities or different
ones.  This may also depend on how you are displaying
to the screen (eg ANSI DISPLAY, extended DISPLAY or
Windows API).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
