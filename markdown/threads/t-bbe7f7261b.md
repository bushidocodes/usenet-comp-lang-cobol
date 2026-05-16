[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Restructure this!

_47 messages · 16 participants · 2003-08 → 2003-10_

---

### Re: Restructure this!

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-09T18:20:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <%RWYa.5405$BC2.2463@newsread2.news.atl.earthlink.net> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com>`

```
There are a couple of "advantages" to the EXIT PARAGRAPH statement - over GO
TO XXXX-exit.

1) It is an "unnamed" destination for the (admittedly implicit) GO TO.  This
means that ONLY an EXIT PARAGRAPH statement may be executed to go to this
"spot".  It canNOT lead to "eventual" spaghetti code with overlapping GO
TO's.

2) As it is unnamed and is ALWAYS the "nearest" end-of-paragraph, it is
impossible for maintenance to "accidentally" insert a new paragraph-name
between the statement's location and the actual paragraph exit (i.e. it is
impossible to introduce "fall-thru" logic with this statement and its
maintenance).

3) Some, but not all, definitions of "structured programming allow for such
a "branch to end of current structure" - as long as there is still only one
entrance and one exit of the structure.

  ***

IMHO, the first two reasons above explain WHY (again in my personal opinion)
this statement avoids all the maintenance and other "problems" that
structured coding were intended to "fix" - even in those environments where
the 3rd reason is not true.
```

#### ↳ Re: Restructure this!

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-10T01:20:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <%RWYa.5405$BC2.2463@newsread2.news.atl.earthlink.net> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net...
| There are a couple of "advantages" to the EXIT PARAGRAPH statement - over
GO
| TO XXXX-exit.
|
| 1) It is an "unnamed" destination for the (admittedly implicit) GO TO.
This
| means that ONLY an EXIT PARAGRAPH statement may be executed to go to this
| "spot".  It canNOT lead to "eventual" spaghetti code with overlapping GO
…[6 more quoted lines elided]…
| maintenance).

You can change the scope of the EXIT PARAGRAPH.
If you move a logic structure from a paragraph, and replace it with a
perform of the moved logic, you would introduce an error if the moved logic
contained an EXIT PARAGRAPH.
With the GO TO EXIT, the error may be obvious, but once the EXIT PARAGRAPH
is moved there is no obvious error.

THAT'S ALL

| 3) Some, but not all, definitions of "structured programming allow for
such
| a "branch to end of current structure" - as long as there is still only
one
| entrance and one exit of the structure.
|
|   ***
|
| IMHO, the first two reasons above explain WHY (again in my personal
opinion)
| this statement avoids all the maintenance and other "problems" that
| structured coding were intended to "fix" - even in those environments
where
| the 3rd reason is not true.
|
…[13 more quoted lines elided]…
| > >"Ask your vendor of choice WHEN they will be providing the EXIT
PARAGRAPH
| > >syntax from the 2002 COBOL Standard"
| >
…[47 more quoted lines elided]…
|
```

##### ↳ ↳ Re: Restructure this!

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-10T17:45:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh4m8d$p8h$1@aklobs.kc.net.nz>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:

> You can change the scope of the EXIT PARAGRAPH.
> If you move a logic structure from a paragraph, and replace it with a
…[3 more quoted lines elided]…
> is moved there is no obvious error.

If the same structure was moved and it contained a GO TO exit then it, too, 
would suffer the same problem if the GOTO was changed to the new paragraph 
exit.  The problem would be considerably worse if the goto was left as it 
was, the program would become spagetti.

The answer is: don't use  short cuts: 'goto exit' or 'next sentence' or 
'exit paragraph/section' are all equally vulnerable to misuse in the way 
you describe.

