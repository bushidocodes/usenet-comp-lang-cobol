[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Glade - Have you experience

_30 messages · 8 participants · 2016-01 → 2016-05_

---

### Glade - Have you experience

- **From:** "delta11nopsam" <ua-author-14501788@usenetarchives.gap>
- **Date:** 2016-01-27T03:47:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n8a02l$p1h$1@dont-email.me>`

```
How to display a GUI glade-3(xml) form and programming events?
Everyone have experience?
```

#### ↳ Re: Glade - Have you experience

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-01-27T12:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<n8a02l$p1h$1@dont-email.me>`
- **References:** `<n8a02l$p1h$1@dont-email.me>`

```
In article ,
Delta11 wrote:
› How to display a GUI glade-3(xml) form and programming events?
› Everyone have experience?

ACCEPT GLADE-3 FROM CONSOLE.
PERFORM S4376-MANIPULATE-GLADE-DATA THRU S4376-EX
VARYING GLADE-SUB FROM DATA-START TO DATA-END
UNTIL INVALID-GLADE OR NO-MORE-GLADE.
IF NOT INVALID-GLADE
DISPLAY FORMATTED-GLADE ON CONSOLE.

What else might be needed?

DD
```

##### ↳ ↳ Re: Glade - Have you experience

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-27T20:38:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p2@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Delta11   wrote:
…[10 more quoted lines elided]…
› What else might be needed?

Syntax that complies with COBOL-85? :-) (Check DISPLAY...)

Don't look at me... I thought Glade was for polishing coffee tables.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2016-01-27T20:45:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p3@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap>`

```
On Thu, 28 Jan 2016 14:38:33 +1300, "Pete Dashwood"
wrote:

› doc··f@pa··x.com wrote:
›› In article ,
…[16 more quoted lines elided]…
› 

Glade, IIRC, is an air freshener. You might be thinking of Pledge.

Louis
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-28T17:18:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p4@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p4@usenetarchives.gap>`

```
Louis Krupp wrote:
› On Thu, 28 Jan 2016 14:38:33 +1300, "Pete Dashwood"
›  wrote:
…[21 more quoted lines elided]…
› Glade, IIRC, is an air freshener.  You might be thinking of Pledge.

My housekeeper confirms you are correct, Louis.

Not my area of expertise so hardly surprising I was wrong about it :-)

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-01-28T08:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p3@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[13 more quoted lines elided]…
› Syntax that complies with COBOL-85? :-) (Check DISPLAY...)

Answering a question with a question, Mr Dashwood, is no answer at all...
the code posted appears to meet or exceed all requirements given.

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-28T17:21:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p6@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[18 more quoted lines elided]…
› all...
 
› And responding with another tired old cliche is no answer either....
 
 
› the code posted appears to meet or exceed all requirements
› given.

No, it doesn't. The requirement was for COBOL-85 syntax and that requires
UPON with DISPLAY

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-01-29T09:20:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p7@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[21 more quoted lines elided]…
› And responding with another tired old cliche is no answer either....
 
› That may be a reason for some folks not doing it.
 
›› the code posted appears to meet or exceed all requirements
›› given.
› 
› No, it doesn't. The requirement was for COBOL-85 syntax and that requires 
› UPON with DISPLAY

Re-read the specs, Mr Dashwood, and post a link that supports your
assertion.

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-02-01T18:46:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p8@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[34 more quoted lines elided]…
› assertion.

Fair enough. I thought he needed COBOL-85 and was wrong about that.

However, the assertion that "the code posted appears to meet or exceed all
requirements" is still incorrect.

Please quote a version of COBOL that allows "DISPLAY... ON".

I can't find one..

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 7)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-01T22:02:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p9@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap>`

