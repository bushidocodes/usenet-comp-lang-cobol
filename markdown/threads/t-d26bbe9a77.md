[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help me identify a Cobol database

_32 messages · 9 participants · 2010-02_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### Help me identify a Cobol database

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T09:11:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com>`

```
Need to identify some database files used by a PC COBOL program
written in the mid-90's.  The extensions are .DB and .IDX.  Given the
date, language and OS, are there any candidates you can think of?  I
can send a sample of the files if that would help.

Thanks,
Jim
```

#### ↳ Re: Help me identify a Cobol database

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-01T17:26:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hk72sr$j5d$1@reader1.panix.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com>`

```
In article <b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com>,
SomeGuy  <jimgreen@nc.rr.com> wrote:
>Need to identify some database files used by a PC COBOL program
>written in the mid-90's.

Find someone who has demonstrable experience in that particular sub-set of 
the discipline.  Verify the references you are given.  Agree on a rate and 
let the job be done.

(You *do* realise that retaining this kind of knowledge is how some folks 
make their livings, right?)

DD
```

##### ↳ ↳ Re: Help me identify a Cobol database

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T09:39:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com>`

```
On Feb 1, 12:26 pm, docdw...@panix.com () wrote:
> In article <b40fdfcc-d80f-4b3e-912a-6c56f313e...@r6g2000yqn.googlegroups.com>,
>
…[11 more quoted lines elided]…
> DD

Wow, DD, thanks, that was so helpful.  Makes me regret all the time
I've spent in the past answering questions on newsgroups for free when
I could have just told them to hire someone!
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-01T12:55:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kkG9n.74380$CM7.7314@newsfe04.iad>`
- **In-Reply-To:** `<bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com>`

```
SomeGuy wrote:
> On Feb 1, 12:26 pm, docdw...@panix.com () wrote:
> 
…[19 more quoted lines elided]…
> I could have just told them to hire someone!

I can appreciate that DD may have pissed you off, but seeing that you 
say you have helped others, (in other languages), via Newsgroups, your 
query is incomplete. So let's take a stab at how perhaps it might have 
conveyed more :-

"- I program in xxxxxxx
  - I DO/Don't know COBOL
  - I haven't got the COBOL compiler, so that's why I'm asking
  - I DO/Don't have the source for the datafile layouts
  - I DO/Don't have any reports that indicate how records were used
  - I DO/Don't have executables, (compiled and 
linked), to run the 									programs
  - the end-user is a cheap skate who wants it to cost 
as little as 									possible
  - I have files on diskettes or CD with names ending 
in xxx.DB and 									xxx.IDX"

How close is above ?

First off can't remember how many compilers but at the time there may 
have been some six in the mid 90s. Some of those vendors have been 
absorbed/taken over into the remaining active vendors.

I don't know which of the (six ?) vendors used those file extensions, 
but I can tell you that Mcro Focus traditionally have extensions of 
xxxx.DAT and xxxx.IDX. (Had that been xxx.INX, then likely it was 
RMCOBOL (Ryan McFarland); became part of Liant and in turn they became 
part of Micro Focus)).

As indicated M/F traditionally use xxxx.DAT to indicate the data file, 
but in this instance, (and assuming it's Micro Focus), the developer 
chose to use the extension xxxx.DB.

The xxxx.IDX indicates that your data file is ISAM (Indexed Sequential 
Access Mode), i.e. the IDX file contains a reference to the KEY for 
records. So :-

01 CustomerRecord.
    05 CustomerNumber	pic x(06).    *> <---- = ONLY key
    05 CustomerName	pic x(40).
    05 etc.....

the IDX file has records for each CustoerNumber x(06), so that you can 
randomly retrieve records by key.

You still don't know what you've got, even with the above. Let's 
complicate it a bit :-

01 CustomerRecord.
    05 CustomerNumber	pic x(06).    		*> = ONLY key
    05 CustomerName	pic x(40).
    05 etc.....
    05 SalesThisWeek	pic s9(06)v9(02) comp-3
				*> signed 6 integers 2 decimals
    05 SalesYTD		pic s9(10)v9(02) comp-3
				*> signed 10 integers 2 decimals

If you try and bring the above up in a 'Viewer', the pic x fields will 
be OK - they indicate strings/text, but those numeric values will look 
like hieroglyphics on a wall in ancient Egypt; they are binary values. 
To complicate it even further, (again assuming Micro Focus), the 
developer, in order to save disk space, may have used a compiler 
DIRECTIVE to compress data - basically repeating characters are 
indicated by a count. With a bit of luck he didn't use a compression 
Directive :-).

