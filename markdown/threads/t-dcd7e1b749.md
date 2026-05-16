[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INSPECT and TRAILING syntax

_131 messages · 18 participants · 2006-05 → 2006-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### INSPECT and TRAILING syntax

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-09T05:29:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3p2b2$fmv$01$1@news.t-online.com>`

```
Seems weird to me that alongside ALL, FIRST and LEADING
the TRAILING keyword never made it into any standard.
Bill, was it ever considered ?
ACU implements it and I have just put it into OpenCOBOL.

Roger While
```

#### ↳ Re: INSPECT and TRAILING syntax

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-09T03:57:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com>`

```
Roger (et al),
  I think the thought is/was that "Function Reverse" lets you do much of this 
(not REPLACING or CONVERTING - but tallying).  If you use REVERSE to move a 
field to a temporary field, you can even do replacing and converting.
```

##### ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-09T06:15:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com>`

```
Yes, as I recall it J4 was of the opinion that anything you'd want to do 
with TRAILING you could accomplish with existing syntax, even if it required 
a "temporary" and an extra statement.

Adding new syntax for functionality that already exists -- particularly when 
the syntax for that functionality is pretty straightforward -- adds 
complexity to the language without adding functional feature content, and 
for that reason the suggestions to provide TRAILING were not followed.

    -Chuck Stevens

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:wqU7g.432129$7i1.140664@fe06.news.easynews.com...
> Roger (et al),
>  I think the thought is/was that "Function Reverse" lets you do much of 
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-11T00:42:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ce5dlF15a7qgU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3q4le$1lf5$1@si05.rsvl.unisys.com...
> Yes, as I recall it J4 was of the opinion that anything you'd want to do 
> with TRAILING you could accomplish with existing syntax, even if it 
…[5 more quoted lines elided]…
> for that reason the suggestions to provide TRAILING were not followed.

Interesting.

That being the case...

Why was EVALUATE added to the language when IF was already there?

Why was SEARCH added when the same effect could be obtained with PERFORM?

Why was EXAMINE dropped in favour of INSPECT when they provide the same 
functionality?

Why were scope delimiters added when we already had full stops?

Why was CONTINUE included when EXIT would have done?

Why was PICTURE provided in the langage when exactly the same functionality 
was available with CLASS, and SIZE?

So much rhetoric, so little time... :-)

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-10T09:50:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1263rv76rk9hh74@corp.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4ce5dlF15a7qgU1@individual.net...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
…[7 more quoted lines elided]…
> > complexity to the language without adding functional feature content,
and
> > for that reason the suggestions to provide TRAILING were not followed.
>
> Interesting.
>
> That being the case...

My best guess for each of the following.

> Why was EVALUATE added to the language when IF was already there?

CODASYL 1978. CODASYL was not J4.

> Why was SEARCH added when the same effect could be obtained with PERFORM?

CODASYL 1965. CODASYL was not J4.

> Why was EXAMINE dropped in favour of INSPECT when they provide the same
> functionality?

CODASYL 1969. CODASYL was not J4.

> Why were scope delimiters added when we already had full stops?

CODASYL 1978. CODASYL was not J4.

> Why was CONTINUE included when EXIT would have done?

CODASYL 1978. CODASYL was not J4.

> Why was PICTURE provided in the langage when exactly the same
functionality
> was available with CLASS, and SIZE?

CODASYL 1968. CODASYL was not J4.

> So much rhetoric, so little time... :-)
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-10T09:03:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3t2ta$cl7$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1263rv76rk9hh74@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:4ce5dlF15a7qgU1@individual.net...

>> Why was PICTURE provided in the langage when exactly the same
> functionality
>> was available with CLASS, and SIZE?
>
> CODASYL 1968. CODASYL was not J4.

Actually, from all I can tell, PICTURE was present from the beginning 
(1960).  If both PICTURE and SIZE were specified, PICTURE was used.  I'm not 
sure what you mean by CLASS here, but USAGEs could appear in SIZE clauses 
between the number of digits and the type of representation 
(CHARACTERS/DIGITS).

The SIZE clause does *not* seem to have made it as far as ANSI X3.23-1968 
(AKA "first standard COBOL"), though it was included in our COBOL(68) 
implementation for upward compatibility with B5000/B5500/B5700 COBOL (an 
implementation of COBOL-60).

Personally, I think the fact that you could say either
    PICTURE 9(5) USAGE DISPLAY or SIZE 5 DISPLAY CHARACTERS
but there was no corresponding mechanism for alphanumeric data items (SIZE 
implies numeric).  I find that a strange limitation.

Likewise, I think the fact that you could say
    SIZE 5 COMPUTATIONAL CHARACTERS
in implementations in which the format and layout of COMPUTATIONAL wasn't 
either "character-oriented" or "digit-oriented" in the first place (e.g., 
binary) was at best misleading.

And the fact that SIZE required the data item to be an *integer* was a real 
limitation -- that requires you to code
    PICTURE 9(5)V99 DISPLAY
instead of something like
    SIZE 7 DISPLAY CHARACTERS SCALE [FACTOR] 2 ...

Yes, lots of people have ways they'd rather code things than the way the 
COBOL standard currently allows them to be coded.  I'm not convinced that 
the language would have been well-served by the retention of the SIZE clause 
from the original CODASYL design, nor am I convinced that the language is 
well-served by adding different ways to do something you can already do in a 
relatively straightforward manner.  I'll vote for spending the energy on new 
*functionality* every time.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T01:21:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cgs32F15r5a8U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3t2ta$cl7$1@si05.rsvl.unisys.com...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
…[12 more quoted lines elided]…
> (1960).

Sorry, the first COBOL compiler I used was COBOL 59 (in 1965, illicitly. I 
was not supposed to be using it... ).I didn't formally go on a COBOL course 
until 1967.. It had no picture clause. We used SIZE, CLASS and USAGE.

 If both PICTURE and SIZE were specified, PICTURE was used.  I'm not
> sure what you mean by CLASS here, but USAGEs could appear in SIZE clauses 
> between the number of digits and the type of representation 
> (CHARACTERS/DIGITS).

CLASS was as used in the Class test to this day. It could be NUMERIC, 
ALPHABETIC, or ALPHANUMERIC.
>
> The SIZE clause does *not* seem to have made it as far as ANSI X3.23-1968 
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-11T07:26:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3vhio$1rg9$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4cgs32F15r5a8U1@individual.net...

>> Actually, from all I can tell, PICTURE was present from the beginning 
>> (1960).

> Sorry, the first COBOL compiler I used was COBOL 59 (in 1965, illicitly. I 
> was not supposed to be using it... ).I didn't formally go on a COBOL 
> course until 1967.. It had no picture clause. We used SIZE, CLASS and 
> USAGE.

I'm going by the "History of COBOL" section of the 1974 standard, which 
indicates that the initial meeting was May 28 and 29, 1959; that the initial 
specification wasn't done until September 1959; that the specification 
wasn't fully fleshed out as a language until December 1959, and that the 
first *published* description of COBOL came out in April 1960 ("COBOL -- A 
Report to the Conference on Data Systems Languages, including Initial 
Specifications for a Common Business Oriented Language (COBOL) for 
Programming Electronic Digital Computers").

Are you sure you weren't using one of the "ancestors" of COBOL as listed in 
the acknowledgments in older COBOL standards, namely, FLOW-MATIC from Univac 
(copyrighted 1958, 1959), the Commercial Translator from IBM (copyrighted 
1959), or FACT from Minneapolis-Honeywell (copyrighted 1960)?


>> If both PICTURE and SIZE were specified, PICTURE was used.  I'm not
>> sure what you mean by CLASS here, but USAGEs could appear in SIZE clauses 
…[4 more quoted lines elided]…
> ALPHABETIC, or ALPHANUMERIC.

Your query was "Why was PICTURE provided in the langage when exactly the 
same functionality was available with CLASS, and SIZE?".

I understood the availability of SIZE as an alternative for PICTURE, but 
couldn't relate to how CLASS was a syntactic/semantic substitute for 
PICTURE.  And thus I stand by the question:  what functionality does the 
class test in the PROCEDURE DIVISION provide that duplicates what PICTURE 
provides in the DATA DIVISION sufficient to render the latter unnecessary?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2006-05-12T09:25:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e41d9j$ovg$1@nntp.fujitsu-siemens.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag 
news:e3vhio$1rg9$1@si05.rsvl.unisys.com...
>
> I understood the availability of SIZE as an alternative for PICTURE, but 
…[4 more quoted lines elided]…
>
The 'COBOL-61 extended' report specifies as one of various clauses within a 
record description in the data division a CLASS clause with 'FUNCTION: To 
indicate the type of data being described' and with a syntax
 CLASS IS {ALPHABETIC / NUMERIC / APHANUMERIC /AN}  (only keywords within 
the brackets are underlined)
and several notes, of which the last says: '6. If a PICTURE is given, the 
CLASS clause is unnecessary. If both are used, however, the class of 
characters shown in the PICTURE must not contradict the CLASS clause of an 
elementary item, or of a group to which the item belongs'

K. Kiesel
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T20:26:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4civ5kF1646dcU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <e41d9j$ovg$1@nntp.fujitsu-siemens.com>`

```

"Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message 
news:e41d9j$ovg$1@nntp.fujitsu-siemens.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag 
…[20 more quoted lines elided]…
>
Thank you for posting that Karl.

Given that your document and Chuck's both indicate PICTURE was available, 
I'm at a loss to account for why we didn't use it. It may have been lack of 
understanding on my part at the time or perhaps it was an installlation 
standard, I honestly can't remember.

I DO remember learning about PICTURE on an ICL COBOL course in Auckland in 
1967.

Pete.
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T20:15:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ciugjF15psdsU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3vhio$1rg9$1@si05.rsvl.unisys.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:4cgs32F15r5a8U1@individual.net...
…[16 more quoted lines elided]…
> Programming Electronic Digital Computers").

It was referred to within the organisation as "COBOL 59 ".  It was an IBM 
site running TOS on system 360-32, usually in 1401 compatibility mode.


>
> Are you sure you weren't using one of the "ancestors" of COBOL as listed 
…[3 more quoted lines elided]…
>
I'm not sure of anything from that time :-) It was the sixties, for 
Chrissake :-)
>
>>> If both PICTURE and SIZE were specified, PICTURE was used.  I'm not
…[9 more quoted lines elided]…
>
Because USAGE was used with or without PICTURE as it is to this day.

And, it was a rhetorical question which was not expecting an answer. 
However, if someone answers a rhetorical question they might at least get 
the answer right...


> I understood the availability of SIZE as an alternative for PICTURE, but 
> couldn't relate to how CLASS was a syntactic/semantic substitute for 
> PICTURE.  And thus I stand by the question:  what functionality does the 
> class test in the PROCEDURE DIVISION provide that duplicates what PICTURE 
> provides in the DATA DIVISION sufficient to render the latter unnecessary?

OK...

01 flip PICTURE 9 USAGE DISPLAY.

01 flip CLASS is NUMERIC, SIZE is 1, USAGE  is DISPLAY.

The two definitions above define identical uses of storage.

01 flop PICTURE X(5).

01 flop CLASS is ALPHANUMERIC, SIZE is 5, USAGE is DISPLAY.

So do those 2...

01 flap PICTURE A(7) USAGE DISPLAY.

01flap CLASS is ALPHABETIC, SIZE is 7, USAGE is DISPLAY.

As do those 2...

And finally....

01   prick SIZE is ENORMOUS, CLASS is OLYMPIC, USAGE is INTERNAL FLOATING 
POINT.

....
I never said the CLASS test in the procedure division was used to define 
data; I said that CLASS worked the same way that a CLASS test does in the 
procedure division...(I was hoping you'd catch my drift... apparently a 
forlorn hope as I have now had to spell it out... :-))

Procedure Division.
...
    if flop is NUMERIC  *> example of COBOL CLASS test
...

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-12T06:55:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e42452$b9h$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4ciugjF15psdsU1@individual.net...

>> I understood the availability of SIZE as an alternative for PICTURE, but 
>> couldn't relate to how CLASS was a syntactic/semantic substitute for 
…[10 more quoted lines elided]…
>

[remainder snipped]

That's the part I couldn't find in any of the information I had available: 
the use of CLASS *in a data-declaration entry* and the associated semantics 
of the clause.

The only pre-'68-standard reference materials I have at hand show no sign of 
the CLASS clause (though they do include SIZE).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-12T12:56:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147463808.984669.249980@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<e42452$b9h$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com>`

```
> That's the part I couldn't find in any of the information I had available:
> the use of CLASS *in a data-declaration entry* and the associated semantics
> of the clause.

> The only pre-'68-standard reference materials I have at hand show no sign of
> the CLASS clause (though they do include SIZE).

I recall early ICL compilers: XE11 Compact Cobol, XE13 Cobol '61 where
PICTURE was a new thing and not to be trusted.  The 'CLASS' keyword was
optional, as was, and is, 'USAGE' and 'SIGN', so one could write:

     77   WS-TOTAL  SIZE 6 DISPLAY NUMERIC.

There were also EDITED and SIGNED but I can't remember if these were
hyphenated to NUMERIC.  There were many things that could not be done
that could be with PICTURE such as insertion characters.

Actually that looks almost like SQL.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-14T13:21:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147638066.184124.228270@v46g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<e42452$b9h$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com>`

```
> That's the part I couldn't find in any of the information I had available:
> the use of CLASS *in a data-declaration entry* and the associated semantics
> of the clause. 

http://www.icl1900.co.uk/techpub/c19ref.html
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-19T08:15:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4kndv$2aek$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com>`

```
Thanks for the URL, Richard.

I do have to admit that neither the ICL 1900 COBOL compiler nor the summary 
and comprehensive documentation for it are products to which I have been 
exposed before!  ICL systems haven't been all *that* common on this side of 
the pond ...

    -Chuck Stevens

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1147638066.184124.228270@v46g2000cwv.googlegroups.com...
>> That's the part I couldn't find in any of the information I had 
>> available:
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-20T17:02:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d7m78F18v09kU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e4kndv$2aek$1@si05.rsvl.unisys.com...
> Thanks for the URL, Richard.
>
…[4 more quoted lines elided]…
>
That's a pity...!

It was excellent hardware and software and a delight to program in COBOL or 
PLAN (Program LAnguage Nineteen hundred) .

It was killed by losing the 6-bit vs 8-bit byte war (along with some other 
very good systems), and the fact that the US market was never really 
penetrated by it. A few systems were sold in the US, but I have no idea who 
they were or where.

It used a single address hardware system  (load and store) with everything 
being done through registers and it was blazingly fast. IBM sold 360against 
it on the basis that the system 360 had a more 'intelligent' instruction 
set, but some benchmarks I did in the late sixties showed that the 1900 
creamed it. So much for 'intelligent' (or what we would now call 
'complex' )instruction sets... 1900 used RISC before the term was even 
invented... :-).

It had  a 24 bit word which was considered to be 4 6-bit characters. When it 
looked like the world was going to standardize on an 8 bit byte, there was 
talk of amending the internal 1900 architecture to consider the 24 bit word 
as 3 8-bit bytes and I believe a prototype was actually built in the UK. By 
the time it could've been brought to market, IBM had taken the market, and 
the 1900 lapsed into obscurity. A new range was released by ICL which, 
again, never really penetrated the US market. Eventually they were taken 
over by Fujitsu.

I have nothing but happy memories of working on 1900s. Wish I could say the 
same about some other household name hardware... :-)

Pete.

<snip>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-22T07:31:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com>`
- **References:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com> <4d7m78F18v09kU1@individual.net>`

```
On Sat, 20 May 2006 17:02:28 +1200, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>> I do have to admit that neither the ICL 1900 COBOL compiler nor the 
>> summary and comprehensive documentation for it are products to which I 
>> have been exposed before!  ICL systems haven't been all *that* common on 
>> this side of the pond ...

It seems odd to name a compiler 1900.   Sounds as though it was
pre-WWI.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 14)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-05-22T15:27:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qhi372hfs8ue43r1q3cnafhfh1ao7kdc9f@4ax.com>`
- **References:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com> <4d7m78F18v09kU1@individual.net> <r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com>`

```
On Mon, 22 May 2006 07:31:13 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Sat, 20 May 2006 17:02:28 +1200, "Pete Dashwood"
><dashwood@enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>pre-WWI.

Around the time of George III, you mean?
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 15)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-05-23T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hZIcg.184838$WI1.105055@pd7tw2no>`
- **In-Reply-To:** `<qhi372hfs8ue43r1q3cnafhfh1ao7kdc9f@4ax.com>`
- **References:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com> <4d7m78F18v09kU1@individual.net> <r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com> <qhi372hfs8ue43r1q3cnafhfh1ao7kdc9f@4ax.com>`

```
Ian Dalziel wrote:
> On Mon, 22 May 2006 07:31:13 -0600, Howard Brazee <howard@brazee.net>
> wrote:
…[15 more quoted lines elided]…
> Around the time of George III, you mean?

Nicely put Ian. You could at least have given him a hint :-)

(Nostalgia for the ICT 1500 and ICL 1900 series).

Jimmy
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 14)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-22T11:42:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148323337.434543.6800@38g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com>`
- **References:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com> <4d7m78F18v09kU1@individual.net> <r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com>`

```
> It seems odd to name a compiler 1900.   Sounds as though it was
pre-WWI.

ICL had a history that went back to the UK agent for Hollerith
equipment which was pre-WWI.

The 1900 series had many items number as 19xx, and some did seem to be
pre-WWI. For example the 1911 High Speed Card Reader was almost
victorian in its engineering and styling. Granted it did originate in
the 1940s as tabulator equipment with electronic changes to give it a
1900 interface. It was a huge complicated piece of equipment with a two
stage input hopper that would gate 2000 cards down to about 100 in the
actual cyclic feed area. This then took two cards to the 'instant'
asynchronous read station. Throght the read cells and could divert
'bad' cards to a reject station while the rest were sent up a track to
the output stacks which were a moving belt of trays that would each
take a handfull of cards.  You had to take the cards off before the
belt turned around the bottom wheels else they would be tipped on the
floor. Actually there were supposed to be light beams to detect
overflow but it wasn't reliable.

Inside was more wheels and levers than a knitting factory, all fed by a
centralised lubrication system with brass pipes to every moving part
(plus dozens of cards from past lives).
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-23T19:44:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dfsqoF19p7opU1@individual.net>`
- **References:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <e42452$b9h$1@si05.rsvl.unisys.com> <1147638066.184124.228270@v46g2000cwv.googlegroups.com> <e4kndv$2aek$1@si05.rsvl.unisys.com> <4d7m78F18v09kU1@individual.net> <r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:r7f372hk3m7ot549o37f9tahaq10hqknmk@4ax.com...
> On Sat, 20 May 2006 17:02:28 +1200, "Pete Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[8 more quoted lines elided]…
>

The compiler wasn't named 1900. The system was. It used the first of 
January, 1900 (which happened to be a Monday) as the base for all its date 
arithmetic.

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-05-12T22:11:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<271ae$44654e67$45491dc8$3016@KNOLOGY.NET>`
- **In-Reply-To:** `<4ciugjF15psdsU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net>`

```
Pete Dashwood wrote:
> 
> 01   prick SIZE is ENORMOUS, CLASS is OLYMPIC, USAGE is INTERNAL FLOATING 
> POINT.

Glad to see your imagination is still there...  ;)

(INTERNAL FLOATING POINT?  That made me laugh....)
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-12T22:25:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126akd8l1gshuff@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <271ae$44654e67$45491dc8$3016@KNOLOGY.NET>`

```
LX-i wrote:
> Pete Dashwood wrote:
>>
>> 01   prick SIZE is ENORMOUS, CLASS is OLYMPIC, USAGE is INTERNAL
>> FLOATING POINT.
>

VALUE "MITY69"

MOVE FUNCTION EXPAND (Prick) TO GOODNESS-ME.
DISPLAY GOODNESS-ME
Massachusetts Institute of Technology Year of 1969.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-14T02:18:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cm86hF15q738U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <271ae$44654e67$45491dc8$3016@KNOLOGY.NET> <126akd8l1gshuff@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:126akd8l1gshuff@news.supernews.com...
> LX-i wrote:
>> Pete Dashwood wrote:
…[9 more quoted lines elided]…
> Massachusetts Institute of Technology Year of 1969.
My Alma Mater... :-)

If that's genuine, HeyBub, I am thrilled to be in such company :-) (MIT, not 
the MITY prick...)

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-13T10:12:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126btr8faudih6f@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <271ae$44654e67$45491dc8$3016@KNOLOGY.NET> <126akd8l1gshuff@news.supernews.com> <4cm86hF15q738U1@individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
> news:126akd8l1gshuff@news.supernews.com...
…[11 more quoted lines elided]…
>> Massachusetts Institute of Technology Year of 1969.

> My Alma Mater... :-)
>
…[3 more quoted lines elided]…
> Pete.

Then you'll appreciate the following (posted on an anti-spam newsgroup to 
those who complain that SPEWS (a blocklist of spamming ISPs) has blocked 
their emails and could SPEWS please remove their IP addresses from the 
list):

1. Your emails are like sperm: ready to leap out and do their thing.
2. Your ISP is a prick.
3. SPEWS is a condom.
4. We are innocent maidens who don't like surprises.
5. You are asking for one teeny hole in the rubber.

You'll have to get us drunk first.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-14T10:50:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cn664F16hpchU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <271ae$44654e67$45491dc8$3016@KNOLOGY.NET> <126akd8l1gshuff@news.supernews.com> <4cm86hF15q738U1@individual.net> <126btr8faudih6f@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:126btr8faudih6f@news.supernews.com...
> Pete Dashwood wrote:
>> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
…[32 more quoted lines elided]…
> You'll have to get us drunk first.
ROFL! And very apposite.

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-14T02:14:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cm7uvF16fq9pU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <1263rv76rk9hh74@corp.supernews.com> <e3t2ta$cl7$1@si05.rsvl.unisys.com> <4cgs32F15r5a8U1@individual.net> <e3vhio$1rg9$1@si05.rsvl.unisys.com> <4ciugjF15psdsU1@individual.net> <271ae$44654e67$45491dc8$3016@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:271ae$44654e67$45491dc8$3016@KNOLOGY.NET...
> Pete Dashwood wrote:
>>
…[3 more quoted lines elided]…
> Glad to see your imagination is still there...  ;)

Hey, all I did was step out of the bath and glance in the mirror...

>
> (INTERNAL FLOATING POINT?  That made me laugh....)
>
Good, that was the general idea. :-) Thanks for letting me know it was worth 
the effort... :-)

Did you notice that in his response, Chuck cut it without referring to it at 
all...? :-)

I expected a comment that the CLASS and SIZE violated COBOL standards. 
('Internal floating point 'could be an IBM extension (pardon the pun... 
:-)). If it isn't, then it bloody well ought to be... I'd use floating point 
arithmetic just so I could code it...:-)

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T08:18:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ft362ls6ds3qav80brvonfcdpv21p5ovm@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net>`

```
On Thu, 11 May 2006 00:42:23 +1200, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>Why was EXAMINE dropped in favour of INSPECT when they provide the same 
>functionality?

I did a conversion once (from Univac 9030) where I replaced lots of
EXAMINE statements with TRANSFORM statements, on the theory that
TRANSFORM works with both ANSII versions and did what we wanted.

Then they dropped TRANSFORM.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T01:24:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cgs8iF15ue2cU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <9ft362ls6ds3qav80brvonfcdpv21p5ovm@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:9ft362ls6ds3qav80brvonfcdpv21p5ovm@4ax.com...
> On Thu, 11 May 2006 00:42:23 +1200, "Pete Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> Then they dropped TRANSFORM.

LOL! Always the way... just when we learn how to use something...:-)

Well, TRANSFORM WAS an IBM extension and it really did not provide quite the 
same functionality as EXAMINE (although some people used it that way, 
believing (incorrectly) it was more efficient. TRANSFORM was intended for 
translating character sets, originally with different tape formats.

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-10T10:01:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3t69i$emk$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4ce5dlF15a7qgU1@individual.net...

> Why was EVALUATE added to the language when IF was already there?

Users of other languages liked the functionality of CASE, which is what 
EVALUATE provides (and much more, I'd say).

> Why was EXAMINE dropped in favour of INSPECT when they provide the same 
> functionality?

INSPECT, introduced in a standard published thirty-two years ago now, 
provides a superset of the functionality previously available with EXAMINE.

As I see it, EXAMINE does not allow comparison by an identifier, does not 
allow combined tallying/replacing in the same statement, does not allow 
BEFORE/AFTER clauses, does not allow multiple replacements within the same 
data item, and does not allow multiple data items to be handled in a single 
statement.   I believe the keyword EXAMINE can be replaced by the keyword 
INSPECT in all contexts in which the former is superseded by the latter; the 
reverse is by no means true.

I wasn't involved in the standards process when this decision was made (it 
first shows up in the JOD of 1969), but my best guess as to the *reason* 
they used a different verb altogether for this was that some significant 
vendor had enhanced EXAMINE in a way that would have made the new features 
incompatible with that implementation.  Since the feature content of INSPECT 
is so much greater than the (standard) feature content of EXAMINE, providing 
a new verb was an approach that was actually friendlier to that user base, 
and not all that unfriendly to the rest of the EXAMINE-using community.

In the past, it seems to me your main "beef" with the COBOL standards 
process has had to do with the fact that in the seventeen years starting in 
1985 it only produced two amendments and an updated standard with 
significant (perhaps *too much*) feature content, and you have had nothing 
negative to say about the standards process *prior to* the introduction of 
the '85 standard.

I can't help but wonder why you seem to have begun complaining *now* about 
the way the '74 and even the '68 standards evolved from Adm. Hopper's 
original ideas as put forth in 1959-1960.   I don't think there's a whole 
lot I can do about convincing the contributors to ANSI X3.23-1968 (or for 
that matter ANSI X3.23-1974 or -1985) that they Did It All Wrong and that 
they Need To Do It All Over -- I strongly suspect the great majority of them 
are dead now anyway!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T11:09:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com>`

```
On Wed, 10 May 2006 10:01:39 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>INSPECT, introduced in a standard published thirty-two years ago now, 
>provides a superset of the functionality previously available with EXAMINE.
…[7 more quoted lines elided]…
>reverse is by no means true.

But as this thread shows, it did not add all the functionality people
wanted.   And then we lost the TRANSFORM verb, and had to change a
bunch of programs.

It didn't seem to be well thought out.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-10T11:13:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3tagg$h51$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com...
> On Wed, 10 May 2006 10:01:39 -0700, "Chuck Stevens"
> <charles.stevens@unisys.com> wrote:
…[16 more quoted lines elided]…
> wanted.

I am unaware of any functionality that the standard EXAMINE verb provided 
that the INSPECT verb did/does not.  What are you referring to?

> And then we lost the TRANSFORM verb, and had to change a
> bunch of programs.

In which *standard* did the TRANSFORM statement appear?

The IBM DOS COBOL (68) manual I have at hand includes it, but the syntax 
diagrams and rules for it are clearly marked as an *IBM extension* to '68 
COBOL.  IBM's decision to eliminate this extension at some point has nothing 
to do with the standard or the standards process.  That was a business 
decision on IBM's part, it seems to me.

Further, it seems to me INSPECT ... CONVERTING provides in *standard* '85 
syntax at least as much power as the *extension* TRANSFORM did, and although 
it's not a simple single-keyword substitution (as was the case for 
EXAMINE/INSPECT), "INSPECT A CONVERTING B TO C" looks equivalent in function 
to IBM's extension "TRANSFORM A [CHARACTERS] FROM B TO C".

> It didn't seem to be well thought out.

Well, as someone who doesn't hold that everything IBM does is the way 
everybody else ought to do it, I'm not sure I agree as to what it was that 
wasn't well thought out ... We've got our share of extensions that later 
turned out to get in the way of writing standard COBOL (the availability of 
USAGE BINARY in our COBOL74 implementation being a straightforward example 
in which users had to change their programs to compile them with COBOL85), 
and I think *every* vendor has.  TRANSFORM strikes me as falling in that 
category ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T12:32:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com>`

```
On Wed, 10 May 2006 11:13:36 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>> But as this thread shows, it did not add all the functionality people
>> wanted.
>
>I am unaware of any functionality that the standard EXAMINE verb provided 
>that the INSPECT verb did/does not.  What are you referring to?

