[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

_5 messages · 3 participants · 2001-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

- **From:** "Dave" <saltaire@ix.netcom.com>
- **Date:** 2001-02-17T21:14:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96ne9h$dla$1@slb2.atl.mindspring.net>`

```
I'm using Fujitsu's free V3 COBOL, and am still trying to compile my COBOL
program.
I was using the Microfocus compiler, ran it through FJ's converter, removed
all the MF compiler directives, fixed all the problems still existing which
the compiler pointed out, and it still won't compile successfully. I'm using
their "Programming Staff" tool, and executing "WINCOB(Compile)" - the only
compiler shown on the menu.

After the compiler thinks for about 8 seconds, it gives me the message:
"F:\...\PCOBOL32\F3BH440.DLL is not found. RC=1157".
The "F..." is the correct path to the compiler and is in the active PATH per
MS/DOS. There are no other messages.

There is no such module anywhere. I can find references in code to "440",
but no references to "F3BH440" or return code "1157" in the manuals or
anywhere else.

Since this free version is supposedly not supported by Fujitsu
(understandably), does anyone have any clues as to what I'm doing wrong? The
program is "plain vanilla" as far as I'm concerned, is less than 6,000 lines
long, uses no features announced in the last 10 or 15 years (except for
STRING which is fairly old, I think).

Any help would be appreciated.

Dave Morton
```

#### ↳ Re: Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

- **From:** "Russell Styles" <RWSTYLES01@CS.COM>
- **Date:** 2001-02-18T02:46:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96nuou$3cl$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<96ne9h$dla$1@slb2.atl.mindspring.net>`

```
    First - have you tried a "Hello world" program? Ie,
no working storage, linkage, file section, minimal procedure
division.


"Dave" <saltaire@ix.netcom.com> wrote in message
news:96ne9h$dla$1@slb2.atl.mindspring.net...
> I'm using Fujitsu's free V3 COBOL, and am still trying to
compile my COBOL
> program.
> I was using the Microfocus compiler, ran it through FJ's
converter, removed
> all the MF compiler directives, fixed all the problems still
existing which
> the compiler pointed out, and it still won't compile
successfully. I'm using
> their "Programming Staff" tool, and executing
"WINCOB(Compile)" - the only
> compiler shown on the menu.
>
> After the compiler thinks for about 8 seconds, it gives me the
message:
> "F:\...\PCOBOL32\F3BH440.DLL is not found. RC=1157".
> The "F..." is the correct path to the compiler and is in the
active PATH per
> MS/DOS. There are no other messages.
>
> There is no such module anywhere. I can find references in code
to "440",
> but no references to "F3BH440" or return code "1157" in the
manuals or
> anywhere else.
>
> Since this free version is supposedly not supported by Fujitsu
> (understandably), does anyone have any clues as to what I'm
doing wrong? The
> program is "plain vanilla" as far as I'm concerned, is less
than 6,000 lines
> long, uses no features announced in the last 10 or 15 years
(except for
> STRING which is fairly old, I think).
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

- **From:** "Dave" <saltaire@ix.netcom.com>
- **Date:** 2001-02-18T17:00:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96pjon$d1a$1@slb4.atl.mindspring.net>`
- **References:** `<96ne9h$dla$1@slb2.atl.mindspring.net> <96nuou$3cl$1@sshuraab-i-1.production.compuserve.com>`

```
I've tried compiling their "COB1.COB" program from the examples.
It's 8 lines, and compiles fine....


"Russell Styles" <RWSTYLES01@CS.COM> wrote in message
news:96nuou$3cl$1@sshuraab-i-1.production.compuserve.com...
>     First - have you tried a "Hello world" program? Ie,
> no working storage, linkage, file section, minimal procedure
…[48 more quoted lines elided]…
>
```

#### ↳ Re: Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-18T14:33:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j3Rj6.2454$6N6.261660@newsread2.prod.itd.earthlink.net>`
- **References:** `<96ne9h$dla$1@slb2.atl.mindspring.net>`

```

"Dave" <saltaire@ix.netcom.com
>
> After the compiler thinks for about 8 seconds, it gives me the
message:
> "F:\...\PCOBOL32\F3BH440.DLL is not found. RC=1157".
> The "F..." is the correct path to the compiler and is in the active
PATH per
> MS/DOS. There are no other messages.

Well, can YOU find F3BH440.DLL? I found mine in the folder with the
other Guijitsu stuff. Looking at it with a hex editor, the only thing
of interest was the literal string 'COBOL COPYRIGHT FUJITSU LIMITED
1994' which occurred an unbelievable 98 times.
```

##### ↳ ↳ Re: Fujitsu COBOL Compile Problem: F3BH440.DLL (not PATH)

- **From:** "Dave" <saltaire@ix.netcom.com>
- **Date:** 2001-02-18T16:54:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96pjci$16e$1@slb1.atl.mindspring.net>`
- **References:** `<96ne9h$dla$1@slb2.atl.mindspring.net> <j3Rj6.2454$6N6.261660@newsread2.prod.itd.earthlink.net>`

```

"Jerry P" <jerryp@bisusa.com> wrote in message
news:j3Rj6.2454$6N6.261660@newsread2.prod.itd.earthlink.net...
>
> "Dave" <saltaire@ix.netcom.com
…[12 more quoted lines elided]…
>

I couldn't find it... Maybe it's hiding behind all those COPYRIGHT
statements... <grin>
I sure found plenty of those....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
