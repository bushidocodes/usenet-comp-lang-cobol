[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# General purpose subroutines

_13 messages · 8 participants · 2000-06_

---

### General purpose subroutines

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393D227D.53E06EF5@cusys.edu>`

```
I have had to remove general purpose subroutine calls from programs to
make more efficient routines directly in the programs.

Do OO programmers have similar needs?
```

#### ↳ Re: General purpose subroutines

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393E2EC6.B6BCBCCC@istar.ca>`
- **References:** `<393D227D.53E06EF5@cusys.edu>`

```
As a follow-on, would the answer be different for separately compiled OO
routines than for OO routines that are included at compile time?  Also
how much of the saving comes from having a specific routine that just
deals with the data rather than a general routine that needs information
on what to do with the data.  An instance of the former would be a
routine that just converts a yyyyddd date to a yyyymmdd date as opposed
to a general purpose date conversion routine that converts dates from
and to various formats?

Is it more efficient in terms of maintenance and documentation to have a
large number of specific purpose routines or objects rather than a much
smaller number of general purpose routines or objects?

CLark Morris, CFM Technical Programming Services Inc. cfmtech@istar.ca  

Howard Brazee wrote:
> 
> I have had to remove general purpose subroutine calls from programs to
> make more efficient routines directly in the programs.
> 
> Do OO programmers have similar needs?
```

##### ↳ ↳ Re: General purpose subroutines

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hlfam$1co1$2@news.hitter.net>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E2EC6.B6BCBCCC@istar.ca>`

```

Clark F. Morris, Jr. wrote in message <393E2EC6.B6BCBCCC@istar.ca>...
>As a follow-on, would the answer be different for separately compiled OO
>routines than for OO routines that are included at compile time?

In theory, this is no difference in performance for separately compiled
methods.

>  Also
>how much of the saving comes from having a specific routine that just
…[4 more quoted lines elided]…
>and to various formats?

As usual, it depends upon the ratio of the execution time for
overhead to the execution time of the individual procedures.
The execution time for overhead includes any data conversion
or movement required to conform to the interface for the call
as well as the time required to begin executing the appopriate
code.

>Is it more efficient in terms of maintenance and documentation to have a
>large number of specific purpose routines or objects rather than a much
>smaller number of general purpose routines or objects?

It depends a great deal on how each is described. It also
depends upon the abilities and experience of the individual
performing the maintenance.

Well-defined copybooks that fully document the interfaces
to general-purpose subroutines are difficult to beat for ease
of maintenance.

An individual who is familiar and comfortable with a collection
of commonly-used and well-named specific-purpose routines
will have little difficulty. OO falls into this category. Those not
comfortable with specific-purpose routines will likely be
uncomfortable with OO and its myriad of methods.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: General purpose subroutines

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393E8F5A.8E632ECD@cusys.edu>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E2EC6.B6BCBCCC@istar.ca> <8hlfam$1co1$2@news.hitter.net>`

```
Rick Smith wrote:
> 
> Well-defined copybooks that fully document the interfaces
> to general-purpose subroutines are difficult to beat for ease
> of maintenance.

Everything's a trade off.  A single record description matching a single
file is nice to have when you are using that file with many programs. 
But the temptation is to increase the copy books with modules which are
used all over the place.  Even without OO, this creates dependencies
which increase the maintenance task and vulnerability.  In enterprise
shops I have seen people write virtually duplicate programs so that one
could be changed without going through the approval process, multiple
unit testing, system testing, and acceptance testing involved when that
module or program is used by more than one user.

Shared modules are somewhat like central governments.  They can be
efficient  when they work right.  They can be costly when they fail, and
the bureaucratic overhead of making changes can be almost as costly. 
Isolated modules may have greater total costs, but they can fail, be
changed, or thrown out without messing up anybody else.  Cheaply.
```

###### ↳ ↳ ↳ Re: General purpose subroutines

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hmfro$apv$1@news.igs.net>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E2EC6.B6BCBCCC@istar.ca> <8hlfam$1co1$2@news.hitter.net> <393E8F5A.8E632ECD@cusys.edu>`

```
Howard Brazee wrote in message <393E8F5A.8E632ECD@cusys.edu>...
>Rick Smith wrote:
>>
…[18 more quoted lines elided]…
>changed, or thrown out without messing up anybody else.  Cheaply.

I think you just answered your own question, Howard.
```

#### ↳ Re: General purpose subroutines

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hlfal$1co1$1@news.hitter.net>`
- **References:** `<393D227D.53E06EF5@cusys.edu>`

```

Howard Brazee wrote in message <393D227D.53E06EF5@cusys.edu>...
>I have had to remove general purpose subroutine calls from programs to
>make more efficient routines directly in the programs.

Hmmm! I violated the principle that code must be reused.
I did this to increase execution efficiency. ;-)

>Do OO programmers have similar needs?

No, reuse of code is too important to violate! ;-)

The "real" answer depends upon why the subroutine call was
inefficient.

If the problem was data conversion, then OO is less of a
problem because the data and methods are defined together.
Because they are defined together, they may be programmed
to work more efficiently than general-purpose subroutine calls.
------------------
Rick Smith
```

#### ↳ Re: General purpose subroutines

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393E66F6.D10DFF8F@zip.com.au>`
- **References:** `<393D227D.53E06EF5@cusys.edu>`

