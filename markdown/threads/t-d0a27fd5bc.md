[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT: How do I remove the underline?

_4 messages · 4 participants · 1999-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### ACCEPT: How do I remove the underline?

- **From:** "Chiew Heng Wah" <heng7@hotmail.com>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380f2ec2.0@news.tm.net.my>`

```
Hi. I am new to this newsgroup.

Is there a clause associated with ACCEPT such that every time you accept the
field would be displayed as underlined?

(I tried "ACCEPT ..... WITH NO UNDERLINE" but that doesn't work.)

By the way, where is the FAQ for this NG located?

Thanks

Heng Wah.
```

#### ↳ Re: ACCEPT: How do I remove the underline?

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7unddm$o61$1@news.inet.tele.dk>`
- **References:** `<380f2ec2.0@news.tm.net.my>`

```
What compiler??
Micro Focus has Accep/display rules, you can modify. The point is that the
entry field is marked to show you its position and size. You will not get
the underscores into your program.

Rgards
Ib
Chiew Heng Wah skrev i meddelelsen <380f2ec2.0@news.tm.net.my>...
>Hi. I am new to this newsgroup.
>
>Is there a clause associated with ACCEPT such that every time you accept
the
>field would be displayed as underlined?
>
…[8 more quoted lines elided]…
>
```

#### ↳ Re: ACCEPT: How do I remove the underline?

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7upd6b$3oj$1@hyperion.mfltd.co.uk>`
- **References:** `<380f2ec2.0@news.tm.net.my>`

```

Chiew Heng Wah wrote in message <380f2ec2.0@news.tm.net.my>...
>Hi. I am new to this newsgroup.
>
>Is there a clause associated with ACCEPT such that every time you accept
the
>field would be displayed as underlined?
>


If the compiler is from Micro Focus, if you do an ACCEPT with attributes (eg
UNDERLINE) followed by an ACCEPT or DISPLAY without attributes, the run-time
just updates the text so the previous attributes remain. A simple way to
force the attributes to be updated is by specifying a colour eg
FOREGROUND-COLOR 7 (white).
```

##### ↳ ↳ Re: ACCEPT: How do I remove the underline?

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uru05$j74$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<380f2ec2.0@news.tm.net.my> <7upd6b$3oj$1@hyperion.mfltd.co.uk>`

```
    Do the underlines go away when you enter data (even spaces)?  If yes, it
might be the prompt clause.


Gael Wilson <gael.wilson@merant.com> wrote in message
news:7upd6b$3oj$1@hyperion.mfltd.co.uk...
>
> Chiew Heng Wah wrote in message <380f2ec2.0@news.tm.net.my>...
…[8 more quoted lines elided]…
> If the compiler is from Micro Focus, if you do an ACCEPT with attributes
(eg
> UNDERLINE) followed by an ACCEPT or DISPLAY without attributes, the
run-time
> just updates the text so the previous attributes remain. A simple way to
> force the attributes to be updated is by specifying a colour eg
> FOREGROUND-COLOR 7 (white).
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
