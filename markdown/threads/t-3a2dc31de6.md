[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Evaluate readability

_32 messages · 21 participants · 2002-05 → 2002-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Evaluate readability

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-05-31T13:16:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
I recently came across the following code:

 Evaluate printSnapshot Also sendEmail
   When true also true
     move both-snapshots-and-email       to retcode
     move ' both snapshots and email'    to retcode-text
   When true also false
     move snapshots-only                 to retcode
     move ' snapshots only          '    to retcode-text
   When false also true
     move email-only                     to retcode
     move ' email only              '    to retcode-text
   When Other
     move neither-snapshots-nor-email    to retcode
     move ' neither snapshots nor email' to retcode-text
 End-Evaluate

Most programmers I have worked with have a hard time with complex Evaluate
conditions ( with ALSO's).

I found this interesting - Do you like this code or dislike this code?
```

#### ↳ Re: Evaluate readability

- **From:** "COJ" <christer.o.jonsson@home.se>
- **Date:** 2002-05-31T13:57:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad7vh3$v743e$1@ID-134254.news.dfncis.de>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
I like it alot, writes it all the time. It's very good when you should do
matrices(decision tables)

COJ

"Howard Brazee" <howard.brazee@cusys.edu> skrev i meddelandet
news:ad7sq7$kco$1@peabody.colorado.edu...
> I recently came across the following code:
>
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?
```

#### ↳ Re: Evaluate readability

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-05-31T14:11:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad800k$lhn$1@peabody.colorado.edu>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
I was thinking I would like:

EVALUATE MY-FIELD
   WHEN 'XO'
         PERFORM XO-ROUTINE
    WHEN NUMERIC
         PERFORM NUMERIC-ROUTINE
    WHEN OTHER
          PERFORM OTHER-ROUTINE
END-EVALUATE.
```

##### ↳ ↳ Re: Evaluate readability

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-31T09:54:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad82s6$5ff$1@slb6.atl.mindspring.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <ad800k$lhn$1@peabody.colorado.edu>`

```
Having I said this before <G>, ...

  Evaluate field-1
    When Numeric
         ...
     When > 3
         ...

is available today (as an extension) in some compilers and will be Standard
in the next one.
```

###### ↳ ↳ ↳ Re: Evaluate readability

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-05-31T15:29:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad84jb$ndi$1@peabody.colorado.edu>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <ad800k$lhn$1@peabody.colorado.edu> <ad82s6$5ff$1@slb6.atl.mindspring.net>`

```

On 31-May-2002, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

> Having I said this before <G>, ...
>
…[8 more quoted lines elided]…
> in the next one.

You make me so antsy waiting for the next standard to come out - and then
for my mainframe shop to find some reason to install it!!
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 4)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-06-01T03:17:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020531231726.03148.00002122@mb-da.aol.com>`
- **References:** `<ad84jb$ndi$1@peabody.colorado.edu>`

```
>From: "Howard Brazee" howard.brazee@cusys.edu 
>Date: 5/31/02 11:29 AM Eastern Daylight Time

>You make me so antsy waiting for the next standard to come out - and then
>for my mainframe shop to find some reason to install it!!
>

I second this, and third it, and so on and so on.

As for the original EVALUATE statement - well - I'm having trouble getting my
feeble brain around the 'true' 'false' thing, but I'm working at it :)   Right
now if I got called to debug that at 2am one of two things would happen 1) my
husband would awaken at 6:30 am and find a blithering idiot sitting at the
computer or 2) they police would call him because I was found wandering the
streets in a dazed state.
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 5)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2002-06-01T10:28:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020601062814.22663.00001728@mb-mg.aol.com>`
- **References:** `<20020531231726.03148.00002122@mb-da.aol.com>`

```
>From: yukonmama@aol.com  (YukonMama)
>Date: 5/31/2002 11:17 PM Eastern Daylight Time

>As for the original EVALUATE statement - well - I'm having trouble getting my
>feeble brain around the 'true' 'false' thing, but I'm working at it :)  

Code such as WHEN TRUE ALSO FALSE is the epitome of
esoteric coding.  This could only make sense to a Zen Buddhist.
Grace Hopper is rolling over in her grave.


