[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ms cobol compiler 2.10 - display at

_2 messages · 2 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### ms cobol compiler 2.10 - display at

- **From:** "Maver" <maverdec@tin.it>
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72actn$ni4$1@nslave1.tin.it>`

```
Hi!
I have to develop a short application in cobol that will run on an old 286.
I'm using an old microsoft compiler version 2.10.
I can't figure out how to use the statement DISPLAY AT:
I tried display at line 10 column 10 item
           display item at 1010
           display item at line 10 column 10
but none of these is accepted by the compiler, I always get syntax error.
Help, please!
```

#### ↳ Re: ms cobol compiler 2.10 - display at

- **From:** Robert Kovacic <rjk@onaustralia.com.au>
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36491EFB.4656FF4B@onaustralia.com.au>`
- **References:** `<72actn$ni4$1@nslave1.tin.it>`

```
Maver wrote:

> Hi!
> I have to develop a short application in cobol that will run on an old 286.
…[6 more quoted lines elided]…
> Help, please!

  DISPLAY (24, 1) "This is displayed on line 24 column"

There are examples in the manual. If you do not have the manuals then you will
most likely encounter other areas where you will get stuck.

Regards, Robert Kovacic.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
