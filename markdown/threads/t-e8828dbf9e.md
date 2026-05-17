[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ansi error code

_3 messages · 3 participants · 1996-11_

---

### Ansi error code

- **From:** "darrel gutierrez" <ua-author-17087037@usenetarchives.gap>
- **Date:** 1996-11-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<327FBFB3.7CC@hitechworld.com>`

```

Does anyone know what an ansi return code = 47 means? I can't reference
materials on the net.
```

#### ↳ Re: Ansi error code

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8828dbf9e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<327FBFB3.7CC@hitechworld.com>`
- **References:** `<327FBFB3.7CC@hitechworld.com>`

```

Darrel Gutierrez wrote:
›
› Does anyone know what an ansi return code = 47 means? I can't reference
› materials on the net.

It means "The execution of a READ or START statement is attempted
referencing a file connector that is not open in the input or I-O
mode.".

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Ansi error code

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8828dbf9e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<327FBFB3.7CC@hitechworld.com>`
- **References:** `<327FBFB3.7CC@hitechworld.com>`

```

In article <327··.@hit··d.com>, dar··.@hit··d.com says...
›
› Does anyone know what an ansi return code = 47 means? I can't referenc
› e
› materials on the net.

I'm not sure, but it appears you are referring to an Ansi File Status
value rather than return-code value. A file status 47 means "The
execution of a WRITE statement was attempted on a file not open in the
input or I-O mode". I have never seen references to Ansi return-code
values. If this is not a file status code, the program could be setting
the Return-Code Special register, in which case it could mean anything
the programmer intended.

mike dodas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
