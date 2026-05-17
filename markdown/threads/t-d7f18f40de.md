[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_16 messages · 7 participants · 2018-05 → 2018-10_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-05-06T02:39:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com>`

```
GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW
GCC) is available for download with either Oracle Berkeley Database or
VBISAM 2.0.1 for Indexed Sequential file or without any Indexed
Sequential file support.

GnuCOBOL 3.0 is the first release that includes COBOL Report Writer.

http://www.arnoldtrembley.com/GnuCOBOL-3.0-MinGW-Build-Guide-draft.pdf

http://www.arnoldtrembley.com/GnuCOBOL-3.0-MinGW-Build-Guide-draft.odt

http://www.arnoldtrembley.com/GC30RC1-BDB-rename-7z-to-exe.7z

http://www.arnoldtrembley.com/GC30RC1-VBI-rename-7z-to-exe.7z

http://www.arnoldtrembley.com/GC30RC1-NODB-rename-7z-to-exe.7z

I've done some simple testing with the BDB and NODB versions to verify
the compiler runs on Windows XP. But I normally build on Windows 7 and
run on Windows 10.

Kind regards,

http://www.arnoldtrembley.com/GnuCOBOL.htm

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

#### ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-05-06T10:43:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p2@usenetarchives.gap>`
- **In-Reply-To:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com>`

```
On 05/06/2018 02:39 AM, Arnold Trembley wrote:
› GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW 
› GCC) is available for download with either Oracle Berkeley Database or 
…[20 more quoted lines elided]…
› 

The Report Writer support seems interesting although I am not
sure how many people actually used it. Generating reports
without it was not at all difficult.

As for ISAM support, just how important is it in this day and age
with the ease of database support especially things like SQLite?

bill
```

##### ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-05-06T23:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p2@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap>`

```
On 5/6/2018 9:43 AM, Bill Gunshannon wrote:
› On 05/06/2018 02:39 AM, Arnold Trembley wrote:
›› GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW 
…[31 more quoted lines elided]…
› 

I've never used COBOL report writer, and IBM seems to have never
included it in their mainframe COBOL compilers:

https://www.ibm.com/support/knowledgecenter/en/SS6SG3_4.2.0/com.ibm.entcobol.doc_4.2/MG/igymapxc023.htm

But there is some demand for Report Writer in GnuCOBOL. I believe there
are some users with software developed for other COBOL compilers
(AccuCOBOL? Microfocus?) who find the lack of COBOL report writer is a
barrier to converting to a free and open-source COBOL solution.

Pete Dashwood and I would both agree that modern database software
offers more features and scalability than native COBOL ISAM. But if
you're trying to move legacy COBOL applications to less expensive
alternatives, it would save time if your COBOL ISAM applications can
simply be recompiled.

While SQLite is a very interesting product, I've read that it has some
limitations compared to fully relational database software like Oracle
or DB2.

https://en.wikipedia.org/wiki/SQLite

And there is a GnuCOBOL interface for SQLite:

https://sourceforge.net/p/open-cobol/contrib/HEAD/tree/trunk/tools/CobolSQLite3/


I believe the long-term goal of the GnuCOBOL developers is to eventually
include all ISO standard COBOL object-oriented features.

Kind regards,


http://www.arnoldtrembley.com/

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2018-05-07T02:51:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p3@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap>`

```
On Sun, 6 May 2018 22:05:48 -0500, Arnold Trembley
wrote:

› On 5/6/2018 9:43 AM, Bill Gunshannon wrote:
›› On 05/06/2018 02:39 AM, Arnold Trembley wrote:
…[37 more quoted lines elided]…
› https://www.ibm.com/support/knowledgecenter/en/SS6SG3_4.2.0/com.ibm.entcobol.doc_4.2/MG/igymapxc023.htm


It was definately implemented in some of IBM's Cobol74 compilers, both
for VSE and MVS (DOS and OS at the time).

Check out page 251 of:

https://ia801902.us.archive.org/2/items/bitsavers_ibm370OSVSCOBOLforOSVSRel2.4Aug83_25369822/GC26-3857-3_IBM_VS_COBOL_for_OS_VS_Rel_2.4_Aug83.pdf

It was dropped in the mid/late eighties, IIRC.
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-05-07T07:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p4@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap> <gap-d7f18f40de-p4@usenetarchives.gap>`

