[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Enterprise COBOL, Requests for Enhancements

_27 messages · 8 participants · 2015-07_

---

### IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-07T13:55:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
I made the following RFEs and would love some votes on them.

Perform until exit (73686): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73686
User defined constants (73687): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73687
Boolean support and bit manipulation (73688): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73688
TRIM Intrinsic function (73689): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73689
Implement dynamic-capacity tables (73693): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73693

Frank Swarbrick
FirstBank - Lakewood, CO USA
```

#### ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "cfmpublic" <ua-author-14486889@usenetarchives.gap>
- **Date:** 2015-07-07T19:59:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
On Tue, 7 Jul 2015 10:55:43 -0700 (PDT), Frank Swarbrick
wrote:

› I made the following RFEs and would love some votes on them.
› 
…[4 more quoted lines elided]…
› Implement dynamic-capacity tables (73693): https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73693

Note for those reading this on comp.lang.cobol, these are for the IBM
z series environment which has gotten a totally new compiler in the
past couple of years. The back end of the compiler (machine code
generation) will be shared with compilers for other languages.

These require an IBM id to view. I'm assuming that all are taken from
the 2002 standard (or more recent if any). I'm assuming the first is
the EXIT PERFORM and related constructs. I don't recall the second
and wonder if it is needed since modern IBM compilers treat a field
that is never updated as a constant and if 1 byte have used Compare
Logical Immediate and Move Immediate instructions with the values
(this dates back to COBOL VS 1.4, the first IBM implementation of the
1985 standard). Boolean and Bit are definitely in the 2002 standard
and were at least 3 decades overdue then. I think dynamic capacity
tables are in the 2002 standard. I would add a request for the
decimal floating point data type and the additional rounding options,
both of which are either in the 2002 standard or draft (final?)
follow-ons. PL/1 has the data type as does IBM C/C++ and DB2. All of
the BINARY usages (CHARACTER, SHORT, LONG, etc.) also should be added.
There are SHARE requirements submitted by me for many of these things
in the 2001 - 2002 time frame if I recall correctly (SHARE
installation CFM).

Clark Morris
›
› Frank Swarbrick
› FirstBank - Lakewood, CO USA
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-07T20:41:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p2@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p2@usenetarchives.gap>`

```
The "perform until exit" is not part of any COBOL standard, although that seems to me to be an "oversight" (though likely intentional). EXIT PERFORM itself was actually already implemented earlier this year (yay!) as part of Enterprise COBOL V5R2. My RFE is for a small enhancement to make using it even more friendly.

User define constants are much more than what is currently available. Here's a simple example:

01 my-field PIC X(80).
01 myfieldlen IS CONSTANT AS LENGTH OF my-field.
01 prev-my-field PIC X(myfieldlen).

my-field and prev-my-field need to always be the same size. By changing the PIC length for my-field you will now implicitly change the PIC length for pre-my-field. There are several other useful uses.

I agree that all of the "binary" usages need to be added. Since we already have COMP-5 I'm not sure how much traction it would get (though we are currently lacking altogether a BINARY-CHAR equivalent), so I didn't make it a priority at the moment. The COBOL 2002 standard has additional usage types: float-short (*), float-long (*), float-extended, (* These two are, I believe, the same as COMP-1 and COMP-2) and COBOL 2014 added float-binary-32, float-binary-64, float-binary-128, float-decimal-16, or float-decimal-34. I don't have any personal "use cases" for those, but I would vote for them if others have a good use case.

It's not clear to me if COBOL 2002 defines rounding rules beyond COBOL 1985, but COBOl 2014 definitely does. In the OPTIONS paragraph you can specify a "DEFAULT ROUNDED MODE" clause with any of the following:
- AWAY-FROM-ZERO
- NEAREST-AWAY-FROM-ZERO
- NEAREST-EVEN
- NEAREST-TOWARD-ZERO
- PROHIBITED
- TOWARD-GREATER
- TOWARD-LESSER
- TRUNCATION
NEAREST-AWAY-FROM-ZERO is the default if this clause is not specified and "is the rounding mode provided by the ROUNDED phrase in previous COBOL
standards"

There is also an "INTERMEDIATE ROUNDING" clause with the following options:
- NEAREST-AWAY-FROM-ZERO
- NEAREST-EVEN
- PROHIBITED
- TRUNCATION
NEAREST-EVEN is the default if this cause is not specified.

You can also override the "DEFAULT ROUNDED MODE" at the statement level:

COMPUTE X ROUNDED MODE IS AWAY-FROM-ZERO = (A * B + C - D) / E.

I dare say it appears you could even do something like this:
COMPUTE X ROUNDED MODE IS AWAY-FROM-ZERO
Y ROUNDED MODE IS NEAREST-TOWARD-ZERO
= (A * B + C - D) / E.

I personally have never had a need to alternative rounding rules, but I'm sure others have.

The TRIM function and dynamic-capacity tables are, believe it or not, part of the COBOL 2014 standard but not the COBOL 2002 standard. When creating the 2002 standard it seems like the working group spent too much time on OO COBOL and not enough on enhancements to basic COBOL! :-(

Frank

On Tuesday, July 7, 2015 at 6:00:04 PM UTC-6, Clark Morris wrote:
› On Tue, 7 Jul 2015 10:55:43 -0700 (PDT), Frank Swarbrick
›  wrote:
…[35 more quoted lines elided]…
›› FirstBank - Lakewood, CO USA
```

#### ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-07T20:53:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
Frank Swarbrick wrote:
› I made the following RFEs and would love some votes on them.

I don't have time at the moment to review these in detail but will try and
look at them when I can.

Meantime, here are some thoughts...

1. It is pretty easy to want stuff. In order to get it, it has to be
implementable with a benefit that will not exceed the cost of doing it. Have
you considered these requests from the POV of a compiler writer?

›
› Perform until exit (73686):
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73686

Not sure what you mean by this. I thought that was what PERFORM normally
does currently...



› User defined constants (73687):
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73687

I remember some early versions of COBOL implementing a CONSTANT SECTION.
Nobody used it because there was little advantage over using
WORKING-STORAGE. Again, you may have a different meaning intended.

› Boolean support and bit manipulation (73688):
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73688

Some of us have been requesting this for years... :-) But, to be fair,
there are external libraries provided by most COBOL vendors that will do it,
and it isn't high on a list of priorities for a language which is intended
to shovel bytes around.



