[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Phase 1 - OO Rosetta Bottles of Beer

_11 messages · 5 participants · 2010-11_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Phase 1 - OO Rosetta Bottles of Beer

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-07T12:38:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FeDBo.18820$3f.1700@newsfe12.iad>`

```
Well I'm there about 99.9%. What really bugged me and held me up was to 
do the following. Bearing in mind Alistair's observation (complaint), it 
is a drag to go through a screen display. I arrived at four options :-

        Rosetta - NINETY-NINE BOTTLES

  (1) Display results on Screen
  (2) Write to Text File - Notepad Edit
  (3) Write to Text File - MS Word Edit
  (4) Show results in a GUI Listbox

      Enter choice : -

The one that held me up - dear ole Microsoft's Word with all the jazz 
needed to get at it as an OLE !!!!  It was in another project - Common 
Dialogs that I initially came up against the problem. But I thought I 
had solved it. Meanwhile I changed machines, and can't be sure what 
happened. We've all used the phrase "Well it used to work and I haven't 
changed anything....." Yes - it's a question of triggering a memory of 
what we *actually* did do.

To cut a long story short M/F had a demo - a Procedural example program 
CREATEP (Create Process) and through it they call Notepad to open an 
existing document. Works like a dream - and uses some three API Calls.

Not to digress at this stage between the simplicity of the API approach 
and getting an OLE version of MS Word to STAY ON THE DAMNED SCREEN, that 
is, pause and let you view what they have done, before it automatically 
quits, I've adapted # 2 above (which is the CreateP) to do exactly that 
for # 3 above, MS Word. I'm not advocatng APIs as a solution, but it 
works in this case. While browsing through my computer I came across an 
example from the young feisty Kellie Fitton, (from California), using 
APIs - remember her ? It works fine, but all that coding for APIs - 
hardly productive in the modern world.

More later on APIs and MS Word to see if we can get it working. Will be 
posted in a separate thread..

The following is no candidate for Rosetta, it goes way beyond the 
'cutsie' snippets of program code provided for most languages. (We will 
exclude Richard's Iteration Program from that comment). This is the 
heart of the topic in my version, the logic for the count.

This Bottles of Beer is a good topic for M/F users to show what can be 
done with OO - so I'll post a zipfile to the Micro Focus Forum. Even 
non-M/F users can access that site as 'Guests'. I'll let you know when 
done and how to get a download, if you are interested. I'll call that 
message 'Phase 2 - Bottles of Beer'

I hope it's understood this will only work with M/F compilers - I've 
used every trick in the book "exclude red tape" to reduce the coding.
I can't be certain, but I'm guessing it may work as far back as M/F's 
VISOC; I know my coding works with V 5.0, (I sent somebody in Brazil a 
separate early zipfile on 'TestDialogs') So if you do have a copy of the 
various compilers .....???

I did post a copy of this to CLC with an zip attachment, containing a 
Systems Flowchart and screenshots of the the displays from the four 
options. Didn't appear in CLC and you don't even get a message back 
saying 'your message was undelivered'.

So for the moment a Mickey Mouse version of the flowchart so that you 
can see where BottleCount below fits into the scenario.

**********************************************************

1. Trigger-Bottles
-------------------
intiates the Project &
first call to Win GUIAPIs

2. Driver-Bottles-App
----------------------------
Invokes (3) Mycollections to -------> 3.\copylib\MyCollections
create two collections                 ------------------------
(a) Text-Collection
(b) Object-Collection.

Passes these two collections -------> 4. Bottlecount (below)
to (4) BottleCount where elements      -----------------------
are added to the Collections

(5). If your choice was #1 - uses a
Callback to display on DOS Screen
from the Text-Collection

For Choices 2 and 3 uses a
Callback to write to (6) LineSeq
.
------------------------------------> 6. \Copylib\FileLineSeq
.                                     -----------------------
.                                     writes to diskfile
.                                     BottleCount.txt
.
.                                     7. \Copylib\FileErrors
.                                     ----------------------
.                                     File Status Errors
---------> 9. MyCreateP
.         -------------               8. \Coplib\MyMessages
.         Accesses disk to open       ----------------------
.         BottleCount.txt             invokes M/F messagebox.
.         in NotePad or MsWord
.
---------> 10.Dialog-Bottles
.          -----------------
.          (GUI parameters)
.
.--------> 11. MyDialog-Listbox-------> 12. \Copylib\MyDialog
           --------------------         ---------------------
           Sub-Class inheriting         Displays Object Collection
           from (12) MyDialog.          in a Dialog with a Listbox
           Has ONE method to override   and just an 'Exit' button
           the Listbox method in
           MyDialog - so that it
           doesn't need a Window event
           for the Listbox


******************************************************************


Here's the source of BottleCount

Jimmy, Calgary AB

APART FROM THE START METHOD "Main", all other methods are listed 
ALPHABETICALLY :-


  *>-----------------------BottleCount.cbl ------------------------
$set ooctrl(-w)

  *> Above Directive allows N/E V 3.1 to use 'Working-Storage'
  *> within methods

  *>---------------------------------------------------------------
  *> OO COBOL - Micro Focus Net Express V3.1 and Wndows XP -
  *>
  *> Author : jgavan@shaw.ca     Date Revised : 2010 Oct 28
  *>
  *>---------------------------------------------------------------
  *>
  Class-id.           BottleCount inherits from Base.

  Class-Control.

          *> M/F Support classes :
          CharacterArray          is class "chararry"

          *> Your classes :
          BottleCount             is class "bottlecount"
          .

  *>---------------------------------------------------------------
  FACTORY.
  *>---------------------------------------------------------------
  WORKING-STORAGE SECTION.
  copy "BottlesChoice.cpy".

  78 ML               value 10.   *> Message Length
  78 SC               value 22.   *> Change the value of this and
                                  *> re-compile if you want to
                                  *> whizz through the display

  78 TR               value 80.   *> Max-Length of Text-Result and
                                  *> Lnk-Element
  78 Tilde            value "~".

  01 charx                        pic x.
  01 Current-NumberName           pic x(15).
  01 Next-NumberName              pic x(15).
  01 Kounter-1                    pic 9(02).
  01 Text-Result                  pic x(TR).

  *> Literal Tables : Initially I tried placing these in the method
  *> they appeared to be solely relevant to i.e., "GetFiveLines".
  *> Unfortunately the indexing in the tables is used elsewhere.

  01  Digits-Table.
      05   pic x(ML) value "One~".
      05   pic x(ML) value "Two~".
      05   pic x(ML) value "Three~".
      05   pic x(ML) value "Four~".
      05   pic x(ML) value "Five~".
      05   pic x(ML) value "Six~".
      05   pic x(ML) value "Seven~".
      05   pic x(ML) value "Eight~".
      05   pic x(ML) value "Nine~".
      05   pic x(ML) value "Ten~".
      05   pic x(ML) value "Eleven~".
      05   pic x(ML) value "Twelve~".
      05   pic x(ML) value "Thirteen~".
      05   pic x(ML) value "Fourteen~".
      05   pic x(ML) value "Fifteen~".
      05   pic x(ML) value "Sixteen~".
      05   pic x(ML) value "Seventeen~".
      05   pic x(ML) value "Eighteen~".
      05   pic x(ML) value "Nineteen~".
      05   pic x(ML) value "~".

  01  Filler redefines Digits-Table.
      05 Digits  pic x(ML) occurs 20
                indexed by Digits-Idx.

  01  Tens-Table.
      05   pic x(ML) value "~".
      05   pic x(ML) value "Twenty~".
      05   pic x(ML) value "Thirty~".
      05   pic x(ML) value "Forty~".
      05   pic x(ML) value "Fifty~".
      05   pic x(ML) value "Sixty~".
      05   pic x(ML) value "Seventy~".
      05   pic x(ML) value "Eighty~".
      05   pic x(ML) value "Ninety~".
      05   pic x(ML) value "~".

  01  filler redefines Tens-Table.
      05 Tens pic x(ML) occurs 10
              indexed by Tens-Idx.

  *>-------Object References.

  01 os-ObjectCollection       object reference value null.
  01 os-TextCollection         object reference value null.

  *>---------------------------------------------------------------
  Method-id. "Main".
  *>---------------------------------------------------------------
  Linkage section.
  01 lnk-Choice                      pic x(4) comp-5.
  01 lnk-ObjectCollection            object reference.
  01 lnk-TextCollection              object reference.

  Procedure Division
      using Lnk-Choice, Lnk-ObjectCollection, Lnk-TextCollection.

  move lnk-Choice          to BottlesChoice
  set  os-ObjectCollection to lnk-ObjectCollection
  set  os-TextCollection   to lnk-TextCollection
  move 99                  to Kounter-1
  invoke self "DecrementCount"

  *> Having finished with the method "DecrementCount", this class
  *> returns to BottleDriver where the results are displayed
  *> according to user's choice.

  End Method "Main".
  *>---------------------------------------------------------------
  Method-id. "AddToList".
  *>---------------------------------------------------------------
  01 RecordLength                 pic x(4) comp-5 value TR.
  01 ls-Object                    object reference.

  if    DisplayOnScreen
        invoke os-TextCollection "add" using Text-Result

  else  invoke CharacterArray "withLengthValue"
               using RecordLength, Text-Result
               returning ls-object
        invoke os-ObjectCollection "add" using ls-object
  end-invoke

  *> The two collectons above were created 'empty' from class
  *> Driver-Bottles-App. This class adds elements to either
  *> collection, but the updated Collections are *** NOT ***
  *> returned through Linkage to Driver-Bottles-App.

  *> With a 'common' object reference, shared with this Class,
  *> Driver-Bottles-App knows how many Elements this class has
  *> added and the properties associated with those elements.

  End Method "AddToList".
  *>---------------------------------------------------------------
  Method-id. "DecrementCount".
  *>---------------------------------------------------------------

  *> This is a RECURSIVE METHOD - i.e. the method re-invokes itself

  01 Subtractor                        pic 9.

  move zeroes to Subtractor
  invoke self "GetNumberName" using Subtractor
              returning Current-NumberName

  move 1 to Subtractor
  invoke self "GetNumberName" using Subtractor
              returning Next-NumberName

  invoke self "GetFiveLines"

  compute Kounter-1 = Kounter-1 - 1

  if    Kounter-1 <> zero
        invoke self "DecrementCount"
  End-if.

  End Method "DecrementCount".
  *>---------------------------------------------------------------
  Method-id. "GetFiveLines".
  *>---------------------------------------------------------------
  78 TL                value 35.
  78 MX                value 6.
  01 Text-Table.
   05 pic x(TL) value " Bottles of Beer~".                  *> 1
   05 pic x(TL) value " on the Wall .....~".                *> 2
   05 pic x(TL) value "Take one down and pass it around ".  *> 3
   05 pic x(TL) value "Only one Bottle left~".              *> 4
   05 pic x(TL) value "No more Beer left".                  *> 5
   05 pic x(TL) value "Please go get some more beer".       *> 6

  01 Filler
     redefines Text-Table.
     05 Temp-Text  occurs MX pic x(TL).

  01 LineNumber                       pic x(4) comp-5.

  *> Sample output specified by Rosetta :

  *> Line 1 - Ninety-Nine Bottles of Beer on the Wall .....
  *> Line 2 - Ninety-Nine Bottles of Beer
  *> Line 3 - Take one down and pass it around
  *> Line 4 - Ninety-Eight Bottles of Beer on the Wall .....
  *> Line 5 - spaces


  PERFORM varying LineNumber from 1 by 1 until LineNumber > 4

       Initialize Text-Result

       Evaluate true also true

       *>---------------------------------
       *> TABLE A : LineNumber = 1
       *>---------------------------------
       *> Kounter-1 > 2          y
       *> Kounter-1 = 2          -  y
       *> Kounter-1 = 1          -  -  y
       *>---------------------------------
       *> 1 - Plural             1  1  -
       *> 2 - On the Wall        2  2  2
       *> 3 - Take down          -  -  -
       *> 4 - Only one           -  -  4
       *> 5 - No More            -  -  -
       *> 6 - Go get             -  -  -
       *>---------------------------------

         when LineNumber = 1 also Kounter-1 > 2
         when LineNumber = 1 also Kounter-1 = 2

              string Current-NumberName delimited by Tilde
                     Temp-Text(1)       delimited by Tilde
                     Temp-Text(2)       delimited by Tilde
                     into Text-Result
              end-string
              invoke self "AddToList"

         when LineNumber = 1 also Kounter-1 = 1

              string Current-NumberName delimited by Tilde
                     Temp-Text(4)       delimited by Tilde
                     Temp-Text(2)       delimited by Tilde
                     into Text-Result
              end-string
              invoke self "AddToList"

       *>---------------------------------
       *> TABLE B : LineNumber = 2
       *>---------------------------------
       *> Kounter-1 > 2          y
       *> Kounter-1 = 2          -  y
       *> Kounter-1 = 1          -  -  y
       *>---------------------------------
       *> 1 - Plural             1  1  -
       *> 2 - On the Wall        -  -  -
       *> 3 - Take down          -  -  -
       *> 4 - Only one           -  -  4
       *> 5 - No More            -  -  -
       *> 6 - Go get             -  -  -
       *>---------------------------------

         when LineNumber = 2 also Kounter-1 > 2
         when LineNumber = 2 also Kounter-1 = 2

              string Current-NumberName delimited by Tilde
                     Temp-Text(1)       delimited by Tilde
                     into Text-Result
              end-string
              invoke self "AddToList"

         when LineNumber = 2 also Kounter-1 = 1

              string Current-NumberName delimited by Tilde
                     Temp-Text(4)       delimited by Tilde
                     into Text-Result
              end-string
              invoke self "AddToList"

       *>---------------------------------
       *> TABLE C : LineNumber = 3
       *>---------------------------------
       *> Kounter-1 > 2          y
       *> Kounter-1 = 2          -  y
       *> Kounter-1 = 1          -  -  y
       *>---------------------------------
       *> 1 - Plural             -  -  -
       *> 2 - On the Wall        -  -  -
       *> 3 - Take down          3  3  3
       *> 4 - Only one           -  -  -
       *> 5 - No More            -  -  -
       *> 6 - Go get             -  -  -
       *>---------------------------------

         when LineNumber = 3 also any

              move Temp-Text(3) to Text-Result
              invoke self "AddToList"

       *>---------------------------------
       *> TABLE D : LineNumber = 4
       *>---------------------------------
       *> Kounter-1 > 2          y
       *> Kounter-1 = 2          -  y
       *> Kounter-1 = 1          -  -  y
       *>---------------------------------
       *> 1 - Plural             1  -  -
       *> 2 - On the Wall        2  -  -
       *> 3 - Take down          -  -  -
       *> 4 - Only one           -  4  -
       *> 5 - No More            -  -  5
       *> 6 - Go get             -  -  6
       *>---------------------------------

         when LineNumber = 4 also Kounter-1 > 2

              string Next-NumberName    delimited by Tilde
                     Temp-Text(1)       delimited by Tilde
                     Temp-Text(2)       delimited by Tilde
                     into Text-Result
              end-string
              invoke self "AddToList"

              move spaces to Text-Result
              invoke self "AddToList"

         when LineNumber = 4 also Kounter-1 = 2

              string Temp-Text(4) delimited by Tilde
                     into Text-Result
              invoke self "AddToList"

              move spaces to Text-Result
              invoke self "AddToList"

         when LineNumber = 4 also Kounter-1 = 1

              move Temp-Text(5) to Text-Result
              invoke self "AddToList"
              move Temp-Text(6) to Text-Result
              invoke self "AddToList"

       End-Evaluate
  END-PERFORM

  End Method "GetFiveLines".
  *>---------------------------------------------------------------
  Method-id. "GetNumberName".
  *>---------------------------------------------------------------
  78 HyphenTilde              value "-~".

  01 Descrip-1                pic x(10).
  01 Separator                pic x(02).
  01 Descrip-2                pic x(10).

  01 Kounter-2                pic 9(02).
  01 Kounter-3
      redefines Kounter-2.
     10 K-Tens                pic 9.
     10 K-Digits              pic 9.

  Linkage Section.
  01 lnk-Subtractor                   pic 9.
  01 lnk-NumberName                   pic x(15).

  Procedure Division using     lnk-Subtractor
                    returning lnk-NumberName.

  if      lnk-Subtractor = zeroes
          compute Kounter-2 = Kounter-1

  else    compute Kounter-2 = Kounter-1 - 1
  end-if

  *> Initialize the three fields :
  move Tilde       to Descrip-1, Descrip-2
  move HyphenTilde to Separator

  if    K-Tens <> zeroes
        set Tens-Idx to K-Tens
  end-if

  Evaluate true

      when Kounter-2 = zeroes
      when Kounter-2 = 1
           move Tilde to Separator

      when Kounter-2 < 20
           set  Digits-Idx to Kounter-2
           Move Tilde to Descrip-1, Separator
           move Digits (Digits-Idx) to Descrip-2

      when other
           move Tens (Tens-idx) to Descrip-1

           if   K-Digits <> zero
                set Digits-Idx to K-Digits
                move Digits (Digits-Idx) to Descrip-2

           else move Tilde to Separator, Descrip-2
           end-if
  End-Evaluate

  String Descrip-1 delimited by Tilde
         Separator delimited by Tilde
         Descrip-2 delimited by Tilde
         Tilde
         into lnk-NumberName
  end-string

  End Method "GetNumberName".
  *>---------------------------------------------------------------
  END FACTORY.
  *>---------------------------------------------------------------
  *>OBJECT.           OBJECT/iNSTANCE not used with Abstract/
  *>END OBJECT.       Singleton classes
  *>--------------------------------------------------------------

  END CLASS BottleCount.
  *>---------------------------------------------------------------
```

#### ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** Kulin Remailer <remailer@reece.net.au>
- **Date:** 2010-11-08T01:26:25
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8K215H5F40490.3933449074@reece.net.au>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad>`

```
No offense to the author, but the code shown is why I got out of the COBOL
business 2 1/2 years ago. Life is just too damn short to look at such
butt-ugly, convoluted, morally-offensive code. Leave the "structured",
lower-cased, wannabe-c-programmer code on UNIX! Now I own a coffee shop and
I make more money and sleep better. Have a nice day, PLONK!
```

##### ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2010-11-08T10:31:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ib955t$ogd$1@news.eternal-september.org>`
- **In-Reply-To:** `<8K215H5F40490.3933449074@reece.net.au>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <8K215H5F40490.3933449074@reece.net.au>`

```
On 11/7/2010 8:26 PM, Kulin Remailer wrote:
> No offense to the author, but the code shown is why I got out of the COBOL
> business 2 1/2 years ago. Life is just too damn short to look at such
…[3 more quoted lines elided]…
>

Yet you still read this ng...
You *want* to write COBOL - you do. You know you do.
You are still assimilated - admit it!
```

#### ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** Fritz Wuehler <fritz@spamexpire-201011.rodent.frell.theremailer.net>
- **Date:** 2010-11-08T17:47:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2b89b487abb838af1f3b364d65e7cacf@msgid.frell.theremailer.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad>`

```
James Gavan <jgavan@shaw.ca> wrote:

Haha reminds me of the movie "Say Anything"

What a load of rubbish! Object-oriented COBOL? You guys have some serious
problems! Just use C++ if you need it so badly. Otherwise, be a man!
```

##### ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-11-08T10:39:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1dgd6p4gtiqkvrbtetddoemirbj21mrom@4ax.com>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <2b89b487abb838af1f3b364d65e7cacf@msgid.frell.theremailer.net>`

```
On Mon, 08 Nov 2010 17:47:46 +0100, Fritz Wuehler
<fritz@spamexpire-201011.rodent.frell.theremailer.net> wrote:

>James Gavan <jgavan@shaw.ca> wrote:
>
…[3 more quoted lines elided]…
>problems! Just use C++ if you need it so badly. Otherwise, be a man!

That code was an exercise (you don't think beer inventory was a
business application??).   Playing around like that can improve our
understanding of OO CoBOL.   

The normal situation for writing OO-CoBOL isn't with new applications
- especially relatively simple new applications.   OO-CoBOL is most
often used to convert existing CoBOL to work in an OO environment.
Practicing one's OO-CoBOL skills can assist in evaluating the costs
and benefits of converting CoBOL vs replacing it.
```

###### ↳ ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-09T13:21:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jrih8Fct8U1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <2b89b487abb838af1f3b364d65e7cacf@msgid.frell.theremailer.net> <j1dgd6p4gtiqkvrbtetddoemirbj21mrom@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 08 Nov 2010 17:47:46 +0100, Fritz Wuehler
> <fritz@spamexpire-201011.rodent.frell.theremailer.net> wrote:
…[17 more quoted lines elided]…
> and benefits of converting CoBOL vs replacing it.

An excellent post, Howard.

(As usual, the voice of Reason... :-))

I believe there IS a place for OO COBOL and it is very much along the lines 
you mention, but I am starting to question even that...

See new thread "Is OO COBOL relevant..."

Pete.
```

#### ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-09T12:57:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jrh3iF5rnU1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad>`

```
TOP POST - nothing more below.

Thanks for posting this, Jimmy.

I like the recursive COBOL method and think it is a good approach.

Overall, the code looks a bit intimidating and I'm not sure that some of the 
repeated WHERE tests couldn't be avoided.

It seems to me there are COPYed members that are not included, but as I 
don't have a Micro Focus environment I couldn't try compiling the code.

You will have seen some of the comments this has evinced.

I think those concerns are worth addressing, so have started another thread 
about the relevance of OO COBOL.

Cheers,

Pete.
James Gavan wrote:
> Well I'm there about 99.9%. What really bugged me and held me up was
> to do the following. Bearing in mind Alistair's observation
…[536 more quoted lines elided]…
>  *>---------------------------------------------------------------
```

##### ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-08T18:08:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a1Co.13274$Ou2.8312@newsfe20.iad>`
- **In-Reply-To:** `<8jrh3iF5rnU1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <8jrh3iF5rnU1@mid.individual.net>`

```
On 11/8/2010 4:57 PM, Pete Dashwood wrote:
> TOP POST - nothing more below.
>
…[10 more quoted lines elided]…
> You will have seen some of the comments this has evinced.

Yes, the first from our friend in Oz; the "Author' wasn't offended and 
in fact had a bloody good laugh. The only words of advice I can give to 
him are, "Stick with Java, cobber and go throw another 'roo on the barbie'".
>
> I think those concerns are worth addressing, so have started another thread
…[4 more quoted lines elided]…
> Pete.

Agreed, it does seem like there are lots of EVALUATEs - which might 
appear unnecessary. But as Howard observed, it *IS* a tutorial approach, 
so although some might suggest you don't need the Decision Tables to 
show what's going on, anybody thinking of taking advantage can adjust 
the code to what they want it to be. Richard once mentioned you could go 
from Decision Tables to generating the checking code - care to give me a 
suggestion Richard to improve on what I've shown ?

Pete,  one observation on the code you wrote - in your program, which 
admittedly was a quick revamp of the effort from Bruce; you used 'String 
with Spaces'. OK, so some joker says, now extend the puzzle starting at 
200 and working you way down. Now we are back to 'South Pacific' - 
what's the easy way to handle the song :-

"One hundred and one pounds of fun, That's my little Honey Bun...." - 
the Tilde can be a very useful separator/joiner.

I was hoping you at least would have a copy of Net Express - doesn't 
matter if it is an old one; I think my code will fit.

The complete code I will be packaging will have copyfiles included, with 
the exception of the following, which I'm guessing I shouldn't 
distribute - copy files from Micro Focus. These are things like :-

p2cevent.cpy - GUI events - primarily Level 88s or Level 78s and Hex 
values for events etc. Accepting that they are there, you don't have the 
complete story, but I think something like 98% will be understood.
And if you do have a copy of Net Express these copyfiles are 
automatically added to your project as soon as you include them in one 
single source program.

Similarly I have heavily commented the features I have used - such as 
Collections, Callbacks - the first some will be familiar with, but I'm 
guessing Callbacks might be a bummer to some.

Here's a conundrum - where others may wish to join in. My MS Word 
document describing intent, included source and copyfiles, flowchart and 
4 sceenshots, etc... is all but done.

I've been debating which font. The very, very rare occasion I've used 
Word to send a private letter, my preference has been Times New Roman.
Anybody making suggestions bear in mind - people like Bill Klein have 
sight disabilities, so anything chosen has to be a compromise as to what 
is an easy read for most, but also takes into account people like Bill.

I like Times New Roman, but I think it's a bit too stylish for 
documentation. Perhaps one of the Arials with point 12 or 14 for text, 
and 16 for Para-Headers and I also think it should be BOLD for 
readability. Any takers ?

Another query with MS WORD - I went through my already written text, 
changing fonts and their properties to get a visual impression. Strange 
thing is I found that having made some changes, there was too much 
"depth" between lines. Suppose I initially set up a paragraph as Point 
14, if then doing a 'block replacement' by highlighting - changing to 
Point 12 - the result is I still see the same depth for Point 14. Is 
there some Word limitation, that once you have written something, you 
have to delete it if you have played around using the Point feature, and 
have to rewrite that text ?

Jimmy

Here's the one you are after from BottleCount :-

*>--------------------BottlesChoice.cpy--------------------------
01 BottlesChoice                pic x(4) comp-5.
    88 DisplayOnScreen           value 1.
    88 WriteFile-Notepad         value 2.
    88 WriteFile-MsWord          value 3.
    88 ShowGUIListbox            value 4.
    88 ValidBottlesChoice        value 1 thru 4.
*>---------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-09T15:04:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jrohgFaaeU1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <8jrh3iF5rnU1@mid.individual.net> <4a1Co.13274$Ou2.8312@newsfe20.iad>`

```
James Gavan wrote:
> On 11/8/2010 4:57 PM, Pete Dashwood wrote:
>> TOP POST - nothing more below.
…[40 more quoted lines elided]…
> the Tilde can be a very useful separator/joiner.

Yes, sometimes using a separator is a very good approach. In my own defence, 
I didn't (couldn't) spend a large amount of time on the code and dare I say 
my COBOL is getting rusty... :-)?

My main priroty in posting it was to remove those horrible DISPLAYs; I 
wasn't too concerned about future requirements.

>
> I was hoping you at least would have a copy of Net Express - doesn't
> matter if it is an old one; I think my code will fit.

The brutal truth is as follows:

1. I'm not really interested in COBOL and COBOL experiments to the extent 
that I once was. (Fujitsu is used by a number of my clients so I stay 
up-to-date on that, but I simply don't have the energy or enthusiasm to 
spare to get to grips with a different environment that can never generate 
revenue for me. (Fujitsu runtimes are free; If I write stuff in it, I can 
sell it. That is about as far as my COBOL interest goes, these days. The 
exception would be where we see a problem or just lack of COBOL experience 
leading to ugly code. In that case I would be tempted to post an 
alternative.) Therefore I don't use Micro Focus and am unlikely to. Now, if 
a Micro Focus Client was considering migration and offered me money to make 
the Migration Toolset support it... :-)

2. The above is not intended as any form of criticism of Micro Focus who are 
an excellent company providing excellent products.

>
> The complete code I will be packaging will have copyfiles included,
…[16 more quoted lines elided]…
> and 4 sceenshots, etc... is all but done.

I noted (and was surprised) you said you had problems using the OLE 
Automation server and reverted to the API instead. It should be a simple 
matter of instancing an Object of the server class and invoking the methods 
and properties available. Certainly, very straightforward in Fujitsu COBOL. 
The problem is not usually with the "mechanics" (which are simple and 
well-estabilished with sample code all over the web), but rather with 
knowing WHICH methods/properties/interfaces/events to activate... An object 
browser resolves this pretty quickly and there is one provided with Office 
for VBA code. I seem to recall covering this before so won't go through it 
all again, but you basically open Word (or whatever Office Automation 
product) and go into the provided VBA (Visual Basic for Applications) 
development environment. It shows all the stuff available, with prototypes 
and method signatures... pretty simple really.  (Hey, if VB guys can do it, 
how hard can it be :-)?)

>
> I've been debating which font. The very, very rare occasion I've used
…[4 more quoted lines elided]…
> Bill.

TNR is a seraphed (serifed) font. These days people are becoming more 
accustomed to UNseraphed fonts (like Calibri) which were designed to reduce 
eyestrain when reading screens
>
> I like Times New Roman, but I think it's a bit too stylish for
> documentation. Perhaps one of the Arials with point 12 or 14 for text,
> and 16 for Para-Headers and I also think it should be BOLD for
> readability. Any takers ?

Selecting a font involves setting the right property. Standard OOP.
>
> Another query with MS WORD - I went through my already written text,
…[5 more quoted lines elided]…
> 14.

This is a "brute force" approach. Try applying a style or theme to the 
document, then experiment with changing that. You can make temporary, 
permanent, global, or local, changes to the style. If you replace the style, 
it is reflected through the whole document, pretty cool... Try "Modern" it 
is one of my favourites :-)



>Is
> there some Word limitation, that once you have written something, you
> have to delete it if you have played around using the Point feature,
> and have to rewrite that text ?

In effect, you are locally overriding the default style. That is why it 
seems that way. There's more here than COBOL programming...

>
> Jimmy
…[10 more quoted lines elided]…
> *>---------------------------------------------------------------

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

_(reply depth: 4)_

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-09T17:01:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mhlCo.8037$8m.991@newsfe09.iad>`
- **In-Reply-To:** `<8jrohgFaaeU1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <8jrh3iF5rnU1@mid.individual.net> <4a1Co.13274$Ou2.8312@newsfe20.iad> <8jrohgFaaeU1@mid.individual.net>`

```
On 11/8/2010 7:04 PM, Pete Dashwood wrote:
> James Gavan wrote:
>> On 11/8/2010 4:57 PM, Pete Dashwood wrote:
…[4 more quoted lines elided]…
>>> I like the recursive COBOL method and think it is a good approach.

To be perfectly truthful I've only ever used a recursive method ONCE 
before. Background on that was the old (deceased corrosion testing 
system). Not unusual for Klaus (died in March) to whistle between two 
oil/gas plants in the same area, because of an urgent request by the 
local manager. So that tended to throw him when he got back to Plant A 
from Plant B. "Which was the last Vessel I was working on, and which 
particular item ( = pipe) ?". "Be nice if you could give me some sort of 
reminder".

So I hit on the idea of using a Treeview of the Plant : Level 0 - Plant,
Level 2 - Vessel, Level 3 - Item etc... To simplify the testing I used a 
Treeview of Cheeses : Level 0 - Cheeses, Level 1 - Continent, Level 2 - 
Country, Level 3 - the actual cheese names. Each element in the Treeview 
had an icon, (could just as easily have been a checkbox). Starting out 
from scratch (a particular Inspection Date in corrosion) all icons were 
Red (unactioned). As you change something for a Cheese it was necessary 
to change the icon colour to Green. That required an override method to 
the normal GUI reaction. (My first intro to overriding and provided for 
me by David Sands of Micro Focus - absolutely dead easy when you have an 
example).

The logic was Cheeses - change to Green individually but you could only 
change the Country icon when all cheeses for that country showed Green. 
Similarly you could only change the Continent icon to Green when all 
countries in that group were Green. And finally the Root Level is only 
Green when all subordinates show Green.

I think that particular problem did lend itself nicely to a recursive 
method. (Well I suppose I could have written perform until 
NoMoreToBeActioned). To be frank for Bottles of Beer, I consider the 
recursive method to be a bit gimmicky, (the technique is just used, 
'because it is available'). Could just as easily have been a PERFORM the 
Decrement method varying count from 99 until count = zero. Regardless of 
which OO COBOL compiler we are talking about - I'm sure their mechanisms 
are fairly close for this. Either PERFORM or doing the RECURSIVE 'call' 
- the method we are 'exiting' is still in memory and I'd bet each 
compiler checks if it is wanted again before 'throwing the method away'. 
As they all probably have some cache technique for current methods, it's 
unlikely it wont be available immediately for re-use.

>>>
>>> Overall, the code looks a bit intimidating and I'm not sure that
>>> some of the repeated WHERE tests couldn't be avoided.

Well for the uninitiated - I will be adding the following at the start 
of each source :-

*>---------------------------------------------------------------
*> OO COBOL - Micro Focus Net Express V3.1 and Windows XP -
*>
*> Author : jgavan@shaw.ca     Date Revised : 2010 Nov 03
*>
*> The DIRECTIVE above :- $set ooctrl(-w)
*>
*> allows N/E V 3.1 to use 'Working-Storage' within methods
*>
*> "Ignore red tape" - Method format.
*>
*> From the directive above, the heading "Working-Storage Section"
*> is assumed within methods, by the compiler. Local-Storage
*> Section is superfluous.
*>
*> The only time you require 'Procedure Division......' in a
*> method is when it is associated with a Linkage-Section where
*> the syntax then reads as one of the three options:-
*>
*>      Procedure Division using xxxxx
*>      Procedure Division returning yyyyy
*>      Procedure Division using xxxxx returning yyyyy
*>
*>---------------------------------------------------------------


> I noted (and was surprised) you said you had problems using the OLE
> Automation server and reverted to the API instead. It should be a simple
…[11 more quoted lines elided]…
> how hard can it be :-)?)

As regards MS Word I could spend many unproductive hours messing around 
with it - holding me up releasing the code for 99-Bottles - so I'll take 
another look later. Meanwhile I'll go with the MyCreateP (API Create 
Process) which automatically opens Notepad or Word and close them as 
they see fit.

Whether or not it has always been the case, but one of the senior people 
from Bill's generation wrote a white paper where one suggestion was 
finalize the object for MsWord, (i.e. disconnect COBOL from the OLE) and 
leave Word there just hanging. Don't like the idea, but it implies the 
OLE routines are not clear cut. (Just google on Create Process, 
Terminate Process associated with APIs and Word/Excel - see all the crap 
you get !). And that's one of the major bitches I have with MS ! They 
have reams of articles/KBs on similar/parallel topics. Somebody needs to 
sit down and revamp their library. I'm not referring to COBOLERs only - 
people in EVERY language have the same problems with MS.

Take the following. Somebody in the M/F Forum asked, "Can I enlarge the 
Open Dialog ?". I know what he was after - increase the dimensions and 
he can view more files. I got back to him saying I hadn't found that 
that could be done. As I was into the Common Dialogs project at the time 
I gave it a try. I changed the x, y co-ordinates from their default to a 
value of say 12 - yes it displayed moved down and across the parent 
window the 12 value, but totally ignored my values for width) and 
h(eight). Well that concluded it can't be done.

Quite by accident, going through the above crap I came across a KB 
Article. "You can't change w or h in Windows XP - but if you have 
Windows Vista, 7 etc... voila !"  Doesn't it make sense to consolidate 
into one article with a proviso about exceptions per version of the OS ? 
The hours you can waste on this. (Don't tell me about your one-liner 
methods in .Net - I'm still using XP).

(As an after-thought, but it is re-inventing the wheel, you could design 
your own version of Open Dialog, (using a SortedCollection) with a 
scrolled list of files. You could be more expansive showing the file 
extension and even Date I would suggest).

To be fair - and I can't recall exactly what I was looking at, but 
dealing with Common Dialog - Open Files, I came across an example in 
BASIC (not using the VB wizard routines - which are only useful if you 
are using VB), and I think it was associated with .Net, spelling out how 
you could customize the Open File Dialog; couldn't have been any more 
clear if they tried ! I'm referring to the Droplist of file types you 
can open. When testing, I got frustrated when a set sequence popped up, 
say the first line was *.txt which I would use for Notepad; had to 
scroll down to get *.doc for Word. To hell with it - from the Driver for 
my project Common Dialogs I allow you to select from a menu - use Open 
Dialog (a) for *.txt and (b) for *.doc and just re-arrange (a) or (b) as 
the first line in the OrderedCollection displayed in the Open File 
Dialog.

Jimmy
```

###### ↳ ↳ ↳ Re: Phase 1 - OO Rosetta Bottles of Beer

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-11T15:09:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k11hsFo76U1@mid.individual.net>`
- **References:** `<FeDBo.18820$3f.1700@newsfe12.iad> <8jrh3iF5rnU1@mid.individual.net> <4a1Co.13274$Ou2.8312@newsfe20.iad> <8jrohgFaaeU1@mid.individual.net> <mhlCo.8037$8m.991@newsfe09.iad>`

```
James Gavan wrote:
> On 11/8/2010 7:04 PM, Pete Dashwood wrote:
>> James Gavan wrote:
…[46 more quoted lines elided]…
> immediately for re-use.

I think it comes down to patterns (as noted by Charlie).

The recursive pattern is applicable to this and, while it isn't the ONLY 
way, it is a good way.
>
>>>>
…[52 more quoted lines elided]…
> close them as they see fit.

Nothing wrong with that, but you may not get the same level of control that 
is provided by manipulating the properties and interfaces directly.

Next time I'm looking for something to occupy my time, I'll post some more 
full examples of dealing with Office from COBOL, but it won't be soon... 
(pretty busy at the moment)
>
> Whether or not it has always been the case, but one of the senior
…[5 more quoted lines elided]…
> - see all the crap you get !).

That is one reason why "one" :-) might find using the provided Class, where 
everything can be invoked in a standard way, advantageous. :-)


> And that's one of the major bitches I
> have with MS ! They have reams of articles/KBs on similar/parallel
> topics. Somebody needs to sit down and revamp their library. I'm not
> referring to COBOLERs only - people in EVERY language have the same
> problems with MS.

The first time I came to grips with this (it was nearly 20 years ago) I 
couldn't find anything in the way of COBOL examples and had to struggle 
through VB samples, translating them as I went. I wasn't as familair then 
with VB as I am today and it was painful.

I think the problem with the libraries and even the KB sometimes, it that 
they are maintaining a huge amount of stuff that is only there for 
historical reference. I went to the Knowledge Base yesterday to find out 
something, spent about 45 minutes reading and absorbing a bunch of stuff, 
then found at the bottom a note saying that since 2008 things no longer work 
that way and it is deprecated. :-)

Served me right, and I learned from it.
>
> Take the following. Somebody in the M/F Forum asked, "Can I enlarge
…[33 more quoted lines elided]…
>
That sounds OK. I use different instances of the dialogue with different 
filters where it makes sense to do that. They retain their own attached 
collection.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
