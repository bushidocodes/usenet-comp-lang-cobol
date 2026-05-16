[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Simple EVALUATE question

_15 messages · 9 participants · 2003-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Simple EVALUATE question

- **From:** studlow1@hotmail.com (The Mean Farmer)
- **Date:** 2003-05-21T12:36:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
When inside an EVALUATE statement is the object interrogated for every
WHEN condition inside of the EVALUATE - even if it has already found
the condition.

Sounds crazy but here is the goal.

EVALUATE WS-MESSAGE-INDEX(MSG-INDX)            
   WHEN 001                                    
        MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT    
        ADD +1               TO MSG-INDX       
   WHEN 002                                    
        MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT    
        ADD +1               TO MSG-INDX       
   WHEN 003                                    
        MOVE HOLD-3-KOUNT    TO DLH-2-KOUNT    
        ADD +1               TO MSG-INDX       
.
.
. 
END-EVALUATE

If I enter the statement with WS-MESSAGE-INDEX(MSG-INDX) = to 001 I
enter the first WHEN condition, move the KOUNT, and incrment the
Subscript by +1.  Now the value of WS-MESSAGE-INDEX(MSG-INDX) = 002.

Will the WHEN 002 condition be executed, or will it just go to the
END-EVALUATE statement??

If not I will just put a PERFORM UNTIL around the EVALUATE statement
and repeat the code over, and over, and over and over ....

Thanks!!!
```

#### ↳ Re: Simple EVALUATE question

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-21T14:46:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bagl32$962$1@slb2.atl.mindspring.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
Good news, bad news, and medium news.

Good news - With the 2002 COBOL Standard, things are "well defined" and
probably work the way you want. See Page 818 where it states (in part) as a
SUBSTANTIVE change from the '85 Standard,

"25) EVALUATE statement, sequence of execution. The sequence of evaluation
of selection subjects and objects is now defined to be from left to right
and selection objects are evaluated as each WHEN phrase is processed. When a
WHEN phrase is selected, no more selection objects are evaluated."

Bad News - this is a substantive change from the '85 Standard because it did
NOT define EVALUATE this way, so a "conforming" compiler WAS supposed to
evaluate ALL expressions (even if an "earlier one" was true).

Medium News - I *beleive* (but am not positive) that several '85 Standard
compilers actually DO work the "new" way not the way that was "strictly
required" by the '85 Standard.  You probably need to "test" your specific
compiler and code to see how they handle this and NOT relie on it when
porting to other compilers.
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-21T15:22:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bagn6i$src$1@slb0.atl.mindspring.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <bagl32$962$1@slb2.atl.mindspring.net>`

```
Although "true" my response was NOT responsive. After reading the other
responses, I realize that you *want* to execute multiple WHEN phrases
"sequentially".  As others have indicated, that doesn't happen (and won't
with the 2002 Standard).

Either your solution of putting this in a "loop" or changing to consecutive
IF (or even EVALUATE) statements will do what you want. Depending on the
rest of your application logic, you may also want to consider changing your
data items

 HOLD-1-KOUNT, HOLD-2-KOUNT, etc

to a table and use a loop with an index and not have either an EVALUATE or
an IF.
```

#### ↳ Re: Simple EVALUATE question

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-21T12:56:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<baglll$2i0t$1@si05.rsvl.unisys.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
Just so we are using the same terms:  In your example, WS-MESSAGE-INDEX
(MSG-INDX) is a "selection subject".  "001" is a "selection object" in
standards terms.

Selection subjects are evaluated once at the beginning of execution of the
EVALUATE statement.

The WHEN phrases are applied, right to left (or top to bottom, if you
prefer) against the values produced by the selection subject, until such
time as a WHEN phrase is satisfied, at which point no more WHEN phrases are
analyzed.

In your example, I would expect execution to proceed to the END-EVALUATE
statement once the MOVE and ADD associated with WHEN 001 are finished.

    -Chuck Stevens

"The Mean Farmer" <studlow1@hotmail.com> wrote in message
news:e0465864.0305211136.35c6530e@posting.google.com...
> When inside an EVALUATE statement is the object interrogated for every
> WHEN condition inside of the EVALUATE - even if it has already found
…[29 more quoted lines elided]…
> Thanks!!!
```

#### ↳ Re: Simple EVALUATE question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-21T22:58:53+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<semncvkle9teje82jb9268hq03apkm3fcq@4ax.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
On 21 May 2003 12:36:32 -0700 studlow1@hotmail.com (The Mean Farmer) wrote:

:>When inside an EVALUATE statement is the object interrogated for every
:>WHEN condition inside of the EVALUATE - even if it has already found
:>the condition.

:>Sounds crazy but here is the goal.

:>EVALUATE WS-MESSAGE-INDEX(MSG-INDX)            
:>   WHEN 001                                    
:>        MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT    
:>        ADD +1               TO MSG-INDX       
:>   WHEN 002                                    
:>        MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT    
:>        ADD +1               TO MSG-INDX       
:>   WHEN 003                                    
:>        MOVE HOLD-3-KOUNT    TO DLH-2-KOUNT    
:>        ADD +1               TO MSG-INDX       
:>.
:>.
:>. 
:>END-EVALUATE

:>If I enter the statement with WS-MESSAGE-INDEX(MSG-INDX) = to 001 I
:>enter the first WHEN condition, move the KOUNT, and incrment the
:>Subscript by +1.  Now the value of WS-MESSAGE-INDEX(MSG-INDX) = 002.

:>Will the WHEN 002 condition be executed, or will it just go to the
:>END-EVALUATE statement??

"The EVALUATE statement provides a shorthand notation for a series of nested
IF statements."

Thus at most one WHEN clause will be executed.

:>If not I will just put a PERFORM UNTIL around the EVALUATE statement
:>and repeat the code over, and over, and over and over ....

You appear to be using the wrong tool. 

You should:

  IF EVALUATE WS-MESSAGE-INDEX(MSG-INDX) = 001
        MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT    
        ADD +1               TO MSG-INDX       
  END-IF 
  IF EVALUATE WS-MESSAGE-INDEX(MSG-INDX) = 002	
        MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT    
        ADD +1               TO MSG-INDX   
  END-IF 
  IF EVALUATE WS-MESSAGE-INDEX(MSG-INDX) = 003
        MOVE HOLD-3-KOUNT    TO DLH-2-KOUNT    
        ADD +1               TO MSG-INDX       
  END-IF 
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-22T11:46:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eccb1b6.253564601@news.optonline.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <semncvkle9teje82jb9268hq03apkm3fcq@4ax.com>`

```
Binyamin Dissen <postingid@dissensoftware.com> wrote:

>On 21 May 2003 12:36:32 -0700 studlow1@hotmail.com (The Mean Farmer) wrote:
>
…[51 more quoted lines elided]…
>  END-IF 

Delete the word EVALUATE in the above. It's not valid COBOL. 

Better yet, put it in a loop:

perform varying k from 1 by 1 until k > [max] or MSG-INDX
    if  WS-MESSAGE-INDEX(MSG-INDX) = k
        move HOLD-k-KOUNT (k) to DLH-k-KOUNT (k)
        add 1 to MSG-INDX
    end-if
end-perform
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-24T21:22:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED028D1.20405@Knology.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <semncvkle9teje82jb9268hq03apkm3fcq@4ax.com>`

```
Binyamin Dissen wrote:
>   IF EVALUATE WS-MESSAGE-INDEX(MSG-INDX) = 001
        ^^^^^^^^
Did you just forget to delete that?  I'm not familiar with that 
syntax...  :)
```

###### ↳ ↳ ↳ Re: Simple EVALUATE question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-25T10:23:01+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rcq0dvggfm0n0lqmkt60hqst9ovqcu1qfg@4ax.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <semncvkle9teje82jb9268hq03apkm3fcq@4ax.com> <3ED028D1.20405@Knology.net>`

```
On Sat, 24 May 2003 21:22:09 -0500 LX-i <DanielJSNOSPAM@Knology.net> wrote:

:>Binyamin Dissen wrote:
:>>   IF EVALUATE WS-MESSAGE-INDEX(MSG-INDX) = 001
:>        ^^^^^^^^
:>Did you just forget to delete that?  I'm not familiar with that 
:>syntax...  :)

Yes.

Robert pointed that out.
```

###### ↳ ↳ ↳ Re: Simple EVALUATE question

_(reply depth: 4)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-25T16:51:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED13ADB.1040303@Knology.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <semncvkle9teje82jb9268hq03apkm3fcq@4ax.com> <3ED028D1.20405@Knology.net> <rcq0dvggfm0n0lqmkt60hqst9ovqcu1qfg@4ax.com>`

```
Binyamin Dissen wrote:
> On Sat, 24 May 2003 21:22:09 -0500 LX-i <DanielJSNOSPAM@Knology.net> wrote:
> 
…[8 more quoted lines elided]…
> Robert pointed that out.

I saw further down - that's what I get for being 4 days behind in 
here...  :)  That's okay - I did something similar a couple of times 
this week.

