[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL "windowing" preprocessor

_4 messages · 3 participants · 1995-05 → 1995-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL "windowing" preprocessor

- **From:** "simon chapman" <ua-author-5633351@usenetarchives.gap>
- **Date:** 1995-05-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<801401101snz@colsys.demon.co.uk>`

```
We are trying to use some of the "windowing support" features available under
MF COBOL 3.0 for UNIX. Basically a preprocessor (window1) allows you to say
things like DISPLAY WINDOW..., DISPLAY BOX..., CLOSE WINDOW...etc.

The example programs all compile OK, but as soon as we compile a program with
a COPY in it, the preprocessor terminates with the message "READ ERROR:" and
the name of the source file. We are using plain COPY with no REPLACING or
other fancy stuff.

The COBCPY environment variable is used to locate copy files, and this
works fine _until_ we introduce the window1 preprocessor.

Thanks for reading this, any ideas will be _most_ gratefully received!

- Simon
```

#### ↳ Re: MF COBOL "windowing" preprocessor

- **From:** "pet..." <ua-author-582426@usenetarchives.gap>
- **Date:** 1995-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b05bdcc042-p2@usenetarchives.gap>`
- **In-Reply-To:** `<801401101snz@colsys.demon.co.uk>`
- **References:** `<801401101snz@colsys.demon.co.uk>`

```
Simon Chapman wrote:

› We are trying to use some of the "windowing support" features available under
› MF COBOL 3.0 for UNIX. Basically a preprocessor (window1) allows you to say
› things like DISPLAY WINDOW..., DISPLAY BOX..., CLOSE WINDOW...etc.

Check that you have a $SET line in the source, the COBDIR synonym is
OK and the compile directives you are using. I thought MF were going
to drop the "window1" syntax.

Rgds
Petras
```

##### ↳ ↳ Re: MF COBOL "windowing" preprocessor

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1995-06-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b05bdcc042-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b05bdcc042-p2@usenetarchives.gap>`
- **References:** `<801401101snz@colsys.demon.co.uk> <gap-b05bdcc042-p2@usenetarchives.gap>`

```
› pet··.@jol··m.au (Petras Virzintas) wrote:
› 
› Check that you have a $SET line in the source, the COBDIR synonym is
› OK and the compile directives you are using. I thought MF were going
› to drop the "window1" syntax.

there are no plans to drop the syntax. infact, the v3.2 release of the
compiler now supports color for the "window1" syntax.

Crookie
g.··.@mfl··o.uk
```

##### ↳ ↳ Re: MF COBOL "windowing" preprocessor

- **From:** "simon chapman" <ua-author-5633351@usenetarchives.gap>
- **Date:** 1995-06-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b05bdcc042-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b05bdcc042-p2@usenetarchives.gap>`
- **References:** `<801401101snz@colsys.demon.co.uk> <gap-b05bdcc042-p2@usenetarchives.gap>`

```
In article <3qoo3j$g.··.@inf··m.au>
pet··.@jol··m.au "Petras Virzintas" writes:

› Simon Chapman  wrote:
› 
…[7 more quoted lines elided]…
› 

Thanks for that. Everything checks out OK in all of our sources and environment
variables. After some considerable experimentation, we have managed to solve
our problem by writing a sub-program which does all of the windowing we need.
This means that we only need to compile one program that uses the window1
preprocessor. It's a bit of a compromise, but it works.

I hope MF are not going to drop the window1 preprocessor, but if they do we
will have to rewrite our sub-program to use PANELS instead. In fact, that was
another reason why we wanted to isolate all the non-standard COBOL within
separate sub-programs. It makes migration to another compiler/platform a little
less fraught.

- Simon
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