```
On Monday, February 1, 2016 at 6:46:03 PM UTC-5, Pete Dashwood wrote:



› Please quote a version of COBOL that allows "DISPLAY... ON".

Thinking like a programmer, I see. This particular sequence is
allowed in OS/VS. The compiler would accept the DISPLAY statement,
followed by ON, but report a different problem.

-----
10 DISPLAY A ON CONSOLE.
* 13-S************************
** User-name required
-----

That is, "CONSOLE" cannot be used with an ON statement.

(I actually used Micro Focus with OS/VS syntax checking.)
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 7)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-02T08:54:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p9@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[44 more quoted lines elided]…
› I can't find one..

That's an excellent place to begin, Mr Dashwood... would that the original
poster would have gone so far! Where did you look?

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 8)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-02-06T16:02:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p11@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[50 more quoted lines elided]…
› original poster would have gone so far!  Where did you look?

The question was: 'Please quote a version of COBOL that allows "DISPLAY...
ON".'

Oddly enough there are people who believe that answering a question with a
question is no answer at all.

It is reasonable to infer from your attempted deflection that you are unable
to provide such a version of COBOL.

A gentleman might admit to being in error.

(But there probably are few gentlemen who frequent Usenet...)

Pete.

Pete.

›
› DD

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 9)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-06T21:22:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p12@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap> <gap-2eafecfbb2-p12@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[54 more quoted lines elided]…
› ON".'

It is easy enough to run into folks who can't read their own handwriting,
a bit more rare to find those who can't read their own typing. The
request to '(p)lease quote a version of COBOL that allows "DISPLAY...
ON""' does not appear to be interrogative.

›
› Oddly enough there are people who believe that answering a question with a
› question is no answer at all.

Their beliefs coincide with mine, Mr Dashwood... and it would appear that
you are of a different creed, no shame in that.

Duplication of effort is to be avoided, hence my query. Is that so
unreasonable?

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 8)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-07T23:14:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p11@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap>`

```
On Tuesday, February 2, 2016 at 8:54:46 AM UTC-5, doc··.@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[49 more quoted lines elided]…
› poster would have gone so far!  Where did you look?

Mr Dwarf, your question reminded me of Popper's falsification,
which I will express as "No number of observations can prove
that 'DISPLAY ... UPON ...' is the only permissible phrasing, but
one verified observation of 'DISPLAY ... ON ...', as permissible,
will falsify it.

So I headed to the bitsavers archive at
< https://archive.org/details/bitsavers >, searched for COBOL
and found 219 documents, some of which are LRMs for several
implementations, including Burroughs, Univac, Control Data,
Honeywell, dec, Wang VS, etc., as well as IBM.

All used "DISPLAY ... UPON ..." with the exception of Wang VS
which omitted the UPON phrase completely. Also, it appeared
that UPON CONSOLE was distinctively used by IBM, others having
used a different device name.

In the COBOL language specifications, including the COBOL 60
Report and the standards for 1968, 1974, 1985, 2002, and 2014,
"DISPLAY ... [ UPON ... ]" is the syntax given. Furthermore, there
are rules for conformance, which involve "Acceptance of standard
language elements" [2002] and prohibitions against "Substitute or
additional language elements" [2002]. [Though 2002 is quite different
from earlier standards, I understand similar rules applied, for
reasons of portability.]

Therefore, a conforming implementation must accept "DISPLAY ...
UPON ..." and must not substitute "DISPLAY ... ON ..." to
accomplish the same effect. However, an implementation may allow,
as an extension, ON as an alternative to UPON. Of course, the only
"unseemly" reason for doing so would be to save two keystrokes.

The "bottom line" is that there is no evidence and no reason to
believe that there exists an implementation that recognizes
"DISPLAY ... ON ..."; which would be necessary to "falsify" what
I have observed to be true.
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 9)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-10T07:45:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p14@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap> <gap-2eafecfbb2-p14@usenetarchives.gap>`

```
In article <9e0adec7-f692-4c14-9bc3-a85··5@goo··s.com>,
Rick Smith wrote:
› On Tuesday, February 2, 2016 at 8:54:46 AM UTC-5, doc··.@pa··x.com wrote:
›› In article ,
…[50 more quoted lines elided]…
›› poster would have gone so far!  Where did you look?
 
› [snip]
 
› So I headed to the bitsavers archive at
› < https://archive.org/details/bitsavers  ...

Nicely done, Mr Smith... it might benefit others to demonstrate such
diligence.

Mr Dashwood might be a bit miffed due to my treating him as I treat...
well, just about anyone else; whether the greenest of newbies or the
hoariest of greybeards it is my wont to respond to 'I can't find it
anywhere!' with 'Where did you look?'

As mentioned, it prevents duplication of effort... it also assists in
assuring that folks Do Their Own Homework.

Differences such as UPON and ON, PERFORM and PERFROM, AND and ALSO...
these are reasons for compiling code before posting it. I'm not in the
habit of doing so and, at times, will generate an 8 or greater.

My error and apologies... thanks much!

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 10)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-10T09:39:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p15@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap> <gap-2eafecfbb2-p14@usenetarchives.gap> <gap-2eafecfbb2-p15@usenetarchives.gap>`

