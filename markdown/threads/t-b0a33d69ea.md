[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inline asembler

_3 messages · 2 participants · 1996-03 → 1996-04_

---

### Inline asembler

- **From:** "daniel...." <ua-author-17086716@usenetarchives.gap>
- **Date:** 1996-03-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4jmar6$b89@ping1.ping.be>`

```
Hi,

Can someone tell me how I can use inline asm in MS COBOL 5.0 on a
normal MS-DOS PC ?
The following code (inline asm in C) must be translated

=== Cut ===
#include

void SetBlinkOn()
{
asm{
mov AX,1003H
mov BX,0001
int 10h
}
}

void SetBlinkOff()
{
asm{
mov ax,1003h
mov bx,0000
int 10h
}
}

void cursoroff()
{
unsigned int ffff = 0xffff;
asm{ mov ah, 03h
mov bh, 00h
int 10h
mov crstyp, cx
mov ah, 01h
mov cx, ffff
int 10h
}
}

void cursoron()
{
asm{ mov ah, 01h
mov cx, crstyp
int 10h
}
}

unsigned int getcursor() // Returns the cursor format.
{
unsigned int tempword;
asm{ mov ah, 03h
mov bh, 00h
int 10h
mov tempword,cx
}
return tempword;
}

void setcursor(unsigned int curstype) // Sets the cursor format.
{
unsigned int tempword;
tempword=curstype;
asm{ mov ah, 01h
mov cx,tempword
int 10h
}
}
=== Cut ===

thx in advance,



Daniel
```

#### ↳ Re: Inline asembler

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-04-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0a33d69ea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4jmar6$b89@ping1.ping.be>`
- **References:** `<4jmar6$b89@ping1.ping.be>`

```
In message <<4jmar6$b.··.@pin··g.be>> Dan··.@pi··g.be writes:
›
› Can someone tell me how I can use inline asm in MS COBOL 5.0 on a
› normal MS-DOS PC ?
› The following code (inline asm in C) must be translated

Page 299 of the System Reference manual will give you a description
of the CALL x"84" routine which allows you to do the things you
want.
```

##### ↳ ↳ Re: Inline asembler

- **From:** "daniel...." <ua-author-17086716@usenetarchives.gap>
- **Date:** 1996-04-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0a33d69ea-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0a33d69ea-p2@usenetarchives.gap>`
- **References:** `<4jmar6$b89@ping1.ping.be> <gap-b0a33d69ea-p2@usenetarchives.gap>`

```
rip··.@kcb··n.nz (Richard Plinston) wrote:



›› Can someone tell me how I can use inline asm in MS COBOL 5.0 on a
›› normal MS-DOS PC ?
›› The following code (inline asm in C) must be translated
 
› Page 299 of the System Reference manual will give you a description
› of the CALL x"84" routine which allows you to do the things you
› want.

The problem is, I'm writing a program for school and have a licence to
use the compiler from the high school. Sow I don't have the reference
manual. I will ask for it, when I go back to school, for the moment,
I'home for Easter.

I suppose you can not give me an example on how to use inline
assembler ?


Greetings,

Daniel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
