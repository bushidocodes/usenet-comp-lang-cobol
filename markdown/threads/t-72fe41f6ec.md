[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/DIALOGUE System

_200 messages · 23 participants · 2003-02 → 2003-03_

---

### COBOL/DIALOGUE System

- **From:** "Eddie Veness" <e.veness@blueyonder.co.uk>
- **Date:** 2003-02-12T21:42:44
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```
I am currently trying to edit a field which is filled by the user with 8
digits alphanumeric. I have to prevent the user from being able to leave a
space anywhere within those eight digits and finally creat an error message.
The error message I can handle, I just can't get my head around preventing
spaces.  I thought at first sight, simple enough but this is getting the
better of me. I have not been programming in COBOL for that long and I would
welcome any help.
```

#### ↳ Re: COBOL/DIALOGUE System

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-12T23:37:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4ADA79.D40C1A5C@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```


Eddie Veness wrote:

> I am currently trying to edit a field which is filled by the user with 8
> digits alphanumeric. I have to prevent the user from being able to leave a
…[4 more quoted lines elided]…
> welcome any help.

Eddie,

You haven't told us which 'screen tool' your are using, although from your
subject heading I'm taking a guess at Net Express Dialog System.

1. Assuming it was Screen Section check out the syntax for ACCEPT - where you
can use FULL, LENGTH-CHECK, UPPER on EXCEPTION etc.

2. Assuming it is a Windows based tool for GUIs - you can build in some of the
above features as you design your Dialogue entry field, (e.g. Numeric(only)
Upper or Uppercase (which gives you 'upper' and numerics).

3. From what you've written you have a pic x(08) which must be 'filled' -
possibly a Customer Account Number which must ALWAYS be 8 characters ?. Over and
above the GUI set-up above, which characters are acceptable - Uppercase Alpha
and Numerics but no spaces or ANY other characters such as "/", "-" etc.

I thought this would be easy until I started looking :-). You can't do IS
NUMERIC tests on pic x and you can't do IS ALPHABETIC-UPPER on pic 9's !!!  Plus
ALPHABETIC-UPPER also accepts the space character as valid. Check your on-line
Help for Class Condition tests for background on this, plus use of the SPECIAL
NAMES.

If you really want to tie it down you could do the following sort of validity
check. (This is off the top of my head so check the syntax)  :-

01 MyInputfield.
     05 charM occurs 8 pic x.

01 CharX                    pic x.
88 ValidAlpha    value "A" thru "Z".
88 ValidNumeric value 0 thru 9.

01 Avalue.                    pic x.
88 GoodValue              value 1.
88 BadValue                value 0.

set Badvalue to true
Perform varying n from 1 by 1 until n > 8

    move CharM(n) to CharX
    if  ValidAlpha OR ValidNumeric
       set GoodValue to true
       EXIT PERFORM
    End-if

End-Perform

If BadValue......... then your error routine

*** In the above I'm testing for 'positive' conditions. I intensely dislike
testing for negatives - just like a Cockney and he 'ain't got none' :-)

Be interesting to see what other responses you get.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-12T23:52:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4ADDE4.78844118@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca>`

```
OOPs ! that wont work. That's what you get when you don't compile ! Still haven't
compiled but following should work :-

01 MyInputfield.
     05 charM occurs 8 pic x.

01 CharX                    pic x.
88 ValidAlpha    value "A" thru "Z".
88 ValidNumeric value 0 thru 9.

01 Avalue.                    pic x..        **** should be pic 9.
88 GoodValue              value 1.
88 BadValue                value 0.

set GoodValue to true
Perform varying n from 1 by 1 until n > 8

    move CharM(n) to CharX
    if  ValidAlpha OR ValidNumeric
        continue

   else  set BadValue to true
       EXIT PERFORM
    End-if

End-Perform

If BadValue......... then your error routine

"James J. Gavan" wrote:

> Eddie Veness wrote:
>
…[63 more quoted lines elided]…
> Jimmy, Calgary AB
```

##### ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-13T01:19:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4af28c.362743046@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>Eddie Veness wrote:
>
…[21 more quoted lines elided]…
>possibly a Customer Account Number which must ALWAYS be 8 characters ?. Over
and
>above the GUI set-up above, which characters are acceptable - Uppercase Alpha
>and Numerics but no spaces or ANY other characters such as "/", "-" etc.
>
>I thought this would be easy until I started looking :-). You can't do IS
>NUMERIC tests on pic x and you can't do IS ALPHABETIC-UPPER on pic 9's !!!
Plus
>ALPHABETIC-UPPER also accepts the space character as valid. Check your on-line
>Help for Class Condition tests for background on this, plus use of the SPECIAL
…[32 more quoted lines elided]…
>Be interesting to see what other responses you get.

The sample is incorrect. It says if the first byte is ok, then the whole string
is ok. 

What is EXIT PERFORM? That's not standard COBOL. 

The code should read:

set Goodvalue to true
Perform varying n from 1 by 1 until n > 8
    move CharM(n) to CharX
    if  not (ValidAlpha or ValidNumeric)
       set BadValue to true
    End-if
End-Perform
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-13T02:20:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4AFD92.BB79A030@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net>`

```


Robert Wagner wrote:

>
> The sample is incorrect. It says if the first byte is ok, then the whole string
…[12 more quoted lines elided]…
> End-Perform

Beat you to it - found the error myself :-). 'Though I do admit your :-

    if not (ValidAlpha or ValidNumeric)

is better coding than my 'Continue'.

Wanna get into semantics Mr. 'COBOL Best Practices' ? EXIT-PERFORM - No it's not
COBOL '85 but is a Micro Focus extension which is now officially part of COBOL 2002
- no more than you do I want to wait 17 years until it's in a compliant COBOL 2002
compiler..

Make up your mind - which is it - OO is verbose OR the bozos on mainframes wont use
OO ? As for verbosity :-

***** Non- OO

perform BY-NAME-PARA
........

BY-NAME-PARA.

if not ByName
   set Byname to true
    perform CREATE-NAMELIST
End-if.

**** OO COBOL (M/F without 'Red tape')

invoke self "byName"
..............

Method-id. "byName".
if not ByName
    set Byname to true
    invoke self "createNamelist"
End-if
End Method "byName".

The OO method contains only one more line of code than the non-OO to signify the
'end' of the 'mini program'. To 'tart' it up I add comment lines for readability.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-13T07:59:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4b5056.4212514@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:
>Wanna get into semantics Mr. 'COBOL Best Practices' ? EXIT-PERFORM - No it's
not
>COBOL '85 but is a Micro Focus extension which is now officially part of COBOL
2002

The syntax is ambiguous. Suppose the program reads:

perform varying ... until ...
    perform until ....
        if  ...
            EXIT-PERFORM
        end-if
    end-perform
end-perform

Which perform does it exit, the inner or the outer?


>Make up your mind - which is it - OO is verbose OR the bozos on mainframes wont
use
>OO ? 

I retracted my assertion that OO COBOL is too verbose. I still believe mainframe
bozos .. excuse me, make that 'professionals' .. will be the last to adopt it. 

As for verbosity :-
>
>***** Non- OO
…[21 more quoted lines elided]…
>End Method "byName".

"set Byname to true" belongs inside the "createNamelist" method. Better
terminology would be 'NamelistCreated' in place of 'Byname'. 

Following mainframe standards, that would read 'perform 9000-BY-NAME-PARA'. As
though we didn't know it was a paragraph and couldn't find it with a text
editor. 

For an additional touch of realism, comment out rather than delete the old
non-OO code. 

I'm pleased to see you using OO COBOL. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-13T06:21:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2g2kt$7si$1@slb9.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net>`

```
The syntax is not at all ambiguous.  Read the 2002 Standard and you see all
the rules about EXIT PERFORM.  For that matter, I think you use Micro
Focus - read their LRM where they already have it as an extension.  (Along
with EXIT PERFORM CYCLE)
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-14T00:07:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4c333b.62306986@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>The syntax is not at all ambiguous.  Read the 2002 Standard and you see all
>the rules about EXIT PERFORM.  For that matter, I think you use Micro
>Focus - read their LRM where they already have it as an extension.  (Along
>with EXIT PERFORM CYCLE)

I read about it and learned it exits the inner loop. CYCLE exits the iteration.
More literate phrases would be EXIT CYCLE or EXIT ITERATION. 

Micro Focus also has EXIT PARAGRAPH, which is the same as NEXT SENTENCE if one
doesn't use periods. I avoid NEXT SENTENCE because it is non-portable. Most
compilers make it synonymous with CONTINUE; Micro Focus thinks it means 'after
the next period'. Restoring the significance of periods, which are generally
regarded as anachronistic, is an error by Micro Focus. In practice, there's a
big difference between CONTINUEing and going to the next period, which is
usually end of paragraph. 

Semantically,  the EXIT clauses and CONTINUE have the flavor of COBOL because
they begin with a verb, whereas NEXT SENTENCE does not. 

All these are disguised GO TOs. I thought we'd learned to do without GO TO. 

Robert



>--
>Bill Klein
…[75 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-14T14:44:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2hhv0$si4$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net>`

```
Robert Wagner wrote:

> Micro Focus also has EXIT PARAGRAPH, which is the same as NEXT SENTENCE if
> one doesn't use periods. 

The use of NEXT SENTENCE in any situation where 'not using periods' is 
viable is disallowed by the '85 standard, though this is an extension by MF.

> Most compilers make it synonymous with CONTINUE; Micro Focus thinks it
> means 'after the next period'. 

The standard states that it is disallowed anywhere this difference in 
interpreation would make a difference.

> Semantically,  the EXIT clauses and CONTINUE have the flavor of COBOL
> because they begin with a verb, whereas NEXT SENTENCE does not.

Syntactically the NEXT SENTENCE is not a statement (though it is as an 
extension in MF) but is a phrase in the IF statement.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-13T22:35:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2hrlp$r0d$1@slb1.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net>`

```
Robert,
   Can you provide an example of ANY (much less "most") compilers think that
"Next Sentence" and "Continue" are "synonymous"?

It is true that in *most* (but definitely not all) ANSI/ISO conforming
cases, the two are the same - but I know of *no* compiler that treats them
as identical in the following "fully conforming" source code:

If Test1 = "1"
   If Test 2 = "2"
       Display "1 and 2"
   Else
        Display "Compile with either Next Sentence or Continue to get
different results"
        If  Test3 = "3"
             If Test4 = "4"
                 Next Sentence
*                  or          *> give different results
                  Compile
             Else
                  Continue
*           No END-IF occurs here - so there is no END-IF with a NEXT
SENTENCE
*           Outer ELSE terminated IF ... NEXT SENTENCE ELSE ... construct
        Else
             Display "Test 3 is false"
        End-If
        Display "Test 3 is true or false - but CONTINUE is coded"
   End-If
   Display "Test 2 is true or false - but continue is coded"
End-If
Display "Always displayed with CONTINUE - never with NEXT Sentence"
     .
Display "Next Sentence goes here"

    ***

Note: If you try this on any ANSI'85 conforming compiler and it fails to
compile cleanly (with either CONTINUE or NEXT SENTENCE - but not both) then
you have a "bug" in that compiler.  The '85 Standard is "clear" that this is
legal and NEXT SENTENCE and CONTINUE are *definably" different things.  If
your style doesn't allow for periods within paragraphs, then you don't need
that last sentence - it is just there to show the difference between the two
constructs more clearly.
     .
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-14T18:56:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2i0i4$371$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2hrlp$r0d$1@slb1.atl.mindspring.net>`

```
William M. Klein wrote:

>    Can you provide an example of ANY (much less "most") compilers think
>    that
> "Next Sentence" and "Continue" are "synonymous"?

My understanding is that MicroFocus originally implemented their '85 
compiler Cobol/2 version 1.x) with this, but quickly realised that the it 
should be 'next full stop' and changed it.

> The '85 Standard is "clear" that this is legal 

I am not convinced that the standard itself is clear that this is legal.  I 
do understand that a clarification was asked for (and this alone implies 
that it wasn't clear), and that it was eventuially agreed that a nested IF 
with a NEXT SENTENCE phrase and without and END-IF within an IF .. END-IF 
was not disallowed by the standard when taken absolutely literally as 
written.

I am sure that this was unintentional and that NEXT SENTENCE should be 
disallowed anywhere within any IF .. END-IF.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-14T15:52:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2j3b6$qq8$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net>`

```

On 13-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> Micro Focus also has EXIT PARAGRAPH, which is the same as NEXT SENTENCE if one
> doesn't use periods. I avoid NEXT SENTENCE because it is non-portable. Most
…[4 more quoted lines elided]…
> usually end of paragraph.

I have argued against the elimination of periods on this forum before - and in
those discussions, the only reason I have seen for the one period paragraphs is
"it makes cutting and pasting easier".  Bah.   Fortunately, I have never had to
work with coders who believe periods are anachronistic.   To me, code that
depends upon a stylistic trick such as only having a period at the end of a
paragraph is non-portable and dangerous.

But my question is:  Which are these "most compilers" that make NEXT SENTENCE
synonymous with CONTINUE?   I was not aware that any compilers did this, much
lest most.

> Semantically,  the EXIT clauses and CONTINUE have the flavor of COBOL because
> they begin with a verb, whereas NEXT SENTENCE does not.
>
> All these are disguised GO TOs. I thought we'd learned to do without GO TO.

Certainly not in maintenance where we like to make minimal changes to a working
program.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-14T09:38:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:b2j3b6$qq8$1@peabody.colorado.edu...

> But my question is:  Which are these "most compilers" that make NEXT
SENTENCE
> synonymous with CONTINUE?   I was not aware that any compilers did this,
much
> lest most.

I can't answer the first question, although there are apparently some that
make this error, and that leads to further comments on your second sentence
above.  ISO/IEC 1989:2002 states in its justification for the archaization
of NEXT SENTENCE: "This phrase can be confusing, especially when specified
in a delimited-scope statement.  It is a common belief among users that
control is transferred to a position after the scope-delimiter rather than
to a separator period that follows it somewhere."  That second sentence
leads me to believe that some implementors might have MISinterpreted the
functioning of NEXT SENTENCE.

I agree with you that a "sentence" in COBOL terms is not synonymous with an
"imperative statement"; the former is ALWAYS terminated by a period, and
thus it seems to me that a control transfer to NEXT SENTENCE is ALWAYS to
the beginning of whatever sentence follows the period that marks the end of
the CURRENT sentence.  That users (and perhaps implementors) have
misunderstood the fact that in COBOL a SENTENCE has ended with a terminator
period since the beginning of time is unfortunate, but it's a
misunderstanding nonetheless.   That's part of the reason the current
standard recommends avoiding it.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-14T18:20:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2jc1t$14p$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com>`

```

On 14-Feb-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> I agree with you that a "sentence" in COBOL terms is not synonymous with an
> "imperative statement"; the former is ALWAYS terminated by a period, and
…[6 more quoted lines elided]…
> standard recommends avoiding it.

I would be surprised if implementers were confused.  I do know that IBM
mainframes allow it even when followed by an END-IF.  But it still goes to the
next period.   I don't use it and go so far as to replace it in maintenance
programs.

I am very much against the practice mentioned in this thread of making it the
equivalent of an EXIT PARAGRAPH, assuming that the paragraph is exactly one
sentence long.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-14T10:36:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2jcvf$2ea7$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <b2jc1t$14p$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:b2jc1t$14p$1@peabody.colorado.edu...

> I am very much against the practice mentioned in this thread of making it
the
> equivalent of an EXIT PARAGRAPH, assuming that the paragraph is exactly
one
> sentence long.

Aye, there's the rub.  If your paragraph is exactly one sentence long, then
a NEXT SENTENCE appearing within that sentence rightly transfers control the
same as EXIT PARAGRAPH would.

A not particularly serious proposal:   If NEXT SENTENCE is going to remain
in the standard, perhaps we need to add EXIT SENTENCE as a synonym for it.
That way, the verb would be imperative, and it would be semantically and
syntactically parallel to all the other EXITs!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T01:12:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4d940f.152644618@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
…[16 more quoted lines elided]…
>functioning of NEXT SENTENCE.

In my experience, most of them misinterpreted it.

>I agree with you that a "sentence" in COBOL terms is not synonymous with an
>"imperative statement"; the former is ALWAYS terminated by a period, and
…[6 more quoted lines elided]…
>standard recommends avoiding it.

This raises the question of what a sentence is. In English, as sentence may be
terminated by a period (full stop), question mark, explanation point (bang) or
NOTHING AT ALL. For example, if I were writing "The file name is foo.txt", I
would omit a period after txt to avoid the reader cutting and pasting an
extraneous period. I'd leave two spaces and capitalize the first word of the
next sentence. Similarly, if I wrote "Please email me at x@y.com", I would omit
a period after com. 

I contend a sentence is defined by its syntactical structure rather than by a
punctuation terminator. In the case of COBOL, the structure is V S O (... O). 
When I write "move a to b move c to d", syntactically there are two sentences. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-15T00:07:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302150007.39c40a50@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> In my experience, most of them misinterpreted it.

Please list your 'experience' of sufficient vendor implementations and
indicate which 'misinterpreted' it, and in what way, to justify your
claim of 'most'.
 
Given that you have also stated that "Most compilers make it
synonymous with CONTINUE" you may like to mention specifically which
ones that you imagine actualy do this.

The _only_ compiler that I know of that did this was a very early MF
Cobol/2 which was released _before_ the '85 standard was finalised and
thus wasn't necessarily a misinterpretation, but may have been based
on drafts that changed.

> This raises the question of what a sentence is. 

> In English, ....

Completely irrelevant.  This isn't english, or greek, or even
'merican.  It is COBOL, and sentences are completely defined in the
language.  If you had read a manual on the language you would know
that.

> I contend a sentence is defined by its syntactical structure rather than by a
> punctuation terminator. In the case of COBOL, the structure is V S O (... O). 
> When I write "move a to b move c to d", syntactically there are two sentences. 

You can't just make up your mind about something and then claim it as
some sort of revealed truth.  If you had two clues to rub together you
would know that those are two _statements_ and a 'sentence' is
_defined_ as being terminated by a full stop and a space.

Your arguments also lack coherence.

Yours claims have been:
     Most implentations misinterpreted it. 
     Most treat is as CONTINUE.

These are quite wrong, but you do seem to think that NEXT SENTENCE
does go to 'the next full stop', while arguing that sentences should
not need to end in a full stop.

You have shown that you _can_ 'read and learn' about EXIT PERFORM, now
try the rest of the manual.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-15T20:59:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4eaa37.29900879@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <217e491a.0302150007.39c40a50@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[4 more quoted lines elided]…
>ones that you imagine actualy do this.

I must concede defeat on this point. I searched most of the COBOL source on my
home PC, some of which dates back to 1990. There was not a single instance of
NEXT SENTENCE, while there were many CONTINUEs. Next I wrote a test program and
compiled it with Realia v3.1 dated 1987. It performed as you said -- by
transferring control to the next 'COBOL sentence' following a full stop.

Fujitsu v3 issued a Warning:
'NEXT SENTENCE' CANNOT BE SPECIFIED IN IF OR SEARCH STATEMENT WITH EXPLICIT
SCOPE TERMINATOR. ACCEPTED AS WRITTEN.
The executable did go to the next 'COBOL sentence'. 

>These are quite wrong, but you do seem to think that NEXT SENTENCE
>does go to 'the next full stop', while arguing that sentences should
>not need to end in a full stop.

I said Micro Focus goes to a full stop, which I believed to be discrepant with
most other compilers. Now I see they all do it. 

I must have discovered this in the '80s, stopped using NEXT SENTENCE, and
forgotten why. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-17T15:40:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2qvpv$1j3$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net>`

```

On 14-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> That second sentence
> >leads me to believe that some implementors might have MISinterpreted the
> >functioning of NEXT SENTENCE.
>
> In my experience, most of them misinterpreted it.

So you have an example?


> This raises the question of what a sentence is. In English, as sentence may be
> terminated by a period (full stop), question mark, explanation point (bang) or
…[4 more quoted lines elided]…
> omit a period after com.

I haven't heard this definition before.  Do you have a citation?   I generally
put in a space before the period as the best way to emulate a sentence in this
example.  But this is English you're talking about.  COBOL is an English-like
language, but it is not English.

> I contend a sentence is defined by its syntactical structure rather than by a
> punctuation terminator. In the case of COBOL, the structure is V S O (... O).
> When I write "move a to b move c to d", syntactically there are two sentences.

Not in COBOL.  A COBOL sentence has a very specific definition.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-18T09:31:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2tqkp$6l1$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e4d940f.152644618@news.optonline.net...

> This raises the question of what a sentence is. In English, as sentence
may be
> terminated by a period (full stop), question mark, explanation point
(bang) or
> NOTHING AT ALL. ...

> I contend a sentence is defined by its syntactical structure rather than
by a
> punctuation terminator. In the case of COBOL, the structure is V S O (...
O).
> When I write "move a to b move c to d", syntactically there are two
sentences.

Contend away.

It would probably be much less frustrating for you to determine what
definitions the rules for COBOL apply to terms like this rather than use
rules you think ought to apply and then find that they don't work the way
you want them to.

COBOL is, to be sure, based on the form of the English imperative sentence.
However, the rules for the formation of COBOL sentences (and COBOL
statements comprising COBOL sentences) are quite different from similar
rules for English (or German or Hill Bondo or Tlingkit).

I think if you studied the rules below and apply them to your COBOL
programming you would likely find yourself less frustrated with what you
perceive as the language's disconnect with reality as you wish to define
that reality to be.  Herewith reality for COBOL as defined in the "grammar
rules" for that language:

ANSI X3.23-1974, Page I-68, Section 4:  Glossary, defines "Sentence" as
follows:  "A sequence of one or more statements, the last of which is
terminated by a period followed by a space."  On Page I-70, this standard
also defines "Statement" as "A syntactically valid combination of words and
symbols written in the Procedure Division beginning with a verb."

ANSI X3.23-1985, Page III-22, Section III:  Glossary, defines "Sentence" as
"A sequence of one or more statements, the last of which is terminated by a
separator period."  On Page III-24, the definition for "Statement" is "A
syntactically valid combination of words, literals, and separators,
beginning with a verb, written in a COBOL source program."

ISO/IEC 1989:2002, Page 382, Section 14.4, Procedural statements and
sentences, contains the definition for "sentence" as follows:  "A sentence
is a sequence of one or more procedural statements, the last of which is
terminated by a separator period."  The same section defines "procedural
statement" as "A procedural statement is a unit of the COBOL language that
specifies an action to be taken.  Statement names are identified in table
13, Procedural statements."  This section goes on to explain that there are
three types of statements:  declarative, imperative and conditional, and the
aforementioned table.

I have not yet been able to get my hands on a copy of ANSI X3.23-1968 (I
have been trying to locate one for some years), but a copy of the "IBM DOS
Full American National Standard COBOL" dated May 1973 (file no. S360-24;
order No. GC28-6394-4) to which I have access has this to say:  "The
statement is the basic unit of the Procedure Division.  A statement is a
syntactically valid combination of words and symbols beginning with a COBOL
verb.  ..." and "A sentence is composed of one or more statements.  The
statements may optionally be separated by semicolons [or the word THEN].  A
sentence must be terminated by a period followed by a space."  (The phrase
in brackets in this quotation is identified as an IBM extension to standard
COBOL).

Likewise, the Unisys A Series COBOL ANSI-68 Programming Reference Manual
(Form 8600 0320, dated September 1991) states, under "Rules of procedure
formation" in Section 7:  "The Procedure Division":  "A sentence consists of
one or more statements and is terminated by a period followed by a space."
and "A statement is a syntactically valid combination of words and symbols
beginning with a COBOL verb."  My guess is, based on past experience, that
the wording in this manual is quite close to that in the 1968 standard.

Using your terms, it is a STATEMENT (not a sentence) that begins with a
"V"erb, and it isn't always defined as followed by an optional "S"ubject"
and an optional "Object".  I would argue that even in ENGLISH, "Move a to b
move c to d", "Move a to b; move c to d." and even the IBM extension "Move a
to b then move c to d." represent multiple STATEMENTS ("main clauses" in
Webster's Ninth definition of "compound sentence") that comprise arguably
single SENTENCES.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Statements, Sentences "and all that jazz" (was: COBOL/DIALOGUE System

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-18T12:20:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2tthf$c70$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com>`

