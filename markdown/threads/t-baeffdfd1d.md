[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mf Variable File Formats

_17 messages · 11 participants · 1999-12_

---

### mf Variable File Formats

- **From:** "Lou de Freitas" <Luiz.deFreitas@dol.net>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<385a6113.0@news.dol.net>`

```
With a MF created executable, I am having a problem creating a variable
length file defined by the use of occurs x times depending on y within the
fields that define the 01 level of the record.  The problem is that the
records are created with the max size even though the occurs depending on
has a value less than the max.  I confirmed this by viewing the created file
in hex and confirmed that this is a problem.

Anyone have a work around until MF gets me a corrected compiler?

Does it on WB  (W95) and Unix (Sun Solaris) versions of MF.

Thanks,

Lou
```

#### ↳ Re: mf Variable File Formats

- **From:** E. Johnson <elizrj@my-deja.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83dvuj$4cu$1@nnrp1.deja.com>`
- **References:** `<385a6113.0@news.dol.net>`

```
Hey Lou

I had this same problem.  I was trying to keep varying sized notes out
for various things on our Win95 POS system.  Then I realized I had set
up the FD wrong.  Here's what I had originally:

       FD NOTES
       01 NOTES-REC.
           03 NOTE-KEY.
               05 NOTE-TYPE                PIC X.
               05 NOTE-2-TYPE              PIC X(03).
               05 NOTE-NUMBER              PIC X(10).
           03 NOTE-FIELD.
               05 NOTE-ARRAY               OCCURS 1 TO 2000 TIMES
                                             DEPENDING ON NOTE-LENGTH.
                   07 NOTE-CHAR            PIC X.
           03 NOTE-LENGTH                  PIC 9(4).
           03 NOTE-REC-LENGTH              PIC 9(4).

But it was missing a statement.  Here's what worked:

       FD NOTES
               RECORD IS VARYING IN SIZE
                   FROM 19 TO 2018 CHARACTERS
                   DEPENDING ON NOTE-REC-LENGTH.
       01 NOTES-REC.
          .......... etc. .......

If you don't include that clause, the system will write the max length
out for each record.  Give it a shot.  Of course I may have done it
wrong, but then I do most things wrong and somehow get them to work in
spite of it ;)

Elizabeth


In article <385a6113.0@news.dol.net>,
  "Lou de Freitas" <Luiz.deFreitas@dol.net> wrote:
> With a MF created executable, I am having a problem creating a
variable
> length file defined by the use of occurs x times depending on y
within the
> fields that define the 01 level of the record.  The problem is that
the
> records are created with the max size even though the occurs
depending on
> has a value less than the max.  I confirmed this by viewing the
created file
> in hex and confirmed that this is a problem.
>
…[8 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: mf Variable File Formats

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<385A94FA.778C0C83@home.com>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com>`

```


"E. Johnson" wrote:
> 
> Hey Lou
…[31 more quoted lines elided]…
> 
Elizabeth,

I was interested in your example because it covers an area I've queried
before. My record has a max-table of 10 x 24. Under ideal conditions I
would like records to expand to the maximum or contract to what is
currently required. I think with what you've illustrated, you've set the
size for notes to be currently what you are outputting.

Question - do you ever read those notes in and increase/decrease their
size ? From some responses I got, it looks like it could be tricky. The
nearest I've gotten to-date is to use Micro Focus data compression. And
unless there is a concise technique, I really don't want to mess around 
playing suck-it-and-see and screw-up my datafiles in the process !

Jimmy, Calgary AB
```

##### ↳ ↳ Re: mf Variable File Formats

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83e62q$i4k$1@aklobs.kc.net.nz>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com>`

```
In comp.lang.cobol E. Johnson <elizrj@my-deja.com> wrote:

:        FD NOTES
:        01 NOTES-REC.
:            03 NOTE-KEY.
:                05 NOTE-TYPE                PIC X.
:                05 NOTE-2-TYPE              PIC X(03).
:                05 NOTE-NUMBER              PIC X(10).
:            03 NOTE-FIELD.
:                05 NOTE-ARRAY               OCCURS 1 TO 2000 TIMES
:                                              DEPENDING ON NOTE-LENGTH.
:                    07 NOTE-CHAR            PIC X.
:            03 NOTE-LENGTH                  PIC 9(4).
:            03 NOTE-REC-LENGTH              PIC 9(4).

: But it was missing a statement.  Here's what worked:

:        FD NOTES
:                RECORD IS VARYING IN SIZE
:                    FROM 19 TO 2018 CHARACTERS
:                    DEPENDING ON NOTE-REC-LENGTH.
:        01 NOTES-REC.
:           .......... etc. .......

How could that _possibly_ work ?

The length field follows the varying part.  It needs to know 
the length of the array/record before it can find where the
field is that tells it the length.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz>`

```

Richard Plinston wrote
>
> How could that _possibly_ work ?
…[3 more quoted lines elided]…
> field is that tells it the length.

It can't.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 4)_

- **From:** E. Johnson <elizrj@my-deja.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83qtb4$pro$1@nnrp1.deja.com>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net>`

```
In article <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net>,
  "Jerry P" <bismail@bisusa.com> wrote:
>
> Richard Plinston wrote
…[9 more quoted lines elided]…
>

So glad you two informed me that this won't work.  I would have gone on
using it with no problems showing up for yet another 2 years.  God,
what would I have told my users?? Just because it LOOKS like it works,
and ACTS like it works, doesn't mean it really works so I have to take
it out of the code until it conforms to something other people say
should work.  WHEW!  Big relief for me.

Seriously tho, I use this in many places.  It holds various notes for
customers, vendors, orders, etc.  It is a dynamic file indexed to the
customer code, the vendor code, the order number, etc.  In 2 years, I
have had absolutely no problems with it ... unless you count the first
couple weeks of installation when I didn't include the varying phrase
and it grew to 6 meg.  After correcting that, the file remains at about
1 meg after 2 years.

There is some finagling (sp?) you have to do to get the notes into and
out of the array.  And since I use dialog, I use a panels call to move
the notes to and from the note field.  All in all it works pretty
simply with only about 13 lines of code.

Sheesh guys, I'm not an expert or anything.  I can't tell you cobol
standards and quote textbook examples of logistical code.  I can,
however, tell when something works or not.  Please give me a little
credit ... but not a lot cause I may get a swelled head and demand a
raise.

~Elizabeth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 5)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<FKd84.19$ix6.1235@nnrp3.rcsntx.swbell.net>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net> <83qtb4$pro$1@nnrp1.deja.com>`

```
At issue:
.
FD NOTES
       01 xxx.
           03 yyy.
               05 aaa                                PIC X.
               05 bbb                                PIC X(03).
               05 ccc                                 PIC X(10).
           03 ddd.
               05 NOTE-ARRAY               OCCURS 1 TO 2000 TIMES
                                             DEPENDING ON NOTE-LENGTH.
                   07 NOTE-CHAR            PIC X.
           03 NOTE-LENGTH                  PIC 9(4).
           03 NOTE-REC-LENGTH              PIC 9(4).