```
Howard Brazee wrote:
> 
> I have had to remove general purpose subroutine calls from programs
> to make more efficient routines directly in the programs.
> 
> Do OO programmers have similar needs?

The simple answer is to not worry about efficiency in the first place.
It is rarely that much of an issue and not worth the programmers time.

Second with correct implementation of OO you can eliminate a lot of
'IF' tests and thereby improve speed not decrease it.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: General purpose subroutines

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393E8C12.C395EC19@cusys.edu>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E66F6.D10DFF8F@zip.com.au>`

```


Ken Foskey wrote:
> 
> Howard Brazee wrote:
…[10 more quoted lines elided]…
> 'IF' tests and thereby improve speed not decrease it.

One reason for subroutines is to change the schema for my database
calls.  

But I was thinking of a particular subroutine which tried to to a lot,
accessing several records for validation purposes - which weren't
needed.  Finally, the call (of a COBOL program) happened to be from
EasyTrieve and the CPU % was up to 30% and slow.  There are limits on
how inefficient we can allow a program to be.
```

###### ↳ ↳ ↳ Re: General purpose subroutines

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393eb3dd.70642558@news.transport.com>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E66F6.D10DFF8F@zip.com.au> <393E8C12.C395EC19@cusys.edu>`

```
On Wed, 07 Jun 2000 11:53:22 -0600, Howard Brazee
<howard.brazee@cusys.edu> wrote:

>
>
…[22 more quoted lines elided]…
>how inefficient we can allow a program to be.

We saw this type of EasyTrieve-calls-COBOL problem too when we changed
releases of Easytrieve, and again when we implemented LE.  Turns out
the real problem has to do with configuring your Easytrieve runtime
environment properly.  We found the problem, fixed it, and the
negative performance issue disapeared.

The nature of the problem is that if you aren't configured properly,
Easytrieve will go out to the loadlib and re-load your subroutines
every time they are called.  When this happens, your job is actually
spending more time loading the subroutine than anything else.

Pete
```

###### ↳ ↳ ↳ Re: General purpose subroutines

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393F99C8.7027B36A@cusys.edu>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <393E66F6.D10DFF8F@zip.com.au> <393E8C12.C395EC19@cusys.edu> <393eb3dd.70642558@news.transport.com>`

```
That was our conclusion.  But the users needed the reports now, so I
took out the COBOL call.   Still, the question of going to simpler
subroutines (with fewer database calls) would still be applicable
without this bug.

Pete Wirfs wrote:
> 
> On Wed, 07 Jun 2000 11:53:22 -0600, Howard Brazee
…[39 more quoted lines elided]…
> Pete
```

#### ↳ Re: General purpose subroutines

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i018a$chh$1@nnrp1.deja.com>`
- **References:** `<393D227D.53E06EF5@cusys.edu>`

```
In article <393D227D.53E06EF5@cusys.edu>,
  Please, do, not, e-mail, replies, to, Howard, Brazee, post, them!!
wrote:
> I have had to remove general purpose subroutine calls from programs to
> make more efficient routines directly in the programs.

Hi:

Could you give us a couple of reasons as to why u did that?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: General purpose subroutines

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3944E415.857BE4D0@cusys.edu>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <8i018a$chh$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <393D227D.53E06EF5@cusys.edu>,
…[7 more quoted lines elided]…
> Could you give us a couple of reasons as to why u did that?

I only have one reason.  The job was taking hours using 25-35% CPU
utilization.  It looks like the problem was with the interface between
the calling EasyTrieve and the called COBOL.   But even if that were
fixed, the called program was designed to do a bunch of extra checking
with lots of database I/O.  This is fine with data entry, but not a good
idea when used with a batch look-up.  A re-write of the called program
could allow for the more efficient look-up, but a re-write of a called
module means lots of testing.  The change is no longer to the one
isolated program, but belongs to each program which uses it.

Which basically is what would happen if our enterprise were OO.  As
reuse and integration goes up, risk goes up, the testing requirements go
up, the finger pointing goes up.   The bigger the enterprise the more
complex these costs are.  Maybe this is why enterprises have avoided OO
despite its advantages.
```

###### ↳ ↳ ↳ Re: General purpose subroutines

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39453041.84879456@207.126.101.100>`
- **References:** `<393D227D.53E06EF5@cusys.edu> <8i018a$chh$1@nnrp1.deja.com> <3944E415.857BE4D0@cusys.edu>`

```
On Mon, 12 Jun 2000 07:22:30 -0600, Howard Brazee
<howard.brazee@cusys.edu> wrote:


>Which basically is what would happen if our enterprise were OO.  As
>reuse and integration goes up, risk goes up, the testing requirements go
>up, the finger pointing goes up.   The bigger the enterprise the more
>complex these costs are.  Maybe this is why enterprises have avoided OO
>despite its advantages.


Well, that can be avoided by inheriting the object and overriding the
methods with your new methods.  But then that opens a whole other
kettle of fish as far as maint goes.   I can see the multiple
inhertience being a nightmare to maintain as well.  
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
