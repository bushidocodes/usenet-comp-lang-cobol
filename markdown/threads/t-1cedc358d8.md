[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Terminal format to ANSI Format converter

_19 messages · 11 participants · 2002-12_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Terminal format to ANSI Format converter

- **From:** travis.chase@leggett.com (Travis Chase)
- **Date:** 2002-12-12T11:58:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66c36a1c.0212121158.f73def6@posting.google.com>`

```
Is there a converter out there that will take terminal formatted COBOL
and convert it to ANSI formatted COBOL.  If it helps we are using
ACUCOBOL.

Thanks in advance,
Travis
```

#### ↳ Re: Terminal format to ANSI Format converter

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-12T22:17:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212122217.4c0f1dc1@posting.google.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com>`

```
VMS has a reformat utility (REFORMAT) to do this.  That's where
terminal format came from (DEC/VAX/VMS).

Acu can handle EITHER format, but the workbench does not have a
converter.

ANSI to terminal is trivial - Terminal to ANSI is much much harder. 
(Continuation insertions etc).

travis.chase@leggett.com (Travis Chase) wrote in message news:<66c36a1c.0212121158.f73def6@posting.google.com>...
> Is there a converter out there that will take terminal formatted COBOL
> and convert it to ANSI formatted COBOL.  If it helps we are using
…[3 more quoted lines elided]…
> Travis
```

##### ↳ ↳ Re: Terminal format to ANSI Format converter

- **From:** robin lee <robinlee@rr.com>
- **Date:** 2002-12-15T00:32:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFBCC2A.B0D9D57D@rr.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com>`

```

Thane Hubbell wrote:
> 
> VMS has a reformat utility (REFORMAT) to do this.  That's where
> terminal format came from (DEC/VAX/VMS).
> 

 I am curious... and this may be a gap in my experience, but to my
knowledge DEC did not have a working COBOL in the seventies when I was
coding in CRT format in DG COBOL.  DEC only had DIBOL.  And of course
this was back in the days of RSTS before VMS came into existence.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-12-15T01:54:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BhRK9.53688$vM1.4289465@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com>`

```

robin lee <robinlee@rr.com> wrote in message news:3DFBCC2A.B0D9D57D@rr.com...
>
>  I am curious... and this may be a gap in my experience, but to my
> knowledge DEC did not have a working COBOL in the seventies when I was
> coding in CRT format in DG COBOL.  DEC only had DIBOL.  And of course
> this was back in the days of RSTS before VMS came into existence.

DEC did indeed have COBOL in the seventies.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-15T04:06:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-6kjwj0j0rW8I@h24-82-204-17.wp.shawcable.net>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com>`

```
On Sun, 15 Dec 2002 00:32:43 UTC, robin lee <robinlee@rr.com> wrote:

> 
> Thane Hubbell wrote:
…[8 more quoted lines elided]…
> this was back in the days of RSTS before VMS came into existence.

From 1976/77 on DEC had COBOL on the PDP-11/70 machines running IAS. 
It worked really well with the IDMS network database system. This 
sotware was carried forward to VMS running on the VAX-11/780 as well.

When I was the Data Processing manager with Yamaha Canada Music, we 
used COBOL and IDMS to implement a customer billing, inventory control
and sales analysis system using COBOL and IDMS.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-15T08:09:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFCA928.1020600@Sympatico.ca>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com>`

```
You are thinking of the PDP-11 line.  The PDP-10 and the 20 had cobol 
from the late 60's on.
Donald


robin lee wrote:

>Thane Hubbell wrote:
>  
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-12-15T17:59:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mq3L9.804$pY6.617@newssvr19.news.prodigy.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com>`

```
I programmed in DIBOL in the late 70s.  It had an EXIT verb that could be
used to exit the current paragraph.  I've heard that an EXIT-PARAGRAPH verb
is going to be part of the new COBOL standards.  Could it be that DIBOL was
30 years ahead of its time?  :)
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 4)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-15T13:02:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFCEDDE.50202@Sympatico.ca>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com>`

```
I programmed in Cobol in the early 70's.  It also had an EXIT verb.  The 
new verb is CONTINUE.

Donald

Terry Heinze wrote:

>I programmed in DIBOL in the late 70s.  It had an EXIT verb that could be
>used to exit the current paragraph.  I've heard that an EXIT-PARAGRAPH verb
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-15T16:47:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212151647.70f5ebc2@posting.google.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca>`

```
Donald Tees <Donald_Tees@Sympatico.ca> wrote


> >I programmed in DIBOL in the late 70s.  It had an EXIT verb that could be
> >used to exit the current paragraph.  I've heard that an EXIT-PARAGRAPH verb
> >is going to be part of the new COBOL standards.  Could it be that DIBOL was
> >30 years ahead of its time?  :)

> I programmed in Cobol in the early 70's.  It also had an EXIT verb.  

It is debatable whether 'EXIT' (by itself) in Cobol is a verb.  It is
entirely a  noise word that has no functionality, other then being
content for an otherwise empty exit paragraph.

Specifically it does _not_ 'exit the current paragraph'.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 6)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-12-16T02:19:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message news:217e491a.0212151647.70f5ebc2@posting.google.com...
> Donald Tees <Donald_Tees@Sympatico.ca> wrote
>
…[11 more quoted lines elided]…
> Specifically it does _not_ 'exit the current paragraph'.

It may, or it may not.  It depends upon the controlling program logic.

I don't believe that there is anything at all debatable about EXIT being a verb.

My understanding of it is that it is a null, or No Operation, placeholder
which can be dynamically modified at runtime to effect a return
to the statement which follows a PERFORM...THRU...statement.

If you do a straight PERFORM of the associated paragraph, the EXIT statement
is of no import as it is in a different paragraph and therefore not executable or executed.

If you GO TO the associated paragraph, you will fall through to the EXIT paragraph,
and then you may fall through to the paragraph following the EXIT paragraph,
or you may shoot off somewhere else entirely,
courtesy of a prior PERFORM....THRU's residual dynamic modification
of the EXIT paragraph.

And that, when you get down to it, makes PERFORM....THRU...
nothing more than a glorified alterable GO TO construct,
with all of the caveats and consequences you know and love so well.

The preceding is a synopsis of my trials and tribulations over the years.
Your experience, compiler, hardware etc most likely will have been different,
but that will not, cannot and does not affect what I have run into.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-16T18:25:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFE1AA8.805B51EF@Azonic.co.nz>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:

> > It is debatable whether 'EXIT' (by itself) in Cobol is a verb.  It is
> > entirely a  noise word that has no functionality, other then being
…[6 more quoted lines elided]…
> I don't believe that there is anything at all debatable about EXIT being a verb.

From my Cobol manual:

"Verb: A word that expresses an action to be taken .."

"An EXIT statement serves only to enable the user to assign a
procedure-name to a given point in a program. Such an EXIT statement has
no other effect on the compilation or execution of the program."

You are correct that it is not debatable - it is not a verb.  It
certainly does not 'exit the current paragraph'.
 
> My understanding of it is that it is a null, or No Operation, placeholder
> which can be dynamically modified at runtime to effect a return
> to the statement which follows a PERFORM...THRU...statement.

It may well be true that some generated code may dynamically modify the
code at the end of a perform range.  This does not require the use of an
EXIT statement.  That is:

        PERFORM A THRU B
        ...
     A.
        MOVE 1    TO X.
     B.
        MOVE 1    TO Y.
     C.
        ...

Will still have the end of paragraph B modified (for systems that do
this).  Thus it is not the EXIT that is modified, but some point beyond
the last line of code.

Of course this code self-modification is rather archaic anyway, for the
last several decades there have been protected mode architectures which
specifically disallow self-modification.  Perform ranges are now done
using stacks or other more modern mechanisms.
  
> If you do a straight PERFORM of the associated paragraph, the EXIT statement
> is of no import as it is in a different paragraph and therefore not executable or executed.

I think that you entirely miss the point of this sub-thread that was
trying to relate EXIT in DIBOL (which apparently works like return() in
C) to EXIT in Cobol.  In fact 'EXIT PARAGRAPH' (or 'EXIT SECTION') is
probably equivalent to Dibol's EXIT from a performed paragraph.  'EXIT
PROGRAM' from a nested program may be closer equivalent (available in
'85).
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-16T09:34:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atkrpj$r7$1@slb4.atl.mindspring.net>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz>`

```
Richard,
  Out of curiosity, which COBOL manual has

