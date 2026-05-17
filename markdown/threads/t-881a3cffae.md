[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol

_2 messages · 2 participants · 1996-11_

---

### Cobol

- **From:** "wend..." <ua-author-17087396@usenetarchives.gap>
- **Date:** 1996-11-15T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00001a84+000018a5@msn.com>`

```

Does anyone out there know what a multiple point entry tecnique in
COBOL? It goes along with the CALL statment!!???
```

#### ↳ Re: Cobol

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-11-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-881a3cffae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<00001a84+000018a5@msn.com>`
- **References:** `<00001a84+000018a5@msn.com>`

```

GWENDOLYN BARNHART wrote:
›
› Does anyone out there know what a multiple point entry tecnique in
› COBOL? It goes along with the CALL statment!!???

In standard COBOL there are no multiple entry points. Some
implementations have added extensions for this. It is like being able
to specify PROCEDURE DIVISION USING ... in multiple places in a
program (each one has a different namt). It is the antithesis of good
structured programming and should be avoided at all costs. If you
want to do something like that, include a parameter that tells the
program which path to take. That way a reader of the program can tell
what it is actually doing.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
