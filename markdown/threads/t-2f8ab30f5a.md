[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NEWBIE Question about ACCEPT

_3 messages · 3 participants · 1999-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### NEWBIE Question about ACCEPT

- **From:** "Koen Van Impe" <101460.651@compuserve.com>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ik58b$opi$1@trex.antw.online.be>`

```
Hello,

I'm only just started to work in Cobol and I'm experiencing a problem.

I want to use the accept commando but with a preinstalled value. For example
when I set the variable   name = "UNKNOWN"
and when I would then use Accept name line 10 position 5 there should be
already UNKNOWN written on the screen, in such a way that the user can
modify the text UNKNOWN.

Is there anyone who can help me?

Best Regards,

Koen Van Impe
Belgium
KoenVan_Impe@csi.com
```

#### ↳ Re: NEWBIE Question about ACCEPT

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ika9h$uo$1@news.cerf.net>`
- **References:** `<7ik58b$opi$1@trex.antw.online.be>`

```
Koen Van Impe <101460.651@compuserve.com> wrote in message
>I want to use the accept commando but with a preinstalled value. For
example
>when I set the variable   name = "UNKNOWN"
>and when I would then use Accept name line 10 position 5 there should be
>already UNKNOWN written on the screen, in such a way that the user can
>modify the text UNKNOWN.

You may try: ACCEPT NAME LINE 10 POSITION 5 WITH UPDATE.

Cheesle
```

#### ↳ Re: NEWBIE Question about ACCEPT

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eNm33.9346$v%.569@news3.mia>`
- **References:** `<7ik58b$opi$1@trex.antw.online.be>`

```
Keep reading the Language reference.  If you accept something how can you
put something
there before anything appears?  (Hint: what do you look at when you use the
computer?)
Koen Van Impe <101460.651@compuserve.com> wrote in message
<7ik58b$opi$1@trex.antw.online.be>...
>Hello,
>
>I'm only just started to work in Cobol and I'm experiencing a problem.
>
>I want to use the accept commando but with a preinstalled value. For
example
>when I set the variable   name = "UNKNOWN"
>and when I would then use Accept name line 10 position 5 there should be
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
