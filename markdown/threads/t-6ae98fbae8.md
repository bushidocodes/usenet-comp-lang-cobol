[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Numeric validation

_21 messages · 10 participants · 2005-06_

---

### Numeric validation

- **From:** "Mark V. Svanesteen" <mark.svanesteen(snabela)mail.dk>
- **Date:** 2005-06-08T12:34:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xn0e399p0e5qps000@news.tele.dk>`

```
Hi all,

Been trying for quite a while now searching for a solution to my
problem..

I use cobol v2.7 on an alpha-system(7.3.1).

Is there a 100% way of telling if a numeric edited field really
contains valid data and not crap data like "20202".

My fields:

	01 field1 PIC S9(9)V99 COMP-3

To validate, I've been trying:

	IF FIELD1 IS NUMERIC THEN
		MOVE FIELD1 TO ...
	ELSE MOVE 0 TO ...
	END-IF

and,

	IF NOT FIELD1 IS NUMERIC THEN
		MOVE 0 TO ...
	ELSE
		MOVE FIELD1 TO ...
	END-IF


In my desperation, I've even tried moving field1 to a alfabetic
temporary field and then to see what is there and then convert it back
to numeric.

	MOVE FUNCTION NUMVAL (FIELD1) TO ...
	
	MOVE FUNCTION NUMVAL-C (FIELD1) TO ...

Even so, I get "20202" in my recieving field.

My frustration is complete and I'm too far behind schedule, please help
me get a fool-proof way of testing for bad data in numeric edited
fields.
```

#### ↳ Re: Numeric validation

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-06-08T16:39:11+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75tda1535hdd46c7m0d5lue4ljtc0pq02p@4ax.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk>`

```
On 08 Jun 2005 12:34:32 GMT "Mark V. Svanesteen"
<mark.svanesteen(snabela)mail.dk> wrote:

:>Been trying for quite a while now searching for a solution to my
:>problem..

:>I use cobol v2.7 on an alpha-system(7.3.1).

:>Is there a 100% way of telling if a numeric edited field really
:>contains valid data and not crap data like "20202".

What is the picture of your numeric edited field?

x'20' is a space in ascii.


:>My frustration is complete and I'm too far behind schedule, please help
:>me get a fool-proof way of testing for bad data in numeric edited
:>fields.

There are consulting firms in the USA which can assist, for a fee.
```

##### ↳ ↳ Re: Numeric validation

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-06-08T14:01:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TSCpe.2575$jS1.2275@newssvr17.news.prodigy.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <75tda1535hdd46c7m0d5lue4ljtc0pq02p@4ax.com>`

```
> :>Is there a 100% way of telling if a numeric edited field really
> :>contains valid data and not crap data like "20202".

Guessing.this would be worth a try...

SPECIAL-NAMES.
  CLASS VALID-EDITED-NUMERIC  VALUES  '0' TO ''9-', ',', ','  (and whatever)

  IF EDITED-NUMERIC-FIELD  NOT VALID-EDITED-NUMERIC
     DISPLAY 'CRAP IN EDITED-NUMERIC FIELD'

.. or something along those lines

MCM
```

#### ↳ Re: Numeric validation

- **From:** docdwarf@panix.com
- **Date:** 2005-06-08T09:41:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d86si1$bg$1@panix5.panix.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk>`

```
In article <xn0e399p0e5qps000@news.tele.dk>,
Mark V. Svanesteen <mark.svanesteen(snabela)mail.dk> wrote:
>Hi all,
>
…[6 more quoted lines elided]…
>contains valid data and not crap data like "20202".

20202 is a perfectly valid number... and it nicely fills a bit of the void 
between twenty thousand, two hundred one and twenty thousand, two hundred 
three.

>
>My fields:
>
>	01 field1 PIC S9(9)V99 COMP-3

Naughty, naughty... no VALUE clause?  It 'smells' to me like you're 
getting SPACES as the uninitialised data (ASCII x'20')... try

01 field1 PIC S9(9)V99 COMP-3 VALUE +0.

... and see what happens.

DD
```

#### ↳ Re: Numeric validation

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-09T02:07:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gocdaFdb9kaU1@individual.net>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk>`

```

"Mark V. Svanesteen" <mark.svanesteen(snabela)mail.dk> wrote in message
news:xn0e399p0e5qps000@news.tele.dk...
> Hi all,
>
…[7 more quoted lines elided]…
>
Mark, you didn't say whether that is hex or not. If it isn't, then the field
is valid... If it is, why would you only show two and a half bytes?

> My fields:
>
> 01 field1 PIC S9(9)V99 COMP-3

Is there more to this definition? I see no full stop. Is it redefined so
that it might have spaces in it? Or uninitialized?

>
> To validate, I've been trying:
…[5 more quoted lines elided]…
>

That's pretty usual. You might need to say 'NUMERIC AND POSITIVE' to avoid
the possibility of an alpha in the last position of your input field being
considered a sign.

There are several things here that don't add up. This is NOT a numeric
edited field; you said  your problem was with such a field. This is an
internal packed decimal field that will occupy 5 bytes. I would expect you
have moved a field from an input device to this field. If that field had
spaces in it, this field will be invalid. Applying the 'NUMERIC AND
POSITIVE' test above should trap this.


> and,
>
…[16 more quoted lines elided]…
>

It looks like packed ASCII blanks.

> My frustration is complete and I'm too far behind schedule, please help
> me get a fool-proof way of testing for bad data in numeric edited
> fields.
>

Personally, I use a numeric validation component  (COM) I wrote some time
ago. It will trap anything and allows a single sign and decimal point.

I understand and sympathise with your frustration. We have all been there.
If the suggestion above doesn't work, mail me privately and I'll give you
the source of the validation component (it is written in COBOL), so you
could call it as a subroutine.

Pete.
```

#### ↳ Re: Numeric validation

- **From:** "Ron" <NoSpam@SpamSucks.Org>
- **Date:** 2005-06-08T18:07:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wv6dnaW8Feu75zrfRVn_vg@giganews.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk>`

```
I am not sure what you are trying to accomplish. I know lot's of people
are going to say comp-3 is implementor dependant, but comp-3 is almost
always packed decimal so lets assume field-1 is packed okay?

But your question is incoherent with the example. A comp-3 field
is by definition NOT numeric edited. Numeric edited is something
like Pic Z,ZZ9 which will never be numeric because of the (possible)
spaces and the comma.

Why can't you say IF field-1 is numeric? If it contains
valid packed data it is numeric, if not it isn't. Note that the sign must
be consistent with the field definition picture otherwise it will test not numeric.
It sounds you're saying you are getting garbage or non-numeric data in field1
that somehow is testing numeric? Can you please post some specific
examples of your input and the results you are receving? There must
be something else we are missing.

A few comp-3 examples:
PIC S999V99  X'12345C' Numeric
                        X'12345D' Numeric
                        X'12345F' NOT Numeric
                        X'020202' NOT Numeric
                        X'1234AD' NOT Numeric

PIC 999V99   X'12345F' Numeric
                       X'12345C' NOT Numeric
```

##### ↳ ↳ Numeric validation revisited

- **From:** "klovn" <mark.svanesteen(snabela)mail.dk>
- **Date:** 2005-06-09T08:17:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xn0e3ahic210pz000@news.tele.dk>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com>`

```
>Can you please post some specific examples of your input and
> the results you are receving? There must be something else we are
> missing.

Ok, I tried to avoid a long problem-definition, but I can now see my
problem is not that easily defined. So, here we go again:

I have a user input fields:

01 VFYS PIC S9(9)V99 COMP-3.
01 VMIN PIC S9(5) COMP-3.
01 VMAX PIC S9(5) COMP-3.
01 LTAN PIC S9(7) COMP-3.

I have to add up a lot of LTAN'es and subtract VFYS from LTAN. Finally
all 4 values are to be printed out.

01 Temp-add-field PIC S9(9)V99 COMP-3.
 
But first, I move them into a table, contaning an exact copy of the
above fields. This way I can sort them, according to some other
irellevant field.

Then, I move them into a print-line with the fields:

01 PRINTLINE.
	...
	03 PFYS PIC ZZZ.ZZZ.ZZ9-.
	03 PMIN PIC ZZZZ9-.
	03 PMAX PIC ZZZZ9-.
	03 PTAN PIC ZZZ.ZZZ.ZZ9-.
	...

It seems my input-data is garbage (stupid users), because On the
printer it says:

... some-string some-thing-else	437   20202 20202   21


Actually only PMIN and PMAX is the problem.

Darn it that deadline is getting close!


I've been trying and trying. Could one of you maybe tell me where to
look.

Thanks for all your replyes (Binyamin,Docdwarf,Pete,Ron and Walter)


Mark, Denmark.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-09T02:41:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118310085.994798.321000@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<xn0e3ahic210pz000@news.tele.dk>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk>`

```
> I have a user input fields:

> 01 VFYS PIC S9(9)V99 COMP-3.
> 01 VMIN PIC S9(5) COMP-3.
> 01 VMAX PIC S9(5) COMP-3.
> 01 LTAN PIC S9(7) COMP-3.

COMP-3 is packed decimal (probably). Why are you accepting data into
COMP-3.  Why would you not have your input fields as DISPLAY ?

202020202.. is the value of a packed decimal field when the bytes it
occupies has spaces in it. This is a perfectly valid value for a
NUMERIC test for a packed decimal.

If these are in fact the subject of an ACCEPT then it is most likely
that you should be accepting into an alphabetic field and then use
NUMVAL() in a COMPUTE with a ON SIZE ERROR.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-09T09:39:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11agl4rndpi6n72@news.supernews.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk>`

```
klovn wrote:
>> Can you please post some specific examples of your input and
>> the results you are receving? There must be something else we are
…[37 more quoted lines elided]…
> Actually only PMIN and PMAX is the problem.

## No. PMIN and PMAX are SYMPTOMS of the problem

>
> Darn it that deadline is getting close!
…[8 more quoted lines elided]…
> Mark, Denmark.

I don't see how a user can input a COMP-3 number. Nevertheless, IF you have 
a COMP-3 number whose content you cannot control AND you must determine 
whether it really IS semi-believable, you could do it the hard way.

Note the last nibble of the last byte must contain "A,B,C,D,E, or F" 
(F,A,C,E imply positive). So, you strip off the last nibble and test it for 
greater than 9.

Consider:
01  LTAN PIC S9(7) COMP-3.
01  WAMPUM PIC S9(7) COMP-3.
01  WAHOO-X REDEFINES WAMPUM.
    02  WAHOO PIC 9(7)  COMP-4.

*> bad data in [ ], good data in { }
Move LTAN to WAMPUM.        [20 20 20 20]   {00 00 12 3F}
Move LOW-VALUES to WAHOO-X(1:3).     [00 00 00 20]    {00 00 00 3F}
Multiply WAHOO by 256.       [00 00 02 00]   {00 00 03 F0}
Move LOW-VALUES to WAHOO-X(1:3).        [00 00 00 00]   {00 00 00 F0}
Divide WAHOO by 256.     [00 00 00 00]    {00 00 00 0F}
If WAHOO > 9
   PERFORM WE-HAVE-GOOD-SIGN-NIBBLE
ELSE
  PERFORM SPIT-BURNING-BLOOD-ON-USER
END-IF

Of course this scheme fails if the original data contains "BARF," but you 
get the idea.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 4)_