> Director, Dissen Software, Bar & Grill - Israel

I must say, that's an interesting mix...  Sounds like a fun place to 
work, though...
```

#### ↳ Re: Simple EVALUATE question

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-22T08:06:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bagm8f$pku$1@aklobs.kc.net.nz>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
The Mean Farmer wrote:


> Will the WHEN 002 condition be executed, 

No.

> or will it just go to the
> END-EVALUATE statement??

Yes.
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** studlow1@hotmail.com (The Mean Farmer)
- **Date:** 2003-05-22T05:15:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0465864.0305220415.6bbad963@posting.google.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <bagm8f$pku$1@aklobs.kc.net.nz>`

```
You guys are my heros.  Thanks you for the replies.

Looks like I get to do ugly coding.  UGH!!!
```

#### ↳ Re: Simple EVALUATE question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-22T11:46:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eccb157.253470306@news.optonline.net>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
studlow1@hotmail.com (The Mean Farmer) wrote:

>When inside an EVALUATE statement is the object interrogated for every
>WHEN condition inside of the EVALUATE - even if it has already found
…[27 more quoted lines elided]…
>and repeat the code over, and over, and over and over ....

COBOL goes to the end-evaluate after the first hit. You want to build your
'state machine' in the C language, where a case statement continues 'evaluating'
after a hit .. unless you say 'break'. Many many bugs have be created by
forgetting to write 'break'.
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-05-22T10:52:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vcpp3bfce0sv7e@corp.supernews.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <3eccb157.253470306@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3eccb157.253470306@news.optonline.net...
> studlow1@hotmail.com (The Mean Farmer) wrote:
[snip]
> >
> >If not I will just put a PERFORM UNTIL around the EVALUATE statement
…[3 more quoted lines elided]…
> 'state machine' in the C language, where a case statement continues
'evaluating'
> after a hit .. unless you say 'break'. Many many bugs have be created by
> forgetting to write 'break'.

