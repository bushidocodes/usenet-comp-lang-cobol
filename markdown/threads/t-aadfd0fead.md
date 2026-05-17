[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# C/C++ for MVS

_2 messages · 2 participants · 1997-02 → 1997-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### C/C++ for MVS

- **From:** "jeff nebeker" <ua-author-15044223@usenetarchives.gap>
- **Date:** 1997-02-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<331524C7.64FE@seanet.com>`

```

I'm using IBM's C/C++ for MVS... Anybody know how to call from Cobol
and/or pass params or structs?

Thank you.

Jeff Nebeker

jne··.@sea··t.com
http://www.seanet.com/~jnebeker
```

#### ↳ Re: C/C++ for MVS

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-03-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aadfd0fead-p2@usenetarchives.gap>`
- **In-Reply-To:** `<331524C7.64FE@seanet.com>`
- **References:** `<331524C7.64FE@seanet.com>`

```

Jeff Nebeker wrote:

› I'm using IBM's C/C++ for MVS... Anybody know how to call from Cobol
› and/or pass params or structs?
 
› Thank you.
 
› Jeff Nebeker
 
› jne··.@sea··t.com
› http://www.seanet.com/â€¾jnebeker

Check out "Advanced MVS JCL Examples: Using MVS/ESA on the Job" by
James G. Janossy, ISBN 0-471-30990-7. Hint: use BINARY with your
"CALL '' USING " in COBOL and
"#pragma linkage( , COBOL )" with your "void ( struct bucket *parm)" in the C program.

Good luck,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
