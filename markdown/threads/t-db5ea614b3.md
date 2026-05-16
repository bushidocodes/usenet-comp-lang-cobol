[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ugly IF Statement

_38 messages · 19 participants · 2001-04 → 2001-05_

---

### Ugly IF Statement

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2001-04-11T02:54:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
We get a lot of students either posting or lurking here so the other day while
working on a particularly nasty program (8000 some lines of spaghetti code with
polish logic) I came across this particular IF statement no less than 9 times
in the program and thought they would like to see what's in store for them.

This is what you get to see in the real world :)

IF (AIHD-SALES-CLS = 11 OR 34 OR 61) OR                  
    ((AIHD-SALES-CLS = 14 OR  35) AND                     
     (WS-DEST-CD-1 = 'AP' OR 'WE'))                       
  OR SPECIAL-CHRY-CLS                                     
  OR ((AIHD-SALES-CLS = 14) AND                           
     (WS-DEST-CD-1 = 'EE' OR 'EF' OR 'FD' OR 'PP' OR 'CC' 
                          OR 'IE'))                       
  OR (AIHD-SALES-CLS = 35)                                
  OR ((AIHD-SALES-CLS = 30) AND                           
      (AIHD-CUST-NO                                       
                   = 09937 OR 10100 OR 10181 OR 10190     
                           OR 11100 OR 09941 OR 09949     
                           OR 10222 OR 01552 OR 11109     
                           OR 10108))                     
  OR ((AIHD-SALES-CLS = 14 OR 35) AND                     
      (WS-DEST-CD     = 'TC04A' OR 'TC11A' OR '0100A'))   
  OR ((AIHD-SALES-CLS = 18) AND                           
      (WS-DEST-CD = '48063' OR '17576'))
OR ((AIHD-SALES-CLS = 30) AND                               
      (WS-DEST-CD = '04179' OR '12014' OR 'LSC07' OR '31   '))
  OR (AIHD-CUST-NO = 08221 OR 05659 OR 00879 OR               
                     08228 OR 10418 OR 11010 OR               
                     08288)                                   
      PERFORM xxxxxx
END-IF

There are lower case x's at the PERFORM to indicate that different paragraphs
are performed each time the IF appeared in the program.  The paragraphs were
identical except for one or two variables from the map (this is a CICS
program).  These variables are actually an occurance but the map is not
redefined so each time the field in question is used such as QTY1 or QTY2 the
paragraph is duplicated.  Makes maintenance a real nightmare.

You will also notice that there are a few ORs that preclude the execution of
other ORs (that is it doesn't matter as something before it takes precedent -
assignment: see if you can find it).

The fields being tested are in the header record which is read at the beginning
of the program.  The IF statement is now reworked and a switch set if
everything makes it thru the tangle and the switch checked where each of the
original IFs were.  Just my part of making this nightmare a bit more managable.

Eileen
```

#### ↳ Re: Ugly IF Statement

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-04-10T22:33:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b0jc8$3o2u$1@newssvr06-en0.news.prodigy.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
That compound IF statement looks like a prime example of someone's
attempting to avoid GO TO statements and by so doing, making the situation
even worse.  I sympathize with you.
```

##### ↳ ↳ Re: Ugly IF Statement

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-04-12T13:18:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD59D32.2D917112@Azonic.co.nz>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <9b0jc8$3o2u$1@newssvr06-en0.news.prodigy.com>`

```
> "YukonMama" <yukonmama@aol.com> wrote in message
> >
…[24 more quoted lines elided]…
> > END-IF

It seems to me that this has been a 'special case' that has grown over
the years.

There area a number of Cust-No, a few Sales-Cls (Sales Class?).  It
seems to me that this is as inappropriate to be hard coded as would the
prices of products.  Without details of what this is actually trying to
solve I would suggest that it would be done better by a field held in
the Customer master record, one in the Sales Class Master (or some
similar) and possibly another in the Destination master record, or maybe
a Class/Destination,Class/Customer file built for the task.

Then the appropriate people can set/reset the factors controlling this
without having to reprogram the system each time.  You may also find
that many of the special cases actually are no longer required but the
reports that result from the selection are just ignored now for those
cases.

It is not so much an 'ugly if statement', but an 'ugly solution' to
whatever requirement drove it.
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-04-12T11:06:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9CC3A6DDB10FE32F.1FD3F58B440EB46E.E7526657520F1EC5@lp.airnews.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <9b0jc8$3o2u$1@newssvr06-en0.news.prodigy.com> <3AD59D32.2D917112@Azonic.co.nz>`

```
On Thu, 12 Apr 2001 13:18:58 +0100, Richard Plinston
<riplin@Azonic.co.nz> enlightened us:

>> "YukonMama" <yukonmama@aol.com> wrote in message
>> >
…[44 more quoted lines elided]…
>whatever requirement drove it.

I've seen uglier IFs than that one, but that one would give you a
headache trying to envision the decision tree.

To add to Richard's thought, I'll bet that IF started out very simple.
Then, for whatever reason, more conditions were added as time went
along.  Finally, it has reached the point where the requirements need
to be totally defined so that the solution is apparent.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I have a twin brother; he's identical, but I'm not.


DON'T DRILL in the Artic National Wildlife Refuge
Read the facts and sign a petition at:

http://www.savepolarbears.org/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** Jeff Baynard <jeffbaynard@home.com>
- **Date:** 2001-04-13T02:23:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6FBDB78.8BF%jeffbaynard@home.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <9b0jc8$3o2u$1@newssvr06-en0.news.prodigy.com> <3AD59D32.2D917112@Azonic.co.nz>`

```
yeah, you just can't write good and clean with this much hardcode.  hardcode
makes me sick pretty much, although it is good job security and OK for older
jobs or systems.  This *could* have been done better with external tables
either from files or a database.

I see NEW programs being written this way, typically to interface one system
to another.  It is pathetic to see NEW programs written that look like this,
but trust me, these people 'round here' can churn this monkey code out in a
fairly unremarkable period of time.  THERE ARE VERY LARGE COMPANIES MAKING
VERY POOR DECISIONS THESE DAYS.   IT CONTINUES TO AMAZE AND BEWILDER ME.



Jeff


in article 3AD59D32.2D917112@Azonic.co.nz, Richard Plinston at
riplin@Azonic.co.nz wrote on 4/12/01 8:18 AM:

>> "YukonMama" <yukonmama@aol.com> wrote in message
>>> 
…[44 more quoted lines elided]…
> whatever requirement drove it.
```

#### ↳ Re: Ugly IF Statement

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-11T03:59:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD3D64A.A40007C@home.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```


YukonMama wrote:

