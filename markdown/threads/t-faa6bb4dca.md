[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GO TO questions

_31 messages · 16 participants · 2001-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### GO TO questions

- **From:** "Jean-Ren��� Duval" <jrduval@videotron.ca>
- **Date:** 2001-10-21T11:23:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
Hello.

I had a discussion with a colleage about that famous GO TO. He said no
matter what the circumstances never use any GO TO because this is bad
programming practices. In a perfect world, section coding should not exceed
2 pages in length and GO TOs are useless. But in a real world, I see so many
programs with 4 or more pages so if I don't use GOTOs, entire sections would
have to be rewritten. And even when I'm coding new ones, I'm using those
GOTO into my code. Is it a good pratice or should I use some kind of switch
instead ?

Another one. Do you know any places that I could find some examples on how
to use system variables (MVS) in a Cobol programs.

Thank you for your response.

Jean-Ren� Duval
jrduvalxxx@videotron.ca
```

#### ↳ Re: GO TO questions

- **From:** "Paul Raulerson" <praul@isot.NOSPAM.com>
- **Date:** 2001-10-21T11:22:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tt5tnq704epfb8@corp.supernews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
My opinion only:

   There is never a good reason to use a GOTO in the average COBOL program.
If the program seems to have sections so large that you *need* GOTO's,  the
program
was not designed correctly.

  Now the generic statement that GOTOs are bad is ridiculous too. There
*are* situations
where you need to use a GOTO - like when you are using COBOL to write stuff
that would be better written in assembler. <grin>

  Actually, the only acceptable situation where I allow GOTOs in my shop is
when it is in legacy
code; I've yet to see a need for it in any newly written code, and that
include CICS modules.
Under CICS, there are some arguments that make sense about using a GOTO in
exception
handling, but I personally have not seen it make enough CPU difference to
say that it is a
good idea.

  YMMV, and there are other people here whose opinions I respect who
disagree.

-Paul

"Jean-Ren� Duval" <jrduval@videotron.ca> wrote in message
news:3OBA7.931$p64.161630@wagner.videotron.net...
> Hello.
>
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?
>
…[10 more quoted lines elided]…
>
```

#### ↳ Re: GO TO questions

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-21T16:31:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tLCA7.37359$ev2.44194@www.newsranger.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
Hi JR,

Here we go again. You've probably started another fire storm, but my view is
that GO TOs s/b (c/b) used to GO TO pgraph-exit but nowhere else. This
convention eliminates the need for some ugly nested IFs and also makes things
easier for the code reader in this respect:

If you code: IF WS-X = y
GO TO 100-EXIT
END-IF

IF WS-A = a
GO TO 100-EXIT
END-IF 
etc.

Code Readers can quickly see that this pgraph doesn't (or does) concern them,
and can procede fairly quickly. Without the GO TO they have to "keep their
place" through a complex IF to determine whether the pgraph is of interest.

Well, that's my take. I'm sure you'll get others. We report; you decide.

Re. your 2nd ques: mvshelp.com has an IBM Manual page. Click on the COBOL
manuals; then go to (go to?) the bottom of the page; the 3rd manual from the
bottom s/b the COBOL Ref Man; click there and then look in the manual index at
the bottom. You might try the COBOL Pgmmer's guide, too. It's 1 or 2 entries
above the REF Man.

Regards, Jack.    




In article <3OBA7.931$p64.161630@wagner.videotron.net>, Jean-Ren� Duval says...
>
>Hello.
…[20 more quoted lines elided]…
>
```

#### ↳ Re: GO TO questions

- **From:** "Jean-Ren��� Duval" <jrduval@videotron.ca>
- **Date:** 2001-10-21T12:39:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5VCA7.1414$p64.229130@wagner.videotron.net>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```

"Jean-Ren� Duval" <jrduval@videotron.ca> a �crit dans le message news:
3OBA7.931$p64.161630@wagner.videotron.net...
> Hello.
>
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?
>
…[10 more quoted lines elided]…
>
Thank you very much for your very quick response. I'll keep your answers in
mind when coding.
```

#### ↳ Re: GO TO questions

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-21T17:56:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```

"Jean-Ren� Duval" <jrduval@videotron.ca> wrote in message
news:3OBA7.931$p64.161630@wagner.videotron.net...
> Hello.
>
>  But in a real world, I see so many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten.

And your dilemma is?

>And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?

No switches. No GO TOs. No SECTIONS. Use PERFORMS, CALL, and INVOKE. Once
you get the hang of it (takes about a year), the thought processes become
automatic.

Here's the reason: While it is possible to write buggy, hard-to-follow, and
error-prone code in any language with any constructs, it's easy, really
easy, to make a mess with GOTOs; GOTO-less programming imposes a mental
discipline which minimizes these problems (or so many people believe).
```

##### ↳ ↳ Re: GO TO questions

- **From:** "Jean-Ren��� Duval" <jrduval@videotron.ca>
- **Date:** 2001-10-22T18:15:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AW0B7.10986$p64.1248653@wagner.videotron.net>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com>`

```

"JerryP" <news@bisusa.com> a �crit dans le message news:
2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com...
>
> "Jean-Ren� Duval" <jrduval@videotron.ca> wrote in message
…[8 more quoted lines elided]…
> And your dilemma is?
Time and money.
>
> >And even when I'm coding new ones, I'm using those
…[6 more quoted lines elided]…
> automatic.
In our shop, sections and exit paragraphs are mandatory. GO TOs (almost).

> Here's the reason: While it is possible to write buggy, hard-to-follow,
and
> error-prone code in any language with any constructs, it's easy, really
> easy, to make a mess with GOTOs; GOTO-less programming imposes a mental
> discipline which minimizes these problems (or so many people believe).
If I understand, GO TO meens bad logic. I don't thing that's always the
case.
But point taken. I'll keep that in mind when coding.

Thank you for your constructive critics.

J.R.Duval
```

###### ↳ ↳ ↳ Re: GO TO questions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-22T17:56:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r28dq$kkj$1@slb6.atl.mindspring.net>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net>`

```
When talking about "GO TO" - there really are three VERY different cases.

A) Case 1 -
    GO TO is from within a procedure (paragraph or section) to a (named)
exit point associated with JUST the procedure in which the GO TO was coded.
Furthermore, there are no other procedure names (labels) between the GO TO
statement and the "exit-label" to which the GO TO refers. This technique
DOES adhere to ONE definition of structured coding - in that every
"procedure block" has a single exit/entry point.

NOTE: This is the technique that can be replaced by the new EXIT
PARAGRAPH/SECTION statements - when/where available.  With the new syntax,
there is NO CHANCE of introducing new "labels" between the GO TO/EXIT
statement and the exit point.  This enhances maintainability and avoids one
type of maintenance error.

B) Case 2 -
  (variation on Case 1) - one uses a GO TO statement to branch "back" to the
procedure-label of the procedure being executed.  This is a "valid loop"
structure - and does also adhere to the "single exit/entry" definition of
structured programming.  In my opinion, there really is no need for this
structure in COBOL - as the UNTIL (with TEST BEFORE/AFTER) really does
provide this facility in an "easy to read/detect" manner.  However,
(particularly in OLD code - for SORT input/output procedures) some existing
applications do use it.

As long as "case 1" and "case 2" are *NEVER* mixed in the same procedure
(and hopefully not in the same application and "nice to have" not even in
the same programming shop),  this is "medium" easy to maintain and enhance.
If you have an "automated" program to verify that you never insert another
procedure-label BETWEEN the GO TO statement and where it goes to, things
should be reasonably maintainable (even though I don't personally LIKE this
technique).

   ***
Case 3 - GO TO statements exist to branch from within one procedure to
another procedure that actually DOES something (rather than "exit").  This
is the one that is "by definition" (and I believe ALL definitions) NOT
structured programming.  Furthermore, this is the type of programming that
is error-prone and hard to maintain.  This type of programming ALSO includes
"fall thru" logic - so you don't even know what logic paths actually include
which procedures within their "scope".

Although Case 3 programming DOES exist - and it is often NOT worth it to
change such existing (working) code - I believe that there is general (not
universal) agreement that such code should be avoided in new code.
```

###### ↳ ↳ ↳ Re: GO TO questions

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-23T01:11:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD4C558.6E9B204B@home.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net>`

```


"Jean-Renï¿½ Duval" wrote:

> If I understand, GO TO meens bad logic. I don't thing that's always the
> case.
…[3 more quoted lines elided]…
>

Not necessarily bad logic, but see Bill's reply. Food for thought - I code in
COBOL all the time and C-A-N'-T  use 'GO TO'. Reason - I work solely in OO
COBOL classes and there isn't application of GO TO - defeats the logic of
invoking methods.

In a sense a METHOD is parallel to a PERFORM - a function that you enter,
execute, exit and return to invoker - or if you prefer, the controlling/calling
perform PARAGRAPH. This concept flows through all the other OO languages.

Jimmy, Calgary, AB
```

###### ↳ ↳ ↳ Re: GO TO questions

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-23T16:23:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net>`

```

"Jean-Ren� Duval" <jrduval@videotron.ca>
> >
> > And your dilemma is?
> Time and money.

Nah. It is an axiom of production programming that you never have time to do
it right, but you always have time to do it over.


> If I understand, GO TO meens bad logic. I don't thing that's always the
> case. But point taken. I'll keep that in mind when coding.

No, not always bad logic. Many times it's actually easier to follow GO TO
code. It's like hiring Afgans to put a new roof on your house: the
probability of roof failure is higher (but not 100%) than the probability
would be if you hired Sears.

(Note: this is but an example and not meant to denigrate or cast aspersions
on any worthless, sub-civilized, unwashed group of offal based on their
national origins nor to hold up to praise any company who proudly and
bravely occupies the biggest terrorism target in America).
```

###### ↳ ↳ ↳ Re: GO TO questions

_(reply depth: 4)_

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2001-10-23T21:16:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47lB7.29$654.15380620@newssvr30.news.prodigy.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net> <fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com>`

```
In my experience, GOTO code can be as easy to read as IF THEN ELSE END-IF
code, but not easier to read--especially whenever EXIT PARAGRAPH can be
used. Moreover, there isn't any scientific evidence, as far as I know, that
suggests GOTO logic is easier to read.

One must take extra care to produce well written GOTO code; whereas, IF THEN
ELSE END-IF logic prevents some errors that can occur in GOTO logic. Using
GOTOs, is like playing with a loaded gun, sooner or later an accident will
happen.

"JerryP" <news@bisusa.com> wrote in message
news:fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com...
>
> "Jean-Ren� Duval" <jrduval@videotron.ca>
…[8 more quoted lines elided]…
> (Note: this is but an example and not meant to denigrate or cast
aspersions
> on any worthless, sub-civilized, unwashed group of offal based on their
> national origins nor to hold up to praise any company who proudly and
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GO TO questions

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-24T15:29:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4FAC03D5A0FDDA86.42A5AAF42734DD79.520837AE8149C661@lp.airnews.net>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net> <fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com>`

```
On Tue, 23 Oct 2001 16:23:39 GMT, "JerryP" <news@bisusa.com>
enlightened us:

>
>"Jean-Renï¿½ Duval" <jrduval@videotron.ca>
…[20 more quoted lines elided]…
>

Per your note:  Did you say you lived near Houston?  First midden and
now offal?  If that's the words used in your part of Houston, and
believe me I visited Houston many times having an old college mate who
worked for Shell living there, I never discovered it :)

By the way, offal is not really the correct word to use here because
it means waste parts, especially of a butchered animal or refuse;
rubbish. (kind of like midden!).

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I live in my own little world, 
but it's OK, they know me here.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO questions

_(reply depth: 5)_

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-24T21:19:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sfGB7.17028$W87.704147@bin4.nnrp.aus1.giganews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net> <fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com> <4FAC03D5A0FDDA86.42A5AAF42734DD79.520837AE8149C661@lp.airnews.net>`

```

"SkippyPB" <swiegand@nospam.neo.rr.com>
> >
> >(Note: this is but an example and not meant to denigrate or cast
aspersions
> >on any worthless, sub-civilized, unwashed group of offal based on their
> >national origins nor to hold up to praise any company who proudly and
…[11 more quoted lines elided]…
>

Perhaps you were not part of the cultural elite of Houston. Our biggest
event is the annual Live Stock Show and Rodeo (which pulls in more visitors
in ten days that our professional sports teams do in a year (which may say
more about sports than cows)).

On "Offal," it's quite simple really: God had to do SOMETHING with the
leftovers - parts that were defective or didn't fit - (this is the
sawdust-theory of creation). Afganistan is God's midden heap, thereby
proving that every country has a place in the grand scheme of things.
```

###### ↳ ↳ ↳ Re: GO TO questions

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-25T11:02:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<205D46EDEBC9063D.B8280AF51BEE9304.8C46F3F1BB17DCEA@lp.airnews.net>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <2%DA7.1064745$ai2.80595301@bin2.nnrp.aus1.giganews.com> <AW0B7.10986$p64.1248653@wagner.videotron.net> <fQgB7.1090289$ai2.82943999@bin2.nnrp.aus1.giganews.com> <4FAC03D5A0FDDA86.42A5AAF42734DD79.520837AE8149C661@lp.airnews.net> <sfGB7.17028$W87.704147@bin4.nnrp.aus1.giganews.com>`

```
On Wed, 24 Oct 2001 21:19:20 GMT, "JerryP" <news@bisusa.com>
enlightened us:

>
>"SkippyPB" <swiegand@nospam.neo.rr.com>
…[22 more quoted lines elided]…
>

Well no I wasn't.  I lived in Dallas and that was too close to Ft.
Worth and its stockyards.  You may have got to experience the
empyreuma of cows once a year.  Living near Ft. Worth you get it year
round!

>On "Offal," it's quite simple really: God had to do SOMETHING with the
>leftovers - parts that were defective or didn't fit - (this is the
>sawdust-theory of creation). Afganistan is God's midden heap, thereby
>proving that every country has a place in the grand scheme of things.
>

I don't know about your theory about how Afghanistan was formed.  That
sounds more like New Jersey to me.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I live in my own little world, 
but it's OK, they know me here.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: GO TO questions

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2001-10-21T21:14:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EUGA7.1255$O43.595250285@newssvr11.news.prodigy.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
Both GOTOs and flags make code more difficult to read, and neither is
necessary. The increased difficulty in reading code with GOTOs and flags
increase the probability of errors when a program is modified during typical
maintenance.

On the other hand, when maintaining code one may need to rearrange
significant portions of a program to eliminate GOTOs and flags. Rewriting
large portions of code also increases the probability of error.

During maintenance, there is no absolutely best rule concerning use of GOTO
exits and flags. If it is necessary to rewrite a 1000 lines of code to avoid
one GOTO exit or one flag, it is probably better to use the GOTO or flag.

When writing new code, one should always write in the best possible style
that is consistent with corporate coding standards. Many shops encourage
GOTO exits and flags--they require an exit paragraph (unnecessary as of
COBOL 85) and an 01 FLAGS data item.

In my 35 years experience, everyone I've met agrees that GOTO should never
be used, except GOTO exit. Otherwise, style preferences differ widely.

You should ask your boss what style to use, and be skilled enough to code in
whatever style your boss requires; regardless, of how bizarre you think the
standard may be. You will be judged by both your coding prowess and your
ability to work with a group. In the eyes of management, coding style is
generally less important than cooperation, minimizing errors, and working
quickly.

"Jean-Ren� Duval" <jrduval@videotron.ca> wrote in message
news:3OBA7.931$p64.161630@wagner.videotron.net...
> Hello.
>
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?
>
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: GO TO questions

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-22T14:45:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r1bba$74s$1@peabody.colorado.edu>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <EUGA7.1255$O43.595250285@newssvr11.news.prodigy.com>`

```

On 21-Oct-2001, "Edwin Earl Ross" <EdwinEarl@yahoo.com> wrote:

> In my 35 years experience, everyone I've met agrees that GOTO should never
> be used, except GOTO exit. Otherwise, style preferences differ widely.

I know of some people who still like GO TO the top of the paragraph.  But I
know a lot more who don't like to use it even for GO TO exit.

When the next ANSI version of CoBOL is out, the argument against GO TO will
be much more compelling as EXIT PARAGRAPH will allow the functionality of GO
TO exit without the EXIT paragraph.
```

#### ↳ Re: GO TO questions

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2001-10-22T02:37:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c15aa2$4a419ba0$7619163f@chottel>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
I would suggest reading "Structured Programming with go to Statements" by
Donald Knuth published in Computing Surveys, Vol. 6, No. 4, December 1974. 
Then decide for yourself how these ideas might or might not apply to Cobol
programs.

Jean-Ren� Duval <jrduval@videotron.ca> wrote in article
<3OBA7.931$p64.161630@wagner.videotron.net>...
> Hello.
> 
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?
> 
> Another one. Do you know any places that I could find some examples on
how
> to use system variables (MVS) in a Cobol programs.
> 
…[8 more quoted lines elided]…
>
```

#### ↳ Re: GO TO questions

- **From:** "Jeff Farkas" <JeffFarkas@noland.com>
- **Date:** 2001-10-22T08:06:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r125h$qsj74$1@ID-101435.news.dfncis.de>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
> Hello.
>
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?

FWIW, I would use GO TOs as well when I'm doing some maintenance.When
doing
new code I try to avoid them but there are some times when I do toss one
in but
most of the time I avoid them like the plague.

Jeff..


> Another one. Do you know any places that I could find some examples on
how
> to use system variables (MVS) in a Cobol programs.
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: GO TO questions

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-22T14:41:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r1b37$6o2$1@peabody.colorado.edu>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```

On 21-Oct-2001, "Jean-Ren� Duval" <jrduval@videotron.ca> wrote:

> I had a discussion with a colleague about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
…[8 more quoted lines elided]…
> switch  instead ?

I don't understand.   I don't write programs with GO TO's and avoid SECTIONS
as well (but I do maintain such programs).  I don't see what difference the
length of a SECTION makes to the arguments for or against GO TO's.

I also avoid switches as much as possible, believing that they can often be
worse than the GO TO's that they were designed to eliminate.  With good
structured design, neither are necessary.   GO TO is a symptom of poorly
structured programs.  The real danger is drop down code, where logic drops
into a paragraph.  With GO TO's, this will happen.
```

#### ↳ Re: GO TO questions

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-22T15:55:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RjXA7.38317$ev2.44917@www.newsranger.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
Nothing wrong with using a GO TO.  The Compiler converts all of the code to
assembler anyway.  We don't have one program on our entire system without a GO
TO that I have found yet.  A Perform is just a GO TO with a return.  Just
because everyone else is doing somthing in a certain way is not a valid reason
to do something.  I can remember my mother saying "If everyone else jumped off a
cliff, it doesn't mean you have to!"

We don't have any real standards where I work, so I kind of had to forget
everything I learned in school to learn how to use the GO TO.  I use perform a
lot also, and prefer to use what works best in a given situation.  It actually
takes more planning and expertise to create a program with a top-down approach.
I took COBOL, RPG, and Assembly all at the same time in a single semester, and I
don't beleive any language represents the best way to do anything or any
instructor has the best idea or technique.  You can go crazy with perform
paragraphs and cause the program to jump back and forth so much that it is far
worse than using GO TO statements. Long live the GO TO.

With all of the old programs out there with the GO TO in it already, it would be
insane to remove it from the standard.  How many programs would you have to
rewrite?

On Sun, 21 Oct 2001 11:23:27 -0400, in article
<3OBA7.931$p64.161630@wagner.videotron.net>, Jean-Ren� Duval stated 
>
>Hello.
…[8 more quoted lines elided]…
>instead ?
```

##### ↳ ↳ Re: GO TO questions

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-22T16:17:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UEXA7.114487$%B.8903146@bin1.nnrp.aus1.giganews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <RjXA7.38317$ev2.44917@www.newsranger.com>`

```

On 22-Oct-2001, Charles <nospam@newsranger.com> wrote:

> Nothing wrong with using a GO TO.  The Compiler converts all of the code
> to
…[6 more quoted lines elided]…
> off a  cliff, it doesn't mean you have to!"

No.  But if everybody else wears seat belts, that isn't a reason to continue
sitting on them.

> We don't have any real standards where I work, so I kind of had to forget
> everything I learned in school to learn how to use the GO TO.  I use
…[4 more quoted lines elided]…
> approach.

Until you get a bit experience writing top-down code.  Once you have this
experience it is just as quick, if not quicker.

But the main reason for structured code is to make maintenance cheaper and
more reliable.   And I have done a LOT of maintenance of programs written by
other programmers.

> I took COBOL, RPG, and Assembly all at the same time in a single semester,
> and I
> don't believe any language represents the best way to do anything or any
> instructor has the best idea or technique.

agreed.

> You can go crazy with perform
> paragraphs and cause the program to jump back and forth so much that it is
> far worse than using GO TO statements. Long live the GO TO.

Not in any programs I have come across - but when I started, we were taught
to use the efficient ALTER statements.

> With all of the old programs out there with the GO TO in it already, it 
> would be
> insane to remove it from the standard.  How many programs would you have
> to  rewrite?

When I have worked at places where coding standards have changed, the number
of programs we have needed to rewrite to meet standards has always been
zero.   Working programs don't get rewritten for that purpose.
```

#### ↳ Re: GO TO questions

- **From:** "David E. Edwards" <dedwards@forje.btinternet.co.uk>
- **Date:** 2001-10-27T22:11:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rf82f$l8q$1@plutonium.btinternet.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net>`

```
I've promised myself for years to stay out of this type of discussion, but
what the H..!

What is a GOTO - nothing more than a branch statement.  NEVER a backward
GOTO - always forward and only to an end-of-section/exit-paragraph - much,
much better (and easier to understand) than complex, convoluted IF/ELSE
structures or performs within performs.

And Flags - have a look at C - without flags C would not function (TRUE or
FALSE?).  And what is a FILE-STATUS if it's not a Flag.  I'd like to see a
multi-file compare situation without flags - I've got a spare month or two
to read the code:-)

Dave E.

Just my tuppence worth.

"Jean-Ren� Duval" <jrduval@videotron.ca> wrote in message
news:3OBA7.931$p64.161630@wagner.videotron.net...
> Hello.
>
> I had a discussion with a colleage about that famous GO TO. He said no
> matter what the circumstances never use any GO TO because this is bad
> programming practices. In a perfect world, section coding should not
exceed
> 2 pages in length and GO TOs are useless. But in a real world, I see so
many
> programs with 4 or more pages so if I don't use GOTOs, entire sections
would
> have to be rewritten. And even when I'm coding new ones, I'm using those
> GOTO into my code. Is it a good pratice or should I use some kind of
switch
> instead ?
>
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: GO TO questions: FLAG portion of post

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2001-10-27T22:32:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDB7C32.BBAE78D8@mb.sympatico.ca>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com>`

```
"David E. Edwards" wrote:

>   I'd like to see a
> multi-file compare situation without flags - I've got a spare month or two
…[5 more quoted lines elided]…
>

Would you consider the moving of HIGH-VALUES to the comparison fields to be
using flags?  If not, then it may be possible.

PL
```

###### ↳ ↳ ↳ Re: GO TO questions: FLAG portion of post

- **From:** "David E. Edwards" <dedwards@forje.btinternet.co.uk>
- **Date:** 2001-10-31T14:15:43
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rp1a3$d2k$1@neptunium.btinternet.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <3BDB7C32.BBAE78D8@mb.sympatico.ca>`

```
I sent the following reply to Peter instead of the group, ergo I am posting
it here for those who are interested.
----------------------
"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
news:3BDB7C32.BBAE78D8@mb.sympatico.ca...
> "David E. Edwards" wrote:
>
> >   I'd like to see a
> > multi-file compare situation without flags - I've got a spare month or
two
> > to read the code:-)
> >
…[5 more quoted lines elided]…
> Would you consider the moving of HIGH-VALUES to the comparison fields to
be
> using flags?  If not, then it may be possible.
>
> PL
I'm assuming you are referring to the practice of moving high-values to key
field(s) on the input record(s)?  Well, whether you use a one byte variable
with a true/false/yes/no value or you use one of the defined record fields,
it is still a flag - an indicator of a condition.

