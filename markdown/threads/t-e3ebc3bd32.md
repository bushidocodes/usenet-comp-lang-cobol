[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help with cobol date

_39 messages · 13 participants · 2003-11 → 2003-12_

**Topics:** [`Date and calendar processing`](../topics.md#dates) · [`Help requests and how-to`](../topics.md#help)

---

### help with cobol date

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2003-11-22T05:43:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
Hi,

I am trying to accept a date and validate it against today's date.

I am getting the user to enter a date - 8 digits ddmmyyyy(required).
My problem is that, I dont want the user to be able to enter a date
greater than todays date.

I tried something like:
	01 date-in PIC 9(8).		
	01 sys-date PIC 9(6).
 	
*user date
	ACCEPT date-in 
*system date
	ACCEPT sys-date FROM DATE
	
Then check that the date-in is not greater sys-date, but the system
date is comming out as YYMMDD, and therefore
the users date is always greater than the system date.
Is there a simplier way to check that the users date is less than
today's date?

Thanks in advance,
Ritchie
```

#### ↳ Re: help with cobol date

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-11-22T14:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vaturvgdo80ce9r2t99ob8oanmfom3srq5@4ax.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
On 22 Nov 2003 05:43:12 -0800, ritchie_s01@yahoo.com (ritchie) wrote:

>Hi,
>
…[13 more quoted lines elided]…
>	ACCEPT sys-date FROM DATE
As you did not mention which COBOL you are using I am going to give
you an example of how Liant's RM/COBOL has implemented a "accept from
date" on their latest versions.

With them you can do
 ACCEPT sys-date FROM DATE YYYYMMDD
and this will return a date on your required format.

IF your existing compiler does not accept extented formats for the
Accept then you will need to do the way everyone else does.
E.g accept the system date as normal, and then compare the year part
to say 80.
If greater than 80 then the we are dealing with 19xx, else it is 20xx.


>	
>Then check that the date-in is not greater sys-date, but the system
…[6 more quoted lines elided]…
>Ritchie




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: help with cobol date

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2003-11-22T09:48:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0311220948.4c2473fa@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <vaturvgdo80ce9r2t99ob8oanmfom3srq5@4ax.com>`

```
Hi,

Sorry about that.

I forgot to mention that I am using th Fujitsu v3 compiler.
Do you know if any date extensions accept for this compiler??
I have checked the manual but can't find anything on it.

Thanks,
Ritchie





Frederico Fonseca <real-email-in-msg-spam@email.com> wrote in message news:<vaturvgdo80ce9r2t99ob8oanmfom3srq5@4ax.com>...
> On 22 Nov 2003 05:43:12 -0800, ritchie_s01@yahoo.com (ritchie) wrote:
> 
…[45 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: help with cobol date

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-22T13:13:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aOdnRSY4vrxKCKiU-KYjA@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
ritchie wrote:
> Hi,
>
…[19 more quoted lines elided]…
> today's date?

Sure.

First get today's date:
MOVE FUNCTION CURRENT-DATE TO TODAY-YYYYMMDD.
COMPUTE TODAY-DAYS = FUNCTION INTEGER-OF-DATE(TODAY-YYYYMMDD)

Next jiggle the user's input to get it in YYYYMMDD format, then
COMPUTE USER-DAYS = FUNCTION INTEGER-OF-DATE(USER-YYYYMMDD)

Then

IF USER-DAYS > TODAY-DAYS
   DISPLAY 'Bad date, dummy! Please re-enter'.

INTEGER-OF-DATE computes the number of days that have passed since Jan 1,
1600. It's a big number.
```

##### ↳ ↳ Re: help with cobol date

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2003-11-22T14:08:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0311221408.7ee3d93c@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com>`

```
Hi there,

Thanks for the reply.
> Sure.
> 
> First get today's date:

But this is where my main problem lies, getting today's date.

> MOVE FUNCTION CURRENT-DATE TO TODAY-YYYYMMDD.
> IF USER-DAYS > TODAY-DAYS
>   DISPLAY 'Bad date, dummy! Please re-enter'.

I call the system date.(Fujitsu v3)
It return's as YYDDMM but I need today's date as DDMMYYYY.
Does anyone know how to get 'todays' date in the format I
need(DDMMYYYY)??

I could move it all around to validate that the users date is less or
equal to the current date,I suppose???( but this still will not solve
the YYddmm instead of ddmmYYYY problem ) but it would be great if
anyone knew of a better way of accomplishing this task.

Thanks again,
Ritchie
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-11-22T22:41:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bpvrv8s39g9so89k573dh392mv71rd34k@4ax.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
On 22 Nov 2003 14:08:46 -0800, ritchie_s01@yahoo.com (ritchie) wrote:

>Hi there,
>
…[22 more quoted lines elided]…
>Ritchie
Ritchie,

all date validation is done AFTER converting any date to format
ccyymmdd, never before.

I have told you a way to do determine if a date is 19xx or 20xx.
Jerry has told you another way that should work with FJv3. e.g. the
output of  "function current-date" should be ccyymmdd if field
TODAY-YYYYMMDD is 8 bytes long.

Now if you need us to do the program for you then I am sure some
financial arrangement can be made with some of the users of this
group.






Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 4)_

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2003-11-23T10:35:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0311231035.70458932@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <5bpvrv8s39g9so89k573dh392mv71rd34k@4ax.com>`

```
Hi all,

Thanks for the help. 

> Now if you need us to do the program for you then I am sure some
> financial arrangement can be made with some of the users of this
> group.

What good would come of me getting a program written for me?  Nothing.
I'd learn nothing.
Thanks for the offer but I am only here to learn.

Thanks all,
Ritchie





Frederico Fonseca <real-email-in-msg-spam@email.com> wrote in message news:<5bpvrv8s39g9so89k573dh392mv71rd34k@4ax.com>...
> On 22 Nov 2003 14:08:46 -0800, ritchie_s01@yahoo.com (ritchie) wrote:
> 
…[45 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** "Ron" <NoSpam@NoMoSpam.ORG>
- **Date:** 2003-11-22T17:12:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eYGdndApKoPrcCKiXTWQkQ@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
Good Grief! What's the big deal about getting the
system date in ddmmyyyy format? You can't use
it like that anyway.

You have to compare dates in YYYYMMDD format.

You're making the user enter a date in ddmmyyyy format
and that date cannot be greater than the current date.

Suppose the user enters date: 01122003 (Dec 1) but today's
date is 21112003 (Nov 21).

Get this:  01122003 is LESS THAN 21112003 even though as
as a date it is later.

Now get this: 20031201 is GREATER THAN 20031121 both
numerically and as a date and therefore fails your edit.

Jeez!
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-22T17:29:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fqWdnRTabaDabCKiU-KYgw@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
ritchie wrote:
> Hi there,
>
…[12 more quoted lines elided]…
> It return's as YYDDMM but I need today's date as DDMMYYYY.

The above does not.

I can think of at least FIVE different ways to get today's date from the
computer.
If the one you are using is ACCEPT TODAYS-DATE FROM DATE you are way off
base.

DO NOT USE THIS CONSTRUCT (Accept ... from Date). IT IS ARCHAIC, WRONG, AND
LEADS TO PROBLEMS.

> Does anyone know how to get 'todays' date in the format I
> need(DDMMYYYY)??

Everybody does. You get the date in some format (usually YYYYMMDD) and move
the pieces around until everything is arranged the way you want it.

>
> I could move it all around to validate that the users date is less or
…[5 more quoted lines elided]…
> Ritchie
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-22T20:29:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311222029.513f6ae3@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> DO NOT USE THIS CONSTRUCT (Accept ... from Date). IT IS ARCHAIC, 

No. It is still current.

> WRONG, 

No.  It is perfectly correct Cobol and always gets a correct date in
thge defined format.

> AND LEADS TO PROBLEMS.

No it doesn't, not to anyone with two clues to rub together.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-23T09:26:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qaudnXam8oMKTF2iU-KYlg@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com>`

```
Richard wrote:
> "JerryMouse" <nospam@bisusa.com> wrote
>
>> DO NOT USE THIS CONSTRUCT (Accept ... from Date). IT IS ARCHAIC,
>
> No. It is still current.

It's "current" in the sense that it exists. Just like ALTER and GO TO ...
DEPENDING ON. Using this format is bad practice, rife with the possibility
of error, and just plain silly when better alternatives abound.

>
>> WRONG,
>
> No.  It is perfectly correct Cobol and always gets a correct date in
> thge defined format.

Only if you define ambiguity as correct.

>
>> AND LEADS TO PROBLEMS.
>
> No it doesn't, not to anyone with two clues to rub together.

Okay.... You use it and tell me what century it reports.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 6)_

- **From:** "Ron" <NoSpam@NoMoSpam.ORG>
- **Date:** 2003-11-23T10:44:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2-Sdnarreqxkfl2iXTWQlg@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com> <qaudnXam8oMKTF2iU-KYlg@giganews.com>`

```
> Okay.... You use it and tell me what century it reports.
>

If you code it right it will report the century.
You have to say "ACCEPT data-name FROM DATE YYYYMMDD" and
it will report 20031123, todays date.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-23T15:55:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xKudnZUPiYpIsVyiU-KYgw@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com> <qaudnXam8oMKTF2iU-KYlg@giganews.com> <2-Sdnarreqxkfl2iXTWQlg@giganews.com>`

```
Ron wrote:
>> Okay.... You use it and tell me what century it reports.
>>
…[3 more quoted lines elided]…
> it will report 20031123, todays date.

I know. The original poster was evidently not using the extension and
getting back six bytes. I was just trying to steer him away from the
construct he was using.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-23T10:01:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311231001.75c6a018@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com> <qaudnXam8oMKTF2iU-KYlg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> > No it doesn't, not to anyone with two clues to rub together.
> 
> Okay.... You use it and tell me what century it reports.

It always reports the current century.  Did you not know that ?

I think that you are confusing two separate issues.  That of storing
dates and not storing away the century that it belongs to, which does
cause problem, and that of getting the current date, which is always
current century.

You may want to argue that some mechanisms may be preferable to
others, but none of them are wrong.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-23T15:54:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ld-dnfvg0_cEsVyiU-KYkA@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com> <qaudnXam8oMKTF2iU-KYlg@giganews.com> <217e491a.0311231001.75c6a018@posting.google.com>`

```
Richard wrote:
> "JerryMouse" <nospam@bisusa.com> wrote
>
…[4 more quoted lines elided]…
> It always reports the current century.  Did you not know that ?

Why is this so confusing for you?

ACCEPT xxx FROM DATE

does not report ANY century; this one, the last one, or any other century.
It returns SIX bytes in the form YYMMDD.

No century.

At all.

>
> I think that you are confusing two separate issues.  That of storing
> dates and not storing away the century that it belongs to, which does
> cause problem, and that of getting the current date, which is always
> current century.

OK, slick. What IS the current century as far as the program is concerned
and where does that appear in the value returned from the ACCEPT... FROM
DATE command. You have to fill it in by hand.



>
> You may want to argue that some mechanisms may be preferable to
> others, but none of them are wrong.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-23T18:24:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311231824.3521fb5d@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <fqWdnRTabaDabCKiU-KYgw@giganews.com> <217e491a.0311222029.513f6ae3@posting.google.com> <qaudnXam8oMKTF2iU-KYlg@giganews.com> <217e491a.0311231001.75c6a018@posting.google.com> <ld-dnfvg0_cEsVyiU-KYkA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> >> Okay.... You use it and tell me what century it reports.
> >
…[7 more quoted lines elided]…
> It returns SIX bytes in the form YYMMDD.

In what way is this (the __current__ date) not in the __current__ century ?
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-22T20:04:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vs05e3b65n6u79@corp.supernews.com>`
- **In-Reply-To:** `<3bee6ba6.0311221408.7ee3d93c@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
ritchie wrote:

> I call the system date.(Fujitsu v3)
> It return's as YYDDMM but I need today's date as DDMMYYYY.
…[6 more quoted lines elided]…
> anyone knew of a better way of accomplishing this task.

You've already been given a couple of solutions.  Accept .. from date 
YYYYMMDD is in the COBOL 85 standard, so it should be supported by 
Fujitsu.  You can also check out Move Corresponding (although there are 
other issues with that) - using this method you could do something like...

01  User-Entered-Date        Pic 9(08).
01  User-Entered-Date-X  Redefines User-Entered-Date  Pic X(08).

01  The-System-Date          Pic 9(08).
01  The-System-Date-X  Redefines The-System-Date.
     12  Four-Digit-Year      Pic 9(04).
     12  Two-Digit-Month      Pic 9(02).
     12  Two-Digit-Day        Pic 9(02).

01  User-Compare-Date        Pic 9(08).
01  User-Compare-Date-X  Redefines User-Compare-Date.
     12  Two-Digit-Day        Pic 9(02).
     12  Two-Digit-Month      Pic 9(02).
     12  Four-Digit-Year      Pic 9(04).

...

Move All "9" to User-Entered-Date-X

Accept The-System-Date from Date YYYYMMDD

Move Corr The-System-Date-X to User-Compare-Date-X

Perform Until User-Entered-Date < User-Compare-Date

     Accept User-Entered-Date

     If User-Entered-Date > User-Compare-Date
         Display "Date too big"
     End-If

End-Perform

Just a couple of things...  I'm not sure if Accept from Date must have a 
numeric definition or not in FJ3 - if not, you can dump the redefines 
and just make The-System-Date a group-level item.  I like to compare 9's 
to 9's and X's to X's, as I've found it's the safest.  If you're 
comparing 123 to "123", are they equal?  If the compiler takes the 
numeric value of the string, or makes a string out of the numeric value, 
you're safe - but if it compares 123 with the character makeup of the 
characters "123", it may not.  With Function NumVal, I could do some of 
the conversion myself.

There are many ways to skin a cat.  Of course, the size of the number is 
but one facet of validating a date...
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-22T20:57:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M4CdnevXVcqBv12iU-KYiw@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com>`

```
LX-i wrote:
> ritchie wrote:
>
…[12 more quoted lines elided]…
> Fujitsu.

DANGER, Will Robinson!

"Accept ... from DATE" does not return YYYYMMDD! The command returns a
TWO-digit year, not four.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-23T10:47:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vs1p5prvu9jo0f@corp.supernews.com>`
- **In-Reply-To:** `<M4CdnevXVcqBv12iU-KYiw@giganews.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <M4CdnevXVcqBv12iU-KYiw@giganews.com>`

```
JerryMouse wrote:

> LX-i wrote:
> 
…[21 more quoted lines elided]…
> TWO-digit year, not four.

You are correct.  But, Accept ... from Date YYYYMMDD returns a 4-digit 
year, which is what he needs.  (Word wrapping bit you, senor mouse? ;> )
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-23T22:40:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311232240.78921bcb@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote

> You've already been given a couple of solutions.  Accept .. from date 
> YYYYMMDD is in the COBOL 85 standard, so it should be supported by 
> Fujitsu. 

Can you provide a reference that supports this view that 'it is in the
ANS'85 standard'.  All the references that I have indicate that it is
not.

It is not supported by Fujitsu 3, nor by any MF compiler that I have.

> You can also check out Move Corresponding (although there are 
> other issues with that) - using this method you could do something like...
…[32 more quoted lines elided]…
> End-Perform

Why do you think that this is at all useful ?  In effect you are only
checking the day number and the month and year become irrelevant if
the day number is unequal.

      IF 24102003 > 22112003   -> yes it is.
 
> Just a couple of things...  I'm not sure if Accept from Date must have a 
> numeric definition or not in FJ3 - if not, you can dump the redefines 
> and just make The-System-Date a group-level item.

ACCEPT FROM DATE acts as if it is a 6 byte numeric so it may be
accepted into a PIC 9(6) or to a X(6) or group field following the
usual rules of numeric to group move.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-24T18:23:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FC24C5C.3F41F74F@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com>`

```


Richard wrote:

> LX-i <lxi0007@netscape.net> wrote
>
…[8 more quoted lines elided]…
> It is not supported by Fujitsu 3, nor by any MF compiler that I have.

Richard,

I didn't want to get into this one, but the following from Net Express V 3.1
which *must* be ANSI 85 - if I checked the V 4.0 on-line manual then no doubt
that will probably be updated to ANSI 2002 :-
---------------------------------------------
Format 2 (FROM DATE)

                                          { DATE [YYYYMMDD}
ACCEPT identifier FROM { DAY [YYYYDDD] }
                                           { DAY-OF-WEEK }
                                           { TIME }
[END-ACCEPT]
-------------------------------------------------------------------

The only part which is non-ANSI 85 is the END-ACCEPT which is highlighted in
blue.

Syntax :   Identifier must be numeric or alphanumeric

General Rules :

1. The END-ACCEPT .........

2. The ACCEPT statement causes the information requested to be transferred to
the data item specified by identifier etc.....

3. DATE, without the phrase YYYYMMDD, is composed of the data elements year of
the current century, month of the year, and day of the month. DATE, without the
phrase YYYYMMDD, when accessed by a COBOL program, behaves as if it had been
described as an unsigned elementary integer data item of usage display six
digits in length, the character positions of which, numbered from left to right,
are:
......(description of contents)

4. DATE, with the phrase YYYYMMDD, is composed of the data elements year in the
Gregorian calendar, month of the year, and day of the month. DATE, with the
phrase YYYYMMDD, when accessed by a COBOL program, behaves as if it had been
described as an unsigned elementary integer data item of usage display eight
digits in length, the character positions of which, numbered from left to right,
are:
.....description of contents......
.
5. DAY, without the phrase YYYYDDD, is composed of the data elements year of the
current century and day of the year. DAY, without the phrase YYYYDDD, when
accessed by a COBOL program, behaves as if it had been described as an unsigned
elementary integer data item of usage display five digits in length, the
character positions of which, numbered from left to right, are:
.....description of contents....

6. DAY, with the phrase YYYYDDD, is composed of the data elements year in the
Gregorian calendar and day of the year.DAY, with the phrase YYYYDDD, when
accessed by a COBOL program, behaves as if it had been described as an unsigned
elementary integer data item of usage display seven digits in length, the
character positions of which, numbered from left to right, are:
.....description of contents

7. DAY-OF-WEEK is composed of a .........
----------------------------------------------------------------------------

Jimmy
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-24T22:38:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FC28858.FA8506B7@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <3FC24C5C.3F41F74F@shaw.ca>`

```


"James J. Gavan" wrote:

> Richard wrote:
>
…[16 more quoted lines elided]…
> that will probably be updated to ANSI 2002 :- <snip>

Guess you could be right Richard. Having just walked the doggies remembered I still
had the hard copy manuals for the DOS V 3. ?, which claims it is ANSI-85 compliant
along with M/F extensions.  Only format is :-

    ACCEPT identifier from DATE (period)

Perhaps clarification from Chuck or Bill - is the "YYYYMMDD"  bit part of the COBOL
'97 enhancements, the major part of which I recall was introduction of the Intrinsic
Functions  ?

"Technically" I believe, there's no such animal as COBOL '97 - bloody confusing !

Jimmy
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-25T05:16:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031125061701.760$UG@news.newsreader.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <3FC24C5C.3F41F74F@shaw.ca> <3FC28858.FA8506B7@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:
>
> "James J. Gavan" wrote:
…[31 more quoted lines elided]…
> "Technically" I believe, there's no such animal as COBOL '97 - bloody confusing!

I'm not aware of any "'97 enhancement", but I have ANSI X3.23-1985, the official
ANSI 1985 COBOL standard document, ANSI X3.23a-1989, the 1989 COBOL
amendment that added intrinsics, and ANSI X3.23b-1993, the 1993 COBOL
Correction Amendment. If there is a mention of "ACCEPT identifier from DATE
(YYYMMDD)" in any of those, I have not been able to find it.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-03T19:29:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jQqzb.26586$sb4.6304@newsread2.news.pas.earthlink.net>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <3FC24C5C.3F41F74F@shaw.ca> <3FC28858.FA8506B7@shaw.ca>`

```
<G> Bill was away for 10 days.  I don't know if anyone answered this here (I
think I saw an answer elsewhere)

The optional "YYYYMMDD" and "YYYYDDD" (keywords) were not a part of the '85
Standard or the '89 or '91 amendments to it.  They are a part of the 2002
Standard.

Furthermore, they were "frozen" early in the development of the 2002 Standard
(when it was still - gasp - expected to be official by '97 or '98).  J4 and WG4
"indicated" to vendors that they INTENDED them to remain "stable" from their
early development to the approval of the "next" revision (i.e. the 2002
Standard) so MANY (but certainly NOT ALL) vendors provided support for them WELL
before 2000.

FYI - any "conforming" '85 (or '89) compiler that supports them MUST flag them
as extensions when ANSI/ISO/NIST flagging is turned on.  Did anyone who
"wondered" about their being standard actually TRY to compile with flagging
turned on?  Does any vendor "support" this syntax in an '85 compiler withOUT
flagging them???
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-12-03T23:05:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FCE671B.8838C2AB@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <3FC24C5C.3F41F74F@shaw.ca> <3FC28858.FA8506B7@shaw.ca> <jQqzb.26586$sb4.6304@newsread2.news.pas.earthlink.net>`

```


"William M. Klein" wrote:

> <G> Bill was away for 10 days.  I don't know if anyone answered this here (I
> think I saw an answer elsewhere)
>

Phew ! Glad you are back - I nearly wrote privately to ask if you were OK. What
you've written below - see my separate thread "Accept Date" - Don gave what you
would normally provide, being the great helper you are.

Judson - I see where I got the funny 'COBOL '97' - that's what Bill refers to below.



> The optional "YYYYMMDD" and "YYYYDDD" (keywords) were not a part of the '85
> Standard or the '89 or '91 amendments to it.  They are a part of the 2002
…[14 more quoted lines elided]…
>

Wasn't aware of Accept YYYYMMDD until Richard mentioned it as 'not existing'. I use
the intrinsic function to get the 21 character Date/Time block - then extract from
that what I want.

Jimmy
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-24T15:48:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311241548.4a1f47a1@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <3FC24C5C.3F41F74F@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote 

> > Can you provide a reference that supports this view that 'it is in the
> > ANS'85 standard'.  All the references that I have indicate that it is
…[6 more quoted lines elided]…
> that will probably be updated to ANSI 2002 :-

While NE is an ANS'85 compiler it also contains many extensions that
are not in ANS'85.  These are often, but not always, marked in the
manuals (of the MF versions that I have) with an (MF) or (OSVS) or
similar symbol to indicate where the extension came from.

> The only part which is non-ANSI 85 is the END-ACCEPT which is highlighted in
> blue.

There is no reference to the YYYYMMDD that I can find in any
documentation that I have on ANS'85.  Perhaps Bill can enlighten.

Specifically MF OCDS does not document it, nor does Fujitsu 3 to 7. 
Fujitsu 7 gives a compilation error for this.
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-24T18:32:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vs58p649ei9605@corp.supernews.com>`
- **In-Reply-To:** `<217e491a.0311232240.78921bcb@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com>`

```
Richard wrote:
> LX-i <lxi0007@netscape.net> wrote
> 
…[10 more quoted lines elided]…
> It is not supported by Fujitsu 3, nor by any MF compiler that I have.

Well, I've looked - my copies of the standards were on the computer that 
was stolen.  :(  I'll have to defer to you on that.  (Someone told me 
that the "YYYYMMDD" was COBOL 85's answer to a major building block to 
Y2K compliance, even when the normal system date didn't return a 
century.  In court, that would be referred to as "hearsay"...)  Function 
Current-Date should still work.

> Why do you think that this is at all useful ?  In effect you are only
> checking the day number and the month and year become irrelevant if
> the day number is unequal.
> 
>       IF 24102003 > 22112003   -> yes it is.

I realized that after I pressed "Send".  I guess I just tried to code 
something in a hurry, without taking a step back to see if the 
requirements made sense to begin with.  :)
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-25T00:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FC2A695.B109AF06@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <vs58p649ei9605@corp.supernews.com>`

```


LX-i wrote:

> > Can you provide a reference that supports this view that 'it is in the
> > ANS'85 standard'.  All the references that I have indicate that it is
…[5 more quoted lines elided]…
> was stolen.  :(  I'll have to defer to you on that.

On the stolen bit. Did you get the same answer from your polizei that I did.
Some kids had removed the protective 'bra' we had over the front of the car
- against stones etc. Two "youths" arrived in police uniform. Having
listened to myself and my wife bitching for a minute or so, one says with a
straight face, "You haven't a hope in hell of getting it back. And that's
being optimistic !".

On the YYYYMMDD let's see what Chuck or Bill respond with.

Jimmy
```

###### ↳ ↳ ↳ Re: help with cobol date

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-25T05:13:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vs6earjoguku0b@corp.supernews.com>`
- **In-Reply-To:** `<3FC2A695.B109AF06@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com> <vs05e3b65n6u79@corp.supernews.com> <217e491a.0311232240.78921bcb@posting.google.com> <vs58p649ei9605@corp.supernews.com> <3FC2A695.B109AF06@shaw.ca>`

```
James J. Gavan wrote:
> 
> On the stolen bit. Did you get the same answer from your polizei that I did.
…[4 more quoted lines elided]…
> being optimistic !".

Well, they were actually not quite that pessimistic.  A lot of things 
like that -do- turn back up for them (at least that what they said - and 
I don't know why they'd lie about something like that).  Since it's a 
touristy type of place, things get swiped and then dumped at a pawn shop 
  with some frequency.  Mine still hasn't turned up yet, though...
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-23T06:58:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311230658.52ca9e2b@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
ritchie_s01@yahoo.com (ritchie) wrote in message news:<3bee6ba6.0311221408.7ee3d93c@posting.google.com>...
> Hi there,
> 
…[22 more quoted lines elided]…
> Ritchie


01  Now-Date-YYYYMMDD.
    03  D-YYYY PIC 9(4).
    03  D-MM   PIC 99.
    03  D-DD   PIC 99.

01  Now-Date-MMDDYYYY.
    03  D-MM   PIC 99.
    03  D-DD   PIC 99.
    03  D-YYYY PIC 9(4).

Move Function Current-Date to Now-Date-YYYYMMDD
Move Corresponding Now-Date-YYYYMMDDD to Now-Date-MMDDYYY

Now-date-mmddyyyy now contains the date in the format you desire.
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-23T14:51:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311231451.6fe070c9@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```
ritchie_s01@yahoo.com (ritchie) wrote 

> > MOVE FUNCTION CURRENT-DATE TO TODAY-YYYYMMDD.
> > IF USER-DAYS > TODAY-DAYS
…[3 more quoted lines elided]…
> It return's as YYDDMM but I need today's date as DDMMYYYY.

ACCEPT FROM DATE in FJ3 only returns YYMMDD.  You need to use the
function as above to get YYYYMMDD.

> Does anyone know how to get 'todays' date in the format I
> need(DDMMYYYY)??

Look in thye manual under 'MOVE'.
 
But you _do_not_ want DDMMYYYY as comparing this format to another
date in this format does not work:

     IF ( "01122003" > "24112003" )

You need to have them as YYYYMMDD to comapre whether the user date is
greater than today, or compare the 3 parts separately, in which case
order is irrelevant.

> I could move it all around to validate that the users date is less or
> equal to the current date,I suppose???( but this still will not solve
> the YYddmm instead of ddmmYYYY problem ) 

You may also want to valideate that what they entered is actually a
valid date, ie MM >= 01 <= 12, DD >= 01 <= days_in_MM.
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-24T16:02:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpta29$77q$1@peabody.colorado.edu>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com> <3bee6ba6.0311221408.7ee3d93c@posting.google.com>`

```

On 22-Nov-2003, ritchie_s01@yahoo.com (ritchie) wrote:

> I call the system date.(Fujitsu v3)
> It return's as YYDDMM but I need today's date as DDMMYYYY.
…[6 more quoted lines elided]…
> anyone knew of a better way of accomplishing this task.

Sure you can.    And you can assume current date is in the 21st century as well.
  Chances are that before 2100 you will have a compiler that meets current
standards and can offer you current date functions.
```

##### ↳ ↳ Re: help with cobol date

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-23T00:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FBFF9ED.C4FE1A66@shaw.ca>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <7aOdnRSY4vrxKCKiU-KYjA@giganews.com>`

```


JerryMouse wrote:

> ritchie wrote:
> > Hi,
…[37 more quoted lines elided]…
> 1600. It's a big number.

My only quibble on Jerry's text above is DON'T "jiggle" the user's input.

Get used to the idea of ISO date formats. (You can use Google to search for
"ISO Date Format"). As you used "ddmmyy" in your earlier message, (indicates
to me you are a Brit), do the following represent 1st October or 10th January
:-

a) ISO         - 20031001
b) UK          - 01102003 (not sure - does this also apply to the Continent
?)
c) US           - 10012003
d) Canada    - God help us - uses both  (b) and (c)  !

