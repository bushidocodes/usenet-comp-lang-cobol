[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Freeware cobol650 help

_2 messages · 2 participants · 1997-03_

---

### Freeware cobol650 help

- **From:** "veg..." <ua-author-17072360@usenetarchives.gap>
- **Date:** 1997-03-07T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3320f5ca.4297551@news.ilos.net>`

```

Has anyone gotten the freeware compiler cobol650 to work. I can get it
to compile .obj code, but not link. Any help would be appreciated.
Thanks,

Chris Ward
veg··.@il··s.net
```

#### ↳ Re: Freeware cobol650 help

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-03-07T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abfafe6520-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3320f5ca.4297551@news.ilos.net>`
- **References:** `<3320f5ca.4297551@news.ilos.net>`

```

Chris Ward (veg··.@il··s.net) wrote:
: Has anyone gotten the freeware compiler cobol650 to work. I can get it
: to compile .obj code, but not link. Any help would be appreciated.
: Thanks,
: Chris Ward
: veg··.@il··s.net
-----------------------------------

Following are the various .ZIP files that have been available:

COB650.ZIP Has asm source, object, cobol source.
COBOL650.ZIP Has old DPATH.COM
COBOL6-1.ZIP Appears obsolete
COBOL6-2.ZIP Appears obsolete

Below is a working setup of the package:

1. Although I you normally keep the source files separate, you should
combine all of the files together in one subdirectory during compiling
(to prevent problems with searching cross-directory).

2. To prevent the compiler from looking at the A: drive, I use the
DOS command:
subst a: g:¥xx (g:¥xx is where all the files are).
You don't need this if you have a diskette in A:

3. To compile, enter: cobol (the screen displays are faster if you
use a .BAT file containing just: cobol)
When you see the message: Licenced to Public Domain, press ESC
When you see the message: Enter the file to compile, enter the
program name.
When you see the message: Send your 25.00 donation, press ESC

4. To link the program, use the following command:
link progname,,,cobol650,, (change "progname" to the same
name as in 4, above).
If you don't have a LINK program with your DOS, other compilers
(such as MASM) have one or you can get a substitute from various
FTP locations. If all else fails, buy an old DOS for a dollarand
use the link program from it.

5. Do not use the DPATH.COM file (no instructions for it) unless
you can figure it out.

This is a list of compiler oddities

1. Usage is COMP does not work. The compiler accepts the statement
but generates Usage is DISPLAY instead (use COMP-0, instead).

2. Display of comp-0 data directly does not work. If you move
it first to a DISPLAY numeric field, it does work, as long as
the maximum value is not exceeded.

3. A string of text must be all capitals to test alphabetic.

4. Call statement: USING pointers are only 2 bytes (not 4).

5. Call statement passing a COMP-0 item. The item is stored
as hhll instead of the normal llhh (h=high, l=low).

6. BEEP and BELL do not work.

7. When opening a file for EXTEND, if the file is not found, the
compiler goes bananas.
--------------------------

Miscellaneous maximum sizes:

Element of group 1000 bytes
Comp-0 picture 5 digits (two bytes), maximum value 32767.
Comp-3 picture 12 digits.

Warning: Exceeding these maximum sizes does not necessarily
generate a warning. Instead garbage may be produced.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
