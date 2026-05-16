[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FASTSRT, COBOL II, SyncSort, VSE

_41 messages · 15 participants · 2000-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "Eileen Preston" <epreston@lear.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM>`

```


>>> docdwarf@clark.net 04/01 10:47 pm >>>
 
In article <8c5t66$g3t$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <38e66554.25614639@nntp.sprynet.com>,
>infocat@sprynet.com (Frank Swarbrick) wrote:
…[6 more quoted lines elided]…
>sorts?

I have seen such things, aye.

>And, if so, why?

Oh, I *cannot* resist... perhaps because they learned how to do so
nimfty-scorg years ago and haven't learned anything new since.

DD


I was 'taught' never use an internal sort because the code wouldn't be 'structured', with 'structured' meaning an internal sort requires a GO TO after the input procedure to get to the output procedure and 'structured code' didn't have GO TOs (I don't want to start the 'go to or not to go to' war again so I'll invoke the mad man right now on the subject).  Shortly after I got into the real world I was shown how to do an internal sort with no GO TOs in it. I was also told that the technique only worked on Big Blue due to the internal archetecture of the machine (whether this was true or if it was, continues to be true today I have no idea).  However I was also 'taught' that one does not use an internal sort when 2 programs and an external sort would do because of maintenance considerations.

I think the last time I wrote a program with an internal sort was........  at least not in the last decade :)

Eileen

 


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ECF4BD.6EA6D5AB@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM>`

```
Eileen Preston wrote:
> 

> I was 'taught' never use an internal sort because the code wouldn't be 'structured', with 'structured' meaning an internal sort requires a GO TO after the input procedure to get to the output procedure and 'structured code' didn't have GO TOs (I don't want to start the 'go to or not to go to' war again so I'll invoke the mad man right now on the subject).  Shortly after I got into the real world I was shown how to do an internal sort with no GO TOs in it. 

I don't think I have ever seen a sort using a GO TO that way, I am not
sure how it would work.

> I was also told that the technique only worked on Big Blue due to the internal archetecture of the machine (whether this was true or if it was, continues to be true today I have no idea).  However I was also 'taught' that one does not use an internal sort when 2 programs and an external sort would do because of maintenance considerations.
> 
> I think the last time I wrote a program with an internal sort was........  at least not in the last decade :)
> 
> Eileen

The last time I wrote a program with an internal sort was....  this
morning.  The last time I wrote a program with an external sort was...
this morning.  Same job.

Some things are easier to write and to maintain with internal sorts,
others with external sorts.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ckhg5$bsk$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu>`

```
In article <38ECF4BD.6EA6D5AB@cusys.edu>,
  Please, do, not, e-mail, replies, post, them!! wrote:
> > I think the last time I wrote a program with an internal sort
was........  at least not in the last decade :)
> >
> > Eileen
…[4 more quoted lines elided]…
>

Hi:

I must live in some charmed(?) world. I haven't designed a system
using any internal/external sorts in 30 years. I still don't get it why
people end up using sorts in a new system.

Thanks

Tony Dilworth
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** amosgreg@my-deja.com
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl67u$37a$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com>`

```
Tony wrote
> Hi:
>
> I must live in some charmed(?) world. I haven't designed a system
> using any internal/external sorts in 30 years. I still don't get it
why
> people end up using sorts in a new system.
>
…[3 more quoted lines elided]…
>

How do you get around using a data set in 1 process and in the next
step needing the same data in a different order for other business
reasons ?

Thanks Greg


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl89l$5l2$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <8cl67u$37a$1@nnrp1.deja.com>`

```
In article <8cl67u$37a$1@nnrp1.deja.com>,
  amosgreg@my-deja.com wrote:
>
> How do you get around using a data set in 1 process and in the next
…[3 more quoted lines elided]…
> Thanks Greg

Hi:

You use the word 'step'. Does this suggest a mainframe, batch-processing
environment?

Well, I use nothing but ISAM and, when designing a complete system,
ensure that I have the keys I need to meet the requirements. I just
never come across situations such as those you mention. If a recurring
new need arose and I didn't have the key I needed, I would just add the
new key to the file, but that rarely happens in my world. Although this
might require file conversion, I don't consider that a big deal.
Certainly not a big enough deal to justify investigating other methods
(like DBMS stuff).

The trick is having foresight when designing your files. If you get
all your keys right, you won't have to do sorts and stuff.

Although there may be execution-time constraints, creating a
new ISAM file as an alternative to SORTing is definitely worth
consideration and would yield an 'enhanced' file.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 5)_

- **From:** amosgreg@my-deja.com
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8csl8l$smp$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <8cl67u$37a$1@nnrp1.deja.com> <8cl89l$5l2$1@nnrp1.deja.com>`

```
Tony wrote..
> You use the word 'step'. Does this suggest a mainframe, batch-
processing environment?


