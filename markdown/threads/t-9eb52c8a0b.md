[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol compiler-linker

_2 messages · 2 participants · 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Cobol compiler-linker

- **From:** "m.daemen" <ua-author-17071477@usenetarchives.gap>
- **Date:** 1997-08-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5t47ma$hof$1@xenon.inbe.net>`

```

I have a problem with linking Cobol programs with cobol650.
After compiling my source(COB file), I try to link this compiled file with
a MS DOS linker. But this linker indicates : Unvalid Object File.
Is the problem my linker or my Object file ( I make the COB files with the
MS DOS editor,maybe one needs another editor to make COB source files)

Miriam

m.d··.@clu··t.be
```

#### ↳ Re: Cobol compiler-linker

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-08-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eb52c8a0b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5t47ma$hof$1@xenon.inbe.net>`
- **References:** `<5t47ma$hof$1@xenon.inbe.net>`

```

M.Daemen wrote:
› 
› I have a problem with linking Cobol programs with cobol650.
…[3 more quoted lines elided]…
› MS DOS editor,maybe one needs another editor to make COB source files)

Hi Miriam

You should run the compiler using the COB file as input and you should
get an object program as output, possibly with the suffix of OBJ. It is
this object file that you should pass to the linker.

+----------+ +--------+
COB ---> | COMPILER | ---> Object (OBJ) ---> | LINKER | ---> EXE
+----------+ +--------+

I hope this is helpful

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