```
On 05/07/2018 02:51 AM, Robert Wessel wrote:
› On Sun, 6 May 2018 22:05:48 -0500, Arnold Trembley
›  wrote:
…[51 more quoted lines elided]…
› 

I can easily guess why. :-)

bill
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-05-07T07:47:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p3@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap>`

```
On 05/06/2018 11:05 PM, Arnold Trembley wrote:
› On 5/6/2018 9:43 AM, Bill Gunshannon wrote:
›› On 05/06/2018 02:39 AM, Arnold Trembley wrote:
…[43 more quoted lines elided]…
› barrier to converting to a free and open-source COBOL solution.

Fair enough. Anything that makes the move to a cheaper platform
(and possibly a better performing platform) doable is a definite
plus.

› 
› Pete Dashwood and I would both agree that modern database software 
…[3 more quoted lines elided]…
› simply be recompiled.

That's true, but one of the constant complaints about COBOL is
its antiquity. I would hope that people considering moving would
also be considering modernization. And I don't mean modernization
as most people do, that is conversion to Java. :-)

›
› While SQLite is a very interesting product, I've read that it has some
› limitations compared to fully relational database software like Oracle
› or DB2.

Yes, but the comparison was to ISAM. I really don't see SQLite
as even comparable to things like MySQL or PostGres. I would think
more along the lines of RMS from the PDP-11 or VMS systems. A
complex data handling system using files.

›
› https://en.wikipedia.org/wiki/SQLite
›
› And there is a GnuCOBOL interface for SQLite:

I know there is, I have used it. Thus my reason for mentioning
it as a likely replacement for ISAM with a smaller effort
requirement than most true RDBMS's.

›
› https://sourceforge.net/p/open-cobol/contrib/HEAD/tree/trunk/tools/CobolSQLite3/
…[4 more quoted lines elided]…
› include all ISO standard COBOL object-oriented features.

And that I see as least needed. The majority of COBOL in use today
doesn't use them as they brought nothing but complexity to the table.
It has long been stated that when these features were added to the
standard the existing COBOL user base rejected them. Unless your
desire is to destroy COBOL I see no reason to waste the time and
effort. If you truly "need" objects then maybe COBOL isn't the
right language for your task.

bill
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-05-08T02:44:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p6@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap> <gap-d7f18f40de-p6@usenetarchives.gap>`

```
On 7/05/2018 11:47 PM, Bill Gunshannon wrote:
› On 05/06/2018 11:05 PM, Arnold Trembley wrote:
›› On 5/6/2018 9:43 AM, Bill Gunshannon wrote:
…[33 more quoted lines elided]…
› standard the existing COBOL user base rejected them. 
I never thought I'd see the day when you would acknowledge that, Bill,
but as you have, "Well Done!"

› Unless your
› desire is to destroy COBOL I see no reason to waste the time and
› effort.
And this attitude was not just held by you alone. The result is what we
see today: COBOL as around 40th most popular programming language in the
World.

Imagine if EVERYBODY had climbed on board the OO COBOL wagon... A new
COBOL responding to a new (event activated) paradigm.

I believe there would still have been "new" languages (I'm teaching
myself "Rust" at the moment and it really makes me smile...) but it
would have been much harder to dislodge COBOL as a top 5 contender.


If you truly "need" objects then maybe COBOL isn't the
› right language for your task.
What?!! I can't believe what I'm hearing... :-)

Perhaps we are all getting old... and wiser.

Pete.--
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-05-08T08:06:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p7@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap> <gap-d7f18f40de-p6@usenetarchives.gap> <gap-d7f18f40de-p7@usenetarchives.gap>`

