[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PERFORM and performance

_49 messages · 15 participants · 2010-08 → 2010-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### PERFORM and performance

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-08-26T02:47:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>`

```
Just as a follow-up on another thread.

I would be VERY interested in any current documentatin indicating that the 
PERFORM statement (with any compiler) has "bad performance".

I can certainly imagine that GO TO might (probably would) haave better 
performance (at least in some cases), but that is like saying that you CAN 
create better performing "good" Assembler than "comparable good" COBOL. 
True, but not very useful in practice as a GENERAL rule.
```

#### ↳ Re: PERFORM and performance

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-26T13:03:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i55omp$fnb$2@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>`

```
In article <k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>,
Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
>Just as a follow-up on another thread.
>
>I would be VERY interested in any current documentatin indicating that the 
>PERFORM statement (with any compiler) has "bad performance".

I would be even more interested in any documentation indicating that such 
a thing as 'bad performance' is something other than a simple-minded way 
of generating a Kantian Categorical Imperative which is applicable only to 
Theoretical Code and not to Any Written Code.

(Any Written Code falls into 'does it perform satisfactorily within The 
Window or not?'... if a Window is specified; if no Window is specified 
then: 

IF PROGRAM-RUNS 
    PERFORM NEXT-ASSIGNMENT 
ELSE 
    PERRFORM CODE-LIKE-HELL 
     UNTIL DAMNED-THING-WORKS.

... seems as valid (under any semi-standard compiler for the past four 
decades) as any other code.)

DD
```

#### ↳ Re: PERFORM and performance

- **From:** Fritz Wuehler <fritz@spamexpire-201008.rodent.frell.theremailer.net>
- **Date:** 2010-08-26T16:37:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>`

```
> I would be VERY interested in any current documentatin indicating that
> the PERFORM statement (with any compiler) has "bad performance". 

I responded to this issue earlier despite the typical arrogant, snide,
know-it-all remarks that keep me from using my name on this newsgroup but
alas the posts didn't make it. That's the nature of anonymous posting.

The answer is to have a look at the code generated for PERFORM. If I
recall, it generates 9 or ten instructions including front and back end. If
you consider using two GOTOs (one to branch to the routine and one to
branch back) you save a net of 7 instructions using GOTO instead of
PERFORM. Take a look at what the compiler generates and you'll see what I'm
talking about. Again I'm speaking to IBM mainframe COBOL, I have not looked
at other versions.

Consider a typical scenario processing a ten million record file. For each
PERFORM (in the main path) you don't use, or for each one you remove, you
save 70 million instructions. Typically PERFORM is overused to the point of
abuse, so in practice you can save billions of instructions in big
jobs. The other bad thing PERFORM does is cause you to make what's
basically one big input/process/output loop into concentric series of
loops, which causes long branches and unnecessary paging and a large
working set. All of this is avoided with regular top-down, forward flowing
code using GOTOs. I haven't seen the business application yet that requires
the use of PERFORM. I'm sure if you code algorithmic solutions in COBOL you
may find them handy, but that's not what COBOL is about.

I have worked on large and very large systems, and I haven't seen any
advantages in maintainability or readability using PERFORM, in fact my
experience is the opposite. PERFORM clearly impacts performance in a
significantly negative way, and in my view reduces readability. PERFORM
should be used very sparingly and thoughtfully, instead of as a default way
of designing and coding, at least in the IBM environment.
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-26T16:18:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5644m$iak$1@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
In article <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>,
Fritz Wuehler  <fritz@spamexpire-201008.rodent.frell.theremailer.net> wrote:
>> I would be VERY interested in any current documentatin indicating that
>> the PERFORM statement (with any compiler) has "bad performance". 
…[3 more quoted lines elided]…
>alas the posts didn't make it.

If one sees remarks as arrogant, snide and know-it-all then one should 
refrain from making them.

[snip]

>Consider a typical scenario processing a ten million record file. For each
>PERFORM (in the main path) you don't use, or for each one you remove, you
>save 70 million instructions.

Using PP 5655-S71 IBM Enterprise COBOL for z/OS  4.2.0 and the LIST option 
the statement:

PERFORM 5000-READEM-N-WEEP UNTIL NO-MORE-INPUT

... generated:

PERFORM                                                               
  47F0 B204               BC    15,516(0,11)            GN=37(000574)
                 GN=17    EQU   *                                    
*5000-READEM-N-WEEP            
READ                           
  5840 913C               L     4,316(0,9)              INPUT-FILE
 (etc)

... and the statement:

GO TO THE-GO-TO

... generated:

GO                                                                
  47F0 B24A               BC    15,586(0,11)            THE-GO-TO
(other intermediate code)
*THE-GO-TO                                                         
READ                                                               
  5840 913C               L     4,316(0,9)              INPUT-FILE

What code/compiler are you using which generates so different a quantity?  
Would you be so kind as to post a sample?

[snip]

>I haven't seen the business application yet that requires
>the use of PERFORM.

All of us are limited, to one extent or another, by what we have seen and 
what we've learned from what we've seen.  Welcome to the club.

[snip]

>I have worked on large and very large systems, and I haven't seen any
>advantages in maintainability or readability using PERFORM, in fact my
>experience is the opposite.

It seems your experience corresponds to another poster here; are you 
familiar with Mr Dilworth?

DD
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-26T12:12:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<283dd5f4-8ad1-42c0-bba8-076ff6abf76c@m17g2000prl.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
On Aug 27, 2:37 am, Fritz Wuehler
<fr...@spamexpire-201008.rodent.frell.theremailer.net> wrote:

> [..] I haven't seen any
> advantages in maintainability or readability using PERFORM, in fact my
> experience is the opposite. PERFORM clearly impacts performance in a
> significantly negative way, and in my view reduces readability.

What is 'easy to understand' and 'readable' is entirely what you are
used to. If you have been using GO TO since the 1960s then it is
perfectly understandable that you are confused by more modern
constructs such as 'PERFORM'. You probably still have all your code in
upper case and use commas and full stops everywhere possible.

However, you shouldn't extrapolate your inability to learn, or
unwillingness, onto others just for your own convenience.

Personally, given your attitudes expressed, I would prefer that you do
not read my programs and would even go so far as to make them even
more difficult for you to read if this enables other, more advanced,
programmers to maintain them.
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-26T17:12:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
Fritz Wuehler wrote:
>> I would be VERY interested in any current documentatin indicating
>> that the PERFORM statement (with any compiler) has "bad performance".
…[19 more quoted lines elided]…
> jobs.

How many instructions you save is unimportant. The issue is how many SECONDS 
(MINUTES, HOURS) you save.

In your hypothetical of 10 million records and 7 instructions, you save 70 
million instructions. A modern PC can currently hit 2,400 MWIPS (million 
Whetstone instructions per second). So, by shrinking the code as you 
suggest, for the ten million records, you'll save (mumble, mumble, carry the 
three, ah!) 0.03 seconds.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

- **From:** Anonymous <cripto@ecn.org>
- **Date:** 2010-08-27T16:53:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20100827145337.20CCA1AD572@www.ecn.org>`
- **References:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com>`