I am still wavering on exit perform, the rest I avoid entirely for exactly 
you reason you give.
```

###### ↳ ↳ ↳ Re: Restructure this!

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-10T11:37:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bh4m8d$p8h$1@aklobs.kc.net.nz...
| Harley wrote:
|
…[4 more quoted lines elided]…
| > With the GO TO EXIT, the error may be obvious, but once the EXIT
PARAGRAPH
| > is moved there is no obvious error.
|
| If the same structure was moved and it contained a GO TO exit then it,
too,
| would suffer the same problem if the GOTO was changed to the new paragraph
| exit.

|The problem would be considerably worse if the goto was left as it
| was, the program would become spagetti.

I don't know, depending on the compiler, it may still work, even though it
is spaghetti.
To me, the GO TO errror would be more obvious than the EXIT PARAGRAPH.

|
| The answer is: don't use  short cuts: 'goto exit' or 'next sentence' or
…[4 more quoted lines elided]…
| you reason you give.

The IBM compiler(s) I use don't support EXIT PERFORM.
I don't have any problems developing structured programs without it.
I don't know if I would use the EXIT PERFORM in new development if it were
available.

I'm wary of new features used as "fixes" to the language, because I've seen
some abuses of features in the past.
I'm not convinced that the EXIT PARAGRAPH is a necessity.
The alternative, GO TO EXIT, may be easier to deal with in a maintenance
environment.

What I can see happening with EXIT PARAGRAPH is people will write an
evaluate equivalent using it.
i.e.

If CONDITION-A
   do something
   EXIT PARAGRAPH
END-IF
.......
If CONDITION-Z
   do something
   EXIT PARAGRAPH
END-IF
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-10T13:20:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308101220.12541339@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote 

> To me, the GO TO errror would be more obvious than the EXIT PARAGRAPH.

That is probably because GO TO is on your 'automatic check list' and
EXIT xxx is not (yet).  It is a matter or training oneself to do these
checks.

> I'm not convinced that the EXIT PARAGRAPH is a necessity.
> The alternative, GO TO EXIT, may be easier to deal with in a maintenance
> environment.

You make it sound as if 'EXIT PARAGRAPH' and 'GO TO xxx-EXIT' are the
alterrnates and there is no other way.

 
> What I can see happening with EXIT PARAGRAPH is people will write an
> evaluate equivalent using it.
…[10 more quoted lines elided]…
> END-IF

Haven't they heard of ELSE even ?

I dislike EVALUATE true and so tend to use IF .. ELSE IF .. when there
is a variety of different tests.  I tend to only use EVALATE variable

  IF Condition-A
      do-a
  ELSE
  IF Condition-B
      do-b
  ELSE
  IF ...

It is necessary to count the IFs for the END-IFs but it works for me,
and doesn't require GOTO _or_ EXIT PARAGRAPH or any other exit
mechanism.  Some of these may be CONTINUE, but that has no problems
associated with it and cannot be abused.

My code also has the advantage that it cannot suffer from the problem
you started this with: taking a block of code out of line and
replacing it with a PERFORM - in fact I do that all the time to break
code down into simpler modules or to reuse.  eg in my above if
Condition-C also needs do-a then this will be an out-of-line perform -
I don't need to contrive a more complicated set of IFs to avoid
repeating in line code for do-a.

Actually the main beef that I have with EXIT PARAGRAPH/SECTION is that
it is NOT equivalent to 'EXIT PERFORM CYCLE' in an out of line PERFORM
as it may be used for.

For example if PERFORMed SECTIONs are being used the EXIT PARAGRAPH
only goes to the end of the current paragraph.  Some here have said
they use commentary paragraph names in PERFORMed SECTIONs.  This makes
the code liable to change depending on how 'comments' are added or
taken away.

Another used PERFORM section THRU paragraph where the exit paragraph
was the last paragraph in the section.  Put an EXIT SECTION in that
and the code fails.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-11T01:50:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lDCZa.95724$0v4.6586611@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308101220.12541339@posting.google.com...
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote
|
…[4 more quoted lines elided]…
| checks.

No, it's because the label associated with the GO TO is obviously out of the
scope of the paragraph, the EXIT has no label associated with it.

|
| > I'm not convinced that the EXIT PARAGRAPH is a necessity.
…[4 more quoted lines elided]…
| alterrnates and there is no other way.

Personally, I only use GO TO for abnormal termination.
I do have to maintain code written or modified by others.

I don't write GO TO EXIT, and I will probably never use EXIT PARAGRAPH.

|
| > What I can see happening with EXIT PARAGRAPH is people will write an
…[13 more quoted lines elided]…
| Haven't they heard of ELSE even ?

Hell, they don't even use evaluate.

And if the use the form above they don't need to use ELSE.

| I dislike EVALUATE true and so tend to use IF .. ELSE IF .. when there
| is a variety of different tests.  I tend to only use EVALATE variable

I find EVALUATE TRUE to be very handy.

|   IF Condition-A
|       do-a
…[14 more quoted lines elided]…
| code down into simpler modules or to reuse.

I do it all the time also.
AND, people go out of their way to thank me for doing it.

| eg in my above if
| Condition-C also needs do-a then this will be an out-of-line perform -
…[11 more quoted lines elided]…
| taken away.

Luckily, I haven't seen many PERFORMed SECTIONS lately.
The use of SECTIONs apparently depends on shop standards, and/or the
prevalent pratice in the region (country, continent).
There was a time when it was common for me to run into shop standards that
required the use of SECTIONs, it's much less common now.

| Another used PERFORM section THRU paragraph where the exit paragraph
| was the last paragraph in the section.  Put an EXIT SECTION in that
| and the code fails.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-11T14:28:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308101220.12541339@posting.google.com...
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote
|
<<snip>>
|
|
…[17 more quoted lines elided]…
| is a variety of different tests.  I tend to only use EVALATE variable

As I said in my other post, I find EVALUATE TRUE handy.

Here is an example of EVALUATE TRUE.
How would you code it?

*    ==============================================
*    THIS ROUTINE MATCHES TRANSACTIONS TO A MASTER
*    USING SEQUENTIAL PROCESSING
*    BECAUSE RANDOM IS TOO SLOW.
*    ------------------------------------------------
*    THERE MAY BE MULTIPLE TRANSACTIONS FOR A MASTER
*    ------------------------------------------------
*    THE READ-MAST ROUTINE WILL REWRITE UPDATED MASTER
*    RECORDS BEFORE READING THE NEXT MASTER RECORD.
*    ----------------------------------------------
     PERFORM  READ-MAST
     PERFORM  READ-TRAN

     PERFORM  UNTIL  EOF-MAST
                AND  EOF-TRAN
         EVALUATE  TRUE
             WHEN  EOF-MAST
                   PERFORM  TRAN-MISSING-MAST
                   PERFORM  READ-TRAN
             WHEN  EOF-TRAN
                   PERFORM  READ-MAST
                   SET  EOF-MAST  TO  TRUE
             WHEN  MAST-KEY  =  TRAN-KEY
                   PERFORM  PROCESS-TRAN
                   PERFORM  READ-TRAN
             WHEN  MAST-KEY  <  TRAN-KEY
                   PERFORM  READ-MAST
             WHEN  OTHER
                   PERFORM  TRAN-MISSING-MAST
                   PERFORM  READ-TRAN
         END-EVALUATE
     END-PERFORM.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-11T13:20:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308111220.3987324f@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote 

> | I dislike EVALUATE true and so tend to use IF .. ELSE IF .. when there
> | is a variety of different tests.  I tend to only use EVALATE variable
 
> Here is an example of EVALUATE TRUE.
> How would you code it?

With IF ... ELSE IF ... END-IF END-IF
 
As a dirct mechanical change it would be:

       PERFORM Read-Mast
       PERFORM Read-Tran
 
       PERFORM  
           UNTIL EoF-Mast
             AND EoF-Tran

            IF ( EoF-Mast )
                PERFORM Tran-Missing-Mast
                PERFORM Read-Tran
            ELSE 
            IF ( EoF-Tran )
                PERFORM Read-Mast               
                SET EoF-Mast      TO TRUE
            ELSE
            IF ( Mast-Key = Tran-Key )
                PERFORM Process-Tran
                PERFORM Read-Tran
            ELSE      
            IF ( Mast-Key < Tran-Key )
               PERFORM Read-Mast
            ELSE
               PERFORM Tran-Missing-Mast
               PERFORM Read-Tran
            END-IF
            END-IF
            END-IF
            END-IF
       END-PERFORM
       .

Though I would not write it exactly this way, for example I tend to
use the record keys as 'EoF-Flags' by having the Read-xxx move
HIGH-VALUES at end.

I also wouldn't have the Read-Mast do the rewrite of the previous, but
would have a separate ReWrite-Mast.  It would be too easy for the next
programmer to delete the Read-Mast on EoF-Tran because he may not see
the need to Read before setting EoF.

In general I would either have the Read-Mast as a random read (there
are very few cases in my systems where the transaction hit-rate is
high enough to require sequential), or I would be processing _every_
master in some way, such as aging the debtors balances, and so would
not short cut with the SET.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 7)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-08-11T16:31:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com>`

```
>"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote 
>
…[54 more quoted lines elided]…
>not short cut with the SET.

Not to cause offense, but... that's pretty horrifying!  At least do a
step-ladder format.  Yikes.  The whole point of EVALUATE is to avoid this
kind of thing!  :-)  Sorry to rag on you, but we have some code in some of
our programs that look a lot like this.  Mostly they were written with the
COBOL-74 standard and then someone decided to add a lot of END-IFs.  I can't
make heads or tails of it without a lot of effort.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-12T17:51:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh9vcc$g1v$1@aklobs.kc.net.nz>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick wrote:

> Not to cause offense, but... that's pretty horrifying!  At least do a
> step-ladder format.  

<shrug> I dislike indenting IFs when they are a case statement at the same 
level and are alternates as in an IF ... ELSE IF.

> Yikes.  The whole point of EVALUATE is to avoid this
> kind of thing!  :-)  

<shrug> A case statement is a case statement whatever the implementation. I 
can use EVALUATE if I want to or a series of IF ELSE if I want (which is 
the way that I have done it in '74 Cobol).  In some other languages I use 
switch {}, or if .. elif ...  The important thing about a _case_ statement 
is that it be recognisable by being a series of choices at the same indent 
level.

That is to say, for this to be a case statement there must be no statements 
between the ELSE and the next IF.

> Sorry to rag on you, but we have some code in some of
> our programs that look a lot like this.  Mostly they were written with the
> COBOL-74 standard 

How farsighted of them to implement the style of a case statement using '74.

> and then someone decided to add a lot of END-IFs.  I
> can't make heads or tails of it without a lot of effort.

Keep working at it.  We all like what we are used to seeing.  Newer styles 
take some time to get used to.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 9)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-08-12T09:37:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhb1kq$vhkjn$1@ID-184804.news.uni-berlin.de>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz>`

