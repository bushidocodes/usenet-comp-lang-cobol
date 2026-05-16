[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need a practical example for OOP Cobol ?

_11 messages · 4 participants · 2011-06_

---

### Need a practical example for OOP Cobol ?

- **From:** Dicky Chan <seekingvengeance4solace@gmail.com>
- **Date:** 2011-06-13T10:29:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`

```
I'm a beginner, actually this semester I have to research about Cobol
language. On the internet, there are few example, even no example
about OOP cobol. There are only st like example for theory, they
doesn't show me how to add st more ( like a main in Java ) to see the
program work. I have some codes like this:

 class-id. A data is protected
               inherits from Base.

     object section.



     method-id. "newWithData"
     linkage section.
         01 lnkObject      object reference.
         01 lnkName        pic x(80).

     procedure division using lnkName
                    returning lnkObject.

  *----Create a new instance of A using the "new" method from Base
         invoke super "new" returning lnkObject
  *----Send it an initialize message.
         invoke lnkObject "initialize" using lnkName
         exit method.
     end method "newWithData".
     object.
     object-storage section.
         01  theName     pic x(80).

        ...

     method-id. "initialize"

     linkage section.
        01  lnkName     pic x(80).
     procedure division using lnkName.
  *----Store the initialization parameter in the object's
  *    instance data
         move lnkName to theName
         exit method.
     end method "initialize".

     end object.
     end class "A".


but I don't know how to run (both theory and practice). Can any one
show me how? It will be best helping me with another example and
explanation.
```

#### ↳ Re: Need a practical example for OOP Cobol ?

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2011-06-13T14:51:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WKuJp.41958$Vp.2348@newsfe14.iad>`
- **In-Reply-To:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`

```
Dicky Chan wrote:
> I'm a beginner, actually this semester I have to research about Cobol
> language. On the internet, there are few example, even no example
…[48 more quoted lines elided]…
> explanation.

Firstly, "I'm a beginner............". What other languages has your 
course covered so far, Java, Visual Basic etc., with an emphasis on OO ?

In the current semester is the use of COBOL a 'broad brush' approach to 
OO COBOL, or should you also be looking at PROCEDURAL COBOL ?

At the current time there are three COBOL approaches to OO - (1) IBM and 
they use mainframe OO COBOL, to create COBOL specific classes as well as 
using Java for most activity, (2) Fujitsu COBOL using dotNet/MS Visual 
Studio and (3) Micro Focus - same route as Fujitsu, but a salesman told 
be about six months back that Net Express V 5.1 will be supported for 
some ten years. Where he got that gem of information from I'd like to 
know, seeing as his new or acquired company was only recently involved 
with Net Express.

Which version of Net Express are you looking at - your sample above is 
available in N/E Version 3.1 onwards up to 5.1. Rather than pursue OO in 
COBOL both Fujitsu and Micro Focus have put the emphasis of letting MS 
Visual Studio do the donkey work using either VB or C#. VS, VB and C# 
are free from Microsoft - F/J and M/F compilers are not - $3,000 upwards 
plus annual maintenance costs.

Firstly I'll mention that there is an on-line set of manuals for Net 
Express 5.1 which covers both Procedural and OO. Your problem with COBOL 
is twofold, in that you have to understand some of the syntax using 
RESERVED WORDS like ADD, SUBTRACT, MOVE etc. This is covered in Language 
Reference Manuals; then as the second leg a separate manual devoted to OO.

Suggestion, subject to how far you want to go with this. You can get a 
second-hand copy of the book "Object Oriented COBOL" by Edmund Arranga 
and Frank Coyle, from Amazon.com for about $18. This was written with an 
early version of Net Express but is compatible with N/E 5.1. At the back 
of the book is a worked example of an in-house library system used in a 
company - doesn't cover GUIs or databases - using Screen displays for 
the former and a table of records in a class holding a Working-Storage 
Table representing info needed for the database.

Nevertheless it does cover the principles of OO COBOL: initializing 
classes and 'calling' or invoking 'methods' from other classes.
If you laboriously typed all the code into your version of Net Express 
it would give you a small working system. However there is a LOT of CODE 
to type. I never had any luck getting the diskette that contained the 
programs in the book.

I'm not going to comment on the pros or cons of using OO COBOL as 
opposed to going completely MS Visual Studio, because obviously your 
instructor has COBOL listed in his curriculum.

If you want more info -  just ask. *VERY* diplomatically you could ask 
the instructor for his comments on what I've written above.

Just as a closer - set up a project for your sample above, compile and 
run it from the Animator, stepping through the code to query values. But 
apart from that one attempt in isolation is doesn't indicate how OO 
coalesces.


Jimmy, Calgary AB
```

##### ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-06-16T15:11:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itdo3s22lcd@news2.newsguy.com>`
- **In-Reply-To:** `<WKuJp.41958$Vp.2348@newsfe14.iad>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <WKuJp.41958$Vp.2348@newsfe14.iad>`

```
James Gavan wrote:
> 
> At the current time there are three COBOL approaches to OO - (1) IBM and
…[6 more quoted lines elided]…
> with Net Express.

Micro Focus COBOL currently supports three or four OO flavors,
depending on how strict you want to be:

- The original MF OO COBOL syntax, as updated in subsequent releases
- ISO 2002 OO COBOL syntax
- Managed OO COBOL, for CLR (.NET) and JVM (Java Virtual Machine)

The first two are native-mode COBOLs; they produce either native
executable code, or MF interpreted code which runs under the native
COBOL runtime.

The third is either one dialect or two, depending on your
interpretation. The CLR and JVM have different OO frameworks, and
there are some syntax differences because of the different facilities
offered by the two runtime environments.

I expect all of these variants to be available for a good long time.
There's a huge installed base of MF COBOL running in native mode, and
while native-mode OO COBOL is a small fraction of that, there's no
advantage to getting rid of it. (The potential for savings, eg in
support, is small, so there's no reason to alienate the customers
using it.)

It's not clear to me what dialect the OP is supposed to be using.

> Which version of Net Express are you looking at - your sample above is
> available in N/E Version 3.1 onwards up to 5.1. Rather than pursue OO in
> COBOL both Fujitsu and Micro Focus have put the emphasis of letting MS
> Visual Studio do the donkey work using either VB or C#.

That's an odd way of putting it at best. Certainly the managed-code OO
frameworks (.NET for CLR and Java standard libraries for JVM) provide
most of the OO environment for those dialects. But it's not VB and C#
doing the "OO work" in .NET - COBOL is fully OO there, and the
framework (containers, support classes, etc) is provided by .NET in
language-agnostic fashion.

And Visual Studio itself has little to do with it, aside from being
the standard IDE for .NET work. If you're targeting JVM, you're more
likely to be using Eclipse; and it's quite possible to avoid the IDE
entirely if that's your preference.

> VS, VB and C#
> are free from Microsoft - F/J and M/F compilers are not - $3,000 upwards
> plus annual maintenance costs.

Yes, Microsoft can afford to subsidize the base levels of their
development tools from their other revenue streams. I'm not sure what
this has to do with the OP's question.

> I'm not going to comment on the pros or cons of using OO COBOL as
> opposed to going completely MS Visual Studio, because obviously your
> instructor has COBOL listed in his curriculum.

Again, these are not orthogonal. MF OO COBOL for .NET uses Visual
Studio as its IDE; you can also refrain from using the IDE. And Visual
Studio by itself does nothing useful - to write code, you have to use
some language.
```

#### ↳ Re: Need a practical example for OOP Cobol ?

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2011-06-13T15:18:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k8vJp.8061$xh5.7334@newsfe02.iad>`
- **In-Reply-To:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`

```
Dicky Chan wrote:
> I'm a beginner, actually this semester I have to research about Cobol etc...

A follow-up message to my previous; I left out an important item. If you 
follow the Micro Focus approach using Visual Studio you can download 
Micro Focus VISUAL COBOL beta version 3 or onwards, to be used with 
Microsoft Visual Studio.

The significant difference is that Net Express has both Character 
Array/Collections classes and GUI classes. The GUI classes have been 
removed from VISUAL COBOL and you are dependent upon VB or C# for doing 
your GUI-ing. (There are differences between VB and C# - but as one man 
is now in charge of both of these languages at Microsoft, any feature 
not currently included in one, will over time, be included in both 
languages). It's interesting that Microsoft admit that for newcomers to 
OO, VB is easier to understand - however the majority of good examples 
are in the C# stable.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** Dicky Chan <seekingvengeance4solace@gmail.com>
- **Date:** 2011-06-14T06:58:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<69cf8419-5422-43df-801a-c8888bf7e422@r33g2000prh.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad>`

```
On Jun 14, 4:18 am, James Gavan <jga...@shaw.ca> wrote:
> Dicky Chan wrote:
> > I'm a beginner, actually this semester I have to research about Cobol etc...
…[16 more quoted lines elided]…
> Jimmy, Calgary AB

-I've learnt Java and C++ before (both with OOP).
-This semester I have to research about Cobol characteristic and
paradigms(procedural and OOP). The final project requires me to self-
create a big example to illustrate nearly everything in the paradigm.
That's why I need to understand OOP Cobol to code.

-I've googled some info about Micro Focus:
http://msdn.microsoft.com/en-us/vstudio/dd643383
"Powerful integration with Microsoft Visual Studio and the .NET
Framework plus direct COBOL Web services capabilities, J2EE
connectivity and XML support allow easy integration of existing and
new COBOL applications with leading enterprise technologies"
It seems that MF supports J2EE
-I searched on Google book but it doesn't display page 352-509 of the
book, while the library application you mentioned is on page 373. Poor
me.

I will ask my instructor. Thanks a lot for your detailed explanation !
```

###### ↳ ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** B-Riemke <bernd.riemke@googlemail.com>
- **Date:** 2011-06-15T01:59:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ce560af-4b8c-4ff6-a218-348281bce0b5@m10g2000yqd.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad> <69cf8419-5422-43df-801a-c8888bf7e422@r33g2000prh.googlegroups.com>`

```
On Jun 14, 3:58 pm, Dicky Chan <seekingvengeance4sol...@gmail.com>
wrote:
> On Jun 14, 4:18 am, James Gavan <jga...@shaw.ca> wrote:
>
…[42 more quoted lines elided]…
> - Show quoted text -

Yes that is right...
--> Micro Focus Net Express with Net and Visual Studio is working
together.
--> Yes there are no good Books on the market about that
But...
--> You must see that you must pay the Runtime on the Micro Focus side
    There is a cheaper way and a way where you can use old cobol files
and
    an old Version from Net Express and this Runtime free...
--> I write dokumentation and samples about that : - )
And...
--> You can work with Java ant Cobol together too...

