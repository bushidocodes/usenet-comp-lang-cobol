[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COPY "QPR.CPY"

_4 messages · 2 participants · 2002-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COPY "QPR.CPY"

- **From:** AlfredLanger@t-online.de (Alfred Langer)
- **Date:** 2002-04-26T19:24:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cc9a83e.11431149@news.t-online.de>`

```
The Fujisu-Compiler(here a Mastering Cobol Version 4.0) didn't find
QPR.CPY. If I copy this file with cut and past, the programm works
well.
```

#### ↳ Re: COPY "QPR.CPY"

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-04-26T16:33:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gOiy8.18517$h02.3331646@news20.bellglobal.com>`
- **References:** `<3cc9a83e.11431149@news.t-online.de>`

```
Try specifying a full path name if it is not in the same directory as the
one containing your source code.
IE: - COPY "C:\FPFJ32PS\QPR.CPY".


Donald

"Alfred Langer" <AlfredLanger@t-online.de> wrote in message
news:3cc9a83e.11431149@news.t-online.de...
> The Fujisu-Compiler(here a Mastering Cobol Version 4.0) didn't find
> QPR.CPY. If I copy this file with cut and past, the programm works
> well.
>
>
```

##### ↳ ↳ Re: COPY "QPR.CPY"

- **From:** AlfredLanger@t-online.de (Alfred Langer)
- **Date:** 2002-04-27T16:19:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ccacf4e.5341762@news.t-online.de>`
- **References:** `<3cc9a83e.11431149@news.t-online.de> <gOiy8.18517$h02.3331646@news20.bellglobal.com>`

```
On Fri, 26 Apr 2002 16:33:55 -0400, "Donald Tees"
<donald_tees@sympatico.ca> wrote:

>Try specifying a full path name if it is not in the same directory as the
>one containing your source code.
>IE: - COPY "C:\FPFJ32PS\QPR.CPY".
Thank you. It works
.
I think I have a problem with my path settings.

Alfred


>
>Donald
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COPY "QPR.CPY"

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-04-27T17:24:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UDEy8.111597$Bp3.3802226@news20.bellglobal.com>`
- **References:** `<3cc9a83e.11431149@news.t-online.de> <gOiy8.18517$h02.3331646@news20.bellglobal.com> <3ccacf4e.5341762@news.t-online.de>`

```
While you might be able to fix the problem by fiddling about with paths,
that is not the way I would do it.  I would set up a project library for the
source code, and place a copy of the QPR file in that area.  While that may
seem to defeat the purpose of the copy, that particular file may evolve as
you develope your approach to using Formprint.  It also means that you can
convert systems separately later if you upgrade versions.

Donald

"Alfred Langer" <AlfredLanger@t-online.de> wrote in message
news:3ccacf4e.5341762@news.t-online.de...
> On Fri, 26 Apr 2002 16:33:55 -0400, "Donald Tees"
> <donald_tees@sympatico.ca> wrote:
…[23 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
