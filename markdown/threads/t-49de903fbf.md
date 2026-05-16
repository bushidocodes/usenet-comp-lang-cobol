[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ASP -> VB -> Cobol architecture

_1 message · 1 participant · 2002-06_

---

### ASP -> VB -> Cobol architecture

- **From:** "Mike Vendel" <mike_vendel@premierintl.com>
- **Date:** 2002-06-26T18:35:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uhkjv7iear2ea9@corp.supernews.com>`

```
Hi!

 Just curious if anyone has ever implemented a project using ASP, VB, and
Cobol dlls.
 We have such a project and are getting some perplexing results.

 A short summary which I can expound upon for the interested listener. VB
COM objects house our new bizness logic. Cobol dlls house our legacy bizness
logic. ASP provides the web presentation.
We have a weird occurrence wherein the VB COM objects that call cobol dlls
must be run as a COM+ application when called from ASP, otherwise cobol
bombs.
 The cobol dlls do share information that is loaded into memory but this
shouldn't really be an issue for the regular COM objects. The dlls should be
loaded into the COM objects process space.
 A vb executable test project works fine. But the only way this architecture
will work with ASP is if the VB objects are housed in COM+.

 Any ideas or arcane references to some documentation that would help me
understand where the cobol dlls are getting loaded when dealing with VB and
ASP?

 Thanks,
 Mike
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
