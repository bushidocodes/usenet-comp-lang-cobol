[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol - Data Exception (Conversion Data).

_48 messages · 17 participants · 2000-03 → 2000-04_

---

### Cobol - Data Exception (Conversion Data).

- **From:** "Gianluigi Angotti" <giangol@tin.it>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bng6o$11p$1@news.flashnet.it>`

```
Visual Age for Cobol Windows NT.
When assign a not numeric data in a COMP-3 variable, this don't  cause a run
time error (the same in debug)

        01    AREA-DATI.
        03     DATO-NUM                PIC S9(5)  COMP-3.
     ....
     MOVE 'AAAAAAAAA'       TO AREA-DATI.
     IF DATO-NUM  > 0
        DISPLAY '*** DATO MAGGIORE DI ZERO'
     END-IF.

This istruction give a "0C7"  (data exception) in a MVS system.
You know a method to intercept this error in a NT system ???
Thank's
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<##RuGHFm$GA.295@cpmsnbbsa04>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
The problem may be related to the character sets:

ASCII - on PC
EBCDIC  - on the mainframe

The character A is x'41' on the PC, and x'C1' on the mainframe.

PC DATO-NUM = x'414141' all non-sign are digits.
MF DATO-NUM = x'C1C1C1' all non-sign are not digits.

You should be able to test for DATO-NUM NOT NUMERIC on both platforms.

Good luck!!

Gianluigi Angotti <giangol@tin.it> wrote in message
news:8bng6o$11p$1@news.flashnet.it...
> Visual Age for Cobol Windows NT.
> When assign a not numeric data in a COMP-3 variable, this don't
cause a run
> time error (the same in debug)
>
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DF541C.302F28BD@zip.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
Gianluigi Angotti wrote:
> 
> Visual Age for Cobol Windows NT.
…[13 more quoted lines elided]…
> Thank's

Should I answer the obvious:

      IF DAT0-NUM NUMERIC OR DATO-NUM  > 0
         DISPLAY '*** DATO MAGGIORE DI ZERO'
      ELSE
	 DISPLAY 'Your program failed fix it'
      END-IF.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38dfdd01@news.iprimus.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <38DF541C.302F28BD@zip.com.au>`

```
A small clarification here too


The code snippet you supply ie...

      IF DAT0-NUM NUMERIC OR DATO-NUM  > 0
         DISPLAY '*** DATO MAGGIORE DI ZERO'
      ELSE
DISPLAY 'Your program failed fix it'
      END-IF.

won't necessarily work. it should really be

IF   AREA-DATI NUMERIC

Also be careful when checking numbers. In NT, numbers come before
alphanumerics. In the MVS system the reverse is true

Regards

Theo


Ken Foskey <waratah@zip.com.au> wrote in message
news:38DF541C.302F28BD@zip.com.au...
> Gianluigi Angotti wrote:
> >
> > Visual Age for Cobol Windows NT.
> > When assign a not numeric data in a COMP-3 variable, this don't  cause a
run
> > time error (the same in debug)
> >
…[22 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E0A616.97FE92F9@zip.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <38DF541C.302F28BD@zip.com.au> <38dfdd01@news.iprimus.com.au>`

```
Westley Lodge Pty Ltd wrote:
> 
> A small clarification here too
…[15 more quoted lines elided]…
> 
...snip...

> > >
> > >         01    AREA-DATI.
> > >         03     DATO-NUM                PIC S9(5)  COMP-3.
...snip...

Theo,

By checking AREA-DATI you are checking for the presence of character
digits, AREA-DATI is considered alphabetic.  By checking DAT0-NUM you
are checking for packed digits and a sign.

If we move '000' to area-dati (character zeros) I believe yours may
provide incorrect results.  Let me know what your compiler does, I
would be interested to know.

By the way numeric checks can be applied on any field.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** Ron <NoSoy@swbell.net>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DF73B5.872DAE3B@swbell.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
IF DATO-NUM NOT NUMERIC
   .....
END-IF.

============================================================

Gianluigi Angotti wrote:
> 
> Visual Age for Cobol Windows NT.
…[13 more quoted lines elided]…
> Thank's
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lHKD4.9069$0o4.66330@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
In article <8bng6o$11p$1@news.flashnet.it>,
Gianluigi Angotti <giangol@tin.it> wrote:
>Visual Age for Cobol Windows NT.
>When assign a not numeric data in a COMP-3 variable, this don't  cause a run
…[12 more quoted lines elided]…
>Thank's

You assigned a non-numeric value to AREA-DATI; this is a group item, and,
by definition, alphanumeric.  On the MVS system you could check:

IF DATO-NUM NOT NUMERIC

... for COMP-3 variables but I recall that this implementation is
IBM-specific.  A check which would work across all platforms I know of is:

05  AREA-TEST     PIC X(5).
05  AREA-TEST-NUM REDEFINES AREA-TEST PIC 9(5).

...

MOVE DATO-NUM TO AREA-TEST-NUM.
IF AREA-TEST NOT NUMERIC
    DISPLAY 'TUTTI DI FROMAGGIO!'.

DD
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38dfd99b@news.iprimus.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net>`

```
Just a small clarification...

Unfortunately, I believe this is wrong, as the "IS NUMERIC" clause could
only be applied to alphanumeric fields, therefore...

IF DATO-NUM NOT NUMERIC

should realy be


IF AREA-DATI NOT NUMERIC

Regards

Theo


<docdwarf@clark.net> wrote in message
news:lHKD4.9069$0o4.66330@iad-read.news.verio.net...
> In article <8bng6o$11p$1@news.flashnet.it>,
> Gianluigi Angotti <giangol@tin.it> wrote:
> >Visual Age for Cobol Windows NT.
> >When assign a not numeric data in a COMP-3 variable, this don't  cause a
run
> >time error (the same in debug)
> >
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ky2E4.9381$0o4.73075@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <38dfd99b@news.iprimus.com.au>`

```
In article <38dfd99b@news.iprimus.com.au>,
Westley Lodge Pty Ltd <wlodge@hotkey.net.au> wrote:
>Just a small clarification...
>
>Unfortunately, I believe this is wrong, as the "IS NUMERIC" clause could
>only be applied to alphanumeric fields,

With all due respect, see:

<http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYLR105/6%2e1%2e6%2e2?SHELF=IGYMS005>

... which, among other things, states:

--begin quoted text:

NUMERIC 
Identifier consists entirely of the characters 0 through 9, with or
without an operational sign. 


If its PICTURE does not contain an operational sign, the identifier being
tested is determined to be numeric only if the contents are numeric and an
operational sign is not present. 


If its PICTURE does contain an operational sign, the identifier being
tested is determined to be numeric only if the item is an elementary item,
the contents are numeric, and a valid operational sign is present. 


The NUMERIC test cannot be used with an identifier described as alphabetic
or as a group item that contains one or more signed elementary items. 


For numeric data items, the identifier being tested can be described 
X as USAGE DISPLAY or (as IBM extensions) USAGE COMPUTATIONAL-3, or 
X USAGE PACKED-DECIMAL. 

--end quoted text

>therefore...
>
…[5 more quoted lines elided]…
>IF AREA-DATI NOT NUMERIC

I agree with the practise but according to the above-quoted COMP-3 can be
tested with IF NUMERIC as well; alphanumeric fields can be tested only for
characters 0 thru 9.

DD

>
><docdwarf@clark.net> wrote in message
…[39 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c65ph$id4$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net>`

```
Sorry, but I couldn't let this go...

docdwarf@clark.net wrote in message ...
>In article <8bng6o$11p$1@news.flashnet.it>,
>Gianluigi Angotti <giangol@tin.it> wrote:


>...A check which would work across all platforms I know of is:
>
…[9 more quoted lines elided]…
>DD
This almost certainly WON'T work across all platforms. (I'd be surprised if
it worked on ANY platform, and it is certainly NOT a solution to the
underlying problem).

It is predicated on the (I believe false) hope that moving an invalid packed
field to a non-packed target will NOT cause a data exception. In other
words, an 0C7 can only be raised during a PACK operation. (Maybe someone in
the NG who has access to a mainframe can confirm or deny whether this is the
current situation...?)

It is now some years since I worked with mainframes, but I seem to recall
that the UNPACK macro could also raise this exception due to an invalid sign
being detected. Even if I'm wrong, and the above works OK, it is a very
dodgy "solution".

The best solution to this problem is NOT to move data to the group level
above DATO-NUM.
(Use INITIALIZE or simply move zero to DATO-NUM when you start whatever
processing cycle it is used in, if it needs to be initialized).

Do you really need to use a PACKED field at all? This format is rooted in
the days when external media cost a fortune and it was necessary to
"compress" everything possible.

(In fact, the original IBM 360s had the decimal instruction set (support for
PACKED) as an option. The idea was that if you were going to use this
beautiful new technology (in 1965) for commercial data processing, you'd
probably need to process money and therefore require a decimal arithmetic
capability that was simpler and took up less space than the native floating
point provided. Later, after finding how surprisingly good for commercial
applications the 360 range was, IBM made the decimal instruction set a
standard part of the system.)

There is a real question as to whether we need this format in today's
processing. There probably isn't an IBM programmer alive who has never had
an 0C7 caused by "packing a blank" or some other invalid character. Yes, you
can argue that if you are processing invalid data, it is better NOT to
continue (that was IBM's philosophy) but other vendors who never implemented
PACKED and the associated data exception, still made a living...

I also question the point of style where a NUMERIC (Class) test is applied
to a field defined as Packed. Although some vendors allow it, Class tests
should only be applied to fields which COULD be something other than they
are defined as. Asking whether a field defined as Pic xxxx is NUMERIC  or
ALPHABETIC makes sense because it could be either. Asking whether a field
defined as numeric is numeric is nonsense. It implies the programmer doesn't
know what is going on with the data in his program. The corollary from this
is that raw data should always be read as Pic x (string) data, then
validated and moved to numeric fields once we are sure that it is numeric.

Pete.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E6EE78.FE1C148E@zip.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz>`

```
"Peter E. C. Dashwood" wrote:
> 
> It is predicated on the (I believe false) hope that moving an invalid
…[3 more quoted lines elided]…
> deny whether this is the current situation...?)

Your back Pete.

The answer is as stated.  The compiler will mostly simply move the
bytes around and therefore not crash.  This does depend upon your
compiler options though.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c8mo4$mic$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <38E6EE78.FE1C148E@zip.com.au>`

```
Thanks Ken, for setting that straight.

I could've sworn that using UNPACK did it too, but I am struggling to recall
Assembler programming in 1968 <grin>.

OK, I was wrong on that one, but I stand by the rest of what I said. It is
an ugly solution that is being proposed....

While we're on it, I can't see the post that Bill Klein did to this thread
where he commented on what I wrote. But I DID receive his post by
mail...weird things going on with my ISP...

Bill, I agree that there are existing extensions to allow Class tests
(NUMERIC and
ALPHABETIC) to be applied to numeric data fields. I just don't condone it. I
really can't see the point. To me it seems logically idiotic to ask whether
a numeric field is numeric. If there was any chance of it NOT being, why
define it as numeric? Yes, I know accidents happen and we clobber fields
inadvertently, but the solution has to be NOT to set things up so that can
happen, rather than closing the door after the horse has gone.

I believe these "extensions", which Bill advises are about to become
standard, just encourage sloppy programming and are being implemented
because people don't understand the proper use of Class tests.

In the early days of COBOL (COBOL 59), BEFORE the PICTURE clause was
invented, fields were described using 3 clauses: SIZE, CLASS, and USAGE.

So a field which today we would describe as "pic x(10)." needed "SIZE 10,
CLASS ALPHANUMERIC, USAGE DISPLAY".

Obviously, this was a bit tiresome, even for COBOL programmers, so PICTURE
was a blessing. But we all understood what CLASS meant. It meant there were
three possibilities: NUMERIC, ALPHABETIC, and ALPHANUMERIC. A field defined
as pic X(10) could hold anything and there were times when it would be
advantageous to know what the CLASS of the data in it was...

Enough said.

Pete.

Ken Foskey wrote in message <38E6EE78.FE1C148E@zip.com.au>...
>"Peter E. C. Dashwood" wrote:
>>
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E888A2.E333FE89@zip.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <38E6EE78.FE1C148E@zip.com.au> <8c8mo4$mic$1@hermes.enternet.co.nz>`

```
"Peter E. C. Dashwood" wrote:
> 
> I could've sworn that using UNPACK did it too, but I am struggling to
> recall Assembler programming in 1968 <grin>.
> 

Rewind.

If you move a packed field to a packed field of the same definition
the compiler will make this a simple byte move*.  If you pack or
unpack (move to or from a display type number) then you had better
have your numbers right.

Sorry for the confusion.

*  Depending upon compiler options, it seems to work this way
optimized and crash in no optimization but do not quote me on this.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 6)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53nhes0u02d35fgf94q53mdfgf5tv7g41v@4ax.com>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <38E6EE78.FE1C148E@zip.com.au> <8c8mo4$mic$1@hermes.enternet.co.nz> <38E888A2.E333FE89@zip.com.au>`

```
On Mon, 03 Apr 2000 22:03:46 +1000 Ken Foskey <waratah@zip.com.au> wrote:

:>"Peter E. C. Dashwood" wrote:
 
:>> I could've sworn that using UNPACK did it too, but I am struggling to
:>> recall Assembler programming in 1968 <grin>.

:>Rewind.

:>If you move a packed field to a packed field of the same definition
:>the compiler will make this a simple byte move*.  If you pack or
:>unpack (move to or from a display type number) then you had better
:>have your numbers right.

Actually PACK and UNPACK will not fail because the data isn't decimal.

PACK combines the low nibbles of two adjacent bytes into one byte, and flips
the nibbles of the last byte.

UNPK splits a byte into two nibbles, place x'f' in the high nibbles, and flips
the nibbles of the last byte.

The packed arithmetic instructions such as AP, SP, CVB, etc. will fail if the
data is not packed with the last nibble being a sign.

:>Sorry for the confusion.

:>*  Depending upon compiler options, it seems to work this way
:>optimized and crash in no optimization but do not quote me on this.

I would expect if the packed fields are identical lengths it would generate
MVC, if unequal length it would generate ZAP.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cegfb$8u$2@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <38E6EE78.FE1C148E@zip.com.au> <8c8mo4$mic$1@hermes.enternet.co.nz> <38E888A2.E333FE89@zip.com.au> <53nhes0u02d35fgf94q53mdfgf5tv7g41v@4ax.com>`

```
Thanks Ben,

your elucidation was faultless and brought back some distant memories...of
course, it isn't the macro instructions which fail it is the decimal
instruction set; I seem to recall CVB being a persistent offender...

So what about this move in COBOL? Invalid data in a packed field, moving it
to  a display numeric field. Are you saying that the UNPACK causes no
problem, and the subsequent filling of the target will be achieved by MVC or
ZAP? Sounds reasonable and it looks as though I was wrong about the move
causing an 0c7 (but I already knew that from Ken...)

I still think the whole approach is decidedly dodgy.

These days PACKED fields are best avoided.

Pete.


>
>I would expect if the packed fields are identical lengths it would generate
…[7 more quoted lines elided]…
>Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H2IG4.16323$0o4.107222@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <38E888A2.E333FE89@zip.com.au> <53nhes0u02d35fgf94q53mdfgf5tv7g41v@4ax.com> <8cegfb$8u$2@hermes.enternet.co.nz>`

```
In article <8cegfb$8u$2@hermes.enternet.co.nz>,
Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:

[snippage]

>So what about this move in COBOL? Invalid data in a packed field, moving it
>to  a display numeric field. Are you saying that the UNPACK causes no
>problem, and the subsequent filling of the target will be achieved by MVC or
>ZAP?

Mr Dashwood, I posted both the code and the PMAP on this yesterday... if
you want I'll email it to you.

>Sounds reasonable and it looks as though I was wrong about the move
>causing an 0c7 (but I already knew that from Ken...)
>
>I still think the whole approach is decidedly dodgy.

Dealing with bunged-up data can get that way, aye.

>
>These days PACKED fields are best avoided.

They are, Mr Dashwood, a fairly large part of the Legacy.

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ci6o9$6gt$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <38E888A2.E333FE89@zip.com.au> <53nhes0u02d35fgf94q53mdfgf5tv7g41v@4ax.com> <8cegfb$8u$2@hermes.enternet.co.nz> <H2IG4.16323$0o4.107222@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message ...
>In article <8cegfb$8u$2@hermes.enternet.co.nz>,
>Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
…[5 more quoted lines elided]…
>
Thank you very much, you are a very helpful little dwarf and I'll mention it
it Snow White next time I meet her at Granma's house ....(oops, sorry, wrong
fairy story...)

