[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CA-Easytrieve Users

_19 messages · 10 participants · 2007-12_

---

### CA-Easytrieve Users

- **From:** bnolan@mergilent.com
- **Date:** 2007-12-15T06:03:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com>`

```
Our company has developed a fully automated tool to convert CA-
Easytrieve code to very elegant
and highly maintainable COBOL code.

If any organization has a large number of CA-Easytrieve programs we
can convert a sample code
to show you the completeness and the elegance of our tool.
```

#### ↳ Re: CA-Easytrieve Users

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-12-15T14:40:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com>`

```
> Our company has developed a fully automated tool to convert CA-
> Easytrieve code to very elegant
> and highly maintainable COBOL code.


Syntax Error.

"automated" , "code", "convert" and "maintainable" may never appear in the 
same sentence.

MCM
```

##### ↳ ↳ Re: CA-Easytrieve Users

- **From:** bnolan@mergilent.com
- **Date:** 2007-12-15T08:51:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net>`

```
Hello,

There are no syntax errors.
I have attached some code for you to see.


       PROCEDURE DIVISION.

       00000-MAINLINE  SECTION.
      *------------------------
       00000-START.

           PERFORM J1000-JOB-001.
           PERFORM J1100-JOB-002.
           PERFORM J1200-PRINT-SUMMARY.

       00000-EXIT.
      *-----------
           EXIT PROGRAM.

       J1000-JOB-001 SECTION.
      *----------------------
       J1000-START.

           MOVE WC-FALSE TO WF-SYSCARD-OPEN.
           PERFORM J1010-JOB-001-RUN
              UNTIL JOB-001-END.

           CLOSE SYSCARD-FILE.
           MOVE WC-FALSE TO WF-SYSCARD-OPEN.

       J1000-EXIT.
      *-----------
           EXIT.

       J1010-JOB-001-RUN SECTION.
      *--------------------------
       J1010-START.

           PERFORM F1000-READ-SYSCARD.
           IF SYSCARD-EOF
              MOVE WC-TRUE TO WF-JOB-001-END
              GO TO J1010-EXIT
           END-IF.
           MOVE QTR-END-DATE TO DATE1-I-DATE.
           MOVE 'E' TO DATE1-I-DATE-FORMAT.
           CALL 'sydate1' USING DATE1-I DATE1-O.
           IF DATE1-O-ERROR-FLAG NOT = 0
              DISPLAY 'PARAMETER DATE ERROR: ' DATE1-I-DATE ' '
               DATE1-O-ERROR-DESCRIPTION
              MOVE 16 TO RETURN-CODE
              EXIT PROGRAM
           ELSE
              MOVE DATE1-O-LONG-DISPLAY TO QTR-END-DATE-R
           END-IF.


       J1010-EXIT.
      *-----------
           EXIT.

       J1100-JOB-002 SECTION.
      *----------------------
       J1100-START.


           IF INFILE-OPEN
              CLOSE INFILE-FILE
           END-IF.
           MOVE WC-FALSE TO WF-INFILE-OPEN.
           PERFORM J1110-JOB-002-RUN
              UNTIL JOB-002-END.

           CLOSE INFILE-FILE.
           MOVE WC-FALSE TO WF-INFILE-OPEN.

       J1100-EXIT.
      *-----------
           EXIT.

       J1110-JOB-002-RUN SECTION.
      *--------------------------
       J1110-START.

           PERFORM F1100-READ-INFILE.
           IF INFILE-EOF
              MOVE WC-TRUE TO WF-JOB-002-END
              GO TO J1110-EXIT
           END-IF.
           IF COVNUM = 99999999
              GO TO J1110-EXIT
           END-IF.


           COMPUTE TOTAMT = BASICAMT + SUPPAMT.
           IF AGEIND = 'O'
              MOVE 'OVER 65 TOTALS' TO AGE
           ELSE
              MOVE 'UNDER 65 TOTALS' TO AGE
           END-IF.

           IF PROVTYPE = '08'
              MOVE 'PUBLIC' TO HOSP
           ELSE
           IF PROVTYPE = '09''10''11'
              MOVE 'PRIVATE' TO HOSP
           ELSE
           IF PROVTYPE = '27'
              MOVE 'DAY HOSP' TO HOSP
           ELSE
           IF PROVTYPE = '00'
              MOVE 'MEDIGAP' TO HOSP
           ELSE
              MOVE 'OTHER' TO HOSP
           END-IF
           END-IF
           END-IF
           END-IF.

           IF W-COMP-NO NOT = FUNDNO
              MOVE FUNDNO TO W-COMP-NO
              PERFORM F1200-SEARCH-CMPY
              IF NOT CMPY-FOUND
                 MOVE ' ' TO W-NAME-ABBR
              END-IF
           END-IF.

           ACCEPT W-DATE FROM DATE.
           MOVE W-YY TO W-SYS-YY.
           MOVE W-MM TO W-SYS-MM.
           MOVE W-DD TO W-SYS-DD.

       J1110-EXIT.
      *-----------
           EXIT.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-12-15T13:15:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DJV8j.39813$L%6.8000@bignews3.bellsouth.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com>`

```
<bnolan@mergilent.com> wrote:
>
> There are no syntax errors.
…[19 more quoted lines elided]…
>           END-IF.

That's "elegant" alright. And that code indenting thing is so difficult
to implement, too. Makes it "highly maintainable". :-)
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-12-15T16:37:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BGY8j.6599$3b7.4994@newsfe23.lga>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net>`

```
Of course there are many different ways of doing this.  No doubt there are
even some that will meet with more approval than others.  So what?  It
works, it's easy to understand, and that's what I would usually expect of
"highly maintainable" code.  No doubt I would run a listing-formatter to
make it easier to read if I had to make any changes, but that's because I'm
lazy.