> We get a lot of students either posting or lurking here so the other day while
> working on a particularly nasty program (8000 some lines of spaghetti code with
…[47 more quoted lines elided]…
> Eileen

Ugly aint the right word for it. I was right, you are still living your life on
this earth maintaining those gawdawful systems <G>. I just love applications where
some jerk throws in account numbers to create exception tests.

Smaller scale, but inspection points being tested look like this :-

        01 Top
        02 Bottom
        03 North
        04 South
        05 .....
        32 After Weld
        ....
        35 Lamination
        .......
        42 Temperature Loss
        43 etc....

In my application last three codes, plus more, create exception conditions for
different calculations - necessitated storing a 'table'. Problem was it was an
afterthought by the user. For the new version of the application I gave the above
two-digit numeric codes four-character mnemonics - easier for user to remember -
TOP - Top, BTM - Bottom, AW - After Weld, LAM - Lamination, TEMP - Temperature etc.

Still concerned about exception testing I took those last three and their
'brethren' and called them XAW, XLAM, XTMP - the "X" gives me one conditional test
- and then I go from there.

What my solution says - it starts at the design level before you hit programming.
In your case that may be a luxury you don't have. But you may have a solution if
you push really hard. I note the account numbers you quote are 5-digit. Can you not
make a case that exception account #s should be re-allocated to start with a  "9"
for example. (That's purely a wild suggestion, not knowing how your A/c #s are
structured). I *know* it's a change of account numbers - but seriously, nobody
should go histrionic over such a suggestion from you, if the justification is to
keep the programming simple and effective. Give them (the bean counters) some BS
that the program currently takes 30 minutes longer to run than it would without an
account number revision.

One other possible solution is what I call analysis codes, e.g. just like in a
Chart of Accounts - completely ignoring the coding system, (which inevitably breaks
down from the originator's original conception), you have an Account-Type field,
telling you it's Current Assets, Fixed Assets etc... Given space in the appropriate
records - say Customer Names, have an analysis flag, (Type of Customer)  that
triggers an exception.

Three questions :-

(1) Not sure when you say "The fields being tested are in the header record which
is read at the beginning of the program". Are these (a) run parameters or (b) a
fixed table complying with Level 88 rules ? Even if (a) they could still be fed
into a table.
.
(1) - Do you favour IFs over EVALUATEs - If it was me I'd go for the latter, even
with the confusion caused in the existing code.

(2) Howz about :-

01 GawdawfulConstants                pic 9(02).
    88 SalesGroup1                        value 11, 34, 61.
    88 SalesGroup2                        value 14, 35.

IF (AIHD-SALES-CLS = 11 OR 34 OR 61) OR
    ((AIHD-SALES-CLS = 14 OR  35) AND

Evaluate true
    when SalesGroup1.......
    when SalesGroup2 AND .........
    when ........

Jimmy
```

#### ↳ Re: Ugly IF Statement

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2001-04-10T23:12:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
Be glad it written in COBOL. At least you can read it.
Think what unintelligible, cryptic, gobbledegook this
would be in C!

IF (AIHD-SALES-CLS = 35) overrides the check further on down
looking for values in WS-DEST-CD. The perform will occur no
matter what is in WS-DEST-CD.

Years ago I worked at an insurance company. They had a claims
processing program (I wish I had a copy of it) that had 1 nested
IF statement 5 pages long. No kidding. An ELSE on page 4 paired
with an IF on page 1 for example. And a whole bunch of
intervening IF - ELSE scattered all throughout.
The only way to do anything with this mess was to print the whole
thing, tack it up on the wall and draw lines to line up the
IF's with the ELSE's, which of course didn't align on the page
at all. This was in the days before END-IF too. It was just dreadful.

=================================================================


"YukonMama" <yukonmama@aol.com> wrote in message news:20010410225436.26397.00004167@ng-cf1.aol.com...
> We get a lot of students either posting or lurking here so the other day while
> working on a particularly nasty program (8000 some lines of spaghetti code with
…[55 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Ugly IF Statement

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2001-04-14T02:42:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010413224213.00708.00000108@ng-ce1.aol.com>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com>`

```
>From: "Ron" NoSoy@swbell.net 
>Date: 4/10/01 9:12 PM Pacific Daylight Time

>Years ago I worked at an insurance company. They had a claims
>processing program (I wish I had a copy of it) that had 1 nested
>IF statement 5 pages long.


Was the company 'blue' by chance? :D  I've also worked in insurance and I think
I may have seen that IF statement!

As for this particular IF - I can tell everyone that yes - those are sales
classes - tells us if the product is production, service, or prototype.  Each
of our customers is assigned a set of these (well at least the big 3 are), and
the DEST are destination codes indicating the assembly plant/dock the product
is to be delivered to.  I have checked and all the customer numbers are still
in business - in fact it is one customer but we assign a customer number to
each ship to rather than sold to thus the multiple numbers (there is another
master that uses Duns numbers for the sold to).  And yes - I hate the hard
coding as much as anyone else.

I can't remember who saw the AIHD-SALES-CLS = 35 but yes - that's it for some
of the other compound parts of the IF.  I've already move it up in the IF and
taken it out of the '14 or 35' statements.

What this is trying to do is determine if another file has to be accessed
and/or updated (which is determined further along in the program).  

Sales classes 11, 34, and 61 belong to one customer and only those particular
destinations need the file updated.  14 and 35 belong to another which could
have destinations starting the same as the other so that's why the compounds
are the way they are (I would have done as was shown by someone else combining
things had this not been the case - and they did not know this so I agree with
the 'solution' as it were). 

Came across another goodie in that program - would you like to tear that one
apart too?  I think it only appears 3 times (maybe 4) in the program.

Eileen
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-14T14:13:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hWYB6.1064$dW5.132936@paloalto-snr1.gtei.net>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com>`

```
YukonMama <yukonmama@aol.com> wrote in message
news:20010413224213.00708.00000108@ng-ce1.aol.com...
> >From: "Ron" NoSoy@swbell.net
> >Date: 4/10/01 9:12 PM Pacific Daylight Time
…[6 more quoted lines elided]…
> classes - tells us if the product is production, service, or prototype....

This whole thing is is really the slam-dunk case for an external call to a
separate (or nested, see below) program.

Instead of inlining the call 4-5-times across several separate programs,
this really should be re-engineered as...


ID DIVISION.
PROGAM-ID. UPSALES.
...
LINKAGE SECTION.
01 SALES-CLASS          PIC X(02).
01 CUSTOMER-NUMBER  PIC X(12),
01 DESTINATION_CODE   PIC X(02).
01 YES-OR-NO                PIC X(01)

PROCEDURE DIVISION USING SALES-CLASS, CUSTOMER-NUMBER, DESTINATION-CODE,
YES-OR-NO

IF
  as ugly as you want it

END-IF
GOBACK
END PROGRAM UPSALES


Then in all using programs at any point,

CALL UPSALES-PROGRAM USING .....    <<< dynamic call
IF YES-OR-NO = "Y'
   PERFORM xxx
END-IF


Now, so what if it's ugly? The using programmer doesn't need to know squat,
and any change in the business logic automatically propogates to all using
programs without recompilation or re-linking. (And you can make the changes
NOW without the need to wait for the business people to decide what the rule
is going to be today).

I did a bunch of these for a "Blue" healthcare insurance firm. I, too, got
tired of the same damn code in four or five different programs and four or
five repeats within each program - changes in the rules were just too big a
PITA to implement across the system.

In this case (a single program with multiple repititions of the same ugly
logic) a nested or conatined program - not even a separate run unit - could
have relocated all the long, ugly IF statements to one common point for
future maintenance.

No, I have not solved the problem of "Ugly IF" but at least this ways
isolates it and prepares the system for a change in the business rules.

Maybe the "Ugly IF" is the result of poor business rules, but it seems to me
the programmer is responsible for engineering the implementation of those
rules, and should have selected a method similar to this.


MCM
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-04-14T14:51:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OtZB6.7996$Pj2.725292@newsread1.prod.itd.earthlink.net>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com> <hWYB6.1064$dW5.132936@paloalto-snr1.gtei.net>`

```

"Michael Mattias" <michael.mattias@gte.net>

> This whole thing is is really the slam-dunk case for an external
call to a
> separate (or nested, see below) program.
>
> Instead of inlining the call 4-5-times across several separate
programs,
> ......

and taking the (very real) chance that one instance gets missed during
a logic update,

...
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 5)_

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2001-04-14T11:19:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tdgtqrtdka71d8@corp.supernews.com>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com> <hWYB6.1064$dW5.132936@paloalto-snr1.gtei.net> <OtZB6.7996$Pj2.725292@newsread1.prod.itd.earthlink.net>`

```
If multiple copies of this "cloned" code (or variants) exist across
multiple files, than you indeed have a serious problem keeping
them up to date.

A tool that can find these copies and factor them out into single
abstractions (e.g., a copybook) can be seen at
http://www.semdesigns.com/Products/Clone/index.html

Another poster suggested that carrying out symbolic simplification
of the ugly IF statements would at least help readability.
The DMS engine underneath the Clone remover can actually
do such symbolic simplification.
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-15T10:32:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad8d467_1@my.newsfeeds.com>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com> <hWYB6.1064$dW5.132936@paloalto-snr1.gtei.net> <OtZB6.7996$Pj2.725292@newsread1.prod.itd.earthlink.net> <tdgtqrtdka71d8@corp.supernews.com>`

```
Thanks Ira,

It is rare to get a direct and simple answer to a question in this
Newsgroup. (That's why I always answer the question before departing into
"the Wild Blue Yonder".)

I asked if anyone knew of any tools which do symbolic simplification and you
have named one.

Appreciated.

Pete.

Ira D. Baxter wrote in message ...
>If multiple copies of this "cloned" code (or variants) exist across
>multiple files, than you indeed have a serious problem keeping
…[37 more quoted lines elided]…
>



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2001-04-17T18:19:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bij2i$nsn$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com>`

```
> Was the company 'blue' by chance? :D  I've also worked in insurance and I think
> I may have seen that IF statement!

Just getting back from Easter vacation....
You got it -  It was in fact 'Blue'! Pretty disgusting code wasn't it?

Another little gem from the same place in a different program was
a PERFORM A THRU A-Exit. Paragraph A contained various GO TO statements
that sent control all over the program no-where within the paragragh A
range. Then from a half dozen different places you would find (in
paragraph R, for example) 'GO TO A-EXIT'. YIKES! A huge mess.

One interesting thing in yet another program was something someone
did with data names by using more than one dash, something like:

05 WS01---CUSTOMER--FIRST--NAME   PIC X(30).
05 WS01---ZIP--CODE               PIC X(5).

Not illegal but I've never that done before or since. Very weird.

Ron.
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 2001-04-18T14:46:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADE0B21.8234B539@compaq.com>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com> <9bij2i$nsn$1@sshuraab-i-1.production.compuserve.com>`

```
In a new version of our compiler (Compaq/Tandem) I had to redo the method of
handling PERFORM exits and had to put a finite limit on the number of nested
performs.  I made it around 30.  The first customer that hit it had exactly what you
describe and found that the program was not doing what they thought it was doing.
The next one said they needed a bigger limit, so I changed it to 50.  Can you
imagine 50 levels of nested performs?  Or, is this legitimate?

Don Nelson

Ron wrote:

> ...
> Another little gem from the same place in a different program was
…[5 more quoted lines elided]…
> ...
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 5)_

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2001-04-21T01:24:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ae0e141.23309227@news1.frb.gov>`
- **References:** `<9b0lj9$a9$1@sshuraac-i-1.production.compuserve.com> <20010413224213.00708.00000108@ng-ce1.aol.com> <9bij2i$nsn$1@sshuraab-i-1.production.compuserve.com> <3ADE0B21.8234B539@compaq.com>`

```
On Wed, 18 Apr 2001 14:46:11 -0700, Don Nelson wrote:

>[...] Can you imagine 50 levels of nested performs?

I have seen stuff that comes out of program generators that could
challenge this limit.

(I said "stuff" as I don't consider "code" to accurately describe most
program generator output.)
```

#### ↳ Re: Ugly IF Statement

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-11T11:37:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lmXA6.206$VS2.34256@dfiatx1-snr1.gtei.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
YukonMama <yukonmama@aol.com> wrote in message
news:20010410225436.26397.00004167@ng-cf1.aol.com...
...
> This is what you get to see in the real world :)
>
…[3 more quoted lines elided]…
> You will also notice that there are a few ORs that preclude the execution
of
> other ORs (that is it doesn't matter as something before it takes
precedent -
> assignment: see if you can find it).
>

Better assignment: rewrite this logic to make it maintainable.

Students only. Spaghetti veterans not eligible. Winner is responsible for
all taxes. Void where prohibited.

MCM
```

#### ↳ Re: Ugly IF Statement

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2001-04-11T07:11:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD449F4.F71A9391@certcoinc.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
My condolences.  Code like that kind of gives you the shivers.

PatH

YukonMama wrote:

> We get a lot of students either posting or lurking here so the other day while
> working on a particularly nasty program (8000 some lines of spaghetti code with
…[47 more quoted lines elided]…
> Eileen
```

##### ↳ ↳ Re: Ugly IF Statement

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-04-11T13:16:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TOYA6.503$DW1.29316@iad-read.news.verio.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3AD449F4.F71A9391@certcoinc.com>`

```
In article <3AD449F4.F71A9391@certcoinc.com>,
Pat Hall  <phall@certcoinc.com> wrote:
>My condolences.  Code like that kind of gives you the shivers.

Hmmmmmm... code like that give me a living!  All that's needed to complete
it would be something like PERFORM D32158-R0300-READ-MF84271-MFILE-NEXT
THRU D31258-EXIT.

(Also of note is the mixing of 88s with hardcoded values; this is usually
found in the more hoary applications which have survived several changes
in shop-styles)

DD

>YukonMama wrote:
>
…[50 more quoted lines elided]…
>
```

#### ↳ Re: Ugly IF Statement

- **From:** Anonymous <anonymous@anonymous.anonymous>
- **Date:** 2001-04-12T03:11:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad47463_1@anonymous>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
Eileen,

I thought it was a beautiful IF statement...<G>

It was certainly jolly interesting...

Instead of doing the daily crossword today I resolved to see if it could be
simplified and how much would be gained.

I converted it to symbolic notation, did a Boolean simplification on it (it
would've been MUCH more "interesting" if we had some NOTs in it...<G>) and
arrived at the following, which purports to be logically equivalent (unless
I made a mistake in the simplification or symbol transitions...not
unknown...I haven't time or inclination to check it on my computer so I'll
just risk the red face if it is wrong...)

Anyway, although there are some savings, there are not as many as you might
think when first looking at it...

if AIHD-SALES-CLS = 11 OR 34 OR 61 OR 35
                         OR
    SPECIAL-CHRY-CLS
                          OR
    AIHD-CUST-NO = 08221 OR 05659 OR 00879 OR
                     08228 OR 10418 OR 11010 OR
                     08288
                          OR
    (AIHD-SALES-CLS = 14 AND
    (WS-DEST-CD-1 = 'AP' OR 'WE' OR 'EE' OR 'EF' OR 'FD' OR
                                       'PP' OR 'CC' OR 'IE'  OR
    WS-DEST-CD     = 'TC04A' OR 'TC11A' OR '0100A'  ))
                          OR
    (AIHD-SALES-CLS = 30 AND
    (AIHD-CUST-NO  = 09937 OR 10100 OR 10181 OR 10190  OR
                                       11100 OR 09941 OR 09949 OR
                                       10222 OR 01552 OR 11109  OR
                                       10108 OR
     WS-DEST-CD = '04179' OR '12014' OR 'LSC07' OR '31   '))
                            OR
     (AIHD-SALES-CLS = 18 AND
      (WS-DEST-CD = '48063' OR '17576'))
        perform XXXX
end-if

I am NOT proposing that the above is "elegant" code, but at least it has
removed the redundant tests (or it should have, if I got my sums
right...<G>). This in turn removes the "precedence" which someone else in
the thread has already identified.

In an on-line environment the tests could be prioritised and shuffled around
the "OR"s so that the most likely events were tested for first; in Batch, it
really doesn't matter...

I agree that a better approach would be to break it down and derive "logic
values" which could be tested.

Thanks for an interesting 20 minutes...<G>

Pete.

YukonMama wrote in message <20010410225436.26397.00004167@ng-cf1.aol.com>...
>We get a lot of students either posting or lurking here so the other day
while
>working on a particularly nasty program (8000 some lines of spaghetti code
with
>polish logic) I came across this particular IF statement no less than 9
times
>in the program and thought they would like to see what's in store for them.
>
…[28 more quoted lines elided]…
>There are lower case x's at the PERFORM to indicate that different
paragraphs
>are performed each time the IF appeared in the program.  The paragraphs
were
>identical except for one or two variables from the map (this is a CICS
>program).  These variables are actually an occurance but the map is not
>redefined so each time the field in question is used such as QTY1 or QTY2
the
>paragraph is duplicated.  Makes maintenance a real nightmare.
>
>You will also notice that there are a few ORs that preclude the execution
of
>other ORs (that is it doesn't matter as something before it takes
precedent -
>assignment: see if you can find it).
>
>The fields being tested are in the header record which is read at the
beginning
>of the program.  The IF statement is now reworked and a switch set if
>everything makes it thru the tangle and the switch checked where each of
the
>original IFs were.  Just my part of making this nightmare a bit more
managable.
>
>Eileen
…[7 more quoted lines elided]…
>


  --------== Posted Anonymously via Newsfeeds.Com ==-------
     Featuring the worlds only Anonymous Usenet Server
    -----------== http://www.newsfeeds.com ==----------
```

##### ↳ ↳ Re: Ugly IF Statement

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-13T15:27:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad674e8_4@my.newsfeeds.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous>`

```
I gave some more thought to this...

While most of the thread is wailing about what awful code it is, and
speculating about how it came to be and what would be a much better solution
(all fine, as far as it goes...) it occurred to me that there is a TON of
this stuff sitting around on mainframes (and PCs probably...) and it won't
go away and it won't get re-written (well, not overnight , anyway).

The 20 minute exercise I did which produced this...

if AIHD-SALES-CLS = 11 OR 34 OR 61 OR 35
                         OR
    SPECIAL-CHRY-CLS
                          OR
    AIHD-CUST-NO = 08221 OR 05659 OR 00879 OR
                     08228 OR 10418 OR 11010 OR
                     08288
                          OR
    (AIHD-SALES-CLS = 14 AND
    (WS-DEST-CD-1 = 'AP' OR 'WE' OR 'EE' OR 'EF' OR 'FD' OR
                                       'PP' OR 'CC' OR 'IE'  OR
    WS-DEST-CD     = 'TC04A' OR 'TC11A' OR '0100A'  ))
                          OR
    (AIHD-SALES-CLS = 30 AND
    (AIHD-CUST-NO  = 09937 OR 10100 OR 10181 OR 10190  OR
                                       11100 OR 09941 OR 09949 OR
                                       10222 OR 01552 OR 11109  OR
                                       10108 OR
     WS-DEST-CD = '04179' OR '12014' OR 'LSC07' OR '31   '))
                            OR
     (AIHD-SALES-CLS = 18 AND
      (WS-DEST-CD = '48063' OR '17576'))
        perform XXXX
end-if

from this...

>
>IF (AIHD-SALES-CLS = 11 OR 34 OR 61) OR
…[24 more quoted lines elided]…
>

...could be automated and done in thousandths of a second.

It would involve converting the conditions to symbolic logic, applying
Boolean Algebra to the symbolic logic to simplify it, then converting the
simplified symbolic logic back to the original conditions, having removed
the unnecessary ones and added new ones which represent combinations of old
ones derived from the simplification.

Of course the same principles would handle much more complex tangles than
the above (especially where negations of existing conditions where also
thrown into the mix).

Three questions:

1. Does anybody know of any source manipulation packages which can do this?

2. Does anybody know of any potential sites where such a tool could be sold?
(I guess Eileen's would be one...<G>)

3. Anybody prepared to help write it, as a spare time back burner project
with the only return being a share in the profits (if any)?

(You would need to state that you have no objection to working with someone
who stands accused of having a retarded NZ education, and a questionable
grasp of logic...at least if this NG is anything to go by...(Don't bother
applying, Jerry...<G>))

Pete.





-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-13T05:05:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD688FF.3C5A2E62@home.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com>`

```


"Peter E. C. Dashwood" wrote:

> I gave some more thought to this...
>
…[4 more quoted lines elided]…
> go away and it won't get re-written (well, not overnight , anyway).

In view of what you've written I've given it some more thought too. The long
term, as Richard and I have suggested, is a flag(s) in records to get at these
conditons. That may or may not be possible.

Your suggestion may turn out a very elegant coding solution, in fact so elegant,
once introduced, a future coder may not want to even tinker with it - not being
sure what his current tinkering will do <G>

So some suggestions :-

1. Change the program to have table(s) to access the specifics used in the
'Ugly' code. Doesn't happen every day, but every time a new addition is made, it
does mean a re-compile. (An alternative to this would be as a forerunner, read
in parameters to currently fill the condition table).

2. Consider use of those file flags - some assumptions here, and it may even
necessitate file reads, which the 'Ugly' program doesn't currently do. Given
that the appropriate file record has a 'filler' either pic x or pic 9, or even
an existing field where you could 'pinch' the last 1 or 2 characters :-

(a).    - Read infile and initialize the new flag field as a pic x space or pic
9 zero

(b).    - 'Assuming' only one program 'edits' the file containing the new
flag(s) -  change the edit program.

(c).    -  Now use the revised edit program to put 'valid flags' into the file
generated    by  (a)  for records you wish to capture (records not appropriate
have either zero or  space flags).

OK (a) - Let's assume it is a file with 30 million customers, (to be extreme),
having tested on a reasonable sample file to prove it - it is only one exercise
to make that change - even if it takes 'x' hours.

And the result is you have something designed logically as well as programmed
logically.

But of course I see the gleam in your eye - let's come up with a nifty
programming solution <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-14T01:07:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad7005b_4@my.newsfeeds.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com> <3AD688FF.3C5A2E62@home.com>`

```
Some comments below, but no issues here. Please see also my response to
Michael.

I think the constraints were missed... (Well, they were in my head, but I
neglected to verbalize them...<G>)

James J. Gavan wrote in message <3AD688FF.3C5A2E62@home.com>...
>
>
…[5 more quoted lines elided]…
>> speculating about how it came to be and what would be a much better
solution
>> (all fine, as far as it goes...) it occurred to me that there is a TON of
>> this stuff sitting around on mainframes (and PCs probably...) and it
won't
>> go away and it won't get re-written (well, not overnight , anyway).
>
>In view of what you've written I've given it some more thought too. The
long
>term, as Richard and I have suggested, is a flag(s) in records to get at
these
>conditons. That may or may not be possible.
>
Are you suggesting that a pass is made to set the flags for the required
extraction? More information please, Jimmy.

>Your suggestion may turn out a very elegant coding solution, in fact so
elegant,
>once introduced, a future coder may not want to even tinker with it - not
being
>sure what his current tinkering will do <G>
>
It would definitely turn out an elegant coding solution; mathematically
pure. The point is you could tinker with it to your heart's content, adding
all the rules you (or the Business or anyone else) could think of, then run
it through the "logic engine" and get mathematically pure, non-redundant
code. It would still need manual optimizing for things the Engine could not
be aware of, like conditional priorities in on-line environments (if anybody
still cares about things like that...)

Actually, when I put it like that, it sounds a bit like a 4GL or
IEF...p'raps it isn't such a good idea after all...<G>

Also, the majority of programmers nowadays don't write stuff like that in
the first place, do they...? Not much point in a logic optimizer if  there's
nothing to optimize...

It is possible that such a tool could be a useful part of another tool which
was employed leveraging and re-factoring Legacy code. Maybe prior to
wrapping the old code as components for re-deployment on the Network (see my
article on www.aboutlegacycoding.com)


>So some suggestions :-
>
>1. Change the program to have table(s) to access the specifics used in the
>'Ugly' code. Doesn't happen every day, but every time a new addition is
made, it
>does mean a re-compile. (An alternative to this would be as a forerunner,
read
>in parameters to currently fill the condition table).
>
>2. Consider use of those file flags - some assumptions here, and it may
even
>necessitate file reads, which the 'Ugly' program doesn't currently do.
Given
>that the appropriate file record has a 'filler' either pic x or pic 9, or
even
>an existing field where you could 'pinch' the last 1 or 2 characters :-

Hey, we're not going to revisit the absorbing discussion on File Opens Vs
Reads again are we...I'll just find my book of Vogon poetry...
>
I saw Richard's suggestion re file flags and liked it. Liked even more his
final summation:

"It is not so much an 'ugly if statement', but an 'ugly solution' to
whatever requirement drove it."

I think everyone here would agree on that.


>(a).    - Read infile and initialize the new flag field as a pic x space or
pic
>9 zero
>
…[3 more quoted lines elided]…
>(c).    -  Now use the revised edit program to put 'valid flags' into the
file
>generated    by  (a)  for records you wish to capture (records not
appropriate
>have either zero or  space flags).
>
>OK (a) - Let's assume it is a file with 30 million customers, (to be
extreme),
>having tested on a reasonable sample file to prove it - it is only one
exercise
>to make that change - even if it takes 'x' hours.
>
>And the result is you have something designed logically as well as
programmed
>logically.
>
Watch the verb "to assume", Jimmy. You know the old saying....

>But of course I see the gleam in your eye - let's come up with a nifty
>programming solution <G>
>

Can't help it. Born to program...uneducated, illogical, still keep churning
'em out. They still keep working and people still keep buying 'em...can't
stop, gotta do it....

Seriously, after 36 years, I STILL get a kick out of it when a program
works, still get a buzz when I write a sexy subroutine or component. The day
I don't, is the day I'll quit...

I'm sure many others here feel the same.

Pete






-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-13T19:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD7513E.8B12650B@home.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com> <3AD688FF.3C5A2E62@home.com> <3ad7005b_4@my.newsfeeds.com>`

```


"Peter E. C. Dashwood" wrote:

Just re-read Michael's - can't disagree with a single thing he says.

> Some comments below, but no issues here. Please see also my>
> Are you suggesting that a pass is made to set the flags for the required
> extraction? More information please, Jimmy.
>

You refer to 'ASS-umptions" down below, but hell ! We've got to make some here,
as we only have the Ugly code to go on. (I don't hear the sound of somebody
cutting me a cheque for $160-200 per hour (US dollars please <G>))

So a 'real' example of the above :-

Firstly the 'old' record format :-

       01  VES-RECORD.
           05  VES-KEY.
               10  VES-KEY-NUMBER         PIC X(03).
               10  VES-RECORD-TYPE        PIC X(01).
               10  VES-SUFFIX                      PIC X(01).
           05  VES-IDENTITY-NUMBER    PIC X(10).
           05  VES-NAME                            PIC X(35).
           05  GROUP-TYPE REDEFINES VES-TYPE       PIC X.
           05  VES-REGISTRATION-NUMBER             PIC X(12).
           05  VES-FIRST-ITEM                      PIC 9(06).
           05  VES-LAST-ITEM                       PIC 9(06).

As you can see doesn't do much other than provide descriptive information, so I
didn't include a filler. And back then, not yet into three-tier systems, yours
truly had this format appearing in say some six programs or more. Along comes
user - "If we could 'squeeze' in the Vessel Type (Aerial Cooler, Line Heater,
Vessel with One Boot etc...), then you can produce me different calculations".

So choice, re-compile every damned program using the new format or try and do it
with one. Decided on latter so 'pinched' a character from the description as
follows :-

           05  VES-NAME                          PIC X(34).
           05  VES-TYPE                            PIC X.

This is Eileen's problem times 'n' . Although maybe only some 30 - 50 of these
records per file, there are umpteen files because of Company/Oil-Plant
designation.
So gave user a 'translate' program changing from pic x(35) to pic x(34) and pic
x(1).
And he has to *remember* to do this translation before he attempts to use a set
of files - not a very satisfactory solution - but given a twenty year old
compiler, the best I could come up with.

Now given the same situation with a 'modern' compiler, using F/J or N/E file
CBL_FILE DateTime stamp access, I can get at individual files to check. Still
got to do this conversion, but in my case, I determine the current set of files
being used at the Master Menu - so hard code a 'ChangeDate' into the Master Menu
and I can DateTime check, warning user :-

    - (1) I'm now going to convert your file (putting a space into the Type
code)
    - (2) Now edit the file for valid Vessel Types before processing

