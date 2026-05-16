[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comprehensive listing of errors

_4 messages · 3 participants · 2002-10_

---

### Comprehensive listing of errors

- **From:** "Dawn Minnis" <dawn_minnis@thefreeinternet.co.uk>
- **Date:** 2002-10-27T22:17:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aphom5$55e$1@helle.btinternet.com>`

```
does anybody know where i can find a really good (and by that I mean fully
explained) list of complie and runtime errors for COBOL.  My list has
basically 5-6 word answers that dont really explain anything.

Any Ideas

Dawn
```

#### ↳ Re: Comprehensive listing of errors

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-10-27T16:55:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aphqsk$ntn$1@slb3.atl.mindspring.net>`
- **References:** `<aphom5$55e$1@helle.btinternet.com>`

```
Tell us what compiler (vendor, release, and operating system) you are
interested in.

IBM's mainframe compiler (for example) will give you a complete list of
compile-time messages - if you simply compile a program with

  IDENTIFICATION DIVISION.
  PROGRAM-ID.  ERRMSG.

    ***

Other vendors provide "message" manuals - while others say that there
messages are "self-documenting".
```

##### ↳ ↳ Re: Comprehensive listing of errors

- **From:** "Dawn Minnis" <dawn_minnis@thefreeinternet.co.uk>
- **Date:** 2002-10-28T18:58:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<apk1cu$1hh$1@sparta.btinternet.com>`
- **References:** `<aphom5$55e$1@helle.btinternet.com> <aphqsk$ntn$1@slb3.atl.mindspring.net>`

```
Im using a compiler that was supplied by the University (Queen's) so i have
know documentation for it but the title at the top of the screen has
"Fortransoft Ltd" if that is of any help.  I have sussed my problem by the
way.  The original .DAT file which was created by someone eles was
incorrect.  Its fixed now and works fine.

Thanks for the help though
```

#### ↳ Re: Comprehensive listing of errors

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-10-27T23:29:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kF_u9.1393$mN6.418300@newssrv26.news.prodigy.com>`
- **References:** `<aphom5$55e$1@helle.btinternet.com>`

```
"Dawn Minnis" <dawn_minnis@thefreeinternet.co.uk> wrote in message
news:aphom5$55e$1@helle.btinternet.com...
> does anybody know where i can find a really good (and by that I mean fully
> explained) list of complie and runtime errors for COBOL.  My list has
> basically 5-6 word answers that dont really explain anything.

All compile and run-time error codes are defined by the compiler publisher.
No such thing as a common set of error codes. If your compiler provides 5-6
words, that's what you get.

About the only COBOL 'code values' which are [semi]-standardized are FILE
STATUS values.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
