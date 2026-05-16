[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Non-DISPLAY numeric data in files

_26 messages · 12 participants · 2004-08_

---

### Non-DISPLAY numeric data in files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-01T00:52:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net>`

```
(Follow-up on another thread)

I am not doing production application development or maintenance today - nor am
I working for a software vendor.  Having said that, it is my impression that
most (not all - but a LARGE number) of production "large institution" mission
critical files still include non-DISPLAY numeric data (e.g. Binary,
Packed-Decimal, and to a VERY limited degree floating-point).  My experience
(with large institutions) was primarily IBM mainframe - and sites "emulating"
IBM mainframes.  Furthermore, how much of this is true of Hierarchical (e.g.
IMS) or Relational (e.g. DB2) database, I am less certain - although, again, my
experience was that this type of data was VERY common.

Experience:

1) While working for IBM mainframe banking and utilities, I saw that almost ALL
"file" numeric data was stored in "COMP-3" (i.e. Packed-Decimal) data.  There
was significant amounts of Binary data as well - especially data (in files)
shared among, COBOL, PL/I and Assembler (later also C/C++).

2) When working for Micro Focus in their "mainframe compatibility" efforts
(targeted at IBM mainframes), the ability to "move" files from the mainframe to
workstations (PC & Unix) with conversion of EBCDIC to ASCII for "character" data
while LEAVING COMP-? data "alone" was something that EVERY mainframe shop that I
worked with wanted.

3) During Y2K "problem solving" I was SHOCKED by the number of files that I
encountered that had
     Pic 9(6) COMP-3
fields in them - much less
     Pic 9(6) COMP
fields.  (The first was a REALLY ugly format on IBM mainframes, and the latter
was only a little better).

As such fields were never (or almost never) used in "computations" - it really
did surprise me how common this was.

   ***

Bottom-Line:
  I won't speak for anyone else's experiences or impressions, but mine is that
in "large <IBM> institutions" the use of non-DISPLAY numeric fields is still
   - widely used (in existing files and applications)
  - widely "added" (in new application design and development)

Whether this is "over-used" in places where in need not be used, is something
that I think only the "data designers" for a specific business can answer.
```

#### ↳ Re: Non-DISPLAY numeric data in files

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-01T14:03:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410ce25f.38658673@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>(Follow-up on another thread)
>
…[8 more quoted lines elided]…
>experience was that this type of data was VERY common.

In my experience, that was true twenty years ago, when VSAM files were the norm.
Now,  in large Unix shops, data is all in databases. The only traditional data
files are for interface. 

I worked at one SMALL shop where Cobol indexed files were used. It was a one man
shop having no technology oversight from its large parent.

>2) When working for Micro Focus in their "mainframe compatibility" efforts
>(targeted at IBM mainframes), the ability to "move" files from the mainframe to
>workstations (PC & Unix) with conversion of EBCDIC to ASCII for "character"
>data while LEAVING COMP-? data "alone" was something that EVERY mainframe shop
>that I worked with wanted.

If they have to go through a conversion, they might as well go to database.
Perhaps that explains the absence of traditional files in Unix shops. They never
want to go through THAT again.

>3) During Y2K "problem solving" I was SHOCKED by the number of files that I
>encountered that had
…[4 more quoted lines elided]…
>was only a little better).

Uglier are dates in databases as INTEGER rather than DATE, sometimes with a two
digit year. Worst is using three tiny integers. Why? Because it takes three
bytes of memory rather than four or six or eight.

I worked on one mainframe flat-file system where year was added as an
afterthought. It was at the end of the record, far from month and day. The
company couldn't understand why off-the-shelf Y2K solutions couldn't handle that
format.

>As such fields were never (or almost never) used in "computations" - it really
>did surprise me how common this was.

When asked why, they say it is "efficient".
```

#### ↳ Re: Non-DISPLAY numeric data in files

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-08-02T12:19:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2n7eukFu3f00U1@uni-berlin.de>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net>`

