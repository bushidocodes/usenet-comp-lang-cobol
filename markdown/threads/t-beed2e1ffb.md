[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL calls to PL/I

_7 messages · 7 participants · 1998-09_

---

### COBOL calls to PL/I

- **From:** "Josep Llu���s" <jlluissanchez@hotmail.com>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36077B75.52651FA3@hotmail.com>`

```
 I need information about how to call PL/I programs from COBOL in
operating system IBM OS/390 2.4. I've been looking in my COBOL manuals
and it seems that this is possible but I don't found how and if there
are some restrictions (sure) and rules. Thank you very much and sorry by
the english level.
```

#### ↳ Re: COBOL calls to PL/I

- **From:** Rodger Whitlock <totototo+newsgroups@mail.pacificcoast.net>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pz1xU7SGdlOC@vmsmail.gov.bc.ca>`
- **References:** `<36077B75.52651FA3@hotmail.com>`

```
"Josep Lluï¿½s" <jlluissanchez@hotmail.com> wrote:
> I need information about how to call PL/I programs from COBOL in
>operating system IBM OS/390 2.4. I've been looking in my COBOL manuals
>and it seems that this is possible but I don't found how and if there
>are some restrictions (sure) and rules.

You may be looking in the wrong manuals. Look in the PL/I manuals instead.
```

##### ↳ ↳ Re: COBOL calls to PL/I

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u8rs4$75d@sjx-ixn1.ix.netcom.com>`
- **References:** `<36077B75.52651FA3@hotmail.com> <Pz1xU7SGdlOC@vmsmail.gov.bc.ca>`

```

Rodger Whitlock wrote in message ...
>"Josep Llu�s" <jlluissanchez@hotmail.com> wrote:
>> I need information about how to call PL/I programs from COBOL in
…[9 more quoted lines elided]…
>

Better yet,
  In the LE (Language Environment) "bookshelf," there is an entire manual
devoted to "interlanguage calls" (ILC).  Check that out.  If you need the
manual number or the online reference, please send me a note and I will get
it for you.
```

#### ↳ Re: COBOL calls to PL/I

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36083640.C25986E2@hankel.mersinet.co.uk>`
- **References:** `<36077B75.52651FA3@hotmail.com>`

```
Josep Lluï¿½s wrote:
> 
>  I need information about how to call PL/I programs from COBOL in
…[3 more quoted lines elided]…
> the english level.

There is no difference in calling PL/1 from COBOL than for any other
called program - the source language of the called program is not
relevant.
```

##### ↳ ↳ Re: COBOL calls to PL/I

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-tcdMQ3w2N9g2@Dwight_Miller.iix.com>`
- **References:** `<36077B75.52651FA3@hotmail.com> <36083640.C25986E2@hankel.mersinet.co.uk>`

```
On Tue, 22 Sep 1998 23:44:00, Charles F Hankel 
<charles@hankel.mersinet.co.uk> wrote:

> There is no difference in calling PL/1 from COBOL than for any other
> called program - the source language of the called program is not
> relevant.
>

Not true on all platforms.  It is true where PL/1 runs however.

On the PC, there is the Pascal calling convention, the C calling 
convention, COBOL and ASM and some others.
```

##### ↳ ↳ Re: COBOL calls to PL/I

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360ec76d.20458108@news3.ibm.net>`
- **References:** `<36077B75.52651FA3@hotmail.com> <36083640.C25986E2@hankel.mersinet.co.uk>`

```
In comp.lang.cobol, Charles F Hankel <charles@hankel.mersinet.co.uk>
wrote:

>There is no difference in calling PL/1 from COBOL than for any other
>called program - the source language of the called program is not
>relevant.

I can't speak to the current versions, but in the past this statement
would not be correct for PL/1 subroutines.. In order for a PL/1
program to be called you had to call a PL/1  service module
(PLISTART?) to establish and maintain the environment before the first
call was made to a PL/1 subroutine. There were also a number of
gotchas because of differing data types, array handling and unique
paramete list issues.

			Scott Peterson
```

###### ↳ ↳ ↳ Re: COBOL calls to PL/I

- **From:** fboll@aol.com (FBoll)
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980924132835.16401.00001182@ng-fb2.aol.com>`
- **References:** `<360ec76d.20458108@news3.ibm.net>`

```

>I can't speak to the current versions, but in the past this statement
>would not be correct for PL/1 subroutines.. In order for a PL/1
…[6 more quoted lines elided]…
>

Scott:
Like you I can't speak to the current versions, but I do remember that the
overhead in establishing the PL/1 environment from a COBOL call  was staggering
from a system resources perspective. So much so that we (NYTel) programmers
were prohibited from doing so. 
Frank J. Boll
Computer Solutions
This message printed on recycled disk space
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
