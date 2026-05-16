[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initialize

_15 messages · 11 participants · 2005-09 → 2005-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Initialize

- **From:** "rockocubs" <rphipps@nospam.indy.rr.com>
- **Date:** 2005-09-27T14:05:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com>`

```
 Can someone settle an argument for me. Does a initialize on an 01 level
move spaces to pic x fields and zeroes to pic 9 fields or does it move
spaces to the whole 01 level?
```

#### ↳ Re: Initialize

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-27T11:16:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dhc266$1lic$1@si05.rsvl.unisys.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com>`

```
"When the statement is written without the REPLACING phrase, data items of
the categories alphabetic, alphanumeric and alphanumeric edited are set to
spaces; data items of category numeric and numeric edited are set to zeroes.
..."  (ANSI X3.23-1985 page VI-93, 6.17, The INITIALIZE statement, General
Rule 5.)

This doesn't address what your particular implementation actually DOES, but
it does address what the '85 standard says it OUGHT TO DO.

Note that index data items and elementary FILLER data items in the record
aren't affected by INITIALIZE at all, and note also that if an item has a
VALUE clause it isn't "re-applied" by INITIALIZE.

The 2002 standard adds "WITH FILLER" and "TO VALUE" syntax to INITIALIZE to
provide for these issues.

    -Chuck Stevens



"rockocubs" <rphipps@nospam.indy.rr.com> wrote in message
news:175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com...
> Can someone settle an argument for me. Does a initialize on an 01 level
> move spaces to pic x fields and zeroes to pic 9 fields or does it move
> spaces to the whole 01 level?
>
```

##### ↳ ↳ Re: Initialize

- **From:** "rockocubs" <rphipps@nospam.indy.rr.com>
- **Date:** 2005-09-27T14:37:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc266$1lic$1@si05.rsvl.unisys.com>`

```
 Thanks Chuck, 
  I haven't saw a cobol manual in years. I wonder if there is a new one
online somewhere. That way i could brush up have to take a Cobol test this
week for an interview, never had to do this before.
```

###### ↳ ↳ ↳ Re: Initialize

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-27T12:49:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dhc7lm$1omn$1@si05.rsvl.unisys.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc266$1lic$1@si05.rsvl.unisys.com> <b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com>`

```
You can (still) download a copy of the 1985 standard for $18.00 from the
ANSI eStandards Store at www.ansi.org.  The Intrinsic Function Amendment and
the Corrections Amendment are included in that price, and are also
downloadable independently at $18 per each.

You can also download the 2002 standard for the same price from the same
place.

From www.ansi.org, click on 'eStandards Store', key in "COBOL" in Search,
then GO.  Document "ANSI INCITS 23-1985 (R2001)" is the 1985 standard with
its amendments, and Document "INCITS /ISO/IEC 1989-2002" is the 2002
standard.

As far as individual vendor's reference manuals for COBOL, I can't answer
for any other companies, but the COBOL85 reference manuals for the Unisys
ClearPath Plus MCP-based systems are accessible without charge from
www.unisys.com.

The way I navigated from there to, say, the COBOL85 "basic implementation"
manual was:

    go to www.unisys.com
    click on "mainframes" under "products"
    click on "Libra Series" under ClearPath Plus MCP Servers
    click on "services and support"
    click on "Unisys Support Online"
    click on "Product Support" in the left column
    click on "documentation" in "Access documentation to learn about ..."
    type "86001518-307" in the "book number" field.

At this point a list of documents show up, in two categories: the manuals
themselves, and the documentation changes (D-notes) that will eventually be
applied to those manuals.  You're interested in the former, entitled "COBOL
ANSI-85 Programming Reference Manual, Volume 1:  Basic Implementation", in
the list.  Any one of the several that show up will do, but the last one in
the list (#7) has all the most recent D-Notes summarized at the beginning.

If you need to go back that far, COBOL74 Volume 1 (yes, we still actively
support it, though we are no longer adding feature content to it) is "book
number" 86000296-203".  Pick the last one on the list.

    -Chuck Stevens

"rockocubs" <rphipps@nospam.indy.rr.com> wrote in message
news:b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com...
> Thanks Chuck,
>   I haven't saw a cobol manual in years. I wonder if there is a new one
> online somewhere. That way i could brush up have to take a Cobol test this
> week for an interview, never had to do this before.
>
```

###### ↳ ↳ ↳ Re: Initialize

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-10-01T08:26:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f0N5xCPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com> <dhc7lm$1omn$1@si05.rsvl.unisys.com>`

```
.    On  27.09.05
  wrote  charles.stevens@unisys.com (Chuck Stevens)
     on  /COMP/LANG/COBOL
     in  dhc7lm$1omn$1@si05.rsvl.unisys.com
  about  Re: Initialize


CS> As far as individual vendor's reference manuals for COBOL, I can't
CS> answer for any other companies, but the COBOL85 reference manuals for
CS> the Unisys ClearPath Plus MCP-based systems are accessible without
CS> charge from www.unisys.com.

   The same applies to the OS/1100 (er, 2200) version.

   BTW, I always go directly to
   <http://public.support.unisys.com/os1/txt/web-verity?type=list>


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Als er am Kirchhofe vorbei ging, sagte er: Die da kï¿½nnen nun sicher sein, daï¿½ sie nicht mehr gehï¿½ngt werden, das kï¿½nnen wir nicht. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Initialize

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-09-27T17:53:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11jjjc0lsn2136a@news.supernews.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc266$1lic$1@si05.rsvl.unisys.com> <b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com>`

```
rockocubs wrote:
> Thanks Chuck,
>  I haven't saw a cobol manual in years. I wonder if there is a new one
> online somewhere. That way i could brush up have to take a Cobol test
> this week for an interview, never had to do this before.

See also:

http://www.netcobol.com/download/index.htm#2
```

###### ↳ ↳ ↳ Re: Initialize

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-28T16:21:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gqz_e.314813$on1.146886@clgrps13>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc266$1lic$1@si05.rsvl.unisys.com> <b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com>`

```

"rockocubs" <rphipps@nospam.indy.rr.com> wrote in message 
news:b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com...
> Thanks Chuck,
>  I haven't saw a cobol manual in years. I wonder if there is a new one
> online somewhere. That way i could brush up have to take a Cobol test this
> week for an interview, never had to do this before.


    I'm using the Liant RM/COBOL Language Reference Manual as my reference, 
which I got from http://www.liant.us/download/pdf/rmclrm75.pdf
```

###### ↳ ↳ ↳ Re: Initialize

- **From:** "Stephen Gennard" <Stephen.Gennard@a.email.host.without.spam.com>
- **Date:** 2005-09-28T20:43:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dhevon$nmf$1@hyperion.microfocus.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc266$1lic$1@si05.rsvl.unisys.com> <b1fab2eb9ff8664fa71b5f655e037c25@localhost.talkaboutprogramming.com>`

```
See also:

Mainframe Express 3.0 Enterprise Edition -
 http://support.microfocus.com/documentation/books/mx30/mx30indx.htm

Net Express 4.0 -
http://support.microfocus.com/documentation/books/nx40/nx40indx.htm

Server Express 4.0 SP1 -
http://support.microfocus.com/Documentation/books/sx40sp1/sx40indx.htm
```

#### ↳ Re: Initialize

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-27T11:18:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dhc2as$1lj2$1@si05.rsvl.unisys.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com>`

```
I neglected to point out that INITIALIZE behavior is the same as a series of
MOVE statements, one for each (named) elementary item in the record, even if
circumstances (and the implementor's cleverness) allows the initialization
to take place using a single transfer of data from somewhere.

    -Chuck Stevens

"rockocubs" <rphipps@nospam.indy.rr.com> wrote in message
news:175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com...
> Can someone settle an argument for me. Does a initialize on an 01 level
> move spaces to pic x fields and zeroes to pic 9 fields or does it move
> spaces to the whole 01 level?
>
```

##### ↳ ↳ Re: Initialize

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-27T11:46:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127846777.489195.211400@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dhc2as$1lj2$1@si05.rsvl.unisys.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <dhc2as$1lj2$1@si05.rsvl.unisys.com>`

```
> one for each (named) elementary item in the record,

Except for redefininitions.
```

#### ↳ Re: Initialize

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-09-27T11:24:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127845440.522685.56510@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com>`

```
Hi,

Yes, the initialize statement will move Zeros to all numeric variables
(pic 9),
and will move spaces to all non-numeric variables (pic X) to the whole
01 level.
you could also use it on the sub-level (05, 10, 15, etc...) with the
same results.

Kellie.
```

##### ↳ ↳ Re: Initialize

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2005-10-02T09:31:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2005.10.02.15.31.32.276068@starband.net>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <1127845440.522685.56510@g49g2000cwa.googlegroups.com>`

```
On Tue, 27 Sep 2005 11:24:00 -0700, Kellie Fitton wrote:

> Hi,
> 
…[7 more quoted lines elided]…
> Kellie.


The INITIALIZE verb also does not act on USAGE POINTER items.
Is POINTER a standard or an IBM extension?  Hmmm.
 
I use POINTERs extensively and need to make sure I initialize them
separately.

Chris
```

###### ↳ ↳ ↳ Re: Initialize

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-10-02T18:24:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11k0nkhtpg8jcfa@corp.supernews.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <1127845440.522685.56510@g49g2000cwa.googlegroups.com> <pan.2005.10.02.15.31.32.276068@starband.net>`

```

"Christopher Pomasl" <pomasl-NOSpam@starband.net> wrote in message
news:pan.2005.10.02.15.31.32.276068@starband.net...
[snip]
> The INITIALIZE verb [snip]

Beginning with COBOL 85 it is 'statement' not 'verb'.

> Is POINTER a standard or an IBM extension?  Hmmm.

USAGE POINTER was added to COBOL 2002;
therefore, it is standard when used with a 2002 conforming
compiler and an extension elsewhere, regardless of vendor.
```

###### ↳ ↳ ↳ Re: Initialize

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-10-03T05:38:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<It30f.73595$1M7.2040@fe12.news.easynews.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <1127845440.522685.56510@g49g2000cwa.googlegroups.com> <pan.2005.10.02.15.31.32.276068@starband.net> <11k0nkhtpg8jcfa@corp.supernews.com>`

```
Although the '85 Standard did refer to the "Initialize Statement" - it was not 
unitl the '02 Standard that the concept/term "verb" was removed.  See (for 
example)