However, many years ago, it was drummed into me that modifying the record/io
buffer for any other reason than to prepare data for storage (and then only
the output record/buffer area) was a definite no-no - which is exactly what
you are doing in this case.  Modifying the input record/buffer areas will
then require that you prepare other variable areas to retain last record key
values - now it's getting messy.

fourpence worth.

regards
Dave E.
```

###### ↳ ↳ ↳ Re: GO TO questions: FLAG portion of post

_(reply depth: 4)_

- **From:** "David E. Edwards" <dedwards@forje.btinternet.co.uk>
- **Date:** 2001-10-31T14:19:06
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rp1gc$d8i$1@neptunium.btinternet.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <3BDB7C32.BBAE78D8@mb.sympatico.ca> <9rp1a3$d2k$1@neptunium.btinternet.com>`

```
Here follows Peter Laceys reply:

"David E. Edwards" <dedwards@forje.btinternet.co.uk> wrote in message
news:9rp1a3$d2k$1@neptunium.btinternet.com...
> I sent the following reply to Peter instead of the group, ergo I am
posting
> it here for those who are interested.
> ----------------------
…[19 more quoted lines elided]…
> I'm assuming you are referring to the practice of moving high-values to
key
> field(s) on the input record(s)?  Well, whether you use a one byte
variable
> with a true/false/yes/no value or you use one of the defined record
fields,
> it is still a flag - an indicator of a condition.
>
> However, many years ago, it was drummed into me that modifying the
record/io
> buffer for any other reason than to prepare data for storage (and then
only
> the output record/buffer area) was a definite no-no - which is exactly
what
> you are doing in this case.  Modifying the input record/buffer areas will
> then require that you prepare other variable areas to retain last record
key
> values - now it's getting messy.
>
…[4 more quoted lines elided]…
>
A pinch of snuff  worth: Assuming a master file /single or multiple
transaction
file/sequential update scenario: no, not moving to the record fields
(although
my sentence did imply that).  What I have in mind is a working-storage key
field
to which the lowest of the current file keys  is moved.  I do move
high-values
to the key fields of the input files at EOF; then if the lowest key selected
turns out to be high-values then it's EOJ time.  I'm sure you do the same.

It occurs to me then: how the devil would one indicate EOF or EOJ without
some
sort of flag?  One of the files may be shorter than the others; it has to be
bypassed until EOJ.

Peter
```

