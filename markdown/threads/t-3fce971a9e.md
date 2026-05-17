[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RESERVED WORD LIST

_6 messages · 6 participants · 1996-03_

---

### RESERVED WORD LIST

- **From:** "ljwa..." <ua-author-17087381@usenetarchives.gap>
- **Date:** 1996-03-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<315B2568.7289@nando.net>`

```
I'm looking for a list of reserved words for COBOL. Example:
current-date, etc. ljw··.@na··o.net
```

#### ↳ Re: RESERVED WORD LIST

- **From:** "michael parkes" <ua-author-13875835@usenetarchives.gap>
- **Date:** 1996-03-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fce971a9e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<315B2568.7289@nando.net>`
- **References:** `<315B2568.7289@nando.net>`

```
ljw··.@na··o.net wrote:
› I'm looking for a list of reserved words for COBOL. Example:
› current-date, etc. ljw··.@na··o.net

There is a complete standard conforming list is the back of
the ANSI COBOL-85 standard.

Regards,

Mike
```

#### ↳ Re: RESERVED WORD LIST

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-03-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fce971a9e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<315B2568.7289@nando.net>`
- **References:** `<315B2568.7289@nando.net>`

```
I'm sending you by e-mail a list of reserved words for many compilers.
The problem with the ANSI list is that most compiler
vendors add their own extensions, CURRENT-DATE
being the prime example.
In the list, a + in the ANSI column means that the
word is an ANSI standard. There are no +'s for the
other compilers for that word if they support the ANSI
standard, but a minus if they don't.
```

#### ↳ Re: RESERVED WORD LIST

- **From:** "glenn a. mitchell" <ua-author-17072865@usenetarchives.gap>
- **Date:** 1996-03-28T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fce971a9e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<315B2568.7289@nando.net>`
- **References:** `<315B2568.7289@nando.net>`

```
The reserved word list changes depending on what level COBOL you're
talking about as well as what compiler you're using. Generally the list
is available in the compiler manual. Frankly, the best place to locate a
general list is in the appropriate standard document itself.

Glenn A. Mitchell               mit··.@m··.org or
Director, Computer Technology   mit··.@poa··c.org
Maine Medical Center            (207) 871-2409
Portland, ME  04101		http://www.mmc.org
```

#### ↳ Re: RESERVED WORD LIST

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1996-03-30T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fce971a9e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<315B2568.7289@nando.net>`
- **References:** `<315B2568.7289@nando.net>`

```
ljw··.@na··o.net wrote:
: I'm looking for a list of reserved words for COBOL. Example:
: current-date, etc. ljw··.@na··o.net

You have to look in the reference manual for the particular compiler
you are using, because each compiler has its own list of reserved
words.

If you have access to a copy of the COBOL 1985 standard and want to
see the minimum list of reserved words that all standard compilers have
to recognize, you can find it on pages IV-45 and IV-46. But you won't
find your example, CURRENT-DATE, in that list, because it is not a
reserved word in standard COBOL.

If you are trying to choose a name for a data item or procedure and
want to avoid accidentally using a reserved word, one way to be safe
is to choose a word that meets any of the following criteria:

1. A word that begins with a digit or the letter 'X' or 'Y'.
2. Any single letter, 'A' through 'Z'.
3. A word with two or more contiguous hyphens.

Another technique some programmers use to avoid reserved words is to
take any English word and insert a hyphen anywhere, for example,
'TOT-AL' or 'CO-UNT' or 'HEAD-ING'.

Maybe other programmers know some more techniques to help avoid
reserved words when there isn't a list handy.

Walter Murray
Hewlett-Packard
Support Technology Lab
```

##### ↳ ↳ Re: RESERVED WORD LIST

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1996-03-31T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3fce971a9e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3fce971a9e-p5@usenetarchives.gap>`
- **References:** `<315B2568.7289@nando.net> <gap-3fce971a9e-p5@usenetarchives.gap>`

```
In article <4jn625$e.··.@ros··p.com>
wal··.@hpr··p.com "Walter Murray" writes:
› ljw··.@na··o.net wrote:
›› I'm looking for a list of reserved words for COBOL.
…[7 more quoted lines elided]…
› reserved words when there isn't a list handy.

There was a discussion on 'Coding Styles' here in Jan 1995 and
dataname prefixes were (generally) approved. Use of a prefix will
also avoid the reserved word problem. One example of this style:
...
01 DB-RECORD.
05 DB-KEY PIC 9(6).
...
01 WS-NUM PIC 9(4).
01 WS-DB-RECORD.
05 WS-DB-KEY PIC 9(6).
...
Richard Ross-Langley  YMMV
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