I do not get to see EVERY post to this NG and sometimes the ones I do see
are out of date so forgive me if I appear to have overlooked your post. I
would appreciate seeing the PMAP. Could you send it to
pete_dashwood@compuserve.com NOT the address above?

Thanks.

PS I haven't been called "Sir" or "Mister" since being in the services 25
years ago. If you persist in this I shall get Grumpy to beat you up...

Pete.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 10)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uU3H4.16434$0o4.108177@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cegfb$8u$2@hermes.enternet.co.nz> <H2IG4.16323$0o4.107222@iad-read.news.verio.net> <8ci6o9$6gt$1@hermes.enternet.co.nz>`

```
In article <8ci6o9$6gt$1@hermes.enternet.co.nz>,
Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>docdwarf@clark.net wrote in message ...
…[10 more quoted lines elided]…
>fairy story...)

Wrong person, as well; I am *not* a part of that 'Snow White' crowd.

>
>I do not get to see EVERY post to this NG and sometimes the ones I do see
>are out of date so forgive me if I appear to have overlooked your post. I
>would appreciate seeing the PMAP. Could you send it to
>pete_dashwood@compuserve.com NOT the address above?

No prob.

>
>Thanks.
>
>PS I haven't been called "Sir" or "Mister" since being in the services 25
>years ago. If you persist in this I shall get Grumpy to beat you up...

