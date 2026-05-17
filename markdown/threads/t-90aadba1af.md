[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol->C or Linux Compiler

_5 messages · 5 participants · 1994-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Cobol->C or Linux Compiler

- **From:** "ste..." <ua-author-17073942@usenetarchives.gap>
- **Date:** 1994-12-01T03:52:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<786271975snz@stevef.demon.co.uk>`

```
I have programmed in COBOL for many years on both ICL Mainframes and Micros.
I also have programmed in PL/1, C, RTL/2 and at the moment am trying to learn
C++ (another story).

In my opinion a GNU COBOL compiler would be much better than a COBOL to C
translator because :-

a) There are a large number of people who use COBOL daily who have no
desire to re-train in C or, because of their background would probably find
the conversion to C difficult. COBOL is fairly easy to learn and understand
and maintain by people who need not have much in the way of training in
Computing. The Compilers and run time support tend to make things fairly
safe. C on the other hand requires a good deal of knowledge and skill if it
is to be used well and safely. For example we take our brighter Clerical Staff
who understand the business and train them in COBOL and they become productive
some of them have moved to projects using C and have real difficulties;
especially where large suites of programs need to be produced. IMHO GNU COBOL
whilst not as "techie" as C and ADA could have a very widespread user base;
especially if there was a DOS version. There are millions of lines of COBOL
out there.


b) COBOL is one of the most portable languages I know. For many
years I developed code on 8 and 16 bit Micros, transferred the source to the
a mainframe, re-compiled and it usually ran without too much difficulty. Pro
viding the I/O and data typing is sorted out problems can be few. For example
I converted 2 major suites (>15000 lines of code) from an ICL 1900 running
Manual exec to an ICL2957 running VME in 3 weeks. I used DECLARATIVES
to sort out the file handling and converted the PICTURES of some ICL specific
data types and the code affected, really not much else to do. That was 11 years
ago.

Problems will occur with "propriatory" extensions to the language, for example :-

a) Interfaces with DBMS, Data Dictionaries and TP Monitors. I suspect
that most recent COBOL code will use these.


b) Interfaces between COBOL and the Operating System/Networking Software.

I have no Compiler Writing Skills I am afraid so whilst I would love to see
a GNU COBOL unfortunatly I probably cannot help to write one.

Stephen John Farthing
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1994-12-02T10:21:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90aadba1af-p2@usenetarchives.gap>`
- **In-Reply-To:** `<786271975snz@stevef.demon.co.uk>`
- **References:** `<786271975snz@stevef.demon.co.uk>`

```
While it is true that COBOL can be written in a highly portable way, it is
a mis-characterization to think of it as a highly portable language. THe
following major features of COBOL, among others, are entirely implementation
dependent:

COMPUTE verb
Representation of all COMPUTATIONAL items
Representation of signed data items lacking SIGN IS SEPARATE clause

Yes, of course you can program without these, but in practice there are
few COBOL programs that are free of the use of the above (pretty important)
features.

In practice the portability situation is not as bad as one would imagine
from the language definition, because IBM mainframe COBOL in practice
tended to define a more extensive standard. Certainly the implementation
of the Realia COBOL compiler spent a huge amount of time worrying about
being IBM mainframe compatible, not just compatible with the standard, which
would have been MUCH easier.

So I think if you find that COBOL in practice is portable, you are commenting
on the implementations, rather than on the language itself.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-02T10:21:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bne1a$ruo@gnat.cs.nyu.edu>`
- **References:** `<786271975snz@stevef.demon.co.uk>`

```
While it is true that COBOL can be written in a highly portable way, it is
a mis-characterization to think of it as a highly portable language. THe
following major features of COBOL, among others, are entirely implementation
dependent:

   COMPUTE verb
   Representation of all COMPUTATIONAL items
   Representation of signed data items lacking SIGN IS SEPARATE clause

Yes, of course you can program without these, but in practice there are
few COBOL programs that are free of the use of the above (pretty important)
features.

In practice the portability situation is not as bad as one would imagine
from the language definition, because IBM mainframe COBOL in practice 
tended to define a more extensive standard. Certainly the implementation
of the Realia COBOL compiler spent a huge amount of time worrying about
being IBM mainframe compatible, not just compatible with the standard, which
would have been MUCH easier.

So I think if you find that COBOL in practice is portable, you are commenting
on the implementations, rather than on the language itself.
```

##### ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-04T11:50:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0ABJn.9A4@Belgium.EU.net>`
- **References:** `<786271975snz@stevef.demon.co.uk> <3bne1a$ruo@gnat.cs.nyu.edu>`

```
Robert Dewar (dewar@cs.nyu.edu) wrote:
: While it is true that COBOL can be written in a highly portable way, it is
: a mis-characterization to think of it as a highly portable language. 
(...deleted...)
: So I think if you find that COBOL in practice is portable, you are commenting
: on the implementations, rather than on the language itself.

Sorry, Robert, but I gotta disagree.  I have written complex programs, like
editors and code generators, parsers, and query/report systems, in Cobol,
which certainly use COMPUTE and signed numbers, and which run on many Cobol
platforms, including: Vax, Realia, Micro-Focus (MS-DOS and Unix), IBM Cobol
II, IBM VS/Cobol, IBM Cobol/400, DG/MV Cobol, Wang VS Cobol, and Bull DPS7.

The portability of Cobol, like any language, depends on the way you use it.
Know what to avoid and what to encapsulate.  Of course, it may just be a
coincidence that my software runs on all these platforms; however, if a
language encourages portable implementations, that is just the same as it
being a portable language...
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** Albert Ratzlaff R. <74754.1307@CompuServe.COM>
- **Date:** 1994-12-08T13:49:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c72t9$dps$1@mhadg.production.compuserve.com>`
- **References:** `<D0ABJn.9A4@Belgium.EU.net>`

```
1. Name: how about "linc"? (Linc is not COBOL), or xinc or minc
or whatever you like (l -> linux).
2. Apologies: I used the word "easy" in one of my previous 
postings, which evidently was not the right term (I learned 
english years 2 to 11, then moved to South America where I 
switched first to German and then Spanish. I read a lot - ALL the 
computer books are in English - but I only write or talk every 
couple of years). I should have said "feasible". I think it's a 
large project, but no single part of it is too difficult. The 
ugly part is that you have to make a lot of decisions between the 
least worst way to implement something.
3. Objectives: IMO there are two well-defined (and different) 
goals: one is to traslate COBOL to C, and then continue working 
in C; the other is to create a working COBOL 
compiler/interpreter and continue working in COBOL. I would 
imagine that the second choice would appeal to more people, 
because that way they would'nt have to switch languages. But, the 
first choice definitly has its attractives.
4. So, why not decide on a project outline and start working?
First, as has allready been noted, you need a language 
definition (BNF). Second, create the lexical analyzer and the 
grammar parser. I've been playing around with these for a while, 
and I've found out that while _yacc_ (or bison) should be able to 
do the job, _lex_ definitely can not. It needs too much feedback 
from yacc to interpret all of the language constructs correctly,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
