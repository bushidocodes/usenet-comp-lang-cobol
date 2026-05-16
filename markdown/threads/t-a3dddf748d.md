[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Compilers

_9 messages · 7 participants · 2000-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL Compilers

- **From:** "Mike Riley" <mriley@floristsmutual_nospam.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ekqs101qsn@enews3.newsguy.com>`

```
I don't know if this is the proper place to post this, so I apologize in
advance if I am "barking up the wrong tree".  My current work environment
consists of this configuration:

AlphaServer 4100, running an ORACLE database, release 7.3.3.6.0, under
OpenVMS v7.1.

Digital COBOL v2.5, with Pro*COBOL Release 1.8.3.0.0.

We are slowly moving off of our AlphaServer.  I have been tasked to look for
alternative, PC based compilers/pre-compilers that would offer us a way to
move off our mainframe.  Where should I start?  Anyone already migrated from
this type of configuration?
Problems encountered?  Costs?

Any help or information greatly appreciated.

TIA.

MJR
```

#### ↳ Re: COBOL Compilers

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390e0488.348883988@wingate>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com>`

```
On Mon, 1 May 2000 15:52:55 -0500, "Mike Riley"
<mriley@floristsmutual_nospam.com> wrote:

>AlphaServer 4100, running an ORACLE database, release 7.3.3.6.0, under
>OpenVMS v7.1.
…[7 more quoted lines elided]…
>Problems encountered?  Costs?

Hi, Mike,

People have been moving from various mainframes to PCs using COBOL for
over fifteen years.  It is eminently practical.  Even with platform
specific issues (screen handling  (our specialty), databases, file
systems - all of which are manageable) you will find it fairly easy to
move a mainframe application to the PC.   COBOL is as advanced on the
PC as anywhere.  In general, it's not too difficult to migrate.

We've been doing PC COBOL development since 1985, and have had some
experience with most of the compilers.  It happens that we are partial
to the CA-Realia Workbench product in our own shop.  

As a COBOL tool vendor, however, we work with all of them, and I can
tell you that we have customers who are happy with Fujitsu COBOL,
Micro Focus (Merant) NetExpress, IBM Visual Age COBOL, mbp COBOL, and
AcuCOBOL as well.  I'd probably rank them in the order I mentioned,
but I'd also guess that the preference on the ng is probably Fujitsu,
due to its competitive pricing.

We have links to most of them from the Links page on our web site.  

I'd probably say that the hardest part of moving an application to the
PC is handling the multi-user file issue.  If the compiler supports
locking in its file system, fine, but fifteen years ago when we did
our first multi-user system we couldn't use the COBOL file system and
switched to a third-party database manager:  Btrieve.  It was a good
solution, and one we still use on the application development side of
our consulting business.

Today, with SQL/ODBC support in all of the major players it's much
easier if that's the way you want to go.

My guess is, you'll find a migration a very satisfying endeavor.

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

##### ↳ ↳ Re: COBOL Compilers

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8el41m$ee2$1@news.igs.net>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com> <390e0488.348883988@wingate>`

```

Kevin Hansen wrote in message <390e0488.348883988@wingate>...
>On Mon, 1 May 2000 15:52:55 -0500, "Mike Riley"
><mriley@floristsmutual_nospam.com> wrote:
…[6 more quoted lines elided]…
>>We are slowly moving off of our AlphaServer.  I have been tasked to look
for
>>alternative, PC based compilers/pre-compilers that would offer us a way to
>>move off our mainframe.  Where should I start?  Anyone already migrated
from
>>this type of configuration?
>>Problems encountered?  Costs?
…[30 more quoted lines elided]…
>

I would agree with everything that Kevin has said, with the possible
exception of the above.  Both Fujitsu and MF handle file locking on the PC
quite well, and I see no reason you should have a problem there.  The
biggest problem that I have had is that PC user's expect windows "look and
feel" which is often inappropriate for the systems that are being designed.
What works well for thousands using a program for an hour a day is seldom
the best for someone that uses the same program for eight hours every day.
*All* my customers, for example, want programs that are mouse driven. Of the
line troops that actually use the programs, every single one of them hate
the mouse, as it forces them to use the screen.  They are use to a hex pad
being used while they talk on the phone and watch traffic out the window.
All that is cosmetic, though. Making things works is quite easy with today's
tools.
```

#### ↳ Re: COBOL Compilers

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390f0f1f.19886141@news.cox-internet.com>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com>`

```
The Oracle Pro*COBOL precompiler works with MicroFocus AND Fujitsu
COBOL's if you are moving to Windows NT or 2000.  Your bigger problem
will be converting your very powerful DCL to something else under NT.

Fujitsu also supports Oracle with ODBC, but my results using that have
been generally poor.  The pre-compiler works much better.


On Mon, 1 May 2000 15:52:55 -0500, "Mike Riley"
<mriley@floristsmutual_nospam.com> wrote:

>I don't know if this is the proper place to post this, so I apologize in
>advance if I am "barking up the wrong tree".  My current work environment
…[19 more quoted lines elided]…
>
```

#### ↳ Re: COBOL Compilers

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4irugs8u43uee6lr0eodcesv6fm953qotm@4ax.com>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com>`

```
"Mike Riley" <mriley@floristsmutual_nospam.com> wrote:

>I don't know if this is the proper place to post this, so I apologize in
>advance if I am "barking up the wrong tree".  My current work environment
>consists of this configuration:

>AlphaServer 4100, running an ORACLE database, release 7.3.3.6.0, under
>OpenVMS v7.1.

>Digital COBOL v2.5, with Pro*COBOL Release 1.8.3.0.0.

>We are slowly moving off of our AlphaServer.  I have been tasked to look for
>alternative, PC based compilers/pre-compilers that would offer us a way to
>move off our mainframe.  Where should I start?  Anyone already migrated from
>this type of configuration?
>Problems encountered?  Costs?

if you are going to a pc environment, you need to learn about alot of
things the mainframe has as standard:

RAID disk arrays
alot of security products
	file security
	database security
	network security
	disk wiping products
OLTP products
24/7 technical support on all purchases


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

##### ↳ ↳ Re: COBOL Compilers

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eq828$cu9$1@news.inet.tele.dk>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com> <4irugs8u43uee6lr0eodcesv6fm953qotm@4ax.com>`

```
I think you have a point, and I just thought about your statement about
security/support. In general I would say that it is default on a mainframe,
but default in PC environment is that it doesn't exist unless you buy it as
an add-on - good eh?

In Windows 24/7 is completely different from its normal meaning. (Only 7 out
of 24 crashes are recoverable. The rest can be considered as a built-in
diskwiping product - free-of-charge) :-).

Sorry, I couldn't resist it.

Ib
G Moore skrev i meddelelsen <4irugs8u43uee6lr0eodcesv6fm953qotm@4ax.com>...
>"Mike Riley" <mriley@floristsmutual_nospam.com> wrote:
>
…[9 more quoted lines elided]…
>>We are slowly moving off of our AlphaServer.  I have been tasked to look
for
>>alternative, PC based compilers/pre-compilers that would offer us a way to
>>move off our mainframe.  Where should I start?  Anyone already migrated
from
>>this type of configuration?
>>Problems encountered?  Costs?
…[14 more quoted lines elided]…
>reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: COBOL Compilers

- **From:** David Sanders <dsanders@legacyj.com>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3910A3AE.5DB01601@legacyj.com>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com>`

```
Why get stuck on another platform?

Visit www.legacyj.com.

David Sanders
LegacyJ, Corp.
info@legacyj.com
```

##### ↳ ↳ Re: COBOL Compilers

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RR6Q4.42201$k5.1206209@news1.frmt1.sfba.home.com>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com> <3910A3AE.5DB01601@legacyj.com>`

```
"David Sanders" <dsanders@legacyj.com> wrote:
> Why get stuck on another platform?

wow, compelling stuff. what do you mean?
```

###### ↳ ↳ ↳ Re: COBOL Compilers

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39132308.66527041@news.cox-internet.com>`
- **References:** `<8ekqs101qsn@enews3.newsguy.com> <3910A3AE.5DB01601@legacyj.com> <RR6Q4.42201$k5.1206209@news1.frmt1.sfba.home.com>`

```
On Thu, 04 May 2000 04:17:53 GMT, "Gazaloo" <gaz@home.com> wrote:

>"David Sanders" <dsanders@legacyj.com> wrote:
>> Why get stuck on another platform?
>
>wow, compelling stuff. what do you mean?
>

He means that there is a (Very GOOD I might add) COBOL compiler that
creates JAVA byte code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