That might not be a Wise Thing, Mr Dashwood... someone might get hurt.  I
abide by the Three Rules of Public Group Discourse I was taught, away back
in my Kollidje Daze:

1) One person speaks at a time.

2) Any opinion, unless it is supported by Reasoned Argument, can be
dismissed as 'mere' opinion.

3) *Everyone* is referred to as Mr or Ms at all times.

... as for 'Sir', I try to avoid that... I was a Sergeant and *my* parents
were married.

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 11)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ECD2EA.51A37BCB@cusys.edu>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cegfb$8u$2@hermes.enternet.co.nz> <H2IG4.16323$0o4.107222@iad-read.news.verio.net> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net>`

```


docdwarf@clark.net wrote:
> 
> In article <8ci6o9$6gt$1@hermes.enternet.co.nz>,
…[15 more quoted lines elided]…
> Wrong person, as well; I am *not* a part of that 'Snow White' crowd.

Which one?  Tanith Lee wrote the short story "Red as Blood", which is
the Snow White story with a twist.  The victor always writes the
history, and in this case the Queen won.  Here's what we know about Snow
White:

Her skin as white as snow.
Her lips as red as blood.
When a woodsman under direct orders from his Queen tries to kill her,
she looked at him and charmed him to kill a stag instead.
She went off into the woods to live with a bunch of misshapen servants.
Animals follow her bidding, and possibly even storms.
She appeared to be dead in her coffin, but was revived by the kiss of
life.

