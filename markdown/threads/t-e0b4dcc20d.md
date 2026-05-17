[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP WITH LINKED LISTS

_12 messages · 11 participants · 1997-04 → 1997-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HELP WITH LINKED LISTS

- **From:** "he..." <ua-author-8810531@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33658920.463873282@news.tu.infi.net>`

```

Hello and thanks for reading this,


I've just finished an introductory course in COBOL and am getting
ready to take the follow-on course in data and file structures.
According to the instructor for that course we will use linked lists
"up one side and down the other". I want to beat him to the punch and
know how to implement a linked list before this class starts in 2
weeks.

The text book used, Stern and Stern' " Structured Cobol Programming"
has no mention of linked lists. I've investigated on my own and have
read several chapters from various sources and have gleened the flavor
of what a linked list is and how it works. These references all have
examples in PASCAL or C, neither of which I'm familiar with. My
problem is this: I learn best from looking at examples of code
demonstrating the principle I'm learning. I'm not looking for anyone
to spoon-feed me. I'm prepared to sweat a little (okay, alot) at the
keyboard to become a good programmer. However, seeing a basic example
of how it's done will be a great help.

Any takers? Or should I say givers?

Thanks again,

John Arcidiacono
he··.@tu.··i.net
```

#### ↳ Re: HELP WITH LINKED LISTS

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33658920.463873282@news.tu.infi.net>`
- **References:** `<33658920.463873282@news.tu.infi.net>`

```

This is interesting. At the risk of putting my foot in my mouth, I (14
years COBOL experience, various platforms), have only HEARD the term Linked
List and I really don't know what they are. I may very well use them every
day, for all I know, but I don't know what is meant here by that term! I
await other comments!


John Arcidiacono wrote in article
<336··.@new··i.net>...
› Hello and thanks for reading this,
› 
…[25 more quoted lines elided]…
›
```

##### ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p2@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap>`

```

In <01bc54cb$1b015e20$43f548a6@thane-hubbell>, "Thane Hubbell" writes:
› This is interesting.  At the risk of putting my foot in my mouth, I (14
› years COBOL experience, various platforms), have only HEARD the term Linked
…[15 more quoted lines elided]…
›› weeks.

Some new varient of COBOL must have pointers. That's all you
need although you can simulate linked lists using arrays and
subscripts.

COBOL has supported chained records in auxliliary storage, VSAM
and ISAM are pointers to chained records, the same concept lives
at the heart of IMS. If you understand VSAM and IMS, you've got
the concept.

The basic idea is a memory record, a structure, contains data and
a pointer or pointers to other records. Subroutines understand
the chaining and calls to subroutines return the next record,
previous record, insert a record following the current, delete a
record and reconnect the chain, etc.

Just like VSAM but in memory.

It helps to be able to GETMAIN and FREE and get address of,

The power is in the flexibility, the downside is that arrays are
faster for SOME applications and link lists are complicated
unless you have a set of prebuilt functions.

I hope that Ross guy considers this technical enough.

Cory Hamasaki http://www.kiyoinc.com
HHResearch Co. OS/2 Webstore & Newsletter
REDWOOD
```

##### ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-04-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p2@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap>`

```



Thane Hubbell wrote in article
<01bc54cb$1b015e20$43f548a6@thane-hubbell>...
› This is interesting.  At the risk of putting my foot in my mouth, I (14
› years COBOL experience, various platforms), have only HEARD the term
…[4 more quoted lines elided]…
› await other comments!
A linked list that may be familiar with a COBOL programmer would be using a
POINTER type field to chain through a series of storage areas which in and
of themselves contain a pointer (address) to the next field ... Ever chain
through some CICS control blocks ... or build a series of GETMAINed areas
in a CICS program? That's a linked list! Not something COBOL types
usually do!
```

##### ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "he..." <ua-author-8810531@usenetarchives.gap>
- **Date:** 1997-04-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p2@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap>`

```

On 29 Apr 97 18:28:11 GMT, "Thane Hubbell" wrote:

› This is interesting.  At the risk of putting my foot in my mouth, I (14
› years COBOL experience, various platforms), have only HEARD the term Linked
…[3 more quoted lines elided]…
› 

Thane -

Thanks for reading my original post and taking an interest.

Here's what I've learned in my readings:

A linked list is a data structure. It can be created in dynamic
memory by languages that allow for that, or with an array of set
length. My understanding is that COBOL doesn't support dynamic memory
allocation.

A COBOL linked list, then , would have the following properties.

It has a head ( a pointer to the start of the list ) and , in a
doubly-linked list, a tail ( a pointer to the end of the list ) .
There is a 'Next' pointer to the next available (physical) place in
the array and a working pointer to help with adding and deleting items
in the array.

The array itself contains the actual data, a 'Next' pointer to the
next logical data item and, in a doubly linked list, a 'Previous'
pointer to the previous logical data item.

Data items can be added to or deleted from the linked list, and data
retrieved from it without constant resorting.

This is a beginners take, and I'm sure there's alot of holes and maybe
some incorrect interpretations.

I hope this helps you recognize what I'm talking about ( with all your
experience, I'm sure it's something you HAVE been using, if not
building).

