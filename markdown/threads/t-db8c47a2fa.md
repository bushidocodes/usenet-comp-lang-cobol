[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Binary Search Compares

_6 messages · 4 participants · 1998-11_

---

### Binary Search Compares

- **From:** Rob Anderson <rta@2xtreme.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363D2F54.ABA335B7@2xtreme.net>`

```
I have an assignment for COBOL class that ask us to find the number of
compare for different size tables.  Unfortunately, i can't find the
formula for a binary search.  Does anyone know the formula for
calculating the number of campares for  given table size for a binay
search?

RTA
```

#### ↳ Re: Binary Search Compares

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363d38d7.0@news1.ibm.net>`
- **References:** `<363D2F54.ABA335B7@2xtreme.net>`

```
Rob Anderson wrote in message <363D2F54.ABA335B7@2xtreme.net>...
>I have an assignment for COBOL class that ask us to find the number of
>compare for different size tables.  Unfortunately, i can't find the
>formula for a binary search.  Does anyone know the formula for
>calculating the number of campares for  given table size for a binay
>search?


1 for size of 1
2 for size of 3
3 for size of 5
4 for size of 9
5 for size of 17
6 for size of 33
7 for size of 65
8 for size of 129
...
log2(n) for size of 2**n+1
```

##### ↳ ↳ Re: Binary Search Compares

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363E2E8B.DF17924@IMN.nl>`
- **References:** `<363D2F54.ABA335B7@2xtreme.net> <363d38d7.0@news1.ibm.net>`

```
Leif Svalgaard wrote:

> Rob Anderson wrote in message <363D2F54.ABA335B7@2xtreme.net>...

8<

> >Does anyone know the formula for
> >calculating the number of campares for  given table size for a binay
> >search?

8<

> log2(n) for size of 2**n+1

? Think you did mean log2(n) for size n+1
Or n for size 2**n+1

Or, ceil(log2(n)) for size n?

The Frog.

Note: It is late, here&now: 23:12 in the NL. Excuses in advance, my math
mostly gets wrong.
```

##### ↳ ↳ Re: Binary Search Compares

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71nhfr$jbs$1@news-inn.inet.tele.dk>`
- **References:** `<363D2F54.ABA335B7@2xtreme.net> <363d38d7.0@news1.ibm.net>`

```

Leif Svalgaard skrev i meddelelsen <363d38d7.0@news1.ibm.net>...
>Rob Anderson wrote in message <363D2F54.ABA335B7@2xtreme.net>...
>>I have an assignment for COBOL class that ask us to find the number of
…[16 more quoted lines elided]…
>

I guess you mean either

"n for size of 2**n + 1"

or

"log2(n-1) for size of n" ?

Kennet
```

###### ↳ ↳ ↳ Re: Binary Search Compares

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363f4a62.0@news1.ibm.net>`
- **References:** `<363D2F54.ABA335B7@2xtreme.net> <363d38d7.0@news1.ibm.net> <71nhfr$jbs$1@news-inn.inet.tele.dk>`

```

kennet wrote in message <71nhfr$jbs$1@news-inn.inet.tele.dk>...
>
>Leif Svalgaard skrev i meddelelsen <363d38d7.0@news1.ibm.net>...
…[24 more quoted lines elided]…
>Kennet


yes, of course, but I didn't want to do all his homework.
From what I said he should be able to figure it out.
```

###### ↳ ↳ ↳ Re: Binary Search Compares

_(reply depth: 4)_

- **From:** Rob Anderson <rta@2xtreme.net>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363FE30E.7C26D6C1@2xtreme.net>`
- **References:** `<363D2F54.ABA335B7@2xtreme.net> <363d38d7.0@news1.ibm.net> <71nhfr$jbs$1@news-inn.inet.tele.dk> <363f4a62.0@news1.ibm.net>`

```
Thanks...I figured it out.

Rob

Leif Svalgaard wrote:

> kennet wrote in message <71nhfr$jbs$1@news-inn.inet.tele.dk>...
> >
…[28 more quoted lines elided]…
> From what I said he should be able to figure it out.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