Without the source showing each record layout and record-size, you are 
screwed. I don't know whether they are still active but if you google on 
'COBOL FAQ', (although not updated for some years), it may have 
references to COBOL Developers who have produced Data conversions - 
primarily they were aiming at converting from COBOL-Vendor-A to 
COBOL-Vendor-B compilers.

Now again assuming it might just be Micro Focus COBOL, Net Express has a 
nifty tool in the IDE where I can use the Common Dialog for 'Open File'
to open files with extension xxxx.DAT. The Header record in that file 
indicates its makeup - well, sort of, and each record gets displayed 
across the screen with a pic s(9)v9(03) comp-3 (assume a value of 
+123.450) - that gets displayed as +000000123.450.

If, and only if, completely stuck, send me the xxx.DB and xxx.IDX for 
one file (not too large !) - and specifically for a file that contains 
numeric values. Not going to say it will work - but perhaps just might.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 4)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T12:43:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com> <kkG9n.74380$CM7.7314@newsfe04.iad>`

```
Thanks for the very helpful reply!

[Aside - I don't think it's uncommon or out-of-line for a NG post to
appear that requires a "need more information" response" (and people
generally don't suggest you're trying to ruin someone else's
livelihood by asking :-)]

No I've never done COBOL development, though I'm familiar with
defining records and that COBOL has various pictured and "comp" types
(I have worked with PL/I which has somewhat similar features).  I was
hoping that the files might be some sort of standard DB (maybe vendor-
specific, maybe obsolete), but it's certainly looking like the
contents are defined by declarations in code.  There are no
identifiable field names, like you might find in, say, a DBF file.
Unfortunately I do not have source and will not have unless we
convince the customer to share code from the prior vendor (if they
even have it).

I'll Google Net Express.  Thanks again.  Jim
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2010-02-01T22:58:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0gem5dnpgpc0a12bo1v3ft2cte4vfml94@4ax.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com> <kkG9n.74380$CM7.7314@newsfe04.iad> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com>`

```
On Mon, 1 Feb 2010 12:43:22 -0800 (PST) SomeGuy <jimgreen@nc.rr.com> wrote:

:>Thanks for the very helpful reply!

:>[Aside - I don't think it's uncommon or out-of-line for a NG post to
:>appear that requires a "need more information" response" (and people
:>generally don't suggest you're trying to ruin someone else's
:>livelihood by asking :-)]

:>No I've never done COBOL development, though I'm familiar with
:>defining records and that COBOL has various pictured and "comp" types
:>(I have worked with PL/I which has somewhat similar features).  I was
:>hoping that the files might be some sort of standard DB (maybe vendor-
:>specific, maybe obsolete), but it's certainly looking like the
:>contents are defined by declarations in code.  There are no
:>identifiable field names, like you might find in, say, a DBF file.
:>Unfortunately I do not have source and will not have unless we
:>convince the customer to share code from the prior vendor (if they
:>even have it).

If you do not have a record layout and do not know the content, how will
knowing which version of ISAM help?

Why wouldn't the client provide the source? Do they want to pay more for your
services? Are they giving you a test?
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T13:39:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b576bb89-41fa-4b7b-b0a9-e2346d460d24@28g2000vbf.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com> <kkG9n.74380$CM7.7314@newsfe04.iad> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com> <f0gem5dnpgpc0a12bo1v3ft2cte4vfml94@4ax.com>`

```
> If you do not have a record layout and do not know the content, how will
> knowing which version of ISAM help?

When I posted this, I did not even know the nature of the DB file.
(COBOL newbie - see above.) It does now appear that a layout will be
required.

> Why wouldn't the client provide the source? Do they want to pay more for your
> services? Are they giving you a test?

They feel they are honoring their contract with the vendor of the
existing program.  They will not provide the executable to us to run.
I do not know if they even have source.

Jim
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-02T14:00:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hk9b6m$qtl$2@reader2.panix.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com> <kkG9n.74380$CM7.7314@newsfe04.iad> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com>`

```
In article <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com>,
SomeGuy  <jimgreen@nc.rr.com> wrote:
>Thanks for the very helpful reply!
>
…[3 more quoted lines elided]…
>livelihood by asking :-)]

Not 'ruin their livelihood'... just get them to do for free what they do 
for a salary.  'Hey, Sam, you got a free day to drive this tractor-trailer 
rig a couple-five hundred miles for me?  I've put some effort into the 
project... see, I know how to buckle my safety-belt!'

