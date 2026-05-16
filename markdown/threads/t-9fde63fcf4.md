[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do GO TO in AN

_1 message · 1 participant · 1994-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How to do GO TO in AN

- **From:** marty.tabnik@greatesc.com (Marty Tabnik)
- **Date:** 1994-12-03T21:10:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94120313504650@greatesc.com>`

```

> Subject: Re: How to do GO TO in ANSI85 COBOL
> Message-ID: <1994Dec2.163115.17069@atlas.com>
> References: <3b882g$9qk@ixnews1.ix.netcom.com>

> In article <3b882g$9qk@ixnews1.ix.netcom.com> kurtmisc@ix.netcom.com (Kurt Mi
> >>In article <3b0c3v$l7r@charles.cdec.polymtl.ca>
…[4 more quoted lines elided]…
> >simpler.

> Let me give you an example:
>  perform p-100 thru p-200
…[7 more quoted lines elided]…
> p-101.

>         do what ever.
>         go to p-200
…[5 more quoted lines elided]…
>         exit

PATIENT: Doctor, it hurts when I do this.
DOCTOR: Then don't do that.

1. Whyever would you WANT to perform p-100 thru p-199?

2. The real problem with your "beautiful" goto is that the next person
will insist that another goto is equally "beautiful".
        RESULT:  One has a "Goto Beauty Contest".
Gotos?  Just so NO! <g>
---
 * SLMR 2.1a * A-borg-rigine:  Australia is irrelevant.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
