[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Constants, Static, Public, Private

_54 messages · 14 participants · 2006-03 → 2006-04_

---

### Constants, Static, Public, Private

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-15T20:27:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
I'm still on the tack "Is FACTORY really necessary ?".

CONSTANTS :

The only reason I'm referring to Constants is to get a handle on the
word 'static' when used in Java. A short, sharp definition - CONSTANTS
are cast in stone. Moses came down from Mount Sinai with two tablets and
the ten entries can't be changed.

Constants were introduced by J4 as a part of COBOL 2002 - a short
version. The situation currently :-

-------------------------------------
1) J4 - Chuck Stevens has since produced a more detailed paper expanding
the syntax - presumably will be part of COBOL 2008 ? He can expand, if
he sees fit - perhaps highlighting which of my M/F Level 78 examples
below, will be available as part of the Standard.
-------------------------------------
2) NetCOBOL - (only just twigged, going to their site, that's the name
for what used to be Fujitsu COBOL)

- The CONSTANT SECTION defines constants used by a  COBOL program.
Values specified in the CONSTANT SECTION do not change (?)  during
program execution. The section header of the CONSTANT section is
followed by 77-level description entries and/or record description entries.

- NetCOBOL also has a feature to use M/F Level 78's below - referred to
as 'Micro Focus named-literals' - whether it functions in the same way,
only somebody using F/J could tell us.

---------------------------------------------------------------------
3) Micro Focus - Accessing both the N/E V 3.1 and 4.0 on-line manuals
there  is no reference to 'Constants', as yet.

Longer than I have been using M/F, there has been, as an extension,
Level 78's. I'm sure M/F must have suggested it as an amendment to the
Standard a long time ago - but it was never picked up on - but Fujitsu
did ! M/F Examples :

        WORKING-STORAGE SECTION.

        78 DN             value 20.    *> DN = DogNameLength
        78 TL             value 28.    *> TL = TextLength
        78 ML             value 30.    *> ML = MethodNameLength
        78 ThisNumber     value 123.45.
        78 myWorld        value 'Hello World'.
        78 MyTextLength   value 100.
        78 MaxTableSize   value 10.
        78 MaxGadgets     value 20.
        01 MyTextEntry    pic x(MyTextLength).

        Here I am passing parameters/properties to my Dialog Template :-

        01 ws-a.

        *>  Entryfields         ID   Seq Len X DF R C F P V
        *>                      IIII,SSS,LLL,X,NN,N,N,N,N,N,
          05.
            10 pic x(TL) value '0301,001,006,0,00,2,0,0,0,0,'.
            10 pic x(ML) value 'EF-CheeseCode'.

          05.
            10 pic x(TL) value '0302,002,020,3,00,0,0,0,0,0,'.
            10 pic x(ML) value 'EF-CheeseName'.

        *> Coloured Droplist ----------------! (Note '4' below)

          05.                         *>     * **
            10 pic x(TL) value '0303,003,030,4,01,0,0,0,0,0,'.
            10 pic x(ML) value 'DL-CountryName'.

          05  etc........

        01 ws-B redefines ws-A.
           05 ws-C occurs MaxGadgets pic x(58).

        *>Note : Could have used continuation character above, but easier
        *>to align with two Level 10 entries. For editing purposes,
        *>(expanding/contracting) as appropriate, just change the values
        *> for TL, ML, or MaxGadgets ONCE !

        01 DogTableA.
            05 pic x(DN) value "Border Collie".
            05 pic x(DN) value "German Shepherd".
            05 pic x(DN) value "Labrador".
            etc......
        01 DogTableB redefines DogTableA.
            05 Dogname  occurs MaxTableSize pic x(DN).

        01 BirdTableA.
            05 pic x(DN) value "Chaffinch".
            05 pic x(DN) value "Blue Jay".
            05 pic x(DN) value "Robin".
            etc......

         *> There is no BirdTableB in this example

        PROCEDURE DIVISION.

        display ThisNumber
        display MyWorld
        compute aLength = function length(MyTextEntry)
        compute a = b + ThisNumber

        perform varying n from 1 by 1 until n > MaxTableSize
          display Dogname(n) *> displays dog breed
        End-perform

        *> For Oliver : deceptive, but the literals in the tables above
        *> aren't Constants, 'well sort-of',  providing they aren't
        *> changed, but see below  :-

        *> assumption is the two Tables are identical, i.e.
        *> element sizes and occurs clause :-

        move BirdTableA to DogTableA
        perform varying n from 1 by 1 until n > MaxTableSize
          display Dogname(n) *> displays bird
        End-perform

Bill - I believe you quite like the Level 78s - can you think of any
'gimmicks' I haven't covered ? (Same goes for Rick).

STATIC :

1. The first thing I picked up on :-

class Example1 {
   public static void main(String args[]) {
     System.out.println(*This is the output from Example1*);
   }
}

And the accompanying text dissected the above. Looking for something
else I accidentally tripped over Frank's IBM AIX on-line manual, which
he has already referred to. Worth quoting in more detail because it
really spells it out :-
-----------------------------------------------------------------------

- COBOL instance methods are equivalent to public nonstatic methods in Java.
- COBOL instance data is equivalent to private nonstatic member data in
a Java class.
- You can access COBOL object instance data only from within COBOL
instance methods defined in the class definition that defines the data.
- You can initialize object instance data with VALUE clauses or you can
write an instance method to perform custom initialization.

- COBOL factory methods are equivalent to public static methods in Java.

Note next one well :-

- A factory method cannot operate directly on instance data of its
class, even though the data is described in the same class definition; a
factory method must invoke instance methods to act on instance data.

I agree next, but don't do it this way, although I did initially :-

- COBOL factory methods are typically used to define customized methods
that create object instances. For example, you can code a customized
factory method that accepts initial values as parameters, creates an
instance object using the NEW operand of the INVOKE statement, and then
invokes a customized instance method passing those initial values as
arguments for use in initializing the instance object.

- COBOL factory data is equivalent to private static data in Java.

- You can access COBOL factory data only within COBOL factory methods
defined in the same class definition.

I didn't find any reference in AIX to the word CONSTANT.

In checking AIX, F/J(NetCOBOL) or M/F I didn't find any specific
references where Instance methods can access FACTORY data.

--------------------------------------------------------------------------

Now what above says to me is, that although FACTORY is not a Reserved
Word in Java, in fact you have a 'Dummy Factory' and that you are
'forced' to have a 'Dummy Factory' because all Java programs begin
execution at "main()" in the 'Dummy Factory' ???

Taking the above Java example it will compile and run because it is the
only method in the 'Dummy Factory'.

2. Java Variables :

Real hazy on this bit - would require more reading to absorb. I can
appreciate you can use literals for both Static Variables and
Instance Variables. Two questions :-

- Can you hold CONCRETE variables as I have demonstrated with the M/F
Level 78s, in either 'dummy Factory' or the Instance ?

- Are there situations where it is an absolute MUST to hold Static
Variables in the 'dummy Factory' for access by Instance Methods, (i.e.,
can a Java Instance invoke the 'Dummy Factory' methods ?).

PUBLIC PRIVATE :

Correct assumption Oliver - all OO COBOL methods are PUBLIC. Don't know
what size organizations you have worked at as yet, but assume a
mainframe installation with 100 programmers, and as Bill has pointed out
in the past, there are some with larger numbers than that. So you don't
want all 100 plus, crawling all over your in-house classes that you
have written, looking for methods and inadvertently picking up on what
are in fact 'Private' methods. (Hang off Pete - Components come up
in a minute). I believe *most* medium to large organizations have a DBA
(Data Base Administrator) who controls the structure of the DB tables
and access. Even in a Procedural environment, *possible* the DBA's
department could produce SQL statements as copy fies for re-use.

Same approach makes sense with OO - The DBA or a parallel administrator
could generate in-house OO classes and the only thing end developers
have access to is a list of the PUBLIC methods applicable, per class,
summarized in a document with sending and returning parameters. A
developer *thinks* he needs to write a new method, he checks and is
advised there is one available to do what he wants, or to accommodate
his request they could write a sub-class to give the additional 'twist'
he is after - which may even override an existing method in the original
class that now becomes a 'super'.

You'll appreciate that over a 10-year period or more, if you approach it 
in willy-nilly fashion without central control, you might finish up with 
5 - 10% of methods, (perhaps more ?), which were initially used, dropped
and nobody knows they are occupying real estate, sat there doing nothing.

Same sort of control applies to Pete's component concept. Firstly,
there's no way you can use his PRIVATE methods - they aren't listed in
his Help Files. Now Pete quoted, working in UK Midlands at a utility
company, he had a bunch of bright young things generating components
on the fly - Pete how was that controlled to avoid overlap or
obsolescence ?

I don't think I've asked this question before. Pete, do you have access 
to the source for F/J support classes, like collections etc ?

So yes OO Methods are PUBLIC - ALMOST ! From the Fujitsu on-line manuals :-
------------------------------------------------------------
Method-id.
	method-name-1 (AS literal-1)

	GET/SET PROPERTY property-name-1 AS Literal-1
	OF Interface-name-1
	OVERRIDE

	IS  PUBLIC/ PRIVATE/ PROTECTED	<***********

	CUSTOM-ATTRIBUTE-PHRASE
-------------------------------------------------------------

Confused ? Well get even more confused - those asterisked words above
appear in M/F as *extensions* when defining the Class :-

	Class-id.	My Class inherits from......
			/Data is PRIVATE
			/Data is PROTECTED
			and a few other 'goodies'

but note are used as a feature to control access to data NOT methods
------------------------------------------------------------------------

OO-COBOL is a real winner when it comes to portability !

Practical use of a class containing PUBLIC/PRIVATE - minimal requirement 
as I'm only interested in YYMM (stored as ccyymm) - my DateAndTime class 
has my few date routines. At the current time NO Factory and all 
methods, public or private, (the latter of course being invoked from the 
'publics') are stored in the OBJECT (Instance) :-

so invoke DateAndTime "new" returning os-DateTime
invoke os-DateTime "checkDate4" using
	 In-Date4(yymm) returning Out-Date6 (ccyymm)

It's purely for convenience. I know a large number of my
programs(classes) are going to want dates so I get the os-DateTime
object reference at the start of the application - passing as necessary
to interested parties.

If I wished I could make it a 'singleton instance', by moving the WHOLE
of the OBJECT code up between FACTORY and END-FACTORY; then Object would
appear "OBJECT. (empty) END-OBJECT".

doing the latter :-

1) I do NOT invoke DateAndTime "new" returning....., BUT
2) invoke DateAndTime "checkDate4" using
	 In-Date4(yymm) returning Out-Date6 (ccyymm)

Whether or not it applies in Java where you have a 'Dummy Factory' and
Instances, I don't know. But a subtlety attached to above. If I take the
approach of using (a) ONLY an Instance(OBJECT-SECTION), or (b) Factory
and Instance - data changed in the Global Working-Storage for the
Instance exists for the life of the Instance; i.e. if I am incrementing
a counter for Number of Accounts opened, the latest incremented count is
available, for the duration of the life of the Instance.

Not so if I ONLY use a FACTORY. Think back to Frank's example - the
Number of Accounts in FACTORY is incremented resulting from finishing
the Instance - i.e., the Instance automatically terminates at some 
point, and as it was 'driven' by a method from the Factory, the next 
instruction it returns to in in Factory is 'increment the count'. If I 
ONLY have a FACTORY, (and I previously quoted the class CharacterArray 
in M/F), then each separate access of the Factory is a new invocation 
starting at 'square one', i.e. just invoking FACTORY methods all 
variables are in an initial state.

COMPONENTS :

Watch this space - I'm going to start a thread on 'Components' - asking
for very specific clarification. Hopefully others will raise issues for 
which they have questions - which, perhaps in the past, they have been 
reticent to ask.

Jimmy
```

#### ↳ Re: Constants, Static, Public, Private

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-15T14:32:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142461953.041645.126860@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<_M_Rf.147168$B94.59312@pd7tw3no>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
> The only reason I'm referring to Constants is to get a handle on the
> word 'static' when used in Java.

´static´ is not ´constant´.  Static is distinct from ´dynamic´.

In C you can declare local variables within a function. These are
created dynamically when the function is entered, usually on the stack,
and disappear when the function returns. If it is required to have a
variable that stays around and has the same value the next time the
function is called then it is declared as ´static´.  It is created
during the compile and is not dynamically created or destroyed.

If ´static´ is applied to a declaration outside a function within a
file then this makes it  created staticly but not available outside the
file (ie not available from other source files in the same program. It
is ´file local´ and available to all following functions.

If a function is declared ´static´ then it too is ´file local´.

So moving this to C++ and Java ´static´ means ´non-dynamic´ and
thus not created nor destroyed when an object is created and destroyed
- it is a class variable and there can only be one, not one per object.


´final´ means cannot be changed.  There is no point having more than
one instance of a final variable thus they should also be ´static´.
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-15T23:33:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%u1Sf.12348$lT3.6405@fe06.news.easynews.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142461953.041645.126860@i39g2000cwa.googlegroups.com>`

```
Richard,
   Not knowing these other languages, does this mean (that for function 
variables)

 "not static" is the same as a COBOL Local-Storage item
      while
 "static" is the same as a COBOL Working-Storage item?

(ignoring things like "CANCEL" and "IS INITIAL" - which aren't relevant to COBOL 
functions, but to COBOL Programs)
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2006-03-15T20:41:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jm3Sf.62$nA2.144526@news.sisna.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142461953.041645.126860@i39g2000cwa.googlegroups.com> <%u1Sf.12348$lT3.6405@fe06.news.easynews.com>`

```
Bill,

In C/C++ variables (and I'm speaking about variables and not functions).

"static" is equivalent of Working-Storage (but not for Cobol.NET, at least 
Fujitsu !!!!!)
If it's outside the function, it's visible for all functions which are 
located below the declaration.
If it's inside, it's visible only in this function.
That's like imagine to put several Cobol programs into one file, put 
working-storage for "all of them" and put additional "working-storage" for 
each of them.

non-static (i.e. absence of the "static" keyword) outside of the function - 
it's in working-storage and it's GLOBAL
but there are some mess and depending on the way modules are linked and 
platform (especially old), you might get a several copies or (more usual) 
you might get "duplicate symbol" during the LINK stage. So usually in C/C++ 
it's better to add "extern" keyword to point out that all references goes to 
the same variable - that will be exact equivalent of GLOBAL (formally there 
should be no "extern" exactly in one program who is the owner, or 
"initiator" of this variable where you can assign initial VALUE, but it's 
messy anyway).

non-static inside the function == Local-Storage

"static" inside the class - it's working-storage but I don't know the name 
resolution in Cobol, i.e. if we have 2 classes and static variable A in 
both, how to address it in Cobol ? In C++ it's "classname::A"

non-static inside the class - instance member.

In java you can't have variables outside of the class at all, so there are 
no equivalents of the working-storage.

Correcting Richard a little bit

> ?final? means cannot be changed.  There is no point having more than one 
> instance of a final variable thus they should also be ?static?.

I agree, it's almost does not make any sense, but it's possible to have a 
"final" and not static (at least in java), so the value of the "final" can 
be assigned only in constructor of the class and can't be changed thereafter 
(or it's a mess in my head and it's about C#?)

Regards,
Sergey


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:%u1Sf.12348$lT3.6405@fe06.news.easynews.com...
> Richard,
>   Not knowing these other languages, does this mean (that for function 
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-16T04:06:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bv5Sf.148425$B94.33692@pd7tw3no>`
- **In-Reply-To:** `<Jm3Sf.62$nA2.144526@news.sisna.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142461953.041645.126860@i39g2000cwa.googlegroups.com> <%u1Sf.12348$lT3.6405@fe06.news.easynews.com> <Jm3Sf.62$nA2.144526@news.sisna.com>`

