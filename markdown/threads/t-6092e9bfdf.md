[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copy and replace file cobol/cics

_3 messages · 3 participants · 1997-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Copy and replace file cobol/cics

- **From:** "bfe..." <ua-author-6637215@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970912231800.TAA25448@ladder02.news.aol.com>`

```

we are working on y2k at work, and i wanted to copy a copylib member i
also wanted to replace certain words in the copy member. basically i
wanted to replace certain characters and not the entire word, i was not
able to do this:

eg:
copy member:
01 FIELD1.
05 AT-FIELD1 PIC X.
05 AT-FIELD2 PIC X.
.
etc etc.

writing:

COPY FILE1 REPLACING AT-FIELD1 BY AS-FIELD1. <==works

but i have many fields.:

COPY FILE1 REPLACING AT BY AS <==does not work
COPY FILE1 REPLACING 'AT' BY 'AS' <==does not work
COPY FILE1 REPLACING ==AT== BY ==AS== <==does not work.

this is a cobol/cics program.

please assist, thanks

eric
```

#### ↳ Re: Copy and replace file cobol/cics

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-09-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6092e9bfdf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970912231800.TAA25448@ladder02.news.aol.com>`
- **References:** `<19970912231800.TAA25448@ladder02.news.aol.com>`

```

In article <199··.@lad··l.com>,
BFETML wrote:
› we are working on y2k at work, and i wanted to copy a copylib member i
› also wanted to replace certain words in the copy member.  basically i
…[25 more quoted lines elided]…
› eric


You need to write: COPY FILE1 REPLACING ==:AT:== BY ==AS==.

And then in copybook:
05 :AT:-FIELD1 PIC X.
05 :AT:-FIELD2 PIC X.

The rule here is: COPY replaces words with words.
So COPY FILE1 REPLACING ==AT== BY ==AS==
replaces word AT with word AS, but not
word AT-FIELD1 with word AS-FIELD1.

By adding colons you make AT a word of sorts, and then it works,
because colons allow you to glue the replacement word
to the neighbouring word.

Instead of :AT: you can use (AT) or any other good symbols
(details can found in Cobol standard).


As to doing Y2K transformations, you can achieve much better results
faster if you use CobolTransformer library. It allows you to write arbitrary
code transformations fairly quiclky.

For details look at http://www.siber.com.sct/


Vadim Maslov
```

##### ↳ ↳ Re: Copy and replace file cobol/cics

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-09-16T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6092e9bfdf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6092e9bfdf-p2@usenetarchives.gap>`
- **References:** `<19970912231800.TAA25448@ladder02.news.aol.com> <gap-6092e9bfdf-p2@usenetarchives.gap>`

```

Vadim,

The solution you describe works in COBOL II, not COBOL. The original post
states "copy and replace file cobol/cics" - no mention of COBOL II. I
asked the very same question that Eric is asking several weeks ago. The
responses received stated that the copy and replace never did work as
described in the IBM manuals. I tried many variations with no success.
While the copy and replace did work in IBM COBOL II, I never could get it
to work in COBOL.

Joseph Lenz
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
