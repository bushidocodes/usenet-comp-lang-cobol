[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FUNCTION and reference modification

_5 messages · 3 participants · 2007-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### FUNCTION and reference modification

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-17T19:41:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ethcp2$kce$00$1@news.t-online.com>`

```
Intersting, (alphanumeric) FUNCTION's can be ref-modded.
OK. I can see the point of getting some
subset of eg. CURRENT-DATE.

Interesting is, however, using ref modding on a
variable length return field.
eg.
MOVE FUNCTION TRIM (MYFLD) (1:1) TO ..

Note that TRIM can (AFAIKS) can return a zero
field length.
Yes, of course, one can test the field for spaces.
The question is what should happen with the move ?
Yes, Rick, I know that ref modding can return
an exception code.
```

#### ↳ Re: FUNCTION and reference modification

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-17T15:28:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vogdvgo57b64c@corp.supernews.com>`
- **References:** `<ethcp2$kce$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:ethcp2$kce$00$1@news.t-online.com...
> Intersting, (alphanumeric) FUNCTION's can be ref-modded.
> OK. I can see the point of getting some
…[10 more quoted lines elided]…
> The question is what should happen with the move ?

FDIS 2002, page 478, 14.8.24.3 [MOVE statement]
General rules, GR1, "The length of the data item
referenced by identifier-1 is evaluated only once,
immediately before the data is moved to the first of
the receiving operands. If identifier-1 is a zero-length
item, it is as if literal-1 were specified as the figurative
constant SPACE."

> Yes, Rick, I know that ref modding can return
> an exception code.

But, did you know that the use "ref modding" makes
me cringe and I prefer "reference modification",
because that is what the standard calls it. <g>
```

##### ↳ ↳ Re: FUNCTION and reference modification

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-03-17T22:32:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ethmp0$lqq$03$1@news.t-online.com>`
- **References:** `<ethcp2$kce$00$1@news.t-online.com> <12vogdvgo57b64c@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12vogdvgo57b64c@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[30 more quoted lines elided]…
>
Ha,
then call things what they really are -
eg. FUNCTION LOCALE-UPPER-CASE
FUNCTION LOCALE-LOWER-CASE
FUNCTION TRIM-LEADING
FUNCTION TRIM-TRAILING
etc. (for more FUNCTIONS) instead of confusing all users.
```

###### ↳ ↳ ↳ Re: FUNCTION and reference modification

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-03-17T17:56:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12vop4d1k4almb1@corp.supernews.com>`
- **References:** `<ethcp2$kce$00$1@news.t-online.com> <12vogdvgo57b64c@corp.supernews.com> <ethmp0$lqq$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:ethmp0$lqq$03$1@news.t-online.com...
>
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
…[3 more quoted lines elided]…
> > news:ethcp2$kce$00$1@news.t-online.com...
[snip]
> >> Yes, Rick, I know that ref modding can return
> >> an exception code.
…[12 more quoted lines elided]…
> etc. (for more FUNCTIONS) instead of confusing all users.

Functions aren't called; they're activated. <g>

FDIS 2002, page 385, 14.5.2.1.1 Active state,
"An instance of a function is placed in an active state
when it is successfully activated and remains active
until the execution of a GOBACK or STOP statement
or an implicit or explicit function format of the EXIT
statement within this instance of this function."
```

#### ↳ Re: FUNCTION and reference modification

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-19T03:56:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRnLh.367006$k82.47667@fe07.news.easynews.com>`
- **References:** `<ethcp2$kce$00$1@news.t-online.com>`

```
Roger,
   What would you do when you reference modify ANY zero-length item, e.g.

  01 Big.
      05  Num1   Pic 9.
      05  Tabl.
             10 Elem occurs 0 to 9 times depending on Num
                     Pic X.
  ...
  Move Zero to Num1
   Move Tabl (1:) to Wherever
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