DD
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-02T13:37:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a930fb6-22fb-4a4f-8fa0-4b73fc71118f@a13g2000vbf.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com> <kkG9n.74380$CM7.7314@newsfe04.iad> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com> <hk9b6m$qtl$2@reader2.panix.com>`

```
On Feb 2, 9:00 am, docdw...@panix.com () wrote:
> In article <c35879ad-0e56-4cf9-8fc1-088fad613...@h33g2000vbr.googlegroups.com>,
>
…[13 more quoted lines elided]…
> DD

Hmmm, let's review this thread, shall we?

Jim: How would I identify the format of a data file used by a PC COBOL
program?
Answer: it contains records defined by COBOL source, which you'll need
to have to read it.

Apparently, the above exchange is equivalent to asking someone to
drive a tractor-trailer rig. For hundreds of miles. For free.

It's all so clear now.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-03T14:07:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hkbvvj$mb5$1@reader2.panix.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com> <hk9b6m$qtl$2@reader2.panix.com> <9a930fb6-22fb-4a4f-8fa0-4b73fc71118f@a13g2000vbf.googlegroups.com>`

```
In article <9a930fb6-22fb-4a4f-8fa0-4b73fc71118f@a13g2000vbf.googlegroups.com>,
SomeGuy  <jimgreen@nc.rr.com> wrote:
>On Feb 2, 9:00?am, docdw...@panix.com () wrote:
>> In article
…[18 more quoted lines elided]…
>program?

A: Familiarising which of a variety of PC COBOL environments produce what 
kinds of files under different conditions is part of the skill-set used by 
a professional programmer to earn a living.

>Answer: it contains records defined by COBOL source, which you'll need
>to have to read it.

Conclusion: you get what you pay for... sometimes even double.

>
>Apparently, the above exchange is equivalent to asking someone to
>drive a tractor-trailer rig. For hundreds of miles. For free.
>
>It's all so clear now.

Requesting that a person provide information and skills which said person 
uses in order to earn a living without offering recompense for said 
information and skills is equivalent to requesting a person provide 
information and skills which said person uses in order to earn a living 
without offering recompense for said information and skills... by Neddie 
Dingo, programming starts with Logic, you may just have taken the first 
step!

DD
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 8)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-03T07:50:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8774f7ee-6b4d-47e3-b3d5-18cb230cedf7@o3g2000yqb.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <c35879ad-0e56-4cf9-8fc1-088fad613fa1@h33g2000vbr.googlegroups.com> <hk9b6m$qtl$2@reader2.panix.com> <9a930fb6-22fb-4a4f-8fa0-4b73fc71118f@a13g2000vbf.googlegroups.com> <hkbvvj$mb5$1@reader2.panix.com>`

```
On Feb 3, 9:07 am, docdw...@panix.com () wrote:
> In article <9a930fb6-22fb-4a4f-8fa0-4b73fc711...@a13g2000vbf.googlegroups.com>,
>
…[49 more quoted lines elided]…
> DD

Ok, dude, whatever.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

- **From:** docdwarf@panix.com ()
- **Date:** 2010-02-02T13:57:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hk9b02$qtl$1@reader2.panix.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <hk72sr$j5d$1@reader1.panix.com> <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com>`

```
In article <bdde5a86-8738-46e0-b046-6a6003dd3476@z26g2000yqm.googlegroups.com>,
SomeGuy  <jimgreen@nc.rr.com> wrote:
>On Feb 1, 12:26?pm, docdw...@panix.com () wrote:
>> In article <b40fdfcc-d80f-4b3e-912a-6c56f313e...@r6g2000yqn.googlegroups.com>,
…[14 more quoted lines elided]…
>I could have just told them to hire someone!

Data which run a company - and the ability to manipulate them - are things 
which, in many cases, are worth money.  Regret is a manifestation of the 
past subjunctive mood and can bee seen as philosophically unjustifiable.  
To do good with the expectation of having good done in return is not 
generosity, it is commerce.

(sorry... the last cookie has a slip in it that reads 'Help!  I'm being 
held prisoner in a Chinese bakery!')

DD
```

#### ↳ Re: Help me identify a Cobol database

- **From:** Duke Normandin <dukeofperl@nospam.net>
- **Date:** 2010-02-01T17:57:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4CE9n.64156$PH1.50288@edtnps82>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com>`

```
On 2010-02-01, SomeGuy <jimgreen@nc.rr.com> wrote:
> Need to identify some database files used by a PC COBOL program
> written in the mid-90's.  The extensions are .DB and .IDX.  Given the
…[4 more quoted lines elided]…
> Jim