This thread was about TRAILING syntax.   If INSPECT was so inadequate
that it needed to be thrown out and replaced, the replacement should
have offered a bigger improvement than it did.

>Well, as someone who doesn't hold that everything IBM does is the way 
>everybody else ought to do it, I'm not sure I agree as to what it was that 
…[5 more quoted lines elided]…
>category ...

Agreed.    That double-change was irritating though for insufficient
increased functionality.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-10T12:00:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3td8d$irv$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com...
> On Wed, 10 May 2006 11:13:36 -0700, "Chuck Stevens"
> <charles.stevens@unisys.com> wrote:
…[9 more quoted lines elided]…
> have offered a bigger improvement than it did.

And what functionality does EXAMINE provide that INSPECT does not with 
respect to TRAILING?

As already pointed out, Function TRIM provides what I think is what people 
want in the first place.   I actually like it better than expanding INSPECT 
to include TRAILING, for two reasons:  first, because it's a FUNCTION (and 
thus almost peripheral to the language itself, given the availability of 
user-defined functions), and second because both the syntax and the 
complexity of code generation for INSPECT have gotten WAY out of hand.   And 
having spent some time examining code generated for INSPECT, I think it'd 
almost certainly take some pretty fancy optimization to get the particular 
cases of INSPECT ... TRAILING that match the functionality of TRIM exactly 
to perform as well, precisely because INSPECT has to account for more 
eventualitites than Function TRIM might.

>>Well, as someone who doesn't hold that everything IBM does is the way
>>everybody else ought to do it, I'm not sure I agree as to what it was that
…[9 more quoted lines elided]…
> increased functionality.

Point being:  Don't blame J4 (or WG4, for that matter) for that one.  There 
is *no change at all* required to bring a program written to be in 
conformance with *standard* COBOL in the first place, because such a program 
*would not* contain the TRANSFORM statement to begin with.

If you chose to use an *IBM extension* and then complained because *IBM* 
dropped support for it in favor of functionality established as a standard 
by vendors *including* IBM, the source of your irritation is IBM, either for 
implementing an extension in the first place, or for decommitting it as an 
extension in later compilers (presumably without a clear migration 
strategy).

In our case, if we were to decommit such a syntactic extension, we'd provide 
logic in an  automated migration tool to make the appropriate substitution. 
The program used to handle '74-to-'85 migration in our environment, for 
example, has to account for the fact that USAGE BINARY was a Unisys 
extension in '74 COBOL but is standard COBOL in '85, and has different 
semantics (the odometer effect is applied only in very limited circumstances 
in our '74 implementation, universally in our '85).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T13:12:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hie462dtru403qf715nj2ek5cbuistv3p0@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com> <e3td8d$irv$1@si05.rsvl.unisys.com>`

```
On Wed, 10 May 2006 12:00:29 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>>
>> This thread was about TRAILING syntax.   If INSPECT was so inadequate
…[4 more quoted lines elided]…
>respect to TRAILING?

I don't know how I'm messing up, but obviously I am not saying what I
intend to say, because you keep asking the same question which seems
unrelated to what I intended to say.

I hope my statement wasn't that confusing to all, and I apologize for
my inability to communicate clearly.

But rereading the above quote, I have no idea how to say what I meant
any more clearly.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-10T19:43:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<unr8g.452435$7i1.49099@fe06.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com> <e3td8d$irv$1@si05.rsvl.unisys.com> <hie462dtru403qf715nj2ek5cbuistv3p0@4ax.com>`

```
All previous info removed - so MAYBE a "fresh" start will help (some).

The ANSI Standard EXAMINE was replaced by the '74 Standard ANSI INSPECT.  That 
statement did NOT include the "converting" facility which was added in the '85 
Standard.  The "question" (which seems pretty academic to me NOW) is WHY was the 
functionality (available with EXAMINE) not provided with the INITIAL inspect 
facility.

"Meanwhile" IBM provided the (extension) TRANSFORM facility which did provide 
the same functionality as this part of the EXAMINE (which the '74 Standard 
INSPECT did not).

Another (pretty academic now) question then arises whether it would have been 
better for J4 to introduce a TRANSFORM statement (which matched the "relatively 
common" extension to the '74 Standard) RATHER than introducing the CONVERTING 
phrase of the INSPECT statement - into the '85 Standard.

   ****

MEANWHILE (coming to the present age) the question of whether the TRAILING 
phrase (again an existing implemented extension) which "parallels" the existing 
STANDARD leading phrase would be a "good thing" is being asked.  In most other 
places in Standard ('85 or '02) COBOL where a "leading phrase" is supported, 
there is also a "trailing phrase".  Therefore, this doesn't seem to be 
unreasonable.  On the other hand, I agree that the INSPECT statement is 
sufficiently "complex" today that many of its uses are obscure (and end up with 
complex object code).

  ***

Finally, during the development of the '02 Standard, (possibly before) a 
suggestion was officially made to J4 that it ONLY add new syntax which was 
already in existence in at least one implementation.  This was rejected - and 
has been rejected when talked about since.  I don't know if this would or would 
not have "helped" the history of Standard COBOL, but it does seem at least 
somewhat relevant to this discussion.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-10T22:19:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3thta$o2k$02$1@news.t-online.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com> <e3td8d$irv$1@si05.rsvl.unisys.com> <hie462dtru403qf715nj2ek5cbuistv3p0@4ax.com> <unr8g.452435$7i1.49099@fe06.news.easynews.com>`

```
Well said Bill, although I might disagree that the INSPECT is "complex".
From a parser point of view it is relatively straight forward.
Especially comparing to the WHEN clause of EVALUATE.
Now that 2002 has added (MF's, I believe) partial-expression, that gets
very very messy. In fact look at the keword NOT following a WHEN and then
ask yourself what a partial-expression can be.

Roger While

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:unr8g.452435$7i1.49099@fe06.news.easynews.com...
> All previous info removed - so MAYBE a "fresh" start will help (some).
>
…[38 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-10T13:41:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3tj54$mc7$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com> <e3td8d$irv$1@si05.rsvl.unisys.com> <hie462dtru403qf715nj2ek5cbuistv3p0@4ax.com> <unr8g.452435$7i1.49099@fe06.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:unr8g.452435$7i1.49099@fe06.news.easynews.com...

> "Meanwhile" IBM provided the (extension) TRANSFORM facility which did 
> provide the same functionality as this part of the EXAMINE (which the '74 
> Standard INSPECT did not).

All I have on TRANSFORM is an IBM DOS reference manual.

As to EXAMINE ... REPLACING, I have the same IBM DOS reference manual, and 
the corresponding manuals from Burroughs from the similar period.  I don't 
see anything in EXAMINE that leads me to believe that it supports TRANSFORM 
functionality.  The IBM manual allows only one literal pair and it has to be 
one byte long.  How do you do a "transform" using EXAMINE ... REPLACING?

It is *possible* possible to handle TRANSFORM functionality using standard 
'74 INSPECT.  The source code is truly hideous (in our implementation the 
resulting code can be really, really fast), but it's not impossible to do. 
It involves, say, 256 "ALL ... BY ..." sequences after the keyword 
REPLACING.    INSPECT ... CONVERTING is a *much* clearer syntactic 
representation of the same functionality, I think.

> Another (pretty academic now) question then arises whether it would have 
> been better for J4 to introduce a TRANSFORM statement (which matched the 
> "relatively common" extension to the '74 Standard) RATHER than introducing 
> the CONVERTING phrase of the INSPECT statement - into the '85 Standard.

Well, seems to me
    INSPECT A-RECORD CONVERTING EBCDIC-CHARLIST TO ASCII-CHARLIST
is at least as clear a description of what's going on as
    TRANSFORM A-RECORD FROM EBCD-CHARLIST TO ASCI-CHARLIST.
so I don't see all that much reason, beyond "Well, IBM does it that way, so 
it must be good!" to choose the latter over the former.

I must admit, though, that sometimes the "IBM way" does creep in to the 
standard -- GOBACK was mentioned somewhere in this thread, and I'm not 
thrilled with the semantics of this verb!   I'd rather see specific 
directions (and runtime failures when they're inappropriate) than the 
vagueness of GOBACK.   ISTR the final discussions on this took place early 
in my tenure on J4, and I lost that argument ... still think GOBACK's a bad 
idea ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-11T02:41:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rvx8g.226046$2g2.31183@fe07.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com> <bg74625nelojlaasjk44aamdqvltp0dplt@4ax.com> <e3tagg$h51$1@si05.rsvl.unisys.com> <u9c462p8fcipl5e2tl50kqlo11qqksq46p@4ax.com> <e3td8d$irv$1@si05.rsvl.unisys.com> <hie462dtru403qf715nj2ek5cbuistv3p0@4ax.com> <unr8g.452435$7i1.49099@fe06.news.easynews.com> <e3tj54$mc7$1@si05.rsvl.unisys.com>`

```
Chuck,
  You are correct (as far as I can find out) that EXAMINE did *not* have the 
same functionality as INSPECT CONVERTING (and TRANSFORM).  My best *guess* is 
that the COBOL (IBM extension) TRANSFORM statement had its origin in the IBM 
S/360 "translate" Assembler instruction.  See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dz9zr003/7.5.141

but as I wasn't involved when TRANSFORM was first introduce, I certainly can't 
swear to this.

P.S.  On the subject of IBM providing "conversion assistance" for previously 
supported, but later dropped extension, see the CCCA manual at:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGYCCM02/CCONTENTS

Than product DOES provide automatic conversion support for both EXAMINE and 
TRANSFORM.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T01:38:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cgt38Frot8dU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <e3t69i$emk$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3t69i$emk$1@si05.rsvl.unisys.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[38 more quoted lines elided]…
>
My 'beef's with the COBOL standards committee are a matter of record. I'm 
not going through them all again. I do believe it started going to Hell in a 
wheelbarrow when ANSI became involved and the original CODASYL committee 
(who had vision and the right attitude) were phased out.

> I can't help but wonder why you seem to have begun complaining *now* about 
> the way the '74 and even the '68 standards evolved from Adm. Hopper's 
> original ideas as put forth in 1959-1960.

Hmmmm... I'm surprised at you Chuck. I thought you of all people whould 
understand the word 'rhetoric'.

My post did not require answers; I am well aware of the answers in every 
case I mentioned. It was intended to point out the inconsistency of a stated 
viewpoint... in a gentle way. As it was intended to be light-hearted and I 
was not expecting answers or for it to be taken seriously, I can't see how I 
am now "complaining". No complaint was expressed or implied.


> I don't think there's a whole lot I can do about convincing the 
> contributors to ANSI X3.23-1968 (or for that matter ANSI X3.23-1974 
> or -1985) that they Did It All Wrong and that they Need To Do It All 
> Over -- I strongly suspect the great majority of them are dead now anyway!

I agree. Neither is there any requirement for you to do so as far as I'm 
concerned.

Pete.

>
>    -Chuck Stevens
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-10T18:22:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mbq8g.73852$JV1.55476@fe05.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net>`

```
Pete,
  I know that Chuck has responded to a couple of the specifics, but as I agree 
with his initial post, I think what was not clear was that the "resistance" to 
adding new (redundant) syntax is a POST-2002 (somewhat in that too) development.

The 2002 Standard introduced LOTS and LOTS (too much IMHO) new "syntax" - some 
for things one could already do, some they couldn't.

Rightly or wrongly (I think rightly) SOME of the resistance to implementing the 
'02 Standard was that it was simply "TOO BIG".

The features that you mention were all introduced in the '85 Standard or 
earlier.

The '02 Standard had SOME new "redundant" features (e.g. GOBACK, partial-word 
replacement, SET TO FALSE).  However, it is my memory that even in the 
development of that Standard there was SOME discussion that these facilities 
COULD already be accomplished and did the language really need them.  In these 3 
cases (and possibly most others), the view was (as I recall it) that the new 
syntax was "more self-documenting".  I am not at all certain that ANY of them 
would make it into a post-02 Standard - if they were up for discussion now. 
Having said that, I do think that every possible enhancement has (and continues 
to be) considered on a "case by case" basis. A (well-discussed in this forum) 
feature was the addition of the "<>" operator - which DID make it into the draft 
'08 Standard.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T02:09:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cgus9F15np3pU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:mbq8g.73852$JV1.55476@fe05.news.easynews.com...
> Pete,
>  I know that Chuck has responded to a couple of the specifics, but as I 
…[12 more quoted lines elided]…
>
Bill,

I appreciate the response and the sincerity of it, but you are preaching to 
the choir.

A position was expressed that it is not good to include in the COBOL 
language new facilities, where the same effect can be achieved with existing 
constructs.

Here is the original quote:

> Yes, as I recall it J4 was of the opinion that anything you'd want to do 
> with TRAILING you could accomplish with existing syntax, even if it 
…[5 more quoted lines elided]…
> for that reason the suggestions to provide TRAILING were not followed.


This struck me when I read it as ludicrous. Given that I don't really care 
and it is all now academic anyway, I responded with what were intended to be 
examples showing that COBOL has ALWAYS been extended when there were already 
facilities in it to do what was being offered as 'new'. Personally, I no 
longer care whether INSPECT implements TRAILING or not. But to piously say 
it won't get done because there is already facility in the language that can 
implement it, is, in the context of the constructs I posted, laughable...

I did not intend to argue it seriously, was not complaining about it, did 
not expect detailed discussions about when and how this came about, was not 
(for once :-)) having a bitch at J4 or implying this was all their fault, 
(when I DO have a bitch about J4 it is not implicit...I don't think anyone 
has any doubts regarding my feelings in this department :-)), and neither 
was I posting a response about whether or not COBOL should have TRAILING on 
the INSPECT verb.

I believe that any further changes to COBOL now are simply a waste of time 
and money. Admittedly that hasn't stopped J4 in the past, and it is ironic 
(yet exactly what I would expect...) that their swan song is going to be an 
XML facility that is unnecessary, unhelpful, and being given priority over 
things like getting the 02 standard implemented.

If they get disbanded it serves them right.

> The '02 Standard had SOME new "redundant" features (e.g. GOBACK, 
> partial-word replacement, SET TO FALSE).  However, it is my memory that 
…[8 more quoted lines elided]…
> the "<>" operator - which DID make it into the draft '08 Standard.

Forgive me being underwhelmed by such an event. :-) I'll look forward to 
replacing the writer's cramp inducing, long winded,  'NOT =' with two 
characters that have no bearing whatsoever on the original stated purpose of 
COBOL  to be English like and understandable.

But we gave that up years ago and decided it was more important to emulate 
fashion than to stick to our guns and retain the vision of the inventors of 
COBOL.

Now let's have a wave of letters telling me how great it is to have an 
unequal operator in COBOL, and what a fuddy-duddy I must be  for not hailing 
it with enthusiasm. (The fact that I use it daily in VB and Java is 
irrelevant; these are not COBOL...)

Bugger, now I've responded seriously to something that was written with 
tongue in cheek, originally.

Gotta love this forum :-)

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-11T08:33:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3vlh4$1tuv$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4cgus9F15np3pU1@individual.net...

> I believe that any further changes to COBOL now are simply a waste of time 
> and money. Admittedly that hasn't stopped J4 in the past, and it is ironic 
> (yet exactly what I would expect...) that their swan song is going to be 
> an XML facility that is unnecessary, unhelpful, and being given priority 
> over things like getting the 02 standard implemented.

Neither J4 nor WG4 nor any of its parent bodies have *any* power to *force* 
anyone to implement a COBOL compiler compliant with the 2002 standard.