Page III-11

"Imperative Statement. A statement that either begins with an imperative verb 
and specifies an unconditional action to be taken or is a conditional statement 
that is delimited by its explicit scope terminator (delimited scope statement). 
An imperative statement may consist of a sequence of imperative statements."

and, Page III-24

"Statement. A syntactically valid combination of words, literals, and 
separators, beginning with a verb, written in a COBOL source program."

and more directly, Page III-26

"Verb. A word that expresses an action to be taken by a COBOL compiler or object 
program."
```

###### ↳ ↳ ↳ Re: Initialize

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-10-03T03:05:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11k1m2ramd5pi59@corp.supernews.com>`
- **References:** `<175c3e3def2daf1a23aa674f5b3adf87@localhost.talkaboutprogramming.com> <1127845440.522685.56510@g49g2000cwa.googlegroups.com> <pan.2005.10.02.15.31.32.276068@starband.net> <11k0nkhtpg8jcfa@corp.supernews.com> <It30f.73595$1M7.2040@fe12.news.easynews.com>`

```

> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:11k0nkhtpg8jcfa@corp.supernews.com...
…[6 more quoted lines elided]…
> > Beginning with COBOL 85 it is 'statement' not 'verb'.
[snip]

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:It30f.73595$1M7.2040@fe12.news.easynews.com...
> Although the '85 Standard did refer to the "Initialize Statement" - it was
not
> unitl the '02 Standard that the concept/term "verb" was removed.  See (for
> example)
[snip]

I did not correctly recall the previous discussion in
< http://groups.google.com/group/comp.lang.cobol/msg/8475d814a04bbc12?hl=en&
>,
from February 2003, and regret not having taken the
time to check. My apologies.

-----begin quote
Just a side note to Chuck's accurate post below.  The 2002 Standard has
eliminated the concept of a "verb" in COBOL.  This was *not* a change that I
was happy with - but did please people who didn't like calling the COBOL
word "IF" a "verb".  There is no replacement term introduced - all there is,
is a list of reserved words that start (procedural) statements.
----- end quote

However, while I'm here, the replacement term appears to be
"statement-name" in the text and "Statement name" from the
column heading of a table in FDIS, page 382, 14.4 Procedural
statements and sentences, Table 13.

See FDIS, page 384, 14.4.2.1 Explicit scope termination,
"...
An explicit scope terminator terminates the scope of:
1) the most-recently preceding unterminated statement having the
    statement-name for which that scope terminator is defined, and
2) any unterminated statements that appear between that
    statement-name and the explicit scope terminator."

And 14.4.2.2 Implicit scope termination,
"The scope of a statement that is not explicitly terminated is
implicitly terminated as follows:
1) for a single imperative statement not contained within another
    statement, by
a) any element that follows the exhaustion of the statement's syntax, or
b) the next-encountered statement-name, or
c) a separator period."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
