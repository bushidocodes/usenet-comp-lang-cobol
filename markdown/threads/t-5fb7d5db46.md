[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol650 problem

_2 messages · 2 participants · 1997-11_

---

### Cobol650 problem

- **From:** "d..." <ua-author-8935123@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65ga4b$jom$1@juliana.sprynet.com>`

```

I am new to cobol programming and I downloaded the cobol6.5 freeware
compiler. The problem is when I try to compile a program I get the
following error message: "FCB unavailable
Abort,Fail? "

Can anyone tell me what this means. Thanks in advance.

D
```

#### ↳ Re: Cobol650 problem

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fb7d5db46-p2@usenetarchives.gap>`
- **In-Reply-To:** `<65ga4b$jom$1@juliana.sprynet.com>`
- **References:** `<65ga4b$jom$1@juliana.sprynet.com>`

```

duke (d.··.@spr··t.com) wrote:
: I am new to cobol programming and I downloaded the cobol6.5 freeware
: compiler. The problem is when I try to compile a program I get the
: following error message: "FCB unavailable
: Abort,Fail? "
(SNIP)
---------------------------------------

A FCB is a DOS file control block. They are used by older programs to
access files.

The default number is 4. You can change it by either adding or changing
the FCBS command in your CONFIG.SYS file.

You didn't say what version of DOS you are using. Either look in your
DOS manual or enter: help on the k/b and look for FCBS for more info.

If you are running Windows 95, this may or may not apply (I don't have
95).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
