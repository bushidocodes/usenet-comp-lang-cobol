[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: General Host Environment Skills Growth Question

_5 messages · 3 participants · 2003-07_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: General Host Environment Skills Growth Question

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-07-22T22:18:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3LiTa.50097$k85.1877584@twister.tampabay.rr.com>`

```
Is the following a common truth or a misconception on my part.  I guess I
thought about this reading the Fortress thread and the "digging in" and lack
of skills upgrading.

Client server (by this I mean Unix/Windows client) developers need to get an
application online and working.  They log onto one of  5 test AIX/Unix/Linux
boxes, install Websphere/JBoss and ship some demos and test files over
there...tweak it and get a prototype....then they change settings, add some
more ....code/develop/test.....they need a database they install MySQL,
UDB...they test, they install a JMS implementation and they .....until they
are fully educated in the world.

Host developers need to get an application online and working.  They log
onto the1 test machine LPAR and see if Websphere is running.  It isn't, they
request support to install....wait.....they ship some demos and test
files......they try and run, RACF won't let them.   They get support to fix
RACFt.  They try again,  it doesn't work, they cannot change setting.  They
tweak. They need DB2/MySQL they call the DBA who calls support, they
wait.....etc etc etc

Is it me or does the environment support structure difference on the two
platforms

1) Encourage poorly structured managed applications where people manage more
than they "really understand"....(i.e. using JDBC doesn't mean your database
subsystem is performance tuned)

2) Inertia that prevents the ability to really "investigate" and try out new
things.

JCE
```

#### ↳ Re: General Host Environment Skills Growth Question

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-23T12:31:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f1dd808_6@news.athenanews.com>`
- **References:** `<3LiTa.50097$k85.1877584@twister.tampabay.rr.com>`

```
Excellent and pertinent comment.

All to often getting things done on Fortress sites is like wading through
treacle.

I've
"jce" <defaultuser@hotmail.com> wrote in message
news:3LiTa.50097$k85.1877584@twister.tampabay.rr.com...
> Is the following a common truth or a misconception on my part.  I guess I
> thought about this reading the Fortress thread and the "digging in" and
lack
> of skills upgrading.
>
> Client server (by this I mean Unix/Windows client) developers need to get
an
> application online and working.  They log onto one of  5 test
AIX/Unix/Linux
> boxes, install Websphere/JBoss and ship some demos and test files over
> there...tweak it and get a prototype....then they change settings, add
some
> more ....code/develop/test.....they need a database they install MySQL,
> UDB...they test, they install a JMS implementation and they .....until
they
> are fully educated in the world.
>
> Host developers need to get an application online and working.  They log
> onto the1 test machine LPAR and see if Websphere is running.  It isn't,
they
> request support to install....wait.....they ship some demos and test
> files......they try and run, RACF won't let them.   They get support to
fix
> RACFt.  They try again,  it doesn't work, they cannot change setting.
They
> tweak. They need DB2/MySQL they call the DBA who calls support, they
> wait.....etc etc etc
…[4 more quoted lines elided]…
> 1) Encourage poorly structured managed applications where people manage
more
> than they "really understand"....(i.e. using JDBC doesn't mean your
database
> subsystem is performance tuned)
>
> 2) Inertia that prevents the ability to really "investigate" and try out
new
> things.
>
> JCE
>
>
```

##### ↳ ↳ Re: General Host Environment Skills Growth Question

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-23T12:35:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f1dd90f_1@news.athenanews.com>`
- **References:** `<3LiTa.50097$k85.1877584@twister.tampabay.rr.com> <3f1dd808_6@news.athenanews.com>`

```
Oops! Sorry...

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f1dd808_6@news.athenanews.com...

As I was saying <G>...

 Excellent and pertinent comment.

 All too often getting things done on Fortress sites is like wading through
 treacle.

 I've even seen programmers fudge a database design from existing tables
because it was politically inexpedient to wait for the DBA's approval and
get a new DB.

I think what is noted here is definitely a contributing factor to the
Fortress mentality.

Pete.


> "jce" <defaultuser@hotmail.com> wrote in message
> news:3LiTa.50097$k85.1877584@twister.tampabay.rr.com...
> > Is the following a common truth or a misconception on my part.  I guess
I
> > thought about this reading the Fortress thread and the "digging in" and
> lack
> > of skills upgrading.
> >
> > Client server (by this I mean Unix/Windows client) developers need to
get
> an
> > application online and working.  They log onto one of  5 test
…[37 more quoted lines elided]…
>
```

#### ↳ Re: OT: General Host Environment Skills Growth Question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-23T01:25:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f1ddd42.19836162@news.optonline.com>`
- **References:** `<3LiTa.50097$k85.1877584@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote:

>Is the following a common truth or a misconception on my part.  I guess I
>thought about this reading the Fortress thread and the "digging in" and lack
…[8 more quoted lines elided]…
>are fully educated in the world.

Isn't that how we learned most of what we know .. by trying things?

>Host developers need to get an application online and working.  They log
>onto the1 test machine LPAR and see if Websphere is running.  It isn't, they
…[7 more quoted lines elided]…
>platforms?

The platforms aren't all that different. The difference is the culture of people
working on those platforms. 

>1) Encourage poorly structured managed applications where people manage more
>than they "really understand"....(i.e. using JDBC doesn't mean your database
>subsystem is performance tuned)

Every database doesn't NEED to be performance tuned. I liken this to old-time
COBOL programmers who pre-optimized every statement, who worried about whether
COMPUTE is faster than ADD when writing new code. We now know that's a waste of
time. One should post-optimize only proven bottlenecks. The same principle
applies to databases. If the application is widely used AND the database is
causing a performance hit THEN it needs to be optimized by professionals. 

>2) Inertia that prevents the ability to really "investigate" and try out new
>things.

Inertia is not just lack of personal initiative, it's institutionalized. 

Prog:      I'd like to get MySQL installed on the test Linux.
Support: Why not use DB2?
Prog:      Its for a project I'm designing. I want to see whether it's faster 
             than DB2. 
Support: Ok, who's the team lead and what's the charge code?
Prog:      It's not an actual project yet. I just want to play with it. 
             Charge your time to general support.
Support: General is for dumb users. I need a project code for developer support.
             Call back when you have an approved project and make sure your team

             lead will sign off on it.
```

##### ↳ ↳ Re: OT: General Host Environment Skills Growth Question

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-07-23T04:14:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GYnTa.1476$BB6.53582@twister.tampabay.rr.com>`
- **References:** `<3LiTa.50097$k85.1877584@twister.tampabay.rr.com> <3f1ddd42.19836162@news.optonline.com>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3f1ddd42.19836162@news.optonline.com...
> Every database doesn't NEED to be performance tuned. I liken this to
old-time
> COBOL programmers who pre-optimized every statement, who worried about
whether
> COMPUTE is faster than ADD when writing new code. We now know that's a
waste of
> time. One should post-optimize only proven bottlenecks.

Bad choice of words...I meant poorly structured...data propagated to
multiple tables, inconsistent etc...usually the reason for poor
performance...I talk to DBAs daily even when there is no table involved as
they have unique perspective on data strategy.

JCE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