http://www.google.com/search?q=cobol+PC+1995&sourceid=mozilla-search&start=0&start=0&ie=utf-8&oe=utf-8&client=mozilla&rls=org.mozilla:en-US:unofficial
```

##### ↳ ↳ Re: Help me identify a Cobol database

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T10:36:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbd95a46-3221-4514-9ca0-8a926d071f4f@21g2000yqj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <4CE9n.64156$PH1.50288@edtnps82>`

```
On Feb 1, 12:57 pm, Duke Normandin <dukeofp...@nospam.net> wrote:
> On 2010-02-01, SomeGuy <jimgr...@nc.rr.com> wrote:
>
…[10 more quoted lines elided]…
> Duke

I've already Google'd various combinations.  Is there a specific hit
in that search that would help with this question?

Thanks.
```

#### ↳ Re: Help me identify a Cobol database

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-01T13:43:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com>`

```
On Feb 2, 6:11 am, SomeGuy <jimgr...@nc.rr.com> wrote:
> Need to identify some database files used by a PC COBOL program
> written in the mid-90's.  The extensions are .DB and .IDX.  Given the
…[4 more quoted lines elided]…
> Jim

The .DB is probably a user choice. The .IDX is most likely an index
file for the .DB. If the first two bytes of the .IDX is 0xFE53 then it
is probable that these are MicroFocus LevelII/CISAM format indexed
files.

The first block of the .IDX should have further information giving
record length and key information (size and start position).

If the files are LevelII/CISAM then the data records in the .DB will
be fixed length with CR/LF record terminators. Other formats may have
variable length records with record headers and/or may have compressed
data.

Without an FD entry you are unlikely to be able to know what the data
fields are or even where they start/end within the record.
```

##### ↳ ↳ Re: Help me identify a Cobol database

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-01T14:22:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dca2f57c-334c-457a-a259-b9c5a1928c73@j6g2000vbd.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com>`

```
On Feb 1, 4:43 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Feb 2, 6:11 am, SomeGuy <jimgr...@nc.rr.com> wrote:
>
…[22 more quoted lines elided]…
> fields are or even where they start/end within the record.

Richard,

FWIW, the IDX starts with 0x31FE.  In any case, it looks like the
vendor is not really the important thing to have but the layout.

Thanks,
Jim
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-02-02T14:23:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b682769$0$279$14726298@news.sunsite.dk>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <dca2f57c-334c-457a-a259-b9c5a1928c73@j6g2000vbd.googlegroups.com>`

```
SomeGuy wrote:

> On Feb 1, 4:43ï¿œpm, Richard <rip...@Azonic.co.nz> wrote:
>> On Feb 2, 6:11ï¿œam, SomeGuy <jimgr...@nc.rr.com> wrote:
…[23 more quoted lines elided]…
> vendor is not really the important thing to have but the layout.

Did you already try to use the file command ? See :
http://www.darwinsys.com/file/
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 4)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-02T13:07:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<de72814e-7e4c-4b82-ba7f-975ad814c952@w12g2000vbj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <dca2f57c-334c-457a-a259-b9c5a1928c73@j6g2000vbd.googlegroups.com> <4b682769$0$279$14726298@news.sunsite.dk>`

```
On Feb 2, 8:23 am, Fred Mobach <f...@mobach.nl> wrote:
> SomeGuy wrote:
> > On Feb 1, 4:43 pm, Richard <rip...@Azonic.co.nz> wrote:
…[31 more quoted lines elided]…
>  .. The rest we monitor ..

Never heard of it before, but just tried online at http://swoag.webhop.org/
(which per Wikipedia uses it internally).  Reports both the DB and IDX
as "data".  Thanks.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-02-04T10:59:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hker7g0n4m@news1.newsguy.com>`
- **In-Reply-To:** `<de72814e-7e4c-4b82-ba7f-975ad814c952@w12g2000vbj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <dca2f57c-334c-457a-a259-b9c5a1928c73@j6g2000vbd.googlegroups.com> <4b682769$0$279$14726298@news.sunsite.dk> <de72814e-7e4c-4b82-ba7f-975ad814c952@w12g2000vbj.googlegroups.com>`

