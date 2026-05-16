[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CD 1.10 inconsistency

_3 messages · 2 participants · 2000-12_

---

### CD 1.10 inconsistency

- **From:** Herwig Huener <Herwig.Huener!@!fujitsu-siemens.com>
- **Date:** 2000-12-07T16:25:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90oa91$1pp$1@news.mch.sbs.de>`

```
2000-12-07 16:25:36 MEZ

In CD 1.10 in section C.23 Example of
free form reference format you see that
inline comments are legal in either free
or fixed reference format. The same rule
follows from 6.1.2 or 6.2.6.2.

In 7.2.2 Syntax rules, bullet 3 and 4
clearly indicate that, for directives,
inline comments are allowed only in
free reference format.

It cannot be that directives have a
restriction which ordinary COBOL-lines
have not. However, we implemented all
that already.

:-(

I expect that the said restriction
for directives will be taken away in
the final standard, and that
inline-comments are allowed in either
reference formats, for directives as
well as ordinary program-text.

So I make inline-comments legal in
directives in either format right now.

Or is there good reason not to do so?

Herwig
```

#### ↳ Re: CD 1.10 inconsistency

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90ontc$77k$1@slb6.atl.mindspring.net>`
- **References:** `<90oa91$1pp$1@news.mch.sbs.de>`

```
I don't know why you post this type of question in this NG and do not send
them to J4 - but FYI,  there were specify "debates" on where in-line
comments would and would not be allowed and I *doubt* that the current rules
will be changed. (i.e. I do NOT expect them to be allowed in fixed form
compiler directing statements)

FYI,
  At the last meeting (and I don't know if this is or is not reflected in CD
1.10) there was a "new" restriction added that inline comments are NOT
allowed on a line with a continued alphanumeric literal, e.g the following
is non-conforming.

    05 abc Pic X(100) Value "abc"-  *> this isn't allowed
           "xyz".
```

##### ↳ ↳ Re: CD 1.10 inconsistency

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2000-12-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A2FF223.C46BA685@Josella-Simone-Playton.de>`
- **References:** `<90oa91$1pp$1@news.mch.sbs.de> <90ontc$77k$1@slb6.atl.mindspring.net>`

```
2000-12-07 21:21:21 MET

"William M. Klein" wrote:
> 
> I don't know why you post this type of question in this NG and do not send
> them to J4

Maybe some advertizing for the new standard?

> - but FYI,  there were specify "debates" on where in-line
> comments would and would not be allowed and I *doubt* that the current rules
> will be changed. (i.e. I do NOT expect them to be allowed in fixed form
> compiler directing statements)

I can live with that. Its just a matter of some

#define FEATURE_SOANDSO

#ifdef FEATURE_SOANDSO
   ...
#else
   ...
#endif

within the compiler itself.

> FYI,
>   At the last meeting (and I don't know if this is or is not reflected in CD
…[5 more quoted lines elided]…
>            "xyz".

This is included in the CD 1.10 as far as I remember
from here.

Herwig
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