› TRIM Intrinsic function (73689):
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73689

I use this a lot in C# but in COBOL I have never seen a need for it. COBOL
tends to deal with fixed length strings and that makes TRIMming them a tad
unnecessary. Having worked with both the COBOL idea of a string and the
dynamic strings in other languages, I am persuaded to the dynamic model
rather than fixed length. For that, TRIM makes sense; for fixed length, less
so... (Strings in C# are immutable. That means that if you want to change it
you must make a new copy (or the compiler will make it for you...) TRIM is
useful in that environment.

› Implement dynamic-capacity tables (73693):
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73693

Another one that people have wanted for as long as I can remember. We used
to use GETMAIN and write our own management for it. But again, it is
difficult to implement for COBOL. Working now in C#, it is the usual case to
have arrays dynamically extend themselves transparently and efficiently,
when they need to. But I find that, where I would probably have used a
(fixed length) table in COBOL, I now tend to use lists and collections in C#
because they are innately enumerable and offer other useful properties
right out of the box.

Considering all of the above, I guess I'm saying that if you really want
these things, use a different language. COBOL has gotten by without them for
many decades.

Nevertheless, Frank, I wish you luck with your RFEs.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-08T02:24:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p4@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap>`

```
Example for "PERFORM UNTIL EXIT":

PERFORM UNTIL EXIT
READ MY-FILE
AT END
EXIT PERFORM
END-READ
PERFORM PROCESS-MY-RECORD
END-PERFORM

Without the "UNTIL EXIT" clause I can:
- Make a dummy condition, set it to "false" and never change it (yuck)
- Go back to using "priming reads"
- Have the AT END condition SET a flag that tells the loop to terminate (and don't do the PERFORM of PROCESS-MY-RECORD

I like "PERFORM UNTIL EXIT".

See my previous reply for a good use of a COBOL constant. Here's another example I've long been wanting a solution for.

01 status-table.
05 status-ent.
10 PIC X VALUE '0'.
10 PIC X(5) VALUE 'ACTV'
05.
10 PIC X VALUE '1'.
10 PIC X(5) VALUE 'DEL'
05.
10 PIC X VALUE '2'.
10 PIC X(5) VALUE 'CAPT'
01 se-max CONSTANT AS LENGTH OF status-table / LENGTH OF status-ent.
01 REDEFINES status-table.
05 status-entry OCCURS se-max TIMES.
10 se-status-code PIC X.
10 se-status PIC X(5).

I can easily add a new entry to status-table and se-max will increase appropriately, automatically.

I have constant need for the TRIM function. Not sure what work-around you use, but I've never found a satisfactory one. No, I'm not talking about fixed-column reports, where in general you don't need them.

As for "use another language", remember this is IBM mainframe. We have:
- COBOL
- PL/I
- C/C++
- Assembler
- and possibly REXX (but not for general business applications, in my opinion).

Which do you suggest?

I am cautiously optimistic about these RFEs being fulfilled. The compiler team seems to be a bit on a roll these days. They've already given us the enhanced EXIT statements and table sorts, and seem very open to additional enhancements.

Oh, and "dynamic strings" are something I am going to request as well. Just wanted to put a few simple ones and a few "heavy hitters" out first.
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-08T09:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p5@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p5@usenetarchives.gap>`

```
Frank Swarbrick wrote:
› Example for "PERFORM UNTIL EXIT":
› 
…[8 more quoted lines elided]…
› Thanks, this clarifies what you were getting at.
 
 
› Without the "UNTIL EXIT" clause I can:
› - Make a dummy condition, set it to "false" and never change it (yuck)
› - Go back to using "priming reads"
› - Have the AT END condition SET a flag that tells the loop to
› terminate (and don't do the PERFORM of PROCESS-MY-RECORD

I use the third of your options, as follows:
...
01 END-FLAG PIC X VALUE '0'.
88 PROCESS-EXIT VALUE '1'.

PERFORM UNTIL PROCESS-EXIT
READ MY-FILE
AT END
EXIT PERFORM [Or.... SET PROCESS-EXIT TO TRUE]
NOT AT END
PERFORM PROCESS-MY-RECORD
END-READ
END-PERFORM

This is pretty close to what you are asking for.

›
› I like "PERFORM UNTIL EXIT".
›
So do I, but not to the extent where I would ask someone to implement it...
:-)



› See my previous reply for a good use of a COBOL constant.  Here's
› another example I've long been wanting a solution for.
…[18 more quoted lines elided]…
› appropriately, automatically.

Gets a bit sticky when you have three levels of OCCURS...

I believe Micro Focus COBOL implements something along these lines but it is
so long since I used it I have forgotten the details.

You can do it yourself, of course, but you must remember to update the
"constant"... (I put a *> note on the table if I do this.)


› 
› I have constant need for the TRIM function.  Not sure what
› work-around you use, but I've never found a satisfactory one.  No,
› I'm not talking about fixed-column reports, where in general you
› don't need them.

I'd need to see a case before commenting. I have never found a need to TRIM
in COBOL . Neither can there be such a need if you are working with fixed
length strings, which is the case in COBOL. You CAN'T trim it because you
can't change the length of the string. If it is padded with spaces (the
default behaviour) it is NOT trimmed...(In fact whatever the remainder of
the field has it is still not trimmed.) I s'pose you could drop a single hex
zero at the end of the text you want trimmed, but that's a bit ugly... and
it still wouldn't always work.

If I wanted to extract specific text from a string in COBOL I would use
refmodding, but you have to put it somewhere, and it will be the length of
wherever you put it. You COULD use the refmodding within a STRING statement
to extract just what you want and build it into something else but
eventually you hit the fixed string length which is innate in COBOL. TRIM
functions only make sense in a context of variable string length and that
isn't COBOL.

Maybe we have different ideas about what you mean by TRIM...

>
› As for "use another language", remember this is IBM mainframe.  We
…[8 more quoted lines elided]…
› Which do you suggest?

COBOL, PL/1, and Assembler will cover everything you asked for.

Given that most of these things are not essential and not required very
often, but would be "nice to have" (from a programming POV), I wouldn't
personally expect someone to implement them at no charge to me.
› 
› I am cautiously optimistic about these RFEs being fulfilled.  The
› compiler team seems to be a bit on a roll these days.  They've
› already given us the enhanced EXIT statements and table sorts, and
› seem very open to additional enhancements.
 
› Well, they need to justify their existence, so you might get lucky... :-)
› 
› Oh, and "dynamic strings" are something I am going to request as
› well.  Just wanted to put a few simple ones and a few "heavy hitters"
› out first.

