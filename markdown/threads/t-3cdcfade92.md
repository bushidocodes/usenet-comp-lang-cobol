[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL to MS Excel

_7 messages · 3 participants · 2009-07_

---

### COBOL to MS Excel

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2009-07-10T17:44:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<znQ5m.28$ho.17@newsfe02.iad>`

```
Our fiend with his percentage format, and problems associated with 
getting an Import to MS Excel.

The simple solution for his *particular* problem - DON'T use COBOL, OO 
COBOL or any other OO languages, including those available via dotNet. 
Merely use COBOL to CALL msexcel.exe !

To be completely blunt - he is a lazy SOB, trying to do a cut and paste 
job where hopefully people supply him with specific code for his problem.

Following his queries here, where I pointed him at references in M/F, he 
subsequently e-mailed me "I'm stuck".

What I find amazing is that he claims he ran his own successful software 
company, (I'm assuming just him), with an application used in N. America 
and other users in some 5 (?) European countries. He's pleasant enough 
in writing and conversation and for my sins he sent me a photograph - 
pleasant looking man with white hair and beard. Now in retirement mode 
at 70 he was looking to earn some pin money. Found two others using N/E 
who because of workload passed this import problem over to him.

Here we go - He has used M/F COBOL for decades and at 70 may possibly 
have more years in COBOL than Pete Dashwood. From conversation he 
PROUDLY tells me, with a laugh, that he is a spaghetti coder. I know the 
term and after all these years I have contact with one ! Even worse he 
likes working with the other two guys because their programming style is 
the same as his. OMG ! When he says spaghetti code I believe him - I've 
seen some of his code associated with this Import problem. He must have 
been self taught because if any tech instructor told him to do it the 
way he does, the latter gentleman should have his genitals removed, even 
if that instructor is already dead. Terms like Three Tier Systems, 
Structured Programming would go completely over his head - so imagine 
how he had a nice fit with something like OO COBOL.

Remember he is the one wanting to use Excel, not me. I don't think he 
even looked at Excel. Had he done so, he would have found the answer to 
his percentage problem. I read it, didn't absorb it, but know it's there 
- I still maintain it is a crappy approach.

Let's put another one to rest on performance and volumes. Looks to me 
Richard that he is very comfortably in the bounds on limitations - but 
I'm not going to give you max rows or columns in case he should read 
this - let the lazy bugger find out for himself.

Writing and talking to him, it wasn't even easy to establish the 
following :-

1. The CSV files are written by the other two - he has no control, or
claims they just give him what they want.

2. What is the application about - Answer : Giving end-users Excel
sheet(s) that they LOVE - but about what, absolutely no specifics.

3. Sample test CSV gives 5,046 rows, 31 columns with a row width up to
3,030 chars. Like Michael W., I just LUV horizontal scrolling. Mind you 
if you put some four screens next to one another and showed a segment of 
the Excel sheet on each, then given a chair on rolling wheels, you could 
whiz from left to right and vice versa to look at the data.

4. The data displayed looked absolutely meaningless to me, and I don't 
think there was any attempt to sort by columns into a sequence. It's a 
guess - take a COBOL record, which wasn't necessarily defined in logical 
groupings and just display it in Excel in the identical sequence.

5. The users 'LOVE' what they get - there are some very naive and dumb 
users in North T**** !

6. When are CSVs produced - as and when, monthly, daily and perhaps
twice or more per day.  Not the 6 he mentioned to us initially, but now
there are 30. Needless to say ambiguous file titles like
Creditors-63523.csv. Manual filing systems were one of my fortes in the
RAF, so I suggested the following directory structure :-

C:\xyz.app
	\Active-Worksheets (created from Master-Worksheet templates
		importing data from Input-Data (CSVs) and bearing date
		of creation - ISO format)
	\Input-Data (created CSVs and bearing date of creation - ISO 					format)
	\Master-Worksheets (containing column headings and established
			column widths - date irrelevant )
	
So the system can have :-

Master-Worksheets	- Creditors.xls (no date)
Input-Data		- Creditors-2009-05-15.csv
Active-Worksheets	- Creditors-2009-06-03.xls (csv input above)

Anybody got a problem with the ISO date-format or perhaps why I'm using
it that way ?

On the above, I said with that structure, to avoid creating a duplicate 
Active WorkSheet for the same day he should use CBL_CHECK_FILE_EXIST, 
and signal a message to the user. Impetuously his response was, "No 
problem, I'll just delete the first one".

7. Obviously wrong now, but I thought I'd have a shot and tickle his 
fancy for OO by providing OO COBOL 101 - the source has more comment 
than code.  Eventually his response was, "No it's not my style, I'll 
stick with spaghetti". He wants to write COBOL in the style when Pontius 
was a Pilate.

8. While this is going on, he's still dabbling with his spaghetti and
asking question of any warm bodies he can find. Not successful 
initially, because it was a bunch of "You could...", or "You can try..." 
based on what he was asking.

9. In addition to the above I loaded Excel to see what it was about. 
Almost without thinking, I imported that CSV file above - BLIP ! Was 
done in perhaps 5 to 7 seconds, if not less. Just manually select 
"Import". However there is a three stage Excel Wizard prompting you on 
the csv file, separator symbols, etc. I ignored that just importing as 
is - got all the columns, but without widths specified, text columns get 
truncated. You have to include the Import Wizard.

10. Told him what I had done in 9. His CSV has the column headings as 
the first row. So he took a crack at it importing. Naturally found 
truncated columns - got around that one by test data with full widths; 
then found, having stored column widths he could delete the headings and 
test rows, and had a template with widths. This is how the man's mind 
works - put in those test rows to 'sort of get the correct width', then 
manually adjust the column widths, based on what he sees on the screen. 
So if 30 characters looks OK, (even though the input field is 40 
characters), adjust the width to 30 !

11. Eventually he strikes gold ! Somebody who has spent some effort in
Excel using their MACRO feature. In response to each of his questions, 
he just keeps getting more and more macro ammunition and coded examples.

Had I been aware of the Macro feature, (and I'm not the one who was
seeking advice on MS Excel), I would have been away to the races. I did 
intend writing a final snotty e-mail to him, but what's the point. At 70 
he is not going to become enlightened. As a point of interest this is 
what I intended for him about macros :-

*******
(Bear in mind I told you that back in the late seventies I was using
Wang word processors and using key combinations  to make and store the
macros. From that I designed for the Purchase Dept., of Dome
Petroleum Ltd., (now defunct), a Purchase Order application where I did
a look-up on Vendor names and addresses and Product Descriptions, ( the
'files' were Wang documents) - long forgotten how, but this application
prompted the stenographers to select names and products, and obviously
they entered quantities. (They were typists, not data entry clerks).
This was far, far more sophisticated than what you are doing - AND - I
started from scratch with nobody to advise me, and reading the
documentation available.)
********

Much too long ago to remember specifics, but there would have been two 
Wang document files - Vendors and Products listed alphabetically. The 
typist's key strokes triggered open the Vendors' file, with the cursor 
go down to the name/address required, highlight and then a macro to 
copy/paste into the Purchase Order; same with Products.

Quite a nifty approach to get purchase orders and the Wang machines had 
good quality typewriters. (You couldn't change fonts without changing 
the printer font ball). The daft part was that the Purchase Manager 
wanted monthly analysis reports. Political situation with a mainframe 
installation. The Purchase Manager wanted to get on to the computer, but 
the DPM consistently refused. The Purchase Manager negotiated with Wang 
for a w/p system to do his purchase orders. In conversation, obviously 
the Wang man mentioned macros in lay terms. "You can 'program' it using 
these macros ?". "Sure", replied the Wang man, not ever having done it.

So I did those reports he was after - as I've indicated previously it 
only took 8 hours overnight :-). The program (set of macros) was using 
an omnibus file of POs, reading each, character-by-character and picking 
out what was required. (To test I had to follow the cursor, 
character-by-character making its way through documents - and it was a 
bit of a bugger to program, having to restart where I found a glitch in 
one of my macros; cure that and start again.

When the Wang guys doing the servicing found out they got the 
eebie-jeebees - there was no precedent in Wang for using the equipment 
that long.

12. There's one problem he will have - that Three-Stage Import Wizard - 
perhaps he got the sucker to give him a macro for that too, but he needs 
to macroize that so the process is hidden from the end-user, (don't 
confuse the user with stuff they don't need to see or know about). Excel 
allows you to set Visible, which is normal user mode but with a set of 
macros creating something, you need to set 'Invisible' while the macros 
are doing their thing; when the data is in the Worksheet then reset set 
Visible.

However this is the one that truly blew me away. Look at his solution to 
getting rid of a duplicate Worksheet - see last paragraph of 6 above. 
Trying to get a handle on what the application was doing, I was asking 
numerous questions, kept on asking was the input source a COBOL ISAM, to 
which he responded talking about the CSV and Excel. Pushed to explain 
what the application was about, where did it start where did it go after 
  his part was finished, I got the following response :-

"These guys are paying me to do it and frankly I don't know or care what 
happens".

At that point I bailed out.

As I said at the beginning he doesn't need OO techniques on this one, 
just sit down and automate it with macros in Excel. Now if he asks me 
how to CALL Msexcel.exe from COBOL - it's easy - but I'll tell him to 
piss off !

---------------------------------------------------------------------
OLE EXAMPLES :

Pete's bit about M/F and OLE.  In their on-line examples there's this 
for using MS WORD :-

    $set ooctrl(+P)
     class-control.
       word is class "$OLE$word.application".
     working-storage section.
       01 theWord object reference.
     procedure division.
       invoke word "new" returning theWord
       invoke theWord "setVisible" using by value 1
       invoke theWord "Quit"
       invoke theWord "finalize" returning theWord
        stop run.

The one I have, with the compiler for Excel is not much more than that. 
Opens a new Worksheet and then some graphs and they disappear before you 
get a chance to look :-). Where I got stuck on trying to code his Import 
was the parameters required for Import. Not being in the game seeing 
that the sending parameter was expressed as a BTSR (?), which led me to 
Variants - I lost it.

Going back through Forum messages somebody was asking was there a 
'detailed' example on OLE, (possibly it was Excel, as that was what I 
was searching on). A polite but curt reply, "We don't provide detailed 
examples, just our skeletons...", as above. But make a stab at OLE and 
they are willing to put you on the right track. Folks who have 
downloaded University Editions, the path will be changed but look for 
something like the following, substituting your version number and leave 
out MERANT which is used in V 3.1 :-

"C:\Program Files\MERANT\Net Express\Base\BIN\MFNXCL31.CHM"

A complete list of M/F classes and methods. Some 20 to 30 classes for 
OLE. On the OLE sample above, they've kept it simple, but as a minimum 
you will need OLE Exceptions. Hopefully most exceptions occur in 
development, but there are always exceptions to Exceptions :-). Don't 
include the Exception Class and up pops a DOS box in the middle of 
animating containing a generalized message and something like 453456 as 
the OLE Error. I read up quickly on Exceptions and M/F have a routine to 
take the number above and translate it to some 10 generalized error 
messages. Just like file status codes, with the OLE Exceptions 
translated to generalized codes, (from M/F) you can display perhaps a 
more meaningful error messagebox to your users.

I didn't read up on SafeArrays etc., so have no idea what they are about 
- at this point in time I don't need to - see ListView below.

LISTVIEW v MS EXCEL:

I still favour the ListView over an Excel sheet - particularly using the 
application detailed above. While M/F provides a Dialog EDITOR (an 
enhanced version of MS dlgedit.exe) that allows you to select icons and 
drag them into your Dialog drawing pane, back in VISOC and since, they 
have never provided an icon for ListView. (No Dialog SYSTEM until 
resurrected in N/E V 1 or 2), so I didn't recognise the difference 
between the terms Listview and Listbox, until somebody wised me up. 
Selecting the Treeview icon gives a blank pane within your draft Dialog, 
where you want the Treeview located - then it's up to you using three 
classes relating to Treeview. So ListView -  create a pane and then use 
three similar classes to create the Listview.

It made absolute sense to me, restrict what you display to a user, 
rather than overkill and confusion by displaying everything. Their OO 
example - Phone application - follows that route. Display a Lisbox 
approx 30% of the screen and you can maximise. Select a line from the 
Listbox and up pops a child dialog containing data for the collection 
element. I've adapted that to display key information in a Listbox, 
perhaps no more than four or five fields - so the user can quickly 
identify. Select the element in the list and I bring up a child Record 
Dialog and go retrieve all info for that selection from a COBOL file or 
DB. (That wretched record above - 3,030 characters - a parent dialog and 
assemble the data into meaningful groups and give the user push buttons 
to select between different sub-dialogs).

Now aware of the ListView as opposed to ListBox, I favour the former for 
its elegant grid. The technique to use either is the same - list, 
select, child-dialog.

In terms of collections/dictionaries/lists it pays to bear in mind data 
volumes, unless of course you quite happily want to add a few trillion 
more Megabytes on your machine, and the end-user's who will be using 
your application. So given a "List" the storage requirements are (1) 
object reference for the Collection, object reference for each element 
and then what's being displayed per element, 50, 60, 100 characters (pic 
x and pic 9).

