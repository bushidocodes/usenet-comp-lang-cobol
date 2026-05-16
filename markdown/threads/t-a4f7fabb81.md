[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with Embedded SQL

_4 messages · 4 participants · 1999-06_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### Help with Embedded SQL

- **From:** walkemn <walkemn@email.uc.edu>
- **Date:** 1999-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375D5D82.3697A876@email.uc.edu>`

```
How can I do this.  I have some knowledge of COBOL but it is very
limited.  Any help would be appreciated.

Thanks,
Darren Sloppy
```

#### ↳ Re: Help with Embedded SQL

- **From:** "Doug McKibbin" <dmckib@NOSPAM.goodnet.com>
- **Date:** 1999-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qzpxvotbbqargpbz.fd1ab40.pminews@enews.newsguy.com>`
- **References:** `<375D5D82.3697A876@email.uc.edu>`

```
Use the COBOL SQL API's:
EXEC SQL
   <SQL statement...>
END-EXEC.

On Tue, 08 Jun 1999 14:14:26 -0400, walkemn wrote:

>How can I do this.  I have some knowledge of COBOL but it is very
>limited.  Any help would be appreciated.
…[3 more quoted lines elided]…
>

Regards,
Doug McKibbin
(remove NOSPAM from address when emailing)
```

##### ↳ ↳ Re: Help with Embedded SQL

- **From:** "Timothy Nicholson" <kf4rtx@nospam.arrl.net>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jpq9k$s6d$1@nntp8.atl.mindspring.net>`
- **References:** `<375D5D82.3697A876@email.uc.edu> <qzpxvotbbqargpbz.fd1ab40.pminews@enews.newsguy.com>`

```
and be sure to have a COBOL compiler that can interpret ESQL, or use a
precompiler before running the code through the COBOL compiler.
```

###### ↳ ↳ ↳ Re: Help with Embedded SQL

- **From:** Manfred Niendiek <MNiendiek@T-Online.de>
- **Date:** 1999-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3763A7F6.45E6B59F@T-Online.de>`
- **References:** `<375D5D82.3697A876@email.uc.edu> <qzpxvotbbqargpbz.fd1ab40.pminews@enews.newsguy.com> <7jpq9k$s6d$1@nntp8.atl.mindspring.net>`

```
Timothy Nicholson schrieb:
> 
> and be sure to have a COBOL compiler that can interpret ESQL, or use a
…[3 more quoted lines elided]…
> snip

ultimate answer <vbg>

Manfred
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
