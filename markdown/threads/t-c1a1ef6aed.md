[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus/Windows NT

_1 message · 1 participant · 1995-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus/Windows NT

- **From:** "sbpa..." <ua-author-17087481@usenetarchives.gap>
- **Date:** 1995-09-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43v771$f5n@hobbes.cc.uga.edu>`

```
Is anyone out there using MicroFocus' compiler under Windows NT on an
Alpha processor?

I have a collection of programs that work fine under OS/2 and have
brought them over to Windows NT. The problem is that a couple of the
programs will only run under the Animator -- and it's sort of touchy
there. If I am patient, I can *always* get the program to run, eventually,
so I feel certain that it is not a program bug (besides the fact that they
run under OS/2). They very rarely die in the same place twice so I think
that it is a memory management problem -- a MicroFocus representative has
since told me that there have been some problems in that area.

The way I can *always* get it to run is by hesitating some between stepping
through each instruction. That tells me it is a synchronization problem.

If I run the .EXE, it *always* fails. If I animate and the program dies,
it kills the animator too. It *usually* fails on a file OPEN, although I have
had one die on an ADD statement (not overflow, it was ADD 1 to [item = zero]).

I have spoken to Microsoft about the meaning of the error code that I get
[128] and they say it means that a synchronization object has been abandoned.
BTW, 128 is not listed among MicroFocus' error codes so I feel somewhat
comfortable in my assumption that it is an OS error code.

All of this jibes with a trace of the assembler code via WinDebug wherein
the program usually dies somewhere close to a critical section and/or
around a memory allocation routine. A couple of times I got the following
display on the console immediately after the program ditched: "No room for
message" or something to that effect.

I am stumped. I get nothing from MicroFocus because they say either that
it isn't their job because this is an SDK from Digital Equipment Corporation
or that I have to reproduce the problem. What reproduce the problem? I can
reproduce it whenever you like - I just run the program again. You tell
*me* what's different between the code in an .INT and the code in an .EXE.
Shouldn't be any, huh? If I could do that I'd know what it is and fix it
myself. Maybe I ought to ask them for a few trade secrets, eh?

We've been going around about this for 2 months (Me, Digital, and MicroFocus)
so I'm pretty much at the end of my rope. Couldn't tell that from the tone
of this post could you?

Thanks in advance for any insight or assistance,
Douglas Parker
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