I understand what you are saying and yes a fair portion of my work has
been batch, and as such I generally don't have the luxary of being able
to develop and re-add the multiple keys necessary. I also, several
years ago, worked a conversion effort that the look-up file I was
accessing (VSAM) was pushing the 4-gig limit and was tough to optimize.
I ended up sorting it and reading the sorted file sequential with my
master file. The reason for the look-up was that I may or may not have
had a record in this particular file (Transaction file).
Because of the system and the size of the files I did not have the
resources avaliable for unlimited indexes. And again because of the
size of the files I was able to sort the files once and use them
sequentially for several different steps in the course of the
conversion.

Thanks


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cnejm$jdj$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <8cl67u$37a$1@nnrp1.deja.com>`

```
amosgreg@my-deja.com wrote in message <8cl67u$37a$1@nnrp1.deja.com>...
>Tony wrote
>> Hi:
…[15 more quoted lines elided]…
>Thanks Greg

When you are a VAR, that does not happen.  I do not use a cash register (and
the VAR PC is closer to a cash register than to an office data processing
terminal) for generalized data processing. I do the same thing, over and
over.  Record the sale, and stash it in a data base by product for
twenty-four hours. At the end of the day, dump the totals and start over.  I
hand over the data I have collected as a flat file, and exit, stage left.

While most VAR stuff is more complex than a simple cash register, the
principal is the same.  This is simply not a batch environment. It is a one
transaction at a time environment, running in real-time.  Any work that I do
on *groups* of records is incidental, like an end of day report.  The crux
of the system is to meld one record from a each of a dozen places with
incoming data to get a specific job done.  That is done over and over again.
To re-sort each of the data bases for each transaction would be mad.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EDDF03.7D56BFEC@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> I must live in some charmed(?) world. I haven't designed a system
> using any internal/external sorts in 30 years. I still don't get it why
> people end up using sorts in a new system.

Don't you create reports?  Users like reports with data sorted their way
- which may or may not be the way we store the data.  Often the sort
criteria is based upon calculated values.  Sometimes the user will want
the same report sorted different ways (by name or by number)

I also sort data before adding it to databases for efficiency sake.  I
sort user supplied tables before putting them in my COBOL table so that
I can do a SEARCH ALL.  I sort files which I will use for match-merge
logic.

What kind of systems were you designing 29 years ago that didn't have
sorted reports nor match/merge?  Heck, 29 years ago, I was using a card
sorter!!!
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8clg90$et5$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu>`

```
In article <38EDDF03.7D56BFEC@cusys.edu>,
  Please, do, not, e-mail, replies, post, them!! wrote:
> Foodman wrote:
> >
> > I must live in some charmed(?) world. I haven't designed a system
> > using any internal/external sorts in 30 years. I still don't get it
why
> > people end up using sorts in a new system.
>

> Don't you create reports?  Users like reports with data sorted their
way
> - which may or may not be the way we store the data.  Often the sort
> criteria is based upon calculated values.  Sometimes the user will
want
> the same report sorted different ways (by name or by number)


---Of course, but the reports are created from ISAM files and do
---not require sorting.

>
> I also sort data before adding it to databases for efficiency sake.

---Did this data come from some other system.  Why is the data not
---added directly to the 'database' at the time of entry or stuck
---in an ISAM file?


> I sort user supplied tables before putting them in my COBOL table so
that

---What format are the user-supplied tables? The user should put his
---stuff into an ISAM file designed for the purpose.

> I can do a SEARCH ALL.  I sort files which I will use for match-merge
> logic.
>

---Match-Merge logic went out years ago, no?  I am talking about new
---systems. MM logic implies sequential, non-indexed files (which
---would require sorts).

> What kind of systems were you designing 29 years ago that didn't have
> sorted reports nor match/merge?  Heck, 29 years ago, I was using a
card
> sorter!!!
>

Same as you. I sorted, etc. in the olden days. But I haven't used a
sort since I discovered multi-key ISAM.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE54F1.413F06B9@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8clg90$et5$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38EDDF03.7D56BFEC@cusys.edu>,
…[17 more quoted lines elided]…
> ---not require sorting.

So you create an ISAM file with the calculated data (and everything else
the report needed) just to avoid doing a sort?  This is like going
around the world to avoid crossing a hill. 

> > I also sort data before adding it to databases for efficiency sake.
> 
> ---Did this data come from some other system.  Why is the data not
> ---added directly to the 'database' at the time of entry or stuck
> ---in an ISAM file?

Because of normalization which doesn't create easily derivable data.
Because multiple indices slow update tremendously.  Because saving
calculated values in the database and updating these every time a member
field gets updated is slow.  Because all this overhead ads complexity
and risk.  

When I want an annual report sorted by average customer expenditure, it
is easy enough to calculate this average and sort the result.  It is
very expensive to maintain a system which updates the average with each
order and has this average indexed - all for this once per year report.
 
> > I sort user supplied tables before putting them in my COBOL table so
> that
> 
> ---What format are the user-supplied tables? The user should put his
> ---stuff into an ISAM file designed for the purpose.

The user provides an editable flat file.  The editor has already been
written, debugged, and paid for.  Flat files are compact and safe, they
never have index problems.  I don't need to write a different program
for each user supplied file nor to maintain one.
 
> > I can do a SEARCH ALL.  I sort files which I will use for match-merge
> > logic.
…[4 more quoted lines elided]…
> ---would require sorts).

You don't think SQL queries do match merges?