```
While not stating that this is a good idea, I can certainly state that the
majority of numeric fields that our shop has in both VSAM files and DL/I
databases are defined as USAGE COMP-3.  Not only that, but our numeric keys
(account numbers et al) are also defined this way.  Of course most of these
files/databases are 20+ years old, but I can pretty much guarantee you that
any new one created today will have the same characteristics.  That's just
what we're all used to.

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 7/31/2004 6:52:59 PM >>>
(Follow-up on another thread)

I am not doing production application development or maintenance today - nor
am
I working for a software vendor.  Having said that, it is my impression
that
most (not all - but a LARGE number) of production "large institution"
mission
critical files still include non-DISPLAY numeric data (e.g. Binary,
Packed-Decimal, and to a VERY limited degree floating-point).  My
experience
(with large institutions) was primarily IBM mainframe - and sites
"emulating"
IBM mainframes.  Furthermore, how much of this is true of Hierarchical
(e.g.
IMS) or Relational (e.g. DB2) database, I am less certain - although, again,
my
experience was that this type of data was VERY common.

Experience:

1) While working for IBM mainframe banking and utilities, I saw that almost
ALL
"file" numeric data was stored in "COMP-3" (i.e. Packed-Decimal) data. 
There
was significant amounts of Binary data as well - especially data (in files)
shared among, COBOL, PL/I and Assembler (later also C/C++).

2) When working for Micro Focus in their "mainframe compatibility" efforts
(targeted at IBM mainframes), the ability to "move" files from the mainframe
to
workstations (PC & Unix) with conversion of EBCDIC to ASCII for "character"
data
while LEAVING COMP-? data "alone" was something that EVERY mainframe shop
that I
worked with wanted.

3) During Y2K "problem solving" I was SHOCKED by the number of files that I
encountered that had
     Pic 9(6) COMP-3
fields in them - much less
     Pic 9(6) COMP
fields.  (The first was a REALLY ugly format on IBM mainframes, and the
latter
was only a little better).

As such fields were never (or almost never) used in "computations" - it
really
did surprise me how common this was.

   ***

Bottom-Line:
  I won't speak for anyone else's experiences or impressions, but mine is
that
in "large <IBM> institutions" the use of non-DISPLAY numeric fields is
still
   - widely used (in existing files and applications)
  - widely "added" (in new application design and development)

Whether this is "over-used" in places where in need not be used, is
something
that I think only the "data designers" for a specific business can answer.
```

#### ↳ Re: Non-DISPLAY numeric data in files

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-08-02T21:47:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p9tg0ph61bggsjqfqskv6jbcp95oqh7aa@4ax.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net>`

```
On Sun, 01 Aug 2004 00:52:59 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>(Follow-up on another thread)
>
…[43 more quoted lines elided]…
>that I think only the "data designers" for a specific business can answer.

As a reseller of a main brand of COBOL in Portugal I deal with many
customers, both small and medium.

I also work for some biggish companies (5000+ employees) with AS400
mainly.

All of them so far have always used COMP-3 with numeric fields on
files. This for both new and old code.

The reasong behind this on the PC side was mainly space related. On
mainframe/as400 side has to do with the fact that DB2 was used in all
my customers and this was the default.

Lack of use of COMP-3 was only visible on newbies that were unware of
itï¿½s existence, and was always corrected by the QAï¿½s.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Non-DISPLAY numeric data in files

- **From:** james8049 <james8049.1agvpl@mail.codecomments.com>
- **Date:** 2004-08-04T12:40:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net>`

```
And why exactly is "PIC 9(6) Comp-3" so ugly.

Comp-3 packed decimal is implemented very efficiently in hardware on
IBM mainframes.
While not as fast as binary for integer arithmatic it is much faster
for fixed point, and the fact that all the pacjed decimal instructions
are storage to storage makes it easier for the compiler to optimise and
reduces "register thrasing  ".

The only dubious thing in terms of efficiency is it would be better
stored as "pic s9(7) comp-3" as the unused nibble must be truncated and
the sign zapped to unsign at the end of every operation. 

And before anyone starts going on about portabilty and standards -- if
mainframe cobol programs had to take the performance hit involved in
using portable "display" numerics and no IBM extensions and
enhancements then the language would have been dumped twenty years ago
for something that was efficient. The problem is with the COBOL
standard and standards process and not with any given compiler writers
implentation.
```

##### ↳ ↳ Re: Non-DISPLAY numeric data in files

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-04T18:07:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<411109ed.310970740@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com>`