- **From:** "Mark Vilstrup Svanesteen" <mark.svanesteen(snabela)mail.dk>
- **Date:** 2005-06-10T06:09:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xn0e3bsqfiz15000@news.tele.dk>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com>`

```

> Note the last nibble of the last byte must contain "A,B,C,D,E, or F" 
> (F,A,C,E imply positive). So, you strip off the last nibble and test
> it for greater than 9.

Will try this. I've never worked on COBOL in the byte-level, it will be
interesting to learn something new.

Very generous giving code-examples and all - is it really that obvious
that I haven't worked with COBOL that much? (Java-programmer Learning
COBOL)

Thank you all !

Mark, Denmark
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 4)_

- **From:** "Mark Vilstrup Svanesteen" <mark.svanesteen(snabela)mail.dk>
- **Date:** 2005-06-10T11:54:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xn0e3c1qtcukl8000@news.tele.dk>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com>`

```
> Note the last nibble of the last byte must contain "A,B,C,D,E, or F" 
> (F,A,C,E imply positive). So, you strip off the last nibble and test
…[18 more quoted lines elided]…
> END-IF

Hi again,

Tried some variations of what you suggested, and it seems smart in
theory, but first of all I can't use COMP-4 fields (probably due to my
COBOL-environment)

Anyways, I try with these:

01 copy-of-field 	PIC S9(7) COMP-3.
01 WAMPUM 		PIC s9(7) cOMP-3.
01 WAHOO-X REDIFINES WAMPUM.
	02 WAHOO 	PIC S9(7) COMP.

But, when I multiply, I move 2 places instead of 1.

---------------------
Ex. of my Crap data:

copy gives hex-value: (20 20 20 00)

clear first two:      (00 00 20 00)

multiply gives:       (00 20 00 00)

clear:                (00 00 00 00)

----------------------

Ex. of good data: (value decimal 60)

copy                  (0C 06 00 00)

CLEAR                 (00 00 00 00)

Well, that doesn't get me far.

And why do I get the value (0c 06 00 00) instead of 3C, which gives the
decimal 60.

Sorry, I'm just confused now!

confused Mark, Denmark
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-10T14:49:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118440179.099130.183730@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<xn0e3c1qtcukl8000@news.tele.dk>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com> <xn0e3c1qtcukl8000@news.tele.dk>`

```
> Tried some variations of what you suggested, and it seems smart in
> theory, but first of all I can't use COMP-4 fields (probably due to my
> COBOL-environment)

WHY ARE YOU USING COMP FIELDS AT ALL ????

> Anyways, I try with these:
> 01 copy-of-field        PIC S9(7) COMP-3.

