[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Porting COBOL to NT

_25 messages · 11 participants · 1999-08_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Porting COBOL to NT

- **From:** terry_ingram@my-deja.com
- **Date:** 1999-08-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pnh5j$d03$1@nnrp1.deja.com>`

```
Background:
  About 4 years ago, we converted from a 4381 (running in s/370 mode) to
an AS/400.  We ran a mix of RPG and COBOL.  That was all pretty good.
Around April we finally turned off the PC/390 (we moved from the 4381 to
the pc/390 about 2 years ago).

Current "opportunity":
  Or MIS Manager is wanting to move to an NT box and saying that COBOL
is the way to do it cause it is portable.  I know he is thinking of
running COBOL programs and storing the data on SQL Server (or some
comparable product).  None of the COBOL currently uses embedded SQL, so
I don't understand how it can work without rewritting.

  I did see that AcuCOBOL claimed to convert the native read/writes to
SQL statements for use with Oracle, SQL server and some others.  Is
anyone using this and how well is it working?  Also, is there some other
product that does the same thing?


Thanks in advance

Terry


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Porting COBOL to NT

- **From:** "JC" <john.e.clark@spam_me_and_die.btinternet.com>
- **Date:** 1999-08-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pplv6$7pb$1@uranium.btinternet.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com>`

```
Have a look at www.xitec.com

They specialise in porting COBOL from one environment to another & might be
able to help.

Ps, I get some commission if you use the product!

John
```

##### ↳ ↳ Re: Porting COBOL to NT

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c1425f.2801652@news.enter.net>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <7pplv6$7pb$1@uranium.btinternet.com>`

```
"JC" <john.e.clark@spam_me_and_die.btinternet.com> wrote:

>Have a look at www.xitec.com
>
…[6 more quoted lines elided]…
>

John:

I tried the URL you posted and it took me to the web site of a company
which manufactures medical imaging equipment.  Can you check the URL
and post the correct one if your original post was incorrect?

Thanks!


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

- **From:** "JC" <john.e.clark@spam_me_and_die.btinternet.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7purdh$1hm$1@uranium.btinternet.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <7pplv6$7pb$1@uranium.btinternet.com> <37c1425f.2801652@news.enter.net>`

```
email sent...

www.xitec-software.com

Sorry!!

john
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c2f4d0.27741116@news.enter.net>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <7pplv6$7pb$1@uranium.btinternet.com> <37c1425f.2801652@news.enter.net> <7purdh$1hm$1@uranium.btinternet.com>`

```
"JC" <john.e.clark@spam_me_and_die.btinternet.com> wrote:

>email sent...
>
…[5 more quoted lines elided]…
>

John:

No apologies necessary.  Thanks for posting the revised URL!


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Porting COBOL to NT

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c0c31c.11815711@news1.ibm.net>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com>`

```
On Sun, 22 Aug 1999 00:44:37 GMT, terry_ingram@my-deja.com wrote:

>Background:
>  About 4 years ago, we converted from a 4381 (running in s/370 mode) to
…[16 more quoted lines elided]…
>

Here I go asking the wrong question MYSELF.

Why store it in a database.  Why not the native indexed file structure
of whatever COBOL you decide on?  Some people don't think the indexed
files (or relative) are supported on the PC.  They certainly are.
```

##### ↳ ↳ Re: Porting COBOL to NT

- **From:** Jürgen Ibelgaufts <ibelgaufts@gfc-net.de>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C10700.4E6CB217@gfc-net.de>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net>`

```
Hello all,

porting from AS400 to PC Cobol might not even be a question of database or not.
Yes, you are right: you can of course use indexed files on a PC which might even
be much faster than SQL. Problems arise from AS400 logical files that you can
define alternative indexes on a PC, but you can't sort them backwards (maybe I'm
wrong here) and you can't have any logical file with the select/omit phrases
which simply don't exist on PC Cobol.

The syntax for reading an indexed file backwards is not included in the
standards. On AS400 and on PC not only the names are different but much worse
the funcionality differs.

Aside from this, even bigger problems come from the user interface. Most AS400
users create their user interface with the native AS400 DDS (data description
specification). Doing this, you get a so-called display file which you can open,
close write and read. Writing displays the screen and reading puts the user
input into your cobol record. While displaying such a screen, you have 99
switches (indicators) that you can associate with the appearance of fields
(color, put the cursor on it, enable input etc). It is not possible to emulate
this with forms, screens or panels on a PC.

