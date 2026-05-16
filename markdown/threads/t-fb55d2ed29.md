[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Merant (Microfocus), Unix, "Scan Directory" (x"91")

_4 messages · 3 participants · 2000-12 → 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Merant (Microfocus), Unix, "Scan Directory" (x"91")

- **From:** karthur@primal.com
- **Date:** 2000-12-23T04:05:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9218a8$e42$1@nnrp1.deja.com>`

```
Hi...

Microfocus cobol compilers used to provide an x"91" call that would
return directory information back to the calling program.  It was
subfunction 69 of the x"91" call-by-number routine.  Returns what
a "dir" command does, i.e. program names, types, sizes, date/time, etc.

On current unix versions of Merant cobol products, they no longer
support most x"91" functions.  That's okay.  They offer call-by-name
routines that return the "current" directory, and whether or not a file
EXISTS, but there doesn't seem to be an equivalent to the above.

Any suggestions?  Some call-by-name routine I'm missing?  Some easy
interface to the unix shell (ls command)?

What I'm trying to do is port a program to unix that does the
equivalent of a DOS "dir" command with wildcards, (e.g. "dir RU*.*").
Some equivalent "ls" functionality is fine.  Program needs to look for
a varying number of files with a particular prefix.

Thanks for your help!

Kevin Arthur


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Merant (Microfocus), Unix, "Scan Directory" (x"91")

- **From:** "William Wood" <beavis27@earthlink.net>
- **Date:** 2000-12-23T20:48:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c816.10958$G4.448115@newsread2.prod.itd.earthlink.net>`
- **References:** `<9218a8$e42$1@nnrp1.deja.com>`

```
We have some code that does this and it does use the 'ls' command to do it.
We format what we are looking for in a WS variable and do a system call
sending the results of the list to a file that we can then read.  For
example:

01  WS-UNIX-CMD.
    05  FILLER                    PIC XXX VALUE "ls".
    05  WS-LS-ARGS        PIC X(20).
    05  FILLER                    PIC X(28) VALUE z" > /tmp/lsfile 2>
/dev/null".

You move your list arguments into WS-LS-ARGS and make a system call

CALL "SYSTEM" USING WS-UNIX-CMD.

Then open the /tmp/lsfile file and read in the results of the list.  It's
ugly but it works.
```

##### ↳ ↳ Re: Merant (Microfocus), Unix, "Scan Directory" (x"91")

- **From:** karthur@primal.com
- **Date:** 2000-12-29T00:18:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92gl7j$7u2$1@nnrp1.deja.com>`
- **References:** `<9218a8$e42$1@nnrp1.deja.com> <7c816.10958$G4.448115@newsread2.prod.itd.earthlink.net>`

```
In article <7c816.10958$G4.448115@newsread2.prod.itd.earthlink.net>,
"William Wood" <beavis27@earthlink.net> wrote:

> We have some code that does this and it does use the 'ls' command to
do it.
> We format what we are looking for in a WS variable and do a system
call
> sending the results of the list to a file that we can then read.  For
> example:
... .... .....

Thank you!  As you might imagine, I was hoping for a more elegant
solution, but hey, like you said - it gets the job done!

Also very much appreciate the example code.

Thanks again!

- K.A.


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Merant (Microfocus), Unix, "Scan Directory" (x"91")

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-03T14:08:02
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92vfqm$qeh$1@hyperion.mfltd.co.uk>`
- **References:** `<9218a8$e42$1@nnrp1.deja.com>`

```
Kevin,

I the X"91" function 69 still exists and still can be used as per older
products. Looks like it was one they did not convert to a call by name (why
I don't know).

Regards,
Steve.

karthur@primal.com wrote in message <9218a8$e42$1@nnrp1.deja.com>...
>Hi...
>
…[4 more quoted lines elided]…
>
...
>Thanks for your help!
>
…[4 more quoted lines elided]…
>http://www.deja.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