Best Regards

Bernd
```

###### ↳ ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-06-16T16:11:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itdo4142lcd@news2.newsguy.com>`
- **In-Reply-To:** `<69cf8419-5422-43df-801a-c8888bf7e422@r33g2000prh.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad> <69cf8419-5422-43df-801a-c8888bf7e422@r33g2000prh.googlegroups.com>`

```
Dicky Chan wrote:
> 
> -I've googled some info about Micro Focus:
…[5 more quoted lines elided]…
> It seems that MF supports J2EE

What that sentence says is "J2EE connectivity". Various Micro Focus
COBOL products have various features for integrating with J2EE and
EJBs. Saying we "support J2EE" isn't saying anything; it's so vague as
to be meaningless.

And that technology is not specific to OO COBOL. In fact, it's mostly
used with procedural COBOL. So I'd suggest you study COBOL first, and
accessories like J2EE connectivity later.
```

##### ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-06-16T16:06:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itdo3u32lcd@news2.newsguy.com>`
- **In-Reply-To:** `<k8vJp.8061$xh5.7334@newsfe02.iad>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad>`

```
James Gavan wrote:
> 
> The significant difference is that Net Express has both Character
> Array/Collections classes and GUI classes. The GUI classes have been
> removed from VISUAL COBOL and you are dependent upon VB or C# for doing
> your GUI-ing.

Jimmy, I'm afraid that's not correct. With MF Visual COBOL in .NET you
have a number of GUI options, such as WinForms. There's no need to go
to VB or C# (or any of the several other .NET languages) for that.
```

