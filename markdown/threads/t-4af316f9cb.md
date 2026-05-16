[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL II and Y2K (was Re: COBOL II Support Dates..was also C-A ....)

_4 messages · 3 participants · 1998-09_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Compilers and vendors`](../topics.md#compilers)

---

### VS COBOL II and Y2K (was Re: COBOL II Support Dates..was also C-A ....)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<6u9k6r$nmv@dfw-ixnews4.ix.netcom.com>`
- **References:** `<19980922003229.TZLE4499@39.chicago-05-10rs.il.dial-access.att.net> <3607E628.5B11@netvision.net.il>`

```
It was an earlier post of mine that made ERRONEOUS statements about VS COBOL
II and being "year 2000 compliant."  Since I made that post, I have gained a
little more "official" knowledge which this note hopes to impart.

Note: The following is true for VS COBOL II under MVS (or VM); for the
status under VSE, it is important to note that support has already ended
there.  This also applies only to Release 4.0 of VS COBOL II; all earlier
releases are already "dropped" as far as both marketing and support goes.

1) IBM does NOT talk (for any product) about "Year 2000 compliant" - they
only talk about "year 2000 ready" - and this has slightly different meanings
for hardware, software (products), and software (applications).  The
following is the definition for software products (which is where any COBOL
compiler fits),

"IBM uses the term "Year 2000 ready" to refer to products that meet the
following definition.  Specifically, "Year 2000 ready" means that "a
product, when used in accordance with its associated documentation, is
capable of correctly processing, providing and/or receiving date data within
and between the 20th and 21st centuries, provided that all products (for
example, hardware, software and firmware) used with the product properly
exchange accurate date data with it."

"IBM considers products not ready for Year 2000 if they don't meet the
definition set out above, or if they have not been tested.  Products not
affected by the Year 2000, such as hardware frames, keyboards, power
supplies, and hardware or software product publications are considered
ready."

  NOTE WELL: the previous definition includes "not tested means not ready".

2) When you use the IBM tool for determining VS COBOL II's (product
5668-958) readiness - you will receive the response
    NOT READY

(See www.ibm.com/2000 for accessing their Y2K evaluation database)

3) The only MVS or OS/390 COBOL products that get a "READY" status (and a
currently supported status) are
   IBM COBOL for MVS & VM - (5688-197)
   IBM COBOL for OS/390 & VM - (5648-A25)
   VA COBOL MLE FOR OS/390&VM - (5648-MLE)

(The last of these "sort-of" uses one of the previous 2)

4) Support for VS COBOL II is provided thru March 31, 2001.  This means that
it will continue to "function correctly" including handling of dates
(including leap day) as defined in the ANSI/ISO Standards for COBOL and in
the IBM LRM for this product.

5) Although IBM does NOT call VS COBOL II "Year 2000 ready", there are two
APARs out there that make it seem as close as you can get (for an "untested
and unsupported-as-Y2K-ready" product).

If you are running the VS COBOL II compiler with the VS COBOL II run-time
libraries, then

   APAR PN76666 provides a new software facility that allows you (the
application program) to call an IBM provided subroutine
    IGZEDT4
which provides the current date WITH a 4 digit year.

Note; APARs PN84080 and PN85139 provide ongoing run-time support for this
routine when you upgrade to the LE run-time library.

If you are running with the VS COBOL II compiler but with the LE run-time
library, then

  APAR PN79703 documents that it is legal (supported) to use the COBOL
dynamic CALL facility to obtain any of the date/time services provided by
the LE callable subroutines.  This means that such VS COBOL II programs can,
not only get 4-digit years, but can also get the full range of IBM supplied
"windowing" routines.

  NOTE: The IBM provided "millenium language extensions" which provide COBOL
native language support for "date windowing" are NOT available for VS COBOL
II.  All this APAR provides is access to the callable "windowing services"
from VS COBOL II.

   **********

Bottom-Line:

A) VS COBOL II is not (and will not) be labeled "Year 2000 ready"

B) VS COBOL II will be supported until the end of 1st quarter of 2001
(including the correct handling of dates - as defined in its language
reference manual)

C) Although the VS COBOL II product is not "year 2000 ready", via APARs you
can get the 4-digit year date under any run-time library and can get date
windowing when running VS COBOL II compiled programs with the LE run-time
library.

D) As stated in my original post, you really REALLY should be starting your
migration to one of the newer IBM COBOLs (probably IBM COBOL for OS/390 &
VM - and ideally with  MLE) now - and should not continue relying on VS
COBOL II.  VS COBOL II does NOT include support for

   - Millenium Language Extensions
   - The "CURRENT-DATE" intrinsic function (providing a 4-digit year)
   - ACCEPT from DAY or DATE getting a 4-digit year
```

#### ↳ Re: VS COBOL II and Y2K (was Re: COBOL II Support Dates..was also C-A ....)

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3609AE5D.4C7D@sprynet.com>`
- **References:** `<19980922003229.TZLE4499@39.chicago-05-10rs.il.dial-access.att.net> <3607E628.5B11@netvision.net.il> <6u9k6r$nmv@dfw-ixnews4.ix.netcom.com>`

```
Here is my question regardling Y2K "compliance."  (Well, some statements, and
maybe a questions.)  We have a lot of DOS/VS COBOL programs.  Specifically, an
ATM system that we purchased from an outside company.  This company has supplied
us with "patches" in order to become Y2K compliant.  Basically, most of the dates
they use are in Julian with a two digit year (ie 98123 is the 123rd day of 1998).
There are gazillions of date comparisions, not to mention many date fields
(six per record in one particular file).  What they've done is, when we read
in this record it now gets run through a subroutine to where the output (a
separate field) is the number of days since 1900.  This subroutine originally,
of course, concidered the year "10" to be 1910, etc., but it has been modified
so that the number 36525 is added to it if the year is less than 90.  So,
obviously it will only work for dates from 1990 to 2089.  Anyway, other dates
in the program are also converted to this "DAYS" format in order for the 
comparisons to work.

This is all done, of course, on a "non-Y2K-compiant" compiler.  My question I
guess is, why do we *need* to go to COBOL for VSE (we're a VSE shop) in order
to make our programs Y2K compliant?

Before you answer, realize that I personally hate using old-COBOL.  I intend to
convert all of these programs to COBOL II, and to then "convert" them to COBOL
for VSE whenever our systems programmers can get it working.  The problem is,
it *isn't* working yet, and we don't have time to wait for them to *get* it
working.  Even if they got it working today, we need to get the Y2K patches 
going ASAP in order to get testing going.  Don't say we still have a year for
that, because our internal deadline (or goal, I should say), is the end of this
year.  In a perfect world these programs would have been converted to COBOL II
years ago (most of our inhouse programs are--well, the CICS ones anyway, and many
of the batch ones).  But they aren't; so there you are.  As long as the code works
with the patches, do I have to beat myself over the head to convert them?  Even
if I do convert them, I don't know that we're going to start using the date
functions that handle four-digit years.  The program is *so* based on the 
two-digit years that it just doesn't seem worth it.

Still, I feel sorry for anyone who has to deal with the Y2.1K problem!  :-)
```

##### ↳ ↳ Re: VS COBOL II and Y2K (was Re: COBOL II Support Dates..was also C-A ....)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uc8rq$hme@dfw-ixnews8.ix.netcom.com>`
- **References:** `<19980922003229.TZLE4499@39.chicago-05-10rs.il.dial-access.att.net> <3607E628.5B11@netvision.net.il> <6u9k6r$nmv@dfw-ixnews4.ix.netcom.com> <3609AE5D.4C7D@sprynet.com>`

```

Frank Swarbrick wrote in message <3609AE5D.4C7D@sprynet.com>...

  <lots of snippage>
>   But they aren't; so there you are.  As long as the code works
>with the patches, do I have to beat myself over the head to convert them?
Even
>if I do convert them, I don't know that we're going to start using the date
>functions that handle four-digit years.  The program is *so* based on the
…[6 more quoted lines elided]…
>work: frank.swarbrick@1stbank.com

The problem with using DOS/VS COBOL (or VS COBOL II under VSE) for your Y2K
compliant program logic has to do with all the other systems that they
interface with.

FOR EXAMPLE,
  As you are a VSE shop, I am going to guess that you probably have some
CICS in your shop.  Are you aware that the "old" CICS won't even come up
after Jan 1, 2000?  Once you go to the new CICS (and I'll admit that I know
MVS better than VSE), the chances are that your "old" COBOL will have
problems with your "new" CICS. And when you are running DOS/VS COBOL or VS
COBOL II compiled programs, you are "unsupported".  (Well actually there are
some rules about supporting "existing" object code - IF you are using the
new LE run-time, but I'll bet you aren't doing that with your DOS/VS COBOL
programs).

This means that everything is fine - until it isn't!

In other words, running DOS/VS COBOL, VS COBOL II (under VSE), or any other
"unsupported" software will work just fine, until some day some other piece
of software or hardware "breaks" your existing applications - and you have
no one to turn to.  IBM is simply going to tell you to get on a "supported"
product and THEN they will help you resolve the problem with your existing
application working with the new hardware/software.

Does this help explain your problem?

P.S.  In case it got lost in the middle of this, IBM fully uspports
continued use of DOS/VS COBOL or VS COBOL II compiled programs when run with
LE/VSE.  However, such programs will NOT be "Y2K-compliant" - as far as IBM
is concerned.

P.P.S.  IBM had a known error in calculating that Feb 29, 2000 was a valid
leap day - when running with VS COBOL II under VSE.  Make certain that you
have the APAR applied to your products and that you test that out with your
"patched" application.
```

###### ↳ ↳ ↳ Re: VS COBOL II and Y2K (was Re: COBOL II Support Dates..was also C-A ....)

- **From:** higgish@dhfs.state.wi.us
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360A4B19.324A0B19@dhfs.state.wi.us>`
- **References:** `<19980922003229.TZLE4499@39.chicago-05-10rs.il.dial-access.att.net> <3607E628.5B11@netvision.net.il> <6u9k6r$nmv@dfw-ixnews4.ix.netcom.com> <3609AE5D.4C7D@sprynet.com> <6uc8rq$hme@dfw-ixnews8.ix.netcom.com>`

```




William M. Klein wrote:

> Frank Swarbrick wrote in message <3609AE5D.4C7D@sprynet.com>...
>
…[49 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
