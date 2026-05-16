[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Binary Storage of PICs

_3 messages · 3 participants · 2000-05_

---

### Binary Storage of PICs

- **From:** "John W. Hom" <j.hom.1@alumni.nyu.edu>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392AE4D6.9BE771B2@alumni.nyu.edu>`

```
How are the following stored, in binary,

05 value1 PIC S9        VALUE +1.
05 value2 PIC  9        VALUE  1.
05 value3 PIC S9 COMP-3 VALUE +1.
05 value4 PIC  9 COMP-3 VALUE  1.

I'm thinking

value1: 0000 0001  0000 1100 (2-bytes)
           0    1     0    +

        Store each digit in it's own byte with the lowest
        order byte holding the sign ('+' = 1100, and
        '-' = 1101).

value2: 0000 0001 (1-byte)
           0    1

        Store each digit in it's own byte -- there is no
        sign to worry about.

value3: 0001 1100 (1-byte)
           1    +

        Store each digit in it's own nybble (4-bits) with
        the lowest order nybble holding the sign.

value4: 0000 0001 (1-byte)
           0    1

        Store each digit in it's own nybble -- there is no
        sign bit to worry about.

Am I right?  If possible, could you reply to both me and the
group?

Thanks,

John
```

#### ↳ Re: Binary Storage of PICs

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gfbpi$5q40$1@newssvr04-int.news.prodigy.com>`
- **References:** `<392AE4D6.9BE771B2@alumni.nyu.edu>`

```

value1    X'C1'
value2    X'F1'
value3    X'1C'
value4    X'1F'
If sign separate clause is used, the above would not be true.

John W. Hom <j.hom.1@alumni.nyu.edu> wrote in message
news:392AE4D6.9BE771B2@alumni.nyu.edu...
> How are the following stored, in binary,
>
…[3 more quoted lines elided]…
> 05 value4 PIC  9 COMP-3 VALUE  1.
```

#### ↳ Re: Binary Storage of PICs

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GqOW4.97$QQ6.9283@dfiatx1-snr1.gtei.net>`
- **References:** `<392AE4D6.9BE771B2@alumni.nyu.edu>`

```
COMP (binary) data is almost always stored in mulitples of eight bits, even
if less space is required. COMP data is, by definition,
"implementor-defined".  IBM mainframe COBOL uses a scheme in which all data
is stored in 16 or 32 bits de (called "word" alignment); but MF Personal
COBOL for DOS uses "byte" alignment, in which only the minium number of
whole bytes is used.


BUT...

If you really want to understand COBOL data types and storage, you simply
MUST download the text and graphics tutorial on the topic at
http://www.flexus.com/softwaredownload.html. Get file COBDATA.ZIP.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
