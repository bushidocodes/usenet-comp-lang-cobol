[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hobby languages

_69 messages · 19 participants · 2010-07_

---

### Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-19T09:44:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```

I was thinking about my retirement, and I have written CoBOL programs
that figured out puzzles and fun stuff.   My choice of languages is
based upon being a competent CoBOL programmer.  

Let's say I want to write a Sudoko puzzler, a Rubic's Cube solver, or
a word puzzle solver.   My home computer is a Mac and I expect this
won't change when I retire.

What languages would you recommend for such a person?
```

#### ↳ Re: Hobby languages

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-19T12:19:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<db614e6f-1620-4897-a184-2fe9e57c0c33@5g2000yqz.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
On Jul 19, 4:44 pm, Howard Brazee <how...@brazee.net> wrote:
> I was thinking about my retirement, and I have written CoBOL programs
> that figured out puzzles and fun stuff.   My choice of languages is
…[13 more quoted lines elided]…
> - James Madison

Try z390 Assembler. It might work on Macs but you would be best
advised to contact Don Higgins and ask him first.

Also, you could try BEFUNGE. This is a language which deliberately
obfuscates code so it could be fun.

Finally, SQL can be used to write a Sudoku solver (I have the code
somewhere). You would probably need the free version of MS SQL Server.

Wikipedia has a page devoted to a listing of different languages and
their attributes (Sorry but I couldn't find it but it is in the other
Wiki sections).
```

#### ↳ Re: Hobby languages

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2010-07-19T15:23:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4708a5e5-42e7-4049-a0a0-e5e5100641d6@g19g2000yqc.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
On Jul 19, 10:44 am, Howard Brazee <how...@brazee.net> wrote:
> I was thinking about my retirement, and I have written CoBOL programs
> that figured out puzzles and fun stuff.   My choice of languages is
…[6 more quoted lines elided]…
> What languages would you recommend for such a person?


For such tasks, a functional language like Haskell would probably be
your best bet.
```

##### ↳ ↳ Re: Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-20T09:44:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v1hb46ps25bocvu8u1g4snn9o4q6se6mn4@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <4708a5e5-42e7-4049-a0a0-e5e5100641d6@g19g2000yqc.googlegroups.com>`

```
On Mon, 19 Jul 2010 15:23:46 -0700 (PDT), "robertwessel2@yahoo.com"
<robertwessel2@yahoo.com> wrote:

>For such tasks, a functional language like Haskell would probably be
>your best bet.

What are the differences between taking up Haskell or taking up Lisp?
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2010-07-20T16:13:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<846abbec-4cdf-4f44-921d-6729d9b1d9b1@w12g2000yqj.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <4708a5e5-42e7-4049-a0a0-e5e5100641d6@g19g2000yqc.googlegroups.com> <v1hb46ps25bocvu8u1g4snn9o4q6se6mn4@4ax.com>`

```
On Jul 20, 10:44 am, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 19 Jul 2010 15:23:46 -0700 (PDT), "robertwess...@yahoo.com"
>
…[4 more quoted lines elided]…
> What are the differences between taking up Haskell or taking up Lisp?


Oh, dear, now *that's* a way to start a flame war...

For interminable discussions of Lisp vs. Haskell, just type that into
your favorite search engine.

Haskell is a pure functional language, and much smaller than Lisp.
Functional programming is very different from imperative programming.
Basically functions cannot have state or side effects, and can be
though of as doing something to their inputs (which are basically not
changeable), to produce an output.  IOW, existing data (using the term
loosely) in immutable - let's say you have a tree, inserting a new
node into the tree leads to a new tree with the new node in it, the
old tree still exists (eventually, if you stop using the old tree,
it'll get garbage collected away).  (And before anyone raises
efficiency concerns, the tree is almost never actually duplicated
under the hood, rather most of it's contents after the insertion
operation would get shared by the old an new trees).

By making all actions stateless, it eliminates huge classes of
possible bugs, and makes functions massively easier to analyze.  To
make a poor analogy, by eliminating goto's, structured programming
allows us to better understand our programs by greatly reducing any
confusion about how we got to a particular place in the program
(remembering that the issue is not the goto itself, rather the label
where it goes).  Eliminating variables takes that many steps further.

Spreadsheets are sometimes used as an example of a limited type of
functional programming - you specify cells as either being constants,
or as some sort of transformation of the contents of other cells, and
there's very limited notion of anything like assignment (in the sense
of assigning a new value to a variable).  Spreadsheets have a host of
different problems, and don't really demonstrate anything that you
might want to call (relatively) bug-free coding.

Functional programs are very often considerably shorter than
equivalent imperative ones, most Haskell proponents claim 2-10 times
less than an equivalent C program, and that's probably realistic
(although not for newbies who are still trying to write imperative
code in Haskell).

Anyway, it's impossible to do the subject any justice in a few
sentences, and I'll refer you to the Haskell Wiki instead:

http://www.haskell.org/haskellwiki/Haskell

Lisp, OTOH, is, well, Lisp.  You can do anything in Lisp, including
functional programming.  Lisp in many ways is not so much a language,
but en environment for creating new languages/paradigms/etc.  It might
actually be a bit easier to transition into Lisp from an imperative
background (since you reasonably hack out fairly imperative style
code).  Lisp is, in practice, a fairly large language.  The "core"
language is quite small (insofar as that's distinct from everything
else), but you really need the massive library that comes with it to
do anything.  In some senses it suffers the same multi-paradigm
problem as does C++, and a common problem is that programs written in
one style or paradigm are difficult to understand to practitioners of
another.  IMO, becoming an expert at Lisp is a rather bigger
undertaking that doing so for Haskell.  Which is not to say that Lisp
isn't worth learning, although I'd probable steer you towards Scheme
rather than Common Lisp on your first outing.

And if you're coming from a Cobol, or most imperative backgrounds,
you'll find either to be visually shocking experiences (although
totally unlike each other).  But syntax is just syntax.

And there are several decent implementations of Haskell, Scheme and
Common Lisp for the Mac.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-21T08:25:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p0e469n3lb4jdijp8pdg0nmdd19qk3fvu@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <4708a5e5-42e7-4049-a0a0-e5e5100641d6@g19g2000yqc.googlegroups.com> <v1hb46ps25bocvu8u1g4snn9o4q6se6mn4@4ax.com> <846abbec-4cdf-4f44-921d-6729d9b1d9b1@w12g2000yqj.googlegroups.com>`

```
I installed Haskell on my Mac.  The
haskell-platform-2010.1.0.1-i386.dmg file had the following files in
it:


GHC-6.12.1-i386
Haskell Platform 2010.1.0.1.pkg
Uninstall GHC

I installed the first two, and noted the directions in the final
screen of GHC-6.12.1-i386.   I didn't notice whether the platform had
instructions, so I installed it again and did see any instructions. I
don't know what it installed and I am not finding it anywhere.

I've found several sites giving the advantages of Haskell over Lisp,
but none going the other direction.
```

#### ↳ Re: Hobby languages

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-20T11:02:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ak3t5FrftU1@mid.individual.net>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
Howard Brazee wrote:
> I was thinking about my retirement, and I have written CoBOL programs
> that figured out puzzles and fun stuff.   My choice of languages is
…[6 more quoted lines elided]…
> What languages would you recommend for such a person?

 Why not do it in COBOL if that is what you are comfortable with?

(COBOL stringing/unstringing facilities might be very useful for a word 
puzzler...)

Procedural things like puzzle solving can be adequately done in COBOL 
although the solution may take a little more writing than in another 
language.

The real challenge is in devising the solution algorithm. Once you have done 
that, as Sir Ernest Rutherford remarked: "The rest is stamp collecting."

Really, it is only the user interface that might be easier in something like 
.NET or VB. I would write the "engine" as separate from the interface 
(communicate through a single block  (to simplify parameter passing) that 
contains data and response), and then you can plug it into a web page or the 
desktop.

Pete.
```

##### ↳ ↳ Re: Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-20T08:51:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net>`

```
On Tue, 20 Jul 2010 11:02:58 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

> Why not do it in COBOL if that is what you are comfortable with?
>
…[5 more quoted lines elided]…
>language.

Finding a good compiler for my Mac might be harder than learning, say
Lisp.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-21T18:26:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ani7uFr1vU1@mid.individual.net>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net> <qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 20 Jul 2010 11:02:58 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> Lisp.

Why not install Open COBOL?

While it doesn't support OO, you probably won't need OO for games (unless 
you are thinking about avanced adventure gaming, where there could be some 
advantages in using OO).

Back in the early 80's  when PCs were still far from established, I remember 
writing a Casino Blackjack game (in Basic) to run on a Sinclair ZX Spectrum, 
for a friend's kids. I didn't know Basic at the time and learned it for the 
exercise. It was a lot of fun to do, and the kids involved loved the 
resulting program. Basic was more than adequate for this task.

I tried Lisp on one project many years ago and found it excellent for data 
management and search, but I don't think I'd want to write a game in it.

Oddly enough, many of the arcade games that ran on Texas Instruments chips 
during the 80s and 90s were written in Pascal.

If it were me, and I was in your situation, I'd use Open COBOL. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2010-07-21T04:27:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68e1e396-03eb-423b-aecf-38e9db4e94bb@z30g2000prg.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net> <qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com> <8ani7uFr1vU1@mid.individual.net>`

```
On Jul 21, 2:26 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Howard Brazee wrote:
> > On Tue, 20 Jul 2010 11:02:58 +1200, "Pete Dashwood"
…[36 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

For my retirement.... I would create a "personal" blog on my website,
and of course watching the wheels turn around (John Lennon).

My website is done in Cobol; http://www.infodynamicsconsult.com/Forum_main.asp

Though it is local, I like the way it was built and patterned around
vBulletin format.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Anonymous <cripto@ecn.org>
- **Date:** 2010-07-21T14:35:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20100721123558.3A6531A7B76@www.ecn.org>`
- **References:** `<8ani7uFr1vU1@mid.individual.net>`

```
> I tried Lisp on one project many years ago and found it excellent for
> data management and search, but I don't think I'd want to write a game in
> it. 

LISP has come a long long way and now is equal to almost any HLL in
function, with tons of built-ins and many libraries available. It's just so
hard to get adjusted to for many people it hasn't caught on. It's very
good, but just not what many people are used to. For games it's probably a
top choice with excellent built-in number crunching capabilities (large
integer support, etc.) and many graphics library interfaces.

For those inclined to use it, it's a fine language with much support. If
all you're used to is algorithmic (algebraic) languages you'll be in for a
shock though.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-22T13:02:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8apjknFtbcU1@mid.individual.net>`
- **References:** `<8ani7uFr1vU1@mid.individual.net> <20100721123558.3A6531A7B76@www.ecn.org>`

```
Anonymous wrote:
>> I tried Lisp on one project many years ago and found it excellent for
>> data management and search, but I don't think I'd want to write a
…[12 more quoted lines elided]…
> in for a shock though.

That is very fair comment.

As I said, I only tried it once and that was around 20 years ago.

Both LISP and I have come a long way since then :-)

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-21T08:27:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4s0e46pbvb06901eim4tj8b5tap2d1t1k1@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net> <qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com> <8ani7uFr1vU1@mid.individual.net>`

```
On Wed, 21 Jul 2010 18:26:04 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Why not install Open COBOL?
>
>While it doesn't support OO, you probably won't need OO for games (unless 
>you are thinking about avanced adventure gaming, where there could be some 
>advantages in using OO).

I found a download for a .tar file, which I could open into a folder
on my Mac.    But turning it into something I know how to use on a Mac
will take a bunch of learning.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-22T13:07:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8apju7FumiU1@mid.individual.net>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net> <qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com> <8ani7uFr1vU1@mid.individual.net> <4s0e46pbvb06901eim4tj8b5tap2d1t1k1@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 21 Jul 2010 18:26:04 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> will take a bunch of learning.

You said you are committed to Mac, and you were looking for a hobby, 
Howard... :-)

I have complete confidence you will achieve whatever you set out to do.

If you write the engine in COBOL there are any number of interface options 
for the GUI.

Another possibility might be to use Haskell. It looks like a "likely" 
language, and it is free and runs on Mac.

It really comes down to hiow much time you have and how much aggravation 
(learning...) you are prepared toundertake. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-22T11:51:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q71h46p0qd86rek7raj3dk2hkp35stagg6@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <8ak3t5FrftU1@mid.individual.net> <qudb46tt8e3cmdroq433rd8o7jiaot9sqd@4ax.com> <8ani7uFr1vU1@mid.individual.net> <4s0e46pbvb06901eim4tj8b5tap2d1t1k1@4ax.com> <8apju7FumiU1@mid.individual.net>`

```
On Thu, 22 Jul 2010 13:07:18 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>You said you are committed to Mac, and you were looking for a hobby, 
>Howard... :-)
…[10 more quoted lines elided]…
>(learning...) you are prepared toundertake. :-)

Right now, I am likely narrowed to Haskell or CoBOL - whichever gives
me least aggravation in what I'm not interested in (getting it
working), and to what I am interested in (programming).
```

#### ↳ Re: Hobby languages

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-19T22:02:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
On Jul 20, 3:44 am, Howard Brazee <how...@brazee.net> wrote:
> I was thinking about my retirement, and I have written CoBOL programs
> that figured out puzzles and fun stuff.   My choice of languages is
…[6 more quoted lines elided]…
> What languages would you recommend for such a person?

OpenCOBOL is free and is alleged to run on a Mac.

http://www.opencobol.org/

I would suggest that you could run it under a web server to give a
user interface on the browser. SVG graphics is supported by Safari.

If you want a different language then I use Python for most everything
and it runs on almost every machine from phones to supercomputers.
```

##### ↳ ↳ Re: Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-20T09:47:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com>`

```
On Mon, 19 Jul 2010 22:02:00 -0700 (PDT), Richard
<riplin@Azonic.co.nz> wrote:

>OpenCOBOL is free and is alleged to run on a Mac.
>
…[3 more quoted lines elided]…
>user interface on the browser. SVG graphics is supported by Safari.

That may be the easiest.

>If you want a different language then I use Python for most everything
>and it runs on almost every machine from phones to supercomputers.

What are the advantages of Python for my personal use on one computer?

Hmmm.    Eventually I will be downsizing and getting rid of my
library.   That will be hard, but at that time I will evaluate e-book
readers, and may choose something that has some computing power.
Technology changes rapidly, so it would be a guess what I'd get - but
that might be a good reason for selecting a language that is on a lot
of platforms.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-22T03:55:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137ab402-246e-4b25-a1eb-ac660f7bfe65@k39g2000yqb.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com> <54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com>`

```
On Jul 20, 4:47 pm, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 19 Jul 2010 22:02:00 -0700 (PDT), Richard
>
…[27 more quoted lines elided]…
> - James Madison

If you were ever to ditch the Mac and buy in to Windows, there is F#
available from Microsoft for free at:
    http://msdn.microsoft.com/en-gb/fsharp/default.aspx
F# is a functional language and borrows much from C#. It is not
available for platforms other than Windows.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-22T12:55:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e2fec081-ab13-443c-9335-b1f6328beda5@m35g2000prn.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com> <54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com>`

```
On Jul 21, 3:47 am, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 19 Jul 2010 22:02:00 -0700 (PDT), Richard
>
…[13 more quoted lines elided]…
> What are the advantages of Python for my personal use on one computer?

Python can be used as an interactive language - just type a line in
and see what it does, or the programs can be built as structured
modules to create large systems, or anything in-between.

The usual implementation takes the source code and uses a JIT compiler
so you never worry about having to compile and build the programs. It
has an extensive library and built in lists, dictionaries and tuples.
It is a compact language that generally has just one way of doing
something - for example it has if .. elif .. elif .. else, but no case
statement. It has classes and closures, threading.

The only unusual thing is that it uses indentation to define the
structure. This means that it is imperative that the source code does
not mix tabs and spaces. Once the editor is configured to, say, never
use tabs, then you are assured that what you are looking at is
actually the logic structure. You won't be fooled by a missing 'end'
or block closure, or by a stray full stop.

Any module can have its own built in testing code which will be
ignored when used as called module from another program. This gives
much faster development speed as the module can be edited and run
alternately without anything else between.

Python is widely used. A recent survey showed that some 30% of
developers use Python as one of their languages of choice. There is
extensive documentation, examples, and support available.


> Hmmm.    Eventually I will be downsizing and getting rid of my
> library.   That will be hard, but at that time I will evaluate e-book
…[10 more quoted lines elided]…
> - James Madison
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-22T14:16:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5850182-022d-431c-ba34-dd6cccaf2155@p11g2000prf.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com> <54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com>`

```
On Jul 21, 3:47 am, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 19 Jul 2010 22:02:00 -0700 (PDT), Richard
>
…[13 more quoted lines elided]…
> What are the advantages of Python for my personal use on one computer?

One more reason, I just looked up Python + OSX and:

http://www.python.org/download/mac/

"""Python on the Mac

Python on the Mac has the ability to work with

    * Apple Events (you can use Python instead of Applescript),
    * Native Mac libraries (you can call all the Objective-C
libraries, including Cocoa),
    * Mac application bundles ("apps", written in Python),

and much much more of the Mac infrastructure!

Python comes pre-installed on Mac OS X,  ... """

You already have it.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-23T10:23:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0bgj465l37mm2trvr58kvucvlk4cd7jkpd@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com> <54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com> <f5850182-022d-431c-ba34-dd6cccaf2155@p11g2000prf.googlegroups.com>`

```
On Thu, 22 Jul 2010 14:16:19 -0700 (PDT), Richard
<riplin@Azonic.co.nz> wrote:

>Python on the Mac has the ability to work with
>
…[5 more quoted lines elided]…
>and much much more of the Mac infrastructure!

That's attractive.   I wonder if I can access the English language
dictionary that OS-X uses.

I suppose it depends on what interests me - Haskell looks like a more
fun language to learn.   Python looks like something that can get me
quicker to useful results.   CoBOL looks like the hardest thing to set
up and know about my environment.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-23T12:45:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13faa4e1-36df-41e9-be3f-2514f223401d@n19g2000prf.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <735526eb-aaf0-4beb-869e-84c4e9fb3ba4@z15g2000prn.googlegroups.com> <54hb46l64iujgevqp7ns0m8tut29qa4ur6@4ax.com> <f5850182-022d-431c-ba34-dd6cccaf2155@p11g2000prf.googlegroups.com> <0bgj465l37mm2trvr58kvucvlk4cd7jkpd@4ax.com>`

```
On Jul 24, 4:23 am, Howard Brazee <how...@brazee.net> wrote:
> On Thu, 22 Jul 2010 14:16:19 -0700 (PDT), Richard
>
…[11 more quoted lines elided]…
> dictionary that OS-X uses.

It seems that there is an AppleScript bridge which should allow
access.

http://appscript.sourceforge.net/py-appscript/index.html

When I mentioned 'dictionaries' this was the Python data structure
accessible by key value (rather than an array accessed by index
number). Other languages may call this a 'hash' or some other. In
COBOL one might use an indexed file for this.

    departments = {}                  # an empty dictionary
    fd = open('departments.txt', 'r') # file of CODE,NAME
    for line in fd:
        (code,name) = line.strip().split(',')
        departments[code] = name
    print departments

{'SAL': 'Sales', 'TTT': 'Transport', 'AAB': 'Absolute Masters'}
```

#### ↳ Re: Hobby languages

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-07-20T13:45:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m2ob46phdvffcusa04gns9g1n81grfmihk@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
On Mon, 19 Jul 2010 09:44:14 -0600, Howard Brazee <howard@brazee.net>
wrote:

>
>I was thinking about my retirement, and I have written CoBOL programs
…[7 more quoted lines elided]…
>What languages would you recommend for such a person?

Back in the 80's I used to write a lot of Commodore Basic and
Commodore Assembler programs for fun and for myself.  Had fun, taught
me a lot about PC programming and ASCII and all of that.  Maybe you'd
want to take a leap and learn something you can run an an Apple or
learn whatever it is they write those phone apps in.

Regards,
```

#### ↳ Re: Hobby languages

- **From:** George Orwell <nobody@mixmaster.it>
- **Date:** 2010-07-21T02:19:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c80918536e67e06ce43c27e5374a3dc@mixmaster.it>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
> Let's say I want to write a Sudoko puzzler, a Rubic's Cube solver, or
> a word puzzle solver.   My home computer is a Mac and I expect this
> won't change when I retire.
> 
> What languages would you recommend for such a person?

Hello Howard,

I think the best language ever to hit the PC is Ada. I think a guy like you
(from what I have seen of your postings anyway) would love it. It's like
PL/I on steroids. If not for the fact it's only available (well modern
versions anyway) under the GPL, it would be perfect. Actually the supplied
libraries are LGPL (sortof kindof asfarasweknow) but most 3rd party libs
are pure shitty GPL. If that doesn't bother you then there is no better
language on the PC than Ada, and if it weren't for assembler there would be
no better mainframe language either.

Il mittente di questo messaggio|The sender address of this
non corrisponde ad un utente   |message is not related to a real
reale ma all'indirizzo fittizio|person but to a fake address of an
di un sistema anonimizzatore   |anonymous system
Per maggiori informazioni      |For more info
                  https://www.mixmaster.it
```

##### ↳ ↳ Re: Hobby languages

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-20T18:33:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e09f1076-c1f6-4dd8-8493-508cb808c3f7@m17g2000prl.googlegroups.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <3c80918536e67e06ce43c27e5374a3dc@mixmaster.it>`

```
On Jul 21, 12:19 pm, George Orwell <nob...@mixmaster.it> wrote:
> > Let's say I want to write a Sudoko puzzler, a Rubic's Cube solver, or
> > a word puzzle solver.   My home computer is a Mac and I expect this
…[13 more quoted lines elided]…
> no better mainframe language either.

Your pseudonym is so appropriate because this message is just right
for '1984'.

 .. apart from the bits about the GPL which is uninformed.

"""The FSF compiler is freely available and doesn't have the license
restrictions of the GNAT GPL."""

"""GNAT Modified GPL releases

With these releases of GNAT, you can distribute your programs in
binary form under licensing terms of your own choosing; you are not
bound by the GPL."""

"""GCC version 4.4 switched to version 3 of the GNU General Public
License and grants a Runtime Library Exception similar in spirit to
the GNAT Modified General Public License used in all previous
versions. This Runtime Library Exception applies to run-time libraries
for all languages, not just Ada."""

If you don't like the idea of GPL, or similar, then purchase
commercial versions of GNAT and the 3rd party libraries. You seem to
want stuff for free that you can build on and sell.
```

##### ↳ ↳ Re: Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-21T08:32:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d11e4611k1bganu87069ee9csom3fk76g6@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <3c80918536e67e06ce43c27e5374a3dc@mixmaster.it>`

```
On Wed, 21 Jul 2010 02:19:59 +0200 (CEST), George Orwell
<nobody@mixmaster.it> wrote:

>
>I think the best language ever to hit the PC is Ada. I think a guy like you
…[6 more quoted lines elided]…
>no better mainframe language either.

PL/I on steroids - attractive.   Both PL/I & Ada were designed to do
everything.   Glancing at Google (on my Windows machine at work), I
get the impression that I'll have to learn how to build the
programming environment similar to what it appears I will have to
learn to build a CoBOL programming environment.   But first
impressions can be misleading.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** "Bruce M. Axtens" <bruce.axtens@gmail.com>
- **Date:** 2010-07-22T17:45:20+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iISdnRmx6-C_jtXRnZ2dnUVZ8kSdnZ2d@westnet.com.au>`
- **In-Reply-To:** `<d11e4611k1bganu87069ee9csom3fk76g6@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <3c80918536e67e06ce43c27e5374a3dc@mixmaster.it> <d11e4611k1bganu87069ee9csom3fk76g6@4ax.com>`

```
On 21/07/2010 10:32 PM, Howard Brazee wrote:
> On Wed, 21 Jul 2010 02:19:59 +0200 (CEST), George Orwell
Speaking of Mac languages, how about Objective Modula-2? 
<http://objective.modula2.net/>

"Objective Modula-2 is a reflective, object oriented programming 
language with dynamic message dispatch (late binding) and both static 
and dynamic typing. Its object system is based on the object model of 
Smalltalk and it uses the runtime library of Objective-C to support the 
Cocoa and GNUstep APIs natively.

"The design is an example how native support for Cocoa (Mac OS X), Cocoa 
Touch (iPhone) and GNUstep (BSD/Linux) can be added to static imperative 
programming languages without implementing an Objective-C bridge."
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** George Orwell <nobody@mixmaster.it>
- **Date:** 2010-07-22T16:30:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<685992e73223defefd30da65b73627f1@mixmaster.it>`
- **References:** `<iISdnRmx6-C_jtXRnZ2dnUVZ8kSdnZ2d@westnet.com.au>`

```
The problem with alot of these languages is they are still niche languages
and using them for real world projects puts you at risk of support issues
and performance issues and other types of problems where you just hit the
wall and "that's the way it is". I know the thread is "Hobby Languages" but
Ocaml, Haskell and tons of other languages are just too weird and not
flexible enough considering all the other mainstream choices like Ada, LISP
variations etc. Most weird languages have a specific agenda (functional
programming, object-oriented programming) that makes them not suitable as
general purpose languages given they more or less force you into their way
of approaching problems. And they seem to revel in bizarre syntax that only
experts can read instead of clarity, with no clear advantage in any other
area. I dislike languages that aren't obvious. Expert languages are great
for experts but code needs to be readable without having funny side-effects
only experts can spot.

For me a hobby language has to be flexible and powerful, I really don't
make a distinction in what I would use for hobby programming vs.
professional programming. The language has to be clean and not get in
my way, and it has to compile to native code (not byte code and not wierd
intermediate code- native code! I mean it!) I don't like having to use
brackets all over the place or overloaded operators. Typing is just not
that expensive compared to a clean looking, pleasing languages.

I don't think every problem in the world is best solved with OO. I don't
even think OO is right for most problems. Nor do I think structured
programming is a good general technique. When I look at a language I choose
one that offers options in how to approach problems so I can solve the
problem how it makes sense to me to solve it instead of having the language
be a mold around every problem.

That is why I am in favor of Ada....it is a "traditional" procedural
language that is readable almost immediately but also offers *additional*
ways of looking at problems and implementing their solutions (object
orientation) without limiting you to a "one world view" of problems. It is
hard to argue procedural languages are inappropriate for the vast majority
of programming problems. That doesn't mean there aren't more natural or
better ways, but a simple old fashioned procedural (functional
decomposition) approach will get the job done 99 times out of a
hundred. When you get into really large systems with big line counts Ada
shines over most other systems simply because dealing with very large
systems was a fundamental aspect that was agreed must be dealt with in the
design of Ada from the very beginning. It's true that if you are a makefile
wizard you can achieve much of the same (but not all) result as you can
with Ada's approach, but I would rather have one stop shopping. Let the
language (the language system) deal with all that rather than me having to
learn peculiarities of gcc, etc. 

Since we are in comp.lang.cobol, Ada is a good choice because even though
in many ways it's very different than COBOL, COBOL programmers will find it
a lot more familiar and easy to live with than most other languages. Ada is
also a mainframe language and has some of the same thinking and approaches
behind it, unlike most of the PC languages. It offers every bit of the
power and flexibility of C and C++ but with a more intelligible
presentation, prettier and less confusing, and much safer. If you can get
past the compiler you have a better than average chance your code will work
as desired, instead of just work.

LISP for all it's apparent wierdness still is quite flexible in allowing
you to choose how to implement your solution and doesn't impose a
particular view of how all problems must be represented. It used to
(everything is a list) but those days are long gone.

Il mittente di questo messaggio|The sender address of this
non corrisponde ad un utente   |message is not related to a real
reale ma all'indirizzo fittizio|person but to a fake address of an
di un sistema anonimizzatore   |anonymous system
Per maggiori informazioni      |For more info
                  https://www.mixmaster.it
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-22T11:55:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hc1h46ti54i380ptfk0jn6tp2c9qls8vs4@4ax.com>`
- **References:** `<iISdnRmx6-C_jtXRnZ2dnUVZ8kSdnZ2d@westnet.com.au> <685992e73223defefd30da65b73627f1@mixmaster.it>`

```
On Thu, 22 Jul 2010 16:30:02 +0200 (CEST), George Orwell
<nobody@mixmaster.it> wrote:

>For me a hobby language has to be flexible and powerful, I really don't
>make a distinction in what I would use for hobby programming vs.
…[4 more quoted lines elided]…
>that expensive compared to a clean looking, pleasing languages.

I figure most of my programs I will use for my hobby language will be
run once to solve a problem.   I won't need it to be efficient, byte
code or Java like environments won't slow me down.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-22T12:27:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5d0a9d19-d7d2-4fe7-84c7-1e872dfbde3d@w35g2000prd.googlegroups.com>`
- **References:** `<iISdnRmx6-C_jtXRnZ2dnUVZ8kSdnZ2d@westnet.com.au> <685992e73223defefd30da65b73627f1@mixmaster.it>`

```
On Jul 23, 2:30 am, George Orwell <nob...@mixmaster.it> wrote:
> The problem with alot of these languages is they are still niche languages
> and using them for real world projects puts you at risk of support issues
> and performance issues and other types of problems where you just hit the
> wall and "that's the way it is".

While there may well be chargeable support for commercial Ada there
does not seem to be a great deal of community support for Ada.

> I know the thread is "Hobby Languages" but
> Ocaml, Haskell and tons of other languages are just too weird and not
…[4 more quoted lines elided]…
> of approaching problems.

Ada was specified and designed as a Real Time and Embedded Systems
language, such as aircraft and aerospace control systems. It has
features that are designed to ensure reliability and recovery from
errors and exceptions. It seems to fit your concept of 'weird
languages'.

> And they seem to revel in bizarre syntax that only
> experts can read instead of clarity, with no clear advantage in any other
> area. I dislike languages that aren't obvious. Expert languages are great
> for experts but code needs to be readable without having funny side-effects
> only experts can spot.

What is readable and 'obvious' is entirely what you are used to.

> For me a hobby language has to be flexible and powerful, I really don't
> make a distinction in what I would use for hobby programming vs.
> professional programming. The language has to be clean and not get in
> my way, and it has to compile to native code (not byte code and not wierd
> intermediate code- native code! I mean it!)

Ada was designed when the 8080 and 6502 had just come out and ran at 1
or 2 KiloHz. Your arguments are entirely suitable for 1984.

> I don't like having to use
> brackets all over the place or overloaded operators. Typing is just not
> that expensive compared to a clean looking, pleasing languages.

What is clean looking and pleasing is entirely what you are used to.

> I don't think every problem in the world is best solved with OO. I don't
> even think OO is right for most problems. Nor do I think structured
…[16 more quoted lines elided]…
> design of Ada from the very beginning.

I doubt that a hobbyist will be be building a really large system.

> It's true that if you are a makefile
> wizard you can achieve much of the same (but not all) result as you can
> with Ada's approach, but I would rather have one stop shopping. Let the
> language (the language system) deal with all that rather than me having to
> learn peculiarities of gcc, etc.

There are many languages which do not require the use of makefiles or
anything similar.

> Since we are in comp.lang.cobol, Ada is a good choice because even though
> in many ways it's very different than COBOL, COBOL programmers will find it
> a lot more familiar and easy to live with than most other languages.

It certainly had a similar history (DoD) and, coming primarily from
the 70s and 80s originates at the same technical level as '74 and '85
COBOL. Granted there was an Ada'95 and 2002 so iut has moved on from
there.

> Ada is
> also a mainframe language and has some of the same thinking and approaches
…[4 more quoted lines elided]…
> as desired, instead of just work.

What is prettier and less confusing is entirely what you are used to.

> LISP for all it's apparent wierdness still is quite flexible in allowing
> you to choose how to implement your solution and doesn't impose a
> particular view of how all problems must be represented. It used to
> (everything is a list) but those days are long gone.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-07-22T15:28:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c484796$0$284$14726298@news.sunsite.dk>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com> <3c80918536e67e06ce43c27e5374a3dc@mixmaster.it> <d11e4611k1bganu87069ee9csom3fk76g6@4ax.com>`

```
Howard Brazee wrote:

> On Wed, 21 Jul 2010 02:19:59 +0200 (CEST), George Orwell
> <nobody@mixmaster.it> wrote:
…[17 more quoted lines elided]…
> impressions can be misleading.

Where (while searching for gcc ada) the first page on Google brought me:
http://eng-osx.sourceforge.net/GNAT.html

which points to sone of the properly maintained package from other
sites. No need to learn how to build the programming environment. :-)
```

#### ↳ Re: Hobby languages

- **From:** Jessica Colman <jessica.colman@augustakom.net>
- **Date:** 2010-07-23T09:27:54+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i2bg9o$2hl$1@news.m-online.net>`
- **In-Reply-To:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`
- **References:** `<acs8465gmq72c39qrf15qlqak8e1qul90t@4ax.com>`

```
Interesting: None of you mentioned Java.

I've been programming PL/I and sometimes COBOL and Assembler for 18 
years. These are great languages for z/OS applications. But if I have to 
write something to run on Windows/Unix I would never even consider them.

For Windows/Unix systems I switched to Java about 13 years ago. The IDE 
support is great and for almost every reoccurring problem there is a 
library. You can integrate theses libraries very easy and most of them 
are free (e.g. apache-commons-lang, -logging, -configuration etc)

As IDE I use Rational Team Concert (RTC). RTC uses a repository which I 
run on on DB/2 express and a build server which I run on Linux. 
Unfortunately RTC does not run on Mac, but you can use Eclipse with 
subversion as repository and ANT for builds alternatively.

So, my recommendation is: Java with Eclipse and ANT.

Jessica

Howard Brazee schrieb:
> I was thinking about my retirement, and I have written CoBOL programs
> that figured out puzzles and fun stuff.   My choice of languages is
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Hobby languages

- **From:** Fritz Wuehler <fritz@spamexpire-201007.rodent.frell.theremailer.net>
- **Date:** 2010-07-23T18:21:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net>`

```
> Interesting: None of you mentioned Java.

That was intentional because we're mostly mainframe guys with sense ;)

My opinion is Java is a solution looking for a problem and that it has
contributed to the dumbing-down of coding without contributing anything
else. It's sloppy, unsafe, and bloated both in source and runtime. I don't
know of any reason to use Java anywhere when real programming languages are
available instead.

> I've been programming PL/I and sometimes COBOL and Assembler for 18 
> years. These are great languages for z/OS applications. But if I have to 
> write something to run on Windows/Unix I would never even consider them.

Fair enough. Most people don't have access to PL/I or COBOL on the PC and
PC assembly is an abomination. For those reasons and others as well, I
don't code on the PC except a little in Ada. Anything else is well, just
too offensive! Some of us want to make our PC's as much like mainframes as
we can, Ada is the cheapest way to do that. COBOL is fine for what it is
for but I agree it's too limited for general purpose programming unless you
enjoy stabbing yourself in the eyes with a pen.

> As IDE I use Rational Team Concert (RTC). RTC uses a repository which I 
> run on on DB/2 express and a build server which I run on Linux. 
> Unfortunately RTC does not run on Mac, but you can use Eclipse with 
> subversion as repository and ANT for builds alternatively.

Do you not have to pay big euros for Rational anything?

> So, my recommendation is: Java with Eclipse and ANT.

But that takes a PC with alot of power. Most commodity PC's die under the
bloat of Java and Eclipse.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-23T11:58:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net>`

```
On Fri, 23 Jul 2010 18:21:02 +0200, Fritz Wuehler
<fritz@spamexpire-201007.rodent.frell.theremailer.net> wrote:

>> Interesting: None of you mentioned Java.
>
…[6 more quoted lines elided]…
>available instead.

Java's big strength is that it can run everywhere.   Other strengths
include garbage management, and finding people who can work with it is
tops. 

Since I'm writing only for myself, doing simple projects these aren't
useful strengths.   The only advantage of OO is if I find objects
already written which, say, read the English language dictionary.
(although I would be happy with functions or library code that can do
that).    Resource use doesn't bother me for my needs.

Ummm, I guess its ubiquity also means I could find more Internet help
with Java.

I have no idea what criteria you use for "Real Programming Languages".
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** "Non scrivetemi" <nonscrivetemi@pboxmix.winstonsmith.info>
- **Date:** 2010-07-25T00:12:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126943e4ae1859c7b576fa56a3ef918c@pboxmix.winstonsmith.info>`
- **References:** `<kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com>`

```
> Java's big strength is that it can run everywhere.   Other strengths
> include garbage management, and finding people who can work with it is
> tops. 

Garbage collection is not a strength, it exposes a fundamental weakness in
the design of Java and other languages requiring garbage collection. It's
interesting to see how people have been sold on the benefits of something
that should never have been necessary in the first place.

Java may run everywhere but it's not (nearly) as portable as Ada. Bjarne
Stroustrup made a point of playing up this deficiency in Java, noting that
often Java applications need to be changed to run on a new platform. Since
you noted you only want something for Mac, it is not obvious why you think
"running everywhere" is a strength. If you really want something that runs
everywhere (as opposed to something that installs on many platforms and
doesn't necessarily run) then both C and C++ are much better choices.

> Ummm, I guess its ubiquity also means I could find more Internet help
> with Java.

Ubiquity only means you can find more internet noise with Java.

> I have no idea what criteria you use for "Real Programming Languages".

I enumerated a few of them earlier.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-07-24T21:23:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u6O2o.150$mW5.22@newsfe14.iad>`
- **In-Reply-To:** `<126943e4ae1859c7b576fa56a3ef918c@pboxmix.winstonsmith.info>`
- **References:** `<kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com> <126943e4ae1859c7b576fa56a3ef918c@pboxmix.winstonsmith.info>`

```
Non scrivetemi wrote:
> 
> 
…[3 more quoted lines elided]…
> that should never have been necessary in the first place.

Agreed Garbage Collection is not a strength, (or perhaps more precisely 
AUTO Garbage Collection), - is just a pure pain in the arse ! I come at 
this as a former Systems Analyst ('63-79) turned to programming to earn 
a living.

As a former analyst (and the job was about DESIGNING - not bits and 
bytes), I fail to see how any language can dovetail neatly to do 
automatic garbage collection for you, and always get it right. (How can 
an independent 'third party', the OO runtime, anticipate 100% accurately 
WHEN I the designer want something destroyed ?). I don't know Ada etc., 
but are there constraints put upon you in class/method design so that it 
recognises when to destroy certain objects ?

The COBOL Standards (J4/PL22.4) had a 'Finalizer" project which they 
cajoled the Japanese representatives (Hitachi) into doing the donkey 
work. To circumvent the bullshit of getting additional stuff into the 
COBOL Standard it was defined as a TR (Technical Report). The theory - 
once OK'd it becomes an addendum to the current Standard without going 
through the ANSI bureaucratic machinery. That TR paper is in the freezer
on ice.

COBOL OO compilers - IBM don't need it - they inherit from JavaBase 
which gets rid of objects created. Alchemy/Fujitsu - don't see them any 
time soon implementing it - their route of choice - .Net. Veryant (from 
Italy) like IBM uses Java - so they don't need it either. Hitachi - 
seeing as they studied it, they 'might' just implement, which doesn't do 
you or me any good as you can only get their compiler in Asia with the 
Japanese character set. Which leaves us with Micro Focus and Net 
Express. I'll put my money on the gamble they will never implement it.

N/E has four 'finalizer' methods, and this how I use them; each class 
instance created has a method "FinalizeObjects"  :-

1a) Single object in this class : and you don't need to 'finalize' 
objects within methods - the Standard states that 'Each time a method is 
invoked, it is in its initial state', i.e. any Working-Storage or 
Local-Storage references to objects are 'junk' until they are used, and 
the are 'junk' once again when you leave the method.

if	ThisObject <> null
	invoke ThisObject "finalize" returning ThisObject
end-if

1b) An instance of another class created in this class: the line
	invoke ..."FinalizeObjects" goes to that method in the Class 2
	specified, which can be a 'dummy' or empty; alternatively where
	objects have been created in Class 2 then it repeats this
	general sequence

if	ThisObject <> null
	invoke ThisObject "FinalizeObjects"
	invoke ThisObject "finalize" returning ThisObject
end-if

2) One-level List/Collection/Dictionary

if	ThisCollection <> null
	invoke ThisCollection "DeepFinalize" returning ThisCollection
end-if

3) Multi Level List/Collection/Dictionary

if	ThisCollection <> null
	move 3 to ls-depth
	invoke ThisCollection "DeepFinalizeWithDepth" using ls-depth
			returning ThisCollection
end-if

4) Believe it or not :-

if	ThisObject <> null
	invoke ThisObject "ReallyDeepFinalize" returning ThisObject
end-if

Sure it's wordy, but it is also very PRECISE. (The objects shown are 
held in Global Working-Storage for the Instance in ALPHABETICAL order - 
and I have them as comment entries in the 'FinalizeObjects' method, so 
that I don't miss them).

(1b) above is a little more than it appears - that class may contain 
objects created internally within the class and possibly objects passed 
to it. A classic example would be a Parent Window for an application, 
created from the Desktop. I pass its object reference quite frequently 
because it is required for messageboxes whether informative or 
error-reporting. I do NOT want a subordinate class finalizing the 
ParentWindow and screwing up the whole application - so I code 
accordingly within the "FinalizeObjects" method.

(To be honest - I might not need to pass ParentWindow - only the other 
day I spotted some M/F code where they had :-

01 oo-Desktop		object reference external.

So maybe I should be reviewing my approach if the 'external' syntax does 
it for me.)

Like the biblical 'Doubting Thomas', I need to see proof before I buy 
into auto garbage collection.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** Louis Krupp <lkrupp_nospam@indra.com.invalid>
- **Date:** 2010-07-24T23:03:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wd2dnYOqab0NWNbRnZ2dnUVZ_vadnZ2d@indra.net>`
- **In-Reply-To:** `<u6O2o.150$mW5.22@newsfe14.iad>`
- **References:** `<kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com> <126943e4ae1859c7b576fa56a3ef918c@pboxmix.winstonsmith.info> <u6O2o.150$mW5.22@newsfe14.iad>`

```
On 7/24/2010 9:23 PM, James Gavan wrote:
> Non scrivetemi wrote:
>>
…[18 more quoted lines elided]…
> recognises when to destroy certain objects ?

I've used Perl, which does automatic garbage collection.  Things seem to 
Just Work, so I assume garbage collection is operating as intended.

Postscript does automatic garbage collection, and I've worked on a 
Postscript implementation, so I know more about that.  Yes, Postscript 
garbage collection is complicated and no, it's not as surgically precise 
as one might hope, keeping stale stuff that happens to be sitting next 
to new stuff, but it works Well Enough.

I would not expect a Perl programmer to worry about memory management. 
I don't when I'm writing Perl.  I'm willing to trade efficiency for 
convenience.  The same is true, only more so, for Postscript.  Most 
Postscript is generated by drivers, not by programmers, and memory 
management is a complication you don't need.  And a Postscript 
interpreter in a printer doesn't have to be blindingly fast;  it just 
has to stay ahead of the print engine.

I've also used C and C++.  I've fixed lots of memory leaks.  I've 
created my share.  I've worked with programmers who had no clue that 
they could run out of virtual memory, that object creation could fail, 
that 'new' could return NULL.

You could argue that C is intended for tight, fast, possibly embedded 
code, that automatic garbage collection has no place in that 
environment, and you would probably be persuasive.  One could argue that 
C++ is less suitable where speed is critical, and that adding an 
automatic garbage collection feature wouldn't be the worst thing in the 
world.  I wouldn't be too surprised to see this happen.  It would widen 
the gap between C and C++, which is perhaps inevitable.

It's not clear how much any of this would matter to someone choosing a 
hobby language.  Perl, Python (about which I know very little), Ruby, 
Lua ... they all do automatic garbage collection, as far as I know, and 
each of them can be entertaining in its own way.

Louis
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** "Non scrivetemi" <nonscrivetemi@pboxmix.winstonsmith.info>
- **Date:** 2010-07-25T16:16:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dde1ce5be38958e64838d326454bc4b3@pboxmix.winstonsmith.info>`
- **References:** `<u6O2o.150$mW5.22@newsfe14.iad>`

```
James Gavan <jgavan@shaw.ca> wrote:

> bytes), I fail to see how any language can dovetail neatly to do 
> automatic garbage collection for you, and always get it right. (How can 
…[3 more quoted lines elided]…
> recognises when to destroy certain objects ?

I'm not the right person to answer your question on Ada but I know it does
allow you to control finalization either directly or indirectly. For a good
answer please ask on comp.lang.ada, several Ada designers and compiler
writers are there and can answer all your questions.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:08:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r02r465ju1gnoa5jjhgbhi36o91cehpc3c@4ax.com>`
- **References:** `<kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com> <126943e4ae1859c7b576fa56a3ef918c@pboxmix.winstonsmith.info>`

```
On Sun, 25 Jul 2010 00:12:34 +0200 (CEST), "Non scrivetemi"
<nonscrivetemi@pboxmix.winstonsmith.info> wrote:

>> Java's big strength is that it can run everywhere.   Other strengths
>> include garbage management, and finding people who can work with it is
…[5 more quoted lines elided]…
>that should never have been necessary in the first place.

Most any characteristic can be both a strength and a weakness.

>Java may run everywhere but it's not (nearly) as portable as Ada. Bjarne
>Stroustrup made a point of playing up this deficiency in Java, noting that
…[4 more quoted lines elided]…
>doesn't necessarily run) then both C and C++ are much better choices.

"Running everywhere" is a strength that isn't useful to me.   But it's
useful to web developers.   I wasn't listing strengths for my needs, I
was listing strengths in general.

>> Ummm, I guess its ubiquity also means I could find more Internet help
>> with Java.
>
>Ubiquity only means you can find more internet noise with Java.

It also means employers can find programmers more easily.

>> I have no idea what criteria you use for "Real Programming Languages".
>
>I enumerated a few of them earlier.

In my opinion, they all are Real Programming Languages.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-26T03:55:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2b0adf27-4714-4800-9b2e-6c9f2b4a9264@q22g2000yqm.googlegroups.com>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net> <kmlj46d7n1j4e9j8rm5qae1bth6n2vs219@4ax.com>`

```
On Jul 23, 6:58 pm, Howard Brazee <how...@brazee.net> wrote:
> On Fri, 23 Jul 2010 18:21:02 +0200, Fritz Wuehler
>
…[19 more quoted lines elided]…
> that).    Resource use doesn't bother me for my needs.

Afriend of mine taught himself Java and wrote a nifty covering letter
generator. Some months later he went to add in some new functionality
and found to his horror that he didn't understand any of the code he
had previously written. Be warned.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-24T13:25:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8autnoFsbcU1@mid.individual.net>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net>`

```
Fritz Wuehler wrote:
>> Interesting: None of you mentioned Java.
>
> That was intentional because we're mostly mainframe guys with sense ;)


That makes you wrong on two counts, Fritz :-)

"Mainframe guys" have no monopoly on sense, and Java is an excellent 
language.
>
> My opinion is Java is a solution looking for a problem and that it has
> contributed to the dumbing-down of coding without contributing
> anything else. It's sloppy, unsafe, and bloated both in source and
> runtime.

I disagree with your opinion. :-)

Java was one of the first generally used OO languages and it serves that 
purpose admirably. In fact, I would (and have) recommend(ed) people who wish 
to move out of COBOL to learn Java. It is an excellent way to pick up the 
concepts of Object Orientation, as it was designed around those concepts. If 
by "dumbing down" you mean simpler, less intricate code, then how is that a 
bad thing? Java is far more "powerful" (in the sense that less of it does 
more...) than COBOL. If you are an old time BAL programmer (as I was in 
another lifetime) it is easy to equate detail with "cleverness" and decide 
that anything which removes the detail is dumb. Let's take a look at your 
criticism:

"sloppy" :    Languages are not sloppy; programmers are sloppy.
"unsafe" :     Competent programmers and compilers/interpreters make code in 
any language safe.
"bloated":    There's a description of code I haven't heard for a while 
(apart from references to the Windows OS...). You may not have noticed but a 
pentium 5 (obsolete) PC has more processing power than an old mainframe (say 
370-145) and has more memory also. So why increase resources and power on a 
computer system unless you intend to use them? There are benefits in using 
Java or any other high level language over most Assembler level languages, 
but compactness of code and run time are not one of those particular 
benefits. That doesn't mean it is bloated, it just means the resources 
provided are being used to obtain benefits that weren't previously available 
or to obtain benefits that are considered to be more important than size of 
runtime.



> I don't know of any reason to use Java anywhere when real
> programming languages are available instead.
>

And by "real programming languages" you mean...?  ADA, COBOL, Assembler?

All of them are useful in some areas and depending on the criteria you have 
established.

If you are unconcerned with resources but are very concerned about readable 
code, you will probably prefer COBOL, for example.

However, if you have an application which is best served by an Object 
Oriented approach (maybe networked) then Java is an excellent choice. 
(Although my personal preference is C#)

It is just silly in this day and age, with the computing resources now 
available, to rant about modern languages "dumbing down" the art of 
programming and requiring bloated resources. There was a time (when we 
managed overlays manually in very limited memory) when these things were 
important. Nowadays, except for some highly specialised command and control 
and real time processing systems (which are not a general part of commercial 
application development), they are not.


>> I've been programming PL/I and sometimes COBOL and Assembler for 18
>> years. These are great languages for z/OS applications. But if I
…[4 more quoted lines elided]…
> and PC assembly is an abomination.

ANYONE can have access to COBOL on the PC and there are some excellent 
implementations available. I have been using Micro Focus and Fujitsu COBOL 
for over 20 years on PCs. They are both excellent products.

PC Assembly is no more an abomination than BAL is. They are just different, 
that's all. If you consider the unfamiliar to be an "abomination" then that 
says more about your mind set than it does about the language in question.


> For those reasons and others as
> well, I don't code on the PC except a little in Ada. Anything else is
> well, just too offensive!

Making programming into a religion may not be a good path to follow. It is 
just computer programming. If you feel so strongly that any breach of your 
commandments for good programming is offensive or an abomination, then you 
are likely to miss out on much that is good and useful. However, it is of 
course, a personal choice.

For me, to be offended by the facilities offered in a computer programming 
anguage is about as logical as being offended by the menu at my local diner. 
Don't like it? Don't order it. Being offended by it is way to sensitive. 
Life is too short... :-)


>Some of us want to make our PC's as much
> like mainframes as we can,

I can't imagine why. Do you also want your bicycle to be as much like a car 
as it can? :-)

If you view a PC in the same way you view a mainframe, you are missing the 
point. A PC on its own, is nothing special. When you start connecting them 
they can do things that mainframes never could. Notice that the arrival of 
the internet didn't happen in the decades when mainframes ruled the world. 
It is about synergy from connectedness. And that is also why the OO paradigm 
has largely replaced the procedural one.That is hard for some "mainframe 
guys" to take (usually the ones who want their PC to be as much like a 
mainframe as possible... :-)) but there are some of us who actually made the 
transition and are happy in either or both camps, recognising things of 
value in both arenas.



>Ada is the cheapest way to do that. COBOL
> is fine for what it is for but I agree it's too limited for general
> purpose programming unless you enjoy stabbing yourself in the eyes
> with a pen.

And yet the world stabbed itself in the eyes with a pen for 50 years, and in 
some quarters is still doing it. Those of us who made a living from COBOL 
did not notice any soreness of the eyes. On the contrary, we actually loved 
it. (I still enjoy working in COBOL although I find it more tedious now than 
I used to before I knew there were better alternatives available.)

I would strongly contest your statement that COBOL is "too limited for 
general purpose programming", having written applications that range from 
heuristic maze traversal, through syntax scanning and parsing of language 
and free format postal addresses, to interactive Web Pages with it, but 
maybe your concept of "limited" and mine are two different ones.

>
>> As IDE I use Rational Team Concert (RTC). RTC uses a repository
…[9 more quoted lines elided]…
> But that takes a PC with alot of power.

Well, it depends what you mean by a "lot"...Certainly, you wouldn't want to 
run it on a x86 under DOS, but ANY modern PC can EASILY accomodate this. I 
was managing projects nearly 10 years ago that used PCs for development in 
precisely this configuration. Not only did they run Java but they were using 
AJAX as well.

You have become so accustomed to viewing a PC as a Mainframe that you have 
lost sight of what they CAN accomplish.

OK, I'm sure your post was light hearted (as my response has been) but the 
bottom line is that Java is a perfectly good language... and so are ADA, 
COBOL, and, in fact, MOST computer programming languages.

(In 40 years in the industry I have become familiar with quite a few and the 
only one I actually loathed and detested was JSP, but it is arguable whether 
that was a "language" as opposed to a "methodology" and my distaste for it 
was more because it limited what I could do in COBOL, and because it was 
"mandated" by an obnoxious little prick who had never written a computer 
program in his life, and enjoyed abusing the tiny bit of power he had been 
given. He threatened to have me fired but I was still there when he left.)

As a sometime regular poster here remarked on several occasions: "It is the 
Artist, not the paintbrush."


>Most commodity PC's die under
> the bloat of Java and Eclipse.

Not sure what you mean by "commodity" in this context. I have never had a PC 
running Java  and Eclipse die under the weight of it. Anything bought within 
the last 3 years should run this easily.

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Nomen Nescio <nobody@dizum.com>
- **Date:** 2010-07-25T00:01:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41b9646285f58ef9794bfbb648fc766d@dizum.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net>`

```
> It is an excellent way to pick up the concepts of Object Orientation, as
> it was designed around those concepts.

No it is not. It is an excellent way to pick up Java's view of OO, which is
not the same thing.

> If by "dumbing down" you mean simpler, less intricate code, then how is
> that a  bad thing? 

Because 100 out of 100 Java "programmers" have no idea what the machine is
doing, and 99/100 Java coders have no idea what the JVM is doing. I don't
consider anything that enables idiots to write code that more or less
provides the desired output as helpful or worthwhile.

> "sloppy" :    Languages are not sloppy; programmers are sloppy.

Not true, language designs themselves can be sloppy, and Java is an example
of that.

> "unsafe" :     Competent programmers and compilers/interpreters make code
> in any language safe.

Also not true, Java constrains you and simply doesn't offer the facilities
it should, so no matter how competent you are you can't write safe code in
Java. 

> There are benefits in using Java or any other high level language over
> most Assembler level languages, but compactness of code and run time are
…[3 more quoted lines elided]…
> be more important than size of runtime. 

I haven't seen any code worth writing where the questionable usefulness or
"benefits" of Java are worth the burden of a VM and runtime.

> It is just silly in this day and age, with the computing resources now 
> available, to rant about modern languages "dumbing down" the art of 
…[4 more quoted lines elided]…
> commercial application development), they are not.

I don't agree with your view, and it's clear that people who share it are
wrong. True, computing resources have grown but not to offset the
performance costs of sloppy code and poorly designed languages and
applications. That is one of the reasons we're in a recession, because the
costs of doing business based on incompetent CTO's making incorrect
technical decisions has made IT a huge cost. You shouldn't need to buy a
new mainframe every year or two according to your view, but you do need to
because of inefficient code and applications.

> ANYONE can have access to COBOL on the PC and there are some excellent
> implementations available. I have been using Micro Focus and Fujitsu
> COBOL for over 20 years on PCs. They are both excellent products.

I said they're not commonly found on the PC and they are not. Just because
you bought them doesn't mean everyone can buy them, especially when most PC
users consider 49 or 99 dollars an upper limit for any PC app.

> PC Assembly is no more an abomination than BAL is. They are just
> different, that's all. If you consider the unfamiliar to be an
> "abomination" then that says more about your mind set than it does about
> the language in question.

It is an abomination, and you would know that if you had looked at
it. First of all there is no one PC assembly language, that in itself is a
big problem. You shouldn't have to learn 2 completely opposite syntaxes to
use assembler on one platform and to be able to move code from system to
system. You do have to do that on the PC.

> Making programming into a religion may not be a good path to follow. It
> is just computer programming. If you feel so strongly that any breach of
> your commandments for good programming is offensive or an abomination,
> then you are likely to miss out on much that is good and useful. However,
> it is of course, a personal choice.

That's nonsense. The point is you have to have some view of good and bad or
you're lost. Not everything is acceptable, and the more you know and the
more pride you take in your work, the more you have opinions based on
experience about what good and bad mean and how they affect life in the
long run.

> I can't imagine why. Do you also want your bicycle to be as much like a
> car as it can? :-)

The difference is I can afford both a bicycle and a car for their different
uses but most people cannot afford a mainframe. Given mainframe people know
mainframes are better, everyone should want one.

> they can do things that mainframes never could. Notice that the arrival
> of the internet didn't happen in the decades when mainframes ruled the
> world. 

Not so, I used internet from a mainframe before most people knew there was
an internet. And we could argue it was better in those days ;)

> And yet the world stabbed itself in the eyes with a pen for 50 years, and
> in some quarters is still doing it. Those of us who made a living from
…[3 more quoted lines elided]…
> alternatives available.) 

You seem to be arguing against yourself. 

> I would strongly contest your statement that COBOL is "too limited for
> general purpose programming", having written applications that range from
> heuristic maze traversal, through syntax scanning and parsing of language
> > and free format postal addresses, to interactive Web Pages with it, but
> > maybe your concept of "limited" and mine are two different ones. 

You can code almost anything in any language (and you certainly seem to
have done so!) but that doesn't prove that language is a good choice. Being
a good coder is having access to the right tools and knowing which ones to
use and which not to use. COBOL is certainly not suited to much beyond
reports and financial systems (where it does shine). Using the correct
languages for all these projects would have made the code much smaller,
more readable, and more maintainable.

> You have become so accustomed to viewing a PC as a Mainframe that you
> have lost sight of what they CAN accomplish.

I don't think so, I find PC's very limited and not interesting.

> OK, I'm sure your post was light hearted (as my response has been) but
> the  bottom line is that Java is a perfectly good language... and so are
> ADA, COBOL, and, in fact, MOST computer programming languages.

I don't agree (with the last part!) There are many awful languages, if I
was to list a few I would include Java, C++, Pascal, and most if not all
interpreted languages. There are very few great languages, especially if
you're talking about great general purpose languages. There are many great
specialty languages but their usage is obviously limited. What makes a
language great? Expressiveness, clarity, quality of the executable
produced, things like that. What makes a language awful? Complexity,
inefficiency, complicated syntax for it's own sake, ugliness, etc. Yes,
there is an aspect of art in programming languages. They are tools but so
is a 2 dollar Chinese pot-metal chisel and so is a 300 dollar hand-forged
and machined chisel and I know the difference.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-25T17:24:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b2052FbfhU1@mid.individual.net>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
Nomen Nescio wrote:
>> It is an excellent way to pick up the concepts of Object
>> Orientation, as it was designed around those concepts.
>
> No it is not. It is an excellent way to pick up Java's view of OO,
> which is not the same thing.

And what part of "Java's view of OO" is NOT OO?
>
>> If by "dumbing down" you mean simpler, less intricate code, then how
…[4 more quoted lines elided]…
> doing.

Donkeys eat carrots.
You eat carrots
Therefore you are a donkey.

"100 out of 100" eh?

I'm a Java programmer (inasmuch as I can and have programmed working 
applications in Java.) I know what the machine is doing and I understand the 
JVM just as I understand CLR for .NET

You statement would therefore appear to be erroneous. (There is at least ONE 
donkey who DOESN'T eat carrots. :-))

Actually, even if you were right, why would it matter? A programming 
language is intended for you to communicate with a computer. If you speak in 
English with someone whose native language is Swahili, do you have to know 
Swahili before you can be sure they understood what you said?


>.I don't consider anything that enables idiots to write code
> that more or less provides the desired output as helpful or
> worthwhile.
>
And, by "idiots" you mean anyone other than yourself, or those who espouse 
the same approach as you do?

>> "sloppy" :    Languages are not sloppy; programmers are sloppy.
>
> Not true, language designs themselves can be sloppy, and Java is an
> example of that.

Perhaps you could provide a sample to support your contention, rather than 
just an assertion?

>
>> "unsafe" :     Competent programmers and compilers/interpreters make
…[4 more quoted lines elided]…
> write safe code in Java.

Really?

I wonder what the World's Java programmers will make of that?

Again, something a bit more than just a high-handed assertion might help 
your case.

>
>> There are benefits in using Java or any other high level language
…[10 more quoted lines elided]…
>

Just as well you don't get to make financial decisions regarding computer 
system development then...:-) I'd love to know how you decide that code is 
"worth writing"... maybe some other time over a beer :-)

>> It is just silly in this day and age, with the computing resources
>> now available, to rant about modern languages "dumbing down" the art
…[8 more quoted lines elided]…
> are wrong.

ROFL!  Don't worry, there are only a few of us... :-)


>  True, computing resources have grown but not to offset the
> performance costs of sloppy code and poorly designed languages and
> applications. That is one of the reasons we're in a recession,
> because the costs of doing business based on incompetent CTO's making
> incorrect technical decisions has made IT a huge cost.

Present your findings to the next G8 conference. (You could be up for a 
Nobel prize, and I'm sure everybody will be immensely relieved to find that 
all they have to do is revamp their IT practises..:-)) IT is NOT a huge 
cost. In fact, it is cheaper now than it has ever been. While, I wouldn't 
disagree there are some very poor CTOs, that doesn't mean they are ALL 
wrong. There are some very smart ones as well. (I know one or two...) Many 
companies are taking IT decisions which make sense in the current economic 
climate. Not because IT is expensive or because their CTO is incompetent, 
but because the recession is forcing ALL areas of the company to be 
scrutinised. Sometimes this scrutiny reveals that historically embedded 
practices (both in SOPs AND IT) are costing a lot more than they should be 
and alternatives need to be found.

Sometimes the alternatives can be outsourcing, packages, even Java... :-) I 
don't know of any cases where they moved to assembler language as a cost 
saving measure... :-)

>You shouldn't
> need to buy a new mainframe every year or two according to your view,
> but you do need to because of inefficient code and applications.

I actually have no opinon about how often someone should replace their 
mainframe; largely because my company doesn't currently use a mainframe. 
However, for the sake of this discussion, let's say I don't think people 
need to buy a new mainframe every year or two. And yet they do. Is it 
because of "inefficient code and applications" (basically, 
"incompetence"...) or is it because they have been persuaded by a salesman 
that what they have is obsolete, or it won't run the latest and greatest 
apps that are about to be released, or support is likely to be dropped, or 
any one of dozens of "other" reasons why?

My point is that the reason you cite is NOT the ONLY possible reason...

>
>> ANYONE can have access to COBOL on the PC and there are some
…[4 more quoted lines elided]…
> I said they're not commonly found on the PC and they are not.

COBOL IS commonly found on the PCs of people who are interested in COBOL.


> Just
> because you bought them doesn't mean everyone can buy them,
> especially when most PC users consider 49 or 99 dollars an upper
> limit for any PC app.

Both MicroFocus and Fujitsu have provided free student editions of their 
products for decades. Since Fujitsu North America changed hands it has been 
harder to find a free version of Fujitsu COBOL but they are available. 
Veryant have promised a free student version of their isCOBOL product (which 
is Java oriented, incidentally...) in the near future, right in this very 
forum, within the last week, and OPEN COBOL has been free and available for 
some years now.

Now, if you are considering developing revenue earning applications, you 
will need to pay run time fees to Micro Focus if you use their product, you 
will need to buy a FULL version of Fujitsu if you choose to use their 
product  (no run time fees or royalties), and OPEN COBOL is free.

I would remind you at this point that VB.NET, C#, C++, and Java are all 
FREE.


>
>> PC Assembly is no more an abomination than BAL is. They are just
…[5 more quoted lines elided]…
> it.

That is simply rude. I have not only looked at it, I have programmed in it 
for some 18 months when PCs first appeared. I've written TSRs in it and 
interfaced it to MicroFocus COBOL. You may be used to people making 
statements for which they have no experiential foundation; do not categorize 
me as such. I know whereof I speak.


> First of all there is no one PC assembly language, that in itself
> is a big problem.

That is no problem at all. If you want to write Motorola 68000 code, learn 
that. If you want to write Intel  x86 code, learn that. If you want to write 
IBM mainframe Assembler code, learn BAL then progress to macro assembler. 
Those are the "joys" of low-level programming. If you want one language that 
will run on ALL these platforms,  use COBOL (oops, you don't want to pay for 
it... OK, learn Java). How hard is that?

If you are referring to the syntax differences between AT&T x86 and Intel 
x86 serves you right for trying to move to Linux :-) Actually, that's not a 
problem either: code in MASM then run it through GAS, or code in GAS and 
select the platform you want.

All it takes is a little imagination and thinking outside the box.




>You shouldn't have to learn 2 completely opposite
> syntaxes to use assembler on one platform and to be able to move code
> from system to system. You do have to do that on the PC.

No you don't. See above.

>
>> Making programming into a religion may not be a good path to follow.
…[6 more quoted lines elided]…
> bad or you're lost.

Some things work better than others, true. Some people see more than others, 
also true. Just because computers see black and white doesn't mean that 
programmers have to. There are many shades of grey surrounding most 
problems.Digging for facts is better exercise than jumping to conclusions, 
or deciding "that's how I've always done it". Treat problems as new and 
worthy of respect. Seek to develop and extend your toolbox and your mind, 
rather than deciding there is only one right way. As your tools expand, so 
will your mind. If you just have one viewpoint and measure everything aginst 
that, you will not get optimum solutions. To a man with a hammer, everything 
is a nail. There is no "good" or "bad"; there are solutions that work and 
solutions that don't. Sometimes there are solutions that work better. These 
are usually found by iteration of a solution, not instantly recognized on 
day one (unless the problem is truly a trivial one...)


> Not everything is acceptable, and the more you
> know and the more pride you take in your work, the more you have
> opinions based on experience about what good and bad mean and how
> they affect life in the long run.
>
Only if your mind is closed. It is good to take pride in your work and we 
all strive to get the best result we can. But if you don't re-evaluate why 
you hold a certain approach to be "good", and measure it in the light of new 
tools and experience, there can be no growth. This might not matter to you, 
and some people are quite content to hit every problem with a hammer and go 
home at 5 o'clock. Not me. My career has been a personal and professional 
growth path which has been fun and satisfying. I'm a better person now than 
I was, and I'm a better programmer now than I was. Good result :-).


>> I can't imagine why. Do you also want your bicycle to be as much
>> like a car as it can? :-)
…[3 more quoted lines elided]…
> mainframe people know mainframes are better, everyone should want one.

:-)

>
>> they can do things that mainframes never could. Notice that the
…[5 more quoted lines elided]…
> ;)

I suggest that what you used was not "the Internet" (World Wide Web, as 
currently understood, although we know there are many more sub-nets than 
just that one...). But it really doesn't matter... If you used connected 
mainframes over any kind of network you should be broader minded about 
connection and synergy than you appear to be. Maybe you were enjoying the 
technical achievment so much you missed the conceptual significance.

In 1973 I was involved in setting up the first satellite link between a 
mainframe in Melbourne (Australia) and a batch terminal in Wellington (New 
Zealand), a distance of about 2500 KM as the crow flies, but much further 
when you consider the distance the signal has to travel up and down to the 
satellite. I couldn't get it to work and ended up going to Melbourne to 
inspect the front-end software on the Cyber. It was a real technical 
challenge as other terminals around Australia were working fine. After 
poring through the code for a couple of days I realised the problem and set 
some delay loops to make it hold our connection. Flew back to Wellington and 
we tried it. The terminal screen just filled with garbage and then suddenly, 
it cleared and the first 3 words appeared neatly at the top of the screen: 
"Haeremai! Haeremai! Haeremai!" (thrice welcome, in Maori...the Melbourne 
operator was a Kiwi). I was so thrilled at having solved the technical 
problem it never occurred to me what this actually meant in terms of 
business and access for problem solution...or in terms of the cash flow it 
would generate and the jobs it would secure. Sometimes we get so focussed on 
one aspect of a problem we can miss the other aspects.
 >
>> And yet the world stabbed itself in the eyes with a pen for 50
…[6 more quoted lines elided]…
> You seem to be arguing against yourself.

No, I still enjoy COBOL, I just have a more realistic context for it. My 
eyes don't hurt.
>
>> I would strongly contest your statement that COBOL is "too limited
…[11 more quoted lines elided]…
> does shine).

I would argue that reporting is not a strength of COBOL. I haven't used it 
for reporting much since Relational databases became available in 1983. Once 
the data repository is relational there are far better tools to extract 
reports from it than COBOL. Crystal Reports and Stimulsoft are just 2 I have 
used and been very satisfied with. I see no point in counting printline 
fillers when I can drag and drop what I want, where I want...:-)

> Using the correct languages for all these projects would
> have made the code much smaller, more readable, and more maintainable.
…[4 more quoted lines elided]…
> I don't think so, I find PC's very limited and not interesting.

I rest my case. :-)  (You see them just like mainframes...)
>
>> OK, I'm sure your post was light hearted (as my response has been)
…[12 more quoted lines elided]…
> own sake, ugliness, etc.

OK, at least you gave examples to support your statement. I won't argue 
this, because I think not much would be achieved by doing so (and I really 
don't care :-); I long ago gave up worrying about what constitutes a "good" 
or "bad" language...) With the advent of functional languages and 
non-procedural code it is pretty much academic anyway. Nevertheless, if you 
search the adjectives you used above I think you will find that many of them 
are subjective and arguable. (What you call "ugliness" I might consider 
"elegance", what you call "complexity" may be "crystal clear" to me...etc.)

I totally respect your right to disagree. All I ask is that you consider the 
arguments, rather than decide that what you currently do is "right". It 
might well be, but it doesn't hurt to re-measure occasionally, does it? :-)


>Yes, there is an aspect of art in
> programming languages.

I would argue there is an aspect of "art" in programming. Attributing this 
to the languages is very much admiring the paintbrush instead of the artist.

<small snip>

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:35:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pl3r46hj6cggdigb1umuk4si7euc1fnp81@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com> <8b2052FbfhU1@mid.individual.net>`

```
On Sun, 25 Jul 2010 17:24:49 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>>You shouldn't
>> need to buy a new mainframe every year or two according to your view,
…[12 more quoted lines elided]…
>My point is that the reason you cite is NOT the ONLY possible reason...

As computers get cheaper, we use them more.   We buy more hard drives,
and use tapes less.   We upgrade the processors so the batch jobs that
used to run from 1:00 to 7:00 get done at 3:00.   We upgrade the
efficiency so that we don't need so much air conditioning and space.
And we add capability to have a big data warehouse with real-time
access for customers to make better decisions.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-25T01:02:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf1ebf92-1116-4342-b3e9-04a31fa8ef61@u31g2000pru.googlegroups.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Jul 25, 10:01 am, Nomen Nescio <nob...@dizum.com> wrote:

> No it is not. It is an excellent way to pick up Java's view of OO, which is
> not the same thing.

There are several 'views' of OO, none of them are _THE_ view. Such
things as multiple inheritance, operator overloading, factory, are all
issues that can be argued for or against.

> Because 100 out of 100 Java "programmers" have no idea what the machine is
> doing, and 99/100 Java coders have no idea what the JVM is doing. I don't
> consider anything that enables idiots to write code that more or less
> provides the desired output as helpful or worthwhile.

Exaggeration merely highlights your high opinionated ignorance.

> I don't agree with your view, and it's clear that people who share it are
> wrong.

Just yell 'I am right and the rest of the world is wrong' over and
over and we will see if that convinces anyone.

> True, computing resources have grown but not to offset the
> performance costs of sloppy code and poorly designed languages and
> applications. That is one of the reasons we're in a recession,

Complete uninformed nonsense.

> because the
> costs of doing business based on incompetent CTO's making incorrect
> technical decisions has made IT a huge cost. You shouldn't need to buy a
> new mainframe every year or two according to your view, but you do need to
> because of inefficient code and applications.

You are confused.

> I said they're not commonly found on the PC and they are not. Just because
> you bought them doesn't mean everyone can buy them, especially when most PC
> users consider 49 or 99 dollars an upper limit for any PC app.

You are uninformed.

The largest number for an application is MS Office and that is much
more than 49 or 99 dollars so most users do not find those numbers an
upper limit.

> It is an abomination, and you would know that if you had looked at
> it. First of all there is no one PC assembly language, that in itself is a
> big problem. You shouldn't have to learn 2 completely opposite syntaxes to
> use assembler on one platform and to be able to move code from system to
> system. You do have to do that on the PC.

Clue number 1: there is no one assembly language on mainframes. It may
be that there is one main IBM OS/MVS assembly (or whatever it is these
days) but those are not the only mainframes. Every architecture has,
of necessity, at least one assembler. Some have several. This means
that there are hundreds of assemblers.

Or are you so limited that you can't think beyond IBM Z Series and
Intel P4 ?

> The difference is I can afford both a bicycle and a car for their different
> uses but most people cannot afford a mainframe. Given mainframe people know
> mainframes are better, everyone should want one.

Are mainframes better at being laptops ? Are mainframes better at
being in-car systems ? Are mainframes better at being smart phones ?

Do you drive a Mack Truck because it is better than a car ?

> I don't think so, I find PC's very limited and not interesting.

I learned very early in life that the more one knew about something
the more interesting it was.  The corollary is that the reason people
find something uninteresting is because they know nothing about it.

The 'limitation' is yours and the 'uninteresting' is due to your
complete lack of knowledge.

> I don't agree (with the last part!) There are many awful languages, if I
> was to list a few I would include Java, C++, Pascal, and most if not all
…[8 more quoted lines elided]…
> and machined chisel and I know the difference.

There are many ways to judge languages. You have been indoctrinated
with the need for 'efficiency' of the executable. I Have clients where
a commodity single core PC under Linux runs all their users (50-60)
with response times that are unnoticeable and the constraint on
performance is _NOT_ the CPU. Having a compiler that produced 'better'
code would make zero difference.

Certainly if I was working in systems dealing with millions of
transactions an hour or a minute then I would care, but I don't.

Just as there are people that care about race car engines and
extracting the last ounce of horse power there are others that only
care that their car works everytime they turn the key.

I do a lot of coding in 'scripting languages', or specifically Python.
In most cases, with the systems I work on, the CPU load is _not_ the
limit. Having the code in assembly would make almost no difference to
the time taken.

Horses for courses. You may learn that if you ever got off your high
horse and learned something new.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:41:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<404r46964mk2c6m3prrljglvq6roasur9t@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com> <cf1ebf92-1116-4342-b3e9-04a31fa8ef61@u31g2000pru.googlegroups.com>`

```
On Sun, 25 Jul 2010 01:02:52 -0700 (PDT), Richard
<riplin@Azonic.co.nz> wrote:

>There are many ways to judge languages. You have been indoctrinated
>with the need for 'efficiency' of the executable. I Have clients where
…[3 more quoted lines elided]…
>code would make zero difference.

I like the differences between a Codd database design and an Inmon
data warehouse design.   Nice theories but very different, as they are
designed with different criteria for efficiency.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:20:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rn2r46l0ungb5p8li71mo31srjc3fjfvd9@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Sun, 25 Jul 2010 00:01:58 +0200 (CEST), Nomen Nescio
<nobody@dizum.com> wrote:

>> If by "dumbing down" you mean simpler, less intricate code, then how is
>> that a  bad thing? 
…[4 more quoted lines elided]…
>provides the desired output as helpful or worthwhile.

After adjusting your numbers to be more realistic - we can say the
same thing about people who drive cars or exercise their bodies, or
use language.

It very rarely matters how the internals work to achieve the desired
goal.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:22:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Sun, 25 Jul 2010 00:01:58 +0200 (CEST), Nomen Nescio
<nobody@dizum.com> wrote:

>That's nonsense. The point is you have to have some view of good and bad or
>you're lost. Not everything is acceptable, and the more you know and the
>more pride you take in your work, the more you have opinions based on
>experience about what good and bad mean and how they affect life in the
>long run.

Base "good and bad" upon objectives and measurable criteria. Otherwise
you are talking religion.

And the objectives shouldn't be based upon "clean code", but upon "are
the needs of the customer met".
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** starwars <nonscrivetemi@tatooine.homelinux.net>
- **Date:** 2010-07-27T02:43:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com>`

```
> Base "good and bad" upon objectives and measurable criteria. Otherwise
> you are talking religion.

I gave you criteria and a lot of other useful information. I don't recall
any thank yous but I do see a lot of arguments you're making for other
people, I guess you see they can't defend themselves.

> And the objectives shouldn't be based upon "clean code", but upon "are
> the needs of the customer met".

That's an interesting and short-sighted comment. If you say part of the
customer's needs are software that's easily and promptly serviced then
clean code does have a direct and measurable influence on whether those
needs are met.

I see you guys are basically middle-of-the-road dopes who really don't care
about quality or performance or understanding how anything really works as
long as it eventually works (sort of). Those are fine goals for applicance
users (or car drivers, etc.) but for people who do this as a living which I
thought we all were, those are some pretty sorry values.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 7)_

- **From:** Louis Krupp <lkrupp_nospam@indra.com.invalid>
- **Date:** 2010-07-26T19:38:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q4KdnVVt64DipdPRnZ2dnUVZ_radnZ2d@indra.net>`
- **In-Reply-To:** `<780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`

```
On 7/26/2010 6:43 PM, starwars wrote:
<snip>
> I see you guys are basically middle-of-the-road dopes who really don't care
> about quality or performance or understanding how anything really works as
> long as it eventually works (sort of). Those are fine goals for applicance
> users (or car drivers, etc.) but for people who do this as a living which I
> thought we all were, those are some pretty sorry values.

Then don't hire us.  Ever.  To do anything.

Take Perl programming, for example.  I said I'd done some, but don't 
believe me.  I'm useless.  As far as I'm concerned, whatever it is, 
there isn't even a single way to do it.

And COBOL.  If I mention that I taught COBOL once -- to a Women in 
Computer Science program at a university in 1983 -- don't be fooled. 
Most of my students, when interviewed a year or two later at their 
various homeless shelters, their starving and neglected children staring 
wanly at the camera, singled out my class as the experience that ruined 
their lives.

And then there's Unisys.  I worked for what was then Unisys CAD/CAM from 
1987 to 1992.  Know what's happened to Unisys lately?  Reverse stock 
split, that's what, and it's all my fault.  Sure, they try to bury it in 
the annual report, since they're tired of having to explain how I set 
the industry back six years while only working there for five, but it's 
there if you look.  They used to promise they'd recover from whatever it 
was I did in ten years, or fifteen, and now they're shooting for twenty.

So don't hire me.  Or any of us.  Pete sounds like an intelligent guy, 
but what is he hiding from down there in New Zealand?  What is Howard 
really going to do when he retires?  And the one who calls himself Doc 
... there's a story there, I'm sure of it.

"Middle of the road dopes" doesn't begin to describe what you're facing 
here.  If you only knew...

Louis
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 8)_

- **From:** George Orwell <nobody@mixmaster.it>
- **Date:** 2010-07-27T15:44:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<21f7e0a19e02f62700a8b170aeb90c32@mixmaster.it>`
- **References:** `<Q4KdnVVt64DipdPRnZ2dnUVZ_radnZ2d@indra.net>`

```
> Then don't hire us.  Ever.  To do anything.

I wouldn't. I write code and get paid handsomely for doing it. I don't need
to hire anybody to do what I'm already good at- code that you can't write
anyway.

I wasn't taking to you, Louis, why are you arguing with me on Howard's
behalf? Did I slap your girlfriend?

I wouldn't hire you to shine my shoes. You couldn't do that on your best
day. 

> "Middle of the road dopes" doesn't begin to describe what you're facing 
> here.  If you only knew...

I do know, and I don't have any patience for mediocrity or people who don't
care enough about what they do to become experts and have unpopular
opinions based on actually knowing something instead of going with the flow
or hiding behind a cadre of other incompetent people parroting the same
incorrect opinions. Sorry to break up your love-in, girls!

You can write all the Perl in the world and teach women COBOL, that doesn't
make you a man ;-)

Il mittente di questo messaggio|The sender address of this
non corrisponde ad un utente   |message is not related to a real
reale ma all'indirizzo fittizio|person but to a fake address of an
di un sistema anonimizzatore   |anonymous system
Per maggiori informazioni      |For more info
                  https://www.mixmaster.it
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-27T14:36:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i2mqtv$583$1@reader1.panix.com>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net> <Q4KdnVVt64DipdPRnZ2dnUVZ_radnZ2d@indra.net>`

```
In article <Q4KdnVVt64DipdPRnZ2dnUVZ_radnZ2d@indra.net>,
Louis Krupp  <lkrupp_nospam@indra.com.invalid> wrote:

[snip]

>And the one who calls himself Doc 
>... there's a story there, I'm sure of it.

zzzZZZZZzzznnuurrrkkk... zzzZZAAWWWWWWWW... huh? whuh? Onwards, onwards 
for the glory of... oh, sorry, I was... thinking about something, did I 
miss much?

A story behind me?  Pfawgh, nothing special... one day I was working on a 
warehouse loading-dock and thought 'Wouldn't being a COBOL-codin' fool 
beat this like a bass drum at a school-band practise-session?'

And there you have it... ONE and two and THREE and four and 'whoodle 
tootle clang clash *whump* *whump* *whump*'.

DD
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-28T11:53:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b99r2FcjsU1@mid.individual.net>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net> <Q4KdnVVt64DipdPRnZ2dnUVZ_radnZ2d@indra.net>`

```
Louis Krupp wrote:
> On 7/26/2010 6:43 PM, starwars wrote:
> <snip>
…[36 more quoted lines elided]…
> Louis

An amusing and well written response, Louis. :-)

I'm of the opinion that Starwars, George Orwell, Non-Scrivetemi, and Nomen 
Nescio all live under the same bridge and may well be the same Troll. :-)

But, like you, I'm just a "middle of the road dope" so I'm probably wrong...

Pete.

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-27T01:38:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<faa7154f-a85e-46c3-80d0-0e245852a887@z30g2000prg.googlegroups.com>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`

```
On Jul 27, 12:43 pm, starwars <nonscrivet...@tatooine.homelinux.net>
wrote:
> > Base "good and bad" upon objectives and measurable criteria. Otherwise
> > you are talking religion.
>
> I gave you criteria and a lot of other useful information.

You are confused.

You appear to imagine that simplistic anecdotes and unsupported
opinions are "criteria and a lot of other useful information".

In the only other 'starwars' posting in this thread you said you hated
Java and met someone who liked it. How does this constitute "criteria"
or even "useful" ?

Maybe you have posted other stuff somewhere else. Even if you have
also posted as 'Non scrivetemi' those messages are also just opinions
with no substance.


> I don't recall
> any thank yous but I do see a lot of arguments you're making for other
> people, I guess you see they can't defend themselves.

You are confused.

Replies are to the messages. This is a forum not a private conversion
between specific individuals.

> > And the objectives shouldn't be based upon "clean code", but upon "are
> > the needs of the customer met".
…[4 more quoted lines elided]…
> needs are met.

What is 'clean code' is entirely what you are used to.

> I see you guys are basically middle-of-the-road dopes

ad hominem.

> who really don't care
> about quality or performance or understanding how anything really works as
> long as it eventually works (sort of). Those are fine goals for applicance
> users (or car drivers, etc.) but for people who do this as a living which I
> thought we all were, those are some pretty sorry values.

Straw man.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-27T08:29:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pnqt4699v5c9di5cmd3famqrt18dkpcj93@4ax.com>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`

```
On Tue, 27 Jul 2010 02:43:42 +0200 (CEST), starwars
<nonscrivetemi@tatooine.homelinux.net> wrote:

>> Base "good and bad" upon objectives and measurable criteria. Otherwise
>> you are talking religion.
…[3 more quoted lines elided]…
>people, I guess you see they can't defend themselves.

Thank-you for being part of an interesting conversation?   I didn't
figure you for a Donald Trump type.

I just took time to re-read your messages, and those with measurable
objective criteria must not have made it to my computer.   Could you
please re-post them?   Thank-you.

>> And the objectives shouldn't be based upon "clean code", but upon "are
>> the needs of the customer met".
…[4 more quoted lines elided]…
>needs are met.

I don't disagree with your second sentence.   If those are the
customer's needs, then why is my comment short-sighted?

"Quality" does not mean "doing things my way".   Criteria should be
determined according to the goals of the job.    Part of the process
should be making sure the goals are complete and measurable.

>I see you guys are basically middle-of-the-road dopes who really don't care
>about quality or performance or understanding how anything really works as
>long as it eventually works (sort of). 

I think you should get your vision checked.

>Those are fine goals for applicance
>users (or car drivers, etc.) but for people who do this as a living which I
>thought we all were, those are some pretty sorry values.

So you want criteria for programming that doesn't apply to car
drivers?    Interesting, to me, the cost of bad car driving can be
higher than the cost of a quick and dirty program.

I also don't see that "doing this as a living" should have higher
standards than "I'm retired but doing this to buy a toy", or even
"doing this because I love it".

But programming standards should be measured against objective
criteria.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-28T12:41:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b9cm7Fps7U1@mid.individual.net>`
- **References:** `<du2r461tt5fifmbqdrh03hek34i9lhb0na@4ax.com> <780dc34249d4a8a7a0fb0377c7210575@tatooine.homelinux.net>`

```
starwars wrote:
>> Base "good and bad" upon objectives and measurable criteria.
>> Otherwise you are talking religion.
…[3 more quoted lines elided]…
> for other people, I guess you see they can't defend themselves.

Given that you are afraid to post under a consistent identifier, and will 
not use your name, and that your posts are unnecessarily hostile (nobody 
here attacked or flamed you; people requested evidence and citation for some 
of the assertions you made), how do you expect to be taken seriously?

Why would anyone need to defend themselvs when you haven't offered a serious 
argument?

If you are not just some kid looking for an argument then make your case 
according to the generally accepted rules of intellectual discussion: 
premises backed by cites, a reasoned discourse to a valid conclusion. (With 
courtesy and respect for the people you are addressing, and accepting that 
if people disagree, that doesn't make them dopes, it just means they 
disagree.)

In actual fact, most people here would have some sympathy for your views on 
the importance of clean code; but we recognise there are other criteria as 
well. Many people here are or were programmers and were involved in 
programming at a time when optimised and clean code was not just important, 
but essential.  Some of us have programmed systems with 4.8K (minicomputers) 
and 16K (IBM mainframe running TOS) and if code wasn't "clean" apps simply 
couldn't be implemented.

If you ARE just some kid looking for an argument then perhaps your time here 
is being wasted? Try Facebook or Twitter...

>
>> And the objectives shouldn't be based upon "clean code", but upon
…[5 more quoted lines elided]…
> whether those needs are met.

Of course it does, IF you are working with severely limited resources, OR 
you have timing constraints (as in real time processes) where response time 
is absolutely critical. For commercial applications, the difference between 
100 milliseconds and 95 milliseconds is seldom critical.
>
> I see you guys are basically middle-of-the-road dopes who really
> don't care about quality or performance or understanding how anything
> really works as long as it eventually works (sort of).

Given that some of us have been posting to this forums for many years (how 
long have you been doing so?) and the trail of posts would gainsay your 
assertion, would it not be a simple matter to look at some of the history 
before jumping to such a rash conclusion? Personally I don't care what you 
think about me because you haven't established enough credibility for me to 
be interested, but there may be more sensitive types here (I know Doc is 
very easly wounded and so is Howard... :-) (yeah, right)). Apart from that, 
it is simply bad manners and discourteous to insult people you don't even 
know. And it is also very unlikely to win people to your point of view.



> Those are fine
> goals for applicance users (or car drivers, etc.) but for people who
> do this as a living which I thought we all were, those are some
> pretty sorry values.

You may be confusing "doing something for a living" with "being 
professional".

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:24:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h23r469mohqbbjf95hmnf0c8p6sp0c5hun@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Sun, 25 Jul 2010 00:01:58 +0200 (CEST), Nomen Nescio
<nobody@dizum.com> wrote:

>> You have become so accustomed to viewing a PC as a Mainframe that you
>> have lost sight of what they CAN accomplish.
>
>I don't think so, I find PC's very limited and not interesting.

Ahh, therefore tools that are optimized for PC use are a waste!

I see.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:27:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t43r461066b2napqet8frq0bmmfb19kh6a@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Sun, 25 Jul 2010 00:01:58 +0200 (CEST), Nomen Nescio
<nobody@dizum.com> wrote:

>I don't agree (with the last part!) There are many awful languages, if I
>was to list a few I would include Java, C++, Pascal, and most if not all
…[8 more quoted lines elided]…
>and machined chisel and I know the difference.

Measured on how much it costs to do the job.   Which includes
programming, platform, maintenance, etc.     If I'm going to be paid
$10 to poke a hole in a stone wall, I'm not going to buy a $300 tool.
That would be an ugly decision and a poor choice.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:33:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1h3r4610gehqmdiavul97r1rhj7616hgqr@4ax.com>`
- **References:** `<8autnoFsbcU1@mid.individual.net> <41b9646285f58ef9794bfbb648fc766d@dizum.com>`

```
On Sun, 25 Jul 2010 00:01:58 +0200 (CEST), Nomen Nescio
<nobody@dizum.com> wrote:

>It is an abomination, and you would know that if you had looked at
>it. First of all there is no one PC assembly language, that in itself is a
>big problem. You shouldn't have to learn 2 completely opposite syntaxes to
>use assembler on one platform and to be able to move code from system to
>system. You do have to do that on the PC.

A big attraction of CoBOL is that I could run it on a Honeywell or
Univac or IBM or any one of the mainframe computers - even though:
First of all there is no one mainframe assembly language.

But Java is better at running on different platforms than CoBOL is.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-26T04:00:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c70422d-e6e4-4794-b814-fc4560cd5cb6@i28g2000yqa.googlegroups.com>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net> <8autnoFsbcU1@mid.individual.net>`

```
On Jul 24, 2:25 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> As a sometime regular poster here remarked on several occasions: "It is the
> Artist, not the paintbrush."
>

and as one artist remarked: you're paying for the 25 years of
experience and not the twenty minutes it took to effect the work of
art.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-26T07:16:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dh2r46pcgiu475nl0ce23detb7du5mceap@4ax.com>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net> <8autnoFsbcU1@mid.individual.net>`

```
On Sat, 24 Jul 2010 13:25:10 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>It is just silly in this day and age, with the computing resources now 
>available, to rant about modern languages "dumbing down" the art of 
…[4 more quoted lines elided]…
>application development), they are not.

The criteria for "dumbing down" changes over time.    And it applies
to a wide variety of skills besides computers.     Old timers tend to
regret changes that make their own skills less valuable in new
environments.   That lamentation is as old as time.
```

###### ↳ ↳ ↳ Re: Hobby languages

- **From:** Jessica Colman <jessica.colman@augustakom.net>
- **Date:** 2010-07-24T19:19:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i2f7ad$d2n$1@news.m-online.net>`
- **In-Reply-To:** `<73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net>`
- **References:** `<i2bg9o$2hl$1@news.m-online.net> <73fb3ca7b5c8ea0f80905f32ebe45274@msgid.frell.theremailer.net>`

```
>> Interesting: None of you mentioned Java.
> 
> That was intentional because we're mostly mainframe guys with sense ;)

Well, I may not be a mainframe GUY, but I'm not with no sense ;-))

For almost anything, Pete answered in better terms than I could (he 
spoke "out of my soul" as say in Germany).

> Do you not have to pay big euros for Rational anything?

This is not an advertisement on Rational stuff. But I really love the 
concept behind RTC. The Express-C edition is free for up to 10 
developers and for "hobby programming" the missing features included in 
the (expensive) enterprise edition do not matter. If you like: Go to 
http://jazz.net

> 
>> So, my recommendation is: Java with Eclipse and ANT.
…[3 more quoted lines elided]…
> 

Yes, in this case you are right (the only case :-)). But developing in 
Java or any OO language needs a smart and powerful IDE. A simple editor 
just won't do. But the benefit you get from eclipse is worth spending 
some euros or dollars on a powerful PC.

