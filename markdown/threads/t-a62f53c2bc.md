[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Listing without compiling

_3 messages · 3 participants · 2002-01_

---

### Listing without compiling

- **From:** Rick DeBow <debow@home.com>
- **Date:** 2002-01-12T06:21:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3FD900.A59A44DB@home.com>`

```
I'm looking for the command to produce a listing of my programs without
compiling them.  I work on a AlphaCluster VMS using XCOBOL.

Any help is greatly appreciated

Rick
```

#### ↳ Re: Listing without compiling

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-01-12T07:24:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0201120724.529e157e@posting.google.com>`
- **References:** `<3C3FD900.A59A44DB@home.com>`

```
Rick,

I've never heard of XCOBOL on VMS - but for DEC COBOL on VMS I use
this:

COBOL/LIST/COPYLIST whatever.COBOL

Now, this DOES do a compile but who cares?  It doesn't link it, and
does give you a full listing with copybooks expanded.


Rick DeBow <debow@home.com> wrote in message news:<3C3FD900.A59A44DB@home.com>...
> I'm looking for the command to produce a listing of my programs without
> compiling them.  I work on a AlphaCluster VMS using XCOBOL.
…[3 more quoted lines elided]…
> Rick
```

##### ↳ ↳ Re: Listing without compiling

- **From:** Jeff Campbell <jcampbell@ins-msi.com>
- **Date:** 2002-01-13T05:37:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C41144D.142F0429@ins-msi.com>`
- **References:** `<3C3FD900.A59A44DB@home.com> <bfdfc3e8.0201120724.529e157e@posting.google.com>`

```
Thane Hubbell wrote:
> 
> Rick,
…[6 more quoted lines elided]…
> Now, this DOES do a compile but who cares?  It doesn't link it, and

Add /NOOBJECT to suppress the compiler's output file:

   COBOL/LIST/COPYLIST/NOOBJECT whatever.COBOL

> does give you a full listing with copybooks expanded.
> 
…[6 more quoted lines elided]…
> > Rick

Jeff
n8wxs@arrl.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
