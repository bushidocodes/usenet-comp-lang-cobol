[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus file errors

_3 messages · 3 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus file errors

- **From:** craigdiaz@my-deja.com
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o5ojd$o4k$1@nnrp1.deja.com>`

```
Hi,
I'm familiar with COBOL, but not on a PC. I'm getting errors trying to
read input files with Micro Focus version 3.0, the status is usually 39
which appears to be an operating system incompatiblity error,
diagnostics say recreate the file. Okay, but with what? I tried using
REBUILD.EXE, all it did eventually was change the error status for the
file to 22, an illegal OPEN error. The files are part of a 'legacy'
system that was running under Novell netware, Win95. I've copied the
files to my stand-alone running Win98. Some of the files I can
read/write no problem, others won't cooperate at all. The error
messages in the manual just don't seem to help. Anyone met this problem
before?


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Micro Focus file errors

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o5pti$gol@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7o5ojd$o4k$1@nnrp1.deja.com>`

```
File status 39 means that your file is NOT defined in your FD the same way
it exits on the hard-drive.  Find out the actual "attributes" of the file,
and then change your source code to match.
```

#### ↳ Re: Micro Focus file errors

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A6735B.F73CC030@home.com>`
- **References:** `<7o5ojd$o4k$1@nnrp1.deja.com>`

```
craigdiaz@my-deja.com wrote:
> 
> Hi,
…[10 more quoted lines elided]…
> before?

I'm using NetExpress. The only time I've hit an Error 39 -  
incompatibility - is where I have changed a record size, recompiled the
program and then used a data file which was in the old record format.
As regards the Error 22 - are you positive you haven't got any dup keys
?

Beyond that I can't help.

Jimmy, Calgary AB
 - example - ascii delimited - length 178
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