```
On 05/08/2018 02:44 AM, pete dashwood wrote:
› On 7/05/2018 11:47 PM, Bill Gunshannon wrote:
›› On 05/06/2018 11:05 PM, Arnold Trembley wrote:
…[36 more quoted lines elided]…
› but as you have, "Well Done!"

Huh? This has always been my position. I have been doing in
this business since long before OO and have never been a fan.
And of all the major COBOL users I know, none of them have
ever been fans either. To mne it has always been: "The
Emperor isn't wearing any clothes at all!!"


› 
›› Unless your
…[7 more quoted lines elided]…
› COBOL responding to a new (event activated) paradigm.

We would have COBOL programs with needless complexity that didn't
do the job they were designed to do any better.

›
› I believe there would still have been "new" languages (I'm teaching
› myself "Rust" at the moment and it really makes me smile...) but it
› would have been much harder to dislodge COBOL as a top 5 contender.

At lest in this country, COBOL is not being dislodged. The smaller
numbers are not due to any decrease in COBOL lines of code but more
due to all the meaningless crap (like Candy Crush Saga :-) being
written in other languages requiring millions of lines of code to
do what a hundred lines of COBOL would have done.


›
›
›   If you truly "need" objects then maybe COBOL isn't the
›› right language for your task.
› What?!! I can't believe what I'm hearing... :-)

Again, nothing new here. It has always been my stand that the
first step in any development system is to pick the language
best suited to the job. And, like it or not, there are still
a lot of tasks where COBOL is that language.

›
› Perhaps we are all getting old... and wiser.

I know I am.

bill
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_(reply depth: 4)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2018-10-13T20:39:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p6@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap> <gap-d7f18f40de-p6@usenetarchives.gap>`

```
I never saw the need for Object Orientated code in the environment I
was working in - IBM 360/370/390 on MVS in batch and CICS. This was
because the needs OO was designed for were already addressed by other
mechanisms and the infrastructure was not available at the time to
make it worth while to change. It also would have required a major
management commitment. This was probably also true of the Unisys
environments and any other classic mainframes that survived. OO
probably is better once the environment is there and in one sense
probably was needed more by C/C++ than it was for COBOL. On the
UNIX/LINUX/WINDOWS systems when OO penetrated it probably was a
different story for COBOL. Also there were probably no conversion
tools in the early days of OO COBOL to help get systems from old
paradigm to OO so a massive effort would have been needed even to
ready a system to take advantage of OO.

Another major difference in environments is that the IBM Mainframe and
probably the other mainframe environments are more record oriented
than string and array oriented and natively support indexed files (the
z series COBOL support is a subset of the total VSAM capabilities).
Assembler, PL1, IDCAMS, SORT and proprietary languages such as DYL280
(now Vision something or other) and Easytrieve all support VSAM - the
IBM sequential, indexed and relative record access method support.
COBOL on the UNIX/Windows platform has to interface with a package and
proprietary indexed file system to have the same capability. In this
environment going directly to using the data base used by all other
packages and programs running on the system makes sense. Of course
that assumes that the business / government department / academic
institution was smart enough to standardize on one DBMS be it Oracle,
DB2, whatever the Microsoft SQL database manager is or the Linux DBMS.

COBOL at best was mediocre for report writing even with the REPORT
WRITER. DYL280 (now Vision something or another), Easytrieve and
other packages were and are far superior. Putting Screen handling in
COBOL may also have been a waste of time.

While waterfall probably was the least bad method of setting up the
early systems, it carried on longer than it should have because whole
bureaucracies had grown up around it. It was not the COBOL
programmers who were rigid so much as the management. Then management
has become interested in packages so COBOL is the backwater in many
organizations. Now the trend is to put things in the cloud. The
common thread in all of these environments is that there is probably
not current documentation of what these various systems as customized
for the organization do and how. If we thought COBOL programs or
assembler could be inscrutable, where does that put systems that are
control table (or Windows registry) driven with mediocre front ends
for maintaining those tables. How many of the organizations test
changes to these tables before putting them in production? How well
are these tables which control some basic processing documented?

Clark Morris
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-13T22:09:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p9@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap> <gap-d7f18f40de-p6@usenetarchives.gap> <gap-d7f18f40de-p9@usenetarchives.gap>`