```
> How many instructions you save is unimportant. The issue is how many
> SECONDS (MINUTES, HOURS) you save.

No, it's both. Batch windows are affected by elapsed time, but many
institutions are being charged for CPU consumption and IBM and software
vendors charge you for how much processor you need and consume, all going
back to how many instructions you execute.

> In your hypothetical of 10 million records and 7 instructions, you save
> 70 million instructions. A modern PC can currently hit 2,400 MWIPS
> (million Whetstone instructions per second). So, by shrinking the code as
> you suggest, for the ten million records, you'll save (mumble, mumble,
> carry the three, ah!) 0.03 seconds. 

First of all, each PERFORM eliminated saves 70 million intructions in that
scenario. Consider a large commercial app with thousands of PERFORMs in one
source deck and you wind up saving billions or trillions of
instructions. You don't find a commercial COBOL application system with
only one PERFORM coded.

Second of all, modern PC MIPS have nothing to do with mainframe MIPS. And
even if they had even the slightest relation, you can't consider MIPS in a
vacuum, you have to realize long instruction paths (and the long branching
from unnecessary PERFORMs as opposed to in-line code) cause problems
disproportional to the amount of instructions. It's not linear.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-27T15:42:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i58mco$hv4$2@reader1.panix.com>`
- **References:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com> <20100827145337.20CCA1AD572@www.ecn.org>`

```
In article <20100827145337.20CCA1AD572@www.ecn.org>,
Anonymous  <cripto@ecn.org> wrote:

[snip]

>First of all, each PERFORM eliminated saves 70 million intructions in that
>scenario.

Up to this point there has been an example given which demonstrates that a 
PERFORM does not require seven more instructions than a GO TO and code has 
been posted which shows that assertion to be false.  

Before things go further might you be so kind as to post code so that your 
assertion not be dismissed as undemonstrated?  The 'onus probandi' is not 
so heavy a burden to bear when one can post the listing.

DD
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2010-08-27T18:43:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RLKdncvi6Jk4ouXRnZ2dnUVZ_oOdnZ2d@earthlink.com>`
- **References:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com> <20100827145337.20CCA1AD572@www.ecn.org>`

```

"Anonymous" <cripto@ecn.org> wrote in message 
news:20100827145337.20CCA1AD572@www.ecn.org...
>> How many instructions you save is unimportant. The issue is how many
>> SECONDS (MINUTES, HOURS) you save.
…[24 more quoted lines elided]…
>

I would suggest that instead of eliminating PERFORM statments that you 
concentrate on removing IF, THEN, ELSE and EVALUATE statements.  These 
involve the generation of conditional branches which oftem wreak havoc with 
the instruction pipeline and with performance.  You will get a bigger bang 
for you time by removing them.  Also instead of replaceing PERFORM with a GO 
TO just manually repeat the code inline at each place that it is needed and 
that way you can get rid of the GO TO altogether.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-27T16:51:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a0111c2-040b-4058-a756-becfd3eeb4c3@k1g2000prl.googlegroups.com>`
- **References:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com> <20100827145337.20CCA1AD572@www.ecn.org> <RLKdncvi6Jk4ouXRnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
On Aug 28, 10:43 am, "Charles Hottel" <chot...@earthlink.net> wrote:
> "Anonymous" <cri...@ecn.org> wrote in message
>
…[37 more quoted lines elided]…
> that way you can get rid of the GO TO altogether.

That last technique is especially relevant to those whose income is
related to LOC statistics.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-30T11:16:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnpn76pafmab80ho4jtmmhukg3820gh97c@4ax.com>`
- **References:** `<SrGdnYE18dQ7d-vRnZ2dnUVZ_tudnZ2d@earthlink.com> <20100827145337.20CCA1AD572@www.ecn.org> <RLKdncvi6Jk4ouXRnZ2dnUVZ_oOdnZ2d@earthlink.com> <9a0111c2-040b-4058-a756-becfd3eeb4c3@k1g2000prl.googlegroups.com>`

```
> How many instructions you save is unimportant. The issue is how many
> SECONDS (MINUTES, HOURS) you save.

The issue is delivering the product reliability & accurately with the
lowest cost.

One criterion that can be used here is how quickly the program runs.
Another is how quickly the program is maintained.
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** Robert <0robert.jones@gmail.com>
- **Date:** 2010-08-29T12:34:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
On Aug 26, 3:37 pm, Fritz Wuehler
<fr...@spamexpire-201008.rodent.frell.theremailer.net> wrote:
> > I would be VERY interested in any current documentatin indicating that
> > the PERFORM statement (with any compiler) has "bad performance".
…[30 more quoted lines elided]…
> of designing and coding, at least in the IBM environment.

I think I see the development of the two extremes of gross abuse of
both GO TO and PERFORM by both some programmers and pundits, deserving
every can of worms and cartesian product they get respectively.

Of course efficiency matters, but it needs to be assessed and balanced
in terms of execution speed, program size, load module size, bandwith,
complexity, reusability of components, adaptability, ease of design
and development, debugging and application of future enhancements and
corrections, all of which have cost impacts and will have different
emphases in different environments.

I don't have access to a mainframe computer, but I think that inline
PERFORMs would have a different footprint to those that perform named
procedures and the VARYING and TIMES clauses are of considerable
benefit when applicable.  Excessive use of the CALL and INVOKE
statements could be expected to have a greater overhead, which is not
to say they shouldn't be used at all.

Procedural copybooks with corresponding data copybooks can reduce some
of the overheads of CALL statements, when appropriate, though changing
them does entail recompilation of all programs using then, while
changing a called subroutine may only require relinking or rebinding,
or neither if the CALL is dynamic.  Called programs that are compiled
within the same source unit, would of course also necessitate
recompilation of all invoking programs when included as common
copybooks.  I would expect their overhead to be intermediate between a
PERFORM and called program that was compiled separately.

My own preference is to use both inline and out-of-line PERFORMs with
both SECTIONs and occasionally PARAGRAPHs where GO TOs are to be used
to exit a PERFORM, which I now find only occasionally useful.
Incidentally the EXIT procedure name facility when available will
eliminate this use of the GO TO statement though with a little more
verbosity.  Program flow would never be designed to "drop through"
from one SECTION to another.  I would also aim to have sections of
around 40 lines of code or whatever would reasonably fit on a page or
screen, this tends to balance the overhead of the control structures
with the code to provide function.  This also makes the logic of the
control structures easier to comprehend as one doesn't then have to
turn many pages or screens to find the terminating part of the
component.  The use of meaningful procedure and data names tends to
make such code reasonably intelligible to the point that comments are
often unnecessary.

Robert
```

###### ↳ ↳ ↳ Re: PERFORM and performance

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-29T14:13:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com>`

