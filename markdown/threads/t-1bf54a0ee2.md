[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus vs AcuCobol

_30 messages · 16 participants · 2002-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus vs AcuCobol

- **From:** ssmith@adelaidebank.com.au (Simon Smith)
- **Date:** 2002-03-07T14:24:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
Hello

I'm looking for some objective insight into the relative benefits of
MicroFocus Cobol and AcuCobol in a Win2000 environment.

One of our subsidurary companies is currently running an application
written in ICOBOL and accessing ISAM files.  The 4 developers have no
IDE and little support infrastructure.  The plan is to migrate to
Win2000 and SQL/Server (to replace the ISAM).  This will involve quite
a bit of redevelopment but it should give the application a new lease
on life.  It should also significantly enhance the developer's ability
to respond to change request from business units.

Thanks

Simon Smith
Adelaide Bank Limited
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** none@none.com (wildman)
- **Date:** 2002-03-08T00:20:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c88159d.1805034@news.earthlink.net>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
I just finished porting a system from a mini computer to NT with Net
Express and I'm very happy with the results.  

The ported application is more portable than it ever was.  It can now
be ported to Linux or Unix - easily.  Cobol & SQL are both highly
portable languages and once combined, the application will deliver for
a long time - perhaps longer than it already has.

As for the IDE, well, your legacy folks will love it.  The compiler
license isn't cheap - but you get what you pay for.  I found the
support well above average.

On 7 Mar 2002 14:24:59 -0800, ssmith@adelaidebank.com.au (Simon Smith)
wrote:

>Hello
>
…[14 more quoted lines elided]…
>Adelaide Bank Limited
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** "Erlend Moen" <erlend.moen@disystemer.no>
- **Date:** 2002-03-08T11:42:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c889590@news.wineasy.se>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
"Simon Smith" <ssmith@adelaidebank.com.au> wrote in message
news:64826f50.0203071424.2d72933b@posting.google.com...
> Hello
>
> I'm looking for some objective insight into the relative benefits of
> MicroFocus Cobol and AcuCobol in a Win2000 environment.

I've been working with AcuCobol for 10 years now.
Our first project was converting from the old MS Cobol (2.1?) to Acu. No
problems at all.
In 1995 I started in a new job where we converted from Wang-Cobol to Acu
running on SCO-Unix server with Win-clients. Again - no problems at all.

I began with GUI-programming in 2000 on AcuGT as it is called now. We have
WinNT, Win2K, WinXP and 98/ME as clients, works like a dream. I can do
almost anything directly from Acu, I can call Windows API, DLL's etc. etc.
We have a tight interaction with several Delphi-application as well,
communicating via DLL's.

One of the things I like best with AcuCorp, is their willingness to support
their customers. I can email a question and I will get an answer the same
day in 9 out of 10 times. They are also very responsive when it comes to
actually bug-reports. They do not try to hide the bugs, but file them and
give me feedback when they have solved them. If it's a critical bug for me,
I can order a patch if I cant wait for the next release.

The compiler is very good, but so is Micro Focus I believe, but you should
also emphasize the companys willingness to take care of you as a customer. I
have never regret that we chose AcuCorp, and I see no reason not to stay
with them further.

Regards,
Erlend Moen
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** davidcfield@yahoo.com.au (David Field)
- **Date:** 2002-03-08T20:29:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8915964.0203082029.3a585e08@posting.google.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
ssmith@adelaidebank.com.au (Simon Smith) wrote in message news:<64826f50.0203071424.2d72933b@posting.google.com>...
> Hello
> 
…[14 more quoted lines elided]…
> Adelaide Bank Limited

Hello Simon,

We have been developing with Acucobol for 8 years. We started off with
Icobol in 1981, switched to Ace Cobol (an ICobol compatible product)
in 1983, attempted to move to RM/Cobol in 1992 and eventually moved to
AcuCobol in 1993. We have also used Microfocus Cobol and Net Express
on occasions over the years.

Our original selection criteria was based purely on Icobol
compatibility - we did not have the resources to do a lot of
redevelopment and our Landmark product had to be ported to a Prime
platform in a very short period of time. Our original port was done
with Acucobol 1.5 - we had to make a few changes but it was relatively
painless. If we had the opportunity to wait until Acucobol version
2.0, we would have had to do virtually no work at all, as additional
Icobol compatibility switches were added by Acucorp in that release.

We have used many of the facilities Acucorp offers, including doing a
full GUI version of our product, using Acu4GL for Informix and Oracle,
extensive use of AcuODBC and integration of external facilities such
as IBM MQSeries, Active X controls and messaging via our e-mail
integration engine, MapiLand. We are also active members of the
Acucorp beta test program.

We have found the overall quality of the product range to be very good
and if you are moving from an Icobol environment, can highly recommend
the compability levels.

Hope this helps

David Field
Director
Landmark Software Pty Ltd
President Acucorp Australia Developers Group
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** geert.borstlap@anubex.com (Geert)
- **Date:** 2002-03-13T05:59:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fe0f0846.0203130559.37f42d70@posting.google.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
... to replace the ISAM ...

It is simpy said, but in practice it is not that evident.
It is a risky rewriting/re-engineering process!

We've already done many of those conversions, so I'll try to give you
some
background: About a year ago, we developed a tool for a number of
banks in Luxemburg and Switzerland that is doing an automated
conversion from ISAM to RDBBMS. It's called the "anugen-IO"
(generating IO-modules), and it converts
automatically all COBOL-programs containing ISAM file-IO to the same
COBOL-programs but with it's data stored in an RDBMS. It also
generates the needed
CTRL files to load the data in the RDBMS. Normally we're doing
migrations of legacy platforms towards modern technology, and the
"upgrade" of Index-sequential COBOL files to a RDBMS tables (and
changing all infected sources automatically) is a spin-off project
leading it's own life now.

Of course we can't simply change every READ in a FETCH, a WRITE in an
INSERT, REWRITE -> UPDATE, ...   This would be too easy.

There are 3 mayor problems when moving from C-ISAM towards RDBMS.
1) A sequence of COBOL file actions (OPEN, START, READ NEXT, READ
PREVIOUS, WRITE, INSERT, CLOSE, ...) works differently in an RDBMS.
You
can READ on the primary key, continue READing on an alternate key,
switch direction by a READ PREVIOUS, ... and the fun has just begon.
2) The datatypes available in Oracle/SQL-server/DB2/... is only a
subset of
all datatypes available in COBOL.
3) An FD (File Description) in COBOL can be defined with levels (03,
05,
07, ...) and OCCURS (arrays) whereas Oracle/SQL-server/DB2 can only
use a
flat buffer whithout OCCURS.

