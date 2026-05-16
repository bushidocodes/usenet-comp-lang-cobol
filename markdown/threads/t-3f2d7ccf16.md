[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and a future

_13 messages · 11 participants · 1999-05 → 1999-06_

---

### COBOL and a future

- **From:** "fs" <fred_snyder@hotmail.com>
- **Date:** 1999-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rYb43.44$cb5.12265@ord-read.news.verio.net>`

```
In the COBOL debate thread I didn't see mention of UNIX platforms. I think
you will find that most UNIX users downsized from various mainframe
platforms and are running COBOL apps very successfully. In addition the
number of NT sever apps written in COBOL is on the rise (now that NT is
"starting" to mature as a serious operating system). Several companies, my
employer included, are planning web apps within an NT environment with COBOL
and Oracle on the server and a thin-client browser front-end. I have also
been lucky enough to get involved with a voice response system that uses
Micro Focus COBOL on the server with very good response times.

In other words COBOL will out live us all, and our grandson's will be having
this same debate after we're long gone.
```

#### ↳ Re: COBOL and a future

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%he43.4268$LA2.68660@dfiatx1-snr1.gtei.net>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net>`

```
COBOL programmers will one day be frantically attempting to deal with the
Y3K problem.
And they will be asked to do so constrained by a totally inadequate budget.
```

##### ↳ ↳ Re: COBOL and a future

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3753DADC.504C1445@NOSPAMhome.com>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <%he43.4268$LA2.68660@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> COBOL programmers will one day be frantically attempting to deal with the
> Y3K problem.
> And they will be asked to do so constrained by a totally inadequate budget.

I see programmers being asked frantically to finish the Y2K problem in
sites with fixed windows and with operating systems with date limits in
the years to come.   At the last minute without an adequate budget.
```

#### ↳ Re: COBOL and a future

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37528279.655A17E@zip.com.au>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net>`

```
fs wrote:
> 
> 
> In other words COBOL will out live us all, and our grandson's will be having
> this same debate after we're long gone.

Sexist!
```

##### ↳ ↳ Re: COBOL and a future

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-05-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au>`

```
    I would assume that the Y3K problem could start at any time, but 2080
would be my best guess.  Some people have been "solving" the Y2K problem
with pivot dates.  Once you pass the pivot date in the new cetury, the fix
fails.

    Of course, why would someone want to look at detailed sales history from
100 years ago.  How many applications truly create data that will be
meaningfull 100 years from now?
```

###### ↳ ↳ ↳ Re: COBOL and a future

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-05-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375314FB.ED25F29C@acm.org>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com>`

```
Russell Styles wrote:
>     I would assume that the Y3K problem could start at any time, but 2080
> would be my best guess.  Some people have been "solving" the Y2K problem
…[4 more quoted lines elided]…
> meaningfull 100 years from now?

  That wouldn't be a "Y3K" problem, as it has no relation to year 3000,
only to reaching the end of a 100-year window.  Those who have chosen a
fixed windowing scheme to reduce the effort of Y2K fixes could start
having problems way before 2080.  Current personnel files can contain
birthdates back into the 1930's and 1940's, and if a "common" window for
all date fields was chosen, things could begin to get dicey as early as
2030 or 2040. Earlier problems could occur for files that also contain
future dates.  Any company that has taken the easy approach on Y2K had
better start giving serious thought by 2001 as to how they are going to
get windowed dates out of database files and out of program internals
while there is still plenty of time.  One of the lessons of Y2K that
should have been learned by anyone who has been awake the last several
years is that programs, and especially the databases they create, have a
lifetime and an influence beyond their lifetime that is much, much
longer than their designers anticipate.
  If those who took the easy path on Y2K properly remedy the use of
fixed windowing (and the use of any other clever compression techniques
with a limited span)  while there is still plenty of time, there should
not be any major date-related problems on any century transition until
there is either a calendar change or a 9999 to 10,000 year transition. 
If they don't learn from the lessons of the past, then they will be
repeating the recent date maintenance exercise every 50-80 years.
  Another lesson that should have been learned is that an installation
should standardize on one routine for any date calculation, especially
that influenced by leap year considerations.  This is both to avoid
errors (it's amazing how many people including some programmers have
problems with the leap-year rules), and to be kind to future generations
who will be working with the cloned descendants of your code when the
next major calendar adjustment is required (at present rates, the
leap-year rules may require the introduction of a 3200-year exception
rule on or about 3200).  We can't write code to implement rules that
don't yet exist, but we can at least centralize things so that only one
routine needs to be changed to address a change in all applications.
  Historians could have an interest in all kinds of mundane data from
previous generations.  They are going to have serious problems with
records which are only preserved in machine readable form on obsolete
media for obsolete programs.
```

###### ↳ ↳ ↳ Re: COBOL and a future

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-05-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3753251e@news3.us.ibm.net>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com> <375314FB.ED25F29C@acm.org>`

```
unix will have a problem around 2031 or thereabouts when the number of
seconds
since 1970 won't fit in 32-bits.
Joel C. Ewing <jcewing@acm.org> wrote in message
news:375314FB.ED25F29C@acm.org...
> Russell Styles wrote:
> >     I would assume that the Y3K problem could start at any time, but
2080
> > would be my best guess.  Some people have been "solving" the Y2K problem
> > with pivot dates.  Once you pass the pivot date in the new cetury, the
fix
> > fails.
> >     Of course, why would someone want to look at detailed sales history
from
> > 100 years ago.  How many applications truly create data that will be
> > meaningfull 100 years from now?
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL and a future

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3753D2EB.998930F0@zip.com.au>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com> <375314FB.ED25F29C@acm.org> <3753251e@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
> 
> unix will have a problem around 2031 or thereabouts when the number of

Thought it was 2047 (could be wrong, the number of seconds from
1960 something in a four byte field.

The bottom line for this one is that the applications will be
compiled in 64 bit before then.  The only problem will be the
integer data conversion modules if the number is stroed in binary.
```

###### ↳ ↳ ↳ Re: COBOL and a future

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37551b34.1245822710@news1.ibm.net>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com> <375314FB.ED25F29C@acm.org> <3753251e@news3.us.ibm.net> <3753D2EB.998930F0@zip.com.au>`

```
On Tue, 01 Jun 1999 22:32:43 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>Leif Svalgaard wrote:
>> 
>> unix will have a problem around 2031 or thereabouts when the number of
>

It's 2037-2038.

>Thought it was 2047 (could be wrong, the number of seconds from
>1960 something in a four byte field.
>
>The bottom line for this one is that the applications will be
>compiled in 64 bit before then. 

And all the COBOL programs written in the 60s and 70s will be replaced
before the 2 digit years are a problem..... uh huh...

> The only problem will be the
>integer data conversion modules if the number is stroed in binary.

Y2K all over again.  <G>
```

###### ↳ ↳ ↳ Re: COBOL and a future

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6f53.2313$o56.523@news1.mia>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com> <375314FB.ED25F29C@acm.org> <3753251e@news3.us.ibm.net> <3753D2EB.998930F0@zip.com.au> <37551b34.1245822710@news1.ibm.net>`

```
Thane Hubbell wrote:
>Ken Foskey wrote:
>>
…[3 more quoted lines elided]…
>Y2K all over again.  <G>

There's one big difference between C and COBOL in this respect.  How
many even 10 year old C programs are still around?  Probably very,
very few.  The things C is being used for are much more volatile and
transient than the things COBOL is used for.
```

###### ↳ ↳ ↳ Re: COBOL and a future

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3753DB3B.2E3CCF29@NOSPAMhome.com>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com>`

```
Russell Styles wrote:
> 
>     I would assume that the Y3K problem could start at any time, but 2080
> would be my best guess.  Some people have been "solving" the Y2K problem
> with pivot dates.  Once you pass the pivot date in the new cetury, the fix
> fails.

920 years early?  Not a chance.  920 days early?  Not likely.  
 
>     Of course, why would someone want to look at detailed sales history from
> 100 years ago.  How many applications truly create data that will be
> meaningfull 100 years from now?

Life insurance.
```

###### ↳ ↳ ↳ Re: COBOL and a future

_(reply depth: 4)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l2jt7LA3vwV3Ewqp@ld50macca.demon.co.uk>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com> <3753DB3B.2E3CCF29@NOSPAMhome.com>`

```
I'm working at a Cobol and Adabas/Natural shop where the year 2000
problem has been 'resolved' by using ALTSEQ in DFSORT (ie sort 50 to 99
before 01 to 49) so I reckon on being back in work at the age 70 in
2049.

In article <3753DB3B.2E3CCF29@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes
>Russell Styles wrote:
>> 
…[11 more quoted lines elided]…
>Life insurance.
```

###### ↳ ↳ ↳ Re: COBOL and a future

- **From:** Charles Hall <charles.hall@platinum.brooks.af.mil>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37541F0A.5EDD@platinum.brooks.af.mil>`
- **References:** `<rYb43.44$cb5.12265@ord-read.news.verio.net> <37528279.655A17E@zip.com.au> <uWKCTY6q#GA.361@nih2naad.prod2.compuserve.com>`

```
Russell Styles wrote:

> 
>     Of course, why would someone want to look at detailed sales history from
> 100 years ago.  How many applications truly create data that will be
> meaningfull 100 years from now?
Our epidemiologists study disease data back as far as they can in order
to spot trends, including partial data from over 100 years ago.  The
great flu pandemic early this century is still being analyzed and
apparently will be well into the next century.  We plan to preserve much
of our data so that future generations will not have to start from
scratch.

Charles Hall
Brooks AFB TX
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