Elegance is strictly in the eye of the beholder where the golden proportion
doesn't apply.

PL

Judson McClendon <judmc@sunvaley0.com> wrote in message
news:DJV8j.39813$L%6.8000@bignews3.bellsouth.net...
> <bnolan@mergilent.com> wrote:
> >
…[25 more quoted lines elided]…
> Judson McClendon       judmc@sunvaley0.com (remove zero)
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-12-15T18:20:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kir8m35hge9oi4sfthf1a99jobu16qbeec@4ax.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga>`

```
On Sat, 15 Dec 2007 16:37:21 -0600, "tlmfru" <lacey@mts.net> wrote:

>Of course there are many different ways of doing this.  No doubt there are
>even some that will meet with more approval than others.  So what?  It
>works, 

I'm always amazed at how people can read code without understanding what it says. 
 IF PROVTYPE = '09''10''11' does not work. It's an obvious bug.


>it's easy to understand, and that's what I would usually expect of
>"highly maintainable" code.  No doubt I would run a listing-formatter to
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 6)_

- **From:** bnolan@mergilent.com
- **Date:** 2007-12-15T17:38:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d394564-7e73-4751-a403-a071adf3b2f1@b40g2000prf.googlegroups.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <kir8m35hge9oi4sfthf1a99jobu16qbeec@4ax.com>`

```
On Dec 16, 11:20 am, Robert <n...@e.mail> wrote:
> On Sat, 15 Dec 2007 16:37:21 -0600, "tlmfru" <la...@mts.net> wrote:
> >Of course there are many different ways of doing this.  No doubt there are
…[45 more quoted lines elided]…
> >> Judson McClendon       ju...@sunvaley0.com (remove zero)

       ......

           05 PROVTYPE        PIC X(10).

       ......

       IF PROVTYPE = '09''10''11' does work. It's not a bug.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-12-15T19:19:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V2%8j.40060$L%6.1928@bignews3.bellsouth.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga>`

```
Code indenting is functional, not esthetics.

"tlmfru" <lacey@mts.net> wrote:
> Of course there are many different ways of doing this.  No doubt there are
> even some that will meet with more approval than others.  So what?  It
…[39 more quoted lines elided]…
>> Judson McClendon       judmc@sunvaley0.com (remove zero)
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-12-16T08:44:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:V2%8j.40060$L%6.1928@bignews3.bellsouth.net...
> Code indenting is functional, not esthetics.

(My $0.02)

In this case even more conventional code indenting would not IMO be a 
sufficient excuse for using fifteen IF... ELSE constructs in lieu of one 
EVALUATE..END-EVALUATE; which, by the way would also neatly handle what I 
THINK was the intent of the invalid "IF PROVTYPE = '09''10''11'  " clause.

But I digress. My original comment...

"Syntax Error:  "automated" , "code", "convert" and "maintainable" may never 
appear in the same sentence."

... was intended as a little humor, nothing more.

Bad audience choice, I guess.

MCM
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 7)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-12-16T12:30:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e9j.6909$3b7.2533@newsfe23.lga>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net>`

