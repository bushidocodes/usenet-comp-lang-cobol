[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fujitsu frustration

_4 messages · 2 participants · 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### fujitsu frustration

- **From:** SkidMike <skidmike@mindspring.com>
- **Date:** 1998-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362D1E57.C0FBCD41@mindspring.com>`

```
still working on the full-screen dilemma.  no matter what values i give
the run-time setup for @scrnsize and @scrnfont, i get an 80x24 area. 
depending on what font and font size i enter, it sometimes is a little
2"x4" screen with the fonts sized accordingly.  no response to my email
to fujitsu, but tech support promised an answer tomorrow.
```

#### ↳ Re: fujitsu frustration

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70jjau$fuo$1@news.igs.net>`
- **References:** `<362D1E57.C0FBCD41@mindspring.com>`

```

SkidMike wrote in message <362D1E57.C0FBCD41@mindspring.com>...
>still working on the full-screen dilemma.  no matter what values i give
>the run-time setup for @scrnsize and @scrnfont, i get an 80x24 area.
>depending on what font and font size i enter, it sometimes is a little
>2"x4" screen with the fonts sized accordingly.  no response to my email
>to fujitsu, but tech support promised an answer tomorrow.

I have had no problems here at all.  Is it possible that you are displaying
on the console rather than the screen?  Try setting the console size
instead of the screen size, and see what happens.
```

##### ↳ ↳ Re: fujitsu frustration

- **From:** SkidMike <skidmike@mindspring.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362DBD57.96545284@mindspring.com>`
- **References:** `<362D1E57.C0FBCD41@mindspring.com> <70jjau$fuo$1@news.igs.net>`

```
no, i'm using the screen.  everything i have is coded in SCREEN
SECTION.  is there a parameter i should code in the SCREEN SECTION?
```

###### ↳ ↳ ↳ Re: fujitsu frustration

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70l2ci$5pf$1@news.igs.net>`
- **References:** `<362D1E57.C0FBCD41@mindspring.com> <70jjau$fuo$1@news.igs.net> <362DBD57.96545284@mindspring.com>`

```

SkidMike wrote in message <362DBD57.96545284@mindspring.com>...
>no, i'm using the screen.  everything i have is coded in SCREEN
>SECTION.  is there a parameter i should code in the SCREEN SECTION?

Not that I know of.  mmm.  Not sure what else to suggest.  Have
you checked the cobol.cbr file with a text editor?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
