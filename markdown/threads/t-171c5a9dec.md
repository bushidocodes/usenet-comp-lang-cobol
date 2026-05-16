[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Annoying AIX COBOL Compiler....

_3 messages · 2 participants · 2002-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Annoying AIX COBOL Compiler....

- **From:** "Paul Raulerson" <praulerson@NOSPAM-hot.rr.com>
- **Date:** 2002-03-19T02:09:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O5xl8.29511$Dv6.1039534@typhoon.austin.rr.com>`

```
Okay, I'm out of my depth again. Would some of you guys with the wise (if
not older!) heads
give me a hand here?

I just have to call a C function from COBOL, something that should be very
easy. In fact, it is
terrifically easy under Windows or OS/2, or better yet, on the Mainframe or
on an AS/400.
And indeed, it *works* under AIX 5L.  But it gives me the following annoying
error that I cannot
seem to eliminate. (Go figure - it will linkedit the .o file and create an
executable file even with the
rotten error in there...)

I wrote a super simply little COBOL and C program to test this. They are
reproduced below.  Ignore the case in the COBOL program; it is there just
because I typed it in vi instead of a COBOL aware editor... ;)  The function
in the C program is in uppercase because I have been trying different
combinations of PGMNAME(UPPER) and
PGMNAME(MIXED). Mixed *always* seem to come out LONGMIXED, which may be the
problem.
I don't know how to track this down however.


Anyways: Here is the error I get -

# cc -c cgic.c
# cob2 -o cgi cgicob.cbl cgic.o
PP 5765-548 IBM COBOL Set for AIX       1.1   in progress ...
LineID  Message code  Message text
     3  IGYDS1046-E   A user-defined word was used as a program under the
                      "PGMNAME(LONGMIXED)" option.  The name was accepted in
                      its uppercased format.
Messages    Total    Informational    Warning    Error    Severe
Terminating
Printed:       1                                    1
End of compilation 1,  program CGICOB,  highest severity: Error.
Return code 8
# ./cgi
Content-type: text/html

<hr>This from the C program<hr>
<br>C return code is 000000056<br>
<br>From the COBOL program<hr>
#

----
And here are the pesky sample programs. The IBM C Set for AIX compiler
version 5 is installed, and
COBOL Set for AIX version 1.1.

-Paul

C program:

#include <stdio.h>
int CGIC () {
   int rc;

   fprintf (stdout,"Content-type: text/html\n\n");
   fprintf (stdout,"<hr>This from the C program<hr>\n");
   return (56);

   }


COBOL Program:

    CBL PGMNAME(M)
    identification division.
    program-id. cgicob.
    data division.
    working-storage section.
    01 program-name             pic x(8) value 'cgic'.
    01 rc                                PIC s9(9) comp.

    procedure division.
        call 'CGIC' returning rc
          end-call
        display '<br>C return code is ' rc '<br>'
        display '<br>From the COBOL program<hr>'
        goback.
```

#### ↳ Re: Annoying AIX COBOL Compiler....

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-18T20:49:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7690i$64t$1@slb7.atl.mindspring.net>`
- **References:** `<O5xl8.29511$Dv6.1039534@typhoon.austin.rr.com>`

```
Boy is it nice to have an "easy question" - and to understand (an obscure)
compiler message.

Change

 program-id. cgicob.
    to
 program-id. "cgicob".

For documentation on this, see:
  http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3lr00/3.1.1?

which says (in part),

"PGMNAME (LONGMIXED)
Program-name must be specified as a literal. "
```

##### ↳ ↳ Re: Annoying AIX COBOL Compiler....

- **From:** "Paul Raulerson" <praulerson@NOSPAM-hot.rr.com>
- **Date:** 2002-03-19T03:09:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rZxl8.29554$Dv6.1083326@typhoon.austin.rr.com>`
- **References:** `<O5xl8.29511$Dv6.1039534@typhoon.austin.rr.com> <a7690i$64t$1@slb7.atl.mindspring.net>`

```
Thanks Bill! I never even looked in the Identification Division, I was so
sure I was doing some stupid in the CALL...

Glad I could offer you a smile too! .

-Paul

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:a7690i$64t$1@slb7.atl.mindspring.net...
> Boy is it nice to have an "easy question" - and to understand (an obscure)
> compiler message.
…[20 more quoted lines elided]…
> > Okay, I'm out of my depth again. Would some of you guys with the wise
(if
> > not older!) heads
> > give me a hand here?
> >
> > I just have to call a C function from COBOL, something that should be
very
> > easy. In fact, it is
> > terrifically easy under Windows or OS/2, or better yet, on the Mainframe
…[5 more quoted lines elided]…
> > seem to eliminate. (Go figure - it will linkedit the .o file and create
an
> > executable file even with the
> > rotten error in there...)
> >
> > I wrote a super simply little COBOL and C program to test this. They are
> > reproduced below.  Ignore the case in the COBOL program; it is there
just
> > because I typed it in vi instead of a COBOL aware editor... ;)  The
> function
…[14 more quoted lines elided]…
> >      3  IGYDS1046-E   A user-defined word was used as a program under
the
> >                       "PGMNAME(LONGMIXED)" option.  The name was
accepted
> in
> >                       its uppercased format.
…[58 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