And the reason XML (and the other TR's) are visible is that they were 
written to be applicable to the 2002 standard as well as incorporated into 
the 2008 draft.  Is that such a bad thing?   I question the characterization 
of the XML TR as J4's "swan song", because I believe XML is but one among 
many features to be incorporated into the next standard; it has visibility 
because as a TR it's being applied against the *current* standard, largely 
as a "trial balloon".  There are lots of features, some big, some small, 
that are being incorporated into the 2008 draft *without* going through the 
"trial-balloon" of a TR because both WG4 and J4 agree they stand on their 
own merit!

For example, I think one of the best things J4 and WG4 have done is the new 
arithmetic mechanisms in the2008 draft -- I'm prejudiced, of course.  I 
think having new modes of arithmetic that are based on formats and behaviors 
that conform to an internationally-adopted *arithmetic* standard (the 
revision to IEEE 754) that is *outside of the COBOL standard* resolves one 
of the HUGE issues preventing the very code portability for which COBOL was 
designed in the first place.  Whether the IEEE standard ends up being 
something that can legitimately be cited in an ISO language standard remains 
to be seen, but I think that feature is a fundamental improvement to the 
internals of the language.

Too little, too late?  Well, maybe.  I first became aware of the IEEE 754 
effort and recognized the  importance to COBOL of the Decimal128 and perhaps 
the Binary128 formats and their rules, in the summer of 2004, informally 
suggested to WG4 at their October 2004 meeting that support for them be 
included in the 2008 draft.  The first draft of a proposal to that effect 
was published in December 2004, and the feature is now described in the 
current working draft.  It's not clear to me that I could have got it done 
much more quickly.   I can't even say whether the IEEE 754 proposals will 
end up being something that the COBOL standard can legitimately reference 
when push comes to shove.  What I can say is that I think the feature 
content is a Big Improvement at the very core of the COBOL language, and 
that I've done my best to make it work.   In general, I think I've made some 
fairly decent contributions to the COBOL standard given that I'm a relative 
newbie to the COBOL standardization process, having attended my first 
meeting as Unisys' representative on J4 in December 2000.

And I know you have disagreed with the feature-content priorities of J4 and 
WG4  over the years.  But if Pete Dashwood says he wants feature "x", and 
DIN and BSI have decided that they want feature "y" instead, it's kind of 
incumbent on WG4 to instruct J4 to work on feature "y".   The whole process 
is driven by *national standards bodies*.  I know you disagree with that 
approach, but neither J4 nor WG4 have any say in whether that's the 
appropriate way for formal international standards to be developed and 
adopted.  Nor do they have any say over whether any implementor decides to 
market a product that conforms, in every detail or only in part, to that 
standard.

I know of no work that J4 or WG4 can do to force or even encourage everyone 
from IBM through TinyCobol, or any subset of that group, to incorporate 
every single widget of every single doodad in the 2002 standard, to say 
nothing of the 2008 draft, under threat of ... what ...?

    -Chuck Stevens
```

###### ↳ ↳ ↳ What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-11T22:08:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JBO8g.400208$BL7.371029@fe09.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3vlh4$1tuv$1@si05.rsvl.unisys.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:4cgus9F15np3pU1@individual.net...
<much snippage>
>
> I know of no work that J4 or WG4 can do to force or even encourage everyone 
…[4 more quoted lines elided]…
>    -Chuck Stevens

Chuck,
   To answer this seriously, there are (IMHO) a few things that COULD be done to 
improve the chances of either the '02 or '08 Standards being implemented.

1) Do a "vendor-independent" survey of what features in the '02 Standard will 
NEVER be implemented by each vendor (as they PROBABLY are most in touch with 
their own customers).  From that list determine which features to either REMOVE 
or make optional in a the next Standard (or sooner).

2) Allocate resources to create a test suite for validation.  (I don't know 
about ISO - where the Standard now "lives" but at least for ANSI, this used to 
be something that COULD be done - but wasn't done while FIPS/NIST did it for 
them).

3) Possibly (I have always had mixed feelings about this) either re-introduce 
"subsets" to the Standard or "divide" the Standard into "mainframe" vs 
"workstation" versions (with a "common" base).

4) Figure out an ongoing "meeting" methodology that would encourage end-user 
participation in the Standards process. (I think, but am not positive that 
INCITS rules might allow this).  Meanwhile, encourage communication between J4 
and the actual users of the various vendors (particularly those NOT on the 
committee) users/customers.

    ****

Besides the "mainframe-thought-process" of the 60's and 70's (and 80's), that 
made COBOL so common (and portable), there is no doubt in MY mind that the US 
government requirement for "conforming COBOL compilers" in some types of 
contracts was what gave the previous Standards some "power".  It would seem to 
me that J4 (or WG4) *could* research what it would take to communicate to 
various government (US, European Union, etc) the need for Standard conforming 
COBOL compilers for *SOME* applications that they still maintain, enhance, and 
develop.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T19:54:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cit9pF165rt7U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com>`

```
As usual, good sound common sense.

I don't agree with the whole nonsense but I do think these are sound and 
positive suggestions.

Good on yer, Bill!

Pete.

TOP POST

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:JBO8g.400208$BL7.371029@fe09.news.easynews.com...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
> news:e3vlh4$1tuv$1@si05.rsvl.unisys.com...
>> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
>> news:4cgus9F15np3pU1@individual.net...

> <much snippage>
>>
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-19T13:21:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4l9bk$2l1s$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net>`

```
In the general case, Pete, I don't disagree with the suggestions; what I 
disagree with is the premise that what *I*, or anybody else on J4 or WG4 
needs to do is add anything more to their plate of things to do!    We'd 
*welcome* any effort on the part of anybody to carry out any of these 
suggestions, but these days I'm busy supporting a whole bunch of language 
compilers in addition to my efforts for the standardization process.

As I mentioned to Bill, someone in the ISO/IEC hierarchy is fond of the 
phrase "You shot it, you drag it home."

Bill, or I, or anyone else can sit here and say "Well, what *you* ought to 
be doing is ..., whereas what *I* ought to be doing is sitting here telling 
you how wrong what *you're* doing and what the priorities *you* are 
following are."

I take my work-time priorities from my employer, and my leisure-time 
priorities from my family.   I have some trouble understanding why those 
priorities should be different from what they are, either as an employee of 
Unisys (upon which my participation in both J4 and WG4 is dependent), or as 
one of the two significant breadwinners for my extended family.   Unisys is 
willing to support the standardization process -- for the time being -- even 
though we do not offer a compiler fully compliant with the 2002 standard. 
My family is willing to support my absence for J4 and WG4 meetings, despite 
considerable hardship on them.

Why should my priorities be more skewed to the COBOL standardization process 
and less toward the needs (to say nothing of the wishes) of either my 
employer or my family?

I know I don't have the resources to carry out Bill's suggestions, and I 
believe the same to be true of the other J4 members.  I personally welcome 
and encourage the participation of anyone who is willing to implement any of 
them.  If the suggestion is that good, then the person making the suggestion 
should at the very least be guiding its implementation -- back to "You shot 
it, you drag it home."

       -Chuck Stevens

<Top post, no more below>

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4cit9pF165rt7U1@individual.net...
> As usual, good sound common sense.
>
…[67 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-05-20T00:59:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4lplj$p2e$1@reader1.panix.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net> <e4l9bk$2l1s$1@si05.rsvl.unisys.com>`

```
In article <e4l9bk$2l1s$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:

[snip]

>Bill, or I, or anyone else can sit here and say "Well, what *you* ought to 
>be doing is ..., whereas what *I* ought to be doing is sitting here telling 
>you how wrong what *you're* doing and what the priorities *you* are 
>following are."

Hmmmmmm... sounds like a Manager, to me.

DD
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-21T00:47:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d8hfrF16pp2qU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net> <e4l9bk$2l1s$1@si05.rsvl.unisys.com> <e4lplj$p2e$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:e4lplj$p2e$1@reader1.panix.com...
> In article <e4l9bk$2l1s$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
…[10 more quoted lines elided]…
>
LOL! For once we agree on this, Doc. I would qualify it to "a BAD Manager", 
but I understand that in the Dwarf Book of Managers, that's the only kind 
there is :-)...

Pete.
> DD
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-05-21T09:36:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4pcbf$6ul$1@reader1.panix.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <e4l9bk$2l1s$1@si05.rsvl.unisys.com> <e4lplj$p2e$1@reader1.panix.com> <4d8hfrF16pp2qU1@individual.net>`

```
In article <4d8hfrF16pp2qU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:e4lplj$p2e$1@reader1.panix.com...
…[15 more quoted lines elided]…
>there is :-)...

Mr Dashwood, I've admitted to the possibility that other kinds of 
Managers might exist... but I've also pointed out that my experiences 
are, primarily, with 'sick shops', ones that, in their unhealthiness, 
seem to promote a kind of Gresham's Law of Management.  I would find it 
most interesting, to say the least, to work in a shop where a Manager 
storms into a Director's office and says 'I don't know *who* you think 
you are... but you are *not* going to treat *my* people this way and if 
you think you are then we need to make an appointment with Regional, 
*period*.'

I might even consider becoming a Manager at such a place... but first 
I'll need to see one.

DD
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-21T00:45:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d8hb3F199vo6U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net> <e4l9bk$2l1s$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e4l9bk$2l1s$1@si05.rsvl.unisys.com...
> In the general case, Pete, I don't disagree with the suggestions; what I 
> disagree with is the premise that what *I*, or anybody else on J4 or WG4 
> needs to do is add anything more to their plate of things to do!

Yes, I can understand that. However, no-one coerced anybody on the committee 
to be on it. It isn't like jury service where there is a moral and legal 
responsibility to participate.

If the workload is too much, either the committee needs to be organised 
better and work smarter (and, possibly, get more resources) or the whole 
thing should be descoped to the point of being manageable.

You can't really say: "Hey, we have a committee, COBOL is alive and well!" 
then in the next breath, when members of the COBOL community start offering 
positive ideas, say: "There's a HUGE amount of work to do, stop adding to 
our burdens...!!".

Bill, was trying to be positive and his suggestions are reasonable and 
probably worth doing. If I was on this committee, I would be seriously 
considering them and encouringing him to join. (He was once a very active 
member of the committee. I think he could be again if the goals were clear, 
worthwhile, and attainable. Of course, I don't want to talk about Bill like 
he isn't in the room, and he is quite capable of deciding his involvement 
for himself :-). I just don't think it is wrong for  someone to offer 
positive suggestions to the committee without necessarily being on it.

>We'd *welcome* any effort on the part of anybody to carry out any of these 
>suggestions, but these days I'm busy supporting a whole bunch of language 
>compilers in addition to my efforts for the standardization process.

So, (and I say this with the utmost respect and not in a hostile way) if you 
are finding that your committee involvement is clashing with your main job, 
maybe you should reconsider the reasons you are on the committee. (Or 
reconsider whether you need/want to be employed in your main job... :-))

Bottom line is that if there a major conflict, then something has to give. 
You volunteered for the committee; your main job is not exactly 
voluntary..., right? :-))
>
> As I mentioned to Bill, someone in the ISO/IEC hierarchy is fond of the 
> phrase "You shot it, you drag it home."
>
I'd not heard this before but I think you could argue as follows...  "Well, 
yes, I DID shoot it, but it's a hunting party, right? Anyone of us COULD 
have shot it. The purpose of the expedition is to shoot things. If one of 
YOU had shot it, I would n't hesitate to give you a hand in dragging it home 
(or cutting it up for easier transport); is it unreasonable for me to expect 
the same?"

If you go into the bush on your own and you shoot something, then you KNOW 
it is YOU who will bring it home. (I know from personal experience that this 
can have a defintie bearing on exactly what you shoot and how much of it. I 
have never shot more than I (and friends and family) could eat, and I have 
never gone hunting for the thrill of killing something; it has always been 
because we needed the food. And I don't hunt any more as we no longer need 
the food... The point in the analogy is that if you are going to go hunting, 
alone or in a party, it is good to know why you are doing so.)

> Bill, or I, or anyone else can sit here and say "Well, what *you* ought to 
> be doing is ..., whereas what *I* ought to be doing is sitting here 
> telling you how wrong what *you're* doing and what the priorities *you* 
> are following are."
>

That's a very fair comment.

I refute it thus:

1.There has been a very bad track record for this committee. For my part, 
I'd be more than happy to see it die. But it hasn't.
2. Being a basically fair man, I would hope that the new incarnation of the 
committee doesn't make the same mistakes the old one did. And I'm prepared 
to start them with a clean slate.
3. Should I say nothing because I am not on the committee?  (I'm sure you 
will understand there is virtually no chance of that... :-)). Can I not 
support this committee by offering advice? It is only advice; if the 
committee don't like it, don't take it. But don't whinge because people 
offer positive advice in a spirit of helpfulness. And it isn't fair to say 
they have no right to offer advice unless they are serving on it.

A wise committee would listen to all the comments it gets and seek to 
improve things. Neither Bill nor anybody else here is going to be offended 
if the advice offered isn't taken,  but what harm can it do to encourage 
comment? It was exactly this supercilious attitude (like, there is nothing 
the committee can learn from the community) that led to the marked lack of 
success of the previous lot. And don't tell me there is 'due process' and 
'procedures' for making representation to the committee. If the committee 
was genuinely interested in what the community thought, it would be very 
easy to submit ideas and there would be a genuine discourse. (God knows, the 
technology exists to do it from around the planet...)

> I take my work-time priorities from my employer, and my leisure-time 
> priorities from my family.   I have some trouble understanding why those 
…[7 more quoted lines elided]…
>
Your priorities are a matter for you, Chuck. I fully empathise with what you 
are saying, but remember this is a kitchen that no-one forced you to go 
into; don't complain about the heat.

> Why should my priorities be more skewed to the COBOL standardization 
> process and less toward the needs (to say nothing of the wishes) of either 
> my employer or my family?
>
In my opinion, they shouldn't. Family first, every time.

> I know I don't have the resources to carry out Bill's suggestions, and I 
> believe the same to be true of the other J4 members.

Hmmm... why not include Bill's suggestions on the next agenda and at least 
consider them jointly? Would it REALLY require such a lot of resource? Maybe 
the returns in doing so would be worth it. If you (as a group) don't 
consider it, you won't know whether it would have been feasible and 
worthwhile. Perhaps it might be more useful to set up a mechanism for 
feedback from the community (All it needs is a web site and a bulletin 
board...) than it is to consider the syntactic details of the new 
unnecessary XML construct... (just an example).

> I personally welcome and encourage the participation of anyone who is 
> willing to implement any of them.  If the suggestion is that good, then 
> the person making the suggestion should at the very least be guiding its 
> implementation

But then we wouldn't need a committee, would we?  Let me ask you 
something... Would you personally be prepared to bring your not 
inconsiderable experience and talent to bear on solving certain COBOL 
Standard issues, and then have the committee tell you that you hadn't 
complied with some obscure rule or procedure known only to people on the 
committee, or that they had decided that what you did was really not a 
priority for them so they wouldn't be taking it on board, or  "Thanks very 
much, but we need to get this other stuff done before we can look at what 
you did for us...", or worst of all..."Thanks for doing that but we've now 
decided it isn't necessary."

The committee needs to have very clear goals and aspirations. It should 
communicate these to the community and elicit support. If this support is 
not forthcoming, then it is fair to assume that there is no real need for 
what is being proposed and it should be descoped to the point where it is 
manageable by the committee.

1. Find out what is needed and wanted. (Don't just assume you know this, or 
let interest groups and lobbies drive it.)
2. Confirm that the perceived needs and wants are the actual needs and 
wants.(Communicate the proposal back to the user community)
3. Work out how many of these can be delivered with the available resources.
4. State what you propose to deliver and when.
5. Do it.(Communicate with the community while you are doing it and 
encourage comment. You might actually get people to help you if you do this. 
:-))

THEN, you may accept awards and bunfights for the great job you did, if that 
is what lights your candle...:-)


 -- back to "You shot
> it, you drag it home."

"I shot it on behalf of the group and any one of us could have pulled the 
trigger. If the kill is acceptable to the group then it is a group 
responsibility to transport it.  That's what 'teamwork' means..."

Pete.
<snip>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-22T11:25:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4svn4$15fa$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net> <e4l9bk$2l1s$1@si05.rsvl.unisys.com> <4d8hb3F199vo6U1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4d8hb3F199vo6U1@individual.net...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
…[3 more quoted lines elided]…
>> needs to do is add anything more to their plate of things to do!

> You can't really say: "Hey, we have a committee, COBOL is alive and well!"

No, Pete, that's not my point.  And I wasn't even saying "COBOL is alive and 
well!", my intent was "The reports of the demise of the COBOL *standards 
process* are slightly premature!"

> then in the next breath, when members of the COBOL community start 
> offering positive ideas, say: "There's a HUGE amount of work to do, stop 
> adding to our burdens...!!".

My response to positive ideas like this is more along the lines of "That's a 
really excellent idea upon whose details you seem to have a firm grasp. 
We've got a particular schedule we're trying to meet, and don't have a lot 
of time or resources to tackle what you suggest right now.  Why don't you 
take it on?  If you don't, it's going to go on the list and wait a while, 
and if you think it ought to be done sooner, then maybe you can help 
identify and allocate the resources to get it done."

> Bill, was trying to be positive and his suggestions are reasonable and 
> probably worth doing. If I was on this committee, I would be seriously 
> considering them and encouringing him to join. (He was once a very active 
> member of the committee.

He was, his ideas have been seriously discussed and considered (recently and 
otherwise), and we have encouraged him to join and participate in the past. 
I was there when he was an active voting member.  It was his choice to 
change his status to observer.

> I think he could be again if the goals were clear, worthwhile, and 
> attainable.

I'm not convinced the goals the committees have established are anything but 
all of these.  I know there have been arguments about the usefulness of XML, 
but there's a whole lot of Good Stuff in the 2008 draft (and technically the 
XML TR hasn't even been folded into it yet).   What some people don't seem 
to realize is that formalized international standards require formalized 
international consensus, and there's a process for that which takes some 
time.  Was the 2002 standard later than anybody wanted it to be?  Yes.  Was 
there stuff in it that was obsolete before the standard even came out?  Yes, 
unquestionably.  That's why the committee (with SIGNIFICANTLY fewer 
resources now than went into the 1985-to-2002 transition!) is putting so 
much energy and focus into getting the 2008 draft out *on time* (or as close 
to on-time as possible) with very little more feature content than was 
agreed to when WG4 first initiated it (the new arithmetic features were not 
on the original list; they were added at the meeting in The Hague; I'm 
pretty sure everything else that's in the draft but not in 2002 was on the 
original list from WG4).

> Of course, I don't want to talk about Bill like he isn't in the room, and 
> he is quite capable of deciding his involvement for himself :-). I just 
> don't think it is wrong for  someone to offer positive suggestions to the 
> committee without necessarily being on it.

Well, Pete, I for one have maybe six or seven weeks a year (five in 
meetings, the remainder in administrative stuff) that my company permits me 
to devote to the standards process.  For those of us employed by large 
companies, the resources *they* permit us to devote to the process are 
limited.  For those who are smaller companies, the resources they can bring 
to the table are also limited, for different reasons.

And I have already said that I think it's a *bad* idea for the committee to 
be the author of the validation suite -- having an independent individual, 
group, organization or company take on this task helps to ensure its 
impartiality.

> So, (and I say this with the utmost respect and not in a hostile way) if 
> you are finding that your committee involvement is clashing with your main 
> job, maybe you should reconsider the reasons you are on the committee. (Or 
> reconsider whether you need/want to be employed in your main job... :-))

No, what I am saying is that being on J4 is not my full-time job, it is one 
of the many things I am called upon to do as part of my duties.  I 
participate on the committee because Unisys has put me there as their 
representative for a variety of reasons, and I serve in that position at 
*their* pleasure, devoting the energies and resources to it that Unisys 
permits me to devote.   I am not in a financial position to resign from 
Unisys, to cover the various membership and meeting fees associated with 
voting participation in J4 and with being a delegate to (to say nothing of 
convener of) WG4, or to absorb the cost of travel to the meetings not held 
in my immediate vicinity.

> Bottom line is that if there a major conflict, then something has to give. 
> You volunteered for the committee;

If you're talking about J4, not exactly.  Unisys selected me as their 
representative in 2000; although I did not object and in fact was honored by 
their choice, I did not volunteer; in fact, I was not Unisys' first choice 
at the time.   With their support I *did* volunteer for the position of WG4 
convener (in part because I believe that position should be held by a member 
of the American delegation which is responsible for the technical details of 
the standard, but perhaps more importantly because nobody else seemed 
willing to take it on).  My participation in both J4 and WG4, and the 
resources I bring to that participation, are at the pleasure of Unisys.

I've already addressed the issues of bringing my *personal* resources to 
participation in these committees; at this point I am not in a position to 
do so.

> your main job is not exactly voluntary..., right? :-))

I've already addressed the issues of bringing my *personal* resources to 
participation in these committees; at this point I am not in a position to 
do so, so no, it's not.

Moreover, part of the whole "main job" includes doing what Unisys supports 
me doing on J4 and WG4 -- not less, but also not more.  I don't have the 
resources to go beyond that, and if I did, Unisys would almost certainly 
expect me to devote those resources to supporting languages *products* 
rather than the J4/WG4 processes, particularly if to do so causes support 
for languages products to suffer (any more than it already does because I 
can't devote full time to it).

> I'd not heard this before but I think you could argue as follows... 
> "Well, yes, I DID shoot it, but it's a hunting party, right?

Not necessarily, because I don't think it's a hunting party.  See below.

> Anyone of us COULD  have shot it.

> The purpose of the expedition is to shoot things.

No, I don't think so.  The purpose of the expedition is to *solve problems*, 
not merely identify them and then sit back and wait for someone else to 
tackle them.  If you think whatever *you* shot is a problem that needs 
solving, then the first candidate for solving it is you.  The rest of us are 
already dragging home all we can carry.

> If one of YOU had shot it, I would n't hesitate to give you a hand in 
> dragging it home (or cutting it up for easier transport); is it 
> unreasonable for me to expect the same?

Well, that helps, but ...

> If you go into the bush on your own and you shoot something, then you KNOW 
> it is YOU who will bring it home. (I know from personal experience that 
> this can have a defintie bearing on exactly what you shoot and how much of 
> it.

Bingo.  We do what we can.  What we're supposed to shoot and drag home has 
already been identified for us, through about the end of 2008 or into 2009. 
I happen to think, for example, it would be a *huge* help to the committee 
if someone were to take on the task of developing a validation test suite. 
I'm booked.  The rest of the committee is booked.

> I have never shot more than I (and friends and family) could eat, and I 
> have never gone hunting for the thrill of killing something; it has always 
> been because we needed the food. And I don't hunt any more as we no longer 
> need the food... The point in the analogy is that if you are going to go 
> hunting, alone or in a party, it is good to know why you are doing so.)

At this phase in the process, at least, I think we're trying to get the meat 
into refrigeration.  The suggestions that we need to drop what we're doing 
and go after more game are not coming from within the "hunting parties"!

> 1.There has been a very bad track record for this committee. For my part, 
> I'd be more than happy to see it die. But it hasn't.

Is your complaint with the current membership of "this committee", a 
personal gripe about the person who has chaired it, or a complaint about the 
fact that what J4 has done is what WG4 has delegated to it to be done, and 
that WG4's priorities were incorrect?   There are two committees involved 
here, one responsible for the overall direction and one responsible for the 
technical details.

> 2. Being a basically fair man, I would hope that the new incarnation of 
> the committee doesn't make the same mistakes the old one did. And I'm 
> prepared to start them with a clean slate.

This isn't a "new incarnation" of the committee.  We will have a different 
chair, which may lend a different "flavor" to the proceedings, but the 
fundamental changes came when ISO/IEC took over the basic direction of the 
COBOL standard and when the American effort was concentrated in J4 rather 
than in two separate processes.  As far as the Convener of WG4 goes, the 
best I can hope for there is that the current leadership doesn't turn out to 
be an unmitigated disaster!

My observation is that what soured you on J4 is that the time frame between 
the publication of the 1985 and 2002 standards was unconscionably long.  I 
don't disagree.  Part of that delay was "feature creep", and part of that 
delay was some political infighting among national standards bodies on 
particular language details (and since the 2002 standard was first and 
foremost an *international* standard, those *international* disputes had to 
be resolved to everyone's satisfaction.  We still have that international 
process, and it's still going to take a fair chunk of time from the point at 
which *J4* deems the draft ready for publication and that at which *WG4* 
submits it to ISO for publication.

> 3. Should I say nothing because I am not on the committee?

No, I certainly invite your active participation.  "Woulda, coulda , 
shoulda" is not really a positive contribution.  What are *you* willing to 
*contribute* to the technical content -- for example, the regression test 
suite?   We process documents from outside the committee all the time!

> (I'm sure you will understand there is virtually no chance of that... 
> :-)).

A problem offerred without a viable solution is not a problem, it's a 
complaint.

> Can I not support this committee by offering advice?

Whether it is supportive or not depends a whole lot on how it's presented, 
and what you're willing to do to help the committee *follow* that advice (or 
at least move in the direction you think it should be going)!

> It is only advice; if the committee don't like it, don't take it.

In case you didn't know, written advice, if it's formally presented to the 
committee, must be formally acted on, the actions must be recorded in the 
minutes, and the submitter must receive a formal response from the committee 
... Do it all the time (wrote one of the latter during the last J4 meeting, 
in fact ...)

> But don't whinge because people offer positive advice in a spirit of 
> helpfulness.

I'm not convinced that what's being offered here is "positive advice" when 
it comes across as a demand for more dedication and more effort on the part 
of those actually trying to accomplish the task, from those who insist that 
their proper role is to sit on the sidelines and complain about how lazy and 
incompetent the "grunts" are, and how much *more* they should be doing!

And speaking of "whinging", how else should I interpret your continued 
expressed resentments about what happened *ending* four years ago with the 
publication of ISO/IEC 1989:2002?

> And it isn't fair to say they have no right to offer advice unless they 
> are serving on it.

I agree that wouldn't be fair -- but I didn't say that.  I did say that the 
committee would be *delighted* if somebody or some organization from outside 
the committee took on some of these tasks.  J4 accepts, and has *always* 
accepted so far as I know, technical documents -- and assistance -- from 
outside the committee.  Why do you think that it is necessary to serve on 
the committee to contribute effort and resources to it?

I also note that much depends on presentation, and like anyone else, the 
committee does not respond well to "whinging".

> A wise committee would listen to all the comments it gets and seek to 
> improve things.

And we do.  If the two committees manage to pull off the 2008 draft in 
something approaching the desired schedule, I think that's patent evidence 
on their efforts to "improve things" that you felt were an issue.  Other 
issues there's not much the *members* can do anything about -- for example, 
I'm not in a position to *tell* Unisys that they *must* devote the resources 
necessary to develop a 2008-compliant -- or even 2002-compliant -- compiler. 
More on this later.

As to "improving things", the period you seem most concerned about is that 
which led to the 2002 standard.  From 1985 to 2002 there were two 
amendments -- the Intrinsic Function amendment of 1989 and the Corrections 
Amendment of 1993.

In contrast, since the publication of the 2002 standard, one TR has been 
published, one TR is entering the international approval process, one TR is 
in its final drafting stages, two Technical Corrigenda are ready for 
publication, and a third Corrigendum is entering the international approval 
process, all while the draft that we hope to get published in 2008 is being 
prepared, with significant new feature content.

Thus, if "improve things" includes responding more quickly, well, I think J4 
and WG4 have demonstrated that admirably.  Did they provide the features 
*you* wanted?  Well, maybe not, but they seem to have provided the features 
New Zealand, The Netherlands, Germany, the United Kingdom and the United 
States wanted ...

The only thing Unisys (or IBM or Micro Focus or Hitachi or Fujitsu or anyone 
else) is likely to listen to in terms of developing new conformant compilers 
is *market pressure*.  If you're dealing in the COBOL marketplace, it's the 
CIO's and CEO's of the people for whom you are working -- or contracting or 
consulting -- that you need to convince.

> Neither Bill nor anybody else here is going to be offended if the advice 
> offered isn't taken,  but what harm can it do to encourage comment?

We process comments all the time.  We do what we can do.  And sometimes it's 
really frustrating (as for the example of a validation suite) that there are 
things we *can't* do because the *people* who do the work on the committees 
don't have the resources to do them, which is why I suggest that if you feel 
strongly enough that something needs to be done, and J4 and WG4 agree, the 
committees would *welcome* the resource contribution.

Advice can be to *change fundamental direction*, which is the purview of WG4 
and requires consent from the various national bodies, and it can also be to 
add some sort of feature content or functionality.  The best way to 
accomplish this latter is by identifying and helping to provide the specific 
resources required for the task.   Without the resources, the "advice" 
becomes a "whinge".

> It was exactly this supercilious attitude (like, there is nothing the 
> committee can learn from the community) that led to the marked lack of 
> success of the previous lot.

I was involved in the very end of the 2002 standards development process, 
and my opinion about that standard was that a large part of the delay was 
the result of *feature creep* -- one after another of community suggestions 
that were incorporated into the standard over the too-long lifetime of its 
development.  Another part was the new process of developing it first as an 
international standard.

> And don't tell me there is 'due process' and 'procedures' for making 
> representation to the committee.

*Representation on* the committee is one thing.  Presenting ideas to the 
committee for their consideration is quite another.

> If the committee was genuinely interested in what the community thought, 
> it would be very easy to submit ideas and there would be a genuine 
> discourse.

There is such a process, and it can be initiated by something as simple as 
sending the J4 chairperson an E-mail.   There are face-to-face meetings five 
times a year, and sometimes there's even internal correspondence on such 
suggestions between meetings.  We also do use scheduled teleconferencing, 
but we have found through experience that this works better for specific 
issues, not as well for "general" meetings with lengthy agendas.

For example, an informal paper was received from a non-J4-member in Germany 
back in April.  We went through it at our most recent face-to-face meeting, 
and suggested changes to the draft and the production of a formal response 
document.  A teleconference is scheduled for 26 June to discuss the 
revisions and the response document.

> (God knows, the technology exists to do it from around the planet...)

And we do use it; we just haven't found that it works very well as a blanket 
substitution for face-to-face meetings.


> Your priorities are a matter for you, Chuck. I fully empathise with what 
> you are saying, but remember this is a kitchen that no-one forced you to 
> go into; don't complain about the heat.

I'm fine with the process.   The kitchen can process just so many meals a 
day, and if there's a waiting line outside the restaurant door, well, the 
people in that waiting line will have to wait.   Suggesting that the chefs 
crank all the ovens up to 600 degrees Fahrenheit so the food cooks faster 
might not be all that helpful ...

> In my opinion, they shouldn't. Family first, every time.

That's kinda what I thought, too.

> Hmmm... why not include Bill's suggestions on the next agenda and at least 
> consider them jointly?

Bill's first suggestion requires J4 to take a "vendor-independent" survey as 
to what features will NEVER be implemented by each vendor.  While J4 could 
indeed consider that, the J4 members who represent vendors would have to 
recuse themselves from any discussions.

More to the point, "NEVER" is pretty strong.  I think there are LOTS of 
features to which vendors would respond "Not scheduled unless, and until, 
there's sufficient demand from the marketplace to make the investment 
worthwhile."  And that might -- or might not -- be a meaningful list, and 
indeed might change based on what implementors provided the feature, and 
whether that feature provided a competitive edge!

The idea of avoiding optional features or "modules" in the standard was a 
specific direction *from WG4*, and rather a hot topic at that level.  J4 
could discuss this all day long, but if something like that were initiated 
at the J4 level, WG4 would almost certainly shoot it out of the sky at its 
next meeting, with probably lots and lots of strong words directed at J4 for 
daring to do such a thing while knowing full well that that was a flagrant 
disobedience by J4!

Bill's second suggestion was for the J4 members to allocate the resources 
needed to build a validation test suite.  This approach relies on the fact 
that the *members* of J4 are actually corporate members, with 
*representatives* on the committee, and that these corporate members have 
both the resources to dedicate to this task and the motivation to dedicate 
those resources.

I can only speak for myself as Unisys' representative, and I can state 
without a whole lot of fear of contradiction that Unisys would not support 
*my* committing the resources to develop, or provide significant assistance 
in developing, a validation suite.

I've said before and I'll say again here, I think the right resource for the 
development of a validation test suite would be something *outside* of the 
membership of J4, preferably something in Academia.

Bill's third suggestion is to divide the standard into "subsets" or to 
divide it into multiple versions with a common base.  The idea of avoiding 
optional features or "modules" in the standard was a specific direction 
*from WG4*, and rather a hot topic at that level.  J4 could discuss this all 
day long, but if something like that were initiated at the J4 level, WG4 
would almost certainly shoot it out of the sky at its next meeting, with 
probably lots and lots of strong words directed at J4 for daring to do such 
a thing while knowing full well that that was a flagrant disobedience by J4! 
I have *been there* for two such discussions.  I have no reason to believe 
WG4 would find the subset argument convincing.

Bill's fourth suggestion is about communications and improved use of 
technology in meetings.  J4 has tried various telecommunications 
methodologies in the past with limited success.  And J4 welcomes, and always 
has welcomed, comments, questions, suggestions from outside the committee. 
A simple E-mail to the chair will suffice.  We spent a good part of the last 
J4 meeting discussing comments received on the Collection Class library TR 
from a non-J4-member from Germany, and another on the same TR from a 
non-J4-member from Canada.   We continue to explore this issue.

My participation in this very forum is evidence of *my* willingness, as a J4 
member and as the convener of WG4, to participate in discussions of 
technical direction outside the framework of the J4 document submission 
procedures (or even simply E-mailing the chair).  Other members of J4 (and 
WG4) avoid this particular forum precisely because so frequently the sincere 
efforts of the members of J4 (present *and past*) have been repeatedly and 
roundly denigrated herein.

> Would it REALLY require such a lot of resource?

Considering the size of the validation suites for the '74 and '85 standards 
and the idea that your specific reference *here* is the validation suites, 
yeah, I think it would.  I think they need to be redone from scratch, and I 
also they need to be more comprehensive.  In all honesty, I'm not impressed 
with the *fundamental quality* and *comprehensiveness* of the validation 
suites for either '74 or '85 as they stand right now.  I'm not optimistic 
that they should even be used as a base for a new set except as a reference.

> Maybe the returns in doing so would be worth it.

No doubt they would.  I don't have the resources to do it, and I don't see 
my company offering it without a marketing incentive to do so (and more 
particularly a marketing incentive that increases Unisys' competitive edge). 
I think it'd make a *great* project for a university with J4 and/or WG4 
monitoring the results.

> If you (as a group) don't consider it, you won't know whether it would 
> have been feasible and worthwhile. Perhaps it might be more useful to set 
> up a mechanism for feedback from the community (All it needs is a web site 
> and a bulletin board...) than it is to consider the syntactic details of 
> the new unnecessary XML construct... (just an example).

Our priorities and our timetables are established by WG4.  We have discussed 
just such feedback mechanisms, but haven't had a lot of resources to pursue 
it much beyond that.  As it stands, E-mail to the J4 chair is welcome. 
(Spam and trolling, of course, are not).

> But then we wouldn't need a committee, would we?

*For that particular task*, maybe not.  I've already said I think having the 
validation suite developed by a group *outside* of J4 is a good idea.

> Let me ask you something...

> Would you personally be prepared to bring your not inconsiderable 
> experience and talent to bear on solving certain COBOL Standard issues, 
> and then have the committee tell you that you hadn't complied with some 
> obscure rule or procedure known only to people on the committee,

I don't think I've argued that, but there are two committees involved here, 
and their procedures are quite different.  To get official WG4 attention you 
*must* go through the National Standards Bodies.  If (like Canada) you don't 
have a National Standards Body participating in WG4, J4 will carry forward 
comments (and we have done exactly that in the past).   J4 will, and has, 
done what it can to carry the content of some pretty informal communications 
forward for formal J4 (and WG4) consideration.   But if the demand is to do 
something, for example, that WG4 has already made it clear to us that they 
will not tolerate, or if the demand is to accomplish something in a 
timeframe that the various (admittedly sometimes obscure) procedures simply 
will not allow, it's a bit frustrating for the committee to be called to 
task for failing to comply with the request!

> or that they had decided that what you did was really not a priority for 
> them so they wouldn't be taking it on board,

J4's priorities are established by WG4.  Sometimes J4 will bring a feature 
to WG4's attention to see if they'll add it to the already-established list 
for the *current* draft (they did this for IEEE 754r arithmetic).  Sometimes 
WG4 will say "great idea, but not for the current draft" and J4 will put it 
on the candidates list.  Sometimes J4 will put such things on the candidates 
list because they need further exploration.  And sometimes J4 will find that 
the feature is technically flawed in some way and reject it altogether.

In terms of what's in the draft *now*, J4 proposed a list of features at WG4 
Meeting #24 in Las Vegas, in conjunction with a COBOL futures workshop, in 
June 2003, and WG4 went through each of them and discussed them at some 
length.  Since then, IEEE 754r arithmetic was added to, and a couple of 
items dropped from WG4's "must-have" list (the latter simply because nobody 
had the time, resources or inclination to tackle them).   Examining and 
updating the "candidates list" has not been a priority at recent J4 
meetings; we're dealing with the list of stuff that WG4 has said "That ain't 
a candidate for inclusion, that's gotta be there, and by last year ..." and 
the "gee, wouldn't it be keen if ..." list isn't on the radar these days

> or  "Thanks very much, but we need to get this other stuff done before we 
> can look at what you did for us...",

That's a reality, Pete.  If something's on the agenda, we can process it, 
and all that's involved there is to get the chair to put it on the agenda. 
What you might regard as "helpful", J4 and even WG4 might regard as 
"distracting".   We went through a whole Big Deal about increasing the use 
of symbols instead of words in standard COBOL back at WG4 meeting #24. 
There was considerable discussion in this very forum on the subject.  What 
the 2008 draft includes is the addition of "<>" for "not equal", parallel to 
the already-present ">=" and "<=" symbols, but the WG4 minutes make clear 
that that's not the direction COBOL should go in general.  My opinion is 
that the introduction of ">=" and "<=" was a bad idea in the '85 standard; 
adding "<>" finishes out the group, but the WG4 minutes are clear that 
"That's IT!!" when it comes to APL-izing COBOL.

> or worst of all..."Thanks for doing that but we've now decided it isn't 
> necessary."

Well, that happens too.  We've already got COMPUTE A = A + B + C, ADD B C TO 
A, ADD B C TO A GIVING A, and MOVE FUNCTION SUM (A B C) TO A that accomplish 
pretty much the same thing with a few minor semantic widgets.  Is it 
*really* that high a priority *for COBOL* to have *yet another* way of doing 
this?  This isn't a "new feature", it's a new way of doing something you can 
already do.   Does COBOL *need* a new way to express this when there are 
alrready at least four ways of doing that that are likely to produce, for 
the examples given, very nearly the same object code (presuming some sort of 
optimization in Function SUM)?

> The committee needs to have very clear goals and aspirations. It should 
> communicate these to the community and elicit support.

Right now J4's goal and aspiration is to get the XML and Collection Class 
TR's out for international ballot, and to get the 2008 draft *with its 
current feature content* ready for international ballot.   We can blue-sky 
all we want about what happens after the 2008 draft gets approved, but now 
is not the time for that.

> If this support is not forthcoming, then it is fair to assume that there 
> is no real need for what is being proposed and it should be descoped to 
> the point where it is manageable by the committee.

There are two committees.  Descoping the feature content of the 2008 draft 
is out of the question because the feature content has been defined, and 
confirmed twice, at the WG4 level.

> 1. Find out what is needed and wanted. (Don't just assume you know this, 
> or let interest groups and lobbies drive it.)

What J4 does is what the National Standards Bodies, through WG4, tells it 
that interest groups and user groups and vendors and end-users have told it 
they want.  J4 knows this because it's in the WG4 minutes, and it's WG4's 
standard.

> 2. Confirm that the perceived needs and wants are the actual needs and 
> wants.(Communicate the proposal back to the user community)

...Which is why the working draft standard and the last two years' worth of 
J4 documents detailing the technical issues and changes are available on the 
internet ...

>  3. Work out how many of these can be delivered with the available 
> resources.

Done in June 2003 at WG4 Meeting #24 in Las Vegas.

> 4. State what you propose to deliver and when.

Done in June 2003 at WG4 Meeting #24 in Las Vegas.

> 5. Do it.(Communicate with the community while you are doing it and 
> encourage comment. You might actually get people to help you if you do 
> this.

Been doing that since WG4 Meeting #24 in Las Vegas, and before ... ;-)

> THEN, you may accept awards and bunfights for the great job you did, if 
> that is what lights your candle...:-)

I'm not interested in kudos.  I happen to think a COBOL standard has value 
whether or not a fully-conforming implementation (with or without 
"processor-dependent" features) is ever produced.

A COBOL85 implementation that also supports the formatted-time and 
formatted-date functions, and does so in a manner strictly conformant with 
the 2008 draft, has made appropriate use of the standard.  A COBOL85 
implementation that supports "free-form reference format" instead of, or in 
addition to, a "proprietary" source format has made some step toward the 
goal of industry compatibility.  The implementor has done *his* part; it's 
now up to the others to follow that example.  If they don't, it's a shame, 
but no flies on him for having done it right.

> -- back to "You shot
>> it, you drag it home."
…[3 more quoted lines elided]…
> responsibility to transport it.  That's what 'teamwork' means..."

Well, it depends on whether the group was out there to cull the herd, and 
whether they'd reached their limit or not.  "Hey guys, I know you're 
cleaning and skinning, and we've already reached the limit that the Fish and 
Game Service had set for us, but I've just shot two does and a fawn, and I 
need you to haul them in and transport them because I've run outta time 
...".  If you offer advice to the group, it is not particularly helpful if 
that advice goes counter to the stated goals and the priorities of that 
group, particularly if those goals and priorities are established for them!

One of the frustrating aspects of the fourth-class year (including Plebe 
Summer) at Annapolis was the fact that every fourth-classman was required to 
be responsible for following the orders of every upper-classman, even when 
those orders conflicted directly.

Given that J4 already has its "marching orders" (from WG4), complaining that 
when a user says "JUMP!" J4 responds with "well, we'll have to look into 
that, but I doubt that's going to be happening anything like soon" instead 
of "how high, SIR!?!?!"  doesn't strike me as all that productive, either, 
Pete.  That's not what teamwork means *to me*.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-23T20:15:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dful1F19phbgU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <4cit9pF165rt7U1@individual.net> <e4l9bk$2l1s$1@si05.rsvl.unisys.com> <4d8hb3F199vo6U1@individual.net> <e4svn4$15fa$1@si05.rsvl.unisys.com>`

```
A good response, Chuck.

But I'm not encouraged to get involved :-)

Seriously, I wish you well and I'll lay off this topic so I don't get 
accused of "whinging"  (which, in our part of the world is a VERY serious 
sin... )

There is one thing I am very certain of though, and I mention it again in 
concluding... If you don't get user engagement, if you don't let people feel 
like they are involved, you will never have success with this venture. 
Whatever the red tape, whatever the existing rules, I would urge you to 
facilitate user feedback and discussion. Keep things open and avoid the 
"ivory tower" syndrome. The image of this body needs to be changed.

Best wishes,

Pete.


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e4svn4$15fa$1@si05.rsvl.unisys.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:4d8hb3F199vo6U1@individual.net...
…[630 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-19T13:06:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4l8g3$2kjv$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com>`

```
Whether there are things "that COULD be done to improve the chances of 
either the '02 or '08 Standards being implemented" is at least somewhat 
orthogonal to the question as to whether I, or the other members of J4, or 
the National Body representation to WG4, have the resources to carry out 
such tasks.   With the Unisys-related duties I have as an employee of that 
company, I consider myself lucky to fit my *current* duties for J4 and WG4 
accomplished.  I am quite sure the same is true for the other 
"corporate-sponsored" members of J4, and doubly true for those members of J4 
who are CEO's of the companies they represent.  I know of nobody on J4 whose 
sole responsibility to their companies is the COBOL standardization process, 
much less anyone whose primary financial support stems from participating in 
that process.

As to your suggestions:  paraphrasing a certain official in the ISO/IEC 
hierarchy:  "You shot it, you drag it home!"  ;-)

For your item 1, I for one do not have the resources to perform such a 
survey, nor do I believe any of the other five members of J4 have them. 
Since you have clear ideas as to how this can be accomplished, maybe you'd 
be the appropriate person to carry out such a survey?   If not, why not, and 
more particularly, why any individual member of J4 or the committee as a 
whole more than you?

Likewise, for your item 2, I have *even less* resources to allocate to the 
development of a complete validation test suite for the 2002 standard, or 
for the 2008 draft.  What resources are *you personally*, with or without 
corporate sponsorship that you might arrange, be willing to bring to the 
table?   J4 would welcome *any* volunteers to take this task on; I've 
already mentioned this elsewhere.

For item 3, I think much of this is already covered by "processor 
dependent"; the problem is in getting the National Bodies to agree on what 
should be "processor dependent" and what should be mandatory for all 
environments.

For item 4, J4 welcomes guests at its meetings (so long as we have 
sufficient notice to provide accommodation for them).  We have used 
teleconferencing methods occasionally, but have found that there are 
circumstances in which they are not as effective as face-to-face discussion.

Perhaps more to the point:  of the six attendees at the J4 meeting just 
completed, *four* were representatives of end users, and only two 
represented vendors.   In what way is J4 discouraging participation by end 
users?    When was the last time you made the effort to attend a J4 meeting 
(as a guest or otherwise)?

<< Besides the "mainframe-thought-process" of the 60's and 70's (and 80's), 
that made COBOL so common (and portable), there is no doubt in MY mind that 
the US government requirement for "conforming COBOL compilers" in some types 
of contracts was what gave the previous Standards some "power".  >>

I agree with you there.  I've made that clear on numerous occasions.  I 
think the relaxation of that requirement was a disaster to the entire 
language standardization process, not just that for COBOL.

< <It would seem to  me that J4 (or WG4) *could* research what it would take 
to communicate to  various government (US, European Union, etc) the need for 
Standard conforming COBOL compilers for *SOME* applications that they still 
maintain, enhance, and develop. >>

There are lots of things that J4 *could* do, if it had any resources to 
speak of beyond that which is necessary to providing standard specifications 
for features demanded of it, alongside the processing of interpretation 
requests and technical corrigenda.  But the resources of J4 are very limited 
in that respect.

We happen to agree that standardized languages protect the investments 
businesses make in programs developed using them.  Convincing people that 
this is a Nice to Have is not the problem.

The only real clout is exerted by *businesses* who insist on conformance to 
such standards in all respects, and from all I've seen so far, what 
businesses are requesting is *features* from the later standards, and it 
becomes difficult for a *vendor* to justify the significant investment 
required to produce, say, the entirety of, say, 2002 COBOL if their entire 
current and potential user base responds with a loud yawn to all but a 
limited subset of the feature content of that standard.

I know *I* would have a real struggle convincing *my* management to invest 
compiler-development resources in providing full support for, say, 
"free-form reference format" -- either as part of a full 2002-compliant 
compiler or as a Unisys-extension to our COBOL85 implementation -- unless 
*at least* one user has indicated to Unisys that it's a real hot-button for 
them -- and so far as I know, none has done so.  I don't think that lessens 
the value of the standard itself, because I don't think having the standard 
be a guide to "If you're thinking of doing something like this, here's the 
way you should really consider doing it." is such a terrible thing.   I've 
said that many times in this forum.

I don't think the National Standards bodies are going to be convinced by us 
Techies.  I think they're going to have to be convinced by CEO's of Very 
Large Corporations as to how this affects *their* bottom lines. 
Furthermore, I don't think it's us Techies that are going to convince the 
CEO's of Very Large Corporations.  And even if either approach succeeded, 
I'm not convinced it's either WG4 or J4 that would be in a position to 
produce a regression suite -- in fact, I'd argue that the production of such 
a suite should be *entirely* outside the purview of either organization, so 
as to avoid the syndrome of the fox guarding the henhouse!

    -Chuck Stevens

<top post, no more below>

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:JBO8g.400208$BL7.371029@fe09.news.easynews.com...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
> news:e3vlh4$1tuv$1@si05.rsvl.unisys.com...
…[50 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-19T23:07:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lcsbg.126370$pd5.59180@fe03.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com>`

```
Chuck,
   Just a matter of clarification on this (and at least one other note).  Things 
may WELL have changed, but it was my understanding that you (Chuck Stevens) were 
NOT a member of J4 - but that Unisys was - and that you were their primary 
representative.

Therefore, when looking at "resources" that COULD (again "hypothetically") be 
applied to this (or certification tests or anything else), I believe that 4 of 
the 6 current J4 members are:

  Unisys
   IBM
   ITSCJ
   Micro Focus

(I haven't seen draft minutes to confirm that Micro Focus is still a member and 
that HP still is NOT).
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-21T01:57:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d8lijF18qrteU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com>`

```
 I read and considered this at length, Chuck. You make some good points, but 
the overall case is not persuasive.

Some comments below...

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e4l8g3$2kjv$1@si05.rsvl.unisys.com...
> Whether there are things "that COULD be done to improve the chances of 
> either the '02 or '08 Standards being implemented" is at least somewhat 
> orthogonal to the question as to whether I, or the other members of J4, or 
> the National Body representation to WG4, have the resources to carry out 
> such tasks.

Then the first priority of the committee should be to get properly resourced 
in order to do the job, right?

> With the Unisys-related duties I have as an employee of that company, I 
> consider myself lucky to fit my *current* duties for J4 and WG4 
> accomplished.  I am quite sure the same is true for the other 
> "corporate-sponsored" members of J4, and doubly true for those members of 
> J4 who are CEO's of the companies they represent.

While it is important to have senior management on the committee, that does 
explain why very little actually gets DONE! CEOs are not people who are used 
to DOING things... "I'll get my people to talk to your people..." They will 
happily sit on a committee and protect their strategic COBOL interests but 
none of that will get a new construct in the language or a poll done or a 
paper written...

> I know of nobody on J4 whose sole responsibility to their companies is the 
> COBOL standardization process, much less anyone whose primary financial 
> support stems from participating in that process.
>

So why are they there?

> As to your suggestions:  paraphrasing a certain official in the ISO/IEC 
> hierarchy:  "You shot it, you drag it home!"  ;-)

A colourful aphorism. See my comments on it elsewhere in this thread.
>
> For your item 1, I for one do not have the resources to perform such a 
> survey, nor do I believe any of the other five members of J4 have them.

What resources? It involves sending an email to all the COBOL vendors. 
(presumably, J4 has a list of contacts?)

It is a very good and useful idea and it SHOULD be done. It might be a bit 
unrealistic to expect them to tick boxes for every facility, but it could be 
worded so as to elicit the functions that they perceive as being most 
difficult, and therefore unlikely to be implemented.


> Since you have clear ideas as to how this can be accomplished, maybe you'd 
> be the appropriate person to carry out such a survey?   If not, why not, 
> and more particularly, why any individual member of J4 or the committee as 
> a whole more than you?

Because the COMMITTEE are the people who SHOULD be interested in the result. 
Bill is not on the committee so he has NOT volunteered his time and energy 
into doing this. The members of the committee have, it is in their interests 
to do it, and that is why the committee SHOULD do it, rather than Bill.

>
> Likewise, for your item 2, I have *even less* resources to allocate to the 
> development of a complete validation test suite for the 2002 standard, or 
> for the 2008 draft.

So, given that you cannot produce a yardstick for the proposed standard, why 
are you wasting time and effort producing it? It's like printing money 
without any way to verify whether it is genuine or not.

Actually, such a yardstick is essential, but there is no requirement that 
you or any other member of the committee must produce it personally. The 
function of the committee is to facilitiate; so get facilitating... :-) You 
already suggested one avenue that might achieve this.


>What resources are *you personally*, with or without corporate sponsorship 
>that you might arrange, be willing to bring to the table?   J4 would 
>welcome *any* volunteers to take this task on; I've already mentioned this 
>elsewhere.

There, you've already started facilitating :-) A public appeal for some help 
and on a specific topic too. Now get some of those CEOs to call in a few 
favours and make a few phone calls...:-)

>
> For item 3, I think much of this is already covered by "processor 
> dependent"; the problem is in getting the National Bodies to agree on what 
> should be "processor dependent" and what should be mandatory for all 
> environments.

Give them options and a finite time to consider them. At the end of that 
time go with a consensus. No appeals, no arguments. They had time to present 
cases and discuss the options; majority rules. Get over it.

>
> For item 4, J4 welcomes guests at its meetings (so long as we have 
> sufficient notice to provide accommodation for them).
(If I bring my own seat, can I turn up anytime? :-))

> We have used teleconferencing methods occasionally, but have found that 
> there are circumstances in which they are not as effective as face-to-face 
> discussion.

At the moment it seems to be a corporate toy, preferred by managers who 
fancy seeing themselves on a large screen. It IS useful when you need to 
have a committee meeting with one or more participants in disjoint 
locations. (That's when you are not sure whether they are in 'dis joint' or 
'dat joint'....). It is used regularly where I work, to have conferences 
with Australia, and it is very effective.   As for "circumstances in which 
they are not as effective as face-to-face discussion" the only cases I can 
think of are where you need to have a confidential discussion with an 
individual, or to physically pass documents or other instruments.
>
> Perhaps more to the point:  of the six attendees at the J4 meeting just 
> completed, *four* were representatives of end users, and only two 
> represented vendors.

Good! (Although there is nothing wrong with vendors being on J4...)

 In what way is J4 discouraging participation by end
> users?

By not facilitating such participation. It isn't enought to put processes in 
place. You need to actively encourage and make it easy for interested 
parties to attend. Alternatively, (maybe as well) get a web presence and a 
bulletin board where interested parties can discuss meeting agendas and 
points arising out of J4 meetings.

>  When was the last time you made the effort to attend a J4 meeting (as a 
> guest or otherwise)?

Hardly a fair question... the person it was directed at is not currently on 
J4 and has bad past experience with the red tape involved. If I were him I 
wouldn't want to attend either. If the question is directed to the community 
at large, I can say, speaking only for myself, I wouldn't attend a meeting 
where 6 people who have no clear agenda or idea of what they SHOULD be 
doing, are sitting round discussing COBOL. It's a big subject. You could 
discuss it for hours...

It isn't discussion that gets standards produced, it is drafts and revisions 
in the light of feedback. (It's called INTERACTION and ITERATION; 
fundamental to the RAD process... People who have been raised throughout 
their careers on SDLC and the Waterfall will struggle with this.


>
> << Besides the "mainframe-thought-process" of the 60's and 70's (and 
…[7 more quoted lines elided]…
> language standardization process, not just that for COBOL.

Why do you suppose they relaxed it?

>
> < <It would seem to  me that J4 (or WG4) *could* research what it would 
…[20 more quoted lines elided]…
> limited subset of the feature content of that standard.

Simple resolution to that problem... give them what they want and drop what 
they don't.
>
> I know *I* would have a real struggle convincing *my* management to invest 
…[12 more quoted lines elided]…
> Very Large Corporations as to how this affects *their* bottom lines.

Then you might as well quit now. NO CEO is going to bet the corporate farm 
on COBOL. It cannot be justified and no suitable Business Case can be made 
for it in this day and age. If you take a 3 year view, have extensive 
applications already developed in it, and a very static environment with 
little likleihood of Business or technology change, you MIGHT be able to 
prepare a suitable Business Case for upgrading or maintaining it in the 
short term. Long term, you can't. And astute CEOs know it. It isn't about 
the technical merits or otherwise, it is about the future of procedural 
programming in house as a solution to commercial IT requirements. The world 
has moved on, the network is becoming ever mightier, and tools and computer 
literacy are becoming exponentially greater than was the case in COBOL's 
heyday.

> Furthermore, I don't think it's us Techies that are going to convince the 
> CEO's of Very Large Corporations.

You got that right :-) Count on the bean counters... :-)


>And even if either approach succeeded, I'm not convinced it's either WG4 or 
>J4 that would be in a position to produce a regression suite -- in fact, 
>I'd argue that the production of such a suite should be *entirely* outside 
>the purview of either organization, so as to avoid the syndrome of the fox 
>guarding the henhouse!

Nope. Strongly disagree. It ain't the fox guarding the henhouse, it is the 
hens ensuring every egg has a little lion on it (sometime UK system of 
quality assurance for eggs).

Pete.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-05-21T09:47:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148230032.339594.178420@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4d8lijF18qrteU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net>`

```
Pete

In response to some of your comments, whIch I have been following.

J4 is the NCITS standard committee and WG4 is the ISO committee for
COBOL.  WG4 decides which features are to be developed from a long list
of suggestions that can be submitted to J4 or a national group by a
variety of interested people whether or not they are on either
committee.  J4 then develops them with occasional participation by
non-members.

As far as I can make out anyone can be a national delegate to WG4 if
their country is participating and, if not, can often participate
through a country in which they work.  Jeanette Nutsford from New
Zealand is an example who has participated via the UK group, I don't
know whether there is an NZ group through which she can participate
while there..  About the only requirement I can see for being a
national committee member for the development of COBOL is an interest
in developing the standard and anyone can be a appointed as a delegate
(sometimes several from each country, though only with one joint vole)
to attend the WG4 meetings that are co-ordinated and co-located with J4
meetings, most of which are in the US with a few in Japan and Europe,
which reflects the majority membership.  Though not all J4 meetings
have an associated WG4 meeting, there are usually something like two
WG4 meetings to 6 J4 meetings per year, WG4 members can still follow
the documents issued for each meeting and make reasoned comments
regarding the iterative process of developing features via proposal
documents that are reviewed and revised before eventual acceptance.

Robert
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-22T05:32:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q1ccg.172325$pd5.79049@fe03.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com>`

```
Robert,
   FYI - the requirements for being a WG4 delegate are set by each "national 
standards body" (or its technical committee).  For example, the US delegation 
(at least the last time I checked) REQUIRED that one participate in 1 of the 
last 2 J4 meetings (for example).  Similarly, when Ian Mooney was still 
participating from Canada, Jimmy tried to get on that delegation and was told 
that he couldn't do so.  (I don't recall the full details).

I suspect that anyone wanting to participate *MIGHT* be able to find a country 
whose delegation would allow them to participate - however, there is certainly 
no guarantee of that.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 12)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-05-23T18:39:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gFIcg.184820$WI1.7656@pd7tw2no>`
- **In-Reply-To:** `<q1ccg.172325$pd5.79049@fe03.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com>`

```
William M. Klein wrote:
> Robert,
>    FYI - the requirements for being a WG4 delegate are set by each "national 
…[9 more quoted lines elided]…
> 
Update for Robert.

Knowing that there was at the time a Canadian rep for J4, (although I 
don't know the last time Canada participated), Bill put me in touch with 
him back in 2000 - I think it was the Ian Mooney he refers to above. Ian 
worked at a Canadian subsidiary, (in Ontario), of a US company but had 
been ill for quite some time. When he eventually returned to his office 
he found our US cousins had closed and emptied the office ! Insufficient 
funds to cover his traveling expenses, he just quietly opted out. 
Presumably if I had been prepared to foot my own bills, technically I 
could have joined J4, which (in theory) would have made me the Canadian 
J4 rep ???

As it was, Bill knew that Stephen Spiro, (US independent), couldn't 
attend that Newbury meeting so suggested I contact him as a stand-in. To 
cover his arse, Stephen had three 'substitutes, yours truly, Huib Klink 
from Netherlands (Chuck referred to him as Don Schricker's deputy as he 
is apparently currently on the M/F payroll) and the gent from the U. of 
Leicister who spent his time snoozing next to Don up the end of your 
side of the table. Huib was sat at the end of the row next to Wim E (?) 
also for Netherlands.

Back to Huib - at the time he was working for an independent software 
house and somebody suggested he should join J4. (A very good technical 
man, particularly OO - as Bill, Donald or Pete could attest to from 
softwaresimple days - when a small group of us were discussing OO). 
Huib's comment sums it up nicely, "My boss is going to ask, 'What's in 
it for me ?'".

Naturally I was making a vacation, (first trip back since '75), as well 
as attending the J4 meeting. As I was going to be there in Newbury made 
sense I should sit in on some  of the ISO(WG4) meeting to see how that 
functioned. Ian put me in touch with the Canadian WG4 team - what a run 
around. Yes I could certainly participate PROVIDED I made a commitment 
to be a member and attend their *own* meetings which could be say in BC, 
Ontario and perhaps Quebec. - assuming I had the money to become a 
'frequent flyer'. So I didn't see any of the WG4 action.

Don't know whether Chuck is prepared to expand. ISO is a bit like the 
bloody Free Masons. Rules are set at their HQ in Zurich (?) and they 
seem to be obsessed with confidentiality - makes them more secretive 
than Opus Dei :-). So there is bureaucratic BS with ISO, not dissimilar 
to the nonsense you have with separate MEPs attending the EU Parliament, 
doing their own thing, independent of the MPs in the House of Commons, 
and the Euro bureaucrats determining that UK sausages are inedible !

See if you can get a handle on ISO/WG4 - I've had no luck googling for 
WG4 representatives for the various countries. Certainly their 
deliberations are confidential. (Apparently both the Ukraine and the PRC 
were going to make contributions/comments on the TR for Collections - 
don't think it ever happened).

I don't want to get into the argy-bargy on COBOL - and as of to-date I 
don't think I want to program any longer in any language or script !
But with the couple of threads tackling COBOL at the moment - I think 
the following is NUMERO UNO :-

Will COBOL survive ? And I don't mean do James, Pete or Robert think 
that COBOL will survive. Much more pertinent, do the people spending 
money on developing COBOL compilers think that COBOL will survive. I'm 
not thinking of just the four vendors on J4 but ALSO Liant (RM/COBOL), 
Acu, HP/Compaq, KOBOL and the Open Source 'Johnnies' etc.

Certainly the J4 structure could act as 'host' encouraging ALL 
(including the non-J4 participants) to attend a Brain-storming session; 
  if they reluctantly agree that it is only a question of time before 
COBOL becomes just an historic blip, then all the other suggestions, 
e.g., 'Can we get everybody to agree about a Standard and implement it 
?', or Bill's left of field suggestion of a separate PC version, just 
become academic idealism.

I could offer some positive suggestions - sadly I just don't see them 
being seriously taken up. It is probably too late to try and view the 
topic with a different perspective anyway.

Reflect on this topic of COBOL - Have you noticed how many hundreds of 
the participants in this Newsgroup have done cartwheels of joy, to get 
involved and put in their two cents of suggestions ? (So many of them 
are just waiting for that magic birthday - when they are 65 !).

Jimmy
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 13)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-23T16:08:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e504kq$31bq$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:gFIcg.184820$WI1.7656@pd7tw2no...


> Presumably if I had been prepared to foot my own bills, technically I 
> could have joined J4, which (in theory) would have made me the Canadian J4 
> rep ???

J4 membership presumes INCITS (previously NCITS) membership, which in 
addition to the costs of attending the J4 meetings (and the fees to cover 
the costs of those meetings) has its own membership fees, which some private 
individuals have protested were too high.

At the time you're discussing, J4 and the US Technical Advisory Group to WG4 
were separate (the latter consisting of the US members of J4); their 
functions were subsequently merged and the membership distinctions erased.

In the last reference I see, Canada is still a "P" member of ISO/IEC 
JTC1/SC22, the parent organization to WG4, but eligibility to be a Canadian 
delegate (or even to be HoD) is a Canadian question.

> ... Stephen had three 'substitutes,

Technically, "alternate members".

> yours truly, Huib Klink from Netherlands (Chuck referred to him as Don 
> Schricker's deputy as he is apparently currently on the M/F payroll)

Last we heard, yes.  But, again, Huib was Don Schricker's alternate *as J4 
rep for Micro Focus*; that conveys nothing as to Don's position as chair.

> Wim E. also for Netherlands.

Wim retired at the WG4 meeting at The Hague, with a ceremony conveying a 
knighthood on behalf of the Dutch government.

> Back to Huib - at the time he was working for an independent software 
> house and somebody suggested he should join J4. (A very good technical 
> man, particularly OO - as Bill, Donald or Pete could attest to from 
> softwaresimple days - when a small group of us were discussing OO).

I agree; I've seen Huib at several WG4 meetings, and he's an asset to the 
process.  Wish we cound get him to cross the pond for J4 meetings.

> Naturally I was making a vacation, (first trip back since '75), as well as 
> attending the J4 meeting. As I was going to be there in Newbury made sense 
> I should sit in on some  of the ISO(WG4) meeting to see how that 
> functioned.

Somewhat confusing in a case like that, when part of the meeting's J4 and 
all of a sudden everybody puts on different hats because it's become a WG4 
meeting ... and then a couple of days later everybody changes hats again and 
it's back to J4 ...

> Ian put me in touch with the Canadian WG4 team - what a run around. Yes I 
> could certainly participate PROVIDED I made a commitment to be a member 
> and attend their *own* meetings which could be say in BC, Ontario and 
> perhaps Quebec. - assuming I had the money to become a 'frequent flyer'.

Sorry to hear that -- but similar rules apply in the US, which does have 
eligibility requirements as to who can be a US delegate, and in our case, if 
I remember it right, that includes attendance at either the two most recent 
J4 meetings as a member or at the most recent WG4 meeting as a US delegate. 
So in at least the case of these two countries, some demonstration of 
commitment to the process is expected!

> So I didn't see any of the WG4 action.

Even at Newbury?

> Don't know whether Chuck is prepared to expand. ISO is a bit like the 
> bloody Free Masons. Rules are set at their HQ in Zurich (?) and they seem 
…[4 more quoted lines elided]…
> Euro bureaucrats determining that UK sausages are inedible !

On the other hand, people might expect to show up and get everybody to jump 
on board for one idea or another, when the likes of DIN and BSI have spent 
significant time and effort crafting positions that the newcomer to the 
process might not like.

> See if you can get a handle on ISO/WG4 - I've had no luck googling for WG4 
> representatives for the various countries.

ISO/IEC Working Group *membership* and *representation* is by *country*, 
just as INCITS/J4 membership is by *company*.  One country, one vote, hence 
the importance of the National Standards Bodies establishing positions.  And 
the Head of Delegation for a country (to say nothing of the composition of 
the delegation as a whole) is established by the National Standards Body for 
that country some time before the Working Group meeting.  What the 
composition of the delegations was at one meeting need have no bearing on 
what it will be at the next.

> Certainly their deliberations are confidential. (Apparently both the 
> Ukraine and the PRC were going to make contributions/comments on the TR 
> for Collections - don't think it ever happened).

I remember that we were expecting comments, but haven't received them. 
Note, however, that the Collection Class library TR has not yet gone to 
*formal* international review.

> I don't want to get into the argy-bargy on COBOL - and as of to-date I 
> don't think I want to program any longer in any language or script !
…[4 more quoted lines elided]…
> COBOL will survive.

I think that depends on what you mean by "survive".  There's a heck of a lot 
of software out there that's still running, and it's still in COBOL, and 
it's still getting recompiled and tweaked so that it continues to run on new 
platforms and new releases of software, and it's still serving the needs of 
major international corporations.  Do I think all that stuff's going to get 
replaced by applications written in Java or C++ next week, or next year, or 
two years from now?  No, I don't; in fact, I would not be at all surprised 
to see Unisys working to keep its *COBOL74* compiler running five, and 
probably ten, years from now.  We started trying to get rid of our COBOL(68) 
compiler in the late 1980's, finally "pulled the plug" at the end of 1999, 
and had customers paying us Many Bucks to continue to support it Just For 
Them for a couple of years more!

> Much more pertinent, do the people spending money on developing COBOL 
> compilers think that COBOL will survive. I'm not thinking of just the four 
> vendors on J4 but ALSO Liant (RM/COBOL), Acu, HP/Compaq, KOBOL and the 
> Open Source 'Johnnies' etc.

I think to a degree the points are orthogonal.  There is much about COBOL 
that is Trailing Edge Technology, and one of the benefits of Trailing Edge 
Technology is that, by and large, it works.

> Certainly the J4 structure could act as 'host' encouraging ALL (including 
> the non-J4 participants) to attend a Brain-storming session;

Did that, specifically, in June 2003, just before the WG4 meeting in Las 
Vegas, in June of that year.  Did everything we could to publicize it, I 
think including here in this forum.  Some people came, and a number of ideas 
were brought forward from that COBOL workshop to the WG4 meeting.

>  if they reluctantly agree that it is only a question of time before COBOL 
> becomes just an historic blip, then all the other suggestions, e.g., 'Can 
> we get everybody to agree about a Standard and implement it ?', or Bill's 
> left of field suggestion of a separate PC version, just become academic 
> idealism.

Again, I've said repeatedly I think there is value in a standard even if it 
is simply to provide guidelines for implementors as to how a consortium of 
interested parties think a given feature should be handled.

For example, one of the things WG4 has historically taken a strong stand on 
is the idea that new features in the language should be available to the 
user of "core COBOL"; limiting stuff like user-defined functions to the 
OO-style environment does not further the cause of *growing* COBOL, it 
basically is a divisive move.

> I could offer some positive suggestions - sadly I just don't see them 
> being seriously taken up. It is probably too late to try and view the 
> topic with a different perspective anyway.

Might well be.  We do what we can!

> Reflect on this topic of COBOL - Have you noticed how many hundreds of the 
> participants in this Newsgroup have done cartwheels of joy, to get 
> involved and put in their two cents of suggestions ? (So many of them are 
> just waiting for that magic birthday - when they are 65 !).

I'll be 62 next month ...     ;-(

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 14)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-05-24T02:48:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bQPcg.184184$P01.162682@pd7tw3no>`
- **In-Reply-To:** `<e504kq$31bq$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:gFIcg.184820$WI1.7656@pd7tw2no...
…[34 more quoted lines elided]…
>
Understood - stand-in for Don on behalf of M/F - not automatically 
assuming the chair.

>>Wim E. also for Netherlands.
> 
…[44 more quoted lines elided]…
> Even at Newbury?

Yes, even at Newbury. The nearest I got to WG4 was having a supper one 
night with Ann and Don, when she was both a member of J4 and Covenor of 
WG4. I made a lousy menu selection at a very swish eatery. I'd been 
forewarned by Ian that J4 folks are 'thrifty' - you each pick up your 
own tab for eats.

> 
>>Don't know whether Chuck is prepared to expand. ISO is a bit like the 
…[105 more quoted lines elided]…
> Might well be.  We do what we can!

Actually my thoughts are quite radical, completely disregarding the 
setup you have 'grown' into. Two immediate impressions :-

1. Get rid of the friggin document you have at the moment. Over 1,000 
pages and still growing - or will be once you start adding the TRs in - 
when 2010 ? Seriously you get the ISO imprimatur for 2008, earliest 
anybody is likely to implement 2009 - *IF* THEY IMPLEMENT; the earliest 
you could get reaction to TRs is 2010/2011 when END USERS have bitched 
to their vendor that the TRs don't work so good !

Hint, hint you still haven't got :-

	invoke thisCollectionObject "quitIteration"

to break out of the iterative loop. It maybe the way that they have done 
it but with M/F if on a conditional test you try to do EXIT METHOD - it 
doesn't work; it only breaks out of an iterative loop, (not necessarily 
the method), with 'quitIteration'.

The replacement for the existing documentation - triggered by Richard 
posting those ICL syntax crib sheets, which of course are in most LRMs. 
If for example it's 'INSPECT REPLACING' show the standard syntax 
IMMEDIATELY followed by umpteen examples showing all the options. Use 
*absolute* minimal wording to describe any nuances which may apply.

You may recall I posted something for Chris where he wanted a picture of 
a box. Did it with the M/F Screen Section syntax. I was real clever ! No 
I wasn't - I cribbed it from an existing M/F example. I can assure you 
that if I had bothered to read the M/F 'words' for the extended syntax I 
would probably never have latched on to the features available. Two 
'goes' at adjusting the existing example which was for a two-dimensional 
table, gave me the result that I could just code DISPLAY SCREEN-BOX, a 
reference to a 50 x 25 Table.


2. What follows from #1 above - more or less your COBOL test suite 
BECAUSE "somebody" having taken the first shot, (a developer at IBM, 
Unisys, Liant, Acu, M/F, F/J, Fujitsu-Siemens, KOBOL, Open Source 
etc...), you publicise the site to the outside world for the examples 
and a small dedicated group receives enhanced/updated examples which 
they accept/reject and if OK are further added to the list of examples.

This example thing is not a new one; I believe it was a topic at J4 
about five years back. Trouble is you work for people who pay you but 
you want US (Certainly most PC-users, the people that have to pay 
ourselves), to initiate this idea.

Just those two points alone show how radically different our thoughts are.


> 
>>Reflect on this topic of COBOL - Have you noticed how many hundreds of the 
…[5 more quoted lines elided]…
> I'll be 62 next month ...     ;-(

And should be showing a bit more responsibility at that age ! Visions of 
somebody fitted out with a biker helmet emblazoned with Teutonic 
symbols, studded jacket, and the boots of course. Jerome G could have 
asked his brother Art to come up with different lyrics, to that lovely 
theme which you could have hummed to yourself while on the road,

(H. David, A. Hammond)
Keeping my eyes on the road, I see you.
Keeping my hands on the bars, I'll greet you.
99 Miles From J4, I miss you, I miss you, please be there.
Passing the cryptic agenda, we're sailing.
Turning the laptops on, we're dancing.
99 Miles From J4, I want you, I need you, please be there.
The windshield is covered with rain, I'm cryin'.
(** Have you got one on your bike ? )
Pressing my foot on the gas, I'm flyin'.
Counting the e-mails, I'll mail you.
Reading the TRs on my tank, I'll write you.
99 Miles From J4, we're laughing, we're loving, please be there.
Counting the e-mails, I'll mail you.
Reading the TRs on my tank, I'll write you.
99 Miles From J4, we're laughing, we're loving, please be there.

Puhleese be there !

  :-)

Don't rush to respond - I'm vacationing for a week.

Jimmy
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T07:47:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e51rlq$10r6$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no>`

```
A few points (I may come back to others later) interspersed below:

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:bQPcg.184184$P01.162682@pd7tw3no...

<snippage>

> Actually my thoughts are quite radical, completely disregarding the setup 
> you have 'grown' into. Two immediate impressions :-
…[6 more quoted lines elided]…
> their vendor that the TRs don't work so good !

First off, the reason we came up with TR's is so that they would get 
exposure *before* they went into the 2008 standard -- the TR's are actually 
applicable to the *2002* standard.

More on the size of the document below, relative to your suggestion about 
how to resolve that.

> Hint, hint you still haven't got :-
>
…[5 more quoted lines elided]…
> the method), with 'quitIteration'.

I really have no expertise in the OO arena, either in COBOL or otherwise.  I 
make my living writing code in ALGOL dialects!     ;-)

> The replacement for the existing documentation - triggered by Richard 
> posting those ICL syntax crib sheets, which of course are in most LRMs. If 
…[3 more quoted lines elided]…
>
As to the size of the document, well, yes, COBOL is wordy and the standard 
is wordy.  But rules are both indicative of what is *permitted* and what is 
*prohibited*, and limiting the description of the language to diagrams and 
examples -- where there is a near-infinite set of the cases that are 
*permitted* as well as a near-infinite set of the cases that are 
*prohibited* -- does not lend itself to a more concise document!  Both the 
COBOL language and the rules in the standard itself have grown to be 
decidedly Baroque, I'll grant readily.  But getting rid of rules that 
reflect forty-five years of precedent is likely to allow for 
incompatibilities with prior standards, and *evolution* is important for 
both the language and the applications written in it.

As an example, I just closed a customer problem report (against COBOL74!) 
complaining that when the Unisys extension that allowed any character in a 
PICTURE character-string outside of the strict ANSI syntax to be treated 
like "0" or "/" was turned on, a value like "-12.34" put into a data item 
declared "PICTURE -(3).ZZ"  contained something like " -1.ZZ".  What exactly 
is wrong with "PIC -(3).ZZ", and how are you going to state what's wrong 
with it in a simple syntax diagram and a set of examples all of which 
compile successfully?

In this instance, the customer did not know that the PICTURE was against 
standard COBOL rules; I cited ANSI X3.23-1974 page II-20, 4.7.4, PICTURE 
clause, General Rule 8, specifically, the paragraph dealing with "Z", " ... 
may only be used to represent the leftmost leading numeric character 
positions ...", and in this instance, the leftmost leading character 
positions are represented by "-" instead, and also pointed him to our 
documentation that said the same thing.  In this case, "PICTURE -(3).99 
BLANK WHEN ZERO" was what the customer wanted, and they were satisfied by 
the response.

There are *a lot* of nuances that apply.

> You may recall I posted something for Chris where he wanted a picture of a 
> box. Did it with the M/F Screen Section syntax. I was real clever ! No I 
…[5 more quoted lines elided]…
> 50 x 25 Table.

Extensive examples have been frequently suggested to J4, and a lot of that 
ends up in the CONCEPTS annex.   The standard is not a reference manual for 
a particular COBOL implementation or a replacement for Thane's book; I think 
its *primary purpose* is as a list of do's and don'ts *for the people who 
are writing COBOL compilers*.  It is *the ultimate reference* to the 
language, and has to be comprehensive in both its inclusions and its 
exclusions.  I am not convinced that the exclusions are adequately covered 
by examples of inclusion.

More when I get time and opportunity                .

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-24T21:29:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ze4dg.46743$bL2.29466@fe02.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e51rlq$10r6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e51rlq$10r6$1@si05.rsvl.unisys.com...
<snippage>
> As to the size of the document, well, yes, COBOL is wordy and the standard is 
> wordy.  But rules are both indicative of what is *permitted* and what is 
…[9 more quoted lines elided]…
>

It might be worth mentioning that during the development of the (eventually) '02 
Standard, there was a reasonable amount of discussion of TRYING to change to

A) A "BNF" grammer
        and/or
B) Any other "formalized" programming language grammer (recognized by ISO or 
others)

It was thought (and I certainly agreeed with this) that the "project" of 
CORRECTLY converting the current format to such a grammer would not just be 
resource-intensive (VERY) but also be incredibly "error-prone".

At the time that I was still a Micro Focus rep on X3J4 (and CCC) Ann Wallace 
(later Bennett) and I would "joke" about the fact that we could "randomly" pick 
a page in the '85 Standard and find SOME error (or contradition) in it. 
Although "fixing" all of these by going to a *NEW*  "foramlized" language 
grammar might be "nice" it would have broken many, MANY programs and 
implementations.  Instead, via the interpretation and revisionprocess (as slow 
as it is/was), all changes (that we did make) in "wordy definitions" were 
INTENTIONAL and where they intentionally introduced changes, such were 
documented.

It may (or may not) be worth noting that the COBOL Standard has used the same 
"descriptive methodology" since 1960 (or so) while programming language "theory" 
has changed dramatically.

If we could only start over "fresh" .... (who knows what we would have)
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 17)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T14:51:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e52kgu$1fe0$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e51rlq$10r6$1@si05.rsvl.unisys.com> <ze4dg.46743$bL2.29466@fe02.news.easynews.com>`

```
... And WG4 and J4 are watching the "Grammarware" research as it applies to 
COBOL syntax (and the COBOL standard) that's being done at Vrije 
Universiteit Amsterdam ... One of the things I hope might come out of that 
is a better (and more accepted) way of expressing the syntax diagrams, 
another is the discovery of errors in the current diagrams that an automated 
notation-translation process might make more obvious in a different 
notation, or even choke on.

    -Chuck Stevens

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:ze4dg.46743$bL2.29466@fe02.news.easynews.com...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
> news:e51rlq$10r6$1@si05.rsvl.unisys.com...
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T10:03:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e523kd$15fl$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no>`

```
Part 3 (not exactly COBOL related):

>> I'll be 62 next month ...     ;-(
>
> And should be showing a bit more responsibility at that age !

Rode a bike from '86 to '96 when I was involved in an accident on my '73 BMW 
(a toaster-tank SWB R75/5 for those who might know of such things).

I'd like to say I "laid 'er down", but what happened was I got squirted off 
the bike like a watermelon seed when I got hit broadside after blowing a red 
light, and I and the bike went flying in different directions!

Anyway, when anybody struts the "I laid 'er down" line, I think to myself 
"Yeah.  That's biker-speak for 'I fall down go boom get big owie.' "  I 
chuckle (snicker, even) every time I hear it.

When I brought up the subject last Labor Day weekend of getting another 
bike, after coming to the realization I'd done ten years penance as of 
September 17 for misreading that light, my wife thought a minute, and 
responded "If not now, when?" and figured I'd be better off having a bike 
*now* than when I'm 75 or 80.  That was around 6PM on Saturday September 3, 
and by 8:30AM on Tuesday September 6 (the very next opportunity; the dealer 
closed at 6 on Saturday and didn't open again until 8 on Tuesday) I was 
riding home on my BMW R1100RA.  Since that date I've put 4100 miles on my 
Toyota Avalon (a very nice car indeed) and 14,700 miles on the bike.

My commute in the cage used to be stop-and-go all the way up the I-5 from 
Mission Viejo to Anaheim, about 24 miles.  Now I take surface streets to the 
Santiago Canyon Road, and it's about 33 miles, and it's a sweet, sweet ride. 
I take the same route in the cage these days, but 't'aint the same.

> Visions of somebody fitted out with a biker helmet emblazoned with 
> Teutonic symbols, studded jacket, and the boots of course.

Well, my helmet's modular full-face, currently emblazoned only with a BMW 
roundel and the Flag of the Republic of Texas on the back; my jacket and 
chaps are unadorned; I own no vest at the moment; and my boots are Western 
in style (can't shift reliably in thick biker boots) -- relatively 
inexpensive Dan Posts.   I've got a number of HD-ridin', patch-holder 
friends, though (and a few one-percenters), so I'm hardly unfamilar with the 
style and subculture.

I do wear a helmet, not because the law requires it, but because I prefer 
both the protection and the noise insulation helmets (in particular 
full-face helmets) provide.   My choice, my preference.

> Jerome G could have asked his brother Art to come up with different 
> lyrics, to that lovely theme which you could have hummed to yourself while 
> on the road,

Met Jerome at an OO Ad Hoc back when Vickie Gould was involved with the 
COBOL standards process.   Haven't seen him since, though.

My musical training is almost entirely classical (I have two flutes and a 
piccolo, all of good professional-symphony-orchestra quality; I also have a 
clavichord in our living room), so I don't recognize the tune to which 
you're referring.  Title please?

Enjoyed the lyrics!  A few points ...

> The windshield is covered with rain, I'm cryin'.

What comes to me on this line is more like:

    I'm ridin' in the rain
    Just ridin' in the rain
    What a glorious feeling,
    I'm happy again!  ...

I think you can figure out the tune to that one ...  I've actually found 
myself singing that one, in the rain, on several occasions!   Man, oh, man!

I don't like bein' in a cage.  I like bein' on my scoot.

I ride in the rain.  I like riding in the rain.  I like riding when it's hot 
out.  I like riding when it's cold out.

I rode to Las Vegas for the J4 meeting in full leathers (including chaps, at 
my wife's request) and when I went through Baker it was 117 degrees.  My 
feet, being behind the cylinders, got a bit warm.  I like riding.  I 
commuted from my home to the previous J4 meeting in Ontario every day along 
the Carbon Canyon Road.  On the last day, I took a *long* route from Anaheim 
to Ontario, via the Santiago Canyon Road, Live Oak Canyon Road, San Juan 
Capistrano, the Ortega Highway, Lake Elsinore and Corona.  Was a half-hour 
late for the meeting that morning.  Oh, well.  I like riding.

 When I leave for work in the morning, if the temperature's below 40, I wear 
my heated gear.  If it's below 42, I wear my chaps.  If it's below 45 I wear 
my winter gloves and keep the liner in my winter jacket.  If it reaches 50 I 
switch to the summer jacket.  I like riding.  If it's raining when I leave 
for work I'll put on my rain gear, and if the forecast says it's supposed to 
rain I'll take my rain gear with me.   I like riding.

Whoa, doggies!  Man, oh, man, do I like riding!  It brings me joy.  I don't 
think I really had a clue what "happy" meant until I got this bike.

[I will admit that I'm not sure I'd be comfortable riding a street bike like 
mine in snow or ice, and I don't think I particularly want to try.]

> (** Have you got [a windshield] on your bike ? )

I have a windshield *for* my bike, had it mounted, took it off, put it back 
on again, and took it off again just before my round trip from the Southern 
California coast to the Hill Country of Texas in April.  I'll keep it around 
as an accessory to include with the bike (along with the Corbin saddle setup 
I bought really inexpensively on the internet, which saddle doesn't fit me 
as well as I'd hoped) if I ever decide to sell it and get a different one. 
I have NO intention of putting it back on as long as I'm riding it.    I'll 
put the Corbin back on when I send the stock seat pans off to have a more 
comfortable saddle done -- probably this fall.   The stock saddle's 
generally acknowledged as not very comfy long term.  Then the Corbin will go 
back on the shelf.

The aerodynamics of my helmet are beyond reproach.  I've learned to deal 
with buffeting on the body without the windscreen; I learned that on the 
I-10 eastbound toward Texas.  At one point I was traveling 90mph in the slow 
lane and got passed by a semi; shortly thereafter I found myself in traffic 
on the right lane cruising along at 110 (held that speed for about 90 
minutes).    My experiments before the trip convinced me that the windscreen 
raises the noise level around the helmet to an unacceptable level.  The 
noise level *without* a windscreen with this helmet is a quiet rush.   There 
may be bike-and-windscreen combinations that work really well, but as far as 
I'm concerned the stock windscreen on a R1100R ain't a combination that 
works for me.   And yes, I've tried a laminar lip.  I've learned to ride 
without a windscreen, learned to *really like* riding without a windscreen, 
and have no particular desire to have a bike with one.

[And as far as the speed goes, riding *with traffic* is a whole lot safer 
than riding at the speed limit, if traffic's going faster than the speed 
limit.]

When I come back from a long ride, I offer a moment of silence for all those 
who sacrificed their lives so that I might ride, before I clean off my 
helmet visor so I can see through it again ...  Whoa, buggies!     Man, oh, 
man!     ;-)

> Pressing my foot on the gas, I'm flyin'.

I don't know if I've *ever* seen a bike with a foot-operated throttle!  On 
most bikes I know of "grabbin' a handful of throttle" or "rollin' it on" 
comes closer ...

Maybe somebody'll get a kick out of this anecdote  ...         8-)

   -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-24T11:44:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com>`
- **References:** `<4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com>`

```
On Wed, 24 May 2006 10:03:09 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>I rode to Las Vegas for the J4 meeting in full leathers (including chaps, at 
>my wife's request) and when I went through Baker it was 117 degrees.  My 
>feet, being behind the cylinders, got a bit warm. 

In my one motorcycle accident, I was wearing a WWII leather jacket,
but normal pants.   My jacket and gloves were torn up, my helmet was
scratched, but my only personal damage was to my leg.    

Leather can be hot, but it protects.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 17)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T11:19:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5283o$184f$1@si05.rsvl.unisys.com>`
- **References:** `<4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com...

> In my one motorcycle accident, I was wearing a WWII leather jacket,
> but normal pants.   My jacket and gloves were torn up, my helmet was
> scratched, but my only personal damage was to my leg.
>
> Leather can be hot, but it protects.

I almost always wear jeans, which are at least a little better than slacks. 
I agree that chaps protect.  And *so long as I'm moving* chaps really aren't 
that much of a heat problem.  Problem is that my 33-mile commute includes 
about 21 miles of normal surface streets and only about 12 miles of canyon 
road.  And I need to get a new pair; my current ones were *very* 
inexpensive, and turned out to be worth every penny.

In the case of my '96 wreck, two metatarsals in my left foot were crushed, 
my right fibula was broken at the ankle, I had a hairline fracture on the 
left femur, I had hefty soft-tissue damage to both knees (which still bother 
me occasionally, as does the left foot, which has two screws in it), and I 
had deep-purple bruises covering the inside half of both thighs from below 
the knee to the groin that took a long time to fade.  I was on 2x750mg 
Vicodin q4h 24/7 for a month, in a wheelchair for two, and on crutches for a 
month after that.   I came back to work maybe three weeks after I got off 
the painkillers.

My summerweight leather jacket suffered an abrasion on the right shoulder 
and elbow, my helmet suffered a quarter-sized paint-scrape off the back 
center, and I suffered no road rash *at all*.   I don't think I was wearing 
chaps at the time.  I'd still be wearing that jacket, except that, alas, it 
shrank to the point that I couldn't zip it up any more ... Amazing how 
leather does that as it ages ... Too bad, nice jacket ...

I'd have gotten right back on a bike as soon as I could walk, but since my 
wife had come to the accident scene and hauled me off to the ER, and it was 
her birthday, I didn't push the idea too hard at the time ... Her request 
that I not jump back onto a bike wasn't unreasonable ... and she still 
panics when I get on the bike ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 18)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-24T12:35:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com>`
- **References:** `<JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com> <e5283o$184f$1@si05.rsvl.unisys.com>`

```
My accident occurred the evening that I was drafted.   I happened to
be in AFROTC at the time, so I was able to get my deferment.   I was
driving towards Drake University with my chess board to go to chess
club when a car pulled out of a bar and hit me.   I was always told to
make sure to get the license of a car that was involved in an
accident, and I did, it was embedded in my leg.

The driver stopped for a moment and then left, saving himself a felony
(drunk or hit and run).   Leaving the scene of the accident didn't
work if I had his licence plate.    Six months later I was in ROTC
Summer camp.   I did get a year of school paid for though - my grades
weren't nearly as good as they were when I worked full time, as I had
plenty of time to study/procrastinate.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 19)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T12:06:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e52ark$19r0$1@si05.rsvl.unisys.com>`
- **References:** `<JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com> <e5283o$184f$1@si05.rsvl.unisys.com> <uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com...

> I was always told to
> make sure to get the license of a car that was involved in an
> accident, and I did, it was embedded in my leg.

The plate itself, or the information on the plate?

> The driver stopped for a moment and then left, saving himself a felony
> (drunk or hit and run).   Leaving the scene of the accident didn't
> work if I had his licence plate.

Not sure why that would make a difference; surely the license plate (or its 
image) would be considered some sort of evidence that at least his car was 
there and was involved ...

Alas, "There's two kinds of bikers:  thems that've been down and thems 
that're goin' down ..."

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-24T13:52:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p3e972p9udr7bod1lb5ualndqm6opra338@4ax.com>`
- **References:** `<4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com> <e5283o$184f$1@si05.rsvl.unisys.com> <uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com> <e52ark$19r0$1@si05.rsvl.unisys.com>`

```
On Wed, 24 May 2006 12:06:28 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>> I was always told to
>> make sure to get the license of a car that was involved in an
>> accident, and I did, it was embedded in my leg.
>
>The plate itself, or the information on the plate?

Maybe I should have asked, instead of just assuming...

>> The driver stopped for a moment and then left, saving himself a felony
>> (drunk or hit and run).   Leaving the scene of the accident didn't
…[4 more quoted lines elided]…
>there and was involved ...

If he hadn't stopped, it would have been a Hit & Run felony.   If he
had stuck around, he would have had Drunken Driving felony.   As it
was, he got charged with Leaving the Scene of the Accident.

>Alas, "There's two kinds of bikers:  thems that've been down and thems 
>that're goin' down ..."

A friend of mine is a horse man.   For a while on his cubicle he had
an article saying "If you spend time around horses, you will get
hurt".


As a programmer, I know that "things will happen".   I might be called
in the middle of the night because I overlooked something, my users
overlooked something - or maybe there was something unforeseeable.   I
keep hearing people say that most crimes don't get solved.   Well most
of my programs work fine as well, but things Will happen.   If my
business is crime, then I will pay the cost when something happens.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 20)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-05-24T13:36:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148502990.573171.132720@j55g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e52ark$19r0$1@si05.rsvl.unisys.com>`
- **References:** `<JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <2q6972p87ug60snd33799lhfo31dq81l7d@4ax.com> <e5283o$184f$1@si05.rsvl.unisys.com> <uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com> <e52ark$19r0$1@si05.rsvl.unisys.com>`

```

Chuck Stevens wrote:
> "Howard Brazee" <howard@brazee.net> wrote in message
> news:uh9972pun9kb6mephkavcjsdue17snsabt@4ax.com...
…[4 more quoted lines elided]…
>

If one takes biking seriously enough then it is inevitable that one is
going down. In the UK, the average period of riding a bike before a
serious accident occurs is two years. I managed six years before
breaking my collar bone (my fault).
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 16)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-03T00:43:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GW4gg.223560$P01.73255@pd7tw3no>`
- **In-Reply-To:** `<e523kd$15fl$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> Part 3 (not exactly COBOL related):
> 
…[7 more quoted lines elided]…
> (a toaster-tank SWB R75/5 for those who might know of such things).

Having read you, Howard and Alistair comin' a cropper on those beasts - 
I knew I was right to avoid them ! A much more modest progression - a 
tricycle when five, (went around the family among cousins, with a fresh 
coat of paint each time until it arrived back on my doorstep for my kid 
  some thirty years later. Possibly only improvement a fresh set of 
rubber hand-drips and brakes ! I don't think the modern phrase 'built-in 
obsolescence' had been invented back then). Teen years a bike (bicycle); 
nothing fancy, an 'Hercules' with standard handlebars, not your sports 
drop-downs.

Real progression - a moped - a bike with an engine in the back wheel - 
Wowee ! Perhaps 20 mph. You probably wont know this one, a 'Corgi'. A 
miniature two-stroke motor-bike - folded and was used to drop alongside 
paratroopers by parachute during WW2. You were sat with your arse about 
ten inches from the road surface. As somebody in the Sergeants' Mess 
unkindly put in once, "I looked like and elephant sat on a pea :-) ).

58/59' bought a spanking new Lambretta. (I note the Vespa is just coming 
back into vogue). Years of pleasure at 80 mpg using two-stroke gas/oil. 
Could click some 50 mph if not going up an incline and 60 mph downhill, 
but the noise suggested the bloody thing was coming apart under your 
feet. Road it until '67 when it 'died'. I think I got 30 or 40K miles 
out of it. A gent from the AA (Automobile Association) arrives, dressed 
like a chauffeur from an Agatha Christie 20's period piece; peaked cap, 
brown uniform with breeches and glistening brown boots. Informs me 
solemnly, "The Big End's gone". Didn't know it had any sort of end - is 
that like Big Endian and Small Endian ?

About 18 months later got into four wheels.
> 

> 
>>Jerome G could have asked his brother Art to come up with different 
…[12 more quoted lines elided]…
> Enjoyed the lyrics!  A few points ...

Enjoyed the lyrics but didn't recognise the song. Come on Chuck, has to 
be your era when you were young and romantic :-

"99 Miles from L.A"

The tape copyright says 1975.

I thought it was Simon and Garfunkel. Not so; separate tape for Art 
Garfunkel where he sings on his own. I thought is was "21 miles from LA" 
so had a job finding it by googling. Did a google on Jerome, which led 
to Art and find that Nancy Sinatra also sang it amongst others. Same 
tape has Art giving a lovely rendition of Al Jolson's "I only have eyes 
for you". (On the S. & G tape there's one "7 o'Clock News - Silent 
Night" - sad period news items from the era accompanied by Silent Night).

> 
>>The windshield is covered with rain, I'm cryin'.
…[10 more quoted lines elided]…
> myself singing that one, in the rain, on several occasions!   Man, oh, man!

Yes Mr. Tap Dancing - Gene Kelly, (much better than Fred Astaire). 
They've just repeated a TV ad for GE, a baby elephant using all four 
feet in a jungle setting, copying the Master's footwork to "Singin' in 
the Rain" :-). Wont mean much in N. America but a pair of very beloved 
comedians in England, Morecombe and Wise used to do Christmas Specials. 
Copying the 'Singin in the Rain' movie set they did an hilarious comedy 
spoof.

Get impression, and from what you have written previously that you like 
what I would call the 'heavy, sombre' classics. Somebody going out of 
town offered me tickets for a concert evening - a real pain in the butt 
- mournful music from Mahler. Fortunately the 'Germanic' evening 
finished with Beethoven's Fifth.

My taste is more catholic, lighter hummable classics, Elgar, Debussy, 
Tchaikovsky, Katchachurian, Copeland, Gershwin, Rodgers and 
Hart/Hammerstein, through pops to the Chairman of Board, Deano and 
Sammy. Yes I like looking at Jay Lo, Beyonce and Brittney etc., but 
there's not one single song of theirs I remember. I really draw the line 
at the sun-tanned gentleman wearing drop-down clothes and orthopedic 
caps on their heads backwards, constantly pointing at the camera - I 
look, and before I switch I have a dire need to throw a grenade at the 
screen !

> 
>>(** Have you got [a windshield] on your bike ? )

Why I asked was because a windshield was a real necessity with Vespas or 
Lambrettas. Unlike you bikers us folks were dressed like normal people - 
so you could get pretty wet even in a heavy drizzle. (Of course the 
original lyrics about a windshield relate to driving a car).
> 
> 
>>Pressing my foot on the gas, I'm flyin'.

Again refers to pressing the gas pedal in a car. Same with scooters - we 
throttled from the handlebars like you bikers. Only pedal was the 
brakes, as I recall - could be wrong.


Jimmy
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 17)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-03T05:54:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149339258.504380.274350@c74g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<GW4gg.223560$P01.73255@pd7tw3no>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no>`

```

James J. Gavan wrote:
> Having read you, Howard and Alistair comin' a cropper on those beasts -
> I knew I was right to avoid them !

<snip>

> Real progression - a moped - a bike with an engine in the back wheel -
> Wowee ! Perhaps 20 mph.

<snip>

> 58/59' bought a spanking new Lambretta.

<snip>

> out of it. A gent from the AA (Automobile Association) arrives, dressed
> like a chauffeur from an Agatha Christie 20's period piece; peaked cap,
> brown uniform with breeches and glistening brown boots. Informs me
> solemnly, "The Big End's gone". Didn't know it had any sort of end - is
> that like Big Endian and Small Endian ?

Yep, it has both a big end and a little end. Which one goes doesn't
matter: it stops and then it's an expensive mechanic job to repair it.

>
> About 18 months later got into four wheels.

Ah, there's the problem. You never were a biker, just a mod. With
biking, once you've done it, it is in the blood for life.

> >
> >>The windshield is covered with rain, I'm cryin'.

<snip>

>
> Yes Mr. Tap Dancing - Gene Kelly, (much better than Fred Astaire).
…[5 more quoted lines elided]…
> spoof.

Once seen, never forgotten.

>
> Get impression, and from what you have written previously that you like
> what I would call the 'heavy, sombre' classics. Somebody going out of
> town offered me tickets for a concert evening - a real pain in the butt
> - mournful music from Mahler.

You've probably listened to the wrong Mahler. For a real tedious
evening you should listen to the full Ring Cycle (Wagner, one good tune
and that is it).

> Fortunately the 'Germanic' evening
> finished with Beethoven's Fifth.
…[4 more quoted lines elided]…
> Sammy.

Try Philip Glass and Steve Reich (minimalist composers?).

> >
> >>(** Have you got [a windshield] on your bike ? )
…[4 more quoted lines elided]…
> original lyrics about a windshield relate to driving a car).

Even leathers and waterproofs leak   |--(

> >
> >
…[4 more quoted lines elided]…
> brakes,

Don't use it, except in real emergencies or when going around bends.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 18)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-03T20:04:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tXlgg.230786$7a.163671@pd7tw1no>`
- **In-Reply-To:** `<1149339258.504380.274350@c74g2000cwc.googlegroups.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com>`

```
Alistair wrote:
> James J. Gavan wrote:
> 

>>Get impression, and from what you have written previously that you like
>>what I would call the 'heavy, sombre' classics. Somebody going out of
…[7 more quoted lines elided]…
> 
I absolutely LOVE Puccini's Madam Butterfly. Some boring bits but for 
the most part also contains some very beautiful melodies. So one night 
I'm watching PBS where they did three one-acts by Puccini. What an 
absolute bore - there was only one decent melody in the three acts. 
Don't know it's name in Italian, but in English comes across as "Oh my 
beloved Father.....".
> 
>>Fortunately the 'Germanic' evening
…[8 more quoted lines elided]…
> Try Philip Glass and Steve Reich (minimalist composers?).


I think the name Philip Glass rings a remote bell. Time Magazine grabs 
TV for hour long stretches offering a set of say 10 DVDs plus a bonus of 
two freebies for around #140 for the twelve. I'm often so tempted.
Their selections, say "Romantics of the 70's", "Hits of the 50's, 60's 
70's", "Soul Music", etc. Naturally they provide video shots of 
performers singing in their early years. The number of tunes I enjoy 
from back then but had no idea of the names of the artists singing them,

Example - while back, Howard mentioned "Mr. Bo Jangles". Immediately I 
recall Sammy Davis Junior's dance routine. But Howard mentioned another 
singer, doing the same song but with a very catchy banjo background. Of 
course we all recognize groups like Abba or the Mommas and Papas - but 
many others we just remember the melodies AND THE WORDS and have no clue 
as to the original singer's identity. I suppose you would have 
remembered back then if you were a record collector - for me, it was 
what I heard from BBC Light Programme.

Talk about boring - did you ever attempt to listen to classics on BBC 3 
? Like listening to a musical version of the Home Service 'Brains Trust'.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 19)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-06-03T21:09:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Umgg.90817$H71.56671@newssvr13.news.prodigy.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:tXlgg.230786$7a.163671@pd7tw1no...
> I absolutely LOVE Puccini's Madam Butterfly. Some boring bits but for
> the most part also contains some very beautiful melodies.

Eat your heart out.

I'm attending a performance of  Verdi's Aida tonight at the Milwaukee
Florentine Opera.

(The Florentine did a really nice 'Butterfly'  two, no, it was  three
seasons ago now).

MCM
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 20)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T08:11:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61hif$1l4c$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <5Umgg.90817$H71.56671@newssvr13.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:5Umgg.90817$H71.56671@newssvr13.news.prodigy.com...
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
> news:tXlgg.230786$7a.163671@pd7tw1no...
…[11 more quoted lines elided]…
> MCM

Don't care much for Aida.  In fact, don't care much for Verdi, with the 
possible exception of Tosca.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 21)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-06-05T15:58:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZwYgg.111221$dW3.29008@newssvr21.news.prodigy.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <5Umgg.90817$H71.56671@newssvr13.news.prodigy.com> <e61hif$1l4c$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:e61hif$1l4c$1@si05.rsvl.unisys.com...
> "Michael Mattias" <michael.mattias@gte.net> wrote in message
> news:5Umgg.90817$H71.56671@newssvr13.news.prodigy.com...
…[11 more quoted lines elided]…
> possible exception of Tosca.

The Florentine's Aida was magnificent. Angela Brown in the title role was
"OK" , but both Jessie Raven as Princess Amneris and Renzo Zulian as Radames
were simply outstanding.

I've been a season ticket holder since 1999, and this was by far the
grandest production. The  cast, orchestra and production people got (or
rather, earned) an ovation just for Act II. I'd go again in a New York
minute.

And Guiseppe Verdi (to whom I often refer using his Americanized name "Joey
Green")?  My my favorite opera composer  bar none. (I really like all the
'chorus' parts where there are many many voices singing).


MCM
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 22)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T09:34:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61mdp$1o7v$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <5Umgg.90817$H71.56671@newssvr13.news.prodigy.com> <e61hif$1l4c$1@si05.rsvl.unisys.com> <ZwYgg.111221$dW3.29008@newssvr21.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:ZwYgg.111221$dW3.29008@newssvr21.news.prodigy.com...

> The Florentine's Aida was magnificent. Angela Brown in the title role was
> "OK" , but both Jessie Raven as Princess Amneris and Renzo Zulian as 
> Radames
> were simply outstanding.

...

> I've been a season ticket holder since 1999, and this was by far the
> grandest production. The  cast, orchestra and production people got (or
…[6 more quoted lines elided]…
> 'chorus' parts where there are many many voices singing).

If you like operatic-polychoral effects with a *very* Italian flavor, and 
you ever get the chance, check out the Prologue to the opera "Mefistofele" 
by Arrigo Boito.  Boito was Verdi's librettist for Poncielli's "La Gioconda" 
and Verdi's "Falstaff" and "Otello".   The opera itself is occasionally 
done, but by the time you're done with the prologue, I think you've heard 
all the good stuff.  One reviewer commented "Arrigo Boito's 'Mefistofele' is 
one of the better bad operas ... ", and I have to admit there are 
compositional details that are just way too precious.   The Prologue's a 
real kick.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-06-07T01:23:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4eldugF1f1trfU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <5Umgg.90817$H71.56671@newssvr13.news.prodigy.com> <e61hif$1l4c$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e61hif$1l4c$1@si05.rsvl.unisys.com...
> "Michael Mattias" <michael.mattias@gte.net> wrote in message 
> news:5Umgg.90817$H71.56671@newssvr13.news.prodigy.com...
…[17 more quoted lines elided]…
>
Nabucco ...specifically "Va pensiero sul alli dorate" (Fly my thoughts on 
wings of gold) does it for me. I heard the most amazing version of this done 
in modern style with electric guitars the other day. It choked me up. The 
artist was an Italian popsinger named Zucchero, singing it in English (which 
I had never heard before). Truly outstanding.

I envy you Aida, Michael.  The last time I saw it was in London and it was 
superb.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 22)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-06T09:13:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149610404.277941.194080@h76g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4eldugF1f1trfU1@individual.net>`
- **References:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <5Umgg.90817$H71.56671@newssvr13.news.prodigy.com> <e61hif$1l4c$1@si05.rsvl.unisys.com> <4eldugF1f1trfU1@individual.net>`

```

Pete Dashwood wrote:
> Nabucco ...specifically "Va pensiero sul alli dorate" (Fly my thoughts on
> wings of gold) does it for me. I heard the most amazing version of this done
…[7 more quoted lines elided]…
> Pete.

I'll be looking for that one on the net soon (Zucchero). I can
certainly recommend (definitely off-off-topic) "Coin operated boy" by
the Dresden Dolls (punk cabaret).
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 19)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-04T09:43:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149439425.344823.96300@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<tXlgg.230786$7a.163671@pd7tw1no>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no>`

```