```
Richard Plinston<riplin@Azonic.co.nz> 08/11/03 11:51PM >>>
>Frank Swarbrick wrote:
>
…[3 more quoted lines elided]…
><shrug> I dislike indenting IFs when they are a case statement at the same

>level and are alternates as in an IF ... ELSE IF.
>
…[3 more quoted lines elided]…
><shrug> A case statement is a case statement whatever the implementation. I

>can use EVALUATE if I want to or a series of IF ELSE if I want (which is 
>the way that I have done it in '74 Cobol).  In some other languages I use 
>switch {}, or if .. elif ...  The important thing about a _case_ statement

>is that it be recognisable by being a series of choices at the same indent

>level.
>
>That is to say, for this to be a case statement there must be no statements

>between the ELSE and the next IF.
>
>> Sorry to rag on you, but we have some code in some of
>> our programs that look a lot like this.  Mostly they were written with
the
>> COBOL-74 standard 
>
>How farsighted of them to implement the style of a case statement using
'74.
>
>> and then someone decided to add a lot of END-IFs.  I
>> can't make heads or tails of it without a lot of effort.
>
>Keep working at it.  We all like what we are used to seeing.  Newer styles

>take some time to get used to.

I guess I'm a bit confused as to why you want to *simulate* as case
statement (using IF ELSE IF ELSE) rather than use the actual case statement
supported by the language (EVALUATE).

As for not understanding it, I have to admit I was exaggerating for effect. 
If done correctly they're not *that* hard to understand.  But I would say
they're probably more prone to error, especially if there are more than a
few conditions.  IBM mainframe compilers have a nice feature that lists each
statement's "level".  Take the following:

0 EVALUATE TRUE
0   WHEN CONDITION-1
1     PERFORM HANDLE-CONDITION-1
0   WHEN CONDITION-2
1     PERFORM HANDLE-CONDITION-2
0   WHEN CONDITION-3
1     PERFORM HANDLE-CONDITION-3
0   WHEN OTHER
1     PERFORM HANDLE-CONDITION-DEFAULT
0 END-EVALUATE

All of the performs are at the same statement level.  (Level 0 is actually
displayed as a blank.) But if I use IFs like you prefer I get:

0 IF CONDITION-1
1     PERFORM HANDLE-CONDITION-1
0 ELSE
1 IF CONDITION-2
2     PERFORM HANDLE-CONDITION-2
1 ELSE
2 IF CONDITION-3
3     PERFORM HANDLE-CONDITION-3
2 ELSE
3     PERFORM HANDLE-CONDITION-DEFAULT
2 END-IF
1 END-IF
0 END-IF

Logically, in terms of a case statement, each of the performs is at the same
level (level 1).  But in terms of COBOL, we have one at level 1, one at
level 2 and two at level 3.

With indentation that matches the statement levels we get:

0 IF CONDITION-1
1     PERFORM HANDLE-CONDITION-1
0 ELSE
1     IF CONDITION-2
2         PERFORM HANDLE-CONDITION-2
1     ELSE
2         IF CONDITION-3
3             PERFORM HANDLE-CONDITION-3
2         ELSE
3             PERFORM HANDLE-CONDITION-DEFAULT
2         END-IF
1     END-IF
0 END-IF

Anyway, I suppose it's just a matter of preference, but I just have a hard
time seeing why either of those IF/ELSE combos would be preferable to the
original EVALUATE...  Don't want to start a style war, though!  :-)



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-12T14:29:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308121329.7f286f28@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <bhb1kq$vhkjn$1@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick<Frank.Swarbrick@efirstbank.com> wrote 

> I guess I'm a bit confused as to why you want to *simulate* as case
> statement (using IF ELSE IF ELSE) rather than use the actual case statement
> supported by the language (EVALUATE).

Because I prefer to not use EVALUATE TRUE in which the WHENs are
actually IFs. I tend to only use EVALUATE variable where this is an
_actual_ case statement.

I didn't put the code up to convince anyone, I was specifically asked
as to "how I did it".
 
> As for not understanding it, I have to admit I was exaggerating for effect. 

Yes, I did think that was the case <grin>.

> If done correctly they're not *that* hard to understand.  

Given that I have been doing case statements this way since well
before EVALUATE, and it is also the way this coding is done in other
languages, then I find it particularly easy to understand.  It is only
a matter of what one is used to.

In C for example one can say:

             switch ( expression )
             {
             case 1:  statement; break;
             case 2:  ...
             }

This is equivalent of EVALUATE expression, but an EVALUATE TRUE can't
be done because the 'case labels' must be integers, except by:

              if ( condition 1)
                  {}
              else 
              if ( condition 2 )
                  ....

I just do it this way in Cobol, C, Python and whatever else I am using
at the time.

> But I would say they're probably more prone to error, 

In what way ?

All coding is 'prone to error'.  In fact there is one way that
EVALUATE can lead to a coding error which the compiler would pick up
when IF .. ELSE is used, that is when the actions of a condition are
commented out - perhaps because no action is actually required, or
hasn't yet been coded in development:  The compiler complains that an
IF has no statements, the EVALUATE silently executes the actions of
the next WHEN.

The actual example was within a PERFORM - the compiler should complain
if the wrong number of END-IF are used (see difference between
conditional and imperitive statements).  Without the PERFORM this is
one place where a full stop may be used to indicate to the next
programmer that this is and must return to level zero (see previous
'discussions').

> IBM mainframe compilers have a nice feature that lists each
> statement's "level".  Take the following:

Yes, the ICL compilers could do that too.  Handy if one has trouble
counting IFs and END-IFs.  Actually it is not such a problem when
END-IFs are used, it was useful when we had to use ELSE NEXT SENTENCE
to step out of a level.

> With indentation that matches the statement levels we get:

<shrug> it's a case statement so indentation need not apply.  As long
as there is nothing between the ELSE and the IF then it is the 'same
level' conceptually because it is an 'ELIF'.

> Anyway, I suppose it's just a matter of preference, but I just have a hard
> time seeing why either of those IF/ELSE combos would be preferable to the
> original EVALUATE...  Don't want to start a style war, though!  :-)

It was my ELSE IF combos that were the original and the EVALUATE
emulated this.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 9)_

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-09-30T19:00:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LMOdndpjv5WuhOeiXTWJiw@comcast.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz>`

```
In article <bh9vcc$g1v$1@aklobs.kc.net.nz>, riplin@Azonic.co.nz wrote:
>Frank Swarbrick wrote:

>> Not to cause offense, but... that's pretty horrifying!  At least do a
>> step-ladder format.  
>
><shrug> I dislike indenting IFs when they are a case statement at the same 
>level and are alternates as in an IF ... ELSE IF.


I myself prefer to line them up like a case statement but put the ELSE IF
on one line:

       PERFORM  
           UNTIL EoF-Mast
             AND EoF-Tran

            IF ( EoF-Mast )
                PERFORM Tran-Missing-Mast
                PERFORM Read-Tran
            ELSE IF ( EoF-Tran )
                PERFORM Read-Mast               
                SET EoF-Mast      TO TRUE
            ELSE IF ( Mast-Key = Tran-Key )
                PERFORM Process-Tran
                PERFORM Read-Tran
            ELSE IF ( Mast-Key < Tran-Key )
               PERFORM Read-Mast
            ELSE
               PERFORM Tran-Missing-Mast
               PERFORM Read-Tran
            END-IF.
       END-PERFORM

Of course, in a case (heh) like this, I would use EVALUATE.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-01T01:27:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com>`

```
and of course if you coded this program, it would get either a compile error
or an ANSI/ISO extension message (if such flagging were turned on) because
you have a CONDITIONAL rather than IMPERATIVE statement within your inline
PERFORM.  ANSI/ISO would require enough END-IF's to terminate ALL the IF
statements - which is why this type of "pretend ELSE IF is a case structure"
coding is so dangerous.

OOPS - I just noticed the period before the END-PERFORM.  I don't know ANY
compiler that would allow that!!!
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-01T14:34:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bleom3$she$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net>`

```

On 30-Sep-2003, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> and of course if you coded this program, it would get either a compile error
> or an ANSI/ISO extension message (if such flagging were turned on) because
> you have a CONDITIONAL rather than IMPERATIVE statement within your inline
> PERFORM.

Just checking my PP 5648-A25 IBM COBOL for OS/390 & VM  2.2.1 compiler is
completely silent about the following code:

PERFORM VARYING ADDR-INDX FROM 1 BY 1
          UNTIL ADDR-INDX > 4
    IF W-ADDR-TYPE (ADDR-INDX) = C-BILLING-ADDR
    OR W-ADDR-TYPE (ADDR-INDX) = C-BD-CONT-ED-ADDR
        PERFORM 3000-CHECK-DATABASE
    END-IF
END-PERFORM.

I suppose there must be a switch I can set to have it yell at me - but why, why,
why did the committee decide this should be illegal?
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 12)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-10-01T18:37:07+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33tlnv87ck8kg42q1qqrq0lt8f1n3socac@4ax.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu>`