Jessica
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 4)_

- **From:** starwars <nonscrivetemi@tatooine.homelinux.net>
- **Date:** 2010-07-25T01:59:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net>`

```
> > That was intentional because we're mostly mainframe guys with sense ;)
> 
> Well, I may not be a mainframe GUY, but I'm not with no sense ;-))

I was surprised to see someone (guy or woman) with 18 years of mainframe
experience who actually likes Java but Pete also has some years and likes
it. I've been around as long as Pete and I hate it. So we can't draw many
conclusions except you and Pete would probably enjoy a long weekend
together. Get a room!
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-25T15:15:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b1oicF88qU1@mid.individual.net>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net>`

```
starwars wrote:
>>> That was intentional because we're mostly mainframe guys with sense
>>> ;)
…[7 more quoted lines elided]…
> enjoy a long weekend together. Get a room!

I spent 20 years prgramming mainframes (and not just IBM ones, either). 
Largely because there was no alternative. Started programming in 1965 in 
assembler languaes and moved to COBOL in 1967. (Actually, I got dragged 
kicking and screaming into COBOL and it was some time before I recognised 
how useful it was... I think my programming level at that time was much akin 
to what Nomen Nescio's development appears to be currently: "What I know and 
the way I do it is the only RIGHT way". Ah, the arrogance of youth.. :-) 
Fortunately, we grow...:-))

