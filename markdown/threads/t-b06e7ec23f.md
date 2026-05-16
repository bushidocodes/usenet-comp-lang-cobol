[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# y2k-proofing my programs

_19 messages · 8 participants · 1998-09_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### y2k-proofing my programs

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FC314B.6C5EE424@mindspring.com>`

```
i tried to post this before and i never saw it, i got some email telling
me that my time zone was wrong.  (damn those black helicopters!)
anyway, i'm an amateur writing a system to run my muffler shop on and
hopefully sell the software.  the only way i see that it would be
subject to y2k is the fiscal calendar, purging old repair estimates
after 15 days, and billing commercial accounts.  my idea was to have in
the system's "control file" a field for yesterday's date yymmdd.  at
each start-of-day routine, the current date is ACCEPTed from the system
and compared to the previous date.  only once every thousand years would
the date in format yymmdd be "less than" the previous day's date.  since
the system will use a 4-digit year the system will check for the
less-than condition and add 20 instead of 19 to the year.  (i checked,
my amd-k6 stores only 2 digits so far as i can tell so it is a perfect
test machine)
ok, what do you think?
```

#### ↳ Re: y2k-proofing my programs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fc35fb.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com>`

```
skidmike wrote in message <35FC314B.6C5EE424@mindspring.com>...
>each start-of-day routine, the current date is ACCEPTed from the system
>and compared to the previous date.  only once every thousand years would
…[5 more quoted lines elided]…
>ok, what do you think?

It is the Cobol runtime that determines what ACCEPT returns.
The AMD-K6 has nothing to to with this.

You don't really need a "yesterday" field. The standard way of
getting the 4-digit year goes like this:

01  THE-DATE      PIC 9(8).
01  FILLER            REDEFINES THE-DATE.
     02  CC                         PIC 99.
     02  YYMMDD              PIC 9(6).
     02  FILLER                  REDEFINES YYMMDD.
            03  YY                    PIC 99.
            03  MM                  PIC 99.
            03  DD                  PIC 99.

ACCEPT YYMMDD FROM DATE
IF YY < 98
      MOVE 20 TO CC
ELSE
      MOVE 19 TO CC
.

This should work for the next 100 years.
```

##### ↳ ↳ Re: y2k-proofing my programs

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FC48BA.25E4B6EB@mindspring.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net>`

```
i thought about that, but any "if less than <year in this century>"
seemed to be too "patchy" for me.  any way i try to ACCEPT the date from
DATE i get a 6 position field with only the last 2 digits of the year
available.  the way i see it is to let the program find the difference
under a controlled condition  i.e.:
   ACCEPT DATE-IN FROM DATE
       000101
   MOVE date-in to the 8 digit field: 00000101
   OPEN...
   READ...
   IF DATE-STO (which is 98981231) > DATE-IN (which is 00000101) THEN
       string 20 <date-in> into current-date-usage
   the program thereby y2k-proofs itself, with a lot less code.
   oh, and before i forget, CLOSE the control file (which contains more
than the date)
Leif Svalgaard wrote:
> 
> skidmike wrote in message <35FC314B.6C5EE424@mindspring.com>...
…[31 more quoted lines elided]…
> This should work for the next 100 years.
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fc4eac.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <35FC48BA.25E4B6EB@mindspring.com>`

```
I'll try one more time to get you off the idea of storing the date in
the control file. Don't do it, you'll be sorry if you do.

skidmike wrote in message <35FC48BA.25E4B6EB@mindspring.com>...
>i thought about that, but any "if less than <year in this century>"
>seemed to be too "patchy" for me.  any way i try to ACCEPT the date from
…[47 more quoted lines elided]…
>> This should work for the next 100 years.
```

##### ↳ ↳ Re: y2k-proofing my programs

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xc7L1.6$kN6.13736@news2.mia.bellsouth.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net>`

```
A more flexible method is to use a 'moving window'.  In cases where
the date being entered will always be within a certain range of the
then current date, it is easy to resolve the date into the correct
century window in a reliable way.  Here is code which demonstrates a
window of current date -79 years to current date +20 years.  The low
and high numbers can be whatever you choose, but the difference
(high number - low number) must be exactly 99 years.  This code will
work reliably until the year 9999.  One assumes COBOL 85 will be
obsolete by then. ;-)  You can't use this method for birth dates,
unless you will always be dealing with a range of ages no more than
a century wide (e.g. ages 5 to 104: low = -104, high = -5).

           03  CURR-CCYY        PIC  9(04).
           03  CURR-CCYY-R      REDEFINES CURR-CCYY.
               05  CURR-CC          PIC  9(02).
               05  CURR-YY          PIC  9(02).
           03  WORK-CCYY        PIC  9(04).
           03  WORK-CCYY-R      REDEFINES WORK-CCYY.
               05  WORK-CC          PIC  9(02).
               05  WORK-YY          PIC  9(02).

           MOVE <2 digit year> TO WORK-YY.
           PERFORM RESOLVE-CENTURY.
      *    (Resolved 4 digit year is now in WORK-CCYY)

       RESOLVE-CENTURY.
           MOVE FUNCTION CURRENT-DATE (1:4) TO CURR-CCYY.
           MOVE CURR-CC TO WORK-CC.
           IF (WORK-CCYY < CURR-CCYY - 79)
               ADD 100 TO WORK-CCYY
           ELSE IF (WORK-CCYY > CURR-CCYY + 20)
               SUBTRACT 100 FROM WORK-CCYY.
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fd0792.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <xc7L1.6$kN6.13736@news2.mia.bellsouth.net>`

```
You don't need a sliding window for today's date.

Judson McClendon wrote in message ...
>A more flexible method is to use a 'moving window'.  In cases where
>the date being entered will always be within a certain range of the
…[74 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WN7L1.15$Wv6.31232@news3.mia.bellsouth.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <xc7L1.6$kN6.13736@news2.mia.bellsouth.net> <35fd0792.0@news1.ibm.net>`

```
Of course not.  You use today's date to know where to 'slide' the
window, of course.  Didn't you read the post? :-)
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fd1177.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <xc7L1.6$kN6.13736@news2.mia.bellsouth.net> <35fd0792.0@news1.ibm.net> <WN7L1.15$Wv6.31232@news3.mia.bellsouth.net>`

```

Judson McClendon wrote in message ...
>Of course not.  You use today's date to know where to 'slide' the
>window, of course.  Didn't you read the post? :-)

This is the original post:

i tried to post this before and i never saw it, i got some email telling
me that my time zone was wrong.  (damn those black helicopters!)
anyway, i'm an amateur writing a system to run my muffler shop on and
hopefully sell the software.  the only way i see that it would be
subject to y2k is the fiscal calendar, purging old repair estimates
after 15 days, and billing commercial accounts.  my idea was to have in
the system's "control file" a field for yesterday's date yymmdd.  at
each start-of-day routine, the current date is ACCEPTed from the system
and compared to the previous date.  only once every thousand years would
the date in format yymmdd be "less than" the previous day's date.  since
the system will use a 4-digit year the system will check for the
less-than condition and add 20 instead of 19 to the year.  (i checked,
my amd-k6 stores only 2 digits so far as i can tell so it is a perfect
test machine)
ok, what do you think?

---------
seems to me it has to do with discovering what the current date is....
---------

>--
>Judson McClendon      judmc123@bellsouth.net  (remove numbers)
…[49 more quoted lines elided]…
>>>>>and compared to the previous date.  only once every thousand years
would
>>>>>the date in format yymmdd be "less than" the previous day's date.
since
>>>>>the system will use a 4-digit year the system will check for the
>>>>>less-than condition and add 20 instead of 19 to the year.  (i checked,
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Zv8L1.25$Wv6.55569@news3.mia.bellsouth.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <xc7L1.6$kN6.13736@news2.mia.bellsouth.net> <35fd0792.0@news1.ibm.net> <WN7L1.15$Wv6.31232@news3.mia.bellsouth.net> <35fd1177.0@news1.ibm.net>`

```
Yes, but that's not my post.  You responded to, and quoted, my post,
which was about moving (sliding) windows.  Your comment didn't make
sense in regard to my post.  That's why I asked if you had read it. :)
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fd16f7.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35fc35fb.0@news1.ibm.net> <xc7L1.6$kN6.13736@news2.mia.bellsouth.net> <35fd0792.0@news1.ibm.net> <WN7L1.15$Wv6.31232@news3.mia.bellsouth.net> <35fd1177.0@news1.ibm.net> <Zv8L1.25$Wv6.55569@news3.mia.bellsouth.net>`

```
Judson McClendon wrote in message ...
>Yes, but that's not my post.  You responded to, and quoted, my post,
>which was about moving (sliding) windows.  Your comment didn't make
>sense in regard to my post.  That's why I asked if you had read it. :)


Judson,
Yes, I read it, and, yes the code is good, and, yes, this is a useful
technique.
I was just trying to help Mike with his original problem and not confuse
him with other issues...

End of thread?
```

#### ↳ Re: y2k-proofing my programs

- **From:** Jeff Farkas <Jeffrey.Farkas@gte.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tjope$1fg$1@news-2.news.gte.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com>`

```
skidmike wrote:
> 
> i tried to post this before and i never saw it, i got some email telling
…[7 more quoted lines elided]…
> and compared to the previous date. 
   
  OK, lets just stop here and let me ask a few questions to see if
I understand what you are attempting to accomplish.  I may not 
fully understand what you are doing and why you need to store
the date on a control file.

    1)  I am assuming when you start up the computer first thing 
         in the morning it will be set up to perform some of the 
         house keeping functions, purge files of old estimates ect.

     2) Question, why do you want to store yesterdays date? I 
          would assume that it would be determine when it is the
          first start up of the day so you would perform the
          house keeping routine?  By storing the date you will make sure
          if the computer is restarted during the day that the house
          keeping function is performed only once.
         

