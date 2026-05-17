[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF setting environment MFP23D

_2 messages · 2 participants · 1997-02_

---

### MF setting environment MFP23D

- **From:** "fernando kvistgaard" <ua-author-6588930@usenetarchives.gap>
- **Date:** 1997-02-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc1373$eed16b80$0a03010a@FEK.LR.DK>`

```

Where can I read in the MF cobol manuals how to set MFP23D environment ON?

SET MFP23D=ON ???????????
```

#### ↳ Re: MF setting environment MFP23D

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1997-02-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8d3aeac53-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc1373$eed16b80$0a03010a@FEK.LR.DK>`
- **References:** `<01bc1373$eed16b80$0a03010a@FEK.LR.DK>`

```

"Fernando Kvistgaard" wrote:
› Where can I read in the MF cobol manuals how to set MFP23D environment ON?
›
› SET MFP23D=ON ???????????

I'm not sure exactly where in the docs you can find it, but setting
the environment variable MFP23D=Anything will cause all Micro Focus
Panels version 2 programs started with this environment variable set
to create it's (Panels2's) controls and windows with a 3D style.

Under 16bit and Windows NT 3.x, this means taking advantage of the
CTL3D(V2)/CTL3D32 DLLs that are shipped with many products.

Under Windows95 and Windows NT 4.x, this means taking advantage of the
native 3D support from the operating system.

The environment variable does not apply to other operating systems.

In preference, it is better to use the flag P2I-CTL3D on Pf-Initialize,
as this gives you control of individual programs.

The control creation flag P2G-IGNORE3D can also be used to switch off
the 3D effect for individual controls.

Hope this helps,
Steve.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
