[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Open fail: stdin when invoking MicroFocus compiler

_2 messages · 2 participants · 2000-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Open fail: stdin when invoking MicroFocus compiler

- **From:** "Jacques Vidal" <jvidal@mail.dotcom.fr>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a8lo4$fvb$1@wanadoo.fr>`

```
Hi,

I am doing a software installation on a distant computer (running Unix SCO
SVR3.2)
thru a telnet connection (Hyperterminal actually, if that matters) There's a
MicroFocus
compiler (4.1.20) on that machine that I need to use for the install.The
compiler was
never used before. The MicroFocus license manager is running OK.

But when I simply run cob, with or without parameters, I get an 'Open fail:
stdin'
message instead of the usual 'I see no work'. Can anyone explain what
happens.
I need a reply quick. I can't contact the guy who installed the compiler.

Thanks in advance.
```

#### ↳ Re: Open fail: stdin when invoking MicroFocus compiler

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aaidc$6kf$1@hyperion.mfltd.co.uk>`
- **References:** `<8a8lo4$fvb$1@wanadoo.fr>`

```

Jacques Vidal wrote in message <8a8lo4$fvb$1@wanadoo.fr>...
>Hi,
>
>I am doing a software installation on a distant computer (running Unix SCO
>SVR3.2)
>thru a telnet connection (Hyperterminal actually, if that matters) There's
a
>MicroFocus
>compiler (4.1.20) on that machine that I need to use for the install.The
…[11 more quoted lines elided]…
>

Hi Jacques,

I had a quick word with one of the developers and this is what he said,

> cob will read stdin if it sees '-' by itself on the command line, which is
> common practice for Unix commands.

> If there are not any parameters on the command line, it could be that "-"
is set
> in $COBOPT or in $COBDIR/cobopt

Btw I tend to type cobrun on its own and wait for the banner to come up to
test I
have the environment set up, and to check the product version.

$ cobrun
V4.1 revision 30 build 10/10/2 G; 26899. Run Time System OXCTX/AA0/00000G


Are you getting this message (then see above)

$ cob -
Open fail : stdin
cob: error(s) in compilation: stdin

Hope this helps,

Regards,
Steve.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