I hope you get what you want, but I owuldn't be holding my breath... :-)

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-10T21:57:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p4@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› Frank Swarbrick wrote:
›› I made the following RFEs and would love some votes on them.
…[8 more quoted lines elided]…
› you considered these requests from the POV of a compiler writer?

Cost/benefit is less the province of a compiler writer and more that of a
compiler seller.

[snip]

›› Boolean support and bit manipulation (73688):
›› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73688
…[4 more quoted lines elided]…
› to shovel bytes around.

It is not easy for me to think of a COmmon Business case for Boolean
support and bit manipulation... but at one time it was not easy for me to
grow a beard or sing baritone. Things change with times and times change
with things.

[snip]

› Considering all of the above, I guess I'm saying that if you really want
› these things, use a different language. COBOL has gotten by without them for
› many decades.

'To get by without' differs from 'to be unreachable from the current
road'.

DD
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2015-07-11T10:24:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p7@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap>`

```
On Sat, 11 Jul 2015 01:57:05 +0000 (UTC), doc··f@pa··x.com () wrote:

› In article ,
› Pete Dashwood  wrote:
…[14 more quoted lines elided]…
› with things.

The customer, product and open account files where I worked in the
1960's and after had bit switches to save tape and disk space.
Although we had assembler routines to pack and unpack bytes, Boolean
would have been much better.

