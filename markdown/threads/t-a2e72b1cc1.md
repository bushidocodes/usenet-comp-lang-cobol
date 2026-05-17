[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Recipe for MF COBOL to C Program connectivity?

_5 messages · 4 participants · 1995-11 → 1995-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Recipe for MF COBOL to C Program connectivity?

- **From:** "park..." <ua-author-1084859@usenetarchives.gap>
- **Date:** 1995-11-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49itg0$oqh@newsbf02.news.aol.com>`

```
Does anyone have a step by step guide which will allow me to get my Micro
Focus COBOL programs to connect to my C routines which are stored in a
DLL?

Any suggestions really appreciated.
============================
Kevin Parker, Director,
Command Technology Corporation,
1040 Marina Village Parkway,
Alameda, CA, 94501, USA
```

#### ↳ Re: Recipe for MF COBOL to C Program connectivity?

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-11-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2e72b1cc1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<49itg0$oqh@newsbf02.news.aol.com>`
- **References:** `<49itg0$oqh@newsbf02.news.aol.com>`

```
Hi:
I have an old manual from Microsoft COBOL that mentions how to
do Windows using COBOL. They discuss how to make a DLL using
COBOL. But what you are doing is calling a DLL from COBOL.

I will check it tonight and try to mail some more info to you.

If your COBOL program is a Windows program, you could use LoadLibrary
function call using the WINAPI method. You would then call the name
of the function. But I have to check the manual. It could be that
you have to do imports or exports in your .Def file at link time.

I was able to call cobol dll from C and C++ by defining a pointer
to a function and then dereferencing the pointer.

However, calling C from COBOL is a little different.

you might try the following:

CALL WINAPI "__LoadLibrary" using by reference "MyDll.dll"
returning handletolibrary.

call winapi "__GetProcAddress" using by value handletolibrary
by reference "thefunction"
returning pointerfarproc

Can COBOL then CALL the function pointed to by pointerfarproc?

Well, I'd better check the manual. My head and my stomach is
spining looking at this...

Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

##### ↳ ↳ Re: Recipe for MF COBOL to C Program connectivity?

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-11-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2e72b1cc1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a2e72b1cc1-p2@usenetarchives.gap>`
- **References:** `<49itg0$oqh@newsbf02.news.aol.com> <gap-a2e72b1cc1-p2@usenetarchives.gap>`

```
The Manual I have says you can call a COBOL DLL as follows:

procedure division.
CALL "COBDLL"
CALL "COBENTRY"

Where the dll is named Cobdll.dll. Maybe you can do this with C DLL
also. The cobentry is the name of the entry point you want to use,
or in the case of c, the function name. You might have to add some
underscrores and/or modify the calling convention:

call winapi "cobdll"
call winapi "__thefunction"

Maybe if you use imports in your cobol main program .def file:

imports yourcdll.yourcdll
yourcdll.thefunction

Or make an import library using implib utility and then link it in:

implib yourcdll.lib yourcdll.dll


Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: Recipe for MF COBOL to C Program connectivity?

- **From:** "r..." <ua-author-12838970@usenetarchives.gap>
- **Date:** 1995-12-04T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2e72b1cc1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<49itg0$oqh@newsbf02.news.aol.com>`
- **References:** `<49itg0$oqh@newsbf02.news.aol.com>`

```

› Does anyone have a step by step guide which will allow me to get my Micro
› Focus COBOL programs to connect to my C routines which are stored in a
› DLL?

You might want to try giving Unidata Inc a call. They have a product called
Cobol Direct Connect.
Cheers
```

#### ↳ Re: Recipe for MF COBOL to C Program connectivity?

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1995-12-05T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2e72b1cc1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<49itg0$oqh@newsbf02.news.aol.com>`
- **References:** `<49itg0$oqh@newsbf02.news.aol.com>`

```
In message <<49itg0$o.··.@new··l.com>> par··.@a··.com writes:
› Focus COBOL programs to connect to my C routines which are stored in a
› DLL?

What environment is this ? It could be OS/2 text mode, PM or
Windows. If it is DOS then you probably can't without a whole
lot of work. If the Cobol progarms are Windows API or QuickWin
then it is possible to just CALL them with appropriate specification
of call type and parameters, such as:


I have a Windows API program and a MS-C .DLL called Interp.DLL
with a routine MathInterp(). In the Cobol it does a
CALL WINAPI "__MathInterp" USING BY VALUE I J L-KN
where the parameters are all long int in the C and S9(9) COMP-5
in the Cobol. Running IMPLIB on the .DLL creates a Interp.Lib
which is linked into the Cobol to satisfy the Call and cause
the .DLL to be loaded.

Hope this helps. If this is along the right lines then I can
pick out more details from what is actually happening. I tend
to solve problems then 'core dump' the solution, leving it
entirely up to the make file to recreate when necessary.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
