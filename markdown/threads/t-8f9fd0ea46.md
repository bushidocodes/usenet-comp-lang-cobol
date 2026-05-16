[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# dynamic index

_46 messages · 16 participants · 2002-05 → 2002-06_

---

### dynamic index

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-28T22:18:52+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad03p7$i2b$1@coco.singnet.com.sg>`

```
Hi
I am doing a program on index file. My index file ha a few record similar to
the one described below

11111
22222
11111
33333

I assigned my file as dynamic. When I read the file for key 11111, it should
read record on 1st and third record which contains key 11111.
when it's invalid, I will put 'n' = no-more record.
thus the calling program will stop it's loop since no-more-record is = to
'n'

But the record keeps reading for few more records before it stops. I am very
sure there is nothing wrong with my code.
I have used the debugger . Was very puzzle, why it did not stop as i would
expect it to stop.

What are the possibilities? Could it be my index file that is causing
problem?

Help is appreciated
```

#### ↳ Re: dynamic index

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-28T23:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg>`

```

"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:ad03p7$i2b$1@coco.singnet.com.sg...
> Hi
> I am doing a program on index file. My index file ha a few record similar
to
> the one described below
>
…[5 more quoted lines elided]…
> I assigned my file as dynamic. When I read the file for key 11111, it
should
> read record on 1st and third record which contains key 11111.
> when it's invalid, I will put 'n' = no-more record.
…[3 more quoted lines elided]…
> But the record keeps reading for few more records before it stops. I am
very
> sure there is nothing wrong with my code.
> I have used the debugger . Was very puzzle, why it did not stop as i would
…[3 more quoted lines elided]…
> problem?

Could be. Index files REQUIRE the keys be unique. Record #3 CANNOT exist in
your file - it would have been discarded.

There are two completely different READ methods for an index file:

READ MYFILE (which attempts to read the record whose key matches the key you
specified)

and

READ MYFILE NEXT (which gets the next record in the file).

Now if you set a key (MOVE "1111"1 TO MYFILE-KEY)

and READ MYFILE, you'll get record 11111. If your next read is:

READ MYFILE

you'll get the same record again.

Bare in mind that if READ MYFILE fails (the record you want doesn't exist),
then subsequent READ MYFILE NEXT statements make no sense and will probably
fail also.
```

##### ↳ ↳ Re: dynamic index

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-29T20:35:56+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad2i48$q3p$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com>`

```
I just realised that read and read next are 2 different thing, however I am
using the correct syntax.
From my textbook , their sytax used  is " read (filename) next record"

Read next record means red sequentially?
Read mean randomly?

Someone suggested me to post my code but I don't think that's appropriate.
This is part of my assignment. I am just fustrated, this is my last hurdle
to completion of this assignment. After spending so many nights , I am still
unable to debug. Indeed logical error is worse than syntax error.

Probably the sample code (simliar to assignment but it's not) below will
help to explain the situation.

PERFORM 1000-PROCESS-FILE
************************
1000-PROCESS-FILE.
   IF  EVERYTHING-CORRECT ='Y'
          START FILE-INDEX   KEY  =  NUMBERS
             INVALID KEY
                  MOVE 'N' TO ANY-DATA
             NOT INVALID KEY
                  PERFORM 2000-READ-FILE UNTIL ANY-DATA = ' N '
          END-START
   END-IF.
****************************
2000-READ-FILE.
  READ FILE-INDEX NEXT RECORD
     AT END
        MOVE 'N' TO ANY-DATA
    NOT AT END
*** THIS 3000-CHECK-SOMETHING WILL CHECK FOR CERTAIN DATA , IF CORRECT WILL
PRODUCE CORRECT-ABC = Y
        PERFORM 3000-CHECK-SOMETHING
        IF CORRECT-ABC = 'Y'
           PERFORM 4000-PRINT
      END-IF
END-READ.


I just don't understand why my file-index was being read all the time even
though there isn't anymore more of the record with the key value.
the error always occurs on 2000-read-file, it just does not go to move'n' to
any-data.

Should I be using READ instead of READ NEXT?
I tried that too but failed


"JerryMouse" <nospam@invalid.com> wrote in message
news:49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com...
>
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
> news:ad03p7$i2b$1@coco.singnet.com.sg...
> > Hi
> > I am doing a program on index file. My index file ha a few record
similar
> to
> > the one described below
…[10 more quoted lines elided]…
> > thus the calling program will stop it's loop since no-more-record is =
to
> > 'n'
> >
…[3 more quoted lines elided]…
> > I have used the debugger . Was very puzzle, why it did not stop as i
would
> > expect it to stop.
> >
…[3 more quoted lines elided]…
> Could be. Index files REQUIRE the keys be unique. Record #3 CANNOT exist
in
> your file - it would have been discarded.
>
> There are two completely different READ methods for an index file:
>
> READ MYFILE (which attempts to read the record whose key matches the key
you
> specified)
>
…[12 more quoted lines elided]…
> Bare in mind that if READ MYFILE fails (the record you want doesn't
exist),
> then subsequent READ MYFILE NEXT statements make no sense and will
probably
> fail also.
>
>
```

###### ↳ ↳ ↳ Re: dynamic index

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-29T15:46:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kJ6J8.61688$%o.5861078@bin3.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg>`

```

"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:ad2i48$q3p$1@coco.singnet.com.sg...
> I just realised that read and read next are 2 different thing, however I
am
> using the correct syntax.
> From my textbook , their sytax used  is " read (filename) next record"
>
> Read next record means red sequentially?
> Read mean randomly?

Yes.

READ MYFILE NEXT (or READ MYFILE PRIOR/PREVIOUS with some compilers)
   AT END do something
   NOT AT END do something else
   END-READ

Gets the next record sequentially from the current location of the 'record
pointer.'

Whereas:

MOVE data-name TO MYFILE-KEY
READ MYFILE
   INVALID KEY do something
   NOT INVALID KEY do something else
   END-READ

Gets the records specified by data-name.

Note the 'record pointer' gets set with AT END, NOT AT END, NOT INVALID KEY
but is meaningless if the INVALID KEY phrase is invoked during a READ
(random). That is, if READ (random) fails, any subsequent READ NEXT commands
generate junk.

Use of the START command on an index file is left as an exercise for the
reader.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-30T00:09:52+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad2ulc$rlr$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <kJ6J8.61688$%o.5861078@bin3.nnrp.aus1.giganews.com>`

```
I just tried a few method on this, Will keep trying. Thanks for the great
help.
"JerryMouse" <nospam@invalid.com> wrote in message
news:kJ6J8.61688$%o.5861078@bin3.nnrp.aus1.giganews.com...
>
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
…[29 more quoted lines elided]…
> Note the 'record pointer' gets set with AT END, NOT AT END, NOT INVALID
KEY
> but is meaningless if the INVALID KEY phrase is invoked during a READ
> (random). That is, if READ (random) fails, any subsequent READ NEXT
commands
> generate junk.
>
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: dynamic index

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2002-05-29T12:03:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0205291103.612e81d8@posting.google.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg>`

```
Try specifying and using/testing the file status for your indexed
file.  I am surprised you even managed to create an indexed file with
duplicate keys and suspect that you didn't use file status in the
program that you used to create the file, so didn't get any messages
to say that duplicate keys were not allowed.  To use file status,
specify a working-storage data item of two bytes and look up the
syntax for the SELECT statement in the File-Control section of the
Environment Division.  Then for each I/O statement for your file test
the file status, which should normally be zero, except for "10" for
end-of-file, "21" for a sequence error when accessing a sequentially
accessed indexed file, "22" for attempting to write a record with the
same key as one that already exists and "23" for attempting to read a
record randomly for a key that does not exist.  If the file status is
not "00" or "10", then display it with the key of the record being
accessed to give a trace of what is happening.  The way your code
fragments are written, your program would think that it had read
subsequent records, when in fact it had failed to read successfully
and the old record was still sitting in the record-description of your
file.  Your manual should give you a full list of file status codes
and their meanings.


Cheers, Robert

"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message news:<ad2i48$q3p$1@coco.singnet.com.sg>...
> I just realised that read and read next are 2 different thing, however I am
> using the correct syntax.
…[110 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-29T14:08:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad3905$3cr$1@slb3.atl.mindspring.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com>`

```
I have been avoiding adding to this thread, but thought that I better add a
"slight" caveat to what others are saying.

A) duplicate ALTERNATE keys are allowed (just in case the original poster
didn't really tell us exactly what was happening). I know that most of those
replying know about this, but I thought it should be mentioned any way.

B) I *hate* it, but some implementations actually *DO* allow for duplicate
primary keys (as an extension).  The semantics for such files often gets
really UGLY and I doubt that this is ever "intentional" in a new
application, but I did want to make certain that everyone in the group
saying that it "couldn't happen" - knew that in SOME environments, it can.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-31T23:47:57+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad864c$baa$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad3905$3cr$1@slb3.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:ad3905$3cr$1@slb3.atl.mindspring.net...
> I have been avoiding adding to this thread, but thought that I better add
a
> "slight" caveat to what others are saying.
>
> A) duplicate ALTERNATE keys are allowed (just in case the original poster
> didn't really tell us exactly what was happening). I know that most of
those
> replying know about this, but I thought it should be mentioned any way.
>
…[9 more quoted lines elided]…
>

.Thanks bills. Anyway didn't manage to complete on time, only 90% completed.
Overall still happy with my project
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-31T23:50:04+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad868c$bc8$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com>`

```
Indeed I did not use file status at all.  Is it a must to use file status
when dealing with index file?

"Robert Jones" <robert@jones0086.freeserve.co.uk> wrote in message
news:fcd09c56.0205291103.612e81d8@posting.google.com...
> Try specifying and using/testing the file status for your indexed
> file.  I am surprised you even managed to create an indexed file with
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-31T11:20:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad87t5$o3i$1@slb0.atl.mindspring.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg>`

```
According to the current ANSI/ISO Standard, you *must* code either a file
status or a declarative.  (Many/most implementations do not enforce this
rule)

Whether or not your compiler requires this, it is HIGHLY recommended that
you always check the file-status after every I/O statement (including OPEN
and CLOSE).  Alternatively, you may want to look at a FILE declarative -
although from my personal experience, this is less often used.

The "traditional" AT END/INVALID KEY phrases only catch *some* file errors.
Although you probably won't experience many of the other types of problems
in beginning course work, they do exist in "production" environments and not
taking explicit programming action may well result in serious (and sometime
undetected) problems.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 6)_

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-05-31T20:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF7DD27.8050408@optonline.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <ad87t5$o3i$1@slb0.atl.mindspring.net>`

```
William M. Klein wrote:

> According to the current ANSI/ISO Standard, you *must* code either a file
> status or a declarative.  (Many/most implementations do not enforce this
…[11 more quoted lines elided]…
> undetected) problems.


What Bill's saying and with which I heartily agree is it's good 
technique & a *very* good idea to learn this way first.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-05-31T16:30:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dyNJ8.1482$m9.101@nwrddc02.gnilink.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg>`

```

Sim Choon Howe <schowe@singnet.com.sg> wrote in message
news:ad868c$bc8$1@coco.singnet.com.sg...
> Indeed I did not use file status at all.  Is it a must to use file status
> when dealing with index file?

It's not a "MUST" in that no COBOL compiler will force you to do this, but
checking FILE STATUS on "all" disk I-O (indexed or sequential) is IMNSHO an
important part of writing good program code.

MCM
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "JamesJ. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-31T16:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF7AB2B.A1F15E7A@shaw.ca>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg>`

```


Sim Choon Howe wrote:

> Indeed I did not use file status at all.  Is it a must to use file status
> when dealing with index file?

Using file status is *NOT* a must and as noted in the past there are many
here who don't use it. It's a question of choice. There's an aspect of
programming called XP (eXtreme Programming) - use every facility there is to
test for any possible errors - inevitably Murphy's Law will kick in at some
time. Pete Dashwood summed it up best recently when he made the statement,
"The only code that matters is that which hasn't yet crashed".

I definitely use file status all the time. Write yourself a simple program
doing the following :-

    set NotEOF to true
    perform READ-NEXT-RECORD
    perform until EOF
        display MyRecord
        perform READ-NEXT-RECORD
    End-perform

    STOP RUN.

    READ-NEXT-RECORD.
        Read Myfile next record
            at end set EOF to true
        End-read

    if file-status <> "00"
        display "File Status Error"
    End-if.

Now check what the program is doing - I haven't OPENED the file - now see
what the file-status gives you ! As a newcomer, or even an 'old hand', you
could get as frustrated as hell trying to figure out why it isn't working.
The file-status gives you an immediate clue.

Jimmy, Calgary AB

>
>
…[22 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-05-31T20:28:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad8m40$3qr$1@peabody.colorado.edu>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca>`

```
I work with a system with called programs within called programs that do
status checks.   The inside program does an OPEN of the VSAM file and checks
the status code.  The status code is '97', which means it opened correctly.
Only the programmers didn't anticipate this and only check for '00'.  The
program passes back a different new error code which means "failure".  Heck,
with that level of detail don't pass anything at all - we will know it
failed when the write aborts!

This called program is used all over the place by the vendor who supplied us
with the system.  And it is exactly the reason why mainframe people tend to
fear OO (While this isn't OO, it does have what OO advocates push as OO's
"advantages").  Mainframe people don't want to change the system because of
extensive testing needed and lots of programs using the interface that need
to be changed.  And the problem goes away - if it aborts and nobody knows
why, restart and it will work correctly IF the abort was caused by a status
code of '97'.

The irritation only costs us a few programmer hours per failure while the
fix would be very expensive getting everybody to sign off on extensive
testing of everything that uses it.  So we live with it and curse the
vendor.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-31T15:37:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad8mtt$dq3$1@slb7.atl.mindspring.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu>`

```
It is worth mentioning when/why the way IBM (mainframe) COBOL produces the
"97" file-status code has been a "matter of discussion" among those who care
about ANSI/ISO conformance.

In theory, a "9x" file status code *should* indicate a FAILURE (defined by
the implementor).  However, the IBM "97" is actually treated as a
"successful" status code (with an "anomalous" situation).

In the next Standard (oops - here we go again <G>) there is a new "0x"
category of "implementor defined successful file status code" which would be
a "better" place for the existing IBM "97" processing.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** "JamesJ. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-31T21:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF7EB87.FEE13DCD@shaw.ca>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> I work with a system with called programs within called programs that do
> status checks.   The inside program does an OPEN of the VSAM file and checks
…[18 more quoted lines elided]…
> vendor.

Where angels fear to tread.... <G>.  So OO only adds to the nightmare ? Put a
file access class between YOU and the rotten Vendor's software.

01 SystemType
    88 IfYouReallyMustUseIBM            value 1.
    88 NormalFolks                                value 2.

set IfYouReallyMustUseIBM to true
invoke OurOwnFileHandler "openFile" using SystemType, Filename
            returning Ls-Result

Class - OurOwnFileHandler
method-id. "openFile"
Linkage section.
01 lnk-SystemType                           pic 9.
    88 IfYouReallyMustUseIBM            value 1.
    88 NormalFolks                                value 2.
01 lnk-FileName                            pic x(100).
01 lnk-Result                                   pic 9(03).
    88 ResultOK                               value 0.
    88 FileError                                 value 99.

Procedure Division using  lnk-SystemType, lnk-Filename returning lnk-Result.

set ResultOK to true
call the vendor's rotten software and get his file-status

Evaluate true
    when file-status = "00"
    when file-status = "97" and IfYouReallyMustUseIBM
            continue
    when other
            set FileError to true
End-evaluate

Before WMK jumps in, you could do the above with a conditional compilation :-

    #if.......
     etc...
    #end-if

or are you salivating, waiting for the latest and greatest compiler ?

*******

Don't think USAF have two seats up front in fighters do they ? Gawd, I'd hate to
be your co-pilot <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-06-03T16:31:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adg5bt$2t7$1@peabody.colorado.edu>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu> <3CF7EB87.FEE13DCD@shaw.ca>`

```

On 31-May-2002, "JamesJ. Gavan" <jjgavan@shaw.ca> wrote:

> Where angels fear to tread.... <G>.  So OO only adds to the nightmare ?
> Put a file access class between YOU and the rotten Vendor's software.

First I need to persuade my employers that we should become the first
company to include OO CoBOL in with existing enterprise CoBOL.

But I am curious - how hard is it to put such a class in between the
existing non OO calling programs and the existing non OO called programs?


> Don't think USAF have two seats up front in fighters do they ? Gawd, I'd
> hate to be your co-pilot <G>.

I have to admit that I missed whatever point you were making here but..

Actually, I did fly T37 jets that had side by side seating.  While I was in
pilot training we had some officers (from Chile?) who didn't advance to the
T38 flying because they were going to fly A37s.   But their A37s didn't have
a right seat.  I've never seen one in person.  I really don't see any
difference in how we would fly whether the fighter plane had tandem or
side-by-side seating.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-03T19:44:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CFBC746.6CCD4848@shaw.ca>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu> <3CF7EB87.FEE13DCD@shaw.ca> <adg5bt$2t7$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> On 31-May-2002, "JamesJ. Gavan" <jjgavan@shaw.ca> wrote:
>
…[7 more quoted lines elided]…
> existing non OO calling programs and the existing non OO called programs?

The only realistic way to get an answer to that one would be to ask IBM how it
fits in with their 'current' version of OO.  I'm assuming initially that you
only want to check '97's' resulting from OPENs.

Jimmy
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-01T16:44:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF8EBCE.1EB93E29@Azonic.co.nz>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
>
> Only the programmers didn't anticipate this and only check for '00'.  

Note that 'success' is indicated entirely by the first character being
'0' and checking both for '00' may result in erroneous failure
indications.

For example on a read or write a file-status of '02' indicates
successful operation but there are valid duplicate alternative keys.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-06-03T16:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adg65f$36v$1@peabody.colorado.edu>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu> <3CF8EBCE.1EB93E29@Azonic.co.nz>`

```

On  1-Jun-2002, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > Only the programmers didn't anticipate this and only check for '00'.
>
…[5 more quoted lines elided]…
> successful operation but there are valid duplicate alternative keys.

Here's the open paragraph:

 OPEN-FILE.
     IF OPEN-SW = 'Y'
         MOVE '2' TO RTN-CODE
         GO TO EXIT-THIS-PGM.
     IF READ-TYPE = 'U'
         OPEN INPUT RND-FILE
       ELSE
         OPEN I-O RND-FILE.
     MOVE 'Y' TO OPEN-SW.
     IF FILE-STATUS NOT = '00'
         MOVE '7' TO RTN-CODE.
     GO TO EXIT-THIS-PGM.

We are gradually getting rid of it - by getting rid of the VSAM files.

I really never understood the advantage of using this kind of call in the
first place - maybe it was because the vendor didn't want to train its
programmers on how to do VSAM I/O.  They also have called programs to write
reports that are MUCH harder to debug than simple writes are.  And they
sometimes are impossible to change to what the user wants - giving us the
excuse to replace the calls with simple CoBOL.

At any rate it is this type of nonsense that makes enterprises leery about
buying a vendor supplied OO system (if such were available).  We just KNOW
that they will have programmers of this quality doing it.  I would rather
fix a poorly designed isolated system than a poorly designed integrated
system.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-04T07:56:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CFC6494.341DCBC9@Azonic.co.nz>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <fcd09c56.0205291103.612e81d8@posting.google.com> <ad868c$bc8$1@coco.singnet.com.sg> <3CF7AB2B.A1F15E7A@shaw.ca> <ad8m40$3qr$1@peabody.colorado.edu> <3CF8EBCE.1EB93E29@Azonic.co.nz> <adg65f$36v$1@peabody.colorado.edu>`

```
> Here's the open paragraph:
> 
…[14 more quoted lines elided]…
> that they will have programmers of this quality doing it.  

I note that it leaves the 'Open-SW' set to "Y" when it has failed to
open the file.  Good work, the OPEN can't even be retried. 

Of course the advantage of a set of centralised routines is that they
can be fixed in one place rather than in every instance in several
hundred programs, but they should get it right.
```

###### ↳ ↳ ↳ Re: dynamic index

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2002-05-29T19:08:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0205291808.14b1ead@posting.google.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg>`

```
"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message news:<ad2i48$q3p$1@coco.singnet.com.sg>...
> I just realised that read and read next are 2 different thing, however I am
> using the correct syntax.
…[36 more quoted lines elided]…
> END-READ.

If ANY-DATA is a  3-character field, 2000-read-file will set it to 'N 
' at the end of the file.  If ANY-DATA is a 1-character field,
2000-READ-FILE will be performed until ANY-DATA is ' '.

When we ask you to post your real code, we are not kidding around. A
typo in your example makes us waste a lot of time.

Stephen J Spiro
Member, ANSI COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-31T23:45:03+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad85uu$bh0$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <49UI8.52393$%o.5150507@bin3.nnrp.aus1.giganews.com> <ad2i48$q3p$1@coco.singnet.com.sg> <4145699b.0205291808.14b1ead@posting.google.com>`

```
Hi,

"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0205291808.14b1ead@posting.google.com...
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:<ad2i48$q3p$1@coco.singnet.com.sg>...
> > I just realised that read and read next are 2 different thing, however I
am
> > using the correct syntax.
> > From my textbook , their sytax used  is " read (filename) next record"
…[4 more quoted lines elided]…
> > Someone suggested me to post my code but I don't think that's
appropriate.
> > This is part of my assignment. I am just fustrated, this is my last
hurdle
> > to completion of this assignment. After spending so many nights , I am
still
> > unable to debug. Indeed logical error is worse than syntax error.
> >
…[20 more quoted lines elided]…
> > *** THIS 3000-CHECK-SOMETHING WILL CHECK FOR CERTAIN DATA , IF CORRECT
WILL
> > PRODUCE CORRECT-ABC = Y
> >         PERFORM 3000-CHECK-SOMETHING
…[10 more quoted lines elided]…
> typo in your example makes us waste a lot of time.

Actually, I like to know more on how the dynamic read works. I am not
suppose to post the code as this was mentioned  by my supervisor in our
course newsgroup. Of course I know you people aren't kidding, coz there are
lots of helpful people in this newsgroup.
Really appreciate all the help you people have given me. Thanks

>
> Stephen J Spiro
> Member, ANSI COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-05-31T12:35:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad88og$sic$1@panix1.panix.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <ad2i48$q3p$1@coco.singnet.com.sg> <4145699b.0205291808.14b1ead@posting.google.com> <ad85uu$bh0$1@coco.singnet.com.sg>`

```
In article <ad85uu$bh0$1@coco.singnet.com.sg>,
Sim Choon Howe  <schowe@singnet.com.sg> wrote:

[snip]

>Of course I know you people aren't kidding, coz there are
>lots of helpful people in this newsgroup.

Oh, I *cannot* resist... and then... there's *me*!  Now, please do your 
own homework... and post a rate, or range of rates, associated with the 
position(s) offered... and while you're at it you can put together a 
diagram showing the Lines of Authority and Responsibility for a typical 
RAD project.

(if none of this made any sense... be very, *very* happy)

DD
```

#### ↳ Re: dynamic index

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-05-28T21:25:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad1e75$nr0$1@nntp-m01.news.aol.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg>`

```
You cannot have duplicate primary keys. If you wish to read by the keys you
have shown you must use something else, something unique, as your primary
key and define this key as an alternate key which can have duplicates.

There were times in my early programming days I have also been very sure there
was nothing wrong with my code. Only to discover I was wrong. I am a better
COBOL programmer now after 25 years and when something doesn't work I
always ask someone else to check me when I cannot see it myself. It is very easy
to get "too close" to your own work and miss the error that is staring you in the face.
I am sure if post your code, people would be willing to help you.

-----------------------------------------------------------------------------
"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message news:ad03p7$i2b$1@coco.singnet.com.sg...
> Hi
> I am doing a program on index file. My index file ha a few record similar to
…[22 more quoted lines elided]…
>
```

#### ↳ Re: dynamic index

- **From:** bangis2k1@eudoramail.com (jun lorena)
- **Date:** 2002-05-28T23:33:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d7858be.0205282233.ef4eacd@posting.google.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg>`

```
Hi,

I used Cobol several years ago but i shift now in xbase.

I think there is some problem with your code.

Try This Procedure Division:

Process-Rtn.
Do While cEOFSW = 0
   If cYourData Not = "11111"
      Perform End-Rtn
   Else
      <Your Process Here>
   EndIf

End-Rtn.
   Exit




"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message news:<ad03p7$i2b$1@coco.singnet.com.sg>...
> Hi
> I am doing a program on index file. My index file ha a few record similar to
…[21 more quoted lines elided]…
> Help is appreciated
```

##### ↳ ↳ Re: dynamic index

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-29T20:36:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad2i5p$pb3$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com>`

```
Is ther a do whiel command for Cobol?
should I do perform until?
"jun lorena" <bangis2k1@eudoramail.com> wrote in message
news:3d7858be.0205282233.ef4eacd@posting.google.com...
> Hi,
>
…[20 more quoted lines elided]…
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:<ad03p7$i2b$1@coco.singnet.com.sg>...
> > Hi
> > I am doing a program on index file. My index file ha a few record
similar to
> > the one described below
> >
…[5 more quoted lines elided]…
> > I assigned my file as dynamic. When I read the file for key 11111, it
should
> > read record on 1st and third record which contains key 11111.
> > when it's invalid, I will put 'n' = no-more record.
> > thus the calling program will stop it's loop since no-more-record is =
to
> > 'n'
> >
> > But the record keeps reading for few more records before it stops. I am
very
> > sure there is nothing wrong with my code.
> > I have used the debugger . Was very puzzle, why it did not stop as i
would
> > expect it to stop.
> >
…[3 more quoted lines elided]…
> > Help is appreciated
```

###### ↳ ↳ ↳ Re: dynamic index

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-29T15:48:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg>`

```

"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:ad2i5p$pb3$1@coco.singnet.com.sg...
> Is ther a do whiel command for Cobol?
> should I do perform until?

PERFORM UNTIL (in COBOL) = DO WHILE (in less robust languages)

You can even:

PERFORM WITH NO LIMIT

which is just about forever.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-05-30T05:58:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF5BF7E.9B2B71D8@worldnet.att.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:
> 
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
…[10 more quoted lines elided]…
> which is just about forever.

I don't believe I have ever seen "PERFORM WITH NO LIMIT".  Is it
possibly some vendor's extension?  Which COBOL compiler allows this?

I must admit I once set up a condition name so I could code the
following example:

PERFORM PROCESS-TRANLOG-FILES
    UNTIL INFINITE-LOOP-DONE.

But I wouldn't necessarily recommend it.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-30T14:20:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HyqJ8.77581$Oa1.6496297@bin8.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF5BF7E.9B2B71D8@worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message
news:3CF5BF7E.9B2B71D8@worldnet.att.net...
> JerryMouse wrote:
> >
…[14 more quoted lines elided]…
> possibly some vendor's extension?  Which COBOL compiler allows this?

The Fujitsu compiler allows it, along with the Get-Out-Of-Jail-Free command:

   EXIT PERFORM

So,

PERFORM WITH NO LIMIT
   IF some-condition
      EXIT PERFORM
   END-IF
END-PERFORM
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 6)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-05-30T10:24:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0DqJ8.11653$Ed1.1843765@news20.bellglobal.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF5BF7E.9B2B71D8@worldnet.att.net> <HyqJ8.77581$Oa1.6496297@bin8.nnrp.aus1.giganews.com>`

```
"JerryMouse" <nospam@invalid.com> wrote in message
news:HyqJ8.77581$Oa1.6496297@bin8.nnrp.aus1.giganews.com...
>
> "Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message
…[19 more quoted lines elided]…
> The Fujitsu compiler allows it, along with the Get-Out-Of-Jail-Free
command:
>
>    EXIT PERFORM
…[9 more quoted lines elided]…
>

Not to mention those caes where you WANT to code an infinite loop.  It may
not be common on a mainframe, but it is common on a microcomputer.

Donald
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-05-31T20:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF7DF12.7000007@optonline.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF5BF7E.9B2B71D8@worldnet.att.net>`

```
Arnold Trembley wrote:

> JerryMouse wrote:
> 
…[24 more quoted lines elided]…
> But I wouldn't necessarily recommend it.


Hmmm, the above is the fundamental processing of many (most?) batch 
COBOL programs, i.e., PERFORM your mainline logic until you're done. The 
mainline logic is built around reading one or more input files and 
INFINITE-LOOP-DONE = EOF.

Perhaps:

PERFORM PROCESS-TRANLOG-FILES
     UNTIL INFINITE-LOOP-DONE

.
.
.

PROCESS-TRANLOG-FILES.
   Read Tranlog-File
     at end  Set INFINITE-LOOP-DONE to True
     not at end  <process the record, which probably includes any other 		 
TRANLOG-FILEs>
   End-Read
   .



I've written/maintained a LOT like that:-)
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-06-01T07:26:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF8771B.8F62F5AE@worldnet.att.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF5BF7E.9B2B71D8@worldnet.att.net> <3CF7DF12.7000007@optonline.net>`

```
Liam Devlin wrote:
> 
> Arnold Trembley wrote:
…[31 more quoted lines elided]…
> I've written/maintained a LOT like that:-)

Actually, my example used a flag and condition name that was *never*
set true, so it really was an infinite loop.  It was an unusual
application, a started task using the H&W SYSB product to capture
transaction data from one CICS system's log files (and thus allowing
another TCB) and STARTing the messages over to a network monitor CICS
region.  Since both CICS systems were (and are) 24 by 7, the data
capture process could only be stopped by cancelling the started task.