Maybe MM logic went out years ago - when COBOL went out.  But I don't
care about what is stylish among academia, I care what works.  Keep it
simple.

But seriously, I have worked in mainframe environments for a long time. 
The use of keyed files has been dropping considerably for decades.  Most
of what I see nowadays are either full fledged databases or temporary
flat files.  We extract from the database in the most efficient way and
sometimes match/merge the data with data provided from some foreign
subschema extraction.  

Sometimes I will extract data, split it into files for each customer,
sort by customer determined criteria, and report.

I sort my data by db-key before doing a database load.  The db-key isn't
even data - it's just where my field will belong.  

If you want fast access, read your record and have the next record
already in your input block.  If you want slow access, read your record
then look up to see where the next record is then access the disk again
to find the next record.  
 
If you want to keep systems people employed, make sure to add a lot of
permanent links, keys, and other overhead.  If you want to spend that
money providing results for your users, keep the system simple and
clean.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cndig$iqd$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8clg90$et5$1@nnrp1.deja.com> <38EE54F1.413F06B9@cusys.edu>`

```
Howard Brazee wrote in message

>If you want fast access, read your record and have the next record
>already in your input block.  If you want slow access, read your record
…[6 more quoted lines elided]…
>clean.

I really tend to agree with what Bill said several posts back, but what you
are saying here really brings it out.

The difference is mainframe versus PC, but also head office processing of
major amounts of historical data, compared to local editing of input data.

If I have a truck pull onto a weigh scale, I have to weight the truck, find
out what they are hauling, tie it to a PO, check where it has to be
delivered and produce BOL, customs papers, delivery instructions, a map,
then generate data to pay the trucker and bill the customer, I really do not
have time to sort anything.  The motor is running in the truck, and there is
a line up behind him of twenty more trucks.

At your end, you want to produce one twenty page report involving thousands
of similar records.  At my end, I want to produce twenty one page reports
involving 25 records, each from a different data source.  It is not really
very surprising that we decide the data should be organized differently.

To reiterate:

>If you want fast access, read your record and have the next record
>already in your input block.  If you want slow access, read your record
>then look up to see where the next record is then access the disk again
>to find the next record.

Only if you are processing two records.  If you are processing one record
from that file, then going on to do the same thing from another set of
records, and then a third thing from a third set of records, sorts suck.
Isam/DBMS is the only way to go.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl44h$7r5$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu>`

```
Howard Brazee wrote in message <38EDDF03.7D56BFEC@cusys.edu>...
>Foodman wrote:
>>
…[7 more quoted lines elided]…
>the same report sorted different ways (by name or by number)

It is a file size thing, Howard.  History files on my systems, for example,
often are keyed under five or six keys.  Granted, I have indices that are
larger than the data files in some cases, but for a file of a couple megs or
so, that is an efficient and easy way to store them.  It has the advantage
that the same access methods can be used online as well as for reports.  For
example, a simple customer file might be keyed on customer number, an
alphabetic code, a postal code, and a date last used.  For a small base, say
under 10,000 customers, resorting it all the time just adds complexity.


>
>I also sort data before adding it to databases for efficiency sake.  I
…[6 more quoted lines elided]…
>sorter!!!
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 5)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net>`

```
In article <8cl44h$7r5$1@news.igs.net>, donald tees
<donald@willmack.com> writes
>Howard Brazee wrote in message <38EDDF03.7D56BFEC@cusys.edu>...
>It is a file size thing, Howard.  History files on my systems, for example,
…[7 more quoted lines elided]…
>
One system I worked on had twenty+ indices. The problem was that the
overnight run to re-allocate products across different groups took 48 +
hours to run. Multiple indices brought their own problems which I had to
resolve in batch using (wait for it!) Sorts....  ;-)
I now try to avoid non-essential multiple indices.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 6)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u1etZ6Mo$GA.361@cpmsnbbsa04>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk>`

```

Alistair Maclean <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk...
> One system I worked on had twenty+ indices. The problem was that the
> overnight run to re-allocate products across different groups took
48 +
> hours to run. Multiple indices brought their own problems which I
had to
> resolve in batch using (wait for it!) Sorts....  ;-)
> I now try to avoid non-essential multiple indices.
> --
I used to use the "25 hour daily Job" as a bad case scenario, I guess
I'll have to amend it.

I don't mind when people overload a file with alternate indexes, and
then use them to access the entire file.
It's easy money for me, when I rewrite it.

In one case I took a 15 hour process (3 runs at 5hrs. each), and got
it down to 15 minutes.
The slick programmer who wrote it really painted himself into a
corner.
Never heard of: Extract, Sort, Print.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 6)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1FB82.FCD7D717@iinet.net.au>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk>`

```

Alistair Maclean wrote:
> 
> One system I worked on had twenty+ indices. The problem was that the
…[3 more quoted lines elided]…
> I now try to avoid non-essential multiple indices.

Have you people never found out about relational databases?