I have a soft spot  for Java because it enabled me to learn Object 
Orientation at a time when OO COBOL seemed unintelligible. Apart from that, 
many people and companies find Java to be a very good development language 
and, as I mentioned, I have managed some significant projects where Java and 
Eclipse were the development platform and they worked very well.

AFTER teaching myself Java and writing a few applications in it (I can 
highly recommend Rogers Cadenhead's book "Sam's teach yourself Java 2 in 24 
hours" although that was not the only book I referenced) I was able to go 
back to OO COBOL and it all fell into place.

I believe that after 18 years as a mainframe programmer, Jessica is entitled 
to bit more respect than has been shown by some posters (not naming any 
names... just follow my eyes... :-)) That was partly why I posted in favour 
of Java, but mainly because I honestly believe Java to be a useful language.

For myself, I don't use it much any more as I prefer C#, but that doesn't 
blind me to the fact that many people are very happy with it.

Don't you think it is kind of sad to get emotional about a computer 
programming language?

I LOVE x... I HATE y...   where x and y are rigidly codified systems of 
communicating with computers. How can you HATE Java, or any other language? 
Iguess we can all have our preferences but assigning strong emotion to 
computer programming languages is really just silly. (And I have been as 
guilty of this over the years as anybody else here...Fortunately, as time 
passes and experience is acquired, we grow...)

