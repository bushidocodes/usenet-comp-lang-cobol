[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "EXIT Immediate" from the middle of a Procedure

_27 messages · 18 participants · 1999-02 → 1999-03_

---

### "EXIT Immediate" from the middle of a Procedure

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com>`

```
I have checked my "saved" and "sent" folders as well as DejaNews and can't
find the summary that I did a few months ago on ways to get out of the
middle of  a procedure "ASAP".  Did anyone else either save it or can you
find it in DejaNews?  This seems to be coming up often enough that I thought
I would repost it.  A semi-short summary of it (without all the PROs and
CONs) is:

A) It is quite common that you are able to detect a situation "early" in a
Procedure (Paragraph, Section, whatever) that causes you to want to "get
out" and not do anything else in that procedure.

B) There are a NUMBER of ways of doing this; which one you use will depend
on your "religious" beliefs and/or shop Standards.  They all work; they are
all maintainable; and any attempt to "mix" them leads to difficult to
maintain code.  (Everyone seems to think that there method is LESS
error-prone that the others - but when "pressed" this is only true if you
try to mix methods or coding techniques)

C)  The (most?) common methods are:

1) Use the EXIT PARAGRAPH/SECTION syntax which is an extension in many
compilers today and will be in the next COBOL Standard.

2) Use "native" COBOL syntax to keep nesting levels of conditionals, e.g.

    Read ...
        At End
            do at end processing - but nothing else
       Not at End
           do normal processing
           If condition-1
                 do fairly common stuff
           Else
                 do less common stuff
           End-IF
           Do more normal processing
    End-Read

3) (Particularly with pre-ANS'85 compilers), break out your code into
separate Paragraphs whenever you hit a new condition, e.g.  In pre-ANS'85
you can't have

   If cond-1
      If Cond-2
            Do X
      Else
            Do Y
      End-IF
     Display  "how do I get here?"
  Else
     Do Z
  End-IF

Therefore, you need to move the "If Cond-2" thru its End-IF to a separate
paragraph and PERFORM it.

4) The ever controversial PERFORM THRU with a GO TO exit-paragraph,  In
other words, for every paragraph (and you need either manual or automated
tools/standards to enforce this) you code an EXIT-Paragraph.  You never
allow any other paragraph labels between an "opening" and "exit" paragraph
label - but you do allow GO TO exit-paragraph syntax when you want to "get
out quick".  (no other GO TOs or "crossing" GO TOs are allowed)

5) Variation on 4 (seemingly most popular in England), you don't ever
PERFORM paragraph thru paragraph-exit, but do PERFORM SECTIONs.  Then within
a section you have 1 paragraph and its exit, so you can again go to that
paragraph-exit.


   *****

OK, regulars, have I forgotten anything (again?)
```

#### ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** "Simon Cordingley" <simonc@casegen.co.uk>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c204c6.0@mercury.nildram.co.uk>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com>`

```
Seems pretty complete to me - didn't know about EXIT PARAGRAPH though, only
thought you could EXIT SECTION - look forward to it being in the standard so
we can use it in Casegen (we pretty much stick to very simple ANSI '85
syntax).

Strange you should mention "England" in your last possibility - that's what
we do in Casegen and we are definitly from the European side of the pond.

Thanks for your informative posting.

Simon Cordingley
Casegen Systems Ltd
www.casegen.co.uk


William M. Klein wrote in message <79sni8$6a0@dfw-ixnews12.ix.netcom.com>...
>I have checked my "saved" and "sent" folders as well as DejaNews and can't
>find the summary that I did a few months ago on ways to get out of the
>middle of  a procedure "ASAP".  Did anyone else either save it or can you
>find it in DejaNews?  This seems to be coming up often enough that I
thought
>I would repost it.  A semi-short summary of it (without all the PROs and
>CONs) is:
…[58 more quoted lines elided]…
>PERFORM paragraph thru paragraph-exit, but do PERFORM SECTIONs.  Then
within
>a section you have 1 paragraph and its exit, so you can again go to that
>paragraph-exit.
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** Ian Glen <glenirxxx@xxerols.com>
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C3AC60.B6D6A7A7@xxerols.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <36c204c6.0@mercury.nildram.co.uk>`

