[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP - MF COBOL 3.2.50 INSTALLATION PROBLEMS

_2 messages · 2 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP - MF COBOL 3.2.50 INSTALLATION PROBLEMS

- **From:** "avalo..." <ua-author-1047408@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998032804202701.XAA07457@ladder01.news.aol.com>`

```

I have 3.2.20 installed and working. But when I upgraded to 3.2.50 using the
downloaded update disks, I keep getting the 'Cobol run time library not
installed error'. The 'update' was succesful. But when I click on any of the
Icons from my WFW 3.11 I get the above error. Any tips/suggestions welcome.

Thanks
Seth
```

#### ↳ Re: HELP - MF COBOL 3.2.50 INSTALLATION PROBLEMS

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1998-03-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bb6f97ff3b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998032804202701.XAA07457@ladder01.news.aol.com>`
- **References:** `<1998032804202701.XAA07457@ladder01.news.aol.com>`

```

AVALONINTL wrote in article
<199··.@lad··l.com>...
› I have 3.2.20 installed and working.  But when I upgraded to 3.2.50 using
› the
…[7 more quoted lines elided]…
› Seth 

I've had that sort of error multiple times, for multiple reasons with
various MF-COBOL versions. It almost always comes down to some environment
variable which is supposed to point to a directory or list of directories
with some specific COBOL RTS module in it (e.g., COBOL¥LBR, COBOL¥EXEDLL).
One fruitful way this can happen is to install a new product, which adds
something in PATH before the MF-COBOL sections, so that the MF stuff gets
so far back in the string that the UPDATE routine doesn't find it (even
under NT, which supports very long paths, the MF UPDATE routine doesn't
scan all the way to the end, only a fixed number of bytes).

Good luck.

Gary Lee gl··.@nos··m.com (Remove the spam filter, etc.)
-----------------
"Twenty years of schoolin' and they put you on the day shift."
Bob Dylan
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