```
Robert Wagner<robert.deletethis@wagner.net> wrote:

>When asked why, they say it is "efficient".

james8049 <james8049.1agvpl@mail.codecomments.com> wrote:

>Comp-3 packed decimal is implemented very efficiently in hardware on
>IBM mainframes.

See .. I was right!

>While not as fast as binary for integer arithmatic it is much faster
>for fixed point,

You say 'add 1 to foo' is fast for this:
01  foo binary pic s9(9).
but slow for this:
01  foo binary pic s9(7)v9(2).

How can that be? Generated code is identical. The only difference is the literal
being added. 

> and the fact that all the packed decimal instructions
>are storage to storage makes it easier for the compiler to optimize and
>reduces "register thrashing  ".

I thought optimization worked by avoiding memory access. How can the compiler
optimize instructions that _require_ three memory accesses per.

>And before anyone starts going on about portabilty and standards -- if
>mainframe cobol programs had to take the performance hit involved in
>using portable "display" numerics and no IBM extensions and
>enhancements then the language would have been dumped twenty years ago
>for something that was efficient.

Did all that efficiency save enough to pay for the $200B hit it caused?

The cost is about $5M per US IBM mainframe ($100B/20K) -- enough to buy two
additional mainframes. Would converting display numbers have caused it to run at
1/3 speed?
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-04T18:23:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cer9j9$ltv$1@peabody.colorado.edu>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net>`

```

On  4-Aug-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:

> Did all that efficiency save enough to pay for the $200B hit it caused?
>
> The cost is about $5M per US IBM mainframe ($100B/20K) -- enough to buy two
> additional mainframes. Would converting display numbers have caused it to run
> at 1/3 speed?

You gotta make a profit in 1970 or else 2000 doesn't matter.

And as a programmer, I needed to follow management's dictates either way.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T06:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4111ce1a.361198803@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <cer9j9$ltv$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On  4-Aug-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:
>
…[8 more quoted lines elided]…
>And as a programmer, I needed to follow management's dictates either way.

I've described how I ran an IT shop that cost 1/5 the industry average. I didn't
save money with nickel-and-dime optimization; I did it with clean programming
style. 

After rewriting thousands of programs from what I call Corporate Style to good
style, I found the *average* run-time decreased by 40% and the average source
program size was half. I was expecting maybe 10-20%. Finding that 50% of typical
code is fuzzy thinking took me by surprise.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T05:12:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cestlq$9r1$1@panix5.panix.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <411109ed.310970740@news.optonline.net> <cer9j9$ltv$1@peabody.colorado.edu> <4111ce1a.361198803@news.optonline.net>`

```
In article <4111ce1a.361198803@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>"Howard Brazee" <howard@brazee.net> wrote:
>
…[14 more quoted lines elided]…
>style. 

Mr Wagner, hasn't it already been determined that the company in question 
had fewer programmers than similar shops when you walked in the door?

DD
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T14:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<411242f7.391119987@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <411109ed.310970740@news.optonline.net> <cer9j9$ltv$1@peabody.colorado.edu> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <4111ce1a.361198803@news.optonline.net>,
>Robert Wagner <robert.deletethis@wagner.net> wrote:
…[7 more quoted lines elided]…
>>>> additional mainframes. Would converting display numbers have caused it to
run
>>>> at 1/3 speed?
>>>
…[4 more quoted lines elided]…
>>I've described how I ran an IT shop that cost 1/5 the industry average. I
didn't
>>save money with nickel-and-dime optimization; I did it with clean programming
>>style. 
>
>Mr Wagner, hasn't it already been determined that the company in question 
>had fewer programmers than similar shops when you walked in the door?

It was on the brink of bankruptcy. Every expense had been cut to the bone. I
increased the programming staff from 2 to 6. When I left, 7 years later, my
replacement increased the staff to about 30.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T11:01:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ceti42$7tb$1@panix5.panix.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com> <411242f7.391119987@news.optonline.net>`

