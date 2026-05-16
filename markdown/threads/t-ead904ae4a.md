[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol not closing my File - WHY?

_2 messages · 2 participants · 2004-11_

---

### Re: Cobol not closing my File - WHY?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-11-11T18:43:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CpOkd.27974$Qv5.23022@newssvr33.news.prodigy.com>`
- **References:** `<7a2e7221.0411111011.50c1a223@posting.google.com>`

```
"Phil" <google@gigdesigns.co.uk> wrote in message
news:7a2e7221.0411111011.50c1a223@posting.google.com...
> This is probably something easily explained (hopefully!).
>
…[18 more quoted lines elided]…
> file handle for the file it should have closed....


If the I-O module is doing a CLOSE WITH LOCK then maybe the compiler is
retaining the open handle specifically to prevent this program from
re-opening this file. Of course, the second and subsequent OPENs should fail
in this case... and if the CLOSE is in fact a common routine then you should
get the same behavior on file 2

(Hell, it's a thought!)

Hmm, another thought... what is your environment? There are some funky
things about *re*-opening files on Windows if the file is created by a
server program and the client is not an authenticated process...I have
details here somewhere but I'm not going to look this up until I know it's
worth the effort....


MCM
```

#### ↳ Re: Cobol not closing my File - WHY?

- **From:** google@gigdesigns.co.uk (Phil)
- **Date:** 2004-11-12T00:30:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a2e7221.0411120030.36da86c9@posting.google.com>`
- **References:** `<7a2e7221.0411111011.50c1a223@posting.google.com> <CpOkd.27974$Qv5.23022@newssvr33.news.prodigy.com>`

```
The environment is on AIX 5.2 Unix, so no windows stuff to worry about.

thanks anyway

"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<CpOkd.27974$Qv5.23022@newssvr33.news.prodigy.com>...
> "Phil" <google@gigdesigns.co.uk> wrote in message
> news:7a2e7221.0411111011.50c1a223@posting.google.com...
…[38 more quoted lines elided]…
> MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