James J. Gavan wrote:
> Alistair wrote:
> > James J. Gavan wrote:
…[5 more quoted lines elided]…
> beloved Father.....".

>From the opera Gianni Schicci by Puccini. Based upon a 13th century
Florentine.

> I think the name Philip Glass rings a remote bell.

Glass wrote the music to Koyaanisqatsi. Don't know about the film but
the music is very uplifting.

>
> Talk about boring - did you ever attempt to listen to classics on BBC 3
> ? Like listening to a musical version of the Home Service 'Brains Trust'.


The Beeb did a series of live radio and tele broadcasts once. I don't
think I've ever been able to sit through a complete bradcast but I am
an avid viewer of opera (BTW, try to avoid Bluebeard's Castle by
Bartok).
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 20)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T08:21:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61i5q$1lf9$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1149439425.344823.96300@i39g2000cwa.googlegroups.com...

> Glass wrote the music to Koyaanisqatsi. Don't know about the film but
> the music is very uplifting.

How can music be uplifting if it doesn't *do* anything?    ;-)

> (BTW, try to avoid Bluebeard's Castle by
> Bartok).

Well, if you know going in that there are basically only two singers in it, 
and that it's intended for minimalist staging, it's a pretty neat piece.  I 
do agree it'd be pretty deadly on TV, but I think it's got something to 
offer seen live.  Here's a case, too, where hearing it in the original 
language is an important part of the experience, as is the spoken prologue 
(rarely done any more).    More listenable than most Alban Berg, anyway.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 21)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-06T04:56:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149594969.480314.324680@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<e61i5q$1lf9$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com>`

```

