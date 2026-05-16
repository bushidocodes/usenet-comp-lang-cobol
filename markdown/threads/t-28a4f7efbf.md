[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Incorrect data-name in REDEFINES clause

_8 messages · 4 participants · 1998-08 → 1998-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Incorrect data-name in REDEFINES clause

- **From:** jraben19@mail.idt.net (Jeff Raben)
- **Date:** 1998-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35e85cf3.1544545@news.idt.net>`
- **References:** `<35df03f8.20027739@netnews.worldnet.att.net>`

```
Vern_Bradner@newcourt.com (Vern Bradner) wrote:

>Hi,
>
…[13 more quoted lines elided]…
>
1) 01 levels are never redefined under an FD/SD

2) WORKING-STORAGE has nothing to do with a file / record except at a
READ.... INTO...
They are in 2 different "address spaces" in particular in most COBOL's
the 01 record area is acquired dynamically.

JR
and stir with a Runcible spoon...
```

#### ↳ Re: Incorrect data-name in REDEFINES cla

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298241.69907.15830@kcbbs.gen.nz>`
- **References:** `<35e85cf3.1544545@news.idt.net>`

```
In message <<35e85cf3.1544545@news.idt.net>> jraben19@mail.idt.net  writes:
> >
> 1) 01 levels are never redefined under an FD/SD

They can be, they may be, they don't need to be.

> 
> 2) WORKING-STORAGE has nothing to do with a file / record except at a
> READ.... INTO...
> They are in 2 different "address spaces" in particular in most COBOL's
> the 01 record area is acquired dynamically.

Regardless of whether the record area is statically created
or dynamically created it must always behave in a valid
way.  The implication of being 'acquired dynamically' is
that sometimes (such as prior to OPEN or after CLOSE or
END) it does not exist.  I do not believe that a record
area that is non-existant during part of a program run
would match the expected behaviour of standard Cobol.
```

##### ↳ ↳ Re: Incorrect data-name in REDEFINES cla

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6scnt7$lfj@dfw-ixnews9.ix.netcom.com>`
- **References:** `<35e85cf3.1544545@news.idt.net> <3298241.69907.15830@kcbbs.gen.nz>`

```

Richard Plinston wrote in message <3298241.69907.15830@kcbbs.gen.nz>...
>In message <<35e85cf3.1544545@news.idt.net>> jraben19@mail.idt.net  writes:
>> >
>> 1) 01 levels are never redefined under an FD/SD
>
>They can be, they may be, they don't need to be.
   No, not in a Standard COBOL program.  A REDEFINES at the 01-level is
ILLEGAL in Standard COBOL (but allowed as an extension in others - this was
actually a major migration headache for IBM environment programmers going
from OS/VS COBOL to VS COBOL II - the former allowed in and the latter does
not)

>
>>
…[12 more quoted lines elided]…
>

Guess again.
   The Standard is quite clear that not only are the contents of the Record
area undefined before an OPEN or after a CLOSE - but even attempting to
access them is "unpredictable".  Many current compilers will cause run-time
termination (usually abnormal) if you try this.
```

##### ↳ ↳ File Record Areas (was Re: Incorrect data-name in REDEFINES cla)

- **From:** Lookin'@You.2 (WDS)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f816f7.3244969@news1.frb.gov>`
- **References:** `<35e85cf3.1544545@news.idt.net> <3298241.69907.15830@kcbbs.gen.nz>`

