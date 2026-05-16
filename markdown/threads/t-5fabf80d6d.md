[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-3 Questions

_9 messages · 8 participants · 2006-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COMP-3 Questions

- **From:** info2006@plus-one.com
- **Date:** 2006-09-12T22:43:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```
Hi,

I have two questions on COMP-3 data types when found in COBOL
copybooks:

1.  Is it safe to say there is no difference between a PIC 99V99 COMP-3
and a PIC 99.99 COMP-3 in a copybook?

The first is an implied decimal point and the second normally tells us
the decimal point can be found in the data.  But for PIC 99.99 COMP-3,
should I expect a decimal point to be found in the actual data?  Based
on the documentation I've found so far, I can't seem to get a clear
answer on this one.  If a decimal is expected in the actual data, this
would seem to contradict why someone would use COMP-3's in the first
place.

2.  All COMP-3 data use the last nybble to store the sign for the
number (i.e., C=positive, D=negative, F=unsigned in the actual data).
Does the COBOL copybook need to have an S (like PIC S99 COMP-3) in
order to see a C or D at the end of the data?   Based on what I've
read, the answer seems to be no.

I'm finalizing support for COMP-3 conversion for our +1Copybook
product, in this case, to read in COMP-3 data into the SQL Server
database using BULK INSERT.

Thanks in advance for any help!

John D.
+1 Software Engineering
```

#### ↳ Re: COMP-3 Questions

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-09-12T23:29:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1158128969.094029.12830@i3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```

info2006@plus-one.com wrote:

> 1.  Is it safe to say there is no difference between a PIC 99V99 COMP-3
> and a PIC 99.99 COMP-3 in a copybook?

PIC 99.99 is not numeric, it is edited-numeric. Comp-3 can only be
applied to a numeric field.  What error does your compiler give for
this ?

> The first is an implied decimal point and the second normally tells us
> the decimal point can be found in the data.  But for PIC 99.99 COMP-3,
> should I expect a decimal point to be found in the actual data?

What 4 bit nybble value would you think that a '.' would have ?

> Based
> on the documentation I've found so far, I can't seem to get a clear
> answer on this one.  If a decimal is expected in the actual data, this
> would seem to contradict why someone would use COMP-3's in the first
> place.

> 2.  All COMP-3 data use the last nybble to store the sign for the
> number (i.e., C=positive, D=negative, F=unsigned in the actual data).
> Does the COBOL copybook need to have an S (like PIC S99 COMP-3) in
> order to see a C or D at the end of the data?   Based on what I've
> read, the answer seems to be no.

This is implementation dependent. Some may use the last nybble for a
digit if there is no sign.

What happens in your implementation ?

> I'm finalizing support for COMP-3 conversion for our +1Copybook
> product, in this case, to read in COMP-3 data into the SQL Server
> database using BULK INSERT.
```

##### ↳ ↳ Re: COMP-3 Questions

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-09-13T04:19:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1158146363.165020.198680@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1158128969.094029.12830@i3g2000cwc.googlegroups.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com> <1158128969.094029.12830@i3g2000cwc.googlegroups.com>`

```

Bottom posting

Richard wrote:
> info2006@plus-one.com wrote:
>
…[32 more quoted lines elided]…
> > database using BULK INSERT.

Futher to Richard's posting, it is always a good idea when posting to
indicate the operating system, database and compiler suppliers names
together with the version numbers, etc.

As Richard says, 99.99 Comp-3 is just non-standard code, your compiler
might interpret it as a valid construct, but you would have to refer to
the manual to find out what is understood by it, or worse test it
yourself to find out.  Manuals can usually be downloaded from suppliers
websites, usually for free.

Robert
```

#### ↳ Re: COMP-3 Questions

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-09-13T06:47:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odvfg29aeishlnsp9ushotuphgoncs8slg@4ax.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```
On 12 Sep 2006 22:43:58 -0700, info2006@plus-one.com wrote:

>1.  Is it safe to say there is no difference between a PIC 99V99 COMP-3
>and a PIC 99.99 COMP-3 in a copybook?

Just curious - what system do you have where you can compile PIC 99.99
COMP-3?    Is it packed-decimal?

In systems I've used, the compiler would flag it as illegal.
```

#### ↳ Re: COMP-3 Questions

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-09-13T16:46:38+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ql2gg2pr3q8e9d1q1l75mj8j23hqk6qg8h@4ax.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```
On 12 Sep 2006 22:43:58 -0700 info2006@plus-one.com wrote:

:>I have two questions on COMP-3 data types when found in COBOL
:>copybooks:

:>1.  Is it safe to say there is no difference between a PIC 99V99 COMP-3
:>and a PIC 99.99 COMP-3 in a copybook?

No.

The former may compile successfully, the latter will cause a compiler error.

:>The first is an implied decimal point and the second normally tells us
:>the decimal point can be found in the data.  But for PIC 99.99 COMP-3,
:>should I expect a decimal point to be found in the actual data?  Based
:>on the documentation I've found so far, I can't seem to get a clear
:>answer on this one.  If a decimal is expected in the actual data, this
:>would seem to contradict why someone would use COMP-3's in the first
:>place.

As the program will not compile, the question is irrelevant.

:>2.  All COMP-3 data use the last nybble to store the sign for the
:>number (i.e., C=positive, D=negative, F=unsigned in the actual data).
:>Does the COBOL copybook need to have an S (like PIC S99 COMP-3) in
:>order to see a C or D at the end of the data?   Based on what I've
:>read, the answer seems to be no.

If S is not specified, setting the field individually (and not at a record
level) will force it to have a positive value.

The instantiation of COMP-3 is up to the compiler, but typically you will see
C/D. Unsigned may have F - depends on the compiler..
```

#### ↳ Re: COMP-3 Questions

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-09-13T09:47:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12gg6fifjsi8751@news.supernews.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```
info2006@plus-one.com wrote:
> Hi,
>
…[4 more quoted lines elided]…
> COMP-3 and a PIC 99.99 COMP-3 in a copybook?

No, not safe. There is a great deal of difference. The '.' is an editting 
character and should generate an error in any COBOL compiler. In this 
regard, the decimal place is similar to other editting characters: "," "CR", 
"-", "$", "*", etc. All of which should generate an error. An editting 
character is used when converting a numeric value (something on which 
arithmetic can be done) into something readable by a human (and on which 
arithmetic cannot usually be done, i.e.,  $ + 2 = ? )

> 2.  All COMP-3 data use the last nybble to store the sign for the
> number (i.e., C=positive, D=negative, F=unsigned in the actual data).
> Does the COBOL copybook need to have an S (like PIC S99 COMP-3) in
> order to see a C or D at the end of the data?   Based on what I've
> read, the answer seems to be no.

Not so. First, not all COMP-3 fields use the last nibble - it depends on the 
machine and the compiler. An old Univac machine I once worked on, used one 
byte for each digit plus an additional byte for the sign when the field was 
defined as COMP-3.  Second, I've never heard of the absence of A,B,C,D,E,F 
indicating an unsigned value. Third, the convention (from IBM days) is 
F,A,C,E = positive, B,D = negative.

COMP-3 stuff was originally concieved as an storage economy measure and IBM 
developed circuitry to handle base-10 arithmetic. Today's PCs don't have 
base-10 capability and when a COBOL compiler encounters a COMP-3 field, the 
compiler generates code to convert the COMP-3 data to binary, performs the 
requested arithmetic, and converts the result back to COMP-3 a rendition. In 
other words, COMP-3 continues - at least in the PC world - as a 
backward-compatible artifact.

Yes, the field must contain "S" in order for the field to designated as 
negative. In the absence of the "S," every line of code in which the field 
in question receives data has additional code generated to FORCE the result 
to be positive. You can think of the absence of the "S" as defining the 
field to contain the absolute value.

>
> I'm finalizing support for COMP-3 conversion for our +1Copybook
…[3 more quoted lines elided]…
> Thanks in advance for any help!

You're welcome. Just a reminder: To use a copybook to decode a COMP-3 field, 
it is almost always necessary to understand the platform and compiler for 
which the copybook was originally designed.
```

#### ↳ Re: COMP-3 Questions

- **From:** info2006@plus-one.com
- **Date:** 2006-09-13T22:23:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1158211396.849550.36570@p79g2000cwp.googlegroups.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com>`

```

Hi,

First I just want to thank everyone who responded.  I really do
appreciate sharing your technical prowess in answering my questions
which you certainly did!

Regarding which compiler or what error I was seeing, I'm not using any
COBOL compiler.  We are developing a product where if a customer
receives a data file which is defined by a COBOL copybook, our goal is
to generate everything you need to load this data into a database on
the same day.

Currently our product works for Oracle and SQL Server and we have
customers using it for both databases today.  For Oracle, we generate
the CREATE TABLE script, the SQL*Loader control file, and support
external tables.  For SQL Server, we generate the CREATE TABLE script,
format file, and perform transformations (implied decimal point, signed
data, and ... the reason for asking my questions, soon COMP-3 data).
We also generate pretty comprehensive HTML output.  Another big area
for us is documenting new or existing databases from an application
point of view.  (I'm not advertising, sounds like it, but just want to
let you know what we are up to.  No flames please!)

We don't really need a COBOL compilier to do what our product does.  We
simply read the COBOL copybook and actual data, which are usually
provided by a third party.  We perform a lot of checks and support a
lot of options and configuration files.  Our web site is a bit out of
date to really show you what we have implemented today, but you can get
a pretty good feel for what we are up to by visiting:

         http://www.plus-one.com/SEINFO/seinfo/tables/index.html

On what 4 bit nybble value would you think a '.' would have?  Excellent
question.  I forgot to state this in my original posting, but you are
right, what would you use since a '.' is represented as a 0x2E?

Thanks again for all of your responses!

John D.
+1 Software Engineering
```

##### ↳ ↳ Re: COMP-3 Questions

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-09-14T12:16:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BKbOg.1203$e66.891@newssvr13.news.prodigy.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com> <1158211396.849550.36570@p79g2000cwp.googlegroups.com>`

```
> Regarding which compiler or what error I was seeing, I'm not using any
> COBOL compiler.  We are developing a product where if a customer
> receives a data file which is defined by a COBOL copybook, our goal is
> to generate everything you need to load this data into a database on
> the same day.

Cannot be done without knowing the compiler and/or knowing if the elementary
items are BYTE or WORD aligned.

For one thing, "COMP <anything> is implementor-defined, meaining each
compiler vendor can make "COMP-3" any format he wants. (vs say,
PACKED-DECIMAL or BINARY, which are standard usage clauses).

For another, even with standard usage, vendors may align - or offer
alignment- options which have the net effect of adding "slack" or "pad"
bytes to a record.  Not to mention, the handing of "OCCURS DEPENDING ON" may
be subject to compiler directives.

You can dig up a little more info with these free downloads:
http://www.flexus.com/ftp/cobdata.zip
http://www.flexus.com/ftp/cobfd.zip

> Currently our product works for Oracle and SQL Server ...
>   the SQL*Loader control file...

FWIW, the above free downloads were some of the credited source material for
Jonathan Gennick's O'Reilly publication "Oracle SQL*Loader: the Definitive
Guide."  Good enough for that, should be worth a look for you.
```

##### ↳ ↳ Re: COMP-3 Questions

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-09-14T18:05:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9SgOg.304833$os2.137708@fe06.news.easynews.com>`
- **References:** `<1158126238.554893.285520@i42g2000cwa.googlegroups.com> <1158211396.849550.36570@p79g2000cwp.googlegroups.com>`

```
From several of the things that you have stated, I would say that you PROBABLY 
(currently) support only IBM mainframe compatible COBOL. This means COBOL 
written and compiled on an IBM mainframe (probably MVS, OS/390, z/OS) *or* 
Workstation (PC or Unix) compilers that EMULATE IBM mainframe behavior.

As others have stated, this really, REALLY impacts any COMP-?? USAGEs.  Not only 
the (very common) COMP-3, but also the MUCH less common COMP-1 and COMP-2.  In 
fact, it even impacts PIC X data.  Is the data that you "get in" usually in 
ASCII or EBCDIC?  If EBCDIC, then again, this is PROBABLY (but not necessarily) 
IBM mainframe (or emulator) data.

On the other hand, having looked at your website, it looks as if you are running 
on a PC or Unix environment as you expect ".txt" files. If this is the case, 
then you really, REALY need to know what the usual COBOL compiler is to 
understand the copybook.  MANY data-types are not portable.  Even your 
"assumption" of x"F" "C" and "D" sign-nibbles for COMP-3 fields (when they are 
Packed-Decimal) is far from universal.  What do you currently do with COMP-5 or 
COMP-6 data? How about COMP-X?   Do ;you support both LINE Sequential and RECORD 
sequential copybooks?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