> 01 WAMPUM               PIC s9(7) cOMP-3.
> 01 WAHOO-X REDIFINES WAMPUM.
>        02 WAHOO        PIC S9(7) COMP.

You obviously have no idea what COMP-3 is, nor what COMP is. The
redefine does you no good at all and will simply give you complete
junk.

> Sorry, I'm just confused now!

Use your text editor to replace all instances of "COMP-3" and of "COMP"
with "DISPLAY".
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-11T09:02:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8endv$5v6$1@panix5.panix.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com> <xn0e3c1qtcukl8000@news.tele.dk> <1118440179.099130.183730@z14g2000cwz.googlegroups.com>`

```
In article <1118440179.099130.183730@z14g2000cwz.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>> Tried some variations of what you suggested, and it seems smart in
>> theory, but first of all I can't use COMP-4 fields (probably due to my
>> COBOL-environment)
>
>WHY ARE YOU USING COMP FIELDS AT ALL ????

Mr Plinston, you might be sufficiently courteous to allow for a response 
to an inquiry before offering further advice.

[snip]

>> Sorry, I'm just confused now!
>
>Use your text editor to replace all instances of "COMP-3" and of "COMP"
>with "DISPLAY".

... and do this *before* determining if these occur in a File 
Description... or an area in WORKING-STORAGE that is the object of a READ 
INTO... or as part of a field used to determine numeric validity, as was 
shown in another posting...

... and stand back as your problems reaching deadline vanish... and I can 
assure of this because I am the King of England.

DD
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-06-11T11:38:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11am1l9b2lfabee@corp.supernews.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com> <xn0e3c1qtcukl8000@news.tele.dk> <1118440179.099130.183730@z14g2000cwz.googlegroups.com> <d8endv$5v6$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:d8endv$5v6$1@panix5.panix.com...
> In article <1118440179.099130.183730@z14g2000cwz.googlegroups.com>,
> Richard <riplin@Azonic.co.nz> wrote:
…[7 more quoted lines elided]…
> to an inquiry before offering further advice.

Mr Dwarf, thirty-siz hours had passed since Mr Plinston's
earlier comment. One for which there was no response.

----begin quote
COMP-3 is packed decimal (probably). Why are you accepting data into
COMP-3.  Why would you not have your input fields as DISPLAY ?
----end quote

> [snip]
>
…[8 more quoted lines elided]…
> shown in another posting...

The posting to which Mr Plinston responded showed.

----begin quote
> I have a user input fields:

> 01 VFYS PIC S9(9)V99 COMP-3.
> 01 VMIN PIC S9(5) COMP-3.
> 01 VMAX PIC S9(5) COMP-3.
> 01 LTAN PIC S9(7) COMP-3.
----end quote

This seems unlikely to be any of file, read into, or partial field,
as described above.

Furthermore, I am confused why others would attempt
to impose IBM knowledge (sign nibbles, COMP-4, and
byte-ordering)  on a DEC problem ... the earliest post, under
the subject "Numeric validation", stated "I use cobol v2.7 on
an alpha-system(7.3.1)", for which I take 'alpha-system' to
mean DEC.

As a "Java-programmer Learning COBOL", it is no wonder
that Mr Svanesteen is confused ... but there is hope ... use
DISPLAY instead of COMP-3, as suggested by Mr Plinston.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-11T18:45:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8fphs$bub$1@panix5.panix.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <1118440179.099130.183730@z14g2000cwz.googlegroups.com> <d8endv$5v6$1@panix5.panix.com> <11am1l9b2lfabee@corp.supernews.com>`

```
In article <11am1l9b2lfabee@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:d8endv$5v6$1@panix5.panix.com...
…[17 more quoted lines elided]…
>----end quote

