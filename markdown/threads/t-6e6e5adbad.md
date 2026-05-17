[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question: The ebcdic code for tab and CR.

_2 messages · 2 participants · 1998-03_

---

### Question: The ebcdic code for tab and CR.

- **From:** "irene jacobsen" <ua-author-17074419@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd4ea0$235bbaf0$c7017a94@fou-lm-11059>`

```

Hey. :-)
I want to produce a file in MVS, that i am going to transfer to unix.

In that job i am interested in knowing the ebcdic code that transfers to
the right ascii-code for:
Tab key
CR (return) key

Can you help me?

Thanks in advance. :-)

Irene Jacobsen
Telenor FoU, Lillehammer.
```

#### ↳ Re: Question: The ebcdic code for tab and CR.

- **From:** "andreas..." <ua-author-7951989@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6e6e5adbad-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd4ea0$235bbaf0$c7017a94@fou-lm-11059>`
- **References:** `<01bd4ea0$235bbaf0$c7017a94@fou-lm-11059>`

```

On 13 Mar 1998 16:50:27 GMT, "Irene Jacobsen"
wrote:

› Hey. :-)
› I want to produce a file in MVS, that i am going to transfer to unix.
…[5 more quoted lines elided]…
› 
I converted these with "realcopy" from ASCII-codes to EBCDIC .

TAB : x"09" --> x"05"
CR : x"0D" --> x"0D"

Try it.

Andy
----------------
Andreas Beckmann
And··.@mue··r.de
http://www.muenster.de/~andy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