```
On 14/10/2018 1:39 PM, Clark F Morris wrote:
› I never saw the need for Object Orientated code in the environment I
› was working in - IBM 360/370/390 on MVS in batch and CICS.  This was
…[4 more quoted lines elided]…
› environments and any other classic mainframes that survived.

This is very fair comment, Clark. Sites who had no intention of moving
to a Networked environment had no incentive to learn about OO,
particularly because, in a centralized mainframe environment, doing
mostly batch processing, everything works pretty well and there is
little need to rock the boat.

You may think that a mainframe running CICS is a lot like a Network with
multiple client/servers, or at least is doing the same job. But such is
not the case... (CICS is just a parasite and isn't even in the same
league as mainframe TP monitors like TaskMaster or Shadow or even
IMS/DC... so the remainder of this post excludes CICS.)


OO
› probably is better once the environment is there and in one sense
› probably was needed more by C/C++ than it was for COBOL.

With the benefit of many years hindsight, I can agree that OO COBOL was
not essential for mainframe COBOL processing. Probably the main reason
it was important to ME was because I moved off mainframes (but not COBOL
at that point) and the "environment" as you say, was different.

As I grew into the environment and OO it just made sense to discard OO
COBOL and use a language like C# which was designed for that.

I have given a lot of thought to why I consider OO so important (at
least in a Networked environment) and my conclusions are explained at:
https://primacomputing.co.nz/PRIMAMetro/objectsAndLayers.aspx


On the
› UNIX/LINUX/WINDOWS systems when OO penetrated it probably was a
› different story for COBOL.  Also there were probably no conversion
› tools in the early days of OO COBOL to help get systems from old
› paradigm to OO so a massive effort would have been needed even to
› ready a system to take advantage of OO.

Absolutely correct! Looking at the tools now available it is a much
different picture and I have spent the last 15 years working on such
tools. Today, we can move COBOL '85 into OO COBOL with a mouse click
and, during the same process we can design, build, and load an optimized
relational database to replace the indexed files, generate a modern OO
Data Access Layer to manage the new RDB, and refactor all of the COBOL
IO verbs in the legacy COBOL that address the indexed files, to be
invokes of the DAL objects... None of this was available when OO COBOL
was first released, and doing it manually would be a huge task. (I did 2
of these migrations manually and the experience prompted me to write the
tools we now have...)

› 
› Another major difference in environments is that the IBM Mainframe and
…[5 more quoted lines elided]…
› IBM sequential, indexed and relative record access method support.

I would call Easytrieve a utility rather than a Language, but it is
around 30 years since I last used it so it may have been enhanced :-).
› COBOL on the UNIX/Windows platform has to interface with a package and
› proprietary indexed file system to have the same capability.

That's true, but both Fujitsu and Micro Focus provide excellent ISAM
support with their COBOL compilers.


In this
› environment going directly to using the data base used by all other
› packages and programs running on the system makes sense.   Of course
› that assumes that the business / government department / academic
› institution was smart enough to standardize on one DBMS be it Oracle,
› DB2, whatever the Microsoft SQL database manager is or the Linux DBMS.

The secret here is separation and layers. (See the web pages referenced
above).

There is really no problem running 2 or 3 different RDBMS as far as the
applications are concerned, PROVIDED you don't go and plug Embedded SQL
into the application code. Applications see an interface and all of the
data manipulation is done by the objects in the DAL layer. (THESE
objects can have SQL in them, although nowadays, we generate LINQ
because it is many times more efficient and the source language of these
objects doesn't matter because they are never maintained.(They contain
code to do every possible action against an RDB, and they are generated
with a mouse click...)

See: https://primacomputing.co.nz/PRIMAMetro/RDBandSQL.aspx

... for my thoughts about this.

› 
› COBOL at best was mediocre for report writing even with the REPORT
› WRITER.  DYL280 (now Vision something or another), Easytrieve and
› other packages were and are far superior. Putting Screen handling in
› COBOL may also have been a waste of time.
 
› I remember when there was no other option (not even CICS... :-))
 
› 
› While waterfall probably was the least bad method of setting up the
› early systems, it carried on longer than it should have because whole
› bureaucracies had grown up around it. 

Amen to that! (https://dzone.com/articles/cretaceous-cobol-can-spawn)



It was not the COBOL
› programmers who were rigid so much as the management.  Then management
› has become interested in packages so COBOL is the backwater in many
…[3 more quoted lines elided]…
› for the organization do and how.

That's certainly true, but it is no longer the powerful argument it once
was. Programmers today have much better tools and it is quite possible
to analyze undocumented code and determine what it does.



If we thought COBOL programs or
› assembler could be inscrutable, where does that put systems that are
› control table (or Windows registry) driven with mediocre front ends
…[4 more quoted lines elided]…
› Clark Morris

An interesting post, Clark.

Thanks,

Pete

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2018-05-07T19:26:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p3@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap>`