RECORD VARYING FROM integer-5 TO integer-6 DEPENDING ON data-name-1

"DEPENDING ON  - If this phrase is present, you must store in
data-name-1 the size of the record before any WRITE or REWRITE
operation on the file. After any successful READ operation,
data-name-1 contains the size of the record just read. Data-name-1
must be an unsigned integer data item defined in the Working-Storage
section."

I think I've found a way in which your code could work.

Since your compiler does not flag NOTE-LENGTH as being absent from
Working Storage (my compiler generates an E-Level diagnostic with the
above code), I assume your compiler is reserving space for maximum
record lengths (as if NOTE-ARRAY were defined in Working Storage).
If that is the case, you are not getting variable length records, they
just seem like it.

Whatever seems to 'work' is guaranteed to fail on a more conforming
compiler.

E. Johnson <elizrj@my-deja.com> wrote in message
news:83qtb4$pro$1@nnrp1.deja.com...
> In article <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net>,
>   "Jerry P" <bismail@bisusa.com> wrote:
…[13 more quoted lines elided]…
> So glad you two informed me that this won't work.  I would have gone
on
> using it with no problems showing up for yet another 2 years.  God,
> what would I have told my users?? Just because it LOOKS like it
works,
> and ACTS like it works, doesn't mean it really works so I have to
take
> it out of the code until it conforms to something other people say
> should work.  WHEW!  Big relief for me.
>
> Seriously tho, I use this in many places.  It holds various notes
for
> customers, vendors, orders, etc.  It is a dynamic file indexed to
the
> customer code, the vendor code, the order number, etc.  In 2 years,
I
> have had absolutely no problems with it ... unless you count the
first
> couple weeks of installation when I didn't include the varying
phrase
> and it grew to 6 meg.  After correcting that, the file remains at
about
> 1 meg after 2 years.
>
> There is some finagling (sp?) you have to do to get the notes into
and
> out of the array.  And since I use dialog, I use a panels call to
move
> the notes to and from the note field.  All in all it works pretty
> simply with only about 13 lines of code.
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83ru12$26m$1@nntp4.atl.mindspring.net>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net> <83qtb4$pro$1@nnrp1.deja.com> <FKd84.19$ix6.1235@nnrp3.rcsntx.swbell.net>`

```
One more time,
  PLEASE look at using the following type of code INSTEAD


  FD NOTES
        Record Varying in Size from 23 to 2022
           Depending on WS-File Size
      .
         01 xxx.
             03 yyy.
                  05 aaa                                PIC X.
                  05 bbb                                PIC X(03).
                  05 ccc                                 PIC X(10).
              03 ddd.
                  05 NOTE-ARRAY               OCCURS 1 TO 2000 TIMES
                                              DEPENDING ON NOTE-LENGTH.
                      07 NOTE-CHAR            PIC X.
              03 NOTE-LENGTH                PIC 9(4).
              03 NOTE-REC-LENGTH       PIC 9(4).

    ....

