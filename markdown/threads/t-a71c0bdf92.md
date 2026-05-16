[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rewrite Twice?

_4 messages · 3 participants · 2006-05_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Rewrite Twice?

- **From:** dmckeon@ameritas.com
- **Date:** 2006-05-31T08:14:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149088494.470474.70070@i40g2000cwc.googlegroups.com>`

```
I have a situation where I'm processing a request that comes in a
sequential file.  At the end of processing, we rewrite the record so we
know processing is complete.  I'm now adding some logic and want to
perform a rewrite in the middle of processing in case the program
abends in the middle, we can recover properly.  Unfortunately, the
second rewrite then fails.  Is there any way to rewrite a record twice
or do I need to close the file and re-read it back to the point I was
at?

I'm using Microfocus Workbench on Windows XP.

Thanks!
```

#### ↳ Re: Rewrite Twice?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-05-31T18:55:35+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6er721c8m50tp11cplp5210i5jcasompt@4ax.com>`
- **References:** `<1149088494.470474.70070@i40g2000cwc.googlegroups.com>`

```
On 31 May 2006 08:14:54 -0700 dmckeon@ameritas.com wrote:

:>I have a situation where I'm processing a request that comes in a
:>sequential file.  At the end of processing, we rewrite the record so we
:>know processing is complete.  I'm now adding some logic and want to
:>perform a rewrite in the middle of processing in case the program
:>abends in the middle, we can recover properly.  Unfortunately, the
:>second rewrite then fails.  Is there any way to rewrite a record twice
:>or do I need to close the file and re-read it back to the point I was
:>at?

Can you change it so that it isn't a sequential file?

Otherwise you are out of luck.

Also, be aware the issuing the WRITE does not guarantee that the record is
firmed to disk, especially when there is an abend. The record may be in a
buffer. A CLOSE will force the write. There may be other tools provided by
your COBOL.
```

#### ↳ Re: Rewrite Twice?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-31T12:39:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127rhou6oclmhec@corp.supernews.com>`
- **References:** `<1149088494.470474.70070@i40g2000cwc.googlegroups.com>`

```

<dmckeon@ameritas.com> wrote in message
news:1149088494.470474.70070@i40g2000cwc.googlegroups.com...
> I have a situation where I'm processing a request that comes in a
> sequential file.  At the end of processing, we rewrite the record so we
…[7 more quoted lines elided]…
> I'm using Microfocus Workbench on Windows XP.

The Byte-stream File Routines may be used or,
perhaps, a second file that contains only the ID
of the record being processed, so that only one
rewrite is required.
```

##### ↳ ↳ Re: Rewrite Twice?

- **From:** dmckeon@ameritas.com
- **Date:** 2006-05-31T10:13:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149095627.191093.44760@f6g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<127rhou6oclmhec@corp.supernews.com>`
- **References:** `<1149088494.470474.70070@i40g2000cwc.googlegroups.com> <127rhou6oclmhec@corp.supernews.com>`

```

Rick Smith wrote:
> <dmckeon@ameritas.com> wrote in message
> news:1149088494.470474.70070@i40g2000cwc.googlegroups.com...
…[14 more quoted lines elided]…
> rewrite is required.

Thanks for the input, guys.  I'll just close the file and re-read it.
I just thought there might be a trick or a command that I was
unfamiliar with.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
