[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INCLUDE statement??

_2 messages · 2 participants · 1999-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### INCLUDE statement??

- **From:** geenidee@my-dejanews.com
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c5i74$bgp$1@nnrp1.dejanews.com>`

```
What does the next code means :

01 FIELD1    INCLUDE FIELD2.

will the FIELD2 sub definitions be matched with FIELD1 like :
01 FIELD2.
  05 AA PIC XX.
  05 BB PIC 99.

will result in the equivalent :
01 FIELD1.
  05 AA PIC XX.
  05 BB PIC 99.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: INCLUDE statement??

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tkHF2.3676$Ek.6326005@news1.mia>`
- **References:** `<7c5i74$bgp$1@nnrp1.dejanews.com>`

```
YES

geenidee@my-dejanews.com wrote in message
<7c5i74$bgp$1@nnrp1.dejanews.com>...
>What does the next code means :
>
…[13 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