By the way Alistair, did you know that !@%$#* Netscape Navigator message spell
checker wants to replace your name with Alligator!
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 7)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3mzrGAGUh84Ewpw@ld50macca.demon.co.uk>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk> <38F1FB82.FCD7D717@iinet.net.au>`

```
In article <38F1FB82.FCD7D717@iinet.net.au>, Joseph Katnic
<josephk@iinet.net.au> writes
>
>Alistair Maclean wrote:
…[10 more quoted lines elided]…
>checker wants to replace your name with Alligator!
I guess that's why I get a bit crotchety at times, and Maclean comes
back as Maculae from Word for Windows.
>
>--
>Joe Katnic     josephk@iinet.net.au
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 7)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CFPI4.3440$_H2.102485@news.swbell.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk> <38F1FB82.FCD7D717@iinet.net.au>`

```

Joseph Katnic <josephk@iinet.net.au
>
> By the way Alistair, did you know that !@%$#* Netscape Navigator
message spell
> checker wants to replace your name with Alligator!

You should really use Internet Explorer. It probably won't spell-check
any better, but at least you'd have a Microsoft product.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 8)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F47459.B1735815@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <+XZ7TBAk2h74EwW$@ld50macca.demon.co.uk> <38F1FB82.FCD7D717@iinet.net.au> <CFPI4.3440$_H2.102485@news.swbell.net>`

```
Jerry P wrote:
> 
> Joseph Katnic <josephk@iinet.net.au
…[6 more quoted lines elided]…
> any better, but at least you'd have a Microsoft product.

Why is that a meaningful criterion in determining which product to use?
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE2152.CA6B4960@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net>`

```


donald tees wrote:
> 
> Howard Brazee wrote in message <38EDDF03.7D56BFEC@cusys.edu>...
…[18 more quoted lines elided]…
> under 10,000 customers, resorting it all the time just adds complexity.

Couldn't disagree more.

Most of my data are in databases.  We don't try to anticipate every way
it will be accessed and pre-sort the data with indices.  This is way too
expensive and adds complications which make maintenance more expensive. 
Sorting it for a particular use just decreases complexity over having a
permanent index in a file which needs to be updated frequently.   Sorts
are simple and go away.  Indices are complex and stick around. 

But even still, I will be asked to produce a report sorted by calculated
results.  These are fields which only exist during the run of the job. 
I suppose I could create an indexed file with my data, read the indexed
file back in, and then delete that file.   But that is sorting by
another name.  I have seen it where a company did not own sort software,
but it was expensive and slow compared to a sort.  

What do you do when you need to output sorted data from calculated
results?
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE2E1C.FD28CA55@home.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu>`

```


Howard Brazee wrote:
> 
> donald tees wrote:
…[3 more quoted lines elided]…
> results?

Produce one file with results keyed on alternate keys. Why keep
re-sorting every time the user back-tracks and asks for a fresh print of
the report ? 

I DON't disagree with sorting - you have to weigh up the pros and cons
as part of overall systems design.

In PC-land or VAR-land speed is determined so often by user input;
without any detrimental effect this allows you to update several files
from one screen transaction. E.g. POS systems - print bill, take
customer's money and in background update the indexed inventory file.
This update concept applies equally to the big chains, the individual
POS terminals feeding into a back office computer. Data from that is
sucked into the Head Office computer overnight.

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE383E.4A97B44F@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com>`

```


"James J. Gavan" wrote:
> 
> Howard Brazee wrote:
…[9 more quoted lines elided]…
> the report ?

Sorting is cheap.  The overhead of keeping rarely used files and indices
is much more costly and complicated.

Indices can really add overhead in any update process.  Indices can add
complexity to any process.  I don't believe in carrying a bunch of
baggage which may only be used occasionally and which can bring down
what I use all the time.  I am a big advocate of simplicity.

If an index is just an expensive way of doing a sort, it is being
misused.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8clf3s$827$1@slb2.atl.mindspring.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:38EE383E.4A97B44F@cusys.edu...
>
>
…[23 more quoted lines elided]…
> misused.

Knowing fairly well both IBM mainframes and PC COBOLs, I think that this view
(expressed by Howard) is much more common on the IBM mainframe then on the
PC. The VSAM multiple indices overhead (especially with 100,000+ records)
seems much more "resource intensive" (especially if you use the IBM COBOL
AIXBLD facility) than comparable (usually smaller) PC multiple indices.

This is a HUGE generalization, but it is my perception of the two different
environments.  (Along with the fact that most IBM mainframe COBOL
environments still have "heavy" batch nightly runs - while PCs "generally"
are quicker/easier - or actually done on the mainframe <G>)
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 9)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#Z8GtYPo$GA.236@cpmsnbbsa03>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <8clf3s$827$1@slb2.atl.mindspring.net>`