Ross
http://community.webshots.com/user/ross_klatte
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-06-01T12:42:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ii3K8.22437$4i.2645308@bin2.nnrp.aus1.giganews.com>`
- **References:** `<20020531231726.03148.00002122@mb-da.aol.com> <20020601062814.22663.00001728@mb-mg.aol.com>`

```

"Ross Klatte" <klatteross@aol.commmm>
>
> Code such as WHEN TRUE ALSO FALSE is the epitome of
> esoteric coding.  This could only make sense to a Zen Buddhist.
> Grace Hopper is rolling over in her grave.

IF END-FILE
   AND NOT END-JOB
   ......

There, that's not so hard, is it? It's just another way of saying:

EVALUATE TRUE ALSO FALSE
   WHEN END-FILE ALSO END-JOB
   ......
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 7)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2002-06-01T15:37:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020601113750.22552.00001821@mb-mg.aol.com>`
- **References:** `<Ii3K8.22437$4i.2645308@bin2.nnrp.aus1.giganews.com>`

```
>From: "JerryMouse" nospam@invalid.com 
>Date: 2002-06-01 08:42 Eastern Daylight Time

>IF END-FILE
>   AND NOT END-JOB
…[7 more quoted lines elided]…
>

I have saved this exquisitely simple explanation.  
We have a shop standard that discourages use of the word "NOT." 
So when I need a NOT, I will simply substitute your code.  All of
the other dinosaurs will stare at me with awe.  


Ross
http://community.webshots.com/user/ross_klatte
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 8)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-06-01T19:45:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4DuK8.894$W74.184262@news20.bellglobal.com>`
- **References:** `<Ii3K8.22437$4i.2645308@bin2.nnrp.aus1.giganews.com> <20020601113750.22552.00001821@mb-mg.aol.com>`

```
"Ross Klatte" <klatteross@aol.commmm> wrote in message
news:20020601113750.22552.00001821@mb-mg.aol.com...
> >From: "JerryMouse" nospam@invalid.com
> >Date: 2002-06-01 08:42 Eastern Daylight Time
…[20 more quoted lines elided]…
>

It is rather awe inspiring, isn't it?  Almost worthy of a committee.  It
says a lot about your design effort when it takes several days and a dozen
emails to figure out what an eight word sentence actually means. I shudder
to think of an actual program.

Donald


Donald
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-06-01T19:36:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DuK8.893$W74.184337@news20.bellglobal.com>`
- **References:** `<20020531231726.03148.00002122@mb-da.aol.com> <20020601062814.22663.00001728@mb-mg.aol.com> <Ii3K8.22437$4i.2645308@bin2.nnrp.aus1.giganews.com>`

```

"JerryMouse" <nospam@invalid.com> wrote in message
news:Ii3K8.22437$4i.2645308@bin2.nnrp.aus1.giganews.com...
>
> "Ross Klatte" <klatteross@aol.commmm>
…[15 more quoted lines elided]…
>

Bah, humbug.  First you start using this true false crap.  The next think
you know, you start to use lower case, and pretty soon your not even
numbering your lines, or sticking to an 80 column format.  This young
generation has no concept of stability.

Donald
```

###### ↳ ↳ ↳ Re: Evaluate readability

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-06-02T06:00:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF9B483.6050407@optonline.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <ad800k$lhn$1@peabody.colorado.edu> <ad82s6$5ff$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:

> Having I said this before <G>, ...
> 
…[4 more quoted lines elided]…
>          ...


I don't think this is what you want. If it's numeric & > 3, you'll 
always take the Numeric case.


This is the sort of situation in which I'd code:

Evaluate 
True
When 
	(printSnapshot and sendEmail)
	process both
When 
	printSnapshot
	process Snapshot only
When 
	sendEmail
	process email only
When 
	Other
	...
End-Evaluate


I think it's a little more straightforward, more easily followed by most 
COBOLers.
```

#### ↳ Re: Evaluate readability

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-05-31T11:31:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11966306B74003A5.5E7FB3612828790A.2EC6442A4EAA6531@lp.airnews.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
On Fri, 31 May 2002 13:16:51 GMT, "Howard Brazee"
<howard.brazee@cusys.edu> enlightened us:

>I recently came across the following code:
>
…[18 more quoted lines elided]…
>I found this interesting - Do you like this code or dislike this code?

