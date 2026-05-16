[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Strange result : I lost one record

_42 messages · 7 participants · 2006-07_

---

### Strange result : I lost one record

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-21T13:52:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9qf6t$bjv$1@s1.news.oleane.net>`

```
Hello,

I've got a file "fgctar". When I read it sequentially, I obtain this

KEY 	| VALUE
...
152001 	| MyRecord1
153001 	| MyRecord2
153153 	| MyRecord3
154001 	| MyRecord4
154154 	| MyRecord5
155001 	| MyRecord6
156001 	| MyRecord7
156156 	| MyRecord8
...

I've got another file "fgcart", the primary key is composed by the first 
three digits of the primary key of my first file "fgctar". When I read 
it, i've got something like this :

KEY 	| NAME
...
152 	| Name1
153 	| Name2
154 	| Name3
155 	| Name4
156 	| Name5
...

Then I read the second file "fgcart" sequentially and I search in the 
first file "fgctar" all records for which primary key of fgcart  match 
primary key of fgctar and I've got this result

KEY 	| NAME		| VALUE
...
152001 	| Name1		| MyRecord1
153001 	| Name2		| MyRecord2
153153 	| Name2		| MyRecord3
154001 	| Name3		| MyRecord4
155001 	| Name4		| MyRecord6
156001 	| Name5		| MyRecord7
156156 	| Name5		| MyRecord8
...

So, the record "154154 MyRecord5" disappeared.

Has someone an idea ?

Jerome
```

#### ↳ Re: Strange result : I lost one record

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-21T12:04:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9qft6$o9u$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net>`

```
In article <e9qf6t$bjv$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:

[snip]

>Then I read the second file "fgcart" sequentially and I search in the 
>first file "fgctar" all records for which primary key of fgcart  match 
>primary key of fgctar

Please pardon the midsentence interruption here... how, in COBOL, do you 
'search the first file (for) all records' with a matching fractional key?

[snip]

>Has someone an idea ?

Yes... my idea is that you post the code which answers the question I 
posed above, as a START.

DD
```

##### ↳ ↳ Re: Strange result : I lost one record

- **From:** epc8@juno.com
- **Date:** 2006-07-22T09:10:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153584654.976174.253550@p79g2000cwp.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <e9qft6$o9u$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <e9qf6t$bjv$1@s1.news.oleane.net>,
> Jerome  <j.aubert1@free.fr> wrote:
…[17 more quoted lines elided]…
> DD

As Ernie Harwell might say, at this point the OP is "loooooooooooooong
gooooooooooone".

But it is not that hard to solve because the fractional key occupies
the leading characters of the key. In addition, the OP can simplify his
program by reading one of the indexed files sequentially.

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-22T22:08:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9u7lr$8cs$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <e9qft6$o9u$1@reader2.panix.com> <1153584654.976174.253550@p79g2000cwp.googlegroups.com>`

```
In article <1153584654.976174.253550@p79g2000cwp.googlegroups.com>,
 <epc8@juno.com> wrote:
>docdwarf@panix.com wrote:
>> In article <e9qf6t$bjv$1@s1.news.oleane.net>,
…[19 more quoted lines elided]…
>gooooooooooone".

Ah well... my habits of bathing, or lack thereof, might be responsible.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-22T23:09:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<meywg.220094$Mn5.50841@pd7tw3no>`
- **In-Reply-To:** `<1153584654.976174.253550@p79g2000cwp.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <e9qft6$o9u$1@reader2.panix.com> <1153584654.976174.253550@p79g2000cwp.googlegroups.com>`

```
epc8@juno.com wrote:
> docdwarf@panix.com wrote:
> 
…[30 more quoted lines elided]…
>

#2 - His problem

I agree with your comments. I don't recall but you may have been the 
person who gave observations/corrections to his program, One thing I did 
notice though was that he had the same External name for two of his 
files - possibly a typo ?.

Somebody from Brazil asked, "How can you program the Help File feature 
that comes with Windows ?". Response he got from M/F was, "Use Activex".
Having already designed generic support classes for file/Table handling 
and GUI-ing, it didn't seem a big deal to me. (Ironically one of the M/F 
examples going back to VISOC the precursor to Net Express, has this 
SEARCH technique).

So produce a Help File Listbox and "setContents" using a Sorted 
Collection. Now user has a text entry field to enter one or more 
characters and using method "wantAllKeys" the event returns keystrokes 
to-date, after each keystroke.

Assume Listbox contains -

Gorgonzola
Gouda

For following checking, turn BOTH the input text and the Listbox entry 
(element) to either Uppercase or Lowercase for comparison purposes.

a) user enters "G" (search input (1:1) against Listbox entries (1:1) 
then highlight Gorgonzola. (If there aren't any "Gs" - nothing happens).
b) same happens when user continues and enters "Go" - (1:2)
c) User enters "Gou" - (1:3) - now Gouda gets highlighted - if that's 
the one the user wants he/she clicks on the Listbox row and the demo 
program using the index position for that row displays "You selected Gouda".

Why go buy an Activex/Cmponent, when the only addition required was the 
Search coding.

Using a fixed RefMod as applies to the OP's files - should be even simpler.

(Funnily enough my wife was watching TV this morning and there was a 
topic about the 20-35 age group getting into text messaging as opposed 
to e-mail and using abbreviations - TTYL, LOL etc., yet people quizzed 
didn't recognize IMHO (In My Humble Opinion you are an asshole and this 
is the way it should be done). Confession - I haven't a bloody clue what 
OP really means :-) Absolute wild guess on reflection, OP = Other Person ?)

# 1 - Acknowledgment

Oh so true ! How many times a half-baked question is phrased, it is 
assummed you know that they are working on big iron or a PC or perhaps 
in that centrifugal tunnel at CERN. It's sometimes left to you to figure 
out which compiler and version number. If you are real lucky, they are 
actually writing about COBOL.

They have a problem and,  "I'm getting the following sorts of errors.... 
  So, this is what is happening.....". So not knowing the problem they 
can  somehow figure out what is causing it, so that they can provide us 
with as litttle informaton as possible (obfuscation).

