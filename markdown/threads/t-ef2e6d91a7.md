[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Why I am (core) dumping C++ for OOCOBOL

_4 messages · 4 participants · 1996-06_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Why I am (core) dumping C++ for OOCOBOL

- **From:** "glenn wardell" <ua-author-10447348@usenetarchives.gap>
- **Date:** 1996-06-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31C066B8.F5C@earthlink.net>`

```

I have three observations based on 11 years of programming experience
(please take with one grain of salt):

1. software written in C++ is unstable
2. C++ programmers are unstable
3. the language specification is unstable

--> 1. I spent my first five years programming in FORTRAN. I saw some
poor code, but nothing like what I've seen in C/C++. The
biggest problem with these languages is dynamic memory
allocation -- four of my five tasks in these languages have been
maintenance (or should I say exorcism) trying to track down
other peoples dangling pointers, free memory reads, etc.
Advocates of the language will point out that there are tools
to find these problems such as Purify, but in reality management
never allocates sufficient time to use these tools effectively,
and to be safe one must exercise every possible state the
program can be in -- nearly an impossible task. In addition, the
errors randomly appear in code "that always worked before" when
the load on the machine changes, a line of code in added to the
executable in a completely different subsystem, etc. COBOB97, as
far as I know, will not support dynamic memory as part of the
standard class library (???). My second complaint against C++ is
operator overloading. The poor maintenance programmer sees

myString = theirText;

In reality a cascade of six functions (copy constructors and cast
operators) get called. From what I've seen, in OOCOBOL when a
function is executed you see a function in the source code. The
last point in this tirade is that the cultural idioms of C++
encourage difficult to maintain code. People try to be "slick" and
compress the notation as much as possible, whereas COBOL is quite
verbose about what is going on. Who but a C/C++ expert would
understand

*i++?{ErrorMsg msg(myStruct->field)}:otherMsg::print();

---> 2. People who write C++ code typically come from an engineering, physics
or computer science backgrounds. They tend to be one-dimensional and
were never tought in school how to think adaptively or communicate.
My perception of COBOL programmers (???) is that they are from
business backgrounds and can be trained to understand the application
domain in which they are programming -- which leads to vastly higher
quality. My last observation is that C/C++ shops tend to have a
chaotic environment while the FORTRAN shops I was in (by extension
I am assuming COBOL) had much more focused process and greater
professionalism.

---> 3. "C++ has templates (parameterized classes) and OOCOBOL doesn't".
Most complilers gag on templates, giving non-portable results if
you can get them to work at all. Metaclasses are another "feature"
proposed for C++ that will cause more portability problems. The
"standard" libraries for C++ also have subtle differences between
compilers. Hopefully this will not be the case in OOCOBOL because
there are only a few major compiler writers who dominate that market.

In conclusion, a career in OOCOBOL looks more satisfying than one in C++.
If those of you from a COBOL background know of skeletons in its closet,
please let a newbie like me know.
```

#### ↳ Re: Why I am (core) dumping C++ for OOCOBOL

- **From:** "ggra..." <ua-author-12492810@usenetarchives.gap>
- **Date:** 1996-06-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ef2e6d91a7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31C066B8.F5C@earthlink.net>`
- **References:** `<31C066B8.F5C@earthlink.net>`

```

Glenn Wardell (pre··.@ear··k.net) wrote:
: I have three observations based on 11 years of programming experience
: (please take with one grain of salt):
:
: 1. software written in C++ is unstable
: 2. C++ programmers are unstable
: 3. the language specification is unstable
:
: --> 1. I spent my first five years programming in FORTRAN. I saw some
:...
: executable in a completely different subsystem, etc. COBOB97, as
: far as I know, will not support dynamic memory as part of the
: standard class library (???). My second complaint against C++ is
: operator overloading. The poor maintenance programmer sees
:
: myString = theirText;
:
: In reality a cascade of six functions (copy constructors and cast
: operators) get called. From what I've seen, in OOCOBOL when a
:...
: ---> 2. People who write C++ code typically come from an engineering, physics
: or computer science backgrounds. They tend to be one-dimensional and
: were never tought in school how to think adaptively or communicate.
:...
: In conclusion, a career in OOCOBOL looks more satisfying than one in C++.
: If those of you from a COBOL background know of skeletons in its closet,
: please let a newbie like me know.

Number 2 is a bit harsh ... clearly you've never worked with any 'old school'
COBOL programmers. The kind of folks who will not let you remove code that
has been commented out of a program for 15 years (literally), "cause we might
need it" (like it would run after 15 years of changes). Or people that use
to UPPER CASE all my SAS code "cause that's how it looks in COBOL". or ...
(I could go on and on and on but the point is that a language or a degree
does not make someone a good or bad programmer/thinker).

You might consider looking into the eiffel programming language you may find
it has the best features of both worlds.

I work under UNIX and use MF COBOL (for the moment) and I find COBOL 85/89
mostly frustrating and I expect OOCOBOL (COBOL 97) will be a truly grand
improvment. Unfortunately, MF (and many other companies) consider UNIX to
be a big pain in the a** and only put resources toward Win95 (as Gates
commands), leaving one guy to work on UNIX products (between sweeping the
floors, emptying the trash and cleaning the toilets).

In short it is at best an imperfect world

Best of Luck,
Greg

//
Greg Granger
ggr··.@na··o.net
```

#### ↳ Re: Why I am (core) dumping C++ for OOCOBOL

- **From:** "scott clark" <ua-author-2804742@usenetarchives.gap>
- **Date:** 1996-06-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ef2e6d91a7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<31C066B8.F5C@earthlink.net>`
- **References:** `<31C066B8.F5C@earthlink.net>`

```

In article: <31C··.@ear··k.net> Glenn Wardell
writes:
› 
› I have three observations based on 11 years of programming experience
…[4 more quoted lines elided]…
› 3.  the language specification is unstable
 
 
› [Snip]
 
 
› In conclusion, a career in OOCOBOL looks more satisfying than one in
› C++. If those of you from a COBOL background know of skeletons in its
› closet, please let a newbie like me know.  

It is nothing to do with the proposed standards for OO COBOL, but I know
someone who has worked for Micro Focus and he says that the INVOKE verb
in their compiler is slow as it requires 3 separate calls to the
run-time. It is 6 months since he worked there so this may have been
addressed now.

------------------------------------------------------------------------
S Clark
```

##### ↳ ↳ Re: Why I am (core) dumping C++ for OOCOBOL

- **From:** "paul grabinar" <ua-author-3257232@usenetarchives.gap>
- **Date:** 1996-06-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ef2e6d91a7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ef2e6d91a7-p3@usenetarchives.gap>`
- **References:** `<31C066B8.F5C@earthlink.net> <gap-ef2e6d91a7-p3@usenetarchives.gap>`

```


On 14 June 1996, Scott Clark wrote...
› It is nothing to do with the proposed standards for OO COBOL, but I know
 
› someone who has worked for Micro Focus and he says that the INVOKE verb 
› in their compiler is slow as it requires 3 separate calls to the 
› run-time.  It is 6 months since he worked there so this may have been 
› addressed now.                                                          

I don't know where he got his information from, but it was wrong. An
INVOKE has never resulted in 3 calls to the run-time, even worst case only
consists of a single call to the run-time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
