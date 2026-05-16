[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right justifying (arbitrary) alphanumeric input

_24 messages · 11 participants · 2005-02 → 2005-03_

---

### Right justifying (arbitrary) alphanumeric input

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-28T21:15:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gSLUd.3656529$f47.654009@news.easynews.com>`

```
Quite a while ago, we had a long discussion about various methods of "right 
justifying" alphanumeric data.  See (for example)

   http://objectz.com/faqs/cobolfaq.htm#Sample_right

When we talked about it, I know "we all" agreed that the "JUST RIGHT' wouldn't 
help in a MOVE *unless* you knew how much non-space data there was.  However, 
someone sent me some source code (off-list) and I can't see anything wrong with 
this (from a Standard conforming) point of view.  Although there may (or may 
not) be better PERFORMING code, does anyone see any problems with the following 
technique?

IDENTIFICATION DIVISION.
PROGRAM-ID. TESTPROG.
DATA DIVISION.
WORKING-STORAGE SECTION.
01    TEST-VARIABLES.
        04 INPUT-VALUE PIC X(22) VALUE 'MYTESTVALUE'.
        04 OUT-VALUE PIC X(22) JUST RIGHT.
        04 DUMMY-VALUE PIC X(22).
PROCEDURE DIVISION.
 0000-MAIN SECTION.
        DISPLAY INPUT-VALUE.
        UNSTRING INPUT-VALUE DELIMITED BY SPACES
                INTO OUT-VALUE DUMMY-VALUE.
         DISPLAY OUT-VALUE.
        STOP RUN.
```

#### ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-02-28T22:54:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com>`

```
On Mon, 28 Feb 2005 21:15:56 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Quite a while ago, we had a long discussion about various methods of "right 
>justifying" alphanumeric data.  See (for example)
…[15 more quoted lines elided]…
>        04 INPUT-VALUE PIC X(22) VALUE 'MYTESTVALUE'.
If input-value is instead
        04 INPUT-VALUE PIC X(22) VALUE 'MY TEST VALUE'.
The unstring will not yeld the expected results.

>        04 OUT-VALUE PIC X(22) JUST RIGHT.
>        04 DUMMY-VALUE PIC X(22).
…[6 more quoted lines elided]…
>        STOP RUN.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** "Ron" <NoSpam@SpamStopper.Org>
- **Date:** 2005-02-28T18:13:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<762dne6b0dIqLr7fRVn_vQ@giganews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com>`

```
>>01    TEST-VARIABLES.
>>        04 INPUT-VALUE PIC X(22) VALUE 'MYTESTVALUE'.
…[4 more quoted lines elided]…
>>        04 OUT-VALUE PIC X(22) JUST RIGHT.


I still think the best way to do this is:

move zero to tally-count.
inspect function reverse (input-value) tallying tally-count for leading spaces.
move input-value (1 : length of input-value - tally-count) to out-value.

out-value will contain '         MY TEST VALUE'
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-03-01T08:10:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<up8821999g81q9lmp5ujdmr0npbiqdtrl8@4ax.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com>`

```
On Mon, 28 Feb 2005 18:13:42 -0600, "Ron" <NoSpam@SpamStopper.Org>
wrote:

>>>01    TEST-VARIABLES.
>>>        04 INPUT-VALUE PIC X(22) VALUE 'MYTESTVALUE'.
…[13 more quoted lines elided]…
>out-value will contain '         MY TEST VALUE'
It is if your compiler supports "function reverse" Not all do.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-03-01T08:21:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d024r5$2jkc$1@si05.rsvl.unisys.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <up8821999g81q9lmp5ujdmr0npbiqdtrl8@4ax.com>`

```

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:up8821999g81q9lmp5ujdmr0npbiqdtrl8@4ax.com...

> It is if your compiler supports "function reverse" Not all do.

It's a requirement for compliance with ANSI X3.23-1985 as amended by ANSI
X3.23a-1989, the Intrinsic Function Amendment.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-01T17:37:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kL1Vd.3443288$B07.538680@news.easynews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <up8821999g81q9lmp5ujdmr0npbiqdtrl8@4ax.com> <d024r5$2jkc$1@si05.rsvl.unisys.com>`

```
Sorry Chuck - but you are in error.

The '89 Amendment introduced the Intrinsic Function module as OPTIONAL.  FIPS, 
on the other hand, made it enquired in their Standard. Therefore, a "fully 
conforming High level - amended third Standard COBOL" need not implement it.

The *really* odd thing about the '89 Amendment was that it didn't even make 
"function" a reserved word UNLESS you implemented the Intrinsic Function module. 
This was changed in '91 by the "Corrections Amendment" where it was made 
reserved whether or not you implemented that module.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-03-01T14:54:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9S1Am6GuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com>`

```
.    On  28.02.05
  wrote  NoSpam@SpamStopper.Org (Ron)
     on  /COMP/LANG/COBOL
     in  762dne6b0dIqLr7fRVn_vQ@giganews.com
  about  Re: Right justifying (arbitrary) alphanumeric input


N> inspect function reverse (input-value)
N>             tallying tally-count for leading spaces.


   The INSPECT statement would need a REVERSE option so that it would  
scan from the end of the variable, instead of from the beginning, and  
one would not need to create a (temporary) reversed string.



Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Wir wohnen in Gï¿½ttingen in Scheiterhaufen, die mit Tï¿½ren und Fenstern versehen sind. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-03-01T09:14:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d027td$2lkn$1@si05.rsvl.unisys.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <9S1Am6GuflB@jpberlin-l.willms.jpberlin.de>`

```

"Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9S1Am6GuflB@jpberlin-l.willms.jpberlin.de...

>
> N> inspect function reverse (input-value)
…[5 more quoted lines elided]…
> one would not need to create a (temporary) reversed string.

I don't think the INSPECT syntax needs anything more than is already
provided by FUNCTION REVERSE.  The idea of new syntax for INSPECT to include
a REVERSE option (or a TRAILING option) was discussed, and rejected, at WG4
(in Las Vegas in 2003, IIRC).

As to "one would not need to create a (temporary) reversed string", the
*user* doesn't need to do this.

Though an *implementor's* first stab at this statement might actually
produce the reversed string in a temporary, the implementor could also
recognize the context of the REVERSE function and optimize to scan the
original text backwards.    Given enough market pressure, the implementor
might even be inclined to provide direct hardware support for doing so.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** epc8@juno.com
- **Date:** 2005-03-02T07:07:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109776059.651885.302910@l41g2000cwc.googlegroups.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com>`

```

Ron wrote:
> >>01    TEST-VARIABLES.
> >>        04 INPUT-VALUE PIC X(22) VALUE 'MYTESTVALUE'.
…[10 more quoted lines elided]…
> inspect function reverse (input-value) tallying tally-count for
leading spaces.
> move input-value (1 : length of input-value - tally-count) to
out-value.
>
> out-value will contain '         MY TEST VALUE'

Q: Are expressions allowed in reference modification?

[Slightly OT]

Here's an interesting way to abuse function reverse.

identification division.
program-id. rot1.
data division.
working-storage section.
01 chars.
05 x pic x(26) value 'abcdefghijklmnopqrstuvwxyz'.
05 y pic x(26).
05 z redefines y.
10 z1.
15 filler pic x occurs 1 to 25 times depending on l1.
10 z2.
15 filler pic x occurs 1 to 25 times depending on l2.
01 counters.
05 i pic 99.
05 l pic 99.
05 l1 pic 99.
05 l2 pic 99.
procedure division.
main.
    compute l = function length(x).
    perform next-i varying i from 0 by 1
      until i is greater than 26.
    stop run.
next-i.
    move x to y.
    if i is > 0 and i < l perform
      compute l1 = i
      compute l2 = l - i
      move function reverse(z1) to z1
      move function reverse(z2) to z2
      move function reverse(y) to y
    end-perform.
    display i space y.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-03-02T15:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9S5MCqbPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com>`

```
.    On  02.03.05
  wrote  epc8@juno.com
     on  /COMP/LANG/COBOL
     in  1109776059.651885.302910@l41g2000cwc.googlegroups.com
  about  Re: Right justifying (arbitrary) alphanumeric input


e> Q: Are expressions allowed in reference modification?

   Yes.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er kann die Tinte nicht halten, und wenn es ihm ankommt, jemand zu besudeln, so besudelt er sich gemeiniglich am meisten. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-03-02T11:16:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d053di$1hpo$1@si05.rsvl.unisys.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com>`

```

<epc8@juno.com> wrote in message
news:1109776059.651885.302910@l41g2000cwc.googlegroups.com...

> Here's an interesting way to abuse function reverse. ...

I tried to compile your program and ran into some problems:

ANSI X3.23-1985 page VI-27, 5.8.3, the OCCURS clause, syntax rule 7:  "A
data description entry that contains format 2 of the OCCURS clause may only
e followed, within that record description, by data description entries
which are subordinate to it.  Ibid., page VI-38, 5.10.3, the REDEFINES
clause, syntax rule 5:  "Neither the original definition nor the
redefinition can include a variable occurrence data item."  Note also that
the definition of the COBOL character set on page III-3 includes the
quotation mark (") but not the apostrophe (').

ISO/IEC 1989:2002 page 307, 13.16.36.2, OCCURS clause, syntax rule 20:  "The
subject of the entry may be followed within that record description entry
only by data description entries that are subordinate to it.".  Ibid., page
336, 13.16.42.2, REDEFINES clause, syntax rule 6:  "Neither the original
definition nor the redefinition shall include a variable-occurrence data
item."   Note that the 2002 standard adds the apostrophe and the underscore
to the COBOL character repertoire.

I'd say this program abuses rather more than the REVERSE intrinsic function!
Could you maybe show a program that illustrates your point that doesn't
violate COBOL standards?       ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-02T19:36:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WAoVd.57051$Zm5.6843@news.easynews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com>`

```
Sounds like Micro Focus or IBM extensions - that I "know and love" <G>
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 5)_

- **From:** epc8@juno.com
- **Date:** 2005-03-02T13:36:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109799364.993754.281280@l41g2000cwc.googlegroups.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com>`

```

Chuck Stevens wrote:
> <epc8@juno.com> wrote in message
> news:1109776059.651885.302910@l41g2000cwc.googlegroups.com...
…[5 more quoted lines elided]…
> ANSI X3.23-1985 page VI-27, 5.8.3, the OCCURS clause, syntax rule 7:
"A
> data description entry that contains format 2 of the OCCURS clause
may only
> e followed, within that record description, by data description
entries
> which are subordinate to it.  Ibid., page VI-38, 5.10.3, the
REDEFINES
> clause, syntax rule 5:  "Neither the original definition nor the
> redefinition can include a variable occurrence data item."  Note also
that
> the definition of the COBOL character set on page III-3 includes the
> quotation mark (") but not the apostrophe (').
>
> ISO/IEC 1989:2002 page 307, 13.16.36.2, OCCURS clause, syntax rule
20:  "The
> subject of the entry may be followed within that record description
entry
> only by data description entries that are subordinate to it.".
Ibid., page
> 336, 13.16.42.2, REDEFINES clause, syntax rule 6:  "Neither the
original
> definition nor the redefinition shall include a variable-occurrence
data
> item."   Note that the 2002 standard adds the apostrophe and the
underscore
> to the COBOL character repertoire.
>
> I'd say this program abuses rather more than the REVERSE intrinsic
function!
> Could you maybe show a program that illustrates your point that
doesn't
> violate COBOL standards?       ;-)
>
>     -Chuck Stevens

Thanks. I have since learned that expressions are allowed in reference
modificaion, once I separate the operators from the operands. So the
program simplifies to this:

identification division.
program-id. test1.
data division.
working-storage section.
01 x pic x(26) value "abcdefghijklmnopqrstuvwxyz".
01 y pic x(26).
01 i pic 99.
01 j pic 99.
procedure division.
main.
    compute j = function length(x).
    perform next-i varying i from 0 by 1
      until i is greater than j.
    stop run.
next-i.
    move x to y.
    if i is > 0 and i < j perform
      move function reverse(y(1:i)) to y(1:i)
      move function reverse(y(i + 1:j - i)) to y(i + 1:j - i)
      move function reverse(y) to y
    end-perform.
    display i space y.

-- Elliot
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-03-02T13:53:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d05clg$1nsp$1@si05.rsvl.unisys.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com> <1109799364.993754.281280@l41g2000cwc.googlegroups.com>`

```
Well, hmm.  What comes to mind is the comment of a dyed-in-the-wool Jaguar
fanatic back in the 1950's when describing Mercedes-Benz engineering
techniques:  "A maximally-complicated solution to a minimal problem."
;-)      Abuse of "function reverse", indeed!

    -Chuck Stevens


<epc8@juno.com> wrote in message
news:1109799364.993754.281280@l41g2000cwc.googlegroups.com...
>
> Chuck Stevens wrote:
…[71 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-03-02T23:32:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v2sVd.558267$8l.13592@pd7tw1no>`
- **In-Reply-To:** `<1109799364.993754.281280@l41g2000cwc.googlegroups.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com> <1109799364.993754.281280@l41g2000cwc.googlegroups.com>`

```
epc8@juno.com wrote:
> 
> Thanks. I have since learned that expressions are allowed in reference
…[27 more quoted lines elided]…
> 

OK so it works - but what does it actually do ? (Lazy way - I compiled 
and ran it) - but it will hiccup if you do the following. Take your two 
fields pic x(26) and make them pic x(44, or 50, or....). Take the 
"a.....z" and put the relevant number of spaces in FRONT of the 
alphabet, similarly put the spaces after the alphabet - although you 
don't need to do that because the spaces are understood when you say pic 
x(44). Other permutations using pic x(44), some spaces in front and at 
the end, and split the alphabet so there are spaces in the middle -

  "abcdefghij  klmnopqrstuvwxyz".

To be worthwhile it has to handle the above options and possibly more I 
haven't thought of. I can do it quite simply using some OO methods (The 
code is already there without me thinking about it) - but that's not 
much help to you.

But I can give you some pointers, and this is NOT a 
recommendation/suggestion how you should do it using Procedural COBOL - 
the string and length are passed to a method which using an array 
technique, (a TABLE in COBOL parlance), i.e. each incoming character 
(not just alpha or numeric) is identified by a position/index in the 
array. Take the split alpha above - it ignores the spaces at the front 
and end and the spaces between "...hij" and "klm". Trying to keep this 
simple - it has a second array of 'words' the 'semi-words' you find 
without a space - those 'semi-words' get stored with differing lengths 
and then they are all STRUNG back together again.

You need to keep a count of the words it finds. So what's happening in 
OO - your y pic x(44) is initialized then I can do a

perform varying n from 1 by 1 until n > MyWordCount

    STRING the current "semi-word" into y.
    Second time around y contains the first 'semi-word' and now
       we string the second 'semi-word" into the existing y
    etc...

end-perform

Simplest way I would suggest, keeping a count of total characters found 
- do a Reference Modification where you want right justified, otherwise 
automatically left justified.

Now the original version I wrote, using the support methods just handled 
strings with the option of including one space between 'real words' in 
the resultant 01 y pic x(44) above, or string the whole thing together 
ignoring ALL spaces. Then because I want to take a text field and 
display it in a Dialog or as a label in a Treeview, then I added options 
to get back the text with/without x'00' at the end.

If the last bit sounds like first-class gibberish :-

01 x pic x(50) value "George Washington".

then you get back

01 y pic x(50)

which will have a value of 'George Washington" + x'00' - a 'real' total 
of 18 used characters.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 7)_

- **From:** epc8@juno.com
- **Date:** 2005-03-02T17:18:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109812706.189405.241780@g14g2000cwa.googlegroups.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com> <1109799364.993754.281280@l41g2000cwc.googlegroups.com> <v2sVd.558267$8l.13592@pd7tw1no>`

```
James J. Gavan wrote:

> epc8@juno.com wrote:

[snip]  move x to y.

> >     if i is > 0 and i < j perform
> >       move function reverse(y(1:i)) to y(1:i)
…[3 more quoted lines elided]…
> >     display i space y.

[snip]

> OK so it works - but what does it actually do ? (Lazy way - I
compiled
> and ran it) - but it will hiccup if you do the following. Take your
two
> fields pic x(26) and make them pic x(44, or 50, or....). Take the
> "a.....z" and put the relevant number of spaces in FRONT of the
> alphabet,
[snip]

I was merely trying to illustrate doing something fun with function
reverse. Of course this would have been simpler:

if i is greater than 0 and i is less than j
  move x(1:i) to y(j - i + 1:i)
  move x(i + 1:j - i) to y(1:j - i)
else
  move x to y
end-if.

In its original context, rotating a string around end in place with
minimal temporary storage, this technique works well, but of course
this is in a language more primitive than COBOL. Also, if I have to do
things character by character, I like to reverse a string as follows
(pesudo-code):

p=start_loc
q=end_loc
while(p<q)
  swap s[p] and s[q]
  p=p+1
  q=q-1

This avoids having to figure out the length of the string and when to
stop. It also handles some special boundary cases, for example when the
string is empty.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 8)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-03-02T22:34:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<112d4u7rmmsts0c@news.supernews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <pd67211cb9qogpfg52ps32k3dkmanfoc2a@4ax.com> <762dne6b0dIqLr7fRVn_vQ@giganews.com> <1109776059.651885.302910@l41g2000cwc.googlegroups.com> <d053di$1hpo$1@si05.rsvl.unisys.com> <1109799364.993754.281280@l41g2000cwc.googlegroups.com> <v2sVd.558267$8l.13592@pd7tw1no> <1109812706.189405.241780@g14g2000cwa.googlegroups.com>`

```
epc8@juno.com wrote:
> James J. Gavan wrote:
>
…[21 more quoted lines elided]…
> reverse.

Fun is not allowed on a newsgroup. Somebody always takes you seriously.
```

#### ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-02-28T23:48:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m1b721lc7fnkm7ubj7dnqco999icveqi9v@4ax.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com>`

```
On Mon, 28 Feb 2005 21:15:56 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Quite a while ago, we had a long discussion about various methods of "right 
>justifying" alphanumeric data.  See (for example)
…[24 more quoted lines elided]…
>        STOP RUN.

Now that someone started this issue, here are two ways of right
justify text.
Some adjustments would need to be done if the destination field is
smaller than the justified text.

Sample 1 - Using unstring to get the "text size".
       IDENTIFICATION DIVISION.
       PROGRAM-ID. "STRSIZE1".
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 W01-MIN       pic 9(4) BINARY.
       01 W01-MAX       pic 9(4) BINARY.
       01 W01-MIDDLE    pic 9(4) BINARY.
       01 W01-STRING    pic X(80).
       01 W01-SIZE      pic 9(4) BINARY.
       01 W01-STRING2   pic X(80).
       01 X1 PIC 9(8).
       PROCEDURE DIVISION.
       MAIN.
           MOVE SPACES TO W01-STRING2
           PERFORM VARYING X1 FROM 1 BY 3
             UNTIL X1 > 44
             MOVE "X" TO W01-STRING(X1:1)
             PERFORM A1
             MOVE W01-STRING(1:W01-SIZE)
               TO W01-STRING2(80 - W01-SIZE:W01-SIZE)
             DISPLAY W01-STRING2 POSITION 1
             MOVE SPACES TO W01-STRING2
           END-PERFORM.
           ACCEPT X1
           GOBACK.
       A1.
           MOVE ZERO TO W01-SIZE.
           MOVE 1 TO W01-MAX
           PERFORM UNTIL W01-MAX > 80
              MOVE W01-MAX TO W01-MIN
              UNSTRING W01-STRING DELIMITED BY ALL SPACES
                 INTO W01-STRING2
               POINTER W01-MAX
           END-PERFORM.
           COMPUTE W01-SIZE = W01-MIN.
           MOVE SPACES TO W01-STRING2.

Sample 2 - Using a binary search to get the "text size"
       IDENTIFICATION DIVISION.
       PROGRAM-ID. "STRSIZE".
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 W01-MIN       pic 9(4) BINARY.
       01 W01-MAX       pic 9(4) BINARY.
       01 W01-MIDDLE    pic 9(4) BINARY.
       01 W01-STRING    pic X(80).
       01 W01-STRING2   pic X(80).
       01 W01-SIZE      pic 9(4) BINARY.
       01 X1            pic 9(8).
       PROCEDURE DIVISION.
       MAIN.
           PERFORM VARYING X1 FROM 1 BY 3
             UNTIL X1 > 50
             MOVE "X" TO W01-STRING(X1:1)
             PERFORM A1
             MOVE W01-STRING(1:W01-SIZE)
               TO W01-STRING2(80 - W01-SIZE:)
             DISPLAY W01-STRING2
             MOVE SPACES TO W01-STRING2
           END-PERFORM.
           ACCEPT X1.
           GOBACK.
       A1.
           MOVE ZERO TO W01-SIZE.
           MOVE 1 TO W01-MIN.
           MOVE 80 TO W01-MAX.
           IF W01-STRING NOT = SPACES
              PERFORM GET-SIZE
                UNTIL W01-MIN > W01-MAX
           END-IF.
           COMPUTE W01-SIZE = W01-MIN - 1.
       GET-SIZE.
           COMPUTE W01-MIDDLE = (W01-MIN + W01-MAX) / 2
           IF W01-STRING(W01-MIDDLE:W01-MAX - W01-MIDDLE + 1) = SPACES
             COMPUTE W01-MAX = W01-MIDDLE - 1
           ELSE
              COMPUTE W01-MIN = W01-MIDDLE + 1
           END-IF.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-03-02T01:08:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38j49bF5n7k2kU1@individual.net>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com>`

```
What purpose does DUMMY-VALUE serve?

Surely it will work without this?
(I haven't tried it and I'm too tired to do so, so I'm taking a chance
posting publicly, but I can't see what DUMMY-VALUE adds to the solution.)

Pete.
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:gSLUd.3656529$f47.654009@news.easynews.com...
> Quite a while ago, we had a long discussion about various methods of
"right
> justifying" alphanumeric data.  See (for example)
>
>    http://objectz.com/faqs/cobolfaq.htm#Sample_right
>
> When we talked about it, I know "we all" agreed that the "JUST RIGHT'
wouldn't
> help in a MOVE *unless* you knew how much non-space data there was.
However,
> someone sent me some source code (off-list) and I can't see anything wrong
with
> this (from a Standard conforming) point of view.  Although there may (or
may
> not) be better PERFORMING code, does anyone see any problems with the
following
> technique?
>
…[21 more quoted lines elided]…
>
```

#### ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-03-01T07:49:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1128snukvetkp82@news.supernews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com>`

```
William M. Klein wrote:
> Quite a while ago, we had a long discussion about various methods of
> "right justifying" alphanumeric data.  See (for example)
…[24 more quoted lines elided]…
>        STOP RUN.

Good catch. Slight amendment:

    04  INPUT-VALUE PIC X(50) VALUE 'MY TEST VALUE'.

UNSTRING INPUT-VALUE DELIMITED 'bb'
    INTO OUT-VALUE

also works as expected ("bb" = two spaces)
```

##### ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-03-01T15:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d022rf$nkk$1@peabody.colorado.edu>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <1128snukvetkp82@news.supernews.com>`

```

On  1-Mar-2005, "JerryMouse" <nospam@bisusa.com> wrote:

> Good catch. Slight amendment:
>
…[5 more quoted lines elided]…
> also works as expected ("bb" = two spaces)

That just makes the problem less likely - it doesn't eliminate it.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-03-01T17:40:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129vbo31b3rdf2@news.supernews.com>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <1128snukvetkp82@news.supernews.com> <d022rf$nkk$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  1-Mar-2005, "JerryMouse" <nospam@bisusa.com> wrote:
>
…[9 more quoted lines elided]…
> That just makes the problem less likely - it doesn't eliminate it.

It does if you use a handy-dandy routine to compact multiple spaces to a 
single blank before the UNSTRING command.

Frankly, I can't imagine anyone dealing with text data that doesn't use such 
"blank-collapsing" utility almost reflexively.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-03-03T15:59:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d07cdg$6c4$1@peabody.colorado.edu>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <1128snukvetkp82@news.supernews.com> <d022rf$nkk$1@peabody.colorado.edu> <1129vbo31b3rdf2@news.supernews.com>`

```

On  1-Mar-2005, "JerryMouse" <nospam@bisusa.com> wrote:

> >> also works as expected ("bb" = two spaces)
> >
…[6 more quoted lines elided]…
> "blank-collapsing" utility almost reflexively.

Reflexive action can sometimes surprise the users who were expecting to see
double spaces kept intact.
```

###### ↳ ↳ ↳ Re: Right justifying (arbitrary) alphanumeric input

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-03-03T10:44:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109875463.373331.146430@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d07cdg$6c4$1@peabody.colorado.edu>`
- **References:** `<gSLUd.3656529$f47.654009@news.easynews.com> <1128snukvetkp82@news.supernews.com> <d022rf$nkk$1@peabody.colorado.edu> <1129vbo31b3rdf2@news.supernews.com> <d07cdg$6c4$1@peabody.colorado.edu>`

```
Reflexive action can sometimes surprise the users who were expecting to
see
double spaces kept intact.

My clients routinely space out addresses and product descriptions to
get the effects they require within the free-form text fields.  They do
not want the computer to arbitralily change the way they input it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