"Verb: A word that expresses an action to be taken .."

This has NEVER really been true in COBOL.  Traditionally, the word "IF" has
been classified as a "verb" in COBOL - which it most certainly is *not* in
any "normal English" definition of "verb" - or in the definition that you
list above.  I can't personally, think of a "good" (not that word again <G>)
definition of a COBOL "verb" that would include CONTINUE but not EXIT.

FYI,
  The 2002 COBOL Standard has *REMOVED* the term "verb" and *only* talks
about statements.

FYI-2,
  Traditionally, the "EXIT PROGRAM" statement uses the COBOL "verb" EXIT.
The new Standard adds "phrases" (or variations) to the EXIT statement
(previously known as the EXIT verb) for
    EXIT PARAGRAPH
    EXIT SECTION
    EXIT PERFORM

each of these "enhances" the cases where "EXIT" is a "verb" in the
traditional (now removed) COBOL meaning.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-16T18:01:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oyoL9.1657$qU5.955122@newssrv26.news.prodigy.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz> <atkrpj$r7$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:atkrpj$r7$1@slb4.atl.mindspring.net...
> Richard,
>   Out of curiosity, which COBOL manual has
…[3 more quoted lines elided]…
> This has NEVER really been true in COBOL.  Traditionally, the word "IF"
has
> been classified as a "verb" in COBOL - which it most certainly is *not* in
> any "normal English" definition of "verb" - or in the definition that you
> list above.

Oh, I don't know...one might say IF is actually 'two verbs in one'  ....
"compare" and "store [result of comparision]"

MCM
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-16T11:40:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212161140.12d00ef0@posting.google.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz> <atkrpj$r7$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote

>   Out of curiosity, which COBOL manual has
> 
> "Verb: A word that expresses an action to be taken .."

Microfocus, Appendix A in some versions, Glossary in others.
 
> I can't personally, think of a "good" (not that word again <G>)
> definition of a COBOL "verb" that would include CONTINUE but not EXIT.

Well, CONTINUE, while it does absolutely nothing in terms of
executable code, actually does do what its english meaning implies.
 
> FYI-2,
>   Traditionally, the "EXIT PROGRAM" statement uses the COBOL "verb" EXIT.

Which is why I qualified with "by itself".

> The new Standard adds "phrases" (or variations) to the EXIT statement
> (previously known as the EXIT verb) for
>     EXIT PARAGRAPH
>     EXIT SECTION
>     EXIT PERFORM

These have been in Microfocus for several years.

> each of these "enhances" the cases where "EXIT" is a "verb" in the
> traditional (now removed) COBOL meaning.

I am not convinced that 'EXIT PARAGRAPH' and 'EXIT SECTION' are
'enhancements'.  They may be useful as "exit to the end of the current
perform", but the correct one has to be used and this can be a trap. 
For example if a section has been performed:

           DoIt SECTION.
               some code 1
               if ( ) EXIT PARAGRAPH.
               some code 2.
           NextBit SECTION.

this works as intended.  However if a 'loop label' is added in some
code 2 (as it seems some might) then the exit goes to this instead of
the end of the section. This is where a change in one part of the
program causes a change in logic flow somewhere else entirely. Very
difficult to find.

This may also be used to create spagetti code because EXIT PARAGRAPH
is really a 'GO TO next-label'.  Within a performed section there may
be several paragraph labels and EXIT PARAGRAPH will jump to the next
one - and there are no 'GO TOs'.

Similarly if EXIT SECTION is used in a performed paragraph the program
loses control.
 
It would be nice if there was an 'exit from current out-of-line
perform whatever it is' but EXIT PERFORM is only used in-line.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-16T20:17:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atlccq$mtl$1@peabody.colorado.edu>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz> <atkrpj$r7$1@slb4.atl.mindspring.net> <217e491a.0212161140.12d00ef0@posting.google.com>`

