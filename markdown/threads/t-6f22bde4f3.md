[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol FAQ Quesiton

_22 messages · 16 participants · 2000-09_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Cobol FAQ Quesiton

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-14T02:39:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000913223943.29261.00000054@ng-fn1.aol.com>`

```
I have a quick questions, as i have posted before i am new to COBOL, for class
we get projects well i got through with Proj1 with no problems but i am
struggling with Proj2, i know HW questions arent usually answered because of
the fear of doing someones homework, but i am really stuck here and i work
during my professors office hours.  

IF this is permited please help me:
In the directions it says increment a 2nd counter variable to keep track of the
records u have selected( I dont understand what that is). I dont know how
someone could help me with this, but if i am wrong for asking this please tell
me and i'll stop(dont flame me).

Thanks,
Deek
```

#### ↳ Re: Cobol FAQ Quesiton

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9C1DCDCD977A5CF1.2B8AA60F6649AEDA.92AFCF3CBC87FDE4@lp.airnews.net>`
- **References:** `<20000913223943.29261.00000054@ng-fn1.aol.com>`

```
On 14 Sep 2000 02:39:43 GMT, deek40@aol.com (Deek40) enlightened us:

>I have a quick questions, as i have posted before i am new to COBOL, for class
>we get projects well i got through with Proj1 with no problems but i am
…[11 more quoted lines elided]…
>Deek

What they are asking you to do is define a variable in working storage
and every time you select a record to process, add 1 to your variable.
So, it might look like:

03  WS-CNTR         PIC S9(5)           VALUE +0.

Then somewhere in your program you might have:

READ INPUT-FILE  AT END  MOVE 'Y' TO INPUT-EOF.
IF INPUT-EOF NOT EQUAL 'Y'
   ADD 1 TO WS-CNTR.

This is a very simplistic example, but I hope it gets you thinking in
the right way.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

#### ↳ Re: Cobol FAQ Quesiton

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-09-14T03:18:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C042F2.E8472B9E@home.com>`
- **References:** `<20000913223943.29261.00000054@ng-fn1.aol.com>`

```


Deek40 wrote:
> 
> I have a quick questions, as i have posted before i am new to COBOL, for class
…[10 more quoted lines elided]…
> 
Deek,

Best bet, post text of the complete question given to you - we wont give
you your completed assignment, but we will give you clues.

Jimmy
```

#### ↳ Re: Cobol FAQ Quesiton

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-14T04:46:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000914004632.28732.00000955@ng-fu1.aol.com>`
- **References:** `<20000913223943.29261.00000054@ng-fn1.aol.com>`

```
another quick question:
here is my code:
IDENTIFICATION DIVISION.
 PROGRAM-ID.       SENIOR.
 AUTHOR.           DERRICK PIZUR
 
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
*Changed file name to c:\cobol\senior.dat 
     SELECT STUDENT-FILE ASSIGN TO 'C:\COBOL\SENIOR.DAT'.
	        ORGANIZATION IS LINE SEQUENTIAL.
     SELECT PRINT-FILE
          ASSIGN TO PRINTER.
 DATA DIVISION.
 FILE SECTION.    
 FD  STUDENT-FILE
     RECORD CONTAINS 43 CHARACTERS
     DATA RECORD IS STUDENT-IN.
The Line  Organization line is sequential  keeps giving me syntax error
message:
invalid word'organization' is found ignore till next valid paragraph, section
or division. 
please help i am kinda stuck.
```

##### ↳ ↳ Re: Cobol FAQ Quesiton

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-09-14T05:06:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C05C54.9D482CAB@worldnet.att.net>`
- **References:** `<20000913223943.29261.00000054@ng-fn1.aol.com> <20000914004632.28732.00000955@ng-fu1.aol.com>`

```
Deek40 wrote:
> 
> another quick question:
…[9 more quoted lines elided]…
>      SELECT STUDENT-FILE ASSIGN TO 'C:\COBOL\SENIOR.DAT'.

Ooops!  You just terminated your SELECT statement with a period...

>                 ORGANIZATION IS LINE SEQUENTIAL.

So what is ORGANIZATION clause connected to?  Nothing!

>      SELECT PRINT-FILE
>           ASSIGN TO PRINTER.
…[9 more quoted lines elided]…
> please help i am kinda stuck.

I hope that helps.
```

##### ↳ ↳ Re: Cobol FAQ Quesiton

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-09-14T07:14:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com>`
- **References:** `<20000913223943.29261.00000054@ng-fn1.aol.com> <20000914004632.28732.00000955@ng-fu1.aol.com>`

```
On 14 Sep 2000 04:46:32 GMT, deek40@aol.com (Deek40) wrote:
Hi Derek,

<snipped>
This line should NOT end with a dot!.  Remove it, and you are set to go!


>     SELECT STUDENT-FILE ASSIGN TO 'C:\COBOL\SENIOR.DAT'.
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-14T05:55:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000914015503.26266.00000423@ng-fu1.aol.com>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com>`

```
Thanks, as i stated before i am learning Cobol and still make dumb mistake oh
well live and learn.
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ATbw5.890$aY1.44140@nnrp2.sbc.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com>`

```
It gets every COBOL programmer at least once a week.

There are some who swear by the (funny-looking) construct of putting
periods on lines by themselves and only having one period per
paragraph. In my view, this syntax looks weird, but it solves (mostly)
the problem of spurious (or missing) periods.

There are, however, one or two things you can get in the habit of
doing to minimize the problem.

One is to use END-(something) at every possible place. For example,

IF condition
   do something
   END-IF

If you plan on using a period instead of END-IF - and you forget the
period - you're hosed. WITH the END-IF, period or no, you're golden.

Don't EVER use commas or semi-colons as syntax in a COBOL program.

"Deek40" <deek40@aol.com> wrote in message
news:20000914015503.26266.00000423@ng-fu1.aol.com...
> Thanks, as i stated before i am learning Cobol and still make dumb
mistake oh
> well live and learn.
>
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 5)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g0xk5q1.pminews@news.wanadoo.es>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net>`

```
On Thu, 14 Sep 2000 16:55:48 -0500, Jerry P wrote:

>It gets every COBOL programmer at least once a week.
>
…[18 more quoted lines elided]…
>

I have come to the conclusion that are two ways to reduce the possibility to
make mistakes.

1. Only use periods when the syntax or the logic of your program requires it.
2. Use periods whenever you can.

I prefer the second, because it's more likely that the compiler catches your
errors.

Anyway, using the END-IF construction is much easier to read, so if your
compiler
supports it, use it (together with END-READ END-PERFORM etc.)

Just my opinion

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 6)_

- **From:** "Christopher J Pomasl" <pomasl@uswest.net>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R0uw5.439$eS1.206945@news.uswest.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g0xk5q1.pminews@news.wanadoo.es>`

```
I made a standard to ALWAYS use the END-xx constructs when the code is more
than one line long.  I have eliminated many stray periods this way and the
compiler ALWAYS tells me when I have one.  When you are working with a IF
statement that is several lines long and may even contain some embedded IF
statements, it is easy to place a incorrect period in fray.  By coding the
END-xx where you EXPECT the end to be, the compiler will flag the statement
as not having a corresponding "xx" statement if you put in a stray period.

Hopefully your compiler supports it as it is more valuable than debugging
the results of a stray period.  Use them!!
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 7)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C31B4D.813FFBB1@optonline.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g0xk5q1.pminews@news.wanadoo.es> <R0uw5.439$eS1.206945@news.uswest.net>`

```
Christopher J Pomasl wrote:
> 
> I made a standard to ALWAYS use the END-xx constructs when the code is more
…[8 more quoted lines elided]…
> the results of a stray period.  Use them!!

I have made it a standard for my happy little band of merry programmers,
telling them to code END-IF, for example, as routinely as they code
END-EXEC. No one seems to feel that END-EXEC is a burden or diminishes
them as a person.

As always, YMMV,
LiamD
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-09-15T00:35:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G9ew5.1292$Xp5.267642@paloalto-snr1.gtei.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net>`

```

Jerry P <jerryp@bisusa.com> wrote in message
news:ATbw5.890$aY1.44140@nnrp2.sbc.net...
> It [misplaced full srop] gets every COBOL programmer at least once a week.
>
…[4 more quoted lines elided]…
>


I got an idea from this NG which I've been using:

The last phrase of every paragraph, on its own line is...

    CONTINUE.

.. and there are no other periods in the paragraph.


MCM
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 6)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ps63k$337i$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net> <G9ew5.1292$Xp5.267642@paloalto-snr1.gtei.net>`

```

What is the advantage of ending every paragraph with "CONTINUE." instead of
simply a "." on it's own line?  I can see that the disadvantage is coding an
unnecessary 8 characters per paragraph.
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C21D02.CB80C26B@brazee.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net> <G9ew5.1292$Xp5.267642@paloalto-snr1.gtei.net> <8ps63k$337i$1@newssvr05-en0.news.prodigy.com>`

```


Terry Heinze wrote:

> What is the advantage of ending every paragraph with "CONTINUE." instead of
> simply a "." on it's own line?  I can see that the disadvantage is coding an
> unnecessary 8 characters per paragraph.

CONTINUE.

is much more obvious and hard to miss than is

.