Still not foolproof - but better than the old way. There's no logic I can use to
insert his new Vessel Types so I just give him pic x value space. Two options
(1) Edit records individually through the Vessel Edit program, or (2) even
easier, produce an Ascill-delimited (CSV) which allows him to peruse quickly and
edit that one field for all records.

Hope that describes it sufficiently.

>
> Hey, we're not going to revisit the absorbing discussion on File Opens Vs
> Reads again are we...I'll just find my book of Vogon poetry...

Most definitely NOT -  Begin, Open, Process, Close, Finish.

On this one - Judson - I could sit down and write my own (i.e. do my own
homework <G>), but do you have any useful examples or timings showing the
dramatic difference between Open, Process ALL, Close - and - Open, Process this
one, Close, Open, Process this one, Close etc.... ?

> I saw Richard's suggestion re file flags and liked it. Liked even more his
> final summation:
> >
> Watch the verb "to assume", Jimmy. You know the old saying....
>

See above re 'assume'

More assumptions, or guesses. Eileen has just given us the one snippet (Ugly
code), but is this :-

    (a) A General Sales Analysis - if so

        if    NotaSpecialCustomer
              perform Standard-Routine

        else perform Exception-Routine

    (b) Special Customer Sales Analysis - i.e. it is only being done for a few