```
Rexx provides 2 ways out of the middle of a loop  - 'leave' which exits
the loop to the next instruction, and 'iterate', which resumes from the
beginning of the loop. 

The only cobol equivalent of 'iterate' that comes close would be a 'GO
TO start-paragraph' - I don't think there is anything equivalent for an
inline PERFORM - does anyone else think that they would have a use for
the 'iterate' instruction?

IG

Simon Cordingley wrote:
> 
> Seems pretty complete to me - didn't know about EXIT PARAGRAPH though, only
…[93 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1999-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a2qdp$s4n@dfw-ixnews11.ix.netcom.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <36c204c6.0@mercury.nildram.co.uk> <36C3AC60.B6D6A7A7@xxerols.com>`

```
This is the exact difference between EXIT PERFORM with and without the
"CYCLE" keyword.


Ian Glen wrote in message <36C3AC60.B6D6A7A7@xxerols.com>...
>Rexx provides 2 ways out of the middle of a loop  - 'leave' which exits
>the loop to the next instruction, and 'iterate', which resumes from the
…[11 more quoted lines elided]…
>> Seems pretty complete to me - didn't know about EXIT PARAGRAPH though,
only
>> thought you could EXIT SECTION - look forward to it being in the standard
so
>> we can use it in Casegen (we pretty much stick to very simple ANSI '85
>> syntax).
>>
>> Strange you should mention "England" in your last possibility - that's
what
>> we do in Casegen and we are definitly from the European side of the pond.
>>
…[6 more quoted lines elided]…
>> William M. Klein wrote in message
<79sni8$6a0@dfw-ixnews12.ix.netcom.com>...
>> >I have checked my "saved" and "sent" folders as well as DejaNews and
can't
>> >find the summary that I did a few months ago on ways to get out of the
>> >middle of  a procedure "ASAP".  Did anyone else either save it or can
you
>> >find it in DejaNews?  This seems to be coming up often enough that I
>> thought
…[3 more quoted lines elided]…
>> >A) It is quite common that you are able to detect a situation "early" in
a
>> >Procedure (Paragraph, Section, whatever) that causes you to want to "get
>> >out" and not do anything else in that procedure.
>> >
>> >B) There are a NUMBER of ways of doing this; which one you use will
depend
>> >on your "religious" beliefs and/or shop Standards.  They all work; they
are
>> >all maintainable; and any attempt to "mix" them leads to difficult to
>> >maintain code.  (Everyone seems to think that there method is LESS
>> >error-prone that the others - but when "pressed" this is only true if
you
>> >try to mix methods or coding techniques)
>> >
…[5 more quoted lines elided]…
>> >2) Use "native" COBOL syntax to keep nesting levels of conditionals,
e.g.
>> >
>> >    Read ...
…[13 more quoted lines elided]…
>> >separate Paragraphs whenever you hit a new condition, e.g.  In
pre-ANS'85
>> >you can't have
>> >
…[11 more quoted lines elided]…
>> >Therefore, you need to move the "If Cond-2" thru its End-IF to a
separate
>> >paragraph and PERFORM it.
>> >
>> >4) The ever controversial PERFORM THRU with a GO TO exit-paragraph,  In
>> >other words, for every paragraph (and you need either manual or
automated
>> >tools/standards to enforce this) you code an EXIT-Paragraph.  You never
>> >allow any other paragraph labels between an "opening" and "exit"
paragraph
>> >label - but you do allow GO TO exit-paragraph syntax when you want to
"get
>> >out quick".  (no other GO TOs or "crossing" GO TOs are allowed)
>> >
…[15 more quoted lines elided]…
>> >
```

#### ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79t079$258$1@news.igs.net>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com>`

