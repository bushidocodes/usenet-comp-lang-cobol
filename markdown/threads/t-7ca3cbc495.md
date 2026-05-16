[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I write 2 blank lines before printing some output?

_2 messages · 2 participants · 1998-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: How do I write 2 blank lines before printing some output?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74g9vv$ea8@sjx-ixn9.ix.netcom.com>`
- **References:** `<74fm8s$m6h$1@nnrp1.dejanews.com> <366b7221.444303987@news1.ibm.net> <36696e30.15865064@news.sofnet.com>`

```
Ask your instructor or Lab assistant if there are ways to set your terminal
for viewing "FBA" or "FBM" files - paying attention to the "carriage control
characters".

If you can find someone who can help you with this, you should be able to
continue using WRITE AFTER ADVANCING *and* seeing the output on your
terminal as you expect.

Caballito wrote in message <36696e30.15865064@news.sofnet.com>...
>I'm just picking this up, my first class in Cobol is finishing up this
>semester, this very week.   We're using an IBM 9221 Mod. 130 with
…[17 more quoted lines elided]…
>>>I am just learning COBOL, and I want to print out some information, but I
want
>>>to print out two blank lines first.
>>>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: How do I write 2 blank lines before printing some output?

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981208214624.05904.00001849@ngol03.aol.com>`
- **References:** `<74g9vv$ea8@sjx-ixn9.ix.netcom.com>`

```

In article <74g9vv$ea8@sjx-ixn9.ix.netcom.com>, "William M. Klein"
<wmklein@ix.netcom.com> writes:

>If you can find someone who can help you with this, you should be able to
>continue using WRITE AFTER ADVANCING *and* seeing the output on your
>terminal as you expect.

This doesn't work in VSE either, when viewing through ICCF. The ICCF manual
even says it doesn't work. If one wants to see a blank line when displaying a
listing on the terminal, one needs to write a blank line, not use WRITE ...
AFTER ADVANCING 2 LINES, or the equivalent in other languages, either with ASA
carriage control or the machine carriage control character.

Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
