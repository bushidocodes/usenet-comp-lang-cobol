[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Examples

_6 messages · 4 participants · 1999-06_

---

### COBOL Examples

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3773EEEB.3CCD9CC4@home.com>`

```
Michael,

Your reply June 25 to "How to write a macro substitution in acucobol?".
Nicely done, as usual, (just as you did in the days of the old
MicroFocus Compuserve forum) - a concise example to the writer's
problem.

Perhaps, amongst others, Bill Klein will contribute to this.

I was about to start "Before it gets out of hand", but it is already 
out of hand - the number of COBOL links - you could spend all day just
cruising in the flotsam looking for gold nuggets on how to use COBOL.

We need a COBOL Master site initially in the following four categories
:-

1- Standards 

Please, a simple organizational chart showing which committee does what
and inter-relationship to ISO, UML etc. No great detail, just a summary
box-chart with links to specific detailed sites. Obviously this is an
area that should include copies of the current and any proposed
standards.

2 - Examples

Needs control so that we don't get overwhelmed with variations of the
same thing, but a resource that covers all the COBOL syntax, examples
being contributed by COBOL developers. Take the message you just sent,
it probably should be listed alphabetically under both "string" and
"reference modification".

Each bit of syntax should have its own examples :-

- Take evaluate; until you look at somebody else's code, it is not
immediately apparent that :-

	evaluate char
	  when char = "a"  invoke/perform "a-and-b-routine"
	  when char = "b"  invoke/perform "a-and-b-routine"
	  when char = "c"  .........

could have been written :-

	evaluate char
	  when char = "a"  
	  when char = "b"  invoke/perform "a-and-b-routine"
	  when char = "c"  .........

And, of course, many variations on the above.

Similarly, first time I used intrinsic functions - following the text
from the M/S COBOL manuals I put :-

		a = function numvalc (my-text)

My query threw their Tech Support guy. He went away, and having spoken
to another techhie, came back with the reply, "it should be :-

		compute a = function numvalc (my-text)

It is only in the last couple of years, looking at others' code, that I
found it could be coded :-

		move function numvalc (my-text) to a

Don't want to flog it to death, but you get the idea.


3 - Compilers & Toolkits

A summary of all known compilers and COBOL-specific toolkits, including
shareware, covering all operating systems with links to each .

4 - Interesting COBOL Sites

Not quite sure how you "name" this one but links to your own site and
others. Can be a bit questionable, some fall into the category of
"vanity publishing". There is one site where the author covers OO -
beautiful elegant coding, but when you look at his current examples,
doesn't do a damn thing for OO - your reaction would be "why should I do
this in OO?". I can achieve the same with performs.

That's it. Jump in folks.

Jimmy, Calgary AB

PS : Funny lot MicroSoft - don't seem to comprehend us Canucks. If I
threw a stone hard enough, south-west of me, I could smash one of the
windows in Bill's University at Bellingham Wa. When using their COBOL
if I got mail from them it came postmarked BRUSSELS - yep, Belgium!
Maybe Bill should give up airmail and put his trust in Amtrak and CPR.
```

#### ↳ Re: COBOL Examples

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7l12e8$9un@dfw-ixnews16.ix.netcom.com>`
- **References:** `<3773EEEB.3CCD9CC4@home.com>`

```

> Similarly, first time I used intrinsic functions - following the text
> from the M/S COBOL manuals I put :-
…[14 more quoted lines elided]…
>

FYI,
  The "move" variation (instead of COMPUTE) *is* allowed by some (many?)
compilers but is NOT legal according to the CURRENT ANSI/ISO Standard.  It
will be legal in the next one.  The example with the COMPUTE is the
"portable" way to do it today.
```

##### ↳ ↳ Re: COBOL Examples

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37745F08.8173278D@home.com>`
- **References:** `<3773EEEB.3CCD9CC4@home.com> <7l12e8$9un@dfw-ixnews16.ix.netcom.com>`

```
Jimmy Gavan wrote :

> > .......found it could be coded :-
> >
> > move function numvalc (my-text) to a
> >
> 
and Bill Klein replied :-

> FYI,
>   The "move" variation (instead of COMPUTE) *is* allowed by some (many?)
> compilers but is NOT legal according to the CURRENT ANSI/ISO Standard.  It
> will be legal in the next one.  The example with the COMPUTE is the
> "portable" way to do it today.

Phew! Bill, you know your COBOL standards. What do you do, read a
chapter each night as you sip your bedtime drink ? I've a lurking
suspicion, given your response time, that you have either got your
laptop on a chain around your neck or you have had an implant - If you
really have nothing better to do, I suggest Microfocus let you loose
providing all those missing OO/GUI examples I keep bitching about!

<G> 

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: COBOL Examples

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7l2qtq$d7k@dfw-ixnews4.ix.netcom.com>`
- **References:** `<3773EEEB.3CCD9CC4@home.com> <7l12e8$9un@dfw-ixnews16.ix.netcom.com> <37745F08.8173278D@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:37745F08.8173278D@home.com...
> Jimmy Gavan wrote :
>
…[9 more quoted lines elided]…
> > compilers but is NOT legal according to the CURRENT ANSI/ISO Standard.
It
> > will be legal in the next one.  The example with the COMPUTE is the
> > "portable" way to do it today.
…[10 more quoted lines elided]…
> Jimmy, Calgary AB

The "advantage" of being on disability - is that I have nothing better to do
(???) than provide enlightenment to the world of COBOL.  Seriously,  at
various time in my life, I have read and reread COBOL Standards, IBM
mainframe documentation, X/Open documentation, and Micro Focus
documentation.  Doing "readers comment forms" is one of my favorite
"hobbies".
```

###### ↳ ↳ ↳ Re: COBOL Examples

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dZed3.12468$4e1.112386@iad-read.news.verio.net>`
- **References:** `<3773EEEB.3CCD9CC4@home.com> <7l12e8$9un@dfw-ixnews16.ix.netcom.com> <37745F08.8173278D@home.com> <7l2qtq$d7k@dfw-ixnews4.ix.netcom.com>`

```
In article <7l2qtq$d7k@dfw-ixnews4.ix.netcom.com>,
William M. Klein <wmklein at ix dot netcom dot com> wrote:

[snippolinio]

>Doing "readers comment forms" is one of my favorite
>"hobbies".

With all due respect, Mr Klein... and folks tell *me* that *I* need
psychiatric help?

DD
```

###### ↳ ↳ ↳ Re: COBOL Examples

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37760975.4D53F315@zip.com.au>`
- **References:** `<3773EEEB.3CCD9CC4@home.com> <7l12e8$9un@dfw-ixnews16.ix.netcom.com> <37745F08.8173278D@home.com> <7l2qtq$d7k@dfw-ixnews4.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Doing "readers comment forms" is one of my favorite "hobbies".

And getting a response from the IBM machine is a miracle. :->
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
