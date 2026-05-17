[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GO TO less purists, how would you do this?

_45 messages · 19 participants · 1997-10 → 1997-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

I have been observing with interest the debates going on in this newsgroup
over PERFORM ... THRU and using GO TO. Many years ago, when I was first
exposed to structured design and programming, I was so impressed with all
the benefits that I became a GO TO less zealot myself, and refused to use
GO TO under any circumstances. After a while (this was before COBOL 85 and
the END-xxx statements were available) I realized that I was having to
write some unwieldy sentences and create many more paragraphs than seemed
prudent. Avoiding GO TO entirely was NOT improving readability and was
taking much more time to code. Following Yordon's guidelines of every code
block having one entry point and one exit point, I began to code every
paragraph XXXX with an XXXX-EXIT, and use PERFORM ... THRU, allowing GOTO
only to the top or bottom of the paragraph. That allowed early exit from
the code block on error and other conditions, and I wrote a program to scan
COBOL source and flag violations. Now, even with COBOL 85's new
constructs, there are situations which I frequently encounter that simply
demand a GO TO exit.

Below is a very typical actual example from a program I recently wrote.
This routine tests every field received from an online transaction screen
to see if a flag was entered to get online help for that field. A similar
routine is used to actually validate each field, exiting on the first
error. This program had to conform to COBOL 74, but even if I could have
written it in COBOL 80, I don't see any way to make it more clear and
readable. I would like to see how you GO TO less purists would have me
code something like this. If you think to avoid GO TO completely here,
consider this. If you expect to avoid GO TO by using IF ... ELSE IF ...
ELSE IF ..., this sample only has about 50 fields, but you can easily have
over 100. How many levels of IF nesting can your compiler handle, or mine?
Probably 10, maybe 50, but very unlikely the 150-200 you would need
sometimes, because I've tried it. Also, to split this into more than one
paragraph to get by a compiler limit would be completely artificial and a
kludge; there is no logical grouping which would support that.

Is it not fair to say that, either there is a clean way to write paragraphs
like this without GO TO EXIT, or it is unreasonable to expect complete
elimination of GO TO EXIT and PERFORM THRU EXIT? So, show me a clean way
to do this without GO TO and PERFORM THRU, and without breaking up the
paragraph artificially or potentially exceeding the compiler's IF nesting
limit. Use any ANSI standard COBOL 85 construct you like. If you can do
it, you will certainly have my kudos.

As an aside, this type of construct is very useful, because the syntax is
so regular that I have a BASIC program which generates the code from a text
file of the data names. The field edits are dictionary based, and I
generate them simultaneously from the same BASIC program. This technique
greatly speeds coding and reduces errors significantly. Using this
technique, I have coded as many as 18 screen inquiry/updates in one day,
with very few errors. Writing one to three a week is probably typical for
most programmers.
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-10-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

For brevity I have snipped most of a very long article. Please
consult the original as needed for context.

Judson D. McClendon wrote:

[snip]

› Below is a very typical actual example from a program I recently wrote.
› This routine tests every field received from an online transaction screen
› to see if a flag was entered to get online help for that field.  A similar
› routine is used to actually validate each field, exiting on the first
› error.  
 
› [snip]
 
› So, show me a clean way
› to do this without GO TO and PERFORM THRU, and without breaking up the
…[6 more quoted lines elided]…
› file of the data names. 
 
› [snip]
 
› 
›            PERFORM 010500-FIND-HELP
…[28 more quoted lines elided]…
›                GO TO 010500-EXIT.
 
› [snip; many more in the same vein]
 
›            MOVE "O1XX-NXT-SCR"  TO HL-DATA-NAME.
›            MOVE RECV-01-NXT-SCR TO HL-DATA-VALUE.
…[8 more quoted lines elided]…
›            EXIT.

At least in a formal sense this code is easy to rewrite:

PERFORM 010500-FIND-HELP.
IF (HL-HELP-SENT-FLAG = 1)
...

010500-FIND-HELP.
*
MOVE 0 TO HL-HELP-SENT-FLAG.
MOVE 0 TO SEND-TAB-COUNT.
*
MOVE "O101-ACTION" TO HL-DATA-NAME.
MOVE RECV-01-ACTION TO HL-DATA-VALUE.
PERFORM 002500-TEST-HELP
THRU 002500-EXIT.
*
IF (HL-HELP-SENT-FLAG NOT = 1)
MOVE "O1XX-TEL-NBR" TO HL-DATA-NAME
MOVE RECV-01-TEL-NBR TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT.
*
IF (HL-HELP-SENT-FLAG NOT = 1)
MOVE "O1XX-QQQ-NBR" TO HL-DATA-NAME
MOVE RECV-01-TAG-NBR TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT.

[snip; many more in the same vein]

IF (HL-HELP-SENT-FLAG NOT = 1)
MOVE "O1XX-NXT-SCR" TO HL-DATA-NAME
MOVE RECV-01-NXT-SCR TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT.
*
IF (HL-HELP-SENT-FLAG NOT = 1)
MOVE 0 TO SEND-TAB-COUNT.
*

No GO TO, no PERFORM THRU (of this paragraph at least; I retained
the others), no EXIT, no artificial fragmentation, no compiler limits
exceeded, not even any COBOL 85 constructs needed. Apart from any
typos I may have committed, this solution meets all the criteria you
defined (you didn't define 'clean'). Furthermore, I expect it would
lend itself equally well to the kind of automatic code generation you
described.

In fact, this solution is so obvious that I suspect you have some
unstated reason for not liking it.

Perhaps you are concerned about efficiency. If HL-HELP-SENT-FLAG
ever equals 1, we will find ourselves testing the same flag
repeatedly, all the way to the bottom. However, this problem arises
only when the user asks for field-level help. Most applications can
afford to waste a microsecond every once in a while.

In other contexts efficiency may be a more serious consideration. I
have always been willing to tolerate a well-placed GO TO when it was
*demonstrably* necessary for performance reasons. In my own work
performance has never been that great a concern, so I am probably
less sensitive to performance issues than some other people.

In still other contexts, where the code is not so repetitive and
stereotyped, it can indeed be awkward to code an early exit. In
such a case I would dearly love to have some kind of EXIT PARAGRAPH
syntax. It would have the same effect as a typical well-formed
GO TO EXIT, but it would be guaranteed to have a restricted scope.

Meanwhile I am content to code an occasional nested IF, or stash
some code in a separate paragraph. Sometimes the awkwardness I
struggle with tells me that I'm not coding at the right level of
abstraction, and a separate paragraph is appropriate rather than
artificial.

GO TO is also more tolerable in code which is machine-generated.
In that case you don't maintain the generated code, where the GO TOs
live, but the input to the code generator.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p2@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p2@usenetarchives.gap>`

```

Michael C. Kasten wrote:
› 
› Judson D. McClendon wrote:
…[95 more quoted lines elided]…
› described.
 
› No, I didn't define 'clean'.  It's often pretty subjective I suppose.
 
› In fact, this solution is so obvious that I suspect you have some
› unstated reason for not liking it.

Yes, I am aware of this technique, but it doesn't meet my personal
definition of 'clean'. The advantage of structured design is that you are
expressing logic in a more economical, organized and clear manner, with
fewer chances for error. When you have to code hundreds (30
screens/program * 50 fields/screen = 1500 additional IF tests) of
additional logical statements to achieve this, you are working to
cross-purposes. I might accept this penalty for my example, but in
practice there can be many reasons for early exit from a long paragraph,
often involving some complex logic test. It would be impractical to repeat
those tests for every following statement, so you would need to create a
flag of some sort strictly for the purpose, and this seems kind of a
kludge.

› Perhaps you are concerned about efficiency.  If HL-HELP-SENT-FLAG
› ever equals 1, we will find ourselves testing the same flag
› repeatedly, all the way to the bottom.  However, this problem arises
› only when the user asks for field-level help.  Most applications can
› afford to waste a microsecond every once in a while.

I wouldn't be too concerned with execution time (help is only requested
occasionally) or the amount compiler generated code, but since it is extra
source code, it is more people time consuming. For this example I do
generate the code automatically, but there are other types of paragraph
where that isn't practical. And you wouldn't generate code every time you
added two or three fields later. People time is what we want to conserve.

› In still other contexts, where the code is not so repetitive and
› stereotyped, it can indeed be awkward to code an early exit.  In
› such a case I would dearly love to have some kind of EXIT PARAGRAPH
› syntax.  It would have the same effect as a typical well-formed
› GO TO EXIT, but it would be guaranteed to have a restricted scope.

This construct gives me exactly what you describe. Remember, I enforce
compliance by using a program which detects violations and guarantees the
restricted scope.

But here is the real kicker: The primary reason PERFORM is superior to GO
TO is that when you see it, you know immediately that the logic is going to
do something and then come right back. You don't have to trace through
reams of GO TO logic to find that out. Your apprehension of the logic is
vastly quicker. In this case, the GO TO is actually superior to the
multiple IFs, because when you see the GO TO EXIT, you know for certain
that the paragraph is finished. With all the IF statements, you have to
actually examine each one to be sure there isn't some logic coded below,
which might escape your notice. And it would be really easy with 100-150
repetitions of the same IF to miss one that was slightly different. And
you can't easily automate enforcement of that.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "mark miller" <ua-author-584162@usenetarchives.gap>
- **Date:** 1997-10-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

Judson D. McClendon wrote:

SNIP
› 
› Below is a very typical actual example from a program I recently wrote.
…[6 more quoted lines elided]…
› code something like this. 
 
 
› 
›            PERFORM 010500-FIND-HELP
…[21 more quoted lines elided]…
›                GO TO 010500-EXIT.

010500-exit
SNIP

Try this.

Define HL-HELP-SENT-FLAG as 88 LEVEL.

PERFORM 010500-FIND-HELP
UNTIL HL-HELP-SENT-FLAG

010500-FIND-HELP.
MOVE "O101-ACTION" TO HL-DATA-NAME.
› MOVE RECV-01-ACTION TO HL-DATA-VALUE.
› PERFORM 002500-TEST-HELP
(within this paragraph set the help flag to true if flag
entered in help field
IE. "SET HL-HELP-SENT-FLAG TO TRUE")

›       *
›            MOVE "O1XX-TEL-NBR"  TO HL-DATA-NAME.
›            MOVE RECV-01-TEL-NBR TO HL-DATA-VALUE.
›            PERFORM 002500-TEST-HELP
(within this paragraph set the help flag to true if
flag entered in help field
IE. "SET HL-HELP-SENT-FLAG TO TRUE")

The same applies to all the other field validation checks. The program
drops out of 010500-FIND-HELP as soon as flag condition is satisfied.
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p4@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap>`

```

Mark Miller wrote:
› Judson D. McClendon wrote:
›› Below is a very typical actual example from a program I recently wrote.
…[62 more quoted lines elided]…
› drops out of 010500-FIND-HELP as soon as flag condition is satisfied.

Mark, I like this approach, and have used it at times in other situations.
There's definitely a performance penalty, because you actually PERFORM and
EXIT for every following field after a help flag is detected, but the logic
is clean. It would work fine for my example (kudos for that), but not as
well for other situations like this below.

When presented with 50 or so fields input from a terminal screen, we first
test for help using code like my example. Then we edit, or validate, the
data which is a two step process for simplicity. First, we validate all
the fields with generated dictionary based edits which check for numeric,
alpha, valid codes, etc. This is done in a paragraph very similar to the
help code example. Then we do logical validation of the fields, testing
things like "is this valid with that?", "can this person modify that
field?", "does this screen balance?" etc. These edits are coded inline,
except where it makes sense to separate a loop or complex edit into another
paragraph. Often there comes a point when you want to exit and skip the
rest of the edits (e.g. you are doing a function for which the rest of the
fields are irrelevant). There may be a number points where this happens,
and the logical tests to determine this condition might be complex.
Sometimes it makes sense to code the rest of the edits as a separate
paragraph, sometimes not. You could set a 'drop through' flag, but you
would have to be constantly testing it, because the edits often involve a
series of IF statements, database reads, etc. To my mind, it just seems
very clean and economical in these cases to code a GO TO EXIT. Clarity is
maintained, efficiency is maintained, structured design is maintained (one
entry, one exit, no exceptions), and you can enforce compliance with a
program which scans for violations. It just seems to me that total
elimination of GO TO is like trying to eliminate all fat from your diet.
Just because unrestricted use is bad, doesn't mean ANY use is bad, and
carefully controlled use may in fact be beneficial. And no use at all even
harmful? 8-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-10-22T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p5@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p5@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› --lots of superfluosity snipped (if superfluosity is in fact a real word)--
…[13 more quoted lines elided]…
› and the logical tests to determine this condition might be complex.

Judson,
You've made some very valid points about editing, specifically, one should not
necessarily stop editing as soon as the first error is encountered.
Case in point: Your DFHMDF's are NOT defined with FSET, and the user enters data
on multiple fields before pressing a PF key. You start editing the fields,
saving the data as you go, then you find one that's not valid so you stop, set a
message, move -1 to the invalid field's length, and send the map. The next time
you do a receive map, the remaining fields which you haven't edited or saved
will not be sent back from the terminal.
This is only one way to process a map, but it's the method I usually use, and
the code would look something like this:


validation-paragraph.

move 'y' to data-valid-flag.
move spaces to error-message.

if field-1 modified
validate field-1
if field-1 valid
move green to field-1C
save field-1 someplace
else
move red to field-1C
move -1 to field-1L
if data-valid-flag = 'y'
move 'n' to data-valid-flag
move 'Field 1 is not valid' to error-message.

if field-2 modified
validate field-2
if field-2 valid
move green to field-2C
save field-2 someplace
else
move red to field-2C
move -1 to field-2L
if data-valid-flag = 'y'
move 'n' to data-valid-flag
move 'Field 2 is not valid' to error-message.


..and so on. Using this method:

(1) You get back everything that needs further processing/validation on the next
receive map;

(2) All fields in error are flagged (in red, fer instance) giving the user, who
is most likely familiar with the application, opportunity to fix more than one
error at a time;

(3) The error message refelects the first validation error, not the last, which
can confuse the user since the first field with -1 will get the cursor.

Like I said...this is just one way to do it.
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-10-20T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p4@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap>`

```

In article <344··.@ibm··l.com>,
Mark Miller wrote:

› Try this.
› 
…[22 more quoted lines elided]…
› drops out of 010500-FIND-HELP as soon as flag condition is satisfied.

No, it won't. You seem to be under the impression that the PERFORM is
continually checking the flag condition, but that is not the case. The
flag condition is evaluated only after the entire paragraph has been
PERFORMed.
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p7@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap>`

```

really dlmiller_at_inetdirect_dot_netDoug Miller wrote:
› Mark Miller  wrote:
› 
…[21 more quoted lines elided]…
› PERFORMed.

I assumed Mark was implying that the routine 002500-TEST-HELP would test
for and exit immediately if HL-HELP-SENT-FLAG was already true.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p8@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap>`

```

In article <01bcdedc$71bb4140$4d34b9ce@juddesk>,
"Judson D. McClendon" wrote:
› really dlmiller_at_inetdirect_dot_netDoug Miller wrote:
›› Mark Miller  wrote:
…[25 more quoted lines elided]…
› for and exit immediately if HL-HELP-SENT-FLAG was already true.

And how does this cause an exit from the PERFORM loop?
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p9@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap> <gap-4178dbd7cb-p9@usenetarchives.gap>`

```

really dlmiller_at_inetdirect_dot_netDoug Miller
wrote in article <62lsnc$3q0··.@p16··t.net>...
› In article <01bcdedc$71bb4140$4d34b9ce@juddesk>,
›    "Judson D. McClendon"  wrote:
…[31 more quoted lines elided]…
› And how does this cause an exit from the PERFORM loop?

I don't understand your question; there is no 'loop'. Every PERFORM
statement in the paragraph would be executed, but once HL-HELP-SENT-FLAG
was set, each PERFORMed paragraph would immediately detect it and exit
without doing anything. As I pointed out in my own response, there is a
performance penalty from doing the extra PERFORM/EXITs, but the logic would
avoid use of a GO TO EXIT in this paragraph. The example code and dialog
above has been snipped a lot, and may no longer make sense. You may need
to read the entire thread.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "tom boshans" <ua-author-17073781@usenetarchives.gap>
- **Date:** 1997-10-22T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p8@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap>`

```

Judson,
This might work:

move zeros to sub1,
hl-help-sent-flag.
move 'no' to ok-flag.
perform 010500-find-help thru 010500-exit
until (hl-help-sent-flag = 1)
or (ok-flag = 'ok').

010500-FIND-HELP.
add 1 to sub1.
evaluate sub1
when 001
move '0101-action' to hl-data-name
move recv-01-action to hl-data-value
when 002
move '01xx-tel-nbr' to hl-data-name
move recv-01-tel-nbr to hl-data-value
when 003
...
when 004
...
when 099 {...number of fields + 1}
move 'ok' to ok-flag
end-evaluate.

if ok-flag = 'no'
perform 002500-test-help
thru 002500-exit.

010500-exit.
exit.

Tom Boshans
tom_b_ny @ msn.com
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "tom boshans" <ua-author-17073781@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p11@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap> <gap-4178dbd7cb-p11@usenetarchives.gap>`

```

Judson,
Do I get a prize or what? :-)
Show me a goto and I'll show you a better way...

