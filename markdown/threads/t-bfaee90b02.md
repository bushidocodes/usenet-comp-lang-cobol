[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS 4.1 HELP PLEASE

_3 messages · 2 participants · 1998-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: CICS 4.1 HELP PLEASE

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bda916$fb6fe170$c58c3398@us0071826>`
- **References:** `<3587C98D.E666AAC7@cslp.org>`

```

Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
statement 
to OS/VS Cobol. This has caused the short on storage above 16MB problem on
a
previous project I was involved. 

AM
```

#### ↳ Re: CICS 4.1 HELP PLEASE

- **From:** RandallBart <Barticus@att.spam.net>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ns5l5$nsh@bgtnsc03.worldnet.att.net>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <01bda916$fb6fe170$c58c3398@us0071826>`

```

AM wrote:
> 
> Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
…[5 more quoted lines elided]…
> AM

Short on storage *above* the line?  I doubt it.  OS/VS Cobol runs only
below the line. 
```

##### ↳ ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bda9b3$c1bfe220$c58c3398@us0071826>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <01bda916$fb6fe170$c58c3398@us0071826> <6ns5l5$nsh@bgtnsc03.worldnet.att.net>`

```
Yes OS/VS COBOL is below the line. and passing the working storages to an
above the line
program such as COBOL II was (one of) the cause(s) of the problem we had.
You cannot use a CALL
statement between OS/VS COBOL and higher COBOL versions (COBOL II / MVS
COBOL) in
a CICS environment.

RandallBart <Barticus@att.spam.net> wrote in article
<6ns5l5$nsh@bgtnsc03.worldnet.att.net>...
| AM wrote:
| > 
| > Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
| > statement
| > to OS/VS Cobol. This has caused the short on storage above 16MB problem
on
| > a
| > previous project I was involved.
…[15 more quoted lines elided]…
|
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
