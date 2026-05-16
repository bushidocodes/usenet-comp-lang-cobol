[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobcap file

_5 messages · 2 participants · 1998-11_

---

### cobcap file

- **From:** "Paulo" <c.m@mail.telepac.pt>
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<733k73$r7p$1@duke.telepac.pt>`

```
on the older cobol compiler (MF Cobol /2 v.1.1) i've a file named 'cobcap',
this file is :
PRINTER01:W:lp:-s:-dprinter_device_name
PRINTER02...... and so on

to print from the cobol i've just to assign the 'PRINTER01' (ex) to the
SELECT clause. Can you tell me if this 'cobcap' is crated by any mf prog ?
or it is already configured ?

If possible show me a sample how can use it. Thanks

Paulo
c.m@mail.telepac.pt
```

#### ↳ Re: cobcap file

- **From:** g1dlc@Radix.Net (David L. Craig)
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73br0l$8jc$1@saltmine.radix.net>`
- **References:** `<733k73$r7p$1@duke.telepac.pt>`

```
In article <733k73$r7p$1@duke.telepac.pt>, Paulo <c.m@mail.telepac.pt> wrote:
>on the older cobol compiler (MF Cobol /2 v.1.1) i've a file named 'cobcap',
>this file is :
…[7 more quoted lines elided]…
>If possible show me a sample how can use it. Thanks

Wow, that's a pretty old version!  I'm no expert in
the older features, and I suspect there is no comparable
feature in the current products, although the 16-bit
compiler might have this.  Maybe Kevin can enlighten us.
I suspect the DD_xxxx='<lpr' method is your only
reasonable approach.  The Compatibility Guide doesn't
mention a cobcap feature, so I'm at a loss.  Where and
how was this discussed in your compiler's documentation?
```

##### ↳ ↳ Re: cobcap file

- **From:** "Paulo" <c.m@mail.telepac.pt>
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73bsbr$m42$1@duke.telepac.pt>`
- **References:** `<733k73$r7p$1@duke.telepac.pt> <73br0l$8jc$1@saltmine.radix.net>`

```
Hi David!

No idea where it came from, this old version came like this from a friend of
mine for evaluation .-( and no manual included of cuorse! Now when i've
bought the v.3.2.20 (2nd hand), i saw no comments about this 'cobcap' file.
It was usefull !

thanks

Paulo

David L. Craig escreveu na mensagem <73br0l$8jc$1@saltmine.radix.net>...
>In article <733k73$r7p$1@duke.telepac.pt>, Paulo <c.m@mail.telepac.pt>
wrote:
>>on the older cobol compiler (MF Cobol /2 v.1.1) i've a file named
'cobcap',
>>this file is :
>>PRINTER01:W:lp:-s:-dprinter_device_name
…[15 more quoted lines elided]…
>how was this discussed in your compiler's documentation?
```

###### ↳ ↳ ↳ Re: cobcap file

- **From:** g1dlc@Radix.Net (David L. Craig)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73elrf$6oc$1@saltmine.radix.net>`
- **References:** `<733k73$r7p$1@duke.telepac.pt> <73br0l$8jc$1@saltmine.radix.net> <73bsbr$m42$1@duke.telepac.pt>`

```
In article <73bsbr$m42$1@duke.telepac.pt>, Paulo <c.m@mail.telepac.pt> wrote:
>It was usefull !
>David L. Craig escreveu na mensagem <73br0l$8jc$1@saltmine.radix.net>...
>>I suspect the DD_xxxx='<lpr' method is your only
>>reasonable approach.
It will be more useful if you, unlike me, use the
correct angle bracket (DD_xxxx='>lpr').  I really
need to work more on my proofreading...
```

###### ↳ ↳ ↳ Re: cobcap file

_(reply depth: 4)_

- **From:** "Paulo" <c.m@mail.telepac.pt>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73en88$2v0$1@duke.telepac.pt>`
- **References:** `<733k73$r7p$1@duke.telepac.pt> <73br0l$8jc$1@saltmine.radix.net> <73bsbr$m42$1@duke.telepac.pt> <73elrf$6oc$1@saltmine.radix.net>`

```

David L. Craig escreveu na mensagem <73elrf$6oc$1@saltmine.radix.net>...
>In article <73bsbr$m42$1@duke.telepac.pt>, Paulo <c.m@mail.telepac.pt>
wrote:
>>It was usefull !
>>David L. Craig escreveu na mensagem <73br0l$8jc$1@saltmine.radix.net>...
…[4 more quoted lines elided]…
>need to work more on my proofreading...

I've understand it ! Thanks !
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
