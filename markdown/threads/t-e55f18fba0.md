[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# maximum supported length of characters in a table

_9 messages · 7 participants · 2001-09_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### maximum supported length of characters in a table

- **From:** "J���rn Fischer" <joern.fischer@surfeu.de>
- **Date:** 2001-09-10T21:36:14+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
Hello, have the following question:

Is there a possibility in COBOL (OS-390 / LE370) to implement tables, whose
storage space contains more than 16 MB? I have to enlarge the size the
following table onto 999999 elements:

01  TB-ABGF.
    03  TB-ELEMENT OCCURS 999999
        INDEXED BY ABGF-I.
        05 TB-FELDNR PIC S9(9) COMP.
        05 TB-FELDPTR PIC S9(4) COMP.
        05 TB-FORMATINT PIC X.
        05 TB-OPERATOR PIC X.
        05 TB-ABGRVON.
           07 TB-ABGRVON-N PIC S9(18) COMP-3.
        05 TB-ABGF-ABGRBIS.
           07 TB-ABGRBIS-N PIC S9(18) COMP-3.

and I receive the following error report from the compiler:

  The length of a table exceeded the maximum supported length of 16777215
  characters for a data record in the "WORKING-STORAGE SECTION",
  "LOCAL-STORAGE SECTION" or "LINKAGE SECTION". The length of the table
  was truncated to 16777215 characters.

The compiler options are:
  *PARMMVS COMPILER=LE370
  *PARMMVS PARM.COB=(RENT,RES,DATA(31),OPT,DYN,MAP,OFFSET,
  *PARMMVS TRUNC(OPT))
  *PARMMVS PARM.LNK=(RENT,REUS,'AMODE=31,RMODE=ANY')

Is my only possibility to separate the table in several parts, when I can't
economize the storage space of the variables in each occurs element? I
almost cant believe it!

Thanks in advance
Jï¿½rn Fischer
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-10T15:17:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nj7aa$7tl$1@slb4.atl.mindspring.net>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
No there is no way to create a single table greater than 16M in IBM COBOL
for OS/390 & VM.

You have (at least) two options:

1) create multiple tables (but be aware of the TOTAL size of WS allowed)

2) and I consider this MUCH more likely, if you have a table of that size,
change it to an indexed file.
```

##### ↳ ↳ Re: maximum supported length of characters in a table

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-09-11T00:09:37+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esaqptk88103bu6efq6j2a9dvldf7l5n8o@4ax.com>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com> <9nj7aa$7tl$1@slb4.atl.mindspring.net>`

```
On Mon, 10 Sep 2001 15:17:05 -0500 "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

:>No there is no way to create a single table greater than 16M in IBM COBOL
:>for OS/390 & VM.

:>You have (at least) two options:

:>1) create multiple tables (but be aware of the TOTAL size of WS allowed)

:>2) and I consider this MUCH more likely, if you have a table of that size,
:>change it to an indexed file.

Would it be possible to call an assembler subroutine which would getmain the
table and use a LINKAGE SECTION descriptor with a smaller number of elements?

:>"Jï¿½rn Fischer" <joern.fischer@surfeu.de> wrote in message
:>news:9nj4nj$ail$04$1@news.t-online.com...
:>> Hello, have the following question:

:>> Is there a possibility in COBOL (OS-390 / LE370) to implement tables,
:>whose
:>> storage space contains more than 16 MB? I have to enlarge the size the
:>> following table onto 999999 elements:

:>> 01  TB-ABGF.
:>>     03  TB-ELEMENT OCCURS 999999
:>>         INDEXED BY ABGF-I.
:>>         05 TB-FELDNR PIC S9(9) COMP.
:>>         05 TB-FELDPTR PIC S9(4) COMP.
:>>         05 TB-FORMATINT PIC X.
:>>         05 TB-OPERATOR PIC X.
:>>         05 TB-ABGRVON.
:>>            07 TB-ABGRVON-N PIC S9(18) COMP-3.
:>>         05 TB-ABGF-ABGRBIS.
:>>            07 TB-ABGRBIS-N PIC S9(18) COMP-3.

:>> and I receive the following error report from the compiler:

:>>   The length of a table exceeded the maximum supported length of 16777215
:>>   characters for a data record in the "WORKING-STORAGE SECTION",
:>>   "LOCAL-STORAGE SECTION" or "LINKAGE SECTION". The length of the table
:>>   was truncated to 16777215 characters.

:>> The compiler options are:
:>>   *PARMMVS COMPILER=LE370
:>>   *PARMMVS PARM.COB=(RENT,RES,DATA(31),OPT,DYN,MAP,OFFSET,
:>>   *PARMMVS TRUNC(OPT))
:>>   *PARMMVS PARM.LNK=(RENT,REUS,'AMODE=31,RMODE=ANY')

:>> Is my only possibility to separate the table in several parts, when I
:>can't
:>> economize the storage space of the variables in each occurs element? I
:>> almost cant believe it!
```