I HATE racial intolerance and social injustice... I intensely dislike JSP 
programming. :-)

As for getting a room with Jessica: if we were working on a Java project I'd 
be happy to do that, and share it with the rest of the team as well... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 6)_

- **From:** Jessica Colman <jessica.colman@augustakom.net>
- **Date:** 2010-07-25T09:50:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i2gqbu$u2p$1@news.m-online.net>`
- **In-Reply-To:** `<8b1oicF88qU1@mid.individual.net>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net> <8b1oicF88qU1@mid.individual.net>`

```
> 
> As for getting a room with Jessica: if we were working on a Java project I'd 
> be happy to do that, and share it with the rest of the team as well... :-)

Let me know if you come to Munich :-))

Jessica
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-26T02:35:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b30d7F30dU1@mid.individual.net>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net> <8b1oicF88qU1@mid.individual.net> <i2gqbu$u2p$1@news.m-online.net>`

```
Jessica Colman wrote:
>> As for getting a room with Jessica: if we were working on a Java
>> project I'd be happy to do that, and share it with the rest of the
…[4 more quoted lines elided]…
> Jessica

Thank you, Jessica. :-)

I lived in Dueselldorf for around 4 years and, of course, visited Muenchen 
and Bayern. I still have a few friends in Germany but it is unlikely I'll 
spend time working there again.

