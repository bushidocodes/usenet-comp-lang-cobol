[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# numeric fields in fujitsu 4.0

_3 messages · 3 participants · 1998-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### numeric fields in fujitsu 4.0

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36732D28.FC270624@mindspring.com>`

```
i haven't seen a thread on this yet so if i'm not in everyone's kill
filters, here goes.

say you have a 'form' in powercobol from fujitsu.  the numeric fields
are monetary (U.S. dollars  i.e.  pic 999v99)  it was suggested to me by
my boss that the user be able to enter the monetary amount without
having to 'hunt-and-peck' for the 'period'.
the solution i came up with was to take the "Text" OF CM-TEXT-BOX and
multiply it by .01  (move the decimal point 2 spaces to the left)
then move the result to "Text" OF CM-TEXT-BOX for display purposes.
ultimately, in terms of customer satisfaction i guess, how far do you
guys go in such a situation?  and is my solution an acceptable one?
```

#### ↳ Re: numeric fields in fujitsu 4.0

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u7YTR1kJ#GA.273@upnetnews03>`
- **References:** `<36732D28.FC270624@mindspring.com>`

```
Let'em 'hunt & peck' for the decimal point (period) - it's easy enough to
find (besides, there are two of them on almost every keyboard if you keep
your NumLock activated :-)

skidmike wrote in message <36732D28.FC270624@mindspring.com>...
>i haven't seen a thread on this yet so if i'm not in everyone's kill
>filters, here goes.
…[9 more quoted lines elided]…
>guys go in such a situation?  and is my solution an acceptable one?
```

#### ↳ Re: numeric fields in fujitsu 4.0

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<750g47$b2m$1@news.igs.net>`
- **References:** `<36732D28.FC270624@mindspring.com>`

```
If you set the render text attributes to Cobol picture,
and set the picture to 999v99, then I don't think
you need to do anything else ...

skidmike wrote in message <36732D28.FC270624@mindspring.com>...
>i haven't seen a thread on this yet so if i'm not in everyone's kill
>filters, here goes.
…[9 more quoted lines elided]…
>guys go in such a situation?  and is my solution an acceptable one?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
