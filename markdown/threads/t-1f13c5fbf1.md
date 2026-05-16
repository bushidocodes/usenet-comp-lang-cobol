[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Loadlib member dates in TSO/ISPF?

_14 messages · 11 participants · 1998-09 → 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Loadlib member dates in TSO/ISPF?

- **From:** gcooper@imf.org
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** COMP.LANG.COBOL
- **Message-ID:** `<6uquqj$c0b$2@nnrp1.dejanews.com>`

```
Does anyone have a way to list members of a loadlib and
their creation dates?  This is a question specific to a
TSO mainframe environment with OS 390, VS COBOL & TSO/ISPF.

I have a large number of members to check out.  I could
browse each member manually, but if there is a better way
I'm all ears.



-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ur580$icv$1@callisto.clark.net>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com>`

```
In article <6uquqj$c0b$2@nnrp1.dejanews.com>,  <gcooper@imf.org> wrote:
>Does anyone have a way to list members of a loadlib and
>their creation dates?  This is a question specific to a
…[4 more quoted lines elided]…
>I'm all ears.

IEHLIST, I believe.

DD
```

##### ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611223b$5$tfs$mr2ice@news>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com> <6ur580$icv$1@callisto.clark.net>`

```
In <6ur580$icv$1@callisto.clark.net>, on 29 Sep 1998 at 17:26,
docdwarf@clark.net () said:

>In article <6uquqj$c0b$2@nnrp1.dejanews.com>,  <gcooper@imf.org> wrote:
>>Does anyone have a way to list members of a loadlib and
…[5 more quoted lines elided]…
>>I'm all ears.

>IEHLIST, I believe.

The LISTIDR function of IEHLIST displays the compilation and link-edit
dates (julian).

Check if you havd the public-domain PDS command on your system (it may be
called PDS, or PDS83, PDS84 or PDS85).  PDS displays link-edit dates in
directory listings; its HISTORY command displays compiler codes, levels
and dates.

Gilbert Saint-flour <gsf@ibm.net>
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981005171953.06051.00002394@ngol03.aol.com>`
- **References:** `<3611223b$5$tfs$mr2ice@news>`

```

In article <3611223b$5$tfs$mr2ice@news>, Gilbert Saint-flour <gsf@ibm.net>
writes:

>>IEHLIST, I believe.
>
…[9 more quoted lines elided]…
>

Could someone please elucidate on this option?  I've been looking thru my
references on IEHLIST and find nothing about LISTIDR.  The only information
that appears in 3.4 (DataSet Utilities) relate to SIZE , TTR, AMode, RMode.
Is there any non-third party utility that provides information on LOADLIB
compile dates?
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

_(reply depth: 4)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3eS1.216$Ex.2291107@storm.twcol.com>`
- **References:** `<3611223b$5$tfs$mr2ice@news> <19981005171953.06051.00002394@ngol03.aol.com>`

```

>Could someone please elucidate on this option?  I've been looking thru my
>references on IEHLIST and find nothing about LISTIDR.  The only information
>that appears in 3.4 (DataSet Utilities) relate to SIZE , TTR, AMode, RMode.
>Is there any non-third party utility that provides information on LOADLIB
>compile dates?

>

Not sure if this will help...but I found this in the IBM manuals:
http://www2.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/DGT1U103/13%2e6?SHELF
=
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

_(reply depth: 5)_

- **From:** stevewie@apk.net (SkippyPB)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361e374d.6494860@news.apk.net>`
- **References:** `<3611223b$5$tfs$mr2ice@news> <19981005171953.06051.00002394@ngol03.aol.com> <d3eS1.216$Ex.2291107@storm.twcol.com>`

```
On Mon, 5 Oct 1998 21:06:11 -0400, "Jeff" <a@a.com> enlightened us:

>
>>Could someone please elucidate on this option?  I've been looking thru my
…[10 more quoted lines elided]…
>

According my Doug Lowe, "OS Utilities" book, IEHLIST has only the
following control statements:

LISTPDS
LISTVTOC
LISTCTLG

No mention of LISTDIR and no mention of its ability to report compile
dates.  Maybe someone was confused?

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
What happens if you get scared half to death twice?
 Steve
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

_(reply depth: 6)_

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361A6C70.F8E3CBE6@yahoo.com>`
- **References:** `<3611223b$5$tfs$mr2ice@news> <19981005171953.06051.00002394@ngol03.aol.com> <d3eS1.216$Ex.2291107@storm.twcol.com> <361e374d.6494860@news.apk.net>`

```
Well the Lowe book does state that there are 15 control ststements for IEHLIST
and that he only describes some of the most used ones.  An IBM JCL Utility manual
will describe them all.

SkippyPB wrote:

> On Mon, 5 Oct 1998 21:06:11 -0400, "Jeff" <a@a.com> enlightened us:
>
…[30 more quoted lines elided]…
>  Steve
```

##### ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** "Art Perry" <arthur.perry@eds88.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ur6mc$7r4$1@news.ses.cio.eds.com>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com> <6ur580$icv$1@callisto.clark.net>`

```
We have a utility called PDS Version 8.2  I'm not sure if this is widely
available or not, but it gives statistics on load library pds'.
```

#### ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36116874.310C@netbox.com>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com>`

```
gcooper@imf.org wrote:
> 
> Does anyone have a way to list members of a loadlib and
…[5 more quoted lines elided]…
> I'm all ears.

I'm not sure, as I'm at home, but FileAid MVS might have that facility.

Bob
```

##### ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** kthompson@netexas.net (Kevin)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F0BAE31457EEA923.C9488B42FD402E66.1ADEAF4975AFBD03@library-proxy.airnews.net>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com> <36116874.310C@netbox.com>`

```
On Tue, 29 Sep 1998 19:08:36 -0400, Bob Berman <bberman@netbox.com>
wrote:

>gcooper@imf.org wrote:
>> 
…[11 more quoted lines elided]…
>-- 
Yes, FileAid has a feature under the library function.  It let's you
map the load showing dates, rmode/amode, etc.

Cheers,
Kevin
```

#### ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611692B.3AA1@netbox.com>`
- **References:** `<6uquqj$c0b$2@nnrp1.dejanews.com>`

```
gcooper@imf.org wrote:
> 
> Does anyone have a way to list members of a loadlib and
…[5 more quoted lines elided]…
> I'm all ears.

A second thought, if you use Endevor to manage both source & load libs,
would be to browse the member list.  I'm sure there is a command to list
the members & their last update date.

Bob
```

##### ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980930170236.05667.00004344@ng112.aol.com>`
- **References:** `<3611692B.3AA1@netbox.com>`

```

gcooper@imf.org wrote:
>> Does anyone have a way to list members of a loadlib and their creation
dates?  This is a question specific to a TSO mainframe environment with OS 390,
VS COBOL & TSO/ISPF.
> >

It is possible that you need look no further than ISPF itself. The Utilities
Menu (which is option 3 in most shops), has a submenu option that allows you to
list the members of a PDS (usually function X), and you can send it to your
current .LIST dataset. When you do that hit PF1 to get an exact DSN.

It may be best to make this the only activity during the ISPF session you use
to go for the list So as to not get other distracting material in the .LIST
dataset.


After invoking the Utility procedure, exit ISPF with an option to save the
.LIST dataset. I would not necessarily print it the first time through this
exercise (that is, until you get accustom to the format, and decide if you like
it).

Instructing ISPF, upon exit, to save the dataset will induce the ISPF to also
leave the dataset alone the next time you enter, i.e. the next .LIST dataset
will have the next higher number. And the old .LIST dataset will be left around
indefinitely.

Re-enter ISPF.  For novices the quickest way may be to logoff and logon again.

You can now browse (or even edit) the older ISPF .LIST dataset.  You will find
that it has a formatted member listing of the PDS you asked  the Utility menu
to list. In some shops you will find that the .LIST dataset may have other
material in it that you were entirely unaware you were recording. So it is
good, in some cases, that you can indeed edit that prior .LIST dataset, to trim
it to just the report on the PDS you want.

After you have edited the dataset, you can print it, ... it already has
carriage control.  Generally that report is going to come out in alphabetical
order. There is probably a way to get ISPF to generate it in Date order
Ascending or Descending.  The report is fixed format so you can do alot of
interesting things to it with the SORT command from within ISPF edit.
(although your headings and carriage control will get disrupted if you sort it
in Edit).

Incidentally, STATS have to be on for the PDS dataset for this to work (or for
IEHLIST to work). I have seen ENDEVOR (mentioned by another poster)
environments, and other unique source code maintenance software, that defeats
STATS.  So it is useful to just inquire the PDS first before you pursue this.
If a Browse member list shows STATS you are okay. (Yes you can Browse a loadlib
PDS, It is very interesting).  

You will also notice sometimes that specific members are stat-less. That can
result from non-IBM software moving the members around, or from an 'advanced'
user of editors (such as ISPF itself) who has knowingly or unknowingly turned
STATS off for the most recent session with that member, that dataset, or for
all of their edit sessions.

It is a fact that you can not list the statistics if they are not there.
Recently, I saw a discussion of STATs apparently dissappearing when a shop
converted to OS/390.  But not really. They just genned the new OS with the less
favorable options, and as they converted individual datasets, the outbound
datasets had no stats, and the attribute was shut off for each PDS so created. 
They had to back track and reconvert.  All IBM OSes will faithfully generate
stats if the utility writing the dataset requests it (unless it is turned of at
the dataset level).

Best Wishes,
Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aoxS1.255$Ex.2826967@storm.twcol.com>`
- **References:** `<3611692B.3AA1@netbox.com> <19980930170236.05667.00004344@ng112.aol.com>`

```
>It is possible that you need look no further than ISPF itself. The
Utilities
>Menu (which is option 3 in most shops), has a submenu option that allows
you to
>list the members of a PDS (usually function X), and you can send it to your
>current .LIST dataset. When you do that hit PF1 to get an exact DSN.


Once you get the list of members on screen, type "SAVE MEMLIST" this should
save what is in the current dataset list to a flat file as I believe:
USERID.MEMLIST.DATASET.  I may be wrong about the extension. From the DSLIST
screen type HELP SAVE to find the specifics. This may have the info
mentioned above. All of the files matching the selection criteria on the
first DSLIST screen will be listed, not just what is on screen.
```

###### ↳ ↳ ↳ Re: Loadlib member dates in TSO/ISPF?

_(reply depth: 4)_

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981006211132.08202.00002834@ngol06.aol.com>`
- **References:** `<aoxS1.255$Ex.2826967@storm.twcol.com>`

```

In article <aoxS1.255$Ex.2826967@storm.twcol.com>, "Jeff" <a@a.com> writes:

>>It is possible that you need look no further than ISPF itself. The
>Utilities
…[14 more quoted lines elided]…
>

This does not provide the information requested as the request relates to the
Date Compiled as opposed to the Created or Changed Dates, NONE of which are
readily apparent when using 3.4 to browse a LOADLIB PDS.
So far I have only found manual processes that require physically browsing each
member for a search key which is different for each compiler(PL1, COBOL, ASM)
in use.

I'd like to find a programmatic means of getting the DATE/TIME Compiled of each
 member of a LOADLIB.   Would there be any help in getting to the end of this
solution?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