Later we added a refinement to read a temp storage queue in the
network monitor CICS system that could be posted with a request to
shut down the data capture system.  Then we set INFINITE-LOOP-DONE to
true.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-06-02T05:49:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF9B1BE.4040107@optonline.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF5BF7E.9B2B71D8@worldnet.att.net> <3CF7DF12.7000007@optonline.net> <3CF8771B.8F62F5AE@worldnet.att.net>`

```
Arnold Trembley wrote:

> Liam Devlin wrote:
> 
…[37 more quoted lines elided]…
> set true, so it really was an infinite loop. 


Okay, Arnold, I was just winging it from your code snippet.

> It was an unusual
> application, a started task using the H&W SYSB product to capture
…[8 more quoted lines elided]…
> true.


Aha!
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 4)_

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-05-30T22:10:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF6A332.1030605@optonline.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:

> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
> news:ad2i5p$pb3$1@coco.singnet.com.sg...
…[5 more quoted lines elided]…
> PERFORM UNTIL (in COBOL) = DO WHILE (in less robust languages)


<snicker>

Sim Choon Howe's probably thinking PERFORM UNTIL is very much like DO 
UNTIL, not DO WHILE.

> You can even:
> 
> PERFORM WITH NO LIMIT
> 
> which is just about forever.


Which is a "Do Forever" in a truly robust language, e.g., REXX.