It is easy to see what crowd 'Snow White' belongs to.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 12)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N05H4.16443$0o4.108437@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net> <38ECD2EA.51A37BCB@cusys.edu>`

```
In article <38ECD2EA.51A37BCB@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, post, them!!> wrote:
>
>
…[20 more quoted lines elided]…
>Which one?

None  of 'em.

> Tanith Lee 

Ha!  *There* you have your Nefarious Connection!  *Anyone* knows that the
Mummy retains his Mystiwockial Immortality *only* by drinking a brew of
tanith lees; *that* source is obviously connected to foul, unnatural, evil
forces, seeking to stain, rend asunder and destroy...

... what's that?  The Mummy drank a tea of 'tanna leaves', not 'tanith
lees'?

Oh.  As you were.

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ED58CB.CF2F14F8@home.com>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cegfb$8u$2@hermes.enternet.co.nz> <H2IG4.16323$0o4.107222@iad-read.news.verio.net> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net>`

```


docdwarf@clark.net wrote:
> 
> That might not be a Wise Thing, Mr Dashwood... someone might get hurt.  I
…[12 more quoted lines elided]…
> 

Well I always used # 3 politely - but mentally always spelled it 'cur' 
- they were happy/I was happy :-)

Jimmy
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 11)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl51o$gtv$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cegfb$8u$2@hermes.enternet.co.nz> <H2IG4.16323$0o4.107222@iad-read.news.verio.net> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net>`

```

docdwarf@clark.net wrote in message ...
>In article <8ci6o9$6gt$1@hermes.enternet.co.nz>,
>Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
…[3 more quoted lines elided]…
>>>Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:

