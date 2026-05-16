[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# More Packed Decimal Help

_2 messages · 2 participants · 2000-02_

---

### More Packed Decimal Help

- **From:** wax_man@my-deja.com
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87rth9$dkh$1@nnrp1.deja.com>`

```
Thanks for the help I've been given so far.

Now I'm trying to verify what some packed values should come out as and
have run into a problem.  How do you handle decimals?

I know that 331 = 00110011 00011111 after packing.  However, what
should 331.01 pack out to?  What is the generic rule for packing with a
decimal?

Thanks,

chris


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: More Packed Decimal Help

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A17DF2.585B488B@cusys.edu>`
- **References:** `<87rth9$dkh$1@nnrp1.deja.com>`

```


wax_man@my-deja.com wrote:

> Thanks for the help I've been given so far.
>
…[5 more quoted lines elided]…
> decimal?

Same thing.  The program keeps track of the implied decimal, it really
isn't there.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
