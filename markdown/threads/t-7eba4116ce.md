[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# STD: Leap Seconds and COBOL

_76 messages · 24 participants · 2000-01 → 2000-02_

---

### STD: Leap Seconds and COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
I just thought I would let this NG know that the J4 (and WG4) distribution
lists are having an "interesting" (and almost heated) discussion about adding
support for leap-seconds into the revision of the Standard.  (This would
impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM TIME).

The Standard (as I understand it) won't require that an operating system be
able to "get" leap-seconds, but if the OS does support them, then "60" would
be a valid value for the second portion of these features.  (It turns out  -
from some international research - that leap-seconds are added to the minute
beginning 23:59 GMT - and that each time zone around the world MIGHT end-up
adding them to different hours - when "midnight" reaches GMT.  Particularly
interesting for time-zones - and there are some - that are 30-minutes plus
some hours off of GMT.  I think there may also be some that are either 15 or
45 minutes off - but I haven't seen that confirmed yet.)

Problems/Questions:

If your operating system DOES return a second value of "60" but the COBOL
Standard doesn't allow that, what is the COBOL run-time supposed to do?
  - return 59 or 00 for two seconds in a row?
 - return 59 for a second and a half and then 00 for the next second an a
half?
 - put the program in "wait state" for a second until a "valid" value is
available?
 - other?

If COBOL is "enhanced" to allow for a value of "60" in the second portion of
these features how serious will the incompatibles be (for existing - and NEW
applications)
 - Tables built for 60 entries over-flowing when they get a 61st entry?
 - Databases that use timestamps not accepting the values?
 - Calculations for "intervals" between split-second actions being wrong?
 - User interfaces and reports "bombing" for date/time validation errors?
 - Other?

***

I don't think that I am asking this NG for input to J4, but did want to alert
you to how even such a MINOR change like this can account for the
difficulties in getting a revision to the Standard complete AND ACCURATE.

If you really do want to say something to J4 about this, you should probably
send a note ASAP to the chair - as this will (probably) be discussed at the
J4 meeting next week. He can be reached at:

   doncobol <at> mediaone.net
```

#### ↳ Re: Leap Seconds and COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ky%e4.535$Oe.4748@dfiatx1-snr1.gtei.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote in message <85h88q$ram$1@nntp9.atl.mindspring.net>...
>I just thought I would let this NG know that the J4 (and WG4) distribution
>lists are having an "interesting" (and almost heated) discussion about
adding
>support for leap-seconds into the revision of the Standard.

Gawd, how I miss the corporate world...committees, consensus, politics,
molehills yearning for mountainhood....


Michael Mattias
Racine WI USA
```

#### ↳ Re: STD: Leap Seconds and COBOL

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000112093350.06658.00001870@ng-fc1.aol.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
I think they should return 

-00:00:00 UTC

That way anyone who doesn't care to know can see zero as zero because their
machines will zap the sign. But if you care just treat it as a signed field,
and check for less than +0!

Same for anyone who is caught straddling a 15 minute mark for two seconds: if
you care, check for negative; if not, force sign to positive and the rest of
the day is yours!

As long as the value comes from a special register, the hardware gurus should
be able to control the sign.

But now, of course, we need a convention to decide if the negative zero follows
the positive zero in time,  or the other way around.  And, naturally,
high-level meetings to design the special FUNCTIONS that will disambiguate this
earth shattering problem.

We need, we can be sure, a FUNCTION to return the number of leap seconds thus
far in the epoc, and a FUNCTION to return the number of leap seconds before
chicken little freaks out and adds bits to the TOD register in 2041.

And of course, there must be meetings, and corporate expense accounts for those
attending the grand convocations.

And when it is all compiled, they sure better copyright it, and not let anyone
reproduce it without permission. All those explicated leap seconds in there,
and what not. 








 
Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: STD: Leap Seconds and COBOL

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-2qbpdboMISsi@localhost>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
On Thu, 1 Jan 1970 00:59:59, "William M. Klein" 
<wmklein@nospam.netcom.com> wrote:

> If COBOL is "enhanced" to allow for a value of "60" in the second portion of
> these features how serious will the incompatibles be (for existing - and NEW
> applications)

This will break several of my programs.

-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ucehF6SX$GA.254@cpmsnbbsa02>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
Would it be possible to have the implementation of FUNCTION return the Leap
Seconds as a separate field dependent on the length of the receiving field.
This would minimize the impact on existing systems, and allow people to
address the situations where is has impact.

     05  PGM-CURRENT-DT.

       10  PGM-CURRENT-DT-YYYY       PIC X(04).
       10  PGM-CURRENT-DT-MM          PIC X(02).
       10  PGM-CURRENT-DT-DD          PIC X(02).
       10  PGM-CURRENT-DT-HR           PIC X(02).
       10  PGM-CURRENT-DT-MN           PIC X(02).
       10  PGM-CURRENT-DT-SC           PIC X(02).
       10  PGM-CURRENT-DT-SC100    PIC X(02).
       10  PGM-CURRENT-GMT-SEP     PIC X.
       10  PGM-CURRENT-GMT-HR        PIC X(02).
       10  PGM-CURRENT-GMT-MN        PIC X(02).
       10  PGM-CURRENT-LEAP-SEC    PIC X(02).
CURRENT-LEAP-SEC returned only if the
Length of PGM-CURRENT-DT says that I want it.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:85h88q$ram$1@nntp9.atl.mindspring.net...
> I just thought I would let this NG know that the J4 (and WG4) distribution
> lists are having an "interesting" (and almost heated) discussion about
adding
> support for leap-seconds into the revision of the Standard.  (This would
> impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM
TIME).
>
> The Standard (as I understand it) won't require that an operating system
be
> able to "get" leap-seconds, but if the OS does support them, then "60"
would
> be a valid value for the second portion of these features.  (It turns
ut  -
> from some international research - that leap-seconds are added to the
minute
> beginning 23:59 GMT - and that each time zone around the world MIGHT
end-up
> adding them to different hours - when "midnight" reaches GMT.
Particularly
> interesting for time-zones - and there are some - that are 30-minutes plus
> some hours off of GMT.  I think there may also be some that are either 15
or
> 45 minutes off - but I haven't seen that confirmed yet.)
>
…[11 more quoted lines elided]…
> If COBOL is "enhanced" to allow for a value of "60" in the second portion
of
> these features how serious will the incompatibles be (for existing - and
NEW
> applications)
>  - Tables built for 60 entries over-flowing when they get a 61st entry?
…[7 more quoted lines elided]…
> I don't think that I am asking this NG for input to J4, but did want to
alert
> you to how even such a MINOR change like this can account for the
> difficulties in getting a revision to the Standard complete AND ACCURATE.
>
> If you really do want to say something to J4 about this, you should
probably
> send a note ASAP to the chair - as this will (probably) be discussed at
the
> J4 meeting next week. He can be reached at:
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85imnp$csr$1@nntp9.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <ucehF6SX$GA.254@cpmsnbbsa02>`

```
I don't think that this would work for (at least) a couple of reasons:

1) The current rules are set up so that you can use FUNCTION CURRENT-DATE
with either truncation or padding - depending on where you "move" it to.

2) It doesn't really have a place that you define a receiving field.  For
example, one of the most common places that I see it used (today) is in
expressions like

   Move Function Current-Date (1:4) to Get-Current-Year

In a case like this, you don't really "have" a receiving item for the
function itself.

It *could* (compatibly - I think) take a new OPTIONAL argument - so something
like
     Function Current-Date (WITH-LEAP)
would mean that you want to get the leap-second - However, that still doesn't
answer what the COBOL run-time should do if it gets a leap-second value
(60) - but the argument is included.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OwNNrxUX$GA.250@cpmsnbbsa02>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <ucehF6SX$GA.254@cpmsnbbsa02> <85imnp$csr$1@nntp9.atl.mindspring.net>`

```
The reference modification in
Move Function Current-Date (1:4) to Get-Current-Year
inplies a length of 4 for Get-Current-Year.

I do like Function Current-Date (WITH-LEAP)

My main concern is that ignoring the leap second may be cheaper than
remediation.
There are instances when it is significant. These cases tend to be rare.

Many shops have date-time algorythms hard coded in programs (no common
sub-routines).
If the standard changes, it should be done in a way that will minimize its
impact.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:85imnp$csr$1@nntp9.atl.mindspring.net...
> I don't think that this would work for (at least) a couple of reasons:
>
…[12 more quoted lines elided]…
> It *could* (compatibly - I think) take a new OPTIONAL argument - so
something
> like
>      Function Current-Date (WITH-LEAP)
> would mean that you want to get the leap-second - However, that still
doesn't
> answer what the COBOL run-time should do if it gets a leap-second value
> (60) - but the argument is included.
…[6 more quoted lines elided]…
> > Would it be possible to have the implementation of FUNCTION return the
Leap
> > Seconds as a separate field dependent on the length of the receiving
field.
> > This would minimize the impact on existing systems, and allow people to
> > address the situations where is has impact.
…[23 more quoted lines elided]…
> > > support for leap-seconds into the revision of the Standard.  (This
would
> > > impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM
> > TIME).
> > >
> > > The Standard (as I understand it) won't require that an operating
system
> > be
> > > able to "get" leap-seconds, but if the OS does support them, then "60"
…[11 more quoted lines elided]…
> > > some hours off of GMT.  I think there may also be some that are either
15
> > or
> > > 45 minutes off - but I haven't seen that confirmed yet.)
…[3 more quoted lines elided]…
> > > If your operating system DOES return a second value of "60" but the
COBOL
> > > Standard doesn't allow that, what is the COBOL run-time supposed to
do?
> > >   - return 59 or 00 for two seconds in a row?
> > >  - return 59 for a second and a half and then 00 for the next second
an a
> > > half?
> > >  - put the program in "wait state" for a second until a "valid" value
is
> > > available?
> > >  - other?
> > >
> > > If COBOL is "enhanced" to allow for a value of "60" in the second
portion
> > of
> > > these features how serious will the incompatibles be (for existing -
and
> > NEW
> > > applications)
> > >  - Tables built for 60 entries over-flowing when they get a 61st
entry?
> > >  - Databases that use timestamps not accepting the values?
> > >  - Calculations for "intervals" between split-second actions being
wrong?
> > >  - User interfaces and reports "bombing" for date/time validation
errors?
> > >  - Other?
> > >
> > > ***
> > >
> > > I don't think that I am asking this NG for input to J4, but did want
to
> > alert
> > > you to how even such a MINOR change like this can account for the
> > > difficulties in getting a revision to the Standard complete AND
ACCURATE.
> > >
> > > If you really do want to say something to J4 about this, you should
> > probably
> > > send a note ASAP to the chair - as this will (probably) be discussed
at
> > the
> > > J4 meeting next week. He can be reached at:
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ STD:Leap Seconds and COBOL

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-d9yqdBdbGzyK@localhost>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <ucehF6SX$GA.254@cpmsnbbsa02>`

```
On Sun, 12 Jan 3900 13:51:55, "DennisHarley" 
<LegacyBlue@email.msn.com> wrote:

> Would it be possible to have the implementation of FUNCTION return the Leap
> Seconds as a separate field dependent on the length of the receiving field.
> This would minimize the impact on existing systems, and allow people to
> address the situations where is has impact.
Returning 60 is not good.

However, let me ask a more basic question.   My understanding is that 
Leap Seconds are added at erratic, and unpredictable intervals as the 
earths orbit around the sun changes.  Just how is the COBOL 
implementation to know about when to add these leap seconds?


-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: STD:Leap Seconds and COBOL

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38827948.689AEEAB@home.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <ucehF6SX$GA.254@cpmsnbbsa02> <Jl0PnHJ5PvPd-pn2-d9yqdBdbGzyK@localhost>`

```
Thane Hubbell wrote:
 [snip]

I think there are two questions here.  One is a need to have a
monotonically increasing time reference.  In many ways it is not
relevant that the time be "real" in any sense of the word.  I mentioned
that I work on a system that is arbitrarily declared to be in UTC
because the actual time zone is too much hassle for the system
programmer.

I can't imagine that slowing down or speeding up the clock would make a
difference in >most< applications.  Regrettably, the ones that break are
probably the most business critical ones -  Are SWIFT/EDIFACT money
transfers time stamped?

But leap seconds have to do with relating clock time to "real,"
astronomical time (I think).  I still haven't heard how they propose to
synchronize all the world's computer clocks.

And, to throw more sticky brown into the discussion, if I remember my
Einstein it is not correct to say that it is "the same time" at two
separated points anyway.  In simpler language, by the time you
synchronize your clocks at least one of them is wrong.
```

###### ↳ ↳ ↳ Re: STD:Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LsLg4.974$SM.12838@news4.mia>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <ucehF6SX$GA.254@cpmsnbbsa02> <Jl0PnHJ5PvPd-pn2-d9yqdBdbGzyK@localhost> <38827948.689AEEAB@home.com>`

```
David A. Cobb wrote:
>
>And, to throw more sticky brown into the discussion, if I remember my
>Einstein it is not correct to say that it is "the same time" at two
>separated points anyway.  In simpler language, by the time you
>synchronize your clocks at least one of them is wrong.

True.  Time measured anywhere on the surface of the earth can be no
more exact than about .047 sec. to clocks on the other side of the
earth.
```

#### ↳ Re: STD: Leap Seconds and COBOL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1nfq7s8cac7o4f37oe4331prbko53r0cn3@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>The Standard (as I understand it) won't require that an operating system be
>able to "get" leap-seconds, but if the OS does support them, then "60" would
>be a valid value for the second portion of these features. 

good. having an extra second every year is a pretty excessive
function. i mean if the time is off, during downtime (or if it's
networked, it will update itself from other networked machines), set
the clock back 1 second.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: Leap Seconds and COBOL

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0snf4.162$8z5.2223@news4.mia>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote in message <85h88q$ram$1@nntp9.atl.mindspring.net>...
>I just thought I would let this NG know that the J4 (and WG4) distribution
>lists are having an "interesting" (and almost heated) discussion about adding
>support for leap-seconds into the revision of the Standard.  (This would
>impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM TIME).

Send the same time for two seconds in a row.  Is this not what a 'leap
second' is anyway?  In my opinion, this would crash far fewer (maybe none)
existent programs than changing the format.
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85mllp$ndb$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia>`

```
    Unless the computer in question has a real time connection to an atomic
clock, just ignore
the leap second completely.  The time will be slow by 1 additional second
until someone corrects
it one way or another.  Most computer clocks are none too good at keeping
exact time anyway.

    If someone does have a need for EXACT time of day, than that program
should run on hardware
with a non standard clock interface.  The best bet seems to be the
suggestion below when leap seconds
MUST be supported.



"Judson McClendon" <judmc@bellsouth.net> wrote in message
news:0snf4.162$8z5.2223@news4.mia...
> William M. Klein wrote in message
<85h88q$ram$1@nntp9.atl.mindspring.net>...
> >I just thought I would let this NG know that the J4 (and WG4)
distribution
> >lists are having an "interesting" (and almost heated) discussion about
adding
> >support for leap-seconds into the revision of the Standard.  (This would
> >impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM
TIME).
>
> Send the same time for two seconds in a row.  Is this not what a 'leap
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OMW#qvmX$GA.265@cpmsnbbsa04>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <85mllp$ndb$1@ssauraab-i-1.production.compuserve.com>`

```
The example you supplied does NOT support leap seconds, it ignores them.

Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote in message
news:85mllp$ndb$1@ssauraab-i-1.production.compuserve.com...
>     Unless the computer in question has a real time connection to an
atomic
> clock, just ignore
> the leap second completely.  The time will be slow by 1 additional second
…[20 more quoted lines elided]…
> > >support for leap-seconds into the revision of the Standard.  (This
would
> > >impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM
> TIME).
> >
> > Send the same time for two seconds in a row.  Is this not what a 'leap
> > second' is anyway?  In my opinion, this would crash far fewer (maybe
none)
> > existent programs than changing the format.
> > --
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85n860$346$1@nntp5.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <85mllp$ndb$1@ssauraab-i-1.production.compuserve.com>`

```
IBM mainframe *can* access universal clocks (for synchronizing across CPUs -
this is a simplification but does give a clue why this is such a "big deal").
The rest of their software is "gradually" being upgraded to return a value of
"60" when a leap-second occurs, so I still do NOT like the thought of COBOL
returning a different time value that other software (such as CALLs to LE
time services).

For those who want COBOL to return a "59" for an extra second, this really
ALSO means sending out "99" in the hundreths of a second for 101 hundredths
of a second.  Otherwise, you start "reversing" time which isn't a good idea -
or requiring a 3-digit field for hundredths of a second which would REALLY be
confusing and incompatible.
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387FE57A.8D6A6F69@home.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia>`

```
Would not any implementation requiring leap seconds -- or indeed any
"exact real time" require the world-wide acknowledgment of one reference
standard clock to which we would all need to connect?

I don't think leap seconds are random.  I watch usno.navy.mil and I see
announcements that the PTB have declared a leap second at such and such
a time UTC.  

How many satellite tracking systems, or whatever, are written in COBOL? 
For pete's sake, my PC gets corrected at least daily in the seconds
field.

In the business world, reality is probably more like my place of
business where the system programmer tells the mainframe we're at
UTC+0000 because it's less trouble.
------------------------
David A. Cobb, Software Engineer
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q8308sgo42b986sih2durk2669i9oquuiu@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com>`

```
"David A. Cobb" <superbiskit@home.com> wrote:

>Would not any implementation requiring leap seconds -- or indeed any
>"exact real time" require the world-wide acknowledgment of one reference
…[8 more quoted lines elided]…
>field.

my pc's minutes get corrected twice a year (and even then, i don't
call up the time service. i simply add 1 hour or subtract 1). plus, it
also gets corrected upon purchase of a new machine (but the correction
is to take my cable tv guides clock and simply copy over the minutes).

i can't think of any machine which needs seconds correction at all.
after all, how many transactions (disk io accounted for) can you
possibly make in 1 second, and how much interest off of it?

hell, they float checks for multiple days, as it is.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85rlht$a9l$1@nntp6.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com>`

```
You start telling an IBM mainframe shop that they are limited to a single
transaction or database update per second (much less for the two seconds
covered by "59" and "60") for a production CICS or DB2 application, and you
better "duck".

I understand that there may be some (but certainly not all) PC or
client/server applications where this would be acceptable - but BELIEVE ME,
it isn't in the whole world that COBOL serves.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 5)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<it268so4v38qnacvp3ebiq4pvqd5r2ct74@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com> <85rlht$a9l$1@nntp6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>You start telling an IBM mainframe shop that they are limited to a single
>transaction or database update per second (much less for the two seconds
>covered by "59" and "60") for a production CICS or DB2 application, and you
>better "duck".

once per year, where they decide when to schedule it? i don't think
that's a problem. there is no practical application for having a leap
second instituted, other than the atomic clock. who would notice 1
second difference in transactions? i sure wouldn't. 1 minute every 60
years? nope. i am certain even mainframes have downtime 1 minute every
60 years.

>I understand that there may be some (but certainly not all) PC or
>client/server applications where this would be acceptable - but BELIEVE ME,
>it isn't in the whole world that COBOL serves.

any mainframe which can't institute downtime to have a leap second,
obviously can't handle day-light savings either, right?

>> >I don't think leap seconds are random.  I watch usno.navy.mil and I see
>> >announcements that the PTB have declared a leap second at such and such
>> >a time UTC.

ahhh, here is our problem. the leap seconds are instituted by some
entity, not at the programmers discretion. even with this problem,
let's pretend you are a big, huge bank with billions in transactions.
how much hassle will the customer give? i know that if i go to a bank,
unless i am dealing with millions, i won't have a chance in hell of
making interest off the extra second. interest isn't even paid by the
second in smaller accounts. so the solution is to add additional code
to the interest calculation, and not the cobol standard.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388187E9.8187F61C@worldnet.att.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com>`

```
G Moore wrote:
> 
> i can't think of any machine which needs seconds correction at all.
> after all, how many transactions (disk io accounted for) can you
> possibly make in 1 second, and how much interest off of it?

I once participated in a stress test of a CICS COBOL application that
logged 185 transactions per second, sustained, for twenty minutes.  Each
transaction consisted of a minimum of five VSAM I/O's, most of them
KSDS.

This was just one large application on a multi-engine CPU running
hundreds of applications concurrently.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 5)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g368ssul3aa5c0ep0e1h9ufvei9sv5nfr@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com> <388187E9.8187F61C@worldnet.att.net>`

```
Arnold Trembley <arnold.trembley@worldnet.att.net> wrote:

>G Moore wrote:
 
>> i can't think of any machine which needs seconds correction at all.
>> after all, how many transactions (disk io accounted for) can you
>> possibly make in 1 second, and how much interest off of it?

>I once participated in a stress test of a CICS COBOL application that
>logged 185 transactions per second, sustained, for twenty minutes.  Each
>transaction consisted of a minimum of five VSAM I/O's, most of them
>KSDS.

i understand all but the ksds part. that does mean direct write, and
not queued, i hope?


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388388EF.CA059142@worldnet.att.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com> <388187E9.8187F61C@worldnet.att.net> <7g368ssul3aa5c0ep0e1h9ufvei9sv5nfr@4ax.com>`

```
G Moore wrote:
> 
> Arnold Trembley <arnold.trembley@worldnet.att.net> wrote:
…[13 more quoted lines elided]…
> not queued, i hope?

In VSAM (Virtual Storage Access Method) there are three kinds of files:

ESDS - Entry Sequenced Data Set
KSDS - Key Sequenced Data Set
RRDS - Relative Record Data Set

When writing to a KSDS there are two components to be updated, the key
file and the data file.  When reading a KSDS data set there are two
components that must be read, first the key file and then the data
file.  In practice, key files will likely be cached, but every KSDS file
access could potentially result in two physical I/O's, possibly more if
control area splits are involved.

My point was that when doing five VSAM I/O's per transaction, the
underlying systems software might need to do more than five physical
I/O's.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** Lawrence Allen Free <free@mcs.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<860pri$189$1@Nntp1.mcs.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <0snf4.162$8z5.2223@news4.mia> <387FE57A.8D6A6F69@home.com> <q8308sgo42b986sih2durk2669i9oquuiu@4ax.com>`

```
In article q8308sgo42b986sih2durk2669i9oquuiu@4ax.com,
	G Moore <gvwmoore@spam.ix.netcom.com> said:
>
>
…[36 more quoted lines elided]…
>

There are a few computers that require such precision, though 
none in COBOL.  Examples are navagational computers which 
need to know the time to the millisecond or process monitoring 
machines.  These generally use an outside time reference which 
does not require the program to keep track of time.  Any language
can reference these.
```

#### ↳ Re: Leap Seconds and COBOL

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qqQf4.929$nh2.23200@cac1.rdr.news.psi.ca>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
 William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:85h88q$ram$1@nntp9.atl.mindspring.net...
> I just thought I would let this NG know that the J4 (and WG4) distribution
> lists are having an "interesting" (and almost heated) discussion about
adding
> support for leap-seconds into the revision of the Standard.  (This would
> impact FUNCTION CURRENT-DATE, FUNCTION WHEN-COMPILED, and ACCEPT FROM
TIME).
>
> The Standard (as I understand it) won't require that an operating system
be
> able to "get" leap-seconds, but if the OS does support them, then "60"
would
> be a valid value for the second portion of these features.  (It turns
ut  -
> from some international research - that leap-seconds are added to the
minute
> beginning 23:59 GMT - and that each time zone around the world MIGHT
end-up
> adding them to different hours - when "midnight" reaches GMT.
Particularly
> interesting for time-zones - and there are some - that are 30-minutes plus
> some hours off of GMT.  I think there may also be some that are either 15
or
> 45 minutes off - but I haven't seen that confirmed yet.)
>
…[11 more quoted lines elided]…
> If COBOL is "enhanced" to allow for a value of "60" in the second portion
of
> these features how serious will the incompatibles be (for existing - and
NEW
> applications)
>  - Tables built for 60 entries over-flowing when they get a 61st entry?
…[7 more quoted lines elided]…
> I don't think that I am asking this NG for input to J4, but did want to
alert
> you to how even such a MINOR change like this can account for the
> difficulties in getting a revision to the Standard complete AND ACCURATE.
>
> If you really do want to say something to J4 about this, you should
probably
> send a note ASAP to the chair - as this will (probably) be discussed at
the
> J4 meeting next week. He can be reached at:
>
…[6 more quoted lines elided]…
>

I tried reading all the messages and I've come to the conclusion that unless
something is very time dependant then a change to allow a 60 second would be
good, however, a leap second is not, I repeat, not added every year.  For
normal time keeping, it's a non-event.

Tim.
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85otf0$9to$1@aklobs.kc.net.nz>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <qqQf4.929$nh2.23200@cac1.rdr.news.psi.ca>`

```
Tim Hillock <hillock@istar.ca> wrote:

: I tried reading all the messages and I've come to the conclusion that unless
: something is very time dependant then a change to allow a 60 second would be
: good, however, a leap second is not, I repeat, not added every year.  For
: normal time keeping, it's a non-event.

Leap seconds are added or subtracted whenever the difference between
UTC and GMT exceeds 0.7 seconds.  This is generally unpredicatable
over a long period but trends are taken into account and the adjustments
are scheduled for various times.  

Any computer clock will not be accurate enough to bother with
leap seconds and if there is a requirement for accuracy to the
second there will be a mechanism to obtain a more accurate
time on a regular basis to keep the clock within a second or so.

As this will require the computer clock to be adjusted when it
is found to not match the accurate clock then _any_ minute 
could have more or less than 60 seconds with any seconds being
repeated or dropped when the adjustment is made.  Just cope with
it.
```

#### ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uKXqqYyX$GA.211@cpmsnbbsa05>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net>`

```
Support for Leap Seconds is a business decision, not a programming decision.

If a business faces regulatory censure, fines, or law suits because they did
not support leap seconds then there will be an effort to support leap
seconds.

There have been rumors that stock trading will become a 24/7 event.
If this happens, there are no "off-hours" during which time can be adjusted,
and leap seconds will have to be used.

This would also require that a standard time be used (I would guess GMT),
and that system clocks would have to be syncronized.

Leap Seconds are not relavent to most business applications. They may be
relavent to some applications within some industries.
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05>`

```
"DennisHarley" <LegacyBlue@email.msn.com> wrote:

>Support for Leap Seconds is a business decision, not a programming decision.
>
>If a business faces regulatory censure, fines, or law suits because they did
>not support leap seconds then there will be an effort to support leap
>seconds.

>There have been rumors that stock trading will become a 24/7 event.
>If this happens, there are no "off-hours" during which time can be adjusted,
>and leap seconds will have to be used.

despite the rumors, there is still the fact that online-trading
doesn't happen in real-time. it happens at the speed the corporation
allows it to happen.

i can't think of any program, which would require leap seconds other
than the atomic clock. pretend, for a moment you don't add in the leap
second. then every 60 years, you will be off 1 WHOLE MINUTE.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#iKy#ZLY$GA.297@cpmsnbbsa03>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com>`

```
Speed is not the issue, the sequence of events is the issue.

G Moore <gvwmoore@spam.ix.netcom.com> wrote in message
news:c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com...
>
> despite the rumors, there is still the fact that online-trading
> doesn't happen in real-time. it happens at the speed the corporation
> allows it to happen.

Speed is not the issue, the sequence of events is the issue.

On-line trading done by you or I will not cause anyone to lose sleep.
However, large Mutual Funds have clout, if they lose money because their
trades were affected, they would probably sue.

> i can't think of any program, which would require leap seconds other
> than the atomic clock. pretend, for a moment you don't add in the leap
> second. then every 60 years, you will be off 1 WHOLE MINUTE.
>

Some industries will not be able to tolerate an error this large.
i.e. We processed your order before you sent it in.
Things are getting faster, and faster.
Look to the future.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i0468skn6ha8a34pkc6ibo9rikstctps4k@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com> <#iKy#ZLY$GA.297@cpmsnbbsa03>`

```
"DennisHarley" <LegacyBlue@email.msn.com> wrote:

>> despite the rumors, there is still the fact that online-trading
>> doesn't happen in real-time. it happens at the speed the corporation
>> allows it to happen.

>Speed is not the issue, the sequence of events is the issue.

>On-line trading done by you or I will not cause anyone to lose sleep.
>However, large Mutual Funds have clout, if they lose money because their
>trades were affected, they would probably sue.

i doubt they would sue for a leap second, as it would open up their
records to possible other problems.

>> i can't think of any program, which would require leap seconds other
>> than the atomic clock. pretend, for a moment you don't add in the leap
>> second. then every 60 years, you will be off 1 WHOLE MINUTE.

>Some industries will not be able to tolerate an error this large.
>i.e. We processed your order before you sent it in.

if they can't handle daylight savings, they surely can't handle 1 leap
second.

>Things are getting faster, and faster.
>Look to the future.

things to me don't look like they are getting faster. you still get
all your withdrawals dated today, but deposits tommorrow. all
accounting still must be done by hand. and you can no longer hire
anyone but experts who have 4 years of college under their belt. doing
1 million transactions doesn't help much, if there are human and
administrative bottlenecks. you still must sign credit cards. people
surely can't type faster. you can't buy a stock without an
administrative fee. you can't use an ATM outside your bank without an
administrative fee. they still require verification for all credit
purchases. that's just dealing with money. technology has made
transmission of ideas easier, because of having a human who can talk
at the other end, at their leisure.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 5)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u2mw2i2Y$GA.253@cpmsnbbsa02>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com> <#iKy#ZLY$GA.297@cpmsnbbsa03> <i0468skn6ha8a34pkc6ibo9rikstctps4k@4ax.com>`

```
I had some extra time on my hands.

I said that things are getting faster, you disagreed.

G Moore <gvwmoore@spam.ix.netcom.com> wrote in message
news:i0468skn6ha8a34pkc6ibo9rikstctps4k@4ax.com...
>
> things to me don't look like they are getting faster. you still get
> all your withdrawals dated today, but deposits tommorrow. all
> accounting still must be done by hand. and you can no longer hire
> anyone but experts who have 4 years of college under their belt.

If all accounting is being done by hand, why am I writing programs to do it?
Summaries are reviewed after the fact.

> doing 1 million transactions doesn't help much, if there are human and
> administrative bottlenecks. you still must sign credit cards. people
…[6 more quoted lines elided]…
>

When I go into a store to buy something this is what normally happend.

The cashier scans the UPC.
The Item description and price appear on my receipt.
A record is sent to the Stores Inventory Control system.
At the end of a period (day, week) the system will automaticly generate an
order to replenish the inventory.

My Credit Card is swiped.
The Cashier presses a button on the Cash Register.
The sales information is transmitted to a service which approves or rejects
the transaction.
If the Transaction is approved, a receipt is printed and I must sign it.

Sometimes the cashier places the receipt on a pad, and instructs me to sign
on the pad.
This pad is capturing my signature in digital format.

The signed receipt never leaves the merchant.





> reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** robj <robj@pdq.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<756CD20BAF77F8B4.703D8B65BC41663F.6BB027AAF504A47F@lp.airnews.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com> <#iKy#ZLY$GA.297@cpmsnbbsa03> <i0468skn6ha8a34pkc6ibo9rikstctps4k@4ax.com> <u2mw2i2Y$GA.253@cpmsnbbsa02>`

```
e

DennisHarley wrote:

> I had some extra time on my hands.
>
…[43 more quoted lines elided]…
> > reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87hg8s0nkvbh32lc15h58ioecv6nii5r5o@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com> <#iKy#ZLY$GA.297@cpmsnbbsa03> <i0468skn6ha8a34pkc6ibo9rikstctps4k@4ax.com> <u2mw2i2Y$GA.253@cpmsnbbsa02>`

```
"DennisHarley" <LegacyBlue@email.msn.com> wrote:

>I had some extra time on my hands.
>
>I said that things are getting faster, you disagreed.

>> things to me don't look like they are getting faster. you still get
>> all your withdrawals dated today, but deposits tommorrow. all
>> accounting still must be done by hand. and you can no longer hire
>> anyone but experts who have 4 years of college under their belt.

>If all accounting is being done by hand, why am I writing programs to do it?
>Summaries are reviewed after the fact.

you are probably writing programs to handle regulations, or institute
accounting tricks.

>> doing 1 million transactions doesn't help much, if there are human and
>> administrative bottlenecks. you still must sign credit cards. people
…[5 more quoted lines elided]…
>> at the other end, at their leisure.


>When I go into a store to buy something this is what normally happend.

>The cashier scans the UPC.
>The Item description and price appear on my receipt.
>A record is sent to the Stores Inventory Control system.
>At the end of a period (day, week) the system will automaticly generate an
>order to replenish the inventory.

>My Credit Card is swiped.
>The Cashier presses a button on the Cash Register.
>The sales information is transmitted to a service which approves or rejects
>the transaction.
>If the Transaction is approved, a receipt is printed and I must sign it.

>Sometimes the cashier places the receipt on a pad, and instructs me to sign
>on the pad.
>This pad is capturing my signature in digital format.

>The signed receipt never leaves the merchant.

yes, but the time signing and swiping, ect has not changed.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388523CE.D988468D@home.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <c4o28soh02tprl7nkm1riq3bru8egi3bq6@4ax.com> <#iKy#ZLY$GA.297@cpmsnbbsa03>`

```
I agree.  The question isn't really "when".  The need is more for a "new
number generator" interlocked across your whole sysplex that just hands
out new numbers (128 bits should do it) every time it's asked.  

Once we talk about time intervals that are down near the latency of the
network, "clock time" isn't clear at all.  Your site and mine and the
USNO's are <emph>guarenteed</emph> to be out-of-synch -- the theory of
relativity I think.

Sequence, "this came in first, then that" is another thing entirely.


DennisHarley wrote:
> 
> Speed is not the issue, the sequence of events is the issue.
> [SNIP]
```

##### ↳ ↳ Re: Leap Seconds and COBOL

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3880731C.7C3BB74D@zip.com.au>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05>`

```
DennisHarley wrote:
> 
> Support for Leap Seconds is a business decision, not a programming
…[14 more quoted lines elided]…
> be relavent to some applications within some industries.

After reading the threads I would recommend:

1.  Not returning leap seconds at all in the cobol application, if
required the machine could adjust the timeclock back one second and
repeat a second.

2.  If the real timeclock is required then a standard function call
will return the leap seconds.  This will probably not return leap
seconds in 99% of hardware available today, it just is not accurate
enough.  Anyone coding time critical code will enable the function
(may be an atomic clock card on the PC :-}) and program accordingly,
handling a '60' second value.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388125A5.4FA3747A@istar.ca>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au>`

```
If you have OS390 and the high priced time source, it knows about leap
seconds.  The question is what should COBOL time functions do when the
operating system provides leap seconds.  Also how should COBOL
programs behave when they get leap seconds in the data.  For example,
I suspect that CICS will provide leap seconds when asked for the time
(EIBTIME?).  This could also affect SMF record time stamps among other
things (and I have a COBOL program that processes SMF records although
at the moment it only uses the time stamp for sorting and matching). 
Most of the use of main-frame time stamps is for uniqueness or reports
and I haven't seen any COBOL code that is checking time passage where
seconds count.  However that is more due to the data I have dealt
with.  

Clark Morris, CFM Technical Programming Services Inc. cfmtech@istar.ca

Ken Foskey wrote:
> 
> DennisHarley wrote:
…[33 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<On69SP3X$GA.244@cpmsnbbsa05>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au> wrote in message
news:3880731C.7C3BB74D@zip.com.au...
> After reading the threads I would recommend:
>
> 1.  Not returning leap seconds at all in the cobol application, if
> required the machine could adjust the timeclock back one second and
> repeat a second.

I DISAGREE:
This would destroy the true sequence of events.
Freezing the time at 59.999999999999 seconds during the Leap Second event is
the only viable solution I can think of, and it may be unacceptable in some
instances..

>
> 2.  If the real timeclock is required then a standard function call
> will return the leap seconds.

I like the FUNCTION CURRENT-DATE(WITH-LEAP) option.

> This will probably not return leap
> seconds in 99% of hardware available today, it just is not accurate
> enough.

We have to address the future, as well as the present.
If there is a need for it, someone will build it.

> Anyone coding time critical code will enable the function
> (may be an atomic clock card on the PC :-}) and program accordingly,
> handling a '60' second value.

There are probably more viable solutions, such as periodic clock
syncronization.

Again: Applications where this support is needed are probably rare.

>
> Thanks
> Ken Foskey
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85qd7o$fv0$1@nntp3.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05>`

```
FYI, (to comp.lang.cobol)
  The latest "suggestion" that J4 has received input (officially) for is to
add a NEW function
        FUNCTION CURRENT-DATE-UTC

See:
  http://people.ne.mediaone.net/doncobol/00-0184.doc

If you read that paper it does have some interesting thoughts/input.  I am
(personally) unhappy about ACCEPT FROM TIME not getting "updated" - in the
same revision where we FINALLY have ACCEPT FROM DAY/DATE upgraded to accept
4-digit years. (ACCEPT FROM TIME does - currently - get seconds and
hundredths of a second.) If we DO go with a separate intrinsic function, then
I would hope we would also provide new "keywords" to ACCEPT FROM TIME - as we
have for ACCEPT FROM DAY/DATE so that you CAN get "60".

I should also say, that from reading various comp.lang.cobol and J4 notes, I
am convinced that *if* we don't enhance the current features, then we will
need to (explicitly?) require the COBOL system to return seconds=59 and
hundredths=99 for 100 hundredths of a second (or is it 101?) and NOT go
backwards or freeze the program or "mod 100" the hundredths.  All of those
options seem to have WAY too many bad side-effects (IMHO).
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X_2g4.5562$8z5.68953@news4.mia>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net>`

```
William M. Klein wrote:
>
>I should also say, that from reading various comp.lang.cobol and J4 notes, I
…[4 more quoted lines elided]…
>options seem to have WAY too many bad side-effects (IMHO).

To be quite honest, I am amazed that they seriously considered any
option, other than 'freezing' the time for one second, more than 30
seconds.  If they were to change the range of return values, it would
break *lots* of programs, and I mean *lots*.  'Reversing' back one
second would break some programs, though far fewer.  But when you also
consider that probably not one COBOL program in a million (literally!)
would know the difference if the runtime returned the same time for a
whole second, it is truly a no brainer, in my opinion.  If they want
to support another option, then create another function for that.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85qfss$7t6$1@nntp8.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia>`

```
Given how INfrequently a value of "60" would be returned, I still haven't
"internalized" why so many users think that returning a value of "60" would
"break lots of programs".  I am not saying that it won't, I just don't really
understand why so many people think that it would.

Can someone help me understand WHY/WHEN programs would break OTHER than
during the incredibly rare event of a leap-second?  If this is the only time
that a program would be "broken" (and even then the program would have to
BOTH be running on a system that COULD return a leap-second and the program
would have to be accessing one of these features at exactly that second) then
I just don't understand why so many "real users" are so emotionally upset by
this potential enhancement.  I know they are, but I just don't "get it".
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EN3g4.5691$OH3.76997@news3.mia>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net>`

```
William M. Klein wrote:
>Given how INfrequently a value of "60" would be returned, I still haven't
>"internalized" why so many users think that returning a value of "60" would
>"break lots of programs".  I am not saying that it won't, I just don't really
>understand why so many people think that it would.

You don't actually suggest permitting a known bug to remain, even
though it may only be encountered very seldom, do you? ;-)