The Listview is completely controllable by me through OO COBOL, possibly 
even more enhanced through dotNet. (Bye the bye - I did suggest Himself 
take a look at the Listview Demo in Dialog System as an alternative. No 
reaction whatsoever).

Jimmy, Calgary AB
```

#### ↳ Re: COBOL to MS Excel

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-11T15:12:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bqe80F22sccbU1@mid.individual.net>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad>`

```
James J. Gavan wrote:
> Our fiend with his percentage format, and problems associated with
> getting an Import to MS Excel.
…[3 more quoted lines elided]…
> Merely use COBOL to CALL msexcel.exe !

That is certainly _A_ solution...  The sad fact is that he could easily do 
all the things he needs and wants to, using COBOL, and controlling Excel 
from it. However, he would need to get to grips with the Classes, Methods, 
and properties that are exposed through the OLE interface to Excel (he was 
given detailed instructions on how to do this using the free Object Browser 
that comes with Office products (including Excel), but he just ignored it.)
>
> To be completely blunt - he is a lazy SOB, trying to do a cut and
> paste job where hopefully people supply him with specific code for
> his problem.

Nice work if you can get it :-)

>
<snipped personal stuff>

> Here we go - He has used M/F COBOL for decades and at 70 may possibly
> have more years in COBOL than Pete Dashwood.

I'm quite sure there are people out there who have less years with it than I 
do (42 this year) and still know more about programming in general than I 
do... Very occasionally I bump into someone who has done the same or more 
COBOL as I have and there seems to be an instant "old-timers" bond :-). I 
had a hard time finding an ISP who would let me run ActiveX and COM 
components on his web servers. Fortunately, the one I'm using for PRIMA is 
an old time COBOL guy... turned out we knew a number of people in common 
from the "old days" (60s and early 70s) in Wellington. Instead of just 
saying:"No, our security policy prevents us from doing that" he asked if I 
would let him see the source code (some of the components are in COBOL, 
others in C#). I told him to be my guest (I have nothing to hide) and he 
then went the extra mile to help me get the components up and running. (We 
have never had a problem with any of them and you can bet this man will be 
getting my internet business for the rest of my life :-))

> From conversation he
> PROUDLY tells me, with a laugh, that he is a spaghetti coder. I know
> the term and after all these years I have contact with one ! Even
> worse he likes working with the other two guys because their
> programming style is the same as his.

I guess not everybody cares about it, Jimmy.  I knew a guy once who was very 
proud of his ability to crush children. He didn't understand why I couldn't 
share his enthusiasm.


> OMG ! When he says spaghetti
> code I believe him - I've seen some of his code associated with this
…[3 more quoted lines elided]…
> dead.

Perhaps the above is a little unfair to those of us who are self taught...? 
:-)

>Terms like Three Tier Systems, Structured Programming would go
> completely over his head - so imagine how he had a nice fit with
> something like OO COBOL.

Yes, from my limited interaction with him (and I don't want to talk about 
Paul as if he wasn't here) I realized that he had no inkling with regard to 
OO. (The "List of invokes" was a dead giveaway...).

Nevertheless, it isn't a crime to not know something, and people come here 
for help.

Hopefully, if we can stimulate them to find out more than is required to 
solve the immediate problem, so that they are better equipped to solve 
similar problems in the future, then everybody wins. For myself, I'm pretty 
laid back about this. I gave him the very best advice I could and explained 
what he needed to do and how to do it. But it involved more effort than he 
was prepared to make. Fair enough, it's his decision. You can lead a horse 
to water... etc. At the end of the day, people who offer advice here are not 
being paid to do so, so why get unwrapped over something you did 
voluntarily?

>
> Remember he is the one wanting to use Excel, not me. I don't think he
> even looked at Excel. Had he done so, he would have found the answer
> to his percentage problem. I read it, didn't absorb it, but know it's
> there - I still maintain it is a crappy approach.

Most approaches have pros and cons. Many people find managing MS Office, 
through the OLE/COM interfaces provided, to be easy and convenient from 
COBOL. I certainly have, and have accessed and manipulated Excel, Word, and 
Access in this way. Having at least a fundamental understanding of OO is 
valuable in this context (so you can decide what methods to invoke and 
properties to access), but you certainly don't need to be an OO programming 
expert. Anything you can do with macros or VBA modules/procedures in the 
native package, you can do with COBOL through OLE/COM.

(The OLE/COM interface for Office products (it's correct name is "Office 
Automation", because it allows you to control Office products from your 
application program) can be invoked from anything that supports the COM 
interface, not just COBOL. I have used it from VB, C#, and Fujitsu OO COBOL 
(NetCOBOL and PowerCOBOL).
>
> Let's put another one to rest on performance and volumes. Looks to me
…[11 more quoted lines elided]…
> sheet(s) that they LOVE - but about what, absolutely no specifics.

He may be bound by a nondisclosure agreement, Jimmy. I have a client who is, 
and I had no idea what he was using my Toolset for. When it was necessary 
for me to look at some of his source, I simply signed the same agreement. I 
still don't know the details of what he is doing and I don't need to or want 
to. If he needs for me to know, he'll tell me.

The point is that, while it is nice to have a full understanding of an 
application, if you are being asked simply to fix something, it may not be 
necessary to know EVERYTHING about it.

>
> 3. Sample test CSV gives 5,046 rows, 31 columns with a row width up to
…[4 more quoted lines elided]…
> the data.

A very innovative solution... :-)


>
> 4. The data displayed looked absolutely meaningless to me, and I don't
…[5 more quoted lines elided]…
> users in North T**** !

Possibly. It is also possible they have more information than you do... :-)

>
> 6. When are CSVs produced - as and when, monthly, daily and perhaps
…[18 more quoted lines elided]…
>

Good stuff...

> Anybody got a problem with the ISO date-format or perhaps why I'm
> using it that way ?

It is important to have time as part of it.

>
> On the above, I said with that structure, to avoid creating a
> duplicate Active WorkSheet for the same day he should use
> CBL_CHECK_FILE_EXIST, and signal a message to the user. Impetuously
> his response was, "No problem, I'll just delete the first one".

Depending on the application that MIGHT be valid. Your suggested solution is 
much better, but it could get tedious if someone tries to create say 20 or 
thirty duplicates and has to click on each one to say it isn't needed... It 
really comes down to whether having more than one per day is valid and 
whether they need to be consolidated before processing. More to it than 
meets the eye...

>
> 7. Obviously wrong now, but I thought I'd have a shot and tickle his
…[3 more quoted lines elided]…
> Pontius was a Pilate.

His choice. There are many people who feel that way. For some of them, it's 
academic and they are retiring soon, for the younger ones who still have a 
carer to consider, they are realizing that procedural COBOL alone is not 
going to make them a living in the long term. Paul is at a time where he 
wants to get by on what he knows, without necessarily wishing to learn new 
stuff. It is really his prerogative. However, when he finds he needs to do 
something which his current skill set is not up to, then he must choose to 
either acquire the knowledge he needs, or offload the task to someone else. 
People who don't know their own limitations are dangerous; very occasionally 
they achieve something in a way it hasn't been done before, more often than 
not though, they simply bang their head against the wall until they finally 
quit.
>
> 8. While this is going on, he's still dabbling with his spaghetti and
> asking question of any warm bodies he can find. Not successful
> initially, because it was a bunch of "You could...", or "You can
> try..." based on what he was asking.

A salutary lesson to all of us that the forming of the question is every bit 
as important as the answer.
>
> 9. In addition to the above I loaded Excel to see what it was about.
> Almost without thinking, I imported that CSV file above - BLIP ! Was
> done in perhaps 5 to 7 seconds, if not less. Just manually select
> "Import".

...Or... you could activate the Import method under the control of your 
COBOL program...



>However there is a three stage Excel Wizard prompting you on
> the csv file, separator symbols, etc. I ignored that just importing as
> is - got all the columns, but without widths specified, text columns
> get truncated. You have to include the Import Wizard.

There are properties that can be set to control all of this.

>
> 10. Told him what I had done in 9. His CSV has the column headings as
…[12 more quoted lines elided]…
> examples.

He could do all of this from COBOL. Of course, it's a lot easier if you have 
someone who will write code for you, for free... :-)
>
> Had I been aware of the Macro feature, (and I'm not the one who was
…[3 more quoted lines elided]…
> interest this is what I intended for him about macros :-

Sometimes, you just have to assess the situation and cut your losses. I did 
that with Paul when I realized he was never going to do what was requested, 
even if it was spelled out for him. It's not personal, just different 
personalities.

<snipped anecdote on Wang> Why does that name always make me smile? It's 
really time I grew up... :-)

> 12. There's one problem he will have - that Three-Stage Import Wizard
> - perhaps he got the sucker to give him a macro for that too, but he
> needs to macroize that so the process is hidden from the end-user,
> (don't confuse the user with stuff they don't need to see or know
> about).

it's really very easy to make it a "one stage" process that can be as 
visible as you like.


>Excel allows you to set Visible, which is normal user mode
> but with a set of macros creating something, you need to set
> 'Invisible' while the macros are doing their thing; when the data is
> in the Worksheet then reset set Visible.

Sure, it is easy to do the same in COBOL.

<snipped unfair public reporting of a private conversation>


> At that point I bailed out.
>
Given Paul's observed behaviour previously in this forum, that is probably 
the best thing to do.


> As I said at the beginning he doesn't need OO techniques on this one,
> just sit down and automate it with macros in Excel.

But the Macros are simply invoking OO Methods already available. His stated 
requirement was to do it from COBOL. It is possible (in fact, you could 
argue it is actually easy), but it requires some time for Paul to get the 
fundamentals, then use the Object Browser provided to see what can be done. 
He doesn't want to do that. Fair enough. His call. Let it go.


>Now if he asks me
> how to CALL Msexcel.exe from COBOL - it's easy - but I'll tell him to
> piss off !

Jimmy, you are taking this to heart and letting it upset you. You tried to 
help, but Paul is a case that cannot be helped. It would require a change of 
attitude and he is perfectly happy with the attitude he has. (And no-one can 
deny people the right to be what they want to be...).

A number of people here tried to help but it was pointless.

Think of it as his loss, if that helps.

>
> ---------------------------------------------------------------------
…[16 more quoted lines elided]…
>
Thanks for posting that. Interesting, and, as you noted, simple.

> The one I have, with the compiler for Excel is not much more than
> that. Opens a new Worksheet and then some graphs and they disappear
> before you get a chance to look :-).

Ah, perhaps you can fix it so it doesn't...?


>Where I got stuck on trying to
> code his Import was the parameters required for Import. Not being in
> the game seeing that the sending parameter was expressed as a BTSR
> (?), which led me to Variants - I lost it.

COM uses platform independent data types. They look a bit strange at first, 
but once you get the hang of it they are quite straightforward.

Because you have laboured this at length and it has been interesting, here's 
some quick explanation...

1. COM data types are referenced as "VT_x" where "x" can be a number of 
things (see list below). The "VT_" indicates "Variant". A variant is a 
datatype which says: "I could be anything, but the code that uses me will 
know how to deal with me."  You might think: "well, isn't that what we use 
PICTURE X for?" and you would not be far wrong, but a variant could be 
floating point or Unicode so there is a subtle difference. It is interesting 
(well, to me, at least... :-)) that in the .NET environment, the variant 
data type is replaced by an object reference.

2. Here is a table of the commonest COM datatypes. Your COBOL compiler will 
convert them to the forms shown. There are many riders and rules regarding 
decimal alignment, precision, effect of compiler options, allowed 
conversions for early and late binding, and these are all compiler dependent 
so you would need to check the documentation on COM for your particular 
compiler if something doesn't work, but for most "normal" operations using 
simple data types, everything works swimmingly. (The list here is not 
comprehensive; there are other VT_ possibilities)

VT_I2         Integer 2 bytes        any valid COBOL numeric or numeric 
edited field (s9(4) comp is probably most efficient)
VT_I4         Integer 4 bytes        any valid COBOL numeric or numeric 
edited field (s9(9) comp is probably most efficient)
VT_CY       Currency                any valid COBOL numeric  or numeric 
edited field with a picture of s9(14)v9(4)
VT_DECIMAL Decimal            any valid COBOL numeric  or numeric edited 
field containing a v
VT_R4        Real 4 bytes            COBOL "short" floating point (COMP-1)
VT_R8        Real 8 bytes            COBOL "long" floating point  (COMP-2)
VT_BSTR   ASCII string           COBOL PIC X (In Fujitsu environments 
VT_BSTR is 8192 bytes.)
VT_DATE   Date                       Any COBOL numeric, floating point, or 
alphanumeric that can accommodate a date

Using the information above, it should be pretty easy to interface to any of 
the OLE/COM methods or properties.

>
> Going back through Forum messages somebody was asking was there a
> 'detailed' example on OLE, (possibly it was Excel, as that was what I
> was searching on).

OLE is the Object Linking and Embedding technology which MS originally 
developed for their own use. It has evolved into the Component Object Model 
(COM). OLE is obsolete now.


<snipped discussion of listview etc>

There IS a place for all of the devices you mentioned, even though at first 
glance they may appear similar. I wouldn't replace an Excel spreadsheet with 
a listview, but I have no difficulty in using Excel from anything I want to.

Just a final point, Jimmy.

Sometimes, when you've had a frustrating experience trying to help somebody 
and it hasn't gone the way you might want it to, it is easy to lose 
perspective and let anger get the better of fairmindedness. (Most of us have 
done it, but it really isn't fair.)

It is out of order to relay private conversations and things people said in 
a personal situation, without their permission, to their detriment, in 
public.

Doing so actually diminishes the poster. I reckon you're better than that.

Pete.
 -- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: COBOL to MS Excel

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-13T09:44:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<valm55pe4ejom081l39iafclnfbqsms4j4@4ax.com>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad> <7bqe80F22sccbU1@mid.individual.net>`

