[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wang COBOL on MicroFocus Workbench

_2 messages · 2 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Wang COBOL on MicroFocus Workbench

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31718926819CBDD1.FCDBA4B8B461E7B7.EE6B3D34C42545F8@library-proxy.airnews.net>`
- **References:** `<S17P2.13864$LX.5386629@WReNphoon3> <370F535E.DFC1C4BE@wt.net> <e3aIbeVh#GA.358@nih2naae.prod2.compuserve.com>`

```
Robert M. Pritchett wrote:
> 
> Interesting. Sounds like the Wang Cobol program should be converted to e.g.
…[5 more quoted lines elided]…
> 
There are already a number of translators for Wang COBOL.  We have had
great success with a product called "VUPort" from SanSoft, Inc,
(http://www.sansoft.com) which pre-compiles our Wang syntax for Micro
Focus COBOL, inserting calls to the VUPort runtime.  Virtually ALL the
Wang behaviors, including screen handling, are identical to the VS.  

However, since the original post mentioned the source would be going
back to the VS, this type of port is not for him--VUPort is a tool for
migrating from the VS to another (UNIX) platform.
```

#### ↳ Re: Wang COBOL on MicroFocus Workbench

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990413194121.16588.00000252@ng-fd1.aol.com>`
- **References:** `<31718926819CBDD1.FCDBA4B8B461E7B7.EE6B3D34C42545F8@library-proxy.airnews.net>`

```
Way back in 1988 I wrote a pharmacy system for a local
health department on a VS.  Had drug interaction and
allergy checking, and all the bells and whistles.

Then the county DP department got wind of how successful
the project was and wanted a piece of the action.  They 
decided that the entire health department would move to
AS 400's.  The AS 400 geeks rolled in and said "Hey,
we have a nifty utility that will convert the Wang source code
to 400 Cobol."  

Nice work if you can get it, sez I.

Well, the got the source code, and ran it through their
nifty little utility, and after six months of gnashing their
teeth and renting their cloth the pharmacy system was
still up and running happily along on the VS.

Like David said, there's enough unique (and highly
desireable) about the Wang VS to make it somewhat
less than fun to even try to pre-compile with another
system.  Been there, done that with a zenix system
being moved to Micro Focus.  LOTS of code
modification, despite the substantial efforts of the good
folks at MF.

Nuf' said.

James Jones.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
