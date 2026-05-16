[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multiple Key-Strokes after Receive(s)

_5 messages · 4 participants · 2000-10_

---

### Multiple Key-Strokes after Receive(s)

- **From:** Bill Gaphardt <bill_gaphardt@my-deja.com>
- **Date:** 2000-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rd9d6$7b7$1@nnrp1.deja.com>`

```
  I have a CICS program that requires me to receive data from the
terminal when the trans-id is typed in by the operator: XALS AUTO or
XALS STOP (or XALS with no data).  I do an ASSIGN STARTCODE to
determine that I was started with Terminal Input, then I do a CICS
RECEIVE INTO an area that's 9 characters long.  AUTO tells it to run as
a background task.  STOP, of course, tells it to stop.  And, the trans-
id with no data tells it to show the screen (SEND the MAP).

  The problem occurs when I type the trans-id with no data and the
screen comes up.  From that point on, if I hit enter I have to hit it
twice.  The same goes for PF-keys - hit 'em twice before they take
affect.  It appears the RECEIVE of the trans-id and data (or no data)
happens the first time I press a key and the RECEIVE of the MAP happens
on the second key-stroke.

  The question is... How do I get my program to react to the first key-
stroke ?





Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Multiple Key-Strokes after Receive(s)

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F53B88EDBB43C977.F0A4BB091409D482.F77F02280F7EB286@lp.airnews.net>`
- **References:** `<8rd9d6$7b7$1@nnrp1.deja.com>`

```
On Tue, 03 Oct 2000 18:43:52 GMT, Bill Gaphardt
<bill_gaphardt@my-deja.com> enlightened us:

>  I have a CICS program that requires me to receive data from the
>terminal when the trans-id is typed in by the operator: XALS AUTO or
…[16 more quoted lines elided]…
>

I expect that you have something wrong in your SEND MAP command.  Post
what you have.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-

Why does Sea World have a seafood restaurant? I'm halfway through my
fishburger and I realize, Oh my....I could be eating a slow learner.  

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

#### ↳ Re: Multiple Key-Strokes after Receive(s)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fpc4usglmr6se57m53r6k8bpq4bsina6c3@4ax.com>`
- **References:** `<8rd9d6$7b7$1@nnrp1.deja.com>`

```
On Tue, 03 Oct 2000 18:43:52 GMT Bill Gaphardt <bill_gaphardt@my-deja.com>
wrote:

:>  I have a CICS program that requires me to receive data from the
:>terminal when the trans-id is typed in by the operator: XALS AUTO or
:>XALS STOP (or XALS with no data).  I do an ASSIGN STARTCODE to
:>determine that I was started with Terminal Input, then I do a CICS
:>RECEIVE INTO an area that's 9 characters long.  AUTO tells it to run as
:>a background task.  STOP, of course, tells it to stop.  And, the trans-
:>id with no data tells it to show the screen (SEND the MAP).

:>  The problem occurs when I type the trans-id with no data and the
:>screen comes up.  From that point on, if I hit enter I have to hit it
:>twice.  The same goes for PF-keys - hit 'em twice before they take
:>affect.  It appears the RECEIVE of the trans-id and data (or no data)
:>happens the first time I press a key and the RECEIVE of the MAP happens
:>on the second key-stroke.

:>  The question is... How do I get my program to react to the first key-
:>stroke ?

Sounds like a bug.

What does CEDF show as happening?
```

#### ↳ Re: Multiple Key-Strokes after Receive(s)

- **From:** Bill Gaphardt <bill_gaphardt@my-deja.com>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rvpul$jm7$1@nnrp1.deja.com>`
- **References:** `<8rd9d6$7b7$1@nnrp1.deja.com>`

```


  I found someone at work who answered my question...

  I only need to receive the data with the startcode once (and then
send the map).  From that point on, I need only receive the map (no
start data).  So, I check EIBCALEN and only receive the start data when
it's equal to zero.  That way, I never do 2 receives in the same
cycle.  Simple !




Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Multiple Key-Strokes after Receive(s)

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-10-10T07:25:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf95uskqlfmiqb7dmqueji06358f4f49b8@4ax.com>`
- **References:** `<8rd9d6$7b7$1@nnrp1.deja.com>`

```
On Tue, 03 Oct 2000 18:43:52 GMT, Bill Gaphardt <bill_gaphardt@my-deja.com> wrote:

>  The problem occurs when I type the trans-id with no data and the
>screen comes up.  From that point on, if I hit enter I have to hit it
…[6 more quoted lines elided]…
>stroke ?


This looks to me like a bug in your program.  Run CEDF to see the sequence of events.   I
would guess that you would see something like this:


EXEC CICS RECEIVE MAP

EXEC CICS SEND MAP

EXEC CICS RECEIVE MAP

EXEC CICS RECEIVE MAP

EXEC CICS SEND MAP

EXEC CICS RECEIVE MAP

EXEC CICS RECEIVE MAP

EXEC CICS SEND MAP

etc.

Either in one task, or in a sequence of tasks.  Regardless, this would be a bug.  Two
receives in a row don't make sense, and two receives in one task violate the concept of
pseudo-conversational design


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Who is General Failure, and why is he reading my drive?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