These days I am enjoying being home and the Pacific lifestyle.

Although the Rhine was very beautiful, I enjoy surf beaches more... :-)

Tchuess!

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 8)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2010-07-26T14:52:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c4d84f6$0$283$14726298@news.sunsite.dk>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net> <8b1oicF88qU1@mid.individual.net> <i2gqbu$u2p$1@news.m-online.net> <8b30d7F30dU1@mid.individual.net>`

```
Pete Dashwood wrote:

> Jessica Colman wrote:
>>> As for getting a room with Jessica: if we were working on a Java
…[13 more quoted lines elided]…
> These days I am enjoying being home and the Pacific lifestyle.

I missed the obvious remark about the Bavarian beers, which might have
influenced your choices. ;-)
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-27T10:54:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b6i1iFpfdU1@mid.individual.net>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net> <8b1oicF88qU1@mid.individual.net> <i2gqbu$u2p$1@news.m-online.net> <8b30d7F30dU1@mid.individual.net> <4c4d84f6$0$283$14726298@news.sunsite.dk>`

```
Fred Mobach wrote:
> Pete Dashwood wrote:
>
…[18 more quoted lines elided]…
> influenced your choices. ;-)

A very good point, Fred.

Living in Germany certainly spoiled beer drinking for me. The fine beers 
produced according to the Rheinheitsgebot are SO far ahead of the fizzy 
chemical concoctions that pass for beer in the rest of the world, that I 
find it very hard to drink beer when outside Germany. Here in NZ they are 
starting to produce pure beers that have no enzymes, fillers, rice, or 
chemical accelerants in them, and one or two of these are not bad, but my 
palate still remembers and hankers for "ein grosses Koenigs oder Bitburger 
Pils..."  I loved watching it being drawn and seeing the white foam slowly 
replaced by the pale golden nectar that is good Pils.... ah, happy times!

