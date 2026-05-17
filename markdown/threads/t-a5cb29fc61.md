[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF - .DLL vs .INT on WinNT

_1 message · 1 participant · 1995-10_

---

### MF - .DLL vs .INT on WinNT

- **From:** "han..." <ua-author-17087711@usenetarchives.gap>
- **Date:** 1995-10-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46rro0$33r@nsmmfs07.cscoe.ac.com>`

```
I have a couple of questions for anyone running MF COBOL on Windows NT.

We have an application that is compiling COBOL code into DLLs using
the commands: cobol, cblnames, then link32. This process creates
a .dll, .int, .idy. Because of the size and complexity of the project
it is hard to answer these questions by trial and error. Therefore,
I'm looking for someone who has already went through this...

When I run my application, which file am I actually loading (the .dll or
.int). What is the execution search order? Does it search COBPATH,
then PATH?

When I run in animator, which file am I loading? Am I actually animating
the .int or .dll?

For the fastest execution, which file should I be loading? What compile
options (for both cobol and link32) should I use to get the fastest
executable?

If I don't specify a /debug: option on the link32, by default do I get
a symbol table or is the symbol table striped off?

Any help or comments would be greatly appreciated!!!

Thanks,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
