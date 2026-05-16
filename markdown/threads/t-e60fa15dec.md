[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SEQMENTATION

_28 messages · 11 participants · 2002-03_

---

### SEQMENTATION

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-16T22:20:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net>`

```
Eddy, Jerry tells it like it is. I just waxed a little detail in there for
personal
mind dumping. Segmentation was hard to get into COBOL. However,
after some vendors began building computers with easy segmentation the
votes came around.

Warren Simmons

From: JerryMouse <nospam@invalid.com>
Subject: Re: Sections
Date: Saturday, March 16, 2002 7:39 AM


"Eddy Scheire" <fa099784@skynet.be> wrote in message
news:3c931758$0$29682$ba620e4c@news.skynet.be...
> Hi,
>
…[25 more quoted lines elided]…
> I mean why should one use sections? To me it looks like unnecessary code.

SECTIONS are an artifact, a fossil, a construct from a primative time.

Their major original function was to partition the code into overlayable
chunks to conserve memory. SECTIONS today permit no unique (or even useful)
purpose. Their presence does, however, tend to confuse or bewilder those who
have never encountered them - or those, like me, who haven't seen SECTIONS
in twenty years.

Check out LEVEL numbers for SECTIONS for more confusion:

   (PRINT-IT SECTION 73.).
```

#### ↳ Re: SEQMENTATION

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-19T01:34:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VAwl8.32020$Es6.811372@news2.west.cox.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net>`

```

"398199821" <warren.simmons@worldnet.att.net> wrote in message
news:DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net...
> Eddy, Jerry tells it like it is. I just waxed a little detail in there for
> personal
…[40 more quoted lines elided]…
> > I mean why should one use sections? To me it looks like unnecessary
code.
>
> SECTIONS are an artifact, a fossil, a construct from a primative time.
>
> Their major original function was to partition the code into overlayable
> chunks to conserve memory. SECTIONS today permit no unique (or even
useful)
> purpose. Their presence does, however, tend to confuse or bewilder those
who
> have never encountered them - or those, like me, who haven't seen SECTIONS
> in twenty years.
…[6 more quoted lines elided]…
>

Q. How do you write STRUCTURED CODE, without using sections, or the highly
fallible Perform of paragrpah ranges.

>
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-18T21:02:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a769nr$6i6$1@slb7.atl.mindspring.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
"Rufio" <davecawdell@cox.net> wrote in message
news:VAwl8.32020$Es6.811372@news2.west.cox.net...
>
 <snip>
> Q. How do you write STRUCTURED CODE, without using sections, or the highly
> fallible Perform of paragrpah ranges.
>

Rufio,
 Are you serious?

You can write an ABSOLUTELY structured program with JUST paragraphs, no
PERFORM x THRU y, no fall thru, whatever.  I don't understand what you think
the problem is.  The basic structure is something like:

Procedure Division.
 Mainline.
    Perform HouseKeeping
    Perform MyLoop
       Until EOF-status
    Perform WindUp
    Stop Run
       .
  HouseKeeping.
     Initialize Whatever
     Open Input A
              Output B
      .
  MyLoop.
    Read A
       At End
          Set EOF-Status to True
          Perform Last-Record-Logic
       Not At End
          Perform
             Do something
             If Error-Cond
                 Set BadRecord to True
             End-If
             If GoodRecord
               Do somethin else
             End-If
         End-Perform
    End-Read
    Perform With-or-Without-Read
       .
  WindUp.
      Perform
           Any after all other processing goes here
      End-Perform
      Close A B
        .
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-22T00:26:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hTum8.42567$Es6.1384996@news2.west.cox.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <a769nr$6i6$1@slb7.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:a769nr$6i6$1@slb7.atl.mindspring.net...
> "Rufio" <davecawdell@cox.net> wrote in message
> news:VAwl8.32020$Es6.811372@news2.west.cox.net...
> >
>  <snip>
> > Q. How do you write STRUCTURED CODE, without using sections, or the
highly
> > fallible Perform of paragrpah ranges.
> >
…[5 more quoted lines elided]…
> PERFORM x THRU y, no fall thru, whatever.  I don't understand what you
think
> the problem is.  The basic structure is something like:
>
…[43 more quoted lines elided]…
>

I use sections in a similar manner to the way chapters are used in novels.
If someone has written a large 5000-10000 line program, keeping paragraph
sizes down to perhaps around 10 statements, then they'll have 500-1000
paragraphs (I DON'T regard a 20+ line paragraph to be structured code) . I
use sections for clarity. My current client has 5000 line PL/1 programs with
no structure at all, just check the flag, and drop through - Oh and my lead
P/A won't allow us to add comments or blank lines, because it takes him too
long to scroll through via Telnet. (I showed him how he could just use
eXcludes etc, but he wasn't buying it).

So, when it's my team, or my project, I don't allow hundreds of paragraphs -
except when contained in sections, and I don't allow paragraphs to grow much
beyond 10 statements.

Sections seem like a bonus, and I feel it's just making life harder, not
using them. So if you want to write code structured as much as possible, in
a way that makes it easier to read, I recommend Sections - but each to his
own, so long as the client keeps paying our salaries !
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 4)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2002-03-24T08:02:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9D8826.5B5143CC@optonline.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <a769nr$6i6$1@slb7.atl.mindspring.net> <hTum8.42567$Es6.1384996@news2.west.cox.net>`

```
Rufio wrote:
> 
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
…[66 more quoted lines elided]…
> paragraphs (I DON'T regard a 20+ line paragraph to be structured code) .

That seems like an arbitrary judgment. To me a paragraph should be as
long as it needs to be, a 1,000 line paragraph can be completely
structured.

I would also recommend *not* writing 5000-10000 line programs. In
general, the bigger the program, the more difficult it is to maintain.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 5)_

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-24T15:41:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hsmn8.78930$Es6.1993372@news2.west.cox.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <a769nr$6i6$1@slb7.atl.mindspring.net> <hTum8.42567$Es6.1384996@news2.west.cox.net> <3C9D8826.5B5143CC@optonline.net>`

```

"Liam Devlin" <LiammD@optonline.net> wrote in message news:3C9D8826.5B5143CC@optonline.net...
> Rufio wrote:
> > 
…[71 more quoted lines elided]…
> structured.

OK, I ws going to let this go, but it has come up a couple of times. My opinion is that if a paragraph contains the code for a process, and needs more than ABOUT 10 lines, you may not have broken down the process FULLY. If you end up with many more lines, it may well be possible to identify separate compononents that can go in their own paragraphs. The case of the 2900-line EAVALUATE sounds different though (although it's hard to be sure, without seeing it). I would say that in that case, the DATA DEFINITIONS may need more work, to break them down further.

As for the size of program, if I found it getting too big, I would either just "go modular", or revisit the design.

 
As for how I use SECTIONS, suppose there is a need to output each records on a report, that meets a criteria. 
(Please bear in mind, I'm currently writing PL/1 after 15 years of COBOL, so I may get mixed up in langauages). 
I might have -


IF criteria
    PERFORM REPORT-PROCESS.


REPORT-PROCESS SECTION.

R1000-HEADER-CHECK.

    IF LINE-COUNT > 58
        WRITE REPORT-HEADER1 AFTER PAGE
        WRITE REPORT-HEADER2 AFTER 1
        LINE-COUNT = 3

 R1000-EXIT.
    EXIT.

R2000-POPULATE-PRINT-LINES..
    
    MOVE A TO N.
    MOVE B TO P.
    MOVE C TO Q.
    MOVE D TO R
    MOVE E TO S.

R2000-EXIT.
    EXIT

R3000-PRINT_LINES.

    WRITE REPORT-LINE1 AFTER 2.
    WRITE REPORT-LINE2 AFTER1.
    WRITE REPORT-LINE3 AFTER1.    

 R3000-EXIT.
    EXIT.

R4000-WRAP-UP.

    ADD 4 TO LINE-COUNT. 
    READ INPUT-FILE-2 INTO INPUT-BUFFER-2
    AT END OF FILE SET INPUT-FILE-2-EOF TO 'Y'.       
 
R4000-EXIT.
    EXIT.

REPORT-PROCESS-EXIT 
    EXIT.

A-N-OTHER SECTION.
.
.
.
.
.
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-19T03:52:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YByl8.292427$pN4.19157106@bin8.nnrp.aus1.giganews.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```

"Rufio" <davecawdell@cox.net>
>
> Q. How do you write STRUCTURED CODE, without using sections, or the highly
> fallible Perform of paragrpah ranges.

Uh, we've got several hundred programs and several hundred thousand lines of
COBOL with no SECTIONS or PERFORM THRU constructs. It's not hard at all once
you get the hang of it.

We even have a few programs with only one period per paragraph (that was
more for fun than the 'extremely useful' moniker bestowed by some).
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-03-19T04:30:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
On Tue, 19 Mar 2002 01:34:45 UTC, "Rufio" <davecawdell@cox.net> wrote:

snip the leadin>
> 
> Q. How do you write STRUCTURED CODE, without using sections, or the highly
> fallible Perform of paragrpah ranges.
> 

Well, you can use small programs that implement the functions required
and "call" them from your "main" program. If you want to keep 
everything in one source file, then you can use the "nested 
subprograms" that have been around since COBOL-85 if my recall has not
failed completely.

Alternatively, if you have a compiler that implements the Object 
Oriented syntax, you can write "classes" that have "methods" that 
implement the functions required. The methods are then "invoked" from 
the "main" class/program. 

The "perform" of a paragraph is equivalent to "calling" the same code 
in a subprogram or "invoking" it in a method. Both techniques have the
benefit of providing reuse of code and make the overall program easier
to understand as each small piece does only one thing. In addition, 
the use of variables is restricted to the code within the 
subprogram/method and the program does not end up with mystery bugs 
that are caused by inadvertent use of variables that affect other 
processing.

So instead of

perform init
perform process
perform ending

init section
blah blah

process section

blah blah blah

ending section

blah blah

you have

call "init" using init-variables
call  "process" using process-variables
call  "ending" using ending variables

or

invoke "init" using init-variables returning init-result
invoke "process" using process-variables returning process-result
invoke "ending" using ending-variables returning ending-result

The subprograms and/or methods are black boxes that do a particular 
thing. 
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-19T06:21:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96D86D.CC438C16@shaw.ca>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost>`

```


lsunley@mb.sympatico.ca wrote:

> On Tue, 19 Mar 2002 01:34:45 UTC, "Rufio" <davecawdell@cox.net> wrote:
>
…[59 more quoted lines elided]…
> Lorne Sunley

Agree 100%. As Bill illustrated you can do it perfectly well with just
performing paragraphs and the control logic can come from identifying paragraphs
by alpha groups, e.g. "P001-Print-It", "R001-Read-Customers", "X00-Open-Files"
etc.. ( Yes, if it's your preference use Sections - I was surprised to see that
"OO-er" Pete still uses Sections in non-OO source - nothing wrong with that, but
I broke away from them the first time I read McCracken's "Structured
Programming").

Doesn't really matter which language, but if the program logic is BIG - chop it
up into
little 'uns, so that a particular piece of "business" stands on its own as
separate source - initially helps in the development stage, running sub-programs
through the compiler for accuracy, and later with maintenance, the maintainer
knows he/she is looking at distinct parts. See note about 'splitting' below.

I was going to compare it to the approach of OO - but you've beaten me to it <G>
- Excellent comparison. From an OO perspective, you could consider Sections to
be separate classes. As an example :-

Three Tier -     (1) Edit Readings    - (2) invokes SQL DB Interface and Tables
                                                    -  (3A) invokes MyDialog

The Dialog bit is somewhat detailed for this particular program, so rather like
sectionalizing in non-OO, instead of (1) Edit Readings containing the parameters
to invoke creation of the Dialog, I have a separate sub-class (3) ReadingsDialog
containing the creation parameters, which in turn invokes (3A) MyDialog for the
actual creation. Then (3) ReadingsDialog returns the created dialog as an object
reference to (1) EditReadings.

(3) ReadingsDialog is a 'once only' and from the first Windows "show" the
interaction is between (1) EditReadings and (3A) MyDialog - (a) 1 to 3A pass
data for display, and (b) 3A to 1 for returning results of Windows events..

As an example of splitting - currently EditReadings above is a purely data entry
program. Exit to the Menu and select - Perform Calculations. It's complex enough
to be treated as a separate class. However, I will be considering doing the
calculations in the EditReadings as the user exits each item displayed. If it
appears to slow things down too much, then I'll leave it as a separate Menu
item. However, by splitting it off as a separate class I have the choice of the
above options without dramatically changing the Calculation class.

If you look at the three Tier above, I've certainly "Sectionalized"  - separate
classes for either COBOL files or DB Tables as well as the GUI handling.

If Howard is reading this he once commented that COBOL file handling "was the
easy bit". True; not for beginners, but certainly for the rest of us.. But all
the more reason to "sectionalize/segment off" into separate classes where the
reusable logic can be tested to be bullet-proof - any errors occurring will be
as a result of Business Logic programming in a Three Tier system.

(This approach to file handling - I don't know how it is with mainframes, but if
I change a copyfile used in COBOL File/SQL classes, and which is 'copied' into
recipient "Business" programs, then the IDE will trigger off re-compilation of
all sources that include the changed copyfile).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-20T01:26:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c975e90_10@Usenet.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca>`

```

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C96D86D.CC438C16@shaw.ca...
>
> Agree 100%. As Bill illustrated you can do it perfectly well with just
> performing paragraphs and the control logic can come from identifying
paragraphs
> by alpha groups, e.g. "P001-Print-It", "R001-Read-Customers",
"X00-Open-Files"
> etc.. ( Yes, if it's your preference use Sections - I was surprised to see
that
> "OO-er" Pete still uses Sections in non-OO source - nothing wrong with
that, but
> I broke away from them the first time I read McCracken's "Structured
> Programming").
>

Well, Jimmy, I don't just use sections in non-OO code. I use them in Object
and Factory Methods as well. And nothing I have read here recently has
persuaded me NOT to use them. (I think Richard has a good point with classes
of labels , but we are unlikely to see it ever implemented...) As for
McCracken...I think it was the worst book on COBOL ever written <G> Tedious,
boring and of little real use.

Better books have been written by Fritz D. McCameron (probably now out of
print but almost certainly the best book on COBOL I have ever read) and
Thane's book is probably the best introductory text I have seen. Will Price
is the man for OO...(In fact I was going to write one on OO COBOL but, after
reading Will's, I had nothing more to say..<G>).

Again, it all comes down to personal styles and I have no doubt you have
seen the discussion on this raging elsewhere in CLC...

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-20T06:46:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C982F4E.B387F969@shaw.ca>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

>
> Well, Jimmy, I don't just use sections in non-OO code. I use them in Object
…[3 more quoted lines elided]…
> McCracken...... <snip>

ZOWEEEEE ! That blew me away that you would use Sections in OO ! This is one on
which we have to agree to disagree. Like Stephen's objections to 'EXITS' this is
one where your personal style comes into play, and if it works - OK why not use
it.

While I certainly can't quote you chapter and verse, ( looking at other
languages doesn't help, while OO COBOL is too "new" to have any rules), but so
far as OO is concerned SECTIONS appears to be an unnecessary icing on the cake.
Certainly Sectionalizing is not something you find mentioned in Will's or Ed
Arranga's books, nor even in those academic OO COBOL tomes that I don't like.

The only relevant quote I can give you is from Jonathan and Victoria Pletzke. I
think we can give them some credence as they go back to the early days at Xerox
PARC :-

"Typicality Smalltalk coding creates simple methods that are approximately this
complex to slightly more complex, (** they give a couple of simple examples
before this text **) and then assembles these methods into comparably simple
methods. This results in a lot of methods generated, but the complexity of
problems, methods and solutions is reduced considerably, and similar operations
can share common sets of code. Any time a Smalltalk programmer finds that he or
she is copying code, he or she can instead create a new method that contains the
common code and can refer to it from both (or many) other methods".

I just wrote a message about varying records. Let's take the format and revamp a
method to your Section style - may not be quite the same concept you use, but
probably close :-

Bear with me, long time since I used Sections so the syntax is probably
incorrect, but you get the idea.

*>----------------------------------------------------------
Method-ID. "access-file".
*>-----------------------------------------------------------
Local-storage section.
01 ls-result                             pic x(4) comp-5.
Linkage Section.
copy "fileactn.cpy".
01 lnk-result                            pic x(4) comp-5.

Procedure Division Using     file-action
                   returning lnk-result.

FILE-ACTION SECTION.

   set file-result-ok to true
   initialize ws-Error-Data

   if   dont-initialize
        continue

   else initialize os-record(1:ws-record-size)
   End-if

   Evaluate TRUE
     When read-next         perform READ-NEXT-RECORD
     When write-record     perform WRITE-A-RECORD
     When close-file          perform CLOSE-A-FILE
     When open-input-file  perform OPEN-AN-INPUT-FILE
     When open-output-file perform OPEN-AN-OUTPUT-FILE
     When delete-file          perform DELETE-A-FILE
     when other                  perform INVALID-ACTION
   End-evaluate

   if file-status <> "00"
      perform ERROR-MESSAGE

   else move file-status to lnk-result
   End-if

   GO TO SECTION-EXIT.
*> (could be GO TO EXIT METHOD)

READ-NEXT-RECORD.

   Read Data-File next record
     At End
       Set file-finis to True
     Not at End
       Move Data-record  (1:ws-record-size)
            to os-record (1:ws-record-size)
   End-Read.

WRITE-A-RECORD.

   Move os-record     (1:ws-record-size)
        to Data-record(1:ws-record-size)
   Write Data-record.

CLOSE-A-FILE.

   Close Data-File.

OPEN-AN-INPUT-FILE.

   Open input Data-File.

OPEN-AN-OUTPUT-FILE.

   Open output Data-file.

DELETE-A-FILE.

     When delete-file
          call "CBL_DELETE_FILE" using     Data-Filename
                                 returning ls-result
           move "00" to ws-filestatus

INVALID-ACTION.

      invoke super "invalid-action" using file-action
      set file-error to true.

ERROR-MESSAGE.

   if      ws-filestatus <> "00"
           move os-record(1:10)  to ws-error-key
           move os-record(11:40) to ws-error-name
           invoke super "check-file-status"
                  using     ws-ErrorFields
                            file-action
                            ws-file-result
                  returning lnk-result
   End-if.

SECTION-EXIT.
        EXIT.

End Method "access-file".
*>--------------------------------------------------------------

While a rough definition of a method is that it is "a mini-program", the above
in fact is a "multi mini-program". In the example I've given, it firstly
necessitates an action flag for file accessing then invoking this one method
from Business Logic.

Without sectionalizing, OO already accommodates different action layers.
Partially rewriting some of the above, the Business Logic can address specific
methods DIRECTLY :-

*>----------------------------------------------------------
Method-ID. "openInputFile".
*>-----------------------------------------------------------
Linkage Section.
copy "fileresult.cpy" replacing ==(tag)== by ==01 lnk==.
Procedure Division returning lnk-result.

set ResultOK to true
open input file

If file-status <> "00"
   set FileError to true
   invoke self "fileError"
End-if

End Method "openInputFile".
*>----------------------------------------------------------
Method-ID. "readNext".
*>-----------------------------------------------------------
Linkage Section.
01  lnk-ReturnValues.
     copy "fileresult.cpy" replacing ==(tag)== by ==05 lnk==.
     05 lnk-record.
      10 occurs 1 to 1530
         depending on ws-record-size  pic x(01).

Procedure Division returning lnk-ReturnValues.

   set ResultOK to true
  Read Data-File next record
     At End
       Set fileFinis to True
     Not at End
       Move Data-record  to lnk-record
   End-Read.

    if file-status = "00" or "10"
       continue
   else set FileError to true
         invoke self "fileError"
End-if

End Method "readNext".
*>----------------------------------------------------------

Note that the two methods while separate, are simpler, and only contain what is
pertinent to them and obviate the necessity of the os-record to move IN or OUT,
depending upon the method. The "openInput" is only concerned with getting a
file-status of "00" whereas the "readNext" has code to cover, OK, EOF or
FileError.

As you wrote above, "And nothing I have read here recently has persuaded me NOT
to use them.", so we can be damn sure you aren't going to be influenced by
anything I write - we agree to disagree <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-21T12:13:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c99271a_6@Usenet.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com> <3C982F4E.B387F969@shaw.ca>`

```
OK, I really don't have time for this at the moment... I have to deliver a
Web Based Reservation system to Melbourne by next Wednesday and I'm still
writing parts of it  (using SECTIONED code...<G>), but, seeing you took the
trouble to post code, and seeing it's you...

Here is my version of your Method:

(In practice, I would not do it this way in an OO system, but this will
serve as an example of sectioned code.)

 *>----------------------------------------------------------
 Method-ID. "access-file".
 *>-----------------------------------------------------------
 Local-storage section.
 01 ls-result                             pic x(4) comp-5.
 Linkage Section.
 copy "fileactn.cpy".
 01 lnk-result                            pic x(4) comp-5.

 Procedure Division Using     file-action
                    returning lnk-result.

Main section.
*
*  This is the controlling section which decides exactly what part of the
Method is being
*  activated.
*
* (In an OO system, the SECTIONS below could (should?) be split out to
different methods.
* Sectioning them actually facilitates this by clearly showing the
boundaries of each function.)
*
a000.
    set file-result-ok to true
    initialize ws-Error-Data

    if   initializing
         initialize os-record(1:ws-record-size)
    End-if

    Evaluate TRUE
      When read-next         perform READ-NEXT-RECORD
      When write-record     perform WRITE-A-RECORD
      When close-file          perform CLOSE-A-FILE
      When open-input-file  perform OPEN-AN-INPUT-FILE
      When open-output-file perform OPEN-AN-OUTPUT-FILE
      When delete-file          perform DELETE-A-FILE
      when other                  perform INVALID-ACTION
    End-evaluate

    if file-status <> "00"
       perform ERROR-MESSAGE
    else
       move "00" to lnk-result
    End-if
    .
a999.
    exit method.
*>-------------------------------------------------------
 READ-NEXT    section.
*
* This section handles the receipt of a READ NEXT action.
*
*( this could easily be another Method. As could any or all of the SECTIONS
below.)
*
rn000.
      Read Data-File next record
      At End
        Set file-finis to True
      Not at End
        Move Data-record  (1:ws-record-size)
             to os-record (1:ws-record-size)
    End-Read
    .
rn999.
   exit.
*>-------------------------------------------------------
 WRITE-a-record   Section.
*
* The logical record is written. The size will have been set so this is a
general solution
* to write records of any size.
*
war000.
     Move os-record     (1:ws-record-size)
         to Data-record(1:ws-record-size)
    Write Data-record
     .
war999.
    exit.
*---------------------------------------------------
 CLOSE-a-file section.
*
*  Close the active file.
*
caf000.

   Close Data-File
   .
caf999.
   exit.
*-----------------------------------------------------
<snipped as too trivial to waste time on...<G> >
...

 INVALID-ACTION     section.
*
* We have been given a bum steer...handle it and get out.
*
ia000.

       invoke super "invalid-action" using file-action
       set file-error to true
       .
ia999.
       exit.
*-----------------------------------------------------------
 ERROR-MESSAGE        section.
*
* Notify User we have a problem...
*
em000.
    if      ws-filestatus <> "00"
            move os-record(1:10)  to ws-error-key
            move os-record(11:40) to ws-error-name
           invoke super "check-file-status"
                   using     ws-ErrorFields
                             file-action
                            ws-file-result
                  returning lnk-result
   End-if
   .
em999.
   exit.
*--------------------------------------------------------------
 End Method "access-file".
 *>------------------------------------------------------------

Few points to note...

1. I sometimes use meaningful paragraph names (especially if they are being
referenced from within the section). I didn't here because it is a trivial
example and all I wanted to do was demonstrate the use of sections. I agree
that the code can be written just as well without them, and I would have no
problem maintaining either your version or my version. (But then, I would
have no problem maintaining anyone else's version either...I'm a
programmer...<G>)

2. I ALWAYS place a comment at the head of a section. And I ALWAYS have an
underline at the end of one. This is mainly to facilitate cutting and
pasting if I want the code in another program (just that bit of it...
obviously, I would invoke or override the Method if I wanted more of it...)
Case in point... I am doing some server side CGI programming at the moment
and I needed a component I use to validate input data. For reasons I won't
gointo here, it was not possible to deploy this component on the server, so
I simply lifted the source code and pasted it into the CGI code. Because it
was sectioned and clearly identified, this was the work of a minute or two.
Had it been paragraphed I would have spent quite some time deciding the
range of paragraphs I required, pasting them, then checking the logic flow,
and so on.

Again, I don't say that either approach is wrong. I just use what works for
me. (And, while I am impressed with the extensive reading you have done
which led you to change your coding style (good for you!), the "argument
from authority" cuts no ice with me. I have seen "Authorities" get it wrong
so often (and many of them live in Acadaemia, far removed from the real
world of actually writing code that has to work in commercial environments),
that these days I check out everything, no matter who says it is a good
idea. The principle is that it doesn't matter WHO's right; it is WHAT's
right that matters...)

some final comments below...

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C982F4E.B387F969@shaw.ca...
>
>
…[3 more quoted lines elided]…
> > Well, Jimmy, I don't just use sections in non-OO code. I use them in
Object
> > and Factory Methods as well. And nothing I have read here recently has
> > persuaded me NOT to use them. (I think Richard has a good point with
classes
> > of labels , but we are unlikely to see it ever implemented...) As for
> > McCracken...... <snip>
>
> ZOWEEEEE ! That blew me away that you would use Sections in OO ! This is
one on
> which we have to agree to disagree. Like Stephen's objections to 'EXITS'
this is
> one where your personal style comes into play, and if it works - OK why
not use
> it.
>

Dare I suggest that you are easily blown...<G>?

> While I certainly can't quote you chapter and verse, ( looking at other
> languages doesn't help, while OO COBOL is too "new" to have any rules),
but so
> far as OO is concerned SECTIONS appears to be an unnecessary icing on the
cake.

Very possibly. But I like icing....

> Certainly Sectionalizing is not something you find mentioned in Will's or
Ed
> Arranga's books, nor even in those academic OO COBOL tomes that I don't
like.
>

Everyone has their own style. I rate Will's book very highly. I didn't stop
reading it because he doesn't use the style of coding I use...

> The only relevant quote I can give you is from Jonathan and Victoria
Pletzke. I
> think we can give them some credence as they go back to the early days at
Xerox
> PARC :-
>
> "Typicality Smalltalk coding creates simple methods that are approximately
this
> complex to slightly more complex, (** they give a couple of simple
examples
> before this text **) and then assembles these methods into comparably
simple
> methods. This results in a lot of methods generated, but the complexity of
> problems, methods and solutions is reduced considerably, and similar
operations
> can share common sets of code. Any time a Smalltalk programmer finds that
he or
> she is copying code, he or she can instead create a new method that
contains the
> common code and can refer to it from both (or many) other methods".
>

I fail to see the relevance of the above. It is certainly true, but you can
implement it with or without Sectioned code.

> I just wrote a message about varying records. Let's take the format and
revamp a
> method to your Section style - may not be quite the same concept you use,
but
> probably close :-
>
> Bear with me, long time since I used Sections so the syntax is probably
> incorrect, but you get the idea.
>
Your use of sections is NOT the same as my use of sections. A section header
requires a paragraph to follow it (at least it does in my book; I don't care
what the compiler lets you get away with....<G>) because this is the innate
structure of a COBOL program....Division>Section> PARAGRAPH> statements. It
makes sense and has served me well for over 30 years now. Although I accept
there are arguments for and against, I see no COMPELLING reason to change.

<snipped code sample>
>
> While a rough definition of a method is that it is "a mini-program", the
above
> in fact is a "multi mini-program". In the example I've given, it firstly
> necessitates an action flag for file accessing then invoking this one
method
> from Business Logic.
>
> Without sectionalizing, OO already accommodates different action layers.
> Partially rewriting some of the above, the Business Logic can address
specific
> methods DIRECTLY :-
>
Yes it can. And it can with my code too...

<snipped>

>
> As you wrote above, "And nothing I have read here recently has persuaded
me NOT
> to use them.", so we can be damn sure you aren't going to be influenced by
> anything I write - we agree to disagree <G>
>
there is a difference between being "influenced" and actually "agreeing
with". To some degree, I am influenced by all the arguments I read in this
forum. I certainly weigh and evaluate them. In this instance I don't agree
or disagree. There is nothng to argue about, unless you are saying that the
results above CANNOT be achieved if sections are used. In which case I say,
"Look again".

This whole religious thing is ridiculous. It is COBOL code. It has no
bearing on the Spiritual well-being of the Planet.

I refuse to agree or disagree on sections. People should use whatever they
feel comfortable with. I use sections. I don't care what anyone else uses
(I'll still fix their code if I need to... that's what I do; I'm a
"programmer".)

Pete




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-21T05:20:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C996CE9.EEA0333@shaw.ca>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com> <3C982F4E.B387F969@shaw.ca> <3c99271a_6@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

>
> Here is my version of your Method:
…[3 more quoted lines elided]…
>

I can only guess - but you don't have separate file classes ? That being the
case, then the structure would look different. But in an OO three-tier system it
is the difference between :-

(1)    Business Class
        set OpenOutputFile to true
        invoke FileClass "access-file" using flag returning result

        File Class
        method "access-file"
         Evaluate .......
            when OpenOutputFile
            either perform Para or Section or invoke self "openOutputFile"
            when etc....

as opposed to :-

(2)    Business Class
        invoke FileClass "openOutputFile" returning result

        File Class
        method "openOutputFile"
            open output file
            if file-status <> "00" etc...

(2) is just shorter and direct.

> Again, I don't say that either approach is wrong. I just use what works for
> me. (And, while I am impressed with the extensive reading you have done
…[7 more quoted lines elided]…
>

Ah, now you are the one who used the word "Academia' - and yet it is Will who
has the academic background, having taught COBOL for years. On the other hand
the Pletzkes were doers, part of the original Smalltalk development team - took
the theory and coded it to make it work.

> > "Typicality Smalltalk coding creates simple methods that are approximately
> this
…[15 more quoted lines elided]…
> implement it with or without Sectioned code.

In a nutshell they are saying keep methods SMALL, focused on one piece of
business.

>
> I refuse to agree or disagree on sections. People should use whatever they
…[3 more quoted lines elided]…
>

No contest - we each do our own thing <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-22T07:09:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9AD8A6.60AA3239@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com> <3C982F4E.B387F969@shaw.ca> <3c99271a_6@Usenet.com> <3C996CE9.EEA0333@shaw.ca>`

```
James J. Gavan wrote:
> BTW I have never found a necessity to use an Open Optional which you have
> mentioned previously - either I want the file and it has to be there or I'm
> opening a fresh file (say for Errors).

I use MF and have the compiler settiings include OPTIONAL-FILE so files
opened I-O are created without the need to have OPTIONAL in the SELECT. 
Fujitsu seems to require OPTIONAL for this to happen, I haven't found a
way of getting the same behaviour as MF.

> PS: Bracknell - was that the old ICL Training Centre in Disraeli's old home,
> or the newer ICL building I've seen a picture of  on the Web plastered with
> 'Fujitsu"  ?

I was sent to Bracknell a couple of times for some months when I worked
for ICL here (NZ) in the 70s and early 80s.  I was in the 10 or 12
storey tower block which had the largest computer hall in Europe - now
completely redundant.  As it was a development centre they had large
numbers of very interesting things going on.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-23T13:53:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9be14b_4@Usenet.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com> <3C982F4E.B387F969@shaw.ca> <3c99271a_6@Usenet.com> <3C996CE9.EEA0333@shaw.ca>`

```

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C996CE9.EEA0333@shaw.ca...
>
>
…[9 more quoted lines elided]…
> I can only guess - but you don't have separate file classes ?

I don't use files, full stop. (I use Line Sequential for trivial things,
everything else is RDB).

>That being the
> case, then the structure would look different. But in an OO three-tier
system it
> is the difference between :-
>
> (1)    Business Class
>         set OpenOutputFile to true

Why would the Business level be doing things that are properly the job of
the Data Access Level?

>         invoke FileClass "access-file" using flag returning result
>
…[6 more quoted lines elided]…
>

I wouldn't do this because it is rubbish. I don't think you would do it
either...

> as opposed to :-
>
…[8 more quoted lines elided]…
> (2) is just shorter and direct.

And better...

You surely aren't suggesting I would argue over that?

>
> > Again, I don't say that either approach is wrong. I just use what works
for
> > me. (And, while I am impressed with the extensive reading you have done
> > which led you to change your coding style (good for you!), the "argument
> > from authority" cuts no ice with me. I have seen "Authorities" get it
wrong
> > so often (and many of them live in Acadaemia, far removed from the real
> > world of actually writing code that has to work in commercial
environments),
> > that these days I check out everything, no matter who says it is a good
> > idea. The principle is that it doesn't matter WHO's right; it is WHAT's
…[3 more quoted lines elided]…
> Ah, now you are the one who used the word "Academia' - and yet it is Will
who

No, I used the word "Acadaemia", which is the beautiful Old English
spelling, and adequately conveys the image of crusty old men in gowns and
mortar boards toasting muffins in their studies, amidst the dreaming
spires...Your sterile North American spelling loses it completely...<G>  I
do not consider Will to be a member of "Acadaemia" despite his being a
member of the Teaching Profession. It has to do with attitude... (and
muffins and dreaming spires etc.)

> has the academic background, having taught COBOL for years. On the other
hand
> the Pletzkes were doers, part of the original Smalltalk development team -
took
> the theory and coded it to make it work.
>

 So...?  What is your point here? I never argued with any of this.

> > > "Typicality Smalltalk coding creates simple methods that are
approximately
> > this
> > > complex to slightly more complex, (** they give a couple of simple
…[3 more quoted lines elided]…
> > > methods. This results in a lot of methods generated, but the
complexity of
> > > problems, methods and solutions is reduced considerably, and similar
> > operations
> > > can share common sets of code. Any time a Smalltalk programmer finds
that
> > he or
> > > she is copying code, he or she can instead create a new method that
…[4 more quoted lines elided]…
> > I fail to see the relevance of the above. It is certainly true, but you
can
> > implement it with or without Sectioned code.
>
> In a nutshell they are saying keep methods SMALL, focused on one piece of
> business.
>
Yes, Jimmy, I am reasonably familiar with the English Language and I don't
need a nutshell to understand what they are saying. My point is I never
disagreed with it. (In fact I said it was "true"...see above). I failed to
see what relevance your posting it here has. As we both agree that it is
correct, why would you introduce it into the argument? It is true and we
both know it. My comment was that it can be implemented by using sections or
not using them. As such it is irrelevant to an argument over the use of
sectioned code.
> >
> > I refuse to agree or disagree on sections. People should use whatever
they
> > feel comfortable with. I use sections. I don't care what anyone else
uses
> > (I'll still fix their code if I need to... that's what I do; I'm a
> > "programmer".)
…[3 more quoted lines elided]…
>
Sometimes we have to do someone else's thing also... it's called
"maintenance". I am not persuaded by the argument that proper use of
sections makes code more difficult to maintain. (I said "proper", not like
the example you posted, which you quite properly excused as being "out of
practice"). I also contend that a good programmer can deal with any form of
code. That is the point that seems to have been missed in this discussion.

We (well, some of us) are obsessed with reducing everything to the lowest
common denominator. Ban this, prohibit that, enforce this style NOT that
one... All in the supposed interests of making code easier to maintain.It
makes a mockery of having facilities in the language. COBOL has a simple,
clear, English-like structure (I don't mean progamming structure; that is
something that is not just the prerogative of COBOL, and is decided by the
programmer, not the Language.)....DIVISION > SECTION > PARAGRAPH >
STATEMENT. It is consistent and clear. That is one reason why I use
SECTIONs. (It  is a natural extension of the underlying "philosophy of
COBOL".)

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-21T12:50:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C99D6FB.9F67106A@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com>`

```
James J. Gavan wrote:

> Let's take the format and revamp a method to your Section style

You haven't done that.  While you have added a SECTION keyword to an
unreferrenced label (File-Action) it would make no difference if this
label did not have the keyword, or if the whole label was just commented
out.

Your GO TO to SECTION-EXIT is dangerous and shows that you don't fully
understand what you wrote.  While you appear to think that you went to
the end of the SECTION and thus the program would exit, it only does so
because it is the end of the source code.  If another section was added
after that point then the program would drop down through it until the
end of source code was reached.

Because File-Action is __NOT__ PERFORMed then the GO TO represents a
loss of control.

In fact, beyond adding a SECTION keyword to an unreferrenced lable there
is nothing that makes it anything like 'Section style' (unless you count
'loss of control'  ;-), it is just paragraphs that are performed.

>    if      ws-filestatus <> "00"

When checking for success you should only ever check the first byte for
being '0'.  There are codes that indicate success that are not '00',
such as '02'.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-21T04:50:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9965B2.CC2A812F@shaw.ca>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <3C96D86D.CC438C16@shaw.ca> <3c975e90_10@Usenet.com> <3C99D6FB.9F67106A@Azonic.co.nz>`

```


Richard Plinston wrote:

> James J. Gavan wrote:
>
…[20 more quoted lines elided]…
>

Richard,

Unfortunately you chose to exclude the quote which really mattered :-

> Bear with me, long time since I used Sections so the syntax is probably
> incorrect, but you get the idea.

As I constantly say to my grand kids, "Which part of that sentence didn't
you understand ?" <G>

In fact I haven't used a Section in over 10 years and the example was a
mock-up (tho' you obviously consider it to be a f---up !) To plagiarize
Rhett Butler, "Frankly my dear I don't give a s....!". The topic wasn't
about Sections but their irrelevance to OO.

>
> >    if      ws-filestatus <> "00"
…[3 more quoted lines elided]…
> such as '02'.

Yep agreed.  Going from my file status table :-

01 E2A.
   05 pic x(34) value "00No further information          ".
   05 pic x(34) value "02Keys are equal/or new dup key   ".
   05 pic x(34) value "04Record length incorrect         ".
   05 pic x(34) value "05Optional file not present       ".
   05 pic x(34) value "07Close on non-reel/unit          ".
   05 pic x(34) value "10End of file - no next record    ".
   05 pic x(34) value "14Relative key is incorrect       " etc..........

The checking for the full two character status code occurs in "file-errors".
That was my point about dividing file accesses into simpler methods, one
file type, one file access Verb. The file status check is very specific to
the particular method, whereas the version I originally wrote was omnibus.

BTW I have never found a necessity to use an Open Optional which you have
mentioned previously - either I want the file and it has to be there or I'm
opening a fresh file (say for Errors). It's academic anyway as I'm switching
to SQL.

PS: Bracknell - was that the old ICL Training Centre in Disraeli's old home,
or the newer ICL building I've seen a picture of  on the Web plastered with
'Fujitsu"  ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-19T17:25:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lwKl8.300665$pN4.19770786@bin8.nnrp.aus1.giganews.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost>`

```

<lsunley@mb.sympatico.ca> >
> So instead of
>
…[14 more quoted lines elided]…
>
Or you could have:

perform init
perform process-data
perform quit.
...

init.
perform file-open
....


file-open.
perform open-printer
...

open-printer.
perform select-printer.
if file-output
    perform select-file
    perform open-printfile
else
    OPEN OUTPUT PRINT-FILE.
perform check-error.

etc.

Or, my all-time favorite:

perform get.
perform mull.
perform put.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 4)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2002-03-24T07:55:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9D865F.2FBD1FC4@optonline.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <ZpzG4UNLyRNq-pn2-yP5pb23wjHjO@thishost> <lwKl8.300665$pN4.19770786@bin8.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:
> 
> <lsunley@mb.sympatico.ca> >
…[47 more quoted lines elided]…
> perform put.

The classic:

Input
Process
Output


<g>
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-03-19T13:17:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1UGl8.21558$e33.10068@nwrddc01.gnilink.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
Rufio <davecawdell@cox.net> wrote in message
news:VAwl8.32020$Es6.811372@news2.west.cox.net...
>
>
> Q. How do you write STRUCTURED CODE, without using sections, or the highly
> fallible Perform of paragrpah ranges.

Invalid Assumption. "Highly Fallible" does not apply to "perform of
paragraph ranges." "Fallible" applies to "programmer misuse of performed
paragraph ranges."

Of course, you could always eschew ranges of paragraphs in favor of
performing single paragraphs.

MCM
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-23T09:04:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9C4524.A0B8AC80@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
Rufio wrote:
> 
> > Q. How do you write STRUCTURED CODE, without using sections, or the highly
> > fallible Perform of paragrpah ranges.

> I use sections in a similar manner to the way chapters are used in novels.

I am missing that, how does a novel 'use' chapters in a way related to
programming ?

> If someone has written a large 5000-10000 line program, keeping paragraph
> sizes down to perhaps around 10 statements, then they'll have 500-1000
> paragraphs (I DON'T regard a 20+ line paragraph to be structured code) .

Measuring whether it is 'structured' by counting lines in the paragraphs
is non-sense.  You may find larger paragraphs to be difficult to cope
with, but that doesn't make them un-structured.

Also, I regard setting entirely arbitrary restrictions on how many
statements should be in a paragraph does not aid programming.  There
should be as many statements as are needed to perform the functionality.
 I
> I use sections for clarity. 

> So, when it's my team, or my project, I don't allow hundreds of paragraphs -
> except when contained in sections, and I don't allow paragraphs to grow much
> beyond 10 statements.

You don't actually explain _how_ you use sections.  I see that you have
sections which may contain 'hundreds of paragraphs'.  You _may_ be just
using GO TO to twist your way amonst these, you may be not referencing
the section label at all and just 'using' it to group related paragraphs
and only performing paragraphs, or you may be performing the section and
only have the paragraph labels as commentary.

The 'structure' is not in how many labels you can scatter through your
code as if they were comments, but in how the program _logic_flow_
follows a structure.

> Sections seem like a bonus, and I feel it's just making life harder, not
> using them. 

But 'using' them in what way ?

> So if you want to write code structured as much as possible, in
> a way that makes it easier to read, I recommend Sections 

I would agree that it may make it easier to read _for_you_.  Everyone
finds that 'what is easy' is 'what they are used to'.  You are used to
sections and 'hundreds' of small paragraphs, I may find this like little
twisty passages with no discernable structure.

BTW: my largest single paragraph is 2900 line long, but it has only two
statements: an EVALUATE and an EXIT PROGRAM.  It is perfectly well
structured and very easy to understand, there just happen to be lots of
WHENs, but as each is named then it is quite easy to find what happens
(or as easy as in any other Windows Call-back).
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-23T00:02:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9BC54C.90ED1331@shaw.ca>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <3C9C4524.A0B8AC80@Azonic.co.nz>`

```


Richard Plinston wrote:

>
> BTW: my largest single paragraph is 2900 line long, but it has only two
…[3 more quoted lines elided]…
> (or as easy as in any other Windows Call-back).

Richard,

When you wrote that, you *knew* somebody had to ask. Is this a menu with 2,000
choices in the application <G>

Seriously is that one Evaluate or nested Evaluates, e.g. :-

Evaluate x
    when 1
    when 2
    when 3
    when etc...

OR :-

Evaluate x
    when Condition1thru20
           Evaluate x
                when 1
                when 2 etc
            End-evaluate
    when Condition21thru30
            Evaluate x
                when 21
                when 22
                when etc....

Interestingly the M/F OO support classes have some methods which are solely an
Evaluate, running to a page or page and a half. Given something like testing
returned Keystrokes (OVKs), you haven't got much choice but to put them in a table
of Evaluates.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-23T13:53:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9C88E6.7ED8C2C1@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <3C9C4524.A0B8AC80@Azonic.co.nz> <3C9BC54C.90ED1331@shaw.ca>`

```
James J. Gavan wrote:
> 
> > (or as easy as in any other Windows Call-back).
> 
> When you wrote that, you *knew* somebody had to ask. Is this a menu with 2,000
> choices in the application <G>

It is a Windows Call-Back.  Whenever _anything_ happens on a particular
window it passes a message to the call-back routine for that window. 
This happens to be a very complex window with lots of menus, keystroke
options and clickable bits.  

It does have nested EVALUATEs within it.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

_(reply depth: 5)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-22T22:26:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203222226.5ea0fc96@posting.google.com>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <3C9C4524.A0B8AC80@Azonic.co.nz> <3C9BC54C.90ED1331@shaw.ca> <3C9C88E6.7ED8C2C1@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote 
> It does have nested EVALUATEs within it.

In my experience, pure nested EVALUATEs are hard to read and maintain.
When nesting an EVALUATE is useful, I PERFORM a paragraph which
contains the subordinate EVALUATE.

Stephen J Spiro
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-25T10:05:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9EF672.7AA5C8A3@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
Rufio wrote:
> 
>>> Q. How do you write STRUCTURED CODE, without using sections, or the highly
>>> fallible Perform of paragrpah ranges.

> REPORT-PROCESS SECTION.
> R1000-HEADER-CHECK.
…[28 more quoted lines elided]…
> A-N-OTHER SECTION.

I think that you have a very understanding of what constitutes
'structure'. You have merely scattered unreferrenced and spurious
paragraph labels and non-functional 'EXIT' statements throughout the
section.  

They are _not_ structural, they are merely cosmetic, they do not aid
understanding they just complexify the code.  Those labels may be better
by being made into comments or removed entirely.

This 'style' may make you feel better because there are 'lots of little
functions', but they are _not_ _functional_.  They merely give the
appearance of structure without their being any, and worse, they obscure
the actual structure.

Whenever a program needs to be understood by someone not the author then
they must go through certain steps to ensure they are actually
understanding it and are not mislead.  At every label they must
understand the flow of the code.  Your code entirely misleads readers.
If there is a piece of code that goes:

      named-label.
         some code
         .
      named-exit.
         exit.

Then it is reasonable to expect that this is a function where
'named-label' is the reference to it and it will exit at the point
marked.

Your code scatters these randomly through the actual code.  R400-Exit
_is_ an actual exit point, the rest are not.  This forces the reader to
investigate each and every label and exit to see whether is is actual or
false.

Your paragraphs are like thumb-tacking extra 4x2s onto a house, they
don't add structure, they don't improve the house, they merely get in
the way and make it difficult to find where the real structure is.

Looking at a block of code there is no indication at all which of these
labels are performed. You may understand that only the sections are but
the next programmer does not know that yet, and may take several hours
before they assure themselves this is the case.  You have wasted your
time putting these labels in, the only nett effect is that the next
programmer will have his time wasted doing the best thing for these
labels, consigning them to the bit bucket.

Here is a functional version of your code (ie removing all
non-functional, cosmetic parts):

REPORT-PROCESS SECTION.
    IF LINE-COUNT > 58
        WRITE REPORT-HEADER1 AFTER PAGE
        WRITE REPORT-HEADER2 AFTER 1
        LINE-COUNT = 3
    END-IF
    MOVE Prod-Code        TO Report-Product
    MOVE Prod-Description TO Report-Description
    MOVE Prod-Unit        TO Report-Unit
    MOVE Prod-Quantity    TO Report-Quantity
    MOVE Prod-Price       TO Report-Price
    WRITE REPORT-LINE1 AFTER 2
    WRITE REPORT-LINE2 AFTER 1
    WRITE REPORT-LINE3 AFTER 1    
    ADD 4      TO LINE-COUNT
    READ INPUT-FILE-2 INTO INPUT-BUFFER-2
      AT END 
         SET INPUT-FILE-2-EOF TO 'Y'
    END-READ       
    .
A-N-OTHER SECTION.

There is no _need_ for comments, and especially no need for
dis-functional labels.  The _code_ should say what it is doing
(otherwise just write in C ;-).  The more lines there are, the more
labels, the more misleading exits, the more difficult it is to
understand and the more complex it is to work on.

Having dealt with how unstructured your labels make the code, I can now
look at what your code actually does.  It is entirely a poor example of
how a structured program should be.

Your 'process-report' section has in it elements of dealing with
page-headings and elements of accessing the file.  While you attempt to
separate these out with non-functional paragraphs these are _cosmetic_,
not _structural_.  You disguise your lack of program design by adding a
layer of paint.  If you paint the house then no one will notice that it
is held together with thumb-tacks.

In fact it seems that you _sole_ criteria for whether it is 'structured'
is how many lines are in a paragraph.  Too many lines can be 'fixed' by
banging in another couple couple of labels and an exit.

I would suggest that you read some books on program design and try to
work out what you should be trying to do. 

PS: you don't get paid or measured by the line of code (LoC) do you ?
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-26T23:37:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4D7o8.1248$Va.75328@news2.west.cox.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <3C9EF672.7AA5C8A3@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3C9EF672.7AA5C8A3@Azonic.co.nz...
> Rufio wrote:
> >
> >>> Q. How do you write STRUCTURED CODE, without using sections, or the
highly
> >>> fallible Perform of paragrpah ranges.
>
…[128 more quoted lines elided]…
> PS: you don't get paid or measured by the line of code (LoC) do you ?

What I did, using Procedural Decomposition was break down the particular
print function into its elementary sub-functions, and place each in it's own
paragraph.This encapsulates elementary functions, in their own structure
(paragraph). I could then have PERFORMed each paragraph -
i.e
PERFORM  R1000-HEADER-CHECK
PERFORM R2000-POPULATE-PRINT-LINES
PERFORM R3000-PRINT LINES
PERFORM R4000-WRAP-UP

But as I know that they will always be performed together, I grouped them in
a section, so that anyone who isn't interested, just has to skip the PERFORM
REPORT-PROCESS statement, at the higher level, rather than the 4 PERFORMs.
Yes - the paragraph statements and their matching Do-nothing paragraph
EXIT's appear to function just as comments. But once I add comments to the
code, it will still be immediately obvious where each elementary function
begins & ends, without having to troll through every comment in the source.
As for GOTOs. No well written top-down program should need a GOTO, as there
should be no need to act a lateral redirect. NOTE: I didn't say I never use
GOTO's - just I don't use them in new programs.

Whatever the programming methodology, the key is always adherence to
standards - paragraph names must be consistent and reflect their contents,
etc. Also, the "secret" is, any time spent in design pays back (perhaps
twofold) in coding.

I don't claim to be the worlds greatest programmer. But after a couple of
decades in the business, working on a dozen or so teams (including being
hired onto the same team 3 TIMES in 7 years), on a couple of continents, and
knowing for a fact that NO-ONE, no colleague, manager or client has made any
adverse comments about my code, in over 10 years - and they keep paying me-
I figure perhaps I know a little something about programming. I code for a
number of different things - efficiency, robustness, ease of support & ease
of development, are some of them. My program aren't the fastest and I
occasionally include bugs. But the last major project I managed (designed &
did some of the coding for - released in 2001) took processes, from 3
different applications, migrated the ultimate repository from DLI to DB2,
cost under $350,000 (paid back in about 11 months), cut 96% off CPU time,
and it has a lower failure rate than it's predecessor, so my code isn't just
pretty - it works too!

Again, I ain't the greatest - but this is how I use sections to enhance my
code - I welcome constructive comments about how BETTER to do so. This is
how I earn a living, so I ALWAYS look for ways to be more beneficial to my
clients.
```

##### ↳ ↳ Re: SEQMENTATION

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-27T17:40:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA2041A.AE5FD95A@Azonic.co.nz>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net>`

```
Rufio wrote:
> What I did, using Procedural Decomposition was break down the particular
> print function into its elementary sub-functions, and place each in it's own
> paragraph.This encapsulates elementary functions, in their own structure
> (paragraph). 

No. Wrong.  You haven't 'encapsulated' them at all.  You have merely
added some decoration.  They are not 'elementary sub-functions' but just
have the appearance.  They are not 'in their own structure', there is no
structure, just flappery.

> I could then have PERFORMed each paragraph -
> i.e
…[3 more quoted lines elided]…
> PERFORM R4000-WRAP-UP

And if you had done so the program would then show signs of there being
a structure, of actually using encapsulation, instead of pretending to.

You have added all the overheads as if there was some actual stucture,
but have gained none of the benefits that arise out of structured
programming.  Those paragraphs aren't reusable in any real sense, they
are not 'elementary', they cannot be moved to group them by
functionality because they are not encapsulated.  The labels are merely
a hindrence to understanding what is really happening and a trap for the
unwary.

> But as I know that they will always be performed together, I grouped them in
> a section, 

You could also have done a PERFORM R1000-Header-Check THRU R400-Exit,
with much the same effect of the 'structure'.  But you seem to recognise
that PERFORM THRU is falable, Please explain why you think that there is
any difference at all in your use of SECTIONs in this way.

> so that anyone who isn't interested, just has to skip the PERFORM
> REPORT-PROCESS statement, at the higher level, rather than the 4 PERFORMs.

The whole point of structured programming is to expand from a higher
level of abstraction down to the details in a way that enables the
program to be understood easily and at the levels required to safely do
changes.  Your 'style' does not do this.  It hides the actual structure
and requires that the different levels of abstraction be physically
positioned together because it is _not_ abstracted.

> Yes - the paragraph statements and their matching Do-nothing paragraph
> EXIT's appear to function just as comments. 

They don't 'function' at all.  In fact the do-nothing exits are worse,
they appear to be exit points but should never be used as such.  

Within a PERFORMed section if there are any paragraph labels at all
(except where the compiler requires an initial paragraph) then the only
point of them is to allow a GO TO (or require a GO TO).

The only point of having a xxxx-Exit paragraph label is to cater for a
GO TO.  There is no other functional reason.

Within your performed section a GO TO xxxxx-Exit would operate
correctly, but if this was changed to the 4 performs then these GO TOs
represent a loss of control.  


> But once I add comments to the
> code, it will still be immediately obvious where each elementary function
> begins & ends, 

Why don't you try doing _actual_ encapsulation, making these into
_actual_ 'elementary functions' instead of just pretending to.

For example the 'Header-Check' could actually be used from 'Print-Lines'
instead of being part of the 'Report-Process'.  In this way it would be
the responability of the 'print-lines' routine to ensure that headers
are on the page.  Doing this in a re-usable way (such as in a copybook,
called routine, or class) would reduce the need to re-invent the
'header-check' each time.  It would also mean that if a new site
standard had some new requirement for what was in the page headers it
could be changed in _one_ place instead of having to change each program
separately.

You have failed to understand _how_ structured programming is done
(though you know what it looks like) and you have failed to understand
_why_ structured programming is done.

If your program was to be extended (by the next programmer), by, say,
building a table as the report is processed and then printing out a
summary at the end, then, this too, will need 'Header-Check'.  They
can't just PERFORM the existing one - it is _not_ encapsulated, it is
_not_ an 'elementary function', they would have to copy-and-paste, or
write a new one.

If they did just do a PERFORM R1000-Header-Check then the program could
be destroyed if some other programmer decided that a 'GO TO R1000-Exit'
would be better than adding some complex condition.  The reason that
this would destroy it is that the program _does_not_have_ the structure
that it appears to, they are only cosmetic and should never be used.

Normally I wouldn't take issue with what other programmers use (well OK,
I would), but you queried "Q. How do you write STRUCTURED CODE, without
using sections" as if they were a requirement and then recommended "if
you want to write code structured as much as possible, in a way that
makes it easier to read, I recommend Sections".

I suggest that you find out how to write structured programs from a
design viewpoint, rather than just how to make them have the superficial
appearance of being structured.
```

###### ↳ ↳ ↳ Re: SEQMENTATION

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-28T23:28:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8GNo8.1217$dJ3.42629@news2.west.cox.net>`
- **References:** `<DyPk8.15605$Ex5.1395006@bgtnsc04-news.ops.worldnet.att.net> <VAwl8.32020$Es6.811372@news2.west.cox.net> <3CA2041A.AE5FD95A@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3CA2041A.AE5FD95A@Azonic.co.nz...
> Rufio wrote:
> > What I did, using Procedural Decomposition was break down the particular
> > print function into its elementary sub-functions, and place each in it's
own
> > paragraph.This encapsulates elementary functions, in their own structure
> > (paragraph).
…[24 more quoted lines elided]…
> > But as I know that they will always be performed together, I grouped
them in
> > a section,
>
…[6 more quoted lines elided]…
> > REPORT-PROCESS statement, at the higher level, rather than the 4
PERFORMs.
>
> The whole point of structured programming is to expand from a higher
…[25 more quoted lines elided]…
> > code, it will still be immediately obvious where each elementary
function
> > begins & ends,
>
…[38 more quoted lines elided]…
> appearance of being structured.

OK - you win. I just got a 6-figure (USD) offer from one of the USA's
largest brokerage firms to go work for them. I won't have time to discuss
this further - Bye!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
