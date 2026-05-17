[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The Programmer's New Clothes

_4 messages · 4 participants · 1996-10_

---

### The Programmer's New Clothes

- **From:** "spam.f..." <ua-author-17086140@usenetarchives.gap>
- **Date:** 1996-10-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<545omu$ck9@news.inetdirect.net>`

```

THE PROGRAMMER'S NEW CLOTHES
----------------------------


"One day there came two men who called themselves weavers. They pretended
that they knew how to weave cloth of the most beautiful colors and magnificent
patterns..." [1]

Object-oriented programming (OOP) and its counterparts, object-oriented
analysis (OOA) and object-oriented design (OOD), burst onto the scene in the
late 1980s amid considerable speculation about their promise to revolutionize
data processing. The object-oriented approach requires the revision or
rejection of many traditional methods of designing and developing computer
software. In return, it promises that designers and developers will realize
numerous benefits: faster development, easier maintenance, and a reduction in
errors, to name a few. Unfortunately, the claims made for this approach are
frequently met with credulous acceptance, and rarely receive the skeptical
attention that the cost demands. This paper shows that the case for abandoning
proven traditional methods of software design and development, in favor of
object-oriented methods, is based on this shaky footing:

* authors and researchers, most with little experience developing real
applications in the real world, citing one another's papers in a mutual
admiration and back-patting society;

* fantastic claims that have all been made before, for other methods;

* exaggeration of the capabilities of object-oriented methods;

* disregard of their drawbacks;

* denigration and misrepresentation of the capabilities of traditional
methods; and

* a fundamental misunderstanding of the nature of the problems that
object orientation is purported to cure.


An Examination of the Claims
----------------------------

Most of the authors beating the drums for object-oriented programming make a
variety of grandiose claims touting the supposed superiority of object
orientation over more traditional methods. Tim Korson [2] states that "the
object-oriented model supports the complete software development life cycle,"
but offers little evidence to suggest that it will surpass traditional methods.
Anthony Wasserman [3] claims that object-oriented structured design is "the best
way to design big, complex systems, no matter what language you program in" _
without explaining exactly how one is supposed to implement object-oriented
techniques in languages such as Cobol or Fortran. Adele Goldberg [4] even goes so
far as to claim that adopting object-oriented methods will "change how your
company operates."


"Not only were the colors and patterns of their material extraordinarily
beautiful, but the cloth had the strange quality of being invisible to anyone
who was unfit for his office or unforgivably stupid." [1]

Many authors seem to take it for granted that the object-oriented approach is
so superior to traditional methods that its benefits are obvious to anyone who
will only take the trouble to look for them. Korson refers to object-oriented
techniques as "natural." Ann Winblad [5] describes the case for object orientation
as "intuitive and compelling."

"And [the Emperor] ordered large sums of money to be given to both the
weavers in order that they might begin their work at once." [1]

Numerous authors state that object-oriented methods will lead to better designs
(Goldberg, Korson, Winblad), increase productivity (Goldberg, Winblad),
simplify maintenance and debugging, (Lieberherr [6], Winblad), reduce program
complexity, and reduce or eliminate software errors (Winblad).

One cannot escape the feeling that we have heard this all before: a method that
will "emphasize the importance of well-thought-out program design, increase
programmer productivity, reduce program complexity, facilitate program
debugging and maintenance, [and] encourage error-free coding." [7] It has been
described as "a major intellectual invention, one that will come to be ranked
with ... the stored program concept." [8] Quotations from the latest article on
object orientation? Hardly. These are descriptions of structured programming,
dating from the mid-1970s.

These are not the only claims being made for object-oriented methods that have
been heard in the past. According to Winblad, "the ease of building
object-oriented models and applications will attract people who would never
identify themselves as programmers ... With the knowledge woven into models and
class libraries, users will be able to build and extend applications." [9]
Similar allegations were made in the 1960s after the introduction of high-level
languages -- Cobol, because of its English-like syntax, was the subject of some
particularly extravagant claims in this regard -- and, more recently, in regard
to fourth generation languages. Winblad's discussion of programming by
end-users contains the startling assertion that these users "will not really
understand exactly what they are doing." [10] This statement is undoubtedly
true, although perhaps not in the sense that its author intended. It is not a
comforting thought, and should scarcely be regarded as justifying the adoption
of object-oriented methods.

According to some authors, object-oriented databases are more "complete" than
conventional databases. [11] They support "security, integrity, and versioning"
and "enhance programmability and performance" [12] -- all rather vague and
tenuous claims, offered with little supporting evidence. These claims are
essentially the same as those that were put forward in the 1980s for the
benefits of relational databases and structured query languages. This is
insufficiently extravagant for a few writers, who go on to claim that
object-oriented databases have the inherent ability to recover from media
failures [13] and "preempt the need for virtual memory paging!" [14]

The literature includes two assertions for object orientation that have not
been made for previous technologies: that object orientation allows data
systems to model the "real world" objects they represent more closely than is
possible with traditional methods, and that this improved modeling will lead
inevitably to better data systems (Khoshafian, Korson, Wasserman, Winblad).
Neither assertion is self-evident; unfortunately, none of these authors produce
any evidence to support either one. Nor do they cite any work by psychologists
or by experts in reasoning and cognition that would justify these claims. In
fact, a substantial body of research on the various psychological factors
influencing software development has existed for at least two decades. [15]
None of it supports these claims, and all of these authors seem unaware that
it even exists.

In short, the claims made for object-oriented methods are both original and
good -- but the claims that are good are not original, and the claims that are
original are not good. High-level languages, structured programming,
fourth-generation languages, artificial intelligence, and relational databases
have all been touted, at various times in the past, as bringing all of the
benefits now being claimed for object-oriented methods. What reason is there to
believe that object orientation will come any closer to fulfilling these dreams?


Drawbacks of the Object-Oriented Approach
-----------------------------------------

"After some little time had passed, the Emperor said to himself, 'I will
send my faithful old Minister to see how the weavers are getting along with my
cloth.' So the old Minister went into the hall where the men were working with
all their might at the empty looms. 'What can be the meaning of this?' thought
the old man. 'I cannot see the least bit of thread on the looms nor the least
bit of cloth woven!' However, he did not speak his thoughts out loud." [1]

Conspicuous by its absence in the literature is any mention of the drawbacks of
the object-oriented approach, or indeed any mention of the fact that there are
any drawbacks. A notable exception is a paper by Dewayne Perry, of AT&T Bell
Laboratories, describing the difficulty of adequately testing object-oriented
programs that make use of multiple inheritance and overriding of inherited
methods. [16] ("Inheritance" refers to the definition of an object or method in
terms of another object or method. Multiple inheritance is the definition of an
object in terms of several other objects; conflicts can arise if different
functions exist under the same name in two or more parent objects. Overriding
of an inherited method occurs when a child object redefines or overrides a
function specification that it inherited from one of its parents.) If the
problems created by these practices were not obvious to other authors, at least
the possibility that problems would exist should have been clear. Yet most
authors assume that these practices have no effect on testing methods -- a most
dangerous assumption. Winblad, for example, asserts that object orientation
"streamlines maintenance and lessens the likelihood of errors." This philosophy
is echoed by many other authors, none of whom provide any evidence to support
the assertion.

Testing problems are far from being the only drawbacks of object orientation
that authors are reluctant to discuss. Korson says that a feature of a class
"may be renamed, reimplemented, duplicated, voided, have its visibility
changed, or undergo almost any other kind of transformation" as it is inherited
by a derived class. Clearly, this ability is fraught with dangers, not only for
testing, but for development and maintenance as well. One might reasonably
expect the author to address those dangers, but his only comment is that
"inheritance can be misused."

One of the supposed strengths of object-oriented languages is polymorphism: the
ability of a variable to assume different data types (integer, string,
structure, etc.) at different times during the execution of a program. Dynamic
binding, or the assignment of data types to variables at run time (instead of
at compile time), is an obvious logical consequence of polymorphism. The
benefits of both polymorphism and dynamic binding are discussed at some length
by many authors (Korson, Khoshafian, Winblad, e.g.). These discussions exhibit
a puzzling failure to address the negative effects of dynamic binding: a
program having a large number of dynamically-bound variables can easily spend
enough time creating and destroying bindings to have a severe impact on program
performance. [17] These effects are well known, and have been described by other
authors in a non-object-oriented context.


Comparison to Traditional Methods
---------------------------------

"The men who were pretending to weave asked him very politely to be so
good as to come nearer, and them, pointing to the empty looms, asked him
whether the design pleased him and whether the colors were not very
beautiful." [1]

When comparing the supposed benefits of the object-oriented approach to
traditional methods, many authors overlook the fact that traditional methods,
when used properly, are capable of achieving the same benefits. [18] For
example, Lieberherr states that "ease of modification is one criterion that
characterizes a good object-oriented programming style." Ease of modification,
as any experienced programmer knows, follows directly from any good programming
style, whether structured or object-oriented. He then states that following his
recommendations "will result in good style, provided that the programmer
follows other well-known style rules such as minimizing code duplication,
minimizing the number of arguments, and minimizing the number of methods."
This is, of course, true _ but it certainly is not unique to object-oriented
programming. It has been well-known since the introduction of structured
programming in the 1970s that ease of modification is a direct consequence of
the use of a good structured style; this was, in fact, one of the major reasons
that structured programming was developed. [19]

Korson is enthralled with the ability of an object-oriented development
environment to support a library of classes and methods: "If higher level
classes are accumulated in a software repository, it would eventually be quite
likely that for almost any derived class, a generalization of that class would
already exist in the software repository." He seems unaware that most
structured development environments already provide this capability, through
the use of data dictionaries and code libraries.

Korson also provides a good discussion of message passing in an object-oriented
context, describing communication between classes. He would have his readers
believe that message passing is in some way unique to object-oriented
environments. But he inexplicably overlooks the requester/server model of
software design, which is built around message passing -- and is easily
implemented using traditional structured techniques. Neither message passing
nor the requester/server model is a new idea. Both have been extensively used
in transaction processing software for many years, and published descriptions
of both techniques are more than a decade old. [20], [21]

According to Winblad, object orientation encourages these strategies: "writing
reusable code, writing maintainable code, polishing existing code modules, and
sharing code with others." These are all laudable goals, to be sure. To imply,
as Winblad does, that they cannot be achieved without the use of
object-oriented methods, is to understate the capabilities of traditional
approaches to software development.

Korson provides a list of guidelines for designing classes in an
object-oriented environment. The guidelines are undeniably worthwhile. He seems
not to realize that they are just as valuable in a traditional structured
environment, if the words "procedure" or "system" are substituted for the word
"class."

Korson also manages to reveal inadvertently that the whole idea of
object-oriented analysis is really a sham anyway: "The object-oriented
requirements document uses objects and classification to blend traditional
analysis information about the required systems functionality with descriptions
of the objects it manipulates." In other words, the actual system specification
still relies on the traditional, procedural, function-oriented approach.


Disturbing Observations in the Literature
-----------------------------------------

There seem to be few seminal works in the literature on object orientation.
Most recent articles on the subject cite only a handful of references older
than a few years. More troubling is the circularity of many references: authors
cite each other's papers, their co-authors' papers, and even their own papers. Several authors, not content with this, cite their own unpublished
papers!

"'Dear me,' he said to himself, 'I must never tell anyone that I could not
see the cloth.'" [1]

Several cases have already been cited above, in which writers have exaggerated
the benefits of object-oriented methods, and understated or ignored the
capabilities of the traditional methods. Even more disturbing are the attempts
by several authors to bias their arguments in favor of object orientation by
misrepresenting the traditional methods:

魹ｽ Korson asserts that the traditional development life cycle is not
iterative [22] -- that it proceeds from analysis through design, coding, and
testing, to maintenance, never returning to a previous phase for refinement.
This contradicts Winblad's description of the traditional software life
cycle [23], and no wonder -- it isn't true.

魹ｽ Lieberherr dismisses structured programming as "the 'thou shalt not
use a GOTO' rule," never realizing that he has failed to grasp its central
concept: that the proper use of structured programming constructs renders the
GOTO statement unnecessary. [24] This was proven mathematically [25] in 1966,
and has been widely known for many years to practitioners of structured
programming. As Bohl put it, "to present the elimination of GOTOs as the whole
point of structured programming is getting the matter backwards. When the three
basic patterns of structured programming are used correctly, there should be
little or no need for GOTOs." [26]

魹ｽ Henderson-Sellers [27] claims that "a system envisaged as providing
a single service is unable to evolve ... with any degree of robustness." This
misrepresents not only the way systems are "envisaged" in the real world, but
also how they are maintained. He asserts that "in top-down design, the system
is characterized by a single function" and calls that "a questionable concept."
This is a questionable statement; when seen in the context of a typical
business environment, it is true only in the broadest possible sense. He
continues: "Top-down design is based on a functional mindset and consequently
the data structure aspect is often completely neglected." In a decade and a
half as a professional software developer, this writer has yet to see even one
experienced programmer who neglects the "data structure aspect" when developing
software.

These misrepresentations may not be deliberate, however. Rather, they may stem
from the appalling lack of practical experience possessed by most of the
authors cited in this paper. As shown by the biographies accompanying their
articles, most of them are either professors, doctoral candidates, or
consultants (one author is described as a "consulting methodologist") -- which
may account for their unfamiliarity with real-world software development. Very
few of these biographies mention any actual software development experience.
One notable exception is Dewayne Perry (cited above), who is (coincidentally?)
one of the few authors to discuss at any length any of the drawbacks of the
object-oriented approach.

Can Object Orientation Deliver on its Promises?
-----------------------------------------------


"'Well, Sir Minister,' said one of the weavers, still pretending to work.
'You do not say whether the stuff pleases you!' 'Oh! It is most beautiful!'
said the Minister quickly, peering at the loom through his spectacles. 'This
pattern and the colors! Yes, I will tell the Emperor without delay how very
wonderful I think them.'" [1]

Perhaps the most attractive facet of the object-oriented approach is its
promise to solve many of the problems of the current "software crisis." Of
course, high-level languages, structured programming, fourth-generation
languages, and relational databases were also claimed to solve the same
problems. We are told, however, that because of its radically different
approach to design and development, object orientation will succeed where the
older methods failed. Let's examine some of these promises.

Korson writes: "Inheritance is the most promising concept we have to help us
realize the goal of constructing software systems from reusable parts." This
is, quite simply, false. The most promising concept, indeed the only workable
concept, for achieving that goal is management support. In the absence of an
organizational commitment to the reuse of software modules, programmers will
continue to develop applications from scratch, regardless of the technical
environment.

Inadequate documentation is likewise the result of a lack of management
commitment. In the absence of proper documentation, technical changes in
analysis and design methods have little hope of success. The attempt to improve
documentation by making those technical changes is doomed before it starts.
What is required is an insistence by management on proper documentation.

Another author recommends "listen[ing] actively" as a means of identifying
classes and objects. This, again, is an attempt to apply a technical solution
to a management problem. The failure of analysts and designers to listen
actively to user's specifications is the major reason that software developers
deliver systems that fail to meet the user's needs. Analysts who are unable to
listen actively in structured analysis will not develop that ability overnight
with the introduction of object-oriented analysis techniques.

Goldberg appears at first to recognize the impossibility of applying technical
solutions to management problems -- "an organization must resolve many issues
before object-oriented technology can be successfully adopted" -- but in the
very next sentence, she begins to discuss organizational changes that she
claims will be brought about by object orientation: "object-oriented technology
impacts various levels of management ... changes the technical rules for all
programming team participants ... impacts the user's expectations ... [and] the
structure of the program development process."

Goldberg's astonishing claim that object orientation will "change the way your
company operates" has the cart before the horse. Organizational change is a
prerequisite to the adoption of object-oriented methods, not a consequence.

Later in her paper, Goldberg again appears on the verge of realizing the true
nature of the problems when discussing strategies for the reuse of software
modules: "managerial and technical support, as well as mutual cooperation, are
required... Developers must learn to overcome personal biases against reusing
artifacts they did not develop ... a long-term organizational commitment must
be made to the reuse process if it is to pay off." That is exactly right. All
of those changes must come first. Unfortunately, she shows in her final
paragraph that she still has the cart before the horse by describing these as
among the "key changes that object-oriented technology brings."

"'But the Emperor has nothing on at all!!!' said a little child. 'The
child tells the truth,' said the father. And so it was that what the child said
was whispered from one to another until all knew and they cried out together,
'BUT HE HAS NOTHING ON AT ALL!!!'" [1]

When the only tool one has is a hammer, everything in the world looks like a
nail. The literature on object orientation is full of papers which were written
by technical software experts who see technology as the solution to all
problems in software development. Goldberg, Winblad, and other authors list
many organizational changes that they claim will result from the adoption of
object-oriented development methods. In fact, any organization that is capable
of making the changes they suggest doesn't need any new methods.

Just as earlier attempts at solving the "software crisis" failed, object
orientation will fail also, and for the same reasons -- not because of any
deficiencies inherent in the methods, but because the most serious problems
plaguing business software development are not technical problems, and cannot
be solved by technical means. The problems we face are management problems,
with management solutions. They will be solved only when we as software
developers and managers are willing to make the difficult commitments needed to
keep our users satisfied throughout the software life cycle: commitment to
really listen to them, so that we develop the software they need; commitment to
creating libraries of reusable code, so that we can develop that software
quickly; commitment to high-quality software, so that they can rely on the
integrity of the data we provide; and a commitment to keeping proper
documentation, so that the data systems we develop can evolve as the user's
needs evolve.


What we need is not object orientation, but customer orientation.


"The Emperor felt very silly for he knew that the people were right but he
thought, 'The procession has started and it must go on now!' So the Lords of
the Bedchamber held their heads higher than ever and took greater trouble to
pretend to hold up the train which wasn't there at all." [1]


References
----------
1. Andersen, H. C. The Emperor's New Clothes, Houghton-Mifflin (1949).
2. Korson, T. and McGregor, J. D. "Understanding Object-Oriented: A
Unifying Paradigm," Communications of the ACM (Sept. 1990).
3. Wasserman, A. I. and Pircher, P. A. "Object-Oriented Structured Design
and C++," Computer Language (Jan. 1991).
4. Goldberg, A. and Rubin, K. S. "Taming Object-Oriented Technology,"
Computer Language (Oct. 1990).
5. Winblad, A.L., Edwards, S. D., and King, D. R. Object-Oriented
Software, Addison-Wesley (1990).
6. Lieberherr, K. J. and Holland, I. M. "Assuring Good Style for
Object-Oriented Programs," IEEE Software (Sept. 1989).
7. Bohl, M. Information Processing, Science Research Associates (1976).
8. McCracken, D. D. "Revolution in Programming," Datamation (Dec. 1973).
9. Winblad, op. cit., p. 49.
10. Ibid.
11. Ibid.
12. Khoshafian, S. and Abnous, R. Object Orientation, Wiley (1990), p. 258.
13. Ibid.
14. Winblad, op. cit., p. 111.
15. Brooks, R. E. "Studying Programmer Behavior Experimentally: The
Problems of Proper Methodology [list of references]," Communications of the ACM
(April 1980).
16. Perry, D. E. and Kaiser, G. E. "Adequate Testing and Object-Oriented
Programming," Journal of Object-Oriented Programming (Jan. 1990).
17. Pratt, T. W. Programming Languages, Prentice-Hall (1984).
18. Ledgard, H. F. and Cave, W. C. "Cobol Under Control," Communications
of the ACM (Nov. 1976).
19. Donaldson, J. R. "Structured Programming," Datamation (Dec. 1973).
20. Tandem, Cobol User's Guide, Tandem Computers (1985). [Originally
published as Cobol Programming Manual (1977)]
21. Tandem, Guardian Operating System Programmer's Guide, Tandem Computers
(1985). [Originally published as Guardian Programming Manual (1977)]
22. Korson, op. cit., p. 41.
23. Winblad, op. cit., pp. 204-209.
24. Dijkstra, E. W. "Go To Statement Considered Harmful," Communications
of the ACM (March 1968).
25. B魹ｽhm, C. and Jacopini, G. "Flow Diagrams, Turing Machines, and
Languages with only Two Formation Rules," Communications of the ACM (May 1966).
26. Bohl, op. cit., p 243.
27. Henderson-Sellers, B. and Edwards, J. M. "The Object-Oriented Systems
Life Cycle," Communications of the ACM (Sept. 1990).


Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