###### ↳ ↳ ↳ Re: GO TO questions: FLAG portion of post

_(reply depth: 5)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-10-31T15:56:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gm38ty0.pminews@News.CIS.DFN.DE>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <3BDB7C32.BBAE78D8@mb.sympatico.ca> <9rp1a3$d2k$1@neptunium.btinternet.com> <9rp1gc$d8i$1@neptunium.btinternet.com>`

```
On Wed, 31 Oct 2001 14:19:06 -0000, David E. Edwards wrote:

>A pinch of snuff  worth: Assuming a master file /single or multiple
>transaction
…[16 more quoted lines elided]…
>
Well, I use the FILE STATUS field. Although irt could be argued that this is
an implicit switch/flag, the fact that I don't  set it reduces the
possibility of errors quite a bit.
```

###### ↳ ↳ ↳ Re: GO TO questions: FLAG portion of post

_(reply depth: 6)_

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2001-10-31T22:42:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7%D7.3494$dk1.747588774@newssvr30.news.prodigy.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <3BDB7C32.BBAE78D8@mb.sympatico.ca> <9rp1a3$d2k$1@neptunium.btinternet.com> <9rp1gc$d8i$1@neptunium.btinternet.com> <jvyyrzubevmbagrfvasbezngvpnpbz.gm38ty0.pminews@News.CIS.DFN.DE>`

