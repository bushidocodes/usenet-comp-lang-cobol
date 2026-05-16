[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The next Date Issue

_10 messages · 7 participants · 2000-01_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Re: The next Date Issue

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<38734F19.A8324565@istar.ca>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk>`

```
Unfortunately COBOL provides no easy way of editing a numeric field to
yyyy-mm-dd because the hyphen is a sign character whereas you can code
9999/99/99 or XXXX/XX/XX as a valid PICTURE.  Given the rationale for
the use of hyphens in the date formatting, I would like to see someone
address the issue for all programming languages but have not seen even
a ripple of interest on various news groups.  I don't know what the
situation is for other languages.  I believe that VISION (DYL280) from
Sterling has the same problem.  Unfortunately standards groups act in
isolation.

Clark Morris, CFM Technical Programming Services, cfmtech@istar.ca

Dr John Stockton wrote:
> 
> JRS:  In article <8EB0A04BEcraznarhotmailcom@139.130.250.4> of Mon, 3
…[25 more quoted lines elided]…
>  Y2k for beginners - year2000.txt  UK mini-FAQ - y2k-mfaq.txt  Don't Mail News
```

#### ↳ Re: The next Date Issue

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<38737EDB.BF1151@home.com>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca>`

```


Clark Morris wrote:
> 
> > >Time to standardise on yyyy/mm/dd before next years date mix up problems.
…[3 more quoted lines elided]…
> > ï¿½ John Stockton, Surrey, UK.  jrs@merlyn.demon.co.uk   Turnpike v4.00   MIME. ï¿½

Your fear is well-founded. I can only make a wild-guess that if the
analyst/programmer was Canadian-born then he uses "M D Y", a la US ;
possibly if he is an ex-Brit he will use "D M Y". Both formats appear on
bills I receive. But there is a neat feature on my telephone bill :-

						  $
	Tue Jan  4 ...........			1.67
	Wed Jan 12 ...........			2.12

the year being understood from the current billing.

The simplest solution to both date and time has to be a standarisation
on the ISO ccyymmdd (the most logical way for date storage for ascending
sequence) and the 24 hour clock. For many years I have written my
personal cheques :-

		99 Jan 23,  now of course - 2000 Jan 23

Jimmy, Calgary AB
```

##### ↳ ↳ Re: The next Date Issue

- **From:** Dr John Stockton <jrs@merlyn.demon.co.uk>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<f27bhEM3u8c4Ew5$@merlyn.demon.co.uk>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com>`

```
JRS:  In article <38737EDB.BF1151@home.com> of Wed, 5 Jan 2000 17:31:23
in news:comp.software.year-2000, James J. Gavan <jjgavan@home.com>
wrote:
>
>The simplest solution to both date and time has to be a standarisation
>on the ISO ccyymmdd (the most logical way for date storage for ascending
>sequence) and the 24 hour clock. For many years I have written my
>personal cheques :-

Except that the ISO standard is yyyymmdd, with the separator, of any,
being "-".

I have seen it reported (comp.risks?) that a request, much more than a
week ago, for CCYY or CC YY data led to the entry of the true value of
the century for CC - 20, where 19 was then needed.  Possibly in the
Texas Highways Department?????

I have also seen a normally-reputable programmer, given a string
containing cYY, where the single digit c is actually (YYYY div 100)-19,
treating c & YY separately in recovering YYYY.

Using CC in the notation, i.e. CCYY rather than YYYY, introduces an
unnecessary hazard.
```

###### ↳ ↳ ↳ Re: The next Date Issue

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<3874A74D.AECD1589@iinet.net.au>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com> <f27bhEM3u8c4Ew5$@merlyn.demon.co.uk>`

```

Dr John Stockton wrote:
> 
> JRS:  In article <38737EDB.BF1151@home.com> of Wed, 5 Jan 2000 17:31:23
…[10 more quoted lines elided]…
> 
Ok Ok,
Lets' fix this date thing once and for all.

01  Internal-Date-Representation.
    03 Year     PIC S9(9) comp.
    03 Month    PIC S9(4) comp.
    03 Day      PIC S9(4) comp.

External date representation is whatever you need for the job at hand.
However, the YEAR should have at least 4 digits as a minimum
requirement.
```

###### ↳ ↳ ↳ Re: The next Date Issue

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<3873F433.E22C8EC2@home.com>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com> <f27bhEM3u8c4Ew5$@merlyn.demon.co.uk>`

```


Dr John Stockton wrote:
> 
> JRS:  In article <38737EDB.BF1151@home.com> of Wed, 5 Jan 2000 17:31:23
…[22 more quoted lines elided]…
> 

Ah ah ! Somebody from the good olde stock-broker belt, or are you at U.
of Guildford ? My ccymmdd was unintentional, I really meant 'yyyymmdd'

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: The next Date Issue

- **From:** "Gary L. Smith" <gls@infinet.com>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<38741ecc$0$50322@news.voyager.net>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com> <f27bhEM3u8c4Ew5$@merlyn.demon.co.uk>`

```
In comp.software.year-2000 Dr John Stockton <jrs@merlyn.demon.co.uk> wrote:

: I have seen it reported (comp.risks?) that a request, much more than a
: week ago, for CCYY or CC YY data led to the entry of the true value of
: the century for CC - 20, where 19 was then needed.  Possibly in the
: Texas Highways Department?????

One case of stupidity isn't sufficient to invalidate an otherwise
reasonable practice.

: I have also seen a normally-reputable programmer, given a string
: containing cYY, where the single digit c is actually (YYYY div 100)-19,
: treating c & YY separately in recovering YYYY.

: Using CC in the notation, i.e. CCYY rather than YYYY, introduces an
: unnecessary hazard.

But what would you do when it's necessary to refer to the two high-order
digits in isolation?  Is there a symbol that's preferable to "cc"?  A
real-life example of such a situation, excepted from a remediation
document dated 19980130:  

Here YYMMDD represents a six-digit date as found in Date Entered, while CC
is the value of the century digits.  Concatenating CC with YYMMDD produces
the full eight-digit date.

Algorithm:

If YYMMDD = 000000, then CC = 00
Else if YY is less than 60, then CC = 20
Else CC = 19.

Examples:

000000  becomes  00000000
980122  becomes  19980122
000102  becomes  20000102
591231  becomes  20591231
600101  becomes  19600101
```

###### ↳ ↳ ↳ Re: The next Date Issue

_(reply depth: 4)_

- **From:** Dr John Stockton <jrs@merlyn.demon.co.uk>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<ogF2EnMJRKd4Ew3n@merlyn.demon.co.uk>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com> <f27bhEM3u8c4Ew5$@merlyn.demon.co.uk> <38741ecc$0$50322@news.voyager.net>`

```
JRS:  In article <38741ecc$0$50322@news.voyager.net> of Thu, 6 Jan 2000
04:49:16 in news:comp.software.year-2000, Gary L. Smith
<gls@infinet.com> wrote:
>In comp.software.year-2000 Dr John Stockton <jrs@merlyn.demon.co.uk> wrote:
>
…[6 more quoted lines elided]…
>reasonable practice.

But one example is sufficient to cast doubt on the practice, and the
practice can be avoided without difficulty.  Can one safely assume that
the THD (or whoever) are uniquely stupid?

>: I have also seen a normally-reputable programmer, given a string
>: containing cYY, where the single digit c is actually (YYYY div 100)-19,
…[12 more quoted lines elided]…
>the full eight-digit date.

"Here YYMMDD represents a six-digit date as found in Date Entered, while
 YYYYMMDD represents a full eight-digit date."

(* The relationship is obvious. *)

>Algorithm:
>
>If YYMMDD = 000000, then CC = 00
>Else if YY is less than 60, then CC = 20
>Else CC = 19.

>If YYMMDD = 000000, then YYYY = 0000
>Else if YY is less than 60, then YYYY = 2000
>Else YYYY = 1900.

/Entia non sunt multiplicanda praeter necessitatem/.

CC of course has two problems, one nullifying the other nearly 1% of the
time : the customary century number is almost always different from Year
div 100.
```

###### ↳ ↳ ↳ Re: The next Date Issue

_(reply depth: 5)_

- **From:** "Gary L. Smith" <gls@infinet.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<38775fbb$0$1808@news.voyager.net>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <38737EDB.BF1151@home.com> <f27bhEM3u8c4Ew5$@merlyn.demon.co.uk> <38741ecc$0$50322@news.voyager.net> <ogF2EnMJRKd4Ew3n@merlyn.demon.co.uk>`

```
In comp.software.year-2000 Dr John Stockton <jrs@merlyn.demon.co.uk> wrote:
: JRS:  In article <38741ecc$0$50322@news.voyager.net> of Thu, 6 Jan 2000
: 04:49:16 in news:comp.software.year-2000, Gary L. Smith
: <gls@infinet.com> wrote:
:>In comp.software.year-2000 Dr John Stockton <jrs@merlyn.demon.co.uk> wrote:
:>
:>: I have seen it reported (comp.risks?) that a request, much more than a
:>: week ago, for CCYY or CC YY data led to the entry of the true value of
:>: the century for CC - 20, where 19 was then needed.  Possibly in the
:>: Texas Highways Department?????
:>
:>One case of stupidity isn't sufficient to invalidate an otherwise
:>reasonable practice.

: But one example is sufficient to cast doubt on the practice, and the
: practice can be avoided without difficulty.  Can one safely assume that
: the THD (or whoever) are uniquely stupid?

I would never say anything bad about Texans (some of my relatives are
Texans) or about highway patrolmen (some of my ...), but I believe that
this particular episode, if it occurred at all, was uniquely stupid.
There's a big difference between using CC to designate the high-order
digits of the year and referring to those digits as "the century".  Tha
latter is definitely a bad move, although there seem to be very few people
these days who understand the terms "19th century" and "20th century". 

:>But what would you do when it's necessary to refer to the two high-order
:>digits in isolation?  Is there a symbol that's preferable to "cc"?  A
:>real-life example of such a situation, excepted from a remediation
:>document dated 19980130:  
:>
:>Here YYMMDD represents a six-digit date as found in Date Entered, while CC
:>is the value of the century digits.  Concatenating CC with YYMMDD produces
:>the full eight-digit date.

: "Here YYMMDD represents a six-digit date as found in Date Entered, while
:  YYYYMMDD represents a full eight-digit date."

: (* The relationship is obvious. *)

:>Algorithm:
:>
:>If YYMMDD = 000000, then CC = 00
:>Else if YY is less than 60, then CC = 20
:>Else CC = 19.

:>If YYMMDD = 000000, then YYYY = 0000
:>Else if YY is less than 60, then YYYY = 2000
:>Else YYYY = 1900.

I find my formulation easier to understand, but I suspect this is
primarily a matter od taste.  No doubt either would suffice almost all the
time.  Those who misunderstand either and fail to ask for clarification
shouldn't be allowed to write code.
```

#### ↳ Re: The next Date Issue

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<I2Mc4.69$Rw3.1460029@news.netdirect.net>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca>`

```
In article <38734F19.A8324565@istar.ca>, Clark Morris <cfmtech@istar.ca> wrote:
>Unfortunately COBOL provides no easy way of editing a numeric field to
>yyyy-mm-dd because the hyphen is a sign character whereas you can code
>9999/99/99 or XXXX/XX/XX as a valid PICTURE.

01 EDITED-DATE    PIC 9999B99B99.
01 NORMAL-DATE   PIC 9(8).
..
MOVE NORMAL-DATE TO EDITED-DATE
INSPECT EDITED-DATE REPLACING ALL " " BY "-"
```

##### ↳ ↳ Re: The next Date Issue

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<8509hc$uk0$1@nntp4.atl.mindspring.net>`
- **References:** `<8EB0A04BEcraznarhotmailcom@139.130.250.4> <bI66+sHyQQc4Ew6Q@merlyn.demon.co.uk> <38734F19.A8324565@istar.ca> <I2Mc4.69$Rw3.1460029@news.netdirect.net>`

```
Ask your  COBOL "vendor of choice" if they already (or soon) support the new
intrinsic functions (from the draft revision)

    LOCALE-DATE
    LOCALE-TIME

These will "format" the date or time portions of FUNCTION CURRENT-DATE
*either* to the default locale specification - or a "specified" LOCALE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
