[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL compiler options problem!

_1 message · 1 participant · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: COBOL compiler options problem!

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-18T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<380B1CCE.37395A30@zip.com.au>`
- **References:** `<7ue0oc$o7r$1@nnrp1.deja.com> <7ue73v$1an$1@nntp6.atl.mindspring.net>`

```
Mr Klein,

I don't have access to Listserv:...

> >   Secondly,do subroutine need to be linkedited?

Link them NCAL  (never call) it is a parameter option, you can link
them like this and then link edit your load module into you main
program.  Never call makes them a load module but does not resolve the
calls in the module.  Be careful that you make the subroutine DYNAM as
well or S0C4 there will be.

> > I think main program must be linkedited ,but subroutine need  not be
> > linkedited,because they will not run themselves? Is it right?

The system calls have stubs linked in (they must be linked) and the
runtime resolves most of the calls (not all of them, some are
statically linked).

> > Recently,I have tried to compile subroutine without linkedit,but
> > when I tried to compile & linkedit main program,there is an error,
…[4 more quoted lines elided]…
> >

name(xyz)
name(sub1)
name(sub2)
..... whatever you do now ....

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