```
On 30 Aug 98 19:25:07 GMT, riplin@kcbbs.gen.nz (Richard Plinston)
wrote:

>Regardless of whether the record area is statically created
>or dynamically created it must always behave in a valid
…[5 more quoted lines elided]…
>
In many implementations, the record area is undefined prior to a
file's OPEN and after its CLOSE.  Sometimes, the record area is also
undefined or unavailable prior to a READ of a file opened INPUT or
after a WRITE of a file opened OUTPUT.  This, however, is usually not
true (the record area *is* available) if the file is opened I-O or if
the file is referenced in a SAME RECORD AREA clause in the I-O-CONTROL
paragraph.

The exact behavior varies.  In some implementations, referencing this
undefined area will produce undefined/invalid results; in others it
will result in program termination for attempting to acceess memory
space that does not exist or that does not belong to the program.

In still other implementations, the behavior will appear to work as
though the record area is always available, as long as the file is
unblocked (or blocked 1) and there are no other buffers (ALTERNATE
AREAS) in use for the file.  In implementations like this, especially
if file blocking and buffering can be specified externally to the
program (such as via external file assignments, JCL, etc.),
unpredictable program behavior can result.  The program may work
correctly for some runs and it may give strange results in other runs
(such as properly processing only one record in each block).  Such
problems can be difficult to track down.

There are some implementations where file record areas are always
available and always accessible to the running program.  In these
implementations, they behave similarly to records defined in
WORKING-STORAGE, except that they are also tied to the files (so they
behave properly in READ, WRITE, etc.)

While I am not as well versed in the published COBOL standards as
perhaps I should be, I do not believe that any of this is contrary to
the expected behavior of standard COBOL.  Usually, the reference
manual for a given COBOL implementation will describe the specifics of
files' record areas and their accessibility.  If, however, you want to
be sure that your code is portable (of if you just want to play it
safe), then don't access the record area before a file is opened,
after it is closed, before a read, after a write, etc.  One solution
to this is to use READ...INTO and WRITE...FROM.
```

###### ↳ ↳ ↳ Re: File Record Areas (was Re: Incorrect data-name in REDEFINES cla)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ta0qp$gh0@dfw-ixnews6.ix.netcom.com>`
- **References:** `<35e85cf3.1544545@news.idt.net> <3298241.69907.15830@kcbbs.gen.nz> <35f816f7.3244969@news1.frb.gov>`

```
I agree with most of the following with one very minor modification.

There ARE actually some rules in the Standard about the record area being
"defined" before an OPEN or after a CLOSE if the SAME AREA clause is used.
At one time, I understood these rules, but as I never use the clause, I
can't tell you exactly what they are.

WDS wrote in message <35f816f7.3244969@news1.frb.gov>...
>On 30 Aug 98 19:25:07 GMT, riplin@kcbbs.gen.nz (Richard Plinston)
>wrote:
…[52 more quoted lines elided]…
>-------------------Decoy@Spammer.Trasher----------------
```

###### ↳ ↳ ↳ Re: File Record Areas (was Re: Incorrect dat

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.71720.26703@kcbbs.gen.nz>`
- **References:** `<35f816f7.3244969@news1.frb.gov>`

```
In message <<35f816f7.3244969@news1.frb.gov>> Lookin'@You.2  writes:
> >
> In many implementations, the record area is undefined prior to a
> file's OPEN and after its CLOSE.  Sometimes, the record area is also

Being undefined means that the value of the content should be
treated as unknowable.  It is also undefined after a WRITE
or REWRITE, ie you should not rely on the record area still
holding the record you just set up.

> undefined or unavailable prior to a READ of a file opened INPUT or
> after a WRITE of a file opened OUTPUT.  This, however, is usually not

If you mean by 'unavailable' that the record area cannot be
accessed then you are simply wrong for any valid COBOL.

These sequences should always be valid in COBOL, the
implication of your statement is that there would be a
failure:

 1)
         OPEN INPUT File
         MOVE Start-Key to File-Key
         START File KEY > File-Key

 2)       WRITE File-Record
          MOVE New-Data   TO File-Record

If your assertion that it is 'unavailable' then these would
cause a failure.  This is sufficient to show that the
implementation is _not_ Cobol.

> true (the record area *is* available) if the file is opened I-O or if
> the file is referenced in a SAME RECORD AREA clause in the I-O-CONTROL
> paragraph.

