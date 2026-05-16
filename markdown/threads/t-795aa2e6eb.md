[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IF statement question

_39 messages · 21 participants · 2000-09_

---

### IF statement question

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-20T01:32:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
I am trying to add an IF statement to my program for CIS160 class when i try to
do what i think is right i get this error message IF statement located where
imperative statement must be specified.

I am stuck (I think i made a big mess!!!!) here is the section of code:

200-PROCESSING.
     PERFORM UNTIL EOF-FLAG = 'Y'
         READ INVENTORY-FILE
	       AT END
		   MOVE 'Y' TO EOF-FLAG
         NOT AT END
         IF IR-QTY-ON-HAND < IR-REORDER-POINT  
         ADD 1 TO WS-COUNT-2
	       ELSE
	       
	   DISPLAY IR-ITEM-NUMBER, ' ', IR-ITEM-DESCRIPTION
	       END-READ
     END-PERFORM


Thanks,
Deek
what would i do without all of you nice people?
```

#### ↳ Re: IF statement question

- **From:** Charles Hammond <ceh1@cec.wustl.edu>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000920101451.24107A-100000@ritz.cec.wustl.edu>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
In structured programming a technique that works is to have a read
paragraph that does nothing but read and set the flag to 'N' at end of the
file.  Then perform the read Paragraph once in the initialization routine.
Then have a process that is in a paragraph and perform that paragraph
until end-flag = 'y'.  In the process paragraph you have a perform read at
the end of the process.  when the read changes the end-flag to 'y' then
the process ends and EOJ is run.

mainline logic
  perform initialization-routine.
  perform process-routine until end-flag = 'y'.
  perform EOJ-routine.


Charles Hammond, BSIM Undergraduate Program

On 20 Sep 2000, Deek40 wrote:

> I am trying to add an IF statement to my program for CIS160 class when i try to
> do what i think is right i get this error message IF statement located where
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IF statement question

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g17mgd0.pminews@news.wanadoo.es>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <Pine.SOL.3.96.1000920101451.24107A-100000@ritz.cec.wustl.edu>`

```
On Wed, 20 Sep 2000 10:25:03 -0500, Charles Hammond wrote:

>In structured programming a technique that works is to have a read
>paragraph that does nothing but read and set the flag to 'N' at end of the
…[13 more quoted lines elided]…
>
What I always do is to define a FILE STATUS field and check for a status of
'10':
The logic stays the same, but I don't have to initialize and to set the flag
(I don't like flags)

mainline logic
  perform initialization-routine.
  perform process-routine until statusfield = '10' ( or an 88 level)
  perform EOJ-routine.


Just my opinion
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

#### ↳ Re: IF statement question

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C8E711.7E91BFCD@mb.sympatico.ca>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```


Deek40 wrote:

> I am trying to add an IF statement to my program for CIS160 class when i try to
> do what i think is right i get this error message IF statement located where
…[20 more quoted lines elided]…
> what would i do without all of you nice people?

Don't you need an END-IF before the END-READ?
```

#### ↳ Re: IF statement question

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qba46$f36n7$1@ID-39920.news.cis.dfn.de>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```

Deek40 <deek40@aol.com> wrote in message
news:20000919213222.11198.00000096@ng-fx1.aol.com...
> I am trying to add an IF statement to my program for CIS160 class when i
try to
> do what i think is right i get this error message IF statement located
where
> imperative statement must be specified.
>
…[19 more quoted lines elided]…
> what would i do without all of you nice people?

I would guess that it is the lack of a delimiter on the IF inside of the
READ.  Try putting END-IF before the END-READ and it should work....
```

#### ↳ Re: IF statement question

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kcvgss03i2oo5n5oaloj9be8auok7d4rtj@4ax.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
On 20 Sep 2000 01:32:22 GMT, deek40@aol.com (Deek40) wrote:
Deek,

you have an IF statement inside a NOT END part of a READ.  This is not allowable here,
because you forgot to terminate the IF with an END-IF, that is the conditional IF range
overlaps the READ - END-READ Range.  Adding an END-IF will make the CONDITIONAL IF into an
IMPERATIVE IF

HTH



>I am trying to add an IF statement to my program for CIS160 class when i try to
>do what i think is right i get this error message IF statement located where
…[21 more quoted lines elided]…
>what would i do without all of you nice people?


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Truth has always been found to promote the best interests of mankind... -- Percy Bysshe Shelley
```

#### ↳ Re: IF statement question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C8B6B5.FB9241DC@brazee.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
Two possible fixes:
1.  Add an END-IF  (It is not obvious that this changes the code to an imperative,
but try it).
2.  Add another PERFORM containing the IF (This is more obvious).

Of course, if you chose PERFORM, you are getting some serious nesting, and you
might want to move some of this code to its own paragraph.  If the compiler can get
confused (see fix #1), certainly maintenance programmers can get confused.

I would also work on aligning my code to make it easier to see which nested level
you are in.


Deek40 wrote:

> I am trying to add an IF statement to my program for CIS160 class when i try to
> do what i think is right i get this error message IF statement located where
…[20 more quoted lines elided]…
> what would i do without all of you nice people?
```

#### ↳ Re: IF statement question

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-09-20T01:59:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XRUx5.18049$3y3.234544@typhoon.austin.rr.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
as the compiler says, you cannot have IF statements
between a READ and an END-READ.

Deek40 <deek40@aol.com> wrote in message
news:20000919213222.11198.00000096@ng-fx1.aol.com...
> I am trying to add an IF statement to my program for CIS160 class when i
try to
> do what i think is right i get this error message IF statement located
where
> imperative statement must be specified.
>
…[19 more quoted lines elided]…
> what would i do without all of you nice people?
```

##### ↳ ↳ Re: IF statement question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q972n$aqq$1@nntp9.atl.mindspring.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <XRUx5.18049$3y3.234544@typhoon.austin.rr.com>`

```
Correct - but misleading.  Change (indentation shows the correction - but
isn't required)

        READ INVENTORY-FILE
        AT END
            MOVE 'Y' TO EOF-FLAG
         NOT AT END
           IF IR-QTY-ON-HAND < IR-REORDER-POINT
              ADD 1 TO WS-COUNT-2
           ELSE
              DISPLAY IR-ITEM-NUMBER, ' ', IR-ITEM-DESCRIPTION
        END-READ

to

        READ INVENTORY-FILE
        AT END
            MOVE 'Y' TO EOF-FLAG
         NOT AT END
           IF IR-QTY-ON-HAND < IR-REORDER-POINT
              ADD 1 TO WS-COUNT-2
           ELSE
              DISPLAY IR-ITEM-NUMBER, ' ', IR-ITEM-DESCRIPTION
            End-If
        END-READ

(adding that END-IF changes the "IF" statement from a conditional to
imperative statement)
```

##### ↳ ↳ Re: IF statement question

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-20T02:14:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000919221449.15807.00000049@ng-fx1.aol.com>`
- **References:** `<XRUx5.18049$3y3.234544@typhoon.austin.rr.com>`

```
What should i do to fix that?  I am new to COBOL and not sure of all the proper
things yet.  I am trying to get it though.

thanks,
Deek
```

###### ↳ ↳ ↳ Re: IF statement question

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-20T02:40:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsVx5.2975$l35.61256@iad-read.news.verio.net>`
- **References:** `<XRUx5.18049$3y3.234544@typhoon.austin.rr.com> <20000919221449.15807.00000049@ng-fx1.aol.com>`

```
In article <20000919221449.15807.00000049@ng-fx1.aol.com>,
Deek40 <deek40@aol.com> wrote:
>What should i do to fix that?

You should do your own homework.

>I am new to COBOL and not sure of all the proper
>things yet.

I am 'old' to COBOL and the same is true for me.

>I am trying to get it though.

By asking others to do it for you?  Please do your own homework.

DD
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 4)_

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-20T03:22:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000919232257.13906.00000382@ng-fb1.aol.com>`
- **References:** `<bsVx5.2975$l35.61256@iad-read.news.verio.net>`

```
ITs called I WAS STUCK, this is like my 2nd week of COBOL i sat here for 2
hours trying to use my text and my own COBOL skills(not much) and kept getting
the same error message over and over, here I was missing a simple thing, i
supplied my code so people know i did some stuff(even if it wasnt 100% right). 
My professor said as someone that knows what they r doing read over ur problem
code in hopes they can explain what u did wrong so you dont do it again.  Since
2 very intelligent people explained what i did wrong now i know to use the
END-IF statement and wont make that mistake again.  Someone please tell me if
what i asked was wrong after hearing my reasoning.

Thanks,
Deek
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q9b4k$lre$1@slb6.atl.mindspring.net>`
- **References:** `<bsVx5.2975$l35.61256@iad-read.news.verio.net> <20000919232257.13906.00000382@ng-fb1.aol.com>`

```
There are some who don't like ANY homework questions submitted to the NG.
There are others who will give you exact answers (especially when you show
your code and the error message - as you did) and there are some who will try
and "give you a hint" on where to look.

I usually do the latter - but in this case, I couldn't think of where to
"point you to" in your text/course material that wouldn't take me a WHOLE lot
more effort than showing you where your error was.

Hopefully, you now (better) understand the difference between conditional and
imperative statements - and not just what was wrong in this case.

In the future, don't be surprised if some people tell you to "do your own
homework" - however, if that seems to be the ONLY response(s) that you get,
it probably means that you haven't shown us enough "work of your own".
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 6)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5M%x5.2999$l35.62814@iad-read.news.verio.net>`
- **References:** `<bsVx5.2975$l35.61256@iad-read.news.verio.net> <20000919232257.13906.00000382@ng-fb1.aol.com> <8q9b4k$lre$1@slb6.atl.mindspring.net>`

```
In article <8q9b4k$lre$1@slb6.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>There are some who don't like ANY homework questions submitted to the NG.
>There are others who will give you exact answers (especially when you show
…[5 more quoted lines elided]…
>more effort than showing you where your error was.

Mr Klein... how about a simple 'consistency in the application of
scope-delimiters might alleviate the difficulty'?

DD
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 6)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-20T04:50:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000920005037.06611.00000063@ng-cj1.aol.com>`
- **References:** `<8q9b4k$lre$1@slb6.atl.mindspring.net>`

```
You're doing fine kid.  DocDwarf (DD) gets a bit testy at times (but we wuv him
anyway)  :).

You've shown your work etc and the error so you're on the right track.

So many have just posted the assignment and then 'demanded' that someone post
the code to do it that the group does get its hackles up at times.

Eileen
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mP%x5.3000$l35.62973@iad-read.news.verio.net>`
- **References:** `<8q9b4k$lre$1@slb6.atl.mindspring.net> <20000920005037.06611.00000063@ng-cj1.aol.com>`

```
In article <20000920005037.06611.00000063@ng-cj1.aol.com>,
YukonMama <yukonmama@aol.com> wrote:

[snippage]

>So many have just posted the assignment and then 'demanded' that someone post
>the code to do it that the group does get its hackles up at times.

This may be true, aye, but it does not excuse the error I made nor the
apologies which appropriately follow.

(Now, of course, my Great Plan is complete... I've made a public mistake
and I've apologised for it in order to show that I have Proper Character)

DD
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 5)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rK%x5.2997$l35.62405@iad-read.news.verio.net>`
- **References:** `<bsVx5.2975$l35.61256@iad-read.news.verio.net> <20000919232257.13906.00000382@ng-fb1.aol.com>`

```
In article <20000919232257.13906.00000382@ng-fb1.aol.com>,
Deek40 <deek40@aol.com> wrote:
>ITs called I WAS STUCK, this is like my 2nd week of COBOL i sat here for 2
>hours trying to use my text and my own COBOL skills(not much) and kept getting
…[6 more quoted lines elided]…
>what i asked was wrong after hearing my reasoning.

You are quite right; my error and apologies for giving you the same
response as given those who do not show any effort.

DD
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 6)_

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000920144232.14036.00000031@ng-fn1.aol.com>`
- **References:** `<rK%x5.2997$l35.62405@iad-read.news.verio.net>`

```
Thanks for all the responses and docdwarf thanks for the apology, it takes a
big dwarf(person) to do that.  I love cobol and am trying to learn as much as i
can, i just get stuck on some things yet.

Deek
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jI7y5.3057$l35.65347@iad-read.news.verio.net>`
- **References:** `<rK%x5.2997$l35.62405@iad-read.news.verio.net> <20000920144232.14036.00000031@ng-fn1.aol.com>`

```
In article <20000920144232.14036.00000031@ng-fn1.aol.com>,
Deek40 <deek40@aol.com> wrote:

[snippette]

>it takes a
>big dwarf(person) to do that.

Pfoo... you'se jes' easily impressed.

DD
```

###### ↳ ↳ ↳ Re: IF statement question

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c984c6.92699006@207.126.101.100>`
- **References:** `<XRUx5.18049$3y3.234544@typhoon.austin.rr.com> <20000919221449.15807.00000049@ng-fx1.aol.com>`

```
I've actually seen some compilers accept this.  However, what I do is
stick a Perform in there.....

On 20 Sep 2000 02:14:49 GMT, deek40@aol.com (Deek40) wrote:

>What should i do to fix that?  I am new to COBOL and not sure of all the proper
>things yet.  I am trying to get it though.
>
>thanks,
>Deek

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: IF statement question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8cissgb5rggt21tuug73s043el1242e32@4ax.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
On 20 Sep 2000 01:32:22 GMT deek40@aol.com (Deek40) wrote:

:>I am trying to add an IF statement to my program for CIS160 class when i try to
:>do what i think is right i get this error message IF statement located where
:>imperative statement must be specified.

:>I am stuck (I think i made a big mess!!!!) here is the section of code:

:>200-PROCESSING.
:>     PERFORM UNTIL EOF-FLAG = 'Y'
:>         READ INVENTORY-FILE
:>	       AT END
:>		   MOVE 'Y' TO EOF-FLAG
:>         NOT AT END
:>         IF IR-QTY-ON-HAND < IR-REORDER-POINT  
:>         ADD 1 TO WS-COUNT-2
:>	       ELSE
:>	       
:>	   DISPLAY IR-ITEM-NUMBER, ' ', IR-ITEM-DESCRIPTION
:>	       END-READ
:>     END-PERFORM

You have to convert to IF to an imperative statement.

The sequences

      IF .......
      ELSE .....
      END-IF

or

      READ  .....
      AT END  ......
      NOT AT END ......
      END-READ

or
        
      ADD  ......

are imperative in the sense that paths join and this unit of code is one
logical statement.  

The sequences

      ADD  ......
      ON SIZE ERROR

or
     
      IF   .......
      ELSE  ......

are not imperative because the clause is hanging until you get a period for
closure.  
```

#### ↳ Re: IF statement question

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfdu8$fel$1@nnrp1.deja.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
In article <20000919213222.11198.00000096@ng-fx1.aol.com>,
  deek40@aol.com (Deek40) wrote:
> I am trying to add an IF statement to my program for CIS160 class
when i try to
> do what i think is right i get this error message IF statement
located where
> imperative statement must be specified.
>
> I am stuck (I think i made a big mess!!!!) here is the section of
code:
>
> 200-PROCESSING.
…[14 more quoted lines elided]…
> Deek

Hi:

I don't know why I am the only one to say this, and I will
probably get yelled at for saying it, but:

You really need to test the FILE-STATUS after every I-O operation
in your program. Without the FILE-STATUS test, and appropriate
actions based on the test, your programs can not be totally dependable.
Putting a FILE-STATUS test and appropriate messages in your example
would change it considerably. You also need to be able to determine if
the data file has no records or only one record in it. Why your
instructor does not make you aware of this, I can't imagine.
There are a few dozen FILE-STATUS codes, see your manual. If you
do not make the test, and an error occurs, your program would
probably produce unpredictable results or crash or something.

If you have the time and the inclination, you might try writing
it in a non-structured way (although your instructor would
probably faint).

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: IF statement question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfik4$ueq$1@slb6.atl.mindspring.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com>`

```
I have NOTHING against adding/using File-status codes, HOWEVER, there are two
things that I would say about their use in this case:

1) There could be a DECLARATIVE, in which case there would be NO need for
file-status code checking "in-line"

2) In *most* cases, if you have checked the file-status after an OPEN *and*
you are doing a sequential READ statement *and* you check for "AT END" - then
it is probably (possible?) that you really DO want your program to "abend"
(die, abnormally terminate) if any other file-status occurs. (I can think of
some unusual exceptions to this, but I also know of many "production"
applications that intentionally work this way.)
```

###### ↳ ↳ ↳ Re: IF statement question

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-23T02:31:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000922223155.23666.00000319@ng-ca1.aol.com>`
- **References:** `<8qfik4$ueq$1@slb6.atl.mindspring.net>`

```
I personally haven't used DECLARATIVE. Guess I'm one of those that isn't too
clear on its use.  I also don't use FILE-STATUS on QSAM (aka flat files) but do
use them on VSAM (aka ISAM on pc's?).  Also GSAMs (although I haven't used a
GSAM in about 7 years).  

In our shop if a VSAM file doesn't do what you want it to do you display the
status, the key, the operation, and set the return code to stop processing.  In
all other cases yes we want a nice big messy abend so the operators will notice
what is going on :)  (At least we hope they do - I've gotten calls 3 hrs after
an abend has occured because someone wasn't paying attention).

We do have a few programs that use the invalid key clause on a flat file (which
means dang thing ran out of space) that display a message, places a 0 in the
return code, and then a stop run.  This in turn causes all sorts of headaches
in the morning when people start calling asking where the rest of the data is. 
We rip out that coding everytime we have to maintenance one of these cuties or
when we get bit in the posterior.

File-status has it's place as does an abend.  

Eileen
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o_1z5.4049$l35.87022@iad-read.news.verio.net>`
- **References:** `<8qfik4$ueq$1@slb6.atl.mindspring.net> <20000922223155.23666.00000319@ng-ca1.aol.com>`

```
In article <20000922223155.23666.00000319@ng-ca1.aol.com>,
YukonMama <yukonmama@aol.com> wrote:

[snippage]

>In our shop if a VSAM file doesn't do what you want it to do you display the
>status, the key, the operation, and set the return code to stop processing.  In
>all other cases yes we want a nice big messy abend so the operators will notice
>what is going on :)  (At least we hope they do - I've gotten calls 3 hrs after
>an abend has occured because someone wasn't paying attention).

A feller just told me a good'un t'other day... just happened last week.
Back in February there was... *something* that happened in one of these
ninety-year old, hundred-and-forty-three step, two-files-in,
VSAM-and-a-report-out, twelve-*billion*-&&TEMPnn-files jobs.

(note to the reader: if that made no sense there's no need to go on.  then
again... if that *did* make sense - gave a kind of 'I know *those*!'
tingle - then you know how the story turns out... and there's no need to
go on)

Anyhow, this feller determined that somewhere, somehow, deep in the bowels
of this mess two files being matched/merged got out of sync because
someone didn't code an error routine for a not-found condition on a
key-read to (another) VSAM for a name-field lookup... or something like
that.  He then coded a *whomper* (a whomper? a gen-yoo-wine *whomper*!) of
an error routine, complete with a full-page-sized 'ERROR' with each large
letter made of identical component letters... the classic, right?  He
codes that baby up, gets it slapped into Prod... and hears nothing about
it.

Seven months later... seven months later he gets called into the Corner
Office where his boss's boss is demanding an explanation as to why this
error is showing up again.  The feller points to the SYSOUT spread across
the desk and shows the 'ERROR' page - which also contains instructions for
fixing the error, whom to notify and restarting the job - and says that
this situation has been encountered and here are the instructions for
dealing with it.

Both his boss and his boss's boss say 'Hmmmmm... is that what that means?
We checked out the SAR (archived) outputs for this job for the past four
months and every one of them had a page like this... we thought it was
normal.'

DD
```

###### ↳ ↳ ↳ Re: IF statement question

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Zf2z5.831$N86.31351@paloalto-snr1.gtei.net>`
- **References:** `<8qfik4$ueq$1@slb6.atl.mindspring.net> <20000922223155.23666.00000319@ng-ca1.aol.com>`

```
I've noticed the ABEND is far and away the weapon of choice to wake up the
operators.

Ideologically, I'm not nuts about using an ABEND to report problems which
could be handled with FILE STATUS or DECLARATIVES and come to a "soft"
landing; however, unless and until someone comes up with a better way to
"raise the problem flag," I guess we'll be doing this for a long time to
come.
```

##### ↳ ↳ I/O failures, FILE-STATUS & aborts

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CB5F89.55EFFABA@brazee.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com>`

```
Foodman wrote:

> I don't know why I am the only one to say this, and I will
> probably get yelled at for saying it, but:

Possibly - but I don't consider this a yell...


> You really need to test the FILE-STATUS after every I-O operation
> in your program. Without the FILE-STATUS test, and appropriate
…[7 more quoted lines elided]…
> probably produce unpredictable results or crash or something.

In what environments do such errors produce unpredictable results?

There are conditions where a crash is a perfectly acceptable result of a
failed I/O command, as long as the system gives you the information needed
to easily trace down the error.  If the system does NOT give that
information, it is necessary to do it yourself (check the file status,
display the information, and THEN crash on purpose).  Or, as you say, when
such an error would produce unpredictable results.  Or when you have some
alternative desired behavior.

The "crash on purpose" is sometimes necessary to make sure the operators
notice and take appropriate action.  You don't code that way on an
interactive program.  I am unfamiliar with non-interactive CoBOL programs
on personal computers - does anybody do these here?  How do you handle
abort situations?
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZcVy5.5094$5p.32808@news2.mia>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net>`

```
The reason your instructor may not have explained about error checking
could be
    a) this is a 100 level class and therefore 'rank' amateurs (not even
novice yet)
        (does anyone remember when they took hid or her FIRST programming
course?)
    b) the instructor could an experienceless PHD who doesn't know better

