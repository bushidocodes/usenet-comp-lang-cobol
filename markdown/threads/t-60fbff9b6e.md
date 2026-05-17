[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Funny COMP-3 Numbers

_3 messages · 3 participants · 1997-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Funny COMP-3 Numbers

- **From:** "jmcelroy" <ua-author-17072033@usenetarchives.gap>
- **Date:** 1997-11-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<345E2197.970B163B@iw.net>`

```

I have source code which states that the following numbers are COMP-3.
Does anyone recognize these as being valid COMP-3 numbers?

Field Format: PIC S9(7)V99

00 00 ba 00 0c
00 01 b5 00 0c
00 01 0a 00 0c
00 01 df 00 0c
```

#### ↳ Re: Funny COMP-3 Numbers

- **From:** "thomas jones" <ua-author-518593@usenetarchives.gap>
- **Date:** 1997-11-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-60fbff9b6e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<345E2197.970B163B@iw.net>`
- **References:** `<345E2197.970B163B@iw.net>`

```

I'm guessing that your source file went through and ASCII/EBCDIC
translator. Checking the handy dandy ASCII/EBCDIC chart in my
MicroFocus Workbench Reference manual I came up with:

ASCII source EBCDIC source HUMAN source
00 00 ba 00 0c 00 00 70 00 0c 0000700.00
00 01 b5 00 0c 00 01 65 00 0c 0001650.00
00 01 0a 00 0c 00 01 25 00 0c 0001250.00
00 01 df 00 0c 00 01 35 00 0c 0001350.00


If my guess was right these are valid comp-3 values.

jmcelroy wrote:
› 
› I have source code which states that the following numbers are COMP-3.
…[7 more quoted lines elided]…
› 00 01 df 00 0c
```

##### ↳ ↳ Re: Funny COMP-3 Numbers

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-60fbff9b6e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-60fbff9b6e-p2@usenetarchives.gap>`
- **References:** `<345E2197.970B163B@iw.net> <gap-60fbff9b6e-p2@usenetarchives.gap>`

```

In <345··.@NOS··i.us>, Thomas Jones writes:
› I'm guessing that your source file went through and ASCII/EBCDIC
› translator.  Checking the handy dandy ASCII/EBCDIC chart in my
…[10 more quoted lines elided]…
› 

You are probably right about the ascii/ebcdic conversion. However,
they are not valid comp-3 items under the ascii column. Comp-3 is
packed decimal which is neither ascii nor ebcdic. Micro Focus comp-3
is the same as IBM mainframe comp-3. Packed decimal is packed
decimal. Micro Focus will recognize this as an invalid value and
it's a sure S0C7 on the mainframe. The only valid packed data above
is under the ebcdic column. If you have packed data that needs to be
downloaded to the PC, do a binary transfer so the data is not
corrupted and then use the Micro Focus Workbench File Loader with a
conversion mask to only convert the ebcdic portions and leave the
packed data alone. Same thing goes for binary data.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
