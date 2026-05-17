[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Repeated string

_5 messages · 5 participants · 1995-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Repeated string

- **From:** "eeu..." <ua-author-17087893@usenetarchives.gap>
- **Date:** 1995-02-17T20:15:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`

```

ok .. this is a silly RTFM question .. but I don't have a FM .. so I'm gonna
ask here, and probably get flamed for it :-) Here goes ...

I want to create a filler line of N occurances of a certain character or
string .. eg, something like

02 FILLER PIC X(80) VALUE "-"(80).

Which would ( I know it doesn't ) give me a line of 80 -'s

I'm using a compiler on VMS with the /ANSI_FORMAT qualifier.

Thanks in advance ...

~D..

+---------------------------------+------------------------------------------+
| ooo oooo Iain MacDonnell | I.M··.@qub··c.uk oooo ooo |
| o o o 22 Ridgeway St. | dse··.@shi··e.edu o o o |
| o o o Belfast. BT9 5FB | dse··.@sou··o.uk o o o |
| ooo o Northern Ireland | dse··.@mec··c.uk o ooo |
+---------------------------------+------------------------------------------+
| +44 (0) 589 202939 | http://shimoda.cis.temple.edu/~dseven |
+----------------------------------------------------------------------------+

43rd Law of Computing:
Anything that can go wr
fortune: Segmentation violation -- Core dumped
```

#### ↳ Re: Repeated string

- **From:** "john m perry" <ua-author-17087542@usenetarchives.gap>
- **Date:** 1995-02-18T03:47:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcdbb0764e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`
- **References:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`

```
eeu··.@que··c.uk (DSEVEN) wrote:
›
 
› I want to create a filler line of N occurances of a certain character or
› string .. eg, something like
…[3 more quoted lines elided]…
›

pic x(80) value all "-".
```

#### ↳ Re: Repeated string

- **From:** "xylo..." <ua-author-921084@usenetarchives.gap>
- **Date:** 1995-02-18T13:02:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcdbb0764e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`
- **References:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`

```
› I want to create a filler line of N occurances of a certain character or
› string .. eg, something like
…[3 more quoted lines elided]…
› Which would ( I know it doesn't ) give me a line of 80 -'s


Did you ever try:
02 FILLER PIC X(80) VALUE ALL "-".

Bob Evans
Xyl··.@a··.com
```

#### ↳ Re: Repeated string

- **From:** "plo..." <ua-author-964218@usenetarchives.gap>
- **Date:** 1995-02-19T21:34:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcdbb0764e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`
- **References:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`

```
Try this:

02 FILLER PIC X(80) VALUE ALL "-".

This should do it for you.
Pamela J. Loree, CCP

"Square Peg, Round Hole, B-I-G Hammer, No Problem!"
```

#### ↳ Re: Repeated string

- **From:** "diedrich..." <ua-author-17088075@usenetarchives.gap>
- **Date:** 1995-02-22T03:52:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcdbb0764e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`
- **References:** `<1995Feb18.011542.35@queens-belfast.ac.uk>`

```
In article <199··.@que··c.uk>, eeu··.@que··c.uk (DSEVEN) says:
› 
› I want to create a filler line of N occurances of a certain character or
…[4 more quoted lines elided]…
› Which would ( I know it doesn't ) give me a line of 80 -'s

Try 02 filler pic x(80) value ALL "-".

MOVE ALL "-" TO ... should work as well.


:-) Diedrich Ehlerding
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