(?)
    selected accounts - then there might be justification for hard coding a
table -
    as the addition of type codes might only affect 1% of the data files.

Eileen - put us out of our agony - some input please <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-04-14T09:46:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD80E55.9210D7C@Azonic.co.nz>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com> <3AD688FF.3C5A2E62@home.com>`

```
> "Peter E. C. Dashwood" wrote:
> 
…[4 more quoted lines elided]…
> > go away and it won't get re-written (well, not overnight , anyway).

The ugly IF statement appears to be a _programmer's_ solution to the
requirement that some customers/classes/types need to be dealt with in a
special way.  A _designer's_ solution would be to build the conditions
into the database so that they can be changed without recompiling the
programs.  It seems to me that this may have started as a single case
and the analysts/designers passed it down to the coders as too trivial
for proper treatment.  

It has now grown and is not only ugly but is completely untestable.  How
much data is required to test that IF statement for working correctly ? 
How much is actually tested ?  Where is the specification that the code
can be compared to ?

While existing ugly code will still exist, no one will go back and
rewrite it because it may break something, there is no reason to accept
that it is acceptable practice for code in the future.  By making
programmers aware that these cases should be dealt with at the design
level (by introducing special case flags or set of data items) they
should be able to pass the requirement back up to the design level for
review _before_ the code gets ugly.