>Can someone help me understand WHY/WHEN programs would break OTHER than
>during the incredibly rare event of a leap-second?  If this is the only time
…[4 more quoted lines elided]…
>this potential enhancement.  I know they are, but I just don't "get it".

Bill, have you considered just how many time logging programs there
are out there?  Time card punch in/out, data logging of all kinds, etc.
There are literally thousands and thousands of them.  The programs that
process that data must pay close attention to the rollover to the next
minute, because you can't directly add or subtract time values in hours,
minutes and seconds.  You might be surprised how subtle it is to deal
with punch in/out times very close to midnight.  Most of those uses aren't
time critical enough that an extra second makes any difference, but to
permit a value of 60 in the seconds field would be something like a Y2K
for those programs.  If they are doing a histogram or other calculation
using seconds as a subscript, they could blow.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85qjae$r39$1@nntp9.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net> <EN3g4.5691$OH3.76997@news3.mia>`

```
Judson McClendon <judmc@bellsouth.net> wrote in message news:EN3g4.5691
  <snip>
>
> Bill, have you considered just how many time logging programs there
…[9 more quoted lines elided]…
> using seconds as a subscript, they could blow.

I guess I just see it from the opposite side.  If the OS is returning a value
of "60" which some NON-COBOL software is using (producingm manipulating,
expecting, etc), then I think those same programs are going to have MORE
problems if COBOL doesn't return the same value as the rest of the operating
system/enviornment.

