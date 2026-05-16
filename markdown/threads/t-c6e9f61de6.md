[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_84 messages · 17 participants · 2003-09 → 2003-10_

---

### 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** dhaar@mideal.de (Dirk Haar)
- **Date:** 2003-09-16T02:40:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`

```
Hi !
I had a very hard discussion with a collegue 
trying to make him understand why a SET xx TO FALSE can't work.

I could not convince him by means of Boole logic examples etc.

Can anybody give me a hint how to make it clear ?
Are there any COBOL tutorials where it is explained completely?

Please remember we both got more than 20 years COBOL experience,
so don't answer "BECAUSE 'FALSE' IS NOT A COBOL WORD blabla'".

Thanks you,

Dirk
```

#### ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-16T11:25:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`

```
On 16 Sep 2003 02:40:56 -0700, dhaar@mideal.de (Dirk Haar) wrote:

>Hi !
>I had a very hard discussion with a collegue 
…[12 more quoted lines elided]…
>Dirk


It DOES work with some COBOL versions.

01  variablex pic x.
88 VALID-ANSWER VALUE "Y" WHEN SET TO FALSE "N".

...

IF (INPUT-FIELD = "A" OR "B" OR "C")
    SET VALID-ANSWER TO TRUE
ELSE
    SET VALID-ANSWER TO FALSE
END-IF



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-16T21:48:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<No2cndjGpIQSVvqiXTWJkw@giganews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com>`

```
Frederico Fonseca wrote:

>
>
…[11 more quoted lines elided]…
> END-IF

If I can interject something regarding style. Using your example, I know
there are programmers who like this technique along with its companion:

IF VALID-ANSWER
   (do something)


Me, I prefer

IF (INPUT-FIELD = 'A' OR 'B' OR 'C')
   MOVE 'Y' TO VALID-ANSWER
ELSE
   MOVE 'N' TO VALID-ANSWER.

then

IF VALID-ANSWER = 'Y'
   (do something)

I'm certain the difference is only a matter of style. Except with mine, I
can handle the VALID-ANSWER = "M(aybe)" case.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-17T18:23:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f68057e_6@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com>`

```
Jerry,

you're right, it is about style. (And personal preferences...)

Personally I HATE both yours and Frederico's.

Seeing "Y" and "N" in COBOL programs just makes me shiver.

We are interested in a LOGICAL TRUE or FALSE, NOT a linguistic affirmative
or negative... ( Besides, I have written COBOL in countries where
affirmative and negative are NOT "Yes" and "No"...

But, I am experienced enough to know that it doesn't REALLY matter in terms
of what code does.

It is a matter of style.

(Some more comments below...)

"JerryMouse" <nospam@bisusa.com> wrote in message
news:No2cndjGpIQSVvqiXTWJkw@giganews.com...
> Frederico Fonseca wrote:
>
…[33 more quoted lines elided]…
>
So your argument comes down to the case for and against using 88 levels. For
you, "VALID-ANSWER" is not a logic state it is a variable.

> I'm certain the difference is only a matter of style. Except with mine, I
> can handle the VALID-ANSWER = "M(aybe)" case.
>

I can see NO DIFFERENCE between using the example which sets valid-answer
FALSE (where "False" is defined as "N"), and the example you give above.
They are logically identical. The 88 level example arguably gives better
documentation, but you handle this with a "meaningful dataname".
(Personally, I prefer 88 levels...)

As for your "maybe" case, if it isn't "Y" or "N" then you HAVE to test for
"M" (or whatever) using a specific test IN EITHER CASE!

To assume it MIGHT be something other than Y or N indicates you have no
control over it...<G>

Here's a solution:

01 flag-variable     pic x value space. *> the initial setting of a flag
should be "indeterminate"; it must be specifically
                                                        *> set to a value by
process code.
    88 valid-answer                   value '1'.
    88  valid-answer-FALSE     value '0'.

This caters for TRUE, FALSE, and MAYBE. (Maybe can be decided by "NOT
(valid-answer OR valid-answer-FALSE)"

if valid-answer
   (do something)
else
    if-valid-answer-FALSE
     (do something else)
    else
      (do maybe)
    end-if
end-if

But this is just begging for EVALUATE, and that is what I would use...

evaluate TRUE
      when valid-answer
               (do something)
      when valid-answer-FALSE
               (do something else)
      when other
               (do maybe)
end-evaluate
...

Many people won't like this at all and that's OK too...

As long as the correct results are obtained, the rest is style and
preference.

Pete.







>
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-18T03:04:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wg9ab.1424$Od.107134@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com>`

```
I sometimes add a third field.

process code.
    88 valid-answer                  value 1.
    88 valid-answer-FALSE     value 0.
    88 valid-answer-state          values 0,1.

Then replace any

IF  NOT (valid-answer OR valid-answer-FALSE)

with

IF NOT VALID-ANSWER-STATE.

Doesn't make sense particularly in this example being just a
TRUE/FALSE...but it means you have a simple way to check that the field is
something that it *should* be and is not unknown.
So for example if the field could have 10 answers but we're only checking 0
and 1.
    88 valid-answer-state          values 0 THRU 10.

It's a quick way to check (in the WHEN OTHER for example) that the maybe
still has some integrity and isn't just a "junk" value.

evaluate TRUE
     when valid-answer
               (do something)
     when valid-answer-FALSE
             (do something else)
    when valid-answer-state
               (do maybe)
     when other
               (do error)
end-evaluate

JCE

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f68057e_6@news.athenanews.com...
> Jerry,
>
…[10 more quoted lines elided]…
> But, I am experienced enough to know that it doesn't REALLY matter in
terms
> of what code does.
>
…[42 more quoted lines elided]…
> So your argument comes down to the case for and against using 88 levels.
For
> you, "VALID-ANSWER" is not a logic state it is a variable.
>
> > I'm certain the difference is only a matter of style. Except with mine,
I
> > can handle the VALID-ANSWER = "M(aybe)" case.
> >
…[17 more quoted lines elided]…
>                                                         *> set to a value
by
> process code.
>     88 valid-answer                   value '1'.
…[32 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-18T03:19:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iv9ab.1464$Od.111561@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f68057e_6@news.athenanews.com...
> Jerry,
>
…[9 more quoted lines elided]…
>     88 valid-answer                   value '1'.

Even though you say it is a style issue I'm going to ask my question out of
curiousity.

IYHO - Should all 88's be numeric? I would assume that you would have no
problem with :

88 FILE-IS-OPEN        VALUE 'O'.
88 FILE-IS-CLOSED   VALUE 'C'.

I wasn't sure if you were talking specifically about hating the values
within the mainline code as in
IF RESPONSE = 'Y', or whether you meant the 88 level also.

I've always found the notion of naming and notation in source code to be an
interesting issue (I work with many dutchman who do things very
differently - though english - thankfully).

Your point is well taken in terms of APIs/external inputs though because I
once supported a product with an api where we had letters for control....we
had "A" for adjustment.  It took us ten minutes to explain to our Japanese
counterparts what adjustment meant :-) The letter "A" was totally
meaningless for them.
However,  I don't see the issue so much in source code if it's not input
from outside world.  Having a check for "Y" if the value is entered on a
screen is setting you up for difficulty later on... if it's just internal
source control fields why would it matter?

And here, I am kidding.....

Shouldn't your 88 level be:
88 A1                VALUE '1'

because
88 VALID-ANSWER          VALUE 'Y' SET TO FALSE 'N'
88 GULTIGE-ANTWORT   VALUE 'J' SET TO FALSE 'N'
88 RISPOSTA-VALIDA      VALUE 'S' SET TO FALSE 'N'
88 RESPOSTA-VALIDA     VALUE 'S' SET TO FALSE 'N'
88 RESPUESTA-VALIDA   VALUE 'S' SET TO FALSE 'N'
88 RESPONSE-VALIDE     VALUE 'O' SET TO FALSE 'N'

have no meaning in some countries....:-)


JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 5)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-18T02:00:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmim0dg4hh2hde@corp.supernews.com>`
- **In-Reply-To:** `<iv9ab.1464$Od.111561@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com>`

```
jce wrote:

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f68057e_6@news.athenanews.com...
…[22 more quoted lines elided]…
> 88 FILE-IS-CLOSED   VALUE 'C'.

That's the beauty of 88-levels.  Who cares what the value is?  I don't 
even name the elementary items anymore - forces me to use the Set to 
True syntax.  If we need more conditions, I can change the definition 
from a Pic 1(01) to Pic 1(02) (for 2 more conditions), or a Pic X if I 
need 26 all at one whack.  Application code changes (for the existing 
conditions)?  Zilch.  :)

I don't understand why people wouldn't like 88-levels.  They make code 
so readable...
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-18T11:52:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309181052.4bd60a09@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote
 
> I don't understand why people wouldn't like 88-levels.  They make code 
> so readable...

There is a huge difference between 'being nice because they are
locally readable' and 'being globally findable'.

Quite often I want to find out where in a whole system where a
particular variable is used.  If it has been used in the form "IF (
variable = value .. )" then it is easy to grep for.  If it has been
aliased into several different names using 88 levels then it is very
much more difficult to find.

It can be just as readable to have the flag values as constants (or
fixed value variables) rather than single character literals.

Instead of:

           MOVE "Y"     TO File-Indicator
           ...
           IF ( File-Indicator = "Y" )

You may have:

           SET File-Indicator-EoF  TO TRUE
           ....
           IF ( File-Indicator-EoF )

I may have:

           MOVE Status-EoF     TO File-Indicator
           ...
           IF ( File-Indicator = Status-EoF )

Both add readability.  Mine does not use aliases.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-18T21:19:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com>`

```
Again, (as I said to Howard) - think about getting one of the MULTITUDE of
products that let you find all explicit and implicit references to a field.
Using "grep" or "find" to find all references to a field is simply NOT
"state-of-the-art".
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-18T19:36:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkdfik$fmm$1@panix1.panix.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net>`

```
In article <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Again, (as I said to Howard) - think about getting one of the MULTITUDE of
>products that let you find all explicit and implicit references to a field.
>Using "grep" or "find" to find all references to a field is simply NOT
>"state-of-the-art".

Hey, you got something against 'documentation via SuperC?'  Outside of the 
hours spent poring over output-lists it sure don't cost much!

DD
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-18T20:27:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309181927.5e664300@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote

> Again, (as I said to Howard) - think about getting one of the MULTITUDE of
> products that let you find all explicit and implicit references to a field.
> Using "grep" or "find" to find all references to a field is simply NOT
> "state-of-the-art".

<shrug> Why would I need to go out and buy some 'multitude' when what
I do works perfectly </shrug>.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-19T03:31:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gMuab.37321$NM1.26875@newsread2.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net> <217e491a.0309181927.5e664300@posting.google.com>`

```
Because, if you can't easily use 88-levels, then I question that what you
have now "works perfectly".
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T08:19:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TvCab.11870$hF3.1303963@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net...
> Again, (as I said to Howard) - think about getting one of the MULTITUDE of
> products that let you find all explicit and implicit references to a
field.
> Using "grep" or "find" to find all references to a field is simply NOT
> "state-of-the-art".
>
> Bill Klein

What would you suggest with net express and a PC? A full compile takes 45
minutes.

Donald
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-19T22:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R%Kab.39583$NM1.13746@newsread2.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <Djpab.36989$NM1.16526@newsread2.news.atl.earthlink.net> <TvCab.11870$hF3.1303963@news20.bellglobal.com>`

```
I would suggest REVOLVE which works well with Net Express and does EXACTLY
what you are saying you can't currently do.  For more information, see:

 http://www.microfocus.com/products/revolve/datasheet.asp
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-09-18T17:32:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkdfb7$g99s$2@ID-184804.news.uni-berlin.de>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com>`

```
>>> Richard<riplin@Azonic.co.nz> 09/18/03 12:52PM >>>
>LX-i <LXi0007@Netscape.net> wrote
…[34 more quoted lines elided]…
>Both add readability.  Mine does not use aliases.

Which is why the C method (see previous message) is great.  It's the best of
both worlds.  You don't need aliases but you can also set by 'value'.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T08:20:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_wCab.11876$hF3.1304332@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <217e491a.0309181052.4bd60a09@posting.google.com> <bkdfb7$g99s$2@ID-184804.news.uni-berlin.de>`

```
"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bkdfb7$g99s$2@ID-184804.news.uni-berlin.de...
> >>> Richard<riplin@Azonic.co.nz> 09/18/03 12:52PM >>>
> >LX-i <LXi0007@Netscape.net> wrote
…[36 more quoted lines elided]…
> Which is why the C method (see previous message) is great.  It's the best
of
> both worlds.  You don't need aliases but you can also set by 'value'.
>
>

There is a perfectly good Cobol mechanism for setting constants.

Donald
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T08:16:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<btCab.11857$hF3.1303559@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com>`

```
"LX-i" <LXi0007@Netscape.net> wrote in message
news:vmim0dg4hh2hde@corp.supernews.com...
> jce wrote:

> > 88 FILE-IS-OPEN        VALUE 'O'.
> > 88 FILE-IS-CLOSED   VALUE 'C'.
…[10 more quoted lines elided]…
>

And almost unmaintainable at the same time.  I have a 250 program, 500,000
line system that I inherited all written just as you say.  To find a
parameter that is incorrect, I have to search 250 different programs for 10
to 15 different data names to find out where it changed.

I cannot find out it's value by single stepping ... all I can do is find out
if a specific condition is true or false.  I CANNOT tell what condition *is*
true, unless I go back to working storage, give the parameter a name, then
display that parameter in the program, or reference it by name so the
debugger can show me the actual value.

Personally, I think it one of the worst style fads to come along in 35 years
of Cobol.  It sucks shit.

Donald
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-19T23:25:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmnllbnsf8qh2d@corp.supernews.com>`
- **In-Reply-To:** `<btCab.11857$hF3.1303559@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com>`

```
Donald Tees wrote:
> "LX-i" <LXi0007@Netscape.net> wrote in message
> news:vmim0dg4hh2hde@corp.supernews.com...
…[18 more quoted lines elided]…
> of Cobol.  It sucks shit.

Reference modification can be severely abused as well.  Ditto for lots 
of other things in COBOL.  It's not a style fad, it's a great way to do 
simple and mutually-exclusive conditions, and validate data.  Now, if 
it's used for much more than that, I could see it getting too 
complicated to follow without way too many brain waves wasted on the 
effort, but are you saying it has no value at all?  (Being able to do it 
a different way doesn't mean it's not valuable.)
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-21T10:03:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dibb.519$yD1.50662@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com>`

```
"LX-i" <LXi0007@Netscape.net> wrote in message
news:vmnllbnsf8qh2d@corp.supernews.com...
> Donald Tees wrote:
> > "LX-i" <LXi0007@Netscape.net> wrote in message
…[7 more quoted lines elided]…
> > And almost unmaintainable at the same time.  I have a 250 program,
500,000
> > line system that I inherited all written just as you say.  To find a
> > parameter that is incorrect, I have to search 250 different programs for
10
> > to 15 different data names to find out where it changed.
> >
> > I cannot find out it's value by single stepping ... all I can do is find
out
> > if a specific condition is true or false.  I CANNOT tell what condition
*is*
> > true, unless I go back to working storage, give the parameter a name,
then
> > display that parameter in the program, or reference it by name so the
> > debugger can show me the actual value.
> >
> > Personally, I think it one of the worst style fads to come along in 35
years
> > of Cobol.  It sucks shit.
>
…[7 more quoted lines elided]…
>

Not at all.  88 levels are a great way to make conditionals table driven ...
that is all code can be changed simply by changing the values of the 88's.
File status values that may change from platform to platform are a perfect
example of this, and an obvious place to use 88's.

However, to bury procedure division conditional statements in a table of
conditional values located in a copy book, 3000 lines away in the program
for the sake of "style" is another thing all together.  That is particularly
true when they are unlikely to change.  The possible alternate values are
the main reason for table driving it, and 88's are just a way of defining
conditionals in a table..

What does it gain?

Take the simple Y/N or T/F situation that is being talked about.  What does
the use of "SET", and an 88 level conditional add to the code in terms of
information?  When you see
        "IF condition1"
as compared to
        'if flag1 is equal to "Y"'
it gives you LESS information, not more.  You have lost the name of the
parameter that is being tested (unless you cross check it), you have lost
the ability to check it's real value, (using a debugger), and you are no
longer able to see that it is a simple "T/F" conditional (an inference,
granted, but still a major clue in understanding the code).

What you have really done is set up a one entry table for a simple
conditional, and added and extra level of ambiguity at the procedure level.
The reader must read the data division to see what is being done.

Donald
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2003-09-25T19:31:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0oHcb.3522$SC5.2484693131@newssvr12.news.prodigy.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com> <8dibb.519$yD1.50662@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:8dibb.519$yD1.50662@news20.bellglobal.com...
[snip]

I am coming late to this discussion, so this may be redundant.


> Take the simple Y/N or T/F situation that is being talked about.  What
does
> the use of "SET", and an 88 level conditional add to the code in terms of
> information?  When you see
…[4 more quoted lines elided]…
> parameter that is being tested (unless you cross check it),

The following is possible:

01  pic x.
    88  is-a-readable-name value "Y" false "N".

No name is lost.

> you have lost
> the ability to check it's real value, (using a debugger), and you are no
> longer able to see that it is a simple "T/F" conditional (an inference,
> granted, but still a major clue in understanding the code).

Hmmm.  Perhaps the debugger should be able to display the value of a
condition-name, the value being <true> or <false>.

===

Perhaps a difficulty in this thread is that condition-names may be used
stand-alone to help maintain program state or in conjunction with a
data-item.   Style questions relating to one use are irrelevant to the
other.

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-26T14:29:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl1ifh$4vo$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com> <8dibb.519$yD1.50662@news20.bellglobal.com> <0oHcb.3522$SC5.2484693131@newssvr12.news.prodigy.com>`

```

On 25-Sep-2003, "Tom Morrison" <t.morrison@liant.com> wrote:

> The following is possible:
>
…[3 more quoted lines elided]…
> No name is lost.

That works if your compiler accepts it (mine doesn't), and if your switch is
binary.   If it can have more values, your grep is not reliable.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 11)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2003-09-26T15:55:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DjZcb.2014$Un4.934@newssvr23.news.prodigy.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com> <8dibb.519$yD1.50662@news20.bellglobal.com> <0oHcb.3522$SC5.2484693131@newssvr12.news.prodigy.com> <bl1ifh$4vo$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:bl1ifh$4vo$1@peabody.colorado.edu...
>
> On 25-Sep-2003, "Tom Morrison" <t.morrison@liant.com> wrote:
…[8 more quoted lines elided]…
> That works if your compiler accepts it (mine doesn't), and if your switch
is
> binary.   If it can have more values, your grep is not reliable.

I was replying to a situation where indeed the switch was binary.

What part of this does your compiler reject -- the FALSE clause?

Tom Morrison
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-26T17:00:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl1rbu$7f$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com> <8dibb.519$yD1.50662@news20.bellglobal.com> <0oHcb.3522$SC5.2484693131@newssvr12.news.prodigy.com> <bl1ifh$4vo$1@peabody.colorado.edu> <DjZcb.2014$Un4.934@newssvr23.news.prodigy.com>`

```

On 26-Sep-2003, "Tom Morrison" <t.morrison@liant.com> wrote:

> > That works if your compiler accepts it (mine doesn't), and if your switch
> is
…[4 more quoted lines elided]…
> What part of this does your compiler reject -- the FALSE clause?

Yep.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-22T16:40:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkn8l7$g4r$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com>`

```

On 19-Sep-2003, LX-i <LXi0007@Netscape.net> wrote:

> Reference modification can be severely abused as well.  Ditto for lots
> of other things in COBOL.  It's not a style fad, it's a great way to do
…[4 more quoted lines elided]…
> a different way doesn't mean it's not valuable.)

I once worked in a shop that was previously 100% RPG II.   Doing maintenance on
those programs, I came to the conclusion that RPG was OK as long as the person
writing it didn't know how to do much with it.   Someone knowledgeable enough to
do weird things left behind programs that were maintenance nightmares.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-09-22T13:13:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bknakj$8nq$1@panix1.panix.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <btCab.11857$hF3.1303559@news20.bellglobal.com> <vmnllbnsf8qh2d@corp.supernews.com> <bkn8l7$g4r$1@peabody.colorado.edu>`

```
In article <bkn8l7$g4r$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:

[snip]

>I once worked in a shop that was previously 100% RPG II.   Doing maintenance on
>those programs, I came to the conclusion that RPG was OK as long as the person
>writing it didn't know how to do much with it.   Someone knowledgeable enough to
>do weird things left behind programs that were maintenance nightmares.

Hmmmmm... sounds similar to what I have labelled as 'Look, Ma, I'm a 
Programmer!' code; this can, to the best of my knowledge, exist in any 
language.

DD
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-20T15:02:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f6bc464_9@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:iv9ab.1464$Od.111561@twister.tampabay.rr.com...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[9 more quoted lines elided]…
> > We are interested in a LOGICAL TRUE or FALSE, NOT a linguistic
affirmative
> > or negative... ( Besides, I have written COBOL in countries where
> > affirmative and negative are NOT "Yes" and "No"...
> >     88 valid-answer                   value '1'.
>
> Even though you say it is a style issue I'm going to ask my question out
of
> curiousity.
>
…[5 more quoted lines elided]…
>
No, I don't like 'O' and 'C' either <G>.

The point about an 88 level is that it really shouldn't matter WHAT value
you use because you are NEVER going to look at it again...

You will use SET  to set the condition and IF to test it; the actual value
is irrelevant.

I wouldn't go so far as to say that I think ALL 88 levels should have a
numeric value (actually, for efficiency in the mainframe environment, I use
a non-numeric field even when the value IS numeric.... That's just habit
from working with mainframes over 20 years... I still do it on the PC.)

For example, if a given system has a certain code defined, I would see no
problem with setting 88 levels to represent the coding structure...

01     record-layout.
         12 record-type   pic xxx.
              88 insert-record       value 'NEW'.
              88 change-record    value 'CHG'.
              88 delete-record      value 'DEL'.
          etc.

When it comes to internal logic states I would prefer 0 and 1. (These are
simply Boolean Truth values in Boolean Algebra; 0 represents the additive
identity and 1 represents multiplicative identity...the fact that certain
computer lanuages represent TRUE as 1 and FALSE as -1 has more to do with
computer hardware than with the postulates of George Boole <G>)

 So the fact that a file is open or closed would be represented (at least in
code written by me...) as:

01   xxx-file-open-flag    pic x value space.
       88  xxx-file-is-open      value '1'.
       88  xxx-file-is-closed    value '0'.

If the program crashed or abended it would be possible to determine easily
from the state of the flag whether the logic to open or close the file had
ever been executed... the same principle applies to all my flags.

> I wasn't sure if you were talking specifically about hating the values
> within the mainline code as in
> IF RESPONSE = 'Y', or whether you meant the 88 level also.
>
Both, but I have less aversion to the 88 as you never really need to look at
it and its value is really unimportant; what is important is the STATE that
it represents.

> I've always found the notion of naming and notation in source code to be
an
> interesting issue (I work with many dutchman who do things very
> differently - though english - thankfully).
>
> Your point is well taken in terms of APIs/external inputs though because I
> once supported a product with an api where we had letters for
control....we
> had "A" for adjustment.  It took us ten minutes to explain to our Japanese
> counterparts what adjustment meant :-) The letter "A" was totally
…[20 more quoted lines elided]…
>

LOL!

Yes, exactly.

(I've always considered it a little arrogant to expect foreign speakers to
recognise YES and NO in program code (even though  they do...) especially
when you are working in THEIR country and THEIR culture...it's more courtesy
than programming practice.)

Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-20T04:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rzQab.13438$kg.7743@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <3f6bc464_9@news.athenanews.com>`

```

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f6bc464_9@news.athenanews.com...
> > "jce" <defaultuser@hotmail.com> wrote in message
<snip snip>
> > IYHO - Should all 88's be numeric? I would assume that you would have no
> > problem with :
…[5 more quoted lines elided]…
>
<snip snip>
> I wouldn't go so far as to say that I think ALL 88 levels should have a
> numeric value (actually, for efficiency in the mainframe environment, I
use
> a non-numeric field even when the value IS numeric.... That's just habit
> from working with mainframes over 20 years... I still do it on the PC.)
A numeric comparison is not as efficient as a character one ?  Not that I am
about to change for the 1ns saving ;)

> When it comes to internal logic states I would prefer 0 and 1. (These are
> simply Boolean Truth values in Boolean Algebra; 0 represents the additive
> identity and 1 represents multiplicative identity...the fact that certain
> computer lanuages represent TRUE as 1 and FALSE as -1 has more to do with
> computer hardware than with the postulates of George Boole <G>)
I didn't know what you were talking about here....
I searched and ended up at
http://mathworld.wolfram.com/MultiplicativeIdentity.html....whooa!
Apparently we didn't do Algebraic Identities where I went to school!

> > I wasn't sure if you were talking specifically about hating the values
> > within the mainline code as in
> > IF RESPONSE = 'Y', or whether you meant the 88 level also.
> >
> Both, but I have less aversion to the 88 as you never really need to look
at
> it and its value is really unimportant; what is important is the STATE
that
> it represents.
I think I'm with you.

> (I've always considered it a little arrogant to expect foreign speakers to
> recognise YES and NO in program code (even though  they do...) especially
> when you are working in THEIR country and THEIR culture...it's more
courtesy
> than programming practice.)
I found it interesting recently to find out that some people learned some
english from coding.

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-21T17:58:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f6d3f16_2@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <3f6bc464_9@news.athenanews.com> <rzQab.13438$kg.7743@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:rzQab.13438$kg.7743@twister.tampabay.rr.com...
>
> > "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f6bc464_9@news.athenanews.com...
> > > "jce" <defaultuser@hotmail.com> wrote in message
<snip>
> > I wouldn't go so far as to say that I think ALL 88 levels should have a
> > numeric value (actually, for efficiency in the mainframe environment, I
> use
> > a non-numeric field even when the value IS numeric.... That's just habit
> > from working with mainframes over 20 years... I still do it on the PC.)

> A numeric comparison is not as efficient as a character one ?  Not that I
am
> about to change for the 1ns saving ;)
>

It is considerably more than 1ns, even on today's powerful processors. It
can represent the difference between doing an arithmetic conversion (so that
numeric compare instructions can be used) and doing a character compare
which requires no conversion (on the IBM mainframe in my day it  used CLI
(Compare Logical Immediate, where the instruction contains the character to
be compared against as one of its operands, and is therefore highly
efficient (no requirement for separate indexed addressing) but I don't know
what they use today...

Logic tells me that something which requires no conversion HAS to be better
than something that DOES (or even MIGHT) require conversion, so I continue
to use non-numeric fields.

> > When it comes to internal logic states I would prefer 0 and 1. (These
are
> > simply Boolean Truth values in Boolean Algebra; 0 represents the
additive
> > identity and 1 represents multiplicative identity...the fact that
certain
> > computer lanuages represent TRUE as 1 and FALSE as -1 has more to do
with
> > computer hardware than with the postulates of George Boole <G>)
> I didn't know what you were talking about here....
…[3 more quoted lines elided]…
>

Well, I was educated in New Zealand and we don't have much else to do except
learn stuff, play sport, and figure out more exciting ways to induce
tourists to kill themselves...<G>

You will have seen that additive and multiplicative identities are
prerequisites (along with some other features) for a number system  to
qualify as a Boolean Algebra. This just happens to be a particular area of
interest to me...actually I was hopeless at Maths when at school (much more
interested in devising ways to kill tourists...<G>) and had to teach myself
algebra, calculus, and trigonometry after I left. I have always been
fascinated by thought and systems of Logic, though.

> > > I wasn't sure if you were talking specifically about hating the values
> > > within the mainline code as in
> > > IF RESPONSE = 'Y', or whether you meant the 88 level also.
> > >
> > Both, but I have less aversion to the 88 as you never really need to
look
> at
> > it and its value is really unimportant; what is important is the STATE
…[4 more quoted lines elided]…
> > (I've always considered it a little arrogant to expect foreign speakers
to
> > recognise YES and NO in program code (even though  they do...)
especially
> > when you are working in THEIR country and THEIR culture...it's more
> courtesy
…[3 more quoted lines elided]…
>

Jeez,  hope not!!! <G>

Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-18T07:25:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BMScnYdcp6GyOfSiXTWJiQ@giganews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> Jerry,
>
…[15 more quoted lines elided]…
> (Some more comments below...)

One programming quirk that drives me nuts involves the concept above. In
debugging a program - or trying to understand it's logic flow - I used to
run into a mess of conditionals:

IF GOOD-TO-GO THEN...
  ELSE IF PAINTED-BLUE THEN ...
    ELSE IF BIGGER-THAN-A-BREADBOX THEN ...
      ELSE IF MARRIED-TO-COUSIN THEN ...

as I had at hand a particular value in a variable (say FURRY-ANIMAL =
"CAT"). This engendered all manner of searching to find out whether CAT was
the same as PAINTED-BLUE and so on.

After much therapy, I've confined my use of conditionals to barking-obvious
cases (IF END-OF-FILE THEN ...).

Works so well (for me), I never needed to go beyond the seventh step (in a
twelve-step program).
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 5)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-09-18T14:58:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0309181358.6640483f@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<BMScnYdcp6GyOfSiXTWJiQ@giganews.com>...

> Works so well (for me), I never needed to go beyond the seventh step (in a
> twelve-step program).

Surely there's *something* you needed to make amends for, even if it's
your excessive humility ... ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 5)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T08:30:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iGCab.11928$hF3.1305853@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:BMScnYdcp6GyOfSiXTWJiQ@giganews.com...
> Peter E.C. Dashwood wrote:
> > Jerry,
…[28 more quoted lines elided]…
> "CAT"). This engendered all manner of searching to find out whether CAT
was
> the same as PAINTED-BLUE and so on.
>
> After much therapy, I've confined my use of conditionals to
barking-obvious
> cases (IF END-OF-FILE THEN ...).


Agreed, 100%.  The problem with 88 levels is that you do not even know what
parameter is being tested, or even if the *same* parameter is being tested
in a list of tests. You really have no idea at all what the above statement
means ... it is like trusting the documentation notes instead of reading the
code.

There is a real good chance that "painted-blue" has been defined as a patch
by a programmer named "blue", while "furry-animal" is defined as a being
assigned to a disk area on a machine "furry". The idea that the 88 level
actually tells you what is going on is a pure fallacy.  You *never* know
what is going on until you look, and excessive use of 88 levels with SET
commands makes it extremely difficult to look.

Donald


Donald.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-19T17:41:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkff3r$k4b$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com>`

```

On 19-Sep-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:

> Agreed, 100%.  The problem with 88 levels is that you do not even know what
> parameter is being tested, or even if the *same* parameter is being tested
> in a list of tests. You really have no idea at all what the above statement
> means ... it is like trusting the documentation notes instead of reading the
> code.

My most common 88 level is with very standard switches:

      SELECT PRTFILE
          ASSIGN TO PRTFILE
          FILE STATUS IS PRTFILE-STATUS.
 =============================
  01  PRTFILE-STATUS          PIC X(02)   VALUE '00'.
      88 PRTFILE-STATUS-OK                VALUE '00' '97'.

 =============================
      SELECT CTRL-CARD-FILE   ASSIGN TO CTRLFL
          FILE STATUS IS CTRL-FILE-STATUS.
 =============================
  01  CTRL-FILE-STATUS        PIC X(02)   VALUE '00'.
      88 CTRL-FILE-STATUS-OK                VALUE '00' '10' '97'.
 ***    '10' IS OPENING AN ALREADY OPENED FILE
      88 CTRL-FILE-STATUS-AT-END          VALUE '10'.


Note the status code of '97' which means, the file opened OK, but the system had
to clean it up first.    This way it gets automatically checked as a good status
code.

A standard that requires all 88 levels to contain the name of the switch might
be a good house standard though.   The grep's of the world will find them.
Should it make them all start the same even though we might get:

88   SSN-RECORD-FOUND-YES        VALUE 'Y'.
88   SSN-RECORD-FOUND-NO          VALUE 'N'.
??????
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T14:43:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P7Iab.3460$mv6.632780@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <bkff3r$k4b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:bkff3r$k4b$1@peabody.colorado.edu...
>
> On 19-Sep-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
> > Agreed, 100%.  The problem with 88 levels is that you do not even know
what
> > parameter is being tested, or even if the *same* parameter is being
tested
> > in a list of tests. You really have no idea at all what the above
statement
> > means ... it is like trusting the documentation notes instead of reading
the
> > code.
>
…[19 more quoted lines elided]…
> Note the status code of '97' which means, the file opened OK, but the
system had
> to clean it up first.    This way it gets automatically checked as a good
status
> code.
>
> A standard that requires all 88 levels to contain the name of the switch
might
> be a good house standard though.   The grep's of the world will find them.
> Should it make them all start the same even though we might get:
…[3 more quoted lines elided]…
> ??????
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-19T14:46:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<taIab.3461$mv6.632898@news20.bellglobal.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <bkff3r$k4b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:bkff3r$k4b$1@peabody.colorado.edu...
>
> On 19-Sep-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
> > Agreed, 100%.  The problem with 88 levels is that you do not even know
what
> > parameter is being tested, or even if the *same* parameter is being
tested
> > in a list of tests. You really have no idea at all what the above
statement
> > means ... it is like trusting the documentation notes instead of reading
the
> > code.
>
…[8 more quoted lines elided]…
>

Tht has been the way I always used them too, and I never had problems.  The
problems seem to come up when people get into this "I have to define every
condition with an 88 because it is 'good style' mode".  Over use of anything
can bugger it up.



>  =============================
>       SELECT CTRL-CARD-FILE   ASSIGN TO CTRLFL
…[8 more quoted lines elided]…
> Note the status code of '97' which means, the file opened OK, but the
system had
> to clean it up first.    This way it gets automatically checked as a good
status
> code.
>
> A standard that requires all 88 levels to contain the name of the switch
might
> be a good house standard though.   The grep's of the world will find them.
> Should it make them all start the same even though we might get:
…[3 more quoted lines elided]…
> ??????

I am not sure if I'd go that far, but I would *definitely* make it a rule
that there must be a data name.  At least that way you can stick a display
in the code.

Donald
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-09-19T15:13:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0309191413.53a75b12@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message news:<iGCab.11928$hF3.1305853@news20.bellglobal.com>...
> "JerryMouse" <nospam@bisusa.com> wrote in message
> news:BMScnYdcp6GyOfSiXTWJiQ@giganews.com...
…[55 more quoted lines elided]…
> Donald.

I think you are barking up the wrong tree, it is not that 88 levels
are difficult to use well, but that many programmers have not learnt
to do so, or don't want to do so.

For example when I use 88 levels for checking file-status, I would use
something along the following lines:

01  WD-File-stati.
    03  WD-acct-file-status.
        05  filler                   pic x               value space.
            88  wd-acct-file-ok                          value '0'.
            88  wd-acct-file-eof                         value '1'.
        05  filler                   pic x               value space.
        88  wd-acct-file-sequence-error                  value '21'.
        88  wd-acct-file-duplicate-key                   value '22'.
        88  wd-acct-file-record-not-found                value '23'.

(Though I might be more inclined to use specific codes for file-ok,
such as '00', '07', '97', etc as appropriate, depending on the
environment and whether anything other than '00' would be acceptable
in the circumstances.)

A similar approach could be taken for sqlcode or preferably sqlstate,
now that its value have stabilised.

Setting items to true or false can also be useful for switches/flags,
when following a similar naming convention, it is quite clear what the
condition names refer to, for example:

01  WE-Switches.
    03  WE-error-sw                 pic x               value '0'.
        88  WE-error-not-found                          value '0'.
        88  WE-error-found                              value '1'.
    03  WE-fairground-item-type     pic xx.
        88  WE-merrygoround                             value '01'.
        88  WE-dodgems                                  value '02'.
        88  WE-helterskelter                            value '03'.

01  acct-record.
    03  acct-num                    pic x(10).
    03  acct-type                   pic xx.
        88  acct-current-ac                             value '01'.
        88  acct-deposit-ac                             value '02'.
    03  acct-balance                pic s9(9)v99       
packed-decimal.
    03  acct-status                 pic x.
        88  acct-open                                   value '1'.
        88  acct-suspended                              value '2'.
        88  acct-closed                                 value '3'.

I am sure you all can think of other and perhaps more appropriate ways
to achieve legibility and it is that which is important, rather than
how badly someone else managed to represent their logic.  After all
the same could be said for the whole of COBOL, or any other computer
language.

Robert
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-19T23:13:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309192213.25dfb603@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com>`

```
robert@jones0086.freeserve.co.uk (Robert Jones) wrote 

> > Agreed, 100%.  The problem with 88 levels is that you do not even know what
> > parameter is being tested, or even if the *same* parameter is being tested
> > in a list of tests. You really have no idea at all what the above statement
> > means ... it is like trusting the documentation notes instead of reading the
> > code.

> I think you are barking up the wrong tree, it is not that 88 levels
> are difficult to use well, but that many programmers have not learnt
> to do so, or don't want to do so.

This sounds like you equate "use well" with "how I do it", and "not
learnt to do so" with "not doing it _my_ way".

> For example when I use 88 levels for checking file-status, I would use
> something along the following lines:
…[9 more quoted lines elided]…
>         88  wd-acct-file-record-not-found                value '23'.

Do you really have a different file status for each file ?  Doesn't
this make it a real pain to have some common code that can be used to
deal with checking and reporting ?

After all you will be checking after each file action, it is not
likely that some other file action will accidentally get put between
one file action and its status check.
 
> (Though I might be more inclined to use specific codes for file-ok,
> such as '00', '07', '97', etc as appropriate, depending on the
> environment and whether anything other than '00' would be acceptable
> in the circumstances.)

How would you cater for additional '0x' codes that may be introduced
by a change in the compiler ?
 
> A similar approach could be taken for sqlcode or preferably sqlstate,
> now that its value have stabilised.

Would you use a separate sqlcode and sqlstate for each table ?

> Setting items to true or false can also be useful for switches/flags,
> when following a similar naming convention, it is quite clear what the
…[9 more quoted lines elided]…
>         88  WE-helterskelter                            value '03'.

In what way is it 'clear' that WE-merrygoround belongs to
WE-fairground-item-type and not to WE-error-sw to someone who has
never heard of a fairground and thinks that 'goround' might be a
looping error ?  More relevantly isn't 'WE-dodgems' a WE-baseball-team
and 'WE-helterskelter' a WE-casino-gambling-table ?

You are only assuming they are obvious because they seem so to _you_.

Everything that _you_ invent is 'obvious', but only to you. It may be
that it is easy for others to assimilate this and these then become
obvious to them, but only after they have learnt them.
 
> I am sure you all can think of other and perhaps more appropriate ways
> to achieve legibility and it is that which is important, rather than
> how badly someone else managed to represent their logic.  After all
> the same could be said for the whole of COBOL, or any other computer
> language.

The basic underlying problem with 88 levels is that they are aliases.
You may think that your alias names _must_ be obvious to everyone,
automatically. You may 'unalias' them by including the whole variable
name as part of the alias, but then this saves nothing over simply
using a comparison and having the remainder of the alias used as a
constant:

        IF ( WE-fairground-item-merrygoround )

vs:

        IF ( WE-fairground-item-type = merrygoround )
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-09-20T05:52:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0309200452.3ce4ccd4@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0309192213.25dfb603@posting.google.com>...
> robert@jones0086.freeserve.co.uk (Robert Jones) wrote 
> 
…[12 more quoted lines elided]…
> 

The last part of my post make it quite clear that other people may
think of other and more appropriate ways to achieve legibility.

> > For example when I use 88 levels for checking file-status, I would use
> > something along the following lines:
…[18 more quoted lines elided]…
>  

Yes, I most certainly do use different file statuses for each file,
that way I can check whether they are at end when doing matching logic
for example.  It also makes it easier to find out which files were
giving problems when trying to resolve a dump.  Code for checking
files is usually specific to each file for the particular requirements
of the logic, if the logic was all the same there wouldn't be any need
to have more than one file.

> > (Though I might be more inclined to use specific codes for file-ok,
> > such as '00', '07', '97', etc as appropriate, depending on the
…[5 more quoted lines elided]…
>  
This is made quite clear by the example.  However, it is
sometimes/often the case that the newly introduced extra valid file
status values are inapplicable to some types of file or use.

> > A similar approach could be taken for sqlcode or preferably sqlstate,
> > now that its value have stabilised.
> 
> Would you use a separate sqlcode and sqlstate for each table ?
> 
After doing the initial checking with the common field provided in the
SQLCA, I might well save them in separate fields so that the program
can use them to control subsequent logic and assist in debugging using
a common procedure to report the latest sqlcodes/sqlstates from each
accessed table.

> > Setting items to true or false can also be useful for switches/flags,
> > when following a similar naming convention, it is quite clear what the
…[22 more quoted lines elided]…
>
Yes you have a point about the fairground example, though arguably it
could be expected that most people likely to amend one of my programs
would know what a fairground is.
  
> > I am sure you all can think of other and perhaps more appropriate ways
> > to achieve legibility and it is that which is important, rather than
…[15 more quoted lines elided]…
>         IF ( WE-fairground-item-type = merrygoround )

Yes, "IF (WE-fairground-item-merrygoround) would be more explicit.

However, 88 levels also accomodate multiple values and thereby reduce
the size and number of explicit comparisons needed.  They also provide
inbuilt documentation regarding the meanings of the values assigned to
the dependent variable, while not requiring that the variable be large
enough to contain the full descriptive name, for example it is usually
more efficient to have a value of '1' for true rather than having to
have a variable of 5 bytes to accomodate the values "true" and
"false".
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-20T13:51:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309201251.77c25829@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <fcd09c56.0309200452.3ce4ccd4@posting.google.com>`

```
robert@jones0086.freeserve.co.uk (Robert Jones) wrote 

> The last part of my post make it quite clear that other people may
> think of other and more appropriate ways to achieve legibility.

But that is exactly the point.  Everyone invents their own form of
'readability' that is obvious to them, but not necessarily so to
others.
 
> Yes, I most certainly do use different file statuses for each file,
> that way I can check whether they are at end when doing matching logic

I almost always use high-values moved to the record key at end of
file.  This way I only have to check that both the match keys have
reached the same high-values and there is never a problem with
'overhang', or specifically having to check for it.

Using the file-status at some later time is also prone to error if,
for example, an unlock or a start has been introduced between where
the read was done and where the existence of the record needs to be
known.  It is OK for simple cases only.

> for example.  It also makes it easier to find out which files were
> giving problems when trying to resolve a dump.  

<shrug> Don't do dumps, don't have dumps.</shrug>

> Code for checking
> files is usually specific to each file for the particular requirements
> of the logic, 

Having one only file status area doesn't _prevent_ having code
specific to each file.  Having separate file statii does prevent
having common code.  Now it may be that you don't bother reporting or
dealing with anything out of the ordinary.  In a batch environment it
may be acceptable to 'abend' and study the entrails, but in an
interactive environment it is necessary to deal with the obscure, or
at least report it in a meaningful way, log it, and hopefully, get the
user to deal with it.

> if the logic was all the same there wouldn't be any need
> to have more than one file.

No. You'll have to explain that one.
 
> This is made quite clear by the example.  However, it is
> sometimes/often the case that the newly introduced extra valid file
> status values are inapplicable to some types of file or use.

Hmmm, that seems to be an answer that you would go through each
program and each and every file and change code as required, or not.
 
> Yes you have a point about the fairground example, though arguably it
> could be expected that most people likely to amend one of my programs
> would know what a fairground is.

And if the maintenance was outsourced to India ?
   
> However, 88 levels also accomodate multiple values and thereby reduce
> the size and number of explicit comparisons needed.  

They don't actually reduce the amount of machine code.

Also I dislike 88 levels used in EVALUATEs.  In any case it is easy to
set up a 'grouping' field if there are always values that are always
treated the same.

       03  WE-fairground-type         ...
     
       03  WE-fairground-group        ..

       EVALUATE WE-fairground-type
       WHEN WE-merrygoround
       WHEN WE-spinning-tops
       WHEN WE-rotating-discs
            MOVE WE-ground-round    TO WE-fairground-group
       ...

In fact I usually do this with a simple table that the _user_ is
responsible for indicating the group for each type.  Having multiple
values in an 88 level usually indicates that too much 'business logic'
is buried in the code and not enough is under user control.

> They also provide
> inbuilt documentation regarding the meanings of the values assigned to
> the dependent variable, 

So do constants, in exactly the same way, but without the aliasing
problem.

> while not requiring that the variable be large
> enough to contain the full descriptive name, 

Leading directly to the aliasing problem.

> for example it is usually
> more efficient to have a value of '1' for true rather than having to
> have a variable of 5 bytes to accomodate the values "true" and
> "false".

Exactly as for constants.

It is simply a matter of style, and thus choice.

Most of my systems have a simple 'decode' file where many different
types of codes are stored.  The key is 'field name' + 'code' and there
is a control file that holds the screen layouts for each 'field name'
for maintaining it.

In most cases the code is 'valid' if it exists in the appropriate
field name section of the decode file.  Grouping, validity, and
processing options are determined from values held there, and not in
some set of 88 levels.

This makes a huge difference to the amount of program mainteneance
required.  If a new 'fairground-type' is introduced _I_ don't have to
change the programs to deal with a new value in the 88 levels, or even
in the IF or EVALUATE statements.  The new code is added to the decode
file by the user and as long as it fits in one of the existing groups
(also must exist in the decode file) then it just works.

The 'field name' is also used in file maintenance (one program does
all files) and reporting (one program does most) to check that codes
are valid, to display description of entered code and to provide a
selection list.

Once in place this mechanism is trivial to extend.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-22T16:40:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkn8la$g4r$2@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com>`

```

On 20-Sep-2003, riplin@Azonic.co.nz (Richard) wrote:

> Do you really have a different file status for each file ?  Doesn't
> this make it a real pain to have some common code that can be used to
> deal with checking and reporting ?

I have found bugs in programs caused by sharing switch names and index names.  
It is easy enough to cut and paste and make them all unique, and less likely to
have an error.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-22T16:59:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wTFbb.53210$Aq2.23339@newsread1.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <bkn8la$g4r$2@peabody.colorado.edu>`

```
I often use "compound" OPEN statements and if you had a SINGLE file status
field, this would not work, e.g.

 Open Input File-1 File-2
          Output File-3
         ....

If you use multiple file status fields but want SOME common logic, you can
use a DECLARATIVE for the "common" processing.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-22T16:07:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309221507.61523d73@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <bkn8la$g4r$2@peabody.colorado.edu> <wTFbb.53210$Aq2.23339@newsread1.news.atl.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote 

> I often use "compound" OPEN statements and if you had a SINGLE file status
> field, this would not work, e.g.
…[3 more quoted lines elided]…
>          ....

Saving a whole 15 characters of source code. 

I would never do this.  I just can't see the point of leaving out a
couple of words.

There is also a danger in that you may not want to have the output
file created if the input file is unavailable.  If the run time will
abend on a missing input will it do so before or after the output file
is created ? Or will the open return with a status for the programmer
to deal with, in which case the output will have been created.
 
> If you use multiple file status fields but want SOME common logic, you can
> use a DECLARATIVE for the "common" processing.

I don't like DECLARATIVEs.  I did use them for a while 25 years ago
when they seemed a really neat idea, but eventually realised they were
a solution to a problem that never actually existed (for me).

It seems that DECLARATIVEs _may_ be useful for retro-fitting onto
mainframe programs where the programmer never bothered with status
checking because 'it will just abend anyway'.

With explicit checking (which I always do) I can do the checks as
required by the logic and then any other fail status can be dumped
into a 'fail' routine.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T15:14:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkscck$6gq$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <bkn8la$g4r$2@peabody.colorado.edu> <wTFbb.53210$Aq2.23339@newsread1.news.atl.earthlink.net> <217e491a.0309221507.61523d73@posting.google.com>`

```

On 22-Sep-2003, riplin@Azonic.co.nz (Richard) wrote:

> > I often use "compound" OPEN statements and if you had a SINGLE file status
> > field, this would not work, e.g.
…[8 more quoted lines elided]…
> couple of words.

Or a couple of keystrokes as I copy one line and change it.   There is really no
downside in having separate OPEN or CLOSE statements, and I can add debug lines,
status checking, & conditional logic between the OPEN's.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T15:15:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksce6$6k3$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <bkn8la$g4r$2@peabody.colorado.edu> <wTFbb.53210$Aq2.23339@newsread1.news.atl.earthlink.net> <217e491a.0309221507.61523d73@posting.google.com>`

```

On 22-Sep-2003, riplin@Azonic.co.nz (Richard) wrote:

> I don't like DECLARATIVEs.  I did use them for a while 25 years ago
> when they seemed a really neat idea, but eventually realised they were
> a solution to a problem that never actually existed (for me).

Same with me.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-22T15:48:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309221448.74297ecf@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com> <bkn8la$g4r$2@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> > Do you really have a different file status for each file ?  Doesn't
> > this make it a real pain to have some common code that can be used to
…[4 more quoted lines elided]…
> have an error.

The File Status variable makes a very poor 'switch', which was the
gist of my message.

The problem with using File Status as a switch is that it is changed
by _any_ action on the file, even by CLOSE and UNLOCK.  So 'bugs' can
be caused by using it as a switch regardless of whether it is shared
or not.

It is _always_ prefererable to use a distinct and explicit switch (or
some other mechanism, such as setting the key to high-values at end of
file) and then sharing the File Statii becomes a benefit rather than a
bugfest.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-22T16:40:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkn8le$g4r$3@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <iGCab.11928$hF3.1305853@news20.bellglobal.com> <fcd09c56.0309191413.53a75b12@posting.google.com> <217e491a.0309192213.25dfb603@posting.google.com>`

```

On 20-Sep-2003, riplin@Azonic.co.nz (Richard) wrote:

> The basic underlying problem with 88 levels is that they are aliases.
> You may think that your alias names _must_ be obvious to everyone,
…[3 more quoted lines elided]…
> constant:

Agreed, that is the basic problem with them.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-21T18:12:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f6d4254_3@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:BMScnYdcp6GyOfSiXTWJiQ@giganews.com...
> Peter E.C. Dashwood wrote:
> > Jerry,
…[28 more quoted lines elided]…
> "CAT"). This engendered all manner of searching to find out whether CAT
was
> the same as PAINTED-BLUE and so on.
>

I sympathize, Jerry. And if you have something that works for you I would
agree there is little need to change it.

But surely it isn't TOO hard to say:

if cat AND painted-blue ...

There isn't "all manner of searching" required, PROVIDED you use meaningful
condition names to represent the various states.

CAT and PAINTED-BLUE CANNOT be the same because they represent different
states of two different variables.

I think your "problem" (and I agree it isn't, because you are happy with how
you do things) stems from failure to recognise the difference between a
STATE and a VARIABLE.

A CAT is one state of the variable FURRY-ANIMAL. PAINTED-BLUE is one state
of the variable WHAT-COLOR.

It is only when you start setting a variable called "PAINTED-BLUE" to "Y"
(or "1" or whatever...) that confusion can arise...


> After much therapy, I've confined my use of conditionals to
barking-obvious
> cases (IF END-OF-FILE THEN ...).
>

Ah, had I been your therapist, a different outcome may have eventuated...<G>

(Notice that the cases where you DO accept a conditional (the
"barking-obvious" ones) are all cases where it is the STATE that is
barkingly obvious!)

> Works so well (for me), I never needed to go beyond the seventh step (in a
> twelve-step program).
>

That's really what it is all about...

Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-21T12:33:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309211133.6e3b8459@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote 

> if cat AND painted-blue ...
> 
…[4 more quoted lines elided]…
> states of two different variables.

Not at all. They could be the same variable with 'painted-blue' a
subset of 'cat'.

    01  Animal-Coloured    ..
        88 Cat value 1 thru 6.
         88 painted-blue value 2.
         88 siamese-brown value 3.
         88 burmese-black value 4
            ...

        if cat
            if painted-blue 
                .....

'optimised' to:
         if cat and painted-blue

Obviously it could be resolved 'if painted-blue' if one _knew_ it was
a subset, but it is necessary to _know_ this first by 'all manner of
searching'.

Your assumption that they _cannot_ be the same variable is a result of
not having done the searching for the aliases (and not knowing that
'painted' is a type of cat which I thought _everyone_ knew).









(PS it isn't, but did you actually know that).
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-23T04:12:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4LPbb.3363$eS5.381@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309211133.6e3b8459@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > if cat AND painted-blue ...
> >
> > There isn't "all manner of searching" required, PROVIDED you use
meaningful
> > condition names to represent the various states.
> >
…[27 more quoted lines elided]…
> (PS it isn't, but did you actually know that).

A better example:
01 ANIMAL-COLOURED.
         88 Horse value 1 thru 3.
          88 painted value 1.
          88 white    value 2.
          88 black    value 3


Your assumption that they _cannot_ be the same variable is a result of
not having done the searching for the aliases (and not knowing that
'painted' is a horse colour which I thought _everyone_ knew).









(PS it is - look up the word pinto :-)).

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T15:17:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksci3$70b$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <4LPbb.3363$eS5.381@twister.tampabay.rr.com>`

```

On 22-Sep-2003, "jce" <defaultuser@hotmail.com> wrote:

> A better example:
> 01 ANIMAL-COLOURED.
…[8 more quoted lines elided]…
> 'painted' is a horse colour which I thought _everyone_ knew).

A rigidly enforced standard which included:
        88  ANIMAL-COLORED-HORSE
        88  ANIMAL-COLORED-PAINTED

etc. can solve the alias problem.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-24T09:42:35+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f70db7f_4@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309211133.6e3b8459@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > if cat AND painted-blue ...
> >
> > There isn't "all manner of searching" required, PROVIDED you use
meaningful
> > condition names to represent the various states.
> >
…[5 more quoted lines elided]…
>

They COULD be but they are NOT. They are NOT because I wouldn't code them in
the way you describe.

I wouldn't do it becuase it is not my STYLE.

Therefore the whole discussion comes down to STYLE, as I said many posts
back...

Pete.


<snipped example of style I would not use <G> >
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-24T00:47:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309232347.2811c0f5@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote 

> > Not at all. They could be the same variable with 'painted-blue' a
> > subset of 'cat'.
> 
> They COULD be but they are NOT. They are NOT because I wouldn't code them in
> the way you describe.

But it wasn't you that was coding:

PECD> I sympathize, Jerry. And if you have something that works for
_YOU_ ..
      
PECD> There isn't "all manner of searching" required, provided _YOU_
use
PECD> meaningful condition names to represent the various states.

(emphasis of 'you' added).

The point being that it is not possible to make assumptions about what
someone else thinks is 'meaningful'.  Or indeed, just because you
think that what you wrote is obvious and 'meaningful', does not mean
that someone else will see the same meaning.

Also, of course, it isn't until _after_ I have done "all manner of
searching" that _I_ can be assured that you did, in fact, write it
with the same meaning that I assumed.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-24T16:24:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksuht$104u$1@news.btv.ibm.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com>`

```
Yes, but I think you need to define some level of common sense.

It is acceptable for someone to code

01  IS-NOT-OPEN.
       88 FALSE           VALUE '1'.
       88 TRUE             VALUE '0'.

But that would be contrary to common sense, history and be basically stupid.
(The above would be typical of American standardized tests where they do not
think that all not stupid
people wouldn't get confused by multiple negatives)

Anyway, one could come up with variable names that make no sense....

IF TOO-MANY-COOKS THEN
    SET BROTH-RUINED
END-IF

By  TOO-MANY-COOKS I mean...someone changed the data that I was using since
I read it...by BROTH-RUINED I mean that I need to go rollback to my check
point.

The bottom line is that if the code doesn't make sense to the next person in
line, and that person is of reasonable intelligence, then the code wasn't
perfectly written...even if that reason is "style".
IMHO, 88 level items don't deserve any special criticism.

JCE

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309232347.2811c0f5@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
…[3 more quoted lines elided]…
> > They COULD be but they are NOT. They are NOT because I wouldn't code
them in
> > the way you describe.
>
…[18 more quoted lines elided]…
> with the same meaning that I assumed.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-26T19:24:01+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f7406ca_5@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309232347.2811c0f5@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
…[3 more quoted lines elided]…
> > They COULD be but they are NOT. They are NOT because I wouldn't code
them in
> > the way you describe.
>
…[18 more quoted lines elided]…
> with the same meaning that I assumed.

As the rules are simple, there is no need to "assume" anything. I simply
don't use DATANAMEs to represent states; instead I use 88 levels (that is
why they are called "CONDITION names"...my emphasis).

If you don't need to assume, you don't need to check the assumption, hence,
no need for "all manner of searching"...

I do take your point about the dangers of assuming what is meaningful to
others. This conversation is a perfect case in point...

I assumed that as it was in simple English, the tenets would be grasped.

I was wrong.

Pete.

I take your point about
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-26T13:24:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309261224.3fc31e37@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> > Also, of course, it isn't until _after_ I have done "all manner of
> > searching" that _I_ can be assured that you did, in fact, write it
> > with the same meaning that I assumed.

> As the rules are simple, there is no need to "assume" anything. 

When inspecting someones else's program I would either have to assume
that you (or whoever) had followed this set of simple rules, or assure
myself that this is actually the case by doing 'all manner of
searching'.

Without having been inside your head when you wrote it how else would
I know what set of rules, if any, you had followed ?

> I simply
> don't use DATANAMEs to represent states; instead I use 88 levels (that is
> why they are called "CONDITION names"...my emphasis).

But how do I actually _KNOW_ that without doing 'all manner of
searching' that you told me wasn't required ?  Does a message box pop
up in my editor and say: "This was written by a sensible programmer -
all your assumptions are guaranteed to be true". ?

> If you don't need to assume, you don't need to check the assumption, hence,
> no need for "all manner of searching"...

You may not need to 'assume', but then you wrote it.

"In God we trust, everyone else pays cash."

> I assumed that as it was in simple English, the tenets would be grasped.
> 
> I was wrong.

I fully understand what you are saying, I just disagree with it.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 11)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-26T22:18:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aX2db.12305$Of2.775050@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309261224.3fc31e37@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > > Also, of course, it isn't until _after_ I have done "all manner of
> > > searching" that _I_ can be assured that you did, in fact, write it
> > > with the same meaning that I assumed.
How many manners of searching are there ?

> > As the rules are simple, there is no need to "assume" anything.
> When inspecting someones else's program I would either have to assume
> that you (or whoever) had followed this set of simple rules, or assure
> myself that this is actually the case by doing 'all manner of
> searching'.
It *should* be safe to assume that a CONDITION has in it something that
expresses a CONDITION.
One may need to find out what that condition it by searching if there is not
an obvious condition in the surrounding context
but that is true of LABELS, Variables, conditions.....I've seen labels
called LOG-OUTPUT for example, that log the output and updates a record.

> Without having been inside your head when you wrote it how else would
> I know what set of rules, if any, you had followed ?
> > I simply
> > don't use DATANAMEs to represent states; instead I use 88 levels (that
is
> > why they are called "CONDITION names"...my emphasis).
> But how do I actually _KNOW_ that without doing 'all manner of
> searching' that you told me wasn't required ?  Does a message box pop
> up in my editor and say: "This was written by a sensible programmer -
> all your assumptions are guaranteed to be true". ?
I will add that to my prologs :-)

> > If you don't need to assume, you don't need to check the assumption,
hence,
> > no need for "all manner of searching"...
> You may not need to 'assume', but then you wrote it.

If we have simple states:
IS-OPEN, IS-CLOSED, IS-HUMAN, IS-FILTERED then it is obvious what those
states are.
There are usually contextual clues a check for IS-HUMAN may come in a
paragraph called - check-species, or animal-group-process.

> > I assumed that as it was in simple English, the tenets would be grasped.
> > I was wrong.
> I fully understand what you are saying, I just disagree with it.
I'm with Pete.

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-27T22:44:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309272144.46adced0@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote

> It *should* be safe to assume that a CONDITION has in it something that
> expresses a CONDITION.
> One may need to find out what that condition it by searching if there is not
> an obvious condition in the surrounding context

Exactly.  The point at contension is that one programmer is certain
that what they write is so clear and meaningful and obvious that no
one ever need check what the condition is about, and this may be true.
 From experience I know that others may write confusing and
non-obvious conditions which only appear to clear and meaningful (but
aren't).

There is no way to tell which of these I am looking at without
initially treating the code as being in the second category.

Even if I am told that it is in the first category then there is no
guarantee that I will draw the same conclusions as the programmer in
respect of the names used because they may represent culture,
knowledge or experiances that differ from mine.  Granted PECD and
myself probably differ very little.

> but that is true of LABELS, Variables, conditions.....I've seen labels
> called LOG-OUTPUT for example, that log the output and updates a record.

Exactly.
 
> If we have simple states:
> IS-OPEN, IS-CLOSED, 

Which file is this referring to, or is it a file ?  If it is a switch
then Is-Open is off and Is-Closed is on (as in electrical switch).  If
it is a door then Is-Open is allowing passage and Is-Closed is
preventing it.

> IS-HUMAN, IS-FILTERED then it is obvious what those
> states are.

Does Is-Filtered refer to a type of cigarette ?  Or is data where the
'filter' has removed unwanted items already.  Does Is-Filtered refer
to the items that are removed (filtered out) or the items that are
left after filtering ?

Why do you think these are 'obvious', is it because you can only think
of one meaning or association for them ?
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 13)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-28T16:23:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wWDdb.14524$Of2.1089126@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309272144.46adced0@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
>
> > It *should* be safe to assume that a CONDITION has in it something that
> > expresses a CONDITION.
> > One may need to find out what that condition it by searching if there is
not
> > an obvious condition in the surrounding context
>
…[8 more quoted lines elided]…
> initially treating the code as being in the second category.

Yes and if I have a variable called EMPLOYEE-NAME it might actually contain
the salary.
Yes and if I have a variable called EMPLOYEE-SALARY it might actually
contain the employee name.
The joke's on you if you don't search.

> Even if I am told that it is in the first category then there is no
> guarantee that I will draw the same conclusions as the programmer in
…[15 more quoted lines elided]…
> preventing it.
Usually the code would be something like ...
IF IS-CLOSED
    PERFORM OPEN-FILE (DOOR/SWITCH)

You should be able to figure out which......for the Switch it would probably
be
IF SWITCH-OFF
    PERFORM SWITCH-ON

because that makes more sense (to me)

> > IS-HUMAN, IS-FILTERED then it is obvious what those
> > states are.
…[7 more quoted lines elided]…
> of one meaning or association for them ?

You copy 90% of my text and remove the following - why did you do that? Is
it because it refutes what you say?

"There are usually contextual clues a check for IS-HUMAN may come in a
paragraph called - check-species, or animal-group-process."

I agree with you:  You cannot look at an IF statement and know what it is
with certainty.

I'm pretty certain you can look at a paragraph and know whether you are
dealing with an electrical switch or a file.....
I'm pretty certain you can look at a paragraph and know whether you are
dealing with a record filter or a cigarette filter.....
In fact I'm more certain if you have an idea what the program is doing at
all...you can probably rule out cigarette filters if you aren't working for
RJR.

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-28T15:39:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309281439.1ef83909@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote

> Yes and if I have a variable called EMPLOYEE-NAME it might actually contain
> the salary.
> Yes and if I have a variable called EMPLOYEE-SALARY it might actually
> contain the employee name.
> The joke's on you if you don't search.

Well of course in trivial cases it may be much more likely that the
meaning is 'obvious' to many more people.

> > > If we have simple states:
> > > IS-OPEN, IS-CLOSED,

> IF IS-CLOSED
>     PERFORM OPEN-FILE (DOOR/SWITCH)

Perhaps you missed the point here: Opening a 'switch' and opening a
'door' have opposite effects.  How do I know which analogue you are
using ?
 
> because that makes more sense (to me)

But does it make more sense to _ME_ ?

> You copy 90% of my text and remove the following - why did you do that? Is
> it because it refutes what you say?

No, it is because I had no issue with that particular item.  It
doesn't refute what I say, or what you say.

It may well be that in any program there is 90% of it where I can make
assumptions, and 10% that I identify as needing 'all manner of
searching' to determine the actual meaning.  The hard part is knowing
where in the 90% I have made a wrong assumption.
 
> I'm pretty certain you can look at a paragraph and know whether you are
> dealing with an electrical switch or a file.....
…[4 more quoted lines elided]…
> RJR.

Those may well be in the 90%, yes.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 15)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-29T01:30:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com>`

```


"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309281439.1ef83909@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
>
…[8 more quoted lines elided]…
> using ?
Once again...you copy 90% my text and remove something...

"You should be able to figure out which......for the Switch it would
probably be
IF SWITCH-OFF
    PERFORM SWITCH-ON
because that makes more sense (to me)"

I think that this statement would be fairly obvious to any westerner with an
electrical switch in their house.
To the 80% of the world that doesn't - it may not.

> > because that makes more sense (to me)
> But does it make more sense to _ME_ ?
It does describe the "analogue" does it not? Of course you'd have to go back
a post to find that out because you did conveniently cut
out the aforementioned paragraph.

I think that I can agree to disagree here.

I trust people to use common sense.
You trust people to use common sense 90% of the time.
Basically - I don't have an issue with 88 levels, and you do, yet I am yet
to see a great alternative that solves all the "problems"
of bad naming conventions and the like.

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-28T23:16:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309282216.43a581c1@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote 

> > > > > If we have simple states:
> > > > > IS-OPEN, IS-CLOSED,
…[6 more quoted lines elided]…
> > using ?

> Once again...you copy 90% my text and remove something...

> "You should be able to figure out which......for the Switch it would
> probably be
> IF SWITCH-OFF
>     PERFORM SWITCH-ON
> because that makes more sense (to me)"

I removed it because I was dealing with OPEN/CLOSE and you want to
change to ON/OFF.  Just deal with OPEN/CLOSE.  The issue I was
attempting to lead to to was: Does 'open' mean 'on' or 'off' ?  You
never actually addressed this, simply changing to using ON/OFF.

> I think that this statement would be fairly obvious to any westerner with an
> electrical switch in their house.

Is open/closed obvious to any westerner in connection with an
electrical switch ?

Are electrical switches on when they are up or when they are down ?

> I trust people to use common sense.
> You trust people to use common sense 90% of the time.

Once again you completely miss the point.  What is 'common' to you may
not be to many others.

   Electrical switches are on when they are down.

   The '1st floor' is one level up from the ground.

   Being 'tabled' means brought out and discussed.

   A gallon of water weighs 10 pounds.

   Drive on the left, give way to the right.

Are these 'common' to you ?  To some they are, to others they are not.
 In some cultures shaking the head from side to side means agreement.

I trust people to use _their_ common sense.  I actually understand
that this is only _mostly_ the same as _my_ common sense for reasons
of culture, education, environment, experience.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 17)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-29T11:40:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309282216.43a581c1@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
>
…[21 more quoted lines elided]…
> never actually addressed this, simply changing to using ON/OFF.
Yes, but the issue is moot because I was saying that I would use ON / OFF
and not OPEN / CLOSE.
I addressed the issue up front by changing the name of the state.

> > I think that this statement would be fairly obvious to any westerner
with an
> > electrical switch in their house.
>
…[3 more quoted lines elided]…
> Are electrical switches on when they are up or when they are down ?
Why does this matter? I don't recall suggesting SWITCH-UP or SWITCH-DOWN...
because in a multi switch environment a switch could be both on and off when
up or down.
I already addressed the open / closed in the prior post.

> > I trust people to use common sense.
> > You trust people to use common sense 90% of the time.
…[15 more quoted lines elided]…
>  In some cultures shaking the head from side to side means agreement.
Once again you miss my point.   What makes this unique to 88 levels?
The issue you describe is to bad naming conventions in general.  Or more
specifically your issue is that people could use a naming convention that
isn't immediately obvious to _eveyone_.
What sets 88 levels apart in this regard?

> I trust people to use _their_ common sense.  I actually understand
> that this is only _mostly_ the same as _my_ common sense for reasons
> of culture, education, environment, experience.
Then I'm not sure that we even disagree.

DB2 has COALESCE keyword, MQ Series / CICS has QUIESCE...half the people I
know don't know what those words mean - and I'm not sure that COALESCE even
means what it does!

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-29T15:41:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309291441.28542e04@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote 

> > > > > > > If we have simple states:
> > > > > > > IS-OPEN, IS-CLOSED,
>  
> > > > > IF IS-CLOSED
> > > > >     PERFORM OPEN-FILE (DOOR/SWITCH)

> > I removed it because I was dealing with OPEN/CLOSE and you want to
> > change to ON/OFF.  Just deal with OPEN/CLOSE.  

> Yes, but the issue is moot because I was saying that I would use ON / OFF
> and not OPEN / CLOSE.
> I addressed the issue up front by changing the name of the state.

Well exactly.  I point out an issue and you just try to wave hands and
claim that while what you did was not 'common sense', you wouldn't
really do that, and change it to something else.
 
> > Are electrical switches on when they are up or when they are down ?
> Why does this matter? 

Because it represents a cultural difference where 'common sense' is
not actually 'common' to everyone.  Perhaps you don't actually know
that some countries have a 'standard' that light and socket switches
are on when they are down, and others that they are off when they are
down.

You claimed to use 'common sense' when naming things and thus have
100% perfection (after hand waving and changing to avoid the issues)
in being understood.  My claim allows for things to be different
between the writer and the reader.

> I don't recall suggesting SWITCH-UP or SWITCH-DOWN...
> because in a multi switch environment a switch could be both on and off when
> up or down.

"Both on and off"  that is a clever trick for a switch.

> Once again you miss my point.   What makes this unique to 88 levels?

Where did I ever say that it was 'unique to 88 levels" ?

What it is about 88 levels is that they are 'aliases' for something. 
That is several items wind up with several names that refer to them. 
You seem to think that the relationship between the aliases and the
base item is made 'obvious' because of your 'common sense'.  I am
pointing out that there is less 'common'ality between people of
different backgrounds, cultures, and experiences than you imagine.

> The issue you describe is to bad naming conventions in general.  

No, not 'bad', just different.  You only think of it as 'bad' because
it is not what you would think of.

> Or more
> specifically your issue is that people could use a naming convention that
> isn't immediately obvious to _eveyone_.

People do use naming that isn't immediately obvious to _everyone_,
including me and including _you_.  You just don't seem to notice this
yet.

> What sets 88 levels apart in this regard?

Nothing at all, except that each one has several aliases.  It is the
relationship between the alias and the base that may get missed or
attributed wrongly.

The argument started when PECD claimed that 'cat' and 'painted-blue'
could not possibly be conditions of the same variable and there was no
need to check.

Even when your 'Is-Open' refers to a file and the state is not an
issue, it is only by inspection that we can determine which file it
refers to.

> > I trust people to use _their_ common sense.  I actually understand
> > that this is only _mostly_ the same as _my_ common sense for reasons
> > of culture, education, environment, experience.

> Then I'm not sure that we even disagree.

It may be a cultural difference, but I would have put 'even' as the
qualifier of 'sure' rather than of 'disagree'.   ;-)

> DB2 has COALESCE keyword, MQ Series / CICS has QUIESCE...half the people I
> know don't know what those words mean - and I'm not sure that COALESCE even
> means what it does!

They may well be more familiar with the adjective of these verbs
though: coalition and quiescent, or perhaps not.

"""COALESCE(expr, expr2 {, expr })   

COALESCE returns the first argument that is not NULL. The arguments
are evaluated in the order in which they are specified. This function
is usually used to replace NULL values with a not NULL value."""

This is certainly different to arriving at a coalition, so much for
'commonality' between that team and my education.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 19)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-30T01:39:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K95eb.32427$eS5.30160@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com>`

```
Last post - though I have enjoyed this :-)

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309291441.28542e04@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
>
…[9 more quoted lines elided]…
> > Yes, but the issue is moot because I was saying that I would use ON /
OFF
> > and not OPEN / CLOSE.
> > I addressed the issue up front by changing the name of the state.
…[3 more quoted lines elided]…
> really do that, and change it to something else.
Touche.

> > > Are electrical switches on when they are up or when they are down ?
> > Why does this matter?
…[12 more quoted lines elided]…
> > because in a multi switch environment a switch could be both on and off
when
> > up or down.
>
> "Both on and off"  that is a clever trick for a switch.
Well not at the same time, unless of course the bulb is out in which case it
is on and off :-)


> > Once again you miss my point.   What makes this unique to 88 levels?
> Where did I ever say that it was 'unique to 88 levels" ?
That was the point of the thread way back when....

> What it is about 88 levels is that they are 'aliases' for something.
> That is several items wind up with several names that refer to them.
…[3 more quoted lines elided]…
> different backgrounds, cultures, and experiences than you imagine.
Understood.

> > The issue you describe is to bad naming conventions in general.
> No, not 'bad', just different.  You only think of it as 'bad' because
> it is not what you would think of.
Understood.

> > Or more
> > specifically your issue is that people could use a naming convention
that
> > isn't immediately obvious to _everyone_.
>
> People do use naming that isn't immediately obvious to _everyone_,
> including me and including _you_.  You just don't seem to notice this
> yet.
I have yet to struggle with different names. I have yet to struggle with
alias problems....
I have already struggled with bad (not different) code :-)
This probably isn't an issue that warranted this much chit chat :-)

> > What sets 88 levels apart in this regard?
>
…[6 more quoted lines elided]…
> need to check.
I still agree with him.  That to me is still bad (not different) code.
The state "painted-blue" and "cat" should be treated as separate states - as
he pointed out this could have been resolved by changing IF CAT ...IF
PAINTED to IF CAT AND PAINTED

> Even when your 'Is-Open' refers to a file and the state is not an
> issue, it is only by inspection that we can determine which file it
> refers to.
True - I usually actually have FILE-<NAME>-IS-OPEN.

> > > I trust people to use _their_ common sense.  I actually understand
> > > that this is only _mostly_ the same as _my_ common sense for reasons
…[4 more quoted lines elided]…
> qualifier of 'sure' rather than of 'disagree'.   ;-)
Not an issue of culture, more an issue of the english education system.

> > DB2 has COALESCE keyword, MQ Series / CICS has QUIESCE...half the people
I
> > know don't know what those words mean - and I'm not sure that COALESCE
even
> > means what it does!
>
…[10 more quoted lines elided]…
> 'commonality' between that team and my education.

I agree with you in concept but not in practice.

Again, thanks for your input.  I have become a little more "diversified".
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-30T14:11:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309301311.1b757772@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <K95eb.32427$eS5.30160@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote 

> > The argument started when PECD claimed that 'cat' and 'painted-blue'
> > could not possibly be conditions of the same variable and there was no
> > need to check.

> I still agree with him.  That to me is still bad (not different) code.

It is only 'bad' if you have made some 'common sense' assumptions
based on how _you_ might arrive at those names and your assumptions
turned out to be wrong.

> The state "painted-blue" and "cat" should be treated as separate states 

How did you arrive at that conclusion ?  Why can't one be a subset of
the other ? How do you _KNOW_ that 'Painted-Blue' is not a type of
'Cat' ?  Are you an expert in the feline industry ?  Do you keep up
with all developments in breeding ?

With any code the names may be Jargon that only appears to be common
names.

There is _always_ a 'need to check'.

> - as
> he pointed out this could have been resolved by changing IF CAT ...IF
> PAINTED to IF CAT AND PAINTED

That does not resolve _anything_, it is a trivial syntax change that
implies nothing about the conditions that is not implied by the
original.

It is possible that they can both be true, this does not mean they are
different variables.  It may be that the original was a structured set
of IFs and later a naieve programmer 'optimised' it as you have done.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 19)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-30T20:45:31+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f795fea_4@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309291441.28542e04@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
<snip>
>
> The argument started when PECD claimed that 'cat' and 'painted-blue'
> could not possibly be conditions of the same variable and there was no
> need to check.
>

yes, here's the quote:

> >
> > CAT and PAINTED-BLUE CANNOT be the same because they represent different
> > states of two different variables.
>
My objection to this was that they are BOTH conditions, NOT Datanames. (It
becomes more obvious if we change "CAT" to "ITS-A-CAT".)

If they represented states of the same variable (which they don't) the
object could only be EITHER a cat, OR painted blue.

It could NOT represent a blue cat because only one state is possible per
variable. Either "ITS-A-CAT " or it's "PAINTED-BLUE".

In order to have a blue cat it is necessary to have TWO variables so that
you can represent BOTH states.

That was the nub of my argument. I also mentioned in passing that
personally, as a matter of style, I use condition names to represent states
(conditions) as I believe that is what they are intended for. Only when this
simple convention is ignored and a dataname is selected as the basis for a
state (which is how the whole discussion got started) is confusion over 88
levels likely to arise.

Richard, I take your point regarding familiarity based on culture, and the
fact that what is familiar to us seems good to us.

But there also has to be some basic degree of reason and commonality of
experience, as JCE has argued.

I think the question is where one draws this line. You draw it higher than
many of us; that doesn't mean you are wrong, it just means you are
stricter...

Ironically, a blue cat would be so far beyond the commonality of experience
that it is unlikely ANY programmer would have trouble recognising that it
must represent the state of TWO variables (Colour and Species).

So, the programmer from Dilworthia who codes a single variable with states
of "blue-cat", "green-horse" and "purple-human" (conditions only known to
himself) is simply living in a different reality...<G>

And that's where he belongs...

Because SOME people "misuse" 88 levels, it does not follow that condition
names in COBOL are of no use, and should be avoided.

Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-30T12:35:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309301135.6d9445a4@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> > > CAT and PAINTED-BLUE CANNOT be the same because they represent different
> > > states of two different variables.
…[8 more quoted lines elided]…
> variable. Either "ITS-A-CAT " or it's "PAINTED-BLUE".

     01  PIC X.
         88  Its-a-Cat          VALUE "A" THRU "E".
         88  Siamese-Blue       VALUE "A".
         88  Painted-Black      VALUE "B".
         88  Painted-Blue       VALUE "C".
             ....

> In order to have a blue cat it is necessary to have TWO variables so that
> you can represent BOTH states.

It is not necessarily animals being talked about, it may be china
ornaments, or naval punishments.  Or 'C.A.T.' may be an acronym for
Coloured-And-Transfered: in a factory it may represent a group state
(as above) for the painting stage.
 
> But there also has to be some basic degree of reason and commonality of
> experience, as JCE has argued.

There is: I mentioned 90% as an approximation, it may be more.  The
hard part is know which bits are in the 90% (and thus need no
checking) and which are oustside the 90% (and thus need to be
checked).

> I think the question is where one draws this line. You draw it higher than
> many of us; that doesn't mean you are wrong, it just means you are
> stricter...

Perhaps that represents that my experiences are more different   ;-)
 
> Ironically, a blue cat would be so far beyond the commonality of experience
> that it is unlikely ANY programmer would have trouble recognising that it
> must represent the state of TWO variables (Colour and Species).

Who said it was an animal ?  That is one of the things that _I_ would
check.

(Note that in the original it was not discovered that Cat was a state
of 'furry-animal' until _after_ 'all manner of searching'.  Is-a-Cat
is no clearer that this is in fact the case.
 
> Because SOME people "misuse" 88 levels, it does not follow that condition
> names in COBOL are of no use, and should be avoided.

There are many things that are multi-state, for example File-Status,
where it is useful to have groups of conditions as well as single
conditions.  For example:

       88  Status-OK             value '00' THRU '0z', '97'.
       88  Status-Duplicate-Alt  value '02'.
       88  Status-No-Optional    value '05'.

And 'Cat' and 'Painted-Blue' _may_ be one of those.

The problem is, as I have repeatedly stated, that when I read a
program that I haven't seen before, I cannot tell if the programmer is
one of the 'some that "misuse" 88 levels', or a perfect programmer
like yourself that has used the _same_ 'common sense' as I would/do.

I don't 'avoid' 88 levels, I just don't use them.

It happens that the way that I design programs there is little place
for them.  I most cases that I have seen the programmer is building
the rules into the code with value clauses on the 88 which means that
the program must be changed if the codes do.  I seldom do that.  I
usually build programs that determine state from data files.  There is
a usually a system control file and a 'decode' file.  The decode has a
key of 'field' and 'code'.  If a code exists in the decode it is
valid, it then contains data items which determine how that code
affects other data.

Instead of having a bunch of 88 levels that determine how much
discount to give, or what day to sell widgets on, I use a bunch of
decode records (or other) which give me a number.  This way I can have
multi-company systems that the users can change to suit their needs,
and do it _now_, rather than wait for the programmers to get around to
it.  (Actually I may be asked to change the data if the relationships
are too complex for them).

So I have little use for 88s.

Where I do have conditions, especially multi-state, I much prefer to
have the code values as constants (even if not explicit ones) and use
a comparison condition, it avoids all that aliasing.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 21)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-10-01T04:36:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Rseb.31407$Of2.1566349@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com> <217e491a.0309272144.46adced0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com> <217e491a.0309301135.6d9445a4@posting.google.com>`

```
So it wasn't my last post  - but this might be ;-)

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309301135.6d9445a4@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
…[5 more quoted lines elided]…
> checked).

If you don't know which is the 90% and which is the 10% you must thoroughly
check the entire code.

It's not bad to understand the code that one is changing; however, your
argument is that you cannot understand the code without understanding the
variable names/aliases, just in case the author has a different view to
yours.  To achieve this understanding, you have to comprehend the program in
its entirety before you can contextualize the variables.  For example, if
the code read:

LIGHT-SWITCH.
    IF LIGHT-SWITCH-ON THEN
        SET LIGHT-SWITCH-OFF
    END-IF.

You must torment yourself by asking is this (a) A light with a switch... or
(b) A player called Light who would determine whether we bat left or right
handed....or (c) The act of turning off a smaller lightweight switch.....etc
etc

So you must read all the code with some level of "doubt" until you can
accurately match your understanding of the code with the variables defined.

I on the other hand would read it as ...hmm if a light switch (a switch that
controls the power to a light) is on (light is lit - determined by a fairly
bright haze to the location) then turn it off (flip the switch up or down or
left or right or in or out until the power to the light is off.  This would
be indicated by a darker atmosphere).
Later on if something didn't make sense to me because, as it turns out,  the
author was disturbed by living in permanently lit house watching baseball
and knowing a switch hitter called Larry Light...I would wonder why this
code existed in a piece of electrical modelling software.

>  snip snip
> > Ironically, a blue cat would be so far beyond the commonality of
experience
> > that it is unlikely ANY programmer would have trouble recognising that
it
> > must represent the state of TWO variables (Colour and Species).
>
> Who said it was an animal ?  That is one of the things that _I_ would
> check.
If the program was commented/documented to describe what it was doing we
would have a context to help.
If it was a program to paint china cats, categorize animals it  should give
you some idea.

If you treated life like this it would be fun:
Could you boil the kettle for me?  --  Don't you mean boil the water in the
kettle ?
Yes, I do                                     --  No I can't, but the kettle
can.
So, could you put the kettle on?   --  On what? Or do you mean....
..could you turn the kettle on?      --  I don't know....."hey pretty
kettle, how *you* doing? You're looking hot today..."


> The problem is, as I have repeatedly stated, that when I read a
> program that I haven't seen before, I cannot tell if the programmer is
> one of the 'some that "misuse" 88 levels', or a perfect programmer
> like yourself that has used the _same_ 'common sense' as I would/do.
> I don't 'avoid' 88 levels, I just don't use them.

So 90% of programmers who use and understand them is saved what?
Nothing...it's just code written by someone with yet "another" different
view :-)
If it works it works. If it is understandable it is understandable :-)
It's a style at this point.

 > It happens that the way that I design programs there is little place
> for them.  I most cases that I have seen the programmer is building
> the rules into the code with value clauses on the 88 which means that
> the program must be changed if the codes do.
Not in my experience.  It's used to make very simple control flow
statements. Is the file open, is this the end of the cursor, do I have more
to do.  I never (or have seen) them used to implement anything that is a
changeable (more complex) rule.

> I seldom do that.  I usually build programs that determine state from data
files.  There is
> a usually a system control file and a 'decode' file.  The decode has a
> key of 'field' and 'code'.  If a code exists in the decode it is
> valid, it then contains data items which determine how that code
> affects other data.
So we save all manner of searching in a program by forcing the reader to (A)
look in a decode file and (B) understand your method of using said decode
file and this is my main question (C) understand what your 'FIELD' means.
In our example would it be PAINTED-BLUE? or what would it be if not?

This sure makes things *much* easier.

I don't disagree with what you are saying - externalizing rules is better
than 88 levels ...but do you have a decode file for a code to determine if
we are at the end of a cursor, or end of a file and other such items...or do
you simply, as you later say, just use variable names which I don't think
fix your issue anyway.

> Instead of having a bunch of 88 levels that determine how much
> discount to give, or what day to sell widgets on, I use a bunch of
…[4 more quoted lines elided]…
> are too complex for them).
These are business rules which would be stored in XML files, DBMS, CSVs with
hopefully a management tool around them, and certainly beyond 88 levels....
I've never seen anything like SET 50-PERCENT-DISCOUNT TO TRUE - but maybe
you have....but even here the argument is maintenance and not the difficulty
in understanding..as it is obvious _to me_ what this setting does..

>
> So I have little use for 88s.
…[3 more quoted lines elided]…
> a comparison condition, it avoids all that aliasing.
I had made this suggestion in an earlier post...
77 CHECKING-ACCOUNT PIC 99 VALUE 50

01 ACCOUNT-TYPE  PIC 99
Then
MOVE CHECKING-ACCOUNT TO ACCOUNT-TYPE
IF ACCOUNT-TYPE = CHECKING-ACCOUNT
 to resolve the Aliasing issue...I just don't think it's that big a deal....

On its own it saves you nothing because you still have the ability to (and
these aren't necessarily advisable)
A) Have a REDEFINES that makes YOUR-MAMA actually be ACCOUNT-TYPE
B) Have ACCOUNT-TYPE not be a 01 level item and set by reading a record into
the 01 (common)
01 ACCOUNT-RECORD.
   05 ACCOUNT-TYPE  PIC 99.
   05 OTHER-STUFF      PIC X(500).

MOVE FILE-REC TO ACCOUNT-RECORD.

I can only imagine that you always read a record and then move it one field
at a time to make sure your _all manner of searching_ is simplified.

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 22)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-01T13:57:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310011257.7794ba32@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com> <217e491a.0309301135.6d9445a4@posting.google.com> <1Rseb.31407$Of2.1566349@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote

> If you don't know which is the 90% and which is the 10% 

What I actually said was that I don't know if each part is within the
90% or within the 10%.  What mechanism do you use to determine this ?

Of course within one shop all code and styles become familiar enough
and any oddities are resolved by reference back to the originator to
'correct' his style to fit the norm.  All code is in the 100%.

Go to another shop and initially it will be 75/25 until you adjust.

> you must thoroughly check the entire code.

No. Only the condition variables and aliases within what is being
looked at, or actually most of the variables and labels used within
that.
 
> It's not bad to understand the code that one is changing; however, your
> argument is that you cannot understand the code without understanding the
> variable names/aliases, just in case the author has a different view to
> yours.  

It is the names that give the program meaning, jargon included.

> To achieve this understanding, you have to comprehend the program in
> its entirety before you can contextualize the variables.  

Do I ? Where was this ?


> For example, if
> the code read:
…[6 more quoted lines elided]…
> You must torment yourself by asking is this (a) A light with a switch... 

No, I just check that these are, in fact, aliases of the same variable
and what other aliases have been affected.

However, if it had been:

       IF ( Light-Switch = Switch-On )
           MOVE Switch-Off TO Light-Switch
       END-IF

then it can be seen that there is no aliasing, and also that a later:

       IF ( Light-Switch = Switch-Broken )

refers to the same variable.

> So you must read all the code with some level of "doubt" until you can
> accurately match your understanding of the code with the variables defined.

I always read with 'doubt', I listen to users requests with 'doubt', I
test my code with 'doubt'.  I don't assume that I understand what
others have written.  A pessimist is an optimist with experience.
 
> I on the other hand would read it as ...hmm if a light switch (a switch that
> controls the power to a light) is on (light is lit - determined by a fairly
> bright haze to the location) then turn it off (flip the switch up or down or
> left or right or in or out until the power to the light is off.  This would
> be indicated by a darker atmosphere).

Yes, but you just _wrote_ that.

> Could you boil the kettle for me?  --  Don't you mean boil the water in the
> kettle ?

Yes, one can have fun with this.  First you have to understand that
most people don't relate the answer they expect to the question they
asked.  Spam phone calls can be made amusing:

  "Do you mind if I take some of your time" ?
    "Yes".
  "I represent ... ... ..."
    "Excuse me, but did you understand the question you asked ?"
  "I didn't ask a question"
    "Yes you did, you asked 'Do you mind .."
     ...

or:

   "May I ask you your age?"
      "Yes"
   "Well, what is your age ?"
      "I didn't say I would answer, only that you may ask."

Of course one has to be more subtle when dealing with clients.  To
determine what they actually require means that you have to ensure
that the answers are actually to the questions, and not to what they
thought the question was.

I have seen too many times systems that failed to match what the user
wanted

> So 90% of programmers who use and understand them is saved what?
> Nothing...it's just code written by someone with yet "another" different
> view :-)
> If it works it works. If it is understandable it is understandable :-)
> It's a style at this point.

That's right, it is just a style.  It is no more than that.  It is
_NOT_ magic, it isn't some automatically understood, universal
mechanism that never needs checking.  It is just like every other
piece of code, like every other name, except is also adds aliasing.

> Not in my experience.  It's used to make very simple control flow
> statements. Is the file open, 

Now in the case of file status I would _definately_ check that
'Is-File-Staus-OK' checks the first byte for '0' rather the the whole
status area for '00'.

> I never (or have seen) them used to implement anything that is a
> changeable (more complex) rule.

eg: Cat and Painted-Blue ?

> So we save all manner of searching in a program by forcing the reader to (A)
> look in a decode file and (B) understand your method of using said decode
> file and this is my main question (C) understand what your 'FIELD' means.

Now where did _I_ say that my programs would not need 'all manner of
searching' by the next programmer ?

The issue being addressed was whether 88 levels managed to make the
magic required to understanding without, as was claimed, 'all manner
of searching'.

> I don't disagree with what you are saying - externalizing rules is better
> than 88 levels ...but do you have a decode file for a code to determine if
> we are at the end of a cursor, or end of a file and other such items...

Actually I do have all the file status values in the decode file, with
descriptions and a 'fatal' indicator.  This is used to display and/or
log exceptions in a generalised routine. This makes it easy to change
for different compilers and versions.  With SQL I can get the message
text.

> or do
> you simply, as you later say, just use variable names which I don't think
> fix your issue anyway.

They are not designed to 'fix the issue', but nor do 88-levels.  At
least with variable names (which is where I started out) I can grep
for them and find every reference, while finding all occurrance of all
the aliases is far more complicated.

> These are business rules which would be stored in XML files, DBMS, CSVs with
> hopefully a management tool around them, and certainly beyond 88 levels....

Actually you will see PECD advocating having them in components.

> I've never seen anything like SET 50-PERCENT-DISCOUNT TO TRUE - but maybe
> you have....

Yes, right here in this message group.

> but even here the argument is maintenance and not the difficulty
> in understanding..as it is obvious _to me_ what this setting does..
 
Yes, but you just wrote it.  What is 50-Percent-Discount an alias of ?
What has just been unset by the SET ?  If the next line is 'IF
Product-Not-Discountable' has this been unset by your 50-percent ?  Or
is this a _separate_variable_ ?  You would know because you wrote it. 
How would _I_ know without checking ?

> 77 CHECKING-ACCOUNT PIC 99 VALUE 50
> 01 ACCOUNT-TYPE  PIC 99
…[3 more quoted lines elided]…
>  to resolve the Aliasing issue...I just don't think it's that big a deal....

Exactly.  This is resolving the aliasing.  This is making the usage
searchable. This is the message that I have been making.


> On its own it saves you nothing because you still have the ability to (and
> these aren't necessarily advisable)
> A) Have a REDEFINES that makes YOUR-MAMA actually be ACCOUNT-TYPE

I find aliasing a bad idea everywhere.  At least by checking I can
discover this, you seemed to try to disuade me from checking.

> B) Have ACCOUNT-TYPE not be a 01 level item and set by reading a record into
> the 01 (common)
…[7 more quoted lines elided]…
> at a time to make sure your _all manner of searching_ is simplified.

Well actually I avoid moving file records into working storage, not
having the paranoia about file records areas that IBM mainframers seem
to have (apparently for good historical reasons).

Of course if the program duplicated the data in this way (either by
record move or by field move) and then _used_ both the field in the
record area _and_ in the working-storage alternately in conditions and
setting, then that would complicate the searching, and probably make
the program unmaintainable.

But, no, I don't do that, nor any of the other things that you
invented for me.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 23)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-10-02T03:52:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fiNeb.37360$Of2.1708889@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com> <217e491a.0309301135.6d9445a4@posting.google.com> <1Rseb.31407$Of2.1566349@twister.tampabay.rr.com> <217e491a.0310011257.7794ba32@posting.google.com>`

```
Really Really Really the last post.

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0310011257.7794ba32@posting.google.com...
> "jce" <defaultuser@hotmail.com> wrote
>
…[3 more quoted lines elided]…
> 90% or within the 10%.  What mechanism do you use to determine this ?
I make common sense assumptions.

> Of course within one shop all code and styles become familiar enough
> and any oddities are resolved by reference back to the originator to
> 'correct' his style to fit the norm.  All code is in the 100%.
Hmm..not in my shop - each to his own is our rule.  As long as it's
readable.  Each module is very short and modularized so it's not an issue.
The only monolithic programs we have are old and only a couple of us are
brave enough to touch them :-)

> > It's not bad to understand the code that one is changing; however, your
> > argument is that you cannot understand the code without understanding
the
> > variable names/aliases, just in case the author has a different view to
> > yours.
>
> It is the names that give the program meaning, jargon included.
Yes, but you have repeatedly argued you don't "know" their meaning..

> > To achieve this understanding, you have to comprehend the program in
> > its entirety before you can contextualize the variables.
>
> Do I ? Where was this ?
If you fail to understand their cultural differences (is a light switch
open)....you don't understand until this contextualization occurs.

> > For example, if
> > the code read:
…[21 more quoted lines elided]…
> refers to the same variable.
I had previously stated this was an appropriate solution.

> > So you must read all the code with some level of "doubt" until you can
> > accurately match your understanding of the code with the variables
defined.
>
> I always read with 'doubt', I listen to users requests with 'doubt', I
> test my code with 'doubt'.  I don't assume that I understand what
> others have written.  A pessimist is an optimist with experience.
A hypochondriac is then a pessimist with experience, no doubt.

> > I on the other hand would read it as ...hmm if a light switch (a switch
that
> > controls the power to a light) is on (light is lit - determined by a
fairly
> > bright haze to the location) then turn it off (flip the switch up or
down or
> > left or right or in or out until the power to the light is off.  This
would
> > be indicated by a darker atmosphere).
> Yes, but you just _wrote_ that.
I would suggest that 99% of individuals reading this without any surrounding
code would also.

> > Could you boil the kettle for me?  --  Don't you mean boil the water in
the
> > kettle ?
> Yes, one can have fun with this.  First you have to understand that
…[8 more quoted lines elided]…
>     "Yes you did, you asked 'Do you mind .."
I'll try that one :-)

> > So 90% of programmers who use and understand them is saved what?
> > Nothing...it's just code written by someone with yet "another" different
…[7 more quoted lines elided]…
> piece of code, like every other name, except is also adds aliasing.
Ok. Understood.

> > Not in my experience.  It's used to make very simple control flow
> > statements. Is the file open,
…[7 more quoted lines elided]…
> eg: Cat and Painted-Blue ?
Yes, even Cat and Painted-Blue

> > So we save all manner of searching in a program by forcing the reader to
(A)
> > look in a decode file and (B) understand your method of using said
decode
> > file and this is my main question (C) understand what your 'FIELD'
means.
>
> Now where did _I_ say that my programs would not need 'all manner of
> searching' by the next programmer ?
Just wondering where the benefits were in swapping one search for
another...other than grep etc not being overly useful in this regard so file
searching may be harder - you don't know which file belongs to a program
without looking at the execution of it.

> > These are business rules which would be stored in XML files, DBMS, CSVs
with
> > hopefully a management tool around them, and certainly beyond 88
levels....
>
> Actually you will see PECD advocating having them in components.
Not once has he advocated hard coding anything in components that I am aware
of.

> > I've never seen anything like SET 50-PERCENT-DISCOUNT TO TRUE - but
maybe
> > you have....
> Yes, right here in this message group.
…[8 more quoted lines elided]…
> How would _I_ know without checking ?
I understand your point.  I still don't think this is complicated..but we
did just stumble on a *much* better example than the blue cat - and I do buy
why this would be complicated to a code newcomer.  15-0.  You're on serve.
:-)

> > 77 CHECKING-ACCOUNT PIC 99 VALUE 50
> > 01 ACCOUNT-TYPE  PIC 99
…[3 more quoted lines elided]…
> >  to resolve the Aliasing issue...I just don't think it's that big a
deal....
>
> Exactly.  This is resolving the aliasing.  This is making the usage
> searchable. This is the message that I have been making.
Then we agree in principle - you're merely a much stricter alias enforcer.

> > On its own it saves you nothing because you still have the ability to
(and
> > these aren't necessarily advisable)
> > A) Have a REDEFINES that makes YOUR-MAMA actually be ACCOUNT-TYPE
>
> I find aliasing a bad idea everywhere.  At least by checking I can
> discover this, you seemed to try to disuade me from checking.
So what about function / program calls where you pass by reference.  Do you
always check there also?
Not really - I would *never* disuade someone from checking.  I just tend to
disagree with how much you think it is required.

> > B) Have ACCOUNT-TYPE not be a 01 level item and set by reading a record
into
> > the 01 (common)
> > 01 ACCOUNT-RECORD.
…[5 more quoted lines elided]…
> > I can only imagine that you always read a record and then move it one
field
> > at a time to make sure your _all manner of searching_ is simplified.
>
> Well actually I avoid moving file records into working storage, not
> having the paranoia about file records areas that IBM mainframers seem
> to have (apparently for good historical reasons).
Very fair point.  30-0.

> Of course if the program duplicated the data in this way (either by
> record move or by field move) and then _used_ both the field in the
> record area _and_ in the working-storage alternately in conditions and
> setting, then that would complicate the searching, and probably make
> the program unmaintainable.
Agreed 100%.

> But, no, I don't do that, nor any of the other things that you
> invented for me.
Glad to hear it.....Game to you - I withdraw.

_I think you've sufficiently convinced me of your issue_

I agree in general - I'm just not as strict as you.

Thanks again

JCE
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-02T17:21:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blhmps$gu5$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com> <217e491a.0309301135.6d9445a4@posting.google.com> <1Rseb.31407$Of2.1566349@twister.tampabay.rr.com> <217e491a.0310011257.7794ba32@posting.google.com> <fiNeb.37360$Of2.1708889@twister.tampabay.rr.com>`

```

On  1-Oct-2003, "jce" <defaultuser@hotmail.com> wrote:

> > What I actually said was that I don't know if each part is within the
> > 90% or within the 10%.  What mechanism do you use to determine this ?

> I make common sense assumptions.

I have found such assumptions to be fraught with danger.   It is safer to assume
that the person who wrote that code uses some sense other than what I would
consider to be common.


> Hmm..not in my shop - each to his own is our rule.  As long as it's
> readable.  Each module is very short and modularized so it's not an issue.
> The only monolithic programs we have are old and only a couple of us are
> brave enough to touch them :-)

Some ways of modularizing can hide the fact that aliases are used.   Some types
of re-use can disguise meaningful names.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-02T14:15:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blhbta$lh1$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <wWDdb.14524$Of2.1089126@twister.tampabay.rr.com> <217e491a.0309281439.1ef83909@posting.google.com> <VWLdb.43410$Ci5.1134643@twister.tampabay.rr.com> <217e491a.0309282216.43a581c1@posting.google.com> <bTUdb.43944$Ci5.1181601@twister.tampabay.rr.com> <217e491a.0309291441.28542e04@posting.google.com> <3f795fea_4@news.athenanews.com> <217e491a.0309301135.6d9445a4@posting.google.com> <1Rseb.31407$Of2.1566349@twister.tampabay.rr.com> <217e491a.0310011257.7794ba32@posting.google.com>`

```

On  1-Oct-2003, riplin@Azonic.co.nz (Richard) wrote:

>    "May I ask you your age?"
>       "Yes"
>    "Well, what is your age ?"
>       "I didn't say I would answer, only that you may ask."

Do you have a watch?
Yes
What time is it?
I don't know.
Could you look at your watch?
Yes.


Please look at your watch.
OK.   Done.

Could you tell me what time it is?
Yes.

See this 2x4?    Anticipate what I will do with it if you don't tell me what
time it is.
8:14 A.M.  MST.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 13)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-28T17:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030928131105.03086.00000412@mb-m07.aol.com>`
- **References:** `<217e491a.0309272144.46adced0@posting.google.com>`

```
This is a fascinating discussion, with many well expressed particular points.

I wish to make an extension of this subject to a part of Object Oriented
programming, and hope that this will be acceptable to those active with this
thread.

COBOL's 88 conditionals actually are an automation of the programmer. instead
of referencing the field name and the value of interest, merely the condition
name is designated. That is arguably an efficiency feature of the common
business language.

When a condition involves a set of values, or as with the modern COBOL a range,
then the referencing of a mere condition name  allows the programmer to avoid
coding a potentially long logical expression. That is a slightly larger
increase in productivity for the hard working technician.

(It is definitely worth noting that the set of values that are effectively ORed
within a conditional list are actually also implicitly syntactically
parenthesized. This has always insulated them from the problems of hot logical
AND in combined abbreviated conditionals from grabbing the last part of the
listed values in an 88 conditional ... nothing compares to this power in COBOL
in any language .. that is definitely an efficiency - keeping the programming
out of that time sink)


When 88s are coded in copybooks we get reuse, and centralized control. So if a
condition is multifaceted the ORed logical expression can be driven into as
many programs as we like by mere re-compile (that includes, by the way removing
one of the values of a conditional).

This 'efficiency' is not the most important thing going on in business data
processing, but it is useful, IMHO, to look at the language facilities as
detemining factors for productivity

Yet the names of conditionals are most definitely a problem. And as well
expressed in this thread culture does limit our ability to pass to the next
coder the sense that we have encoded in the name.

My extension to object oriented programming, is that this is about to get much
worse! An 88, for all intents and purposes is simply an early achievement of a
wrapper. 

When our 88s are dealing with a binary yes/no or true/false, we are just
dealing with COBOL's first booleans. As the set of 88's per switch grow more
robust, we do not have easy terms for the logical switches.

In OO COBOL we will have a choice of getting the actual value (or what we think
is the actual value) with an accessor such as

  myObject :: getSwitchXyz

And there will then be possible the literal kind of test

 IF  myObject :: getSwitchXyz = 'Y' PERFROM ...

Then someone will wrap it a la Object with a boolean accessor say

  myObject :: switchXyzIsGreen

or another  wrapper than encompasses a range

  myObject :: switchXyzIsInRange


So this naming issue that you are talking about so eloquently in this thread is
about to jump like a very mobile jack right out of the box and impact code
readability big time. It is not just the conditionals in the new OOP tools.

You see, this concern about condition names is really just a concern about the
names of wrappers that have historically been available in COBOL. OO COBOL will
be practiced by people who graduate from schools where they are told to wrap
EVERYTHING. And that is not an exaggeration.

This is really a major issue that is very slowly brewing. I have asserted in
another thread that we will need CBAs and CBEs. One of the jobs of the Common
Base Enabler will be to mentor people. The only way to promote reuse is to
teach people what is there to be reused. In diverse societies there will infact
be linguistic issues at the point of the name of accessors, mutators and
boolean conglomerate conditionals.

As OO code accumulates into its own sizable legacy there will have to be
individuals that assist in transfering knowledge of what the code names mean. 

At this time entire college courses are taught concerning foundation classes. 
As companies establish major collections of classes unique to their business,
there will be a need to teach their Proprietary Common Base elements to each
succeeding generation of workers in their shop. This will be needed right down
to the level of the accessors, mutators, and bools.

So, I hope that it is not rude to enter this view within this thread. I think
that it is really not oblique, but an expansion.  My sense is, if the aspects
you all are talking about are interesting to you, well then look just ahead
there on the road. There is a monster there all wrapped up in multiple layers
of names.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-29T14:09:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl9eds$ekl$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <217e491a.0309232347.2811c0f5@posting.google.com> <3f7406ca_5@news.athenanews.com> <217e491a.0309261224.3fc31e37@posting.google.com> <aX2db.12305$Of2.775050@twister.tampabay.rr.com>`

```

On 26-Sep-2003, "jce" <defaultuser@hotmail.com> wrote:

> If we have simple states:
> IS-OPEN, IS-CLOSED, IS-HUMAN, IS-FILTERED then it is obvious what those
> states are.
> There are usually contextual clues a check for IS-HUMAN may come in a
> paragraph called - check-species, or animal-group-process.

Yes.   But we still have to look at the switch to find out what can set IS-HUMAN
to something else.

IS-ANIMAL
IS-ALIEN
IS-INHUMAN
IS-NOT-HUMAN
IS-PROGRAMMER
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-24T15:18:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksckr$78p$1@peabody.colorado.edu>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com>`

```

On 23-Sep-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> They COULD be but they are NOT. They are NOT because I wouldn't code them in
> the way you describe.
…[4 more quoted lines elided]…
> back...

That works if your style of code was the only style of code that you work with.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-26T19:16:41+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f74051f_6@news.athenanews.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <BMScnYdcp6GyOfSiXTWJiQ@giganews.com> <3f6d4254_3@news.athenanews.com> <217e491a.0309211133.6e3b8459@posting.google.com> <3f70db7f_4@news.athenanews.com> <bksckr$78p$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bksckr$78p$1@peabody.colorado.edu...
>
> On 23-Sep-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > They COULD be but they are NOT. They are NOT because I wouldn't code
them in
> > the way you describe.
> >
…[5 more quoted lines elided]…
> That works if your style of code was the only style of code that you work
with.

Fair comment, Howard.

In actuality, I have no problem with dealing with most styles of COBOL. I
have done so for over 30 years, in different cultures and countries.
Strangely, no one I have worked with has ever had problems maintaining my
style of code either.

(At least I have never heard about it...<G>. (I exclude Foodman, who
definitely objected to my style, but I never actually worked with him...).
More often, they end up adopting elements of the style I use. This is right
and proper because I adopted most of it from very wise old programmers now
sadly departed to the Great Computer Room in the Sky. I was trained in the
days before Computer Science when Common Sense (for the most part...) ruled
COBOL...<G>)

If you call yourself a COBOL programmer, you should be able to handle COBOL
and the way different people write it.

Pete.
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-17T10:13:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j39gmv4mfjuij0hp4v2mpnci7ak77iq7q6@4ax.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com>`

```
On Tue, 16 Sep 2003 21:48:48 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>Frederico Fonseca wrote:
>
…[16 more quoted lines elided]…
>there are programmers who like this technique along with its companion:
Sure you can. 
>

>IF VALID-ANSWER
>   (do something)
Thats precisely my style.
>
>
…[13 more quoted lines elided]…
>can handle the VALID-ANSWER = "M(aybe)" case.
This particular thread was about  "set to false". When using this one
would normally only use two possible values (not mandatory though).
In my particular case if I have more than two possible options for a
variable then I do NOT use the "set to false" options. So on your
particular example I would code


01  variablex pic x.
   88 VALID-ANSWER-CLEAR VALUE " ".
   88 VALID-ANSWER-Y VALUE "Y".
   88 VALID-ANSWER-N VALUE "N".
   88 VALID-ANSWER-M VALUE "M".

and use them accordingly with "set to true" only.

But all this is really just a questions of style, both usable and
readable.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-16T10:57:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p0C9b.21611$NM1.911@newsread2.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`

```
SET TO FALSE is a "required" part of the 2002 COBOL Standard - and is
available as an extension in some existing compilers.

It requires that one define the FALSE-value in the 88 level definition, e.g.

  88  Good-Value "Y" False is  "N".
           ...
  Set Good-Value to False   *> now as a value of "N".
```

#### ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-16T06:26:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmdsrgn5auv90e@corp.supernews.com>`
- **In-Reply-To:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`

```
Dirk Haar wrote:

> Hi !
> I had a very hard discussion with a collegue 
…[8 more quoted lines elided]…
> so don't answer "BECAUSE 'FALSE' IS NOT A COBOL WORD blabla'".

While I've seen that two people have already stated that FALSE is part 
of the 2002 standard, I'm betting you all are probably on COBOL 85.  If 
your compiler does not support that extension, it's really pretty simple 
as to why FALSE is not supported.

Take this example (an actual piece of code from one of my copy 
procedures)...

            12  W415-NFSDTC-Method                    Pic 1(18) Binary-1.
       *>           The following condition enumerates all valid methods
       *>           of this class.  If another method is added, be sure
       *>           to modify this condition.
                88  W415-Valid-Method         Values  0 Thru 16,
                                                     21 Thru 29,
                                                     41 Thru 57,
                                                     61 Thru 66,
                                                     81 Thru 84,
                                                     91 Thru 95.
       *>           No method
                88  W415-No-Method-Passed               Value 0.
       *>           Date/time retrieval methods
                88  W415-Get-All-Dates-Times            Value 1.
                88  W415-Get-All-Zulu-Date-Time         Value 2.
                88  W415-Get-Zulu-Jul-Date-Time         Value 3.
                88  W415-Get-Zulu-Std-Date-Time         Value 4.
                88  W415-Get-Zulu-Mil-Date-Time         Value 5.
                88  W415-Get-Zulu-TimeStamp             Value 6.
                88  W415-Get-All-Gang-Date-Time         Value 7.
                88  W415-Get-Gang-Jul-Date-Time         Value 8.
                88  W415-Get-Gang-Std-Date-Time         Value 9.
                88  W415-Get-Gang-Mil-Date-Time         Value 10.
                88  W415-Get-Gang-TimeStamp             Value 11.
                88  W415-Get-All-Unit-Date-Time         Value 12.
                88  W415-Get-Unit-Jul-Date-Time         Value 13.
                88  W415-Get-Unit-Std-Date-Time         Value 14.
                88  W415-Get-Unit-Mil-Date-Time         Value 15.
                88  W415-Get-Unit-TimeStamp             Value 16.
       *>           Reference conversion methods
                88  W415-Convert-Zulu-to-All            Value 21.
                88  W415-Convert-Zulu-to-Gang           Value 22.
                88  W415-Convert-Zulu-to-Unit           Value 23.
                88  W415-Convert-Gang-to-All            Value 24.
                88  W415-Convert-Gang-to-Zulu           Value 25.
                88  W415-Convert-Gang-to-Unit           Value 26.
                88  W415-Convert-Unit-to-All            Value 27.
                88  W415-Convert-Unit-to-Zulu           Value 28.
                88  W415-Convert-Unit-to-Gang           Value 29.
       *>           Format conversion methods
                88  W415-Convert-Jul-to-All             Value 41.
                88  W415-Convert-Jul-to-Std             Value 42.
                88  W415-Convert-Jul-to-Mil             Value 43.
                88  W415-Convert-Jul-to-TS              Value 44.
                88  W415-Convert-Std-to-All             Value 45.
                88  W415-Convert-Std-to-Jul             Value 46.
                88  W415-Convert-Std-to-Mil             Value 47.
                88  W415-Convert-Std-to-TS              Value 48.
                88  W415-Convert-Mil-to-All             Value 49.
                88  W415-Convert-Mil-to-Jul             Value 50.
                88  W415-Convert-Mil-to-Std             Value 51.
                88  W415-Convert-Mil-to-TS              Value 52.
                88  W415-Convert-TS-to-All              Value 53.
                88  W415-Convert-TS-to-Jul              Value 54.
                88  W415-Convert-TS-to-Std              Value 55.
                88  W415-Convert-TS-to-Mil              Value 56.
       *>           Date manipulation methods
                88  W415-Day-of-Week                    Value 61.
                88  W415-Offset                         Value 62.
                88  W415-Difference                     Value 63.
                88  W415-Elapsed-Time                   Value 64.
                88  W415-Date-Range-Check               Value 65.
                88  W415-Offset-Date-Range-Check        Value 66.
       *>           Date expansion methods
                88  W415-Expand-Jul-Date                Value 81.
                88  W415-Expand-Std-Date                Value 82.
                88  W415-Expand-Mil-Date                Value 83.
                88  W415-Expand-Year                    Value 84.
       *>           Date validation methods
                88  W415-Validate-Julian-Date           Value 91.
                88  W415-Validate-Standard-Date         Value 92.
                88  W415-Validate-Military-Date         Value 93.
                88  W415-Validate-TimeStamp             Value 94.
                88  W415-Validate-Time                  Value 95.

(Binary-1 is a Unisys extension that allows exact binary - the maximum 
value of this, represented numerically, would be 262,143.)

Now, what should the compiler do if, for example, I say "Set 
W415-Validate-Time to False"?  The compiler has no way of knowing what 
value to put in the actual variable, because it isn't defined.  Also, if 
the compiler "guessed" and put a valid but non-95 value in it, it could 
inadvertently set another condition to True, which would be bad...

This was how I explained it to some other 20+ year veterans where I 
work.  :)  Of course, with the new syntax (and the extension on some 
compilers), you can control the false value, which means that the 
compiler could handle it (which is why it would work in that case).
```

##### ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-16T12:47:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ttdmvcopjql99ei5u9b9sdcfg5mbik8e9@4ax.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <vmdsrgn5auv90e@corp.supernews.com>`