All problems are solved in an IO-module. This IO-module (one per file,
so in Oracle/SQL-server/DB2 terms one per table) ensures that we get
the same data, as
you would get with the ISAM version. All COBOL-programs are parsed,
stored in a COBOL-tree and regenerated, and every FILE-statement
(READ, WRITE, OPEN, ...) is automatically changed into a CALL
statement, calling the appropriate IO-module.

Well, the work is done in 5 steps. (which means you run the
"anugen-IO"-tool 5 times)

Step 1) (optional) analyse all COBOL sources and count the numbers of
ISAM files used and the number of "file-IO statement" replacements
that needs to be done. This gives you an idea how much work you have
if you want to do it manually.
Step 2) generates the CREATE TABLE scripts.
Step 3) generates an IO-module per FD description (ISAM file)
Step 4a) (fast data migration): generates the CTRL files per FD
description
Step 4b) (slow data migration): generates a small COBOL program that
reads the complete ISAM file and INSERT record per record in the
RDBMS.
Step 5) replaces every file IO statement in your COBOL program, and
replace it by the appropriate CALL IO-module statement. These new
statements are doing functional exactly the same as the original ones.

Now you create the tables in the database, migrate the data, compile
the IO-modules (.pco -> .o), compile and link your final exe's (with
the generated IO-modules) and you are ready.
After these steps you have your old COBOL-application working exactly
the same, however the data is stored in an RDBMS now. No manual work
needs to be done.

Some optimisation which are built in:
1) renaming: It is possible to choose new names for your fields in the
RDBMS table.
2) The IO-module can be generated for all keys (primary and alternate
keys) or for a certain key alone. This produces smaller object-code.
3) The IO-module can be generated in an optimalisation mode. When you
would read your complete file  in certain COBOL programs (in
RDBMS-terminology i.e a full table scan) this would boost performance.

We got good results in production. There was no performance penalty to
be paid.

If you want to know more: www.anubex.com and push the "the migration
Centre" button.

Hope this info helps.
Geert
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-14T10:13:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c8fc2af_6@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
Simon,

I have a tool I wrote (ISAM2RDB) that analyses the COBOL source and
generates an equivalent RDB in third normal form. It has been used
successfully in Australia and I can give you a Company reference in
Melbourne.

It is a 3 step process:

1. Create the database.
2. Create the modules to load the database.
3. Load the database.

The final step of  converting the application is "manual with assistance". I
thought about writing something to automate this, but the possibilities are
so huge and there hasn't been the demand that would warrant it. It is also a
good thing to review the existing code as part of the conversion.

Alternatively, I will gladly give a fixed price to deliver the converted,
loaded, database. (It works out at around $Aus30.00 per ISAM file for SQL
Server, if you have more than 50 files).

You will still need to convert the Application.

Pete.

Simon Smith <ssmith@adelaidebank.com.au> wrote in message
news:64826f50.0203071424.2d72933b@posting.google.com...
> Hello
>
…[14 more quoted lines elided]…
> Adelaide Bank Limited



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-03-16T08:04:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0203160804.7c30726d@posting.google.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
I know you specifically mentioned ACUCOBOL vs MicroFocus - but have
you considered the alternatives?  Fujitsu, RM, TinyCOBOL?

Main difference between Acu and MicroFocus - P-Code vs Native Code.


ssmith@adelaidebank.com.au (Simon Smith) wrote in message news:<64826f50.0203071424.2d72933b@posting.google.com>...
> Hello
> 
…[14 more quoted lines elided]…
> Adelaide Bank Limited
```

##### ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "Christer O. Jonsson" <christer.o.jonsson@home.se>
- **Date:** 2002-03-16T18:37:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6vvtj$hj1ga$1@ID-134254.news.dfncis.de>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160804.7c30726d@posting.google.com>`

