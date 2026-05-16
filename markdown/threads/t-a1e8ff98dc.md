[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus COBOL in Windows Millenium problem

_3 messages · 3 participants · 2001-07 → 2001-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus COBOL in Windows Millenium problem

- **From:** Mirek Hetman <miro@vienna.com.pl>
- **Date:** 2001-07-30T17:50:27+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B658243.A84AAFBD@vienna.com.pl>`

```
I have a program written in COBOL.
I upgraded from MS-Dos to Windows Millenium and have a problem.
While I try to run the program I get error:

"load failure (170) on file ADIS"

I guess compiler version is MicroFocus/Microsoft COBOL 4.5 (dated at
1991).

Please help,
Mirek Hetman

my e-mail is:
miro@vienna.com.pl
```

#### ↳ Re: MicroFocus COBOL in Windows Millenium problem

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-07-30T17:01:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B659332.5D406AD@home.com>`
- **References:** `<3B658243.A84AAFBD@vienna.com.pl>`

```


Mirek Hetman wrote:

> I have a program written in COBOL.
> I upgraded from MS-Dos to Windows Millenium and have a problem.
…[6 more quoted lines elided]…
>

It's quite a while since I used ADIS(Accept/Display) - but - have you
got the ADIS support files in your program path. (Can't  remember for
sure, but doesn't there have to be an entry in your Autoexec 'pointing'
to the ADIS path ?).

Jimmy, Calgary AB
```

##### ↳ ↳ Re: MicroFocus COBOL in Windows Millenium problem

- **From:** Roblec <roblec@rr.com>
- **Date:** 2001-08-02T03:14:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B68C568.3EE32BE3@rr.com>`
- **References:** `<3B658243.A84AAFBD@vienna.com.pl> <3B659332.5D406AD@home.com>`

```
Three ADIS object files (adis.obj adisinit.obj adiskey.obj) must be
linked into the executable, or they may be linked together in a
standalone ADIS.EXE in the current directory or found in the DOS PATH. 
Also the file ADISCTRL must be in the current directory or in the
directory specified in the COBDIR variable.

"James J. Gavan" wrote:
> 
> Mirek Hetman wrote:
…[16 more quoted lines elided]…
> Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
