[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comparing Modula2 and Cobol

_2 messages · 2 participants · 1994-12_

---

### Comparing Modula2 and Cobol

- **From:** Bruce.Feist@f615.n109.z1.fidonet.org (Bruce Feist)
- **Date:** 1994-12-01T07:43:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a90_9412020139@blkcat.fidonet.org>`

```
ip-lanca@ladle.csm.uwe.ac.uk wrote in a message to All:

icuau> I have an assignment to do on Cobol, what
icuau> sort of  differences there are between it and other
icuau> languages, i.e. the main features of the language. I know
icuau> Modula2 reasonbly well, but don't know Cobol very well at
icuau> all. Could someone give me some references, ideas on the
icuau> main points /advantages of Cobol.

The two languages are both fairly traditional procedural languages; despite
what anyone else may tell you, the similarities are far greater than the
differences.  Both languages have a complement of structured programming
constructs; both have subroutines, local and global variables, modularity,
and so on.  That understood, let's go on to the differences.

Philosophically, the languages are different.  Modula-2 is a rather
minimalist language; COBOL is large.  Modula is terse, with a clean
structure; COBOL is verbose with a fair amount of syntactic and structural
clutter (which makes the language look more English-like, and encourages
people to program when they would perhaps be better off in another field,
such as forestry).

COBOL's strengths are its extensive built-in data types and operations, and
its attractive and readable way of defining data structures (alias records,
alias group fields).  Its disadvantages include lack of user-defined data
types, lack of type checking in subroutine calls, method of parameter passing
(by reference or by value) being specified in the wrong place (at the call
rather than at the procedure definition), poor string handling facilities
(many COBOL programmers don't believe this), and a tradition of writing
non-modular, non-structured code (this used to be necessary, but modern COBOL
fixes this.  Now, if only the mainstream programmers would catch on...).

Bruce
---------
Fidonet:  Bruce Feist 1:109/615
Internet: Bruce.Feist@f615.n109.z1.fidonet.org
```

#### ↳ Re: Comparing Modula2 and Cobol

- **From:** Martyn Woerner <mw@mfltd.co.uk>
- **Date:** 1994-12-02T09:14:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bmoi9$7md@icebox.mfltd.co.uk>`
- **References:** `<a90_9412020139@blkcat.fidonet.org>`

```
> Its disadvantages include lack of user-defined data
> types, lack of type checking in subroutine calls, method of parameter passing
…[4 more quoted lines elided]…
> fixes this.  Now, if only the mainstream programmers would catch on...).

But many of these disadvantages are being addressed both within the standards
bodies and released products.  For example, Micro Focus COBOL V3.2 includes
support for type definitions and call prototypes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