```
Native code that I know, but P-code whats that?

Christer O. Jonsson
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-16T18:16:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-JouWQL9DCqXY@thishost>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160804.7c30726d@posting.google.com> <a6vvtj$hj1ga$1@ID-134254.news.dfncis.de>`

```
On Sat, 16 Mar 2002 17:37:17 UTC, "Christer O. Jonsson" 
<christer.o.jonsson@home.se> wrote:

> Native code that I know, but P-code whats that?
> 
> Christer O. Jonsson
> 
> 

I think it refers to the Pascal "P-code" that was executed by a 
virtual machine. Java and other languages use the same idea, the 
source is translated into a "machine language" that is executed by a 
virtual machine rather than the souce code being translated in machine
language that is executed directly by the computer hardware. 

The Microfocus compiler can generate both "native code" (.obj files) 
and P-code (.int files)

The foregoing was overly simplistic but ... :-)
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 4)_

- **From:** "Christer O. Jonsson" <christer.o.jonsson@home.se>
- **Date:** 2002-03-16T19:19:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a702d2$h9i71$1@ID-134254.news.dfncis.de>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160804.7c30726d@posting.google.com> <a6vvtj$hj1ga$1@ID-134254.news.dfncis.de> <ZpzG4UNLyRNq-pn2-JouWQL9DCqXY@thishost>`

```
Thanks!

Get the general idea.

Christer O. Jonsson
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-03-16T23:39:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sIQk8.9297$e33.683@nwrddc01.gnilink.net>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160804.7c30726d@posting.google.com> <a6vvtj$hj1ga$1@ID-134254.news.dfncis.de>`

```
Christer O. Jonsson <christer.o.jonsson@home.se> wrote in message
news:a6vvtj$hj1ga$1@ID-134254.news.dfncis.de...
> Native code that I know, but P-code whats that?

"P-code" is sometimes used as an abbreviation for "pseudo-code;" but this
nickname is used primarily by those who cannot spell "pseudo."

MCM
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-03-16T08:06:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0203160806.34326187@posting.google.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
While I'm at it - 

Sometimes people migrate to RDB for no discernable reason other then
their fear/ignorance if ISAM files.  SQL server certainly won't be
less expensive - is there a good reason for the conversion to such for
data storage?


ssmith@adelaidebank.com.au (Simon Smith) wrote in message news:<64826f50.0203071424.2d72933b@posting.google.com>...
> Hello
> 
…[14 more quoted lines elided]…
> Adelaide Bank Limited
```

##### ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-16T18:31:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com>`

```
Usually conversion to using an RDBMS system is to allow other 
applications access to the data processed by the COBOL (or any other 
langauge) programs.

The RDBMS data is readily available to third party query and report 
writer tools that support an ODBC interface. One can choose tools that
provide ease of use to the end user community without requiring a 
large investment in additional custom code. 

The cost of the RDBMS plus "shrink wrap" query/reporting is low in 
comparison to the cost of custom code to provide the same level of 
functionality.

I would like to offer that SQL Server is not the best tool for the 
RDBMS engine however. If you are going to invest in an RDBMS something
like IBM's DB2 will offer much more functionality.

My personal preference is Microfocus COBOL over AcuCOBOL but that is 
because I prefer applications that are built as EXEs and DLLs rather 
than many individual interpreter code files.

Lorne

On Sat, 16 Mar 2002 16:06:37 UTC, thaneh@softwaresimple.com (Thane 
Hubbell) wrote:

> While I'm at it - 
> 
…[23 more quoted lines elided]…
> > Adelaide Bank Limited
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-17T10:09:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9537c9_5@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost>`

```
Absolutely endorse this 100%, Lorne.

The arguments about which RDBMS is "best" is trivial. ANY of them are better
than being locked into the COBOL file system and thereby isolated. I have
posted at length on this subject both here and elsewhere...the file system
is one of the major factors contributing to the "Death of COBOL" and the
perception of COBOL within Corporates as something which "...the sooner we
are rid of it, the better..."

There is nothing intrinsically wrong with the COBOL file system. We all know
that superb data storage and retrieval systems have been built with it and
many of them are still in operation.

But the World has moved on, and Data must be shared. Writing interfaces and
downstream feeds to the Corporate Data resource is NOT an acceptable
solution any more. The data resource must be OPEN to access by standard
software and able to be queried by non-technical people without having to
wait for as long as it takes the IT department to prioritise, develop, test,
and debug, a COBOL program... RDB meets this need and that is why it is
successful.

Pete.

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost...
> Usually conversion to using an RDBMS system is to allow other
> applications access to the data processed by the COBOL (or any other
…[32 more quoted lines elided]…
> > ssmith@adelaidebank.com.au (Simon Smith) wrote in message
news:<64826f50.0203071424.2d72933b@posting.google.com>...
> > > Hello
> > >
…[18 more quoted lines elided]…
> Lorne Sunley



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 4)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-03-18T22:03:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yutl8.66$xs2.41950340@newssvr11.news.prodigy.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <3c9537c9_5@Usenet.com>`

