[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mouse & COBOL

_3 messages · 3 participants · 1999-11_

---

### mouse & COBOL

- **From:** "Nick de Graeve" <de.graeve@village.uunet.be>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80e6nb$40c$1@xenon.inbe.net>`

```
Hi,

I made a small DOS-program with 3 screens and some "buttons". I wanted, when
I click on those buttons, to go from one screen to the others but wherever I
click I get, at the bottom of the screen, the message "There is no field
beyond here". It seems that ACCEPT doesn't accept my mouse clicks. Got any
suggestions? Thank you,

Nick.

PS.
I use the MicroFocus/Microsoft 4.5 Compiler.
```

#### ↳ Re: mouse & COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382AFC20.95AE010A@home.com>`
- **References:** `<80e6nb$40c$1@xenon.inbe.net>`

```


Nick de Graeve wrote:
> 
> Hi,
…[5 more quoted lines elided]…
> suggestions? Thank you,

Nick.

I don't know M/F V 4.5 but do you have the CBL_ routines which include
use of Mouse. Suggest you post the source of your programs to this
NewsGroup, then somebody will be able to help.

Jimmy, Calgary AB
```

#### ↳ Re: mouse & COBOL

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80et5r$291$1@hyperion.mfltd.co.uk>`
- **References:** `<80e6nb$40c$1@xenon.inbe.net>`

```
Nick,

When you use the mouse with ACCEPTs the only thing you can use it for is to
reposition the cursor at the mouse position. If there is no field at that
position, or you are beyond the end of the data in the field you will get
the message mentioned. That is correct behaviour.

The behaviour of the mouse can, however, be configured using the Key Control
option in ADISCF. I do not know whether you will be able to do what you want
but at least it gives you some possibilities.

Nick de Graeve wrote in message <80e6nb$40c$1@xenon.inbe.net>...
>Hi,
>
>I made a small DOS-program with 3 screens and some "buttons". I wanted,
when
>I click on those buttons, to go from one screen to the others but wherever
I
>click I get, at the bottom of the screen, the message "There is no field
>beyond here". It seems that ACCEPT doesn't accept my mouse clicks. Got any
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