What happened to communicaton ? Some four decades ago I go into this 
racket as a Systems Analyst - and that resulted in the observation that 
EDP, (let's be politically correct "IT"), was the automation of paper 
shuffling; and taking that process, cutting out the irrelvant bumph and 
making the operation slicker and cheaper. Cheaper. Hmmm. Have we helped 
reduce the paper flow ? (Note to self - "Invest some money in the BC 
lumber/paper mill  industry").

Some queries are from individuals - cottage industry workers; on the 
other hand they quite often could be working at an installation where 
there are other warm bodies also programming. A has a problem. Why 
doesn't he ask B who sits three feet from him ? As a general rule, I 
can't believe his co-workers would be anti to being asked questions. So 
I tend to conclude it is A's self worth - doesn't want to admit he 
doesn't know, so comes here in a vague way, asking for help and hopes 
that if one or two of us throw some runes, we will come up with the 
answer *he/she* wants.

If A asks B a quick question, off-hand he will get a suggested solution. 
Two dayas later A stilll doen't have it figured out. So in the nicest 
possible way he asks B to help with the problem. B's response this time, 
"Show me your source". How novel. But when it comes to asking us, 
short-change us where we are supposed to guess without some inkling of 
what is in the source listing.

A classic was the recent query on moving a combined FirstName/LastName 
field into separate First Name and Last Name fields. Answer - there is 
no known generic way of doing this. Observation - the OP is using the 
Net to get into clc. How many times has he signed up for something on 
the Net where it just asks for "your name" - 99.999% of the time, as a 
minimum you are requested to enter as separate fileds you First Name and 
then your Last Name. The problem goes back to the original design and 
not trying to shuffle the 'unknown' into 'known' fields. (The 
alternative of course is Corporate Name - any applicaton allowing for 
personal names or a corporate name probably requires re-definition of 
the name fileds).

Perhaps for their sin of taking programmng up as a career, new graduates 
should be forced to do a year of penance in Purgatory - i.e., shuffling 
bits of paper in an office !

Of course a quick "Thank You" doesn't hurt. We've had a couple recently 
- but they are preety rare.

Jimmy
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 4)_

- **From:** epc8@juno.com
- **Date:** 2006-07-22T19:11:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153620715.182694.257550@h48g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153584654.976174.253550@p79g2000cwp.googlegroups.com> <meywg.220094$Mn5.50841@pd7tw3no>`

```

James J. Gavan wrote:
> epc8@juno.com wrote:
> > docdwarf@panix.com wrote:
…[38 more quoted lines elided]…
> files - possibly a typo ?.

I found the original program so hard to follow that I ran off a program
listing and started marking it up in pencil. Having files FGCTAR and
FGCART did not help either. My suggestions were somewhat off the mark
but I did point out that searching a file repeatedly for all possible
variations of a partial key instead of using the partial key directly
was not the way to go.

[snip discussion on search techniques]

Confession - I haven't a bloody clue what
> OP really means :-) Absolute wild guess on reflection, OP = Other Person ?)

Original Poster, I think. In CLC maybe it is Original Pest? :-).

>
> # 1 - Acknowledgment
…[12 more quoted lines elided]…
> What happened to communicaton ?

Yes, this I think is the key idea. Back in ye olde days computer
resources were centralized. In a typical computing center people
gathered to punch cards, wait for their jobs to run, and to look at
their print outs. So programming was partly a social activity. Asking
others for help or helping others, or sitting down with a program
listing and a pencil, was common.

Now people have enormous computing power on their desktops so they can
work or study alone. But they also have the resources of the internet.

It bothers me that people who are obviously using the internet to post
don't have the knowledge or the time or the inclination to read or do a
google groups search or a web search before posting. I'm old enough to
start blathering about instant gratificaton, etc. but I won't.

Second, it amazes me that many people are not taught how to solve
problems. They don't know how to formulate a problem succinctly. They
don't know how to gather and present relevant information to others
which makes the problem solving process easier. They don't know how to
narrow down their problem to a small test case, etc.

Instead someone posts a long program listing, some rubbish output, and
asks "What's wrong with my program?"

[flame on] Perhaps it is sun spots, better nutrition or earlier puberty
if you will, but I think part of the blame lies in the de-emphasis in
education on math and science. IMO students do not learn that some
questions do have right answers and that there are situations where you
can't get something for nothing. [flame off]

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-23T02:59:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9uomg$j73$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153584654.976174.253550@p79g2000cwp.googlegroups.com> <meywg.220094$Mn5.50841@pd7tw3no> <1153620715.182694.257550@h48g2000cwc.googlegroups.com>`

```
In article <1153620715.182694.257550@h48g2000cwc.googlegroups.com>,
 <epc8@juno.com> wrote:

[snip]

>I'm old enough to
>start blathering about instant gratificaton, etc. but I won't.

[snip]

>[flame on] Perhaps it is sun spots, better nutrition or earlier puberty
>if you will, but I think part of the blame lies in the de-emphasis in
>education on math and science. IMO students do not learn that some
>questions do have right answers and that there are situations where you
>can't get something for nothing. [flame off]

... an' don't git me started 'bout what them kids're callin' 'music' 
nowadays, neither... buncha durned *noise*, 'f ya ask me... an' another 
thing, what about them clothes they're wearin'?  Ain't they got no mothers 
t' shame 'em?

... an' th' language they use... buncha nonsense, every word... 'Daddy-o' 
an' 'hey-bob-a-ree-bop' an' 'it's a real blast'... an' those fool 'sock 
hops', where'd they git th' idea fer such foolishment?

... an' another thing!... zzzzzzzzz

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 6)_

- **From:** epc8@juno.com
- **Date:** 2006-07-22T20:59:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153627181.705171.123850@i42g2000cwa.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153584654.976174.253550@p79g2000cwp.googlegroups.com> <meywg.220094$Mn5.50841@pd7tw3no> <1153620715.182694.257550@h48g2000cwc.googlegroups.com> <e9uomg$j73$1@reader2.panix.com>`

```

docdwarf@panix.com wrote:
> In article <1153620715.182694.257550@h48g2000cwc.googlegroups.com>,
>  <epc8@juno.com> wrote:
…[25 more quoted lines elided]…
> DD

Well, OK. I've temporarily slipped into old f*rt mode.

It just gets harder to participate in this NG when from time to time an
OP vanishes into a puff of smoke, leaving behind a program where the
best answer to "How do I fix this?" might be "Tear it up and start
over."

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-23T12:54:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9vri0$4ab$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153620715.182694.257550@h48g2000cwc.googlegroups.com> <e9uomg$j73$1@reader2.panix.com> <1153627181.705171.123850@i42g2000cwa.googlegroups.com>`

```
In article <1153627181.705171.123850@i42g2000cwa.googlegroups.com>,
 <epc8@juno.com> wrote:
>
>docdwarf@panix.com wrote:
…[6 more quoted lines elided]…
>> >start blathering about instant gratificaton, etc. but I won't.

[snip]

>> ... an' another thing!... zzzzzzzzz
>
>Well, OK. I've temporarily slipped into old f*rt mode.

Happens to some folks, I believe, if they live long enough... and some 
others even if they don't.

>
>It just gets harder to participate in this NG when from time to time an
>OP vanishes into a puff of smoke, leaving behind a program where the
>best answer to "How do I fix this?" might be "Tear it up and start
>over."

It gets difficult to do that on the job, too, when the orders assume the 
ancient 'there'll be time to do it over but there isn't time to do it 
right'... part o' life, from what I've seen.

DD
```

#### ↳ Re: Strange result : I lost one record

- **From:** epc8@juno.com
- **Date:** 2006-07-21T07:43:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153493019.011833.273860@m73g2000cwd.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net>`