```

Michael Mattias <mmattias@talsystems.com> wrote in message
news:PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net...

> But I digress. My original comment...
>
> "Syntax Error:  "automated" , "code", "convert" and "maintainable" may
never
> appear in the same sentence."
>
…[5 more quoted lines elided]…
>

How about: Tools which claim to "convert" "maintainable" "code" are  nothing
more than "automated" "syntax error" generators!

Mind you, the general principle that there are words which can never appear
in a sentence together is quite correct: such as "good" and "coffee".  (A
famous mathematician once said that mathematicians are devices for
converting coffee into theorems.  Then there was Gallagher Plus, who
invented a machine that turned dirt into music ...)

PL
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-12-17T13:41:02+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5slussF1a03btU1@mid.individual.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net...
> "Judson McClendon" <judmc@sunvaley0.com> wrote in message 
> news:V2%8j.40060$L%6.1928@bignews3.bellsouth.net...
…[14 more quoted lines elided]…
> ... was intended as a little humor, nothing more.

I got it Michael, and I agree...

The thing that strikes me about this is WHY you would want to convert 
Easytrieve into  a dying language that must then be compiled before you can 
run it, and recompiled every time you maintain it, leaving aside whether the 
generated code is "elegant" or not.

If you wanted to use COBOL you would have used it in the first place and not 
chosen Easytrieve.

COBOL programmers who have been exposed to Easytrieve pick it up fairly 
quickly; it isn't rocket science.

I see this as a pointless exercise...

Pete.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 8)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-12-16T22:04:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t0mbm3ts2fflfrr2v26kv2e3s6cc1vteml@4ax.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net>`

```
On Mon, 17 Dec 2007 13:41:02 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[25 more quoted lines elided]…
>generated code is "elegant" or not.

I can think of a few reasons.

1.  Eliminate the annual cost of maintenance of the product which
increases with CPU capacity (especially if you are at a sited that
doesn't like CA - Computer Associates).

2.  Performance if this is on a time critical path (not likely but
there because it may take 3 times the amount of CPU for the task but
normally that still is relatively small).

3.The program has outstripped Easytrieve capabilities.  Also I have
seen Easytrieve used in ways that are awkward and obscure because
people didn't read the manual.
>
>If you wanted to use COBOL you would have used it in the first place and not 
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-12-18T12:30:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5sof59F1ad6maU1@mid.individual.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net> <t0mbm3ts2fflfrr2v26kv2e3s6cc1vteml@4ax.com>`

```


"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:t0mbm3ts2fflfrr2v26kv2e3s6cc1vteml@4ax.com...
> On Mon, 17 Dec 2007 13:41:02 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[34 more quoted lines elided]…
> I can think of a few reasons.

OK... I'm listening :-)
>
> 1.  Eliminate the annual cost of maintenance of the product which
> increases with CPU capacity (especially if you are at a sited that
> doesn't like CA - Computer Associates).

You could eliminate the cost of many tools by simply not using them. This 
means you need to ask why you bought them in the first place... If the cost 
of such tools is escalating, then some negotiation with the vendor may be 
required. Basically, you either need tools or you don't. If you write 
everything in COBOL (or see that as an option...) then don't buy tools... If 
you don't buy tools, then you won't be using a tool that translates 
Easytrieve into generated COBOL.

>
> 2.  Performance if this is on a time critical path (not likely but
> there because it may take 3 times the amount of CPU for the task but
> normally that still is relatively small).

As you have discounted this as a REAL objection, I won't comment further... 
:-)

>
> 3.The program has outstripped Easytrieve capabilities.  Also I have
> seen Easytrieve used in ways that are awkward and obscure because
> people didn't read the manual.

OK. If the "program" has outstripped Easytrieve capabilities, then maybe the 
"program" wasn't thought about very carefully in the first place.

Is a tool which converts it to generated COBOL, really going to help much? 
Shouldn't the whole requirement be re-evaluated and probably re-specced?


>>
>>If you wanted to use COBOL you would have used it in the first place and 
…[6 more quoted lines elided]…
>>I see this as a pointless exercise...

I still see this as a pointless exercise...

Pete.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 8)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2007-12-17T11:18:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iu7dm39op8v0na0abgpfc57h28874upct2@4ax.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net>`

