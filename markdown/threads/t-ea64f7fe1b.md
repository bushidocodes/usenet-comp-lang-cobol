[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Function Keys

_3 messages · 3 participants · 2002-12_

---

### Function Keys

- **From:** "BRaTaX CK" <bratax@pandora.be>
- **Date:** 2002-12-15T10:59:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gZK9.51531$Ti2.8053@afrodite.telenet-ops.be>`

```
Hey guys,

I'm working with function keys for the first time and I have a little
problem.

I wanted to make a menu where I can choose between:
- pushing on the arrow buttons to choose an option, and press enter to
confirm
- just enter a number

I was wondering if anybody has a list with all function keys (i'm using MF
Cobol, didn't manage to find one on Google), so that I can include an
if-statement that says:
IF arrow-up OR arrow-down OR ent OR esc THEN run-code-1
IF numberbutton1 OR numberbutton2 OR... THEN run-code-2

(I only know the value of the function keys "escape", "enter", "arrow-up"
and "arrow-down", so this part of my code works perfect, the problem is the
numberbuttons)

Thanks in advance,

Vincent
```

#### ↳ Re: Function Keys

- **From:** "Chris Keavy" <ckeavy@cox.net>
- **Date:** 2002-12-17T03:02:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttwL9.431$I23.105854@news1.east.cox.net>`
- **References:** `<3gZK9.51531$Ti2.8053@afrodite.telenet-ops.be>`

```
"BRaTaX CK" wrote
> I was wondering if anybody has a list with all function keys (i'm using MF
> Cobol, didn't manage to find one on Google), so that I can include an
> if-statement that says:

Vincent,

     Just make a quick test program that will DISPLAY the value of the key
after you hit it.  You can build up a chart in no time.

Chris
```

##### ↳ ↳ Re: Function Keys

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-31T05:16:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021231001619.06965.00000433@mb-cj.aol.com>`
- **References:** `<ttwL9.431$I23.105854@news1.east.cox.net>`

```
     in the personal cobol (dos) from micro focus, look in sub directory
mfcobol. then look in sub sub directory samples.
  look for the file  funkey.cbl  which also includes a para as follows:
   tell-which-function-key-was-pressed
(spelling may be off)  take a look.

if you have the windows version of microfocus cobol.  it should be in pcobwin
directory -  sub sub directory is samples and its there ( funkey.cbl)  
        hope this helps
            RonGlaz@juno.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
