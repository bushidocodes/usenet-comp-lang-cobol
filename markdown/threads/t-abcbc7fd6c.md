[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# more y2k problems

_7 messages · 5 participants · 1999-12 → 2000-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### more y2k problems

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84em9t02d9@enews4.newsguy.com>`

```
Weird problem happened today.  A strange dump led us to a reporting job that
was S0C7'ing all over the place.   One of the records it accessed, it went
for the 0 occurence of table and walked over the previous elements.  After
dumping the internal tables with some displays, I saw some records that were
coming from the database that were all screwed up.

A program runs daily which creates sets in an IDMS database.  For one
record, it disconnects 4 sets, then reconnects them based on the records
with the most recent date (to create the active sets if you will).  We had
put date windowing in the program but the problem was with the records.
They only had a 2 digit year.  When the program reconnects sets, it walks an
automatic set to sweep the records.  Problem is the automatic set was in an
ascending order, so the future effective date records with '00' in the year
were walked first.  A strange logic bug in the program then appeared, where
the program walks prior one record before connecting a set.  It was walking
all over the place and corrupting our database real fast, hence causing the
reporting job to blow up.

The '00' year dated records also manifested more bugs in our CICS screens.
After looking at about 3 or 4 screens, sure enough, none of the screens have
any windowing logic, so '00' year records are presently 'history'.  After
the 1st of the year, I guess all records will become 'future'.  Not good.

Anyways, bottom line is, none of this stuff was tested before, so now we pay
the price.

duh.

Jeff
```

#### ↳ Re: more y2k problems

- **From:** kthompson@netexas.net (Kevin)
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net>`
- **References:** `<84em9t02d9@enews4.newsguy.com>`

```
On Wed, 29 Dec 1999 23:15:54 -0500, "Jeff Baynard"
<union27@macconnect.com> wrote:

>The '00' year dated records also manifested more bugs in our CICS screens.
>After looking at about 3 or 4 screens, sure enough, none of the screens have
…[8 more quoted lines elided]…
>Jeff

You're starting to scare me Jeff.  How many LOC was "renovated" at
this company?  Simple regression testing with aged data on (1) a
separate LPAR running in 2000 or (2) using a system date tool such as
Hourglass or Time Machine Journey would have shown these errors.

Sure we've had some failures but not this many so far out of 32
million LOC.  I predict many hours of overtime for you shortly.

cheers,
Kevin
```

##### ↳ ↳ Re: more y2k problems

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xTSa4.1198$Gj5.26382@dfiatx1-snr1.gtei.net>`
- **References:** `<84em9t02d9@enews4.newsguy.com> <A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net>`

```
The one problem I've been running into is date displays MM/DD/YY: a bunch of
the copylibs are coded using PIC ZZ/ZZ/ZZ.
```

###### ↳ ↳ ↳ Re: more y2k problems

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386CB8ED.BA8A4A1D@NOSPAMwebaccess.net>`
- **References:** `<84em9t02d9@enews4.newsguy.com> <A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net> <xTSa4.1198$Gj5.26382@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> The one problem I've been running into is date displays MM/DD/YY: a bunch of
> the copylibs are coded using PIC ZZ/ZZ/ZZ.
> 

That one also looks ugly, you have dates looking like "10/ 1/99" even
without a new century.  Was the author into ugliness?
```

###### ↳ ↳ ↳ Re: more y2k problems

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BI5b4.479$_S6.11684@dfiatx1-snr1.gtei.net>`
- **References:** `<84em9t02d9@enews4.newsguy.com> <A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net> <xTSa4.1198$Gj5.26382@dfiatx1-snr1.gtei.net> <386CB8ED.BA8A4A1D@NOSPAMwebaccess.net>`

```
At least they *are* in copylibs, so it is (at least should be!) just a
recompile/linkedit.

PS: I *like*  "10/ 1/99"   format

PPS : I do NOT like  " 1/ 1/  "
```

##### ↳ ↳ Re: more y2k problems

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84p9ii0au1@enews4.newsguy.com>`
- **References:** `<84em9t02d9@enews4.newsguy.com> <A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net>`

```
We have alot of programs, don't know how many.  Our group is responsible for
well over 2,000 programs, mostly batch.  The guy who 'tested' this system in
particular *retired* in 1998 so that probably explains it.  Plus, this
particular database runs on a different LPAR than our main one; I joined the
company after most Y2K testing was done so I really don't know how well they
tested this database.

Otherwise, very few Y2K related problems occured over the weekend to my
knowledge.  The worst one was our pharmacies were denying over 10 different
insurance plans on Saturday but it was attibuted to the third party systems,
not ours.

We also had a problem with a yearly job that was modified with some new
steps last year, but that would have happened for any year.  IDCAMS was
trying to delete/define/repro an open 'date' dataset.  A call to the systems
people shut the files down in a matter of seconds and the job was restarted.
Sounds like a need for a CMTBATCH close step.  Funny part is, I doubt
anybody's gonna fix it so it'll just happen again next year.  Hope I'm not
on call.

Jeff

----------
In article
<A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net>,
kthompson@netexas.net (Kevin) wrote:


> On Wed, 29 Dec 1999 23:15:54 -0500, "Jeff Baynard"
> <union27@macconnect.com> wrote:
…[22 more quoted lines elided]…
> Kevin
```

###### ↳ ↳ ↳ Re: more y2k problems

- **From:** Pete Maddock <Frank@maddockp.demon.co.uk>
- **Date:** 2000-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Rw2QFAc5Ic4Ewe2@maddockp.demon.co.uk>`
- **References:** `<84em9t02d9@enews4.newsguy.com> <A8F81C2AD9018649.E4B467E77000F55E.5C40F80A5B4CEB83@lp.airnews.net> <84p9ii0au1@enews4.newsguy.com>`

```
Nothing to do with COBOL but this amused me.

The systems where a friend of mine works were shut down over the new
year and were due to be brought back up on the Monday. He had to go in
and test the distribution systems on the 1st and they had been planning
this for months - fully scripted, the works. 2 days before Xmas the user
of the time and recording system rang him and asked 'while you are in
could you just test our system for us please?'. 

Three guesses what the answer was (and 1 guess as to which of the
systems in his place didn't work).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