```
A great technique.

"Willem Clements" <willem@horizontes-informatica.com> wrote in message

> Well, I use the FILE STATUS field. Although irt could be argued that this
is
> an implicit switch/flag, the fact that I don't  set it reduces the
> possibility of errors quite a bit.
>
>
```

##### ↳ ↳ Re: GO TO questions

- **From:** "Paul Raulerson" <praul@isot.NOSPAM.com>
- **Date:** 2001-10-28T11:18:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttofkr22enf636@corp.supernews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com>`

```

These are pretty simplistic examples of course, but if you take that into a
nasty
IF/THEN/ELSE thing (always supposing they didn't code it as a nice
structured
EVALUATE :) well... <grin>

Seriously, your points are correct, a GOTO is a branch, and one of the
biggest things
people have to learn in assembler is how to use branches correctly and
efficiently, and there
is nothing inherently evil about them. But it is a lot cleaner to think in
terms of processes and
functions in COBOL, than to think in assembler mind sets.

Mind you, almost all our products are in assembler, for speed and clean
design, but
if you really need that, then code in assembler. It is not *that* much more
difficult
than COBOL. On the other paw, if you code in COBOL, use every paradigm
available
to make your COBOL code as maintainable as possible, and depend primarly on
the compiler to do the optimizations.

