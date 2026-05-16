[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Little-Endian and Big-Endian?

_5 messages · 5 participants · 1999-11_

---

### Little-Endian and Big-Endian?

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E47B36D9946CD311995000A0C9EA3E925F5FD1@voyager.okc.disa.mil>`

```
I think I understand what in general it refers to, but not specifically.
Can somebody explain where this term came from and what its roots are?

Thanks....



 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: Little-Endian and Big-Endian?

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vn9j1$rim$1@aklobs.kc.net.nz>`
- **References:** `<E47B36D9946CD311995000A0C9EA3E925F5FD1@voyager.okc.disa.mil>`

```
Thompson, William <wthompson@okc.disa.mil> wrote:
: I think I understand what in general it refers to, but not specifically.
: Can somebody explain where this term came from and what its roots are?


Gulliver's Travels.
Eggs.
```

##### ↳ ↳ Re: Little-Endian and Big-Endian?

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381f9ad4_1@news3.prserv.net>`
- **References:** `<E47B36D9946CD311995000A0C9EA3E925F5FD1@voyager.okc.disa.mil> <7vn9j1$rim$1@aklobs.kc.net.nz>`

```

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7vn9j1$rim$1@aklobs.kc.net.nz...
>
> Gulliver's Travels.
> Eggs.


To elaborate: There were these two kinds of people: the big-endians who
maintained that the proper way to eat an egg would be first to seat it
firmly
on its blunt end, and the little-endians who maintained that the proper way
to seat it was on its pointed end.
```

###### ↳ ↳ ↳ Re: Little-Endian and Big-Endian?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iaXT3.164$sa5.4162@dfiatx1-snr1.gtei.net>`
- **References:** `<E47B36D9946CD311995000A0C9EA3E925F5FD1@voyager.okc.disa.mil> <7vn9j1$rim$1@aklobs.kc.net.nz> <381f9ad4_1@news3.prserv.net>`

```
Leif Svalgaard wrote in message <381f9ad4_1@news3.prserv.net>...
>
>Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
…[11 more quoted lines elided]…
>


And to think I heroically resisted..

"One little, two little, three little-endians,
Four little, five little...."


MCM
```

#### ↳ Re: Little-Endian and Big-Endian?

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381F1959.4989@NOSPAMguysoftware.com>`
- **References:** `<E47B36D9946CD311995000A0C9EA3E925F5FD1@voyager.okc.disa.mil>`

```
Thompson, William wrote:
> 
> I think I understand what in general it refers to, but not specifically.
> Can somebody explain where this term came from and what its roots are?

Binary numbers may be stored with the first byte being the highest value byte, or with 
the first byte being the lowest value byte:

The default shown is known as "Little Endian", a  computer architecture in which, within 
a given 16- or 32-bit word, bytes at lower addresses have lower significance (the word 
is stored "little-end-first"). The PDP-11 and VAX families of computers and Intel 
microprocessors and a lot of communications and networking hardware are little-endian. 

Big Endian is a computer architecture in which, within a given multi-byte numeric 
representation, the most significant byte has the lowest address (the word is stored 
"big-end-first"). Most processors, including the IBM 370 family, the PDP-10, the 
Motorola microprocessor families, and most of the various RISC designs, are big-endian. 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