```
On Tue, 16 Sep 2003 06:26:37 -0500, LX-i <LXi0007@Netscape.net> wrote:

>Dirk Haar wrote:
>
…[15 more quoted lines elided]…
>as to why FALSE is not supported.

Well I have been using it at least since 1993, long before the 2000
extensions were being discussed. COBOL 85.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-16T18:11:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmf65btihfqa10@corp.supernews.com>`
- **In-Reply-To:** `<4ttdmvcopjql99ei5u9b9sdcfg5mbik8e9@4ax.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <vmdsrgn5auv90e@corp.supernews.com> <4ttdmvcopjql99ei5u9b9sdcfg5mbik8e9@4ax.com>`

```
Frederico Fonseca wrote:
> On Tue, 16 Sep 2003 06:26:37 -0500, LX-i <LXi0007@Netscape.net> wrote:
> 
…[23 more quoted lines elided]…
> extensions were being discussed. COBOL 85.

Then you did it outside of the ANSI/ISO COBOL 85 standard.  My reply was 
geared toward that standard, as they may or may not be using a compiler 
that supports such constructs.  :)
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-16T23:38:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B9N9b.25876$NM1.14492@newsread2.news.atl.earthlink.net>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <vmdsrgn5auv90e@corp.supernews.com> <4ttdmvcopjql99ei5u9b9sdcfg5mbik8e9@4ax.com> <vmf65btihfqa10@corp.supernews.com>`

