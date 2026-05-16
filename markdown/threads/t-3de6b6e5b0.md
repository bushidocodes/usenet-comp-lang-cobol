[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol MVS vs IMS

_19 messages · 12 participants · 2002-11 → 2003-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol MVS vs IMS

- **From:** tjguerra@attbi.com (Tom G)
- **Date:** 2002-11-05T18:15:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dc3887b.0211051815.223625fc@posting.google.com>`

```
I have been writing Cobol/CICS on the IBM/MVS platform for about 15
years now. Unfortunately the downsize happened. I see many positions
in my area (Colorado)for IMS platform Cobol/CICS programmers. Can
anyone explain to me in 25 words or less what is the difference in the
platforms or point me in the area where I can learn the differences???

Any help is appreciated.
```

#### ↳ Re: Cobol MVS vs IMS

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-11-06T02:24:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2853b$95acf520$168bf243@chottel>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com>`

```
IMS is a database management system.  See the book "IMS for the Cobol
Programmer" vol 1 and 2 at http://www.murach.com/books/mainframe.htm

Tom G <tjguerra@attbi.com> wrote in article
<6dc3887b.0211051815.223625fc@posting.google.com>...
> I have been writing Cobol/CICS on the IBM/MVS platform for about 15
> years now. Unfortunately the downsize happened. I see many positions
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol MVS vs IMS

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-05T20:48:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aq9vuj$qo2$1@slb0.atl.mindspring.net>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel>`

```
I slightly disagree with Charles' summary.

 CICS (which the original poster knows) is ONLY a "transaction management
system".  It relies on various "file" systems (including VSAM, DB2 or even
IMS) for "data storage".

IMS includes two parts  - one is a hierarchical database system (which can
be accessed from batch, from CICS, *or* from an IMS transaction system).  In
addition, IMS provides its own  "transaction system"

    ***

From a COBOL programmer's point of view,  CICS uses
   EXEC CICS  (and/or EXEC DLI and/or EXEC SQL) statements to do both screen
and file I/O (Using "native" COBOL OPEN, READ, WRITE, CLOSE is a DEFINITE
"no-no")

IMS uses CALL "CBLTDLI" (or slight variations) to do screen I/O and IMS
database access.  It is allowable (depending on some technical situations)
to use OPEN, READ, WRITE, CLOSE, etc *and* EXEC SQL in an IMS program.

Both CICS and IMS use "native COBOL" syntax for all "business logic" -
everything except screen and "file" I/O.  You shouldn't need any
"re-training" for this part.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-06T04:14:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021105231431.16750.00000052@mb-bg.aol.com>`
- **References:** `<aq9vuj$qo2$1@slb0.atl.mindspring.net>`

```
>From: "William M. Klein" wmklein@nospam.ix.netcom.com 
>Date: 11/5/02 9:48 PM Eastern Standard Time

>
>IMS includes two parts  - one is a hierarchical database system (which can
…[20 more quoted lines elided]…
> wmklein <at> ix.netcom.com

The batch side of IMS is called IMS-DB while the transactional part is called
IMS-DC (you may see these terms in the job descriptions).

As Bill said to access the database you'll need to learn the syntax of the
calls but everything else is your everyday COBOL.

For the transaction side instead of BMS maps IMS used MID/MOD's and DIF/DOF's
which you'll have to learn as well.  MID (if memory serves it's been about 10
years since I've done IMS-DC) is Map Input Definition and MOD is Map Output
Definition while DIF is Data Input Definition and DOF is Data Output
Definition.  Unlike BMS maps where the data comes in exactly as found on the
map you can designate that the data from the map come into the program other
than in the order of the fields on the screen, and that the data be in another
order as well.

All in all it was interesting.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS - Modern IMS Terminology

_(reply depth: 4)_

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2002-11-07T10:39:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCAB375.CE54DD45@attglobal.net>`
- **References:** `<aq9vuj$qo2$1@slb0.atl.mindspring.net> <20021105231431.16750.00000052@mb-bg.aol.com>`

```
IMS/DB is now called IMS/DM (Database Manager).
IMS/DC is now called IMS/TM (Transaction Manager).

I think these terms have both been in use since at least IMS V5; V8 has just been
recently announced.

See
http://www-3.ibm.com/software/data/ims/
for more info, including complete manual sets you can download and learn from!

YukonMama wrote:

> >From: "William M. Klein" wmklein@nospam.ix.netcom.com
> >Date: 11/5/02 9:48 PM Eastern Standard Time
…[40 more quoted lines elided]…
> All in all it was interesting.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS - Modern IMS Terminology

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-10T07:52:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021110025218.20540.00000085@mb-cl.aol.com>`
- **References:** `<3DCAB375.CE54DD45@attglobal.net>`

```
>From: Colin Campbell cmcampb@attglobal.net 
>Date: 11/7/02 1:39 PM Eastern Standard Time

>IMS/DB is now called IMS/DM (Database Manager).
>IMS/DC is now called IMS/TM (Transaction Manager).
…[4 more quoted lines elided]…
>

Well I said it's been a long time and I see it certainly has :)
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-11-06T12:10:43+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2dqhsu0dqfv4tfckk4ha945p43b48ps5ah@4ax.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net>`

```
On Tue, 5 Nov 2002 20:48:48 -0600 "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

:>I slightly disagree with Charles' summary.

:> CICS (which the original poster knows) is ONLY a "transaction management
:>system".  It relies on various "file" systems (including VSAM, DB2 or even
:>IMS) for "data storage".

:>IMS includes two parts  - one is a hierarchical database system (which can
:>be accessed from batch, from CICS, *or* from an IMS transaction system).  In
:>addition, IMS provides its own  "transaction system"

:>    ***

:>From a COBOL programmer's point of view,  CICS uses
:>   EXEC CICS  (and/or EXEC DLI and/or EXEC SQL) statements to do both screen
:>and file I/O (Using "native" COBOL OPEN, READ, WRITE, CLOSE is a DEFINITE
:>"no-no")

:>IMS uses CALL "CBLTDLI" (or slight variations) to do screen I/O and IMS
:>database access.

IMS/DC does not do screen I/O. The Message Processing Program (MPP) is invoked
with all the data needed to perform the instruction (such invocation may have
been a while before) and then returns results (which, again, may not be
displayed for a while).

:>                  It is allowable (depending on some technical situations)
:>to use OPEN, READ, WRITE, CLOSE, etc *and* EXEC SQL in an IMS program.

As allowed in CICS - though you would probably get your fingers broken for
doing it (in an MPP).

Batch programs would be allowed to do such functions.

:>Both CICS and IMS use "native COBOL" syntax for all "business logic" -
:>everything except screen and "file" I/O.  You shouldn't need any
:>"re-training" for this part.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

- **From:** tjguerra@attbi.com (Tom G)
- **Date:** 2002-11-06T07:46:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dc3887b.0211060746.7ca60fe1@posting.google.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<aq9vuj$qo2$1@slb0.atl.mindspring.net>...
> I slightly disagree with Charles' summary.
> 
…[40 more quoted lines elided]…
> > >


Thanks Bill,

I will assume then that I will need to learn a new screen mapping
system as IMS doesn't use BMS it uses something called PPS.

No big deal though.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 4)_

- **From:** tjguerra@attbi.com (Tom G)
- **Date:** 2002-11-17T12:55:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dc3887b.0211171255.37695f42@posting.google.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com>`

```
tjguerra@attbi.com (Tom G) wrote in message news:<6dc3887b.0211060746.7ca60fe1@posting.google.com>...
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<aq9vuj$qo2$1@slb0.atl.mindspring.net>...
> > I slightly disagree with Charles' summary.
…[43 more quoted lines elided]…
> 
Call me confused... I just received his message from Germany.

Both are Platforms on IBM Mainfraimes  
Both, IMS  and CICS  als Transaction Monitor  

For  Learning  Application Programming as Cobol Programmer 
there ist  some literature written by 

Steve Eckols    ISBN  0-911625-29-1     and 0-911625-30-5  

IMS  ise more simple than CICS   for application programmer 

I assumed IMS was a database management system not a Transaciton Monitor like CICS.

Where are all the knowlegeable IMS people???
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-11-17T23:51:33+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ie2gtu8vn2rm82s2ee3d3pt86voo9s6a7k@4ax.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com>`

```
On 17 Nov 2002 12:55:42 -0800 tjguerra@attbi.com (Tom G) wrote:

   [ snipped ]

:>Call me confused... I just received his message from Germany.

:>Both are Platforms on IBM Mainfraimes  
:>Both, IMS  and CICS  als Transaction Monitor  

:>For  Learning  Application Programming as Cobol Programmer 
:>there ist  some literature written by 

:>Steve Eckols    ISBN  0-911625-29-1     and 0-911625-30-5  

:>IMS  ise more simple than CICS   for application programmer 

:>I assumed IMS was a database management system not a Transaciton Monitor like CICS.

IMS/DB - database
IMS/DC - transaction processor

:>Where are all the knowlegeable IMS people???

You got me.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-17T17:12:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ar97pa$f8q$1@slb4.atl.mindspring.net>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com> <ie2gtu8vn2rm82s2ee3d3pt86voo9s6a7k@4ax.com>`

```
Or more "current"

> IMS/DB - database
 See: "Application Programming: Database Manager"

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/DFSP30F3/CCONTENT
S


> IMS/DC - transaction processor
 See: "Application Programming: Transaction Manager"

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/DFSP20F3/CCONTENT
S
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-11-17T22:52:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C4VB9.688$Kw6.519697@newssrv26.news.prodigy.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com>`

```
"Tom G" <tjguerra@attbi.com> wrote in message
news:6dc3887b.0211171255.37695f42@posting.google.com...
> Where are all the knowlegeable IMS people???

Retired.

MCM
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-11-17T23:50:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c28e94$20bdaa40$0ccaf943@chottel>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com> <C4VB9.688$Kw6.519697@newssrv26.news.prodigy.com>`

```
Downsized.

Michael Mattias <michael.mattias@gte.net> wrote in article
<C4VB9.688$Kw6.519697@newssrv26.news.prodigy.com>...
> "Tom G" <tjguerra@attbi.com> wrote in message
> news:6dc3887b.0211171255.37695f42@posting.google.com...
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-18T01:37:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021117203727.08958.00000028@mb-cp.aol.com>`
- **References:** `<6dc3887b.0211171255.37695f42@posting.google.com>`

```
>From: tjguerra@attbi.com  (Tom G)
>Date: 11/17/02 3:55 PM Eastern Standard Time
>

>Where are all the knowlegeable IMS people???
>

Working on CICS/DB2 systems.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 5)_

- **From:** "Leahy, Don" <zzdlf@tdbank.ca>
- **Date:** 2002-11-18T08:51:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tf6C9.2697$kS3.279144@news20.bellglobal.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com>`

```
There are some brilliant IMS experts on the IMS-L list.

As others have pointed out, IMS has both a data management and transaction
management component.  <IMS bigot> IMS TM, while not as popular as CICS, is
actually a superior transaction manager.  </IMS bigot>.   :-)


"Tom G" <tjguerra@attbi.com> wrote in message
news:6dc3887b.0211171255.37695f42@posting.google.com...
> tjguerra@attbi.com (Tom G) wrote in message
news:<6dc3887b.0211060746.7ca60fe1@posting.google.com>...
> > "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:<aq9vuj$qo2$1@slb0.atl.mindspring.net>...
> > > I slightly disagree with Charles' summary.
> > >
> > >  CICS (which the original poster knows) is ONLY a "transaction
management
> > > system".  It relies on various "file" systems (including VSAM, DB2 or
even
> > > IMS) for "data storage".
> > >
> > > IMS includes two parts  - one is a hierarchical database system (which
can
> > > be accessed from batch, from CICS, *or* from an IMS transaction
system).  In
> > > addition, IMS provides its own  "transaction system"
> > >
…[3 more quoted lines elided]…
> > >    EXEC CICS  (and/or EXEC DLI and/or EXEC SQL) statements to do both
screen
> > > and file I/O (Using "native" COBOL OPEN, READ, WRITE, CLOSE is a
DEFINITE
> > > "no-no")
> > >
> > > IMS uses CALL "CBLTDLI" (or slight variations) to do screen I/O and
IMS
> > > database access.  It is allowable (depending on some technical
situations)
> > > to use OPEN, READ, WRITE, CLOSE, etc *and* EXEC SQL in an IMS program.
> > >
…[9 more quoted lines elided]…
> > > > IMS is a database management system.  See the book "IMS for the
Cobol
> > > > Programmer" vol 1 and 2 at http://www.murach.com/books/mainframe.htm
> > > >
> > > > Tom G <tjguerra@attbi.com> wrote in article
> > > > <6dc3887b.0211051815.223625fc@posting.google.com>...
> > > > > I have been writing Cobol/CICS on the IBM/MVS platform for about
15
> > > > > years now. Unfortunately the downsize happened. I see many
positions
> > > > > in my area (Colorado)for IMS platform Cobol/CICS programmers. Can
> > > > > anyone explain to me in 25 words or less what is the difference in
the
> > > > > platforms or point me in the area where I can learn the
differences???
> > > > >
> > > > > Any help is appreciated.
…[15 more quoted lines elided]…
> I assumed IMS was a database management system not a Transaciton Monitor
like CICS.
>
> Where are all the knowlegeable IMS people???
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 6)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-11-18T17:23:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DD92418.9020300@nycap.rr.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com> <tf6C9.2697$kS3.279144@news20.bellglobal.com>`

```
Someone wrote:  Where are all the knowlegeable IMS people???

Yes, retired, downsized, etc.  How true.  I had been doing 
DB2 & CICS for so long that I'd almost forgotten about IMS, 
but given my current work situation (or lack thereof), I'd 
do IMS again.  I'm not proud (except of my code).


Leahy, Don wrote:
> There are some brilliant IMS experts on the IMS-L list.
> 
…[3 more quoted lines elided]…
> 


As far as transaction managers go, anything beats CICS. 
MicroFocus COBOL's screen handling comes to mind, but I've 
also used XEDIT in an IBM/VM environment to handle 
transactions, not pretty, but fairly easy.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 5)_

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2002-12-23T04:35:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NtidnVzvF95Le5ujXTWcrg@comcast.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com>`

```
In article <6dc3887b.0211171255.37695f42@posting.google.com>, 
tjguerra@attbi.com wrote:

>Where are all the knowlegeable IMS people???

The Florida Department of Insurance uses it on their mainframe systems.
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-23T23:44:04
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e07a0e3_1@Usenet.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com> <NtidnVzvF95Le5ujXTWcrg@comcast.com>`

```
I spent 10 years working with IMS and know a thing or two about it. I don't
post  on it here because most people don't even say "thanks" and I no longer
have access to a mainframe to test any code I posted.

There are probably a lot of people here who are using IMS every day. Did it
occur to you that some of them may make a living out this and would be loth
to give it away free?

Having said that, there is a wealth of information here that is freely given
and the general tone of the NG is "helpful".

Maybe you should try posting a specific problem rather than asking for
general support on IMS?

Pete.

Ubiquitous <weberm@polaris.net> wrote in message
news:NtidnVzvF95Le5ujXTWcrg@comcast.com...
> In article <6dc3887b.0211171255.37695f42@posting.google.com>,
> tjguerra@attbi.com wrote:
…[4 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Cobol MVS vs IMS

_(reply depth: 7)_

- **From:** mnk <member21805@dbforums.com>
- **Date:** 2003-01-06T23:59:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2354462.1041897583@dbforums.com>`
- **References:** `<6dc3887b.0211051815.223625fc@posting.google.com> <01c2853b$95acf520$168bf243@chottel> <aq9vuj$qo2$1@slb0.atl.mindspring.net> <6dc3887b.0211060746.7ca60fe1@posting.google.com> <6dc3887b.0211171255.37695f42@posting.google.com> <NtidnVzvF95Le5ujXTWcrg@comcast.com> <3e07a0e3_1@Usenet.com>`

```

I just became member of this forum and happened to see this. Ims paid my
bills for most of my career and still is. If you still need more info, I
would not mind helping out..

mnk
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