```

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3c9537c9_5@Usenet.com...
[snip]
> The arguments about which RDBMS is "best" is trivial. ANY of them are
better
> than being locked into the COBOL file system and thereby isolated.
[snip]
> There is nothing intrinsically wrong with the COBOL file system. We all
know
> that superb data storage and retrieval systems have been built with it and
> many of them are still in operation.
>
> But the World has moved on, and Data must be shared.

[At the risk of posting an advert]

But Pete, why abandon that which works to gain something that may be gained
using another tool.

Relativity (http://www.liant.com/products/relativity/) can make COBOL data
quite accessible to the ad hoc query (not to mention ASP programmer, PHP
programmer, Java programmer, ...) without affecting the 'back office'
application.
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-20T03:43:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c975e98_10@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <3c9537c9_5@Usenet.com> <yutl8.66$xs2.41950340@newssvr11.news.prodigy.com>`

```

Tom Morrison <t.morrison@liant.com> wrote in message news:yutl8.66> >
> > But the World has moved on, and Data must be shared.
>
> [At the risk of posting an advert]
>
> But Pete, why abandon that which works to gain something that may be
gained
> using another tool.
>
For the same reason that we moved on from Ox-carts, sleds, and flint tools
(all of which worked), to Ferraris, speedboats, titanium saws and laser
drills. The current is replaced by the new, not because the current doesn't
work, but because the new works BETTER.

> Relativity (http://www.liant.com/products/relativity/) can make COBOL data
> quite accessible to the ad hoc query (not to mention ASP programmer, PHP
> programmer, Java programmer, ...) without affecting the 'back office'
> application.
>
Tom, not having used Relativity, I cannot make fair comment. There are a
number of tools that can "bridge" between the file system and RDB technology
(I've written one myself...<G>). At the end of the day, it isn't the Bridge
that is needed, it is open access directly by all "standard" corporate
tools.  It isn't just about ad hoc queries, it is about the extension and
joining of new requirements with the existing data resource. RDB technology
is our best bet until Content Addressable File Store (CAFS) becomes a viable
and cheap alternative (about 15 years, I reckon).

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-20T07:10:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9835F0.655C075C@Azonic.co.nz>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <3c9537c9_5@Usenet.com> <yutl8.66$xs2.41950340@newssvr11.news.prodigy.com> <3c975e98_10@Usenet.com>`

```
Peter E. C. Dashwood wrote:
> 
> is our best bet until Content Addressable File Store (CAFS) becomes a viable
> and cheap alternative (about 15 years, I reckon).

I remember seeing one of them spread about over the computer floor at
Bracknell a quarter of a century ago as they were assembling yet another
prototype.
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-20T12:09:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c97d67f_11@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <3c9537c9_5@Usenet.com> <yutl8.66$xs2.41950340@newssvr11.news.prodigy.com> <3c975e98_10@Usenet.com> <3C9835F0.655C075C@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C9835F0.655C075C@Azonic.co.nz...
> Peter E. C. Dashwood wrote:
> >
> > is our best bet until Content Addressable File Store (CAFS) becomes a
viable
> > and cheap alternative (about 15 years, I reckon).
>
> I remember seeing one of them spread about over the computer floor at
> Bracknell a quarter of a century ago as they were assembling yet another
> prototype.

I give ICL credit for at least researching and building something along
these lines. Unfortunately, it was too expensive, too complex and
consequently, non-viable. I don't know what the state of this is today at
ICL. Under the Fujitsu umbrella it may have been shelved.

I know of at least one project which is currently investigating this area
but I am not allowed to give any clues...<G>

Seems a pretty fair bet that as hardware efficiency accelerates, the idea of
a CAFS will be recycled and somebody somewhere will achieve the right
hardware/software balance to implement it. When it finally arrives it may
not be in the form of disk storage at all...

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-17T03:45:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gjUk8.16135$Ex5.1435823@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost>`

```
Ah!

RDBMS "is to allow other applications access to the data processed by the
COBOL..."

In other words this method of storage helps avoid using uniform and standard
metods! Yes? No?

I was given the purpose of Relational data organization was because it made
finding it faster.
Use a table concept, read right and down to the answer kind of a thing could
follow math
logic and not involve looking procedurally for the answer except with
another tool called .... which
had to be added to the front end of the search of the data base.

I see the use of other applications via call and return, I don't see the
segmentation of lookup logic
to some interface not a part of the uniform and standard I/O package Except
as a method of
blocking one's competitors or one's users from a clear cut procedure.

Just what was the feature requiring the use of RDBMS?  Make it simple to
compute, and you can stand
on your head to use it. Why couldn't the need be added to the standard? To
whose advantage was that?

How much hardware and software did it sell? Just who made out?

Old men have a time adjusting to the world that has not stopped "to think".

IMNSHO,

Warren Simmons

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost...
> Usually conversion to using an RDBMS system is to allow other
> applications access to the data processed by the COBOL (or any other
…[32 more quoted lines elided]…
> > ssmith@adelaidebank.com.au (Simon Smith) wrote in message
news:<64826f50.0203071424.2d72933b@posting.google.com>...
> > > Hello
> > >
…[18 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 4)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-17T04:12:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-8sKGXDMNXx7g@thishost>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <gjUk8.16135$Ex5.1435823@bgtnsc04-news.ops.worldnet.att.net>`

