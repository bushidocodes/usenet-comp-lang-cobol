[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Information about direct cobol abort codes

_6 messages · 3 participants · 2006-12_

---

### Re: Information about direct cobol abort codes

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-18T15:27:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<em6c11$fom$1@reader2.panix.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <X%Zgh.104$2Y2.99@newsfe03.lga> <em22rd$h68$1@reader2.panix.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com>`

```
In article <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com>,
Ron  <ron@address.below> wrote:
>docdwarf@panix.com () wrote:
>>In article <X%Zgh.104$2Y2.99@newsfe03.lga>,
…[9 more quoted lines elided]…
>a bit fast on the trigger.

That might be... and when I see that I've made an error I do my best to 
admit it and apologise for it, as well.

>This question was esoteric
>enough that experienced COBOL programmers could have a
>tough time with the answer.  Besides not being a part of
>the COBOL standard, it's completely operating system and
>compiler version dependent.

The original poster's statement of 'this should not be done with SOC7 or 
return codes' indicates, to me, an IBM mainframe operating system of some 
sort... and the lack of any sort of indication as to a reason for avoiding 
the two most basic mechanisms points towards - in my experience - an 
academic exercise.  The original poster's utter silence on the matter 
can be seen as falling into the 'assignment due-date has passed' 
category... for those who, upon hearing hoofbeats, might first conclude 
'horses' instead of 'zebras', with all the associated pitfalls of such 
activity, that is.

(The usual 'my boss says these are forbidden' wouldn't hold much water, 
either, as that would indicate a Shop Standard... in which case this 
situation would, most likely, have been addressed by other programs.)

DD
```

#### ↳ Re: Information about direct cobol abort codes

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-18T09:15:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <X%Zgh.104$2Y2.99@newsfe03.lga> <em22rd$h68$1@reader2.panix.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com> <em6c11$fom$1@reader2.panix.com>`

```
On Mon, 18 Dec 2006 15:27:29 +0000 (UTC), docdwarf@panix.com () wrote:

>The original poster's statement of 'this should not be done with SOC7 or 
>return codes' indicates, to me, an IBM mainframe operating system of some 
…[10 more quoted lines elided]…
>situation would, most likely, have been addressed by other programs.)

I've been told similar things by bosses.   This seems to be a very
unlikely student question to me, not really being about CoBOL, but
being about shop standards.

I, also could be wrong, but it fits my experience.
```

##### ↳ ↳ Re: Information about direct cobol abort codes

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-18T16:37:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<em6g42$ear$1@reader2.panix.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com> <em6c11$fom$1@reader2.panix.com> <8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com>`

```
In article <8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 18 Dec 2006 15:27:29 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>(The usual 'my boss says these are forbidden' wouldn't hold much water, 
>>either, as that would indicate a Shop Standard... in which case this 
…[6 more quoted lines elided]…
>I, also could be wrong, but it fits my experience.

I have run into a few of these Shop Standards before... and my 
experience has been that I've been given an assignment, coded it, turned 
it over for review and then had the listing tossed back on my desk with 
a sniffed 'You're using a SEARCH/internal sort/(other 
Standards-permissible technique); those aren't allowed here and you have 
to use a PERFORM/external sort (other technique)'; I then apologise for 
my ignorance and ask 'Is there a program that's done something like this 
that I can use as a template?'... and there has always been such.

So... if it were a matter of Shop Standards then I'd assume - based on my 
own limited exposure to various places and with all the inherent Risks of 
Assumption - that there'd be at least one other program in the system 
where the technique that was needed was used; it would be a rather unusual 
thing to encounter 'Nobody has had to try anything like that previously 
but what you are doing is forbidden.'

(that 'unusual thing' might have been more common in shops that I've 
*heard* of, but never worked in... I recall a fellow, decades on back, 
telling me that on an airline reservation system he worked on (in IBM 
Assembley Language) they were allowed to use only register-based 
instructions (most often RR or RX types)... so that at one point *someone* 
must have written routines that would use these faster instructions to do 
the same stuff as the more-frequently-used SS instructions... but not only 
was that an Assembley shop but it was back in the Oldene Dayse, when a 
bare-metal coder could code code, lo, such as *ten* bare-metal coders 
could not bear to code, todady)

DD
```

###### ↳ ↳ ↳ Re: Information about direct cobol abort codes

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-18T09:46:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45hdo29qdfrf5qa5trcr0dfkd633bcr2ip@4ax.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com> <em6c11$fom$1@reader2.panix.com> <8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com> <em6g42$ear$1@reader2.panix.com>`

```
On Mon, 18 Dec 2006 16:37:22 +0000 (UTC), docdwarf@panix.com () wrote:

>I have run into a few of these Shop Standards before... and my 
>experience has been that I've been given an assignment, coded it, turned 
…[5 more quoted lines elided]…
>that I can use as a template?'... and there has always been such.

The alternative is rare - where a shop standard has existed for some
time and then we are told that it is no longer The Right Way. (Mainly
because they found an important program that had a confusing abort
when the standard didn't work as expected).     Attempting to Updating
standards is normally a futile exercise - unless some big boss was
inconvenienced by the old one (the Important job failed).
```

###### ↳ ↳ ↳ Re: Information about direct cobol abort codes

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-12-18T11:27:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e08f7$4586cf93$454920f8$14308@KNOLOGY.NET>`
- **In-Reply-To:** `<45hdo29qdfrf5qa5trcr0dfkd633bcr2ip@4ax.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com> <em6c11$fom$1@reader2.panix.com> <8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com> <em6g42$ear$1@reader2.panix.com> <45hdo29qdfrf5qa5trcr0dfkd633bcr2ip@4ax.com>`

```
Howard Brazee wrote:
> Attempting to Updating
> standards is normally a futile exercise - unless some big boss was
> inconvenienced by the old one (the Important job failed).

This is true.  :)  I once tried to do this in our shop, when we 
transitioned from COBOL 74 to COBOL 85.  Some of the most contentious 
ones were the ones that weren't new!

One of the standards says something along the lines of "PERFORM...THRU" 
is discouraged - however, if it is used, the target listed on the "THRU" 
clause must be an empty exit paragraph.  From my time there up to that 
point, that wouldn't have changed anyone's code.  There were a couple of 
people who told me that *I* was full of crap, and they would use EXIT 
paragraphs whenever they darn well pleased.  (Of course, this wasn't 
*my* rule (although I agree with it), and what they said they were going 
to do didn't violate it anyway!)

Another one was the removal of the requirement to prefix paragraph names 
with numbers.  I'll admit to being the idea-man on that one - we no 
longer worked from listings, and I'd seen out-of-order paragraphs too 
many times to count -- so much so, that whenever I picked up a new 
program, I ignored them.  A couple of the old-school guys were like 
"What about when we have to code from listings?"  (This became a moot 
point a few months later when our RLP died, and we found out that it no 
longer had a maintenance contract...)

Since I've been back from my deployment, though, I've been looking at a 
lot of code.  (I'm now NCOIC in our shop, so I get included in a lot of 
peer reviews...)  Every one of the military folks, and most of the 
contractors, are using these amended standards that I produced.  Of 
course, we do have a standard (of sorts - not sure if it's official or 
not) that maintenance should be done in the existing style of the program.

One of the cool things I've found relates to DML.  Those who have used 
DML on the Unisys 2200-series mainframes know what I'm talking about. 
Basically, the commands are not surrounded by EXEC...END-EXEC blocks, 
but the compiler acts as a pre-processor (in COBOL 85 - COBOL 74 
actually has a separate pre-processor) and converts these to CALL 
statements.  One of these statements is an IF that checks for set 
membership (ex. "IF RECORD MEMBER OF AUE-TO-MRECS SET").  Since it's 
internally converted to a CALL, there is no END-IF allowed, which can be 
annoying if you're structuring your program with scope delimiters.  I 
got to thinking, and one day I decided to wrap the IF statement in a 
PERFORM...END-PERFORM block.  So now, it looks something like

PERFORM IF RECORD MEMBER OF AUE-TO-MRECS SET
     [do something]
ELSE
     [do something else]
END-PERFORM

The first time I showed this to everyone (as a "hey, look what we can 
do"), about half the people said "Aw, I don't like that - look how 
confusing!"  Once again, they came around - it's a standard way of 
checking for set membership, especially when we're already nested. 
There are two record types in our database that can be joined by one of 
three different sets.  It works really well for that.

I guess the point I'm trying to get across is this - it is possible to 
change standards, especially if there is a good rationale behind it. 
You'll never get 100% agreement - but, if you're doing maintenance, 
you're never going to have 100% compliance in the code unless you do a 
systematic rewrite of everything.  Over time, in the trenches is where 
good standards and bad standards are shaken out.

I still stand by my comment about Mr. Dwarf's "hey, is it apparent what 
this code does?" question.  The number 1 standard that I harp on is 
commenting - don't assume we know what the code does, tell us; and 
telling us why is even better.  That way, if it's not doing it right, we 
have an idea what it's trying to do, even if it doesn't do it.  My #2 
foot-stomper is error handling.  If something can cause an error, it 
should be checked for and handled - this saves hours (and days, in some 
cases) in debugging, when a sympathetic error is the one that gets 
reported instead of the root cause.

My goal is that, once I'm gone from here, the shop will be better off 
because I was there.  Contributions to standards, "best practices," and 
"tips & tricks" are one thing that make me feel that I may realize my 
goal.  I've also created a wiki where I'm writing a lot of information 
about the system - I hope that, since it's easy to write stuff, that 
others will read it, and contribute their own knowledge as well.

Sorry - didn't mean to write a book.  It's been a few days since I've 
had an adult conversation...  :)
```

###### ↳ ↳ ↳ Re: Information about direct cobol abort codes

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-18T11:47:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ifodo2pui3fand0d7gbk4kvuipc3lmj7hg@4ax.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ug9do2h1338h81p2l8a0p09tsm7rvd72nq@4ax.com> <em6c11$fom$1@reader2.panix.com> <8ffdo2pigvorphfhk06s4oogat2ij19e2t@4ax.com> <em6g42$ear$1@reader2.panix.com> <45hdo29qdfrf5qa5trcr0dfkd633bcr2ip@4ax.com> <e08f7$4586cf93$454920f8$14308@KNOLOGY.NET>`

```
On Mon, 18 Dec 2006 11:27:56 -0600, LX-i <lxi0007@netscape.net> wrote:

>PERFORM IF RECORD MEMBER OF AUE-TO-MRECS SET
>     [do something]
>ELSE
>     [do something else]
>END-PERFORM

With my pre-compiler I can do the following:
IF H-EXT = SPACE                                    
   MOVE AA-BS-BILL-PRINT TO AA-BN-BILL-PRINT        
ELSE                                                
    OBTAIN IABRCNS WITHIN IABRCAA-IABRCNS           
        USING H-EXT                                 
    ON DB-REC-NOT-FOUND                             
        CONTINUE                                    
END-IF.                                             

Which translates to:
     IF H-EXT = SPACE                                     
        MOVE AA-BS-BILL-PRINT TO AA-BN-BILL-PRINT         
     ELSE                                                 
*        OBTAIN IABRCNS WITHIN IABRCAA-IABRCNS            
*            USING H-EXT                                  
*        ON DB-REC-NOT-FOUND                              
           MOVE 13 TO DML-SEQUENCE                        
           CALL 'IDMS' USING SUBSCHEMA-CTRL               
                   IDBMSCOM (33)                          
                   SR1813                                 
                   IABRCAA-IABRCNS                        
                   H-EXT                                  
                   IDBMSCOM (43)                          
           IF NOT DB-REC-NOT-FOUND PERFORM IDMS-STATUS;   
           ELSE                                           
             CONTINUE                                     
     END-IF.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
