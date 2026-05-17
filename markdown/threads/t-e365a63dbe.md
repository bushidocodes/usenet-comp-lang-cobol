[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need HELP with strange DISPLAY problem

_4 messages · 4 participants · 1995-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Need HELP with strange DISPLAY problem

- **From:** "francesco carollo" <ua-author-16120105@usenetarchives.gap>
- **Date:** 1995-04-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`

```
Question: Can the removal of a DISPLAY command affect the run-time
results of a program?

Background: Program A and B are both written in Cobol II and have been
compiled with Release 4 libraries. They run in a MVS environment.
Program A dynamically calls program B and the latter performs all
database I/O in a DB2 Release 3 environment.

Program A uses data passed to it by B to dump the database data in a
formatted report. B contains some DISPLAY commands that will be used
for debugging purposes when it goes to production. It currently has
some temporary DISPLAYs to help debug the program as I was writing it.
These latter DISPLAYs must be removed before implementation. This is
where the problem occurs. If I remove a specific temporary DISPLAY, a
bug appears in the report produced by program A. If the DISPLAY remains,
no problem (unfortunately, delivering the code with the temporary
DISPLAYs is not an option).

The bug I'm referring to is the kind where one page has 65 lines of
data and the following page is only supposed to have 64. Turns out that
the last line from the previous page mysteriously reappears on the
subsequent page. I've considered program logic however everything looks
ok to me. I've always thought that DISPLAY commands were harmless
creatures. Has anybody ever encountered this sort of problem? If so,
how do I get rid of it. Help of any kind would be greatly appreciated.

Thanks
Francesco
bb··.@mus··l.ca


Francesco
bb··.@mus··l.ca
```

#### ↳ Re: Need HELP with strange DISPLAY problem

- **From:** "e..." <ua-author-17073894@usenetarchives.gap>
- **Date:** 1995-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e365a63dbe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`
- **References:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`

```
In article <29A··.@VM1··L.CA>
BBP··.@MUS··L.CA "Francesco Carollo" writes:

› 
› The bug I'm referring to is the kind where one page has 65 lines of
…[6 more quoted lines elided]…
› 

The only possibility I can think of is that the line that contains the
DISPLAY command ends with a period and when removing it, it somehow alters the
scope of an IF (or some other command).

Hope this helps!

Enzo------------------------------------------------------------------
And everything under the sun is in tune
but the sun is eclipsed by the moon.
Siri------------------------------------------------------------------
```

#### ↳ Re: Need HELP with strange DISPLAY problem

- **From:** "morcos" <ua-author-52563034@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e365a63dbe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`
- **References:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`

```
On 29 Apr 1995, Francesco Carollo wrote:

› Question: Can the removal of a DISPLAY command affect the run-time
›           results of a program?
…[23 more quoted lines elided]…
› 
I'm posting from a friend's account because I kepp getting communication
errors from my McGill account. In answer to some peoples comments. I had
already verified that the removal of the DISPLAY would not affect the end
of a paragraph. I even went as far as checking the source for hidden
characters which could adversely affect the run-time results. Everything
keeps checking out fine.

Did I say help? No. I said HELP!!!!!!!

Please post your replies to these groups since t seems I can't answer
from my own account.

Thanks again from your help
Francesco Carollo (bb··j@mus··l.ca) using a friend's account.
```

#### ↳ Re: Need HELP with strange DISPLAY problem

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e365a63dbe-p4@usenetarchives.gap>`
- **In-Reply-To:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`
- **References:** `<29APR95.11504386.0075@VM1.MCGILL.CA>`

```
Just a guess here. DISPLAY output usually goes to the SYSOUT DD
statement which is usually assigned to SYSOUT=*. It sounds as if
you may have the DISPLAY output and the report output going to
the same page (ie the same output file on two DD's). If this is
the case you could be having buffer overlap problems. Be sure
the report and DISPLAY output go to two different files.

A second guess is be sure that you have the called and the
calling programs compiled with the exact same compiler options
with regard to DYNAM RES DATA(31) (or whatever variation you
require). I've had trouble in the past with DISPLAYS in
subroutines not compiled the same as the caller.

Good Luck. Ron.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
