[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Random Number Generation In COBOL 85

_2 messages · 2 participants · 1997-07_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Random Number Generation In COBOL 85

- **From:** "almcc..." <ua-author-17073623@usenetarchives.gap>
- **Date:** 1997-07-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970702193701.PAA25483@ladder02.news.aol.com>`

```

A couple years ago I had a need and the solution I ended up using is as
follows:

01 SYSTEM-TIME PIC 9(08).
01 SYSTEM-TIME-RED
REDEFINES SYSTEM-TIME.
05 SYSTEM-HOUR PIC 9(02).
05 SYSTEM-MIN PIC 9(02).
05 SYSTEM-SEC PIC 9(02).
05 SYSTEM-100TH-SEC PIC 9(02).

01 WORK-RANDOM-NUMBER PIC 9(06)V(06).
01 WORK-RANDOM-NUMBER-RED
REDEFINES WORK-RANDOM-NUMBER.
05 WORK-RAND-PREFIX PIC 9(06).
05 RANDOM-NUMBER PIC 9(06).

.
.
.

ACCEPT SYSTEM-TIME FROM TIME.
COMPUTE WORK-RANDOM-NUMBER = SYSTEM-TIME ** (-.5).


This give you the decimal protion of the square root of the system time.
It works
quite well unless you need to be able to reproduce your results for
testing. If
this is the case, you will need to use something other than the system
time to
seed the generator.

Good Luck
```

#### ↳ Re: Random Number Generation In COBOL 85

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-07-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fbb8f8d36-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970702193701.PAA25483@ladder02.news.aol.com>`
- **References:** `<19970702193701.PAA25483@ladder02.news.aol.com>`

```

In message <<199··.@lad··l.com>> alm··.@a··.com writes:

›      ACCEPT SYSTEM-TIME FROM TIME.
›      COMPUTE WORK-RANDOM-NUMBER = SYSTEM-TIME ** (-.5).
…[8 more quoted lines elided]…
› seed the generator.  

And, when developed, they put your program into a cron job.
Around 11:30pm the grating for the start time to get a unique
random number is around 1 minute. That is if the start time
is between 23:30 and 23:31 the same seed will be used.

Try inverting the time first so it reads ddssmmhh and then
take the square root.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
