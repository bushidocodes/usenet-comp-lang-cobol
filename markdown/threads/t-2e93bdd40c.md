[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# May I introduce myself to cobol?...

_65 messages · 12 participants · 2005-02_

---

### May I introduce myself to cobol?...

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-15T15:31:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com>`

```
Hello Everyone,

one handy feature with C++ language is that it allows the
programmer to Introduce a function (win32 API function, his own
function or some formula) for the requested arguments --- when
calling a win32 API, in an effort to save storage space and reduce
the number of declared variables in the program. That said, I know
that cobol is equally resourceful as C++, (if not exceeding,
business wise) I would like to know why cobol did not implemented
such feature in the ISO 2002 standard?, or why Micro Focus did not
include it as an extension to their cobol compiler?

thanks a lot for the comments. Kellie.

case in point source code:

*> C++ Window (1)
hMainWnd = CreateWindowEx(0, ClassName,
     TEXT("Main Window"),
     WS_OVERLAPPEDWINDOW,
     GetSystemMetrics(SM_CXSCREEN)/4,
     GetSystemMetrics(SM_CYSCREEN)/4,
     GetSystemMetrics(SM_CXSCREEN)/2,
     GetSystemMetrics(SM_CYSCREEN)/2,
     NULL, NULL, hInstance, NULL);

*> C++ Window (2)
hMainWnd = CreateWindowEx(0, ClassName,
    TEXT("Main Window"),
    WS_OVERLAPPEDWINDOW,
    (DesktopRect.right  - 340) / 2,
    (DesktopRect.bottom - 200) / 2,
    340, 200,
    NULL, NULL, hInstance, NULL);

*> Cobol window (3)
call WINAPI "CreateWindowExA" using
       by value     0 size 4
       by reference MyClass
       by reference MyHeading
       by value     hstyle
       by value     CW-USEDEFAULT
       by value     0 size 4
       by value     CW-USEDEFAULT
       by value     0 size 4
       by value     hParent
       by value     hMenu
       by value     hInst
       by value     0 size 4
    returning       hWindow
end-call.
```

#### ↳ Re: May I introduce myself to cobol?...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-16T00:40:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gEwQd.8133$ng6.3187@newssvr17.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com>`

```
"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1108510305.006428.237000@g14g2000cwa.googlegroups.com...
>
> one handy feature with C++ language [ and the BASIC language. MCM] is that
it allows the
> programmer to Introduce a function (win32 API function, his own
> function or some formula) for the requested arguments --- when
…[5 more quoted lines elided]…
> include it as an extension to their cobol compiler?

While I agree if would be nice to not have to go thru the COBOL coding steps
necessary replace a a function call with a dataname set up in
working-storage, such a construct does NOT save any storage space at all:
the compilers just use part of the stack to store a temporary variable, and
since you are already 'paying' for the stack space, it's free.

AFAIK, COBOL is not only stingy with functions, but has also been stingy
about allowing expressions; e.g.,

   MOVE WS-MULTIPLIER * WS-COUNTER TO  DEST-FIELD
   can't be done, instead you have to COMPUTE DEST-FIELD or MULTIPLY
WS-MULTIPLIER BY WS-COUNTER GIVING DEST-FIELD

Yup, COBOL can be a tad verbose. But look on the bright side: it works.

MCM
```

#### ↳ Re: May I introduce myself to cobol?...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-15T17:08:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108516103.905735.183550@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com>`

```
> one handy feature with C++ language is that it allows the
> programmer to Introduce a function (win32 API function, his
> own function or some formula) for the requested arguments

It is called overloading.  Several functions can have the same name
within one class, these are differentiated by the parameters supplied.
This is usually implemented using 'name mangling'.

It is most useful in doing operator overloading where an object may be
used in an expression as if it were a built-in type.

eg:

|    complex a, b, c, d;
|    a = new complex(1.0, 2.1);
|    b = new complex(1.0, 3.0);
|    c = a + b;
|    d = a + 1;

The two + operators would have quite different effects which would be
defined by two different operator methods.

The way that name mangling usually works is that the parameter types
are coded and added to the method name so that you actually wind up
with: complex.operator_plus_complex(complex self, complex a) and
complex.operator_plus_int(complex self, int i)

In other words the use of operator overloading is shorthand.

Cobol OO does not support the use of operator overloading or the use of
objects in expressions.  These things are C++'s solutions to C problems
that were never a problem in Cobol.

It is not a big deal to use unique method names for named functions
when developing a class.  Operator overloading would be impossible
without name mangling or some similar scheme and that this also works
for named functions is a bonus, but one that may cause confusion, it
may not always be obvious which particular function is being used as it
will depend on promotion.

> in an effort to save storage space and reduce
> the number of declared variables in the program.

Why do you think that is an objective or an outcome ? How are these
actually achieved ?
```

##### ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-15T21:01:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108526697.928623.234600@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1108516103.905735.183550@c13g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com>`

```
Well, declaring variables in cobol programs is a Major job, you need to
define the correct
type, the correct size, the correct location (working storage section,
local section and
linkage section), and you need to define all these variables with
descriptive names --- so
you can remember them when you are coding the main logic in the
procedure division.
most programs (Real World Applications) make a large number of calls to
the win32 AP's
system ---- so, if you can reduce the number of declared variables
(overloading functions),
it will make the program much smaller in size, and therefore will run
much faster, and
that should improve the performance of the application. Right?  Also,
if we can perform
two functions simultaneously (overloading) that should save CPU
execution time as well.
most C++ programmers claim that cobol have a major problem with
Prolixity, too Verbose
and very Wordy language --- so, why declare a storage in memory when we
can have the
win32 API function use a temporary location on the stack, while
executing that function?
this way, we can hit two birds with one stone, and silence our critics.
:--)  am I correct?
  
Regards, Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "Peter E.C Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-02-16T23:35:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108550126.3f8c2401c63e3e41d8d6106c1703b3f0@teranews>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com>`

```

"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1108526697.928623.234600@g14g2000cwa.googlegroups.com...
> Well, declaring variables in cobol programs is a Major job, you need to
> define the correct
…[24 more quoted lines elided]…
>
No Kellie, you are not strictly correct on this occasion. (But you are not
totally wrong either  :-))

Read Richard's explanation again. (I found it informative and interesting)

As to why you are not 'correct' consider this:

1.  Most application programs do NOT make a large number of calls to the
API. This is manipulated by another layer, often provided by a third party
supplier. By tying your program directly to the API (rather than to an
abstract layer) you are sentencing it to life with ONE operating system.
That's why we use multi-tier systems and multi-tier design. Separate the
business logic from the 'presentation' layer. How do you do that?... make
your application code communicate with a memory buffer that 'represents' a
window or screen display. This is an interface to the presntation layer.

2. Your observations about defining data in COBOL are right on the button;
it IS tedious... BUT it takes no more space at run time than any other
method in any other language. I think you may be confusing source code and
runtime object code here.
Do not incorrectly assume that because data is pushed on the stack it does
not occupy space in memory. Where do you think the stack is? :-)

3. Making a program smaller in size (by overloading functions, or any other
way, short of removing code that it currently executes) does NOT guarantee
that it will run faster. It will load faster (although the difference would
be impossible for a human to detect). The time it takes to run will be
determined by the execution path (the capture time), not by the size of it.
(I covered this in an article about components some time ago; here's a link:
http://www.aboutlegacycoding.com/archives/v3/v30201.asp

4.Overloading a function does not necessarily allow it to execute
simultaneously with another instance of itself. This will be determined by
threading models and instantiation, not by overloading.

Hope this helps.

Pete.







> Regards, Kellie.
>
>
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-16T08:14:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1116las5aadl881@news.supernews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com>`

```
Kellie Fitton wrote:
> Well, declaring variables in cobol programs is a Major job, you need
> to define the correct
…[25 more quoted lines elided]…
> Regards, Kellie.

Observations:

1. I dispute "most real world applications" make direct API calls. 
Specifically, API calls are not usually part of the COBOL programmer's tool 
kit. COBOL programmers avoid them for several reasons: 1) They're not needed 
for the kinds of problems attacked by COBOL programming, 2) They are not 
portable, 3) They are difficult - sometimes impossible - to use.

2. Your definition of the "problem" - smaller size and improved 
performance - is simply not a problem worthy of study to most COBOL 
programmers, especially at the micro level.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-16T14:59:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:1116las5aadl881@news.supernews.com...
> Observations:
>....
>  3) [Direct Windows' API calls ] are difficult - sometimes impossible - to
use.

Thou, sir, speaketh but for thyself. Calling the Windows API is no different
from calling any other external support library.


MCM
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 5)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T08:38:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108571889.932695.188110@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com>`

```
Hello,
every program exist today, whether it is written with C++, Delphi,
Visual Basic,
perl, MFC, Java++ or any other wacked out language or framework you can
think of,
is eventually built UPON the win32 API functions. In many cases this
interaction is
totally hidden, so you don't deal directly with the win32 API's, the
runtime system
and the support libraries simply do it for you automatically "Behinde
Close Doors".
the Third-Party Layer or whatever interface you are using, can only do
what the
win32 API's can do, because it's built on top of it. Regards.

Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 6)_

- **From:** Adrien Plisson <aplisson-news@stochastique.net>
- **Date:** 2005-02-16T18:16:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42138008$0$20893$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<1108571889.932695.188110@o13g2000cwo.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com>`

```
Kellie Fitton wrote:
> Hello,
> every program exist today, whether it is written with C++, Delphi,
…[3 more quoted lines elided]…
> is eventually built UPON the win32 API functions. 

with the one and only precondition that you are running on a win32 
based system. some program (most of them in fact) are written in a way 
which allows them to perform the exact same things on other systems.

have you ever touched a computer running something else as an OS than 
windows ? do you know that all the computer in the world are not IBM 
PC compatible ?

now think of the way you can make a software run on different OSes. 
then you would understand the point raised in this thread about API 
calls, and you may eventually understand why you are wrong with the 
statement quoted on top.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 7)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T10:20:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108578002.119643.205360@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<42138008$0$20893$ba620e4c@news.skynet.be>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be>`

```
Hi Rien,
first of all, a clarification on what the win32 API
functions are. The win32 API's is a generic term
meaning "Application Programming Interface",
However, in the context of the OS Windows
programming, it means specifically the Windows
API's, which is the Lowest-Level of Interaction
between an applications and the existing
Operating System. Drivers of course have even
lower-levels code, and maybe different sets of
function calls to work with, but for the majority of
windows development, this is not a problem at
all. That said, if a business application is
running on a different OS other than windows,
then these programs are using some low-level
system library supports (Assembly api or
C++ api), which is the same thing as the win32
API's --- except it is coded for a different
environment, with different names and maybe
different entry-points. After all, why would you
re-invent the cobol wheel?  Regards.

Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T11:07:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108580825.524713.21820@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1108578002.119643.205360@l41g2000cwc.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com>`

```
> first of all, a clarification on what the win32 API functions are.

Most Cobol applications do not access the 'OS API' directly at all, or
at least only make limited access to it. Even when they are GUI
programs they would use an interface library such as SP/2 or Dialog or
WoW or PowerCobol or the AcuCobol built in features.  C++ programs are
more likely to use MFC or some higher level class library.

While these may have underlying access to the OS API this dilutes your
point that you can save a few bytes of memory by avoiding having
explicit variables in the API call.

I have, starting in 1990, wriiten Cobol systems that made extensive use
of the Windows API including entirely graphical drawings such as
graphs, plans and perspective views.  I would not recommend this path
and would suggest that you use something that hides all the grubby
details that need to be dealt with.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 9)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T13:06:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108586099.180816.104300@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1108580825.524713.21820@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com>`

```
Hi Richard,
my point is NOT "overloading" -- I would like to
introduce expressions as call parameters or
rather arguments, and reduce the number of
declared variables in my program, especially
when the returned value from the call is not
needed, after the function call is done
(temporary variables).

if the programming language is trying to avoid
weaknesses or limitations by disallowing C++
constructs, so it would NOT burden the cobol
programmer, then at what expense? It would be
at the expense of "Loss-Of-Flexiability" and
having to decalre more variables in the program
unnecessarily.

personally, I think Cobol language have the
power, knowledge and more than 40 years of
real-world experience, to circumvent all the
problems and the limitations, of the way that C
or C++ uses expressions in function calls.

in fact, Cobol have the power to improve,
enhance and modernize the methods of using
expressions, and function-overloading when
calling the win32 API's. after all, the Cobol word
stands for "Cobol Objects Bulldozerize Other
Languages". :-)) :-))

regards, Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T13:39:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108589970.105316.216170@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1108586099.180816.104300@c13g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com>`

```
> I think Cobol language have the power, knowledge and more
> than 40 years of real-world experience, to circumvent all the
> problems and the limitations, of the way that C or C++ uses
> expressions in function calls.

Please explain how Cobol could 'circumvent all the problems and the
limitations' while actually using expressions that include CALL ...
RETURNING ...

The way forward is actually to bury the rather arcane API calls into a
higher level library, such as you could write yourself in OO Cobol,
that does this grubby stuff behind the scenes in a reusable way, rather
than you recoding it into every program you write.

Then the 'major job' is done just once to be accessed from any program
that requires it.  Also it is alleged that when MS finally gets
Longwait out it will have a different API known as Avalon. It will be
much easier to change over if it is all localised rather than being
dispersed through all your programs.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 11)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-16T18:23:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LBQQd.7575$dZ.468027@news20.bellglobal.com>`
- **In-Reply-To:** `<1108589970.105316.216170@f14g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com>`

```
Richard wrote:
>>I think Cobol language have the power, knowledge and more
>>than 40 years of real-world experience, to circumvent all the
…[18 more quoted lines elided]…
> 

I agree.  It also makes the porting of a system far easier, as the 
system dependent things all reside in a single library. One could have, 
for example, one library for Linux, and another for Windows. Placing 
them inline results in a far more difficult re-write for each platform.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-16T23:53:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02RQd.2140607$B07.327281@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1108589970.105316.216170@f14g2000cwb.googlegroups.com...
>> I think Cobol language have the power, knowledge and more
>> than 40 years of real-world experience, to circumvent all the
…[6 more quoted lines elided]…
>
See my separate note on the support in both Micro Focus and the ISO 2002 
Standard for arithmetic expressions in BY CONTENT and BY VALUE phrases - when 
CALL prototypes are used.

"Obviously" these cannot be used in the RETURNING or BY REFERENCE phrases.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T16:50:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108601453.237798.21350@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<02RQd.2140607$B07.327281@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com> <02RQd.2140607$B07.327281@news.easynews.com>`

```
> arithmetic expressions in BY CONTENT and BY VALUE phrases

Of course, and these expressions could contain intrinsic functions and
user functions, but can they include arbitrary callable programs or
library routines.

In the particular case the routine is used as:

         CALL WINAPI "GetSystemMetrics"
                   USING BY VALUE SM_CXSCREEN size 4
                   REURNING Screen-X

Can the expression include some form of this as:

         CALL .....
                  USING by value ( GetSystemMetrics(SM_CXSCREEN) / 4 )
                  ....
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-17T01:21:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VkSQd.2429149$f47.427652@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com> <02RQd.2140607$B07.327281@news.easynews.com> <1108601453.237798.21350@z14g2000cwz.googlegroups.com>`

```
You betcha <G>

If the "routine" is reached

 A) by an inline invocation (in the case of a "method")
 B) by a user defined intrinsic function (as an "intermediate" level for a 
subprogram)

Both of these can be used wherever a "sending" data item can be used (including 
a CALL or INVOKE statement - BY CONTENT or BY VALUE)
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 14)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T17:32:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108603972.414741.260550@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<VkSQd.2429149$f47.427652@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com> <02RQd.2140607$B07.327281@news.easynews.com> <1108601453.237798.21350@z14g2000cwz.googlegroups.com> <VkSQd.2429149$f47.427652@news.easynews.com>`

```
>> Of course, and these expressions could contain intrinsic functions
and
>> user functions, but can they include arbitrary callable programs or
>> library routines.
…[10 more quoted lines elided]…
>>                  USING by value ( GetSystemMetrics(SM_CXSCREEN) / 4
)
>>                  ....

> If the "routine" is reached
> A) by an inline invocation (in the case of a "method")
> B) by a user defined intrinsic function (as an "intermediate" level
for a
> subprogram)

So the actual answer is NO, but you can write a wrapper (OO method or
User function) for it that can be used in an expression, as I had
already said.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-17T01:56:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jRSQd.2432375$f47.428205@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com> <02RQd.2140607$B07.327281@news.easynews.com> <1108601453.237798.21350@z14g2000cwz.googlegroups.com> <VkSQd.2429149$f47.427652@news.easynews.com> <1108603972.414741.260550@g14g2000cwa.googlegroups.com>`

```
For an OO method, you don't need to create a wrapper - but yes, you do need to 
for a subprogram.

Looking at the web for Java, Win32, and API - it looks like there are (already) 
Java "wrappers" for many (not all) Win32 API's.  Depending upon the OO COBOL 
used, some of these may be "directly" available to general OO COBOL programs. 
If not, then yes "you" (or someone) would need to create "wrappers" to use 
inline invocations as CALL parameters.

All of this sounds as if there *might* be a business case for someone to create 
(and market) either a CLASS-LIBRARY or set of "user-defined functions" for 
accessing all (or many/most) of the Win32 API's.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 16)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T02:28:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%iTQd.410665$8l.86221@pd7tw1no>`
- **In-Reply-To:** `<jRSQd.2432375$f47.428205@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <1108589970.105316.216170@f14g2000cwb.googlegroups.com> <02RQd.2140607$B07.327281@news.easynews.com> <1108601453.237798.21350@z14g2000cwz.googlegroups.com> <VkSQd.2429149$f47.427652@news.easynews.com> <1108603972.414741.260550@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com>`

```
William M. Klein wrote:
> For an OO method, you don't need to create a wrapper - but yes, you do need to 
> for a subprogram.
…[10 more quoted lines elided]…
> 

But where is the PORTABILITY - can I truly use general 'API' code from 
FJ with MF - and vice versa ? What about Acu, HP, Liant, Realia etc.....

Yeah, but by the time it's done, as Richard pointed out, Microsloth with 
'Longwait' using Avalon will have screwed the author !

Richard is not the first I've seen write to warn about the threat of 
Longhorn. I hope vendors and developers scream blue murder if MS makes 
the new APIs/GUIs incompatible with what has gone before.

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 17)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-17T10:46:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no>`

```
.    On  17.02.05
  wrote  jgavandeletethis@shaw.ca (James J. Gavan)
     on  /COMP/LANG/COBOL
     in  %iTQd.410665$8l.86221@pd7tw1no
  about  Re: May I introduce myself to cobol?...


JJG> Richard is not the first I've seen write to warn about the threat of
JJG> Longhorn. I hope vendors and developers scream blue murder if MS
JJG> makes the new APIs/GUIs incompatible with what has gone before.

   If that is really the case, the transition to, say, Linux would not  
be so difficult anymore.

   Because of that, I presume, Microsoft will introduce a lot of  
backwards compatibility.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Gerade das Gegenteil tun heiï¿½t auch nachahmen, es heiï¿½t nï¿½mlich das Gegenteil nachahmen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 18)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-17T09:49:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108662546.460545.159270@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de>`

```
> Because of that, I presume, Microsoft will introduce a lot of
> backwards compatibility.

MS purchased Virtual PC which is used to run several operating systems
one one machine at the same time.  Some thought it was stop it being
able to run Windows and Linux together.  It may be so that a copy of XP
can run alongside Longhorn for the 'legacy applications' (ie anything
current).

Of course that means buying _two_ operating systems plus Virtual PC
next time around.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 18)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T19:05:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bW5Rd.414360$Xk.216137@pd7tw3no>`
- **In-Reply-To:** `<9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  17.02.05
>   wrote  jgavandeletethis@shaw.ca (James J. Gavan)
…[13 more quoted lines elided]…
> backwards compatibility.

MS must surely be aware of this - so they must ensure backwards 
compatibility.

I have no knowledge of either Unix or Linux although I did develop an 
RM/COBOL app a couple of decades ago which used the then MS Xenix - but 
I used the 'bare bones' to get my COBOL up and running.

Couple of years back, Corel, based in Eastern Canada, did intend to 
introduce a user-friendly GUI front-end for Linux. The CEO got fired and 
that project was put on hold or dumped. For Linux to 'grow' I think 
somebody has to come up with a universal GUI package. I recently got the 
following reply from somebody at Micro Focus. I wouldn't mind betting he 
is one of Bill's 'reliable sources' :-) :-
------------------------------------------------------------------------

ME : "So as I'm not aware of Unix - can you just quickly clarify. Is 
Unix a Character Based environment ONLY, as opposed to Linux which I
understand  has the equivalent of its own "GUI" features ????

REPLY : " - This is not quite correct.  UNIX and Linux systems are, 
basically, character mode systems, by default.  There have been several 
attempts to put GUI interfaces on UNIX/Linux systems, but none have yet 
taken off completely.  This includes the older X-Windows and the newer 
GUI interface on Linux (which include a Windows look-alike as well as 
others).  The problem with the UNIX/Linux world is that there are no 
standards and everyone does their own thing, especially when it comes to 
graphical interfaces.  For example, in addition Sun and HP both had 
their own graphical interface you could use, which was loosely based on 
X-Windows, but were not compatible with each other.

- Even in the Linux world, there is no standard, so even though a lot of 
the stuff works off of the same free code base, everyone (vendor wise) 
modifies things to match their own needs, which introduces differences 
and some lack of commonality.  So, for the UNIX world, it seems that 
most people either stick with the base character mode terminal 
operations or uses a Web based interface, as those two pretty much work 
across the board on all UNIX/Linux systems the same.  (Note, because of 
the above, we don't even offer our Dialog System on UNIX platforms.  We 
used to offer an older character based Dialog System, but I think we 
even dropped that several years ago.)..."
------------------------------------------------------------------------

A few years back M/F did have a Linux COBOL compiler - $4,000 CDN as I 
recall. You can guesstimate how many people bought it. From memory it 
didn't do any GUI-ing. I *think* at the time it was offered it directed 
your attention to a particular Linux GUI package.

Interesting thing about Dialog System (as opposed to Dialog Editor and 
GUI classes, which I'm using) -  M/F are seeking beta users for a dotNet 
version of Dialog System.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 19)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-17T12:12:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108671162.044943.120820@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<bW5Rd.414360$Xk.216137@pd7tw3no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no>`

```
> Couple of years back, Corel, based in Eastern Canada, did intend to
> introduce a user-friendly GUI front-end for Linux. The CEO got fired
and
> that project was put on hold or dumped.

That's not quite true.  First of all it was 1999, and it was released.
I have a copy here including WordPerfect 8 for Linux.  The main issue
way back then was installing.  6 years ago installers were a pain and
required arcane knowledge of the system.  Corel uses KDE as its GUI.

These days with most distros you just put the CD in and it installs.
When I put Mandrake on my laptop a month or two ago it correctly
resized the Windows XP partitions to give itself some disk space and
installed sucessfully finding and using all the hardware.

Basically Corel was running out of money because its markets had dried
up and it was looking for new markets such as Linux for its WordPerfect
products.  MS gave it some money to stop it doing that.

> GUI interfaces on UNIX/Linux systems, but none have yet taken off
completely.

All Unix/Linux can run X which is enough to get a GUI, even remotely or
on several screens.  To that a Window Manager can be added which may be
a simple, streamlined one or something with much more facilities. There
were several for Unix such as CDE which was standard on UnixWare and
OpenServer more than a decade ago.  Most Linux use Gnome or KDE, or
both.  While these do compete (Redhat prefers Gnome and Mandrake
prefers KDE) there is no real issue as programs run on either.  It is
called _choice_, something that Windows users get little of.

> The problem with the UNIX/Linux world is that there are no
> standards and everyone does their own thing

Yes, there are standards.  LSB for example ensures that programs can
rely on finding stuff in the correct places.  There is choice, you can
choose to use Qt or GTK or wxWindows or Glade or Tk or any number of
windowing toolkits and they will all work whether it is Gnome or KDE or
BlackBox on the desktop.

> A few years back M/F did have a Linux COBOL compiler - $4,000 CDN

They still do, and it requires per user run-time licences.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 20)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T20:43:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tl7Rd.414639$Xk.79951@pd7tw3no>`
- **In-Reply-To:** `<1108671162.044943.120820@z14g2000cwz.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com>`

```
Richard wrote:
> 
> These days with most distros you just put the CD in and it installs.
> When I put Mandrake on my laptop a month or two ago it correctly
> resized the Windows XP partitions to give itself some disk space and
> installed sucessfully finding and using all the hardware.

Interesting - Mandrake does the disk partioning without removing any of 
the Windows stuff ? Or are there some BUTs....... ?

Not quite clear - are you using any COBOL compiler with Linux ?

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 21)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-17T12:57:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108673861.975845.28700@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<tl7Rd.414639$Xk.79951@pd7tw3no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no>`

```
> Interesting - Mandrake does the disk partioning without removing any
of
> the Windows stuff ? Or are there some BUTs....... ?

It just resized the Windows partitions without damaging them, installed
itself and set up the dual boot.  I can boot to XP if I ever wanted to.
 Mandrake also mounts the Windows partions so I can access all the
files there, or just use the disk space to make the stuff available
under both OSes.

> Not quite clear - are you using any COBOL compiler with Linux ?

I do have Fujitsu for Linux.  I got it at the special introductory
price so it wasn't too painful.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 22)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-17T16:39:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W98Rd.21926$4I5.1034736@news20.bellglobal.com>`
- **In-Reply-To:** `<1108673861.975845.28700@f14g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <1108673861.975845.28700@f14g2000cwb.googlegroups.com>`

```
Richard wrote:
>>Interesting - Mandrake does the disk partioning without removing any
> 
…[17 more quoted lines elided]…
> 

Anyone know a current price?

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 23)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-02-17T20:42:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fla119rg14d3oue2jkufqo0nhhab5jouv@4ax.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <1108673861.975845.28700@f14g2000cwb.googlegroups.com> <W98Rd.21926$4I5.1034736@news20.bellglobal.com>`

```
On Thu, 17 Feb 2005 16:39:02 -0500, Donald Tees
<donald_tees@sympatico.ca> wrote:

>Richard wrote:

>> I do have Fujitsu for Linux.  I got it at the special introductory
>> price so it wasn't too painful.
>> 
>
>Anyone know a current price?

$2,500 USD.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 21)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-17T16:38:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g98Rd.21915$4I5.1034433@news20.bellglobal.com>`
- **In-Reply-To:** `<tl7Rd.414639$Xk.79951@pd7tw3no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no>`

```
James J. Gavan wrote:
> Richard wrote:
> 
…[12 more quoted lines elided]…
> Jimmy

The version I am using did it all, including the installation of a dual 
boot so that I can boot either system. The Linux machine sees everything 
... windows and linux drives, and can read both no problem.  The windows 
boot sees only the windows drive, and sees Linux as a foreign partition.

It did make the default boot (press reset and walk away) linux, but I 
can change that using a fairly simple utility.

If you want to play with it, you can install it on any windows machine 
with 7-8 gigs free (thats loaded, you could get by with 1/4 that) and 
the only noticable difference on the windows machine is that some of 
your disk gets used up.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 22)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-17T14:35:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108679701.969313.81390@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<g98Rd.21915$4I5.1034433@news20.bellglobal.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com>`

```
> If you want to play with it, you can install it on any windows
machine
with 7-8 gigs free

Or you can try a Knoppix, Mandrake Move or similar CD where it boots
and runs off the CD.  If you plug in a USB memory drive you can save to
that and then run on any machine that is handy.

Or you can load CoLinux which installs and runs _within_ a Windows
system so the Linux is just windows alongside Windows.  This is the
reverse of Win4Lin which runs a Windows OS as a window on a Linux
desktop.

> (thats loaded, you could get by with 1/4 that)

I have linux systems so small they boot and run off a floppy, no hard
drive, no CD.

> The windows boot sees only the windows drive, and sees Linux as a
foreign partition.

When MS releases its Malicious Sotware Removal Program it will
maliciously remove ..
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 22)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T23:02:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0o9Rd.415595$Xk.144442@pd7tw3no>`
- **In-Reply-To:** `<g98Rd.21915$4I5.1034433@news20.bellglobal.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com>`

```
Donald Tees wrote:
> 
> The version I am using did it all, including the installation of a dual 
…[11 more quoted lines elided]…
> 
Thanks Richard and Donald for clarification. Nice to know that something 
can be done without hitting headaches !

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 23)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-17T22:42:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xudRd.24467$4I5.1123666@news20.bellglobal.com>`
- **In-Reply-To:** `<0o9Rd.415595$Xk.144442@pd7tw3no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no>`

```
James J. Gavan wrote:
> Donald Tees wrote:
> 
…[18 more quoted lines elided]…
> Jimmy


Well, I'm not sure I'd go that far<G>. I've found Linux a horrendous 
learning curve, and have had all sort of problems, and spent hours on 
them.  For example, I have yet to get my DVD burner working under Linux.

However one thing it has done flawlessly, and right from the begining 
with remarkably few problems, is serve as a secure web client and a 
secure server. I tossed all the virus checkers, etc., and just do my web 
stuff from Linux.  I can play with client/server stuff inhouse, and 
leave my machines on/online 24/7 without worrying about security.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 24)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-18T05:43:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YffRd.417302$8l.99004@pd7tw1no>`
- **In-Reply-To:** `<xudRd.24467$4I5.1123666@news20.bellglobal.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com>`

```
Donald Tees wrote:
> James J. Gavan wrote:
> 
…[18 more quoted lines elided]…
> Donald

What I was really meaning was that the actual install went without a 
cock-up :-). (Shudder, shudder if it corrupted your existing Windows setup).

Thinking back to the old MS Xenix - I wasn't thrilled with its cryptic 
"command lines" - so I appreciate what you are saying about implementing 
actual features.

That's where the Corel GUI friendly front end was 'supposed' to be the 
white saviour. I know that Richard doesn't care much for IDEs, and I 
don't think you have an abundance of enthusiasm either - but that sort 
of approach gets around the damned 'cryptics'. Xenix remember was around 
1980 - doesn't seem we have moved too far since then in getting around 
the Human Interface problem.

If you reflect on it, not much that's ambiguous with Windows - XP has 
added features compared to Win 98. You discover them when you perform 
certain operations, e.g.  if I click on an icon and select 'Preview' 
from the dropdown menu, I don't automatically get the ImageEditor; first 
it gives me the 'new', (well 'new' to me, anyway), Windows Picture and 
Fax Viewer instead of the old Win 98 jumping straight into ImageEditor).

To compete against Windows it has to be friendly or even more friendly. 
Haven't used it yet, but Windows-wise I've got a CD and have added the 
help file for burning CDs - dumb maybe, but I'm not anticipating any 
problems.

That lack of friendliness could possibly be why Linux hasn't caught on 
commercially. Sure programmers using it like it, but end-users who want 
things KISS fashion ? I *know* Linux is used in Calgary, but I could 
probably put money on it that end-users in the oil patch just don't want 
to touch it - unless they can view something with an easy front-end.

As a 'rocket scientist' - I need all the friendly help I can get !

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 25)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-17T23:17:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108711076.997321.72210@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<YffRd.417302$8l.99004@pd7tw1no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no>`

```
> old MS Xenix - I wasn't thrilled with its cryptic "command lines"

MS Xenix predated MS-DOS.

> That's where the Corel GUI friendly front end was 'supposed' to be
the
> white saviour.

The Corel GUI was just KDE with some Corel enhancements.  KDE, which is
the standard GUI for many distros, probably incorporated those, it
certainly has moved forward in the intervening 5 years.

You seem to have the rather odd notion that Linux is like Xenix of 25
years ago and Corel was the only distro to have a GUI.  KDE may have
been rather new in 1999, but it has been in most distros since around
that time, along with Gnome if that is preferred.

> Richard doesn't care much for IDEs

I've not found one that I liked.  IDEs seem to have been developed to
overcome the limitations of having a single-tasking system (MS-DOS) or
where it was too difficult to have different tasks doing appropriate
things.  I never had thaose problems so never needed to solve them with
an IDE, I could build a toolset that suited me, not one that suited
someone else.

I also find that IDEs work 'upside down' compared to how I prefer to
work.  I use midnight commander, usually several copies, with some
added menu items and the editor of my choice and make to do the builds
in background.

But you can use Eclipse or KDevelop (part of KDE) or Idle or any number
of graphic IDEs if you wish.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 25)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-18T10:43:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RWoRd.853$K72.219@fe40.usenetserver.com>`
- **In-Reply-To:** `<YffRd.417302$8l.99004@pd7tw1no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no>`

```
James J. Gavan wrote:
> 
> That lack of friendliness could possibly be why Linux hasn't caught on 
…[3 more quoted lines elided]…
> to touch it - unless they can view something with an easy front-end.

Almost any application a non-techie person would want to use has a GUI 
that works on Linux.

Micros~1 Outlook Express -> Thunderbird
Micros~1 Internet Exploder -> Firefox
Micros~1 Office -> OpenOffice.org
Roxio Easy CD Creator -> K3B
WinAmp -> XMMS
Windows Media Player/assorted DVD players -> xine

The major difference is the built-in security (root vs. a user account) 
and the different filesystem (FHS) Linux uses.  Nothing a 20-minute 
automated tutorial couldn't fix.

I'm actually looking at setting up something like this as a service - 
bring me your computer, I'll configure it, and you get it back.  From an 
administration standpoint, I think there are tools that will automate that.

I can see it now - the Linux Standard Desktop.  (Hmm... maybe that 
acronym needs a little work...)
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 26)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-18T18:10:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cqRd.423392$6l.238575@pd7tw2no>`
- **In-Reply-To:** `<RWoRd.853$K72.219@fe40.usenetserver.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no> <RWoRd.853$K72.219@fe40.usenetserver.com>`

```
LX-i wrote:
> James J. Gavan wrote:
> 
…[18 more quoted lines elided]…
> 

Daniel,

Fine. But the current strength with Windows is that right from start-up 
you have a common display with a common 'look and feel' which keeps 
non-techies in a 'comfort zone'. Subserviently, if you like, as 
developers we follow the same rules so that end-users aren't having to 
learn something new. Although any application does require an intro 
period. To put it bluntly, end-users don't want to piss around - see below.

Bubbling with oil and gas, Calgary downtown is rich and aggressive. Even 
got mention last night on the Daily Show with John Stewart - 'the 
Athabasca Oil Sands', way north of me - the reserves are greater than 
Saudi Arabia. They are currently thinking of a new pipeline across 
country down to just south of Chicago. Without a blink of the eye 
engineers can envision in grand style; pipe gas down from the Arctic and 
use it to heat the tar sands to extract oil, which is then piped south. 
They will spend billions in the process. As engineers they have no 
problems with the concept, it fits in with their technical expertise. 
Now to same engineers, enhance something doing it on a computer - ahhhh....

Some 25 years back when possibly COBOL still reigned as king/queen here 
on mainframes, it was a bloody tough sell for vendors to make a mark 
with minis and then the 'PC' family. Wang back then had a pretty decent 
dedicated w/p system. Even that was a tough sell. Sellers tried to 
persuade lawyers as a group to switch to w/p (Wang and eventually PCs). 
Real tough - and took several years. First one, then another, then 
another bought into the idea - then ALL the lawyers followed like 
lemmings switching to automated w/p.

Same sort of problem with minis/PCs v mainframe - "How can you possibly 
do all that number crunching on those 'toys'". Well eventually the oil 
patch bought into the idea when inter-active screen displays started to 
become the norm. Side-by-side, there were PC packages for specialized 
areas - e.g. like a geologist on site wanting to get a graphical view of
of test drillings on a laptop.

Now I do know Linux is used in Calgary. It was mentioned in the local 
paper about three/four years ago, but how far it has cut into the 
Windows game I have no idea. Knowing that 'cautious' approach to 
computer technology that exists, I suspect it would still be a very hard 
sell to say get a major oil company to switch. As both you and Richard 
point out - several ways of going at GUIs with Linux. Now put yourself 
in the shoes of 'Cautious Johnny' the engineer where you are giving him 
a demo. "What do you mean ? Use this GUI tool, use that GUI tool. Why 
not just one desktop like Windows ?"
> 
> I can see it now - the Linux Standard Desktop.  (Hmm... maybe that 
> acronym needs a little work...)
> 
Now you have hit the nail on the head - 'The Linux Standard Desktop'. 
Come on Linus T., as the originator, this is perhaps where you should 
put your two cents in.

The long-term success of Linux will depend upon acceptance from end-usrs 
not us intermediary techies.

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 27)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-18T11:20:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108754440.426485.108140@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<9cqRd.423392$6l.238575@pd7tw2no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no> <RWoRd.853$K72.219@fe40.usenetserver.com> <9cqRd.423392$6l.238575@pd7tw2no>`

```
> But the current strength with Windows is that right from start-up
> you have a common display with a common 'look and feel' which keeps
> non-techies in a 'comfort zone'.

Actually the 'common' look and feel keeps changing with Windows.  I
find that XP has changed all the 'look and feel', all the icons are
different, all the dialogs are changed, all the colours, I don't
recognise anything.  Of course I could try 'classic' but that is not
the same as XP and thus is a different 'look and feel'.

And this has happened with every version 3.11 -> 95 -> 98 'channels'
(or what were they called) -> 2000 -> XP. and Avalon is completely
different again.

> we follow the same rules so that end-users aren't having to learn
something new.

Yet each version of Office shuffles the menus so that the user can't
find what they used before.

> Come on Linus T., as the originator, this is perhaps where you should
put your two cents in.

Linus does the kernel.  There are many others that do other aspects.

> will depend upon acceptance from end-usrs

In several places I have put in Linux desktops and users just use them
without complaint, without whining that 'Windows has an extra pixel
here'.  I guess some people do get confused and can't cope if one
desktop icon goes missing, just as some drivers couldn't drive a
different car if the light switch was in the 'wrong' place.

> The long-term success of Linux

Linux already has a long term success.  It has been the OS of choice
for the majority of the Web Servers for many years, it is the OS of
choice for super computer clusters and for many servers.  It has a much
larger desktop usage than Apple (which is also now Unix based).

The 'free' in Linux is freedom of choice.  No one is going to force you
to pay for Linux, or even have it installed, when you buy a new
computer (1), no one makes you use it or change to 'the new way'. It is
about _choice_.  If you choose Windows then that is OK, no one in
Linux-world will mind (2).


(1) actually this may happen. Microsoft contractually forces
manufacturers to install an OS before they ship.  Due to anti-trust
regulations they can only partially force this to be Windows so
manufacturers may not be able to offer an empty machine for the user to
make a choice and may need to ship it with Linux or FreeDOS to meet
MS's contract.

(2) they will mind if you choose Windows and then become 'pwned' and
spew out spam email by being a zombie-bot as many Windows machines seem
to be, unknown to their owners. The current estimate is that 60% of all
spam is from networks of these machines. Make sure you are not one of
them.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 27)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-18T14:16:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n2sRd.870$K72.826@fe40.usenetserver.com>`
- **In-Reply-To:** `<9cqRd.423392$6l.238575@pd7tw2no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no> <RWoRd.853$K72.219@fe40.usenetserver.com> <9cqRd.423392$6l.238575@pd7tw2no>`

```
James J. Gavan wrote:
> LX-i wrote:
> 
…[27 more quoted lines elided]…
> non-techies in a 'comfort zone'.

Many of these applications' interfaces are not as different as you 
think.  My sister just recently started using Thunderbird as her mail 
reader, and her first comment, when it came up, was "Oh - is this like 
Outlook?"  :)  (Of course, this was with Windows...)

And, the word "common" you used there could have more than one 
interpretation.  If by common you mean that it looks like a lot of other 
PC's, then I grant you your point there.  If you mean that the 
applications on the platform behave similarly, then I'd differ a bit. 
Linux apps almost all have File -> Open/Save/Save As.../Close/etc, Edit 
-> Cut/Copy/Paste/Select All/Find/etc, Help -> About, and the like.  The 
biggest difference is that the main program configuration is in 
Edit->Preferences, instead of Tools->Options - but, this is common 
throughout Linux.

(As an aside, T-bird and Firefox for Windows have their configuration at 
Tools->Options, but under Linux, it's Edit->Preferences.)

> Now I do know Linux is used in Calgary. It was mentioned in the local 
> paper about three/four years ago, but how far it has cut into the 
…[6 more quoted lines elided]…
> not just one desktop like Windows ?"

Well, there are defaults, based on your distribution.  You don't have to 
exercise any of the options if you don't want to.  But, there are 
options.  :)

>> I can see it now - the Linux Standard Desktop.  (Hmm... maybe that 
>> acronym needs a little work...)
…[3 more quoted lines elided]…
> put your two cents in.

I don't think you're going to get Linus to pick a standard default 
desktop.  In fact, the whole appeal of different distributions is that 
they picked what they think are the best applications, and those are the 
defaults.  Red Hat (and its derivatives) uses the GNU Object Modeling 
Environment (GNOME) for their default desktop.  Mandrake uses the K 
Desktop Environment (KDE) for theirs.

Each desktop environment has its own libraries of graphical interfaces 
that programmers can use (GNOME has GTK+, KDE has something else (not 
quite sure of the name)).  The really cool part is that if you have the 
proper libraries installed, it doesn't matter which the app you're using 
needs.  You can run K applications under GNOME, and vice versa.  Firefox 
is built on the GTK+ architecture, but still runs fine under K.

Right now, I'm running White Box Enterprise Linux.  It's Red Hat 
Enterprise Linux (for which RH charges), with the Red Hat copyrighted 
items replaced, then rebuilt.  (This is legal - what RH charges for is 
the support, but the source code is still open and freely available.) 
However, I'm running K as my desktop currently.  I prefer its windowing 
colors - that's about the extent of it.  :)

> The long-term success of Linux will depend upon acceptance from end-usrs 
> not us intermediary techies.

Linux has already been around a pretty long time - it's mainstream 
acceptance is a little more real, but I think it's here to stay.  End 
users don't know how to run servers, but they sure do like hitting 
websites.  Underneath it all, Linux is a quite robust server operating 
system.  Not every user needs that kind of power - but, if current 
trends continue, I wouldn't be surprised in a few years to be able to 
order a standard desktop PC from Dell or Gateway with Linux and 
OpenOffice pre-installed.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 26)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-18T18:31:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_UuRd.16206$dZ.728366@news20.bellglobal.com>`
- **In-Reply-To:** `<RWoRd.853$K72.219@fe40.usenetserver.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <YffRd.417302$8l.99004@pd7tw1no> <RWoRd.853$K72.219@fe40.usenetserver.com>`

```
LX-i wrote:
> James J. Gavan wrote:
> 
…[30 more quoted lines elided]…
> 

I think the best summary, Jim, is that Linux is a setup problem, while 
Windows is a maintainence problem.  Since you can do damned near 
anything ... from setting up a desktop mail machine to setting up a 
university data center, Linux can never have a standard installation. 
Windows, you plug it in and it does what it does. Period.

If an amateur bought a machine for just about anything net related, and 
got it set up, they could run for the next ten years without any 
problems that were not hardware related. They could not even hurt 
themselves deliberately without specifically logging in as root, or 
switching to the root account (with password). It's bullet proof, and 
probably far more complete (like spreadsheet and word processor 
included) than windows.

It is stuff like sound cards, and the latest DVD readers/writers that 
seem to cause the most Linux problems.  Nobody designs a PC board and 
does not supply a windows driver. All sorts do that but also make their 
specs trade secrets, so that Linux drivers require someone figuring out 
the hardware in spite of no specs.

At the actual user kevel, with KDE installed, it is simpler and easier 
to use than windows.  I do my file maintenance for my windows machines 
on the Linux GUI. The easiest way to move data from my win98 machine to 
my xpro machine is to drag and drop it from one to the other on the 
Linux box.

On the other hand, I do all my cobol on windows machines. Most of that 
is because I own compilers on them, and upgrading is going to cost me 
about 6 grand canadian.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 24)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-18T10:33:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aNoRd.850$K72.844@fe40.usenetserver.com>`
- **In-Reply-To:** `<xudRd.24467$4I5.1123666@news20.bellglobal.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com>`

```
Donald Tees wrote:
> 
> Well, I'm not sure I'd go that far<G>. I've found Linux a horrendous 
> learning curve, and have had all sort of problems, and spent hours on 
> them.  For example, I have yet to get my DVD burner working under Linux.

What kind of DVD burner is it?  I haven't had any problems out of K3B...

> However one thing it has done flawlessly, and right from the begining 
> with remarkably few problems, is serve as a secure web client and a 
> secure server. I tossed all the virus checkers, etc., and just do my web 
> stuff from Linux.  I can play with client/server stuff inhouse, and 
> leave my machines on/online 24/7 without worrying about security.

There are occasional weaknesses found - nothing a decent firewall can't 
protect you from, but I wouldn't just leave them out there naked on the 
'net...  Depending on your distribution, "yum upgrade all" on a weekly 
basis will keep you pretty well up-to-date.  :)
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 25)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-18T19:08:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xsvRd.30922$4I5.1337628@news20.bellglobal.com>`
- **In-Reply-To:** `<aNoRd.850$K72.844@fe40.usenetserver.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <aNoRd.850$K72.844@fe40.usenetserver.com>`

```
LX-i wrote:
> Donald Tees wrote:
> 
…[20 more quoted lines elided]…
> 


I have a sandbox machine set up, firewalled on the net side but open to 
my inhouse ethernet. It updates from Mandrake automatically once a week, 
and confirms what it did by sending me email. It's an old machine, and 
is pretty slow with a gui as it ends up swapping like a bitch, so I 
never really look at it. I just point everything else at it and use it 
as a gate/router.

About the only way anybody is going to get through that gateway is by 
password hacking, and I use a ten character random generated password.

As to the DVD, I'd have to shut down the machine to look ... I am sure 
that with an hour or two of work, probably some time in Google and 
asking a few people, I could get it to go. I just hate fiddling about 
with *any* hardware setup, so have left it and am using my windows DVD.

I'm gradually learning to use this thing, but there is a lot to learn. I 
just spent damned near a week of my spare time getting DHCP set up 
correctly so that I can boot all six machines consistently, in any 
order, and still have everything work. I could spent six months on 
Webmin alone. I am on a terminal 75 hours a week now.  I do not *want* 
to spend a saturday trying to set up a Linux DVD burner, much as I like 
Linux.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 26)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-18T17:25:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108776348.260386.56610@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<xsvRd.30922$4I5.1337628@news20.bellglobal.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <aNoRd.850$K72.844@fe40.usenetserver.com> <xsvRd.30922$4I5.1337628@news20.bellglobal.com>`

```
> I am sure that with an hour or two of work, probably some time in
Google and
> asking a few people, I could get it to go.

Or just use K3b (Applications, Archiving, CD Burning).

One of the things that I find annoying with most Windows programs is
that you _have_ to use the GUI.  For doing an application's backup to a
CD one starts Nero or similar, and pokes around with the nice GUI until
it writes to the CD.

With Linux I can do that too, but there is no need for the GUI, a
script runs tar (Tape ARchive) to store the data files and compresses,
makes an ISO file system file of this and uses cdrecord to write to the
CDRW.

The application menu has a 'Make Backup Now' option that does it all
(after checking that all other application users have logged off).
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 27)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-19T09:31:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r5IRd.19878$dZ.821047@news20.bellglobal.com>`
- **In-Reply-To:** `<1108776348.260386.56610@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <jRSQd.2432375$f47.428205@news.easynews.com> <%iTQd.410665$8l.86221@pd7tw1no> <9R3Z1R1PflB@jpberlin-l.willms.jpberlin.de> <bW5Rd.414360$Xk.216137@pd7tw3no> <1108671162.044943.120820@z14g2000cwz.googlegroups.com> <tl7Rd.414639$Xk.79951@pd7tw3no> <g98Rd.21915$4I5.1034433@news20.bellglobal.com> <0o9Rd.415595$Xk.144442@pd7tw3no> <xudRd.24467$4I5.1123666@news20.bellglobal.com> <aNoRd.850$K72.844@fe40.usenetserver.com> <xsvRd.30922$4I5.1337628@news20.bellglobal.com> <1108776348.260386.56610@g14g2000cwa.googlegroups.com>`

```
Richard wrote:
>>I am sure that with an hour or two of work, probably some time in
> 
…[5 more quoted lines elided]…
> Or just use K3b (Applications, Archiving, CD Burning).

That hung, deader than a doornail. It was the first thing I tried, of 
course.

Donald
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-16T23:51:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40RQd.2140435$B07.327305@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com>`

```
The ISO 2002 Standard *does* allow one to use either an arithmetic or boolean 
expression for either BY CONTENT or BY VALUE - in the Format 3 CALL statement. 
It also allows an arithmetic expression (but not boolean expression) in a BY 
VALUE clause. This format requires  a "call prototype" (or nested program). 
This means that (at compile time) the compiler can figure out "what format" to 
use for the results of such expressions.

In the Micro Focus Net Express V4 LRM, the same support (for arithmetic 
expressions) is shown for Format 2 - also for CALL statements with prototypes. 
(MF also has an extension allowing a literal in a format 1 CALL statement)

For those working in an OO environment, similar support is provided for the 
INVOKE and inline invocations statements.

   ***

So exactly WHAT are you saying is missing?
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 11)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T23:57:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108627065.241088.252310@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<40RQd.2140435$B07.327305@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <40RQd.2140435$B07.327305@news.easynews.com>`

```
Hi Bill,

what do you mean by "in the Format 3 CALL statement" --- when I used an
arithmetic
expression or the compute statement or some function calls in the "by
value" argument,
the compiler gives an error message. Please see my C++ sample code in
this thread,
so you would know what I am refering too.  Regards.

Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-17T09:01:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l3ZQd.2473935$f47.438630@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <1108586099.180816.104300@c13g2000cwb.googlegroups.com> <40RQd.2140435$B07.327305@news.easynews.com> <1108627065.241088.252310@f14g2000cwb.googlegroups.com>`

```
What version of Micro Focus are you using?  Check the (online) LRM and look for 
a format of the CALL statement that uses a CALL prototype.  (In the LRM, I see - 
it is Format 2 - while in the ISO 2002 Standard it is a format 3 CALL 
statement).

If you define a CALL prototype, are using the current MF product, and are using 
the ISO2000 directive, you shouldn't get any error using an arithmetic 
expression in a CALL by VALUE/CONTENT statement.  If you do, then contact your 
MF support person (as this is documented as working).

Please DO not ask me to look at C++, (Java, C#) whatever code.  I know COBOL and 
understand how it works (or is supposed to work). I do *not* take specs in the 
form of "how do you do this XYZ-language stuff in COBOL".

There are others in this forum qualified to do that, but I don't claim to be one 
of them.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 9)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-16T21:16:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vKOQd.409240$8l.182684@pd7tw1no>`
- **In-Reply-To:** `<1108580825.524713.21820@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com>`

```
Richard wrote:
>>first of all, a clarification on what the win32 API functions are.
> 
…[16 more quoted lines elided]…
> 
Kellie,

Richard is right - try and avoid the 'grubby details'.

Here's a challenge for you and Michael as API aficionados -  try adding 
checkboxes, or colouring *individual* labels in Treeviews, (i.e., the text).

Checkboxes can be done, with some effort. Listview has methods for 
checkboxes but Treeview doesn't.

Coloured labels, not so sure - although somebody, using another 
language, suggested using class RichEditField before setting the 
Treeview label - but didn't provide any code or confirm that it can be 
done. (The problem is the Label in the TreeViewControl is class 
TreeViewItem which is not the same as RichEditField which inherits from 
class TextField).

To avoid any ambiguity - no problem setting the *whole* Treeview to 
foreground NavyBlue on background PaleBlue (using RGB).

Hey ! If either of you find out - let me know :-)

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-16T22:03:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PqPQd.8357$ng6.6510@newssvr17.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:vKOQd.409240$8l.182684@pd7tw1no...
> Here's a challenge for you and Michael as API aficionados -  try adding
> checkboxes, or colouring *individual* labels in Treeviews, (i.e., the
text).
>
> Checkboxes can be done, with some effort. Listview has methods for
> checkboxes but Treeview doesn't.

???

First of all, you can add one column of checkboxes simply by specifying the
extended style WS_EX_CHECKBOXES, which you set with the
LVM_SETEXTENDEDLISTVIEWSTYLE message.

If you want more than one column to have checkboxes..piece of cake,  just
use DrawFrameControl and process the NM_CUSTOMDRAW notification.

Funny you should ask today, because  it was just earlier today I posted code
to draw your own multiple checkboxes on a listview control.
See my code at
http://www.powerbasic.com/support/forums/Forum6/HTML/004773.html

> Coloured labels, not so sure - although somebody, using another
> language, suggested using class RichEditField before setting the
…[3 more quoted lines elided]…
> class TextField).

Sheesh, why bother bleeping around with richtext? Just make the Treeview
Item's szTextmember = LPSTR_TEXTCALLBACK and Windows will notify you when it
wants the text; OR, you can NM_CUSTOMDRAW the treeview nodes the same way as
the listview. (Or you can set the label text color options once and let
Windows handle it, if you want).

What is you want on thre treeview? Checkboxes? There's a style bit you can
set which will automatically create them (you could draw yourself as in the
listview example above, but why split a gut when you don't need to?)

Or do you just want various nodes of the tree to have different colors? I do
that in my EDI Pal(tm) ANSI EDI Viewer-Editor-Printer software.

> Hey ! If either of you find out - let me know :-)

I think I've given you a pretty good head start.  Windows is your friend..
IF  you give yourself the time to know it well....

...But if you need a matchmaker,  or need only an introduction... I know
COBOL, I know Windows, and I'm in the business of providing professional
assistance.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 10)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T14:07:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108591641.411140.305660@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<vKOQd.409240$8l.182684@pd7tw1no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no>`

```
Hi Jimmy,

here is the "Check Box" API code, powered by
Cobol, of course. Kellie.

MyWindowProcedure section.
entry MyWinProc  using
        by value lnk-hwnd
        by value lnk-iMessage
        by value lnk-wParam
        by value lnk-lParam.

      move isFalse to ls-mResult.

      evaluate lnk-iMessage

	when WM-CREATE

	    add WS-VISIBLE
	           WS-CHILD
                            BS-AUTOCHECKBOX
                   giving CheckBoxStyle

            call winapi "CreateWindowEx" using
                 by value     0  size 4
                 by reference "BUTTON"    & x"00"
                 by reference "Check Box" & x"00"
                 by value        CheckBoxStyle
                 by value       10 size 4
                 by value       10 size 4
                 by value       80 size 4
                 by value       20 size 4
                 by value       hWnd
                 by value       100  *> or any number
                 by value       hInstance
                 by value       0 size 4
                returning       hCheckBox
          end-call

the code for coloring the text in a treeview will
follow asap, just remember, Cobol is cool.

regards.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 10)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T15:11:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108595482.806894.31640@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<vKOQd.409240$8l.182684@pd7tw1no>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no>`

```
Hi Jimmy,

here is the API code for coloring "TreeView text",
powered by Cobol, of course.  Kellie.

call winapi "SendMessageA" using
         by value hTreeView
         by value TVM-SETLINECOLOR
         by value 0 size 4
         by value CLR-DEFAULT
      returning    hPreviousLineColor
end-call

call winapi "SendMessageA" using
         by value hTreeView
         by value TVM-SETTEXTCOLOR
         by value 0 size 4
         by value ClrText  *> colorRef of RGB
      returning   hPreviousTextColor
end-call

Regards.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T15:24:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108596289.635690.51290@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1108595482.806894.31640@f14g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com>`

```
>        by value hTreeView
>         by value TVM-SETTEXTCOLOR

The question was:

JJG >> colouring *individual* labels in Treeviews,

The emphasis on *individual* implies that it is easy to colour _all_
text as you have done, now show how each text item can be coloured
differently.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 12)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T03:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lWTQd.411304$6l.317293@pd7tw2no>`
- **In-Reply-To:** `<1108596289.635690.51290@f14g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com>`

```
Richard wrote:
>>       by value hTreeView
>>        by value TVM-SETTEXTCOLOR
…[9 more quoted lines elided]…
> 
COLORING :

Richard is right on the button (label). Kellie if you handed in an
assignment your lecturer/prof would say, "Kellie you've written a
beautiful p;program that works. But I can't give you full marks because
it isn't doing what I asked you to do !"  :-)

As I said, no problem with *ALL* coloring. Experimenting with Treeviews
I wanted to test Buttons/NoButtons, (official name - those are the [+] 
or [-] symbols to contract/expand Level nodes), 
LinesatRoot/NoLinesAtRoot, Lines/NoLines - those are the method names BTW.

Additionally I wanted to set *ALL* for foreground/background color 
choices. I display a Dialog with RadioButton Groups for the above. When 
the events are returned to the Business Class this is what I do for 
coloring :-

        *>-------------------------------------------------------------
        Method-id. 'RB-Color'.
        *>-------------------------------------------------------------
        Working-Storage Section.
        01 ColorTableA.
         05 pic x(12) value "000,000,000,".   *> Black
         05 pic x(12) value "255,255,255,".   *> White
         05 pic x(12) value "173,252,248,".   *> Pale Blue
         05 pic x(12) value "011,015,166'".   *> Navy Blue
         05 pic x(12) value "244,232,140'".   *> Straw (Yellow)
         05 pic x(12) value "196,250,169,".   *> Pale Green
         05 pic x(12) value "174,013,073,".   *> Deep Red

        01 ColorTableB
           redefines ColorTableA.
           05 ColorC occurs 7.
              10 ColorRed               pic 9(03).
              10                        pic x.
              10 ColorGreen             pic 9(03).
              10                        pic x.
              10 ColorBlue              pic 9(03).
              10                        pic x.

        01 SelectedColor.
              05 ColorRed               pic x(4) comp-5.
              05 ColorGreen             pic x(4) comp-5.
              05 ColorBlue              pic x(4) comp-5.

        01 ls-fgN                       pic x(4) comp-5.
        01 ls-bgN                       pic x(4) comp-5.

        01 ls-Foreground                object reference.
        01 ls-Background                object reference.

        Linkage section.
        copy "\copylib\dlgreturn.cpy" replacing ==(tag)== by ==lnk==.

        Procedure Division using lnk-ReturnValues.


        move lnk-FieldID to Dialog-Field
        Evaluate true
            when Field-RB-Color1   *> = Black(1) on White (2)
                 move 1 to ls-fgN
                 move 2 to ls-bgN
            when Field-RB-Color2   *> = Black(1) on Straw (5)
                 move 1 to ls-fgN
                 move 5 to ls-bgN
            when Field-RB-Color3   *> = Dk Blue (4) on Pale Blue (3)
                 move 4 to ls-fgN
                 move 3 to ls-bgN
            when Field-RB-Color4   *> = Dk Red (7) on Pale Green (6)
                 move 7 to ls-fgN
                 move 6 to ls-bgN
        End-Evaluate

        move CORR ColorC(ls-fgN) to SelectedColor
        invoke Color "RGB"
               using ColorRed    of SelectedColor
                     ColorGreen  of SelectedColor
                     ColorBlue   of SelectedColor
               returning ls-Foreground

        move CORR ColorC(ls-bgN) to SelectedColor
        invoke Color "RGB"
               using ColorRed    of SelectedColor
                     ColorGreen  of SelectedColor
                     ColorBlue   of SelectedColor
               returning ls-Background

        invoke os-Treeview "setColor"  using ls-Foreground, ls-Background
        invoke ls-Foreground "finalize" returning ls-Foreground
        invoke ls-Background "finalize" returning ls-Background

        End Method 'RB-Color'.
        *>-------------------------------------------------------------

You'll note Donald recommended hiving off routines so that they could be 
REUSED. Look at my list of RGB colours above. Bearing in mind I'm just 
experimenting, but it would make more sense if I had my own Class 
"MyColors" inherits from the N/E Class 'Colors'. Without going 
Dinsneyesque or Technicolor mad I could decide on a general set of 
colours to put in the table in MyColors. (To be used in any application 
I design). Then all I have to do is :-

*>-----------------
Sender :

01 n1			pic x(4) comp5. *> say set value to 1
01 n2			pic x(4) comp5. *> say set value to 2

invoke os-MyColors "MyColorsRGB" using n1, n2 returning 
os-ForegroundBackground :-

*>--------------------
Class - MyColors - Mehotd-id "MyColorsRGB".

Linkage section.
01 lnk-Color1 pic x(4) comp-5.
01 lnk-Color2 pic x(4) comp-5.
01 lnk-ForegroundBackground.
    05 lnk-fg object reference.
    05 lnk-bg object reference.

Procedure Division using lnk-Color1, lnk-Color2
	returning lnk-ForegroundBackground.

..... Then the coding is similar to the method 'RB-Color' above.
........
........
*>---------------------

Sure - above is extremely verbose compared to your API call, but any 
COBOL programmer, whether or not familiar with OO, can probably follow 
the above logic, even if not being completely comfortable with what is 
going on.

Now I haven't yet seen a screenshot of a Treeview which has differently
coloured labels, but I'll follow up on Michael's suggestions.


CHECKBOXES : - Michael

NO problem with Listviews, it is Treeviews I was after. Had it been 
Listviews then I could have cribbed OO code from a Dialog System 
example. (That's different to Dialog Editor and GUI classes which I'm 
using).


WHAT I WANT :

Having quizzed you two, I've subsequently reliazed I don't need either 
feature :-) But Michael, I will follolw-up on the Colouring you are 
talking about, out of interest.

OK - so here are my original thoughts - An Oil Gas Plant is being 
inspected on an  annual basis and VISUALLY as 'bits and pieces' are 
actioned, I want to convey to the end-user what has been 'actioned' and 
what still requires action. (An inspection can spread roughly over three 
days - so, no matter how disciplined, they, (inspectors), can lose track 
of where they are).

Level 0 - Root = Oil/Gas Plant

Level 1 - Main Plant
Level 1 - Satellite Site # 1 (e.g.  some 12 miles from plant)
Level 1 - Satellite Site # 2....
Level 1 etc...

Level 2 - a Vessel (think hot water tank with inlet and outlet pipes0

Level 3 - individual pipes, 'pieces' in Level 2 being inspected.

Wanted to convey visually, either 'ticking' a checkbox as 'ON' or 
re-coloring the text in the Label - I would use only ONE changed 
foreground color.

Using either checkbox/foregound color - as each Level 3 is 'updated' - 
change the node display. Similarly when all Level 3s within a Level 2 
are 'actioned' then change checbox/color for Level 2. Similarly when all 
Level 2s within a Level 1 have been actioned, 'change' Level 1 display.

I don't want to go either color or widget-mad so it could be an option 
between a checkbox or foreground color. Now Checkboxes, rather like 
Radiobuttons are meant to convey end-user choices so that the program 
follows down a particular path. That's not exactly how I want to use 
checkboxes - from above you can see I want to set them 'ON' 
programatically - not an end-user option. So I would be 'misusing' 
checkboxes.

Using the ImageList concept (like we see 'folders' in Windows Explorer), 
I want an "actioned" icon to appear before the label description. Much 
easier and I already have sample code to introduce images. Haven't tried 
it yet, but want labels to appear initially without an 'OK icon' and 
only display the 'OK Icon' image when necessary. Much easier.

If anybody is interested in extracting icons for Treeviews etc., here's 
a neat piece of Shareware :-

http://www.nirsoft.net/utils/iconsext.html

You can select specifics like Shell32.dll or run the software to extract 
a list of *ALL* icons on your machine. Beware ! The full feature on my 
machine gave over 3,000 icon images, You get 'repeats' of icons if you 
include sub-folders. From the scrolled dialog you then select the icons 
you want to keep in your own library.

Kellie and Michael - thank you for your input.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 13)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-17T15:51:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F33Rd.6240$Gt2.2390@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <lWTQd.411304$6l.317293@pd7tw2no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:lWTQd.411304$6l.317293@pd7tw2no...
>
> CHECKBOXES : - Michael
…[4 more quoted lines elided]…
> using).

Treeview styles, direct from the Windows SDK:
"TVS_CHECKBOXES
Version 4.70. Enables check boxes for items in a tree-view control. A check
box is displayed only if an image is associated with the item. When set to
this style, the control effectively uses DrawFrameControl to create and set
a state image list containing two images. State image 1 is the unchecked box
and state image 2 is the checked box. Setting the state image to zero
removes the check box altogether. For more information, see Working with
state image indexes.
Version 5.80. Displays a check box even if no image is associated with the
item.

Once a tree-view control is created with this style, the style cannot be
removed. Instead, you must destroy the control and create a new one in its
place. Destroying the tree-view control does not destroy the check box state
image list. You must destroy it explicitly. Get the handle to the state
image list by sending the tree-view control a TVM_GETIMAGELIST message. Then
destroy the image list with ImageList_Destroy.

If you want to use this style, you must set the TVS_CHECKBOXES style with
SetWindowLong after you create the treeview control, and before you populate
the tree. Otherwise, the checkboxes might appear unchecked, depending on
timing issues."

Line colors in treeview control: See TVM_SETLINECOLOR message (sets all)

Change color of labels (node text) for individual tree nodes:
Process the NM_CUSTOMDRAW message using the same logic as shown my listview
code at http://www.powerbasic.com/support/forums/Forum6/HTML/004773.html

(Except use the treeview calls instead of the listview calls, e.g., to get
the rectangle, use TreeView_getItemRect. You'll have to set the text color,
background color (and optionally the font to be used) using standard GDI
calls, then draw the text without either TextOut or DrawText)

MCM





> Coloured labels, not so sure - although somebody, using another


n the link to listview control code I posted yesterday)









MCM





>
>
…[60 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 14)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T17:39:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jF4Rd.414183$Xk.75959@pd7tw3no>`
- **In-Reply-To:** `<F33Rd.6240$Gt2.2390@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <lWTQd.411304$6l.317293@pd7tw2no> <F33Rd.6240$Gt2.2390@newssvr31.news.prodigy.com>`

```
Michael Mattias wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
> news:lWTQd.411304$6l.317293@pd7tw2no...
…[10 more quoted lines elided]…
> "TVS_CHECKBOXES
<snip>

Just recently re-loaded Net Express on my new XP. There was also a 
(dated) CD for SDK, which came as part of the package. Tried loading it 
but said you need a new one. Guess I'd better check out MS and download 
latest SDK.

Thanks for the additional detail.

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 12)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-16T20:38:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108615104.389166.154670@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1108596289.635690.51290@f14g2000cwb.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com>`

```
Hi Jimmy,

here is another API code for Selective Item coloring for
the TreeView, just another proof that Cobol is cool.
Kellie.

*> NM-CUSTOMDRAW Message  *> first message...

      initialise nmtvcustomdraw.
      call winapi "SendMessageA" using
             by value       hTreeView
             by value       NM-CUSTOMDRAW
             by value       0 size 4
             by reference NMTVCUSTOMDRAW
            returning       CDRF-NOTIFYITEMDRAW
      end-call.

      01  NMTVCUSTOMDRAW is typedef.
          02  tagNMTVCUSTOMDRAW.
                03 hwndFrom     HWND.
                03 idFrom          UINT.
                03 code             UINT.
          02  tagNMHDR.
                04 DrawStage    DWORD.
                04 hdc               HDC.
                04 rc                  RECT.
                04 ItemSpec       DWORD_PTR.
                04 ItemState       UINT.
                04 ItemlParam    LPARAM.
          02  clrText              COLORREF.
          02  clrTextBk          COLORREF.
          02  iLevel                INT.

*> need to select flags from the following for Array:
   NMCUSTOMDRAW Structure

DrawStage:

CDDS-POSTERASE
CDDS-POSTPAINT
CDDS-PREERASE
CDDS-PREPAINT
CDDS-ITEM
CDDS-ITEMPOSTERASE
CDDS-ITEMPOSTPAINT
CDDS-ITEMPREERASE
CDDS-ITEMPREPAINT
CDDS-SUBITEM

ItemState:

CDIS-CHECKED
CDIS-DEFAULT
CDIS-DISABLED
CDIS-FOCUS
CDIS-GRAYED
CDIS-HOT
CDIS-INDETERMINATE
CDIS-MARKED
CDIS-SELECTED
CDIS-SHOWKEYBOARDCUES

Regards.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 13)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-17T15:51:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <1108615104.389166.154670@f14g2000cwb.googlegroups.com>`

```
"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1108615104.389166.154670@f14g2000cwb.googlegroups.com...
> Hi Jimmy,
>
…[14 more quoted lines elided]…
>


Sorry, Kellie, that's not correct. The programmer does not send
NM_CUSTOMDRAW: Windows sends it automatically. It comes in the
NMTVCUSTOMDRAW stucture supplied as a parameter when processing WM_NOTIFY.
If you send this message as shown, you'll end up doing the painting twice
each time the control needs repainting... and  if you don't return one of
the CDRF-xxxxx values, the default painting occurs on the system-generated
WM_NOTIFY/NM_CUSTOMDRAW.

See my code at
http://www.powerbasic.com/support/forums/Forum6/HTML/004773.html . That's
for the listview, but the treeview code is quite similar. Yes my code is
written in BASIC, but I've always said well-written BASIC looks a lot like
well-written COBOL.

(And poorly written BASIC or COBOL looks like... well, they look like poorly
written BASIC or COBOL)

MCM
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 14)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-17T09:35:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108661758.146137.30870@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <1108615104.389166.154670@f14g2000cwb.googlegroups.com> <F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com>`

```
Hi Michael,

the NM_CUSTOMDRAW is a message and NOT a window notification.
this message can be sent using the win32 API "sendmessage" function,
with a reference to the NM_CUSTOMDRAW (Tree View) notification, that
uses the predefined array structure as I have listed in my code above.
there are TWO formats for windows controls: (1). is a message, and can
be sent by the programmer to the control any time. (2). is a
notification for
a header, a rebar, a button, a listview, a tooltip, a trackbar, a
treeview or
a toolbar control. These notifications are sent by windows to the
control.
I researched these informations at the MSDN and thats what they told me
to give to Jimmy. :--)
Regards, Kellie.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 14)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-17T18:43:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0B5Rd.414332$Xk.259636@pd7tw3no>`
- **In-Reply-To:** `<F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <1108615104.389166.154670@f14g2000cwb.googlegroups.com> <F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com>`

```
Michael Mattias wrote:
> "Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
> news:1108615104.389166.154670@f14g2000cwb.googlegroups.com...
…[39 more quoted lines elided]…
> 
Kellie,

Interesting what Michael writes above, and I *think* the following topic 
is in the same vein. Just for a 'little' colouring, I wanted to add 
pastel shades to ComboBox Dropdown lists. Bearing in mind that a Combo 
is made of two parts (a) the Text Area (top entry) and (b) the actual 
droplist, I had no problem colouring the Text Area, but couldn't for the 
life of me figure how to get coloured droplist entries.

David Sands, Micro Focus, provided the solution. Firstly in the Dialog 
Editor you have to set the properties for OwnerDraw and HasStrings for 
the Combo control. (Irritatingly the GUI classes do not provide methods 
for either of these features - which following the N/E route means that 
you must hard-code in the Dialog Editor properties, giving no chance of 
dynamically creating a droplist). OK, so using a pick and shovel 
approach you *could* use APIs to dynamically create the droplist :-)

I think the code below is on the same tack that Michael is indicating; 
Windows itself triggers the actual drawing and painting. I adjusted 
David's code to allow for a Dialog having more than one droplist. 
Haven't done it recently, but stepping through the source code with the 
Animator line-by-line, I could visually see the droplist entries being 
created, overlaying the image of my source file - (1) draw a rectangle 
and colour it, then (2) fill it with the text for each individual 
element. I've expanded David's text. For my own sake, I've made 
notations against the API entries.

Like Bill, I'm comfortable with COBOL, but looking at APIs, C or Java - 
and translating what they are doing ???????

        *>--------------------------------------------------------------
        method-id. "wmDrawItem".
        *>--------------------------------------------------------------

        *> Here we trap the Paint notifications to the Drop Down
        *> ComboBox on the Dialog. Its up to us how it's drawn !

        *> This is an adaptation of code provided by David Sands of
        *> Micro Focus. David set up four basic colours so that the
        *> four elements in his list each reflect their own colour,
        *> (Object Reference os-Color occurs 4). I have adapted the
        *> routine to have a pastel colour per droplist, (using RGB)
        *> - the program will accept up to 6 different DropDown Lists
        *> per Dialog

        working-storage section.
        01 ls-display.
           05 pic x(04) value "Type".
           05 lsd-ctltype        pic zz9.
           05 pic x(07) value " ResID".
           05 lsd-ctlid          pic zzz9.
           05 pic x(08) value " Itemid".
           05 lsd-Itemid         pic zzzzzzzz9.
           05 pic x(04) value " Idx".
           05 lsd-Index          pic zz9.
           05 pic x(02) value "  ".
           05 lsd-text           pic x(40).

        *> above used for testing

        local-storage section.

        01 n2               pic x(4) comp-5.
        01 n3               pic x(4) comp-5.

        01 ls-bytes          pic x(4) comp-5.
        01 ls-height         pic s9(9) comp-5.
        01 ls-Index          PIC S9(9) COMP-5.
        01 ls-PixelHeight    pic 9(9) comp-5.
        01 ls-Size           pic x(4) comp-5.
        01 ls-StateFlag      uint.
        01 ls-width          pic s9(9) comp-5.
        01 ls-x              pic s9(9) comp-5.
        01 ls-y              pic s9(9) comp-5.

        01 ls-Brush          usage object reference.
        01 ls-Collection     usage object reference.
        01 ls-Drawsurface    usage object reference.
        01 ls-Font           usage object reference.
        01 ls-string         usage object reference.

        linkage section.
        01 lnkWnd       HWND.
        01 lnkMsg       INT.
        01 lnkwParam    INT.
        01 lnklParam    POINTER.
        01 mResult      LRESULT.
        01 drawItem     DRAWITEMSTRUCT.

        procedure division using lnkWnd lnkMsg lnkwParam lnklParam
           returning mResult.

        *>01  tagDRAWITEMSTRUCT is typedef.

        *> 02 ctltype       usage uns-int.
            *>78  ODT-MENU      value           1.
            *>78  ODT-LISTBOX   value           2.
            *>78  ODT-COMBOBOX  value           3.
            *>78  ODT-BUTTON    value           4.
            *>78  ODT-STATIC    value           5.

        *> 02 ctlid    usage uns-int.   = Resource ID
        *> 02 itemid   usage uns-int.   = Index of Element in DropList

        *> 02 itemaction            usage uns-int.
            *>78  ODA-DRAWENTIRE    value h"0001".
            *>78  ODA-SELECT        value h"0002".
            *>78  ODA-FOCUS         value h"0004".

        *> 02 itemstate             usage uns-int.
            *>78  ODS-SELECTED      value h"0001".
            *>78  ODS-GRAYED        value h"0002".
            *>78  ODS-DISABLED      value h"0004".
            *>78  ODS-CHECKED       value h"0008".
            *>78  ODS-FOCUS         value h"0010".
            *>78  ODS-DEFAULT       value h"0020".
            *>78  ODS-COMBOBOXEDIT  value h"1000".

        *> 02 hwnditem    usage data-pointer. = handle to control
        *> 02 1hdc        usage data-pointer. = handle to device context
        *> 02 rcitem      usage rect.         = rectangle defined in 1hdc
        *> 02 itemdata    usage uns-long.     = CB SETITEMDATA for Combo

        set address of drawitem to lnklparam

        move ctltype to lsd-ctltype
        move ctlid   to lsd-ctlid
        move Itemid  to lsd-Itemid

        move zeroes to n3
        Perform varying n2 from 1 by 1 until n2 > DropListCount

               if ctlid = ws-DropListID(n2)
                  move n2 to n3
                  EXIT PERFORM
               End-if
        End-perform

        Evaluate true
           when  n3 = zeroes
           when  itemid = -1
                 EXIT METHOD
           when  other
                 invoke os-DropList(n3) "copyOfContents"
                      returning ls-collection
                 invoke ls-Collection "size" returning ls-size

        End-Evaluate

           Evaluate true
               when  itemAction = ODA-DRAWENTIRE
               when  itemAction = ODA-SELECT
                     perform DRAW-ENTIRE
           End-evaluate
        .
        EXIT PROGRAM.

        DRAW-ENTIRE.

         invoke DrawingSurface "fromHandle" using 1hdc
             returning ls-Drawsurface

         invoke brush          "new"                returning ls-Brush
         invoke ls-Brush       "solid"
         invoke ls-Brush       "setcolor"           using os-color(n3)
         invoke ls-Drawsurface "setBackGroundColor" using os-color(n3)

         move 1left          to ls-x
         move 1top           to ls-y
         compute ls-height = 1bottom - 1top
         compute ls-width  = 1right - 1left
         invoke ls-Drawsurface "fillrectangle"
             using ls-x ls-y ls-width ls-height ls-Brush
         compute ls-Index = itemid + 1

         invoke os-DropList(n3) "GetItemText"
                using ls-Index returning ls-string

         move ls-Index to lsd-Index
         invoke ls-string "sizeinbytes" returning ls-bytes
         invoke ls-string "getValue"    returning lsd-text
        *> display ls-display

         invoke ls-Drawsurface "getFont" returning ls-Font
         invoke ls-Font        "getPixelHeight" returning ls-PixelHeight
         compute ls-y = (1bottom + 1top - ls-PixelHeight) /2
         invoke ls-Drawsurface  "drawTextAt" using ls-string ls-x ls-y

        *> If this is the Selected Item then draw a Focus
        *> rectangle around the item to give user feedback on what
        *> is current in the list

            move ods-selected to ls-StateFlag
            call "cbl_and" using itemstate
                                 ls-StateFlag
                                 by value 4
            if ls-StateFlag > 0
                call wapi "DrawFocusRect"
                 using by value 1hdc by reference rcitem
            end-if

        *>---- Clean Up

          invoke ls-Brush       "finalize"     returning ls-Brush
          invoke ls-string      "finalize"     returning ls-string
          invoke ls-Font        "destroyproxy" returning ls-Font
          invoke ls-Drawsurface "destroyproxy" returning ls-Drawsurface
          .

        End method "wmDrawItem".
        *>--------------------------------------------------------------
        Method-id. "zCreateColoredDroplist".
        *>--------------------------------------------------------------

*> Following is me using the info from the Dialog Editor to setup the
*> combos, then as necessary Windows triggers the method above

        *> This method is for coloured droplists and overrides the same
        *> method in 'super' TabbedDialog (tdialog.cbl). 'OwnerDraw' and
        *> 'HasStrings' MUST be set in the Dialog Editor when creating
        *> the ComboBox

        Local-storage section.
        01 k                             pic x(4) comp-5.
        01 ls-event                      pic x(4) comp-5.
        Linkage section.
        copy "\copylib\dlgParams.cpy" replacing ==(tag)== by ==lnk==.

        Procedure Division using lnk-Params.

        *> Note : My collection is already sorted, so I don't want the
        *> Dialog sorting the contents before display

         move lnk-DropListNumber to k
         move lnk-ID to ws-DropListID(k)

         initialize ws-MethodRec
         invoke self "getObjectFromId" using lnk-ID
                returning os-DropList(k)
         invoke os-DropList(k) "MonoSpacedFont"
        *> invoke os-DropList(k) "NotSorted"
         move p2ce-select to ls-event
         invoke os-DropList(k) "setEventTo" using
                     ls-event self "ReturnDropList "
                     lnk-Field, lnk-ReturnType
         invoke os-DialogCollection(1) "add" using  os-DropList(k)
         move lnk-MethodName to ws-MethodName
         invoke os-DialogCollection(2) "add" using  ws-MethodRec

        End Method "zCreateColoredDroplist".
        *>--------------------------------------------------------------


Meanwhile I'll go take a look at Michael's Basic code. I've looked 
before and it is 'user friendly'.

Question Michael - have you had a chance to look at VB with dotNet, and 
does it provide simple features for this 'mystery stuff' like we are 
discussing above  ?

Jimmy
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 15)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-17T20:07:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UP6Rd.8811$hU7.7189@newssvr33.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com> <1108580825.524713.21820@g14g2000cwa.googlegroups.com> <vKOQd.409240$8l.182684@pd7tw1no> <1108595482.806894.31640@f14g2000cwb.googlegroups.com> <1108596289.635690.51290@f14g2000cwb.googlegroups.com> <1108615104.389166.154670@f14g2000cwb.googlegroups.com> <F33Rd.6241$Gt2.1534@newssvr31.news.prodigy.com> <0B5Rd.414332$Xk.259636@pd7tw3no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:0B5Rd.414332$Xk.259636@pd7tw3no...
>
> Meanwhile I'll go take a look at Michael's Basic code. I've looked
> before and it is 'user friendly'.

Thrank you.
>
> Question Michael - have you had a chance to look at VB with dotNet, and
> does it provide simple features for this 'mystery stuff' like we are
> discussing above  ?

I looked at dot-net about three years ago, and pretty much decided then my
interest in same is precisely zero. I just do not see what good learning
dot-net at my age will do: there is still plenty of need for quality
"non-dot-net" software and since that's what I'm good at, that's where I am
staying for the forseeable future. (Were I twenty years younger, I'd look at
dot-net harder).

I also don't do "O-O" - all my Windows code is 100% "SDK-Style" calls to the
Windows API. Since I market "applications results" rather than "programming
technique", my only competitive disadvantage occurs when a prospect actually
cares.. which generally coincides with those times when I am perfectly
willing to "lose" a proposal to a competitor.

Remember, I had 20+ years as an operations manager/general manager in the
distribution industry before I changed to Information Technology about 12
years ago. When I was on the "I/T customer side of the desk,"  I was
generally bored to death by presentations on which technology, methodology
or ideology was used to build software: as a businessman, I just wanted
something which got the job done, got it done right, and got it done on
time. (Sheesh, pretty naive, huh? Amazing I've been able to eke out a living
all this time.)

My "thing" is results, not process: meaning I would likely have been one
terrible bureaucrat. But my late sainted mother would still have been proud
of me.

MCM
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 8)_

- **From:** Adrien Plisson <aplisson-news@stochastique.net>
- **Date:** 2005-02-16T22:03:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4213b486$0$22461$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<1108578002.119643.205360@l41g2000cwc.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com> <42138008$0$20893$ba620e4c@news.skynet.be> <1108578002.119643.205360@l41g2000cwc.googlegroups.com>`

```
Kellie Fitton wrote:

> Hi Rien,
> first of all, a clarification on what the win32 API
> functions are. The win32 API's is a generic term
> meaning "Application Programming Interface",

the generic term here is "API", not "Win32 API" which refers explicitly 
to programming for the windows operating system.

[snip]
 > That said, if a business application is
> running on a different OS other than windows,
> then these programs are using some low-level
> system library supports (Assembly api or
> C++ api),

not more low-level than the Win32 API...

> which is the same thing as the win32
> API's --- except it is coded for a different
> environment, with different names and maybe
> different entry-points. 

so it is different... it is the same concept, but a totally different 
implementation, not even the same interface. (to complicate a bit, think 
about POSIX: a platform independent OS API implemented in term of OS 
specific API...)

this leads us to the point raised on this thread: if you directly use 
the OS's API (whatever the OS), your application is not portable: you 
have to stick to this OS. one way to render your application portable is 
to abstract features and wrap low-level system calls into higher level 
modules. this way, you can easily rewrite the higher level module's 
implementation to run on a different platform. then how do you define 
your higher level module's interface ? it is an API...

this is the way we write portable libraries: define an OS independent 
interface, and implement it using low-level API depending on the OS it 
targets.

> After all, why would you
> re-invent the cobol wheel?  

here is the rest of the point, if you can define a module to make an 
abstraction of a set of feature, chances are a (portable) library 
already exists doing the same. then, instead of using the low-level OS 
API, you'd better use the library, it will save you a lot of time (and 
quite a lot). after  all, why would you re-invent the (insert the name 
of your favorite programming language here) wheel ?
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T09:46:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108576010.628567.99150@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1108571889.932695.188110@o13g2000cwo.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com>`

```
> every program exist today .. is eventually built UPON the win32 API
functions.

Why do you think that every program runs on Windows - have you never
heard of or seen anything else ?
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-16T20:18:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7UNQd.2118501$B07.323605@news.easynews.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com> <1116las5aadl881@news.supernews.com> <hdJQd.8419$hU7.1743@newssvr33.news.prodigy.com> <1108571889.932695.188110@o13g2000cwo.googlegroups.com>`

```
Kellie,
   Other have already pointed out your fallacy in think that "every program" is 
written to run in a Windows Environment.

It is my "best guess" that there are still more (MANY MORE) *COBOL* programs 
being written and maintained for "mainframe" operating systems than for Windows. 
(Certainly more in the "maintained" status - possibly more in the "written" 
category too).

However, it is also true that no (or very few) Linux and Unix application 
programs use Windows API's at their "underlying" level.

Finally, I do not know, but my *guess* is that many COBOL programs that run on 
Windows are ""command" driven (not interactive) and of those, certainly SOME 
don't use Windows API's  (Some do - but certainly not all)
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-16T14:22:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AGIQd.6075$C27.3758@newssvr31.news.prodigy.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com>`

```
"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1108526697.928623.234600@g14g2000cwa.googlegroups.com...
> if we can perform
> two functions simultaneously (overloading) that should save CPU
> execution time as well.

Only in multi-processor systems. As my late sainted mother might have said,
" there are only so many 'clocks' available from a processor, and a single
processor can only do one little thing at a time."   (Ok, so it's a pretty
tiny "might").

> if you can reduce the number of declared variables
> (overloading functions), it will make the program much smaller in size,
and therefore will run
> much faster, and that should improve the performance of the application.
Right?

Sorry, Kellie, that's an urban myth, an old wives tale, a bunch of
hooey.....All that stuff you don't do is done by the compiler anyway. (part
of what you pay for).

MCM
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T10:15:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108577747.170413.200720@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1108526697.928623.234600@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com>`

```
> declaring variables in cobol programs is a Major job

I misunderstood the feature you were illustrating.  It wasn't
overloading at all.  You were wanting to use expressions as call
parameters.

In C (not just C++) and C like languages, expressions, including those
with function calls,  can be used where a value is required.  This
includes parameter lists for calls.

In Cobol the function call must be used to return a value to a variable
which is then used in the call.

If you had used C extensively then you would understand some of the
problems and limitations of the way that C uses expressions.  An
experienced programmer knows these issues and knows when to use them
and when not to, when casts are required, or coersion, when short
circuiting will bypass function evaluation, when to worry about order
of evaluation.

Instead of burdening Cobol programmers with all those issues, the
language avoids them completely by disallowing constructs that would
require the programmer to know about such things.
```

###### ↳ ↳ ↳ Re: May I introduce myself to cobol?...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-16T10:31:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108578689.211406.289180@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1108526697.928623.234600@g14g2000cwa.googlegroups.com>`
- **References:** `<1108510305.006428.237000@g14g2000cwa.googlegroups.com> <1108516103.905735.183550@c13g2000cwb.googlegroups.com> <1108526697.928623.234600@g14g2000cwa.googlegroups.com>`

```
> if you can reduce the number of declared variables (overloading
functions),

No, overloading is something different.  I misunderstood what you were
saying.

> it will make the program much smaller in size,

No.  Not 'much smaller', a few bytes perhaps.  You may also be able to
use LOCAL-STORAGE for intermediates which makes it stack-based and thus
makes W-S smaller.

In fact you probably should be using LOCAL-STORAGE for many variables
as otherwise the callbacks can kill your data.

> and therefore will run much faster, and that should improve the
performance of the application.

There is _no_ indication that avoiding using explicit variables makes
the program faster.  The expression still stores its result somewhere,
this result is still passed by the call.  You may have saved a few
bytes of source code, but there is no reason to think that the program
will run faster.

> this way, we can hit two birds with one stone, and silence our
critics.
> :--)  am I correct?

No.  It will still not be the 'perfect' language they think theirs is.


I think that you are having enough problems without having to worry
about casts, coersion, evaluation order and short circuiting.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
