[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can I get "Subscript out of range" error message from C program

_7 messages · 4 participants · 1997-07_

---

### Can I get "Subscript out of range" error message from C program

- **From:** "you" <ua-author-10579@usenetarchives.gap>
- **Date:** 1997-07-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5qpp4b$6os@reader.seed.net.tw>`

```

Hi everbody:
I have a MF COBOL problem, describe as floowing, Could anyone give
me some suggestions.
We use C and COBOL to write a server's program, then COBOL program
error in "Subscript out of range" and exit program such that client program
can't get any error message. Can I get "Subscript out of range" error message
from C program such that we can send this error message to client ? My Micro
Focus COBOL is version 3.1 for SCO/UNIX and 3.2 for AIX4.1,
HP-UX B.10.10, SunOS 5.5. sample program as follow: main.c:main(int argc, char
*argv[])
{ cobinit(); cobfunc("t",argc,argv); cobexit(); }
t.cob: IDENTIFICATION DIVISION.
PROGRAM-ID. TMSINITCOB.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 WK-INDEX PIC 9(2). 01 WK-AREA-OCCURS OCCURS 5 TIMES.
05 WK-AREA-DATA PIC 9(10).
LINKAGE SECTION.
PROCEDURE DIVISION.
MOVE 6 TO WK-INDEX.
MOVE 1 TO WK-AREA-OCCURS(WK-INDEX).
EXIT PROGRAM.
cc -c main.c ;cob -cx t.cob;cob -x -o t main.o t.o
We execute program t, then we get following error message: Object Code error :
file 't'
error code: 153, pc=144, call=1, seg=0 153 Subscript out of range
Can I get "Subscript out of range" error message from C program(main.c) such
that we can send this error message to client ?
```

#### ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-07-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5qpp4b$6os@reader.seed.net.tw>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw>`

```

In message <<5qpp4b$6.··.@rea··t.tw>> y··@som··t.somedomain writes:
› We execute program t, then we get following error message: Object Code error : 
› file 't'
…[3 more quoted lines elided]…
› 

Why don't you stop the error happening ?
```

##### ↳ ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "you" <ua-author-10579@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e87cf3a24c-p2@usenetarchives.gap>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw> <gap-e87cf3a24c-p2@usenetarchives.gap>`

```

In article <329··.@kcb··n.nz>, rip··.@kcb··n.nz says...
› 
› In message <<5qpp4b$6.··.@rea··t.tw>> y··@som··t.somedomain  writes:
…[10 more quoted lines elided]…
› 
Because my programs have two prat, One part is server program, the other
is client program. If this error happen, I want to my server program to
do following things:
(1)Clean resource(UNIX IPCs) of creation by server .
(2)Inform monitor of server to restart another same server.
(3)Inform error message to client program such that client program can
display error message to the user.
```

#### ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5qpp4b$6os@reader.seed.net.tw>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw>`

```

WuChihLiang wrote:
›
› ...snip...
› Can I get "Subscript out of range" error message from C program(main.c) such
› that we can send this error message to client ?

Option 1: All programming that I know of requires two things:
1. Default startup code
2. Library routines.

Either one of these will give you the answer to your problem. Look into
the fundamental calls that the compiler generates for an out of range
and tap into this call. If it branches to the startup code does this
code come with the compiler and can you hack it to perform your purpose.

Option 2: The cross language environment you use may have a tap into
the abend process for Cobol. If you can trap these abends then you know
what is happening.

Option 3: Agree with Richard and test the ranges yourself before use of
the subscript.

Good luck...
```

#### ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "you" <ua-author-10579@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5qpp4b$6os@reader.seed.net.tw>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw>`

```

In article ,
je··.@a.g··y.com says...
› 
› WuChihLiang wrote:
…[15 more quoted lines elided]…
› A Jedi craves not these things!"
Same result in case "MOVE 6 TO WK-INDEX."
Chih Liang Wu 1997/7/21
```

#### ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5qpp4b$6os@reader.seed.net.tw>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw>`

```

WuChihLiang wrote:
› 
› Hi everbody:
…[5 more quoted lines elided]…
› from C program such that we can send this error message to client ?

Hi.

Take a look at the CBL_ERROR_PROC call-by-name routine in your COBOL
System
Reference. You can call this from C before entering the COBOL program.
When an
error occurs and the function is called, parse the string supplied to
it.
Note that the return-code from your function will determine whether the
normal
COBOL RTS error routine is executed (and the error message output), but
you
cannot prevent the COBOL RTS from shutting down.
Note also that this routine could be called from within a signal handler
(in
the case when the error message is for error 114 or 115, for instance)
so you
should be careful about just what work you do in such a routine. It's
probably
a bad idea to start CALLing COBOL programs within this routine, also :)

Cheers,
Kev.
```

##### ↳ ↳ Re: Can I get "Subscript out of range" error message from C program

- **From:** "you" <ua-author-10579@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e87cf3a24c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e87cf3a24c-p6@usenetarchives.gap>`
- **References:** `<5qpp4b$6os@reader.seed.net.tw> <gap-e87cf3a24c-p6@usenetarchives.gap>`

```

In article <33D··.@mfl··o.uk>, k.··.@mfl··o.uk says...
› 
› WuChihLiang wrote:
…[17 more quoted lines elided]…
› Kev.
I have found COBOL sample program which call CBL_ERROR_PROC from COBOL
System Reference. Do you have any C sample programs which call
CBL_ERROR_PROC ?
Thanks.
WuChihLinag.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