Clark Morris
› 
› [snip]
…[8 more quoted lines elided]…
› DD
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-11T11:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p8@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap>`

```
In article <9e9··n@4··.com>,
Clark F Morris wrote:
› On Sat, 11 Jul 2015 01:57:05 +0000 (UTC), doc··f@pa··x.com () wrote:
› 
…[21 more quoted lines elided]…
› would have been much better.

Mr Morris, some find this shocking but... the most recent part of the
1960s are nigh a half-century back. I recall well having the need to set
up to 255 conditions for an 8-bit field then.

Perspective: in 1955 would one say 'there's a need to set aside funds from
the city budget for cleaning up the day's horse-droppings?'

The answer might well be 'Horse-droppings!' In 1905 clearing out the
manure was something Everyone Knew needed to be done and by 1955 the same
Everyone knew it never needed to be done.

Things change with times and times change with things. There might be a
COmmon Business case to be made in this brave, new millennium for Boolean
support and bit-level manipulation but the year 2019 has yet to arrive.

DD
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-11T20:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p9@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p9@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article <9e9··n@4··.com>,
› Clark F Morris   wrote:
…[40 more quoted lines elided]…
› yet to arrive.

I agree.

Continuing the horse analogy, there are still people who ride horses, but
they don't generally do so on the main street. (New York cops are an
exception... and there is some concern about them...
http://nypost.com/2013/08/19/outrage-at-nypd-poo/ ,
http://www.nydailynews.com/opinion/horse-occupation-wall-st-resident-tired-stepping-minefields-manure-article-1.995081 ,
http://www.boweryboogie.com/2013/11/responsible-cleaning-nypd-horse-shit-hell-square/
...and there are many more)

There is a certain incongruity in requiring dog owners (who pay an annual
licence fee) to immediately clean up after their pets, but horses with cops
on are allowed to dump with impunity.

The point is that anachronisms (like mounted policemen and, possibly, bit
processing requirements in COBOL) can bring their own problems.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-12T10:06:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p10@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p9@usenetarchives.gap> <gap-d038bfc32f-p10@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article <9e9··n@4··.com>,
 
›› [snip]
 
›› The answer might well be 'Horse-droppings!'  In 1905 clearing out the
›› manure was something Everyone Knew needed to be done and by 1955 the
…[7 more quoted lines elided]…
› I agree.

When someone agrees with me I think 'One of us must be wrong!'... but at
times I think Wildely.

[snip]

› There is a certain incongruity in requiring dog owners (who pay an annual
› licence fee) to immediately clean up after their pets, but horses with cops
› on are allowed to dump with impunity.

The relationship between the populace and the constabulary in the USA may
be a bit different than it is in other parts of the world; the discussion
of the increase militarisation of my country's police force might be cause
for other discussions.