#### ↳ Re: The Programmer's New Clothes

- **From:** "rth..." <ua-author-12495133@usenetarchives.gap>
- **Date:** 1996-10-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cd9ae5a39-p2@usenetarchives.gap>`
- **In-Reply-To:** `<545omu$ck9@news.inetdirect.net>`
- **References:** `<545omu$ck9@news.inetdirect.net>`

```

I have been studying and practicing structured programming for about 14 years
now. In small environments and in the very large. I would tend to agree that
many of the real problems are not technical, but environmental/interpersonal/
interprocess related. It might be that claims of benefits WILL be a catalyst
for changes in those areas. But I would prefer this to be explored honestly,
rather than treated covertly by those espousing the new technology.

Is there a crisis in the software development industry? All the shops I have
been involved in, including the small ones, were reasonably applying the
concepts of structured design and development. Some were doing this even
in the absence of a formal, documented methodology. Maybe because customer
orientation was to them an obvious ingredient to their success. Maybe because the
developers, through experience and, in the interest of self preservation in the
face of increasing demands for new functionality, figured out flexible code
design to build libraries (both copybooks and subprograms) was needed. It
does take time to build and become aware of an existing base of code, both
in-house developed and commercially available. But, this is inescapable. Try
to do object oriented development without knowledge of the class library which
comes with the compiler, and those derived or developed in-house!