```
Hello Arnold!

Monday May 07 2018 04:05, Arnold Trembley wrote to All:

>> The Report Writer support seems interesting although I am not
>> sure how many people actually used it.Â  Generating reports
…[4 more quoted lines elided]…
>>

> I've never used COBOL report writer, and IBM seems to have never
> included it in their mainframe COBOL compilers:

> https://www.ibm.com/support/knowledgecenter/en/SS6SG3_4.2.0/com.ibm.en
> tcobol.doc_4.2/MG/igymapxc023.htm

> But there is some demand for Report Writer in GnuCOBOL. I believe
> there are some users with software developed for other COBOL compilers
> (AccuCOBOL? Microfocus?) who find the lack of COBOL report writer is
> a barrier to converting to a free and open-source COBOL solution.


The RWRC is available in the current releases of v3.0 (rc1) and has been
for some time - OK, at least since late last year.

Yes I do use it sometimes for more simple reporting but that may well be me
as I have not used it much.

This mostly because there are few compilers with it as standard as against
an add on and then mostly third party products (IBM etc).

Now for SQLite, I did take a look at it but there seems to be no DB design
tools such as available with MySQL, MariaDB, Oracle, DB2 and possibly
Postgres. That was a primary reason for ignoring it but at the end of the
day a reusable RDBMS is some what more important for users who may well
want to use it for other applications within a business.

Cobol ISAM (etc) files are still very much used providing the multi-user
element is limited as it has serious limitations - at least in my lesting
a few years back. --- All this using GnuCOBOL as m/f is a different kettle
of fish.



Vince
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-05-08T02:28:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p3@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap> <gap-d7f18f40de-p3@usenetarchives.gap>`

```
On 7/05/2018 3:05 PM, Arnold Trembley wrote:
› On 5/6/2018 9:43 AM, Bill Gunshannon wrote:
›› On 05/06/2018 02:39 AM, Arnold Trembley wrote:
…[49 more quoted lines elided]…
› simply be recompiled.

Funny you should say that... :-)

I'm currently helping a client move from PowerCOBOL onto .Net. Their
long term aim is to replace their ISAM with RDB and we COULD have done
that first, but, for PowerCOBOL it involves a lot of manual activity
with updating existing scriptlets.

We now have the capability to write a tool that could automate this (we
didn't have the knowledge of how to update existing PowerCOBOL projects
(which are based on MS Compound files and very tricky to manage) until a
few months ago), but if we move them OFF PowerCOBOL first, it is really
easy to do a fully automated migration to RDB.

So they will move to .Net with ISAM still in place, THEN we will run
tools to convert that.

Although I do prefer RDB to using ISAM (there is a comparison which led
me to this conclusion here:
https://primacomputing.co.nz/PRIMAMetro/RDBandSQL2.aspx), I would stress
that "simply recompiling" is NOT a course of action I would normally
endorse.

When COBOL is moved to the Network, the IO in it SHOULD be refactored to
a separate Data Access Layer. And especially so if an ISAM to RDB
conversion is being done at the same time. It isn't hard to do this
manually, but it IS time consuming and error prone, so we have tools
that do it fully automatically and correctly.

In the example given above we can "tolerate" the Code going to .Net with
embedded ISAM in it, because the PowerCOBOL scriptlets get stripped out
into OO COBOL Classes (Win Forms "code-behinds") along the way. The
final phase of the Migration Transforms all the ISAM references in the
code-behinds into invokes of the DAL layer, which, in turn, contains the
SQL (or LINQ, as an option) to manage the new optimized 3NF RDB.

There is NO embedded SQL in the Business Logic any more; all data
management is through the DAL layer via an interface.
›
› While SQLite is a very interesting product, I've read that it has some
› limitations compared to fully relational database software like Oracle
› or DB2.

The main claimed advantage for it was that it is FREE and it is easy to
deploy, as it is a smaller package than most of the main ones. Given
that SQL Server is free (Unless you plan to manage a server farm with
it...), there is little advantage in using SQL Lite.


› 
› https://en.wikipedia.org/wiki/SQLite
…[8 more quoted lines elided]…
› include all ISO standard COBOL object-oriented features.

"'Tis a consummation devoutly to be wished..." and I wish them every
success with it. I would be using GNU COBOL if it supported the
Component Object Model and OO COBOL.

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2018-05-07T02:19:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p2@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p2@usenetarchives.gap>`