Fair bet, if not already, EU regulations will opt for the (a) ISO format
above., (ccyymmdd) Same with time - probably universally the major
transportation systems , air, train, bus, follow what was referred to as the
'military clock', 6:15 pm = 18:15. (Haven't checked, but I think that
'military format' is now also the ISO format for Time).

I know there's a problem using your Fujitsu Screen Section as Richard pointed
out, but it doesn't take a major change, even for users, to switch to ISO -
so you can
have a display :-

"Enter date (yyyyMMdd)  : [.............] "

and when you get into Windows GUIs there are facilities to 'prompt mask' the
input field :-

"Enter Date [yyyyMMdd]  " - in this case the 'yyyyMMdd' is greyed in the
entry-field, and overridden as the user starts keying in...

The most significant thing is if you store the dates in records and you want
to sort in ascending order by date. Which of (a),  (b) or (c)  above gives it
to you automatically ? Granted if you are printing a heading for a report all
three formats are understood if you substitute "Jan" or "Oct" for the month
in all three formats.

For about the past 20 years I have written cheques manually, dating them e.g.
:-  2003 Nov 23, which is what I also use for print headings - following the
ISO format. (Note - nobody, including bank staff,  has ever queried my 'funny
date' format on any of my cheques).

Just one other thing - Date Validation :- your date can appear to be
"kosher", i.e., less than system date - BUT - user could key in "33" days or
"15" months.  (You watch all our 'Date Experts" will jump in here <G>)  One
way to do this, off the top of my head, because I'm not interested in "days"
in my application , :-

01 DaysPerMonthA.
     pic x(36) value "31,28,31,30,31,30,31,31,30,31,30,31".
01 DaysPerMonthB redefines DaysPerMonthA.
     05  occurs 12.
     *> if Fujitsu doesn't like above line then change it to :-
     *> 05 DaysPerMonthC occurs 12.
         10 NumberOfDays            pic 9(02).
         10                                     pic x.

*> The commas between the values above are to make the table more readable -
to *> YOU - not the computer !

01 In-Date.
     05 In-Year           pic 9(04).
     05 In-Month        pic 9(02).
     05 In-Month        pic 9(02).

1) Step 1 - check for Leap Years - see below

2) Step 2 - accept in-Date