```
In article <411242f7.391119987@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
>>In article <4111ce1a.361198803@news.optonline.net>,
>>Robert Wagner <robert.deletethis@wagner.net> wrote:

[snip]

>>>I've described how I ran an IT shop that cost 1/5 the industry average. I didn't
>>>save money with nickel-and-dime optimization; I did it with clean programming
…[5 more quoted lines elided]…
>It was on the brink of bankruptcy.

'The brink of bankruptcy', Mr Wagner, is not numerically quantifiable.  
The amount of business that it did and the number of programmers which 
sustained this amount of business both are.  The shop was still in 
business and doing all its processing with fewer programmers when you 
walked in the door.

>Every expense had been cut to the bone.

How nice that they could still afford your services.

>I
>increased the programming staff from 2 to 6. When I left, 7 years later, my
>replacement increased the staff to about 30. 

Some people can shape clay into statues and vases, Mr Wagner, and some can 
only shape it into irregular lumps.

DD
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 8)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T16:34:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41125390.395370102@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com> <411242f7.391119987@news.optonline.net> <ceti42$7tb$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <411242f7.391119987@news.optonline.net>,
>Robert Wagner <robert.deletethis@wagner.net> wrote:

>>>Mr Wagner, hasn't it already been determined that the company in question 
>>>had fewer programmers than similar shops when you walked in the door?
…[3 more quoted lines elided]…
>'The brink of bankruptcy', Mr Wagner, is not numerically quantifiable.  

Sure it is. When liabilities > assets, the company is bankrupt.

>>Every expense had been cut to the bone.
>
>How nice that they could still afford your services.

Thanks to cash infusion from new owners.

>>I increased the programming staff from 2 to 6. When I left, 7 years later, my
>>replacement increased the staff to about 30. 
>
>Some people can shape clay into statues and vases, Mr Wagner, and some can 
>only shape it into irregular lumps.

Thank you.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T12:48:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetodb$3eh$1@panix5.panix.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <411242f7.391119987@news.optonline.net> <ceti42$7tb$1@panix5.panix.com> <41125390.395370102@news.optonline.net>`

```
In article <41125390.395370102@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[10 more quoted lines elided]…
>Sure it is. When liabilities > assets, the company is bankrupt.

That defines 'bankruptcy', Mr Wagner, not its brink.... what is the 
'brink' of 'greater than'?

>
>>>Every expense had been cut to the bone.
…[3 more quoted lines elided]…
>Thanks to cash infusion from new owners.

For whatever reason, it is still... how nice.

>
>>>I increased the programming staff from 2 to 6. When I left, 7 years later, my
…[5 more quoted lines elided]…
>Thank you.

No gratitude is necessary for a simple statement of fact, Mr Wagner... but 
if I'm in need of such I remember to mention that pure water at sea level 
boils at 100 Centigrade, give-or-take a hair.

DD
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-05T17:24:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetqge$27r$1@peabody.colorado.edu>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com> <411242f7.391119987@news.optonline.net> <ceti42$7tb$1@panix5.panix.com> <41125390.395370102@news.optonline.net>`

```

On  5-Aug-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:

> Sure it is. When liabilities > assets, the company is bankrupt.

Not necessarily.  I want to start a company.  I borrow some money and
immediately spend some on a non-refundable deposit on an office.   I have a plan
to increase cash flow to keep working.   Hopefully, I will soon have enough
income to pay the interest on my debt.  It is only after this becomes a lost
cause that the company is bankrupt.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 10)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T23:13:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4112bec0.422814587@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com> <411242f7.391119987@news.optonline.net> <ceti42$7tb$1@panix5.panix.com> <41125390.395370102@news.optonline.net> <cetqge$27r$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  5-Aug-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>immediately spend some on a non-refundable deposit on an office.   I have a
plan
>to increase cash flow to keep working.   Hopefully, I will soon have enough
>income to pay the interest on my debt.  It is only after this becomes a lost
>cause that the company is bankrupt.

Your startup cannot borrow money; the loan is on your personal credit. 
The non-refundable deposit is an asset under the 'ongoing business' precept of
GAAP. 

The company's books look like this:

Assets
Cash     5,000
Office Deposit 5,000

Capital
Owner's Equity 10,000

Your personal books look like this:

Assets
Investsment in startup 10,000

Liabilities
Loan  10,000

Neither entity is bankrupt.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T15:15:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408051415.48203834@posting.google.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <4111ce1a.361198803@news.optonline.net> <cestlq$9r1$1@panix5.panix.com> <411242f7.391119987@news.optonline.net> <ceti42$7tb$1@panix5.panix.com> <41125390.395370102@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> 
> Sure it is. When liabilities > assets, the company is bankrupt.

No, that is not true.  If, for example, there is sufficient cash flow
to meet required payments then they need not be bankrupt.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-04T18:06:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xOWdnYjo2J2c8YzcRVn-hw@giganews.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net>`

