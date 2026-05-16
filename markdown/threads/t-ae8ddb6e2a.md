[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Paragraph Pointers

_24 messages · 12 participants · 2003-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Paragraph Pointers

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-12T19:47:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
I was quite glad to see ALTER removed for 2002.  As a statement, it had one
huge, glaring, fatal, problem -- the failure to return to whence it was
called.

It did offer a sort of prehistoric polymorphism, and it that sense it was
useful.  I got to thinking about it when writing some code like below:

  Perform varying table-ndx from 1 by 1
    until table-ndx > size-of-table

    Evaluate true

      when table-type-1 (table-ndx)
        perform process-type-1

      when table-type-2 (table-ndx)
        perform process-type-2

      when table-type-3 (table-ndx)
        perform process-type-3

      ...

      when table-type-255 (table-ndx)
        perform process-type-255

    End-Evaluate

  End-perform

The evaluate works, but it is tedious both to read and write.  If this were
one of the c or Pascal family-tree languages I would use a table of
function pointers indexed by element-type.  But with Cobol that is not
possible.

Now ALTER would not fix this problem, somewhere in the code I would still
need a 255-way evaluate to alter a single procedure name.  (nor would I use
it, and it would imply an additional 255 go-to-exits pity you couldn't
"ALTER x TO PERFORM y")

But it got me thinking -- what I wanted was a PARAGRAPH-POINTER.

Something I could set via the set statement or in working storage like so:

  5 proc-tab-area.
   10 filler    PARAGRAPH-POINTER value Process-Type-1.
   10 filler    PARAGRAPH-POINTER value Process-Type-2.
   10 filler    PARAGRAPH-POINTER value Process-Type-3.
     ...
   10 filler    PARAGRAPH-POINTER value Process-Type-255.
  5 proc-tab redefines proc-tab-area occurs 255.


Then I could change my overly long evaluate to something shorter, like so:


  Perform varying table-ndx from 1 by 1
    until table-ndx > size-of-table

     Perform Proc-Tab ( table-type (table-ndx) )

  End-perform


So what would CLC think of this idea?  Am I the only person that would find
this useful?

Regards,

Joe Zitzelberger
```

#### ↳ Re: Paragraph Pointers

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-03-13T13:41:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QT%ba.542$Nl6.435428@newssrv26.news.prodigy.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
> But it got me thinking -- what I wanted was a PARAGRAPH-POINTER.
>
> So what would CLC think of this idea?  Am I the only person that would
find
> this useful?

Can't honestly say I've ever had the desire, but for the rare occasion I
might find this useful, multiple entry points in a CALLed subprogram would
seem to suffice.

MCM
```

#### ↳ Re: Paragraph Pointers

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-13T05:55:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303130555.74110cd1@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
Have you considered submitting this via the J4/WG4 call for papers for
the COBOL Expo Workshop?

More details at http://www.cobolreport.com


psychedelic-harry@mindless.com (Joe Zitzelberger) wrote in message news:<16e2f010.0303121947.6c4e0870@posting.google.com>...
> I was quite glad to see ALTER removed for 2002.  As a statement, it had one
> huge, glaring, fatal, problem -- the failure to return to whence it was
…[67 more quoted lines elided]…
> Joe Zitzelberger
```

#### ↳ Re: Paragraph Pointers

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-13T08:00:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4q2tc$mjg$1@slb4.atl.mindspring.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
If you WANTED to do this, you could do it already via nested programs and
CALL identifier, e.g.

  01  All-Programs.
       05  EachProgram occurs 10 times indexed by ind
                        Pic X(08).
  01  Filler redefines All-Programs Pic X(80)  Value
        "Program1Program2Program3 ...."

      ...
Perform varing ind from 1 by 1
            Call EachProgram(Ind)
 end-perform

     ....

I don't see much use for this personally, but it would work (and as I think
Joe comes from an IBM mainframe environment, the call to nested programs
"program1" ... "program9" would be almost as efficient as a PERFORM.
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-13T18:25:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E70CDAC.D58E5382@shaw.ca>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net>`

```


"William M. Klein" wrote:

> If you WANTED to do this, you could do it already via nested programs and
> CALL identifier, e.g.
…[10 more quoted lines elided]…
>  end-perform

Short answer is this type of thing is already available in COBOL 2002 - OO ! Now
question. How long do we keep running non-OO COBOL and OO-COBOL in tandem
introducing features which are specifically geared to one and not the other.

Can we clarify this - is COBOL to remain as what is regarded as a dinosaur by
users of the languages du jour, or does it become COBOL 2002, containing OO and
links to other languages - but still coding in non-OO classes, if that's your
preference, (why go through a huge source code change),  but CALLING/INVOKING
these features from the OO syntax when they apply, rather than having a series
of wise heads chewing the fat on discussing and introducing tandem features.

The other alternative are :-

(a) Stop pissing around and drop OO COBOL
(b) Produce a SEPARATE Standard for OO COBOL

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-13T10:43:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303131043.53a80fde@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net>`

```
You are quite correct.  That works great.

I was so busy trying to find an out-of-the-box solution that I forgot
that I could do a dynamic call to a nested program just as easily. 
Somewhere in the course of trying to point a Procedure-Pointer at a
nested program I got it into my head that they were static only.

Thanks for the fix.

"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<b4q2tc$mjg$1@slb4.atl.mindspring.net>...
> If you WANTED to do this, you could do it already via nested programs and
> CALL identifier, e.g.
…[16 more quoted lines elided]…
> "program1" ... "program9" would be almost as efficient as a PERFORM.
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-17T00:01:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e750dce.45188041@news.optonline.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net> <16e2f010.0303131043.53a80fde@posting.google.com>`

```
psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

Dynamic call searches first inside the program before going to the disk. 

I earlier wrote:
>COBOL 2002 (and Micro Focus, now) has procedure pointers which allow you do to
>it the c/Pascal way. I dislike this for the same reason I dislike early-bound
>calls -- when anything changes, you must relink the program.

>The COBOL-style alternative is a table of program names. You say: 
> call table-entry (table-ndx)
>  where table-entry looks like 05 filler value 'Save' pic  x(30).
>  Calls are late-bound. 

The faster procedure-pointer (called program-pointer in COBOL 2002) can be bound
statically or dynamically, but static is more practical. Dynamic requires
tediously writing SET statements to load target programs. 

Static:
  05  filler external 'program1' program-pointer.
  05  filler external 'program2' program-pointer.

Dynamic:
  05  program-pointer-n occurs 10 program-pointer.

  perform varying n from 1 by 1 until n > 10
      set program-pointer-n (n) to address of EachProgram (n)
  end-perform

Micro Focus syntax:
  set procedure-pointer-n (n) to entry EachProgram (n)

It is unclear whether either approach searches nested programs before going to
the linker or disk. Nested programs usually do _not_ produce EXTERNs which can
be resolved by a linker. They are handled entirely within the COBOL compiler. My
guess would be EXTERNAL generates references to EXTERNs which will fail. The
dynamic approach would probably work because it shares code already written for
dynamic calls. That's just my speculation, your mileage may vary. 

In the course of researching this answer, I saw errors galore in the 2002
standard. Under SET statement, Format 8, it says you can only set a
program-pointer to another program-pointer. That can't possibly be right.
Section 8.4.11.4.2, discussing address of, says "this identifier format (address
of) shall not be specified as a receiving operand". Yet SET,  Format 7, says you
can SET address of data-name-1 to identifier-7.

Why don't CLC posters jump on the standards committees for publishing ambiguity?


Hint: after going to http://www.techstreet.com/direct/ISO+IEC+CD+1_8-1989.pdf,
save it to your local disk. It will load much faster the next time. 

Robert

>You are quite correct.  That works great.
>
…[7 more quoted lines elided]…
>"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:<b4q2tc$mjg$1@slb4.atl.mindspring.net>...
>> If you WANTED to do this, you could do it already via nested programs and
>> CALL identifier, e.g.
…[16 more quoted lines elided]…
>> "program1" ... "program9" would be almost as efficient as a PERFORM.
```

###### ↳ ↳ ↳ Program-Pointers in 2002 Standard (was: Paragraph Pointers

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-16T19:03:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b536u0$hii$1@slb9.atl.mindspring.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net> <16e2f010.0303131043.53a80fde@posting.google.com> <3e750dce.45188041@news.optonline.net>`

```
Robert's latest error was sent to me via private email - so that I could
correct it for the rest of comp.lang.cobol.

In a recent note, he stated

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e750dce.45188041@news.optonline.net...
> psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:
 <snip>
> In the course of researching this answer, I saw errors galore in the 2002
> standard. Under SET statement, Format 8, it says you can only set a
> program-pointer to another program-pointer. That can't possibly be right.
> Section 8.4.11.4.2, discussing address of, says "this identifier format
(address
> of) shall not be specified as a receiving operand". Yet SET,  Format 7,
says you
> can SET address of data-name-1 to identifier-7.
>
> Why don't CLC posters jump on the standards committees for publishing
ambiguity?
>

Notice that Robert (not the Standard) said,

  "it says you can only set a program-pointer to another program-pointer"

what the 2002 Standard says in SR(20) actually is:

  "Identifier-8 <the sending item in a Format 8 SET statement> shall be of
category program-pointer."

OK, what does the Standard say about *IDENTIFIERS* of "category
program-pointer".  One looks at page 99 where it clearly states,

 "Program-address-identifier creates a unique data item of class pointer and
category program-pointer that contains the address of a program identified
by one of the following: ..."

Therefore, if one actually follows the full Standard, one finds that it is
PERFECTLY valid to code:

   Set receiving-program-pointer to Address of Program "Whatever"

as

   Address of Program "whatever"

fully meets the requirements of being an identifier of category
program-pointer.

I am not positive what he is talking about when he mentions

 "Section 8.4.11.4.2, discussing address of, says "this identifier format
(address of) shall not be specified as a receiving operand".

as there is no section 8.4.11 - however, there is such a rule in section
"8.4.2.12.2" which in SR(4) says,

"4) This identifier format shall not be specified as a receiving operand."

which doesn't cause any real problems - as you may NOT say

  Set Addres of Program "Whatever" to some-program-pointer

and it really wouldn't make any sense to have such an identifier used as a
RECEIVING item - but does make sense to use it as a sending item - which
Format 8 (not 7) of the SET statement allows.

If Robert actually DID have a question/issue with Format 7 (which is for
data-pointers) then it explicitly DOES include support for setting the
ADDRESS OF as the receiving item - but for the address of a data-item, not a
program. My guess is that he simply isn't aware that the 2002 Standard has
two very different features:


Data-address-identifier (defined in 8.4.2.11)
    versus
 Program-address-identifier (defined in 8.4.2.12)

How to use/modify these different types of identiers via the SET statement
corresponds to the difference between Format 7 and Format 8 of the SET
statement.


Bottom-Line:
  The 2002 Standard may (or may not) have "errors galore" (Mr. Wagner's
words) - but the only errors in this post are in his not
reading/understanding what the 2002 Standard *does* clearly state.

Hopefully, this note will clear up any confussion that Mr. Wagner's latest
misrepresentation of a COBOL Standard might have caused.
```

###### ↳ ↳ ↳ Re: Program-Pointers in 2002 Standard (was: Paragraph Pointers

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-17T08:58:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e757ba2.10443901@news.optonline.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net> <16e2f010.0303131043.53a80fde@posting.google.com> <3e750dce.45188041@news.optonline.net> <b536u0$hii$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Robert's latest error was sent to me via private email - so that I could
>correct it for the rest of comp.lang.cobol.
…[45 more quoted lines elided]…
>program-pointer.

Program-address-identifier is not synonymous with program-pointer. It is but one
type of reference returning a program-pointer. 

The standard language is " Identifier-8 shall reference a data item of category
program-pointer. Identifier-9 shall be of category program-pointer." Your
defense of identifier-9 .. a fair one, I admit .. would apply as well to
identifier-8, where it makes no sense in the context of SET. Program-pointers
_can_ be SET. It says so above. 

The standard  language is simply ambiguous, by failing to distinguish between
'category program-pointer' and the value returned by 'address of program'.

>I am not positive what he is talking about when he mentions
>
> "Section 8.4.11.4.2, discussing address of, says "this identifier format
>(address of) shall not be specified as a receiving operand".

I meant to say 8.4.2.11.2.5. Apologies for the sloppy reference. 

>as there is no section 8.4.11 - however, there is such a rule in section
>"8.4.2.12.2" which in SR(4) says,
…[15 more quoted lines elided]…
>two very different features:

Yes, I was referring to data pointers. 8.4.2.11.2.5 seems to say a data (not
program) pointer may not be SET. 

"5) This identifier format shall not be specified as a receiving operand."

What it really means is you can say

set data-pointer to (whatever)

You cannot say

set address of data-item to (whatever)

In other words, the pointer can be changed but the 'address of' is immutable. I
understand the reasoning behind that. 

This is a significant change from current IBM/Micro Focus/Fujitsu semantics,
where you _can_ say 'set address of data-item to (whatever)'. The 2002 standard
wants us to use BASED in place of the de facto standard 'set address of'.

I don't like the change because it has its roots in the C language, where &
means 'address of' and * means 'dereferenced by this pointer'. Neophytes have a
hard time distinguishing between the two. If we're to be more readable than C,
we shouldn't adopt C semantics when there is a more easily understood de facto
standard already in place. 

Robert
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-16T19:35:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303161935.7d043d20@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q2tc$mjg$1@slb4.atl.mindspring.net> <16e2f010.0303131043.53a80fde@posting.google.com> <3e750dce.45188041@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e750dce.45188041@news.optonline.net>...
> 
> In the course of researching this answer, I saw errors galore in the 2002
…[12 more quoted lines elided]…
> Robert
 

Robert - let's be fair:

You saw what YOU think are errors and contradictions not in the COBOL
2002 standard, but in Committee DRAFT 1.8.
```

#### ↳ Re: Paragraph Pointers

- **From:** docdwarf@panix.com
- **Date:** 2003-03-13T09:52:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4q5vd$nbr$1@panix1.panix.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
In article <16e2f010.0303121947.6c4e0870@posting.google.com>,
Joe Zitzelberger <psychedelic-harry@mindless.com> wrote:

[snip]

>But it got me thinking -- what I wanted was a PARAGRAPH-POINTER.
>
…[23 more quoted lines elided]…
>this useful?

Hmmmmmm... it seems perilously close to self-modifying code, something 
that many ASM jockies used as a way of saying 'Look, Ma, I'm a 
Programmer!'.  Consider the following nightmare when styles get mixed:

01  WS-PARA-NAMES.
    05  WS-PARA-NAME-TBL.
        10  FILLER PIC X(21) VALUE 'MASTER-FILE-READ     '.
        10  FILLER PIC X(21) VALUE 'DIVISION-FILE-READ   '.
        10  FILLER PIC X(21) VALUE 'INV-FILE-READ        '.
        10  FILLER PIC X(21) VALUE 'STORE01-FILE-READ    '.
        10  FILLER PIC X(21) VALUE 'STORE02-FILE-READ    '.
        10  FILLER PIC X(21) VALUE 'STORE03-FILE-READ    '.
...
        10  FILLER PIC X(21) VALUE 'STORE99-FILE-READ    '.        
    05  PARA-DESIRED REDEFINES WS-PARA-NAME-TBL OCCURS MAX-STORES TIMES  
                                                PIC X(21).

...
    IF LINK-FUNC = 'UPDATE INVENTORY QUANTITY'
        PERFORM VARYING SUB1 FROM 1 BY 1 UNTIL SUB1 > MAX-STORES
            PERFORM PARA-DESIRED(SUB1)
        END-PERFORM
        PERFORM UPDATE-INV-QTY-RTN  THRU  UIVQ-EX
        IF EASTERN-DIVISION-SPECIAL-OFFER
            INSPECT WS-PARA-NAMES REPLACING ALL 'FILE-READ '
                                             BY 'FILE-UPDT '
            PERFORM VARYING SUB1 FROM (LINK-STORE-RANGE-START + 3)
             BY 1 UNTIL SUB1 > (LINK-STORE-RANGE-END + 3)
                PERFORM PARA-DESIRED(SUB1)
            END-PERFORM
        END-IF
    END-IF.

(on the other hand... these 'dynamic' paragraph names could cut down on 
those pesky GO TO... DEPENDING ONs)

DD
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-13T10:49:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303131049.2c590839@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q5vd$nbr$1@panix1.panix.com>`

```
There is nothing tricky about a jump table.  It's just smaller than an
Evaluate by a factor of 2...

If modeled after the Procedure-pointer, where
the module entry address is the actual pointer value, the
INSPECT/REPLACING would not be a possibility.


docdwarf@panix.com wrote in message news:<b4q5vd$nbr$1@panix1.panix.com>...
> Hmmmmmm... it seems perilously close to self-modifying code, something 
> that many ASM jockies used as a way of saying 'Look, Ma, I'm a 
…[34 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

- **From:** docdwarf@panix.com
- **Date:** 2003-03-13T14:27:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4qm28$rrd$1@panix1.panix.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q5vd$nbr$1@panix1.panix.com> <16e2f010.0303131049.2c590839@posting.google.com>`

```
In article <16e2f010.0303131049.2c590839@posting.google.com>,
Joe Zitzelberger <psychedelic-harry@mindless.com> wrote:
>There is nothing tricky about a jump table.  It's just smaller than an
>Evaluate by a factor of 2...

There's nothing tricky about a GO TO... DEPENDING ON, either... and yet 
they are avoided like the plague, and rightly so.

>
>If modeled after the Procedure-pointer, where
>the module entry address is the actual pointer value, the
>INSPECT/REPLACING would not be a possibility.

That was not what I saw coded in your posting... did I miss something?

DD
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

_(reply depth: 4)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-13T13:44:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303131344.21fce974@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4q5vd$nbr$1@panix1.panix.com> <16e2f010.0303131049.2c590839@posting.google.com> <b4qm28$rrd$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<b4qm28$rrd$1@panix1.panix.com>...
> In article <16e2f010.0303131049.2c590839@posting.google.com>,
> Joe Zitzelberger <psychedelic-harry@mindless.com> wrote:
…[10 more quoted lines elided]…
> That was not what I saw coded in your posting... did I miss something?

If you had the address of a paragraph entry point you could not very
well "INSPECT array-of-entry-points REPLACING 'READ' by 'UPDT'"
because READ would not exist in the pointer.
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-03-13T21:29:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4repo$bhq$1@panix1.panix.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <16e2f010.0303131049.2c590839@posting.google.com> <b4qm28$rrd$1@panix1.panix.com> <16e2f010.0303131344.21fce974@posting.google.com>`

```
In article <16e2f010.0303131344.21fce974@posting.google.com>,
Joe Zitzelberger <psychedelic-harry@mindless.com> wrote:
>docdwarf@panix.com wrote in message news:<b4qm28$rrd$1@panix1.panix.com>...

[snip]

>> That was not what I saw coded in your posting... did I miss something?
>
>If you had the address of a paragraph entry point you could not very
>well "INSPECT array-of-entry-points REPLACING 'READ' by 'UPDT'"
>because READ would not exist in the pointer.

Ahhhhh, now I see... my error and apologies, I misunderstood the 
reference and thought that older COBOL techniques were being used, similar 
to dynamic vs. static CALLs.

DD
```

#### ↳ Re: Paragraph Pointers

- **From:** jeff.lanam-nospam-@compaq-dot-com.not (Jeff Lanam)
- **Date:** 2003-03-13T18:33:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e70ce5f.780615315@news.cpqcorp.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
On 12 Mar 2003 19:47:10 -0800, the evil clone of
psychedelic-harry@mindless.com (Joe Zitzelberger) emitted:

>I was quite glad to see ALTER removed for 2002.  As a statement, it had one
>huge, glaring, fatal, problem -- the failure to return to whence it was
…[31 more quoted lines elided]…
>possible.

Seems like it would be cleaner to have a PERFORM DEPENDING ON
variant.  I don't much like the idea of having pointers to
procedures.  From an implementation standpoint, code generators
like to know where a branch will go to.  It's easier to
implement when the possible destinations are spelled out.


Jeff Lanam  jeff.lanam at hp.com
COBOL for HP NonStop Systems
Hewlett-Packard
```

#### ↳ Re: Paragraph Pointers

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-13T23:42:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e710d5c.310700774@news.optonline.net>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

> I got to thinking about it when writing some code like below:
>
…[26 more quoted lines elided]…
>possible.

COBOL 2002 (and Micro Focus, now) has procedure pointers which allow you do to
it the c/Pascal way. I dislike this for the same reason I dislike early-bound
calls -- when anything changes, you must relink the program.

The COBOL-style alternative is a table of program names. You say: 
  call table-entry (table-ndx)
  where table-entry looks like 05 filler value 'Save' pic  x(30).
  Calls are late-bound. 
This has the additional advantage of permitting the user to extend your text
editor with compiled 'macros', and then binding a key to the macro without the
need to relink. The text editor I wrote and use works exactly this way. For
example, my spelling checker is such a macro. 

>But it got me thinking -- what I wanted was a PARAGRAPH-POINTER.

You got it. But they don't point to paragraphs, they point to callable programs.

I used to call these functions until CLC posters make a big stink about the
(alleged) distinction between functions and programs. I still don't see the
difference, but stopped using the word function. <shrug>

Personally, I think out-of-line PERFORM is an anachronism. Every performed
paragraph can, and should IMO, be turned into an embedded program, which I used
to call 'local function'. The advantage is local variables and limited
visibility to the 'ocean of data' in working-storage, plus the opportunity to
pass parameters. 

Someone said I think like a C programmer. Generally, I'd take that as an insult,
but in this case I think the C & many other languages got it right and COBOL's
PERFORM got it wrong. 

Robert
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-03-13T19:02:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IW8ca.1036$wg5.218798@news20.bellglobal.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <3e710d5c.310700774@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e710d5c.310700774@news.optonline.net...
<snip>
> Personally, I think out-of-line PERFORM is an anachronism. Every performed
> paragraph can, and should IMO, be turned into an embedded program, which I
used
> to call 'local function'. The advantage is local variables and limited
> visibility to the 'ocean of data' in working-storage, plus the opportunity
to
> pass parameters.

That's roughly what you get with OO COBOL: a ton of little callable programs
(called methods), embedded in a larger piece of source (call class).  Each
has its own local-storage and linkage sections.

> Someone said I think like a C programmer. Generally, I'd take that as an
insult,
> but in this case I think the C & many other languages got it right and
COBOL's
> PERFORM got it wrong.

You must be thinking like a COBOL porgrammer after all <G>

Calin, TORONTO
```

#### ↳ Re: Paragraph Pointers

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-13T18:19:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EIqcnd8w_MclveyjXTWckQ@giganews.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```

"Joe Zitzelberger" <psychedelic-harry@mindless.com> wrote in message
news:16e2f010.0303121947.6c4e0870@posting.google.com...
> I was quite glad to see ALTER removed for 2002.  As a statement, it had
one
> huge, glaring, fatal, problem -- the failure to return to whence it was
> called.
>
[...]

> So what would CLC think of this idea?  Am I the only person that would
find
> this useful?

Like Bertrand Russell finding the first paradox in set theory by the asking
of a single question, you have single-handedly set back the next release of
COBOL standards by at least five years, maybe forever. Committees will be
formed, debates held, communications circulated, proposals floated, comments
solicited. And that's just for round one.

Notaries public will become overworked. Paper by the ton (or bandwidth by
the bushel) will be consumed. I wouldn't be surprised if the UN got
involved.

Best to forget the whole idea.
```

#### ↳ Re: Paragraph Pointers

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-14T20:29:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4qion$vgi$1@aklobs.kc.net.nz>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
Joe Zitzelberger wrote:

>   Perform varying table-ndx from 1 by 1
>     until table-ndx > size-of-table
…[24 more quoted lines elided]…
> possible.

I can't think why it would be written this way at all, apart from seeming 
'inverted' it relies on 'size-of-table' being the same for every table, or 
already being set by a previous evaluate.

It seems that you want to save the source code size of the perform varying 
statement at the run-time expense of the evaluate.

Surely it would be preferable to have the perform varying inside the whens, 
or inside the process-type-nnn paragraph, at a vast imnprovement of speed, 
and then the table size can be specified correctly at those points instead 
of having to be set previously by a different mechanism.
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-13T13:41:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303131341.1c033114@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4qion$vgi$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<b4qion$vgi$1@aklobs.kc.net.nz>...
> Joe Zitzelberger wrote:
> 
…[38 more quoted lines elided]…
> of having to be set previously by a different mechanism.


That was an unfortunate choice of generic names.  I suppose I did it
to myself by changing all instances of 'array' and 'buffer' to
'table'.   That converted both array-ndx and buffer-ndx into
table-ndx.

The idea I was trying to convey was processing a file with a large
number of record types that need type-specific processing.  Or a
stream of bytes, each requiring byte-specific processing (shown in
example).
```

#### ↳ Re: Paragraph Pointers

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2003-03-14T18:29:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4ts4d$kp9$1@ngspool-d02.news.aol.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com>`

```
Wouldn't "go to depending on" do pretty much the same thing?

Perform proc-cntl thru proc-exit
 varying sub from 1 by 1
 until sub > sub-max.

....

proc-cntl.
     go to process-type-1
           process-type-2
           process-type-3
           ...
     depending on sub.
proc-exit.
  exit.

process-type-1.
    do stuff.
    go to proc-exit.

 ....

I know. I know. I'm gonna get all kinds of flak for the
out of line "go to". But it works and compiles and isn't
nearly as complicated as "paragraph-pointer".
Gee "Perform depending on" might be a nice idea and avoid
the go to's.


    --------------------------------------------

"Joe Zitzelberger" <psychedelic-harry@mindless.com> wrote in message
news:16e2f010.0303121947.6c4e0870@posting.google.com...
> I was quite glad to see ALTER removed for 2002.  As a statement, it had one
> huge, glaring, fatal, problem -- the failure to return to whence it was
…[67 more quoted lines elided]…
> Joe Zitzelberger
```

##### ↳ ↳ Re: Paragraph Pointers

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-03-15T16:30:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NyIca.415$we1.340867@newssrv26.news.prodigy.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4ts4d$kp9$1@ngspool-d02.news.aol.com>`

```


"Ron" <NoSoy@swbell.net> wrote in message
news:b4ts4d$kp9$1@ngspool-d02.news.aol.com...
> Wouldn't "go to depending on" do pretty much the same thing?
> ...
> I know. I know. I'm gonna get all kinds of flak for the
> out of line "go to".

Not if you make each of the GOTO'd paragraphs themselves GOTO a common
point...

    PERFORM GOTO-DEPENDING THRU GOTO-DEPENDING-EXIT
      .....

GOTO-DEPENDING.
    GOTO  proc-1 proc-2 proc-3.... DEPENDING ON X
RETURN-HERE.
   CONTINUE.
GOTO-DEPENDING-EXIT.
       EXIT.
PROC-1.
  yadda yadda
  GOTO RETURN-HERE.
PROC-2
  yadda yadda
  GOTO RETURN-HERE.
...

(Sure, I have an extra 'layer' in there, but I can understand it better this
way).

MCM
```

###### ↳ ↳ ↳ Re: Paragraph Pointers

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-17T10:26:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303171026.197c961@posting.google.com>`
- **References:** `<16e2f010.0303121947.6c4e0870@posting.google.com> <b4ts4d$kp9$1@ngspool-d02.news.aol.com> <NyIca.415$we1.340867@newssrv26.news.prodigy.com>`

```
I'll fall back to my initial statement that the problem with the two
obsolete gotos is that neither returns to their caller.  Yes, this
structure would work, and be logically identical to the n-way
evaluate, but I would always choose the n-way evaluate over the
goto/depend or alter/goto.

Nested program name provides the necessary early-binding and reduced
lines of code.  Neither of the gotos offer this and add the necessity
of extra goto-common-exit over the verbose-but-simple evaluate.

"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<NyIca.415$we1.340867@newssrv26.news.prodigy.com>...
> "Ron" <NoSoy@swbell.net> wrote in message
> news:b4ts4d$kp9$1@ngspool-d02.news.aol.com...
…[28 more quoted lines elided]…
> MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