Working-Storage Section.
   ...
01  WS-File-Size Pic 9(04).

  ...

Then MOVE the length of each file to be written to WS-File-Size before doing
your WRITE statement.  After each READ WS-File-Size will contain the size of
the record that was read.

I have NOT changed the location of NOTE-LENGTH, but unless you really have a
system that can handle that, I *strongly* recommend that you put the "object
of the ODO" *before* the ODO itself - and not after it.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 7)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<848odk$jt6$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net> <83qtb4$pro$1@nnrp1.deja.com> <FKd84.19$ix6.1235@nnrp3.rcsntx.swbell.net> <83ru12$26m$1@nntp4.atl.mindspring.net>`

```
    With MF cobol, this code should work just fine so long as you avoid the
ODOSLIDE compiler directive.
Without this directive (the default), NOTE-LENGTH would be placed after a
FULL length array.

    With ODOSLIDE, this arrangement might be unusable.

    Sorry about delay - thought that Outlook would
send it automatically.


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:83ru12$26m$1@nntp4.atl.mindspring.net...
> One more time,
>   PLEASE look at using the following type of code INSTEAD
…[26 more quoted lines elided]…
> Then MOVE the length of each file to be written to WS-File-Size before
doing
> your WRITE statement.  After each READ WS-File-Size will contain the size
of
> the record that was read.
>
> I have NOT changed the location of NOTE-LENGTH, but unless you really have
a
> system that can handle that, I *strongly* recommend that you put the
"object
> of the ODO" *before* the ODO itself - and not after it.
>
…[106 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83u2fc$1e9$1@nnrp1.deja.com>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net> <83qtb4$pro$1@nnrp1.deja.com>`