```
Just a side note to Chuck's accurate post below.  The 2002 Standard has
eliminated the concept of a "verb" in COBOL.  This was *not* a change that I
was happy with - but did please people who didn't like calling the COBOL
word "IF" a "verb".  There is no replacement term introduced - all there is,
is a list of reserved words that start (procedural) statements.

It should be noted that the '85 Standard was a little (well actually QUITE)
sloppy on the use of the terms "verb" versus the term "statement".

None of this changes (in any way) the fact that a COBOL sentence is, was,
and probably will be for a long time in the future well defined as 1 or more
statements followed by a separator period.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-20T00:39:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5423be.388742903@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[30 more quoted lines elided]…
>that reality to be. <snip>

>Using your terms, it is a STATEMENT (not a sentence) that begins with a
>"V"erb, and it isn't always defined as followed by an optional "S"ubject"
…[4 more quoted lines elided]…
>single SENTENCES.

I cannot dispute the Rules of COBOL, which are clearly stated in the citations
you gave and I deleted for brevity. My problem is with incorrect word usage. 

A STATEMENT is bigger than a sentence. A statement can use more than one
sentence. The word they should have used is CLAUSE. 

Collins English Dictionary defines Sentence as: "a sequence of words capable of
standing alone to make an assertion, ask a question, or give a command, usually
consisting of a subject and a predicate containing a finite verb."  Simplified,
one subject and one predication. Note the lack of reference to punctuation.
Vocal English doesn't use punctuation nor does poetry, in many instances. Only
written English (and other languages with a writing tradition) use punctuation,
and when it does, a Compound Sentence is punctuated by a semi-colon (not
commonly used in COBOL)  or the word 'then' (an IBM extension). Lacking those
two, one clause is the 'main clause' while the others are subordinate. COBOL
doesn't have Compound Sentences. 

When scores on English language SAT are corelated with college major, computer
science comes in dead last .. below business, below education, below home
economics. 

What we have is a struggle between technicians who want to preserve the period
because they think it makes parsing easier vs. COBOL practitioners with some
literacy and 40 years bad experience with errant periods, especially the periods
that land in column 73. The 2002 standard recommends against using periods while
ambivalantly making them significant in NEXT SENTENCE. 

My Best Practice is don't use periods and don't use NEXT SENTENCE. Both are in
the same Legacy boat. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-19T17:11:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b319vj$2jao$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e5423be.388742903@news.optonline.net...

> I cannot dispute the Rules of COBOL, which are clearly stated in the
citations
> you gave and I deleted for brevity. My problem is with incorrect word
usage.
>
> A STATEMENT is bigger than a sentence. A statement can use more than one
> sentence.  The word they should have used is CLAUSE.

Sigh.

ANSI X3.23-1974, Page I-53, Section I, "Introduction to the Standard", Topic
4:  Glossary:  "A clause is an ordered set of consecutive COBOL
character-strings whose purpose is to specify an attribute of an entry."

ANSI X3.23-1974, Page I-64, same section, same topic:  "A phrase is an
ordered set of one or more consecutive COBOL character-strings that form a
portion of a COBOL procedural statement or of a COBOL clause."

If the standard were a grammar of written English, maybe.  It's not a
grammar of written English, it's a grammar of COBOL, and the definitions of
the various components of the language are specified in that grammar.  And
for the purposes of this discussion, the hierarchy in the Procedure Division
IS:  phrase, clause, statement, sentence, paragraph, section.  Best I can
tell, it's been that way since 1960.

If pigs had wings they could fly.  If we had some ham, we could have some
ham and eggs, if we had some eggs.  Shoulda.  Woulda. Coulda.

> Collins English Dictionary defines Sentence as: "a sequence of words
capable of
> standing alone to make an assertion, ask a question, or give a command,
usually
> consisting of a subject and a predicate containing a finite verb."
Simplified,
> one subject and one predication. Note the lack of reference to
punctuation.

The definition of "sentence" in COBOL is not found in the Collins English
Dictionary, it is found in the COBOL standard.

That being said, I prefer the Merriam-Webster dictionaries as more
definitive of American English (just as I prefer the Oxford for English
English).  The definition in the Ninth New Collegiate I have handy does
include reference to end punctuation (though indicates that it is optional).

> Vocal English doesn't use punctuation nor does poetry, in many instances.
Only
> written English (and other languages with a writing tradition) use
punctuation,
> and when it does, a Compound Sentence is punctuated by a semi-colon (not
> commonly used in COBOL)  or the word 'then' (an IBM extension). Lacking
those
> two, one clause is the 'main clause' while the others are subordinate.
COBOL
> doesn't have Compound Sentences.

I know of languages that do not distinguish between word, clause, sentence
and utterance.  What's your point?   What English does does not necessarily
apply to what Hill Bondo or Tlingkit or Tagalog or Mandarin do.  Or COBOL.

> What we have is a struggle between technicians who want to preserve the
period
> because they think it makes parsing easier vs. COBOL practitioners with
some
> literacy and 40 years bad experience with errant periods, especially the
periods
> that land in column 73.

What we have is the desire to preserve the value of existing programs as
they stand unless there is an overriding reason to make some component of
such programs obsolete.  What we have here is a sizeable body of people who
are called upon to maintain code that's been running just fine, thank you
very much, for a very long time.

<<The 2002 standard recommends against using periods while
> ambivalantly making them significant in NEXT SENTENCE.

NEXT SENTENCE is an ARCAIC element in ISO/IEC 1989:2002, and has been in
COBOL for a VERY long time (as previously indicated), and in every standard
in which it exists, it, and the associated "SENTENCE", mean EXACTLY what the
standard says they mean.  With some fleshing out of scope terminators in '02
COBOL, it is now POSSIBLE to AVOID periods, if you choose to do so as a
matter of style, but the 2002 standard does NOT MAKE periods any more
significant than they were in '85, '74 or '68, and the standards committee
is not likely to make "inter-paragraph" periods archaic, obsolescent,
obsolete OR illegal in COBOL until there's SUBSTANTIAL evidence that VERY
few EXISTING applications will be adversely affected -- whether they were
originally written  last week or forty years ago.

> My Best Practice is don't use periods and don't use NEXT SENTENCE. Both
are in
> the same Legacy boat.

That's fine for you.  Your choice.  And as to NEXT SENTENCE, the standards
folks actually agree with you (though I could be convinced that EXIT
SENTENCE might be of value as a synonym)!  But are you certain no
programmer's EVER going to cause your programs to break by adding periods
(or paragraph-names, for whatever reason)?   And do you feel justified in
taking the position "Well, HE can't POSSIBLY know REAL COBOL because HE
actually thinks that periods can be used in the PROCEDURE DIVISION!" without
being willing to bear any responsibility for, say, the company's bankruptcy?
All *his* fault for not being fluent in your style as pronounced by you as
Universal Truth, ex cathedra by virtue of your ordination?   I'm not
convinced.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-20T09:12:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e549c05.419538311@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e5423be.388742903@news.optonline.net...

>The definition of "sentence" in COBOL is not found in the Collins English
>Dictionary, it is found in the COBOL standard.

Let's put aside my comparison of COBOL grammar to English grammar and your
appeal to authority. I'll try to explain my objection to periods in abstract
terms that a systems-oriented person might find more understandable. 

We're all familiar with systems designed in layers. For instance, the ISO
7-layer model for communication. A cardinal tenant of this design is that each
layer be self-contained. A structure initiated at level n should be terminated
at level n, not by a sub rosa 'pass-through' from level n-1. 

The grammar of all languages -- English, COBOL and (whatever) -- contains two
layers: lexicon and syntax. Lexicon deals with the meaning of words; syntax
deals with the assemblage of words into larger structures such as clauses and
sentences. When I write language processing programs, including COBOL
compilers,I write one layer that deals with lexicon and a separate layer that
deals with syntax. 

Punctuation such as the period are words. Technically, they are called
logographs, meaning 'a symbol representing a word'. An easy example is '=',
which is synonymous with  'equal to'.

Because syntax deals with sentences, the logic about what terminates a sentence
should be at the syntax level. It should not be 'passed-through' from the
lexicon level. 

Does this make sense?

>are you certain no
>programmer's EVER going to cause your programs to break by adding periods
…[6 more quoted lines elided]…
>convinced.

When systems malfunction, there are two approaches to providing a solution. The
rational approach asks 'how can we prevent this from happening again'? The
emotional approach asks 'who's guilty?', we want to punish the guilty.' The
emotional approach provides short-term self-gratification by giving the
appearance something is being done, perhaps a deterrent put in place, when we
know in our heart it isn't so.

By shifting the discussion from 'what's right' to 'who's guilty', you are
attempting to move it from the rational plane to the emotional. 

Policy determines the fate of systems and institutions; Politics determines the
fate of individual people. The former is hopefully rational; the latter is
always emotional. I find it more productive to pursue rational solutions. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-20T10:58:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302201058.34ddb93f@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >The definition of "sentence" in COBOL is not found in the Collins English
> >Dictionary, it is found in the COBOL standard.
> 
> Let's put aside my comparison of COBOL grammar to English grammar and your
> appeal to authority. 

Chuck's wasn't an 'appeal to authority', it was simply pointing out
that when you contrived an 'appeal to authority', you used the wrong
authority:

  >> Collins English Dictionary defines Sentence as: ...

> I'll try to explain my objection to periods in abstract
> terms that a systems-oriented person might find more understandable. 

We are not arguing because we don't understand exactly what it is you
are saying, we are arguing because you are wrong.  Using condecending
terms doesn't make us more sympathetic to your ideas.
 
> [irrelelevant material deleted]

> Punctuation such as the period are words. Technically, they are called
> logographs, meaning 'a symbol representing a word'. An easy example is '=',
> which is synonymous with  'equal to'.

Punctuation is _not_ 'a symbol representing a word'. An '=' symbol is
_not_ punctuation.  The two groups of symbols are quite distinct
(though the same grphic may be used in both groups differently).  You
are confused because each punctuation symbol has a name (or several),
it doesn't mean that it is a symbol for that word.

> Because syntax deals with sentences, the logic about what terminates 
> a sentence should be at the syntax level. 

I thought that you said you were going to "put aside my comparison of
COBOL grammar to English grammar".

Natural languages are primarily spoken.  Sentences are terminated by
vocal signals: pauses or changes of inflection and intonation.  When
the language is written down it uses symbols to represent the
vocalisation.  In English (and several others) these symbols include
',;:." which represent different lengths of pausing, and "()-?!" which
also indicate changes in inflection and emphasis.

Cobol and other computer languages are not spoken.  They do not use
the punctuation symbols to indicate the same things.  Your attempt at
imposing rules intended to assist written forms of natural language
rules makes no sense at all.  While there may be some superficial
similarities to written natural languages this does not mean that
Cobol should use inappropriate rules.

> Does this make sense?

Only to you.

If you don't like the way Cobol is defined then go and find a language
you prefer, or write your own.
 
> the latter is always emotional. I find it more productive to pursue 
> rational solutions. 

Yet your arguments about what senteces are seem based entirely on your
emotion, obsession even.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-21T01:58:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5587c9.31506817@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:


>> Punctuation such as the period are words. Technically, they are called
>> logographs, meaning 'a symbol representing a word'. An easy example is '=',
…[6 more quoted lines elided]…
>it doesn't mean that it is a symbol for that word.

You are simply wrong. Every punctuation symbol represents a word. It may not be
enunciated in the spoken language, but it is still a word. 

>> Because syntax deals with sentences, the logic about what terminates 
>> a sentence should be at the syntax level. 
>
>I thought that you said you were going to "put aside my comparison of
>COBOL grammar to English grammar".

I thought I did. The message was about system hierarchies, independent of
language. 

>Natural languages are primarily spoken.  Sentences are terminated by
>vocal signals: pauses or changes of inflection and intonation.  When
…[3 more quoted lines elided]…
>also indicate changes in inflection and emphasis.

There are no pauses or questions in COBOL. We have only imperative sentences.

Granted, COBOL is written, but the 2002 standard discourages the use of periods.
I do as well. They don't contain any information. They're superfluous. 

>Cobol and other computer languages are not spoken.  They do not use
>the punctuation symbols to indicate the same things.  Your attempt at
…[3 more quoted lines elided]…
>Cobol should use inappropriate rules.

How are the rules inappropriate? I don't find them so. It seems to me that if
COBOL used English grammer and word meanings correctly, its reputation as the
most readable language would be enhanced. 

Aren't we in this forum because we love COBOL's readability?

Robert
```

###### ↳ ↳ ↳ Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-20T21:19:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b345r7$7q8$1@slb3.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```
Robert,
  Yet another statement that I don't know where you got it.  See below:
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-21T12:12:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e56179d.68332813@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Robert,
>  Yet another statement that I don't know where you got it.  See below:
…[15 more quoted lines elided]…
>periods - and as many periods as you might want within a single procedure.

Intra-paragraph periods are discouraged by:

..Designating NEXT SENTENCE as archaic
..Providing explicit terminators for IF, SEARCH and EVALUATE

If one uses explicit terminators and doesn't use NEXT SENTENCE then periods
serve no purpose (except paragraph termination).

Robert
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T16:07:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35isa$aak$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net>`

```

On 21-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> >There is NOTHING in the 2002 standard that in ANY WAY discourages the use of
> >periods - and as many periods as you might want within a single procedure.
…[4 more quoted lines elided]…
> ..Providing explicit terminators for IF, SEARCH and EVALUATE

Please go on.  How does this discourage the use of periods?

> If one uses explicit terminators and doesn't use NEXT SENTENCE then periods
> serve no purpose (except paragraph termination).

That's one purpose.   Another purpose is to make the language more English like,
which purpose you professed to think is valid.

A third purpose is that it makes it easier for compilers to check for END IF
mismatches.

Does the CoBOL verb COMPUTE discourage the use of the verb ADD ?
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57eb75.188118638@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net> <b35isa$aak$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 21-Feb-2003, robert@wagner.net (Robert Wagner) wrote:
…[5 more quoted lines elided]…
>mismatches.

Please give an example.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T04:16:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e584b15.212602848@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net> <b35isa$aak$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 21-Feb-2003, robert@wagner.net (Robert Wagner) wrote:
…[5 more quoted lines elided]…
>mismatches.

Please give an example.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-21T10:16:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35jch$jng$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net>`

```
Just because there are multiple options - doesn't mean that they are in any
way discouraged.  The Standard *does* have a way of "discouraging" use - and
that is putting an item in either the archaic or obsolete category - and
periods in the middle of paragraphs are NOT in that category.

According to your "theory", the Standard is "discouraging" the use of Add,
Subtract, Multiply, and Divide - because you COULD use COMPUTE to do the
same thing.   ADD is even *more* discouraged because you could use the SUM
intrinsic function.

You are simply WRONG in stating that periods in the middle of paragraphs are
being discouraged.  They are *not* required - but neither are comments,
using meaningful user-defined words, or any other "stylistic" feature of the
language.

Please, PLEASE, do not make erroneous statements about the COBOL Standards -
which you have (so far) shown little knowledge much less understanding of.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-21T11:46:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302211146.3a1f74eb@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >There is NOTHING in the 2002 standard that in ANY WAY discourages the use of
> >periods - and as many periods as you might want within a single procedure.
…[7 more quoted lines elided]…
> serve no purpose (except paragraph termination).

There is _NOTHING_ in these that discourages the use of full stops at
all.

It is entirely neutral on the issue.

The scope terminators were in the '85 standard, so no change there. 
NEXT SENTENCE was disallowed in an IF .. END-IF in '85.

You are obsessive about trying to stop people using full stops and are
just inventing all sorts of unsupportable nonsense arguments.

No one is going to change their style because of any of these silly
'reasons', just get over it.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57eb78.188121892@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b345r7$7q8$1@slb3.atl.mindspring.net> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[9 more quoted lines elided]…
>'reasons', just get over it.

The volume of responses indicates a significant portion of the COBOL community
regards periods as a symbol representing other practices to which they are
attached and are afraid of losing. Like falling into paragraphs, PERFORM ..
THRU, the superfluous 77 level and the sacred GO TO. 

You are defending a Culture, not a punctuation mark. 

Robert
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-23T11:32:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b38tr6$d1h$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com> <3e57eb78.188121892@news.optonline.net>`

```
Robert Wagner wrote:

>>No one is going to change their style because of any of these silly
>>'reasons', just get over it.
…[3 more quoted lines elided]…
> which they are attached and are afraid of losing. 

Some may use full stops, some use as few as possible, others use whatever 
they feel enhances the readability of their code _to_them_ and theirs. This 
is their personal choice.

Full stops will never be entirely eliminated, as you feel they should, they 
form a necessary function.

As it happens, I use as few as possible wherever practical, but I would not 
try to _impose_ my usage on others.
 
> You are defending a Culture, not a punctuation mark.

I am not defending either a culture or a punctuation mark, I am defending 
rational and cogent arguments from your onslaught of nonsense and made up 
silliness.

> Like falling into
> paragraphs, PERFORM .. THRU, the superfluous 77 level and the sacred GO
> TO.

These have absolutely nothing to do with whether one uses full stops or not 
and is just another crap argument.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T01:40:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5826a2.203270063@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com> <3e57eb78.188121892@news.optonline.net> <b38tr6$d1h$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>> The volume of responses indicates a significant portion of the COBOL
…[5 more quoted lines elided]…
>is their personal choice.

To most professionals, it's a shop choice. The shop publishes a stylebook
containing do's and don'ts, and uses 'code walkthrus' to ensure compliance. 
Some have a full-time staff who do nothing but police coding style. 

Most COBOL stylebooks were written in the '70s, or by programmers who stopped
growing in the '70s. 

>As it happens, I use as few as possible wherever practical, but I would not 
>try to _impose_ my usage on others.

The paper which started this discussion was a tutorial instructing newbies on
Best Practices. My secondary objective was to see it adopted as a stylebook by a
few companies (such as mine), so that 'code Nazis' would not _impose_ '70s style
COBOL on neophytes. They love to _impose_, usually after the code is tested and
ready to go into production. 
> 
>> You are defending a Culture, not a punctuation mark.
…[3 more quoted lines elided]…
>silliness.

Generally, ad hominem arguments are incorrect, not because they are unmannerly,
but because they are irrelevant. If the person doesn't hold himself to be an
authority then criticism of his character is irrelevant to the points he makes.
You must rebut his points or remain silent. 

This case is different because I DO claim to be an authority on Practical Use of
COBOL. My claim is based on forty years of writing a million lines of code and
supervising the write/rewrite of 5-10 million lines. 

So feel free to respond emotively. However, because this is a public forum, it
would be instructive to readers if you rebutted SOME of the points I make.
Otherwise, you'll sound like that 'poopie' guy. Readers don't benefit much from
learning I'm a low-IQ a-hole. 

Robert
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-23T10:45:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302231045.5d004a48@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com> <3e57eb78.188121892@news.optonline.net> <b38tr6$d1h$1@aklobs.kc.net.nz> <3e5826a2.203270063@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> You must rebut his points or remain silent. 
> 
> This case is different because I DO claim to be an authority on Practical Use of
> COBOL. My claim is based on forty years of writing a million lines of code and
> supervising the write/rewrite of 5-10 million lines. 

And I have 'only' 35 years of Cobol and several other languages.

You have, however, shown that you are _not_ an authority on what the
Cobol standards say, making several claims that were completely wrong.

You are obviously not an authority on natural languages, merely making
up arguments that you feel may support your crusade.

You certainly aren't an authority on personal motovation.  You will
not get anyone to change their style by implying they are incompetent.

> So feel free to respond emotively. However, because this is a public forum, it
> would be instructive to readers if you rebutted SOME of the points I make.
> Otherwise, you'll sound like that 'poopie' guy. 

Readers don't benefit much from
> learning I'm a low-IQ a-hole. 

In an earlier post about your 'byte level OS' you stated that the
comp.sci. types wouldn't reply with cogent arguments, but resorted to
insults.  At the time I offered that they had been giving arguments
which you simply ignored because you were too attached to your own
ideas, and eventually they just told you to fuck off because they
realised you would never listen.

Now why would I have thought that ?

> Readers don't benefit much from learning I'm a low-IQ a-hole. 

They learn that from your messages, not mine.
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-24T01:33:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5958fa.281706151@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com> <3e57eb78.188121892@news.optonline.net> <b38tr6$d1h$1@aklobs.kc.net.nz> <3e5826a2.203270063@news.optonline.net> <217e491a.0302231045.5d004a48@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> You must rebut his points or remain silent. 
>> 
>> This case is different because I DO claim to be an authority on Practical Use
of
>> COBOL. My claim is based on forty years of writing a million lines of code
and
>> supervising the write/rewrite of 5-10 million lines. 
>
…[3 more quoted lines elided]…
>Cobol standards say, making several claims that were completely wrong.