Is Sim Choon Howe clear on PERFORM vs. PERFORM WITH TEST AFTER?


BTW, M. Mouse, what's the difference between "PERFORM" and "PERFORM WITH 
NO LIMIT"?
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 5)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-05-31T23:59:32+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad86q3$bi1$1@coco.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net>`

```
Oh dear,
Can i say Do until means  do something until the counter reach a certain
value?

Do while-- keep doing until condition is met

isn't that the same?



> Is Sim Choon Howe clear on PERFORM vs. PERFORM WITH TEST AFTER?

I got mixs up. PERFORM is similiar to subroutine procedure?
Can explain a little bit more on PERFORM WITH TEST AFTER?

I am new to cobol, thanks for being patience with me

"Liam Devlin" <LiamDD@optonline.net> wrote in message
news:3CF6A332.1030605@optonline.net...
> JerryMouse wrote:
>
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-31T21:40:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg>`

```

"Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
news:ad86q3$bi1$1@coco.singnet.com.sg...
> Oh dear,
> Can i say Do until means  do something until the counter reach a certain
…[4 more quoted lines elided]…
> isn't that the same?

Well, you can't say "DO" (unless you're writing in Fortran).

>
>
…[4 more quoted lines elided]…
> Can explain a little bit more on PERFORM WITH TEST AFTER?

