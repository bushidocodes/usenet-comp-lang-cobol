[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# submit job to run at specified time

_2 messages · 2 participants · 2002-10_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### submit job to run at specified time

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-10-04T00:18:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c26b3b$87961e40$f991f243@chottel>`

```
I seem to remember someone on this group having this problem, so I am
reposting from the ibm.main newsgroup:

You may use the command // COMMAND '$T A,T=hh.mm,''$A jobname''' in a
batch job with TYPRUN=HOLD

 or (if you may experience problems with duplicate names), issue
                           via CONSOLE
   '$T A,T=hh.mm,'$A Jnnnn' (obtaining the job number from the
                         SUBMIT command)


The rexx program can be executed any time before the execution time

Regards
```

#### ↳ Re: submit job to run at specified time

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-10-03T23:59:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0210032259.1fa86383@posting.google.com>`
- **References:** `<01c26b3b$87961e40$f991f243@chottel>`

```
Thanx, Charlie.

Regards, Jack.

"Charles Hottel" <chottel@cpcug.org> wrote in message news:<01c26b3b$87961e40$f991f243@chottel>...
> I seem to remember someone on this group having this problem, so I am
> reposting from the ibm.main newsgroup:
…[17 more quoted lines elided]…
> www.MainFrameForum.com - USENET Gateway
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
