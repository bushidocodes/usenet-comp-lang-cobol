[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compilation and/or Linkage option for COBOL/370 ?

_2 messages · 2 participants · 1998-05_

---

### Compilation and/or Linkage option for COBOL/370 ?

- **From:** "young-hak, lee" <ua-author-17084302@usenetarchives.gap>
- **Date:** 1998-05-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6j8uvm$a4d$1@hiline.shinbiro.com>`

```

Hello everibody,

I'm using Cobol/370 under MVS/ESA, and I'd like to get assembly coded output
as a result
of compilation/linkage procedure.

I remember, about 7 years ago when we were under IBM VS/COBOL and VSE/SP,
we could get it using // OPTION CATAL,LISTX , but I can't find any idea
under MVS
which compilation/linkage option should be used because we don't have ant
reference book.

Any comment would be appreciated.

Thanks in advance.

Young,
```

#### ↳ Re: Compilation and/or Linkage option for COBOL/370 ?

- **From:** "david ingoldsby" <ua-author-17084108@usenetarchives.gap>
- **Date:** 1998-05-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bebd09e39-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6j8uvm$a4d$1@hiline.shinbiro.com>`
- **References:** `<6j8uvm$a4d$1@hiline.shinbiro.com>`

```

The LIST option gives a full assembler listing. Put PROCESS LIST as the
first line of your program.

David Ingoldsby

› Hello everibody,
› 
…[17 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
