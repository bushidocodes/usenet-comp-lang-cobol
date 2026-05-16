[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to specify a port address in MF COBOL under DOS on PC?

_5 messages · 4 participants · 2002-09 → 2002-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### How to specify a port address in MF COBOL under DOS on PC?

- **From:** "Bob Henderson" <ntfobk@NOSPAMknowt.com>
- **Date:** 2002-09-29T14:26:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ytl9.1074$Os6.178052@news.xtra.co.nz>`

```
The sub-programs with MF Cobol include routines, (CALL X"87" and CALL
X"96"), to enter a hardware port and return a one or two byte value where
"port" is defined as a PIC 9(4) COMP-X field.

I want to access the parallel port. The address of this port is 0378 in hex.

What value do I put into the comp-x field?

Thanks in advance for your replies.
```

#### ↳ Re: How to specify a port address in MF COBOL under DOS on PC?

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-09-29T02:51:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-pbd5MMloxdBq@h24-82-204-17.wp.shawcable.net>`
- **References:** `<7ytl9.1074$Os6.178052@news.xtra.co.nz>`

```
On Sun, 29 Sep 2002 03:26:11 UTC, "Bob Henderson" 
<ntfobk@NOSPAMknowt.com> wrote:

> The sub-programs with MF Cobol include routines, (CALL X"87" and CALL
> X"96"), to enter a hardware port and return a one or two byte value where
…[8 more quoted lines elided]…
> 

try

move x"0378" to comp-x-field

that is a WAG, by the way
```

#### ↳ Re: How to specify a port address in MF COBOL under DOS on PC?

- **From:** Lybush <lklafter@tampabay.rr.com>
- **Date:** 2002-10-04T18:52:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oorpusgpvm73fudf3qoh9rfk5gj7pbgeu@4ax.com>`
- **References:** `<7ytl9.1074$Os6.178052@news.xtra.co.nz>`

```
I think I once used PIC 9(5) value 957   and it worked ok.; I think it
might also have been HEX 3BE

Hope this helps!

On Sun, 29 Sep 2002 14:26:11 +1200, "Bob Henderson"
<ntfobk@NOSPAMknowt.com> wrote:

>The sub-programs with MF Cobol include routines, (CALL X"87" and CALL
>X"96"), to enter a hardware port and return a one or two byte value where
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How to specify a port address in MF COBOL under DOS on PC?

- **From:** "Bob Henderson" <ntfobk@NOSPAMknowt.com>
- **Date:** 2002-10-06T12:32:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IEKn9.3828$Os6.534607@news.xtra.co.nz>`
- **References:** `<7ytl9.1074$Os6.178052@news.xtra.co.nz> <3oorpusgpvm73fudf3qoh9rfk5gj7pbgeu@4ax.com>`

```
"Lybush" wrote:
> "Bob Henderson" wrote:
> >The sub-programs with MF Cobol include routines, (CALL X"87" and CALL
> >X"96"), to enter a hardware port and return a one or two byte value where
> >"port" is defined as a PIC 9(4) COMP-X field.
> >I want to access the parallel port. The address of this port is 0378 in
hex.
> >What value do I put into the comp-x field?
> >Thanks in advance for your replies.

> I think I once used PIC 9(5) value 957   and it worked ok.; I think it
> might also have been HEX 3BE

This morning I changed the PIC 9(4) COMP-X field to PIC 9(5) and it worked
perfectly on the first compile. (I am moving 888 decimal to the field for
HEX 0378 which is where DOS says the port is.)

Although it now works, I do not understand why I have to use pic 9(5)
instead of the 9(4) COMP-X as documented in the MF Operating Guide.
Any ideas?

> Hope this helps!

I suspect I would NEVER have discovered this from my own efforts so your
hopes are realised and I am now very happy because I have been pottering
about with this for a couple of weeks. Thank you for sharing your knowledge.
```

###### ↳ ↳ ↳ Re: How to specify a port address in MF COBOL under DOS on PC?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-10-06T00:12:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<anogne$a0h$1@slb7.atl.mindspring.net>`
- **References:** `<7ytl9.1074$Os6.178052@news.xtra.co.nz> <3oorpusgpvm73fudf3qoh9rfk5gj7pbgeu@4ax.com> <IEKn9.3828$Os6.534607@news.xtra.co.nz>`

```
There are a VAST number of Micro Focus directives that impact how
binary/comp fields are handled.  MOST of them don't impact COMP-5 fields,
but I would check your directives to see if this explained your original
"problem".  Look for directives like TRUNC, IBM-COMP, COMP-5, etc
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