Tom Boshans wrote in article
<01bce02b$e79be360$21072399@tomszeos>...
› Judson,
› This might work:
…[35 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 6)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p12@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap> <gap-4178dbd7cb-p11@usenetarchives.gap> <gap-4178dbd7cb-p12@usenetarchives.gap>`

```

Sorry, Tom. I've been busy and wanted to give these suggestions a fair
review.

Well, the idea wasn't simply to be able to accomplish the job with no GO TO
statements, but to provide a GO TO-less way that is as efficient and
comparably easy to code and understand as the GO TO exit way. In other
words, a 'clean' solution. Your method would add the overhead of 50 loops,
plus execution of 50 additional IF tests coded (and debugged) in each loop,
or 2500 extra IF tests just for this one screen. For an average program
with 30 screens or so, that's 1500 loops and 75,000 extra IF tests. Good
try, but no cigar. 8-)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 7)_

- **From:** "tom boshans" <ua-author-17073781@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p13@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap> <gap-4178dbd7cb-p11@usenetarchives.gap> <gap-4178dbd7cb-p12@usenetarchives.gap> <gap-4178dbd7cb-p13@usenetarchives.gap>`

```

Judson,
My version and your version would execute the identical number of if
statements. Of course I didn't have to type in the additional 49 if's that
you did, not to mention the extra 49 performs. It's very clear that my
version is the cleanest, easiest to maintain and most elegant. :-)