> only once every thousand years would the date in format yymmdd 
>be "less than" the previous day's date.  since
…[4 more quoted lines elided]…
> ok, what do you think?

  I think I more interested in why you are doing this rather than how.
You have a coupe of good ideas posted on how what I am curious 
about is the Why?  
```

##### ↳ ↳ Re: y2k-proofing my programs

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tkcqe$av0$1@news.igs.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <6tjope$1fg$1@news-2.news.gte.net>`

```
>     2) Question, why do you want to store yesterdays date? I
>          would assume that it would be determine when it is the
…[3 more quoted lines elided]…
>          keeping function is performed only once.


As an aside, I have a program that goes in every autoexec that does
exactly that.  It reads the last boot date/time off the disk, checks that
the clock has not gone backwards, then updates the disk. If it has
gone backwards, then it pops open a windows, and asks the operator
to check the clock, as the most likely problem is a bad clock/battery.

I wrote it one day after having a system generate an entire day's
transactions with the date set wrong. It created havoc.
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

- **From:** Jeff Farkas <Jeffrey.Farkas@gte.net>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tlncc$qk0$1@news-2.news.gte.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <6tjope$1fg$1@news-2.news.gte.net> <6tkcqe$av0$1@news.igs.net>`

```
Donald Tees wrote:
> 
> >     2) Question, why do you want to store yesterdays date? I
…[13 more quoted lines elided]…
> transactions with the date set wrong. It created havoc.

Thanks for the info. That  is a good thing to know and 
remember. I bet cleaning that mess up was a bit of a 
pain in the old ass! <g>

PS, it is a shame that old Mike does not what to 
divulge the reason why he wants to do his date
thing. I guess he is afraid that one of us will steal
the idea and he will not get all those big bucks from
his unique idea. <HUGE G>

Mike: If you happen to read this, if we know why you
want to do your date thing maybe we can give you a better
method of doing what you want to accomplish!
```

