[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FCOBOL calc in batch vs CICS

_1 message · 1 participant · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### RE: FCOBOL calc in batch vs CICS

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90491CB93918D21189BD00805FBE300B01442F54@voyager.okc.disa.mil>`

```
Obscure? How dare you...(grin)...

As I recall, there are no "run-time" modules as such, and those verbs that
used external routines were discuraged from being used under CICS.  

What CICS release?  

Could LE be raising its ugly little head?  

Both compiles could be gened to create assembler procedure lists and
detailed data division maps, that could point to where the diffs are....

<snip>
I pride myself on my knowledge of "obscure" and "obsolete" IBM mainframe
COBOLs - but COBOL-F under VSE is beyond me.  The obvious thing to check out
is that your "steplib" search is finding the same run-time modules - and/or
that your link-edits pointed to the same libraries.
<snip>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