I did not claim to be an authority on COBOL standards; I said Practical Use.
(Why don't they jump on you for writing Cobol rather than COBOL?)

>You are obviously not an authority on natural languages, merely making
>up arguments that you feel may support your crusade.

Your arguments would be stronger if you provided examples of where I screwed up
linguistics. Name-calling may cut it in the small pond where you swim, but not
here in the big pond. 

>You certainly aren't an authority on personal motovation.  You will
>not get anyone to change their style by implying they are incompetent.

Most, not all, old-timers are beyond redemption. I was trying to teach
neophytes.

>
>> So feel free to respond emotively. However, because this is a public forum,
it
>> would be instructive to readers if you rebutted SOME of the points I make.
>> Otherwise, you'll sound like that 'poopie' guy. 
…[9 more quoted lines elided]…
>realised you would never listen.

I didn't write a 'byte level OS', I wrote an 'OO OS'. 

They responded poorly because they were immature, like our 'poopie'. One would
think that nearly universal college education for the middle class would at
least, at minimum, if nothing else, teach them to think rationally rather than
emotionally. To form conclusions based on evidence rather than feelings. It
hasn't. It's been a total waste of money.

>> Readers don't benefit much from learning I'm a low-IQ a-hole. 
>
>They learn that from your messages, not mine.

Let's let them judge for themselves .. based on substance rather than
name-calling. 

Robert
```

###### ↳ ↳ ↳ Re: Where did you get this? (was: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:31:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dhdu$66t$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e56179d.68332813@news.optonline.net> <217e491a.0302211146.3a1f74eb@posting.google.com> <3e57eb78.188121892@news.optonline.net> <b38tr6$d1h$1@aklobs.kc.net.nz> <3e5826a2.203270063@news.optonline.net>`

```

On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> This case is different because I DO claim to be an authority on Practical Use
> of
> COBOL. My claim is based on forty years of writing a million lines of code and
> supervising the write/rewrite of 5-10 million lines.

So in 5 years I will be as much of an authority as you and will suddenly see the
light?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-21T17:00:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b348ab$7rt$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```
Robert Wagner wrote:

>>Punctuation is _not_ 'a symbol representing a word'. 

> You are simply wrong. Every punctuation symbol represents a word. It may
> not be enunciated in the spoken language, but it is still a word.

What crap. If it is not enunciated in a spoken language it is not a word.

"punctuation: system of marks indicating pauses or logical and grammatical 
relationships in written language."

You are confused because each symbol has a name, which is quite different 
from 'representing a word'.
 
> I thought I did. The message was about system hierarchies, independent of
> language.

But you are still trying to relate two completely different systems.  Just 
because human speech is a language and Cobol is a 'language' doesn't mean 
that you can apply rules or hierarchies from one to the other.
 
> There are no pauses or questions in COBOL. We have only imperative
> sentences.

Exactly, which is why trying to relate english rules of punctuation (or 
what you term system hierarchies) to Cobol is meaningless babble.
 
> Granted, COBOL is written, but the 2002 standard discourages the use of
> periods. I do as well. They don't contain any information. They're
> superfluous.

Why didn't you just say how you feel about full stops instead of ranting on 
about irrelevancies.  Of course, you may have felt that it made your 
arguments seem quasi-intellectual, but in the end it just boils done to you 
think that 'full stops are silly'.

In fact full-stops are not superfluous.  They are still required at the end 
of every paragraph to eliminate ambiguity.

> How are the rules inappropriate? I don't find them so. It seems to me that
> if COBOL used English grammer and word meanings correctly, its reputation
> as the most readable language would be enhanced.

If you don't like the way Cobol is then either rewrite the standard and 
submit it to the committee for consideration or wander off and write a 
different language that you feel is better.

You also take an extremely insular view.  Many programmers don't have 
English as their first, or indeed as any, language. Cobol has a set of 
rules and usage that is appropriate and is well defined.  Natural languages 
have arbitrary, ill-defined and contradictory rules and exceptions.  Even 
when rules are followed it is still possible to result in ambiguity.
 
Using 'English grammer[sic] and word meanings' would degrade Cobol 
enormously and would result in prolonged arguments that could never be 
resolved.  Well, just like this one actually.

In any case you would probably want it the be 'American grammar and word 
meanings', which is quite a different matter again.

On the one hand you claim that making it more 'English like' would make it 
more readable, yet your actual code is _less_ like English.  Where is all 
the capitalisation of proper names, not even the start of a paragraph is 
capitalised?  Where are all the commas to separate the phrases? Why haven't 
you used noise-words such as 'then' to make it more English like?

The answer of course is that your argument has nothing to do with being 
'English like' or using 'English grammar and word meanings' at all.

It is a simple tirade against the use of full stops dressed up in an 
attempt to look quasi-intellectual.


> Aren't we in this forum because we love COBOL's readability?

Not specifically, no.  While that is an attribute of Cobol, it is, as with 
any other stylistic aspect, a matter of recognition.

What is found by any individual to be 'readable' is what one is used to.  
If one is used to all uppercase and full stops wherever possible then that 
is what one finds to be the most readable.  If one mostly sees mixed case 
and minimum full stops then that is found to be most readable.

You appear to use minimum full stops and all lower case and thus find that 
most readable.  But you seem to feel that your opinions are some sort of 
absolute rather than a matter of training and recognition.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-21T12:11:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e560ad0.65055203@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:
>Robert Wagner wrote:

>Cobol has a set of 
>rules and usage that is appropriate and is well defined.  Natural languages 
>have arbitrary, ill-defined and contradictory rules and exceptions.  Even 
>when rules are followed it is still possible to result in ambiguity.

The desire to remove ambiguity from programming languages gave us C's == to
represent equal comparison. Designers didn't want to use = because it means
assignment. As a result, a C programmer who writes 'if (a = b) ..;' gets b
copied into a then the result tested for zero. This is a common error, committed
even by seasoned programmers. The invention of '==' INCREASED misunderstanding
rather than decreasing it, as intended. 

We successfully deal with ambiguity in written and spoken language all the time.
In COBOL, we read the = in 'if a = b' as a relational operator, while
recognizing the = in 'compute a = b' as an assignment operator. The
disambiguation is not hard to understand. 

>On the one hand you claim that making it more 'English like' would make it 
>more readable, yet your actual code is _less_ like English.  Where is all 
>the capitalisation of proper names, not even the start of a paragraph is 
>capitalised?  Where are all the commas to separate the phrases? Why haven't 
>you used noise-words such as 'then' to make it more English like?

They are not phrases, they are sentences. In English, we need initial caps,
terminators, separators and joining adverbs because we do not write each
sentence on a separate line. In programming, line breaks provide sufficient
delineation of sentences. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T15:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35ffg$8bg$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net>`

```

On 21-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> They are not phrases, they are sentences. In English, we need initial caps,
> terminators, separators and joining adverbs because we do not write each
> sentence on a separate line. In programming, line breaks provide sufficient
> delineation of sentences.

In CoBOL, line breaks do no such thing.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-21T13:01:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302211301.50f45ad9@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> The desire to remove ambiguity from programming languages gave us 

Do you think that ambiguity should not be removed ?

> C's == to
> represent equal comparison. Designers didn't want to use = because it means
> assignment. 

Most computer languages differenciate between assignment and equality
is some way.  Pascal uses ':=' for assignment, other dissallow
contexts where these could be confused.

> As a result, a C programmer who writes 'if (a = b) ..;' gets b
> copied into a then the result tested for zero. 

This is _not_ a result of differentiating between assignment and
equality.  It is the result of C having assignment as an operator and
not a statement and of allowing expressions in conditionals.  These
features of C give it a great deal of power and flexability.

> This is a common error, committed
> even by seasoned programmers. 

No. Seasoned programmers are the ones that have learned to use tools
which eliminate this as a problem.

> The invention of '==' INCREASED misunderstanding
> rather than decreasing it, as intended. 
 
No. Wrong. Either assignment are to be the same thing as '=' which
means there is entire ambiguity and no understanding, or they are to
be different things, such as '=' and '==' or ':=' and '=' or some
other.  Obviously if they are different things then this is better
than 'no understanding'.

Oh and by the way, in "if ( a = b )" it tests for true if the result
is _not_ zero.  You may find this ambiguous, I don't.

> We successfully deal with ambiguity in written and spoken language all the time.

Complete crap.  You may feel that you deal with ambiguity
'successfully', but you probably just take it as support for your
predefined conclusions regardless of what was intended.

In many cases ambiguity is simply not noticed by the receiver, it is
only if the sender notices an inappropriate result that the ambiguity
is noticed and the message modified.

> In COBOL, we read the = in 'if a = b' as a relational operator, while
> recognizing the = in 'compute a = b' as an assignment operator. The
> disambiguation is not hard to understand. 

That is because you cannot put a COMPUTE into a condition.  Cobol
loses flexibility compared to other languages.

This is a result of the 'desire to remove ambiguity'.

But C's problems have nothing to do with the need to remove ambiguity
in Cobol. A full stop is required prior to a paragraph label in order
to remove ambiguity.

> They are not phrases, they are sentences. In English, we need initial caps,
> terminators, separators and joining adverbs because we do not write each
> sentence on a separate line. 

Yet more complete crap.

Capitals on initial words in a sentence, on proper names, acronyms and
others are a style designed to resolve ambiguity.  Punctuation
(terminators and separators) indicate pauses and intonation, and this
also resolves ambiguity.

Writing English on a separate line per sentence would not be a
substitute for this style.

We don't "need caps, etc' because we don't write each sentance on a
separate line".  If we did use a separate line we would _still_ need
capitals and punctuation.  If fact we do in poetry and in lists.

You wanted to make Cobol written in a more englishlike way to be more
readable, yet you reject the mechanisms that would do this, with
completely spurious arguments.

> In programming, line breaks provide sufficient
> delineation of sentences. 

Putting in line breaks for each statement, phrase, clause, sentence,
or whatever, is a _style_ not a requirement of the language.  Many
lanuages, including Cobol can be packed, even splitting words at the
end of a line.

Now it may be that you would prefer to use a language that enforces
line breaks and resolves ambiguity some diffeent way.  Well please do
so, either by moving on or by writing your own.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-21T14:08:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3681m$2t5p$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net> <217e491a.0302211301.50f45ad9@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0302211301.50f45ad9@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote

<<Many lanuages, including Cobol can be packed, even splitting words at the
end of a line.>>

Speaking of discouraged practices, the splitting of words at the end of a
fixed-form reference format source image is actively discouraged by the
current COBOL standard as an archaism.  The splitting of words across source
images is *not* permitted in free-form reference format.   See ISO/IEC
1989:2002 Page 8332, G.1, Archaic language elements, item 1, Continuation of
COBOL words

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57dc70.184273080@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net> <217e491a.0302211301.50f45ad9@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> The desire to remove ambiguity from programming languages gave us 
>
>Do you think that ambiguity should not be removed ?

Misunderstanding should be removed. Ambiguity in the lexicon can be resolved by
context in the syntax. 

>Most computer languages differenciate between assignment and equality
>is some way.  Pascal uses ':=' for assignment, other dissallow
>contexts where these could be confused.

Languages such as COBOL. 

>> As a result, a C programmer who writes 'if (a = b) ..;' gets b
>> copied into a then the result tested for zero. 
…[4 more quoted lines elided]…
>features of C give it a great deal of power and flexability.

The 'power' to shoot yourself in the foot. How often does a programmer need to
do assignment in the middle of a conditional?

>> This is a common error, committed
>> even by seasoned programmers. 
>
>No. Seasoned programmers are the ones that have learned to use tools
>which eliminate this as a problem.

You are referring to LINT. The existence of such safety nets demonstrates how
error-prone the language is.

>Oh and by the way, in "if ( a = b )" it tests for true if the result
>is _not_ zero.  You may find this ambiguous, I don't.

I said, "the result is tested for zero." How else would it determine the result
is_not_zero? Wait .. I have it .. use a ternary operator: if ((a = b) ? false :
true) .. ;  <pausing to admire the elegence of his code>

>In many cases ambiguity is simply not noticed by the receiver, it is
>only if the sender notices an inappropriate result that the ambiguity
>is noticed and the message modified.

That's called debugging. 

>> In COBOL, we read the = in 'if a = b' as a relational operator, while
>> recognizing the = in 'compute a = b' as an assignment operator. The
…[3 more quoted lines elided]…
>loses flexibility compared to other languages.

You should lobby for that feature, and even more strongly for function calls
which look like references to subscripted variables. The compiler sees 'COMPUTE
a = b(c);' cannot find an array named b, cannot find a function prototype,
therefore <fanfare> b must be a function (rather than a misspelling). It's
obvious. 

>But C's problems have nothing to do with the need to remove ambiguity
>in Cobol. A full stop is required prior to a paragraph label in order
>to remove ambiguity.

My COBOL pre-processor recognized paragraph names without a preceeding period.
When it saw a  one-word sentence not defined as data, that's a paragraph name.
Terminate the previous sentence with a period to placate the COBOL compiler. For
example, when presented with 'move a b c. move d e', it looked to see whether
'c' was defined as data. If not, it output:
     move a to b.
c.
     move d to e

I acknowledge that's as sloppy as the function call example above, which is why
I stopped using the preprocessor.

>Now it may be that you would prefer to use a language that enforces
>line breaks and resolves ambiguity some diffeent way.  Well please do
>so, either by moving on or by writing your own.

I did write my own preprocessor. For instance, it, along with APS and others,
honored indentation as significant. When people read source code, they see
subordination based on indentation, not explicit block terminators or level
numbers. It would be nice if compilers at least gave a warning when seeing an
out-dent without a preceeding terminator. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-22T21:31:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302222131.1fc6af3a@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net> <217e491a.0302211301.50f45ad9@posting.google.com> <3e57dc70.184273080@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> Misunderstanding should be removed. Ambiguity in the lexicon can be resolved by
> context in the syntax. 

That is correct.  In the case of Cobol labels the ambiguity is
resolved by have a full stop at the end of each paragraph.

> The 'power' to shoot yourself in the foot. How often does a programmer need to
> do assignment in the middle of a conditional?

If you don't like C then please do not use it.  C programmers do, in
fact, like the idiom of being able to do assignment in conditionals. 
In many cases this saves code repetition.

> You are referring to LINT. The existence of such safety nets demonstrates how
> error-prone the language is.

lint is one tool, in fact lint like facilities are in the compilers
now, just as they are in other languages.

For example some Cobol compilers will report unreachable code.  Does
this indicate how error-prone Cobol is ?

> You should lobby for that feature, 

No, I shouldn't.  Cobol has features that I like and C has features
that I like.  This does not mean that I _should_, or even want to, try
to impose those on others.

> and even more strongly for function calls
> which look like references to subscripted variables. 

No. I shouldn't.  Nor do I care for your attempt to tell me what I
should or shouldn't do.

> My COBOL pre-processor recognized paragraph names without a preceeding period.
> When it saw a  one-word sentence 

A sentence id _defined_ as being terminated by a full-stop and space. 
If it saw a 'sentence' then this must have been bounded by the end of
the previous sentence and teminated by another full-stop and space.

But of course you are not using the terms in any defined way but just
making up how you term things.  This does introduce ambiguity.

> not defined as data, that's a paragraph name.

Your pre-processor is obviously just ignoring one interpretation of
the ambiguous state.  You have been shown cases where this _is_
ambiguous, the fact that your pre-processor is incompetent is of no
consequence, the compiler will pick this up later.

> Terminate the previous sentence with a period to placate the COBOL compiler. For
> example, when presented with 'move a b c. move d e', it looked to see whether
> 'c' was defined as data. If not, it output:
   x1.
>      move a to b.
> c.
…[3 more quoted lines elided]…
> I stopped using the preprocessor.

Not only sloppy but dangerous.  If the program had 'perform x1' and
the 'c' was a typing error for an actual variable c1, then how do you
discover the two introduced bugs ?

As I said it fails to resolve the ambiguity.
 
> I did write my own preprocessor. For instance, it, along with APS and others,
> honored indentation as significant. When people read source code, they see
> subordination based on indentation, not explicit block terminators or level
> numbers. It would be nice if compilers at least gave a warning when seeing an
> out-dent without a preceeding terminator. 

This is not part of Cobol, indentation is entirely up to the
programmer.  If you like enforced indentation indicating level then
try Python.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T04:11:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5849ec.212305638@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b348ab$7rt$1@aklobs.kc.net.nz> <3e560ad0.65055203@news.optonline.net> <217e491a.0302211301.50f45ad9@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> The desire to remove ambiguity from programming languages gave us 
>
>Do you think that ambiguity should not be removed ?

Misunderstanding should be removed. Ambiguity in the lexicon can be resolved by
context in the syntax. 

>Most computer languages differenciate between assignment and equality
>is some way.  Pascal uses ':=' for assignment, other dissallow
>contexts where these could be confused.

Languages such as COBOL. 

>> As a result, a C programmer who writes 'if (a = b) ..;' gets b
>> copied into a then the result tested for zero. 
…[4 more quoted lines elided]…
>features of C give it a great deal of power and flexability.

The 'power' to shoot yourself in the foot. How often does a programmer need to
do assignment in the middle of a conditional?

>> This is a common error, committed
>> even by seasoned programmers. 
>
>No. Seasoned programmers are the ones that have learned to use tools
>which eliminate this as a problem.

You are referring to LINT. The existence of such safety nets demonstrates how
error-prone the language is.

>Oh and by the way, in "if ( a = b )" it tests for true if the result
>is _not_ zero.  You may find this ambiguous, I don't.

I said, "the result is tested for zero." How else would it determine the result
is_not_zero? Wait .. I have it .. use a ternary operator: if ((a = b) ? false :
true) .. ;  <pausing to admire the elegence of his code>

>In many cases ambiguity is simply not noticed by the receiver, it is
>only if the sender notices an inappropriate result that the ambiguity
>is noticed and the message modified.

That's called debugging. 

>> In COBOL, we read the = in 'if a = b' as a relational operator, while
>> recognizing the = in 'compute a = b' as an assignment operator. The
…[3 more quoted lines elided]…
>loses flexibility compared to other languages.

You should lobby for that feature, and even more strongly for function calls
which look like references to subscripted variables. The compiler sees 'COMPUTE
a = b(c);' cannot find an array named b, cannot find a function prototype,
therefore <fanfare> b must be a function (rather than a misspelling). It's
obvious. 

>But C's problems have nothing to do with the need to remove ambiguity
>in Cobol. A full stop is required prior to a paragraph label in order
>to remove ambiguity.

My COBOL pre-processor recognized paragraph names without a preceeding period.
When it saw a  one-word sentence not defined as data, that's a paragraph name.
Terminate the previous sentence with a period to placate the COBOL compiler. For
example, when presented with 'move a b c. move d e', it looked to see whether
'c' was defined as data. If not, it output:
     move a to b.
c.
     move d to e

I acknowledge that's as sloppy as the function call example above, which is why
I stopped using the preprocessor.

>Now it may be that you would prefer to use a language that enforces
>line breaks and resolves ambiguity some diffeent way.  Well please do
>so, either by moving on or by writing your own.

I did write my own preprocessor. For instance, it, along with APS and others,
honored indentation as significant. When people read source code, they see
subordination based on indentation, not explicit block terminators or level
numbers. It would be nice if compilers at least gave a warning when seeing an
out-dent without a preceeding terminator. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T14:58:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35eq9$83l$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```

On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> You are simply wrong. Every punctuation symbol represents a word. It may not
> be enunciated in the spoken language, but it is still a word.

Cite?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57eb61.188098832@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>Cite?

..The beloved '85 COBOL standard, section 5.1.7:

"The separator period, when used in these formats, has the status of a required
word." 

They could have said 'The separator period is required.' Instead they went out
of their way to promote it to a word. 

..Common usage, as seen in 'dot-com' and 'dot-NET'. 

..My Demo program parses COBOL source into a list of "words". It does not have
one type structure for lexemes and a different structure for punctuation.

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-22T22:51:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b39k1b$u5v$1@slb9.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu> <3e57eb61.188098832@news.optonline.net>`

```
Robert,
  You are wrong again.  Read what the '85 Standard really says.  It says

    "has the status of a required  word."

which is NOT to say that it is a word - in fact the '85 Standard is quite
clear that it is not.

See page IV-4 which CLEARLY distinguishes COBOL words from separators
(including the separator period) when it says,

"The individual characters of the language are concatenated to form
character-strings and separators. ..."

COBOL words are then listed as part of "character-string".

I really, REALLY wish that you would stop justifying your 'personal views"
my MIS-representing the Standard.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-22T22:27:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302222227.13f0bb95@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu> <3e57eb61.188098832@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> You are simply wrong. Every punctuation symbol represents a word. It may not
> >> be enunciated in the spoken language, but it is still a word.
…[6 more quoted lines elided]…
> word." 

This does not say that the full stop _is_ a word, or _represents_ a
word, as you claimed, but only that under certain conditions it is
given the same status as a required word in that it is required.
 
> They could have said 'The separator period is required.' Instead they went out
> of their way to promote it to a word. 

No. The full stop is not promoted to _being_ a word, it is not even
being promoted to having the same status as a word, it is having the
same status as a _required_ word.

'Status' (eg 'required') is an attribute.  'Required word' and
'full-stop' are entities.  Just because two enties have the same value
in an attribute does not make them the same entity.

But this is irrelevant.  Your claim was for 

>> "The grammar of all languages -- English, COBOL and (whatever) --
...
>> Punctuation such as the period are words.

Show us an example in English.

> ..Common usage, as seen in 'dot-com' and 'dot-NET'. 

In '.com' and '.NET' the '.' is _not_ a punctution full stop.  It
happens that it is the same symbol as is used for punctuation, but it
not punctuation.

Your claim was 'Every punctuation symbol represents a word'.  The fact
that non-punctuation symbols (such as '=', '+', '&' or the '.' in
3.14157) may be voiced is irrelevant to punctuation.
 
> ..My Demo program parses COBOL source into a list of "words". It does not have
> one type structure for lexemes and a different structure for punctuation.

The fact that your program chooses to process in this way shows
nothing about your claim.  In fact it may be that your program has
inappropriately named variables and this should be a list of "words
and symbols".

Yet you attempt to use this as _evidence_ ?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T15:58:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dffi$58b$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu> <3e57eb61.188098832@news.optonline.net> <217e491a.0302222227.13f0bb95@posting.google.com>`

```

On 22-Feb-2003, riplin@Azonic.co.nz (Richard) wrote:

> >> Punctuation such as the period are words.
>
> Show us an example in English.

http://www.kor.dk/borge/b-mus-1.htm
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-25T09:21:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9FB9E3074E2594B5.FD3E15F47CACE611.BAD5C412919253B9@lp.airnews.net>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu> <3e57eb61.188098832@news.optonline.net> <217e491a.0302222227.13f0bb95@posting.google.com> <b3dffi$58b$1@peabody.colorado.edu>`

```
On Mon, 24 Feb 2003 15:58:42 GMT, "Howard Brazee" <howard@brazee.net>
enlightened us:

>
>On 22-Feb-2003, riplin@Azonic.co.nz (Richard) wrote:
…[5 more quoted lines elided]…
>http://www.kor.dk/borge/b-mus-1.htm

LOL!!  But I think this only applies to Danes speaking English.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-25T14:13:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302251413.19bc26be@posting.google.com>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu> <3e57eb61.188098832@news.optonline.net> <217e491a.0302222227.13f0bb95@posting.google.com> <b3dffi$58b$1@peabody.colorado.edu> <9FB9E3074E2594B5.FD3E15F47CACE611.BAD5C412919253B9@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote in message news:<9FB9E3074E2594B5.FD3E15F47CACE611.BAD5C412919253B9@lp.airnews.net>...
> On Mon, 24 Feb 2003 15:58:42 GMT, "Howard Brazee" <howard@brazee.net>
> enlightened us:
…[7 more quoted lines elided]…
>  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I love the sig line!!!
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T04:13:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e584a66.212427082@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35eq9$83l$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>Cite?

..The beloved '85 COBOL standard, section 5.1.7:

"The separator period, when used in these formats, has the status of a required
word." 

They could have said 'The separator period is required.' Instead they went out
of their way to promote it to a word. 

..Common usage, as seen in 'dot-com' and 'dot-NET'. 

..My Demo program parses COBOL source into a list of "words". It does not have
one type structure for lexemes and a different structure for punctuation.

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T14:58:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35erj$83p$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```

On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> Granted, COBOL is written, but the 2002 standard discourages the use of
> periods.

Cite?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T15:06:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35f99$8b1$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```

On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> Granted, COBOL is written, but the 2002 standard discourages the use of
> periods.  I do as well. They don't contain any information. They're
> superfluous.

They give some information, but even if not - a little redundancy can make for a
more readable language.  A little redundancy can make it more like a spoken
language.

What is the big attraction to eliminating periods?   Did it make it more English
like?   Did it make it easier to get a clean compile (without the compiler
noticing that you have an IF without an END IF)?


> How are the rules inappropriate? I don't find them so. It seems to me that if
> COBOL used English grammar and word meanings correctly, its reputation as the
> most readable language would be enhanced.

So obviously you wish to emulate English more closely.   Fortunately, CoBOL
allows you to put more than one period in a paragraph, avoiding run-on
sentences.   It allows you to avoid un-English constructs such as END IF.   You
can easily make your code more English-like.



> Aren't we in this forum because we love COBOL's readability?

It's can be more understandable than English.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57eb66.188103944@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35f99$8b1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>What is the big attraction to eliminating periods?  

Moving sections of code in and out of if statements is simplified.

> Did it make it easier to get a clean compile (without the compiler
>noticing that you have an IF without an END IF)?

That's a problem. The period terminating a paragraph also terminates an
incorrect IF statement. I wish there was a compiler option to require explicit
terminators.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-22T22:47:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302222247.30d5f6ce@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35f99$8b1$1@peabody.colorado.edu> <3e57eb66.188103944@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >What is the big attraction to eliminating periods?  
> 
> Moving sections of code in and out of if statements is simplified.

Finally, after screeds of nonsense in made up arguments, most of which
were completely irrelvant, many of which were just wrong, you have
discovered the only real argument against full stops wherever
possible.

Of course, most of us knew this anyway, some find that it not a big
deal anyway, many having adequate tools that can deal with this (does
your editor have macros or are you using archaic and obsolete tools ?)
I quite agree that this is made easier, and it is partly why I don't
use full stops on the end of each statement.  The other is that it is
an issue of personal choice and I choose one way, others choose
another.

But it does not apply to the full stop at the end of a paragraph which
I put on a line by itself.  This makes no difference at all to
indenting or outdenting the code.

There is no reason at all to eliminate that, and every reason to
retain it (eliminating ambiguity).
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:01:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dfkd$5f1$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35f99$8b1$1@peabody.colorado.edu> <3e57eb66.188103944@news.optonline.net>`

```

On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> >What is the big attraction to eliminating periods?
>
> Moving sections of code in and out of if statements is simplified.

That seems like a big attraction to you?   It seems like a miniscule attraction
to me.  But you have a point, even the smallest simplification can be nice - if
it doesn't have a corresponding complication.


> > Did it make it easier to get a clean compile (without the compiler
> >noticing that you have an IF without an END IF)?
…[3 more quoted lines elided]…
> terminators.

Sometimes the use of periods will help the compiler recognize these errors.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 16)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-21T08:37:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35kl7$2fvu$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e5587c9.31506817@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:

> Granted, COBOL is written, but the 2002 standard discourages the use of
periods.

I acknowledge that the 2002 standard *allows* programs to be written with
very few periods, and I also acknowledge that it offers a repertoire of
mechanisms that allow individual programmers as a matter of style largely to
avoid them, but so far as I know the use of periods is not in any way
explicitly or implicitly *discouraged* by the standard, any more than it
discourages the use of hand-coded editing routines in favor of VALIDATE or
GO TO ... DEPENDING in favor of EVALUATE.

The convention for "discouraging" the use of a widely-used feature of the
language starts with placing it in the archaic category (like NEXT SENTENCE,
MOVE HIGH-VALUES TO <numeric item>, continuation of COBOL words across line
boundaries, ON OVERFLOW instead of ON EXCEPTION on a CALL statement, and the
use of <identifier> in a COPY ... REPLACING in the '02 standard).   The use
of periods in the Procedure Division for any purpose other than terminating
a paragraph is simply not in that list.

> How are the rules inappropriate? I don't find them so. It seems to me that
if
> COBOL used English grammer and word meanings correctly, its reputation as
the
> most readable language would be enhanced.

The rules of COBOL are appropriate to COBOL precisely because they DEFINE
COBOL.  COBOL is not English, Tagalog, Sanskrit, or Chinese, it is COBOL,
and it has its own grammar (and its own terms in describing that grammar).
The use of the term "aspect" in a Russian grammar is unlikely to bear much
relevance in a grammar of Mandarin.  The use of the word "article" in
English grammars has no meaning whatever in either Russian or Chinese
grammars.  Guess what:  Articles are IMPORTANT in English.  Verbal aspect is
IMPORTANT in Russian.  Neither has any relevance to COBOL.   If COBOL used
ALL the rules of English grammar, it would cease to be COBOL.

And COBOL is not only not English, it is DECREASINGLY targeted to the
monoglot in English.  The current standard is FIRST released as an
INTERNATIONAL standard, and includes significant support for
internationalization mechanisms.    In what way would slavish adherence to
the conventions of written English in the composition of COBOL program
enhance its legibility to the monoglot in Tlingkit?   Yes, this may be an
extreme example -- but see below for some that aren't!

> Aren't we in this forum because we love COBOL's readability?

Maybe you are.  As for me, that doesn't rank all that high up on my reasons
for participating in this forum.

And I'd have to say that COBOL's inability to support, say, Venezuelan
currency-representation conventions in the PICTURE clause (to say nothing of
non-English-character-set identifiers) from the inception of the language up
to the 2002 standard was a *limitation* in its usefulness to those outside
English-speaking countries.  Readability to the person fluent in written
English is *lower* on the priority scale for COBOL than ever it was before,
I would say.

I had a recent discussion with a member of another standards development
group on the subject of coding identifiers in other than "regular" character
sets.  There is no argument whatever as to whether they should ultimately be
able to encode them in Cyrillic, Greek, any of the Japanese writing
schemata, or Chinese ideographs; there is, however, some resistance to
allowing such identifiers to be encoded in representations of, say,
cuneiform or Egyptian hieroglyphics.   English readability?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-22T21:28:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e57eb6b.188108378@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[12 more quoted lines elided]…
>GO TO ... DEPENDING in favor of EVALUATE.

The 2002 standard discourages periods by providing explicit terminators and
discouraging NEXT SENTENCE, leaving the period with no role except paragraph
termination. Because its old role was preserved, it has become a trouble-maker
which must be avoided inside IF and every other explicitly terminated statement.

>The convention for "discouraging" the use of a widely-used feature of the
>language starts with placing it in the archaic category (like NEXT SENTENCE,
…[4 more quoted lines elided]…
>a paragraph is simply not in that list.

I speculate periods were not designated archaic for political reasons. The COBOL
community includes many, perhaps mostly, mainframers who want to retain old
practices. Some of them refer to '85 COBOL as "new COBOL" .. 18 years later. 
They are not the constituancy who will be first in line to try OO COBOL; they
will be near the end of the line.

Because it retained backward compatibility, C++ experienced the same growing
pains. I've been in many shops who SAY they program in C++. Examining their code
reveals that it is pure ANSI C. They are compiling it with a compiler designated
C++ to give the appearance of using a modern language, to benefit from a modern
editor and debugger, and to avoid the embarrassment of admitting the truth. They
are packaging old wine in new bottles. 

I'd wager that, if one examined the code of people who support periods, (s)he
would also find paragraph names prefixed with numbers, large monolithic programs
containing GO TOs, and a generally poor sense of structural design. COBOL bears
that legacy. It will not be eliminated by adding new syntax. Traditionalists
will simply avoid using the new features. It will be eliminated only by a major
paradigm shift, such as OO. For this reason, I applaud the addition of OO
features to COBOL. 

<snip>

>I had a recent discussion with a member of another standards development
>group on the subject of coding identifiers in other than "regular" character
…[4 more quoted lines elided]…
>cuneiform or Egyptian hieroglyphics.   English readability?

OO turns a programming language into a mega-language. Don't like the English
word ADD? Create a method named the Russian equivalent. Don't like English names
for data structures? Create a class named the Kanji logogram for Table. Don't
like the way UNSTRING works? Replace it with your own PARSE. Please make it
virtual so I can overload it with my PARSE, because mine is so much better.
Every programmer has been promoted to language designer.

Is this good or bad?

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-22T17:25:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5822F5.6000108@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net>`

```
Robert Wagner wrote:
> 
> I speculate periods were not designated archaic for political reasons. The COBOL
…[5 more quoted lines elided]…
> Because it retained backward compatibility, C++ experienced the same growing


What absolute drivel.

The period is an excellent terminator, and by eliminating it in favour 
of all sorts of scope delimiters, all you are doing is encouraginging 
huge monolothic sentences.  The natural "chunk" of code in Cobol is the 
paragraph, comprised of sentences.

Insisting that each paragraph be a single sentence, simply does away 
with the entire purpose of the paragraph.  When IF statements get so 
complex that you cannot tell what they are doing, it is a very simple 
matter to break it down into groups of statements by putting the groups 
into multiple paragraphs, and giving them names.  That way, things are 
readable.

Instead, you want to make the sentence huge, clutter it up with dozens 
of "end" statements of various forms, and leave all the stateements 
within it unlabeled so that one has to spebd an hour figuring out what 
each group of statements do.  When the sheer compexity of the resulting 
sentence, makes the punctuation (rather than the grammar) so critical to 
the functioning of the code that you need twenty type of periods to sort 
it all out, then you want to make the simple mechanism obsolete so you 
cannot paint yourself into  corner with the complexities you introduce.

As to your inference that everyone not agreeing to your convoluted style 
is incompetent, mired in twenty year old practices, and incapable of 
understanding your way of doing things, that is just pure ego.  I have 
not used a numbered paragraph in my thirty-five years of Cobol, and the 
last time I coded a goto (about three in thirty-five years), it was 
because the code was a deliberate infinite loop, a very sound reason for 
a goto, in my opinion.  I also have been writing OOP now for better than 
three or four years.

Donald
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T00:46:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5819d5.199992244@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote:

>The period is an excellent terminator, and by eliminating it in favour 
>of all sorts of scope delimiters, all you are doing is encouraginging 
>huge monolothic sentences.  

Without explicit delimiters, one can write huge monolithic sentences almost as
easily. I assume you are referring to long nested IFs. 

>The natural "chunk" of code in Cobol is the 
>paragraph, comprised of sentences.

I think the natural chunk is a 'block'. Other languages make this clear by using
begin and end marks e.g. curly braces in C. 

You don't use periods inside IF and EVALUATE statements. You're not allowed to.
Why are they suddenly important when outside an IF? It's asymmetrical. You would
have us do condition testing in one paragraph, or a paragraph per level if
nested, and all imperative operations in paragraphs of their own. For example:

if (condition)
  move a to b                 *> build output record
  move c to d
  perform until (condition)
    move e to f                *> put price history into record
  end-perform
end-if

== versus --

if (condition)
  perform build-output-record.

-- 100 lines of unrelated code --

build-output-record.
  move a to b.
  move c to d.
  perform put-price-history-into-record until (condition).
put-price-history-into-record.
  move e to f.

Now a maintenance change requires changing "move c to d." to a conditional. The
code becomes: 

build-output-record.
  move a to b.
  perform get-value-of-d.
  perform put-price-history-into-record until (condition).
put-price-history-into-record.
  move e to f.
get-value-of-d.
  if (condition)
     perform put-c-into-d
  else
     perform put-new-c-into-d
  end-if.
put-c-into-d.
  move c to d.
put-new-c-into-d.
  move new-c to d.

After a few more change iterations, your code has turned into spaghetti.

Now a production support person is trying to figure out how garbage got into c.
(S)he must trace backward through three levels of non-adjacent code to
understand the conditions under which things are moved to c .. constructing the
first example mentally or in pseudo-code. 

>Insisting that each paragraph be a single sentence, simply does away 
>with the entire purpose of the paragraph.

This is a circular argument i.e. one that uses its conclusion as one of its
premises. You define 'sentence' as 'text terminated by a period', then conclude
all my paragraphs contain one sentence. The dictionary defines 'sentence' as 'a
statement containing one noun and one predicate.'

> When IF statements get so 
>complex that you cannot tell what they are doing, it is a very simple 
>matter to break it down into groups of statements by putting the groups 
>into multiple paragraphs, and giving them names.  That way, things are 
>readable.

Now you've (unwittingly) put your finger on the real issue here -- fear of being
overwhelmed by complexity. That threshold is a function of the program's logic
AND your ability to comprehend. The program's logic isn't going to change, no
matter how it written. It is going to make the same decisions ONE WAY OR
ANOTHER. They can be made in one complete statement or they can be disbursed
into simpler but incomplete statements. The only variable is you. 

In the paper which started this <cough> 'discussion', I tried to give readers
tools for dealing with complex logic. Tools more powerful than 'common sense'
and natural language skills, which have a relatively low capacity for
complexity. I compared it to the difference between solving mathematical 'word
problems' with sixth-grade skills vs. solving them with algebra. Sadly, most
programmers are running on the former. 

>Instead, you want to make the sentence huge, clutter it up with dozens 
>of "end" statements of various forms, and leave all the statements 
>within it unlabeled so that one has to spend an hour figuring out what 
>each group of statements do. 

Comments are for explaining what statements do, not paragraph names. If it takes
an hour for you to figure out what a group of statements does, add a comment so
the next maintenance programmer won't have to do it again. I sometimes comment
code I wrote a few months ago. 

>As to your inference that everyone not agreeing to your convoluted style 
>is incompetent, mired in twenty year old practices, and incapable of 
…[5 more quoted lines elided]…
>three or four years.

A pat on the back to you. You're 90% on the way to Real Programming. We just
need to work on those periods and logic anxiety. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-23T09:29:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5904DE.3030608@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net>`

```
Robert Wagner wrote:
> 
>>When IF statements get so 
…[12 more quoted lines elided]…
> 


Are you being deliberately insulting, is it just lack of social skills, 
or are you actually this thick?

It was not unwittingly at all. It is the crux and the center of the 
arguement.

Any properly written top down program, with the advent of all the new 
scope delimiters, can be broken down into chunks in three ways.

We can use sentences, with periods, we can use paragraphs, with names, 
and we can use inline statements, with terminators. As you say, the 
logic does not change.

I could quite easily remve every single paragraph name in my code, and 
every period but one in the entire procedure division. Everything else 
could be handled by scope delimiters.

I could also remove every single group of more than one statement, place 
each in a paragraph, and give it a name.  If I do that, then the problem 
with periods in the middle of IF's ceases to exist.

I really do not see that

	IF LINE-COUNT IS GREATER THAN PAGE-SIZE
		PERFORM NEW-PAGE-ROUTINE.
	BLAH BALH BLAH

is inferior to:

	IF LINE-COUNT IS GREATER THAN PAGE-SIZE
********* The following is the page routine
		BLAH BLAH BLAH
********* end of the page routine
	END IF
*********END OF THE PAGEING IF
	ELSE
	BLAH BLAH BLAH
	.
*********END OF THE PARAGRAPH

It simply clutters things up.  The fact that the paragraph dealing with 
paging is elsewhere in the code is NOT detrimental, as you claim.  In 
fact, it is the eaxct opposite ... if I am interested in fixing a paging 
bug, I can search for it.  If I am not, I can safely ignore it and 
continue reading.  I do not have to analyse the sentnce to find our 
where it continues.

Your arguement about inserting "sentences" into IF statements bears the 
same flaw ... do not do it.  If you lay your paragraphs out correctly, 
then you put it into the correct paragraph, not into the IF statement.

To repeat:

I could quite easily remve every single paragraph name in my code, and 
every period but one in the entire procedure division. Everything else 
could be handled by scope delimiters.

However, to assert that such an approach, even in part, is sytlistically 
preferable shows an appalling lack of sophistocation in code writing 
ability.  You seem to be locked into a mindset more suited to a 
different langauge ... perhaps one that does not have such an elegant 
solution as a named paragraph.

Donald.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T23:04:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e594f38.279207777@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote:

>Robert Wagner wrote:

>Any properly written top down program, with the advent of all the new 
>scope delimiters, can be broken down into chunks in three ways.

There are four (non-OO) ways. I'll discuss the fourth below.

>We can use sentences, with periods, we can use paragraphs, with names, 
>and we can use inline statements, with terminators. As you say, the 
…[8 more quoted lines elided]…
>with periods in the middle of IF's ceases to exist.

Everything you just said is correct. The issue is called granularity, the quest
for the optimum-sized chunk of code. Some factors affecting the answer are human
comprehension, experience with the style used and (often overlooked) tools used
to view source. For example, if we could hyperlink to an out-of-line paragraph
or function by hitting one key then return by hitting one key, out-of-line
paragraphs would be more attractive. Similarly, in-line code would be more
attractive if the viewer worked like an outline processor, letting us hide and
reveal subordinate blocks of code with a single keypress or mouseclick. My text
editor does both. 

>However, to assert that such an approach, even in part, is sylistically 
>preferable shows an appalling lack of sophistocation in code writing 
>ability.  You seem to be locked into a mindset more suited to a 
>different langauge ... perhaps one that does not have such an elegant 
>solution as a named paragraph.

I did not advocate one packaging style exclusively. In fact, the non-trivial
Demo Program I posted here uses a balance of all three methods. A snippet is
copied below. 

The Demo uses a fourth method: the function. Every named paragraph could be
converted to an inline function, which provides the same functionality but with
two significant benefits:
.. You can pass parameters to a function, not to a paragraph
.. A function has its own working-storage variables which the parent cannot
change. Also, a function cannot monkey around with the parent's working-storage.

A commonly-held false belief is that functions must be separately compiled.
Every '85-compliant COBOL compiler offers the option of putting them in the same
source file with their parent, which may be the 'main' program or one of its
functions. Thus you have a single 'program to compile'. I find it elegant the
way they are nested inside their respective parents in telescoping fashion.
Named paragraphs, by contrast, may be scattered anywhere. 

The Demo Program used five functions nested three-deep for its outer structure.
Simply put, it used functions for big chunks of code, named paragraphs for
medium-sized chunks, and inline code for small chunks. Does that demonstrate
lack of sophistication or single-minded advocacy of one style over all others?

Code sample follows:

         if  current-verb equal to 'delete'
             perform find-file-entry
         else
             perform find-file-entry-by-record
         end-if
         if  file-found
             set file-write to address of word-entry
         end-if
     end-if
     move a-word to a-word-previous.
 find-file-entry.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-select
         if  address of word-entry not equal to null and
             word-text equal to current-fd
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 find-file-entry-by-record.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-record
         if  address of word-entry not equal to null and
             word-text equal to current-record
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 find-file-entry-by-name.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-name
         if  address of word-entry not equal to null and
             word-text equal to current-record
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 construct-file-entry.
     compute allocation-length =
         length of fixed-portion of file-entry + 2
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf  error constructing file ' return-code
         goback
     end-if
     set address of file-entry to last-file
     if  first-file equal to null
         set first-file to allocation-pointer
     else
         set next-file to allocation-pointer
     end-if
     set address of file-entry to allocation-pointer
     move zero to file-length
     move low-values to fixed-portion of file-entry
     move last-file to previous-file
     move allocation-pointer to last-file.
 end program analysis-function.
```

###### ↳ ↳ ↳ Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-23T19:12:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3bril$u2v$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net>`

```
Yet again Mr. Wagner has shown his ignorance of both ANSI/ISO COBOL
terminology - but also "common usage" in many (not all) COBOL programming
environments.

FYI,
  The '85 Standard introduced the ability to create "nested programs" and
*not* user-defined functions.  The '89 Amendment to the '85 Standard (ANSI)
and the 1991 amendment to the ISO Standard introduced "intrinsic functions".

As far as I know (and I admit that I could be mistaken in this) the "normal"
difference in programming language (and CERTAINLY the difference in the 2002
COBOL Standard) between functions and "called procedures" is whether or not
a value is "returned" without having to "pass" it as a parameter in the
original CALL statement.

In the 2002 COBOL Standard, there is the introduction of "user-defined" (as
well as an expanded list of) functions.  For user-defined functions, a
RETURNING phrase is added to the Procedure Division header (currently
supported - as an extension to the '85 Standard - by Micro Focus and
Fujitsu - possibly others).  In addition (and I know of no vendor supporting
this yet) the "Function-ID" paragraph replaces the Program-ID paragraph in
the Identification division - for a user-defined function.

It should be noted that a RETURNING phrase *may* be used in a CALLed
program - but such an compilation entity may NOT be used where a function
may be referenced in the procedure division (of a 2002 Standard conforming
program).

It is perfectly true, that the '85 Standard does provide a facility for
"localizing" both procedural code and data - without creating separately
compiled programs.  However, this facility has a name - and the name is
"nested programs" - it is NOT "functions".

  ***

In another thread Mr. Wagner made some comments about the thread that I
started with his name in the subject line.  My intention in doing so was to
insure that any reader of this newsgroup's "archives" will be well aware
that whatever Mr. Wagner *may* (or may not) know - any post of his referring
to the "official" Standard and what it says should be taken as worth the
paper that it is emailed on.   Some of his stylistic ideas are good - some
are probably useful if used "consistently" - some may even be portable to
all the (unlisted) compilers that he has ever worked on (although at least
one test that he did indicated that even this isn't true).  However, any
"justification" for his opinions based upon references to the OFFICIAL
Standard ('85 or 2002) is simply NOT reliable. It may even be correct - but
I place that just slightly higher than the chances of those "infinite number
of monkeys" creating a copy of the '85 Standard.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-24T03:19:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e598f30.295585789@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Yet again Mr. Wagner has shown his ignorance of both ANSI/ISO COBOL
>terminology - but also "common usage" in many (not all) COBOL programming
…[4 more quoted lines elided]…
>*not* user-defined functions. 

They are synonymous. COBOL's "nested programs" are called "local functions" in
general programming parlance. 

>As far as I know (and I admit that I could be mistaken in this) the "normal"
>difference in programming language (and CERTAINLY the difference in the 2002
>COBOL Standard) between functions and "called procedures" is whether or not
>a value is "returned" without having to "pass" it as a parameter in the
>original CALL statement.

Micro Focus, IBM and Fujitsu (at least) provide RETURN-CODE and GOBACK RETURNING
...

>It is perfectly true, that the '85 Standard does provide a facility for
>"localizing" both procedural code and data - without creating separately
>compiled programs.  However, this facility has a name - and the name is
>"nested programs" - it is NOT "functions".

Forgive me for using common English rather than COBOL-speak.

>In another thread Mr. Wagner made some comments about the thread that I
>started with his name in the subject line.  My intention in doing so was to
…[10 more quoted lines elided]…
>of monkeys" creating a copy of the '85 Standard.

I do not represent myself as a spokesman for standards. I write for real-world
practicing programmers using Micro Focus, IBM, Fujitsu and Realia compilers in
2003. That's a reasonable stance.

Robert
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-23T22:06:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3c5ng$sl6$1@slb1.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net> <3e598f30.295585789@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e598f30.295585789@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[8 more quoted lines elided]…
> They are synonymous. COBOL's "nested programs" are called "local
functions" in
> general programming parlance.

Can you provide any evidence on the web of this usage?  I just did a search
on "COBOL" and "local function" - I could find some "hits" but NONE that
used these two terms as "synonymous".   I certainly would guess that it
MIGHT occur in some literature - but it certainly is not "general
programming parlance".

I would suggest that anyone who DOES use these as synonomous start learning
about the difference - as they are significantly DIFFERENT syntactic
structures in the 2002 COBOL Standard.  I have also heard that implementing
"user defined functions" is a relatively high priority among the user base
of a number of vendors - certainly among two of those that you mention, i.e.
Micro Focus and IBM.

The RETURNING phrase on GoBack is available with a number of compilers
today.  HOWEVER, it is still impossible (at least with IBM, Funitsu, Realia,
and Micro Focus) to reference such an "entity" in those places in procedural
code where a function may be used, e.g.

   Move Function Program-with-Returning (Passed-Parameter-1
Passed-Parameter-2) to receiving-item.

This syntax IS valid with the 2002 Standard.  (In fact, by using the proper
facilities of the Repository paragraph, the COBOL word "FUNCTION" may even
be omitted.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-24T17:30:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5a56ad.3377505@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net> <3e598f30.295585789@news.optonline.net> <b3c5ng$sl6$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e598f30.295585789@news.optonline.net...
…[18 more quoted lines elided]…
>programming parlance".

Definition: A function is a contained block of code that accomplishes some task.
It can be passed parameters and it can return a value.
http://cplus.about.com/library/glossary/bldef-function.htm
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-24T13:47:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dssi$vlt$1@slb1.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net> <3e598f30.295585789@news.optonline.net> <b3c5ng$sl6$1@slb1.atl.mindspring.net> <3e5a56ad.3377505@news.optonline.net>`

```
I asked for COBOL *and* Function - you gave a reference to a C/C++
reference - which clearly is NOT talking about COBOL nested programs.  If
there is some doubt about the target audience of this definition, see the
"main" page of that URL at:

     http://cplus.about.com/library/

and that, of course is pretty obvious from the http://cplus at the beginning
of the URL.

There *are* differences of terminology between programming languages.  Just
think about "array" versus "table"
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-23T23:32:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302232332.48df4f7d@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net> <3e598f30.295585789@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >  The '85 Standard introduced the ability to create "nested programs" and
> >*not* user-defined functions. 
> 
> They are synonymous. COBOL's "nested programs" are called "local functions" in
> general programming parlance. 

No. Wrong.

'functions' in 'general programming parlance', and specifically in
Cobol and many other languages are procedures that, not only return a
value, but also may be used within an expression. Procedures that are
not functions are not used within expressions.

For example in Cobol a function may be used as:

      COMPUTE a = x * FUNCTION SQRT(y)

Similar distinctions are made in C, Pascal, Fortran and most other
languages.

Cobol 'nested programs' must be accessed using the CALL statement and
cannot be used in expressions.  Whether they return a value is of no
consequence to their naming.

'Nested programs' are _not_ functions in _any_ parlance (by anyone
with two clues to rub together) and they are certainly not
'user-defined functions' which would create a function usable in the
same way as the intrinsic functions.

> >As far as I know (and I admit that I could be mistaken in this) the "normal"
> >difference in programming language (and CERTAINLY the difference in the 2002
…[4 more quoted lines elided]…
> Micro Focus, IBM and Fujitsu (at least) provide RETURN-CODE and GOBACK RETURNING

Which is actually irrelevant to "the 'normal' difference in
programming languages".  In Pascal for example the difference between
a Procedure and a Function is whether it can return a value.  In order
to capture the value returned from a function it must be used in the
expression of an assignment:

            result = myfunc(param1);

which is exactly analogous to Cobol COMPUTE result = FUNCTION
myfunc(param1).

In Pascal, a procedure is used _not_ in an assignment:

            myproc(param2);

which is exactly analogous to Cobol CALL "myproc" USING param2.

WMK is entirely correct, your note on RETURNING is irrelevant, they
are still not functions.

> Forgive me for using common English rather than COBOL-speak.

Except of course, you simply got common usage wrong.  It may be how
you refer to nested programs, but it is still wrong.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-25T01:21:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5a95be.6733920@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net> <b3bril$u2v$1@slb6.atl.mindspring.net> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[3 more quoted lines elided]…
>> They are synonymous. COBOL's "nested programs" are called "local functions"
in
>> general programming parlance. 
>
…[5 more quoted lines elided]…
>not functions are not used within expressions.

I see no benefit in referring to callable programs by two names -- function and
procedure. The called program isn't written differently. The concept here is how
to package chunks of code. We should be able to come up with a generic term for
callable programs. 

'Procedure' is no good in COBOL because named paragraphs are procedures; they
are in the procedure division. 

'Callable program' is redundant. Every program is callable. Main programs are
called by the operating system, which passes the command line as a parameter and
receives return-code as an output. Under Micro Focus, they are called by 'the
run-time guy' -- cobrun. This is why I prefer GOBACK over STOP RUN.

'Program' is not bad. That's what the standard uses when it refers to "nested
programs". But non-IT workers think "program" means a run unit, as in 'I ran the
Word program.' They don't regard the dozen dll's it dynamically loaded as
programs. Conversational English seems to have preempted the word "program" from
having a technical definition. 

The only word left, that I can think of, is 'function', which has worked well
for the C language, where EVERY program is a function. 

The business about 'returning a value' comes from mathematics, where a function
always returns the same value when presented with the same inputs. That's not
true in programming. I can write 'a = foo(1, 2, 3); a = foo(1, 2, 3); a = foo(1,
2, 3);' and receive three different outputs. What if the function needs to
return two values, or zero values (class void in C, as you know)? What if it has
no inputs? Mathematicians don't have an answer. What you term a 'procedure call'
is a minimalist function call in C, looking like: 
foo();
It is not in an assignment statement because it doesn't return a value. So what?
It's still a function. 

How are we to distinguish between functions in the same compile unit vs.
functions compiled separately? Granted, they're written the same, but the
distinction is still useful. The obvious answer is 'internal function' vs.
'external function'. Alternatively, 'private function' vs. 'public function'.

>For example in Cobol a function may be used as:
>
…[3 more quoted lines elided]…
>languages.

Not in C. See above. 

>'Nested programs' are _not_ functions in _any_ parlance (by anyone
>with two clues to rub together) and they are certainly not
>'user-defined functions' which would create a function usable in the
>same way as the intrinsic functions.

They are in the parlance of C, where they are called 'local functions'. 

If I were talking to programmer who didn't know COBOL nor C and said I had
written a 'nested program', (s)he wouldn't have a clue what that meant. If I
said I'd written a 'local function', (s)he would .. even if the non-COBOL/non-C
language used different terminology, such as 'procedure'. 


Robert
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-25T15:10:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ejda$q8c$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net>`

```
Robert Wagner wrote:

> The only word left, that I can think of, is 'function', which has worked
> well for the C language, where EVERY program is a function.

And Cobol already has 'functions'.  The word is already used for something 
that is not a 'nested program'.  The word is already used for functions 
which are used like C functions.  Nested Programs are not like Cobol 
functions or like C functions, they are CALLed in exactly the same way as 
non-nested programs and are analogous to Pascal Procedures, or indeed C 
procedures (which are void functions).

How hard is that to understand ?
 
In some languages, such as Pascal and Java, there can be 'nested 
procedures' and 'nested functions'.

In Cobol there are functions (used like C functions) and there are programs 
which are called.  It happens that one class of programs may be nested, 
hence they are called 'nested programs'.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-25T10:19:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz>`

```
On Tue, 25 Feb 2003 15:10:51 +1300, Richard Plinston
<riplin@Azonic.co.nz> enlightened us:

>Robert Wagner wrote:
>
…[19 more quoted lines elided]…
>

Maybe I'm one those old dinosaur's who writes way too much monolithic
code, but the programmers I work with now and before have a term for
CALLED programs.  They are called Subroutines..no matter what they do
or what language they are written in.  I thought that was a fairly
common term but maybe only back in the computer-cambrian era when
large monolithic programs written with periods and perform thrus were
written with much glee.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T00:36:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5bf795.97331351@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Tue, 25 Feb 2003 15:10:51 +1300, Richard Plinston
><riplin@Azonic.co.nz> enlightened us:
…[30 more quoted lines elided]…
>written with much glee.

The context of the discussion was packaging code in various ways, specifically
performed paragraphs vs. called programs -- 'nested' and external. The word
'subroutine' is not useful in this context because it does not distinguish
between the two.

Some would consider an inline 'perform .. until' to be a subroutine. 

I was never comfortable with 'subroutine'. When does a 'routine' become a
'subroutine'? Lacking a clear definition, why not just call them all 'routines'
.. or procedures or programs or functions?

Robert
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-25T22:22:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302252222.3f895562@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

>  called programs -- 'nested' and external. 

Now _there_ is a great idea, just call them 'programs' and distinguish
between these, if it is ever required, with 'nested programs' and
'external programs'.

That sounds easy enough.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-26T09:46:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A6B0C19A9668B202.90502C80CB77F757.DA30FE7CE9A9D359@lp.airnews.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net>`

```
On Wed, 26 Feb 2003 00:36:57 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:
>
…[45 more quoted lines elided]…
>Robert

Too bad about your not being comfortable.  Let me ease your pain.  A
subroutine, as defined by my computer science prof in 1974, is a
subprogram consisting of a set of instructions that perform some
subordinate function with the program.  A closed subroutine is stored
in one place and connected to the program by means of linkages at one
or more points in the program.  An open subroutine is inserted
directly into a program at each point where it is to be used.

Therefore, all of what you are talking about are subroutines.  Nested
ones are just subroutines with static calls.  External use dynamic
calls.  Both are closed subroutines.  Those within the program
accessed via performs, go to, or fall into, are open subroutines. 

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-27T00:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d4abb.6270622@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net> <A6B0C19A9668B202.90502C80CB77F757.DA30FE7CE9A9D359@lp.airnews.net>`

```
The computing world has changed since 1974. That's the _point_ here.

What you call 'open subroutine' are now called 'inline functions'. 

At any rate, you didn't answer my objection -- terminology to distinguish
between different ways of packaging code: inline vs. performable vs. callable.
Under your nomenclature they're all 'subroutines'.

Robert

SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Wed, 26 Feb 2003 00:36:57 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:
…[45 more quoted lines elided]…
>>'subroutine'? Lacking a clear definition, why not just call them all
'routines'
>>.. or procedures or programs or functions?
>>
…[27 more quoted lines elided]…
>Steve
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-26T15:09:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ilam$q8b$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net>`

```

On 25-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> I was never comfortable with 'subroutine'. When does a 'routine' become a
> 'subroutine'? Lacking a clear definition, why not just call them all
> 'routines'
> .. or procedures or programs or functions?

Agree - there should be no "main" for C languages, and all exits should be of
the GOBACK variety.   In reality, this has been happening.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-27T00:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d4d04.6856175@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net> <b3ilam$q8b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 25-Feb-2003, robert@wagner.net (Robert Wagner) wrote:
…[7 more quoted lines elided]…
>the GOBACK variety.   In reality, this has been happening.

I assume you're being sarcastic. 

A C "main" does a GOBACK (return) exactly the same as other functions. And it
doesn't return a 'void', it returns a termination status code. 

When DOES a routine cross the line and become demoted to a subroutine? Sounds to
me like you're making up pseudo-intellectual words to impress your aunt or
grandmother.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 31)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-02-27T02:22:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CDe7a.50495$F%.2687676@twister.austin.rr.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <B5132F6A63710044.F00845AD82905453.AF12BF63B20B6AFF@lp.airnews.net> <3e5bf795.97331351@news.optonline.net> <b3ilam$q8b$1@peabody.colorado.edu> <3e5d4d04.6856175@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message news:3e5d4d04.6856175@news.optonline.net...
> "Howard Brazee" <howard@brazee.net> wrote:
> I assume you're being sarcastic.
…[3 more quoted lines elided]…
>

void main (int argc, char *argv[]) {
    // what do you think this will return?
    }
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T00:36:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5bfb84.98337877@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[10 more quoted lines elided]…
>How hard is that to understand ?

It is hard to understand, given that C terminology is 'void function' rather
than 'void procedure'.

>In some languages, such as Pascal and Java, there can be 'nested 
>procedures' and 'nested functions'.
…[3 more quoted lines elided]…
>hence they are called 'nested programs'.

A Cobol function is not written any differently whether dispatched by 'call
'foo'  using a, b, c' or 'x = function foo (a, b, c)'. If the function doesn't
care how it is invoked, we shouldn't need elaborate semantics to distintuish
'called function' from 'real function'.  The more useful distinction is between
'called' and 'performed'. 

Robert
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-26T10:30:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302261030.44d29fa0@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> A Cobol function is not written any differently whether dispatched by 'call
> 'foo'  using a, b, c' or 'x = function foo (a, b, c)'.

On which systems have you actually done this ?  

(written a nested program in Cobol and invoked it in a COMPUTE or MOVE
statement as FUNCTION name(params))
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-27T06:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d72f0.16565336@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261030.44d29fa0@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[6 more quoted lines elided]…
>statement as FUNCTION name(params))

What's your point? If there is a difference, show it.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-27T23:30:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3kpdt$f6i$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261030.44d29fa0@posting.google.com> <3e5d72f0.16565336@news.optonline.net>`

```
Robert Wagner wrote:

>>> A Cobol function is not written any differently whether dispatched by
>>> 'call
…[7 more quoted lines elided]…
> What's your point? If there is a difference, show it.

You mean that you really don't know ?

In '85 Cobol (actually the addendum), you can use _only_ the supplied 
intrinsic functions in move or compute statements.  You cannot write your 
own Cobol functions for use in that way.  Anything that you write is a 
program and can only be called.

In '2002 Cobol you can write Cobol user defined functions that are executed 
by putting them in-line in, say, a compute statement.  They are similar to 
programs but use FUNCTION-ID and EXIT FUNCTION and must be registered.

I had been working under the impression that you actually understood some 
of this stuff, obviously not.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 31)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-28T02:55:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5ebfa6.101752049@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261030.44d29fa0@posting.google.com> <3e5d72f0.16565336@news.optonline.net> <b3kpdt$f6i$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:


>In '2002 Cobol you can write Cobol user defined functions that are executed 
>by putting them in-line in, say, a compute statement.  They are similar to 
…[3 more quoted lines elided]…
>of this stuff, obviously not.

I'm a dunb-ass COBOL programmer. How is a function registered? I would think
that compiling it would do the job.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 32)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-27T21:49:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3mm7p$vr3$1@slb3.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261030.44d29fa0@posting.google.com> <3e5d72f0.16565336@news.optonline.net> <b3kpdt$f6i$1@aklobs.kc.net.nz> <3e5ebfa6.101752049@news.optonline.net>`

```
By the use of the (new) "REPOSITORY" paragraph. This same paragraph allows
one to leave out the (previously required) COBOL  word "FUNCTION" i.e.  one
can (when the proper REPOSITORY paragraph is used) code:

 Move Sum (field-1 Field-2) to Num-Field

   where the '89 Amendment required

Move Function Sum (field1 Field-2) to Num-Field

Further more, if you define a user-defined function   What-Is-It, then you
can code

 Move what-is-it (parm1) to Other-Field

and (because of the repository entry) it is "clear" to the compiler that

    what-is-it

is a user-defined function and NOT a "subscripted" data item.

Note Well:
  It is also possible to put RETURNING on a program (with a program-id
paragraph - not a function-id paragraph)

But in such a case it is still NON-conforming to code:

  Move Subprogram (parm1) to other-field.

Instead you need to code (and this shows the difference between
(sub-)programs and functions)

Call Subprogram
       Using parm1
       Returning other-field
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-26T18:59:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302261859.347d72ca@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> A Cobol function is not written any differently whether dispatched by 'call
> 'foo'  using a, b, c' or 'x = function foo (a, b, c)'.

Actually you are quite wrong. User written functions are new in '2002
and are similar to programs but have a FUNCTION-ID and use EXIT
FUNCTION rather than PROGRAM-ID and EXIT PROGRAM.  They also get
registered.

User written functions may be separately compiled or compiled with, or
within, a program source file.  In other words they can be nested or
external, just like programs.

> If the function doesn't care how it is invoked, 

But it _does_.  A function cannot be CALLed, a program cannot be
in-lined.

> we shouldn't need elaborate semantics to distintuish
> 'called function' from 'real function'.  The more useful distinction is 
> between
> 'called' and 'performed'. 

Procedures are performed.
Programs are CALLed
functions are in-lined.

Why do you insist on being so contrary by using a well defined term in
Cobol (function) and apply it to something else which has a perfectly
good name of its own (program).
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-28T02:55:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5ec0db.102061010@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261859.347d72ca@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[15 more quoted lines elided]…
>in-lined.

I have no experience with COBOL functions. Please post sample code showing the
difference between functions and called programs. 

>Why do you insist on being so contrary by using a well defined term in
>Cobol (function) and apply it to something else which has a perfectly
>good name of its own (program).

You have already answered the question .. because I'm stupid or ignorant or
pig-headed or ...

Robert
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-27T21:53:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3mmgo$6i2$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261859.347d72ca@posting.google.com> <3e5ec0db.102061010@news.optonline.net>`

```
In any '85 Standard  conforming compiler with the '89 Intrinsic function
module, an example of the use of an (intrinsic) - and that is all that the
'89 Standard support - function is something like:

  Move Function Sum (data-item-with-occurs (all) another-num-field) to
Receiving field.

As pointed out in another note, an example of the 2002 Standard
"user-defined function" facility would be

Move <function> My-Function (passed-parm1 passed-parm-2) to receiving-item

While if you use the RETURNING phrase on the procedure division of an entity
with the Program-Id paragraph, not Function-ID paragraph, you would need to
code something like

Call My-sub-Program
      Using passed-parm-1
                passed-parm-2
      returning receiving-item

        ***

Does this help show the difference between "programs" and "functions" (in
COBOL Syntax)?
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-28T13:15:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302281315.4b71b605@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261859.347d72ca@posting.google.com> <3e5ec0db.102061010@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> I have no experience with COBOL functions. Please post sample code showing the
> difference between functions and called programs. 

Functions were introduced in the 1989 (year) addendum.  You will find
them in your Cobol manual under 'Intrinsic functions', including how
to use them and the restrictions on their use (eg you cannot CALL
them).

User written functions are in the 2002 standard and I don't have a
compiler that has implemented these yet.  They have a few syntax
changes such as already mentioned and they can use RETURNING, actually
they _MUST_ use returning.

RETURNING is still a non-standard extension for programs, and may be
done differently in different compilers.  eg Fujitsu 7 requires the
returned variable in LINKAGE SECTION and the RETURNING is on the
PROCEDURE DIVISION header while MF has the variable in W-S and the
RETURNING on the EXIT PROGRAM.

But the difference in syntax between a program and a function is
almost irrelevant, it is the difference in implementation that is
important, this is why a function cannot be CALLed or a program
in-lined.
```

###### ↳ ↳ ↳ Re: Functios are NOT "nested programs" (was: COBOL/DIALOGUE System

_(reply depth: 31)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-28T15:44:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ol8q$itn$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e598f30.295585789@news.optonline.net> <217e491a.0302232332.48df4f7d@posting.google.com> <3e5a95be.6733920@news.optonline.net> <b3ejda$q8c$1@aklobs.kc.net.nz> <3e5bfb84.98337877@news.optonline.net> <217e491a.0302261859.347d72ca@posting.google.com> <3e5ec0db.102061010@news.optonline.net> <217e491a.0302281315.4b71b605@posting.google.com>`

```
Richard,
  According to the section

  "10.2 The PROCEDURE DIVISION Header"

that can be viewed online from
  http://supportline.microfocus.com/documentation/books/nx31sp1/nx31indx.htm

Micro Focus has already implemented the RETURNING phrase on the Procedure
Division header (as well as the older extension of on EXIT PROGRAM/METHOD)
and such an item would be in the Linkage Section - just as the 2002 Standard
requires.  In fact, it is marked with an "ISO2000" bubble.

HOWEVER, I haven't tried this yet - and don't know if it really works (yet)
or not, because there is also an ISO2002  bubble by the following rule

"8. The RETURNING phrase must be specified in a function definition and in a
function prototype definition."

which seems a "bit" odd - as NetExpress V3.1 shows support FUNCTION-ID in

  "5.8 The Function-ID Paragraph
The Function-ID paragraph specifies the name by which a function is
identified and assigns selected attributes to that function."

but I didn't think that V3.1 actually supported this yet.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-23T23:10:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E59C570.6050309@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <3E5904DE.3030608@Sympatico.ca> <3e594f38.279207777@news.optonline.net>`

```
Robert Wagner wrote:
> Donald Tees <Donald_Tees@Sympatico.ca> wrote:
> 
…[11 more quoted lines elided]…
> 
And that is the point.  By making extensive use of scope delimiters 
rather than paragraph names, you change the granularity in such a way 
that the period becomes a pain in the ass.  I prefer to use the period, 
but use it in conjunction with well chosen paragraphs, each paragraph 
fairly small.  I find it makes the code much more readable, and the use 
of the period much less prone to problems.  It depends as well on having 
a goodeditor, as you say.  However, I found that editors tend to become 
articles of passion for programmers, for that very reason.  I cannot 
conceive of a highly productive programmer wihout a personally set up 
and tuned editor.

BTW, as an aside, yes I overlooked the function.  I never liked it much, 
and find OOP methodology so superior that there is little point to it. 
OPP methods and the abilitie to move data in and out of objects in a 
controled manner is simply preferable.

Donald
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-23T10:16:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302231016.66abb5b6@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> After a few more change iterations, your code has turned into spaghetti.
 
> Now a production support person is trying to figure out how garbage got into c.

Have you never heard of a 'strawman argument' ?

> Comments are for explaining what statements do, not paragraph names. If it takes
> an hour for you to figure out what a group of statements does, add a comment so
> the next maintenance programmer won't have to do it again. I sometimes comment
> code I wrote a few months ago. 

Did it take you an hour to figure out your own code ?
 
> A pat on the back to you. You're 90% on the way to Real Programming. We just
> need to work on those periods and logic anxiety. 

You are an arrogant little prat aren't you.  Being condescending
doesn't win you friends, or change anyone's minds about how to
program.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:14:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dgct$5mv$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net>`

```

On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> This is a circular argument i.e. one that uses its conclusion as one of its
> premises. You define 'sentence' as 'text terminated by a period', then
…[3 more quoted lines elided]…
> statement containing one noun and one predicate.'

Not http://www.m-w.com/cgi-bin/dictionary?sentence

Which dictionary uses this definition?


> In the paper which started this <cough> 'discussion', I tried to give readers
> tools for dealing with complex logic. Tools more powerful than 'common sense'
…[3 more quoted lines elided]…
> programmers are running on the former.

Eliminating periods is one of these tools?   How does eliminating periods help
us deal with complex logic?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-25T01:21:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5aa6e6.11127277@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <b3dgct$5mv$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

>> In the paper which started this <cough> 'discussion', I tried to give readers
>> tools for dealing with complex logic. Tools more powerful than 'common sense'
>> and natural language skills, which have a relatively low capacity for
>> complexity. I compared it to the difference between solving mathematical
'word
>> problems' with sixth-grade skills vs. solving them with algebra. Sadly, most
>> programmers are running on the former.
>
>Eliminating periods is one of these tools?   How does eliminating periods help
>us deal with complex logic?

I was referring to my tutorial on Boolean algebra, but, yes, eliminating periods
does help. As Donald Tees correctly pointed out, an entire application can be
written as one (COBOL-defined) sentence, or every string of imperatives can be
put into a performable paragraph. It's all a matter of packaging. 

I often find myself cutting and pasting chunks of code into or out of inline
code. For instance, two lines in a paragraph performed from only one place into
inline. When doing that, periods just get in the way. 

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-25T14:54:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3g02c$a1n$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <3E5822F5.6000108@Sympatico.ca> <3e5819d5.199992244@news.optonline.net> <b3dgct$5mv$1@peabody.colorado.edu> <3e5aa6e6.11127277@news.optonline.net>`

```

On 24-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> >Eliminating periods is one of these tools?   How does eliminating periods
> >help
…[6 more quoted lines elided]…
> put into a performable paragraph. It's all a matter of packaging.

I can do that as well - but prefer to simplify complex logic by breaking it into
understandable steps.  (which perform does quite well - using periods).

> I often find myself cutting and pasting chunks of code into or out of inline
> code. For instance, two lines in a paragraph performed from only one place
> into inline. When doing that, periods just get in the way.

I don't use much in-line code.  If I can't see the logic on a screen, I prefer
to do a perform.  If I can see it on a screen, then cutting, pasting, and
editing is a trivial task.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-22T23:11:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302222311.6e3a25b2@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> it has become a trouble-maker
> which must be avoided inside IF and every other explicitly terminated statement.

Actually the full stop _always_ had to be avoided inside IF (that is
between the IF and the terminating mechanism.  It hasn't 'become'
this, it always has been.

> I speculate periods were not designated archaic for political reasons. 

No.

Some of them refer to '85 COBOL as "new COBOL" .. 18 years later.

Evidence ?  _Who_ has recently called the '85 standard 'new' ?
 
> They are not the constituancy who will be first in line to try OO COBOL; they
> will be near the end of the line.

You have absolutely _no_ idea who has and who has not tried OO Cobol,
or indeed who had already tried other OO languages over the last few
decades before OO Cobol became available to try.  Many who have
already been using OO Cobol for some time are Cobol programmers from
30 years ago or so.
 
> Because it retained backward compatibility, C++ experienced the same growing
> pains. 

Crap.  C++ grew in usage exactly because it retained backwards
compatability.  It it had not then it would have grown much more
slowly, or not at all.

> I've been in many shops who SAY they program in C++. 

Delivering Pizzas were you ?

> It will be eliminated only by a major
> paradigm shift, such as OO. For this reason, I applaud the addition of OO
> features to COBOL. 

You criticised C++ because it added OO feature to the core of C to
retain backwards compatability, now you praise Cobol for
_exactly_the_same_thing_.

> OO turns a programming language into a mega-language. ...
> Every programmer has been promoted to language designer.

Now you criticise OO, in fact you criticise the 'major paradigm shift'
that you claimed was required and you applauded.

You are a very confused little puppy.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T23:04:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e594f31.279200319@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <217e491a.0302222311.6e3a25b2@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>Some of them refer to '85 COBOL as "new COBOL" .. 18 years later.
>
>Evidence ?  _Who_ has recently called the '85 standard 'new' ?

Skillset inventories used by recruiters list COBOL and COBOL II as two separate
languages, giving the impression plain vanilla COBOL means the '74 standard. 

Job ads placed by employers similarly list COBOL and COBOL II as distinct
skills.

Competency tests, such as TechChek, have separate exams for COBOL and COBOL II. 

Aside -- don't ever take the COBOL II TechChek exam. I've scored 98-100 on every
COBOL test I've taken .. until that one. I scored 65 on it. Why? Because it
isn't about the COBOL language nor was it written by a COBOL programmer. Its
questions concern compiler installation issues such as command-line switches and
environment variables. One question asked 'What's the difference between v3.1
and v3.2?' The exam was obviously written by a systems programmer who had
installed some compilers and thought that experience qualified him or her as a
COBOL expert. I sent a complaint to the publisher. Of course, they didn't
respond. 

>> They are not the constituancy who will be first in line to try OO COBOL; they
>> will be near the end of the line.

>You have absolutely _no_ idea who has and who has not tried OO Cobol,

You are correct. 

>or indeed who had already tried other OO languages over the last few
>decades before OO Cobol became available to try.  Many who have
>already been using OO Cobol for some time are Cobol programmers from
>30 years ago or so.

I congratulate them. My comments were based on my personal experience with
mainframe COBOL veterans, and a lifetime of rewriting the bad code they left
behind.

>> Because it retained backward compatibility, C++ experienced the same growing
>> pains. 
…[3 more quoted lines elided]…
>slowly, or not at all.

I did not criticize C++ for offering backward compatibility. I pointed out that
it went through the same growing pains, and that it offered a refuge for
traditionalists. 

>> It will be eliminated only by a major
>> paradigm shift, such as OO. For this reason, I applaud the addition of OO
…[4 more quoted lines elided]…
>_exactly_the_same_thing_.

Your arguments would be more convincing if they rebutted the points I actually
make rather than the straw men you set up. 

>> OO turns a programming language into a mega-language. ...
>> Every programmer has been promoted to language designer.
>
>Now you criticise OO, in fact you criticise the 'major paradigm shift'
>that you claimed was required and you applauded.

Further evidence of the straw man fallacy. The context of that discussion was
non-English names for objects and methods. My point was that OO empowered
programmers to do it themselves. They were no longer limited by language
designers and compiler vendors. I also pointed out that home-grown languages
might be less capable or less compatible. That's not criticism; that's fair
comment.

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-24T13:52:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3bqds$jro$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e57eb6b.188108378@news.optonline.net> <217e491a.0302222311.6e3a25b2@posting.google.com> <3e594f31.279200319@news.optonline.net>`

```
Robert Wagner wrote:

>
>>Evidence ?  _Who_ has recently called the '85 standard 'new' ?
…[9 more quoted lines elided]…
> COBOL II.

And the word 'new' appears exactly where ?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:22:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dgs3$5vo$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <217e491a.0302222311.6e3a25b2@posting.google.com> <3e594f31.279200319@news.optonline.net>`

```

On 23-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> Skillset inventories used by recruiters list COBOL and COBOL II as two
> separate
> languages, giving the impression plain vanilla COBOL means the '74 standard.

Recruiters use key words.  They don't know what is important in finding
programmers.   I didn't get hired one time because I used Univac CoBOL instead
of CoBOL II.   But they were the same thing at the time!!!


> I congratulate them. My comments were based on my personal experience with
> mainframe COBOL veterans, and a lifetime of rewriting the bad code they left
> behind.

We all have to do this.  Most of us don't think eliminating periods is a
worthwhile part of this clean-up.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:07:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dfvk$5ft$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net>`

```

On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> The 2002 standard discourages periods by providing explicit terminators and
> discouraging NEXT SENTENCE, leaving the period with no role except paragraph
> termination.

Then the COMPUTE statement discourages the ADD statement?

> Because its old role was preserved, it has become a trouble-maker
> which must be avoided inside IF and every other explicitly terminated
> statement.

Having a period before the END IF will be caught by the compiler.    Anything
that's caught by the compiler is not "trouble".
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:09:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dg4j$5g3$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net>`

```

On 22-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> I speculate periods were not designated archaic for political reasons. The
> COBOL
…[3 more quoted lines elided]…
> will be near the end of the line.

Since there are people here who participated in this process, they can tell you
about what debate was done about keeping periods.   I suspect there was no
debate at all about it - no political reasons - that there was nobody who
brought forth a reason to eliminate periods.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-24T11:21:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3drcc$1qmq$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b3dg4j$5g3$1@peabody.colorado.edu...
> Since there are people here who participated in this process, they can
tell you
> about what debate was done about keeping periods.   I suspect there was no
> debate at all about it - no political reasons - that there was nobody who
> brought forth a reason to eliminate periods.

There is also SIGNIFICANT reluctance to making a change on stylistic grounds
that would require the implementors to provide mechanisms in the compilers
to identify millions upon millions of lines of existing code as being
stylistically antiquated.  When any syntax in the language is determined to
be archaic or obsolete in the standard, the technical reasons for doing so
are given, and even then the move from "archaic" to "obsolete" may never
occur precisely because the committee does NOT feel it is appropriate to
require companies to spend vast sums of money rewriting and redesigning code
that is running today for the sole purpose of satisfying a stylistic shift.
Where POSSIBLE, existing conforming SOURCE code should continue to compile
and run.

As a standards committee member, and as someone who supports compilers for a
major vendor, I feel a MAJOR part of the reason for having a standard and a
standards process in the first place is so that the COMPANIES who have
invested billions of dollars over the last forty years in developing and
maintaining COBOL code are NOT subjected to any more additional costs than
absolutely necessary in upgrading to a compiler conformant with the Latest
and Greatest standard.

ISO/IEC 1989:2002, page 833, G.1, "Archaic language elements" reads as
follows:

"The purpose of the archaic language element designation is to discourage
the use in new programs of some features that are unreliable, poor
programming practice, or ill-defined -- where better programming techniques
are available in standard COBOL.  These elements are classified as archaic
rather than obsolete because their use in existing programs might be too
extensive to warrant removal in the next revision of standard COBOL.

"Archaic language elements are intended to remain in the next revision of
standard COBOL.  There is no plan for the removal of archaic elements;
however, should their use in program inventories become insignificant, they
may be considered for designation as obsolete by future architects of
standard COBOL."

I for one am not convinced that the use of embedded periods in *existing
program inventories* will decline at a sufficiently rapid rate so as to
justify its archaization in the next standard, and for that reason alone I
think that "archaization" is a bad idea (conversely, I can see continued
words, move of alpha figs to numerics, and NEXT SENTENCE dying away
rapidly).   Personally, I would hope that it wouldn't happen in the
foreseeable future -- not because I'm in favor of embedded periods, but
because I don't think it's right for the STANDARDS committee to require
COMPANIES to spend money to update running programs just because the
programs aren't in somebody's idea of the most modern style!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-25T13:46:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302251346.5b9fb113@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:<b3drcc$1qmq$1@si05.rsvl.unisys.com>... 
> There is also SIGNIFICANT reluctance to making a change on stylistic grounds
> that would require the implementors to provide mechanisms in the compilers
…[8 more quoted lines elided]…
> and run.

<rant>

I would submit that the use of full-stop periods is not a mere
stylistic  preference.  I would suggest that it is a symptom of, or in
some cases a facilitator of several industry-disapproved habits like
large, monolithic programs; fall thru logic; roll your own control
constructs via go-to and perform-thru; unusual and unpredictable
control flow changes via next sentence, etc.

In the last three-plus decades a generally accepted practice in the
software construction industry has been toward smaller, 
self-contained, loosely coupled, reusable pieces of software that are
assembled to produce the desired software effect.  Because of this
approach size (LOC) of systems built today are several orders of
magnitude larger greater than those of yesteryear.  Required in this
approach is that the small pieces are unaware of the context of their
use.  The use of full stop periods violates this approach -- dependant
upon context it can terminate nothing or they may terminate many
things outside of their scope.

In no other industry is state-of-the-art minus 30 years considered
acceptable.  Auto mechanics can no longer refuse to repair autos with
fuel injection systems.  Doctors can no longer paint throats with
Mercurochrome to treat streptococci infections.  It isn't because
carburetors and Mercurochrome don't work, but that the respective
industries have moved toward fuel injection as cleaner and more
efficient and antibiotics as less toxic.

The mechanic would lose customers, even though there are still plenty
of carburetors around.  The doctor could face malpractice litigation,
even though Mercurochrome is a valid and effective treatment.

However, in the programming world there are people that insist on
respect for their unwillingness to keep up with the state of the art. 
They wrap themselves in a WADITW cloak and refuse to deal with those
newfangled practices of software construction.  This view seems to be
more common around Cobol and mainframes than other places, perhaps
because of the age of these things.

At best (and with lots of effort), the full stop period is logic
neutral.

At worst it alters logic flow and block scope, this is the usual case
when it is used at all.

When I think of a style I tend to think of something that doesn't
alter logic flow, like perhaps uppercase/lowercase, or the choice
between a comment flower box above a paragraph name, or surrounding
it.  The choice of periods -vs- no periods is a bit more important.

</rant>
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-26T15:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ilpq$qfi$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com>`

```

On 25-Feb-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:

> I would submit that the use of full-stop periods is not a mere
> stylistic  preference.  I would suggest that it is a symptom of, or in
…[3 more quoted lines elided]…
> control flow changes via next sentence, etc.

I submit that there are big bloated programs using any style.

I submit that you see lots of big bloated programs which were written before it
became stylish to eliminate periods, and you are confusing cause and effect.  
Eliminating periods did not cause people to write structured small modules.

Neither did writing code in mixed case.


> At best (and with lots of effort), the full stop period is logic
> neutral.

At best, it clarifies when a pre-compiler statement condition ends.  (I use a
pre-compiler that sticks in IF but doesn't stick in END IF)

> At worst it alters logic flow and block scope, this is the usual case
> when it is used at all.

If you have terminators and CONTINUE, this worst case won't happen.   Which
standard addresses the real problem, requiring CONTINUE and terminators, or
proscribing periods?

Don't cure the symptom - cure the disease.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-26T11:06:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302261106.52eddca@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b3ilpq$qfi$1@peabody.colorado.edu>...
> On 25-Feb-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:
[snip regarding use of periods]
> > At worst it alters logic flow and block scope, this is the usual case
> > when it is used at all.
…[3 more quoted lines elided]…
> proscribing periods?

I don't quite get what you are saying.  Are you suggesting that it is
possible to write with scope terminators AND full-stop periods in the
same code?

That sounds like a great way to get lots of compiler errors about
dangling END-* statements to me.

What exactly does CONTINUE have to do with anything?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-26T20:46:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3j937$5nk$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu> <dcedb8d0.0302261106.52eddca@posting.google.com>`

```

On 26-Feb-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:

> > > At worst it alters logic flow and block scope, this is the usual case
> > > when it is used at all.
…[7 more quoted lines elided]…
> same code?

Why not?  I do it all the time.   My paragraphs typically have more than one
sentence.  Some sentences are READ/END-READ or complex IF/END-IF sentences. 
Some are not.

> That sounds like a great way to get lots of compiler errors about
> dangling END-* statements to me.

I don't mind compiler errors.  It's logic errors that are expensive.  If I can
get a compiler to catch a dangling END statement, great!   The END-IF guarantees
that the period won't be within the IF logic.   The period guarantees that you
didn't miss an END-IF (from a pre-compiler generated IF statement).

> What exactly does CONTINUE have to do with anything?

Replacing NEXT SENTENCE by CONTINUE gets rid of the problem of GO TO
NEXT-PERIOD.    Now it doesn't matter if someone sticks in an extra period or
takes out a period.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-27T08:55:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302270855.7a31cb15@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu> <dcedb8d0.0302261106.52eddca@posting.google.com> <b3j937$5nk$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b3j937$5nk$1@peabody.colorado.edu>...
> On 26-Feb-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:
> 
…[27 more quoted lines elided]…
> takes out a period.

Seems like alot of extra work for a best case of no benefit.

As a down side, if you ever find the need to wrap some statemens in an
IF or a PERFORM you then need to remove all those extra periods, thus
screwing up your source control system and making it look like you
changed much more that you did.

I would suggest you are introducing potential logic errors by
scattering periods where they are not needed, but that is just an
opinion.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-27T17:58:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ljkk$bdc$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu> <dcedb8d0.0302261106.52eddca@posting.google.com> <b3j937$5nk$1@peabody.colorado.edu> <dcedb8d0.0302270855.7a31cb15@posting.google.com>`

```

On 27-Feb-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:

> > Replacing NEXT SENTENCE by CONTINUE gets rid of the problem of GO TO
> > NEXT-PERIOD.    Now it doesn't matter if someone sticks in an extra period
…[3 more quoted lines elided]…
> Seems like a lot of extra work for a best case of no benefit.

I think using NEXT SENTENCE can cause errors.  CONTINUE is a much safer piece of
code.
I think the use of terminators catches lots of logic errors (I've participated
in enough code walk thrus to have reasons for this belief).

There is benefit in these standards which I believe is worth the extra work.

> As a down side, if you ever find the need to wrap some statemens in an
> IF or a PERFORM you then need to remove all those extra periods, thus
> screwing up your source control system and making it look like you
> changed much more that you did.

Back to periods again.   If I was going to wrap up some code, I will edit it as
well, doing indenting and such.  My change control will see these lines as
changed, and that's OK by me.

> I would suggest you are introducing potential logic errors by
> scattering periods where they are not needed, but that is just an
> opinion.

I think that a shop with standards that require terminators and eliminate NEXT
SENTENCE, the use of periods will be pretty much cosmetic, at least when we
don't have pre-compilers adding logic that makes periods useful.

But show me an instance where these are used and the program compiles cleanly
where a logic error can be caused by the use or non-use of a period.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-02-27T19:13:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0302271913.52a514ab@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu> <dcedb8d0.0302261106.52eddca@posting.google.com> <b3j937$5nk$1@peabody.colorado.edu> <dcedb8d0.0302270855.7a31cb15@posting.google.com> <b3ljkk$bdc$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b3ljkk$bdc$1@peabody.colorado.edu>...
> I think that a shop with standards that require terminators and eliminate NEXT
> SENTENCE, the use of periods will be pretty much cosmetic, at least when we
…[3 more quoted lines elided]…
> where a logic error can be caused by the use or non-use of a period.

That really is the problem.  Most of the places I see periods there
are no explicit scope terminators and next sentence is often seen as
well.

If you put those conditions on it, then the period is mostly harmless.
 If you remove the scope terminators, as is often the case in the
full-stop -vs- no-stop discussion then it changes.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-28T15:12:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3nu8u$p55$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e57eb6b.188108378@news.optonline.net> <b3dg4j$5g3$1@peabody.colorado.edu> <b3drcc$1qmq$1@si05.rsvl.unisys.com> <dcedb8d0.0302251346.5b9fb113@posting.google.com> <b3ilpq$qfi$1@peabody.colorado.edu> <dcedb8d0.0302261106.52eddca@posting.google.com> <b3j937$5nk$1@peabody.colorado.edu> <dcedb8d0.0302270855.7a31cb15@posting.google.com> <b3ljkk$bdc$1@peabody.colorado.edu> <16e2f010.0302271913.52a514ab@posting.google.com>`

```

On 27-Feb-2003, psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

> > But show me an instance where these are used and the program compiles
> > cleanly
…[4 more quoted lines elided]…
> well.

Understood.   Periods were necessary when scope terminators were not used (or
when you have pre-compilers where scope is unknown).

The problem is that scope wasn't obvious.   The solution is to add obvious scope
terminators.

> If you put those conditions on it, then the period is mostly harmless.
>  If you remove the scope terminators, as is often the case in the
> full-stop -vs- no-stop discussion then it changes.

So you're setting up shop standards.   If the standard is to require scope
terminators (and replace NEXT SENTENCE), your problem is solved.   If the
standard is to remove periods, you either keep your problem (if you don't have
the above standard), or you problem is still solved (if you have the above
standard).     Periods isn't the problem.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T04:15:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e584a83.212456266@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[12 more quoted lines elided]…
>GO TO ... DEPENDING in favor of EVALUATE.

The 2002 standard discourages periods by providing explicit terminators and
discouraging NEXT SENTENCE, leaving the period with no role except paragraph
termination. Because its old role was preserved, it has become a trouble-maker
which must be avoided inside IF and every other explicitly terminated statement.

>The convention for "discouraging" the use of a widely-used feature of the
>language starts with placing it in the archaic category (like NEXT SENTENCE,
…[4 more quoted lines elided]…
>a paragraph is simply not in that list.

I speculate periods were not designated archaic for political reasons. The COBOL
community includes many, perhaps mostly, mainframers who want to retain old
practices. Some of them refer to '85 COBOL as "new COBOL" .. 18 years later. 
They are not the constituancy who will be first in line to try OO COBOL; they
will be near the end of the line.

Because it retained backward compatibility, C++ experienced the same growing
pains. I've been in many shops who SAY they program in C++. Examining their code
reveals that it is pure ANSI C. They are compiling it with a compiler designated
C++ to give the appearance of using a modern language, to benefit from a modern
editor and debugger, and to avoid the embarrassment of admitting the truth. They
are packaging old wine in new bottles. 

I'd wager that, if one examined the code of people who support periods, (s)he
would also find paragraph names prefixed with numbers, large monolithic programs
containing GO TOs, and a generally poor sense of structural design. COBOL bears
that legacy. It will not be eliminated by adding new syntax. Traditionalists
will simply avoid using the new features. It will be eliminated only by a major
paradigm shift, such as OO. For this reason, I applaud the addition of OO
features to COBOL. 

<snip>

>I had a recent discussion with a member of another standards development
>group on the subject of coding identifiers in other than "regular" character
…[4 more quoted lines elided]…
>cuneiform or Egyptian hieroglyphics.   English readability?

OO turns a programming language into a mega-language. Don't like the English
word ADD? Create a method named the Russian equivalent. Don't like English names
for data structures? Create a class named the Kanji logogram for Table. Don't
like the way UNSTRING works? Replace it with your own PARSE. Please make it
virtual so I can overload it with my PARSE, because mine is so much better.
Every programmer has been promoted to language designer.

Is this good or bad?

Robert
```

###### ↳ ↳ ↳ Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-22T22:55:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b39k8b$gec$1@slb1.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e584a83.212456266@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
…[10 more quoted lines elided]…
> >mechanisms that allow individual programmers as a matter of style largely
to
> >avoid them, but so far as I know the use of periods is not in any way
> >explicitly or implicitly *discouraged* by the standard, any more than it
> >discourages the use of hand-coded editing routines in favor of VALIDATE
or
> >GO TO ... DEPENDING in favor of EVALUATE.
>
> The 2002 standard discourages periods by providing explicit terminators
and
> discouraging NEXT SENTENCE, leaving the period with no role except
paragraph
> termination. Because its old role was preserved, it has become a
trouble-maker
> which must be avoided inside IF and every other explicitly terminated
statement.

You are wrong. You have been told you are wrong.  You continue to
mis-represent what the Standard does.

Do you think that you will have anyone believing you when you state
something correctly - if you keep arguing for things that have already been
shown to be wrong.

The 2002 Standard has explicit ways of "discouraging" features - and periods
just are NOT in this category.  It doesn't matter what you WANT, you can't
claim it for the Standard.

You *might* want to submit a paper asking for "middle of the paragraph"
periods to be put in the archaic category in the NEXT COBOL Standard.  Maybe
if you need that and heard back from the real standards committees you would
stop making a complete fool of yourself.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T06:41:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e586d2e.221332893@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>You are wrong. You have been told you are wrong.  You continue to
>mis-represent what the Standard does.
…[12 more quoted lines elided]…
>stop making a complete fool of yourself.

Judging from the vitriol, I'm obviously hitting a nerve. The period is more than
a punctuation mark, it's a SYMBOL of old COBOL. If the period falls, so too do
fall-through paragrphs, PERFORM .. THRU and the 77 level .. all of which are
indefensible. 

This is about culture, not about a punctuation mark. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-23T12:53:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net>`

```
On Sun, 23 Feb 2003 06:41:45 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[23 more quoted lines elided]…
>Robert

No, it is about your bias, your ego and your arrogance.  What you are
opposing is the part of the very structure of Cobol and whether you
like it or not it is there in the language; it is not indefensible;
and it is useful.  Maybe you'd like to see commas removed from IBM
Assembler because they are an old symbol as well?  Or maybe you should
just stick to C++ or the language du jour as I'm sure they won't have
any archaic symbols to gnaw in your craw.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Vulcanization: The process whereby rubber grows pointed ears and 
starts saying "Live long and prosper". 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-02-23T19:02:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1V86a.8779$Tz6.402405@twister.austin.rr.com>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net>`

```
Hey guys -

   Take a chill pill please - this discussion is borering periously close to personal attacks, and that is something we don't need.
Especially over something as silly as a period.

   I will state that Bill, Thane, Doc, Don, and others here are better authorities on COBOL than you will find gathered together
*anywhere* else - and as such have more than earned at least enough respect to demand politeness.

  I am interested in Periods in pretty much an academic sense. I don't allow periods to be used in the procedure section except to
end paragraphs and where required. I also don't allow fall through programming or perform-thru. The reason I don't allow those
techniques has nothing to do with technical COBOL issues, it is because those design choices offend those of us trained in OOD.

 Paradoxically, I don't find semi-colons behind C statements offensive, but my C shop is also not allowed to use them to end if
statements, while statements, and such. They have to use {} pairs even when the language does not require them.
Same reason as above.

I find that inconsistancy in myself a little amusing I suppose.

Anyway, point is, find a little more humor in this guys, and let the rancor, even if you believe it is deserved, go.

-Paul
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-24T01:33:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e596e6a.287194324@news.optonline.net>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net> <1V86a.8779$Tz6.402405@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:

>Hey guys -
>
>   Take a chill pill please - this discussion is borering periously close to
personal attacks, and that is something we don't need.
>Especially over something as silly as a period.

When their emotional values are threatened, they respond emotively. 

Ironically, most participants have said they avoid intra-paragraph periods,
therefore agree with me. Nobody piled on them. Why? Because they don't pose a
threat to Bad Programming in general.

>   I will state that Bill, Thane, Doc, Don, and others here are better
authorities on COBOL than you will find gathered together
>*anywhere* else - and as such have more than earned at least enough respect to
demand politeness.

I concur. I've never disrespected them, even though Bill keeps attacking me. 

>  I am interested in Periods in pretty much an academic sense. I don't allow
periods to be used in the procedure section except to
>end paragraphs and where required. I also don't allow fall through programming
or perform-thru. The reason I don't allow those
>techniques has nothing to do with technical COBOL issues, it is because those
design choices offend those of us trained in OOD.

Yep, you got that right. Be careful, least they be after you next. 

> Paradoxically, I don't find semi-colons behind C statements offensive, but my
C shop is also not allowed to use them to end if
>statements, while statements, and such. They have to use {} pairs even when the
language does not require them.
>Same reason as above.

That's a common C stylebook standard. Not a biggie to me.

>I find that inconsistancy in myself a little amusing I suppose.

Ogden Nash wrote, "Incompatibility provides the spice of life, so long as he
provides the income and she is pattable." <ducking and covering>

>Anyway, point is, find a little more humor in this guys, and let the rancor,
even if you believe it is deserved, go.

THEY won't let it go. So I'll keep holding their nose to it. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-24T16:26:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dh39$605$1@peabody.colorado.edu>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net> <1V86a.8779$Tz6.402405@twister.austin.rr.com> <3e596e6a.287194324@news.optonline.net>`

```

On 23-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> When their emotional values are threatened, they respond emotively.
>
> Ironically, most participants have said they avoid intra-paragraph periods,
> therefore agree with me. Nobody piled on them. Why? Because they don't pose a
> threat to Bad Programming in general.

Periods don't pose a threat to Good Programming in general.   There are much
more useful targets to aim for.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-02-25T01:24:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Bz6a.16322$O41.664161@twister.austin.rr.com>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net> <1V86a.8779$Tz6.402405@twister.austin.rr.com> <3e596e6a.287194324@news.optonline.net>`

```
Snort - let me make it plainer,  you seem to be arguing with people, not with the subject matter.
Please step back and cool off, or redirect your ire towards a subject, not the people.
Also please remember people say things in e-mail or postings that they would NEVER
say in person.

-Paul

"Robert Wagner" <robert@wagner.net> wrote in message news:3e596e6a.287194324@news.optonline.net...
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:
>
…[46 more quoted lines elided]…
> Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T00:36:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5bf08f.95532245@news.optonline.net>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <83104344D7D14F3B.B49D5B3D3223E20B.6DAD16FA5C435951@lp.airnews.net> <1V86a.8779$Tz6.402405@twister.austin.rr.com> <3e596e6a.287194324@news.optonline.net> <2Bz6a.16322$O41.664161@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:

>Snort - let me make it plainer,  you seem to be arguing with people, not with
the subject matter.

I do argue the subject matter. I've never disparaged others with phrases like
'pure rubbish', 'don't know what you're talking about', 'don't have two clues',
'ignorant', etc. Your comments should be addressed to those who do.

Look at the subject of this thread. I didn't originate it.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-26T15:33:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3h946$uvo$1@aklobs.kc.net.nz>`
- **References:** `<b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e596e6a.287194324@news.optonline.net> <2Bz6a.16322$O41.664161@twister.austin.rr.com> <3e5bf08f.95532245@news.optonline.net>`

```
Robert Wagner wrote:

> I do argue the subject matter. I've never disparaged others with phrases
> like 'pure rubbish', 'don't know what you're talking about', 'don't have
> two clues', 'ignorant', etc. Your comments should be addressed to those
> who do.

You have a severe difficulty distinguishing between 'what you say' and 'who 
you are'.

If you make a statement that is simply wrong in fact and in substance, as 
you have often done here, then saying that your _statement_ is 'pure 
rubbish' does _not_ mean that _you_ are pure rubbish.

Saying that 'you don't know what you are talking about' after you have 
repeatedly made statements that disagree with the facts is not 
'disparaging', but is just a statement that says 'you do not know'.

'ignorant' derives from the same root as 'ignore'.  If you repeatedly 
ignore corrections and continue to make statements that are provably wrong 
then 'ignorant' is just fair comment, you ignore.

You have, however, disparaged others:

RW> Mainframe programmers are, for the most part, mediocre. ...
RW> the bright people are working elsewhere.

I am no longer a mainframe programmer, not for 25 years, but many here are.

RW>  Old-timers who prefix paragraph names with 4-5 digit numbers and 
cannot understand NOT ..

RW> they were doctrinaire assholes lacking social skills and
RW> ability to think outside the box they were trained in. 

However, I can quite see how you will talk about this group to others:

RW> If I was incorrect,
RW> they should have at least offered cogent rebuttal rather than attacking
RW> my character. 

You had also complained about:

>If you are really serious in having your COBOL views accepted then you
>might want to reconsider your communication style, that is if arrogance can
>rightly be considered a style. A little religion might not hurt either:

RW> This newsgroup is for public discussion of ideas about COBOL. It is not
RW> a social club, nor a forum to discuss my communication style. Please
RW> critique the points I make, not my personality nor courtesy.

Again you take criticism as a personal afront.  You had asked for comments, 
the subjuct included 'seeking feedback'.  The style of your writing gives 
the impression of arrogance as well as self-serving ego (eg "I rewrote more
than 1,000 COBOL programs in the first year.").

No one will read an article through to the end if they find it 
condescending and arrogant.  'Communication style' is as important as 
content if you want to get your message across.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-23T11:18:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302231118.1dae3629@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >You are wrong. You have been told you are wrong.  You continue to
> >mis-represent what the Standard does.
…[12 more quoted lines elided]…
> >stop making a complete fool of yourself.
 
> Judging from the vitriol, 

I see no 'vitriol' in the reply to you, only an informed opinion
stating that your assertions are simply wrong.

> I'm obviously hitting a nerve. 

Yes, you are hitting a nerve.  WMK is extremely well informed on the
standards, while you have demonstrated a complete lack of knowledge of
them.  Repeatedly you have made incorrect statements about what the
standards do or do not say in an attempt to further your crusade.

Even when your errors are pointed out to you you completely ignore
this because, apparently, your crusade is more important to you than
facts.

> The period is more than
> a punctuation mark, it's a SYMBOL of old COBOL. If the period falls, so too do
> fall-through paragrphs, PERFORM .. THRU and the 77 level .. all of which are
> indefensible. 

The full stop will not 'fall'.  Its use (whether minimum or maximum)
is quite independent of other features, you are merely attempting to
appeal to emotion.
 
> This is about culture, not about a punctuation mark. 

I thought that you had made it a crusade.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-24T01:33:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e59749e.288782844@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>> This is about culture, not about a punctuation mark. 
>
>I thought that you had made it a crusade.

You're right. It's a crusade against Bad Programming, not against the full stop.


Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 22)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-25T08:19:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dr96$fu7$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net>`

```
Robert Wagner wrote:


> You're right. It's a crusade against Bad Programming, not against the full
> stop.

No, yours is a crusade against programming that doesn't look identical to 
yours.

While you may have seen many lines of Cobol in various sites, and may have 
decided what was good or bad about those.  You are attempting to judge that 
others write 'Bad Programming' without even seeing a single line of their 
code.

I can find some 'Bad Programming' in your code, even when you have given 
reasonable cause for a particular practice:

RW> Moving sections of code in and out of if statements is simplified.

Yet in your demo program you consistently put the full stop at the end of 
the paragraph onm the end of the last statement.  Bad.

Good programming practice would have the full-stop on its own line after 
the last statement where it is more easily seen by not being lost in the 
clutter _and_ it fullfills the moving of the code, _including_ the last 
line.

I insist that you change this immediately otherwise I will think that you 
are only '90% competent' (or less).
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-25T03:48:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5acd51.20963372@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>While you may have seen many lines of Cobol in various sites, and may have 
>decided what was good or bad about those.  You are attempting to judge that 
>others write 'Bad Programming' without even seeing a single line of their 
>code.

The first sentence says I've seen many lines of COBOL; the second contradicts it
by saying I've seen none. 

>Yet in your demo program you consistently put the full stop at the end of 
>the paragraph onm the end of the last statement.  Bad.
…[4 more quoted lines elided]…
>line.

I like even better Donald Tees' idea of putting the 'terminating' full stop in
front of the paragraph name. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-25T18:07:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3etp7$ukp$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <3e5acd51.20963372@news.optonline.net>`

```
Robert Wagner wrote:

>>While you may have seen many lines of Cobol in various sites, and may have
>>decided what was good or bad about those.  You are attempting to judge
…[4 more quoted lines elided]…
> contradicts it by saying I've seen none.

Do you need me to type this very slowly for you ?

You have seen many lines of COBOL in various sites ...

You are attempting to judge that _others_ write 'Bad Programming' ..

Do you understand what 'others' mean ?  It means those of the group not 
contained in the first group.

You have seen much code of the first group, and no code of the 'others' 
group.

Is that clear now ?

You have claimed that older programmers are writing bad code even though 
you have not seen any of their code:

""I'd wager that, if one examined the code of people who support periods, 
(s)he
would also find paragraph names prefixed with numbers, large monolithic 
programs
containing GO TOs, and a generally poor sense of structural design. COBOL 
bears
that legacy. ""

Given that some of the posters here have chosen to use full stops then 
obviously you are accusing them of 'large monolithic programs' and 'poor 
sense of structural design'.

Yet you probably haven't seen any of their code.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-25T09:47:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5BAC34.7030907@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <3e5acd51.20963372@news.optonline.net>`

```
Robert Wagner wrote:
> Richard Plinston <riplin@Azonic.co.nz> wrote:
> 
…[4 more quoted lines elided]…
> Robert

I saw the reference, but you are crediting it to the wrong person ... 
not sure who suggested it.

Donald
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T00:36:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5bf15e.95740098@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <3e5acd51.20963372@news.optonline.net> <3E5BAC34.7030907@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote:

>Robert Wagner wrote:
>> Richard Plinston <riplin@Azonic.co.nz> wrote:
>> 
>> 
>> I like even better Donald Tees' idea of putting the 'terminating' full stop
in
>> front of the paragraph name. 
>> 
…[3 more quoted lines elided]…
>not sure who suggested it.

My apologies to Robert Jones for crediting his good idea to the wrong poster. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 23)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-25T04:25:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2dc85$e09027a0$0a8bf243@chottel>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz>`

```
I noticed two other things in the demo program that I would write
differently.  First:

if (a-byte not less than 'a' and not greater than 'z') or
   (a-byte not less than 'A' and not greater than 'Z') or
   (a-byte not less than '0' and not greater than '9') or
   (a-byte equal to '-')
      set cobol-character to true
else
      set not-cobol-character to true
end-if

I would write this as:
  
if (a-byte not = space) and
   (a-byte is alphabetic or
    a-byte is numeric or
    a-byte = '-')
      set cobol-character to true
else
      set not-cobol-character to true
end-if

I believe the orginal version was coded with the ascii character set in
mind and the latter version should work regardless of character set.

Second :

if a-byte equal to x'22' or x'27' ...

would be clearer if written as:

if a-byte equal to ascii-double-quote or ascii-single-quote ...

with those two fields appropriately defined as separate fields





Richard Plinston <riplin@Azonic.co.nz> wrote in article
<b3dr96$fu7$1@aklobs.kc.net.nz>...
> Robert Wagner wrote:
> 
> 
> > You're right. It's a crusade against Bad Programming, not against the
full
> > stop.
> 
> No, yours is a crusade against programming that doesn't look identical to

> yours.
> 
> While you may have seen many lines of Cobol in various sites, and may
have 
> decided what was good or bad about those.  You are attempting to judge
that 
> others write 'Bad Programming' without even seeing a single line of their

> code.
> 
…[5 more quoted lines elided]…
> Yet in your demo program you consistently put the full stop at the end of

> the paragraph onm the end of the last statement.  Bad.
> 
…[5 more quoted lines elided]…
> I insist that you change this immediately otherwise I will think that you

> are only '90% competent' (or less).
> 
>
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-25T15:00:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3g0dg$a5k$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel>`

```
Speaking of making things easy to edit (removing periods to aid in cutting and
pasting)...

I prefer the following IF OR style:

	IF A = B
	OR C=D
	OR E=F
                   PERFORM Z
            END-IF.

to:

	IF A = B OR
	    C=D   OR
	    E=F
                   PERFORM Z
            END-IF.


It makes it easy to add or comment out conditions as each condition is on the
same line as it's OR or AND.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2003-03-02T23:07:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59w8a.443$2p2.59@twister.nyroc.rr.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <b3g0dg$a5k$1@peabody.colorado.edu>`

```
opposite view below

"Howard Brazee" <howard@brazee.net> wrote in message
news:b3g0dg$a5k$1@peabody.colorado.edu...
> Speaking of making things easy to edit (removing periods to aid in cutting
and
> pasting)...
>
…[17 more quoted lines elided]…
> It makes it easy to add or comment out conditions as each condition is on
the
> same line as it's OR or AND.

And just to have one more thing noone can agree on, I prefer:
IF    VAR1 = VAR2    OR
        VAR3 = VAR4    OR
        E = F

My rationale: It is easier to read with the conditions lined up under each
other. (Note: I used tabs in the note, but would use spaces in real code.)
I considered your way, for your reason, but decided ease of reading was more
important (to me) than ease of debugging. Also, for mixed conditions, I
often code as follows, beacuse I believe it makes the meaning clearer:
IF    ERROR-FLAG NOT = 'Y'
        AND
        (VAR1 = VAR2   OR
        VAR3 = VAR4   OR
        E = F)
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-25T15:02:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YzL6a.833$PK3.80486@newssrv26.news.prodigy.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c2dc85$e09027a0$0a8bf243@chottel...
> I noticed two other things in the demo program that I would write
> differently.  First:
…[10 more quoted lines elided]…
> I would write this as:...

SPECIAL-NAMES.

   CLASS COBOL-CHARACTER IS  'a' THRU 'z', 'A' THRU 'Z', '0 THRU 9', ','
....

  ....
  IF WS-CHAR  IS [NOT] COBOL-CHARACTER......


(Alpha ranges do not work this nicely using EBCDIC character set)


MCM









>
> if (a-byte not = space) and
…[34 more quoted lines elided]…
> > No, yours is a crusade against programming that doesn't look identical
to
>
> > yours.
…[5 more quoted lines elided]…
> > others write 'Bad Programming' without even seeing a single line of
their
>
> > code.
…[6 more quoted lines elided]…
> > Yet in your demo program you consistently put the full stop at the end
of
>
> > the paragraph onm the end of the last statement.  Bad.
…[6 more quoted lines elided]…
> > I insist that you change this immediately otherwise I will think that
you
>
> > are only '90% competent' (or less).
> >
> >
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-02-26T06:35:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5C60B6.1D9BE7E1@worldnet.att.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <YzL6a.833$PK3.80486@newssrv26.news.prodigy.com>`

```
Michael Mattias wrote:
> (snip)
> > I would write this as:...
…[11 more quoted lines elided]…
> MCM

So, just make it read:

SPECIAL-NAMES.
    CLASS COBOL-CHARACTER IS
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-".

(that is, if you can fit it all on one line, or continue it)

And on an IBM mainframe COBOL, "IF WS-CHAR IS COBOL-CHARACTER" will
compile to a single TRT instruction.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T00:36:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5bf1a3.95808476@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel>`

```
"Charles Hottel" <chottel@cpcug.org> wrote:

>I noticed two other things in the demo program that I would write
>differently.  First:
…[19 more quoted lines elided]…
>end-if

Alphabetic and numeric are a minefield of inconsistency. Some compilers consider
'A' numeric because it might be a +1. Some consider space to be alphabetic.
Hyphen could be alphabetic, numeric or neither. I learned long ago to avoid
alphabetic and numeric tests. 

>I believe the orginal version was coded with the ascii character set in
>mind and the latter version should work regardless of character set.

You are right. I could test for A thru I, J thru R, etc. Soon as I did, someone
would make a cutting remark about 'EBCDIC bias', or describe a small-ending
system where the Latin alphabet is in reverse order. :)

The only system-independent solution is: 

move a-byte to test-byte
inspect test-byte converting 
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789-' to
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
if  test-byte equal to 'a'

>Second :
>
…[5 more quoted lines elided]…
>with those two fields appropriately defined as separate fields

I dislike making the reader look elsewhere. An inline solution would be:

if a-byte equal to '"' or quote   *> literal is apost-quote-apost

Again, this exposes you to compiler ambiguity. What is 'quote'? Some compilers
interpret it to mean double-quote and others to mean the current quote symbol:
apostrophe. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-26T15:03:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3h7bp$u8j$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net>`

```
Robert Wagner wrote:

>>if (a-byte not = space) and
>>   (a-byte is alphabetic or
…[8 more quoted lines elided]…
> consider 'A' numeric because it might be a +1. 

Which ?

> Some consider space to be alphabetic. 

No. _ALL_ consider space to be alphabetic, which is why there was a special 
case to exclude it.

Name any modern compiler which doesn't consider space to be alphabetic ?

> Hyphen could be alphabetic, numeric or neither. I learned long
> ago to avoid alphabetic and numeric tests.

No. You didn't learn anything, and you certainly didn't learn how they 
actually work.

> The only system-independent solution is:
> 
…[4 more quoted lines elided]…
> if  test-byte equal to 'a'

No, it isn't.  The code above _is_ system-independent and portable.

INSPECT CONVERTING is '85 standard and may not be available to anyone using 
pre'85 systems (thus is not system-independent).

>>Second :
>>
>>if a-byte equal to x'22' or x'27' ...
> 
> I dislike making the reader look elsewhere. An inline solution would be:

Yet you originally hard coded values that may need to be looked for in a 
ASCII value table.

> if a-byte equal to '"' or quote   *> literal is apost-quote-apost
> 
> Again, this exposes you to compiler ambiguity. What is 'quote'? Some
> compilers interpret it to mean double-quote and others to mean the current
> quote symbol: apostrophe.

Which actual compilers will take the figurative constant QUOTE to be 
anything other than '"' ?  The standard requires this to be the quote 
symbol and not apostrophe.
```

###### ↳ ↳ ↳ Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-25T22:36:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3hg93$1ki$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b3h7bp$u8j$1@aklobs.kc.net.nz...
> Robert Wagner wrote:
>
 <snip>
> > Again, this exposes you to compiler ambiguity. What is 'quote'? Some
> > compilers interpret it to mean double-quote and others to mean the
current
> > quote symbol: apostrophe.
>
…[4 more quoted lines elided]…
>

I know a number of compilers that have an OPTION for treating the figurative
constant QUOTE as either the character
    "
      or the character
    '

Certainly, all IBM compilers do (see the QUOTE/APOST compiler option).
Realia and Micro Focus also do (as they provide "IBM mainframe compatibility
options")  I believe that Fujitsu does - but haven't checked recently.

In EACH of these cases, there is "clear" documentation that using the "treat
QUOTE as an 'apostrophe'" compiler option places the code in "non-ANSI/ISO
conforming" mode.   I believe that many - if not most - of these same
compilers USED to (but no longer do) distinguish between the character
needed to delimit alphanumeric literals based on this same compiler option.
Currently IBM and Micro Focus (I don't know about the others) allow a
program to "mix" quotes and apostrophes as delimiters (but not the
figurative constant) in the same program.
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-26T18:12:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3hiel$3ad$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:

> I know a number of compilers that have an OPTION for treating the
> figurative constant QUOTE as either the character
>     "
>       or the character
>     '

So this shouldn't be 'confusing' to the average programmer, they should 
know when they use an option to make the program non-standard.
 
> option. Currently IBM and Micro Focus (I don't know about the others)
> allow a program to "mix" quotes and apostrophes as delimiters (but not the
> figurative constant) in the same program.

Yes, I was aware that literals could use either, as long as they were 
consistent for one literal.  Again this is non-standard.
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-26T00:40:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3hnh6$c80$1@slb6.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net> <b3hiel$3ad$1@aklobs.kc.net.nz>`

```
Just one more part to this thread.  In the 2002 COBOL Standard it *does*
become "Standard" to use apostrophe's or quotation mark (aka "single or
double quote marks") to delimit literals.  The QUOTE figurative constant,
however, remains the "double" quote mark.
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T10:59:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5c9e2a.10205268@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net> <b3hiel$3ad$1@aklobs.kc.net.nz> <b3hnh6$c80$1@slb6.atl.mindspring.net>`

```
I just tried this under Fujitsu:

01  a-byte pic x.
move quote to a-byte
evaluate a-byte
    when x'22' display 'double'
    when x'27' display 'single'
end-evaluate

It displayed 'single'.

Robert


"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Just one more part to this thread.  In the 2002 COBOL Standard it *does*
>become "Standard" to use apostrophe's or quotation mark (aka "single or
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-26T11:06:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302261106.19a31029@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net> <b3hiel$3ad$1@aklobs.kc.net.nz> <b3hnh6$c80$1@slb6.atl.mindspring.net> <3e5c9e2a.10205268@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> I just tried this under Fujitsu:
> 
…[7 more quoted lines elided]…
> It displayed 'single'.

RP>> So this shouldn't be 'confusing' to the average programmer, they should
RP>> know when they use an option to make the program non-standard.

But then you are not an 'average programmer'.
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 31)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-06T15:21:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303061521.27585925@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net> <b3hiel$3ad$1@aklobs.kc.net.nz> <b3hnh6$c80$1@slb6.atl.mindspring.net> <3e5c9e2a.10205268@news.optonline.net> <217e491a.0302261106.19a31029@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote


> > I just tried this under Fujitsu:
> > 
…[7 more quoted lines elided]…
> > It displayed 'single'.

Just a note to say that I tried this under Fujitsu and using entirely
the default options it displayed 'double'.

This is because Fujitsu have seen the light and made their version 7
compiler more standards compliant.  QUOTE is now the default setting.
```

###### ↳ ↳ ↳ Re: Quote vs Apost (was: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-26T09:10:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5CF511.2040901@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <b3hg93$1ki$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Certainly, all IBM compilers do (see the QUOTE/APOST compiler option).
> Realia and Micro Focus also do (as they provide "IBM mainframe compatibility
> options")  I believe that Fujitsu does - but haven't checked recently.
> 
Certainly Fujitsu does.  I have used '"quoted text"' quite frequently, 
as it is common nowadays to have to use quotation marks within file 
names to get arround imbedded space.

Donald


> In EACH of these cases, there is "clear" documentation that using the "treat
> QUOTE as an 'apostrophe'" compiler option places the code in "non-ANSI/ISO
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T11:25:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5ca3dc.11663493@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>

>> if a-byte equal to '"' or quote   *> literal is apost-quote-apost
>> 
…[6 more quoted lines elided]…
>symbol and not apostrophe.

I just tried Fujitsu and Realia. Both gave apostrophe for QUOTE.

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-26T12:45:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3j1vh$98s$1@slb0.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <3e5ca3dc.11663493@news.optonline.net>`

```
Show your compiler options (in effect) - I think that BOTH of your tests
were run with an "APOST" compiler option in effect - which does do exactly
what you say.  However, if you read the documentation - you will see that
both vendors DOCUMENT that this option is "non-conforming" - and that QUOTE
option is required for ANSI/ISO conformance.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-27T06:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d693c.14080476@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3h7bp$u8j$1@aklobs.kc.net.nz> <3e5ca3dc.11663493@news.optonline.net> <b3j1vh$98s$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Show your compiler options (in effect) - I think that BOTH of your tests
>were run with an "APOST" compiler option in effect - which does do exactly
>what you say.  However, if you read the documentation - you will see that
>both vendors DOCUMENT that this option is "non-conforming" - and that QUOTE
>option is required for ANSI/ISO conformance.

Yes, both tests were run with APOST on. The Fujitsu test was run with STDH,
meaning highest level ANSI standard. It did not negate the APOST option.
```

###### ↳ ↳ ↳ Robert Wagner's latest error (was: various other erroneous posts

_(reply depth: 25)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-25T22:28:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3hfq8$2ca$1@slb0.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net>`

```
Please, PLEASE Robert - do some (any?) research before you post these
statements where you CLAIM that "some compilers" do something or another.

The "alphabetic" test is clearly defined in the ANSI/ISO Standard.  All
conforming compilers treat the same characters as either alphabetic or NOT
alphabetic.  There was a difference (about 17 years ago) before the
introduction of the '85 Standard "Alphabetic-Upper" and "Alphabetic-Lower"
class tests on whether lower-case as well as upper-case letters were treated
as "alphabetic" - but in all current releases of conforming compilers there
is NOTHING whatsoever non-portable about the IF alphabetic class test.

Again, what you "learned long ago" (your words - not mine) is no longer true
with the currently supported version (using ANSI/ISO conforming options -
usually the defaults) of any mainframe or PC compiler that I know of.

If you really think that this is a "minefield of inconsistency" with any
currently SUPPORTED compiler, please post the code, compiler, and operating
system.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-26T09:34:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net>`

```
On Wed, 26 Feb 2003 00:36:55 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"Charles Hottel" <chottel@cpcug.org> wrote:
>
…[27 more quoted lines elided]…
>

You are joking aren't you?  On what platform would an "A" be
considered a plus 1?  Burroughs 15-20 years ago, maybe.  Certainly not
on any IBM or IBM like system I've ever done work on.  And if you've
never done a numeric test, then you've not lived in an environment of
user data entry.  You really are a piece of work.

>>I believe the orginal version was coded with the ascii character set in
>>mind and the latter version should work regardless of character set.
…[30 more quoted lines elided]…
>Robert

If you don't know what "quote" is, the only ambiguity is why you
didn't ask whomever installed the compiler what the standard option
is.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T23:16:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d4ab2.6262016@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Wed, 26 Feb 2003 00:36:55 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:
…[26 more quoted lines elided]…
>>Alphabetic and numeric are a minefield of inconsistency. Some compilers
consider
>>'A' numeric because it might be a +1. Some consider space to be alphabetic.
>>Hyphen could be alphabetic, numeric or neither. I learned long ago to avoid
…[4 more quoted lines elided]…
>considered a plus 1? 

I've seen it .. on then-current mainstream compilers. I'm not making this up. At
the time, I too found it hard to believe. 

In the Good Old Days, some compilers wouldn't let you test pic x for IS NUMERIC;
it had to be pic 9.

>  Certainly not
>on any IBM or IBM like system I've ever done work on.  And if you've
>never done a numeric test, then you've not lived in an environment of
>user data entry.  You really are a piece of work.

Don't be insulting. Of course I've done numeric tests. How much more difficult
is it to test for 0-9 than numeric? Not much .. both fit on one line of code. 

>If you don't know what "quote" is, the only ambiguity is why you
>didn't ask whomever installed the compiler what the standard option
>is.

In most cases I installed the compiler. In others, the person who installed it
no longer works there and the options are in a directory to which  I don't have
access. 

I don't want to write installation-specific code. I want to write generic COBOL
that works almost everywhere. Is that unreasonable? 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-26T17:26:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3jiev$eq1$1@slb3.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net> <3e5d4ab2.6262016@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e5d4ab2.6262016@news.optonline.net...
> SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:
>
…[4 more quoted lines elided]…
> >>
 <snip>
>
> In most cases I installed the compiler. In others, the person who
installed it
> no longer works there and the options are in a directory to which  I don't
have
> access.
>
> I don't want to write installation-specific code. I want to write generic
COBOL
> that works almost everywhere. Is that unreasonable?
>
> Robert

No, that isn't unreasonable.  However, to do so, you really SHOULD read the
documentation on which compiler options/directives are required for ANSI/ISO
conformance.  With IBM, Micro Focus, Realia, and Fujitsu (possibly others),
you *MUST* install it with the QUOTE compiler option as the default.

What you want to do is look for a section (where it is depnends on the
vendor) like the following from the IBM documenation on which of their
options are required for ANSI conformance (and hence for the greatest
porabilty probability) .  See:

 "2.4.1 Option settings for COBOL 85 Standard conformance"

at

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/2.4.1

(Notice how it says that QUOTE is a required option - among others)

I think that you will find a similar section in all compiler vendor
documentation.  (See a separate note on how Micro Focus offers the

   Dialect(ANS85)

feature to turn on (and off) all their non-conforming options.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-27T10:05:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A5FA25521FD29081.445A75A90B5E0B46.9FDC12A7673563B2@lp.airnews.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net> <3e5d4ab2.6262016@news.optonline.net>`

```
On Wed, 26 Feb 2003 23:16:01 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:
>
…[40 more quoted lines elided]…
>

Please give an example or document what system would pass a numeric
test if the byte contained an alphabetic "A".  

>In the Good Old Days, some compilers wouldn't let you test pic x for IS NUMERIC;
>it had to be pic 9.
…[20 more quoted lines elided]…
>Robert

Then I suggest you don't work for an employer, i.e., work for
yourself, write code for yourself etc.  Installations have their
options and not all have the same options.  If you work in their
environment then you must know what the constraints, limitations and
options of that environment are.  So yes, it is unreasonable  that you
would't take the time to find out what the institution's Cobol compile
options are.  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2003-02-27T18:56:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3mc47$1o5h30$1@ID-39920.news.dfncis.de>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net> <3e5d4ab2.6262016@news.optonline.net> <A5FA25521FD29081.445A75A90B5E0B46.9FDC12A7673563B2@lp.airnews.net>`

```

"SkippyPB" <swiegand@neo.NOSPAM.rr.com> wrote in message
news:A5FA25521FD29081.445A75A90B5E0B46.9FDC12A7673563B2@lp.airnews.net...
> On Wed, 26 Feb 2003 23:16:01 GMT, robert@wagner.net (Robert Wagner)
> enlightened us:

<snip>

> >>You are joking aren't you?  On what platform would an "A" be
> >>considered a plus 1?
> >
> >I've seen it .. on then-current mainstream compilers. I'm not making this
up. At
> >the time, I too found it hard to believe.
> >
>
> Please give an example or document what system would pass a numeric
> test if the byte contained an alphabetic "A".

As he already pointed out, on the IBM mainframe, the hex code for a +1 and
the capital "A" are the same (x'c1').  Therefore, the following would
display "numeric"...

01 a-field.
   05 a-number        pic s9.

move "A" to a-field.
if a-number numeric
   display "numeric"
else
   display "not numeric"
end-if.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 29)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-02-28T11:15:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8821C92EDBF9C2B4.33C7642E58D2E364.426C469271BBDF6C@lp.airnews.net>`
- **References:** `<3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net> <3e5d4ab2.6262016@news.optonline.net> <A5FA25521FD29081.445A75A90B5E0B46.9FDC12A7673563B2@lp.airnews.net> <b3mc47$1o5h30$1@ID-39920.news.dfncis.de>`

```
On Thu, 27 Feb 2003 18:56:40 -0600, "DBuck" <dbuck@prairieinet.net>
enlightened us:

>
>"SkippyPB" <swiegand@neo.NOSPAM.rr.com> wrote in message
…[32 more quoted lines elided]…
>

Notice I said "alphabetic A".  Look at the EBCDIC Binary code for the
Letter A and a plus 1:  The letter A is indeed a hex C1 but is
represented in binary as 1100 0001.  A numeric 1 is represented in
binary as 1111 0001.  However, once arithmetic has been done on the
field, the 1111 will become 1100, so I see that I was wrong having
forgot somewhat about this minor anomaly.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 30)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-03-02T17:22:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E623DD0.4040909@optonline.NOSPAM.net>`
- **References:** `<3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <A11608520AC71C9C.339372FC91D3FB47.CAB426428539B436@lp.airnews.net> <3e5d4ab2.6262016@news.optonline.net> <A5FA25521FD29081.445A75A90B5E0B46.9FDC12A7673563B2@lp.airnews.net> <b3mc47$1o5h30$1@ID-39920.news.dfncis.de> <8821C92EDBF9C2B4.33C7642E58D2E364.426C469271BBDF6C@lp.airnews.net>`

```
SkippyPB wrote:
> On Thu, 27 Feb 2003 18:56:40 -0600, "DBuck" <dbuck@prairieinet.net>
> enlightened us:
…[35 more quoted lines elided]…
> binary as 1111 0001.

Only if you're working with Display fields:

binary	= x'00000001'
packed	= x'1c'

The x'F1' is a COBOLism applied after calculations, there are no 
instructions to perform calculations on external decimal, i.e., Display, 
fields.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 25)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-26T09:03:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3is1f$2632$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e5bf1a3.95808476@news.optonline.net...

> Alphabetic and numeric are a minefield of inconsistency.

They shouldn't be.

> Some compilers consider 'A' numeric because it might be a +1.

Depends on USAGE and PICTURE.  If the raw data in a PIC 9 DISPLAY item is
"A", the numeric test had better be false.   If the PICTURE is S9, it might
end up returning TRUE depending on the implementor's representation of zones
and digits.   So far as I know there are no inconsistencies.

> Some consider space to be alphabetic.

Is there someone that doesn't?  ANSI X3.23-1974 explicitly requires that
they do so (page II-43, 5.2.1.2, Class Condition), and I see evidence that
the '68 standard did as well.

> Hyphen could be alphabetic, numeric or neither.

I don't think so.

Alphabetic in '74 is 'A' through 'Z' plus space.  Hyphen could be in a
numeric data item if the item has a SIGN SEPARATE clause and the hyphen's in
the right place for a sign; otherwise it's probable (but not certain) that
it would fail the NUMERIC tests.  Alphabetic in '85 adds lower-case (and the
tests ALPHABETIC-UPPER and ALPHABETIC-LOWER).  To that, the 2002 standard
adds rules for LOCALEs to those already specified; they're not the issue
here.

