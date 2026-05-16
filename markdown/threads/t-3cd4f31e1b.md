[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hexadecimal Input Files

_14 messages · 8 participants · 2006-06_

---

### Hexadecimal Input Files

- **From:** "Stacy Kay" <stacykw85@hotmail.com>
- **Date:** 2006-06-26T05:56:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`

```
I'm currently trying to do a project that uses a Hexadecimal input
file. From what I've heard, COBOL does not like this format. I have
to do calculations with this input. I'm not sure how to go about
using this input file. How should I declare the input file? Do I need
to some how convert the file to a different format within the program?
Please list any ideas regarding a hexadecimal input file.
```

#### ↳ Re: Hexadecimal Input Files

- **From:** docdwarf@panix.com ()
- **Date:** 2006-06-26T13:20:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7omv7$476$1@reader2.panix.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`

```
In article <1151326592.466740.58500@y41g2000cwy.googlegroups.com>,
Stacy Kay <stacykw85@hotmail.com> wrote:
>I'm currently trying to do a project that uses a Hexadecimal input
>file.

Most data I have run across over the past few decades have been in a 
format reducible to hexadecimal... it might be that others would be able 
to make a similar statement.

>From what I've heard, COBOL does not like this format.

This indicates a lack of familiarity with COBOL on your part... is this 
indication reflected in your experience?

>I have
>to do calculations with this input. I'm not sure how to go about
>using this input file.

It should be used in accordance with the specifications you were given, 
said specs to include the file's format.

>How should I declare the input file?

Platform and compiler information might make this question more readily 
answered.

>Do I need
>to some how convert the file to a different format within the program?
>Please list any ideas regarding a hexadecimal input file.

My first idea is 'Show what you have already done, so that work is not 
repeated and mistakes not perpetuated.'

My second idea is 'Do your own job/homework'... and if this is your job my 
third idea is 'Tell Management that your skill-set is not equal to the 
task being assigned.'

DD
```

##### ↳ ↳ Re: Hexadecimal Input Files

- **From:** "Stacy Kay" <stacykw85@hotmail.com>
- **Date:** 2006-06-26T07:23:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151331823.840604.30880@i40g2000cwc.googlegroups.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <e7omv7$476$1@reader2.panix.com>`

```
I guess I didn't give enough information. I am an intern this summer. I
have already finished a program in Assembler. What my task is, is to
convert that program to COBOL. I have had two semesters of COBOL class
experience.  The format of the input file I am to use is in
hexadecimal. I just haven't had this experience before with this
format. I've read it before in a JCL dump, but just haven't used it.
Also, I am working on a mainframe environment. I didn't want to have
someone do my work. I just wanted ideas or even just information about
the relationship between COBOL using hexadecimal numbers. I've looked
in some of my mentor's manuals, but nothing goes too deep on this
subject.


docdwarf@panix.com wrote:
> In article <1151326592.466740.58500@y41g2000cwy.googlegroups.com>,
> Stacy Kay <stacykw85@hotmail.com> wrote:
…[35 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** docdwarf@panix.com ()
- **Date:** 2006-06-26T14:47:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7os27$272$1@reader2.panix.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <e7omv7$476$1@reader2.panix.com> <1151331823.840604.30880@i40g2000cwc.googlegroups.com>`

```
In article <1151331823.840604.30880@i40g2000cwc.googlegroups.com>,
Stacy Kay <stacykw85@hotmail.com> wrote:
>I guess I didn't give enough information. I am an intern this summer. I
>have already finished a program in Assembler. What my task is, is to
>convert that program to COBOL. I have had two semesters of COBOL class
>experience.

Some familiarity, then... well, that's a start.

>The format of the input file I am to use is in
>hexadecimal.

Ummmmm... maybe what the difficulty here is a matter of terminology.  
Usually when a COBOL programmer refers to 'the format of a file' what is 
indicated is the layout of the records, found either in the FD or in the 
WORKING-STORAGE SECTION as the target of a READ (filename) INTO.  Without 
that one is usually reduced to READing a file into a field defined as a 
simple alphanumeric and 'making sense' of the results by use of reference 
modification.  For example:

FD  INFILE.
01  INFILE-REC PIC X(  ).
...
WORKING-STORAGE SECTION.
...
01  WS-INFILE-REC.
    05  WS-INFILE-LNAME PIC X(25) VALUE SPACES.
    05  WS-INFILE-FNAME PIC X(20) VALUE SPACES.
    05  WS-INFILE-MI    PIC X(01) VALUE SPACES.
    05  WS-INFILE-EMPNO PIC 9(09) VALUE ZEROES.
    05  WS-INFILE-DPTNO PIC X(05) VALUE SPACES.
    05  WS-INFILE-MGRNO PIC 9(09) VALUE ZEROES.
...
PROCEDURE DIVISION.
...
    READ INFILE INTO WS-INFILE-REC
     AT END SET NO-MORE-INFILE TO TRUE.

After this READ is successfully executed both INFILE-REC and WS-INFILE-REC 
contain the same data.  One can refer to WS-INFILE-DPTNO or 
INFILE-REC(55:5) and the data will be the same; a COBOL programmer would, 
in my experience, refer to the 'format' as being WS-INFILE-REC.

Where is a similar structure to be found for the file you will be using?


>I just haven't had this experience before with this
>format.

With good reason... one of the advantages of COBOL is that when (not if) 
the program blows up at 2:am and Ops calls you then you will have an 
easier time making sense of (and repairing) WS-INFILE-DEPTNO than 
INFILE-REC(55:5).

>I've read it before in a JCL dump, but just haven't used it.
>Also, I am working on a mainframe environment.

With 'JCL' and 'mainframe' being mentioned I will conclude that you are 
working in an IBM-compatible environment... this, also, is helpful to 
know.

>I didn't want to have
>someone do my work. I just wanted ideas or even just information about
>the relationship between COBOL using hexadecimal numbers. I've looked
>in some of my mentor's manuals, but nothing goes too deep on this
>subject.

Once again, 'hexadecimal numbers' are used in different ways... compare 
the differences between what results from

01  NUM-COMP  PIC S9(8) COMP VALUE +123456.

... and ...

01  NUM-COMP3 PIC S9(8) COMP-3 VALUE +123456.

DD
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-06-26T08:49:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fesv9218fkr6hs0f2uvjkg1umrkd0btr0e@4ax.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <e7omv7$476$1@reader2.panix.com> <1151331823.840604.30880@i40g2000cwc.googlegroups.com>`

```
On 26 Jun 2006 07:23:43 -0700, "Stacy Kay" <stacykw85@hotmail.com>
wrote:

>I guess I didn't give enough information. I am an intern this summer. I
>have already finished a program in Assembler. What my task is, is to
…[8 more quoted lines elided]…
>subject.

Usually we have access to the program that created a file.   What you
need is to learn the format of the data.

First, make sure your data are in EBCDIC if you are using an EBCDIC
machine (there are ways around this - but check).   Then see how each
field is defined.    Let's pretend you have an 80 character file as
input.    It doesn't have a single hex number running for 80 bytes.
Instead it has a bunch of fields, some might be binary, others might
be packed, and others display.   Signs will make a difference.

CoBOL starts off by defining this structure.   CoBOL expects you to
enter the description of this record.    As long as the description is
constant, CoBOL has an easy time with this.

If the program that created the file is CoBOL, then you can copy that
program's description of the record.   If it is some other language,
you can determine the description.    At any rate, you need to find
out how the record is arranged.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2006-06-26T12:30:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nk20a2del3rl1hqp35vhl4a9b48blj8f6o@4ax.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <e7omv7$476$1@reader2.panix.com> <1151331823.840604.30880@i40g2000cwc.googlegroups.com>`

```
On 26 Jun 2006 07:23:43 -0700, "Stacy Kay" <stacykw85@hotmail.com>
enlightened us:

>I guess I didn't give enough information. I am an intern this summer. I
>have already finished a program in Assembler. What my task is, is to
…[9 more quoted lines elided]…
>

If this is the same file you read into your Assembler program then
your task, as far defining the data in the file, is pretty simple.  If
you defined a field in the file in the Assembler program as

FIELDA     DS   CL10

Then in Cobol it would be:

FIELDA     PIC X(10).

Also, if you defined a field as:

FIELDB    DS   PL5

You might define it in Cobol as

FIELDB    PIC 9(9)   COMP-3 or
FIELDB    PIC 9(7)V99  COMP-3.

And finally, by way of example, if you had a field in the Assembler
program defined as:

FIELDC    DS    XL4

It may be defined in Cobol as:

FIELDC   PIC 9(8)   COMP

I hope that helps.


>
>docdwarf@panix.com wrote:
…[37 more quoted lines elided]…
>> DD

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


SAM: "What's new Normie?"
NORM: "Terrorists, Sam. They've taken over my stomach and they're
demanding beer."
From the US TV Sitcom, "Cheers"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Hexadecimal Input Files

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-06-26T13:50:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xCRng.123444$dW3.50220@newssvr21.news.prodigy.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`

```
"Stacy Kay" <stacykw85@hotmail.com> wrote in message
news:1151326592.466740.58500@y41g2000cwy.googlegroups.com...
> I'm currently trying to do a project that uses a Hexadecimal input
> file. From what I've heard, COBOL does not like this format. I have
…[3 more quoted lines elided]…
> Please list any ideas regarding a hexadecimal input file.

There is no such thing as a "hexadecimal input file."   Files is files, data
are data.

Perhaps you mean the file data are "character strings with each pair of
characters representing a value using hexadecimal digits?"

That is, were the data to be defined in the data division rather than a disk
file it would look like...

05  THE-DATA  PIC X(08) VALUE "010A2B94"

..in which  the data are to be interpreted as four (4) numeric values, 0x01,
0x0A, 0x2b and 0x94 ????

If you want a tutorial on COBOL data types you can go to
http://www.flexus.com/download.html and get file COBDATA.ZIP. This is old,
but it does include a text file explaining all the common data types used by
COBOL compilers. It's possible you will be able to use a PICTURE clause
which would allow direct MOVEs to destination datanames without an explict
conversion, or maybe you can't.

If there are no intrinsic data types for the format (and there is no type of
which I am aware which would allow direct MOVEs of the data if it are as
described above), you'll have to go back to math 101 and compute the values
character by character using base 16 arithmetic.

MCM
(author/contributor of said tutorial paper).
```

#### ↳ Re: Hexadecimal Input Files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-06-26T08:01:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jlpv92t2rcad1vfg5t5gs6qpnentf715p7@4ax.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`

```
On 26 Jun 2006 05:56:32 -0700, "Stacy Kay" <stacykw85@hotmail.com>
wrote:

>I'm currently trying to do a project that uses a Hexadecimal input
>file. From what I've heard, COBOL does not like this format. I have
…[3 more quoted lines elided]…
>Please list any ideas regarding a hexadecimal input file.

Could you possibly be talking about a file that was created on one
computer, and you want to process it on a computer that represents
data differently?    

Or maybe you mean a file that just has numbers in non-display format.
In that case, your question and assumption are opposite from what we
normally get.   Quite often when someone mistakenly refers to "a cobol
file", that person is referring to data that just looks like hex
digits instead of delimited character that some "modern" languages
like.   The format of the data is dependent upon the computer, not the
language though.

If you don't know CoBOL, why are you interested in doing calculations
with it?    

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Hexadecimal Input Files

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-26T11:34:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151346896.681967.199800@b68g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com>`

```

Stacy Kay wrote:
> I'm currently trying to do a project that uses a Hexadecimal input
> file. From what I've heard, COBOL does not like this format. I have
…[3 more quoted lines elided]…
> Please list any ideas regarding a hexadecimal input file.

By now you will know that you have walked into a full broadside from
the usual suspects.

You won't get very far on this group without at least posting an
assembler layout for the file or a cobol FD. From your use of assembler
you will probably be aware that mainframes (IBM at least) have a number
of data formats available to them: binary, character, packed being the
most common. Michael Mattias quoted a reference to a site which will
aid further in considering the various formats:

X'C1C2' in assembler is character 'AB' in Cobol (ie PIC XX or PIC X2 or
PIC A2) EBCDIC.

P'123C' in assembler is packed 123 in Cobol (ie PIC S999 COMP-3).

X'0001' in assembler is binary 1 and in cobol is represented as PIC
S9(4) COMP.

Cobol has no problem in using binary or hex. If you have had two
semesters of Cobol then you have probably received more formal training
than most people in this group. If you are having serious trouble
defining the file (vis Select...assign, fd, etc.) then perhaps you
should ask for help from your supervisor.
```

##### ↳ ↳ RE: Hexadecimal Input Files

- **From:** "Stacy Kay" <stacykw85@hotmail.com>
- **Date:** 2006-06-26T12:07:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151348863.668360.54570@b68g2000cwa.googlegroups.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <1151346896.681967.199800@b68g2000cwa.googlegroups.com>`

```
I know what you are saying; about actually showing you what the file
layouts are. It would take up more room than you would want to see. All
of the records have different layouts past 35 bytes. Plus I don't think
it would be a good idea to just put those out there. I would probably
be breaking a policy. I appreciate all your help and information you
have given me thus far. It is enough to work with for now. I need to
organize myself a little more. Thanks for taking time out of your day
to respond.
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** docdwarf@panix.com ()
- **Date:** 2006-06-26T19:19:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7pc00$pf9$1@reader2.panix.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <1151346896.681967.199800@b68g2000cwa.googlegroups.com> <1151348863.668360.54570@b68g2000cwa.googlegroups.com>`

```
In article <1151348863.668360.54570@b68g2000cwa.googlegroups.com>,
Stacy Kay <stacykw85@hotmail.com> wrote:

[snip]

>I appreciate all your help and information you
>have given me thus far. It is enough to work with for now. I need to
>organize myself a little more. Thanks for taking time out of your day
>to respond.

No problem... it's probably worth double what you've been asked, here, to 
pay for it.

DD
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-06-26T22:15:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q0Zng.245978$Vt5.213686@fe09.news.easynews.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <1151346896.681967.199800@b68g2000cwa.googlegroups.com> <1151348863.668360.54570@b68g2000cwa.googlegroups.com>`

```
From the fact that the data in the first 35 bytes is "standard" and after that 
different, then you probably have different record types - possibly of different 
lengths.   If you have (IBM talk) RECFM=VB, then you will want to handle this in 
COBOL via the RECORD VARYING IN SIZE clause in your FD.

If all the records ARE the same size - but have different layouts, you can 
handle this in COBOL by having multiple 01-levels under your FD - or by using 
READ INTO an 01-level in Working-Storage that has REDEFINES.
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2006-06-26T16:54:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12a0pei4p1ctp99@corp.supernews.com>`
- **In-Reply-To:** `<1151348863.668360.54570@b68g2000cwa.googlegroups.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <1151346896.681967.199800@b68g2000cwa.googlegroups.com> <1151348863.668360.54570@b68g2000cwa.googlegroups.com>`

```
Stacy Kay wrote:
> I know what you are saying; about actually showing you what the file
> layouts are. It would take up more room than you would want to see. All
…[6 more quoted lines elided]…
> 

In the presumably unlikely event that this problem does drive you back 
to comp.lang.curmudgeon, you might want to post a sample of the data you 
have to interpret (with field names changed to protect the innocent).  A 
small proof-of-concept program could be all you need.

Louis (who taught COBOL on a Burroughs mainframe in 1982)
```

###### ↳ ↳ ↳ Re: Hexadecimal Input Files

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-06-26T23:44:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7prh7$i17$1@reader2.panix.com>`
- **References:** `<1151326592.466740.58500@y41g2000cwy.googlegroups.com> <1151346896.681967.199800@b68g2000cwa.googlegroups.com> <1151348863.668360.54570@b68g2000cwa.googlegroups.com> <12a0pei4p1ctp99@corp.supernews.com>`

```
In article <12a0pei4p1ctp99@corp.supernews.com>,
Louis Krupp  <lkrupp@pssw.nospam.com.invalid> wrote:
>Stacy Kay wrote:

[snip]

>> I appreciate all your help and information you
>> have given me thus far. It is enough to work with for now. I need to
…[6 more quoted lines elided]…
>have to interpret (with field names changed to protect the innocent).

... but don't git me started on what those kids're callin' 'music' 
nowadays, neither... buncha durned noise, 'f ya ask me... an' another 
thing, have ya ever seen the *clothes* they wear, or not, as the case may 
be?  Guess they ain't got no mothers lookin' out fer 'em... an' another 
thing...

zzzzZZZZZzzzzz....

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
