[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT the TTY line number in MF COBOL

_2 messages · 2 participants · 2006-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### ACCEPT the TTY line number in MF COBOL

- **From:** "C C" <someone@atsbcglobal.net>
- **Date:** 2006-09-27T01:19:56+00:00
- **Newsgroups:** comp.lang.cobol,comp.unix.aix
- **Message-ID:** `<0lkSg.15948$Ij.9536@newssvr14.news.prodigy.com>`

```
Is there a better way to accept the pts line number of a telnet session in
Microfocus Cobol in AIX 5.3?

We are using Micro Focus Server Express.

Thanks in advance.
```

#### ↳ Re: ACCEPT the TTY line number in MF COBOL

- **From:** "Stephen Gennard" <stephen.gennard@microfocus.com>
- **Date:** 2006-09-27T09:34:17+01:00
- **Newsgroups:** comp.lang.cobol,comp.unix.aix
- **Message-ID:** `<12hkdtlc91dkna1@corp.supernews.com>`
- **References:** `<0lkSg.15948$Ij.9536@newssvr14.news.prodigy.com>`

```
The easiest way I can think of is:

        select foobar assign "</usr/bin/tty"
                line sequential.
        fd foobar.
        01  rec pic x(20).

        procedure division.
                open input foobar
                    read foobar
                    at end
                       move "unknown" to rec
                    end-read
                close foobar
                display "My TTY is : " rec
                exit program.

"C C" <someone@atsbcglobal.net> wrote in message 
news:0lkSg.15948$Ij.9536@newssvr14.news.prodigy.com...
> Is there a better way to accept the pts line number of a telnet session in
> Microfocus Cobol in AIX 5.3?
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
