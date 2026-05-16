[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unstructured Programming in COBOL

_15 messages · 10 participants · 2000-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Unstructured Programming in COBOL

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<879g6q$fhe$1@nnrp1.deja.com>`

```


Hi:

I read the post by RMP Consulting Partners LLC about structured
programming and thought I would say something.

Surely, the objective of application development is to produce
a totally dependable, self-documented, easy-to-learn, easy-to-use,
efficient and economical-to-operate software system to accomplish
a particular task.  The programming style should be subordinate to
the objective.

I have been an active programmer for almost 40 years and can still
turn out a couple of hundred lines of debugged code in a day. I have
never
embraced the structured style although I experimented with it in
the sixties. I have programmed in many languages on many different
platforms. I have used PL/I, ALGOL, FORTRAN, various assembler
languages, RPG and FARGO(!), etc. but my overall favorite which I
use to this day is MicroFocus COBOL with Multi-Key ISAM (Using
the truly marvelous FLEXUS GUI) (Who needs CICS?). My programs use
GO TO, PERFORMS and all those other things which are despised by
the structured devotees (although ALTER is never used).  Furthermore,
I use a subset of COBOL consisting of only the barest essentials.
I never use EVALUATE or any of the modern stuff. (There is one
very important benefit to this approach and that is that the COBOL
code is highly portable and can be converted to another compiler not
only in a relatively short time but with a high degree of confidence
that the converted code will not contain mysterious bugs caused
by the use of 'obscure' coding methods. SORT and REPORT-WRITER
are NEVER used.)

The problem which structured programming attempts to address is
poor programming when, in actuality, poor programming arises from
poor design. Furthermore, sloppy, horrible code can be, and is,
written in any language.

In the olden days, there were programmers and coders. The programmer
DESIGNED the program and the coder CODED FROM THE FLOWCHART.

Unfortunately, programming is not taught anywhere that I am aware of.
People go to school to learn a programming language, and, having taken
the course, it is assumed that since they 'know' the language they
know how to program. Knowing COBOL or any other language does not
mean that one knows how to program. Getting a 'Computer Science'
degree, in my opinion, is totally useless for a COBOL application
programmer.

If a program is PROPERLY designed by someone who knows what to do,
there is no reason why the program can not be written in a non-
structured style. Although efficiency in software is a largely
forgotten and irrelevant consideration, the purist should derive
satisfaction from designing a program which considers every
logical eventuality, and is a model of efficiency and clarity.
This can be done, but not by many and not by anyone without a
LOT of experience.

The reason most software is so horrible is that it is written
by people with no or little experience. They start to write something
without really knowing how to do it, encounter problems, devise
crude solutions which complicate it further and end up with a shaky
liability. Windows is a perfect example of software written
by amateurs.

Perhaps, every program should be written twice: the first
time to find out what the problems are and the second to write it
properly.

As a commercial-application programmer, I rarely write programs from
scratch. In the world of commercial data-processing there are two
primary types of programs: File-Maintenance programs and 'Report'
programs. The former let users add, change, delete, records from
files and may provide other basic functions pertaining to the
data. 'Report' programs read files sequentially and produce some
output; normally a report or display.  I have hired and supervised
trainee programmers who could 'write' programs of this type using
skeleton-program generators which produce the efficient type of
code mentioned above. Virtually all systems can be developed using
only programs of these two types.  I wonder if someone could come
up with a structured File-Maintenance skeleton-generator?

The biggest single factor in the design of ANY system is the
design of the DATA FILES to be used. Poor file-design will lead
to amateurish solutions to problems arising because of the poor
design. (And, no, I don't leave 'gaps' in my level numbers!).

My objective during my programming career has been to design
and program applications which require no external documentation,
are completely self-explanatory, are totally dependable and do
NOT require telephone support. I am happy to say that I have
succeeded and I did (and still do it) in my unstructured way.

Anthony Dilworth

p.s. there are many varieties of spaghetti.






Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** shine98@my-deja.com
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<879j7p$htr$1@nnrp1.deja.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```
I'm interested in what you have, can you show me some of these these
programs or elaborate on some of the principles? I really think that you
are right in saying that a well though out data structure makes the
programming so much easier and clearer, but could you please elaborate.

Thanks.

~shine


In article <879g6q$fhe$1@nnrp1.deja.com>,
  Foodman <foodman123@aol.com> wrote:
>
>
…[97 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EOXl4.78357$Dv1.2238950@news2.rdc1.on.home.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```

"Foodman" <foodman123@aol.com> wrote in message
news:879g6q$fhe$1@nnrp1.deja.com...
>
>
…[3 more quoted lines elided]…
> programming and thought I would say something.

<<SNIP>>

> only programs of these two types.  I wonder if someone could come
> up with a structured File-Maintenance skeleton-generator?
>
Where have you been? There are hundreds of companies doing just this. I work
for one such company and would be delighted to tell you all about it, but
not in the newgroup.

<<SNIP>>


> p.s. there are many varieties of spaghetti.

A long time ago we had a discussion in R&D about being able to produce
programs in a variety of coding styles. We developed the concept of 'pasta
programming' and decided the optimum was ravioli.

spaghetti - a mess
spaghetti and meatballs - a mess with a few meaty bits worth keeping
lasagna - way too structured with performs of performs of performs of
paragraphs
fetuccini - kind of like spaghetti but a little more manageable
fetuccini alfredo - you think it's manageable until your arteries clog
ravioli - manageable bite-size pieces with substance in the middle

-- Karl Wagner

>
>
…[5 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-jtqN8HLJ6ddd@localhost>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <EOXl4.78357$Dv1.2238950@news2.rdc1.on.home.com>`

```
Trevor sez, "Oscar T. Grouch" <dustbin@home.com> keyed the following on Wed, 2 Feb 2000 15:11:32:

> the optimum was ravioli

ROFLMAO!   *That* one's a keeper!  Thanks..

=Dwight=
X1=L, X2=L & the domain is phonetic
```

##### ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LDC2mLA$BFm4EwZF@ld50macca.demon.co.uk>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <EOXl4.78357$Dv1.2238950@news2.rdc1.on.home.com>`

```
In article <EOXl4.78357$Dv1.2238950@news2.rdc1.on.home.com>, "Oscar T.
Grouch" <dustbin@home.com> writes
>
>
…[7 more quoted lines elided]…
>
What about:
   lasagna verdi - way too structured and written by someone who is a 
   little green around the gills 
   tagliattelli - a more manageable mess than spaghetti
   bows, spirals and shells?
```

###### ↳ ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VN1m4.673$kP3.18670@dfiatx1-snr1.gtei.net>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <EOXl4.78357$Dv1.2238950@news2.rdc1.on.home.com> <LDC2mLA$BFm4EwZF@ld50macca.demon.co.uk>`

```
Alistair Maclean wrote in message ...
>>
>What about:
…[4 more quoted lines elided]…
>--


Please, Alistair, do you really have to share the details of your sordid
pasta?

MCM
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38985021.D856C72A@NOSPAMwebaccess.net>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```
Foodman wrote:

> In the olden days, there were programmers and coders. The programmer
> DESIGNED the program and the coder CODED FROM THE FLOWCHART.

Or from pseudo code.  The coder was just a clerk, and nobody wanted to be
a coder.  Now we're all programmers who can type, so the flow chart is
pretty much obsolete.

> The reason most software is so horrible is that it is written
> by people with no or little experience. They start to write something
> without really knowing how to do it, encounter problems, devise
> crude solutions which complicate it further and end up with a shaky
> liability.

I think the reason most software is so horrible is that it was designed,
written, and then changed a zillion times with changing business needs.
Unstructured programs have unstructured modifications all over the place,
and the concepts which flowed out of the original programmer's head have
been obscured by more unstructured code.  Neither the trees nor the forest
are really visible anymore.

So the goal in making better software is to write in such a way that the
changing requirements can be integrated in a readable, accurate
technique.  That is why structured programming is useful.
```

##### ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87f3ah$g1f$1@nnrp1.deja.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <38985021.D856C72A@NOSPAMwebaccess.net>`

```

> Foodman wrote:
>
…[3 more quoted lines elided]…
> Or from pseudo code.  The coder was just a clerk, and nobody wanted
to be
> a coder.  Now we're all programmers who can type, so the flow chart is
> pretty much obsolete.

We may all be able to type but that does not mean that we know how
to program. You suggest that one just sits down and starts merrily
typing and it all comes out alright in the end? I hope
that newcomers to programming are not led to believe that the
'flow chart is dead'. Certainly, a flow chart or its logical
equivalent should be the first thing prepared before typing.

One can learn programming without knowing a programming language by
drawing flow charts so long as one knows the fundamental capabilities
of the machine and the requirements of the application.

Tony


Tony


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389B1BAE.347225C4@NOSPAMwebaccess.net>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <38985021.D856C72A@NOSPAMwebaccess.net> <87f3ah$g1f$1@nnrp1.deja.com>`

```
> We may all be able to type but that does not mean that we know how
> to program. You suggest that one just sits down and starts merrily
…[3 more quoted lines elided]…
> equivalent should be the first thing prepared before typing.

My statement you quoted was more of an observation than a recommendation,
but...

It depends on the complexity.  It has been 20 years since I have seen
anybody create a flow chart before writing a simple extract, match, and
report program.  (in those days people flow charted each if, etc.).  I still
see (and write and use) data flow diagrams, batch dependency diagrams, etc.
And of course, flow charts can be a wonderful debugging tool.

I have seen similar overly detailed pseudo code as near as 10 years ago,
only because I have been primarily a consultant who has worked in many
shops.

Where there is a standard stand-alone program, the structured programming
does the same thing as the old style flow chart.

> One can learn programming without knowing a programming language by
> drawing flow charts so long as one knows the fundamental capabilities
> of the machine and the requirements of the application.

No argument there.
```

###### ↳ ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87fg3s$1mk$1@aklobs.kc.net.nz>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <38985021.D856C72A@NOSPAMwebaccess.net> <87f3ah$g1f$1@nnrp1.deja.com>`

```
Foodman <foodman123@aol.com> wrote:

: We may all be able to type but that does not mean that we know how
: to program. You suggest that one just sits down and starts merrily
: typing and it all comes out alright in the end? I hope
: that newcomers to programming are not led to believe that the
: 'flow chart is dead'. Certainly, a flow chart or its logical
: equivalent should be the first thing prepared before typing.

I used to do flowcharts a few decades ago, then structure
diagrams then I moved to pseudo-code.

However, I soon realised that when I used interactive text editors,
such as WordStar and such in the late 70s, that I was keying the
pseudo-code into the editor (rather than scribbling it down on paper)
and then revising it until it would work correctly and then going back
over it converting the pseudo-code into Cobol.

I found that by using Cobol _as_ the pseudo-code language I could
save a step and arrive at correctly working programs a good deal
faster.

I would agree, however, that each new programmer should go through
the process of learning logic through flowcharts, structure
diagrams and pseudo-code (or other equivalents) until they are
proficients in these and the language(s) they are using.  It is
a matter of abstraction.  I can abstract in Cobol because I no
longer need to think about the language (or those parts that I
actually use).  If a new programmer tried to use this technique
they would get distracted by the detailed usage of the language.
Pseudo-code is supposed to be simple and flexible so that one
can make it do whatever one wishes and then worry about 
implementing each item one at a time.
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** kownby@humboldt1.com (Kindrick Ownby)
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38986baf.10132069@news.humboldt1.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```
On Wed, 02 Feb 2000 14:50:03 GMT, Foodman <foodman123@aol.com> wrote:

>Surely, the objective of application development is to produce
>a totally dependable, self-documented, easy-to-learn, easy-to-use,
>efficient and economical-to-operate software system to accomplish
>a particular task.  The programming style should be subordinate to
>the objective.

It is good if the code can be understood by another if errors do arise
and/or enhancements are required. I assume that your style would
be consistent within a program or system.

>I have been an active programmer for almost 40 years and can still
>turn out a couple of hundred lines of debugged code in a day. I have
>never embraced the structured style although I experimented with it in
>the sixties. I have programmed in many languages on many different
>platforms. [...]

My experience has been similar.  I did use ALTER once in an
application for which it was efficacious.  And I have used the COBOL
in-line SORT. Otherwise, I agree with the approach of using only a
subset of the language.

[...]

I'll wager that, when confronted with some "new" approach to 
program design, that you have realized that you have been doing
that for years (without the almost religious fanaticism).

It's good to hear from another programmer from the 60's or
earlier.

Kindrick       (IBM 650, '57)
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** "Robert Kovacic" <rjk@bigpond.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N3cm4.6078$VJ1.9877@newsfeeds.bigpond.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```
Couldn't agree more.

Regards, Robert.

Foodman <foodman123@aol.com> wrote in message
news:879g6q$fhe$1@nnrp1.deja.com...
>
>
…[9 more quoted lines elided]…
> the objective..............
```

#### ↳ Re: Unstructured Programming in COBOL

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A4169DF2C6DB0F08.F056A108D67A8EBD.282B35A7547017D5@lp.airnews.net>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com>`

```
Anthony,

Along with some other interesting observations, you wrote:

> 
> In the world of commercial data-processing there are two
…[4 more quoted lines elided]…
> output; normally a report or display. 

I would add a third archetype:  the 'Posting' program (e.g., interface
Accounts Payable to General Ledger).  Posts are often structured like a
Report program, but the main function is to update one or more files. 
Typically a report is also produced (the posting journal), but it is
secondary to the main update function. 
```

##### ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87f27q$fbh$1@nnrp1.deja.com>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <A4169DF2C6DB0F08.F056A108D67A8EBD.282B35A7547017D5@lp.airnews.net>`

```
Hi David:

The example you give is really another 'Report' program. Read the
A/P file sequentially, post directly via ISAM to the other files
and print a report. The sequential reading of the A/P file is
the 'logical process' which is the heart of the program and which makes
it fit into the 'Report' category. Maybe 'Report Program' is not a good
name for these; perhaps 'Sequential-Process Program' might
be a better name instead. (Besides, we need more things to make
acronyms from).

tony

In article
<A4169DF2C6DB0F08.F056A108D67A8EBD.282B35A7547017D5@lp.airnews.net>,
  "David W. Furin" <dfurin@larich.com> wrote:
> Anthony,
>
…[11 more quoted lines elided]…
> Accounts Payable to General Ledger).  Posts are often structured like
a
> Report program, but the main function is to update one or more files.
> Typically a report is also produced (the posting journal), but it is
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Unstructured Programming in COBOL

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<07E77CA3EADEAFC0.4C868DD19C4CF535.B71432381F2FEB38@lp.airnews.net>`
- **References:** `<879g6q$fhe$1@nnrp1.deja.com> <A4169DF2C6DB0F08.F056A108D67A8EBD.282B35A7547017D5@lp.airnews.net> <87f27q$fbh$1@nnrp1.deja.com>`

```
Hi Tony:

You're right--the essential logic driving a report and 'post' is the
same, but I always mentally separate the two.  I can run a 'report' over
and over without harm, but I can only run a 'post' once.  If we're going
to invent acronyms we could keep things simple:  FM (file maintenance)
and SP (sequential process)   :-)



Foodman wrote:
> 
> Hi David:
…[11 more quoted lines elided]…
> 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