```
On Sat, 11 Jul 2009 15:12:05 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>That is certainly _A_ solution...  The sad fact is that he could easily do 
>all the things he needs and wants to, using COBOL, and controlling Excel 
…[3 more quoted lines elided]…
>that comes with Office products (including Excel), but he just ignored it.)

There are some simpler ways for someone like him - in the right shop.
For instance, he could have a program that converts output to XML, and
let someone else worry about Classes, Methods, or properties.

I've written plenty of programs that read or wrote delimited files to
be FTPd between the mainframe and desktops for users using Excel.

But in our new system, we have tools that will extract data and open
up Excel to view them - the interface is automatic.    We don't need
programmers who know those skills (OLE, methods, etc)- we need people
who understand the data and their business needs.   
```

###### ↳ ↳ ↳ Re: COBOL to MS Excel

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-14T12:16:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c213bF252ul3U1@mid.individual.net>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad> <7bqe80F22sccbU1@mid.individual.net> <valm55pe4ejom081l39iafclnfbqsms4j4@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 11 Jul 2009 15:12:05 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> let someone else worry about Classes, Methods, or properties.

Agreed there are many ways to get data in and out of Excel and other Office 
products.

However, this was a COBOL programmer requesting a COBOL solution. When he 
got it, it was just "too hard".
>
> I've written plenty of programs that read or wrote delimited files to
…[3 more quoted lines elided]…
> up Excel to view them - the interface is automatic.

