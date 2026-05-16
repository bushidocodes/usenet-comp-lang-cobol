[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Effective use of DOS base memory for COBOL programs

_11 messages · 8 participants · 2002-08_

---

### Effective use of DOS base memory for COBOL programs

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2002-08-20T02:18:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
Hi there,

I have MF COBOL programs running under MS DOS. What I understand is
that Micro Focus COBOL is using the base memory (640K) to run the
program.

Thus, when loaded with DOS, with some networking protocols, there will
only left about 600K base memory. Some of my programs are quite big
that required more than 600K base memory. At the end, the program is
unable to load and giving errors.

I have to separate those BIG programs into few smaller programs. But
the processing will be a bit slower and less efficient.

Please, is there anyone can help me to run the MF COBOL programs under
base memory, either by using less base memory, or how to use less
memory?

Thank you.

Regards,
Calvin
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-08-20T09:40:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W7o89.3404$yt3.1436025@newssrv26.news.prodigy.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
"Calvin" <calvinchin@fm333.com> wrote in message
news:62843e96.0208200118.5e0f7207@posting.google.com...
>
> Thus, when loaded with DOS, with some networking protocols, there will
> only left about 600K base memory. Some of my programs are quite big
> that required more than 600K base memory....

> Please, is there anyone can help me to run the MF COBOL programs under
> base memory, either by using less base memory, or how to use less
> memory?

You cannot get a quart from a pint pot, so your only option is to write
programs requiring less memory.

MCM
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** patrick.magee@microfocus.com (Patrick Magee)
- **Date:** 2002-08-20T08:13:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d27f2e40.0208200713.5e1c52b4@posting.google.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
calvinchin@fm333.com (Calvin) wrote in message news:<62843e96.0208200118.5e0f7207@posting.google.com>...
Calvin,
The 16bit Micro Focus COBOL systems came with a "DOS extender" named 
"XM.EXE". This program will run your existing programs in extended 
memory. You should find documentation in your COBOL System Reference 
Volume 2. Some experimentation may be required to get all the switches 
set corectly. The most recent versions (3.2, 3.4) are probably the 
most likely to work well with Microsoft's most recent versions of DOS.
-magee

> Hi there,
> 
…[19 more quoted lines elided]…
> Calvin
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2002-08-20T09:27:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0208200827.1d0b3532@posting.google.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
Hello Calvin,

You could consider using the segmentation facility, if your compiler
has it, or preferably subdivide your program into separately compiled
modules and use dynamic linkage with CALL/CANCEL, if that is an option
provided by your compiler and linkage editor.  In either case, your
program would have to be organised such that the amount of swapping in
and out is minimised and that its nature is appropriate to your task. 
Much better, if possible, is to design your solution to use smaller
programs by subdividing the component tasks differently.  There may be
techniques to use the high memory area, extended and expanded storage,
but I don't know them myself and you would have to read the compiler
documentation to see whether they are available and how to use them.

Regards, Robert

calvinchin@fm333.com (Calvin) wrote in message news:<62843e96.0208200118.5e0f7207@posting.google.com>...
> Hi there,
> 
…[19 more quoted lines elided]…
> Calvin
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-08-20T09:34:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0208200834.d10b715@posting.google.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
MF solved this problem long ago.  Use XM.


calvinchin@fm333.com (Calvin) wrote in message news:<62843e96.0208200118.5e0f7207@posting.google.com>...
> Hi there,
> 
…[19 more quoted lines elided]…
> Calvin
```

##### ↳ ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2002-08-20T19:07:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0208201807.6063d7c4@posting.google.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com> <bfdfc3e8.0208200834.d10b715@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote in message news:<bfdfc3e8.0208200834.d10b715@posting.google.com>...
> MF solved this problem long ago.  Use XM.

Hi Thane & Others,

Thank you very much for your suggestions. My mind is open and excited
with these ideas.

However, I look thru my COBOL package but couldn't find the XM.EXE
utility. I think some people has deleted it perviously and no more
backup of it. I would appreciate if you and others can help to email
the file to me. Pls send your file to calvinchin@ipmuda.com.my

Thank you very much.

Regards,
Calvin

> 
> 
…[22 more quoted lines elided]…
> > Calvin
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-20T17:46:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D628200.679FE9AE@shaw.ca>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```


Calvin wrote:

> Hi there,
>
…[14 more quoted lines elided]…
> memory?

Good old Patrick, (Micro Focus) jumped in and referred you to the XM
solution; similarly Thane said that was the solution. It can be but not
necessarily so

Let's go back to your statement, "Some of my programs are quite big....".
I hate that.
Starting with only 64K on a Radio Shack some 20 years ago I was a Nervous
Nellie about size. I always come back to this one, having toured a Weston
biscuit factory when I was a 17-year old kid in the RAF.

Making chocolate covered meringue biscuits :-

- Flour, sugar, powdered milk, lard etc., dumped into huge vats to mix
into pastry
- the above put through a series of heavy duty rollers, then rolling out
the pastry to a specific thickness.
- cookie cutters descended on the pastry, the residual dropping off at the
end of the conveyer belt
- cut cookies partially heated
- blob of jam
- blob of meringue
- coated with liquid chocolate
- partially re-cooked
- finished cookies slipped into packaging trays
- packages sealed

At any stage that process can go wrong - like the nozzle squirting the jam
gets gunged up. Although the process stops, the maintenance engineers can
zero in on the 'jam squirting process' - sub programming.

Programming is essentially the automation of human clerical processes.
Your BIG programs - are they 'all singing all dancing', referencing files,
performing calculations, printing reports. Can they be identified to
discrete processing units and be sub or called programs ?

Certainly one solution would be to hive off your files as separate called
programs. Do you have a copy of Micro Focus Mudemo.cbl (Mullet User demo)
which calls file programs - this illustrates how you can do this.

If you don't want to get involved in a major change then XM could well be
your current solution - but I still hate BIG ! The other problem with BIG
is that any innocent change in the source could trip you up all over the
place, elsewhere in the program. Business logic sub-divided into
sub-programs or calls allows you to test as discrete units, and going back
to your prime program, the change may affect sub G,
but subs A through F still retain their integrity.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-21T02:53:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhD89.120051$Yd.5311367@twister.austin.rr.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com> <3D628200.679FE9AE@shaw.ca>`

```
Big is not necessarily nor automatically bad. For example, a very small and simple program can have a BIG memory footprint, and with
good reasons. There is also a lot of be said for having all the parts of a program
in a small number of source files. The single biggest nuisance with Java (or even more so, Smalltalk) is the vast number of parts
and pieces scattered around. It makes it difficult to get a big picture.

Even IBM fell victim to that one - I think youcould not view an entire Java source file until VA Java 3.01 was released; you could
only part of the source file (i.e. a method or the class definition) at a time. Most hatefully annoying!
-Paul

"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:3D628200.679FE9AE@shaw.ca...
>
>
…[68 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-21T17:39:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D63D1D0.C48F5E58@shaw.ca>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com> <3D628200.679FE9AE@shaw.ca> <bhD89.120051$Yd.5311367@twister.austin.rr.com>`

```


Paul Raulerson wrote:

> Big is not necessarily nor automatically bad. For example, a very small and simple program can have a BIG memory footprint, and with
> good reasons. There is also a lot of be said for having all the parts of a program
> in a small number of source files. The single biggest nuisance with Java (or even more so, Smalltalk) is the vast number of parts
> and pieces scattered around. It makes it difficult to get a big picture.
>

Granted, and note I didn't make mention of OO, you did <G>. I appreciate what you are saying below, and even in an OO COBOL context it
makes sense to have a flowchart of an hierarchy to get where the peices,(classes) fit in - i.e., a hierarchy of what you've written, not
the vendor's support classes.

Jimmy

>
> Even IBM fell victim to that one - I think youcould not view an entire Java source file until VA Java 3.01 was released; you could
…[74 more quoted lines elided]…
> >
```

#### ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-20T12:44:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0208201144.c3a1876@posting.google.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com>`

```
calvinchin@fm333.com (Calvin) wrote 

> I have MF COBOL programs running under MS DOS. What I understand is
> that Micro Focus COBOL is using the base memory (640K) to run the
…[5 more quoted lines elided]…
> unable to load and giving errors.

There are several ways of improving the situation:

   1.  Use XM to allow use of several megabytes of memory

   2.  Compile with OPT"0" to create byte coded programs rather
       than generated code - approx 1/3rd code size.

   3.  Optimize CALL/CANCEL operation to keep maximum free space.

   4.  Use the RTS and build your systems as .INT/.GNT as the 
       RTS (chargable runtime) will shuffle memory.

   5.  Use overlays. In the largest programs reorganise the 
       program into SECTIONs that operate at different times
       and give them section 'priorities'.  eg 50 for code
       that only runs at initialisation, 51 for code that is
       only done at end of run, 52 for phase 1 processing, etc.

   6.  Replace SORTs with ISAM files. 

I have systems that total several megabytes of .EXE that will run in
600Kb or less.

If sounds like (due to "I have running .." and "at the end,..") that
you have a system structure that does CALL/CANCEL to run various parts
of the system and this eventually runs out of memory.

CALL works by filename but CANCEL works by PROGRAM-ID.  If the
identity is not the same as the filename then the CANCEL will not
work.  This will eventually lead to running out of memory.

If there is a hierarchy of CALLing then ensure that CANCELs are done
as the hierarchy collapses to retain maximum contiguous memory.  If
there are called routines that are to remain during several successive
programs then add dummy CALLs to load these into memory early rather
then have them lodge in memory.

The basic structure that I use is a very small control program which
basically sits in a loop doing CALL/CANCEL of whatever some other
program tells it to. This starts with the name of the menu program to
start off with.  Before it CALLs this it does a DISPLAY..AT to load
the ADIS.EXE module, oepns a dummy ISAM file to load the EXTFH.EXE
module and dummy CALLs a control routine which stays in memory for the
whole run.  The idea is that these load into lower area of the 600Kb
leaving one contiguous area for application programs to be
CALL/CANCELed.

With Overlays you need to be careful about the structure of the system
and common routines performed from several overlays need to be in the
permanent part of the program, but if the program progresses through
several phases or has several sections that are executed at different
times depending on user control then it can reduce the run size
enormously.

> I have to separate those BIG programs into few smaller programs. But
> the processing will be a bit slower and less efficient.

This may or may not help if the smaller programs still have to be
loaded into memory by CALLing each other.
```

##### ↳ ↳ Re: Effective use of DOS base memory for COBOL programs

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-08-20T22:56:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UOz89.3625$yt3.1497572@newssrv26.news.prodigy.com>`
- **References:** `<62843e96.0208200118.5e0f7207@posting.google.com> <217e491a.0208201144.c3a1876@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0208201144.c3a1876@posting.google.com...
>
> There are several ways of improving the situation...
>    1.  Use XM to allow use of several megabytes of memory
>  [snipped]

I know next to nothing about shrinking the memory footprint using MFCobol,
but that was the most lucid and enlightening post I have read here in some
time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
