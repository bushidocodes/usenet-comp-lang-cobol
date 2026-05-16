[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Command-Line arguemnts for MFcobol 4.1 for Solaris

_2 messages · 2 participants · 1998-11_

---

### Command-Line arguemnts for MFcobol 4.1 for Solaris

- **From:** ggarrett@unconfigured.xvnews.domain (Garry Garrett)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71t5l2$9u4@omantsrv14.csgsystems.com>`

```
Hi!  I'm a Systems Administrator for a Solaris (2.5.1) machine.
We put MicroFocus Cobol 4.1 on it.  The development box for this
project is an AIX box, also with MicroFocus cobol (I would have
made the developlment box have the same O.S., but I'm sure the
powers that be don't understand that all unix isn't the same...).

I had a cobol class about 10 years ago, and haven't touched it
since (which is why I don't follow this newsgroup, so I'd appreciate
e-mail responses if you could; and I would post my e-mail address
here, but every time I have done that on Usenet I get TONS of spam)
so in your response please assume I have no knowledge of cobol.

Here lies the problem:  My programmers have no problems passing
arguments between programs, but they can't seem to read arguments
off of the command line.  The funny thing is, this works fine on
the AIX version of MFcobol that they have.  I'm thinking that I either
need a patch from Sun or from MicroFocus, otherwise the same exact
source code shouldn't work on AIX either.  My question is, has
anyone else out there seen this behavior, and if so, what did
you do (what patches did you get from whom) to fix it?

We have a service contract with Sun (so I can get patches from them)
and we are working on one from MicroFocus (gawd purchasing can be
slow at times).  I would just wait and call MicroFocus, but the
project is at a halt until we can resolve this.
```

#### ↳ Re: Command-Line arguemnts for MFcobol 4.1 for Solaris

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3642BE8F.7872391@mfltd.co.uk>`
- **References:** `<71t5l2$9u4@omantsrv14.csgsystems.com>`

```
Garry Garrett wrote:
> 
> Hi!  I'm a Systems Administrator for a Solaris (2.5.1) machine.
…[3 more quoted lines elided]…
> powers that be don't understand that all unix isn't the same...).
[snip]
> Here lies the problem:  My programmers have no problems passing
> arguments between programs, but they can't seem to read arguments
> off of the command line.  The funny thing is, this works fine on
> the AIX version of MFcobol that they have.
[snip]

Garry, 
Can you post some example source code which works on AIX but not
Solaris ? The reason I ask is because there are many ways to "read
the command line". Also, the contents of any $COBDIR/cobconfig files
might be useful (there are options to control some of the command-line
behaviour).

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