That said, I have seen enough so that I do believe that there are benefits to
the object-oriented technologies. But I must admit that I have heard very
little, and READ of none of the pitfalls. The testing of inheritence was one
thing you mentioned that did give me reason for pause. Like may things of
a tech nature, we just assume we can trust the implementors of those
facilities, much like we have trusted the marketers of commercial libraries.

But many of us would have to admit we do not like putting ourselves in that
position, and in the past have demanded at least the option of purchasing the
source code! More and more, we rely on the underpinnings of others. In fact,
when you think about all the layers we rely on as developers, it is astounding
things work as well as they do! But, I digress; should we be less trusting
of these technologies and their implementors?

If there is a real crisis, it may be because of the shift from centralized
computing to decentralized. This introduction of common, daily interactions
among multiple heterogeneous platforms forces the interaction of the people
who support those platforms. In some cases, the degree of maturity and
diversity of experiences of the individuals leads to a "clash of cultures"
which can become frustratingly futile, not only to those directly involved, but
to the organization as a whole, which looks for an easy solution or a
common enemy to enable unity. Such technology and vendor diverse
environments increase the complexity of problems by magnitudes!

If you think code reuse is tough to sell, imagine philosophy reuse!!!!
(By the way, although I have spent time working
on legacy/mainframe, midsize, micro, and handheld computer platforms, I am
primarily a microcomputer developer. I believe for development,
microcomputers are the ticket. However, over time, having to support
the end result in the bigger ocean of the large organization, I have come to
appreciate the lessons offered by the simple scale/largeness of other platforms.
It is a mistake to ignore wisdom being offered for free by well meaning people
who share a common goal - success of the organization!)