###### ↳ ↳ ↳ Re: maximum supported length of characters in a table

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-10T16:34:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9njbnb$4v3$1@slb2.atl.mindspring.net>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com> <9nj7aa$7tl$1@slb4.atl.mindspring.net> <esaqptk88103bu6efq6j2a9dvldf7l5n8o@4ax.com>`

```
I thought about "data-in-virtual" and Linkage Section as a "solution" too
(even though I PERSONALLY question any application "design" for such a large
table in memory at the same time).  However, COBOL does "check" that
01-levels EVEN in Linkage Section aren't larger than 16M.  It is true that
you could get a "data in virtual" (or assembler) "chunk" of storage and LIE
to your program about the table size in Linkage Section.  However, not only
is that poor programming (IMHO) and error-prone when it comes to
maintenance, but it also means that you can never use SSRANGE and *may* in a
future release of COBOL find that you are getting run-time errors for
fibbing to your linkage section.
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-09-10T20:24:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k9n7.257663$VV1.19398780@bin1.nnrp.aus1.giganews.com>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```

On 10-Sep-2001, "J�rn Fischer" <joern.fischer@surfeu.de> wrote:

> Hello, have the following question:
>
…[33 more quoted lines elided]…
> almost cant believe it!

Yep, I used to hit the old limit, but haven't hit this limit yet.   When I
need a table that big, I use a keyed file instead.  With modern virtual
memory, that might not be too much slower than the paging you get with such
a huge program.  How does your table find an element?  Is it a hashed table?

But why should separating the table in several parts not economize the
storage space?

There are different ways of breaking up a table.   You can have two tables
with fewer occurrences, or you can have multiple fields in the same position
in different tables.  If you are using a hashed table, the latter would work
better.

Why are you wanting such a huge table in memory?
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-09-10T22:31:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010910183154.21852.00000807@mb-ck.aol.com>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
Jï¿½rn Fischer writes ...


>Hello, have the following question:
>
…[31 more quoted lines elided]…
>almost cant believe it!

Yep. About a year or so ago, at SHARE, I raised the issue of supporting tables
larger than 16MB. The COBOL developers seemed surprised that anyone would want
to. Maybe they've been working on enlarging the limit in the next release. But
currently, you can't have a table larger than 16MB.

Kind regards,

Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2001-09-11T16:38:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0109111538.6ad58042@posting.google.com>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
I have successfully done this type of  thing in the distant past, when
the limit wasn't so high and the compilers perhaps not so stringent in
checking such usage, by defining the table in the working storage of 
a calling program and immediately after defining several other large
consecutive tables, then passing the address to the first table as the
parameter to the called program, which was then able to access the
higher level elements in the subsequent tables with appropriate index
settings.   The only processing that the calling program did was to
initialise the table.  The calling program could instead be an
assembler program that defines the passed table directly as a single
unit.  This would obviate possible problems where consecutively
defined 01 level items in a COBOL program were not necessarily
consecutive in the resultant object code.  I would be inclined to
first check with your local systems programmers to ensure that
assembler doesn't impose similar limits.

I agree with one of the other respondents that this solution is prone
to problems with future compiler upgrades, though such upgrades might
also increase the maximum table size limit at the same time. 
Certainly, I would test it in a simple program first, it is not enough
just to clean compile such a solution.  It might also be advisable to
ensure that it works in the production environment first too.  You may
have to alter some of your organisation's compiler options to get this
to work, as one of the other respondents indicated.

Using two tables instead of just one doesn't seem excessively onerous.
 Each could be of 500,000 elements and use of a procedure (section,
subprogram, nested program or method) to access the table could
automatically sort out which to access in a manner that the rest of
the program would not have to be concerned about.  However, such a
procedure should not be an independently compiled program because of
the execution time overheads.

If you decide instead to hold the table as a file, then using a VSAM
RRDS seems to be the most appropriate route.  If you adjust the JCL
parameters to ensure that the buffering is such that the whole file is
in the buffers at the same time, then the speed of file access would
be greatly enhanced, provided the system doesn't have page thrashing
problems, where it spends too much time swapping pages in and out of
memory, again, this should be discussed with your local system
programmers.

I see that the size of your individual table elements is 28 bytes,
this would allow you to fit 599,186 elements into a table just within
the 16,777,215 table size limit, it may be that this would be
sufficient for your current purposes and the table size could be
subsequently increased again when compiler upgrades permit.  999,999
elements of 28 bytes requires a table size of 27,999,972 bytes.  There
is an ultimate limit to this type of fiddling, in that the size of an
index is itself limited, but you are way off that at present and the
use of subscripts rather than indexes would extend it a bit further,
though even they are limited to 2**32 -1.  16,777,216 is 2**24, while
258 is 2**8.

Cheers Robert


"J?n Fischer" <joern.fischer@surfeu.de> wrote in message news:<9nj4nj$ail$04$1@news.t-online.com>...
> Hello, have the following question:
> 
…[34 more quoted lines elided]…
> Jï¿½rn Fischer
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** jraben@cascinc.com (Jeff Raben)
- **Date:** 2001-09-12T15:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b9f83a3.2838186@news.bullseyetelecom.net>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
"J�rn Fischer" <joern.fischer@surfeu.de> wrote:

>Hello, have the following question:
>
…[3 more quoted lines elided]…
>
snip

Build a file with Very Large Records with thousands of occurance in
each.
Then you can read a relative record 1 .... n to pull in part of the
array.  You can even REWRITE the record to update the array.
Your reads would be low (unless the input data referencing the table
is a real sorted mess.
Maybe SORT your input for some semblance of order. To reduce the above
pseudo paging.

JR

and stir with a Runcible spoon...
```

