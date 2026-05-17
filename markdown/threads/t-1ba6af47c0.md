[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Realia 5.0 and true Win DLL's

_2 messages · 2 participants · 1996-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Realia 5.0 and true Win DLL's

- **From:** "jan paimo" <ua-author-6589465@usenetarchives.gap>
- **Date:** 1996-09-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<322EF311.139D@qinette.se>`

```

Hi

I'm trying to understand how to build true
Windows DLL's with the Realia 5.0 version

I'm not sure how to do, as I feel the
examples provided by CA are not very easy to
understand.

If anyone that has done something in this area and
could share his knowledge with me, I would be most
grateful!

What I would like to get is :

1. a _small_ source code example
2. any specific compile options needed
3. linking directives needed


With thanks in advance


Jan Paimo


Qinette Data AB

E-mail to: pa··.@qin··e.se
```

#### ↳ Re: Realia 5.0 and true Win DLL's

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-09-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ba6af47c0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<322EF311.139D@qinette.se>`
- **References:** `<322EF311.139D@qinette.se>`

```

*In article <322··.@qin··e.se>, pa··.@qin··e.se says...
*>
*>Hi
*>
*>I'm trying to understand how to build true
*>Windows DLL's with the Realia 5.0 version
*>
*>I'm not sure how to do, as I feel the
*>examples provided by CA are not very easy to
*>understand.
*>
*>If anyone that has done something in this area and
*>could share his knowledge with me, I would be most
*>grateful!
*>
*>What I would like to get is :
*>
*>1. a _small_ source code example
*>2. any specific compile options needed
*>3. linking directives needed
*>
*>
*>With thanks in advance
*>
*>
*>Jan Paimo
*>
*>
*>Qinette Data AB
*>
*>E-mail to: pa··.@qin··e.se

Jan -

I'm not sure what your definition is or what you mean by a
"true windows .dll". For the most part, a .dll is an executable
file containing sub-routines or simply another entire program
called from the main program. From a Cobol perspective, a .dll
is another program. It can be referenced by its program name or
an entry point. .DLL's were introduced in CA-Realia version 4.0/4.2
and are identical to those in 5.0. One new feature in 5.0 is that
it allows you to create a stand-alone .dll--that is, one that also
contains the run-time.

Can you provide more specifics about your needs?

mike dodas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