I have been trying to spend some time becoming familiar with this "new"
approach and associated development tools. As I have become most
comfortable with COBOL, I was looking to learn only the differences, to
deal with the smallest delta possible. So, I have purchased the "Introduction
to Object Orientation for COBOL Programmers" (or something like that) from
MicroFocus. I have also purchased thier Object Cobol compiler (for OS/2).
>From what I have read so far, it is not only a good treatment of how good
COBOL development is done, but also on how OO can make some historically
frustrating things easier. However, thus far, it has not really outlined the
associated concerns/pitfalls accompanying some of these benefits. Maybe
it covers these enmass in a chapter dedicated to such.....

Thanks for your "doubting Thomas"/"show me" attitude. I really appreciate
your posting this material. For me, it is timely. I look
forward to hearing responses from other more informed individuals like
yourself. I would especially appreciate reading a response from the author of
the book I am using to familiarize myself with this stuff (Mr. Orr of
Micro Focus?). Any MicroFocus employee should know of this work and could
forward these entries to him, I would think.......

Thanks,
Robert Thelen
```

#### ↳ Re: The Programmer's New Clothes

- **From:** "kevin j. hansen" <ua-author-17072510@usenetarchives.gap>
- **Date:** 1996-10-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cd9ae5a39-p3@usenetarchives.gap>`
- **In-Reply-To:** `<545omu$ck9@news.inetdirect.net>`
- **References:** `<545omu$ck9@news.inetdirect.net>`