```
Robert Wagner wrote:

>
> How can that be? Generated code is identical. The only difference is
…[8 more quoted lines elided]…
> per.

I promise:

Load Register 1
Load Register 2
Add Register 1, 2 then
Store Register 1

Is WAY faster than Add Storage - even if storage is packed decimal and
you're using Add Packed. If each of the register functions above take 2 usec
each, the storage-to-storage operation takes on the order of 50-100 usec.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-04T19:00:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408041800.5ca87b89@posting.google.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 


> Did all that efficiency save enough to pay for the $200B hit it caused?

The $200b is a completely fictional figure dragged out of someone's
arse, it has no meaning in reality.
 
> The cost is about $5M per US IBM mainframe ($100B/20K) -- enough to buy two
> additional mainframes. Would converting display numbers have caused it to run at
> 1/3 speed?

That is completely incompetent misuse of statistics.  It is like
taking half the estimated cost of all road accidents and dividing by
the number of Mack Trucks. In fact that is exactly what your
'calculation' was. That figure would be enough to cover all Mack
Trucks in pillows.

The cost of $200B, or even half of it, even if it was a real cost, was
not paid out by computer departments, or was not even necessarily a
cost to companies that owned computers.

There may have some small amount of cost associated with reprogramming
and converting files, in the main it was done with existing staff and
equipment and thus merely represented existing cost, and _not_ extra
cost.  The only consequence was that other projects were delayed, or,
more likely, were not scheduled to be worked on in that time frame.

Putting it another way: If you are so concerned about file formats
then why haven't you got 'sign separate leading' in all your file
definitions ?
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T07:55:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4111dd7c.365137242@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[4 more quoted lines elided]…
>cost to companies that owned computers.

In 1998-99, the net was awash with ads for Cobol programmers making up to $75/hr
for Y2K 'remediation'. I took the bait and have been a contractor since. 

My first contract, at Sears, was indeed pure Y2K. We fixed a payroll system
written in assembly language that would have failed 1.5 years before the end of
the century. Issues were 'next review date' and 'next salary increase'. 

The system was replaced by PeopleSoft in late 1999. Y2K fixes to the old system
cost the company several million. 

Merrill Lynch paid $800M to 'remediate' all their systems. The effort involved
hundreds of contractors, not employees. I saw the evidence of their work in the
source code.

>There may have some small amount of cost associated with reprogramming
>and converting files, in the main it was done with existing staff and
…[6 more quoted lines elided]…
>definitions ?

I don't have file definitions; I'm 100% database.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T15:04:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408051404.d85c021@posting.google.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <4111dd7c.365137242@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> My first contract, at Sears, was indeed pure Y2K. We fixed a payroll system
> written in assembly language 

So what part of that is attributable to _Cobol_ programmers ?

> The system was replaced by PeopleSoft in late 1999. Y2K fixes to the old
> system cost the company several million. 

So, basically, you failed.

> Merrill Lynch paid $800M to 'remediate' all their systems. 

"""" ------------------
Merrill Lynch is the most famous stock brokerage firm in the U.S. It
has budgeted over half a billion dollars to get compliant. It still
had $157 million left to spend as of late March.

As of April, it was 99.7% finished with its y2k project, even though
it still had $157 million left to spend. This is a very precise
number. I guess they are way under budget and ahead of schedule.
------------------ """

It seems that your figure is just another one pulled out of someones
arse.

Also the project was not just about mainframes.  It also required PCs
to be replaced where their BIOSes did not recognise 2000 dates and
reverted to 1980 and replacement of Win95.  In many cases Y2K also
required cash registers to be replaced, and paper forms with 19__.

There is no doubt that there was a large amount spent on Y2K, but
dividing by the number of mainframes is incompetent misuse of
statistics.

Merril Lynch also claimed that there was vast overspending on Y2K:

""" -----------------------
Consumers are set to reap big benefits from lower prices as a result
of the millennium bug, but shareholders will lose out as earnings of
many major companies fall, according to a report released yesterday.

A drop in prices due to improved technology will be a major side
effect of improved computer systems. Bank customers in particular will
reap rewards through lower cost loans and other transactions. . . .

Head of research at Merrill Lynch, Mr Michael Brown, said: "The
surging capital expenditure will lead to ... more cost efficiencies.
The significant over-expenditure will lead to a risk of deflation."
Deflation, while bad for company earnings, means lower prices for
customers. . . .
---------------- """

No one added up all these savings as a counter to the alleged $200B.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-06T00:27:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4112cf88.427110349@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <4111dd7c.365137242@news.optonline.net> <217e491a.0408051404.d85c021@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote
>
…[3 more quoted lines elided]…
>So what part of that is attributable to _Cobol_ programmers ?

The files were 'aged' for testing by a Cobol program I wrote. It added one year
to all dates. 

>> The system was replaced by PeopleSoft in late 1999. Y2K fixes to the old
>> system cost the company several million. 
>
>So, basically, you failed.

How did you reach that conclusion? The assembly language system functioned
correctly until its planned retirement. 

>> Merrill Lynch paid $800M to 'remediate' all their systems. 
>
…[8 more quoted lines elided]…
>------------------

Good research. I was told by a reliable source that they'd paid $800M to a
single contracting company. I saw that company's signature all over the source
code. 

>Also the project was not just about mainframes.  It also required PCs
>to be replaced where their BIOSes did not recognise 2000 dates and
>reverted to 1980 and replacement of Win95.  In many cases Y2K also
>required cash registers to be replaced, and paper forms with 19__.

It included many Unix and Windows systems. Merrill Lynch doesn't have any cash
registers. 

>Merril Lynch also claimed that there was vast overspending on Y2K:
>
…[16 more quoted lines elided]…
>No one added up all these savings as a counter to the alleged $200B.

That's all speculative. It's been four years and we haven't seen deflation.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T22:52:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408052152.375f546b@posting.google.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <4111dd7c.365137242@news.optonline.net> <217e491a.0408051404.d85c021@posting.google.com> <4112cf88.427110349@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 

> >So what part of that is attributable to _Cobol_ programmers ?
> 
> The files were 'aged' for testing by a Cobol program I wrote. It added one
> year to all dates. 

Maybe the remedy was in part done by Cobol, but the problem wasn't.

> >"""" ------------------
> >Merrill Lynch is the most 

> Good research. 

About 5 seconds with Google.

> I was told by a reliable source that they'd paid $800M to a
> single contracting company. I saw that company's signature all over the source
> code. 

You should revise what you consider to be a 'reliable' source.  This
is not the first time you've posted mis-information that someone 'told
you'.

> It included many Unix and Windows systems. 

Well, exactly, which is why 'dividing by the number of mainframes' is
so flawed, as well as blaming it on Cobol.

> Merrill Lynch doesn't have any cash registers. 

No, what I indicated was that the so called '$200B' included such
things as cash registers and paper forms.

> That's all speculative. 

So was the $200B.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-14T19:16:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RXxTc.15866$5s3.438@fe40.usenetserver.com>`
- **In-Reply-To:** `<217e491a.0408051404.d85c021@posting.google.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <4111dd7c.365137242@news.optonline.net> <217e491a.0408051404.d85c021@posting.google.com>`

