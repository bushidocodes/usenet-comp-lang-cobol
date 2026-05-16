[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO as a Form of Modular Programming

_5 messages · 4 participants · 2007-02 → 2007-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO as a Form of Modular Programming

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-20T13:56:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12tmh42rjop5627@corp.supernews.com>`

```
The above subject is discussed in Bertrand Meyer,
"Object-Oriented Software Construction," Second
Edition, 1997, Chapter 3, "Modularity".

I have omitted much of the text in order to support
and emphasize the points I have raised recently.
OO [Design] is modular programming, and
Modular programming is design methods.

"Modular programming was once taken to mean the
construction of programs as assemblies of small pieces,
usually subroutines. But such a technique cannot bring
real extendibility and reusability benefits unless we have
a better way of guaranteeing that the resulting pieces
-- the modules -- are self-contained and organized in
stable architectures. ...

"A software construction method is modular, then, if it
helps designers produce software systems made of
autonomous elements connected by a coherent, simple
structure. ... The focus will be on design methods, but
the ideas also apply to earlier stages of system construction
(analysis, specification) and must of course be maintained
at the implementation and maintenance stages.

"... This chapter introduces a set of complementary
properties: five criteria, five rules and five principles of
modularity which, taken collectively, cover the most
important requirements on a modular design method.

"... The discussion will lead in a later chapter to the O-O
form of module -- the class -- ..."

-----

Found on the internet, some time ago:

C++ is the only current language making
COBOL look good. -- Bertrand Meyer
```

#### ↳ Re: OO as a Form of Modular Programming

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-20T12:30:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<snimt2tobutpn4fn2f7fiib7hhmi2mc5rj@4ax.com>`
- **References:** `<12tmh42rjop5627@corp.supernews.com>`

```
On Tue, 20 Feb 2007 13:56:29 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>"Modular programming was once taken to mean the
>construction of programs as assemblies of small pieces,
…[4 more quoted lines elided]…
>stable architectures. ...

It's a changing target.    But one requirement seems to be that each
module is something that has been created and assembled to create the
final product.    Modular homes include pre-fabricated walls complete
with electrical wires.   Re-usability hasn't been a requirement in the
past.

Larger modules are easier to work with.   A house built with modular
rooms goes together faster than a house built with modular walls. And
objects go together faster than COMPUTE statements which go together
faster than assembler which replace machine language.

Modules can also be stronger and safer - that modular wall could have
been built in ideal conditions and tested before being incorporated in
the house.

Certainly objects are a type of module - with more power and utility
than paragraphs and copy members.
```

##### ↳ ↳ Re: OO as a Form of Modular Programming

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-03-01T23:54:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XfqdnYpmKOCzV3rYnZ2dnUVZ_hynnZ2d@comcast.com>`
- **In-Reply-To:** `<snimt2tobutpn4fn2f7fiib7hhmi2mc5rj@4ax.com>`
- **References:** `<12tmh42rjop5627@corp.supernews.com> <snimt2tobutpn4fn2f7fiib7hhmi2mc5rj@4ax.com>`

```
Howard Brazee wrote:
> Larger modules are easier to work with.   A house built with modular
> rooms goes together faster than a house built with modular walls. And
…[5 more quoted lines elided]…
> the house.

You're right - but that's where the "inheritance" principle in OO comes 
in.  A "room" will have 4 or more "wall" object, who themselves may have 
"window" or "door" objects.  While the room may be quite specific, the 
lower-level components, such as doors or windows, are more generic. 
Just because the room isn't assembled at the job site doesn't mean that 
it didn't have to get assembled somewhere.  :)

And, your room analogy illustrates another advantage of OO design. 
Companies can combine low-level components into functional "larger 
modules", which themselves can become the lower-level components of an 
even larger module - for example, a house.

> Certainly objects are a type of module - with more power and utility
> than paragraphs and copy members.

The biggest problems we'd really started to run into was the global 
nature of COBOL variables.  Now yes, I know you don't have to do it that 
way, but most people don't even know about nested subprograms, and even 
fewer use them in their design and construction.  We had a terrible time 
with either left-over data, or data that was changed out from under the 
application program.

OO solves that dilemma by encapsulating the data with the code.  The 
more I use it, the more I like it.  :)  And now, when I look at doing 
something in COBOL, I find myself thinking in nested subprograms instead 
of paragraphs.

(not that any of this is new to you - your post just brought those 
thoughts to mind...)
```

#### ↳ Re: OO as a Form of Modular Programming

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-20T12:17:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172002661.074206.152600@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<12tmh42rjop5627@corp.supernews.com>`
- **References:** `<12tmh42rjop5627@corp.supernews.com>`

```
On Feb 20, 6:56 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> The above subject is discussed in Bertrand Meyer,
> "Object-Oriented Software Construction," Second
…[31 more quoted lines elided]…
> -----

sure...Modularity is a basic form of Fractal design.

We have OO types (classes, interfaces, Abstract Classes ,etc) which
are modules.
We Bundle certain instances of these types together to create
components (dataaccess layers, GUI libraries, etc) which are modules
We bundle these together to create applicants (Web Services, Web Apps,
Thick Clients etc) which are modules of Systems.
We link Systems together to create larger systems
  (Customer ordering web site
     -> Back office inventory management systems
      -> Warehouse inventory systems
       -> Robotic Pickers)

Its a fractal world after all.

Indeed, many OO Design Patterns consist of Fractals too (Model View
Control Uses the Listener aka Publish Subscribe pattern)

Andrew
```

##### ↳ ↳ Re: OO as a Form of Modular Programming

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-20T12:20:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172002802.950332.215210@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1172002661.074206.152600@a75g2000cwd.googlegroups.com>`
- **References:** `<12tmh42rjop5627@corp.supernews.com> <1172002661.074206.152600@a75g2000cwd.googlegroups.com>`

```
On Feb 20, 8:17 pm, "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote:
> On Feb 20, 6:56 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
>
…[56 more quoted lines elided]…
> Andrew

Its this fractal nature of things that causes some of the confusion,
we pick a word that describes somethign specific and others see the
same fractal pattern at a different level.  So they use it too, but
then people start to get confused as to the 'true' meaning of it,
instead of looking at the underlying principle of it.

My 2c

Andrew
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
