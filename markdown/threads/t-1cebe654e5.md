[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ProCobol Outer join

_15 messages · 5 participants · 2008-05_

---

### ProCobol Outer join

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-08T06:58:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com>`

```
I am having a problem with a left outer join when I add conditionals.

Select
        A. vehicle,
        B.Vehicle,
        B.acct,
        B.MOYR,
        B.Trancode
 from  Table1 A, Table2 B
 where A.vehicle=B.vehicle(+)
  and   B.acct='1234'
  and   B.MOYR = '0502'
  and  B.trancode='80'
  order by a.vehicle

I need all a.vehicles for all vehicles to come back in the cursor
regardless. Any ideas?
```

#### ↳ Re: ProCobol Outer join

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-05-08T09:24:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com>`

```
"jeff" <jmoore207@gmail.com> wrote in message 
news:c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com...
>I am having a problem with a left outer join when I add conditionals.
>
…[14 more quoted lines elided]…
> regardless. Any ideas?

ALL A.vehicles?

Then you can't us the conditionals that way, since that will omit any 
a.vehicles which don't have any rows in b matching the conditions.

You can change your select to return a 'nvl'  (oracle) or 'nullif' 
(something) or CASE (I think that is standard) to return the rows where the 
"b" results set columns will be null and eliminate the WHEREs , but there 
are others here who write SQL far far better than do I.

MCM
```

##### ↳ ↳ Re: ProCobol Outer join

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-08T07:40:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ffca9256-ffb9-4cea-b3a1-7ed6a747d374@j22g2000hsf.googlegroups.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net>`

```
On May 8, 10:24 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> "jeff" <jmoore...@gmail.com> wrote in message
>
…[36 more quoted lines elided]…
> - Show quoted text -

Yeah that was kind of an overview, I did use NVL for the B.Table
fields to account for nulls. Thanks for your help
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2008-05-08T10:54:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e14b54de-bde9-49c3-8f86-48010682a6c3@l64g2000hse.googlegroups.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net> <ffca9256-ffb9-4cea-b3a1-7ed6a747d374@j22g2000hsf.googlegroups.com>`

```
On 8 May, 15:40, jeff <jmoore...@gmail.com> wrote:
> On May 8, 10:24 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>
…[39 more quoted lines elided]…
> fields to account for nulls. Thanks for your help

I don't know whether you can explicity state Left outer join in
ProCOBOL, but if you can then presumably the syntax diagrams will
explain how to use it. I think you use ON rather than WHERE for the
matching criteria.

Alternately, in addition to Michael's suggestion, you could try a
UNION for the select with the matching criteria together with a select
just for table A.

Good luck (I am rather rusty!)

Robert
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

_(reply depth: 4)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-08T11:01:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f1ca71aa-3018-4264-8557-ea5579ab5cde@z72g2000hsb.googlegroups.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net> <ffca9256-ffb9-4cea-b3a1-7ed6a747d374@j22g2000hsf.googlegroups.com> <e14b54de-bde9-49c3-8f86-48010682a6c3@l64g2000hse.googlegroups.com>`

```
On May 8, 1:54 pm, Robert Jones <rjon...@hotmail.com> wrote:
> On 8 May, 15:40, jeff <jmoore...@gmail.com> wrote:
>
…[58 more quoted lines elided]…
> - Show quoted text -

The way you are suggesting do I do a select within a select?
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

_(reply depth: 5)_

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2008-05-08T13:56:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc44413a-9778-4c64-9ac3-9c1598373666@2g2000hsn.googlegroups.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net> <ffca9256-ffb9-4cea-b3a1-7ed6a747d374@j22g2000hsf.googlegroups.com> <e14b54de-bde9-49c3-8f86-48010682a6c3@l64g2000hse.googlegroups.com> <f1ca71aa-3018-4264-8557-ea5579ab5cde@z72g2000hsb.googlegroups.com>`

```
On 8 May, 19:01, jeff <jmoore...@gmail.com> wrote:
> On May 8, 1:54 pm, Robert Jones <rjon...@hotmail.com> wrote:
>
…[59 more quoted lines elided]…
> The way you are suggesting do I do a select within a select?

No you do two selects separated/joined by a UNION ALL phrase, each
select selects the same columns or their logical equivalents, which
can be values as is the case here.

e.g. something like (without referring to a manual)

Select a.vehicle
      ,b.vehicle(+)
      ,b.acct
      ,b.MOYR
      ,b.trancode
  from table1 a, table2 b
 where  a.vehicle=b.vehicle(+)
   and  b.acct='1234'
   and  b.MOYR = '0502'
   and  b.trancode='80'
 union all
select a.vehicle
      ,''
      ,''
      ,''
      ,''
  from table1 a
 order by a.vehicle

(UNION ALL should eliminate any identical rows, which UNION alone does
not)

I don't understand the syntax/meaning of b.vehicle(+), but I expect
you do.

Good luck

Robert
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-08T18:36:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k63724p247pl4atqvt5bt441kkhp11p57h@4ax.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <t2EUj.2679$3O7.1553@newssvr19.news.prodigy.net> <ffca9256-ffb9-4cea-b3a1-7ed6a747d374@j22g2000hsf.googlegroups.com> <e14b54de-bde9-49c3-8f86-48010682a6c3@l64g2000hse.googlegroups.com> <f1ca71aa-3018-4264-8557-ea5579ab5cde@z72g2000hsb.googlegroups.com> <bc44413a-9778-4c64-9ac3-9c1598373666@2g2000hsn.googlegroups.com>`

```
On Thu, 8 May 2008 13:56:21 -0700 (PDT), Robert Jones <rjones0@hotmail.com> wrote:

>On 8 May, 19:01, jeff <jmoore...@gmail.com> wrote:
>> On May 8, 1:54 pm, Robert Jones <rjon...@hotmail.com> wrote:
…[88 more quoted lines elided]…
>not)