```
In article <83qtb4$pro$1@nnrp1.deja.com>,
  E. Johnson <elizrj@my-deja.com> wrote:
> > >
> > > How could that _possibly_ work ?
>
> So glad you two informed me that this won't work.  I would have gone
on
> using it with no problems showing up for yet another 2 years.  God,
> what would I have told my users?? Just because it LOOKS like it
works,
> and ACTS like it works, doesn't mean it really works so I have to
take
> it out of the code until it conforms to something other people say
> should work.  WHEW!  Big relief for me.

I may be instructive (for you) to examine what of this code _does_ work
and what does _not_ work.

You have a varying record containing a varying array followed by the
array size and then the record size.

The compiler should object to this, the fact that it does not does not
mean that the code is correct, only that _this_ compiler doesn't care.

The program will be treating the twoi length fields as if they were in
Working-Storage.  That is the record will be written out to the length
specified, and when the record is read the _system_ will be setting the
length read.  The two lengths will not, however, be written out as part
of the actual record.  These two lenths are in character positions
2000+ of the record.  When a record is written (assuming lengths are
set expecting the fields to be written) then the record will contain
the initial data, the text in the array and the next 8 bytes of the
array and _not_ the lengths.

When the record is read back in the record length will be set as for
any variable record even if this length was in (as it is supposed to
be) Working-Storage.  The text array length will _not_ be set as it
is outside the record size (except with a 2022 sized record).  You are
probably recalculating the array size from the record size after each
read and never knew why this was often wrong.

So what is _not_ working is the array length is not being written, the
record length is not being written (but is recreated), you are wasting
8 bytes on every record and are having to recalulate the array length.

You are also risking a new compiler forcing you to recode and
restructure the file.

>
> Sheesh guys, I'm not an expert or anything.  I can't tell you cobol
> standards and quote textbook examples of logistical code.

I had noticed.

>  I can,
> however, tell when something works or not.

Obviously not.  have you actually looked at the data file itself and
noticed the last 8 bytes of every record is rubbish left over from a
previous record ?


> Please give me a little
> credit ... but not a lot cause I may get a swelled head and demand a
> raise.

I don't think that you risk that.  You appear to program by 'trial and
error', with the emphasis on the 'error'.  This is a poor approach that
is expensive and time consuming.  What is even more worrying is that
you seem to think that the code is actually 'working' and have no idea
what parts are or are not or why.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<386A9ECB.BE6EEA04@zip.com.au>`
- **References:** `<385a6113.0@news.dol.net> <83dvuj$4cu$1@nnrp1.deja.com> <83e62q$i4k$1@aklobs.kc.net.nz> <DlC64.2151$M34.23809@nnrp1.rcsntx.swbell.net> <83qtb4$pro$1@nnrp1.deja.com> <83u2fc$1e9$1@nnrp1.deja.com>`

```
riplin@kcbbs.gen.nz wrote:
> 
> > Please give me a little
…[7 more quoted lines elided]…
> what parts are or are not or why.

Look up pragmatic programmer 
http://www.pragmaticprogrammer.com/ppbook/.  Look up the section
programming by accident.  

This book is on my 'to be purchased list'.  Please take a look at the
samples, good stuff from the web site.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: mf Variable File Formats

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83drsd$sod$1@nntp4.atl.mindspring.net>`
- **References:** `<385a6113.0@news.dol.net>`

```
Rather than RECORD CONTAINS, use the (new with '85 Standard) RECORD VARYING
IN SIZE DEPENDING ON option in your FD.  It will require you to put the
size-to-be-written into a working-storage field, but should (I think) solve
your problem.
```

#### ↳ Re: mf Variable File Formats

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<XqD64.9436$o97.85846@news3.mia>`
- **References:** `<385a6113.0@news.dol.net>`

```
Repost with the Select and FD stmts.

Lou de Freitas <Luiz.deFreitas@dol.net> wrote in message
news:385a6113.0@news.dol.net...
> With a MF created executable, I am having a problem creating a variable
> length file defined by the use of occurs x times depending on y within the
> fields that define the 01 level of the record.  The problem is that the
> records are created with the max size even though the occurs depending on
> has a value less than the max.  I confirmed this by viewing the created
file
> in hex and confirmed that this is a problem.
>
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: mf Variable File Formats