```
On Wed, 1 Oct 2003 14:34:41 GMT "Howard Brazee" <howard@brazee.net> wrote:

:>On 30-Sep-2003, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

:>> and of course if you coded this program, it would get either a compile error
:>> or an ANSI/ISO extension message (if such flagging were turned on) because
:>> you have a CONDITIONAL rather than IMPERATIVE statement within your inline
:>> PERFORM.

:>Just checking my PP 5648-A25 IBM COBOL for OS/390 & VM  2.2.1 compiler is
:>completely silent about the following code:

:>PERFORM VARYING ADDR-INDX FROM 1 BY 1
:>          UNTIL ADDR-INDX > 4
:>    IF W-ADDR-TYPE (ADDR-INDX) = C-BILLING-ADDR
:>    OR W-ADDR-TYPE (ADDR-INDX) = C-BD-CONT-ED-ADDR
:>        PERFORM 3000-CHECK-DATABASE
:>    END-IF
:>END-PERFORM.

:>I suppose there must be a switch I can set to have it yell at me - but why, why,
:>why did the committee decide this should be illegal?

Why should it yell at you?

IF .... END-IF  is an imperative statement.

As is READ ... END-READ.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-01T19:01:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bwFeb.11434$NX3.11340@newsread3.news.pas.earthlink.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu>`

```
But it should be.  You have used an IMPERATIVE statement in your inline
perform.  The point was that the original code an IF with our a
corresponding END-IF.

Try the following code and see what your compiler says

  PERFORM VARYING ADDR-INDX FROM 1 BY 1
            UNTIL ADDR-INDX > 4
      IF W-ADDR-TYPE (ADDR-INDX) = C-BILLING-ADDR
      OR W-ADDR-TYPE (ADDR-INDX) = C-BD-CONT-ED-ADDR
          PERFORM 3000-CHECK-DATABASE
       Else if W-ADDR-TYPE (ADDR-INDX) = spaces
            continue
      END-IF
  END-PERFORM.

and compare that with

  PERFORM VARYING ADDR-INDX FROM 1 BY 1
            UNTIL ADDR-INDX > 4
      IF W-ADDR-TYPE (ADDR-INDX) = C-BILLING-ADDR
      OR W-ADDR-TYPE (ADDR-INDX) = C-BD-CONT-ED-ADDR
          PERFORM 3000-CHECK-DATABASE
       Else if W-ADDR-TYPE (ADDR-INDX) = spaces
            continue
      end-if
      END-IF
  END-PERFORM.

My comment was that trying to use "ELSE IF" as a "case statement" leads to
problems, not that you can't use a scope-termianted IF (an imperative
statement) within a PERFORM

P.S.  The ANSI/ISO compiler option for IBM mainframe compilers is FLAGSTD.
See:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3PG10/2.4.24?SHELF=IGY3SH10&DT=20020923143836
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-02T14:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blhcjl$p01$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu> <bwFeb.11434$NX3.11340@newsread3.news.pas.earthlink.net>`

```

On  1-Oct-2003, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> Try the following code and see what your compiler says
>
…[8 more quoted lines elided]…
>   END-PERFORM.

OK, I see the problem.   It's sort of like unmatched parenthesis.   For this to
work, the END-PERFORM needs to do an implicit END-IF the way periods do.    I
suppose the period could do an END-PERFORM as well, if they were going that way.
   Easy enough for the compiler makers to code (if they wanted to), but ugly.  
I don't mind that this is non-compliant, but would accept it either way.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 14)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-10-02T15:11:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031002111141.25496.00000150@mb-m05.aol.com>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu>`

```
I think I disagree with where you all are taking this.

Compliance with standards is one thing, and we can yield to the experts on the
standards per se.

However, practically, I do not want a compiler that complains for

  PERFORM
      ADD 1 TO STMT-DELIMIT-CNT
      .
*    ^ PERIOND AS SCOPE DELIMITER.

So

  PERFORM
      ADD 1 TO STMT-DELIMIT-CNT

      PERFORM NAMED-PARAGRAPH
      END-PERFORM
      .
*    ^ SCOPE DELIMITER OUTTER PERFOMR

Or

  PERFORM
      ADD 1 TO WESTSIDE-STORY

      PERFORM 
         ADD 1 TO INSIDE-STORY
      END-PERFORM
      .
*    ^ SCOPE DELIMITER OUTTER PERFOMR

Should not create noise, because I have work to do.  I am not speaking pure
compliance here.

Also, deprecated or not, a period is a scope
delimiter.  COBOL has, in effect, a super end curly brace. And it is not useful
to question its semantics. Everything ends at the end of a SENTENCE, because
that is how natural language works!

The deprecation of period is a mistake. The period symbol enables significant
efficiencies for the technical worker. It is much more powerful than a C
language or Jave end curly brace.

A period is much more efficient coding than END-PERFORM. Infact it can take the
place of numerous END-xyzs.

A period symbol is like a lexical analogue to semantic tail recursion. It
facilitates ordered contemplation of the nested code units.

I think we should lead back to the basics. COBOL mimicks natural language for a
number of reasons, including the fact that natural language works effectively,
period.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 15)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-10-02T23:19:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mV5fb.6177$op2.720786@news20.bellglobal.com>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu> <20031002111141.25496.00000150@mb-m05.aol.com>`

```
"RKRayhawk" <rkrayhawk@aol.com> wrote in message
news:20031002111141.25496.00000150@mb-m05.aol.com...
> I think I disagree with where you all are taking this.
>
> Compliance with standards is one thing, and we can yield to the experts on
the
> standards per se.
>
…[28 more quoted lines elided]…
> Should not create noise, because I have work to do.  I am not speaking
pure
> compliance here.
>
> Also, deprecated or not, a period is a scope
> delimiter.  COBOL has, in effect, a super end curly brace. And it is not
useful
> to question its semantics. Everything ends at the end of a SENTENCE,
because
> that is how natural language works!
>
> The deprecation of period is a mistake. The period symbol enables
significant
> efficiencies for the technical worker. It is much more powerful than a C
> language or Jave end curly brace.
>
> A period is much more efficient coding than END-PERFORM. Infact it can
take the
> place of numerous END-xyzs.
>
…[3 more quoted lines elided]…
> I think we should lead back to the basics. COBOL mimicks natural language
for a
> number of reasons, including the fact that natural language works
effectively,
> period.
>

I agree whole heartedly.  In fact, I think the standard of one period per
paragraph degrades the language. In effect, we are saying "thou shalt
program in run-on sentences".  I also see no reason to ban "next sentence".

"Next sentence" means one thing, and "continue" means quite another,
certainly, but *both* have their uses.  The usage of "next sentence" is
certainly no worse than the ancient standard of a dedicated exit paragraph
with allowable go to's within that paragraph.

One period per paragraph also loses you a whole extra level of granularity
when it comes to other stylistic usages.
As you say, the sentence is the basic structure of every human language.
Making the sentence and the paragraph two instances of the same object makes
the code far less readable, at least to me.

Last but not least, I believe the whole issue of cut and past with/without
periods, is not nearly as clear cut as the purists claim.  Two days ago, in
this same newsgroup, there was a bug that involved romoving periods for the
sake of style, and the entire code snippet failed prescisely because the
programmer removed the period that was "bad style", and reinserted it at the
"correct place".  If the period had simply been left in place, the code
would have worked fine, and the cut and paste would have worked fine. The
basic "cut unit" is the sentence, or group of such.

Cutting and pasting without reading the code line by line and adjusting the
indentation, mentally executing it, and generally tidying up is a mugs game
anyway. After a year oe two of Cobol, one should see the periods just fine.
In fact, they can be a lot clearer to read than matching up delimiters.  A
period is the end of the statement, no ifs ands or buts.

Donald
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 15)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-10-03T00:48:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-F05586.00480903102003@corp.supernews.com>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu> <20031002111141.25496.00000150@mb-m05.aol.com>`