```
I agree with your assessment.
We are not just talking "apples and oranges" here,
we are talking "apples and elephants".

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8clf3s$827$1@slb2.atl.mindspring.net...
>
> Knowing fairly well both IBM mainframes and PC COBOLs, I think that
this view
> (expressed by Howard) is much more common on the IBM mainframe then
on the
> PC. The VSAM multiple indices overhead (especially with 100,000+
records)
> seems much more "resource intensive" (especially if you use the IBM
COBOL
> AIXBLD facility) than comparable (usually smaller) PC multiple
indices.

I have worked on a system with over 10 million customer records.
The system was segmented into sub-systems with around 1 million
customers each.
There was a single CICS system which processed all 12 sub-systems.
Suggesting adding alternate indexes could get you hurt really bad.
Beaten to a bloody pulp (by the women in the group).

Other systems had monthly volumes of over 100 million transactions.

The methods we use are determined by the volume of the data, and the
platform.
What I would do to process 5,000 records, may be inappropriate for 100
million records.

> This is a HUGE generalization, but it is my perception of the two
different
> environments.  (Along with the fact that most IBM mainframe COBOL
> environments still have "heavy" batch nightly runs - while PCs
"generally"
> are quicker/easier - or actually done on the mainframe <G>)
>
I think we all have to look at the environments which support COBOL.
From the desktop to the mainframe, each can employ methods which are
inappropriate in another environment. We just have to accept the
differences, and maybe learn from the perspectives of others.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE7A33.13504284@home.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <8clf3s$827$1@slb2.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
…[38 more quoted lines elided]…
> 
Bill,

You point is well made. If I've learned anything in this NG it is that
there is a vast chasm on file handling between mainframes and PCs, to
the extent that Windows does it for you on PCs, those mainframe O/S's
also seem to be offering features for the 'big' world.

As I originally wrote to Howard, '... how you do it is part of the
overall system design concept'. There's no sure fire answer whether
mainframe or PC. The list can get pretty endless, the commercial
organization you are working for, their needs, your tools and the
hardware.

Go back to ye olden dayse - NCR CRAM and RCA MCF - we had the latter.
It worked fine electronically, but physically whipping the mag cards out
of a container down a tramway, figure-of-eight around the read/write
drum, then tally-ho back along the tramway - home sweet home. The
physical bit would go GERPLUNK -  and cards got ripped !

Our systems thinking, we could get all customers on, say 100-150  cards
and our products (3,600 of them) on ONE card. We took input transactions
and sorted them on mag tape (a) by customer then (b) by product - with
the latter we just kept that one product card zipping around the
read/write head.

Same system to-day - an entirely different baby because of hardware. No
centralized key-punching on to paper tape - instead three or four PCs at 
each of the 60 distribution points; even better if we could justify
giving each salesman a hand-held computer to feed-in his orders. Even
invoices could be printed locally. The mainframe, take already sorted
data by account from depots and update Sales Ledger(A/R).

Jeez I'd love to have a crack at that system again - it was my most fun
time in computing. (Besides which Bridgette Bardot was only a sultry
18/20-year old. And as for Sophia - yummy, yummy <G>). Still, mustn't
forget, my wife was a real sweetheart too !

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 9)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135a84e1fd74d0179896cc@news.freedombird.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <8clf3s$827$1@slb2.atl.mindspring.net>`

```
I noticed that William M. Klein as wmklein@nospam.ix.netcom.com said...
> 
> This is a HUGE generalization, but it is my perception of the two different
> environments.  (Along with the fact that most IBM mainframe COBOL
> environments still have "heavy" batch nightly runs - while PCs "generally"
> are quicker/easier - or actually done on the mainframe <G>)

<g>
How and when data is sorted or not does seem to be very much environment 
based.  For instance, internal sorting is hardly ever used on mainframe 
systems and the number of discussions about whether or not to use a 
bubble sort are few and far between.

Sorting files in a mainframe batch process is almost compulsory - I've 
seen long batch jobs where one out of three steps is an execution of the 
excellent sort utility.  Also the sort utility has exits which can be 
used for basic extraction and manipulation, while the sort provides 
control counts on the way.

On PC-type systems, maybe because they don't come with a decent sort 
utility, and maybe because formal CS education teaches sorting 
techniques, sorting data within an applications program is more or less 
the norm.  I don't really know, I haven't done anything much in Windows 
programming[*] but these are just some of my impressions of the 
differences.

[*] I'll soon have a bit of time to get to grips with Windows 
programming - I'm presently armed with a Fujitsu CD, some C/C++ tools 
and the Charles Petzold book on Windows programming.  My inclination is 
to go with the book first so as to gain some fundamental knowledge, but 
can anyone say whether or not this is a worthwhile approach?
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F15055.93C3FD77@home.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <8clf3s$827$1@slb2.atl.mindspring.net> <MPG.135a84e1fd74d0179896cc@news.freedombird.net>`

```


Charles F Hankel wrote:
> 
> 
…[4 more quoted lines elided]…
> can anyone say whether or not this is a worthwhile approach?

Charles,

I'm assuming you are already comfortable with C++ (which I'm not <G>).
And again my 'take' is that you want to do your own thing rather than
perhaps use SP2 or ScreenIO with Fujitsu ?

If as stated, go with Petzold's latest book. I have very few books on C
but a really comprehensive 'Bible' on C - event highlights where M/S
have made boob boobs in Windows :-

Win32 Programmming - Brent E.Rector & Joseph M. Newcomer - 1996
Addison Wesley Longman Inc. ISBN 0-201-63492-9 . (Hopefully they've done
an update in C++ which you would be more interested in).

If however you want a quickie into Windowing then make a choice going
the SP2 or ScreenIO route.

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 11)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135d2652fa92ea9e9896df@news.freedombird.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <8clf3s$827$1@slb2.atl.mindspring.net> <MPG.135a84e1fd74d0179896cc@news.freedombird.net> <38F15055.93C3FD77@home.com>`