Chuck Stevens wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1149439425.344823.96300@i39g2000cwa.googlegroups.com...
…[14 more quoted lines elided]…
> (rarely done any more).    More listenable than most Alban Berg, anyway.

What spoken prologue? All I can recall is a lot of bits that should
have been spoken but were sung. I hate speech that is sung; much better
to have a rousing belter of a song with vocab spoken as links. It was
on tv and it was sh*te.

> 
>     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 22)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-06T07:48:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e644jh$5tu$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <1149594969.480314.324680@y43g2000cwc.googlegroups.com>`

```
"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1149594969.480314.324680@y43g2000cwc.googlegroups.com...

> What spoken prologue? All I can recall is a lot of bits that should
> have been spoken but were sung. I hate speech that is sung; much better
> to have a rousing belter of a song with vocab spoken as links. It was
> on tv and it was sh*te.

There's an introductory prologue -- maybe about as long as the Gettysburg 
address -- delivered (preferably in Hungarian) by an old man (I don't 
remember if it's onstage or off), before the music starts.  Sets the mood 
even better than the music.  Many recordings and performances omit it, to 
the opera's detriment in my opinion.  The vinyl recording I have, from the 
early 1950's, includes it.

Given that the set throughout the work is supposed to be a big hall with 
seven doors, and all of the "effects" are supposed to be done with different 
colored lights from behind the doors as they open (and two people walking 
around and opening doors and singing for an hour is pretty much all there is 
to the action!), it's a tough piece to stage and keep interesting, I'd say. 
Familiarity with the plot helps; I couldn't disagree with the argument e 
that it works best as an audio-only experience, letting your imagination 
provide the scenery.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 23)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-06T09:10:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149610200.159000.245320@j55g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e644jh$5tu$1@si05.rsvl.unisys.com>`
- **References:** `<4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <1149594969.480314.324680@y43g2000cwc.googlegroups.com> <e644jh$5tu$1@si05.rsvl.unisys.com>`

```

