[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Failure of a SORT

_2 messages · 2 participants · 1997-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Failure of a SORT

- **From:** "irwin, jason" <ua-author-3355871@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<199711121047.KAA12764@hgty.capgemini.co.uk>`

```

I have received a rather curious error message and I am having some
'fun' trying to nail the problem down. I have one theory which I was
hoping some one could confirm or deny.

A SORT command failed, with the error message 'There was an invalid
attempt to end a sort or merge'. I am wondering if this could be caused
by the INPUT PROCEDURE executing a STOP RUN. Obviously this could only
be the case if the INPUT PROCEDURE is actually considered to be part of
the SORT, unfortunately my college text book doesn't go into enough
detail.

Does anyone have any ideas? Thanks in advance

I apologise is this is a duplicate post, I appear to be having some
access problems.

Jason Irwin, Junior Programmer, Cap Gemini (UK)
Ban Spam!
```

#### ↳ Re: Failure of a SORT

- **From:** "scottp4-remove..." <ua-author-2777696@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a17d3ea1b9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<199711121047.KAA12764@hgty.capgemini.co.uk>`
- **References:** `<199711121047.KAA12764@hgty.capgemini.co.uk>`

```

"Irwin, Jason" wrote:

› I have received a rather curious error message and I am having some
› 'fun' trying to nail the problem down.  I have one theory which I was
…[8 more quoted lines elided]…
› 

If the input procedure includes the STOP RUN statement then the output
phases of the sort are never executed. This would result in a SORT
error such as you describe. You'll get a non-zero return code any time
that the SORT is terminated before the last record is returned and the
EOF condition is raised.

Scott Peterson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