```
On Sun, 6 May 2018 10:43:06 -0400, Bill Gunshannon
wrote:

› On 05/06/2018 02:39 AM, Arnold Trembley wrote:
›› GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW 
…[25 more quoted lines elided]…
› without it was not at all difficult.


Report writer worked well if the structure of your reports fell into
the model that report writer used. If not, using it was often far
more trouble than it was worth.

That being said, something like DYLAKOR was more flexible, and much
simpler to use (and usually requiring considerable less code as well).

The bigger problem was lack of familiarity. It was just not widely
used, and often that made it impractical to use in many places, if not
outright forbidden.

A certain level of bugginess in early IBM implementations didn't help
either.
```

#### ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2018-05-11T12:15:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p14@usenetarchives.gap>`
- **In-Reply-To:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com>`

```
domingo, 6 de Maio de 2018 às 07:39:46 UTC+1, Arnold Trembley escreveu:
› GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW 
› GCC) is available for download with either Oracle Berkeley Database or 
…[26 more quoted lines elided]…
› https://www.avast.com/antivirus




"Cobol Report Writer" in the xxi century does not look interesting and should be very little used. Embedding graphical interfaces (UI/GUI) and SQL access (more easily), seems to be much more interesting and necessary, otherwise GnuCobol does not have a great future. But working for free it´s not easy.
```

##### ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-05-11T13:39:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p14@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p14@usenetarchives.gap>`

```
On 05/11/2018 12:15 PM, JM wrote:
› domingo, 6 de Maio de 2018 às 07:39:46 UTC+1, Arnold Trembley escreveu:
›› GnuCOBOL 3.0 Release Candidate 1 for Windows (built using 32-bit MinGW
…[33 more quoted lines elided]…
› 

I have had quite a bit of success generating HTML reports for delivery
on the web instead of killing trees (ask me some day about one of the
systems I worked on 30 years ago that killed lots of trees needlessly!!)

I have also had success doing web front ends directly from COBOL. One
of these days I will make a suggestion to the developers about a way
I think it could be made even easier.

bill
```

###### ↳ ↳ ↳ Re: GnuCOBOL 3.0 Release Candidate 1 for Windows, with COBOL Report Writer

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2018-05-11T17:34:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7f18f40de-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d7f18f40de-p15@usenetarchives.gap>`
- **References:** `<s-KdnXTHNZm2PnPHnZ2dnUU7-cPNnZ2d@giganews.com> <gap-d7f18f40de-p14@usenetarchives.gap> <gap-d7f18f40de-p15@usenetarchives.gap>`

```
sexta-feira, 11 de Maio de 2018 às 18:39:44 UTC+1, Bill Gunshannon escreveu:
› On 05/11/2018 12:15 PM, JM wrote:
›› domingo, 6 de Maio de 2018 às 07:39:46 UTC+1, Arnold Trembley escreveu:
…[44 more quoted lines elided]…
› bill

If you could share your ideas / concepts with the GbuCobol community, it could be very interesting.
Regards,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