- **From:** "Lou de Freitas" <Luiz.deFreitas@dol.net>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<385b7392.0@news.dol.net>`
- **References:** `<385a6113.0@news.dol.net> <XqD64.9436$o97.85846@news3.mia>`

```
This var file has only one occurs depending on sections in the record and it
always gets greated with the max size of 560

          SELECT NAME-ADDR-OUTFILE        ASSIGN TO
          'vfcreat2.dat'
                               ORGANIZATION IS SEQUENTIAL.

       DATA DIVVARON.
       FILE SECTION.

       FD  NAME-ADDR-OUTFILE
           RECORDING MODE IS V
           LABEL RECORDS ARE STANDARD
           RECORD IS VARYING IN SIZE FROM 144 TO 560
           DATA RECORD IS VAR-LOAD.
       01 VAR-LOAD.
          02 VAR-INPUT-REC.
             03 VAR-SERIAL-NBR                   PIC 9(9).
             03 VAR-DATA-FOR-COUNTRY             PIC X(3).
             03 VAR-LANGUAGE                     PIC 9(3).
             03 VAR-INSTITUTION                  PIC X(4).
             03 VAR-LOCATION-NO                  PIC X(12).
             03 VAR-ACCT-KEY.
                04 VAR-PROD-CODE                 PIC X(5).
                04 VAR-PLAN-CODE                 PIC X(5).
                04 VAR-ACCT-NBR                  PIC X(30).
             03 VAR-CIF-KEY-DSPLY                PIC X(20).
             03 VAR-CIF-KEY-BINARY               PIC X(20).
             03 VAR-SSEID-NBR                    PIC 9(15).
             03 VAR-SSEID-XREF-LINE              PIC 9(2).
             03 VAR-DATE-PROCESSED.
                04 VAR-DATE-PROC-YYYY            PIC 9(4).
                04 VAR-DATE-PROC-MM              PIC 9(2).
                04 VAR-DATE-PROC-DD              PIC 9(2).
             03 VAR-CHANGE-OR-DELETE-SW          PIC X.
                88 VAR-IS-A-CHANGE                       VALUE 'C'.
                88 VAR-IS-A-DELETE                       VALUE 'D'.
                88 VAR-IS-A-ADD                          VALUE 'A'.
                88 VAR-IS-A-SCRUB                        VALUE 'S'.
             03 VAR-RECTYPE                      PIC X.
             03 VAR-NBR-LINES-IN                 PIC 9(2).
             03 VAR-NBR-LINES-OUT                PIC 9(2).
             03 VAR-LINES.
                04 VAR-NAME-ADDR-INFO
                   OCCURS 0 TO 8 TIMES
                   DEPENDING ON VAR-NBR-LINES-IN.
                   05 VAR-NAME-ADDR.
                      06 VAR-1CHAR               PIC X.
                      06 VAR-RMNG                PIC X(49).
                   05 VAR-LINE-CODE              PIC X.
                   05 VAR-SEX-CODE               PIC X.
             03 VAR-CRLF                        PIC X(2).