Tom

Judson D. McClendon wrote in article
<01bce247$83d71e80$4734b9ce@juddesk>...
› Sorry, Tom.  I've been busy and wanted to give these suggestions a fair
› review.
…[63 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 8)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p14@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap> <gap-4178dbd7cb-p8@usenetarchives.gap> <gap-4178dbd7cb-p11@usenetarchives.gap> <gap-4178dbd7cb-p12@usenetarchives.gap> <gap-4178dbd7cb-p13@usenetarchives.gap> <gap-4178dbd7cb-p14@usenetarchives.gap>`

```

Tom, you are counting COBOL statements. But one statement of COBOL does
not equal one line of machine code. What I was referring to is the actual
code generated by the compiler, and executed by the CPU. Unless you have
an assembly language background, and study the code generated by your
compiler, you may not realize the cost tradeoffs of using one construct Vs
another. Subscripting is more expensive, because the actual address of the
referenced field has to be calculated at runtime. A construct like MOVE
AAA(X) TO BBB(Y) can generate a number of extra instructions, and take
several times as long to execute as MOVE AAA TO BBB. Statements like
SEARCH or SORT or COMPUTE might generate hundreds of machine instructions,
or call routines hundreds of instructions long. To give you an idea, I'll
generate a little 'pseudo assembly' for you. :-)