You got it backwards -- Union eliminates dups, Union All does not.

b.vehicle(+) in the select list is invalid.

Unmatched quotes in the bottom select are invalid. They should say NULL.

It doesn't matter because there are no duplicates to eliminate. Written your way, the a
vehicles that match b vehicles will appear twice -- once with b data to the right and once
without. 

>I don't understand the syntax/meaning of b.vehicle(+), but I expect
>you do.

It's Oracle syntax for LEFT OUTER JOIN.
```

#### ↳ Re: ProCobol Outer join

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-08T20:40:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lj3724d5ohrvdm3vvl91gq43hk154hsa85@4ax.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com>`

```
On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:

>I am having a problem with a left outer join when I add conditionals.
>
…[14 more quoted lines elided]…
>regardless. Any ideas?

select *  from
( (select a.vehicle, b.vehicle as b_vehicle,  b.acct, b.MOYR, b.trancode
  from table1 a, table2 b
  where a.vehicle = b.vehicle
      and b.acct='1234'
      and b.MOYR = '0502'
      and b.trancode='80'
 ) matches
 union 
 select vehicle, null, null, null, null
  from table1 a
  where vehicle not in (select vehicle from matches)
 order by vehicle
)

There is a simpler way using DISTINCT, which applies to all columns FOLLOWING the word
distinct. 

select vehicle, b_vehicle, acct, MOYR, trancode  from
(select b_vehicle, acct, MOYR, trancode, DISTINCT vehicle from
 (select a.vehicle, b.vehicle as b_vehicle,  b.acct, b.MOYR, b.trancode, '1' as source
   from table1 a, table2 b
   where a.vehicle = b.vehicle
      and b.acct='1234'
      and b.MOYR = '0502'
      and b.trancode='80' 
  union 
  select vehicle, null, null, null, null, '2' as source 
   from table1
  order by vehicle, source
 )
)
```

##### ↳ ↳ Re: ProCobol Outer join

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-09T15:09:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68htj7F2tbc89U1@mid.individual.net>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <lj3724d5ohrvdm3vvl91gq43hk154hsa85@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:lj3724d5ohrvdm3vvl91gq43hk154hsa85@4ax.com...
> On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:
>
…[51 more quoted lines elided]…
> )

Very impressive, Robert.

Thanks for posting this. I, for one, learned something.