This var file has two occurs depending on sections and it always gets
created with max size of 4466.
          SELECT NAME-ADDR-OUTFILE        ASSIGN TO
          'vfcreate.dat'
                               ORGANIZATION IS SEQUENTIAL.

       FD  NAME-ADDR-OUTFILE
           RECORDING MODE IS V
           LABEL RECORDS ARE STANDARD
           RECORD IS VARYING IN SIZE FROM 144 TO 4466.
       01 VAR-LOAD.
          02 VAR-INPUT-REC.
             03 VAR-SERIAL-NBR                   PIC 9(9).
             03 VAR-DATA-FOR-COUNTRY             PIC X(3).
             03 VAR-LANGUAGE                     PIC 9(3).
             03 VAR-INSTITUTION                  PIC X(4).
             03 VAR-LOCATION-NO                  PIC X(12).
             03 VAR-ACCT-KEY.
                04 VAR-PROD-CODE                 PIC X(5).
                04 VAR-PLAN-CODE                 PIC X(5).
                04 VAR-ACCT-NBR                  PIC X(30).
             03 VAR-CIF-KEY-DSPLY                PIC X(20).
             03 VAR-CIF-KEY-BINARY               PIC X(20).
             03 VAR-SSEID-NBR                    PIC 9(15).
             03 VAR-SSEID-XREF-LINE              PIC 9(2).
             03 VAR-DATE-PROCESSED.
                04 VAR-DATE-PROC-YYYY            PIC 9(4).
                04 VAR-DATE-PROC-MM              PIC 9(2).
                04 VAR-DATE-PROC-DD              PIC 9(2).
             03 VAR-CHANGE-OR-DELETE-SW          PIC X.
                88 VAR-IS-A-CHANGE                       VALUE 'C'.
                88 VAR-IS-A-DELETE                       VALUE 'D'.
                88 VAR-IS-A-ADD                          VALUE 'A'.
                88 VAR-IS-A-SCRUB                        VALUE 'S'.
             03 VAR-RECTYPE                      PIC X.
             03 VAR-NBR-LINES-IN                 PIC 9(2).
             03 VAR-NBR-LINES-OUT                PIC 9(2).
             03 VAR-LINES.
                04 VAR-NAME-ADDR-INFO
                   OCCURS 0 TO 8 TIMES
                   DEPENDING ON VAR-NBR-LINES-IN.
                   05 VAR-NAME-ADDR.
                      06 VAR-1CHAR               PIC X.
                      06 VAR-RMNG                PIC X(49).
                   05 VAR-LINE-CODE              PIC X.
                   05 VAR-SEX-CODE               PIC X.
             03 OUTPUT-VAR-LINES.
                04 VAR-OUTPUT-LINES
                   OCCURS 0 TO 14 TIMES
                   DEPENDING ON VAR-NBR-LINES-OUT.
                   05 VAR-OUT-LINES.
                      06 VAR-OUT-ERROR             PIC X(16).
                      06 VAR-OUT-TYPE              PIC X.
                      06 VAR-OUT-ID-SW             PIC X.
                      06 VAR-IN-XREF-NBR           PIC 9(2).
                      06 VAR-OUT-LINE              PIC X(259).
                      06 VAR-OUT-LINE-NA REDEFINES VAR-OUT-LINE.
                          07 VAR-NAME-LINE         PIC X(50).
                          07 VAR-LINE.
                             08 VAR-FIRST          PIC X(30).
                             08 VAR-SURN           PIC X(30).
                          07 VAR-APP-PRE-CODE      PIC 9(3).
                          07 VAR-APP-PRE           PIC X(16).
                          07 VAR-TITLE-CODE        PIC 9(3).
                          07 VAR-TITLE             PIC X(16).
                          07 VAR-CONJ-CODE         PIC 9(3).
                          07 VAR-CONJ              PIC X(16).
                          07 VAR-SUFF-CODE         PIC 9(3).
                          07 VAR-SUFF              PIC X(16).
                          07 VAR-CV-APP-CODE       PIC 9(3).
                          07 VAR-CV-APP            PIC X(16).
                          07 VAR-BK-APP-CODE       PIC 9(3).
                          07 VAR-BK-APP            PIC X(16).
                          07 VAR-SEX               PIC X.
                          07 VAR-SUMM2             PIC X(30).
                          07 FILLER                PIC X(4).
                      06 VAR-STREET-INFO REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-STREET-LINE       PIC X(50).
                          07 VAR-STREET-NAME       PIC X(40).
                          07 VAR-HOUSE-NBR         PIC X(10).
                          07 VAR-FRAC              PIC X(5).
                          07 VAR-APT-NBR           PIC X(5).
                          07 VAR-BOX-NBR           PIC X(5).
                          07 VAR-RURAL-NBR         PIC X(5).
                          07 VAR-BLDG-NBR          PIC X(5).
                          07 VAR-PRE-DIR-CODE      PIC 9(3).
                          07 VAR-PRE-DIR           PIC X(16).
                          07 VAR-POSTDIR-CODE      PIC 9(3).
                          07 VAR-POSTDIR           PIC X(16).
                          07 VAR-APT-CODE          PIC 9(3).
                          07 VAR-APT               PIC X(16).
                          07 VAR-BOX-CODE          PIC 9(3).
                          07 VAR-BOX               PIC X(16).
                          07 VAR-RURAL-CODE        PIC 9(3).
                          07 VAR-RURAL             PIC X(16).
                          07 VAR-BLDG-CODE         PIC 9(3).
                          07 VAR-BLDG              PIC X(16).
                          07 FILLER                PIC X(20).
                      06 VAR-CITY-INFO REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-CITY-LINE         PIC X(50).
                          07 VAR-CITY-NAME         PIC X(40).
                          07 VAR-STATE             PIC X(16).
                          07 VAR-ZIP-CODE.
                             08 VAR-ZIP-1          PIC X(10).
                             08 VAR-ZIP-2          PIC X(10).
                          07 VAR-COUNTRY-CODE      PIC 9(3).
                          07 VAR-COUNTRY           PIC X(40).
                          07 FILLER                PIC X(90).
                      06 VAR-DESC-INFO REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-DESC-LINE         PIC X(50).
                          07 VAR-DESC-CODES        PIC X(24).
                          07 VAR-DESC-TABLE REDEFINES
                             VAR-DESC-CODES.
                             08 VAR-D-OCCURS
                                OCCURS 8 TIMES
                                INDEXED BY VAR-DESC-IDX.
                                09 VAR-DESC-CODE   PIC 9(3).
                          07 FILLER                PIC X(185).
                      06 VAR-ORIG-AREA REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-ORIG-LINE          PIC X(50).
                          07 VAR-ORIG-NAME1         PIC X(30).
                          07 VAR-ORIG-NAME2         PIC X(30).
                          07 FILLER                 PIC X(57).
                          07 VAR-ORIG-CODES         PIC X(36).
                          07 VAR-ORIG-TABLE REDEFINES
                             VAR-ORIG-CODES.
                             08 VAR-ORIG-OCCURS
                                OCCURS 12 TIMES
                                INDEXED BY VAR-ORIG-IDX.
                                09 VAR-ORIG-CODE    PIC 9(3).
                          07 FILLER                 PIC X(21).
                          07 VAR-ORIG-GENDER        PIC X.
                          07 VAR-ORIG-NAME3         PIC X(30).
                          07 FILLER                 PIC X(4).
                      06 VAR-COMMENTS-AREA REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-COMMENTS-SW       PIC X.
                          07 VAR-COMMENTS          PIC X(70).
                          07 VAR-X7-SW             PIC XX.
                          07 VAR-EXTRA-LINE7       PIC X(48).
                          07 VAR-X8-SW             PIC XX.
                          07 VAR-EXTRA-LINE8       PIC X(48).
                          07 VAR-BATCH             PIC X(7).
                          07 VAR-BATCH-STATUS      PIC X.
                          07 FILLER                PIC X(80).
                      06 VAR-USER-AREA REDEFINES
                         VAR-OUT-LINE.
                          07 VAR-X9-SW             PIC XX.
                          07 EXTRA-LINE9           PIC X(48).
                          07 VAR-X10-SW            PIC XX.
                          07 VAR-EXTRA-LINE10      PIC X(48).
                          07 FILLER                PIC X(159).
                03 VAR-CRLF                        PIC X(2).

