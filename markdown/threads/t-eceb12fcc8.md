[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Database Connection

_5 messages · 4 participants · 2001-02_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Database Connection

- **From:** cobolchappy@yahoo.com (Cobol Boy)
- **Date:** 2001-02-19T21:46:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010219204613.3625.qmail@web12712.mail.yahoo.com>`

```
Hello All,

I am using the free Fujitsu compiler and am wanting my
program to retrieve some data from a database that I
use for my Delphi work. The database is a Paradox
database and I have the ODBC driver.

What I need to know is how do I set up my Cobol
envioronment so that the program knows where to find
my database and talk to it.

I've checked the online manuals on the CD but I seem
to be going round in circles, which is why I've posted
the question here in case someone has done this sort
of thing before and can give me a quick and simple
step by step guide to how to set this up.

Thanks very much for your time.

John.

__________________________________________________
Do You Yahoo!?
Get personalized email addresses from Yahoo! Mail - only $35 
a year!  http://personal.mail.yahoo.com/
```

#### ↳ Re: Database Connection

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2001-02-19T22:37:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A91A03C.1ED3E90C@boeing.com>`
- **References:** `<20010219204613.3625.qmail@web12712.mail.yahoo.com>`

```
Cobol Boy wrote:
> 
> Hello All,
…[9 more quoted lines elided]…
> 

I could be wrong, but I think it is part of your compile options.

	Susan A
```

#### ↳ Re: Database Connection

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-02-19T23:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96sb80$o9v$1@ins21.netins.net>`
- **References:** `<20010219204613.3625.qmail@web12712.mail.yahoo.com>`

```
There are three steps:

1.  Identify the ODBC data source - look for "ODBC Data Sources" under
Control Panel in Win 95.  I think it is one more layer down in Win
2000.

2.  Define the data source to the COBOL program using sqlodbc.exe, located
in the fujitsu directory structure.

3.  Issue the appropriate COBOL and SQL commands to access the database.

I am not sure how I figured this all out, but much of it came from the
fujitsu manual - other hints came from other ODBC tutorials. You might
want to look at material on using JDBC for other hints.

Floyd Johnson


Cobol Boy (cobolchappy@yahoo.com) wrote:
: Hello All,

: I am using the free Fujitsu compiler and am wanting my
: program to retrieve some data from a database that I
: use for my Delphi work. The database is a Paradox
: database and I have the ODBC driver.

: What I need to know is how do I set up my Cobol
: envioronment so that the program knows where to find
: my database and talk to it.

: I've checked the online manuals on the CD but I seem
: to be going round in circles, which is why I've posted
: the question here in case someone has done this sort
: of thing before and can give me a quick and simple
: step by step guide to how to set this up.

: Thanks very much for your time.

: John.

: __________________________________________________
: Do You Yahoo!?
: Get personalized email addresses from Yahoo! Mail - only $35 
: a year!  http://personal.mail.yahoo.com/

: -- 
: Posted from web12712.mail.yahoo.com [216.136.174.59] 
: via Mailgate.ORG Server - http://www.Mailgate.ORG
```

#### ↳ Re: Database Connection

- **From:** "Anthony Borla" <ajborla@bigpond.com>
- **Date:** 2001-02-20T16:24:00+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q1nk6.265$722.229@newsfeeds.bigpond.com>`
- **References:** `<20010219204613.3625.qmail@web12712.mail.yahoo.com>`

```
"Cobol Boy" <cobolchappy@yahoo.com> wrote in message
news:20010219204613.3625.qmail@web12712.mail.yahoo.com...
> Hello All,
>
…[14 more quoted lines elided]…
>

I'm pretty sure that ODBC connectivity is disabled on the 'free' version
(V3) of the compiler. See: http://www.adtools.com/student/description.htm
for details.

I hope this helps.
```

##### ↳ ↳ Re: Database Connection

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-02-20T05:46:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96t0bf$os1$1@ins21.netins.net>`
- **References:** `<20010219204613.3625.qmail@web12712.mail.yahoo.com> <q1nk6.265$722.229@newsfeeds.bigpond.com>`

```
Interesting - we have been using version 3 on our campus for several
years, and have not had a problems.  I wonder if this is a change? 

What about the version that is shipped with "Teach Yourself COBOL in 24
Hours"?

Floyd Johnson

Anthony Borla (ajborla@bigpond.com) wrote:
: "Cobol Boy" <cobolchappy@yahoo.com> wrote in message
: news:20010219204613.3625.qmail@web12712.mail.yahoo.com...
: > Hello All,
: >
: > I am using the free Fujitsu compiler and am wanting my
: > program to retrieve some data from a database that I
: > use for my Delphi work. The database is a Paradox
: > database and I have the ODBC driver.
: >
: > What I need to know is how do I set up my Cobol
: > envioronment so that the program knows where to find
: > my database and talk to it.
: >
: > I've checked the online manuals on the CD but I seem
: > to be going round in circles, which is why I've posted
: > the question here in case someone has done this sort
: > of thing before and can give me a quick and simple
: > step by step guide to how to set this up.
: >

: I'm pretty sure that ODBC connectivity is disabled on the 'free' version
: (V3) of the compiler. See: http://www.adtools.com/student/description.htm
: for details.

: I hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
