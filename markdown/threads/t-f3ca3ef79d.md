[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Replace GO TO w/perform Question

_18 messages · 13 participants · 1999-01 → 1999-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Replace GO TO w/perform Question

- **From:** codetrader@aol.com (Codetrader)
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
Hi-

Q. What would be an effective way to replace this  GO TO with a PERFORM ?
     My snag is that the GO TO in this example ends this section.  I have
     seen examples where you PERFORM somethig, but if you pass the test
     (IF) and a GO TO then ends the section, how could a perform or logic
     change allow for the next test, and/or the MOVE that follows the first
test?
     I am not allowed to use GO TO.
Thanks in advance
    - Jake


example: 
PROCEDURE DIVISION.

PERFORM 100-VALIDATE-THIS-DATA THRU DATA-VALIDATED.

100-VALIDATE-THIS-DATA.
      IF THIS-PIECE IS ALPHABETIC
      GO TO 100-DATA VALIDATED.
      MOVE ...........
      IF THIS-PIECE IS NUMERIC
       MOVE THIS PIECE TO VLD-PIECE.
100-DATA VALIDATED.
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1999-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.110fb1c31c9b405b98968e@news.earthlink.net>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
In article <19990121041129.04344.00000491@ng-
fc1.aol.com>, codetrader@aol.com says...
<Snip>

Hi Jake,

    I agree with Judson's answer to this question. It 
seems that the best way to approach this is to make use 
of a GO TO statement and transfer control to the end of 
the section of code. 

    In many cases you will have multiple edits to 
perform on a particular data item and the "best" way to 
attack it is to locate all of the edits in one section 
of code and perform each test one at a time. When one of 
them fails use a GO TO and get out of that section of 
logic. 

     While use of a GO TO can lead to some problems it 
is a very acceptable way to code large sections of logic 
and not fragment them into dozens of small pieces that 
become hard to related at a later date. 

     Just my 2 cents on the topic since you can't use a 
GO TO in you program you will need to break up the logic 
into small paragraphs and/or use some other method to 
get around the use of a GO TO.

Jeff



> example: 
> PROCEDURE DIVISION.
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TMFp2.50$jE1.40956@news4.mia>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
Jake,

I triggered a *long* thread on this several months ago.  There are three
general approaches to removing the GO TO in your example.  1. Move the
remainder of the paragraph into a separate paragraph and perform it in
the inverse of the GO TO conditional.  2. Set some kind of 'error flag'
and test it in every following statement in the paragraph.  3. In COBOL
85 you can embed the remainder of the paragraph between ELSE/END IF.

To my thinking, neither of these alternatives is to be desired.  The
first approach would mecessitate breaking a large, contiguous paragraph
up into many smaller ones in cases where there were a number of such
GO TO's.  The second approach adds a host of otherwize unnessary 'IF'
tests in the remainder of the paragraph, unduly obfuscating the logic
in the process.  The third method works fine for small paragraphs, but
breaks down into deeply nested, obfuscated code on long paragraphs with
many such points.  The proposed standard will have the EXIT PARAGRAPH
statement, which does the same thing without the GO TO or exit paragraph,
making this question a moot point.  Until then, I much prefer the simple
use of PERFORM ... THRU ...-EXIT, and GO TO ...-EXIT to the slavish
avoidance of GO TO at all costs, under any circumstances.  In my opinion,
the only real disadvantage of a GO TO ...-EXIT as used here is that it
presents an opportunity for a programming error when a GO TO is made
to a paragraph other than the proper exit.  Personally, I use a simple
code checked to eliminate this possibility.  After all, the EXIT
PARAGRAPH statement is effectively a GO TO which can only be to the
paragraph exit; identical in function, use and limitations to GO TO
...-EXIT when used with the code checker.

Get braced, for you will no doubt receive a flurry of rebuttals to my
position. :-)
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** Albert Ratzlaff <albert@conexion.com.py>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A8454D.2B270AEF@conexion.com.py>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <TMFp2.50$jE1.40956@news4.mia>`

```
Judson McClendon wrote:

> Get braced, for you will no doubt receive a flurry of rebuttals to my
> position. :-)

Here's the first!
(just kidding :-)

I have in my hands a copy of "Writings of the Revolution - Selected Readings on
Software Engineering", edited by Edward Jourdon. It contains "Notes on Avoiding
GO TO Statements", by Knuth and Floyd. The general spirit of the paper, as I
understand it, is to not concentrate on avoiding GO TOs, but on coding in the
most clear and efficient way. If you can do that better by using GO TO, then by
all means, do it.

There are some interesting examples in the paper - and you all know how thorough
Knuth is when he writes something!

Regards
Albert Ratzlaff
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ObdG2OpS#GA.172@upnetnews03>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <TMFp2.50$jE1.40956@news4.mia>`