```
On Sun, 17 Mar 2002 03:45:16 UTC, "398199821" 
<warren.simmons@worldnet.att.net> wrote:

> Ah!
> 
…[5 more quoted lines elided]…
> 

This method helps "using uniform and standard methods" not "avoid 
using ...".

The RDBMS engine does provide a standard and uniform access to the 
data base.

> I was given the purpose of Relational data organization was because it made
> finding it faster.

An RDBMS engine is not faster than COBOL ISAM file I-O. There is a lot
more overhead in processing in an RDBMS engine. Although some 
processing is faster with an RDBMS engine, but a well written COBOL 
progam can probably do faster processing for particular application 
requirements.

> Use a table concept, read right and down to the answer kind of a thing could
> follow math
…[83 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-17T03:57:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost>`

```

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost...
> Usually conversion to using an RDBMS system is to allow other
> applications access to the data processed by the COBOL (or any other
> langauge) programs.

And the downside is that user-written programs - like an Excel spreadsheet -
can really muck up the data.

I once had to straighten out a oil well database that had been 'corrected'
by various users with EasyTrieve. Some wells had depths of -11,000 feet
which meant the wells each had two miles of pipe sticking up toward the
clouds.
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 4)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-17T04:08:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-yGbH2SfJO4pP@thishost>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com>`

```
On Sun, 17 Mar 2002 03:57:49 UTC, "JerryMouse" <nospam@invalid.com> 
wrote:

> 
> <lsunley@mb.sympatico.ca> wrote in message
…[13 more quoted lines elided]…
> 

Well ...

The administrator of the RDBMS package is responsible for the granting
of access to the data tables in the database. Any good RDBMS allows 
the DBA to grant "read only" permission to a data table for a user or 
group of users. If this is done properly then the "user written, death
to data integrity" programs do not have the opportunity to screw 
around with the data.

If the DBA does not do her/his/its job then data destruction is the 
normal result.

AFAIK an RDBMS like IBMs DB2 does allow the restriction of users to 
"read only" access to the data tables. Of couse you could do something
really idiotic and store your data in an "MS Access" database and 
allow unrestricted access to the data.
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-17T05:01:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9422A3.24F02B5C@shaw.ca>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com> <ZpzG4UNLyRNq-pn2-yGbH2SfJO4pP@thishost>`

```


lsunley@mb.sympatico.ca wrote:

> On Sun, 17 Mar 2002 03:57:49 UTC, "JerryMouse" <nospam@invalid.com>
> wrote:
…[36 more quoted lines elided]…
> Lorne Sunley

See my message on DB Security - Guess I'm one of the idiots that you are referring
to <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T13:13:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c954508_8@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com> <ZpzG4UNLyRNq-pn2-yGbH2SfJO4pP@thishost>`

```
Lorne,

you are incorrect on a couple of points in this thread, though in general, I
would agree with your arguments in favour of RDB.

1. ISAM I-O is faster than RDB IO.

This HAS to be qualified. For large sequential volumes of data it is
certainly true... In all other cases it MAY not be. I don't want to go into
this in detail because it is of little interest to the majority of people
here, but consider an ISAM file where second level overflow has occurred or
the indexes have not been re-organised for some time...The RDB is self
re-organising (think of VSAM on your DB2 database) and there is therefore a
fair chance that on random access it will kill the ISAM file. Anyway, it is
NOT the speed (or otherwise) of access which points us towards RDBs, it is
the openness of access and the removal of the requirement for a COBOL
program to be written every time a user department wants data.

2. Your scathing comments regarding MS ACCESS are quite out of place and
indicate that you have not used the latest versions of ACCESS.

ACCESS is a true RDB which implements the current standard for SQL. It has
ALL the permissions and restrictions which DB2 has. (In fact , I have
converted a Mainframe DB2 application to the PC and used exactly the same
SQL against ACCESS as was used against DB2...it was a doddle.) The only
difference is that it can be used by users without the control of the IT
department. (Some IT departments are not happy about this...)

I use ACCESS to simulate major file conversions and take them off-line from
the mainframe or whatever platform they are currently existing on. It is an
excellent implementation of the Relational Model. You can simulate the
proposed system and get all the SQL right and the tables built and loaded
without any impact on the existing platform. Then simply export the table
definitions and load to the target. It is every bit as much an RDB as
INGRES, ORACLE, DB2, UDB, DATACOM, or SQL SERVER (in fact, thanks to the
miracle of ODBC I have used it with all of the above...)

The poor reputation of ACCESS stems from people writing very bad "Database
applications" using ACCESS BASIC. If it is used purely as a repository,
accessed with COBOL/SQL/ODBC it is superb.

Pete.
<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-yGbH2SfJO4pP@thishost...
> On Sun, 17 Mar 2002 03:57:49 UTC, "JerryMouse" <nospam@invalid.com>
> wrote:
…[8 more quoted lines elided]…
> > And the downside is that user-written programs - like an Excel
spreadsheet -
> > can really muck up the data.
> >
> > I once had to straighten out a oil well database that had been
'corrected'
> > by various users with EasyTrieve. Some wells had depths of -11,000 feet
> > which meant the wells each had two miles of pipe sticking up toward the
…[22 more quoted lines elided]…
> Lorne Sunley



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Microfocus vs AcuCobol

_(reply depth: 6)_

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-18T03:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2adl8.15595$tP2.1359388@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com> <ZpzG4UNLyRNq-pn2-yGbH2SfJO4pP@thishost> <3c954508_8@Usenet.com>`

