[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 2002 for the AS/400

_8 messages · 5 participants · 2002-01_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`AS/400, iSeries, RPG`](../topics.md#as400)

---

### COBOL 2002 for the AS/400

- **From:** david.silber@hpdsoftware.com (David Silber)
- **Date:** 2002-01-17T05:44:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad85f189.0201170544.2765ec91@posting.google.com>`

```
At the end of November 2001, IBM applications development people in
Toronto were unable to confirm that they would support the forthcoming
COBOL 2002 standard (acc. to an email sent to me by the UK AS/400
(i-Series) Programme Manager. Has anyone heard anything different?
While other vendors like Micro Focus have been very active, it would
appear that IBM have been sitting on their hands. I would suggest an
intensive lobbying effort by those concerned.
```

#### ↳ Re: COBOL 2002 for the AS/400

- **From:** Fred Snyder <fred_snyder@hotmail.com>
- **Date:** 2002-01-17T09:28:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C46DF7A.5332C629@hotmail.com>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com>`

```
I'll start my response with IMHO!! I doubt IBM or any other major (those
that are left) hardware vendor is inclined to put the money into a new
COBOL standard at this point. Had the new standard come out when it was
supposed to in 1997 it would have had a better chance of being accepted by
the IBM's of the world. With new development platforms such as Java and
C++ changing almost weekly its hard for a major vendor to put people and
money into something that only changes every 11 years or so. Companies
like Micro Focus have the talent and committment to be able to add
extensions to the language as they have done over the past 25 years.
Should you stay in a client/server environment where you use compilers
such as Micro Focus then you will be able to take advantage of the new
features but I don't think you'll ever see them running on the mainframe.
This is in no means a dig at the standards committee, they do great work
but are not organized in a way to be able to respond to a changing
development environment.

David Silber wrote:

> At the end of November 2001, IBM applications development people in
> Toronto were unable to confirm that they would support the forthcoming
…[4 more quoted lines elided]…
> intensive lobbying effort by those concerned.
```

#### ↳ Re: COBOL 2002 for the AS/400

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-18T11:08:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a29l46$lo3$1@slb3.atl.mindspring.net>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com>`

```
IBM has made *no* comment concern a "statement of direction" for *any*
platform - including OS/390 (z/OS) where COBOL is still one of their "major"
application products.

HOWEVER, be careful in reading this.  I did say they have made NO statement
and that means they have not made any statement PRO or CON for supporting
the next Standard.

They have (several years ago) indicated that they would NOT implement the
various "iterations" of the draft Standard as:

 A) it was constantly changing - so anything they provided one year, would
be incompatible with what would come out the next year (and therefore cause
their customers migration problems)

 B) there were/are parts of the draft that were changing from "required" to
"processor dependent" and they did NOT intend on implementing some features
that ended up as "processor dependent" where their customers would NOT want
to use the features (e.g. character-based screen handling and
file-sharing/record locking)

C) They were (and ARE concentrating) on those features/functions (in and OUT
of the draft Standard) that THEIR customers have expressed a serious
"demand" for (e.g. improved performance for binary items, XML support, and
Java interoperability, and on OS/400 "locale" support)

  ***

As far as I know, *ONLY* Micro Focus has made a "public statement" that
their NEXT release will conform to the draft (final?) Standard.  I believe
that Fujitsu has indicated that they are staying RELATIVELY current with the
developments of the draft - but usually new features/functionality comes out
in the Japanese products about 6-12 months before it reaches the "US"
product.  Just this week they came out with the MS "NET" product (in beta)
so it seems that has been where the MAJORITY of their development as been.
(Actually, as far as I can tell from "externals" the Siemens portion of
Fujitsu is staying "closer" to the draft Standard than the PC portion.)

   ***

You are correct that *IF* Standard conformance is IMPORTANT to you (your
company), that you should communicate this to IBM.   I believe the "normal"
path for OS/400 people is thru "COMMON" (while the normal path for z/OS
customers would be SHARE).