```
On Wednesday, February 10, 2016 at 7:45:29 AM UTC-5, doc··.@pa··x.com wrote:
› In article <9e0adec7-f692-4c14-9bc3-a85··5@goo··s.com>,
› Rick Smith   wrote:
…[74 more quoted lines elided]…
› My error and apologies... thanks much!

You are most welcome and such a gentlemanly acknowledgement!
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 10)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-02-10T18:47:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p15@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap> <gap-2eafecfbb2-p14@usenetarchives.gap> <gap-2eafecfbb2-p15@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article <9e0adec7-f692-4c14-9bc3-a85··5@goo··s.com>,
› Rick Smith   wrote:
…[67 more quoted lines elided]…
› anywhere!' with 'Where did you look?'

Understood. I am not and was not miffed by that. I WAS disappointed you
refused to admit that your sweeping "the code posted appears to meet or
exceed all requirements
given." is, in fact, not true because it can't be run, as written, on any
standard-compliant implementation of COBOL.

(As Rick observed, when posting to this forum I do sometimes think like a
programmer... usually when actual code is involved. I make no apology for
that.)


› 
› As mentioned, it prevents duplication of effort... it also assists in
…[4 more quoted lines elided]…
› the habit of doing so and, at times, will generate an 8 or greater.

Posting code to CLC is ALWAYS a risk and it is right that it should be so.
Compiling and running it BEFORE doing so is probably the only way to be sure
you are giving correct information.
›
› My error and apologies... thanks much!

An apology for a typing error is not an apology for a sweeping statement
that was wrong, but it would be churlish to pursue it, so I won't.

Thank you for your post.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 11)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-11T08:50:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p17@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p6@usenetarchives.gap> <gap-2eafecfbb2-p7@usenetarchives.gap> <gap-2eafecfbb2-p8@usenetarchives.gap> <gap-2eafecfbb2-p9@usenetarchives.gap> <gap-2eafecfbb2-p11@usenetarchives.gap> <gap-2eafecfbb2-p14@usenetarchives.gap> <gap-2eafecfbb2-p15@usenetarchives.gap> <gap-2eafecfbb2-p17@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:

[snip]

› Understood. I am not and was not miffed by that. I WAS disappointed you 
› refused to admit that your sweeping "the code posted appears to meet or 
› exceed all requirements
› given." is, in fact, not true because it can't be run, as written, on any 
› standard-compliant implementation of COBOL.

Mr Dashwood, it seems that we may be using the language differently. In
the abovequoted it was my intent for 'appears' to be read in the sense of
'to have the appearance of being'
(http://dictionary.reference.com/browse/appear?s=t , 2) where 'appearance'
is used according to http://dictionary.reference.com/browse/appearance 3,
'outward show or seeming, semblance'.

In short, it was a reference to something which can be deceiving... wasn't
that the moral of a fable attrib uted to Aesop?

('The Wolf in Sheep's Clothing'... but I am only a dolt in cheap clothing)

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-04T11:57:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p3@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap>`

```
On Wednesday, January 27, 2016 at 8:38:38 PM UTC-5, Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[7 more quoted lines elided]…
››  UNTIL INVALID-GLADE OR NO-MORE-GLADE.
 
››     REPLACE ==ON== BY ==UPON==.
 
›› IF NOT INVALID-GLADE
››    DISPLAY FORMATTED-GLADE ON CONSOLE.
 
››     REPLACE OFF.
 
›› What else might be needed?
› 
› Syntax that complies with COBOL-85? :-) (Check DISPLAY...)

Now it conforms to COBOL 85.
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-02-06T15:57:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p19@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p19@usenetarchives.gap>`

```
Rick Smith wrote:
› On Wednesday, January 27, 2016 at 8:38:38 PM UTC-5, Pete Dashwood
› wrote:
…[22 more quoted lines elided]…
› Now it conforms to COBOL 85. 

Thanks, Rick.

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 4)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-11T11:20:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p19@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p19@usenetarchives.gap>`

```
On Thursday, February 4, 2016 at 11:57:58 AM UTC-5, Rick Smith wrote:
› On Wednesday, January 27, 2016 at 8:38:38 PM UTC-5, Pete Dashwood wrote:
›› doc··f@pa··x.com wrote:
…[21 more quoted lines elided]…
› Now it conforms to COBOL 85. 

It appears I misspoke. No conforming COBOL 85 implementation
would accept, from the above:

VARYING GLADE-SUB FROM DATA-START TO DATA-END
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-11T14:43:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p21@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p19@usenetarchives.gap> <gap-2eafecfbb2-p21@usenetarchives.gap>`

