[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Blink

_2 messages · 2 participants · 2002-06 → 2002-07_

---

### Blink

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-30T04:12:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d1ebf0b@news.mhogaming.com>`

```
Why doesn't blink work for me, i would code something like this, but it
wouldn't blink.

  03 line 1 column 34 value "Blink Test" underline, reverse-video, Blink.
```

#### ↳ Re: Blink

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-01T08:37:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2006A8.BF87EC2E@Azonic.co.nz>`
- **References:** `<3d1ebf0b@news.mhogaming.com>`

```
Joseph Ostreicher wrote:
> 
> Why doesn't blink work for me, i would code something like this, but it
> wouldn't blink.
> 
>   03 line 1 column 34 value "Blink Test" underline, reverse-video, Blink.

All that the options can do is to set the attributes if they exist on
the particular device being used. This is not just for an IBM PC video
but may be any number of completely different terminals.

The IBM presumably has a VGA (or SVGA, XGA etc being used in VGA) and
this is nominally 16 colour in text mode - there is an 8 bit attribute. 
For foreground colours it is 8 colours + bright (so yellow is 'brown +
bright'), the background colours may be used as 8 colour + bright or as
8 colour + flash.  

Now if your machine had an MDA (Monochrome) card then it _would_ flash,
and get a true underline but there would be no colours (except
green/black or so).

This is one reason that I don't use SCREEN SECTION or DISPLAY WITH - It
becomes hard coded in the program and on different screen types (such as
telnet sessions or actual terminals) may be inappropriate.  I wrote code
decades ago that set the display attributes by displaying terminal
escape sequences, ANSI codes or using CALL x"A7" (on MF).  A program
allows each user to set whatever colours that they like for the terminal
(or by company, application etc) and this is recivered when they login
to my system.

Much the same can be done using CBL_SCR_.. routines on MF.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