Deek, If you can find a book by Shelley and Cashman (CIRCA 80) called
'STRUCTURED COBOL' or something similar, get it, next best will maybe
be something like 'C' or COBOL programmers.  A lot of it will be over your
head for now, but it gives pretty good explanations of the Language
Constructs.

But Deek, don't feel bad, I've seen some 'professional' COBOL programmers
who if I was in charge, I would fire on the spot for either laziness or
incompetence!

Good Luck

Howard Brazee <howard@brazee.net> wrote in message
news:39CB5F89.55EFFABA@brazee.net...
> Foodman wrote:
>
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 4)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-23T04:13:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000923001342.22224.00000506@ng-fx1.aol.com>`
- **References:** `<ZcVy5.5094$5p.32808@news2.mia>`

```
>From: "mangogwr" mangogwr@bellsouth.net 
>Date: 9/23/00 2:07 AM Eastern Daylight Time

>Deek, If you can find a book by Shelley and Cashman (CIRCA 80) called
>'STRUCTURED COBOL' or something similar, get it, 


Aaahhhh - Shelly and Cashman - such fond memories  :)  Yes indeed - find the
book.

Had 3 quarters of COBOL at the community college.  First 2 used the
Shelly/Cashman books.  Third quarter was by special request of the instructor
of the first two to teach structured code as it was just 'invented' .  He had
gone to an IBM seminar (if memory serves) and our first assignment was to
rewrite our final from the previous quarter in structured code.