```

Jerome wrote:
> Hello,
>
…[46 more quoted lines elided]…
> Jerome

** Editorial comments **

1. It would help to post your problem and program listing with copy
members expanded in one post.

2. It would help to give your file identifiers more meaningful names.

3. It is also confusing that these identifiers are *anagrams*.

** End editorial comments **

** expanded program listing inserted **

       INPUT-OUTPUT SECTION.
        FILE-CONTROL.
            SELECT FGCTAR ASSIGN TO RANDOM "fgctar01"
               ORGANIZATION INDEXED
               ACCESS DYNAMIC
               RECORD KEY GCTAR-CLE
               STATUS ST-GCTAR.
            SELECT FGCART ASSIGN TO RANDOM "fgcart01"
               ORGANIZATION IS INDEXED
               ACCESS IS DYNAMIC
               RECORD KEY IS GCART-CLE
               ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES
                FILE STATUS IS FichierStatus.
            SELECT OUTART ASSIGN TO RANDOM "out-ess.txt"
                ORGANIZATION IS LINE SEQUENTIAL.
        DATA DIVISION.
        FILE SECTION.
       *    COPY "FGCART.CPY".
        FD  FGCART LABEL RECORD STANDARD.
        01  GCART-FILE.
            02 GCART-CLE.
               04 GCART-NUM       PIC X(12).
       *    COPY "FGCTAR.CPY".
        FD  FGCTAR LABEL RECORD STANDARD.
        01  GCTAR-FILE.
            02 GCTAR-CLE.
               04 GCTAR-ART       PIC X(12).
               04 GCTAR-TAR       PIC 999.
        FD OUTART LABEL RECORD STANDARD.
        01 OUT-ART.
            02 OUT-CLE          PIC X(12).
            02 SEPAR2                   PIC X(1).
       *     02 OUT-INTITULE         PIC X(30).
            02 SEPAR3                   PIC X(1).
            02 OUT-PUHT         PIC 9(6).9(2).
            02 SEPAR4                   PIC X(1).
       *            02 OUT-PUTTC        PIC 9(6).9(2).
            02 SEPAR5                   PIC X(1).
            02 OUT-TAR.
                04 OUT-CLEART   PIC X(12).
                04 OUT-CLETAR  PIC 9(3).

        WORKING-STORAGE SECTION.
        01 FichierStatus        PIC X(2).
        01 ST-GCTAR             PIC X(2).
            88 RecordFound      VALUE "00".
        01 cpt                  PIC 9(3) VALUE 000.
        01 tmp                  PIC 9(6).9(2).

        01 FLAGTROUVE           PIC 9 VALUE 0.

        PROCEDURE DIVISION.
        TRAITEMENT SECTION.
        DEBUT.
            OPEN INPUT FGCART.
            OPEN INPUT FGCTAR.
            OPEN OUTPUT OUTART.

            MOVE ";" TO SEPAR2 SEPAR3 SEPAR4 SEPAR5.

            PERFORM UNTIL GCART-CLE = HIGH-VALUES
            MOVE LOW-VALUES TO GCART-CLE
            START FGCART
                KEY IS GREATER THAN GCART-CLE
                INVALID KEY MOVE HIGH-VALUES TO GCART-CLE
            END-START
            PERFORM UNTIL GCART-CLE = HIGH-VALUES
            READ FGCART
                NEXT RECORD
                 AT END MOVE HIGH-VALUES TO GCART-CLE
                 NOT AT END
       * Lecture du 2eme fichier
                    MOVE GCART-CLE TO GCTAR-ART
                    MOVE 000 TO GCTAR-TAR
                    MOVE 0 TO FLAGTROUVE
       * Balayage de toutes les valeurs possibles de GCTAR-TAR
                    PERFORM VARYING cpt FROM 1 BY 1 UNTIL cpt = 999
                    MOVE cpt TO GCTAR-TAR
                    READ FGCTAR
                        INVALID KEY CONTINUE
                    END-READ
                    IF GCTAR-CLE = "154         154"
                        DISPLAY ST-GCTAR
                    END-IF
                    IF RecordFound
                         MOVE 1 TO FLAGTROUVE
                         MOVE GCART-CLE TO OUT-CLE
                         MOVE GCTAR-CLE TO OUT-TAR
                         MOVE GCTAR-PUHT TO OUT-PUHT
                          WRITE OUT-ART
                    END-IF
                    END-PERFORM
       * Si on a pas trouvé d'enregistrement
                    IF FLAGTROUVE = 0
                         MOVE GCART-CLE TO OUT-CLE
                         MOVE GCTAR-CLE TO OUT-TAR
                         MOVE GCTAR-PUHT TO OUT-PUHT
                          WRITE OUT-ART
                     END-IF

       * Fin de traitement du 2eme fichier
            END-READ
            END-PERFORM
            END-PERFORM

            CLOSE FGCART.
            CLOSE FGCTAR.
            CLOSE OUTART.
        FIN-TRAITEMENT SECTION.

        SORTIE SECTION.
        AFFICHAGE.
            DISPLAY "Fin du traitement ", ST-GCTAR.
        FIN-SORTIE SECTION.

** end expanded program listing **

Using database terminology, you are joining two tables. Let's call
GCART your name table and GCTAR your transaction table.

1. You are using an alternate key on your name table. There is only one
key, the name_id_number. Second, the identifier GCART-NOM does not
exist in your program. Third you are declaring it WITH DUPLICATES but
the keys in the name table are unique.

2. For each record in the name table you access the transaction table
999 times looking for all possible keys. So it really does not matter
why your program does not work properly.

I suggest you try one of two things.

1. make the key on the transaction file just the first three characters
and use WITH DUPLICATES on that key. For each record in the name file,
look up all matching records in the transaction file.

2. You may want to process these tables differently. It depends on the
relative sizes of the files and other factors. For each record in the
transaction table, look up the name in the name table. If it exists,
output a detail record, otherwise do something else, perhaps nothing.

-- elliot
```

##### ↳ ↳ Re: Strange result : I lost one record

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-24T10:51:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea21mk$sh8$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153493019.011833.273860@m73g2000cwd.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com>`

```
epc8@juno.com a ï¿½crit :

> 
> I suggest you try one of two things.
…[11 more quoted lines elided]…
> 

Thanks a lot for your answer. I'm not the original programmer and i'm 
not a cobol programmer so I'm lost. But your analyse will be very helpfull.

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-24T09:41:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea24kb$cql$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea21mk$sh8$1@s1.news.oleane.net>`

```
In article <ea21mk$sh8$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:
>epc8@juno.com a �crit :
>
>> 
>> I suggest you try one of two things.

[snip]

>
>Thanks a lot for your answer. I'm not the original programmer and i'm 
>not a cobol programmer so I'm lost.

I suggest you try one of the following:

1) Tell your boss that if he put a carpenter to work building brick walls 
then the house might fall down.

2) Realise that if your boss insists on putting a carpenter to work 
building brick walls that the strength of the house that results is, 
obviously, not very important.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** epc8@juno.com
- **Date:** 2006-07-24T07:11:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153750274.512757.263680@p79g2000cwp.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea21mk$sh8$1@s1.news.oleane.net>`

```
Jerome wrote:
> epc8@juno.com a écrit :
>
…[20 more quoted lines elided]…
> Jerome

See http://en.wikipedia.org/wiki/JOIN for a relevant discussion.
(Sorry. I could not find a comparable article at fr.wikipedia.org.)
While there is a "Java for Cobol Programmers" book I don't know of a
"Cobol for Some_other_language Programmers book". Thane Hubbell's
"Teach Yourself Cobol in 24 Hours" (Sams) does present an introduction
to COBOL. See the chapters on INDEXED file processing. (Murach
publishes professional level books on COBOL.)

After thinking about the problem some more, my strategy changed
somewhat. The major features are to read the name file sequentially and
look up records with a matching key in the transaction file. Since the
3 digit name-id-number occupies the first three characters of the 6
digit key in the transaction file, you can search the second file using
a query that consists of the first 3 digits followed by 3 spaces.
(Moving a shorter data item to a larger one pads right with spaces - if
you define these fields as character (X) rather than numeric (9).)