Chuck Stevens wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1149594969.480314.324680@y43g2000cwc.googlegroups.com...
…[11 more quoted lines elided]…
> early 1950's, includes it.

Thanks, but I have been put off of Bartok's opera (still like his piano
concertos) and won't be revisiting it.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 23)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-06T18:04:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Osjhg.247218$7a.103633@pd7tw1no>`
- **In-Reply-To:** `<e644jh$5tu$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <1149594969.480314.324680@y43g2000cwc.googlegroups.com> <e644jh$5tu$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
> news:1149594969.480314.324680@y43g2000cwc.googlegroups.com...
…[14 more quoted lines elided]…
> 

Given in Hungarian ? I'm not bloody surprised they bypass it. Dammit I 
have difficulty remembering my daughter's new Hungarian surname, and the 
husband is of Polish descent but born in Hungary !

Jimmy

> Given that the set throughout the work is supposed to be a big hall with 
> seven doors, and all of the "effects" are supposed to be done with different 
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 24)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-06T11:38:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64i3k$eac$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <1149594969.480314.324680@y43g2000cwc.googlegroups.com> <e644jh$5tu$1@si05.rsvl.unisys.com> <Osjhg.247218$7a.103633@pd7tw1no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:Osjhg.247218$7a.103633@pd7tw1no...
> Chuck Stevens wrote:
>> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
…[19 more quoted lines elided]…
> husband is of Polish descent but born in Hungary !

Well, in this instance the whole bloody opera's written in Hungarian ... 
It's only to make it more accessible that they translated it to German (and 
almost always dropped the prologue in any language in that version).

As to Polish, my high school chemistry teacher used to comment that his name 
was pronounced exactly as it was spelled -- Wojczynski -- and my later 
linguistic studies proved him right ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-06-07T01:53:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4elfniF1f3l2gU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e61i5q$1lf9$1@si05.rsvl.unisys.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
…[5 more quoted lines elided]…
> How can music be uplifting if it doesn't *do* anything?    ;-)

C'mon Alistair... if it's written by GLASS it HAS to be UPLIFTING... (hic) 
:-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 22)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-06T08:57:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149609428.588835.131420@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4elfniF1f3l2gU1@individual.net>`
- **References:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <4elfniF1f3l2gU1@individual.net>`

```

Pete Dashwood wrote:
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
> news:e61i5q$1lf9$1@si05.rsvl.unisys.com...
…[12 more quoted lines elided]…
> Pete.

Hoi! I was the one who liked Glass (half-full or half-empty). Chuck
criticised my choice.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 23)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-06T09:00:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e648rd$8i5$1@si05.rsvl.unisys.com>`
- **References:** `<e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <1149439425.344823.96300@i39g2000cwa.googlegroups.com> <e61i5q$1lf9$1@si05.rsvl.unisys.com> <4elfniF1f3l2gU1@individual.net> <1149609428.588835.131420@i39g2000cwa.googlegroups.com>`

```
A fine distinction, perhaps ... but I don't criticize your choice, I just 
don't agree with it!

    -Chuck Stevens

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1149609428.588835.131420@i39g2000cwa.googlegroups.com...
>
> Pete Dashwood wrote:
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 19)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T08:10:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61hgd$1l2i$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:tXlgg.230786$7a.163671@pd7tw1no...

> I absolutely LOVE Puccini's Madam Butterfly. Some boring bits but for the 
> most part also contains some very beautiful melodies. So one night I'm 
…[3 more quoted lines elided]…
> Father.....".

Most of Puccini's pretty nice stuff.  The one-acts you mention may have been 
intended to be treated as a unit (-- "Il Trittico", consisting of "Il 
Tabarro", "Suor Angelica", and "Gianni Schicchi").  Often one or more of 
them will pair with one or the other of "Cav and Pag" (Mascagni's 
"Cavalerria Rusticana" and Leoncavallo's "I Pagliacci").  A lot of his plots 
are a little implausible (Butterfly's one), but the music is gorgeous, I 
think.  My personal favorite is Turandot; it's a pity he never finished it.


> I think the name Philip Glass rings a remote bell. Time Magazine grabs TV 
> for hour long stretches offering a set of say 10 DVDs plus a bonus of two 
> freebies for around #140 for the twelve. I'm often so tempted.

I am not a fan of Philip Glass' works.  He seems to be devoted to repeating 
the same thing over and over and over and over and over again with only the 
minutest variations, and the game seems to be to figure out what changed 
between the fourth time you heard the tume and the fifty-seventh.  If you've 
ever sat through Bach's "St. Matthew Passion" with its several variations on 
"O sacred head surrounded", take out everything but those chorales and throw 
it away, and multiply it by about fifty, you've got the essence of Philip 
Glass.  When I hear Philip Glass -- and for that matter when I hear the 
Matthew -- all I can think of is "Alright, already.  We got your point.  May 
we please move on?"  Alas, ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 20)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-06-06T04:51:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149594711.891380.98620@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e61hgd$1l2i$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <tXlgg.230786$7a.163671@pd7tw1no> <e61hgd$1l2i$1@si05.rsvl.unisys.com>`

```

Chuck Stevens wrote:

> I am not a fan of Philip Glass' works.  He seems to be devoted to repeating
> the same thing over and over and over and over and over again with only the
…[9 more quoted lines elided]…
>     -Chuck Stevens

I am a fan of PG. But for a truly repetitive experience try Drumming by
Steve Reich. (Which I like BTW).
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 18)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T07:56:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61gm8$1klg$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com>`

```
"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1149339258.504380.274350@c74g2000cwc.googlegroups.com...

> You've probably listened to the wrong Mahler. For a real tedious
> evening you should listen to the full Ring Cycle (Wagner, one good tune
> and that is it).

Naah.  Only opera I've ever walked out of was Il Trovatore; stuck around for 
the Anvil Chorus and packed it in.

Now, if you want tedious Wagner ... try Rienzi.  The San Antonio Symphony 
did the *first* fully-staged production of Rienzi in English in the United 
States a few decades ago (I sang in the chorus), cut it to ribbons (a 
virtually impossible task), and it was *still* interminable.   I think we 
reduced it from six-plus hours to something under five.  As written, 
*during* the big festival celebrating Rienzi's return to Rome there's 
something like a *forty-minute* pantomine for his entertainment, with no 
lyrics *at all*.   I think it's generally regarded as Wagner's worst work.

Our English translation of the lyrics was pretty laughable, too ... A couple 
of gems from the chorus parts: "Burn down the capitol at once!  Burn it 
down!" and if I recall correctly, in response, "Make way, you fools, or feel 
our swords!".  Worst chorus lyrics I've seen with the possible exception of 
those in the original French for Bizet's Carmen (also embarrassingly bad).

Rienzi's got a few nice tunes, but man, oh man, oh MAN, oh man-oh-man, is it 
a long, long, LONG song.  Even with the elephants and camels onstage in the 
triumphal scene it's laughably tedious.  Some wag once said it was the best 
opera Meyerbeer ever wrote.  It almost looks *purposefully* bad -- the 
stereotype of the overblown, bad "numbers" opera (as in act/scene numbers, 
in this case five acts of five, three, three, two and four scenes 
respectively.  Act II scene 2 is the big elephants-and-camels procession; 
the final scene has Rienzi and Irene perishing in each others' arms as the 
Roman Capitol burns.  It is rumored that Wagner forbade in perpetuity the 
production of Rienzi at Bayreuth.

Ring cycle?  Like it or not, a masterpiece of drama and craftsmanship 
compared to Rienzi.  It's bad.  It's really, really, REALLY bad.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-06-05T09:02:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mnh882dhq86ugauqguqki61h6rmte1d11h@4ax.com>`
- **References:** `<e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no> <1149339258.504380.274350@c74g2000cwc.googlegroups.com> <e61gm8$1klg$1@si05.rsvl.unisys.com>`

```
The trouble with Opera is that even when it's sung in English, I can't
understand half the lyrics.  (That's the trouble with songs in
general, but usually they aren't the plot).   Nowadays subtitle boxes
help.  (I haven't seen an English Language opera since they started
adding these - I hope they have subtitles as well).

On the other hand Opera is the fastest Browser on Windows.
```

###### ↳ ↳ ↳ Re: OT: Ridin' tall on the Santiago Canyon Road (was Re: What could J4 (or WG4) do)

_(reply depth: 17)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-06-05T07:36:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e61fi1$1juu$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no> <e523kd$15fl$1@si05.rsvl.unisys.com> <GW4gg.223560$P01.73255@pd7tw3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:GW4gg.223560$P01.73255@pd7tw3no...

> Having read you, Howard and Alistair comin' a cropper on those beasts - I 
> knew I was right to avoid them ! A much more modest progression - a 
…[6 more quoted lines elided]…
> drop-downs.

Yeah, I had a three-speed Hercules with caliper brakes back when machines of 
this type were called "English racing bikes" and most people rode Schwinns 
with a single speed and coaster brakes ... that would have been, oh, about 
1955 or 1956 ...

> Real progression - a moped - a bike with an engine in the back wheel - 
> Wowee ! Perhaps 20 mph.

Had a Garelli moped in the early 1980's, and often commuted to work on it. 
It was not one of the folding ones, though.  Had what was euphemistically 
called an "automatic transmission", when in reality what it had was a big 
synthetic-rubber doughnut that acted as a centrifugal clutch.  I think there 
was a total of something like seven moving parts in the entire drivetrain, 
if you counted the chain as a single part ...

There were some pretty sophisticated, and well-built, mopeds back then -- I 
remember Kreidler being regarded as the Ne Plus Ultra of mopeds at the time 
...

> ... As somebody in the Sergeants' Mess unkindly put in once, "I looked 
> like and elephant sat on a pea :-) ).

I remember a guy some 6'5" riding on a Honda Rebel, which is something like 
a half-size Harley Dyna, looking a little silly ... Then there's the whole 
modern "pit bike" phenomenon ...

> but the noise suggested the bloody thing was coming apart under your feet. 
> ... A gent from the AA (Automobile Association) arrives ...  Informs me 
> solemnly, "The Big End's gone".

Which is probably what it was trying to tell you with all that clattering 
and banging before it quit ... 2-strokes are really sensitive about 
lubrication, better too much (and have to scrub off the spark plugs 
occasionally and risk the ire of the gendarmerie from the clouds of blue 
smoke) than too little ...

> Come on Chuck, has to be your era when you were young and romantic :-

Sorry, not my style. I discovered the joys of Telemann in Junior High.  And 
that's way, way before the Baroque got popular.
>
> "99 Miles from L.A"
>
> The tape copyright says 1975.

Thanks, I'll hunt it up.

> Get impression, and from what you have written previously that you like 
> what I would call the 'heavy, sombre' classics.

Well, hard to say.  I'm particularly fond of Bach, but I don't find him 
particularly somber (in fact, I'd say parts of the Tocatta, Adagio and Fugue 
in C Major are downright riotous).

> Somebody going out of town offered me tickets for a concert evening - a 
> real pain in the butt - mournful music from Mahler.

Generally I find Mahler way more trouble than it's worth.  But I have 
performed in the chorus in the 2nd Symphony (Resurrection) and have to admit 
Mahler's attempt to outdo the ending of the Beethoven Ninth succeeds, if you 
can last through what it takes to get there ...

> Fortunately the 'Germanic' evening finished with Beethoven's Fifth.

All nine of the Beethoven symphonies have something to offer.

> I really draw the line at the sun-tanned gentleman wearing drop-down 
> clothes and orthopedic caps on their heads backwards, constantly pointing 
> at the camera - I look, and before I switch I have a dire need to throw a 
> grenade at the screen !

I have a great deal of difficulty associating their antics with "music".

> Why I asked was because a windshield was a real necessity with Vespas or 
> Lambrettas. Unlike you bikers us folks were dressed like normal people - 
> so you could get pretty wet even in a heavy drizzle.

I've been told that a windscreen is a real necessity on any cross-country 
trip by some serious bikers.  I've pretty much decided I don't agree, bugs 
or no bugs, rain or no rain, and if I get into a hailstorm the windscreen 
ain't gonna do a heck of a lot of good anyway!

The way I figure it, I'll give the idea of riding in the rain a second 
thought if I'm *leaving* home, because if I get wet I'll have to stay wet 
the whole time I'm out, but if I'm *coming* home I don't even think about 
it; if I get wet, no harm done.


>>>Pressing my foot on the gas, I'm flyin'.
>
> Again refers to pressing the gas pedal in a car. Same with scooters - we 
> throttled from the handlebars like you bikers. Only pedal was the brakes, 
> as I recall - could be wrong.

Probably so on the automatic-transmission scooters.  Motorcycle controls 
these days have standardized to left foot pedal = gearshift lever, right 
foot pedal = rear brake, left hand lever = clutch, right hand lever = front 
brake, and right handgrip = throttle.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T10:03:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e523lk$15fm$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <bQPcg.184184$P01.162682@pd7tw3no>`

```
Part 2 of my response:

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:bQPcg.184184$P01.162682@pd7tw3no...

> 2. What follows from #1 above - more or less your COBOL test suite BECAUSE 
> "somebody" having taken the first shot, (a developer at IBM, Unisys, 
…[3 more quoted lines elided]…
> accept/reject and if OK are further added to the list of examples.

There was some serious discussion of this a while back.  I may have the 
details wrong, but as I remember it the EDS rep on J4 was in the process of 
setting up just such a mechanism when his company decided to withdraw 
support from the entire COBOL standardization process.

> This example thing is not a new one; I believe it was a topic at J4 about 
> five years back. Trouble is you work for people who pay you but you want 
> US (Certainly most PC-users, the people that have to pay ourselves), to 
> initiate this idea.

My personal opinion is that the more examples the better -- but that they 
should be in a separate volume, precisely so as to reduce the size of the 
*reference* manual.  Examples by their very nature are "informative" rather 
than "normative".

I work for people who pay me to do stuff, and a *small* part of that stuff 
is COBOL standardization (a MUCH LARGER part is supporting COBOL, RPG, 
ALGOL, WorkFlow and SORT compilers among other products) and managing the 
processes by which they are supported.   If Unisys were willing to pay me 
full time to do nothing but work on COBOL standardization, that'd be great. 
But they're not, so there's not a whole lot *I personally* can do to make 
sure the gruntwork gets done.   I also don't have a whole lot of personal 
investment in *whether* it gets done, which is why I encourage those who 
think it is MANDATORY that it be done, and SOON, to get crackin' if its that 
important!   I have no reason to believe that what *you* think *Unisys* 
should be paying me to do is as important to Unisys as what *Unisys* thinks 
they should be paying me to do!

> Just those two points alone show how radically different our thoughts are.

I do what I can.  I won't accept responsibility for more than  that.

    -Chuck ("ridin' tall on the canyon road") Stevens    8-)
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-24T02:52:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LTPcg.19387$aA3.2378@fe06.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e504kq$31bq$1@si05.rsvl.unisys.com...
>
<much snippage>
> Again, I've said repeatedly I think there is value in a standard even if it is 
> simply to provide guidelines for implementors as to how a consortium of 
> interested parties think a given feature should be handled.
>

Chuck,
   If my memory serves me correctly, you became invovled with J4 (or X3J4) 
*after* the merger with CCC (CODASYL COBOL Committee).  If so, then this may be 
an unfair question.

It seems to me that (as I see the current situation - and your comment above), 
that you see the "value" in the Standard ('02 or later) being that of what the 
JOD (Journal of Development) *used* to be. In fact, some features WERE 
implemented by vendors based on the JOD - and some got "changed" by the time 
they got into the '85 ANSI or '02 ISO Standard.  On the other hand, some 
features, did become "medium common" extensions (never in the Standard) based on 
JOD inclussion.

Do you see the PRIMARY role of the current Standard and development of the next 
Standard as such - or if not, how do you distinguish their roles?
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-24T07:02:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e51p1h$v7c$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <q1ccg.172325$pd5.79049@fe03.news.easynews.com> <gFIcg.184820$WI1.7656@pd7tw2no> <e504kq$31bq$1@si05.rsvl.unisys.com> <LTPcg.19387$aA3.2378@fe06.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:LTPcg.19387$aA3.2378@fe06.news.easynews.com...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
> news:e504kq$31bq$1@si05.rsvl.unisys.com...
…[10 more quoted lines elided]…
> may be an unfair question.

Whether the question is fair or not, my first direct involvement with J4 was 
at Meeting #228 in December 2000 at Carmel, CA.

> It seems to me that (as I see the current situation - and your comment 
> above), that you see the "value" in the Standard ('02 or later) being that 
…[4 more quoted lines elided]…
> (never in the Standard) based on JOD inclussion.

Though our linguistic training is in different language families, it appears 
necessary to remind you that I chose my words carefully, and presuming you 
chose your words equally carefully, I think you've misquoted (or 
mis-paraphrased) me.

There is a sketch in "Beyond the Fringe" that applies here.  It's a 
hypothetical exchange between an unnamed member of the cast and Bertrand 
Russell (I forget the title of the sketch).   Here's a paraphrase from 
memory:

    (UMC):  "Are there any apples in that basket?"
    (BR):  "No", replied Mr. Russell.
    (UMC): "Are there some apples in that basket?"
    (BR):  "No", replied Mr. Russell, who smiled seraphically (as was his 
wont).
    (UMC):  That left me in a logical cleft stick from which there was but 
one escape:
            "Are there apples in that basket?"
    (BR):  "YES!" replied Mr. Russell, and from that day forward we were the 
very best of friends.

I stated that I see value in the standard, and in the process of its 
development, as a guide to implementor design and development.   That is a 
far cry from stating, or intending to state, that I see 'the "value" ' being 
in that arena.  If you're going to argue, or ask for my explanations as to 
what I meant by what I actually stated, it is generally considered Bad Form 
to request my elaboration of an argument I did not make!

> Do you see the PRIMARY role of the current Standard and development of the 
> next Standard as such - or if not, how do you distinguish their roles?

Nor did I say "primary".   The roleS that the standard and the draft will, 
or might, play in the lives of developers and implementors is out of my 
control.   As it stands right now, whether anyone *ever* comes up with an 
implementation conforming absolutely in every respect to either one, I think 
the standard has value as a guide, as an ideal, as a goal.  Whether anyone 
attains that goal is not relevant to that point.

At this point, if somebody provides a fully-conforming implementation of 
2002 standard COBOL, or of the 2008 draft once it's complete, I think it 
would be of benefit to COBOL at large, and I think that would be a separate 
issue from the value of the standard itself.  I think the value of the 
standard would be *enhanced* if an implementor provided a conforming 
implementation -- but then I think the value of the standard is *enhanced* 
every time somebody decides, for example, to implement the time/date 
intrinsic functions from the draft , or free-form reference format or the 
exception-handling routines from the 2002 standard, as extensions to their 
existing offerings.  And I think the standard has value as a simple 
guideline along the lines of "IF you are going to do something like <x>, 
here's a recommended way of doing it, because if you do it this way, others 
are likely to follow".

I think the standard and the process both have value in all of these areas, 
taken individually and in combination, and am not inclined to dismiss any of 
them or assign each area a ranking.  Value is sufficient unto itself, in my 
view.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-21T23:06:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148278017.411623.114890@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<1148230032.339594.178420@i39g2000cwa.googlegroups.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com>`

```
> Jeanette Nutsford from New Zealand

Many years^H^H^H^H decades ago when I worked at ICL in Auckland, Ken
Nutsford and Jeanette (?) both worked there and were maried for months
before they told anyone. I wonder if that is the same one.

That strikes me as such an old-fashioned idea now - getting married to
buy a house and live together.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-23T01:27:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ddshmF1a1akkU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1148278017.411623.114890@u72g2000cwu.googlegroups.com...
>> Jeanette Nutsford from New Zealand
>
> Many years^H^H^H^H decades ago when I worked at ICL in Auckland, Ken
> Nutsford and Jeanette (?) both worked there and were maried for months
> before they told anyone. I wonder if that is the same one.

Without wishing to embarrass either of them, I can confirm they were indeed 
the couple you describe :-)
>
> That strikes me as such an old-fashioned idea now - getting married to
> buy a house and live together.
>
As opposed to remaining a transient vagrant and fathering children all 
around the world? :-)