Two years later I transfered to the university and was required to take COBOL
101 again (seems the 4 year school didn't accept their affiliated 2 year
schools credits in some things - grrrrr) and THAT is when I had the dumb PhD
instructor (who also wrote the book we had to use).  By that time I already had
my first programming job and he wasn't pleased I did my homework at my real
work :).
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi30t$h7q$1@nnrp1.deja.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net>`

```

> In what environments do such errors produce unpredictable results?

Hi:

Windows.

>
> There are conditions where a crash is a perfectly acceptable result
of a
> failed I/O command, as long as the system gives you the information
needed
> to easily trace down the error.  If the system does NOT give that
> information, it is necessary to do it yourself (check the file status,
> display the information, and THEN crash on purpose).  Or, as you say,
when
> such an error would produce unpredictable results.  Or when you have
some
> alternative desired behavior.
>
> The "crash on purpose" is sometimes necessary to make sure the
operators
> notice and take appropriate action.

Can't you TELL the operator something is wrong and DEMAND their
acknowledgement? BTW, is 'the system' the operating system or
the application system?


 You don't code that way on an
> interactive program.  I am unfamiliar with non-interactive CoBOL
programs
> on personal computers - does anybody do these here?  How do you handle
> abort situations?

All my report programs are non-interactive (except for letting
the user specify the content). If an error is encountered, the user
is notified and MUST acknowledge the error.
>

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qjaf7$ksj$1@slb1.atl.mindspring.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net> <8qi30t$h7q$1@nnrp1.deja.com>`

```
I don't know about other mainframes, but to explain to those who are NOT
familiar with IBM's MVS (aka OS/390), let me BRIEFLY explain *why* an ABEND
can be "better" than a clean "error report".

