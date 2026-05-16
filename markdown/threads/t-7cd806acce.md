[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FUJITSU 5.0 calling a .DLL

_16 messages · 8 participants · 2002-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### FUJITSU 5.0 calling a .DLL

- **From:** tomnj9612@aol.com (TOM NJ9612)
- **Date:** 2002-02-06T21:43:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```
Hello all,

     We are using Fujitsu 5.0.  We need to link to a .DLL to get information
back into the program.  When it calls the DLL we get the following message :

JMP00151-U cannot call PGRM GET
code 0x485

     The DLL we got, was a third party DLL. The company gave us what to pass
it, but it never appears to make it there.  I am assuming that we have done
something wrong with the linking of it.  
     Any help would be greatly appreciated.

Thanks in advance.
```

#### ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-02-07T11:08:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c62536f_7@Usenet.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```
This is caused by the called program not being found, or the parameters to
it being incompatible.

Ensure the dll is in the current directory or on the system path.

DON'T try and statically link to it. Call it dynamically.

Ensure the parameter list you give it is in the correct order that it
expects and DON'T use RETURNING in your call.

Just pass the result field in the list like any other parameter.

example:
...
01  the-get-program   pic x(15) value "GET".

call the-get-program
      using    parm-1
                  parm-2
                  GET-result
      on exception
                  ....whatever
end-call

If this .DLL is an activeX control make sure it is registered with RegSvr32.
In this case you shouldn't be calling it at all (you must INVOKE its
Methods) so I'll assume that it isn't.

If it still doesn't work, it is probably because the .DLL is expecting
parameters by Value rather than by Reference. Consult the vendor and find
out EXACTLY what it needs, of what type, in what order, and HOW they must be
passed.

I would advise using a Component, rather than a .DLL. These simply plug in
to your application and are invoked easily. (See ActiveX above.) If you
really MUST use a .dll, expect to have problems with parameter passing,
especially if it is from a vendor who doesn't use COBOL.

It is possible to call .DLLs from V5. I do it all the time. Don't lose
hope...<G>

Pete.

TOM NJ9612 <tomnj9612@aol.com> wrote in message
news:20020206164347.20792.00002058@mb-cg.aol.com...
> Hello all,
>
>      We are using Fujitsu 5.0.  We need to link to a .DLL to get
information
> back into the program.  When it calls the DLL we get the following message
:
>
> JMP00151-U cannot call PGRM GET
> code 0x485
>
>      The DLL we got, was a third party DLL. The company gave us what to
pass
> it, but it never appears to make it there.  I am assuming that we have
done
> something wrong with the linking of it.
>      Any help would be greatly appreciated.
>
> Thanks in advance.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "JerryMouse" <invalid@invalid.net>
- **Date:** 2002-02-06T22:57:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```

"TOM NJ9612" <tomnj9612@aol.com> wrote in message
news:20020206164347.20792.00002058@mb-cg.aol.com..
.
> Hello all,
>
>      We are using Fujitsu 5.0.  We need to link
to a .DLL to get information
> back into the program.  When it calls the DLL we
get the following message :
>
> JMP00151-U cannot call PGRM GET
> code 0x485
>
>      The DLL we got, was a third party DLL. The
company gave us what to pass
> it, but it never appears to make it there.  I am
assuming that we have done
> something wrong with the linking of it.
>      Any help would be greatly appreciated.

What command are you using? You don't normally
link called DLLs (that's why they're called
'Dynamic'). And, of course, the operating system
has to be able to find them at execute time, so
you'll need to specify the path (somewhere).

In PowerCOBOL it's

INVOKE POW-SELF 'CALLFORM' USING 'entryname'
'dllname'

example:

INVOKE POW-SELF 'CALLFORM' USING 'MYBEGIN'
'MYDLL.DLL'.
```

##### ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-02-07T23:27:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c625a8d_1@Usenet.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com>`

```

JerryMouse <invalid@invalid.net> wrote in message
news:ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com...
>
>
…[9 more quoted lines elided]…
>
Oh No it isn't <G>!

This invokes the CALLFORM method of the Form you are currently using, which
expects a specific type of .DLL.  You cannot use this to activate ANY .DLL.

As he never said he was using PowerCOBOL or OO Methodology, it would be
quite pointless to use INVOKE at all.

See the response I wrote to him.

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "JerryMouse" <invalid@invalid.net>
- **Date:** 2002-02-07T14:24:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I6w88.13263$6o2.766541@bin4.nnrp.aus1.giganews.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com> <3c625a8d_1@Usenet.com>`

