[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Y2K

_12 messages · 10 participants · 2000-01 → 2000-02_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Y2K

- **From:** Ritchie Menzies <ritchie.menzies@gecm.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387DFF69.58F0CF68@gecm.com>`

```
Can someone please tell me if there is still need for COBOL programmers
in regards to correcting Y2K in the united kingdom and europe as a
whole?

I'm new to cobol and would appreciate any and all input...

Thanks
```

#### ↳ Re: Y2K

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85n5aq$60i$1@news.igs.net>`
- **References:** `<387DFF69.58F0CF68@gecm.com>`

```
No.  Have you looked at a calendar lately?

Ritchie Menzies wrote in message <387DFF69.58F0CF68@gecm.com>...
>Can someone please tell me if there is still need for COBOL programmers
>in regards to correcting Y2K in the united kingdom and europe as a
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Y2K

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J6Ff4.620$Lm3.3871@dfiatx1-snr1.gtei.net>`
- **References:** `<387DFF69.58F0CF68@gecm.com>`

```
Ritchie Menzies wrote in message <387DFF69.58F0CF68@gecm.com>...
>Can someone please tell me if there is still need for COBOL programmers
>in regards to correcting Y2K in the united kingdom and europe as a
…[3 more quoted lines elided]…
>


Well, I think all the Y2K work is done in both the US and the UK.

However....it is still summertime in the Southern Hemisphere, so there might
be a couple of months of Y2K work available in South America or Africa...


MCM
```

##### ↳ ↳ Re: Y2K

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387F31F9.FF821D4A@NOSPAMwebaccess.net>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <J6Ff4.620$Lm3.3871@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> However....it is still summertime in the Southern Hemisphere, so there might
> be a couple of months of Y2K work available in South America or Africa...
> 
> MCM


You're joking, right?
```

###### ↳ ↳ ↳ Re: Y2K

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GfQf4.927$nh2.23022@cac1.rdr.news.psi.ca>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <J6Ff4.620$Lm3.3871@dfiatx1-snr1.gtei.net> <387F31F9.FF821D4A@NOSPAMwebaccess.net>`

```

Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:387F31F9.FF821D4A@NOSPAMwebaccess.net...
> Michael Mattias wrote:
> >
> > However....it is still summertime in the Southern Hemisphere, so there
might
> > be a couple of months of Y2K work available in South America or
Africa...
> >
> > MCM
>
>
> You're joking, right?

Maybe in some strange logic he was thinking that in that part of the world
it's warm to hot and they didn't have to worry about freezing if the power
went off.
```

#### ↳ Re: Y2K

- **From:** Arthur <alembert@mypad.com>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85r2fe$fmf$1@nnrp1.deja.com>`
- **References:** `<387DFF69.58F0CF68@gecm.com>`

```
In article <387DFF69.58F0CF68@gecm.com>,
  Ritchie Menzies <ritchie.menzies@gecm.com> wrote:
> Can someone please tell me if there is still need for COBOL
programmers
> in regards to correcting Y2K in the united kingdom and europe as a
> whole?
…[5 more quoted lines elided]…
>

Hello, I think not all bugs were corrected. I also think the Feb 29 2000
problem will cause lot of troubles (because nobody know about it). Just
to say not all computers know leap-year formula is 1/4 - 1/100 + 1/400.

More info http://www.50megs.com/aalembert/y2kco.html

Thanks
```

##### ↳ ↳ Re: Y2K

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CzLg4.986$SM.12670@news4.mia>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <85r2fe$fmf$1@nnrp1.deja.com>`

```
Arthur wrote:
>
>Hello, I think not all bugs were corrected.

Agreed.

> I also think the Feb 29 2000
>problem will cause lot of troubles (because nobody know about it). Just
>to say not all computers know leap-year formula is 1/4 - 1/100 + 1/400.

I do not agree.  Why would anyone have put the Year/100 test for leap
year in a system using only a 2 digit year?  Very, very few systems
using 2 digit year were concerned with February, 1900.  If they were
concerned with dates that far back, they would probably have also been
concerned with dates before 1900, and used 4 digit year.  My guess is
that there will be more programs (if any) that fail 2/29/2000 because
of faulty Y2K remediation than because they did the Y/100 test, but not
the Y/400 test, in the original code.
```

###### ↳ ↳ ↳ Re: Y2K

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5CNg4.1928$nh2.65575@cac1.rdr.news.psi.ca>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <85r2fe$fmf$1@nnrp1.deja.com> <CzLg4.986$SM.12670@news4.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:CzLg4.986$SM.12670@news4.mia...
> Arthur wrote:
> >
…[23 more quoted lines elided]…
>

2000 / 4 = 500 with no remainder.  Should be flagged as a leap year.
Programs not using the 400 yr test shouldn't fail.  it will fail in/with the
year 2100 or 1900, in the sense that it's not a leap year although it too
has zero remainder.

Most programs I've seen have only the 4 yr test and not the 400 or 100 yr.
98.9999 % of the programs should work ok in the day to day business world.
Of couse this falls apart if they still somehow use 2 digits for a date
somewhere.

Tim
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 4)_

