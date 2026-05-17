[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Object oriented programming

_4 messages · 4 participants · 1997-11_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Object oriented programming

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<347a0904.1257178@news.tig.com.au>`

```

I have been waiting for a better description of object oriented
programming and some rebuttals to the ï¿½it just modular programmingï¿½
statements. Since none have been forth coming here are my thoughts
on the subject. I know about 0% on the Cobol extension of this and I
will have to make a conscious effort to read up on object oriented
Cobol ï¿½real soon nowï¿½. (Donï¿½t watch this space for findings, it could
be a while.)

Object oriented programming comes with the following three things:
encapsulation, inheritance and polymorphism. These are not simply
modifications to the way that programs are written but whole new
thought processes in design.

Encapsulation:

This is the concept of keeping the data and the logic that works on it
tightly bound. Access methods to the data should always come though a
defined interface. In other words a ï¿½move 1 to data-item in groupï¿½
should not be valid but a ï¿½call set-data-item in instance using 1ï¿½ is.
The reason is that the way that the value is stored within the routine
may dramatically change between platforms however your logic should
not.

An ï¿½instanceï¿½ is the actual object. For example I can describe a table
as flat top having four legs this is the definition. What I am
sitting at now is an instance of a table. This is surprisingly
important concept as you may be acting on an instance that you have
not defined. My computer table rejects setting a place as no food is
allowed there but my dining table does not. Your code just queries the
instance and relies on the definition of that instance to give the
result. Encapsulation also hides the fact that my computer desk top
goes up and down to the wide world. If you ask me as a ï¿½computer deskï¿½
then I do because it is important in that context.

Inheritance:

This is the concept of taking a unit of work and extending it to
perform new work but leaving the basic code alone. Objects are
sometimes mistaken for good modular programming and there are some
similarities. The major addition is the fact that it also adds the
data items to the equation. For example all accounts at the bank have
balance, withdrawals and deposit transactions. This can be defined
in a fundamental structure and all accounts will behave in a similar
way but the bugs associated with maintaining balances are very
centralised and therefore removed quickly. An incentive account will
take on the look of the general ï¿½accountï¿½ details and add some
interest tier details. A term deposit account will not allow any type
of withdrawal except for complete withdrawal and will have special
withdrawal logic it inherits all other logic from the general
ï¿½accountï¿½.

Polymorphism:

This is the concept of making the driving program work in a defined
way but getting different results based upon what type of item (or
object) it is working on.

Using the bank example: Assume I have 2 term deposits, 1 cheque, 1
credit card and 1 non interest bearing account. I might write a
program that does a daily interest calculation. My driver will read
all my accounts and it will create an ï¿½instanceï¿½ of every account
2+1+1+1(four types with 5 instances). The program will then call
each of the calculate interest routines for all 5 accounts, one may
just return (non interest), others check against dates, and other do a
daily calculation. The point is my driver does not know or care about
the details of each type. In a perfect set up you could just add a
new definition of an account and then it would automatically be
available for all account functions.

Regarding Modular Programming:

The problem is that the encapsulation is for all the ï¿½methodsï¿½ or
modules that act upon the embedded code to be bound up as one unit.
This means that more than one module would have to reference the data.
While this is possible with having a create module that returns a
pointer to the object data. Each object provides providing a series
of calls to act on the object there is no guarantee by the compiler
that code not associated to the object can access the internal
definition. This also leads to the problem of implementing being huge
evaluate statements to select which data type is being called for and
then actions as appropriate.

Dynamics may replace this if each object (group level) contains a
field that contains the module to call when accessing the data. This
leads to the ï¿½dynamicï¿½ function call overhead as highlighted in
previous discussions. In a true OO environment the objects can be
statically bound (put in with a linker not called from a library) and
references to them come via indirection (pointer to functions). This
means that the call would be conceptually ï¿½call x in object using ...ï¿½
where x is NOT ï¿½dynamicallyï¿½ called from a library. The one level of
indirection is definitely an overhead however it is offset by
reduction of evaluate statements in the code.

Parting words:

Creating an object oriented program is definitely an art as designing
the application on the wrong level of abstraction (which is the crux).
The wrong choice can totally destroy any benefits that otherwise be
gained. I recommend lots of reading and some throw away examples
before trying anything ambitious.

When considering this what level of abstraction is appropriate for a
Cobol compiler, is a file an object, a section or a statement. Is
the compiler fundamentally object variable name list, process
statements. Choose the wrong one then when you implement it becomes a
nightmare. I read an article on how to write an assembler in OO and
the design surprised me.

I believe herein lies the future of programming. If you disagree
flame me and defame me but time wonï¿½t shame me.

Ken
I program for fun with Cobol for a living.
```

#### ↳ Re: Object oriented programming

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-11-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d62e013dec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<347a0904.1257178@news.tig.com.au>`
- **References:** `<347a0904.1257178@news.tig.com.au>`

```

Ken Foskey wrote:
› 
› I have been waiting for a better description of object oriented
…[111 more quoted lines elided]…
› I program for fun with Cobol for a living.

I'll throw in my two cents! IMHO, one of the main reasons for the rise
of the use of OO concepts is the GUI. There are a lot of things that OO
helps that are not related to the GUI, but if I can have a series of
easily extendable objects to create a button bar, a dialog box, a radio
box, a drop down list box, etc, etc then it offords the opportunity to
create that code much more quickly than coding at the API level. I can
spend the majority of time working on the business and processing
application than reinventing the wheel. Thus, using something like MFC
or OWL to write windows program user interfaces offers a great deal of
code reusability. When you need to access an API function you can do so.

Unfortunately, there aren't too many cases I can think of to apply this
to a mainframe environment and get the same bang for the buck. Maybe a
field validation object for CICS programs to use, maybe in a particular
department there may be a way to encapsulate some common, volatile
business logic, but there just doesn't seem to be as many time saving
areas as the GUI examples commonly used as an example of pc OO.

Again this is just my opinion, maybe some others can comment and we can
get a discussion going???

Steve

*****************************************************************

            Support the Western Bigfoot Research effort
                         for information:
             http://www.teleport.com/~caveman/wbs.html

prg··.@ep··x.net
url http://www.epix.net/~prgsdw
*****************************************************************
```

##### ↳ ↳ Re: Object oriented programming

- **From:** "andre rosenthal" <ua-author-17072399@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d62e013dec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d62e013dec-p2@usenetarchives.gap>`
- **References:** `<347a0904.1257178@news.tig.com.au> <gap-d62e013dec-p2@usenetarchives.gap>`

```

Actually one can use an ORB that is CORBA compliant and extend an object in
a distributed environment. Without OO this is virtually not possible. I
guess this is the most important issue of OO in a server(s) (as far as
n-tier architecture is concerned.) As far as GUI is concerned, you are
absolutely right on saying that frameworks such as MFC are vital for RAD,
which will take a life-time had it not being for OO.

Cheers ..
Andre

steve wolfe wrote in message <347··.@ep··x.net>...
|Ken Foskey wrote:
|>
…[146 more quoted lines elided]…
|*****************************************************************
```

###### ↳ ↳ ↳ Re: Object oriented programming

- **From:** "s..." <ua-author-13061530@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d62e013dec-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d62e013dec-p3@usenetarchives.gap>`
- **References:** `<347a0904.1257178@news.tig.com.au> <gap-d62e013dec-p2@usenetarchives.gap> <gap-d62e013dec-p3@usenetarchives.gap>`

```

"Andre Rosenthal" wrote:
› Actually one can use an ORB that is CORBA compliant and extend an object in
› a distributed environment. Without OO this is virtually not possible. I
› guess this is the most important issue of OO in a server(s) (as far as
› n-tier architecture is concerned.)

OO also lets you into the world of ActiveX/DCOM/OLE - the Microsoft competitor
to ORBs. Although it's possible to write COM applications in non-Object
COBOL or another non-OO language, having objects makes it far easier.
With the advent of services based on COM such as Microsoft Transaction
Server, it becomes even more useful, especially with a distributed
architecture.

COM, incidentally, is based on interface inheritance, rather than
implementation inheritance - that is, while a subclass may inherit the
methods of its parent, it is forced to implement them itself rather
than relying on the parent's implementation.

This is an interesting choice, made (I believe) because in a (large) OO
system, one of the disadvantages is that a certain amount of knowledge
of each super class method is needed when over-riding them in order
to keep the integrity of the base class.

For instance, your method "makevisible" may actually unshow the object
while at the same time setting a visibility field (in the super class)
to true. Any methods then called on the super class might thereafter
assume that the object is visible.

› As far as GUI is concerned, you are
› absolutely right on saying that frameworks such as MFC are vital for RAD,
› which will take a life-time had it not being for OO.

Well, you can design GUI interfaces and application with design tools that
are not "true" OO - there are many such tools out there, such as Visual
Basic or MF's own Dialog System.

Sometimes, this approach is better than frameworks, which can be large,
and may "straitjacket" your application.

[Snip]

Steve.
A developer at Micro Focus.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
