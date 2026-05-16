[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 2000 pointers to functions/procedures?

_1 message · 1 participant · 2001-02_

---

### Re: COBOL 2000 pointers to functions/procedures?

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-02-28T05:09:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97iivt$1h3k$1@news.hitter.net>`
- **References:** `<GKSm6.27273$B5.178761@typhoon.bart.nl>`

```

Ronald wrote in message ...
>
>Does the upcoming COBOL standard provide support for pointers to functions?
>(as in: PERFORM function-pointer)

Not "as in" PERFORM.

Not for COBOL functions or COBOL procedures.

COBOL functions are always invoked in-line. COBOL
procedures are, by definition, paragraphs or sections.

There is a USAGE PROGRAM-POINTER. This pointer may
be set to the address of a COBOL program or non-COBOL
procedure or function. The CALL statement is used to
transfer control to the program (or non-COBOL routine), as in:

    CALL program-pointer-1
        [USING arg-1 ...] [RETURNING arg-2].
------------------
Rick Smith
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