James King <mangogwr@bellsouth.net> wrote in message
news:XqD64.9436$o97.85846@news3.mia...
> Repost with the Select and FD stmts.
>
…[3 more quoted lines elided]…
> > length file defined by the use of occurs x times depending on y within
the
> > fields that define the 01 level of the record.  The problem is that the
> > records are created with the max size even though the occurs depending
on
> > has a value less than the max.  I confirmed this by viewing the created
> file
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83fo9i$e0r$1@news.hitter.net>`
- **References:** `<385a6113.0@news.dol.net> <XqD64.9436$o97.85846@news3.mia> <385b7392.0@news.dol.net>`

```
Having  VAR-CRLF at the end of the record descriptions
makes the length of these records fixed due to the ANS
rules for ODO. (But see below for using ODOSLIDE.)

For the first record description, decrease the minimum and
maximum sizes by 2 and eliminate VAR-CRLF and the
record will be variable.

For the second record description, do the same as above;
but note that the record will be variable based upon the
second ODO, the first ODO will always have 8 slots
allocated.

If the proper precautions have been taken for moving data
into the both records, and every other ODO in the programs
that use these files, you could use the ODOSLIDE compiler
directive. This directive causes ODO to behave as in older
IBM mainframe compilers.

Also get rid of the RECORDING MODE IS V. RECORD IS
VARYING is the ANS 85 replacement for RECORDING MODE.
------------------
Rick Smith

