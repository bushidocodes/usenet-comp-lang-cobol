[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus /Sql Server performance issue

_4 messages · 4 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### MicroFocus /Sql Server performance issue

- **From:** csm14@my-deja.com
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p9o80$itr$1@nnrp1.deja.com>`

```
We have a job that reads a 6000 byte file, and for each record performs
various selects and then inserts into various tables.  The job was
compiled using MicroFocus COBOL 4.0. This process was running in about
10 hours.  We had to make a small change (an additional field on the
file was checked before processing) and after recompile the process is
now taking about 40 hours.  When we use the NT performance monitor we
are only seeing about 5% CPU usage and very limited I/O.  The source,
application and target are all on the same server which is used
exclusively for this one application.  What is even more confusing is
that running under animator (which is interpreted) is now faster than
running the compiled job.  After this problem surfaced we upgraded from
6.5 to version 7 hoping to improve performance, with no effect.  Any
suggestions?


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: MicroFocus /Sql Server performance issue

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p9ted$ea9$2@aklobs.kc.net.nz>`
- **References:** `<7p9o80$itr$1@nnrp1.deja.com>`

```
csm14@my-deja.com wrote:
: We have a job that reads a 6000 byte file, and for each record performs

I hope that this is a mistyping of 6000 MEGA byte if it takes
10/40 hours.

: various selects and then inserts into various tables.  The job was
: compiled using MicroFocus COBOL 4.0. This process was running in about
: 10 hours.  We had to make a small change (an additional field on the
: file was checked before processing) and after recompile the process is
: now taking about 40 hours.  When we use the NT performance monitor we
: are only seeing about 5% CPU usage and very limited I/O.  The source,
: application and target are all on the same server which is used
: exclusively for this one application.  What is even more confusing is
: that running under animator (which is interpreted) is now faster than
: running the compiled job.  After this problem surfaced we upgraded from
: 6.5 to version 7 hoping to improve performance, with no effect.  Any
: suggestions?

Ummmm.... Don't use NT or SQL Server ?
```

#### ↳ Re: MicroFocus /Sql Server performance issue

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e%t3.15195$C6.153404@news2.rdc1.on.home.com>`
- **References:** `<7p9o80$itr$1@nnrp1.deja.com>`

```
<csm14@my-deja.com> wrote in message news:7p9o80$itr$1@nnrp1.deja.com...
> We have a job that reads a 6000 byte file, and for each record performs
> various selects and then inserts into various tables.  The job was
…[14 more quoted lines elided]…
> Share what you know. Learn what you don't.

All things being equal, it sounds like you used different compiler
directives than the last person who compiled the program. Try to find out
how the program used to be built. Failing that:

1) Check your precompiler directives for CONNECT and DISCONNECT. It may be
that the precompiler stuck them in all over the place.
2) Check if you're working in EXCLUSIVE or SHARED mode. Sharing adds
overhead.
3) Find and read the Micro Focus reference manual for working with SQL
Server.
```

#### ↳ Re: MicroFocus /Sql Server performance issue

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 1999-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pb8v7$aq6$1@hyperion.mfltd.co.uk>`
- **References:** `<7p9o80$itr$1@nnrp1.deja.com>`

```
Can you tell me the exact version of Micro Focus COBOL you are using i.e.
4.0.xx?

Can you tell the service pack level of your NT machine?

Many thanks.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT Micro Focus International.

<csm14@my-deja.com> wrote in message news:7p9o80$itr$1@nnrp1.deja.com...
> We have a job that reads a 6000 byte file, and for each record performs
> various selects and then inserts into various tables.  The job was
…[14 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
