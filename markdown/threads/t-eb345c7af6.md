[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# variable and paragraph naming conventions

_27 messages · 13 participants · 2000-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### variable and paragraph naming conventions

- **From:** "Mayer Goldberg" <gmayer@cs.bgu.ac.il>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
Hello:

I'm having a problem with selecting variable names in cobol. So far, I'm
using cobol-85 so my variable names are all global. After a while, in a
reasonably large program, most of my time is spent on looking up what those
names are. There must be a better way: What useful naming
conventions/practices are there?

Thanks,

Mayer
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3915C7F4.4BE70A0E@worldnet.att.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
Mayer Goldberg wrote:
> 
> Hello:
…[6 more quoted lines elided]…
> 

The shop standards where I work strongly encourage naming all variables
with either a three digit numeric prefix or (in the case of copybooks) a
four-character alphnumeric prefix.

All datanames within the same "01" record must have the same prefix. 
Some people don't care for prefixes, but in my experience it's fairly
useful in helping to keep track of variables and guaranteeing unique
names in large programs.

In the case of copybooks, a prefix might be something like CB01-, which
would mean Customer Billing.  The "01" might indicate a master file. 
Every dataname in that copybook would be prefixed with CB01-.

For datanames not defined in a copybook, we have a naming structure.

100-199  Program switches or flags.  

200-299  Local record layouts (control cards, for example)

300-399  Program literals and constants.  We have a shop standard that
discourages the use of numeric and alphanumeric literals in the
procedure division.  All such constants should be defined in the 300-
area, and should never be modified in the procedure division.

400-499  Program counters and arithmetic work areas.

500-599  Program tables.  With COBOL-85 and higher, you can put VALUE
statements under the occurs clause.  I think that's a good thing to do.

600-699  Program messages.  These will likely have variables that would
be populated at execution time.

700-799  Report record layouts, or in CICS programs we place
redefinitions of BMS maps here.

800-899  General work areas.  Sort of a grab bag.  Subscripts.  Work
areas for transformations.  Sting/Unstring hold areas.

900-999  Record layouts or parameter fields for called subprograms,
abend work areas.

I see a couple of advantages to this general approach.  Once you're used
to it, you can tell a few things about how a variable is used by its
prefix (although you should always have a clear and easily understand
name apart from the prefix).

With almost any text editor, and certainly with ISPF or similar editors,
it's pretty easy to locate a variable you're unsure of, and you will
generally find related fields when you do.

We also use numeric prefixes for paragraph names, generally four-digits
but occasionally five digits.  The advantage here is that you should
always perform down through the program.  If you need to look at the
calling paragraph you can search backwards for its prefix without
knowing the calling paragraph's name.

PROCEDURE DIVISION.
0000-MAINLINE.
    PERFORM 1000-INITIALIZE-THE-PROGRAM
    PERFORM 2000-PROCESS-1-CUSTOMER-RECORD
        UNTIL 88-100-ALL-RECORDS-PROCESSED  
        (note the odd numbering standard for prefixing a condition
name!)
    PERFORM 3000-DISPLAY-FINAL-MESSAGES
    STOP RUN.
1000-INITIALIZE-THE-PROGRAM.
    PERFORM 1100-DISPLAY-START-MESSAGES
    PERFORM 1200-OBTAIN-CONTROL-CARD
    PERFORM 1300-OPEN-THE-FILES
    PERFORM 1400-READ-INITIAL-RECORDS
    PERFORM 1500-LOAD-TABLES

et cetera, ad infinitum.  Note the attempt to describe the heirarchical
structure in the prefix numbers.

Note also that our paragraph naming conventions encourage a paragraph
name to consist of an action verb followed by a direct object.  It's a
lot harder than you might think to come up with a good name for a
paragraph, but it has immense benefits for documentation and for ease of
maintenance by the next programmer.  It's especially hard to think of
good names when you're limited to 30 characters, and the disadvantage to
paragraph name prefixes is that it cuts into that 30-character limit.

With our particular naming scheme (there are, of course, others)
paragraphs that are called from multiple locations are numbered in the
8000-8999 range.  Abend or error handling paragraphs are numbered in the
9000-9999 range.  Otherwise, no paragraph can be performed from more
than one location.  Unless your structure tree is very deep (use wider
numbers) your current paragraph name tells you what the prefix of the
calling paragraph must be.  It's very easy to search backwards to find
the caller.

For multiple use paragraphs you'll have to do "X ALL;F prefix ALL" in
ISPF.

Not everyone likes numbering datanames and paragraphs.  Different shops
may have strict standards or no standards, and enforcement may be rigid
or lackadaisical.

While I am used to this approach where I work, and generally like it
pretty well, there's absolutely no guarantee there isn't a better way to
do it.
```

##### ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3916AD72.AD8AC7E9@iinet.net.au>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <3915C7F4.4BE70A0E@worldnet.att.net>`

```

Arnold Trembley wrote:
> 
> For datanames not defined in a copybook, we have a naming structure.
…[26 more quoted lines elided]…
> 
You are kidding aren't you!
NO other langauge uses this excuse to obfuscate what would otherwise
have been meaningful code.
You are not REQUIRED to do this, only the weight of history is behind it.

The reason for numbering paragraphs was so that they could be found in listings.
A higher numbered paragraph was obviously towards the end of the
program, i.e. towards the back of the listing.

Advanced or not so advanced editors and the online nature of programming
makes this redundant.
As to the numbering scheme above, why not append a noun to the variable
name to say what it is.
e.q. var-FLAG or var-SWITCH, var-LOCAL-RECORD, var-LITERAL, var-COUNTER,
var-TABLE, etc.

Then we know exactly what you programmed without having to remember
obscure naming conventions.
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000508113348.09031.00002088@nso-cc.aol.com>`
- **References:** `<3916AD72.AD8AC7E9@iinet.net.au>`

```
In article <3916AD72.AD8AC7E9@iinet.net.au>, Joseph J Katnic
<josephk@iinet.net.au> writes:

>You are kidding aren't you!
>NO other langauge uses this excuse to obfuscate what would otherwise
>have been meaningful code.
>You are not REQUIRED to do this, only the weight of history is behind it.
>

Noody said it was for obfuscation.  It is for ease of maintenance.  Any
programmer
can jump into the program an identify what the working components are when
there is a well defined standard established and adhered to.
So far as I have been reading, there is no such standard to the OO method.
There are still factions fighting over what is 'the standard'.
Guidelines must be established to make it easier for yourself or the next 
programmer to come back into the program cold and still be functional.
These rules are not that outrageous.  In fact it would make life very easy 
for an outsider to come in an be productive with just a brief overview of
standards.
This is normally a good thing to have when dealing with programs containing 
hundreds to thousands of lines of code.  Anything greater than the 'ideal' one
page
inline perform needs to have some form of structure that can help map the
program
flow by paragraph names and performs without having to 'chase' the flow with
your
editor's search functions.
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f8equ$idu$1@slb3.atl.mindspring.net>`
- **References:** `<3916AD72.AD8AC7E9@iinet.net.au> <20000508113348.09031.00002088@nso-cc.aol.com>`

```
My guess is that this "you've got to be kidding" correspondence is (once
again) a difference between LARGE mainframe shop (with multi-hundred
programmers) versus "single or small" programming staff environment.

It is NOT particularly unusual in a large (100 Plus) COBOL programming shop
to have a (YUCK) hard-copy of a (hopefully) recent compile of a program (this
program is 50,000 lines long - not counting COPY statements - and is part of
a "run" that includes 10-25 programs) and be told by "ye olde manager" (aka
he/she who pays the checks) to "add just this "small" enhancement (two new
report fields and one new subtotal) to the program by the weekend.  This, for
a programmer who has never SEEN this program before (but does know one of the
others in the "application suite").

Folks,
  For you people who "program in your own small worlds,"  the life of a COBOL
programmer in a LARGE mainframe shop *does* requires "standards" that may
seem strange to you - but they really, REALLY, do work.
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 5)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3918227D.829D8021@iinet.net.au>`
- **References:** `<3916AD72.AD8AC7E9@iinet.net.au> <20000508113348.09031.00002088@nso-cc.aol.com> <8f8equ$idu$1@slb3.atl.mindspring.net>`

```

"William M. Klein" wrote:
> 
> My guess is that this "you've got to be kidding" correspondence is (once
> again) a difference between LARGE mainframe shop (with multi-hundred
> programmers) versus "single or small" programming staff environment.
> 
Wrongo,
Can't mention where I work, but we have (conservatively) 2M LOC.
Standards, you want standards, well how about these
1. NO SINGLE PROGRAM GREATER THAN 2K LOC (approx.)
2. ALL variables follow Smalltalk standards,
   e.g. aCounter, theContentsofaTruck, etc. Size is not limited.
3. Programs dynamically call other programs.
4. The usual structure standards (IF etc.)
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 5)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fa43m$bp9$1@news.inet.tele.dk>`
- **References:** `<3916AD72.AD8AC7E9@iinet.net.au> <20000508113348.09031.00002088@nso-cc.aol.com> <8f8equ$idu$1@slb3.atl.mindspring.net>`

```
Happily I can announce that my naming conventions goes for my mainframe
systems too.

The past 5 years I've been fooling arround with a mainframe system. At the
beginning we were 195 programmers, 2 years after 144 and today we are only
48 left. We are making further development and in a few months we will
expand again to 100+ because of some extra development caused by the EURO.

The system is used by 73 banks and we handle all selling/buying of bonds and
stocks for the banks customers.

Every night 4,482 jobs are run (4,100 are cobol programs and the rest is
sort and iebgener and so on). The system is based upon 640 DB2 tables 2340
CICS programs and 4100 batchprograms.

If someone came to us and told us to put numbers or silly char-combinations
to our well defined and well analyzed data definitions, we would shoot
him/her. After that we would hang him/her and finally we would burn down the
compay who sent that person.

When we refer to ACCOUNT-NO, we know exactly what it is, and  we know
exactly which programs and tables that field is used in. If we want to
change the format of ACCOUNT-NO, Our source code control system will tell us
what to do.

Regards
Ib


William M. Klein skrev i meddelelsen
<8f8equ$idu$1@slb3.atl.mindspring.net>...
>My guess is that this "you've got to be kidding" correspondence is (once
>again) a difference between LARGE mainframe shop (with multi-hundred
…[3 more quoted lines elided]…
>to have a (YUCK) hard-copy of a (hopefully) recent compile of a program
(this
>program is 50,000 lines long - not counting COPY statements - and is part
of
>a "run" that includes 10-25 programs) and be told by "ye olde manager" (aka
>he/she who pays the checks) to "add just this "small" enhancement (two new
>report fields and one new subtotal) to the program by the weekend.  This,
for
>a programmer who has never SEEN this program before (but does know one of
the
>others in the "application suite").
>
>Folks,
>  For you people who "program in your own small worlds,"  the life of a
COBOL
>programmer in a LARGE mainframe shop *does* requires "standards" that may
>seem strange to you - but they really, REALLY, do work.
…[12 more quoted lines elided]…
>> >You are not REQUIRED to do this, only the weight of history is behind
it.
>> >
>>
>> Noody said it was for obfuscation.  It is for ease of maintenance.  Any
>> programmer
>> can jump into the program an identify what the working components are
when
>> there is a well defined standard established and adhered to.
>> So far as I have been reading, there is no such standard to the OO
method.
>> There are still factions fighting over what is 'the standard'.
>> Guidelines must be established to make it easier for yourself or the next
>> programmer to come back into the program cold and still be functional.
>> These rules are not that outrageous.  In fact it would make life very
easy
>> for an outsider to come in an be productive with just a brief overview of
>> standards.
>> This is normally a good thing to have when dealing with programs
containing
>> hundreds to thousands of lines of code.  Anything greater than the
'ideal'
>one
>> page
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3916C46F.49E9D2A8@cusys.edu>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <3915C7F4.4BE70A0E@worldnet.att.net>`

```
Oh, one thing to consider when setting naming conventions.

Know how copy replacing works if you use COBOL copy members, and how
your data dictionary works if you are using data dictionary copies. 
Don't make it difficult to modify your names.


I forgot you wanted paragraph naming conventions.  I generally have
something like this:

PROCEDURE DIVISION.
0000-MAIN.
    PERFORM 0100-INITIALIZE.
    PERFORM 1000-PROCESS-BILL-RECORDS UNTIL SW-BILL-RECORD-EOF.
    PERFORM 9000-DISPLAY-TOTALS.
    CLOSE BILL-FILE.
    CLOSE PRINT-FILE.
    GOBACK.
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f4rl202k2@enews4.newsguy.com>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
As a start, prefix or suffix the names of grouped variables:

01  HOLDING-TBL-GRP.
    05  HOLDING-TBL-FIELD1  PIC X(2).
    05  HOLDING-TBL-FIELD2  PIC X(3).

For files, I like this approach:
SELECT MASTER-FILE   ASSIGN MYDDMSTR.

FD  MASTER-FILE
    BLOCK 0
    RECORDING MODE F.
01  MASTER-RECORD      PIC X(500).

WORKING-STORAGE SECTION.
01  WS-MASTER-RECORD.
    05  WS-MASTER-RECORD-MONTH  PIC X(2).
    05  FILLER                  PIC X(498).

PROCEDURE DIVISION.
100-START.
    OPEN MASTER-FILE.
200-READ-MASTER.
    READ MASTER-FILE INTO WS-MASTER-RECORD
      AT END  GO TO 999-EOJ.
    IF WS-MASTER-RECORD-MONTH NOT = '12'
       GO TO 200-READ-MASTER.
300-PROCESS-DECEMBER.
    .....
999-EOJ.
    CLOSE MASTER-FILE.
    GOBACK.


I like to make my sort stuff with the prefix SORT-
SD  SORT-FILE
    DATA RECORD SORT-RECORD.
01  SORT-RECORD.
    05  SORT-KEY.
        10  SORT-KEY-CUST-SSN PIC 9(9).
    05  SORT-DATA.
        10  SORT-CUST-NAME    PIC X(40).
        10  SORT-CUST-AGE     PIC 9(3).



Linkage section stuff should usually start with LINK-

01  LINK-PARM-GRP.
    05  LINK-PARM-LENGTH    PIC S9(4)  COMP.
    05  LINK-PARM-VALUE     PIC X(8).


All fields in a table should have a prefix or suffix that binds them
together.

Literals should start with LIT- just as a hold variable should be HOLD- or
an edit might be EDIT- .  Some people suggest everything in WORKING-STORAGE
should start with WS- but I don't find this necessary except for like in the
WS-MASTER-RECORD where you would have 2 copies of the same information.

These are just some ideas; there are always better ways to do it.

Jeff



----------
In article <n7jR4.21266$0o4.221141@iad-read.news.verio.net>, "Mayer
Goldberg" <gmayer@cs.bgu.ac.il> wrote:


> Hello:
>
…[8 more quoted lines elided]…
> Mayer
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FWqR4.2478$XK.7087@news.swbell.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
Another trick is to alphabetize Working-Storage datanames. This is of
IMMENSE help when dealing with hundreds and thousands of variables.

Mayer Goldberg <gmayer@cs.bgu.ac.il> wrote in message
news:n7jR4.21266$0o4.221141@iad-read.news.verio.net...
> Hello:
>
> I'm having a problem with selecting variable names in cobol. So far,
I'm
> using cobol-85 so my variable names are all global. After a while,
in a
> reasonably large program, most of my time is spent on looking up
what those
> names are. There must be a better way: What useful naming
> conventions/practices are there?
…[3 more quoted lines elided]…
> Mayer
```

##### ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39180742.ED866327@zip.com.au>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <FWqR4.2478$XK.7087@news.swbell.net>`

```
Jerry P wrote:
> 
> Another trick is to alphabetize Working-Storage datanames. This is of
> IMMENSE help when dealing with hundreds and thousands of variables.

My first variable is 'a', second 'b', third 'c'...
Yep, that would work :-}

Put another way: huh??

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QF4S4.264$Rk6.51990@nnrp3.sbc.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <FWqR4.2478$XK.7087@news.swbell.net> <39180742.ED866327@zip.com.au>`

```
It is not the case that the first data name should be "A" and the
second "B." Jeeze!

Let's say I have to modify a program to output records to a file in
the same program where they are already being printed. While doing
this, I decide I need a new data name; let's say, NUMBER-RECORDS-OUT.
In this program I have 100 (or 2,500) places in Working Storage where
I could insert this new data name.

All other things being equal, for me (and apparently only a few others
for whom the Roman alphabet is our native symbol set), the logical
place to put NUMBER-RECORDS-OUT is:

01  NUMBER-RECORDS-IN                 PIC 9(9).
---------------------------------------------------- <<< I would put
NUMBER-RECORDS-OUT here
01 NUMBER-RECORDS-PRINTED    PIC 9(9).


Ken Foskey <waratah@zip.com.au> wrote in message
news:39180742.ED866327@zip.com.au...
> Jerry P wrote:
> >
> > Another trick is to alphabetize Working-Storage datanames. This is
of
> > IMMENSE help when dealing with hundreds and thousands of
variables.
>
> My first variable is 'a', second 'b', third 'c'...
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39196453.C9EBF3F4@cusys.edu>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <FWqR4.2478$XK.7087@news.swbell.net> <39180742.ED866327@zip.com.au> <QF4S4.264$Rk6.51990@nnrp3.sbc.net>`

```


Jerry P wrote:
> 
> It is not the case that the first data name should be "A" and the
…[16 more quoted lines elided]…
> 

It may be so.  But that is because you are grouping similar data
together.

Or you may choose to put new variables at the bottom of WORKING-STORAGE
so that people can more easily find the latest changes.

But does it make maintenance easier because variables starting with "N"
are in between variables starting with "M" and "O"?  Back in the days
when we ran our punched cards through a printer to get a uncompiled
listing of our source code, this was a useful technique.  But not now,
when we have our source code in the editor (except for copy modules
which have their own order).
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391810E5.2BE38FFD@cusys.edu>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <FWqR4.2478$XK.7087@news.swbell.net> <39180742.ED866327@zip.com.au>`

```
Jerry P wrote:
>
> Another trick is to alphabetize Working-Storage datanames. This is of
> IMMENSE help when dealing with hundreds and thousands of variables.

I have been thinking about this and I don't think it is for me.  I want
my variables ordered by function.  The way I put a functional prefix may
make it possible for me to alphabetize the function, but certainly
fields within a record won't be alphabetized.

It is easy to find a variable in working storage.  I just tell my editor
to find it, or if the source isn't available, I look at the cross
reference in the listing.  I use a naming convention to make it easier
to know what the code is doing in the PROCEDURE DIVISION.  Sorting
WORKING-STORAGE won't help this.
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fa57g$dcd$1@news.inet.tele.dk>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <FWqR4.2478$XK.7087@news.swbell.net> <39180742.ED866327@zip.com.au> <391810E5.2BE38FFD@cusys.edu>`

```
Just define everything as 01, impot it in excell and sort it - there you
go.:-)

Well to be serious. I made a program some years ago for another department
in the company. They took over and until February 2000 I didn't se my
program, but suddenly something should be added to the application.Surprise,
surprise I got my old program back. The program was changed and when I asked
the, what they had done, they smiled and answered:  "Alphabetized the
copybooks". (shit)

I always respect the structure in the programs I change, but in this case, I
had to put in copybooks in correct sequense - hard work.-)

Regards
Ib


Howard Brazee skrev i meddelelsen <391810E5.2BE38FFD@cusys.edu>...
>Jerry P wrote:
>>
…[12 more quoted lines elided]…
>WORKING-STORAGE won't help this.
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3916C03B.FCD4ACDD@cusys.edu>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
Mayer Goldberg wrote:
> 
> Hello:
…[5 more quoted lines elided]…
> conventions/practices are there?

Generally I use a prefix which tells me what record that field belongs
to.  Then the field contains an english language (or accounting or
banking or sales or whatever) term.

01  STUDENT-BILL-RECORD.
    05  SB-KEY.
        10  SB-CAMPUS.
        10  SB-SSN.
    05  SB-HOME-ADDRESS.

Note, SSN has to be well understood, or else it should be written out.

01  VALID-STATE-MAX       PIC 9(02)   PACKED-DECIMAL VALUE 50.
01  VALID-STAT-INDEX      PIC 9(02)   PACKED-DECIMAL.
01  VALID-STATE-TABLE.
    05   VALID-STATE-RECORDS   OCCURS 50.
        10   VALID-STATE-CODE  PIC X(02).
        10   VALID-STATE-NAME  PIC X(10).
```

##### ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3918235E.3FF4CD65@iinet.net.au>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <3916C03B.FCD4ACDD@cusys.edu>`

```


Howard Brazee wrote:
> 
> Generally I use a prefix which tells me what record that field belongs
…[8 more quoted lines elided]…
> 
Hmm,
What's wrong with
  KEY IN STUDENT-BILL-RECORD
  KEY IN TUTOR-BILL-RECORD
Then you could (if you wanted to)
 MOVE CORRESPONDING STUDENT-BILL-RECORD TO TUTOR-BILL-RECORD.
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39182815.2CDFB109@cusys.edu>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <3916C03B.FCD4ACDD@cusys.edu> <3918235E.3FF4CD65@iinet.net.au>`

```


Joseph J Katnic wrote:
> 
> Howard Brazee wrote:
…[16 more quoted lines elided]…
>  MOVE CORRESPONDING STUDENT-BILL-RECORD TO TUTOR-BILL-RECORD.

Mainly because our standards disallow that.  The only time I do it is
when I am doing one-time jobs such as unload-reload.  Guessing at
reasons:

It is hard to tell if you are missing a field after maintenance changes
a copy member.
It is hard to search for programs which access a field.
It is a pain to write IN or OF clauses all over the place.

The last doesn't look large, because you likely only need it a few
places... but the point of having prefixes for a particular file is to
tell us immediately where a field being referenced belongs.  Maybe I
never move that field, but I like to know where that field came from. 
e.g.

COMPUTE TL-STUDENT-BALANCE = BR-STUDENT-BALANCE + (BR-NEW-BILL *
CR-BONUS)

vs

COMPUTE STUDENT-BALANCE OF TOTAL-LINE = STUDENT-BALANCE OF BILL-RECORD +
(NEW-BILL OF BILL-RECORD * BONUS OF CAMPUS-RECORD).

Either way, I can tell where the field belongs, but which is easier to
use?
```

###### ↳ ↳ ↳ MOVE CORR (was: variable and paragraph naming conventions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f9dkb$8b1$1@slb0.atl.mindspring.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <3916C03B.FCD4ACDD@cusys.edu> <3918235E.3FF4CD65@iinet.net.au>`

```
Just another "general comment" - MOVE CORRESPONDING is "frowned upon" by
many - but certainly not all shops and programmers.  (This doesn't mean that
it doesn't have its place and use - but it is often considered just SLIGHTLY
better than GO TO DEPENDING).

There are a "bunch" of obscure rules that can easily impact how it works -
which is why it is considered "error-prone" (and not to be used - if there
are other ways of doing something) by many.

Originally, it was going to be put in the "obsolete" category in the '85
Standard (and removed in the next revision).  This did NOT happen, but it is
still not looked upon with much approval - by many.

My "favorite" example of one of the "obscure" rules about MOVE CORR, consider
the following:

  01  Group1.
        05  anElem Pic X.
        05  aNother Pic X.
 01  Group2.
        05  anElem Pic X.
        05  aNother Pic X.
        05  anElem Pic X.

      ...

    Move Corr Group1 to Group2.

***

OK, who wants to guess what will happen?  Will this cause a compiler error?
If not, what will happen at run-time?  (My usual prize of "any number of bits
that you want" - for the person who correctly tells what the '85 COBOL
Standard says about this - and why it is different from the '74 Standard.)
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000509151206.24964.00001980@nso-fy.aol.com>`
- **References:** `<3918235E.3FF4CD65@iinet.net.au>`

```
In article <3918235E.3FF4CD65@iinet.net.au>, Joseph J Katnic
<josephk@iinet.net.au> writes:

>Hmm,
>What's wrong with
…[5 more quoted lines elided]…
>-

Using MOVE CORRESPONDING creates 'opportunities' if the group level item
you are referencing has sub-ordinate group level entries under it.  In past
attempts
at using Initialize and Corresponding, I have found that sub-groups do not
always
get handled the way that you might expect and result in corrupted data.
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f6gb2$pv3$1@news.inet.tele.dk>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
I don't think I reveal any big national secrets, when I tell you that I try
to be the laziest person in the universe. Therefore I normally think very
much before I go to work, and that goes for this problem too.

The following hints are for structured Cobol - in the OO-world the approach
is different.

When the design is ready for the new application (could be one program and
it could be several hundreds of programs), then forget about the logic for a
while and concentrate on data.

I start to produce copy-books. 4 for each file (one for select, one for the
FD and two for WS. The first one in WS is the record structure and the
second one is File-Status and EOF-Switch)
The date-copy-book was made years ago, and I re-use it. It contains 3
formats.The one I get from the date-function, the one I want to store and
the one I want to display - thats it.

I have many good re-useable copy-books and copy-books I can use after minor
changes.

After defining all common data elements, I define my user-interface. If it
is a Screen Section application I add a copybook containing variables as
FG-Color and BG-Color.

Normally I start to make a layout-screen (with Date, title at the top and
Function-keys at the bottom). I use the layout-screen as a skeleton for all
the screens to avoid 'bumping' screens when the user moves through the
system.

Until now we haven't coded one line in Procedure Division. We have made som
pre-fabrication to be used in this (and future) applications.

Now to the answer of your question. I use numbers in JSP-cobol - never in
other dialects. I will always have a datamodel (even if I have to make it
myself). My 'CUST-NO' is always the name of customer number in the FD of the
customer file. In fact everything in the customer file is prefixed with
'CUST'. 'WS-CUST-NO' is the same field, but in my WS-structure. Again
'ORDER-CUST-NO'
is my 'CUST-NO' in the FD of the order-file. 'SCR-CUST-NO' is my 'CUST-NO'
in Screen.section iand it can be to, from or using 'WS-CUST-NO',
'WS-ORDER-CUST-NO' or whatever.

I think you've got it by now. I can make minor changes to my standard. If I
choose to handle IO in sub-programs WS is changed to LS (I use the structure
in Linkage Section in the sub-program). That decission is made, when I know
about the development tool and the risk for future change of IO system (If a
SQL-system is a possible future extension, it might be a good idea to
isolate IO in separate modules - sorry, but lazy again)

Now, what's left for the individual programs. 'Local workspace' as counters,
sums, totals, yes, anything to support the procedure in this unique program.

My advice is: 'Be lazy, creative and think upon the future - I mean, a
customer record is probably used in a later assignment too???'.

Regards
Ib

Mayer Goldberg skrev i meddelelsen ...
>Hello:
>
…[8 more quoted lines elided]…
>Mayer
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39170ED9.CB254E0A@home.com>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```


Mayer Goldberg wrote:
> 
> Hello:
…[8 more quoted lines elided]…
> 
Well you sure got plenty of advice/suggestions. As you can see in larger
shops their standards can be pretty rigid. Couple of tips, and others
have mentioned, :-

- list your variables alphabetically where possible
- make names meaningful to you; avoid confusion such as following
  when devising variables :-

	Customer-Num
	Customer-Numbr
	Customer-No
	Customer-Number - stick with one 'type' 

- certainly follow those suggestions which recommend prefixes like
'Customer-number', 'Vendor-key' etc.

Ib mentioned OO. I don't currently use structured but some compilers and
the new COBOL 200X allows for Local-Storage Section - so it isn't
difficult to figure out your names because they are particular to just
that piece of 'local' code.

OO-wise my Global Working-Storage is absolutely MINIMAL - so I don't
have sheaves of pages to look at to 'search'. As much as possible I keep
my variables in specific methods (sub-routines, if you like). My own
particular style within Methods :-

*>----------------------
Method-id. "method-name".
*>-----------------------
Working-storage section.
01 a-number			pic 9(02).
01 ws-number2			pic 9(02).
Local-storage section.
01 ls-number			pic 9(02).
01 ls-number2			pic 9(02).
Linkage section.
01 lnk-numberA			pic 9(02).
01 lnk-NumberB			pic 9(02).
01 lnk-result			pic x(4) comp-5.

Procedure Division using lnk-numberA lnk-NumberB returning lnk-result.
	.............
End Method "method-name".
*>---------------------------

In small code like this it isn't difficult to figure out a-number and
ws-Number2, although consistency wouldn't hurt. Another trick coming in
because of the influence of OO languages is 'CamelBack' e.g.
CustomerNumber, AnObject, aDialogBox etc...

Jimmy, Calgary AB
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f8f17$tjn$1@slb6.atl.mindspring.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
Lots of "interesting" replies to this note - but so far (and I haven't read
all of them), no one as "latched on" to the use of the word "global" in this
original note.

My *guess* is that this is someone who is used to programming in one (or
more) other languages.

The '85 Standard for COBOL introduced "nested programs".  If this "turns you
on" (or is something that is more familiar to you - and does NOT violate your
shop standards), then look at using these to get "local" variables - and
code.  The trick is to reach "subroutine" logic via a CALL (to a nested
program) rather than using a PERFORM of a paragraph.

