[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL - CALLING OS COMMANDS

_2 messages · 2 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL - CALLING OS COMMANDS

- **From:** "Tom McCormick" <tmccormick@amp.com>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde6fc$ae1e2480$02d011cc@tmccormick.gb.amp.com>`

```
Simple question,

We have recently "upgraded" from MF COBOL to IBM COB2, we have about 6
COBOL programs, key to these programs is the ability to CALL an OS function
in our case an AIX 4.0 UNIX shell script. Using MF COBOL we called SYSTEM
passing the shell script name as a parameter, the syntax is incorrect for
IBM COBOL I only have postscript manual which I can't search.

My question is how can I run (Call) an OS command from the COBOL programs


TIA

rcooper@amp.com
rcooper@psesoft.com
rcooper@netcomuk.co.uk
```

#### ↳ Re: IBM COBOL - CALLING OS COMMANDS

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uc56q$ugb@lotho.delphi.com>`
- **References:** `<01bde6fc$ae1e2480$02d011cc@tmccormick.gb.amp.com>`

```
Off the top of my head, you could call the "_system" call in
the CLIB library directly of course, but that may not be very 
portable. Why not try something like this? 

Create a C object file with a function like this in it:

> $ cat systemcall.c          
> void systemcall( char *cmd) 
…[4 more quoted lines elided]…
> $                           

Then create a COBOL program something like this:

> $ cat c.cbl                                             
>       **********************                            
…[17 more quoted lines elided]…
> $                                                         

Then it is very simple to link them together, and you simply
change your null terminated string to whatever command or
set of commands you want to execute. 


> $ cc -c systemcall.c
> $ cob2 -q"pgmname(mixed) callint(optlink) adata" -o c c.cbl systemcall.o
…[3 more quoted lines elided]…
> End of compilation 1,  program C,  highest severity: Informational.  

Running the "c" program created fro the COBOL compile works just
as expected. 

You can find more examples of this, and probably better ones 
on pp. 376-385 of the Programming Guide.  

I tested this under AIX 4.2.1 by the way. I assume it will work
just fine under 4.3. 

Yours,
-Paul





















: We have recently "upgraded" from MF COBOL to IBM COB2, we have about 6
: COBOL programs, key to these programs is the ability to CALL an OS function
: in our case an AIX 4.0 UNIX shell script. Using MF COBOL we called SYSTEM
: passing the shell script name as a parameter, the syntax is incorrect for
: IBM COBOL I only have postscript manual which I can't search.

: My question is how can I run (Call) an OS command from the COBOL programs


: TIA

: rcooper@amp.com
: rcooper@psesoft.com
: rcooper@netcomuk.co.uk
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
