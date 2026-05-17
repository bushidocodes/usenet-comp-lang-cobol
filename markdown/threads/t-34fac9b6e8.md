[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 65

_2 messages · 2 participants · 1996-09_

---

### COBOL 65

- **From:** "information technology" <ua-author-14529001@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32378E49.1819@talmtl.ccmail.compuserve.com>`

```

(n.b.: previous version of this message mistakenly sent from wrong e-mail i.d. - sorry! -pjd)

I've downloaded (from a number of sites) COBOL 6.5, the one written by someone who does not sign himself,
only says he is (was?...) dying of AIDS.

Aside from what appears to be a pretty good tutorial on COBOL, there is precious little documentation on
the actual operation of the compiler, and a reference to a linker which is not included . When I try to
run either the compiler (COBOL.EXE) or what appears to be the runtime (RUN650.EXE) on my Pentium, I get
mixed results, ranging from 0-byte files to complete computer lockups.

Can anyone provide me with, or refer me to, some additional information on this?

Or, could someone refer me to a good DOS-based compiler & linker, compatible with COBOL 74/85?

Thank you!

Paul Desormeaux
McGill University
e-mail
pde··.@tal··e.com
```

#### ↳ Re: COBOL 65

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1996-09-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-34fac9b6e8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32378E49.1819@talmtl.ccmail.compuserve.com>`
- **References:** `<32378E49.1819@talmtl.ccmail.compuserve.com>`

```

Information Technology (pde··.@tal··e.com) wrote:

(snip)

: I've downloaded (from a number of sites) COBOL 6.5, the one written by someone who does not sign himself,
: only says he is (was?...) dying of AIDS.

: Can anyone provide me with, or refer me to, some additional information on this?
(snip)


Below is the way I use the package.

1. Although I normally keep the source files separate, I combine all
files together in one subdirectory while using the compiler.
2. I do not use the DPATH.COM file (no instructions for it).
3. To prevent the compiler from looking at the A: drive, I use the
DOS command subst a: g:\xx (g:\xx is where all the files are).
4. To compile, enter: cobol (the screen displays are faster if you
use a .BAT file containing just: cobol)
When you see the message: Licenced to Public Domain, press ESC
When you see the message: Enter the file to compile, enter the
program name.
When you see the message: Send your 25.00 donation, press ESC
5. To link the program, use the following command:
link progname,,,cobol650,, (change "progname" to the same
name as in 4, above).
If you don't have a LINK program with your DOS, other compilers
(such as MASM) have one or you can get a substitute from various
FTP locations.
You must have the files that have names starting with RUN, or
the compiler will not generate an .OBJ or .LST file.

I hope that helps somewhat.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