```
In article <20031002111141.25496.00000150@mb-m05.aol.com>,
 rkrayhawk@aol.com (RKRayhawk) wrote:
<snip>
> Should not create noise, because I have work to do.  I am not speaking pure
> compliance here.
…[5 more quoted lines elided]…
> that is how natural language works!

Bob, I hate to be the one to break this to you, but 'natural language' 
sucks as a communication method.  How much time does all of humanity 
spend arguing over Mr. X said "x-y-z", or did he say "x-Y-z", but when 
he really said it, did he mean "X-y-ZZZ".

Idiom and imprecision are not good ways to communicate with a machine 
that works only with the exact values of 0 and 1.


> The deprecation of period is a mistake. The period symbol enables significant
> efficiencies for the technical worker. It is much more powerful than a C
> language or Jave end curly brace.

But that shortcut requires much effort on the part of future programmers 
to cope with.  The famous Yourden stat -- 90% of all code is added after 
the first release as maintenance, becomes important.  If you save 5 
seconds by not typing END-* when you initially code, it might well cost 
the company 45 seconds in the future to cope with the mess created -- 
for a net LOSS of 40 seconds.

And I disagree that it is any sort of inefficiency for the technical 
worker.  Any programmer worth the title knows what constructs he/she is 
using before they stop staring out the window.  The act of saving a few  
keystrokes in the _least_ time consuming part of the programming process 
(typing) is negligible.  There should be no need for a 
"terminate-everything-I-forgot-to" keyword.  


> A period is much more efficient coding than END-PERFORM. Infact it can take 
> the place of numerous END-xyzs.

The compiler will have an easier time with explicit constructs known at 
compile time (e.g. SPLAT to END-SPLAT) than with the roll-your-own 
constructs that can become possible when periods, sentences and labels 
are used.

Efficient at code time is a single use, but efficient at run time is 
forever.


> A period symbol is like a lexical analogue to semantic tail recursion. It
> facilitates ordered contemplation of the nested code units.

I always think of a period as a lazy end-paren.  

Would you assume that the last paren in a mathematical expression 
auto-magically 'closed' all preceding open parens, regardless of number?  
That would be nice and neat, but it introduces a very iffy level of 
ambiguity as to what the mathematician actually might have intended.


> I think we should lead back to the basics. COBOL mimicks natural language for 
> a number of reasons, including the fact that natural language works 
> effectively,

Which is why people _never_ miss-communicate.

The thing about a sentence is that everyone defines it differently.  In 
Cobol, a sentence can be anything from a single statement to an entire 
section -- much as in natural language a run on can ramble on, and on, 
and on, and on...The lack of explicit definition of a sentence  makes 
that construct meaningless.

> period.

I say kill the period, it allows imprecision that only a human, or a 
heuristically able computer, can understand.

Efforts by binary exact computers will always find ways to misunderstand 
them...


Regards,

END-POST
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-10-03T05:55:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bljh1t$5ca$1@panix1.panix.com>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu> <20031002111141.25496.00000150@mb-m05.aol.com> <joe_zitzelberger-F05586.00480903102003@corp.supernews.com>`

```
In article <joe_zitzelberger-F05586.00480903102003@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:

[snip]

>I say kill the period, it allows imprecision that only a human, or a 
>heuristically able computer, can understand.

Associative powers are such curious things... I read the above and thought 
of the assertion of Lucy van Pelt, in Charles Schulz's comic-strip 
'Peanuts', bellowing 'I LOVE mankind... it's PEOPLE I can't stand!'.

DD
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 16)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-10-03T14:37:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blkflb$kki$1@news.btv.ibm.com>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu> <20031002111141.25496.00000150@mb-m05.aol.com> <joe_zitzelberger-F05586.00480903102003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-F05586.00480903102003@corp.supernews.com...
> In article <20031002111141.25496.00000150@mb-m05.aol.com>,
>  rkrayhawk@aol.com (RKRayhawk) wrote:
> <snip>
> > Should not create noise, because I have work to do.  I am not speaking
pure
> > compliance here.
> >
…[3 more quoted lines elided]…
> > to question its semantics. Everything ends at the end of a SENTENCE,
because
> > that is how natural language works!
>
…[3 more quoted lines elided]…
> he really said it, did he mean "X-y-ZZZ".
Do you mean X-Y-Zee or X-Y-Zed?

> > The deprecation of period is a mistake. The period symbol enables
significant
> > efficiencies for the technical worker. It is much more powerful than a C
> > language or Jave end curly brace.
…[11 more quoted lines elided]…
> "terminate-everything-I-forgot-to" keyword.
A reasonable writer writes 50-120 words a minute.  Your removal of END-IF
would save approximately 1-3 seconds.

> > A period is much more efficient coding than END-PERFORM. Infact it can
take
> > the place of numerous END-xyzs.

I have seen numerous problems resulting from mismatched IFs where someone
has nested a number of them.
The problem is often more accute if the code is indented incorrectly.
IF X=Y THEN
     ADD ONE TO X
ADD ONE TO Y.

There are two intentions here....the one with the period, and the one with
the indenting. which is correct?
You have to read the code to really know.

Take C as another example of cheap efficiencies.
if (x=y)
    y++;
if (x=z)
    z++;

If later someone wants to add something they have to be cognizant of the
shortcut.  Yes, most people would know this rule, but if you are making
minor changes to tens of programs there will be an increased error risk with
this type of shortcut.  So for example, adding a counter p  if x OR z are
equal to x.

if (x==y)
    p++;
    y++;
if (x==z)
    p++;
    z++;
Probably is *NOT* what they want - so they would have to add the { }.

I therefore, always delimited and end my scopes.  It makes adding them much
easier.
 if (x==y)
{
    y++;
}
we would easily differentiate:
 if (x==y)
{
    p++;
    y++;
}
from
 if (x==y)
{
    p++;
}
y++;

Of course C coders would go extreme and
if (x==y++) p++;

> The compiler will have an easier time with explicit constructs known at
> compile time (e.g. SPLAT to END-SPLAT) than with the roll-your-own
…[4 more quoted lines elided]…
> forever.
Efficient at code time is a single use, but efficient at run time is
forever, and efficient at write time can be terribly confusing at read time.

I wouldn't have quite a large issue if the delimiter was say } ] | \ ? $ #
@, but unfortunately . is very small....didn't Bill miss it the first time
round in the original post?

> > A period symbol is like a lexical analogue to semantic tail recursion.
It
> > facilitates ordered contemplation of the nested code units.
>
…[6 more quoted lines elided]…
> > I think we should lead back to the basics. COBOL mimicks natural
language for
> > a number of reasons, including the fact that natural language works
> > effectively,
…[7 more quoted lines elided]…
> that construct meaningless.
This is why I've never used a next-sentence :-)

> > period.
>
> I say kill the period, it allows imprecision that only a human, or a
> heuristically able computer, can understand.
I say keep it because hell will freeze over before I work on a period
removal project.
Deprecate it and make it *always* print a compiler warning..then force the
practice of forcing developers to "understand" and "justify" each non
informational message in compiles.
I'm so tired of people who ignore compile warnings and then are surprised
when something isn't right.

In agreement,

JCE
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-03T18:49:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blkgc3$om8$1@peabody.colorado.edu>`
- **References:** `<blhcjl$p01$1@peabody.colorado.edu> <20031002111141.25496.00000150@mb-m05.aol.com> <joe_zitzelberger-F05586.00480903102003@corp.supernews.com>`