```
I noticed that James J. Gavan as jjgavan@home.com said...
> 
> Charles F Hankel wrote:
…[22 more quoted lines elided]…
> the SP2 or ScreenIO route.

It's an idea.  I tend to want to know a lot more about the system than 
just a quick entry thing - somehow it puts the programming into context 
more than, say, a quick Visual Basic of Delphi window process.  I notice 
that the Petzold book relies a lot on C knowledge but it seems to me 
that there are fundamentals in there that cross the language barriers.

I'm leaning towards the book route at the moment and will happily come 
back to quick tools once I'm more au fait with the overall environment.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE6C2D.5C295F07@home.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu>`

```


Howard Brazee wrote:
> 
> "James J. Gavan" wrote:
…[20 more quoted lines elided]…
> 

Sorting maybe cheap - but not necessarily when associated with
calculating which determines sequences for printing. But you miss the
point because your mindset is on number crunching :-

Run 1 - do calculations reading sequentially then generate indexed file
with print sequences.

Run 2 - user realizes he missed or entered incorrect data and changes 3
records out of a 1,000. Run 2 re-calculates for the 3 records only and
regenerates indexed output

Run 3 - Having done the calculations and reports in Imperial - Amoco
Canada (I don't know why) - specifically ask for a copy of the
information in Metric. I take the same calculated index file and merely
convert to Metric.

Run 4 - now I'll throw a zinger at you - having done Run 1 or Run 2 the
user goes into the data file for display. Now he would like to see a
graph associated with those calculations (Calcualte/Sort every time he
wants a graph ?) Additionally in the Viewing program he may stipulate
"Only show me those items where the loss is greater than xxx mills -
again categorized and stored in the calculation indexed file.

(Printing Reports - run through a large file sequentially to recalculate
and then sort to get desired sequence every time you want to print
??????)

> If an index is just an expensive way of doing a sort, it is being
> misused.

And that Howard is YOUR VIEW - Not everybody else's !

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 9)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EE9741.FC261AC3@zip.com.au>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <38EE6C2D.5C295F07@home.com>`

```
"James J. Gavan" wrote:
> 
> > If an index is just an expensive way of doing a sort, it is being
> > misused.
> 
> And that Howard is YOUR VIEW - Not everybody else's !

I agree with you position, and I agree with Howard's.  The bottom line
is that trade off's are made in every system.  These are different in
each case.

Great argument on the indexing side.  This is a good use of indexing,
however Howard is right, too much indexing costs a lot of time in the
online.   Testing is the only real measure.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 10)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1D95F.4BEED1AF@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <38EE6C2D.5C295F07@home.com> <38EE9741.FC261AC3@zip.com.au>`

```
Ken Foskey wrote:
> 
> I agree with you position, and I agree with Howard's.  The bottom line
…[5 more quoted lines elided]…
> online.   Testing is the only real measure.

James basically said that sorting is obsolete.  In response, I didn't
quite say that indexed files is obsolete (only that databases are taking
over this function).  But I know from experience that I had better not
assume obsolescence in a programming technique.

His ideas of simplicity is to extract your data into a file, to keep it
around adding indices whenever the user asks for a slightly different
report.

My idea of simplicity is to make any such file temporary, re-extracting
the data if the user wants a slightly different report.  

From these, one would guess that I was using a PC and had to manage all
of my files personally, and he had the mainframe with other people
purging the files after a given amount of time.  But the reverse is
true.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F7E3BA.90A8ACEA@home.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <38EE6C2D.5C295F07@home.com> <38EE9741.FC261AC3@zip.com.au> <38F1D95F.4BEED1AF@cusys.edu>`