PERFORM is a very robust and powerful construct and it has lots of little
knobs and switches.

Originally you had:

1. PERFORM procedure-name (where procedure-name was a paragraph somewhere
else in the program). In that regard, it's similar to a VB function or a
subroutine in other languages.

2. PERFORM procedure-name THRU another-name (where another-name was yet
another paragraph, so everything between the beginning of procedure-name and
the last statement of another-name got executed)

3. PERFORM procedure-name nnnn TIMES (do the procedure-name nnnn times)

4. PERFORM procedure-name UNTIL terminal-condition

5. PERFORM procedure-name VARYING x FROM y BY z UNTIL terminal-condition
(example: PERFORM MYLOOP VARYING MYINDX FROM 1 BY 1 UNTIL MYINDX > 100)

In #5, the terminal condition is tested at the beginning of the procedure.
So, if the terminal condition is true when the computer hits the PERFORM
statement, the code pointed to by the PERFORM statement is skipped. If you
always want the code executed at least once, you can add the phrase WITH
TEST AFTER to the PERFORM statement. WITH TEST BEFORE is implied.

6. PERFORM (any of the above constructs without a procedure name), followed
by code to execute, followed by END-PERFORM. This is the so-called "In-Line
Perform" and doesn't require a separate procedure somewhere else. For
example:

