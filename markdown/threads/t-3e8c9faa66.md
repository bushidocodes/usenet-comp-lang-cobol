[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INITIALIZE?

_5 messages · 4 participants · 2001-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### INITIALIZE?

- **From:** C Pac <WhiteDragon@dexchange.de>
- **Date:** 2001-01-23T21:53:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A6DEF43.5F990B5A@dexchange.de>`

```
Hi,
I know, this is an old question, sorry: How das the INITIALIZE-Order
works in groups, numerics and alphanumeric vars?
Thanks, Chris.
```

#### ↳ Re: INITIALIZE?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-24T00:05:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d%ob6.1249$KJ3.61403@newsread2.prod.itd.earthlink.net>`
- **References:** `<3A6DEF43.5F990B5A@dexchange.de>`

```
My manual has three pages on the actions of INITIALIZE.

At the most basic level, the verb sets elementary items to spaces or
zero depending on the PIC. The verb skips FILLERs (or implicit FILLERs
like "02  PIC X(10)"  ). INITALIZE ignores group items (but not the
elementary items subordinate to a group).

So,
01  MYDATA.
   02  MYALPHA      PIC X(10).       *>Set to spaces
   02  MYNUM           PIC 9(5).         *>Set to '00000'.
   02  MYVAL.                                    *>Ignored, but ends
up as low-values because of next item
        05  MYCOMP       PIC S9(4) COMP-5     *>Set to low-values
   02  FILLER           PIC X(10).                *> Undefined

There are variations depending on REDEFINES, NATIONAL CHARACTER,
OCCURS DEPEDING ON, REPLACING, and other exotics.


"C Pac" <WhiteDragon@dexchange.de> wrote in message
news:3A6DEF43.5F990B5A@dexchange.de...
> Hi,
> I know, this is an old question, sorry: How das the INITIALIZE-Order
…[3 more quoted lines elided]…
>
```

#### ↳ Re: INITIALIZE?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-24T03:36:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5sb6.10743$Sl.561918@iad-read.news.verio.net>`
- **References:** `<3A6DEF43.5F990B5A@dexchange.de>`

```
In article <3A6DEF43.5F990B5A@dexchange.de>,
C Pac  <WhiteDragon@dexchange.de> wrote:
>Hi,
>I know, this is an old question, sorry: How das the INITIALIZE-Order
>works in groups, numerics and alphanumeric vars?

The same way the manual says it does... usually.

Now, please do your own homework.

DD
```

##### ↳ ↳ Re: INITIALIZE?

- **From:** alex <alex.ortiz@cpa.state.tx.us+3>
- **Date:** 2001-01-24T06:30:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94mhug$nq2$1@goblin.tdh.state.tx.us>`
- **References:** `<3A6DEF43.5F990B5A@dexchange.de> <f5sb6.10743$Sl.561918@iad-read.news.verio.net>`

```
NA wrote:

> In article <3A6DEF43.5F990B5A@dexchange.de>,
> C Pac  <WhiteDragon@dexchange.de> wrote:
…[8 more quoted lines elided]…
> DD

yeah... <begin sarcasm>don't be bothering this group with nonsensical
or inconsequential inquiries! <end sarcasm>.
```

###### ↳ ↳ ↳ Re: INITIALIZE?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-24T13:52:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m6Bb6.10796$Sl.564365@iad-read.news.verio.net>`
- **References:** `<3A6DEF43.5F990B5A@dexchange.de> <f5sb6.10743$Sl.561918@iad-read.news.verio.net> <94mhug$nq2$1@goblin.tdh.state.tx.us>`

```
In article <94mhug$nq2$1@goblin.tdh.state.tx.us>,
alex  <alex.ortiz@cpa.state.tx.us+3> wrote:
>NA wrote:
>
…[13 more quoted lines elided]…
>or inconsequential inquiries! <end sarcasm>.

Now, now... 'sensible' or 'consequential' are, many would say, more
frequently matters of interpretation than what is stated in The Manual;
the invocation of 'Read The Fornicating Manual' applies to coders, last
time I looked.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
