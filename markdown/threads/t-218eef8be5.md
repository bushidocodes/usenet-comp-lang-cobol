[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 3.0

_3 messages · 3 participants · 2001-09 → 2002-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu 3.0

- **From:** "RJ" <donTEveNThinK@boutiT.com>
- **Date:** 2001-09-14T00:40:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mco7.10406$sM1.3401054@news3.rdc1.on.home.com>`

```
Hi all;

I downloaded Fujitsu Cobol, but when I execute my program it displays the
following message:

JMP0310 I-O OPEN ERROR. FILE = TRANSIN.TXT. 'NON-FILE. PGM=LAB4 ADR=00401218

and a second message shows:

JMP0099I-O TERMINATION. CODE=0310.

Does anyone know why an I getting this and how to rectify it?
Any suggestion would greatly be appreciated.

Thanks
RJ

p.s Is there a FAQ for Fujitsu Cobol?
```

#### ↳ Re: Fujitsu 3.0

- **From:** "mkozelka" <m_kozelka@ameritech.net>
- **Date:** 2001-09-14T17:26:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B5ro7.1663$7g6.627152@newssrv26.news.prodigy.com>`
- **References:** `<6mco7.10406$sM1.3401054@news3.rdc1.on.home.com>`

```
The "NON-FILE" means Fujitsu can not find the file.  Check you path, etc
```

#### ↳ Re: Fujitsu 3.0

- **From:** aperezg502 <member@dbforums.com>
- **Date:** 2002-03-01T21:24:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c8045e1_1@spamkiller.newsgroups.com>`
- **References:** `<6mco7.10406$sM1.3401054@news3.rdc1.on.home.com>`

```
Hi:

You need a check your logic, if you are create a file, you must be sure
that you have an OPEN OUTPUT FILE NAME or OPEN I-O FILENAME.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