>
>Wrong person, as well; I am *not* a part of that 'Snow White' crowd.
>
Thats not what she says...I told her you were sending me a PMAP and she
burst into tears and ran off muttering something about never trusting a
doctor again and  the only one who could be spared from work in the mines to
help her out after the baby arrives, will be Dopey and he's incoherent. The
poor girl was very upset... Oh Sure, Doc's the friendly looking bespectacled
one, who now denies all knowledge...("Trust me, I'm a Doctor..." "Take your
clothes off...")


>>
>>PS I haven't been called "Sir" or "Mister" since being in the services 25
…[4 more quoted lines elided]…
>in my Kollidje Daze:


Grumpy is not intimidated. He put the "Bash" in Bashful...  Besides, he owes
me a favour, if it wasn't for the magic musrooms I gave him he would've
caught what Sneezy's got...

Well Mr. Dwarf I don't know what Kollidje you went to, but the 3 rules at
mine were:

1. The one who yells the loudest is the rightest.
2. Anyone physically smaller than you is wrong.
3. Anyone who presents a better argument than yours gets a smack in the
mouth.

>... as for 'Sir', I try to avoid that... I was a Sergeant and *my* parents
>were married.
>
A Sergeant whose parents were married?  What States allow marriage with
retarded chimps? (That's what it takes to produce a Sergeant...) Now THAT is
a fairy story...

Pete.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 12)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmFI4.16697$0o4.112628@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net> <8cl51o$gtv$1@hermes.enternet.co.nz>`

```
In article <8cl51o$gtv$1@hermes.enternet.co.nz>,
Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>docdwarf@clark.net wrote in message ...
…[16 more quoted lines elided]…
>clothes off...")

... and at this hour of the morning, too... well, what else is there...

>
>
…[19 more quoted lines elided]…
>mouth.

... and it shows, Mr Dashwood, it most certainly shows.  As a professor of
philosophy once taught me, years ago, when explaining Hobbes' statement
about 'the differences between men are so small as to be inconsequential'
(or something like that): 'Now, imagine you have a siege-howitzer, ready
to blow anyone who approaches to Kingdom Come... and all I have is this
little-bitty hammer.  You might think that's a Great Difference Between
Men...

... but *I've* read Hobbes... and *I* know that you gotta go to sleep some
time.'

Rest well, Mr Dashwood.

>
>>... as for 'Sir', I try to avoid that... I was a Sergeant and *my* parents
…[4 more quoted lines elided]…
>a fairy story...

Is that the honest evaluation of one who's participated in a few, then?

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 13)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d25q9$4eq$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8ci6o9$6gt$1@hermes.enternet.co.nz> <uU3H4.16434$0o4.108177@iad-read.news.verio.net> <8cl51o$gtv$1@hermes.enternet.co.nz> <cmFI4.16697$0o4.112628@iad-read.news.verio.net>`

```

>Is that the honest evaluation of one who's participated in a few, then?


Shut up and pass the peanuts...<grin>

Pete.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iK2G4.16205$0o4.105292@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8c65ph$id4$1@hermes.enternet.co.nz> <38E6EE78.FE1C148E@zip.com.au> <8c8mo4$mic$1@hermes.enternet.co.nz>`

```
In article <8c8mo4$mic$1@hermes.enternet.co.nz>,
Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
>Thanks Ken, for setting that straight.
>
…[4 more quoted lines elided]…
>an ugly solution that is being proposed....

Well, Mr Dashwood, I'm glad that someone else managed to set you straight
before I 'graced' the newsgroup with a compile-listing (*with*
PMAP!)... oh, heck, why not...

WORKING-STORAGE SECTION.                                
01  NUMFLD PIC S9(9) COMP-3 VALUE +1.                   
01  STUFF.                                              
    05  DATA-AREA.                                      
        10  NUM-AREA PIC S9(5) COMP-3.                  
    05  TEST-AREA PIC X(5).                             
    05  TEST-AREA-NUM REDEFINES TEST-AREA PIC 9(5).     
PROCEDURE DIVISION.                                     
                                                        
    MOVE ALL 'A' TO DATA-AREA.                          
    MOVE NUM-AREA TO TEST-AREA-NUM.                     
    IF TEST-AREA NOT NUMERIC                            
        DISPLAY ' TUTTI BUONO - ', TEST-AREA-NUM.       
    GOBACK.                                             

... generates...

MOVE       000320                     START    EQU   *                
           000320  05 EC                       BALR  14,12            
           000322  0001                        DC    X'0001'          
           000324  92 C1 6 008                 MVI   008(6),X'C1'     
           000328  D2 01 6 009 6 008           MVC   009(2,6),008(6)  
MOVE       00032E  F3 42 6 00B 6 008           UNPK  00B(5,6),008(3,6)
           000334  96 F0 6 00F                 OI    00F(6),X'F0'     
IF         000338  58 20 C 020                 L     2,020(0,12)      
           00033C  DD 04 6 00B 2 000           TRT   00B(5,6),000(2)  
           000342  58 10 C 030                 L     1,030(0,12)      
           000346  07 81                       BCR   8,1              
DISPLAY    000348  05 EC                       BALR  14,12            
           00034A  0002                        DC    X'0002'          
           00034C  58 F0 C 024                 L     15,024(0,12)     
           000350  05 EF                       BALR  14,15            
           000352  58 F0 C 028                 L     15,028(0,12)     
           000356  05 1F                       BALR  1,15             
           000358  0001                        DC    X'0001'          
           000358  0001                        DC    X'0001'      
           00035A  10                          DC    X'10'        
           00035B  00000F                      DC    X'00000F'    
           00035E  0C000038                    DC    X'0C000038'  
           000362  0000                        DC    X'0000'      
           000364  0F                          DC    X'0F'        
           000365  000005                      DC    X'000005'    
           000368  0D000200                    DC    X'0D000200'  
           00036C  000B                        DC    X'000B'      
           00036E  FFFF                        DC    X'FFFF'      
GOBACK     000370                     GN=01    EQU   *            
           000370  05 EC                       BALR  14,12        
           000372  0003                        DC    X'0003'      
           000374  58 F0 C 024                 L     15,024(0,12) 
           000378  05 EF                       BALR  14,15        
           00037A                     GN=02    EQU   *            

... etc.

Running the code produces the display:

IEF376I  JOB/FRDS38LF/STOP  2000094.1124 CPU    0MIN 00.02SEC SRB    0MIN00.00
 TUTTI BUONO -  1 1                                                            

