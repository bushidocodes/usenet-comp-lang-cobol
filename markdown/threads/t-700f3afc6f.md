[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help getting started with Fujitsu Compiler

_4 messages · 3 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help getting started with Fujitsu Compiler

- **From:** "kai..." <ua-author-6252920@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34fb88b8.131117625@news.ma.ultranet.com>`

```


When I try to link the example in Sample1.obj (or for that matter a
"Hello World" program) I get the following msg:

fatal error 01077

c:\fsc\pcobol32\samples\sample1\sample1.obj
c:\fsc\pcobol32\project.res
c:\fsc\pcobol32\f3bicimp.lib
c:\fsc\pcobol32\libc.lib
c:\fsc\pcobol32\kernel32.lib
c:\fsc\pcobol32\user32.lib

LINK: fatal error LNK1561: entry point must be defined.

What am I doing wrong?

Any help would be appreciated.

Thanks,

Don
Kai··.@ult··t.com
```

#### ↳ Re: Help getting started with Fujitsu Compiler

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-700f3afc6f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34fb88b8.131117625@news.ma.ultranet.com>`
- **References:** `<34fb88b8.131117625@news.ma.ultranet.com>`

```

Don Kaiser wrote:
› 
› When I try to link the example in Sample1.obj (or for that matter a
…[17 more quoted lines elided]…
› Thanks,

Don, I'll try to do this from Memory. If I what I tell you does not
work, e-mail me and I'll go through it step by step for you.

You have to tell the linker that this program is a MAIN program. How do
you do that? NOT from the work frame, but from the compile icon, there
is a settings pull down. Go in there and ADD MAIN. Once that is done,
it will work.

I had this trouble too and someone else on the news group helped me.
Hopefully they will reply with more detailed instructions.
```

#### ↳ Re: Help getting started with Fujitsu Compiler

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-700f3afc6f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34fb88b8.131117625@news.ma.ultranet.com>`
- **References:** `<34fb88b8.131117625@news.ma.ultranet.com>`

```

Don,

You should have got a Micro Focus COBOL product .

Good luck.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus UK

Don Kaiser wrote in message <34f··.@new··t.com>...
› 
› When I try to link the example in Sample1.obj (or for that matter a
…[23 more quoted lines elided]…
›
```

#### ↳ Re: Help getting started with Fujitsu Compiler

- **From:** "kai..." <ua-author-6252920@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-700f3afc6f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34fb88b8.131117625@news.ma.ultranet.com>`
- **References:** `<34fb88b8.131117625@news.ma.ultranet.com>`

```


Well I answered my own question.

Why does that so often happen after you ask for help?

Anyway, I discovered that the default for the Fujitsu compiler is to
compile as a subroutine.

Don
Kai··.@ult··t.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
