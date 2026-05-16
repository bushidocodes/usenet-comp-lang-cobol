[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help - Micro Focus - start another task in Unix

_2 messages · 2 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help - Micro Focus - start another task in Unix

- **From:** "Niels Chr. Madsen" <ncm@memobase.dk>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C28063.3B57F2E6@memobase.dk>`

```
Hi;

I'm porting our system from OS/2 to SUN Solaris.

In our system, we sometimes starts another task, in OS/2 we are using
the X'91' - 35 function "X"91" function 35 - Execute a Program" - but
this is  only for OS/2, DOS and Windows.

How to do this in UNIX

/Niels Chr. Madsen
```

#### ↳ Re: Help - Micro Focus - start another task in Unix

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C2960C.5B1AEF18@mfltd.co.uk>`
- **References:** `<37C28063.3B57F2E6@memobase.dk>`

```


"Niels Chr. Madsen" wrote:
> 
> Hi;
…[7 more quoted lines elided]…
> How to do this in UNIX

Hi. The easiest way to do this is:

CALL "SYSTEM" using "unix-command-line" & x"00"

(ie, pass a nul-terminated string BY REFERENCE).

There are other ways (such as opening a pipe to another process
using file handling syntax, or the CBL_EXEC_RUN_UNIT call on Server
Express) but use of them would depend on your requirements. Calling
'SYSTEM' (use the upper-case version, as this ensures the screeen
handling subsystem doesn't get confused if your subprocess happens to
write to the terminal) is the easiest way.

Cheers, 
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
