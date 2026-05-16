[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Return Code (RC)

_9 messages · 6 participants · 2000-10_

---

### Return Code (RC)

- **From:** "Curious" <leng1@bigfoot.com>
- **Date:** 2000-10-22T11:59:43+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8stoi7$8eq$1@violet.singnet.com.sg>`

```
Hi,

Just another question  :->

By the way, sometimes during compile or run
there is a return code of 08 or 16 or 04 or FLUSH etc.
May I know what is the meaning of all these and where
can I get the meaning of all these code in the system ?

In addition, normally after see those RC, I will just scroll
down page by page to look for those error. I believe there is
a better way to go directly. Could anybody let me know since
I am still trying to figure out those command and still fresh in
this kind of system.

Tks in advance :->

( P/S : By the way, is there any good web-site on those mainframe
          (OS/390) thing etc whereby I can readup so as to get a better
          concept on all these ( JCL, DB2, Bind etc )
```

#### ↳ Re: Return Code (RC)

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F2E058.30774667@zip.com.au>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg>`

```
Curious wrote:

>
> By the way, sometimes during compile or run
…[3 more quoted lines elided]…
>

By convention:

Return code 4 is a warning message
Return code 8 is an error message
Return code 16 is a severe error.

Flush occurs when the step was not executed.  For example it may have a
cond= statement that stopped it running,   it may be missing an input file
and failed on start up.


I am not sure what you mean by the second paragraph.   You might look up
locate in ISPF edit ('l 319600'  will take you to that line for example,
if you are using num on cob.

Ken
```

##### ↳ ↳ Re: Return Code (RC)

- **From:** "Curious" <leng1@bigfoot.com>
- **Date:** 2000-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8suouq$al7$1@violet.singnet.com.sg>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg> <39F2E058.30774667@zip.com.au>`

```

> 
> Ken wrote (extract)
> I am not sure what you mean by the second paragraph.   You might look up
> locate in ISPF edit ('l 319600'  will take you to that line for example,
> if you are using num on cob.
===> Hi ken, what I am trying to say is that once we see the return code,
         then, from there, how do u know which statement is wrong. How do u
         go DIRECTLY :-> to the statement that it went wrong. U see, I will
         normally scroll down page by page of those JCL statements to look
         for those errors statement. I believe there should be a better way.
         In addition, friend, thanks for explanation of those RC  :-> 



> 


"Ken Foskey" <waratah@zip.com.au> wrote in message news:39F2E058.30774667@zip.com.au...
> Curious wrote:
> 
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Return Code (RC)

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F420E8.EDC54BE7@zip.com.au>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg> <39F2E058.30774667@zip.com.au> <8suouq$al7$1@violet.singnet.com.sg>`

```
Curious wrote:

>  >
> > Ken wrote (extract)> I am not sure what you mean by the second
…[9 more quoted lines elided]…
> addition, friend, thanks for explanation of those RC  :->

Your compile will be set to NUM or NONUM on the options to the
compiler.   If it is NONUM then the line number in the message at the
bottom of the listing (thanks Bill) will refer to the relative line
number   ('num off' in edit).   If the option is NUM then the reference
will be the cobol line number ('num on cob' in edit).   To go to the
specific line and have a look at the source code simply put in
'L linenum' from the error message.

I very much treat warnings as errors as I have found quite a few
production faults lurking in warning messages.   I found them before the
customers picked them up.

Ken

(PS:  I typically subtract a few from linenum as locate puts the line
you jump to at the top of the screen and you generally need a few lines
above to get some context).
```

#### ↳ Re: Return Code (RC)

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8svk6s$lhdf9$1@ID-39920.news.cis.dfn.de>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg>`

```

Curious <leng1@bigfoot.com> wrote in message
news:8stoi7$8eq$1@violet.singnet.com.sg...
> Hi,
>
…[6 more quoted lines elided]…
>

Under normal convention, 04 is a warning, 08 is a conditional, 12 is an
error, and 16 is a severe error.  Of course, these can be returned by a user
program and may mean anything...

FLUSH means that the steo did not run.  This normally occurs when there is a
condition statement (COND=) in the JCL to allow the step to run only under
certain conditions.

> In addition, normally after see those RC, I will just scroll
> down page by page to look for those error. I believe there is
…[3 more quoted lines elided]…
>

I usually look for 'ABEND' - works most of the time.  If I am looking for a
JCL error, then I look for 'EXEC' last.  Again, it works most of the time...

> Tks in advance :->
>
…[3 more quoted lines elided]…
>

IBM has a Book Manager site that describes pretty much all of these things.
It isn't the easier to use, but the information is there if you can find it.
Try www.ibm.com and work from there...
```

##### ↳ ↳ Re: Return Code (RC)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8svodf$nc8$1@slb0.atl.mindspring.net>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg> <8svk6s$lhdf9$1@ID-39920.news.cis.dfn.de>`

```
If you are looking at/for compile-time (not run-time) "error" messages, I
suggest that you use the
   FLAG(W,W) - or FLAG(I,I)
compiler message.

This makes certain that your "error" (warning, informational) compile-time
messages (for IBM mainframe compilers) will occur in the "middle" of your
source code - by the very line that "caused" the problem - or at least what
the compiler THINKS is the line causing the problem.

The default (by IBM) is to JUST list the messages at the end of the listing.
This is "reasonable" if you are working with hard-copy - but not as useful
if looking at the output "on-line".
```

#### ↳ Re: Return Code (RC)

- **From:** ba600@FreeNet.Carleton.CA (Mike Kenzie)
- **Date:** 2000-10-22T04:05:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8stp1o$78o$1@freenet9.carleton.ca>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg>`

```
"Curious" (leng1@bigfoot.com) writes:
> Hi,
> 
> ( P/S : By the way, is there any good web-site on those mainframe
>           (OS/390) thing etc whereby I can readup so as to get a better
>           concept on all these ( JCL, DB2, Bind etc )

There is Bookmanager on the system which is full of stuff, it is also
available on CD and from the IBM web site
```

##### ↳ ↳ Re: Return Code (RC)

- **From:** "Curious" <leng1@bigfoot.com>
- **Date:** 2000-10-22T12:57:06+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8strto$8kb$1@violet.singnet.com.sg>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg> <8stp1o$78o$1@freenet9.carleton.ca>`

```

Hi Mike ,

If that's is the case,
then do u know how to go to the Bookmanager in the system
(ie the command) and if it is the web-site, what's the web-site
address :-> I went to www.ibm.com but couldn't find any  :->
Thanks in adv for the advise  :->


"Mike Kenzie" <ba600@FreeNet.Carleton.CA> wrote in message
news:8stp1o$78o$1@freenet9.carleton.ca...
> "Curious" (leng1@bigfoot.com) writes:
> > Hi,
…[6 more quoted lines elided]…
> available on CD and from the IBM web site
```

###### ↳ ↳ ↳ Re: Return Code (RC)

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sumiq$srm$1@nnrp1.deja.com>`
- **References:** `<8stoi7$8eq$1@violet.singnet.com.sg> <8stp1o$78o$1@freenet9.carleton.ca> <8strto$8kb$1@violet.singnet.com.sg>`

```
In article <8strto$8kb$1@violet.singnet.com.sg>,
  "Curious" <leng1@bigfoot.com> wrote:

>
> Hi Mike ,
>
> If that's is the case,
> then do u know how to go to the Bookmanager in the system

<SNIPPAGE>

Try any of the following:

http://publib.boulder.ibm.com/cgi-bin/bookmgr/LIBRARY

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/library

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/LIBRARY

Cheers,

Bill





Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