```
looks to me like you have them covered ...

William M. Klein wrote in message <79sni8$6a0@dfw-ixnews12.ix.netcom.com>...
>I have checked my "saved" and "sent" folders as well as DejaNews and can't
>find the summary that I did a few months ago on ways to get out of the
>middle of  a procedure "ASAP".  Did anyone else either save it or can you
>find it in DejaNews?  This seems to be coming up often enough that I
thought
>I would repost it.  A semi-short summary of it (without all the PROs and
>CONs) is:
…[58 more quoted lines elided]…
>PERFORM paragraph thru paragraph-exit, but do PERFORM SECTIONs.  Then
within
>a section you have 1 paragraph and its exit, so you can again go to that
>paragraph-exit.
…[10 more quoted lines elided]…
>
```

#### ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** denis548@aol.com (Denis548)
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990214090348.09998.00001408@ng29.aol.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com>`

```
>I have checked my "saved" and "sent" folders as well as DejaNews and can't
>find the summary that I did a few months ago on ways to get out of the
>middle of  a procedure "ASAP".  Did anyone else either save it or can you
>find it in DejaNews?  This seems to be coming up often enough that I thought
>I would repost it.  

I worked for a software development company for years and here's what we
settled over time:  PERFORM through an exit if you need to "bail out in the
middle".   This is the rough equivalent of the "return" in some languages.  

Also we allowed a "GO TO" to only go to the top of the paragraph.  This is the
equivalent of "continue" in a while loop in some languages.

Denis
```

##### ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C842A8.FBB26F70@NOSPAMhome.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com>`

```
> Also we allowed a "GO TO" to only go to the top of the paragraph.  This is the
> equivalent of "continue" in a while loop in some languages.
> 
> Denis

I would be very reluctant to GO TO the top of a performed paragraph.  I
don't have confidence that any increments and checks would be done
correctly.  Testing would mean that it would work correctly for this
particular compile, but maybe not when we upgrade compilers.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vP%x2.6593$wj1.9765393@news2.mia>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com>`

```
Howard Brazee wrote:
>
>I would be very reluctant to GO TO the top of a performed paragraph.

I can understand that.

>I don't have confidence that any increments and checks would be done
>correctly.  Testing would mean that it would work correctly for this
>particular compile, but maybe not when we upgrade compilers.

Oh, Howard, come on now, that's pretty lame. :-)  Are you *really*
worried that a new compiler might not compile a GO TO correctly? ;-)
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C88E7B.6186E498@NOSPAMhome.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[10 more quoted lines elided]…
> worried that a new compiler might not compile a GO TO correctly? ;-)

I see your smileys, but want to clarify - it's the PERFORM which would
be more likely to break if it has a GOTO within it.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 5)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990215172820.07685.00001563@ng156.aol.com>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com>`

