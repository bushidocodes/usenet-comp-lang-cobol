[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL 4.0.32 Execution error 107 HELP!

_6 messages · 5 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL 4.0.32 Execution error 107 HELP!

- **From:** "Garry Dell" <gdell@laserdirect.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#qIX3BP39GA.286@upnetnews05>`

```
I created a program in MF COBOL for Windows NT 4.0 and then proceeded to
create the library and ultimately built the exe file according to
MicroFocus' directions.


When I went to execute the newly created exe file, I received the execution
error 107

the following is an excerpt from the screen:


error code: 107  pc=0, call=2, seg=0


Please help me to resolve this problems as I have already spent some time
with MicroFocus' tech Support personnel
and they were either unwilling or unable to help me with this.  (it seems as
this is apparently a new problem for them)


I looked up the error code and the manual says that execution error code is
as follows:


107     Operation not implemented in this run-time system (Fatal)

        You are trying to perform a file operation which your run-time
system does not support.

        You should recode your program so that it does not try such
operations, or you should acquire a version of your system that does support
this facility.




The only operations that my program is doing is opening a text file, reading
dat, writing data, and closing the file.  Nothing special is occuring in
this program and it runs fine under the animator.




Please help me to find the fix as I am unable to get any help from
MicroFocus.
```

#### ↳ Re: MF COBOL 4.0.32 Execution error 107 HELP!

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mZXJ1.262$te.380203@news2.mia.bellsouth.net>`
- **References:** `<#qIX3BP39GA.286@upnetnews05>`

```
Perhaps you should post the code?
```

##### ↳ ↳ Re: MF COBOL 4.0.32 Execution error 107 HELP!

- **From:** "Garry Dell" <gdell@laserdirect.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e2Iw$zQ39GA.257@upnetnews05>`
- **References:** `<#qIX3BP39GA.286@upnetnews05> <mZXJ1.262$te.380203@news2.mia.bellsouth.net>`

```
I found the problem, the problem is that I have to open up a DOS window and
then type the following:


setmfenv 32


this is not widely known and I suspect that most of the tech support
personnel don't have this information.



Judson McClendon <judmc123@bellsouth.net> wrote in message
mZXJ1.262$te.380203@news2.mia.bellsouth.net...
>Perhaps you should post the code?
>--
…[10 more quoted lines elided]…
>>When I went to execute the newly created exe file, I received the
execution
>>error 107
>>
…[6 more quoted lines elided]…
>>and they were either unwilling or unable to help me with this.  (it seems
as
>>this is apparently a new problem for them)
>
>
>
```

#### ↳ Re: MF COBOL 4.0.32 Execution error 107 HELP!

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e$v#FCd39GA.302@upnetnews03>`
- **References:** `<#qIX3BP39GA.286@upnetnews05>`

```

Garry Dell wrote in message <#qIX3BP39GA.286@upnetnews05>...
>I created a program in MF COBOL for Windows NT 4.0 and then proceeded to
>create the library and ultimately built the exe file according to
…[14 more quoted lines elided]…
>and they were either unwilling or unable to help me with this.  (it seems
as
>this is apparently a new problem for them)
>
…[11 more quoted lines elided]…
>operations, or you should acquire a version of your system that does
support
>this facility.
>
…[3 more quoted lines elided]…
>The only operations that my program is doing is opening a text file,
reading
>dat, writing data, and closing the file.  Nothing special is occuring in
>this program and it runs fine under the animator.
>


If the file is opened for input-output, you cannot just WRITE modified
records back into the file, you have to REWRITE them.

If the file is opened for input, you cannot either WRITE or REWRITE a
record.

If you want to WRITE records onto the end of an existing sequential file,
you must open extend.

Does that about cover the main bases for a sequential file?


>
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: MF COBOL 4.0.32 Execution error 107 HE

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.4283.16709@kcbbs.gen.nz>`
- **References:** `<#qIX3BP39GA.286@upnetnews05>`

```
In message <<#qIX3BP39GA.286@upnetnews05>> "Garry Dell" <gdell@laserdirect.com> writes:
> 
> The only operations that my program is doing is opening a text file, reading
> dat, writing data, and closing the file.  Nothing special is occuring in
> this program and it runs fine under the animator.

Does it do it in the order implied here ?:  OPEN READ WRITE CLOSE ?

Or are you doing it in a viable order: OPEN READ CLOSE OPEN WRITE
CLOSE ?

LINE SEQUENTIAL files cannot be both read and written to in
the same OPEN - you may get a 107 error if you do that.
```

#### ↳ Re: MF COBOL 4.0.32 Execution error 107 HELP!

- **From:** Karl Wagner <kwagner@sympatico.ca>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F88A29.A8AE3743@sympatico.ca>`
- **References:** `<#qIX3BP39GA.286@upnetnews05>`

```
Garry Dell wrote:
> 
> I created a program in MF COBOL for Windows NT 4.0 and then proceeded to
…[26 more quoted lines elided]…
> 

The last time I saw this it was because I had mismatched versions of the
run-time system (RTS) on the execution path. That is, my 4.0.32 .EXE was
trying to use an older RTS. It would explain why it works in the
animator but not from a command line.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