PERFORM VARYING INDX FROM 1 BY 1 UNTIL INDX > 100
   MOVE ZERO TO MYNUM (INDX)
   END-PERFORM.

or, a more useful example:

READ MYFILE.    *>so-called 'priming read'
PERFORM UNTIL MYFILE-STATUS NOT = '00'
    process record
   READ MYFILE
END-PERFORM.

There's more. Much more.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-01T02:04:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rYVJ8.4579$b73.2315@nwrddc01.gnilink.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com>`

```
JerryMouse <nospam@invalid.com> wrote in message
news:G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com...
> Well, you can't say "DO" (unless you're writing in Fortran).

or BASIC.

MCM
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 8)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-06-01T04:23:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-XIedExd940bB@thishost>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <rYVJ8.4579$b73.2315@nwrddc01.gnilink.net>`

```
On Sat, 1 Jun 2002 02:04:07 UTC, "Michael Mattias" 
<michael.mattias@gte.net> wrote:

> JerryMouse <nospam@invalid.com> wrote in message
> news:G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com...
…[3 more quoted lines elided]…
> 

Wash your mouth out with soap..... :-)
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 8)_

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-06-02T05:50:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF9B21E.4060701@optonline.net>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <rYVJ8.4579$b73.2315@nwrddc01.gnilink.net>`