A simple direct move like this:

MOVE AAA TO BBB.

could generate (depending on the CPU) one or several machine instructions.
But for simplicity, let's say it only takes one. If it was more than one,
you would also have more than one in the final sequence below:

Move AAA to BBB

A subscripted move like this:

MOVE AAA(X) TO BBB(Y).

would likely generate something like this:

Multiply length of AAA entry times X giving TEMP
Move TEMP to INDEX1
Multiply length of BBB entry times Y giving TEMP
Move TEMP to INDEX2
Move (start of AAA table + INDEX1) to (start of BBB table + INDEX2)

This is a reasonably typical example, taking 5 instructions instead of just
one. For some CPUs, it might be only three, and for others, more than
five. Plus, the final indexed move is usually slower than an unindexed
move, because the indexes have to be added. If you use indexes instead of
subscripts, the multiply is eliminated, but you add the overhead of
converting the index back and forth when you compare or set between the
index and another index or numeric value.
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p7@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p4@usenetarchives.gap> <gap-4178dbd7cb-p7@usenetarchives.gap>`

```

›› The same applies to all the other field validation checks.  The program
›› drops out of 010500-FIND-HELP as soon as flag condition is satisfied.
…[4 more quoted lines elided]…
› PERFORMed.

Scary how some folks think COBOL flows!
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p17@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

Judson D. McClendon wrote:
› 
› --snip--
…[40 more quoted lines elided]…
›            EXIT.

OK, how 'bout THIS:

010500-FIND-HELP.
*
MOVE 0 TO HL-HELP-SENT-FLAG.
MOVE 0 TO SEND-TAB-COUNT.
*
MOVE "O101-ACTION" TO HL-DATA-NAME
MOVE RECV-01-ACTION TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT
IF (HL-HELP-SENT-FLAG = 1)
NEXT SENTENCE
END-IF
*
MOVE "O1XX-TEL-NBR" TO HL-DATA-NAME
MOVE RECV-01-TEL-NBR TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT
IF (HL-HELP-SENT-FLAG = 1)
NEXT SENTENCE
END-IF
*
MOVE "O1XX-QQQ-NBR" TO HL-DATA-NAME
MOVE RECV-01-TAG-NBR TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
THRU 002500-EXIT
IF (HL-HELP-SENT-FLAG = 1)
NEXT SENTENCE
END-IF
*
--and so on until finally--
*
MOVE 0 TO SEND-TAB-COUNT.

Notice that only the first two and the last statement have periods, thus the
NEXT SENTENCE in effect branches to the end of the paragraph :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p17@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap>`

```

Jim Van Sickle wrote in article
<344··.@i··.net>...
› Judson D. McClendon wrote:
›› 
…[41 more quoted lines elided]…
› NEXT SENTENCE in effect branches to the end of the paragraph :-)

Nice try Jim, but the ANSI COBOL 85 standard forbids use of NEXT SENTENCE
in an IF statement with an END-IF, though some compilers allow it.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "tedw..." <ua-author-1716797@usenetarchives.gap>
- **Date:** 1997-10-22T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p17@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap>`

```

In article <344··.@i··.net>, ji··.@i··.net says...
› 
› OK, how 'bout THIS:
…[20 more quoted lines elided]…
› NEXT SENTENCE in effect branches to the end of the paragraph :-)

Jim,

I agree with your logic. Until the first asshole newbie puts a period in the
middle of the paragraph... So, you fire him/her after the payroll run abends,
and you end up doing a tap dance in front of your boss (to save your job) and
explain why the newbie didn't follow the procedures. Been there, done
that...

Toni

Toni
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "pete ferzoco" <ua-author-6589080@usenetarchives.gap>
- **Date:** 1997-11-04T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p17@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap>`

```



Jim Van Sickle wrote:

› Judson D. McClendon wrote:
›› 
…[38 more quoted lines elided]…
› NEXT SENTENCE in effect branches to the end of the paragraph :-)

Yeah! I noticed - but would I notice at 2:32 AM with some Ops Analyst breathing
down my neck? I DOUBT IT! ;-)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "de..." <ua-author-17071313@usenetarchives.gap>
- **Date:** 1997-11-05T13:35:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p20@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap> <gap-4178dbd7cb-p20@usenetarchives.gap>`

```

Purity will remove the 'Next Sentence ' since this
creates
the exact same asm code as a goto

Next Sentence causes the compiler to evaluate the
address of the
next executable while a 'continue' truely drops
through

