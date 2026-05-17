[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu V4 Dll's

_10 messages · 4 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu V4 Dll's

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t0ok5$5um$1@news.igs.net>`

```
I am trying to set up a project with a mainline and
several subroutines that are in a DLL. As long as
I name each DLL the same as the subroutine name,
all goes well. I understand that to put them into one
large DLL, I need to create a RES file that tells the
calling program what DLL to look in for each subroutine,
but I cannot seem to get it to work. Do I need a RES
file for both the main and the subroutine (one export
and one import?)?

Could someone give me an overview of the
relationships?
```

#### ↳ Re: Fujitsu V4 Dll's

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6t0ok5$5um$1@news.igs.net>`
- **References:** `<6t0ok5$5um$1@news.igs.net>`

```

Donald Tees wrote in message <6t0ok5$5um$1.··.@new··s.net>...
› I am trying to set up a project with a mainline and
› several subroutines that are in a DLL.  As long as
…[6 more quoted lines elided]…
› and one import?)?


Don,
I couldn't get this to work either.
If this *would* work, then one could put all the
Fujitsu runtime DLLs in one big DLL as well.
This does not seem to be possible.
We had a discussion on this a while back in
this NG, (it was about making one big EXE,
but close enough), but no solution emerged
and Fujitsu was remarkable quiet on this.
My ultimate goal in one big EXE, or next best:
one small EXE and one big DLL.
This is my midweek (and everyday!) whine.
```

##### ↳ ↳ Re: Fujitsu V4 Dll's

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p2@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap>`

```

Leif Svalgaard wrote in message <35f··.@new··m.net>...
›
› My ultimate goal in one big EXE, or next best:
› one small EXE and one big DLL.
› This is my midweek (and everyday!) whine.


Got it!
First, you set up a DLL in the project. Do all the standard
stuff and build it. Now, what happens is that the build creates
TWO files, XXX.DLL, and XXX.OBJ. The xxx.obj references
the xxx.dll, so you have to add XXX.LIB where XXX is the DLL
name to the library folder of the program that uses it.
example:
main.cbl is going to call suba.cbl and subb.cbl from mainsub.dll.
1. build mainsub.dll as if it was an exe file. mainsub.lib will be
created in the same area. mainsub's source file folder should contain
suba.cbl and subb.cbl.
2. add main.exe to the program, an put main.cbl in the source
file, then put mainsub.LIB in the library file. Mainsub.DLL never
gets mentioned in any MAIN folder, only MAINSUB.LIB.
3. Build the whole lot.

That will work as long as every CALL is of the form CALL "SUBA" etc.
If you are going to dynamically call as in:
MOVE "SUBA" TO SUBROUTINE-NAME.
CALL SUBROUTINE-NAME.
then it will not work. There should be a way to force *that* as
well, but I have not figured it out yet.
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

- **From:** "gene webb" <ua-author-6589136@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p3@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap>`

```
I am not sure if you can do this in Fujitsu, but the way you do it in
Microfocus is to create a variable of a procedure pointer and do the
following set theVariable to entry "NameOfDLL.DLL"


Donald Tees wrote in message <6t1m1s$343$1.··.@new··s.net>...
› 
› Leif Svalgaard wrote in message <35f··.@new··m.net>...
…[31 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

_(reply depth: 4)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p4@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap> <gap-7b94fad93b-p4@usenetarchives.gap>`

```

Gene Webb wrote in message <6t1rif$m.··.@ene··y.com>...
› I am not sure if you can do this in Fujitsu, but the way you do it in
› Microfocus is to create a variable of a procedure pointer and do the
› following set theVariable to entry "NameOfDLL.DLL"
›


You're going to have to be patient here, I've had this
compiler for about 70 hours so far ... I don't have a clue
what you are talking about. Could you give me a three liner
include I can paste into a test-program? I have it all working
now (DLLs build solved) for all but when I cannot force a load.
IE: call data-name
where: data-name picture x(8) value "subname".
if I: call "subname"
then: I have no problem.
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

_(reply depth: 5)_

- **From:** "gene webb" <ua-author-6589136@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p5@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap> <gap-7b94fad93b-p4@usenetarchives.gap> <gap-7b94fad93b-p5@usenetarchives.gap>`

```
working-storage.
01 pgmToCall pic x(8).
01 aProcedure procedure-pointer.
Procedure Division.

move "SUBNAME" to pgmToCall.
set aProcedure to entry pgmToCall.

Try something like that. It should force that DLL to be loaded.


Donald Tees wrote in message <6t21jk$g7b$1.··.@new··s.net>...
› 
› Gene Webb wrote in message <6t1rif$m.··.@ene··y.com>...
…[17 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

- **From:** "fujitsu software" <ua-author-6589312@usenetarchives.gap>
- **Date:** 1998-09-07T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p3@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap>`

```
Donald,

Fujitsu COBOL allows you to dynamically call sub programs as long as you use
the DLOAD compiler option.

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: http://www.adtools.com


Donald Tees wrote in message <6t1m1s$343$1.··.@new··s.net>...
› 
› Leif Svalgaard wrote in message <35f··.@new··m.net>...
…[31 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

_(reply depth: 4)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-09-07T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p7@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap> <gap-7b94fad93b-p7@usenetarchives.gap>`

```

Fujitsu Software wrote in message <6t3ptj$kgu$1.··.@nnt··t.com>...
› Donald,
› 
…[3 more quoted lines elided]…
› 
Thank you ...
```

###### ↳ ↳ ↳ Re: Fujitsu V4 Dll's

_(reply depth: 4)_

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-09-07T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p7@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap> <gap-7b94fad93b-p3@usenetarchives.gap> <gap-7b94fad93b-p7@usenetarchives.gap>`

```
Fujitsu Software wrote in message <6t3ptj$kgu$1.··.@nnt··t.com>...
› Donald,
› 
…[10 more quoted lines elided]…
››› This is my midweek (and everyday!) whine.


I think you are missing the point here.
What Donald and I and many others really want
is a way of packaging all the support modules
in one big DLL or EXE. THIS INCLUDES THE
FUJITSU F3I*.DLL modules. If you can't have
*ALL* the modules in one place, there is little
gained by having only *some* of them packaged.

We have had this discussion before. And always
we get an evasive answer from Fujitsu. Please,
be helpful this time. Thanks. If you can provide a
solution to this problem, Fujitsu Cobol is going to
kill the others.
```

##### ↳ ↳ Re: Fujitsu V4 Dll's

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-09-06T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7b94fad93b-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7b94fad93b-p2@usenetarchives.gap>`
- **References:** `<6t0ok5$5um$1@news.igs.net> <gap-7b94fad93b-p2@usenetarchives.gap>`

```
Well, I was able to get it all into one big EXE, but that is
not suitable, in this case. To get it into one big exe, you
can never call a routine without naming it explicitly.

IE- convert "call program-name" to
if program-name equals "sub1"
call "sub1"
else
if program-name equals "sub2"
call "sub2"
etc.

When you create a DLL, it seems that Fujitsu ALSO creates a .LIB
as a side effect. That can be put into the library folder for the project,
and will link provided every subroutine needed is referenced by
a direct call. If you have a complete list, the above code could be
put into a subroutine like so:

call program-name
is converted to:
call "caller" using program-name.

Caller would just list the names in an if statement ... then you get
one big EXE. My problem is that each customer uses a different
program to print invoices, and that program is named in a setup file.
That means my subroutine would have to have an IF for every
single customer.

› Don,
› I couldn't get this to work either.
…[9 more quoted lines elided]…
› This is my midweek (and everyday!) whine.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