###### ↳ ↳ ↳ Re: Need a practical example for OOP Cobol ?

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2011-06-16T21:55:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<weAKp.15302$8G4.3985@newsfe17.iad>`
- **In-Reply-To:** `<itdo3u32lcd@news2.newsguy.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad> <itdo3u32lcd@news2.newsguy.com>`

```
Michael Wojcik wrote:
> James Gavan wrote:
> 
…[9 more quoted lines elided]…
> 
Agree with what you say and I have no in depth knowledge of what 
'add-ons' there are which can be used with Visual COBOL. And I didn't 
want to confuse Dicky Chang with a big menu of options.

However, since the days of VISOC there has been a gradual progression 
(via Net Express), all versions of which were backwards compatible.

You only have to review the old Forum (Answer Exchange) to see that the 
majority of users went with Dialog System when it was introduced in N/E 
V 1. In fact I know of old DOS version users who gave VISOC and N/E a 
miss until the Dialog System they had been used to in DOS was 
re-introduced to the N/E product.

Not being aware of Dialog System when I tackled VISOC I went the Dialog 
Editor route with GUI classes, (M/F version of DLGEDIT as opposed to the 
original M/S DLGEDIT, introduced for 'C', I believe). Well there were 
ONLY two choices - Dialog Editor or Screen Section.

