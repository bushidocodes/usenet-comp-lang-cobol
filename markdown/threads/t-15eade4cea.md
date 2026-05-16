[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is 4000 a leap year?

_14 messages · 11 participants · 2000-01 → 2000-02_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### RE: Is 4000 a leap year?

- **From:** einomoto@compuserve.com (Edmond J. Inomoto)
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00000029123740.OUI26.einomoto@compuserve.com>`

```
Hi,

On January 24 2000, Kent Feiler <kfeiler@cpiusa.com> wrote:

> Interesting, I thought this was a rule as well, i.e. that dates
> divisable by 4,000 were NOT leap years.  Believe it or not, I need to
…[6 more quoted lines elided]…
> kfeiler@cpiusa.com

According to the book "Standard C Date/Time Library" by Lance Latham,
Miller-Freeman, 1998, p. 249:

"... The alleged reform would add a fourth part to the Gregorian leap
year rule, making years evenly divisible by 4,000 common years [i.e.
non-leap years]..."

"...While this reform has been proposed occassionally, it has never been
implemented."

HTH.
```

#### ↳ Re: Is 4000 a leap year?

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3896ECB4.63C05424@NOSPAMwebaccess.net>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com>`

```
"Edmond J. Inomoto" wrote:

> "... The alleged reform would add a fourth part to the Gregorian leap
> year rule, making years evenly divisible by 4,000 common years [i.e.
…[5 more quoted lines elided]…
> HTH.

Well, we'd better hurry up, it's only 2000 years away.
```

#### ↳ Re: Is 4000 a leap year?

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<878rjd$66r$1@news.inet.tele.dk>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com>`

```
4000 is a leap year. The 4000-rule is only a proposal - so ignore it in your
countdown. You will probably find the time to change it, if the rules are
changed.
regards
Ib
Edmond J. Inomoto skrev i meddelelsen
<00000029123740.OUI26.einomoto@compuserve.com>...
>Hi,
>
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Is 4000 a leap year?

- **From:** jgrnwld@gcfn.org (Jason Greenwald)
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87te3v$2en$1@acme.gcfn.org>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com> <878rjd$66r$1@news.inet.tele.dk>`

```
Is that now the Y4K problem?

Ib Tanding (ib@tanding.dk) wrote:
: 4000 is a leap year. The 4000-rule is only a proposal - so ignore it in your
: countdown. You will probably find the time to change it, if the rules are
: changed.
: regards
: Ib
: Edmond J. Inomoto skrev i meddelelsen
: <00000029123740.OUI26.einomoto@compuserve.com>...
: >Hi,
: >
: >On January 24 2000, Kent Feiler <kfeiler@cpiusa.com> wrote:
: >
: >> Interesting, I thought this was a rule as well, i.e. that dates
: >> divisable by 4,000 were NOT leap years.  Believe it or not, I need to
: >> know this since I was thinking of turning my Y2K countdown clock into
: >> a Y10K countdown.  Are 4,000 and 8,000 leap years or not?
: >>
: >>
: >>
: >> Kent Feiler
: >> kfeiler@cpiusa.com
: >
: >According to the book "Standard C Date/Time Library" by Lance Latham,
: >Miller-Freeman, 1998, p. 249:
: >
: >"... The alleged reform would add a fourth part to the Gregorian leap
: >year rule, making years evenly divisible by 4,000 common years [i.e.
: >non-leap years]..."
: >
: >"...While this reform has been proposed occassionally, it has never been
: >implemented."
: >
: >HTH.
: >
: >
: >--
: > - Edmond J. Inomoto einomoto@compuserve.com
: >
```

#### ↳ Re: Is 4000 a leap year? ONCE AGAIN

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m8zm4.2658$Sx.47390@news4.mia>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com>`

```
Once again, for those of you who are too lazy (or SMUG) to look this up: you
can find the
info by searching for [Y2K Leap Year Pope] on Hotbot.com or Yahoo.  From
Hotbot, listing  one was:
from U.S. DOE:




Leap Year Considerations
March 17, 1998
Year 2000 is a leap year and this could cause problems in two ways.
The rule laid down by Pope Gregory in 1582 is that leap years are those that
are divisible by four. Century years are only leap years if they are also
divisible by 400. So the year 2000 is, but 1900 was not, even though it is
divisible by four. If the computer thinks it is dealing with the year 1900,
not 2000, it will have a problem because 2000 is a leap year, but 1900 was
not. Therefore, all entries for February 29, 1900, will be rejected.
A more likely scenario, is that the computer system may recognize that the
year is 2000, but because of programming error, may not understand that it
is a leap year. Software programmers sometimes forget about leap years or
have not provided for all the exceptions. An Internet site with an in-depth
explanation (http://www.gmt-2000.com), quotes from the Latin version in
which Pope Gregory XIII defines "anno vero MM" (Year 2000) specifically as a
leap year.
Also visit the National Institute of Standards and Technology (NIST) site
for "How to Compute Leap Year -- The Algorithm" at:
http://www.nist.gov/y2k/.


Select first item - FAQ


Question #3:
Q. Is the year 2000 a leap year?
A. Yes. Normally century years (those ending in 00) are not leap years, but
2000 is. See the white paper on how to compute leap year.

HOW TO COMPUTE LEAP YEAR
How does one calculate whether a year is a Leap year? This question and its
cousin "Is the year 2000 a Leap year?" have been asked often enough that it
is time to put a note here on the web site.
According to the Papal Bull of 1582, Pope Gregory declared that a year is
365.2425 days in length. From this, a normal year is 365 days with a leap
year occuring every 4th year. This corrects the movement of the calendar
date in relation to the sun's position to within 3 days in 400 years. To
further correct for this 3-day error, 3 leap years are skipped every 400
years. By proclamation, Pope Gregory made all years divisible by 4 with no
remainder a leap year, and modified that to exclude years that were
divisible by 100 with no remainder. Further, the 400 year rule corrected the
100 year rule so that a leap year occurs in years divisible by 400 with no
remainder. Leap years occur normally in years divisible by 4 with no
remainder, except for those years that are century years, such as 1700,
1800, and 1900 (i.e., 3 leap years are dropped every 400 years). Century
years that are divisible by 400 with no remainder, such as 1600, 2000, and
2400 are leap years, which occur once every 400 years.
Simple? For those tuned to programming, the following shows a pseudocode
specification of the algorithm:
Given a year, Y, and a function, MOD(Y,n) that returns the remainder of Y
divided by n, then--
if (MOD(Y,4) == 0) and ((MOD(Y,100) <> 0) or (MOD(Y,400) == 0)) LeapYear =
true
    else LeapYear = false;
A table of these rules and several examples appears as follows:


RULE / EXAMPLE                                             1999     1996
1900     2000
Year divisible by 4 with no remainder?           FALSE  TRUE    TRUE  TRUE
Year divisible by 100 with no remainder?      FALSE  FALSE  TRUE TRUE
Year divisible by 400 with no remainder?      FALSE  FALSE  FALSE TRUE
Is it a leap year?                                                NO
YES        NO      YES

Any questions?

For further information on time measurement, check the NIST time web site at
http://www.boulder.nist.gov/timefreq/faq/faq.htm.


Edmond J. Inomoto <einomoto@compuserve.com> wrote in message
news:00000029123740.OUI26.einomoto@compuserve.com...
> Hi,
>
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%gFm4.3502$Sx.62770@news4.mia>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com> <m8zm4.2658$Sx.47390@news4.mia>`

```
James King wrote:
>Once again, for those of you who are too lazy (or SMUG) to look this up: you
>can find the
>info by searching for [Y2K Leap Year Pope] on Hotbot.com or Yahoo.  From
>Hotbot, listing  one was:
>from U.S. DOE:

If anyone is writing a COBOL program that cares whether year 4000 is
a leap year or not, please let me know.  I would be fascinated to
learn the reason for such a thing. :-)
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000207002512.05639.00002137@ng-fz1.aol.com>`
- **References:** `<%gFm4.3502$Sx.62770@news4.mia>`

```
>If anyone is writing a COBOL program that cares whether year 4000 is
>a leap year or not, please let me know.  I would be fascinated to
>learn the reason for such a thing. :-)

Not that I am writing one, but I can think of one - Part of a control system
for the proposed Federal Nuclear Waste Repository, which needs to be functional
for several 10's of thousands of years.  Of course, the power supply problems
might be more critical!! <G>
Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87n36j$4l4$1@aklobs.kc.net.nz>`
- **References:** `<%gFm4.3502$Sx.62770@news4.mia> <20000207002512.05639.00002137@ng-fz1.aol.com>`

```
Steve Newton <stevenln@aol.comnospam> wrote:
:>If anyone is writing a COBOL program that cares whether year 4000 is
:>a leap year or not, please let me know.  I would be fascinated to
:>learn the reason for such a thing. :-)

: Not that I am writing one, but I can think of one - Part of a control system
: for the proposed Federal Nuclear Waste Repository, which needs to be functional
: for several 10's of thousands of years.  

While that may be a system that will cater for dates quite some time
in the future, I doubt that it would _care_ whther 4000 is a leap
year or not.  It is not like to will have to match up with a
printed calendar stuck on the wall.

Whether there is an adjustment around 4000 or 3600 depends on
variations in the Earth's orbit and rotational speed.  We
cannot predict accurately enough to know when is the best
time to take off one day to keep within half a day of the
cycles set in 1582.  The decision about this has been left
for the future to make.  In the meantime assume 3600 and 4000
will be leap years, just as everyone else is.
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389F1129.6251456C@NOSPAMwebaccess.net>`
- **References:** `<%gFm4.3502$Sx.62770@news4.mia> <20000207002512.05639.00002137@ng-fz1.aol.com> <87n36j$4l4$1@aklobs.kc.net.nz>`

```
Some short sighted people will wait for the very last millennium to fix Y4K bugs.
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389EE3D8.D417DAEC@NOSPAMwebaccess.net>`
- **References:** `<%gFm4.3502$Sx.62770@news4.mia> <20000207002512.05639.00002137@ng-fz1.aol.com>`

```
Steve Newton wrote:

> >If anyone is writing a COBOL program that cares whether year 4000 is
> >a leap year or not, please let me know.  I would be fascinated to
…[5 more quoted lines elided]…
> might be more critical!! <G>

Cobol will be around for a while, but 2000 years is a stretch.  And one day won't
make any significant difference.  A plaque might be better, but who knows what
language people will be speaking then?  Is the rate of change in the world slowing
down?

If the rate of change stays constant, the year 4000 will be as different from now
as the year 1 was.  And the language and people in Star Trek will be as different
as Shakespeare.  But it appears that the rate of change is accelerating, in which
case things will be a lot more different.
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KDBn4.3952$Xi6.49269@news2.mia>`
- **References:** `<%gFm4.3502$Sx.62770@news4.mia> <20000207002512.05639.00002137@ng-fz1.aol.com>`

```
Steve Newton wrote:
>>If anyone is writing a COBOL program that cares whether year 4000 is
>>a leap year or not, please let me know.  I would be fascinated to
…[5 more quoted lines elided]…
>might be more critical!! <G>

Hmmm.  Think missing a leap day after 4000 years is going to make
any difference? ;-)
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88835c$hk2$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com> <m8zm4.2658$Sx.47390@news4.mia> <%gFm4.3502$Sx.62770@news4.mia>`

```
    I don't think anybody has mentioned this - For all practical purposes up
to the year 2100,
the old simple rule, "It is a leap year if divisable by 4" works just fine.



Judson McClendon <judmc@bellsouth.net> wrote in message
news:%gFm4.3502$Sx.62770@news4.mia...
> James King wrote:
> >Once again, for those of you who are too lazy (or SMUG) to look this up:
you
> >can find the
> >info by searching for [Y2K Leap Year Pope] on Hotbot.com or Yahoo.  From
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 4)_

- **From:** sbt@my-deja.com
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8898fb$m5o$1@nnrp1.deja.com>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com> <m8zm4.2658$Sx.47390@news4.mia> <%gFm4.3502$Sx.62770@news4.mia> <88835c$hk2$1@ssauraaa-i-1.production.compuserve.com>`

```
Yes but as programmers we must think of every possibility. I would not
want to have to debug my 100 year old code in the year 2099 because of
a possible problem with 2100 not being a leap year.
-Steve

In article <88835c$hk2$1@ssauraaa-i-1.production.compuserve.com>,
  "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM> wrote:
>     I don't think anybody has mentioned this - For all practical
purposes up
> to the year 2100,
> the old simple rule, "It is a leap year if divisable by 4" works just
fine.
>
> Judson McClendon <judmc@bellsouth.net> wrote in message
> news:%gFm4.3502$Sx.62770@news4.mia...
> > James King wrote:
> > >Once again, for those of you who are too lazy (or SMUG) to look
this up:
> you
> > >can find the
> > >info by searching for [Y2K Leap Year Pope] on Hotbot.com or
Yahoo.  From
> > >Hotbot, listing  one was:
> > >from U.S. DOE:
…[8 more quoted lines elided]…
> > whoever believes in Him should not perish but have everlasting
life."
> >
> >
> >
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Is 4000 a leap year? ONCE AGAIN

_(reply depth: 5)_

- **From:** "John Kurt Nielsen" <johnkurt@image.dk>
- **Date:** 2000-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88avt8$n1m$1@news.inet.tele.dk>`
- **References:** `<00000029123740.OUI26.einomoto@compuserve.com> <m8zm4.2658$Sx.47390@news4.mia> <%gFm4.3502$Sx.62770@news4.mia> <88835c$hk2$1@ssauraaa-i-1.production.compuserve.com> <8898fb$m5o$1@nnrp1.deja.com>`

```
It is simpel.
It is a lead year if You can divide with 4, but but:
1) If You can divide with 100 it is NOT a lead year except if You can divide
with 400 it IS a lead anyway

John Kurt Nielsen
jknls@tdk.dk
sbt@my-deja.com skrev i meddelelsen <8898fb$m5o$1@nnrp1.deja.com>...
>Yes but as programmers we must think of every possibility. I would not
>want to have to debug my 100 year old code in the year 2099 because of
…[40 more quoted lines elided]…
>Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