```

On 16-Dec-2002, riplin@Azonic.co.nz (Richard) wrote:

>            DoIt SECTION.
>                some code 1
>                if ( ) EXIT PARAGRAPH.
>                some code 2.
>            NextBit SECTION.

Which won't effect new code unless standard copymembers include ERROR-SECTION
SECTION or some such nonsense (I work in such a shop).  Obsolete standards will
be the only reason for sections past the start of the PROCEDURE DIVISION start.
(Declaratives are before this start).   Fortunately, if this is the ONLY section
(with a syntax error removing dummy section at the start - an exit section will
fall through to the ERROR-ROUTINE.

For shops that currently mix up sections and paragraphs, this type of absurdity
will occur.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 10)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-16T15:36:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212161536.3c94d778@posting.google.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz> <atkrpj$r7$1@slb4.atl.mindspring.net> <217e491a.0212161140.12d00ef0@posting.google.com>`

```
Richard - one comment below...and a question..

riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0212161140.12d00ef0@posting.google.com>...

> This may also be used to create spagetti code because EXIT PARAGRAPH
> is really a 'GO TO next-label'.  Within a performed section there may
> be several paragraph labels and EXIT PARAGRAPH will jump to the next
> one - and there are no 'GO TOs'.
> 

This is no different than performing that first paragraph within the
section.

We did extensive work on the Exit Paragraph, exit Perform etc to
ensure clear transfers of control.  There won't be any more accidental
fall through than there is already today.

> Similarly if EXIT SECTION is used in a performed paragraph the program
> loses control.

Huh?
```

###### ↳ ↳ ↳ EXIT ??? problems (was: Terminal format to ANSI Format converter

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-16T17:52:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atlp0p$qee$1@slb9.atl.mindspring.net>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz> <atkrpj$r7$1@slb4.atl.mindspring.net> <217e491a.0212161140.12d00ef0@posting.google.com> <bfdfc3e8.0212161536.3c94d778@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0212161536.3c94d778@posting.google.com...
>
> > Similarly if EXIT SECTION is used in a performed paragraph the program
> > loses control.
>
> Huh?

Thane,
  This indeed is a "known" problem with the new EXIT structures (although as
you indicated in the snipped portion of your original note - this is NOT
something that couldn't happen before).

Consider the following Procedure Division code:

Procedure Division.
  Sect1 Section.
    Para1.
       Display "Starting out"
       Perform Para2
       Display "Won't ever get back here"
       GoBack.
  Sect2 Section.
    Para2.
       Display "In Para2"
       Exit Section  *> Go To Para3 would have the SAME problem in '85
Standard
       Display "Flow of control is LOST and 'falls' off end of program"
         .
    Para3.
       Display "Never Executed"
          .
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 8)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-12-17T06:34:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nAzL9.1166$e73.75587731@newssvr15.news.prodigy.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca> <217e491a.0212151647.70f5ebc2@posting.google.com> <HKaL9.63889$hK4.5280752@bgtnsc05-news.ops.worldnet.att.net> <3DFE1AA8.805B51EF@Azonic.co.nz>`

```
Just saw your note mentioning the verb RETURN.  I managed to locate my old
DIBOL manual, and it IS the RETURN verb, not EXIT as I'd thought:  "The
RETURN statement causes control to return to the statement immediately
following the last executed CALL or XCALL statement.  A RETURN statement
must be placed at the logical end of every subroutine."  Copyright 1975,
1976 by Digital Equipment Corporation.
```

###### ↳ ↳ ↳ Re: Terminal format to ANSI Format converter

_(reply depth: 5)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-12-16T05:14:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DidL9.793$0S5.680@newssvr16.news.prodigy.com>`
- **References:** `<66c36a1c.0212121158.f73def6@posting.google.com> <bfdfc3e8.0212122217.4c0f1dc1@posting.google.com> <3DFBCC2A.B0D9D57D@rr.com> <mq3L9.804$pY6.617@newssvr19.news.prodigy.com> <3DFCEDDE.50202@Sympatico.ca>`

```
I think you missed the point.  The following is an example of a DIBOL paragraph.  Forgive any errors since this is from memory.  :)

INIT.
    X = 0.
    CALL LODTBL.
    end program.
LODTBL.
    INCR X.
    IF X > MAXX
        EXIT.
    do stuff here.
    GO TO LODTBL.

DIBOL IFs didn't have ELSEs as I recall.  The EXIT terminated the performing (CALLing) of the paragraph.  A DIBOL CALL was the equivalent of a COBOL PERFORM.  An XCALL was a COBOL CALL.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