Partially, I assume (I know good programmers NEVER assume) that when an
Operating System (or environment) is "enhanced" to produce "60" for leap
seconds that most of its software will be enhanced at the same time.  If
COBOL is defined so that it canNOT do this - but other software can, I see
this producing more problems than any potential "logging" problems that will
occur when "60" is returned and the application isn't upgraded to handle it.

I will report back to the NG what J4 actually does about this during its
meeting from Jan 17 thru Jan 28.  If I had to make a guess, I would say that
they are going to add the "60" value to the existing features, but I am not
particularly postive about this, and I still haven't completely made up my
own mind on how I will vote.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 9)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<upPeYz5X$GA.221@cpmsnbbsa04>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net> <EN3g4.5691$OH3.76997@news3.mia> <85qjae$r39$1@nntp9.atl.mindspring.net>`

```
Please, please, please.
Ensure that we have the OPTION of walking this change in.

We have seen what happens in the real world.
Even though modules exist for Date/Time Validation and Calendar Handling,
some people will hard code their own (incorrect) routines. Without
sophisticated program analysis software, it may be very difficult to
remediate some of these routines.

I agree that this could become another Y2K type endeavor.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:85qjae$r39$1@nntp9.atl.mindspring.net...
> Judson McClendon <judmc@bellsouth.net> wrote in message news:EN3g4.5691
>   <snip>
…[7 more quoted lines elided]…
> > with punch in/out times very close to midnight.  Most of those uses
aren't
> > time critical enough that an extra second makes any difference, but to
> > permit a value of 60 in the seconds field would be something like a Y2K
…[3 more quoted lines elided]…
> I guess I just see it from the opposite side.  If the OS is returning a
value
> of "60" which some NON-COBOL software is using (producingm manipulating,
> expecting, etc), then I think those same programs are going to have MORE
> problems if COBOL doesn't return the same value as the rest of the
operating
> system/enviornment.
>
…[4 more quoted lines elided]…
> this producing more problems than any potential "logging" problems that
will
> occur when "60" is returned and the application isn't upgraded to handle
it.
>
> I will report back to the NG what J4 actually does about this during its
> meeting from Jan 17 thru Jan 28.  If I had to make a guess, I would say
that
> they are going to add the "60" value to the existing features, but I am
not
> particularly postive about this, and I still haven't completely made up my
> own mind on how I will vote.
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85qvcb$sn4$1@aklobs.kc.net.nz>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net> <EN3g4.5691$OH3.76997@news3.mia> <85qjae$r39$1@nntp9.atl.mindspring.net>`

```
: Judson McClendon <judmc@bellsouth.net> wrote in message news:EN3g4.5691
:   <snip>
:>
:> Bill, have you considered just how many time logging programs there
:> are out there?  Time card punch in/out, data logging of all kinds, etc.
:> There are literally thousands and thousands of them.  The programs that
:> process that data must pay close attention to the rollover to the next
:> minute, because you can't directly add or subtract time values in hours,
:> minutes and seconds.  