Do a REQUIREMENT and see how many shops actually agree with you that this
should be done.  IBM will listen - but (IMHO) they won't necessarily do a
lot based on "theory" rather than paying customers' needs/desires.
```

##### ↳ ↳ Re: COBOL 2002 for the AS/400

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-19T07:13:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C491CA3.CF16D692@Azonic.co.nz>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com> <a29l46$lo3$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> IBM has made *no* comment concern a "statement of direction" for *any*
> platform - including OS/390 (z/OS) where COBOL is still one of their "major"
> application products.

> that ended up as "processor dependent" where their customers would NOT want
> to use the features (e.g. character-based screen handling and
> file-sharing/record locking)

While this may be true for OS/390 it is not the only IBM system.  Linux
will run on most IBM hardware and would require both character screen
based (for console/telnet) and file share/locking.  Given that IBM is
pushing Linux then a new Visual-Age Cobol for Linux would be useful.
```

###### ↳ ↳ ↳ Re: COBOL 2002 for the AS/400

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-18T13:31:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a29vet$qdd$1@slb6.atl.mindspring.net>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com> <a29l46$lo3$1@slb3.atl.mindspring.net> <3C491CA3.CF16D692@Azonic.co.nz>`

```
If you think those would be useful in those environments *and* you are a
current IBM (paying) customer for those products, then I *strongly*
recommend that you use "normal" IBM enhancement request (requirement)
procedures for communicating this to IBM.

IBM *does* listen to PAYING customers; they do NOT (normally) implement
feature "just because someone thinks they MIGHT be useful - someday)

NOTE: I am *not* disagreeing (necessarily) with your perception - I am only
saying that without user input to request these features (in those
environments) that you should NOT expect IBM to provide them (even IF they
do provide a "fully conforming" 2002 compiler).
```

###### ↳ ↳ ↳ Re: COBOL 2002 for the AS/400

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T15:48:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4AE6C1.33C50D2F@Azonic.co.nz>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com> <a29l46$lo3$1@slb3.atl.mindspring.net> <3C491CA3.CF16D692@Azonic.co.nz> <a29vet$qdd$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> If you think those would be useful in those environments *and* you are a
> current IBM (paying) customer for those products, 

No, I am not a 'current paying customer for those products' because
there is no product 'IBM Cobol for Linux' (that was the point of the
message).

If they were to release such a product as VisualAge Cobol for Linux then
I may well become a paying customer for it.  However, I would only do so
if it had console ACCEPT/DISPLAY (preferably X/Open) and file
sharing/locking, even if mainframers don't see the point.
```

###### ↳ ↳ ↳ Re: COBOL 2002 for the AS/400

_(reply depth: 5)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-01-20T03:29:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-CWj3ytH1cu50@thishost>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com> <a29l46$lo3$1@slb3.atl.mindspring.net> <3C491CA3.CF16D692@Azonic.co.nz> <a29vet$qdd$1@slb6.atl.mindspring.net> <3C4AE6C1.33C50D2F@Azonic.co.nz>`

```
On Sun, 20 Jan 2002 15:48:17 UTC, Richard Plinston 
<riplin@Azonic.co.nz> wrote:

> William M. Klein wrote:
> > 
…[10 more quoted lines elided]…
> sharing/locking, even if mainframers don't see the point.

I'll second that, a Visualage COBOL for Linux would be something very 
good to have.
```

###### ↳ ↳ ↳ Re: COBOL 2002 for the AS/400

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-20T19:22:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2fqga$dpf$1@slb7.atl.mindspring.net>`
- **References:** `<ad85f189.0201170544.2765ec91@posting.google.com> <a29l46$lo3$1@slb3.atl.mindspring.net> <3C491CA3.CF16D692@Azonic.co.nz> <a29vet$qdd$1@slb6.atl.mindspring.net> <3C4AE6C1.33C50D2F@Azonic.co.nz>`

```
Please note that *both* the Accept/Display *and* the
File-sharing/record-locking support in the 2002 Standard are NOT identical
to that in the last (before it became "defunct") X/Open COBOL specification.
Therefore, I think that for *new* products, it is HIGHLY likely that when
you do see these facilities, they will probably match the ANSI/ISO Standard
and not the X/Open definition.  My guess is that vendors that currently
provide the X/Open support will continue to provide it (at least for a
while) as an OPTION, but not necessarily their "preferred" support.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
