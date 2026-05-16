[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copybooks

_3 messages · 3 participants · 2001-03_

---

### Re: Copybooks

- **From:** jim_royle_myarse@yahoo.com (Jim Royle)
- **Date:** 2001-03-08T20:54:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010308195437.10364.qmail@web10307.mail.yahoo.com>`

```
My COPY statement is coded COPY copybook and my
copybook file is just called 'copybook' with no
extension. (although I have tried it with the
extension of cbl and cpy). I've just tried Jerry's
suggestion of including the full path name and that
seems to work, but I really didn't want to have to do
this. I thought I could just specify the name of the
copybook and in the compiler options somewhere specify
which directory all of my copybooks are kept in. Is
this possible to do ?

__________________________________________________
Do You Yahoo!?
Get email at your own domain with Yahoo! Mail. 
http://personal.mail.yahoo.com/
```

#### ↳ Re: Copybooks

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-03-08T13:05:08-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AA80214.F3F0B647@dced.state.ak.us>`
- **References:** `<20010308195437.10364.qmail@web10307.mail.yahoo.com>`

```
It might be in an environment variable vs. a compiler option. Microfocus
uses COBCOPY.

Jim Royle wrote:

> My COPY statement is coded COPY copybook and my
> copybook file is just called 'copybook' with no
…[16 more quoted lines elided]…
> via Mailgate.ORG Server - http://www.Mailgate.ORG
```

##### ↳ ↳ Re: Copybooks

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-03-09T00:41:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010308194136.18653.00000319@nso-cl.aol.com>`
- **References:** `<3AA80214.F3F0B647@dced.state.ak.us>`

```
In article <3AA80214.F3F0B647@dced.state.ak.us>, Calvin Crumrine
<Calvin_Crumrine@dced.state.ak.us> writes:

>
>It might be in an environment variable vs. a compiler option. Microfocus
…[8 more quoted lines elided]…
>

Definitely, in FujiCOBOL you can specify the directory to 
search for COPY members.
LIB=<drive>:<copylib path>
As far as I know, the compiler will look in the current directory
AND whatever directory is specified by LIB=
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