What happens if your users need to display the data differently for some 
sheets? Can a different template be specified to the "automatic interface", 
for instance...?

>  We don't need
> programmers who know those skills (OLE, methods, etc)- we need people
> who understand the data and their business needs.

Howard, somebody wrote your "automatic" interface, even if it is just using 
file association. I take your point that in your case you need more business 
analysts than programmers; that's an increasingly common requirement as the 
"nuts and bolts" of programming become buried ever deeper under the covers, 
and it is no bad thing.Business knowledge trumps programming knowledge and 
always has done. You can get a technical solution to a sticking point in 
programming pretty easily, even if it means hiring a consultant for a day or 
two; a knowledge and understanding of the business processes and 
implications of changing them cannot be so easily obtained. A programmer who 
has both is beyond rubies...

However, the solution for Paul was not subject to that requirement.

He requested a programming solution. To control Excel from COBOL requires 
some familiarity with OLE, unless all you want to do is start it up (You can 
do THAT from a simple shell, just like any other program...).

Sometimes, a person asks a question and they don't like the answer they get. 
(I am reminded of the Oracle at Delphi, where the answers were often 
deliberately obtuse to make the interrogator think more carefully about why 
they were seeking advice in the first place... In Paul's case, a straight 
question was asked and a straight answer was received. The question was 
not:" How should I go about doing this?" it was a request for a list of 
possible invokes...)

