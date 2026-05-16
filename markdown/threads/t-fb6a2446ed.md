[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# isam data files

_10 messages · 4 participants · 2002-09_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### isam data files

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2002-09-25T20:25:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bZok9.681$wH.60@sccrnsc01>`

```
Hello all,

I have used for years an old DOS compiler to create and use ISAM files.

Recently got Net Express and have been benchmarking performance and found
file i-o REALLY SLOW.

For example I can create with DOS compiler a 100,000 record isam file in
about 10 seconds
using NetExpress it takes 150 seconds

should I go to a third party file system to get faster i-o ?

any suggestions greatly appreciated


TIA,


J.W.
```

#### ↳ Re: isam data files

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-26T01:56:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vPtk9.13809$8o3.304873@twister.austin.rr.com>`
- **References:** `<bZok9.681$wH.60@sccrnsc01>`

```
Roughly speaking - You Got Something Wrong There Son.

To create a 100000 record indexed file under Windows XP (1.8ghz P4):
   AcuCobol  -  about 0.2 seconds
   MicroFocus NetExpress - 1.1 seconds
   IBM VisualAge COBOL 3.1 - 1.9 seconds / .7 seconds (BTRIEVE)
   Fujitsu COBOL 3 -- ~ 2.1 seconds

Under AIX on a modest RS/6000:
   MicroFocus - 8 seconds      (no cache)
   IBM COBOL - 11 seconds (no cache)
   Microfocus  - .3 seconds      (cache)
   IBM COBOL - .2 seconds   (cache)


Of course, Windows does cache.  The file created was six characters in length and used
the record number as the key.

-Paul


"Jason" <jasonsdog@att.net> wrote in message news:bZok9.681$wH.60@sccrnsc01...
> Hello all,
>
…[21 more quoted lines elided]…
>
```

##### ↳ ↳ Re: isam data files

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2002-09-26T04:08:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WKvk9.77863$gA4.27485@sccrnsc02>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com>`

```

Raul,

below is the source of my benchmark

would you, could you  ISAM-I-AM     compile and see if you don't get a slow
time ?


thanks again for your help


JW





  IDENTIFICATION DIVISION.
       PROGRAM-ID.   BENCH1.

********  TEST ISAM FILE PERFORMANCE ON WRITING

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FILEONE ASSIGN TO "TESTTIME.DAT"
               ORGANIZATION IS INDEXED
               ACCESS IS RANDOM
               RECORD KEY IS TEST-KEY
               ALTERNATE RECORD KEY IS TF-FIELD3 WITH DUPLICATES
               STATUS IS TEST-CODE.

       DATA DIVISION.
       FILE SECTION.
       FD  FILEONE.
       01  TEST-REC.
           03  TEST-KEY.
               05  TF-FIELD1        PIC X(20).
               05  TF-FIELD2        PIC X(16).
               05  TF-FIELD3        PIC X(11).
               05  TF-FIELD4        PIC X(15).
               05  TF-FIELD5        PIC X(25).
           03  TF-FIELD8            PIC X(144).

       WORKING-STORAGE SECTION.
       01  TEST-CODE    PIC XX.
       01  WS-FIELD3    PIC 9(12) VALUE 0.
       01  WS-FIELD2    PIC 9(11) VALUE 0.
       01  SUBA         PIC 9(7) VALUE 0.
       01  SUBB         PIC 9(7) VALUE 0.
       01  SUBC         PIC 9(7) VALUE 0.
       01  SUBD         PIC 9(7) VALUE 0.
       01  WS-TIME-START     PIC S9(8).
       01  WS-TIME-STOP      PIC S9(8).
       01  WS-BLANK-SCREEN    PIC X(1920) VALUE SPACES.
       PROCEDURE DIVISION.

       0000-RECORD-PROMPT.
           DISPLAY "HOW MANY RECORDS TO CREATE FOR THIS TEST "
               LINE 1 POSITION 1 ERASE.
           ACCEPT SUBC LINE 1 POSITION 43.
           IF SUBC = 0 STOP RUN.

           ACCEPT WS-TIME-START FROM TIME.
       0001-OPEN-FILES.
           OPEN OUTPUT FILEONE.
           DISPLAY "RECORDS MADE" LINE 1 POSITION 15 ERASE.
           DISPLAY SUBC LINE 2 POSITION 43.
           DISPLAY " REQUESTED" LINE 2 POSITION 60.
       0002-CREATE-RECORDS.
           INITIALIZE TEST-REC.
           ADD 1 TO WS-FIELD3.
           IF WS-FIELD3 > SUBC GO TO 0003-STOP.
           DIVIDE WS-FIELD3 BY 50 GIVING SUBD.
           MOVE SUBD TO TF-FIELD1.
           ADD 1 TO WS-FIELD2.
           DIVIDE WS-FIELD2 BY 10 GIVING SUBA REMAINDER SUBB.
           ADD 1000000 TO SUBD.
           MOVE SUBD TO TF-FIELD3.
           MOVE WS-FIELD3 TO TF-FIELD4.
           WRITE TEST-REC INVALID KEY GO TO ERROR-PARA.
           DISPLAY WS-FIELD3 LINE 1 POSITION 1.
           GO TO 0002-CREATE-RECORDS.

       ERROR-PARA.
           DISPLAY "ERROR AT "   LINE 5  POSITION 1.
           DISPLAY TEST-CODE     LINE 6  POSITION 1.
           DISPLAY " = FILE STATUS RETURNED" LINE 6 POSITION 4.
           DISPLAY WS-FIELD3     LINE 7  POSITION 1.
           DISPLAY SUBA          LINE 8  POSITION 1.
           DISPLAY SUBB          LINE 9  POSITION 1.
           DISPLAY SUBC          LINE 10 POSITION 1.
           DISPLAY SUBD          LINE 11 POSITION 1.

       0003-STOP.
           CLOSE FILEONE.
           ACCEPT WS-TIME-STOP FROM TIME.
           DISPLAY WS-TIME-START LINE 15 POSITION 1.
           DISPLAY WS-TIME-STOP LINE 16 POSITION 1.
           STOP RUN.

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:vPtk9.13809$8o3.304873@twister.austin.rr.com...
> Roughly speaking - You Got Something Wrong There Son.
>
…[13 more quoted lines elided]…
> Of course, Windows does cache.  The file created was six characters in
length and used
> the record number as the key.
>
…[3 more quoted lines elided]…
> "Jason" <jasonsdog@att.net> wrote in message
news:bZok9.681$wH.60@sccrnsc01...
> > Hello all,
> >
> > I have used for years an old DOS compiler to create and use ISAM files.
> >
> > Recently got Net Express and have been benchmarking performance and
found
> > file i-o REALLY SLOW.
> >
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: isam data files

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-26T05:15:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CJwk9.14414$8o3.345317@twister.austin.rr.com>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com> <WKvk9.77863$gA4.27485@sccrnsc02>`

```
[ I sent this along to your home e-mail as well. Excuse the types, I am up playing when I should be asleep. ]

The DISPLAY's are very costly; so I removed them for testing a second round, and because
I didn't feel like fixing the DISPLAYs for the Fuji dialect.  I used 100000 records as you specified in your original message, they
all ran on the same machine.

Yours,
-Paul



23470964   (With DISPLAYS, MicroFocus 1396)
23472360

00021335   (Without DISPLAYS, Microfocus 771)
00022106


23534110  (With DISPLAYS, AcuCBL  7277)
23541387

23571050   (Without DISPLAY, AcuCBL 1587)
23572637

00051954   (Without DISPLAYS, Fujitsu COBOL V3, 325)
00052279


"Jason" <jasonsdog@att.net> wrote in message news:WKvk9.77863$gA4.27485@sccrnsc02...
>
> Raul,
…[154 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: isam data files

_(reply depth: 4)_

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2002-09-26T15:15:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mwFk9.216879$Jo.85770@rwcrnsc53>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com> <WKvk9.77863$gA4.27485@sccrnsc02> <CJwk9.14414$8o3.345317@twister.austin.rr.com>`

```
Paul,


thanks for the reply and the testing
you must be in the western US or you stay up WAY too late


I will remove the displays and see what I get

thanks a bunch


JW




"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:CJwk9.14414$8o3.345317@twister.austin.rr.com...
> [ I sent this along to your home e-mail as well. Excuse the types, I am up
playing when I should be asleep. ]
>
> The DISPLAY's are very costly; so I removed them for testing a second
round, and because
> I didn't feel like fixing the DISPLAYs for the Fuji dialect.  I used
100000 records as you specified in your original message, they
> all ran on the same machine.
>
…[22 more quoted lines elided]…
> "Jason" <jasonsdog@att.net> wrote in message
news:WKvk9.77863$gA4.27485@sccrnsc02...
> >
> > Raul,
…[3 more quoted lines elided]…
> > would you, could you  ISAM-I-AM     compile and see if you don't get a
slow
> > time ?
> >
…[122 more quoted lines elided]…
> > > > I have used for years an old DOS compiler to create and use ISAM
files.
> > > >
> > > > Recently got Net Express and have been benchmarking performance and
…[3 more quoted lines elided]…
> > > > For example I can create with DOS compiler a 100,000 record isam
file in
> > > > about 10 seconds
> > > > using NetExpress it takes 150 seconds
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: isam data files

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-09-26T05:25:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tTwk9.52958$1C2.2437872@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com> <WKvk9.77863$gA4.27485@sccrnsc02>`

```

    Turns out that what you are really testing here is
the display verb.  Net express's ADIS subsystem
is REALLY REALLY slow.

    Try displaying the record number only every 100
writes instead of every write.  That will even things out.




"Jason" <jasonsdog@att.net> wrote in message
news:WKvk9.77863$gA4.27485@sccrnsc02...
>
> Raul,
…[3 more quoted lines elided]…
> would you, could you  ISAM-I-AM     compile and see if you don't get a
slow
> time ?
>
…[122 more quoted lines elided]…
> > > I have used for years an old DOS compiler to create and use ISAM
files.
> > >
> > > Recently got Net Express and have been benchmarking performance and
…[3 more quoted lines elided]…
> > > For example I can create with DOS compiler a 100,000 record isam file
in
> > > about 10 seconds
> > > using NetExpress it takes 150 seconds
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: isam data files

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-09-27T21:58:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d94c545_1@Usenet.com>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com>`

```

Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote in message
news:vPtk9.13809$8o3.304873@twister.austin.rr.com...
> Roughly speaking - You Got Something Wrong There Son.
>
<snip>
>
> Of course, Windows does cache.  The file created was six characters in
length and used
> the record number as the key.
>
> -Paul
>
Er...if the file created was 6 characters in length then Jason is not the
only one who got something wrong...<G>

I think you mean each record was 6 characters...

This is then not a fair test.(Insofar as it does NOT test the conditions he
stated...)

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: isam data files

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-28T00:06:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Co6l9.29654$Fw2.657593@twister.austin.rr.com>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <vPtk9.13809$8o3.304873@twister.austin.rr.com> <3d94c545_1@Usenet.com>`

```
Certainly I meanr that the record length was six Peter. :)
But it was a fair test, and the results received vindication when I ran Jason's test program as well.
<grin>

-Paul

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:3d94c545_1@Usenet.com...
>
> Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote in message
…[28 more quoted lines elided]…
>                 http://www.usenet.com
```

#### ↳ Re: isam data files

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-09-26T05:25:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rTwk9.52957$1C2.2436222@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bZok9.681$wH.60@sccrnsc01>`

```

"Jason" <jasonsdog@att.net> wrote in message
news:bZok9.681$wH.60@sccrnsc01...
> Hello all,
>
…[19 more quoted lines elided]…
>

    Could it be that you switched from using DOS O/S to windows?
The "lock mode" in the select statement can make a HUGE
difference when on a network (windows is always on a "network"
of sorts.

    If you still have the DOS PC around, try running with and without SHARE.
You might be shocked at the difference with "LOCK MODE MANUAL".

    "LOCK MODE EXCLUSIVE" is fast, as is no lock mode at all.

    This is most obvious with small records.
```

##### ↳ ↳ Re: isam data files

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2002-09-26T15:15:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lwFk9.409505$kp.1196168@rwcrnsc52.ops.asp.att.net>`
- **References:** `<bZok9.681$wH.60@sccrnsc01> <rTwk9.52957$1C2.2436222@bgtnsc04-news.ops.worldnet.att.net>`

```
Russell,


thanks for the reply

I am actually using the same VAIO laptop using XP Home  for the benchmark

will try removing the display counter and see what happens



"Russell Styles" <RWSTYLES@worldnet.att.net> wrote in message
news:rTwk9.52957$1C2.2436222@bgtnsc04-news.ops.worldnet.att.net...
>
> "Jason" <jasonsdog@att.net> wrote in message
…[5 more quoted lines elided]…
> > Recently got Net Express and have been benchmarking performance and
found
> > file i-o REALLY SLOW.
> >
…[21 more quoted lines elided]…
>     If you still have the DOS PC around, try running with and without
SHARE.
> You might be shocked at the difference with "LOCK MODE MANUAL".
>
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