Pete.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 13)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-22T11:48:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148323690.886180.184210@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<4ddshmF1a1akkU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com> <4ddshmF1a1akkU1@individual.net>`

```
> As opposed to remaining a transient vagrant and fathering children all
> around the world? :-)

Well I might have, but my wife wouln't let me.

It seems to me that most, or at least many, these days buy a house and
live together and eventually get married.  I did.  My children did.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-05-23T19:16:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wcJcg.184852$WI1.75829@pd7tw2no>`
- **In-Reply-To:** `<4ddshmF1a1akkU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com> <4ddshmF1a1akkU1@individual.net>`

```
Pete Dashwood wrote:
> "Richard" <riplin@Azonic.co.nz> wrote in message 
> news:1148278017.411623.114890@u72g2000cwu.googlegroups.com...
…[18 more quoted lines elided]…
> Pete.

Just an update for you Kiwis. Don't where I picked up on it but came 
across a message about Jeanette. Back at Newbury in 2000 she and hubby 
stood in for Bob Karlin on J4, and at time Jeanette was very much 
involved with the HP Users' Group as chairwoman. She has recently quit - 
and nobody has shown interest in taking over the job.

Jimmy
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-23T12:37:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4voa7$2q66$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com> <4ddshmF1a1akkU1@individual.net> <wcJcg.184852$WI1.75829@pd7tw2no>`

```
Jeanette was both a New Zealand delegate and a UK delegate to WG4 Meeting 
#24 in Las Vegas in June 2003 (Ken was a NZ delegate), but I'm pretty sure 
they haven't been at a WG4 meeting since then.

As to her involvement with the HP user's group (and Bob Karlin was also 
heavily involved with the HP user community), I seem to recall from 
discussions around then that general interest in that group bore some 
correlation to HP's level of support for the HP3000 architecture at the 
time, which architecture formed much of the impetus for the group's very 
existence.    I may be mistaken, though.

Jeanette's been the alternate representative to J4 for Karlins' Korner for 
some time, so her standing in for Bob at the J4 meeting in Newbury (before 
my time) and presumably being a New Zealand and probably also a UK delegate 
at the WG4 meeting that was held there isn't surprising.

    -Chuck Stevens

<top post, no more below>

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:wcJcg.184852$WI1.75829@pd7tw2no...
> Pete Dashwood wrote:
>> "Richard" <riplin@Azonic.co.nz> wrote in message 
…[27 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-22T07:39:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mnf372p51n5eil06s3dctkecl04d8f1qkd@4ax.com>`
- **References:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com>`

```
On 21 May 2006 23:06:57 -0700, "Richard" <riplin@Azonic.co.nz> wrote:

>That strikes me as such an old-fashioned idea now - getting married to
>buy a house and live together.

Those are two different things.   I know people who have lived
together and then married to facilitate buying a house.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-22T12:56:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4t50m$18ja$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com>`

```
Almost certainly the same couple.

    -Chuck Stevens

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1148278017.411623.114890@u72g2000cwu.googlegroups.com...
>> Jeanette Nutsford from New Zealand
>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 13)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-22T13:15:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148328916.633998.76900@j73g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e4t50m$18ja$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com> <e4t50m$18ja$1@si05.rsvl.unisys.com>`

```
> Almost certainly the same couple.

IIRC Ken left ICL to become the Auckland sales manager for Unisys.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-23T20:19:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dfusvF19dqq7U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <1148278017.411623.114890@u72g2000cwu.googlegroups.com> <e4t50m$18ja$1@si05.rsvl.unisys.com> <1148328916.633998.76900@j73g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1148328916.633998.76900@j73g2000cwa.googlegroups.com...
>> Almost certainly the same couple.
>
> IIRC Ken left ICL to become the Auckland sales manager for Unisys.
>
ROFL! I didn't know that... small world...

Pete.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-23T01:24:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ddscqF19qngrU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com>`

```
Thanks for that clarification,Robert.

Ken and Jean Knutsford were proponents of COBOL back in the late 60s in 
Auckland and I remember them well.

I had a phone conversation with Jean regarding the standards in the U.K. 
some years ago and I know she has been involved.

I'm not sure if there is a NZ branch of WG4 although I seem to recall Bill 
mentioning it in private mail to me some years back.

My own interest is not sufficient that I would now get involved. I have 
found the whole fiasco just too heartbreaking over years. Having said that 
(and it is honestly how I feel about it), I do wish the new committee well.

Hopefully lessons have been learned but I still believe it is now too late 
for COBOL.

As I've pointed out before, the fact that we may love COBOL does not mean it 
is still viable or relevant in today's world. It isn't just about COBOL; it 
is about completely new ways of developing software solutions that are 
oriented to the network. Procedural programming just won't cut it. Many of 
the people who frequent this forum are working on sites which have a big 
investment in COBOL and are continuing to maintain it while they look for a 
better idea...Most of them have not been exposed to other environments and 
therefore think that COBOL is the way... The fact is that there are some 
amazing tools and approaches that just render the maintaining of source code 
in-house unnecessary.

New approaches and tools will replace the existing systems within 10 years 
and by 2015 it will be very rare to see people using COBOL for in-house 
development. (I first predicted this in 1997 (to a barrage of derision which 
has seriously abated of late :-)); I stand by it).

In this context, it makes the work of WG4 and J4 and even the ISO/ANSI 
process irrelevant as far as COBOL is concerned. I think Roger's Open COBOL 
compiler is an excellent idea, but it is far too late. However, enthusiasts 
will certainly embrace it. I seem to recall Jimmy Gavan suggesting that Open 
COBOL might be a good idea some time in the late last century, but no-one 
seemed to pay any attention.

The history of the last twenty years of COBOL is a history of missed 
opportunities. OO was not embraced, components were not written in it 
(subsequent experience has shown that outside the COBOL enclave these two 
things are taken as read and now accepted as standard practice), there was a 
general reluctance to to extend skill sets, it took 17 years to produce a 
viable standard and it was done in a way which excluded the user base, and 
the proponents of COBOL adopted a siege mentality which led me to coin the 
term "Fortress COBOL".

It is kind of sad that COBOL's epitaph appears to be: "Too little, too 
late."

That won't stop some of us from continuing to use it :-), but it will be for 
personal rather than Enterprise use. It is already almost impossible to 
recommend that COBOL be used for Enterprise development in-house. I came to 
this sad realization some years back when attempting to make a Business Case 
for developing some new systems in COBOL. I realised then that the risks 
were just too high. You simply cannot afford to bet the company on 
maintaining source code. It is a slow, error-prone, and expensive process. 
We did it for years because there was no other viable option. Now there are 
many.

It is sad, but that's how I see it.

Pete.




"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1148230032.339594.178420@i39g2000cwa.googlegroups.com...
> Pete
>
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-22T07:42:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<grf372pibmmpi66kuhata5m6k5l67i0cl5@4ax.com>`
- **References:** `<wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com> <4ddscqF19qngrU1@individual.net>`

```
On Tue, 23 May 2006 01:24:31 +1200, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>New approaches and tools will replace the existing systems within 10 years 
>and by 2015 it will be very rare to see people using COBOL for in-house 
>development. (I first predicted this in 1997 (to a barrage of derision which 
>has seriously abated of late :-)); I stand by it).
...
>The history of the last twenty years of COBOL is a history of missed 
>opportunities. OO was not embraced, components were not written in it 
…[5 more quoted lines elided]…
>term "Fortress COBOL".

I really have my doubts that doing everything "right" for those
opportunities would have made a significant difference.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-22T12:55:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4t4uu$18j9$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net> <1148230032.339594.178420@i39g2000cwa.googlegroups.com>`

```
"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1148230032.339594.178420@i39g2000cwa.googlegroups.com...
> Jeanette Nutsford from New
> Zealand is an example who has participated via the UK group, I don't
> know whether there is an NZ group through which she can participate
> while there..

Actually, Jeanette (and Ken, for that matter), has participated as part of 
the National Delegations for both the United Kingdom and New Zealand at the 
same WG4 meetings.  Who is permitted to be a member of a National Delegation 
for a given country is strictly up to the Head of Delegation of that 
country.

> About the only requirement I can see for being a
> national committee member for the development of COBOL is an interest
> in developing the standard and anyone can be a appointed as a delegate
> (sometimes several from each country, though only with one joint vole)

Not even that.  If the HoD of a country thinks his six-year-old nephew needs 
to be a delegate, WG4 really has nothing to say about it  (reductio ad 
absurdum, of course!).

> to attend the WG4 meetings that are co-ordinated and co-located with J4
> meetings, most of which are in the US with a few in Japan and Europe,
> which reflects the majority membership.

A couple of adjustments:  Sometimes J4/WG4 do colocation, sometimes they 
don't.  We haven't in a while.  Generally speaking, every other WG4 meeting 
is in the US, the alternates are elsewhere (e.g.  Europe, Japan).

> Though not all J4 meetings
> have an associated WG4 meeting, there are usually something like two
> WG4 meetings to 6 J4 meetings per year,

Typically one WG4 meeting per year, but the last was in October 2005 and 
it's likely the next won't be until October 2007 (though the current 
schedule still says March).  We've been running five week-long J4 meetings 
per year for a while now.

>WG4 members can still follow
> the documents issued for each meeting and make reasoned comments
> regarding the iterative process of developing features via proposal
> documents that are reviewed and revised before eventual acceptance.

Yes, and they are also welcome and encouraged to participate in the J4 
processing of those documents.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-22T12:46:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4t4ec$1889$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <4d8lijF18qrteU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4d8lijF18qrteU1@individual.net...
> I read and considered this at length, Chuck. You make some good points, 
> but the overall case is not persuasive.
…[12 more quoted lines elided]…
> resourced in order to do the job, right?

J4 has not a whole lot of say as to whether member companies join it (or 
elect to stay with it).  The resources J4 has is what they have, not more. 
And what "the job" is is ultimately defined and even mandated by WG4.

>> With the Unisys-related duties I have as an employee of that company, I 
>> consider myself lucky to fit my *current* duties for J4 and WG4 
…[9 more quoted lines elided]…
> poll done or a paper written...

In a one- or two-person company, it may well be the "CEO" that gets things 
done.  Such is the condition in which at least two members of J4 find 
themselves.

>> I know of nobody on J4 whose sole responsibility to their companies is 
>> the COBOL standardization process, much less anyone whose primary 
>> financial support stems from participating in that process.
>
> So why are they there?

Because they (in the case of the one-person companies) believe that 
continuing to refine the rules by which they believe COBOL should evolve is 
a worthwhile task.  That does not mean it is, or even that it should be, 
their *only* task.

> What resources? It involves sending an email to all the COBOL vendors. 
> (presumably, J4 has a list of contacts?)

J4 has a list of contacts, but I am not aware of a list of E-mail addresses 
for those responsible for the current and future marketing requirements at 
each and every vendor of COBOL compilers worldwide!   We have *some*.

But Bill's question involved what features they would "NEVER" implement.  I 
have *serious* doubts that that's a meaningful question in the first place. 
What a given implementor will provide as feature content in a COBOL compiler 
*at any given time* is what his current or future customer base requests be 
included.

> It is a very good and useful idea and it SHOULD be done. It might be a bit 
> unrealistic to expect them to tick boxes for every facility, but it could 
> be worded so as to elicit the functions that they perceive as being most 
> difficult, and therefore unlikely to be implemented.

Well, as I said in another part of this thread, I think the standard has 
value as a "rule book" whether or not implementors choose to follow 
everything in it!   And speaking as an implementor, it's not just 
difficulty, it's "bang for the buck".  Implementors might well provide a 
feature that was difficult to implement if they felt it would improve their 
"bottom line".   I have some doubts that a more realistic question like 
"Presuming not a single customer or prospective customer mentions to you 
that this feature might be an enhancement they would like in your product, 
how likely are you to provide it *anyway*?".  There's more on this below.

> Because the COMMITTEE are the people who SHOULD be interested in the 
> result. Bill is not on the committee so he has NOT volunteered his time 
> and energy into doing this. The members of the committee have, it is in 
> their interests to do it, and that is why the committee SHOULD do it, 
> rather than Bill.

In the particular case of the regression suite, I haven't seen an argument 
that has convinced me that it's the job of J4 members to write this set of 
programs.

In the case of the "feature content survey", I am certain that Unisys would 
not be willing to discuss the planned-but-as-yet-unannounced feature content 
of its (current or future) products with J4 for any reason.    That is 
considered proprietary marketing information.   I could not get permission 
to provide such information; I would be fired on an ethics violation for 
divulging it.  And as indicated above, even if it were accurate *today* it 
might not be accurate *next week*.   I believe the same points hold for all 
of the vendors, and render the validity of the information that could be 
gleaned from such a survey virtually meaningless.

> So, given that you cannot produce a yardstick for the proposed standard, 
> why are you wasting time and effort producing it? It's like printing money 
> without any way to verify whether it is genuine or not.

I disagree that it has no value without a regression suite.  *Enforcement* 
is impossible without it, but a good-faith effort to follow the rules for a 
given feature is worthwhile, and thus I believe the standard itself is 
worthwhile.

> Actually, such a yardstick is essential, but there is no requirement that 
> you or any other member of the committee must produce it personally. The 
> function of the committee is to facilitiate; so get facilitating... :-) 
> You already suggested one avenue that might achieve this.

It's been brought up before at J4 meetings; I just haven't been able to find 
the reference in the minutes.  My *recollection* is that J4 put out an 
invitation to the World At Large for the development of the regression 
suite.  This was sometime around the period that EDS dropped out of J4; they 
were the last organization to have responsibility for the regression suite.

Interesting point, though:  It's my understanding, based on a conversation 
at J4 last week, that once *enforcement* was dropped, not a single vendor 
approached EDS to have their products validated.  So if someone spends a 
whole lot of effort to write a regression suite, what is going to motivate 
vendors to submit their products for evaluation (whether it's done for-fee 
or free-gratis)?

< There, you've already started facilitating :-) A public appeal for some 
help
> and on a specific topic too. Now get some of those CEOs to call in a few 
> favours and make a few phone calls...:-)

I'd rather start with a Certain University.  I think Corporate Sponsorship 
has a higher likelihood of favoring a particular implementation or vendor. 
Probably sometime this week I'm going to send an E-mail to see if I can 
shake something loose.

>> For item 3, I think much of this is already covered by "processor 
>> dependent"; the problem is in getting the National Bodies to agree on 
…[5 more quoted lines elided]…
> present cases and discuss the options; majority rules. Get over it.

Been there.  Done that.  WG4.  They want it all, and they *don't* want 
options.  I think the ability to do this at all was probably the result of 
the fact that the SCREEN SECTION represented a green-screen approach and was 
already obsolete before the standard came in.  Before that, I think WG4's 
position was "all or nothing at all".   There are a total of thirty-one 
items in the processor-dependent list in the '02 standard.  Some of these 
are obvious:  if your machine doesn't have a mass storage device, you don't 
have to support the DELETE, OPEN I-O, REWRITE, or USE ... I-O.

> (If I bring my own seat, can I turn up anytime? :-))

Actually, yes -- all you have to do is let the chair know you're coming.

>> We have used teleconferencing methods occasionally, but have found that 
>> there are circumstances in which they are not as effective as 
…[11 more quoted lines elided]…
> documents or other instruments.

In the one instance where we tried it for the whole meeting, it did not 
involve *video* teleconferencing, because it wasn't available to the people 
who were at remote sites.  And if the people that really need to be there 
don't have access to the video part of it (or their corporations are 
unwilling to provide the equipment for such access), there's not much the 
other J4 members can do about that!   We do use *audio* teleconferencing 
extensively, have for some time.

> In what way is J4 discouraging participation by end
>> users?
…[5 more quoted lines elided]…
> points arising out of J4 meetings.

Well, hey.  I do what *I* can.  The J4 documents are currently, and have 
been for some time, at www.cobolportal.com/j4/.  There's a mailing list, 
including E-mail addresses, for all current members and alternates, and a 
number of other "interested parties".  Granted, this website isn't set up 
with all the "whizbang" graphics and videos one might hope for, but the 
information's there!

> Hardly a fair question... the person it was directed at is not currently 
> on J4 and has bad past experience with the red tape involved.

To be a guest at a meeting, all one has to do is notify the chair.  My 
recollection is that about one meeting out of five is held within relatively 
easy commuting distance of this particular person's home, and I have to 
admit being rather surprised that he had not been there.

> If I were him I wouldn't want to attend either.

Well, that's your choice, and his.  But someone being unwilling to 
participate at the face-to-face meetings out of resentments from the past 
does not give me confidence they would be champing at the bit to participate 
in teleconferences!

> If the question is directed to the community at large, I can say, speaking 
> only for myself, I wouldn't attend a meeting where 6 people who have no 
> clear agenda or idea of what they SHOULD be doing, are sitting round 
> discussing COBOL.

There is a clear agenda, and the people who are discussing this agenda have 
a pretty good idea of what they should be doing because WG4 has made it very 
clear what they should be doing.  "The future of COBOL" does end up being 
discussed, but pretty much mostly at breaks.

> It's a big subject. You could discuss it for hours...

Yeah, we could.  We could also be discussing "What's it gonna take to get 
this standard out the door", which is what WG4 has made it clear *they* want 
us to be discussing!

> It isn't discussion that gets standards produced, it is drafts and 
> revisions in the light of feedback. (It's called INTERACTION and 
> ITERATION; fundamental to the RAD process...

Yeah, and ...?  Every single iteration and every single adjustment to 
proposals is reflected in the J4 documents.  Some of those revisions come 
from internal comments at J4, others come from written proposals from within 
and without J4.

>>
>> I agree with you there.  I've made that clear on numerous occasions.  I 
…[3 more quoted lines elided]…
> Why do you suppose they relaxed it?

I think it ran something like this:  the Executive Branch of the federal 
government at the time decided that implementors were being subjected to 
unnecessary costs in having to validate their compilers against the language 
standards (not just COBOL), that those costs were being passed on to other 
businesses, and that the requirement by the Defense Department that all 
compilers used therein be validated was an unfair burden on small 
businesses.  In a parallel move, the administration turned the maintenance 
and running of the validation suite to a private company, who was expected 
to charge a fee for validating compilers.  As it happens, with no *legal 
requirement* for validation, none of the vendors had any incentive to spend 
the money to have their products validated.  This was all part of 
"trickle-down economics", as I remember.


> Simple resolution to that problem... give them what they want and drop 
> what they don't.

We actually agree -- the only difference is that it's the *vendor* who 
decides what features he's going to offer and what features he's not.  Some 
of those will be "vendor-specific", some of those will be features verbatim 
and literatim from the standard.  The standard encourages vendors to follow 
certain rules for certain features.  I don't have a problem with that as the 
standard's primary role, given the lack of an enforcement mechanism!

>> I don't think the National Standards bodies are going to be convinced by 
>> us Techies.  I think they're going to have to be convinced by CEO's of 
>> Very Large Corporations as to how this affects *their* bottom lines.
>
> Then you might as well quit now.

I believe in the COBOL standardization process.  I will also be 62 years old 
next month.  I ride a motorcycle 33 miles to work every day along a canyon 
road.  Realistically speaking, how long do you think I'm going to be 
involved in the COBOL standardization process anyway?

> NO CEO is going to bet the corporate farm on COBOL.

> It cannot be justified and no suitable Business Case can be made for it in 
> this day and age. If you take a 3 year view, have extensive applications 
…[3 more quoted lines elided]…
> term. Long term, you can't.

I'm not convinced that it's as short term as you indicate.  There are some 
pretty huge businesses running some pretty huge "bespoke" applications out 
there.  A lot more of the world runs on COBOL than a lot of people are 
willing to admit.

> And astute CEOs know it. It isn't about the technical merits or otherwise, 
> it is about the future of procedural programming in house as a solution to 
> commercial IT requirements. The world has moved on, the network is 
> becoming ever mightier, and tools and computer literacy are becoming 
> exponentially greater than was the case in COBOL's heyday.

Don't disagree; small local shops having their own home-written COBOL 
applications on the likes of System/3 and Burroughs B1000 systems have 
either grown enough to warrant much bigger machines or gone to the likes of 
QuickBooks.  No argument.  But QuickBooks doesn't hack it (pardon the pun) 
for large customers with unique needs, and if their applications work, and 
can be "encapsulated" in a way that makes them work and function seamlessly 
in a "GUI" environment, why fix what's broke?

>>And even if either approach succeeded, I'm not convinced it's either WG4 
>>or J4 that would be in a position to produce a regression suite -- in 
…[6 more quoted lines elided]…
> quality assurance for eggs).

And that's where J4 as a *consultant* in the process comes in.  The person 
who composes the standard's description of a feature might have a blind spot 
with respect to one or more flaws in it that the author of a validation 
program for that feature is more likely to catch.  I think this is a *vital* 
source of corrigenda to the standard as the suite gets written.  I still 
argue for direct authorship of the regression suite from outside the body of 
folks responsible for the rules themselves.

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-20T19:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zdKbg.167109$Gi7.22251@fe06.news.easynews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com>`

```
(previous material "snipped")

Chuck (et al),
   I know that you and I will never agree on what is/would be/might be "best" 
for COBOL (vendors and users) and I hope I try to "respect" your opinions (even 
though I disagree with them).  Without an "alternate universe" machine to test 2 
different paths, there really is no way to determine which (if either) of us is 
"correct".

However, ...

    ****

Much of my "negative" feeling toward the committee and standard can be 
summarized as follows:

1) (To me), to be considered a "viable" language Standard, at least 2 vendors 
(or possibly one vendor on 2 distinct platforms) must implement (or have 
publicly stated implementation plan) for a "fully conforming Standard".  Without 
this, no reasonable level of source code portability can/should be expected. 
The 2002 Standard does not have this - and I (personally) see nothing in J4's 
(or WG4's) work that is addressing WHY this is true (or how to correct it).

2) (To me) a valid feature (enhancement) in a language Standard must be 
implemented (or be in the process of being implemented) by a MAJORITY (not all - 
but majority) of "commercially delivered" compilers - for compiler/vendor 
combinations where they ARE continuing to provide "regular" (12-18 month) new 
releases/versions "with enhancements". It is my perception that ALMOST none of 
the new (and certainly none of the MAJOR) new features of the '02 Standard have 
been implemented by ANY vendor - who didn't have the features in their existing 
product by 1997 or at least 2001.  Again, I haven't seen any effort on J4 or 
WG4's part to determine WHY "new features" for which their were insufficient 
"business cases" for adding to real-world compilers were added to the '02 
Standard - and whether such features SHOULD be kept as required by the '08 
Standard.

3) (To me) a valid language Standard's committee should have either members (or 
at least "paid observers") from a majority (again not all) vendors of compilers 
of that language that are continued to be "enhanced".   As far as I can tell, J4 
has not addressed WHY most existing COBOL vendors do NOT feel that it is even 
worth "observing" the J4 process (much less participating in it).  This seems 
(to me) to indicate that they view both the committee and its work as 
"irrelevant" to their needs AND those of their customers.

4) (To me) the BIGGEST failure of J4 (and WG4) has been its refusal to do "post 
mortems" on is previous work and workings.  Although there was (some - not a 
lot) of "finger pointing" explaining the delay in the '02 Standard, there was 
very little effort put into actually thinking about what went right and what 
went wrong.  I know that J4 (and WG4) both agreed that it was CRITICAL to not 
"slip" the time-frame for the '08 Standard and not to allow "feature creep" into 
its development, but other than that, I have seen (from the outside) no other 
serious looks at either the process or the content that lead to an 
un-implemented Standard with a shrinking committee for a programming language 
receding in importance.  Were/are there things that could/should be done?  I am 
NOT looking for "self-flagellation" - but would have thought that "learning from 
past mistakes AND successes" should have been a high priority.
```

###### ↳ ↳ ↳ Re: What could J4 (or WG4) do (was: INSPECT and TRAILING syntax

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-22T14:11:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4t9ec$1bap$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com> <JBO8g.400208$BL7.371029@fe09.news.easynews.com> <e4l8g3$2kjv$1@si05.rsvl.unisys.com> <zdKbg.167109$Gi7.22251@fe06.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:zdKbg.167109$Gi7.22251@fe06.news.easynews.com...

> 1) (To me), to be considered a "viable" language Standard, at least 2 
> vendors (or possibly one vendor on 2 distinct platforms) must implement 
…[4 more quoted lines elided]…
> this is true (or how to correct it).

