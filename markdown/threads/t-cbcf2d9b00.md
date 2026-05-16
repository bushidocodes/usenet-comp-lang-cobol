[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Internationalization in COBOL

_2 messages · 2 participants · 2000-12_

---

### Internationalization in COBOL

- **From:** "Rover" <Rover@pobox.com>
- **Date:** 2000-12-12T22:03:18+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<915422$e0j$1@bunyip.cc.uq.edu.au>`

```
Hi,

Does someone have a good source of material in showing me how to handle Double Byte Characters Sets or UNICODE in COBOL running on minis and mainframes? What is the best way to convert an existing suite of COBOL program from SBCS to handle foreign languages?

Thanks.

Rover
```

#### ↳ Re: Internationalization in COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-12T12:25:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<915qf0$eld$1@slb7.atl.mindspring.net>`
- **References:** `<915422$e0j$1@bunyip.cc.uq.edu.au>`

```
*UNFORTUNATELY* there is no "general" way to do this today - without knowing
which compiler you are using.  If by "mainframe and minis" you mean IBM
mainframe compilers - and the PC compilers that "emulate them" - or if you
mean any "mini" compiler that conforms to the (older) X/Open Standard, then
you *probably* can/should use PIC N (and the implied USAGE NATIONAL).
However, these have limited support for run-time LOCALES (i.e. same source
code but different "run-time results" depending on where - what locale -
your application is actually run).

All of this *is* included in the draft Standard. So once (if) it gets
approved and implemented, there will be "standard" ways to do this.

If this is not a "general" question but a question about how to do a
specific task with a specific compiler (and specific operating system), let
us know the details and we can give you more information/solutions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
