[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# linux cobol compiler

_7 messages · 5 participants · 2011-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### linux cobol compiler

- **From:** Paride Desimone <parided@gmail.com>
- **Date:** 2011-03-27T23:54:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7Qjp.13990$%g.35528@twister1.libero.it>`

```
Hi,
I have an old warehouse program write in old microfocus powercobol
running on old msdos.
I want to port it on GNU/Linux. Does anyone know where to download a copy?
```

#### ↳ Re: linux cobol compiler

- **From:** mainframezen <ribeirolog@gmail.com>
- **Date:** 2011-03-28T05:11:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a74b5fc8-d398-4cee-9b6e-a67bfdc101ac@x1g2000yqb.googlegroups.com>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it>`

```
On Mar 28, 12:54 am, Paride Desimone <pari...@gmail.com> wrote:
> Hi,
> I have an old warehouse program write in old microfocus powercobol
> running on old msdos.
> I want to port it on GNU/Linux. Does anyone know where to download a copy?

Try opencobol, forget Micro Focus.
http://www.opencobol.org/

Also:
http://www.cobol-it.com/
```

#### ↳ Re: linux cobol compiler

- **From:** "Vince Coen" <VBCoen@gmail.com>
- **Date:** 2011-03-28T15:54:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1301324063@f1.n250.z2.fidonet.ftn>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it>`

```
Hello Paride!

28 Mar 11 00:54, Paride Desimone wrote to All:

 > I have an old warehouse program write in old microfocus powercobol
 > running on old msdos.
 > I want to port it on GNU/Linux. Does anyone know where to download a
 > copy?

Assuming you are refuring to a Cobol compiler then check out Open Cobol v1.1 
as it converts Cobol to C code then uses the GNU Gcc compiler to finish the 
job.

Works well



Vince
```

#### ↳ Re: linux cobol compiler

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2011-03-28T17:08:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<imq8b2$djm$02$1@news.t-online.com>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it>`

```
Hi,

opencobol and cobol-it are free, but to migrate an mf-cobol-based app
is not easy if you use for example split keys in your isam files.
The working with the functions keys is different, too.

Perhaps I know somebody who can let work remote with a mf compiler
to try what are differences and troubles.

VS

Paride Desimone wrote:

> Hi,
> I have an old warehouse program write in old microfocus powercobol
> running on old msdos.
> I want to port it on GNU/Linux. Does anyone know where to download a copy?
```

##### ↳ ↳ Re: linux cobol compiler

- **From:** "Vince Coen" <VBCoen@gmail.com>
- **Date:** 2011-03-30T00:41:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1301442087@f1.n250.z2.fidonet.ftn>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it> <imq8b2$djm$02$1@news.t-online.com>`

```
Hello Vaclav!

28 Mar 11 16:08, Vaclav Snajdr wrote to All:

 > Hi,

 > opencobol and cobol-it are free, but to migrate an mf-cobol-based app
 > is not easy if you use for example split keys in your isam files.
 > The working with the functions keys is different, too.

 > Perhaps I know somebody who can let work remote with a mf compiler
 > to try what are differences and troubles.

I converted over 200k lines from MF to OC with very minor issues. If anything 
with the large increase in extra functions, it cut down a lot of very old code 
after primary migration.



Vince
```

###### ↳ ↳ ↳ Re: linux cobol compiler

- **From:** Paride Desimone <parided@gmail.com>
- **Date:** 2011-03-31T21:47:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ND6lp.15926$%g.48826@twister1.libero.it>`
- **In-Reply-To:** `<1301442087@f1.n250.z2.fidonet.ftn>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it> <imq8b2$djm$02$1@news.t-online.com> <1301442087@f1.n250.z2.fidonet.ftn>`

```
Il 30/03/2011 00:41, Vince Coen ha scritto:

> I converted over 200k lines from MF to OC with very minor issues. If anything 
> with the large increase in extra functions, it cut down a lot of very old code 
> after primary migration.

Ok, I'll try!

Paride
```

#### ↳ Re: linux cobol compiler

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-03-28T12:39:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b924dde-c86d-49d9-854a-7c41ad200892@v11g2000prb.googlegroups.com>`
- **References:** `<n7Qjp.13990$%g.35528@twister1.libero.it>`

```
On Mar 28, 12:54 pm, Paride Desimone <pari...@gmail.com> wrote:
> Hi,

> I have an old warehouse program write in old microfocus powercobol
> running on old msdos.

PowerCOBOL is/was a Fujitsu product that was GUI based. It ran on
Windows. There was a Windows 3.x version many years ago (I have a CD
here).

MicroFocus COBOLs for DOS were: CIS COBOL, Level II COBOL, COBOL/2,
Object COBOL.

> I want to port it on GNU/Linux. Does anyone know where to download a copy?

MicroFocus products are quite expensive and you will need run-time
licenses to run the system. Fujitsu (now sold to someone else) is
better priced and can avoid run-time costs. Both have free educational
versions that do not allow distribution, but not of their GNU/Linux
systems.

Free COBOLs are OpenCOBOL, tinyCOBOL and some versions of COBOL-IT
(which is OpenCOBOL based).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
