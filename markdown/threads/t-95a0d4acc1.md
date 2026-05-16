[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie Question: Indexed I-O File Status Error 43

_1 message · 1 participant · 1999-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Newbie Question: Indexed I-O File Status Error 43

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3786090B.92818FCC@IMN.nl>`
- **References:** `<375AB8B4.A3C67AC5@intranet.ca> <3782a32a.21506278@news1.frb.gov>`

```
The Micro Focus NetExpress help file says, about 43:

43	Files in sequential access mode. The last I/O statement executed for
the file, before the execution of a DELETE or REWRITE statement, was not
a READ statement.

Mind the word SEQUENTIAL in this text!! Are your opening the file
sequential and did you not do a read. (F.e. a rewrite immediately after
the open)?

Hope this sets you on the right track to a solution.

The Frog

WDS wrote:
> 
> On Sun, 06 Jun 1999 17:59:35 GMT, Carlos Featherston wrote:
…[16 more quoted lines elided]…
> as being the same record.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