Maybe the question needs to be formulated differently, maybe the person 
asking it needs to do more, who knows?

A fair solution was provided and time was taken to provide it and make it 
"doable" for someone not necessarily familiar with what was involved.

My conscience is clear... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL to MS Excel

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-14T08:36:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n25p55pgbpjihd9h5qqqsr28sno17tq7cm@4ax.com>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad> <7bqe80F22sccbU1@mid.individual.net> <valm55pe4ejom081l39iafclnfbqsms4j4@4ax.com> <7c213bF252ul3U1@mid.individual.net>`

```
On Tue, 14 Jul 2009 12:16:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:


>Agreed there are many ways to get data in and out of Excel and other Office 
>products.
>
>However, this was a COBOL programmer requesting a COBOL solution. When he 
>got it, it was just "too hard".

Yes, I understand, I was expanding the discussion beyond that one
user.   People like him need to be worked around, we just need to know
such obstacles are there and do what we can.

>> I've written plenty of programs that read or wrote delimited files to
>> be FTPd between the mainframe and desktops for users using Excel.
…[6 more quoted lines elided]…
>for instance...?

I don't yet know enough to answer that with certainty, but I believe
the answer is yes.

>>  We don't need
>> programmers who know those skills (OLE, methods, etc)- we need people
…[11 more quoted lines elided]…
>has both is beyond rubies...

