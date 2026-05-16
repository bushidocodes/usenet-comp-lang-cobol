[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Here is one person view, what do you think?

_12 messages · 9 participants · 1998-06_

---

### Re: Here is one person view, what do you think?

- **From:** "Steve" <sfoster@proweb.co.uk>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35912dbc.0@news.proweb.co.uk>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Mon, 15 Jun 1998 07:18:56, Esmond Pitt <pitte@cpgen.cpg.com.au>
>wrote:
…[7 more quoted lines elided]…
>feasable and reliable solution.


I'm a relative beginner at programming especially in the windows environment
so excuse the question, but what is a sliding window. I've not come across
this term before.

Regards,

Steve Foster
```

#### ↳ Re: Here is one person view, what do you think?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4_ak1.1056$w05.1600699@news1.atl.bellsouth.net>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com> <35912dbc.0@news.proweb.co.uk>`

```

Steve wrote:
>
>I'm a relative beginner at programming especially in the windows environment
>so excuse the question, but what is a sliding window. I've not come across
>this term before.


Let me give you a real example which I coded just last week for a client.
Assume that the 2 digit year is within the century beginning 79 years ago
and ending 20 years in the future.  You could make any other assumption you
like about the target century, so long as the span is 100 years, but this was
appropriate for our data.  You can easily resolve (interpret) the date to
be within that period by using the computer date and a little logic, like
this:

       01  DATE-WORK-AREA.
           03  DW-TODAYS-CCYY    PIC  9(04).
           03  DW-TODAYS-CCYY-R  REDEFINES DW-TODAYS-CCYY.
               05  DW-TODAYS-CC      PIC  9(02).
               05  DW-TODAYS-DD      PIC  9(02).

           03  DW-CCYY           PIC  9(04).
           03  DW-CCYY-R         REDEFINES DW-CCYY.
               05  DW-CC             PIC  9(02).
               05  DW-YY             PIC  9(02).

Populate DW-TODAYS-CCYY from computer date at program BOJ.  Then, when
you get ready to 'window' a 2 digit year, do this:

       MOVE DW-TODAYS-CC   TO DW-CC.
       MOVE <2 digit year> TO DW-YY.
       IF (DW-CCYY < DW-TODAYS-CCYY - 79)
           ADD 100 TO DW-CCYY
       ELSE
           IF (DW-CCYY > DW-TODAYS-CCYY + 20)
               SUBTRACT 100 FROM DW-CCYY.

Note that if the actual date is February 29, and DW-YY = zero, you will
need to examine DW-CC to see if it is a leap year.  If DW-CC MOD 4 = 0,
then the century year is a leap year, otherwise not.  If you don't take
this step, February 29, 2100, and 2200, 2300, 2500, etc., will be accepted
as valid, although 2100, 2200, 2300, 2500, etc. will not be leap years. ;-)

Because this method assumes the input date falls within a specified
'window', relative to the current date, you never have a problem as time
progresses, because the computer date progresses.  Dates such as birth
dates usually cannot be resolved this way, because in early 2000, there
will be birth dates spanning three centuries (18xx, 19xx, 20xx), even
for living people.  Only if you can assume that the dates will always
fall with some window <= 100 years, relative to some known date, such as
computer date, can this method be used.

Windowing is very useful to permit users to continue entering 6 digit
dates indefinitely, for transaction dates or other dates which will
always fall within the moving window.
```

#### ↳ Re: Here is one person view, what do you think?

- **From:** Chip Ling <chipling@sympatico.ca>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35917699.611B@sympatico.ca>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com> <35912dbc.0@news.proweb.co.uk>`

```

Steve wrote:
> 
> Thane Hubbell wrote in message ...
…[17 more quoted lines elided]…
> Steve Foster

Steve,

What the discussion about windowing solution is one of the way how we
use 2 digits year field to overcome the year 2000 problem. See 
Judson's detail explanation in his mail. There's nothing related to
the "Window environment", I assume you are talking about MicroSoft
Window or XWindow.

Rgds,
Chip Ling
```

#### ↳ Re: Here is one person view, what do you think?

- **From:** john@watkins.cix.co.uk (John Watkins)
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<memo.19980624202632.39N@watkins.compulink.co.uk>`
- **References:** `<35912dbc.0@news.proweb.co.uk>`

```

In article <35912dbc.0@news.proweb.co.uk>, sfoster@proweb.co.uk (Steve)
wrote:

> Thane Hubbell wrote in message ...
> >On Mon, 15 Jun 1998 07:18:56, Esmond Pitt <pitte@cpgen.cpg.com.au>
…[14 more quoted lines elided]…
> this term before.
 
It's nothing to do with 'Windows', but is a way of implementing conversion
from two digit years to four digit years.

We use a window of -30 to +70 from the current date, so at the moment:

              Now
  |------------X---------------------------|
1968          1998                       2067

Any date entered with values greater than 68 uses the lower date century,
and any date less than 68 uses the upper date century.


+--------------+------------------------------------+
| John Watkins | mailto:john@watkins_dot_cix.co.uk  |
|              | http://www_dot_cix.co.uk/~watkins/ |
+--------------+------------------------------------+
```

##### ↳ ↳ Re: Here is one person view, what do you think?

- **From:** "Arnold Hausmann" <ArnoldH@msn.com>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ezokrA#n9GA.256@upnetnews05>`
- **References:** `<35912dbc.0@news.proweb.co.uk> <memo.19980624202632.39N@watkins.compulink.co.uk>`

```

John Watkins wrote in message ...
(snip)
>It's nothing to do with 'Windows', but is a way of implementing conversion
>from two digit years to four digit years.
…[8 more quoted lines elided]…
>and any date less than 68 uses the upper date century.

I am missing why this is called a "sliding" window.  You have a "pivot" year of '68; any two digit year under is 21th century, etc.  How does this slide?  Wouldn't you have to change the pivot year for the window to slide?
```

###### ↳ ↳ ↳ Re: Here is one person view, what do you think?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dk8LltQeuDQz@Dwight_Miller.iix.com>`
- **References:** `<35912dbc.0@news.proweb.co.uk> <memo.19980624202632.39N@watkins.compulink.co.uk> <ezokrA#n9GA.256@upnetnews05>`

```

On Thu, 25 Jun 1998 02:25:06, "Arnold Hausmann" <ArnoldH@msn.com> 
wrote:

> -------Begin Encoded File-------
> Encoded filename: 
…[4 more quoted lines elided]…
> 

Here's what I see.   

Yes Arnold, you do have to move the pivot point for the window to 
slide.  That pivot point is based on the current date.
```

###### ↳ ↳ ↳ Re: Here is one person view, what do you think?

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998062507272000.DAA12315@ladder03.news.aol.com>`
- **References:** `<ezokrA#n9GA.256@upnetnews05>`

```

In article <ezokrA#n9GA.256@upnetnews05>, "Arnold Hausmann" <ArnoldH@msn.com>
writes:

>DQpKb2huIFdhd

Arnold, I have seen several messages from you with that type of stuff in the
body of the message. It makes the messages from you impossible to read.

Mark A. Young
```

###### ↳ ↳ ↳ Re: Here is one person view, what do you think?

- **From:** Peter Maddock <Frank@maddockp.demon.co.uk>
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QwNdtAA+Agk1EwNp@maddockp.demon.co.uk>`
- **References:** `<35912dbc.0@news.proweb.co.uk> <memo.19980624202632.39N@watkins.compulink.co.uk> <ezokrA#n9GA.256@upnetnews05>`

```

In article <ezokrA#n9GA.256@upnetnews05>, Arnold Hausmann
<ArnoldH@msn.com> writes
>
>John Watkins wrote in message ...
…[17 more quoted lines elided]…
>

I think what he means is:-

The window above is for this year, so a year of '67' will give '2067',
'68' will give '1968', and '69' will give '1969'. But then as of 1 Jan
next year the pivot will move so '67' will give '2067', '68' will give
'2068' and '69' will give '1969'. (I am sure someone will correct me if
I'm wrong). (Doesn't help with things like birthdays which can be > 100
years old though).
```

###### ↳ ↳ ↳ Re: Here is one person view, what do you think?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jPpk1.1207$w05.2062811@news1.atl.bellsouth.net>`
- **References:** `<35912dbc.0@news.proweb.co.uk> <memo.19980624202632.39N@watkins.compulink.co.uk> <ezokrA#n9GA.256@upnetnews05>`

```

Arnold Hausmann wrote in message ...
>
>John Watkins wrote in message ...
…[16 more quoted lines elided]…
>to slide?


Does the phrase "from the current date" ring a bell? ;-)
```

#### ↳ Re: Here is one person view, what do you think?

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35929cf6.8070500@news.enter.net>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com> <35912dbc.0@news.proweb.co.uk>`

```

"Steve" <sfoster@proweb.co.uk> wrote:

>Thane Hubbell wrote in message ...
>>On Mon, 15 Jun 1998 07:18:56, Esmond Pitt <pitte@cpgen.cpg.com.au>
…[18 more quoted lines elided]…
>

Steve:

Uh Oh...Now Thane is going to ask us to support "sliding GUI windows"
in sp2.  I guess the function parameter would be something like
SP2-CONVERSE-GREASED-PANEL.

Thane wasn't referring to a "GUI" windows when he was speaking of
"sliding windows" he was referring to a technique which is used in
some Year 2000 remediation projects.

The "sliding window" he was referring to was a "window of time" which
allows the application to correctly determine whether the 2 digit year
in question is attributable to the 20th century (i.e. "19") or the
21st century (i.e. "20")

The "sliding" part refers to the ability for the window of time to
periodically adjust so that the application can continue to correctly
determine the proper century digits.

How'd I do, Thane??

I will refrain from expressing my opinion on whether or not windowing
techniques are good or bad because it will start a thread which won't
die until we all start worrying about the Y10K problem....besides, I
am an amatuer when it comes to discussing Y2K solutions.

I prefer to express my opinions on GUI windowing issues.

Hope that helps.



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Here is one person view, what do you think?

- **From:** MIXXERDW@EYE_EYE_ECHS.COM
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-tvYBMSEiLW8O@dsm4merlin.iix.com>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com> <35912dbc.0@news.proweb.co.uk> <35929cf6.8070500@news.enter.net>`

```

On Thu, 25 Jun 1998 19:05:34, rtwolfe@flexus.com (Bob Wolfe) wrote:

> start a thread which won't
> die until we all start worrying about the Y10K problem....
> 
Heh, that's OK ... I'm about to put Thane onto the DOW10K problem, 
though.  He'll get a big kick out of it when I ask him to do it all in
Zulu time for international trading.

=Dwight=
X1=L, X2=L & the domain is phonetic
```

###### ↳ ↳ ↳ Re: Here is one person view, what do you think?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-6d4GqdzzFDuy@Dwight_Miller.iix.com>`
- **References:** `<357C0243.F91ED7EF@epamail.epa.gov> <Jl0PnHJ5PvPd-pn2-qQWNwdRUzXgl@Dwight_Miller.iix.com> <6lh5mu$fnr$1@websites.campbellhall.org> <6li8sb$6vd@bgtnsc03.worldnet.att.net> <3584CAE0.27FE4D4C@cpgen.cpg.com.au> <Jl0PnHJ5PvPd-pn2-ZLZRoTLZGtE2@Dwight_Miller.iix.com> <35912dbc.0@news.proweb.co.uk> <35929cf6.8070500@news.enter.net> <1tGZ16mMk7i4-pn2-tvYBMSEiLW8O@dsm4merlin.iix.com>`

```

On Fri, 26 Jun 1998 17:31:27, MIXXERDW@EYE_EYE_ECHS.COM wrote:

> On Thu, 25 Jun 1998 19:05:34, rtwolfe@flexus.com (Bob Wolfe) wrote:
> 
…[5 more quoted lines elided]…
> Zulu time for international trading.

I've had about enough Zulu time for the day.  Maybe next week.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