Fortunately, NZ is producing very good wine at very reasonable prices so my 
attention has shifted more in that direction.

Pete.
```

###### ↳ ↳ ↳ Re: Hobby languages

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-27T08:41:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<efrt46trfe7ovlrjfg8p6mo7g8ggbep85m@4ax.com>`
- **References:** `<i2f7ad$d2n$1@news.m-online.net> <121a2cbb893f452d34b21da55893598b@tatooine.homelinux.net> <8b1oicF88qU1@mid.individual.net> <i2gqbu$u2p$1@news.m-online.net> <8b30d7F30dU1@mid.individual.net> <4c4d84f6$0$283$14726298@news.sunsite.dk> <8b6i1iFpfdU1@mid.individual.net>`

```
On Tue, 27 Jul 2010 10:54:41 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Living in Germany certainly spoiled beer drinking for me. The fine beers 
>produced according to the Rheinheitsgebot are SO far ahead of the fizzy 
…[6 more quoted lines elided]…
>replaced by the pale golden nectar that is good Pils.... ah, happy times!

Of course, taste is taste.    Personally, I'd much rather drink
Belgian ale than German Pilsner.    (Not to say that Germans don't
make good ale too - but there are microbreweries all over the world
with fine brews).    It would be convenient if I liked lagers.

I do like the whole thing about having so many new microbreweries.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