```
In article <70cd7709-8f25-4867-bc8b-5d2··e@goo··s.com>,
Rick Smith wrote:
› On Thursday, February 4, 2016 at 11:57:58 AM UTC-5, Rick Smith wrote:
›› On Wednesday, January 27, 2016 at 8:38:38 PM UTC-5, Pete Dashwood wrote:
…[27 more quoted lines elided]…
›    VARYING GLADE-SUB FROM DATA-START TO DATA-END

01 GLADE-SUB PIC 9(2) VALUE ZEROES.
01 DATA-START PIC 9(2) VALUE ZEROES.
01 DATA-END PIC 9(2) VALUE ZEROES.

(somewhere else in the code)

EVALUATE DAY-OF-RUN
WHEN IT-IS-MONDAY
MOVE 1 TO DATA-START
MOVE 7 TO DATA-END
WHEN IT-IS-TUESDAY
MOVE 2 TO DATA-START
MOVE 6 TO DATA-END
...
WHEN OTHER
GO TO Z9999-BLOW-UP
END-EVALUATE

... etc.

This doesn't work in a COBOL 85 implementation?

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2016-02-11T16:54:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p22@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p19@usenetarchives.gap> <gap-2eafecfbb2-p21@usenetarchives.gap> <gap-2eafecfbb2-p22@usenetarchives.gap>`

```
On Thursday, February 11, 2016 at 2:43:45 PM UTC-5, doc··.@pa··x.com wrote:
› In article <70cd7709-8f25-4867-bc8b-5d2··e@goo··s.com>,
› Rick Smith   wrote:
…[51 more quoted lines elided]…
› This doesn't work in a COBOL 85 implementation?

No, it needs FROM ... BY ...
instead of FROM ... TO ...
As in:

PERFORM ...
VARYING GLADE-SUB FROM DATA-START BY 1
UNTIL GLADE-SUB > DATA-END OR ....

While I had glanced over the code, I only concentrated
on the DISPLAY statement, because that it what Mr Dashwood
had mentioned. It 'appears' so natural, I was deceived
until I took a closer look.
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

_(reply depth: 7)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-02-14T11:12:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p23@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p3@usenetarchives.gap> <gap-2eafecfbb2-p19@usenetarchives.gap> <gap-2eafecfbb2-p21@usenetarchives.gap> <gap-2eafecfbb2-p22@usenetarchives.gap> <gap-2eafecfbb2-p23@usenetarchives.gap>`

```
In article <73d7db25-b540-409a-a2e2-e5d··7@goo··s.com>,
Rick Smith wrote:
› On Thursday, February 11, 2016 at 2:43:45 PM UTC-5, doc··.@pa··x.com wrote:
›› In article <70cd7709-8f25-4867-bc8b-5d2··e@goo··s.com>,
…[65 more quoted lines elided]…
› until I took a closer look.

Quite right, Mr Smith. Permit me to glance down and see if I remember to
zip my... oh dear.

DD
```

##### ↳ ↳ Re: Glade - Have you experience

- **From:** "chottel" <ua-author-3267354@usenetarchives.gap>
- **Date:** 2016-01-28T01:27:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p2@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap>`

```

wrote in message news:n8aur3$4to$1··@rea··...
› In article ,
› Delta11   wrote:
…[12 more quoted lines elided]…
› DD

why not

PERFORM 9999-SOLVE-ANY-PROBLEM THRU 9999-EXIT

? otherwise known as please do your own homework.
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-01-28T08:35:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p25@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p25@usenetarchives.gap>`

```
In article ,
Charles Hottel wrote:
› 
›  wrote in message news:n8aur3$4to$1··@rea··...
…[20 more quoted lines elided]…
› ?

Standards and Practises will reject any code where an ACCEPT of data is
not followed by a PERFORM directing execution to a paragraph whose label
begins with S, Mr Hottel... some folks forget so easily.

(memories of Prod Reviews of the Oldene Dayse...

'Why'd'ja do it *that* way.. why'n'cha do it *this* way?'

'I did it that way because it works.'

'Yeah, sure, it works... but why'n'cha do it *this* way?')

DD
```

###### ↳ ↳ ↳ Re: Glade - Have you experience

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-28T17:26:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2eafecfbb2-p25@usenetarchives.gap>`
- **References:** `<n8a02l$p1h$1@dont-email.me> <gap-2eafecfbb2-p2@usenetarchives.gap> <gap-2eafecfbb2-p25@usenetarchives.gap>`

```
Charles Hottel wrote:
›  wrote in message
› news:n8aur3$4to$1··@rea··...
…[20 more quoted lines elided]…
› ? otherwise known as please do your own homework.

Absolutely.

I'd do it as: PERFORM DUZ-THE-LOT (where it would be: DUZ-THE-LOT SECTION.)

Both of these are equally useless in helping someone who has requested help.

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Glade - Have you experience

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-27T20:16:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p28@usenetarchives.gap>`
- **In-Reply-To:** `<n8a02l$p1h$1@dont-email.me>`
- **References:** `<n8a02l$p1h$1@dont-email.me>`