In article <63pkdk$gs0$1.··.@gte··e.net>,
pfe··.@g··.net wrote:
› 
› 
…[41 more quoted lines elided]…
›› Notice that only the first two and the last
statement have periods, thus
the
›› NEXT SENTENCE in effect branches to the end of
› the paragraph :-)
›
› Yeah! I noticed - but would I notice at 2:32 AM
with some Ops Analyst
breathing
› down my neck? I DOUBT IT! ;-)
› --
…[4 more quoted lines elided]…
› PGP FingerPrint: B48F 8AC1 830D A169 2689  BC39
1DD3 F69B 8865 F822

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "esmond pitt" <ua-author-4373961@usenetarchives.gap>
- **Date:** 1997-11-06T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p21@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap> <gap-4178dbd7cb-p20@usenetarchives.gap> <gap-4178dbd7cb-p21@usenetarchives.gap>`

```

This is a multi-part message in MIME format.
--------------7118674F4436679727AF3411
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

De··.@tec··e.com wrote:
›
› Purity will remove the 'Next Sentence ' since this
› creates
› the exact same asm code as a goto

Not in a COBOL system which supports ALTER. Also NEXT SENTENCE doesn't
oblige you to have a paragraph label next, which saves some overhead.

› Next Sentence causes the compiler to evaluate the
› address of the
› next executable while a 'continue' truely drops
› through

This really does generate an asm GOTO. So do all the ELSE statements and
a whole lot of other things. I really don't see what the assembly output
has to do with the price of fish.
--------------7118674F4436679727AF3411
Content-Type: text/x-vcard; charset=us-ascii; name="vcard.vcf"
Content-Transfer-Encoding: 7bit
Content-Description: Card for Esmond Pitt
Content-Disposition: attachment; filename="vcard.vcf"

begin: vcard
fn: Esmond Pitt
n: Pitt;Esmond
org: CP Telemedia Software Laboratories
adr: 493 St Kilda Rd;;;Melbourne;Victoria;3004;Australia
email;internet: pi··.@cpg··m.au
title: Consultant
tel;work: 61 3 9243 2285
tel;fax: 61 3 9243 2233
tel;home: 61 3 9534 5704
x-mozilla-cpt: ;0
x-mozilla-html: FALSE
end: vcard


--------------7118674F4436679727AF3411--
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "pete ferzoco" <ua-author-6589080@usenetarchives.gap>
- **Date:** 1997-11-04T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p17@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p17@usenetarchives.gap>`

```



Jim Van Sickle wrote:

› Judson D. McClendon wrote:
›› 
…[38 more quoted lines elided]…
› NEXT SENTENCE in effect branches to the end of the paragraph :-)

Yeah! I noticed - but would I notice at 2:32 AM with some Ops Analyst breathing
fown my neck? I DOUBT IT! ;-)
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "edwar..." <ua-author-1795746@usenetarchives.gap>
- **Date:** 1997-10-23T20:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p24@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

In article <01bcdd51$40bdc7c0$5134b9ce@juddesk>, "Judson D. McClendon"
writes:

<<< Endless code snipped >>>

Assuming that your screen fields are different lengths, the more corresponding
moves them to items in a table - all the same length - long enough to hold
the longest
item. The table is redefined, with the redefined items indexed. Flags
turned into "88"
level items. Coding the working storage correspondings & redefines is
facilitated
by block edit features of most good editors.

000-DEMO-PARAGRAPH.

SET NO-HELP-SENT TO TRUE
INITIALIZE SEND-TAB-COUNT

MOVE CORRESPONDING SCREEN-FIELDS TO TABLED-FIELDS

PERFORM
VARYING N FROM 1 BY 1
UNTIL (HELP-SENT)
MOVE TABLED-DATA-NAME (N) TO HL-DATA-NAME
MOVE TABLED-DATA-VALUE (N) TO HL-DATA-VALUE
PERFORM 002500-TEST-HELP
END-PERFORM

DISPLAY '*** VOILA IT''S DONE ***'

CONTINUE.

999-NEXT-PARAGRAPH.
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p24@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p24@usenetarchives.gap>`

```

I know some people like it, but I really hate using MOVE CORRESPONDING.
Defining all those identical field names makes the MOVE easier, but you
have to qualify every other reference to the fields. I experimented with
it years ago, and it always wound up being a lot more trouble than it was
worth. And you can easily have a field skipped and not know it. You would
also have to set up the extra hold area, which could get quite large, since
each field in the table would have to be as large as the largest possible
screen field. And the looping and subscripting would add considerable
overhead. Thanks for trying.
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p26@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

Here's an email response from: Jesper S魹ｽndergaard Jensen j.··.@p··.dk
›  
› What about this solution:
…[30 more quoted lines elided]…
› Cheers 

Thanks Jesper. I have two main objections to this approach. First is the
extra storage space required, which could be substantial. Second is the
performance penalty for use of subscripts and loop.
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "jesper s��ndergaard" <ua-author-16631167@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p26@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p26@usenetarchives.gap>`

```



› 
› Thanks Jesper.  I have two main objections to this approach.  First is
…[4 more quoted lines elided]…
› 

Extra storage - sure. Performance penalty? - that's nearly nothing!
Sometimes a table could increase performance (maybe not in this example) if
results of the treatments is used over an over (ex. by use of a search
all).
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p27@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p26@usenetarchives.gap> <gap-4178dbd7cb-p27@usenetarchives.gap>`

```

Jesper S魹ｽndergaard wrote:
› Judson McClendon  wrote:
›› Thanks Jesper.  I have two main objections to this approach.  First is
…[7 more quoted lines elided]…
› all).

Sure, tables can be ideal for some situations. Let's take a look at your
suggested code for this situation, and make an estimate of what the
performance penalty would be over GOTO exit. Here your suggested code:

› What about this solution:
› 
…[22 more quoted lines elided]…
›            END-PERFORM     

Instead of 100 direct moves (50 sets of 2 moves), we now have 100 indexed
moves, plus the 002500-TEST-HELP routine also has to use indexing to
reference the fields. With 50 fields, you have an additional 50 adds (SET
HL-DATA-IX UP BY 1), 100 extra moves of the index to an index register
(perhaps only 50, if the compiler is smart), plus data moves in general are
slower with indexing. In this routine alone we have 150 extra move/add
operations added the 100 original moves. (The number of PERFORMS and IF
statements is the same.) Add that to the indexed references in
002500-TEST-HELP, and this method is going to take somewhere on the order
of twice the CPU time. Agreed, the user will never notice it in this one
program. But to me, a doubling of CPU time is a significant performance
hit. If every similar routine is coded this way, we're talking around 50%
more CPU time overall for the program. If every program in the shop uses
this technique, you're going to need 50% more CPU horsepower to run the
online programs. Wouldn't you consider that a 'performance penalty'?
Because CPUs are so fast these days, programmers often get the impression
that stuff like this doesn't matter. It is usually not perceptible in a
given program, unless you benchmark it. But the cumulative effect over
many programs can be very significant.