3) Steps 3 - onwards...........
if in-Year < 1950 (whatever 'lowest' year you want to accept) *****
error.........
if in-Year > "x" - this check you are doing against your Current-Date, later
if in-Month ( = zeroes) OR ( > 12 ) **** error......
if In-Days = zeroes ****** error
if In-Days > NumberOfDays(in-Month) ****** error

You may not yet be familiar with the subscripting above, using tables -
assume you are checking for September, for which max days is "30" :-

if In-Days {= 31} > NumberOfDays{in-Month = 9)
 --- NumberOfDays contains "30"
      using Month value 9 to get the actual number of days

Just one more twist - Februrary is it 28 or 29 ?. If you are just checking
ONE input date then you do an if LeapYear check. However, in the real world,
if you were doing this check over and over again for different dates, then do
the Leap Year check which I've shown above as Step 1. Others will have
different ways, but having established that Februrary needs to be "29" days -
I would change the contents of the Table above :-

INSPECT DaysPerMonth REPLACING ALL "28" BY "29"
(Use the F/J on-line manual to check the syntax for   INSPECT and REPLACING.)

- now for each successive date you enter the DaysPerMonthTable can be
accessed with just that initial setting to "29", prior to the very first date
that you check.. That's one way to do it, but there is a "gotcha" - IF ALL
your Dates coming in as input have a common year (say 1998), then it's fine.
If you have a mixture of years then you need to do each Leap Year check
independently against each one.