```
On Aug 30, 7:34 am, Robert <0robert.jo...@gmail.com> wrote:
>
> I think I see the development of the two extremes of gross abuse of
…[41 more quoted lines elided]…
> often unnecessary.

While you start by stating that there are "two extremes of gross
abuse .." that lead to cans of worms, you then describe how you muddle
along in the middle using, it seems, every variety of structure on a
arbitrary 'as I feel like' basis. You sometime use 'PERFORM section'
and sometimes 'PERFORM paragraph'. Occasionally you use a 'GO TO
exit', at others 'EXIT section/paragraph'.

You mention that you limit the size of procedures because of the issue
of "find[ing] the terminating part of the component".

It seems that you no clear plan of how to construct programs in ways
that make it easy to understand or maintain and simply make each
situation have an arbitrary solution because that is the least effort
at that point.

COBOL was originally created to incorporate all the programming
techniques of the then current programmers mainly used assembler plus
some early autocoders. Partly this was to provide easy transfer of
skills and partly because these mechanisms were suitable to create
efficient code on the computers at that time.

Later, some more modern techniques were added but most early
mechanisms remained (hopefully ALTER has gone entirely).

Modern languages were developed to be much more easily maintainable by
restricting the ways that elements could be used. For example in C
(and almost every later language) a procedure (function) name can
_only_ be executed. It cannot be 'dropped into' or 'gotoed'. The
physical 'terminating point' is clearly defined, it is the next
procedure, they cannot be combined (by, eg, THRU or SECTION).

By using a limited set of structures in COBOL one can create a
guarantee about some aspects of the code so the 'the next programmer'
can more readily understand the code in localized areas.  For example
if a program only had one form for the PERFORM then the next
programmer would be able to appreciate the scope of that without
having to "turn many pages or screens to find the terminating part".

If, eg, every PERFORM was of a SECTION (and never a paragraph) then it
is only necessary to scan for the next SECTION keyword. If they are
always PERFORM name THRU name-EXIT where these are paragraphs then it
is the name-EXIT that is looked for. It it is exclusively PERFORM
paragraph then the next label is the end of the scope.

The problem then becomes how does one check that this has been
followed correctly. For example if one keyword SECTION had been
accidentally omitted from a label then the PERFORM of that label will
work correctly (assuming no spurious labels exist) but the PERFORM of
the SECTION above will also incorporate this paragraph. It may be that
the resulting error is not noticeable in testing and may not even
affect the results in live running - until some exception happens at
2am.

Your use of procedure division COPYbooks may make this even more
difficult to detect. A program may detect the mis-coding but the only
sure way is to manually inspect every PERFORM and check specifically
for the keyword.

OTOH if the PERFORMs had all been of paragraphs the a simple text
search or grep can assure that there are no SECTION keywords in PD and
thus there is no mixture of PERFORM SECTION and PERFORM paragraph.

If, for example, the program uses PERFORM name THRU name-EXIT
consistently then the next programmer can be assured about the
"terminating part". The problem then is that the name and name-EXIT
must match exactly in both the PERFORM statement and within the
PERFORM scope. If, accidentally, the PERFORM was miscoded as PERFORM
A1011 THRU A1101-EXIT then this may work as written, but it just
happens to drop through a few extra paragraphs which may, or may not,
be detectable in testing.

A more subtle problem exists when the miscoding is of the form:

     A1011.
         If very-rare-condition
             GO TO A1101-EXIT.
         blah blah
     A1011-EXIT.

Again it may be months before there is a call at 2am.

Again programs can examine the code and find these errors, the
compiler certainly won't (unless the miscode is of names that don't
exist). The only other option is exhaustive manual checking of every
line.

Of course if the THRU option is discarded then a simple text search or
grep can show that the keyword THRU (or THROUGH) does not exist. A
search or grep can show that GO does not exist so there can be no
miscoded GO TOs.

I code my programs so that, like modern languages, there is only _one_
way that a block of code can be executed, there is only _one_
mechanism for the "terminating part", and these are provable using
simple tools.

It was initially quite difficult to restrict myself and apply
sufficient discipline to the task, but the results have proven
themselves time and again to reduce my own coding errors and this
results in less development time and more reliable code. More
importantly is is much more easily maintained.

Now, as long as I don't have to work on your code, I have no interest
in how you write it but I do urge you to choose _one_ mechanism,
whether that be PERFORM SECTION or PERFORM THRU or GO TO, and stick to
it and avoid all this random structuring on an arbitrary basis.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 4)_

- **From:** Robert <0robert.jones@gmail.com>
- **Date:** 2010-08-29T16:02:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a963ec2-608e-4b6d-8c08-66b233ed32b1@q22g2000yqm.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com>`

```
On Aug 29, 10:13 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Aug 30, 7:34 am, Robert <0robert.jo...@gmail.com> wrote:
>
…[153 more quoted lines elided]…
> it and avoid all this random structuring on an arbitrary basis.

my apologies the following text

> > My own preference is to use both inline and out-of-line PERFORMs with
> > both SECTIONs and occasionally PARAGRAPHs where GO TOs are to be used
…[3 more quoted lines elided]…
> > verbosity.

Should have said "... to exit a SECTION ..." instead of "... to exit a
PERFORM ...".  I don't personally like PERFORM THRU because of the
verbosity, but would conform with the style of pre-existing code when
changing programs.

What I really dislike are inline nested PERFORMs and EVALUATEs that
ramble over several pages.

RJ
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-29T17:26:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5aa40293-cb23-45e2-95bc-3466a2ebf7b9@k1g2000prl.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <3a963ec2-608e-4b6d-8c08-66b233ed32b1@q22g2000yqm.googlegroups.com>`

```
On Aug 30, 11:02 am, Robert <0robert.jo...@gmail.com> wrote:
> On Aug 29, 10:13 pm, Richard <rip...@Azonic.co.nz> wrote:
>
…[167 more quoted lines elided]…
> changing programs.

It isn't the 'verbosity' that should be concerning, that is a trivial
issue compared to having reliable and maintainable programs.

The use of 'EXIT SECTION/PARAGRAPH' is, to me, also a bug trap. For
example the compiler doesn't, and can't, discriminate between these.
If, for example there is bad code that is:

        A SECTION.
           PERFORM Ax
           GO TO Ay.
        Ax.
           ....
               EXIT SECTION.
        Ay.
        B SECTION.

the result may not be obvious or what was intended. Consider also what
would happen if there was a 'PERFORM Ax' outside the A SECTION. In
fact any 'EXIT something' must be checked manually to determine what
could happen, and this may involve checking the whole program.

> What I really dislike are inline nested PERFORMs and EVALUATEs that
> ramble over several pages.

One likes what one is used to. One dislikes what one finds confusing
because of lack of familiarity.

Nested inline PERFORMs could have been written because the alternative
was 'too expensive' in terms of coding effort. If the 'shop standard',
for example, requires that every out-of-line procedure should be of a
SECTION with an name-EXIT, and this shall be allocated a number to go
with the name that represents the hierarchy, and the code shall be
placed into its position determined by that hierarchy; then I can see
the programmer saying "sod it, this can go in-line".

I did have one program that was a very large Windows GUI (full
graphics: profiles, graphs, even a perspective view) that had an
EVALUATE on the callback that ran to 1500 lines or more. But this was
not a problem at all because each WHEN was specifically for a message
so these could be treated as if they were separate sections of code.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-30T12:43:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e0d6dFtsnU1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com>`