- **From:** Warren Porter <wb999port@bellsouth.net>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38848A34.160FD8B2@bellsouth.net>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <85r2fe$fmf$1@nnrp1.deja.com> <CzLg4.986$SM.12670@news4.mia> <5CNg4.1928$nh2.65575@cac1.rdr.news.psi.ca>`

```
True.  Code with only the 4 year test works from 1901-2099 which is quite
adequate for most businesses.

Tim Hillock wrote:

> Most programs I've seen have only the 4 yr test and not the 400 or 100 yr.
> 98.9999 % of the programs should work ok in the day to day business world.
…[3 more quoted lines elided]…
> Tim
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 5)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000119020514.03564.00000197@ng-cj1.aol.com>`
- **References:** `<38848A34.160FD8B2@bellsouth.net>`

```
> Of couse this falls apart if they still somehow use 2 digits for a date
>> somewhere.

Or, if they are expecting the month to only have 28 days, such as table
lookups, indice creations, and such??
Asimov, Heinlein, and Zappa
Still the best
```

##### ↳ ↳ Re: Y2K

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38974a41.3872858@news1.frb.gov>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <85r2fe$fmf$1@nnrp1.deja.com>`

```
On Sun, 16 Jan 2000 00:13:42 GMT, Arthur wrote:

>Hello, I think not all bugs were corrected. I also think the Feb 29 2000
>problem will cause lot of troubles (because nobody know about it). Just
>to say not all computers know leap-year formula is 1/4 - 1/100 + 1/400.

Actually, I think that the Year 2000 Feb 29 issue will probably little
different from any other leap year.  That is, it will probably be
nearly a non-event.

It is true that some computers/programs/people do not know the correct
way to determine leap year in a year ending in 00.  In fact, most of
said computers/programs/people do not know that the determination is
any different than on any other leap year.  That being the case, it is
likely that 02/29/2000 will work by default; it would be different had
it been 1900, 2100, or such.

There could possibly be problems that are related to faulty
programming, anticipating the special case for a year divisible by
400, but introducing errors in the process.  Otherwise, it is not
likely that 02/29/2000 will provide any different experiences than
would 02/29/AnyOtherLeapYear.
```

###### ↳ ↳ ↳ Re: Y2K

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<878rit$2vo$1@news.igs.net>`
- **References:** `<387DFF69.58F0CF68@gecm.com> <85r2fe$fmf$1@nnrp1.deja.com> <38974a41.3872858@news1.frb.gov>`

```
I think the biggest problem will be April fools day.  After all, the first
April fools day of the millennium, what virus writer could resist?

WDS wrote in message <38974a41.3872858@news1.frb.gov>...
>On Sun, 16 Jan 2000 00:13:42 GMT, Arthur wrote:
>
…[23 more quoted lines elided]…
>-------------------Decoy@Spammer.Trasher----------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
