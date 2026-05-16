[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetCOBOL on Mandriva

_6 messages · 4 participants · 2008-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### NetCOBOL on Mandriva

- **From:** charles.goodman@bell.ca
- **Date:** 2008-01-25T13:27:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com>`

```
I am trying an eval of NetCOBOL for Linux.
I am using Mandriva 2008.
Installation is complete and I am able to compile, but I am getting a
link error: "ld: No such file or directory".
Fujitsu support are trying to help, but are a bit slow.
Have any of you had luck getting Fujitsu's Linux compiler working on
newer Linux distros?

Best Regards,  Charlie
```

#### ↳ Re: NetCOBOL on Mandriva

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-26T20:37:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b523da03-b4ba-4ee4-888a-84dbc77a0181@i72g2000hsd.googlegroups.com>`
- **References:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com>`

```
On Jan 26, 10:27 am, charles.good...@bell.ca wrote:
> I am trying an eval of NetCOBOL for Linux.
> I am using Mandriva 2008.

It should work fine on Mandriva. I run my copy of Fujitsu on that,
though it has not been updated to 2008.

> Installation is complete and I am able to compile, but I am getting a
> link error: "ld: No such file or directory".
> Fujitsu support are trying to help, but are a bit slow.
> Have any of you had luck getting Fujitsu's Linux compiler working on
> newer Linux distros?

The problem is most likely case sensitivity. While DOS/Windows files
are case insensitive under Unix and Linux file names with different
case are distinct files. However, to setting of various compiler
options can lead to confusing. The ALPHAL setting may change the case
of program names and especially of literals used in a CALL. If you
have a CALL "xxxx" then the linker may want to find a file: libXXXX.so
and will fail if it doesn't exist, or has been named libxxx.so.
```

##### ↳ ↳ Re: NetCOBOL on Mandriva

- **From:** C Goodman <foxgrove@shaw.ca>
- **Date:** 2008-01-27T12:43:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0%mj.16463$ow.8096@pd7urf1no>`
- **In-Reply-To:** `<b523da03-b4ba-4ee4-888a-84dbc77a0181@i72g2000hsd.googlegroups.com>`
- **References:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com> <b523da03-b4ba-4ee4-888a-84dbc77a0181@i72g2000hsd.googlegroups.com>`

```
Richard wrote:
> On Jan 26, 10:27 am, charles.good...@bell.ca wrote:
>> I am trying an eval of NetCOBOL for Linux.
…[3 more quoted lines elided]…
> though it has not been updated to 2008.
That's good news.
>> Installation is complete and I am able to compile, but I am getting a
>> link error: "ld: No such file or directory".
…[10 more quoted lines elided]…
> and will fail if it doesn't exist, or has been named libxxx.so.
I don't think that is the problem.  My test program simply uses DISPLAY 
and ACCEPT for hello world.  This may be a problem once I start working 
on my full system of 1000 programs.
```

#### ↳ Re: NetCOBOL on Mandriva

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-01-27T11:37:26
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1201433846@f609.n257.z2.fidonet.ftn>`
- **References:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com>`

```
Hello charles!

25 Jan 08 21:27, you wrote to All:

 cg> I am trying an eval of NetCOBOL for Linux.
 cg> I am using Mandriva 2008.
 cg> Installation is complete and I am able to compile, but I am getting a
 cg> link error: "ld: No such file or directory".
 cg> Fujitsu support are trying to help, but are a bit slow.
 cg> Have any of you had luck getting Fujitsu's Linux compiler working on
 cg> newer Linux distros?

Having installed cobol have you run ldconfig ?

If not do a man ldconfig and run it.

Vince
```

##### ↳ ↳ Re: NetCOBOL on Mandriva

- **From:** C Goodman <foxgrove@shaw.ca>
- **Date:** 2008-01-27T13:03:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ni%mj.14762$4w.6213@pd7urf2no>`
- **In-Reply-To:** `<1201433846@f609.n257.z2.fidonet.ftn>`
- **References:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com> <1201433846@f609.n257.z2.fidonet.ftn>`

```
Vince Coen wrote:
> Hello charles!
> 
…[16 more quoted lines elided]…
> 
Thanks Vince,

I will try ldconfig on Monday.  LD_LIBRARY_PATH is set with pointers to 
NetCOBOL.  The first suggestion from support was to add the location of 
my source to both LD_LIBRARY_PATH and PATH.
```

#### ↳ Re: NetCOBOL on Mandriva

- **From:** charles.goodman@bell.ca
- **Date:** 2008-01-28T13:15:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40d082c4-3cb9-45a1-9a78-89c834901479@h11g2000prf.googlegroups.com>`
- **References:** `<3f36bdbf-b692-4d35-8736-fb12137d8d6e@m34g2000hsb.googlegroups.com>`

```
I'm making some progress, and learning a bunch about Linux.  The ld
error was caused by not having the gcc package installed.  I used
"urpmi gcc".  I am now able to compile and execute.

My next problem is getting the interactive debugger to work.  I
compile with a command like "cobol -M -Dt -o mytest mytest.cbl".  The
executable works by simply entering the command "mytest".

I am using the command "svd mytest" to invoke the interactive
debugger.  It returns an error "svd: ERROR: The specified file is not
a executable program.".  The attributes of mymain show it to be
generated as executable.

---Charlie


On Jan 25, 3:27 pm, charles.good...@bell.ca wrote:
> I am trying an eval of NetCOBOL for Linux.
> I am using Mandriva 2008.
…[6 more quoted lines elided]…
> Best Regards,  Charlie
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
