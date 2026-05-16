[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I have a question: How can this work?

_7 messages · 7 participants · 1999-09_

---

### I have a question: How can this work?

- **From:** "john smith" <someone@microsoft.com>
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com>`

```
New to COBOL
I know this MUST happen everyday, but I'm lost as to an approach.
I designing a program that will take a file that has batches of records in
it.
There is 2 header records with each batch they help to define whats in the
batch, there is no trailer, I guess the 2nd header acts like a trailer.
Each Header has 80 bytes. the difference is the first three bytes are
either:
    '$NE' 1st header or '777' 2nd Header
The record types in the batch are all of the same type.
Each batch can have a different record type with a piecing of the record in.
    Here are the types with the length which IS the 1st 3 bytes.
             Type                 Lng   3-Bytes
          SpecialRec-Hdr  111  '111'
          SpecialRec-Dtl    087 '087'
          SpecialRec-Tlr    077 '077'

          NormalRec1-Hdr 114 '114'
          NormalRec1-Trl   090 '090'

there are two more normal recs with header and trailer that use codes in the
header2 to differentiate them with exactly the same length and 1st three
bytes as NormalRec1, ie.  NormalRec2, NormalRec3.

I cant understand how to process a batch that I wouldnt know how big it
could get, so I dont want to use a table of letsay 10000 occurs.
That would really eat up memory I think.

When I think this through, maybe my ignorance of how COBOL does things will
show through.
I define the records -ALL as TYPE  PIC X(03) and FILLER PIC X(111) to fit
all in one place with the largest size.

I will open the file
read the first record.
Run a routine  to check the first three bytes.
that sets a high-value of some constant, HEADER1-Y if 1st 3 bytes is $NE
Move that to working storage defined with Header1 and all its details.

that sets a high-value of some constant HEADER2-y if 1st 3 bytes is 777
Move that to working storage defined with Header2 and all its details.

that sets a high-value of some constant SpecialRecHdr-y if 1st 3 bytes is
111
Move that to working storage defined with SpecialRecHdr and all its details.

that sets a high-value of some constant SpecialRecDtl-y if 1st 3 bytes is
087
Move that to working storage defined with SpecialRecDtl1 and all its
details.

that sets a high-value of some constant SpecialRecTrl-y if 1st 3 bytes is
077
Move that to working storage defined with SpecialRecTrl and all its details.

that sets a high-value of some constant NormalRecHdr-y if 1st 3 bytes is 114
check working storage of header 2 for magic byte that is normalRec 1,2,3
Move that to working storage defined with NormalRecHdr1 2 or 3 as
appropriate and all its details.

that sets a high-value of some constant NormalRecTrl-y if 1st 3 bytes is 090
check working storage of header 2 for magic byte that is normalRec 1,2,3
Move that to working storage defined with NormalRecTlr1 2 or 3 as
appropriate and all its details.


If none of the above move it to an error-file as is.

I think that should work, however I get really baffled when I must DO
something with this batch.  I cant seem to figure out when to write the
record to my output.  I dont want to write the batch unless the header info
validates what is in the batch.  It could have gotten botched up in
transmission, and merged two batches together or something ugly like that.

I have seen reports that say batch so and so is invalid, using sums and
things from a header and trailer and puts the whole thing out in a report,
and file so it can be fixed and included in the next cycle. That is a smart
thing.
I just wonder how to find the whole batch if i've already read it and wrote
it out and changed it , without keeping the whole thing in memory somewhere.

oh i am so confused.
I dont want huge amounts of memory and I dont want bad batches.
any advice.
Thank you
```

#### ↳ Re: I have a question: How can this work?

- **From:** "gee" <grant_englebrecht@nospam.compuware.com>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37e6c062@199.186.16.51>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com>`

```
what is the sequence the records appear in
if you only have
hdr1
hdr2
btch dtl
btch dtl
btch dtl
hdr1
hdr2
btch dtl
btch dtl
btch dtl

then there is no need to store any records.
you only need to store the info from the hdrs to verify batch totals
eg
hdr1-flag = n
hdr2-flag = n

read rec
perform until eof
   if hdr1 then hdr1-flag = y
   elseif hdr2 then hdr2-flag = y
     elseif btch-dtl then
          if hdr1-flag = 'y' and hdr2-flag = y then
            perform process-batch until next hdr or eof
            if hdr1 or hdr2
               verify totals for batch
            endif
            hdr1-flag = n
            hdr2-flag = n
       else
         say rec seq error
        stop
       endif
   endif
 endif

if not eof then
   read rec
endif

sub process-batch
 verify batch rec
 store info
  read rec.
endsub


john smith wrote in message ...
>New to COBOL
>I know this MUST happen everyday, but I'm lost as to an approach.
…[8 more quoted lines elided]…
>Each batch can have a different record type with a piecing of the record
in.
>    Here are the types with the length which IS the 1st 3 bytes.
>             Type                 Lng   3-Bytes
…[7 more quoted lines elided]…
>there are two more normal recs with header and trailer that use codes in
the
>header2 to differentiate them with exactly the same length and 1st three
>bytes as NormalRec1, ie.  NormalRec2, NormalRec3.
…[21 more quoted lines elided]…
>Move that to working storage defined with SpecialRecHdr and all its
details.
>
>that sets a high-value of some constant SpecialRecDtl-y if 1st 3 bytes is
…[6 more quoted lines elided]…
>Move that to working storage defined with SpecialRecTrl and all its
details.
>
>that sets a high-value of some constant NormalRecHdr-y if 1st 3 bytes is
114
>check working storage of header 2 for magic byte that is normalRec 1,2,3
>Move that to working storage defined with NormalRecHdr1 2 or 3 as
>appropriate and all its details.
>
>that sets a high-value of some constant NormalRecTrl-y if 1st 3 bytes is
090
>check working storage of header 2 for magic byte that is normalRec 1,2,3
>Move that to working storage defined with NormalRecTlr1 2 or 3 as
…[16 more quoted lines elided]…
>it out and changed it , without keeping the whole thing in memory
somewhere.
>
>oh i am so confused.
…[5 more quoted lines elided]…
>
```

#### ↳ Re: I have a question: How can this work?

- **From:** john_mindock@my-deja.com
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s85uq$e2l$1@nnrp1.deja.com>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com>`

```
In article <uIPE3.54332$223.832212@typ12.nn.bcandid.com>,
  "john smith" <someone@microsoft.com> wrote:
> New to COBOL
> I know this MUST happen everyday, but I'm lost as to an approach.
> I designing a program that will take a file that has batches of
records in
> it.
> There is 2 header records with each batch they help to define whats
in the
> batch, there is no trailer, I guess the 2nd header acts like a
trailer.

snipped for space reasons

I think I understand the problem - try something like this:
The key strategy is a double-pass of the input file.

A. Set up Working-Storage definitions for each type of record you might
encounter. Set up accumulators for detail-record numbers, etc. that
will be used to balance the batches.
B. Read Input file (File1).
   If record is a header, check to see if previous batch balanced.
        If balanced, write a record with the batch-number to a new
output file, File2. In any case clear accumulators, and start on the
next batch.
C. After all batches have been investigated, close File1 and File2.
Don't forget to investigate the last batch for balancing.
D. Open File1 and File2 for input. This starts them anew, from the top.
Open Output File3 (good batches) and Output File4 (rejects).
E. Now use File2 as a driver. Read a record from File2, then read File1
until you find the batch-number you got from File2.
If you encounter records for a different batch-number (on File1) write
them to File4 (the reject file). If you find records that match File2's
batch-number, write then to File3 (good records).

And so on. (Some details of the matching omitted above.)

John











Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: I have a question: How can this work?

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sdv0n$ctv$1@aklobs.kc.net.nz>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com>`

```
john smith <someone@microsoft.com> wrote:

: I think that should work, however I get really baffled when I must DO
: something with this batch.  I cant seem to figure out when to write the
: record to my output.  I dont want to write the batch unless the header info
: validates what is in the batch.  It could have gotten botched up in
: transmission, and merged two batches together or something ugly like that.

Just write out the batch records to a tempory file.  At start of
batch open output a relative or sequential file and write each
record.  At end of batch re open this input or open output to
delete the batch.
```

##### ↳ ↳ Re: I have a question: How can this work?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SMwG3.1949$2Q5.20628@news3.mia>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com> <7sdv0n$ctv$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
>john smith <someone@microsoft.com> wrote:
>
…[9 more quoted lines elided]…
>delete the batch.

I prefer another approach which is much faster; on the platforms I
have tried it on.  Open two sequential files input, both to the same
physical file.  Use one file to pass the batch for validation, then
use the other to fetch the batch for output.  Sequential can be much
faster than relative files for this type of operation; sometimes
many times as fast.  And always faster than reading, writing, then
reading again. :-)
```

#### ↳ Re: I have a question: How can this work?

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nHWH3.2252$j4.64545@viper>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com>`

```
What I think you have here is what I think is called an EDI file (electronic
data interchange). What you typically have is a structure similar to a
report with several groupings:

report header
page header
column header
detail rec1
detail rec2
column trailer
page trailer
report trailer

And of course you have different names such as BATCH header and possibly
others.

What I have done when processing these types of files is to:
- define separate work areas for each record type, no redefinition
- define a generic WS group which has the max record length and the record
identifier, NOT the FD.
- define each record type as a conditional based on the record identifier of
the generic record
- 2000-read file
- 2100-check indicator
- 2200-move generic record to specific record type based on conditional
- 2300-do generic processing based on record type
- 2400-read file
- loop to 2100

The generic processing would set the flags you mentioned based on the record
type. To output the records you have already processed you could use 2
record identifiers pointing to the same DDNAME. Use one for validation and
the other for actual processing: Reading ahead with the validation pointer
to see if the batch is valid. Then use the generic pointer to do the
standard processing or exception processing based on the validation set by
the validation pointer.

If you have FILEAID using a copybook which contains the GENERIC record type
and all of the SPECIFIC rcord types. Then you can verify your record layouts
using the cross reference functions.

To think about it in another way, line up the record types left to right in
the HEADER1 HEADER2 HEADER3 DETAIL1 DETAIL2 DETAIL3 FOOTER3 FOOTER2 FOOTER1.
This composite record is typically what is fed into a COBOL program to
produce a CONTROL BREAK REPORT. In this case the CONTROL BREAK REPORT is
your data file.
```

##### ↳ ↳ Re: I have a question: How can this work?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fW6I3.340$zc3.12434@dfiatx1-snr1.gtei.net>`
- **References:** `<uIPE3.54332$223.832212@typ12.nn.bcandid.com> <nHWH3.2252$j4.64545@viper>`

```
Gumbo wrote in message ...
>What I think you have here is what I think is called an EDI file
(electronic
>data interchange). What you typically have is a structure similar to a
>report with several groupings:


Um, I've been working with ANSI and EDIFACT EDI since 1983, and I still
don't buy that there is such a thing as a "generic EDI file." While EDIFACT
EDI "documents" do use 'groups' fairly liberally, ANSI EDI documents are
more often 'looped' than 'grouped.'


MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