To paraphrase a saying from an old movie, "Frankly my dear, it
sucks!".  Can you imagine getting called at 2 am and having to come
into the shop and debug that statement?   Please folks..KISS

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Blessed are the flexible for they shall not be bent out of shape.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: Evaluate readability

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-05-31T16:43:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020531124344.07950.00002272@mb-fi.aol.com>`
- **References:** `<11966306B74003A5.5E7FB3612828790A.2EC6442A4EAA6531@lp.airnews.net>`

```
Steve Wiegand writes ...

>On Fri, 31 May 2002 13:16:51 GMT, "Howard Brazee"
><howard.brazee@cusys.edu> enlightened us:
…[25 more quoted lines elided]…
>into the shop and debug that statement?   Please folks..KISS

To my mind, Steve, that IS simple.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Evaluate readability

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-05-31T12:30:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<obcffu8qifgda4483c1r01ds3nd7hqc1bm@4ax.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <11966306B74003A5.5E7FB3612828790A.2EC6442A4EAA6531@lp.airnews.net>`

```
On Fri, 31 May 2002 11:31:46 -0400 SkippyPB <swiegand@neo.rr.com> wrote:

:>On Fri, 31 May 2002 13:16:51 GMT, "Howard Brazee"
:><howard.brazee@cusys.edu> enlightened us:

:>>I recently came across the following code:

:>> Evaluate printSnapshot Also sendEmail
:>>   When true also true
:>>     move both-snapshots-and-email       to retcode
:>>     move ' both snapshots and email'    to retcode-text
:>>   When true also false
:>>     move snapshots-only                 to retcode
:>>     move ' snapshots only          '    to retcode-text
:>>   When false also true
:>>     move email-only                     to retcode
:>>     move ' email only              '    to retcode-text
:>>   When Other
:>>     move neither-snapshots-nor-email    to retcode
:>>     move ' neither snapshots nor email' to retcode-text
:>> End-Evaluate

