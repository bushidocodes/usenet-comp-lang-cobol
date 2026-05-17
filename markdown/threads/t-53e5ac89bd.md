[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Y2K starting to show

_2 messages · 2 participants · 1997-02_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Y2K starting to show

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1997-02-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e12ad$7l9$1@news1.i1.net>`

```



Without going into too much detail, I'm trouble shooting problems for
a service bureau's latest client. And I ran into a date compare
problem.

April 7, 1997 might prove to be a forwarning of Y2K problems.

04/07/97 is 999 days before 01/01/00.

This system has a 3 digit field that adds number of days to a
pd-to-date to compare against the transaction date. The value of this
field is user defined. This user set the value to 999. Suddenly, a
number of transactions started kicking out as delinquent.

The (temporary) fix was easy. A value of 999 was extreme for their
needs, they've changed it to value less than half of 999. BTW, the
Y2K fix should be done this spring.

I thought I'd pass this on, in case someone hasn't thought of this Y2K
problem.


TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

#### ↳ Re: Y2K starting to show

- **From:** "sl..." <ua-author-4338670@usenetarchives.gap>
- **Date:** 1997-02-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-53e5ac89bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5e12ad$7l9$1@news1.i1.net>`
- **References:** `<5e12ad$7l9$1@news1.i1.net>`

```

tro··.@i··.net (Tim Oxler) wrote:
› April 7, 1997 might prove to be a forwarning of Y2K problems.
› 04/07/97 is 999 days before 01/01/00.
› The (temporary) fix was easy.  A value of 999 was extreme for their
› needs, they've changed it to value less than half of 999.  BTW, the
› Y2K fix should be done this spring.

Interesting. I have been yelling about this for a couple of years now
but nobody is much interested. My particular bugbear is OS tape
catalogs, which are not really geared for the solution you suggest.
99 days expiry, 9 days expiry etc. We shall just have to wait
and see won't we.
----------------------------------------------------------------
Chris Anderson email: sl··.@fas··o.za
Y2K Cinderella Project web··.@cin··o.za
www.cinderella.co.za - Striving to achieve Year 2000 Compliance
----------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