```
Richard wrote:
> On Aug 30, 7:34 am, Robert <0robert.jo...@gmail.com> wrote:
>>
…[150 more quoted lines elided]…
> it and avoid all this random structuring on an arbitrary basis.

Hear! Hear!

This post makes very good cases as toWHY a particular form of coding should 
be adhered to, rather than just a style war based on "I do it this way..."

Not only that, but the points made are equally applicable across different 
languages and not just COBOL.

The bottom line is that if consistency of coding style is maintained (even 
though there may be risks inherent in it, as outlined above) there is a 
fighting chance that the code can be maintained more easily and will be less 
error prone than if every kind of possible construct is used willy-nilly.

Pete.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-29T22:21:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6094095-e5d1-4585-b863-484f75d6cc53@s24g2000pri.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net>`

```
On Aug 30, 12:43 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Aug 30, 7:34 am, Robert <0robert.jo...@gmail.com> wrote:
…[156 more quoted lines elided]…
> be adhered to, rather than just a style war based on "I do it this way..."

"I do it this way..." is _NOT_ a style war. 'You should do it this
way' or 'My way is better' is.


> Not only that, but the points made are equally applicable across different
> languages and not just COBOL.

Some of what I said is not relevant to many other languages because
these restrict the way that code can be written. However, many other
languages do have other, different ways that are not relevant to
COBOL.


> The bottom line is that if consistency of coding style is maintained (even
> though there may be risks inherent in it, as outlined above) there is a
> fighting chance that the code can be maintained more easily and will be less
> error prone than if every kind of possible construct is used willy-nilly.

The main issue that I have (being lazy) is that if I have to look at
another's code, which in fact I will have to do over the next week or
so to sort out changes in GST, then I want to be able to look at the
smallest possible part of that code that achieves the changes.

Original coders may tend not to worry much about localizing logic
because they understand the complete program. When I am the 'next
programmer' I need to be assured that I can make certain assumptions
without having to examine every line of code in the program.

Typically I will look at a label and ask 'what are the logic flows
around this label'. Potentially in COBOL (but not in many other
languages) a label can be the target of PERFORM, THRU (of a PERFORM),
GO TO, or drop through. In arbitrary cases I can only determine which
actually occur by detailed examination of every line of code and
tracing through the whole logic path.

Aside: If there were to be ALTERs referencing the label then that adds
yet another complexity in that a complete trace using a set of data
may be required to see when, or if, the ALTERs were ever reached and
how that changed the flow after that happened. I have been fortunate
in that any programs that did have an ALTER (I recall in the early 70s
such a set did arrive in the office), I was able to avoid completely.

If there are guarantees that particular constructs never occur then
the examination of the program can be reduced by those factors. But
how do we receive such a guarantee that is actually valid and true. It
is relatively easy to eliminate some contructs by text search for '
SECTION', ' GO ', ' THRU ' but it is not generally possible, without
special programs, to verify consistency when these are used.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-08-30T10:24:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net>`

```
On Mon, 30 Aug 2010 12:43:55 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Richard wrote:
>> On Aug 30, 7:34 am, Robert <0robert.jo...@gmail.com> wrote:
…[166 more quoted lines elided]…
>Pete.

Totally agree.  And really, is there a real reason or purpose to have
SECTIONs in a program that doesn't contain a SORT INPUT/OUPUT
PROCEDURE or the even more rare REPORT Section?  Aren't paragraphs
sufficient?

Regards,
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 6)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-08-30T11:47:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com>`

```
"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com...
> On Mon, 30 Aug 2010 12:43:55 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
>
<snip>
> Totally agree.  And really, is there a real reason or purpose to have
> SECTIONs in a program that doesn't contain a SORT INPUT/OUPUT
> PROCEDURE or the even more rare REPORT Section?  Aren't paragraphs
> sufficient?
>
Thre isn't any requriement to have SECTIONS in the Procedure Division for 
either SORTs with INput/Output Procedures or Report Writer, either.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-30T11:17:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bspn7650bjd4nn7n4b9meb270tro6kha4e@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com>`

```
On Mon, 30 Aug 2010 11:47:02 -0500, "Bill Klein"
<wmklein@noreply.ix.netcom.com> wrote:

>Thre isn't any requriement to have SECTIONS in the Procedure Division for 
>either SORTs with INput/Output Procedures or Report Writer, either. 

I wouldn't be surprised if there aren't some compilers still in use
that still require SECTIONs for these.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 7)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2010-08-30T20:09:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tho761749k7v09palqsmpe11f24enjgpo@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com>`

```
On Mon, 30 Aug 2010 11:47:02 -0500, "Bill Klein"
<wmklein@noreply.ix.netcom.com> wrote:

>"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
>news:bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com...
…[11 more quoted lines elided]…
>
Whenever I went on a contract, was always dismayed to see SECTION's
used in the code and happy when not there. From ancient recall,
SECTION usage sites were outweighed 5:1 if not higher.
Graham H
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-31T00:40:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5hj1s$kqj$2@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com>`

```
In article <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com>,
Graham Hobbs  <ghobbs@cdpwise.net> wrote:

[snip]

>From ancient recall,
>SECTION usage sites were outweighed 5:1 if not higher.

I'm not sure what unit of weight is being employed here... but I recall 
that SECTIONs were efficient back in the days when Applications 
Programmers had to write code to fit into paging-restrictions.

(Personally I have managed to Keep Up With the Times to such a point as I 
don't shudder over the thought of excessive code-page swapping... but I 
still get the jim-jams (nigh unto the collywobbles) at the sight of a 
backwards-referring PERFORM.)

DD
```

###### ↳ ↳ ↳ Sec tion vs Paragraphs (was: PERFORM and performance

_(reply depth: 8)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-08-30T19:45:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com>`

```
"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
news:6tho761749k7v09palqsmpe11f24enjgpo@4ax.com...
> On Mon, 30 Aug 2010 11:47:02 -0500, "Bill Klein"
> <wmklein@noreply.ix.netcom.com> wrote:
<much snippage>
> Whenever I went on a contract, was always dismayed to see SECTION's
> used in the code and happy when not there. From ancient recall,
> SECTION usage sites were outweighed 5:1 if not higher.
> Graham H

As I have previously stated in this forum, when I used to work for/with 
vendors, I found a very funny (to me) distinction.  In the US, it was very 
common to see code with only paragraphs (no sections) and in Europe 
(partiuclarly the UK) it was highly common to see all sections, no (or 
minimal) paragraphs.