One might prefer to use COBOL to do the equivalent of C,
two methods come to mind.

I have used the second method to improve program
performance. These were the increases of 80% and
900% I had previously mentioned in the group.

Perform paragraphs only style.

W-SWITCH.
  EVALUATE WS-MESSAGE-INDEX(MSG-INDX)
     WHEN 001
          PERFORM W-001
     WHEN 002
          PERFORM W-002
     WHEN 003
          PERFORM W-003


   END-EVALUATE.

W-001.
     MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT
     PERFORM W-002.
W-002.
     MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT
     PERFORM W-003.
W-003.
     MOVE HOLD-3-KOUNT    TO DLH-3-KOUNT
     PERFORM W-004.

Peform sections style.

W SECTION.
W-SWITCH.
  GO TO W-001 W-002 W-003 ...
    DEPENDING ON MSG-INDX
  GO TO W-EXIT.
W-001.
     MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT.
W-002.
     MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT.
W-003.
     MOVE HOLD-3-KOUNT    TO DLH-3-KOUNT.


W-EXIT.
  EXIT.
```

##### ↳ ↳ Re: Simple EVALUATE question

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-23T07:23:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<baj844$skb$1@aklobs.kc.net.nz>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com> <3eccb157.253470306@news.optonline.net>`

```
Robert Wagner wrote:

> COBOL goes to the end-evaluate after the first hit. 

Correct.

> You want to build your
> 'state machine' in the C language, where a case statement continues
> 'evaluating' after a hit .. unless you say 'break'. 

No, that is wrong.  That is not how the C case (switch) statement works. It 
does not 'continue evaluating', it does not 'evaluate' each case after a 
hit.

In a C switch the case labels are just numeric labels.  The switch is, in 
effect, a go to depending on.  After the case label has been selected the 
code will continue to be executed until the end of the block or a break 
statement.

The presence or absence of other case labels is irrelevant to this 'drop 
through', they are not 'evaluated'.


> Many many bugs have be
> created by forgetting to write 'break'.

OTOH actions can be combined by ordering the case labels and having the 
drop throughs in a useful way.

Cobol allows several empty WHENs to use one set of actions.  One has to be 
careful that if no action is required on a particular case a CONTINUE is in 
place otherwise the next WHEN's actions are done.
```

#### ↳ Re: Simple EVALUATE question

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-05-23T14:37:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<balbn4$aev$4@news.utelfla.com>`
- **References:** `<e0465864.0305211136.35c6530e@posting.google.com>`

```
The Mean Farmer <studlow1@hotmail.com> wrote:

: When inside an EVALUATE statement is the object interrogated for every
: WHEN condition inside of the EVALUATE - even if it has already found
: the condition.

EVALUATE stops at the first condition which evaluates as TRUE.


: Sounds crazy but here is the goal.

: EVALUATE WS-MESSAGE-INDEX(MSG-INDX)            
:    WHEN 001                                    
:         MOVE HOLD-1-KOUNT    TO DLH-1-KOUNT    
:         ADD +1               TO MSG-INDX       
:    WHEN 002                                    
:         MOVE HOLD-2-KOUNT    TO DLH-2-KOUNT    
:         ADD +1               TO MSG-INDX       
:    WHEN 003                                    
:         MOVE HOLD-3-KOUNT    TO DLH-2-KOUNT    
:         ADD +1               TO MSG-INDX       
: .
: .
: . 
: END-EVALUATE

: If I enter the statement with WS-MESSAGE-INDEX(MSG-INDX) = to 001 I
: enter the first WHEN condition, move the KOUNT, and incrment the
: Subscript by +1.  Now the value of WS-MESSAGE-INDEX(MSG-INDX) = 002.

: Will the WHEN 002 condition be executed, or will it just go to the
: END-EVALUATE statement??

: If not I will just put a PERFORM UNTIL around the EVALUATE statement
: and repeat the code over, and over, and over and over ....

Remove the EVALUATE statement and replace it with a PERFORM loop.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
