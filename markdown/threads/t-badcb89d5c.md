[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Useing AcuCobol programs in batch (background) processing.

_3 messages · 3 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Useing AcuCobol programs in batch (background) processing.

- **From:** blakew@balsa.fuller.com ()
- **Date:** 1999-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn7j37pp.l6r.blakew@fullerbrush.com>`

```
Hello Cobol World!

We have a job written in Acucobol on our Tru64-Unix 4.0 system.  We would like
to have the job run in batch (background) processing.  It would be REALY nice
if we could run this job with a cron / crontab entry.

Every time we try to do this the AcuCobol job crashes and in the log file
it puts...

	Memory access violation

Any suggestions?

Thank you for your time.
```

#### ↳ Re: Useing AcuCobol programs in batch (background) processing.

- **From:** "D.Newman" <Domenyk.Newman@MCL-Group.com>
- **Date:** 1999-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<926007795.5961.0.nnrp-11.9e98ccda@news.demon.co.uk>`
- **References:** `<slrn7j37pp.l6r.blakew@fullerbrush.com>`

```
What happens if you run the program from the command prompt. Do you get the
same error.
```

#### ↳ Re: Useing AcuCobol programs in batch (background) processing.

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fAzWTEAVuxO3IweE@rcav8r.demon.co.uk>`
- **References:** `<slrn7j37pp.l6r.blakew@fullerbrush.com>`

```
Hi,

Have you checked with Acucorp support? I seem to remember a
problem a long time ago where certain operations could cause a
problem in a background program (I think ACCEPT FROM
SYSTEM-INFO was one). This problem was resolved quite some
time ago, so if you have an older release an upgrade should fix it.

I'm guessing you're in the USA so you can just call
1-800-COBOL85, or email support@acucorp.com


Best regards

Nigel

In article <slrn7j37pp.l6r.blakew@fullerbrush.com>,
blakew@balsa.fuller.com writes
>Hello Cobol World!
>
…[21 more quoted lines elided]…
>The Fuller Brush Company        |                               - Blaise Pascal
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
