[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress 3.0 NOTRICKLE directive

_2 messages · 2 participants · 2002-10_

---

### NetExpress 3.0 NOTRICKLE directive

- **From:** rondos@zahav.net.il (davidc)
- **Date:** 2002-10-06T08:50:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a5699b5.0210060750.c3e3c70@posting.google.com>`

```
I try to compile various programs with NOTRICKLE directive and always
receive the message "notrickle - rejected".

No matter where I put this directive (source, command line, directives
file) the compiler rejects it.

Maybe somebody knows why?
```

#### ↳ Re: NetExpress 3.0 NOTRICKLE directive

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-10-07T15:28:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KKho9.10744$ue4.503242@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<4a5699b5.0210060750.c3e3c70@posting.google.com>`

```

"davidc" <rondos@zahav.net.il> wrote in message
news:4a5699b5.0210060750.c3e3c70@posting.google.com...
> I try to compile various programs with NOTRICKLE directive and always
> receive the message "notrickle - rejected".
…[4 more quoted lines elided]…
> Maybe somebody knows why?

    If you check the help, you will note that it does not seem to mention
the trickle
directive.  It has been deleted for some reason.

    I suppose the the compatiblity manual / document should say more.

    I would hope.

    Remove that directive.  If you try to eliminate perform thru's and
go to's, you should not need TRICKLE anyway.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