A hyphen in any "normal" data item should UNCONDITIONALLY cause the item to
FAIL an ALPHABETIC test.

If a COBOL(68),. COBOL74, COBOL85 or COBOL2002 compiler generated code that
indicated that an elementary USAGE DISPLAY item containing a hyphen was
ALPHABETIC, I would contend that that compiler was in direct violation of
the standard to which its vendors claim it conforms.

> I learned long ago to avoid alphabetic and numeric tests.

And after all this we're supposed to presume that's because you had read and
understood what the tests were actually supposed to do?

> Again, this exposes you to compiler ambiguity. What is 'quote'? Some
compilers
> interpret it to mean double-quote and others to mean the current quote
symbol:
> apostrophe.

ANSI X3.23-1974, ANSI X3.23-1985, and ISO/IEC 1989:2002 all explicitly
require "QUOTE"/"QUOTES" to mean quotation mark (or double-quote) as
distinct from apostrophe (or single-quote) (I'll forego the specific
citations for the moment).  Which compilers violate the standards in that
respect?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-27T00:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2ddfa$6208c6a0$53c2f943@chottel>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com>`

```
This is from an IBM mainframe viewpoint.

   05  alpha-1                          pic x   value 'A'.
   05  num-1 redefines alpha-1 pic 9.
   05  num-p                           pic s9 comp-3.

    if num-1 is numeric   ....    should be false.

    move num-1 to num-p
    if num-p is numeric   ....    should be true. 