```

Judson McClendon wrote in message ...
>Jake,
>
…[28 more quoted lines elided]…
>position. :-)


Not from me!  Judicious use of GO TO, restricted as you have outlined, is
IMHO preferable to most of the alternatives.  I believe GO TO should be used
ONLY to exit a paragraph invoked in a PERFORM paragraph-name THRU
paragraph-name-exit construct, where paragraph-name-exit contains only EXIT.
Even this usage will be obviated upon the adoption of the EXIT-PARAGRAPH
construct in the COBOL Standard of the next millennium.

>Judson McClendon      judmc123@bellsouth.net  (remove numbers)
>Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
…[9 more quoted lines elided]…
>>     change allow for the next test, and/or the MOVE that follows the
first
>>test?
>>     I am not allowed to use GO TO.
…[18 more quoted lines elided]…
>
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A73A76.D8CFE823@home.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
The way to avoid using GO TO is to design your program properly to begin
with.  However, sometimes we are given code designed for GO TO and told
to remove the GO TO's.  See below.

Codetrader wrote:
> 
> Hi-
…[22 more quoted lines elided]…
> 100-DATA VALIDATED.

The easiest solution (not the best one - the best one is more of a
rewrite) is to do the following:
> 100-VALIDATE-THIS-DATA.
>       IF THIS-PIECE IS not ALPHABETIC
            perform 110-continue validation.

  110-continue-validation.
>***    GO TO 100-DATA VALIDATED.
>       MOVE ...........
>       IF THIS-PIECE IS NUMERIC
>        MOVE THIS PIECE TO VLD-PIECE.
> 100-DATA VALIDATED.
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A856C8.25B6F6D9@IMN.nl>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36A73A76.D8CFE823@home.com>`

```
Howard Brazee wrote:

> Codetrader wrote:
> > PERFORM 100-VALIDATE-THIS-DATA THRU DATA-VALIDATED.
…[20 more quoted lines elided]…
> > 100-DATA VALIDATED.

But then the perform should also be changed and become:
    PERFORM 100-VALIDATE-THIS-DATA
in other words: the THRU-part is left off, otherwise the 110-continue-validation
would always be executed, once for alphabetic and twice for non-alphabetic
this-pieces.

The Frog
```

###### ↳ ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A891D8.4D31A73@home.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36A73A76.D8CFE823@home.com> <36A856C8.25B6F6D9@IMN.nl>`

```
> But then the perform should also be changed and become:
>     PERFORM 100-VALIDATE-THIS-DATA
> in other words: the THRU-part is left off, otherwise the 110-continue-validation
> would always be executed, once for alphabetic and twice for non-alphabetic
> this-pieces.

Right.  If I had my way, Procedure division sections and the word THRU
would go the way of ALTER.  Too many maintenance problems.  Let each
perform do a single function.
```

###### ↳ ↳ ↳ Re: Replace GO TO w/perform Question

_(reply depth: 4)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A8CE26.D58791D9@IMN.nl>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36A73A76.D8CFE823@home.com> <36A856C8.25B6F6D9@IMN.nl> <36A891D8.4D31A73@home.com>`

```
Howard Brazee wrote:

> Right.  If I had my way, Procedure division sections and the word THRU
> would go the way of ALTER.  Too many maintenance problems.  Let each
> perform do a single function.

My idea.

Frog
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<787jgf$npj$1@nnrp1.dejanews.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
In article <19990121041129.04344.00000491@ng-fc1.aol.com>,
  codetrader@aol.com (Codetrader) wrote:
> Hi-
>
> Q. What would be an effective way to replace this  GO TO with a PERFORM ?
<snip>
> example:
> PROCEDURE DIVISION.
…[10 more quoted lines elided]…
>

I would code this little piece of code the following way:

 PERFORM 100-VALIDATE-THIS-DATA
 IF ERROR-FLAG = 'S' OR ERROR-FLAG = 'E'
  THEN PERFORM 999-ERROR
 END-IF

 100-VALIDATE-THIS-DATA SECTION.
       IF THIS-PIECE IS ALPHABETIC
        THEN
         MOVE ...........
        ELSE
         IF THIS-PIECE IS NUMERIC
          THEN
           MOVE THIS-PIECE TO VLD-PIECE
          ELSE
           MOVE 'S' TO ERROR-FLAG
           MOVE 'INVALID DATA IN THIS-PIECE' TO ERROR-DIAGNOSTIC
         END-IF
       END-IF
      .

Or maybe I would use the EVALUATE-Statement in this case (only the section
part):

 100-VALIDATE-THIS-DATA SECTION.
      EVALUATE TRUE
       WHEN THIS-PIECE IS ALPHABETIC
         MOVE ...........
       WHEN THIS-PIECE IS NUMERIC
         MOVE THIS PIECE TO VLD-PIECE
       WHEN OTHER
         MOVE 'S' TO ERROR-FLAG
         MOVE 'INVALID DATA IN THIS-PIECE' TO ERROR-DIAGNOSTIC
      END-EVALUATE
      .
Daniel