```
SomeGuy wrote:
> On Feb 2, 8:23 am, Fred Mobach <f...@mobach.nl> wrote:
>> Did you already try to use the file command ? See :http://www.darwinsys.com/file/
…[3 more quoted lines elided]…
> as "data".  Thanks.

The standard Unix file command does not contain information about file
types. Instead, it uses a side file, /etc/magic, which describes
heuristic identifiers for various kinds of files.

Originally, /etc/magic was just a list of "magic cookie" values that
appeared as the first few bytes of a handful of specific file types on
various Unix implementations - executables, shell scripts, archive
libraries, etc. Later implementations of the file command and
/etc/magic are more sophisticated, and entries in /etc/magic can be
fairly complicated rules (along the lines of search for this regular
expression, then get the value of this byte at this offset from the
match, and so on).

So just using some random implementation of the file command doesn't
guarantee that you're using one with a very comprehensive /etc/magic
file. And many ISVs add entries to /etc/magic as part of product
installation, to recognize the particular file types their code generates.

Since http://swoag.webhop.org/ provides no information (that I could
find) about what implementation it's using, who knows if it's any good?

Of course, this won't help you identify the files in question, unless
you want to go around trying different file implementations (which you
probably don't).

Incidentally, file implementations are available for Windows, for
example as part of Cygwin. (For the record, the Cygwin /etc/magic
doesn't recognize MF ISAM files or their index files as anything but
"data". I'm not sure there *is* anything in MF ISAM files that can be
used to distinguish them.) While they may not help in this particular
case, they can be useful in others.
```

##### ↳ ↳ Re: Help me identify a Cobol database

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-02T04:18:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com>`

```
On Feb 1, 9:43 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Feb 2, 6:11 am, SomeGuy <jimgr...@nc.rr.com> wrote:
>
…[22 more quoted lines elided]…
> fields are or even where they start/end within the record.

Am I the only person who remembers dBase files which (IIRC) were
suffixed .DB?
Since the .DB files are unlikely to contain cobol specific data items
then importing the flat files in to MS Access would be an option. It
would require some understanding of data formats and intelligent
guessing of layouts. Not too difficult, even I have done that in the
past.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-02T13:11:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com>`

```
On Feb 2, 7:18 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On Feb 1, 9:43 pm, Richard <rip...@Azonic.co.nz> wrote:
>
…[34 more quoted lines elided]…
> past.

How would one go about guessing the layout of a COBOL-generated file
for which you know next to nothing about the layout?  Note that,
unlike DBase files, I can discern no field descriptors (name, type,
start, length, etc...) in the file.

Thanks.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-02T18:37:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vr4an.150013$uH1.1193@newsfe25.iad>`
- **In-Reply-To:** `<920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com>`

```
SomeGuy wrote:
> On Feb 2, 7:18 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>>
…[13 more quoted lines elided]…
> Thanks.

Well sort of - you've basically got to get at the DB Engine where you 
INITIALLY CREATE a Table specifying for each column, what type, length 
etc., it has. Granted the format and Data are in the same file, and to 
some extent the M/F COBOL file headers have 'some' information, but it 
doesn't take you all the way. So without Alistair the Alligator's 
guessing game, to be ABSOLUTELY proof positive you need two things from 
the COBOL application, and the first I forgot to mention, concentrating 
  on the Record Layout. Here's some template stuff I have for files 
using OO classes :-

  *>------------------------------------------------------------
  OBJECT.
  *>------------------------------------------------------------
$*> set datacompress "1" - use as necessary

  FILE-CONTROL.

   Select               Data-File
   assign               Data-filename
   organization         indexed
   access               dynamic
   record key           Data-PrimeKey   *> +++ CHANGE **** (1)
   alternate key        Data-AltKey1    *> +++ CHANGE **** (1 & 2)
   file status          ws-FileStatus.
  *> lock mode            .............. *> +++ CHANGE **** (3)

