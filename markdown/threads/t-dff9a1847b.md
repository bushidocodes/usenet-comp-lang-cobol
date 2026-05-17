[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [newbie qn] How to detect a single keypress

_2 messages · 2 participants · 1996-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### [newbie qn] How to detect a single keypress

- **From:** "limc..." <ua-author-7148397@usenetarchives.gap>
- **Date:** 1996-04-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4lrvqb$ip9@nuscc.nus.sg>`

```

Hi,
I'm a newbie to COBOL so please pardon me if this question seems too
trival. I need to detect a single keypress wihtout requiring the user to
press ENTER to terminate the input. Can I use

ACCEPT INPUT_CHAR WITH AUTO-SKIP

where INPUT_CHAR is PIC X?

thanks,
Chung Yong
```

#### ↳ Re: [newbie qn] How to detect a single keypress

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dff9a1847b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4lrvqb$ip9@nuscc.nus.sg>`
- **References:** `<4lrvqb$ip9@nuscc.nus.sg>`

```

In , bob··.@cix··o.uk ("Bob Sharp") writes:
›› -I need to detect a single keypress without
›› -requiring the user to press ENTER to
…[14 more quoted lines elided]…
›        ACCEPT SCREEN-n.

I'd suggest the easy way is to
CALL "CBL_READ_KBD_CHAR" (see the call-by-name subroutine docs)

Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
