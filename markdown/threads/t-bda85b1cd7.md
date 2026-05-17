[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus and Win 3.11 Problem

_2 messages · 2 participants · 1996-02 → 1996-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus and Win 3.11 Problem

- **From:** "ga..." <ua-author-8766037@usenetarchives.gap>
- **Date:** 1996-02-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4gj3uv$t09@cletus.bright.net>`

```
I have MF Cobol installed on a Pentium 100 with 16M memory. Whenever I
try to compile with windows running, the compiler cancels. If I shut down
windows, it compiles fine. Anyone know what the problem is?

Thanks Gary.
```

#### ↳ Re: Micro Focus and Win 3.11 Problem

- **From:** "ferr..." <ua-author-17086290@usenetarchives.gap>
- **Date:** 1996-03-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bda85b1cd7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4gj3uv$t09@cletus.bright.net>`
- **References:** `<4gj3uv$t09@cletus.bright.net>`

```
In article <4gj3uv$t.··.@cle··t.net>, ga··.@bri··t.net says...
›
› I have MF Cobol installed on a Pentium 100 with 16M memory. Whenever I
› try to compile with windows running, the compiler cancels. If I shut down
› windows, it compiles fine. Anyone know what the problem is?
›


Problem is that you Windows hasn't allocated enough memory
in the DOS window you are using.

Using the 'pif editor', create a new windows DOS application.
I called mine "DOS 640k".

The program name is "command.com".

The important thing is that you must select 640k as the
MINIMUM memory required.

Otherwise, its just like setting up any other DOS application
under windows. This way, when you run the DOS window, you will
have 640k available for the MF compiler. This may also be required
to run your MF application, depending on how large the compiled
program is.

don
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