Again thanks for taking the time to respond, and I hope you, or
someone else out there can help with a coded example and save me alot
of trial and error.

Sincerely,

John Arcidiacono
he··.@tu.··i.net
```

###### ↳ ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "kbr..." <ua-author-7376390@usenetarchives.gap>
- **Date:** 1997-04-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p5@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap> <gap-e0b4dcc20d-p5@usenetarchives.gap>`

```

The really cool thing about linked lists is not having to know at
compile time how big they will get, which is completely lost if you
build one in a working storrage table in COBOL. No COBOL I ever used
supported dynamic memory allocation. IBM COBOL II and COBOL/LE370
both support "ADDRESS OF" and "SET ADDRESS OF" clauses for 01 level
linkage section items, and "USAGE IS POINTER" for address items.
Everything you need is there except for actually allocating the memory
dynamically. For that you must go over to the dark side, and call a
simple assembly language subroutine. You pass a length to the
subroutine, which allcoates that much memory and returnd the address
in a pointer type parameter. Then you "SET ADDRESS OF list-element TO
pointer-paramter" and you're in business. The actual Assembler
subroutine is almost trivial in 370 Assembler, so I believe it would
be simple on any platform.
```

###### ↳ ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p5@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap> <gap-e0b4dcc20d-p5@usenetarchives.gap>`

```

To Computer Science Students everywhere:

Yes, a 'linked list' is a 'data structure', and as a result does not
actually exist in real life. I've been doing this (MF COBOL) for a few
years myself and have never heard the term used since graduating from
college.

Note: My 'data structures' professor was a real jerk. Also, the course
was tought using PASCAL, for whatever that's worth :-)

(ps. If ever there were an open invitation to flaming this may be it,
but *please* don't e-mail it! Put it here so we can all get a good
laugh)

Jim Van Sickle
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

###### ↳ ↳ ↳ Re: HELP WITH LINKED LISTS

_(reply depth: 4)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p7@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p2@usenetarchives.gap> <gap-e0b4dcc20d-p5@usenetarchives.gap> <gap-e0b4dcc20d-p7@usenetarchives.gap>`

```



Jim Van Sickle wrote in article <336··.@i··.net>...
› To Computer Science Students everywhere:
› 
…[3 more quoted lines elided]…
› college.

I couldn't agree more. I shall now employ some generalities about
academics and apologise in advance to those few (and I'm sure they must
exist somewhere) who are not subject to my generalisations.

Sadly for those of us in the real world, we have to cope with the products
of academia and the fact that academics know nothing about the
business-oriented IT world where COBOL thrives.

Thus when they teach COBOL (I believe there are a few left) they teach
their students to write it just like C insofar as they can. They
illustrate the language with the huge multilevel, multipage IF and PERFORM
statements that they love. They depart so far from one of the original
principles of the language - that it should be English-like and should be
understandable to the non-programmer. That is, after all, the reason for
the subject-verb-object construct employed in the PROCEDURE DIVISION.

As for linked-lists, they just love to read an entire datafile into memory
and sort it on the fly when most of us out here in the world have utility
software to do this for us. How many times in the business world do we
need to insert a keyed record into a file and undertake the linked-list
process? I think not at all.

The linked-list and other C techniques are probably necessary for those who
use a language that is incapable of understanding the concepts of files and
databases. I found during my postgraduate study over a year ago that the
academics were also incapable of understanding basic business concepts such
as never using floating point arithmetic for money calculations.

When I raised such matters, especially in light of a quarter of a century's
experience on the front line, they would just brush over it.

If I give the impression that I'm brassed off with academics, it's true.
My concept was to do some postgraduate study with a view to learning a few
things and to formalise my computer experience into a piece of paper that
is understood by human resources morons. Well, apart from getting the
piece of paper, the rest of the experience was a waste of my time, money
and revenue-earning potential.

Gosh, I've done it again! A short reply has changed into a diatribe.
Sorry.

---
>From the quill pen of Charles F Hankel
```

#### ↳ Re: HELP WITH LINKED LISTS

- **From:** "trevor powdrell" <ua-author-17072182@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p9@usenetarchives.gap>`
- **In-Reply-To:** `<33658920.463873282@news.tu.infi.net>`
- **References:** `<33658920.463873282@news.tu.infi.net>`

```