```
Now, class, we have a pop quiz.

It would appear that we have had here in this innocent thread a clear
recordation of the concerns, felt mutually, of two very informed
prognosticators to the effect that should there be a mixture of GOTO and
PERFORM of the particular variety of a GOTO to the top paragraph name that
there could be a breakage, as it were, betwixt releases of the compiler.

In particular, the iterative functionality latent in PERFORM may be
dysfunctionalized by such a jump.  There was humorously a disagreement as to
whether this would be a break of the GOTO or a break of the PERFORM, (surely
that is expertise instantiated).

Now it must be agreed that the iterator is actaully a transparent piece of code
that is in there somewhere between the header and whatever might be considered
the end, and the august postors are concerned that this iterator might, oh
heaven forbid, be skipped by a precociously executed GO-of-some-sort. Oh,
anything but that!

For 'tis true as the great commentors have so implied that an implementor, be
they the great blue or the littlest language deployer, is free to implement
that iterator in the way they choose and in a manner fitting to the device
where implemented, as long as they stick to the language syntax rules.

So, ..., class, for extra extra super extra credit, beyond the holding capacity
of the largest numeric field, I mean in outright overflow of the shear capacity
to calculate, please write an entry suitable for posting on the internet
itself, commenting as to whether you feel that it  is not by these very same
tokens of admonitions that we mighten not take cognizance of the fact that the
exact locus of an iterator in a structure coded as the object of a PERFORM 1-a
THRU 1-exit is syntactically undefined.

Comment to the effect, think you not, that a GOTO the 1-exit is just as 'risky'
since we have no language standard stating the location of the iterator.  

And since, in most of the interesting discussions the 1-exit paragraph is, of
course, recommended to contain nothing except the EXIT statement, which
statement is guaranteed to do nothing as a matter of language standard, then
could not the implementor place the iterator just nigh of the 1-exit label?  

And could not the arguements presented to dissuade coders from expressing the
GOTO top paragraph construct be, perforce, presented in opposition to the GOTO
1-exit, when in the same context these same sources insist that  1-exit be void
of code? 

So, class, the point might be that the advocacy of GOTO 1-exit depends utterly
upon an experts knowledge of implementation details, and that implementors are
now limitted by the practices in the field, not by the approved or documented
language standard.

In contradistinction to the foregoing comments in this thread the proposition
is that a GOTO begining, can not be more offensive than GOTO ending. If the
expert tells you that the iterator, about which only the greatest minds could
be informed, might be damaged by a non-linear jump, then it must be true no
matter which direction you jump.


Best Wishes for those who jump not at all,
 

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C8AA10.AD376143@NOSPAMhome.com>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com>`

```
I've read your code!!!!

RKRayhawk wrote:
> 
> Now, class, we have a pop quiz.
…[59 more quoted lines elided]…
> RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aajeo$5ge$1@news.igs.net>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com>`

```
GOTO ...  <G>

RKRayhawk wrote in message <19990215172820.07685.00001563@ng156.aol.com>...
>Now, class, we have a pop quiz.
>
…[7 more quoted lines elided]…
>dysfunctionalized by such a jump.  There was humorously a disagreement as
to
>whether this would be a break of the GOTO or a break of the PERFORM,
(surely
>that is expertise instantiated).
>
>Now it must be agreed that the iterator is actaully a transparent piece of
code
>that is in there somewhere between the header and whatever might be
considered
>the end, and the august postors are concerned that this iterator might, oh
>heaven forbid, be skipped by a precociously executed GO-of-some-sort. Oh,
>anything but that!
>
>For 'tis true as the great commentors have so implied that an implementor,
be
>they the great blue or the littlest language deployer, is free to implement
>that iterator in the way they choose and in a manner fitting to the device
>where implemented, as long as they stick to the language syntax rules.
>
>So, ..., class, for extra extra super extra credit, beyond the holding
capacity
>of the largest numeric field, I mean in outright overflow of the shear
capacity
>to calculate, please write an entry suitable for posting on the internet
>itself, commenting as to whether you feel that it  is not by these very
same
>tokens of admonitions that we mighten not take cognizance of the fact that
the
>exact locus of an iterator in a structure coded as the object of a PERFORM
1-a
>THRU 1-exit is syntactically undefined.
>
>Comment to the effect, think you not, that a GOTO the 1-exit is just as
'risky'
>since we have no language standard stating the location of the iterator.
>
>And since, in most of the interesting discussions the 1-exit paragraph is,
of
>course, recommended to contain nothing except the EXIT statement, which
>statement is guaranteed to do nothing as a matter of language standard,
then
>could not the implementor place the iterator just nigh of the 1-exit label?
>
>And could not the arguements presented to dissuade coders from expressing
the
>GOTO top paragraph construct be, perforce, presented in opposition to the
GOTO
>1-exit, when in the same context these same sources insist that  1-exit be
void
>of code?
>
>So, class, the point might be that the advocacy of GOTO 1-exit depends
utterly
>upon an experts knowledge of implementation details, and that implementors
are
>now limitted by the practices in the field, not by the approved or
documented
>language standard.
>
>In contradistinction to the foregoing comments in this thread the
proposition
>is that a GOTO begining, can not be more offensive than GOTO ending. If the
>expert tells you that the iterator, about which only the greatest minds
could
>be informed, might be damaged by a non-linear jump, then it must be true no
>matter which direction you jump.
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c8b6b4.87468511@news1.ibm.net>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com>`

