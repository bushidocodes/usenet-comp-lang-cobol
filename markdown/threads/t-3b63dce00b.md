[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO Classes - Public Domain Source code

_7 messages · 4 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO Classes - Public Domain Source code

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C9DC1E.F99A067C@home.com>`

```

Public domain OO class source with specific reference to the sub-set
which covers collections/dictionaries..

For starters let's take our COBOL flat-file verbs - 

  Close, delete file, delete record, Open input, open i-o, open output, 
read,  read next, read previous, rewrite, start , write

 - a total of 12 which quite happily suits us for
mainframes/minis/desktops. Regardless of the mechanism that each
compiler uses, the verbs return the same result. There is a compiler sat
out there, can't remember its name, but they have introduced
non-Standard verbs for file handling. Unless you are certifiable, you
would be crazy to even contemplate using that compiler, regardless of
any other benefits it offers - total lack of compatibility with all the
other flavours of compilers.

Now let's move on to public domain OO classes. In concept, Newbury May
2000 is supposed to give us the official blessing for OO - but there is
as yet no commitment on what any common classes should/would contain. My
immediate concern is with the group called collections/dictionaries. So
I'll take the Merant(NetExpress) classes, Thane has told me Fujitsu also
has collections/dictionaries, so we'll see what he comes up with. As a
third contender, there is that mystery compiler, Hitachi OO COBOL, which
also has collections/dictionaries.

The Merant List - the following is a rough count per class, and although
separated out I haven't bothered to illustrate the branches of the tree.
This group is subordinate to Dependent which in turn is subordinate to
Base. For subordinate read 'inherits from'. What these specific classes
and methods do is irrelevant. It is the concept of orderly systems
documentation which is my concern. In theory someone might contend that
the Merant list is unnecessarily 'verbose', they can do the same thing
with a lesser number of method-names. Again that is irrelevant and
merely side-tracks, the typical nonsense that occurs in large committee
meetings. (Truly, only a triumvirate committee works effectively, a
record keeper and two others discussing; agreement is arrived at by the
trio).

The number of Method-names are shown for each class. (if you have
difficulty with the concept, think of an OO Class as being a public
domain structured program with common paragraph-names, so that
developers easily remember which paragraph-names to call/perform).

Base
    Dependent

	Collection			44

	Bag				10
	Ssequencedcollection		37

	ArrayedCollection		36

	Array				38

	ByteArray			76
	CharacterArray			84

	dynamicArrayedCollection	52

	orderedcollection		61
	sortedcollection		58

	ValueSet			13

	dictionary			37

	identitydictionary		38
	SymbolTable			38

	IdentitySet			13

		TOTAL	               635

From browsing NetExpress GUI classes, I am aware that there are methods
with the notation "This method is retained for backwards compatibility,
use method-w". I don't think the above group is affected by that
situation, but assuming it is let's deduct 10% of the methods. It is
also a factor in any class, vendor or developer written, that there will
be methods 'PRIVATE' to the particular class. That is, this method is
invoked only within the class. You the developer may invoke
MyCollections "method-a" which may in turn invoke self "method-x"
"method-y", "method-z".	Merant documentation is typically marked "This
method is PRIVATE do not invoke directly". On this basis, I've no
numbers so we'll reduce the list of method names by 50% :-

							635
		Less 10% backwards compatible		571
		50 % to allow for PRIVATE		286

On that basis we have the possibility of 286 different method-names the
developer can invoke for JUST collections/dictionaries. (The true number
is probably around 300 - 400). As a user I may well only employ 10-20%
of this number, and the names are not lodged in my 'memory-box' for
instant recall.

We know that Fujitsu and Hitachi also have collections/dictionaries; for
now, discount the other vendors, that only adds to the confusion. Now it
just so happens that Fujitsu, Hitachi and Merant have hit on using the
exact same names for method-names in classes that perform the same
functions - who is kidding who ?. There is the possibility of having :-

 Total permutations for likely method-names = 
 
		n * v 	where n = 286 and v = number of vendors

No matter, I only use NetExpress, so I'm not really concerned. But if
you change jobs, now you could be confronted with a fresh set of 286
method-names and in all likelihood the results returned from the methods
may will differ too. In practical terms, do developers really want to
re-learn a list (might contain 250-300 on average per vendor).

Is there a way out of this potential mess - Yes. Through Standards
committees a consensus on a common set of method-names. This in no way
restricts compiler vendors, they may produce less support by offering
fewer, or more methods over and above the current Standards list.
Somebody will observe, "But we already have a large customer base using
our existing method-names".

Back to our three vendors and they use different method names to do the
same thing :-

	Fujitsu		"get-a-name"		"return-a-name"
	Hitachi		"set-nameobject"	"return-a-name"
	Merant		"get-a-name"		"return-asObjectName"

If this is going to work there has to be general agreement that if the
method names "get-a-name" and "return-a-name" are classified as being
the common standard, then both Hitachi and Merant have to make changes.
Is that insurmountable ? The very simple answser is 'No' using the
following technique which is already in use :-

	(a) existing developers will be attuned to "return-asObjectName"
		and will continue using it.
	(b) New developers, consulting the index of method-names 
		available would pick up on "get-a-name"

	Merant Collection Class :

	*>-----------------------------------------------
	Method-id. "return-asObjectName".

	*> This method is retained for backwards compatibility - use 
	*> "get-a-name"
	*>--------------------------------------------------------
	Linkage section.
	01 n				pic x(4) comp-5.
	01 lnk-name			object reference.
	Procedure Division using n returning lnk-name.
	   invoke self "get-a-name" returning lnk-name
	End Method "return-asNameObject".
	*>---------------------------------------------------

	*>---------------------------------------------------
	Method-id. "get-a-name".
	*>-----------------------------------------------------------
	Linkage section.
	01 n				pic x(4) comp-5.
	01 lnk-object			object reference.
	Procedure Division using n returning lnk-object.
	   invoke os-Collection "at" using n returning lnk-object
	End Method "get-a-name".
	*>-------------------------------------------------

Now does that look at all complicated to achieve a common
systems/programming document base to achieve portability using public
domain source code ? OK, you are reading this and say "Who cares,
goddamned OO again - forget it". That really isn't the issue - too late
now for COBOL 200x, but by getting involved we might, just might get a
smoother update to COBOL 2005 if and when it happens. And this concept
established as the norm has to have side benefits for other modules in
COBOL.

If you can see any merit in this, and particularly if you are not using
OO, why not try it out on your national J4 members ? If you can see the
sense of it and they become 'iffy' then I suggest you should be asking a
big "WHY ?" and don't be satisfied with a shrug off.


Jimmy
```

#### ↳ Re: OO Classes - Public Domain Source code

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C9F914.B9E7DFAF@iinet.net.au>`
- **References:** `<38C9DC1E.F99A067C@home.com>`

```

"James J. Gavan" wrote:
> 
> On that basis we have the possibility of 286 different method-names the
…[4 more quoted lines elided]…
> 
To me, this strikes right at the heart of OO.
300-400 FUNCTIONS to be remembered. I find it difficult enough to
remember all the normal COBOL syntax plus standard COBOL function names.
Now you want me to remember another 300-400 names.

This is patently ridiculous.
Eventually, OO programming bogs down in the area of which method/Object
to use and is there one that will do the job.

I have not heard of any solution to this problem.
Often it is quicker to write the code yourself than to search the
methods for something that might do.

I have a notion that OO has the right idea but TOTALLY missed the point
about re-use.
Programs follow generic patterns or templates. For example a windows
program should always have a thread devoted to Window manipulation and a
thread that actually does the work the user requested. A Merge program
is generically the same no matter how many files are involved. A
Transaction update has a pattern that matches other transaction updates.

What is needed is a set of these patterns that can be cloned and THE
BUSINESS LOGIC added to perform the specific function.

I would much rather see a set of generic programs being delivered that
can be copied and updated.

Now the challenge for the language is how to make that tailoring
simpler. The answer lies in statements directed to the editor as to
where to expect changes and where changes might reasonably be
discouraged.

Once some experience with this type of programming has been achieved,
maybe enhancements to the language can be made to ease the effort of
using patterns.

I would like to see something like:

IDENTIFICATION DIVISION.
 PATTERN SECTION.
  PATTERN NAME (IS) STANDARD-MERGE
   USING 2 INPUT-FILE
   USING 1 OUTPUT-FILE.
 PROGRAM-ID. MYMERGE.
.
.
I-O SECTION.
FD INPUT-FILE-1
   .
   .
FD INPUT-FILE-2
   .
   .
FD OUTPUT-FILE-1
   .
   .
PROCEDURE DIVISION.
MERGE-SELECTION-CRITERIA SECTION.
   logic to determine whether to merge or not.

The compiler would know how to take the above statements and merge them
with the STARNDARD-MERGE pattern which contains other COBOL statements
and produce a workable program. 
```

##### ↳ ↳ Re: OO Classes - Public Domain Source code

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CA90E8.416E366C@home.com>`
- **References:** `<38C9DC1E.F99A067C@home.com> <38C9F914.B9E7DFAF@iinet.net.au>`

```


Joseph Katnic wrote:
> 
> "James J. Gavan" wrote:
…[7 more quoted lines elided]…
> To me, this strikes right at the heart of OO.

DAMMIT IT RIGHT OFF THE BAT YOU GO OFF AT A TANGENT. Ignore the bloody
OO and whether or not you think it is viable - I'm addressing the issue
of the STANDARDS and a standardized approach to what compiler vendors
give you and me. 

It just so happens that the OO is an issue which standards haven't
resolved and unless we get actively involved - just like Bill Klein's
oft repeated concerns, that COBOL 200X is over-blown, then COBOL
2005/2010 will similarly not address our needs, we the developers who do
the grunt work - and presumably who are supposed to benefit from the
standards. Forget about your perception of OO - concentrate on the
standards. Just like file handling verbs I want some consistency in the
various modules that vendors produce - so that you and I can swap code,
yes, not just OO, but STRUCTURED. 

And if anybody else jumps in and wants to wax forth about OO - I could
care bloody less - PLEASE, concentrate on the Standards issue.

Now back to your points about OO - agreed it does seem like overkill -
and there is no way you or I can memorize 100, let alone 300 method
names. View it from the perspective that you have bought a series of
non-OO packages, to do things like forecasting, graphics, bar-charts -
you name it.

These packages are replete with features. Probably there is no way you
are ever going to use all those features (call modules) tied into a
specific application of yours. So you do a cursory look at the
introductory material to get an overall feel.

Assume you are a lawyer, (God forbid !), and rather like lawyers with
there shelves of case-law books, you build up a vague memory-bank 
of what's available. No, you don't dive for a specific book, but given
the topic, that initial reading of yours does allow you to zero-in on a
particular area. So then you go through the index to find exactly what
you are after.

So back to EDP and my packages above - same applies with OO. I doubt I
use 10% of methods available. Should I want to bugger around with
bitmaps, icons, then I know there are a set of classes covering the GUIs
(in NetExpress). This is the first time I'm doing it, so now I reference
the specific class to check out the methods available to me. Ignore the
OO - and think back to the packages I suggested - does that seem an
unreasonable approach - that somebody should provide you with pre-canned
stuff that you reference as you have a need !

And in concluding your message you write, "I would like to see.....".
Maybe you would but it isn't going to happen because you would like it.
Get beyond "I would like....", addrss your concerns now or for the
future of COBOL to your J4 participant ! In this particular context, I
recently wrote, that's like saying, "I don't bother to vote, but I think
the government is doing a lousy job".

Jimmy
```

###### ↳ ↳ ↳ Re: OO Classes - Public Domain Source code

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CB9BB8.951E1A0E@iinet.net.au>`
- **References:** `<38C9DC1E.F99A067C@home.com> <38C9F914.B9E7DFAF@iinet.net.au> <38CA90E8.416E366C@home.com>`

```

"James J. Gavan" wrote:
> 
> DAMMIT IT RIGHT OFF THE BAT YOU GO OFF AT A TANGENT. Ignore the bloody
…[3 more quoted lines elided]…
> 
OOPS,
Sorry to yank your chain. I forgot to look at the thread title.
My comments still apply whether there are a standard set of
methods/objects or not.
However, Standards are a VERY important method for alleviating the
problem.

I agree that it is probably better to have a public "library" of
objects/methods than to let each vendor create their own standard. The
Standards bodies, would probably take too long to determine the
appropriate standard in an very fluid and evolving environment.
The time for the standards body is later when a practical consensus has
been reached.

I have used SMALLTALK and JAVA. I am looking at the COBOL implementation
of OO.

You do realize that the compiler vendors have to offer differences in
their compilers. Otherwise how would they compete, on price alone -
don't make me laugh.
This is one of the reasons it takes so long for the standards to be set.
It takes some time for the various vendors to ensure that their
implementation is included in the standard.

One of the best things about the current computing environment is the
emergence of OPEN source code. Not that I'm interested in writing
operating systems (LINUX) or compilers.
However, there are people who are interested in doing those things. I
suggest that this is the approach that would probably work best. WHO
sets the standard for LINUX?
Does LINUX evolve faster than an ISO standards committee would allow?
You betcha.

I suspect that OPEN source may eventually see the death of standards
committees in the software arena, and probably this will be a good
thing.

So, public domain OPEN Source code OO classes for COBOL would be a good
thing. BUT, someone must OWN the source (like Linus Torvalds does for
LINUX) so that a decision can be made when to modify the OPEN Source
officially. 

Who is going to OWN the code? Which set of CLASSES do you use as a
model?
Can you use any of the vendors classes as a model? Will you infringe
copyright?
```

###### ↳ ↳ ↳ Re: OO Classes - Public Domain Source code

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCD290.34B41584@zip.com.au>`
- **References:** `<38C9DC1E.F99A067C@home.com> <38C9F914.B9E7DFAF@iinet.net.au> <38CA90E8.416E366C@home.com> <38CB9BB8.951E1A0E@iinet.net.au>`

```
Joseph Katnic wrote:
> 
> Who is going to OWN the code? Which set of CLASSES do you use as a
> model?
> Can you use any of the vendors classes as a model? Will you infringe
> copyright?

These are excellent questions.

1.  Copyright.  GNU software requires a release form from your
employer to remove this issue when you submit major amendments to
source.  They have had to remove a significant part of one product
once due to copyright.

2.  Ownership.  There must be a central controlling body for the code.
This typically would be the person that originates it.  CVS
repositories are the method of choice to store it with only authorized
check in (i.e. Linus's lieutenants for Linux).  If you want to make a
change and are not directly authorized you submit the change to the
group for acceptance and typically it is accepted, although it may be
modified to meet group standards.

I would hope we can find a friendly Unix person to give us a CVS
pserver, and the rest is (future) history.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: OO Classes - Public Domain Source code

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CB658E.7CF5A2AF@zip.com.au>`
- **References:** `<38C9DC1E.F99A067C@home.com> <38C9F914.B9E7DFAF@iinet.net.au>`

```
Joseph Katnic wrote:
> This is patently ridiculous.
> Eventually, OO programming bogs down in the area of which
…[12 more quoted lines elided]…
> other transaction updates.

OK let's take this back a step.  I cannot talk specifically about the
interfaces defined (I don't have Documentation, any on the web?)

When we talk about a collection we talk about a consistent interface
that is implemented slightly differently for ordered and other
incarnations.  The methods for an ordered and unordered set are the
same just with some features specific to that improvement.

When you use an unordered set in a program and test it, it works fine
but the output is out of order, the solution is simple change the
object that is created in the beginning and the rest simply does not
change.

So what we come down to is that we must learn a standard interface for
collections, and how to create different instances of ordered sets and
dictionaries.  This is the premise of OO.

Regarding OO and reuse.  When we initially define an unordered
collection we create all the methods that we need to access any
collection, when we extend that we add features onto that standard
interface.  This is what it is all about.

This brings down the methods to about 34 with the functions performed
slightly modified to reflect the type of collection.  (34 sounds high
to me, really would like to see some Doco).

The promised reuse of OO has come about very slowly, there are some
very successful frameworks available.  The reuse is more at a business
level.

> What is needed is a set of these patterns that can be cloned and THE
> BUSINESS LOGIC added to perform the specific function.

The business logic is often the thing that is consistent between many
different applications of the logic.  OO gives you the ability to
provide a logic object that contains the business logic.


> I would much rather see a set of generic programs being delivered
> that can be copied and updated.
…[4 more quoted lines elided]…
> discouraged.

With Procedural code you build the lowest level and reuse that, in OO
you can build the highest level and replace the lowest level easily by
inheritance and replacing the working methods.

For example:  I am defining a complex sort algorithm.  The stats are
collected for all records, the sort is optimized, then the sort is
applied reading multiple records.

The problem is that in one instance I have to rewrite the file in the
correct order directly, in another I need to read the input file
sequentially and write a key on the output record. Output is the
lowest functionality of the system.  If I define this as an object I
create an interface with writing records in the revised order as the
base class case, I then override it with the special case of keeping
the order.  This is very similar to call back where you want to
replace default functionality with something new.

> Once some experience with this type of programming has been achieved,
> maybe enhancements to the language can be made to ease the effort of
> using patterns.

Analysis patterns are exactly this.  More than program skeletons,
common logic solutions that often require tailored programs to
implement.

> I would like to see something like:
> 
> IDENTIFICATION DIVISION.
>  PATTERN SECTION.

I would love to see this.  This is templates as C++ calls them.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: OO Classes - Public Domain Source code

- **From:** Karl Kiesel <karl.kiesel@mch6.siemens.de>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE18BE.58018949@mch6.siemens.de>`
- **References:** `<38C9DC1E.F99A067C@home.com>`

```
James J. Gavan schrieb:

> The number of Method-names are shown for each class. (if you have
> difficulty with the concept, think of an OO Class as being a public
…[8 more quoted lines elided]…
> 

Just did a quick look at WD1.4 (june 1996), that still contained the
proposed Standard classes:
it is not as horrible as that, but there are still 35 classes (nested 5
levels) subordinate to the base class with 105 methods alltogether (I
did count all specified methods, even if the name was the same, did not
care for any errors in the specification); 3 classes accounted for 30%
of these methods. 

Karl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