... so yes, it *does* work... and yes, it *is* ugly.

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c8g9r$drn$1@slb3.atl.mindspring.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz>`

```
One part of what Pete says, I think I need to disagree with (regardless of
compiler).
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c8nm5$mjp$1@hermes.enternet.co.nz>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <8c8g9r$drn$1@slb3.atl.mindspring.net>`

```
Re-read your post Bill (now I can see it...)

Point 2 is a good one. You're quite right that our program may "inherit" bad
data records from a previous process. My position is predicated on the
assumption that data being passed from another program has been validated.

In fact, I think data should be validated at the time it is acquired (I like
the way OO handles this; the object owning the data is responsible for it).

I agree the world is not perfect and there are times when you may need to
apply a CLASS test to numeric fields. But you won't catch me doing
it...<grin>

Pete.



William M. Klein wrote in message <8c8g9r$drn$1@slb3.atl.mindspring.net>...
>One part of what Pete says, I think I need to disagree with (regardless of
>compiler).
…[7 more quoted lines elided]…
>2) The time to do a numeric test (IMHO regardles of USAGE) is when the
field
>might have been "filled" by some group move (and hence may have invalid
>data).  This certainly happens when you move another group to the group
>containing a numeric field (which is often SIGNIFICNANTLY more efficient
that
>moving the individual elementary fields).  More importantly, it ALWAYS
>happens when you read a record.  You get the entire record - and if it has
>any packed, binary, or other numeric fields, these may or MAY NOT be
"valid".
>I think such fields need to be tested somewhere in your application.  This
>may happen when you first get "user input" (and you do validation there) -
>but it also may occur when the records are first about to be used.  This
>depends on the "origin" of the data and the control your application has on
>such.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uE8ThRIo$GA.229@cpmsnbbsa03>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz>`

```

Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote in message
news:8c65ph$id4$1@hermes.enternet.co.nz...

I'm getting into the fray a little late, some of the posts have
clarified the processes involved.

1) PACK & UNPACK will not cause an 0C7. (Already in several posts.)

>
> Do you really need to use a PACKED field at all? This format is
rooted in
> the days when external media cost a fortune and it was necessary to
> "compress" everything possible.

We used packed whether we like it or not.
1) DB2 carries decimal numbers in packed format, thus the DCLGEN will
have computational-3 fields. (I beleive the MS-Jet engine also
supports decimal format for COBOL applications).

2) When you use a display numeric item, it is converted to COMP-3 for
processing.
There may be some situations where it is converted to binary, but it
will be converted to comp-3 first.
Using COMP or COMP-3 cuts your conversion overhead.
You not only save data space (WS, Linkage etc), you also save
Instruction space (Procedure Division). You would probably need a
high-volume computational situation to see a difference in CPU
utilization.

