[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Graphics character ????

_3 messages · 3 participants · 1995-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Graphics character ????

- **From:** "kmd..." <ua-author-6421711@usenetarchives.gap>
- **Date:** 1995-01-04T00:08:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3edagq$inl@news.tamu.edu>`

```
I am trying to dress up some menus. What are the graphics characters avaible
in MF-Cobol?
```

#### ↳ Re: Graphics character ????

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-01-04T04:55:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0a924b4dee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3edagq$inl@news.tamu.edu>`
- **References:** `<3edagq$inl@news.tamu.edu>`

```
kmd··.@tam··u.edu (Kristen Dunham) wrote:
›
› I am trying to dress up some menus. What are the graphics characters avaible
› in MF-Cobol?
›

I guess it depends a bit on what terminal you have. On Windows you can
use any IBMPC characters using the old trick of holding down the Alt key and
then using the numeric keys to get the characters into nonnumeric literals
and using these in screen items. On Unix this wouldn't work as you could
have any old terminal connected and the hex values might do strange things.

So you may need to do this stuff in a generic or portable way. If its line
drawing then by using the CBL_GET_SCR_LINE_DRAW routine (look it up in your
docs for details under Library Routines - Call by name) you get back the
graphics characters or ascii equivalents depending on the capabilities of
the terminal. For other graphics look at CBL_GET_SCR_GRAPHICS.

Using these routines you should be able to get menus that work under DOS,
Windows, OS/2 and Unix. Good luck.
```

##### ↳ ↳ Re: Graphics character ????

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-01-04T07:21:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0a924b4dee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0a924b4dee-p2@usenetarchives.gap>`
- **References:** `<3edagq$inl@news.tamu.edu> <gap-0a924b4dee-p2@usenetarchives.gap>`

```

In article <3edrb9$8.··.@ice··o.uk>, Martyn Woerner writes:
› kmd··.@tam··u.edu (Kristen Dunham) wrote:
›› 
…[8 more quoted lines elided]…
› have any old terminal connected and the hex values might do strange things.
 
› Please don't do it this way.
 
› So you may need to do this stuff in a generic or portable way.  If its line
› drawing then by using the CBL_GET_SCR_LINE_DRAW routine (look it up in your
› docs for details under Library Routines - Call by name) you get back the 
› graphics characters or ascii equivalents depending on the capabilities of 
› the terminal.  For other graphics look at CBL_GET_SCR_GRAPHICS.

Please do it this way.

Cheers,
Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