While it won't go away, there is no need to add more.
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-13T11:59:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2TBB6.49$Yi2.39705@paloalto-snr1.gtei.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com>`

```
Peter E. C. Dashwood <dashwood@enternet.co.nz.nospam> wrote in message
news:3ad674e8_4@my.newsfeeds.com...
> I gave some more thought to this...
>
> While most of the thread is wailing about what awful code it is, and
> speculating about how it came to be and what would be a much better
solution
> (all fine, as far as it goes...) it occurred to me that there is a TON of
> this stuff sitting around on mainframes (and PCs probably...) and it won't
…[13 more quoted lines elided]…
> 1. Does anybody know of any source manipulation packages which can do
this?
>
> 2. Does anybody know of any potential sites where such a tool could be
sold?
> (I guess Eileen's would be one...<G>)
>
> 3. Anybody prepared to help write it, as a spare time back burner project
> with the only return being a share in the profits (if any)?
>

Well, Pete, software designed to create software has been with us since the
'50s, but methinks you have missed something of significance.

Who the hell wrote the "business rule" this software is supposed to support?
Twenty bucks ($US, $NZ or whatever) sez that twenty (quality) minutes with
the business decisionmaker results in better code. Probably would result in
a code something like

EVALUATE TRUE
   WHEN Designated-class
   WHen designated customer
   when designated location-code
     perform xxx
END-EVALUATE

where the "designated" class and customer are tabled lists.

Five bucks (not quite as confident) sez the 'location code'  qualifiers
could come out, too. That looks like old temporary code which was installed
prior to the designated class or customer being assigned to the customer.

I have no idea who the user is or even the industry, but I've seen enough
code like this. Sure looks like, " we'll just hard-code this and fix it
later." Of course, "later" never comes.

Cheap and Dirty gets the programmer home for dinner tonight. Doing it right
gets him home for dinner many more nights, after doing something far more
productive during the day.

What would be more interesting to develop would be some way of trapping how
many times a particular portion of this "rule" is actually invoked. For
example, are there any customers still assigned class 14? Is customer #29876
bankrupt and out of business?

Just as businesses set up periodic reviews of marketing plans, finance
plans, transportation plans, etc, IT managers should schedule periodic
reviews of business logic in code. Unfortunately,  too many managers have a
congenital inability to see beyond the next profit-and-loss statement to
make this small investment.

My $0.02 ($US)

MCM
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-14T04:02:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad727b0_2@my.newsfeeds.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com> <2TBB6.49$Yi2.39705@paloalto-snr1.gtei.net>`

```
Hmmmm....

I agree of course, Michael and your money is safe <G>

I had limited the solution (quite deliberately) to the the constraints that
it must NOT introduce ANYTHING new...that means flags on files,
walkthroughs, meetings with the Business, or anything OTHER than the
EXISTING SOURCE CODE.

Certainly, better solutions are attainable and you are quite right to
question the business rules and who formulated them and when. I have
certainly been in this game long enough to know that, and have even
advocated it quite recently here in CLC  for the resolution of a Database
problem.

No, the fact remains that we do not live in a perfect World. Sometimes ALL
we have is the code. The people who wrote (perpetrated ?) it may be long
gone, business rules have been added to it like Topsy without the time or
inclination or resources to understand it, or try and improve it. So the
"reality" is the code. My speculation was that a tool which could bring some
kind of order to this code MIGHT be useful...(I'm in no particular hurry to
write it but would certainly do so if there's a Market for it...(my stance
on Market Forces is a matter of public record...<G>))

Even if it could make the job of a dedicated maintenance programmer easier
it might be worthwhile. Suppose Eileen had only needed 10% of the time she
spent dealing with this mess... It has to be worthwhile I would've thought,
but I could be wrong. Maybe the Management decision is just "re-write it in
Java". But even that isn't always viable (just as well, really...).