So first here is some pseudo code:

for each record in the name file
   position the record pointer in the transaction file to key greater
or equal
   to "nnn<space><space><space>"
   while name-id-from-name-file matches first-3-characters-of-long-key
do
     output detail record to output file

Here is some COBOL using a compiler comparable to the original source
code. Variable names and field lengths are my own choices. Note that my
program does no real error checking and it does no file status checking
as it really should do....

       identification division.
       program-id. join.
       environment division.
       configuration section.
       source-computer. ibm-pc.
       object-computer. ibm-pc.
       input-output section.
       file-control.
           select name-file assign to disk 'name.dat'
             organization is indexed
             record key is name-key.
           select trans-file assign to disk 'trans.dat'
             organization is indexed
             access mode is dynamic
             record key is trans-key.
           select out-file assign to disk 'out.txt'
             organization is line sequential.
       data division.
       file section.
       fd name-file.
       01 name-rec.
         05 name-key pic x(3).
         05 name-data pic x(5).
       fd trans-file.
       01 trans-rec.
         05 trans-key.
           10 trans-name-id pic x(3).
           10 trans-num pic x(3).
         05 trans-data pic x(9).
       fd out-file.
       01 out-rec.
         05 out-key pic x(6).
         05 filler pic x.
         05 out-name pic x(5).
         05 filler pic x.
         05 out-data pic x(9).
       working-storage section.
       01 flags.
         05 name-eof pic x value 'n'.
         05 trans-eof pic x.
         05 key-not-found pic x.
       procedure division.
       main.
           open input name-file
           open input trans-file
           open output out-file
           move all '|' to out-rec
           perform until name-eof is equal to 'y'
             read name-file
               at end
                 move 'y' to name-eof
               not at end
                 perform get-match
             end-read
           end-perform
           close name-file
           close trans-file
           close out-file
           stop run.
       get-match.
           move name-key to trans-key
           start trans-file key not < trans-key
             invalid key
               move 'y' to key-not-found
             not invalid key
               move 'n' to trans-eof
               move 'n' to key-not-found
               perform until trans-eof is equal to 'y'
               or key-not-found is equal to 'y'
                 read trans-file next record
                   at end
                     move 'y' to trans-eof
                   not at end
                     if name-key is not equal to trans-name-id
                       move 'y' to key-not-found
                     else
                       move trans-key to out-key
                       move name-data to out-name
                       move trans-data to out-data
                       write out-rec
                     end-if
                 end-read
              end-perform
           end-start.

Good luck.

-- elliot

NG regulars might complain about the non-standard quote marks but at
least it is '85 standard. :-). I am sure I could also use one flag as
an exit condition on the match-records loop too.
```

##### ↳ ↳ Re: Strange result : I lost one record

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-24T15:50:55+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea2j88$cth$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153493019.011833.273860@m73g2000cwd.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com>`

```
epc8@juno.com a ï¿½crit :

> 
> Using database terminology, you are joining two tables. Let's call
…[5 more quoted lines elided]…
> the keys in the name table are unique.

> 
> -- elliot
> 

Hello,

I tried to delete the sentence :

         ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES

but when i run the program, i've got this I/O error :

cobol I/ error 39,52 on fgcart file ...

I use RM/COBOL-85 Runtime version 5.36.00 by Liant Software and this 
error is not referrenced in the user manual guide. I've already submit a 
question on this ng and someone told me that it is a hexadecimal code. 
Ok, after differents tests, i wrote this :

         ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES

and since, i'haven't this error.

What do you think about it ?

Best regards,

Jerome
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-24T13:05:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153771515.186559.7030@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<ea2j88$cth$1@s1.news.oleane.net>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net>`

```

Jerome wrote:

> I tried to delete the sentence :
>
…[7 more quoted lines elided]…
> error is not referrenced in the user manual guide.

Yes, it is. It is in the block 39, 50 through 39, 5E and states that
there is a mismatched key length for keys 0 through 14.  52 refers to
key 2.

The definition of the file in the FD must match the actual file as it
was created, you can't just change the FD and expect the data and
indexes to recreated themselves by morphing the bits on the disk.

If you want a file with a different configuration of keys then you must
rebuild the data into a file of that new definition.

> I've already submit a
> question on this ng and someone told me that it is a hexadecimal code.
…[4 more quoted lines elided]…
> and since, i'haven't this error.

You put the definition back to what it should be for that file.  You
fixed what you broke.
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 4)_

- **From:** epc8@juno.com
- **Date:** 2006-07-24T14:50:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153777825.059762.22000@i3g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com>`

```

Richard wrote:
> Jerome wrote:
>
…[9 more quoted lines elided]…
> > error is not referrenced in the user manual guide.

I am more confused now than before. How does the OP get his program, as
listed, to compile?

The identification division is missing.
The primary key and the alternate key are the same.
One variable is undeclared - it does not appear a FD.

How does the program, if it compiles and runs, produce the output
given?????

The data as listed for the files does not match the FDs given. The only
common item in both files is a 3 digit number which is NOT listed as
the key. The key is a PIC X(12) to which OTHER digits are affixed to
produce the second key.

> The definition of the file in the FD must match the actual file as it
> was created, you can't just change the FD and expect the data and
…[14 more quoted lines elided]…
> fixed what you broke.

The original is still broken in other ways.

It is still unclear what his data files really look like - or how they
were created.

What is the actual common key? Names? Three digits? The code says one
thing, the listed data something else and the explanation something
else all together.

-- elliot [resuming my search for an apiary in Sussex]
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-25T03:49:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<axgxg.228040$Mn5.205317@pd7tw3no>`
- **In-Reply-To:** `<1153777825.059762.22000@i3g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com>`

```
epc8@juno.com wrote:
> 
> -- elliot [resuming my search for an apiary in Sussex]

Given that the word apiary has Latin origins, following might narrow 
your search. Try the Roman Villa site at Bignor, on the way to Bognor 
Regis or Chichester :-).

If you don't find beez at least you'll be able to look at some 
fascinating floor mosaics. (Apparently done a lot to the site since I 
saw it in late 'fifties).

Jimmy
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 6)_

- **From:** epc8@juno.com
- **Date:** 2006-07-24T21:04:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153800247.106710.138530@i3g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <axgxg.228040$Mn5.205317@pd7tw3no>`

```

James J. Gavan wrote:
> epc8@juno.com wrote:
> >
…[10 more quoted lines elided]…
> Jimmy

Thanks for the itinerary. Actually I'm not planning a trip to the UK in
the near future. :-). My comment was a reference to the parting words
of a well known fictional character. I'll leave that as a bit of a
mystery but this itself will provide a small clue.

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-25T17:58:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YYsxg.232976$iF6.151395@pd7tw2no>`
- **In-Reply-To:** `<1153800247.106710.138530@i3g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <axgxg.228040$Mn5.205317@pd7tw3no> <1153800247.106710.138530@i3g2000cwc.googlegroups.com>`

