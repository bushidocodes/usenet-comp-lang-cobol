[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call HLASM program from COBOL MVS program

_15 messages · 13 participants · 1998-12 → 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Call HLASM program from COBOL MVS program

- **From:** "Kin" <choick@asiaonline.net>
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76dfli$e6q2@news.asiaonline.net>`

```
I decided to write a COBOL MVS program which would pass several parameters
to an high level assembler program. Would anyone have some idea on that?

The programs are expected to run on OS/390 platform.

Thanks.
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** spam@nowhere.com
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<au7j2.215$v9.2162254@news3.voicenet.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```
Now, mind you, I am no Cobol expert.

The Cobol statement would be something like --

  CALL 'xxx' USING arg1, ...

and it is equivalent to this Assembler --

         CALL xxx,(arg1,...),VL

In <76dfli$e6q2@news.asiaonline.net>, "Kin" <choick@asiaonline.net> writes:
>I decided to write a COBOL MVS program which would pass several parameters
>to an high level assembler program. Would anyone have some idea on that?
…[5 more quoted lines elided]…
>


-- Steve Myers

The E-mail addresses in this message are private property.  Any use of them
to  send  unsolicited  E-mail  messages  of  a  commerical  nature  will be
considered trespassing,  and the originator of the message will be  sued in
small claims court in Camden County,  New Jersey,  for the  maximum penalty
allowed by law.
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76jatq$91m@dfw-ixnews8.ix.netcom.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```

Kin wrote in message <76dfli$e6q2@news.asiaonline.net>...
>I decided to write a COBOL MVS program which would pass several parameters
>to an high level assembler program. Would anyone have some idea on that?
…[5 more quoted lines elided]…
>

There really shouldn't be any problems or issues.  The one thing to think
about is the fact that the opposite (HLASM calling COBOL) *does* have some
issues about when the COBOL environment is set up.  So be a little careful
about "who's on top" of your application)
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<368E5783.A5DC5158@ASPMnetdoor.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```
A note about the parameters on the assembler side.  If register 1 = 0, no
parameters were passed.  If all parameters were passed by reference, register
1 will point to a parameter list.  After doing the using, register save, and
new save area, do a  LM 4,7,0(1) and registers 4-7 will point to the
parameters passed them.

Kin wrote:

> I decided to write a COBOL MVS program which would pass several parameters
> to an high level assembler program. Would anyone have some idea on that?
>
> The programs are expected to run on OS/390 platform.
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "Simon Cordingley" <simonc@casegen.co.uk>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<368ff80f.0@mercury.nildram.co.uk>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```
Hi

We do this all the time at Casegen - contact me if you need help.

Simon Cordingley
Casegen Systems Ltd
www.casegen.co.uk

Kin wrote in message <76dfli$e6q2@news.asiaonline.net>...
>I decided to write a COBOL MVS program which would pass several parameters
>to an high level assembler program. Would anyone have some idea on that?
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "Chris Craddock" <crashclc@netin.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76oa46$llg$1@news.onramp.net>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```

Kin wrote in message <76dfli$e6q2@news.asiaonline.net>...
>I decided to write a COBOL MVS program which would pass several parameters
>to an high level assembler program. Would anyone have some idea on that?


It is pretty simple. If the asm program is called from Cobol like this...

    CALL asmcode USING arg1 arg2 etc

Then the asm program will receive control (via standard linkage) with R1
pointing to a list of addresses. The first one is the address of arg1, the
second is the address of arg2 etc.

>The programs are expected to run on OS/390 platform.

In that case you can probably save yourself a little bit of programming
effort by having your assembler code run under the control of LE. Go look at
the LE book on interlanguage calls. The CEEENTRY macro can be used to
perform entry linkage and obtain working storage (if required) and the
CEEEXIT macro can be used to return control to your calling program.

Enjoy!
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** Chris Franklin <cfranklin@co.slo.ca.us>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<369127C5.FB8019DA@co.slo.ca.us>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```
Aside from all the good answers given already, I have a couple of questions
for you to ponder.

1) Does the sub-program already exist ? If so then the only concern you should
have is providing the parameters it requires.

2) If you intend to write the assembly and need help on basic parameter list
stuff, do you know enough assembler to complete the task ?

3) Is assembly language the best language for the sub-program? Is there a
requirement that cannot be satisfied with COBOL ?



Kin wrote:

> I decided to write a COBOL MVS program which would pass several parameters
> to an high level assembler program. Would anyone have some idea on that?
…[3 more quoted lines elided]…
> Thanks.
```

##### ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "Kin" <choick@asiaonline.net>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76t9p6$774@news.asiaonline.net>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us>`

```

Chris Franklin wrote in message <369127C5.FB8019DA@co.slo.ca.us>...
>Aside from all the good answers given already, I have a couple of questions
>for you to ponder.
>
>1) Does the sub-program already exist ? If so then the only concern you
should
>have is providing the parameters it requires.
>
Actually, the subprogram exist ... but need a little customization.

>2) If you intend to write the assembly and need help on basic parameter
list
>stuff, do you know enough assembler to complete the task ?
>
>3) Is assembly language the best language for the sub-program? Is there a
>requirement that cannot be satisfied with COBOL ?
>
The subprogram need to output message from MVS console. I wonder if COBOL
program can do that.

>
>
>Kin wrote:
>
>> I decided to write a COBOL MVS program which would pass several
parameters
>> to an high level assembler program. Would anyone have some idea on that?
>>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** mrm@lerami.lerctr.org (Ray Mullins)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<F53Lz3.Mon@lerami.lerctr.org>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net>`

