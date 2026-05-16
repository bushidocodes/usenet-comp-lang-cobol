[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# packed decimal question

_26 messages · 15 participants · 1999-10 → 1999-11_

---

### packed decimal question

- **From:** lopax@aol.com (Lopax)
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990930234135.02152.00000391@ng-cm1.aol.com>`

```
I have a file that contains packed decimal fields that I am ultimately trying
to move to  pic x fields.  I tried doing the following:

05  wkly-sal    pic 9(5)v99 comp-3 value zeroes
05  wkly-sal-r redefines wkly-sal pic x(07).

I was getting a wkly-sal-r redefined a smaller item error.  How can I move that
comp-3 field to a pic x field?  Can I use redefines like I was attempting to
do?  Any help would be greatly appreciated.  Thanks.
```

#### ↳ Re: packed decimal question

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F4F581.F6EA7070@NOSPAMhome.com>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com>`

```
Lopax wrote:
> 
> I have a file that contains packed decimal fields that I am ultimately trying
…[7 more quoted lines elided]…
> do?  Any help would be greatly appreciated.  Thanks.


Do you have a switch where your compiler can show you how large IT
thinks your fields are?  If so, use it.  I don't know if there are other
definitions, but on IBM mainframes, pic 9(5)v99 is stored like in 4
bytes like this: s9 99 99 99
```

##### ↳ ↳ Re: packed decimal question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<967J3.2981$Pt.23590@news4.mia>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com>`

```
Howard Brazee wrote:
>
>...  I don't know if there are other
>definitions, but on IBM mainframes, pic 9(5)v99 is stored like in 4
>bytes like this: s9 99 99 99

Howard, the IBM mainframe is not my forte', but is the sign not in
the rightmost nibble?  Like this: 99 99 99 9s where 's' = hex 'F'
because the field is 'unsigned' (otherwise 'C' = + and 'D' = -).
```

###### ↳ ↳ ↳ Re: packed decimal question

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F50324.F3E299E5@NOSPAMhome.com>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[7 more quoted lines elided]…
> because the field is 'unsigned' (otherwise 'C' = + and 'D' = -).

You're correct.  When I count how big it is, I start from left to right,
including the sign from the picture - but when I read a dump, the sign
trails.

My bad.
```

###### ↳ ↳ ↳ sign is leading....

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OhHQ3.1371$CS3.42989@viper>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia>`

```
>Howard, the IBM mainframe is not my forte', but is the sign not in
>the rightmost nibble?  Like this: 99 99 99 9s where 's' = hex 'F'
>because the field is 'unsigned' (otherwise 'C' = + and 'D' = -).


Correct, with a further clarification. The SIGN IS LEADING clause moves the
sign to the leading nibble:
sign is leading s9 99 99 99
sign is trailing 99 99 99 9s
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 4)_

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w2PQ3.26241$Fj2.238229@news1.mia>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper>`

```
No, that's ONLY for COMP-3 / Packed Decimal.
You are thinking of what is known as 'OVERPUNCHED'
a 0 is {
    1 is A
    ..
    9 is I
(Positive)
Negative is
    1 is J
    ..
    9 is R

Also you can code 'SEPERATE [Leading / trailing] CHARACTER, in which case
you count
the Sign as a position and it is a physically seperate byte.


Gumbo wrote in message ...
>>Howard, the IBM mainframe is not my forte', but is the sign not in
>>the rightmost nibble?  Like this: 99 99 99 9s where 's' = hex 'F'
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 4)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<802sf6$kna$1@nntp1.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper>`

```
On the subject of signs - came across an interesting phenomena last week.
Not sure if it's just Cob-370 -
Moving record field by field my program converted assumed positive sign of F
to C in my comp-3 fields. Just a plain move. I didn't ask it to change the
field,
just move it. Cob-370 just wants to show some initiative I guess!

Gumbo <a@a.com> wrote in message news:OhHQ3.1371$CS3.42989@viper...
> >Howard, the IBM mainframe is not my forte', but is the sign not in
> >the rightmost nibble?  Like this: 99 99 99 9s where 's' = hex 'F'
…[3 more quoted lines elided]…
> Correct, with a further clarification. The SIGN IS LEADING clause moves
the
> sign to the leading nibble:
> sign is leading s9 99 99 99
> sign is trailing 99 99 99 9s
>
>
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 5)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7gb2sgqn94f7m0lcshqobi7l6p2hnn50b@4ax.com>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net>`

```
On Sat, 6 Nov 1999 20:26:39 -0700 "Unbeliever" <popsider@ix.netcom.com> wrote:

:>On the subject of signs - came across an interesting phenomena last week.
:>Not sure if it's just Cob-370 -
:>Moving record field by field my program converted assumed positive sign of F
:>to C in my comp-3 fields. Just a plain move. I didn't ask it to change the
:>field,
:>just move it. Cob-370 just wants to show some initiative I guess!

If it was a move from a COMP-3 to a COMP-3, the odds are strong that a ZAP
instruction was generated.

ZAP, like most decimal instructions will force a "preferred" sign, either C(+)
or D(-).

If you wish to retain the sign, either redefine the field as X(n) or move the
group level.

:>Gumbo <a@a.com> wrote in message news:OhHQ3.1371$CS3.42989@viper...
:>> >Howard, the IBM mainframe is not my forte', but is the sign not in
:>> >the rightmost nibble?  Like this: 99 99 99 9s where 's' = hex 'F'
:>> >because the field is 'unsigned' (otherwise 'C' = + and 'D' = -).

:>> Correct, with a further clarification. The SIGN IS LEADING clause moves
:>the
:>> sign to the leading nibble:
:>> sign is leading s9 99 99 99
:>> sign is trailing 99 99 99 9s
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 6)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804ros$kmc$1@nntp5.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <d7gb2sgqn94f7m0lcshqobi7l6p2hnn50b@4ax.com>`

```
Good thought - could have been ZAPped.
I have a record layout that is INITIALIZEd in program 1, and then passes
though various programs.
The F->C sign change occurs in a field which was apparently INITIALIZEd in
program 1, then has
never been filled, so it is x'000000000F' and the move makes it
x'000000000C'.

Seems like I assumed that INITIALIZE would do a better job. But ultimately,
the only problem was that
my SUPERC compare failed on the sign change. As I was curious, I used a
Fileaid repl, to change
all zero-filled fields from a sign of F to C - then the before/after files
matched QED!

Binyamin Dissen <postingid@dissensoftware.com> wrote in message
news:d7gb2sgqn94f7m0lcshqobi7l6p2hnn50b@4ax.com...
> On Sat, 6 Nov 1999 20:26:39 -0700 "Unbeliever" <popsider@ix.netcom.com>
wrote:
>
> :>On the subject of signs - came across an interesting phenomena last
week.
> :>Not sure if it's just Cob-370 -
> :>Moving record field by field my program converted assumed positive sign
of F
> :>to C in my comp-3 fields. Just a plain move. I didn't ask it to change
the
> :>field,
> :>just move it. Cob-370 just wants to show some initiative I guess!
…[4 more quoted lines elided]…
> ZAP, like most decimal instructions will force a "preferred" sign, either
C(+)
> or D(-).
>
> If you wish to retain the sign, either redefine the field as X(n) or move
the
> group level.
>
…[5 more quoted lines elided]…
> :>> Correct, with a further clarification. The SIGN IS LEADING clause
moves
> :>the
> :>> sign to the leading nibble:
…[8 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<805114$87j$1@nntp6.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <d7gb2sgqn94f7m0lcshqobi7l6p2hnn50b@4ax.com> <804ros$kmc$1@nntp5.atl.mindspring.net>`

```
I have *not* tried this - but I would EXPECT that

INITIALIZE with a field defined as PIC 9   (Usage Display or Packed-Decimal)
   would move a X'F' to the receiving (initialized) field's sign-nibble

INITIALIZE with a field defined as PIC S9  (Usage Display or Packed-Decimal)
  would move a X'C' to the receiving (initialized) field's sign-nibble.

I would also THINK about what NUMPROC compiler option I was using - but I
*think* that for a receiving field, any setting SHOULD set the sign-nibble to
what you tell it to.

Moving from a PIC 9 to a PIC S9 field almost certainly will "zap" the
sign-nibble (I do not THINK that the reverse move would "remove" the sign,
but I won't swear to that).

If your INITIALIZE is really of a field defined with a sign and the
sign-nibble is X'F' and not X'C' - then I think you have found a "bug" in the
compiler.
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 8)_

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382610B5.F0FF8FC8@nbnet.nb.ca>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <d7gb2sgqn94f7m0lcshqobi7l6p2hnn50b@4ax.com> <804ros$kmc$1@nntp5.atl.mindspring.net> <805114$87j$1@nntp6.atl.mindspring.net>`

```
A move from S9(n) to 9(n) for either packed-decimal or display usages in
the receiving field will guarentee an 'F' zone in the receiving field. 
I have used this since COBOL D for DOS release 26 on a 360/30.  A move
from 9(n) to S9(n) does cause code to be generated that forces a C zone
(either Zero add packed or a combination of OR immediate followed by AND
immediate).

Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca  

"William M. Klein" wrote:
> 
> 
…[74 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 5)_

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6CqV3.16191$aS6.186111@news4.mia>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net>`

```
SIGN is LEADING does NOT apply to comp-3 / packed-decimal.  That makes it
comp-5.

Unbeliever wrote in message <802sf6$kna$1@nntp1.atl.mindspring.net>...
>On the subject of signs - came across an interesting phenomena last week.
>Not sure if it's just Cob-370 -
>Moving record field by field my program converted assumed positive sign of
F
>to C in my comp-3 fields. Just a plain move. I didn't ask it to change the
>field,
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<805g5q$8mh$1@nntp3.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <6CqV3.16191$aS6.186111@news4.mia>`

```
Check the dialect being talked about, in this case it was "COB-370" which was
an IBM mainframe dialect - which doesn't even KNOW about COMP-5.

FYI,
  I actually know of NO dialect in which "sign is leading" changes a COMP-3
to COMP-5.  Certainly EVERY PC compiler that I know of *does* support "sign
is leading" for COMP-3 items (which are treated as equivalent to
PACKED-DECIMAL).

Can you tell us what dialect DOES use "sign is leading" to change COMP-3 to
COMP-5? You aren't (by any chance) confusing SIGN IS LEADING with big-endian
versus little-endian?  If that is the case it changes how usage BINARY (or
sometimes COMP) is stored, but not where the sign-nibble is for DISPLAY or
PACKED-DECIMAL items.
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 6)_

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uGsV3.168$Av4.6861@typhoon.columbus.rr.com>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <6CqV3.16191$aS6.186111@news4.mia>`

```
>SIGN is LEADING does NOT apply to comp-3 / packed-decimal.  That makes it
>comp-5.
>


Regardless of what name you call it. The syntax of COMP-3 allows for the use
of the SIGN IS LEADING. SIGN IS LEADING places the sign in the high order
nibble of the leftmost byte of a field.
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826926e_2@news3.prserv.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <6CqV3.16191$aS6.186111@news4.mia> <uGsV3.168$Av4.6861@typhoon.columbus.rr.com>`

```
Gumbo <a@a.com> wrote in message
news:uGsV3.168$Av4.6861@typhoon.columbus.rr.com...
> >SIGN is LEADING does NOT apply to comp-3 / packed-decimal.  That makes it
> >comp-5.
>
> Regardless of what name you call it. The syntax of COMP-3 allows for the
use
> of the SIGN IS LEADING. SIGN IS LEADING places the sign in the high order
> nibble of the leftmost byte of a field.

I don't think so, and it would in any case be hardware dependent.
SIGN IS LEADING may be allowed syntactically with some compilers
but strictly speaking is only allowed for USAGE DISPLAY.
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806703$i9q$1@nntp5.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <6CqV3.16191$aS6.186111@news4.mia> <uGsV3.168$Av4.6861@typhoon.columbus.rr.com> <3826926e_2@news3.prserv.net>`

```
I stand corrected on my earlier post.  The Standard *does* require that the
item be explicitly (or implicitly) defined as USAGE DISPLAY.

The IBM LRM is a little fuzzy on whether they have a documented extension
allowing it for other USAGES and I would have sworn that Micro Focus did (but
can't find any documentation supporting this).

Sorry for the "mis-information" in my previous note(s).
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804579$436$1@nntp1.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net>`

```
Sign handling with ALL (old and new) IBM mainframe COBOLs is "an art without
an artist" <G>

If you have a field defined as signed (Packed or display) but that has a
sign-nibble of X"F" or an unsigned field with a sign-nibble of X"C".  What
happens is a  truly "remarkable" study in undocumented rules.  When you start
getting into things like X'40' in a field that is SUPPOSED to be numeric, the
variations grow dramatically.

Bottom-line,
   If you have data in a numeric (or numeric-edited) field that doesn't match
its picture clause, do NOT rely on it doing any of this - but don't be
surprised at anything that it does (and don't assume that what it does today
will happen tomorrow  - much less if you ever change compiler options or
releases).
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 5)_

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nzsV3.164$Av4.6536@typhoon.columbus.rr.com>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net>`

```
>On the subject of signs - came across an interesting phenomena last week.
>Not sure if it's just Cob-370 -
>Moving record field by field my program converted assumed positive sign of
F
>to C in my comp-3 fields. Just a plain move. I didn't ask it to change the
>field,
>just move it. Cob-370 just wants to show some initiative I guess!


Something I ran into recently was right up the same alley.370 is not
converting an assumed sign of F to C. It is converting an unsigned numeric
field to a signed numeric field. "F" is being carried over from the old
versions of card punches. I am far too young to have an experienced
knowledge of punch cards. But it had something to do with how signed
numerics were coded on the odld punch cards. Currently COBOL allows for
these values to be input to a COBOL program, but internal processing will
convert the old, defunct, vestigal sign of "F" to the proper value of "C".

If you display signed numeric fields, then look at the hex values of such,
you will get C or D in their appropriate vaues. Unsigned numerics will
generate a proper "F" since they are meant to be compatible with the PIC X
version of the same value.
```

###### ↳ ↳ ↳ Re: sign is leading....

_(reply depth: 6)_

- **From:** "Nilo Paim" <npaim@bigfoot.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806jhi$uss$1@srv4-poa.zaz.com.br>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com> <37F4F581.F6EA7070@NOSPAMhome.com> <967J3.2981$Pt.23590@news4.mia> <OhHQ3.1371$CS3.42989@viper> <802sf6$kna$1@nntp1.atl.mindspring.net> <nzsV3.164$Av4.6536@typhoon.columbus.rr.com>`

```

Gumbo <a@a.com> wrote in message
news:nzsV3.164$Av4.6536@typhoon.columbus.rr.com...
> >On the subject of signs - came across an interesting phenomena last week.
> >Not sure if it's just Cob-370 -
> >Moving record field by field my program converted assumed positive sign
of
> F
> >to C in my comp-3 fields. Just a plain move. I didn't ask it to change
the
> >field,
> >just move it. Cob-370 just wants to show some initiative I guess!
…[16 more quoted lines elided]…
>

I recall that some years ago, i had to ADD ZERO TO FIELD9 in order to get
proper value of the sign. Sorry, it was a lot of years ago and i can't
remember details on it. But i'm sure it was a IBM4341 with VM and DOS/VSE. I
can't say what Cobol version was...

Nilo npaim@zaz.com.br
```

#### ↳ Re: packed decimal question

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com>`

```
wkly-sal is only 4 bytes in size, not 7...each digit is a nibble in PD
fields, with a nibble for the sign...12 34 56 7C for example...

kenmullins


Lopax <lopax@aol.com> wrote in message
news:19990930234135.02152.00000391@ng-cm1.aol.com...
> I have a file that contains packed decimal fields that I am ultimately
trying
> to move to  pic x fields.  I tried doing the following:
>
…[3 more quoted lines elided]…
> I was getting a wkly-sal-r redefined a smaller item error.  How can I move
that
> comp-3 field to a pic x field?  Can I use redefines like I was attempting
to
> do?  Any help would be greatly appreciated.  Thanks.
```

##### ↳ ↳ Re: packed decimal question

- **From:** lopax@aol.com (Lopax)
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991001003546.02150.00000534@ng-cm1.aol.com>`
- **References:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net>`

```
I understand that now, but how can I move comp-3 fields to pic x fields.  I
tried moving the pic 9(7)v99 comp-3 to pic 9(7) then moving those pic 9(7)'s to
pic x(7)'s and that worked.  Is there a more efficient way than that?  Can I
redefine the comp-3's as pic 9's then move to pic x's?  Or do I have to move
the comp-3's 2 times like I stated above?  Thanks again



>wkly-sal is only 4 bytes in size, not 7...each digit is a nibble in PD
>fields, with a nibble for the sign...12 34 56 7C for example...
…[17 more quoted lines elided]…
>> do?  Any help would be greatly appreciated.  Thanks.
```

###### ↳ ↳ ↳ Re: packed decimal question

- **From:** Andreas Strzoda <as@as-data.de>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F46E8D.27B743C0@as-data.de>`
- **References:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net> <19991001003546.02150.00000534@ng-cm1.aol.com>`

```


Lopax schrieb:

> I understand that now, but how can I move comp-3 fields to pic x fields.  I
> tried moving the pic 9(7)v99 comp-3 to pic 9(7) then moving those pic 9(7)'s to
…[8 more quoted lines elided]…
> >

No, the only way to unpack a Comp-3 field is the MOVE to
a numeric field with usage is DISPLAY (the default), and..
take care of the decimal-point!

so define
01 TO-SHOW PIC 99999.99 [usage is display].
and move your field to this field. If you prefer leading spaces at the beginning
use the Z instead of the 9'th.
greating

AS
```

###### ↳ ↳ ↳ Re: packed decimal question

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t26hb$oqu$1@nnrp1.deja.com>`
- **References:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net> <19991001003546.02150.00000534@ng-cm1.aol.com>`

```
In article <19991001003546.02150.00000534@ng-cm1.aol.com>,
  lopax@aol.com (Lopax) wrote:

<Snipped>

> >Lopax <lopax@aol.com> wrote in message
> >news:19990930234135.02152.00000391@ng-cm1.aol.com...
> >> I have a file that contains packed decimal fields that I am
ultimately
> >trying
> >> to move to  pic x fields.  I tried doing the following:
…[4 more quoted lines elided]…
> >> I was getting a wkly-sal-r redefined a smaller item error.  How
can I move
> >that
> >> comp-3 field to a pic x field?  Can I use redefines like I was
attempting
> >to
> >> do?  Any help would be greatly appreciated.  Thanks.
>
>

If you define your unpacked (target) field as PIC 9(05)V99 and then
redefine it as PIC X(07), you can save yourself one MOVE statement. You
may want to consider defining the target as PIC S9(05)V99 to preserve
the sign, providing whether the value could in fact, be negative.

However, when addressing the PIC X(07), the usage of the implied two
position decimal and the sign-overpunch is not considered. It will just
look like any 7-byte character string. Also, you can't do any
arithmetic (if needed) on the PIC X(07). Note that the last (7th) byte
will include the sign. If you're confident the COMP-3 field will always
be ZERO or GREATER, then eliminate the sign on the target field.

03 WKLY-SAL PIC S9(05)V99 COMP-3 VALUE ZERO.
03 WKLY-SAL-UNPK-NUMERIC PIC 9(05)V99.
03 WKLY-SAL-UNPK-CHAR REDEFINES WKLY-SAL-UNPK-NUMERIC PIC X(07).

MOVE WKLY-SAL TO WKLY-SAL-UNPK-NUMERIC.

HTH....

Cheers,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: packed decimal question

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t2f1k$if6$1@news.igs.net>`
- **References:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net> <19991001003546.02150.00000534@ng-cm1.aol.com>`

```
It depends on whether you want to just move them or convert them.  If you
redefine accurately, and move the result to a picture x field, the data will
be there. If you want them *converted* to a straight ASCII field, then you
have to move them to a field defined that way.

You say you want to "move" fields.  If that is all you want, then the MOVE
statement works quite well with any data you want, from any definition you
want to any other definition you want.


Lopax wrote in message <19991001003546.02150.00000534@ng-cm1.aol.com>...
>I understand that now, but how can I move comp-3 fields to pic x fields.  I
>tried moving the pic 9(7)v99 comp-3 to pic 9(7) then moving those pic
9(7)'s to
>pic x(7)'s and that worked.  Is there a more efficient way than that?  Can
I
>redefine the comp-3's as pic 9's then move to pic x's?  Or do I have to
move
>the comp-3's 2 times like I stated above?  Thanks again
>
…[17 more quoted lines elided]…
>>> I was getting a wkly-sal-r redefined a smaller item error.  How can I
move
>>that
>>> comp-3 field to a pic x field?  Can I use redefines like I was
attempting
>>to
>>> do?  Any help would be greatly appreciated.  Thanks.
>
>
```

###### ↳ ↳ ↳ Re: packed decimal question

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HeHQ3.1370$CS3.43054@viper>`
- **References:** `<7t1c7n$i7o$1@nntp1.atl.mindspring.net> <19991001003546.02150.00000534@ng-cm1.aol.com>`

```
>>> 05  wkly-sal    pic 9(5)v99 comp-3 value zeroes
>>> 05  wkly-sal-r redefines wkly-sal pic x(07).


I am geussing a little bit here about what you want but....

05 wkly-sal pic 9(5)v99 usage packed-decimal value zeroes.
05 wkly-sal-display pic 9(5).99 usage display.

Move wkly-sal to wkly-sal-display

The above will translate the number into a properly displayed number with a
decimal point. However no mathemeatical operations will be able to pe
performed on the -display field. If operations need to be performed on the
number, then defining it as a PIC X as you previously did does not make
sense.
```

#### ↳ Re: packed decimal question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<op2J3.2443$Pt.19729@news4.mia>`
- **References:** `<19990930234135.02152.00000391@ng-cm1.aol.com>`

```
Lopax wrote:
>I have a file that contains packed decimal fields that I am ultimately trying
>to move to  pic x fields.  I tried doing the following:
…[6 more quoted lines elided]…
>do?  Any help would be greatly appreciated.  Thanks.

It is not clear what you mean when you say "move that COMP-3 field to a PIC
X field."  There are several possible meanings to what you ask.

1. Unpack the numeric digits into bytes, for example: 12345v67 -> "1234567"
   (not room for decimal in 7 bytes).  For this, define the receiving field
   as PIC 9(5)V99 DISPLAY, and redefine it as PIC X(7) for reference.

2. Convert the COMP-3 field to a properly formatted edited text field:
   12345v67 -> "12345.67".  For this, define the receiving field as
   PIC 9(5).99 DISPLAY, and redefine it as PIC X(8) for reference.

3. Move the COMP-3 field bit-for-bit into the correct number of bytes in a
   PIC X field.  For this, redefine wkly-sal as PIC X(4) for reference.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