I donated lots of blood, sweat and tears. Whether medium sized software 
houses went this route I have no idea, but no more than about a half 
dozen people ever commented on Dialog Editor/Class problems. I can't 
recall the company name, but some developers in Eastern Canada did, as 
well as university instructor Young Kim in Ohio. In Young's case he 
religiously followed the M/F sample code for creating GUIs. It was 
bloody awful, and after the event, he commented how time consuming the 
approach was.

I wrote 'bloody awful'. Nothing wrong with the sample, it did exactly 
what was required for a single dialog, but M/F didn't go the next step - 
how could you speed up the process by creating the majority of GUIs via 
a generic class CreateDialogs, (Re-usability). From day one I latched on 
to the fact that Re-usability was a must. It didn't happen over night. 
Regardless of which GUI tool you use, (and the same applied to using 
paper pads with two-dimensional tables to layout out screens with Screen 
Section), you have to see the screen visually - in my case the Dialog 
Editor (giving the RC file).

Each dialog I create has a table of parameters, (entry-fields, MLEs, 
lists/combo boxes etc, radio and push buttons etc.), which are passed to 
an Instance of MyDialog. Within the latter the appropriate method 
creates the necessary control and sets events which via call-back, are 
returned to the Driver, either - now instantly, or later.

What initially pushed me this route was the old RM/COBOL system had a 
two dimensional table 10 columns (Dates), 25 rows - average rows about 
15, with decimal inch values. The newly designed dialog had 320 controls 
- too big for use with Dialog Editor. I had to go dynamically having 
first figured out my x,y,w,h co-ordinates for each control. Plus when 
entering initial historical data into the old RM system, the sequence 
was going column by column (Date), down as many rows (values) as were 
applicable per column, then move to the next column. The Dialog Editor 
sequence Tab key was ignored and the screen responds to the downwards 
sequence I've indicated. Once data is entered then the user can randomly 
select controls, or the particular cell in the table, with the mouse. 
(Just to clarify, the extra controls for text, Pushbuttons  etc., are 
'drawn' in the Dialog Editor - it is primarily the two-dimensional table 
that is dynamically created).

Non-dynamic dialogs pop up almost instantly. This particular dialog 
there is a discernible pause - but assuming non-dynamic dialogs take say 
5 seconds to display, this dynamic table shows in 10-15 seconds on the 
very first display; subsequent displays are fast.

I've been honing away at this approach for as long as Pete and I have 
been using OO. The parameters passed - those are a bit tricky to watch 
for typing errors, and when you go back and change parameter values in 
the parameter table. Using the M/F or M/S approach each control has a 
name, ID_CUSTOMER_NUMBER, ID_CITY, ID-LISTBOX. I chose to identify each 
by type EF_CUSTOMER_NUMBER, EF_CITY, RB_BLACK, RB_BLUE, PB_OK, PB_DELETE 
etc. The prefix tells me which method to access in MyDialog for creating 
the control and the full-name is the method-name the event result is 
returned to in the Driver.

Speed up the above - was an intended new enhancement. Read the RC file 
(containing your dialog image) as a Line Sequential (text) and extract 
info for each control with its known properties. Use the extraction to 
generate the table of parameters, (programmed correctly it should be 
foolproof). Those automated parameters are then passed to MyDialog as 
required.

Lists in conjunction with Listboxes, dropdown combos : When I reviewed 
some Microsoft text I noted that they allowed either Lists 
(Collections/Dictionaries) or Dialog Controls for Combo boxes or 
Selection Lists to have parallel methods. That struck me as being 
unnecessary duplication - others may disagree. My approach has been to 
create all lists in Collections/Dictionaries and pass the object to the 
appropriate dialog control for display. If we are talking a Selection 
List then the user clicks on the appropriate line; I pass the index 
position back to the Collection object which uses the same index 
position to access the appropriate element in the collection and 
retrieves the full or partial information from the database file as 
required. Additions, changes or deletions in the Selection List are 
passed back to the Collection object to take action. Any changes to the 
Collection causes a re-display of the dialog Selection List.

