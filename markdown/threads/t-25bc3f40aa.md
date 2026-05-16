[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Environment variables

_6 messages · 6 participants · 1998-09_

---

### Environment variables

- **From:** "CFC" <michael_kelleher@countrywide.com>
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde8d9$8f2425a0$62973586@mis8mk>`

```
I am working on a HP-UX 10.2 system with Micro Focus Cobol V3.2.
What I am trying to do is reset an environment variable within a cobol
program, for use later in another cobol program in my job-stream.
I have tried using "DISPLAY <varname> UPON ENVIRONMENT-VALUE"
                          "DISPLAY <setting> UPON ENVIRONMENT-NAME"
and it does not change the environment variable.

Does anyone know of another method to do this.
```

#### ↳ Re: Environment variables

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1998-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uldl5$8av$1@news.megsinet.net>`
- **References:** `<01bde8d9$8f2425a0$62973586@mis8mk>`

```
I don't have my manual handy, but I think MF-COBOL has functions that can be
CALLed to do what you want.

- Darius Cooper

CFC wrote in message <01bde8d9$8f2425a0$62973586@mis8mk>...
>I am working on a HP-UX 10.2 system with Micro Focus Cobol V3.2.
>What I am trying to do is reset an environment variable within a cobol
…[5 more quoted lines elided]…
>Does anyone know of another method to do this.
```

##### ↳ ↳ Re: Environment variables

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F008CJ.Eo0.0.bloor@torfree.net>`
- **References:** `<01bde8d9$8f2425a0$62973586@mis8mk> <6uldl5$8av$1@news.megsinet.net>`

```
Darius Cooper (Darius_cooper@Bigfoot.com) wrote:
: I don't have my manual handy, but I think MF-COBOL has functions that can be
: CALLed to do what you want.

: CFC wrote in message <01bde8d9$8f2425a0$62973586@mis8mk>...
: >What I am trying to do is reset an environment variable within a cobol
: >program, for use later in another cobol program in my job-stream.

Are you sure that you remain in the same environment after changing the 
variable? If, for instance, you are in Windows, each window inherits the 
environment variables from the operating system, but doesn't modify the 
original. If the next program in your stream is clonning a new 
environment... that will be your problem.
```

##### ↳ ↳ Re: Environment variables

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6un9cd$pha$2@news00.btx.dtag.de>`
- **References:** `<01bde8d9$8f2425a0$62973586@mis8mk> <6uldl5$8av$1@news.megsinet.net>`

```
Darius Cooper schrieb:

> I don't have my manual handy, but I think MF-COBOL has functions that
> can be
…[13 more quoted lines elided]…
> >Does anyone know of another method to do this.

   You can't change the environment-variable, becaouse every task
start's
with a copy of the environment-variables. You have to backtrace the
call-structure in memory to
find out the root-environment (..not very easy in DOS/WIN..) and then
you may
change the value (depending on size etc.)

No programm directly support these way, so you have to write your own
assembler-routine
to change the value permanently.

AS
```

###### ↳ ↳ ↳ Re: Environment variables

- **From:** Haluk Okur <spbis@sbs.de>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360FBCD9.2E97@sbs.de>`
- **References:** `<01bde8d9$8f2425a0$62973586@mis8mk> <6uldl5$8av$1@news.megsinet.net> <6un9cd$pha$2@news00.btx.dtag.de>`

```
Andreas Strzoda wrote:
> 
>    You can't change the environment-variable, becaouse every task
> start's
> with a copy of the environment-variables.
....
> AS


My Unix-days are long gone but I seem to remember the "export"
statement which passed the new value of an environment variable
to the parent shell. Can't this can be done from within COBOL
also?
```

###### ↳ ↳ ↳ Re: Environment variables

_(reply depth: 4)_

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360F954D.19E521C0@mfltd.co.uk>`
- **References:** `<01bde8d9$8f2425a0$62973586@mis8mk> <6uldl5$8av$1@news.megsinet.net> <6un9cd$pha$2@news00.btx.dtag.de> <360FBCD9.2E97@sbs.de>`

```
Haluk Okur wrote:
> 
> Andreas Strzoda wrote:
…[10 more quoted lines elided]…
> also?

No. You're thinking of Bourne shell (and it's derivatives) which use
the same syntax for working with local variables and "environment"
variables (ie, X=1; print $X). "export" simply tags a variable name
as "external" (inherited by sub-processes) rather than local to the
shell.

Obviously, this doesn't apply to COBOL programs, whose local variables
are in the data division and are different beasts altogether from
environment variables, so the equivalent of "export" is implied.

Back to the original post - it states that the DISPLAY syntax is used
to modify the environment variable, but the order it gives is
DISPLAY ... UPON ENVIRONMENT-VALUE, DISPLAY ... UPON ENVIRONMENT-NAME.
This is the wrong order - you must set the NAME before you set (or
read) the VALUE.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
