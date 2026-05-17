[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF 3.2 Unix: embedding control characters

_2 messages · 2 participants · 1995-12_

---

### MF 3.2 Unix: embedding control characters

- **From:** "george lewycky" <ua-author-12797862@usenetarchives.gap>
- **Date:** 1995-12-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49ohte$5d7@news.ios.com>`

```

I have tried everything in the book and even options
MF has told me over the phone and I still cannot
embed a control charcter particularly TAB (x'09')
in either a LINE or RECORD sequential file...


amy ideas, samples, SOLUTIONS, alternates would
be appreciated..

Thanks

George




==================================================
George R Lewycky "I'd rather be on Titan !!"
Windows 95 = Macintosh 1989 with dual air bags

try me: http://soho.ios.com/~lewycky/

lew··.@soh··s.com geo··.@a··.com
==================================================
```

#### ↳ Re: MF 3.2 Unix: embedding control characters

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-12-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a145bc2a6f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<49ohte$5d7@news.ios.com>`
- **References:** `<49ohte$5d7@news.ios.com>`

```

In article <49ohte$5.··.@new··s.com>, George Lewycky writes:
› I have tried everything in the book and even options
› MF has told me over the phone and I still cannot
› embed a control charcter particularly TAB (x'09')
› in either a LINE or RECORD sequential file...

The 'T' runtime switch ($COBSW) controls tabs specifically. There's also an
'N' switch which causes control characters to be "escaped" with a nul byte (eg,
so you can embed newlines that don't act as record terminators).

Having said that, for RECORD sequential, you should be able to do anything -
it's not a format specifically for text as LINE sequential is.

If this is no help, send me a specific (very short) piece of code & I'll take
a look for you.

Cheers, Kev.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
