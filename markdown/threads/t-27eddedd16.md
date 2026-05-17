[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with MicroFocus COBOL and C++ integration on UNIX

_6 messages · 5 participants · 1996-10 → 1996-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "ateeque r. haque" <ua-author-17087204@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<327519B8.454F@tasc.com>`

```

Hi,
I am looking for some help please.

I am writing an API in COBOL for a set of class libraries that were
developed in C++.

My goal is to take the object file generated from the cob compiler and
link it with the library using the C++ compiler.

However, the linker complains about the following 3 undefiend symbols:
hashtb
dlopen
dlsym

Any ideas as to what to do? I have already searched all of the
libraries for definitions of these symbols.

Thanks in advance.
ARH
```

#### ↳ Re: Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "soft..." <ua-author-6881452@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27eddedd16-p2@usenetarchives.gap>`
- **In-Reply-To:** `<327519B8.454F@tasc.com>`
- **References:** `<327519B8.454F@tasc.com>`

```

Ateeque R. Haque (arh··.@ta··c.com) wrote:

: My goal is to take the object file generated from the cob compiler and
: link it with the library using the C++ compiler.

Good luck. Mixing COBOL and another procedural language like
C is hard, mixing it with C++ is almost impossible.

: However, the linker complains about the following 3 undefiend symbols:
: hashtb
: dlopen
: dlsym

: Any ideas as to what to do?

Here are some:

1. Are these symbols exported as C or C++ symbols? Name mangling for
data type checking is most likely what's killing you. Dump the symbol
table of the library your C++ compiler created and see what the symbols
look like. If you're trying to link class methods in, just forget
it, it'll probably never work.

2. Does the linker understand the library format of your C++ libraries.
(Or vice versa, I can't really tell from the post which is the library
and which is the main language.) There are big incompatibilities
between different library formats and linkers and stuff. A COBOL
compiler might emit symbols a C++ linker chokes on, or you could be
trying to link a Borland .LIB file with the MicroFocus COBOL Microsoft
linker, or whatever.

3. Are you sure all the libraries are getting linked at all? Turn on
verbosity and stuff. You never know what is really being pulled in
unless you double check.

4. Depending on the environment and type of linking you're
doing, make sure the symbols you want are actually exported
and available. In Win32, for example, all symbols in a DLL need
to be explicitly exported to be seen by COBOL.

5. Make sure everyone is in the same memory model and architecture.
I discovered MicroFocus' OS/2 compiler was a *16-bit* one, and
couldn't link my 32-bit C library in at all.

I can't really tell from the post if you're trying to link a COBOL
routine into a C++ program or vice versa. Whichever, consult your
compilers' manuals on mixed language programming, and if what you want
to do isn't there, then you're probably going into uncharted waters
where no one has ever been.

Scott
```

##### ↳ ↳ Re: Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-10-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27eddedd16-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27eddedd16-p2@usenetarchives.gap>`
- **References:** `<327519B8.454F@tasc.com> <gap-27eddedd16-p2@usenetarchives.gap>`

```

Scott McMahan - Softbase Systems wrote:
› 
› Ateeque R. Haque (arh··.@ta··c.com) wrote:
…[5 more quoted lines elided]…
› C is hard, mixing it with C++ is almost impossible.

Mixing COBOL with C using Micro Focus COBOL on Unix is actually incredibly easy.
CALL "cfunc" .... will get from a COBOL program to a C function, and
cobol_program(); .... will get from a C function to a COBOL program.

Any "difficulty" is in ensuring that the parameter lists are of the correct
type and are passed in the correct fashion - but that's not a problem
restricted to mixed-language.

› : Any ideas as to what to do?
› 
› Here are some:
 
› 2. Does the linker understand the library format of your C++ libraries.
› (Or vice versa, I can't really tell from the post which is the library
…[4 more quoted lines elided]…
› linker, or whatever.

He's on Unix - there will only be one system linker to worry about, and that will
no doubt cope with the two main object formats (COFF and ELF). I think the problem
is more in the way that the "compile/link" front ends ('cob' for COBOL, 'cc' for C
and 'CC' (?) for C++) use the system linker (giving it additional language-specific
libraries, doing extra work such as static object initializer lists, using the
language-specific startup code). Each compiler front end knows what's needed for
*it's* language (the COBOL one also knows about what C requires, to allow COBOL/C
linking) but not for all other lanuages. You have to cajole them to work together.

› 5. Make sure everyone is in the same memory model and architecture.
› I discovered MicroFocus' OS/2 compiler was a *16-bit* one, and
› couldn't link my 32-bit C library in at all.
 
› This is not an issue on Unix.
 
› I can't really tell from the post if you're trying to link a COBOL
› routine into a C++ program or vice versa.

There's no distinction between those two, other than the choice of the "compiler"
that is used (cob, cc etc) to produce the executable. I have a method of allowing
COBOL/C++ linking with Micro Focus COBOL on Unix, which I am currently writing up
(to avoid having to type the same thing in for each individual case). I'll email
it on when it's finished.

› Whichever, consult your
› compilers' manuals on mixed language programming, and if what you want
› to do isn't there, then you're probably going into uncharted waters
› where no one has ever been.

It's not supported explicitly by the COBOL system as yet, but it's fairly easy
(when you know how "cob" works) to work around this problem.

Cheers, Kev.
```

##### ↳ ↳ Re: Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "marilyn e. sander" <ua-author-17086523@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27eddedd16-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27eddedd16-p2@usenetarchives.gap>`
- **References:** `<327519B8.454F@tasc.com> <gap-27eddedd16-p2@usenetarchives.gap>`

```

Scott McMahan - Softbase Systems wrote:
› 
› Ateeque R. Haque (arh··.@ta··c.com) wrote:
…[12 more quoted lines elided]…
› : Any ideas as to what to do?

Sorry I missed your original posting. Regarding these three symbols, I know
what dlopen and dlsym are. They are found in the UNIX System V Release 4
library libdl.so. If you are running on a Unix platform, add -ldl to your
cc or ld command line. I have never heard of hashtb. But if you are using
the cc front end to compile a c++ program, and link it with an already-compiled
cobol program, you need to find out what libraries are part of the COBOL
run-time environment. The fact that dlopen and dlsym are undefined, and that
a hash table is being used, suggests that you are using COBOL's dynamic
call facilities. If you are using a Solaris platform I might be able to help
further, as I know what ccs tools you can use to analyze the cobol object files.

Marilyn Sander

Marilyn E. Sander
msa··.@cyg··s.com
(415)903-1416
```

##### ↳ ↳ Re: Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "sit..." <ua-author-12404967@usenetarchives.gap>
- **Date:** 1996-11-02T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27eddedd16-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27eddedd16-p2@usenetarchives.gap>`
- **References:** `<327519B8.454F@tasc.com> <gap-27eddedd16-p2@usenetarchives.gap>`

```

sof··.@mer··h.com (Scott McMahan - Softbase Systems)
wrote:

› : My goal is to take the object file generated from the cob compiler and
› : link it with the library using the C++ compiler.

MF COBOL generates a ".int" or ".gnt"; these are interpreted by the
RTS (runtime system). It's rarely useful to use the third option -
generating a standalone executable - it's huge!

› Good luck. Mixing COBOL and another procedural language like
› C is hard, mixing it with C++ is almost impossible.

MicroFocus COBOL allows you to "build" a new RTS (run-time system)
from the shipped version by linking in any C functions you care to.
It's been a long time since I did this, but we successfully ported a
whole AS/400 application (about a million LOC!) to MF COBOL and
Oracle. (The C part was the screen handler - since the AS/400 does a
heck of a lot of things in the background, we had to emulate all of
that!) Once you've done that, all the C functions you linked into the
RTS are callable by any COBOL program (whose gnt or int is being)
interpreted by the new RTS.

Look up the manuals for descriptions relating to the "-xe" option of
the "cob" command. If I remember right, that was the switch that
built a new runtime.

Dont know about C++ though...

(Since I missed the original post, I may be way off-base here in my
understanding of what you're looking for :-)

Sitaram.
```

###### ↳ ↳ ↳ Re: Help with MicroFocus COBOL and C++ integration on UNIX

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-27eddedd16-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-27eddedd16-p5@usenetarchives.gap>`
- **References:** `<327519B8.454F@tasc.com> <gap-27eddedd16-p2@usenetarchives.gap> <gap-27eddedd16-p5@usenetarchives.gap>`

```

Sitaram Chamarty wrote:
› 
› sof··.@mer··h.com (Scott McMahan - Softbase Systems)
…[7 more quoted lines elided]…
› generating a standalone executable - it's huge!

Yes, a standalone executable can be big, BUT you need one to run those .int and
.gnt files also ($COBDIR/rts32 is the default one we ship, which "cobrun" will
invoke). In fact, if you are distributing one application, it may be *preferable*
to ship a static linked executable. The reason for this is that $COBDIR/rts32 or
ANY RTS that is created to allow dynamic loading (ie calling .int or .gnt, or
call-by-data-name) will pull in EVERYTHING that you MIGHT need to call (we don't
know until we actually load up that .gnt what you're going to be doing - index
file IO ? screen handling ?). When you statically link, the linker KNOWS just what
you're using and will ONLY link that in. Of course, you then have to add the size
of your COBOL programs into the size of the executable, BUT remember that the code
pages of the executable (and that includes your COBOL) will be shared across
simultaneous executions of that exe file by multiple users. With the dynamic RTS
and .int/.gnt model, each .gnt is loaded seperately by each process requiring it.

Basically, it depends on both your application and the way in which it is used. I
just wanted to say that I don't think static linking should be completely ignored
across the board.
Besides, on SVR4 environments, we support the creation of shared objects, which
gives you the best of both worlds.

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