Whether I agree or disagree with the position, the issue of "modularity" and 
"optionality" in my opinion lies squarely on WG4's shoulders.  The 
discussions on this point to which I was privy in the two most recent Las 
Vegas meetings as well as the one in the Hague (I missed Nara) were heated 
and unequivocal.   This was considered one of the MAJOR shortcomings of the 
1985 standard and was Not To Be Tolerated in any standard that followed it. 
Period.

I also am a bit uncomfortable with the expectation that *any* vendor *must* 
provide product planning information to J4, whether under a confidentiality 
agreement or not, much less to the world at large.  As I've said elsewhere, 
this requirement raises ethics issues.   I can't comment on Unisys' *future* 
product plans, and don't feel it's appropriate for me to demand that some 
authorized representative do so.  I don't think "Macy's has to tell 
Gimbal's" which products they're going to be putting in their Fall 
Collection, regardless of where those products were designed!

> 2) (To me) a valid feature (enhancement) in a language Standard must be 
> implemented (or be in the process of being implemented) by a MAJORITY (not 
> all - but majority) of "commercially delivered" compilers - for 
> compiler/vendor combinations where they ARE continuing to provide 
> "regular" (12-18 month) new releases/versions "with enhancements".

Well, that's interesting.  The initial official release of the Unisys MCP 
COBOL85 compiler was made available, best I can determine, around 1992.

I think the COBOL74 compiler for the Burroughs Large System was made 
available around 1980 or so to fulfil the DoD marketing requirement that we 
provide a validated compiler, and it was still having serious teething 
troubles in 1984 when I began working on it, partly because for quite a long 
time no customers used it or felt the need to use it, as the old reliable 
COBOL(68) compiler served their needs.   We discontinued support for 
COBOL(68) in December 1999, and our COBOL74 compiler remains a 
fully-supported product today, with a *significant* number of satisfied 
users.

If an *implementor* has reason to believe that its *particular customers* 
won't use a feature, why should the implementor be *required* to provide it?

More to the point, why should *J4* be called to task because they were told 
to standardize a feature or a functionality based on user demand at the 
*standardization* level, and that user demand failed to materialize at the 
*economic* level?

>Again, I haven't seen any effort on J4 or WG4's part to determine WHY "new 
>features" for which their were insufficient "business cases" for adding to 
>real-world compilers were added to the '02 Standard - and whether such 
>features SHOULD be kept as required by the '08 Standard.

WG4 is adamant that features *NOT* be "optional" in standard COBOL. 
"Processor dependent" status was allowed very, very reluctantly.  What the 
business cases are for an individual implementor are unique to that 
implementor, and I would expect that to be proprietary information. 
"Inquiring minds want to know" is not a sufficient justification for (say) 
IBM or Unisys to release its five-year software product plans.

> 3) (To me) a valid language Standard's committee should have either 
> members (or at least "paid observers") from a majority (again not all) 
> vendors of compilers of that language that are continued to be "enhanced".

I can't speak for other vendors.  I see two classes:  those who provide 
compilers for particular proprietary platforms ("enterprise servers", AKA 
"legacy mainframes"), and those who provide compilers for "commodity" 
platforms.  As I see it, at least all the major players in the former 
category are participating.  At the risk of omitting somebody, I'd further 
state that that's all both of them.   I gather Micro Focus may be playing in 
this arena as well.  As to the others, there are a number of people from at 
least one other compiler vendor that participate actively in the process, 
*and contribute to the development of standards features*, whether or not 
there'll be a "fully-conforming" implementation on their platform or on any 
others.

Whether those players are planning to enhance their compilers -- or planning 
to *announce* their plans to enhance their compilers -- or not -- is a 
marketing issue that I can't address.

> As far as I can tell, J4 has not addressed WHY most existing COBOL vendors 
> do NOT feel that it is even worth "observing" the J4 process (much less 
> participating in it).

One answer *could* be that they trust the process enough to presume that 
what the process will produce is of value to them.

Another answer *could* be that *in their particular environments* they have 
no market demand for the features of any standard later than '85 (or the '89 
amendment).  That *those* implementor's don't feel customer demand for a 
fully-conformant '02 (or later) compiler does not mean that no such demand 
exists.  I don't have a problem with the sets of demands for individual 
features of compiler standards from different vendors not being identical; I 
don't even have a problem with those sets being entirely disjoint.   I don't 
think that has anything to do with the value of the features.

> This seems (to me) to indicate that they view both the committee and its 
> work as "irrelevant" to their needs AND those of their customers.

May be.  I'm ill-equipped to speak for them, and it would raise ethical 
issues for me to attempt to speak *to* them on that subject.

) (To me) the BIGGEST failure of J4 (and WG4) has been its refusal to do 
"post
> mortems" on is previous work and workings.  Although there was (some - not 
> a lot) of "finger pointing" explaining the delay in the '02 Standard, 
> there was very little effort put into actually thinking about what went 
> right and what went wrong.

Just out of curiosity, Bill, in your opinion, how much time and energy 
should J4 have committed to this process of figuring out what all the 
process failures were in the publication of the 2002 standard, and getting 
new processes developed to replace the old ones so that such a delay would 
not occur again?  How much time should WG4 have devoted toward verifying the 
"business case" for the features they requested that J4 include in the next 
draft?

Contemplating one's navel has its place, but I'm not convinced that 
contemplating the causes of the main failings of the 2002 standard -- e.g., 
"too much, too late" -- is worth the *delaying* of the production of the 
next standard.   Spending a whole lot of time on processes and customer 
surveys and marketing analyses would be nice, but I think it'd have added 
*way* too much time to the process after the publication of the 2002 
standard, and the 2008 standard would receive the same "too late" complaint 
that the 2002 did.   I think 2008 (or 2009) is marginally too long, but I 
don't think J4 could have shortened the time frame any.  And given the 
demands for *mandatory feature, must be included* from WG4, what J4 might 
have had to say as the result of subsequent marketing surveys doesn't 
matter -- WG4 said do it, by and large J4 did it (there were a couple of 
features that fell out because J4 simply didn't have resources to design 
them).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T19:51:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cit4dF162r17U1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <wqU7g.432129$7i1.140664@fe06.news.easynews.com> <e3q4le$1lf5$1@si05.rsvl.unisys.com> <4ce5dlF15a7qgU1@individual.net> <mbq8g.73852$JV1.55476@fe05.news.easynews.com> <4cgus9F15np3pU1@individual.net> <e3vlh4$1tuv$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:e3vlh4$1tuv$1@si05.rsvl.unisys.com...
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:4cgus9F15np3pU1@individual.net...
…[10 more quoted lines elided]…
>

So why have standards?

<snip>
> For example, I think one of the best things J4 and WG4 have done is the 
> new arithmetic mechanisms in the2008 draft -- I'm prejudiced, of course. 
…[8 more quoted lines elided]…
>
Gosh, yes. Let's have computers that can do arithmetic. Pity CODASYL never 
thought of that...

> Too little, too late?  Well, maybe.  I first became aware of the IEEE 754 
> effort and recognized the  importance to COBOL of the Decimal128 and 
…[4 more quoted lines elided]…
> the current working draft.

4 years huh? And still no sign of it... and if it DOES happen, no way to 
ensure anyody implements it.

Why have standards?



> It's not clear to me that I could have got it done much more quickly.

This discussion was never intended to be personal and I state again that I 
have nothing but the highest respect for your dedication and ability, Chuck.

If you choose to waste your time with a pointless, toothless, bunch of 
wankers who have done no service for COBOL, that is entirely a matter for 
you :-)

> I can't even say whether the IEEE 754 proposals will end up being 
> something that the COBOL standard can legitimately reference when push 
> comes to shove.  What I can say is that I think the feature content is a 
> Big Improvement at the very core of the COBOL language, and that I've done 
> my best to make it work.

Sure, and who knows, maybe your efforts might have made some difference. But 
the outcome is the same. No results, and nobody being encouraged to even 
implement the 02 standard. It is a pointless exercise. Surely, the past 
experience has demonstrated that. I see no changes being implemented.

  In general, I think I've made some
> fairly decent contributions to the COBOL standard given that I'm a 
> relative newbie to the COBOL standardization process, having attended my 
> first meeting as Unisys' representative on J4 in December 2000.
>

Well, that's all right then...:-)  As long as YOU think so...

> And I know you have disagreed with the feature-content priorities of J4 
> and WG4  over the years.

Yeah, I reckon an unbiased observer could glean that from the tirades I have 
repeatedly posted here :-).

Actually, I really am over it now. But it still hurts when I think about it 
so, as a general rule, I don't...

>But if Pete Dashwood says he wants feature "x", and DIN and BSI have 
>decided that they want feature "y" instead, it's kind of incumbent on WG4 
>to instruct J4 to work on feature "y".

Actually, Pete Dashwood has NEVER said he wanted ANYTHING in the COBOL 
standard. On the contrary, Pete Dashwood has consistently questioned the 
usefulness of and the effectiveness of both the standards committee and the 
standard. My position has been (and still is) that COBOL is better off 
without a standard, given that the governing standards body is about as 
useful as boxing gloves to a watchmaker.


>The whole process is driven by *national standards bodies*.  I know you 
>disagree with that approach, but neither J4 nor WG4 have any say in whether 
>that's the appropriate way for formal international standards to be 
>developed and adopted.

Precisely. So what exactly CAN they do? They are part of the ISO/ANSI gravy 
train. (Oops, sorry that is a non-profit gravy train of course...) Why can't 
they have a word to the Engineer and get a few things changed? It is now far 
too late as the COBOL train is headed onto a siding that ends in Oblivion 
County. (No one ever goes there unless they're stoned or pissed...) If 
people were serious about a COBOL standard it should have been sorted years 
ago.


> Nor do they have any say over whether any implementor decides to market a 
> product that conforms, in every detail or only in part, to that standard.
>
So why have a standard? What good is a law without enforcement? And nobody 
is going to stand for being enforced to implement what a committee that long 
ago lost all credibility, is saying COBOL needs to make it viable.

> I know of no work that J4 or WG4 can do to force or even encourage 
> everyone from IBM through TinyCobol, or any subset of that group, to 
> incorporate every single widget of every single doodad in the 2002 
> standard, to say nothing of the 2008 draft, under threat of ... what ...?
>

Threat of not being allowed to call it COBOL for a start...

But I tire of this so I'll not present all the other arguments, that won't 
make a jot of difference anyway.

I don't understand why a talented capable person like yourself would lend 
your energy to this farce, but that is your prerogative and I'm sure you 
have your reasons. (C'mon... level with us... is someone paying you to do 
this :-)?)

I honestly wish you luck, Chuck.

Pete.
```

#### ↳ Re: INSPECT and TRAILING syntax

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-09T09:51:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cbs4hF14rcseU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com>`

```
>>>> Roger While<simrw@sim-basis.de> 05/08/06 9:29 PM >>>
>Seems weird to me that alongside ALL, FIRST and LEADING
>the TRAILING keyword never made it into any standard.
>Bill, was it ever considered ?
>ACU implements it and I have just put it into OpenCOBOL.

I totally agree.  I'm much more likely to use TRAILING than LEADING.  (In
fact I have utilized LEADING with FUNCTION REVERSE in order to simulate
TRAILING.  I don't agree with those that think that TRAILING should not be
added just because you can use LEADING with FUNCTION REVERSE.  I am all for
so-called "syntactic sugar" when it makes things easier to code and easier
to read.

Of course the (now dead?) COBOL 2008(?) standard appears to support even
more useful things such as FUNCTION TRIM(argument [left/right]) and the ANY
LENGTH clause.  For instance:

FD varlen-file.
01  varlen-record  PIC X ANY LENGTH LIMIT 120.

01  my-fixed-field PIC X(120).
01  my-varlen-field PIC X ANY LENGTH LIMIT 80 DELIMITED.

ACCEPT my-fixed-field
WRITE varlen-record FROM TRIM(my-fixed-field)

MOVE TRIM(my-fixed-field RIGHT) TO my-varlen-field
CALL c-func USING my-varlen-field

Not sure if I have all of the above correct, but I think the meaning is
fairly obvious.
Feel free to implement it into OpenCOBOL.  :-)

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-09T10:07:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net>`

```
On Tue, 9 May 2006 09:51:41 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>I totally agree.  I'm much more likely to use TRAILING than LEADING.  (In
>fact I have utilized LEADING with FUNCTION REVERSE in order to simulate
…[3 more quoted lines elided]…
>to read.

Using FUNCTION REVERSE for this purpose grates on me.   Sure,
computers are fast and this ugly code doesn't cost as much as it used
to.    

I'd much rather use reference modification than use a function to copy
and reverse the string so that we can run a CoBOL command.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-09T16:37:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ccjtrF15hi17U3@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com>`

```
Howard Brazee<howard@brazee.net> 05/09/06 10:07 AM >>>
>On Tue, 9 May 2006 09:51:41 -0600, "Frank Swarbrick"
><Frank.Swarbrick@efirstbank.com> wrote:
…[3 more quoted lines elided]…
>>TRAILING.  I don't agree with those that think that TRAILING should not
be
>>added just because you can use LEADING with FUNCTION REVERSE.  I am all
for
>>so-called "syntactic sugar" when it makes things easier to code and
easier
>>to read.
>
…[5 more quoted lines elided]…
>and reverse the string so that we can run a CoBOL command.

I assume you mean something like...

COMPUTE TRIMMED-LEN = FUNCTION LENGTH(MY-STRING)
PERFORM VARYING R FROM FUNCTION LENGTH(MY-STRING) BY -1 
        UNTIL  R = ZERO OR MY-STRING(R:1) NOT = SPACE
    SUBTRACT 1 FROM TRIMMED-LEN
END-PERFORM

Is than better than this?
MOVE ZERO TO TALLY
INSPECT FUNCTION REVERSE(MY-STRING) TALLYING TALLY FOR LEADING SPACES
COMPUTE TRIMMED-LEN = FUNCTION LENGTH(MY-STRING) - TALLY

Maybe, maybe not.  But I'd definitely prefer
MOVE ZERO TO TALLY
INSPECT MY-STRING TALLYING TALLY FOR TRAILING SPACES
COMPUTE TRIMMED-LEN = FUNCTION LENGTH(MY-STRING) - TALLY

Or, of course, best of all would be:
COMPUTE TRIMMED-LEN = FUNCTION TRIM(MY-STRING RIGHT)

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-09T20:29:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1262gf5g7m80nbd@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net>`

```
Frank Swarbrick wrote:
> Howard Brazee<howard@brazee.net> 05/09/06 10:07 AM >>>
>> On Tue, 9 May 2006 09:51:41 -0600, "Frank Swarbrick"
…[37 more quoted lines elided]…
> Frank

Fujitsu has:

COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-10T09:01:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3s356$en4$03$1@news.t-online.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com>`

```
> Fujitsu has:
>
> COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).

Are these Fujitsu extensions documented anywhere on Internet ?


Re: using FUNCTION REVERSE (or whatever)
Of course, the Cobol runtime has to acquire memory to do this
(as with many other FUNCTION's) which may or may not ever
be free'd/reused.
So be careful using this in a paragraph you are perfoming a
couple of million times  :-)
Your sysadmin might come knocking on your door  :-)

Roger While

"HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag 
news:1262gf5g7m80nbd@news.supernews.com...> Fujitsu has:
>
> COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).

> Frank Swarbrick wrote:
>> Howard Brazee<howard@brazee.net> 05/09/06 10:07 AM >>>
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-10T09:54:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1263vl5rbif2lda@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s356$en4$03$1@news.t-online.com>`

```
Roger While wrote:
>> Fujitsu has:
>>
>> COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).
>
> Are these Fujitsu extensions documented anywhere on Internet ?

http://www.adtools.com/products/windows/cobol.htm

(also available in their FORTRAN compiler, I believe)
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 7)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-10T18:02:03+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3t2q2$c9u$01$1@news.t-online.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s356$en4$03$1@news.t-online.com> <1263vl5rbif2lda@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag 
news:1263vl5rbif2lda@news.supernews.com...
> Roger While wrote:
>>> Fujitsu has:
…[7 more quoted lines elided]…
> (also available in their FORTRAN compiler, I believe)

No, that's no good.
I don't want version highlights.
I need reference doc.
Just like ACU, Fujitsu do not seem want to put
their reference manuals on the net. Pfui.
At least MF have their complete doc on the web.

Roger While
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2006-05-10T11:26:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147281666_4697@sp6iad.superfeed.net>`
- **In-Reply-To:** `<e3t2q2$c9u$01$1@news.t-online.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s356$en4$03$1@news.t-online.com> <1263vl5rbif2lda@news.supernews.com> <e3t2q2$c9u$01$1@news.t-online.com>`

```
Roger While wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag 
> news:1263vl5rbif2lda@news.supernews.com...
…[18 more quoted lines elided]…
> 

<http://www.adtools.com/download/index.htm>

Jeff Campbell
n8wxs@arrl.net

----== Posted via Newsfeeds.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-12T01:29:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cgsidF15rcjsU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s356$en4$03$1@news.t-online.com> <1263vl5rbif2lda@news.supernews.com> <e3t2q2$c9u$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e3t2q2$c9u$01$1@news.t-online.com...
> "HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag 
> news:1263vl5rbif2lda@news.supernews.com...
…[20 more quoted lines elided]…
>
Well, Gee, Roger, if you looked a little harder you'd find the entire 
reference manual set on the web at the same site. Pretty decent of them 
really. Considering SOME people want to reverse engineer the product... :-) 
(I can't imagine why...you'd think they'd let it go with dignity...)

Pfui yourself :-)

Pete.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-11T09:39:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1266j5g2nvq1m87@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s356$en4$03$1@news.t-online.com> <1263vl5rbif2lda@news.supernews.com> <e3t2q2$c9u$01$1@news.t-online.com>`

```
Roger While wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag
> news:1263vl5rbif2lda@news.supernews.com...
…[16 more quoted lines elided]…
> At least MF have their complete doc on the web.

====== begin quote
FUNCTION STORED-CHAR-LENGTH (argument-1)

Argument

1. Argument-1 must be alphanumeric or national characters. It must not be a
group item.
2. Argument-1 must consist of one or more characters.

Function Value

1. The function value is the number of character positions of the effective
characters contained in argument-1.
2. When argument-1 is the alphanumeric class, the function value indicates 
the
number of alphanumeric character positions of the effective characters.
3. When argument-1 is the national class, the function value indicates the 
number
of national character positions of the effective characters.
4. The characters stored in argument-1 must follow the encoding forms 
dictated by
the class of argument-1. Otherwise, the result is undefined.

Function Type

The function type is integer.

===== end quote

http://www.adtools.com/download/v8manuals/NetCOBLanguageRef.pdf

(pdf file, 14 megabytes)
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-10T10:18:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3s7le$6sj$00$1@news.t-online.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag 
news:1262gf5g7m80nbd@news.supernews.com...
> Fujitsu has:
>
> COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).
>
>

Sounds useful. Just implemented it in OpenCOBOL  :-)
Question, does it only check for trailing spaces or does it
also check for low-values ?

Roger While
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T08:21:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmt362d9e4t2a51gqr49tat5olnh7h1djn@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s7le$6sj$00$1@news.t-online.com>`

```
On Wed, 10 May 2006 10:18:50 +0200, "Roger While" <simrw@sim-basis.de>
wrote:

>> COMPUTE TRIMMED-LEN = FUNCTION STORED-CHAR-LENGTH(MY-STRING).
>>
…[4 more quoted lines elided]…
>also check for low-values ?

Just make it easy to add function libraries.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-10T09:52:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1263vglr25dvq8b@news.supernews.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <1262gf5g7m80nbd@news.supernews.com> <e3s7le$6sj$00$1@news.t-online.com>`

```
Roger While wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> schrieb im Newsbeitrag
> news:1262gf5g7m80nbd@news.supernews.com...
…[8 more quoted lines elided]…
> also check for low-values ?

Spaces only.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-10T08:20:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kt362l0cg4snorev2nveuo7q1643st92r@4ax.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net>`

```
On Tue, 9 May 2006 16:37:47 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>I assume you mean something like...

I agree with your whole post.
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-10T10:24:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ceidqF158quvU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <bbf162tid4nlvhc6ss727i1nmurlp2m36f@4ax.com> <4ccjtrF15hi17U3@individual.net> <6kt362l0cg4snorev2nveuo7q1643st92r@4ax.com>`

```
Howard Brazee<howard@brazee.net> 05/10/06 8:20 AM >>>
>On Tue, 9 May 2006 16:37:47 -0600, "Frank Swarbrick"
><Frank.Swarbrick@efirstbank.com> wrote:
…[3 more quoted lines elided]…
>I agree with your whole post.

I feel faint.
Please don't agree with me.
It makes me woozy.
:-)
```

##### ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-09T09:20:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3qfh4$1scp$1@si05.rsvl.unisys.com>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:4cbs4hF14rcseU1@individual.net...

> Of course the (now dead?) COBOL 2008(?) standard ...

Rumors to that effect are, I think, premature.

J4 plans to continue to meet, even with a vice-chair, for the foreseeable 
future and has meetings scheduled next week, at the end of July, in October, 
and in December of this year, presuming INCITS doesn't prevent it.  Note 
that I'm acting vice-chair of J4, so we *can* conduct meetings, and we 
expect to have a permanent vice-chair by the beginning of the July/August 
meeting (so I won't have to act as host, secretary and chair all at the same 
time for that meeting!).

WG4 meets in March 2007, and as far as I'm concerned the main goal of that 
meeting is to move the 2008 draft on its path toward adoption, by which 
point it is hoped that the work of J4 on that draft will be pretty much 
done.

Membership of J4 is still sufficient for quorum -- in fact, because Micro 
Focus has a designated alternate representative who is still employed by the 
company, they're still a member despite Don Schricker's departure as their 
primary representative and as chairperson of the committee, and we do have 
more than one person "legitimized" by INCITS to conduct the meetings.

I do intend to lobby at the INCITS level for them to allow J4 to continue 
its business even without a designated chairperson.

WG4 has delegated the technical work to J4 in the past.  If INCITS decides 
(despite our efforts to the contrary) to disband J4 on the sole grounds that 
nobody has (yet) stepped up to take on the permanent chairmanship, I don't 
see any reason why WG4 can't continue the final editorial cleanup of the 
2008 standard, as well as the development of future standards, if they so 
chose.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-09T16:50:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cckmdF14k81oU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <e3qfh4$1scp$1@si05.rsvl.unisys.com>`

```
Chuck Stevens<charles.stevens@unisys.com> 05/09/06 10:20 AM >>>
>
>"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
…[7 more quoted lines elided]…
>future and has meetings scheduled next week, at the end of July, in
October, 
>and in December of this year, presuming INCITS doesn't prevent it.  Note 
>that I'm acting vice-chair of J4, so we *can* conduct meetings, and we 
>expect to have a permanent vice-chair by the beginning of the July/August 
>meeting (so I won't have to act as host, secretary and chair all at the
same 
>time for that meeting!).
>
>WG4 meets in March 2007, and as far as I'm concerned the main goal of that

>meeting is to move the 2008 draft on its path toward adoption, by which 
>point it is hoped that the work of J4 on that draft will be pretty much 
…[3 more quoted lines elided]…
>Focus has a designated alternate representative who is still employed by
the 
>company, they're still a member despite Don Schricker's departure as their

>primary representative and as chairperson of the committee, and we do have

>more than one person "legitimized" by INCITS to conduct the meetings.
>
…[3 more quoted lines elided]…
>WG4 has delegated the technical work to J4 in the past.  If INCITS decides

>(despite our efforts to the contrary) to disband J4 on the sole grounds
that 
>nobody has (yet) stepped up to take on the permanent chairmanship, I don't

>see any reason why WG4 can't continue the final editorial cleanup of the 
>2008 standard, as well as the development of future standards, if they so 
>chose.

Tell Bill to stop spreading nasty rumors!  :-)

I have a curious question about J4 and the COBOL standards...  It looks like
some (most? all?) of the major COBOL vendors have members on this commitee. 
Yet I haven't heard that any vendor has made any statement with regard to
supporting the entire COBOL 2002 standard, much less the follow-on standard.
 Is there some commitment there?  And if not, why not?  I know many vendors
have implemented parts (some more than others), but I haven't heard of any
vendor supporting all, or even most, of it.

I did see that Hitachi has something called "The COBOL2002 Family".  I
haven't determined whether or not this implements the entire 2002 standard
or not.  Plus it looks like Hitachi is pretty much focused on the Japanese
market only, or at least all of the web references seem to be in Japanese!

Anyway, having an IBM compiler I am especially interested to hear what their
"statement of direction" for COBOL might be.  Anyone know?

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: INSPECT and TRAILING syntax

_(reply depth: 4)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-05-10T12:37:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147289859.239151.207180@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<4cckmdF14k81oU1@individual.net>`
- **References:** `<e3p2b2$fmv$01$1@news.t-online.com> <4cbs4hF14rcseU1@individual.net> <e3qfh4$1scp$1@si05.rsvl.unisys.com> <4cckmdF14k81oU1@individual.net>`

```

Frank Swarbrick wrote:
> Chuck Stevens<charles.stevens@unisys.com> 05/09/06 10:20 AM >>>
> >
…[69 more quoted lines elided]…
> FirstBank Data Corporation - Lakewood, CO  USA

It seems to me that most of the investment in time and money towards
producing the 2002 and 2008 standards came from the vendors themselves,
with relatively minor, though not necessarily insignificant, input from
a few other interested persons.  If ISO had not adopted the standard
from CODASYL, it is conceivable that the vendors and other interested
parties could continue to develop it independently with or without a
chairman.  Now that the 2002 standard has been created under the
auspices of ISO, it seems unlikely that ISO will allow it to go
"independent" again, what with copyright, etc issues.  Ultimately, I
suppose, further development depends on the preparedness of  vendors
and perhaps large consumers to provide support, which depends on what
they see in it from expected benefits in the way of sales and need to
support and extend existing systems and develop new ones..

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