```
Sergey Kashyrin wrote:
> Bill,
> 
…[26 more quoted lines elided]…
> both, how to address it in Cobol ? In C++ it's "classname::A"

OK - in C++ you have the shorthand version. Nothing equivalent that I'm 
aware of in COBOL. We have three Classes, A the Invoker, and B and C 
which both hold your variable A in their Global Working-Storage.

in Class A:
invoke MyClassB-Object "get-variableA" returning ws-VariableA1
invoke MyClassC-Object "get-variableA" returning ws-VariableA2

Could return both to ws-VariableA1 - but I don't think that's what you 
are after :-).

But it maybe, subject to what you are after - like capturing the total 
number of new credit cards opened(sold to customers). That in turn is 
further complicated by the fact that general retail now seems to be open 
09:00 to 21:30, three shifts of staff, say approx 3 to 4 people per 
shift, both register operators and sales staff (PC = Sales Associates. 
Rah ! Rah ! We all love Wal Mart !), each person with the responsibility 
of selling new credit cards.

End of post.

Jimmy
> 
> non-static inside the class - instance member.
…[15 more quoted lines elided]…
>
```

#### ↳ Re: Constants, Static, Public, Private

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-15T16:49:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47rnfqFgnjfbU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
Could one "simulate" a private method using "nested methods"?  Not sure if
this is even allowed, but...

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-17T01:48:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47t54vFhbgngU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:47rnfqFgnjfbU1@individual.net...
> Could one "simulate" a private method using "nested methods"?  Not sure if
> this is even allowed, but...
>
> Frank
>
Not nested Methods... nested Programs. Fujitsu does this with PowerCOBOL. 
And it is very viable with NetCOBOL also.

Richard has made the main point that 'static' is as opposed to 'dynamic' 
storage, and I have posted twice already explaining Factory, and answering 
Jimmy's question as to how factory methods are invoked in OO COBOL. It seems 
it either wasn't understood or it didn't register. (I certainly had no 
acknowledgement of it, or request for further information so I figured it 
was clear. )

A major point that has been ignored is that early or late binding have a 
major effect on how Factory works in OO COBOL.

The thought crosses my mind that it's really a bit late now to be getting 
interested in the details of OO COBOL; time for that was 6 or 7 years ago.

Similarly with components. If it wasn't interesting then, how come it is 
now? I've been posting here for years on the advantages of these things and 
all I get is dismissed as an 'evangelist' who couldn't possibly be telling 
the truth. Well, I did the hard yards and got the benefits. When I suggested 
that using components could minimise the maintenance of source code, it was 
SO unacceptable I received abuse from some quarters.  NOW there's interest? 
You'll forgive me if my contribution to this thread is minimal... (These 
days I build them visually and embed them in web pages to distribute them. 
Hardly ever use COBOL for it any more; ASP does it fine.)

I guess the dinosaurs take a long time to move. Sadly, this boat has been 
well missed and the smoke from it is now a smudge on the horizon. The Java 
viewpoints are still relevant because their boat is running a regular ferry 
service... :-) Meantime we are seeing new jet skis and fizzboats buzzing 
around the docks every other month...

Good heavens, next thing you'll all be wanting to know about UML and Object 
modelling methods. Then it'll be RAD and replacing SPF with Eclipse or 
Visual Studio... no, it's more than flesh and blood can stand... I need to 
find a darkened room and lie down with a nice treatise on Linux...or 
Vista... :-)

Pete.

PS If anyone is genuinely interested in using OO COBOL (Fujitsu) or 
components and needs help, mail me privately. If I can help, I will.

PPS If anyone can recommend a dual processor 64 bit laptop (I want to run 
Vista on it...eventually)  I'd appreciate hearing your experience.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

- **From:** Peter Lacey <lacey@mts.net>
- **Date:** 2006-03-16T10:42:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44199558.42B0A2F4@mts.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net>`

```
Pete Dashwood wrote:

> 
> The thought crosses my mind that it's really a bit late now to be getting
…[7 more quoted lines elided]…
> SO unacceptable I received abuse from some quarters.  

Now, now, namesake.  You didn't say "minimize".  You said "never".  You
may have meant only the components but you never made that distinction.

PL
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-18T14:21:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4815k4Fhlr0jU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net>`

```

"Peter Lacey" <lacey@mts.net> wrote in message 
news:44199558.42B0A2F4@mts.net...
> Pete Dashwood wrote:
>
…[19 more quoted lines elided]…
> PL

It's OK. I got over it. :-)  As the discussion was about components, I took 
it as read that my comments would apply to that.

The fact is that I have components deployed live, and they have been for 
years, and they have NEVER been maintained, even though changes have been 
made to the system. It isn't just about OO COBOL and components. It is about 
a whole different way of doing things and, short of writing incredibly long, 
tedious, threads here, I see no quick way to explain it. When I started to 
think about launching into explanations, I suddenly thought: "Why? Is anyone 
REALLY interested?"

I don't think so.  Anyway, it's too late now; the COBOL boat has sailed.

Not only that, but experience here has shown a resistance to new ideas and 
the constant comparison of any new concept against "What we do now. It's 
really just a re-invention of what we've always done..."

When what you are atempting to describe is similar in some ways, but 
extremely different in other critical ways, and no attempt is made to grasp 
the basic concepts before measuring them against "What we do now", it becmes 
tedious and demotivating to continue. It's like the desire is to have an 
argument, rather than to allow things to be posited and laid out, THEN argue 
about it. I would happily argue my case with anyone who has actually 
developed a component based system and deployed it (but I don't need to 
then, because those people have no argument as to the merits of this 
approach :-)), but it is simply stupid for me to do it with people who 
haven't grasped the fundamental ideas and won't, because they can't see past 
what they have always done. IT is the old ITSA thing... Describe something 
to someone and they immediately decide ITSA whatever... when, in fact, it is 
LIKE whatever, in SOME aspects, and this may have no bearing on the essence 
of it.

The only good thing about banging your head against a wall is that it's nice 
when you stop :-)

And why would I want to persuade people to a different way of doing things? 
Like I have observed before, I have no vested interest, I'm not selling a 
product, and I'm not on commission. Why set myself up for aggro and abuse? 
No, I'll just make like Brer Rabbit here... :-).

Consider me a 'retired' evangelist... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-18T02:15:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63KSf.155612$B94.79123@pd7tw3no>`
- **In-Reply-To:** `<4815k4Fhlr0jU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net> <4815k4Fhlr0jU1@individual.net>`

```
Pete Dashwood wrote:
> 
> Consider me a 'retired' evangelist... :-)
> 
> Pete. 
> 
Seriously, please don't. I'm working out a reply to Frank on his 
'Nested' methods - Uggh ! Meanwhile I have a partial response to you - 
about me not answering - and I for one *am* interested in Components, 
and in fact always was, but with a touch of skepticism on the 'How to' - 
but you don't appreciate, being so close to your solution, and can't 
understand why others would have questions or are skeptical until they 
have further feedback.

So you and I accept COBOL is on the way out, for slightly differing 
reasons, but arriving at the same point. What was your date 2015 - 
that's still some 9 years away, during which time some effective 
Component coding could be done in COBOL. Come 2015, COBOL doesn't drop 
off the edge of the earth; applications written 5 years earlier could 
still be running efficiently through to 2025.

Meanwhile, given some expanded explanation of what your topic is about, 
I think Frank, just delving into OO with AIX for the first time, could 
well benefit from your experience - but with a lot MORE detail to set 
him on the right track. It follows he could take your ideas, adapt and 
come up with an even slicker answer. There aren't too many originals 
around; through history it has been updating the ideas of predecessors.

Stay tuned.

Jimmy
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-20T02:33:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4858diFiggtbU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net> <4815k4Fhlr0jU1@individual.net> <63KSf.155612$B94.79123@pd7tw3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:63KSf.155612$B94.79123@pd7tw3no...
> Pete Dashwood wrote:
>>
…[10 more quoted lines elided]…
>
That's not quite true. I do understand and expect scepticism. The problem is
pre-conceived ideas, and the inability to lay them aside.

Anyway, the whole thing is being overtaken by events.

Components are the accepted way of doing things for most of the computer
development community, outside of COBOL. Java sites use beans (which are
components) to build functional components, in very much the way I suggested
here years ago. MS sites use VB, C++, and C# to build COM and ActiveX
components (which I have been doing with OO COBOL for the past 7 years). The
Windows Operating System is a container for hundreds (No, it's thousands... 
I just ran a free Object Browser called QIQ and it reports well over 2000 
components (COM and ActiveX only) found on my system, most of which are 
provided by the Windows OS. The number is nearer 3000 if I include controls, 
.DLL servers, and .EXE servers.)

> So you and I accept COBOL is on the way out, for slightly differing
> reasons, but arriving at the same point. What was your date 2015 - that's
> still some 9 years away, during which time some effective Component coding
> could be done in COBOL.

Yes, it could. But what's the point? It can be done in other languages too, 
and THEY have a future. If you use a Visual IDE you don't even need ANY 
language. You can build the components visually with tools like Visual 
Studio and have the code generated in C# or C++ or really, anything you 
like...

Building components in OO COBOL now, is really just flogging a dead horse. 
Besides, you come back to the perennial problem of the RTS. Unless you use 
.NET COBOL (and it is around $3000 a desk) your components are going to 
experience resistance when it comes to deploying them. I've stopped building 
components with OO COBOL except if I want them only for myself, and COBOL 
makes the most sense to use.

>Come 2015, COBOL doesn't drop off the edge of the
> earth; applications written 5 years earlier could still be running
> efficiently through to 2025.

Let's see what happens. Dropping off the edge of the earth cannot be 
discounted. It has already dropped a pretty fair percentage of the user base 
it had 10 years ago, and if you look at the base it had 25 years ago, you 
could say it is already dead....
>
> Meanwhile, given some expanded explanation of what your topic is about, I
> think Frank, just delving into OO with AIX for the first time, could well
> benefit from your experience - but with a lot MORE detail to set him on
> the right track.

The 'right track', huh...? :-)

My advice to Frank, as it is to anyone who's serious about getting into OO, 
is: Learn Java.

Why go OO at all? The general resistance to it by the COBOL community has 
been a major nail in COBOL's coffin. It's too late now. The future of COBOL 
is clear. It will be a batch processing language using traditional 
procedural coding techniques. (Until the people who write it die off or 
retire...) And before someone mentions CICS, I predict that all current CICS 
systems will be converted to 'something else' (probably the Web, but I'm not 
closing my options) by 2020. There are new developments in the pipeline that 
obviate the need for a  CICS style TP Monitor. Servers will run 
transactions, and they'll do it with a different approach.

The main reason to go OO at all is to facilitate the building of components. 
COBOL suffers by comparison at this, so why use it?

> It follows he could take your ideas, adapt and come up
> with an even slicker answer.

Nah, that 's not gonna happen :-)

Pete.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-20T17:50:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4890uiFivhf5U1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net> <4815k4Fhlr0jU1@individual.net> <63KSf.155612$B94.79123@pd7tw3no> <4858diFiggtbU1@individual.net>`

```
Pete Dashwood<dashwood@enternet.co.nz> 03/19/06 7:33 AM >>>
>
>
>My advice to Frank, as it is to anyone who's serious about getting into OO,

>is: Learn Java.

Actually, I started "learning" OO with C++ way back in the early 90s.  I've
been using Java here and there for four years or so.  My issue at the moment
is trying to take that knowledge and relate it to OO COBOL.
Of course if I had actually worked on a "real" project in Java it might come
to me more naturally.

As it is, Java does me little good with regard to my current position.  Java
is not even available on our operating system.  Of course the "web apps"
guys use Java as their main language, but to get at the mainframe data they
still have to interface with us and our COBOL programs.  :-)

>Why go OO at all? The general resistance to it by the COBOL community has 
>been a major nail in COBOL's coffin. It's too late now. The future of COBOL

>is clear. It will be a batch processing language using traditional 
>procedural coding techniques. (Until the people who write it die off or 
>retire...) And before someone mentions CICS, I predict that all current
CICS 
>systems will be converted to 'something else' (probably the Web, but I'm
not 
>closing my options) by 2020. There are new developments in the pipeline
that 
>obviate the need for a  CICS style TP Monitor. Servers will run 
>transactions, and they'll do it with a different approach.
>
>The main reason to go OO at all is to facilitate the building of
components. 
>COBOL suffers by comparison at this, so why use it?

I've been browsing through the draft of the next COBOL standard and I have
to say that, OO and otherwise, it has a lot of good stuff in it.  Perhaps
*too* much, actually.  COBOL, as a language, is already huge, and this only
makes it larger.  Nonetheless, I'm impressed.  But if no one has yet
implemented even much of the 2002 standard I do have to wonder what hope the
new standard has...

Speaking of the next COBOL standard, is there something other than this
draft that gives an overview of the new language features?  Preferably with
examples?  I do much better with seeing an example and then perhaps looking
at the reference to get more information.  Just reading the reference itself
I can't always visualize what the heck it's talking about!

By the by, I just "discovered" Ruby over the past week.  Does anyone here
use it?  I found it to be quite fascinating, and it actually has quite a few
features that I've been looking for.  Doesn't help with COBOL, but it's
still interesting.  My main problem now with learning new languages is that
I can't think of an interesting project to do to really test out the
language.  Ah well.

Frank



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 8)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-21T14:46:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YkUTf.5978$nQ6.228@clgrps13>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net> <4815k4Fhlr0jU1@individual.net> <63KSf.155612$B94.79123@pd7tw3no> <4858diFiggtbU1@individual.net> <4890uiFivhf5U1@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:4890uiFivhf5U1@individual.net...
>
> By the by, I just "discovered" Ruby over the past week.  Does anyone here
…[6 more quoted lines elided]…
> language.  Ah well.

    Read a few tutorials on Ruby, but haven't actually installed an 
interpreter/compiler and actually played with it yet. Usually when someone 
wants to "show off" Ruby, they do a demo using "Ruby on Rails" which speeds 
up web application developments. Maybe you could try following along one of 
those "Ruby on Rails" tutorials for a project to toy with.

    - Oliver
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-20T17:37:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48905nFj11rbU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <47t54vFhbgngU1@individual.net> <44199558.42B0A2F4@mts.net> <4815k4Fhlr0jU1@individual.net> <63KSf.155612$B94.79123@pd7tw3no>`

```
James J. Gavan<jgavandeletethis@shaw.ca> 03/17/06 7:15 PM >>>
>Pete Dashwood wrote:
>> 
…[26 more quoted lines elided]…
>Stay tuned.

Just a clarification, but I am not actually looking into OO in COBOL for
AIX.  I was searching for some OO stuff (I forget what) and found it in the
COBOL for AIX manual.  We don't even have AIX, or even an OO COBOL
compiler...  Which is why I am asking so many questions instead of testing
them out for myself.  I have nothing to test with!

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-17T00:26:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nnSf.149866$sa3.103297@pd7tw1no>`
- **In-Reply-To:** `<47rnfqFgnjfbU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net>`

```
Frank Swarbrick wrote:
> Could one "simulate" a private method using "nested methods"?  Not sure if
> this is even allowed, but...
> 
> Frank

Frank,

I note Pete has already responded in a slightly different vein,
concentrating on your word 'Nesting'.

Was your query sort of tongue-in-cheek, or do you have a hang-up that
you have to 'invent' private methods ?

A quick example using 'nested' private methods.

        Class A the invoker
        Class B containing the PUBLIC Method you invoke, PUBLIC Method-B

        Class B or some other Classes, where you are using PRIVATE
              methods, C through H etc....

        Two approaches :-

        Class-A--->Class-B(Public)---->
            ---->PRIV - Method-C---->PRIV - Method-D--->PRIV - Method-E


            OR :-
                                       '----> PRIV - Method C
                                       '
        Class-A---->Class-B(Public)----'----> PRIV - Method D
                                       '
                                       '----> PRIV - Method E

Above is not comprehensive, but the top part illustrates your 'nesting'
query.

However, if you are thinking in terms of 'dreaming up' Private methods
then you are designing from the wrong end. The existence and coding of
Private methods is only crystallized when you get into an invoked class
via a PUBLIC method.

