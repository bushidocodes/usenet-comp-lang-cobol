[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# prettyCBL - was Variable Length Records

_8 messages · 6 participants · 1999-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### RE: prettyCBL - was Variable Length Records

- **From:** Peter van Zeeland <peter.van.zeeland@cmg.nl>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01>`

```
> >         Line numbers are as obsolete as the program's red tape (author,
> > date-written, date-compiled, remarks, security)
…[5 more quoted lines elided]…
> 
	Kidding, are you?
	Can YOU ever hold the author of a program responsible for anything ?
	What does the date a program was written (once, long, long ago) tell
YOU today ?

>  I suppose you have a violent objection to modcodes in cc 73-80, too.
> 
	Quite right.
	Not only does it destroy the visual appearance of a program, it also
is rather troublesome to preserve when modifications are modified
themselves. Version control (which I can do without) is a much better
solution.

> > 
> >         And while I'm at it: incrementing data item level numbers by 2
…[4 more quoted lines elided]…
> 
	01  DATA-ITEM.
	     05  SUB-ITEM.
	           10 SUB-SUB-ITEM.
	                15 ETCETERA   PIC X.

	That's when I say  "huh?"  too !!






 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

#### ↳ Re: prettyCBL - was Variable Length Records

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pukv8$g7d@dfw-ixnews4.ix.netcom.com>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01>`

```
Peter van Zeeland <peter.van.zeeland@cmg.nl> wrote in message
news:6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01...
 <snip>
>
> > >
…[13 more quoted lines elided]…
>

Peter,
  Although I think your environment isn't everyone's environment, I can
understand why you don't like (and/or don't use) sequence numbers.  HOWEVER,
I don't understand your point on incrementing level numbers.  Are you saying
that you SHOULD use "1, 5, 10, 15" instead of "1, 3, 5, 7" - or that COBOL
should (somehow?) figure out relationships in a group without any level
numbers or something else?  I (fully) agree that ANY "incrementing" value is
purely aribtrary - and totally depends on how much "maintenance" you expect
(requiring you to "insert" intermediate levels) - or whether you like
renumbering levels each time you do maintenance.  However, I don't see any
way to support COBOL's view of levels and redefinitions without SOME form of
level numbers.

(P.S.  Related to another part of this thread, the "INSERT" "DELETE" and
"REPLACE" *verbs* are indeed COBOL "verbs" with IBM mainframe compilers.  I
assume from your note, that you were mistaking them for something else - but
they are very definitely a current part of the COBOL language - in one of
its "dialects".)
```

##### ↳ ↳ Re: prettyCBL - was Variable Length Records

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c33992@news3.us.ibm.net>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com>
> Peter van Zeeland <peter.van.zeeland@cmg.nl> > > 01  DATA-ITEM.
> >      05  SUB-ITEM.
…[4 more quoted lines elided]…
> understand why you don't like (and/or don't use) sequence numbers.
HOWEVER,
> I don't understand your point on incrementing level numbers.  Are you
saying
> that you SHOULD use "1, 5, 10, 15" instead of "1, 3, 5, 7"

no, no, and no again: the proper sequence is 1, 2, 3, 4,...

In the olden days when people did not indent programs, the argument was
that with 1, 5, 10, ...  you could insert intermediate levels. With
indentation
you cannot anymore without changing the indentation and then you can
as well change the level numbers.
```

###### ↳ ↳ ↳ Re: prettyCBL - was Variable Length Records

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C3EBF6.367F3152@zip.com.au>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com> <37c33992@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
> 
> no, no, and no again: the proper sequence is 1, 2, 3, 4,...
…[4 more quoted lines elided]…
> and then you can as well change the level numbers.

The reason to increment 1,5,10 is to allow you to insert groups into
the definition later without a major resequence.

for example a fist attempt:

01  fred-struct.
  02  dd-fred pic...
  02  mm-fred...
  02  yyyy-fred....
  02  a-string-in-fred
  02 something-else-in-fred.

in order to insert a group on the dd,mm,yyyy field you need to
increment the counters on these fields.  Ok for this example but I
have had to group keys and data after the event on programs with a
very large number of fields.

Ken
```

###### ↳ ↳ ↳ Re: prettyCBL - was Variable Length Records

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C3F32F.FCD6441F@NOSPAMhome.com>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com> <37c33992@news3.us.ibm.net>`

```
Leif Svalgaard wrote:

> no, no, and no again: the proper sequence is 1, 2, 3, 4,...
> 
…[4 more quoted lines elided]…
> as well change the level numbers.

My first COBOL program was written in 1969, and this was after that time
- we indented.  If we wanted to insert an intermediate level, we
indented 2 instead of 4.

At any rate, is there some cost savings in going 1, 2, 3, 4,... insted
of 01, 05, 10, 15?

Oh, I never use single character numbers for suffixes.  I tend to think
of global changes and sorts.   If I change DEBUG-1 to DEBUG-7, it will
change DEBUG-10 to DEBUG-70.  DEBUG-01 is free (now that I am not
dependent upon teletyping speeds).
```

###### ↳ ↳ ↳ Re: prettyCBL - was Variable Length Records

_(reply depth: 4)_

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itTw3.110$wv2.7621@axe.netdoor.com>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com> <37c33992@news3.us.ibm.net> <37C3F32F.FCD6441F@NOSPAMhome.com>`

```
Back in the punched card days, leaving gaps in the level numbers made sense
if it was necessary to add a new level between existing ones.  With punched
cards now in museums and serving as bookmarks,  someone can add a new level
number between contiguous ones with a few thought out substitutions with
their editor.

Howard Brazee wrote in message <37C3F32F.FCD6441F@NOSPAMhome.com>...
>Leif Svalgaard wrote:
>
…[13 more quoted lines elided]…
>of 01, 05, 10, 15?
```

###### ↳ ↳ ↳ Re: prettyCBL - was Variable Length Records

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C40BEE.508CF4C5@NOSPAMhome.com>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com> <37c33992@news3.us.ibm.net> <37C3F32F.FCD6441F@NOSPAMhome.com> <itTw3.110$wv2.7621@axe.netdoor.com>`

```
OK.  So the advantage of skipping levels has decreased.   What is the
advantage of not skipping levels?

Warren Porter wrote:
> 
> Back in the punched card days, leaving gaps in the level numbers made sense
…[21 more quoted lines elided]…
> >of 01, 05, 10, 15?
```

###### ↳ ↳ ↳ Re: prettyCBL - was Variable Length Records

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c48984@news3.us.ibm.net>`
- **References:** `<6DE2D20B5851D2119BB300A0C9DAF69845042B@NL-AMB-MAIL01> <7pukv8$g7d@dfw-ixnews4.ix.netcom.com> <37c33992@news3.us.ibm.net> <37C3F32F.FCD6441F@NOSPAMhome.com>`

```
> At any rate, is there some cost savings in going 1, 2, 3, 4,... insted
> of 01, 05, 10, 15?
>
> Oh, I never use single character numbers for suffixes


I agree with you. Mea culpa, I should have used 01, 02, 03, 04...
There is no savings with  straight 01, 02, 03,,, but then there is
no cost either. It just seems simpler to have something at level
4 also being designated as being at 04. Programming is hard
as it is. Good rule: call things what they are.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
