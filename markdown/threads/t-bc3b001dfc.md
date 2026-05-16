[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# use of CLOSE UNIT FOR REMOVAL

_8 messages · 4 participants · 2004-03_

---

### use of CLOSE UNIT FOR REMOVAL

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-03-04T11:27:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>`

```
First, the COBOL in question here is COBOL for VSE/ESA.  I'm guessing it
also applies to other IBM mainframe COBOLs such as Enterprise COBOL (for
z/OS), but perhaps not.

History: We have several COBOL jobs that read 1 or more tapes that are in
the same format (NACHA format, Visa Base II format, etc.).  On some days
there is only one tape, some days two, some days three etc.  Most of our
program do something like this (some of this is pseudo-COBOL):

OPEN INPUT TAPE-FILE
READ AND PROCESS TAPE-FILE UNTIL END OF FILE
CLOSE TAPE-FILE
ASK OPERATOR "Is there another tape?"
if YES,  tell operator "eject tape and then answer 'yes' to continue.  when
operator answers we loop back to the top.
if NO end program

I (and the operators) have long wished that COBOL itself could eject the
tape.

Somewhere (and it's been a while so I don't recall where) I came upon the
knowledge that using the statement "CLOSE file-name UNIT FOR REMOVAL" will
eject the tape *without* actually closing the file.  See the following
example:

OPEN INPUT TAPE-FILE
READ TAPE-FILE
CLOSE TAPE-FILE UNIT FOR REMOVAL
READ TAPE-FILE
CLOSE TAPE-FILE UNIT FOR REMOVAL
READ TAPE-FILE
CLOSE TAPE-FILE WITH LOCK

What this would do is open tape 1, read a record on tape 1, eject tape 1,
read a record on tape 2 (once tape 2 is loaded), eject tape 2, read a record
on tape 3 (once tape 3 is loaded), eject tape 3 and quit.

This seems to work fine.  The problem is reading the tape until the
end-of-file condition is met.  Once the EOF condition is met, while I can
close it for removal and it ejects the tape my next read returns with status
code '46' ("preceding READ statement caused an at end condition").

This both does and does not make sense.  It makes sense in that the error
it's giving is accurate.  However I still want to be able to do what I want
to do, which is reach the end of 1 tape, eject that tape, have a new tape
loaded and continue processing.

Now in the case of the file formats I am looking at there is a trailer
record.  I am able to set an EOF field to true once I've read the trailer
record but prior to attempting another read.  By doing this I can avoid
triggering the actual "at end" condition.  This allows my program to work as
desired.  But it still bugs me!  It seems to me that doing the CLOSE UNIT
FOR REMOVAL should reset the "at end" condition to no longer be true.

Any thoughts?  Do other COBOLs work this way?  Am I just being anal, since I
already know a work-around?


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** docdwarf@panix.com
- **Date:** 2004-03-04T13:48:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c27tm6$3gc$1@panix5.panix.com>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>`

```
In article <c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>First, the COBOL in question here is COBOL for VSE/ESA.

I know nothing of this dialect... my comments are directed differently.

>Am I just being anal, since I
>already know a work-around?

Well, since you bring it up... perhaps it might be wise to meditate on the 
following bit of ancient code

IF PROGRAM-RUNS
   PERFORM NEXT-ASSIGNMENT
ELSE
    PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING-WORKS.

DD
```

##### ↳ ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-03-04T17:02:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c28g3j$1qcr39$1@ID-184804.news.uni-berlin.de>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de> <c27tm6$3gc$1@panix5.panix.com>`

```
Good advice, perhaps, but it goes a bit against my nature!  :-)

>>> <docdwarf@panix.com> 3/4/2004 11:48:38 AM >>>
In article <c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>First, the COBOL in question here is COBOL for VSE/ESA.

I know nothing of this dialect... my comments are directed differently.

>Am I just being anal, since I
>already know a work-around?

Well, since you bring it up... perhaps it might be wise to meditate on the 
following bit of ancient code

IF PROGRAM-RUNS
   PERFORM NEXT-ASSIGNMENT
ELSE
    PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING-WORKS.

DD
```

###### ↳ ↳ ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** docdwarf@panix.com
- **Date:** 2004-03-04T21:07:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c28ndo$90e$1@panix1.panix.com>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de> <c27tm6$3gc$1@panix5.panix.com> <c28g3j$1qcr39$1@ID-184804.news.uni-berlin.de>`

```
In article <c28g3j$1qcr39$1@ID-184804.news.uni-berlin.de>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>Good advice, perhaps, but it goes a bit against my nature!  :-)

As did, perhaps, singing baritone go against the nature of many a 
youngster... but, with time, things changed.

DD


>
>>>> <docdwarf@panix.com> 3/4/2004 11:48:38 AM >>>
…[17 more quoted lines elided]…
>DD
```

#### ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-04T18:54:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vXK1c.19067$yZ1.5821@newsread2.news.pas.earthlink.net>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>`

```
Frank,
  As you know, I know just enough about VSE to get myself in trouble.
Furthermore, I explicitly remember there being a LOT of  "issues" about REMOVAL
and REWIND with COBOL on VSE (differences between DOS/VS COBOL and - I think -
VS COBOL II - also VSE working differently than MVS).

HOWEVER, without knowing your exact application needs, it sounds to me as if you
should be able to code a

   USE AFTER STANDARD ENDING REEL LABEL PROCESSING

DECLARATIVE to accomplish what you want.

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igyvr002/8.1.15.3


In the declarative, you could "ask" the operator if there was another tape or
not - if not simply CLOSE the file - if SO - do NOT close the file but simply
try another READ and it should call for the mount of the next reel.

Am I missing something?

P.S.  Check the IBM "archives" for APARs related to CLOSE REWIND or REMOVAL on
VSE.  They may be VERY old - but I think they may help you understand exactly
what is (or is supposed to be) happening.
```

