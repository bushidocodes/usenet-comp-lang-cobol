[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with segmenting cobol programs

_4 messages · 3 participants · 1998-04_

---

### Problems with segmenting cobol programs

- **From:** "cares" <ua-author-14538431@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hkugm$5h1$1@news.itis.com>`

```

Can anyone suggest a good way of breaking up a huge cobol program into
smaller segments so I can compile it on Realia workbench. The workbench is
16-bit so can't compile my mainframe applications which are usually greater
than 64 K.
```

#### ↳ Re: Problems with segmenting cobol programs

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8e98bdb0b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6hkugm$5h1$1@news.itis.com>`
- **References:** `<6hkugm$5h1$1@news.itis.com>`

```

Cares wrote:
› 
› Can anyone suggest a good way of breaking up a huge cobol program into
› smaller segments so I can compile it on Realia workbench. The workbench is
› 16-bit so can't compile my mainframe applications which are usually greater
› than 64 K.

Number the sections and Realia can compile, or - they have a compile
time switch (My book is at home) that will allow it. Look for /X I
think. Anyone remember?
```

#### ↳ Re: Problems with segmenting cobol programs

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8e98bdb0b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6hkugm$5h1$1@news.itis.com>`
- **References:** `<6hkugm$5h1$1@news.itis.com>`

```

Cares wrote:
› Can anyone suggest a good way of breaking up a huge cobol program into
› smaller segments so I can compile it on Realia workbench. The workbench is
› 16-bit so can't compile my mainframe applications which are usually greater
› than 64 K.


I can't speak for Realia, but Micro Focus COBOL has segmenting options.
Does Realia support segmenting by section number? Traditionally, sections
were added to COBOL to facilitate defining 'overlays' for segmentation. If
you use sections with section numbers, all sections with numbers above some
value (which you might be able to specify in the Environment Division) would
be overlaid, and all sections with numbers below that value would be always
resident. Non-contiguous sections with the same level number would be
overlaid together. If this technique is used, be careful about performs of
one overlay from another overlay, or situations where one overlay performs
resident code which performs another overlay, then exits back to the first
overlay. Not all compilers handle all of these situations as you might
expect or want.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove numbers from email id to respond)
```

#### ↳ Re: Problems with segmenting cobol programs

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8e98bdb0b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6hkugm$5h1$1@news.itis.com>`
- **References:** `<6hkugm$5h1$1@news.itis.com>`

```

Cares wrote:
› 
› Can anyone suggest a good way of breaking up a huge cobol program into
› smaller segments so I can compile it on Realia workbench. The workbench is
› 16-bit so can't compile my mainframe applications which are usually greater
› than 64 K.

Sorry I took so long, but I have an answer.

To do this without modifying source code, use the HC: compiler
directive.

Use HC:9999 replacing 9999 with the number of verbs to count. Once this
count is reached the NEXT paragraph will go into the NEXT code segment.
Once Realia reaches it's limit of code segmennts, it starts over, adding
the next set to the first generated code segment, then the second and so
on.

This can work, (I used it once, but revereted to assigning my own
section numbers) but it is very inefficient.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
