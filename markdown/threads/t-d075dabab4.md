[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Usage of COMP-5

_2 messages · 2 participants · 2009-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Usage of COMP-5

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-11-16T16:59:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YaudnZXSA-ehRJzWnZ2dnUVZ_uWdnZ2d@earthlink.com>`
- **References:** `<e7abbcfc-95c1-4dbb-b180-e36365b4e52a@g1g2000pra.googlegroups.com>`

```
Rene_Surop wrote:
>
> Is it really therefore safe to say that binary numeric data is for
> "computations" only and not safe for data storage?

Oh, it's safe enough to store numbers as binary, but they have other 
problems.

In our shop, binary usage is reserved for passing variables between units 
and for internal things like subscripts.

Any numeric value that gets written to a (non-temp) file is in display mode, 
even though it might subsequently used in a computation (i.e., hourly 
salary).

Further, if you can't do arithmetic on it, a variable is NEVER written as 
numeric display. Things like postal codes, telephone numbers, Social 
Security Number, and the like are not "numbers" and should not be treated as 
such.
```

#### ↳ Re: Usage of COMP-5

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-11-17T08:48:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jch5g5h9j5pcv3dro50ekdbilr7jhku8tv@4ax.com>`
- **References:** `<e7abbcfc-95c1-4dbb-b180-e36365b4e52a@g1g2000pra.googlegroups.com> <YaudnZXSA-ehRJzWnZ2dnUVZ_uWdnZ2d@earthlink.com>`

```
On Mon, 16 Nov 2009 16:59:05 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>Further, if you can't do arithmetic on it, a variable is NEVER written as 
>numeric display. Things like postal codes, telephone numbers, Social 
>Security Number, and the like are not "numbers" and should not be treated as 
>such. 

At one time, there was an argument for compressing a SSAN into less
space.    But it is my opinion that most people who store it as PIC
9(09) did so because they were not thinking.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