If you are new to COBOL, then this may be a method of working that you just
have not been introduced to yet.

NOTE: Calling a "separately compiled program" is also a useful concept - but
doesn't seem relevant to your use of GLOBAL (and implicitly LOCAL) when
describing variable names.
```

##### ↳ ↳ Re: variable and paragraph naming conventions

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39184535.7F33C399@home.com>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <8f8f17$tjn$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Lots of "interesting" replies to this note - but so far (and I haven't read
…[4 more quoted lines elided]…
> more) other languages.

Go to the top of the form :-). Mayer is programming in COBOL for 'fun'.
He's already familiar with other OO languages. So from my response he's
now asking about OO COBOL.

Can you answer one of his questions Bill, from your knowledge. Apart
from us 'little folks', is there anybody out there in the mainframe
world making an attempt to use OO COBOL. (The only reference I saw was
in coblreport.com that a German Bank (has to be mainframe doesn't it ?)
was developing in OO. Can your IBM/Merant contacts give you any clues.

Jimmy
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f9na8$ciq$1@slb7.atl.mindspring.net>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <8f8f17$tjn$1@slb6.atl.mindspring.net> <39184535.7F33C399@home.com>`

```
I have asked IBM for any reference sites or even how to find out about them -
and so far there is "dead silence".

The German Bank *may* be using Siemens - which does offer OO on "their
mainframe". (Interestingly enough - Siemens is now a part of Fujitsu, but I
do not think the OO implementations in the two variations of Fujitsu COBOL
are particularly close - yet.)

I doubt that MERANT would have any information on this, because they do NOT
provide an "IBM-mainframe compatible" OO implementation dialect - which would
make inter-operating system development fairly difficult.

I will post a note to IBM-MAIN asking if they know of anyone doing this
(yet)?
```

