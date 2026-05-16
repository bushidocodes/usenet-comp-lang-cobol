[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL Mixed Addressing Modes and Dynamic Calls

_2 messages · 2 participants · 2004-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL Mixed Addressing Modes and Dynamic Calls

- **From:** tdriscoll@amre.com (Tom Driscoll)
- **Date:** 2004-09-24T10:20:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86d6a01a.0409240920.1519bd61@posting.google.com>`

```
I'm a newbie to Microfocus COBOL, so bear with me if my terminology is
not quite correct.
We have MF Server Express running in 64 bit mode, on HP-UX v11.1 also
running in 64 bit mode. Because of some application dependencies,
COBOL PGMA has to run in 32 bit mode. It needs to make a dynamic call
to PGMB which must run in 64 bit mode. Can this be done ?
```

#### ↳ Re: MF COBOL Mixed Addressing Modes and Dynamic Calls

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-24T19:42:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slr8l0takbj530uf8vj8lieq2jp7r1s7gq@4ax.com>`
- **References:** `<86d6a01a.0409240920.1519bd61@posting.google.com>`

```
On 24 Sep 2004 10:20:50 -0700, tdriscoll@amre.com (Tom Driscoll)
wrote:

>I'm a newbie to Microfocus COBOL, so bear with me if my terminology is
>not quite correct.
…[3 more quoted lines elided]…
>to PGMB which must run in 64 bit mode. Can this be done ?

The answer is yes, but there can be problems if shared memory or
memory-mapped files are involved. You must either link PGMA with +s or
specify LD_LIBRARY_PATH in the link: -Wl,+b$(whatever)/lib32 

One of the rules is that all memory-mapped files within a process must
be the same 32/64 mode. If PGMA creates one as 32-bit, then PGMB tries
to create one as 64-bit, the second mget() will fail. There is an
option to fix this, but you can't change code inside the Cobol
runtime.

If a structure passed between the two contains pointers, obviously the
size will be wrong. You'd have to define it as a 32-bit integer in
PGMB and monkey around with REDEFINES to convert it to a pointer.

You can read all about it here:
http://devresource.hp.com/drc/STK/docs/refs/3264interop.jsp#transdataux

I wrestled with a similar problem -- a 64-bit database calling a
32-bit external procedure. After a few days, I gave up and compiled
the procedure as 64-bit.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