```
Michael Mattias wrote:

> JerryMouse <nospam@invalid.com> wrote in message
> news:G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com...
…[4 more quoted lines elided]…
> or BASIC.


Or REXX, or PL/I (IIRC), etc. Pretty much everything *except* COBOL that 
I've seen.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 7)_

- **From:** "Sim Choon Howe " <schowe@singnet.com.sg>
- **Date:** 2002-06-04T00:03:16+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adg456$dc$1@clematis.singnet.com.sg>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com>`

```
Thanks Jerry!
"JerryMouse" <nospam@invalid.com> wrote in message
news:G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com...
>
> "Sim Choon Howe " <schowe@singnet.com.sg> wrote in message
…[29 more quoted lines elided]…
> another paragraph, so everything between the beginning of procedure-name
and
> the last statement of another-name got executed)
>
…[13 more quoted lines elided]…
> 6. PERFORM (any of the above constructs without a procedure name),
followed
> by code to execute, followed by END-PERFORM. This is the so-called
"In-Line
> Perform" and doesn't require a separate procedure somewhere else. For
> example:
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-04T07:48:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CFC62AC.CC72024D@Azonic.co.nz>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <adg456$dc$1@clematis.singnet.com.sg>`

```
"JerryMouse" <nospam@invalid.com> wrote 

> 4. PERFORM procedure-name UNTIL terminal-condition
>
…[5 more quoted lines elided]…
> statement, the code pointed to by the PERFORM statement is skipped. 

This may confuse some.  You should have said "In #4, the terminal .."

It is true that the terminal condition is tested in #5 but only after
the FROM phrase, so in #5 the code will not be skipped regardless of the
state of 'MyTndx' prior to the PERFORM.

> > READ MYFILE.    *>so-called 'priming read'
> > PERFORM UNTIL MYFILE-STATUS NOT = '00'
> >     process record
> >    READ MYFILE
> > END-PERFORM.

A file status should only be tested for success in the first byte. 
Testing both bytes may result in false failures being indicated.  For
example a status of "02" is a successful read and there are valid
duplicates in an alternate key.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-06-03T21:34:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VhRK8.108552$Kp.11000645@bin7.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <adg456$dc$1@clematis.singnet.com.sg> <3CFC62AC.CC72024D@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3CFC62AC.CC72024D@Azonic.co.nz...
> "JerryMouse" <nospam@invalid.com> wrote
>
…[5 more quoted lines elided]…
> > In #5, the terminal condition is tested at the beginning of the
procedure.
> > So, if the terminal condition is true when the computer hits the PERFORM
> > statement, the code pointed to by the PERFORM statement is skipped.
…[6 more quoted lines elided]…
>
If you're referring to the example, the original condition of MYINDX, I
agree, is irrelevant since MYINDX is under complete control of the PERFORM
construct.

Otherwise, the original #5 and it's explanation is correct.

The terminal condition is tested before the perform. If the terminal
condition is satisfied, the perform code is not executed. Not even once.

MOVE -1 TO TERMINAL-CONDITION.
PERFORM VARYING INDX FROM 1 BY 1 UNTIL
    INDX > TERMINAL-CONDITION
   (some code)
END-PERFORM.

(some code) is never executed.

Now you could force (some code) to be executed at least once by including
the WITH TEST AFTER phrase.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-04T17:29:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CFCEAE9.FEE2B7E9@Azonic.co.nz>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <adg456$dc$1@clematis.singnet.com.sg> <3CFC62AC.CC72024D@Azonic.co.nz> <VhRK8.108552$Kp.11000645@bin7.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:

> > > 5. PERFORM procedure-name VARYING x FROM y BY z UNTIL terminal-condition
> > > (example: PERFORM MYLOOP VARYING MYINDX FROM 1 BY 1 UNTIL MYINDX > 100)
…[4 more quoted lines elided]…
> > > statement, the code pointed to by the PERFORM statement is skipped.

> Otherwise, the original #5 and it's explanation is correct.

But misleading.  Your example in #5 would be performed 100 times
regardless of whether the 'terminal condition is true when it hits the
PERFORM statement'. 

If 'MyIndx' were 200 when it 'hit the perform' the terminal condition is
true but it still does the perform 100 times (other things being equal).
 
> The terminal condition is tested before the perform. If the terminal
> condition is satisfied, the perform code is not executed. Not even once.

No. Wrong. The terminal condition is _NOT_ tested _before_ the PERFORM,
it is tested _during_ the PERFORM, after any VARYING .. FROM phrases and
before executing the specified procedure name or inline code.

> MOVE -1 TO TERMINAL-CONDITION.
> PERFORM VARYING INDX FROM 1 BY 1 UNTIL
…[4 more quoted lines elided]…
> (some code) is never executed.

But the VARYING ... FROM phrase is.  That is: the PERFORM will be
executed at least as far as INDX being set to 1 before the test is
done.  This is not the same as 'Before the PERFORM' or 'when it hits the
PERFORM'.

In your revised example the 'terminal condition' remains true after the
VARYING phrase, in the original example #5, the terminal condition may
have been true when it 'hits' the PERFORM, but the VARYING phrase
changed this, so your reference to 'before the PERFORM' was misleading
(ie wrong).
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 11)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-06-04T13:17:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g53L8.122873$Oa1.12021505@bin8.nnrp.aus1.giganews.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <3d7858be.0205282233.ef4eacd@posting.google.com> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <adg456$dc$1@clematis.singnet.com.sg> <3CFC62AC.CC72024D@Azonic.co.nz> <VhRK8.108552$Kp.11000645@bin7.nnrp.aus1.giganews.com> <3CFCEAE9.FEE2B7E9@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3CFCEAE9.FEE2B7E9@Azonic.co.nz...
> JerryMouse wrote:
>
> > > > 5. PERFORM procedure-name VARYING x FROM y BY z UNTIL
terminal-condition
> > > > (example: PERFORM MYLOOP VARYING MYINDX FROM 1 BY 1 UNTIL MYINDX >
100)
> > > >
> > > > In #5, the terminal condition is tested at the beginning of the
> > procedure.
> > > > So, if the terminal condition is true when the computer hits the
PERFORM
> > > > statement, the code pointed to by the PERFORM statement is skipped.
>
…[4 more quoted lines elided]…
> PERFORM statement'.

Forget the example.

>
> If 'MyIndx' were 200 when it 'hit the perform' the terminal condition is
…[27 more quoted lines elided]…
>

OK. I surrender to the protestations of the pedantic fuddy-duddy cartel.

I should have said:

"The terminal condition is tested before any of the executable statements
comprising the scope of the perform are executed."

I apologize to all for summoning the demons who infest the wire-ways with
admonitions of precision way beyond that which is required for government
work.

I'm off to measure my latest purchase of milk to the nearest microliter.
```