I have no issue with you and what you suggest is certainly better; my only
reservation is that sometimes this is NOT possible...

I'd still appreciate answers to the 3 qustions if anyone is interested.

Pete.

(few more comments below.)


Michael Mattias wrote in message
<2TBB6.49$Yi2.39705@paloalto-snr1.gtei.net>...
>Peter E. C. Dashwood <dashwood@enternet.co.nz.nospam> wrote in message
>news:3ad674e8_4@my.newsfeeds.com...
…[6 more quoted lines elided]…
>> this stuff sitting around on mainframes (and PCs probably...) and it
won't
>> go away and it won't get re-written (well, not overnight , anyway).
>>
…[25 more quoted lines elided]…
>Who the hell wrote the "business rule" this software is supposed to
support?
>Twenty bucks ($US, $NZ or whatever) sez that twenty (quality) minutes with
>the business decisionmaker results in better code. Probably would result in
…[10 more quoted lines elided]…
>

What about combinations of designations, Michael? Like a Customer is only to
be designated when certain classes and locations are in certain combinations
and with other combinations NOT true? This is where Jimmy's decision tables
are extremely useful and you say yourself "tabled lists"... but the tables
still need to be evaluated and the ghost of George Boole is smiling  in the
background  (Me and George go back a long way; he's got me off the hook on
several occasions, not that I know anything about logic, you
understand...<G>)

>Five bucks (not quite as confident) sez the 'location code'  qualifiers
>could come out, too. That looks like old temporary code which was installed
…[13 more quoted lines elided]…
>example, are there any customers still assigned class 14? Is customer
#29876
>bankrupt and out of business?
>
Ah, there are definitely debuggers  and analysers that can do that.

>Just as businesses set up periodic reviews of marketing plans, finance
>plans, transportation plans, etc, IT managers should schedule periodic
…[3 more quoted lines elided]…
>
Absolutely! Couldn't agee more....

>My $0.02 ($US)
>

Worth more than that, I think...<G>

Pete.





-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-04-14T09:53:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD81016.2175AB12@Azonic.co.nz>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <3ad47463_1@anonymous> <3ad674e8_4@my.newsfeeds.com> <2TBB6.49$Yi2.39705@paloalto-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> example, are there any customers still assigned class 14? Is customer #29876
> bankrupt and out of business?

Has that customer been deleted and the number reused for someone
completely different ?
```

#### ↳ Re: Ugly IF Statement

- **From:** "Cliff Peterson" <cliffpeterson@spamcop.net>
- **Date:** 2001-05-10T02:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com>`

```
Eileen,

I can't resist a puzzle - I don't do crosswords, but love this stuff.

I'm just an old code pusher, but how about this?  Not shorter, but perhaps
clearer...

88s to group the cust-no and dest-cd could shorten and simplify as well.

EVALUATE TRUE
WHEN SPECIAL-CHRY-CLS
WHEN AIHD-CUST-NO   = 08221
WHEN AIHD-CUST-NO   = 05659
WHEN AIHD-CUST-NO   = 00879
WHEN AIHD-CUST-NO   = 08228
WHEN AIHD-CUST-NO   = 10418
WHEN AIHD-CUST-NO   = 11010
WHEN AIHD-CUST-NO   = 08288
WHEN AIHD-SALES-CLS = 11
WHEN AIHD-SALES-CLS = 34
WHEN AIHD-SALES-CLS = 35
WHEN AIHD-SALES-CLS = 61
    PERFORM XXXXXX

WHEN AIHD-SALES-CLS = 14
    EVALUATE WS-DEST-CD-1
    WHEN 'AP'
    WHEN 'WE'
    WHEN 'EE'
    WHEN 'EF'
    WHEN 'FD'
    WHEN 'PP'
    WHEN 'CC'
    WHEN 'IE'
        PERFORM XXXXXX
    END-EVALUATE

WHEN AIHD-SALES-CLS = 18
    EVALUATE WS-DEST-CD
    WHEN '48063'
    WHEN '17576'
        PERFORM XXXXXX
    END-EVALUATE

WHEN AIHD-SALES-CLS = 30
    EVALUATE WS-DEST-CD
    WHEN '04179'
    WHEN '12014'
    WHEN 'LSC07'
    WHEN '31   '
        PERFORM XXXXXX
    WHEN OTHER
        EVALUATE AIHD-CUST-NO
        WHEN 09937
        WHEN 10100
        WHEN 10181
        WHEN 10190
        WHEN 11100
        WHEN 09941
        WHEN 09949
        WHEN 10222
        WHEN 01552
        WHEN 11109
        WHEN 10108
            PERFORM xxxxxx
        END-EVALUATE
    END-EVALUATE

END-EVALUATE.



"YukonMama" <yukonmama@aol.com> wrote in message
news:20010410225436.26397.00004167@ng-cf1.aol.com...
> We get a lot of students either posting or lurking here so the other day
while
> working on a particularly nasty program (8000 some lines of spaghetti code
with
> polish logic) I came across this particular IF statement no less than 9
times
> in the program and thought they would like to see what's in store for
them.
>
> This is what you get to see in the real world :)
…[27 more quoted lines elided]…
> There are lower case x's at the PERFORM to indicate that different
paragraphs
> are performed each time the IF appeared in the program.  The paragraphs
were
> identical except for one or two variables from the map (this is a CICS
> program).  These variables are actually an occurance but the map is not
> redefined so each time the field in question is used such as QTY1 or QTY2
the
> paragraph is duplicated.  Makes maintenance a real nightmare.
>
> You will also notice that there are a few ORs that preclude the execution
of
> other ORs (that is it doesn't matter as something before it takes
precedent -
> assignment: see if you can find it).
>
> The fields being tested are in the header record which is read at the
beginning
> of the program.  The IF statement is now reworked and a switch set if
> everything makes it thru the tangle and the switch checked where each of
the
> original IFs were.  Just my part of making this nightmare a bit more
managable.
>
> Eileen
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Ugly IF Statement

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-10T12:25:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net>`

```
Cliff Peterson <cliffpeterson@spamcop.net> wrote in message
news:SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net...
> Eileen,
>
…[4 more quoted lines elided]…
>
 Much clearer! Very nice!

MCM
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-11T12:52:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3afb3b49_2@Usenet.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote in message
<0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net>...
>>
> Much clearer! Very nice!
>
>MCM


Sadly, the original poster may not recognise your irony, Michael.

You WERE being ironic, right? <G>

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-11T12:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y5RK6.87$Qc1.40954@dfiatx1-snr1.gtei.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com>`

```
Peter E. C. Dashwood <dashwood@free.net.nz> wrote in message
news:3afb3b49_2@Usenet.com...
>
> Michael Mattias wrote in message
…[10 more quoted lines elided]…
>

Now you have me wondering.

The no-shit, for-real answer is, I found the nested EVALUATE statement so
much easier to read and understand than the
nested-IF-with-AND-and-OR-and-NOT-and-parentheses version original posted by
Ms. Preston that I just had to say something nice about it.

Of couse, as a critic of programming style and syntax, I am somewhat
hampered by my twenty-plus years' experience in The Real World, where
actually communicating with other human beings was part of the job
description.

MCM
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 4)_

- **From:** "Cliff Peterson" <cliffpeterson@spamcop.net>
- **Date:** 2001-05-14T17:26:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@free.net.nz> wrote in message
news:3afb3b49_2@Usenet.com...
> Michael Mattias wrote in message
> > Much clearer! Very nice!
…[3 more quoted lines elided]…
> Pete.

Pete,

As the "original poster", I have a few comments.

I'm a day-to-day coder, not the Tintoretto of  Cobol.

If I ran across the code originally posted during a maintenance project, I
would NOT...
- rewrite the program,
- restructure the file logic,
- take the previous programmers to task,
- attempt to dazzle the shop with my scintillating intellect.

If I've been asked to change the program, my job is to do just that - not
prove my adherence to the latest Cobol religion.

I WOULD...
- decompose an IF statement into a more readable form if I was having
trouble understanding it (you see the result),
- replace it in the program only if I felt sure I could test the resultant
code within my allocation of hours,
- print it and pin it to my cube wall for next time if I couldn't.

Now...

I submit that my code, in my humble opinion, is easier to read and
understand than the originally posted version and does not intrude on other
functioning code.  My purpose in submitting it was within this context, not
to be sniffed at by Cobol "instructors" for its lack of, well, whatever.

Assuming that the MIS in this shop hasn't personally asked you to beautify
this code, what is your solution, Pete?


Cliff
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-16T03:39:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b015433_5@Usenet.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net>`