```

"Peter E. C. Dashwood" <> >
> >
> > In PowerCOBOL it's
…[11 more quoted lines elided]…
> This invokes the CALLFORM method of the Form you
are currently using, which
> expects a specific type of .DLL.  You cannot use
this to activate ANY .DLL.
>
> As he never said he was using PowerCOBOL or OO
Methodology, it would be
> quite pointless to use INVOKE at all.

Oh Yes it is.
"In PowerCOBOL it's INVOKE...." an astonishingly
true statement.
If he has FJ COBOL V5, he has PowerCOBOL - he may
not be USING PowerCOBOL (although I can't imagine
why not).

>
> See the response I wrote to him.

I saw your response. But shouldn't the defintion
be:

01 The-Get-Program  PIC X(15) value "GET.DLL".

I don't think the loader is smart enough to
distinguish between GET.BAT, GET.COM, GET.EXE and
GET.DLL (or even GET.DOC).
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-02-08T11:45:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c63049c_1@Usenet.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com> <3c625a8d_1@Usenet.com> <I6w88.13263$6o2.766541@bin4.nnrp.aus1.giganews.com>`

```

JerryMouse <invalid@invalid.net> wrote in message
news:I6w88.13263$6o2.766541@bin4.nnrp.aus1.giganews.com...
>
>
> Oh Yes it is.
> "In PowerCOBOL it's INVOKE...." an astonishingly
> true statement.

Oh No it ISN'T!

Power COBOL is Object Oriented and therefore must use INVOKE to activate
object methods. However to Call a .DLL you would still need to use CALL. It
is not the use of INVOKE that I questioned. It is the use of the CALLFORM
Method as a means to call a non PowerCOBOL .DLL.

While your statement may be true, it is not applicable to the case in point.


> If he has FJ COBOL V5, he has PowerCOBOL - he may
> not be USING PowerCOBOL (although I can't imagine
> why not).
>

There are many reasons why people use or don't use a product. I share your
appreciation of PowerCOBOL and have used it for developing GUI applications
and COM components for a number of years now (since Version 3 (16 bit), in
fact). Nevertheless, when I want to call a third party .DLL I don't (and
cannot) use INVOKE. The only exception to this would be if the .DLL was a
registered ActiveX control or was an OLE (COM) server. Paolo mentioned this
in his post.

INVOKE is used to activate Object Methods. CALL is used to activate
sub-programs and external programs. (.DLLs come in this latter category.)

There are a number of things you have wrong in this post (usually you are
pretty right, but on this occasion you are demonstrating a serious lack of
understanding).

I believe you are using PowerCOBOL and have never looked at OO programming
and principles. If you had, you would understand the subtle distinction
between the use of INVOKE and the use of CALL.This is not an expressed or
implied criticism. Many people use PowerCOBOL without knowing OO. One of the
big pluses of the product is that you CAN do this.

Your statement above that if he has V5 he has PowerCOBOL is also NOT
accurate. Power COBOL is provided only with the Professional and Enterprise
editions of the product.

> >
> > See the response I wrote to him.
…[9 more quoted lines elided]…
>
Well, Jerrymouse, maybe you should do a little more testing and a little
less "thinking..."<G>

Wrong again. The extension is not required when calling a .DLL

You would know this if you had ever actually done what you are offering
advice about.

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-02-08T07:44:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C6381C9.84DA3E5F@Azonic.co.nz>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com> <3c625a8d_1@Usenet.com> <I6w88.13263$6o2.766541@bin4.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:
> 
> If he has FJ COBOL V5, he has PowerCOBOL -

No. Wrong.  Fujitsu comes in three price levels.  The Standard edition
does not include PowerCobol, only the Professional and Enterprise do.

> he may
> not be USING PowerCOBOL (although I can't imagine
> why not).

Because:
    a) he doesn't have it
 or b) it is inappropriate to his needs
 or c) he doesn't want to be locked to a single
       vendor 
 or d) he doesn't want to ne locked to a single OS
 or e) he uses another GUI such as SP/2
 or f) he has existing code he is porting to FJ

On point b), not all programs are appropriate for Windows 'point and
click'.  Some may be Web CGI programs, others may have no on-going user
interface, being background service programs.

In fact one of my gripes with many web sites is that they attempt to
provide 'a really nice user interface' for things that should require
_no_ user interface at all.  In some cases it is necessary for a user to
read one screen (their local computer system) and type into a web
enquiry screen and then read the results to be typed into the computer
system.

Get a decent program-to-program interface and the user need not be
involved at all.

I am sure that someone else with imagination can think of many other
reasons for not using PowerCobol.
```

##### ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** tomnj9612@aol.com (TOM NJ9612)
- **Date:** 2002-02-07T16:11:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020207111117.13561.00000023@mb-mv.aol.com>`
- **References:** `<ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com>`

```
Hi Jerry, 

 Your code is a good start.
  Thanks for your response.  We are using the below code:

Call 'GET' with STDCALL using
by reference field-name
by value       field-name

   Unfortunatly, I only have the code that the consultant left me, but will get
more information tommorow.
    I beleive it is a BTREIVE call.

Thanks again.

Tom
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-02-08T11:54:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c636878_7@Usenet.com>`
- **References:** `<ixi88.911$6o2.93385@bin4.nnrp.aus1.giganews.com> <20020207111117.13561.00000023@mb-mv.aol.com>`

```
TOM NJ9612 <tomnj9612@aol.com> wrote in message
news:20020207111117.13561.00000023@mb-mv.aol.com...
> Hi Jerry,
>
>  Your code is a good start.
>   Thanks for your response.  We are using the below code:

I don't know whether Jerry has sent you code privately. The only code I can
see in this public thread was posted by me.

>
> Call 'GET' with STDCALL using
> by reference field-name
> by value       field-name
>

This is a static call. It can never succeed. Please see the example code I
posted in response to your original query.

You must use a dynamic call.

>    Unfortunatly, I only have the code that the consultant left me, but
will get
> more information tommorow.
>     I beleive it is a BTREIVE call.
>
If you are trying to call a BTRIEVE function written in C, there may be
other considerations for the call as well.

See how you go with the dynamic call.

Pete.






 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-02-06T23:06:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0202062306.295c111@posting.google.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```
tomnj9612@aol.com (TOM NJ9612) wrote in message news:<20020206164347.20792.00002058@mb-cg.aol.com>...
> Hello all,
> 
…[11 more quoted lines elided]…
> Thanks in advance.

********************************************************************************
Hi,
         I am agree with Jerrymouse's view. Generally DLL are not
linked, it is loaded at runtime. I do not experience with Fujitsu but
on OS/390 I dynamically called DLL. For calling DLL from COBOL program
you have to compile and bind COBOL program with
'RENT,NOEXPORTALL,NODYNAM,DLL' options.
         You can statically link DLL with COBOL but it is not a good
programming practice.
         Hope this helps.
Regards.
shyam
```

##### ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-02-08T07:59:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C63854F.F67BA17B@Azonic.co.nz>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <c02fd744.0202062306.295c111@posting.google.com>`

```
shyam nivas wrote:

>          I am agree with Jerrymouse's view. Generally DLL are not
> linked, it is loaded at runtime. I do not experience with Fujitsu but
> on OS/390 I dynamically called DLL. For calling DLL from COBOL program
> you have to compile and bind COBOL program with
> 'RENT,NOEXPORTALL,NODYNAM,DLL' options.

I am not sure that describing a _completely_ different system is at all
helpful and is likely to lead to more confusion.

> You can statically link DLL with COBOL but it is not a good
> programming practice.

With Fujitsu (in my limited experience with it) it may be that small
stub library routines (.LIB) are required to be linked into the program
to satify the call linkage, these may then cause the DLL to load when
the program starts and they invoke the actual .DLL routines when the
CALL is executed.

This avoids one problem with .DLLs where the CALL is to a routine in a
DLL of a completely different name to that of the routine, as is mostly
the case.

He is calling 'GET' but I doubt that he has a 'GET.DLL' to resolve to. 
By statically linking a 'AddOn.LIB' derived from 'AddOn.DLL' containing
a stub for the 'GET' routine then the linker can resolve the CALL _and_
at run-time it will be known which 'GET' to execute.
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-02-08T01:14:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0202080114.303c031e@posting.google.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <c02fd744.0202062306.295c111@posting.google.com> <3C63854F.F67BA17B@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3C63854F.F67BA17B@Azonic.co.nz>...
> shyam nivas wrote:
> 
…[25 more quoted lines elided]…
> at run-time it will be known which 'GET' to execute.

********************************************************************************
Hello Richard,
                  You are absolutely right. I have faced similar
problem on OS/390. I have defined several fuction in DLL and saved the
DLL with different name than the fuctions name, from COBOL program
when I call function then at runtime I got error "Requested module not
found". From you reply I interpret that I need to linkedit a stub
program that will help in resolving function name in the DLL.But how
do we get the stub program if I am writing own DLL in C language on
OS/390?

Thanks and Regards.
shyam
```