In "batch" jobs, it is possible to "group" a bunch of different steps (each
with its own program) into a "single run" (or job).  The way that IBM JCL
works, it is possible to tell the operating system WHAT to do with files
after EITHER a successful or an unsuccessful (ABEND) in that step.   OFTEN
you tell the system to "catalog" a new file if the step is successful but to
"delete" it if the step ABENDs.  Therefore, if you issue a "nice error
report" (even if someone pays attention to it) it will be marked as
"available" to the next Step in the same job (and possibly even other jobs) -
while if you INTENTIONALLY let/tell the application to ABEND (when there is a
problem), then no future step will "try" and work with this "bad" file.

I know of NO "comparable" methodology on PC's (well you could SORT-of emulate
it with batch or command files - but it would certainly be "unusual").
Therefore, what is GOOD methodology in one environment is bad in others.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CD04DA.C76535B7@istar.ca>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net> <8qi30t$h7q$1@nnrp1.deja.com>`

```
One of the major environments where abends make sense as a termination
is main frame batch.  They also make sense in certain database
environments because they trigger rollback procedures (IMS is one of
them).  In batch abnormal termination can trigger certain clean-up
procedures and interface with job scheduling systems.  (One of the major
IBM mainframe utilities is a two instruction utility that sets the
return code to zero and returns to caller thus activating pre-call
allocation services and post-call termination services).  Thus the
system default of abend on I-O error for batch can be adequate.  In the
programs I have written I have defaulted to standard handling for
sequential files and used status code checking for random access and
direct access files.  Note the programs have status code checked all I-O
operations with status code defined.  I also normally have only one
instance of each verb for each file (only 1 OPEN for each type of OPEN,
only 1 READ, only 1 READ NEXT, etc.) and if there was more than 1
logical place to execute the I-O, the I-O was performed.  Status code
checking was also done for sequential files where the standard error
default was not the action desired.

