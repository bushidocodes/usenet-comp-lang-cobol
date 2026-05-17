[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How convert 999x99 to 999X99?

_11 messages · 10 participants · 1996-11 → 1996-12_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### How convert 999x99 to 999X99?

- **From:** "byate..." <ua-author-14787294@usenetarchives.gap>
- **Date:** 1996-11-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

Hi,

I am writing a program as homework in which the user enters a
part code on the screen and then the ACCEPT command transfers the data
into the working storage area, PARTS-CODE-IN PIC x(5).

The program then searches a table to see if the data in PARTS-
CODE-IN matches a part code in an internal table.

An example of a valid part code in the table is 914C80. That is
to say, every part code contains three numbers, an uppercase
letter, and then two numbers, nnnXnn.

I would like to know if there is a Cobol command that will force
the caps lock key on, so that the user always enters an upper
case letter.

If not, and if the user enters a lower case letter, is there a
way to modify the ACCEPT command so that it converts any lower
case letter to upper case before it enters PART-CODE-IN?

Or, lastly, is there an easy way to convert nnnxnn to nnnXnn
(999a99 to 999A99) after the fact?

We are using the Rm-85 compiler (student edition) and the text
book by Stern and Stern titled "Structured Cobol Programming."

Thanks,


B.Yates
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "dt..." <ua-author-7376421@usenetarchives.gap>
- **Date:** 1996-11-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

bya··.@a··.com wrote:

› Hi, 
 
› I am  writing a program as homework in which the user enters a
› part code on the screen and then the ACCEPT command transfers the data
› into the working storage area, PARTS-CODE-IN PIC x(5).
 
› The program then searches a table to see if the data in PARTS-
› CODE-IN matches a part code in an internal table.
 
› An example of a  valid part code in the table is 914C80. That is
› to say, every part code contains three numbers, an uppercase
› letter, and then two numbers, nnnXnn.
 
› I would like to know if there is a Cobol command that will force
› the caps lock key on,  so that the user always enters an upper
› case letter.
 
› If not, and if the user enters a lower case letter, is there a
› way to modify the ACCEPT command so that it converts any lower
› case letter to upper case before it enters PART-CODE-IN?
 
› Or, lastly, is there an easy way to convert nnnxnn to nnnXnn
› (999a99 to 999A99) after the fact?
 
› We are using the Rm-85 compiler (student edition) and the text
› book by Stern and Stern titled "Structured Cobol Programming."
 
› Thanks,
 
 
› B.Yates

I'm not familiar with RM Cobol, so I don't know if it has any
uppercase functions like MF Cobol (CBL_TOUPPER). So, unless you
"grab" every key stroke the user enters and convert it 'on the fly',
the only way around this is to convert it after the data is entered.
You can do this several ways, some more efficient than others, but
heres one simple, down and dirty method.

Pseudo Code:

01 Ws-AlphaNumeric-Area.
03 Ws-Part-No.
05 filler Pic 999.
05 The-Letter Pic X.
05 filler Pic 99.


Display (10, 1) "Enter part number: ".
Accept Part-Number with prompt empty-check beep.
Move Part-Number to Ws-Part-No.
Perform Upper-Case.
Move Ws-Part-No to Part-Number.

.
.
.

Upper-Case.
Inspect The-Letter replacing all "a" by "A".
Inspect The-Letter replacing all "b" by "B".
Inspect The-Letter replacing all "c" by "C".


(and so on....)


This isn't the greatest, but it works, and it's fast. Hope that
helps.

D.
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1996-11-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

Check your manual for the exact syntax of INSPECT ... CONVERTING. Also
check the manual to see if you have the 1989 addition of FUNCTIONs such
as FUNCTION (upper-case). Both of these will do the job. If you are
using a screen handler or screen program front end that may do it for
you.
›  
› Hi,  
…[30 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at morrisc.nbnet.nb.ca
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "bbell..." <ua-author-1898047@usenetarchives.gap>
- **Date:** 1996-11-23T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

Yes, you can do an Inspect on the input entered, and then convert any
lower case letters to upper case. I am using MF personal cobol it also has
a function that can convert to upper case.
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "glenn a. mitchell" <ua-author-17072865@usenetarchives.gap>
- **Date:** 1996-11-25T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

bya··.@a··.com wrote:
›
 
› If not, and if the user enters a lower case letter, is there a
› way to modify the ACCEPT command so that it converts any lower
› case letter to upper case before it enters PART-CODE-IN?
›


Probably the easiest way (assuming your compiler supports it) is to use
the intrinsic function after the ACCEPT verb:

MOVE INTRINSIC UPPER-CASE(PART-CODE-IN) TO PART-CODE-IN.

Glenn A. Mitchell               mailto:mit··.@poa··c.org
Director, Computer Technology   http://www.mmc.org
Maine Medical Center            
Portland, ME  04101
```

##### ↳ ↳ Re: How convert 999x99 to 999X99?

- **From:** "dmv..." <ua-author-17072164@usenetarchives.gap>
- **Date:** 1996-11-25T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b26b418cca-p5@usenetarchives.gap>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com> <gap-b26b418cca-p5@usenetarchives.gap>`

```

You can use ACCEPT identifier FROM ...... WITH UPPER.

This is using Micro Focus. I'm not sure with other compilers.

Tony M. Mina




On Tue, 26 Nov 1996 08:45:08 -0800, "Glenn A. Mitchell"
wrote:

› bya··.@a··.com wrote:
›› 
…[16 more quoted lines elided]…
› Portland, ME  04101
```

##### ↳ ↳ Re: How convert 999x99 to 999X99?

- **From:** "stevenc" <ua-author-1500476@usenetarchives.gap>
- **Date:** 1996-12-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b26b418cca-p5@usenetarchives.gap>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com> <gap-b26b418cca-p5@usenetarchives.gap>`

```

Glenn A. Mitchell wrote:
› 
› bya··.@a··.com wrote:
…[11 more quoted lines elided]…
› MOVE INTRINSIC UPPER-CASE(PART-CODE-IN) TO PART-CODE-IN.


With all due respect, I think you mean:
MOVE FUNCTION UPPER-CASE(PART-CODE-IN) TO PART-CODE-IN.
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1996-11-25T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p8@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

bya··.@a··.com wrote in article
<199··.@lad··l.com>...
› I am  writing a program as homework in which the user enters a
› part code on the screen and then the ACCEPT command transfers the data
…[6 more quoted lines elided]…
› case letter to upper case before it enters PART-CODE-IN?

Yes, but it is nonstandard.

accept PARTS-CODE-IN control "UPPER"

› Or, lastly, is there an easy way to convert nnnxnn to nnnXnn
› (999a99 to 999A99) after the fact?

This is the better way, because it can rely on standard COBOL:

inspect PARTS-CODE-IN
converting "abcdefghijklmnopqrstuvwxyz"
to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

You might also consider the following:

if PARTS-CODE-IN(1:3) not numeric
or PARTS-CODE-IN(4:1) not alphabetic
or PARTS-CODE-IN(5:2) not numeric

end-if

› We are using the Rm-85 compiler (student edition) and the text
› book by Stern and Stern titled "Structured Cobol Programming."

A great COBOL!


Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-719-7019  FAX:512-719-7070
```

#### ↳ Re: How convert 999x99 to 999X99?

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-11-27T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p9@usenetarchives.gap>`
- **In-Reply-To:** `<19961123162100.LAA26073@ladder01.news.aol.com>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com>`

```

An old trick we mainframers use is:

01 WS-UPPER PIC X(25) VALUE 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
01 WS-LOWER PIC X(25) VALUE 'abcdefghijklmnopqrstuvwxyz'.

INSPECT WS-FIELD
CONVERTING WS-LOWER TO WS-UPPER.

If you don't have CONVERTING use:

INSPECT WS-FIELD
REPLACING ALL 'a' BY 'A'
'b' BY 'B'
'c' BY 'C'
...
...
...
'z' BY 'Z'.

Or if you have COBOL/390:

MOVE FUNCTION UPPER-CASE(WS-FIELD) TO WS-NEW-FIELD.
MOVE WS-NEW-FIELD TO WS-FIELD.

Good luck

Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

##### ↳ ↳ Re: How convert 999x99 to 999X99?

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-12-01T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b26b418cca-p9@usenetarchives.gap>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com> <gap-b26b418cca-p9@usenetarchives.gap>`

```

› Return-path: 
› Date: Fri, 29 Nov 1996 14:57:53 -0500
…[11 more quoted lines elided]…
› factor to add.

True, but most flavors of COBOL won't let oneself manipulate
characters at the hex level.

Just my 1.5 cents worth, adjusted for inflation
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

##### ↳ ↳ Re: How convert 999x99 to 999X99?

- **From:** "freddie schwenke" <ua-author-13484813@usenetarchives.gap>
- **Date:** 1996-12-03T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b26b418cca-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b26b418cca-p9@usenetarchives.gap>`
- **References:** `<19961123162100.LAA26073@ladder01.news.aol.com> <gap-b26b418cca-p9@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
› An old trick we mainframers use is:
…[33 more quoted lines elided]…
›  '---------------------------------------------------------------------'
I like this method and it is available in RM-85.

Freddie
:)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