#### ↳ Re: y2k-proofing my programs

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35feb378.3511080@nntp.ix.netcom.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com>`

```
On Sun, 13 Sep 1998 16:55:39 -0400, skidmike <skidmike@mindspring.com>
wrote:

the only way i see that it would be
>subject to y2k is the fiscal calendar, purging old repair estimates
>after 15 days, and billing commercial accounts.  my idea was to have in
…[3 more quoted lines elided]…
>the date in format yymmdd be "less than" the previous day's date.  

how about instead, if you know that the number of days difference in
the repair estimate *must* be positive, to simply
get the absolute value of the difference of days?


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: y2k-proofing my programs

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FDBE90.68FCE9EA@mindspring.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35feb378.3511080@nntp.ix.netcom.com>`

```
I am either an amateur or dense.  probably both.  ok, here's what i did
to see what would happen.  wrote a small cobol pgm to simply ACCEPT and
DISPLAY the date.  all i can get is 6 digits 98mmdd.  so the way i see
it is i have to write the software to put the 19 in front of the year in
my DATE-USAGE PIC 9(8) field and catch the discrepancy when ACCEPT
DATE-IN FROM DATE yields 000101 and is less than dec. 31, 1999.  maybe
when rewriting several thousand lines of someone else's code to keep
armageddon at bay for another 50 years or so is one thing, but when
writing from scratch, might as well head it off at the pass.  my project
uses and 8 digit date field yyyymmdd and there you go.
i am probably doing it the long way or totally unconventional but it's
the best i could think of and seems to be a good preventative measure
for the long run. but i am saving and printing posts with anything to do
with y2k coding.

