[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is the error RTS 148?

_2 messages · 2 participants · 1999-06_

---

### What is the error RTS 148?

- **From:** roebuck@mindspring.com (S. Timothy Roebuck)
- **Date:** 1999-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jav1u$hb2$1@nntp8.atl.mindspring.net>`

```
For the life of me I am trying to fugure where my program is in error.
It compiles fine.  Upon execution, I get a Error 148.  The reference 
matrerial I have regarding Error codes seems useless.  Has anyone 
experienced this error and if so, can you offer some additional
information as to where I might look to find the error?

I would appreciate any help.

Thanks in Advance!

STR
```

#### ↳ Re: What is the error RTS 148?

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375929aa@news3.us.ibm.net>`
- **References:** `<7jav1u$hb2$1@nntp8.atl.mindspring.net>`

```
148 is "wrong access mode for write".
E.g. you opened the file for input and now you are trying to write to it.

S. Timothy Roebuck <roebuck@mindspring.com> wrote in message
news:7jav1u$hb2$1@nntp8.atl.mindspring.net...
> For the life of me I am trying to fugure where my program is in error.
> It compiles fine.  Upon execution, I get a Error 148.  The reference
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