```
"LX-i" <LXi0007@Netscape.net> wrote in message
news:vmf65btihfqa10@corp.supernews.com...
> Frederico Fonseca wrote:
> > On Tue, 16 Sep 2003 06:26:37 -0500, LX-i <LXi0007@Netscape.net> wrote:
> >
<snip>
> > Well I have been using it at least since 1993, long before the 2000
> > extensions were being discussed. COBOL 85.
…[5 more quoted lines elided]…
>

Well, Yes and No.

  True - SET TO FALSE was an extension to the ANSI/ISO '85 Standard
  but also TRUE - SET TO FALSE *was* included in the CODASYL JOD *long*
before 1993

Therefore, if by "standard" you mean (and most people do) ANSI/ISO COBOL
Standard, then this was an extension.  However, there WAS a "standard"
definition of this feature well before the 2002 ANSI/ISO Standard included
it.
```

#### ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Dirk Haar <news@mideal.de>
- **Date:** 2003-09-19T00:40:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030919002818.2DA1.NEWS@mideal.de>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com>`

```
Thank you Bill, "Live from Montgomery,AL w/o name" and Howard,
who told me what I asked for.
I argued the same way as you did, except that I didn't know about 
the new COBOL2002 std option.
This syntax change of course enables the compiler to set the variable
to a correct and logical value (where I believe the latter is hard to
control in a multi-variable/value definition, like
01 Q	PIX 99 VALUE ZERO.
  88 Q1MONTH	VALUE 01,02,03.
  88 Q2MONTH	VALUE 04,05,06.
  88 Q3MONTH	VALUE 07,08,09.
  88 Q4MONTH	VALUE 10,11,12.

I guess we'll soon find someone who wants to set Q1MONTH to FALSE...

Dirk
```

##### ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** docdwarf@panix.com
- **Date:** 2003-09-18T19:39:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkdfml$g88$1@panix1.panix.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <20030919002818.2DA1.NEWS@mideal.de>`

```
In article <20030919002818.2DA1.NEWS@mideal.de>,
Dirk Haar  <news@mideal.de> wrote:

[snip]

>This syntax change of course enables the compiler to set the variable
>to a correct and logical value (where I believe the latter is hard to
…[7 more quoted lines elided]…
>I guess we'll soon find someone who wants to set Q1MONTH to FALSE...

As I understand it unless a FALSE value is specified at the 88 level 
you'll get a syntax error.

DD
```

##### ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-19T07:13:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmlsn54i6t50a8@corp.supernews.com>`
- **In-Reply-To:** `<20030919002818.2DA1.NEWS@mideal.de>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <20030919002818.2DA1.NEWS@mideal.de>`

```
Dirk Haar wrote:

> Thank you Bill, "Live from Montgomery,AL w/o name"

It's Daniel.  :)  And you're welcome.  I wish our compiler supported the 
"False is" clause - I'd use the heck out of it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