-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a795ab.11233535@netnews>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <787jgf$npj$1@nnrp1.dejanews.com>`

```
'Twas Thu, 21 Jan 1999 16:10:01 GMT, when daniel.jacot@winterthur.ch
illuminated comp.lang.cobol thusly:

> 100-VALIDATE-THIS-DATA SECTION.
>       IF THIS-PIECE IS ALPHABETIC

In Cobol-85 you need a paragraph header between the section header and a
statement.  This requirement is relaxed in the next standard.

Ramaniuk had the best answer to the original question.
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A76372.7893@zag.si>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
Codetrader wrote:
> example:
> PROCEDURE DIVISION.
…[9 more quoted lines elided]…
> 100-DATA VALIDATED.

  *%%%%%%%%%%%%%%%%%%%%%%% 
   100-VALIDATE-THIS-DATA.
  *%%%%%%%%%%%%%%%%%%%%%%% 
       IF THIS-PIECE NOT ALPHABETIC
          MOVE .....
          IF THIS-PIECE IS NUMERIC
             MOVE THIS-PIECE TO VLD-PIECE
          END-IF
       END-IF
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** corky <corky@compuserve.com>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A8E751.C7ACF9E5@compuserve.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
Codetrader wrote:
> 
> Hi-
…[22 more quoted lines elided]…
> 100-DATA VALIDATED.

no body is going to like this but why bother, if it works etc..
```

#### ↳ Re: Replace GO TO w/perform Question

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1999-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ad1c46.1027042@nntp.ix.netcom.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com>`

```
On 21 Jan 1999 09:11:29 GMT, codetrader@aol.com (Codetrader) wrote:


>PERFORM 100-VALIDATE-THIS-DATA THRU DATA-VALIDATED.

>100-VALIDATE-THIS-DATA.
>      IF THIS-PIECE IS ALPHABETIC
…[4 more quoted lines elided]…
>100-DATA VALIDATED.

hmm.

how about

if this-piece is numeric
move this piece to vld-piece

since alphabetic and other are the only fall throughs, he only real
check you have to do is for numeric



gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ac047b.4796160@nntp.ix.netcom.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36ad1c46.1027042@nntp.ix.netcom.com>`

```
On Sat, 23 Jan 1999 19:02:35 GMT, gvwmoore@ix.netcom.com (G Moore)
wrote:

>
>
…[4 more quoted lines elided]…
>check you have to do is for numeric

I missed a part about the MOVE...


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#oTr6apS#GA.91@upnetnews03>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36ad1c46.1027042@nntp.ix.netcom.com>`

```

G Moore wrote in message <36ad1c46.1027042@nntp.ix.netcom.com>...
>On 21 Jan 1999 09:11:29 GMT, codetrader@aol.com (Codetrader) wrote:
>
…[21 more quoted lines elided]…
>gvwmoore@ix.spam.netcom.com to reply remove the spam

Was this "how about ... " that you've offered here without careful
consideration of all the facts anything like the "suggestions" on
programming practices that you have offered to prospective employers? The
sage advice (AFAIK attributed to Abe Lincoln) "It is better to remain silent
and be thought a fool than to open your mouth and dispel all doubt" may have
specific applicability to your employability.

Dennis Minette
CCCO
```

###### ↳ ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b1a48b.941030@nntp.ix.netcom.com>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36ad1c46.1027042@nntp.ix.netcom.com> <#oTr6apS#GA.91@upnetnews03>`

```
On Thu, 28 Jan 1999 03:17:42 -0500, "Dennis J. Minette"
<dennis_minette@email.msn.com> wrote:

>>>PERFORM 100-VALIDATE-THIS-DATA THRU DATA-VALIDATED.

>>>100-VALIDATE-THIS-DATA.
>>>      IF THIS-PIECE IS ALPHABETIC
…[23 more quoted lines elided]…
>specific applicability to your employability.

I sent a cancel usenet message, so you sjhouldn't have even recieved
the above message. Us programmers constantly improve code. By the way,
who are you?


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

###### ↳ ↳ ↳ Re: Replace GO TO w/perform Question

- **From:** "Topcoder" <no@spam.com>
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798m2n$pra@bgtnsc02.worldnet.att.net>`
- **References:** `<19990121041129.04344.00000491@ng-fc1.aol.com> <36ad1c46.1027042@nntp.ix.netcom.com> <#oTr6apS#GA.91@upnetnews03>`

```

Dennis J. Minette wrote in message
<#oTr6apS#GA.91@upnetnews03>...
>
<snip>
>Was this "how about ... " that you've offered here without
careful
>consideration of all the facts anything like the
"suggestions" on
>programming practices that you have offered to prospective
employers? The
>sage advice (AFAIK attributed to Abe Lincoln) "It is better
to remain silent
>and be thought a fool than to open your mouth and dispel
all doubt" may have
>specific applicability to your employability.
>
>Dennis Minette
>CCCO

After 'careful consideration of all the facts',
I said the hell with it and decided to wing it', so...

"It is better to remain silent and be thought
a fool than to speak up and remove all doubt."    Mark Twain
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