Let's do a bit of speculation and assume your Bank gives the go ahead to
revamp in OO, both COBOL and Java. Some of the following will already 
exist  in your procedural applications :-

- Customers' Name and Address File/or DB Tables

- Individual Customer Accounts using IDs from above with sub-levels
Chequing, Savings, Plastic (you wrote recently you are looking into
that), and many others. Even within your individual account types you no
doubt have flags to indicate which of a series of rules apply to a
specific account.

- For want of a name 'All Accounts' or 'Accounts Main', and in OO
parlance this is a 'super' providing common routines/methods to however
many of the categories you have above.

- Series of Transaction files providing history and audit trail

- The real reason banking exists - saves me putting my money in a sock
under the bed AND makes money for the bank from interest charges :-).
As I wrote this I recalled that early Economics text - Joe Blow deposits
$100 in the bank. The bank takes a gamble retaining only $10 in cash and
loans out the other $90, (with interest of course), hoping they've
always got some real cash around should Joe Blow decide he wants to
withdraw $50. Generally works fine for banks except for loans to 'iffys'
like Enron or WorldCom - then the banks can get burned !

So OO-wise, Interest calculations are a big item for you. The
calculations need to call upon date routines to get time spans. But so
far as OO is concerned it would be a big mistake to have a Class called
"Interest Charges and DateandTime routines". They work hand-in-glove
with one another but should be considered as two separate classes,
Class-Interest, Class-Dates as independently they have entirely 
different objectives. It's very likely that what I refer to as 
Class-Interest may  well have been designed by you as a group of 
sub-classes for account  types, drawing off super Class-Interest for 
common routines/methods.

That is certainly the case with the M/F support classes where they have
obviously spent considerable time designing, utilizing a series of
private methods in various classes, to support the one public method
message.

If we just concentrate on what I referred to as Class-Dates, given about
4-6 of you having a brainstorming session you could come up with a
DateClass which *could* be written within AIX in either COBOL or Java.
Now COBOL is already rich in date routines with the Date functions;
however, with some research you may find there are canned routines in
Java which do all you want, and then some.

I didn't list the following before, because of its length, but my
DateAndTime class follows shortly. I've commented it fairly heavily and 
indicated difference between PUBLIC and PRIVATE methods. My use is 
minimal because I'm only interested in Year and Month - days of month 
are irrelevant to the application I *was* designing You *could* do it in 
COBOL code with one minor stumbling block - where I use object 
references. These objects are  associated with GUI displayables. 
Assuming you are GUI-ing in Java there are either Java routines to 
translate to pic x or the IBM routines that  Bill made reference to for 
somebody with a query in the IBM Newsgroup.

So your think-tank sits down to figure out what you want in a Date
Class. You arrive at a set of invokes to PUBLIC methods in the Date
Class knowing that you may have combinations of :-

invoke myDateTimeObject 'public-method-name' using xxx (perhaps ?)
returning xxx.

Quite possible in your case you might come up with some 50-70 'publics'
covering dates for banking. Who knows, you might be pleasantly surprised
and find you only have 30 'publics'.

I'll make a point here, and it is my own personal view, and I don't know
whether any of the academics who write tomes on OO-methodology even
support the idea - but - I believe it is a flaw to have a method doing
too many things - you will finish up duplicating, and each 'duplication'
just means more testing. As a general rule, I would suggest, a method
should not occupy much more than half a page, perhaps one page where you
are using EVALUATE or CASE statements. (I have some methods which are no
more than three lines of code).

You will find that initially you will be tempted to write a PUBLIC
method coding your instructions through from 'a' to 'z'. Given that you
are writing a series of 'publics', and we are concentrating on a Date
Class, it will become apparent that you have several public methods with
duplication of routines. This is where PRIVATE comes into play. You are
looking for commonality and within your 'publics' you chop out the
repetitive code and insert it into 'generic' PRIVATE methods which can
be accessed by several or lots of 'publics'. The point I'm making is
your invoked public methods are an entry-point into a black-box, the
Date Class, which internally is being instructed to access the private
methods.

In practical terms I don't think you would find yourself writing too
many levels of a hierarchy, perhaps just the one-class approach I
illustrate below. To get any real leverage from hierachial structures
requires quite a considerable amount of thought and the result has to be
'generic' or vanilla-flavaoured enough to handle all sorts of situations 
for comparative objects.

We don't have PRIVATE in COBOL - but I don't foresee it as a stumbling
block. I haven't been tripped up yet.

The class below, I have heavily commented to give you an indication of
what is going on. To tell you the truth, when I started looking at it, I
had to scratch my head - quite simply when you have written a class and
moved on to other activities you lose recall of what the specifics of
the class are. You write it, thoroughly test it, and other than you know
you have to feed it specific method names with/without sending and
receiving parameters - you really don't need to be familiar with its
internals.

Did the class below require maintenance. A definite 'Yes'. Check the 
comments for method "getMonthYearObject" below. Originally I had a 
dialog display of 10 columns with two rows (a) Month and (b) Year. 
Key-in 'yymm' to either (a) or (b), and I redisplayed 'Month' in (a) and 
'ccyy' in (b). Daft - when I got the hang of what MLEs (Multiple Line 
Entryfields) can really do, (originally thinking they were there for 
some say 20 or 30 lines of text) - then I dropped (a) and (b) 
substituting a new (a) which was a two-line MLE with the wrap-around.
(Clarification on data-entry - enter '1' and I display Jan 2000; '103' = 
Mar 2001 etc.)

Compiles required - two - (1) the program below and (2) the Dialog
Template which needed the new enhancement. Effect on an application,
just the two mentioned; no other classes/programs got touched.

It wasn't the intention, but I guess the above sort of turned into an 
OO-COBOL-101. Hopefully it gives you a few hints.

PS: It's conceivable that Pete will suggest that a series of Components
could replace this class. Very likely, but is it necessary ? That's one
of the points I want to ask him about should he be responsive to a
series of questions on Components. (My queries wont be a series of
'gotchas' but "Please expand, exactly how does this feature fit in ?").
 From his answers, I think a skeptic, (justifiably so from lack of
information), like Peter Lacey, will respond, "Now I understand what you
were saying. I accept that, now how does this piece of Lego fit in ?"

Jimmy

The source of my DateAndTime follows. Remember, I've cut this back to 
the minimum using the M/F 'ignore red tape', and where I have 
"Class-Control", substitute "Repository" syntax.  I can use a directive 
"$set ISO 2000" which will let the compiler accept "Repository" syntax - 
other than looking 'pretty', it doesn't do a damn thing for me in V 3.1 
- I would need to upgrade to V 4.0 :-

*>--------------------- datetime.cbl --------- 2005 Sep 10 ------------

        Class-id.        DateAndTime
                         inherits from base.

        Class-control.   DateAndTime     is class "datetime"
                         CharacterArray  is class "chararry"

                         .

        *> The methods are "quad-purpose" (1) Numerics for file/DB
        *> storage, (2) For printing (3) GUI 'ACCEPTS' and
        *> (4) GUI 'DISPLAYS'
        *>
        *> Although this class does validity checks it doesn't generate
        *> any error messageboxes; a result is returned to the 'Caller'
        *> which is responsisble for displaying messages

        *>--------------------------------------------------------------
        *>FACTORY.
        *>--------------------------------------------------------------
        *>END FACTORY.
        *>--------------------------------------------------------------
        OBJECT.
        *>--------------------------------------------------------------
        WORKING-STORAGE SECTION.
        01 ws-monthTable
           value "JanFebMarAprMayJunJulAugSepOctNovDec".
           05 monthName occurs 12     pic x(03).

        01 Date21.
           05 Date21-Year-Month.
              10 Date21-Year              pic 9(04).
              10 Date21-Month             pic 9(02).
           05.
              10 Date21-Day               pic 9(02).
              10 Date21-Hours             pic 9(02).
              10 Date21-Minutes           pic 9(02).
              10 Date21-Seconds           pic 9(02).
           05.
              10 Hundredths               pic 9(02).
              10 GMT-PlusMinus            pic x(01).
              10 GMT-HoursDifference      pic 9(02).
              10 GMT-MinutesDifference    pic 9(02).

        *> For following see method "setCCYYMMcheck"

        01 yymm4                          pic 9(04) value 0.
        01 ccyymm6                        pic 9(06) value 0.
        *>--------------------------------------------------------------
        Method-id. "checkCentury".   *> PRIVATE
        *>--------------------------------------------------------------
        *> This is invoked by 'checkDate4" and "CheckYearMonthText"

        Linkage section.
        01 lnk-YearIn                        pic 9(02).
        01 lnk-YearOut                       pic 9(04).

        Procedure Division using     lnk-YearIn
                           returning lnk-YearOut.

           if   lnk-YearIn < 50
                add 2000 to lnk-YearIn giving lnk-YearOut

           else add 1900 to lnk-YearIn giving lnk-YearOut
           End-if

        End Method "checkCentury".
        *>------------------------------------------------------------
        Method-id. "checkDate4".         *> PUBLIC
        *>------------------------------------------------------------

        *> checking validity of MM and returning ccYYMM. Returns
        *> lnk-Date6 = zeroes, if incorrect

        Local-storage section.
        01 ls-date4.
           05 ls-year2                       pic 9(02).
           05 ls-month2                      pic 9(02).
              88 ValidMonth                  value  1 thru 12.
        01 ls-year4                          pic 9(04).

        Linkage section.
        01 lnk-date4                     pic 9(04).
        01 lnk-date6                     pic 9(06).

        Procedure Division using     lnk-date4
                           returning lnk-date6.

         initialize        lnk-date6
         move lnk-date4 to ls-date4

         if      ValidMonth
                 invoke self "checkCentury" using     ls-year2
                                            returning ls-year4
                 compute lnk-date6 = (ls-year4 * 100) + ls-month2
         End-if

         if      (ccyymm6 <> zeroes) AND
                 (lnk-date6 > ccyymm6)
                 move zeroes to lnk-Date6
         End-if

        End Method "checkDate4".
        *>--------------------------------------------------------------
        Method-id. "checkYearMonthText".  *> PUBLIC
        *>--------------------------------------------------------------

        *> Uses GUI input field object containing "yymm"; if valid
        *> returns lnk-Date6 = ccyymm, ( or = zeroes for errors)

        *> invoked by "getDate4AsObject"

        Local-storage section.
        01 ls-date4                          pic 9(04).
        01 ls-date4A redefines ls-date4.
           05 ls-year2                       pic 9(02).
           05 ls-month2                      pic 9(02).
              88 ValidMonth                  value  1 thru 12.

        01 ls-length                         pic x(4) comp-5.
        01 ls-string                         object reference.
        01 ls-text                           pic x(04).
        01 ls-year4                          pic 9(04).
        Linkage section.
        01 lnk-DateObject                    object reference.
        01 lnk-date6                         pic 9(06).

        Procedure Division using     lnk-DateObject
                           returning lnk-date6.

         initialize lnk-date6
         move length of lnk-DateObject to ls-length
         invoke lnk-DateObject "getText" returning ls-string
         invoke ls-string "trimblanks" returning ls-string
         invoke ls-string "getValueWithSize"
                using ls-Length returning ls-text
         invoke ls-string "finalize" returning ls-string
         compute ls-date4 = (function numval (ls-text))

         if      ValidMonth
                 invoke self "checkCentury" using     ls-year2
                                            returning ls-year4
                 compute lnk-date6 = (ls-year4 * 100) + ls-month2
         End-if

         if      (ccyymm6 <> zeroes) AND
                 (lnk-date6 > ccyymm6)
                 move zeroes to lnk-Date6
         End-if

        End Method "checkYearMonthText".
        *>--------------------------------------------------------------
        Method-id. "getCurrentDate".     *> PUBLIC
        *>--------------------------------------------------------------
        Local-storage section.
        Linkage section.
        01 lnk-Year-Month.
           05 lnk-year                   pic 9(04).
           05 lnk-month                  pic 9(02).

        Procedure Division returning lnk-Year-Month.
          move function Current-Date  to Date21
          move Date21-Year-Month      to lnk-Year-Month

        End Method "getCurrentDate".
        *>--------------------------------------------------------------
        Method-id. "getDate4AsObject".    *> PUBLIC
        *>--------------------------------------------------------------
        *> Takes a GUI input date pic 9(04) = yymm, and returns an object
        *> containg Mth ccyy (e.g. Sep 2004 ) - if valid

        01 ls-date6                    pic 9(06).

        Linkage section.
        01 lnk-object                  object reference. *> GUI input
        01 lnk-Values.
           05 lnk-result               pic x(4) comp-5.
           05 lnk-string               object reference.

        Procedure Division using lnk-object returning lnk-values.

        initialize lnk-result
        invoke self "checkYearMonthText"
               using lnk-object returning ls-date6

        if     ls-date6 <> zeroes
               invoke self "getMonthYearObject"
                    using ls-date6 returning lnk-string

        else   move 99 to lnk-result
        End-if

        End Method "getDate4AsObject".
        *>--------------------------------------------------------------
        Method-id. "getDate6FromObject".   *> PUBLIC
        *>--------------------------------------------------------------
        *> Note : Background to this method. User enters a GUI date
        *> as pic 9(04) = yymm. If user presses TAB key after entering
        *> the date it will be validated and yymm = 0707 will be
        *> re-displayed in the Dialog as Jul 2007.
        *> If however, the user clicks on the PB-OK button the input
        *> wont be converted and the value will remain as '0707' -
        *> which is unacceptable to this method - the purpose of which is
        *> to convert Jul 2007, back to '200707' for storage in the
        *> DataBase via the Busines Logic program.

        01 n                                    pic x(4) comp-5.
        01 ls-length                            pic x(4) comp-5.
        01 ls-string                            object reference.
        01 ls-text                              pic x(08).
        Linkage section.
        01 lnk-Object                           object reference.
        01 lnk-Date6.
           05 lnk-Year                          pic 9(04).
           05 lnk-Month                         pic 9(02).

        Procedure Division using lnk-Object returning lnk-Date6.

        initialize lnk-Date6
        move length of ls-text to ls-length
        invoke lnk-Object "getText" returning ls-string
        invoke ls-string "trimblanks" returning ls-string
        invoke ls-string "getValueWithSize"
              using ls-Length returning ls-text

        Evaluate true
           when ls-text = spaces
           when ls-text (1:3) not alphabetic
                continue
           when other
              move ls-text(5:4) to lnk-Year
              perform varying n from 1 by 1 until n > 12

                    if MonthName(n) = ls-text(1:3)
                       move n to lnk-month
                       EXIT PERFORM
                    End-if
              End-perform
        End-Evaluate

        End Method "getDate6FromObject".
        *>--------------------------------------------------------------
        Method-id. "getDateModified".     *> PUBLIC
        *>--------------------------------------------------------------
        Linkage section.
        01 lnk-Date.
           05 Date21-Year-Month.
              10 Date21-Year              pic 9(04).
              10 lnk-Colon1               pic x.
              10 Date21-Month             pic 9(02).
              10 lnk-Colon2               pic x.

           05.
              10 Date21-Day               pic 9(02).
              10 lnk-Colon3               pic x.
              10 Date21-Hours             pic 9(02).
              10 lnk-Colon4               pic x.
              10 Date21-Minutes           pic 9(02).

        Procedure Division returning lnk-Date.

         move function Current-Date  to Date21
         move CORR Date21            to lnk-Date
         move ":" to lnk-Colon1, lnk-Colon2, lnk-Colon3, lnk-Colon4

        End Method "getDateModified".
        *>--------------------------------------------------------------
        Method-id. "getMonthYearObject".       *> PUBLIC
        *>--------------------------------------------------------------

        *> lnk-date6 is returned as an object reference. As it is
        *> being used with a MultipleLineEntry field :   "^Jan^2005".
        *> Note the space prior to '2005' causes the MLE to wrap-around
        *> so that the date is displayed in a MLE width a width of 4
        *> as :-
        *>                      ^Jan
        *>                      2005
        *>
        Local-storage section.
        01 ls-date6.
           05 ls-year4                   pic 9(04).
           05 ls-month2                  pic 9(02).
        01 ls-length                     pic x(4) comp-5.
        01 ls-month3                     pic x(03).
        01 ls-text.
           05 filler                     pic x.
           05 ls-text1                   pic x(03).
           05 filler                     pic x.
           05 ls-text2                   pic x(04).

        Linkage section.
        01 lnk-date6                     pic 9(06).
        01 lnk-DateObject                object reference.

        Procedure Division using     lnk-date6
                           returning lnk-DateObject.

         move lnk-date6  to ls-date6
         move spaces     to ls-text
         invoke self "getMonthAlpha3"
               using ls-month2 returning ls-month3
         initialize         ls-text
         move ls-month3  to ls-text1
         move ls-year4   to ls-text2
         move length of ls-text to ls-length
         invoke CharacterArray "withLengthValue"
              using ls-length, ls-text returning lnk-DateObject

        End Method "getMonthYearObject".
        *>--------------------------------------------------------------
        Method-id. "getYearMonthObjects".        *> PUBLIC
        *>--------------------------------------------------------------
        Local-storage section.
        01 ls-dateN.
           05 ls-year4                   pic 9(04).
           05 ls-month2                  pic 9(02).
           01 ls-length                  pic x(4) comp-5.
        01 ls-month3                     pic x(03).
        Linkage section.
        01 lnk-date6                     pic 9(06).
        01 lnk-DateObjects.
           05 lnk-year                   object reference.
           05 lnk-month                  object reference.

        Procedure Division using     lnk-date6
                           returning lnk-DateObjects.

         move lnk-date6  to ls-dateN
         move length of ls-year4 to ls-length
         invoke CharacterArray "withLengthValue"
            using ls-length, ls-year4 returning lnk-year
         invoke self "getMonthAlpha3"
            using ls-month2 returning ls-month3
         move length of ls-month3 to ls-length
         invoke CharacterArray "withLengthValue"
           using ls-length, ls-month3 returning lnk-month

        End Method "getYearMonthObjects".
        *>--------------------------------------------------------------
        Method-id. "getDateTime19".     *> PUBLIC
        *>--------------------------------------------------------------

        *> Returns a standard printer header Date block, in format :-
        *>
        *>                   2003^May^27^^^14:57

        Working-storage section.
        01 ls-Date.                    *> ccyymmmdd
           05 ls-dateYear              pic 9(04).
           05                          pic x.
           05 ls-dateMonth             pic x(03).
           05                          pic x.
           05 ls-dateDay               pic z9.
           05                          pic x(03).
           05 ls-Hours                 pic 99.
           05 ls-colon                 pic x.
           05 ls-Minutes               pic 99.

        Linkage section.
        01 lnk-DateAndTime             pic x(19).

        Procedure Division returning lnk-DateAndTime.

          move function Current-Date       to Date21
          initialize ls-Date
          move Date21-Year                 to ls-dateYear
          invoke self "getMonthAlpha3"
            using Date21-Month returning ls-dateMonth
          move Date21-Day                  to ls-dateDay
          move Date21-Hours                to ls-Hours
          move ":"                         to ls-colon
          move Date21-Minutes              to ls-Minutes
          move ls-Date                     to lnk-DateAndTime

        End Method "getDateTime19".
        *>---------------------------------------------------------------
        Method-id. "getMonthAlpha3".     *> PRIVATE
        *>--------------------------------------------------------------
        Linkage section.
        01 lnk-month-in          pic 9(02).
           88 ValidMonth         value  1 thru 12.
        01 lnk-month-out         pic x(03).

        Procedure Division using lnk-month-in
                           returning lnk-month-out.

          if    ValidMonth
                move MonthName (lnk-month-in) to lnk-month-out

          else  move spaces to lnk-month-out
          End-if

        End Method "getMonthAlpha3".
        *>--------------------------------------------------------------
        Method-id. "getMonthYearText".    *> PUBLIC
        *>--------------------------------------------------------------
        Local-storage section.
        01 ls-date6.
           05 ls-year                    pic 9(04).
           05 ls-month                   pic 9(02).

        Linkage section.
        01 lnk-DateIn                    pic 9(06).
        01 lnk-DateOut.
           05 lnk-datemonth              pic x(03).
           05                            pic x.
           05 lnk-dateyear               pic x(04).

        Procedure Division using     lnk-DateIn
                           returning lnk-DateOut.

          move lnk-DateIn               to ls-date6
          move spaces                   to lnk-DateOut
          move ls-year                  to lnk-dateyear
          invoke self "getMonthAlpha3"
                 using ls-month returning  lnk-datemonth

        End Method  "getMonthYearText".
        *>------------------------------------------------------------
        Method-id. "setCCYYMMcheck".            *> PUBLIC
        *>------------------------------------------------------------
        *> If the Business class whishes to control the
        *> validity of dates entered, Business Class invokes its
        *> instance of DateAndTime to retrieve currentDate. The
        *> Business class stores the 'check date' as appropriate.
        *> Additionally, where dates are used with Dialogs the 'check
        *> date' is passed to Tabbed Dialog, which in turn puts the
        *> 'date check' in its own instance of DateAndTime

        *> Initial values for yymm4 and ccyymm6 are zeroes.

        Linkage section.
        01 lnk-ccyymm                   pic 9(06).
        Procedure Division using lnk-ccyymm.

        move lnk-ccyymm(3:4) to yymm4
        move lnk-ccyymm      to ccyymm6

        End Method "setCCYYMMcheck".
        *>------------------------------------------------------------
        Method-id. "validateCCyymm".    *> PUBLIC
        *>------------------------------------------------------------
        Local-storage section.
        01 ls-date6.
           05 ls-cc                      pic 9(02).
              88 ValidCentury            value 19 thru 20.
           05 ls-yy                      pic 9(02).
           05 ls-month                   pic 9(02).
              88 ValidMonth              value  1 thru 12.

        Linkage section.
        01 lnk-date6                     pic x(06).
        01 lnk-result                    pic x(4) comp-5.

        Procedure Division using lnk-date6 returning lnk-result.

          move zeroes to lnk-result

          Evaluate true
             when lnk-date6 not numeric
                  move 99 to lnk-result
             when other
                  move lnk-date6 to ls-date6

                  Evaluate true
                     when not ValidCentury
                     when not ValidMonth
                          move 99 to lnk-result
                     when ccyymm6 <> zeroes

                       if ls-date6 > ccyymm6
                          move 99 to lnk-result
                       End-if
                  End-evaluate

          End-evaluate

        End Method "validateCCyymm".
        *>------------------------------------------------------------

        End OBJECT.
        End CLASS DateAndTime.

        *>-------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-17T11:30:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<480dicFi0o1lU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <6nnSf.149866$sa3.103297@pd7tw1no>`

```
James J. Gavan<jgavandeletethis@shaw.ca> 03/16/06 5:26 PM >>>
>Frank Swarbrick wrote:
>> Could one "simulate" a private method using "nested methods"?  Not sure
if
>> this is even allowed, but...
>> 
…[8 more quoted lines elided]…
>you have to 'invent' private methods ?

