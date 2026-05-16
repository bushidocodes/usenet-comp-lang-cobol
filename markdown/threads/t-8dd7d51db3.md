[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: How do I convert between types in Cobol? (long)

_2 messages · 2 participants · 1994-12_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Q: How do I convert between types in Cobol? (long)

- **From:** ito@htk.hitachi-cable.co.jp (Ito Kazumitsu)
- **Date:** 1994-12-01T23:54:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ITO.94Dec2085423@johp400.htk.hitachi-cable.co.jp>`
- **In-Reply-To:** `dewar@cs.nyu.edu's message of 30 Nov 1994 18:03:38 -0500`
- **References:** `<58183.cmorris@fox.nstn.ns.ca> <ITO.94Nov29142731@johp400.htk.hitachi-cable.co.jp> <3bj0ca$lci@gnat.cs.nyu.edu>`

```
In article <3bj0ca$lci@gnat.cs.nyu.edu> dewar@cs.nyu.edu (Robert Dewar) writes:

>   I hate seeing code like:
>
…[5 more quoted lines elided]…
>   the semantics of compute is implementation dependent.

I agree with you in that the semantics of compute is implementation dependent.
And my original code:

		COMPUTE WS-COMP-2 = S2N-A / S2N-N

really had a bad problem, so I corrected it this way:

                MOVE S2N-A TO WS-COMP-2
		COMPUTE WS-COMP-2 = WS-COMP-2 / S2N-N

I still use COMPUTE just because the verb COMPUTE is more familiar to me
(and for not a few non-English-speaking people, I think) than those verbs
like MULTIPLY or DIVIDE. It is not easy for me to understand that

               DIVIDE X INTO Y

means

               COMPUTE Y = Y / X

If the syntax and semantics of DIVIDE were like this:

               DIVIDE X BY Y
means
               COMPUTE X = X / Y

then I would be pleased to use DIVIDE instead of COMPUTE.
```

#### ↳ Re: Q: How do I convert between types in

- **From:** Richard_Plinston@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1994-12-02T19:51:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3294335.71498.7453@kcbbs.gen.nz>`
- **References:** `<ITO.94Dec2085423@johp400.htk.hitachi-cable.co.jp>`

```

>I still use COMPUTE just because the verb COMPUTE is more familiar to me
>(and for not a few non-English-speaking people, I think) than those verbs
…[14 more quoted lines elided]…
>then I would be pleased to use DIVIDE instead of COMPUTE.

The 'rule' here is that the result is placed in the final operand.
Divide X into Y, Multiply X by Y, Add X to Y, Subtract X from Y;
the result is in Y.  Any GIVING makes that the final operand, and
thus is the result.  Divide X by Y cannot be used without giving
as it would break the rule if the result went to X.

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