This because in EBCDIC  an A  is x'C1' and when it is moved to a packed
decimal
field it becomes  x'1C' and the C is treated as a plus sign and num-1 is
treated as +1.
In my view NOT a reason to avoid NUMERIC tests just a reason to be cautious
and to
understand how language constructs work.  No computer language is perfect
and every
one that I have seen has its own peculiar situations.  An experienced
programmer learns
to recognize these and deal with them.

Chuck Stevens <charles.stevens@unisys.com> wrote in article
<b3is1f$2632$1@si05.rsvl.unisys.com>...
> 
> "Robert Wagner" <robert@wagner.net> wrote in message
…[9 more quoted lines elided]…
> "A", the numeric test had better be false.   If the PICTURE is S9, it
might
> end up returning TRUE depending on the implementor's representation of
zones
> and digits.   So far as I know there are no inconsistencies.
> 
…[3 more quoted lines elided]…
> they do so (page II-43, 5.2.1.2, Class Condition), and I see evidence
that
> the '68 standard did as well.
> 
…[5 more quoted lines elided]…
> numeric data item if the item has a SIGN SEPARATE clause and the hyphen's
in
> the right place for a sign; otherwise it's probable (but not certain)
that
> it would fail the NUMERIC tests.  Alphabetic in '85 adds lower-case (and
the
> tests ALPHABETIC-UPPER and ALPHABETIC-LOWER).  To that, the 2002 standard
> adds rules for LOCALEs to those already specified; they're not the issue
> here.
> 
> A hyphen in any "normal" data item should UNCONDITIONALLY cause the item
to
> FAIL an ALPHABETIC test.
> 
> If a COBOL(68),. COBOL74, COBOL85 or COBOL2002 compiler generated code
that
> indicated that an elementary USAGE DISPLAY item containing a hyphen was
> ALPHABETIC, I would contend that that compiler was in direct violation of
…[4 more quoted lines elided]…
> And after all this we're supposed to presume that's because you had read
and
> understood what the tests were actually supposed to do?
> 
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-26T22:32:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302262232.28ff764e@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com> <01c2ddfa$6208c6a0$53c2f943@chottel>`

```
"Charles Hottel" <chottel@cpcug.org> wrote