```
epc8@juno.com wrote:
> James J. Gavan wrote:
> 
…[20 more quoted lines elided]…
> -- elliot

> Never heard of Val Andrews. Still doing a google, "Elementary my dear 
Watson".
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-25T18:12:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5mu0$abk$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153800247.106710.138530@i3g2000cwc.googlegroups.com> <YYsxg.232976$iF6.151395@pd7tw2no>`

```
In article <YYsxg.232976$iF6.151395@pd7tw2no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:
>epc8@juno.com wrote:
>> James J. Gavan wrote:
…[3 more quoted lines elided]…
>>>>-- elliot [resuming my search for an apiary in Sussex]

[snip]

>> My comment was a reference to the parting words
>> of a well known fictional character. I'll leave that as a bit of a
…[3 more quoted lines elided]…
>Watson".

My memory is, admittedly, porous... but I seem to recall reading somewhere 
that this is one of those 'great lines the character never really said', 
along with Rick's (Humphrey Bogart) request to 'Play it again, Sam.'

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 9)_

- **From:** epc8@juno.com
- **Date:** 2006-07-25T11:28:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153852133.104366.130690@m79g2000cwm.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153800247.106710.138530@i3g2000cwc.googlegroups.com> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com>`

```

docdwarf@panix.com wrote:
> In article <YYsxg.232976$iF6.151395@pd7tw2no>,
> James J. Gavan <jgavandeletethis@shaw.ca> wrote:
…[20 more quoted lines elided]…
> DD

It certainly appeared on film. See
http://www.imdb.com/title/tt0037168/quotes

Anyway, there is a story that Watson once visited Holmes carrying a
large textbook on COBOL programming. "I'm puzzled," said Watson "It
says that some data items have subordinates. But what about those that
do not?" To which Holmes replies "Elementary, my dear Watson."
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-25T18:43:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5ooo$mt7$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com> <1153852133.104366.130690@m79g2000cwm.googlegroups.com>`

```
In article <1153852133.104366.130690@m79g2000cwm.googlegroups.com>,
 <epc8@juno.com> wrote:
>
>docdwarf@panix.com wrote:
…[25 more quoted lines elided]…
>http://www.imdb.com/title/tt0037168/quotes

Ummmm... it may be my imagination, or lack thereof, but on the page for 
'Memorable Quotes from The Pearl of Death' (which is where the abovegiven 
URL leads me) the word 'Elementary' does not appear; the word 'dear' is 
found in 'My dear chap, I really must caution you against hitting 
newspaper reporters in the teeth...'

It may be my memory, or lack thereof, but I do not recall a story by Sir 
Arthur Conan Doyle entitled 'The Pearl of Death', either... but wasn't 
there some bit of cinematic fluff about 'Sherlock Holmes versus... The 
Nazis!'?

Ahhhh... http://imdb.com/title/tt0035317/ .

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 9)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-25T18:51:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AKtxg.235516$Mn5.32552@pd7tw3no>`
- **In-Reply-To:** `<ea5mu0$abk$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153800247.106710.138530@i3g2000cwc.googlegroups.com> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <YYsxg.232976$iF6.151395@pd7tw2no>,
> James J. Gavan <jgavandeletethis@shaw.ca> wrote:
…[25 more quoted lines elided]…
> along with Rick's (Humphrey Bogart) request to 'Play it again, Sam.'

Ilsa (Ingrid Bergman) and Lazslo (Paul Henried) had already entered the 
bar, unbeknown to Rick. Ilsa sees the pianist, Sam (Dooley Wilson) :-

Ilsa: Play it once, Sam. For old times' sake.
Sam: [lying] I don't know what you mean, Miss Ilsa.
Ilsa: Play it, Sam. Play "As Time Goes By."
Sam: [lying] Oh, I can't remember it, Miss Ilsa. I'm a little rusty on it.
Ilsa: I'll hum it for you. Da-dy-da-dy-da-dum, da-dy-da-dee-da-dum...
[Sam begins playing]
Ilsa: Sing it, Sam.
Sam: [singing] You must remember this / A kiss is still a kiss / A sigh 
is just a sigh / The fundamental things apply / As time goes by. / And 
when two lovers woo, / They still say, "I love you" / On that you can 
rely / No matter what the future brings-...
Rick: [rushing up] Sam, I thought I told you never to play-...
[Sees Ilsa. Sam closes the piano and rolls it away]

Amazing how a two-bit corny movie became such an enjoyable and perennial 
romantic classic.

Jimmy
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-25T19:04:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5q0h$bbn$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com> <AKtxg.235516$Mn5.32552@pd7tw3no>`

```
In article <AKtxg.235516$Mn5.32552@pd7tw3no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:
>docdwarf@panix.com wrote:
>> In article <YYsxg.232976$iF6.151395@pd7tw2no>,
…[43 more quoted lines elided]…
>[Sees Ilsa. Sam closes the piano and rolls it away]

From http://imdb.com/title/tt0034583/quotes:

--begin quoted text:

Rick: You know what I want to hear. 
Sam: [lying] No, I don't. 
Rick: You played it for her, you can play it for me! 
Sam: [lying] Well, I don't think I can remember... 
Rick: If she can stand it, I can! Play it! 

--end quoted text

... and nary a 'Play it again, Sam' in sight.

>
>Amazing how a two-bit corny movie became such an enjoyable and perennial 
>romantic classic.

As I recall 'The Wizard of Oz' opened to lukewarm reviews... and now it 
isn't in Kansas any more.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 11)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-07-27T15:28:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaam2n022br@news1.newsguy.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com> <AKtxg.235516$Mn5.32552@pd7tw3no> <ea5q0h$bbn$1@reader2.panix.com>`

```

In article <ea5q0h$bbn$1@reader2.panix.com>, docdwarf@panix.com () writes:
> 
> As I recall 'The Wizard of Oz' opened to lukewarm reviews... and now it 
> isn't in Kansas any more.

Some of us still think it's a feeble distortion of a fine novel.
(Salman Rushdie disagrees, but - much as I like Rushdie - he's wrong.)

The film turns Baum's self-confident, capable Dorothy into a
trembling, nearly helpless wimp, thereby completely missing the point
of the narrative (which is Yet Another version of how the vital rural
underclass will rehabilitate the effete urban aristocracy), and
ruining one of the best female characters in children's literature;
fills Oz with saccharine clowning and patronizing moralizing
(particularly in its version of the Wizard's gifts), thereby robbing
the narrative of its connection to the original European marchen
tradition; and cheats at the end, thereby robbing itself of any claim
to decent plotting.

It has some technical merit, particularly in the famous transition
from sepia-tone (the Kansas segments are not actually black-and-white)
to full (indeed over-full) color, and some good scenes, such as the
Wicked Witch's Emerald City flyover.  But that's not enough to make
it a good film, much less a great one.

Not that I care, or anything.
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-27T16:16:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaaosq$j1n$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <AKtxg.235516$Mn5.32552@pd7tw3no> <ea5q0h$bbn$1@reader2.panix.com> <eaam2n022br@news1.newsguy.com>`