That is the core of how things are changing, and why companies IS
staffs are having fewer and fewer applications programmers.

It isn't just CoBOL programmers who need to adapt, all company
applications programmers need to see which way the wind is blowing. 
>However, the solution for Paul was not subject to that requirement.
>
>He requested a programming solution. To control Excel from COBOL requires 
>some familiarity with OLE, unless all you want to do is start it up (You can 
>do THAT from a simple shell, just like any other program...).

And as you said, he wasn't willing to accept a programming
requirement, so I continued the discussion in a tangent that interests
me more than obstinate programmers do.
```

###### ↳ ↳ ↳ Re: COBOL to MS Excel

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2009-07-19T20:35:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BJQ8m.20060$8l4.6342@newsfe10.iad>`
- **In-Reply-To:** `<n25p55pgbpjihd9h5qqqsr28sno17tq7cm@4ax.com>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad> <7bqe80F22sccbU1@mid.individual.net> <valm55pe4ejom081l39iafclnfbqsms4j4@4ax.com> <7c213bF252ul3U1@mid.individual.net> <n25p55pgbpjihd9h5qqqsr28sno17tq7cm@4ax.com>`

```
Quick update. Paul has family with him this week, children, grand-kids 
etc., so naturally tied down. We wont be talking in detail until next 
week. I anticipated it - but at the moment he is still trying to use the 
macros, and is stumped at this point in time on CALLing MS Excel with a 
flag to trigger his master macro to set off the others to get the Import 
macro to function.

Suffice to say at 70 he needs the $$$$$s just like I do. I think his 
mind is go with what he has put some effort into so far and make it 
work. To be realistic he like me is never going to get a 'real' COBOL 
job or any other job for that matter, and appears to have two guys 
(employers), who fit in with his needs.

Whether he can be persuaded to do it crisply in OO COBOL, I just don't 
know. I've even offered to do it for him, but I don't think he gets the 
message. With solid days put in, which I wont (e.g. gardening in our 
short summers), I could knock it off in less than a week utilising 
classes I already have designed. It requires one dialog (1) Drop list - 
listing Master templates, select and (2) it displays the name of the 
generated Spreadsheet, (3) Droplist - Display list of available Input 
CSVs and select appropriate. Now do the import - the sticking point - 
I'm so close.

The answer to the Import is the MSDN that Frederico recommended looking 
at. See following on Import :-

http://msdn.microsoft.com/en-us/library/aa562381.aspx

You can search the net in vain, numerous knowledge base articles and 
umpteen 'how to's' from outsiders. The sheer volume indicates problems 
with the MS Approach. If they focused everybody (in programming) on the 
MSDN and each article, like the Import I refer to above, THEN within 
those pages they could expand to the Knowledge Base with a series of 
articles amplifying their own MSDN Import routine.

It's all there awaiting 'translation;' to COBOL using their Basic 
example as a guide. I hope Ballmer starts to need glasses then he can 
bitch at the MSDN team to make the examples readable. I had to copy and 
paste into Word to get a decent viewing of the example text.
Coupled with those VT_ thinggies recommended by our Resident Expert, 
back to looking at the M/F On-line covering this and if I get truly 
stuck asking the M/F Forum. Show them the code I have attempted and 
although it is not their baby, I think they will come across.

Having looked at the Import Example, briefly, the question I have is, 
does one send ALL the parameters required, that is both fixed and 
optional, using zeroes perhaps for the optionals not used ?

However, I think Paul's mindset is stick with good ole spaghetti COBOL 
for general use and use his macros which are specific to his project.
(Shame if he does do preceding - I could have challenged him, using OO, 
to try and fit in his beloved spaghetti ). Just have to wait and see 
what he concludes next week, after discussion. (Dammit, I might just 
give that import a shot before we talk again !).

Only came out in an e-mail two days ago to me. He has medical problems, 
lacks stamina, (still we all do when 70 +), plus if he had a real job he 
could fall asleep at the desk. I'm doing the apologizing to him, now 
that I know some background. Well naturally you don't start off a 
conversation with a fellow programmer with, "I've got medical problems, 
blah, blah", instead of, "I program this and that and achieve etc....."

Jimmy
```

#### ↳ Re: COBOL to MS Excel

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-13T08:45:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40im55lpfq0kp623dpuqq8uabfsv2le7mc@4ax.com>`
- **References:** `<znQ5m.28$ho.17@newsfe02.iad>`

```
On Fri, 10 Jul 2009 17:44:34 -0600, "James J. Gavan"
<jgavandeletethis@shaw.ca> wrote:

>When he says spaghetti code I believe him - I've 
>seen some of his code associated with this Import problem. He must have 
>been self taught because if any tech instructor told him to do it the 
>way he does, the latter gentleman should have his genitals removed, even 
>if that instructor is already dead.

In the early days, structured programming wasn't taught.   It took a
while to learn what processes worked well.

That said, I see way too much spaghetti code by people young enough to
have been taught better.   Usually, they never were taught better and
didn't have any interest in learning.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