:>>Most programmers I have worked with have a hard time with complex Evaluate
:>>conditions ( with ALSO's).

:>>I found this interesting - Do you like this code or dislike this code?

:>To paraphrase a saying from an old movie, "Frankly my dear, it
:>sucks!".  Can you imagine getting called at 2 am and having to come
:>into the shop and debug that statement?   Please folks..KISS

How would you code this statement?

Are nested IFs that much more understandable?
```

###### ↳ ↳ ↳ Re: Evaluate readability

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-31T13:15:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad8ejo$qds$1@slb6.atl.mindspring.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <11966306B74003A5.5E7FB3612828790A.2EC6442A4EAA6531@lp.airnews.net> <obcffu8qifgda4483c1r01ds3nd7hqc1bm@4ax.com>`

```
Like others, I don't find anything particularly difficult with the original
code.  It *might* be clearer/more self-documenting (from a maintenance
perspective) to code:

Evaluate TRUE Also TRUE
    When printSnapshot also sendEmail
> :>>     move both-snapshots-and-email       to retcode
> :>>     move ' both snapshots and email'    to retcode-text
     When printSnapshot also NOTsendEmail
> :>>     move snapshots-only                 to retcode
> :>>     move ' snapshots only          '    to retcode-text
     When NOT sendEmailalso sendEmail
> :>>     move email-only                     to retcode
> :>>     move ' email only              '    to retcode-text
     When NOT sendEmail also NOT sendEmail
> :>>     move neither-snapshots-nor-email    to retcode
> :>>     move ' neither snapshots nor email' to retcode-text
 End-Evaluate

to *SOME* this may more accurately reflect the underlying "truth table".
(Remember that there is no "requirement" to always code a "WHEN OTHER"
clause - if logically, only one option is left)
```

#### ↳ Re: Evaluate readability

- **From:** "JamesJ. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-31T17:43:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF7B64F.ED003FB7@shaw.ca>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> I recently came across the following code:
>
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?

Like Steve I don't find the above difficult to follow - and I can't see why it
would give a maintenance programmer the eebie-jeebies at 2am <G>

It's a question of preference. I personally don't like multiple True/False
tests, keeping them simple :-

        invoke os-Collection "isEmpty" returning ls-bool
        if isTrue
            do this...
        else ...
        End-if

Reworking above code slightly, given there are four conditions from a Decision
Table :-

    Evaluate true
        when SnapshotAndEmail
            .....
        when SnapshotOnly
            ........
        when EmailOnly
            .......
        when Other (e.g. 88 = Neither )
            ........
    End-Evaluate

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Evaluate readability

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-06-01T11:39:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46EBB3BD3967E823.8428589646FBAB23.B01E3155517F14A0@lp.airnews.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <3CF7B64F.ED003FB7@shaw.ca>`

```
On Fri, 31 May 2002 17:43:00 GMT, "JamesJ. Gavan" <jjgavan@shaw.ca>
enlightened us:

>
>
…[50 more quoted lines elided]…
>Jimmy, Calgary AB

Jimmy's solution is what I was getting at.  Having not had a lot of
exposure to the ALSO statement, debugging that EVALUATE would take too
much time and I guarantee that at 2 AM I would probably not get it
right the first time.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Blessed are the flexible for they shall not be bent out of shape.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Evaluate readability

- **From:** "Schroeder" <jfriedman@nc.rr.com>
- **Date:** 2002-05-31T23:57:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D5UJ8.22308$lM2.592393@twister.southeast.rr.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
Actually, I only think it really poor depending on where it came from.  The
Evaluate verb was (partly) designed to implement  decision tables.  If this
was automatically generated from a table, keeping it in sync with the table
makes a lot of sense.   But since that was probably not the case, I guess I
side with all of you who had something negative to say about it! <g>

Partial-expressions in Evaluate (in the next Standard) is going to help the
evaluate statement a LOT.

Jeff Friedman





"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:ad7sq7$kco$1@peabody.colorado.edu...
> I recently came across the following code:
>
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?
```

#### ↳ Re: Evaluate readability

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-01T07:40:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF86C50.A5FB2219@Azonic.co.nz>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
>  Evaluate printSnapshot Also sendEmail
>    When true also true
>      move both-snapshots-and-email       to retcode
>      move ' both snapshots and email'    to retcode-text
...
>  End-Evaluate
 
> I found this interesting - Do you like this code or dislike this code?

It is a decision table coded as an evaluate. Having used decision tables
some decades ago with pre-processors I find that evaluates tables such
as this are 'sideways'.  If pre-processors were still around, or I could
be bothered writing one, then I might use a real decision table, but I
usually find that nested evaluates are more understandable than single
combined ones.

Of corse in this case where there are only a few options and the action
is entirely repetitive I would probably do it in a data table.  If the
text descriptions were actually used, for example in printing an
invoice, then I would put these into my 'decode file' where the user can
maintain them.  The evaluate would then degrade to:

         MOVE "REQUIRED"       TO Decode-Field
         MOVE Required-Flags   TO Decode-Key
         PERFORM Decode
         MOVE Decode-Text      TO RetCode-Text
         MOVE Decode-Flag      TO Retcode

'Decode' basically does an index file read on a key that concatenates
the 'field' and 'key'.  Many small items fit into one file that in my
systems is always open.  The file is maintained by one program that gets
the record layout for each 'field' from a control file.

In this particular case the decode may also contain the charge to apply
for sending the EMail and/or Snapshots.
```

#### ↳ Re: Evaluate readability

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-06-02T18:46:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cfb34a8_5@Usenet.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
In my opinion this is junk.

The condition names are good, but the Evaluate is too convoluted. I believe
Evaluates with ALSO are best avoided...(I have NEVER used ALSO in an
Evaluate)...

As I like general solutions, I have one for such instances. I have used it
for the past 30 years with great success in both High and Low Level
Languages.

The problem can be stated as:

1. A number of conditions must be detected which are non-mutually exclusive
and non-implicative. In other words, they are not dependent on each other (P
does NOT imply Q) and if any one is true, it does NOT preclude ANY others
being true (In this case, there are 2 such conditons, plus the "boundary
condition" that nothing is true.)

2. Any number of them may be true at any given time. (In this case, UP to
2...)

As 2 is a fairly trivial quantity, let's demonstrate with 4. I'll call them
C1 thru C4 and you can substitute any conditions you like that meet the
above constraints.

Here's my code for the same "problem"...

(set up a field in WS called truthValue. It has to hold a number and will be
involved in arithmetic, so, after carefully reading all the threads on
efficiency posted in CLC over the past 5 years, make it floating point...
<G> No, it should be whatever is most efficient on your machine IF YOU CARE
ABOUT THAT SORT OF THING! (It is not for me to say whether you should or
shouldn't care about that sort of thing, any more than it is my place to
tell you whether you should care about the rainforest, or regularly changing
your underwear...))

In my environment it is a field called truthValue defined as PIC s9(4)
comp-5. (On the mainframe I'd use a halfword...)
...
move zero to truthValue
if C1 move 1 to truthValue end-if
if C2 move 2 to truthValue end-if
if C3 move 4 to truthValue end-if
if C4 move 8 to truthValue end-if
evaluate truthValue
     when 0
            *> nothing is true...
     when 1
            *> C1 ONLY is true
     when 2
            *> C2 ONLY is true
     when 3
            *> C1 AND C2 are true

Note: This would be the extent required for the example given. (Exactly the
same number of WHENs but ALSO is not required)...

     when 4
            *> C3 ONLY is true
     when 5
            *> C3 AND C1 are true
     when 6
            *> C3 AND C2 are true
     when 7
            *> C3 AND C2 AND C1are true
     when 8
            *> C4 ONLY is true
     when 9
            *> C4 AND C1 are true
     when 10
            *> C4 AND C2 are true
     when 11
            *> C4 AND C2 AND C1 are true
     when 12
            *> C4 AND C3 are true
     when 13
            *> C4 AND C3 AND C1 are true
     when 14
            *> C4 AND C3 AND C2 are true
     when 15
            *> C4 AND C3 AND C2  AND C1 are true    (ALL conditions true)
     when other
            *>  there was an internal haemhorrage and the CPU lies broken
and bleeding...
            *> the state of your conditions
            *> pales into insignificance as you realise the machine is not
insured and your last
            *> backup was just before the Millennium party...
end-evaluate
(You should arrange your WHEN clauses in the order of what is most likely,
rather than numerical sequence, given that you KNOW which combinations are
most likely and given that you CARE... (see above).)

This is a relatively simple way of handling a number of conditions without
going to the overhead of decision tables (although I reckon these are
excellent for complex decisions, PROVIDED there has been a Boolean
Simplification of the conditions before they are loaded to the decision
tables...but that's another story...).

The most valuable use I found for this technique was in the old days when we
needed to update/merge multiple sequential files against a Master (the
classic 3-way-split operation). It was very useful to control what was
"high" in the various 3-way-splits of the files against each other and the
Master... I liked it because you could do a bunch of key compares, then
split to the correct processing without having to do multiple in-line
3-way-splits. Then they went and spoiled it all by inventing disk drives
<G>....

Pete.

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:ad7sq7$kco$1@peabody.colorado.edu...
> I recently came across the following code:
>
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Evaluate readability

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-06-03T10:33:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cfb35dd_3@Usenet.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <3cfb34a8_5@Usenet.com>`

```
oops!


Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3cfb34a8_5@Usenet.com...
> In my opinion this is junk.
>
> The condition names are good, but the Evaluate is too convoluted. I
believe
> Evaluates with ALSO are best avoided...(I have NEVER used ALSO in an
> Evaluate)...
…[7 more quoted lines elided]…
> 1. A number of conditions must be detected which are non-mutually
exclusive
> and non-implicative. In other words, they are not dependent on each other
(P
> does NOT imply Q) and if any one is true, it does NOT preclude ANY others
> being true (In this case, there are 2 such conditons, plus the "boundary
…[5 more quoted lines elided]…
> As 2 is a fairly trivial quantity, let's demonstrate with 4. I'll call
them
> C1 thru C4 and you can substitute any conditions you like that meet the
> above constraints.
…[3 more quoted lines elided]…
> (set up a field in WS called truthValue. It has to hold a number and will
be
> involved in arithmetic, so, after carefully reading all the threads on
> efficiency posted in CLC over the past 5 years, make it floating point...
> <G> No, it should be whatever is most efficient on your machine IF YOU
CARE
> ABOUT THAT SORT OF THING! (It is not for me to say whether you should or
> shouldn't care about that sort of thing, any more than it is my place to
> tell you whether you should care about the rainforest, or regularly
changing
> your underwear...))
>
…[3 more quoted lines elided]…
> move zero to truthValue

The following MOVEs should be ADDs of course...very tired and in a hurry.

> if C1 move 1 to truthValue end-if
> if C2 move 2 to truthValue end-if
…[12 more quoted lines elided]…
> Note: This would be the extent required for the example given. (Exactly
the
> same number of WHENs but ALSO is not required)...
>
…[42 more quoted lines elided]…
> The most valuable use I found for this technique was in the old days when
we
> needed to update/merge multiple sequential files against a Master (the
> classic 3-way-split operation). It was very useful to control what was
…[27 more quoted lines elided]…
> > Most programmers I have worked with have a hard time with complex
Evaluate
> > conditions ( with ALSO's).
> >
…[8 more quoted lines elided]…
>                 http://www.usenet.com



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Evaluate readability

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2002-06-19T01:46:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oRP8.30730$uk2.13022908@twister.nyroc.rr.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
Can I have comments on another approach. I, also, am not that comfortable
with ALSO.

What do people think of this? Is this bad, since, in the second and third
WHENs, it may not be obvious the first one (as a whole) is false?

Evaluate true
   When printSnapshot AND sendEmail
     move both-snapshots-and-email       to retcode
     move ' both snapshots and email'    to retcode-text
   When printSnapshot    (===>SendEmail must be false if you are here)
     move snapshots-only                 to retcode
     move ' snapshots only          '    to retcode-text
   When sendEmail          (===>printSnapshot must be false if you are here)
     move email-only                     to retcode
     move ' email only              '    to retcode-text
   When Other
     move neither-snapshots-nor-email    to retcode
     move ' neither snapshots nor email' to retcode-text
 End-Evaluate



"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:ad7sq7$kco$1@peabody.colorado.edu...
> I recently came across the following code:
>
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?
```

##### ↳ ↳ Re: Evaluate readability

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-19T04:48:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D100D70.A81D5105@shaw.ca>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <4oRP8.30730$uk2.13022908@twister.nyroc.rr.com>`

```


William Bub wrote:

> Can I have comments on another approach. I, also, am not that comfortable
> with ALSO.
…[17 more quoted lines elided]…
>  End-Evaluate

Now your option is one I could probably have a problem with at either 2am or 2pm
<G>. But, with a qualifier. If your lines with "===>" were in fact comments "*>"
then I could grudgingly live with it - but in the wee small hours the
maintenance programmer still has to read your comments to get the hang of it..

However, there's another aspect - what if it was 8 or 16 conditions ? Plus what
we haven't discussed - frequency  (Pareto - 20% of conditions account for 80% of
the actions). Given that there was a genuine need to put them in descending, by
'highest frequency', I can see your approach might well run into trouble. Given
8 or 16 conditions, they could of course be nested Evaluates.

In summary - Nah ! Don't like it ! <G>

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Evaluate readability

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-19T12:02:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p_P8.64158$uX3.4235@nwrddc01.gnilink.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <4oRP8.30730$uk2.13022908@twister.nyroc.rr.com>`

```
William Bub <fathafluff@hotmail.com> wrote in message
news:4oRP8.30730$uk2.13022908@twister.nyroc.rr.com...
> Can I have comments on another approach. I, also, am not that comfortable
> with ALSO.
…[7 more quoted lines elided]…
>    When sendEmail          (===>printSnapshot must be false if you are
here)
>    When Other
>  End-Evaluate

In general  I do not like source code which relies on "negative" testing;
i.e, "if you get here, (condition) must be (whatever)".  I much prefer
explicit "positive" tests.....

Assuming I went this way, just for readability I'd probably use...

 Evaluate true
    When printSnapshot    AND sendEmail
    When printSnapshot    AND NOT SendEmail
    When sendEmail         AND NOT PrintSnapshot
   When Other
  End-Evaluate

.. which of course, leads right back to ALSO.

MCM
```

###### ↳ ↳ ↳ Re: Evaluate readability

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-06-19T14:29:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2CE237F5B7F79C01.E362855C0B8349E0.E0EE2D925E3F6A8F@lp.airnews.net>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <4oRP8.30730$uk2.13022908@twister.nyroc.rr.com> <5p_P8.64158$uX3.4235@nwrddc01.gnilink.net>`

```
On Wed, 19 Jun 2002 12:02:09 GMT, "Michael Mattias"
<michael.mattias@gte.net> enlightened us:

>William Bub <fathafluff@hotmail.com> wrote in message
>news:4oRP8.30730$uk2.13022908@twister.nyroc.rr.com...
…[30 more quoted lines elided]…
>
Programmer tastes are like snowflakes...

Anyway I like the original because I don't like the use of NOT
especially in an AND statement.  The original was very understandable
to me (especially if the comments were taken off of the coding lines)
and so is Michael's, but if it were me doing the coding I would have
probably done it as it was shown in the original post.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Smoking kills. If you're killed, you've lost a very 
important part of your life."  - Brooke Shields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Evaluate readability

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-06-22T00:02:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0206212302.1ad623cd@posting.google.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
I use this all the time.  In fact, I wrote an article about it for
"Enterprise Systems Journal" in 1997.  One thing I recommend is LINE
UP THE CODE ELEMENTS.  It makes it much more readable, particularly if
there are more elements than this example.  If the lines get too long,
the new standard will let you code beyond column 72. (The devil made
me say it!  I've been opposing the new formats since I joined the
Committee!)

  Evaluate printSnapshot Also sendEmail
    When   true          also true
      move both-snapshots-and-email       to retcode
      move ' both snapshots and email'    to retcode-text
    When   true          also false
      move snapshots-only                 to retcode
      move ' snapshots only          '    to retcode-text
    When   false         also true
      move email-only                     to retcode
      move ' email only              '    to retcode-text
    When Other
      move neither-snapshots-nor-email    to retcode
      move ' neither snapshots nor email' to retcode-text
  End-Evaluate
  
This is standard syntax, not a cutesy-poo kludge.  Anyone who has
trouble with this code at 2am is not yet a professional COBOL
programmer.

Stephen J Spiro
J4 COBOL Stabdards Committee

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:<ad7sq7$kco$1@peabody.colorado.edu>...
> I recently came across the following code:
> 
…[18 more quoted lines elided]…
> I found this interesting - Do you like this code or dislike this code?
```

#### ↳ Re: Evaluate readability

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-06-26T10:12:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B93F442B0110CA3610E07880@news-east.usenetserver.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
On Fri, 31 May 2002 9:16:51 -0400, Howard Brazee wrote
> I recently came across the following code:
> 
>  Evaluate printSnapshot Also sendEmail

I too like ALSO, but I have found that the typical COBOL programmer 
does not.

And despite the power for implementing decision tables, I have found 
that the EVALUATE which I use most often -- even when I'm following my 
own nose -- is EVALUATE TRUE. Far too many actual problems involve 
messy and overlapping conditions which must be tested sequentially, and 
the decision table model does not fit these well. When I last taught 
COBOL74->85 update, I spent some time on decision tables. On the next 
iteration, I will replace this with rules-based programming (see 
below).

Interestingly, in my rather small experience in the matter, I've found 
that it's the older COBOL programmers who know decision tables, or 
perhaps the ones who've been trained in business analysis rather than 
just COBOL.

Any EVALUATE can be rewritten as EVALUATE TRUE, although it often 
becomes quite a bit wordier and (to me) less understandable. But at 
least typical COBOL programmers are delighted with EVALUATE data-name, 
and accept EVALUATE TRUE as preferable to what was used in COBOL74.

I have no objection at all to WHEN TRUE ALSO FALSE, and I think that 
any COBOL programmer who takes the time to become familiar with it will 
follow it easily. EVALUATE TRUE ALSO FALSE is a different matter, and I 
would use it only in very limited, formal contexts with lots of 
explanation. Of course, EVALUATE FALSE used to avoid writing NOT is 
simply a game -- it only avoids the word NOT; it fails to avoid the 
kind of logic that some COBOL programmers find problematic and is even 
harder to follow than a simple NOT.

I have also found, in converting a lot of COBOL74 to COBOL85, that I 
can often take complex, convoluted, nearly impenetrable, sometimes 
nested IF statements and convert them to a simple list of WHENs. This 
gets into the area of rules-based programming. I think that all COBOL 
programmers ought to be exposed to rules-based programming, simply 
because (like decision tables) it arises so often in the application 
domains where COBOL is commonly used. The ease and clarity of 
implementing a set of rules with EVALUATE -- even just EVALUATE TRUE -- 
just reinforces this as a good idea.

As far as professional programmers, the fact is that many -- perhaps 
most -- COBOL programmers are not professional programmers in any 
strong sense of the word. The good ones are mostly generalists -- they 
know some COBOL, some programming, a good bit about their agency's 
function and operation, a good bit about the logic of the systems they 
work with, something about their organization and its people, etc. It 
would be ideal if they were experts in everything, but we have to 
respect the environment in which they actually work.

Edward Reid
```

##### ↳ ↳ Re: Evaluate readability

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-06-27T00:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c21d73$d044a780$da95f243@chottel>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <01HW.B93F442B0110CA3610E07880@news-east.usenetserver.com>`

```
Can you give us some references to good info on rules base programming? 
Thanks.

Edward Reid <edwardreid@spamcop.net> wrote in article
<01HW.B93F442B0110CA3610E07880@news-east.usenetserver.com>...
> On Fri, 31 May 2002 9:16:51 -0400, Howard Brazee wrote
> > I recently came across the following code:
…[56 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Evaluate readability

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-06-27T11:32:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B940A85001646B9A10E07880@news-east.usenetserver.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <01HW.B93F442B0110CA3610E07880@news-east.usenetserver.com> <01c21d73$d044a780$da95f243@chottel>`

```
On Wed, 26 Jun 2002 20:45:34 -0400, Charles Hottel wrote
> Can you give us some references to good info on rules base programming? 

The term "rule based programming" (rather than "rules") seems to be the 
norm. I googled it and found lots of references, including a lot of 
commercial products, but no good introduction. The best article seems 
to be

  Rule-based Systems, by Frederick Hayes-Roth, Communications
  of the ACM, Sept 1985 (v28 n9) p921.

It's available on the ACM Digital Library (http://www.acm.org). I'm not 
sure whether just ACM membership is enough to access it (since it's in 
CACM, which all members receive) or if you have to buy the Digital 
Library add-on. Since the PDF version is technically restricted, I 
can't make a public offer to email it to you.

Rule-based programming is a lot more than I was talking about, and 
complete rule based systems don't look like procedural programming at 
all. In particular, it includes storage of facts as well as rules, and 
the concept of an inference engine which analyzes rules and enables 
complex inferences. I was talking -- and rather loosely at that -- 
about the simpler case where you have a list of rules -- conditions and 
actions:

  IF this THEN do that
  IF the-other THEN do something-else

and you pick the first that applies. Quite similar to decision tables 
when you drop the inference part.

The piece of the concept that I was picking up was, it's a lot simpler 
to follow and modify the program (business and COBOL) if you simply 
have a one-layer list of rules explaining what to do in each case. Once 
you nest the decisions, it's harder to follow what's happening, and 
often a LOT harder to modify. As with decision tables, you restrict and 
simplify the structure, and if properly applied then this simplifies 
the tasks of program creation, understanding, and modification.

So I really took a small part of the rule-based concept and applied it 
to COBOL usage patterns.

Edward
```

###### ↳ ↳ ↳ Re: Evaluate readability

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-06-28T01:39:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c21e44$7fead120$fe95f243@chottel>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu> <01HW.B93F442B0110CA3610E07880@news-east.usenetserver.com> <01c21d73$d044a780$da95f243@chottel> <01HW.B940A85001646B9A10E07880@news-east.usenetserver.com>`

```
Thanks I think I can look at the article  in a local university library.



Edward Reid <edwardreid@spamcop.net> wrote in article
<01HW.B940A85001646B9A10E07880@news-east.usenetserver.com>...
> On Wed, 26 Jun 2002 20:45:34 -0400, Charles Hottel wrote
> > Can you give us some references to good info on rules base programming?

> 
> The term "rule based programming" (rather than "rules") seems to be the 
…[12 more quoted lines elided]…
> 
<snip>
```

#### ↳ Re: Evaluate readability

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2002-07-10T00:19:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O4LW8.113101$vq.5554576@bin6.nnrp.aus1.giganews.com>`
- **References:** `<ad7sq7$kco$1@peabody.colorado.edu>`

```
In article <ad7sq7$kco$1@peabody.colorado.edu>, howard.brazee@cusys.edu 
wrote:

>I recently came across the following code:
>
…[4 more quoted lines elided]…
>I found this interesting - Do you like this code or dislike this code?

While I get the gist of it, I don't believe one should ever use Evaluate
statements like that. I think it's better style to use IF statements 
or perform statements embeded witin it, or replace the whole thing
with nested IF-THEN statements.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
