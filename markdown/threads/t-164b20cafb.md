[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# When is a quote not a quote?

_23 messages · 10 participants · 1998-03_

---

### When is a quote not a quote?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

I would like to get some input (hear some feedback) from this newsgroup on
an issue related to the draft of the next COBOL Standard.

In the next Standard, it will (finally) be legal to use either a "double
quote" or a 'single quote' (aka apostrophe) around alphanumeric literals.
(Almost every compiler that I know of has had this ability since key punch
machines or when the compiler was first released - but that is another
issue.) The draft Standard allows the two to be mixed in the same program
but not for the same literal (as is allowed in some but not all existing
compilers that allow single quotes at all.)

HOWEVER, the draft Standard requires that the figurative constant QUOTE
*always* represent the "double quote" variation.

My question is whether you think that this is a real problem or not? Would
you like there to be a way to control this (options that exist today that I
know of include compiler options/directives or special-names phrases). Would
you like a new figurative constant (e.g. APOSTROPHE) to represent the single
quote?

or Generally, don't you care what the draft does about this?
```

#### ↳ Re: When is a quote not a quote?

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

On Thu, 12 Mar 1998 07:27:07 -0800, "William M. Klein"
wrote:

› Would
› you like a new figurative constant (e.g. APOSTROPHE) to represent the single
› quote?

hmm. it would be nice to have APOS as num 39(34?)
but apostrophe is a hard word to spell.



gvw··.@ix.··m.com remove the spam
```

#### ↳ Re: When is a quote not a quote?

- **From:** "alan brown" <ua-author-25618@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```



William M. Klein wrote in article
<6e8usr$h.··.@dfw··m.com>...
› I would like to get some input (hear some feedback) from this newsgroup
› on
…[22 more quoted lines elided]…
› quote?

I think there would be a problem if QUOTE were not consistant. Otherwise,
the results of the program would change from it's original intent based
upon a compiler/installation option. APOSTROPHE would be okay, but not
necessary.

› 
› or Generally, don't you care what the draft does about this?
…[12 more quoted lines elided]…
›
```

#### ↳ Re: When is a quote not a quote?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote:

› My question is whether you think that this is a real problem or not? Would
› you like there to be a way to control this (options that exist today that I
…[4 more quoted lines elided]…
› or Generally, don't you care what the draft does about this?

I have used the "QUOTE" quite often - but only because I was using a
compiler that needed the double quotes and not the apostrophes.

The problem cam in when the Apost was used instead of the Quote - heck
for years I thought the "double quote" was wrong.

Say you wanted something to be this: That's my name.

With the apost usage you could not do it easily. 'That's my name.'
would choke the compiler. "That's my name" works fine, but you have to
use quotes everywhere currently.

I'm getting to the point - bear with me.

The new standard that allows mixing, but not on the same litterals would
solve both problems - almost.

You could say '"Drat", he said' or
"That's mine"
but not:
'"Drat", he said, "That's mine"'

It would choke on that. Having QUOTE works well for stringing and
unstringing comma quote delimited files, but would not solve the above.

The above is solveable by using multiple literals and stringing them
together, even without the APOST word, having QUOTE is sufficient.

To allow one full freedom, it would be nice to have an APOST and a
QUOTE, but it will be better than present the way it is newly defined.

Answer: Don't care.
```

#### ↳ Re: When is a quote not a quote?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote:
› 
 
› [cut to the chase]
 
› HOWEVER, the draft Standard requires that the figurative constant QUOTE
› *always* represent the "double quote" variation.
› 
› My question is whether you think that this is a real problem or not? 

... as opposed to a 'fake problem'? No matter *what* the change is some
folks'll like it, some'll whine, urinate and moan... as they say in
Latin, 'ayn chadash tachat hashemesh'. Me, personally, I am so used to
single-quotes that you'll notice I use them all the doo-dah day... but I
am sure that somewhere, in the bowels of a Very Important System, that
Mission-Ctitical Code depends on the reserved-word QUOTE producing a
'... and I'm sure there is a Very Good Reason for it, too.

DD
```

#### ↳ Re: When is a quote not a quote?

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-03-12T14:06:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote:
› snipped
 
› HOWEVER, the draft Standard requires that the figurative constant QUOTE
› *always* represent the "double quote" variation.
…[7 more quoted lines elided]…
› or Generally, don't you care what the draft does about this?

Before you respond, be aware that the proposed standard allows literals
to be concatenated. Why would one need APOSTROPHE (or QUOTE for that
matter)? Of course, using the word QUOTE in creating a literal string
made little sense anyhow. For things like delimiters it was always just
as easy to say """" instead of QUOTE using standard terminology.

'Porky said "That' & "'s all folks" & '".'

Gee - it looks almost like C!

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

##### ↳ ↳ Re: When is a quote not a quote?

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p6@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap>`

```

On Thu, 12 Mar 1998 19:06:28 GMT, Don Nelson
wrote:

› Before you respond, be aware that the proposed standard allows literals
› to be concatenated.  Why would one need APOSTROPHE (or QUOTE for that
…[4 more quoted lines elided]…
›   'Porky said "That' & "'s all folks" & '".'


---------------------------------------------------------------
Ever Notice....

....how quickly "pay later" comes when you "buy now"?
....the weaker the arguments, the stronger the words?
....the first piece of luggage out of the airport baggage chute never belongs to anybody?
....the shortest line becomes the slowest line once you choose it?
....the last key in the bunch usually opens the lock?
....the first person to get off a crowded eleveator is always standing in the back?
....immediately after you buy an item, you find a coupon for it?
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p7@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p7@usenetarchives.gap>`

```

Paul Knudsen wrote:

› On Thu, 12 Mar 1998 19:06:28 GMT, Don Nelson 
› wrote:
…[7 more quoted lines elided]…
››   'Porky said "That' & "'s all folks" & '".'

Besides, those compiler vendors that allowed ' i.s.o. " (by specifying compile options) say
in their manuals that the figurative constant QUOTE(s) acts in accordance with the choosen
option. So the ones that really used the ' and the word QUOTE in their sources can (and will)
continue to do so. Almost nobody would like to mix usage of ' and " except in (rarely used)
porky-like constructs, where it will behave well-defined.

Implement it, I say!

2000 Cobol Frog(s)

[sig snip]
```

##### ↳ ↳ Re: When is a quote not a quote?

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p6@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap>`

```

On Thu, 12 Mar 1998 19:06:28 GMT, Don Nelson
wrote:

› Before you respond, be aware that the proposed standard allows literals
› to be concatenated.  Why would one need APOSTROPHE (or QUOTE for that
…[6 more quoted lines elided]…
› Gee - it looks almost like C!

You're right, it's just as unreadable. What were you and the
committee smoking the day you came up with this gem?
---------------------------------------------------------------
Ever Notice....

....how quickly "pay later" comes when you "buy now"?
....the weaker the arguments, the stronger the words?
....the first piece of luggage out of the airport baggage chute never belongs to anybody?
....the shortest line becomes the slowest line once you choose it?
....the last key in the bunch usually opens the lock?
....the first person to get off a crowded eleveator is always standing in the back?
....immediately after you buy an item, you find a coupon for it?
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p9@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap>`

```

Paul Knudsen wrote:
› 
› On Thu, 12 Mar 1998 19:06:28 GMT, Don Nelson 
…[13 more quoted lines elided]…
› committee smoking the day you came up with this gem?

... possibly some very well-aged stuff that caused some *other*
committee to come up with (COND,5,LT)?

DD
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 4)_

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p10@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p10@usenetarchives.gap>`

```

On Fri, 13 Mar 1998 06:50:49 -0500, The Goobers
wrote:

› Paul Knudsen wrote:
›› 
…[7 more quoted lines elided]…
› DD

That's "(COND=5,LT)". And now there's IF-THEN-ELSE and SET available
in JCL.. Progress at least.
---------------------------------------------------------------
Ever Notice....

....how quickly "pay later" comes when you "buy now"?
....the weaker the arguments, the stronger the words?
....the first piece of luggage out of the airport baggage chute never belongs to anybody?
....the shortest line becomes the slowest line once you choose it?
....the last key in the bunch usually opens the lock?
....the first person to get off a crowded eleveator is always standing in the back?
....immediately after you buy an item, you find a coupon for it?
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 5)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p11@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p10@usenetarchives.gap> <gap-164b20cafb-p11@usenetarchives.gap>`

```

Paul Knudsen wrote:

› On Fri, 13 Mar 1998 06:50:49 -0500, The Goobers 
› wrote:
…[13 more quoted lines elided]…
› in JCL..  Progress at least.

I assume you didn't have your JCL reference handy when you dashed off the above. It has to
be",COND=(5,LT)...". Pity about the IF-THEN-ELSE stuff, though, my QA people have them on the
"unapproved" list and won't accept JCL containing it:-(

Bill Lynch


› ---------------------------------------------------------------
› Ever Notice....
…[7 more quoted lines elided]…
› ....immediately after you buy an item, you find a coupon for it?
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 6)_

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p12@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p10@usenetarchives.gap> <gap-164b20cafb-p11@usenetarchives.gap> <gap-164b20cafb-p12@usenetarchives.gap>`

```

On Fri, 13 Mar 1998 22:52:05 -0500, Bill Lynch
wrote:


› I assume you didn't have your JCL reference handy when you dashed off the above. It has to
› be",COND=(5,LT)...". Pity about the IF-THEN-ELSE stuff, though, my QA people have them on the
› "unapproved" list and won't accept JCL containing it:-(
› 
› Bill Lynch

I must have been asleep! (Laughing) .

Truthfully I've found little need for IF-THEN-ELSE, but there was an
instance when we moved a trail from one site to another. Had to do an
XCOM at the old site but not the new. So we ran a house utility that
generates a condition code depending on what site it's running on,
and IF'd the XCOM step. Handy.

My company doesn't forbid much, but I get heat from my colleagues if I
use something they don't understand. Which includes a lot. Guess
that amounts to the same thing.
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 6)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p12@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p10@usenetarchives.gap> <gap-164b20cafb-p11@usenetarchives.gap> <gap-164b20cafb-p12@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
› Paul Knudsen wrote:
…[18 more quoted lines elided]…
› I assume you didn't have your JCL reference handy when you dashed off the above. It >has to be",COND=(5,LT)...". Pity about the IF-THEN-ELSE stuff, though, my QA people >have them on the "unapproved" list and won't accept JCL containing it:-(

Oh, I absolutely *adore* situations like that... tell me, has anyone
ever asked what the reason is for demanding that the language remain in
its most primitive form?

DD
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p9@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap>`

```

Paul Knudsen wrote:

› On Thu, 12 Mar 1998 19:06:28 GMT, Don Nelson 
› wrote:
 
› 8<
 
››   'Porky said "That' & "'s all folks" & '".'
›› 
…[3 more quoted lines elided]…
› committee smoking the day you came up with this gem?

I can read that. Works just like rexx.

Cobol Frog
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p15@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p15@usenetarchives.gap>`

```

Cobol Frog (Huib Klink) wrote:

› Paul Knudsen wrote:
› 
…[13 more quoted lines elided]…
› 

Exactly! I never have a problem reading REXX coded this way (which, of
course, is how I code it).

Bill Lynch


› Cobol Frog
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-03-13T12:50:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p9@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap>`

```

Paul Knudsen wrote:
›› as easy to say """" instead of QUOTE using standard terminology.
›› 
…[5 more quoted lines elided]…
› committee smoking the day you came up with this gem?

Good stuff! Actually, though, literal concatenation is a very good
thing. For instance, it is a zillion times easier than trying to
continue a literal across lines. It is just that you can write some
strange constructs with it.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 4)_

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p17@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p17@usenetarchives.gap>`

```

On Fri, 13 Mar 1998 17:50:41 GMT, Don Nelson
wrote:

› Paul Knudsen wrote:
››› as easy to say """" instead of QUOTE using standard terminology.
…[11 more quoted lines elided]…
› strange constructs with it.

Well maybe. I'll keep an open mind about it.

But what about:

77 Text Pic X(29) Value 'Porky said "That s all folks"'.
. . .
Move QUOTE to Text (17:1).

Would tend not to scramble the readers heads, especially with a PC
font.
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 5)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p18@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p6@usenetarchives.gap> <gap-164b20cafb-p9@usenetarchives.gap> <gap-164b20cafb-p17@usenetarchives.gap> <gap-164b20cafb-p18@usenetarchives.gap>`

```

Paul Knudsen wrote:
(snip)

›› 
›› Good stuff!  Actually, though, literal concatenation is a very good
…[13 more quoted lines elided]…
› font.

>From my perspective, this is very ugly. I'd want to think of "TEXT" as a
constant, which it isn't here. I might code this as:

01 TEXT.
05 FILLER PIC X(16) VALUE 'Porky said "That'.
05 FILLER PIC X VALUE QUOTE.
05 FILLER PIC X(13) VALUE 's all folks"'.

or (much more likely nowadays):

INITIALIZE TEXT
STRING 'Porky said "That' QUOTE 's all folks"'
DELIMITED BY SIZE INTO TEXT
END-STRING

Probably a matter of personal preference and local practice (i.e., this
is not meant as a flame).

Bill Lynch
```

#### ↳ Re: When is a quote not a quote?

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p20@usenetarchives.gap>`
- **In-Reply-To:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com>`

```

On Thu, 12 Mar 1998 07:27:07 -0800, "William M. Klein"
wrote:

› I would like to get some input (hear some feedback) from this newsgroup on
› an issue related to the draft of the next COBOL Standard.
…[18 more quoted lines elided]…
› or Generally, don't you care what the draft does about this?

It could be a problem. Apostrophe was the standard for so long that
most programs still use it. So you'll usually find that "Quote" means
apostrophe. In fact I know in CICS "Quote" stands for some screen
attribute. So if you're right about this standard it might break a
lot of programs.
---------------------------------------------------------------
Ever Notice....

....how quickly "pay later" comes when you "buy now"?
....the weaker the arguments, the stronger the words?
....the first piece of luggage out of the airport baggage chute never belongs to anybody?
....the shortest line becomes the slowest line once you choose it?
....the last key in the bunch usually opens the lock?
....the first person to get off a crowded eleveator is always standing in the back?
....immediately after you buy an item, you find a coupon for it?
```

##### ↳ ↳ Re: When is a quote not a quote?

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-03-13T12:55:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p20@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p20@usenetarchives.gap>`

```

› It could be a problem. Apostrophe was the standard for so long

It was never in any standard. It started as an IBM extension back in
the 60s or 70s.

› that
› most programs still use it.  So you'll usually find that "Quote" means
› apostrophe.  In fact I know in CICS "Quote" stands for some screen
› attribute.  So if you're right about this standard it might break a
› lot of programs.

It won't break anything. The single quote was an extension. All
previous standards said explicity that the quote was a quote, not an
apostrophe. What would break programs is a vendor who had the
apostrophe extension and took it away. I assume those vendors who had
such an extension will continue to support is as a non-standard
extension.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p21@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p20@usenetarchives.gap> <gap-164b20cafb-p21@usenetarchives.gap>`

```


Don Nelson wrote in message <350··.@tan··m.com>...
›› It could be a problem.  Apostrophe was the standard for so long
› 
›  >snippage<
 
› 
› It won't break anything.  The single quote was an extension.  All
…[7 more quoted lines elided]…
> more snippage< -

Actually, it will "break programs" if users think that because they can now
use the single-quote (apostrophe) as a literal delimeter, that they won't
need to use any extension. The example given by the user is an excellent
example. The QUOTE figurative constant appears in some vendor-supplied (IBM
in this case) COPYBOOKs in the VALUE clause of a field used as an attribute
byte. With the previous extension-implementation, this copybook was ONLy
used when the APOST (extension) compiler option was used - and this was easy
to veryify because other VALUE clauses would "fail" because they used
'literal' format VALUE clauses. Now, however, these other VALUE clauses
will work fine (because the draft allows the use of apostrophe and quote as
delimiters in the same program) and the VALUE QUOTE will compile just fine
as well - it will just cause radically different (i.e. "program is broken")
run-time results.

All of this is "fixable" by the programmer - but only after the program has
failed and their perception will be that the new Standard has caused it.
That perception could easily be avoided if the draft Standard provided its
own solution to what the figuative constant QUOTE means.
```

###### ↳ ↳ ↳ Re: When is a quote not a quote?

_(reply depth: 4)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-164b20cafb-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-164b20cafb-p22@usenetarchives.gap>`
- **References:** `<6e8usr$h3u@dfw-ixnews11.ix.netcom.com> <gap-164b20cafb-p20@usenetarchives.gap> <gap-164b20cafb-p21@usenetarchives.gap> <gap-164b20cafb-p22@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Don Nelson wrote in message <350··.@tan··m.com>...
›› 
›› It won't break anything.  The single quote was an extension.  
 
› Actually, it will "break programs" if users think that because they can now
› use the single-quote (apostrophe) as a literal delimeter, that they won't
› need to use any extension.

The genesis of this problem is that in olden times we had 6-bit
character sets, and 026 keypunches, and the character set didn't
necessarily have all the characters that the standard called for. It
was perfectly legal to use some other character, e g, apostrophe for
quote.

Then we went to ASCII and EBCDIC, where all the characters are present,
but old programs and old programmers kept using apostrophe. Vendors
provided the option to use the apostrophe, to maintain backward
compatibility.

This is an area where the standard bends over backwards to not specify
anything, then people get upset what wasn't specified. You are not
required to use any particular character encoding, nor any particular
font. Does the standard prohibit me from using a character set which is
almost ASCII, where characters 34 and 39 have been reversed? Does the
standard specify that I can't use a font where quote is a single tick?

But now the standard is going to support two quoting characters. If
this is being done in the name of compatibility, then it ought not to
break old programs. The standard committee should recognize the 6-bit
origins of the problem, and not blame implementors for historical
accident.

Therefore the standard should recognize the need for QUOTE to be
recognized as "'". I would add three reserved words: APOSTROPHE,
QUOTE-SINGLE and QUOTE-DOUBLE. Normally QUOTE would be the same as
QUOTE-DOUBLE, but a special names clause QUOTE IS QUOTE-SINGLE (or
APOSTROPHE) would provide compatibility.

(Aside: I discover that I'm going to have a second phone number back in
818 in order to keep my old 818 number alive. The service I wanted,
which would have used only one number, was eliminated to conserve phone
numbers. 818 was just split; why they just started conserving phone
numbers is beyond me.)

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-310-542-6013                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ The puzzle too hard for human beings:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