```

"Cliff Peterson" <cliffpeterson@spamcop.net> wrote in message
news:ezUL6.22224>
> Pete,
>
> As the "original poster", I have a few comments.
>
> I'm a day-to-day coder, not the Tintoretto of  Cobol.

Now I wonder who that would be...?

>
> If I ran across the code originally posted during a maintenance project, I
…[5 more quoted lines elided]…
>

Good. Neither would I. Possibly the last, but not deliberately...<G>

> If I've been asked to change the program, my job is to do just that - not
> prove my adherence to the latest Cobol religion.
>

I'm a devout Atheist...

> I WOULD...
> - decompose an IF statement into a more readable form if I was having
> trouble understanding it (you see the result),

Is your string of EVALUATES any more readable than the compound IFs? It is
certainly arguable.

> - replace it in the program only if I felt sure I could test the resultant
> code within my allocation of hours,
> - print it and pin it to my cube wall for next time if I couldn't.
>
 I have scantily clad women on mine, but each to his own...

> Now...
>
> I submit that my code, in my humble opinion, is easier to read and
> understand than the originally posted version and does not intrude on
other
> functioning code.

I agree. In fact, having spent much more time on it than I should have, I
almost like it...<G> It certainly meets the criteria above.

> My purpose in submitting it was within this context, not
> to be sniffed at by Cobol "instructors" for its lack of, well, whatever.
…[3 more quoted lines elided]…
>

All very fair comment.  I apologise (genuinely) for thoughtlessly offending
you.

I wasn't "sniffing " at your code for any perceived lack. It is just that
this particular example is so horrible that there is very little that can be
done to improve it.

Certainly substituting a bunch of EVALUATEs for a bunch of IFs doesn't cut
it, at least as far as I'm concerned. As you are obviously miffed, I'll show
you my solution and you can feel free to comment, criticise or generally
"get your own back"  <G>. (If you had read the whole thread you would've
seen it.)

And please don't take it so personally. You really can survive without my
approval...<G>

Here's my response to Eileen:
<start quote>
I thought it was a beautiful IF statement...<G>

It was certainly jolly interesting...

Instead of doing the daily crossword today I resolved to see if it could be
simplified and how much would be gained.

I converted it to symbolic notation, did a Boolean simplification on it (it
would've been MUCH more "interesting" if we had some NOTs in it...<G>) and
arrived at the following, which purports to be logically equivalent (unless
I made a mistake in the simplification or symbol transitions...not
unknown...I haven't time or inclination to check it on my computer so I'll
just risk the red face if it is wrong...)

Anyway, although there are some savings, there are not as many as you might
think when first looking at it...

====================================== Pete's solution ==================
if AIHD-SALES-CLS = 11 OR 34 OR 61 OR 35
                         OR
    SPECIAL-CHRY-CLS
                          OR
    AIHD-CUST-NO = 08221 OR 05659 OR 00879 OR
                     08228 OR 10418 OR 11010 OR
                     08288
                          OR
    (AIHD-SALES-CLS = 14 AND
    (WS-DEST-CD-1 = 'AP' OR 'WE' OR 'EE' OR 'EF' OR 'FD' OR
                                       'PP' OR 'CC' OR 'IE'  OR
    WS-DEST-CD     = 'TC04A' OR 'TC11A' OR '0100A'  ))
                          OR
    (AIHD-SALES-CLS = 30 AND
    (AIHD-CUST-NO  = 09937 OR 10100 OR 10181 OR 10190  OR
                                       11100 OR 09941 OR 09949 OR
                                       10222 OR 01552 OR 11109  OR
                                       10108 OR
     WS-DEST-CD = '04179' OR '12014' OR 'LSC07' OR '31   '))
                            OR
     (AIHD-SALES-CLS = 18 AND
      (WS-DEST-CD = '48063' OR '17576'))
        perform XXXX
end-if
===================== End Pete's solution - 24 lines =====================
I am NOT proposing that the above is "elegant" code, but at least it has
removed the redundant tests (or it should have, if I got my sums
right...<G>). This in turn removes the "precedence" which someone else in
the thread has already identified.

In an on-line environment the tests could be prioritised and shuffled around
the "OR"s so that the most likely events were tested for first; in Batch, it
really doesn't matter...

I agree that a better approach would be to break it down and derive "logic
values" which could be tested.

Thanks for an interesting 20 minutes...<G>

Pete.
======================= Eileen's original =================================
YukonMama wrote in message <20010410225436.26397.00004167@ng-cf1.aol.com>...
>We get a lot of students either posting or lurking here so the other day
while
>working on a particularly nasty program (8000 some lines of spaghetti code
with
>polish logic) I came across this particular IF statement no less than 9
times
>in the program and thought they would like to see what's in store for them.
>
>This is what you get to see in the real world :)
>
================= Very nasty person on Eileen's site solution ==============
>IF (AIHD-SALES-CLS = 11 OR 34 OR 61) OR
>    ((AIHD-SALES-CLS = 14 OR  35) AND
…[22 more quoted lines elided]…
>END-IF
======================== End very nasty "solution"   - 25 lines
================
>
>There are lower case x's at the PERFORM to indicate that different
paragraphs
>are performed each time the IF appeared in the program.  The paragraphs
were
>identical except for one or two variables from the map (this is a CICS
>program).  These variables are actually an occurance but the map is not
>redefined so each time the field in question is used such as QTY1 or QTY2
the
>paragraph is duplicated.  Makes maintenance a real nightmare.
>
>You will also notice that there are a few ORs that preclude the execution
of
>other ORs (that is it doesn't matter as something before it takes
precedent -
>assignment: see if you can find it).
>
>The fields being tested are in the header record which is read at the
beginning
>of the program.  The IF statement is now reworked and a switch set if
>everything makes it thru the tangle and the switch checked where each of
the
>original IFs were.  Just my part of making this nightmare a bit more
managable.
>
>Eileen
>
===================== Cliff's solution  ==========================
EVALUATE TRUE
WHEN SPECIAL-CHRY-CLS
WHEN AIHD-CUST-NO   = 08221
WHEN AIHD-CUST-NO   = 05659
WHEN AIHD-CUST-NO   = 00879
WHEN AIHD-CUST-NO   = 08228
WHEN AIHD-CUST-NO   = 10418
WHEN AIHD-CUST-NO   = 11010
WHEN AIHD-CUST-NO   = 08288
WHEN AIHD-SALES-CLS = 11
WHEN AIHD-SALES-CLS = 34
WHEN AIHD-SALES-CLS = 35
WHEN AIHD-SALES-CLS = 61
    PERFORM XXXXXX

WHEN AIHD-SALES-CLS = 14
    EVALUATE WS-DEST-CD-1
    WHEN 'AP'
    WHEN 'WE'
    WHEN 'EE'
    WHEN 'EF'
    WHEN 'FD'
    WHEN 'PP'
    WHEN 'CC'
    WHEN 'IE'
        PERFORM XXXXXX
    END-EVALUATE

WHEN AIHD-SALES-CLS = 18
    EVALUATE WS-DEST-CD
    WHEN '48063'
    WHEN '17576'
        PERFORM XXXXXX
    END-EVALUATE

WHEN AIHD-SALES-CLS = 30
    EVALUATE WS-DEST-CD
    WHEN '04179'
    WHEN '12014'
    WHEN 'LSC07'
    WHEN '31   '
        PERFORM XXXXXX
    WHEN OTHER
        EVALUATE AIHD-CUST-NO
        WHEN 09937
        WHEN 10100
        WHEN 10181
        WHEN 10190
        WHEN 11100
        WHEN 09941
        WHEN 09949
        WHEN 10222
        WHEN 01552
        WHEN 11109
        WHEN 10108
            PERFORM xxxxxx
        END-EVALUATE
    END-EVALUATE
END-EVALUATE.

======================== end Cliff's solution - 56 lines==============

My Choice?

NONE of the above!

I WILL however, agree that your solution is much better than the
original...<G>

(Actually, in the course of writing this it has kind of grown on me, and I
like it much more now than I did at the start... <G>  I still think all
three solutions stink: the only thing mine has going  for it is that it is
mathematically "pure"; it certainly isn't a fine example of how to write
COBOL).

Cliff, it is only computer programming, not life and death... your value as
a person does not depend on your code, any more than mine does. (Just as
well in my case...<G>)

Can we be friends now <G>?

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 6)_

- **From:** "Cliff Peterson" <cliffpeterson@spamcop.net>
- **Date:** 2001-05-15T23:45:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kcjM6.25385$t12.1914316@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net> <3b015433_5@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:
> My Choice?
>
> NONE of the above!

Nope - you gotta choose...;-)

> I WILL however, agree that your solution is much better than the
> original...<G>

Thanks, I think...

> (Actually, in the course of writing this it has kind of grown on me, and I
> like it much more now than I did at the start... <G>

I grow on you... actually, I like the idea of being able to tabulate the IF,
letting me see what's what.  I'm just a sucker for indentation...:-)

> Can we be friends now <G>?

Well..... you bet.  Sorry to be a little testy - us old geezers need our
sleep or we get cranky - right, DD?

Cheers,
Cliff
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-05-17T09:59:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0392EE.AE8839FB@Azonic.co.nz>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net>`

