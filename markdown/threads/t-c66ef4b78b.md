[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In search of a PL/I - COBOL for OS/390 comparison

_3 messages · 3 participants · 1999-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** robin <robin_v@bigpond.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<or9M3.2034$_4.3415@newsfeeds.bigpond.com>`

```
From: "William M. Klein" <wmklein@nospam.netcom.com>, 
MindSpring EnterprisesDate: Sat, 9 Oct 1999 11:38:48 -0500
robin <robin_v@bigpond.com> wrote in message
news:CpIL3.1233$_4.2153@newsfeeds.bigpond.com...
>> "William M. Klein" <wmklein@nospam.netcom.com> writes:
>> > Also note that the copyright date on that book is 1977.  This is 8 years
…[10 more quoted lines elided]…
>> > PL/I

"few" years?  Surely you're not referring to X3.74 of 1987,
some ten years later?

> - and said that it was "functionally" frozen as a programming
>> >language
…[9 more quoted lines elided]…
> Mainframe PL/I compilers.

There's nothing new in this.  IBM's OS PL/I Version 2 object code was
incompatible with Version 1 object code, owing to changes with certain
library functions.

Also, different interfaces with various operating systems required
different object code for each different version.

>  Also, as far as I know, this NEW (incompatible)
> version of IBM's mainframe PL/I compiler

AFAIK, it's a new compiler, not a new version of the existing IBM Mainframe
compiler.

> finally has support for ANSI/ISO
> conforming PL/I (conforming to the now functionally stabilized compiler) even
> though most IBM PL/I programmers "hate" having PL/I behave (or limited) to
> Standard syntax and functionality.

That's their preference, of course.

> Even so, I still would say that there have been MORE significant changes to
> the IBM mainframe COBOLs than to the IBM mainframe PL/I compilers - since
> 1977.

What changes to IBM COBOL since 1977 do you think would affect Tucker's
ratings of COBOL vs PL/I ?  Bearing in mind that PL/I was then streets
ahead of COBOL in the areas cited.

>  However, that is a matter of opinion - but whatever you think about
> the amount or type of change, it is certainly true that any comparison made
> in 1977 has little to do with the language advantages, structure, or uses
>today.

See above.

---
Bill Klein
```

#### ↳ Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<7trb0s$sg2$1@nntp3.atl.mindspring.net>`
- **References:** `<or9M3.2034$_4.3415@newsfeeds.bigpond.com>`

```
robin <robin_v@bigpond.com> wrote in message
news:or9M3.2034$_4.3415@newsfeeds.bigpond.com...
> From: "William M. Klein" <wmklein@nospam.netcom.com>,
> MindSpring EnterprisesDate: Sat, 9 Oct 1999 11:38:48 -0500
> robin <robin_v@bigpond.com> wrote in message
> news:CpIL3.1233$_4.2153@newsfeeds.bigpond.com...
  <much snippage>
>
> What changes to IBM COBOL since 1977 do you think would affect Tucker's
> ratings of COBOL vs PL/I ?  Bearing in mind that PL/I was then streets
> ahead of COBOL in the areas cited.
>

Let's see what are just SOME of the changes to IBM's mainframe COBOL since
1977.

 - Scope-terminators and other "structured" constructs added
 - Intrinsic Functions
 - Native OO programming
 - Recursive Coding
 - CALL by VALUE, RETURNING, and other ILC enhancements for complete
availability of access to "Standard" API's
 - Pointers
 - Easy interface with LE callable services

If we were to look at the "What's new" section of each LRM for VS COBOL II (4
releases), COBOL/370, IBM COBOL for MVS & VM, and IBM COBOL for OS/390 & VM -
I am certain we would find plenty of other additions.

P.S. It is obviously "old news" and not really relevant any more, but would
like to comment on WHY IBM themselves, were so "hesitant" in adding PL/I to
SAA? Could it be that - unlike COBOL which was one of the first languages
added - they didn't really see the future for the customers in that language
across platforms.
```

##### ↳ ↳ Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** "Mark Yudkin" <myudkin@csi.com>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<7ts015$j2f$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<or9M3.2034$_4.3415@newsfeeds.bigpond.com> <7trb0s$sg2$1@nntp3.atl.mindspring.net>`

```
I think it is unfair to talk about IBM lack of commitment to PL/I, given the
evidence for increased support.

Yes, at one stage IBM was not keen on adding PL/I to SAA. After this
changed, compilers were released for OS/2, NT and AIX, and this compiler has
now been ported to OS/390.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7trb0s$sg2$1@nntp3.atl.mindspring.net...
> robin <robin_v@bigpond.com> wrote in message
> news:or9M3.2034$_4.3415@newsfeeds.bigpond.com...
…[23 more quoted lines elided]…
> If we were to look at the "What's new" section of each LRM for VS COBOL II
(4
> releases), COBOL/370, IBM COBOL for MVS & VM, and IBM COBOL for OS/390 &
VM -
> I am certain we would find plenty of other additions.
>
> P.S. It is obviously "old news" and not really relevant any more, but
would
> like to comment on WHY IBM themselves, were so "hesitant" in adding PL/I
to
> SAA? Could it be that - unlike COBOL which was one of the first languages
> added - they didn't really see the future for the customers in that
language
> across platforms.
>
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