I have not used declaratives in any of the programs I have written for
the past 30 years.  The reason is that DECLARATIVES would allow me to do
anything that status code checking wouldn't let me do.  

For CICS I have inherited programs that established HANDLE conditions
for I-O exceptions and others that used the response codes.  I have
wished for the time and authorization to eliminate all use of HANDLE
conditions except HANDLE program abend and other events not triggered by
CICS calls.  A HANDLE condition is sort of a resetable DECLARATIVE with
all sorts of potential for unexpected consequences if not established
properly for all generic conditions and not fully reset before each
specific CICS call (EXEC CICS verb).

I would like to see a generic DECLARATIVE - USE ON INITIAL ENTRY and I
will look into the exception handling in the next standard.  

Clark Morris, CFM Technical Programming Services, cfmtech@istar.ca    

Foodman wrote:
> 
> > In what environments do such errors produce unpredictable results?
…[42 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF6B31.6EF562BA@brazee.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net> <8qi30t$h7q$1@nnrp1.deja.com>`

```


Foodman wrote:

> > In what environments do such errors produce unpredictable results?
>
> Hi:
>
> Windows.

I guessed as much.


> > There are conditions where a crash is a perfectly acceptable result
> of a
…[15 more quoted lines elided]…
> acknowledgement?

Not easily.  Display upon console has been disabled in most shops for
decades.  And standard aborts ARE noticed and acted upon.

> BTW, is 'the system' the operating system or the application system?

Both and more.  Such products as CA7 which schedule jobs with dependencies
also understand standard aborts.


>  You don't code that way on an
> > interactive program.  I am unfamiliar with non-interactive CoBOL
…[6 more quoted lines elided]…
> is notified and MUST acknowledge the error.

That's the main criterion - all such errors MUST be responded to.  In my
environment, the surest way to do this is via a standard abort.  I don't
know how you do this with PC batch jobs.  I suppose it isn't common to have
scheduling software.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 5)_

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qt04t$u6v$1@nnrp1.deja.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net> <8qi30t$h7q$1@nnrp1.deja.com> <39CF6B31.6EF562BA@brazee.net>`

```
In article <39CF6B31.6EF562BA@brazee.net>,
  Howard Brazee <howard@brazee.net> wrote:

Just use the statement
FILE STATUS IS FILE-CHK in the select statement and make a storage
named FILE-CHK and check the value in the open statement.
Then display it if it isnt zero, print the file name and FILE-CHK,
close all the files OPEN, and STOP RUN.



>
>
…[10 more quoted lines elided]…
> > > There are conditions where a crash is a perfectly acceptable
result
> > of a
> > > failed I/O command, as long as the system gives you the
information
> > needed
> > > to easily trace down the error.  If the system does NOT give that
> > > information, it is necessary to do it yourself (check the file
status,
> > > display the information, and THEN crash on purpose).  Or, as you
say,
> > when
> > > such an error would produce unpredictable results.  Or when you
have
> > some
> > > alternative desired behavior.
…[13 more quoted lines elided]…
> Both and more.  Such products as CA7 which schedule jobs with
dependencies
> also understand standard aborts.
>
…[3 more quoted lines elided]…
> > > on personal computers - does anybody do these here?  How do you
handle
> > > abort situations?
> >
…[4 more quoted lines elided]…
> That's the main criterion - all such errors MUST be responded to.  In
my
> environment, the surest way to do this is via a standard abort.  I
don't
> know how you do this with PC batch jobs.  I suppose it isn't common
to have
> scheduling software.
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D209C1.924FC0FF@brazee.net>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <8qfdu8$fel$1@nnrp1.deja.com> <39CB5F89.55EFFABA@brazee.net> <8qi30t$h7q$1@nnrp1.deja.com> <39CF6B31.6EF562BA@brazee.net> <8qt04t$u6v$1@nnrp1.deja.com>`

```
How does this guarantee that the next dependent job in the schedule
doesn't get run?