The inquiry to which I referred was the one which immediately preceded my 
reference; my apologies if that was not made sufficiently clear.

>
>> [snip]
…[23 more quoted lines elided]…
>as described above.

Mr Plinston's question (... AT ALL??? (caps original)) appears to expand 
the scope of inquiry beyond the fields mentioned, or so it seems to me... 
once again, my apologies if my interpretation is incorrect.  Mr Plinston's 
specification of 'all instances' appears go to beyond the examples given, 
hence my conclusion.

[snip]

>As a "Java-programmer Learning COBOL", it is no wonder
>that Mr Svanesteen is confused ... but there is hope ... use
>DISPLAY instead of COMP-3, as suggested by Mr Plinston.

There is a difference between using something and globally replacing (my 
interpretation of 'replace all instances', hence my cautions.  A 
'Java-programmer Learning COBOL' might do well to learn the Anciente 
Wisdome of 'Touch other than what is required to solve the problem at the 
possibility of Grave Risk'.

DD
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-11T14:13:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118524387.523109.236830@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<d8endv$5v6$1@panix5.panix.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com> <xn0e3c1qtcukl8000@news.tele.dk> <1118440179.099130.183730@z14g2000cwz.googlegroups.com> <d8endv$5v6$1@panix5.panix.com>`

```
> and do this *before* determining if these occur in a File
> Description... or an area in WORKING-STORAGE that is the object of a READ
> INTO...

Well, actually, I had read all the messages _before_ posting advice,
something that you obviously have not bothered with:

>>> I have a user input fields:
>>> 01 VFYS PIC  S9(9)V99 COMP-3.
>>> 01 VMIN PIC S9(5) COMP-3.
>>> 01 VMAX PIC S9(5) COMP-3.
>>> 01 LTAN PIC S9(7) COMP-3.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-11T18:46:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8fpl3$lup$1@panix5.panix.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <1118440179.099130.183730@z14g2000cwz.googlegroups.com> <d8endv$5v6$1@panix5.panix.com> <1118524387.523109.236830@o13g2000cwo.googlegroups.com>`

```
In article <1118524387.523109.236830@o13g2000cwo.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>> and do this *before* determining if these occur in a File
>> Description... or an area in WORKING-STORAGE that is the object of a READ
…[9 more quoted lines elided]…
>>>> 01 LTAN PIC S9(7) COMP-3.

I had not read enough messages to learn that 'all instances' is supposed 
to be read as 'all instances shown in the samples given'... and I doubt, 
severely, that enough messages exist to convince me that this is a good 
practise.

DD
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-10T21:36:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11akjhr3u18hg1b@news.supernews.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk> <11agl4rndpi6n72@news.supernews.com> <xn0e3c1qtcukl8000@news.tele.dk>`

```
Mark Vilstrup Svanesteen wrote:
>> Note the last nibble of the last byte must contain "A,B,C,D,E, or F"
>> (F,A,C,E imply positive). So, you strip off the last nibble and test
…[24 more quoted lines elided]…
> COBOL-environment)

COMP-4 is implementor-defined. I meant it to be straight binary.

>
> Anyways, I try with these:
…[11 more quoted lines elided]…
> copy gives hex-value: (20 20 20 00)

This is a bizarre result.

>
> clear first two:      (00 00 20 00)

Clear first two? I cleared the first three.

>
> multiply gives:       (00 20 00 00)
…[7 more quoted lines elided]…
> copy                  (0C 06 00 00)

Impossible. 60 = 00 00 06 0C

>
> CLEAR                 (00 00 00 00)
…[8 more quoted lines elided]…
> confused Mark, Denmark

Well, work with what you've got. If YOUR comp-3 numbers look like 60 = 0C 06 
00 00, do whatever's necessary to isolate the "C" nibble and test it.

You've probably got an Intel chip where [ab cd ef gh] => [dc ba hg fe] when 
viewed in hex.
```

###### ↳ ↳ ↳ Re: Numeric validation revisited

- **From:** "Ron" <NoSpam@SpamSucks.Org>
- **Date:** 2005-06-09T18:31:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UZSdneO5-bz1TDXfRVn_vg@giganews.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com> <xn0e3ahic210pz000@news.tele.dk>`

