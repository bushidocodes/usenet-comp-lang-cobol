[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# .exe with RM/COBOL-85?

_4 messages · 4 participants · 2000-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### .exe with RM/COBOL-85?

- **From:** "Ijverige?" <extralarge@freegates.be>
- **Date:** 2000-12-16T21:27:32+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<87R_5.114955$lR2.3528760@afrodite.telenet-ops.be>`

```
I have the following compilers:

1) RM/COBOL-85 Compiler - Version 5.30.00 (dos)    (cbl -> cob)
This one runs great, but you still need the interpreter (runcobol) to run
the application.

2) CA-Realia Classroom COBOL Version 4.200 (dos)
Same code I used with the compiler above needs changes! :(
It produces a working .exe , but does not give me the great running
experience like above.

3) CA Realia II (windows)
Same as (2) and some bad experiences everytime while compiling & linking!
Some of the code that compiled perfectly with (2) now gives *major* errors.
+ Still needs .dll's for the "standalone" exe ...


Cause of the disadvantages of <realia> we use now the RM/COBOL-85 compiler
(1). Is it possible with some kind of tool to compile the .cob files to
.obj's.
Then link them to an executable? Or another way ?
```

#### ↳ Re: .exe with RM/COBOL-85?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-16T16:10:27-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<91gp45$3r6$1@slb6.atl.mindspring.net>`
- **References:** `<87R_5.114955$lR2.3528760@afrodite.telenet-ops.be>`

```
I will leave others to reply to the question of creating .exe's with RM, but
I did want to "suggest" one thing for your consideration.

Have you tried developing under RM using their "ANSI flagging" facility? My
guess is that if you coded according to the ANSI Standard (not using any
extensions), that you would find it easy (or at least easier) to "port" your
source code to other compilers.

If you have tried this already and it doesn't help, can you give us some
examples of code that compiles and runs correctly under RM but *not* under
CA-Realia?  Also, I would like to mention that CA-Realia doesn't document
(as far as I know) "RM-compatibility".  On the other hand, MERANT (Micro
Focus) *does* provide some RM-emulation/compatibility facilities - and it
MOST certainly provides .exe support (but does include some run-time
charges - depending on how you plan to use them).
```

#### ↳ Re: .exe with RM/COBOL-85?

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2000-12-18T11:05:13-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aur%5.22$cg7.243@client>`
- **References:** `<87R_5.114955$lR2.3528760@afrodite.telenet-ops.be>`

```
Ijverige? <extralarge@freegates.be> wrote in message
news:87R_5.114955$lR2.3528760@afrodite.telenet-ops.be...
> I have the following compilers:
>
> 1) RM/COBOL-85 Compiler - Version 5.30.00 (dos)    (cbl -> cob)
> This one runs great, but you still need the interpreter (runcobol) to run
> the application.
[snip]
> Cause of the disadvantages of <realia> we use now the RM/COBOL-85 compiler
> (1). Is it possible with some kind of tool to compile the .cob files to
> .obj's.
> Then link them to an executable? Or another way ?

Thanks for making the right choice!  :-)

There is no tool to translate .cob to .obj.  There is a Windows runcobol
available, as well as several tools to bring your applications to a 'native
Windows' look-and-feel.  Is that what you wish to accomplish?

Tom Morrison
Liant Software Corporation
```

#### ↳ Re: .exe with RM/COBOL-85?

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-12-18T20:32:19+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-9lUngoXb4Plq@tcpserver>`
- **References:** `<87R_5.114955$lR2.3528760@afrodite.telenet-ops.be>`

```
On Sat, 16 Dec 2000 21:27:32, "Ijverige?" <extralarge@freegates.be> 
wrote:

> I have the following compilers:
> 
…[21 more quoted lines elided]…
> 

Use another COBOL compiler that generates .obj files and
link them to form EXE or DLL files.

This may require some serious "porting" effort if you used
a lot of compiler specific features in the code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
