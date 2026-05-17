[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Dialog System

_2 messages · 2 participants · 1996-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Dialog System

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1996-09-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<324D43A1.22C3@idgonline.no>`

```

I am using Cobol Workbench 4.0 with Dialog System 2.5.64.

I have a couple of problems...!!

Is it possible to trap CURU and CURD in a listbox ???

Is it possible to create context-sensitive help in Dialog System ala
those yellow-windows in other Win '95 programs ??


Any help would be appreciated ..

Tommy Nilsen

tom··.@idg··e.no
```

#### ↳ Re: MicroFocus Dialog System

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1996-09-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aac4b1fa6c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<324D43A1.22C3@idgonline.no>`
- **References:** `<324D43A1.22C3@idgonline.no>`

```

Tommy Nilsen wrote:
› 
› I am using Cobol Workbench 4.0 with Dialog System 2.5.64.
…[12 more quoted lines elided]…
› tom··.@idg··e.no

Heres the comments from one of the developers:

"... the CURU/CURD work on a list box (I haven't tested), but only if
the dialog is on the list box. And I don't recommend using them because
they interfere with ITEM-SELECTED.

As for Win95 context help, this has to be programmed by the user as API
calls (I implemented these for DS v3.0)."

Hope it helps.
Martyn      (m.··.@mfl··o.uk)
Phone: +44 (0)1635 565 358, fax +44 (0)1635 565 567
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
