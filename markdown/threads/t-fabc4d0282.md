[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol V4.5 XMS and size of OBJ

_2 messages · 2 participants · 1996-04_

---

### Cobol V4.5 XMS and size of OBJ

- **From:** "paulo pinto" <ua-author-5516128@usenetarchives.gap>
- **Date:** 1996-04-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3175607B.3408@grupo.bfe.pt>`

```
Hi everybody,

I would like to know if you have the answer to the following:

I need to use extended memory with COBOL Microsoft 4.5. I think I need
XM utility. Is that true?

Another problem is:

I was using before Level II Cobol V2.6 Micro Focus and all my aplication
took about 1.5 Mb. Now, with Cobol V4.5 Microsoft the same aplication
takes near 10 Mb of disk space. The size of .OBJ files is now very big.
I used the minimum link parameters. Is there any chance to make the .OBJ
files smaller ?

Thanks
Paulo Pinto
```

#### ↳ Re: Cobol V4.5 XMS and size of OBJ

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-04-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fabc4d0282-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3175607B.3408@grupo.bfe.pt>`
- **References:** `<3175607B.3408@grupo.bfe.pt>`

```
In message <<317··.@gru··e.pt>> Paulo Pinto writes:
› 
› I would like to know if you have the answer to the following:
…[3 more quoted lines elided]…
› 
 
› XM will cater for extended memory usage, yes.
 
› Another problem is:
› 
…[4 more quoted lines elided]…
› files smaller ?

It is likely that the Level II compiled to .INT files which are
tokenised p-code rather than actual object code. There was a
separate generator that turned these .INT to .GNT executable code
which were somewhat larger but faster.

The default of MS Cobol 4.5 is generated object code. Use OPT(0)
to create the equivalent of a .INT file. This will save disk
space but will be slower to execute. Whether this is significant
or not depends on the amount of I-O done.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