*>----------------------------------------------------------------

  *> (1) PRIME and ALTERNATE KEYS :

  *> Both PrimeKeys and Alternate Keys can be SLIT KEYS :-
  *>
  *> 01 Data-Record.
  *>    03 FirstName         pic X(10).
  *>    03 Personnel-no      pic X(4).
  *>    03 LastName          pic X(15).

  *>  the syntax:  record key is Fullname = LastName, FirstName

  *> would cause the COBOL system to treat Fullname as though it
  *> were an explicitly defined group item consisting of :

  *>    03 LastNamee pic X(15).
  *>    03 FirstName pic x(10).

  *> (2) ALTERNATE KEYS

  *> Either delete or specify 'with or without duplicates'.
  *> If present ensure you add methods to handle alternates

  *> (3) LOCK MODE :

  *> lock mode } automatic} with (1) lock On (Multiple) Record(s)
  *>           } manual   }  "    "   "      "        "    "
  *>                         "   (2) Rollback
  *>           } exclusive

  *>---------------------------------------------------------------

  FILE SECTION.

  FD  Data-File.

  01  Data-record.                     *> +++ CHANGE ****
      05 Data-PrimeKey  pic x(20).     *> by substituting your
      05 Data-Info-1    pic x(70).     *> copy record
      05 Data-AltKey1   pic x(30).     *>
      05 Data-info-2    pic x(140).    *>

  *> Replace this dummy info with a copyfile containing your record.
  *> So that the copyfile can be used elsewhere in other programs/
  *> classes, prefix each field with (tag), so that you can have an
  *> entry :-
  *>
  *> 01 Data-Record.
  *> copy 'myrecord.cpy' replacing ==(tag)== by ==Data==.

  *>---------------------------------------------------------------

It's possible, that in some instances the developers *may* have used 
Alternate Keys for some of their ISAM files. If their application is 
multi-user, they may have used the LOCK MODE feature.

Using that DFE (Data File Editor) I mentioned - I tried it on a simple 
file. As I indicated it takes the binary values and translates them to 
what is referred to in COBOL as Usage Display, (printable numbers), i.e. :-

pic 9(04)v9(02) comp-3 (contains 012345) shows as '0123.45' in the 
display dialog. BUT it doesn't give you a column-header description, nor 
when you look at the size does it indicate whether or not the field was 
specified as :-

- pic 9(04).9(02), pic 9(04)v9(02) or pic 9(04)v9(02) comp-3, and 
depending upon the compiler, other variations on the 'comp-3', such as 
comp-1, comp-5.

The only thing it specifically does, in the case of ISAM, is define the 
positioning of the PrimeKey and any Alternate Keys, such as :-

- PrimeKey (1:20)    Alt-Key-1 (30:40)  Alt-Key-2 (78:20)

I drafted something, but I don't think I sent it. Either the end-user 
has got to show you what they have, from reports, (which will still 
entail you doing a lot of messing about to extract the data), or bite 
the bullet, and for an acceptable fee get the file formats from the 
original developers - *IF* they will sell them to you !

Did you google on COBOL data conversions, or look at the COBOL FAQ for 
help ?

Jimmy, Calgary AB

PS: Alistair once told us spell checkers want to change his name to 
'Alligator' ;-)
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-03T08:13:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f74a3eff-b9c7-4ae3-a56b-2a004751fc88@s12g2000yqj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <vr4an.150013$uH1.1193@newsfe25.iad>`

```
On Feb 2, 8:37 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> SomeGuy wrote:
> > On Feb 2, 7:18 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
…[129 more quoted lines elided]…
> 'Alligator' ;-)

To be honest, never having used COBOL, I didn't really follow
everything you posted.  I looked at the Net Express website but
couldn't find information about the DFE.  I did try the Siber Systems
Data Viewer.  It manages to report a lot of columns, many of them with
legitimate-looking values.  But the rest have basically gibberish and
all have only generated names (like "GUESSED-535-1").

Another thought: is there a tool that will scan COBOL source and
produce a report (copybook? FDD?) with the layout?  If so, perhaps I
can give the tool to the client to run for me (assuming they have
source).

I really appreciate the effort you've put in.  Above and beyond.

Jim
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-03T09:52:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d27b5726-c5e5-47fa-ab97-81c5801c6712@h2g2000yqj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <vr4an.150013$uH1.1193@newsfe25.iad> <f74a3eff-b9c7-4ae3-a56b-2a004751fc88@s12g2000yqj.googlegroups.com>`

```
On Feb 3, 4:13 pm, SomeGuy <jimgr...@nc.rr.com> wrote:
> On Feb 2, 8:37 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
>
…[148 more quoted lines elided]…
>

The COPYBOOKS (some of the files suffixed .cbl) should be part of the
project environment available to your clients. If the copybooks are
not there they are unlikely to be in the program code. Copybooks
contain record layouts (in cobol-speak) which may contain the FD (file
description) but don't have to contain the FD.

The copybooks, if they exist, should be readable using notepad and
will contain stuff like:

   01  record-layout.

     03  text-data-item   pic x(255).          < text, length 255
characters.
     03  numeric-item     pic 9(9) comp-3.     <  a packed field
     03  another-number   pic s9(4) comp.      <  a binary number. How
