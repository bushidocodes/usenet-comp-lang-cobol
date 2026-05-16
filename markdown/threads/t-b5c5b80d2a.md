[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# pause, break, etc...

_6 messages · 4 participants · 2004-02_

---

### pause, break, etc...

- **From:** jerome <yrsnms@caramail.com>
- **Date:** 2004-02-20T08:13:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c14bto$so3$1@s1.read.news.oleane.net>`

```
Hello,

I don't know COBOL, but I must work on a old software to find a bug.

I'd like to stop the soft at any point I want, like "PAUSE" with DOS (to 
continue press any key).

How can I do this miracle ?

Sorry for my poor english.

Best regards.

jerome
```

#### ↳ Re: pause, break, etc...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-02-20T12:28:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r3nZb.11794$PY.9853@newssvr26.news.prodigy.com>`
- **References:** `<c14bto$so3$1@s1.read.news.oleane.net>`

```
"jerome" <yrsnms@caramail.com> wrote in message
news:c14bto$so3$1@s1.read.news.oleane.net...
> Hello,
>
…[5 more quoted lines elided]…
> How can I do this miracle ?

The COBOL part is immaterial... since you say you must 'work on' the
software, I assume you have the source code and the compiler.. which you
MUST have. You must then re-compile the program, either inserting the
correct compiler options/statements to run the program using a stepping
debugger (if available for your compiler, and if your site has licensed such
a product, which are often 'optional, priced add-ons' to the 'base' compiler
product) , or inserting the correct language commands to force the program
to stop and go.

What those specific steps are can vary wildly depending on the specific
compiler and / or the operating system; perhaps with the way the program is
written; and almost surely depending on 'what is the bug' you are trying to
isolate and fix.

In your case - realistically - your best bet will be to bring in an outside
consultant familiar with debugging COBOL programs. Since you don't know
COBOL you could spend weeks doing what someone with experience might handle
in a couple of hours.
```

##### ↳ ↳ Re: pause, break, etc...

- **From:** jerome <yrsnms@caramail.com>
- **Date:** 2004-02-23T11:59:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1cm92$ej6$1@s1.read.news.oleane.net>`
- **In-Reply-To:** `<r3nZb.11794$PY.9853@newssvr26.news.prodigy.com>`
- **References:** `<c14bto$so3$1@s1.read.news.oleane.net> <r3nZb.11794$PY.9853@newssvr26.news.prodigy.com>`

```
Michael Mattias wrote:
  I assume you have the source code and the compiler..

Yes I have,

You must then re-compile the program, either inserting the
> correct compiler options/statements to run the program using a stepping
> debugger (if available for your compiler, and if your site has licensed such
> a product, which are often 'optional, priced add-ons' to the 'base' compiler
> product) ,

It-s available and I think my enterprise has licensed it. But I don't 
undersant how usse it.
To compile, I put this statement :
rmcobol myprog.cbl -D
But what else ?

  or inserting the correct language commands to force the program
> to stop and go.

Yes, but which commands ?
I found : Stop run.
And I used some loops

For information, I found the bug because it was a little program (1250 
lines). But, if you could answer to my questions please.

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: pause, break, etc...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-02-23T12:02:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HZl_b.16567$PY.15197@newssvr26.news.prodigy.com>`
- **References:** `<c14bto$so3$1@s1.read.news.oleane.net> <r3nZb.11794$PY.9853@newssvr26.news.prodigy.com> <c1cm92$ej6$1@s1.read.news.oleane.net>`

```
"jerome" <yrsnms@caramail.com> wrote in message
news:c1cm92$ej6$1@s1.read.news.oleane.net...
> Michael Mattias wrote:
>   I assume you have the source code and the compiler..
…[5 more quoted lines elided]…
> > debugger (if available for your compiler, and if your site has licensed
such
> > a product, which are often 'optional, priced add-ons' to the 'base'
compiler
> > product) ,
>
…[14 more quoted lines elided]…
> lines). But, if you could answer to my questions please.


I *did* answer your questions.  IMO, for a non-COBOL person to attempt to
modify a COBOL program to locate and fix a bug is a fool's errand. "Maybe"
it could be done via newsgroup, but.. you'd have to write a complete and
accurate description of the bug, create instructions to replicate the bug
and/or include all data files required to run the program, provide a copy of
the failing executable program and post all source code and compiler
options. Not just that, but "which" of possibly twenty or thirty possible
verbs/functions/statements and where in the program they should be inserted
will vary with "what kind" of bug you think you have. (I would like a nickel
for every time a client has said, "I think the problem is xxxxx" and the
problem REALLY was yyyyy).

I still say your best bet from both a time and money standpoint is to engage
a COBOL professional to handle this. When he/she arrives, watch, but do not
under any circumstances attempt to help unless this is part of the
'up-front' agreement.

That gets you past your short-term problem. Long term, you will require
maintenance of your software, so you should plan accordingly. Take a COBOL
class, or find a reliable person/firm to perform this maintenance as a
contractor/consultant.

Your Mileage May Vary.

MCM
```

###### ↳ ↳ ↳ Re: pause, break, etc...

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2004-02-25T01:56:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0402250156.1531e945@posting.google.com>`
- **References:** `<c14bto$so3$1@s1.read.news.oleane.net> <r3nZb.11794$PY.9853@newssvr26.news.prodigy.com> <c1cm92$ej6$1@s1.read.news.oleane.net>`

```
jerome <yrsnms@caramail.com> wrote in message news:<c1cm92$ej6$1@s1.read.news.oleane.net>...
> Michael Mattias wrote:
>   I assume you have the source code and the compiler..
…[27 more quoted lines elided]…
> Jerome

AH!
rmcobol... you'r using Liant's RMCOBOL right?
1) You cant certainly use -D but that is useful ONLY if you've got "D"
lines in your source (I won't eleborate on this). But what you really
need is -y option along with -l and -m. "-l" produces a compile list;
"-m" adds an allocation map to that list (you probably don't need it,
but it won't hurt either); "-y" inserts the symbol table in the
object, so during the debbug session, you can name variables by their
name instead of their offset only.
2)runcobol myprog.cob -d. This will start the program in debug mode.
So, armed with your compile listing, you can:
"s" - step one line
"a xxx" - go to line xxx ("a" without "xxx" goes to the end).
"d var1" - displays var1 in it's defined type; as opposed to "d var1,
hex" which would display the contents of var1 in hexadecimal notation.
"q" - quit 
There are a bunch of other commands and options, but I can't recall
them right now.

Regards, 

Paulo Vieira, Emporsoft
```

#### ↳ Re: pause, break, etc...

- **From:** Willie Wortel <wiwo@nospam.nl>
- **Date:** 2004-02-25T00:21:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<403BDC89.8060209@nospam.nl>`
- **References:** `<c14bto$so3$1@s1.read.news.oleane.net>`

```
Hi Jerome,

To stop the program at any point where you suspect a failure, use 
"breakpoints". Breakpoints work in the way that you describe, so like 
"pause" and continue by pressing some key.

Open the COBOL source in your compiler. Then look for the breakpoint 
option. In every COBOL compiler as far as I know this feature is called 
"breakpoint".

You select a line where you want to pause, then you activate the 
breakpoint option. The line will be marked. When you run the program in 
the debug mode, it will stop at all the lines where you defined a 
"breakpoint". You will also have to find out (in the Help or so) how to 
continue after a breakpoint. Probably this will be the same key that you 
also use to start the debug run.

Good luck,
Willie

jerome wrote:
> Hello,
> 
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