##### ↳ ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-03-08T10:49:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2ibnm$1ta2o2$2@ID-184804.news.uni-berlin.de>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de> <vXK1c.19067$yZ1.5821@newsread2.news.pas.earthlink.net>`

```
Hi Bill,

I attempted doing a few things using DECLARITIVES but I've never used them
before and to be honest, I couldn't figure it out!  Maybe with a bit more
effort I could, but as you'll see in my message to Micrcea Tamas, he's led
me down the path I was looking for.  Thanks for your help.

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 3/4/2004 11:54:19 AM >>>
Frank,
  As you know, I know just enough about VSE to get myself in trouble.
Furthermore, I explicitly remember there being a LOT of  "issues" about
REMOVAL
and REWIND with COBOL on VSE (differences between DOS/VS COBOL and - I think
-
VS COBOL II - also VSE working differently than MVS).

HOWEVER, without knowing your exact application needs, it sounds to me as if
you
should be able to code a

   USE AFTER STANDARD ENDING REEL LABEL PROCESSING

DECLARATIVE to accomplish what you want.

See:
 
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igyvr002/8.1.15.3



In the declarative, you could "ask" the operator if there was another tape
or
not - if not simply CLOSE the file - if SO - do NOT close the file but
simply
try another READ and it should call for the mount of the next reel.

Am I missing something?

P.S.  Check the IBM "archives" for APARs related to CLOSE REWIND or REMOVAL
on
VSE.  They may be VERY old - but I think they may help you understand
exactly
what is (or is supposed to be) happening.
```

#### ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** mircea_tamas@yahoo.com (mircea)
- **Date:** 2004-03-07T07:27:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f25b5cf.0403070727.77973034@posting.google.com>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de>`

```
Frank

your problem seems to mirror my problem about "Tape load/unload from
within a Cobol/MVS program" at
http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&oe=UTF-8&threadm=5f25b5cf.0301230204.71170b4c%40posting.google.com&rnum=1&prev=/groups%3Fhl%3Den%26lr%3D%26ie%3DUTF-8%26oe%3DUTF-8%26selm%3D5f25b5cf.0301230204.71170b4c%2540posting.google.com

I had to write an undefinite number of tapes, every tape containing
one file with same structure. You have to read the same thing.
The clue is dynamic allocation of tapes through an Assembler
subroutine.
In my program, after the first tape is allocated to program, file it's
written, file closed and tape deallocated. Now the second tape can be
mounted, allocated to program and so on.
I don't know if dynamic allocation is allowed under VSE, this can be
really sad.
Another push to upgrade. ;)
Regards,
Mircea
```

##### ↳ ↳ Re: use of CLOSE UNIT FOR REMOVAL

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-03-08T10:47:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2ibiu$1ta2o2$1@ID-184804.news.uni-berlin.de>`
- **References:** `<c27sds$1q6m0m$1@ID-184804.news.uni-berlin.de> <5f25b5cf.0403070727.77973034@posting.google.com>`

```
Hi Mircea,

Actually, following your link I was able to find other link which gave the
the answer I was looking for.  That link is:
http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&newwindow=1&threadm=B0000
107577%40apps.escape.net.au&rnum=1&prev=/groups%3Fhl%3Den%26lr%3D%26ie%3DUTF
-8%26newwindow%3D1%26selm%3DB0000107577%2540apps.escape.net.au

This link may only apply to VSE, but anyway the answer is very simple.  So
simple it's embarassing, actually!  Basically, it's just the following:
CLOSE filename REEL FOR REMOVAL
CLOSE filename
OPEN INPUT filename

What I had been trying to do was eject the tape and process the next tape as
part of the "same file", kind of as if it was a single file spanning more
than one tape.  The above way simply treats the new tape as, well, a new
tape.  Which is the way the program was working in the first place, with the
only difference being the old way was something like:
CLOSE filename
STOP "OPERATOR: Please eject current tape and enter new tape, then press
Enter"
OPEN INPUT filename

Thanks for the pointer!  I had done a google groups search but had not seen
what I was looking for.

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> mircea<mircea_tamas@yahoo.com> 3/7/2004 8:27:29 AM >>>
Frank

your problem seems to mirror my problem about "Tape load/unload from
within a Cobol/MVS program" at
http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&oe=UTF-8&threadm=5f25b5cf
.0301230204.71170b4c%40posting.google.com&rnum=1&prev=/groups%3Fhl%3Den%26lr
%3D%26ie%3DUTF-8%26oe%3DUTF-8%26selm%3D5f25b5cf.0301230204.71170b4c%2540post
ing.google.com

I had to write an undefinite number of tapes, every tape containing
one file with same structure. You have to read the same thing.
The clue is dynamic allocation of tapes through an Assembler
subroutine.
In my program, after the first tape is allocated to program, file it's
written, file closed and tape deallocated. Now the second tape can be
mounted, allocated to program and so on.
I don't know if dynamic allocation is allowed under VSE, this can be
really sad.
Another push to upgrade. ;)
Regards,
Mircea
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