###### ↳ ↳ ↳ Re: dynamic index

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-06-05T13:43:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0206051243.33997de3@posting.google.com>`
- **References:** `<ad03p7$i2b$1@coco.singnet.com.sg> <ad2i5p$pb3$1@coco.singnet.com.sg> <gL6J8.67127$Gs.6168744@bin5.nnrp.aus1.giganews.com> <3CF6A332.1030605@optonline.net> <ad86q3$bi1$1@coco.singnet.com.sg> <G5SJ8.17863$4i.2084778@bin2.nnrp.aus1.giganews.com> <adg456$dc$1@clematis.singnet.com.sg> <3CFC62AC.CC72024D@Azonic.co.nz> <VhRK8.108552$Kp.11000645@bin7.nnrp.aus1.giganews.com> <3CFCEAE9.FEE2B7E9@Azonic.co.nz> <g53L8.122873$Oa1.12021505@bin8.nnrp.aus1.giganews.com>`

```
"JerryMouse" <nospam@invalid.com> wrote 

JM > Otherwise, the original #5 and it's explanation is correct.

Well, actually, no.  It was wrong.

> OK. I surrender to the protestations of the pedantic fuddy-duddy cartel.
> 
> I apologize to all for summoning the demons who infest the wire-ways with
> admonitions of precision way beyond that which is required for government
> work.

I can't comment on whether your 'precision' is adequate for the work
that you do, that should be an issue between you and your employer.

In general, your precision would have been adequate if you were
conversing with the experienced members of this group, they may
understand that it was imprecise but would know what actually
occurred.

However, you were responding to a student who had no experience or
knowledge that would allow him to filter out misleading or wrong
information.  You were attempting to teach a particular aspect of the
language and for this a higher standard of correctness is required.


> I'm off to measure my latest purchase of milk to the nearest microliter.

That should be 'microlitre'.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
