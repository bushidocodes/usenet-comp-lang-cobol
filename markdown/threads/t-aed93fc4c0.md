[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Debug tools for programs running under CICS on MVS

_1 message · 1 participant · 1997-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Debug tools for programs running under CICS on MVS

- **From:** "colin gibson" <ua-author-1751878@usenetarchives.gap>
- **Date:** 1997-08-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33F83DB4.46F4@dial.pipex.com>`

```

I'm not sure if this is the right newsgroup to post this to...

We are currently undertaking an investigation to evaluate the effect that
European Monetary Union will have on our mainframe systems. The concern
is that the new monetary values will be 50% higher than the current
sterling figures held. This will potentially cause programs to fail as
intermediate fields overflow etc.

What we are looking for is a tool (or tools) that will be able to catch
these exceptions and report on them without the system (overnight or
batch) coming to a halt (we already have a tool compiled into some of our
COBOL programs called Detector that takes a snapshot of an exception then
allows the program to continue). Ideally, this tool would not require any
recompilation of existing modules.

The language sources we have on the mainframe are a mix of COBOL (on-line
& batch), Adabas Natural (again on-line & batch) & IBM Assembler.

Any pointers to tools or even the best place to ask for information like
this would be appreciated.

Regards

Colin Gibson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