#### ↳ Re: maximum supported length of characters in a table

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2001-09-12T15:01:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0109121401.37ecbdd@posting.google.com>`
- **References:** `<9nj4nj$ail$04$1@news.t-online.com>`

```
Follow up before other comments were received - sent on 12Sep2001

A word of caution is in order when initialising such tables in a
calling program.  It is important to ensure that the 01 definitions in
the calling program are integral multiples of eight bytes in length to
prevent gaps between the consecutive items.  I think I just defined
them as PIC X(nnnnnn) without any subordinate levels and initialised
to low-values.  A check to ensure that there are no inter-item gaps
would be in order, in case compilers don't behave  in quite the same
way these days.

Regarding whether to use a VSAM KSDS or RRDS if going for the file
option, it depends on the circumstances, if you always want the full
table present, then the RRDS is preferable and probably a good deal
faster, but if only some of the table is used most of the time, then a
KSDS would generally use much less space.  JCL is not the only way to
affect how much of the file is held in memory at one time, the VSAM
DEFINE parameters can be used similarly, though I forget how, so
reading the AMS (access methods services) manuals is advisable.  One
advantage of using an RRDS, or for that matter a full size table, is
that the program would establish whether or not it could get
sufficient resources at the commencement of execution rather than
possibly fail part way through.

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
