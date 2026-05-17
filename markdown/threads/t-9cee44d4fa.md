[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Very slow disk I/O under MS/Windows with MF Cobol

_5 messages · 5 participants · 1995-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Very slow disk I/O under MS/Windows with MF Cobol

- **From:** "el..." <ua-author-17087548@usenetarchives.gap>
- **Date:** 1995-03-08T12:23:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9503081723.AA07204@mpt.com>`

```


I ported some .int files (disk I/O intensive) to windows and when I
run them using "runw" it takes forever to get done (20seconds) compared
to less than one second under windows using the "run" command (Dos mode).
The disk seems to go through some major thrashing with the runw. How can one
fix this serious fault ?

Regards, Elie.
```

#### ↳ Re: Very slow disk I/O under MS/Windows with MF Cobol

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-03-09T22:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cee44d4fa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<9503081723.AA07204@mpt.com>`
- **References:** `<9503081723.AA07204@mpt.com>`

```
Elie I. Mourad (el··.@m··.com) wrote:


: I ported some .int files (disk I/O intensive) to windows and when I
: run them using "runw" it takes forever to get done (20seconds) compared
: to less than one second under windows using the "run" command (Dos mode).
: The disk seems to go through some major thrashing with the runw. How can one
: fix this serious fault ?

: Regards, Elie.

This is more a characteristic of Windows than of COBOL. Generally, the
equivalent program in DOS will always run 5 - 20 times faster than the Windows
version. This is due to the high Windows overhead. This is true regardless
of the language used to develop the program.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

##### ↳ ↳ Re: Very slow disk I/O under MS/Windows with MF Cobol

- **From:** "ch..." <ua-author-1720442@usenetarchives.gap>
- **Date:** 1995-03-10T16:13:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cee44d4fa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9cee44d4fa-p2@usenetarchives.gap>`
- **References:** `<9503081723.AA07204@mpt.com> <gap-9cee44d4fa-p2@usenetarchives.gap>`

```
In <3joh5u$k.··.@Mar··s.com>, fr··.@M··.COM (Lawrence Free/ A.F. Software Services) writes:
› Elie I. Mourad (el··.@m··.com) wrote:
› 
…[13 more quoted lines elided]…
› 

Ever heard the term "Windows SUX"?? The only words left out are "speed and
resources" ;) -=>SORRY, *couldn't* resist<=-

Chad
```

##### ↳ ↳ Re: Very slow disk I/O under MS/Windows with MF Cobol

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-11T07:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cee44d4fa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9cee44d4fa-p2@usenetarchives.gap>`
- **References:** `<9503081723.AA07204@mpt.com> <gap-9cee44d4fa-p2@usenetarchives.gap>`

```
"This is more a characteristic of Windows than of COBOL. Generally, the
equivalent program in DOS will always run 5 - 20 times faster than the Windows
version. This is due to the high Windows overhead. This is true regardless
of the language used to develop the program."

THis is just wrong, the claim of a factor of 5-20 is not sustainable at all.
Disk I/O if anything will run faster under windows than on DOS if you are
using the 32-bit file extensions in Windows. If you see anything like a
factor of 5-20, this cannot be blamed on Windows overhead, it is something
else. I am no great fan of Windows (in fact I think it is junk), but this
kind of extreme claim is not reasonable!
```

#### ↳ Re: Very slow disk I/O under MS/Windows with MF Cobol

- **From:** "ets..." <ua-author-17072749@usenetarchives.gap>
- **Date:** 1995-03-11T11:24:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cee44d4fa-p5@usenetarchives.gap>`
- **In-Reply-To:** `<9503081723.AA07204@mpt.com>`
- **References:** `<9503081723.AA07204@mpt.com>`

```
Elie,

Don't use RUNW ! RUNW should really only be used if you're programming
GUI (ie, PANELSV2) code. I assume since you say the normal RUN command does
work, that you're NOT writing this type of code.

One thing, though, that I've noticed writing PANELSV2 code under PM and
WINDOWS, is that the FIRST time I load a program it does take a while (not
20 seconds, though) but the second, third, etc, time it seems to come up faster.

A last thought, is your machine fast enough to really support RUNW ?
Remember, it does take quite a bit for PANELSV2 to do it's thing...


Hope it helps...


Ethan H. Schultz
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
