[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The actual value of LOW-VALUES

_29 messages · 17 participants · 2003-07_

---

### The actual value of LOW-VALUES

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2003-07-02T00:50:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com>`

```
I'm curious about the implementation of LOW-VALUES on systems other than my
own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
implemented as binary zero (all zero bits) in a character. Is that
commonplace among other compilers and systems? What other possibilities are
out there?
```

#### ↳ Re: The actual value of LOW-VALUES

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-02T01:02:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com>`

```

"Douglas Gallant" <no@spam.net> wrote in message
news:S%pMa.29299$8B.3874@twister.nyroc.rr.com...
| I'm curious about the implementation of LOW-VALUES on systems other than
my
| own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
| implemented as binary zero (all zero bits) in a character. Is that
| commonplace among other compilers and systems? What other possibilities
are
| out there?
|

In IBM COBOL, low-values is the same thing.
I doubt that there are any differences on other platforms.
```

##### ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-07-06T22:37:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net...
>
> "Douglas Gallant" <no@spam.net> wrote in message
…[11 more quoted lines elided]…
> I doubt that there are any differences on other platforms.

AS POINTED OUT EARLIER IN THIS THREAD...

'LOW-VALUE[S]' is *NOT* a fixed value. it is *NOT* implementor-defined. It
is *NOT*  hardware-defined. It is defined as the "lowest value in the
program collating sequence."

Not that I can imagine anyone using a collating sequence in which the lowest
element would be other than 0x00, but it *is* possible!

MCM
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-06T23:27:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com...
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
| news:0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net...
…[3 more quoted lines elided]…
| > | I'm curious about the implementation of LOW-VALUES on systems other
than
| > my
| > | own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
| > | implemented as binary zero (all zero bits) in a character. Is that
| > | commonplace among other compilers and systems? What other
possibilities
| > are
| > | out there?
…[9 more quoted lines elided]…
| program collating sequence."

Correct.
I was wrong, Again.

|
| Not that I can imagine anyone using a collating sequence in which the
lowest
| element would be other than 0x00, but it *is* possible!
|

Someone will do it, in order to say they did it.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-07T12:04:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f08b99a_6@news.athenanews.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net...
>
> Someone will do it, in order to say they did it.
>
>
Hmmm...I wonder who <G>?
(Definitely NOT me...I'm not bright enough to mess with collating
sequences....)
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-07T14:27:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f08b99a_6@news.athenanews.com...
|
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[8 more quoted lines elided]…
|

You start with a programmer who wants to prove that they are smarter than
everyone else, and so they write a program that only they can maintain (or
so they think).
OR
Someone fits a problem to the solution. ("I've never used it, and wanted to
try it".)

I'm never amazed at what I might find in a system.
Misuse of features doesn't occur that often, but sometimes I run across a
square peg solidly lodged in a round hole.
```

###### ↳ ↳ ↳ Alternate Collating sequences was Re: The actual value of LOW-VALUES

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-07-07T15:28:37-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F09BBD5.84D98306@istar.ca>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net>`

```
In the discussion below the alternate collating sequence may be for a
sort.  I know that both major mainframe SORT packages have an ALTSEQ
provision.  I have never used it but it is there.  Also, someone may
have EBCDIC data and want it sorted in ASCII (ISO) sequence or vice
versa.  The function may also be used in a COBOL program to get the
compares in a desired sequence that is not the same as the EBCDIC or
ASCII sequence.

See discussion below fro background, no further comments

Harley wrote:
> 
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[22 more quoted lines elided]…
> square peg solidly lodged in a round hole.
```

###### ↳ ↳ ↳ Re: Alternate Collating sequences was Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-08T01:12:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oUoOa.43554$0v4.2996600@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net> <3F09BBD5.84D98306@istar.ca>`

```

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3F09BBD5.84D98306@istar.ca...
| In the discussion below the alternate collating sequence may be for a
| sort.  I know that both major mainframe SORT packages have an ALTSEQ
…[4 more quoted lines elided]…
| ASCII sequence.

It's a little bit more powerful.
You mention legitimate uses, but there are others.
Given some idle time, and a desire to fool around you could create a
masterpiece, or a nightmare.

<<snip>>

Here's what the IBM Manual says regarding ALPHABET IS.
I have inserted some comments (== precedes comments).

== this is the programmer controlled option.
literal-1
literal-2
literal-3
Specifies that the collating sequence for alphanumeric data is determined
by the program, according to the following rules:
 The order in which literals appear specifies the ordinal number, in
ascending sequence, of the character(s) in this collating sequence.
 Each numeric literal specified must be an unsigned integer.
 Each numeric literal must have a value that corresponds to a valid
ordinal position within the collating sequence in effect.
Appendix C, "EBCDIC and ASCII collating sequences" on page 522,
lists the ordinal number for characters in the single-byte EBCDIC and
ASCII collating sequences.

 Each character in an alphanumeric literal represents that actual
character in the character set. (If the alphanumeric literal contains
more than one character, each character, starting with the leftmost, is
assigned a successively ascending position within this collating
sequence.)
==  Another part of the manual ==

Hexadecimal notation for alphanumeric literals
Hexadecimal notation can be used for alphanumeric literals. Hexadecimal
notation
has the following format:
Format 3 - Hexadecimal notation for alphanumeric literals
X"hexadecimal-digits"
X'hexadecimal-digits'
X" or X'
The opening delimiter for hexadecimal notation of an alphanumeric literal.
== End of other part of manual ==

 Any characters that are not explicitly specified assume positions in this
collating sequence higher than any of the explicitly specified characters.
The relative order within the set of these unspecified characters within the
character set remains unchanged.

 Within one alphabet-name clause, a given character must not be
specified more than once.

 Each alphanumeric literal associated with a THROUGH or ALSO
phrase must be 1 character in length.

 When the THROUGH phrase is specified, the contiguous characters in
the native character set beginning with the character specified by
literal-1 and ending with the character specified by literal-2 are
assigned successively ascending positions in this collating sequence.
This sequence can be either ascending or descending within the
original native character set. That is, if "Z" THROUGH "A" is
specified, the ascending values, left-to-right, for the uppercase letters
are:
ZYXWVUTSRQPONMLKJIHGFEDCBA

== nobody will ever do this?

 When the ALSO phrase is specified, the characters specified as literal-1,
literal-3, etc., are assigned to the same position in this collating
sequence. For example, if you specify:
"D" ALSO "N" ALSO "%"
the characters D, N, and % are all considered to be in the same
position in the collating sequence.

== You could specify    "A" also "a" etc. which might come in handy.

 When the ALSO phrase is specified and alphabet-name-1 is referenced
in a SYMBOLIC CHARACTERS clause, only literal-1 is used to
represent the character in the character set.

 The character having the highest ordinal position in this collating
sequence is associated with the figurative constant HIGH-VALUE. If
more than one character has the highest position, because of
specification of the ALSO phrase, the last character specified (or
defaulted to when any characters are not explicitly specified) is
considered to be the HIGH-VALUE character for procedural statements
such as DISPLAY, or as the sending field in a MOVE statement. (If all
characters and the ALSO phrase example given above were specified
as the high-order characters of this collating sequence, the
HIGH-VALUE character would be %.)

 The character having the lowest ordinal position in this collating
sequence is associated with the figurative constant LOW-VALUE. If
more than one character has the lowest position, because of
specification of the ALSO phrase, the first character specified is the
LOW-VALUE character. (If the ALSO phrase example given above
were specified as the low-order characters of the collating sequence,
the LOW-VALUE character would be D.)

== It seems that someone could have a LOW-VALUE of x"FF",
and a HIGH-VALUE of x'00'.

==In the real world, I would like to think that nobody will use this to have
some fun, but that may not be the case.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 6)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2003-07-09T08:38:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.hhrcg50.pminews@News.CIS.DFN.DE>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net>`

```
On Mon, 07 Jul 2003 14:27:02 GMT, Harley wrote:

>
>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[23 more quoted lines elided]…
>

I have used it. Here in Spain, we have a nice letter "�" that in the Spanish
alphabet comes between the "n" and the "o".
This feature solves this problem, but unfortunately we had a few more. The
combinations "CH", "LL" and "RR" were seen as different letters, so sorting a
list of names beginning with "C" had to be in the following order.
First "CA" through "CG", then "CI" through CZ" and then "CH".

I am sure that other languages with special alphabets will have similar
probles (German, Danish, Swedish...)
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-09T12:54:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfUOa.46067$3o3.3119195@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net> <jvyyrzubevmbagrfvasbezngvpnpbz.hhrcg50.pminews@News.CIS.DFN.DE>`

```

"Willem Clements" <willem@horizontes-informatica.com> wrote in message
news:jvyyrzubevmbagrfvasbezngvpnpbz.hhrcg50.pminews@News.CIS.DFN.DE...
On Mon, 07 Jul 2003 14:27:02 GMT, Harley wrote:

>
>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[23 more quoted lines elided]…
|>

|I have used it. Here in Spain, we have a nice letter "�" that in the
Spanish
|alphabet comes between the "n" and the "o".
|This feature solves this problem, but unfortunately we had a few more. The
|combinations "CH", "LL" and "RR" were seen as different letters, so sorting
a
|list of names beginning with "C" had to be in the following order.
|First "CA" through "CG", then "CI" through CZ" and then "CH".

|I am sure that other languages with special alphabets will have similar
|probles (German, Danish, Swedish...)

I can see using it for sequencing names, and I do understand that the
EBCDIC, and ASCII alphabets sometimes fall short.
I wonder what they do in Russia.

Even when there are no differences between the alphabet and EBCDIC/ASCII
character sets, you may want to have Upper, and Lower case letters in a
sequence other than the default sequence.
i.e. "A" also "a", etc. or "AaBb" etc.

I hope that when these situations arise the solution is implemented in a
manner that doesn't cause confusion (like the 'Z' thru "A" scenario).
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "Nico de Jong" <nico@DUMPTHISfarumdata.dk>
- **Date:** 2003-07-20T19:25:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DnASa.82$qE3.5@news.get2net.dk>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <WqfOa.42819$0v4.2940170@bgtnsc04-news.ops.worldnet.att.net> <jvyyrzubevmbagrfvasbezngvpnpbz.hhrcg50.pminews@News.CIS.DFN.DE>`

```
"Willem Clements" <willem@horizontes-informatica.com> skrev i en meddelelse
news:jvyyrzubevmbagrfvasbezngvpnpbz.hhrcg50.pminews@News.CIS.DFN.DE...
>I have used it. Here in Spain, we have a nice letter "ï¿½" that in the
Spanish
>alphabet comes between the "n" and the "o".
>This feature solves this problem, but unfortunately we had a few more. The
>combinations "CH", "LL" and "RR" were seen as different letters, so sorting
a
>list of names beginning with "C" had to be in the following order.
>First "CA" through "CG", then "CI" through CZ" and then "CH".

>I am sure that other languages with special alphabets will have similar
>probles (German, Danish, Swedish...)

Quite so. We have the letters ï¿½ ï¿½ ï¿½, which are located behind the Z. The
EBCDIC values for these letters are # @ and $. Furthermore, the letters AA
(like in the surname HAASE) is to be sorted as Hï¿½SE, because the double A
was changed to ï¿½ back in 1948. However, familynames with AA were permitted
to exist. So if you want to find someone with AA in the danish telephone
directories, look behind ï¿½ and ï¿½ ...

Nico
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-08T12:58:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f08b99a_6@news.athenanews.com...
|
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[8 more quoted lines elided]…
|

Look at this:
 When the THROUGH phrase is specified, the contiguous characters in
the native character set beginning with the character specified by
literal-1 and ending with the character specified by literal-2 are
assigned successively ascending positions in this collating sequence.
This sequence can be either ascending or descending within the
original native character set. That is, if "Z" THROUGH "A" is
specified, the ascending values, left-to-right, for the uppercase letters
are:
ZYXWVUTSRQPONMLKJIHGFEDCBA

If you do this, you can flip the GREATER THAN/LESS THAN relationship testing
of alphanumeric data.
It doesn't take much work.
Wouldn't you just LOVE to see someone do it?
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-07-08T08:33:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beeo8o$u4c$1@si05.rsvl.unisys.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net...

> Look at this:
>  When the THROUGH phrase is specified, the contiguous characters in
…[9 more quoted lines elided]…
> If you do this, you can flip the GREATER THAN/LESS THAN relationship
testing
> of alphanumeric data.
> It doesn't take much work.
> Wouldn't you just LOVE to see someone do it?

It's been "do-able" in standard COBOL since ANSI X3.23-1974 (see page II-10,
3.1.3.4 SPECIAL-NAMES General Rules (3)d Rule 4).  Surely *somebody's* done
it in the last thirty years!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-08T18:25:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<befju0$8co$1@slb2.atl.mindspring.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net> <beeo8o$u4c$1@si05.rsvl.unisys.com>`

```
And if one REALLY wants to get "obscure" you should look at one of the
"Substantive" changes in the 2002 Standard.  According to page 831,

"136) THROUGH phrase in VALUE clause and EVALUATE statement. A collating
sequence can be identified in the THROUGH phrase for use in determining a
range of values. This allows use of portable ranges across various
implementations. It also allows the range to be determined from a locale,
which is not necessarily portable when different locales are used."
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-09T00:49:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qEJOa.44982$0v4.3100953@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net> <beeo8o$u4c$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:beeo8o$u4c$1@si05.rsvl.unisys.com...
|
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[9 more quoted lines elided]…
| > specified, the ascending values, left-to-right, for the uppercase
letters
| > are:
| > ZYXWVUTSRQPONMLKJIHGFEDCBA
…[7 more quoted lines elided]…
| It's been "do-able" in standard COBOL since ANSI X3.23-1974 (see page
II-10,
| 3.1.3.4 SPECIAL-NAMES General Rules (3)d Rule 4).  Surely *somebody's*
done
| it in the last thirty years!
|

Luckily, I haven't had to maintain it.

I wonder how many hits you would get for ALPHABET if you scanned the source
libraries of a few companies.
Thank the deity of your choice this isn't used frequently.
I can see legitimate uses, like "AaBbCc...etc. to sort names, but I think
people use other methods.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 6)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-07-08T16:18:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7IFOa.6229$Ag6.274805@news20.bellglobal.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[24 more quoted lines elided]…
> If you do this, you can flip the GREATER THAN/LESS THAN relationship
testing
> of alphanumeric data.
> It doesn't take much work.
> Wouldn't you just LOVE to see someone do it?
>

I wonder if it works with Isam file keys?  You could write out an Isam file
key file with the colating sequence reversed, then a normal program could
read it backwards.

Donald
;<)
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-09T12:00:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0b5bac_1@news.athenanews.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net...
>
> Wouldn't you just LOVE to see someone do it?
>
No.

(With the encroaching old age and grumpiness, I no longer  have a sense of
fun and my sense of humopur is atrophying. HARRRUMMPHHHHH!!)

Pete.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-09T00:41:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DwJOa.44972$0v4.3100976@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net> <3f08b99a_6@news.athenanews.com> <ydzOa.44870$3o3.3014987@bgtnsc05-news.ops.worldnet.att.net> <3f0b5bac_1@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f0b5bac_1@news.athenanews.com...
|
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[8 more quoted lines elided]…
|
LOL.

I still have my sense of humor, and sometimes laugh at something in a
program.
Some find it strange, others laugh with me.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-07T10:29:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_hmdnfZFzOVBDJSiXTWJjg@giganews.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <8f2Oa.40387$0v4.2877543@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:
>
> Someone will do it, in order to say they did it.

I ran across a subroutine in FORTRAN made exclusively of a varying number of
dollar signs:

e.g.
$$$ = SQRT($$ + $$$$**2)
$$$ = $$ + 1.2345

I ran across another, this time in assembly, where the programmer used a lot
of special characters in variable names - many of which were unprintable
(and the print train wrapped them to something else). Of course, we were
looking at a listing.....
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-07T00:17:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f08baa7.38997447@news.optonline.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:

>"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
>news:0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net...
…[22 more quoted lines elided]…
>element would be other than 0x00, but it *is* possible!

Burroughs Medium Systems (natively EBCDIC) defined low-values as spaces, because
space is the lowest in the "COBOL character set". It defined high values as 9s
X'F9'. The formerly-Burroughs side of Unisys no longer does that.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

_(reply depth: 4)_

- **From:** "Elaine Muraskin" <emuraskin@nyc.rr.com>
- **Date:** 2003-07-07T02:38:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l25Oa.6831$351.3283123@twister.nyc.rr.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <0bqMa.32177$3o3.2334235@bgtnsc05-news.ops.worldnet.att.net> <Tw1Oa.12886$BM.4044144@newssrv26.news.prodigy.com> <3f08baa7.38997447@news.optonline.com>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3f08baa7.38997447@news.optonline.com...
> "Michael Mattias" <michael.mattias@gte.net> wrote:
>
…[5 more quoted lines elided]…
> >> | I'm curious about the implementation of LOW-VALUES on systems other
than
> >> my
> >> | own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
> >> | implemented as binary zero (all zero bits) in a character. Is that
> >> | commonplace among other compilers and systems? What other
possibilities
> >> are
> >> | out there?
…[7 more quoted lines elided]…
> >'LOW-VALUE[S]' is *NOT* a fixed value. it is *NOT* implementor-defined.
It
> >is *NOT*  hardware-defined. It is defined as the "lowest value in the
> >program collating sequence."
> >
> >Not that I can imagine anyone using a collating sequence in which the
lowest
> >element would be other than 0x00, but it *is* possible!
>
> Burroughs Medium Systems (natively EBCDIC) defined low-values as spaces,
because
> space is the lowest in the "COBOL character set". It defined high values
as 9s
> X'F9'. The formerly-Burroughs side of Unisys no longer does that.

I worked on a Honeywell 1200 machine between 1973-1977. IIRC, LOW-VALUES
were spaces and HIGH-VALUES were ampersands. The only time this was a
problem was when the company bought the McCormack and Dodge Accounts Payable
System, written in IBM COBOL.  (The entire source code was delivered to me
on punch cards.)   I had to change the transaction sorts because it expected
"9999"s to sort last.
Elaine.
```

#### ↳ Re: The actual value of LOW-VALUES

- **From:** "Schroeder" <jfriedman@nc.rr.com>
- **Date:** 2003-07-02T03:59:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jMsMa.124204$_w.6559354@twister.southeast.rr.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com>`

```
I believe the only way you can get other than binary zeroes for LOW-VALUES
is to define your own alphabet and use it as the program collating sequence
and make the first character in that alphabet other than X"00".

Jeff Friedman

"Douglas Gallant" <no@spam.net> wrote in message
news:S%pMa.29299$8B.3874@twister.nyroc.rr.com...
> I'm curious about the implementation of LOW-VALUES on systems other than
my
> own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
> implemented as binary zero (all zero bits) in a character. Is that
> commonplace among other compilers and systems? What other possibilities
are
> out there?
>
>
```

##### ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-01T23:29:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdtn4a$hdi$1@slb2.atl.mindspring.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <jMsMa.124204$_w.6559354@twister.southeast.rr.com>`

```
It may be "urban legand" - but I think I heard of a COBOL (somewhere) that
ran on an operating system where the "space" was the LOWEST collating
sequence character - in which case LOW-VALUES would have pointed to that (by
default).  It is always (well at least from the '85 and I think '74
Standards) to "define" your own collating sequence within your source code
and then LOW-VALUES changes (when using that named alphabet as a collating
sequence) accordingly.

Certainly "binary zeroes" is by FAR the most common value for Low-Values.
Similarly, today X"FF" is (I believe) the most common value for
HIGH-VALUES - although their are still some "environments" where X"7F" is
used as HIGH-VALUES.
```

#### ↳ Re: The actual value of LOW-VALUES

- **From:** "Jim Morcombe" <jim@byronics.com.au>
- **Date:** 2003-07-02T15:17:02+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdu0ep$jfs$1@yeppa.connect.com.au>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com>`

```
As far as I am aware, this is the definition of LOW-VALUES.
That is, it will always be binary ZEROs.

Likewise, HI-VALUES will always be binary ONEs.

Jim

Douglas Gallant <no@spam.net> wrote in message
news:S%pMa.29299$8B.3874@twister.nyroc.rr.com...
> I'm curious about the implementation of LOW-VALUES on systems other than
my
> own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
> implemented as binary zero (all zero bits) in a character. Is that
> commonplace among other compilers and systems? What other possibilities
are
> out there?
>
>
```

##### ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-02T19:44:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F037C87.80005@Netscape.net>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <bdu0ep$jfs$1@yeppa.connect.com.au>`

```
Jim Morcombe wrote:
> As far as I am aware, this is the definition of LOW-VALUES.
> That is, it will always be binary ZEROs.
> 
> Likewise, HI-VALUES will always be binary ONEs.

This isn't the way the COBOL 85 compiler works on the Unisys 2200.  If 
you use certain COMPAT options (COMPAT/FULL is pretty much necessary 
because of some differently-moded subsystems most folks interface with), 
you can get either 177 or 377.  The first, in actuality, equates to 1/4 
the highest value, and the second (the default with no COMPAT) is 1/2 
the highest value.

I thought I was going crazy when I defined a Pic 9(05) Binary (see other 
Unisys thread for history on that), and said "Move High-Values to 
Half-Word", then displayed half-word - I got 131,076 (which is 1/2 of 
262,143, the expected result).  I e-mailed a guy at Unisys, and he 
pointed me to the (2 ** [bits]) - 1 formula.

If PC-based compilers handle that differently, I'm happy to hear it.  :)
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-07-07T07:49:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bec19u$20to$1@si05.rsvl.unisys.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <bdu0ep$jfs$1@yeppa.connect.com.au> <3F037C87.80005@Netscape.net>`

```
"LX-i" <LXi0007@Netscape.net> wrote in message
news:3F037C87.80005@Netscape.net...

> I thought I was going crazy when I defined a Pic 9(05) Binary (see other
> Unisys thread for history on that), and said "Move High-Values to
> Half-Word", then displayed half-word - I got 131,076 (which is 1/2 of
> 262,143, the expected result).  I e-mailed a guy at Unisys, and he
> pointed me to the (2 ** [bits]) - 1 formula.

The format and content of USAGE COMP is always defined by the implementor.
The same is true for USAGE BINARY (introduced in the '85 standard).

    -Chuck Stevens
```

#### ↳ Re: The actual value of LOW-VALUES

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-07-02T07:31:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bduqc7$1rmt$1@si05.rsvl.unisys.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com>`

```
"Douglas Gallant" <no@spam.net> wrote in message
news:S%pMa.29299$8B.3874@twister.nyroc.rr.com...
> I'm curious about the implementation of LOW-VALUES on systems other than
my
> own (Unisys 2200/ClearPath IX). On the Unisys systems, LOW-VALUES is
> implemented as binary zero (all zero bits) in a character. Is that
> commonplace among other compilers and systems? What other possibilities
are
> out there?

The standards of the language apply here.

ANSI X3.23-1974:  "Represents one or more of the character that has the
lowest ordinal position in the program collating sequence."

ANSI X3.23-1985:  "Except in the SPECIAL-NAMES paragraph, represents one or
more of the character that has the lowest ordinal position in the program
collating sequence."

The wording from ISO/IEC 1989:2002 is rather more complex, involving as it
does locales, but the concepts are consistent.

In an 8-bit encoding system in which there are 256 characters in the program
collating sequence and in which the default collating sequence is in use, it
strikes me as unlikely that LOW-VALUES would have a value higher than @00@,
the hex representation of the lowest character in that set of 256
characters.  I don't know how I'd reconcile such a situation with the
requirements of the standards.

    -Chuck Stevens
```

##### ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-07-02T19:30:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BSmdnbrWNZS19p6iXTWJkg@comcast.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <bduqc7$1rmt$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:bduqc7$1rmt$1@si05.rsvl.unisys.com...
> "Douglas Gallant" <no@spam.net> wrote in message
> news:S%pMa.29299$8B.3874@twister.nyroc.rr.com...
…[13 more quoted lines elided]…
> ANSI X3.23-1985:  "Except in the SPECIAL-NAMES paragraph, represents one
or
> more of the character that has the lowest ordinal position in the program
> collating sequence."
…[4 more quoted lines elided]…
> In an 8-bit encoding system in which there are 256 characters in the
program
> collating sequence and in which the default collating sequence is in use,
it
> strikes me as unlikely that LOW-VALUES would have a value higher than
@00@,
> the hex representation of the lowest character in that set of 256
> characters.  I don't know how I'd reconcile such a situation with the
…[4 more quoted lines elided]…
>

    I am not certain, but I think that some Cobols used to work differently
when dealing with a numeric field, eg moving the lowest LEGAL value.
```

###### ↳ ↳ ↳ Re: The actual value of LOW-VALUES

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-07-07T07:46:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bec13n$20lv$1@si05.rsvl.unisys.com>`
- **References:** `<S%pMa.29299$8B.3874@twister.nyroc.rr.com> <bduqc7$1rmt$1@si05.rsvl.unisys.com> <BSmdnbrWNZS19p6iXTWJkg@comcast.com>`

```

"Russell Styles" <RWS0202@comcast.net> wrote in message
news:BSmdnbrWNZS19p6iXTWJkg@comcast.com...

>     I am not certain, but I think that some Cobols used to work
differently
> when dealing with a numeric field, eg moving the lowest LEGAL value.

If they did it would have been an extension in which the implementor defined
(or even failed to define) the consequences.  Also, this definition might
present problems with signed fields; do you mean the lowest legal MAGNITUDE?
And if so, is the sign positive or negative?

LOW-VALUES is defined in standard COBOL as a character-based entity.
Essentially, I *believe* a statement like MOVE LOW-VALUES TO NUMERIC-ITEM is
handled as if LOW-VALUES is supposed to produce the same results as:
    01  NUMERIC-ITEM PIC S9(5)V99.
    01  TEMP-FIELD PIC X(5).
    01  TEMP-FIELD-NUMERIC REDEFINES TEMP-FIELD PIC 9(5).
    ...
     MOVE LOW-VALUES TO TEMP-FIELD.
     MOVE TEMP-FIELD-NUMERIC TO NUMERIC-ITEM.

Note that the results of the first MOVE are defined, but the results of the
second are not.  For a numeric data item, "its content when expressed in
standard data format must be one or more numeric characters  ..."  Only in
implementations and operating environments in which the bit pattern of the
character that LOW-VALUES represents also happens to represent a numeric
character are the results of the second MOVE defined in standard COBOL, and
that's not true for either ASCII or EBCDIC.

The LOWEST-ALGEBRAIC function was introduced in the 2002 standard at least
in part to provide a standard mechanism for determining the lowest legal
value for a given numeric field.

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
