[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus 3.2.xx question ?

_5 messages · 4 participants · 1998-02 → 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus 3.2.xx question ?

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-02-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980227021101.VAA27174@ladder02.news.aol.com>`

```

Hi,

I have developed a DOS application (6.22) with MicroFocus 3.2.24. I have
package the file as a LBR. The file is made up of the following:
program1.gnt
program2.gnt
program2.g01
program3.gnt
program3.g01
program4.gnt
program5.gnt
program5.g01

The size of the library is about 420,000 bytes. For the most part everything
functions fine. However every once in a while i get strange lock problems.
Usually if i change the memory configuration the problems go away.

Has anyone had problems like this ? Does the fact that some of my programs are
G01 files indicate anything ?

Thanks in advance for any help you can offer.

Bob
```

#### ↳ Re: MicroFocus 3.2.xx question ?

- **From:** "neal denison" <ua-author-17074517@usenetarchives.gap>
- **Date:** 1998-02-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cdb3fc8eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980227021101.VAA27174@ladder02.news.aol.com>`
- **References:** `<19980227021101.VAA27174@ladder02.news.aol.com>`

```

Did you use the 01shuffle directive? The .g01's were generated because
your programs are large. If you're in the gnt and try to access data in
the .g01 it might not be getting to it.
You might try to break your programs into smaller units if possible.
Neal
```

#### ↳ Re: MicroFocus 3.2.xx question ?

- **From:** "einar clementz" <ua-author-6588781@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cdb3fc8eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19980227021101.VAA27174@ladder02.news.aol.com>`
- **References:** `<19980227021101.VAA27174@ladder02.news.aol.com>`

```

Hi Bob

MF 3.2 is 16 bits, that one thing. You should make an upgrade to 3.2.50, that level
has more stability, but its stil 16 bits.
Your G01 comes from that you have large working storage. The compiler generates
this G01 (and G0X) when WS is to large for one GNT and put in some code so the
runtime can keep track of where it is. This can certely make some errors dpending
on difference in data.

The best You could do is to get the 4.0.xx, that is 32 bits and this will probably
get rid of the problem. You could also try to organize Your memory usage a little
better.

Einar Clementz, Oslo, Norway


Bob7536 wrote:

› Hi,
› 
…[20 more quoted lines elided]…
› Bob
```

##### ↳ ↳ Re: MicroFocus 3.2.xx question ?

- **From:** "einar clementz" <ua-author-6588781@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cdb3fc8eb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9cdb3fc8eb-p3@usenetarchives.gap>`
- **References:** `<19980227021101.VAA27174@ladder02.news.aol.com> <gap-9cdb3fc8eb-p3@usenetarchives.gap>`

```

› Hi Bob
› 
…[12 more quoted lines elided]…
› 

Hi again.

I did put a missleading information to You.
It is the code part, not the data part, of the program that is the reason for the
compiler to make segments.
You learn new things every day.

Thanks to the person telling me this.

Einar


› Bob7536 wrote:
› 
…[22 more quoted lines elided]…
›› Bob
```

###### ↳ ↳ ↳ Re: MicroFocus 3.2.xx question ?

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cdb3fc8eb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9cdb3fc8eb-p4@usenetarchives.gap>`
- **References:** `<19980227021101.VAA27174@ladder02.news.aol.com> <gap-9cdb3fc8eb-p3@usenetarchives.gap> <gap-9cdb3fc8eb-p4@usenetarchives.gap>`

```

Bon,

Einar is correct.

Hope this helps.

Paddy Coleman, Distributed Computing Support (WinTel)
Micro Focus UK

Einar Clementz wrote in message <34F··.@big··t.com>...
›› Hi Bob
›› 
…[73 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
