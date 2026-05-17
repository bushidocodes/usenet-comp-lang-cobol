[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Signal, trap, possibly

_1 message · 1 participant · 1998-02_

---

### Signal, trap, possibly

- **From:** "udc" <ua-author-16279686@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34D65153.E882D778@udc.co.nz>`

```

setup:
microfocus cobol running under hp-ux without the aid of a GUI

problem:
How, at user request (via a keystroke e.g P) can I get
(interactive) program B to interrupt (interactive) program A when
program A has no knowledge of program B what so ever.
[Program A may be any program in the shop. Program B provides access via
a pop-up type menu to a range of useful info. On exit program A
resumes.]
My first thought was to generate a signal and execute program B via
'trap'.
Two problems arise:
how to generate say SIGUSR1 with say P ... stty? - no joy so far
how to make trap effective a child process - is it possible?

please note:
this problem arises out of a conversion, it was achievable under Primos.

Thanks in advance.

Regards,

JimG

mailto:ji··.@act··n.nz
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
