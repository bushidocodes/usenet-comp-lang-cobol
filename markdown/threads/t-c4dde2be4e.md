[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling a script from MF Conol

_5 messages · 3 participants · 1999-03 → 1999-04_

---

### Calling a script from MF Conol

- **From:** tony@hibou.demon.co.uk (Tony Geraghty)
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<922660391snz@hibou.demon.co.uk>`

```

Does anyone know if it is possible to call a script from MF Cobol on 
a Unix box, and have the script run asynchronously (sp?) ?

For reasons best known to himself, one of my colleagues wants to do 
this. He's working his way through the manuals, but hasn't come up 
with any way to do this yet.

The compiler is version 4, and the box is using Unixware version 2.1
```

#### ↳ Re: Calling a script from MF Conol

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27zL2.9316$PY.99358@news.rdc1.on.wave.home.com>`
- **References:** `<922660391snz@hibou.demon.co.uk>`

```
Check out the fork() and execvp() system functions. I think Merant may
have a white paper on this, with some sample code at their web site.

Tony Geraghty <tony@hibou.demon.co.uk> wrote in message
news:922660391snz@hibou.demon.co.uk...
>
> Does anyone know if it is possible to call a script from MF Cobol on
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Calling a script from MF Conol

- **From:** tony@hibou.demon.co.uk (Tony Geraghty)
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<922915161snz@hibou.demon.co.uk>`
- **References:** `<922660391snz@hibou.demon.co.uk> <27zL2.9316$PY.99358@news.rdc1.on.wave.home.com>`

```
In article <27zL2.9316$PY.99358@news.rdc1.on.wave.home.com>
           kewagner@home.com "Karl Wagner" writes:

> Check out the fork() and execvp() system functions. I think Merant may
> have a white paper on this, with some sample code at their web site.
…[5 more quoted lines elided]…
> > a Unix box, and have the script run asynchronously (sp?) ?

Many thanks for the suggestions, I've passed them on and my colleague 
is looking into them.
```

###### ↳ ↳ ↳ Re: Calling a script from MF Conol

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37035DB0.D50C670@mfltd.co.uk>`
- **References:** `<922660391snz@hibou.demon.co.uk> <27zL2.9316$PY.99358@news.rdc1.on.wave.home.com> <922915161snz@hibou.demon.co.uk>`

```
Tony Geraghty wrote:
> 
> In article <27zL2.9316$PY.99358@news.rdc1.on.wave.home.com>
…[12 more quoted lines elided]…
> is looking into them.

Tony,

The simplest way is to execute the script using the SYSTEM call. As the
SYSTEM call will use your $SHELL to execute whatever command is given
to it, you can just use whatever shell notation applies. ie:

CALL "SYSTEM" USING "./my_script &" & x"00"
Shell notation ------------------^
(SYSTEM requires a nul-terminated string )

Note that the COBOL screen handler may get confused if the script you
are running asynchronously writes to the terminal - this is not the
case if the SYSTEM call was synchronous (although obviously, it can't
read what was written to the screen by the shell script).

Cheers, Kev.
```

###### ↳ ↳ ↳ Re: Calling a script from MF Conol

_(reply depth: 4)_

- **From:** tony@hibou.demon.co.uk (Tony Geraghty)
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<923127882snz@hibou.demon.co.uk>`
- **References:** `<922660391snz@hibou.demon.co.uk> <27zL2.9316$PY.99358@news.rdc1.on.wave.home.com> <922915161snz@hibou.demon.co.uk> <37035DB0.D50C670@mfltd.co.uk>`

```
In article <37035DB0.D50C670@mfltd.co.uk> ked@mfltd.co.uk "Kevin Digweed" writes:

> Tony Geraghty wrote:
> > 
…[10 more quoted lines elided]…
> 

Kev,

Thank you.  It seems that the idea is to kick off a print program 
which will not need to commumicate with the calling program.

The program is part of a rewrite/Y2K conversion of an existing 
client/server system; the current system runs a print program as an 
asynchronous process via a call to Tuxedo which allowed the users to 
contimue woriking while the proprt was printed. In the rewrite this 
was replaced by a subprogram call, with the obvious results.
 
I've suggested that he should have a look at the communications 
manual but he doesn't know if the rewrite is also a C/S system and 
seems reluctant to call the people who did the conversion work.

tony
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
