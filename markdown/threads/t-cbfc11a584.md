[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO-COBOL and java Dynamic call to subroutine

_4 messages · 3 participants · 2009-02_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Re: OO-COBOL and java Dynamic call to subroutine

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-02-25T16:24:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49A570D4.6F0F.0085.0@efirstbank.com>`

```
It's unfortunate they named the options DYNAM and NODYNAM.  It really should
be DYNAMALWAYS and NODYNAMALWAYS.

n 2/24/2009 at 8:54 PM, in message
<Qh3pl.54057$Rp1.2394@en-nntp-01.dc1.easynews.com>, William M.
Klein<wmklein@nospam.ix.netcom.com> wrote:
> First, to those who don't recognize the "buzz-words", this must be for 
> Enterprise COBOL on z/OS.
…[9 more quoted lines elided]…
>
```

#### ↳ Re: OO-COBOL and java Dynamic call to subroutine

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-25T18:52:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CJlpl.131375$pp1.40382@en-nntp-06.dc1.easynews.com>`
- **References:** `<49A570D4.6F0F.0085.0@efirstbank.com>`

```
<G> How about
  DYNAM(ALWAYS)
     versus
  DYNAM(SOMETIMES)
   ???
```

##### ↳ ↳ Re: OO-COBOL and java Dynamic call to subroutine

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-26T13:15:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<go64lp$4l5$3@reader1.panix.com>`
- **References:** `<49A570D4.6F0F.0085.0@efirstbank.com> <CJlpl.131375$pp1.40382@en-nntp-06.dc1.easynews.com>`

```
In article <CJlpl.131375$pp1.40382@en-nntp-06.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
><G> How about
>  DYNAM(ALWAYS)
>     versus
>  DYNAM(SOMETIMES)
>   ???

I'm glad someone else picked up on that... I was getting ready to trot out 
the lack of a DWIM (Do What I Mean) command for it.

DD
```

#### ↳ Re: OO-COBOL and java Dynamic call to subroutine

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-26T13:14:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<go64jk$4l5$2@reader1.panix.com>`
- **References:** `<49A570D4.6F0F.0085.0@efirstbank.com>`

```
In article <49A570D4.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>It's unfortunate they named the options DYNAM and NODYNAM.  It really should
>be DYNAMALWAYS and NODYNAMALWAYS.

Hey... *any* ASM-jockey worth their paycheck will know that *any* and 
*all* concepts and descriptions can be transmitted in eight characters or 
fewer!

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