Never mind that policevolk can break posted speed limits or drive the
wrong way on one-way streets and garner nary a glance... horse-droppings
or not I (a well-known fraidy-cat) am loath to attempt even a polite
'Mightn't it be done otherwise?' to someone who carries a gun, a club and
a can of tear-gas.

DD
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 7)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-13T02:21:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p11@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p9@usenetarchives.gap> <gap-d038bfc32f-p10@usenetarchives.gap> <gap-d038bfc32f-p11@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[36 more quoted lines elided]…
› DD

Understood. I believe I'd take the same position you do, if I lived in such
a State.

Cops here are encouraged to engage with the populace, do not (yet) overtly
carry guns (they have access to guns in the car and we have equivalent to
SWAT teams for serious armed offending), and they are subject to the same
Laws as the rest of us. In fact, police chases have to be called off if
there is a danger to the public in continuing pursuit. These days, with the
availability of eyes in the sky, very few get away. We live on islands, with
a comparatively small population, so there is nowhere to run to and most
serious crimes get solved. Nevertheless, the image of police amongst certain
sectors of the population is still "bad".

My personal experience (which is a limited sample) has been that they are
courteous and generally fair. I treat them the same way. :-)

I have never forgotten the bumper sticker I observed once in Texas: "If you
don't like cops, next time you're in trouble, call for a hippie."

But there is still a real danger that if ANY police force is too militant it
won't be long before the rights they are supposed to be protecting will be
trodden down for "the greater good".

There always needs to be a discernible difference between martial law
(imposed in extreme circumstances and enforced by the military) and normal
law (decided by the Democratic process and enforced by the police force). If
you can't tell the difference, then the police force needs review.

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 6)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2015-07-12T12:54:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p10@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p9@usenetarchives.gap> <gap-d038bfc32f-p10@usenetarchives.gap>`

```
On Sun, 12 Jul 2015 12:29:55 +1200, "Pete Dashwood"
wrote:

› doc··f@pa··x.com wrote:
›› In article <9e9··n@4··.com>,
…[58 more quoted lines elided]…
› processing requirements in COBOL) can bring their own problems.

I believe that PL1, C/C++ and other programs can create bit switch
data. I have used COBOL to process IBM's SMF records which contain
bit switches. Do the various data bases have bit data types? DYL280
now Vision something or another allowed bit manipulation. Bits, the
various forms of floating point and other data are available and used
in other language environments that are used to deal with "business"
data processing. And then there are things such as pictures which
have to be accommodated in the sense of at least being described and
movable.

Clark Morris
›
› Pete.
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-11T20:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p8@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap>`

```
Clark F Morris wrote:
› On Sat, 11 Jul 2015 01:57:05 +0000 (UTC), doc··f@pa··x.com () wrote:
› 
…[12 more quoted lines elided]…
› would have been much better.

So, you are saying you SHOULD have made your RFE 55 years ago... :-)

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 5)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2015-07-12T12:47:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p14@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p14@usenetarchives.gap>`

```
On Sun, 12 Jul 2015 12:17:13 +1200, "Pete Dashwood"
wrote:

› Clark F Morris wrote:
›› On Sat, 11 Jul 2015 01:57:05 +0000 (UTC), doc··f@pa··x.com () wrote:
…[15 more quoted lines elided]…
› So, you are saying you SHOULD have made your RFE 55 years ago... :-)
I believe that I made submissions to X3J4 in the 1970's or 1980's. I
don't think I submitted any SHARE (IBM mainframe user group)
requirements but I know I wanted bit manipulation from the 1960's
onward. Also there is other data that might be provided from
non-COBOL sources that contains bit switches. It is the same as IBM
COBOL only recognizing hexadecimal floating point when it has to
inter-operate with Java which only recognizes IEEE floating point. If
there is a base data type COBOL such as character, Unicode, the
various types of floating point, etc. COBOL may have to deal with it
because it is created by a non-COBOL process and passed to a COBOL
program.

CLark Morris
›
› Pete.
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-13T20:06:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p15@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p4@usenetarchives.gap> <gap-d038bfc32f-p7@usenetarchives.gap> <gap-d038bfc32f-p8@usenetarchives.gap> <gap-d038bfc32f-p14@usenetarchives.gap> <gap-d038bfc32f-p15@usenetarchives.gap>`

```
Clark F Morris wrote:
› On Sun, 12 Jul 2015 12:17:13 +1200, "Pete Dashwood"
›  wrote:
…[30 more quoted lines elided]…
› program.

