[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SELECT ... ASSIGN TO UT-S-XXXX.

_14 messages · 8 participants · 2001-10_

---

### SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** dimbriale@bear.com (Don Imbriale)
- **Date:** 2001-10-05T12:35:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<340ff33e.0110051135.2f19a38c@posting.google.com>`

```
IBM mainframe COBOL: In the ASSIGN clause on a SELECT statement under
FILE-CONTROL. in the INPUT-OUTPUT SECTION., is there any significance
to the "UT-"?  What about the "S-"?  It seems that any values are
accepted by the compiler.  Do they affect processing?  Are they
needed?
```

#### ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-05T15:15:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pl4gu$bno$1@slb7.atl.mindspring.net>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com>`

```
Assuming an OS/390, z/OS, or VM environment, see
  http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igylr205/4.2.3.1
for what is and is not "meaningful" in currently supported IBM mainframe
compilers.

I believe that VSE still "parses" some of the other prefixes. (Let me know
if  you need me to find the online references for that)

OLDER COBOL's used the "stuff before the DDName" for a LOT more information
than the current compilers/run-times do.  If you are supporting older
(DOS/VS COBOL, OS/VS COBOL, or even ANS COBOL) applications, then you will
need to find the HARDCOPY versions of those manuals for all the "gruesome"
details.
```

##### ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-06T11:25:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bbe425b_3@news.newsgroups.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net>`

```
The "UT" stands for "Utility" which translates as "disk" (the general
workhorse medium of IBM Mainframes).

The "S" means "Sequential", so the ASSIGN is telling the compiler that this
will be a sequential disk file which can be allocated anywhere on available
disk storage.

Like Bill said, it applies more to the "old days" and is probably not so
relevant or necessary now...

As COBOL moves further away from its original simplicity, it is pretty
difficult to keep up with what is relevant. Fortunately, we have guys like
Bill in the NG who DO keep up with it...<G>

For myself (and a number of others who have written to me), I just write it
and if it doesn't work, THEN I investigate it...

This is an easier strategy than concerning myself with the details of what
is in every COBOL Standard (real or imagined, implemented or
"forthcoming"...), which MIGHT  (or might not) be implemented by the
particular vendor whose platform I am looking at.

To be fair, it is many years now since I wrote IBM COBOL Mainframe code.

Pete.
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9pl4gu$bno$1@slb7.atl.mindspring.net...
> Assuming an OS/390, z/OS, or VM environment, see
>   http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igylr205/4.2.3.1
…[6 more quoted lines elided]…
> OLDER COBOL's used the "stuff before the DDName" for a LOT more
information
> than the current compilers/run-times do.  If you are supporting older
> (DOS/VS COBOL, OS/VS COBOL, or even ANS COBOL) applications, then you will
…[14 more quoted lines elided]…
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-10-06T12:26:32+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net> <3bbe425b_3@news.newsgroups.com>`

```
On Sat, 6 Oct 2001 11:25:34 +1200, Peter E. C. Dashwood wrote:

>The "UT" stands for "Utility" which translates as "disk" (the general
>workhorse medium of IBM Mainframes).

??? I remember using UT for tape device, DA for disk and UR for printers.

I always believed that the stand for Unit Tape, Direct Access and Unit Record
(but of course I could be wrong)





Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

_(reply depth: 4)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-10-06T14:12:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<njEv7.233$uY1.91726905@newssvr15.news.prodigy.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net> <3bbe425b_3@news.newsgroups.com> <jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE>`

```
    It's been a lot of years, but that's the way I remember it, too.  The
(U)nit (R)ecord devices were card reader and card punch in addition to
printer.
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-06T12:20:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381FA20C848F1E3E.FB96FBC9B4E9272D.B193014E17499D58@lp.airnews.net>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net> <3bbe425b_3@news.newsgroups.com> <jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE>`

```
On Sat, 06 Oct 2001 12:26:32 +0200 (CDT), "Willem Clements"
<willem@horizontes-informatica.com> enlightened us:

>On Sat, 6 Oct 2001 11:25:34 +1200, Peter E. C. Dashwood wrote:
>
…[16 more quoted lines elided]…
>

From my very old "Fundamentals of COBOL Programming" by Carl Feingold,
the Class Indicator can be and have the following meanings:

UR = Unit Record - card reader, card punch, printer

UT = Utility - Tape or Disk or Drum or Cell (note:  if UT and Disk or
Tape, organization must be S)

DA = Direct Access - Disk, Drum or Cell (note:  organization indicator
must be I or D).

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I don't do drugs anymore 'cause I find I get the 
same effect just by standing up really fast.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-08T11:17:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc0d7b8_8@news.newsgroups.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net> <3bbe425b_3@news.newsgroups.com> <jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE> <381FA20C848F1E3E.FB96FBC9B4E9272D.B193014E17499D58@lp.airnews.net>`

```

"SkippyPB" <swiegand@nospam.neo.rr.com> wrote in message
news:381FA20C848F1E3E.FB96FBC9B4E9272D.B193014E17499D58@lp.airnews.net...
> On Sat, 06 Oct 2001 12:26:32 +0200 (CDT), "Willem Clements"
> <willem@horizontes-informatica.com> enlightened us:
…[12 more quoted lines elided]…
>

Thanks Steve.

I posted my response to Willem before I saw this, but it bears out exactly
what I remember.

Pete.




-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-08T11:14:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc0d429_7@news.newsgroups.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <9pl4gu$bno$1@slb7.atl.mindspring.net> <3bbe425b_3@news.newsgroups.com> <jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE>`

```
Before there were disk drives, tapes were "utility devices".

I remember programming under TOS (Tape Operating System) and it used to be
real fun to watch the SYSRES tape loading logical transients...

When the first 360s became available we used to run them at night with all
the lights out...

Watching the console lights and the tape selector lights on the tape drives
was a VERY spooky experience. Protected tapes had a red light, tapes being
written had a green light and when a drive was selected it had a yellow
(white) light. As the program progressed these lights would dance along the
tape drives.

The SYSRES tape was nearly ALWAYS "busy" and it used to be housed on a drive
which could read forward and backwards so it could be passed faster (not ALL
Tape drives had this capability; it cost extra).

The concept of a UTILITY device changed when the first 2311s arrived, but
COBOL supported either tape or disk as Utility.

The "DA" was for "Direct Access" and that meant "non-sequential" and
therefore could NOT be a UTILITY device.

The "UR" meant "Unit Record" which really meant "unblocked" (early printers
and punch card readers/punches accepted a single "record"). It was only
later when we started spooling print to disk that print files became
"blocked", but COBOL still allowed them to be treated as "unit record" (as
it does to this day...).

Ah, happy times...<G>

Pete.

"Willem Clements" <willem@horizontes-informatica.com> wrote in message
news:jvyyrzubevmbagrfvasbezngvpnpbz.gkslo80.pminews@News.CIS.DFN.DE...
> On Sat, 6 Oct 2001 11:25:34 +1200, Peter E. C. Dashwood wrote:
>
…[5 more quoted lines elided]…
> I always believed that the stand for Unit Tape, Direct Access and Unit
Record
> (but of course I could be wrong)
>
…[9 more quoted lines elided]…
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

#### ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-08T14:59:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9psetm$95j$1@peabody.colorado.edu>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com>`

```

On  5-Oct-2001, dimbriale@bear.com (Don Imbriale) wrote:

> IBM mainframe COBOL: In the ASSIGN clause on a SELECT statement under
> FILE-CONTROL. in the INPUT-OUTPUT SECTION., is there any significance
> to the "UT-"?  What about the "S-"?  It seems that any values are
> accepted by the compiler.  Do they affect processing?  Are they
> needed?


They used to be required, and still are accepted.  I don't use them anymore.
```

#### ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** dimbriale@bear.com (Don Imbriale)
- **Date:** 2001-10-08T14:51:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<340ff33e.0110081351.733aa307@posting.google.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com>`

```
dimbriale@bear.com (Don Imbriale) wrote in message news:<340ff33e.0110051135.2f19a38c@posting.google.com>...
> IBM mainframe COBOL: In the ASSIGN clause on a SELECT statement under
> FILE-CONTROL. in the INPUT-OUTPUT SECTION., is there any significance
> to the "UT-"?  What about the "S-"?  It seems that any values are
> accepted by the compiler.  Do they affect processing?  Are they
> needed?

Thanks for all the responses.  From the COBOL Language Reference
manual:

"label-
    Documents the device and device class to which a file is assigned.
 If
    specified, it must end with a hyphen.

S-
    For QSAM files, the S- (organization) field can be omitted.

AS-
    For VSAM sequential files, the AS- (organization) field must be
    specified.

    For VSAM indexed and relative files, the organization field must
be
    omitted.

The syntax diagram shows that both are optional.  Empirical testing
reveals that any characters are acceptable for the 'label'.
```

##### ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-08T17:12:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pt8ef$ij7$1@nntp9.atl.mindspring.net>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <340ff33e.0110081351.733aa307@posting.google.com>`

```
FYI -
  I have gone thru my "historical" manuals and have found in
    GC28-6396-5
        which is the LRM for "IBM OS Full American National Standard COBOL"
aka ANS V4

that the "last" IBM mainframe compiler to actually "use" this field was ANS
COBOL V3.  From ANS V4 on (including OS/VS COBOL, VS COBOL II, AD/Cycle SAA
COBOL/370, IBM COBOL for MVS & VM, and IBM COBOL for OS/390 & VM) this has
been treated as totally a "documentary" field.  (I am still not positive if
all the VSE compiler also "ignore" it.)

In the older compiler (ANS COBOL V3 and earlier) there were a BUNCH of
fields that had meaning.  Some of these are discussed in the "no longer
supported" section of the current Migration Guide - see
  http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igymg202/4.1.5?

and see the sections on
  "ASSIGN TO integer system-name"
    and
  "ASSIGN ... FOR MULTIPLE REEL/UNIT"

The ANS COBOL V4 LRM does "confirm" that when IBM last supported
"meaningful" entries in this field - that it only supported the three values
(already discussed in this thread) of
   DA (mass storage)
   UT (utility)
   UR (unit-record)
        - (The parenthetical are what page 74 of that manual calls them)

If anyone REALLY needs/wants the gruesome details on this, I probably could
scan the 3 pages talking about the ASSIGN clause in that manual.  However, I
assume that as this field has been treated as "documentary ONLY" for a
couple of decades now, that this probably isn't useful.  Please send me
PRIMATE email, if you need/want those pages.
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-09T11:42:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc22cc2_4@news.newsgroups.com>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <340ff33e.0110081351.733aa307@posting.google.com> <9pt8ef$ij7$1@nntp9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9pt8ef$ij7$1@nntp9.atl.mindspring.net...

> Please send me
> PRIMATE email, if you need/want those pages.
>
 Proof again (if proof were needed...) that you really are a monkey,
Bill...<G>

Pete.




-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

- **From:** JAndersen@screenio.com (John Andersen)
- **Date:** 2001-10-08T22:53:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc22db6.601760529@192.168.2.2>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <340ff33e.0110081351.733aa307@posting.google.com> <9pt8ef$ij7$1@nntp9.atl.mindspring.net>`

```
On Mon, 8 Oct 2001 17:12:37 -0500, "William M. Klein" <wmklein@nospam.ix.netcom.com>
wrote:

 >Please send me
 >PRIMATE email, if you need/want those pages.

Amy specific class of primate Bill?
Will the postman qualify, or were you looking
for something somewhat more simian?

;-)

John Andersen
NORCOM
http://www.SCREENIO.com/
Juneau, Alaska
```

###### ↳ ↳ ↳ Re: SELECT ... ASSIGN TO UT-S-XXXX.

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-08T18:21:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ptcft$fip$1@slb3.atl.mindspring.net>`
- **References:** `<340ff33e.0110051135.2f19a38c@posting.google.com> <340ff33e.0110081351.733aa307@posting.google.com> <9pt8ef$ij7$1@nntp9.atl.mindspring.net> <3bc22db6.601760529@192.168.2.2>`

```
<G> sorry about that

Actually, that manual is SO OLD that you may need to find a "proto-primate"
to care about it.  Or maybe, it is the old "if an infinite number of
primates send me mail, then one of them will care about this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
