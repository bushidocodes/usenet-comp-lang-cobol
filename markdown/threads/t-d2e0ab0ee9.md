[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie Question...

_3 messages · 3 participants · 1998-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Newbie Question...

- **From:** "james watkins" <ua-author-2134783@usenetarchives.gap>
- **Date:** 1998-02-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6c0ea6$aa0@news.cei.net>`

```

I just got MicroFocus Cobol and I was wondering if there is a command to get
a character without having to press the enter key? Kind of like getch( ) in
C++. What I'm using it for is when I ask "Do you want to continue ?"
the user can just press Y or N and the program will execute the next line of
code.

Thanks in advance,

James
```

#### ↳ Re: Newbie Question...

- **From:** "edw" <ua-author-7163589@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d2e0ab0ee9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6c0ea6$aa0@news.cei.net>`
- **References:** `<6c0ea6$aa0@news.cei.net>`

```

Have a look at "cbl_read_kbd_char" in library routines(call-by-name) in the
system reference.

› I just got MicroFocus Cobol and I was wondering if there is a command to
› get
› a character without having to press the enter key? Kind of like getch( )
```

##### ↳ ↳ Re: Newbie Question...

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d2e0ab0ee9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d2e0ab0ee9-p2@usenetarchives.gap>`
- **References:** `<6c0ea6$aa0@news.cei.net> <gap-d2e0ab0ee9-p2@usenetarchives.gap>`

```

James,

You could also take a look at the x"af" ADIS routines in the COBOL System
Reference. Another option might be the ACCEPT WITH TIMEOUT.

Good luck.

Paddy Coleman
Team Leader, UK Distributed Computing Support (WinTel)
Micro Focus.

edw wrote in message <01bd3860$576a44c0$3a4e80c1@loanstt>...
› Have a look at "cbl_read_kbd_char" in library routines(call-by-name) in the
› system reference.
…[5 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