```
Richard wrote:

> robert.deletethis@wagner.net (Robert Wagner) wrote
> 
…[12 more quoted lines elided]…
> So, basically, you failed.

Come on now, Richard...  What you snipped was that they were going to 
hit "Y2K" problems in 1998 because of future dates in the program. 
Being replaced by PeopleSoft in late 1999 means that the completed 
program worked in production for a year and a half.

I know you two are like oil and water, but please try not to let your 
contempt for the person make you assume the worst.  Perhaps Sears paid 
to have the "future" dates converted as a run up to Y2K, and then 
decided to go with PeopleSoft for the day-to-day stuff.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 7)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-15T09:58:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fecuh0h3ip83oo712i9ha7nch9cs7qvrpt@4ax.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <4111dd7c.365137242@news.optonline.net> <217e491a.0408051404.d85c021@posting.google.com> <RXxTc.15866$5s3.438@fe40.usenetserver.com>`

```
On Sat, 14 Aug 2004 19:16:50 -0500, LX-i <lxi0007@netscape.net> wrote:

>Come on now, Richard...  What you snipped was that they were going to 
>hit "Y2K" problems in 1998 because of future dates in the program. 
…[6 more quoted lines elided]…
>decided to go with PeopleSoft for the day-to-day stuff.

The target and actual date for PeopleSoft was 6/99. Fixes to the old
system were limited to dates that would fail before 10/99. Examples:
date of next review, date of next raise. There were ten times as many
dates that would have failed in the 21st century.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 4)_

- **From:** james8049 <james8049.1aj9tn@mail.codecomments.com>
- **Date:** 2004-08-05T19:39:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<511c6ef382d3c661db80bbd70c4b62df@news.thenewsgroups.com>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com>`

