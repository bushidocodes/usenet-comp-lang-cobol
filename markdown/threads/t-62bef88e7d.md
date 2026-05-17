[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Compiler Question

_4 messages · 4 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Compiler Question

- **From:** "dt..." <ua-author-7376421@usenetarchives.gap>
- **Date:** 1996-12-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a76do$k1d@camel0.mindspring.com>`

```

This should be easy ...

Does the MF compiler, specifically version 3.1.35, exclude
coding/paragraphs that aren't used from the final executable? I never
really noticed until tonight ... I was recoding an application and
removed several hundred lines of coding that were no longer used, and
the resulting .EXE wasn't any smaller. I was very upset by this, at
first, and then thought, well, maybe the compiler is optimizing the
coding, like Borland's C++ and Delphi compilers do, and it's excluded
unused paragraphs from the final .EXE. This would be great if it's
doing that. Would save me some time. I have the compiler directive
OPT set to 1 for normal optimization (doesn't really go into what
"normal" is).

Let me know what you know (or think). Just post to this NG.

Thanks.
D.

Todays motto: When all else fails, read the manual. When you wake up,
ask a friend for help.
```

#### ↳ Re: MF Compiler Question

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-12-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-62bef88e7d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5a76do$k1d@camel0.mindspring.com>`
- **References:** `<5a76do$k1d@camel0.mindspring.com>`

```

I don't know the answer but I suspect it's true. Here's why. We did an
experment with a very large application that "Performed" all file I-O .
There was a read paragraph, a write paragraph, etc. We removed the
performs and put the paragraphs in line, thus increasing the code
dramatically. The code segment and data segment size of the compiled code
was the same.


Douglas Troy wrote in article
<5a76do$k.··.@cam··g.com>...
› This should be easy ...
› 
…[22 more quoted lines elided]…
›
```

##### ↳ ↳ Re: MF Compiler Question

- **From:** "ro..." <ua-author-6589469@usenetarchives.gap>
- **Date:** 1996-12-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-62bef88e7d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-62bef88e7d-p2@usenetarchives.gap>`
- **References:** `<5a76do$k1d@camel0.mindspring.com> <gap-62bef88e7d-p2@usenetarchives.gap>`

```

On 30 Dec 1996 14:42:04 GMT, "Thane Hubbell" wrote:

Well it is true, and as the matter of fact, it is a verry good
optimizer. If you want to test it, compile for gnt with ANIM and GANIM
directives, and then use xilarator (xil) and step throught the
programm. You will be supprized with the optimazisation. Try to see
the code with assembly also (F8 I think).

Happy new year !!!

› I don't know the answer but I suspect it's true.  Here's why.  We did an
› experment with a very large application that "Performed" all file I-O . 
…[32 more quoted lines elided]…
›› 


I.Ioannou (ro··.@com··k.gr)
```

#### ↳ Re: MF Compiler Question

- **From:** "mike childers" <ua-author-6588922@usenetarchives.gap>
- **Date:** 1996-12-31T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-62bef88e7d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5a76do$k1d@camel0.mindspring.com>`
- **References:** `<5a76do$k1d@camel0.mindspring.com>`

```

When you are using MF, the obj code created is very small, MF adds a lot
to handle the PC environment (so do other languages). I have written both
'C' and
MF Cobol program that did the same function. I had 27K more in the exe in
Cobol than I had in my 'C' program. This is not true in all cases. 100
lines of Cobol code is not a big deal, now if you erased 1000 lines you
might see changes.

Do not give up on Cobol, it is a fair PC language! Not great but fair!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
