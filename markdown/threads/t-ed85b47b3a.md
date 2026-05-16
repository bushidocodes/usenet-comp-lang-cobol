[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# microfocus:File status 9/025

_5 messages · 3 participants · 2003-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### microfocus:File status 9/025

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-13T11:34:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2523922.1045136090@dbforums.com>`

```

Windows NT/2000/XP

What�s this?
Soluction?
```

#### ↳ Re: microfocus:File status 9/025

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-13T12:14:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2523927.1045138472@dbforums.com>`
- **References:** `<2523922.1045136090@dbforums.com>`

```

I have that problem today. a workstation uses, it liberates, the times
leaves and if other to use the same file or registration of the
mistake 9/025.
I used cbl_alloc_mem and it didn't solve.
what do make?
```

##### ↳ ↳ Re: microfocus:File status 9/025

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-14T07:09:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2gn4s$gl4$1@aklobs.kc.net.nz>`
- **References:** `<2523922.1045136090@dbforums.com> <2523927.1045138472@dbforums.com>`

```
mfcobol2002 wrote:

> I have that problem today. a workstation uses, it liberates, the times
> leaves and if other to use the same file or registration of the
> mistake 9/025.
> I used cbl_alloc_mem and it didn't solve.
> what do make?

If you are using cbl_alloc_mem in your program and it gives a completely 
spurious error, such as as 9/025, or otherwise behaves is really strange 
ways then it is probably because you are not handling the allocated memory 
correctly.

Using pointers allows you to accidentally write to _any_ location and not 
just the places that the compiler sets for you.  If you have coded your 
program wrongly then you could be overwriting data that doesn't belong to 
you.
```

###### ↳ ↳ ↳ Re: microfocus:File status 9/025

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-14T01:04:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4c4094.65724114@news.optonline.net>`
- **References:** `<2523922.1045136090@dbforums.com> <2523927.1045138472@dbforums.com> <b2gn4s$gl4$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>mfcobol2002 wrote:
>
…[14 more quoted lines elided]…
>you.

Drat .. uncovered. Can you believe Microsoft provides no memory protection? An
application can write over any other applications memory, and even the operating
system's. 

That's the secret we BRILLIANT hackers use to crash DoD and NSA computers .. at
least in the movies, where we are portrayed as 12 year-old kids. Never mind that
the computers are running IBM or Unix operating systems. If one dog has spots,
all dogs have spots. It's called "hasty generalization" by logic folks, but what
do they know about computers? They shoulda checked with us BRILLIANT hackers,
who could have explained how stupid the establishment is.

mfcobol2002: lay off the drugs. You'll recover within a week.
```

#### ↳ Re: microfocus:File status 9/025

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-14T10:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2529150.1045217861@dbforums.com>`
- **References:** `<2523922.1045136090@dbforums.com>`

```

respected friend,

the mistake this giving without using the alloc_mem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
