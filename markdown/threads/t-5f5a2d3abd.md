[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dear Kaptn cobol

_2 messages · 2 participants · 1997-06_

---

### Dear Kaptn cobol

- **From:** "cobol..." <ua-author-17071858@usenetarchives.gap>
- **Date:** 1997-06-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33a7c020.19036687@news.calypso.net>`

```

Hi
We still have problems with MicroFocus Work Bench and making exe-files
Now we are stuckt on LINKING.
As long as the CBl-file not content no Screen Section or Data-files
there is no problems.
We now try to link *.OBJ
Link filename+extfh+adis,,,lcobol+cobapi/nod/noe

no error message but when running the exe-file
Fail to find adisinit
Run time error :173

/Cobolligan
```

#### ↳ Re: Dear Kaptn cobol

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-06-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5f5a2d3abd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33a7c020.19036687@news.calypso.net>`
- **References:** `<33a7c020.19036687@news.calypso.net>`

```

In message <<33a··.@new··o.net>> cob··.@hot··l.com writes:
› We still have problems with MicroFocus Work Bench and making exe-files
› Now we are stuckt on LINKING.
…[7 more quoted lines elided]…
› Run time error :173

ADISINIT also needs to be linked in, as will ADISKEY:

LINK filename+extfh+adis+adisinit+adiskey,,,lcobol+cobapi/nod/noe;

Will give a standalone .EXE that will run.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
