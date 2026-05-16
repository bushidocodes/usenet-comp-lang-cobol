[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL putting a program to sleep

_15 messages · 9 participants · 2003-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL putting a program to sleep

- **From:** bill <xx@xx.net>
- **Date:** 2003-01-10T13:59:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
I have a Micro Focus COBOL program that  checks for presence of a file
that is created by another process and placed on the LAN. I am using
the MF subroutine CBL_CHECK_FILE_EXIST to do this.  If the file exists
the program does its thing, but if it doesn't exist, I want the
program to wait for some period of time and then look for the file
again.  I'd like to do this so the program relinquishes control rather
than doing something like a counting loop that will use up CPU time. 

I've tried using the CBL_THREAD_SLEEP subroutine but it does not seem
to work for me. No matter what millisecond value I give it, it returns
immediately with a good return code.

Any ideas? 

TIA
Mike
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-10T17:04:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E1F6DAF.2060508@Sympatico.ca>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
The simple way is to convert it to a run once program, then schedule it 
to run once per minute with the task scheduler.  I am presuming a 
windows environment.  That simplifies matters immensely with the the 
data recovery/maintenance/ and start/stop procedures as well.

I made that change in a SAP project that was talking to cobol using the 
"go to sleep method", and it was a vast improvement.  It has a 
resolution of once per minute, but you do not get into having to go out 
and restart it problems, or rebooting problems nearly as often.

Basically, you just rip out all the sleep code, and set it up as a run 
once command line program. The put the command line in the scheduler. 
Nice and simple.

Donald

bill wrote:
> I have a Micro Focus COBOL program that  checks for presence of a file
> that is created by another process and placed on the LAN. I am using
…[13 more quoted lines elided]…
> Mike
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** bill <xx@xx.net>
- **Date:** 2003-01-11T10:04:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i2g02vkl8hm0tceiqov6ipg9cdf9h6mu6r@4ax.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <3E1F6DAF.2060508@Sympatico.ca>`

```
Donald,

Thanks for this. I never thought of that! 

Mike



On Fri, 10 Jan 2003 17:04:47 -0800, Donald Tees
<Donald_Tees@Sympatico.ca> wrote:

>The simple way is to convert it to a run once program, then schedule it 
>to run once per minute with the task scheduler.  I am presuming a 
…[30 more quoted lines elided]…
>> Mike
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-10T17:13:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301101713.25339d54@posting.google.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
bill <xx@xx.net> wrote

> I want the
> program to wait for some period of time and then look for the file
> again.  I'd like to do this so the program relinquishes control rather
> than doing something like a counting loop that will use up CPU time. 

On DOS or Windows you can use the INT 0x'2F' AX = 0x'1680' despatch
call, while checking time. This isn't a true 'sleep' as it merely
releases the timeslice to the next process, but it doesn't use CPU
time that another program can use.

Fujitsu has a CALL "CBL_YIELD_RUN_UNIT" that also is just a despatch.

On Unix/Linux you can CALL "SYSTEM" USING "sleep n" & 0x'00'.
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2003-01-11T02:33:30
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avnvot$a6t$1@news6.svr.pol.co.uk>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
If you are using a 16bit compier (ie DOS) then simply use ACCEPT x FROM DATE
in a tight loop. By default the clock is updated 18.2 times per second under
DOS
which windows understands and will optimise.

"bill" <xx@xx.net> wrote in message
news:v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com...
> I have a Micro Focus COBOL program that  checks for presence of a file
> that is created by another process and placed on the LAN. I am using
…[13 more quoted lines elided]…
> Mike
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2003-01-11T03:18:37
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avo2df$30m$1@newsg1.svr.pol.co.uk>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <avnvot$a6t$1@news6.svr.pol.co.uk>`

```
Should have typed ACCEPT x FROM TIME although DATE may
also work.
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-01-10T22:37:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0301102237.7ff4dd95@posting.google.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
Mike,

What platform is your program running on?
Which Version of MF COBOL?
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** bill <xx@xx.net>
- **Date:** 2003-01-11T10:02:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<puf02vobh7gs224ht4u4ea4rvlfkus5cmf@4ax.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <bfdfc3e8.0301102237.7ff4dd95@posting.google.com>`

```
Thane,  

I am running Micro Focus Net Express 3.1 on W2K.

MIke


On 10 Jan 2003 22:37:04 -0800, thaneh@softwaresimple.com (Thane
Hubbell) wrote:

>Mike,
>
>What platform is your program running on?
>Which Version of MF COBOL?
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** "Russell Styles" <RWSTYLES@comcast.net>
- **Date:** 2003-01-11T03:52:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_secndrxBNRURoKjXTWcqQ@comcast.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```

"bill" <xx@xx.net> wrote in message
news:v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com...
> I have a Micro Focus COBOL program that  checks for presence of a file
> that is created by another process and placed on the LAN. I am using
…[13 more quoted lines elided]…
> Mike


    If you are using Microfocus net express on Windows 95 or above,
the following will work.

    This was all lined up in editor.
Looks okay in courier I guess.


       IDENTIFICATION DIVISION.
       PROGRAM-ID.
           WINSLEEP.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
000200 SOURCE-COMPUTER.  IBM-PC.
000300 OBJECT-COMPUTER.  IBM-PC.
       SPECIAL-NAMES.
           CALL-CONVENTION 74 IS WINAPI.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
005400 01 ULONG    IS TYPEDEF PIC 9(9) COMP-5.
005700 01 DWORD    IS TYPEDEF ULONG.
       01  MY-WS.
         03 MAIN-WS.
           05 SLEEP-TIME   DWORD.
      ****************************************
      *****************************************
      *  1000 = 1 SECOND
       77 PASS-SLEEP-TIME         PIC 9(6).
      *****************************************
      *****************************************
      *****************************************
      *****************************************
       PROCEDURE DIVISION USING PASS-SLEEP-TIME.
       MAIN-SEC SECTION.
           PERFORM MY-DELAY.
       THE-EXIT.
           EXIT PROGRAM.
       THE-STOP.
           STOP RUN.
      *****************************************
      *****************************************
       MY-DELAY.
           IF PASS-SLEEP-TIME NOT NUMERIC
             EXIT PARAGRAPH
           END-IF.
           CALL "COB32API".
           MOVE PASS-SLEEP-TIME TO SLEEP-TIME.
      $SET CASE       *> Do not change case of "Sleep"
           CALL WINAPI "Sleep" USING BY VALUE SLEEP-TIME.
      $SET NOCASE
      ******************************************
      ******************************************


    If you are using a 16 bit compiler, I suggest looking into using the
task scheduler.  I have never managed to access
the windows 32 bit API with Microfocus 16 bit workbench.
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** bill <xx@xx.net>
- **Date:** 2003-01-11T10:03:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m1g02vkv7j79ru4cp9881mi5seqei9piu1@4ax.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <_secndrxBNRURoKjXTWcqQ@comcast.com>`

```
Thanks for the tip and sample code! 

Mike



On Sat, 11 Jan 2003 03:52:53 -0500, "Russell Styles"
<RWSTYLES@comcast.net> wrote:

>
>"bill" <xx@xx.net> wrote in message
…[77 more quoted lines elided]…
>
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** renfrewthejust@yahoo.com (Renfrew)
- **Date:** 2003-01-12T04:02:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avqpc2$kj5$1@bob.news.rcn.net>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
In article <v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>, xx@xx.net says...
>
>I have a Micro Focus COBOL program that  checks for presence of a file
…[14 more quoted lines elided]…
>Mike


I like to use the time-out setting on an ACCEPT statement to create 
sleeper intervals.  It works just great, does not seem to dog the cpu, 
and also provides ongoing opportunity during runtime to cleanly make 
the program close&exit, which is of course quite preferable to using 
ctrl/alt/delete.  

I can dig up sample code later on if you want (am away somewhere else 
at the moment).

DaveM

(Remove "SPAMOUT" if replying to my email address)
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-01-12T15:16:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TEfU9.7221$qU5.5561707@newssrv26.news.prodigy.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <avqpc2$kj5$1@bob.news.rcn.net>`

```
"Renfrew" <renfrewthejust@yahoo.com> wrote in message
news:avqpc2$kj5$1@bob.news.rcn.net...
> In article <v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>, xx@xx.net says...
> >
…[7 more quoted lines elided]…
> >

If this is running on Windows(r), you can write a program which uses the
FindFirstChangeNotification and WaitforSingle Object API calls. This works
on all Windows systems. There is an option to 'time out' after 'n' seconds
even if a change has not occured.

If you do not have to operate on Windows 9x, on Win2000/NT/XP there is a
ReadDirectoryChangesW function you can use, but that works a little
differently.

(Weird. I am working on a project 'as we speak' where this is exactly what I
am doing).

If this is Windows, you don't feel comfortable calling the Win API but would
feel comfortable calling a function in a DLL, and have a modest budget, drop
me a note and I'll put together a  proposal on a DLL you could call from
COBOL using  "CALL (function) USING..xx RETURNING yyy " and that function
would not return until your file appeared. Although, you'd probably want to
return more often so you could exit gracefully on demand, something like...

  05  CALL-Status         PIC X(01).
       88  changeFound     VALUE IS 'C'.
       88  Timeout             VALUE IS 'T'.
....
  PERFORM UNTIL  Quit
    CALL "function"  using parameter returning CALL-STATUS
    EVALUATE TRUE
       WHEN changeFound
            perform process-the-change  end-perform
      WHEN timeout
             IF (Condition mandating exit)
                 SET Quit to TRUE
             END-IF
   END-EVALUATE
 END-PERFORM
```

##### ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** bill <xx@xx.net>
- **Date:** 2003-01-12T19:46:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1j642vc3hu5u2aok5u7ti36ul7t1t8flf3@4ax.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <avqpc2$kj5$1@bob.news.rcn.net>`

```
thanks Dave, I'd like to see the sample code.



On 12 Jan 2003 04:02:10 GMT, renfrewthejust@yahoo.com (Renfrew) wrote:

>In article <v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>, xx@xx.net says...
>>
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF COBOL putting a program to sleep

- **From:** renfrewthejust@yahoo.com (Renfrew)
- **Date:** 2003-01-17T01:34:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b07mk1$biu$1@bob.news.rcn.net>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com> <avqpc2$kj5$1@bob.news.rcn.net> <1j642vc3hu5u2aok5u7ti36ul7t1t8flf3@4ax.com>`

```
Bill,

Sorry it took so long to get back to you.  

Here is a skeletal version of some "sleeper code" logic that 
works via TIME-OUT parameter on ACCEPT statement.  Please 
understand that this was gleaned from a rather more cryptic 
working example, so do not presume that this particular code 
is error free, but it should still illustrate the concept 
well enough.  

To reduce the burden on daytime/primetime network traffic we 
often start our long batch update jobs when we leave at night, 
but this used to cause problems because the system backup 
would skip major files while the batch job was running.  We 
greatly reduced this problem by developing sleeper code which 
makes the program release the files during a pre-established 
time frame (when the system backup was supposed to be running) 
and then re-awakens to pick up right where it left off.  

Not shown in this particular example is an even better way 
that we learned to handle this type of situation, because the 
system backup sometimes runs longer than expected:  Instead of 
relying on a specific ending time, the program instead 
periodically examines the archive flag on the master file(s) 
during sleep mode.  Once the archive flag is cleared the 
program knows that the backup is complete so it can then wake 
up and resume processing.  




       0000-CONTROL.

           Move 60 to SLEEP-CHECK-INTERVAL-SECONDS.

           Perform OPEN-FILES. 
           
           Perform READ-NEXT-INPUT-RECORD.
           If EOF-IN
              perform SCREAM-AND-DIE.

           Perform ACCEPT-CURRENT-DATE-TIME.

           Perform 1000-MAIN-LOOP-PROCESSING
            until (EOF-IN).

           STOP RUN.


       1000-MAIN-LOOP-PROCESSING. 
           On 1 and every 100
              Perform SLEEP-IF-NECESSARY.

           <Do whatever stuff> 

           Write MASTER-REC.

           Perform READ-NEXT-INPUT-RECORD.
           

       SLEEP-IF-NECESSARY.
           Perform CHECK-SLEEP-CLOCK.
       
           If IT-IS-TIME-TO-SLEEP
              Perform SLEEP-CYCLE-PROCESSING.
       
       
       SLEEP-CYCLE-PROCESSING.
           Move IN-KEY to HOLD-KEY. 
           Perform CLOSE-FILES. 
       
           Perform SLEEP-CYCLE-LOOP until (IT-IS-TIME-TO-BE-AWAKE).
       
           Perform OPEN-FILES. 
           Move HOLD-KEY to IN-KEY.
           Perform START-AND-READ-IN-FILE.
           If FILE-STATUS not equal "00" and "02"
              Perform SCREAM-AND-DIE.
       
       
       SLEEP-CYCLE-LOOP.
           Display SleeperScreen.
           Accept SleeperScreen TIME-OUT SLEEP-CHECK-INTERVAL-SECONDS.
           Perform CHECK-SLEEP-CLOCK.
       
       
       CHECK-SLEEP-CLOCK.
           Perform ACCEPT-CURRENT-DATE-TIME.
           Move zero to IT-IS-TIME-TO-SLEEP-SW.
           If (CURRENT-DATE-TIME not less than SLEEP-START-DATE-TIME)
           and (CURRENT-DATE-TIME < SLEEP-END-DATE-TIME)
              Move 1 to IT-IS-TIME-TO-SLEEP-SW
           End-if.


Note:  In this example the screen "SleepScreen" merely displays 
time frame parameters along with the fact that the program is 
presently asleep, and it pacifies the ACCEPT statement with an 
essentially do-nothing i-o field.  Of course, instead of using 
a do-nothing field you could easily add more logic enabling the 
user to enter an overriding request, e.g., to wake-up-right-away 
or abort-processing.

Hope this helps.

DaveM
(Remove "SPAMOUT" if replying to my email address)


In article <1j642vc3hu5u2aok5u7ti36ul7t1t8flf3@4ax.com>, xx@xx.net says...
>
>thanks Dave, I'd like to see the sample code.
…[38 more quoted lines elided]…
>
```

#### ↳ Re: MF COBOL putting a program to sleep

- **From:** "Gael Wilson" <gael.wilson@nospam.microfocus.com>
- **Date:** 2003-01-13T15:53:08
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avuml8$1rl$1@hyperion.microfocus.com>`
- **References:** `<v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com>`

```
Bill,

Make sure you are using the threaded run-time. If you are not, the
CBL_THREAD_SLEEP is a dummy function that just returns because the threading
APIs are only supported on the threaded run-time .

"bill" <xx@xx.net> wrote in message
news:v49u1vgioc1r9fdoao5fkj0ut76sdkbpup@4ax.com...
> I have a Micro Focus COBOL program that  checks for presence of a file
> that is created by another process and placed on the LAN. I am using
…[13 more quoted lines elided]…
> Mike
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
