[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Displaying BMP's with Microfocus COBOL

_2 messages · 2 participants · 1996-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Displaying BMP's with Microfocus COBOL

- **From:** "joel fox" <ua-author-16751015@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbca89$5b9a74c0$4668918e@hineman.moh.gov.on.ca>`

```

Is it possible to have a DOS COBOL program display a background from a .BMP
file?

Thanks,

Art McEwen
mce··.@epo··n.ca
```

#### ↳ Re: Displaying BMP's with Microfocus COBOL

- **From:** "soft..." <ua-author-6881452@usenetarchives.gap>
- **Date:** 1996-11-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b181cca2c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbca89$5b9a74c0$4668918e@hineman.moh.gov.on.ca>`
- **References:** `<01bbca89$5b9a74c0$4668918e@hineman.moh.gov.on.ca>`

```

Joel Fox (fo··.@gov··n.ca) wrote:
: Is it possible to have a DOS COBOL program display a background from a .BMP
: file?

Anything is possible.

I doubt you could do this *AND* use text mode console output at the
same time, though. You'd probably have to write the module in C as well
to be able to (easily) parse the BMP file and do low-level DOS VGA
graphics programming (or if you're lucky higher level graphics like
BGI, if you can get them and COBOL to work together).

Of course, I've never done it (and can't imagine why anyone would want
to waste this much time and effort on a *DOS* program) so I don't know
what kind of problems you'd run into.

Scott
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
