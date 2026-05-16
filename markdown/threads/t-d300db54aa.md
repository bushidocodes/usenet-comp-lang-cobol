[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Compiler version question

_4 messages · 3 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Compiler version question

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f22879.4484636@news.enteract.com>`

```
Hello,

Is it possible to run programs compiled using the MF Unix compiler
version 3.0.5  under the run-time supplied with new MF Unix compiler
version 4.1???

It would be nice not to have to re-compile everything!

Thanks,

Paul
--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

#### ↳ Re: MF Compiler version question

- **From:** "T Brown" <tom.brown@clara.net>
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VaAI2.973$mi3.257@nnrp3.clara.net>`
- **References:** `<36f22879.4484636@news.enteract.com>`

```
There's a compiler directive INTLEVEL"x"  - for your case compile your new
stuff with INTLEVEL"3" and mixing old and new .INTs should work (in
theory) - What it does is force the new compiler to make code compatible
with the old. - Obviously you can't take advantage of any of the new
features added to the compiler.
I did try this using Object cobol 4.1 and cobol/2 V1.3 (1998 compiler with
1990 INTs) - not surprisingly it didn't work.  But you may have a better
chance since your 2 versions of cobol are closer.
Regards Tom

PAL3000 wrote in message <36f22879.4484636@news.enteract.com>...
>Hello,
>
…[11 more quoted lines elided]…
>words REMOVETHIS from my email address
```

#### ↳ Re: MF Compiler version question

- **From:** areymond@csi.com (Alain Reymond)
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f20a3a.2069069@news.skynet.be>`
- **References:** `<36f22879.4484636@news.enteract.com>`

```
If yours programs are linked, they are native exe and you don't need
to recompile.
If you use int or gnt, it will work. But be careful. You'd better
recompile the code because if you make any modification with the code,
you'll have a mix of v 3 and v 4 int and/or gnt. And the result might
be unpredictible. 
Recompiling is easy under Unix. A for ... do ... done loop will do the
job in just a few minutes. If the code is error free....

Yours faithfully

Alain Reymond


On Thu, 18 Mar 1999 16:24:47 GMT, pduboisREMOVETHIS@enteract.com
(PAL3000) wrote:

>Hello,
>
…[11 more quoted lines elided]…
>words REMOVETHIS from my email address
```

##### ↳ ↳ Re: MF Compiler version question

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f48170.3657268@news.enteract.com>`
- **References:** `<36f22879.4484636@news.enteract.com> <36f20a3a.2069069@news.skynet.be>`

```


Thanks for the help,

Paul

On Fri, 19 Mar 1999 08:29:59 GMT, areymond@csi.com (Alain Reymond)
wrote:

>If yours programs are linked, they are native exe and you don't need
>to recompile.
…[28 more quoted lines elided]…
>>words REMOVETHIS from my email address

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