IMNSHO of course. :)

-Paul



    para1.
       if EOF then GOTO para1EXIT
       process-this-and-that
       read-next-record
        at end move 'Y' to EOF-FLAG
       goback.

    para1EXIT.
       close-the-files
       goback.


vs:

    perform until EOF
       process-this-and-that
       read-next-record
         at end move 'Y' to EOF-FLAG
      end-perform
    close-the-files
    goback







"David E. Edwards" <dedwards@forje.btinternet.co.uk> wrote in message
news:9rf82f$l8q$1@plutonium.btinternet.com...
> I've promised myself for years to stay out of this type of discussion, but
> what the H..!
…[32 more quoted lines elided]…
> > Another one. Do you know any places that I could find some examples on
how
> > to use system variables (MVS) in a Cobol programs.
> >
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GO TO questions

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-29T12:20:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDD4981.C0674174@Azonic.co.nz>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <ttofkr22enf636@corp.supernews.com>`

```
Paul Raulerson wrote:
> 
>     para1.
…[18 more quoted lines elided]…
>     goback

I hope you weren't expecting these to be equivalent blocks of code.
```

###### ↳ ↳ ↳ Re: GO TO questions

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praul@isot.NOSPAM.com>
- **Date:** 2001-10-28T21:02:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttphr7a0jkdc26@corp.supernews.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <ttofkr22enf636@corp.supernews.com> <3BDD4981.C0674174@Azonic.co.nz>`

