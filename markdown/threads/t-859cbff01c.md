[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe Rates in NYC metro area

_3 messages · 3 participants · 1997-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Mainframe Rates in NYC metro area

- **From:** "jim..." <ua-author-88074@usenetarchives.gap>
- **Date:** 1997-11-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19971102054500.AAA00974@ladder02.news.aol.com>`

```

Looking to find out what are the best rates for NYC and its suburbs (north
Jersey and Westchester/Rockland counties).

I am a 20 year geek in the field, straight out of high school. COBOL 19 of
those years, CICS/VSAM 15, IMS 11, DB2 a couple (also Oracle mainframe
SQL as well).... Know all about the Y2K issues, working for a company in
complete denial still, since they haven't moved their butts in months since
they did an initial inventory assessment using tools such as Viasoft Estimate
2000, which showed it to be a $15 million nut they can't accept, just for the
mainframe portion....

Thinking about bailing out. Knowing real rates people are getting out there
would help. And places giving the better rates would be nice (hey I can
dream, can't I?).
```

#### ↳ Re: Mainframe Rates in NYC metro area

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-11-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-859cbff01c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19971102054500.AAA00974@ladder02.news.aol.com>`
- **References:** `<19971102054500.AAA00974@ladder02.news.aol.com>`

```

Jim7458 wrote:
› 
› Looking to find out what are the best rates for NYC and its suburbs (north
…[12 more quoted lines elided]…
›  dream, can't I?).

I can't help you with NYC rates, but I can comment on Viasoft Estimate
2000, since we used it to develope an initial estimate for our mainframe
conversion. We used it for estimating Easytrieve and assembler programs
as well as COBOL, and I believe it also supports PL/1.

Viasoft will give you a pretty good estimate, BUT their tool assumes
that all dates will be expanded to a 4-digit year. That includes every
screen and printed report, and every date in every file. You may be
able to reduce your effort with a windowing logic approach, provided
your date horizons are short enough (we have some systems where dates
consist only of month and day).

One example where windowing may be the only practical approach is in
using ACH files (Automated Clearing House). Thousands of banks and
retail businesses exchange data using ACH file formats, which only
support 2-digit years. Dates in ACH files normally cannot be more than
a year old. It will not be possible for all ACH users to convert at the
same time.

Windowing is not appropriate for dates that could span more than 100
years. Date-of-birth is a common example. Dates in VSAM file keys also
cannot be windowed very successfully. Some system timing applications
will also require full date expansion.

It would be a big mistake not to attempt any Y2K remediation, just
because the Viasoft estimate is too high.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Mainframe Rates in NYC metro area

- **From:** "shivkumar visvanathan" <ua-author-17073382@usenetarchives.gap>
- **Date:** 1997-11-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-859cbff01c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19971102054500.AAA00974@ladder02.news.aol.com>`
- **References:** `<19971102054500.AAA00974@ladder02.news.aol.com>`

```

Based on your experience ,you could $40-50 per hour.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