```
In article <eaam2n022br@news1.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>In article <ea5q0h$bbn$1@reader2.panix.com>, docdwarf@panix.com () writes:
…[4 more quoted lines elided]…
>Some of us still think it's a feeble distortion of a fine novel.

Welcome to Hollywood, Mr Wojcik... such things happen there, at times... 
or so I've been told.  Feeble or not the film has managed to work its way 
into American popular culture, to the point where an intoned 'I'll get 
you... and your little dog, too!' seems to be recognised across the length 
and breadth of This Great Nation as an embodiment of 'wickedness'.

[snip]

>Not that I care, or anything.

You don't care?  It may not be apathy, Mr Wojcik - oh, and you left out 
the part about the Silver Standard, too - it may be simple... fear.  
Perhaps things might be different were you to have a bit more bravery... 
after all...

What makes a king out of a slave?  Courage!

What makes the flag on the mast to wave?  Courage!

What makes the elephant charge his tusk, in the misty mist or the dusty 
dust?  What makes the muskrat guard his musk?  Courage!

What makes the Sphinx the seventh wonder?  Courage!

What makes the dawn come up like thunder?  Courage!

What makes the Hottentot so hot?

What puts the 'ape' in ap-ri-cot?

What do they got that you ain't got?

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-25T12:52:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqpcc2lskeh3u01gsvg6tc03j95vq7170o@4ax.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153800247.106710.138530@i3g2000cwc.googlegroups.com> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com>`

```
On Tue, 25 Jul 2006 18:12:16 +0000 (UTC), docdwarf@panix.com () wrote:

>> Never heard of Val Andrews. Still doing a google, "Elementary my dear 
>>Watson".
…[3 more quoted lines elided]…
>along with Rick's (Humphrey Bogart) request to 'Play it again, Sam.'

But Woody Allen said it again.

When you've had as many movies as Sherlock Homes has (IMDB has 257
matches on that character), we can have a large variance from the
original source.   Basil Rathbone did not like having his mouth
hidden, so he started using anachronistic the calabash pipe that we
associate with Holmes today.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-26T09:33:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea7cto$kh9$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <YYsxg.232976$iF6.151395@pd7tw2no> <ea5mu0$abk$1@reader2.panix.com> <cqpcc2lskeh3u01gsvg6tc03j95vq7170o@4ax.com>`

```
In article <cqpcc2lskeh3u01gsvg6tc03j95vq7170o@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 25 Jul 2006 18:12:16 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>But Woody Allen said it again.

Well, what else what might expect from a Brooklyn-boy?

>
>When you've had as many movies as Sherlock Homes has (IMDB has 257
…[3 more quoted lines elided]…
>associate with Holmes today.

Well... I recall references to Holmes' smoking an 'oily, black clay'... 
checking http://www.gutenberg.org/dirs/etext99/advsh12.txt (only thirteen 
of Conan Doyle's stories... but a fitting number, nevertheless) there are 
also references to a briar and a 'long cherrywood'.  A bit of 
web-sleuthing indicates that one Gary Schrier has recently published 'The 
History of the Calabash Pipe' recently and it is being pitched as having 
'plenty of direct Sherlockian interest' 
(http://www.sherlock-holmes.org.uk/pdf/DM263.pdf)... but what's even more 
interesting, to my eye, is this exchange from 
http://forum.pipes.org/discus/messages/23/29455.html?1139537539 which 
mentions 'a gentleman writing the first book on the history of the 
calabash but it is not due out until May', referring, I believe, to the 
book that came out recently.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-24T23:05:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153807543.759469.98410@s13g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<axgxg.228040$Mn5.205317@pd7tw3no>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <axgxg.228040$Mn5.205317@pd7tw3no>`

```

James J. Gavan wrote:

> Given that the word apiary has Latin origins, following might narrow
> your search. Try the Roman Villa site at Bignor, on the way to Bognor
> Regis or Chichester :-).

And just the other side of Chichester along the same Stane Street is
Fishbourne Villa which wasn't discovered until the 60s.
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-25T18:25:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mtxg.235392$Mn5.123895@pd7tw3no>`
- **In-Reply-To:** `<1153807543.759469.98410@s13g2000cwa.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <axgxg.228040$Mn5.205317@pd7tw3no> <1153807543.759469.98410@s13g2000cwa.googlegroups.com>`

```
Richard wrote:
> James J. Gavan wrote:
> 
…[8 more quoted lines elided]…
> 
This is an interesting link to the Sussex sites, with photographs, 
which I just checked :-

http://www.romansinsussex.co.uk/sussex/bignor.asp

We were Bognor-bound for a week's holiday from Guildford - back in 
Lambretta days. Probably would have whisked by in a car, but at a small 
intersection saw a sign to our right (west):  Bignor - Roman Villa.
Curious, we went and took a look.

I think what impressed me most was the baths at Bath, Somerset. 
Originally built at ground level, you can now look over a bridge or 
roadway to the baths below. Human garbage over the centuries has 
increased the height of the road to some 20 - 30 feet.

Jimmy
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-25T18:46:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5otr$7th$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153807543.759469.98410@s13g2000cwa.googlegroups.com> <6mtxg.235392$Mn5.123895@pd7tw3no>`

```
In article <6mtxg.235392$Mn5.123895@pd7tw3no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:

[snip]

>I think what impressed me most was the baths at Bath, Somerset. 
>Originally built at ground level, you can now look over a bridge or 
>roadway to the baths below. Human garbage over the centuries has 
>increased the height of the road to some 20 - 30 feet.

My response to this is 'a person standing on a tall pile of trash still 
sees a farther horizon than one standing on a flat plain of pure, white 
sand'.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-25T12:54:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n5qcc2ljeh4d6po1e3ubcucerjl3cr73pd@4ax.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <axgxg.228040$Mn5.205317@pd7tw3no> <1153807543.759469.98410@s13g2000cwa.googlegroups.com> <6mtxg.235392$Mn5.123895@pd7tw3no> <ea5otr$7th$1@reader2.panix.com>`

```
On Tue, 25 Jul 2006 18:46:19 +0000 (UTC), docdwarf@panix.com () wrote:

>My response to this is 'a person standing on a tall pile of trash still 
>sees a farther horizon than one standing on a flat plain of pure, white 
>sand'.

Sort of like "I can see farther because I stand on the shoulders of
midgets".

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-26T09:35:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea7d1t$3fu$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <6mtxg.235392$Mn5.123895@pd7tw3no> <ea5otr$7th$1@reader2.panix.com> <n5qcc2ljeh4d6po1e3ubcucerjl3cr73pd@4ax.com>`

```
In article <n5qcc2ljeh4d6po1e3ubcucerjl3cr73pd@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 25 Jul 2006 18:46:19 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>midgets".

Sort of... excepts midgets are usually not defined as being 'tall', as the 
pile of trash was... and midgets are human beings, composed of cells with, 
for the most part, 23 pairs of chromosomes, and trash, quite frequently, 
isn't...

... other than that, *most* 'sort of'... kinda almost like, maybe.

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 5)_

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-25T09:35:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea4hk5$aor$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153777825.059762.22000@i3g2000cwc.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com>`

```
epc8@juno.com a ï¿½crit :

> 
> I am more confused now than before. How does the OP get his program, as
> listed, to compile?

> -- elliot [resuming my search for an apiary in Sussex]
> 
OK, I'm going to work with your code and going to read carefully your 
explanations (and the others contrib).

I thank you again for your help

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 6)_

- **From:** epc8@juno.com
- **Date:** 2006-07-25T05:01:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153828875.430834.183310@m79g2000cwm.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <ea4hk5$aor$1@s1.news.oleane.net>`

