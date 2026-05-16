[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# POWER COBOL V6

_2 messages · 2 participants · 2005-04_

---

### POWER COBOL V6

- **From:** "Gys Els" <ghmcomputers@absamail.co.za>
- **Date:** 2005-04-21T12:43:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8vOdnRa7yex4G_rfRVn-jw@is.co.za>`

```
can anybody please give me a example of how to use the POW-ESCAPE-KEY in a 
program.
```

#### ↳ Re: POWER COBOL V6

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-04-21T08:21:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<116fa1vm0n49u33@news.supernews.com>`
- **References:** `<8vOdnRa7yex4G_rfRVn-jw@is.co.za>`

```
Gys Els wrote:
> can anybody please give me a example of how to use the POW-ESCAPE-KEY
> in a program.

In the KeyUp, KeyDown, or KeyPress event, code:

   IF POW-KEYCODE = POW-KEY-ESCAPE
    (do something).

BUT - PowerCOBOL traps for the ESC key during debugging and interrupts 
execution.* Your application will still see the escape key, but execution 
stops and you have to mash [F5] to continue executing.

---------
*Why, oh why, they didn't use the "ScrollLock" key to control the debugging 
process is a mystery.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