By passing collection parameters to an Instance of DBMain, (the 
positioning of fields in Collection elements), a generic class is used 
to access information for any Collection.

As indicated it could still use some fine tuning, but I'm in the state 
that I can be comfortable with what the above is doing. Then a short 
while back somebody at Newbury referred me to the the new baby Visual 
COBOL to be used with Visual Studio. Imagine my displeasure, (I was 
pissed off actually), to find that backwards compatibility was gone - 
COBOL GUI classes are no longer present.

If it ain't broke why fix it. I can't believe the problem would have 
been insurmountable - why as of version 5.1. couldn't the new Visual 
COBOL have contained those GUI classes. Those using GUI classes may have 
continued with them and perhaps at a later stage, once familiar with 
Visual Studio, have then switched to a non-COBOL GUI approach. If I was 
bright-eyed and bushy tailed instead of being 80 in September, I might 
possibly have said, "Ho-hum I've got to switch to VB or C# or whatever". 
Why accumulate the knowledge for a new GUI-creator when I could be dead 
next week :-). If you wanna know, I feel fine at the moment !

Just in case should you ask, "Did you ever talk to anybody at M/F about 
this ?". Yep, I spoke to two good programmers at Newbury in 2000 - 
weren't interested, or we had insufficient time, (only some 15 minutes), 
for me to put across what I was asking for - the automation above.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Need a practical example for OOP Cobol ?

_(reply depth: 4)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2011-06-17T13:09:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itg213217j5@news1.newsguy.com>`
- **In-Reply-To:** `<weAKp.15302$8G4.3985@newsfe17.iad>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com> <k8vJp.8061$xh5.7334@newsfe02.iad> <itdo3u32lcd@news2.newsguy.com> <weAKp.15302$8G4.3985@newsfe17.iad>`

```
James Gavan wrote:
> 
> I donated lots of blood, sweat and tears. Whether medium sized software
…[3 more quoted lines elided]…
> well as university instructor Young Kim in Ohio.

Hmm. I wonder if that's the same Young Kim I knew (vaguely) when I was
a graduate student in Ohio. Not that it's relevant to the matter at hand.

> I wrote 'bloody awful'. Nothing wrong with the sample, it did exactly
> what was required for a single dialog, but M/F didn't go the next step -
> how could you speed up the process by creating the majority of GUIs via
> a generic class CreateDialogs, (Re-usability).

I've never used the MF GUI classes, but a quick glance at the current
version of the GUI Programming Tutorial suggests that there's
significant discussion of reuse and abstraction there, so this may
have been improved since you looked at it.

> Speed up the above - was an intended new enhancement. Read the RC file
> (containing your dialog image) as a Line Sequential (text) and extract
…[3 more quoted lines elided]…
> required.

Similar mechanisms are already available in the .NET environment. Most
of our GUI controls are populated by decorating object members with
attributes in the source. If you add a member, you tack an attribute
on its definition - then it shows up as a new field in the control
when the GUI is drawn. This all happens through reflection. There's no
more mucking about with resource files.

So when we produce a COBOL for .NET, it makes sense to use the .NET
GUI framework and tooling.

> As indicated it could still use some fine tuning, but I'm in the state
> that I can be comfortable with what the above is doing. Then a short
…[3 more quoted lines elided]…
> COBOL GUI classes are no longer present.

They've never been present in Visual COBOL. Visual COBOL is not the
successor to Net Express / Server Express. It's a new product. It
doesn't have all the features of NX/SX; it has a bunch of features
that aren't in those products (necessarily, since NX/SX don't produce
managed code).

NetExpress is still around - we just released 6.0 SP2. It still has
the COBOL GUI classes.

> If it ain't broke why fix it.

Visual COBOL is a different product. It doesn't have COBOL GUI classes
for much the same reason a Ford Focus doesn't have a truck bed.
Different tools for different jobs.

I understand if someone tells you that Visual COBOL is the latest and
greatest, you might be under the impression that it replaced Net
Express - indeed, it's entirely possible someone told you it replaces
Net Express. And who knows, someday it may. And someday those GUI
classes may disappear from all current Micro Focus products - though
considering the amount of ancient cruft, I mean "legacy features", we
still carry around, my guess is it'll be a long time yet.

> I can't believe the problem would have
> been insurmountable - why as of version 5.1. couldn't the new Visual
> COBOL have contained those GUI classes.

