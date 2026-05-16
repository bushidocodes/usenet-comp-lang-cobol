[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call a Windows exe Programm

_3 messages · 3 participants · 2000-12_

---

### Call a Windows exe Programm

- **From:** "Ralph Leiherr" <leiherr@vwda.de>
- **Date:** 2000-12-14T11:02:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91a5m8$vid$03$1@news.t-online.com>`

```
Hallo,

first: my compiler is a Micro-Focus Workbench Compiler 4.0.32, my operating
system is Windows NT 4.0.

So, I need a call from my program to a exe file. First I use call X"91"
using Z-Pgm-Result, Z-Pgm-Function, Z-Pgm-Len. And it workï¿½s but the call
open a DOS-Box in background and I donï¿½t need this.

Now my question, how can I call an "window".exe file without a DOS-Box ?

Many thanks in advance
Yours

Ralph Leiherr
```

#### ↳ Re: Call a Windows exe Programm

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-12-14T12:46:52
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91aj1g$1re$1@hyperion.mfltd.co.uk>`
- **References:** `<91a5m8$vid$03$1@news.t-online.com>`

```
Ralph,


"Ralph Leiherr" <leiherr@vwda.de> wrote in message
news:91a5m8$vid$03$1@news.t-online.com...
> Hallo,
>
> first: my compiler is a Micro-Focus Workbench Compiler 4.0.32, my
operating
> system is Windows NT 4.0.
>
> So, I need a call from my program to a exe file. First I use call X"91"
> using Z-Pgm-Result, Z-Pgm-Function, Z-Pgm-Len. And it work�s but the call
> open a DOS-Box in background and I don�t need this.

The reason that the DOS box appears is that the call starts a command
processor to allow DOS commands to be executed as well as executables.

>
> Now my question, how can I call an "window".exe file without a DOS-Box ?


You can do this by using the CBL_EXEC_RUN_UNIT call.

>
> Many thanks in advance
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Call a Windows exe Programm

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-12-15T04:24:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001214232455.23985.00004458@ng-fs1.aol.com>`
- **References:** `<91aj1g$1re$1@hyperion.mfltd.co.uk>`

```
Hi Ralph,

You can also use the windows api CreateProcess.  Please e-mail me for a sample.

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
