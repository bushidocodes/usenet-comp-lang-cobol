[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need URGENT help on Microfocus Netexpress Screen

_8 messages · 7 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Need URGENT help on Microfocus Netexpress Screen

- **From:** "Hugh Tran" <hugh_tran@hotmail.com>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bj0bi$e19$1@news1.mpx.com.au>`

```
Hi there,

I am using Microfocus Netexpress 2.0 on windows 95/NT PCs. I ahve a "screen
section" to define my screen layout and the screen variables. This is only a
TEXT screen -- NOT a GUI.

I am not able to do:

(1) I want all input fields to be underlined. I can make them reverse-video
using Adis BUT underlining is easier on the eyes. HOW???

(2) When I use the TAB or arrow keys (down, up, left and right), the cursor
moves to the next or previous screen input fields. I would like to make it
so that when I press the down arrow key, the cursor jumps to the input field
DIRECTLY or IN-DIRECTLY below the current input field. I am able to achieve
this ONLY if the input field is DIRECTLY below the current one. HOW????

Thanks in a million


hugh_tran@hotmail.com
```

#### ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-U1dfTfkBJWgX@Dwight_Miller.iix.com>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au>`

```
On Wed, 3 Mar 1999 09:37:31, "Hugh Tran" <hugh_tran@hotmail.com> 
wrote:

> Hi there,
> 
…[8 more quoted lines elided]…
> 

When I last attempted this, I too failed.  MicroFocus has the best 
screen section I have worked with, but I never could get underline 
support to work.  It's not supported for DOS/WINDOWS that I can see.

> (2) When I use the TAB or arrow keys (down, up, left and right), the cursor
> moves to the next or previous screen input fields. I would like to make it
> so that when I press the down arrow key, the cursor jumps to the input field
> DIRECTLY or IN-DIRECTLY below the current input field. I am able to achieve
> this ONLY if the input field is DIRECTLY below the current one. HOW????

Redefine the down arrow to be a TAB key with an ADIS call. It is one 
of the X"AF" calls. MAKE SURE to re-map the key upon exit.
```

##### ↳ ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bko92$6ko@lotho.delphi.com>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au> <Jl0PnHJ5PvPd-pn2-U1dfTfkBJWgX@Dwight_Miller.iix.com>`

```
You cannot do underlining on VGA. It just doesn't work. :) 
-Paul

Some compielrs fake it out with a series of underlines, but ther eis
no TRUE underlining. 



Thane Hubbell (redsky@ibm.net) wrote:
: On Wed, 3 Mar 1999 09:37:31, "Hugh Tran" <hugh_tran@hotmail.com> 
: wrote:

: > Hi there,
: > 
: > I am using Microfocus Netexpress 2.0 on windows 95/NT PCs. I ahve a "screen
: > section" to define my screen layout and the screen variables. This is only a
: > TEXT screen -- NOT a GUI.
: > 
: > I am not able to do:
: > 
: > (1) I want all input fields to be underlined. I can make them reverse-video
: > using Adis BUT underlining is easier on the eyes. HOW???
: > 

: When I last attempted this, I too failed.  MicroFocus has the best 
: screen section I have worked with, but I never could get underline 
: support to work.  It's not supported for DOS/WINDOWS that I can see.

: > (2) When I use the TAB or arrow keys (down, up, left and right), the cursor
: > moves to the next or previous screen input fields. I would like to make it
: > so that when I press the down arrow key, the cursor jumps to the input field
: > DIRECTLY or IN-DIRECTLY below the current input field. I am able to achieve
: > this ONLY if the input field is DIRECTLY below the current one. HOW????

: Redefine the down arrow to be a TAB key with an ADIS call. It is one 
: of the X"AF" calls. MAKE SURE to re-map the key upon exit.
```

##### ↳ ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DE5EFF.91F6074A@mfltd.co.uk>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au> <Jl0PnHJ5PvPd-pn2-U1dfTfkBJWgX@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Wed, 3 Mar 1999 09:37:31, "Hugh Tran" <hugh_tran@hotmail.com>
…[16 more quoted lines elided]…
> support to work.  It's not supported for DOS/WINDOWS that I can see.

Various people have pointed out that a Windows console will not support
underline. However, if you run your Micro Focus application as a
graphical app, the text console is emulated by the COBOL Runtime System.

Within this emulation, it *is* possible to have underline support in
addition to the regular VGA set of attributes.
A caveat of this functionality is that you must be careful when using
the CBL_ calls to read/write the screen attributes, as they have a
one-byte-attribute interface which defaults to the VGA attribute byte
and thus do not have underline support. There are CBL_ calls which
will set up custom attributes in the palette if you wish to read/write
them with the CBL_ one-byte-attribute interfaces.

As an example, try running the following program first using
"run prog.int" (Windows console), then "runw prog.int" (RTS emulation).

procedure division.
  display "Reverse" at 1010 with reverse-video
  display "Underline" at 1110 with underline
  .

Cheers, Kev.
```

#### ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bj3tn$ul6@hyperion.mfltd.co.uk>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au>`

```
Hugh,

1) Unfortunately the console support on Win95/NT does not provide any
support for the underline attribute so there is no way to get it.

2) The functionality of the TAB and arrow keys is configurable using ADISCF.
However, it is not clear what you mean by DIRECTLY and IN-DIRECTLY. It would
appear that the default behaviour for the cursor keys is what you are
requesting. eg if your cursor is on a field at line 1 column 1 and you press
the down arrow, the cursor will move to a field in which column 1 is valid.
If that is several lines down screen it will move to that point. Unless I
have misunderstood your note that is what I took to mean INDIRECTLY,
DIRECTLY being the next line.



Hugh Tran wrote in message <7bj0bi$e19$1@news1.mpx.com.au>...
>Hi there,
>
>I am using Microfocus Netexpress 2.0 on windows 95/NT PCs. I ahve a "screen
>section" to define my screen layout and the screen variables. This is only
a
>TEXT screen -- NOT a GUI.
>
…[7 more quoted lines elided]…
>so that when I press the down arrow key, the cursor jumps to the input
field
>DIRECTLY or IN-DIRECTLY below the current input field. I am able to achieve
>this ONLY if the input field is DIRECTLY below the current one. HOW????
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36dd4b86.187371736@news.enterprise.net>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au>`

```
On Wed, 3 Mar 1999 20:37:31 +1100, "Hugh Tran" <hugh_tran@hotmail.com>
wrote:

>Hi there,
>
…[7 more quoted lines elided]…
>using Adis BUT underlining is easier on the eyes. HOW???

Underline only works on monochrome screens. There isn't an attribute
bit in the standard PC attribute byte for underline. On good old DOS,
you set this up with MODE MONO but I don't know how Netexpress would
do it - I presume it runs in a text window emulation and not a DOS
shell?
```

##### ↳ ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-o0h8rq56sL9e@Dwight_Miller.iix.com>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au> <36dd4b86.187371736@news.enterprise.net>`

```
On Wed, 3 Mar 1999 14:51:15, scm@enterprise.net (Shaun C. Murray) 
wrote:

> Underline only works on monochrome screens. There isn't an attribute
> bit in the standard PC attribute byte for underline. On good old DOS,
> you set this up with MODE MONO but I don't know how Netexpress would
> do it - I presume it runs in a text window emulation and not a DOS
> shell?

Interestingly, the Fujitsu COBOL screen section DOES support 
Underline.  But the cursor control is VERY primative.
```

###### ↳ ↳ ↳ Re: Need URGENT help on Microfocus Netexpress Screen

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bkoan$cfv$1@news.igs.net>`
- **References:** `<7bj0bi$e19$1@news1.mpx.com.au> <36dd4b86.187371736@news.enterprise.net> <Jl0PnHJ5PvPd-pn2-o0h8rq56sL9e@Dwight_Miller.iix.com>`

```
Don't you mean non-existent?

Thane Hubbell wrote in message ...
>On Wed, 3 Mar 1999 14:51:15, scm@enterprise.net (Shaun C. Murray)
>wrote:
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