```

It's about time someone questioned the validity of Object Oriented
Programming.

Having been in COBOL from big mainframes through PCs for around 25 years,
I've seen plenty of new programming "paradigms" come and go. All of them
promised to revolutionize software development, but none really delivered.
Some, like Structured Programming, introduced fundamentally sound and
intuitively obvious (well, they were after someone suggested them) concepts
to the profession.

Those of us who are where the rubber meets the road are pragmatists. Our
first job, after all, is to get the job done. Adopting certain techniques
of design and coding makes this easier. Sure, we occasionally use a GO TO.
So what? "Pure" structured code can be more confusing than the
judiciously coded GO TO, so why not be reasonable about it.

One of the most important attributes of COBOL is that you can grab a
reasonably warm body off the street and get them productive in a
maintenance environment. Assuming the original code is reasonably well
written. (Try that in a C language shop!)

At the risk of revealing my thick-headedness, I must admit that I have had
a very difficult time grasping what OOP is, in the real world. The
introduction of un-obvious terminology and somewhat abstract definitions
thereof just serves to further obfuscate the issue. If an old fart like me
can't get his arms around OOP, how are you going to teach it to a new
programmer? I have observed that all proponents of OOP make a point of
mentioning that it "requires a completely new mindset" and "will involve a
steep learning curve". So, if OOP is so swell, how come it's so hard to
figure out?

Much of OOP revolves around what is essentially a library of objects which
are coded by some OOP gurus in a black box somewhere. How is this going to
work, when most shops are unable to develop, maintain, and enforce the use
of any other standard program modules developed in-house?

Seems to me that well designed data structures supported by straightforward
code will better serve the profession.

I have noticed that the proponents of OOP always select rather simplistic
transaction-processing types of examples (e.g., a checking account). Well,
the real world introduces many complications to the processing required.
OOP doesn't IMHO address even common things like batch processing (how
efficient will it be to have to call an account object and ask it to print
itself and somehow keep running totals for your report, for example)?

An excellent paper, Doug.

Kevin J. Hansen
NORCOM - Developers of COBOL Programming Tools
ScreenIO screen manager, NORCOM Date Routines, COBCLEAN code reformatter
http://www.alaska.net/~norcom
```

##### ↳ ↳ Re: The Programmer's New Clothes

- **From:** "la..." <ua-author-1928616@usenetarchives.gap>
- **Date:** 1996-10-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cd9ae5a39-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9cd9ae5a39-p3@usenetarchives.gap>`
- **References:** `<545omu$ck9@news.inetdirect.net> <gap-9cd9ae5a39-p3@usenetarchives.gap>`

```

There are two formidable intellectual issues which must be resolved
before objects (or, for that matter, standard code libraries of any sort)
come into general use and begin to realize their promise.
1) An absolutely standard way (symbolic or in ordinary language) of
describing exactly what the object does and how it does it (so a potential
user can be sure that the object is in fact the right one for the
requirement under consideration)
2) An equally standard method of storing them so that they can be
discovered according to the description in (1).

Otherwise, we won't be able to find a suitable object at at all, and if
we do find one that looks promising we won't know if it's what we need. I
may be looking for an object that does standard payrolls for Manitoba, but
I also want to be sure that it handles our "bring four pounds of
smallcoals in the cold weather" deduction (which only fourteen other
companies in Manitoba have) properly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