On reflection, try this for simplicity :-

    if In-Month <>  2
       perform OTHER-MONTHS-PARA *> uses Table to check for days

    else perform LEAP-YEAR-PARA
          *> establish if this is a Leap Year, then check for 28 or 29 as
appropriate
   End-if

**** Doing this free-hand I originally typed "if In-Month = 2 etc...." - take
a guess at why I switched them around (????) ********

Oodles of stuff on Leap Years on the Web, and others may give you routines. I
did a Google search, and fortuitously hit as my first site, the Royal
Observatory in Greenwich - can't do much better than that ! From their site
:-
-----------------------------------------------------------------------------

LEAP YEARS

The calendar year is 365 days long, unless the year is exactly divisible by
4, in
which case an extra day is added to February to make the year 366 days long.
If
the year is the last year of a century, e.g.. 1800, 1900, 2000, then it is
only a leap
year if it is exactly divisible by 400. Therefore, 1900 wasn't a leap year
but 2000
was. The reason for these rules is to bring the average length of the
calendar
year into line with the length of the Earth's orbit around the Sun, so that
the
seasons always occur during the same months each year.
-------------------------------------------------------------------------------------

Jimmy, Calgary AB
```

#### ↳ Re: help with cobol date

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-22T20:36:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311222036.73ecfd18@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
Hi ritchie,

You can try this until you get a Y2K compliant compiler:

 01 date-in.
    05 cc        PIC X(2).
    05 date-in-6 PIC X(6).  

 01 sys-date     PIC 9(6).

*user date
 	ACCEPT date-in 
*system date
 	ACCEPT sys-date FROM DATE

        IF date-in-6 > sys-date 
           DISPLAY 'no-no msg'
           .
           .
           .

On a more serious note, before you do anything you should perform a
validity chk on the input date; i.e. 0 < mm < 13; 0 < dd < 32. And
while you're at it you could add a windowing routine to add the cc to
the sysdate.Then you won't need my suggestion. :)

If you're ambitious you can even build a tbl to get the max days in
each month (adjusted for leap year) and use it in the dd validation.

Regards, Jack.

ritchie_s01@yahoo.com (ritchie) wrote in message news:<3bee6ba6.0311220543.740ad43d@posting.google.com>...
> Hi,
> 
…[22 more quoted lines elided]…
> Ritchie
```

