[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help: adding to an indexed file problem

_4 messages · 1 participant · 2000-12_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### help: adding to an indexed file problem

- **From:** goble@gtech (David. E. Goble)
- **Date:** 2000-12-22T09:52:13+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3a4218c1.379813@news.adelaide.on.net>`

```
Hi all;

Iam using Microfocus personnal Cobol.

I have created a program to create an indexed file from a sequential
file. It has one record.
   
       FILE-CONTROL.
           SELECT f200-members-file
               ASSIGN TO DISK "data/starters/members.dat"
               ORGANIZATION IS LINE SEQUENTIAL
               ACCESS IS SEQUENTIAL
               FILE STATUS IS w120-file-status.
           SELECT f100-members-file
               ASSIGN TO DISK "data/members.dat"
               ORGANIZATION IS INDEXED
               ACCESS IS RANDOM
               RECORD KEY IS f110-memb-licNo
               ALTERNATE RECORD KEY IS f120-memb-name
               FILE STATUS IS w120-file-status.
       DATA DIVISION.
      ***************
       FILE SECTION.
      *-------------
       FD  f100-members-file
           LABEL RECORDS ARE STANDARD
           RECORD CONTAINS 196 CHARACTERS
           DATA RECORD IS f100-members-rec.

key pic x(07)
name 
	first pic x(14)
	surname pic x(14)

So the indexed file has

temparyChristopher              Surname

I wrote another program to add to the index file. It asks the user for
a first name and surname, then...

    OPEN I-O f100-members-file.
...
           READ f100-members-file
               KEY IS f120-memb-name
               INVALID KEY
                   PERFORM 2100-GET-MORE-DETAILTS
                   PERFORM 2200-WRITE-MEMBER
                   PERFORM 2300-ANYMORE-MEMBERS
               NOT INVALID KEY
                   STRING err1 f110-memb-licNo w120-file-status
                           DELIMITED BY SIZE
                       INTO w990-display-message
                   END-STRING
                   PERFORM 2900-ERROR
           END-READ.

But when I enter the name "Christopher Surname" and trace the program,
it assumes that  the new key is "         " (ie spaces) and rightly or
wrongly assumes that the new record is not invalid!

This behaviour is that of the "with duplicates". I want behaviour of
without duplicates.

Is there a way to use an alternate key without duplicates???
--Regards       David. E. Goble
             goble [AT] kin.net.au
          http://www.kin.net.au/goble
Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

#### ↳ Re: help: adding to an indexed file problem

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-12-28T01:50:05+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<92cpvh$ksh$1@hermes.enternet.co.nz>`
- **References:** `<3a4218c1.379813@news.adelaide.on.net>`

```
In  a previous response to David's message I wrote:

======================   Start quote from previous response ================

"The answer is also simple, David.

There has to be a logic error. (Or maybe a definition changed between the
version you are running and the version which created the file...)

The fact that the primary key has spaces in it has no bearing on it. You
have correctly defined the Alternate key to be the "Key of Reference".

This apparently exists on the file, but the system is sure that it
doesn't...

Check that the single record on the test file has the correct information in
the Alternate key field. It is not one byte out, or something similar. You
will get an INVALID KEY on READ if the record is not found. It won't be
found if the key on the file doesn't match the key in the program."

==================  End Quote from previous response ================

(I wrote this before receiving the file...spooky isn't it <G>)

Examination of the file with a Hex editor reveals that the defined alternate
key is 13 bytes and the program has defined 14.

Problem solved. An easy error which most of us have made at some time. Be
warned!

Pete.
```

##### ↳ ↳ Re: help: adding to an indexed file problem

- **From:** goble@gtech (David. E. Goble)
- **Date:** 2000-12-30T16:01:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3a4e001e.9896787@news.adelaide.on.net>`
- **References:** `<3a4218c1.379813@news.adelaide.on.net> <92cpvh$ksh$1@hermes.enternet.co.nz>`

```
On Thu, 28 Dec 2000 01:50:05 +1300, "Peter E. C. Dashwood"
<dashwood@enternet.co.nz> wrote:
>
>(I wrote this before receiving the file...spooky isn't it <G>)
>
Not really. My newsreader shows your initial post as;

Date: Mon, 25 Dec 2000 15:18:38 +1300

and your second post as;

Date: Thu, 28 Dec 2000 01:50:05 +1300

As you are in New Zealand and Iam in South Australia, your linux box
must have a time problem or something.
>
>Examination of the file with a Hex editor reveals that the defined alternate
>key is 13 bytes and the program has defined 14. Problem solved. An easy error 
>which most of us have made at some time. Be warned!
>
It's amazing, the first thing I did was to actually checked for this
very problem. I must not have checked well enough :[

Thanks for the help.
--Regards       David. E. Goble
             goble [AT] kin.net.au
          http://www.kin.net.au/goble
Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

###### ↳ ↳ ↳ Re: help: adding to an indexed file problem

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-12-31T15:09:45+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<92m61t$487$1@hermes.enternet.co.nz>`
- **References:** `<3a4218c1.379813@news.adelaide.on.net> <92cpvh$ksh$1@hermes.enternet.co.nz> <3a4e001e.9896787@news.adelaide.on.net>`

```
David,

Allow me to refresh your memory... (I resent the implication that I
fabricated this...)

On the 25th I posted to this NewsGroup, in response to your request for
help.
(We agree on that.)

In that post I suggested (among other things) that you check the key on the
file against the key in the program.

Here's the quote:
================    start quote from 25 December  ===================
"The fact that the primary key has spaces in it has no bearing on it. You
have correctly defined the Alternate key to be the "Key of Reference".

This apparently exists on the file, but the system is sure that it
doesn't...

Check that the single record on the test file has the correct information in
the Alternate key field. It is not one byte out, or something similar. You
will get an INVALID KEY on READ if the record is not found. It won't be
found if the key on the file doesn't match the key in the program."

==============   End Quote from 25th December ===================

The next thing that happened (and you seem to have overlooked it...) was
that you sent Barry Steinholtz a copy of the source code and the file, and
also copied me.

That was on the 27th December. TWO DAYS AFTER the post containing the
prediction above.

I checked the file, found that it was indeed ONE BYTE OUT as I had
predicted, and mailed you privately a complete summary of the problem with a
screenshot from the Hex editor, showing the exact field in error, on the
28th. To jog your memory, here is the message:

========= Quote from private mail to David A. Goble on 28th
December:==========

"David,

The solution to your problem, along with some tips which might be helpful,
are attached.

Good luck with your COBOL.

Pete Dashwood."

======End Quote from private mail to David A. Goble on 28th
December:==========
Attached was the screenshot described above.

My post to the NewsGroup on the 28th was to advise anyone else to avoid the
same problem. The reference to it being "spooky" was because the key was act
ually ONE BYTE out, as I had predicted 3 Days BEFORE! (It could've been ANY
number of bytes out; it was the fact that it was ONE that I described as
"spooky".)

So there was NO tampering with dates on Linux boxes or anything else.
(Anyway, my ISP would be responsible for that, not me). It was just years of
experience predicting a possible source of error that could result in the
problem you described. And actually getting it right on the button.

Pete.

David. E. Goble wrote in message <3a4e001e.9896787@news.adelaide.on.net>...
>On Thu, 28 Dec 2000 01:50:05 +1300, "Peter E. C. Dashwood"
><dashwood@enternet.co.nz> wrote:
…[14 more quoted lines elided]…
>>Examination of the file with a Hex editor reveals that the defined
alternate
>>key is 13 bytes and the program has defined 14. Problem solved. An easy
error
>>which most of us have made at some time. Be warned!
>>
…[7 more quoted lines elided]…
>Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
