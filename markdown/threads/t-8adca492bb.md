[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acucobol Byte Stream IO

_5 messages · 4 participants · 2002-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Acucobol Byte Stream IO

- **From:** none@none.com (JF)
- **Date:** 2002-11-04T12:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc66730.3223694@news.earthlink.net>`

```
Anyone know if there are byte stream file io calls available in
Acucobol, such as CBL_OPEN, CBL_READ and CBL_WRITE?  I can't find
anything  in the Acubench manuals.  I don't want the Vision file
system - I'm looking for simple byte stream IO that use system file
handles on W2K.  Microfoucs, Relalia, etc include a complete stream io
library (have done so for years).  I'd rather not have to write C
programs and link them to Acu's runtime,  just to read and write a
stream of bytes to disk.  

Thanks,

JF
```

#### ↳ Re: Acucobol Byte Stream IO

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2002-11-04T22:21:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nTidnW4JvITZpFqgXTWcqQ@comcast.com>`
- **References:** `<3dc66730.3223694@news.earthlink.net>`

```
There are some CBL_* routines listed in the appendix, but none with those
names or capabilities (that I see).

I've always been able to do any file I/O I needed with the standard
OPEN/READ/WRITE, even for OS files, but I can't say I've dealt with every
situation.

Note that you don't necessarily have to link your C routines to the runtime.
You can put them in a DLL can call the DLL, or put the entire sub.c
interface into a DLL.  (I wish they'd do the same thing with the sub85.c
interface - I'd love to stop linking into the runtime, but I need to know
the sizes and types of parameters passed in the CALL.)


"JF" <none@none.com> wrote in message
news:3dc66730.3223694@news.earthlink.net...
> Anyone know if there are byte stream file io calls available in
> Acucobol, such as CBL_OPEN, CBL_READ and CBL_WRITE?  I can't find
…[9 more quoted lines elided]…
> JF
```

#### ↳ Re: Acucobol Byte Stream IO

- **From:** "Fim W���stberg" <fim.wastberg@fimator.se>
- **Date:** 2002-11-05T20:58:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LhWx9.2688$h%5.96181@newsb.telia.net>`
- **References:** `<3dc66730.3223694@news.earthlink.net>`

```

"JF" <none@none.com> skrev i meddelandet
news:3dc66730.3223694@news.earthlink.net...
> Anyone know if there are byte stream file io calls available in
> Acucobol, such as CBL_OPEN, CBL_READ and CBL_WRITE?  I can't find
…[9 more quoted lines elided]…
> JF

Use ORGANIZATION IS RELATIVE and a recordsize of just one byte.
Works fine for me.

Fim W�stberg
```

#### ↳ Re: Acucobol Byte Stream IO

- **From:** "Acucorp" <shaun_gough@hotmail.com>
- **Date:** 2002-11-05T14:03:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DA91646D29C2DF4A85EC32EA1C484BEB237BE1@ras.acucorp.com>`
- **References:** `<3dc66730.3223694@news.earthlink.net>`

```
From ACUCOBOL-GT version 5.2.0, you can use the I$IO library routine to
simulate the CBL_OPEN, CBL_READ etc.

ACUCORP Inc.
8515 Miralani Drive, San Diego, CA 92126, USA
WWW: http://www.acucorp.com/

Want the latest COBOL tips, tricks and information?
Subscribe to the Acucorp newsletter today:
<http://www.acucorp.com/News/Newsletter/subscribe.html>. Acucorp's quarterly
newsletter contains news and solutions, technical advice, product
announcements and much more! For a copy of the latest issue, visit
<http://www.acucorp.com/News/Newsletter/newsletter.html>.

"JF" <none@none.com> wrote in message
news:3dc66730.3223694@news.earthlink.net...
> Anyone know if there are byte stream file io calls available in
> Acucobol, such as CBL_OPEN, CBL_READ and CBL_WRITE?  I can't find
…[9 more quoted lines elided]…
> JF
```

##### ↳ ↳ Re: Acucobol Byte Stream IO

- **From:** none@none.com (JF)
- **Date:** 2002-11-07T01:55:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc9c56a.3575956@news.earthlink.net>`
- **References:** `<3dc66730.3223694@news.earthlink.net> <DA91646D29C2DF4A85EC32EA1C484BEB237BE1@ras.acucorp.com>`

```
On Tue, 5 Nov 2002 14:03:33 -0800 , "Acucorp"
<shaun_gough@hotmail.com> wrote:

>From ACUCOBOL-GT version 5.2.0, you can use the I$IO library routine to
>simulate the CBL_OPEN, CBL_READ etc.
>

Thanks.  Calling a file handler designed for indexed files wasn't
what I had in mind.  I'll call C++ library routines directly and link
the call map into Acucobol's runtime, but I was hoping to avoid the
support issue this solution creates ... for the client's sake.

JF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
