[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress OpenESQL Named Connections

_3 messages · 3 participants · 2000-06_

---

### NetExpress OpenESQL Named Connections

- **From:** "��� " <floydkc@attglobal.net>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393d700a_3@news1.prserv.net>`

```
I can not get this to work.  I have a main program, which calls subroutine A
and then subroutine B.  Sub A does the connect and then sub B tries to use
the connection.  I've tried various combinations of the CONNECT syntax; and
tried using host variables and literals for the connection name.  The
connection works, but the SET CONNECT returns SQLSTATE IM001 with a message
'Connection name not found'.

I'm using the NetExpress ODBC driver for DB2 running under Win NT, and a DB2
UDB on NT.

Has anybody gotten named connections to work ?  What environment were you in
?  Samples of working code would be appreciated.

Thanks in advance for any help and advice,

Ken Floyd
Shaw Systems
kfloyd@shawsystems.com
```

#### ↳ Re: NetExpress OpenESQL Named Connections

- **From:** "Randy Zimmerman" <rzmerant@execpc.com>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393e7af4$0$95983@news.execpc.com>`
- **References:** `<393d700a_3@news1.prserv.net>`

```
The SET CONNECTION statement is only needed if the application is doing
connects to multiple data sources and will not work with db2 udb using the
ODBC precomiler  since the way ibm implemented SET CONNECTION (from IBM DB2
UDB SQL Reference)
"Although an interactive SQL facility might provide an interface that gives
the appearance of interactive execution, this statement can only be embedded
within an application program. It is an executable statement that cannot be
dynamically prepared. "

The ODBC precompiler/run time in Net Express transforms sql statements into
dynamic sql ODBC calls.  If you are only using one data source, your
application should work okay as described without the set connection.

If you need to connect to multiple data sources, then you are going to need
to compile the SET CONNECTION module with the DB2 precompiler (via the DB2
directive)

If you need some specific examples, please contact me at
randy.zimmerman@merant.com


"� " <floydkc@attglobal.net> wrote in message
news:393d700a_3@news1.prserv.net...
> I can not get this to work.  I have a main program, which calls subroutine
A
> and then subroutine B.  Sub A does the connect and then sub B tries to use
> the connection.  I've tried various combinations of the CONNECT syntax;
and
> tried using host variables and literals for the connection name.  The
> connection works, but the SET CONNECT returns SQLSTATE IM001 with a
message
> 'Connection name not found'.
>
> I'm using the NetExpress ODBC driver for DB2 running under Win NT, and a
DB2
> UDB on NT.
>
> Has anybody gotten named connections to work ?  What environment were you
in
> ?  Samples of working code would be appreciated.
>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: NetExpress OpenESQL Named Connections

- **From:** "Ken Floyd" <kfloyd@shawsystems.com>
- **Date:** 2000-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZjR%4.44$vg6.1124@client>`
- **References:** `<393d700a_3@news1.prserv.net> <393e7af4$0$95983@news.execpc.com>`

```
Thanks for the response.

I am using separately linked programs - main program A is an .exe;
subroutine A (which establishes the connection) is A.dll; subroutine B
(which uses the connection) is B.dll.  The NetExpress ODBC documentation
says that when using separately linked modules like this that I have to use
named connections.

I did get my code to work.  I had used the directive SQL THREAD=ISOLATE.
Changing to THREAD=SHARE got the named connections working.

My code is not now using threads, so I'm not clear why ISOLATE vs SHARE
should make any difference.  Can you shed any light on this ?  I was testing
under Animator - maybe it uses threads.

Eventually, I'll want this to work under CICS TX Series 4.3.  It uses
threads (I think) to handle what it calls 'application servers'.  When a
transaction starts, it's 'assigned' to one of the application servers. I'll
have my first program (A) make the connection, then do a CICS LINK to the
'business rule' module (B).  That module will CALL an I/O subroutine (C),
which will do a SET CONNECTION then whatever SQL is required.  The
connection name (established by program A) will be passed along from program
to program in a control block.  I plan to use CICS Temp storage (or
something) to make sure that each transaction uses a different named
connection.

Whether I'll need THREAD=ISOLATE then is a question.  It seems to me that I
will.  If you can answer this question, I would appreciate it.  If you have
any samples of code using ODBC in combination with CICS, I would really like
to seem them.

Thanks in advance,
Ken Floyd
Shaw Systems
kfloyd@shawsystems.com

Randy Zimmerman wrote in message <393e7af4$0$95983@news.execpc.com>...
>The SET CONNECTION statement is only needed if the application is doing
>connects to multiple data sources and will not work with db2 udb using the
>ODBC precomiler  since the way ibm implemented SET CONNECTION (from IBM DB2
>UDB SQL Reference)
>"Although an interactive SQL facility might provide an interface that gives

>the appearance of interactive execution, this statement can only be
embedded
>within an application program. It is an executable statement that cannot be
>dynamically prepared. "
…[15 more quoted lines elided]…
>> I can not get this to work.  I have a main program, which calls
subroutine
>A
>> and then subroutine B.  Sub A does the connect and then sub B tries to
use
>> the connection.  I've tried various combinations of the CONNECT syntax;
>and
…[22 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