So the program converts it to ... ( hr * 3600 ) + ( min * 60 ) + sec
and winds up as if the next minute had started.  This hardly seems
a problem.

:> You might be surprised how subtle it is to deal
:> with punch in/out times very close to midnight.

Well do go on and explain and surprise us.  It is just another 
time.  Obviously if an hour of 24 is returned then it is in the
next day and this will need normalisation.

:>  Most of those uses aren't
:> time critical enough that an extra second makes any difference, but to
:> permit a value of 60 in the seconds field would be something like a Y2K
:> for those programs.  

Nothing like, actually.


:> If they are doing a histogram or other calculation
:> using seconds as a subscript, they could blow.

Of course, but can you think of _any_ real application where this
would be done just on 0-59 seconds ?A
A
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 8)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64o28ss0agbnj5005acqlgpr0kltsml3to@4ax.com>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net> <EN3g4.5691$OH3.76997@news3.mia>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:

>Bill, have you considered just how many time logging programs there
>are out there?  Time card punch in/out, data logging of all kinds, etc.
…[3 more quoted lines elided]…
>minutes and seconds.

when i worked with time-punch cards, they would add up the minutes and
round to the nearest 15 (which i had to argue with sometimes). instead
of adding a leap second into the code, perhaps they could get rid of
petty managers.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 7)_

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-NzlQO4fddJDn@localhost>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net>`

```
On Sun, 15 Jan 3900 13:57:26, "William M. Klein" 
<wmklein@nospam.netcom.com> wrote:

> Given how INfrequently a value of "60" would be returned, I still haven't
> "internalized" why so many users think that returning a value of "60" would
> "break lots of programs".  I am not saying that it won't, I just don't really
> understand why so many people think that it would.
> 

Let me make you a deal<G>.  I'll show you some code that will break if
you tell me how in the world the computer is going to know when a leap
second is required, and when to set the seconds to 60 (if that is the 
ultimate solution).

Understand what I'm asking.  Let's say this existed today.  Now next 
month whoever the powers that be are decide that at the end of 2000 an
extra leap second will be required.

Now, three years hence they decide to take it back.

How in the world will the COBOL compiler know that?  The entire thing 
seems like a non issue to me.  We've had leap seconds for a long time 
and it;'s not caused any COBOL grief as far as I am aware.

However, returning a value of 60 WILL cause me some grief in programs 
that create a future time based on current returned time.  It's the 
base 60 math that will become busted.

-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86u1a0$6rl$1@nntp5.atl.mindspring.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <X_2g4.5562$8z5.68953@news4.mia> <85qfss$7t6$1@nntp8.atl.mindspring.net> <Jl0PnHJ5PvPd-pn2-NzlQO4fddJDn@localhost>`

```
OK folks - so here is what ACTUALLY happened at the J4 meeting about leap
seconds. (Remember EVERYTHING is still subject to change, but my guess is
that this PROBABLY will stay until this revision actually becomes official).

1) ACCEPT FROM TIME, FUNCTION WHEN-COMPILED and FUNCTION CURRENT-DATE were
"returned" to allowing a maximum of 59 in the seconds portion of the returned
value.

2) A "new directive" is being added:

   >>DIR LEAP-SECOND ON/OFF

which will *default* to "Off".  When it is explicitly coded as "ON" (i.e. you
must create new code or CHANGE existing code), then *if* the implementor has
the ability, they MAY (are permitted) to return a value greater than 59.  (J4
didn't limit it to 60 - because there is some thought at the "international
time" level of putting leap-seconds more infrequently - but more than one at
a time).

  ***

Interesting note:
 When looking at the actual wording of the '85 Standard (with the '89
Intrinsic Function amendment) - it is true that the two intrinsic functions
are limited to ONLY reporting seconds up to "59".
   HOWEVER,  the ACCEPT FROM TIME has a rule that says that the maximum value
(in hhmmsshh format) is 23595999.  UNFORTUNATELY, there is no rule that says
that you can't have "60" in the seconds portion of any hour/minute except
"23:59". Therefore, THEORETICALLY, the '85 (and probably even the '74)
Standard allows a value of
    22:59:61:99  (hh:mm:ss:hh)

Having said that, we (J4) don't think any vendor actually ever did this. !!!
<G>
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000116160605.18031.00000846@ng-ft1.aol.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia>`

```
>  But when you also
>consider that probably not one COBOL program in a million (literally!)
>would know the difference if the runtime returned the same time for a
>whole second, it is truly a no

EXCUSE ME!!  I know of, and personally worked on dozens of COBOL programs using
transaction time-stamps where "freezing" for an entire second would corrupt
several dozen to several hundred transaction records. Time functions return
small fractions of seconds for very real reasons!  And, in an OS/390
environment, with CICS or ENCINA or IMB DB/DC transaction logs, is one of the
most critical.  Or, is the committee to simply say to IBM and Hitachi and the
others, "Oh well, deal with it yourself, we are not going to put it in the
standard!"  I suspect we would not like the results!
Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FCFg4.297$FS5.3160@news3.mia>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com>`

```
Steve Newton wrote:
>>  But when you also
>>consider that probably not one COBOL program in a million (literally!)
…[10 more quoted lines elided]…
>standard!"  I suspect we would not like the results!

I have spent most of my career on mainframe systems myself, though not
in IBM shops (except for the IBM 1401 in my early days).  I have also
written the underlying system software that supports online database
recovery, in both communications and database system software, and in
applications, of course.  And I know that if you are depending entirely
on HH:MM:SS.th for transaction tracking and identification, you are in
trouble.  Many mainframes can perform more than a hundred transactions
per second, and certainly can receive many more than 100 transaction
requests per second.  If your mainframe COBOL only provides time down
to the 100th of a second, you are going to have to add another field,
say a serial number, after the time (or instead of the time) to permit
unique transaction identification in any case.  Time to the 100th of a
second is simply not sufficient for a unique identifier, right now.
Since you already must allow for multiple transactions per 100th of a
second, then what difference does it make if there are say 200 of them?
If you are using another timer, say a counter register of milliseconds
or microseconds since midnight, there is not necessarily a reason to
make that counter adjust for leap seconds, because it will automatically
reset and correct itself at the next midnight.  If you don't already
allow for more than 100 transactions a second, then what are you going
to do when the mainframe gets fast enough to perform 1,000 transactions
a second, or 10,000?
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 8)_

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dVGg4.340$x3.572@wormhole.dimensional.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia>`

```

"Judson McClendon" <judmc@bellsouth.net> wrote in message
news:FCFg4.297$FS5.3160@news3.mia...
...
> allow for more than 100 transactions a second, then what are you going
> to do when the mainframe gets fast enough to perform 1,000 transactions
> a second, or 10,000?
...

Hi Judson, long time no see!

We have some transactions in our shop that flow through in the 3000-5000
range per second already.  Most, however, are in the 300 or so a second
ballpark.  An online transaction that takes more than 1/2 second CPU is rare
in systems with performance contracts.  Even in the worst case there are as
many as 12 processors driving an indeterminate number of online regions to
keep throughput up.  For all that, a mainframe is really just like a big PC,
most people don't realize how big <g>.

Glenn
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 8)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:

>If your mainframe COBOL only provides time down
>to the 100th of a second, you are going to have to add another field,
>say a serial number, after the time (or instead of the time) to permit
>unique transaction identification in any case.

why would they provide the time down to 100th of a second? no one can
respond that fast.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fuLh4.10823$wk.130516@news1.mia>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com>`

```
G Moore wrote:
>"Judson McClendon wrote:
>>
…[6 more quoted lines elided]…
>respond that fast.

The COBOL 85 standard FUNCTION CURRENT-DATE provides time to the
100th of a second.  If you are logging transactions from 5000 users,
you certainly can receive more than 100 transactions per second. :-)
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 10)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:

>G Moore wrote:
>>why would they provide the time down to 100th of a second? no one can
>>respond that fast.

>The COBOL 85 standard FUNCTION CURRENT-DATE provides time to the
>100th of a second.  If you are logging transactions from 5000 users,
>you certainly can receive more than 100 transactions per second. :-)

yes, but no one responds that fast, and no one changes their account
that fast either.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 11)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86cja8$48m$1@news.inet.tele.dk>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia> <g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com>`

```
Hey, what's up doc.
We must be talking about an application with transaction logging on the
server only - a client/server application. In that case you can let the
program check if the time is unique, and if not you'll have to make a new
function call.

It you are talking about distributed computing - forget the nice theory.
First of all, the clock will be different on 5000 users, and you'll never
know when they press Enter - 50 of them could do it at the same time.

Regards
Ib

G Moore skrev i meddelelsen ...
>"Judson McClendon" <judmc@bellsouth.net> wrote:
>
…[12 more quoted lines elided]…
>reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 12)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p2uk8ssgppe652p306k96f23i8lfsrkh9v@4ax.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia> <g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com> <86cja8$48m$1@news.inet.tele.dk>`

```
"Ib Tanding" <ib@tanding.dk> wrote:

>Hey, what's up doc.
>We must be talking about an application with transaction logging on the
>server only - a client/server application. In that case you can let the
>program check if the time is unique, and if not you'll have to make a new
>function call.

but what could be the possible reason for having transactions
accounted for in centi-seconds? for testing purposes?

>>>The COBOL 85 standard FUNCTION CURRENT-DATE provides time to the
>>>100th of a second.  If you are logging transactions from 5000 users,
>>>you certainly can receive more than 100 transactions per second. :-)

>>yes, but no one responds that fast, and no one changes their account
>>that fast either.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 13)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86f810$re4$1@news.inet.tele.dk>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia> <g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com> <86cja8$48m$1@news.inet.tele.dk> <p2uk8ssgppe652p306k96f23i8lfsrkh9v@4ax.com>`

```
It was your idea - not mine. Nothing in my statement indicates anything
about test. What I am saying is very simple. You cannot use any flavour of
timestamp in a PC environment unless the action is done on the server in a
program controlled process. Any other design will be 'freakware'.

Regards
Ib

G Moore skrev i meddelelsen ...
>"Ib Tanding" <ib@tanding.dk> wrote:
>
…[17 more quoted lines elided]…
>reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 11)_

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388A87A4.1475930D@acm.org>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia> <g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com>`

```

G Moore wrote:
> "Judson McClendon" <judmc@bellsouth.net> wrote:
> 
…[9 more quoted lines elided]…
> that fast either.

You are thinking in PC, single-user mode.  The other responders are
talking about multi-user application systems concurrently supporting
1000's of users accessing some shared data base.  In such systems the
transaction activity of single individuals is insignificant compared to
the aggregate transaction arrival rate from all users.  The issue is not
one of timing individual user's transactions to greater precision, but
rather one of having time stamps that can uniquely identify the time
order of actions done in response to 100's of transactions per second
arriving from 1000's of users.

It is not that common in such large applications to have cases where you
need a unique value associated with actions performed for each handled
transaction (for example, to guarantee uniqueness in an index column in
each row of a relational database), and in some cases there is also a
requirement that this unique value be monotone increasing with time.  In
the past, the cheapest, simplest way do this may have been to use a
clock value, but increases in processor speed without comparable
increases in clock resolution are causing these techniques to break. 
One could argue for a better long-range approach, but the cheapest
short-term fix may be to increase clock resolution.

This approach may not work well in distributed systems where there are
limits to the precision of clock synchronization, but it can work
extremely well in the mainframe and mainframe-sysplex environments where
all processors share a common hardware timebase.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 12)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com>`
- **References:** `<X_2g4.5562$8z5.68953@news4.mia> <20000116160605.18031.00000846@ng-ft1.aol.com> <FCFg4.297$FS5.3160@news3.mia> <ta588so9lrj7i62phfik2muq2ik7eu9er3@4ax.com> <fuLh4.10823$wk.130516@news1.mia> <g5hg8sgfeo5m07nl2qak51gcle5bsgb20v@4ax.com> <388A87A4.1475930D@acm.org>`

```
"Joel C. Ewing" <jcewing@acm.org> wrote:

>> yes, but no one responds that fast, and no one changes their account
>> that fast either.

>It is not that common in such large applications to have cases where you
>need a unique value associated with actions performed for each handled
…[7 more quoted lines elided]…
>short-term fix may be to increase clock resolution.

ahh, i see. we are talking *maintenance* of old code which used the
time function as a key, and they haven't changed the indexed files
over to duplicate keys, and some of the code also doesn't use record
locks, but instead the key as a method of determining priority, 

and.... it's theoretically possible some of the big accounts *do* have
multiple transactions on them... and they must show the transaction
deposits match withdrawal times.

yes, i would argue for a better long-range approach. of course,
de-regulating the code wouldn't change much, as they would only 'fix'
the code which would represent a profit.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 13)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000125035025.07131.00000179@ng-ck1.aol.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com>`

```
G Moore gvwmoore@spam.ix.netcom.com 
Date: Sun, 23 Jan 2000 14:40:00 -0500

seems to be minimizing a few categories of challenge with phrasing such as

.. snips

<<
 i see. we are talking *maintenance* of old code which used the
time function as a key, and they haven't changed the indexed files
over to duplicate keys, and some of the code also doesn't use record
locks, but instead the key as a method of determining priority, 

and.... it's theoretically possible some of the big accounts *do* have
multiple transactions on them... and they must show the transaction
deposits match withdrawal times.

>>

I hope I have quoted enough. I don't mean to distort. But these time stamp
problems are not old-lander dummy legacy code. And the requirements are not
restricted to collisions on big accounts in a data file.

The problem more generally is that wherever you have activity, it is precisely
there that your are likely to have other activity. Take a single credit card
account.  Two pieces of plastic with the same number, one for Mom, one for Pop.
They both go to the Mall at the same time; but one goes to the clothes store,
the other to the sports store. 

It could be a small account. Maybe two transactions a quarter! The transactions
can collide, easily.  Furthermore, some system designs fracture processing
activity into distinct transactions that are handled asynchronously. These
spawned tasks can easily come back together in competition for the same
resource.

Financial applications frequently log absolutely everything. A single
transaction frequently causes multiple log actions. It does get hairy when
multiple transactions enter a system and commence to generate a list of
loggable activities.  If you rely on a single clock access to stamp these, then
a low precision can make things collide immediately.  If you try to extend the
unique field with a mechanical iterator, then one iterator can overrun the
others early numbers if you are not going back to the clock.

The modern systems are extremely fast. Surprisingly, the worst case scenerios
can sometimes happen in the best case execution contexts.

 When systems are _not_ busy you can have _more_ challenges. The stress testing
mentioned by some posters, and the remarkable real world transaction rates in
production environments mentioned by others are situations where multiple
accesses to the clock actually tend to resolve problems because the clock will
(on average) tend to tick for you between each access, because in a
multi-tasking system you get swapped out more often (statistically speaking).

Under light load, monsterous apparent steady state can come from the clock,
because nothing is slowing you down!

The clock resolution problem is getting worse in mainframe environments. To
some extent the movement of the keystroke processing to desktop technology has
generally freed the mainframes to concentrate on insisting that the backplane
deliver a steady flow of resources for individual less frequently interrupted
tasks. A unit of work on a mainframe is increasingly likely to get to the next
request to the TOD device without delay.

Superscalar technology, whether apparent in the architected programmer
interface of the machine or not, actually also increases the chance that clock
request will happen sooner in the instruction stream. Although so far TODs seem
to be special resources that have single threaded access. Distinct portions of
code can execute in parallel now.
So the effective time between needs is reduced. This will be especially true as
we get thread level parallelism, rather than just the simple taks level
parallelism possible in SMP.

When you step back from it you see that often the time stamp is just a unique
value generator in the resource collision situations. Whatever the device that
is used to do it will need increasing resolution as time goes on.

Incidentally, most of the systems that are trying to mediate these collisions
_are_ using record locks; they are most assuredly in update mode. The unique
keys are a way to avoid locking the same records. 

Best Wishes,












Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 14)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com>`

```
rkrayhawk@aol.com (RKRayhawk) wrote:

>G Moore gvwmoore@spam.ix.netcom.com 

><<
> i see. we are talking *maintenance* of old code which used the
…[6 more quoted lines elided]…
>deposits match withdrawal times.

>>>

>I hope I have quoted enough. I don't mean to distort. But these time stamp
>problems are not old-lander dummy legacy code. And the requirements are not
>restricted to collisions on big accounts in a data file.

>The problem more generally is that wherever you have activity, it is precisely
>there that your are likely to have other activity. Take a single credit card
>account.  Two pieces of plastic with the same number, one for Mom, one for Pop.
>They both go to the Mall at the same time; but one goes to the clothes store,
>the other to the sports store. 

>It could be a small account. Maybe two transactions a quarter! The transactions
>can collide, easily.  Furthermore, some system designs fracture processing
>activity into distinct transactions that are handled asynchronously. These
>spawned tasks can easily come back together in competition for the same
>resource.



>Financial applications frequently log absolutely everything. A single
>transaction frequently causes multiple log actions. It does get hairy when
…[4 more quoted lines elided]…
>others early numbers if you are not going back to the clock.

it makes me wonder why use a unique field in the first place. use
duplicates, and the greater field goes to the right branch (or the
lesser to the left).

>The modern systems are extremely fast. Surprisingly, the worst case scenerios
>can sometimes happen in the best case execution contexts.


> When systems are _not_ busy you can have _more_ challenges. The stress testing
>mentioned by some posters, and the remarkable real world transaction rates in
…[3 more quoted lines elided]…
>multi-tasking system you get swapped out more often (statistically speaking).

hmm. translation: when you switch tasks, the time between the switch
generally exceeds a clock tick?

>Under light load, monsterous apparent steady state can come from the clock,
>because nothing is slowing you down!

translation: when you have fewer accesses, the clock ticks have a
greater chance of having the same tick.

>The clock resolution problem is getting worse in mainframe environments. To
>some extent the movement of the keystroke processing to desktop technology has
…[3 more quoted lines elided]…
>request to the TOD device without delay.

>Superscalar technology, whether apparent in the architected programmer
>interface of the machine or not, actually also increases the chance that clock
>request will happen sooner in the instruction stream. Although so far TODs seem
>to be special resources that have single threaded access. Distinct portions of
>code can execute in parallel now.

translation: because there are multiple cpus, they can run the tasks
at the same time, decreasing the chance of a unique tick all the more.

>So the effective time between needs is reduced. This will be especially true as
>we get thread level parallelism, rather than just the simple taks level
>parallelism possible in SMP.

>When you step back from it you see that often the time stamp is just a unique
>value generator in the resource collision situations. Whatever the device that
>is used to do it will need increasing resolution as time goes on.

ahh. so the *time* stamp is a process id.

>Incidentally, most of the systems that are trying to mediate these collisions
>_are_ using record locks; they are most assuredly in update mode. The unique
>keys are a way to avoid locking the same records. 

i'd hope most of the code, if not all, was moved towards locks if
possible.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 15)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388F0520.45B58AC1@NOSPAMwebaccess.net>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com>`

```
G Moore wrote:
> 
> it makes me wonder why use a unique field in the first place. use
> duplicates, and the greater field goes to the right branch (or the
> lesser to the left).

From an IDMS environment, I have been wondering that throughout this
thread.  We store data by keys with DUPLICATES NEXT, PRIOR, or NOT
ALLOWED.  I have bee wondering why in any access method one would need
to have a unique time-date-stamp key.