I never found the real origin of this distinction,, but it was quite common 
(but certainly NOT universal)
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs (was: PERFORM and performance

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-31T15:27:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e3b4aFc6cU1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`

```
Bill Klein wrote:
> "Graham Hobbs" <ghobbs@cdpwise.net> wrote in message
> news:6tho761749k7v09palqsmpe11f24enjgpo@4ax.com...
…[15 more quoted lines elided]…
> common (but certainly NOT universal)

That gels precisely with my experience too. Australia and NZ seem to follow 
Europe in this regard, rather than the USA. As Bill notes, it isn't 
universal but a general trend.

Pete.
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs (was: PERFORM and performance

_(reply depth: 9)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2010-08-31T00:02:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rdvo76hivmlprvrpjcrc9r5dk2594aeo63@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`

```
On Mon, 30 Aug 2010 19:45:50 -0500, "Bill Klein"
<wmklein@noreply.ix.netcom.com> wrote:

>"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
>news:6tho761749k7v09palqsmpe11f24enjgpo@4ax.com...
…[16 more quoted lines elided]…
>
Didn't know that - the one place I had to use SECTION's was the UK,
all other eperiences were North America and no SECTION's at all.
Graham H
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs (was: PERFORM and performance

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-31T08:08:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j33q76d8mlu37m8b0mtonql97niu83kdjf@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`

```
On Mon, 30 Aug 2010 19:45:50 -0500, "Bill Klein"
<wmklein@noreply.ix.netcom.com> wrote:

>As I have previously stated in this forum, when I used to work for/with 
>vendors, I found a very funny (to me) distinction.  In the US, it was very 
>common to see code with only paragraphs (no sections) and in Europe 
>(partiuclarly the UK) it was highly common to see all sections, no (or 
>minimal) paragraphs.

I once worked (at EDS), where our local standard which they hoped to
make company wide was to have sections that each had an exit
paragraph.    I did not like that standard at all.
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs (was: PERFORM and performance

_(reply depth: 10)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-01T04:23:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2314628c-575e-4ed1-9732-08e0e905bfdf@f25g2000yqc.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com> <j33q76d8mlu37m8b0mtonql97niu83kdjf@4ax.com>`

```
On Aug 31, 3:08 pm, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 30 Aug 2010 19:45:50 -0500, "Bill Klein"
>
…[10 more quoted lines elided]…
>

That is the standard that I use. I love it coz I can insert go to
exits to keep the in-stream code simple.
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs

_(reply depth: 9)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T10:47:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c82076f$0$6274$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com>`

```
Am 31.08.2010 02:45, schrieb Bill Klein:
> As I have previously stated in this forum, when I used to work for/with
> vendors, I found a very funny (to me) distinction.  In the US, it was very
…[5 more quoted lines elided]…
> (but certainly NOT universal)

   Using SECTIONS makes a COBOL program look like a real programming 
language (ahem).

   One can be sure, that nobody can change the logic of the program by 
inserting a SECTION somewhere up or down the line, i.e. introduce a 
higher level structuring than the low level one (paragraph) one uses.

   My COBOL programs are structured into SECTIONs, and each SECTION has 
the same initial paragraph called ANFANG (German for "Begin"). The first 
section would be called HAUPT SECTION (haupt: GErman for "main").

   When I had to use COBOL'74, i.e. without proper structuring, sections 
might have had a final paragraph called ENDE (German for "end") with 
EXIT as the only instruction, so that an unavoidable GOTO (without COME 
FROM) could GOTO ENDE.

   Also the HAUPT (main) SECTION used to have an ENDE paragraph for the 
STOP PROGRAM or RETURN statement (which had to be in a paragraph by 
itself, I believe to remember correctly).

   All just a spell against spaghetti programming jumping back and forth 
thru the program code.


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: Sec tion vs Paragraphs

_(reply depth: 10)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T14:47:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c823fc9$0$6274$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<4c82076f$0$6274$6e1ede2f@read.cnntp.org>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <fgReo.72008$MG3.66596@en-nntp-16.dc1.easynews.com> <6tho761749k7v09palqsmpe11f24enjgpo@4ax.com> <7hYeo.72691$Yn5.31587@en-nntp-14.dc1.easynews.com> <4c82076f$0$6274$6e1ede2f@read.cnntp.org>`

```
Am 04.09.2010 10:47, schrieb Lï¿½ko Willms:
>    My COBOL programs are structured into SECTIONs, and each SECTION has
> the same initial paragraph called ANFANG (German for "Begin"). The first
> section would be called HAUPT SECTION (haupt: GErman for "main").

>    Also the HAUPT (main) SECTION used to have an ENDE paragraph for the
> STOP PROGRAM or RETURN statement (which had to be in a paragraph by
> itself, I believe to remember correctly).

   After reading some more contributions to this thread, I want to add 
that, of course, PERFORM something THRU something-else is absolutely 
prohibited in the programs I am and have been responsible for.

   The above structuring makes also sure, that the program ends when its 
execution has reached the main section, and that there is no fall thru 
to other parts of the program, and other parts of the code can and will 
only be executed by a PERFORM this-or-that-section, and that thus a fall 
thru to other sections is excluded.

   Using the upper-most possible level of code structuring in COBOL 
(within the same source code unit), i.e. SECTION, assures the casual 
reader of the program, that those basic units of the program are not 
accidentally part of a larger SECTION, so that the code which she or or 
he thinks will be only executed as a single paragraph, cannot be 
executed as fall thru section of a PERFORM on the level of a SECTION.


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-31T13:37:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e34moFe1hU1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com>`

```
SkippyPB wrote:
> On Mon, 30 Aug 2010 12:43:55 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[181 more quoted lines elided]…
> sufficient?

This is one that has been argued to death here over the years. Personally, I 
like SECTIONS but most of that is historical and stems from force of habit. 
It is like what Richard says about familiarity.

Since moving away from COBOL I have been exposed to new concepts that have 
broadened my vision, and I like to think I am a better programmer now than I 
was. (Still learning... :-)). As understanding grows, it becomes apparent 
that arguing over branching conventions in program code is a bit like 
arguing over whether an umbrella is more useful than a raincoat, when you 
live in the Sahara desert...(Yes, an umbrella could be pressed to service as 
a parasol, but a raincoat could be a useful groundsheet... Neither of them 
have particular relevance to the purpose for which they were created, if it 
hardly ever rains...  you catch my drift.)

I don't think using SECTIONs is better than using PARAGRAPHS; in a COBOL 
context it really doesn't matter as long as the use is CONSISTENT. (And that 
is the gist of this thread.)

On the extremely rare (almost never...) occasions when I still need 
procedural code in COBOL, I NEVER perform a paragraph, or use THROUGH/THRU, 
and anyone maintaining my code can know with complete certainty that an out 
of line PERFORM will be to a SECTION.
They can also be certain that, in the unlikely event of GO TO being 
encountered it will NEVER be to anywhere outside the SECTION.

It works for me, but most of the work I do now is in C# anyway and I have 
never used GO TO in that language. The PERFORMED SECTIONS of COBOL (loosely) 
become object methods in C# which don't need to branch anywhere (not even 
within themselves, usually). There are other considerations about partial 
Classes, PRIVATE, PUBLIC, and STATIC modifiers, which all have a bearing on 
why you don't need branching. Code is created in clearly defined blocks, 
sequential, logical and straightforward. The IDE makes it easy to maintain 
by allowing you to "disappear" (collapse) parts you are not interested in so 
you don't have to scroll through dozens of lines of code that have no 
relevance to what you are looking at. Sometimes when maintaining legacy 
COBOL I go to collapse a region, then realise I can't...

Matters of style are seldom right or wrong.

Consistency is generally "right" because even if something is found to be 
"wrong" much later on, it is far easier to fix if it has been consistenly 
applied than if it hasn't.

Pete.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-30T23:10:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<020852be-b5c8-46f7-b097-5f480343ab86@l38g2000pro.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net>`

```
On Aug 31, 1:37 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> This is one that has been argued to death here over the years. Personally, I
> like SECTIONS but most of that is historical and stems from force of habit.
…[21 more quoted lines elided]…
> encountered it will NEVER be to anywhere outside the SECTION.

They may may be maintaining it to eradicate a bug. Do you also claim
"with complete certainty" that there are no bugs ?

What independent method did you use to verify that your assurances
made "with complete certainty" are, in fact, true ?

It is not that I doubt you, but when I am given another's program to
maintain I don't trust any assurances that are not objectively
verifiable.

> It works for me, but most of the work I do now is in C# anyway and I have
> never used GO TO in that language. The PERFORMED SECTIONS of COBOL (loosely)
…[7 more quoted lines elided]…
> relevance to what you are looking at.

> Sometimes when maintaining legacy
> COBOL I go to collapse a region, then realise I can't...

That is not an attribute of the language but is of the tools that you
use. Folding editors are available, and have been for several decades.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-08-31T23:34:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e47lrFbfvU1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <020852be-b5c8-46f7-b097-5f480343ab86@l38g2000pro.googlegroups.com>`

```
Richard wrote:
> On Aug 31, 1:37 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[28 more quoted lines elided]…
> "with complete certainty" that there are no bugs ?

Why would I do that? I certainly have programs which have been running on 
various sites for decades and never crashed. All that means is that they 
haven't crashed yet. Anyone who has been programming for some time knows 
that the fact that a program consistently runs correctly does not mean it 
has no bugs in it. It can mean it has "No Known Bugs"...

And I have been contacted occasionally by people maintaining code I wrote 20 
years ago. Usually to confirm some background aspects of how things work, 
not because the code was unintelligible.(In fact, I've had comments from 
people saying they found the code easy to maintain and learned something by 
doing so.)

>
> What independent method did you use to verify that your assurances
> made "with complete certainty" are, in fact, true ?

I wrote the code. I know what it does. And I know why it does things the way 
that it does. Anyone else can either take my word for it or not. It really 
isn't my problem.

>
> It is not that I doubt you, but when I am given another's program to
> maintain I don't trust any assurances that are not objectively
> verifiable.

And that is entirely a matter for you.  I have no problem with people 
doubting my assurance or not. In fact,  I think anyone maintaining code 
should take whatever steps they need to, to assure themselves of the state 
of it. Taking such steps with my code will simply show that what I said is 
true.
>
>> It works for me, but most of the work I do now is in C# anyway and I
…[15 more quoted lines elided]…
> use. Folding editors are available, and have been for several decades.

Not with the Fujitsu COBOL IDE, which is what I use for COBOL. I never said 
it was an attribute of the language; I merely said that "Sometimes when 
maintaining legacy COBOL I go to collapse a region, then realise I can't..." 
It is a simple statement of fact and not intended to be contentious.

If it really bothered me I could certainly move to an independent editor 
like Eclipse, but then I would lose some of the integration I get from the 
Fujitsu IDE. The difference is that with Visual Studio (which is what I use 
for C#) I get integration AND decent editing features. I simply don't have 
that currently with COBOL.

Actually, it wouldn't be too hard to write a COBOL plugin for Visual Studio 
and I suspect that's what Fujitsu have done for NetCOBOL for .Net.

Pete.
 -- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-31T08:17:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3n3q76tj04qkmkr47lqgfos3nfn51iqljl@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <020852be-b5c8-46f7-b097-5f480343ab86@l38g2000pro.googlegroups.com> <8e47lrFbfvU1@mid.individual.net>`

```
On Tue, 31 Aug 2010 23:34:17 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>And I have been contacted occasionally by people maintaining code I wrote 20 
>years ago. Usually to confirm some background aspects of how things work, 
>not because the code was unintelligible.(In fact, I've had comments from 
>people saying they found the code easy to maintain and learned something by 
>doing so.)

If I get a question like that, my answer is "Let me read the code and
documentation".   My memory won't do the job.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-09-01T02:55:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e4jedFkc0U1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <020852be-b5c8-46f7-b097-5f480343ab86@l38g2000pro.googlegroups.com> <8e47lrFbfvU1@mid.individual.net> <3n3q76tj04qkmkr47lqgfos3nfn51iqljl@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 31 Aug 2010 23:34:17 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> documentation".   My memory won't do the job.

Funny you should say that. I had just such a query today. Not for 20 
year-old code but code that was in OO COBOL. It is a complex application and 
the first thing I did was reach for the delivery documentation I wrote at 
the time, and  retrieved the source code from an archive. The delivery 
document was aimed at a maintenance programmer and explained why certain 
approaches were taken and gave details that a programmer would need to know. 
Page 14 of it exlpained exctly what the guy was asking and page 18 of it had 
the solution to another problem that he had been trying to solve for some 
time. (it was ironic but I had actually written this in red, as it was so 
critical.)

His problem was not with understanding my code, it was with understanding 
the COBOL approach (he is not an experienced COBOL guy although he is an 
excellent programmer in other languages). I had been preparing to dive into 
the application and run his problem down but there was really no need. It 
was all in the documentation. He had read the release documentation when he 
took delivery but at that point, it just hadn't gelled. I always provide 
conceptual diagrams as well as documenting file and DB usage and interfaces 
and components. He apologised for overlooking the fact that what he needed 
to know was in the documentation, but I think it was understandable. It's 
only when you really get into something that the documentation makes sense.

I completely agree that memory cannot be relied on (especially as the years 
advance) but the detals of a complex system design are not as simple as the 
rules you apply when writing code. I don't have to remember every line of 
code I ever wrote to know that I only perform SECTIONs out of line, etc. It 
is so instinctive for me that any deviation would definitely be memorable. 
:-)

I should probably mention that my comments apply ONLY to code I have control 
over. I have worked on sites where they had different standards and I 
obviously complied with what they required. However, in developing my own 
code base (and sometimes on other sites too) I have been free to code as I 
see fit and the way I see fit is as previously described.

Pete.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 9)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T11:33:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c821247$0$6277$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<8e47lrFbfvU1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <020852be-b5c8-46f7-b097-5f480343ab86@l38g2000pro.googlegroups.com> <8e47lrFbfvU1@mid.individual.net>`

```
Am 31.08.2010 13:34, schrieb Pete Dashwood:
> Actually, it wouldn't be too hard to write a COBOL plugin for Visual Studio
> and I suspect that's what Fujitsu have done for NetCOBOL for .Net.

   Micro Focus has done it.


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-31T08:15:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<193q76h9glkahuf3esg9o3e9so003ftsvp@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net>`

```
On Tue, 31 Aug 2010 13:37:26 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>On the extremely rare (almost never...) occasions when I still need 
>procedural code in COBOL, I NEVER perform a paragraph, or use THROUGH/THRU, 
…[3 more quoted lines elided]…
>encountered it will NEVER be to anywhere outside the SECTION.