Pete.
```

#### ↳ Re: ProCobol Outer join

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-08T20:48:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com>`

```
On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:

>I am having a problem with a left outer join when I add conditionals.
>
…[14 more quoted lines elided]…
>regardless. Any ideas?

On second thought, just add left outer join (+) to all the right columns:

Select
        A. vehicle,
        B.Vehicle,
        B.acct,
        B.MOYR,
        B.Trancode
 from  Table1 A, Table2 B
 where A.vehicle=B.vehicle(+)
  and   B.acct(+)='1234'
  and   B.MOYR(+) = '0502'
  and  B.trancode(+)='80'
  order by a.vehicle
```

##### ↳ ↳ Re: ProCobol Outer join

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-09T15:11:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68htmgF2suhsfU1@mid.individual.net>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com...
> On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:
>
…[31 more quoted lines elided]…
>  order by a.vehicle

Hmmm... it seems there are facilities in Oracle that are not usual. 
Nevertheless, a very elegant solution.

Pete.
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-08T22:55:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1bi7241m6bp17fed17maf0jkc5ru7m0lnv@4ax.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com> <68htmgF2suhsfU1@mid.individual.net>`

```
On Fri, 9 May 2008 15:11:11 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[38 more quoted lines elided]…
>Nevertheless, a very elegant solution.

Logically, a=foo(+) means a=foo or foo is null
                foo(+)=a means foo=a or foo is null

you could also think of it meaning  a=nvl(foo,a)
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-05-09T08:17:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bYUj.2660$7k7.1465@flpi150.ffdc.sbc.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com> <68htmgF2suhsfU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:68htmgF2suhsfU1@mid.individual.net...

> Hmmm... it seems there are facilities in Oracle that are not usual.

Oracle is a hell of a DBMS.  Not inexpensive but it has a ton of facilities, 
it's fast, reliable, a lot of extensions to standard SQL, command-line 
exection of PL/SQL via SQL+ ... and on and on and on.

FWIW, Oracle offers an 'express'  version free for the download, kind of 
like Microsoft offers their SQL Server Express (or maybe it's called MSDE) . 
It's a really good way to learn the Oracle extensions to SQL at a low cost. 
Go to the Oracle web site and start hitting links and you'll find it.

MCM
```

###### ↳ ↳ ↳ Re: ProCobol Outer join

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-10T12:57:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68ka7sF2t030vU1@mid.individual.net>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com> <g5b7245ohs5ob6nrikqm0uaql8e1n708ul@4ax.com> <68htmgF2suhsfU1@mid.individual.net> <8bYUj.2660$7k7.1465@flpi150.ffdc.sbc.com>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:8bYUj.2660$7k7.1465@flpi150.ffdc.sbc.com...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:68htmgF2suhsfU1@mid.individual.net...
…[15 more quoted lines elided]…
>
 Thanks for the tip, Michael.

As I already have 4 RDBMS installed on my notebook I'm loth to add another 
one :-)

Nevertheless, I'll keep this in mind for when someone pays me to do 
something with Oracle... :-)

Pete.
```

#### ↳ Re: ProCobol Outer join

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-08T22:25:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mmg7245hbpg6m4ia9t8k3qd48l9mv3598t@4ax.com>`
- **References:** `<c06426f2-e7e7-428c-9350-b3343d6a612c@k13g2000hse.googlegroups.com>`

```
On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:

>I am having a problem with a left outer join when I add conditionals.
>
…[14 more quoted lines elided]…
>regardless. Any ideas?

You might find ANS syntax more intuitive. It is available on Oracle 9 and above.

Select
        A. vehicle,
        B.Vehicle,
        B.acct,
        B.MOYR,
        B.Trancode
 from  Table1 A LEFT OUTER JOIN Table2 B
 where A.vehicle=B.vehicle
  and   B.acct='1234'
  and   B.MOYR = '0502'
  and  B.trancode='80'
  order by a.vehicle

What if a vehicle appears in B but not in A? It cannot be done easily with the old syntax;
it's a snap with ANS syntax. Just change LEFT OUTER JOIN to FULL OUTER JOIN.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
