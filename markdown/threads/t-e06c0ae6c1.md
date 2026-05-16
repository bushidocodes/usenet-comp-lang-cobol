[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MAINFRAME/DB2 question

_6 messages · 5 participants · 1999-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### MAINFRAME/DB2 question

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3738B936.8D@saif.com>`

```
MAINFRAME SITUATION:
We have a single DB2 sub-system that supports multiple test environments
by using unique table ownerid's.  I would prefer to have a separate DB2
sub-system for each test environment, in order to simplify connectivity
to other test system components.

MY QUESTION:
Does anyone else out there share my opinion?
Or better yet, are you working for a shop that utilizes multiple test
DB2 sub-systems?
(I need to prove to my management that my idea is not crackers!)

The only responses I get from the DB2 news group is that it is more
convienent to keep all the test systems under a single sub-system... but
I would expect that from DBAs.

Pete
```

#### ↳ Re: MAINFRAME/DB2 question

- **From:** Mike <nospam@anywhere.com>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37398122.9E97E31F@anywhere.com>`
- **References:** `<3738B936.8D@saif.com>`

```
At Caterpiller, Production and Quality have their own sub-system.
But, Unit Test and System Test share a sub-system, the same
way you do.

Mike
DBA contractor

Pete Wirfs wrote:

> MAINFRAME SITUATION:
> We have a single DB2 sub-system that supports multiple test environments
…[14 more quoted lines elided]…
> Pete
```

#### ↳ Re: MAINFRAME/DB2 question

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37398557.BEA87CC9@zip.com.au>`
- **References:** `<3738B936.8D@saif.com>`

```
Pete Wirfs wrote:
> 
> MAINFRAME SITUATION:
…[15 more quoted lines elided]…
> Pete

Peter,

DB2 subsystems tend to be very expensive to run for an MVS box. 
Therefore it is more efficient to create one subsystem but
segregate the tables by an owner id.  This means that if one DB2
test area is not used the MVS does not have the added overhead of
a started task.

I have worked extensively with multiple test regions and I have
found that the only reason to set up a third one (one for
production, one for test) is for new release testing and Y2k
testing.

If you are using the owner id inside your program somehow then
this might be where you are coming from.  If you are doing this
remove it and put it into your bind cards.  If you are using
dynamic SQL this is a new area, one solution is to create special
user id that you submit the job under (for each test area) and
then make a view to that userid.

If you can give us specifics of what problems you are trying to
hurdle in your application then we can possibly help you.

I am an application programmer not a DBA!

Ken
```

##### ↳ ↳ Re: MAINFRAME/DB2 question

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3739A339.DF6@saif.com>`
- **References:** `<3738B936.8D@saif.com> <37398557.BEA87CC9@zip.com.au>`

```
Ken Foskey wrote:
> 
> Pete Wirfs wrote:
…[44 more quoted lines elided]…
> Ken


Whoops, I failed to state the problem that is killing us right now.  We
want to use DB2 stored procedures which run in the SPAS component of the
DB2 sub system, but with a single test DB2 sub-system, we found we can
only run a single test version of any given stored procedure, when we
may have a requirement for more than one test version.  

(We currently specify table ownerid during BIND, only)

Thank you for any ideas you can offer...
Pete
```

#### ↳ Re: MAINFRAME/DB2 question

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hc5av$2ck$1@news.ses.cio.eds.com>`
- **References:** `<3738B936.8D@saif.com>`

```
At our shop we have a DB2 region for production, test, model office,
and tech support.  The tech support region is usually shut down, and
is activated only when they have installation or upgrade work to do.


Pete Wirfs <petwir@saif.com> wrote in message
news:3738B936.8D@saif.com...
> MAINFRAME SITUATION:
> We have a single DB2 sub-system that supports multiple test
environments
> by using unique table ownerid's.  I would prefer to have a separate
DB2
> sub-system for each test environment, in order to simplify
connectivity
> to other test system components.
>
> MY QUESTION:
> Does anyone else out there share my opinion?
> Or better yet, are you working for a shop that utilizes multiple
test
> DB2 sub-systems?
> (I need to prove to my management that my idea is not crackers!)
>
> The only responses I get from the DB2 news group is that it is more
> convienent to keep all the test systems under a single sub-system...
but
> I would expect that from DBAs.
>
> Pete
```

#### ↳ Re: MAINFRAME/DB2 question

- **From:** Matthew Son <esmks@email.ais.unc.edu>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37398327.28EE20F6@email.ais.unc.edu>`
- **References:** `<3738B936.8D@saif.com>`

```
Pete,

I agree with you.  
I used to work for GTE-DS and we used separate subsystems for our
different environments.  I'm not a database guru, so I don't understand
their side of it, but basically it is probably easier for them to
maintain (with a single sub-system).  I think it would make it a lot
more difficult for the programmers.  Also, besides the connectivity you
are concerned about, test systems have a tendency to need to be reset
quite often.  If you had test group A and test group B working on the
same subsystem, test group B could foul up the database for group A.  I
don't know what functionality you need, but I think in any case it would
be better for the application programmers to have separate subsystems.

Good luck - DBA's usually are stubborn and have clout.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