Maybe they can be certain.   But I find it is dangerous to be certain
of such things without actually checking.

I have seen problems with unexpected drop through code than in
unexpected early ending of performed code.    I know that one can
program with sections and treat them the same as paragraphs, with no
drop-through code, but without the old memory-segmentation use of
sections, I don't see the advantage of this.

The big advantage of sections is at places which don't have EXIT
PARAGRAPH.   They can use a GO TO to get to the exit paragraph.   But
with a more modern compiler, that advantage goes away, and we can get
rid of drop-through code.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-09-01T03:37:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e4ltmF4j6U1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <193q76h9glkahuf3esg9o3e9so003ftsvp@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 31 Aug 2010 13:37:26 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> of such things without actually checking.

Fine. I already covered that elsewhere. I don't think you (or Richard) are 
wrong for wanting to check; but it doesn't make my statement any less true 
:-).

I really don't care whether you guys believe me or not; (although it would 
be nice to think I have some credibility after decades of posting here 
(including samples of code) - but if not, well, it is Usenet... I can't get 
unwrapped about it...)  I just stated what I do.I don't care if other people 
adopt the same approach or not, I don't care how other people write COBOL, 
and I don't care how they maintain COBOL  It simply isn't my problem.

What IS my problem is ME being able to maintain what other people write, and 
I made a living doing that for many years. I don't care whether they use 
SECTIONS or PARAGRAPHS or write spaghetti code or use complex constructs and 
nestings. It is only COBOL. I'm a COBOL programmer; bring it on...

