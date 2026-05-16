[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reentrant Cobol from TSO Call - Is it possible?

_5 messages · 4 participants · 2000-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Reentrant Cobol from TSO Call - Is it possible?

- **From:** Jeremy Coast <Jeremy.Coast@bt.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E0E14E.9E4377A0@bt.com>`

```
Does anyone know the answer?

I am calling a cobol program from a Clist. I cannot find a way to make
it reentrant,
as it wants to perform the initialization routines every time.

RENT and RESIDENT are default compile options but makes no difference.

I have trawled through various manuals but cannot find anything that
says whether it
is even possible or not possible.

Thanking you in advance for your time.
Regards,
```

#### ↳ Re: Reentrant Cobol from TSO Call - Is it possible?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8br4cq$vna$1@slb6.atl.mindspring.net>`
- **References:** `<38E0E14E.9E4377A0@bt.com>`

```
It really isn't a question of reentrant or not - it is a question of "last
used state".

It may not fit into your environment but IF you placed a COBOL "stub" program
at the top and have *it* invoke the CLIST (which in turn calls your "real"
code) - you will find that re-initialization does NOT occur.

Your current "design" has COBOL build and "destroy" the COBOL environment
each time the program is called.

NOTE:
  If you were calling your routine from another programming language - not a
CLIST - then you could use ILBOSTP0 or IGZERRE (to keep the COBOL environment
active) - but I don't think those will work from a CLIST.
```

##### ↳ ↳ Re: Reentrant Cobol from TSO Call - Is it possible?

- **From:** "Searcher" <mangogwr@bellsouth.net>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LddE4.2703$4T2.497@news4.mia>`
- **References:** `<38E0E14E.9E4377A0@bt.com> <8br4cq$vna$1@slb6.atl.mindspring.net>`

```
You can't find what doesn't exist.

A CLIST can't 'CALL' a non-clist module.
Even though you code it 'call "IEBGENER" ...'
It doesn't set up a 'true call'  instead, since TSO knows
this isn't a CLIST procedure, it invokes TSOEXEC to EXEC PGM=.

Even the 'exits' / 'subroutines' that can be coded in COBOL / PLI /
Fortran or Assembler for ISPF are not 'Subroutines' rather they are
executed by the standard LOAD PGM SVC and perform CALLS
to obtain data.

Whenever a COBOL progra runs, there must be a linkage established
to the Runtime Routines AND, the program's data only EXISTS WITHIN
THE CONTEXT OF THAT RUN-UNIT.  RUN-UNIT means LINK-EDITED
NON-INTERPRETED MODULE.

If you are wanting data to remain in a particular state, the best thing is
to have
a process like we use in CICS.

Have the Clist delete (if exists) and then create a sequential file for
initial data.
The program upon execution reads the file and if that FAILS, performs
INITIALIZATION, if the read was OK, then no init is done, instead, move a
large
work-area to WORKING-STORAGE  '01 ITEM'.  Just prior to STOP RUN / GOBACK
MOVE the 01 ITEM to Record area and write file.


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:8br4cq$vna$1@slb6.atl.mindspring.net...
> It really isn't a question of reentrant or not - it is a question of "last
> used state".
>
> It may not fit into your environment but IF you placed a COBOL "stub"
program
> at the top and have *it* invoke the CLIST (which in turn calls your "real"
> code) - you will find that re-initialization does NOT occur.
…[5 more quoted lines elided]…
>   If you were calling your routine from another programming language - not
a
> CLIST - then you could use ILBOSTP0 or IGZERRE (to keep the COBOL
environment
> active) - but I don't think those will work from a CLIST.
>
…[21 more quoted lines elided]…
>
```

#### ↳ Re: Reentrant Cobol from TSO Call - Is it possible?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E203FA.A5C13342@zip.com.au>`
- **References:** `<38E0E14E.9E4377A0@bt.com>`

```
Jeremy Coast wrote:
> 
> Does anyone know the answer?
…[4 more quoted lines elided]…
> 

Why are you using Clist?  You can use ISPLINK instead of ISPEXEC for
display stuff and you will not have the problem then.

You might need a starter clist that calls the main cobol program but
it would be very short.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Reentrant Cobol from TSO Call - Is it possible?

- **From:** Jeremy Coast <Jeremy.Coast@bt.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E32770.45454CBD@bt.com>`
- **References:** `<38E0E14E.9E4377A0@bt.com> <38E203FA.A5C13342@zip.com.au>`

```
Whoosh!

I'm sorry Ken, that one passed me right by.

Regards,

Ken Foskey wrote:

> Jeremy Coast wrote:
> >
…[15 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