Or do PC users even have scheduling software?  Is this obvious enough
that your clerk knows to call someone before submitting the next job?

I am not being antagonistic - I am being curious.  What I don't know
about processing on a PC may hurt me in the future.


lcccpiasabird@my-deja.com wrote:
> 
> In article <39CF6B31.6EF562BA@brazee.net>,
…[6 more quoted lines elided]…
> close all the files OPEN, and STOP RUN.

...

> > That's the main criterion - all such errors MUST be responded to.  In
> my
…[4 more quoted lines elided]…
> > scheduling software.
```

###### ↳ ↳ ↳ Re: I/O failures, FILE-STATUS & aborts

_(reply depth: 7)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000927183014.15880.00000475@nso-fm.aol.com>`
- **References:** `<39D209C1.924FC0FF@brazee.net>`

```
In article <39D209C1.924FC0FF@brazee.net>, Howard Brazee <howard@brazee.net>
writes:

>
>How does this guarantee that the next dependent job in the schedule
…[4 more quoted lines elided]…
>

I am not too familiar with how things would work in the Windows environment,
but I think that the DOS level BAT files were able to check the ERRORLEVEL
which (I think) is the equivalent to the IBM Mainframe RETCODE.
If the people setting up the BAT files were concerned about proper EOJ/ABEND
type closing status , edits would be placed in the BAT file for ERRORLEVEL
==0 GOTO GOODEOJ or fall thru to GOTO :BADEOJ

<bat file>
<drive>:\<path>\<program>
if errorlevel ==0 goto :GOODEOJ
goto :BADEOJ
:GOODEOJ
echo next program step to run
goto :EXIT
:BADEOJ
echo <program> ABENDed : reload and try again
goto :EXIT
:EXIT
exit
```