```
On 15 Feb 1999 22:28:20 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:

>Now, class, we have a pop quiz.

If one performs the perform --- thru paragraph UNTIL such and such
condition, the GO TO back to the top of said perform is unnecessary,
and implied.  However, such a GO TO is permitted, and the perform will
complete, and if one uses particular PC compilers one will blow ones
stack.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 6)_

- **From:** "Jay Siegel" <ka2csh@nospam.nowhere>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h5.e5.h02V3EKoRsq4iEEr4.NR@nospam.nowhere>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com>`

```
"RKRay" == "RKRayhawk" writes:

RKRay> Now, class, we have a pop quiz.
RKRay> 
RKRay> It would appear that we have had here in this innocent thread
RKRay> a clear recordation of the concerns, felt mutually, of two
RKRay> very informed prognosticators to the effect that should there
RKRay> be a mixture of GOTO and PERFORM of the particular variety of
RKRay> a GOTO to the top paragraph name that there could be a
RKRay> breakage, as it were, betwixt releases of the compiler.
RKRay> 
RKRay> In particular, the iterative functionality latent in PERFORM
RKRay> may be dysfunctionalized by such a jump.  There was humorously
RKRay> a disagreement as to whether this would be a break of the GOTO
RKRay> or a break of the PERFORM, (surely that is expertise
RKRay> instantiated). --- major snip --- Robert Rayhawk
RKRay> RKRayhawk@aol.com
RKRay> 
Apparently, nobody but me on this news group has worked on Burroughs
Large Systems COBOL (now Unisys).  There's a command there that is so
succint in its structure and ability to resolve the problem of going
to an EXIT paragraph.  You simply code: EXIT HERE and it is just like
GOing TO the EXIT paragraph.  IBM never implemented it, but they
borrowed other stuff from Burroughs. If you think about what you're
really doing here, you really wouldn't need a GO TO the EXIT in
almost all cases, except those of complex conditions.  You should
code the PERFORM THROUGH using UNTIL condition.  This usually
eliminates the need for a condition test inside the PERFORM.  You
also need to break the logic up into smaller blocks to avoid using
the GO TO the EXIT.

Jay
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DD47ED.23589E18@NOSPAMhome.com>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com> <h5.e5.h02V3EKoRsq4iEEr4.NR@nospam.nowhere>`

```
> Apparently, nobody but me on this news group has worked on Burroughs
> Large Systems COBOL (now Unisys).  There's a command there that is so
…[9 more quoted lines elided]…
> the GO TO the EXIT.

I used Bourroughs (Large & small) a long time ago, and Univac more
recently - didn't know about that nice command.  I still don't like
performing more than one paragraph.  It seems that with the EXIT HERE
command there's even less reason for having THROUGH than before.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 8)_

- **From:** Ernest.Gose@Lexis-Nexis.com (Ernie Gose)
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bm90h$6pt$1@mailgate2.lexis-nexis.com>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com> <h5.e5.h02V3EKoRsq4iEEr4.NR@nospam.nowhere> <36DD47ED.23589E18@NOSPAMhome.com>`

