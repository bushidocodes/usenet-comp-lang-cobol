[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Runtime Library

_4 messages · 4 participants · 2002-08 → 2002-09_

---

### Cobol Runtime Library

- **From:** d.g.a@gmx.net (Diego Gozzi Aranda)
- **Date:** 2002-08-29T06:27:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89dd71d1.0208290527.1e5e4f98@posting.google.com>`

```
Hello

First of all, i am totaly new to Cobol.

I am trying to run a program from a friend, but it shows to me the
following message:

Cobol run time library not installed

Any of you could please help me? Where on the www can i fint such
library?

Thanks in advance.

Diego
```

#### ↳ Re: Cobol Runtime Library

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-29T14:34:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aklt0g$ntq$1@slb2.atl.mindspring.net>`
- **References:** `<89dd71d1.0208290527.1e5e4f98@posting.google.com>`

```
Did your friend tell you *which* COBOL compiler they used?  Depending upon
the compiler, you may need to PURCHASE a run-time library to run this
program.  If your friend didn't tell you this (and you can't get the
information from him), did the message have some type of "prefix"
(alphanumeric - e.g. XXX123) part at the beginning of the message?  If so,
we MIGHT be able to figure this out for you.

Another possibility is to ask your friend if their compiler has an option to
"build a stand-alone executable".  Some compilers have this option, while
others do not.
```

#### ↳ Re: Cobol Runtime Library

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-29T12:46:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0208291146.4c08346e@posting.google.com>`
- **References:** `<89dd71d1.0208290527.1e5e4f98@posting.google.com>`

```
d.g.a@gmx.net (Diego Gozzi Aranda) wrote 
> 
> I am trying to run a program from a friend, but it shows to me the
…[5 more quoted lines elided]…
> library?

You are a little short on details:

    Operating System
    Cobol brand and version
    Command line used
    Licence number of run-time

As a complete guess, and assuming that your 'friend' had two clues to
rub together and did send you all that was required, is that this is a
DOS program running on Windows NT/2000 and you need to prefix the
command with FORCEDOS.
```

##### ↳ ↳ Re: Cobol Runtime Library

- **From:** "Gael Wilson" <gael.wilson@nospam.microfocus.com>
- **Date:** 2002-09-02T11:03:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akvd78$rki$1@hyperion.microfocus.com>`
- **References:** `<89dd71d1.0208290527.1e5e4f98@posting.google.com> <217e491a.0208291146.4c08346e@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0208291146.4c08346e@posting.google.com...
> d.g.a@gmx.net (Diego Gozzi Aranda) wrote
> >
…[4 more quoted lines elided]…
> >

This message is because you are attempting to run a 16-bit version of Micro
Focus COBOL, or application created by it, on Windows NT/2000/XP and the
Os2LibPath environment variable does not contain the directory containing
the run-time DLLs for your COBOL system (eg COBOL\EXEDLL). You can, as
Richard pointed out, use FORCEDOS to run the DOS part of the executable, but
setting up the environment variable eliminates the need to do so as it runs
the 16-bit OS/2 part of the executable instead.

I hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