When you benchmark your coding techniques (which I often do), you become
more aware of the costs and tradeoffs. When I started programming, it was
a requirement to be efficient in time and memory. It's not that critical
now, with more memory and CPU resources available. But wouldn't you like
programs like MS Word or Excel to load and run faster, and use less memory?
They would, if their programmers paid more attention to efficiency.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "jesper s��ndergaard" <ua-author-16631167@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p28@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p26@usenetarchives.gap> <gap-4178dbd7cb-p27@usenetarchives.gap> <gap-4178dbd7cb-p28@usenetarchives.gap>`

```



Judson D. McClendon skrev i artiklen
<01bce30e$e1657020$4e34b9ce@juddesk>...
› 
› Instead of 100 direct moves (50 sets of 2 moves), we now have 100 indexed
…[36 more quoted lines elided]…
› 


... If every similar routine is coded this way ... That's a wrong
assumption. They are not!

Oh yes, you should always have attention to efficiency (ex. be careful
about the initialize statement). But sometimes you have to find a balance
between proper design and easy maintainence - and maximal efficiency. (I
know that this is not the case in your example!). Often both can be
obtained.

I have been working with COBOL since 1985 in a organisations with 15-25
COBOL-programmers. Efficiency is here very important, but it's also very
important that anyone fast and easy can read, understand and change in
COBOL-programs written by other programmers.
The GO TO exits approach is a part of our standard and have been used for a
least 15 years. (And yes, we also developed a "FIND GO TO's out of a
paragraf/section"-rutine in the past. Like everybody else!)

And for your interest (another thread); we always perform sections and
never paragrafs. In a section we have 2-3 paragrafs. Ex. in 200-something
there could be a 200-start, 200-next and 200-exit. So we also have a "GO TO
next " approach. (Perform 200-something until ... )
And why sections: We use "200-something section 50." for the use of shared
code in our TP-system.
And a section is "a little bit more" a block of code (better abstraction).
And the rest is history...

Cheers
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-27T19:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p29@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p26@usenetarchives.gap> <gap-4178dbd7cb-p27@usenetarchives.gap> <gap-4178dbd7cb-p28@usenetarchives.gap> <gap-4178dbd7cb-p29@usenetarchives.gap>`

```

Jesper Sï¿½ndergaard wrote:
› 
› Judson D. McClendon  wrote:
…[8 more quoted lines elided]…
› assumption. They are not!

When I said "every similar routine", I referred to those other routines
which have the same structure as the TEST-HELP example I gave. The
TEST-HELP and very similar EDIT-FIELDS routines comprise a significant
portion of the code in these programs.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-10-30T19:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p31@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```



Judson D. McClendon wrote in article
<01bcdd51$40bdc7c0$5134b9ce@juddesk>...
› I have been observing with interest the debates going on in this
› newsgroup
…[73 more quoted lines elided]…
›                GO TO 010500-EXIT.


To answer the question I need to see what is in the 002500-Test-help
paragraph.

At first glance, since you want to exit upon the first hit, the Evaluate
statement would clean this up very nicely. I'll code an example for you
when I see what is in the above paragraph.
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-30T19:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p31@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p31@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› To answer the question I need to see what is in the 002500-Test-help
…[4 more quoted lines elided]…
› when I see what is in the above paragraph.

Any solution that is dependent on what 002500-TEST-HELP does would not
likely be useful. I gave the help example because it is very simple and
straightforward; but the field edits (not the one below, but the
interrelation edits) can be much more complex and irregular. In practice,
we couldn't use EVALUATE because the compiler is COBOL 74. But EVALUATE
would be suitable in a general solution to this situation.

002500-TEST-HELP.
*
IF (HL-DATA-1ST-CHAR = "?")
PERFORM 002000-SEND-HELP
THRU 002000-EXIT.
*
ADD 1 TO SEND-TAB-COUNT.
*
002500-EXIT.
EXIT.

A more fitting example would be 001000-EDIT, which is PERFORMED in a
similar manner to 002500-TEST-HELP.

001000-FIELD-EDIT.
*
MOVE 0 TO FEW-FIELD-ERROR-FLAG.
MOVE 0 TO FEW-NUM-VALUE.
MOVE 0 TO FEW-HOLD-CC.
MOVE 0 TO FEW-HOLD-YY.
MOVE 0 TO FEW-HOLD-MM.
MOVE 0 TO FEW-HOLD-DD.
MOVE SPACES TO FEW-ERROR-MSG.
*
FIND RSDF-RECORD VIA RSDF-NAME-SET
AT (RSDF-DATA-NAME = FEW-FIELD-NAME)
ON EXCEPTION
STRING "FIELD: " DELIMITED BY SIZE
FEW-FIELD-NAME DELIMITED BY " "
" NOT IN DICTIONARY FILE"
DELIMITED BY SIZE
INTO FEW-ERROR-MSG
MOVE SPACES TO RSDF-SHORT-DESC
PERFORM 001010-ERROR
THRU 001010-EXIT
GO TO 001000-EXIT.
*
IF (FEW-FIELD-VALUE = SPACES)
IF (RSDF-REQ-FLAG NOT = "Y")
GO TO 001000-EXIT
ELSE
IF (RSDF-VALUE-FLAG NOT = "Y")
MOVE "VALUE REQUIRED"
TO FEW-ERROR-MSG
PERFORM 001010-ERROR
THRU 001010-EXIT
GO TO 001000-EXIT.
*
IF (RSDF-TYPE = "A")
PERFORM 001100-ALPHA
THRU 001100-EXIT
ELSE
IF (RSDF-TYPE = "N")
PERFORM 001200-NUMERIC
THRU 001200-EXIT
ELSE
IF (RSDF-TYPE = "R")
PERFORM 001300-RANGE
THRU 001300-EXIT
ELSE
IF (RSDF-TYPE = "D")
PERFORM 001400-DATE
THRU 001400-EXIT
ELSE
IF (RSDF-TYPE = "T")
PERFORM 001500-TIME
THRU 001500-EXIT
ELSE
IF (RSDF-TYPE = "M")
PERFORM 001600-NAME
THRU 001600-EXIT
ELSE
IF (RSDF-TYPE = "S")
PERFORM 001700-SOC-SEC
THRU 001700-EXIT
ELSE
MOVE "DICTIONARY TYPE CODE INVALID"
TO FEW-ERROR-MSG
PERFORM 001010-ERROR
THRU 001010-EXIT
GO TO 001000-EXIT.
*
001000-EXIT.
EXIT.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: GO TO less purists, how would you do this?

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-07T19:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p33@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk>`

```

It is trivially simple to write a Cobol program without a single GO TO.
One needs only observe that Cobol doesn't even *have* a GO TO statement;
Cobol has a GO statement, which happens to contain the noise word TO.
Simply remove the extraneous TO and you have GO TO free code.
I  |\    Randall Bart                      mailto:Bar··.@usa··m.net
L  |/             @worldnet.att.net and @hotmail.com I am also Barticus
o  |\    1-818-985-3259                       Please reply without spam
v  | \   
e    |\  Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
Y    |/  
o    |\  Think You're Smart?
u    |/  Can you solve http://members.aol.com/PanicYr00/Sequence.html ?
```

##### ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p33@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap>`

```

RandallBart wrote:
› 
› It is trivially simple to write a Cobol program without a single GO TO.
…[11 more quoted lines elided]…
› u    |/  Can you solve http://members.aol.com/PanicYr00/Sequence.html ?
 
› I saw your COBOL puzzler in comp.software.year-2000:
 
› Cobol Quiz.
› 
…[3 more quoted lines elided]…
›        IF  A = B OR > C OR D

I must admit that I don't know the answer to this one. Will you post
the answer if us dinosaurs in comp.lang.cobol can't explain it?

Can I assume the correct answer is not:

IF A = B
OR A > C
OR A > D

Thanks in advance.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p34@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap>`

```

Arnold Trembley wrote:
› RandallBart wrote:
›› 
…[30 more quoted lines elided]…
› OR A > D

As I recall, the COBOL rule for evaluation of partial relation expressions
like this is that an incomplete relation reverts back to the last completely
expressed relation. In this case, the last complete relation was 'A = B', so
the result would be as if you had coded:
IF (A = B) OR (A > C) OR (A = D)

As an aside, I am amused by Mr. Bart's blatant narcissism (e.g. 'I LOVE YOU
RB' in his sig.). I was also amused by his 'Think You're Smart?' quiz.
Numerical sequence questions such as "What is the next number in
a,b,c,d,...?" are fallacious. There are virtually an infinite number of
possible answers, all equally valid, though some are more complex than
others. It reminds me of those stupid questions you get on some tests, for
example "A programming language is ____ ?". You could probably give several
different, perfectly defensible answers, but the teacher is looking for one
particular answer, maybe not even the best. In my younger, more foolish
years, I was on an ego trip as well. Yes, I blew the school curve on all the
achievement tests, and made the highest college entrance scores in my high
school's history, and in my college Calculus I class, the teacher asked me if
it was okay not to use my grade in the scale, because the next highest grade
would have been a C, etc. This is heady stuff. But an inflated ego is a
hungry beast. You have to feed it all the time, because at bottom it is
based on insecurity. You constantly have to prove yourself. That's why
people on ego trips like IQ tests and such, and like to remind you how high
they scored, particularly if it was higher than you. I learned years ago
that it is far better just to look at each individual, including yourself, as
a uniquely valuable person, no matter what their IQ. Each person has their
own strengths and weaknesses, and everybody has worth. For example, though
my wife is intelligent, she doesn't have the analytical and logical ability
that I do. But she does have such a wonderful personality, it's like she has
this 'nice field' which surrounds her. Everybody likes her, and people think
better of me because of her. With a few words, she can really cheer someone
who is depressed or worried. Which ability is more valuable? We as a
society need everybody's individual gifts. Being smart is, in some ways,
very much like being good looking or wealthy; it may be useful, and even
pleasant, but it is a very poor measures of the worth of a person, and can be
a great pitfall into selfish pride and ego.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p35@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› Arnold Trembley  wrote:
›› RandallBart wrote:
››› 
 
›› I saw your COBOL puzzler in comp.software.year-2000:
›› 
…[20 more quoted lines elided]…
›   IF (A = B) OR (A > C) OR (A = D)
 
› Correct.
 
› As an aside, I am amused by Mr. Bart's blatant narcissism (e.g. 'I LOVE YOU
› RB' in his sig.). 

Narcissism? Narcissus was in love with his own reflection. I love
every person and every thing. Hardly the same.

› I was also amused by his 'Think You're Smart?' quiz.
› Numerical sequence questions such as "What is the next number in
› a,b,c,d,...?" are fallacious.  There are virtually an infinite number of
› possible answers, all equally valid, though some are more complex than
› others. 

On that page (http://members.aol.com/PanicYr00/Sequence.html -- thanks
for the invitation to plug my own page), I already state that for any
sequence of n terms it is possible to generate a polynomial of degree
n-1 to fit it. I also state that the solution is "nicer" than that.
When the solution is finally revealed, my name will be cursed on 74
planets, but you will be forced to admit it's a simple sequence. I can
describe the algorithm in 28 bytes. (It will actually take more like
75 bytes to describe it so that anyone else will understand.)

I also stated that I don't think anyone will solve it in less than 11
terms. I have just yesterday posted the 11th term. Some genius should
be solving it soon.



› I learned years ago
› that it is far better just to look at each individual, including yourself, as
› a uniquely valuable person, no matter what their IQ.

Yes, though I'm more uniquely valuable than most people. 8^)

I  |\    Randall Bart                      mailto:Bar··.@usa··m.net
L  |/             @worldnet.att.net and @hotmail.com I am also Barticus
o  |\    1-818-985-3259                       Please reply without spam
v  | \   
e    |\  Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
Y    |/  
o    |\  Think You're Smart?
u    |/  Can you solve http://members.aol.com/PanicYr00/Sequence.html ?
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "je..." <ua-author-6589243@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p36@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p36@usenetarchives.gap>`

```

RandallBart wrote:



› Yes, though I'm more uniquely valuable than most people. 8^)

"Unique" is an absolute and thus cannot be qualified. It is therefore
incorrect to say that something is more/less unique, it is simply
unique.. :)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p38@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p36@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p36@usenetarchives.gap>`

```

RandallBart wrote in article
<6493m2$r.··.@bgt··t.net>...
› Judson D. McClendon wrote:
›› Arnold Trembley  wrote:
…[26 more quoted lines elided]…
› 

You guys have lost me somewhere.
In Unisys COBOL74 the expression compiles exactly as Arnold Trembley
suggested.
For example, substituting A=1, B=9, C=9, D=1
gives me a false because
A not = B
A not > C and
A not > D

Ross

http://www.geocities.com/Hollywood/Set/7185/
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 4)_

- **From:** "ti..." <ua-author-17073144@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p39@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p35@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap>`

```

On 10 Nov 1997 17:02:17 GMT, "Judson D. McClendon"
wrote:

› Arnold Trembley  wrote:
›› RandallBart wrote:
…[37 more quoted lines elided]…
›  IF (A = B) OR (A > C) OR (A = D)
Actually, this is not correct. I tested this on MicroFocus using this
scenario:
A=1
B=0
C=1
D=0
The condition as stated (A=B OR > C OR D) evaluated true. To break it
down, it apparently works like this
IF (1=0) OR (1>1) OR (1>0)
-or-
IF FALSE OR FALSE OR TRUE
So, Arnold was correct in his assumption (albeit he thought it was
wrong). MicroFocus COBOL would expand the condition to be:
IF (A=B) OR (A>C) OR (A>D).
› 
› As an aside, I am amused by Mr. Bart's blatant narcissism (e.g. 'I LOVE YOU
…[34 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 5)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p40@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p39@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap>`

```

Timothy Nicholson wrote:
› 
› Judson D. McClendon  wrote:
…[39 more quoted lines elided]…
› 	IF (A=B) OR (A>C) OR (A>D).

You are correct. On seeing your post, I looked up 'Conditional Expressions'
in both COBOL 74 and COBOL 80 manuals. The rule actually says "The effect of
using such abbreviations is as if the last preceding stated subject were
inserted in place of the omitted subject, and the last stated relational
operator were inserted in place of the omitted relational operator." It is
always best to verify how things 'should' work by checking the COBOL
standard. Any given compiler _could_ be implemented incorrectly, though in
this case it's not likely. I can't recall ever seeing this used in practice.
I wonder if many programmers actually code this way?
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 6)_

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p41@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p40@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap> <gap-4178dbd7cb-p40@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› Timothy Nicholson  wrote:
…[18 more quoted lines elided]…
›  I wonder if many programmers actually code this way?

Those that do should be taken out back and shot!
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 6)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p42@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p40@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap> <gap-4178dbd7cb-p40@usenetarchives.gap>`

```

Sorry, that should be 'both COBOL 74 and COBOL 85 manuals'.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 6)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p43@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p40@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap> <gap-4178dbd7cb-p40@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› Timothy Nicholson  wrote:
›› 
›› Judson D. McClendon  wrote:
››› 
 
›››››        IF  A = B OR > C OR D
››› 
…[7 more quoted lines elided]…
›› Actually, this is not correct.  I tested this on MicroFocus 
 
›› it apparently works like this
››       IF (1=0) OR (1>1) OR (1>0)
…[12 more quoted lines elided]…
› standard. 

Did you check the ANSI standard or the manual of a particular
implementation? (I regret I have neither at hand.)

› Any given compiler _could_ be implemented incorrectly, though in
› this case it's not likely.

You recalled the arcane trivia correctly, but now you're believing the
implementation.

› I can't recall ever seeing this used in practice.
› I wonder if many programmers actually code this way?

I've never seen this occur in practice either. The closest I've seen is

IF TYPE-CODE = 0 OR 3 OR 5 OR > 7
error

Anybody who codes this as

IF TYPE-CODE = 0 OR 3 OR > 7 OR 5
error

expecting the semantics we *both* recalled is a fool.

I  |\    Randall Bart                      mailto:Bar··.@usa··m.net
L  |/             @worldnet.att.net and @hotmail.com I am also Barticus
o  |\    1-818-985-3259                       Please reply without spam
v  | \   
e    |\  Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
Y    |/  
o    |\  Think You're Smart?
u    |/  Can you solve http://members.aol.com/PanicYr00/Sequence.html ?
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 7)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p44@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p43@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap> <gap-4178dbd7cb-p40@usenetarchives.gap> <gap-4178dbd7cb-p43@usenetarchives.gap>`

```

RandallBart wrote:
› 
› Judson D. McClendon wrote:
…[33 more quoted lines elided]…
› implementation?  (I regret I have neither at hand.)  

I checked two different COBOL manuals, one from a mainframe manufacturer, the
other MF COBOL, one COBOL 74, the other COBOL 85, published at least 20 years
apart. The whole paragraph was word-for-word identical in both manuals.
Either both paragraphs were accidentally written identically at astronomical
odds, or they were both taken from a common source. That common source is
almost certainly the ANSI COBOL standard. My son has my copy right now, so I
can't check to be sure.

›› Any given compiler _could_ be implemented incorrectly, though in
›› this case it's not likely. 
› 
› You recalled the arcane trivia correctly, but now you're believing the
› implementation.

No, just the opposite. I was so confident in my memory of the rule, that I
was looking up the reference to refute the test results. But both manuals
clearly agreed with the test, and the manuals 'appear' to quote verbatim from
the ANSI COBOL standard.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: GO TO less purists, how would you do this?

_(reply depth: 6)_

- **From:** "je..." <ua-author-6589243@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4178dbd7cb-p45@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4178dbd7cb-p40@usenetarchives.gap>`
- **References:** `<01bcdd51$40bdc7c0$5134b9ce@juddesk> <gap-4178dbd7cb-p33@usenetarchives.gap> <gap-4178dbd7cb-p34@usenetarchives.gap> <gap-4178dbd7cb-p35@usenetarchives.gap> <gap-4178dbd7cb-p39@usenetarchives.gap> <gap-4178dbd7cb-p40@usenetarchives.gap>`

```

"Judson D. McClendon" wrote:

› this case it's not likely. I can't recall ever seeing this used in practice.
› I wonder if many programmers actually code this way?

Only once - if they work for me!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