```
Peter points out some problems with ISAM I-O.
I find this concern out of wack with my experience.
ISAM as first implemented dealt with overflow requiring re-orgs.
Many organizations found ways to enhance ISAM to remove this.
However, since my exposure is very old, my experience may be unique,
maybe just in my mind, but I remember trying to get the code from
..... in the 60's.

Warren Simmons
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3c954508_8@Usenet.com...
> Lorne,
>
> you are incorrect on a couple of points in this thread, though in general,
I
> would agree with your arguments in favour of RDB.
>
…[3 more quoted lines elided]…
> certainly true... In all other cases it MAY not be. I don't want to go
into
> this in detail because it is of little interest to the majority of people
> here, but consider an ISAM file where second level overflow has occurred
or
> the indexes have not been re-organised for some time...The RDB is self
> re-organising (think of VSAM on your DB2 database) and there is therefore
a
> fair chance that on random access it will kill the ISAM file. Anyway, it
is
> NOT the speed (or otherwise) of access which points us towards RDBs, it is
> the openness of access and the removal of the requirement for a COBOL
…[12 more quoted lines elided]…
> I use ACCESS to simulate major file conversions and take them off-line
from
> the mainframe or whatever platform they are currently existing on. It is
an
> excellent implementation of the Relational Model. You can simulate the
> proposed system and get all the SQL right and the tables built and loaded
…[28 more quoted lines elided]…
> > > by various users with EasyTrieve. Some wells had depths of -11,000
feet
> > > which meant the wells each had two miles of pipe sticking up toward
the
> > > clouds.
> > >
…[28 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ DataBase Security - WAS Re: Microfocus vs AcuCobol

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-17T04:55:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C942162.BA974FDD@shaw.ca>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com>`

```


JerryMouse wrote:

> <lsunley@mb.sympatico.ca> wrote in message
> news:ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost...
…[10 more quoted lines elided]…
> clouds.

Valid observation and raises the issue of security of DB information. Let's
expand on Jerry's comment :-

I'm in the process, (like Jerry - it's the oil/gas industry) of switching from
COBOL files (ISAMs etc.) to Microsoft Access. M/S Access is being used solely as
the repository for the data, with data input being validated or calculated via
COBOL programs.

Sole reason I'm switching - most of the major corporations here in Calgary as HQ
for oil/gas, use some form of DB package, DB2, Oracle etc. Inevitably what I am
storing in either COBOL files or a DB is not necessarily the format the oil
company maintains their system in. Two options :-

- (1) Restrict user access to the core DB - would necessitate me writing  CSVs
each time they wanted to extract to do something different. (While an irritant,
also a plus for me - extra bucks <G>).

- (2) Allow them entry directly into M/S Access - obviates the necessity of my
writing or receiving CSVs and they can manipulate the data, (generating
additional report tables etc.), as they see fit..

#2 is where Jerry's downside comes into play. By storing current thicknesses of
'Items' the purpose of the application is to trigger when sufficient corrosion
has occurred to indicate either (a) Below acceptable Minimum thickness, or (b)
The Life Expectancy (number of operative years left) is starting to get
dangerously close.

There is no logical reason that an end user should need to change the inspection
data recorded by inspection companies from various Non-Destructive Testing
methods, (Ultrasonics, X-rays, Radiography, Coupons  etc.). Both down there in
Texas and up here in Alberta it is a government requirement that oil
corporations confirm on an annual basis that all vessels (production units) have
been inspected.

Assume some failure due to corrosion, ( a plant shutdown could mean over
$3million lost per day). But again, think of something as disastrous as Bophal,
India. Logically the inspection company's data, (stored via COBOL), should have
indicated this to the end user corporation. Now assume somebody in the oil
company 'monkies' with the inspection data to hide the obvious corrosion. Who is
responsible :-

- Me, the application developer
- the Inspection Company, or
- the Oil Corporation  ? (Don't forget the latter can employ a bevy of legal
sharks to 'prove' their nose is clean.)

Now translate the same sort of problem to a financial DB used by our friends at
say, Enron.

Anybody out there got some recommendations about DB security, or can point us to
references on the topic ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: DataBase Security - WAS Re: Microfocus vs AcuCobol

_(reply depth: 5)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-17T15:34:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-LGpX7hfBxRwI@thishost>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com> <3C942162.BA974FDD@shaw.ca>`