this appears in the
                                                  data depends upon
whether the hardware
                                                  is big-endian or
little-endian.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-03T15:37:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jUman.26522$p66.1770@newsfe09.iad>`
- **In-Reply-To:** `<f74a3eff-b9c7-4ae3-a56b-2a004751fc88@s12g2000yqj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <vr4an.150013$uH1.1193@newsfe25.iad> <f74a3eff-b9c7-4ae3-a56b-2a004751fc88@s12g2000yqj.googlegroups.com>`

```
>>SomeGuy wrote:
>>
…[29 more quoted lines elided]…
> legitimate-looking values.  

Doesn't surprise me; no doubt you could clearly see text fields such as :-

01 CustomerRecord.
05 CustomerKey	pic x(05).
05 Customer Name pic x(40).
		 ---> 'Encana Construction Ltd.................."	
or Usage Display values :-

05 GSTorVatNumber pic 9(10).
		----> '8282233344'

Your gibberish will be (which accounts for "GUESSED-535-1" ):-

05 SalesThisWeek	pic s9(04)v9(02) comp-3.
05 Sales YTD		pic s9(10)v9(02) comp-3.

But the rest have basically gibberish and
> all have only generated names (like "GUESSED-535-1").
> 
…[4 more quoted lines elided]…
> 
No there just aren't such tools; as previously indicated, a limited 
amount in the File Header record, primarily to do with sizing and 
accessing but the real answer is in the record formats.

Even assuming you are very proficient at 'bit-fiddling', and given you 
had the record layouts, you've still got to locate the fields by size 
and translate them into numeric values that you want. (Seeing as Bob has 
just recently done a low key sales pitch :-), check out Flexus.com. They 
have a document from Michael Mattias, a contributor here, explaining 
COBOL binary fields).

I can assure you GIVEN a COBOL programmer had BOTH the record layouts, 
and the appropriate compiler, (We're still into assuming it's Micro 
Focus), it wouldn't take too much time to knock out a conversion per 
file. (Which was what DD was alluding to). The steps are :-

1 - create a COBOL source that contains the copyfiles for the FD and 
Record layouts, which Alistair and I mentioned.
2 - above includes the record layout additionally for a CSV file
3 - Open Your file as input and the CSV file as Output
4 - read records sequentially and just move the input fields to text and 
non-binary fields as appropriate.

01 CSV-Record.
  05 CustomerKey			pic x(06).
  05				pic x value ",".
  05 CustomerName		pic x(40).
  05				pic x value ",".
  05 GSTorVatNumber 		pic 9(10).
  05				pic x value ",".
  05 SalesThisWeek		pic -9999.99.	    *> shows +/-
  05				pic x value ",".
  05 Sales YTD			pic -9999999999.99. *> shows +/-
  05				pic x value ",".			
  05				pic x value ",".
  05 etc....

It is not a challenging exercise; I've done it moving RM/COBOL data 
files to Micro Focus; but in my case I additionally had the advantage of 
bit routines from Micro Focus, to convert RM binaries to M/F format.
Why my Two Step approach ? Without going into details, I took the 
opportunity to enhance the application, so wrote to the output CSVs, 
which meant incoming Record-A might finish up as output Records B and C, 
particularly when I got into (R)DBMS and SQL.

Bear in mind I had the compiler for RM/COBOL as well, and MOST 
IMPORTANTLY, having programmed the application in RM, I also had the RM 
RECORD FORMATS ! 	

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-03T09:44:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b5a4f50-187e-4477-acb5-863c7ce02969@m31g2000yqb.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <vr4an.150013$uH1.1193@newsfe25.iad>`

```
On Feb 3, 1:37 am, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> SomeGuy wrote:
> > On Feb 2, 7:18 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
…[4 more quoted lines elided]…
>

Seeing as another thread has brought up soundex, shoulsd the spell
checkers come up with Aligator or LGTR ?
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-03T04:01:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com>`

```
On Feb 2, 9:11 pm, SomeGuy <jimgr...@nc.rr.com> wrote:
> On Feb 2, 7:18 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>
…[47 more quoted lines elided]…
> - Show quoted text -

The same way that I went about guessing the contents of a VDF (Visual
Data Flex) file: look at the reports or screens produced/used and tie
their contents to the data in the file. It takes a bit of brain
processing and is not guaranteed to be 100% foolproof especially if
you don't know the data formats available to the database.