> I have seen problems with unexpected drop through code than in
> unexpected early ending of performed code.    I know that one can
…[7 more quoted lines elided]…
> rid of drop-through code.

I'm wearying of this discussion and won't be responding further. I "got rid 
of drop-through code" 30 years ago. I just don't see it as important enough 
to make a deal about. In fact it's kind of sad that something as trivial as 
branch control in COBOL has occupied the time and space it has here. I'm 
sorry I allowed myself to be sucked in.

Pete.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-31T10:42:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hhbq76l63ak9nl5bd0ubg5q9brgcipv7md@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <193q76h9glkahuf3esg9o3e9so003ftsvp@4ax.com> <8e4ltmF4j6U1@mid.individual.net>`

```
On Wed, 1 Sep 2010 03:37:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:


>> Maybe they can be certain.   But I find it is dangerous to be certain
>> of such things without actually checking.
…[10 more quoted lines elided]…
>and I don't care how they maintain COBOL  It simply isn't my problem.

OK.   But in my workplace, how others do maintenance on my code *is*
my problem.    

>What IS my problem is ME being able to maintain what other people write, and 
>I made a living doing that for many years. I don't care whether they use 
>SECTIONS or PARAGRAPHS or write spaghetti code or use complex constructs and 
>nestings. It is only COBOL. I'm a COBOL programmer; bring it on...

I'm adjustable.   But I need to anticipate how others will be
maintaining my code.   They don't have share my preferences.   They
shouldn't have to have my techniques to avoid problems.    But if they
stick in a line of code to PERFORM 2010-tax-check, and add a new
paragraph somewhere, I don't want that 2010-tax-check paragraph to be
accidentally part of 2009-ledger-check.

I've been burned that way before.


>I'm wearying of this discussion and won't be responding further. I "got rid 
>of drop-through code" 30 years ago. I just don't see it as important enough 
>to make a deal about. 

That's fine - but others are reading this thread as well.

>In fact it's kind of sad that something as trivial as 
>branch control in COBOL has occupied the time and space it has here. 

I don't know the criteria you use to determine whether something is
trivial.   For me, if someone makes a change to my program to cause me
to be called in the middle of the night - it's not trivial.

>I'm sorry I allowed myself to be sucked in.

I'm sorry you feel that way.    What would you like to be discussing
instead?
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 9)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T14:41:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c823e3a$0$6277$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<8e4ltmF4j6U1@mid.individual.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com> <8e34moFe1hU1@mid.individual.net> <193q76h9glkahuf3esg9o3e9so003ftsvp@4ax.com> <8e4ltmF4j6U1@mid.individual.net>`

```
Am 31.08.2010 17:37, schrieb Pete Dashwood:

> . In fact it's kind of sad that something as trivial as
> branch control in COBOL has occupied the time and space it has here.

   The problem is with COBOL -- there was no proper way of doing it in 
COBOL before compilers according to the 1985 standard hit the market. 
COBOL has a genetic defect in this respect, I might say, suffering from 
a too much Assembler look of those developing it. So it is 
understandable that the debate about how to overcome these inherent 
weeknesses of COBOL always occupy a large part of the discussions among 
COBOL programmers.

   Don't mind...


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-04T03:05:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0882c5d-e26c-4838-a888-badc4321f6b6@e14g2000yqe.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <0d61d264-e722-4024-a58c-8cb40ca166b7@x25g2000yqj.googlegroups.com> <91c90e7e-694f-4f06-9480-32af25bc8413@q16g2000prf.googlegroups.com> <8e0d6dFtsnU1@mid.individual.net> <bkfn761nmlidgv2e1nck189v49opnffvrp@4ax.com>`

```
On Aug 30, 3:24 pm, SkippyPB <swieg...@Nospam.neo.rr.com> wrote:
> On Mon, 30 Aug 2010 12:43:55 +1200, "Pete Dashwood"
>
…[178 more quoted lines elided]…
> sufficient?

Back in Doc's Golden Daze, I had occasion to modify a spaghetti
encoded Cobol program with rampant PERFORM ... THRU code structures.
More experienced programmers had already added SECTIONs at the tail of
the program as their way of adding code which they knew would not be
accidentally dropped into. I did the same. It was the safest solution
and more economic than spending 6 weeks trying to understand the
convoluted knottage of code.
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2010-08-30T16:37:59-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
On Thu, 26 Aug 2010 16:37:15 +0200, Fritz Wuehler
<fritz@spamexpire-201008.rodent.frell.theremailer.net> wrote:

>> I would be VERY interested in any current documentatin indicating that
>> the PERFORM statement (with any compiler) has "bad performance". 
…[11 more quoted lines elided]…
>at other versions.

As someone who has looked carefully at the code generated by PERFORM
on IBM 360/370/390/z series systems, starting with VS COBOL II 1.4,
the first Ansi 85 IBM compiler the ball game changed.  On COBOL VS (74
standard) and prior there were statements like
    MVC save_exit_address,exit_address
    MVC exit_address,return_address
    L R15,perform_paragraph_start
    BR R15
return_point DS 0H
    MVC exit_address,save_exit_address.  

There would be a 
    L R15,exit_address
    BR R15 