I take your point, Clark.

And I'm not unsympathetic to having bit facilities in COBOL, but you haven't
made (in my opinion) a persuasive case for it, when the facility you require
is already available, just by usng a different language.

"COBOL may have to deal with it
because it is created by a non-COBOL process and passed to a COBOL
program."

But it is only passed to a COBOL program because that is what you choose to
use. If it made more sense to have COBOL call out to a different language to
deal with it, or you passed it to a language more suitable, the problem
would be solved.

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-10T20:37:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p17@usenetarchives.gap>`
- **In-Reply-To:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
In article <9b0193e1-f63a-42c9-a17a-7de··f@goo··s.com>,
Frank Swarbrick wrote:
› I made the following RFEs and would love some votes on them.
› 
…[9 more quoted lines elided]…
› https://www.ibm.com/developerworks/rfe/execute?use_case=viewRfe&CR_ID=73693

I thought about this for a bit. My conclusion was that my being unable to
see the use for a tool does not mean that others should be discouraged
from developing it.

Signing up for an account was a necessary nuisance.

DD
```

#### ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-13T16:40:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p18@usenetarchives.gap>`
- **In-Reply-To:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
The ISO 8583 standard used to transport "card" (credit card etc) data has a bitmap. Certainly the parsing or creating of such a message is a "business function".

The X.690 ASN.1 encoding formats (BER, CER and DER) are very much binary formats. The EMV specification for chip/smart cards encodes data using BER. Again, a business function.

So yes, "bit twiddling" would be useful in COBOL. (Micro Focus already supports it.)
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-14T08:28:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p18@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap>`

```
In article ,
Frank Swarbrick wrote:
› The ISO 8583 standard used to transport "card" (credit card etc) data
› has a bitmap.  Certainly the parsing or creating of such a message is a
…[7 more quoted lines elided]…
› supports it.)

An excellent point, Mr Swarbrick. A quibble might be that both examples
are for subsets of transactions for a specific business (interchange of
financial data), not COmmon Business functions... but this is truly a
quibble.

DD
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2015-07-14T08:36:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p18@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap>`

```
Hello Frank!

Monday July 13 2015 21:40, Frank Swarbrick wrote to All:

> The ISO 8583 standard used to transport "card" (credit card etc) data
> has a bitmap. Certainly the parsing or creating of such a message is
> a "business function".

> The X.690 ASN.1 encoding formats (BER, CER and DER) are very much
> binary formats. The EMV specification for chip/smart cards encodes
> data using BER. Again, a business function.

> So yes, "bit twiddling" would be useful in COBOL. (Micro Focus
> already supports it.)

Bit processing has been in the standard for a while and is supported in
GNUCobol (formally Open Cobol) at least in the v2.0 compiler and many
other compilers.

Not so sure about tight processing of AND, OR, XOR etc..


Vince
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-14T19:12:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p20@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap> <gap-d038bfc32f-p20@usenetarchives.gap>`

```
On Tuesday, July 14, 2015 at 7:48:30 AM UTC-6, Vince Coen wrote:
› Hello Frank!
› 
…[4 more quoted lines elided]…
› Not so sure about tight processing of AND, OR, XOR etc..

Indeed. And none of those other COBOL compilers are available for my environment (z/OS), which is why I am requesting the compiler that is available for that environment (IBM Enterprise COBOL) have these enhancements as well.
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2015-07-15T03:17:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p18@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap>`

```
On 7/13/2015 3:40 PM, Frank Swarbrick wrote:
› The ISO 8583 standard used to transport "card" (credit card etc) data has a bitmap. Certainly the parsing or creating of such a message is a "business function".
›
…[3 more quoted lines elided]…
›

I've worked with a couple of different parsers and formatters for
ISO-8583 messages written entirely in IBM mainframe COBOL, without using
any assembler subprograms. They use somewhat clumsy tricks to decode
bitmaps into byte switches and compress byte switches into bitmaps. We
can parse 150 million ISO-8583 messages in a batch job that runs 20
minutes. That means we can decode 16 bytes of bit flags into 128
one-byte switches at a rate of 125,000 transactions per second, and the
program does much more than simply decode the bitmaps.

I think we even distribute this code to customer banks who request it.

