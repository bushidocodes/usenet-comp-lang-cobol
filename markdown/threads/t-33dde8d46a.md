[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can COBOL MVS be used to access Sybase & DB2?

_13 messages · 4 participants · 2000-04 → 2000-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### Can COBOL MVS be used to access Sybase & DB2?

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e4t65$iam$1@goblin.tdh.state.tx.us>`

```
I have a need to refresh data stored in Sybase with DB2 v5 data.   We can
extract the data into a flat file and then FTP & load into Sybase, but were
hoping to have a more direct method.
```

#### ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e6ndsfyr$GA.295@cpmsnbbsa04>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us>`

```
I thought Sybase offered a product capable of just what you are asking for .
. .

<pause for search through Sybase's website>

Oh yeah, middleware from Sybase called ClearConnect.

Go to this website:
http://www.sybase.com/products/entcon/clear_connect.html

Lead off paragraph of the product description goes like this:

Have a departmental, workgroup, or pilot application that requires access to
IBM DB2 data?
Sybase ClearConnect provides two-tier connectivity from any Windows 3.1,
Windows 95 or Windows NT platform (16- or 32-bit) directly to any IBM DB2
data source. With ClearConnect, applications such as those built with
Powerbuilder, Microsoft Access, Visual Basic, or other ODBC-compliant tools
can access and update DB2 data directly, without a middle-tier access
server.


If your Sybase isn't on a PC, try reading up on DirectConnect or even
OmniConnect (both also from Sybase).

I haven't used any of them, so I can't vouch for their effectiveness.  This
post is just FYI.


"Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote in message
news:8e4t65$iam$1@goblin.tdh.state.tx.us...
> I have a need to refresh data stored in Sybase with DB2 v5 data.   We can
> extract the data into a flat file and then FTP & load into Sybase, but
were
> hoping to have a more direct method.
>
>
>
```

##### ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e79b5$gam$1@goblin.tdh.state.tx.us>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04>`

```
Thanks Chris, I'll check them out.  Of course if a product purchase is
necessary, I may be out of luck.

"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
news:e6ndsfyr$GA.295@cpmsnbbsa04...
> I thought Sybase offered a product capable of just what you are asking for
.
> . .
>
…[9 more quoted lines elided]…
> Have a departmental, workgroup, or pilot application that requires access
to
> IBM DB2 data?
> Sybase ClearConnect provides two-tier connectivity from any Windows 3.1,
> Windows 95 or Windows NT platform (16- or 32-bit) directly to any IBM DB2
> data source. With ClearConnect, applications such as those built with
> Powerbuilder, Microsoft Access, Visual Basic, or other ODBC-compliant
tools
> can access and update DB2 data directly, without a middle-tier access
> server.
…[5 more quoted lines elided]…
> I haven't used any of them, so I can't vouch for their effectiveness.
This
> post is just FYI.
>
…[3 more quoted lines elided]…
> > I have a need to refresh data stored in Sybase with DB2 v5 data.   We
can
> > extract the data into a flat file and then FTP & load into Sybase, but
> were
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#GOPIy#r$GA.303@cpmsnbbsa04>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04> <8e79b5$gam$1@goblin.tdh.state.tx.us>`

```
It is, these products are quite definitely for sale.


"Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote in message
news:8e79b5$gam$1@goblin.tdh.state.tx.us...
> Thanks Chris, I'll check them out.  Of course if a product purchase is
> necessary, I may be out of luck.
…[3 more quoted lines elided]…
> > I thought Sybase offered a product capable of just what you are asking
for
> .
> > . .
…[10 more quoted lines elided]…
> > Have a departmental, workgroup, or pilot application that requires
access
> to
> > IBM DB2 data?
> > Sybase ClearConnect provides two-tier connectivity from any Windows 3.1,
> > Windows 95 or Windows NT platform (16- or 32-bit) directly to any IBM
DB2
> > data source. With ClearConnect, applications such as those built with
> > Powerbuilder, Microsoft Access, Visual Basic, or other ODBC-compliant
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

_(reply depth: 4)_

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ecmh8$7r7$1@goblin.tdh.state.tx.us>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04> <8e79b5$gam$1@goblin.tdh.state.tx.us> <#GOPIy#r$GA.303@cpmsnbbsa04>`

```
If I understood correctly, it sounds like these can only be used from the pc
side.  I need to do this from the mainframe to  manipulate the data and then
place on a nightly job schedule.

"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
news:#GOPIy#r$GA.303@cpmsnbbsa04...
> It is, these products are quite definitely for sale.
>
…[26 more quoted lines elided]…
> > > Sybase ClearConnect provides two-tier connectivity from any Windows
3.1,
> > > Windows 95 or Windows NT platform (16- or 32-bit) directly to any IBM
> DB2
…[17 more quoted lines elided]…
> > > > I have a need to refresh data stored in Sybase with DB2 v5 data.
We
> > can
> > > > extract the data into a flat file and then FTP & load into Sybase,
but
> > > were
> > > > hoping to have a more direct method.
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

_(reply depth: 5)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uPu7G9Xs$GA.237@cpmsnbbsa03>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04> <8e79b5$gam$1@goblin.tdh.state.tx.us> <#GOPIy#r$GA.303@cpmsnbbsa04> <8ecmh8$7r7$1@goblin.tdh.state.tx.us>`

```
Sorry, I didn't go far enough up the product ladder.

Sybases Open Server Connect is the product you need (in theory, anyway)

Here are it's claims to functionality (note the parts about MVS):


#####################################################
Sybase Open ServerConnect
A Sybase EnterpriseConnect Product

Organizations need to access data from a wide range of heterogeneous systems
to formulate strategic decisions. With Sybase's Open ServerConnect� for CICS
and Open ServerConnect for IMS and MVS, users running their favorite
LAN-based applications on desktops get high-performance read/write access to
data and on-line production applications that reside on CICS, IMS, and MVS
systems. At the same time, these products allow mainframe managers to
maintain control of data integrity and security through existing mainframe
security systems.
Open ServerConnect for CICS and Open ServerConnect for IMS and MVS allow
your mainframe to act as both an application server and a data server in a
distributed environment. These application programming interfaces (APIs)
allow CICS, IMS, and MVS data and application programs to appear as Sybase�
data to a calling program --typically an Open Client� application. These
APIs let you deliver critical CICS, IMS, and MVS data and services to
requesting clients through a single Sybase infrastructure.


DirectConnect for MVS also acts as an OmniSQL Access Module� for enterprise
location transparency with OmniConnect. This allows you to integrate your
mainframe data seamlessly with other LAN-based systems such as joining
Oracle and Adaptive Server data.
###################################

Unfortunately it looks like you need an array of these products to get what
you want.

:(












"Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote in message
news:8ecmh8$7r7$1@goblin.tdh.state.tx.us...
> If I understood correctly, it sounds like these can only be used from the
pc
> side.  I need to do this from the mainframe to  manipulate the data and
then
> place on a nightly job schedule.
>
…[12 more quoted lines elided]…
> > > > I thought Sybase offered a product capable of just what you are
asking
> > for
> > > .
…[17 more quoted lines elided]…
> > > > Windows 95 or Windows NT platform (16- or 32-bit) directly to any
IBM
> > DB2
> > > > data source. With ClearConnect, applications such as those built
with
> > > > Powerbuilder, Microsoft Access, Visual Basic, or other
ODBC-compliant
> > > tools
> > > > can access and update DB2 data directly, without a middle-tier
access
> > > > server.
> > > >
> > > >
> > > > If your Sybase isn't on a PC, try reading up on DirectConnect or
even
> > > > OmniConnect (both also from Sybase).
> > > >
> > > > I haven't used any of them, so I can't vouch for their
effectiveness.
> > > This
> > > > post is just FYI.
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** prinzeck@my-deja.com
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e9lg2$37t$1@nnrp1.deja.com>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04> <8e79b5$gam$1@goblin.tdh.state.tx.us>`

```
In article <8e79b5$gam$1@goblin.tdh.state.tx.us>,
  "Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote:
> ... if a product purchase is necessary, I may be out of luck.
>

Mayby You can use FTP-DB2-Connect like this job:

 //* =================================================== *
 //STEP0010 EXEC PGM=IDCAMS
 //SYSPRINT DD  SYSOUT=*
 //SYSIN    DD  *
      DELETE MyTsoUser.SQL.OUTDAR          PURGE
      IF MAXCC = 8 THEN SET MAXCC = 0
 /*
 //* =================================================== *

 //* ==========================================
 //FTPSTEP EXEC PGM=FTP,
 //            PARM='00.0.0.0    (EXIT'
 //STEPLIB  DD  DISP=SHR,DSN=DB2T.DB201.TARG.SDSNLOAD   DSNALI/DSNHLI2..
 //*
 //* MYTSOUSER.SQL.IN
 //*   contains
 //*
 //*     SELECT *
 //*       FROM      Owner.DB2TABLE
 //* ----------------------------------------------
 //*
 //*       FTP-Subcommands:
 //INPUT    DD *
     MyUseerAt00.0.0.0
     MyPasswordAt00.0.0.0
     DIR
     LOCSITE FILETYPE=SQL
     LOCSITE DB2=DB2T
     LOCSITE SQLCOL=NAMES
     LOCSITE SPREAD
     PUT    'MYTSOUSER.SQL.IN'   SQLOUTDAR.TXT
     DIR
     LOCSITE FILETYPE=SEQ
     LOCSITE RECFM=VB
     LOCSITE BLKSIZE=0
     LOCSITE LRECL=32752
     GET     SQLOUTDAR.TXT    SQL.OUTDAR
     DELETE  SQLOUTDAR.TXT
     DIR
     CLOSE
     QUIT
 //*
 //SYSPRINT DD SYSOUT=*
 //OUTPUT   DD SYSOUT=*
 //SYSABEND DD SYSOUT=*
 //*
 //*
 //* ==============
 //


Hope it helps!

Eckhard


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

_(reply depth: 4)_

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ecqj2$c7t$1@goblin.tdh.state.tx.us>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <e6ndsfyr$GA.295@cpmsnbbsa04> <8e79b5$gam$1@goblin.tdh.state.tx.us> <8e9lg2$37t$1@nnrp1.deja.com>`

```
This looks interesting.

Since I need to join 2 tables and manipulate the data from DB2, I will need
to have a cobol pgm.  Can I output the results in a flat file rather then a
"spreadsheet" format?  Or can the "spreadsheet" format be created with my
pgm output?

Do you know how the data in SQL.OUTDAR is being loaded into a Sybase table?
Or is this a separate step on the server side?

<prinzeck@my-deja.com> wrote in message news:8e9lg2$37t$1@nnrp1.deja.com...
> In article <8e79b5$gam$1@goblin.tdh.state.tx.us>,
>   "Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote:
…[17 more quoted lines elided]…
>  file://STEPLIB  DD  DISP=SHR,DSN=DB2T.DB201.TARG.SDSNLOAD
DSNALI/DSNHLI2..
>  file://*
>  file://* MYTSOUSER.SQL.IN
…[42 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "scoobie" <scoobie_net@excite.com>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3907fe90.0@nnrp1.news.uk.psi.net>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us>`

```
you may want to contact liant software. they do a product called relational
databridge and/ or relativity......
www.liant.com
i think that is what you are looking for..........
scoobie.

Vic Hariton <vic.hariton@cpa.state.tx.us> wrote in message
news:8e4t65$iam$1@goblin.tdh.state.tx.us...
> I have a need to refresh data stored in Sybase with DB2 v5 data.   We can
> extract the data into a flat file and then FTP & load into Sybase, but
were
> hoping to have a more direct method.
>
>
>
```

##### ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ecqv1$cos$1@goblin.tdh.state.tx.us>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <3907fe90.0@nnrp1.news.uk.psi.net>`

```
Looks like a cool product, but state budget process would not approve a
purchase.  Too bad, they're in my home town...

Thanks.
"scoobie" <scoobie_net@excite.com> wrote in message
news:3907fe90.0@nnrp1.news.uk.psi.net...
> you may want to contact liant software. they do a product called
relational
> databridge and/ or relativity......
> www.liant.com
…[5 more quoted lines elided]…
> > I have a need to refresh data stored in Sybase with DB2 v5 data.   We
can
> > extract the data into a flat file and then FTP & load into Sybase, but
> were
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** prinzeck@my-deja.com
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eri23$f8m$1@nnrp1.deja.com>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us> <3907fe90.0@nnrp1.news.uk.psi.net> <8ecqv1$cos$1@goblin.tdh.state.tx.us>`

```

>..can the "spreadsheet" format
Yes, Your Program can produce a flat file in spreadsheet-Format: Its
just fields in display-format, with tabs delimiting each field.
I dont know anything about Sybase - sorry!

Output-example in hex:

DSTA.         DARS. AGDAR.
44CEEC0444444444CCDE04CCCCD0
0042315000000000419250174195
 ---------------------------
    10.    129500.00.   862.
4444FF04444FFFFFF4FF0444FFF0
00001050000129500B0050008625
 ---------------------------
    10.    362000.00.   862.
4444FF04444FFFFFF4FF0444FFF0
00001050000362000B0050008625


- EBCDIC Code Table            (HT- horizontal tabs)
-
Dec.  Hex  Binary    Mnemonic  EBCDIC      ASCII
----------------------------------------------------
 5    05  0000 0101    BALR    HT          ENQ
...
 9    09  0000 1001    ISK     SPS         HT
-----------------------------------------------------


>how the data in SQL.OUTDAR is being loaded into a Sybase table?
>Or is this a separate  step on the server side?

Yes, a separate step - mayby You can invoke a little batch-program
(Sybase loading utility) by
a separate step, a remote-shell call:

//* ----------------------------------------------------------------- *
//*
//STEP0070 EXEC PROC=ISPFBAT
//*TITELS......TSOBAT RemoteSHell to execute a Bat-File
//ISPFBAT.SYSTSIN DD *
    RSH   000.000.000.000     MyBatFile  [BatParm ...]
/*
//*------------------------------------------------------------------ *

 Hope it helps

Eckhard

Reference for Performing DB2 SQL Queries with FTP:

http://www.redbooks.ibm.com:80/cgi-bin/bookmgr/BOOKS/F1AA2001/CCONTENTS

OS/390 SecureWay Communications Server
IP User's Guide

Document Number GC31-8514-nn

Program Number 5647-A01

1.3.19        Performing DB2 SQL Queries with FTP
  1.3.19.1      SQL Data Types Supported by FTP
  1.3.19.2      Creating the Input Data Set
  1.3.19.3      Setting the Characteristics for the SQL Query
  1.3.19.4      Submitting the Query
  1.3.19.5      Examples of SQL Query Output



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eR3r18Xs$GA.233@cpmsnbbsa03>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us>`

```
Hmm, what version of MVS are you running?  What is your Sybase product
running on and what version is it?




"Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote in message
news:8e4t65$iam$1@goblin.tdh.state.tx.us...
> I have a need to refresh data stored in Sybase with DB2 v5 data.   We can
> extract the data into a flat file and then FTP & load into Sybase, but
were
> hoping to have a more direct method.
>
>
>
```

#### ↳ Re: Can COBOL MVS be used to access Sybase & DB2?

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8emm0n$nn0$1@goblin.tdh.state.tx.us>`
- **References:** `<8e4t65$iam$1@goblin.tdh.state.tx.us>`

```
I want to thank everyone for their suggestions.  Due to the ugly time &
budget constraint reality,  I will need to focus on the old fashion "flat
file" & "FTP" approach for now.  I was recently informed that the product we
are running on Sybase has an upgrade option for running from DB2.  So it
looks like the old approach will get me past the deadline and changing my
code later should be a snap.  Of course it may be awhile before the DB2
option is available to us.

Thanks again, Vic


"Vic Hariton" <vic.hariton@cpa.state.tx.us> wrote in message
news:8e4t65$iam$1@goblin.tdh.state.tx.us...
> I have a need to refresh data stored in Sybase with DB2 v5 data.   We can
> extract the data into a flat file and then FTP & load into Sybase, but
were
> hoping to have a more direct method.
>
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
