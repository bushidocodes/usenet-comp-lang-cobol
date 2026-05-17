[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol - File Descriptions

_5 messages · 4 participants · 1997-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Cobol - File Descriptions

- **From:** "douglas t. pavik" <ua-author-2364249@usenetarchives.gap>
- **Date:** 1997-09-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bccced$e2518500$0a72d9cd@pcport>`

```

Is there a way to extract the field descriptions and sizes from a datafile
and/or its corresponding .idx?

Thanks
```

#### ↳ Re: MicroFocus Cobol - File Descriptions

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-73ecfae5c5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bccced$e2518500$0a72d9cd@pcport>`
- **References:** `<01bccced$e2518500$0a72d9cd@pcport>`

```

Douglas T. Pavik wrote in article
<01bccced$e2518500$0a72d9cd@pcport>...
› Is there a way to extract the field descriptions and sizes from a
› datafile
› and/or its corresponding .idx?
› 
› Thanks
Actually, if you want the field descriptions, look in the INT file. That
is where a number of MFs own products (like the data file conversion
utilities) extract them from. Of course, this means you are going back to
a program, not the file itself, but any program with the record
layout/structure in it will have this. In particular, if you have the INT
but not the source you should be able to find it. I do not know whether it
is also in the GNT, but I really doubt it, as that is much closer to
machine code.

There is limited information about the file in it's headers, for some of
the file organizations. Since this is documented in the manuals, you
probably already know that. Beyond simple things like the file type, key
position/length, and overall record length, you are probably out of luck
from that source.
```

##### ↳ ↳ Re: MicroFocus Cobol - File Descriptions

- **From:** "douglas t. pavik" <ua-author-2364249@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-73ecfae5c5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-73ecfae5c5-p2@usenetarchives.gap>`
- **References:** `<01bccced$e2518500$0a72d9cd@pcport> <gap-73ecfae5c5-p2@usenetarchives.gap>`

```

Thanks. I have datafiles but no source FD's. I'll try the INT files if they
are distributed with the gnt's.

Doug.

Gary Lee wrote in article
<01bccd50$92d5e3a0$2b8··.@gle··l.com>...
› Douglas T. Pavik  wrote in article
› <01bccced$e2518500$0a72d9cd@pcport>...
…[23 more quoted lines elided]…
›
```

#### ↳ Re: MicroFocus Cobol - File Descriptions

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-73ecfae5c5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bccced$e2518500$0a72d9cd@pcport>`
- **References:** `<01bccced$e2518500$0a72d9cd@pcport>`

```

On 29 Sep 1997 15:39:35 GMT, "Douglas T. Pavik"
wrote:

› Is there a way to extract the field descriptions and sizes from a datafile
› and/or its corresponding .idx?

no. get the original docs, or guesstimate.
it's my guess the idx field only sorts according to a specific
location, and does not store the field name anywhere. but it probably
does store the field size. at least, that's how i would do it if i
were writing a B-Tree.
```

#### ↳ Re: MicroFocus Cobol - File Descriptions

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1997-09-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-73ecfae5c5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bccced$e2518500$0a72d9cd@pcport>`
- **References:** `<01bccced$e2518500$0a72d9cd@pcport>`

```

Douglas T. Pavik wrote:
›
› Is there a way to extract the field descriptions and sizes from a datafile
› and/or its corresponding .idx?
›
› Thanks

As far as I know (Not very far admittedly !!!) the only information of
this type stored in the .idx is likely to be the location and size of
the keys. There won't be any descriptive information in these .idx
files.

I am basing this assumption upon the fact that as long as the key
location and size is the same, you can read a file with an FD that
doesn't contain any of the same field description information.

This goes for the data (as opposed to key) information as well.

Mike.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