If there were more bit manipulation features in z/OS COBOL the generated
code could possibly be made more efficient. It might also be quicker to
write bit manipulation routines and easier to understand them for future
maintenance. Bit manipulation in COBOL almost never needs to be
modified for business application changes.

Kind regards,

http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-15T08:50:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p22@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap> <gap-d038bfc32f-p22@usenetarchives.gap>`

```
In article ,
Arnold Trembley wrote:

[snip]

› We 
› can parse 150 million ISO-8583 messages in a batch job that runs 20 
› minutes.  That means we can decode 16 bytes of bit flags into 128 
› one-byte switches at a rate of 125,000 transactions per second, and the 
› program does much more than simply decode the bitmaps.

Mr Trembley, at times when folks warble about a few tens of thousands of
transactions being 'big data' such numbers as you supply get met with a
stunned silence...

... into which it is appropriate to interject 'That's the way Real
Professionals do it, aye.'

DD
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-07-16T00:03:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p23@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap> <gap-d038bfc32f-p22@usenetarchives.gap> <gap-d038bfc32f-p23@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Arnold Trembley   wrote:
…[8 more quoted lines elided]…
› 
 
› Commendable.
 
› Mr Trembley, at times when folks warble about a few tens of thousands
› of transactions being 'big data' such numbers as you supply get met
› with a stunned silence...

"stunned silence" for 125,000 transactions a second? I don't think so.

Rather, just nothing remarkable.

http://www.extremetech.com/extreme/192929-255tbps-worlds-fastest-network-could-carry-all-the-internet-traffic-single-fiber

›
› ... into which it is appropriate to interject 'That's the way Real
› Professionals do it, aye.'
›

And the "REAL professionals" are the engineers who make this level of
throughput possible, not some software developers riding on their coat
tails... :-)

Pete
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-07-16T07:41:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p24@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p18@usenetarchives.gap> <gap-d038bfc32f-p22@usenetarchives.gap> <gap-d038bfc32f-p23@usenetarchives.gap> <gap-d038bfc32f-p24@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[11 more quoted lines elided]…
› Commendable.
 
› [snip of four lines of text]
 
› Rather, just nothing remarkable.

Mr Dashwood, ex Africa sepmer aliquid novi... do tell, when did your
dialect stop considering 'commendable' as a remark?

[snip]

›› ... into which it is appropriate to interject 'That's the way Real
›› Professionals do it, aye.'
…[4 more quoted lines elided]…
› tails... :-)

The skill of the road's designers in no way diminishes the professional
capabilities demonstrated by the drivers.

(a Real Professional might conclude with something about mail-order
courses in dismissive sneering offered by a Mancunian diploma-mill)

DD
```

#### ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "bugmagnet" <ua-author-14456390@usenetarchives.gap>
- **Date:** 2015-07-15T04:54:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p26@usenetarchives.gap>`
- **In-Reply-To:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com>`

```
On Wed, 08 Jul 2015 01:55:43 +0800, Frank Swarbrick
wrote:

› I made the following RFEs and would love some votes on them.
›

Joined up. Voted.

Pardon my abysmal awareness of COBOL -- it's been decades since I last had
anything serious to do with it: Does it have associative arrays yet?

Bruce.

Using Opera's mail client: http://www.opera.com/mail/
```

##### ↳ ↳ Re: IBM Enterprise COBOL, Requests for Enhancements

- **From:** "fswarbrick" <ua-author-11707177@usenetarchives.gap>
- **Date:** 2015-07-15T20:26:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d038bfc32f-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d038bfc32f-p26@usenetarchives.gap>`
- **References:** `<9b0193e1-f63a-42c9-a17a-7de921d934bf@googlegroups.com> <gap-d038bfc32f-p26@usenetarchives.gap>`

```
On Wednesday, July 15, 2015 at 2:54:21 AM UTC-6, Bruce M. Axtens wrote:
› On Wed, 08 Jul 2015 01:55:43 +0800, Frank Swarbrick   
› wrote:
…[4 more quoted lines elided]…
› Joined up. Voted.
 
› Great!
 
› Pardon my abysmal awareness of COBOL -- it's been decades since I last had  
› anything serious to do with it: Does it have associative arrays yet?

If only! I'm not sure we'll ever get to that one. I have a feeling any vendor would say "just use a binary SEARCH".

Nonetheless I do plan of requesting it some day.

Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
