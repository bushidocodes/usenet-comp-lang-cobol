[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 88 Level Q

_14 messages · 11 participants · 2001-05_

---

### 88 Level Q

- **From:** Aaron J Roquena <aroque1@uic.edu>
- **Date:** 2001-05-14T09:47:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
        I've just been thrown into some COBOL programming recently. I got
a COBOL book but it doesn't discuss scope very well. I was wondering if
something like this is legal. COND-1 and COND-2 are conditionals used for
2 fields. I would like to use the same name becuase logically they
represent identical things. Should I make  FIELD-1's conditionals have a
different nameS than FIELD-2's? No one over here knows.

01 FILE-LAYOUT.
   05 FIELD-1                    PIC X(1).
      88 COND-1                   VAL '0'.
      88 COND-2                   VAL 'A'.
   05 FIELD-2                    PIC X(1).
      88 COND-1                   VAL '0'.
      88 COND-2                   VAL 'A'.

 Thanks for your time!
```

#### ↳ Re: 88 Level Q

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-05-14T15:26:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HOSL6.5041$DW1.227334@iad-read.news.verio.net>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
In article <Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>,
Aaron J Roquena  <aroque1@uic.edu> wrote:
>        I've just been thrown into some COBOL programming recently.

Then your boss deserves what s/he gets.

>I got
>a COBOL book but it doesn't discuss scope very well. I was wondering if
…[3 more quoted lines elided]…
>different nameS than FIELD-2's?

I would say 'yes'... and I believe that a few compilers might agree with
me.

>No one over here knows.
>
…[8 more quoted lines elided]…
> Thanks for your time!

Well, as Wittgenstein tells us, 'Logic is a game played by a particular
set of rules'... so I would argue that the two conditions do *not*
'logically... represent identical things'.  Consider:

01  FILE-LAYOUT.
    05 FIELD-1                    PIC X(1). 
       88 FLD1-CONTAINS-A-ZERO     VALUE '0'.
       88 FLD1-CONTAINS-AN-A       VALUE 'A'.
    05 FIELD-2                    PIC X(1).
       88 FLD2-CONTAINS-A-ZERO     VALUE '0'.
       88 FLD2-CONTAINS-AN-A       VALUE 'A'.

To say that these are logically identical seems like granting such
equivalence to conditions such as:

05  YOUR-BANK-BALANCE PIC S9(11)V99 VALUE +0.
    88  YOUR-BALANCE-IS-HIGH VALUE +1000000.
05  MY-BANK-BALANCE   PIC S9(11)V99 VALUE +0.
    88  MY-BALANCE-IS-HIGH   VALUE +1000000.
...
MOVE +1000000 TO YOUR-BANK-BALANCE.
EVALUATE TRUE
    IF MY-BALANCE-IS-HIGH
        PERFORM TITHE-TO-CHARITIES THRU TTC-EX
         UNTIL APPROPRIATE-OBLIGATIONS-FULFILLED
        PERFORM LIVE-WELL-N-EASY THRU LWNE-EX
         UNTIL CONSIDERED-A-CREDIT-2-COMMUNITY
    END-IF
END-EVALUATE.

... et and cetera.

DD
```

#### ↳ Re: 88 Level Q

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-05-14T18:45:11+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<suuvftop19gfrjetaolrkljlrnn8f75s69@4ax.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
On Mon, 14 May 2001 09:47:29 -0500 Aaron J Roquena <aroque1@uic.edu> wrote:

:>        I've just been thrown into some COBOL programming recently. I got
:>a COBOL book but it doesn't discuss scope very well. I was wondering if
:>something like this is legal. COND-1 and COND-2 are conditionals used for
:>2 fields. I would like to use the same name becuase logically they
:>represent identical things. Should I make  FIELD-1's conditionals have a
:>different nameS than FIELD-2's? No one over here knows.

:>01 FILE-LAYOUT.
:>   05 FIELD-1                    PIC X(1).
:>      88 COND-1                   VAL '0'.
:>      88 COND-2                   VAL 'A'.
:>   05 FIELD-2                    PIC X(1).
:>      88 COND-1                   VAL '0'.
:>      88 COND-2                   VAL 'A'.

You don't have to, but the fields become quite clumsy if you don't - you would
have to qualify them, i.e., COND-1 of FIELD-1. 
```

#### ↳ Re: 88 Level Q

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-05-14T17:15:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ipUL6.836$6j3.76758@www.newsranger.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
Hi Aaron,

Here's a few ways to "work around" the prob:

Code the conds F1-COND1, F2-COND1, etc
Move fld1 fld2 to a wrk-fld with the 88s there, then code IF WRK-COND-1, etc.
not sure about this: code IF COND-1 OF FIELD-2, etc. Not sure if OF works
w'conditionals.

Hope this helps, Jack.



In article <Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>, Aaron J
Roquena says...
>
>        I've just been thrown into some COBOL programming recently. I got
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: 88 Level Q

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-14T12:44:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9dp5eu$o0i$1@slb0.atl.mindspring.net>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu> <ipUL6.836$6j3.76758@www.newsranger.com>`

```
Yes, "of" works with 88-levels.  Whether or not it is a "good" way to
program is another question.  I find it fairly unusual and medium-ugly - but
there is nothing "theoretically" wrong with it.
```

#### ↳ Re: 88 Level Q

- **From:** weberm@news.polaris.net (Michael Weber)
- **Date:** 2001-05-25T17:03:51+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<9em39m$7he$3@news.utelfla.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
Aaron J Roquena (aroque1@uic.edu) wrote:

:         I've just been thrown into some COBOL programming recently. I got
: a COBOL book but it doesn't discuss scope very well. I was wondering if
: something like this is legal. COND-1 and COND-2 are conditionals used for
: 2 fields. I would like to use the same name becuase logically they
: represent identical things. Should I make  FIELD-1's conditionals have a
: different nameS than FIELD-2's? No one over here knows.
: 
: 01 FILE-LAYOUT.
:    05 FIELD-1                    PIC X(1).
:       88 COND-1                   VAL '0'.
:       88 COND-2                   VAL 'A'.
:    05 FIELD-2                    PIC X(1).
:       88 COND-1                   VAL '0'.
:       88 COND-2                   VAL 'A'.

If FIELD-1 and FIELD-2 are the same, why use two variables?
```

##### ↳ ↳ Re: 88 Level Q

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-05-25T16:58:01-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<4145699b.0105251558.21b69011@posting.google.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu> <9em39m$7he$3@news.utelfla.com>`

```
weberm@news.polaris.net (Michael Weber) wrote here knows.
> : 
> : 01 FILE-LAYOUT.
…[7 more quoted lines elided]…
> If FIELD-1 and FIELD-2 are the same, why use two variables?

Come on! FIELD-1 and FIELD-2 are NOT the same, they are two different
fields whose data may or may not be the same. They MAY contain the
same values, or they may not!

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: 88 Level Q

- **From:** weberm@news.polaris.net (Michael Weber)
- **Date:** 2001-05-31T16:59:58+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<9f5tae$qp7$4@news.utelfla.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu> <9em39m$7he$3@news.utelfla.com> <4145699b.0105251558.21b69011@posting.google.com>`

```
Stephen J Spiro (stephenjspiro@hotmail.com) wrote:

: Come on! FIELD-1 and FIELD-2 are NOT the same, they are two different
: fields whose data may or may not be the same. They MAY contain the
: same values, or they may not!

If memory serves me right, the orignal poster stated that the two
were the same. Is there an alternative to Deja News that actually WORKS?
```

###### ↳ ↳ ↳ Re: 88 Level Q

_(reply depth: 4)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-05-31T21:45:52+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<20010531174552.11877.00001996@ng-ft1.aol.com>`
- **References:** `<9f5tae$qp7$4@news.utelfla.com>`

```
>From: weberm@news.polaris.net  (Michael Weber)
>Date: 2001-05-31 12:59 Eastern Daylight Time

>Stephen J Spiro (stephenjspiro@hotmail.com) wrote:
>
…[5 more quoted lines elided]…
>were the same. Is there an alternative to Deja News that actually WORKS?

Technically, it doesn't matter what he said.  
His code said they were not the same.  
As I remember, he said the 88-level possibilites were the same for
each of the two different fields.  [My interpretation]

Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: 88 Level Q

_(reply depth: 4)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-05-31T14:48:20-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<4145699b.0105311348.3a9ddb14@posting.google.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu> <9em39m$7he$3@news.utelfla.com> <4145699b.0105251558.21b69011@posting.google.com> <9f5tae$qp7$4@news.utelfla.com>`

```
weberm@news.polaris.net (Michael Weber) wrote in message news:<9f5tae$qp7$4@news.utelfla.com>...
> Stephen J Spiro (stephenjspiro@hotmail.com) wrote:
> 
…[5 more quoted lines elided]…
> were the same. Is there an alternative to Deja News that actually WORKS?

Original post was "I would like to use the same name becuase logically
they
represent identical things. "

LOGICALLY, not physically. Physically, they could have different
values at any given time. They could also have the same values. That
is why there are two fields.

Stephen J Spiro
```

#### ↳ Re: 88 Level Q

- **From:** gencbl <azabala@cobol.com.ar>
- **Date:** 2001-05-25T19:12:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8yP6.425$G45.24150@news1.onlynews.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```


Aaron: write VALUE (no VAL) This source code can help you ?

       working-storage section. 01 FILE-LAYOUT. 05 FIELD-1 PIC X(1). 88
       COND-1 VALUE '0'. 88 COND-2 VALUE 'A'. 05 FIELD-2 PIC X(1). 88
       COND-1 VALUE '0'. 88 COND-2 VALUE 'A'.

       procedure division. entra. set cond-1 of field-1 to true set
       cond-2 of field-2 to true

           if cond-1 of field-1 display 'Condicion 1 del field-1 true'
           end-if if cond-2 of field-1 display 'Condicion 2 del field-1
           true' end-if

           if cond-1 of field-2 display 'Condicion 1 del field-2 true'
           end-if if cond-2 of field-2 display 'Condicion 2 del field-2
           true' end-if .



Aaron J Roquena  wrote:
  > I've just been thrown into some COBOL programming recently. I got a
  > COBOL book but it doesn't discuss scope very well. I was wondering if
…[6 more quoted lines elided]…
  >  Thanks for your time!
```

##### ↳ ↳ Re: 88 Level Q

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-05-26T22:03:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010526180358.25580.00001676@ng-ca1.aol.com>`
- **References:** `<e8yP6.425$G45.24150@news1.onlynews.com>`

```
>Date: 2001-05-25 15:12 Eastern Daylight Time
>Message-id: <e8yP6.425$G45.24150@news1.onlynews.com>
…[42 more quoted lines elided]…
>
Just to add some explanation to Mr. Zabala's code:  

The "05 FIELD-1" and "05 FIELD-2" does not mean they are
the same data.  Quite the opposite.  It means that they
are two different pieces of data of the same hierarchical rank. 
If this is all the fields declared under the "01" level, then
you have a record with a length of 2 bytes.  The first byte
is named "FIELD-1" and the second byte is named 
"FIELD-2."  
Although I cannot recommend using the same name for
the conditions, it is legal.  To interrogate a particular condition
you must "qualify" the reference--that is, tell the compiler
specifically which of your conditions you are talking about.  
So you must say "COND-2 OF FIELD-1" if you mean 
"FIELD-1  =  'A' " and you must say "COND-2 OF FIELD-2"
if you mean "FIELD-2 = 'A' " [double-quotes are mine.] 

Identical names (requiring the "OF" qualification) were very
popular when programs had to keyed in on punch cards.  
Giving boolean-like 88-level identifiers the same name
mystifies me.  It negates whatever dubious advantage
there may be to using 88's.  

Though the same code letter (zero of 'A') is being used, I
don't think they are "logically the same."  To me, it looks
like sheer coincidence.  
If FIELD-1 represents "DWI violations" and FIELD-2 represents 
"DUS violations" and if in both cases the code '0' means
"never got one" and code 'A' means "All the frigging time" 
then the two fields (not the conditions) are logically 
similar--but not identical.  Right?  After all, next week the
director may decide to add Code 'J' (meaning Just once but
it was a long time ago) as a possibility for the Driving-While-
Impaired field, but not for the Driving-Under-Suspension field.  
The following week he may announce that henceforth the
DWI field will be using the code 'A' to mean "Alcohol blood 
level of 2.2 or higher" and that code 'C' is going to mean 
"Constantly getting busted for drunk driving." 

I would rewrite your datanames as:  
01 AARONS-DRIVING-RECORD-LAYOUT. 
    05 ADR-FIELD-1-DWI-VIOLATIONS PIC X(1). 
         88 NO-VIOLATIONS-DWI       VALUE 'N'. 
         88 MANY-VIOLATIONS-DWI  VALUE 'A'. 
    05 ADR-FIELD-1-DUS-VIOLATIONS PIC X(1). 
         88 NO-VIOLATIONS-DUS       VALUE 'N'. 
         88 MANY-VIOLATIONS-DUS  VALUE 'A'. 

(Just to be extra picky, I have changed your term "FILE-LAYOUT"
to "RECORD-LAYOUT."  You're happy, right?
Also, I don't like your mixing numbers and letters--purely
for aesthetic reasons--so I changed your '0' to 'N.'  You're
still happy, right?)



  

Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: 88 Level Q

- **From:** "Sal Cambareri" <sal@lasermax.com>
- **Date:** 2001-05-27T13:44:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GEdQ6.6217$X4.649600@nntp2.onemain.com>`
- **References:** `<e8yP6.425$G45.24150@news1.onlynews.com> <20010526180358.25580.00001676@ng-ca1.aol.com>`

```
An alternative to unique condition names and qualification.

I'm not sure about the COBOL standard, but I know that AcuCobol supports the
following alternative for Aaron's code"

01 FILE-LAYOUT.
    03 FIELD-NAME       PIC X       OCCURS 2.
        88 COND-1            VALUE '0'.
        88 COND-2            VALUE 'A'.

Then in the procedure division COND-1(n) uniquely identifies the condition.

"Ross Klatte" <klatteross@aol.commmm> wrote in message
news:20010526180358.25580.00001676@ng-ca1.aol.com...
> >Date: 2001-05-25 15:12 Eastern Daylight Time
> >Message-id: <e8yP6.425$G45.24150@news1.onlynews.com>
…[26 more quoted lines elided]…
> >  > for 2 fields. I would like to use the same name becuase logically
they
> >  > represent identical things. Should I make FIELD-1's conditionals have
a
> >  > different nameS than FIELD-2's? No one over here knows.
> >  > 01 FILE-LAYOUT. 05 FIELD-1 PIC X(1). 88 COND-1 VAL '0'. 88 COND-2 VAL
…[14 more quoted lines elided]…
>
{snip}
>
> I would rewrite your datanames as:
…[21 more quoted lines elided]…
>
```

#### ↳ Re: 88 Level Q

- **From:** idnonada@home.com (TePeTo)
- **Date:** 2001-05-30T18:10:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1ee8a26.0105301710.65c92f@posting.google.com>`
- **References:** `<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>`

```
Aaron J Roquena <aroque1@uic.edu> wrote in message news:<Pine.GSO.4.10.10105140931520.6546-100000@icarus.cc.uic.edu>...
> I've just been thrown into some COBOL programming recently. I got
> a COBOL book but it doesn't discuss scope very well. I was wondering if
…[13 more quoted lines elided]…
>  Thanks for your time!
Perhaps the best ("quality") feature of Cobol is readability and self
documentation, IF the QUALITY of source code is kept in mind with the
rules of KISS.  Keep It Simple...  Reusing condition names or data
tags, or qualifying with "such-and-such" OF "so-and-so" is confusing
at best.  My experience has been that COMPILERS ARE DIFFERENT.  What
works right with one compiler may work differently with another
compiler *EVEN IN THE SAME SHOP*, and especially if multiple operating
systems (AND/OR) compilers are used.  Also keep future changes in
vendors (IBM or NCR to UNISYS), etc.  There is little I can add to
what others have written in response to your question, as they all
have good points.  Use techniques that will be compatible WITH ANY
COMPILER.  Also ensure that code such as (IF NOT condition OR NOT
condition) is ALWAYS AVOIDED.  Use (IF NOT condition AND NOT
condition) instead.  Avoid NOT OR NOT.
Good luck.  Jim
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
