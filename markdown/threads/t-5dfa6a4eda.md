[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol web language?

_3 messages · 3 participants · 2002-07_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Cobol web language?

- **From:** irgendein@gmx.net (Roger Schmid)
- **Date:** 2002-07-20T10:59:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahbfqq$s1p$1@rex.ip-plus.net>`

```
Hy,

Just for fun and to learn more about cobol:

Is there a way to run cobol together with apache on a linux box?
Actually PHP does the work, so it's might possible to replace PHP with
cobol. I have found cobolscript, but IMHO you have to pay for that. 

May I haven't seen any hints in your faq.

   thanks,
    Roger
```

#### ↳ Re: Cobol web language?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-21T08:22:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D3A6150.1102FB4F@Azonic.co.nz>`
- **References:** `<ahbfqq$s1p$1@rex.ip-plus.net>`

```
Roger Schmid wrote:
> 
> Is there a way to run cobol together with apache on a linux box?
> Actually PHP does the work, so it's might possible to replace PHP with
> cobol. I have found cobolscript, but IMHO you have to pay for that.

All that is required for CGI is that the program be able to read from
stdin, write to stdout and read environment variables.  Many Cobols can
do this.  There are some callable routines that will hide the mechanism
involved but these are not necessary as it should be possible with
ACCEPT and DISPLAY.

I have Cobol code that will work with several web servers on various
OSes, including Linux/Apache.

Go to Google comp.lang.cobol in thread "How I can get the request query
string?".

However this is for MF and there may be some differences required for
other compilers.

CobolScript is not quite Cobol but similar.  It does do CGI easily and
is only $50.
```

#### ↳ Re: Cobol web language?

- **From:** "Paul Barnett" <paul.barnett@microfocus.nospam.com>
- **Date:** 2002-07-22T12:04:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahgscq$5hg$1@hyperion.eu.merant.com>`
- **References:** `<ahbfqq$s1p$1@rex.ip-plus.net>`

```
Micro Focus COBOL can do this.

The products are Net Express on Windows, Object COBOL Developer Suite on
Linux and Server Express on the Unix platforms.

See www.microfocus.com

"Roger Schmid" <irgendein@gmx.net> wrote in message
news:ahbfqq$s1p$1@rex.ip-plus.net...
> Hy,
>
…[9 more quoted lines elided]…
>     Roger
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
