[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing device drivers in C (was: Re: COBOL and Perl)

_18 messages · 12 participants · 1998-08_

---

### Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s2715$dng$1@news.igs.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net>`

```
>I find this fascinating, because I was on the team that built the first
>COBOL compiler for the PDP-10 and therefore paid a lot of attention to
…[3 more quoted lines elided]…
>their COBOL implementations.


By golly.  My milk machine.  The first Cobol I coded was on your
compiler<g>, about 68-69.  That was also the machine I learnt
my first Fortran and my first assembler on.  The first major Fortran
program that I ever worked on was a bootstrap Pascal compiler
to port native Pascal (in Pascal) to the 10.

Modern compilers could learn a lot from Tops-10, in my opinion
one of the most innovative and best OS's ever written.  As I recall,
I could say "COMPILE ABC" where ABC.CBL was a Cobol program,
that called a Fortran program, that called an assembler program, and
the compile command was smart enough to figure out which language
to call for each module, compile all three using the appropriate language,
then link them ... all done completely invisibly and from the single
command.  Nice job.
```

#### ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<35E4D974.570@inficad.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net>`

```
Donald Tees wrote:
> 
> >I find this fascinating, because I ever written.  As I recall,
…[5 more quoted lines elided]…
> command.  Nice job.


Why can't we have that now?

Warren Simmons
```

##### ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s2uc1$c5e$1@news.igs.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com>`

```

>> I could say "COMPILE ABC" where ABC.CBL was a Cobol program,
>> that called a Fortran program, that called an assembler program, and
>> the compile command was smart enough to figure out which language
>> to call for each module, compile all three using the appropriate
language,
>> then link them ... all done completely invisibly and from the single
>> command.  Nice job.
…[3 more quoted lines elided]…
>
Damned if I know.  Maybe because every tool is designed by a different
vendor?  Maybe because nobody likes command line interfaces anymore?
Even a good make command seems hard to come by these days. Not
one of the "integrated environments" that I have seen in the last five years
has the capability of supporting a second language.  In fact, most of them
bury the command structure so deeply that it is almost impossible to write
one for lack of information.  The pseudo-make that I am using at the
moment has wonderful pictures compared to ten years back, but cannot
handle a project with more than one main program more than one level
of dependency, nor even a filename that does not conform to it's own
private notions of file-naming conventions. There is no way to maintain
a library, or update copy books, etc. etc. etc.  How anybody that has ever
written a program greater than 1000 lines long could design a make
that is non-iterative I will never understand.  Even a DOS batch can call
DOS batch.<grumble mode on>
;<)

Maybe I should write one in Cobol.  The damned thing is just a tree
structure of dependencies.
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<%OhF1.2128$sG2.2226253@news3.mia.bellsouth.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net>`

```
Donald Tees wrote:
>
>The pseudo-make that I am using at the
…[8 more quoted lines elided]…
>;<)


That should give us a clue, Donald, as to the kinds of folks making
decisions in the industry these days.  I.e. People who don't have a clue,
because they've never done any real-world systems.
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s3bpb$7el@lotho.delphi.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net>`

```
Look at Visual Age for COBOL. It has all that in a visual mode,
plus it comes with a fairly decent make clone as well. ;) 

-Paul



Donald Tees (donald@willmack.com) wrote:

: >> I could say "COMPILE ABC" where ABC.CBL was a Cobol program,
: >> that called a Fortran program, that called an assembler program, and
: >> the compile command was smart enough to figure out which language
: >> to call for each module, compile all three using the appropriate
: language,
: >> then link them ... all done completely invisibly and from the single
: >> command.  Nice job.
: >
: >
: >Why can't we have that now?
: >
: Damned if I know.  Maybe because every tool is designed by a different
: vendor?  Maybe because nobody likes command line interfaces anymore?
: Even a good make command seems hard to come by these days. Not
: one of the "integrated environments" that I have seen in the last five years
: has the capability of supporting a second language.  In fact, most of them
: bury the command structure so deeply that it is almost impossible to write
: one for lack of information.  The pseudo-make that I am using at the
: moment has wonderful pictures compared to ten years back, but cannot
: handle a project with more than one main program more than one level
: of dependency, nor even a filename that does not conform to it's own
: private notions of file-naming conventions. There is no way to maintain
: a library, or update copy books, etc. etc. etc.  How anybody that has ever
: written a program greater than 1000 lines long could design a make
: that is non-iterative I will never understand.  Even a DOS batch can call
: DOS batch.<grumble mode on>
: ;<)

: Maybe I should write one in Cobol.  The damned thing is just a tree
: structure of dependencies.
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s3g86$kn5$1@news.igs.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net> <6s3bpb$7el@lotho.delphi.com>`

```

paulr wrote in message <6s3bpb$7el@lotho.delphi.com>...
>Look at Visual Age for COBOL. It has all that in a visual mode,
>plus it comes with a fairly decent make clone as well. ;)
>
gotta web site?
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 5)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s5fe3$r0l@lotho.delphi.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net> <6s3bpb$7el@lotho.delphi.com> <6s3g86$kn5$1@news.igs.net>`

```
Donald Tees (donald@willmack.com) wrote:

: paulr wrote in message <6s3bpb$7el@lotho.delphi.com>...
: >Look at Visual Age for COBOL. It has all that in a visual mode,
: >plus it comes with a fairly decent make clone as well. ;)
: >
: gotta web site?

www.ibm.com         then hit the software development links.
The web site doesn'tdo this compiler justice though. It is very
nice, and very portable.

-Paul
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-QdJddSEX43bE@Dwight_Miller.iix.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net> <6s3bpb$7el@lotho.delphi.com> <6s3g86$kn5$1@news.igs.net> <6s5fe3$r0l@lotho.delphi.com>`

```
On Fri, 28 Aug 1998 05:32:51, paulr@bix.com (paulr) wrote:

> Donald Tees (donald@willmack.com) wrote:
> 
…[8 more quoted lines elided]…
> nice, and very portable.


Paul,

Does it include NATIVE indexed file support on the PC?  That's 
something I have always wondered about it.

What is the method of GUI creation?  API calls?  Other method?
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 7)_

- **From:** "Paul Raulerson" <paulr@axs2000.net>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s7feb$e6a@news.etcfiber.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com> <6s2uc1$c5e$1@news.igs.net> <6s3bpb$7el@lotho.delphi.com> <6s3g86$kn5$1@news.igs.net> <6s5fe3$r0l@lotho.delphi.com> <Jl0PnHJ5PvPd-pn2-QdJddSEX43bE@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Fri, 28 Aug 1998 05:32:51, paulr@bix.com (paulr) wrote:
>
…[17 more quoted lines elided]…
>

<grin> You can stop wondering, yes it does. On workstations of course,
which is where you would need native support. Of course, if you mean NATIVE
as in, can it support mainframe (i.e. OS/390 Big Endian format) then you are
still in luck, because, yes it can. With a simple flip of a compiler switch.

The basic file formats supported are:

STL - provides the basic facilities for local files, and supports
sequential, relative, and
indexed files.

VSAM- wihch allows reading and writing files on remote systems with COBOL
I/O statements,
and also supprts sequential, relative, and indexed file types. Under OS/2 or
CICS 4.1 on NT,
you can also have local VSAM files.

BTRIEVE- files are also supported. If you use the BTRIEVE file system, this
also gives
you access to CICS files under OS/2.

STL files have the following characteristics:
    Minimum record size: 1 byte
    Maximum record size: 65536 bytes
    Max record key length: 255 bytes
    Max number or alternate keys: 253 bytes
    Max relative key value: 2**32 -1
    Max number of bytes allocated for a file: 2**32 -1

VSAM files have the following characteristics: (since they can be local...
:)
    Minimum record size: 1 byte
    Maximum record size: 64,000 bytes
    Max record key length: 255 bytes
    Max relative key value: 2**32 -2
    Max number of bytes allocated for a file: 2**32

>What is the method of GUI creation?  API calls?  Other method?
>

It is an API of course (what isn't?) but it is actually done with a very
cool front end.
The paradigm expressed is an almost total separation of presentation logic
from
the business logic- visual parts vs. non-visual parts. The actual code
produced uses
a fairly standard call using interface to do the work, but I don't think I
have ever
had to modify a single compiler generated screen yet, that is, modify it by
hand.

I think they have a free download on the ibm site, but I would attempt to
get the docs with
it first. It is VERY upwards compatible, to the point you can actually do
remote edit/compile/
debug cycles with it. It also has very good support for CICS and DB2 SQL.
(Naturally! :)

-Paul
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** cwr@cts.com (Will Rose)
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<904322741.456420@optional.cts.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s2uc1$c5e$1@news.igs.net>`

```
Donald Tees (donald@willmack.com) wrote:

: >> I could say "COMPILE ABC" where ABC.CBL was a Cobol program,
: >> that called a Fortran program, that called an assembler program, and
: >> the compile command was smart enough to figure out which language
: >> to call for each module, compile all three using the appropriate
: language,
: >> then link them ... all done completely invisibly and from the single
: >> command.  Nice job.
: >
: >
: >Why can't we have that now?
: >
: Damned if I know.  Maybe because every tool is designed by a different
: vendor?  Maybe because nobody likes command line interfaces anymore?
: Even a good make command seems hard to come by these days. Not
: one of the "integrated environments" that I have seen in the last five years
: has the capability of supporting a second language.  In fact, most of them
: bury the command structure so deeply that it is almost impossible to write
: one for lack of information.  The pseudo-make that I am using at the
: moment has wonderful pictures compared to ten years back, but cannot
: handle a project with more than one main program more than one level
: of dependency, nor even a filename that does not conform to it's own
: private notions of file-naming conventions. There is no way to maintain
: a library, or update copy books, etc. etc. etc.  How anybody that has ever
: written a program greater than 1000 lines long could design a make
: that is non-iterative I will never understand.  Even a DOS batch can call
: DOS batch.<grumble mode on>
: ;<)

IBM got around this fairly successfully with their Workframe product,
used with VAC++ 3.0 for OS/2.  However, OS/2 died in the marketplace
and IBM are moving to a more 'normal', editor-based IDE.  A lot of
Workframe's functionality was based on IBM's Workplace Shell, a very
powerful GUI which it wouldn't be practical to port.  Still, it was
the best GUI/environment I've ever used.


Will
cwr@crash.cts.com
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 4)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<35E956AC.5C014D93@hankel.mersinet.co.uk>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s2uc1$c5e$1@news.igs.net> <904322741.456420@optional.cts.com>`

```
Will Rose wrote:
> 
> IBM got around this fairly successfully with their Workframe product,
> used with VAC++ 3.0 for OS/2.  However, OS/2 died in the marketplace

I think your report of the death of OS/2 is somewhat premature.  It may
have a fairly low profile in the marketplace but that has as much to do
with IBM's inability to out-advertise Microsoft and Microsoft's constant
disinformation about it (OS/2 is not IBM's backbone product without
which the company will fail), as do posts to newsgroups asserting that
the product is dead.

> and IBM are moving to a more 'normal', editor-based IDE.  A lot of
> Workframe's functionality was based on IBM's Workplace Shell, a very
> powerful GUI which it wouldn't be practical to port.  Still, it was
> the best GUI/environment I've ever used.

And still is for me.  The system that I use for newsgroup access is,
sadly, NT4 but my server is OS/2 as are all but one of my other
clients.  I have more trouble with this single NT system than with all
four of the OS/2 systems put together.  And the shutdown in OS/2 WPS is
where it should be; a click away.
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 5)_

- **From:** cwr@cts.com (Will Rose)
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<904486565.345099@optional.cts.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <35E956AC.5C014D93@hankel.mersinet.co.uk>`

```
Charles F Hankel (charles@hankel.mersinet.co.uk) wrote:
: Will Rose wrote:
: > 
: > IBM got around this fairly successfully with their Workframe product,
: > used with VAC++ 3.0 for OS/2.  However, OS/2 died in the marketplace

: I think your report of the death of OS/2 is somewhat premature.  It may
: have a fairly low profile in the marketplace but that has as much to do
: with IBM's inability to out-advertise Microsoft and Microsoft's constant
: disinformation about it (OS/2 is not IBM's backbone product without
: which the company will fail), as do posts to newsgroups asserting that
: the product is dead.

Well, it may not be dead, but IBM is very unwilling to sell it to anyone;
even quite large IBM customers (thousands of seats) have had difficulty
specifying OS/2 over IBM's preferred NT.  However, IBM still supports it,
and until I get new hardware (for which drivers won't be available) I for
one plan to continue using it.


Will
cwr@crash.cts.com
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 6)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sc5ij$p1r@lotho.delphi.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <35E956AC.5C014D93@hankel.mersinet.co.uk> <904486565.345099@optional.cts.com>`

```

Ummm- I have no trouble ordering OS/2, and I can't imagine
the large accounts would have more trouble than I would.
I'm not sure, but your local OS/2 acquisition problems
may be just that, local. 

Yours,
-Paul


Will Rose (cwr@cts.com) wrote:
: Charles F Hankel (charles@hankel.mersinet.co.uk) wrote:
: : Will Rose wrote:
: : > 
: : > IBM got around this fairly successfully with their Workframe product,
: : > used with VAC++ 3.0 for OS/2.  However, OS/2 died in the marketplace

: : I think your report of the death of OS/2 is somewhat premature.  It may
: : have a fairly low profile in the marketplace but that has as much to do
: : with IBM's inability to out-advertise Microsoft and Microsoft's constant
: : disinformation about it (OS/2 is not IBM's backbone product without
: : which the company will fail), as do posts to newsgroups asserting that
: : the product is dead.

: Well, it may not be dead, but IBM is very unwilling to sell it to anyone;
: even quite large IBM customers (thousands of seats) have had difficulty
: specifying OS/2 over IBM's preferred NT.  However, IBM still supports it,
: and until I get new hardware (for which drivers won't be available) I for
: one plan to continue using it.


: Will
: cwr@crash.cts.com
```

###### ↳ ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

_(reply depth: 7)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ea5f25.1229967@news2.ibm.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <35E956AC.5C014D93@hankel.mersinet.co.uk> <904486565.345099@optional.cts.com> <6sc5ij$p1r@lotho.delphi.com>`

```
On 30 Aug 1998 18:27:31 GMT, paulr@bix.com (paulr) wrote:

>
>Ummm- I have no trouble ordering OS/2, and I can't imagine
…[6 more quoted lines elided]…
>


Paul,

just try to buy an IBM Thinkpad with OS/2 pre-loaded .... you just
cannot do it!

Regards

Volker Bandke
(BSP GmbH)

with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** tstyles@my-dejanews.com
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s3has$11g$1@nnrp1.dejanews.com>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E4D974.570@inficad.com>`

```
In article <35E4D974.570@inficad.com>,
  warrens@iname.com wrote:
> Donald Tees wrote:
> >
…[12 more quoted lines elided]…
>

$ probably. You can make more money by selling products that require add-ons
and support than by selling something that's simple and works.
```

#### ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** Ari Lukumies <ari.lukumies@elmont.fi>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<35E51718.621C0CA2@elmont.fi>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net>`

```
Donald Tees wrote:

[snip]
> Modern compilers could learn a lot from Tops-10, in my opinion
> one of the most innovative and best OS's ever written.  As I recall,
…[5 more quoted lines elided]…
> command.  Nice job.

Would that be a little like 'cc' (compiler control) in Unix? (No, it
doesn't stand for 'c compiler'.)

	AriL
```

##### ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<6s3cpt$hk6$1@news.igs.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E51718.621C0CA2@elmont.fi>`

```

>Would that be a little like 'cc' (compiler control) in Unix? (No, it
>doesn't stand for 'c compiler'.)


I don't know, have never used it.
```

##### ↳ ↳ Re: Writing device drivers in C (was: Re: COBOL and Perl)

- **From:** John Porter <jdporter@min.net>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.c
- **Message-ID:** `<35E55C72.1E3D@min.net>`
- **References:** `<35e08cf0.3273969@nntp.ix.netcom.com> <3298232.76073.22283@kcbbs.gen.nz> <35df95c8.636306@nntp.ix.netcom.com> <I1%D1.448$Kt4.2131068@news1.atlantic.net> <6rqiq9$ehg@lotho.delphi.com> <ZYdE1.473$Kt4.2409046@news1.atlantic.net> <6s007l$4u2@lotho..delphi.com> <904129648snz@genesis.demon.co.uk> <6s106c$cke@lotho.delphi.com> <6s1fsg$2io@news-central.tiac.net> <6s2715$dng$1@news.igs.net> <35E51718.621C0CA2@elmont.fi>`

```
Ari Lukumies wrote:
> 
> Would that be a little like 'cc' (compiler control) in Unix? (No, it
> doesn't stand for 'c compiler'.)

I think so.  In typical unixes (or at least SunOS, where my experience
is), all compilers (c, fortran, pascal, and whatever else) generate
object (code|files) which look just like the object generated by
the assembler; so once the objects are created by each compiler, the
objects can all be linked together, as if they were generated by the
assembler.  cc can dispatch the appropriate compiler (or the assembler),
based on the file name.  (Of course, to actually link such objects
together successfully, they have to cooperate on calling conventions,
which can take some work.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
