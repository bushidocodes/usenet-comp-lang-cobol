[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS Garbage in WS - LE vs. COBOLII?

_7 messages · 5 participants · 2001-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS Garbage in WS - LE vs. COBOLII?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-09T19:11:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net>`

```

This isn't strictly a matter of applications coding... but there have been
some discussions of this which have floated o'er the cubicle wall and I
thought I'd mention it.

I am kinda sketchy on the details but... it seems that when testing a new
version of CICS folks have found that programs which have previously been
well-behaved are now showing garbage in unitialised WS fields.  This
happens to either LE programs or COBOLII (I *said* I was sketchy).

Has anyone else run across this phenomenon or one similar?

DD
```

#### ↳ Re: CICS Garbage in WS - LE vs. COBOLII?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-09T16:04:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961plt$qq6$1@slb2.atl.mindspring.net>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net>`

```
What you are talking about is a "well known" issue with post-OS/VS COBOL.

If you are using the VS COBOL II run-time library, then make certain that
you use the WSCLEAR run-time option (to initialize fields without VALUE
clauses to binary zero).

If you are using the LE run-time library, then use the STORAGE (00, ...)
run-time option.  (You will want to look at the other parts of the STORAGE
option - as they SHOULD be different under CICS and non-CICS.

There are no compile-time options to "impact" this - but using VALUE clauses
will "solve" the problem as well.
```

##### ↳ ↳ Re: CICS Garbage in WS - LE vs. COBOLII?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-10T00:56:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%k0h6.15886$Sl.697441@iad-read.news.verio.net>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net> <961plt$qq6$1@slb2.atl.mindspring.net>`

```
In article <961plt$qq6$1@slb2.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>What you are talking about is a "well known" issue with post-OS/VS COBOL.

Hmmmm... is that 'well known' as in 'that well-known singer, Wilf Carter,
Canada's Yodelling Cowboy'?

Thanks much for the info, Mr Klein; I'll pass it along to those who deal
in such arcana.  Full attribution will be given, of course.

DD
```

##### ↳ ↳ Re: CICS Garbage in WS - LE vs. COBOLII?

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2001-02-10T02:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9627vj$4is$1@nnrp1.deja.com>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net> <961plt$qq6$1@slb2.atl.mindspring.net>`

```
In article <961plt$qq6$1@slb2.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> What you are talking about is a "well known" issue with post-OS/VS
COBOL.
>
> If you are using the VS COBOL II run-time library, then make certain
that
> you use the WSCLEAR run-time option (to initialize fields without
VALUE
> clauses to binary zero).
>
> If you are using the LE run-time library, then use the STORAGE
(00, ...)
> run-time option.  (You will want to look at the other parts of the
STORAGE
> option - as they SHOULD be different under CICS and non-CICS.
>
> There are no compile-time options to "impact" this - but using VALUE
clauses
> will "solve" the problem as well.
>
…[6 more quoted lines elided]…
> > This isn't strictly a matter of applications coding... but there
have been
> > some discussions of this which have floated o'er the cubicle wall
and I
> > thought I'd mention it.
> >
> > I am kinda sketchy on the details but... it seems that when testing
a new
> > version of CICS folks have found that programs which have
previously been
> > well-behaved are now showing garbage in unitialised WS fields.  This
> > happens to either LE programs or COBOLII (I *said* I was sketchy).
…[6 more quoted lines elided]…
>

Bill,

Although these options WILL work in both the LE and COBOL2
environments, they are overhead. How substantial ? It depends on the
workload.

I totally agree. Going forward, new programs should use either the
VALUE clause or issue initialisations during HOUSEKEEPING.

Cheers,

Bill


Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: CICS Garbage in WS - LE vs. COBOLII?

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 2001-02-10T21:48:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A85B65B.B1BE4CC1@acm.org>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net> <961plt$qq6$1@slb2.atl.mindspring.net>`

```
I am enough of a programming purist that I have always argued that code
that depends on a initial value in a variable that is not explicitly
initialized is "incorrect code".  I suspect the COBOL standard would
describe such values as "undefined" and leave behavior of such a program
up to the implementation.  To write code whose ultimate behavior is
determined by factors outside the programmer's control is not goodness.

Unfortunately in the real world you have programmers that have gotten
away with poor coding practices, and removing operating system support
that allows such code to run with some degree of success becomes a
political issue.  When we converted to COBOL II many years ago, we tried
running without WSCLEAR in the CICS environment to improve performance. 
There was an initial attempt to clean up bad code as part of the
migration to COBOL II, but there was just too much bad code out there
and the "it used to run" argument won the battle.  We have been running
with WSCLEAR and the LE STORAGE equivalent ever since.

"William M. Klein" wrote:
> What you are talking about is a "well known" issue with post-OS/VS COBOL.
> If you are using the VS COBOL II run-time library, then make certain that
…[8 more quoted lines elided]…
>  wmklein <at> ix.netcom.com
...
```

#### ↳ Re: CICS Garbage in WS - LE vs. COBOLII?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-02-12T21:46:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fuhg8toc97nvt7uim81gbgi87ujiqlouhd@4ax.com>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net>`

```
On Fri, 09 Feb 2001 19:11:16 GMT, docdwarf@clark.net (  NA) wrote:

>
>This isn't strictly a matter of applications coding... but there have been
…[10 more quoted lines elided]…
>DD
Doc,

In older releases of CICS (up to Version 2) CICS would initialize the working storage of a
COBOL program (OS/VS COBOL or VS/COBOL II) to binaty zeroes before the COBOL runtime would
insert the initial values.

Since CICS Version 3 this initialization by CICS no longer happens.  While one might argue
that this is a bug, it is actually a fix to a bug, because IBM always has stated that the
contents of initialized variables in Working-Storage is unpredictable.

How do you get out of the mess?

option1: Always initialize variables in your program.  Most important, at the beginning of
your program, do MOVE LOW-VALUES to mapnameO for all the maps you are working with.  But
initializing must be done for all other variables as well

option2: Let the runtime system do it for you.  WSCLEAR is the option for VS/COBOL,
STORAGE is the option for LE.  No changes to the program (good news).  Because of higher
overhad - longer responsetimes (bad news). Because of higher processor speed and faster
I/O system - less responsetime (good news)

Programmer time being more expensive than computer time, I would opt for option2 (and
still would ask all the programmers to work according to option 1)
 
     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         What does CICS mean? - Crash IBM Computer Swiftly
```

##### ↳ ↳ Re: CICS Garbage in WS - LE vs. COBOLII? - Thanks to all!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-12T20:57:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K6Yh6.16326$Sl.721116@iad-read.news.verio.net>`
- **References:** `<ohXg6.15847$Sl.694504@iad-read.news.verio.net> <fuhg8toc97nvt7uim81gbgi87ujiqlouhd@4ax.com>`

```

To all - many thanks for you kind and rapid responses; they have been
relayed to the Appropriate Personnel and the response was:

'Well... we kinda figured that out but it's nice to see that we aren't the
only ones who came up with that problem.'

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
