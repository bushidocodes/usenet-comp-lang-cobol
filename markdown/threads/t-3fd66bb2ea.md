[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODO's and "IBM mentality"

_7 messages · 3 participants · 2003-06_

---

### ODO's and "IBM mentality"

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-08T22:23:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc0ujr$tje$1@slb9.atl.mindspring.net>`

```
As a follow-up on a different thread, I thought that I would point out two
IBM "extensions" that deal with ODO's (Occurs Depending On) structures.  I
know that Micro Focus has an emulation for these; I assume that Realia does,
and wouldn't be surprised if others do as well.  I am *not* (necessarily)
saying that these are "wonderful" constructs - but they are cases where
"existing" (and new) programs designed for IBM environments find ODO's
particularly useful.

"Feature" 1 - nested ODO.

 Consider a structure of the format:

  01 aRec.
       05 Num1    Pic 99.
       05 Num2    Pic 99.
       05 Level1 Occurs 1 to 99 times
                         depending on Num1.
             10  Elem1    Pic X.
             10  Level2  Occurs 1 to 50 times
                                Depending on Num2
                   15 Elem2   Pic XX.


This type of "structure" where the nested ODO "floats" within the containing
ODO is particularly "useful" for modeling some "real-world" structures.  In
the IBM extension, the maximum STORAGE may be allocated - but the references
are to the "user-friendly" (well at least friendly to me <G>) locations.


"Feature" 2 -  ODO with following data

 Consider a structure of the format:

  01 aRec.
       05  Num1   Pic 99.
       05  Level1 occurs 1 to 99 times
                         depending on Num1
             10  Elem1   Pic X.
       05  After-ODO    Pic X(10).

With this IBM extension, the "location" of the data-item After-ODO "floats"
within aRec depending on the CURRENT size of Num1.

    ***

It should be noted that BOTH of these structures are medium-error-prone for
those NOT used to them - but work "as expected" (and self-documenting) for
those who have "grown up" in an IBM COBOL environment.  OBVIOUSLY, such code
is *not* portable to "strictly" ANSI/ISO conforming compilers, but does
provide valid (?) functionality within a "strictly" IBM mainframe
environment.
```

#### ↳ Re: ODO's and "IBM mentality"

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-09T22:54:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee467e1_4@news.athenanews.com>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net>`

```
I disagree vehemently, Bill.

Comments below...

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:bc0ujr$tje$1@slb9.atl.mindspring.net...
> As a follow-up on a different thread, I thought that I would point out two
> IBM "extensions" that deal with ODO's (Occurs Depending On) structures.  I
> know that Micro Focus has an emulation for these; I assume that Realia
does,
> and wouldn't be surprised if others do as well.  I am *not* (necessarily)
> saying that these are "wonderful" constructs - but they are cases where
…[18 more quoted lines elided]…
> This type of "structure" where the nested ODO "floats" within the
containing
> ODO is particularly "useful" for modeling some "real-world" structures.

OK, name one...

Then show how it couldn't be achieved WITHOUT ODO...

> In
> the IBM extension, the maximum STORAGE may be allocated - but the
references
> are to the "user-friendly" (well at least friendly to me <G>) locations.
>

So, you agree the maximum storage is allocated?

Rest my case.

>
> "Feature" 2 -  ODO with following data
…[10 more quoted lines elided]…
> With this IBM extension, the "location" of the data-item After-ODO
"floats"
> within aRec depending on the CURRENT size of Num1.
>

Yes, there WAS a time when we did this. After we realised the horrific code
it generates and recognised how error prone it is , most of us STOPPED doing
it 30 years ago! (And before Doc chimes in with "plural Majestatus est" I
mean "we" in the sense of the group of mainframe programmers I worked with
on various sites throughout the sixties and into the early 70s. By 1973 I
didn't know a single person who would endorse this data structure.)

Even the die-hards who insist on using ODO, for the most part, realise that
the ODO field MUST be the LAST field in the record.

If people are still doing this (and I believe your argument is predicated on
the fact that they are) then it's time SOMEONE pointed out to them the
dangers inherent in doing so and the fact that it isimply isn't NECESSARY.

>     ***
>
> It should be noted that BOTH of these structures are medium-error-prone
for
> those NOT used to them - but work "as expected" (and self-documenting) for
> those who have "grown up" in an IBM COBOL environment.

Bollocks, Bill!

They work "as expected" for anyone who uses them. It doesn't alter the fact
that they are clumsy and inefficient, as well as UNNECESSARY.



>  OBVIOUSLY, such code
> is *not* portable to "strictly" ANSI/ISO conforming compilers, but does
> provide valid (?) functionality within a "strictly" IBM mainframe
> environment.
>

Yes, the functionality is valid but so is GO TO and ALTER.  (These two
constructs are at least efficient, whatever else they may be...).

My point is they are UNNECESSARY. I defy you to show me an instance where
they can do something that standard COBOL definitions cannot.

(Actually, I could forgive them being unnecessary; in COBOL there is usually
more than one way to skin a cat... What REALLY pisses me off about them is
that they lure people into a sense of false security by appearing to be
"clever" when, in fact, all they are is DANGEROUS!.)

OK, I'm calm now...<G>

Pete.
```

##### ↳ ↳ Re: ODO's and "IBM mentality"

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-09T15:17:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Px1Fa.195900$ja4.10382026@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net> <3ee467e1_4@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ee467e1_4@news.athenanews.com...


In general, I agree with your assessment.

I disagree on the issue of allocating storage.
We now have the storage for large tables.
I have changed some of my practices due to the fact that I no longer need to
be a storage miser (both in-core, and DASD).
If it's within reason, I avoid using redefines in records, especially when
numeric, and character data can occupy the same physical area of a record.
I will probably never again write a program to keep the last n records of a
randomly accessed file to improve I/O performance. I will just extract what
I have to keep and store it all in a table.
16 meg will hold over 200,000 80 byte records, enough to store most
transaction files in a table. I've seen programs that store 100 records in a
table, and use DASD to store any overflow. Now, there is no real need to do
so.
The net result is cleaner programs which address business processing without
the overhead and complexity of intermixed storage management.

WAR STORY: I got a chuckle, and the comment "Wow, I've never seen a picture
X eight million before" when I asked someone to review a series of programs.
```

###### ↳ ↳ ↳ Re: ODO's and "IBM mentality"

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-10T11:00:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee511e3_8@news.athenanews.com>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net> <3ee467e1_4@news.athenanews.com> <Px1Fa.195900$ja4.10382026@bgtnsc05-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harley@worldnet.att.net> wrote in message
news:Px1Fa.195900$ja4.10382026@bgtnsc05-news.ops.worldnet.att.net...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[4 more quoted lines elided]…
>
Good <G>!

> I disagree on the issue of allocating storage.

Er...I don't have a position on this so I'm not sure what you are
disagreeing with <G>. I have no problem with people allocating storage,
whatever environment they are working in. I have a problem with them
thinking OCCURS...DEPENDING does this for them.

> We now have the storage for large tables.
> I have changed some of my practices due to the fact that I no longer need
to
> be a storage miser (both in-core, and DASD).
> If it's within reason, I avoid using redefines in records, especially when
> numeric, and character data can occupy the same physical area of a record.
> I will probably never again write a program to keep the last n records of
a
> randomly accessed file to improve I/O performance. I will just extract
what
> I have to keep and store it all in a table.
> 16 meg will hold over 200,000 80 byte records, enough to store most
> transaction files in a table. I've seen programs that store 100 records in
a
> table, and use DASD to store any overflow. Now, there is no real need to
do
> so.
> The net result is cleaner programs which address business processing
without
> the overhead and complexity of intermixed storage management.
>
> WAR STORY: I got a chuckle, and the comment "Wow, I've never seen a
picture
> X eight million before" when I asked someone to review a series of
programs.
>

While this may seem a little "excessive", if your environment supports it
and it makes sense, I would have no problem with people doing what you are
doing. It is no more difficult to understand and maintain than normal COBOL.
(In fact, for you at least, it IS normal COBOL...)

There is one point I would raise on this... Can you be sure that grabbing
huge areas of virtual memory will not have an overall debilitating effect on
other concurrent processes? If you can confidently say "No", then there can
be no objection to it.

Pete.
>
>
>
```

###### ↳ ↳ ↳ Re: ODO's and "IBM mentality"

_(reply depth: 4)_

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-10T00:49:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iW9Fa.116999$cO3.8604385@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net> <3ee467e1_4@news.athenanews.com> <Px1Fa.195900$ja4.10382026@bgtnsc05-news.ops.worldnet.att.net> <3ee511e3_8@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ee511e3_8@news.athenanews.com...
|
| "Harley" <dennis.harley@worldnet.att.net> wrote in message
…[15 more quoted lines elided]…
| thinking OCCURS...DEPENDING does this for them.

No, but it does allocate the maximum storage, and I thought that you thought
that it may be excessive.

|
| > We now have the storage for large tables.
| > I have changed some of my practices due to the fact that I no longer
need
| to
| > be a storage miser (both in-core, and DASD).
| > If it's within reason, I avoid using redefines in records, especially
when
| > numeric, and character data can occupy the same physical area of a
record.
| > I will probably never again write a program to keep the last n records
of
| a
| > randomly accessed file to improve I/O performance. I will just extract
…[3 more quoted lines elided]…
| > transaction files in a table. I've seen programs that store 100 records
in
| a
| > table, and use DASD to store any overflow. Now, there is no real need to
…[14 more quoted lines elided]…
| doing. It is no more difficult to understand and maintain than normal
COBOL.
| (In fact, for you at least, it IS normal COBOL...)

It wasn't "normal" COBOL, it was a cross between applications, and systems
type processing. (the 8 meg thing)
I needed a huge buffer to store variable length records.
It was a learn as you go project.
I did display how much of the buffer was actually being used, planning to
cut it back after I got statistics.
After reviewing the statistics, I figured I had enough storage to handle a
worst case scenario.

|
| There is one point I would raise on this... Can you be sure that grabbing
| huge areas of virtual memory will not have an overall debilitating effect
on
| other concurrent processes? If you can confidently say "No", then there
can
| be no objection to it.

I haven't seen any instances of paging being done in the batch environment
in quite some time. I would assume, probably wrongly, that excessive storage
allocation would  cause some page swapping.

On a CICS project, I contacted the CICS systems programmer, said I would
need 3 meg of storage if I used Temporary Storage Queue processing. He said
not to worry it wasn't a big deal, go ahead and use Temp Storage.

I really don't know how much storage mainframes come with now, but from what
I've seen using a meg or 2 of storage isn't going to slow the system down.
People regularly increase the number of file buffers to speed up processing.
```

##### ↳ ↳ Re: ODO's and "IBM mentality"

- **From:** Patrick Herring <"ph"@$pamblock.anweald.co.uk>
- **Date:** 2003-06-10T12:38:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc4fv6$80h$1@hermes.shef.ac.uk>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net> <3ee467e1_4@news.athenanews.com>`

```
"Peter E.C. Dashwood" wrote:
> 
> I disagree vehemently, Bill.

I agree and disagree.
 
> Comments below...
> 
> "William M. Klein" <wmklein@ix.netcom.com> wrote in message
> news:bc0ujr$tje$1@slb9.atl.mindspring.net...
...
> > "Feature" 2 -  ODO with following data
> >
…[27 more quoted lines elided]…
> simply isn't NECESSARY.

ODO tables are useful, I've found, for variable-length linkage records,
particularly when the calling program is not COBOL and expects to deal
in variable length strings. You have to have a maximum length of course,
and know where the length is recorded so you can first move it to the
ODO number field, but if the called program walks off the end of the
memory set up by the calling program you get a proper exception not a
weird uninitialised storage bug, which is good. I'm not sure how that is
implemented - it implies that the linkage storage isn't addressable
until call time, which makes sense, but also that the COBOL run-unit
knows what storage has been allocated by the calling program, which may
not be in COBOL, which is a bit magical.

Another situation where I've seen ODO used well is in record formats for
variable-length record files - the particular case I recall had wildly
varying lengths and a /lot/ of space would have been wasted, enough to
significantly effect ftp times. But to actually save file space we had
to have just one ODO table and put it at the end, due to the maximum
size being compiled in as Peter points out, so those IBM extensions had
no point there.
```

###### ↳ ↳ ↳ Re: ODO's and "IBM mentality"

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-10T12:44:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0pkFa.161$0v4.14030@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bc0ujr$tje$1@slb9.atl.mindspring.net> <3ee467e1_4@news.athenanews.com> <bc4fv6$80h$1@hermes.shef.ac.uk>`

```

"Patrick Herring" <"ph"@$pamblock.anweald.co.uk> wrote in message
news:bc4fv6$80h$1@hermes.shef.ac.uk...
| "Peter E.C. Dashwood" wrote:
| >

|
| Another situation where I've seen ODO used well is in record formats for
…[6 more quoted lines elided]…
|

Another option is to use the RECORD IS VARYING DEPENDING ON, FD
specification.
A Working-Storage (or Linkage Section) variable is used to store the length.
of the record.
Reads update the length, writes use the length.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
