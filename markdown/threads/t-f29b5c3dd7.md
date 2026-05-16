[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fujitsu cobol v3

_3 messages · 3 participants · 2002-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### fujitsu cobol v3

- **From:** radami1@uic.edu (ron)
- **Date:** 2002-01-03T15:35:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85105800.0201031535.6ae36196@posting.google.com>`

```
I am using fujitsu cobol version 3 in a batch job on winnt and I
always get a window opening up every time the batch runs. The window's
purpose is to get runtime variable values and it is genreated by the
fujitsu system. The program won't start unless this window is
satisfied. How do I suppress this window so that the job can be
scheduled at a later time for unattended operation?

                Ron
```

#### ↳ Re: fujitsu cobol v3

- **From:** "Dionisis Vrionis" <software@dksoft.gr>
- **Date:** 2002-01-04T09:30:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a13lh8$iis$1@ulysses.noc.ntua.gr>`
- **References:** `<85105800.0201031535.6ae36196@posting.google.com>`

```
Use the command on this window typing

@EnvSetWindow=UNUSE

in Cobol85.cbr file.

Take care of upper and lower cases


"ron" <radami1@uic.edu> wrote in message
news:85105800.0201031535.6ae36196@posting.google.com...
> I am using fujitsu cobol version 3 in a batch job on winnt and I
> always get a window opening up every time the batch runs. The window's
…[5 more quoted lines elided]…
>                 Ron
```

#### ↳ Re: fujitsu cobol v3

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2002-01-07T17:44:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U7l_7.7332$cD4.11867@www.newsranger.com>`
- **References:** `<85105800.0201031535.6ae36196@posting.google.com>`

```
in the COBOL85.CBR file insert this line:

@EnvSetWindow=UNUSE

In article <85105800.0201031535.6ae36196@posting.google.com>, ron says...
>
>I am using fujitsu cobol version 3 in a batch job on winnt and I
…[6 more quoted lines elided]…
>                Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
