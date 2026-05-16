[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing to COM2:

_3 messages · 3 participants · 2002-01_

---

### Writing to COM2:

- **From:** "JEY" <jey@sf.dk>
- **Date:** 2002-01-09T12:25:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c3c28b3$0$5496$edfadb0f@dspool01.news.tele.dk>`

```
Hi Guys

Does anybody know, how to write to com2: from acucobol programs ???

Cheers
```

#### ↳ Re: Writing to COM2:

- **From:** "Acucorp News" <shaun_gough@hotmail.com>
- **Date:** 2002-01-09T16:58:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1451C740A890D411B65C00104B95B1C055DFF6@ras.acucorp.com>`
- **References:** `<3c3c28b3$0$5496$edfadb0f@dspool01.news.tele.dk>`

```
Dear Sir.

Acucorp recomends using a C or Active-X program to control the data sent and
recieved by the COM ports, to provide a much lower control of handling the
data flow.

Thanks
Shaun Gough - Senior Customer Solutions Analyst.
ACUCORP Inc.
8515 Miralani Drive, San Diego, CA 92126, USA
E-Mail: sgough@acucorp.com
http://www.acucorp.com

Please send all responses to support@acucorp.com to ensure prompt handling
of the issue by a technical support representative. If an existing issue,
please mark for my attention.

Want the latest COBOL tips, tricks and information?
Subscribe to the Acucorp newsletter today:
http://www.acucorp.com/News/Newsletter/subscribe.html.  Acucorp's quarterly
newsletter contains news and solutions, technical advice, product
announcements and much more!  For a copy of the latest issue, visit
http://www.acucorp.com/News/Newsletter/newsletter.html.

"JEY" <jey@sf.dk> wrote in message
news:3c3c28b3$0$5496$edfadb0f@dspool01.news.tele.dk...
> Hi Guys
>
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Writing to COM2:

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-01-10T01:02:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-NHiqQLwx3gfs@thishost>`
- **References:** `<3c3c28b3$0$5496$edfadb0f@dspool01.news.tele.dk>`

```
On Wed, 9 Jan 2002 11:25:50 UTC, "JEY" <jey@sf.dk> wrote:

> Hi Guys
> 
…[5 more quoted lines elided]…
> 

assign out-file to output "com2:"
  organization line sequential.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
