[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol compiler for linux and SQL

_4 messages · 3 participants · 2001-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Cobol compiler for linux and SQL

- **From:** <tfhkcyt2000@taifuji.com>
- **Date:** 2001-03-25T19:51:34+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99km2d$q8t1@imsp212.netvigator.com>`

```
Hello,

Now we are using Informix IDS 9.21 server
on Suse Linux 7.0, can you suggest us
COBOL products that can compile COBOL
program on Linux, and use Informix IDS 9.21
database directly or using embed SQL?

Thanks for your help.
```

#### ↳ Re: Cobol compiler for linux and SQL

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-03-25T20:31:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lhsbt850s73s27i6ph9nsvp8ihlknltu6@4ax.com>`
- **References:** `<99km2d$q8t1@imsp212.netvigator.com>`

```
ghItlh <tfhkcyt2000@taifuji.com> 

>Hello,
>
…[7 more quoted lines elided]…
>

To do this with tinycobol and Oracle on linux, I wrote my own
preprocessor.

It accepted embedded SQL in a COBOL program and built C programs to
access the data. It changed the COBOL embedded SQL to calls to the C
routines.

The C routines were passed though Pro*C before being compiled up.

Messy but it worked.

Perhaps you could do similar for your Informix database. I think I put
around 100 hours of development time into my preprocessor.
```

##### ↳ ↳ Re: Cobol compiler for linux and SQL

- **From:** aflinsch <avflinsch@att.net>
- **Date:** 2001-03-26T12:53:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABF8235.8EDEA35E@att.net>`
- **References:** `<99km2d$q8t1@imsp212.netvigator.com> <6lhsbt850s73s27i6ph9nsvp8ihlknltu6@4ax.com>`

```
qIroS wrote:
> 
> ghItlh <tfhkcyt2000@taifuji.com>
…[24 more quoted lines elided]…
> around 100 hours of development time into my preprocessor.

Sounds pretty cool, any chance you would be willing to share your
work?
```

###### ↳ ↳ ↳ Re: Cobol compiler for linux and SQL

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-03-27T21:20:02+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8os1ct0o92ji1rljoppbtdue0b16ofsmqk@4ax.com>`
- **References:** `<99km2d$q8t1@imsp212.netvigator.com> <6lhsbt850s73s27i6ph9nsvp8ihlknltu6@4ax.com> <3ABF8235.8EDEA35E@att.net>`

```
ghItlh aflinsch <avflinsch@att.net> 


>Sounds pretty cool, any chance you would be willing to share your
>work?

I could I guess.

The problem is it makes two very big assumptions:

1) It works with the way _I_ write SQL (HV definition assumptions
mostly, such as all HVs belong to a single 01 level HOST-VARIABLES and
all HV's are 02 levels beneath this)

2) It produces C code suitable for running through Oracle Pro*C and
may not work with Ingres/DB2/whatever precompilers for C without
modification.

Some neat things it DOES do is allow you to use (for example)
Packed-Decimal HVs in COBOL and the preprocessor will handle
converting these to and from C to Cobol.

IMO, if you want COBOL and SQL on Linux, CA OpenIngres 2.0 is the only
way to go; It's the only Linux RDBMS that I know of that has a native
COBOL precompiler for embedded SQL.

Cheerie pip.

If people are genuinley interested in seeing the preprocessor, I may
put it on line. If there is sufficient interest.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
