[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL reconstruction

_2 messages · 2 participants · 1995-02_

---

### COBOL reconstruction

- **From:** "colin..." <ua-author-5711152@usenetarchives.gap>
- **Date:** 1995-02-17T18:06:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8A3C006.09D20005BA.uuout@almac.co.uk>`

```
› Not so long ago, I even reconstructed a lost COBOL source program f
› dump, much to the astonishment of the rest of the department.

JT> Did I read this right? You reconstructed a COBOL program out of thi
JT> air and machine code? Please share your technique with the rest of
JT> us.

OK, I admit it. I exaggerated a bit. There was a listing of an earlier
version, but a few lines had been changed.

The diagnostic tool had a dis-assembler to show the machine code as an
assembler instruction which helped. Straightforward code fragments are
easy if you can code BAL. For PERFORMs and other difficult things you
can compare other parts of the program that match the old listing.

Fortunately, it was fairly simple code, and the whole program was quite
small so was not difficult to re-key. Then compile the program with a p-
map and compare to the original dump.

Then when everyone was happy, modify the program to stop it dumping!
---
* RM 1.3 00712 * Fools rush in where fools have been before.
```

#### ↳ Re: COBOL reconstruction

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-02-19T17:46:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9aac2edf56-p2@usenetarchives.gap>`
- **In-Reply-To:** `<8A3C006.09D20005BA.uuout@almac.co.uk>`
- **References:** `<8A3C006.09D20005BA.uuout@almac.co.uk>`

```
At least in the case of IBM mainframe COBOL, the code is VERY stylized
(that's why people have successfully been able to post-optimize the
generated code). Especially if the code has NOT been post-optimized, it
is certainly practical though painstaking to reconstruct COBOL source
from object code. Of course names would be gone, unless you have some
additional information source (such as symbol tables for a dynamic
debugger), or, as mentioned in an earlier reply, an earlier version
of the program.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
