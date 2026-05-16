[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Instead of DB2... Batch? Forward... Into the Past!

_23 messages · 7 participants · 2001-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-09T14:08:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net>`

```


All right, gang... now it is time for *me* to ask for someone to Do My Job
for me.  I hope I've included enough information to make it less tedious.

What I have is a DB2 table... actually two tables but of almost identical
design.  Changing a few minor details in order to protect the identity of
my client... the tables contain detail-information about orders and
charges placed by customers.  The first table is for charges less than 14
days old; after two weeks a batch process shuffles stuff onto the
report-charge table (so named because it is used more for reports than
online queries.  Combined the tables contain about 3,000,000 rows.

The table(s) are ordered by are:

CUST_NO
ORDER_NO
BRANCH_CD
DEPT_CD
TOTAL_PRICE
RECORD_STATUS
REVERSAL_IND

... and now, of course, the client wants an online report where a range of
dates can be selected (up to one year) for a given BRANCH_CD/DEPT_CD
combination and then the count of customers (DISTINCT CUST_NO) and grand
total of prices (SUM TOTAL_PRICE) can be shown for a couple of different
RECORD_STATUSes.  REVERSAL_IND is to show that the order was reversed and
the TOTAL_PRICE is negative.

Data volume is... unpredictable, to say the least; a given
BRANCH_CD/DEPT_CD combo can have, for a year, a couple of hundred thousand
transactions... or none... or any number in-between.  Initial analysis
against the tables showed that for a larger-volume combo a query of:

SELECT COUNT(DISTINCT CUST_NO), SUM(TOTAL_PRICE)
 INTO :WS-BILLED-NOTREV-CNT,                    
      :WS-BILLED-NOTREV-SUM                     
 FROM   BIGGERTBL                               
     WHERE SERVICE_DT BETWEEN :WS-FROM-DT AND WS-TO-DT           
       AND RECORD_STATUS = 'B'                  
       AND REVERSAL_CHG_IND ,= 'Y'

... took about twenty minutes to run.  Not wanting to face a Corner-Office
Idiot after he'd waited through such a response-time I had an idea which,
of course, violates all the rules of System Design: build another table
for a single application.  The new table would have 366 rows for each
BRANCH_CD/DEPT_CD combo (there are about 400 such combos, making for a
full table - initially - of a hair more than 146K rows), one for each day,
and have each row contain the various COUNTs and SUMs for the sundry
RECORD_STATUSes and REVERSAL_INDs.  That way a given day's data would be
available immediately and a range BETWEEN dates would involve a scan of a
much smaller table.

Are you still with me?  Since this NEWTBL would have to be created daily
(on any given day orders can be submitted for any given customer for any
given service-date so I cannot initially load history and then just add
new transactions) and the larger-volume queries, as shown above, can take
inordinate amounts of time I put together a program which would create a
temporary table for each BRANCH_CD/DEPT_CD combo so that SUMs would not
have to go against the larger table... in other words I would:

INSERT INTO TEMPTBL                               
    SELECT CUST_NO,                               
           SERVICE_DT,                            
           BRANCH_CD,                         
           DEPT_CD,                             
           TOTAL_PRICE,                           
           RECORD_STATUS,                         
           REVERSAL_CHG_IND                       
FROM   BIGGERTBL                                
WHERE BRANCH_CD = :WS-BRANCH-CD     
  AND DEPT_CD     = :WS-DEPT-CD         
  AND SERVICE_DT BETWEEN :WS-FROM-DT AND :WS-TO-DT
  AND RECORD_STATUS IN ('B', 'S')

... and then I would SELECT my various COUNTs and SUMs for each date
against this subset.

The only problem is... it *still* take too long; depending on system load
the job runs 9 - 13 hrs wall-time and burns up 3+hrs of CPU.  For a daily
process this is unacceptable.

So... whence go I from here?  My only alternative seems to be... Back to
Batch.  As I see it now I would use ol' IKJEFT01 to

SELECT CUST_NO,                                        
       SERVICE_DT,                                     
       BRANCH_CD,                                  
       DEPT_CD,                                      
       TOTAL_PRICE,                                    
       RECORD_STATUS,                                  
       REVERSAL_CHG_IND                                
FROM   BIGGERTBL                              
ORDER BY BRANCH_CD, DEPT_CD, SERVICE_DT, CUST_NO;

... and dump the results to tape.  (this takes a mere 10 minutes)  Next
would be to MERGE this with the same results from the SMALLERTBL and then
run the whole mess through a COBOL batch program to generate the NEWTBL
rows, with COUNTs and SUMs done in olde-style control-break fashion.  Just
to keep it fast I would probably write all the output to a flat file and
then finish the jobstream with another IKJEFT01 to DROP the current
NEWTBL, re-CREATE it and then LOAD DATA with a DSNUTILB.

Back in the Oldene Dayse my Drill Sergeant used a phrase to describe a
situation which was unpleasant for the active participant, unpleasant for
the passive participant and unpleasant for the observer... something which
met these criteria was called 'monkey dicked the dog'.  Creating a new
table, used by a single application, in this fashion - because the data
are of such volume and arrangement that SQL functions take too long -
strikes me as just this.  In the spirit of 'four-eye debugging' I present
this to the group, then, and ask for responses as time, inclination and
generosity permit.

(note: consider this to be the issuing of 'Good luck, ya poor bastard';
it, and its variants, now no longer need consume bandwidth)

Thanks much!

DD
```

#### ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-09T19:08:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LWHw7.21960$ev2.30599@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net>`

```
Well DD,

I hit such a beast where I work now and guess what?  I ended up extracting and
sorting and creating again from a good old COBOL program with a sort.  My
process takes about 1/100 of the time the QUERY takes.  However, might I suggest
an alternative for you to TRY that stays within the database world.

Create a VIEW of the original table based on your requirements and then add some
indexes to it.  Might work - might not.  Might slow the WHOLE ENTERPRISE Down
while the view is updated as records are inserted -- might be unnoticable.


In article <RxDw7.8729$ym4.375005@iad-read.news.verio.net>,   NA says...
>
>
…[118 more quoted lines elided]…
>DD
```

##### ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-10T12:53:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XwXw7.8811$ym4.378936@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <LWHw7.21960$ev2.30599@www.newsranger.com>`

```
In article <LWHw7.21960$ev2.30599@www.newsranger.com>,
Thane Hubbell  <nospam@newsranger.com> wrote:
>Well DD,
>
>I hit such a beast where I work now and guess what?  I ended up extracting and
>sorting and creating again from a good old COBOL program with a sort.

Looks like I'll be doing something similar, Mr Hubbell, except that I'll
be letting The System take care of sorting with an ORDER BY in my extract.

(tech observation: a straight SELECT, table-to-tape, of what I need -
361-char tbl-rows to 30-char flat file rec - takes 7 - 8 min of wall-time;
the ORDER BY bumps that out to 10 - 11 min)

>My
>process takes about 1/100 of the time the QUERY takes.  However, might I suggest
…[4 more quoted lines elided]…
>while the view is updated as records are inserted -- might be unnoticable.

It was the former... got calls from Ops saying 'How come you're chowin'
down all that CPU?' and the job got cancelled 3.5 wall-hours into the run.

Thanks much for the thoughts, though!

DD
```

#### ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2001-10-09T19:50:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC35517.1F3C5726@boeing.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net>`

```


NA wrote:
> 
> All right, gang... now it is time for *me* to ask for someone to Do My Job
> for me.  I hope I've included enough information to make it less tedious.
> 

what sort of primary and secondary indexes do you have?
I have built indexes to speed up processing (& it can make a huge
difference)

	Susan A
```

##### ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** "Tom Sheckells" <tomsheckells@home.com>
- **Date:** 2001-10-10T03:25:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rcPw7.135979$Xz1.19081293@news1.rdc1.md.home.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com>`

```
NA
    Susan is on the right track!  When I was a DB2 DBA (hint) the indexes
were more important than the table sizes.  HOWEVER; after you make sure you
have the correct indexes, you MUST check the bind to make sure that the
indexes are being used (and correctly).  Also, please note that only unique
indexes should be used.

    Tom

"Susan A Allen" <susan.a.allen@boeing.com> wrote in message
news:3BC35517.1F3C5726@boeing.com...
>
>
> NA wrote:
> >
> > All right, gang... now it is time for *me* to ask for someone to Do My
Job
> > for me.  I hope I've included enough information to make it less
tedious.
> >
>
…[4 more quoted lines elided]…
> Susan A
```

##### ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-10T16:42:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VT_w7.8842$ym4.379758@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com>`

```
In article <3BC35517.1F3C5726@boeing.com>,
Susan A Allen  <susan.a.allen@boeing.com> wrote:
>
>
…[6 more quoted lines elided]…
>what sort of primary and secondary indexes do you have?

None that are of any use, sadly... there's a secondary on BRANCH_CD and
DEPT_CD but I need access by these two + SERVICE_DT.

>I have built indexes to speed up processing (& it can make a huge
>difference)

I've run the idea of expanding the secondary to what I need past the DBA
crew... their response lead me to believe that this will happen right
after my snowball-fight with Satan.

Thnks much for the suggestions, though!

DD
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-10T19:44:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ly1x7.23559$ev2.32231@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net>`

```
If your customer has a valid need for the report, make the Database Committe or
whatever turn you down in writing and show it to a higher boss.  Then let them
argue about it.
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-11T10:09:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zdex7.8975$ym4.382210@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net> <Ly1x7.23559$ev2.32231@www.newsranger.com>`

```
In article <Ly1x7.23559$ev2.32231@www.newsranger.com>,
Charles  <nospam@newsranger.com> wrote:
>If your customer has a valid need for the report, make the Database Committe or
>whatever turn you down in writing and show it to a higher boss.  Then let them
>argue about it.

I've done such things, when I was younger and more nasty... but right now
things are a bit slow so hey, why not... and I'm doing it in batch.

DD
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-10T20:04:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Q1x7.23577$ev2.32503@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net>`

```
Is there a big performance hit to create the view and apply the index to said
view?


In article <VT_w7.8842$ym4.379758@iad-read.news.verio.net>,   NA says...
>
>In article <3BC35517.1F3C5726@boeing.com>,
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-11T10:11:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lfex7.8976$ym4.382572@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net> <_Q1x7.23577$ev2.32503@www.newsranger.com>`

```
In article <_Q1x7.23577$ev2.32503@www.newsranger.com>,
Thane Hubbell  <nospam@newsranger.com> wrote:
>Is there a big performance hit to create the view and apply the index to said
>view?

Mr Hubbell, I am confused... aren't indices applicable to tables only?
(I'd always imagined a view as a kind of set of results from a stored
procedure... but I freely admit that there are things beyond my
imagination.)

DD

>
>
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 5)_

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-11T22:57:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5tpx7.25255$ev2.34367@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net> <_Q1x7.23577$ev2.32503@www.newsranger.com> <Lfex7.8976$ym4.382572@iad-read.news.verio.net>`

```
I live in the Oracle world.  I'm not sure if what I suggested is possible - with
Oracle or DB2 -- but I was fairly certain one could add an index to a view.
Maybe NOT!  I'll investigate with my Oracle guru's tomorrow - any DB2ers here
know about DB2 having this feature?


In article <Lfex7.8976$ym4.382572@iad-read.news.verio.net>,   NA says...
>
>In article <_Q1x7.23577$ev2.32503@www.newsranger.com>,
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 6)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-12T13:59:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dHCx7.9100$ym4.389802@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <_Q1x7.23577$ev2.32503@www.newsranger.com> <Lfex7.8976$ym4.382572@iad-read.news.verio.net> <5tpx7.25255$ev2.34367@www.newsranger.com>`

```
In article <5tpx7.25255$ev2.34367@www.newsranger.com>,
Thane Hubbell  <nospam@newsranger.com> wrote:
>I live in the Oracle world.  I'm not sure if what I suggested is possible - with
>Oracle or DB2 -- but I was fairly certain one could add an index to a view.

According to the SQL Reference (DB2 for OS/390, Version 5, SC26-8966-00) a
view is created as a subselect:

CREATE VIEW view-name (column-name) AS subselect WITH buncha stuff

... and an index is created on a table:

CREATE (TYPE 1/2) (UNIQUE) INDEX index-name ON table-name.

>Maybe NOT!

Be *very* wary of *any* solution which begins with 'All ya gotta do is...'

> I'll investigate with my Oracle guru's tomorrow - any DB2ers here
>know about DB2 having this feature?

As noted above, thus speaketh the manual... but perhaps there's more out
there.

Thanks much, though!

DD

>
>
…[49 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 7)_

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-12T21:51:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aBJx7.26807$ev2.35415@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <_Q1x7.23577$ev2.32503@www.newsranger.com> <Lfex7.8976$ym4.382572@iad-read.news.verio.net> <5tpx7.25255$ev2.34367@www.newsranger.com> <dHCx7.9100$ym4.389802@iad-read.news.verio.net>`

```
Well... the Oracle people here say the same thing.  But...

They say you can create an index on the combination of colums.  HOWEVER to make
sure that index is USED you must specify the columns in the SAME order as the
index is defined in your where clause - else it will not be used.  So there may
yet be hope.  Can you see if the same applies to DB2?



In article <dHCx7.9100$ym4.389802@iad-read.news.verio.net>,   NA says...
>
>In article <5tpx7.25255$ev2.34367@www.newsranger.com>,
…[80 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 8)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-15T13:22:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_pBy7.9299$ym4.403997@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <5tpx7.25255$ev2.34367@www.newsranger.com> <dHCx7.9100$ym4.389802@iad-read.news.verio.net> <aBJx7.26807$ev2.35415@www.newsranger.com>`

```
In article <aBJx7.26807$ev2.35415@www.newsranger.com>,
Thane Hubbell  <nospam@newsranger.com> wrote:
>Well... the Oracle people here say the same thing.  But...
>
…[3 more quoted lines elided]…
>yet be hope.  Can you see if the same applies to DB2?

Thanks again, Mr Hubbell - truth be known, I learned about views in an
Oracle class I took recently! - but, as mentioned in other places in this
thread I've gone Forward, Into the Past and put the whole thing into a
batch COBOL program.

Sometimes it is a Good Thing to have a hammer to take care of the problems
that actually *are* nails, I guess.

DD
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** "Rick Price" <rick@hpdsoftware.com>
- **Date:** 2001-10-12T09:31:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q69m5$lvagn$1@ID-39799.news.dfncis.de>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net>`

```

" NA" <docdwarf@clark.net> wrote in message
news:VT_w7.8842$ym4.379758@iad-read.news.verio.net...
> In article <3BC35517.1F3C5726@boeing.com>,
> Susan A Allen  <susan.a.allen@boeing.com> wrote:
…[4 more quoted lines elided]…
> >> All right, gang... now it is time for *me* to ask for someone to Do My
Job
> >> for me.  I hope I've included enough information to make it less
tedious.
> >>
> >
…[3 more quoted lines elided]…
> DEPT_CD but I need access by these two + SERVICE_DT.

If  there is a secondary index on branch and dept then,  AFAIK, the query
should make use of it even though you have additional criteria.  Your
original sample SELECT COUNT doesn't actually do a selection on branch and
dept.  Is this just an oversight in the sample?  If you are using branch and
dept criteria, maybe you need to check if the query is using this available
index, and if its not, try to find out why not.

How long does it take to retrieve all the data where the only criteria are
branch and dept?  I don't actually know anything about DB2 (nor much about
RDBMS) but is it possible that this index is set up so that it is only
updated when used?  Probably not possible, but I know that on the AS400, it
is possible to set up alternate key paths that are not updated dynamically
but only when the data is used.

Have you got a test DB so you can test with different criteria?  I know this
is a totally different  set up and size problem, but we recently had a query
that was taking 20 seconds (shock horror) on a SQL Server data base.  For
the amount of data, this was too long.  We discovered that it wasn't using
an available index.  We played around with the query,  including trying
different nonce criteria (e.g DATA = %) and finally got it to use the index.
The query then took 2 seconds.

>
> >I have built indexes to speed up processing (& it can make a huge
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-15T13:15:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3kBy7.9298$ym4.404013@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <3BC35517.1F3C5726@boeing.com> <VT_w7.8842$ym4.379758@iad-read.news.verio.net> <9q69m5$lvagn$1@ID-39799.news.dfncis.de>`

```
In article <9q69m5$lvagn$1@ID-39799.news.dfncis.de>,
Rick Price <rick@hpdsoftware.com> wrote:
>
>" NA" <docdwarf@clark.net> wrote in message
…[21 more quoted lines elided]…
>index, and if its not, try to find out why not.

Well, even if it is using the index it takes too long.  For a sample from
one of the larger Branch/Dept combos (100K+ rows covering 166 days) the
whole process - create TEMPTBL, INSERT into TEMPTBL the SELECTs of rows
from both main tbls, process TEMPTBL with four SELECT COUNT(DISTINCT) and
SUMs per day (only DISPLAYing results), DROPing the TEMPTBL and
re-creating it for the next combo - took 7 min, 43 sec of wall-time.

At the other end of the scale a Branch/Dept combo with only one row, for
one day's data, went through this loop in 45 sec of wall... but these are
both extremes, of course.  For approx. 400 Branch/Dept combos, each with
366 days of data it is just... too much.  I've managed, I think, to
duplicate the COUNT(DISTINCT) and SUM with the following batch COBOL
logic:

(note - the four conditions being totalled for are billed/reversed,
billed/not reversed, sent/reversed and sent/not reversed)

IF WS-IN-CUSTNO NOT = WS-PREV-CUSTNO                        
    MOVE WS-IN-CUSTNO  TO  WS-PREV-CUSTNO                   
    MOVE SPACES TO WS-COND-FLAGS.                           
                                                            
EVALUATE TRUE                                               
    WHEN WS-IN-RECSTAT = 'B' AND                            
         WS-IN-REVERSAL-IND NOT = 'Y'                       
        ADD WS-IN-TOTPRC  TO  WS-OUT-BILLED-NOTREV-SUM      
        IF NOT COND1-FOUND                                  
            SET COND1-FOUND TO TRUE                         
            ADD +1          TO  WS-OUT-BILLED-NOTREV-CNT    
        END-IF                                              
    WHEN WS-IN-RECSTAT = 'B' AND WS-IN-REVERSAL-IND = 'Y'   
        ADD WS-IN-TOTPRC  TO  WS-OUT-BILLED-REV-SUM         
        IF NOT COND2-FOUND                                  
            SET COND2-FOUND TO TRUE                         
            ADD +1          TO  WS-OUT-BILLED-REV-CNT       
        END-IF                                              
    WHEN WS-IN-RECSTAT = 'S' AND                         
         WS-IN-REVERSAL-IND NOT = 'Y'                    
        ADD WS-IN-TOTPRC  TO  WS-OUT-SENT-NOTREV-SUM     
        IF NOT COND3-FOUND                               
            SET COND3-FOUND TO TRUE                      
            ADD +1          TO  WS-OUT-SENT-NOTREV-CNT   
        END-IF                                           
    WHEN WS-IN-RECSTAT = 'S' AND WS-IN-REVERSAL-IND = 'Y'
        ADD WS-IN-TOTPRC  TO  WS-OUT-SENT-REV-SUM        
        IF NOT COND4-FOUND                               
            SET COND4-FOUND TO TRUE                      
            ADD +1          TO  WS-OUT-SENT-REV-CNT      
        END-IF                                           
END-EVALUATE.                                            

... and yes, I know that the same customer can, in theory, be counted four
times but this is what The Customer wants.

DD
```

#### ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** "Paul Raulerson" <praul@isot.NOSPAM.com>
- **Date:** 2001-10-10T06:55:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ts8dud3t0rc821@corp.supernews.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net>`

```
Hey Doc -
  Before you go to all that, why don' t you do an explain on that query, and
post that and the bind results? It's probably possible to speed that query
up
to acceptable levels without all the gyrations. ;)

-Paul

" NA" <docdwarf@clark.net> wrote in message
news:RxDw7.8729$ym4.375005@iad-read.news.verio.net...
>
>
…[117 more quoted lines elided]…
> DD
```

##### ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-11T20:02:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NVmx7.25044$ev2.33985@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com>`

```
On Wed, 10 Oct 2001 06:55:52 -0500, in article
<ts8dud3t0rc821@corp.supernews.com>, Paul Raulerson stated 
>
>Hey Doc -
…[130 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2001-10-12T06:49:09+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC605C4.D1A76241@melbpc.org.au>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com> <NVmx7.25044$ev2.33985@www.newsranger.com>`

```
What you are doing, maybe without realizing it, is creating a data warehouse.
There are lots of good books on the topic that discuss the problems you are
having in detail.

Mainly you are doing the right thing, separating out the DW from the operational
system, etc.

The problem with data warehouses is that, as you found, the normalized data
model leads to inefficient query performance in various domains. Thus the Data
Mart was invented. It is a specialized database with denormalized structure
built for good query performance in various domains. You build the DW and then
build the DMs from it. Some data marts even use 'summary tables' which are
predigested tables of summary statistics. This is what you are thinking of
doing. The usual advice is 'only do that if you need to do it' but if you need
to do it you are following the right approach - though on some platforms there
are tools to help you do all this.

I known this may be heresy but you could put the query database on a Wintel box
and give it 1gb of RAM. The whole table would fit in memory and the queries
should go really fast. Very few data warehouses are on manframes; they are
usually on Wintel or Unix depending on relability and scale requirements.

One main risk here is that you are going to create a DW/DM without having
properly architected it, and you will have to redo it all in a few years time.

Tim Josling

>news:RxDw7.8729$ym4.375005@iad-read.news.verio.net...
>>
…[8 more quoted lines elided]…
>>>> ... and dump the results to tape.  (this takes a mere 10 minutes)
(...etc...)

>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-12T13:44:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ltCx7.9098$ym4.389965@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com> <NVmx7.25044$ev2.33985@www.newsranger.com> <3BC605C4.D1A76241@melbpc.org.au>`

```
In article <3BC605C4.D1A76241@melbpc.org.au>,
Tim Josling  <tej@melbpc.org.au> wrote:
>What you are doing, maybe without realizing it, is creating a data warehouse.

Wow... does this mean my hourly rate is too low?

[snip]

>I known this may be heresy but you could put the query database on a Wintel box
>and give it 1gb of RAM. The whole table would fit in memory and the queries
>should go really fast. Very few data warehouses are on manframes; they are
>usually on Wintel or Unix depending on relability and scale requirements.

Now *that* would be interesting... unload the table, ftp the unload to the
Wintel, rebuild the table in... I dunno, Oracle or something, on a hurkin'
great RAM-disk, run the program to create an output flatfile, ftp the
flatfile back to the mainframe and load the result into the new table.

In interesting approach... not a snowball's chance of getting it approved,
mind you, but most interesting.  Thanks much for the pretty thoughts!

>
>One main risk here is that you are going to create a DW/DM without having
>properly architected it, and you will have to redo it all in a few years time.

Hey, not a problem... life-expectancy of a system's less than that,
there'll *never* be a Y2K problem!

Greatly appreciated, Mr Josling.

DD

>>news:RxDw7.8729$ym4.375005@iad-read.news.verio.net...
>>>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-12T13:26:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XbCx7.9093$ym4.389721@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com> <NVmx7.25044$ev2.33985@www.newsranger.com>`

```

... strange, Mr Raulerson's posting never made it to my news-server.  I'll
address both, here.

In article <NVmx7.25044$ev2.33985@www.newsranger.com>,
Charles  <nospam@newsranger.com> wrote:
>On Wed, 10 Oct 2001 06:55:52 -0500, in article
><ts8dud3t0rc821@corp.supernews.com>, Paul Raulerson stated 
…[4 more quoted lines elided]…
>>to acceptable levels without all the gyrations. ;)

What a difference two days make... thanks, Mr Raulerson, for the
suggestion but I've already coded up the unloads, sort,COBOL and load; the
whole mess now runs in about 25 min of wall-time.

DD
```

##### ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-11T20:05:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YXmx7.25047$ev2.33877@www.newsranger.com>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com>`

```
3 hrs isnt too bad if you could run it every Night while you are asleep.  It
might run faster at night anyway.  Can you run it as a timed event at 1:00 AM?

>Hey Doc -
>  Before you go to all that, why don' t you do an explain on that query, and
…[129 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [OT] Instead of DB2... Batch? Forward... Into the Past!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-12T13:53:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mBCx7.9099$ym4.390029@iad-read.news.verio.net>`
- **References:** `<RxDw7.8729$ym4.375005@iad-read.news.verio.net> <ts8dud3t0rc821@corp.supernews.com> <YXmx7.25047$ev2.33877@www.newsranger.com>`

```
In article <YXmx7.25047$ev2.33877@www.newsranger.com>,
Charles  <nospam@newsranger.com> wrote:
>3 hrs isnt too bad if you could run it every Night while you are asleep.  It
>might run faster at night anyway.  Can you run it as a timed event at 1:00 AM?

Ummmmm... that's 3 hrs *CPU* time.  Wall-time is 9 - 13 hrs and everything
else using the tables - which is, more or less, everything else - slows to
a crawl.

Thanks much, though!

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