If you don't have the file layouts and probably you don't have report
or screen shots then you probably won't be able to resolve the issue.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** SomeGuy <jimgreen@nc.rr.com>
- **Date:** 2010-02-03T08:16:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cc38566d-b087-4677-bc93-255fe937b809@b2g2000yqi.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com>`

```
On Feb 3, 7:01 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On Feb 2, 9:11 pm, SomeGuy <jimgr...@nc.rr.com> wrote:
>
…[56 more quoted lines elided]…
> or screen shots then you probably won't be able to resolve the issue.

We do have screen shots and output, but I can't imagine that approach
would be economical for this project.

Jim
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-03T09:54:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eca9974-d892-44e4-88ee-dbfaa1076422@s12g2000yqj.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com> <cc38566d-b087-4677-bc93-255fe937b809@b2g2000yqi.googlegroups.com>`

```
On Feb 3, 4:16 pm, SomeGuy <jimgr...@nc.rr.com> wrote:
> On Feb 3, 7:01 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>
…[64 more quoted lines elided]…
>

It worked for me on a project with about 8 database files. It was a
right pain as the compression of the data resulted in rubbish
characters in the data stream. I was faced with a lot of manual
editing.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-02-04T11:02:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hker7g1n4m@news1.newsguy.com>`
- **In-Reply-To:** `<a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com>`

```
Alistair wrote:
> 
> The same way that I went about guessing the contents of a VDF (Visual
…[6 more quoted lines elided]…
> or screen shots then you probably won't be able to resolve the issue.

In other words, this is a forensic exercise. It's impossible to
reconstruct the data format with guaranteed complete accuracy in the
general case, and difficult in many specific cases. You'd need to
perform a cost/benefit analysis to determine how much effort is
reasonable to expend on it.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-05T06:45:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ab8a062b-29ba-4ba9-bd68-8d4ede2783a6@l19g2000yqb.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com> <hker7g1n4m@news1.newsguy.com>`

```
On Feb 4, 4:02 pm, Michael Wojcik <mwoj...@newsguy.com> wrote:
> Alistair wrote:
>
…[14 more quoted lines elided]…
>

The application of a cost benefit analysis is quite a good idea as I
found the effort excessive (but I had very little choice in the
matter).

I think SOMEGUY is banging his head against a brick wall (ce taper la
tete contre le mur as they say in Germany) without the copylibs.
```

###### ↳ ↳ ↳ Re: Help me identify a Cobol database

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2010-02-05T10:00:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hkhmv40vp6@news3.newsguy.com>`
- **In-Reply-To:** `<ab8a062b-29ba-4ba9-bd68-8d4ede2783a6@l19g2000yqb.googlegroups.com>`
- **References:** `<b40fdfcc-d80f-4b3e-912a-6c56f313e0b1@r6g2000yqn.googlegroups.com> <f0c29504-4002-4684-9456-3dc2e053ea5b@q2g2000pre.googlegroups.com> <a5f0a855-0dea-4801-8c62-421691e70d8b@b2g2000yqi.googlegroups.com> <920ae29b-af21-40d7-ac29-9726fb7f03c6@a1g2000vbl.googlegroups.com> <a7f1f637-57ca-47f5-9120-2ae323d0e62c@z26g2000yqm.googlegroups.com> <hker7g1n4m@news1.newsguy.com> <ab8a062b-29ba-4ba9-bd68-8d4ede2783a6@l19g2000yqb.googlegroups.com>`

```
Alistair wrote:
> On Feb 4, 4:02 pm, Michael Wojcik <mwoj...@newsguy.com> wrote:
>> Alistair wrote:
…[12 more quoted lines elided]…
> matter).

And that may be the case for the OP here, too. Of course, having
"little choice" should be considered a benefit, in the cost/benefit
analysis - that is, avoiding the consequences (whatever they may be)
of not doing the job compensates for the effort.

> I think SOMEGUY is banging his head against a brick wall (ce taper la
> tete contre le mur as they say in Germany) without the copylibs.

Certainly it makes the problem much worse. Sometimes the record
structure can be reconstructed by comparing known data to the file
contents - at *this* offset we have a last name, and here we have an
account number, etc. But it may be necessary to follow the execution
of a program that uses the file to determine what individual fields
correspond to.

We see a lot of this sort of thing in security research, as
researchers often have to deal with undocumented interfaces, security
by obscurity, program state at random points in its execution, and
code in object form only. If you read vulnerability disclosure
research, for example, you'll see it's quite typical in the field to
determine data formats by tracing program execution. Not everyone's
cup of tea.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