```
Yes I would say you are one of the "idiots" <G>  (from other post)

On Sun, 17 Mar 2002 04:55:45 UTC, "James J. Gavan" <jjgavan@shaw.ca> 
wrote:

> 
> 
…[23 more quoted lines elided]…
> 

If your COBOL programs use ODBC to access the data in the "MS Access" 
database, they can do the same thing if the data tables are stored in 
some other RDBMS. All you have to do is write the program so that it 
uses SQL 92 compliant SQL code and just about any RDBMS engine can be 
used to store the data. I recently wrote an "add in" to the 
Grandmaster Suite Payroll package using the Microfocus   COBOL ESQL 
option that allows export/import to an ODBC compliant database engine.
It works with DB2, SQL Server, and even Excel and "text files" through
the ODBC interface.

> Sole reason I'm switching - most of the major corporations here in Calgary as HQ
> for oil/gas, use some form of DB package, DB2, Oracle etc. Inevitably what I am
…[6 more quoted lines elided]…
> 

Revenue is revenue, and a good thing :-)

> - (2) Allow them entry directly into M/S Access - obviates the necessity of my
> writing or receiving CSVs and they can manipulate the data, (generating
> additional report tables etc.), as they see fit..
> 

You should have option 3 - allow the user to choose the database where
the data is stored. The ODBC interface shipped with Windows allows a 
DSN to be defined for just about any database engine. Providing option
3 allows the user of the application to determine where the data is 
stored.

> #2 is where Jerry's downside comes into play. By storing current thicknesses of
> 'Items' the purpose of the application is to trigger when sufficient corrosion
…[18 more quoted lines elided]…
> - Me, the application developer

Yes, you are responsible as you did not provide a third option for 
support of user determined data storage and security. 

> - the Inspection Company, or

They carry a responsibility if they cannot show that the data was 
"monkied" with

> - the Oil Corporation  ? (Don't forget the latter can employ a bevy of legal
> sharks to 'prove' their nose is clean.)
> 

They carry a responsibility if their employees "monkied" and the 
changes were ordered my "management".

If you provide the "user determined" storage and security then the 
legal sharks will have a harder time of placing the blame on the 
application developer. You can make it an item in the contract/license
for the use of the software - it may not help much, but something is 
better than nothing.

> Now translate the same sort of problem to a financial DB used by our friends at
> say, Enron.
> 

Based on the news bits I have seen, the scenario of outright fraud 
supported by the "management" and the outside auditors will defeat any
security measures that can be put in place.

> Anybody out there got some recommendations about DB security, or can point us to
> references on the topic ?
> 
> Jimmy, Calgary AB
> 

You can use "triggers" in the database to timestamp modifications of 
the rows in the data tables and capture the time and user that did the
modifications. Coupled with a decent RDBMS security set up this will 
at least identify the culprit doing the data modifications, although 
this can be bypassed by a competent DBA - but then the responsibility 
for data security rests on that same DBA.....

The data tables would have to have a "created timestamp" and a 
"modified timestamp" for each row. The values set could determine if 
the row was modified after it was inserted into the table.

Use of triggers for this is supported by DB2, SQL Server and Oracle at
least (probably PostgreSQL as well).


Both DB2 and Oracle support individual user access settings per table,
SQL Server sort  of does this but it is a bit complicated.

You would have to allow for the application to create its data tables 
for each of the database engines supported, as there are differences 
in the data definition langauges (DDL) for each engine. The SQL syntax
used for data manipulation should adhere to the SQL 92 standard as 
this is supported by most database engines and/or ODBC drivers.


<Start Plug>
You can download a personal developers edition of IBMs DB2 product 
from < 
http://www14.software.ibm.com/webapp/download/category.jsp?s=c&cat=dat
a > This is a single user version of the full DB2 product. You can use
it to develop applications without any license fees.

I believe an equivalent is available from Oracle as well < 
http://www.oracle.com >

and PostgreSQL is freely available and is open source as well < 
http://www.postgresql.org/ >

<End Plug>
```

###### ↳ ↳ ↳ Re: DataBase Security - WAS Re: Microfocus vs AcuCobol

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T13:29:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c954519_8@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com> <ZpzG4UNLyRNq-pn2-yyqDHmzb2jzy@thishost> <1vUk8.265598$pN4.16524374@bin8.nnrp.aus1.giganews.com> <3C942162.BA974FDD@shaw.ca>`

```
Jimmy, Lorne has covered this in his response and it is fine.

Couple of points...

If you use a multi-tiered architecture you don't need database triggers to
timestamp the access. It can be built directly into the Update Pathway.
Update permission is restricted only to programs in that level.

It's not that there is anything wrong with triggers per se, but they lock
you in to a particular database and they are not part of your application
control.

You should also consider generating an audit trail where parties other than
yourself are granted update access or permission to use the update path.

I would disagree with Lorne that you need another RDB (I don't share his
contempt for ACCESS) but that is really something for you to decide.

As Lorne observed, if people really want to bend things they will. The best
you can hope for is to know who stole the horse and when, before you bolt
the stable door...

Pete.