```


Howard Brazee wrote:
> 
> Ken Foskey wrote:
…[24 more quoted lines elided]…
> true.

Howard,

Now you've got me jumping up and down like Pete Dashwood; if I don't
quote him verbatim he throws on his Horace Rumpole outfit and does a G &
S operetta :-)

I'm afraid you misconstrued what I said - possibly because the 'major
attack' was from the other geriatric - Mr. Dilworth. In no sense do I
say sorts are obsolete - the many messages in this thread with examples
make a strong case for using DBs and Sorting. I would gauge the same
applies to the Unix world because of multi-user.

Back in '60s we sorted even though we had that MCF unit and used less
than 10% of its capacity (3 billion I think from memory), for invoice
printing. Same goes with department store group - a million credit
customers - again a lot of sorting on an ICL 1900 mainframe.

PCs are slightly different - or at least stand-alones are. Review what
Don Tees said about queuing up those vehicles at a checkpoint to weigh
contents and get them through the hoop as quickly as possible.

Same goes for my application - handles a lot of data in total (have no
idea of total volumes, and they aren't relevant) - but each process
(Corporation/Gas Plant) is small potatoes, laughable size compared to
your mainframe volumes. That calculation file I mentioned - just checked
out a couple - not much more than 1 KB per file. So zip all 7 files per
process and there's little to store. (Note : I can re-print reports in
some 10 minutes as opposed to recalculating 15 mins., followed by
another 10 for printing).

The nature of PCs has tended to create its own approach. As an end user
I get irritated when loading Netscape to get in here (CLC) - certainly
takes way less than a minute - but to me observing, it seems to take
forever before it loads. So much of this Windows stuff is instant.
For the small amount of book-keeping I do, I use Quickbooks - one file
containing all my data for one company. Enter a transaction - flip to
Balance Sheet or P & L - pause to specify the period time frame - and
Boom! it displays at you what it will also print - very impressive.
(It's obvious Intuit must be using a DB engine - I'm not even obligated
to use Chart-of-Account Numbers - just descriptions).

Don't know what Tony Dilworth's POS systems are aimed at, but take a Mom
and Pop Liquor Store. A bit like Don's system, it is queue sensitive,
(people arriving to buy booze). Unlike the chains, the owner has to play
it lean and mean to keep his cash flow healthy - very often they will
stock to a minimum. Given two PCs - he can use one as the register and
meanwhile the other for enquiries - How am I in stock for whiskey/rye ?
He can query instantly without resorting to updates/sorts - jumps in his
vehicle and goes and picks up several cases. Not the nice sophisticated
approach of the chains - but that's the way many operate. And he is only
able to do this because he doesn't sort but uses indices to update.

Yes, use sorts and DBs on mainframes, but there is a case for PrimeKey
indexing on PCs, (go easy on alternate keys though). Volumes are
starting to get large on a PC ? - then you are veering towards something
like Unix anyway.

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 12)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FB18C4.4313FCB2@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <38EE6C2D.5C295F07@home.com> <38EE9741.FC261AC3@zip.com.au> <38F1D95F.4BEED1AF@cusys.edu> <38F7E3BA.90A8ACEA@home.com>`

```
"James J. Gavan" wrote:
> 
> Yes, use sorts and DBs on mainframes, but there is a case for PrimeKey
> indexing on PCs, (go easy on alternate keys though). Volumes are
> starting to get large on a PC ? - then you are veering towards something
> like Unix anyway.

There's a case for PrimeKey indexing on all systems.  But as with any
choice, there is a cost either way.  I agree that each added index adds
complexity and slows down updates.  I suspect that on a PC, the slow
down in producing a sorted report is not as significant as on mainframes
(unless the user is sitting there with his hand on his mouse).

But let me recap.
Original statement was something like this:
Sorts are obsolete, you can always add an index to get the data in the
right order.

To which I replied:
If the only reason for an index is to be an expensive sort, that index
is being misused.

I have seen it misused/used even in a mainframe environment where sorts
were not available.  And of course, most any application which uses the
index to retrieve a selected record is NOT misusing the index.  If you
have a reason to have the file indexed on the desired key, of course,
you use it to get your sorted data.  But when you want the data in a
different order (possibly by a calculated field which isn't even on the
file), the better tool is a sort utility.  (better than creating a new
index, and certainly better than creating a new file with that
calculated field, and then adding the index to that field - to simply
read in again to create your report!)

On the other hand, if your run-time environment includes some kind of
ISAM support, but no sort support, I can understand why you would pick
the option which is already paid for, making a simpler deliverable. 
Sometimes, you just can't persuade a customer that he needs to purchase
the right tool to make your product work best.   One advantage of
working with mainframes is that we can safely assume that all of our
customers have a decent sort utility (which all work pretty much the
same way).
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1D691.761E7FE5@cusys.edu>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu> <38EE2E1C.FD28CA55@home.com> <38EE383E.4A97B44F@cusys.edu> <38EE6C2D.5C295F07@home.com>`

```


"James J. Gavan" wrote:
> 
> Howard Brazee wrote:
…[33 more quoted lines elided]…
> regenerates indexed output

So you're saying it is cheaper to keep the file for unforeseen changes
than to re-extract.  I think keeping track of such files and deciding
when to purge them is more work than running the extract again.

> Run 3 - Having done the calculations and reports in Imperial - Amoco
> Canada (I don't know why) - specifically ask for a copy of the
> information in Metric. I take the same calculated index file and merely
> convert to Metric.

That doesn't change the sort order, but again I prefer extracting again
rather than keep redundant files lying around.
 
> Run 4 - now I'll throw a zinger at you - having done Run 1 or Run 2 the
> user goes into the data file for display. Now he would like to see a
…[3 more quoted lines elided]…
> again categorized and stored in the calculation indexed file.

If he's going to play with the results, put the data into a warehouse, a
spreadsheet, or whatever.  Let HIM sort it.  In that case, you don't
need that index either.
 
> (Printing Reports - run through a large file sequentially to recalculate
> and then sort to get desired sequence every time you want to print
> ??????)

VS saving a large file just in case someone wants a report they didn't
ask for, then adding an index to sort the file, and then running the
report again.  Is adding that index cheaper than sorting?  Is keeping
that file cheaper than re-extracting?
 
> > If an index is just an expensive way of doing a sort, it is being
> > misused.
> 
> And that Howard is YOUR VIEW - Not everybody else's !

Now whose view do you EXPECT me to state?

But "if an index is just an expensive way of doing a sort" - why do you
think it isn't being misused?  
 
> Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cnca4$i6f$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu> <8cl44h$7r5$1@news.igs.net> <38EE2152.CA6B4960@cusys.edu>`