```

On  2-Oct-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> Bob, I hate to be the one to break this to you, but 'natural language'
> sucks as a communication method.

What do you mean by that?
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 12)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-10-01T13:43:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0310011243.20346bc6@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<bleom3$she$1@peabody.colorado.edu>...

<< history snipped>  

> Just checking my PP 5648-A25 IBM COBOL for OS/390 & VM  2.2.1 compiler is
> completely silent about the following code:
…[10 more quoted lines elided]…
> why did the committee decide this should be illegal?

I may be mistaken, but I think what Bill was commenting on looked more
like
    PERFORM ... IF  ... END-IF.   ... END-PERFORM
in which I see at least two problems:  the in-line PERFORM isn't
terminated by an END-PERFORM *in the same sentence*, and the
END-PERFORM that does exist doesn't match up to a PERFORM *in the same
sentence*.  It's the period after the END-IF that's causing the
problem.

NONE of this is intended to be a discussion of personal style issues,
only of syntactic validity.  Implicit references are to the 2002
standard.

I would expect a sequence like 
    PERFORM ... IF ... END-PERFORM 
to receive a syntax error because what goes inside the in-line PERFORM
has to be imperative, and IF without a matching END-IF is conditional,
not imperative.

A sequence like 
    PERFORM ... IF ... END-IF ... END-PERFORM 
looks OK to me because the IF ... END-IF combination comprises an
imperative statement.

An END-PERFORM is unambiguously a scope terminator for the most recent
in-line PERFORM, and the END-IF is unambiguously the scope terminator
for the IF, making the IF an imperative.  An *in-line* PERFORM *must*
be terminated, and an *out-of-line* PERFORM *can't* be.

Thus, I don't see anything wrong, offhand, with 
   PERFORM ... IF ... PERFORM A-PARAGRAPH ... END-IF ... END-PERFORM 

I don't think the committee decided that what *you* posted was
illegal.  But I agree with Bill that the example *he* seemed to be
discussing -- which had a period after the END-IF and before the
END-PERFORM -- ought to receive complaints, probably more than one,
from a conforming compiler.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-02T14:29:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blhcnb$ph4$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu> <c60a0b82.0310011243.20346bc6@posting.google.com>`

```

On  1-Oct-2003, charles.stevens@unisys.com (Chuck Stevens) wrote:

> I don't think the committee decided that what *you* posted was
> illegal.  But I agree with Bill that the example *he* seemed to be
> discussing -- which had a period after the END-IF and before the
> END-PERFORM -- ought to receive complaints, probably more than one,
> from a conforming compiler.

I thought he made his post and then added on that he noticed the period later,
implying that his objection was elsewhere.   His reply to my message indicates
that his primary objection was to the missing END-IF and that he assumed the
period was just a typo.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 14)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-10-02T16:00:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0310021500.7b93210c@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu> <c60a0b82.0310011243.20346bc6@posting.google.com> <blhcnb$ph4$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<blhcnb$ph4$1@peabody.colorado.edu>...
> On  1-Oct-2003, charles.stevens@unisys.com (Chuck Stevens) wrote:
> 
…[9 more quoted lines elided]…
> period was just a typo.

Your example was fine, as I see it.  

I think Ubiquitous' example as written should have received TWO syntax
errors:  one complaining about the fact that the in-line PERFORM
didn't have a required terminating END-PERFORM, and one complaining
that the END-PERFORM that formed the following sentence wasn't a valid
COBOL verb.

If the period between the END-IF and the END-PERFORM were emended the
syntax errors complaining about END-PERFORM itself should have gone
away, but then I'd expect some sort of error on the fact that the
statement inside the PERFORM wasn't imperative (maybe just one, maybe
one for each undelimited IF).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-01T14:03:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310011303.10522afb@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com> <E3qeb.9429$RW4.2448@newsread4.news.pas.earthlink.net> <bleom3$she$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> > and of course if you coded this program, it would get either a compile error
> > or an ANSI/ISO extension message (if such flagging were turned on) because
…[15 more quoted lines elided]…
> why did the committee decide this should be illegal?

You failed to understand the distinction between a 'Conditional
statement' and an 'imperitive statement'.

In you first example the compiler would (or could) complain about two
things:

     The full-stop before the END-PERFORM.
     The lack of a full set of END-IFs (4 are needed).

In the current example the IF is correctly terminated by an END-IF and
the content of the perform is an imperitive statement.

That is:

          IF ( condition )
              action

is a conditional statement.

          IF ( condition )
              action
          END-IF

Is an imperitive statement because it is correctly terminated.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 10)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-10-02T11:43:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blho3e$cj46n$1@ID-184804.news.uni-berlin.de>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com> <bh95fl$vc1ba$2@ID-184804.news.uni-berlin.de> <bh9vcc$g1v$1@aklobs.kc.net.nz> <LMOdndpjv5WuhOeiXTWJiw@comcast.com>`

```
Ubiquitous<weberm@polaris.net> 09/30/03 06:00PM >>>
>In article <bh9vcc$g1v$1@aklobs.kc.net.nz>, riplin@Azonic.co.nz wrote:
>>Frank Swarbrick wrote:
…[4 more quoted lines elided]…
>><shrug> I dislike indenting IFs when they are a case statement at the same

>>level and are alternates as in an IF ... ELSE IF.
>
…[25 more quoted lines elided]…
>Of course, in a case (heh) like this, I would use EVALUATE.

Of course this would not work because you have a period (full stop) prior to
your END-PERFORM.  I wonder if you could remove the END-PERFORM and have the
period terminate both the PERFORM and the IF.

Anyway, If COBOL had an ELSEIF (or ELSE-IF) in addition to an ELSE I would
be OK with this.  I believe BASIC works this way. It would look like this:

      PERFORM  
           UNTIL EoF-Mast
             AND EoF-Tran

            IF ( EoF-Mast )
                PERFORM Tran-Missing-Mast
                PERFORM Read-Tran
            ELSE-IF ( EoF-Tran )
                PERFORM Read-Mast               
                SET EoF-Mast      TO TRUE
            ELSE-IF ( Mast-Key = Tran-Key )
                PERFORM Process-Tran
                PERFORM Read-Tran
            ELSE-IF ( Mast-Key < Tran-Key )
               PERFORM Read-Mast
            ELSE
               PERFORM Tran-Missing-Mast
               PERFORM Read-Tran
            END-IF
       END-PERFORM

But lacking the ELSE-IF I'll stick with EVALUATE.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-12T21:14:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LMc_a.98275$0v4.6764392@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <qKNZa.93846$3o3.6560831@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308111220.3987324f@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308111220.3987324f@posting.google.com...
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote
|
…[43 more quoted lines elided]…
| HIGH-VALUES at end.

The 88 level could have been specified under the Key areas.
I usually save the Keys in working storage.

In the IBM mainframe environment a single byte flag generates more efficient
code.
I could be saving hundreths of a nano-second.
|
| I also wouldn't have the Read-Mast do the rewrite of the previous, but
| would have a separate ReWrite-Mast.

IMHO, it may simplify things to have the READ control the rewite.
i.e. Before I read, make sure the previous record was rewritten, if it was
changed.
IMHO, it's easier to implement a pre-tran, tran, and post-tran update
process.

| It would be too easy for the next
| programmer to delete the Read-Mast on EoF-Tran because he may not see
| the need to Read before setting EoF.

Most programmers who would screw it up, are also afraid to remove code.
You recognized why it was there.
A simple comment in the code could explain why it was there.

| In general I would either have the Read-Mast as a random read (there
| are very few cases in my systems where the transaction hit-rate is
| high enough to require sequential), or I would be processing _every_
| master in some way, such as aging the debtors balances, and so would
| not short cut with the SET.

If that were the case,
    WHEN  EOF-TRAN
                 PERFORM  READ-MAST
                       UNTIL   EOF-MAST
                 PERFORM  LAST-MAST

I saw Frank's response <G>.

The group we belong to sets the standards for the group, and so you find
different standards, some good, some bad, throughout the COBOL world.
There is no universal standard.

In the end, we are masters of our own destiny.
If our practices are acceptable within the organization, there is no need to
change them.
If our practices are not acceptable within the organization, it's wise to
consider changing either the practice, or the organization.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-11T17:47:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh8ks8$e33$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com>`