I wasn't being tongue in cheek at all.   I just was wonder how, if there's
no "private" or "public" attribute in COBOL, you could make methods that can
be invoked from within other methods of that class but not from anything
outside of the class.  (Not sure if that's clear, but...)

I honestly haven't read your entire message, yet, but all I was wondering
was if the comments I have made in the following are, in fact, true:

class-id. myClass.
object.
method-id. method1.
procedure division.
    display "in public method1"
*   allowed because private-method1 is nested inside method1?
    invoke self "private-method1"
*   allowed because private-method2 is global and nested inside method2
which is inside this object?
    invoke self "private-method2"
    exit method.

method-id. private-method.
procedure division.
    display "in private-method1"
    exit method.
end method private-method1.
end method method1.

method-id. method2.
procedure division.
    display "in public method2"
*   allowed because private-method2 is nexted inside method2?
    invoke self "private-method2"
*   not allowed because private-method1 is nested inside method1 and is not
global?
    invoke self "private-method1"
    exit method.

method-id. private-method2 is global.
procedure division.
    display "in private-method2"
    exit method.
end method private-method2.
end method method2.
end object.
end myClass.

program-id. myootest.
working-storage section.
77 myObj object reference myClass.
procedure division.
    invoke myClass "new" returning myObj
*   the following two are allowed.
    invoke myObj "method1"
    invoke myObj "method2"
*   the following two are not allowed because they are nested inside other
methods??
    invoke myObj "private-method1"
    invoke myObj "private-method2"
end program myootest.


I will read through your message later.
Thanks,
Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-17T11:45:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142624726.285789.135120@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<480dicFi0o1lU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net>`

```
> *   the following two are not allowed because they are nested inside other
>methods??
>    invoke myObj "private-method1"
>    invoke myObj "private-method2"

While nested methods (or nested functions in Pascal) may have some
trivial utility, they are not particularly useful for exactly that
reason.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 5)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-17T20:39:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8FSf.62$nQ6.59@clgrps13>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1142624726.285789.135120@i39g2000cwa.googlegroups.com...
>> *   the following two are not allowed because they are nested inside 
>> other
…[7 more quoted lines elided]…
>

I believe PHP allows nested functions, and has a single, global namespace. 
If a function A is only ever used by function B, it may make sense to nest 
function A inside of function B to avoid a namespace collision.

    - Oliver
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-17T15:57:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142639830.961493.124390@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<p8FSf.62$nQ6.59@clgrps13>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13>`

```
> If a function A is only ever used by function B, it may make sense to nest
> function A inside of function B to avoid a namespace collision.

If it is only ever used by B then it may make sense to have it as
inline code rather than making it into a function.

If it causes a namespace collision then the 'next programmer' may be
confused about which function is being called.

But then I dislike PHP and the whole approach of mixing code and
content.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-17T18:55:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4817ldFhmr0jU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <1142639830.961493.124390@i40g2000cwc.googlegroups.com>`

```
Richard<riplin@Azonic.co.nz> 03/17/06 4:57 PM >>>
>> If a function A is only ever used by function B, it may make sense to
nest
>> function A inside of function B to avoid a namespace collision.
>
…[7 more quoted lines elided]…
>content.

What if B wished to call function (method) A from several different places,
but we still want to hide it from the outside world?  I see "private"
methods and functions as being very useful.  Not to override a global
function, necessarily, but just to have functions that only have meaning
within a particular class, and can't be directly invoked from outside the
class.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 7)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-18T19:32:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvhn8v0vtq@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142639830.961493.124390@i40g2000cwc.googlegroups.com>`

```

In article <1142639830.961493.124390@i40g2000cwc.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> > If a function A is only ever used by function B, it may make sense to nest
> > function A inside of function B to avoid a namespace collision.
> 
> If it is only ever used by B then it may make sense to have it as
> inline code rather than making it into a function.

There are many cases where this is not true - for example, when the
most reasonable design for B has it call A from multiple places.

Private functions are a perfectly reasonable technique that has been
used to fine effect for decades.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-21T14:04:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142978699.388096.248020@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dvhn8v0vtq@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142639830.961493.124390@i40g2000cwc.googlegroups.com> <dvhn8v0vtq@news4.newsguy.com>`

```

Michael Wojcik wrote:

> Private functions are a perfectly reasonable technique that has been
> used to fine effect for decades.

But they ain't private methods, nor can they act as private methods,
they cannot be accesed from other functions or methods in the same file
at the level of their parent.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 9)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-23T05:55:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvtd9c02pmu@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142978699.388096.248020@j33g2000cwa.googlegroups.com>`

```

In article <1142978699.388096.248020@j33g2000cwa.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> 
> Michael Wojcik wrote:
…[4 more quoted lines elided]…
> But they ain't private methods,

There are obvious counterexamples.  In C, for example, there is no
language construct for "methods" distinct from functions; OO in C has
to be constructed by the programmer (and has been any number of
times), and that construction can certainly use private functions to
implement private methods.

> nor can they act as private methods,

How do "private methods" act that is impossible for private functions?

> they cannot be accesed from other functions or methods in the same file
> at the level of their parent.

I'm afraid you lost me there.  I'm not sure what construct you're
describing.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-23T00:52:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143103941.634178.3400@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<dvtd9c02pmu@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1142978699.388096.248020@j33g2000cwa.googlegroups.com> <dvtd9c02pmu@news4.newsguy.com>`

```

Michael Wojcik wrote:

> There are obvious counterexamples.  In C, for example, there is no
> language construct for "methods" distinct from functions;

There is however a 'private' construct, a static function is only
available to other functions in the same file.

> OO in C has
> to be constructed by the programmer

Or just use cflow.

> How do "private methods" act that is impossible for private functions?

The question should be: how do 'private methods' act that is impossible
for 'nested functions'.

> > they cannot be accesed from other functions or methods in the same file
> > at the level of their parent.
>
> I'm afraid you lost me there.  I'm not sure what construct you're
> describing.

If I have a class with several public methods, say A, B, and C, then I
can have, in Java, a 'private' method that can be accessed from A and B
but is not visible outside the class. A nested method within, say, A
would, if it were allowed, be available to A but not to B or C.

In the same way a nested function in Pascal is only available to the
function that contains it whereas in C a static function could be
accessed by any function in the same file while still being private and
not available to other functions in the same program.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 11)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-28T23:03:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0cfc609ch@news1.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1143103941.634178.3400@g10g2000cwb.googlegroups.com>`

```

In article <1143103941.634178.3400@g10g2000cwb.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> Michael Wojcik wrote:
> 
…[4 more quoted lines elided]…
> available to other functions in the same file.

I don't see how that's relevant to my point.  You distinguished
"methods" from "functions", in text that you unfortunately snipped.
I wrote that "private functions are a perfectly reasonable
technique"; you replied that "they ain't private methods"; my
response, quoted above, is that sometimes they *are* private methods,
insofar as the target language is concerned.

The existence in C of a facility for creating "private functions"
(which you mischaracterize, BTW; applying the "static" sc-specifier
to a function declaration restricts the linkage of that function to
the *remainder* (not the entirety) of the current translation unit;
and that function can still be made "available" to functions in other
TUs by returning a pointer to it from another function in the current
TU, for example) only supports my point.

> > OO in C has to be constructed by the programmer
> 
> Or just use cflow.

cflow generates a call graph from C source.  Are you thinking of
cfront, the original C++ implementation that translated C++ to C?
That's a C++ implementation, not a C implementation.  Its use of C
as an intermediate language is only an implementation detail.

(The language implemented by cfront isn't ISO C++, but that's
beside the point.)

> > How do "private methods" act that is impossible for private functions?
> 
> The question should be: how do 'private methods' act that is impossible
> for 'nested functions'.

In a strict sense, they don't, of course; that follows right from
Kolmogorov complexity theory.

And if that's the question, what's the answer?  I'm not the one
advocating private methods in this discussion; I'm arguing that there
are advantages to nested functions.  (Obviously those advantages have
nothing to do with computing power, per the previous paragraph.  The
advantages of nested functions are coupling reduction and that sort
of thing.)

> > > they cannot be accesed from other functions or methods in the same file
> > > at the level of their parent.
…[12 more quoted lines elided]…
> not available to other functions in the same program.

Yes, but so what?  They're different constructs with different
scoping rules.  The existence of one doesn't in itself say anything
about the other.  Private methods have potentially wider scope than
nested functions; nested functions, on the other hand, have access to
their caller's environment.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-28T16:34:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143592498.036316.132980@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<e0cfc609ch@news1.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1143103941.634178.3400@g10g2000cwb.googlegroups.com> <e0cfc609ch@news1.newsguy.com>`

