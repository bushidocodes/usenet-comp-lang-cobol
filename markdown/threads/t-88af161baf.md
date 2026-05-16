[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I ran into a problem with a copybook

_7 messages · 4 participants · 2000-05_

---

### I ran into a problem with a copybook

- **From:** "tom" <news@news.com>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p75Q4.75$%w.641@news.swbell.net>`

```
Today I was modifying a copybook on a record that had a header and some
details.  In the header I was using an occurs depending on clause for a
certain field, and the details amount was controlled by a occurs depending
on clause.
This all ran fine.   However when I tried to add an occurs depending on
clause WITHIN each of the details, I found I could no longer use file-aid to
read the file.  If I removed the depending on clause and allowed a static
inclusion in the fields everything was fine.  Is this a rule I am violating
or is this a function of the compiler.  I am on an IBM OS390 mainframe.

Thanks
TOm
```

#### ↳ Re: I ran into a problem with a copybook

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2DbQ4.20763$0o4.190401@iad-read.news.verio.net>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net>`

```
In article <p75Q4.75$%w.641@news.swbell.net>, tom <news@news.com> wrote:

[snippage]

>This all ran fine.   However when I tried to add an occurs depending on
>clause WITHIN each of the details, I found I could no longer use file-aid to
>read the file.  If I removed the depending on clause and allowed a static
>inclusion in the fields everything was fine.  Is this a rule I am violating
>or is this a function of the compiler.  I am on an IBM OS390 mainframe.

This sounds like a FileAid problem and more information might be
helpful.  When you say that you couldn't 'read the file' are you saying
that FileAid couldn't *open* the file at all... or that you had trouble
with the formatted displaying of the file?

DD
```

##### ↳ ↳ Re: I ran into a problem with a copybook

- **From:** "tom" <news@news.com>
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2odQ4.95$%w.5110@news.swbell.net>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net> <2DbQ4.20763$0o4.190401@iad-read.news.verio.net>`

```

<docdwarf@clark.net> wrote in message news:2DbQ4.20763>
> [snippage]
>
> >This all ran fine.   However when I tried to add an occurs depending on
> >clause WITHIN each of the details, I found I could no longer use file-aid
to
> >read the file.  If I removed the depending on clause and allowed a static
> >inclusion in the fields everything was fine.  Is this a rule I am
violating
> >or is this a function of the compiler.  I am on an IBM OS390 mainframe.
>
…[4 more quoted lines elided]…
>
File aid wouldnt open the file though before i made the changes to the
copybook it did just fine.  It reported an error and showed a screen I had
never seen before.
```

###### ↳ ↳ ↳ Re: I ran into a problem with a copybook

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7yfQ4.20803$0o4.191443@iad-read.news.verio.net>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net> <2DbQ4.20763$0o4.190401@iad-read.news.verio.net> <2odQ4.95$%w.5110@news.swbell.net>`

```
In article <2odQ4.95$%w.5110@news.swbell.net>, tom <news@news.com> wrote:
>
><docdwarf@clark.net> wrote in message news:2DbQ4.20763>
…[15 more quoted lines elided]…
>never seen before.

Hmmmmm... sounds more and more like a FileAid problem.  Try the simplest
invocation, something like:

--begin screenprint

Browse Mode                 ===> C         
                                           
Specify Browse Information:                
   Browse dataset name      ===> 'YOUR.FILENAME.HERE'
   Member name              ===>           
   Volume serial            ===>           
                                           
                                           
Specify Record Layout and XREF Information:
   Record layout usage      ===> N         
   Record layout dataset    ===>           
   Member name              ===>           
   XREF dataset name        ===>           
   Member name              ===>           
                                           
Specify Selection Criteria Information:    
   Selection criteria usage ===> N         
   Selection dataset name   ===>           
   Member name              ===>           
                                           
--end screenprint

... and see if it chokes.  If you get into a basic Browse that way then
you might try a slightly more intricate invocation; I would suggest making
a separate PDS member containing just the 01 level that is causing you
problems (no multiple record-layouts) and then trying:

--begin screenprint

Browse Mode                 ===> C         
                                           
Specify Browse Information:                
   Browse dataset name      ===> 'YOUR.FILENAME.HERE'
   Member name              ===>           
   Volume serial            ===>           
                                           
                                           
Specify Record Layout and XREF Information:
   Record layout usage      ===> S
   Record layout dataset    ===> 'YOUR.PDS.HERE'
   Member name              ===> MEMBRNAM
   XREF dataset name        ===>           
   Member name              ===>           
                                           
Specify Selection Criteria Information:    
   Selection criteria usage ===> N         
   Selection dataset name   ===>           
   Member name              ===>           
                                           
--end screenprint

... and this sshould bring you back into the unformatted Browse as
before.  Once in the Browse issue the line command of FMT and see how it
'gacks'.

DD
```

#### ↳ Re: I ran into a problem with a copybook

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f96cv$kec$1@slb0.atl.mindspring.net>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net>`

```
Just because it might be missed by some,

Having nested ODOs (OCCURS DEPENDING ON) is an EXTENSION which IBM mainframe
COBOLs support (and have for MANY a year).  This is not a "valid"
(conforming) structure for most COBOLs - but IBM allows/supports it.

Now for the file-aid issue:

1) are the "objects of the ODO" (the thing that is pointed to by the OCCURS
DEPENDING ON) all in the "fixed" portion of the record?  For the nested ODO,
is the object of the ODO also under the "top" ODO?  The answers to this may
impact what is happening (or whether or not this is supported)