I'm not sure what you're referring to here as "version 5.1". Visual
COBOL is at version 2010 R3. It's never had a version 5.1. Net Express
is at version 6.0 SP2, and it still has the GUI classes.

> Those using GUI classes may have
> continued with them and perhaps at a later stage, once familiar with
…[4 more quoted lines elided]…
> next week :-). If you wanna know, I feel fine at the moment !

Good to hear!

> Just in case should you ask, "Did you ever talk to anybody at M/F about
> this ?". Yep, I spoke to two good programmers at Newbury in 2000 -
> weren't interested, or we had insufficient time, (only some 15 minutes),
> for me to put across what I was asking for - the automation above.

The main problem was that market demand wasn't there. Few customers
tried to use the GUI stuff.

>From my experience, in fact, more are using the .NET GUI features in
Visual COBOL than are using the GUI classes, and the .NET GUI stuff is
catching up to Dialog System.

Of course, using HTML for the presentation layer is also a popular option.
```

#### ↳ Re: Need a practical example for OOP Cobol ?

- **From:** B-Riemke <bernd.riemke@googlemail.com>
- **Date:** 2011-06-14T01:07:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba07c0aa-3e31-40e4-a50f-4503e8392d97@hg8g2000vbb.googlegroups.com>`
- **References:** `<1aada8d2-a984-4292-9912-b8f2b905d267@s41g2000prb.googlegroups.com>`