>
> There is a real question as to whether we need this format in
today's
> processing. There probably isn't an IBM programmer alive who has
never had
> an 0C7 caused by "packing a blank" or some other invalid character.
Yes, you
> can argue that if you are processing invalid data, it is better NOT
to
> continue (that was IBM's philosophy) but other vendors who never
implemented
> PACKED and the associated data exception, still made a living...
>

You can pack a blank or low-values and continue processing in some
situations.
If you move the field to an UNSIGNED field, an "Or Immediate" OI will
be generated to force the Sign to unsigned. (x"F0" or x"0F"). Check
out Doc's PMAP.

field-a PIC S9(5).
Field-b pic 9(5) comp-3.

assume FIELD-A = spaces X'4040404040"
MOVE FIELD-A to field-B.
after PACK Field-b = x'000004'
after OI Field-b = x'00000F'
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EDDCAF.2FFA61FE@cusys.edu>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03>`

```
Working in different (mainframe) environments, I have had mixed results
with checking IF NUMERIC on non display data.  But I can't remember the
details.  It might be a good idea to keep this in the back of your mind
if you ever change environments, especially if you work in an old,
unfamiliar OS.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl3cc$7he$1@news.igs.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03>`

```

DennisHarley wrote in message ...
>
>Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote in message
…[55 more quoted lines elided]…
>

??? X"40"=space?
I always thought it was hex 20.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cl4mb$3ft$1@slb6.atl.mindspring.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net>`

```

"donald tees" <donald@willmack.com> wrote in message
news:8cl3cc$7he$1@news.igs.net...
>
  <snip>
> >
> >field-a PIC S9(5).
…[11 more quoted lines elided]…
>

Donald, - am I missing a <G> here?

We are talking explicitly about IBM mainframe environment here - which are
VERY definitely EBCDIC - where spaces are X'40' not the ASCII X'20'.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IUoH4.146443$Hq3.3432812@news2.rdc1.on.home.com>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net>`

```

"donald tees" <donald@willmack.com> wrote in message
news:8cl3cc$7he$1@news.igs.net...
>
<<snip>>
> ??? X"40"=space?
> I always thought it was hex 20.
>
X"40" = EBCDIC
X"20" = ASCII
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8clo63$hi2$1@news.igs.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <lHKD4.9069$0o4.66330@iad-read.news.verio.net> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net> <IUoH4.146443$Hq3.3432812@news2.rdc1.on.home.com>`

```
Oscar T. Grouch wrote in message ...
>
>"donald tees" <donald@willmack.com> wrote in message
…[8 more quoted lines elided]…
>

I actual thought of that as I hit the "post" button, but did not ask as I
was embarrassed over the fact I did not know how to spell EBCDIC.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LIpH4.16508$0o4.109295@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net>`

```
In article <8cl3cc$7he$1@news.igs.net>,
donald tees <donald@willmack.com> wrote:
>
>DennisHarley wrote in message ...

[molto snippenmtio]

>>assume FIELD-A = spaces X'4040404040"
>>MOVE FIELD-A to field-B.
…[5 more quoted lines elided]…
>I always thought it was hex 20.

The answer is... maybe it is, maybe it ain't.  What does your yellow card
tell you about those values?

(note to various Codgers:  I *know* it was nasty but I couldn't resist)

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8clogi$hr0$1@news.igs.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net>`

```
Strangely enough, though I have coded Cobol now for thirty-three years, I
have never done it on an IBM machine.  I started on a PDP-10, used a Cyber
64, Honeywell 200, Honeywell 6000, Altos, then PC's since about 82.  The
only IBM machine I ever used was a series 1, and I was coding on that in
PL1.

docdwarf@clark.net wrote in message ...
>In article <8cl3cc$7he$1@news.igs.net>,
>donald tees <donald@willmack.com> wrote:
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rdxH4.16533$0o4.109686@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net>`

```
In article <8clogi$hr0$1@news.igs.net>,
donald tees <donald@willmack.com> wrote:
>Strangely enough, though I have coded Cobol now for thirty-three years, I
>have never done it on an IBM machine.  I started on a PDP-10, used a Cyber
>64, Honeywell 200, Honeywell 6000, Altos, then PC's since about 82.  The
>only IBM machine I ever used was a series 1, and I was coding on that in
>PL1.

Thanks e'er-so-much for 'sharing' with the group, Mr Tees... but my memory
is, admittedly, porous; where did I say anything about IBM?

DD

>
>docdwarf@clark.net wrote in message ...
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EF321B.FD9DDE66@zip.com.au>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
> In article <8clogi$hr0$1@news.igs.net>,
…[9 more quoted lines elided]…
> memory is, admittedly, porous; where did I say anything about IBM?

How many non IBM ebcdic machines are there.  You also mentioned a
yellow card, refering to the IBM ebcdic reference card.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OknnlTko$GA.226@cpmsnbbsa03>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net> <38EF321B.FD9DDE66@zip.com.au>`

```
Between the mid 70's and about 1992-3, the PRIME corporation (with one of
the hottest NYSE stocks of 1980) manufactured computers that used EBCDIC.
They were used all over the place, and there are a few holdouts here and
there still using them (they get support from 3rd party support vendors
who've taken over care of these aging computers).


"Ken Foskey" <waratah@zip.com.au> wrote in message
news:38EF321B.FD9DDE66@zip.com.au...
> docdwarf@clark.net wrote:
> >
…[17 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** bbreynolds@aol.comskipthis (Bruce B. Reynolds)
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000410174937.18319.00000832@ng-fz1.aol.com>`
- **References:** `<38EF321B.FD9DDE66@zip.com.au>`

```
>How many non IBM ebcdic machines are there.

Burrough B3500, etc.  In Vietnam I got
a systems job because I could spell
EBCDIC.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1D1B8.DC08E1AB@cusys.edu>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net> <38EF321B.FD9DDE66@zip.com.au>`

```
Ken Foskey wrote:
> 
> How many non IBM ebcdic machines are there.  You also mentioned a
> yellow card, refering to the IBM ebcdic reference card.

I used a Univac 9030.  What did the RCAs use?
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tFI4.16699$0o4.112366@iad-read.news.verio.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net> <38EF321B.FD9DDE66@zip.com.au>`

```
In article <38EF321B.FD9DDE66@zip.com.au>,
Ken Foskey  <waratah@zip.com.au> wrote:
>docdwarf@clark.net wrote:
>> 
…[12 more quoted lines elided]…
>How many non IBM ebcdic machines are there.

Amdahl is the first which comes to mind... and I know that MicroFocus has
EBCDIC/ASCII switches, for whatever use they might have.

>You also mentioned a
>yellow card, refering to the IBM ebcdic reference card.

Ahhhh, the quaint art of misdirection snares another one!... certainly the
yellow card is the IBM reference but EBCDIC codes are EBCDIC codes... or
are you saying that the speed of light found in the Encyclopaedia
Britannica is the 'British' one?

DD
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cnl40$mlo$1@news.igs.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote in message ...
>In article <8clogi$hr0$1@news.igs.net>,
>donald tees <donald@willmack.com> wrote:
…[9 more quoted lines elided]…
>DD

You use IBM terms, and IBM "in" jokes; I explained why I do not "get" them.
Perhaps, though, I am mistaken. Perhaps EBCDIC has come into common usage by
other hardware vendors and I have just missed it. Perhaps many vendors now
have yellow cheat sheets.  Maybe they have even started to paint their
machines blue. Maybe "JCL" and "CICS" and "abend" and countless other terms
have become so geriatric(oops, meant generic), that they now apply to the
CPU in a Timex digital.

You are being a bit aggressive this morning Doc. But then, I have not eaten
breakfast yet either, so perhaps I should just mention Hitler and back out.

Donald --> A *CRANKY* old codger, damnit.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F1D245.64673572@cusys.edu>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net> <rdxH4.16533$0o4.109686@iad-read.news.verio.net> <8cnl40$mlo$1@news.igs.net>`

```
donald tees wrote:
> 
> Perhaps many vendors now have yellow cheat sheets.  

Interesting enough, I don't think I have seen a cheat sheet at my
current workplace other than mine, and I usually pull out my green one
when I need it.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EEECFA.340E8C90@worldnet.att.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <8c65ph$id4$1@hermes.enternet.co.nz> <uE8ThRIo$GA.229@cpmsnbbsa03> <8cl3cc$7he$1@news.igs.net> <LIpH4.16508$0o4.109295@iad-read.news.verio.net> <8clogi$hr0$1@news.igs.net>`

```
donald tees wrote:
> 
> Strangely enough, though I have coded Cobol now for thirty-three years, I
…[4 more quoted lines elided]…
> 

An IBM Series/1?  Was that EDX or RPS (or perhaps even CPS or Unix)? 
The IBM Series/1 was an EBCDIC machine and I have fond memories of
coding ANSI-74 COBOL on it.  My recollection was that COBOL on the
Series/1 supported only DISPLAY USAGE and COMP numerics.  No COMP-3 or
packed-decimal of any kind.

If you used the RPS operating system, it was similar to OS/360 or MVS. 
EDX (Event Driven Executive) was quite a bit different.

I remember my very first COBOL program on the Series/1 (just about 21
years ago).  They needed a day-of-week subroutine.  I had no idea how
that was done, so they gave me an old S/360 assembler routine to copy
from.  I managed to convert it without understanding it completely, but
it did need a date with a four-digit year.

We got rid of our last S/1 in January.  IBM stopped making them around
1992.  They weren't Y2K compliant.
```

###### ↳ ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

_(reply depth: 8)_

- **From:** bbreynolds@aol.comskipthis (Bruce B. Reynolds)
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000410174535.18319.00000830@ng-fz1.aol.com>`
- **References:** `<38EEECFA.340E8C90@worldnet.att.net>`

```
>An IBM Series/1?  Was that EDX or RPS (or perhaps even CPS or Unix)? 
>The IBM Series/1 was an EBCDIC machine and I have fond memories of
…[20 more quoted lines elided]…
>

Packed decimal available in the MFSL
(Mathematical and Functional Subroutine
Library), which could be used with COBOL,
PL/I, FORTRAN, or assembler on RPS and
CPS, plus EDL under EDX; essentially
a combination of the CSP (Commercial
Subroutine Package) and SSP (Scientific
Subroutine Package) from S/360 and
1130/1800 days.  The examples were
written as if cards were still in use.

The Series/1 is Y2K compliant, and
EDX is also compliant, except that the
date displays on the operator commands
do not zero fill, so that there is garbage
shown; tested and in use on Series/1's
and emulated Series/1's at my last
contracts.

PS: IBM sold an incrediably small number
of the "IX" for Series/1.
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8booo5$fgj$1@slb7.atl.mindspring.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
There are several (correct) replies to this note indicating that the BEST way
to fix this problem is to put in an explicit IF NUMERIC test.  This should be
done (contrary to what some have suggested) against the field "dato-num" and
NOT against the group field.  This wouldn't be required if the numeric field
were USAGE display, but there is no way to test a "group item" to see if one
of the subordinate fields is correctly a PACKED numeric field.

Having said that, I think it is important to point out to the original poster
that there is NO GUARANTEE that an IBM mainframe COBOL program will (or will
not) get an S0C7 if there is non-numeric data in a numeric field.  This was
(is) one of the MAJOR inhibitors in moving from OS/VS COBOL to the newer
COBOLs.  *ALL* that IBM (or the COBOL Standard) requires is that *if* a
numeric field contains "incompatible data" that the results are
UNPREDICTIBABLE.

If there is a case that DOES get an S0C7 on the mainframe but does not get an
"exception" on the Workstation, I would suggest that you contact IBM for
information on how to get the most "compatible" results.
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9oh3es0ne2pgbgqm6nc5qfn8vcj30u6o61@4ax.com>`
- **References:** `<8bng6o$11p$1@news.flashnet.it>`

```
On Mon, 27 Mar 2000 13:20:27 +0200 "Gianluigi Angotti" <giangol@tin.it> wrote:

:>Visual Age for Cobol Windows NT.
:>When assign a not numeric data in a COMP-3 variable, this don't  cause a run
:>time error (the same in debug)

:>        01    AREA-DATI.
:>        03     DATO-NUM                PIC S9(5)  COMP-3.
:>     ....
:>     MOVE 'AAAAAAAAA'       TO AREA-DATI.
:>     IF DATO-NUM  > 0
:>        DISPLAY '*** DATO MAGGIORE DI ZERO'
:>     END-IF.

:>This istruction give a "0C7"  (data exception) in a MVS system.
:>You know a method to intercept this error in a NT system ???

You cannot always check a COMP type field for NUMERIC and get meaningful
results. For example, a true binary field is ALWAYS numeric, by definition. 

You have to check the source (USAGE DISPLAY) field before moving it to a COMP
field.

As a side point, try  

   MOVE "//*" to AREA-DATI 

on S/390 architecture. You will not notice an 0C7 since

    c'//*' = x'61615c'

which happens to fit the rules for a 5 digit packed number (+61615). 

If DATA-NUM was described as USAGE COMP then no matter what you moved into
AREA-DATI you would not get an 0C7.
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bto7k$efj$1@slb2.atl.mindspring.net>`
- **References:** `<8bng6o$11p$1@news.flashnet.it> <9oh3es0ne2pgbgqm6nc5qfn8vcj30u6o61@4ax.com>`

```
Binyamin,
  Interestingly enough the "IF NUMERIC" test in the COBOL revision is defined
to NOT always give a "true" result for a binary field.  Instead, it is
defined to check that the value fits into the PICTURE clause of the field.
In other words, (using typical OS/390 type terminology) it will check that
the value is valid for TRUNC(STD).

This was discussed at J4 and this was felt to be the "best" solution.  In the
draft, there are a number of NEW usages (e.g. binary-char) which define
binary items WITHOUT a picture clause - where the IF NUMERIC test will always
be true.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
