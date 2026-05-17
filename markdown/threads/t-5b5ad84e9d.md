[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# From DOS to UNIX(AIX)

_3 messages · 3 participants · 1997-12_

---

### From DOS to UNIX(AIX)

- **From:** "super-user" <ua-author-463904@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<349689C9.AD516312@titasz.hu>`

```

Hi,

We written a program in DOS and now we want to take to UNIX.
Any functions does not working (i.e. CBL_READ_KBD_CHAR ). The
documentation does not
informing , that is not working on UNIX. Have you got any idea why, or
how can i change it?

Dont displaying any colors. I use ansi terminal.

If you have other tipps to change, please help.

Peter
```

#### ↳ Re: From DOS to UNIX(AIX)

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5b5ad84e9d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<349689C9.AD516312@titasz.hu>`
- **References:** `<349689C9.AD516312@titasz.hu>`

```

Super-User,
You've left out quite a few details. Which brand of Cobol are you
using? Have the objects been re-linked in Aix? Are you using a runtime
system? Have you contacted the manufacturer of the product? They are
usually the best source of information. Aix is a very distant cousin of
Unix. So don't expect Unix programs to run in Aix. Don't even expect Aix
programs to run in Aix. What I mean by that is there have been a number of
different versions of Aix released. This affects executables with kernel
calls and the file system. So make sure your program is ported to the
correct Aix version(ie. Aix 3.1.5 executables may not run on Aix 4.02 etc).
I only mention this because I ran into the problem a couple of weeks ago
with a customer in Georgia. They upgraded their Aix and didn't inform us
and the runtime blew a fuse, so we had to upgrade them to the correct
runtime port.

Happy Holidays
Dan Maltes
Applied Systems

Super-User wrote in message <349··.@tit··z.hu>...
› Hi,
› 
…[11 more quoted lines elided]…
›
```

##### ↳ ↳ Re: From DOS to UNIX(AIX)

- **From:** "steve" <ua-author-10786@usenetarchives.gap>
- **Date:** 1997-12-14T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5b5ad84e9d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5b5ad84e9d-p2@usenetarchives.gap>`
- **References:** `<349689C9.AD516312@titasz.hu> <gap-5b5ad84e9d-p2@usenetarchives.gap>`

```


Daniel Maltes wrote:

› Super-User,
›     You've left out quite a few details.  Which brand of Cobol are you
…[4 more quoted lines elided]…
› programs to run in Aix.

GEE, it looks like UNIX, is called a UNIX dirivative, and every unix command
*I* have used has worked! I even compiled two UNIX programs on IT(JED and
KERMIT). BOTH work fine! What is really different? The PID has been
increased(that was the ONLY problem I had)(M/F COBOL originally assumed the
normal 16 bit number)!

› What I mean by that is there have been a number of
› different versions of Aix released. This affects executables with kernel
…[6 more quoted lines elided]…
› 

That happens with nearly EVERY operating system! POSIX is now very limiting,
and IBM OBVIOUSLY decided to change SOME things! Others will have to change
EVERYWHERE! Even LINUX finds it too limiting, so they may soon change it as
well, already they are pulling some tricks. Who would have thought that 4GB or
even 2GB would be a SEVERE limitation so soon?

BTW, it ALSO has happened a lot with DOS, and with WINDOWS, and VMS!

BTW, the original problem PROBABLY has to do with raw and cooked input! MOST
operating systems have key interupts done on single key input. In UNIX(AND
AIX), the default mode is COOKED! That means that all input is SAVED until you
hit an active key such as C/R, and it THEN behaves as it should have up to that
C/R(except editing chars such as delete modify what was typed in, rather than
being sent).

Check to see if the COBOL has a method to switch to RAW input!

› Happy Holidays
› Dan Maltes
…[16 more quoted lines elided]…
››
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