#### ↳ Re: IF statement question

- **From:** David Bretz <DBretz@mescoma.com>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D0CB98.5AF22EEA@mescoma.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com>`

```
NOT AT END is an imperative statement....meaning that NOT AT END can
only be followed by some action (ie. MOVE, etc) not a conditional
expression like IF.



Deek40 wrote:
> 
> I am trying to add an IF statement to my program for CIS160 class when i try to
…[21 more quoted lines elided]…
> what would i do without all of you nice people?
```

##### ↳ ↳ Re: IF statement question

- **From:** "alan jones" <ob2@freeuk.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JHGA5.854$7h.8143@news2-win.server.ntlworld.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <39D0CB98.5AF22EEA@mescoma.com>`

```
just to add my two cents, why use the NOT AT END when you've alread flaged for AT END.

instead of :

> > 200-PROCESSING.
> >      PERFORM UNTIL EOF-FLAG = 'Y'
…[11 more quoted lines elided]…
> >

try :

> > 200-PROCESSING.
> >      PERFORM UNTIL EOF-FLAG = 'Y'
> >          READ INVENTORY-FILE
> >                AT END
> >                    MOVE 'Y' TO EOF-FLAG
               END-READ

               IF EOF-FLAG NOT EQUAL 'Y' AND
                    IR-QTY-ON-HAND  <  IR-REORDER-POINT
> >              ADD 1 TO WS-COUNT-2
> >         ELSE
…[3 more quoted lines elided]…
> >


David Bretz <DBretz@mescoma.com> wrote in message news:39D0CB98.5AF22EEA@mescoma.com...
> NOT AT END is an imperative statement....meaning that NOT AT END can
> only be followed by some action (ie. MOVE, etc) not a conditional
…[28 more quoted lines elided]…
> > what would i do without all of you nice people?
```

###### ↳ ↳ ↳ Re: IF statement question

- **From:** "alan jones" <ob2@freeuk.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PXGA5.864$7h.8525@news2-win.server.ntlworld.com>`
- **References:** `<20000919213222.11198.00000096@ng-fx1.aol.com> <39D0CB98.5AF22EEA@mescoma.com> <JHGA5.854$7h.8143@news2-win.server.ntlworld.com>`

```
whoops!

> try :
>
…[7 more quoted lines elided]…
>                IF EOF-FLAG NOT EQUAL 'Y'
                       IF IR-QTY-ON-HAND  <  IR-REORDER-POINT
> > >                  ADD 1 TO WS-COUNT-2
> > >             ELSE
> > >                  DISPLAY IR-ITEM-NUMBER, ' ', IR-ITEM-DESCRIPTION
> > >            END-IF
                 END-IF
> > >    END-PERFORM

alan jones <ob2@freeuk.com> wrote in message
news:JHGA5.854$7h.8143@news2-win.server.ntlworld.com...
> just to add my two cents, why use the NOT AT END when you've alread flaged for AT END.
>
…[69 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
