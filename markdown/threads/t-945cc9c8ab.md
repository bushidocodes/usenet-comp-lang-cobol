[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM-Cobol Data Translation Utility

_2 messages · 2 participants · 2000-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RE: RM-Cobol Data Translation Utility

- **From:** "Juan Manuel Peralta Lopez" <j_peralta@jet.es>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bqok8$oju$1@lola.ctv.es>`
- **References:** `<sdr6haealul66@news.supernews.com>`

```
Hi,

    You can try a program called "recover2.cob", this program extract data
from any compressed and indexed RM/Cobol file into a plain text file with
just a record separator.


Ray Felix <forthay@yahoo.com> escribi� en el mensaje de noticias
sdr6haealul66@news.supernews.com...
> Hello,
>
…[3 more quoted lines elided]…
> Thank you
```

#### ↳ Re: RM-Cobol Data Translation Utility

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k=TgODW+hICmox7E6xrUepQ1+CcZ@4ax.com>`
- **References:** `<sdr6haealul66@news.supernews.com> <8bqok8$oju$1@lola.ctv.es>`

```
On Tue, 28 Mar 2000 19:08:51 +0200, "Juan Manuel Peralta Lopez"
<j_peralta@jet.es> wrote:

>Hi,
>
>    You can try a program called "recover2.cob", this program extract data
>from any compressed and indexed RM/Cobol file into a plain text file with
>just a record separator.
Not quite.
Although it creates a file just with the records, this file is a
binary sequentian file.
This means that if the record it self had some "COMP-XXXX" fields
these will NOT be converted.
And as most people know these are were the problems with other
"software" applications exist.

If this was that easy no one would need the conversion for
files created by MF or by RM/COBOL (dual file).

FF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
