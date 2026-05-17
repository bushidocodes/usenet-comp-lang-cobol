[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL on UNIX: cobputenv question

_2 messages · 2 participants · 1995-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL on UNIX: cobputenv question

- **From:** "george lewycky" <ua-author-12797862@usenetarchives.gap>
- **Date:** 1995-11-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48388f$l76@news.ios.com>`

```
MF COBOL on UNIX: cobputenv question

using the cobputenv in Microfocus COBOL 3.0 on Unix
how do we set an environment variable from a COBOL
program ??

a working example would be really helpful,
the manual has an example for cobgetenv but
nothing for cobputenv.

thanks in advance

George


==================================================
George R Lewycky "I'd rather be on Titan !!"
Windows 95 = Macintosh 1989 with dual air bags

try me: http://soho.ios.com/~lewycky/

lew··.@soh··s.com geo··.@a··.com
==================================================
```

#### ↳ Re: MF COBOL on UNIX: cobputenv question

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-11-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dfe7fa5f0c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<48388f$l76@news.ios.com>`
- **References:** `<48388f$l76@news.ios.com>`

```

In article , Joan Colley writes:
› George Lewycky   wrote:
›› MF COBOL on UNIX: cobputenv question
…[6 more quoted lines elided]…
› which contains a null terminated value of the form "varname=value".
[snip]

Hi. Actually, cobputenv() is only really there for C programs that are to be
linked into a COBOL runtime executable and need to set environment variables
that COBOL is to pick up (either directly or indirectly (eg dd_ filename
mapping variables)). Beware though, as you have to be careful that the memory
whose address you pass is not changed or freed until that variable is
overwritten with a new value (see the putenv() man page). This could happen
"accidentally" in COBOL (eg, call cobputenv() with a string literal then
someone else CANCELs the program containing the literal).

I'd suggest that a better, more correct way of doing this from COBOL is to use
the ACCEPT/DISPLAY FROM/UPON ENVIRONMENT-NAME/ENVIRONMENT-VALUE X/Open syntax,
which is documented in your language reference manual. The COBOL runtime system
handles the allocating/freeing of the environment space for you.

Cheers, Kev.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