```

Michael Wojcik wrote:

> > There is however a 'private' construct, a static function is only
> > available to other functions in the same file.
>
> I don't see how that's relevant to my point.  You distinguished
> "methods" from "functions", in text that you unfortunately snipped.

Because it was irrelevant to my point. Having a nested piece of code
that is only available to the single piece that it is nested within is
only trivally useful to me. The discussion was nested vs unnested but
private/local.

> I wrote that "private functions are a perfectly reasonable
> technique"; you replied that "they ain't private methods";

What you wrote seemed to be entirely related to nested functions. While
they are a reasonable technique, I have never found them useful.

Private methods, as implemented in Java are not nested within other
methods and therefore are much more useful.  For example if there are
several constructors then they all use the common code in a private
method without exposing that.

> my
> response, quoted above, is that sometimes they *are* private methods,
> insofar as the target language is concerned.

> The existence in C of a facility for creating "private functions"
> (which you mischaracterize, BTW; applying the "static" sc-specifier
> to a function declaration restricts the linkage of that function to
> the *remainder* (not the entirety) of the current translation unit;

No, I did not mischaracterise them at all.  I never mentioned or
implied _all_, but they can be made available to all either by placing
them at the start of the file or by including a prototype or
declaration at the start (which I routinely do anyway for all
functions, or actually I have utility do it for me).

> and that function can still be made "available" to functions in other
> TUs by returning a pointer to it from another function in the current
> TU, for example) only supports my point.

But that 'other function' that is returning the pointer must be in the
file where the function is static, so it can only be made available
from within the file.

> > > OO in C has to be constructed by the programmer
>
> cflow generates a call graph from C source.  Are you thinking of
> cfront, the original C++ implementation that translated C++ to C?

Quite right: cfront.

> That's a C++ implementation, not a C implementation.  Its use of C
> as an intermediate language is only an implementation detail.

The OO language that cfront implemented, C with Classes, after much
enhancement, came to be called C++, yes.

But it does give 'OO in C' that is not 'contructed by the programmer'.

> (The language implemented by cfront isn't ISO C++, but that's
> beside the point.)

Thank you for confirming that cfront is _not_ C++, though C++ was
derived from it.

> > > How do "private methods" act that is impossible for private functions?
> >
…[11 more quoted lines elided]…
> of thing.)

Whatever. The advantages _to_me_ are whether I can write more reliable
progroms faster, I neither know nor care about 'coupling reduction' or
how complex Kolmogrov can make things.

> Yes, but so what?  They're different constructs with different
> scoping rules.  The existence of one doesn't in itself say anything
> about the other.

Well, exactly. That is why I argued that using nested (piece of code)
as a substitute for the unavailability of a peer level private (piece
of code) was not very useful.

> Private methods have potentially wider scope than
> nested functions;

And the point of private/static is to restrict that scope to where it
is needed.

> nested functions, on the other hand, have access to
> their caller's environment.

Doesn't that conflict with 'coupling reduction' ?
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 13)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-30T21:13:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0hhlg01fgp@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1143592498.036316.132980@u72g2000cwu.googlegroups.com>`

```

In article <1143592498.036316.132980@u72g2000cwu.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> Michael Wojcik wrote:
> 
…[9 more quoted lines elided]…
> private/local.

OK.  I was confused by your previous post; this one has cleared
things up.  I think we're generally in agreement on the differences
among nested functions, file-scope private functions, and private
methods in C++-style OO languages.

> > I wrote that "private functions are a perfectly reasonable
> > technique"; you replied that "they ain't private methods";
> 
> What you wrote seemed to be entirely related to nested functions. While
> they are a reasonable technique, I have never found them useful.

Fair enough.  Most of my work is in C, which as we've already noted
lacks nested functions, and I get along fine there without them. If C
had them, there are constructs where I'd use them, just as I use all
of C's flow-control mechanisms; but I can understand that not
everyone finds them to their liking.  Not all carpenters want to use
a mortising machine when a chisel can do the job just as well.

Personally, I like to have lots of tools available, which is why I
like languages like OCaml, which offers all three of the alternatives
we're discussing here.  (Does Ruby?  I think it might, though I
haven't used it enough to know for certain off the top of my head.)

> > [cfront is] a C++ implementation, not a C implementation.  Its use of C
> > as an intermediate language is only an implementation detail.
…[4 more quoted lines elided]…
> But it does give 'OO in C' that is not 'contructed by the programmer'.

Here we'll have to disagree.  I don't think cfront provided OO in
C; I think it implemented a different language, just as if I wrote
a COBOL compiler that generated C as an intermediate language.  But
that's a minor point.

> Whatever. The advantages _to_me_ are whether I can write more reliable
> progroms faster, I neither know nor care about 'coupling reduction' or
> how complex Kolmogrov can make things.

Some people care about how cars are engineered; some just want one
that will do a decent job of getting them from point A to point B.

> > nested functions, on the other hand, have access to
> > their caller's environment.
> 
> Doesn't that conflict with 'coupling reduction' ?

Not exactly, any more than say adding parameters (which all else
being equal increases coupling) to a function necessarily increases
the coupling of the program as a whole - because the new parameters
may take the place of global variables, which have wider scope and
so more coupling.

So a nested function's closure includes the parent's environment and
parameters, which in itself does increase coupling, but the avail-
ability of function nesting allows constructs with less coupling than
the alternatives, in some situations.  The parent's environment acts
like additional parameters to the child, but they're "automatically"
provided by the compiler (like the "this" parameter to object methods
in C++-style languages), so they have relatively little coupling (or
their coupling is lightweight, which comes down to the same thing).
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 14)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-30T17:33:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<493bmeFmoaepU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1143592498.036316.132980@u72g2000cwu.googlegroups.com> <e0hhlg01fgp@news4.newsguy.com>`

```
Michael Wojcik<mwojcik@newsguy.com> 03/30/06 2:13 PM >>>
>
>Personally, I like to have lots of tools available, which is why I
>like languages like OCaml, which offers all three of the alternatives
>we're discussing here.  (Does Ruby?  I think it might, though I
>haven't used it enough to know for certain off the top of my head.)

I was fooling around with nested methods in Ruby the other day.  It does
appear to allow them, but it doesn't seem to hide them from code outside of
the method in which it is nested.  For example...

def outerMethod my_parm
  def innerMethod a_parm
    puts a_parm
  end
  innerMethod "#{my_parm}: This is a test"
end

outerMethod "Invoking outer method"
innerMethod "Invoking innter method directly"

If I recall correctly I did *not* get an error when attempting to invoke
innerMethod from outside of outerMethod.  That being the case I'm not sure
what the point of allowing nested methods is in Ruby.  I'm probably missing
something.  I may post a message to the Ruby newsgroup asking about it.

What were the other two of the "three alternatives" you mention above?

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 15)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-31T21:42:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0k7nu02nb9@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <493bmeFmoaepU1@individual.net>`

```

In article <493bmeFmoaepU1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> Michael Wojcik<mwojcik@newsguy.com> 03/30/06 2:13 PM >>>
> >
…[11 more quoted lines elided]…
> what the point of allowing nested methods is in Ruby.

Well, even if nesting does not limit the scope of the method
identifier to the enclosing method, it still gives (or should give)
the inner method access to the environment formed by the outer
method's closure.  As I noted in one of my posts yesterday, this is
significant if, for example, the inner method is passed as a delegate
to an external method.

So there could still be *some* point, though not following the usual
scoping conventions seems a bit odd.

> What were the other two of the "three alternatives" you mention above?

Besides nested functions/methods, they were private functions (which
aren't nested but are defined in a limited scope of some sort,
typically to the source file or part of it) and private methods
(which are accessible only from other methods in the class which
defines them).

OCaml has all three because it's an ML derivative, and the original
ML wasn't OO (though it has its own brand of polymorphism).  Like
other functional languages, ML has nested functions - in fact it has
unnamed, dynamic functions, so you can nest functions arbitrarily
deeply at runtime by creating closures.  Then OCaml added OO (and
private members) and the module system (which provides file-scope
private functions, in effect).

Dynamic closures, by the way, are a fourth kind of "local function"
that I think a language benefits from.  And Ruby's unnamed blocks
and yield operator (essentially a restricted but elegant coroutine
mechanism) are a fifth.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 16)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-31T17:38:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4960bgFmtancU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <493bmeFmoaepU1@individual.net> <e0k7nu02nb9@news4.newsguy.com>`

```
Michael Wojcik<mwojcik@newsguy.com> 03/31/06 2:42 PM >>>
>
>
…[17 more quoted lines elided]…
>mechanism) are a fifth.

I tried some stuff with Ruby last night and the only way I could get a
nested method to *not* be available from outside the method in which it was
nested was to declare it to be private.  I didn't get around to posting to
the Ruby newsgroup yet.  Ruby doesn't have functions, only methods, so of
course it does not have private functions.  (Actually I'm not sure if your
reference to function up there refers to regular C-style functions or to
"functional programming" functions.  In any case, I don't think Ruby has
either.)  It does have private (and protected) methods.

It looks like Ruby has, as well as unnamed blocks, some sort of "closure"
functionality.  I'm not sure I have a good grasp of it, but I just found an
interesting article that discusses it.  You might like to take a look.
http://www.artima.com/intv/closures.html 

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 17)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-04-03T15:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0rfuv02ptn@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <4960bgFmtancU1@individual.net>`

```

In article <4960bgFmtancU1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> 
> It looks like Ruby has, as well as unnamed blocks, some sort of "closure"
> functionality.  I'm not sure I have a good grasp of it, but I just found an
> interesting article that discusses it.  You might like to take a look.
> http://www.artima.com/intv/closures.html 

Thanks for the link.  In fact, that piece suggests that Ruby has full-
blown continuations (which let you capture the whole state of a
computation and then resume it at a later time, possibly in a
different location in the process), not just closures, which would be
nice.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 18)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2006-04-04T06:39:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AwoYf.391$Es3.354@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<e0rfuv02ptn@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <4960bgFmtancU1@individual.net> <e0rfuv02ptn@news4.newsguy.com>`

```
Michael Wojcik wrote:
> In article <4960bgFmtancU1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> 
…[10 more quoted lines elided]…
> nice.

All right, now...  Here I think I'm finally getting a bit of a handle on 
closures and you have to go an introduce yet another programming feature 
I've never heard of!  :-)

Frank
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 19)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-04-05T14:53:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e10llh01ipq@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <4960bgFmtancU1@individual.net> <e0rfuv02ptn@news4.newsguy.com> <AwoYf.391$Es3.354@newsread3.news.atl.earthlink.net>`

```

In article <AwoYf.391$Es3.354@newsread3.news.atl.earthlink.net>, Frank Swarbrick <infocat@sprynet.com> writes:
> Michael Wojcik wrote:
> > 
…[8 more quoted lines elided]…
> I've never heard of!  :-)

That's OK.  I studied closures and continuations and all that stuff
in college, but I run across computing concepts I've never heard of
before pretty much every day on the OCaml newsgroup.

There's a short introduction to continuations at:

   http://www.madore.org/~david/computers/callcc.html

Basically, a continuation lets you save the state of what you're
doing at the moment, and then resume it later on.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-28T16:55:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143593716.809374.209740@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<e0cfc609ch@news1.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <1143103941.634178.3400@g10g2000cwb.googlegroups.com> <e0cfc609ch@news1.newsguy.com>`

```

Michael Wojcik wrote:

> (which you mischaracterize, BTW; applying the "static" sc-specifier
> to a function declaration restricts the linkage of that function to
> the *remainder* (not the entirety) of the current translation unit;

Just to clarify your observation about whether I 'mischaracterised'
static, here is an extract from my first post in this thread:

"""If ´static´ is applied to a declaration outside a function within
a
file then this makes it  created staticly but not available outside the
file (ie not available from other source files in the same program. It
is ´file local´ and available to all following functions.

If a function is declared ´static´ then it too is ´file local´. """

You may note the use of 'following'.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-18T19:31:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvhn600vt1@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <47rnfqFgnjfbU1@individual.net> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13>`

```

In article <p8FSf.62$nQ6.59@clgrps13>, "Oliver Wong" <owong@castortech.com> writes:
> 
> "Richard" <riplin@Azonic.co.nz> wrote in message 
…[9 more quoted lines elided]…
> > reason.

In some cases, that's precisely what makes them useful.  Restricting
access to portions of code improves abstraction and reduces coupling,
both of which can improve reliability and ease of maintenance.

> I believe PHP allows nested functions, and has a single, global namespace. 
> If a function A is only ever used by function B, it may make sense to nest 
> function A inside of function B to avoid a namespace collision.

Namespace scope is only one effect of nested functions.  Often the
more significant effect is that a nested function, in most languages,
has access to the active frame in the parent function from which it
was called.  That means nested functions operate in dynamic closures.
They have access to the values of parameters and local variables in
the parent at the time they were called.

This has particularly interesting results in the case of recursive
inner and outer functions (and even more so if they're mutually
recursive).  Like all high-level constructs, it can be manually
implemented in languages that don't support nested functions; having
it as a built-in is just a convenience for the programmer.  The
downside is that the compiler has to generate code for the runtime to
maintain visibility to the enclosing environment.  (The two common
techniques for that are called "static chains" and "displays", and
are described in compiler texts.)

That's why C, for example, doesn't have nested functions -
eliminating them makes the compiler simpler and easier to port.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-28T18:46:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143600398.529957.304970@e56g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<dvhn600vt1@news4.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <dvhn600vt1@news4.newsguy.com>`

```

Michael Wojcik wrote:

> That's why C, for example, doesn't have nested functions -
> eliminating them makes the compiler simpler and easier to port.

Ritchie, Kernighan et al in the Bell System Technical Journal of
July-August 1978 writing on nested functions in C, or the lack of them:

"""It has turned out that the ability to make certain functions and
data invisible to programs in other files(by explicity declaring them
'static') is sufficient to provide one of their most important
functions, namely hiding their names from other functions."""

So while the lack simplifies the implementation, they are replaced by,
what I consider, a better mechanism.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-29T09:37:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48vrfdFlpo57U1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <dvhn600vt1@news4.newsguy.com> <1143600398.529957.304970@e56g2000cwe.googlegroups.com>`

```
Richard<riplin@Azonic.co.nz> 03/28/06 7:46 PM >>>
>
>Michael Wojcik wrote:
…[13 more quoted lines elided]…
>what I consider, a better mechanism.

But why use the keyword "static" in that case?  Wouldn't the keyword
"private" make more sense?  I'm sure they used "static" because it was
already a keyword so they just figured they'd reuse it, but it certainly is
not obvious (to me, anyway) that declaring a function as "static" simply
hides the function from the outside world...

Nonetheless, nested functions could still serve a possibly purpose.  I can't
think of a "real life" example, but....

/* funcs.c */
void dosomethinghere();
void dosomethingelsehere();

int func1()
{
    int dosomething()  // should this be prefixed with static?
    { 
        dosomethinghere();
    }

    return dosomething();
}

int func2()
{
    int dosomething()  // should this be prefixed with static?
    { 
        dosomethingelsehere();
    }

    return dosomething();
}

/* main.c */
int main()
{
    return func1() + func2();
}

In this admittedly contrived example both func1 and func2 call
"dosomething()", but they each call their own special version of
dosomething, one which calls dosomethinghere and one which calls
dosomethingelsehere.  I'm sure there are other ways to get the same result,
but personally I find this to be very readable...



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 9)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-29T17:26:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rzWf.15986$K11.3507@clgrps12>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <dvhn600vt1@news4.newsguy.com> <1143600398.529957.304970@e56g2000cwe.googlegroups.com> <48vrfdFlpo57U1@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:48vrfdFlpo57U1@individual.net...
>
> Nonetheless, nested functions could still serve a possibly purpose.  I 
> can't
> think of a "real life" example, but....

Maybe something like this:

function a() {
  function b(int value) {
    //do something complex, taking up several lines of code.
  }

  if (someCondition) {
    doStuff;
    b(someValue)
    while(someOtherCondition) {
      doMoreStuff
      b(anotherValue);
    }
    if (yetAnotherCondition) {
      b(yetAnotherValue);
    }
  } else {
    for (int i = 0; i < someLimit; i++) {
      doSomethingElse;
      if (someConditionInvolingI) {
        b(i);
      }
    }
  }
}

    You'd like to avoid copy and pasting the code for b() at several 
locations, but nobody uses b() except for a(), so you'd like for b() to only 
be visible to a().

    I don't do any C programming, but this comes up in PHP for me. I'll 
sometimes be writing an API library for someone else to use, and I want to 
provide a() to them, but I want to hide b(), since all the functions share a 
global namespace. The compromise I do prefix the filename before the names 
of tthe "hidden" functions. E.g, if the file was "tokenGeneration.php":

function a() {
  //As above, but without nested function b.
}

function tokenGeneration_b() {
  //As above
}

    The API was for generating a unique "security token" (arbitrary string 
of characters, like those CD keys you need to type in to install some 
software), and the b's were various methods involving database 
initialization, alphabet rotation, etc. The client didn't care about all of 
that stuff, but just wanted a(), a method which is guaranteed to return a 
new random token which was not already present in the database.

    - Oliver
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-29T12:16:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143663387.970398.76880@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9rzWf.15986$K11.3507@clgrps12>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <480dicFi0o1lU1@individual.net> <dvhn600vt1@news4.newsguy.com> <48vrfdFlpo57U1@individual.net> <9rzWf.15986$K11.3507@clgrps12>`

