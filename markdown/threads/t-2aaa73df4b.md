[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Possibly stupid question for you IBM mainframers... :-)

_67 messages · 28 participants · 2004-07 → 2004-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Possibly stupid question for you IBM mainframers... :-)

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-12T12:18:39-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<vfs8ApHpvioW092yn@visi.com>`

```
Hi, guys...

I've been out of work for a while, and while I know COBOL well enough
on both the Unisys 2200 and A-series platforms (I've written code in
both of those environments now), most of the mainframe work I see out
there is in IBMland.

No, this isn't a surprise to me.  :-)

My question, though: How does a person like me go about learning more
about CICS, COBOL2, DB2, etc., on the IBM side...?

I already know how to operate in environments like TSO/ISPF (having
used various tools in that environment for over a decade at a former
workplace), and I have a couple of Doug Lowe's books on CICS "for the
COBOL programmer" which seem quite interesting at first glance, but
I've been too busy reading up on Javascript and other seemingly more
marketable things to spend too much time reading things IBMish.

So many books, so little time.  :-(

How does one learn about the IBM world nowadays?  Or is that something
which is no longer a realistic desire?

Am I crazy for even being interested?

Is there a better newsgroup to ask this?  Maybe I'll also fork this to
a.f.c (since I know a lot of former IBMers post there as well).
```

#### ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-07-12T17:49:04+00:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<ccuiuf$d6k$1@peabody.colorado.edu>`
- **References:** `<vfs8ApHpvioW092yn@visi.com>`

```

On 12-Jul-2004, rsteiner@visi.com (Richard Steiner) wrote:

> My question, though: How does a person like me go about learning more
> about CICS, COBOL2, DB2, etc., on the IBM side...?

CICS is pretty much unique, but I have been able to work over half of my career
on IBM mainframes without significant CICS work.

As for COBOL2 and DB2, the main trick is to convince personal that you know how
to do the work.   Switching from one relational database using SQL to another is
trivial.   The differences between ways of handling DB2 code within CoBOL
programs can be bigger than switching between Oracle and DB2.

I once didn't get a job because I didn't have COBOL 2 experience.   Well, I had
experience with COBOL on VAX and Univac that looked just like COBOL 2, and I had
experience on IBM with older versions of COBOL, so there was nothing I needed to
learn - but since they couldn't check off that I had experience with it, I
didn't get the job.

Funny thing is that lots of shops skipped right past COBOL 2 because it didn't
have everything needed for Y2K.    But it was standard COBOL.
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Joachim Pense <spam-collector@pense-online.de>
- **Date:** 2004-07-12T20:24:24+02:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<ccukqi$gt8$04$1@news.t-online.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu>`

```
Howard Brazee wrote <ccuiuf$d6k$1@peabody.colorado.edu>:

> Switching from one relational database using SQL to
> another is
> trivial.   The differences between ways of handling DB2 code within CoBOL
> programs can be bigger than switching between Oracle and DB2.

I would not buy that. While SQL is SQL is SQL, the details differ. That is
not really an issue; what is more important is that you can forget half of
what you know about writing performant Queries in DBMS 1 if you switch to
DBMS 2. Also, there are all kinds of locking and other kinds of behavior,
which are particularly different between Oracle and the rest of the world.
While it is trivial to write a trivial SQL statement in just any relational
DBMS, it is less trivial to avoid freezing down the whole system after you
switched. 

Joachim
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Richard Steiner <rsteiner@visi.com>
- **Date:** 2004-07-12T18:33:46+00:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<slrncf5mca.5me.rsteiner@bigmike.claycon.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu>`

```
On Mon, 12 Jul 2004 17:49:04 GMT in comp.lang.cobol, Howard Brazee
<howard@brazee.net> spake unto us, saying:

> CICS is pretty much unique, but I have been able to work over half of my
> career on IBM mainframes without significant CICS work.

I've done some batch COBOL work as well, but since I've spent most of
my career playing with on-line transactions (either in TIP/HVTIP or in
COMS), it's CICS that I've been naturally more curious about.

Okay, I'm curious about TPF as well, but who uses that now except for
the folks at WorldSpan, etc.?

> As for COBOL2 and DB2, the main trick is to convince personal that you
> know how to do the work.  Switching from one relational database using
> SQL to another is trivial.   The differences between ways of handling
> DB2 code within CoBOL programs can be bigger than switching between
> Oracle and DB2.

When I was at NWA I had a chance to compare some COBOL/RDMS1100 code
with some IBM COBOL/DB2 code, and it was pretty close in terms of the
basic syntax.  The examples we had seemed similar, anyway.

> I once didn't get a job because I didn't have COBOL 2 experience.
> Well, I had experience with COBOL on VAX and Univac that looked just
> like COBOL 2, and I had experience on IBM with older versions of COBOL,
> so there was nothing I needed to learn - but since they couldn't check
> off that I had experience with it, I didn't get the job.

That seems to be the status quo for most employers nowadays.  One has
to have specifics -- general language or coding experience doesn't seem
to be worth diddly.  :-(

> Funny thing is that lots of shops skipped right past COBOL 2 because
> it didn't have everything needed for Y2K.    But it was standard COBOL.  

What's the current flavor of IBM COBOL called?
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-07-12T17:30:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2lgl87Fbtei5U1@uni-berlin.de>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu> <slrncf5mca.5me.rsteiner@bigmike.claycon.com>`

```
I believe VisaNet uses TPF.

>>> Richard Steiner<rsteiner@visi.com> 7/12/2004 12:33:46 PM >>>
On Mon, 12 Jul 2004 17:49:04 GMT in comp.lang.cobol, Howard Brazee
<howard@brazee.net> spake unto us, saying:

> CICS is pretty much unique, but I have been able to work over half of my
> career on IBM mainframes without significant CICS work.

I've done some batch COBOL work as well, but since I've spent most of
my career playing with on-line transactions (either in TIP/HVTIP or in
COMS), it's CICS that I've been naturally more curious about.

Okay, I'm curious about TPF as well, but who uses that now except for
the folks at WorldSpan, etc.?
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-13T03:35:29+00:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<5MIIc.831$mL5.260@newsread1.news.pas.earthlink.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu> <slrncf5mca.5me.rsteiner@bigmike.claycon.com>`

```

"Richard Steiner" <rsteiner@visi.com> wrote in message
news:slrncf5mca.5me.rsteiner@bigmike.claycon.com...
> On Mon, 12 Jul 2004 17:49:04 GMT in comp.lang.cobol, Howard Brazee
> <howard@brazee.net> spake unto us, saying:
…[34 more quoted lines elided]…
> What's the current flavor of IBM COBOL called?

For z/OS (the most common - I think - IBM environment) it is
    IBM Enterprise COBOL for z/OS & OS/390
        commonly known as
   Enterprise COBOL

For the most current "bookshelf" of documentation see:

   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/Shelves/IGY3SH20
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Peter Flass <Peter_Flass@Yahoo.com>
- **Date:** 2004-07-14T01:01:59+00:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<bC%Ic.63416$bp1.27997@twister.nyroc.rr.com>`
- **In-Reply-To:** `<slrncf5mca.5me.rsteiner@bigmike.claycon.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu> <slrncf5mca.5me.rsteiner@bigmike.claycon.com>`

```
Richard Steiner wrote:
> 
> I've done some batch COBOL work as well, but since I've spent most of
> my career playing with on-line transactions (either in TIP/HVTIP or in
> COMS), it's CICS that I've been naturally more curious about.

I don't think TIP and CICS are all that similar, IIRC.

[snip]

>>I once didn't get a job because I didn't have COBOL 2 experience.
>>Well, I had experience with COBOL on VAX and Univac that looked just
…[8 more quoted lines elided]…
> 

This was discussed here not too long ago.  Unfortunately the people or 
software doing the screening don't understand what the job actually 
requires, all they do is look for keywords to check off.  If you get 
through the first level you might have a chance.  If the resume is 
screened by a program you might be able to get away with something like 
"experienced with TIP, a CICS/TS-like transaction processing monitor."

One other factor is equal-opportunity employment laws.  If you put in 
the job description or ad that a job requires two years CICS experience, 
by gosh, you're setting yourself up for a potential lawsuit if you don't 
stick to that.  Either you'll be explaining why you hired someone 
without the stated qualifications if you turn down an applicant with 
them, or else someone will sue charging that you discouraged potential 
applicants from applying by listing phony job requirements.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-14T09:22:35+00:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<40f4fb27.220447885@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu> <slrncf5mca.5me.rsteiner@bigmike.claycon.com> <bC%Ic.63416$bp1.27997@twister.nyroc.rr.com>`

```
Peter Flass <Peter_Flass@Yahoo.com> wrote:

>This was discussed here not too long ago.  Unfortunately the people or 
>software doing the screening don't understand what the job actually 
…[3 more quoted lines elided]…
>"experienced with TIP, a CICS/TS-like transaction processing monitor."

Or you might say:
Weakness: have no experience with CICS.

During a dry spell, I did that (for something other than CICS) and got a job
within a week. :)
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Charles Shannon Hendrix <shannon@news.widomaker.com>
- **Date:** 2004-07-23T22:35:24-04:00
- **Newsgroups:** alt.folklore.computers,comp.lang.cobol
- **Message-ID:** `<cthsdc.sql.ln@escape.goid.lan>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <ccuiuf$d6k$1@peabody.colorado.edu> <slrncf5mca.5me.rsteiner@bigmike.claycon.com>`

```
["Followup-To:" header set to alt.folklore.computers.]

> That seems to be the status quo for most employers nowadays.  One has
> to have specifics -- general language or coding experience doesn't seem
> to be worth diddly.  :-(

Amen.

I can write code in most any language, I just need time to practice.

No one wants to give you that time.

They scan your resume for buzzwords, and reject you without any
regard for your capacity to learn, or what your experience in other
languages/systems/hardware might have given you.
```

#### ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-12T21:26:52-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<10f6i394dlc37c9@corp.supernews.com>`
- **In-Reply-To:** `<vfs8ApHpvioW092yn@visi.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com>`

```
Richard Steiner wrote:
> Hi, guys...
> 
…[3 more quoted lines elided]…
> there is in IBMland.

If you haven't yet, take a look at Royal Caribbean cruise lines - 
they're based in Miami (I believe), and they're using 2200's...
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-13T01:42:04-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407130042.1d967515@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote in message news:<10f6i394dlc37c9@corp.supernews.com>...
> Richard Steiner wrote:
> > Hi, guys...
…[7 more quoted lines elided]…
> they're based in Miami (I believe), and they're using 2200's...

Cool! Do employees get free travel? And, is Algol still in use on
these mainframes? I ask this because Burroughs was one of the Seven
Dwarves that became Unisys along with Honeywell and others.

In 1991 I interviewed at a Florida company that was still building and
maintaining Algol compilers for Unisys. I wonder if the geographical
proximity is more than coincidental.
> 
> 
…[9 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-13T08:40:58-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd0vqb$1kj7$1@si05.rsvl.unisys.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com>`

```
"Edward G. Nilges" <spinoza1111@yahoo.com> wrote in message
news:f5dda427.0407130042.1d967515@posting.google.com...

> > If you haven't yet, take a look at Royal Caribbean cruise lines -
> > they're based in Miami (I believe), and they're using 2200's...

More on this below.

> And, is Algol still in use on
> these mainframes?

Not in heavy use on the Unisys OS2200 systems, which are the descended from
the Univac 1108.  ALGOL's common on the Unisys MCP systems.  So far as I
know Unisys does not offer an ALGOL compiler for the OS2200 environment.

But as you indicate below, there might be a third party that does so.

> I ask this because Burroughs was one of the Seven Dwarves
> that became Unisys along with Honeywell and others.

Dunno how you meant the grammar, but Honeywell didn't end up part of Unisys.

> In 1991 I interviewed at a Florida company that was still building and
> maintaining Algol compilers for Unisys.

I have no knowledge of this; I've been directly involved with developing and
maintaining Unisys MCP language compilers since September 1984, and I can
state with absolute certainty that primary ALGOL compiler development and
maintenance *for that system* has been "in-house" during that entire
period -- prior to 1984, in Mission Viejo; from 1984 to 1994 in Lake Forest;
and from 1994 to the present back in Mission Viejo.  Some work on the ALGOLs
was also done from Tredyffrin throughout the subject period.

Back to Royal Caribbean:  I personally wasn't aware that this company was
using 2200's, but I was able to determine that Royal Caribbean International
(NYSE:RCL) also operates Celebrity Cruise Lines.

I was, however, under the impression that *Carnival*, also based in Miami,
is (or was at one recent time) a 2200 customer.  Carnival Corporation
(NYSE:CCL) has grown significantly over the last decade, and is now the
parent company of Carnival Cruise Lines, Princess Cruises, Holland America
Line, Costa Cruises, P&O Cruises, AIDA, Cunard Line, Ocean Village, P&O
Cruises Australia, Swan Hellenic, Seabourn Cruise Line and Windstar Cruises.
That's quite a portfolio.   I believe that from time to time there have been
job offerings posted on behalf of Carnival for COBOL folk (and if I remember
right, explicitly in the OS2200 environment) in this very news group.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-13T11:58:30-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd10r6$ftf$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <cd0vqb$1kj7$1@si05.rsvl.unisys.com>`

```
In article <cd0vqb$1kj7$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:

[snip]

>I believe that from time to time there have been
>job offerings posted on behalf of Carnival for COBOL folk (and if I remember
>right, explicitly in the OS2200 environment) in this very news group.

Hmmmmm... was it the one that generated this response?

<http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&selm=b1criu%24qga%241%40panix1.panix.com>

--begin quoted text:

When posting to comp.lang.cobol please include a rate, or range of 
rates...

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-13T09:59:45-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd14e1$1no1$1@si05.rsvl.unisys.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <cd0vqb$1kj7$1@si05.rsvl.unisys.com> <cd10r6$ftf$1@panix5.panix.com>`

```
Don't think that was the one; the original posting indicated the job site
was in Atlanta, and I believe the shop for CCL is in Miami.

    -Chuck Stevens

<docdwarf@panix.com> wrote in message news:cd10r6$ftf$1@panix5.panix.com...
> In article <cd0vqb$1kj7$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
…[4 more quoted lines elided]…
> >job offerings posted on behalf of Carnival for COBOL folk (and if I
remember
> >right, explicitly in the OS2200 environment) in this very news group.
>
> Hmmmmm... was it the one that generated this response?
>
>
<http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&selm=b1criu%24qga%241%40
panix1.panix.com>
>
> --begin quoted text:
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "Charlie Gibbs" <cgibbs@kltpzyxm.invalid>
- **Date:** 2004-07-13T07:54:57-08:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<941.690T2894T4746399cgibbs@kltpzyxm.invalid>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com>`

```
In article <f5dda427.0407130042.1d967515@posting.google.com>
spinoza1111@yahoo.com (Edward G. Nilges) writes:

>LX-i <lxi0007@netscape.net> wrote in message
>news:<10f6i394dlc37c9@corp.supernews.com>...
…[6 more quoted lines elided]…
>Dwarves that became Unisys along with Honeywell and others.

I doubt it.  While it's true that Algol and variants were big on
Burroughs machines, the 2200 series are descendents of the 1100
line, which was Univac.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-13T21:22:30-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<10f9675se0mrke6@corp.supernews.com>`
- **In-Reply-To:** `<f5dda427.0407130042.1d967515@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com>`

```
Edward G. Nilges wrote:
> LX-i <lxi0007@netscape.net> wrote in message news:<10f6i394dlc37c9@corp.supernews.com>...
> 
…[15 more quoted lines elided]…
> Dwarves that became Unisys along with Honeywell and others.

I'm not sure - they sent me an e-mail (found my resume on the web), but 
at that time, I wasn't in the market.

> In 1991 I interviewed at a Florida company that was still building and
> maintaining Algol compilers for Unisys. I wonder if the geographical
> proximity is more than coincidental.

Could be...  :)  (Of course, I know the States of Georgia and Florida 
are still using Unisys mainframes, as they were well-represented at the 
last UNITE conference.)  So, if you're looking for the south, you might 
have some luck in those places as well.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-14T09:22:35+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<40f4fb39.220465852@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <10f9675se0mrke6@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote:


> I know the States of Georgia and Florida 
>are still using Unisys mainframes, as they were well-represented at the 
>last UNITE conference.

The State of New York often advertises for Unisys programmers. Pay rate is good.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "Stimpy" <stimpy1997uk@yahoo.com>
- **Date:** 2004-07-15T23:21:53+01:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<2loelrFeoirsU1@uni-berlin.de>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com>`

```
Edward G. Nilges wrote:
>
> Cool! Do employees get free travel? And, is Algol still in use on
> these mainframes? I ask this because Burroughs was one of the Seven
> Dwarves that became Unisys along with Honeywell and others.

The Bunch... Burroughs, Univac, Nixdorf, C????, Honeywell
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-07-15T15:44:34-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd71cj$2te7$1@si05.rsvl.unisys.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <2loelrFeoirsU1@uni-berlin.de>`

```

"Stimpy" <stimpy1997uk@yahoo.com> wrote in message
news:2loelrFeoirsU1@uni-berlin.de...

> The Bunch... Burroughs, Univac, Nixdorf, C????, Honeywell

Burroughs, Univac, NCR (National Cash Register), CDC (Control Data
Corporation), Honeywell.  On this side of the pond, anyway.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** Peter Flass <Peter_Flass@Yahoo.com>
- **Date:** 2004-07-15T23:55:59+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<jQEJc.45462$yd5.45198@twister.nyroc.rr.com>`
- **In-Reply-To:** `<2loelrFeoirsU1@uni-berlin.de>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <2loelrFeoirsU1@uni-berlin.de>`

```
Stimpy wrote:

> Edward G. Nilges wrote:
> 
…[5 more quoted lines elided]…
> The Bunch... Burroughs, Univac, Nixdorf, C????, Honeywell

Burroughs, Univac, *NCR*, *CDC*, Honeywell.  Previously "the seven 
dwarfs", though I don't recall the other two: RCA and GE?



> 
>
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** Anne & Lynn Wheeler <lynn@garlic.com>
- **Date:** 2004-07-15T18:25:57-06:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<uiscon6ga.fsf@mail.comcast.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <2loelrFeoirsU1@uni-berlin.de>`

```
> The Bunch... Burroughs, Univac, Nixdorf, C????, Honeywell

a few old bunch/dwarf postings:
http://www.garlic.com/~lynn/2002o.html#78 Newsgroup cliques?
http://www.garlic.com/~lynn/2003.html#14 vax6k.openecs.org rebirth
http://www.garlic.com/~lynn/2003.html#36 mainframe
http://www.garlic.com/~lynn/2003.html#71 Card Columns
http://www.garlic.com/~lynn/2003b.html#61 diffence between itanium and alpha
http://www.garlic.com/~lynn/2003o.html#43 Computer folklore - forecasting Sputnik's orbit with
http://www.garlic.com/~lynn/2004d.html#22 System/360 40th Anniversary

seven dwarfs:
burroughs, control data, general electric, honeywell, 
ncr, rca, sperry-rand 

BUNCH:
burroughs, univac, ncr, control data, honeywell
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** "Steve McKenna" <steveDELETE@mckenna.ca>
- **Date:** 2004-07-19T10:30:10+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<SoNKc.226775$rCA1.92538@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <10f6i394dlc37c9@corp.supernews.com> <f5dda427.0407130042.1d967515@posting.google.com> <2loelrFeoirsU1@uni-berlin.de>`

```
Control Data??

"Stimpy" <stimpy1997uk@yahoo.com> wrote in message
news:2loelrFeoirsU1@uni-berlin.de...
> Edward G. Nilges wrote:
> >
…[16 more quoted lines elided]…
>
```

#### ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-13T03:41:07+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<nRIIc.835$mL5.295@newsread1.news.pas.earthlink.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com>`

```
What part of the country are you in?  There are actually some (not many)
Community Colleges still providing IBM-centric "JCL, CICS, Utilities, whatever)
courses.  I know that near me, Northern Illinois University has fairly extensive
courses.

If you give me a "general" location, I may be able to find the name of someplace
where you could get some training *and* some "on machine" time.

If you want to check on your own, check out the "IBM Scholars Program"
information starting at:

   http://www-306.ibm.com/software/info/university/featured_members.html
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-13T02:52:02-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<iS58ApHpva6b092yn@visi.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <nRIIc.835$mL5.295@newsread1.news.pas.earthlink.net>`

```
Here in alt.folklore.computers,
"William M. Klein" <wmklein@nospam.netcom.com> spake unto us, saying:

>What part of the country are you in?

I'm in southwestern suburb of Minneapolis/St. Paul.  :-)

>There are actually some (not many) Community Colleges still providing
>IBM-centric "JCL, CICS, Utilities, whatever) courses.  I know that
>near me, Northern Illinois University has fairly extensive courses.

Hmmm.  That sounds like it could be useful.

>If you want to check on your own, check out the "IBM Scholars Program"
>information starting at:
>
>   http://www-306.ibm.com/software/info/university/featured_members.html

Looks like there are several places in the Twin Cities on that list,
so it looks like I need to do some searching here.  :-)

Thanks for the information!
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Joe Morris <jcmorris@mitre.org>
- **Date:** 2004-07-13T12:59:44+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd0mc0$104$1@newslocal.mitre.org>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <nRIIc.835$mL5.295@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> writes:

>What part of the country are you in?  There are actually some (not many)
>Community Colleges still providing IBM-centric "JCL, CICS, Utilities,
>whatever) courses.  I know that near me, Northern Illinois University
>has fairly extensive courses.

...and I'll bet that a lot of the reason for that is Dr. Robert Rannie,
who until the early 1980s was my opposite number at Oak Ridge National
Labs.  I've never been to NIU, but knowing Robert I expect that
anyone who gets through the classes he teaches there can be assumed to
understand what's going on inside both the OS and the computer.

Joe Morris
```

#### ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-14T19:55:32-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407141855.29014ef9@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com>`

```
rsteiner@visi.com (Richard Steiner) wrote in message news:<vfs8ApHpvioW092yn@visi.com>...
> Hi, guys...
> 
…[3 more quoted lines elided]…
> there is in IBMland.

Many companies and other institutions talk a good game about getting
rid of their mainframes and their inventory of Cobol programs, because
structurally "the mainframe" has become the intended focus of user
resentment, in a structure wherein the phenomenon is divided between
"usable, direct, honest" speech, and "unusable, overly complex, and
dishonest" writing.

This bifurcation pervades technical and media discourse...to the
extent that in the celebrations of the "heroes" of September 11 one
finds firefighters and cops (who deserved their honors, of course) but
none at all of the achievement of air traffic controllers, who
systematically landed thousands of aircraft when the FAA grounded
flights on that date. In the public psyche, the fire-fighter or cop is
admirable in part because he's able to create a defensible
self-definition and culture around his work, and exclude others,
whereas the air traffic controllers failed signally to do so in 1981,
and, ever since, have been a suspect crew and hence, in the media,
invisible. Their work becomes a form of writing which is taken for
granted and as such cannot be named or celebrated.

[Parenthetically we find a similar economy in Grigorii Medvedev's
account of Chernobyl: the Russian firefighters are celebrated, but the
nuclear technicians, despite similar self-sacrifice, are in effect
blamed for the disaster.]

As a result companies and institutions have concealed their ongoing
dependence on a morass of ill-understood software in mainframes, and,
in answer to your question, still need Cobol people...and are willing
in many cases to overlook platform dependencies. You do need to learn
JCL and the IBM mainframe "utilities". CICS, as another poster has
pointed out, is somewhat optional.

My experience in the 1970s was that one could go far if one troubled
to learn the amazingly primitive "utilities" for common tasks such as
printing the contents of a file. They turned out even then to have all
sorts of options and giz mos added over time which made them useful
for real work, as long as one reconciled oneself to their weirdness.

Be sure to learn Rexx, which is a language developed at IBM UK in the
early 1980s by Mike Cowlishaw. Originally intended as a way to write
procedures on Conversational Monitor System, REXX is now also used on
MVS and Time Squandering Option (TSO).

Rexx is based on PL/I and as such has a reasonably up to date syntax.
Its semantics is based on the traditional IBM MIS idea (which I think
dates to the IBM 1401, a character, decimal machine introduced in
1959) that all data worth processing is a completely variable length
string or a completely variable length decimal number.

As such Rexx is a powerful tool for getting fast results on the
mainframe.


> 
> No, this isn't a surprise to me.  :-)
…[19 more quoted lines elided]…
> a.f.c (since I know a lot of former IBMers post there as well).
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-07-15T02:00:39-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<Xui9ApHpvWaP092yn@visi.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com>`

```
Here in alt.folklore.computers,
spinoza1111@yahoo.com (Edward G. Nilges) spake unto us, saying:

>Be sure to learn Rexx, which is a language developed at IBM UK in the
>early 1980s by Mike Cowlishaw. Originally intended as a way to write
>procedures on Conversational Monitor System, REXX is now also used on
>MVS and Time Squandering Option (TSO).

As a long-time OS/2 user, I'm quite familiar with REXX.  :-)
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** docdwarf@panix.com
- **Date:** 2004-07-15T05:25:53-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd5ij1$89o$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com>`

```
In article <f5dda427.0407141855.29014ef9@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:

[snip]

>Many companies and other institutions talk a good game about getting
>rid of their mainframes and their inventory of Cobol programs, because
…[3 more quoted lines elided]…
>dishonest" writing.

Now this is an interesting distinction... speech vs writing?  There are 
many examples in common culture how the graphic ('graphic' here is used in 
the sense of 'writing' instead of 'drawing'; compare 'telegraph' with 
'graphic arts') is superior to the spoken ('get it in writing', 'it is 
written thus', 'it's in the book' all indicate a kind of solidity or 
permanence).

How is it that you classify the two in this manner, speech 'on the right' 
and script 'on the left'?

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-15T19:40:28-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407151840.11a6ef20@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cd5ij1$89o$1@panix5.panix.com>...
> In article <f5dda427.0407141855.29014ef9@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[15 more quoted lines elided]…
> permanence).

That is why the situation is so damn confusing and that is why a Frog,
of all people, is needed to sort it out for us (Derrida).

Yes, on the face of it we think writing is superior to speech ("get it
in writing").

But note how once you enter the education system past K-12 a very
curious reversal takes place.

A sort of Romanticism settles in where (perhaps merely as a result of
academic and professional competition), orality resumes its topmost
place vis a vis writing.

Actually attending the lecture becomes "better than" reading the
book...in part because any slob can "read the book".

In computing, I have long noticed how upper level executives depend
not on writing but on orality. When one company made the mistake of
trying to "groom" me for an upper level job as a suit, they placed
great emphasis on my need to learn the Great Art of Powerpoint
presentation.

I was informed that my logocentric, professorial and bookish air were
positive drawbacks because in the executive presentation, similar to
the argument before the Supreme Court, the logocentric flow of
presentation is continually interrupted and superseded by the orality
of the executive's, or judge's breaking in with the question that
undercuts the entire presentation.

Part of executive presentation is in fact the oral, pre-literate
skill, similar to that of the court jester in the Middle Ages, of
being able to respond to pre-literate power at the cost (today,
anyway) of your job.

I could see that my handlers had a point, but at the same time they
were themselves merely aging technical types and academic wash-outs
from the tenure system who themselves didn't have a clue: for they
actually thought that the pre-literate could be reduced to yet another
technical manual.

It was only in fact when I read Derrida's Writing and Difference and
Of Grammatology that I could see from whence the confusion resulted:
for my handlers, and myself, were enmeshed in a dialectical situation
such that any logocentric reduction was foolish.

I found in fact that the ability to make an "executive presentation"
is more a matter of completely, in the Zen fashion, letting go of the
outcome and having fun in the very process.

We need only to contrast George Bush's self-presentation and that of
Clinton to see the key point: for Bush has obviously "prepared" a
profoundly false "written" persona whereas Clinton, while mastering in
fact far more written detail that Bush, projected something akin to
his reality, which Clinton, unlike Bush, has been able to confront.

> 
> How is it that you classify the two in this manner, speech 'on the right' 
> and script 'on the left'?
>
I try not to. I try to keep in mind that we cannot think outside the
two to any sort of conceivable world in which speech existed, and
writing did not. For in the closest situation to a pre-writing world,
that of the primitive, family cohesion and storytelling seems to
REPLACE writing smoothly becoming what I think derrida calls "arche"
writing, a difficult term, meaning, apparently, "that which performs
the function of what we choose to call writing".

Derrida is difficult to understand because he does not write like the
typical American or English hack-philosopher, but in the terms that
might be used by the latter, I think that Derrida's claims, taking in
the analytic spirit, MEAN that were we to encounter creatures from
another planet, they might not have the "tokens" of writing (pens,
paper, ink, word processors or email) but would manifest empirical
behavior and institutions performing the function of writing, which is
to complement the deficiencies of orality with its own deficiencies.
> DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-16T09:18:07-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cd8kif$bb0$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <f5dda427.0407151840.11a6ef20@posting.google.com>`

```
In article <f5dda427.0407151840.11a6ef20@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cd5ij1$89o$1@panix5.panix.com>...
>> In article <f5dda427.0407141855.29014ef9@posting.google.com>,
…[19 more quoted lines elided]…
>of all people, is needed to sort it out for us (Derrida).

A structuralist... ahhhhh, now it begins to become apparent.

(I almost wrote 'now it makes sense'... but then realised the inherent 
contradiction.)

>
>Yes, on the face of it we think writing is superior to speech ("get it
…[10 more quoted lines elided]…
>book...in part because any slob can "read the book".

This was not my experience; in some institutions I attended (Bard, 
Columbia, NYU) the professors made it clear that the lectures were 
intended to compliment/supplement the text and that a student would be at 
a disadvantage were s/he not familiar with both.  At my Alma Mater (St 
John's College, Annapolis, MD) the texts were considered paramount, to the 
point where courses in the source-languages of many (Ancient Greek and 
French) were required.

Different schools have different rules, though... whatever happened to the 
wearing of the Freshman beanie, anyhow?

>
>In computing, I have long noticed how upper level executives depend
>not on writing but on orality.

Oh, I *cannot* resist... better than depending on things eminating from 
the other end of the digestive tract, neh?

>When one company made the mistake of
>trying to "groom" me for an upper level job as a suit, they placed
…[8 more quoted lines elided]…
>undercuts the entire presentation.

This might be the case only if the presentation's structure depends on an 
uninterrupted flow.  Consider the differences in presentation of a typical 
Socratic dialogue and a classic university lecture; the latter depends on 
a passive audience while the former allows for... well, dialogue.

>
>Part of executive presentation is in fact the oral, pre-literate
>skill, similar to that of the court jester in the Middle Ages, of
>being able to respond to pre-literate power at the cost (today,
>anyway) of your job.

'I don't want yes-men around me.  I want everyone to tell the truth, even 
if costs them their jobs.' - Samuel Goldwyn.

>
>I could see that my handlers had a point, but at the same time they
…[3 more quoted lines elided]…
>technical manual.

'We need people to be creative and independent... so let's give them 
lessons which, if they follow them rigidly, will all them to do so on 
command.'  It might be a good idea to be... wary of 'points' made by 
people who 'didn't have a clue.'

>
>It was only in fact when I read Derrida's Writing and Difference and
>Of Grammatology that I could see from whence the confusion resulted:
>for my handlers, and myself, were enmeshed in a dialectical situation
>such that any logocentric reduction was foolish.

'This situation cannot be reduced to words... let's talk about it a lot, 
then!'

>
>I found in fact that the ability to make an "executive presentation"
>is more a matter of completely, in the Zen fashion, letting go of the
>outcome and having fun in the very process.

'The journey is the destination... but let's hope the train isn't late, 
anyway.'

[snip]

>> 
>> How is it that you classify the two in this manner, speech 'on the right' 
>> and script 'on the left'?
>>
>I try not to.

<http://groups.google.com/groups?selm=f5dda427.0407141855.29014ef9%40posting.google.com&output=gplain>

(pardon the sentence-fragment)

--begin quoted text:

... the phenomenon is divided between "usable, direct, honest" speech, and 
"unusable, overly complex, and dishonest" writing.

--end quoted text

Seems like the try wasn't all too successful, neh?

>I try to keep in mind that we cannot think outside the
>two to any sort of conceivable world in which speech existed, and
…[4 more quoted lines elided]…
>the function of what we choose to call writing".

Similar things have been noticed... you might wish to consider

<http://groups.google.com/groups?selm=74jgb6%24e6q%241%40callisto.clark.net&output=gplain>

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 5)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-16T20:53:43-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407161953.665181ce@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <f5dda427.0407151840.11a6ef20@posting.google.com> <cd8kif$bb0$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cd8kif$bb0$1@panix5.panix.com>...
> In article <f5dda427.0407151840.11a6ef20@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[26 more quoted lines elided]…
> contradiction.)

Without structuralism there is no making sense, for example, of the
fact that Plato explicitly derides the very idea of a comprehensive
encyclopedia or manual while he relied during his lifetime on writing.
Human behavior being constantly self-reflexive is not going to "make
sense" in any neat, technical or artifactual sense.

> 
> >
…[19 more quoted lines elided]…
> French) were required.

Guess what. The professors are not in charge, while being absolutely
essential to the continued functioning of the system.
> 
> Different schools have different rules, though... whatever happened to the 
…[24 more quoted lines elided]…
> a passive audience while the former allows for... well, dialogue.

The paradox here is that the actual Socratic dialog was not a "dialog"
in the dialogic, Bakhtinian sense at all.

Instead, Socrates' one goal in the dialogs as preserved (an important
qualifier because their written presentation is all we know) is
proving a foregone conclusion. In The Republic, Thasymachus is a
cardboard character who is trotted on stage to claim that justice is
superior force, only to be proven wrong in a non-dialogic fashion.

Indeed, the whole process has been inspirational for totalitarians
since it purports to show a sort of Leninist point, that discussion
has a foregone conclusion which we must accept.

Consider the major survival of Socratic dialogue, and this is the
typical lecture in the prestige American law school.

In the non-prestige American law school, like John Marshall in
Chicago, the students actually have a chance to dialog with professors
who are in many cases working lawyers who actually know how to file
briefs and motions nearby in the Loop.

But in the prestige venue, everything becomes a "Socratic" "dialog"
the purpose of which is to show that the law professor knows
everything about "contracts" even when (we may well imagine) his own
handymen at his own new house have ripped him off by knowing more
about real contracts.

Engaging in this dialog becomes very much unlike give and take.

In fact, my own experience on university faculty is that the students
would like the prof to give a one-way, amusing lecture and don't
necessarily want to talk back.

> 
> >
…[7 more quoted lines elided]…
> 
Truly a paradox, for what he will end up is a series converging to
yes-men.

> >
> >I could see that my handlers had a point, but at the same time they
…[8 more quoted lines elided]…
> people who 'didn't have a clue.'

Indeed.

> 
> >
…[6 more quoted lines elided]…
> then!'

Chinese philosopher Ling Fu-Yan: "we must talk a great deal before we
are silent".

There are of course books which one reads once, and other books to
which one returns many times.

> 
> >
…[40 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-17T11:09:43-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdbffn$a92$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407151840.11a6ef20@posting.google.com> <cd8kif$bb0$1@panix5.panix.com> <f5dda427.0407161953.665181ce@posting.google.com>`

```
In article <f5dda427.0407161953.665181ce@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cd8kif$bb0$1@panix5.panix.com>...
>> In article <f5dda427.0407151840.11a6ef20@posting.google.com>,
…[33 more quoted lines elided]…
>sense" in any neat, technical or artifactual sense.

What you describe here seems to be along the lines of 'members of the 
human species do not always behave in fashions which other members of that 
species would label as 'sensible'' or 'Sense?  Why do you expect something 
to 'make sense' when you're dealing with people?'

>
>> 
…[23 more quoted lines elided]…
>essential to the continued functioning of the system.

Guess what... I don't recall mentioning anything about 'in charge', doing 
so reminds me too much of the Bilderbergers.  You made a statement about 
'the education system past K-12' without any supporting evidence 
and I gave evidence - granted, anecdotal - to the contrary.

>> 
>> Different schools have different rules, though... whatever happened to the 
…[27 more quoted lines elided]…
>in the dialogic, Bakhtinian sense at all.

This just might possibly be one of the reasons that it was referred to as 
a 'Socratic dialogue' and not a 'Bakhtinian' one.

>
>Instead, Socrates' one goal in the dialogs as preserved (an important
…[3 more quoted lines elided]…
>superior force, only to be proven wrong in a non-dialogic fashion.

And yet... there are still folks talking to each other, an interchange - 
granted staged, structured and stylised but an interchange, nonetheless - 
of views and idea.

>
>Indeed, the whole process has been inspirational for totalitarians
>since it purports to show a sort of Leninist point, that discussion
>has a foregone conclusion which we must accept.

Indeed, many countries have called themselves 'democratic' when they are 
anything but; the concept of 'democracy' is not at fault here.

>
>Consider the major survival of Socratic dialogue, and this is the
>typical lecture in the prestige American law school.

You seem to have changed your emphasis from the 'education system past 
K-12' to a very specific subset of instutitions giving one particular kind 
of technical education; I am not sure what you are attempting to do here 
but it appears to disporve your original assertions.

[snip]

>In fact, my own experience on university faculty is that the students
>would like the prof to give a one-way, amusing lecture and don't
>necessarily want to talk back.

Ahhhhh... finally!  You see... I have anecdotal evidence one way, you have 
anecdotal evidence another.  This appears to be the crux of the matter.

>
>> 
…[10 more quoted lines elided]…
>yes-men.

... or a series converging to nobody, since they've all been fired.

>
>> >
…[24 more quoted lines elided]…
>are silent".

'Speech is silver yet silence is golden' is often... said.

>
>There are of course books which one reads once, and other books to
>which one returns many times.

Books?  Pfah, I read a book, once... didn't do much for me.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 7)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-17T17:58:48-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407171658.12054e2a@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407151840.11a6ef20@posting.google.com> <cd8kif$bb0$1@panix5.panix.com> <f5dda427.0407161953.665181ce@posting.google.com> <cdbffn$a92$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cdbffn$a92$1@panix5.panix.com>...
> In article <f5dda427.0407161953.665181ce@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[40 more quoted lines elided]…
> to 'make sense' when you're dealing with people?'

The educational system disseminates, as a mark of
pseudo-enlightenment, the idea that "nothing makes sense when dealing
with people". Structuralism and post-structuralism is an attempt to
make sense which is probably why conservative educators are so
terrified of it, for they are invested in a game in which only a
futile reactionary stance is supposed to "make sense".

> 
> >
…[29 more quoted lines elided]…
> and I gave evidence - granted, anecdotal - to the contrary.

Granted, anecdotal. 

The education "game" has always been threatened by the book because in
theory, some slob from the provinces could become that species of
irritating auto-didact outside the university, closed of old to all
but the wealthy EXCEPT when governments, in what has to be a
high-handed manner, open the universities to talents from all social
classes.

Thus the PhD candidate has always been expected, no matter what, to
Oedipally overcome his professors in oral exchanges.

This may be a good thing. One needs to be able to think on one's feet.

However, it pre-judges such phenomena as "distance learning" to such
an extent that instiutions are pre-characterized as diploma mills
irrespective of the hard work of their students.

> 
> >> 
…[31 more quoted lines elided]…
> a 'Socratic dialogue' and not a 'Bakhtinian' one.

The REAL Socrates appears to have been more "Bakhtinian" than his
amaneusis Plato who when he recorded "Socrates" was invested in the
success of a written Academy. In other words...the corruption was
written-in from the start.

> 
> >
…[80 more quoted lines elided]…
> 'Speech is silver yet silence is golden' is often... said.

Which is of course the paradox that Derrida got all hung up on. Speech
about speech is a zone of paradox.
> 
> >
…[5 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-17T22:24:40-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdcn18$2e7$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407161953.665181ce@posting.google.com> <cdbffn$a92$1@panix5.panix.com> <f5dda427.0407171658.12054e2a@posting.google.com>`

```
In article <f5dda427.0407171658.12054e2a@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cdbffn$a92$1@panix5.panix.com>...
>> In article <f5dda427.0407161953.665181ce@posting.google.com>,
…[45 more quoted lines elided]…
>with people".

Another blanket assertion without support... consider that such things are 
likely to be dismissed out-of-hand.

>Structuralism and post-structuralism is an attempt to
>make sense which is probably why conservative educators are so
>terrified of it, for they are invested in a game in which only a
>futile reactionary stance is supposed to "make sense".

I noticed that you were good enough to label them as 'attempts'... little 
else might be said.

>
>> 
…[39 more quoted lines elided]…
>classes.

Hmmmm... this seems to be... why, yes, another blanket assertion without 
any documentation whatsoever. 

>
>Thus the PhD candidate has always been expected, no matter what, to
>Oedipally overcome his professors in oral exchanges.

Really?  I thought that the PhD candidate, in order to be admitted into 
'the club', had to demonstrate to other members worthiness and that this 
was, in essence, no different than a tinker or a cobbler presenting a 
'master-work' to the guild's authorities.  Curious that one finds it 
possible to see this simple test-of-skill in terms that include 'Oedipal' 
and 'oral exchanges', though.

>
>This may be a good thing. One needs to be able to think on one's feet.

One might hope for chairs in the dissertation-chamber.

>
>However, it pre-judges such phenomena as "distance learning" to such
>an extent that instiutions are pre-characterized as diploma mills
>irrespective of the hard work of their students.

Oh, look... another blanket generalisation without any support outside of 
it's own asserting.

>
>> 
…[37 more quoted lines elided]…
>written-in from the start.

I am not sure what you are calling the 'REAL' (caps original) Socrates... 
are you referring to the depiction in Xenophon?  The answer to the 
question of 'Vass you dere, Charlie' in regards to Socrates seems rather 
obvious yet you seem to give credence to one depiction over another; this 
might indicate nothing about what was 'REAL' but, more Rohrshach-like, 
everything about the prejudices brought to the subject.

(Oh... and that assertion about the 'REAL' Socrates had - little surprise 
here - nothing in the way of support outside of itsself.)

[snip]

>> 
>> 'Speech is silver yet silence is golden' is often... said.
>
>Which is of course the paradox that Derrida got all hung up on. Speech
>about speech is a zone of paradox.

So might be said about thinking about thinking... but in those days folks 
didn't have television, they had to do *something* with their time.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 9)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-20T20:08:00-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407201908.31ac94b1@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407161953.665181ce@posting.google.com> <cdbffn$a92$1@panix5.panix.com> <f5dda427.0407171658.12054e2a@posting.google.com> <cdcn18$2e7$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cdcn18$2e7$1@panix5.panix.com>...
> In article <f5dda427.0407171658.12054e2a@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[104 more quoted lines elided]…
> any documentation whatsoever. 

This is in fact self-reflexive "documentation" since it's clear you've
been indoctrinated not to make sense without cites appropriate to the
hard sciences.

We become in other words well-trained not to make "blanket" assertions
even when they are necessary by an ideology that dares not speak its
name.

> 
> >
…[8 more quoted lines elided]…
> and 'oral exchanges', though.

The problem is that the process, in many instances, fails. Ability to
teach is never tested and even scholarship is inadequately tested, by
a reifying process at second tier institutions.

These institutions are aware, with that self-protective habit of irony
which is a feature of academic life, that the maxim is "publish or
perish". One (ironic) response is to publish, but a more sophisticated
response is to avoid publication. The problem is that the ironic
response, which is a refusal of critique, leaves the reified system in
control.

A midwestern philosopher  and teach, E. D. Klemke, published several
books in a non-ironic spirit including Essays on Wittgenstein and
works on the ontology of G. E. Moore. He remained non-ironic
throughout his career and actually believed, with reason, that he was
doing actual philosophy in this from his perch at two third-tier
institutions, which were graced, IMO, by his presence.

However, when I was asked to help nominate Klemke for a lifetime
achievement award shortly before his death, I learned that he was
denied the award by other faculty who'd felt he'd published...too
much.

A post-structuralist analysis of this sad situation, of the failure to
recognize a man's lifetime achievement, would show that "publish or
perish" by virtue of being an ironic response, and as such one that
despairs of change, means that it should never be interpreted
literally. What it MEANS is "publish what we expect to see, and do so
with an ultimate unseriousness because the name of this game is tenure
and parking spaces".

As such, Klemke's very idea that the university might after all be a
safe place for him to do philosophy was held up, throughout his
career, to an undertone of scorn. He was also a brilliant teacher for
the simple reason that he cared about philosophy, but this, of course,
and 1.75 will buy a coffee at Starbuck's.


> 
> >
> >This may be a good thing. One needs to be able to think on one's feet.
> 
> One might hope for chairs in the dissertation-chamber.

With one hopes leg and arm restraints and a high-intensity lamp.
Bitch-slapping might be a feature of some processes.

> 
> >
…[5 more quoted lines elided]…
> it's own asserting.

Best kind there is if one lives in a corrupt society.

> 
> >
…[49 more quoted lines elided]…
>
Except, of course, the text.
 
> [snip]
> 
…[9 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-21T07:56:22-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdlll6$h8v$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407171658.12054e2a@posting.google.com> <cdcn18$2e7$1@panix5.panix.com> <f5dda427.0407201908.31ac94b1@posting.google.com>`

```
In article <f5dda427.0407201908.31ac94b1@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cdcn18$2e7$1@panix5.panix.com>...
>> In article <f5dda427.0407171658.12054e2a@posting.google.com>,
>> Edward G. Nilges <spinoza1111@yahoo.com> wrote:

[snip]

>> >The educational system disseminates, as a mark of
>> >pseudo-enlightenment, the idea that "nothing makes sense when dealing
…[3 more quoted lines elided]…
>> likely to be dismissed out-of-hand.

[snip]

>> >The education "game" has always been threatened by the book because in
>> >theory, some slob from the provinces could become that species of
…[10 more quoted lines elided]…
>hard sciences.

Many things can seem to make sense without being true... isn't it 
self-evident that heavier things will fall faster than lighter ones?  
Person A asserts that heavier things fall faster than lighter one, Person 
G says that objects which experience no resistance fall at the same 
rate... where to go from here except to experimentation, observation and 
conclusion?

An alternative to this seems to be Carrol's 'Caucus-Race', from 'Alice in 
Wonderland', where everyone runs as they see fit and all are declared 
winners.

>
>We become in other words well-trained not to make "blanket" assertions
>even when they are necessary by an ideology that dares not speak its
>name.

I have no idea who 'we' might be here... but ideology or no, anyone can 
make a blanket assertion without any support or documentation.  In that 
wise all arguments based on such are equally valid... and equally invalid; 
you have, then, apparently rendered you arguments - and the conclusions 
derived therefrom - utterly indistinct from any others.

>
>> 
…[11 more quoted lines elided]…
>The problem is that the process, in many instances, fails.

Another unsupported assertion.

>Ability to
>teach is never tested and even scholarship is inadequately tested, by
>a reifying process at second tier institutions.

Ability to teach is not what a dissertation committe is measuring; as for 
the inadequate testing of scholarship... oh, look, another unsupported 
assertion!

[snip]

>However, when I was asked to help nominate Klemke for a lifetime
>achievement award shortly before his death, I learned that he was
>denied the award by other faculty who'd felt he'd published...too
>much.

Ahhhh, evidence of a sort... but, appropriately matching earlier 
statements I made, anecdotal evidence.

We now have evidence of equal quality - both are anecdotal - which leads 
to contradictory conclusions.  What do you believe the next step to be?

[snip]

>> >This may be a good thing. One needs to be able to think on one's feet.
>> 
…[3 more quoted lines elided]…
>Bitch-slapping might be a feature of some processes.

Someone of suitable credentials might be able to provide an analysis - 
post-structural or otherwise - of the metaphors used to describe academia 
which include 'Oedipal... oral performances', 'which dare not speak its 
name' and 'bitch-slapping'.

I, with a good bit of relief, will leave such things to The Professionals.

>
>> 
…[8 more quoted lines elided]…
>Best kind there is if one lives in a corrupt society.

How interesting... the response to the pointing-out of a blanket 
generalisation without any support outside of it's own asserting is... 
another of the same.

There's a Classic Response to such things that my Sainted Father was 
taught in the Bronx, permit me to trot it out here just to see how it 
works... 'sez who?'

[snip]

>> >The REAL Socrates appears to have been more "Bakhtinian" than his
>> >amaneusis Plato who when he recorded "Socrates" was invested in the
…[13 more quoted lines elided]…
>Except, of course, the text.

Which text outside of itsself, please?  Second request here.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 11)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-22T20:09:13-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407221909.58632a3a@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407171658.12054e2a@posting.google.com> <cdcn18$2e7$1@panix5.panix.com> <f5dda427.0407201908.31ac94b1@posting.google.com> <cdlll6$h8v$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cdlll6$h8v$1@panix5.panix.com>...
> In article <f5dda427.0407201908.31ac94b1@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[38 more quoted lines elided]…
> winners.

This is in fact a fantasy of the personality without internal
self-discipline: the anxiety that IF we depart from some reified
procedure, THEN "all are declared winners".

> 
> >
…[9 more quoted lines elided]…
>
But, of course, the support was there. In fact, when a conclusion is
reached in the essay form, the charge becomes that there is "too much"
documentation...too many words.

 
> >
> >> 
…[14 more quoted lines elided]…
>
? The incompetence and unoriginality of PhD holders from n-tier
institutions is in fact well-known and documented.
 
> >Ability to
> >teach is never tested and even scholarship is inadequately tested, by
…[5 more quoted lines elided]…
>
And what is it testing? Contribution to the sum-total of human
knowledge?

Here's another blanket assertion, just to piss you off: the ability to
teach cannot be separated, IMO, from scholarship. If it is, teaching
becomes a technology of emotional manipulation aimed at getting the
teacher high student rankings.
 
> [snip]
> 
…[7 more quoted lines elided]…
>
Any evidence can be dismissed. However, to have one's own pet cites
and studies in a human science is a corruption. We cannot "prove"
academic-sociological conclusions by OTHER than stories and
narratives, and today's best sociologists know this.

This is because we're part of the phenomenon described and have an
interest in the outcome.
 
> We now have evidence of equal quality - both are anecdotal - which leads 
> to contradictory conclusions.  What do you believe the next step to be?

Actually, this isn't true, because I was familiar with Klemke for
several years and I saw what was done to him by the sort of shitheads
he was surrounded by.

> 
> [snip]
…[13 more quoted lines elided]…
> I, with a good bit of relief, will leave such things to The Professionals.

If you can't stand the heat...

In the human sciences we're talking, are we not, about people's lives,
and they are not to be reduced to cites and studies, which are today
manufactured with corporate funding to alternatively prove that real
pain does not exist, or, preferably, that there's a simple mechanistic
explaination, and, of course, a product to buy: an anodyne.

"Someone of suitable credentials" is of course today's magus who as of
old is another stunted man dressed in today's priest's robes, whose
job it is to tell us that our stories are without foundation: that
pain either does not exist or can be ended with an anodyne.

This someone seems to rather haunt the epistemology of the Internet
which by oh, so very "empowering", disempowers precisely because we
see so many voices talking and so very few listening.
> 
> >
…[40 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 12)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T07:25:46+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<4100bbf4.124696776@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407171658.12054e2a@posting.google.com> <cdcn18$2e7$1@panix5.panix.com> <f5dda427.0407201908.31ac94b1@posting.google.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com>`

```
spinoza1111@yahoo.com (Edward G. Nilges) wrote:

>"Someone of suitable credentials" is of course today's magus who as of
>old is another stunted man dressed in today's priest's robes, whose
>job it is to tell us that our stories are without foundation: that
>pain either does not exist or can be ended with an anodyne.

"Pay no attention to the man behind the curtain." J. Frank Baum nailed
academicians with that personification. The hero was the dog, Toto, who pulled
the curtain aside to reveal Truth. Toto was Everyman.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T07:55:30-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdqubi$aud$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com> <4100bbf4.124696776@news.optonline.net>`

```
In article <4100bbf4.124696776@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:

[snip]

>"Pay no attention to the man behind the curtain." J. Frank Baum nailed
>academicians with that personification. The hero was the dog, Toto, who pulled
>the curtain aside to reveal Truth. Toto was Everyman.

Mr Wagner, just about every 'analysis' of 'The Wizard of Oz' with which I
am familiar assigns the 'Everyman' role to Dorothy; how is it that you
have come to your conclusion?

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 14)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T22:29:45+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<410177c9.14028828@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <4100bbf4.124696776@news.optonline.net>,
>Robert Wagner <robert.deletethis@wagner.net> wrote:
…[9 more quoted lines elided]…
>have come to your conclusion?

Toto sets the story in motion by running through Miss Gulch's garden, thereby
causing a conflict, which in turn causes Dorothy to be caught in a tornado. Toto
is the only character who loves her unconditionally for what she it; the others
want to change her. She says he's the only thing in life that brings her joy.

She goes on a quest through a land where ALL the male characters have a defect
-- cowardly, stupid, unfeeling, midget (no offense), flying monkey, full of
humbug. Was this thing written by a lesbian? Dorothy is seeking a perfect lover,
without much success.

Toto puts the quest to an end by revealing the wizard to be a fraud. Then he
stops her from going on yet another flight of fancy, another pointless quest in
a balloon. She comes of age when she wakes up to the real world.

The moral is that the love she was seeking was literally at her feet the whole
time. Dorothy is an immature Everywoman; Toto is her loyal partner, Everyman.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 15)_

- **From:** Eric Smith <eric-no-spam-for-me@brouhaha.com>
- **Date:** 2004-07-23T18:01:27-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<qhacxqp6ag.fsf@ruckus.brouhaha.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) writes about
Dorothy as "everywoman" in The Wizard of Oz:
> She goes on a quest through a land where ALL the male characters have
> a defect -- cowardly, stupid, unfeeling, midget (no offense), flying
> monkey, full of humbug

The book is *much* different than the film in this regard.  In the book,
the scarecrow claims to have no brains, the woodsman no heart, and that
lion no courage, just as in the film.  However, in the book, the
scarecrow is the one who comes up with clever plans to get out of
predicaments.  The woodsman points out that because of his lack of a
heart, he makes a conscious effort to be extremely careful to be
courteous and not to hurt anyone.  And the lion is quick to jump to the
party's defense whenever danger looms.

Thus in the book, it makes a lot more sense when the wizard eventually
gives them each a token item rather than what they requested.  Aside
from Dorothy, they each actually already possessed the attribute they
desired.

It reminds me of the article "Unskilled and Unaware of It" by
Justin Kruger and David Dunning (Journal of Personality and Social
Psychology Vol. 77 No. 6, December 1999), in which they found that
incompetent people often believe they are competent, but competent
people tend to underestimate their own abilities relative to others.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T21:45:52-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdsf0g$j73$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net>`

```
In article <410177c9.14028828@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[14 more quoted lines elided]…
>causing a conflict, which in turn causes Dorothy to be caught in a tornado.

Oh, *I* see now, Mr Wagner... you're basing your interpretation on the 
film, not the book.  That might explain a few things about your 
interpretation, certainly.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 16)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T04:17:32+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<4101d847.38734222@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>Oh, *I* see now, Mr Wagner... you're basing your interpretation on the 
>film, not the book.  That might explain a few things about your 
>interpretation, certainly.

Most interpretations are based on the film, not the book. The film is a cultural
icon experienced by nearly every American; the book isn't.

Huckleberry Finn, Moby Dick, The Scarlet Letter are works where the book
surpasses film(s). Baum's Wizard series doesn't belong in the category. But for
the 1939 film, his work would have been forgotten. 

Was it a Populist allegory, as most analysts say? Who cares? Populism is foreign
to today's Americans. They don't care about the Gold Standard vs. the Silver
Standard. To have enduring appeal, it had to address more universal issues.
Emotional issues. The screenwriters gave it that universalism. 

Yes, it's Pop Culture rather than respectible Philosophy. Are you prepared to
tell the lumpenproletariat that they are slobs?

I thought not.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 17)_

- **From:** jmfbahciv@aol.com
- **Date:** 2004-07-24T10:11:53+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<4102471f$0$5644$61fed72c@news.rcn.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com> <4101d847.38734222@news.optonline.net>`

```
In article <4101d847.38734222@news.optonline.net>,
   robert.deletethis@wagner.net (Robert Wagner) wrote:
>docdwarf@panix.com wrote:
>
…[4 more quoted lines elided]…
>Most interpretations are based on the film, not the book. The film is a 
cultural
>icon experienced by nearly every American; the book isn't.
>
>Huckleberry Finn, Moby Dick, The Scarlet Letter are works where the book
>surpasses film(s). Baum's Wizard series doesn't belong in the category. 
But for
>the 1939 film, his work would have been forgotten. 

Not in my life.  I read the book before I saw the film.  The books
were much better.  Judy Garland whinged all the time.  Dorothy
didn't.

Thread drift:  I found a set of self-published books by Mark Twain
and finally got around to reading one of them.  I just finished
three scifi short stories.  I never knew he wrote scifi.  I felt
like I was mining coal and found a huge lump of gold.

/BAH


Subtract a hundred and four for e-mail.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 18)_

- **From:** Randy Howard <randyhoward@FOOverizonBAR.net>
- **Date:** 2004-07-24T16:02:09+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<MPG.1b6c3dd56862b719989963@news.verizon.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com> <4101d847.38734222@news.optonline.net> <4102471f$0$5644$61fed72c@news.rcn.com>`

```
In article <4102471f$0$5644$61fed72c@news.rcn.com>, jmfbahciv@aol.com says...
> Thread drift:  I found a set of self-published books by Mark Twain
> and finally got around to reading one of them.  I just finished
> three scifi short stories.  I never knew he wrote scifi.  I felt
> like I was mining coal and found a huge lump of gold.

Can you provide a reference to this please, sounds interesting.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 19)_

- **From:** jmfbahciv@aol.com
- **Date:** 2004-07-25T10:03:24+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<410396ae$0$5638$61fed72c@news.rcn.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com> <4101d847.38734222@news.optonline.net> <4102471f$0$5644$61fed72c@news.rcn.com> <MPG.1b6c3dd56862b719989963@news.verizon.net>`

```
In article <MPG.1b6c3dd56862b719989963@news.verizon.net>,
   Randy Howard <randyhoward@FOOverizonBAR.net> wrote:
>In article <4102471f$0$5644$61fed72c@news.rcn.com>, jmfbahciv@aol.com 
says...
>> Thread drift:  I found a set of self-published books by Mark Twain
>> and finally got around to reading one of them.  I just finished
…[3 more quoted lines elided]…
>Can you provide a reference to this please, sounds interesting.

Damn.  Sorry for wasting your time; I meant to post it but
forgot.

Here's all the poop:

Author's National Edition
The Writings of Mark Twain Volume XIX
Sketches New and Old

That's the book info.  The titles of the 3 stories are:

Some Learned Fables, For Good Old Boys and Girls In Three
Parts

Part First--How the animals of the  Wood Sent out a Scientific
Expedition

Part Second--How the Animals of the Wood Completed Their
Scientific Labors

Part Third

/BAH

Subtract a hundred and four for e-mail.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 20)_

- **From:** Randy Howard <randyhoward@FOOverizonBAR.net>
- **Date:** 2004-07-25T23:16:30+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<MPG.1b6dfb49dcc7249398996e@news.verizon.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <4100bbf4.124696776@news.optonline.net> <cdqubi$aud$1@panix5.panix.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com> <4101d847.38734222@news.optonline.net> <4102471f$0$5644$61fed72c@news.rcn.com> <MPG.1b6c3dd56862b719989963@news.verizon.net> <410396ae$0$5638$61fed72c@news.rcn.com>`

```
In article <410396ae$0$5638$61fed72c@news.rcn.com>, jmfbahciv@aol.com says...
> In article <MPG.1b6c3dd56862b719989963@news.verizon.net>,
>    Randy Howard <randyhoward@FOOverizonBAR.net> wrote:
…[10 more quoted lines elided]…
> forgot.

No problem, at least you made it back... :-)
 
> Here's all the poop:
> 
> Author's National Edition
> The Writings of Mark Twain Volume XIX
> Sketches New and Old

I'll see if I can locate a copy, thank you.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-24T09:45:47-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdtp6b$iqf$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <410177c9.14028828@news.optonline.net> <cdsf0g$j73$1@panix5.panix.com> <4101d847.38734222@news.optonline.net>`

```
In article <4101d847.38734222@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[4 more quoted lines elided]…
>Most interpretations are based on the film, not the book.

Most interpretations have Dorothy as Everyman, Mr Wagner... what might be 
made of that?

[snip]

>Yes, it's Pop Culture rather than respectible Philosophy. Are you prepared to
>tell the lumpenproletariat that they are slobs?

As soon as I intend such a thing I'll give it consideration, Mr Wagner... 
but thanks e'er-so-much for asking.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 13)_

- **From:** Rich Alderson <news@alderson.users.panix.com>
- **Date:** 2004-07-23T15:44:47-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<mdd3c3ijyog.fsf@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407171658.12054e2a@posting.google.com> <cdcn18$2e7$1@panix5.panix.com> <f5dda427.0407201908.31ac94b1@posting.google.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com> <4100bbf4.124696776@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) writes:

> "Pay no attention to the man behind the curtain." J. Frank Baum nailed

ITYM L. Frank Baum, and you'd be wrong.

The book contains no reference to a curtain:  The "wizard" was standing behind
a screen which Toto knocked over when the Lion roared and startled him.

So, according to IMdb.com, you meant one of Noel Langley and Florence Ryerson
and Edgar Allan Woolf, or the uncredited Irving Brecher, William H. Cannon,
Herbert Fields, Arthur Freed, Jack Haley, E.Y. Harburg, Samuel Hoffenstein,
Bert Lahr, John Lee Mahin, Herman J. Mankiewicz, Jack Mintz, and Sid Silvers.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T07:20:33-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdqsa1$6on$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407201908.31ac94b1@posting.google.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com>`

```
In article <f5dda427.0407221909.58632a3a@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cdlll6$h8v$1@panix5.panix.com>...

[snip]
 
>> Ability to teach is not what a dissertation committe is measuring; as for 
>> the inadequate testing of scholarship... oh, look, another unsupported 
…[8 more quoted lines elided]…
>teacher high student rankings.

It seems that we are motivated by different purposes; it is not my 
intention to anger you but it is your purpose, in the above, to anger me.

I've not found much in UseNet that I consider of sufficient important to 
raise my ire... but I have found that when it is the intention of a 
participant to do so that there will be little of value, learning or humor 
which follows.  I'll cease participation, then, until such time as this 
motive has been removed from your attempts; feel free to try again at 
another time.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T07:22:39-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdqsdv$70p$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407201908.31ac94b1@posting.google.com> <cdlll6$h8v$1@panix5.panix.com> <f5dda427.0407221909.58632a3a@posting.google.com>`

```
In article <f5dda427.0407221909.58632a3a@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>docdwarf@panix.com wrote in message news:<cdlll6$h8v$1@panix5.panix.com>...

[snip]

>> Ability to teach is not what a dissertation committe is measuring; as for 
>> the inadequate testing of scholarship... oh, look, another unsupported 
…[8 more quoted lines elided]…
>teacher high student rankings.

It seems that we are motivated by different purposes; it is not my
intention to anger you but it is your purpose, in the above, to anger me.

I've not found much in UseNet that I consider of sufficient importance to 
raise my ire... but I have found that when it is the intention of a 
participant to do so that there will be little of value, learning or humor 
which follows.  I'll cease participation, then, until such time as this 
motive has been removed from your attempts; feel free to try again at 
another time.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-17T17:39:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40f963bb.509406956@news.optonline.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <f5dda427.0407151840.11a6ef20@posting.google.com> <cd8kif$bb0$1@panix5.panix.com> <f5dda427.0407161953.665181ce@posting.google.com>`

```
spinoza1111@yahoo.com (Edward G. Nilges) wrote:

>Without structuralism there is no making sense, for example, of the
>fact that Plato explicitly derides the very idea of a comprehensive
>encyclopedia or manual while he relied during his lifetime on writing.
>Human behavior being constantly self-reflexive is not going to "make
>sense" in any neat, technical or artifactual sense.

Your style is a beam of bright light in this often drab forum. Keep it up.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 7)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-17T17:50:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5dda427.0407171650.3d20d9e0@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <f5dda427.0407151840.11a6ef20@posting.google.com> <cd8kif$bb0$1@panix5.panix.com> <f5dda427.0407161953.665181ce@posting.google.com> <40f963bb.509406956@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote in message news:<40f963bb.509406956@news.optonline.net>...
> spinoza1111@yahoo.com (Edward G. Nilges) wrote:
> 
…[6 more quoted lines elided]…
> Your style is a beam of bright light in this often drab forum. Keep it up.

Thanks for your comment.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** shoppa@trailing-edge.com (Tim Shoppa)
- **Date:** 2004-07-17T18:01:43-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<bec993c8.0407171701.30295d55@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<cd5ij1$89o$1@panix5.panix.com>...
> In article <f5dda427.0407141855.29014ef9@posting.google.com>,
> Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[10 more quoted lines elided]…
> Now this is an interesting distinction... speech vs writing?

Writing about music is like dancing about architecture.

I'm not as critical as whoever originally said (wrote?) this, but it
has merit.  One form of expression can never completely replace another.
Photography didn't replace painting.  Telephones didn't replace 
direct speech.

Some of us still prefer the power of writing.  It's a lot easier
to xerox 100 copies of something than it is to repeat the same thing
100 times.  Although some corporate phone systems let you mass-deliver
voice messages.

Tim.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-17T22:25:56-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdcn3k$2n7$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <bec993c8.0407171701.30295d55@posting.google.com>`

```
In article <bec993c8.0407171701.30295d55@posting.google.com>,
Tim Shoppa <shoppa@trailing-edge.com> wrote:
>docdwarf@panix.com wrote in message news:<cd5ij1$89o$1@panix5.panix.com>...
>> In article <f5dda427.0407141855.29014ef9@posting.google.com>,
…[13 more quoted lines elided]…
>Writing about music is like dancing about architecture.

Not a bad beat to that line... are you going to set it to a tune?

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 5)_

- **From:** "Jack Peacock" <peacock@simconv.com>
- **Date:** 2004-07-18T14:41:43-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<HJ6dnZ6UmIwIc2fdRVn-vA@mpowercom.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <bec993c8.0407171701.30295d55@posting.google.com> <cdcn3k$2n7$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:cdcn3k$2n7$1@panix5.panix.com...
> >Writing about music is like dancing about architecture.
>
> Not a bad beat to that line... are you going to set it to a tune?
>
Dust off the ballroom floor, grab your partner and cue the piano player,
it's time for the Bauhaus Boogie...
  Jack Peacock
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-18T18:31:04-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<cdetn8$9u5$1@panix5.panix.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <bec993c8.0407171701.30295d55@posting.google.com> <cdcn3k$2n7$1@panix5.panix.com> <HJ6dnZ6UmIwIc2fdRVn-vA@mpowercom.net>`

```
In article <HJ6dnZ6UmIwIc2fdRVn-vA@mpowercom.net>,
Jack Peacock <peacock@simconv.com> wrote:
><docdwarf@panix.com> wrote in message news:cdcn3k$2n7$1@panix5.panix.com...
>> >Writing about music is like dancing about architecture.
…[4 more quoted lines elided]…
>it's time for the Bauhaus Boogie...

Truth be known... I lived in Newark, NJ for six years in a genuine Ludwig 
Mies van der Rohe 'cigarette pack school of design' Bauhaus; now I fear 
nothing.

DD
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** spinoza1111@yahoo.com (Edward G. Nilges)
- **Date:** 2004-07-18T00:37:40-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<f5dda427.0407172337.6955d203@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <cd5ij1$89o$1@panix5.panix.com> <bec993c8.0407171701.30295d55@posting.google.com>`

```
shoppa@trailing-edge.com (Tim Shoppa) wrote in message news:<bec993c8.0407171701.30295d55@posting.google.com>...
> docdwarf@panix.com wrote in message news:<cd5ij1$89o$1@panix5.panix.com>...
> > In article <f5dda427.0407141855.29014ef9@posting.google.com>,
…[23 more quoted lines elided]…
> voice messages.

This may confuse what Derrida means by "arche" writing. It appears to
me that walking from one person to the next and saying the same thing
would be for Derrida a form of arche-writing because I believe he
means by arche writing, that which is complementary to and complements
the deficiencies of speech.

Thus in preliterate cultures, the stories parents tell their children
are a form of arche-writing in that they preserve and pass along
important tribal information, likewise even the dance may perform the
same function.

For Derrida, any one specific named form of communication is NEITHER
writing nor speech until it becomes part of a "structural economy".
This is because as a post-structuralist, Derrida is aware that we
can't go around slapping labels on such universal activities as speech
and writing (using speech and writing to do so) without paradox, and
without those labels tending, in the actual manner of labels, to
becoming either gradually unstuck, or else written over with graffito.

But (and this is an all important "but", primarily because
irresponsible American academics get only to the apparent nihilism of
the end of the preceding paragraph) we still can in fact "do" both
literary criticism and philosophy (and for that matter program
computers, at least some of the time). This is because prior to
assigning names we can if we think hard enough recognize the systems
in which we are enmeshed by definition.

In this connection I am reminded of the anthropologist Gregory Bateson
who realized that quite ordinary men, United States war veterans who
were recovering alcoholics being treated in Palo Alto, could in fact
recognize the fact of being enmeshed in structures for which society
had given them no language to talk about.

In Bateson's work, which unfortunately and to my knowledge, has never
been linked at all to post-structuralism, these ordinary men through a
"spiritual" process in Alcholics Anonymous recognized how one could in
fact acquire a language for a system one could not stand outside. They
couldn't "recover" from alcoholism but instead stood inside alcoholism
and discoursed about it by narrating to each other their experiences,
and found a language which, while not allowing them to emerge from the
alcoholic "system" (structure) of alkie and bottle, did allow them to
more or less keep the system at arms length on a daily basis.

Likewise, I think Derrida is engaged in both living inside a system he
cannot think "outside" while at the same time needing to keep the
system from doing the thinking for him, just as Bateson's alkie needed
AA to provide him with a language other than "I think I will have a
shot, or two", language that was incommensurate to the reality, which
was having a shot, or two, and ending up two weeks later butt naked on
a street in Mexico City.

The sad results on this parallel of "addiction" to Platonism,
"addiction" to unconsciously prising speech over writing while
depending on the "lesser" term are usually neo-conservative and
neo-ethnocentric, in which the addict-philosopher constructs elaborate
defenses for a world view about which he isn't, in the end, serious.
> 
> Tim.
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Anne & Lynn Wheeler <lynn@garlic.com>
- **Date:** 2004-07-15T08:37:16-06:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<ud62xnxpf.fsf@mail.comcast.net>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com>`

```
spinoza1111@yahoo.com (Edward G. Nilges) writes:
> Be sure to learn Rexx, which is a language developed at IBM UK in the
> early 1980s by Mike Cowlishaw. Originally intended as a way to write
> procedures on Conversational Monitor System, REXX is now also used on
> MVS and Time Squandering Option (TSO).


some old rexx threads:
http://www.garlic.com/~lynn/94.html#11 REXX
http://www.garlic.com/~lynn/2000b.html#29 20th March 2000
http://www.garlic.com/~lynn/2000b.html#30 20th March 2000
http://www.garlic.com/~lynn/2000b.html#31 20th March 2000
http://www.garlic.com/~lynn/2000b.html#32 20th March 2000
http://www.garlic.com/~lynn/2000b.html#33 20th March 2000
http://www.garlic.com/~lynn/2002g.html#57 Amiga Rexx
http://www.garlic.com/~lynn/2002g.html#58 Amiga Rexx
http://www.garlic.com/~lynn/2002g.html#59 Amiga Rexx
http://www.garlic.com/~lynn/2002g.html#60 Amiga Rexx
http://www.garlic.com/~lynn/2004d.html#17 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#19 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#20 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#21 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#26 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#41 REXX still going strong after 25 years
http://www.garlic.com/~lynn/2004d.html#42 REXX still going strong after 25 years
```

##### ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** Morten Reistad <firstname@lastname.pr1v.n0>
- **Date:** 2004-08-03T19:07:03+02:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<nngoec.65f2.ln@via.reistad.priv.no>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com>`

```
In article <f5dda427.0407141855.29014ef9@posting.google.com>,
Edward G. Nilges <spinoza1111@yahoo.com> wrote:
>rsteiner@visi.com (Richard Steiner) wrote in message news:<vfs8ApHpvioW092yn@visi.com>...
>> Hi, guys...
…[4 more quoted lines elided]…
>> there is in IBMland.

It is of course perfectly viable to download hercules and some
of the IBM systems they allow for personal use, and have a go. 

>Many companies and other institutions talk a good game about getting
>rid of their mainframes and their inventory of Cobol programs, because
…[3 more quoted lines elided]…
>dishonest" writing.

I am in the process of doing a web-style application, and I am
struck by how much this resembles the mainframe way.

  MySql looks a lot like old-style DB2, around 1987 or so.
  Apache/PHP/cgi looks a lot like cics/vtam.
  Forms interactions look a lot like 3270 streams.

I use a lot of the old Cics/db2 tricks, and the applications
fly. 

Then it is very odd to hear how the users love web-systems and
hate 3270 systems; not knowing how much they resemble each other.

>This bifurcation pervades technical and media discourse...to the
>extent that in the celebrations of the "heroes" of September 11 one
…[9 more quoted lines elided]…
>granted and as such cannot be named or celebrated.

It's those media people. They need to have an angle to everything, 
"personal touch" or what have you. Straight, honest reporting has
been out for decades. 

>[Parenthetically we find a similar economy in Grigorii Medvedev's
>account of Chernobyl: the Russian firefighters are celebrated, but the
…[19 more quoted lines elided]…
>MVS and Time Squandering Option (TSO).

There are so amazing amounts of business logic present in all the
mainframe stuff that it will provide safe employment for mainframe
people for decades; even if they are indeed scrapping the stuff.
In which case they will need to reimplement it somewhere else. 

>Rexx is based on PL/I and as such has a reasonably up to date syntax.
>Its semantics is based on the traditional IBM MIS idea (which I think
…[5 more quoted lines elided]…
>mainframe.

It also exists in other environments.

>> No, this isn't a surprise to me.  :-)
>> 
…[13 more quoted lines elided]…
>> which is no longer a realistic desire?

The people from the big mainframe boom of 1964-1975 are moving into
retirement in large numbers now. But the big iron is still with us. 

>> Am I crazy for even being interested?
>> 
>> Is there a better newsgroup to ask this?  Maybe I'll also fork this to
>> a.f.c (since I know a lot of former IBMers post there as well).

Now, you must get used to getting a weekly haircut, and a tie and ...

(only kidding).

-- mrr
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-08-03T18:16:44-05:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<czBEBpHpvufZ092yn@visi.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no>`

```
Here in alt.folklore.computers,
Morten Reistad <firstname@lastname.pr1v.n0> spake unto us, saying:

>>rsteiner@visi.com (Richard Steiner) wrote in message news:<vfs8ApHpvioW092yn@visi.com>...
>>> 
…[6 more quoted lines elided]…
>of the IBM systems they allow for personal use, and have a go.

What is Hercules?   An IBM mainframe emulator of sorts?

I already have a decade of experience in TSO/ISPF, at least using a
limited subset of utilities and editors.  I just haven't written code
in that particular environment.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** ignatios@theory.cs.uni-bonn.de (Ignatios Souvatzis)
- **Date:** 2004-08-04T10:26:42+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<ceqdl2$s0k$1@f1node01.rhrz.uni-bonn.de>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no> <czBEBpHpvufZ092yn@visi.com>`

```
Richard Steiner writes:

> What is Hercules?   An IBM mainframe emulator of sorts?

Exactly. Runs some Unices and, I have seen claimed, on Windows.

	-is
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 5)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-06T17:56:41-04:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<joe_zitzelberger-0FFCD7.17564106082004@knology.usenetserver.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no> <czBEBpHpvufZ092yn@visi.com> <ceqdl2$s0k$1@f1node01.rhrz.uni-bonn.de>`

```
In article <ceqdl2$s0k$1@f1node01.rhrz.uni-bonn.de>,
 ignatios@theory.cs.uni-bonn.de (Ignatios Souvatzis) wrote:

> Richard Steiner writes:
> 
…[4 more quoted lines elided]…
> 	-is

Any poxix environment.  Various unices, windoze, macos and z/Linux...
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** T��� Rowan <reynirhs@mi.is>
- **Date:** 2004-08-04T05:25:18+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<anq0h0h6acpestv4t8pe08l0k5a7j64ibs@4ax.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no>`

```
Saith Morten Reistad:

>In article <f5dda427.0407141855.29014ef9@posting.google.com>,
>Edward G. Nilges <spinoza1111@yahoo.com> wrote:
…[3 more quoted lines elided]…
>It also exists in other environments.

Didn't the Amiga always have ARexx? Plus, there's Regina (and probably
some other Rexx interpreters) for Linux et al.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

_(reply depth: 4)_

- **From:** "Charlie Gibbs" <cgibbs@kltpzyxm.invalid>
- **Date:** 2004-08-04T09:42:11-08:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<601.712T573T5820929@kltpzyxm.invalid>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no> <anq0h0h6acpestv4t8pe08l0k5a7j64ibs@4ax.com>`

```
In article <anq0h0h6acpestv4t8pe08l0k5a7j64ibs@4ax.com>, reynirhs@mi.is
(T� Rowan) writes:

>Didn't the Amiga always have ARexx?

Well, not always.  Certainly not before release 2.0 of AmigaOS.
But it was eventually included as part of the standard release,
and many programs (including Thor, the newsreader I'm using to
write this) include ARexx ports.
```

###### ↳ ↳ ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** jmfbahciv@aol.com
- **Date:** 2004-08-04T09:19:51+00:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<4110bbdf$0$2815$61fed72c@news.rcn.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com> <f5dda427.0407141855.29014ef9@posting.google.com> <nngoec.65f2.ln@via.reistad.priv.no>`

```
In article <nngoec.65f2.ln@via.reistad.priv.no>,
   Morten Reistad <firstname@lastname.pr1v.n0> wrote:
<snip kooky stuff>

>>> Am I crazy for even being interested?
>>> 
…[5 more quoted lines elided]…
>(only kidding).

You forgot the starch.

/BAH

Subtract a hundred and four for e-mail.
```

#### ↳ Re: Possibly stupid question for you IBM mainframers... :-)

- **From:** hancock4@bbs.cpcn.com (Jeff nor Lisa)
- **Date:** 2004-07-15T11:05:14-07:00
- **Newsgroups:** comp.lang.cobol,alt.folklore.computers
- **Message-ID:** `<de64863b.0407151005.7f8e760e@posting.google.com>`
- **References:** `<vfs8ApHpvioW092yn@visi.com>`

```
rsteiner@visi.com (Richard Steiner) wrote 

> My question, though: How does a person like me go about learning more
> about CICS, COBOL2, DB2, etc., on the IBM side...?

COBOL to COBOL2 is no big deal; IBM has manuals on its website
including IIRC a conversion guide.

CICS is not so easy.

A lot depends on what a potential employer is doing.  Some have
very complex networks using high-end CICS components that require
skill and experience to make work properly, efficiently and reliably.
Others have simple systems using more basic components.

As others have mentioned, sometimes the screening process is rather
imperfect

Another issue is what the IBM mainframe job market is in your
area.  If employers are looking for people, they won't be as fussy
and allow you to get up to speed on their time.  But if the market
is tight they'll be more picky.

In my area the mainframe market, indeed the overall IT market,
is rather bad.  I know several smart and hard working experience
former consultants who just can't find anything and were forced
to move on to other fields.  From news reports it seems this is
widespread.

Another possibility is to seek more of a systems analysis position
that isn't as hardware dependent.


I would also see how your local job market is in more modern IT
stuff like Oracle, Java, web development, MS-Office support, etc.
If there is a market, it may be better to get training in those
fields.  In my area, many community colleges offer night courses
in such subjects, but not in mainframe stuff.


An alternative market might be as a substitute teacher, or perhaps
a regular teacher, again depending on how hard they are up for 
teachers and how much certification they require up front or down
the road.  One big city allows you to get the certification within
a year or so after getting hired.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
