[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Report help

_9 messages · 5 participants · 2006-11_

---

### Report help

- **From:** jeff@sum-it.com
- **Date:** 2006-11-21T06:58:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com>`

```
Does anybody have a good routine I can use to calculate 50 days prior
to todays-date. This will be used for an AR report and I want to be
able to list accounts that have balances over 50 days.
```

#### ↳ Re: Report help

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-11-21T08:14:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<po56m2t4phohs3s0jua9p4spvcklcriagj@4ax.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com>`

```
On 21 Nov 2006 06:58:01 -0800, jeff@sum-it.com wrote:

>Does anybody have a good routine I can use to calculate 50 days prior
>to todays-date. This will be used for an AR report and I want to be
>able to list accounts that have balances over 50 days.

Sure.   Check out FUNCTION DATE-OF-INTEGER & FUNCTION INTEGER-OF-DATE
```

##### ↳ ↳ Re: Report help

- **From:** jeff@sum-it.com
- **Date:** 2006-11-21T10:42:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1164134553.790329.195610@m7g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<po56m2t4phohs3s0jua9p4spvcklcriagj@4ax.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com> <po56m2t4phohs3s0jua9p4spvcklcriagj@4ax.com>`

```
Thanks, I have other programs that use it.


Howard Brazee wrote:
> On 21 Nov 2006 06:58:01 -0800, jeff@sum-it.com wrote:
>
…[4 more quoted lines elided]…
> Sure.   Check out FUNCTION DATE-OF-INTEGER & FUNCTION INTEGER-OF-DATE
```

#### ↳ Re: Report help

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2006-11-22T13:33:13+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4shk6cF100l98U1@mid.individual.net>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com>`

```

<jeff@sum-it.com> wrote in message 
news:1164121081.814164.145560@k70g2000cwa.googlegroups.com...
> Does anybody have a good routine I can use to calculate 50 days prior
> to todays-date. This will be used for an AR report and I want to be
> able to list accounts that have balances over 50 days.
>

Compute 50daysAgo =  function DATE-OF-INTEGER (function INTEGER-OF-DATE 
(CURRENT-DATE) - 50))

... or something like that.

(If you don't state what platform/compiler you have, you make it hard to 
help you...)

If the above doesn't work (and I haven't tried it), you might consider 
checking the documentation for your platform...look for COBOL FUNCTIONS, 
INTEGER-OF-DATE, DATE-OF-INTEGER, CURRENT-DATE, etc.

If you don't have functions, and can't get a Julian date, you will need to 
calculate your own integer of date (or maybe get it from whatever OS you are 
running).  You COULD calculate the number of days since December 31st, 1899 
(useful, because the 1st of January, 1900 was a Monday and NOT a leap year) 
or you could simply calculate it from the beginning of the year previous to 
the current year.  (Assuming you will never want to do arithmetic on dates 
older than (365.25 + days this year) ago) Once you have the facility to 
convert dates into numbers you can calculate with, the rest is downhill.

Hopefully, this exercise will persuade you to think about things and do some 
homework... :-)

Pete.
```

#### ↳ Re: Report help

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-11-21T18:52:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b73d$45639f43$454920f8$1954@KNOLOGY.NET>`
- **In-Reply-To:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com>`

```
jeff@sum-it.com wrote:
> Does anybody have a good routine I can use to calculate 50 days prior
> to todays-date. This will be used for an AR report and I want to be
> able to list accounts that have balances over 50 days.
> 

You've gotten some COBOL replies on this.  You might also see if however 
you're pulling the data can be constrained (i.e., including a date in a 
SQL "where" clause).  That way, you're only addressing the data you 
need, instead of going through a lot of data and only processing certain 
entries.
```

##### ↳ ↳ Re: Report help

- **From:** docdwarf@panix.com ()
- **Date:** 2006-11-22T01:58:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ek0asg$3sa$1@reader2.panix.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com> <8b73d$45639f43$454920f8$1954@KNOLOGY.NET>`

```
In article <8b73d$45639f43$454920f8$1954@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>jeff@sum-it.com wrote:
>> Does anybody have a good routine I can use to calculate 50 days prior
…[6 more quoted lines elided]…
>SQL "where" clause).