#### ↳ Re: help with cobol date

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-23T15:30:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311231530.7515188a@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
Hi ritchie,

Sorry I missed the ymd/dmy mismatch. You can use move corresponding to
work around your problem. See below:

01 date-in. 
     05 cc              PIC X(2). 
     05 date-in-6    PIC X(6).

01 sys-date-ymd.
     05  yy             PIC 9(2).
     05  mm           PIC 9(2).
     05  dd             PIC 9(2).

01 sys-date-dmy.
     05  dd             PIC X(2).
     05  mm           PIC X(2).
     05  yy             PIC X(2).

 

*user date
 ACCEPT date-in 
*system date
 ACCEPT sys-date-ymd FROM DATE 

 MOVE CORR sys-date-ymd TO sys-date-dmy
 IF date-in-6 > sys-date-dmy 
      DISPLAY 'no-no msg' 
 .
 .
 . 






ritchie_s01@yahoo.com (ritchie) wrote in message news:<3bee6ba6.0311220543.740ad43d@posting.google.com>...
> Hi,
> 
…[22 more quoted lines elided]…
> Ritchie
```

##### ↳ ↳ Re: help with cobol date

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-23T18:21:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311231821.1be52c4f@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <8a2d426e.0311231530.7515188a@posting.google.com>`

