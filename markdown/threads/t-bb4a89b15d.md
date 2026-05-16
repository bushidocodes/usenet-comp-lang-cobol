[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 114 in Microfocus Server Express 2.2 when calling C functions

_2 messages · 2 participants · 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Error 114 in Microfocus Server Express 2.2 when calling C functions

- **From:** cyberkiks <member44206@dbforums.com>
- **Date:** 2003-10-15T04:35:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3483292.1066206940@dbforums.com>`

```

I am running a server express 2.2 run-time on a HPUX 11 O/S.

COBOL programs are linked with C functions, and in particular with OCI
Oracle C functions.



I have execution problem when executing some of the C functions :

<<

error code: 114 Attempt to access item beyond bounds of memory
(Signal 11)

>>



It seems that IF statements with null pointer in the C programs are the
cause of this stop.

However, previous versions of Microfocus compilers were compliant with
this syntax.



Do you know a run-time option or a compiler option to prevent this error
? Microfocus support is not very quick in finding something...



Thanks in advance for your help.
```

#### ↳ Re: Error 114 in Microfocus Server Express 2.2 when calling C functions

- **From:** "Simon Tobias" <Simon.Tobias@nospam.MicroFocus.com>
- **Date:** 2003-10-15T23:47:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmkih6$n84$1@hyperion.microfocus.com>`
- **References:** `<3483292.1066206940@dbforums.com>`

```
Are you executing with the threaded COBOL run-time? This is necessary on
HP-UX due to Oracle linking their own libraries with the threaded C run-time
on this platform.

If the code causing the RTS114 is the C code, which is calling Oracle
functions, does this trap, or fail in any other way, if you run it
standalone (i.e. without COBOL)?

Regarding your final point :

> Do you know a run-time option or a compiler option to prevent this error
> ? Microfocus support is not very quick in finding something...

Have you contacted SupportLine with a cutdown sample which demonstrates this
problem? It sounds like you've isolated where the problem is occuring which
is good, but is the NULL pointer due to a corruption coming from COBOL?

SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
