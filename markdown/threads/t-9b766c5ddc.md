[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fileshare and Server Express

_3 messages · 2 participants · 2007-09_

---

### Fileshare and Server Express

- **From:** umwelt@hotmail.com
- **Date:** 2007-09-24T04:27:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190633242.666640.111830@50g2000hsm.googlegroups.com>`

```
Hi

We're trying to amend our bespoke software application to use
fileshare security and according to documentation, we should be able
to link fhrdrpwd.o with our client application.

UNIX:
On UNIX, all the Fileshare Client modules are automatically available
so you do not need to link any extra objects when creating an
executable version of your application. However, if you want to create
a stand-alone static executable, you need to include the objects
fhrdrpwd.o and fhxscomp.o.

Unfortunately, this module doesn't appear present in Server Express
(this .o file was present in Object COBOL).

Is there an alternative to this .o?

Any help, or suggestions, would be much appreciated.
```

#### ↳ Re: Fileshare and Server Express

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-24T07:39:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tmbff3dc9m57k8905lv9iicskiq5qas0hc@4ax.com>`
- **References:** `<1190633242.666640.111830@50g2000hsm.googlegroups.com>`

```
On Mon, 24 Sep 2007 04:27:22 -0700, umwelt@hotmail.com wrote:

>Hi
>
…[16 more quoted lines elided]…
>Any help, or suggestions, would be much appreciated.

You're asking how to statically link a shared library. It cannot be done.

If they supplied .a files, you can statically link them just like .o files. 

You can use -L to set the library search path to . (current directory) or the directory
where your software will be installed. By doing that, you don't need to worry about being
in the end user's LD_LIBRARY_PATH.
```

#### ↳ Re: Fileshare and Server Express

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-24T08:07:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r8dff3d4c5v46mljuvskhjpproo7j61hua@4ax.com>`
- **References:** `<1190633242.666640.111830@50g2000hsm.googlegroups.com>`

```
On Mon, 24 Sep 2007 04:27:22 -0700, umwelt@hotmail.com wrote:

>Hi
>
…[16 more quoted lines elided]…
>Any help, or suggestions, would be much appreciated.

To see which libraries your application is using, run

ldd (your executable name)

Names on the list are the ones you must distribute. They need not be in a directory named
/opt/cobol (whatever), they could be in the same directory with your executable. At
execution time, the loader finds them by searching -L and LD_LIBRARY_PATH.

LD_LIBRARY_PATH complies with the POSIX Standard and is available on every Unix. Do not
use older proprietary names such as SHLIB_PATH.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
