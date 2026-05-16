[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Determine execute location program

_1 message · 1 participant · 2003-06_

---

### Re: Determine execute location program

- **From:** "R. Hendriks" <R.Hendriks_1@uvt.nl>
- **Date:** 2003-06-20T14:41:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcuvcj$c2m$1@kostnix.uvt.nl>`
- **References:** `<bcpvsd$qv$1@kostnix.uvt.nl> <bcs8e1$5kt$1@kostnix.uvt.nl>`

```
Also sorted the win95 problem. The docs say it's supported, the user32.dll
export says it's not. I've now used GetModuleFileName which is supported
from win95 and winnt3.1 and up. Use GetModuleHandle to resolve the handle of
the current module.

Rik

"R. Hendriks" <R.Hendriks_1@uvt.nl> wrote in message
news:bcs8e1$5kt$1@kostnix.uvt.nl...
> I've continued searching after posting my message to this group and found
> the answer myself in the API call GetWindowModuleFileName. For those
…[13 more quoted lines elided]…
> *   This call needs the handle of the current window to determine the
path.
> Within PowerCOBOL this handle
> *   is a property of every form (=pow-self). This property is not visible
…[26 more quoted lines elided]…
> illegal output of user32.dll? The SDK clearly states that minimun OS req.
is
> Windows 95, Windows NT4 SP3. Anyone has an idea on this?
>
…[12 more quoted lines elided]…
> > \myapp\ on a drive of choice. For instance the path to the .exe could
be:
> > C:\MYAPP\MYAPP.EXE or E:\MYAPP\MYAPP.EXE.
> > I've made a config file called myapp.ini which is always located in the
…[3 more quoted lines elided]…
> > Problem now is how to determine the drive (or the whole path) on which
the
> > myapp.exe program is executed so that I can determine the path to the
> > myapp.ini file (by simply changing the .exe to the .ini). What would be
…[6 more quoted lines elided]…
> > Is there a API-call, CBL-routine or COBOL-function that can determine
the
> > execution path / location of a program? I've tried PC_READ_DRIVE but
that
> > can change during execution I believe (correct me if I'm wrong). By the
> way,
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