```

Jerome wrote:

> OK, I'm going to work with your code and going to read carefully your
> explanations (and the others contrib).

Good luck.

One point Richard made is particularly important. If you change the
program then you will have to create files containing your data that
follow that layout. For ordinary "line sequential" (text) files you can
use a standard text editor. For organization is indexed files you
generally write a program that builds these files by reading some other
type of file and writing records out to the indexed file.

Here are some sample data files:

---- name.txt ----
152Name1
153Name2
154Name3
155Name4
156Name5
---- end of file ----

---- trans.txt ----
152001MyRecord1
153001MyRecord2
153153MyRecord3
154001MyRecord4
154154MyRecord5
155001MyRecord6
156001MyRecord7
156156MyRecord8
---- end of file ----

Here is a program to read the first .txt file and create the name
table:

---- loadname.cbl ----
       identification division.
       program-id. loadname.
       environment division.
       configuration section.
       source-computer. ibm-pc.
       object-computer. ibm-pc.
       input-output section.
       file-control.
           select name-text assign to disk 'name.txt'
             organization is line sequential.
           select name-file assign to disk 'name.dat'
             organization is indexed
             record key is name-key.
       data division.
       file section.
       fd name-text.
       01 text-rec.
         05 text-key pic 9(3).
         05 text-data pic x(5).
       fd name-file.
       01 name-rec.
         05 name-key pic 9(3).
         05 name-data pic x(5).
       working-storage section.
       01 flags.
         05 name-eof pic x value 'n'.
       procedure division.
       main.
           open input name-text
           open output name-file
           perform until name-eof is equal to 'y'
             read name-text
               at end
                 move 'y' to name-eof
               not at end
                 move text-rec to name-rec
                 display name-key '|' name-data '|'
                 write name-rec
             end-read
           end-perform
           close name-text
           close name-file
           stop run.
---- end of file ----

Here is a program to read the second text file and write the
transaction table:

---- loadtran.cbl ----
       identification division.
       program-id. loadtrans.
       environment division.
       configuration section.
       source-computer. ibm-pc.
       object-computer. ibm-pc.
       input-output section.
       file-control.
           select trans-text assign to disk 'trans.txt'
             organization is line sequential.
           select trans-file assign to disk 'trans.dat'
             organization is indexed
             record key is trans-key.
       data division.
       file section.
       fd trans-text.
       01 text-rec.
         05 text-key pic 9(6).
         05 text-data pic x(9).
       fd trans-file.
       01 trans-rec.
         05 trans-key pic 9(6).
         05 trans-data pic x(9).
       working-storage section.
       01 flags.
         05 trans-eof pic x value 'n'.
       procedure division.
       main.
           open input trans-text
           open output trans-file
           perform until trans-eof is equal to 'y'
             read trans-text
               at end
                 move 'y' to trans-eof
               not at end
                 move text-rec to trans-rec
                 display trans-key '|' trans-data '|'
                 write trans-rec
             end-read
           end-perform
           close trans-text
           close trans-file
           stop run.
---- end of file ----

With these programs you can create test INDEXED files suitable for
running with my example join program. Then you can see how the program
that I posted works.

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 7)_

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-25T15:27:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5683$13c$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153828875.430834.183310@m79g2000cwm.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <ea4hk5$aor$1@s1.news.oleane.net> <1153828875.430834.183310@m79g2000cwm.googlegroups.com>`

```
epc8@juno.com a ï¿½crit :

> 
> With these programs you can create test INDEXED files suitable for
…[4 more quoted lines elided]…
> 

Waouh, super !

My problem is that I work with data files created by another programmer 
there is a long time and I haven't not enough documentation about his work.
Another problem is I'm not a specialist of cobol, but you noticed it :-)

Your codes, explanations and advices are very useful and precious (I 
hope it is the good word in english). I'm going to work with the new 
code that you posted.

Great thanks

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 8)_

- **From:** epc8@juno.com
- **Date:** 2006-07-25T07:55:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153839302.185649.188840@m73g2000cwd.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <ea4hk5$aor$1@s1.news.oleane.net> <1153828875.430834.183310@m79g2000cwm.googlegroups.com> <ea5683$13c$1@s1.news.oleane.net>`

```

Jerome wrote:
> epc8@juno.com a écrit :
>
…[12 more quoted lines elided]…
> Another problem is I'm not a specialist of cobol, but you noticed it :-)

I'm going to translate what you just said back into French and guess
that the original programmer is no longer there.

If your data files are indexed files then you may be able to convert
them back into sequential files without writing a COBOL program. Some
indexed file formats contain enough information about the file
structure to make this possible. I don't know if your compiler includes
this facility.

Here is a non COBOL example. dBase3 files are small databases. Each
contains header records which describe enough of the file's contents to
allow external utilities to extract data from the file, including field
by field access.

-- elliot
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 9)_

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-25T17:35:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea5dnk$8uh$1@s1.news.oleane.net>`
- **In-Reply-To:** `<1153839302.185649.188840@m73g2000cwd.googlegroups.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <1153493019.011833.273860@m73g2000cwd.googlegroups.com> <ea2j88$cth$1@s1.news.oleane.net> <1153771515.186559.7030@m73g2000cwd.googlegroups.com> <1153777825.059762.22000@i3g2000cwc.googlegroups.com> <ea4hk5$aor$1@s1.news.oleane.net> <1153828875.430834.183310@m79g2000cwm.googlegroups.com> <ea5683$13c$1@s1.news.oleane.net> <1153839302.185649.188840@m73g2000cwd.googlegroups.com>`

```
epc8@juno.com a ï¿½crit :
> 
> If your data files are indexed files then you may be able to convert
…[3 more quoted lines elided]…
> this facility.

> -- elliot
> 

I'm reading the installation and user's guide of my compiler. 7 
utilities are described. I'will seek this utilities (the original floppies).

In any case, you answered my questions in your preceding posts

Jerome
```

#### ↳ Re: Strange result : I lost one record

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-27T06:06:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SJYxg.243112$iF6.132019@pd7tw2no>`
- **In-Reply-To:** `<e9qf6t$bjv$1@s1.news.oleane.net>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net>`

```
Jerome wrote:
> Hello,
> 
…[46 more quoted lines elided]…
> Jerome

Any luck so far - you don't seem to be getting anywhere fast on this 
one. You are reading ISAMs sequentially.

Let's cheat a bit - hopefully you can do this with RM/COBOL. (It's the 
technique Micro Focus provides to get RM/COBOL ISAM data into Micro 
Focus format). Don't know your compiler but I am *assuming* RM/COBOL 
still has two files for each ISAM, e.g. fgctar01.dat and fgctar01.idx. 
Routine below ignores the "idx" or "inx" file.

Take your existing file definitions and in a *separate* program do this  :-

       INPUT-OUTPUT SECTION.
        FILE-CONTROL.
         SELECT FGCTAR ASSIGN TO RANDOM "fgctar01"
               ORGANIZATION INDEXED
               ACCESS DYNAMIC
               RECORD KEY GCTAR-CLE
               STATUS ST-GCTAR.
         SELECT FGCART ASSIGN TO RANDOM "fgcart01"
               ORGANIZATION IS INDEXED
               ACCESS IS DYNAMIC
               RECORD KEY IS GCART-CLE
               ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES
         FILE STATUS IS FichierStatus.
            SELECT OUTART ASSIGN TO RANDOM "out-ess.txt"
                ORGANIZATION IS LINE SEQUENTIAL.