```
Delta11 wrote:
› How to display a GUI glade-3(xml) form and programming events?
› Everyone have experience?

Do you wish to display the XML, or the form which the XML describes?

If you are moving into Gnome programming in COBOL, you should consider using
GNU COBOL...

I think Brian may have mentioned using Gnome/Gtk with it some time back.

Pete.

"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Glade - Have you experience

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2016-01-27T23:41:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p29@usenetarchives.gap>`
- **In-Reply-To:** `<n8a02l$p1h$1@dont-email.me>`
- **References:** `<n8a02l$p1h$1@dont-email.me>`

```
On Wednesday, January 27, 2016 at 9:48:00 PM UTC+13, Delta11 wrote:
› How to display a GUI glade-3(xml) form and programming events?
› Everyone have experience?

It is really easy with Python. It is only necessary to provide methods with the same name as the signal names created in the Glade designer. The glade support module automatically links the signals to the methods.

I did a system, a few years ago that ran unchanged on Windows, Linux and Nokia N800 tablet.

To do it in COBOL read a C language tutorial for Glade and do it that way in GNUCobol.
```

#### ↳ Re: Glade - Have you experience

- **From:** "bwtiffin" <ua-author-14501766@usenetarchives.gap>
- **Date:** 2016-05-03T08:38:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2eafecfbb2-p30@usenetarchives.gap>`
- **In-Reply-To:** `<n8a02l$p1h$1@dont-email.me>`
- **References:** `<n8a02l$p1h$1@dont-email.me>`

```
On Wednesday, January 27, 2016 at 3:48:00 AM UTC-5, Delta11 wrote:
› How to display a GUI glade-3(xml) form and programming events?
› Everyone have experience?

Take a look at https://sourceforge.net/p/open-cobol/discussion/cobol/thread/ab28685d/#285e/f9d1

It got better though, cobweb-gtk can now take advantage of new extensions in GnuCOBOL 2, as of Revision 814.

PROCEDURE DIVISION USING gtk-widget gtk-user RETURNING OMITTED

Until recently COBOL could not generate functions that mapped to C void returns, now it can. That means the GtkBuilder XML can mention COBOL subprogram entry points for managing callbacks, for things like button clicked events. Previous version required a thin C layer that effectively ate the default return-code from COBOL programs. No need for the voidcall.c wrapper anymore, and that means straight up COBOL can play a part in the GTK+ event handlers.

The need for that voidcall wrapper pretty much put paid to using GtkBuilder with Glade files, as there was no way to insert the wrapper given the XML source. The callbacks had to be C functions, or the burden was on the developer to call all the attach-signal functions, which defeated a lot of the Glade designer tools. That is fixed now.

It means that event handlers have proper COBOL access to the program state, and can manipulate working-storage without passing data around through layers of CALL or being wrapped in voidcall. (And that only worked by using up the GTK userdata pointer that is associated with most widgets. That gets freed up now for all callback registrations with RETURNING OMITTED.

So, yayys. It's an extension, but it allows GnuCOBOL to take part in a lot more gui development. Even for Windows with timer event callbacks and the like, the new PROCEDURE DIVISION RETURNING OMITTED will generate code that does not put a default return-code into the callframe.

RETURNING OMITTED generates a void return entry point, and sets RETURN-CODE to 0.

PROCEDURE DIVISION RETURNING NOTHING generates a void return and leaves RETURN-CODE untouched.

I'll update the cobweb-gtk sources and docs within the next few, umm, sometime. :-) But for now, the new-builder example can be used with RETURNING OMITTED callback handlers and it won't corrupt any call frames, so the Glade XML files will work just fine with COBOL entry point names.

It kinda means you can have executable GUI programs in three lines of COBOL main procedure division

move new-builder(xmlname, 1) to gtk-builder-record
move gtk-go(gtk-builder-record) to return-code
goback.

two lines if you really want to go to town,

move gtk-go(new-builder(xmlname, 1)) to return-code
goback.

but that is getting a little too lean, and not very COBOL like. ;-)

Drop a note on SourceForge if you need any help.

docs are still at http://peoplecards.ca/cobweb/cobweb-gtk/ and http://peoplecards.ca/cobweb/cobweb-gtk/cobweb-gtk_cob.html#robo13

Project space at https://sourceforge.net/p/open-cobol/discussion/help/

Have good, make well,
Brian
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