```
On Mon, 17 Dec 2007 13:41:02 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[26 more quoted lines elided]…
>

You can create executible object from Easytrieve just like you can
from Cobol source.  Easytrieve can also use existing Cobol copybooks.
So, my question would be, unless you are dumping your Easytrieve
license, why would you want to convert your Easytrieve's to Cobol?

And what language on the mainframe can you write in that doesn't have
to be compiled or assembled or somehow turned into machine code before
it can be executed?

>If you wanted to use COBOL you would have used it in the first place and not 
>chosen Easytrieve.
>

"Quick and dirty" reports often times turn out to be something users
need daily, weekly, monthly etc.  Easytrieve is quicker to write than
Cobol and is why it is often times chosen over Cobol.  I've run across
auditors and business analysts who can and do write Easytrieve but
couldn't begin to write a Cobol program.


>COBOL programmers who have been exposed to Easytrieve pick it up fairly 
>quickly; it isn't rocket science.
>

True.

>I see this as a pointless exercise...
>

If you mean, converting your Easytrieve to Cobol, I agree.

>Pete.
>

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Bart, a woman is like a beer. They look good,
they smell good, and you'd step over your own
mother just to get one."
---Homer Simpson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-12-17T09:58:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0ladm3plvseamil9sgd8t5taj3v2qpgivl@4ax.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net> <iu7dm39op8v0na0abgpfc57h28874upct2@4ax.com>`

```
On Mon, 17 Dec 2007 11:18:43 -0500, SkippyPB
<swiegand@nospam.neo.rr.com> wrote:

>"Quick and dirty" reports often times turn out to be something users
>need daily, weekly, monthly etc.  Easytrieve is quicker to write than
>Cobol and is why it is often times chosen over Cobol.  I've run across
>auditors and business analysts who can and do write Easytrieve but
>couldn't begin to write a Cobol program.

But I haven't run across their programs that were written the way
programmers would.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-12-18T12:33:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5sofa9F1ajt0jU1@mid.individual.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net> <iu7dm39op8v0na0abgpfc57h28874upct2@4ax.com>`

```


"SkippyPB" <swiegand@nospam.neo.rr.com> wrote in message 
news:iu7dm39op8v0na0abgpfc57h28874upct2@4ax.com...
> On Mon, 17 Dec 2007 13:41:02 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[65 more quoted lines elided]…
> If you mean, converting your Easytrieve to Cobol, I agree.

That was my meaning, so, good!

Pete.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 8)_

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2007-12-17T12:37:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56b14c78-445e-4255-a2c0-3b2f1eb276b0@p69g2000hsa.googlegroups.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net>`

```
On Dec 17, 12:41 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Michael Mattias" <mmatt...@talsystems.com> wrote in message
>
…[37 more quoted lines elided]…
> Pete.

I mostly agree, as someone else said Easytrieve plus can be compiled
and runs very quickly, at a similar speed to COBOl.

I suppose if you wanted to disccontinue the use of Easytrieve
altogether and save the cost of the licence fee, it might be worth it,
though despite the pretty good formatting, I very much doubt whether
it would be as amaintainable and would best be applied for programs
for which no further changes are planned.  I would wish to see a
conversion of a program that produced at least one report and used at
least one internal sort if I were responsible for buying the product.
In fact, as I think about it some more, I would probably send off the
most complicated program in the system to see whether that was handled
properly, before making a commitment.

Robert
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-12-18T12:35:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5sofdmF1a56nuU1@mid.individual.net>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga> <V2%8j.40060$L%6.1928@bignews3.bellsouth.net> <PUa9j.6118$fl7.2912@newssvr22.news.prodigy.net> <5slussF1a03btU1@mid.individual.net> <56b14c78-445e-4255-a2c0-3b2f1eb276b0@p69g2000hsa.googlegroups.com>`

```


"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:56b14c78-445e-4255-a2c0-3b2f1eb276b0@p69g2000hsa.googlegroups.com...
> On Dec 17, 12:41 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[59 more quoted lines elided]…
> properly, before making a commitment.

There is a wealth of wisdom in your paragraph above, Robert.

Pete.
```

###### ↳ ↳ ↳ Re: CA-Easytrieve Users

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-12-17T09:56:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dadm35a3rgeq9l7p3q00utmt3c54d3o5t@4ax.com>`
- **References:** `<8dbbe9a8-e145-4009-bb2d-98ac739ca141@a35g2000prf.googlegroups.com> <8HR8j.30390$lD6.18005@newssvr27.news.prodigy.net> <1700a8ba-763c-48cb-a30a-a6f2b9113ff6@d27g2000prf.googlegroups.com> <DJV8j.39813$L%6.8000@bignews3.bellsouth.net> <BGY8j.6599$3b7.4994@newsfe23.lga>`

```
Of course, if the code is simple - why not leave it in EasyTrieve? If
it is complex and unclear, then the converted result will be complex
and unclear.

I worked at a shop once that used to be 100% RPG II.   Programmers
knew how to do some very obscure tricks to accomplish their needs.
When we added CoBOL, new RPG programs were all simple, but some of the
old stuff was unmaintainable.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