```
(*sigh*)
  Just put the perform loop in there, or a goto, whatever. I never code
goto's in
COBOL, so cut me a little slack. You are welcome to post a corrected
version. :)

-Paul

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3BDD4981.C0674174@Azonic.co.nz...
> Paul Raulerson wrote:
> >
…[21 more quoted lines elided]…
> I hope you weren't expecting these to be equivalent blocks of code.
```

###### ↳ ↳ ↳ Re: GO TO questions

- **From:** deedwards@talk21.com (David E. Edwards)
- **Date:** 2001-10-29T09:08:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ac12c47.0110290908.7324f7f8@posting.google.com>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com> <ttofkr22enf636@corp.supernews.com>`

```
Gosh, Darn, well blow me down - it's Paul Raulerson - thought you had
emigrated to Texas.
Hows it going Paul?
Nice to see you are using Flags in your example.
However your example only presents a single file read - how about 3/4
file read comparisons.

regards
Dave E.

"Paul Raulerson" <praul@isot.NOSPAM.com> wrote in message news:<ttofkr22enf636@corp.supernews.com>...
> These are pretty simplistic examples of course, but if you take that into a
> nasty
…[49 more quoted lines elided]…
> 
<SNIP>
```

##### ↳ ↳ Re: GO TO questions

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T15:32:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rjslq$2jt$1@peabody.colorado.edu>`
- **References:** `<3OBA7.931$p64.161630@wagner.videotron.net> <9rf82f$l8q$1@plutonium.btinternet.com>`

```

On 27-Oct-2001, "David E. Edwards" <dedwards@forje.btinternet.co.uk> wrote:

> I've promised myself for years to stay out of this type of discussion, but
> what the H..!
…[4 more quoted lines elided]…
> structures or performs within performs.

Certainly some GOTOs make maintenance harder than others.  I think you're
recommending that we don't allow the worst ones.

> And Flags - have a look at C - without flags C would not function (TRUE or
> FALSE?).

So you're saying that if C does it - we should or should not do it in CoBOL?

After you answer that - please tell me why should the fact that it is
necessary in C make a difference to what is a good idea in CoBOL?

> And what is a FILE-STATUS if it's not a Flag.  I'd like to see a
> multi-file compare situation without flags - I've got a spare month or two
> to read the code:-)

The trouble with flags is pretty much the same trouble with GoTOs.  It can
be hard to follow backwards.  Easily maintained flags are easy to follow
backwards, and hard to screw up.   Use system defined flags and more
importantly system set flags. Use compiler generated GOTOs.  But make it
obvious in the code what got you here and why.

Generally speaking, if you designed your code without GOTOs and without many
switches, it WILL be obvious.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
