[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed Files question

_2 messages · 2 participants · 1997-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed Files question

- **From:** "ell e tweedy" <ua-author-12405789@usenetarchives.gap>
- **Date:** 1997-10-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34438dfc.0@news.cc.umr.edu>`

```


Hello...

If I remember correctly, indexed files are stored in two files, the
.idx file with the index and another file with the actual data.

Does anyone know what the format of .idx file is?
I don't have a copy of the ANSI standard or any other refernece which
has this information. I'm writing a Cobol to C translator for a
semester project.

I'm assuming that the .idx is a tree of some kind? I can make my own format
for the time being, but I'd rather be compatible with the standard, if
there is one for indexed file formats.

Thanks!
laura
Laura Tweedy :: twe··.@u··.edu
   Peacefully discovering
  the path I wish to take...
```

#### ↳ Re: Indexed Files question

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c70d0af0d1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34438dfc.0@news.cc.umr.edu>`
- **References:** `<34438dfc.0@news.cc.umr.edu>`

```

Sounds like you're talking about Micro Focus COBOL ISAM files. I think you
will find that such details are very implementer specific. In the case of
Micro Focus, the format of the IDX file is specified (among several
possible), by the IDXFORMAT compiler directive. Would it not be simpler to
just dump the data out in a form easy to convert into another keyed access
system like Btrieve, which is easy to use in C? If it is within the
project requirements, you can specify the MF COBOL compiler option to use
Btrieve as the ISAM file format. Then both COBOL and C programs could
easily access the same physical file. Building indexed access code into
someone else's file format is a non-trivial exercise. :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