>    05  alpha-1                          pic x   value 'A'.
>    05  num-1 redefines alpha-1 pic 9.
…[5 more quoted lines elided]…
>     if num-p is numeric   ....    should be true. 

If it was standard Cobol then "IF num-p IS NUMERIC" wouldn't be
allowed.

'85 states that an IF NUMERIC can only reference a field that is
explicitly or implicitly DISPLAY.

If you do a numeric test on Comp-3 or any other non-Display field then
it is a case of Garbabe In, Garbage Out.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-28T00:38:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2dec1$9a3c6960$d093f243@chottel>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com> <01c2ddfa$6208c6a0$53c2f943@chottel> <217e491a.0302262232.28ff764e@posting.google.com>`

```
You snipped out my first sentence: "from an IBM mainframe point of view". I
never claimed it was standard. I simply thought some people would not
understand how Mr. Wanger could ever think A = +1 and was trying to
demonstrate how it could happen. I was NOT advocating using NUMERIC check
on COMP-3/PACKED DECIMAL.

Richard <riplin@Azonic.co.nz> wrote in article
<217e491a.0302262232.28ff764e@posting.google.com>...
> "Charles Hottel" <chottel@cpcug.org> wrote
> 
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-27T06:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5d6cdb.15007992@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e5bf1a3.95808476@news.optonline.net...

