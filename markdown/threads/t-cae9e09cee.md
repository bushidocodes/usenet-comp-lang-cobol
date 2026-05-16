[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Adding extra fields...

_13 messages · 10 participants · 1999-11_

---

### Adding extra fields...

- **From:** morella3253@my-deja.com
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
Hi to all,

I have to add two extra fields to my existing record layout and
I was wondering whether once I have changed the copy book for this
new record layout, do I have to change anything in programs that
are not using these new fields??
(i.e will programs that are using the old record layout still work)

The two extra fields will be added to the end of the existing record.


Thanks
Morella Hernandez


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Adding extra fields...

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7n_3.1535$5q.15247@news3.mia>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
Let's see, data record is n bytes,
ADD 6 to n
write new records at n+6 with changed progra
read records at n+6 in unchanged programs
CAN YOU SAY FILE-STATUS = 95?

At the very least you will need to RECOMPILE all PROGRAMS USING that
COPYBOOK

morella3253@my-deja.com wrote in message <81btp7$7sh$1@nnrp1.deja.com>...
>Hi to all,
>
…[14 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: Adding extra fields...

- **From:** "Anon" <anon@anon.com>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Spf_3.36931$YI2.1853881@typ11.nn.bcandid.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
<morella3253@my-deja.com> wrote in message
news:81btp7$7sh$1@nnrp1.deja.com...
> I have to add two extra fields to my existing record layout and
> I was wondering whether once I have changed the copy book for this
> new record layout, do I have to change anything in programs that
> are not using these new fields??
> (i.e will programs that are using the old record layout still work)

Once you have converted the file it will be necessary to recompile every
program which uses that copybook.  Programs using the old record layout will
NOT work once the record length (maybe blocksize on some systems) changes.
HTH
```

#### ↳ Re: Adding extra fields...

- **From:** "ChrisOsborne" <chris_n_osborne@msn.com>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#8o4hQRN$GA.275@cpmsnbbsa03>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
What platform?
What compiler?
What type of files?

If you're using anything on a mainframe, then it's quite likely you'll have
a bunch of JCL to change, at least.


<morella3253@my-deja.com> wrote in message
news:81btp7$7sh$1@nnrp1.deja.com...
> Hi to all,
>
…[14 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Adding extra fields...

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383988E9.87BFB3C0@NOSPAMhome.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
morella3253@my-deja.com wrote:
> 
> Hi to all,
…[7 more quoted lines elided]…
> The two extra fields will be added to the end of the existing record.

With fixed length records, this should not be any problem.  Obviously
anywhere where you had the old record length hard coded, the number
should change.  (JCL, FD) as long as anywhere you copy the record to and
from (READ INTO). 

Also consider whether you will need to access previous versions of this
file with your changed programs.  If so, you may wish to convert them to
the new record size with spaces (or whatever) for the new fields.
```

#### ↳ Re: Adding extra fields...

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3839ABC9.70E0202A@home.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```


morella3253@my-deja.com wrote:
> 
> Hi to all,
…[8 more quoted lines elided]…
> 

As indicated by Anon you will have to re-compile any programs which
contain the larger record format for the new record. There are several
factors which can help with changing file record sizes :-

(a) If possible, make access to a file a common sub-routine so that the
only program affected is the 'file-program'; however, if you are
returning the COMPLETE record to your calling program then the copybook
change or the returned data through Linkage will necessitate the calling
program being re-compiled. (If you only return selective fields, then
'receiving' programs don't need to be re-compiled).

(b) It is not a bad idea to add a FILLER area to the end of your file
record format, say, 10 or 20 characters - so that this area can hold
values for future fields.

(c) If you are NOT CHANGING existing record size :-

    01 existing-record.
       05 existing data    pic x(......
       05 filler	   pic x(10).

    in your copybook change the filler to, e.g. :-      

    01 existing-record.
       05 existing data    pic x(......
       05 new-number	   pic 9(02).
       05 new-char	   pic x.
       05 filler	   pic x(07).   *> 10 - 3

Then you need to run a program - read in existing records and write out
new records either initializing or move zeroes or spaces to new-number
and new-char. (If you already know the values to go into new-number and
new-char, you could enter them at this stage).

(d) If you ARE CHANGING the record size :-

oldcopybook :-

    01 old-existing-record.
       05 old-existing data    pic x(......
	
newcopybook :-

    01 new-existing-record.
       05 new-existing data    pic x(......
       05 new-number	       pic 9(02).
       05 new-char	       pic x.
       05 filler	       pic x(10). 
  
Read in oldfile, move old-existing data to new-existing data; initialize
or move values to new-number and new-char; write new-existing record.
 
It's messy - but helps if you can plan for record-size increases. I
don't know which compiler you are using, but mine will re-compile all
programs which have a copybook which has been changed.

Jimmy, Calgary AB
```

#### ↳ Re: Adding extra fields...

- **From:** john_mindock@my-deja.com
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81ect5$17v$1@nnrp1.deja.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
In article <81btp7$7sh$1@nnrp1.deja.com>,
  morella3253@my-deja.com wrote:
> Hi to all,
>
…[9 more quoted lines elided]…
> Morella Hernandez

As other posters have said: There are situations that require changes
to other programs and other situations that will work without the
changes.

However, let me throw in a plug for future maintenance. Let's say you
change the copybook/records for your immediate needs in program ABC but
don't change program XYZ's view of that file's records.
Three years later someone gets a hot project that causes them to add
some fields to the same record layout, for use in program XYZ. So they
use 'a few unused bytes at the end of the record'. Unfortunately they
don't see the changes you made, so they step on top of the 'few unused
bytes at the end of the record' that your activities changed. Your
previously-modified records get clobbered with their new data.
IMHO It's better to bite the time bullet and recompile them all. Maybe
you can convince the Q/A guys that the recompiles don't need to be
tested.

John

>
> Sent via Deja.com http://www.deja.com/
> Before you buy.
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Adding extra fields...

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<th8n3sk0qvr6k8lmiocr4488jmah4bg1em@4ax.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com> <81ect5$17v$1@nnrp1.deja.com>`

```
On Tue, 23 Nov 1999 15:46:46 GMT john_mindock@my-deja.com wrote:

   [ snipped ]

:>However, let me throw in a plug for future maintenance. Let's say you
:>change the copybook/records for your immediate needs in program ABC but
:>don't change program XYZ's view of that file's records.
:>Three years later someone gets a hot project that causes them to add
:>some fields to the same record layout, for use in program XYZ. So they
:>use 'a few unused bytes at the end of the record'. 

Which will be in the copybook.

They will see that those few bytes they thought were available by looking at
the listing aren't available.

As a side point, I would expect that few programmers look at the COBOL listing
(rather than the source) other than to check the DMAP/PMAP after an abend.

I used to, for complicated COBOL statements, after I had discovered a bug in
the compiler. I wanted to make sure the machine code was correct.

:>                                                   Unfortunately they
:>don't see the changes you made, so they step on top of the 'few unused
:>bytes at the end of the record' that your activities changed. Your
:>previously-modified records get clobbered with their new data.
:>IMHO It's better to bite the time bullet and recompile them all. Maybe
:>you can convince the Q/A guys that the recompiles don't need to be
:>tested.

If the source program uses the copybook there is no issue and no need to
recompile.

If the source program does not use the copybook you already have a maintenance
nightmare and I would advise rectification of the problem.

All recompiles should be QA'd. There is always the possibility that the source
and load do not match as well as changes in compiler options.
```

###### ↳ ↳ ↳ Re: Adding extra fields...

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383BF15E.485ED864@NOSPAMhome.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com> <81ect5$17v$1@nnrp1.deja.com> <th8n3sk0qvr6k8lmiocr4488jmah4bg1em@4ax.com>`

```
Binyamin Dissen wrote:

> As a side point, I would expect that few programmers look at the COBOL listing
> (rather than the source) other than to check the DMAP/PMAP after an abend.

But line numbers in the abend reference the listing, not the source.
 
> I used to, for complicated COBOL statements, after I had discovered a bug in
> the compiler. I wanted to make sure the machine code was correct.

I have seen some troubles with pre-compiler nested IFs before - looking
at the listing will help here.


> If the source program uses the copybook there is no issue and no need to
> recompile.

WHAT?!?!  If you change the size of the record there certainly IS a need
to recompile.  It also helps you read formatted dumps if the record
format is current.

And it is easier to recompile everything when a copymember changes - as
opposed to finding implementing the new record format next time
maintenance is done on that program.  Change it everywhere, test it, and
keep the change simple.


> All recompiles should be QA'd. There is always the possibility that the source
> and load do not match as well as changes in compiler options.

What does "QA'd" mean?  

We use Endeavor to (among other things) force standard compile options
in all production jobs.
```

###### ↳ ↳ ↳ Re: Adding extra fields...

_(reply depth: 4)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g26o3sororpdiuohu2ga1udj7mg70aubc9@4ax.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com> <81ect5$17v$1@nnrp1.deja.com> <th8n3sk0qvr6k8lmiocr4488jmah4bg1em@4ax.com> <383BF15E.485ED864@NOSPAMhome.com>`

```
On Wed, 24 Nov 1999 07:08:30 -0700 Howard Brazee <brazee@NOSPAMhome.com>
wrote:

:>Binyamin Dissen wrote:

   [ snipped ]

:>> If the source program uses the copybook there is no issue and no need to
:>> recompile.

:>WHAT?!?!  If you change the size of the record there certainly IS a need
:>to recompile.  It also helps you read formatted dumps if the record
:>format is current.

If the record size changes you will have a bit more work than just
recompiling. File conversions, archival copies of programs to be able to run
against the data backups, etc.

If "unused bytes" are used and thus the record size didn't change, why
recompile?

:>And it is easier to recompile everything when a copymember changes - as
:>opposed to finding implementing the new record format next time
:>maintenance is done on that program.  Change it everywhere, test it, and
:>keep the change simple.

If it is a copybook it will be done automatically.

If unused bytes of a record are needed for a particular subset of programs why
recompile all programs?

:>> All recompiles should be QA'd. There is always the possibility that the source
:>> and load do not match as well as changes in compiler options.

:>What does "QA'd" mean?  

Quality Assurance, i.e., tested.

:>We use Endeavor to (among other things) force standard compile options
:>in all production jobs.

And one can hope that everyone uses the standards.
```

###### ↳ ↳ ↳ Re: Adding extra fields...

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383D2065.6B8621D8@zip.com.au>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com> <81ect5$17v$1@nnrp1.deja.com> <th8n3sk0qvr6k8lmiocr4488jmah4bg1em@4ax.com> <383BF15E.485ED864@NOSPAMhome.com> <g26o3sororpdiuohu2ga1udj7mg70aubc9@4ax.com>`

```
Binyamin Dissen wrote:
> 
> On Wed, 24 Nov 1999 07:08:30 -0700 Howard Brazee <brazee@NOSPAMhome.com>
…[14 more quoted lines elided]…
> 

QA does not necessarily mean tested.  It does mean verified.  IF your
procedures allow a visual verification by another experienced
programmer to ensure functionality is not compromised then that is
absolutely fine.

If you do wish to test what level do you require.
-  Smoke test - run a parallel production run and does it fall over.
- Thorough test - run a full testing schedule against it.

We work with compromises, where do you draw the line.

I would not necessarily require a recompile, however I would have to
be very familiar with the application to be sure.
```

###### ↳ ↳ ↳ Re: Adding extra fields...

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3842B882.B32A3FB1@NOSPAMhome.com>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com> <81ect5$17v$1@nnrp1.deja.com> <th8n3sk0qvr6k8lmiocr4488jmah4bg1em@4ax.com> <383BF15E.485ED864@NOSPAMhome.com> <g26o3sororpdiuohu2ga1udj7mg70aubc9@4ax.com>`

```
Binyamin Dissen wrote:
> 
> On Wed, 24 Nov 1999 07:08:30 -0700 Howard Brazee <brazee@NOSPAMhome.com>
…[18 more quoted lines elided]…
> recompile?

Then you continue with other statements which require that the record
size does not change.  We're in agreement there, although recompiling
can help in formatted dumps.  We also seem to be in agreement that if
the record size does change, we need to recompile, and that is what my
understanding of the situation was.
```

#### ↳ Re: Adding extra fields...

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1I_3.1692$bH2.27451@typhoon01.swbell.net>`
- **References:** `<81btp7$7sh$1@nnrp1.deja.com>`

```
All the responses so far are correct; you will have to
recompile all the programs. But if you will permit a
re-phrasing of your question, it might be made clearer.

"I have to add fields to the end of an existing record.
I will change the appropriate copy books, but does
record definition take place at execution time or at
compile time?

The answer is "compile time." Copy books are not
a form of data dictionary the program interrogates at
run time to access the latest rendition of the data.

<morella3253@my-deja.com> wrote in message
news:81btp7$7sh$1@nnrp1.deja.com...
> Hi to all,
>
…[6 more quoted lines elided]…
> The two extra fields will be added to the end of the existing
record.
>
>
…[5 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
