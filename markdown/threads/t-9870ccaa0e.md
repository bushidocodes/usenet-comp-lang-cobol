[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF file compression

_3 messages · 3 participants · 2000-02_

---

### MF file compression

- **From:** john_barrie@my-deja.com
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87q5p9$7jd$1@nnrp1.deja.com>`

```
Can someone help with the different levels of file compression
available on MF ISAM files, i.e what the real diffs are between each of
the levels 1-7?

Also, I'd be grateful if anyone's had any experience with 'mix and
match' compression levels on .DAT and .DAT.idx files, e.g. one level on
the DAT, and anoither on the idx ?


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: MF file compression

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38a0ebf1.11281393@news.freewwweb.com>`
- **References:** `<87q5p9$7jd$1@nnrp1.deja.com>`

```
On Tue, 08 Feb 2000 22:36:26 GMT, john_barrie@my-deja.com wrote:

>Can someone help with the different levels of file compression
>available on MF ISAM files, i.e what the real diffs are between each of
>the levels 1-7?
>

I've mixed index and data compressions before with good results.  As I
recall 7 combines the most algorythms.  But I always had to look in
the manual for what the different levels mean.  It's in the books,
clearly laid out.  One is for zero suppression.  Another for blank
suppression, etc.  I usually had the best results with Index
compression 1 and data compression 7.
```

##### ↳ ↳ Re: MF file compression

- **From:** jgill_1@my-deja.com
- **Date:** 2000-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87t59g$c7s$1@nnrp1.deja.com>`
- **References:** `<87q5p9$7jd$1@nnrp1.deja.com> <38a0ebf1.11281393@news.freewwweb.com>`

```


On my system, I added the following to the COBOL.DIR file:
DATACOMPRESS"1"
KEYCOMPRESS"7"

This works good for me. If you have alternate keys that are
often blank, I add the line "SUPPRESS WHEN SPACES" when describing
the key in the select statement.




In article <38a0ebf1.11281393@news.freewwweb.com>,
  thaneH@softwaresimple.com (Thane Hubbell) wrote:
> On Tue, 08 Feb 2000 22:36:26 GMT, john_barrie@my-deja.com wrote:
>
> >Can someone help with the different levels of file compression
> >available on MF ISAM files, i.e what the real diffs are between each
of
> >the levels 1-7?
> >
…[8 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
