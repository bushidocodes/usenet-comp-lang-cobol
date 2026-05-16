[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to get address of Cobol variable?

_2 messages · 2 participants · 1998-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: How to get address of Cobol variable?

- **From:** "COBOLFrog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<359C80CD.C83B3025@IMN.nl>`
- **References:** `<01bda426$68ac5980$703d868b@nmc-pc> <1998070213375500.JAA18163@ladder01.news.aol.com> <359BACB4.6B6B@bt.com>`

```

Patrick Herring wrote:

> S Comstock wrote:
> ...
…[4 more quoted lines elided]…
> 31-bit addressing,

On IBM mainframes, this bit is not used for *addressing* and as such
normally set to zero although it could be one, because it is ignored by the
hardware address registers. To keep things neat, it als almost always set to
zero.BUT ...
The bit is used for some totally other thing in this IBM blue world. And
most frequently used that way:
When passing a parameter list (CALL ... USING P1, P2 etc) in machine code
there is a register involved that is filled by the caller with the addes of
the list of addresses of the parameters. Say for example that there is a
list of three addresses, that will be 12 bytes long (3 parms X 4 bytes).
These 12 bytes (contiguous) are in storage on some location and THAT address
is put in the parameter-list-address-register (in COBOL usually register 1,
I am told). Now how does at run-time now the called program how many
addresses are in the list, in other words how many parameters are passed?
Simply by the wide-spread convention that all addresses except the last will
have that one bit ZERO. The leftmost bit is thus an end-of-list-flag.
Other compilers, f.e. PL/1, use other addressing schemes, f.e. passing the
address of an parameter-description block in which much more info is present
like number of parameters, type and size of them (especially for arrays and
structures) a.s.o.

> and does the sign in the picture mean Cobol does the
> Right Thing with it?

(This stays typically IBM)In COBOL there is no way to describe a binary
field in base 2. The picture is always base-10. The number of 9's is telling
the maximum decimal value: 10**8-1 in this case. This is stored binary,
because usage is specified as such (COMP). Now the compiler reasons as
follows:
1) I am allowed to allocate either 2, 4 or 8 bytes for binary fields
2) I try the smallest possible which is able to hold the figure 10**8-1 in
binary format.
The result is a 4 bytes field. In that field, you may know (but need not
know) how the info is stored. If you use it to store an address, you
probably do not want to know the internal structure, but knowing that the
SIGN is part of the 32 bits, you specify it, so all buts will be usable.
Most probably the compiler thas not move around with the bits, so the sign
is not really needed. But you never know. This is implementor defined.

If you want to display the address, you can also redefine it as pic x(4) and
use some charToHex function to show it hexadecimally on the screen.

The Frog
```

#### ↳ Re: How to get address of Cobol variable?

- **From:** RandallBart <Barticus@att.spam.net>
- **Date:** 1998-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6njdhv$k6d@bgtnsc01.worldnet.att.net>`
- **References:** `<01bda426$68ac5980$703d868b@nmc-pc> <1998070213375500.JAA18163@ladder01.news.aol.com> <359BACB4.6B6B@bt.com> <359C80CD.C83B3025@IMN.nl>`

```

COBOLFrog (Huib Klink) wrote:
> 
> Patrick Herring wrote:

> > and does the sign in the picture mean Cobol does the
> > Right Thing with it?
…[14 more quoted lines elided]…
> is not really needed. But you never know. This is implementor defined.

Actually, the standard expects the compiler to always keep the value
within the PIC.  If you move an address of X"7FFF0000" to a PIC 9(8)
field, the decimal value 134213632 should be truncated to 34213632
(X"20A0F00").  I understand that there's some compile time kluge to get
around this.  In A Series we have USAGE BINARY EXTENDED (not for
addresses, just to avoid truncation).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