```

Oliver Wong wrote:

> Maybe something like this:
>
…[27 more quoted lines elided]…
> be visible to a().

The C idiom is to use many small source files. It would be usual to put
a() in its own fle with b() as a static function plus any other
functions that want to use b().

Pascal, however, was designed by Wirth so that the whole source program
was in one file and compiled all at once. This made it necessary to use
nested functions to make them local.

>     I don't do any C programming, but this comes up in PHP for me. I'll
> sometimes be writing an API library for someone else to use, and I want to
> provide a() to them, but I want to hide b(), since all the functions share a
> global namespace. The compromise I do prefix the filename before the names
> of tthe "hidden" functions. E.g, if the file was "tokenGeneration.php":

Yes, each language has to create an idiom that deals with its
limitations. PHP was not designed to be more than a simple HTML
generator (Private Home Page) but has had to try to growup to cater for
more needs.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 10)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-30T21:50:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0hjr102mg0@news1.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <dvhn600vt1@news4.newsguy.com> <1143600398.529957.304970@e56g2000cwe.googlegroups.com> <48vrfdFlpo57U1@individual.net> <9rzWf.15986$K11.3507@clgrps12>`

```

In article <9rzWf.15986$K11.3507@clgrps12>, "Oliver Wong" <owong@castortech.com> writes:
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
> news:48vrfdFlpo57U1@individual.net...
…[4 more quoted lines elided]…
> Maybe something like this:

[snip example of nested function called at multiple points]

Like Frank's example of multiple functions with the same name (which
scoping mechanisms *are* often used for, though more often with
variables than with functions), this is indeed a possible use of nested
functions.  I think I mentioned something similar in another post.

Another use is as delegates in various constructs.  For example,
in a made-up language for purposes of illustration:

   PrintObjectsWithAttribute(c : collection of myObject, a : attribute)
      PrintObjectIfAttribute(o : Object)
         begin
         myObject m = o
         if m.attribute = a
            print m
         end

      begin
      // Iterate is a generic collection-iteration function in the
      // visitor pattern - it will call the specified function on
      // every item in the collection.
      Iterate(c, PrintObjectIfAttribute)
      end

Here the visitor delegate PrintObjectIfAttribute is a closure that
captures the parent's parameter a, allowing it to perform the
necessary comparison.  The Iterate iteration function is completely
generic; it always takes a collection and a function that takes a
single parameter which is itself a generic object.  It doesn't need
any mechanism for passing arbitrary data to the delegate because the
caller can wrap that into the delegate's closure.

There are plenty of ways to do similar things in languages without
nested functions; I do this sort of thing (visitor patterns) fre-
quently in C, just by having the iterator take a pointer to untyped
data and pass it on to the delegate.  But some form of dynamic
closure (whether that's nested functions or dynamic functions or
perhaps something else) is more elegant, because the language does
more of the work for you.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-29T12:06:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143662805.587290.125180@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<48vrfdFlpo57U1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <6nnSf.149866$sa3.103297@pd7tw1no> <480dicFi0o1lU1@individual.net> <1142624726.285789.135120@i39g2000cwa.googlegroups.com> <p8FSf.62$nQ6.59@clgrps13> <dvhn600vt1@news4.newsguy.com> <1143600398.529957.304970@e56g2000cwe.googlegroups.com> <48vrfdFlpo57U1@individual.net>`

```

Frank Swarbrick wrote:

> But why use the keyword "static" in that case?  Wouldn't the keyword
> "private" make more sense?

I never found the use of 'static' a problem. You may need to read the
compiler source of the original C compiler to know why, it may be that
a particular compiler table is used for all 'static' items.

>  I'm sure they used "static" because it was
> already a keyword so they just figured they'd reuse it, but it certainly is
> not obvious (to me, anyway) that declaring a function as "static" simply
> hides the function from the outside world...

Static = stays in one place.

> Nonetheless, nested functions could still serve a possibly purpose.  I can't
> think of a "real life" example, but....
…[35 more quoted lines elided]…
> but personally I find this to be very readable...

Why would you use exactly the same name for two quite different things
? Why would you confuse the next programmer to whom it may not be
immediately obvious that there are two things with one name ?

If dosomething() within each is only used once then why not just inline
it and not have a name at all. With C each block can declare local
variables so that is not a reason to have nested (pieces of code).

int main()
{
       int a;

       if ( ... )
           {
           int b;
           char s(80);

           some code using b and s and can use a
            for (int i = 0 ; .... < new i
                  {
                  int b;    <- new local b
                  some code using local b and i
                  }
           }
}

So the only advantage of named nested functions is that they can be
accessed from several points and parameters passed.  If they are used
from several places then they may be useful enough to use from other
functions as well.

But if you prefer nested functions you can do that - just use Pascal.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 9)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-03-30T21:36:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0hj1002kq9@news1.newsguy.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <48vrfdFlpo57U1@individual.net>`

```

In article <48vrfdFlpo57U1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> Richard<riplin@Azonic.co.nz> 03/28/06 7:46 PM >>>
> >
…[12 more quoted lines elided]…
> hides the function from the outside world...

Quite a few people have opined that the keyword "static" is used for
too many purposes by C.  C99 added a new one (in an array declarator
for an array-type function parameter, to indicate the minimum number
of elements in the actual parameter, which is even more bizarre),
prompting Peter Seebach's oft-quoted "It wouldn't be a new C standard
if it didn't give a new meaning to the word 'static'".

On the topic of the original C's reuse of "static" to mean both static
storage duration (for variables) and internal linkage (for variables
and functions), Dennis Ritchie wrote in comp.std.c:

   I've come to believe that my mother was unexpectedly startled 
   by the suggestion of a new keyword during her first pregnancy, 
   and when a tempter in the early 1970s formulated schemes to 
   avoid another one, the prenatal influence manifested itself.[1]

For C99, the committee was reluctant to add new keywords, since that
could break existing code.  Still, they added "restrict", which is in
the application namespace, and they added other keywords in the
implementation namespace (such as "_Bool").

To make up for it, C also has the "auto" keyword, which has no use.


1. <39ADAF09.C50FDBAB@bell-labs.com> 31 August 2000; see
http://groups.google.com/group/comp.std.c/msg/b9eb00765b95c690
```

#### ↳ Re: Constants, Static, Public, Private

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-03-16T15:53:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cSfSf.282$me6.91@clgrps13>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
Discalimer: I wasn't able to follow everything in this post either.

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:_M_Rf.147168$B94.59312@pd7tw3no...
> I'm still on the tack "Is FACTORY really necessary ?".

    Does there exist a program behaviour which could be implemented using 
the "FACTORY" keyword, but which could not be implemented without that 
keyword? I don't think so. I mean, before OO COBOL came around, there was no 
FACTORY keyword, and you did just fine, right?

    Does is the "FACTORY" keyword useful? Yes, it's very useful for 
methods/procedures which create new objects (i.e. which act as factories for 
those objects).

>
> CONSTANTS :
…[5 more quoted lines elided]…
>
[snip]

    As Richard and Sergey mentioned, Java has a seperate keyword for 
indicating that some variable is a constant: "final". It looks like this:

<example>
final int x = 3;
x = 4;
</example>

The compiler will give an error on the second line, saying that you can't 
redefine the value of a final variable.

However, as Sergey mentioned, you have a bit of flexibility with final 
variables in Java: The only restriction is that the variable MUST be 
assigned some value before the first time it's read, and once it is assigned 
a value, it cannot ever be assigned a value again.

<example>
final int x;
int y = x;
x = 3;
</example>

The above example produces an error because x was not assigned a value 
before it was read from (on the second line, the JVM will try to read from x 
to store the value it found there in y).

<example>
final int x;
if (someCondition) {
  x = 3;
} else {
  x = 4;
}
int y = x;
</example>

The above example compiles fine. The compiler can prove that x will be 
assigned some value before it reaches the line that reads "y = x", and it 
can also prove that x will not be assigned to twice.

>
> STATIC :
…[7 more quoted lines elided]…
> }

    To fully "get" what's going on here, I think one needs to really 
understand OO. First of all, there's a big difference between a class, and 
instances of that class. In this example:

<example>
class Foo {
  public void someMethod() {
    Foo bar = new Foo();
  }
}
</example>

Foo is a class, and bar is an instance of Foo. bar is not itself a class. 
Classes basically represent a class of objects (e.g. a class called "Dog" 
might represent the abstract concept of what a dog is like, and how it 
should behave, while a particular instance of "Dog" represents one 
particular dog). Now to further complicate things, in Java, there exists a 
class called "Class", which represents the abstract concept of what a class 
is like, and how a class should behave.

The "Foo" class, for example, has a method called "someMethod". That's a 
property of the particular instance of Class known as "Foo", just like the 
"has brown fur" is a property of the particular instance of Dog known as 
"Fido".

    So "bar" is an instance of the class "Foo", and "Foo" is an instance of 
the class "Class" (actually, it's even more complicated than that; I'm 
simplifying things a bit).

    In Java, when something has the "static" keyword, it means that this 
thing (it might be a field or a method for example) exists "at the class 
level". A static field "a" in class "Foo", for example, means that the field 
exists inside of "Foo" itself, and not in any of its instances. So if you 
have two instances of Foo, "bar1" and "bar2", and bar1 modifies "a", bar2 
will see the new value, because they are both refering to the same field 
which exists in Foo.

    If there's a field "b", which is NOT static, then it exists at the 
"instance level". So if bar1 modifies the value of b, bar2 will NOT see the 
new value, because it has its own copy of b which is completely independent 
of bar1's copy.

    So now, back to your example:

> class Example1 {
>   public static void main(String args[]) {
>     System.out.println("This is the output from Example1");
>   }
> }

What this code says is that there exists a class "Example1", which has a 
static method called "main", and which take a single argument, which is an 
array of Strings. Because it is static, you don't need to have an actual 
instance of Example1 to execute that method; you can execute it directly off 
the class itself.

Methods called "main" and which take an array of Strings has a special 
meaning *TO THE VIRTUAL MACHINE*, but *NOT TO THE COMPILER*. The compiler 
treats this method like any other method.

Usually when you want to run a Java program, you have to give the JVM the 
name of a class. Most JVMs are hardcoded to look for a static method called 
"main" on the provided class, and to execute it, passing as argument the 
command line parameters provided.

