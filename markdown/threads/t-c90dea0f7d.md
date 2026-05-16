[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# First Semester problrm: simple cobol rm cobol / 85 problem with subprograms

_3 messages · 3 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### First Semester problrm: simple cobol rm cobol / 85 problem with subprograms

- **From:** "Khalid Shah" <specialk@alphalink.com.au>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ih58o$ujt$1@news.alphalink.com.au>`

```
If any one can help, please reply, I have a subprogram and the calling
program. Whats the code in the calling program to call the subprogram which
is a seperate file
```

#### ↳ Re: First Semester problrm: simple cobol rm cobol / 85 problem with subprograms

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7igrf9$mlb$1@nnrp1.deja.com>`
- **References:** `<7ih58o$ujt$1@news.alphalink.com.au>`

```



In article <7ih58o$ujt$1@news.alphalink.com.au>,
  "Khalid Shah" <specialk@alphalink.com.au> wrote:
> If any one can help, please reply, I have a subprogram and the calling
> program. Whats the code in the calling program to call the subprogram
which
> is a seperate file
>
>
```

##### ↳ ↳ Re: First Semester problrm: simple cobol rm cobol / 85 problem with subprograms

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ikvf6$dvn@enews3.newsguy.com>`
- **References:** `<7ih58o$ujt$1@news.alphalink.com.au> <7igrf9$mlb$1@nnrp1.deja.com>`

```
For simple calls, use:

call 'program-name' using 'work-record'...

where work-record is a group of data elements to be passed to the
subprogram.  The calling program will need to have the same 'work-record' in
it's linkage section and accepts the data using

procedure division using 'work-record'

Jeff

----------
In article <7igrf9$mlb$1@nnrp1.deja.com>, Ed Stevens
<Ed.Stevens@nmm.nissan-usa.com> wrote:


>
>
…[20 more quoted lines elided]…
> ---Share what you know. Learn what you don't.---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