This looks like a C or Pascal class that has been converted to teach
Cobol. Although I have come across samples of implementing linked lists
in Cobol
(Microfocus Compliations. Can't remember which issue. Try there web site
http://www.microfocus.com/Marketing/compilations/comissue.htm)
I have never seen them used in an actual business application in my 14
years experience. This of course means next week my manager will ask me
to fix a bug in a program that contains a listed list. If I stretch it
out a little I might not have to go back to the year200 project I am on.

John Arcidiacono wrote:
› 
› Hello and thanks for reading this,
…[24 more quoted lines elided]…
› he··.@tu.··i.net

How to waste 2 hours trying to come up with something original 
in your signature file.
```

#### ↳ Re: HELP WITH LINKED LISTS

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-29T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p10@usenetarchives.gap>`
- **In-Reply-To:** `<33658920.463873282@news.tu.infi.net>`
- **References:** `<33658920.463873282@news.tu.infi.net>`

```

What COBOL compiler and platform do you intend to utilize?
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: HELP WITH LINKED LISTS

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-30T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p11@usenetarchives.gap>`
- **In-Reply-To:** `<33658920.463873282@news.tu.infi.net>`
- **References:** `<33658920.463873282@news.tu.infi.net>`

```

John Arcidiacono ?

Here's where you turn things around a bit, and alter the situation to fit the
tools at hand. Being human, this should not be a problem (human beings excel at
turning situations around to fit their own needs).

What you're looking to do is build something that the current incarnation of
COBOL isn't capable of doing: dynamically allocate RAM so you can store
information with a pointer to the prior entry and a pointer to the next entry.
Assuming, of course, that you don't have access to a language like Pascal or C
or BASIC, or Assembly.

I had to do this once (keep track of a series of choices made by the users on
any number of menus, where each choice would lead to another menu with more
choices - the idea being that I would 'back' the user out the way they came
in), and all I could code in was COBOL/400. Keep in mind that there was no
limit to the number of menus that any user could traverse.

Solution? Turn the situation around to fit the COBOL/400 scene: an indexed file
in the QTEMP area that kept track of the individual's menu choices, where the
key was the choice sequence (1st choice was +1, 2nd choice was +2, etc.), and
the data was the name of the menu and the value of the choice itself so I could
redisplay the menu, and high light the previously chosen option as I backed
out. Since the AS/400 is an excellent I/O machine, and COBOL/400 comes with the
READ NEXT and READ PRIOR capabilities built-in, I was in business. At the start
of the program, I used QCMDEXC to issue a CPYF to place a fresh version of my
'dynamic memory' indexed file into QTEMP, and then an OVRDBF to point at the
file I'd just created (all from within the COBOL program -- you'd be amazed at
the things you can do inside a COBOL/400 program!). Then, as the user made menu
choices, I'd store them in the file, each one being a separate entry. When the
user wanted to back out, I'd read the prior entry, delete it, and display the
menu, high lighting the choice.

Result: a COBOL/400 style linked list, implemented as only a COBOL program can
do it.

Ohhh... at the end of the program, I used the same QCMDEXC to issue a DLTF, so
the physical file would be removed from the QTEMP area.

Since the QTEMP area on the AS/400 is unique to each process (you have five
sessions going, you have five, unique QTEMP areas available to you
automatically), I didn't have to worry about two users clashing.

I'm not sure how I'd do this using VAX/COBOL... though, I suppose, with the
long file name capabilities of VMS (sadly lacking under OS/400), it would be
easy to create an RMS file with the user's PID as part of the name, and then
follow the same scenario. Hmmm... I don't recall READ PRIOR being part of
VAX/COBOL though. No problem: just keep track of the last entry number in
WORKING-STORAGE, and do a random read to retrieve that entry when the user
backs out. Then delete the entry, and subtract 1 from the counter. Everything
else would be about the same, except that the file would have to be
created/deleted in the DCL, since there isn't anything like QCMDEXC under VMS.

I have no idea how this would be accomplished under something like MVS... or
whether something like this would even be possible. Any of you MVS gurus out
there care to give an example of how this could be done using COBOL in the
mainframe environment??
```

##### ↳ ↳ Re: HELP WITH LINKED LISTS

- **From:** "hca..." <ua-author-6878906@usenetarchives.gap>
- **Date:** 1997-05-01T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0b4dcc20d-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0b4dcc20d-p11@usenetarchives.gap>`
- **References:** `<33658920.463873282@news.tu.infi.net> <gap-e0b4dcc20d-p11@usenetarchives.gap>`

```


"The Programmer" wrote:

› John Arcidiacono ?
 
› What you're looking to do is build something that the current incarnation of
› COBOL isn't capable of doing: dynamically allocate RAM so you can store
› information with a pointer to the prior entry and a pointer to the next entry.
› Assuming, of course, that you don't have access to a language like Pascal or C
› or BASIC, or Assembly.

My shop is preparing to migrate to Cobol for MVS which utililizes
Language Environment for MVS. In reading through the programing
reference guide to LE/MVS, I've discovered that LE/MVS provides a
callable service to allocate additional heap storage areas(or
non-destructively enlarge existing heap storage areas) and to
allocate memory from heap storage areas. Thus it would seem that
using Cobol/MVS you can dynamically allocate memory.

Harry Carter
hca··.@clu··s.net - finger for PGP key
Home Page: http://www.mcs.net/~hcarter

"Make no little plans; they have no magic to stir men's blood."
Daniel Burnham
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