```
> Ok, I tried to avoid a long problem-definition, but I can now see my
> problem is not that easily defined. So, here we go again:
…[6 more quoted lines elided]…
> 01 LTAN PIC S9(7) COMP-3.

How does data get in these fields in the first place? I doubt users are entering
packed decimal data directly. Are your reading from a screen? Moving from
a record or what? I am going to take a pure guess here that you're reading from
a screen and moving into these packed fields. Here's how I would edit the screen
input. I make the assumption that the screen input field can contain 5 characters
plus a sign at end if they want it negative since that's how your fields are defined.
I do not like to use function numval because at least on the IBM mainframe the stupid
thing abends if the data is not valid to start with making it useless for the most part.

This is technique I use quite a bit and should work for most any size field. But I
have not compiled the exact code I've put here so suggestions for improvements
or noting dumb syntax errors welcome from the peanut gallery.


01 inp-x  pic x(6).
01 inp-9 pic S9(5) sign trailing separate.
01 inp-work redefines inp-9.
     05 inp-data pic x(5) justified right.
     05 inp-sign pic x.
01 tally-c pic 9(4) comp.
01 beg-char pic 9(4) comp.
01 end-char pic 9(4) comp.

move spaces to inp-x.
perform make-them-enter-something-into-inp-x.
if inp-x = spaces
  display 'Enter something dumbhead'
  go to p-exit
end-if.

* find the first non-blank
move zero to tally-c.
inspect inp-x tallying tallyc-c for leading spaces.
compute beg-char = tally-c + 1

* find the last non-blank
move zero to tally-c.
inspect function reverse (inp-x) tallying tally-c for leading spaces.
compute end-char = length of inp-x - tally-c.

* are there any imbedded blanks
move zero to tally-c.
inspect input-c (beg-char: end-char - beg-char + 1)
 tallying tally-c for all spaces.
If tally-c > zero
  display 'What kind of junk is this?'
  go to p-exit
end-if.

move spaces to inp-work.

* did they enter a sign
if inp-c (end-char:) = '+' or '-'
  move inp-c (end-char:) to inp-sign
  subtract 1 from end-char
else
  move '+' to inp-sign
end-if.

* move it to the work area
move inp-c (beg-char: end-char - beg-char + 1) to inp-data.
inspect inp-data converting spaces to zeros.

* Now FINALLY
if inp-9 is numeric
   move inp-9 to VMIN
else
   display 'Will you stop entering this crap?'
end-if.

p-exit.
    exit.
```

##### ↳ ↳ Re: Numeric validation

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2005-06-09T09:11:48-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<clcfa1dvfes1ta3qa24vcu20m12ftvgp4s@4ax.com>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk> <wv6dnaW8Feu75zrfRVn_vg@giganews.com>`

```
On Wed, 8 Jun 2005 18:07:17 -0500, "Ron" <NoSpam@SpamSucks.Org> wrote:

>I am not sure what you are trying to accomplish. I know lot's of people
>are going to say comp-3 is implementor dependant, but comp-3 is almost
…[18 more quoted lines elided]…
>                        X'12345F' NOT Numeric
For IBM COBOL compilers for the z series (nee 390, etc.) whether the
previous value is numeric depends on the NUMPROC option.  If your shop
uses CSP and possibly some other software, the NUMPROC option should
treat it as numeric.
>                        X'020202' NOT Numeric
>                        X'1234AD' NOT Numeric
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Numeric validation

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2005-06-08T20:26:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42a7b7e4$1_1@spool9-west.superfeed.net>`
- **References:** `<xn0e399p0e5qps000@news.tele.dk>`

```
"Mark V. Svanesteen"  wrote:

[snip]

> My frustration is complete and I'm too far behind schedule, please help
> me get a fool-proof way of testing for bad data in numeric edited
> fields.

First, as others have pointed out, the field you gave in your example is not
numeric edited.  I assume you are asking how to check for valid data in a
numeric data item with usage COMP-3.

Next, COBOL doesn't define what constitutes valid data in a COMP-3 data
item, so it's up to your compiler's implementor to define that and, maybe,
give you a way to test for it.

Finally, as you have perhaps noticed, the NUMERIC class test might be
problematic when applied to a COMP-3 data item.  In standard [1985] COBOL,
you can't do that (even if use a standard usage, such as PACKED-DECIMAL).
If you test for NUMERIC on a COMP-3 field, you are at the mercy of whatever
your particular compiler does for that test.  If you want to reliably test a
numeric data item for valid contents using the NUMERIC class test, the item
must have usage DISPLAY, in other words, it can't be COMP or COMP-3.

So I'm afraid the answer to your question will be specific to the compiler
and platform you are using.

Walter



----== Posted via Newsfeeds.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