```
Ah the old Y2K boondoggle!

Point 1. In the 1960s the average application system had a lifespan of
about 5 to 8 years. New hardware was bough purely on the basis of price
performance so changes of supplier were common and even if you stuck
with the same vendor the new hardware/OS  was generally so different
from the old hardware/OS that porting the application was out of the
question.

Point 2. Then came the 360 series. Systems were still designed written
with an expected service life of five to ten years. But system 360
hardware could be upgraded without changeing anything in software (or
very minor tweaks and for drastic upgrades perhaps a recompile) other
manufacturers were forced to follow IBMs lead and upward compatibility
became the norm.

Point 3. The many systems written at this time performed so well that
there was no reason to replace them ever!
There was an awareness of possable date calculation bugs around the
year 2000. But these were generally known and fixes were planned to fit
in with normal maintenance. Until-- 

Point 4. Some shameless and nameless (but you know who you are!)
consultants created a such massive hype that any company spending less
the $50 million dollars on the y2k "problem" risked shareholder
lawsuits. Every line of code was examined scanned and re-exeamind. I
had to do a Y2K certification test on a unix based comms systems which
moved bit did not read messages at a cost of $120,000 although the
whole excercise was pointless and the one area where date problems
could have just been possable was not tested by the "expert" doing the
certification. 

Point 5. To illustrate what a non problem the whole thing was. Italy
had the lowest Y2K spend of any industrialised country. So low that the
boondogling consultants had the state department lobby the Italian
government with scare stories of how everything would fall apart on the
1st Jan 2000. In the event I think some comuters had trouble buying tram
tickets in Milan and got a free ride till 3rd of Jan. 

The whole Y2K scare was a complete non event and all those involved
should be ashamed of themselves.
```

###### ↳ ↳ ↳ Re: Non-DISPLAY numeric data in files

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-06T00:27:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4112d030.427278529@news.optonline.net>`
- **References:** `<L9XOc.4761$9Y6.807@newsread1.news.pas.earthlink.net> <1e7cc7db24652283ee145f9083dc6a8d@news.thenewsgroups.com> <411109ed.310970740@news.optonline.net> <217e491a.0408041800.5ca87b89@posting.google.com> <511c6ef382d3c661db80bbd70c4b62df@news.thenewsgroups.com>`

```
james8049 <james8049.1aj9tn@mail.codecomments.com> wrote:

>The whole Y2K scare was a complete non event and all those involved
>should be ashamed of themselves.

This looks like flame-bait, but what would I know about that?

The Y2K problems I fixed were very real. Some were subtle and couldn't be found
by scanning source. For instance, a date in the key of an indexed file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