However, there exists 3rd party "Virtual Machines for Java" (not sure if 
they're legally allowed to be called "JVMs"), which might do something 
different (BlueJ for example, will try to create a new instance of the 
class, rather than executing its main method).

So technically, the above code is defining a static method in a class. 
Nothing more. But in practice, the programmer who wrote that class is 
probably implicitly relying on the fact that most JVMs will treat that 
method specially, and is depending on that special behaviour.

When you write a Java applet, you do NOT provide a static main method. You 
actually structure your code something like this:

<example>
class ExampleApplet extends Applet {
  public void init() {
    /*Do initialization stuff here*/
  }

  public void start() {
    /*This method is executed when the method "starts up", which is after 
the initialization. This method may be called more than once.*/
  }

  public void stop() {
    /*This method is usually called when the user navigates off the page 
containing the applet.*/
  }
}
</example>

Here, what the JVM will do is call the init method when the browser first 
downloads the applet, and then the start method whenever it wants to run the 
method (note that the applet is only initialized once, but might be started 
multiple times; for example, if the applet is saved in a cache, it is 
initialized upon first download, but every time the user views the page, the 
applet is started again).

Again, the compiler treats these methods as just "normal" methods, but the 
JVM treats them specially.

[snip]
> --------------------------------------------------------------------------
>
…[6 more quoted lines elided]…
> only method in the 'Dummy Factory'.

    Hope the above explanation clarified things.

>
> 2. Java Variables :
…[6 more quoted lines elided]…
> Level 78s, in either 'dummy Factory' or the Instance ?

    I don't know what you mean by "concrete" variables. If by that, you mean 
"not literal", as in a calculated expression, then yes. More formally, when 
you have an assignment statement, the left hand side of the assignment must 
refer to a variable, while the right hand side must be an expression. A 
literal is considered to be a valid (albeit very simple) expression. So 
these are both legal:

x = 3;
x = 3 + 5;

>
> - Are there situations where it is an absolute MUST to hold Static
> Variables in the 'dummy Factory' for access by Instance Methods, (i.e.,
> can a Java Instance invoke the 'Dummy Factory' methods ?).

    Instances methods can invoke static methods, but if a static method 
wants to invoke an instance method, it must specify WHICH instance it wants 
to invoke the method upon.

    That is, when you are "in" an instance method, you can access other 
instance methods because it's implied that the instance you're working with 
is the same instance that you're "inside" of. And you can access static 
methods, because it's implied that the class whose static methods you want 
to invoke is the class to which your instance belongs.

    I'll try to give an example:

<example>
class Dog {
  static String biologicalFamily = "mammal";
  String name;

  public Dog(String newName) {
    /*This is a constructor, because it has the same name as the class*/
    setName(newName);
  }

  public void setName(String newName) {
    this.name = newName;
  }

  public static void setFamily(String newBiologicalFamily) {
    Dog.biologicalFamily = newBiologicalFamily;
  }

  public void anInstanceMethod() {
    setName("Fido");
    setFamily("avian");
  }

  public static void aStaticMethod() {
    Dog myDog = new Dog("Spike");
    myDog.setName("Wolfie");
    myDog.setFamily("insect");
    Dog.setFamily("fish");
    setFamily("insect");
    Cat.setFamily("reptile");
  }
}

class Cat {
  public static void setFamily(String newBiologicalFamily) {
    /*Implementation goes here.*/
  }
}
</example>

I've made "biologicalFamily" a static variable because presumably all dogs 
belong to the same biological family. However, I made "name" an instance 
variable because each dog has its own name, which may be different from 
every other dog.

Now look at "anInstanceMethod". If I am "in" that method (meaning JVM is 
currently executing the code in that method), then there must already exist 
some instance of Dog, and that particular instance's "anInstanceMethod" 
method is the one that is running. So when I call setName("Fido"), the JVM 
doesn't wonder "Which dog's name should I set?" because it's implied that 
I'm talking about "this" dog. I.e. the dog whose instance method I'm 
currently running.

When I call setFamily("avian"), the JVM doesn't have to ask "Which dog?" 
because the family actually applies to ALL dogs. It's a class level 
variable, rather than an instance level variable.

Now look at "aStaticMethod". When I call setName("Wolfie"), I have to 
specify which dog I'm speaking about, because "aStaticMethod" exists at the 
class level, and not with any particular instance. So the statement reads 
myDog.setName("Wolfie"), specifying that the dog whose name should be set is 
"myDog".

Next we have the statement myDog.setFamily("insect"). This is a bit "weird", 
and actually the compiler will generate a warning here, but the code is 
valid. Although I specify "myDog", the JVM will ignore this, because 
setFamily is a static method, and thus it applies to ALL dogs. The warning 
message that the compiler produces will read something like "Don't specify 
an instance when calling a static method".

Finally, there's the statement Dog.setFamily("fish"). This is perfectly fine 
code, and the compiler will produce neither errors nor warnings. It says 
call the setFamily() method which applies to Dogs. I could have omitted the 
"Dog" part, as I did in the next line which reads setFamily("insect"), as 
the compiler will infer that I mean the static method on the class Dog 
(since this method is defined inside of that class). Finally, the last line 
calls a static method in a different class "Cat". Again, I didn't need a 
specific instance of Cat, since setFamily was (presumably) defined to be 
static in that class.

>
> PUBLIC PRIVATE :
…[26 more quoted lines elided]…
> and nobody knows they are occupying real estate, sat there doing nothing.

    We've got 2 programmers, including myself, working in the "compiler 
tools" project that I've posted about earlier in this group. And we are 
going pretty much willy-nilly about it, and we do end up with methods that 
are dropped. However, we have compiler tools available to us that will 
notify us, for example, when a method isn't being used at all, and we 
usually remove them as we discover them.

    The project is actually in a highly mutative or experimental state, 
where we occasionally drop entire modules (that may have taken 3 to 6 weeks 
to write) as we discover better ways of accomplishing the same task. I think 
the type of development we're doing is called "Rapid Prototype", where we 
quickly get something working to test out the feasability of it, and 
experiment a lot, before we commit to a particular methodology.

    We're looking at the benefits of using the AspectJ programming language 
instead of Java, for example. (Luckily, AspectJ is a superset of Java, so we 
won't have to completely scratch all the work we've done so far to make this 
switch).

    Dropping 3 to 6 weeks worth of code is "rapid prototyping" in the sense 
that this is considered to be a very long term project, on the order of tens 
of years, I think. This project is also not the "main source of income" for 
this company. I guess you could say I'm doing R&D on compiler technologies 
for the company.

>
> Same sort of control applies to Pete's component concept. Firstly,
…[4 more quoted lines elided]…
> obsolescence ?

    Perhaps, like for us, it simply isn't a big deal if there's some 
overlapping or obsolete components. Of course, with only 2 developers, it 
isn't so bad for us.

[snip]
> doing the latter :-
>
…[20 more quoted lines elided]…
> initial state.

    This is the part that confused me the most. If I understand correctly, 
you're saying that if you execute a factory method from an instance method, 
a side effect of this execution is that all instance variables are 
re-initialized?

    - Oliver
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-03-16T20:27:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371c0$441a1ea2$45491d7a$19137@KNOLOGY.NET>`
- **In-Reply-To:** `<cSfSf.282$me6.91@clgrps13>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <cSfSf.282$me6.91@clgrps13>`

```
Oliver Wong wrote:
> Discalimer: I wasn't able to follow everything in this post either.

But I sure was able to follow this one.  Wow - I've been through Java 
training, even written some Java, but this made a *lot* of since.  Thanks!
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-18T15:41:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<481aanFhm39pU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <cSfSf.282$me6.91@clgrps13>`

```

"Oliver Wong" <owong@castortech.com> wrote in message 
news:cSfSf.282$me6.91@clgrps13...
> Discalimer: I wasn't able to follow everything in this post either.
>
…[7 more quoted lines elided]…
> no FACTORY keyword, and you did just fine, right?

I disagree. I agree for standard COBOL but not for OO.  I can post OO COBOL 
behaviour that REQUIRES FACTORY  but I simply haven't time at the moment and 
these threads are already too long.

As a clue... suppose you want to limit the number of concurrent object 
instances running at any given moment?

Or... suppose you want to trigger an event notifying a network administrator 
that certain RPCs were made, but selectively, and only for certain 
instances?

I'm sure you catch my drift...

FACTORY is an important and useful part of OO COBOL.

But hey! that's just my opinion... :-)

Pete.
```

#### ↳ Re: Constants, Static, Public, Private

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-03-16T09:41:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvc808$1v0i$1@si05.rsvl.unisys.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
Top post; no more below.

Constants in '02 COBOL are source-level manipulation tools.  The standard
even specifies explicitly that you may include a constant *within* a PICTURE
character-string as a repetition value, and the compiler is obligated to
compile the result appropriately.  For example:
    01  Forever CONSTANT 99999999.
    01  Long-string PICTURE X(forever).
should be legal according to the '02 standard.   A CONSTANT ENTRY is a
different animal from a data item.

It looks to me like '02 COBOL's
    01  Forever CONSTANT 99999999.
is equivalent in function to the MF/FJ
    78  Forever VALUE 99999999.
that you cite.

Although I wasn't there when this was decided, J4 is reluctant to reserve
yet another level number for yet another special purpose unless there was a
particularly good reason to do so.  CONSTANT had a history as a reserved
word in COBOL, and I think the syntax J4 chose stands a better chance of
interfering less with future enhancements to data declaration entry syntax
than the reservation of yet another level number from a limited repertoire
would have.

What my proposal for the '08 draft did was to add the CONSTANT RECORD clause
to the syntax for data-description entries, and the record in which the
clause appears is termed a "structured constant".  In all respects it is a
record in the SECTION in which it appears, with the exception that any
attempt to treat either the data item itself or any item subordinate to it
is a violation of a fundamental *syntax* rule.

The current draft for the next standard (accessible from
www.cobolportal.com/j4/ ; it's the "20xx Base Document ...", sixth item on
the list of J4 Administrative Documents) includes a discussion of
"structured constants" in the Concepts appendix on Page 824 at section D.18.

The CONSTANT SECTION was an ancient feature of COBOL that was *dropped* from
the '74 standard.  I thought about trying to bring it back, but the way it
was specified in the '68 standard left a number of loopholes that made
records therein no different from any other record in terms of
"inviolability", and I also felt restricting the user (and the implementor)
to putting "structured constants" in  a *single* section was too
restrictive.

    -Chuck Stevens

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:_M_Rf.147168$B94.59312@pd7tw3no...
> I'm still on the tack "Is FACTORY really necessary ?".
>
…[320 more quoted lines elided]…
>
```

#### ↳ Re: Constants, Static, Public, Private

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2006-03-20T21:01:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y_JTf.6517$366.2915@fe06.lga>`
- **In-Reply-To:** `<_M_Rf.147168$B94.59312@pd7tw3no>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no>`

```
James J. Gavan wrote:
> I'm still on the tack "Is FACTORY really necessary ?".
> 
…[318 more quoted lines elided]…
> 
In the Cobol Standard all variables are global.  If you dont like it, 
get over it.  This means you have to have good naming conventions.  If 
you have 100 files all the variable in every file should be unique! 
Generally, I handle this at my shop by a convention where every file has 
a 4 characher/number file name.  ST11, PE11, CR11, ETC.  Student file, 
Personnel File, Course File, etc.  So no matter what program you are in, 
you can tell what file it is.  Global naming requires more skill and 
more planning.

COBOL is not C++ or Java.  Some versions of COBOL may have object 
oriented variables, but that is not the COBOL Standard.  If you want to 
program in COBOL dont use some other languages usage be your excuse to 
fail.  Get a grip and learn the language you are programming in.

It will probably be at least 10 years before the next standard for COBOL 
come out.
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-21T03:26:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UnKTf.77002$fe6.12685@fe01.news.easynews.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga>`

```
"Last Boy Scout" <eggbtr@ezl.com> wrote in message 
news:y_JTf.6517$366.2915@fe06.lga...
> James J. Gavan wrote:
>> I'm still on the tack "Is FACTORY really necessary ?".
>>
<much snippage>
> In the Cobol Standard all variables are global.  If you dont like it, get over 
> it.  This means you have to have good naming conventions.  If you have 100 
…[5 more quoted lines elided]…
>

HUH???  (he asked rhetorically)

In COBOL, the default is "totally" local variable names.

The GLOBAL attribute (if explicitly coded) makes a variable "visible" to nested 
programs.

The EXTERNAL attribute (if explicitly coded) makes identically named variables 
in separately compiled programs refer to the same item.

It is true that COBOL doesn't have "local" variables at the "procedure" 
(paragraph or section) level, but it most certainly DOES at the nested program 
level.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-22T00:15:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48a931FiqqjfU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga> <UnKTf.77002$fe6.12685@fe01.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:UnKTf.77002$fe6.12685@fe01.news.easynews.com...
> "Last Boy Scout" <eggbtr@ezl.com> wrote in message 
> news:y_JTf.6517$366.2915@fe06.lga...
…[27 more quoted lines elided]…
>
You are exactly right, Bill.

However the point about nested programs seems to have been entirely missed 
by both Frank and Jimmy and now Last Boy Scout.

Maybe because they are unfamiliar with their use. It is a while since I used 
them, but, from memory, my understanding is ...

Briefly...
1. Nested programs DO allow nested functionality.
2. Nested programs are PRIVATE.
3. Nested program variables are LOCAL, except as you described above (use of 
GLOBAL and EXTERNAL)
4. A FACTORY can act as a COMMON area for nested programs, but the rules 
still apply. Access TO the FACTORY must be through Factory methods, and 
access FROM the factory must be via instance methods. FACTORY variables 
should be accessed by GET and SET methods if late binding is used,(but don't 
HAVE to be if they are declared GLOBAL EXTERNAL). Also, they need not be, if 
prototyping or early binding is used. This is where the REPOSITORY comes 
into its own.

There are a numberof variables in play here and it is NOT just a simple 
"yes" or "no".

Until someone actually writes some applications that use nested COBOL, they 
are unlikely to feel comfortable with it. However, like most things, if you 
make the investment, there are paybacks.

Pete.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-21T13:04:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48b4hqFj5q4uU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga> <UnKTf.77002$fe6.12685@fe01.news.easynews.com> <48a931FiqqjfU1@individual.net>`

```
 Pete Dashwood<dashwood@enternet.co.nz> 03/21/06 5:15 AM >>>
>You are exactly right, Bill.
>
>However the point about nested programs seems to have been entirely missed

>by both Frank and Jimmy and now Last Boy Scout.
>
>Maybe because they are unfamiliar with their use. It is a while since I
used 
>them, but, from memory, my understanding is ...
>
…[3 more quoted lines elided]…
>3. Nested program variables are LOCAL, except as you described above (use
of 
>GLOBAL and EXTERNAL)
>4. A FACTORY can act as a COMMON area for nested programs, but the rules 
>still apply. Access TO the FACTORY must be through Factory methods, and 
>access FROM the factory must be via instance methods. FACTORY variables 
>should be accessed by GET and SET methods if late binding is used,(but
don't 
>HAVE to be if they are declared GLOBAL EXTERNAL). Also, they need not be,
if 
>prototyping or early binding is used. This is where the REPOSITORY comes 
>into its own.
…[4 more quoted lines elided]…
>Until someone actually writes some applications that use nested COBOL, they

>are unlikely to feel comfortable with it. However, like most things, if you

>make the investment, there are paybacks.

Hmm, I'm not sure why you put me in that esteemed group, there.  I
understand nested programs and their usefulness.  I've actually been doing
some stuff with it recently.  My goal, at this point, is simply to allow the
called program to "own" the "ICMMSTR" records and have them be able to be
expanded without the calling programs needing to be recompiled.  I can't say
tha I've utilized a lot (or any!) of "local" working-storage, but I
certainly could if it is warranted.
Also, there's only one real example of a "getter" type function
('GET-USERNAME'), but there certainly would be more, as well as "setters".

Take a look.


 IDENTIFICATION DIVISION.                                         
 REPLACE                                                          
    ==:PROG-ID:== BY =='ICMINFO'==                               
 .                                                                
 PROGRAM-ID. :PROG-ID:.                                            
 ENVIRONMENT DIVISION.                                            
 INPUT-OUTPUT SECTION.                                            
 FILE-CONTROL.                                                    
     SELECT ICMMSTR-FILE                                          
         ASSIGN TO ICMMSTR                                        
         ORGANIZATION IS INDEXED                                  
         ACCESS IS RANDOM                                         
         RECORD KEY IS ICMMSTR-KEY                                
         FILE STATUS IS ICMMSTR-STATUS.                           
                                                                 
 DATA DIVISION.                                                   
 FILE SECTION.                                                    
 FD  ICMMSTR-FILE                GLOBAL.                          
     COPY ICMMSTRF.                                               
                                                                 
 WORKING-STORAGE SECTION.                                         
******************************************************************
*    GLOBAL EXTERNAL DATA GOES HERE.                             *
*    THIS AREA IS SHARED BETWEEN ALL PROGRAMS IN THE ENTIRE      *
*    RUN-UNIT (INCLUDING THE CALLING PROGRAM).                   *
******************************************************************
 01  EXT-ERROR-MESSAGE           PIC X(80) GLOBAL EXTERNAL.       
******************************************************************
*    GLOBAL WORKING-STORAGE GOES HERE.                           *
*    THIS AREA IS SHARED BETWEEN ALL NESTED PROGRAMS BELOW.      *
******************************************************************
 01  GLOBAL-WS                   GLOBAL.                          
     05  ICMMSTR-STATUS          PIC XX        VALUE SPACES.      
         88  ICMMSTR-SUCCESSFUL                VALUE '00'.        
         88  ICMMSTR-NOT-FOUND                 VALUE '23'.        
     05  ICMMSTR-FILE-OPEN-SW         PIC X    VALUE 'N'.         
         88  ICMMSTR-FILE-OPEN                 VALUE 'Y'.         
     05  SUBROUTINE              PIC X(31).                       
                                                                  
 COPY GLOBALLE.                                                   
/                                                                 
 LINKAGE SECTION.                                                 
 01  FUNC                        PIC X(31).                       
 01  PARM1                       PIC X.    
 01  PARM2                       PIC X.    
                                          
 01  ICMMSTR-HDR-REC             GLOBAL.   
*  more record data here
 01  ICMMSTR-GRP-REC             GLOBAL.
*  more record data here
 01  ICMMSTR-USR-REC             GLOBAL.
*  more record data here
 01  ICMMSTR-CMP-REC             GLOBAL.
*  more record data here
 01  ICMMSTR-ACC-REC             GLOBAL.
*  more record data here
 PROCEDURE DIVISION USING FUNC           
                          PARM1          
                          PARM2.         
                                         
     MOVE ZEROES TO RETURN-CODE          
     MOVE SPACES TO EXT-ERROR-MESSAGE    
     MOVE FUNC TO SUBROUTINE             
     CALL SUBROUTINE USING PARM1         
                           PARM2         
     EXIT PROGRAM.                       
                                         
 IDENTIFICATION DIVISION.                
 PROGRAM-ID. 'ALLOC'.                    
 DATA DIVISION.                          
 LINKAGE SECTION.                        
 01  ALLOC-ADDR                  POINTER.

 PROCEDURE DIVISION USING FUNC           
                          PARM1          
                          PARM2.         
                                         
     MOVE ZEROES TO RETURN-CODE          
     MOVE SPACES TO EXT-ERROR-MESSAGE    
     MOVE FUNC TO SUBROUTINE             
     CALL SUBROUTINE USING PARM1         
                           PARM2         
     EXIT PROGRAM.                       
                                         
 IDENTIFICATION DIVISION.                
 PROGRAM-ID. 'ALLOC'.                    
 DATA DIVISION.                          
 LINKAGE SECTION.                        
 01  ALLOC-ADDR                  POINTER.
 01  ALLOC-RECNAME               PIC X(8).               
                                                         
 PROCEDURE DIVISION USING ALLOC-ADDR                     
                          ALLOC-RECNAME.                 
     MOVE ZEROES TO RETURN-CODE                          
     SET ALLOC-ADDR TO NULL                              
     EVALUATE ALLOC-RECNAME                              
     WHEN 'HEADER'                                       
         MOVE LENGTH OF ICMMSTR-REC-HDR TO STGSIZE       
     WHEN 'GROUP'                                        
         MOVE LENGTH OF ICMMSTR-REC-GRP TO STGSIZE       
     WHEN 'USER'                                         
         MOVE LENGTH OF ICMMSTR-REC-USR TO STGSIZE       
     WHEN 'COMPANY'                                      
         MOVE LENGTH OF ICMMSTR-REC-CMP TO STGSIZE       
     WHEN 'ACCOUNT'                                      
         MOVE LENGTH OF ICMMSTR-REC-ACC TO STGSIZE       
     WHEN OTHER                                          
         STRING :PROG-ID: '-T--UNKNOWN ICM RECORD TYPE: '
                 ALLOC-RECNAME                           
           DELIMITED BY SIZE                             
           INTO EXT-ERROR-MESSAGE                        
         END-STRING                               
         MOVE 12 TO RETURN-CODE                   
         EXIT PROGRAM                             
     END-EVALUATE                                 
                                                  
     PERFORM GET-STORAGE                          
     SET ALLOC-ADDR TO ADDRSS                     
     IF NOT ICMMSTR-FILE-OPEN                     
         CALL 'OPEN-ICMMSTR'                      
     END-IF                                       
     EXIT PROGRAM.                                
                                                  
 GET-STORAGE.                                     
     MOVE ZERO                   TO HEAPID        
     MOVE LE-GET-STORAGE         TO SUBROUTINE    
     CALL SUBROUTINE USING HEAPID STGSIZE ADDRSS  
                           FC                     
     CALL 'CHECK-CEE-FC'                          
     IF RETURN-CODE > ZERO                        
         EXIT PROGRAM                             
     END-IF                                       
     EXIT.                                        
                                                     
 END PROGRAM 'ALLOC'.                                
/                                                    
 IDENTIFICATION DIVISION.                            
 PROGRAM-ID. 'LOOKUP'.                               
 DATA DIVISION.                                      
 WORKING-STORAGE SECTION.                            
 01  ABEND   PIC S9(9) COMP-3.                       
 LINKAGE SECTION.                                    
 01  ICM-KEY                     PIC X(17).          
/                                                    
 PROCEDURE DIVISION USING ICM-KEY.                   
     CALL 'READ-ICMMSTR' USING ICM-KEY               
     IF RETURN-CODE > ZERO                           
         STRING :PROG-ID: '-T--ERROR READING RECORD '
                ICM-KEY                              
           DELIMITED BY SIZE                         
           INTO EXT-ERROR-MESSAGE                    
         END-STRING                                  
         EXIT PROGRAM.                               
                                                     
     EVALUATE TRUE                                   
     WHEN ICMMSTR-REC-TYPE-HDR                               
         SET ADDRESS OF ICMMSTR-HDR-REC TO ADDRESS OF ICM-KEY
         MOVE ICMMSTR-REC-HDR TO ICMMSTR-HDR-REC             
     WHEN ICMMSTR-REC-TYPE-GRP                               
         SET ADDRESS OF ICMMSTR-GRP-REC TO ADDRESS OF ICM-KEY
         MOVE ICMMSTR-REC-GRP TO ICMMSTR-GRP-REC             
     WHEN ICMMSTR-REC-TYPE-USR                               
         SET ADDRESS OF ICMMSTR-USR-REC TO ADDRESS OF ICM-KEY
         MOVE ICMMSTR-REC-USR TO ICMMSTR-USR-REC             
     WHEN ICMMSTR-REC-TYPE-CMP                               
         SET ADDRESS OF ICMMSTR-CMP-REC TO ADDRESS OF ICM-KEY
         MOVE ICMMSTR-REC-CMP TO ICMMSTR-CMP-REC             
     WHEN ICMMSTR-REC-TYPE-ACC                               
         SET ADDRESS OF ICMMSTR-ACC-REC TO ADDRESS OF ICM-KEY
         MOVE ICMMSTR-REC-ACC TO ICMMSTR-ACC-REC             
     WHEN OTHER                                              
         STRING :PROG-ID: '-T--UNKNOWN RECORD TYPE '         
                ICMMSTR-REC-TYPE                             
           DELIMITED BY SIZE                                 
           INTO EXT-ERROR-MESSAGE                            
         END-STRING                                          
         MOVE 12 TO RETURN-CODE                              
     END-EVALUATE                             
     ADD 1 TO ABEND                           
     EXIT PROGRAM.                            
 END PROGRAM 'LOOKUP'.                        
/                                             
 IDENTIFICATION DIVISION.                     
 PROGRAM-ID. 'GET-USERNAME'.                  
 DATA DIVISION.                               
 LINKAGE SECTION.                             
 01  USER-NAME                   PIC X(40).   
/                                             
 PROCEDURE DIVISION USING ICMMSTR-USR-REC     
                          USER-NAME.          
     MOVE ICMMSTR-USR-NAME TO USER-NAME       
     EXIT PROGRAM.                            
 END PROGRAM 'GET-USERNAME'.                  
/                                             
 IDENTIFICATION DIVISION.                     
 PROGRAM-ID. OPEN-ICMMSTR IS COMMON PROGRAM.  
 DATA DIVISION.                               
 PROCEDURE DIVISION.                                            
     OPEN INPUT ICMMSTR-FILE                                    
     IF ICMMSTR-SUCCESSFUL                                      
         SET ICMMSTR-FILE-OPEN TO TRUE                          
     ELSE                                                       
         STRING :PROG-ID: '-T-- UNSUCCESSFUL OPEN ON ICMMSTR '  
                ICMMSTR-STATUS                                  
           DELIMITED BY SIZE                                    
           INTO EXT-ERROR-MESSAGE                               
         END-STRING                                             
         MOVE 12 TO RETURN-CODE                                 
     END-IF                                                     
     EXIT PROGRAM.                                              
 END PROGRAM 'OPEN-ICMMSTR'.                                    
                                                                
 IDENTIFICATION DIVISION.                                       
 PROGRAM-ID. 'READ-ICMMSTR' IS COMMON PROGRAM.                  
 DATA DIVISION.                                                 
 LINKAGE SECTION.                                               
 01  ICM-KEY                     PIC X(17).                     
 PROCEDURE DIVISION USING ICM-KEY.                              
     MOVE ICM-KEY TO ICMMSTR-KEY                                
     READ ICMMSTR-FILE                                            
     EVALUATE TRUE                                                
     WHEN ICMMSTR-SUCCESSFUL                                      
         CONTINUE                                                 
     WHEN ICMMSTR-NOT-FOUND                                       
         MOVE 4 TO RETURN-CODE                                    
     WHEN OTHER                                                   
         STRING :PROG-ID: '-T-- UNSUCCESSFUL OPEN ON ICMMSTR '    
                ICMMSTR-STATUS                                    
           DELIMITED BY SIZE                                      
           INTO EXT-ERROR-MESSAGE                                 
         END-STRING                                               
         MOVE 12 TO RETURN-CODE                                   
     END-EVALUATE                                                 
     EXIT PROGRAM.                                                
 END PROGRAM 'READ-ICMMSTR'.                                      
                                                                  
 IDENTIFICATION DIVISION.                                         
 PROGRAM-ID. 'CHECK-CEE-FC' IS COMMON PROGRAM.                    
******************************************************************
*    CHECK LANGUAGE ENVIRONMENT (CEE) FEEDBACK CODE (FC)         *
******************************************************************
 DATA DIVISION.                                                   
 WORKING-STORAGE SECTION.                                         
 01  CHECK-CEE-WS.                                                
     05  LE-MSG-NO               PIC 9(4).                        
                                                                  
 PROCEDURE DIVISION.                                              
     IF CEE000 OF FC                                              
         EXIT PROGRAM                                             
     END-IF                                                       
                                                                  
     MOVE MSG-NO OF FC TO LE-MSG-NO                               
     STRING :PROG-ID: '-T--LE ROUTINE '                           
            SUBROUTINE ' FAILED WITH MSG '                        
            LE-MSG-NO                                             
       DELIMITED BY SIZE                                          
       INTO EXT-ERROR-MESSAGE                                     
     END-STRING                                                   
     MOVE 12 TO RETURN-CODE                                       
     EXIT PROGRAM.          
                            
 END PROGRAM 'CHECK-CEE-FC'.
                            
 END PROGRAM :PROG-ID:.     


Then in a calling program I have:
*    ALLOCATE STORAGE FOR ICMMSTR USER RECORD AND OPEN
*    ICMMSTR FILE.                                    
     MOVE 'ICMINFO' TO SUBROUTINE                     
     MOVE 'ALLOC' TO FUNC-NAME                        
     CALL SUBROUTINE USING FUNC-NAME                  
                           ADDRESS OF ICMMSTR-REC     
                           BY CONTENT 'USER    '      
     IF RETURN-CODE > ZERO                            
         GO TO 9900-EXTERNAL-ERROR.                   


     MOVE 'ICMINFO' TO SUBROUTINE                     
     MOVE SPACES TO ICMMSTR-REC                       
     SET ICMMSTR-REC-TYPE-USR TO TRUE                 
     MOVE WIREMNT-ICM-USER-ID    TO ICMMSTR-REC-USR-ID
     MOVE 'LOOKUP' TO FUNC-NAME                       
     CALL SUBROUTINE USING FUNC-NAME                  
                           ICMMSTR-REC                
     EVALUATE RETURN-CODE                             
*      error checking here...
     END-EVALUATE

     MOVE 'GET-USERNAME' TO FUNC-NAME      
     CALL SUBROUTINE USING FUNC-NAME       
                           ICMMSTR-REC     
                           ICMMSTR-USR-NAME
     IF RETURN-CODE > ZERO                 
         GO TO 9900-EXTERNAL-ERROR.        




Anyway, just something I was messing with recently...  At this point it
takes more code than it replaces in a standard COBOL program, but it was
interesting to work with.  Don't know how far I'll take it.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-03-23T01:49:48+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48d306FjiqlmU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga> <UnKTf.77002$fe6.12685@fe01.news.easynews.com> <48a931FiqqjfU1@individual.net> <48b4hqFj5q4uU1@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:48b4hqFj5q4uU1@individual.net...
> Pete Dashwood<dashwood@enternet.co.nz> 03/21/06 5:15 AM >>>
>>You are exactly right, Bill.
…[37 more quoted lines elided]…
> understand nested programs and their usefulness.

My apologies. I thought you were asking questions like ""Are nested methods 
PRIVATE?" "Can functions be nested by nested programming?"   (That's why I 
made a point of giving short answers above.)

