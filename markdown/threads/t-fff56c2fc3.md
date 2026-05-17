[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ���2��� & IBM Cobol for AIX

_3 messages · 3 participants · 1997-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### ���2��� & IBM Cobol for AIX

- **From:** "panos ioannou" <ua-author-17073311@usenetarchives.gap>
- **Date:** 1997-11-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63nq1p$eo91@athserv.otenet.gr>`

```

I am trying to get the system year as a four digit number directly from the
OS but unfortunately I can't find anything (the manuals mention nothing
about it).
Any kind of help is welcome...

Thanx in advance.
```

#### ↳ Re: ���2��� & IBM Cobol for AIX

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-11-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fff56c2fc3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<63nq1p$eo91@athserv.otenet.gr>`
- **References:** `<63nq1p$eo91@athserv.otenet.gr>`

```

In article <63nq1p$eo··.@ath··t.gr>,
"Panos Ioannou" wrote:
›
› I am trying to get the system year as a four digit number directly from
› the OS but unfortunately I can't find anything (the manuals mention
› nothing about it).

Your Subject: line arrived here somewhat garbled, but if you are talking
AIX, it's on page 437 of SC26-4769, and the following will probably work
for you even if you are not talking AIX:

05 WS-YYYY-X.
10 WS-YYYY-9 PIC 9(4).

MOVE FUNCTION CURRENT-DATE TO WS-YYYY-X.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: ���2��� & IBM Cobol for AIX

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-11-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fff56c2fc3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<63nq1p$eo91@athserv.otenet.gr>`
- **References:** `<63nq1p$eo91@athserv.otenet.gr>`

```

Look for the Intrinsic function CURRENT-DATE.

MOVE FUNCTION CURRENT-DATE TO 21-BYTE-GROUP-ANSWER

Provides synchronized 4 digit year date, Julian, Time, GMT offset.
Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