```

On 10-Aug-2003, riplin@Azonic.co.nz (Richard) wrote:

> For example if PERFORMed SECTIONs are being used the EXIT PARAGRAPH
> only goes to the end of the current paragraph.  Some here have said
> they use commentary paragraph names in PERFORMed SECTIONs.  This makes
> the code liable to change depending on how 'comments' are added or
> taken away.

I suppose they included EXIT SECTION for completions sake.  But once EXIT
PARAGRAPH is available, why do we need procedure division SECTIONs?
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-08-11T16:42:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vjg01aepj0nkef@corp.supernews.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:bh8ks8$e33$1@peabody.colorado.edu...
>
> On 10-Aug-2003, riplin@Azonic.co.nz (Richard) wrote:
…[8 more quoted lines elided]…
> PARAGRAPH is available, why do we need procedure division SECTIONs?

GO TO ... DEPENDING; just perform the section, no THRU.

Simulation of OO constructs. Use method names as section
names and class names for paragraphs. Evaluate a class ID
to determine which paragraph to execute within the method
(section). Make the 'object' accessable to the method then
perform method-name (that is, perform the section).

Simulation of modern modular programming. Use the module
name to identify the section and the entry name to identify
procedures within that module. Perform entry-name of
module-name.

Simulate the source structure of some other languages where
procedures are defined before use. Sections contain major
divisions of code. Each section is built of detailed procedures
(bottom-up). The driver for the section is last. Perform driver
of section-name. The driver performs its predefined
procedures. Such programs *may* be read, with
understanding, from the first source line to the last.

As to whether any of these is an improvement over common
practices is a matter of conjecture. I have experimented with
each and see more good than bad, for me; though I have not
yet undertaken a substantial project to exploit these ideas.

Your question was "[W]hy do we need procedure division
SECTIONs?". The answer is "We don't. I do."
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-11T21:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh905c$ik3$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu> <vjg01aepj0nkef@corp.supernews.com>`

```

On 11-Aug-2003, "Rick Smith" <ricksmith@mfi.net> wrote:

> > I suppose they included EXIT SECTION for completions sake.  But once EXIT
> > PARAGRAPH is available, why do we need procedure division SECTIONs?
>
> GO TO ... DEPENDING; just perform the section, no THRU.

I never found a real difference between PERFORM THRU or PERFORM section.   Same
errors happen with people adding paragraphs.  Same drop through logic needs to
be looked for.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-08-11T22:40:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vjgkvfbh6iiq1a@corp.supernews.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu> <vjg01aepj0nkef@corp.supernews.com> <bh905c$ik3$1@peabody.colorado.edu>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:bh905c$ik3$1@peabody.colorado.edu...
[snip]
> I never found a real difference between PERFORM THRU or PERFORM section.

Perform section-a thru section-z is more than one section.
Perform section-1 is one section. <g>

The 'real' difference is the number of sections performed.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-12T14:10:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhasga$j1m$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu> <vjg01aepj0nkef@corp.supernews.com> <bh905c$ik3$1@peabody.colorado.edu> <vjgkvfbh6iiq1a@corp.supernews.com>`

```

On 11-Aug-2003, "Rick Smith" <ricksmith@mfi.net> wrote:

> > I never found a real difference between PERFORM THRU or PERFORM section.
>
…[3 more quoted lines elided]…
> The 'real' difference is the number of sections performed.

Errors are the same.   Problems are the same.   A standard that allows one but
not the other doesn't go far enough.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-11T14:16:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308111316.445dd44@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 
 
> I suppose they included EXIT SECTION for completions sake.  But once EXIT
> PARAGRAPH is available, why do we need procedure division SECTIONs?

The lack of a need for performed sections and of perform thru is
independent of the availability of 'shortcuts' such as EXIT
PARAGRAPH/SECTION.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-12T14:13:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhaslg$j5e$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu> <217e491a.0308111316.445dd44@posting.google.com>`

```

On 11-Aug-2003, riplin@Azonic.co.nz (Richard) wrote:

> > I suppose they included EXIT SECTION for completions sake.  But once EXIT
> > PARAGRAPH is available, why do we need procedure division SECTIONs?
…[3 more quoted lines elided]…
> PARAGRAPH/SECTION.

The argument that I have grudgingly given into, is that doing maintenance,
sometimes a GO TO EXIT is significantly less disruptive of the current flow, and
thus less likely to introduce unexpected results.   (and more likely to be
traceable by future maintenance programmers).

My code doesn't have them.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-12T12:59:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308121159.1471a719@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0308101220.12541339@posting.google.com> <bh8ks8$e33$1@peabody.colorado.edu> <217e491a.0308111316.445dd44@posting.google.com> <bhaslg$j5e$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote

> The argument that I have grudgingly given into, is that doing maintenance,
> sometimes a GO TO EXIT is significantly less disruptive of the current flow, and
> thus less likely to introduce unexpected results.   (and more likely to be
> traceable by future maintenance programmers).

As I may have briefly mentioned once: At the time and place of adding
a GO TO there is absolutely nothing wrong with it, it is always
obvious at to its action.  At the label, however, the next programmer,
not having seen the GO TO or EXIT PARAGRAPH may make assumptions that
are defeated by the shortcut.

Usually there is an idiom of having a xxx-exit paragraph which forms a
warning that this may be expected.  The EXIT PARAGRAPH lacks this
warning mechanism and thus, in my view, ranks with NEXT SENTENCE +
END-IF as bug-breeders.
 
> My code doesn't have them.

No need to be so defensive   ;-)
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-11T17:45:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh8kna$e2r$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net>`

```

On 10-Aug-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:

> I'm wary of new features used as "fixes" to the language, because I've seen
> some abuses of features in the past.
> I'm not convinced that the EXIT PARAGRAPH is a necessity.
> The alternative, GO TO EXIT, may be easier to deal with in a maintenance
> environment.

Only if there IS an exit paragraph.    But with an EXIT PARAGRAPH available for
maintenance programmers, the last reasonable argument for PERFORM THRU is
destroyed.   And that is worth a lot.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-11T19:14:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fWRZa.94112$3o3.6582158@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <X7qZa.92501$3o3.6436908@bgtnsc05-news.ops.worldnet.att.net> <bh8kna$e2r$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bh8kna$e2r$1@peabody.colorado.edu...
|
| On 10-Aug-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:
|
| > I'm wary of new features used as "fixes" to the language, because I've
seen
| > some abuses of features in the past.
| > I'm not convinced that the EXIT PARAGRAPH is a necessity.
…[3 more quoted lines elided]…
| Only if there IS an exit paragraph.    But with an EXIT PARAGRAPH
available for
| maintenance programmers, the last reasonable argument for PERFORM THRU is
| destroyed.   And that is worth a lot.

I agree about the PERFORM THRU.
When I do development, I never use THRU, EXIT paragraphs, or SECTIONs, and I
doubt that I would use EXIT PARAGRAPH.
But, who knows, I may change my mind.
```

