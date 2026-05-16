[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol and threads

_3 messages · 3 participants · 1999-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol and threads

- **From:** "Stephen Felts" <sdf@beasys.com>
- **Date:** 1999-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mq1s1$6kg$1@news.beasys.com>`

```
I am having trouble compiling/linking programs on Unix that
require the threads libraries but are not currenty multithreaded.
I tried on Digital Unix 4.0 and AIX 4.3.  I'm also interested in
a few others like Solaris 2.5.1 and HP 11.
Where can I find a list of what MicroFocus COBOL compilers are supported on
   what platforms?
Does MicroFocus COBOL support threaded applications?
```

#### ↳ Re: MF Cobol and threads

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mqk2d$dck@dfw-ixnews15.ix.netcom.com>`
- **References:** `<7mq1s1$6kg$1@news.beasys.com>`

```
Have you tried MERANT (aka Micro Focus) homepage at
   www.merant.com
```

#### ↳ Re: MF Cobol and threads

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vr9k3.1862$4J2.32122@news1.frmt1.sfba.home.com>`
- **References:** `<7mq1s1$6kg$1@news.beasys.com>`

```
Stephen, the 'Express range of compiler products from MERANT Micro Focus
(Net Express on NT, Server Express on UNIX) fully (and i emphasize "fully")
support building multi-threaded COBOL applications.

now, i expect that the compiler you are using is one of COBOL, Toolbox or
Object COBOL Dev Suite. none of these support multi-threading. i don't think
it's even possible to create something that is thread-safe.

Server Express is currently available for AIX and Solaris (more platfoms are
in the works).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