2)  One of your notes mentions a "new error screen".  Can you tell us exactly
what it says - this may give us a clue to a solution or at least a
circumvention.

3) Have you contacted Compuware support?
```

##### ↳ ↳ Re: I ran into a problem with a copybook

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fapsu$coj$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net> <8f96cv$kec$1@slb0.atl.mindspring.net>`

```
    I personally feel that the occurs depending on can easily be
the equivalent of buying trouble.

    I suppose that depends on whether you (and the compiler
writer) look at ODO as
a simple stop sign, or as a method to change the true length of
the array.

    To be truly usefull with memory allocation, it should be
possible to allocate ONLY enough
memory to cover the ODO length, NOT the maximum.

    Hence the problems with data names after the variable length
item.

    Note to confused - see Microfocus documentation for
"ODOSLIDE" for more
information.  I assume (hope?) that other cobols have a similar
option.

    While we are at it, please try to get them to at least issue
a compile warning
when someone uses initialize on an ODO item with ODOSLIDE active.
Better
yet, make it work.



William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8f96cv$kec$1@slb0.atl.mindspring.net...
> Just because it might be missed by some,
>
> Having nested ODOs (OCCURS DEPENDING ON) is an EXTENSION which
IBM mainframe
> COBOLs support (and have for MANY a year).  This is not a
"valid"
> (conforming) structure for most COBOLs - but IBM
allows/supports it.
>
> Now for the file-aid issue:
>
> 1) are the "objects of the ODO" (the thing that is pointed to
by the OCCURS
> DEPENDING ON) all in the "fixed" portion of the record?  For
the nested ODO,
> is the object of the ODO also under the "top" ODO?  The answers
to this may
> impact what is happening (or whether or not this is supported)
>
> 2)  One of your notes mentions a "new error screen".  Can you
tell us exactly
> what it says - this may give us a clue to a solution or at
least a
> circumvention.
>
…[7 more quoted lines elided]…
> > Today I was modifying a copybook on a record that had a
header and some
> > details.  In the header I was using an occurs depending on
clause for a
> > certain field, and the details amount was controlled by a
occurs depending
> > on clause.
> > This all ran fine.   However when I tried to add an occurs
depending on
> > clause WITHIN each of the details, I found I could no longer
use file-aid
> to
> > read the file.  If I removed the depending on clause and
allowed a static
> > inclusion in the fields everything was fine.  Is this a rule
I am violating
> > or is this a function of the compiler.  I am on an IBM OS390
mainframe.
> >
> > Thanks
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: I ran into a problem with a copybook

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fb9c2$e5$1@slb7.atl.mindspring.net>`
- **References:** `<p75Q4.75$%w.641@news.swbell.net> <8f96cv$kec$1@slb0.atl.mindspring.net> <8fapsu$coj$1@ssauraaa-i-1.production.compuserve.com>`

```
So everyone (including Russell) understands, the ANSI Standard (current,
past, and future) is *incredibly* clear that an ODO absolutely, POSITIVELY,
does not impact memory allocation.  It only impacts the number of elements
that are currently "available".

Furthermore, the '68 ANSI Standard did allow nested ODOs - but didn't define
how they worked (exactly).  Since then ('74 Standard and later), the use of
nested ODOs (including ODOs subordinate to a fixed OCCURS clause) are
strictly non-Standard.  The reason that this is true is that are some
definite problems in "defining" how these should work.  IBM continues to
support this (along with ODOs that are not the last group in/under another
record/group).  Many implementors (including MERANT with ODOSLIDE) provide a
method of matching the IBM behavior, but this (as with INITIALIZE) can still
lead to LOTS of problems.

P.S.  I am WELL aware that for "existing" databases (flat files or
otherwise), there may be no choice but to use this "feature" if that is the
way it was originally created.  Having said this, I hope no NEW
files/databases are created this way - and that "old" ones are being changed
not to depend on this - as they files themselves get upgraded.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