SAME RECORD AREA should simply remap the record areas to the 
same location in memory, similar to a redefines.  This has
implications about when it becomes undefined (in _content_)
but not about its availability.

> 
> The exact behavior varies.  In some implementations, referencing this
> undefined area will produce undefined/invalid results; in others it
> will result in program termination for attempting to acceess memory
> space that does not exist or that does not belong to the program.

Please indicate specifically which implementations exhibit
any of these behaviours and yet still claim to be Cobol.
It sounds like folklore to me.

> 
> In still other implementations, the behavior will appear to work as
…[8 more quoted lines elided]…
> problems can be difficult to track down.

Sounds broken to me, but then it may be a useful excuse for
programmers to use when they can't get their programs
working correctly.

> 
> There are some implementations where file record areas are always
…[3 more quoted lines elided]…
> behave properly in READ, WRITE, etc.)

And these are called 'COBOL'.

> 
> While I am not as well versed in the published COBOL standards as
…[7 more quoted lines elided]…
> to this is to use READ...INTO and WRITE...FROM.

Rubbish.  There is never any reason for Cobol to need INTO 
or FROM (I understand it does make some core dumps easier
to work with, if you need core dumps).  In fact the WRITE
FROM should behave _exactly_ as if you had coded a MOVE
and the a WRITE, ie:

        MOVE WS-Record    TO File-Record
        WRITE File-Record

is _exactly_ the same as:

        WRITE File-Record FROM WS-Record

As the two bits of code are exactly exchangable to idea
that one makes a record area available in some way and
the other may cause a failure simply shows that it is
not COBOL.

Or, perhaps, that you have simply collected the last few
decades worth of lame programmer excuses for failing to be
able to write working programs.
```

###### ↳ ↳ ↳ Re: File Record Areas (was Re: Incorrect dat

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tc7ep$gb8@dfw-ixnews3.ix.netcom.com>`
- **References:** `<35f816f7.3244969@news1.frb.gov> <3298253.71720.26703@kcbbs.gen.nz>`

```

Richard Plinston wrote in message
   <snip>
>
>If your assertion that it is 'unavailable' then these would
>cause a failure.  This is sufficient to show that the
>implementation is _not_ Cobol.
>
 <more snip>

If you are saying that the record area (the 01-level under an FD) is
required to be "available" (i.e. you can move things from or to it) before
the first OPEN or after the last CLOSE, then please point me to where in the
Standard this is required.  I know of a number of compilers that will cause
an abnormal termination if you try this (and will provide names and releases
AFTER you tell me where in the Standard this might be required).

After a WRITE (after a successful OPEN), then I believe that you are correct
that the record area must be available - but its contents are unpredictable.
(Certainly, after a successful READ the contents are well defined.)
```

###### ↳ ↳ ↳ IBM mainframe COBOL file buffers in CEEDUMP

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tkh0p$daj$1@garnet.nbnet.nb.ca>`
- **References:** `<6ta0qp$gh0@dfw-ixnews6.ix.netcom.com> <35e85cf3.1544545@news.idt.net> <3298241.69907.15830@kcbbs.gen.nz> <35f816f7.3244969@news1.frb.gov>`

```
I can find the file information block (FIB) in the CEEDUMP (Language   
Environment Dump dataset) listing but I haven't been able to find the current   
record for the file in the dump.  Since the read/write area for a file is   
always addressable while the file is open (the contents are undefined before   
first read and after every write), it should be available in the dump.  I am   
using COBOL for MVS and VM 1.2.  Are the current record areas for all OPEN   
files available in the dump?  Are the buffers for all OPEN files available?   
the  
 
As a side note the behaviour after end of file on a READ changed with the 85   
COBOL's (VS COBOL II and COBOL for this and that) so that the record area is   
still addressable.   
 

Clark F. Morris, Jr. 
CFM Technical Programming Services 
Bridgetown, Nova Scotia, Canada 
cmorris@fox.nstn.ca 
on assignment at morrisc@nbnet.nb.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
