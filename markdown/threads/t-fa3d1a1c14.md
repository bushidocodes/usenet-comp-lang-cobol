[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with BTR2XFH alternatives

_2 messages · 2 participants · 1998-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with BTR2XFH alternatives

- **From:** "non_d..." <ua-author-17084396@usenetarchives.gap>
- **Date:** 1998-02-03T11:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<886522406.1755774980@dejanews.com>`

```

We have a Microfocus cobol app that we support on PCs and Unix. On PCs
we use Btrieve, and on unix we use the BTR2XFH interface that routes out
to MF-isam files via the EXTFH module.

We are hitting a problem with the 1 Gig file size limit imposed by EXTFH,
and have recently found out that Microfocus have "frozen" (read
"discontinued") support for BTR2XFH.

Know of any off-the-shelf alternatives? We are currently contemplating
writing our own BTR2XFH equivalent based on a commercial isam package,
such as Informix c-isam, D-isam, Ctree or similar.

If you've come across this problem, and maybe come up with a solution I'd
be keen to share the experience. We have about 2 million lines of code,
and we need to continue support for Btrieve, so we can't really consider
options that require us to touch the source of the application.

If you have something that would work I'm open to commercial propositions.

Thanks in advance

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Help with BTR2XFH alternatives

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fa3d1a1c14-p2@usenetarchives.gap>`
- **In-Reply-To:** `<886522406.1755774980@dejanews.com>`
- **References:** `<886522406.1755774980@dejanews.com>`

```

On Tue, 03 Feb 1998 10:36:56 -0600, non··.@hot··l.com wrote:

› We have a Microfocus cobol app that we support on PCs and Unix. On PCs
› we use Btrieve, and on unix we use the BTR2XFH interface that routes out
› to MF-isam files via the EXTFH module.

Hi

Ã do not remember how you work with the files with EXTFH but
if you do normal OPEN/READ/WRITE/CLOSE you can have a
look at www.rldt.fr.
They hava a product that allows you to connect to Informix or Oracle
or Sybase without messing with the programs.

Best


Frederico Fonseca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
