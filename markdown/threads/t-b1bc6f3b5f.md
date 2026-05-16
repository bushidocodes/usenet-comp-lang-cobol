[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pi

_5 messages · 3 participants · 1999-10_

---

### Re: Pi

- **From:** Randall Bart <Barticus@usa.spam.net>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yi79Nx566DXqYvysC=PIdHH7bj6Q@4ax.com>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be>`

```
The venerable "Geoffrey Ketels" <geoffrey.ketels@zonien.be> bestowed
upon comp.lang.cobol on Mon, 4 Oct 1999 18:44:42 -0700 these words:

>how do I integrate Pi in a cobol program

Pi is a constant, so the integral is zero.

If your compiler has the FUNTION PI, use it.

If your compiler doesn't have FUNCTION PI use

     77  PI  PIC 9V9(14)  VALUE 3.14159265358979.

Do not worry about using PI as a dataname.  It is not a reserved word
in the draft standard, and will be a legal dataname unless you specify
PI in the REPOSITORY paragraph.  If you do that, all you will need to
do is remove this line.

Don't use PI to mean anything other than the constant pi.
```

#### ↳ Re: Pi

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37fd7865.187681281@news2.ibm.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <Yi79Nx566DXqYvysC=PIdHH7bj6Q@4ax.com>`

```
On Thu, 07 Oct 1999 16:59:17 -0700, Randall Bart <Barticus@usa.spam.net> wrote:

>The venerable "Geoffrey Ketels" <geoffrey.ketels@zonien.be> bestowed
>upon comp.lang.cobol on Mon, 4 Oct 1999 18:44:42 -0700 these words:
…[3 more quoted lines elided]…
>Pi is a constant, so the integral is zero.

<nitpick>

???  The integral of a constant is a linear function.  The differential of a constant is
zero.

INT pi dx  =  = pi * x + C

d(pi)
-------    = 0
 dx  

</nitpick>
>
>If your compiler has the FUNTION PI, use it.
…[5 more quoted lines elided]…
>Do not worry about using PI as a dataname.  It is not a reserved word

yet, because what about FUNCTION PI?  Wouldn't that make using a variable name of PI
illegal (cannot test it, my compiler is still asleep <g>)

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Give: help support hepless victims of computer error.
```

##### ↳ ↳ Re: Pi

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tk02s$q0f$1@nntp2.atl.mindspring.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <Yi79Nx566DXqYvysC=PIdHH7bj6Q@4ax.com> <37fd7865.187681281@news2.ibm.net>`

```
Volker Bandke <vbandke@ibm.net> wrote in message
news:37fd7865.187681281@news2.ibm.net...
> On Thu, 07 Oct 1999 16:59:17 -0700, Randall Bart <Barticus@usa.spam.net>
wrote:
  <snip>
> >
> >Do not worry about using PI as a dataname.  It is not a reserved word
>
> yet, because what about FUNCTION PI?  Wouldn't that make using a variable
name of PI
> illegal (cannot test it, my compiler is still asleep <g>)
>

Intrinsic Function names are not now (nor in the next Standard when PI is
included) "reserved words". HOWEVER,  the next Standard will (finally IMHO)
provide a method whereby you can "omit" the reserved word FUNCTION - when it
appears before an intrinsic (or user-defined) function name.  HOWEVER, you
can only do this for those names that are never used as user-defined words
within your program.  THEREFORE, I remain strong in my opinion that using
"PI" as a dataname is only asking for trouble in the future.
```

###### ↳ ↳ ↳ Re: Pi

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38012316.2079830@news2.ibm.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <Yi79Nx566DXqYvysC=PIdHH7bj6Q@4ax.com> <37fd7865.187681281@news2.ibm.net> <7tk02s$q0f$1@nntp2.atl.mindspring.net>`

```
On Fri, 8 Oct 1999 00:31:47 -0500, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Intrinsic Function names are not now (nor in the next Standard when PI is
>included) "reserved words". HOWEVER,  the next Standard will (finally IMHO)
…[4 more quoted lines elided]…
>"PI" as a dataname is only asking for trouble in the future.

Thanks for the clarification

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         I'm not a complete idiot, some parts are missing!
```

##### ↳ ↳ Re: Pi

- **From:** Randall Bart <Barticus@usa.spam.net>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p9b9N2E3xseYGWymh4C9m41VcnOR@4ax.com>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <Yi79Nx566DXqYvysC=PIdHH7bj6Q@4ax.com> <37fd7865.187681281@news2.ibm.net>`

```
The venerable vbandke@ibm.net (Volker Bandke) bestowed upon
comp.lang.cobol on Fri, 08 Oct 1999 04:56:22 GMT these words:

>On Thu, 07 Oct 1999 16:59:17 -0700, Randall Bart <Barticus@usa.spam.net> wrote:
>
…[10 more quoted lines elided]…
>zero.

Correct you are.  I seem to be doing my calculus backwards.

>     With kind Regards            |\      _,,,---,,_
>                            ZZZzz /,`.-'`'    -.  ;-;;,
>     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
>      (BSP GmbH)                '---''(_/--'  `-'\_)

I like your cat.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
