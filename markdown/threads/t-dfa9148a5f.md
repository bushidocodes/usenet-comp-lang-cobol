[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linus Torvalds on OO

_1 message · 1 participant · 2008-02_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Linus Torvalds on OO

- **From:** Clark Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-02-19T18:03:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1kmr39qkmk96k3kmh1ojgl6jbqusmjk2s@4ax.com>`

```
The following was posted on the IBM mainframe group regarding Linus
Torvald's comments on C++.  The posting itself was part of a thread on
whether parts of various IBM operating systems and IBM systems
programming services like TCPIP were written in either C or C++.  

I consider an operating system and the various utilities just a
peculiar application so these comments may have relevance in other
areas.  There also are interesting trade-offs in terms of systems
reliability versus system thruput in determining the types of linking
and the verification of data at boundaries.  

I am assuming that Thomas Berg who posted this has gotten the quotes
accurately.

 * * * * 
  Linus Torvalds on C++

 Some opinions by Linus Torvalds regarding C++ ( ;) ):

An interview 1998:

Many people ask why the kernel is written in C instead of C++. What is
your point against using C++ in the kernel? What is the language you
like best, excluding C?

    Linus: C++ would have allowed us to use certain compiler features
that I would have liked, and it was in fact used for a very short
timeperiod just before releasing Linux-1.0. It turned out to not be
very useful, and I don't think we'll ever end up trying that again,
for a few reasons. 

    One reason is that C++ simply is a lot more complicated, and the
compiler often does things behind the back of the programmer that
aren't at all obvious when looking at the code locally. Yes, you can
avoid features like virtual classes and avoid these things, but the
point is that C++ simply allows a lot that C doesn't allow, and that
can make finding the problems later harder. 

    Another reason was related to the above, namely compiler speed and
stability. Because C++ is a more complex language, it also has a
propensity for a lot more compiler bugs and compiles are usually
slower. This can be considered a compiler implementation issue, but
the basic complexity of C++ certainly is something that can be
objectively considered to be harmful for kernel development. 

An email reply 2007:
> 
> When I first looked at Git source code two things struck me as odd:
> 1. Pure C as opposed to C++. No idea why. Please don't talk about portability,
> it's BS.

*YOU* are full of bullshit.

C++ is a horrible language. It's made more horrible by the fact that a
lot 
of substandard programmers use it, to the point where it's much much 
easier to generate total and utter crap with it. Quite frankly, even
if 
the choice of C were to do *nothing* but keep the C++ programmers out,
that in itself would be a huge reason to use C.

In other words: the choice of C is the only sane choice. I know Miles 
Bader jokingly said "to piss you off", but it's actually true. I've
come 
to the conclusion that any programmer that would prefer the project to
be 
in C++ over C is likely a programmer that I really *would* prefer to
piss 
off, so that he doesn't come and screw up any project I'm involved
with.

C++ leads to really really bad design choices. You invariably start
using 
the "nice" library features of the language like STL and Boost and
other 
total and utter crap, that may "help" you program, but causes:

 - infinite amounts of pain when they don't work (and anybody who
tells me 
   that STL and especially Boost are stable and portable is just so
full 
   of BS that it's not even funny)

 - inefficient abstracted programming models where two years down the
road 
   you notice that some abstraction wasn't very efficient, but now all
your code depends on all the nice object models around it, and you 
   cannot fix it without rewriting your app.

In other words, the only way to do good, efficient, and system-level
and 
portable C++ ends up to limit yourself to all the things that are 
basically available in C. And limiting your project to C means that
people 
don't screw that up, and also means that you get a lot of programmers
that 
do actually understand low-level issues and don't screw things up with
any 
idiotic "object model" crap.

So I'm sorry, but for something like git, where efficiency was a
primary 
objective, the "advantages" of C++ is just a huge mistake. The fact
that 
we also piss off people who cannot see that is just a big additional 
advantage.

If you want a VCS that is written in C++, go play with Monotone.
Really. 
They use a "real database". They use "nice object-oriented libraries".
They use "nice C++ abstractions". And quite frankly, as a result of
all 
these design decisions that sound so appealing to some CS people, the
end 
result is a horrible and unmaintainable mess.

But I'm sure you'd like it more than git.

			Linus

 

> -----Ursprungligt meddelande-----
> Frï¿½n: IBM Mainframe Discussion List 
…[34 more quoted lines elided]…
> 
Search the archives at http://bama.ua.edu/archives/ibm-main.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
