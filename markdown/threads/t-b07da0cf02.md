[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# copy statement in fujitsu's cobol.net

_5 messages · 4 participants · 2003-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax) · [`Web, XML, modern integration`](../topics.md#web)

---

### copy statement in fujitsu's cobol.net

- **From:** john.mcginnis@eac.edu (John)
- **Date:** 2003-04-03T08:27:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f850cb4.0304030827.6b7cedaa@posting.google.com>`

```
Has anyone tried to use a copy statement in cobol.net?  I get the
following error generated.


JMN1062I-S  COBOL LIBRARY IS NOT ALLOCATED. OR DATA SET ALLOCATED FOR
LIBRARY HAS INVALID ORGANIZATION OR RECORD FORMAT.

copy statements attempted include: 

COPY BSTDWS.

COPY "BSTDWS.LIB".

COPY "BSTDWS".

COPY 'BSTDWS'.

COPY 'BSTDWS.LIB'.

COPY "BSTDWS.CBL".   // AFTER RENAMING LIB TO CBL

COPY 'BSTDWS.CBL'.
```

#### ↳ Re: copy statement in fujitsu's cobol.net

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-03T15:33:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tcacnW-UQJg6NRGjXTWcow@giganews.com>`
- **References:** `<3f850cb4.0304030827.6b7cedaa@posting.google.com>`

```

"John" <john.mcginnis@eac.edu> wrote in message
news:3f850cb4.0304030827.6b7cedaa@posting.google.com...
> Has anyone tried to use a copy statement in cobol.net?  I get the
> following error generated.
…[19 more quoted lines elided]…
> COPY 'BSTDWS.CBL'.

Seems as if the *location* of the copy book is unknown to the compiler.
```

##### ↳ ↳ Re: copy statement in fujitsu's cobol.net

- **From:** gerry.wolfe@sympatico.ca (Gerry Wolfe)
- **Date:** 2003-04-04T14:05:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8d90c7.2423538@news1.on.sympatico.ca>`
- **References:** `<3f850cb4.0304030827.6b7cedaa@posting.google.com> <tcacnW-UQJg6NRGjXTWcow@giganews.com>`

```


Under v4.x... Use the COBOL OPTIONS to specify LIB (and browse to
where the library is located).  Could also be the SRF option... this
one specifies whether the copycode is fixed length, variable length,
etc.

:-)

On Thu, 3 Apr 2003 15:33:29 -0600, "JerryMouse" <nospam@bisusa.com>
wrote:

>
>"John" <john.mcginnis@eac.edu> wrote in message
…[26 more quoted lines elided]…
>
```

#### ↳ Re: copy statement in fujitsu's cobol.net

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-04-05T15:52:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6mn38$ng2$1@reader08.wxs.nl>`
- **References:** `<3f850cb4.0304030827.6b7cedaa@posting.google.com>`

```
Open your project, expand all, right-click properties of scripts (do so for
each form), and provide the compiler with the place of your copybooks. Name
copybooks exactly as they are named on disk. And check your copybooks on
content......A/B region etc.....

"John" <john.mcginnis@eac.edu> schreef in bericht
news:3f850cb4.0304030827.6b7cedaa@posting.google.com...
> Has anyone tried to use a copy statement in cobol.net?  I get the
> following error generated.
…[19 more quoted lines elided]…
> COPY 'BSTDWS.CBL'.
```

##### ↳ ↳ Re: copy statement in fujitsu's cobol.net

- **From:** john.mcginnis@eac.edu (John)
- **Date:** 2003-04-09T11:45:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f850cb4.0304091045.1b56621b@posting.google.com>`
- **References:** `<3f850cb4.0304030827.6b7cedaa@posting.google.com> <b6mn38$ng2$1@reader08.wxs.nl>`

```
Problem solved, thanks to everyone who replied.


"Danny Maijer" <info@liveartists.com> wrote in message news:<b6mn38$ng2$1@reader08.wxs.nl>...
> Open your project, expand all, right-click properties of scripts (do so for
> each form), and provide the compiler with the place of your copybooks. Name
…[26 more quoted lines elided]…
> > COPY 'BSTDWS.CBL'.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