From the code below, I see you certainly have had a go at it and there's 
nothing there that would make me swoon in horror... :-)

>I've actually been doing
> some stuff with it recently.  My goal, at this point, is simply to allow 
> the
> called program to "own" the "ICMMSTR" records and have them be able to be
> expanded without the calling programs needing to be recompiled.

That could be achieved by the conventional mechanism of calling a completely 
separate module, as well as nesting programs.


> I can't say
> tha I've utilized a lot (or any!) of "local" working-storage, but I
> certainly could if it is warranted.

You are not running multiple separate instances of code, as you could be in 
an OO environment. In that circumstance you might be glad of local 
storage...

> Also, there's only one real example of a "getter" type function
> ('GET-USERNAME'), but there certainly would be more, as well as "setters".
…[305 more quoted lines elided]…
> interesting to work with.  Don't know how far I'll take it.

There are some good concepts embodied in the above.  The whole nested entity 
is getting like a class, with internal methods and data (Properties).

It seems to me you have 'ALLOC' nested twice and that wouldn't work in my 
environment (Fujitsu), and I'd be worried about Linkage data that doesn't 
match the procedure division header, but there may be some variation in 
platforms here. I see no REPOSITORY so I can't tell whether conformance 
checking is employed in your environment, but it looks as if it isn't. On 
the other hand I can't tell whether this is early or late bound either. All 
of this would have a bearing if it was OO code.

If you chose to move on to OO, I think the above exercise could be 
considered good experience.

I'd still learn Java though (if you haven't already).

Pete.
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-03-22T10:27:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48dfo7FijvcdU1@individual.net>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga> <UnKTf.77002$fe6.12685@fe01.news.easynews.com> <48a931FiqqjfU1@individual.net> <48b4hqFj5q4uU1@individual.net> <48d306FjiqlmU1@individual.net>`

```
Pete Dashwood<dashwood@enternet.co.nz> 03/22/06 6:49 AM >>>
>

>From the code below, I see you certainly have had a go at it and there's 
>nothing there that would make me swoon in horror... :-)
>
>>I've actually been doing
>> some stuff with it recently.  My goal, at this point, is simply to allow

>> the
>> called program to "own" the "ICMMSTR" records and have them be able to
be
>> expanded without the calling programs needing to be recompiled.
>
>That could be achieved by the conventional mechanism of calling a
completely 
>separate module, as well as nesting programs.

This is, in fact, what I am doing.  ICMINFO is a program that is called by
other programs that wish to access the ICMMSTR record.  'ALLOC' and the like
are programs nested within ICMINFO, and they can only be called (directly)
by ICMINFO itself.  In order for another program to call ALLOC it really
calls ICMINFO passing the value 'ALLOC' as a parameter:  CALL ICMINFO USING
ALLOC, ADDRESS OF ICMMSTR.  All that the "main" program ICMINFO does is
calls the nested program named in the first parameter: CALL FUNC USING PARM1
(here FUNC is really the first parameter passed to ICMINFO and PARM1 is the
second parameter passed to ICMINFO).  I was actually a bit surprised that
that worked.  I was expecting I might have to do something awful like
EVALUATE FUNC
WHEN 'ALLOC' CALL 'ALLOC' USING PARM1, PARM2
WHEN 'LOOKUP' CALL 'LOOKUP' USING PARM1
...
END-EVALUATE

But I'm glad it works as it does!

>There are some good concepts embodied in the above.  The whole nested
entity 
>is getting like a class, with internal methods and data (Properties).
>
…[5 more quoted lines elided]…
>the other hand I can't tell whether this is early or late bound either. All

>of this would have a bearing if it was OO code.

No, there is no REPOSITORY.  My compiler does not support it, nor any OO
and/or COBOL 2002 functionality.  Which is why I'm trying to "simulate" it a
bit using COBOL 85...

>If you chose to move on to OO, I think the above exercise could be 
>considered good experience.
>
>I'd still learn Java though (if you haven't already).

I have.  By no means an expert, but I can get around...

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Constants, Static, Public, Private

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-21T13:44:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p5p022tkhs1853g81sdvbpidc5gmlkf62d@4ax.com>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga> <UnKTf.77002$fe6.12685@fe01.news.easynews.com> <48a931FiqqjfU1@individual.net>`

```
On Wed, 22 Mar 2006 00:15:23 +1200, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>Briefly...
>1. Nested programs DO allow nested functionality.
…[4 more quoted lines elided]…
>still apply.

I played with nested programs one time, but in the environments I have
worked in, I haven't seen a particular advantage in using them.   Back
when in the days of humongous, non-structured programs, local
variables wouldn't have been *that* useful.   I really don't worry
about the size of working storage.

In Java, local variables are just another thing for the environment to
clean-up, but they allow me to reuse variable names without worry.
That's not a problem with Working-Storage.
```

##### ↳ ↳ Re: Constants, Static, Public, Private

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-21T14:20:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142979625.368704.27080@t31g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<y_JTf.6517$366.2915@fe06.lga>`
- **References:** `<_M_Rf.147168$B94.59312@pd7tw3no> <y_JTf.6517$366.2915@fe06.lga>`

```
> In the Cobol Standard all variables are global.

No. Typically my old Cobol applications are in several dozen programs.
Each W-S has the _local_ data for that program and the programs can
call each other in arbitrary (non-recursive) ways.  In some I do
actually have 'global' data by using the EXTERNAL qualifier. In most I
pass a parameter in each call that is a reference back to a record in
the root program's data area where the application's 'global' data is
stored.

Nested programs in particular have to specify which data items are
accessible by contained programs using the GLOBAL qualifier.

> If you dont like it, get over it.

You give the impression that you write complete Cobol applications in
one humungus several thousand line source files and never learnt the
benefits of modularity.

>  This means you have to have good naming conventions.  If
> you have 100 files all the variable in every file should be unique!

This is not true even if you do write programs in archaic styles.
Qualification of variables has been around for a few decades now, some
even use MOVE CORRESPONDING as a benefit of having common naming
(though I rarely do so myself).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