Lou de Freitas wrote in message <385b7392.0@news.dol.net>...
>This var file has only one occurs depending on sections in the record and
it
>always gets greated with the max size of 560
[...]
>       FD  NAME-ADDR-OUTFILE
>           RECORDING MODE IS V
…[4 more quoted lines elided]…
>          02 VAR-INPUT-REC.
[...]
>             03 VAR-NBR-LINES-IN                 PIC 9(2).
>             03 VAR-NBR-LINES-OUT                PIC 9(2).
…[3 more quoted lines elided]…
>                   DEPENDING ON VAR-NBR-LINES-IN.
[...]
>             03 VAR-CRLF                        PIC X(2).
>
>This var file has two occurs depending on sections and it always gets
>created with max size of 4466.
[...]
>       FD  NAME-ADDR-OUTFILE
>           RECORDING MODE IS V
…[3 more quoted lines elided]…
>          02 VAR-INPUT-REC.
[...]
>             03 VAR-NBR-LINES-IN                 PIC 9(2).
>             03 VAR-NBR-LINES-OUT                PIC 9(2).
…[3 more quoted lines elided]…
>                   DEPENDING ON VAR-NBR-LINES-IN.
[...]
>             03 OUTPUT-VAR-LINES.
>                04 VAR-OUTPUT-LINES
>                   OCCURS 0 TO 14 TIMES
>                   DEPENDING ON VAR-NBR-LINES-OUT.
[...]
>                03 VAR-CRLF                        PIC X(2).
>
…[18 more quoted lines elided]…
>> > Does it on WB  (W95) and Unix (Sun Solaris) versions of MF.
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 4)_

- **From:** "Frank Lucivero" <nitesun@goes.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<38697716@news.goes.com>`
- **References:** `<385a6113.0@news.dol.net> <XqD64.9436$o97.85846@news3.mia> <385b7392.0@news.dol.net> <83fo9i$e0r$1@news.hitter.net>`

```
frankres@goes.com     OUTSTANDING OPPORTUNITIES IN NY/NJ   $$$$$$$$$$

"Rick Smith" <ricksmith@aiservices.com> wrote in message
news:83fo9i$e0r$1@news.hitter.net...
> Having  VAR-CRLF at the end of the record descriptions
> makes the length of these records fixed due to the ANS
…[74 more quoted lines elided]…
> >> > With a MF created executable, I am having a problem creating a
variable
> >> > length file defined by the use of occurs x times depending on y
within
> >the
> >> > fields that define the 01 level of the record.  The problem is that
the
> >> > records are created with the max size even though the occurs
depending
> >on
> >> > has a value less than the max.  I confirmed this by viewing the
created
> >> file
> >> > in hex and confirmed that this is a problem.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: mf Variable File Formats

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<84c2jl$cqd$1@nntp5.atl.mindspring.net>`
- **References:** `<385a6113.0@news.dol.net> <XqD64.9436$o97.85846@news3.mia> <385b7392.0@news.dol.net> <83fo9i$e0r$1@news.hitter.net> <38697716@news.goes.com>`

```
I started to "reply" to this person - who responded with these NON-response
posts to the NG - however, having looked at his "name" - I assume this is a
TRULY OBNOXIOUS form of a "troll"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