But it appears that the issue is that one record with a later
time-date-stamp will be entered before another record with an earlier
time-date-stamp, because the clock has been reset.  I still think that
the solution should be a business solution rather than a technological
solution.  Figure out why this matters and solve it the same way people
have been handling it forever where priority has been an issue with
clerks writing in the time by hand!
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 16)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net>`

```
Howard Brazee <brazee@NOSPAMwebaccess.net> wrote:

>But it appears that the issue is that one record with a later
>time-date-stamp will be entered before another record with an earlier
>time-date-stamp, because the clock has been reset.

if the clock is reset, then is the time stamp valid period? or do no
records get stamped at that time?



reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B8kk4.16789$ln.1163231@news4.mia>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com>`

```
G Moore wrote:
>Howard Brazee wrote:
>>
…[5 more quoted lines elided]…
>records get stamped at that time?

In the systems I am familiar with, the date/time stamp has little to
do with processing sequence in real-time, because that is established
by queuing sequence and priority.  It is when doing reprocessing of
transactions during database recovery that transaction sequence is
paramount.  For this purpose, a time stamp with only a hundredth of
a second is insufficient; some other or additional method must be
used.  So, my contention is that, since time to the hundredth of a
second is insufficient already, what difference would it make if the
time function returned the exact same time for a whole second?  Once
you build the capability to correctly process multiple transactions
with the apparent exact same time (because they happened in the same
hundredth of a second), then a larger number of transactions, also
with the exact same time (because that hundredth of a second was
extended by the clock for a whole leap second), would seem to be a
non issue.  That's why I think simply 'freezing' the clock for a whole
leap second is the best way to go.  If somebody has specific examples
where a hundredth of a second is sufficient, but holding that same
hundredth of a second for a whole second would fail, I would love to
hear about it. :-)
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 18)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:

>>if the clock is reset, then is the time stamp valid period? or do no
>>records get stamped at that time?

>In the systems I am familiar with, the date/time stamp has little to
>do with processing sequence in real-time, because that is established
>by queuing sequence and priority.  It is when doing reprocessing of
>transactions during database recovery that transaction sequence is
>paramount.

hmm. wouldn't it be better to save the priority... err, no. that would
add code.

  For this purpose, a time stamp with only a hundredth of
>a second is insufficient; some other or additional method must be
>used.

i suppose on machines which really do have two transactions on the
same account, (and since writing one set of code is easier than two,
except in the case where you can make a profit) would require a
smaller tick, and i'll agree that having a smaller time stamp would be
good for compilers in those cases.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
usenet has been down for awhile... switching audio card
```

###### ↳ ↳ ↳ Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 19)_

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B5F0E6.A737CF55@home.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com>`

```
A very basic question:  what is the significance of Friday, 14 October
1582 that it should be "day 1" of the Lillian day count?  It sounds about
right for the introduction of the Gregorian calendar - presumably in Rome
since the English speaking countries didn't adopt it until 17-something
and the Orthodox world has never completely adopted it.  Going further
east, of course, Buddhist countries didn't have any "Year 2000" excitement
either.  Whichever - it's a pretty parochial scheme. ;-)
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 20)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38b5f6f3_2@news3.prserv.net>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com>`

```

David A. Cobb <superbiskit@home.com> wrote in message
news:38B5F0E6.A737CF55@home.com...
> A very basic question:  what is the significance of Friday, 14 October
> 1582 that it should be "day 1" of the Lillian day count?  It sounds about
> right for the introduction of the Gregorian calendar

 History of the Calendar
The history of the calendar is fascinating.  The year of a planet is the
time it takes to orbit the Sun.  There are, however, different types of
year.  The time it takes the Earth to make one complete revolution with
respect to the distant stars is called the sidereal year (deriving from the
Latin word sidus, which meant constella-tion).  The sidereal year  (for
1950) is equal to 365.25636566 days or 31,558,149.993 seconds.
The time it takes for the Earth to return to the same point in its seasonal
cycle (which is what counts as far as the calendar is concerned) is called
the tropical year (after the Greek verb trepein, which means to turn).  The
tropical year is equal to 365.24219342 days or 31,556,925.511 seconds being
about 20 m 25 s shorter than the sidereal year.  The modern definition of a
second is the duration of 9,192,631,770 cycles of the radiation emitted by
the transition between the two hyperfine levels of the ground state of the
133Cs atom.
The tropical year is shorter than the sidereal year because of the
precession of the Earth's axis.  Precession is the motion of the axis of a
spinning top.  The Earth, like a top, has an equatorial bulge caused by the
centrifugal force of its rotation - the equatorial radius is 21.360 km
longer than the polar radius.  This bulge experiences a torque applied by
the gravitational influence of the Moon, the Sun, and the planets.  The
result is a precessional motion of the Earth's axis.  This was discovered by
Hipparchos about 150 BC.
The astronomical motions of the Earth and the Moon provide the basis for the
calendar - the subdivision of time into years, months, weeks, and days.  The
problem with these subdivisions is that they are based on phenomena that
have different periods - the revolution of the Earth around the Sun, the
revolution of the Moon around the Earth, and the rotation of the Earth.  The
periods are not commensurate: there are about 29.53 days in a lunar month,
4.22 weeks in a lunar month, and 365.24 days in a tropical year.  The
development of an accurate calendar has been a vexing problem since
antiquity (the name calendar derives from the Latin name kalendae for the
day of the new Moon, marking the beginning of the lunar month).
The Egyptians started their year in the latter part of July, when the Nile
began flooding the delta.  This was a big event, because the flooding
fertilized the delta.  The Egyptians divided the year into 12 months of 30
days each, giving a total of 360 days, to which they added an extra 5 days
at the end.  In the years around 4241 BC, the Egyptians noticed that the
rising of the Nile coincided with the day when the star Sirius (known as
Sothis) became again visible in the southern sky as seen from the capital
city of Memphis.
The Roman author Censorinus reported in his work De die natali (written in
238 AD and dedicated to his patron on his birthday) that in 139 AD the
rising of Sothis had occurred on July 20.  Now, the Egyptian year of 365
days was shorter by 0.242 day than the tropical year.  As a result, the
Egyptian calendar fell behind by 1 day in 4 years, making one full circle
(called the Sothis cycle) in 4x365 = 1,460 years.  Because the rising of
Sirius at Memphis and the beginning of flooding of the delta coincide only
once in 1,460 years, the Egyptians must have developed their calendar at one
of the following times: 1460 - 139 = 1321 BC, or 1321 + 1460 = 2781 BC, or
2781 + 1460 = 4241 BC...  This last date is the most probable, because the
calendar was already in use about 3000 BC.
The early Greeks adopted the Egyptian calendar, but in the fifth century BC,
the oktaeteris was introduced, a period of 8 years in which each year
consisted of 6 lunar months of 30 days and 6 lunar months of 29 days, plus 1
lunar month of 30 days in 3 out of the 8 years.  The total number of days
was thus 2,922, giving an average of exactly 365.25 days per year.  The
Greeks set the beginning of the year at either the summer or winter solstice
(depending on which Greek city).
According to legend, Rome was founded by Romulus, its first king, on April
21, 753 BC.  At that time, the Romans had a calendar of 10 months (Martius
after Mars, the god of war, Aprilis, after Apru, the Etruscian goddess of
love, Maius, after Maia, eldest daughter of At-las, Junius, after Juno, wife
of Jupiter, Quin-tilis, Sextilis, September, October, November, and
December, the fifth month through the tenth month, of which four had 31 days
and the other six had 30 days.  In addition, there were two unnamed months
each in the winter.
The second king of Rome, Numa Pompilius (715-672 BC), is said to have named
the two winter months Ianuarius, after Janus, the two-faced god of gates,
and Febriarius, after Februa, the day of purification (the 15th) and to have
moved the beginning of the year to January 1.  In the reform recommended by
the Alexandrine astronomer Sosigenes and promulgated by Julius Caesar (100 -
44 BC), the year remained equal to 365.25 days, by having 365 days per year,
but adding to the month of February one day every fourth year (the leap
year).  In addition, the names Quintilis and Sextilis were changed to July
and August to honour Julius Caesar and his adopted son Augustus, and both
given a length of 31 days, together with December which also got 31 days.
Poor February was used as a source for extra days.  The first Julian year
began on January 1, 709 AUC (Ab Urbe Condita, i.e. since the founding of the
City), which translates into January 1, 45 BC.
In 526 AD, the Byzantine emperor Justinian asked a monk named Dionysius
Exiguus to change the calendar, reckoning time no longer from the founding
of Rome, but from the birth of Jesus Christ.  Dionysius figured that Jesus
had been born 753 years after the founding of Rome, apparently not knowing
that Herod, under whom Jesus was born, had died 749 years AUC.  Accordingly,
Jesus had to be born at least four years earlier than the good monk thought.
This error was discovered long after the Justinian Calendar had been adopted
by all the Christian nations of Europe.
To complicate things, some recent research indicates that Jesus Christ was
crucified on April 3, 33 AD.  Because He was 33 years old when He died, His
birth could be fixed at the end of the year 1 BC or at the beginning of the
year 1 AD (there is no year zero), four years after Herod had died.  At this
point we notice that there are discrepancies among the four gospels.  Most
important, the earliest gospel, Mark, says nothing about the birth of Christ
or about Herod, and neither does John.  It is thus possible that Dionysius
Exiguus made no mistake after all and that the birth of Christ took place at
the beginning of year 1, after the death of Herod.  In any case, we still
reckon the years from the fix provided by Dionysius Exiguus.  May his soul
rest in peace.
The number of days in a tropical year, as fixed by Julius Caesar's reform is
not quite exact - it is too large by 0.0078 days = 11.23 minutes.  By the
middle of the sixteenth century, the calendar was off by 11.7 days with
respect to the seasons.  Pope Gregory XIII ordered that the day after
Thursday, October 4, 1582, should be henceforth Friday, October 15, 1582; in
addition, from that year on, centennial years should not be leap years, even
though divisible by 4, unless divisible by 400.  In a 400-year cycle,
therefore, there would be (365x400) + 97 = 146097 days, equal to 365.242
days per year.
The Gregorian calendar was not the work of Gregory XIII (just as the Julian
calendar was not the work of Julius Caesar), but of the Jesuit priest
Christopher Clavius (after whom a prominent crater on the Moon is named) and
the Neapolitan astronomer and physician Luigi Lillio Ghiraldi.  The new
calendar was soon adopted in all Catholic countries, but only in 1752 in
England and the British Empire (by which time they were 12 days behind), and
only in 1918 in Russia, when that country was 13 days behind - which is why
the October Revolution was celebrated in November.  Lillian days, named
after Luigi Lillio, are simply days counted from the start of the Gregorian
reform.
In the same year, 1582, that Pope Gregory XIII promulgated his reform of the
calendar, the scholar Joseph Scaliger (1540-1609) devised the Julian period,
which he named after his father, Julius Caesar Scaliger.  The Julian period
is a period of 7,980 years that is obtained by multiplying three cycles, the
solar (28y), Metonic (19y), and indictio (15y) cycles: 28x19x15 = 7,980.
The solar cycle is a period of 28 years that derives from the fact that in
365 days there are 52 weeks + 1/7 of a week.  In successive years,
therefore, the same day of the year will fall on the following day of the
week.  Were it not for leap years, in which the day of the week advances by
two, the cycle would be completed in 7 years.  It is instead completed in
7x4 = 28 years.  The Metonic cycle (discovered by the Greek astronomer Meton
in the fifth century BC) is a period of time that is divisible into both a
whole number of years and a whole number of lunar months; it is equal to 19
years and includes 235 lunar months.  The indictio cycle is an ancient
Egyptian cycle, that beginning with January 1, 313 AD, was adopted by the
emperor Constantine as the Roman taxation cycle.
Scaliger adopted the three cycles not for astronomical reasons, but because
they were already used in Hellenistic, Roman, and Byzantine calendars.
Scaliger set the begin-ning of the current Julian period at January 1 at
12:00 noon Greenwich time, 4713 BC.  Reck-oning from noon is advantageous in
astronomy because most astronomical observations are made at night, meaning
that the observations from one night are not divided into separate days (at
least in Europe).  Days are counted in continuity from that date.  The
Julian period is important, because astronomers, even today, use it to
record the dates of celestial phenom-ena.  Thus January 1, 2000, at 00:00h,
will be Julian date (JD) 2,451,544.50.  Often the term Julian day is used to
mean the day count within a given year.  This is a confusing prac-tice, that
unfortunately has taken root, and is here to stay.
The seven day week dates from antiquity - it appears in Genesis, for
instance.  It may have originated from the observation that the lunar cycle,
29.5 days long, exhibits four phases - new Moon, half Moon, full Moon, half
Moon.  Each phase, therefore, lasting about 7 days.  In fact, in many
languages the word for week derives from the word for seven (e.g. ebdomaz in
Greek, septimana in Latin).  Noticing, in addition, that there were seven
heavenly bodies, the ancients related each body to a day of the week: Sun
for Sunday, Moon for Monday, Mars for Tuesday (dies Marties in Latin) where
the Norse god Tir takes the place of Mars in the Germanic languages, Mercury
for Wednesday (dies Mercurii), and so on.
A lot of the history of the calendar can be found back in the various
constants and algorithms used by CALRPK.

http://www.etk.com/download/etkpak/etkpak.htm#CALRPK
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 20)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<894uof$1o8s$1@newssvr04-int.news.prodigy.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com>`