```
Interesting topic and quite timely for me as I used a goto the other day for 
the first time in at least 10 years.  My mentor taught me to exit paragraphs - 
actually called internal modules in PL/1 - by going to xxxx-exit.  He also 
impressed upon us to keep each paragraph within a page.  I always thought this 
was about the right amount of space required to code the essance of the 
'whole' function that you are coding.  Which I think is not only structured 
but much easier to understand than many itty bitty paragaphs.  But people who 
wouldn't recognize a comp-3 data type if it bit them in their arse instantly 
branded my code as unstructured and expensive to maintain.

A few years ago I noticed that recent college graduates had adopted the 
same method that I had been taught many years before.  Somewhere along the 
line acadamia got a dose of common sense.  Good!

However, EXIT HERE would have been a great implementation and eliminated 
adopting itty-bitty paragraphs as 'ordained' structured.  

BTW: Correct me if I'm wrong - if ever there's a sure thing ... - until isn't 
the optimum solution if you've discovered you need to get 'exit' in 
mid-paragraph.

In article <36DD47ED.23589E18@NOSPAMhome.com>, brazee@NOSPAMhome.com says...
>
>> Apparently, nobody but me on this news group has worked on Burroughs
…[15 more quoted lines elided]…
>command there's even less reason for having THROUGH than before.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 9)_

- **From:** "R. Hayes" <rmch@cadvision.com>
- **Date:** 1999-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f10d91.0@news.cadvision.com>`
- **References:** `<36C88E7B.6186E498@NOSPAMhome.com> <19990215172820.07685.00001563@ng156.aol.com> <h5.e5.h02V3EKoRsq4iEEr4.NR@nospam.nowhere> <36DD47ED.23589E18@NOSPAMhome.com> <7bm90h$6pt$1@mailgate2.lexis-nexis.com>`

```
Be aware that you've probably just started yet another 150,000 message
thread.



Ernie Gose wrote in message <7bm90h$6pt$1@mailgate2.lexis-nexis.com>...
>Interesting topic and quite timely for me as I used a goto the other day
for
>the first time in at least 10 years.  My mentor taught me to exit
paragraphs -
>actually called internal modules in PL/1 - by going to xxxx-exit.  He also
>impressed upon us to keep each paragraph within a page.  I always thought
this
>was about the right amount of space required to code the essance of the
>'whole' function that you are coding.  Which I think is not only structured
>but much easier to understand than many itty bitty paragaphs.  But people
who
>wouldn't recognize a comp-3 data type if it bit them in their arse
instantly
>branded my code as unstructured and expensive to maintain.
>
…[7 more quoted lines elided]…
>BTW: Correct me if I'm wrong - if ever there's a sure thing ... - until
isn't
>the optimum solution if you've discovered you need to get 'exit' in
>mid-paragraph.
>
>In article <36DD47ED.23589E18@NOSPAMhome.com>, brazee@NOSPAMhome.com
says...
>>
>>> Apparently, nobody but me on this news group has worked on Burroughs
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aabqm$vn$1@news.igs.net>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com>`

```
I think you are stretching it too, Howard. I cannot see
perform breaking because a programmer uses GO To.

Howard Brazee wrote in message <36C88E7B.6186E498@NOSPAMhome.com>...
>Judson McClendon wrote:
>>
…[14 more quoted lines elided]…
>be more likely to break if it has a GOTO within it.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cc96c3.76825519@netnews>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com>`