```
jacksleight@hotmail.com (Jack Sleight) wrote

> Sorry I missed the ymd/dmy mismatch. You can use move corresponding to
> work around your problem. See below:
…[24 more quoted lines elided]…
>       DISPLAY 'no-no msg' 

Is this in any way useful ??

Comparing dates in the form ddmmyy will not show if one is later than another.
```

###### ↳ ↳ ↳ Re: help with cobol date

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-24T16:59:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311241659.55d088c4@posting.google.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com> <8a2d426e.0311231530.7515188a@posting.google.com> <217e491a.0311231821.1be52c4f@posting.google.com>`

```
Of course you're right, Richard. Just went right by me. As the saying
goes, "I knew that."

In any event, the alt solution is only a move corr away - from the
user input date to a ymd work field.
 
Regards, Jack.



riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0311231821.1be52c4f@posting.google.com>...
> jacksleight@hotmail.com (Jack Sleight) wrote
> 
…[30 more quoted lines elided]…
> Comparing dates in the form ddmmyy will not show if one is later than another.
```

#### ↳ Re: help with cobol date

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-24T16:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpt9u6$6ja$1@peabody.colorado.edu>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
Methods of obtaining YYYYMMDD are dependent on your compiler.

Do you have FUNCTION CURRENT-DATE available?

Check your documentation for your ACCEPT command to see if you have a YYYY
version.

If your compiler is too old, then you will have to assume that today's date is
in the 20th century.   That probably is a safe assumption.
```

#### ↳ Re: help with cobol date

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-11-28T00:06:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bq63hu$t6l$1@news.utelfla.com>`
- **References:** `<3bee6ba6.0311220543.740ad43d@posting.google.com>`

```
ritchie <ritchie_s01@yahoo.com> wrote:


: Then check that the date-in is not greater sys-date, but the system
: date is comming out as YYMMDD, and therefore
: the users date is always greater than the system date.
: Is there a simplier way to check that the users date is less than
: today's date?

How about using CCYYMMDD format for both dates and making sure the
entered date is not greater than the current date?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