```
On Jun 13, 7:29 pm, Dicky Chan <seekingvengeance4sol...@gmail.com>
wrote:
> I'm a beginner, actually this semester I have to research about Cobol
> language. On the internet, there are few example, even no example
…[45 more quoted lines elided]…
> explanation.

You need a Trigger Program like this:

==========================================================================================

 
*******************************************************************
      * Startprogramm einer GUI
Anwendung                               *
 
*                                                                 *
 
*                                                                 *
 
*******************************************************************
       PROGRAM-ID. Trigger.
      *
       OBJECT SECTION.
       CLASS-CONTROL.
           EventManager        is class "p2emgr"
           Klasse1             is class "klasse1"
           KlasseA             is class "KlasseA"
          .
      *
       WORKING-STORAGE SECTION.
      *------------------------
      *
       01 WSEVENTMANAGER           OBJECT REFERENCE.
       01 WSWINDOW                 OBJECT REFERENCE.
       01 WSDESKTOP                OBJECT REFERENCE.
      * Methode1 Felder
       01 Funktionen             pic 9.
       01 Feld1                  pic s9(4).
       01 Feld2                  pic s9(4).
       01 ERGEBNIS               pic s9(5).
       01 M1-RETURN-WERT         pic s9(4) comp-5.
      *
       01 KlasseAPointer         OBJECT REFERENCE.

 
*******************************************************************
       procedure division.
      *-------------------
      *
 
*=================================================================*
      *--  Laden der GUI-Klassen Libary ( fertig von MF )
      *
           CALL "apigui"
 
*=================================================================*
      *--  Initialisieren des EventManager und holen von Obj-
Referenzen
      *
           INVOKE EventManager   "New"        RETURNING wsEventManager
           INVOKE wsEventManager "Initialize"
           INVOKE wsEventManager "GetDesktop" RETURNING wsDesktop
      *
      *    Beispiele für Inhalt der Felder
      *    -  wsEventManager     X"F4 00 00 00"
      *    -  wsDesktop          X"84 00 00 00"
      *
 
*=================================================================*
      *--  Aufrufen der Base
klasse1
      *------------------->  Klassen Methoden OK !
      *                      Methode  "Methode2"
      *
           MOVE   1   TO FELD1, FELD2 FUNKTIONEN
           MOVE   0   TO ERGEBNIS, M1-RETURN-WERT

           INVOKE Klasse1 "Methode2"  USING by reference Funktionen,
                                            by reference Feld1,
                                            by reference Feld2,
                                            by reference Ergebnis,
                                            returning    M1-RETURN-
WERT.
      *
      *--  Aufrufen der Base
klasse1
      *------------------->  Instance Methoden Fehler !
      *                      Methode
"Methode1"
      *                      Exception Fehler 24
      *
           MOVE   2   TO FELD1, FELD2 FUNKTIONEN
           MOVE   0   TO ERGEBNIS, M1-RETURN-WERT

           INVOKE Klasse1 "Methode1"  USING by reference Funktionen,
                                            by reference Feld1,
                                            by reference Feld2,
                                            by reference Ergebnis,
                                            returning    M1-RETURN-
WERT.

      *
      *--  Aufrufen der Base
KlasseA
      *------------------->  Instance Methoden funktioniert so...
      *                      Methode  "New"
      *                     (Generiert Verbindung zu "KlasseA")
      *
      *
           INVOKE KlasseA        "New"      returning KlasseAPointer.
           INVOKE KlasseAPointer "Methode1"
                              USING by reference Funktionen,
                                    by reference Feld1,
                                    by reference Feld2,
                                    by reference Ergebnis,
                                    returning    M1-RETURN-WERT.

      *
 
*=================================================================*
      *--  Generieren eines anzeigbaren Windows sowie die Anzeige
      *    dieses Objektes selber
      *
      *    invoke wsWindow "Start"
      *    invoke wsWindow "show"
      *
 
*=================================================================*
      *--  Starten des Prozesses über den EventManager mit "run".
      *    Hiermit wird die eigentliche Ablaufroutine gestartet !
      *
      *    INVOKE wsEventManager "run"
      *
 
*=================================================================*
      *--   BEENDEN des Ablauf-Routine
      *
           STOP RUN.
      *
 
*******************************************************************
 
*******************************************************************
 
*******************************************************************
 
*******************************************************************
 
*******************************************************************

==========================================================================================
Klasse1:


      *>-----------------------------------------------------------
      *> Class description
      *>-----------------------------------------------------------
       class-id. Klasse1 data is protected
                 inherits from base with data.

       object section.
       class-control.
           Klasse1 is class "klasse1"
      *> OCWIZARD - start list of classes
           base is class "base"
      *> OCWIZARD - end list of classes
      *>---USER-CODE. Add any additional class names below.

           .

      *>-----------------------------------------------------------
       working-storage section. *> Definition of global data
      *>-----------------------------------------------------------

      *>-----------------------------------------------------------
       class-object.   *> Definition of class data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard class methods
      *> OCWIZARD - end standard class methods

 
*>---------------------------------------------------------------
       method-id. "Methode2".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 M2Funktionen             pic 9.
       01 M2Feld1                  pic s9(4).
       01 M2Feld2                  pic s9(4).
       01 M2ERGEBNIS               pic s9(5).
       01 M2-RETURN-WERT           pic s9(4) comp-5.
       procedure division using by reference M2Funktionen,
                                by reference M2Feld1,
                                by reference M2Feld2,
                                by reference M2Ergebnis,
                                returning    M2-RETURN-WERT.

        EVALUATE M2FUNKTIONEN
            WHEN 1
                 COMPUTE M2ERGEBNIS ROUNDED =
                         M2FELD1 + M2FELD2
                 END-COMPUTE
                 MOVE 0    TO M2-RETURN-WERT
            WHEN 2
                 COMPUTE M2ERGEBNIS ROUNDED =
                         M2FELD1 - M2FELD2
                 END-COMPUTE
                 MOVE 0    TO M2-RETURN-WERT
            WHEN 3
                 COMPUTE M2ERGEBNIS ROUNDED =
                         M2FELD1 * M2FELD2
                 END-COMPUTE
                 MOVE 0    TO M2-RETURN-WERT
            WHEN 4
                 COMPUTE M2ERGEBNIS ROUNDED =
                         M2FELD1 / M2FELD2
                 END-COMPUTE
                 MOVE 0    TO M2-RETURN-WERT

            WHEN OTHER
                 MOVE 9999 TO M2-RETURN-WERT

        END-EVALUATE.


       exit method.
       end method "Methode2".
 
*>---------------------------------------------------------------

 
*>---------------------------------------------------------------
       method-id. "Methode3".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 M3Funktionen             pic 9.
       01 M3Feld1                  pic s9(4).
       01 M3Feld2                  pic s9(4).
       01 M3ERGEBNIS               pic s9(5).
       01 M3-RETURN-WERT           pic s9(4) comp-5.

       procedure division using by reference M3Funktionen,
                                by reference M3Feld1,
                                by reference M3Feld2,
                                by reference M3Ergebnis,
                                returning    M3-RETURN-WERT.

           INVOKE  "Methode1" using by reference M3Funktionen,
                                        by reference M3Feld1,
                                        by reference M3Feld2,
                                        by reference M3Ergebnis,
                                        returning    M3-RETURN-WERT.


       exit method.
       end method "Methode3".
 
*>---------------------------------------------------------------


       end class-object.

      *>-----------------------------------------------------------
       object.         *> Definition of instance data and methods
      *>-----------------------------------------------------------
       object-storage section.

      *> OCWIZARD - start standard instance methods
      *> OCWIZARD - end standard instance methods

 
*>---------------------------------------------------------------
       method-id. "Methode1".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 Funktionen             pic 9.
       01 Feld1                  pic s9(4).
       01 Feld2                  pic s9(4).
       01 ERGEBNIS               pic s9(5).
       01 M1-RETURN-WERT         pic s9(4) comp-5.

       procedure division using by reference Funktionen,
                                by reference Feld1,
                                by reference Feld2,
                                by reference Ergebnis,
                                returning    M1-RETURN-WERT.

        EVALUATE FUNKTIONEN
            WHEN 1
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 + FELD2
                 END-COMPUTE
                 MOVE 0    TO M1-RETURN-WERT
            WHEN 2
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 - FELD2
                 END-COMPUTE
                 MOVE 0    TO M1-RETURN-WERT
            WHEN 3
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 * FELD2
                 END-COMPUTE
                 MOVE 0    TO M1-RETURN-WERT
            WHEN 4
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 / FELD2
                 END-COMPUTE
                 MOVE 0    TO M1-RETURN-WERT

            WHEN OTHER
                 MOVE 9999 TO M1-RETURN-WERT

        END-EVALUATE.


       exit method.
       end method "Methode1".
 
*>---------------------------------------------------------------


       end object.

       end class Klasse1.

==========================================================================================
KlasseA:


      *>-----------------------------------------------------------
      *> Class description
      *>-----------------------------------------------------------
       class-id. KlasseA
                 inherits from base.

       object section.
       class-control.
           KlasseA is class "KlasseA"
      *> OCWIZARD - start list of classes
           base    is class "base"
      *> OCWIZARD - end list of classes
      *>---USER-CODE. Add any additional class names below.

           .

      *>-----------------------------------------------------------
       working-storage section. *> Definition of global data
      *>-----------------------------------------------------------

      *>-----------------------------------------------------------
       class-object.   *> Definition of class data and methods
      *>-----------------------------------------------------------
 
*>----------------------------------------------------------------
      *>Create and initialize a new application object.
 
*>----------------------------------------------------------------
       method-id. "New".

       linkage section.
       01 KlasseAPointer           object reference.

       procedure division returning KlasseAPointer.

           invoke super "New" returning KlasseAPointer
           invoke KlasseAPointer "initialize"
           exit method.

       end method "New".

       end class-object.

       object.

       object-storage section.

      *> OCWIZARD - start standard class methods
      *> OCWIZARD - end standard class methods

       method-id. "initialize".
       local-storage section.


       procedure division.
      *----Initialisierungen von Daten.




       exit method.
       end method "initialize".

 
*>---------------------------------------------------------------
       method-id. "Methode1".
       local-storage Section.
      *>---USER-CODE. Add any local storage items needed below.
       linkage Section.
       01 Funktionen             pic 9.
       01 Feld1                  pic s9(4).
       01 Feld2                  pic s9(4).
       01 ERGEBNIS               pic s9(5).
       01 RETURN-WERT         pic s9(4) comp-5.

       procedure division using by reference Funktionen,
                                by reference Feld1,
                                by reference Feld2,
                                by reference Ergebnis,
                                returning    RETURN-WERT.

        EVALUATE FUNKTIONEN
            WHEN 1
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 + FELD2
                 END-COMPUTE
                 MOVE 0    TO RETURN-WERT
            WHEN 2
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 - FELD2
                 END-COMPUTE
                 MOVE 0    TO RETURN-WERT
            WHEN 3
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 * FELD2
                 END-COMPUTE
                 MOVE 0    TO RETURN-WERT
            WHEN 4
                 COMPUTE ERGEBNIS ROUNDED =
                         FELD1 / FELD2
                 END-COMPUTE
                 MOVE 0    TO RETURN-WERT

            WHEN OTHER
                 MOVE 9999 TO RETURN-WERT

        END-EVALUATE.


       exit method.
       end method "Methode1".

       end object.

       end class KlasseA.

==========================================================================================

For more information please contact me via E-Mail...

Best Regards

Bernd

(Bernd.Riemke@Riemke-it.de)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
