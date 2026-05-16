[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Apostrophes and quotation marks

_4 messages · 4 participants · 1994-12_

---

### Apostrophes and quotation marks

- **From:** walterm@hprctbs3.rose.hp.com (Walter Murray)
- **Date:** 1994-12-01T18:41:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bl5da$slk@hpchase.rose.hp.com>`

```
I'm curious whether someone who's "in the know" can explain the
background on apostrophes and quotation marks in COBOL.

The rules in the COBOL standard are very simple.

     1.  Quotation marks are used to delimit nonnumeric literals:

	      "This is a test"

     2.  If you want to embed a quotation mark in a nonnumeric
	 literal, you use two consecutive quotation marks:

	      "This is a quotation "" mark"

     3.  An apostrophe is just like any other character and requires
	 no special treatment:

	      "They say it's easy"

But a lot of people seem to use apostrophes instead of quotation marks
to delimit nonnumeric literals, so many compilers must permit that.
And some compilers have an option to make the figurative constant QUOTE
be an apostrophe instead of a quotation mark.  

Is this something that was different in the early days of COBOL?  Is
this an IBM thing?  In what COBOL environments today is it common to
use apostrophes in place of quotation marks for nonnumeric literals?

Just looking to broaden my horizons and get the historical perspective.

Walter
```

#### ↳ Re: Apostrophes and quotation marks

- **From:** malexand@wimsey.com (Murray Alexander)
- **Date:** 1994-12-02T00:42:29
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<malexand.56.0000B4F0@wimsey.com>`
- **References:** `<3bl5da$slk@hpchase.rose.hp.com>`

```
In article <3bl5da$slk@hpchase.rose.hp.com> walterm@hprctbs3.rose.hp.com (Walter Murray) writes:
>From: walterm@hprctbs3.rose.hp.com (Walter Murray)
>Subject: Apostrophes and quotation marks
>Date: 1 Dec 1994 18:41:46 GMT

>I'm curious whether someone who's "in the know" can explain the
>background on apostrophes and quotation marks in COBOL.

>The rules in the COBOL standard are very simple.
<snip>
>But a lot of people seem to use apostrophes instead of quotation marks
>to delimit nonnumeric literals, so many compilers must permit that.
>And some compilers have an option to make the figurative constant QUOTE
>be an apostrophe instead of a quotation mark.  

>Is this something that was different in the early days of COBOL?  Is
>this an IBM thing?  In what COBOL environments today is it common to
>use apostrophes in place of quotation marks for nonnumeric literals?

>Just looking to broaden my horizons and get the historical perspective.

>Walter

Someone in another thread suggested that apostrophes were an option because 
they were easier to type (huh?); no need to burden programmers with the need 
to press that awkward Shift key. Hmm...perhaps the compiler development team 
consulted the keyboard design group?

It's at least partly an IBM thing. My shop had to switch from quotes to 
apostrophes when we converted to IBM and started using an IBM product which 
demanded the APOST option.


Murray Alexander
City of Vancouver

"Do it right, or do it over. Which do you prefer?" - me
```

#### ↳ Re: Apostrophes and quotation marks

- **From:** wcivy@adpc.purdue.edu
- **Date:** 1994-12-02T08:29:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bnb5p$7g5@mozo.cc.purdue.edu>`
- **References:** `<3bl5da$slk@hpchase.rose.hp.com>`

```

In article <3bl5da$slk@hpchase.rose.hp.com>, <walterm@hprctbs3.rose.hp.com> 
writes:
> 
> I'm curious whether someone who's "in the know" can explain the
…[4 more quoted lines elided]…
> use apostrophes in place of quotation marks for nonnumeric literals?

It might be an IBM thing.  I don't know whether my experience counts for the 
"early days of COBOL", but I started just about 25 years ago programming in 
COBOL in our office at Purdue (then Administrative Data Processing Center).  
The default to delimit non-numeric literals has always been the single quote or 
apostrophe mark.  This can be changed as an option when you run the compiler.  
The default is set by the people who install the compiler.  Based on our 
typical practice to use IBM defaults (except where we have specific different 
needs), I would expect that this is the default.

I tried to remember if there was any reasons given for this, but I can't think 
of any.  I even checked with another long-term person in the office, but he 
couldn't think of why, either.
```

#### ↳ Re: Apostrophes and quotation marks

- **From:** ejs@enzosiri.demon.co.uk (Enzo J Siri)
- **Date:** 1994-12-02T23:16:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<786410196snz@enzosiri.demon.co.uk>`
- **References:** `<3bl5da$slk@hpchase.rose.hp.com>`

```
In article <3bl5da$slk@hpchase.rose.hp.com>
           walterm@hprctbs3.rose.hp.com "Walter Murray" writes:
> 
> But a lot of people seem to use apostrophes instead of quotation marks
> to delimit nonnumeric literals, so many compilers must permit that.
> And some compilers have an option to make the figurative constant QUOTE
> be an apostrophe instead of a quotation mark.  

And the IBM mainframe compiler (COBOL II for MVS) has an option to make
the string delimiter a quote or apostrophe. And it depends on the 
place: in some companies people use quotes and in others they use
apostrophes.
> 
> Is this something that was different in the early days of COBOL?  Is
> this an IBM thing?  In what COBOL environments today is it common to
> use apostrophes in place of quotation marks for nonnumeric literals?

In Assembler 370 the literals are always delimited by apostrophes, what
makes me think that the same must have been true for the early versions
of COBOL. Why they were changed to quotes later, remains a mystery to me.

The COBOL compiler allows both options for "backwards compatibility"
reasons.

Enzo------------------------------------------------------------------
              And everything under the sun is in tune
              but the sun is eclipsed by the moon.
Siri------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