```
'Twas Mon, 15 Feb 1999 14:15:39 -0700, when Howard Brazee
<brazee@NOSPAMhome.com> illuminated comp.lang.cobol thusly:

>Judson McClendon wrote:
>> 
…[14 more quoted lines elided]…
>be more likely to break if it has a GOTO within it.

Howard, I have used COBOL and read about COBOL for over 25 years and
AFAICR this is the first time that anyone has suggested that GO TO top of
paragraph might have any effect on the PERFORM.  Increments and checks
happen when you fall off the bottom of your PERFORM range, not when you GO
anywhere.  This includes GO TO EXIT-PAR.  The PERFORM exit logic kicks in
when you fall out of the EXIT paragraph, and only if it's the end of your
PERFORM range.

For the record, I too abhor the reckless use of GO TO.  I was raised with
the opposite.  My first language was Basic, where the only thing IF could
do was GOTO.  I then learned Fortran IV, with the choice between
artihmetic IF or a logical IF which took only a single statement.  In the
mid-70s I had a COBOL teacher who said, "Never use ELSE.  Use GO TO to
show what you really mean."  At the time I considered this advice
assinine, but my code was GO-heavy until I learned the wisdom of
"structured coding" a few years later.

Let me enumerate the situations where I still use GO TO:

1)  GO TO top, as an alternative to recursive PERFORM.  (For the poor
fellow whose compiler limits PERFORM recursion to 2, I feel very sad.
With Burroughs you always had room for a PERFORM stack of at least 10 and
if you asked for more space it was hundreds.  I remember using
non-recursive compilers in the 1970s, but people don't still use those, do
they?)
2)  GO TO EXIT.
3)  GO TO abort procedure.  Actually PERFORM abort procedure is better
form, but if the risk of getting stack overflow on that PERFORM is
credible, GO TO becomes inherently superior.  On Burroughs Medium System
(Unisys V Series) there were cases where this mattered.  I haven't
actually used this in 15 years, and the arguments for it grow only weaker.
4)  GO TO next paragraph.  Before there were scope terminators this was
often the easiest way to write a routine.  Scope terminators mostly
eliminate the need for this construct, but not completely.  Sometimes the
code gets so nested that it is useful to break it up just to reduce the
nesting.  Usually this is best done by moving a logical chunk to another
location and PERFORMing.  But this has the unfortunate effect of putting
code logically out of sequence.  By using GO TO next paragraph a large but
relatively simple routine can be kept in logical sequence.

The reason GO TO is (appropriately) shunned is that it is the most bug
prone command.  Toward this end, any style checker should flag any use of
GO TO, and attempt to categorize it as one of these 4 (and #3 is pretty
iffy).  Any GO TO which doesn't fit one of these should be banned.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CD8194.E42B109A@NOSPAMhome.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com> <36cc96c3.76825519@netnews>`

```
> Let me enumerate the situations where I still use GO TO:

> 3)  GO TO abort procedure.  Actually PERFORM abort procedure is better
> form, but if the risk of getting stack overflow on that PERFORM is
> credible, GO TO becomes inherently superior.  On Burroughs Medium System
> (Unisys V Series) there were cases where this mattered.  I haven't
> actually used this in 15 years, and the arguments for it grow only weaker.

This is the only place I still use GO TO.  Mainly because I disagree
that PERFORM is better form.  If there's no way I want to ever come back
and coming back will mess me up, I will be honest and write GO TO. 
PERFORM is a obsfucation.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 7)_

- **From:** JD <beta1@bigfoot.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D5ECB3.E5F2A589@bigfoot.com>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com> <36cc96c3.76825519@netnews> <36CD8194.E42B109A@NOSPAMhome.com>`

```
I agree.  A case in point is CICS transactions.  I've been in shops where ALL
routines were performed, even though it would be impossible to return from the
routine (e.g. the routine does a map send and returns control to CICS).  This is
actually a DUMB practice, and makes for much more difficulty in maintenance of
the program.  Perform should ONLY be used if the code will come back after the
performed routine completes, otherwise it simply "obfuscates" the code's
intended function..

Howard Brazee wrote:

> > Let me enumerate the situations where I still use GO TO:
>
…[9 more quoted lines elided]…
> PERFORM is a obsfucation.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 8)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36d60cac.88876140@news1.ibm.net>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com> <36cc96c3.76825519@netnews> <36CD8194.E42B109A@NOSPAMhome.com> <36D5ECB3.E5F2A589@bigfoot.com>`

```
On Thu, 25 Feb 1999 16:37:07 -0800, JD <beta1@bigfoot.com> wrote:

>I agree.  A case in point is CICS transactions.  I've been in shops where ALL
>routines were performed, even though it would be impossible to return from the
…[4 more quoted lines elided]…
>intended function..

Actually control does not return to CICS until an EXEC CICS RETURN is
executed - unless you are conversational - in which case your program
just stays in control.  At any rate, the point to this is - performing
the "return to CICS" routine is complete and utterly appropriate -
although I would prefer to "fall through" it instead.

I'm not saying "perform" so you don't have "go to".  The reality as I
have seen it work itself in ME is this:

Trying first just to eliminate go to:  Leads to the necessity to
"think differently" about the creation of the code.

This "different" way of thinking leads to more structured code, fewer
bugs and faster development.

Using this "different" way of thinking automatically creates code
without GO TO.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 8)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D63DF4.A5E689DE@att.net>`
- **References:** `<79sni8$6a0@dfw-ixnews12.ix.netcom.com> <19990214090348.09998.00001408@ng29.aol.com> <36C842A8.FBB26F70@NOSPAMhome.com> <vP%x2.6593$wj1.9765393@news2.mia> <36C88E7B.6186E498@NOSPAMhome.com> <36cc96c3.76825519@netnews> <36CD8194.E42B109A@NOSPAMhome.com> <36D5ECB3.E5F2A589@bigfoot.com>`

