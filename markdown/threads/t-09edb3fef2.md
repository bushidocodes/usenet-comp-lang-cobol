[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro-Focus Cobol and AIX

_1 message · 1 participant · 1997-07_

---

### Micro-Focus Cobol and AIX

- **From:** "jean-francois leblond" <ua-author-14650233@usenetarchives.gap>
- **Date:** 1997-07-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33D4D6D6.641A@compuserve.com>`

```

We're using Micro-Focus Cobol 3.2 with IBM AIX for a while now.
We just upgraded AIX from 4.1.4 to 4.1.5. We're experiencing a delay
problem with the escape key in our programs. When we press the ESC key
we have a 15 seconds delay before it get processed. But when we send
another ESC before the end of the delay, it pushes the first ESC to be
processed as well as the second one. There's an environment variable
called COBKEYTIMEOUT which enable COBOL to distinguish between an ESC
alone and a function key. We're using both in our programs.

I'm looking for a solution within Micro-Focus.

IBM is currently looking for one in AIX.

Anyone have any clue ?

J-F Leblond
Uni-Select
jfl··.@com··e.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