>> Some consider space to be alphabetic.
>
>Is there someone that doesn't? 

Speakers of Common English, who understand that space is not a letter in the
Latin alphabet. 

>> Hyphen could be alphabetic, numeric or neither.
>
>I don't think so.

Not a biggie. Let's skip that one.

>> I learned long ago to avoid alphabetic and numeric tests.
>
>And after all this we're supposed to presume that's because you had read and
>understood what the tests were actually supposed to do?

I'm more concerned with Practice than Theory. When I find them doing irrational
or unpredictable stuff, I stop using them. 


>ANSI X3.23-1974, ANSI X3.23-1985, and ISO/IEC 1989:2002 all explicitly
>require "QUOTE"/"QUOTES" to mean quotation mark (or double-quote) as
>distinct from apostrophe (or single-quote) (I'll forego the specific
>citations for the moment).  Which compilers violate the standards in that
>respect?

Almost all of them, if you specify APOST. I thought APOST referred to source
code bounding of literals, not interpretation of QUOTE. Evidentally I was wrong;
compilers apply it to both. 

APOST is not necessary on IBM, Micro Focus and Fujitsu because they let you use
either. I believe it is necessary on others. 

My point is: if you want to write generic COBOL, don't use QUOTE. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-27T03:12:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302270312.d78a94f@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com> <3e5d6cdb.15007992@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> Some consider space to be alphabetic.
> >
…[3 more quoted lines elided]…
> Latin alphabet. 

But Cobol is not defined by 'Common English'.
 
> >> Hyphen could be alphabetic, numeric or neither.
> >
> >I don't think so.
> 
> Not a biggie. Let's skip that one.

LOL.
 
> I'm more concerned with Practice than Theory. When I find them doing irrational
> or unpredictable stuff, I stop using them. 

No. They _are_ entirely predictable, by anyone who reads how they are
supposed too work.  For example NUMERIC can only be done on DISPLAY
variables, it seems that you tried it on COMP-3 and found it
'strange'.  That should have been predictable.
 
> My point is: if you want to write generic COBOL, don't use QUOTE. 

If you want to write standard Cobol don't use APOST, use option QUOTE.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 27)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-27T12:11:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3lrde$15ui$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com> <3e5d6cdb.15007992@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e5d6cdb.15007992@news.optonline.net...

> >ANSI X3.23-1974, ANSI X3.23-1985, and ISO/IEC 1989:2002 all explicitly
> >require "QUOTE"/"QUOTES" to mean quotation mark (or double-quote) as
…[4 more quoted lines elided]…
> Almost all of them, if you specify APOST. I thought APOST referred to
source
> code bounding of literals, not interpretation of QUOTE. Evidentally I was
wrong;
> compilers apply it to both.

And APOST is an implementor extension to the '68, '74 and '85 standards.
The behavior it enables is in direct conflict with the standard.

> APOST is not necessary on IBM, Micro Focus and Fujitsu because they let
you use
> either. I believe it is necessary on others.

APOST, or anything that does what APOST apparently does, is considered
"necessary" in our compilers.

> My point is: if you want to write generic COBOL, don't use QUOTE.

A better "best practice":  don't use vendor-specific extensions like APOST.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 28)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-27T12:18:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3lrqh$169b$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e586d2e.221332893@news.optonline.net> <217e491a.0302231118.1dae3629@posting.google.com> <3e59749e.288782844@news.optonline.net> <b3dr96$fu7$1@aklobs.kc.net.nz> <01c2dc85$e09027a0$0a8bf243@chottel> <3e5bf1a3.95808476@news.optonline.net> <b3is1f$2632$1@si05.rsvl.unisys.com> <3e5d6cdb.15007992@news.optonline.net> <b3lrde$15ui$1@si05.rsvl.unisys.com>`

```
I wrote:

<<APOST, or anything that does what APOST apparently does, is considered
 "necessary" in our compilers.>>

What I intended to write was more like

<<APOST, or anything that does what APOST apparently does, is NOT considered
"necessary" in our pre-2002 compilers; in fact, doing what APOST apparently
does is not even "possible" in our pre-2002 compilers.  Our compilers all
require alphanumeric literals to be composed in a manner that is consistent
with the applicable standard, and don't give the user the option to do
otherwise in this respect.>>

    -Chuck Stevens

POSSIBLE .
>
> > My point is: if you want to write generic COBOL, don't use QUOTE.
>
> A better "best practice":  don't use vendor-specific extensions like
APOST.
>
>     -Chuck Stevens
>
>
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-24T08:32:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3dhet$1jo9$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e586d2e.221332893@news.optonline.net>`

```
Robert Wagner wrote:

<<The period is more than a punctuation mark, it's a SYMBOL of old COBOL. If
the period falls, so too do fall-through paragrphs, PERFORM .. THRU and the
77 level .. all of which are indefensible. >>

Trouble!  Right here in River City!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T07:08:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e587352.222904756@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>You *might* want to submit a paper asking for "middle of the paragraph"
>periods to be put in the archaic category in the NEXT COBOL Standard.  Maybe
>if you need that and heard back from the real standards committees you would
>stop making a complete fool of yourself.

I probably will not be around seventeen years hence. COBOL standards committees
are unacceptably slow. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-02-23T07:25:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0302230725.545aa694@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e587352.222904756@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e587352.222904756@news.optonline.net>...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
> 
…[8 more quoted lines elided]…
> Robert

Two quick comments:

First re: speed and standards - check the excellent article by Jerome
Garfunkel at cobolreport.com - it has some interesting historical
perspective on this and on COBOL's place in general.

Second - I glean from your messages that you think making something
Archaic is the first step toward making it obsolete.  Items in the
Archaic category do not move directly into obsolete by any mechanism,
nor it appearing in the Archaic category a precursor to something
becoming obsolete.
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-23T23:04:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e59514c.279739508@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e587352.222904756@news.optonline.net> <bfdfc3e8.0302230725.545aa694@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e587352.222904756@news.optonline.net>...
>> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>> 
…[5 more quoted lines elided]…
>> I probably will not be around seventeen years hence. COBOL standards
committees
>> are unacceptably slow. 
>> 
…[6 more quoted lines elided]…
>perspective on this and on COBOL's place in general.

I thought it was exceptionally well written. I would only quibble with "No other
programming language has such a robust IDE." DevStudio is better than any COBOL
IDE.

I used to live in Albany, which is 40 miles from Garfunkel's home in Woodstock.
If I'd read the article sooner, I would have offered him and spouse dinner at
one of two outstanding four-star restaurants in nearby Saugerties, in exchange
for conversation. The Hudson River Valley is a magical place. 

>Second - I glean from your messages that you think making something
>Archaic is the first step toward making it obsolete.  Items in the
>Archaic category do not move directly into obsolete by any mechanism,
>nor it appearing in the Archaic category a precursor to something
>becoming obsolete.

I didn't say anything about Archaic, Messrs. Klein and Stevens did. 

Garfunkel says, "COBOL features designated as "obsolete" are required to remain
in the new COBOL standard for at least one more iteration before they�re
permanently removed from the official COBOL standard."  He doesn't say how they
reach the Obsolete status. 

-----------------------------------------------
We COBOL programmers are inured to disrespect, but I knew I touched a nerve when
my name and flammage become the Subject of a thread originated by William Klein.
I must be getting close to the sacred orb protected by  keepers of the flame.

I know what it is, because I spent my life rewriting it. It's Bad Programming. 

Robert
```

###### ↳ ↳ ↳ Re: Robert Wagner continues hs errors (was: COBOL/DIALOGUE System

_(reply depth: 20)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-24T08:41:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3di0f$1k8b$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b319vj$2jao$1@si05.rsvl.unisys.com> <3e549c05.419538311@news.optonline.net> <217e491a.0302201058.34ddb93f@posting.google.com> <3e5587c9.31506817@news.optonline.net> <b35kl7$2fvu$1@si05.rsvl.unisys.com> <3e584a83.212456266@news.optonline.net> <b39k8b$gec$1@slb1.atl.mindspring.net> <3e587352.222904756@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e587352.222904756@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:

> I probably will not be around seventeen years hence. COBOL standards
committees
> are unacceptably slow.

Id argue that amuch more productive way to accomplish your desired goals in
that respect is to suit up and show up; certainly throwing rotten tomatoes
from the sidelines at those who have been doing their level best to produce
the current (and the next) standard in a timely fashion does nothing but
slow them down.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-20T15:07:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b31d8l$vd5$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net>`

```
Robert Wagner wrote:

> I cannot dispute the Rules of COBOL, 

> A STATEMENT is bigger than a sentence. A statement can use more than one
> sentence. The word they should have used is CLAUSE.

You then immediately turn around and dispute them.

> Collins English Dictionary defines Sentence as: 

It ain't English, get over it.

> What we have is a struggle between technicians who want to preserve the
> period because they think it makes parsing easier 

Why would you think it make parsing easier ?

> The 2002 standard
> recommends against using periods while ambivalantly making them
> significant in NEXT SENTENCE.
 
The standard disallows use of NEXT SENTENCE in any situation where it would 
make a difference.  It may only be used in an IF or SEARCH that is 
terminated by a full stop (or specifically does not have an END-IF or 
END-SEARCH).

It is only when it is used as an extension (such as MF) or is contrived to 
defeat the intent of the standard that there would be any difference.

The _standard_ makes no such significance for NEXT SENTENCE and full stops 
that you claim.

How hard it that to understand ?
```

###### ↳ ↳ ↳ Next Sentence vs Continue (was: COBOL/DIALOGUE System

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-19T20:42:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b31fb2$ql1$1@slb9.atl.mindspring.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b31d8l$vd5$1@aklobs.kc.net.nz>`

```
Sorry Richard, but as previously stated - both J4 and WG4 have confirmed
that the '85 Standard did (whether intentionally or not) make a real
difference between  NEXT SENTENCE and CONTINUE in *fully* conforming source
code.  The rule is that the NEXT SENTENCE phrase may not be  *immediately*
in an IF that is terminated by an END-IF.  However, it may well be in an IF
that is terminated by the ELSE of a containing IF that does, itself end in
an END-IF.  This means that it is entirely possible to have '85 Standard
conforming source code that requires that a compiler (and a programmer)
knows the difference between the two.

Having said that, Robert was mistaken in most of the rest of what he wrote,
so I hope he understood the intent of your note.
```

###### ↳ ↳ ↳ Re: Next Sentence vs Continue (was: COBOL/DIALOGUE System

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-19T23:32:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302192332.5ec38f87@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b31d8l$vd5$1@aklobs.kc.net.nz> <b31fb2$ql1$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote

> Sorry Richard, but as previously stated - both J4 and WG4 have confirmed
> that the '85 Standard did (whether intentionally or not) make a real
…[6 more quoted lines elided]…
> knows the difference between the two.
 
I am aware that the committees have had to agree that the wording of
the standard can be contrued to allow some contrived constructs
designed to fit the letter of the rules rather than what I believe to
be the intent.

Of course some extensions also allow there to be a difference too.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-20T02:35:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E543F34.63CC32CE@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net>`

```


Robert Wagner wrote:

> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>

Gawd ! I jes keep on checkin'  this one - jes in case there's actually something
about the topic MICRO FOCUS DIALOG SYSTEM

Can some brave heart start a new thread with "Robert versus the Rest : Was Dialogue
System ". Could always loop back to 'Best Practices'  <G>

I don't suppose it matters a dam, but Chuck, your extracts/definition of clauses,
sentences etc. convinced me. Hey it was easier for you than Colin Powell at the UN.
Sacre Bleu !

Jimmy
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-20T15:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b32qhk$t55$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net>`

```

On 19-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> I cannot dispute the Rules of COBOL, which are clearly stated in the citations
> you gave and I deleted for brevity. My problem is with incorrect word usage.
>
> A STATEMENT is bigger than a sentence. A statement can use more than one
> sentence. The word they should have used is CLAUSE.

In English a statement can be bigger than a sentence, it can be smaller than a
sentence, it can be the same size as a sentence.  It is "a single declaration or
remark".

Which is also is true with a statement in CoBOL.


A clause is "a group of words containing a subject and predicate and functioning
as a member of a complex or compound sentence".  A predicate may or may not
include a verb.


> My Best Practice is don't use periods and don't use NEXT SENTENCE. Both are in
> the same Legacy boat.

So you are upset because CoBOL isn't English enough for you in it's definitions
of statement and sentence - so you recommend making it more English by only
using a period to end a paragraph.  All paragraphs are one sentence long.   
Just like English...

Anyway,  I don't use NEXT SENTENCE, and I do use END IF.   Given that, what
advantage would my programs gain if they didn't have periods?
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-21T01:02:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e557aa4.28141917@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b32qhk$t55$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>So you are upset because CoBOL isn't English enough for you in it's definitions
>of statement and sentence - so you recommend making it more English by only
>using a period to end a paragraph.  All paragraphs are one sentence long.   
>Just like English...

Well, just like spoken and poetic English. COBOL isn't Literature. It's written
by code monkeys trying to get the job done with below-average literacy. 

It would be refreshing to see COBOL written in blank verse. I've tried without
success. 

>Anyway,  I don't use NEXT SENTENCE, and I do use END IF.   Given that, what
>advantage would my programs gain if they didn't have periods?

Huge advantage. Suppose you wrote
 move a to b.
 move c to d.
Then you decided to do it only under certain conditions. The code becomes
 if (condition)
    move a to b
    move c to d
end-if

You must tediously delete the periods on every line. I would turn the question
around to ask what utilityt these periods provide. The answer is none. If
periods are superfluous, why write them in the first place?

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 14)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-21T14:33:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Nq5a.14901$UF6.1531752@newssrv26.news.prodigy.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b32qhk$t55$1@peabody.colorado.edu> <3e557aa4.28141917@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e557aa4.28141917@news.optonline.net...
> "Howard Brazee" <howard@brazee.net> wrote:

> COBOL [is] written by code monkeys trying to get the job done with
below-average literacy.

I beg your pardon, sir?

There are numerous COBOL programmers who create prose for publication; prose
not limited to technical subjects.

Michael Mattias
One of many published 'below-average literacy code monkeys'
Racine WI
mmattias@talsystems.com.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T15:25:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35gd1$8u4$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b32qhk$t55$1@peabody.colorado.edu> <3e557aa4.28141917@news.optonline.net> <4Nq5a.14901$UF6.1531752@newssrv26.news.prodigy.com>`

```

On 21-Feb-2003, "Michael Mattias" <michael.mattias@gte.net> wrote:

> > COBOL [is] written by code monkeys trying to get the job done with
> below-average literacy.
>
> I beg your pardon, sir?

I think he vastly over-rates "average literacy".

Of course, when he starts an argument on this forum and EVERY SINGLE response
disagrees with him completely (without anybody arguing with any of these
responses) - then we all must be idiots.   I know several people who write books
that the idiot publishers won't publish and the idiot readers won't buy.

Us code-monkeys have to be below-average literacy, because if there was one with
half an ounce of sense, one of these posts would be supporting his statements -
or at least arguing with someone who disagreed with him.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T15:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35g03$8mv$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b32qhk$t55$1@peabody.colorado.edu> <3e557aa4.28141917@news.optonline.net>`

```

On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> >So you are upset because CoBOL isn't English enough for you in it's
> >definitions
…[6 more quoted lines elided]…
> by code monkeys trying to get the job done with below-average literacy.

Then with your spoken and poetic CoBOL, leave out the periods.    (I thought you
said periods were words)

If you're going to demand CoBOL be English like, at least compare written CoBOL
with written English.

> It would be refreshing to see COBOL written in blank verse. I've tried without
> success.

It's not hard at all.  But maintenance is a bitch.  Blank verse is designed to
add ambiguity and isn't designed to be obvious.   Good programming goes counter
to these goals.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-21T15:20:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35g4m$8tl$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <b2j9jb$2bqb$1@si05.rsvl.unisys.com> <3e4d940f.152644618@news.optonline.net> <b2tqkp$6l1$1@si05.rsvl.unisys.com> <3e5423be.388742903@news.optonline.net> <b32qhk$t55$1@peabody.colorado.edu> <3e557aa4.28141917@news.optonline.net>`

```

On 20-Feb-2003, robert@wagner.net (Robert Wagner) wrote:

> >Anyway,  I don't use NEXT SENTENCE, and I do use END IF.   Given that, what
> >advantage would my programs gain if they didn't have periods?
…[12 more quoted lines elided]…
> periods are superfluous, why write them in the first place?

I could have cut and pasted using a windows utility without including the
period.   But any rate, it is not tedious nor onerous to remove the periods.

I write them for clarity.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-14T12:38:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302141238.67b93a3d@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote 

> To me, code that
> depends upon a stylistic trick such as only having a period at the end of a
> paragraph is non-portable and dangerous.

While I have no issue with your liking of full stops, I would like to
know why you categorize 'minimum full stops' in this way.

* In what way does the code _depend_on_ not having full stops ?
 
Stops could be added anywhere that is not within a structure, just as
you would have them, without changing the meaning.  There is no
dependancy.

* In what way is it a stylistic 'trick' ?

How does it trick anything ?

* In what way is it non-portable ?

Which compilers or operating systems won't compile it to work
identically ?

* In what way is it dangerous ?

Compared to, say, having extra full-stops accidentally left in a block
under an IF.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-17T15:48:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2r090$1nl$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <217e491a.0302141238.67b93a3d@posting.google.com>`

```

On 14-Feb-2003, riplin@Azonic.co.nz (Richard) wrote:

> > To me, code that
> > depends upon a stylistic trick such as only having a period at the end of a
…[3 more quoted lines elided]…
> know why you categorize 'minimum full stops' in this way.

I don't understand what you're asking here.  Specifically what is "minimum full
stops"?.

> * In what way does the code _depend_on_ not having full stops ?

If "Next Sentence" is used to mean the same thing as "Exit Paragraph", then
having a period before the end of the paragraph will have it work incorrectly.

> Stops could be added anywhere that is not within a structure, just as
> you would have them, without changing the meaning.  There is no
> dependancy.

The concept of "go to next period" is dangerous when a period could be added
without a syntax check.

> * In what way is it a stylistic 'trick' ?

To make it mean "Exit Paragraph", then you must use a style.  (one I haven't
seen used).

> How does it trick anything ?

It tricks maintenance programmers.

> * In what way is it non-portable ?

Programmers will do conversions - it is best to make your code obvious to some
contract programmer who isn't used to your style.

> Which compilers or operating systems won't compile it to work
> identically ?
>
> * In what way is it dangerous ?

It tricks maintenance programmers.

> Compared to, say, having extra full-stops accidentally left in a block
> under an IF.

If a period is left in before an END-IF, then the compiler will tell you.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-17T11:19:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302171119.ef8e685@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <217e491a.0302141238.67b93a3d@posting.google.com> <b2r090$1nl$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote 

> > > To me, code that
> > > depends upon a stylistic trick such as only having a period at the end of a
> > > paragraph is non-portable and dangerous.

I now understand that you aren't against 'only having a period at the
end of a paragraph', you are against next sentence in conjuction with
END-IF.

As next sentence is disallowed by the standard in any structure that
has an END-IF or END-SEARCH, then any use of next sentence in these
conditions is indeed a stylistic trick that is dangerous and
non-portable.

* I do know that a clarification has conceeded that the standard was
insufficiently rigorous and that some contrived usage of next sentence
is not specifically disallowed as it should be.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-02-17T19:49:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2rec7$a16$1@peabody.colorado.edu>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net> <b2j3b6$qq8$1@peabody.colorado.edu> <217e491a.0302141238.67b93a3d@posting.google.com> <b2r090$1nl$1@peabody.colorado.edu> <217e491a.0302171119.ef8e685@posting.google.com>`

```

On 17-Feb-2003, riplin@Azonic.co.nz (Richard) wrote:

> > > > To me, code that
> > > > depends upon a stylistic trick such as only having a period at the end
…[5 more quoted lines elided]…
> END-IF.

This latter is what I was calling dangerous.  It's not clear from above that the
it isn't the "stylistic trick" that bothered me - it was the way NEXT SENTENCE
as an EXIT PARAGRAPH depended upon that style that I considered dangerous.

> As next sentence is disallowed by the standard in any structure that
> has an END-IF or END-SEARCH, then any use of next sentence in these
…[5 more quoted lines elided]…
> is not specifically disallowed as it should be.

Specifically, IBM has chosen to allow a NEXT SENTENCE within an IF END-IF loop.
 Using the NEXT SENTENCE as a replacement for END PARAGRAPH (which is not yet
available in my compiler), is non-portable as well.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-14T09:22:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2j8kn$2b2s$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <b2g2kt$7si$1@slb9.atl.mindspring.net> <3e4c333b.62306986@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e4c333b.62306986@news.optonline.net...

> Micro Focus also has EXIT PARAGRAPH, which is the same as NEXT SENTENCE if
one
> doesn't use periods.

The current ISO standard includes both EXIT PARAGRAPH and EXIT SECTION.

> I avoid NEXT SENTENCE because it is non-portable. Most
> compilers make it synonymous with CONTINUE; Micro Focus thinks it means
'after
> the next period'.

Silly Micro Focus.  Can you imagine any implementor with the remotest
consideration for portability actually producing a compiler that does what
every standard from at the latest ANSI X3.23-1968 through the current ISO
standard has required that NEXT SENTENCE actually accomplish?        ;-)

> Restoring the significance of periods, which are generally
> regarded as anachronistic, is an error by Micro Focus. In practice,
there's a
> big difference between CONTINUEing and going to the next period, which is
> usually end of paragraph.

The current ISO standard does have more ways of limiting periods to the ends
of paragraphs, but that's not the only meaningful, clear, legible way to
write COBOL programs.  Thus far, sentences terminated by periods within
paragraphs has not (yet) been marked an archaic element in standard COBOL.
Programs *can* be written so that intermediate periods are unnecessary, but
there is no particular reason other than style (either individual or site
standards) to do so.  That *you* regard periods as unconditionally
anachronistic, and that many of the people who jump onto the latest
bandwagon of programming style regard them as unconditionally anachronistic,
does not necessarily make it so.

> Semantically,  the EXIT clauses and CONTINUE have the flavor of COBOL
because
> they begin with a verb, whereas NEXT SENTENCE does not.

I'm not sure about the reasoning of "flavor of COBOL", but NEXT SENTENCE is
marked as an archaic element in the current ISO standard on the grounds that
scope delimiters and CONTINUE provide equivalent functionality without
falling into the trap that "most implementors" have fallen into!  See
ISO/IEC 1989:2002 Page 833, G.1, Archaic language elements, item 3, NEXT
SENTENCE phrase in IF and SEARCH statements.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-13T17:37:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4BD81A.130AADDE@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net>`

```
Naturally, your observations are based on the code I gave you. To illustrate the
'real' thing. I have a dialog with the left side of screen showing an input record
and the right side showing a listbox of existing records to select from, (sorted
collection). The default for the listbox is display in alphabetical name sequence
and the user can select by Pushbutton to show in PrimeKey sequence or another (when
appropriate). So :-

1. Class Dialog :-

*>--------------------------------------------------------
Method-id. "zCreatePushbutton".
*>--------------------------------------------------------
Local-storage section.
78 DefaultButtonID               value 1.
78 ExitButtonID                  value 55.
01 ls-event                      pic x(4) comp-5.
01 ls-object                     object reference.
Linkage section.
copy "dilogprm.new" replacing ==(tag)== by ==lnk==.

Procedure Division using lnk-Params.

move clicked to ls-event
invoke self "getObjectFromId"
   using lnk-ID returning ls-object

Evaluate true

  when lnk-id = DefaultButtonID  *> PB-OK
       etc..
  when lnk-id = 55   *> PB-Exit
       etc...
  when other
       invoke ls-object "setEventto" using
           ls-event, os-Caller, lnk-Methodname
End-Evaluate

*> above 'Caller' is the Edit Program and lnk-Methodname will contain
*> "PB-ByName", "PB-ByKey" or "PB-Other" for this example

End Method "zCreatePushbutton".
*>--------------------------------------------------------

2. Class - Edit Program

*>-------------------------------------------------
Method-id. "PB-ByName".
*>-------------------------------------------------
Procedure Division.

   if not Byname of ws-CollectionParams
      set ByName of ws-CollectionParams to true
      invoke self "initCollection"
   End-if

*> "initCollectiuon" picks up on the global setting for the Sequence Flag.

End Method "PB-ByName".
*>-------------------------------------------------

Same sort of code for both 'PB-ByKey" and "PB-ByOther"

- Hope that clarifies usage, as we don't have nested performs.

Jimmy, Calgary AB

Robert Wagner wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
> >Wanna get into semantics Mr. 'COBOL Best Practices' ? EXIT-PERFORM - No it's
…[61 more quoted lines elided]…
> Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-13T10:45:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302131045.65eed6f4@posting.google.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> The syntax is ambiguous. Suppose the program reads:
> 
…[8 more quoted lines elided]…
> Which perform does it exit, the inner or the outer?

Which part of the actual rules didn't you read ?  What part of 'the
END-PERFORM of the nearest in-line PERFORM' don't you understand ?

BTW it is 'EXIT PERFORM' not 'EXIT-PERFORM'.
 
> I still believe mainframe bozos .. 

>> "they should have at least offered cogent rebuttal rather than
attacking my character."
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-14T00:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4c39bb.63971098@news.optonline.net>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3e4b5056.4212514@news.optonline.net> <217e491a.0302131045.65eed6f4@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[15 more quoted lines elided]…
>BTW it is 'EXIT PERFORM' not 'EXIT-PERFORM'.

If you want to elevate your standing in this newsgroup, you'll have to do it by
helping others and generally acting positive. Disparaging my intelligence or
knowledge doesn't make YOU stand any taller. To the contrary, it makes you seem
crotchety. 

Your evening postings come through google.com, while your daytime postings come
through kc.net.nz. Do we have a Jekyll-Hyde dynamic going?

Feel free to answer privately if it suits you.

Robert
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-14T14:21:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2hgfa$ruq$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4b5056.4212514@news.optonline.net> <217e491a.0302131045.65eed6f4@posting.google.com> <3e4c39bb.63971098@news.optonline.net>`

```
Robert Wagner wrote:

>>> The syntax is ambiguous. Suppose the program reads:
>>> ...
 
> If you want to elevate your standing in this newsgroup, 

My postings are only rarely aimed at trying to inflate any standing that I 
may or may not have here, it is only no importance to me at all.

> you'll have to do it by helping others 

If I thought that you were a newbie having difficulty finding your way 
around then I may have posted the extract from the manual plus a useful 
explanation.  However, it seemed that you would have already read that and 
had formed a definitive conclusion: "The syntax _is_ ambiguous".

> To the contrary, it makes you seem crotchety.

Good, it is working then    ;-)

> Your evening postings come through google.com, while your daytime postings
> come through kc.net.nz. Do we have a Jekyll-Hyde dynamic going?

No, it just indicates flexibility.

And of course, it is summer here, and light when all else is dark.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 4)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-23T08:50:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E58FBB8.2060106@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca>`

```
James J. Gavan wrote:
> 
> Method-id. "byName".
…[10 more quoted lines elided]…
> 
Only if you allow fall-through to end of program, Jimmy.  ;).

You really should have an EXIT METHOD in there before the end method, 
though it will work that way.  Falling off the end of a program is not a 
good idea.

Donald
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-24T08:02:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3b5t2$bcc$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3E58FBB8.2060106@Sympatico.ca>`

```
Donald Tees wrote:

> You really should have an EXIT METHOD in there before the end method,
> though it will work that way.  Falling off the end of a program is not a
> good idea.

Implicit return at end of a procedure (or method) is common in many 
languages, such as C/C++.

Not only will it 'work that way' but the standard guarantees that it will 
work.  

Your 'should have' and 'good idea' are purely a matter of personal style, 
as is everything else that you argue about and try to impose on others.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-24T10:00:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3bcre$e42$1@aklobs.kc.net.nz>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3E58FBB8.2060106@Sympatico.ca> <b3b5t2$bcc$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> Donald Tees wrote:
> .....
> 
> as is everything else that you argue about and try to impose on others.

Oops, sorry, I unreservedly withdraw this, it was an overflow from writing 
to RW.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 7)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-23T23:21:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E59C810.4020204@Sympatico.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3E58FBB8.2060106@Sympatico.ca> <b3b5t2$bcc$1@aklobs.kc.net.nz> <b3bcre$e42$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> Richard Plinston wrote:
> 
…[10 more quoted lines elided]…
> 

<grin>

Well in that case.  You are quite right about the drop through being an 
implicit end, but to my mind laeving out the exit method (or the stop 
run), is a thousandfold worse habit than using too many periods.

All too often, some poor sucker comes along, and unwittingly places a 
new paragraph (where else) at the end of the program.

Donald
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-24T20:57:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5A8782.514199CE@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <3E4ADA79.D40C1A5C@shaw.ca> <3e4af28c.362743046@news.optonline.net> <3E4AFD92.BB79A030@shaw.ca> <3E58FBB8.2060106@Sympatico.ca>`

```


Donald Tees wrote:

> James J. Gavan wrote:
> >
…[18 more quoted lines elided]…
> Donald

Phew ! Saw Richard got snotty with you until he realized who he was responding to <G>.

It really is a question of style. As you well know I really LUV to leave out all that
extraneous stuff that M/F calls "red tape". I know that you have followed on with much
of the syntax into OO because you felt more comfortable with that, while I consider it
easier to read, (leaving out the extraneous) and I also think it tends to counter the
argument COBOL is verbose.

My own little set of 'house rules' - ***but note folks - purely in an OO context*** :-

- PERFORM - basically I'm using in-line performs but to get out quick EXIT PERFORM,
which either drops down to the next executable code or END METHOD.

- NOT very often, I perform PARAGRAPHS

Method-id "dosomething"

evaluate true
 when xx perform PARA-1
when yy perform PARA-2
when....
End-evaluate

... might be some more code here........

EXIT METHOD.

PARA-1
para1 code.....
.
PARA-2.
para2 code
.
End Method  "dosomething"
*>---------

Note that the EXIT METHOD above is ABSOLUTELY essential otherwise it will drop through
to the 'remaining code' and the subsequent paragraphs.(A la Laurel and Hardy, "This is
a fine mess you've got us into Stanley !" <G>)

I signal to myself by putting EXIT PERFORM and EXIT METHOD in uppercase.

Like you I'm much more comfortable with OO now so I don't like yet another line of
extraneous code - 'EXIT METHOD' - although it does no harm. However, it does have one
advantage, (in Net Express), like End-Perform, End-if, End-Evaluate etc.. I can pause
the Animator(Debugger) on EXIT METHOD to check results - You can't do that on END
METHOD - never tried it, but don't think the Animator would pause on END PROGRAM
either..

PS: Did you follow-up on your Dad's RAF(RCAF)  logbook ?

Jimmy, Calgary AB
```

#### ↳ Re: COBOL/DIALOGUE System

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-12T23:46:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2d2f0$f4583280$a88bf243@chottel>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```
move zeros to space-count
inspect name8 tallying space-count for all spaces
if space-count > zero
    display 'errormsg'
end-if

Eddie Veness <e.veness@blueyonder.co.uk> wrote in article
<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>...
> I am currently trying to edit a field which is filled by the user with 8
> digits alphanumeric. I have to prevent the user from being able to leave
a
> space anywhere within those eight digits and finally creat an error
message.
> The error message I can handle, I just can't get my head around
preventing
> spaces.  I thought at first sight, simple enough but this is getting the
> better of me. I have not been programming in COBOL for that long and I
would
> welcome any help.
> 
> 
>
```

#### ↳ Re: COBOL/DIALOGUE System

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-12T15:53:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2empc$29fn$1@si05.rsvl.unisys.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```
INSPECT field-name TALLYING numeric-item FOR ALL SPACES.
IF numeric-item IS GREATER THAN ZERO THEN PERFORM issue-error.

Is that what you had in mind?

There's a conflict in your description.  If the field is actually being
filled with eight NUMERIC digits, no sign (as implied by "those eight
digits"), and you've defined the field as PICTURE X(8), then I'd suggest a
REDEFINES with PICTURE 9(8) DISPLAY, and doing an IF numeric-redefinitioin
IS NOT NUMERIC to determine whether to issue the error.

      -Chuck Stevens

"Eddie Veness" <e.veness@blueyonder.co.uk> wrote in message
news:Wdz2a.904$I06.332@news-binary.blueyonder.co.uk...
> I am currently trying to edit a field which is filled by the user with 8
> digits alphanumeric. I have to prevent the user from being able to leave a
> space anywhere within those eight digits and finally creat an error
message.
> The error message I can handle, I just can't get my head around preventing
> spaces.  I thought at first sight, simple enough but this is getting the
> better of me. I have not been programming in COBOL for that long and I
would
> welcome any help.
>
>
```

#### ↳ Re: COBOL/DIALOGUE System

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-12T19:02:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ldB2a.2363$3g1.283404@news20.bellglobal.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```
If it's Dialog System, just define the field as 9(8).  Open your screenset,
double-click on the entry field (or choose properties) and enter 9(8) in the
picture string.

If it's more than this, it's not DS :-)

Calin, TORONTO

"Eddie Veness" <e.veness@blueyonder.co.uk> wrote in message
news:Wdz2a.904$I06.332@news-binary.blueyonder.co.uk...
> I am currently trying to edit a field which is filled by the user with 8
> digits alphanumeric. I have to prevent the user from being able to leave a
> space anywhere within those eight digits and finally creat an error
message.
> The error message I can handle, I just can't get my head around preventing
> spaces.  I thought at first sight, simple enough but this is getting the
> better of me. I have not been programming in COBOL for that long and I
would
> welcome any help.
>
>
```

#### ↳ Re: COBOL/DIALOGUE System

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-13T08:26:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0Odnau-V_LBNtajXTWckA@giganews.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk>`

```

"Eddie Veness" <e.veness@blueyonder.co.uk> wrote in message
news:Wdz2a.904$I06.332@news-binary.blueyonder.co.uk...
> I am currently trying to edit a field which is filled by the user with 8
> digits alphanumeric. I have to prevent the user from being able to leave a
> space anywhere within those eight digits and finally creat an error
message.
> The error message I can handle, I just can't get my head around preventing
> spaces.  I thought at first sight, simple enough but this is getting the
> better of me. I have not been programming in COBOL for that long and I
would
> welcome any help.

It's worse than you might think.

The user leaves field A, triggering some kind of lost-focus event. Your code
takes over.

You can check the user's input manually and, if not correct, put him back in
field A until he gets it right.

Cool. Now here's the tricky part:

The user, in leaving the field, goes directly (via a mouse click, say) to
another field, B. The contents of field B depend on the correct value in
field A (say Field A is the customer number and field B is the customer
name).

The got-focus event for field B triggers before the lost-focus for field A.

Immediately upon entering field B, the program uses the value from field A
to do something (like look up the customer's name). If field A is wrong,
BOOM!

We use Fujitsu's PowerCOBOL and this sequence drives us nuts.

Here's one circumvention.

First statement in got-focus event for "A"
   Move 'N' to ALLOW-FOCUS.

Lost-focus event for "A"
   (after passing all validity checks)
   Move "Y" to ALLOW-FOCUS

1st statement in Got-focus event for "B"
   If ALLOW-FOCUS = "N"
       Exit-program.
   (which should get the lost-focus event for "A" as next-from-queue)

What's needed (I'm told) is a robust VALIDATE method as in VB.
```

##### ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** B Berman <bberman@netbox.com>
- **Date:** 2003-02-13T16:20:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4BC673.C8AE7549@netbox.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <a0Odnau-V_LBNtajXTWckA@giganews.com>`

```
JerryMouse wrote:

> It's worse than you might think.
>
…[35 more quoted lines elided]…
> What's needed (I'm told) is a robust VALIDATE method as in VB.

If there is a 'KeyPress' event, as in VB, you can check each digit entered as
the user enters them, and never leave (lose focus) the text box field.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-13T18:26:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2e-dnbMYHqHupdGjXTWcjQ@giganews.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <a0Odnau-V_LBNtajXTWckA@giganews.com> <3E4BC673.C8AE7549@netbox.com>`

```

"B Berman" <bberman@netbox.com> wrote in message
news:3E4BC673.C8AE7549@netbox.com...
> JerryMouse wrote:
>
> > It's worse than you might think.
> >
> > The user leaves field A, triggering some kind of lost-focus event. Your
code
> > takes over.
> >
> > You can check the user's input manually and, if not correct, put him
back in
> > field A until he gets it right.
> >
> > Cool. Now here's the tricky part:
> >
> > The user, in leaving the field, goes directly (via a mouse click, say)
to
> > another field, B. The contents of field B depend on the correct value in
> > field A (say Field A is the customer number and field B is the customer
> > name).
> >
> > The got-focus event for field B triggers before the lost-focus for field
A.
> >
> > Immediately upon entering field B, the program uses the value from field
A
> > to do something (like look up the customer's name). If field A is wrong,
> > BOOM!
…[19 more quoted lines elided]…
> If there is a 'KeyPress' event, as in VB, you can check each digit entered
as
> the user enters them, and never leave (lose focus) the text box field.

Yeah, we use that technique sometimes. In the above scenario, the technique
fails when the user has to enter, say, a five-digit customer number, enters
only 3 digits, then clicks the "Exit" button. That is, customer number lost
focus gets control, determines the customer number is bad, produces warning
message, and sets the focus back to the customer number field. The Exit
event fires. Moan.
```

###### ↳ ↳ ↳ Re: COBOL/DIALOGUE System

_(reply depth: 4)_

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-14T09:39:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K973a.4887$606.1035526@news20.bellglobal.com>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <a0Odnau-V_LBNtajXTWckA@giganews.com> <3E4BC673.C8AE7549@netbox.com> <2e-dnbMYHqHupdGjXTWcjQ@giganews.com>`

```
That's why you need a cancel button.  User clicks, you don't validate but
ask the user "sure you wish to do that?" and then go quietly.  :-)

Normally in the lost focus routine you check if the gain focus was on the
cancel button and act accordingly (i.e. don't validate).

Calin, TORONTO


"JerryMouse" <nospam@bisusa.com> wrote in message
news:2e-dnbMYHqHupdGjXTWcjQ@giganews.com...
>
> "B Berman" <bberman@netbox.com> wrote in message
…[5 more quoted lines elided]…
> > > The user leaves field A, triggering some kind of lost-focus event.
Your
> code
> > > takes over.
…[9 more quoted lines elided]…
> > > another field, B. The contents of field B depend on the correct value
in
> > > field A (say Field A is the customer number and field B is the
customer
> > > name).
> > >
> > > The got-focus event for field B triggers before the lost-focus for
field
> A.
> > >
> > > Immediately upon entering field B, the program uses the value from
field
> A
> > > to do something (like look up the customer's name). If field A is
wrong,
> > > BOOM!
> > >
…[18 more quoted lines elided]…
> > If there is a 'KeyPress' event, as in VB, you can check each digit
entered
> as
> > the user enters them, and never leave (lose focus) the text box field.
>
> Yeah, we use that technique sometimes. In the above scenario, the
technique
> fails when the user has to enter, say, a five-digit customer number,
enters
> only 3 digits, then clicks the "Exit" button. That is, customer number
lost
> focus gets control, determines the customer number is bad, produces
warning
> message, and sets the focus back to the customer number field. The Exit
> event fires. Moan.
>
>
```

##### ↳ ↳ Re: COBOL/DIALOGUE System

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-13T23:33:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4C2B7C.3A8C309@shaw.ca>`
- **References:** `<Wdz2a.904$I06.332@news-binary.blueyonder.co.uk> <a0Odnau-V_LBNtajXTWckA@giganews.com>`

```


JerryMouse wrote:

> "Eddie Veness" <e.veness@blueyonder.co.uk> wrote in message
> news:Wdz2a.904$I06.332@news-binary.blueyonder.co.uk...
…[11 more quoted lines elided]…
>

Are you trying to scare him to death Jerry :-) He did say he was a 'beginner'.
Hopefully he's OK. I'm not familiar with Dialog System (Pete and Thane both
Fujitsu users know more about Dialog System than I'll ever know - or want to
know !). For  each control the DS system allows him to add in-line code to do
his validity checks. If that's not clear then Calin can jump in and expand.

>
> The user leaves field A, triggering some kind of lost-focus event. Your code
…[34 more quoted lines elided]…
> What's needed (I'm told) is a robust VALIDATE method as in VB.

I agree with you gained focus, lost focus and the Event Loop are a real pig,
depending upon what you are trying to do. For the following reasons I use both
'gain' and 'lost' events :-

- Gain Focus - I find it most irritating to backspace to 'clear' an existing
field; so I have two options.  (1) 'clear' or 'setEmpty' object - accepts fresh
input from user. From memory that is the way it works with COBOL Screen
Section.  (2) Insert mode - don't clear the field, say for SIN, VAT, GST and any
other big numbers. Allow the user to 'insert' new characters as appropriate.

- Lost Focus (1) Do I want to return directly to Business Logic now - user has
entered a new PrimeKey - so check it exists and either display or accept input
for new record. (2) For convenience (some 70% of the application's input) is
decimal inches/cms - 9.999 or 99.999 - which are entered as integers - on lost
focus redisplay with decimal point. (3) Third possibility - user clicks on a
checkbox or radio button - this gives two options (a) Retain value selected
until PB-OK entered or (b) must return the check box/radio button value NOW as
Business Logic may determine that additional controls (currently hidden) now
need to be 'activated' with set enable and show.

I  have real fun using both 'gained' and 'lost'.  For your ALLOW-FOCUS flag I
utilize methods "accessSystemEvents" and "cancelAccessToSystemEvents" for the
next object(control).

I try to stay within the logic of the Dialog - such as redisplaying decimal
numbers, and same applies to dates where user enters for YYMM a value of '1' -
then I will re-display as 'Jan 2001'. Kind of goes against the grain but for the
most part I'm currently opting for validating input when user enters PB-OK which
triggers the return to the Business class.

I wouldn't claim my approach is the simplest - but with a lot of buggering
around it works !

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