One will have to rewrite most of the database and user interface code for
porting from AS400 to PC.

Juergen Ibelgaufts

-------------------------------------------------------

Thane Hubbell schrieb:

> 
> Here I go asking the wrong question MYSELF.
…[3 more quoted lines elided]…
> files (or relative) are supported on the PC.  They certainly are.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

- **From:** "pmjones" <pmjones@netcomuk.co.uk>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pr18a$3e9$1@taliesin.netcom.net.uk>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de>`

```

To read an indexed file backwards (this works using Micro Focus' products)
...

MOVE HIGH-VALUES TO FILE-KEY
START DATA-FILE
    KEY < FILE-KEY
    INVALID KEY (etc)

READ DATA-FILE PREVIOUS
    AT END (etc)

eg. (supply your own error handling !!)

       select f1-data-file     assign "idxfile"
                               organization indexed
                               access mode  dynamic
                               record key   f1-key
                               file status  ww-status.

       fd          f1-data-file.
       01          f1-rec.
           03      f1-key              pic x(10).
           03      f1-data             pic x(20).

       working-storage section.
       01          ww-status           pic xx.

       procedure division.
       a-logic section.
           perform b-write
           perform c-read-backwards
           stop run.

       b-write section.
           open output f1-data-file
           move "key-1"    to f1-key
           move "data-1"   to f1-data
           write f1-rec
           move "key-2"    to f1-key
           move "data-2"   to f1-data
           write f1-rec
           move "key-3"    to f1-key
           move "data-3"   to f1-data
           write f1-rec
           close f1-data-file

       exit.

       c-read-backwards section.
           open i-o f1-data-file
           move high-value to f1-key
           start f1-data-file key < f1-key
           read f1-data-file previous
           display f1-rec
           read f1-data-file previous
           display f1-rec
           read f1-data-file previous
           display f1-rec

       exit.


Pete Jones
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7prv32$qqd$1@news.cerf.net>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de>`

```
J�rgen Ibelgaufts wrote in message <37C10700.4E6CB217@gfc-net.de>...
>The syntax for reading an indexed file backwards is not included in the
>standards. On AS400 and on PC not only the names are different but much
worse
>the funcionality differs.

I am not sure if it targets what you think of, but, with Acucobol one may;

    READ myfile PREVIOUS

Hence, one may read both back and forth.

Cheesle
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ps0pk$1dn@dfw-ixnews21.ix.netcom.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net>`

```
This thread has mentioned several compilers that currently support READ
PREVIOUS (as an extension) - but I thought I would add:

   GOOD NEWS - this is included in the draft of the next Standard
      BAD NEWS - It is included in the "processor dependent" category (which
means that vendors can implement it or not depending on the "market
positioning" of their processor)
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ps5p7$mr$1@aklobs.kc.net.nz>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote:
: This thread has mentioned several compilers that currently support READ
: PREVIOUS (as an extension) - but I thought I would add:

:    GOOD NEWS - this is included in the draft of the next Standard
:       BAD NEWS - It is included in the "processor dependent" category (which
: means that vendors can implement it or not depending on the "market
: positioning" of their processor)

Or the ability of their file systems to be able or not to
actually achieve PREVIOUS.  For example if their system's ISAM
structure only had index and forward links then it would be
necessary to satisfy a READ PREVIOUS by reading through the 
file from the start remembering the last read until the
current were found again, or having everyone rebuild their
data files with additional index structure.

But READ PREVIOUS is not a big deal - in most cases a careful
design of index keys and a mechanism for maintaing a stack
can avoid the need for it. (especially on systems that don't
have it).
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ps6ca$nvi@dfw-ixnews16.ix.netcom.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz>`

```
I understand the theory that their indexed system MIGHT not CURRENTLY
support "reading previous" - but in the history of COBOL, the Standard has
(often?) required that vendors enhance (implement?) their "support systems"
to MEET the Standard.  In fact, when COBOL first required indexed file
support - many "operating systems" or "file systems" didn't have support for
this - and the COBOL requirement MADE them add support for it.

Now, if you had a COBOL system that was "targeted" at an environment where
no "mass storage device" was available, then I could understand that there
really WAS a "hardware" issue in providing support for READ PREVIOUS.  If on
the other hand, you have an environment that fully supports a SQL-type
database, and you tell me that your "processor doesn't support
READ/PREVIOUS" - then I say "I DOUBT YOU!"  - If on the other hand, you
say - "my customers don't care about COBOL files or the portability of their
programs - so I will "force" them to use SQL rather than native COBOL by not
implementing READ/PREVIOUS" - then I believe you, but don't think that the
Standard has done what a Standard SHOULD do.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pst7m$6tc$1@aklobs.kc.net.nz>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote:
: I understand the theory that their indexed system MIGHT not CURRENTLY
: support "reading previous" - but in the history of COBOL, the Standard has
: (often?) required that vendors enhance (implement?) their "support systems"
: to MEET the Standard.  In fact, when COBOL first required indexed file
: support - many "operating systems" or "file systems" didn't have support for
: this - and the COBOL requirement MADE them add support for it.

: Now, if you had a COBOL system that was "targeted" at an environment where
: no "mass storage device" was available, then I could understand that there
: really WAS a "hardware" issue in providing support for READ PREVIOUS.  If on
: the other hand, you have an environment that fully supports a SQL-type
: database, and you tell me that your "processor doesn't support
: READ/PREVIOUS" - then I say "I DOUBT YOU!"  - If on the other hand, you
: say - "my customers don't care about COBOL files or the portability of their
: programs - so I will "force" them to use SQL rather than native COBOL by not
: implementing READ/PREVIOUS" - then I believe you, but don't think that the
: Standard has done what a Standard SHOULD do.

As designing around a lack of READ PREVIOUS is a trivial exercise
such as by having an inverted alternate key or by maintaing a
stack of relevant positions, then I don't see any need to force
vendors into re-implementing their file system or forcing users
into rebuilding all their data files (including those that are
archived) just to satisfy your demand for a relatively obscure
feature.

I have programmed without a READ PREVIOUS for 30 years and have
mechanisms that do everything without needing this.

I do, in fact, have some systems where an inverted date/time is
used to give latest first, why do you think the READ PREVIOUS
is essential ?  Why do you think that a lack of this 'forces'
people to use SQL ?
```

###### ↳ ↳ ↳ Portability (was Porting COBOL to NT

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pt2la$m7t@dfw-ixnews6.ix.netcom.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz>`

```

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7pst7m$6tc$1@aklobs.kc.net.nz...
> William M. Klein <wmklein@nospam.netcom.com> wrote:
  <much snippage>
>
> As designing around a lack of READ PREVIOUS is a trivial exercise
…[16 more quoted lines elided]…
> --

Although I have "snipped" most of my original quote, let me clarify two
things:

 1) I do not think that lack of READ PREVIOUS will force people into using
SQL.  I was only using an example of where an implementor DID support SQL,
but claimed that their processor couldn't support READ PREVIOUS.

 2) Whether or not the next Standard includes READ PREVIOUS is a very
different question from whether or not the Standard includes READ PREVIOUS -
but makes its implementation "dependent upon the market positioning of a
processor". I am STRONGLY against adding things to the Standard that are NOT
GUARANTEED to be portable to ANY environment where the feature is
implementable.

That means that I don't need READ PREVIOUS in the Standard at all (although
those programmers who have had it available have found it to be quite
useful) but if it is added to the Standard, then I want it to be truly
portable.  I understand why  OPEN I-O is made "dependent" upon a system with
a mass storage device - but I don't understand (or LIKE) it being dependent
upon the implementor's market positioning of their compiler.  That just
makes it impossible to code a "portable" application.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 8)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pvuqa$peo$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz>`

```

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7pst7m$6tc$1@aklobs.kc.net.nz...
>
> As designing around a lack of READ PREVIOUS is a trivial exercise
…[15 more quoted lines elided]…
>

    What mechanism do you recommend for adding new records to an indexed
file in a multiuser environment when the prime key is an arbitrary
sequentially generated number?

    Ie the first record is 00000001, second is 00000002, etc.

    Keep in mind other users will be adding new records as well in real
time.

    Since the user has the option of changing their mind and not adding
the record, I have found no method that avoids unwanted holes in the key
sequence.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C3F1CE.68BDA42F@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz> <7pvuqa$peo$1@ssauraaa-i-1.production.compuserve.com>`

```
>     What mechanism do you recommend for adding new records to an indexed
> file in a multiuser environment when the prime key is an arbitrary
…[9 more quoted lines elided]…
> sequence.

Have you ever used relative files?  They used to be popular for data
entry.  Typically, one would read the first record and find the position
of the next data entry record.  Then they would update that position and
write the record.

A variation of this two read/write method could work for you.  Have a
record large enough to hold a map of the file (bit 1 = record 1, etc.). 
Your data entry finds the first empty bit, updates it, and then writes
the record.  If it needs to roll back, it empties the map bit.

By the way, why do you need to avoid holes?
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C29915.3B485A37@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz>`

```
> I have programmed without a READ PREVIOUS for 30 years and have
> mechanisms that do everything without needing this.

And we have programmed without lots of other extensions to the language
as well.  Are you implying that a READ PREVIOUS isn't a good idea
because we have worked around it for so long?
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pv1mm$ote$1@aklobs.kc.net.nz>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz> <37C29915.3B485A37@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:
:> I have programmed without a READ PREVIOUS for 30 years and have
:> mechanisms that do everything without needing this.

: And we have programmed without lots of other extensions to the language
: as well.  Are you implying that a READ PREVIOUS isn't a good idea
: because we have worked around it for so long?

No, I am saying it isn't necessary.  I was also saying that the
lack of it does not _force_ programmers to use SQL (as was
implied).
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C31368.EBB0B1AC@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz> <37C29915.3B485A37@NOSPAMhome.com> <7pv1mm$ote$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Howard Brazee <brazee@nospamhome.com> wrote:
…[9 more quoted lines elided]…
> implied).

I missed that (or failed to infer it).  It still seems like a good idea
- although not as useful as it would have been 20 years ago!

Going to the SQL concept.

Right now, it would be almost acceptable to give up variable length
records, relative files, and other types of record storage which are
becoming obsolete with the use of external databases.  Lots of Cobol
skip the internal I-O commands and instead use external commands (IDMS,
IMS, SQL, etc) accessed through calls (via pre-compilers etc).  
(note the "almost" - I'm not suggesting this, but I would like to see
some discussion).

Files with header records and various detail type records became more
and more common as a replacement for variable length record files until
they in turn were replaced by databases.  Sure we have some leftovers,
but this seems to be a strong trend to me.

But we didn't use Cobol commands to read "Detail Record type A", instead
we wrote code which acts like hierarchical databases, calcing into the
parent record and then walking the set of detail records.  I haven't
seen any Cobol accessing object databases.  Cobol reading SQL cursors
doesn't look like the Cobol I am used to.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Syzw3.650$SC5.30543@iad-read.news.verio.net>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <7ps6ca$nvi@dfw-ixnews16.ix.netcom.com> <7pst7m$6tc$1@aklobs.kc.net.nz>`

```
In article <7pst7m$6tc$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@kcbbs.gen.nz> wrote:

[snippimente]

>I have programmed without a READ PREVIOUS for 30 years and have
>mechanisms that do everything without needing this.
…[4 more quoted lines elided]…
>people to use SQL ?

Mr Plinston, with all due respect... this sound remarkably like the
attitude which Rear Adm Grace W. Hopper, may she sleep with the angels,
used to call 'most dangerous' and described as 'but we've *always* done it
This Way'.

DD
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C1B876.BD86BF40@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> Or the ability of their file systems to be able or not to
> actually achieve PREVIOUS.  For example if their system's ISAM
…[9 more quoted lines elided]…
> have it).

Most hierarchical and network databases allow the equivalent of READ
PREVIOUS.  If your set does not have prior pointers, you can have
performance problems.  Over the years as hardware costs have shrunk,
most sets have been created with next, prior, and owner (if allowed)
pointers.  If READ PREVIOUS were allowed and keyed datasets could have
previous pointers, shops would default with having them turned on in
short order.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pstge$6tc$2@aklobs.kc.net.nz>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <37C1B876.BD86BF40@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:

: Most hierarchical and network databases allow the equivalent of READ
: PREVIOUS.  If your set does not have prior pointers, you can have
: performance problems.  Over the years as hardware costs have shrunk,
: most sets have been created with next, prior, and owner (if allowed)
: pointers.  If READ PREVIOUS were allowed and keyed datasets could have
: previous pointers, shops would default with having them turned on in
: short order.

In what way are 'hierarchical and network databases' ISAM systems ?
In what way does the lack of READ PREVIOUS prevent accessing these
databases in appropriate ways ?  In which way would a vendor using
READ to access these databases have a problem in implementing
a PREVIOUS option ?
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C29A5C.4FA04002@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <37C1B876.BD86BF40@NOSPAMhome.com> <7pstge$6tc$2@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Howard Brazee <brazee@nospamhome.com> wrote:
…[9 more quoted lines elided]…
> In what way are 'hierarchical and network databases' ISAM systems ?

They aren't, but they process ordered data in a similar fashion.

> In what way does the lack of READ PREVIOUS prevent accessing these
> databases in appropriate ways ?  

It depends on what you mean by "appropriate ways".  When you have a
better tool, that better tool becomes the "appropriate way".  Sure you
can get the job done with an inferior tool, but why not improve on our
tool chest?

> In which way would a vendor using
> READ to access these databases have a problem in implementing
> a PREVIOUS option ?

If the database/file was designed with next pointers but not with prior
pointers.
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pv28b$ote$2@aklobs.kc.net.nz>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <37C1B876.BD86BF40@NOSPAMhome.com> <7pstge$6tc$2@aklobs.kc.net.nz> <37C29A5C.4FA04002@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:
:> 
:> In what way are 'hierarchical and network databases' ISAM systems ?

: They aren't, but they process ordered data in a similar fashion.

But do they use the READ statement to do so ?  If your argument
is that the lack of a READ PREVIOUS is restrictive on the use
of 'hierarchical and network databases' then you have to show
that these databases are actually accessed using the READ
statement (and not some CALL or EXEC-SQL) and that the implementations
that give this READ statement access have decided not to 
implement the PREVIOUS option.

:> In what way does the lack of READ PREVIOUS prevent accessing these
:> databases in appropriate ways ?  

: It depends on what you mean by "appropriate ways".  When you have a
: better tool, that better tool becomes the "appropriate way".  Sure you
: can get the job done with an inferior tool, but why not improve on our
: tool chest?

Which implementations without READ PREVIOUS use the READ statement
to access their hierarchical and network databases ?

:> In which way would a vendor using
:> READ to access these databases have a problem in implementing
:> a PREVIOUS option ?

: If the database/file was designed with next pointers but not with prior
: pointers.

Is that a limitation of the database system or on the designed structure
of the particular set of data ?
```

###### ↳ ↳ ↳ Re: Porting COBOL to NT

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C315D1.98334E8D@NOSPAMhome.com>`
- **References:** `<7pnh5j$d03$1@nnrp1.deja.com> <37c0c31c.11815711@news1.ibm.net> <37C10700.4E6CB217@gfc-net.de> <7prv32$qqd$1@news.cerf.net> <7ps0pk$1dn@dfw-ixnews21.ix.netcom.com> <7ps5p7$mr$1@aklobs.kc.net.nz> <37C1B876.BD86BF40@NOSPAMhome.com> <7pstge$6tc$2@aklobs.kc.net.nz> <37C29A5C.4FA04002@NOSPAMhome.com> <7pv28b$ote$2@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Howard Brazee <brazee@nospamhome.com> wrote:
…[5 more quoted lines elided]…
> But do they use the READ statement to do so ?  

No, the READ statement was an inadequate tool for this task.  They had
to be non-Cobol via pre-compiler calls.  The function of a READ PREVIOUS
was one of the characteristics which was required but which was not
available.

> If your argument
> is that the lack of a READ PREVIOUS is restrictive on the use
…[4 more quoted lines elided]…
> implement the PREVIOUS option.

They worked around this restriction because this restriction was large
enough to make the READ useless.   I am missing the point of your
statement.  If READ PREVIOUS had been available, they might have used
it.  It wasn't.  
 
> :> In what way does the lack of READ PREVIOUS prevent accessing these
> :> databases in appropriate ways ?
…[7 more quoted lines elided]…
> to access their hierarchical and network databases ?

None do, because READ is insufficient to the task.  So they use
equivalent commands which translate into call statements. 
 
> :> In which way would a vendor using
> :> READ to access these databases have a problem in implementing
…[6 more quoted lines elided]…
> of the particular set of data ?

Doesn't matter.  Nowadays, people routinely put in next, prior, and
owner pointers without doing any analysis about which are actually
needed.  It is cheaper to have them and not need them than to have to
add them in later when requirements change.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