G Moore wrote:
> 
> On Sun, 13 Sep 1998 16:55:39 -0400, skidmike <skidmike@mindspring.com>
…[14 more quoted lines elided]…
> gvwmoore@ix.spam.netcom.com to reply remove the spam
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tkhf1$so1@dfw-ixnews8.ix.netcom.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35feb378.3511080@nntp.ix.netcom.com> <35FDBE90.68FCE9EA@mindspring.com>`

```
To get the 8 digit date in COBOL:
   Assume a Working-Storage item
    05  My-8-Digit-Field  Pic 9(08).

A)  use (this is Standard and works with any CURRENT compiler - but not old
ones)
    Move Function Current-date (1:8) to my-8-digit-field.

B) If you have a compiler that will accept it (Micro Focus and IBM do
already and I think some others are starting to - and it will be in the next
Standard), use
    Accept my-8-digit-field from date YYYYMMDD

C) If you happen to be running on an IBM mainframe and have VS COBOL II but
not LE, then use
   Call "IGZEDT4" using my-8-digit-field

skidmike wrote in message <35FDBE90.68FCE9EA@mindspring.com>...
>I am either an amateur or dense.  probably both.  ok, here's what i did
>to see what would happen.  wrote a small cobol pgm to simply ACCEPT and
…[30 more quoted lines elided]…
>> gvwmoore@ix.spam.netcom.com to reply remove the spam
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

_(reply depth: 4)_

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn6vt615.iu.cadams@cadams-ntw.acucorp.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35feb378.3511080@nntp.ix.netcom.com> <35FDBE90.68FCE9EA@mindspring.com> <6tkhf1$so1@dfw-ixnews8.ix.netcom.com>`

```
On Mon, 14 Sep 1998 William M. Klein <wmklein@ix.netcom.com> wrote:
>B) If you have a compiler that will accept it (Micro Focus and IBM do
>already and I think some others are starting to - and it will be in the next
>Standard), use
>    Accept my-8-digit-field from date YYYYMMDD

Just for reference, Acucobol-GT 4.3 will support this syntax. In the meantime,
ACCEPT date FROM CENTURY-DATE has been available for quite awhile.

----
# Chris Adams <cadams@acucorp.com>
```

##### ↳ ↳ Re: y2k-proofing my programs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ffbdd5.0@news1.ibm.net>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35feb378.3511080@nntp.ix.netcom.com>`

```

G Moore wrote in message <35feb378.3511080@nntp.ix.netcom.com>...
>On Sun, 13 Sep 1998 16:55:39 -0400, skidmike <skidmike@mindspring.com>
>wrote:
…[12 more quoted lines elided]…
>

Won't work Mr. G, as you cannot simply subtract two yymmdd's
to get the difference in days.
```

###### ↳ ↳ ↳ Re: y2k-proofing my programs

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360a33db.9087780@nntp.ix.netcom.com>`
- **References:** `<35FC314B.6C5EE424@mindspring.com> <35feb378.3511080@nntp.ix.netcom.com> <35ffbdd5.0@news1.ibm.net>`

```
On Wed, 16 Sep 1998 08:31:59 -0500, "Leif Svalgaard" <leif@ibm.net>
wrote:

>>how about instead, if you know that the number of days difference in
>>the repair estimate *must* be positive, to simply
>>get the absolute value of the difference of days?

>Won't work Mr. G, as you cannot simply subtract two yymmdd's
>to get the difference in days.


good point. in any case, this sounds like a job for file expansion,
since 15 days of repair estimates for 1 shop not working 24/7 does
have plenty of extra i/o cycles. (i am assuming that since
you are developing this yourself, its not on a micro or mainframe)

look up my y2k tutorial posted on dejanews to this newsgroup.



gvwmoore@ix.spam.netcom.com to reply remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