###### ↳ ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2002-02-09T14:55:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020209095502.25819.00000775@mb-ce.aol.com>`
- **References:** `<c02fd744.0202080114.303c031e@posting.google.com>`

```
In article <c02fd744.0202080114.303c031e@posting.google.com>,
nivas_shyam@indiatimes.com (shyam nivas) writes:

>ound". From you reply I interpret that I need to linkedit a stub
>program that will help in resolving function name in the DLL.But how
…[6 more quoted lines elided]…
>

I belive that you can code the COBOL side to force dynamic linkage by using
the CALL <data-name> syntax.  As for matching the actual Function within 
a DLL with multiple routines/entrypoints, This should be able to be resolved in
the 
Run-Time Environment setup area.

[CALLDLL]                     <- main program
@EnvSetWindow=UnUse
IconDLL=F3BIIconn.dll

[CALLDLL.ENTRY]           <- entry point control for dynamic library calls
SUBPROGRAM3=SUBDLL3.DLL      <- <called name>=<actual dll file name>
Entry1=CALLDLL
```

#### ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2002-02-07T01:56:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0202070156.308eb057@posting.google.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```
tomnj9612@aol.com (TOM NJ9612) wrote in message news:<20020206164347.20792.00002058@mb-cg.aol.com>...
> Hello all,
> 
…[11 more quoted lines elided]…
> Thanks in advance.

Hi,
From the message you get, it seems that you are trying to use the
special OLE class that comes with Fujitsu's compiler. Of course it
will only work with OLE modules; that is, modules that have been built
with the apropriate tags to be COM compliant.
I have been able to call both COM and non COM DLLs from a Fujitsu
program, but the techniques are quite different.
May be if you elaborate a bit on the subject, we could help you.
regards,
Paulo Vieira, Emporsoft
```

##### ↳ ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-02-07T23:42:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c62fd8c_4@Usenet.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com> <b5b8d7c7.0202070156.308eb057@posting.google.com>`

```

Paulo Vieira <pvieira@emporsoft.pt> wrote in message
news:b5b8d7c7.0202070156.308eb057@posting.google.com...
> tomnj9612@aol.com (TOM NJ9612) wrote in message
news:<20020206164347.20792.00002058@mb-cg.aol.com>...
> > Hello all,
> >
> >      We are using Fujitsu 5.0.  We need to link to a .DLL to get
information
> > back into the program.  When it calls the DLL we get the following
message :
> >
> > JMP00151-U cannot call PGRM GET
> > code 0x485

> From the message you get, it seems that you are trying to use the
> special OLE class that comes with Fujitsu's compiler.

HUH?!

There is no indication he is trying to activate an OLE server here and this
message is NOT just produced when you DO fail to access an OLE server.  (In
fact, under these circumstances you get a lot more than just 0x485...)I have
had this message when accessing simple .DLLs as he is apparently trying to
do.)

This code simply means that the system cannot locate the .DLL or there is an
inconsistency in the parameter passing.

Please see my response to him elsewhere in this thread.

> Of course it
> will only work with OLE modules; that is, modules that have been built
> with the apropriate tags to be COM compliant.

COM servers in the Fujitsu environment generally return a 0x8??????? code
when they fail.

> I have been able to call both COM and non COM DLLs from a Fujitsu
> program, but the techniques are quite different.

Me too. And I agree. But in this instance he is not talking about a COM
.DLL.

> May be if you elaborate a bit on the subject, we could help you.
Always good advice...<G>

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: FUJITSU 5.0 calling a .DLL

- **From:** Jeff Campbell <jcampbell@ins-msi.com>
- **Date:** 2002-02-07T17:55:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C62B671.1654EEEF@ins-msi.com>`
- **References:** `<20020206164347.20792.00002058@mb-cg.aol.com>`

```
You may want to use DUMPBIN to check the .DLL for the "GET" entry you
are trying to call. Perhaps the function's name was changed.

I assume you have included the type library for the .DLL in your project
(no compile errors).

Jeff Campbell
n8wxs@arrl.net

TOM NJ9612 wrote:
> 
> Hello all,
…[12 more quoted lines elided]…
> Thanks in advance.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