James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C942162.BA974FDD@shaw.ca...
>
>
…[8 more quoted lines elided]…
> > And the downside is that user-written programs - like an Excel
spreadsheet -
> > can really muck up the data.
> >
> > I once had to straighten out a oil well database that had been
'corrected'
> > by various users with EasyTrieve. Some wells had depths of -11,000 feet
> > which meant the wells each had two miles of pipe sticking up toward the
> > clouds.
>
> Valid observation and raises the issue of security of DB information.
Let's
> expand on Jerry's comment :-
>
> I'm in the process, (like Jerry - it's the oil/gas industry) of switching
from
> COBOL files (ISAMs etc.) to Microsoft Access. M/S Access is being used
solely as
> the repository for the data, with data input being validated or calculated
via
> COBOL programs.
>
> Sole reason I'm switching - most of the major corporations here in Calgary
as HQ
> for oil/gas, use some form of DB package, DB2, Oracle etc. Inevitably what
I am
> storing in either COBOL files or a DB is not necessarily the format the
oil
> company maintains their system in. Two options :-
>
> - (1) Restrict user access to the core DB - would necessitate me writing
CSVs
> each time they wanted to extract to do something different. (While an
irritant,
> also a plus for me - extra bucks <G>).
>
> - (2) Allow them entry directly into M/S Access - obviates the necessity
of my
> writing or receiving CSVs and they can manipulate the data, (generating
> additional report tables etc.), as they see fit..
>
> #2 is where Jerry's downside comes into play. By storing current
thicknesses of
> 'Items' the purpose of the application is to trigger when sufficient
corrosion
> has occurred to indicate either (a) Below acceptable Minimum thickness, or
(b)
> The Life Expectancy (number of operative years left) is starting to get
> dangerously close.
>
> There is no logical reason that an end user should need to change the
inspection
> data recorded by inspection companies from various Non-Destructive Testing
> methods, (Ultrasonics, X-rays, Radiography, Coupons  etc.). Both down
there in
> Texas and up here in Alberta it is a government requirement that oil
> corporations confirm on an annual basis that all vessels (production
units) have
> been inspected.
>
> Assume some failure due to corrosion, ( a plant shutdown could mean over
> $3million lost per day). But again, think of something as disastrous as
Bophal,
> India. Logically the inspection company's data, (stored via COBOL), should
have
> indicated this to the end user corporation. Now assume somebody in the oil
> company 'monkies' with the inspection data to hide the obvious corrosion.
Who is
> responsible :-
>
> - Me, the application developer
> - the Inspection Company, or
> - the Oil Corporation  ? (Don't forget the latter can employ a bevy of
legal
> sharks to 'prove' their nose is clean.)
>
> Now translate the same sort of problem to a financial DB used by our
friends at
> say, Enron.
>
> Anybody out there got some recommendations about DB security, or can point
us to
> references on the topic ?
>
> Jimmy, Calgary AB
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Microfocus vs AcuCobol

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-17T10:01:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9537c4_5@Usenet.com>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com> <bfdfc3e8.0203160806.34326187@posting.google.com>`

```

Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0203160806.34326187@posting.google.com...
> While I'm at it -
>
…[3 more quoted lines elided]…
> data storage?

C'mon Thane...give it up!

We've debated this endlessly and, while I respect your right to maintain
your opinion, surely it must be apparent by now that "fear and ignorance"
have nothing to do with it.

The advantages of moving away from the COBOL file system are manifest and
overwhelming. I said so 5 years ago and I say it today. The difference is
that now many other people are recognising it too.

Whether you personally are persuaded by the arguments or not, the market
place is voting with their feet. We will see more and more VSAM/ISAM
conversions to RDB.

"Resistance is futile..." <G>

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Microfocus vs AcuCobol

- **From:** "Sal Cambareri" <salcam@teleport.com>
- **Date:** 2002-03-19T17:37:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MHKl8.1388$s8.146731@newsread1.prod.itd.earthlink.net>`
- **References:** `<64826f50.0203071424.2d72933b@posting.google.com>`

```
Simon-
The conversion from ICOBOL to AcuCobol is trivial. Not only is the Acu
instruction set a complete superset of all of the ICOBOL verbs (e.g. DELETE
FILE xxxx), there are flags and switches available for both the compiler and
the runtime that account for all of the ICOBOL oddities (aka ANSI 85
variances) including, but not limited to, an identical implementation of the
Screen Section, initialization of the Working Storage, and DG specific file
statuses. As an ICOBOL users, you'll be very pleased with the speed and
flexibility of the Vision ISAM package included in the runtime. As someone
who lived for a long time with the ICOBOL ISAM limitations, I continue to be
impressed by its power speed and flexibility of the Vision ISAMs.  Some
people (e.g. Thane H.), for reasons I don't understand don't like the Acu
debugger.  I love it, especially the 5.1 version which empowers me to debug
in an intuitively reasonable way threaded COBOL.
In converting to Acu from ICOBOL, the only real headache my clients had 10
years ago (when we migrated) was that the #P passfile utility did not exist.
I ended up writing a COBOL replacement that has served pretty well. It was
possible to do so because AcuCOBOL provides so many useful COBOL extensions.
I haven't used MicroFocus for a couple of years, and frankly I just didn't
like it. The major annoyances were the too complex Animator, the Screen
Section variances with ICOBOL, and the limitation of source to 80 column
mode.  I've never tried to convert from ICOBOL to MicroFocus but I imagine
that if your source is in terminal mode, you will find the 80 column
conversion very time consuming.
Regards,
Sal
(No, I don't own stock in AcuCOBOL, but there are times I wish I did.)

"Simon Smith" <ssmith@adelaidebank.com.au> wrote in message
news:64826f50.0203071424.2d72933b@posting.google.com...
> Hello
>
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
