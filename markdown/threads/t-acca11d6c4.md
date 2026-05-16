[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AIX Cobol. How to get an environment variable?

_5 messages · 4 participants · 2000-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### AIX Cobol. How to get an environment variable?

- **From:** teyo2000@my-deja.com
- **Date:** 2000-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t6ue9$ekb$1@nnrp1.deja.com>`

```
Hello!

I have a problem when trying to consent to variables of having defined
in the
operating system AIX from a program Cobol.

Somebody could tell me what instructions of code Cobol I need to be
able to
use the value of a variable inside a program Cobol.

By example. I defined in AIX:
export MYVAR=anystring

And in my cobol program I need "some" to get the value of MYVAR

I have attempted with code lines as:

ACCEPT W-VAR FROM $MYVAR

But it doesn't compile

Exist any callable service of AIX that returns the value of an
environment variable ?

I am totally lost...

I will be very grateful to all the people that help me.

Thank you.

Forgive my horrible English



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: AIX Cobol. How to get an environment variable?

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-10-27T04:31:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qy7K5.1091$w6.727047@news3.rdc1.on.home.com>`
- **References:** `<8t6ue9$ekb$1@nnrp1.deja.com>`

```
Try

DISPLAY "MYVAR" UPON ENVIRONMENT-NAME
ACCEPT W-VAR FROM ENVIRONMENT-VALUE

<teyo2000@my-deja.com> wrote in message news:8t6ue9$ekb$1@nnrp1.deja.com...
> Hello!
>
…[33 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: AIX Cobol. How to get an environment variable?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-27T08:38:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tc0cf$op9$1@slb0.atl.mindspring.net>`
- **References:** `<8t6ue9$ekb$1@nnrp1.deja.com> <qy7K5.1091$w6.727047@news3.rdc1.on.home.com>`

```
I do not believe that IBM (on any platform) supports the X/Open syntax using
ACCEPT/DISPLAY for setting/getting environment variables.  The following
example is from the newest OS/390 Programmer Guide on how to do this under
Unix System Services.  I would *try* this technique - but I don't guarantee
that it will work.

***

CBL pgmname(longmixed)
Identification division.
Program-id.�envdemo �.
Data division.
Working-storage section.
01 P pointer.
01 PATH pic x(5)value Z �PATH �.
01 var-ptr pointer.
01 var-len pic 9(4)binary.
01 putenv-arg pic x(14)value Z �MYVAR=ABCDEFG �.
01 rc pic 9(9)binary.
Linkage section.
01 var pic x(5000).
Procedure division.
*Retrieve and display the PATH environment variable
Set P to address of PATH
Call �getenv � using by value P returning var-ptr
If var-ptr = null then
Display �PATH not set �
Else
Set address of var to var-ptr
Move 0 to var-len
Inspect var tallying var-len
for characters before initial X �00 �
Display �PATH =� var(1:var-len)
End-if
*Set environment variable MYVAR to ABCDEFG
Set P to address of putenv-arg
Call �putenv �using by value P returning rc
If rc not =0 then
Display �putenv failed �
Stop run
End-if
Goback.

   ***

My "cut-and-paste" lost all the formatting on this example, so if it gets
compiler errors "correct as necessary"
```

###### ↳ ↳ ↳ Re: AIX Cobol. How to get an environment variable?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-28T01:51:16+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F99664.CDA67719@zip.com.au>`
- **References:** `<8t6ue9$ekb$1@nnrp1.deja.com> <qy7K5.1091$w6.727047@news3.rdc1.on.home.com> <8tc0cf$op9$1@slb0.atl.mindspring.net>`

```
"William M. Klein" wrote:

> Call ?getenv ? using by value P returning var-ptr
> Call ?putenv ?using by value P returning rc

These look like they are straight out of the C runtime library.   For AIX the
variables are case specific.

a)  getenv returns a null (x'00') terminated string.

b) putenv takes a null terminated string like:

XYZ=abc x'00'

and creates a variable XYZ in your current space,  note that it will disappear
after you have completed your program.

One trap is that putenv requires different storage for each variable:

perform until eof
        read set-statements into putenv-field
        call 'putenv' using putenv-field
end-perform

will not work, from my experience with C over the last couple of days, it only
stores the last variable.   This would make the sample code wrong because the
'by value' would create an implicit temporary which would disappear as soon as
you returned from the call.

Execute the command 'set' to see the results of your work from within your
program.

Ken
```

###### ↳ ↳ ↳ Re: AIX Cobol. How to get an environment variable?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-27T13:58:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tcj2s$770$1@slb6.atl.mindspring.net>`
- **References:** `<8t6ue9$ekb$1@nnrp1.deja.com> <qy7K5.1091$w6.727047@news3.rdc1.on.home.com> <8tc0cf$op9$1@slb0.atl.mindspring.net> <39F99664.CDA67719@zip.com.au>`

```
"Ken Foskey" <waratah@zip.com.au> wrote in message
news:39F99664.CDA67719@zip.com.au...
> "William M. Klein" wrote:
>
…[3 more quoted lines elided]…
> These look like they are straight out of the C runtime library.   For AIX
the
> variables are case specific.

this is why the sample include the initial statement,

 CBL pgmname(longmixed)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
