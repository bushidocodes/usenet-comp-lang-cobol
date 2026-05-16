[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Data ----> DB4?

_15 messages · 14 participants · 1999-02 → 1999-03_

---

### COBOL Data ----> DB4?

- **From:** "Kevin Gagnon" <kmg@connectnet.com>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```
I am tasked with TRYING to pull data from an existing COBOL program
(programmer unknown) and convert it to a DB4 database.  I know nothing
about a COBOL data structure.  How is the data stored..... Customers,
Invoices..... etc?


Is it possible to pull data from a COBOL program and map into a DB4
structure??
```

#### ↳ Re: COBOL Data ----> DB4?

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990227102530.15313.00001026@ng-fv1.aol.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```
Kevin Gagnon writes ...

>I am tasked with TRYING to pull data from an existing COBOL program
>(programmer unknown) and convert it to a DB4 database.  I know nothing
…[5 more quoted lines elided]…
>structure??

Sorry, but what is DB4?

Regards,



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: COBOL Data ----> DB4?

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36daadd0.3598902@news.enter.net>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <19990227102530.15313.00001026@ng-fv1.aol.com>`

```
scomstock@aol.com (S Comstock) wrote:

>Kevin Gagnon writes ...
>
…[21 more quoted lines elided]…
>USA


Steve....

My Algebra I teacher in high school would tell you that DB4 is 2
instances of DB2 running simultaneously!

...or would that actually be DB2 * DB2, in which case it would be D
squared times B squared times 4.

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DB6FE4.8989378F@att.net>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <19990227102530.15313.00001026@ng-fv1.aol.com> <36daadd0.3598902@news.enter.net>`

```
Bob Wolfe wrote:
> 
> scomstock@aol.com (S Comstock) wrote:
> 
(snip)
> >Sorry, but what is DB4?
> >
…[15 more quoted lines elided]…
> instances of DB2 running simultaneously!

I thought it was a reference to IBM's long rumoured successor to DB2,
DBAlso.

Bill Lynch :-)

> 
> ...or would that actually be DB2 * DB2, in which case it would be D
…[5 more quoted lines elided]…
> Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: COBOL Data ----> DB4?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b9ask$7gm$2@news-2.news.gte.net>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```
It doesn't matter what the target database is: you must have the source data
record layout.

COBOL does not define what is stored in various files (customers, invoices,
etc); that is defined by the system designer, as are all the field
definitions (is this data alpha? Numeric? Packed? Binary? BCD?).

There is virtually no way to solve your problem - regardless of the target -
unless you can obtain the record layouts of the files. These are called
"File Descriptions" (FD's) in COBOL, and are either in the COBOL source code
of the application or in what is called a "copylib."

If you have the COBOL source, any quality COBOL consultant should be able to
help you extract the data. (He, a quality COBOL consultant, said, with no
hint of modesty).

Without those definitions,you, sir, are well and truly up Fecal Matter Creek
sans paddle.

MCM


Kevin Gagnon wrote in message <01be625b$69edf120$fb02fccc@kevin-laptop>...
>I am tasked with TRYING to pull data from an existing COBOL program
>(programmer unknown) and convert it to a DB4 database.  I know nothing
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL Data ----> DB4?

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b9ghb$3uk@sjx-ixn6.ix.netcom.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net>`

```
I would add one thing to the "attached" note.  You also need to know what
COMPILER was used.  (You also need to be aware that the actual file
description - as it is broken down into specific fields of different types -
may be in the Working-Storage of your program not just under the FD.

Bottom-line:
  You need to have someone who knows COBOL, can find the source code, and
knows what compiler was used.

There is a "trial and error" method if your COBOL program still "runs" and
you can control (via known input) what data is in the output - however, this
is pretty error-prone and fairly unlikely to work well.
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b9rel$d4q$1@fenix.maxitel.pt>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net> <7b9ghb$3uk@sjx-ixn6.ix.netcom.com>`

```
Am I wrong or have already heard about cobol utilities that, given a
Cobol file, can map out its description in terms of size of records,
how many records in the file, how may keys, their starting
positions and lenghts ?
Still, as the posters said, without knowing the cobol trademark and
at least the non-key fields arrangements, it'll be a tough task - but
an impossible one ?
Rgds
P.Cruz

William M. Klein wrote in msg<7b9ghb$3uk@sjx-ixn6.ix.netcom.com>...
>I would add one thing to the "attached" note.  You also need to know what
>COMPILER was used.  (You also need to be aware that the actual file
>description - as it is broken down into specific fields of different
types -
>may be in the Working-Storage of your program not just under the FD.
>Bottom-line:
…[6 more quoted lines elided]…
>data record layout.

>>Without those definitions,you, sir, are well and truly up Fecal Matter
>Creek
…[9 more quoted lines elided]…
>>>structure??
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ba2bh$7ut@dfw-ixnews12.ix.netcom.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net> <7b9ghb$3uk@sjx-ixn6.ix.netcom.com> <7b9rel$d4q$1@fenix.maxitel.pt>`

```
I think that the recent posts have been talking about products that can take
an FD (or Working-Storage record description) and produce a
COBOL-independent "map".  There are also some products (like file-aid) that
take the record description and let you edit the file intelligently.
However, I don't recall (but could be wrong) any product that will "read the
file" and produce a field mapping -  I just don't see how that would be
possible.
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DAAE8A.E644C295@NOSPAMhome.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net> <7b9ghb$3uk@sjx-ixn6.ix.netcom.com> <7b9rel$d4q$1@fenix.maxitel.pt> <7ba2bh$7ut@dfw-ixnews12.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I think that the recent posts have been talking about products that can take
…[5 more quoted lines elided]…
> possible.

It still seems rather silly.  I suppose one could enter a COBOL
formatted description into an IDMS IDD and read it out in its native
format.  But the COBOL format is easier to read and understand.
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yt2C2.11$n12.79@news19.ispnews.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net> <7b9ghb$3uk@sjx-ixn6.ix.netcom.com> <7b9rel$d4q$1@fenix.maxitel.pt>`

```

PAULO CRUZ wrote in message <7b9rel$d4q$1@fenix.maxitel.pt>...
>Am I wrong or have already heard about cobol utilities that, given a
>Cobol file, can map out its description in terms of size of records,
>how many records in the file, how may keys, their starting
>positions and lenghts ?

Some indexed file rebuild utilities supply that type of data. However,
it may not supply information about the composition of the key fields.

>Still, as the posters said, without knowing the cobol trademark and
>at least the non-key fields arrangements, it'll be a tough task - but
>an impossible one ?

The level of difficulty varies inversely with the amount of experience
of the programmer and the programmer's knowledge of the COBOL
implementation and the application. With a starting point of
"know(ing) nothing about COBOL data structure," the task would
appear to be nearly impossible. However, nothing was said of how
much time was available. For example, given four weeks to do work
requiring six months makes a tough task impossible. We know that
some people will not wait forever; hence, impossible seems to be
a reasonable conclusion.

[...]
>William M. Klein wrote in msg<7b9ghb$3uk@sjx-ixn6.ix.netcom.com>...
>>I would add one thing to the "attached" note.  You also need to know what
…[6 more quoted lines elided]…
>>knows what compiler was used.
[...]
>>Michael Mattias wrote in message <7b9ask$7gm$2@news-2.news.gte.net>...
>>>It doesn't matter what the target database is: you must have the source
>>data record layout.
[...]
>>>Kevin Gagnon wrote in message
<01be625b$69edf120$fb02fccc@kevin-laptop>...
>>>>I am tasked with TRYING to pull data from an existing COBOL program
>>>>(programmer unknown) and convert it to a DB4 database.  I know nothing
>>>>about a COBOL data structure.  How is the data stored..... Customers,
>>>>Invoices..... etc?
[...]
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: COBOL Data ----> DB4?

_(reply depth: 4)_

- **From:** Greg Leman <gleman@metagenix.com>
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DCB040.DEF5BEB9@metagenix.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop> <7b9ask$7gm$2@news-2.news.gte.net> <7b9ghb$3uk@sjx-ixn6.ix.netcom.com> <7b9rel$d4q$1@fenix.maxitel.pt>`

```
Not exactly an impossible task.  Not a fun task, but what you need here is a
metadata profiling tool that will allow you to reverse engineer the metadata
from the actual data.  We happen to have such a tool, named MetaRecom (tm).  You
can read all about it at http://www.metagenix.com.

If you have the copybooks, there are plenty of tools that will extract the FDs.
We happen to have one -- Cobol/Stage -- that will also preload the jobs into
DataStage (the industry leading extract, transformation, and load tool).  Just
push a button and you've generated a complete job that will take your legacy
cobol data into almost anything, for instance an ODBC compliant RDBMS.

PAULO CRUZ wrote:

> Am I wrong or have already heard about cobol utilities that, given a
> Cobol file, can map out its description in terms of size of records,
…[34 more quoted lines elided]…
> >>>structure??
```

#### ↳ Re: COBOL Data ----> DB4?

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bd75n$at$1@birch.prod.itd.earthlink.net>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```

Kevin Gagnon wrote in message <01be625b$69edf120$fb02fccc@kevin-laptop>...

>Is it possible to pull data from a COBOL program and map into a DB4
>structure??


If you are trying to decode a FILE without access to the original program
source code (and probably the compiler), you will fail. A COBOL program
has no pre-defined output nor can the output be determined as with a
DB2 file. A COBOL program can read, modify, then output an EXE file,
for example. Or the program can output a simple ASCII text file. No rhyme,
no reason.

If, OTOH, you have the program listing, with a COBOL manual, you should
be able to ferret out the basic file layout. Then, in combination with
knowledge of how the particular compiler represents certain data (mostly
numbers - and there are many ways to represent numbers), you may
be able to deduce the actual innards of the file in question.

Next is the matter of writing a conversion program to massage the
suspect file into the format you desire. This may prove quite messy
for some data types unsupported in the language of the translating
program (i.e., packed decimal).

Altogether, a dark and thankless job.
```

#### ↳ Re: COBOL Data ----> DB4?

- **From:** "Topcoder" <no@spam.com>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bnv1n$9s@bgtnsc01.worldnet.att.net>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```

Kevin Gagnon wrote in message
<01be625b$69edf120$fb02fccc@kevin-laptop>...
>I am tasked with TRYING to pull data from an existing COBOL program
>(programmer unknown) and convert it to a DB4 database.  I know
nothing
>about a COBOL data structure.  How is the data stored.....
Customers,
>Invoices..... etc?
>
>Is it possible to pull data from a COBOL program and map into a DB4
>structure??
>
Let's start with a clarification:  Did you mean IBM's DB2, or
Borland's dBase IV.

Second point:  The first step in any successfull systems analysis
and design project is to define the problem.  So be careful about
using 'expressions like "pull data from an existing COBOL program".
I *think* I know what you mean - you want to convert a database
generated by the COBOL program you referred to to "DB4"?

If so, that will entail writing a conversion program or three.

You should be able to determine the current segment layouts
from the COBOL source code or listing, if available.  If not,
the job will be a little trickier.  You also need to define
the DB2/4? segment layouts.

One solution would be to write COBOL programs to walk the
current Customer, Invoice, Sales Order, etc databases
and create flat files to be input into your new DB load programs.

As you say know nothing about COBOL, you, I am afraid,
are not the ideal candidate for this task.

I am not a contractor, so it is not self-serving for me to suggest
that your company should outsource this task.
```

##### ↳ ↳ Re: COBOL Data ----> DB4?

- **From:** boblorenze@aol.com (BobLorenze)
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990307104416.15819.00005333@ng141.aol.com>`
- **References:** `<7bnv1n$9s@bgtnsc01.worldnet.att.net>`

```
Well, I am a consultant with 20+ years COBOL experience, 10+ years C/C++, and a
past partner at Mathematica, Inc., and am involved in a similar task right now.
It is a formidable, but not impossible task but I agree with the people who say
you need the FDs. Sure makes life a lot easier.
```

#### ↳ Re: COBOL Data ----> DB4?

- **From:** Harry Mason <hcmason@shell5.ba.best.com>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.BSF.4.05.9903121525460.7581-100000@shell5.ba.best.com>`
- **References:** `<01be625b$69edf120$fb02fccc@kevin-laptop>`

```
Hi:
I did something like this years ago.  DB4 was that ashton-tate
then borland database....Nice XBASE language...
Kevin: What you need to do is the following:

Get a copy of the COBOL Source code.
Look at the select assign statements and the FD (file definition)
language details.  Look for the record layout of the file.

Write a cobol program to create a new file delimited by semicolons
(the output fields).

Use the import fucntion of DB4.  Append from or some such...
That is how I would do it.  I could do it in a week.
But I have 14 years experience and can read cobol and immediately
(depending on my mood and how many cups of coffeee)
understand cobol data descriptions...

Email me the record layout and I'll code you a dump program
for a small fee...

Good luck,
Chris "show me the money" mason.

On Sat, 27 Feb 1999, Kevin Gagnon wrote:

> I am tasked with TRYING to pull data from an existing COBOL program
> (programmer unknown) and convert it to a DB4 database.  I know nothing
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