```

Howard Brazee wrote in message <38EE2152.CA6B4960@cusys.edu>...
>
>
…[6 more quoted lines elided]…
>> >> using any internal/external sorts in 30 years. I still don't get it
why
>> >> people end up using sorts in a new system.
>> >
…[5 more quoted lines elided]…
>> It is a file size thing, Howard.  History files on my systems, for
example,
>> often are keyed under five or six keys.  Granted, I have indices that are
>> larger than the data files in some cases, but for a file of a couple megs
or
>> so, that is an efficient and easy way to store them.  It has the
advantage
>> that the same access methods can be used online as well as for reports.
For
>> example, a simple customer file might be keyed on customer number, an
>> alphabetic code, a postal code, and a date last used.  For a small base,
say
>> under 10,000 customers, resorting it all the time just adds complexity.
>
…[17 more quoted lines elided]…
>results?

I don't deal with "results".  I deal with original data, coming in one
transaction at a time.  I normally have to check that data against several
dozen factors, but my systems tend to be much closer to designing an ATM
than to balancing the books at the other end.

When I say "history", I am talking much closer to "audit trail" than to the
type of historical data that you would be talking about at the data
processing end ... which was the real point of the file size statement.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1FA9A.E2F9ACD4@iinet.net.au>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <38EDDF03.7D56BFEC@cusys.edu>`

```

Howard Brazee wrote:
> 
> Foodman wrote:
…[9 more quoted lines elided]…
> 
God Damned Users get what I give em and like it!
Besides they never liked choices anyway! :)
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl3pg$7i6$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com>`

```
Foodman wrote in message <8ckhg5$bsk$1@nnrp1.deja.com>...

>I must live in some charmed(?) world. I haven't designed a system
>using any internal/external sorts in 30 years. I still don't get it why
…[5 more quoted lines elided]…
>
I would say you were living in a VAR world.  While I agree that most systems
do not need them, I have seen lots of systems that did. In a large batch
environment (files being processed with a million records and up, for
example), a sort and a sequential pass are by far the most efficient.

In the VAR environment, which I am also in, it is almost always more
efficient to simply keep the data in ISAM files or in a DBS. The files tend
to be quite small, even for very large companies, simply because you are
almost always working in a niche. While I do work for companies that all
tend to be several billion per year net companies, I seldom process a file
of even a gig, simply because as a VAR, my data is normally spread out over
thirty or fourty computers in an organization.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d1nse$8r9$1@nnrp1.deja.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <8cl3pg$7i6$1@news.igs.net>`

```
In article <8cl3pg$7i6$1@news.igs.net>,
  "donald tees" <donald@willmack.com> wrote:
> >
> I would say you were living in a VAR world

Hi:

To me a VAR is a Value-Added-Reseller which doesn't sound
like what you are. What is your definition of VAR?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d1ta2$si1$1@news.igs.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu> <8ckhg5$bsk$1@nnrp1.deja.com> <8cl3pg$7i6$1@news.igs.net> <8d1nse$8r9$1@nnrp1.deja.com>`

```
The same.

Foodman wrote in message <8d1nse$8r9$1@nnrp1.deja.com>...
>In article <8cl3pg$7i6$1@news.igs.net>,
>  "donald tees" <donald@willmack.com> wrote:
…[15 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8coq2r0u8p@enews1.newsguy.com>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <38ECF4BD.6EA6D5AB@cusys.edu>`

```
This is very true.  The nice thing about external sorts is that you can see
the unsorted dataset in the JCL.  This makes it somewhat easier to debug and
maintain.  If there is no reason I'd want to see the unsorted dataset and
the logic is simple, then an internal sort will do just fine thank you.

Jeff

----------


>
> The last time I wrote a program with an internal sort was....  this
…[4 more quoted lines elided]…
> others with external sorts.
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%BbH4.49163$QJ3.4955022@dfiatx1-snr1.gtei.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM>`

```
Eileen Preston <epreston@lear.com> wrote in message
news:s8ecb3a9.032@UTAEMAIL.UTA.COM...
> However I was also 'taught' that one does not use an internal sort when 2
programs and an external sort would >do because of maintenance
considerations.


Then thou, madam, was taughteth by wimps. Real Men, er, Real Programmers
aren't afraid of internal sorts.

MCM
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1357b27ed7dff2289896b7@news.freedombird.net>`
- **References:** `<s8ecb3a9.032@UTAEMAIL.UTA.COM> <%BbH4.49163$QJ3.4955022@dfiatx1-snr1.gtei.net>`

```
I noticed that Michael Mattias as michael.mattias@gte.net said...
> Eileen Preston <epreston@lear.com> wrote in message
> news:s8ecb3a9.032@UTAEMAIL.UTA.COM...
…[5 more quoted lines elided]…
> aren't afraid of internal sorts.

Nor are they afraid of E15 and E35.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
