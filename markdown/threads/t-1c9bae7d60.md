[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# procedure pointer OS/390 COBOL370/VSCOBOL II

_3 messages · 2 participants · 2005-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### procedure pointer OS/390 COBOL370/VSCOBOL II

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2005-01-12T02:50:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0501120250.1fa6e22f@posting.google.com>`

```
Hi,

I have a short question about procedure pointer.
we have some lines in our cobol progs, like 

move 'progname' to prog
call prog   using something

cancel prog




Now I will use procedure-pointer


01  pgmptr         procedure-pointer

set pgmptr         to entry 'progname'

call pointer         using soemthing



can i use in this case 

cancel    'progname'

to cancel the upro


regards

jï¿½rg
```

#### ↳ Re: procedure pointer OS/390 COBOL370/VSCOBOL II

- **From:** patrick.magee@microfocus.com
- **Date:** 2005-01-14T07:48:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105717687.983227.112840@z14g2000cwz.googlegroups.com>`
- **References:** `<7f6b3f56.0501120250.1fa6e22f@posting.google.com>`

```
01 pgmptr procedure-pointer.
set pgmptr to entry 'progname'
call pgmptr using soemthing
cancel 'progname'

The above should work.
```

#### ↳ Re: procedure pointer OS/390 COBOL370/VSCOBOL II

- **From:** patrick.magee@microfocus.com
- **Date:** 2005-01-14T07:48:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105717736.616065.114650@f14g2000cwb.googlegroups.com>`
- **References:** `<7f6b3f56.0501120250.1fa6e22f@posting.google.com>`

```
01 pgmptr procedure-pointer.
set pgmptr to entry 'progname'
call pgmptr using soemthing
cancel 'progname'

The above should work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
