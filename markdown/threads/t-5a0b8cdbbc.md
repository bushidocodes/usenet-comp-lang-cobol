[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student 'green' in Cobol seeks insight.

_10 messages · 10 participants · 1997-08 → 1997-09_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Student 'green' in Cobol seeks insight.

- **From:** "lorto..." <ua-author-8826452@usenetarchives.gap>
- **Date:** 1997-08-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970817155500.LAA18110@ladder02.news.aol.com>`

```

I am new to Internet & Cobol (programming student). I have been
spending some time reading this group, though, and I have a question for
the moderator.

Would this be an appropriate venue to ask the following types of q's:
- can I have examples of what an entry-level programmer's job is like
- how much JCL do you actually code on the job
- give me an example of a 'maintenance' assignment
- am I allowed to ask for help, even though q's may seem basic-level;
I am having a great deal of trouble comprehending 'Tables', for example.
I know this concept is basic to programming. Right now, I am in a big
rut on
project using tables. I have a learning disability, and need to
'mentally' visualize the navigational concept of tables rather than
just reading about them.

If you can't help, do you someone who can...thanks in advance for your
help.
```

#### ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-08-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970817155500.LAA18110@ladder02.news.aol.com>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com>`

```

LORTOM5257 wrote:
› 
›   I am new to Internet & Cobol (programming student).  I have been
› spending some time reading this group, though, and I have a question for
› the moderator.
 
› I think that we don't have a moderator, so here goes.
 
›   Would this be an appropriate venue to ask the following types of q's:

I suppose it is. I'll do my best to keep it short and sweet; there are
plenty of others here who will help as well.

› - can I have examples of what an entry-level programmer's job is like

Normally, a trainee/entry-level programmer will be given similar work to
the average programmer though possibly simpler assignments or more time
will be allowed. You will usually have several people to ask about how
to do various things.

› - how much JCL do you actually code on the job

You can go for weeks without coding any JCL, and then you may have to
deal with a whole bundle of it. It all depends on the situation at any
given time.

Some installations actually have a rule that programmers don't do JCL,
though this can be obstructive rather than constructive. I have
experienced this first-hand and a colleague has also experienced it at
another site.

› - give me an example of a 'maintenance' assignment

These vary considerably. You could be asked to investigate a problem
and sort it out, or you may be given an extremely detailed specification
right down to the line number that you should change. Again, this
depends on the normal practice of the site you work at.

› - am I allowed to ask for help, even though q's may seem basic-level;
 
› Of course.
 
›   I am having a great deal of trouble comprehending 'Tables', for example.
›   I know this concept is basic to programming.  Right now, I am in a big
…[3 more quoted lines elided]…
› just reading about them.

Start thinking of an average table being merely a list. Each item in
the list is a table entry.

A subscript is a number that you use to look at, say, the tenth item on
the list, such as WA-ENTRY (10).

An index is really a pointer to the table entry's address but, for most
purposes at this stage, you could think of it as being the same as a
subscript in that you would set its value to ten to look at the tenth
entry in the table. Just remember that it is not the same as a
subscript and that it works in a different way.

Generally speaking, an index is the better thing to use because it is
usually more efficient than a subscript, but this does not stop you
using a subscript if you want to.

Concepts also come with time and practice - not necessarily during a
lesson.

› If you can't help, do you someone who can...thanks in advance for your
› help.

Ask your questions of the group because some of us are not able to use
e-mail every day, or access the newsgroup every day. However, there
will usually be someone who looks at it who can help out a bit.

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

#### ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "vernon l. cole" <ua-author-17073392@usenetarchives.gap>
- **Date:** 1997-08-16T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19970817155500.LAA18110@ladder02.news.aol.com>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com>`

```

'll take a shot at the 'Table' question.

A table is a way of organizing data so that specific data can be
retrieved.

Visualize a table in the form of a book. The name of the book is the
name of the table. The book is made up of pages (page 1, page 2, ...
page n). Each page is made up of lines (line 1, line 2, ... line n).
Each line is made up of words (word 1, word 2, ... word n).

There is only one 'page 1' in the book, but there is a 'line 1' on each
page, and a 'word 1' on each line.

Assign an index (or subscript) to represent the values of page, line,
and word, and you can navigate your way around the book as if it were a
three-dimensional table.

I could tell you, for instance to do the following. "Take the book
Robinson Crusoe. Turn to page 37. Look at line 11 on that page. Find
the third word on that line and say it out loud."

If you can do that, you are on your way to handling tables in COBOL.




LORTOM5257 wrote:
› 
›   I am new to Internet & Cobol (programming student).  I have been
…[22 more quoted lines elided]…
› help.
```

##### ↳ ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "hoy..." <ua-author-4372734@usenetarchives.gap>
- **Date:** 1997-09-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5a0b8cdbbc-p3@usenetarchives.gap>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com> <gap-5a0b8cdbbc-p3@usenetarchives.gap>`

```


I think that this is an appropriate place to ask your COBOL questions.

I will try to answer the questions about an entry-level programmer's
job. To give you an idea of what I am basing my answer on, I am in
South Africa, working at a big COBOL and Adabas/Natural site. When I
arrived I only worked in Natural, but now (nearly 2 years later) I am
working in COBOL as well. I have mainly written batch programs, so my
Natural experience can be easily translated to COBOL.

› - can I have examples of what an entry-level programmer's job is like
I worked under a systems analyst, who either gave me a spec on paper,
or explained what was wanted of me. I soon found that taking notes
when things were explained was the only way to remember anything. My
first project was to write a program to fix faulty data on a file, to
prepare it for a new development that someone else was doing. The
programming part of the project was fairly simple, just updating 2
fields on the file, but this project introduced me to all the other
things that are part of a programmer's job. I had to write the JCL for
the job to run on test and live. I had to copy programs to the test
database for testing. Then I learnt how to fill in a change control
which allowed my program to be copied to and run on the live machine.
In all these jobs I was guided by an analyst/ programmer. This first
time, he did most of the admin type things, and I watched so that the
next time I could do it myself.

› - how much JCL do you actually code on the job
I code all the JCL for running my batch jobs for testing, and the live
JCL for when the program goes live. Each time I "code" JCL, I am
really just copying and adapting a previous piece of JCL - originally
people in my department gave me their JCL to adapt. Some things like
my compile JCL I still don't understand, I just use it.

› - give me an example of a 'maintenance' assignment
It depends what you mean by maintenance. Often maintenance of an old
system means writing new programs that enhance the system. This feels
like new development to the programmer. On the other hand, one can be
told to add a particular line of code in a particular place in a
program. One can also be asked to find out what is wrong with a
particular function of the system, and fix it as seems appropriate. In
all cases it is best to ask lots of questions to get the background of
your small change. Then you learn about the system, and are more
capable of more interesting work.

As far as tables go, I find it easy to visualise a 2-dimensional table
as a table like one sees in a wordprocessing package or a spreadsheet.
3-dimensional is harder, but if you imagine it like a Rubic's Cube you
have an idea.

Beccy
```

#### ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "alan" <ua-author-30212@usenetarchives.gap>
- **Date:** 1997-08-17T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19970817155500.LAA18110@ladder02.news.aol.com>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com>`

```

›   I am having a great deal of trouble comprehending 'Tables', for
› example.
…[8 more quoted lines elided]…
› 

A SIMPLE example using subscripting (efficiencies aside)....

01 W-DATE.
05 W-YEAR PIC 9999.
05 W-MONTH PIC 99.
05 W-DAY PIC 99.
01 YT-YEAR-TABLE.
05 YT-MONTH OCCURS 12 TIMES.
10 YT-DAY OCCURS 31 TIMES.
15 YT-WHATEVER-DATA.
...

to navigate to YT-WHATEVER-DATA for a particular day, reference as...

YT-WHATEVER-DATA (W-MONTH,W-DAY)

or April 15 as...

YT-WHATEVER-DATA (4,15)

YT-MONTH defines a list of 12 months. Within each month, YT-DAY defines a
list of 31 (maximum) days.

Hopes this helps.
Alan
```

#### ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "art daly" <ua-author-6588987@usenetarchives.gap>
- **Date:** 1997-08-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<19970817155500.LAA18110@ladder02.news.aol.com>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com>`

```

I am also in the Green Stage and we are starting some hands on training
in JCL and ISPF/TSO I am wondering how much a
new programmer would spend working with these tools as opposed to the
straight heads-down grunt,groan, and code?? Thanks,

art daly
art··.@pei··o.ca
```

##### ↳ ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-08-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5a0b8cdbbc-p6@usenetarchives.gap>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com> <gap-5a0b8cdbbc-p6@usenetarchives.gap>`

```

art daly wrote:
› 
› I am also in the Green Stage and we are starting some hands on training
…[5 more quoted lines elided]…
› art··.@pei··o.ca


If you're working in an IBM mainframe environment, TSO/ISPF and JCL will
be joined at the hip with you. Since TSO/ISPF is the primary
environment for entering and editing your program source, you should
find that you should become confortable with it quite rapidly. ISPF
will also be the primary access for third-party tools.

JCL--it's going to be with you, too. In all of the years I have been in
this business, I have found that most people dislike JCL more than just
about anything. I never did, but then I've had more involvement with it
than just programming tasks, and never minded it. Just consider these
things as tools and parts of the solution to your tasks. These will be
just a few of things you will encounter along the way!

Mike Dodas

(Remove NOSPAM! for e-mail replies)
```

##### ↳ ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "k..." <ua-author-612019@usenetarchives.gap>
- **Date:** 1997-08-19T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5a0b8cdbbc-p6@usenetarchives.gap>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com> <gap-5a0b8cdbbc-p6@usenetarchives.gap>`

```

On Tue, 19 Aug 1997 20:40:19 -0700, art daly
wrote:

› I am also in the Green Stage and we are starting some hands on training 
› in JCL and ISPF/TSO   I am wondering how much a 
› new programmer would spend working with these tools as opposed to the 
› straight heads-down grunt,groan, and code?? Thanks,
› 
Art,
I spent 8 hours today with a TSO session up and running using ELIPS
to research code in the librarian file, DB2 Proedit to verify some new
DB2 table structures, and ran several JCL jobs to search librarian and
pds files. I also spent a few hours in Word and Excel updating design
documents and estimate level-of-effort worksheets.

I'm a mainframe development programmer and probably spend less than
10% of my time actually hacking code. I did get to crank out a new
program Monday afternoon. JCL and TSO are usually the items new-hires
don't understand and are usually part of the learning curve. Get to
know it as well as Cobol if you plan on working mainframes. It will
be a great plus if you learn it in school.



Cheers,

Kevin........."Due to SPAM, remove KEV and replace
with KKLT1 when replying by email"
```

##### ↳ ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "tracy gilmore" <ua-author-14378979@usenetarchives.gap>
- **Date:** 1997-08-19T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5a0b8cdbbc-p6@usenetarchives.gap>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com> <gap-5a0b8cdbbc-p6@usenetarchives.gap>`

```

JCL is grunt work of sorts. It is the Language that MVS uses to actually
run your programs. ISPF/TSO provides more usable tools to key, compile,
run and view output from your programs . Without JCL and a tool to view
output, what good will the program be.

art daly wrote in article
<33F··.@pei··o.ca>...
› I am also in the Green Stage and we are starting some hands on training 
› in JCL and ISPF/TSO   I am wondering how much a
 
› new programmer would spend working with these tools as opposed to the 
› straight heads-down grunt,groan, and code?? Thanks,
…[3 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Student 'green' in Cobol seeks insight.

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-08-20T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5a0b8cdbbc-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5a0b8cdbbc-p6@usenetarchives.gap>`
- **References:** `<19970817155500.LAA18110@ladder02.news.aol.com> <gap-5a0b8cdbbc-p6@usenetarchives.gap>`

```

If you plan to make a living in the IBM mainframe world, then you will need
to know JCL at some point. Very few shops do not require their programmers
to do at least some of their own JCL. You will be less useful to potential
employers (and hence, be paid less, be less employable) if you don't know
it. If you are familiar with PC-DOS batch files, then JCL is just a
somewhat more complicated (and richly functional) approach to the same
problem. The key part on which to concentrate is the DD card. That's what
you'll have the most of, and that's what's got the most options (hence, the
most complicated).

As to ISPF/TSO, that is to MVS as the C:\ prompt is to DOS. While there
are lots of other things which could be used (and are), TSO/ISPF is the
most common (like 98% of the shops), so get used to it now. You don't need
to know how to code for an ISPF screen dialog, but you'd better know how to
use the ones supplied. It is, in fact, so common that programmers will
talk about operations in it by just the standard menu numbers. For example

Statement Translation
'Do a 3 dot 4 on SOC.MW1000 and Go to menu option 3, sub menu 4,
tell me what you see...' which is file list, and display all of
the cataloged files with dataset
names beginning with
'SOC.MW1000'

'Oh, set the PF key 24 on 0 dot 1' Go to menu 0, sub menu 1,
terminal options, and use the
option to set 12 or 24 pfkeys on
your terminal emulator

'Go 3 dot 1 4 on ...' Use the string search utility -
menu 3, submenu 14 - to search a
library for a string

The bottom line is, if you are employed on a system with TSO, you had best
know how to use it. ISPF itself is not as hard as it looks (it's primarily
a command interpreter), and most of the products under it (the editor, the
browser, third party products) make more sense when you have a specific
assignment in hand.

Good luck.

art daly wrote in article
<33F··.@pei··o.ca>...
› I am also in the Green Stage and we are starting some hands on training 
› in JCL and ISPF/TSO   I am wondering how much a
 
› new programmer would spend working with these tools as opposed to the 
› straight heads-down grunt,groan, and code?? Thanks,
…[3 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
