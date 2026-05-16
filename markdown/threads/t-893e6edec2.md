[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# extf and C

_3 messages · 2 participants · 2005-09 → 2005-10_

---

### extf and C

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2005-09-27T10:34:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43390228$0$21684$ba620e4c@news.skynet.be>`

```
Hello,

Does someone has a small example of a C program calling the extfh module
from Micro Focus ?
I could only find an example of a cobol program calling extfh. I should
be possible from C.

I thank you.

Best regards.

Alain Reymond
```

#### ↳ Re: extfh and C

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2005-10-07T08:48:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43461858$0$14828$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<43390228$0$21684$ba620e4c@news.skynet.be>`
- **References:** `<43390228$0$21684$ba620e4c@news.skynet.be>`

```
I did not write it correctly : it was extfh instead of extf.
I think that everybody saw it.

Regards.

Alain Reymond a ï¿½crit :
> Hello,
> 
…[9 more quoted lines elided]…
> Alain Reymond
```

##### ↳ ↳ Re: extfh and C

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-07T00:37:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1128670663.189610.95490@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<43461858$0$14828$ba620e4c@news.skynet.be>`
- **References:** `<43390228$0$21684$ba620e4c@news.skynet.be> <43461858$0$14828$ba620e4c@news.skynet.be>`

```
> I did not write it correctly : it was extfh instead of extf.
> I think that everybody saw it.

I did write a test C program using extfh many years ago, but it has
been lost. It was using the dos MF 3.x (or possibly 2.x) version but I
do recall that version did not work correctly for C and needed some
nasty code to recover the stack correctly. I am sure that it was fixed
in a later version.

It does need some accurate setting up of the FCD and key structs to get
perfect alignment but should work.  There was an example included with
MF - extfhrd.c

It may be arguable whether it is licensed for use and distribution. If
you are a licenced developer then you can use the code and can
distribute it with licensed runtimes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