###### ↳ ↳ ↳ Re: variable and paragraph naming conventions

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391b8e89.6717110@news.cox-internet.com>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net> <8f8f17$tjn$1@slb6.atl.mindspring.net> <39184535.7F33C399@home.com> <8f9na8$ciq$1@slb7.atl.mindspring.net>`

```
On Tue, 9 May 2000 14:02:01 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>I have asked IBM for any reference sites or even how to find out about them -
>and so far there is "dead silence".

I asked several people who should know at CA-World about this and they
knew of no one on an IBM mainframe using OO COBOL.
```

#### ↳ Re: variable and paragraph naming conventions

- **From:** areymond@csi.com (Alain Reymond)
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39183d55.36748376@news.skynet.be>`
- **References:** `<n7jR4.21266$0o4.221141@iad-read.news.verio.net>`

```
I use little paragraphs but most of the time the 'call .. using'
syntax which I prefer, especially with the program-id. ... end program
syntax. I find it more secure. So, I have little problems with
paragraph names.
 
For the variable, I have a personal system which cannot be universal
but works most of the time. It is bases on a prefix for the fd, wss
and linkage section, a variable description, and a name
prefix-description-name
The prefix is (guess what!) : wss, lnk, fd
The description is : 
    i for numeric
    x for alphanumeric
and the length.

For example : 
fd my-file.
01 fdmyf-x20-name pic x(20).
working-storage section.
01 wss-x20-name pic x(20.).
01 wss-x20-firstname pic x(20).
linkage section.
01 lnk-i3-name pic 999.

You can use 'f' and the number of bytes for float, df for double
float, etc...

The system doesn't work in complicated cases of pictures but most of
the time, it is sufficient. The advantages I see is - like in the
polish notationin C - that you know what is the type of your variable
(numeric, alphanumeric), the length. It prevents errors while moving
one variable to another. 
It is also very convenient for redefinitions using the 'copy
replacing' statement. Your variable will differ only from the prefix.

copy file:
01 (tag)file01.
	02 (tag)-x20-name pic x(20).
	02 (tag)-x20-firstname pic x(20).
in the source
copy '...' replacing ==(tag)== by ==fdmyfile==.
working-storage section.
copy '...' replacing ==(tag)== by ==wss==.
procedure division.
move fdmyfile-x20-name to wss-x20-name
etc...

If you have to modify the structure of the record, just modify the tag
file and recompile.

That were only a few ideas that works well here at our office and
makes our maintenance easier.

Alain Reymond
 

>Hello:
>
…[8 more quoted lines elided]…
>Mayer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
