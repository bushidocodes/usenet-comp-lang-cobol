[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Correction: DEC VAX CoBOL CALL to BAS$EDIT

_1 message · 1 participant · 1996-03_

---

### Correction: DEC VAX CoBOL CALL to BAS$EDIT

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1996-03-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1996Mar21.033154.14903@giant>`

```
Thanks to nog··.@lbe··n.ca (John Nogueira/Information Services) for
discovering that I had the input and the output strings interchanged in the call
to the undocumented BAS$EDIT routine. It should have been:

CALL "BAS$EDIT"
USING BY DESCRIPTOR WS-STRING-OT
BY DESCRIPTOR WS-STRING-IN
BY VALUE WS-BAS$EDIT-COMMAND
GIVING WS-VMS-CONDITION-VALUE.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