Also, my shop won't accept period by itself as part of its standards.  Besides
being easy to miss, and non-English language, it is ugly.  We really aren't
worried about the cost of writing storing those extra 8 characters.  If we had
wanted a terse, hard to read language, we wouldn't have picked CoBOL.
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 8)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C31AA2.B4B692DF@optonline.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com> <ATbw5.890$aY1.44140@nnrp2.sbc.net> <G9ew5.1292$Xp5.267642@paloalto-snr1.gtei.net> <8ps63k$337i$1@newssvr05-en0.news.prodigy.com> <39C21D02.CB80C26B@brazee.net>`

```
Howard Brazee wrote:
> 
> Terry Heinze wrote:
…[12 more quoted lines elided]…
> being easy to miss, and non-English language, it is ugly. 

Beauty, clearly, is in the eye of the beholder. I used to think it was
bizarre, now it looks normal and periods (full stops) on every line look
odd.

LiamD
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 4)_

- **From:** "Erlend Moen" <erlend.moen@disys.no>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pq3pc$btn$1@oslo-nntp.eunet.no>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com>`

```
Deek40 <deek40@aol.com> skrev i
news:20000914015503.26266.00000423@ng-fu1.aol.com
> Thanks, as i stated before i am learning Cobol and still make dumb mistake
oh
> well live and learn.

You are doing it just fine!  I admire your polite messages as well! I'm sure
you will be treated nice in here!

As for the period you had problem with, remember to use the periods
correctly in if-statements or else you may experience some weird things
happen in you code :-).

<-emo->
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pr1pf$r2a$1@slb1.atl.mindspring.net>`
- **References:** `<mjn0sssb9o7rnfous1gef8cf4tiggpljst@4ax.com> <20000914015503.26266.00000423@ng-fu1.aol.com>`

```
As I am certain that all (well almost all) of the other "experienced" COBOL
programmers will tell you, "misplaced" periods (full-stops) are something
that will "bug" <G> you for the rest of the time you code in COBOL (whether
it is one year, one decade, or more).
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 4)_

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-16T06:06:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000916020644.02532.00000404@ng-fn1.aol.com>`
- **References:** `<20000914015503.26266.00000423@ng-fu1.aol.com>`

```
Another Question:
Not to spite anyone here, but could someone explain what COBOL is used for in
every day life?  What little I have saw of COBOL it looks like a database that
takes a lot of extra time to plan.  What type of things can u do with COBOL
that is unique?  Remember I am not expierenced with COBOL or anything else, but
HTML.
Thanks from the newbie,
Deek
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c389cc.4348468@207.126.101.100>`
- **References:** `<20000914015503.26266.00000423@ng-fu1.aol.com> <20000916020644.02532.00000404@ng-fn1.aol.com>`

```
Not sure it it's "unique" or not but here is a short list of COBOL
program functions I have written that are a "little off the beaten
path".

Clipboard monitor - anything that lands in the clipboard gets appended
to a file.

Socket Interface
Serial communications fully automated file transfer of statement data
to a statement processor

Pedigree Tracking (Cats)

Fax Server

Then some more mundane:

Bowling center managment
Archery shoot Software
Invoice printing
Tax Lookup (Web Interface)
POS
Data Entry

That's a short list.  It can do virtually anything you want with a
programmng language.

On 16 Sep 2000 06:06:44 GMT, deek40@aol.com (Deek40) wrote:

>Another Question:
>Not to spite anyone here, but could someone explain what COBOL is used for in
…[5 more quoted lines elided]…
>Deek

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 5)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C31B80.F3409FB1@optonline.net>`
- **References:** `<20000914015503.26266.00000423@ng-fu1.aol.com> <20000916020644.02532.00000404@ng-fn1.aol.com>`

```
Deek40 wrote:
> 
> Another Question:
…[4 more quoted lines elided]…
> HTML.

It's a floor polish AND a delicious dessert topping.

HTH,
LiamD
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 5)_

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-09-17T02:38:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C42E8B.DAF3DC6@neo.rr.com>`
- **References:** `<20000914015503.26266.00000423@ng-fu1.aol.com> <20000916020644.02532.00000404@ng-fn1.aol.com>`

```
Deek40 wrote:
> 
> Another Question:
…[6 more quoted lines elided]…
> Deek

Well, let me see.  IRS has millions of lines of it for processing
tax returns/refunds.

USGov't has millions of lines of it for doing payroll, inventory,
weapons tracking, certain things for NASA use COBOL, USNavy
personnel helped develop the language...

"Private Sector" Payroll, cash management, check processing (aka,
Item Processing for banks), inventory, order entry, Circulation
management (news paper companies and magazines), anything you
want done with/via/for accounting, credit card processing
(merchant, bank, card-holder, embossing), a few games have been
written in COBOL.  Uh, what more would you like?
```

###### ↳ ↳ ↳ Re: Cobol FAQ Quesiton

_(reply depth: 6)_

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000917173904.06589.00000049@ng-ca1.aol.com>`
- **References:** `<39C42E8B.DAF3DC6@neo.rr.com>`

```
Thanks everyone
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