```
Cliff Peterson wrote:
> 
> I submit that my code, in my humble opinion, is easier to read and
…[5 more quoted lines elided]…
> this code, what is your solution, Pete?

All these 'solutions' may be very much better than the original, but
they all miss the point entirely: Data items are being built into the
code.  To test this IF statement properly it would be necessary to give
it data with every combination of values and to check each of several
thousand results.

The only usable solution is to have a flag in the customer record, the
class record and the destination (DEST?) record and have these set by
whoever cares about the outcome of the IF.  Then the system need not be
rebuilt everytime there is a change in the status of a customer, nor the
necessity of retesting the system.

As an interim step the code could be changed such that the IF statement
is coded as if these flags are in the data and the values that are
currently in the IF can be taken out to a separate set of tests:

   IF (AIHD-CUST-NO = 08221 OR 05659 OR 00879 OR
                      08228 OR 10418 OR 11010 OR
                      08288)
	MOVE "ALWAYS"		TO AIHD-CUST-Process
   ELSE
   IF (AIHD-CUST-NO = 09937 OR 10100 OR 10181 OR 10190
                            OR 11100 OR 09941 OR 09949
                            OR 10222 OR 01552 OR 11109
                            OR 10108)
	MOVE "GRP02"           TO AIHD-CUST-Process
   ELSE
   IF ( AIHD-CUST-NO = ..
        MOVE "GRP42"           TO ...
   ELSE
        MOVE "NEVER"           TO ...
   END-IF
   END-IF
   END-IF

   IF ( AIHD-SALES-CLASS = 11 OR 34 OR 61 )
        MOVE "CLSON"           TO AIHD-SALES-Process
     ....

The purpose of this is to give meanings to the groups of data items so
that the problem can be understood as a _business_ solution.  Those
customers must be of a specific set of types.  For example they have
signed a particular trade agreement or non-disclosure.  They are
'special' in some way(s).  This should be in the customer record as a
value or even a group of values to memorialise this.  Then it can also
be shown on the enquirey screen and changed as required.

The Sales Class, too, is some sort of special set of products perhaps. 
Why is the class record, or the product records not indicating this fact
?

If it is impossible to change the data records then set up a text file
with, say:

     *CUSTOMER=ALWAYS
     08221 
     ...
     *CUSTOMER=GRP02
     10100
     10181
     *CLASS=ALWAYS
     11
 
Read this into tables and apply tests to set a group of flags or 88
levels.

Once the _business_ model is understood and implemented then the code
can be written in terms of that model using meaningful values instead on
anonymous codes.

A decision table should then be used to establish how the flags fit into
whether the processing is done or not.

The savings that this will give are:

     Reduction in testing to samples of each setting.
     The data list and decision table can be verified
        and/or changed by those that care *.
     The system won't be rebuilt everytime there is a
        new customer or product.

  * I am assuming that the programmer neither knows nor
    cares who the customers actually are or why they 
    get this special processing, but the marketing or
    sales manager will, so may the development or
    production manager.
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-05-17T01:55:54+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o216gtgtfuuf1eun0irku89uj172s0e499@4ax.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net> <3B0392EE.AE8839FB@Azonic.co.nz>`

```
On Thu, 17 May 2001 09:59:26 +0100 Richard Plinston <riplin@Azonic.co.nz>
wrote:

:>Cliff Peterson wrote:
 
:>> I submit that my code, in my humble opinion, is easier to read and
:>> understand than the originally posted version and does not intrude on other
:>> functioning code.  My purpose in submitting it was within this context, not
:>> to be sniffed at by Cobol "instructors" for its lack of, well, whatever.
 
:>> Assuming that the MIS in this shop hasn't personally asked you to beautify
:>> this code, what is your solution, Pete?

:>All these 'solutions' may be very much better than the original, but
:>they all miss the point entirely: Data items are being built into the
:>code.  To test this IF statement properly it would be necessary to give
:>it data with every combination of values and to check each of several
:>thousand results.

:>The only usable solution is to have a flag in the customer record, the
:>class record and the destination (DEST?) record and have these set by
:>whoever cares about the outcome of the IF.  Then the system need not be
:>rebuilt everytime there is a change in the status of a customer, nor the
:>necessity of retesting the system.

The problem with such a solution is that how many flags will you be adding to
the record, i.e., how complex a conditional statement do you need before you
add the flag?

   [ snipped ]
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-05-21T12:24:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B08FAF5.580733C5@Azonic.co.nz>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net> <3B0392EE.AE8839FB@Azonic.co.nz> <o216gtgtfuuf1eun0irku89uj172s0e499@4ax.com>`

```
Binyamin Dissen wrote:

> :>All these 'solutions' may be very much better than the original, but
> :>they all miss the point entirely: Data items are being built into the
…[11 more quoted lines elided]…
> the record, 

1) Enough to satisfy the _business_model_.  It is the complexity of how
the customers, sales classes, and other items need to be described that
should determine this.  Currently the business model is not even
embodied in the IF syatement, just a series of apparently unconnected
codes tied together in various combinations or ANDs and ORs.

If the business model is actually investigated then there may, in fact,
be simplifications that could never be apparent from the IF statement.

What does it all mean ?

2) "None", if my alternate scheme of setting the flags for groups of
codes using separate IF statements to preset the flags in WS is used.
eg:

      SET Customer-Normal     TO TRUE
      IF ( Customer-Code = lsit of anonymous codes 1 )
           SET Customer-Beta-Tester     TO TRUE
      ELSE
      IF ( Custome-Code = list of codes 2 )
           SET Customer-Alpha-Tester    TO TRUE
        etc    
     
3) "None" if my alternate scheme of describing these codes in a text
file is used.

> i.e., how complex a conditional statement do you need before you
> add the flag?

The resulting conditional statement need not be more complex at all.  If
will in fact become simpler to understand.  Instead of:

      IF (customer code is one of anonymous list)

it becomes:

      IF ( customer is of type )

and this can be a direct 1:1 replacement in the original IF of a list of
codes by a type comparison.

Why would it be 'more complex' ?
```

###### ↳ ↳ ↳ Re: Ugly IF Statement

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-17T12:13:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b031a8d_4@Usenet.com>`
- **References:** `<20010410225436.26397.00004167@ng-cf1.aol.com> <SfnK6.13740$4f7.1067825@bgtnsc06-news.ops.worldnet.att.net> <0NvK6.228$uV4.28222@dfiatx1-snr1.gtei.net> <3afb3b49_2@Usenet.com> <ezUL6.22224$4f7.1763596@bgtnsc06-news.ops.worldnet.att.net> <3B0392EE.AE8839FB@Azonic.co.nz>`

```
This is very valid, Richard.

I believe Eileen has used flags to try and simplify this tangle, but these
may be flags within the program rather than flags on the data.

I agree that it would be better to flag the data.

Sometimes, when it comes to maintenance though, altering the existing data
is just not an option.

Pete.
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B0392EE.AE8839FB@Azonic.co.nz...
> Cliff Peterson wrote:
> >
> > I submit that my code, in my humble opinion, is easier to read and
> > understand than the originally posted version and does not intrude on
other
> > functioning code.  My purpose in submitting it was within this context,
not
> > to be sniffed at by Cobol "instructors" for its lack of, well, whatever.
> >
> > Assuming that the MIS in this shop hasn't personally asked you to
beautify
> > this code, what is your solution, Pete?
>
…[85 more quoted lines elided]…
>     production manager.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
