[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Large File Sizes for unix Server Express 2.0

_2 messages · 2 participants · 2002-09 → 2002-10_

---

### Large File Sizes for unix Server Express 2.0

- **From:** mike_smith54@hotmail.com (Mike_Smith)
- **Date:** 2002-09-30T10:52:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7de328f0.0209300952.20b0fd96@posting.google.com>`

```
Hi guys, having trouble reading into a cobol program a file that is >
2Gb, and all our techy guys have gone home!

Cobol is Server Express 2.0., unix is SunOS 5.8

Do any of you know if theres a way to get the cobol to take the larger
file size??

Thanks,
```

#### ↳ Re: Large File Sizes for unix Server Express 2.0

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-10-01T00:08:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gI5m9.265349$Jo.116082@rwcrnsc53>`
- **References:** `<7de328f0.0209300952.20b0fd96@posting.google.com>`

```
Look at chapter 6 -- File Handling Configuration.

Striping might be an option for you. Or (preferably) IDXFORMAT(8).

Gazaloo.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