change above :-


*>            Select               Data-File
*>            assign               Data-filename
*>            organization         SEQUENTIAL
*>            access               sequential
*>            file status          ws-FileStatus.



         SELECT FGCTAR ASSIGN TO  "fgctar01"
               ORGANIZATION SEQUENTIAL
               ACCESS SEQUENTIAL
               FILE-STATUS FGCTAR-Status
         SELECT FGCART ASSIGN TO  "fgcart01"
               ORGANIZATION SEQUENTIAL
               ACCESS SEQUENTIAL
               FILE-STATUS FGCART-Status

Leave your record formats unchanged.

Separately for the two files above :-

1) Open as INPUT
2) READ NEXT until EOF
3) WRITE each record read to a temporary file LINE SEQUENTIAL
4) Then CLOSE inputs and outputs
5) As you step through each file, for each "action" ( OPEN, READ, WRITE 
or CLOSE) ensure you check the files-status code :-

IF FILE-STATUS <> ?????
    PERFORM file-error

Now when you bring up the two LINE SEQUENTIALS in a text editor do you 
get *exactly* the same set of records per file you showed in your very 
first message ?

Record sequencing wont necessarily be the same :-

1) READing an ISAM Sequentially (READ NEXT) will give records in 
ascending sequence by key.

2) Re-classifying ISAM files as SEQUENTIAL will give you records in the 
sequence that they were added to the file.

Have you got just the one set of test data; if possible try it against 
another test set and see if again you "lose" records.

One other alternative - use the RM/COBOL ISAM Rebuild routines. I have a 
very old copy of RM and it had the nasty habit of silently dropping 
problematic records. Hopefully their routines are more slick now.

Whichever route you go, do a record count per file.

Above doesn't solve your problem, if it works - but it should help point 
you in the right direction with your "real" program.


Jimmy
```

##### ↳ ↳ Re: Strange result : I lost one record

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-27T10:31:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea9tkv$ik5$1@s1.news.oleane.net>`
- **In-Reply-To:** `<SJYxg.243112$iF6.132019@pd7tw2no>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <SJYxg.243112$iF6.132019@pd7tw2no>`

```
James J. Gavan a ï¿½crit :

> Above doesn't solve your problem, if it works - but it should help point 
> you in the right direction with your "real" program.
> 
> 
> Jimmy

Thank you for your help,

I haven't index file, my compiler is a RM/COBOL-85 Liant Software v5.36.

My problem has been already solved but I will read your code attentively 
because it's a luck for me to learn cobol. So, I still thank you for 
your assistance.

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-27T09:18:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaa0ch$if9$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <SJYxg.243112$iF6.132019@pd7tw2no> <ea9tkv$ik5$1@s1.news.oleane.net>`

```
In article <ea9tkv$ik5$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:
>James J. Gavan a �crit :
>
…[12 more quoted lines elided]…
>your assistance.

Congratulations on getting your problem solved... can you post the code 
that did it?

DD
```

###### ↳ ↳ ↳ Re: Strange result : I lost one record

_(reply depth: 4)_

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-07-27T11:54:32+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaa2gv$lcp$1@s1.news.oleane.net>`
- **In-Reply-To:** `<eaa0ch$if9$1@reader2.panix.com>`
- **References:** `<e9qf6t$bjv$1@s1.news.oleane.net> <SJYxg.243112$iF6.132019@pd7tw2no> <ea9tkv$ik5$1@s1.news.oleane.net> <eaa0ch$if9$1@reader2.panix.com>`

```
docdwarf@panix.com a ï¿½crit :

> Congratulations on getting your problem solved... can you post the code 
> that did it?
> 
> DD
> 
Yes, of course, in fact it is the code of Eliott that solved my problem :

        IDENTIFICATION DIVISION.
	PROGRAM-ID. JOIN.
	ENVIRONMENT DIVISION.
	CONFIGURATION SECTION.
	SOURCE-COMPUTER. IBM-PC.
	OBJECT-COMPUTER. IBM-PC.
	INPUT-OUTPUT SECTION.
	FILE-CONTROL.
	    SELECT NAME-FILE ASSIGN TO DISK "fgcart01"
	        ORGANIZATION IS INDEXED
		 RECORD KEY IS GCART-NUM
		 ALTERNATE RECORD KEY IS GCART-NOM WITH DUPLICATES.
	    SELECT TRANS-FILE ASSIGN TO DISK "fgctar01"
	        ORGANIZATION IS INDEXED
		 RECORD KEY IS GCTAR-CLE.
	    SELECT OUT-FILE ASSIGN TO DISK "out.txt"
	        ORGANIZATION IS LINE SEQUENTIAL.
	DATA DIVISION.
	FILE SECTION.
	    COPY "FGCART.CPY".
	    COPY "FGCTAR.CPY".
	FD OUT-FILE.
	01 OUT-REC.
	    05 OUT-KEY PIC X(6).
	    05 FILLER PIC X.
	    05 OUT-NAME PIC X(5).
	    05 FILLER PIC X.
	    05 OUT-DATA PIC 9(6).9(2).
	WORKING-STORAGE SECTION.
	01 FLAGS.
	    05 NAME-EOF PIC X VALUE 'n'.
	    05 TRANS-EOF PIC X.
	    05 KEY-NOT-FOUND PIC X.
	PROCEDURE DIVISION.
	MAIN.
	    OPEN INPUT NAME-FILE
	    OPEN INPUT TRANS-FILE
	    OPEN OUTPUT OUT-FILE
	    MOVE ALL '|' TO OUT-REC
	    PERFORM UNTIL NAME-EOF IS EQUAL TO 'y'
	        READ NAME-FILE
		     AT END
		         MOVE 'y' TO NAME-EOF
		     NOT AT END
		         PERFORM GET-MATCH
		 END-READ
	    END-PERFORM
	    CLOSE NAME-FILE
	    CLOSE TRANS-FILE
	    CLOSE OUT-FILE
	    STOP RUN.
	GET-MATCH.
	
	    MOVE GCART-NUM TO GCTAR-ART
	
	    START TRANS-FILE KEY NOT < GCTAR-ART
	        INVALID KEY
		     MOVE 'y' TO KEY-NOT-FOUND
		 NOT INVALID KEY
		     MOVE 'n' TO TRANS-EOF
		     MOVE 'n' TO KEY-NOT-FOUND
                    PERFORM UNTIL TRANS-EOF IS EQUAL TO 'y'
		     OR KEY-NOT-FOUND IS EQUAL TO 'y'
		
                        READ TRANS-FILE NEXT RECORD
			      AT END
			          MOVE 'y' TO TRANS-EOF
			      NOT AT END
			          IF GCART-NUM IS NOT EQUAL TO GCTAR-ART
				       MOVE 'y' TO KEY-NOT-FOUND
				   ELSE
				       MOVE GCTAR-CLE TO OUT-KEY
					MOVE GCART-NOM TO OUT-NAME
					MOVE GCTAR-PUHT TO OUT-DATA
					WRITE OUT-REC
				   END-IF
                        END-READ
                    END-PERFORM
                END-START.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