at the end of the perform range.  With COBOL 85, if the paragraph
being performed is single entry, single exit the perform is simplified
and depending on various algorithms the performed paragraph may be
moved inline with all perform code eliminated.  PERFORM varying went
from being a pig to having very efficient code.  PERFORM x THRU x-exit
probably is suboptimal.  In short, I changed my coding practices to
make sure all GO TO statements were eliminated because they mess up
PERFORM optimization.  Code optimization I did that saved substantial
time on a compute bound run for COBOL VS would have to have be redone
to take advantage of the PERFORM optimization in VS COBOL II release
1.4 and newer.  I am glad that I noted the possibility in an article I
had published on code optimization in the Naaspa magazine in 1991 or
1992 (I can't remember the title).

Clark Morris
>
>Consider a typical scenario processing a ten million record file. For each
…[16 more quoted lines elided]…
>of designing and coding, at least in the IBM environment.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-08-30T14:28:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e6d2a790-e71e-48f8-a857-16115f1f3c39@x20g2000pro.googlegroups.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com>`

```
On Aug 31, 7:37 am, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Thu, 26 Aug 2010 16:37:15 +0200, Fritz Wuehler
>
…[42 more quoted lines elided]…
> 1992 (I can't remember the title).

So, you are saying that it isn't that PERFORM is worse than GO TO in
performance but that PERFORM that has GO TOs in it is worse (because
it can't be optimized).

This seems to lead to a conclusion that 'eliminating GO TO' can give
better performance than 'eliminating PERFORM'.

I doubt though that Fritz will change his mind.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

- **From:** docdwarf@panix.com ()
- **Date:** 2010-08-31T00:32:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5hijj$kqj$1@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com>`

```
In article <021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Thu, 26 Aug 2010 16:37:15 +0200, Fritz Wuehler
><fritz@spamexpire-201008.rodent.frell.theremailer.net> wrote:
…[9 more quoted lines elided]…
>>recall, it generates 9 or ten instructions including front and back end.

[snip]

>As someone who has looked carefully at the code generated by PERFORM
>on IBM 360/370/390/z series systems, starting with VS COBOL II 1.4,
…[15 more quoted lines elided]…
>moved inline with all perform code eliminated.

Mr Morris, you've posted a bit of a PMAP here... I posted a bit of a LIST 
someplace else... and the poster who asserted something about saving 
hundreds and dozens and tens-of-severals of instructions has done neither, 
despite a request or two for such... or even just some COBOL that could be 
run through a compiler or three.

It just might be a Very Wise Thing to wait until the one who made the 
assertion recognises and responds to the responsibility of the onus 
probandi.

DD
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 4)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T11:28:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c8210ed$0$6277$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<i5hijj$kqj$1@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com> <i5hijj$kqj$1@reader1.panix.com>`

```
Am 31.08.2010 02:32, schrieb docdwarf@panix.com:
> Mr Morris, you've posted a bit of a PMAP here... I posted a bit of a LIST
> someplace else... and the poster who asserted something about saving
> hundreds and dozens and tens-of-severals of instructions has done neither,
> despite a request or two for such... or even just some COBOL that could be
> run through a compiler or three.

    Remember what he wrote:

Am 26.08.2010 16:37, schrieb Fritz Wuehler:
 >> The answer is to have a look at the code generated for PERFORM.
 >> If I recall, it generates 9 or ten instructions including front
 >> and back end.

   See the "if I recall"? With the conditional "IF"?


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-09-05T00:19:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5unma$o26$2@reader1.panix.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <021o761cn1mi0h46q0a5mms62bfifdj0oj@4ax.com> <i5hijj$kqj$1@reader1.panix.com> <4c8210ed$0$6277$6e1ede2f@read.cnntp.org>`

```
In article <4c8210ed$0$6277$6e1ede2f@read.cnntp.org>,
L?ko Willms  <lueko.willms@t-online.de> wrote:
>Am 31.08.2010 02:32, schrieb docdwarf@panix.com:
>> Mr Morris, you've posted a bit of a PMAP here... I posted a bit of a LIST
…[12 more quoted lines elided]…
>   See the "if I recall"? With the conditional "IF"?

Already noticed and responded to with Actual Code, so that the frailities 
of memory might not need to be relied on... and if I recall there were 
postings after the original which continued something about 'saving 
hundreds and dozens and tens-of-severals of instructions' with nary a 
scrap of source to support it (along with somve Very Sensitive noticing 
about sarcasm or mean-spiritiedness or overall negativity or a variation 
on one of those themes).

DD
```

##### ↳ ↳ Re: PERFORM and performance

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T10:59:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c820a52$0$6276$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net>`

```
Am 26.08.2010 16:37, schrieb Fritz Wuehler:

   replying to Bill Klein's query:

>> I would be VERY interested in any current documentatin indicating that
>> >  the PERFORM statement (with any compiler) has "bad performance".

> The answer is to have a look at the code generated for PERFORM.

   The question actually was not, if such documentation warning against 
using PERFORM is true and well founded (for that compiler and system), 
but if there is such warning in the documentation provided by the 
compiler maker.

   To answer that, frankly, I haven't found any such warning in the at 
my time current COBOL compiler manuals of the three Sperry Univac 
systems I had worked on (on OS/1100 only COBOL'74, i.e. ACOB and 
COBOL'85 i.e. UCOB, not the obsolete "DOD COBOL").


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: PERFORM and performance

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-04T15:48:04+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c824ddd$0$6273$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<4c820a52$0$6276$6e1ede2f@read.cnntp.org>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com> <65c546c531f937e6034a80e58b433db1@msgid.frell.theremailer.net> <4c820a52$0$6276$6e1ede2f@read.cnntp.org>`

```
Am 04.09.2010 10:59, schrieb Lï¿½ko Willms:
>    The question actually was not, if such documentation warning against
> using PERFORM is true and well founded (for that compiler and system),
…[6 more quoted lines elided]…
> COBOL'85 i.e. UCOB, not the obsolete "DOD COBOL").

   Since the above might be misleading, by "the three systems" I meant, 
besides the OS/1100-type machines, the two byte machine series with VS/9 
(Sperry's name for RCa's TSOS) on the one hand and OS/3 on the other.


Cheers,
L.W.
```

#### ↳ Re: PERFORM and performance

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-08-26T09:25:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2c1d769dgb049rafiou1v892mp2s2uogam@4ax.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>`

```
On Thu, 26 Aug 2010 02:47:20 -0500, "Bill Klein"
<wmklein@noreply.ix.netcom.com> wrote:

>I would be VERY interested in any current documentatin indicating that the 
>PERFORM statement (with any compiler) has "bad performance".
…[4 more quoted lines elided]…
>True, but not very useful in practice as a GENERAL rule. 

The first thing to do in designing such guidelines is to agree on the
best criteria for "bad performance".    But that would involve
defining the goals of a program for short and long term and analyzing
costs and benefits.

Even in olden dayz, when programming costs were considered low
relative to hardware costs, we sometimes had to consider trade-offs
between CPU costs, disk costs, tape costs, & even bandwidth costs.

Our DBA used to spend most of his time figuring out how to make small
changes to increase efficiencies.    Nowadays that part of his job has
been replaced with throwing more disk space at the database.   And the
users get a bigger improvement in response time much sooner without
much cost.
```

#### ↳ Re: PERFORM and performance

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-08-26T17:19:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SrGdnYA18dQ7d-vRnZ2dnUVZ_tsAAAAA@earthlink.com>`
- **References:** `<k_odo.95442$Bh.78468@en-nntp-12.dc1.easynews.com>`

```
Bill Klein wrote:
> Just as a follow-up on another thread.
>
…[6 more quoted lines elided]…
> good" COBOL. True, but not very useful in practice as a GENERAL rule.

In the main, the vast majority of cases, it is counter-productive to chase 
micro-efficiencies.

Still, it would be trivial to test:

CALL 'CLOCKON'
PERFORM 1000000 TIMES
  MOVE 'X' TO A
  END-PERFORM
CALL 'CLOCKOFF' USING TIMEIT
DISPLAY TIMEIT

vs. some other code that accomplishes the same work. For example:

   MOVE 0 TO I
   CALL CLOCKON
LOOP.
   ADD 1 TO I
   IF I < 1000000
      MOVE 'X' TO A
      GO TO LOOP.
   CALL 'CLOCKOFF' USING TIMEIT
   DISPLAY TIMEIT
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
