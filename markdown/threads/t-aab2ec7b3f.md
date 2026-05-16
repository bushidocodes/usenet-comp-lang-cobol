[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interfacing with C

_3 messages · 3 participants · 2006-10_

---

### Interfacing with C

- **From:** "guigouz" <guigouz@gmail.com>
- **Date:** 2006-10-18T13:42:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161204157.593125.278120@m7g2000cwm.googlegroups.com>`

```
Hello
   When a Cobol program CALLs another program, what is passed to the
new program, and how it is passed ?
   I'm asking it because I want to create a C program that receives
some information from cobol. Is it possible ?

   Just a side note, we use novell 3.12 and the cobol compiler from
that era.

Thanks in advance for any information

Guilherme Barile
```

#### ↳ Re: Interfacing with C

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-18T15:26:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161210389.845691.8720@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1161204157.593125.278120@m7g2000cwm.googlegroups.com>`
- **References:** `<1161204157.593125.278120@m7g2000cwm.googlegroups.com>`

```

guigouz wrote:

>    When a Cobol program CALLs another program, what is passed to the
> new program, and how it is passed ?

That depends on what is specified in the source, the compiler and
options given to the compiler.

In the simplest case the USING paramers are passed as addresses of the
data areas (ie thiese may be pointers).

>    I'm asking it because I want to create a C program that receives
> some information from cobol. Is it possible ?

Whether it is possible depends on whether the Cobol compiler generates
code that is compatible with the code that the C compiler generates.

>    Just a side note, we use novell 3.12 and the cobol compiler from
> that era.

'That era' may be the 80s.  Is the compiler running on the Novell
machine or is the Novell just a red herring because it is just a file
server ?

What brand and version of Cobol and of C are you using and what OS will
they target.  Where will the executable run ?

There are thousands of combinations that would never work, there may be
a few that do.
```

#### ↳ Re: Interfacing with C

- **From:** "Vivian" <vsaegesser@infogix.com>
- **Date:** 2006-10-24T11:00:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161712827.717987.266220@f16g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1161204157.593125.278120@m7g2000cwm.googlegroups.com>`
- **References:** `<1161204157.593125.278120@m7g2000cwm.googlegroups.com>`

```
We call C, C++, assembler, and even Java from within our Cobol
programs.  We use an old compiler too, but for MVS, so can't help you
with Novell.  But, the concept is definitely doable.


guigouz wrote:
> Hello
>    When a Cobol program CALLs another program, what is passed to the
…[9 more quoted lines elided]…
> Guilherme Barile
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