This is something that I'm teaching my Tech Lead on my present contract.  
While I make sure the Olde Stuffe keeps running he's learning PeopleSoft 
and SQL for the first time in a 12-year-or-so COBOL career... one of the 
things I pointed out was that in a COBOL program one quite often first 
gets a record and then applies the edits... all right, now I've got data, 
let me see if it matches the conditions for processing.

It may be useful, on the other hand, to think of SQL as establishing the 
conditions first and *then* getting the data which satisfy them... oh, and 
you have to learn to read the queries from the inside outwards, as well.

DD
```

###### ↳ ↳ ↳ Re: Report help

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-11-21T20:30:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbf33$4563b644$454920f8$9762@KNOLOGY.NET>`
- **In-Reply-To:** `<ek0asg$3sa$1@reader2.panix.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com> <8b73d$45639f43$454920f8$1954@KNOLOGY.NET> <ek0asg$3sa$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8b73d$45639f43$454920f8$1954@KNOLOGY.NET>,
> LX-i  <lxi0007@netscape.net> wrote:
…[13 more quoted lines elided]…
> you have to learn to read the queries from the inside outwards, as well.

This is a true story from our last major project (AKA "schema change" 
for our network database schema).  We implemented some relational tables 
to hold reference data.  Several programs used to read all the network 
records in a particular set, create an indexed file, then read it back 
sorted.  This was one of the groups of data we moved to the relational side.

A couple of years later, one of the programmers in my then-office was 
reviewing a change, and trying to figure out why this particular program 
took so long to run.  What they had basically done was implemented the 
same process from the network side, but from the relational side.  And, 
instead of opening a cursor and reading it like that, they did 
repetitive singleton selects of the form

select [stuff] from [table]
where [key] =
   (select min([key]) from [table]
    where [key] not < [previous-key])

(because, of course, cursors *have* to be less efficient - we have to 
prepare the statement, then allocate the cursors, then open them, then 
do all those fetches...)

Replaced the whole thing with an ordered cursor, and the transaction 
came back almost before you pressed the Xmit key.  :)

Of course, this anecdote illustrates your point - it is a different way 
of thinking about retrieving data.  :)
```

###### ↳ ↳ ↳ Re: Report help

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-11-22T10:11:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ek17op$7a9$1@reader2.panix.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com> <8b73d$45639f43$454920f8$1954@KNOLOGY.NET> <ek0asg$3sa$1@reader2.panix.com> <dbf33$4563b644$454920f8$9762@KNOLOGY.NET>`

```
In article <dbf33$4563b644$454920f8$9762@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>> In article <8b73d$45639f43$454920f8$1954@KNOLOGY.NET>,
…[3 more quoted lines elided]…
>>> SQL "where" clause).

[snip]

>> It may be useful, on the other hand, to think of SQL as establishing the 
>> conditions first and *then* getting the data which satisfy them... oh, and 
>> you have to learn to read the queries from the inside outwards, as well.

[snip]

>(because, of course, cursors *have* to be less efficient - we have to 
>prepare the statement, then allocate the cursors, then open them, then 
…[3 more quoted lines elided]…
>came back almost before you pressed the Xmit key.  :)

Well... I recall a classic DB2 Tech Interview question from... oh, about 
twenty years ago, almost... something along the lines of 'What do you have 
to look out for during cursor processing?'; the expected response was 
'keeping it open so you keep your place and 'cursor drag' on system 
resources'... given the state of processing back then it was something to 
worry about, I guess, along with keeping all your flags as single 
characters.

>
>Of course, this anecdote illustrates your point - it is a different way 
>of thinking about retrieving data.  :)

'What do you MEAN, the problem isn't a nail?'

DD
```

###### ↳ ↳ ↳ Re: Report help

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-11-22T08:57:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pls8m2dle9rs4qupg53sm4ierrmnvv5t67@4ax.com>`
- **References:** `<1164121081.814164.145560@k70g2000cwa.googlegroups.com> <8b73d$45639f43$454920f8$1954@KNOLOGY.NET> <ek0asg$3sa$1@reader2.panix.com> <dbf33$4563b644$454920f8$9762@KNOLOGY.NET> <ek17op$7a9$1@reader2.panix.com>`

```
On Wed, 22 Nov 2006 10:11:37 +0000 (UTC), docdwarf@panix.com () wrote:

>'What do you MEAN, the problem isn't a nail?'

Now I'm humming some Peter, Paul, and Mary...   (actually Pete Seeger)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