###### ↳ ↳ ↳ Re: Restructure this!

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-10T10:53:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u-ecnaVyHsQL96uiXTWJkg@giganews.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
>
> I am still wavering on exit perform, the rest I avoid entirely for
> exactly you reason you give.

There are a few cases where EXIT PERFORM comes in handy. The most obvious is
when you don't know the perform's range.

PERFORM WITH NO LIMIT
    (la-de-da...)
   IF (terminal condition)
      EXIT PERFORM
      END-IF
END-PERFORM.

or to bail early:

PERFORM UNTIL EOF = 'Y'
   (get a record)
   (check record against case 1)
   IF REALLY-BIG-BLUNDER EXIT PERFORM END-IF
   (check record against 100 other records)
   (look up everything in OED)
   (arrange Pokemon deck)
   (boil water)
   (consult queen)
   etc.
END-PERFORM.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-10T13:31:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308101231.3f56831@posting.google.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <u-ecnaVyHsQL96uiXTWJkg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> There are a few cases where EXIT PERFORM comes in handy. The most obvious is
> when you don't know the perform's range.

I know that it is 'handy', and I have used it for exactly what you
exemplify, but if the content of the PERFORM gets unwieldy I may take
it to another paragraph and make it an out-of-line perform.  With EXIT
PERFORM [CYCLE] this fails to work.  However a flag and 'UNTIL flag'
works either way.  While not 'modern' or 'super-efficient', it always
works and is not a trap for the next programmer (which may be me) to
fall into.

I tend to throw blocks of code around for reuse of to simply deep
nesting. Any style or idiom that gets in the way of doing this is
replaced by code that doesn't. No: GO TO, THRU, EXIT <anything>,
performs of SECTIONs, commentary labels, NEXT SENTENCE, or anything
else that changes meaning when moved.
```

###### ↳ ↳ ↳ Re: Restructure this!

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-10T21:16:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-YWdnT8_g40KYauiXTWJiw@giganews.com>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz> <u-ecnaVyHsQL96uiXTWJkg@giganews.com> <217e491a.0308101231.3f56831@posting.google.com>`

```
Richard wrote:
> "JerryMouse" <nospam@bisusa.com> wrote
>
…[15 more quoted lines elided]…
> else that changes meaning when moved.

I agree. I almost never use EXIT PERFORM. But I don't NOT use it when it's
the clearest way out of a mess. Same rationale as the NOTE paragraph.
```

###### ↳ ↳ ↳ Re: Restructure this!

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-11T17:43:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh8kk9$e2g$1@peabody.colorado.edu>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com> <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <c5hZa.94533$0v4.6467706@bgtnsc04-news.ops.worldnet.att.net> <bh4m8d$p8h$1@aklobs.kc.net.nz>`

```

On  9-Aug-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> The answer is: don't use  short cuts: 'goto exit' or 'next sentence' or
> 'exit paragraph/section' are all equally vulnerable to misuse in the way
…[3 more quoted lines elided]…
> you reason you give.

Where this command would be used is in maintenance where you want to make a
minimal change.   New code can be written without needing it (I do it all the
time), but it can be costly to restructure paragraphs in maintenance when a
EXIT-PARAGRAPH can do the job.
```

#### ↳ Re: Restructure this!

- **From:** codecrafters@cix.compulink.co.uk
- **Date:** 2003-08-18T23:31:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhrnk2$jaa$1@thorium.cix.co.uk>`
- **References:** `<oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net>`

```
In article <oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net>, 
wmklein@nospam.netcom.com (William M. Klein) wrote:

Much stuff about exit this, that and the other. But one trick seems to 
have gotten lost. The stuff below is a slightly modified version of a 
post of mine back in 1994 (alt.cobol days!):

While I agree with the notion of "exit section/paragraph" clauses, the 
problem I tend to have is that often one needs to <do> something, usually 
a quite simple something, at exit time. While it's possible (of course) to 
arrange things around the new exit clauses, the old 
paragraph-qualification trick (although an undisguised GO TO) can actually 
be much more convenient, IMHO. It works by using the requirement that 
duplicately-defined paragraph names (at program level) are automatically 
qualified to the current section - allowing the more useful Go to 
Section-Exit construct. It's the only GO TO you'll ever need. Example:
 
1000-Office-Process    Section.
    If Office-Not-Required
        Go to Section-Exit.
 
    < Other code >
Section-Exit.
    Perform 9000-Get-next-office.  (or anything *simple*)
 
2000-Salesman-Process Section.
    If Whatever-True
        Go to Section-Exit.
 
     < Other Code >
 
Section-Exit.
     Whatever you like. But keep it simple.
 
And so on. Each get-out GO TO can't go anywhere except the right place, 
your end-of-section code doesn't have to be replicated or in the 
performing section, and it even reads well (I'm a fan of COBOL for the 
english-like syntax).

You can of course break this by putting complex code in the exit 
paragraph. I restrict myself to either "continue" or a perform of a READ 
NEXT section, and it works a treat. 
 
Shown to me by a bloke years ago, and I've never even been tempted to use
anything else - mostly because I can't think of an improvement!
 
Pete.
```

##### ↳ ↳ Re: Restructure this!

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-19T13:58:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhtae3$dl6$1@peabody.colorado.edu>`
- **References:** `<oXaZa.5689$vo2.4807@newsread1.news.atl.earthlink.net> <bhrnk2$jaa$1@thorium.cix.co.uk>`

```
So what is the difference between this and the GO TO EXIT's that have plagued
code that I have had to maintain for decades?

(I replace EXIT with CONTINUE when maintaining such code, making it easier to
put in debugging commands - but I NEVER write code with multiple paragraphs
performed).
```

###### ↳ ↳ ↳ Re: Restructure this!

- **From:** codecrafters@cix.compulink.co.uk
- **Date:** 2003-08-19T16:58:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhtkvb$g9f$1@thorium.cix.co.uk>`
- **References:** `<bhtae3$dl6$1@peabody.colorado.edu>`

```
In article <bhtae3$dl6$1@peabody.colorado.edu>, howard@brazee.net (Howard 
Brazee) wrote:

> So what is the difference between this and the GO TO EXIT's that have 
> plagued
> code that I have had to maintain for decades?

Well, with the scheme you discuss it's tragically easy to make a mistake 
and GO to the wrong exit point, at which time things go horribly 
pear-shaped (to say the least) - that first observation being doubly true 
if the section numbers had been changed. I ran into a number of these 
mistakes one after the other and for a time was an advocate of the no-go's 
style. But even with the 85 extensions, I still found I was either 
indenting code (or nesting paragraphs) more deeply than I felt was 
consistent with clarity of intent (I firmly believe that layout of code 
on screen/paper is a woefully neglected art).

Anyway, I was chatting about this problem with a colleague and he 
suggested the scheme I outlined. I still like it, although it does offend 
purists (maybe that's part of the attraction)  :-) 

If you'll forgive a general observation not specifically aimed at 
yourself, I'll point out the last of George Orwell's six elementary rules 
("Politics and the English Language", 1946): "Break any of these rules 
sooner than say anything outright barbarous". I think we need to keep that 
in mind when discussing these points of style - it's easy to construct 
examples (and counter-examples**n, n usually a painfully large number) 
that show the awfulness of almost any of these methods, my own included. 
But if we keep the goal of _clarity_of_intent_ foremost in mind, we can 
focus on that instead, which to my mind is a potentially *much* more 
interesting discussion.

It's clear that you don't like the way I would do this - well, so be it. 
I'm afraid that you must take my word for it that you would find the code 
very easy to comprehend - which is, to my mind, the point.         
 
> (I replace EXIT with CONTINUE when maintaining such code, making it 
> easier to
> put in debugging commands - but I NEVER write code with multiple 
> paragraphs
> performed).

Oh, go on, let yourself go. Live a little. Orwell would smile at you :-)

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
