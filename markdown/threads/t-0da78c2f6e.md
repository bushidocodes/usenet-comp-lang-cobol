[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL /Rebuild / Compressed files

_2 messages · 2 participants · 1995-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL /Rebuild / Compressed files

- **From:** "soft-..." <ua-author-35930@usenetarchives.gap>
- **Date:** 1995-03-18T21:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<135177@cup.portal.com>`

```
Hi, this is something that happened to us, and what we learned
might be useful to to others.

When we issue a release of our software (in MF COBOL) the install
procedure routinely runs REBUILD /D on all the files just for
good measure (our customers are always turning off their PC's
in the middle of transactions and trashing their files).

This time, our first release using Micro Focus COBOL 3.2, we
got complaints from customers that they ran out of disk space
doing the installation, or that the size of the files increased
dramatically.

What we found is that if you run REBUILD /D on a file using
DATACOMPRESS, the output file from REBUILD is not compressed.
We have some fairly sparse files and the increased file size
was 2-3x.

The workaround is to explicitly specify the /c:d1 (or whatever
is appropriate) on the REBUILD command line.

I think that this behavior is different from version 3.1.

Kevin Davidson (QS Inc.)
```

#### ↳ Re: MF COBOL /Rebuild / Compressed files

- **From:** "r..." <ua-author-4509538@usenetarchives.gap>
- **Date:** 1995-03-20T04:21:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da78c2f6e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<135177@cup.portal.com>`
- **References:** `<135177@cup.portal.com>`

```
In message <135··.@cup··l.com> - soft-.··@cup··l.com (Kevin W
Davidson) writes:
› What we found is that if you run REBUILD /D on a file using
› DATACOMPRESS, the output file from REBUILD is not compressed.
…[8 more quoted lines elided]…
› Kevin Davidson (QS Inc.)

This bug is now fixed in an update to 3.2. This only affected the /d option,
so a rebuild infile, outfile would work. Try the 3.2.41 update (as I think
this is the latest).
Roy Harrington (r.··.@mfl··o.uk)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