```
In article <76t9p6$774@news.asiaonline.net>, Kin <choick@asiaonline.net> wrote:
>
>Chris Franklin wrote in message <369127C5.FB8019DA@co.slo.ca.us>...

[snipped first part, but it is excellent - after all, he had a good teacher
  at a good school  :-)]

>>3) Is assembly language the best language for the sub-program? Is there a
>>requirement that cannot be satisfied with COBOL ?
>>
>The subprogram need to output message from MVS console. I wonder if COBOL
>program can do that.

DISPLAY whatever UPON CONSOLE is how to do it in COBOL. If you need
a response from the operator, ACCEPT whatever FROM CONSOLE.

ObASM370:  If you need to call a WTO program, it probably has two parameters,
the length of the text and the text itself.

Later,
Ray
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76tp6d$arf@dfw-ixnews6.ix.netcom.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net>`

```

Kin wrote in message <76t9p6$774@news.asiaonline.net>...
>
>Chris Franklin wrote in message <369127C5.FB8019DA@co.slo.ca.us>...

>>3) Is assembly language the best language for the sub-program? Is there a
>>requirement that cannot be satisfied with COBOL ?
…[4 more quoted lines elided]…
>>


  DISPLAY xxxx UPON CONSOLE
      or
  ACCEPT xxxx FROM CONSOLE

work just fine with any MVS COBOL (however, many shops don't like this - but
it certainly should be allowed whenever a WTOR is allowed in Assembler)
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

_(reply depth: 4)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<36926F7C.64D49EB@home.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net> <76tp6d$arf@dfw-ixnews6.ix.netcom.com>`

```
> 
>   DISPLAY xxxx UPON CONSOLE
…[4 more quoted lines elided]…
> it certainly should be allowed whenever a WTOR is allowed in Assembler)

Many shops disable it entirely!

I have worked where UPON CONSOLE wasn't necessary - and their printed
consoles would sometimes have somebody's COBOL loop displaying until the
operators killed the job!!
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** WOB@my-dejanews.com
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<76tugj$pv2$1@nnrp1.dejanews.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net>`

```
In article <76t9p6$774@news.asiaonline.net>,
  "Kin" <choick@asiaonline.net> wrote:
> >
> The subprogram need to output message from MVS console. I wonder if COBOL
> program can do that.
>

Kin,

Do you need to issue the console messages in CICS or Batch? For CICS, use the
WRITE OPERATOR command (CICS/ESA only). For Batch, use DISPLAY UPON CONSOLE. I
believe CICS/VSE 2.2 and greater supports the WRITE OPERATOR command as well.

HTH....

WOB,
Atlanta




-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<3692a31b.175872168@news1.ibm.net>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net>`

```
On Tue, 5 Jan 1999 23:09:45 +0800, "Kin" <choick@asiaonline.net>
wrote:


>The subprogram need to output message from MVS console. I wonder if COBOL
>program can do that.

I know 50 other people are going to answer this, but:

DISPLAY "OUTPUT MESSAGE" UPON CONSOLE.
```

###### ↳ ↳ ↳ Re: Call HLASM program from COBOL MVS program

- **From:** "German Castillo" <gcastillo@corpbanca.com.ve>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<5eqk2.1680$E_3.52@news01>`
- **References:** `<76dfli$e6q2@news.asiaonline.net> <369127C5.FB8019DA@co.slo.ca.us> <76t9p6$774@news.asiaonline.net>`

```
There is an Excellent Book (It Might be hard to find tho) wich explains this
and many more issues regarding Beside Calls from Any Programing language
using MVS Standard Linkage.
It is (If I recall properly... If not I am sure many other people reading
can correct me)
MVS Programing for Systems & Application Programmers
The Author is Carmine Cannatelo
It could teach anybody good Assembler Techniques. Very Good Value If you
Find it
Cheers, German

Kin escribi� en mensaje <76t9p6$774@news.asiaonline.net>...
>
>Chris Franklin wrote in message <369127C5.FB8019DA@co.slo.ca.us>...
>>Aside from all the good answers given already, I have a couple of
questions
>>for you to ponder.
>>
…[29 more quoted lines elided]…
>
```

#### ↳ Re: Call HLASM program from COBOL MVS program

- **From:** John A Parke <jparke@mindspring.com>
- **Date:** 1999-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<3697BDE6.54BE8427@mindspring.com>`
- **References:** `<76dfli$e6q2@news.asiaonline.net>`

```
I don't know if I understand your question correctly.  If you  mean that your
Cobol program is going to call an Assembler program then the answer is pretty
straight forward.

The MVS convention is for the calling program, in this case COBOL to pass the
address in register 1 of a list of addresses of the passed parameters.  COBOL
will do this for you automatically.  The Assembler program  gets the address
of the passed parameters by again using register 1.  Just remember that R1
points to a  list of addresses of the passed parameters and not the actual
parameters themselves. Each address is 4 bytes long, so that the first address
is pointed to by R1, the 2nd address is at the address in R1 + 4, etc.

The last parameter address will have it's high order bit set to x'80' ,
however this isn't a concern if you're always passing a fixed number of
arguments.

I hope I understood your question and provided some help.

John

Kin wrote:

> I decided to write a COBOL MVS program which would pass several parameters
> to an high level assembler program. Would anyone have some idea on that?
…[3 more quoted lines elided]…
> Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