```

David A. Cobb <superbiskit@home.com> wrote in message
news:38B5F0E6.A737CF55@home.com...
> A very basic question:  what is the significance of Friday, 14 October
> 1582 that it should be "day 1" of the Lillian day count?  It sounds about
…[4 more quoted lines elided]…
> either.  Whichever - it's a pretty parochial scheme. ;-)


By 1582, the Spring Equinox fell on Mar. 11 (10 days slow), so Pope Gregory
XIII established  "NS" calendar.  Luigi Lilio proposed the new calendar.
Thu., Oct. 4 was followed by Fri., Oct. 15.  That makes Oct. 15, 1582 day 1
of the Lilian day count.  England & the colonies made up for the 11 days
difference in 1752 and Wed., Sep. 2 followed by Thu., Sep 14 that year.  By
the year 3200, the calendar is estimated to be 1 full day "slow" again.  I
don't plan on being around to see if they decide to "skip" a leap day or
what. :)
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 21)_

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B615A0.4E5605B9@acm.org>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com> <894uof$1o8s$1@newssvr04-int.news.prodigy.com>`

```


Terry Heinze wrote:
...
> By 1582, the Spring Equinox fell on Mar. 11 (10 days slow), so Pope Gregory
> XIII established  "NS" calendar.  Luigi Lilio proposed the new calendar.
…[5 more quoted lines elided]…
> what. :)

Actually 3200 is approximately the point (the closest multiple of 400
years) where the error will exceed 0.5 days and hence be time for a one
day jump to keep the calendar rounded to the nearest day.  The error is
approximately 1 day in 3200 years or 0.5 day in 1600 years and things
were in sync after the correction in 1582 (approximately 1600).
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 21)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B69DAF.6A53D04F@cusys.edu>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com> <894uof$1o8s$1@newssvr04-int.news.prodigy.com>`

```
Terry Heinze wrote:

>  By
> the year 3200, the calendar is estimated to be 1 full day "slow" again.  I
> don't plan on being around to see if they decide to "skip" a leap day or
> what. :)

Go ahead and plan on being around.  At least do what you can to make sure the
world's still around and a good place to live.  If you happen to die, the world
you helped mold will still be here.
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8957le$iup$1@slb0.atl.mindspring.net>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com>`

```
Although not asked in this thread, I thought I would repeat (?) why COBOL
uses Jan 1, 1601 for INTEGER-OF-DAY/DATE - instead of the "correct" Lillian
date.  This is because that was a SUNDAY - and therefore, the remainder when
dividing INTEGER-OF-DATE/DAY by 7 gives you the same number as ACCEPT FROM
DAY-OF-WEEK (with the minor problem of 7 versus 0)

Also, for the IBM mainframers among you, LE does use the "true" Lillian date,
but there is an option to "switch" to a COBOL-compatible number.
```

###### ↳ ↳ ↳ Re: Lillian Date Question (Was: Leap Seconds and COBOL)

_(reply depth: 21)_

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B74F6F.13813681@home.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <h6hr8s0nrib4o56qm0ctiuhh45csmbiso4@4ax.com> <388F0520.45B58AC1@NOSPAMwebaccess.net> <1r4v8s49aqv044ooq0sreclpoahf7sapvm@4ax.com> <B8kk4.16789$ln.1163231@news4.mia> <j6qh9s077l1uau1covtv8hdi27r90dgu39@4ax.com> <38B5F0E6.A737CF55@home.com> <8957le$iup$1@slb0.atl.mindspring.net>`

```
"William M. Klein" wrote:

> Although not asked in this thread, I thought I would repeat (?) why COBOL
> uses Jan 1, 1601 for INTEGER-OF-DAY/DATE - instead of the "correct" Lillian
> date.  This is because that was a SUNDAY - and therefore, the remainder when
> dividing INTEGER-OF-DATE/DAY by 7 gives you the same number as ACCEPT FROM
> DAY-OF-WEEK (with the minor problem of 7 versus 0)

And I thought it was just ease of calculation (1601 would mark the first year of
a 400 year epoch or cycle for leap year calculations.)

>
>
> Also, for the IBM mainframers among you, LE does use the "true" Lillian date,
> but there is an option to "switch" to a COBOL-compatible number.
>

I'm one myself which is how I came to ask the question.

Thank you, all.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 14)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86lknk$8of$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com>`

```
    I have not tried this on a wide variety of systems, but on
at least one pc, running either DOS or Win95/98, I found that
the system clock would not return every tick in the hundredths field,
but would update itself only (I assume) 18.2 times a second.




 .. snips
>
> <<
…[10 more quoted lines elided]…
>

<snip>
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k4Dj4.29616$wk.516728@news1.mia>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <86lknk$8of$1@ssauraab-i-1.production.compuserve.com>`

```
Russell Styles wrote:
>    I have not tried this on a wide variety of systems, but on
>at least one pc, running either DOS or Win95/98, I found that
>the system clock would not return every tick in the hundredths field,
>but would update itself only (I assume) 18.2 times a second.

This is correct.  It is a holdover and one of the deficiencies of
the original IBM PC architecture.  I hate to agree with Bill Gates
on anything, but one of the reasons he wants to get completely rid
of DOS compatibility is so Windows can move to an entirely new
architecture without the severe restrictions of the old IBM PC
architecture.  In the long run, this really will be a good thing.
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 16)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eas09soo378sgfitepgpbvfr27ucgoomin@4ax.com>`
- **References:** `<ep7m8s0j268sehc15hoi9ejvnvtv484tha@4ax.com> <20000125035025.07131.00000179@ng-ck1.aol.com> <86lknk$8of$1@ssauraab-i-1.production.compuserve.com> <k4Dj4.29616$wk.516728@news1.mia>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:

>Russell Styles wrote:
>>    I have not tried this on a wide variety of systems, but on
>>at least one pc, running either DOS or Win95/98, I found that
>>the system clock would not return every tick in the hundredths field,
>>but would update itself only (I assume) 18.2 times a second.

>This is correct.  It is a holdover and one of the deficiencies of
>the original IBM PC architecture.  I hate to agree with Bill Gates
…[3 more quoted lines elided]…
>architecture.  In the long run, this really will be a good thing.

i don't know if this is true or not. i do know that there is still
software out there which uses 18.2 ticks as a method for determining
the driver speed. i also know that if gates tries to change one thing,
he will change other things as well, usually to our detriment. i still
have not found any logical explanation for the gui change from windows
3.11 to 95. i understand the FAT expansion and the 256 char filename,
but i don't agree with the expansion to a 32 bit bus.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3884783A.5CCDA61F@NOSPAMwebaccess.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net>`

```
Just curious.  What type of business needs have COBOL programs which
care about leap seconds?
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kd9h4.1807$hi2.30408@dfiatx1-snr1.gtei.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <3884783A.5CCDA61F@NOSPAMwebaccess.net>`

```
Howard Brazee wrote in message <3884783A.5CCDA61F@NOSPAMwebaccess.net>...
>Just curious.  What type of business needs have COBOL programs which
>care about leap seconds?

Legal Accounting Systems.

The  $&^@(&%  lawyers bill for everything.

MCM
```

###### ↳ ↳ ↳ Re: Leap Seconds and COBOL

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388F0573.9710A522@NOSPAMwebaccess.net>`
- **References:** `<85h88q$ram$1@nntp9.atl.mindspring.net> <uKXqqYyX$GA.211@cpmsnbbsa05> <3880731C.7C3BB74D@zip.com.au> <On69SP3X$GA.244@cpmsnbbsa05> <85qd7o$fv0$1@nntp3.atl.mindspring.net> <3884783A.5CCDA61F@NOSPAMwebaccess.net> <kd9h4.1807$hi2.30408@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> Howard Brazee wrote in message <3884783A.5CCDA61F@NOSPAMwebaccess.net>...
…[7 more quoted lines elided]…
> MCM

As they did when they had clerks writing in the time by hand.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