```
JD wrote:
> 
> This is actually a DUMB practice, and makes for much more difficulty in maintenance of
> the program.

Really? If you're looking at a program which performs a paragraph
containing a GOBACK or EXEC CICS RETURN END-EXEC and you're confused,
who's the DUMB one? I've worked with IBM mainframes more than thirty
years and God knows how many COBOL programmers. They weren't all A-list
programmers, but I can't recall anyone finding the above confusing.

> Perform should ONLY be used if the code will come back after the
> performed routine completes, otherwise it simply "obfuscates" the code's
> intended function..

I don't agree - color me DUMB (or is this a troll?). It seems all the
pontificating doesn't come from Rome.

Bill Lynch
```

##### ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** veronem@aol.com (Veronem)
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990226160215.15438.00001234@ng-fi1.aol.com>`
- **References:** `<19990214090348.09998.00001408@ng29.aol.com>`

```
I've been reading this thread for a couple of days now,  I find it long winded
and unrealistic.  Basically,  whatever your compiler or shop wants is what you
are going to do.

My preference is to use  xxx-EXIT, only because it shows a definite beginning
and ending of a paragraph.  And because I have worked on several different
compiler, some required the exit others didn't.  

As far as GOTO, everyone uses them.  If your a good programmer you know how to
use them properly and if your not, well nothing you do is going to help.

Just my 2 cents,
Mary Veronesi


>Subject: Re: "EXIT Immediate" from the middle of a Procedure
>From: denis548@aol.com (Denis548)
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D71113.D1BA8C58@NOSPAMhome.com>`
- **References:** `<19990214090348.09998.00001408@ng29.aol.com> <19990226160215.15438.00001234@ng-fi1.aol.com>`

```
Veronem wrote:
> 
> I've been reading this thread for a couple of days now,  I find it long winded
…[8 more quoted lines elided]…
> use them properly and if your not, well nothing you do is going to help.

Your first and last paragraphs don't agree.  Lots of shops say no
GOTOs.  And unless my shop says I have to use GOTOs, I don't use them
except where others would do PERFORM 0000-ABORT.
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2FB2.837$FN5.707616@news3.mia>`
- **References:** `<19990214090348.09998.00001408@ng29.aol.com> <19990226160215.15438.00001234@ng-fi1.aol.com>`

```
Veronem wrote:
>I've been reading this thread for a couple of days now,  I find it long winded
>and unrealistic.  Basically,  whatever your compiler or shop wants is what you
>are going to do.


This is true.  But some of us are in the position of defining what the
standard will be. :-)
```

###### ↳ ↳ ↳ Re: "EXIT Immediate" from the middle of a Procedure

_(reply depth: 4)_

- **From:** SS <wldfilly@sgi.net>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E8ABC1.E6645860@yahoo.com>`
- **References:** `<19990214090348.09998.00001408@ng29.aol.com> <19990226160215.15438.00001234@ng-fi1.aol.com> <b2FB2.837$FN5.707616@news3.mia>`

```
Judson McClendon wrote:
> 
> Veronem wrote:
…[7 more quoted lines elided]…
> Judson McClendon    

   Oh aren't you the lucky one! Our rules are to only use "GO TO"'s when
going to the 9999-EXIT
 when it will significantly speed up processing. Not a bad rule, at
least it provides some guidance
 to "newbies".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
