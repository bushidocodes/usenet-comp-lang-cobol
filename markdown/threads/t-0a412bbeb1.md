[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Go To" and "Structured programming"

_166 messages · 24 participants · 2003-04 → 2003-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### "Go To" and "Structured programming"

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-28T00:46:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```
As a follow-up on another thread ...

What I stated in the other thread is that SOME (but not all) definitions of
"structured" programming allow for a "Go To Exit of procedure" feature  -
such as the following structure

  Perform  ABC thru ABC-Exit
      ...
 ABC.
    Perform Something
    If Bad-Status
      Go to ABC-Exit
    End-If
    Perform Another
    If Also-Bad
      Go To ABC-Exit
    End-If
    Perform Finish-ABC
       .
   ABC-Exit.
        Exit.

    ***

There are other ways that this may ALSO be coded, but this does meet some
definitions of "structured programming" - in that there is a "single entry
and single exit" to each section of code - and there are no "crossing go
to's" or even "drop thru" logic.

For examples on the web, see:

-  http://www.ais.ucla.edu/ais/policies/cobolstd.htm
 "Programs should follow guidelines for 'structured' programming. 'GoTo's
should be used primarily to 'go to' an exit of a performed routine."

-
http://www.marriottschool.byu.edu/teacher/ISYS540/Fall1997/Structured.htm#sp
 "Another key to structured programming is that each block of code (i.e.,
sequence of statements) has a single entry point and a single exit point."

 - http://www.cusys.edu/pubs/cobgdln.html
  "All programs should follow the basic principles of structured and
top-down programming.   ...
GO TO statements should only be used to branch down to the exit of a
section/paragraph or to an abort routine. "

  ***

and if you use GOGGLE or equivalent, you will find many others.  It is ALSO
possible to find a number of places that indicate that this usage DOES
violate the rules of "structured programming" - which is why I (originally
and still) indicate that it may or may not be "valid" in structured
programming (depending upon your definition).
```

#### ↳ Re: "Go To" and "Structured programming"

- **From:** Gerry Wolfe <gerry.wolfe@sympatico.ca>
- **Date:** 2003-04-28T09:38:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```
Along those lines...

Remember that a main purpose of "structured programming" is to
increase readability, reduce errors, reduce maintenance, yadda
yadda...

When I come across a catastrophic error (e.g. major FILE STATUS issue)
I have no probs with displaying related info and doing an immediate
STOP RUN or GO TO a shutdown routine.  I mean, there ain't any further
processing to be done, so why bother (for example) setting a switch to
indicate that the end of the world has actually arived (as far as the
program is concerned) and then have to test for it in higher-level
logic.

Just my $0.02Cdn...

On Mon, 28 Apr 2003 00:46:00 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>As a follow-up on another thread ...
>
…[50 more quoted lines elided]…
>programming (depending upon your definition).
```

##### ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T15:13:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jgep$d92$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com>`

```

On 28-Apr-2003, Gerry Wolfe <gerry.wolfe@sympatico.ca> wrote:

> Along those lines...
>
> Remember that a main purpose of "structured programming" is to
> increase readability, reduce errors, reduce maintenance, yadda
> yadda...

Agreed.   See below.

> When I come across a catastrophic error (e.g. major FILE STATUS issue)
> I have no probs with displaying related info and doing an immediate
…[4 more quoted lines elided]…
> logic.

Agreed.

But I also don't think it is structured to replace GO TO with a switch. 
Switches do not "increase readability, reduce errors, reduce maintenance, yadda,
yadda".
```

##### ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T03:51:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eadb031.361090998@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com>`

```
Gerry Wolfe <gerry.wolfe@sympatico.ca> wrote:

>Along those lines...
>
…[10 more quoted lines elided]…
>logic.

That's like giving a file clerk authority to declare the company bankrupt
because she finds the file drawer jammed shut. Within her narrow perspective,
it's an 'unrecoverable error'. 

Perhaps someone higher up can recover from the condition by dispatching a
repairperson (VERIFY). Perhaps the file was 'optional' and the program can
operate without it.

Programs should be organized like corporations, with decisions made at high and
intermediate levels of management, grunt work done at low levels. Grunts
shouldn't make major decisions like aborting the job. Even if we 'know' the
manager will cave today, that might change tomorrow when a new manager takes his
place. 

As for single exit point, I think GO TO, EXIT PARAGRAPH and the like are form
over substance. There isn't really a single exit point, the EXIT PARAGRAPH is
the exit point. In cases like this, I have no problem with setting a return code
followed by inline GOBACK. That seems more honest. It doesn't pretend to go
through the 'single' exit point. 

--- history follows ---

>
>On Mon, 28 Apr 2003 00:46:00 -0500, "William M. Klein"
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** docdwarf@panix.com
- **Date:** 2003-04-29T09:45:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8lvl7$b5c$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net>`

```
In article <3eadb031.361090998@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>Gerry Wolfe <gerry.wolfe@sympatico.ca> wrote:
>
…[20 more quoted lines elided]…
>operate without it.

... or perhaps the problem is beyond the scope of a VERIFY, perhaps the 
file is 'mandatory' and maybe the Ops crew needs to wake up on-call 
support at 3:am just to check the readability of the source-code.

>
>Programs should be organized like corporations, with decisions made at high and
>intermediate levels of management, grunt work done at low levels. Grunts
>shouldn't make major decisions like aborting the job.

... or not-aborting the job when the specs say to do it.

>Even if we 'know' the
>manager will cave today, that might change tomorrow when a new manager takes his
>place. 

... or it might not.  Meanwhile the program has to be written and the 
Business Analyst has demanded that if the file containing the dates for 
business holidays is not found when it is opened then the program's 
calculations of intervening business days will be invalid so the program 
should be ABENDed and re-run after further research.

In this case - and not a few others like it, Mr Wagner - clear, 
unambiguous and direct instructions are given for the programmer to code 
an ABEND.  What do you think a programmer should do when given a clear, 
unambiguous, direct and legal instruction by a duly-authorised corporate 
superior?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-30T12:36:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaf1a9b_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b8lvl7$b5c$1@panix1.panix.com...
> In article <3eadb031.361090998@news.optonline.net>,
> Robert Wagner <robert@wagner.net> wrote:
…[7 more quoted lines elided]…
>
That looks like the Nuremburg defence to me, Doc...<G>

As somebody who frequently prepares specs for programmers, I am pleased if
they question something that doesn't look good to them.

It is supposed to be a team effort. No analyst will necessarily have all the
information that the people at the "coal face" may have, especially where it
is specific to their particular environment.

Does it hurt to take a few minutes and look at it again?

As a programmer, I have frequently questioned specs presented by a
"duly-authorised corporate superior" and they are usually glad I did.

I am also extremely pissed off when a guy codes something which he KNOWS is
not going to work "because the spec said to do so..." (I have actually fired
one guy for doing this. He had a personality problem with a particular
Analyst and was prepared to bring production to a standstill to make the guy
look bad... I can't use guys with that kind of attitude. He believed that
his defence was water-tight "I only did what I was told". Not good enough on
my watch, I'm afraid. I want people who will think about what they are told
and keep the overall purpose in mind...)

I believe you and I have disagreed on this before, but I'm happy to explore
it again....<G>.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-29T21:48:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8na20$roe$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1>`

```
In article <3eaf1a9b_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b8lvl7$b5c$1@panix1.panix.com...
…[10 more quoted lines elided]…
>That looks like the Nuremburg defence to me, Doc...<G>

Ummmmm... last I looked 'corporate' was a civilian entity, not a military 
one.

>
>As somebody who frequently prepares specs for programmers, I am pleased if
>they question something that doesn't look good to them.

Once the questioning is done there may come a point where a 
duly-authorised corporate superior gives a programmer a clear, 
unambiguous, direct and legal instruction as to the functioning a program 
is to be written to perform.  What do you think a programmer should do 
then?

>
>It is supposed to be a team effort. No analyst will necessarily have all the
…[3 more quoted lines elided]…
>Does it hurt to take a few minutes and look at it again?

I have seen some folks act as though it does... but that aside, fine, well 
and good, it is looked at again... and a duly authorised corporate 
superior (etc., see above).  What is a programmer to do then?

>
>As a programmer, I have frequently questioned specs presented by a
>"duly-authorised corporate superior" and they are usually glad I did.

'Usually' is not 'universally', last I looked.  There may come a point 
when a duly-authorised corporate superior (etc., see above).  What is a 
programmer to do then?

>
>I am also extremely pissed off when a guy codes something which he KNOWS is
…[3 more quoted lines elided]…
>look bad... I can't use guys with that kind of attitude.

I disagree, Mr Dashwood.  I would think that you disagree with one who 
will sacrifice Work for Politics.

>He believed that
>his defence was water-tight "I only did what I was told". Not good enough on
>my watch, I'm afraid. I want people who will think about what they are told
>and keep the overall purpose in mind...)

What you want, Mr Dashwood, and the desires of others just might possibly 
not be the same thing... you may have noticed this.

>
>I believe you and I have disagreed on this before, but I'm happy to explore
>it again....<G>.

The exploration is a simple one.  A spec is issued.  The programmer speaks 
of concerns and these concerns receive a fair, impartial and dispassionate 
review.  After said review a duly-authorised corporate superior states 
that the programmer, as a corporate resource, is to be directed towards 
the clear, unambiguous and legal action of coding an ABEND in the program 
for a certain set of conditions.

What is the programmer to do under such conditions?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-30T21:01:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaf90f5_1@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b8na20$roe$1@panix1.panix.com...
> In article <3eaf1a9b_2@127.0.0.1>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:b8lvl7$b5c$1@panix1.panix.com...
> >> In article <3eadb031.361090998@news.optonline.net>,
> >> Robert Wagner <robert@wagner.net> wrote:
…[3 more quoted lines elided]…
> >> unambiguous and direct instructions are given for the programmer to
code
> >> an ABEND.  What do you think a programmer should do when given a clear,
> >> unambiguous, direct and legal instruction by a duly-authorised
corporate
> >> superior?
> >>
…[4 more quoted lines elided]…
>

I use the term "Nuremburg defence" as a generic term for this type opf
defence. It doesn't matter whether it is Civil or Military exactly as your
"Brooklyn Bridge" defence is a generic one, and not limited to residents of
New York...<G>.
> >
> >As somebody who frequently prepares specs for programmers, I am pleased
if
> >they question something that doesn't look good to them.
>
…[6 more quoted lines elided]…
> >

Once the questioning is done and any observations have been examined, then
management have the right to manage and a direction can be given, which
should be complied with.  In the example you used, there had been no such
provision for question or examination, just the direction to "Do it".

> >It is supposed to be a team effort. No analyst will necessarily have all
the
> >information that the people at the "coal face" may have, especially where
it
> >is specific to their particular environment.
> >
…[4 more quoted lines elided]…
> superior (etc., see above).  What is a programmer to do then?

Once the questioning is done and any observations have been examined, then
management have the right to manage and a direction can be given, which
should be complied with.  In the example you used, there had been no such
provision for question or examination, just the direction to "Do it".


>
> >
…[6 more quoted lines elided]…
>

Once the questioning is done and any observations have been examined, then
management have the right to manage and a direction can be given, which
should be complied with.  In the example you used, there had been no such
provision for question or examination, just the direction to "Do it".



> >
> >I am also extremely pissed off when a guy codes something which he KNOWS
is
> >not going to work "because the spec said to do so..." (I have actually
fired
> >one guy for doing this. He had a personality problem with a particular
> >Analyst and was prepared to bring production to a standstill to make the
guy
> >look bad... I can't use guys with that kind of attitude.
>
> I disagree, Mr Dashwood.  I would think that you disagree with one who
> will sacrifice Work for Politics.
>

Yeah...that too <G>.

> >He believed that
> >his defence was water-tight "I only did what I was told". Not good enough
on
> >my watch, I'm afraid. I want people who will think about what they are
told
> >and keep the overall purpose in mind...)
>
> What you want, Mr Dashwood, and the desires of others just might possibly
> not be the same thing... you may have noticed this.
>

Yes, I have encountered dissent. It is usually an essential part of the
growth process and leads in the end to a better solution. It is not WHO's
right but WHAT's right that is important. Obtaining agreement on what's
right is the job of a good manager.

> >
> >I believe you and I have disagreed on this before, but I'm happy to
explore
> >it again....<G>.
>
> The exploration is a simple one.  A spec is issued.  The programmer speaks
> of concerns and these concerns receive a fair, impartial and dispassionate
> review.

That is a change of position, Doc. Nowhere in the original post did you
grant that a review or question was a good idea. I have no problem with your
re-stated position as it is a fair and reasonable one. The original
statement was not, and prompted this post...


 >After said review a duly-authorised corporate superior states
> that the programmer, as a corporate resource, is to be directed towards
…[3 more quoted lines elided]…
> What is the programmer to do under such conditions?

Once the questioning is done and any observations have been examined, then
management have the right to manage and a direction can be given, which
should be complied with.  In the example you used, there had been no such
provision for question or examination, just the direction to "Do it".

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-30T09:15:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8oi93$fdk$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eaf90f5_1@127.0.0.1>`

```
In article <3eaf90f5_1@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b8na20$roe$1@panix1.panix.com...
…[24 more quoted lines elided]…
>New York...<G>.

Thanks much for that clarification, Mr Dashwood; as I understood the 
Nuremburg defense it was invoked by soldiers who were performing illegal 
acts under direct military orders.

>> >
>> >As somebody who frequently prepares specs for programmers, I am pleased if
…[13 more quoted lines elided]…
>provision for question or examination, just the direction to "Do it".

Thanks for the clarification, Mr Dashwood.

[snippage of repetition]

>
>> >
…[10 more quoted lines elided]…
>Yeah...that too <G>.

So I noticed, aye.

>
>> >He believed that
…[11 more quoted lines elided]…
>right is the job of a good manager.

Mr Dashwood, getting people to work together in order to resolve a 
difficulty is part of the job of *any* manager... and yet many seem to see 
it easier to accomplish this task by asking 'Who is responsible for this?' 
instead of 'Who can fix this?'

>
>> >
…[8 more quoted lines elided]…
>grant that a review or question was a good idea.

Nowhere did I rule it out, either, Mr Dashwood.

>I have no problem with your
>re-stated position as it is a fair and reasonable one. The original
>statement was not, and prompted this post...

Mr Dashwood, my apologies for 'cutting to the chase' and leaving out steps 
which cause such confusion but again, nowhere was even the possibility of 
such a review ruled out.  Notice I didn't include any mention of 
coffee-breaks, either... and a good thing, too, as I didn't mention 
bathroom-breaks!

>
>
…[10 more quoted lines elided]…
>provision for question or examination, just the direction to "Do it".

Oh, I *cannot* resist...

... before or after a coffee-break?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-01T01:27:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eafcf43_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eaf90f5_1@127.0.0.1> <b8oi93$fdk$1@panix1.panix.com>`

```
ROFL!

I never thought I'd see the day...

A totally unworthy response Doc; I expected more from you...<G>

"Nowhere did I rule it out "....

You know as well as I do that your position was untenable so you changed it.

It really doesn't matter, but when others do exactly that here, you are
merciless...

OK, I'll let it go and the readership can draw their own conclusions...<G>

Pete.


<docdwarf@panix.com> wrote in message news:b8oi93$fdk$1@panix1.panix.com...
> In article <3eaf90f5_1@127.0.0.1>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:b8na20$roe$1@panix1.panix.com...
> >> In article <3eaf1a9b_2@127.0.0.1>,
> >> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> >> >> unambiguous and direct instructions are given for the programmer to
code
> >> >> an ABEND.  What do you think a programmer should do when given a
clear,
> >> >> unambiguous, direct and legal instruction by a duly-authorised
corporate
> >> >> superior?
> >> >>
> >> >That looks like the Nuremburg defence to me, Doc...<G>
> >>
> >> Ummmmm... last I looked 'corporate' was a civilian entity, not a
military
> >> one.
> >>
> >
> >I use the term "Nuremburg defence" as a generic term for this type opf
> >defence. It doesn't matter whether it is Civil or Military exactly as
your
> >"Brooklyn Bridge" defence is a generic one, and not limited to residents
of
> >New York...<G>.
>
…[5 more quoted lines elided]…
> >> >As somebody who frequently prepares specs for programmers, I am
pleased if
> >> >they question something that doesn't look good to them.
> >>
> >> Once the questioning is done there may come a point where a
> >> duly-authorised corporate superior gives a programmer a clear,
> >> unambiguous, direct and legal instruction as to the functioning a
program
> >> is to be written to perform.  What do you think a programmer should do
> >> then?
…[3 more quoted lines elided]…
> >Once the questioning is done and any observations have been examined,
then
> >management have the right to manage and a direction can be given, which
> >should be complied with.  In the example you used, there had been no such
…[8 more quoted lines elided]…
> >> >I am also extremely pissed off when a guy codes something which he
KNOWS is
> >> >not going to work "because the spec said to do so..." (I have actually
fired
> >> >one guy for doing this. He had a personality problem with a particular
> >> >Analyst and was prepared to bring production to a standstill to make
the guy
> >> >look bad... I can't use guys with that kind of attitude.
> >>
…[10 more quoted lines elided]…
> >> >his defence was water-tight "I only did what I was told". Not good
enough on
> >> >my watch, I'm afraid. I want people who will think about what they are
told
> >> >and keep the overall purpose in mind...)
> >>
> >> What you want, Mr Dashwood, and the desires of others just might
possibly
> >> not be the same thing... you may have noticed this.
> >>
…[13 more quoted lines elided]…
> >> >I believe you and I have disagreed on this before, but I'm happy to
explore
> >> >it again....<G>.
> >>
> >> The exploration is a simple one.  A spec is issued.  The programmer
speaks
> >> of concerns and these concerns receive a fair, impartial and
dispassionate
> >> review.
> >
…[19 more quoted lines elided]…
> >> the clear, unambiguous and legal action of coding an ABEND in the
program
> >> for a certain set of conditions.
> >>
> >> What is the programmer to do under such conditions?
> >
> >Once the questioning is done and any observations have been examined,
then
> >management have the right to manage and a direction can be given, which
> >should be complied with.  In the example you used, there had been no such
…[7 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-30T10:32:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8ompp$d89$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf90f5_1@127.0.0.1> <b8oi93$fdk$1@panix1.panix.com> <3eafcf43_2@127.0.0.1>`

```
In article <3eafcf43_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>ROFL!
>
>I never thought I'd see the day...
>
>A totally unworthy response Doc; I expected more from you...<G>

Blessed is one who expects nothing, Mr Dashwood, as disappointment is 
rare.

>
>"Nowhere did I rule it out "....
>
>You know as well as I do that your position was untenable so you changed it.

Mr Dashwood, I explicitly stated that I was 'cutting to the chase'; your 
concern was that I did not 'grant that a review or question was a good 
idea'.  As the posting demonstrates it was as much 'granted that it was a 
good idea' as it was 'ruled out'; sentiment can fall with equal grace on 
either side of that particular debate.

>
>It really doesn't matter, but when others do exactly that here, you are
>merciless...

Mr Dashwood, that is, I believe, incorrect; an example of what you see as 
a lack of 'mercy' might prove instructive.

>
>OK, I'll let it go and the readership can draw their own conclusions...<G>

How generous of you, Mr Dashwood... might they take a coffee-break first?

DD

><docdwarf@panix.com> wrote in message news:b8oi93$fdk$1@panix1.panix.com...
>> In article <3eaf90f5_1@127.0.0.1>,
…[133 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-01T10:35:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb0d452.566979012@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:


>The exploration is a simple one.  A spec is issued.  The programmer speaks 
>of concerns and these concerns receive a fair, impartial and dispassionate 
…[3 more quoted lines elided]…
>for a certain set of conditions.

Your description is discrepant with reality in the world of formal methodology.
You are describing military and small company environments where methodology is
absent, so order comes from social/management strata. 

One might ask why even write a programming spec? Some organizations don't. There
are two reasons: 

1. Training for junior programmers.
 
2. The client has old-timers who might say, 'How can you expect them to get it
right without programming specs? Harumph. In my day we always had clear marching
orders and rules of engagement.' So we produce something that looks like a
programming spec to appease them. Programming specs are unimportant within the
methedology model,
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-01T14:07:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8r9nt$7u2$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net>`

```

On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >The exploration is a simple one.  A spec is issued.  The programmer speaks
> >of concerns and these concerns receive a fair, impartial and dispassionate
…[8 more quoted lines elided]…
> is absent, so order comes from social/management strata.

Every shop I have worked in with a formal methodology has had strict rules for
coding.   Most every one has at least one rule that I disagreed with.  My
current shop has at least two rules that you disagree with.   A formal
methodology doesn't mean that you won't have explicit instructions to code
something that you don't believe is proper.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T10:27:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb19f64_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b8r9nt$7u2$1@peabody.colorado.edu...
>
> On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:
>
>
> Every shop I have worked in with a formal methodology has had strict rules
for
> coding.

Interesting.

How strict?

Like, if I code a GO TO do I get fired?

Who polices it?

At what point? While I am still developing it? Or, by review after it has
gone live? If it is successfully working in production, will they pull it
back and demand the offending GO TO be removed, in order to comply with the
standard? (see "How strict?", above)

I ask these questions because, over the years, I have been responsible for
the implementation of style based standards in a number of shops. My
experience has been that the adoption of a strict authoritarian approach is
counter productive and simply lowers morale and stifles enthusiasm.

The best way to implement coding standards is by discussion and consensus.
They should never be "carved in stone". If the team find that a particular
standard hampers their work it should be reviewed. I have used examples, and
encouragement towards a sensible set of standards (rather than "You WILL do
this. It is mandatory on this site"), always recognising that style is a
matter of preference, but we need to standardise the approach to facilitate
maintaining each other's work.

I also believe that an Annexe to the standards called "Useful code examples"
is an essential part of any shop standard. Anyone on the team who has
developed a method for doing a fairly common task should be encouraged to
review their approach with a senior programmer and then the code can be
posted to this annexe (and placed on the system as a COPY book, if
appropriate...).


>  Most every one has at least one rule that I disagreed with.  My
> current shop has at least two rules that you disagree with.   A formal
> methodology doesn't mean that you won't have explicit instructions to code
> something that you don't believe is proper.

Yep, there is usually something that someone is not comfortable with.
However, if the pros and cons are openly discussed and everyone gets a
chance to make their objections known, then at least they work with it on
the understanding that the majority of the team think it is a good thing.

As is a matter of record here <G>, I actually encourage dissent (for a
limited period, and under specific circumstances) as it is a good way to
cause all concerned to re-evaluate their agreements or objections. However,
once we have decided that something is "in", then there is no place for
smouldering resentment or mutterings under the breath...<G> You win some;
you lose some. I have worked, and coded in compliance with, standards which
I personally thought were clumsy and unwieldy, but I had my chance to make a
case and failed to persuade my colleagues.

The overall morale of the shop is MUCH more important than the autocratic
insistence on "Holy Writ".

Standards are better implemented as guidelines, with the site priorities
spelled out on page one. (For example, is it more important to comply with
the standard than for the code to be efficient? Does the fact that code
works, outweigh the fact that it may have minor standard violations in it?
Etc.)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T14:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tuka$i10$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1>`

```

On  1-May-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> Interesting.
>
> How strict?

It varies.

> Like, if I code a GO TO do I get fired?

Not immediately.   But oddly enough I don't recall that being an enforced
standard.

> Who polices it?

The most strict standards checking is done by whomever migrates the job to
production.   These checks are generally according to guidelines that don't
really matter much to the way the code works.   But they're easy to check.

"Easy to check" seems to be the most important criterion.

I forgot how EDS enforced their requirement about exit paragraphs.   But it was
a requirement, and we followed it.


> I ask these questions because, over the years, I have been responsible for
> the implementation of style based standards in a number of shops. My
> experience has been that the adoption of a strict authoritarian approach is
> counter productive and simply lowers morale and stifles enthusiasm.

I mostly agree.  I have seen shops that required that sorts be either internal
or external (depending on the shop).   If there was a real good reason for going
against the standard, you could appeal your design.

But when a shop said "Your JCL should use these sort work files", I told them
that this is all done dynamically now - is anybody authorized to change this
standard.   Nobody was, so I followed their standard.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T03:03:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb2fc7e.21095380@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

I too have established style standards at a number of shops ..about 7. My
technique is based primarily on personal interaction rather than written rules. 

I start with a one page document which talks about high level principles and
objectives.  

1.  I deliberately rotate assignments so the programmer assigned to work on a
program today is never the same one who worked on it last time. I make it clear
that if you are writing new code, when it needs maintenance three months hence,
someone else will be assigned to do it. No program 'belongs' to a programmer;
the whole program library is team property. 

Within a few months, a consensus style emerges. You cannot tell from looking at
a program who wrote it. They all look the same, stylistically. Not because
someone shoved a rule book down their throats; because they developed the style
themselves. 

A standing rule says everyone has permission to rewrite a section of code purely
to improve its style. Of course, he must retest that section if the change is
more than trivial. This is contrary to the policy in most shops, which prohibits
changes that are not relevant to the assignment. It is supported by my high
level objective saying we want the highest quality source code that we're
capable of producing. 

None of the de-facto standards were written down. I didn't want them to be for
fear they'd become immutable. Standards should be permitted to evolve. 

2. I put in place a precompiler that was  mandatory for both test and
production. It did two things. It beautified code by lining up pics, doing
indentation, etc. Those things are trivial. Its second function and real reason
for being was to grade each program for quality. It inserted the grade as a
comment in identification division. I don't say a word about it until they ask. 

Programmers soon asked what the criteria were. I'd tell them it's a measure of
expressiveness and lack of redundancy. Expressiveness is a function of average
data name size (on some kind of log scale, I don't remember the details);
redundancy is measured by assigning points to verbs. Those which create new
information, either data or logical state, get the highest points -- if,
compute, etc. Those which merely shuffle data or control around -- move, perform
-- get medium-low points. Verbs I don't like -- go to, more than one goback --
get zero points. The average verb score goes into the program grade. 

Within weeks, all programs are scoring 100. Again, not because I shoved precepts
down their throats but because I appealed to their sense of pride. 
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-03T21:24:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb38ad1_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1> <3eb2fc7e.21095380@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb2fc7e.21095380@news.optonline.net...
<snip>

This sounded to me like a very effective approach, Robert.

You are right that it could only work with the right people and, sometimes,
we just don't have the luxury of getting the people we would like.

Nevertheless, a less than Authoritarian approach will bring out the best in
most people.

I was kind of amused that you would go so far as to rate code by the use of
verbs, but it is an interesting idea.

I wouldn't do it myself because it smacks of covert appraisal and I believe
that appraisals should be overt, but, as you found it to be useful, I won't
make judgements one way or the other.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T15:39:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB4290B.3040309@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1> <3eb2fc7e.21095380@news.optonline.net>`

```
Robert Wagner wrote:
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> 
> I too have established style standards at a number of shops ..about 7. My
> technique is based primarily on personal interaction rather than written rules. 

8<----- snip ------

This sounds pretty cool - Could you post (or e-mail) these rankings, and 
how you came up with the algorithm to average them?  I'd be interested 
in seeing how you did it.  :)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:10:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95utg$po0$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1> <3eb2fc7e.21095380@news.optonline.net>`

```

On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:

> Programmers soon asked what the criteria were. I'd tell them it's a measure of
> expressiveness and lack of redundancy. Expressiveness is a function of average
…[10 more quoted lines elided]…
> down their throats but because I appealed to their sense of pride.

I liked everything you said until this quote.   Programs such as this don't
measure quality of the program, except as how the program should fit a
particular style.   Once people know what the objective is, they can easily
change their style to what they think their boss wants.   That doesn't mean they
have pride in having a better program, it means they want to look good when
evaluations come up.   Do they really believe that changing the data name size
to the pre-determined optimum makes the program better?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-06T09:14:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb77cdc.119309351@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1> <3eb2fc7e.21095380@news.optonline.net> <b95utg$po0$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:
>
>> Programmers soon asked what the criteria were. I'd tell them it's a measure
of
>> expressiveness and lack of redundancy. Expressiveness is a function of
average
>> data name size (on some kind of log scale, I don't remember the details);
>> redundancy is measured by assigning points to verbs. Those which create new
…[3 more quoted lines elided]…
>> -- get medium-low points. Verbs I don't like -- go to, more than one goback
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-06T14:20:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b98gc0$6tl$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb19f64_2@127.0.0.1> <3eb2fc7e.21095380@news.optonline.net> <b95utg$po0$1@peabody.colorado.edu> <3eb77cdc.119309351@news.optonline.net>`

```

On  6-May-2003, robert@wagner.net (Robert Wagner) wrote:

> I would have preferred to use a spelling cheeker, but didn't have one at the
> time. The objective was to get rid of abbreviations such as DP, DPT and DEPT.
> They don't save time, they slow you down because they make you look at the
> data description to see how it is spelled *this* time

I've never seen this problem eliminated entirely.  The trouble is, once you buy
some software, we are stuck with multiple standards.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-02T06:32:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb1f3a3.28224158@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[16 more quoted lines elided]…
>something that you don't believe is proper. 

Those 'shop coding standards' aren't born of modern methodology. They're a
holdover from the past , when they, along with code walkthrus, were all the
quality control we had. They are enforced by Team Leaders who usually have 3-5
years of programming experience. 

Four out of five places where I worked recently did not enforce them. They were
enforced in one shop where COBOL was the primary language; they were not
enforced when the Team Leader didn't know COBOL well. In the one COBOL shop,
Team Leaders supplemented (or contervened) the published standard with their
personal preference.
  
Modern methodologies are oriented toward examining external results. Old
attempts at methodology, designed by programmers, looked inward, thinking
quality could be achieved by self-discipline.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T14:23:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tv0e$i8c$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb1f3a3.28224158@news.optonline.net>`

```

On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:

> Those 'shop coding standards' aren't born of modern methodology. They're a
> holdover from the past , when they, along with code walkthrus, were all the
> quality control we had. They are enforced by Team Leaders who usually have 3-5
> years of programming experience.

In my experience, team leaders aren't the enforcers, nor do they have that
limited programming experience.  But my experience quite often disagrees with
the whole world as described by you.


> Modern methodologies are oriented toward examining external results. Old
> attempts at methodology, designed by programmers, looked inward, thinking
> quality could be achieved by self-discipline.

There are some advantages in following a common style in a shop.   Certainly
your "best practices" document supports that people should follow your style.  
If you were king, I suspect you would strongly recommend that your programmers
follow your standards.

And certainly there are practices that we have learned are more prone to
troubles than other practices.   The difficulty for managers is in finding the
fine line between sharing this experience and encouraging innovation.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb415dd.93137469@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8r9nt$7u2$1@peabody.colorado.edu> <3eb1f3a3.28224158@news.optonline.net> <b8tv0e$i8c$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>> quality control we had. They are enforced by Team Leaders who usually have
3-5
>> years of programming experience.
>
>In my experience, team leaders aren't the enforcers, nor do they have that
>limited programming experience.  But my experience quite often disagrees with
>the whole world as described by you.

Was any of your experience at shops with formal methodology? 

When they get methodology, they push obsolete qa controls to the bottom of the
political hierarchy. 

>> Modern methodologies are oriented toward examining external results. Old
>> attempts at methodology, designed by programmers, looked inward, thinking
…[5 more quoted lines elided]…
>follow your standards.

I described how I did it here. I agree that a common style is an important goal.
We disagree on how to achieve it. I believe in voluntary compliance motivated by
teamwork; you seem to support rules imposed from above. 

>And certainly there are practices that we have learned are more prone to
>troubles than other practices.   The difficulty for managers is in finding the
>fine line between sharing this experience and encouraging innovation.

Authoritarian shops are not known for encouraging innovation. But then, routine
programming projects don't NEED innovation; they just follow the established
model.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T12:03:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rggi$ou2$1@panix5.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net>`

```
In article <3eb0d452.566979012@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[8 more quoted lines elided]…
>Your description is discrepant with reality in the world of formal methodology.

No, Mr Wagner, your 'world of formal methodology' seems to be discrepant 
with 'reality'.

I try to use words like 'reality' as little as possible; Greater Minds 
than Mine have argued about this term for millennia.  I use phrases such 
as 'I have seen' and the like... is there *anyone* reading who has not 
seen a situation like this or something similar?

>You are describing military and small company environments where methodology is
>absent, so order comes from social/management strata. 

I am describing what I have seen, Mr Wagner, and what I believe - rightly 
or wrongly - that others have seen.  No matter how it comes about or 
where it is found the question appears to be valid... and you are dodging 
a direct addressing of it a second time.

>
>One might ask why even write a programming spec? Some organizations don't. There
…[8 more quoted lines elided]…
>methedology model,  

One might ask for change of a buck, as well... but I have asked this
particular question twice and twice you have not addressed it.  Third and
final time, then:  A spec is issued.  The programmer speaks of concerns
and these concerns receive a fair, impartial and dispassionate review.  
After said review a duly-authorised corporate superior states that the
programmer, as a corporate resource, is to be directed towards the clear,
unambiguous and legal action of coding an ABEND in the program for a
certain set of conditions.  What is the programmer to do?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-01T16:25:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rhqg$bca$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com>`

```

On  1-May-2003, docdwarf@panix.com wrote:

> One might ask for change of a buck, as well... but I have asked this
> particular question twice and twice you have not addressed it.  Third and
…[5 more quoted lines elided]…
> certain set of conditions.  What is the programmer to do?

I believe he said he would insult the boss, quit, and incite the other
programmers to quit.

Since following employers standards is required in every job, and since few
companies will have standards that are 100% congruent with any given programmer,
I expect he has done this many, many times in his long career.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T14:02:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rneo$k99$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <b8rhqg$bca$1@peabody.colorado.edu>`

```
In article <b8rhqg$bca$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-May-2003, docdwarf@panix.com wrote:
…[11 more quoted lines elided]…
>programmers to quit.

Aye, that he did... I found that and responded in a separate posting.

>
>Since following employers standards is required in every job, and since few
>companies will have standards that are 100% congruent with any given programmer,
>I expect he has done this many, many times in his long career.

I try to keep my expectations small so as to decrease disappointment... 
and Mr Wagner has shown a tendency towards double-standards in the past.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T10:33:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb1a0c9$1_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <b8rhqg$bca$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b8rhqg$bca$1@peabody.colorado.edu...
>
> On  1-May-2003, docdwarf@panix.com wrote:
>
> > One might ask for change of a buck, as well... but I have asked this
> > particular question twice and twice you have not addressed it.  Third
and
> > final time, then:  A spec is issued.  The programmer speaks of concerns
> > and these concerns receive a fair, impartial and dispassionate review.
> > After said review a duly-authorised corporate superior states that the
> > programmer, as a corporate resource, is to be directed towards the
clear,
> > unambiguous and legal action of coding an ABEND in the program for a
> > certain set of conditions.  What is the programmer to do?
…[3 more quoted lines elided]…
>
I didn't see that!

Good answer! (If you are determined not to make a career in commercial
computer programming...<G>)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T03:03:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb30685.23662985@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <b8rhqg$bca$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  1-May-2003, docdwarf@panix.com wrote:
…[14 more quoted lines elided]…
>companies will have standards that are 100% congruent with any given
programmer,
>I expect he has done this many, many times in his long career.

I've never resigned for reasons remotely close to shop standards. The reason has
usually been because the company was close to bankruptcy. As an insider with
access to financial statements I can see it coming. Every company I've worked
for (as a perm)  has gone belly up. In most cases, I resigned a year before the
end. 

For 25 years, I was the manager who wrote the standards (see my reply to PEC
Dashwood for more on this). For another ten years I was independent, developing
tools, an operating system and OEM stuff, using my own standards. Only in the
last five years, as a contractor,  have I worked in shops using someone else's
standards. They all had formal methodologies such as CMM and ISO9000, which are
oriented toward results rather than navel gazing. In these shops, the old
standards were seen as anachonisms .. something held over from the past. They
were not enforced. 

Is it possible you've worked only in medium sized shops using methodology from
the '80s?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-05-03T08:37:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdLsa.18836$8e7.801918@twister.austin.rr.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <b8rhqg$bca$1@peabody.colorado.edu> <3eb30685.23662985@news.optonline.net>`

```
Occam's razor might apply here - please do not apply to work in my shop! :)
:) :)

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb30685.23662985@news.optonline.net...
> I've never resigned for reasons remotely close to shop standards. The
reason has
> usually been because the company was close to bankruptcy. As an insider
with
> access to financial statements I can see it coming. Every company I've
worked
> for (as a perm)  has gone belly up. In most cases, I resigned a year
before the
> end.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb41a1c.94225007@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <b8rhqg$bca$1@peabody.colorado.edu> <3eb30685.23662985@news.optonline.net> <gdLsa.18836$8e7.801918@twister.austin.rr.com>`

```
I prefer Groucho Marx's explanation, when he said "I wouldn't want to belong to
a club that would admit someone like me." :)

Making an autodidact manager is probably a bad idea, in general. They got lucky
with me, but struck out with other managers. 


"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:

>Occam's razor might apply here - please do not apply to work in my shop! :)
>:) :)
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T10:31:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb1a05d$1_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eaf1a9b_2@127.0.0.1> <b8na20$roe$1@panix1.panix.com> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b8rggi$ou2$1@panix5.panix.com...
> In article <3eb0d452.566979012@news.optonline.net>,
> Robert Wagner <robert@wagner.net> wrote:
…[10 more quoted lines elided]…
>

For Chrissake, Robert, answer his question <G>.

It is now clear and unequivocal...

The programmer under these circumstances (in my opinion) has two choices:

1. Comply.

2. Walk.

How hard is that <G>?

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T23:14:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8snr3$snp$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <3eb1a05d$1_2@127.0.0.1>`

```
In article <3eb1a05d$1_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b8rggi$ou2$1@panix5.panix.com...
…[16 more quoted lines elided]…
>It is now clear and unequivocal...

Is it clear, Mr Dashwood... even without mentioning coffee-breaks?  Mr 
Wagner did answer, in another posting.

>
>The programmer under these circumstances (in my opinion) has two choices:
…[5 more quoted lines elided]…
>How hard is that <G>?

It neglects refusing to comply (which leaves the organisation several 
alternatives)... or inciting to disaffection (one of Mr Wagner's 
suggestions.

I am certain there are other alternatives which minds better than mine
might be able to supply.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T20:27:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb22bfe_1@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0d452.566979012@news.optonline.net> <b8rggi$ou2$1@panix5.panix.com> <3eb1a05d$1_2@127.0.0.1> <b8snr3$snp$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b8snr3$snp$1@panix1.panix.com...
> In article <3eb1a05d$1_2@127.0.0.1>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:b8rggi$ou2$1@panix5.panix.com...
> >> In article <3eb0d452.566979012@news.optonline.net>,
> >

I have since seen his response which I have also responded to...

> >The programmer under these circumstances (in my opinion) has two choices:
> >
…[9 more quoted lines elided]…
>
No it doesn't...they are all covered under "Walk".

I was just following your example and "cutting to the chase"
<G>...Surprised you didn't pick that up...

> I am certain there are other alternatives which minds better than mine
> might be able to supply.
>

I doubt it...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-02T08:17:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tnl5$nr8$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1a05d$1_2@127.0.0.1> <b8snr3$snp$1@panix1.panix.com> <3eb22bfe_1@127.0.0.1>`

```
In article <3eb22bfe_1@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b8snr3$snp$1@panix1.panix.com...
…[25 more quoted lines elided]…
><G>...Surprised you didn't pick that up...

Silly me... when you stated a specific number and repeated it I thought 
you were maintaining the finitude you established.

>
>> I am certain there are other alternatives which minds better than mine
…[3 more quoted lines elided]…
>I doubt it...<G>

Well, then... what's Life without a bit of Uncertainty?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-04-30T11:18:10+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mf1vavk5scc76t2k0jv0rhoic1hq6d7eah@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1>`

```
On Wed, 30 Apr 2003 12:36:36 +1200 "Peter E.C. Dashwood"
<dashwood@enternet.co.nz> wrote:

   [ snipped ]

:>As a programmer, I have frequently questioned specs presented by a
:>"duly-authorised corporate superior" and they are usually glad I did.

:>I am also extremely pissed off when a guy codes something which he KNOWS is
:>not going to work "because the spec said to do so..." (I have actually fired
:>one guy for doing this. He had a personality problem with a particular
:>Analyst and was prepared to bring production to a standstill to make the guy
:>look bad... I can't use guys with that kind of attitude. He believed that
:>his defence was water-tight "I only did what I was told". 

I did that.

Of course I told the analyst and his supervisor about the problem but they
chose to keep their heads in the send.

I coded it as designed and it worked as designed.

When the condition that I warned about occurred it still worked as designed
but did not produce the desired results. I had the paper trail that showed
that I had indicated the problem.

:>                                                          Not good enough on
:>my watch, I'm afraid. I want people who will think about what they are told
:>and keep the overall purpose in mind...)

I was good enough that I wasn't asked to be a pure "coder" again.

   [ snipped ]
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-30T21:09:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaf92c0_1@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eaf1a9b_2@127.0.0.1> <mf1vavk5scc76t2k0jv0rhoic1hq6d7eah@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
news:mf1vavk5scc76t2k0jv0rhoic1hq6d7eah@4ax.com...
> On Wed, 30 Apr 2003 12:36:36 +1200 "Peter E.C. Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> :>I am also extremely pissed off when a guy codes something which he KNOWS
is
> :>not going to work "because the spec said to do so..." (I have actually
fired
> :>one guy for doing this. He had a personality problem with a particular
> :>Analyst and was prepared to bring production to a standstill to make the
guy
> :>look bad... I can't use guys with that kind of attitude. He believed
that
> :>his defence was water-tight "I only did what I was told".
>
…[4 more quoted lines elided]…
>

Then you did what is correct and professional. Having discharged your duty,
you can then code their solution with a clear conscience.

> I coded it as designed and it worked as designed.
>
> When the condition that I warned about occurred it still worked as
designed
> but did not produce the desired results. I had the paper trail that showed
> that I had indicated the problem.

Excellent! I would have no problem with a programmer who behaved in that
way. (I'd probably have a quiet word to the Analyst concerned, though <G>)
>
> :>                                                          Not good
enough on
> :>my watch, I'm afraid. I want people who will think about what they are
told
> :>and keep the overall purpose in mind...)
>
> I was good enough that I wasn't asked to be a pure "coder" again.

They were stupid to expect you to be so in the first place...

I have worked on some sites where the management simply don't recognise and
utilise the value of the people they have. Usually these managers are very
insecure because they have no personal technical background, do not
understand what the people they are managing have to do, and substitute the
"Rule of Fear" or Authoritarianism as a means of keeping control. These are
very unpleasant places to work and it is hardly surprising that morale and
productivity both suffer accordingly.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-30T17:20:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eafd941.502695520@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3eadb031.361090998@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[29 more quoted lines elided]…
>>Programs should be organized like corporations, with decisions made at high
and
>>intermediate levels of management, grunt work done at low levels. Grunts
>>shouldn't make major decisions like aborting the job.
…[4 more quoted lines elided]…
>>manager will cave today, that might change tomorrow when a new manager takes
his
>>place. 
>
…[10 more quoted lines elided]…
>superior?

In environments with a formal methodology, there isn't a single 'program spec'.
There are at least three levels of documentation, usually more:

1.  Business requirements. Written by a manager.
2.  High level design. Written by a systems analyst. Contains no 'technical
stuff' such as record layouts or abends. It is written in English rather than
jargon.
3.  Low level program spec. Usually written by an intern or junior programmer.
This one is full of technical detail, sometimes has pseudo-code. 

The programmer can use the low level spec or ignore it. Low level specs are
often full of errors. When there is a question about what the change is intended
to accomplish, the high level design is 'the bible'. If there is a conflict
between high level design and business requirement (this happens rarely), the
business requirement prevails. 

Although they are formally structured, these environments do not have the
authoritarian attitude you describe. 'Do as you're told and shut up' is found in
UNstructued environments, where order comes from personal relationships because
better tools are absent.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-30T15:01:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8p6it$r8a$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net>`

```
In article <3eafd941.502695520@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[74 more quoted lines elided]…
>better tools are absent. 

Mr Wagner, that is all well and good... but I noticed that something 
rather minor seems to be missing, that being an answer to my question.  
Second time, then: clear, unambiguous and direct instructions are given 
for the programmer to code an ABEND.

(Note, Mr Wagner, that 'specs' are not mentioned, 'environments' are not 
mentioned, organisational structures are not mentioned.  Addressing such 
matters would seem to be irrelevant.)

What do you think a programmer should do when given a clear, unambiguous,
direct and legal instruction by a duly-authorised corporate superior?

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-04-30T22:41:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0304302141.47b7b970@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com>`

```
I don't get the tap dancing on this issue. 

If there's a conflict between what's right and what's written, you go
to the guy/gal you report to and explain the situation, with or w/o
your opinion and get a decision. If (s)he can't make it, it's on up to
the next level for them.

If the decision goes against you, you update the scorecard. If the bad
guys are way ahead and you think it's time to say "adios", you dust
off the resume, or you think not, and you keep your mouth shut and
just keep on keepin on.

Regards, Jack.    

docdwarf@panix.com wrote in message news:<b8p6it$r8a$1@panix1.panix.com>...
> In article <3eafd941.502695520@news.optonline.net>,
> Robert Wagner <robert@wagner.net> wrote:
…[90 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-01T21:41:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb0ebcc_1@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com>`

```
I'd be honoured to have you working on my team, Jack <G>.

Succinct and accurate.

Pete.

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0304302141.47b7b970@posting.google.com...
> I don't get the tap dancing on this issue.
>
…[12 more quoted lines elided]…
> docdwarf@panix.com wrote in message
news:<b8p6it$r8a$1@panix1.panix.com>...
> > In article <3eafd941.502695520@news.optonline.net>,
> > Robert Wagner <robert@wagner.net> wrote:
…[12 more quoted lines elided]…
> > >>>>When I come across a catastrophic error (e.g. major FILE STATUS
issue)
> > >>>>I have no probs with displaying related info and doing an immediate
> > >>>>STOP RUN or GO TO a shutdown routine.  I mean, there ain't any
further
> > >>>>processing to be done, so why bother (for example) setting a switch
to
> > >>>>indicate that the end of the world has actually arived (as far as
the
> > >>>>program is concerned) and then have to test for it in higher-level
> > >>>>logic.
> > >>>
> > >>>That's like giving a file clerk authority to declare the company
bankrupt
> > >>>because she finds the file drawer jammed shut. Within her narrow
perspective,
> > >>>it's an 'unrecoverable error'.
> > >>>
> > >>>Perhaps someone higher up can recover from the condition by
dispatching a
> > >>>repairperson (VERIFY). Perhaps the file was 'optional' and the
program can
> > >>>operate without it.
> > >>
> > >>... or perhaps the problem is beyond the scope of a VERIFY, perhaps
the
> > >>file is 'mandatory' and maybe the Ops crew needs to wake up on-call
> > >>support at 3:am just to check the readability of the source-code.
> > >>
> > >>>
> > >>>Programs should be organized like corporations, with decisions made
at high
> >  and
> > >>>intermediate levels of management, grunt work done at low levels.
Grunts
> > >>>shouldn't make major decisions like aborting the job.
> > >>
…[3 more quoted lines elided]…
> > >>>manager will cave today, that might change tomorrow when a new
manager takes
> >  his
> > >>>place.
> > >>
> > >>... or it might not.  Meanwhile the program has to be written and the
> > >>Business Analyst has demanded that if the file containing the dates
for
> > >>business holidays is not found when it is opened then the program's
> > >>calculations of intervening business days will be invalid so the
program
> > >>should be ABENDed and re-run after further research.
> > >>
> > >>In this case - and not a few others like it, Mr Wagner - clear,
> > >>unambiguous and direct instructions are given for the programmer to
code
> > >>an ABEND.  What do you think a programmer should do when given a
clear,
> > >>unambiguous, direct and legal instruction by a duly-authorised
corporate
> > >>superior?
> > >
> > >In environments with a formal methodology, there isn't a single
'program spec'.
> > >There are at least three levels of documentation, usually more:
> > >
> > >1.  Business requirements. Written by a manager.
> > >2.  High level design. Written by a systems analyst. Contains no
'technical
> > >stuff' such as record layouts or abends. It is written in English
rather than
> > >jargon.
> > >3.  Low level program spec. Usually written by an intern or junior
programmer.
> > >This one is full of technical detail, sometimes has pseudo-code.
> > >
> > >The programmer can use the low level spec or ignore it. Low level specs
are
> > >often full of errors. When there is a question about what the change is
intended
> > >to accomplish, the high level design is 'the bible'. If there is a
conflict
> > >between high level design and business requirement (this happens
rarely), the
> > >business requirement prevails.
> > >
> > >Although they are formally structured, these environments do not have
the
> > >authoritarian attitude you describe. 'Do as you're told and shut up' is
found in
> > >UNstructued environments, where order comes from personal relationships
because
> > >better tools are absent.
> >
…[9 more quoted lines elided]…
> > What do you think a programmer should do when given a clear,
unambiguous,
> > direct and legal instruction by a duly-authorised corporate superior?
> >
> > DD




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T12:06:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rglk$p9j$1@panix5.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com>`

```
In article <8a2d426e.0304302141.47b7b970@posting.google.com>,
Jack Sleight <jacksleight@hotmail.com> wrote:
>I don't get the tap dancing on this issue. 

Mr Sleight, I do not believe that I am tapdancing... but it may be that 
someone else is; it takes two to *tango*, as I recall.

>
>If there's a conflict between what's right and what's written, you go
…[7 more quoted lines elided]…
>just keep on keepin on.

How utterly... pragmatic!  Mr Sleight, doesn't the world of Formal 
Methodology, Sigma Six or Whang-Dang-Doodle-Dooh-Dah figure into this at 
*all*?

DD
>
>docdwarf@panix.com wrote in message news:<b8p6it$r8a$1@panix1.panix.com>...
…[92 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-02T06:32:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb1fde5.30851164@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com>`

```
jacksleight@hotmail.com (Jack Sleight) wrote:

>I don't get the tap dancing on this issue. 
>
…[8 more quoted lines elided]…
>just keep on keepin on.

You just descibed a hierarchical organization. In my experience, the decision
process has been networked. You and your supervisor together go to a systems
analyst or Subject Matter Expert, who makes a determination based on facts and
policy rather than politics. He usually has the courtesy to explain the decision
by citing relevant documents. The consultation is often done via email rather
than in person. 

>docdwarf@panix.com wrote in message news:<b8p6it$r8a$1@panix1.panix.com>...
>> In article <3eafd941.502695520@news.optonline.net>,
…[22 more quoted lines elided]…
>> >>>because she finds the file drawer jammed shut. Within her narrow
perspective,
>> >>>it's an 'unrecoverable error'. 
>> >>>
…[9 more quoted lines elided]…
>> >>>Programs should be organized like corporations, with decisions made at
high
>>  and
>> >>>intermediate levels of management, grunt work done at low levels. Grunts
…[5 more quoted lines elided]…
>> >>>manager will cave today, that might change tomorrow when a new manager
takes
>>  his
>> >>>place. 
…[13 more quoted lines elided]…
>> >In environments with a formal methodology, there isn't a single 'program
spec'.
>> >There are at least three levels of documentation, usually more:
>> >
>> >1.  Business requirements. Written by a manager.
>> >2.  High level design. Written by a systems analyst. Contains no 'technical
>> >stuff' such as record layouts or abends. It is written in English rather
than
>> >jargon.
>> >3.  Low level program spec. Usually written by an intern or junior
programmer.
>> >This one is full of technical detail, sometimes has pseudo-code. 
>> >
>> >The programmer can use the low level spec or ignore it. Low level specs are
>> >often full of errors. When there is a question about what the change is
intended
>> >to accomplish, the high level design is 'the bible'. If there is a conflict
>> >between high level design and business requirement (this happens rarely),
the
>> >business requirement prevails. 
>> >
>> >Although they are formally structured, these environments do not have the
>> >authoritarian attitude you describe. 'Do as you're told and shut up' is
found in
>> >UNstructued environments, where order comes from personal relationships
because
>> >better tools are absent. 
>> 
…[12 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-02T08:28:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8to8h$qql$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net>`

```
In article <3eb1fde5.30851164@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>jacksleight@hotmail.com (Jack Sleight) wrote:
>
…[15 more quoted lines elided]…
>policy rather than politics.

This seems a sidestep, Mr Wagner... whether it is one's direct supervisor 
giving a clear, direct, unambiguous and legal instruction or a systems 
analyst giving a clear, direct, unambiguous and legal instruction or a 
'Subject Matter Expert' giving a clear, direct, etc...

... and whether the determination is made before or after a discussion, or 
a coffee-break or a take-out Chinese lunch of K'ung Pao Brocolli... or 
before or after a discussion of the merits of various schools of 
programming structure...

... it boils down to something asking a programmer to do something which
said programmer Just Doesn't Like.  In this case - a GO TO directing
program execution to an -ABEND routine - the matter involved is one of
'mere style' but that is the heart of the matter: someone with the
authorisation to direct the use of a programmer's time as a corporate
resource directs the programmer to do something said programmer Just 
Doesn't Like.

How does one respond to being told to do something one Just Doesn't Like?  
That, of course, depends on the someone.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T13:13:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB406BA.3020201@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> How does one respond to being told to do something one Just Doesn't Like?  

As a military member, I believe the appropriate response is "Sir, yes sir!"

(They have a special term for when people "just leave" when they don't 
like something...)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-03T20:17:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB4203A.8AEEEC5D@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net>`

```


LX-i wrote:

> docdwarf@panix.com wrote:
> > How does one respond to being told to do something one Just Doesn't Like?
>
> As a military member, I believe the appropriate response is "Sir, yes sir!"
>

Agreed. It comes out sounding like above, but as an ex-military man I was
always mentally spelling it as :-

                "Cur, yes cur ! Three bags full cur !".

BTW - are you actually in uniform or are you a 'civvy'. Long after I left the
RAF my boss an ex-airman (your PFC) and yours truly an ex-sergeant - we both
visited a military training establishment at Blandford Forum in Dorset.
Primarily run by two RAF flight lieutenants (Education branch).

The students were 'hossifers' from all three services primarily being trained
as analysts; possibly with some programming being thrown in. Can't have
officers and gentlemen dirtying their hands - onerous tasks such as operating
the computer - that was left to a hariy-assed RAF flight sergeant and his
minions, corporals and a bunch of AC-plonks !

The two flight-lewies latched on to the fact that the visiting duo were ex RAF
- but the rules of gentlemanliness forbade them the opportunity to ask, "So
what were you.....?"

Jimmy
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T17:18:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB4404B.8000203@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <3EB4203A.8AEEEC5D@shaw.ca>`

```
James J. Gavan wrote:
> 
> LX-i wrote:
…[18 more quoted lines elided]…
> Primarily run by two RAF flight lieutenants (Education branch).

I'm in uniform - SSgt (E-5) in the USAF.

> The students were 'hossifers' from all three services primarily being trained
> as analysts; possibly with some programming being thrown in. Can't have
> officers and gentlemen dirtying their hands - onerous tasks such as operating
> the computer - that was left to a hariy-assed RAF flight sergeant and his
> minions, corporals and a bunch of AC-plonks !

In the USAF, the programmers are in the "communications" career field. 
Our current officer in charge (OIC) was over a base communications 
squadron before coming to our shop.  The comm squadron is responsible 
for phones, mobile radio, LAN, etc.  Quite a bit different than what we 
do (systems analysis, design, and lots o' coding).  To his credit, he's 
done a great job, but I think its strange that the career field is that 
broad.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:14:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95v4c$ppt$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <3EB4203A.8AEEEC5D@shaw.ca> <3EB4404B.8000203@Knology.net>`

```

On  3-May-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:

> In the USAF, the programmers are in the "communications" career field.
> Our current officer in charge (OIC) was over a base communications
> squadron before coming to our shop.

In 1969 we had two different programming departments.   While awaiting pilot
training I worked in the one that handled the business of running the base.   I
suppose there are more than two now.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T00:31:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb44cb4.4987946@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net>`

```
LX-i <DanielJSNOSPAM@Knology.net> wrote:

>docdwarf@panix.com wrote:
>> How does one respond to being told to do something one Just Doesn't Like?  
>
>As a military member, I believe the appropriate response is "Sir, yes sir!"

I could never muster the preppiness. I'd respond "Whatever you say .. SIR" with
a downward deflection on sir indicating disdain. But then, we in Recon were not
known for military correctness. :)

>(They have a special term for when people "just leave" when they don't 
>like something...)

Civilian?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T19:47:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB46330.5010108@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <3eb44cb4.4987946@news.optonline.net>`

```
Robert Wagner wrote:
> LX-i <DanielJSNOSPAM@Knology.net> wrote:
> 
…[10 more quoted lines elided]…
> known for military correctness. :)

I'm the only person in my shop who's not retired military.  They're all 
at least retired MSgt (E-7), my supervisor (currently GS-12) is a 
retired SMSgt (E-8), and one of the contractors is a retired LtCol 
(O-5).  So, although I'm the only military, I'm still expected to be 
courteous.

Of course, they're all pretty laid back - most of the "directives" that 
I end up having to "shut up and color" on are from outside our office. 
It's not too back - heck, I've stayed here over 5 years, and am about 
the only military person in our office (our shop + all other on the 
project) who wouldn't love to PCS...

>>(They have a special term for when people "just leave" when they don't 
>>like something...)
> 
> 
> Civilian? 

I was thinking more "AWOL"...  :)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T20:58:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b91oiv$p2p$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net>`

```
In article <3EB406BA.3020201@Knology.net>,
LX-i  <DanielJSNOSPAM@Knology.net> wrote:
>docdwarf@panix.com wrote:
>> How does one respond to being told to do something one Just Doesn't Like?  
>
>As a military member, I believe the appropriate response is "Sir, yes sir!"

Leaving aside the response I, and many others, have employed of 'Not 
'sir', 'sergeant'... *my* parents were married!'...

... even if the one doing the telling is of a lower rank?

>
>(They have a special term for when people "just leave" when they don't 
>like something...)

I think folks who can do that are called 'civilians'.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T20:23:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB46B79.2080108@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3EB406BA.3020201@Knology.net>,
> LX-i  <DanielJSNOSPAM@Knology.net> wrote:
…[11 more quoted lines elided]…
> .... even if the one doing the telling is of a lower rank?

heh - actually, I've only met one person like that since I've been in... 
  We even called our Training Instructors "sir" and "ma'am" in BMT.  I 
hadn't heard "my parents were married", but I have heard "I work for a 
living".  :)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** Jeff York <pogo50@talk21.com>
- **Date:** 2003-05-17T23:46:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net>`

```
LX-i <DanielJSNOSPAM@Knology.net> wrote:

>docdwarf@panix.com wrote:
>> In article <3EB406BA.3020201@Knology.net>,
…[17 more quoted lines elided]…
>living".  :)

Sounds rather like the Sergeants at Sandhurst (Officer Training
Establishment, UK).  They announce themselves to their Officer Cadets
thus-  "You are Officer Cadets and as a noncommissioned officer I have
to call you 'Sir'..  I am in charge of you, so you will call *me*
'Sir'..  The difference is, that *you* will mean it!".   :-)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-17T23:38:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EC6C437.E2C2@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com>`

```


Jeff York wrote:

>
> Sounds rather like the Sergeants at Sandhurst (Officer Training
…[4 more quoted lines elided]…
>

Oh those *delightful* drill sergeants. As an apprentice I had two RAF Regiment
flight sergeants as drill instructors. I've mentioned before a certain
acquaintance who was with me - Stuffins - his name and sexual preference are not
inappropriate to the following :-

"Attenshun ! Get your bleedin' 'ands clenched.  YOU Stuffins ! If you don't clench
your bleedin 'ands, I'll stuff my ....... .. in your bleedin 'and !".

Jimmy
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-18T13:53:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec774b7_1@corp-news.newsgroups.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com>`

```

"Jeff York" <pogo50@talk21.com> wrote in message
news:u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com...
>
> Sounds rather like the Sergeants at Sandhurst (Officer Training
…[4 more quoted lines elided]…
>
In NZ, which is modelled on the British Army, NCOs are NEVER addressed as
"Sir". If you inadvertently called a Staff Sergeant or other NCO "Sir" it
would almost invariably elicit the gruff response: "Don't call ME Sir,
there's no birdshit on my shoulder..." (Officers up to the rank of Captain
have brown and white splashes called "pips" on their epaulettes.)

The use of "Sir" to address an Officer was taken to a fine art by some of
the NCOs. My favourite memory was as a newly graduated acting
second-lieutenant, fresh out of OCTU, instructing a platoon on the
afternoon's exercise and, in my inexperience, missing some pretty critical
points. The long-suffering Maori Staff Sergeant  (who was a REAL soldier
with many years experience) listened to my address then said: "Well, that's
a pretty stupid thing to do, SIR...".  It made me smile at the time and it
makes me laugh even now. He then filled all of us in on the proper way to do
things (the "Army way"...) and we were all much more enlightened. You don't
have to be a genius to realise that the army is run by the NCOs whatever the
Officers may tell you...<G>

Fortunately or unfortunately, depending on your point of view, I got pulled
out on medical grounds before I could complete the conscripted term of
service (I was going deaf as a result of childhood infection and trauma from
high explosive), so I never got to be a serving Officer. I had a problem
with taking the Oath of Allegiance anyway...it requires us to swear to
uphold Queen Elizabeth the Second, her heirs and successors...as a pretty
staunch Republican at the time, I could never to that. As an Atheist,
swearing on the Bible was a bit pointless, but they said that was OK, I
could just give my word... I said I still had a problem with it and they
said they'd see if it could be changed  so that I could promise to defend NZ
(they were pretty desperate to get career Officers in those days and were
really trying to encourage the last of us conscripts into considering a
career with the Army...). I was pulled out before we resolved the issue, but
in the meantime I had about 2 months as an acting Officer. It was a very
valuable experience.

Pete.



> --
> Jeff.         Ironbridge,  Shrops,  U.K.
> jeff@jakfield.xu-netx.com  (remove the x..x round u-net for return
address)
>
> ... "There are few hours in life more agreeable
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** Jeff York <pogo50@talk21.com>
- **Date:** 2003-05-18T16:11:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ik7fcv85b25jfif5l8mlaj82nfr7d12ntt@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com> <3ec774b7_1@corp-news.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Jeff York" <pogo50@talk21.com> wrote in message
…[9 more quoted lines elided]…
>"Sir".

It's the same in the British army.. So the above struck me as odd when
I first saw/heard it..  Could be that Officer Cadets are in some form
of military limbo - as they're probably not officially soldiers at all
at that point and are expected to address the Sergeant with a courtesy
title - much the same as you'd address a policeman as "Sir" (If you've
any sense that is..).

>.... The long-suffering Maori Staff Sergeant  (who was a REAL soldier
>with many years experience) listened to my address then said: "Well, that's
>a pretty stupid thing to do, SIR...".  It made me smile at the time and it
>makes me laugh even now.

Part of the training for a good senior NCO is to be able to pronounce
the word spelled p.i.l.l.o.c.k as "Sir"..  :-)

> He then filled all of us in on the proper way to do
>things (the "Army way"...) and we were all much more enlightened. You don't
>have to be a genius to realise that the army is run by the NCOs whatever the
>Officers may tell you...<G>

Never was a truer word written.. :-)

>... I had a problem with taking the Oath of Allegiance anyway...
>...
>.. I said I still had a problem with it and they said they'd see if it could be 
>changed  so that I could promise to defend NZ (they were pretty desperate
> to get career Officers in those days...

Sounds like they were so desperate they'd have been willing to let you
recite "Jabberwocky" with your fingers crossed.  :-)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-19T13:44:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec83446_1@corp-news.newsgroups.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com> <3ec774b7_1@corp-news.newsgroups.com> <ik7fcv85b25jfif5l8mlaj82nfr7d12ntt@4ax.com>`

```

"Jeff York" <pogo50@talk21.com> wrote in message
news:ik7fcv85b25jfif5l8mlaj82nfr7d12ntt@4ax.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> >
> > He then filled all of us in on the proper way to do
> >things (the "Army way"...) and we were all much more enlightened. You
don't
> >have to be a genius to realise that the army is run by the NCOs whatever
the
> >Officers may tell you...<G>
>
…[4 more quoted lines elided]…
> >.. I said I still had a problem with it and they said they'd see if it
could be
> >changed  so that I could promise to defend NZ (they were pretty desperate
> > to get career Officers in those days...
…[3 more quoted lines elided]…
>
Thanks for the response, Jeff.

I hasten to add that all this was long before I actually travelled to, and
lived in the UK.

Ironically, I found myself some years later living next door to the Palace
(I was in Buckingham Gate SW1) and whether it was the exposure at first hand
to things English, or just the natural process of "growing up" I found that
after a few years my extreme Republicanism became softened.

I still care passionately about my country, but I don't see the Monarchy as
a load of parasitic maggots any more, and I can live with us being or not
being a Republic...

As for Jabberwocky...it has always been, and remains to this day, one of my
favourites. I know it by heart of course, just from having read it many
times as a child. If they had asked me to recite that instead, I would've
done so in a heartbeat <G>.

Pete.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-05-19T02:57:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SUOdnTfYupriHVWjXTWcqw@comcast.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com> <3ec774b7_1@corp-news.newsgroups.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ec774b7_1@corp-news.newsgroups.com...
>
> "Jeff York" <pogo50@talk21.com> wrote in message
…[13 more quoted lines elided]…
>


    In the US army (circa 1980), they would reply "SIR! I work for a living!
Followed by "get down and give me 20" (At least in basic training).

    US Marine NCO's on the other hand expect to be called "SIR".


> The use of "Sir" to address an Officer was taken to a fine art by some of
> the NCOs. My favourite memory was as a newly graduated acting
…[3 more quoted lines elided]…
> with many years experience) listened to my address then said: "Well,
that's
> a pretty stupid thing to do, SIR...".  It made me smile at the time and it
> makes me laugh even now. He then filled all of us in on the proper way to
do
> things (the "Army way"...) and we were all much more enlightened. You
don't
> have to be a genius to realise that the army is run by the NCOs whatever
the
> Officers may tell you...<G>
>
> Fortunately or unfortunately, depending on your point of view, I got
pulled
> out on medical grounds before I could complete the conscripted term of
> service (I was going deaf as a result of childhood infection and trauma
from
> high explosive), so I never got to be a serving Officer. I had a problem
> with taking the Oath of Allegiance anyway...it requires us to swear to
…[4 more quoted lines elided]…
> said they'd see if it could be changed  so that I could promise to defend
NZ
> (they were pretty desperate to get career Officers in those days and were
> really trying to encourage the last of us conscripts into considering a
> career with the Army...). I was pulled out before we resolved the issue,
but
> in the meantime I had about 2 months as an acting Officer. It was a very
> valuable experience.
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-19T16:35:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec902be.12124115@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com> <3ec774b7_1@corp-news.newsgroups.com> <SUOdnTfYupriHVWjXTWcqw@comcast.com>`

```
"Russell Styles" <RWS0202@comcast.net> wrote:

>    US Marine NCO's on the other hand expect to be called "SIR".

Only in boot camp. 

Very senior NCOs such as sergeants major are sometimes called sir out of
respect. 

Lieutenants can be called Mister, but it's not commonly used.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 16)_

- **From:** Gerry Wolfe <gerry.wolfe@sympatico.ca>
- **Date:** 2003-05-20T21:23:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72llcvolin21j96guorrul1m455fidvn02@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com> <3ec774b7_1@corp-news.newsgroups.com> <SUOdnTfYupriHVWjXTWcqw@comcast.com> <3ec902be.12124115@news.optonline.net>`

```
I can't believe how long this this off-topic, off-subject thread has
been going on!!!

Must be an all-time record.

Let's kill it, OK.  Some of us are interested in the implications of
the GOTO statement and structured programming in COBOL, but don't give
a rats ass about trivial salutations in the armed forces.  

advTHANKSance... g

On Mon, 19 May 2003 16:35:43 GMT, robert@wagner.net (Robert Wagner)
wrote:

>"Russell Styles" <RWS0202@comcast.net> wrote:
>
…[7 more quoted lines elided]…
>Lieutenants can be called Mister, but it's not commonly used.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-20T21:39:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<baelbu$36u$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <SUOdnTfYupriHVWjXTWcqw@comcast.com> <3ec902be.12124115@news.optonline.net> <72llcvolin21j96guorrul1m455fidvn02@4ax.com>`

```
In article <72llcvolin21j96guorrul1m455fidvn02@4ax.com>,
Gerry Wolfe  <gerry.wolfe@sympatico.ca> wrote:
>I can't believe how long this this off-topic, off-subject thread has
>been going on!!!
…[7 more quoted lines elided]…
>advTHANKSance... g

Some of 'us' might do that, aye... and others might appear to be enjoying 
the thread and its turns, as is evidenced by its continuation.

DD

>On Mon, 19 May 2003 16:35:43 GMT, robert@wagner.net (Robert Wagner)
>wrote:
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-18T00:04:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EC7145C.2030900@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <3EB46B79.2080108@Knology.net> <u2cdcvgle5fm17es456ohpbr2drt377lp3@4ax.com>`

```
Jeff York wrote:
> Sounds rather like the Sergeants at Sandhurst (Officer Training
> Establishment, UK).  They announce themselves to their Officer Cadets
> thus-  "You are Officer Cadets and as a noncommissioned officer I have
> to call you 'Sir'..  I am in charge of you, so you will call *me*
> 'Sir'..  The difference is, that *you* will mean it!".   :-)

heh heh - that's great...  :)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-03T23:27:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-56412D.23275803052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com>`

```
In article <3EB406BA.3020201@Knology.net>, LX-i  
<DanielJSNOSPAM@Knology.net> wrote:

> >How does one respond to being told to do something one Just Doesn't Like?  
> >
>As a military member, I believe the appropriate response
>is "Sir, yes sir!"

I thought you were in the Air Force.

;-)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T09:54:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb4e2d2.43423950@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <3EB406BA.3020201@Knology.net>, LX-i  
><DanielJSNOSPAM@Knology.net> wrote:
…[8 more quoted lines elided]…
>;-)

ROFL. Excellent response.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-08T22:34:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBB21BB.1060805@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com>`

```
Joe Zitzelberger wrote:
>>As a military member, I believe the appropriate response
>>is "Sir, yes sir!"
…[4 more quoted lines elided]…
> ;-)

We say "sir" most of the time...  :)  (except when gender-inappropriate)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** joe_zitzelberger@vsam.org (Joe Zitzelberger)
- **Date:** 2003-05-09T09:05:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c99d007f.0305090805.6295bd22@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net>`

```
LX-i <DanielJSNOSPAM@Knology.net> wrote in message news:<3EBB21BB.1060805@Knology.net>...
> Joe Zitzelberger wrote:
> >>As a military member, I believe the appropriate response
…[6 more quoted lines elided]…
> We say "sir" most of the time...  :)  (except when gender-inappropriate)

Hmmmm.  My (admittedly limited) experience with the Air Force
indicates the more typical response would be something like:

    "Gee Bob, I'm not sure I really agree with 
    you on that.  Perhaps we should discuss it
    on the driving range, and perhaps afterward
    we could stop by the club for drinks."

I took BNCOC at Maxwell AFB (isn't that where you are) in 95.  I must
say the gueat barracks were quite comfy.  And the free mini-bar and
maid service was a joy after a hard day of school.

Of course, it could just be envy that you were smart enough to join
the Air Force and I believed the all the things the Army recruiter
told me... ;-)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-09T11:33:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBBD842.60508@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com>`

```
Joe Zitzelberger wrote:
> Hmmmm.  My (admittedly limited) experience with the Air Force
> indicates the more typical response would be something like:
…[4 more quoted lines elided]…
>     we could stop by the club for drinks."

Sounds like you've been hanging out with some officers...

> I took BNCOC at Maxwell AFB (isn't that where you are) in 95.  I must
> say the gueat barracks were quite comfy.  And the free mini-bar and
> maid service was a joy after a hard day of school.

:)  I was right...   Yes, I'm actually over on Gunter, but it's part of 
Maxwell.  They do have a nice VOQ...

> Of course, it could just be envy that you were smart enough to join
> the Air Force and I believed the all the things the Army recruiter
> told me... ;-)

heh - the recruiters don't necessarily lie, but they can definitely put 
an undeservedly positive spin on things...
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-09T20:14:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-12C230.20143909052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3EBBD842.60508@Knology.net>`

```
In article <3EBBD842.60508@Knology.net>,
 LX-i <DanielJSNOSPAM@Knology.net> wrote:

> Joe Zitzelberger wrote:
> > Hmmmm.  My (admittedly limited) experience with the Air Force
…[7 more quoted lines elided]…
> Sounds like you've been hanging out with some officers...

I used to spend alot of time with the ALO team -- they always hand more 
fun and interesting things to do, like hang out the side of a AC-130 for 
kicks...
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 16)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-09T22:24:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBC70D8.4080201@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3EBBD842.60508@Knology.net> <joe_zitzelberger-12C230.20143909052003@corp.supernews.com>`

```
Joe Zitzelberger wrote:
> In article <3EBBD842.60508@Knology.net>,
>  LX-i <DanielJSNOSPAM@Knology.net> wrote:
…[17 more quoted lines elided]…
> kicks...

That sounds like fun.  That's the one downside (and an upside) about my 
job - I don't get to hang out of airplanes.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T20:08:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd43c4.181670028@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3EBBD842.60508@Knology.net> <joe_zitzelberger-12C230.20143909052003@corp.supernews.com> <3EBC70D8.4080201@Knology.net>`

```
LX-i <DanielJSNOSPAM@Knology.net> wrote:

>Joe Zitzelberger wrote:

>> I used to spend alot of time with the ALO team -- they always hand more 
>> fun and interesting things to do, like hang out the side of a AC-130 for 
…[3 more quoted lines elided]…
>job - I don't get to hang out of airplanes.

At one programming job we had a Cessna Conquest twin engine turbo to support
truck stops in god forsaken places such as Rawlins, Wyoming. I used to sit in
the copilot seat and play navigator with the VOR. Occasionally I'd pilot the
thing. It was great. I could leave Texas in the morning, fly 2,000 miles to
California, work on computer, and be home in time for dinner. And while aloft, I
could smoke on the plane.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 18)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-10T20:35:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBDA8C9.8020708@Knology.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3EBBD842.60508@Knology.net> <joe_zitzelberger-12C230.20143909052003@corp.supernews.com> <3EBC70D8.4080201@Knology.net> <3ebd43c4.181670028@news.optonline.net>`

```
Robert Wagner wrote:
> LX-i <DanielJSNOSPAM@Knology.net> wrote:
>>That sounds like fun.  That's the one downside (and an upside) about my 
…[8 more quoted lines elided]…
> could smoke on the plane. 

That sounds cool...  :)  Programming and flying at the same time!
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-09T12:47:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9gm3v$l1a$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com>`

```
In article <c99d007f.0305090805.6295bd22@posting.google.com>,
Joe Zitzelberger <joe_zitzelberger@vsam.org> wrote:

[snip]

>Of course, it could just be envy that you were smart enough to join
>the Air Force and I believed the all the things the Army recruiter
>told me... ;-)

As has been called-and-responded on the PT Fields of Lackland in the
pre-dawn hours:

'Rainbow, rainbow, don't be blue,
My recruiter screwed me, too!'

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-09T17:10:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBBDD30.39143AE1@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <b9gm3v$l1a$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:

> In article <c99d007f.0305090805.6295bd22@posting.google.com>,
> Joe Zitzelberger <joe_zitzelberger@vsam.org> wrote:
…[12 more quoted lines elided]…
>

Seeing your use of 'blue' but in a slightly different context. Instead
of the US oxymoron 'friendly fire',  the Brits use 'blue on blue'.
Canada suffered a blue on blue in Afghanistan - the first fatalities we
have had since the Korean War.

Jimmy
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T03:12:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebc3a03.113626234@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com>`

```
joe_zitzelberger@vsam.org (Joe Zitzelberger) wrote:

>LX-i <DanielJSNOSPAM@Knology.net> wrote in message
news:<3EBB21BB.1060805@Knology.net>...
>> Joe Zitzelberger wrote:
>> >>As a military member, I believe the appropriate response
…[22 more quoted lines elided]…
>told me... ;-)

How stupid does that make me for joining the Marine Corps? 8-)

At the time, the Army and Air Force age cutoff was 18.5, and they wanted a four
year commitment.  The Navy, Marine Corps and Coast Guard were happy with 17 and
a three year commitment.  I was 16, there weren't any Coast Guard recruiters to
be seen, everyone knew Navy were a bunch of lowlife swabbies, so the choice was
obvious, by elimination. I fudged a little on the age thing and got out at age
19.

If I had it to do over, I would have waited and joined the Air Force. If the
draft had been rescinded, I would have chosen none of the above.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-10T10:28:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-F65C77.10285110052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3ebc3a03.113626234@news.optonline.net>`

```
In article <3ebc3a03.113626234@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:
> 
> How stupid does that make me for joining the Marine Corps? 8-)

I'm not going to touch that...
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 16)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-05-10T12:21:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6n9qbvc01i4s6cg88hntum29268r87buvr@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3EB406BA.3020201@Knology.net> <b91oiv$p2p$1@panix1.panix.com> <joe_zitzelberger-56412D.23275803052003@corp.supernews.com> <3EBB21BB.1060805@Knology.net> <c99d007f.0305090805.6295bd22@posting.google.com> <3ebc3a03.113626234@news.optonline.net> <joe_zitzelberger-F65C77.10285110052003@corp.supernews.com>`

```
On Sat, 10 May 2003 10:28:51 -0400, Joe Zitzelberger
<joe_zitzelberger@nospam.com> enlightened us:

>In article <3ebc3a03.113626234@news.optonline.net>,
> robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>I'm not going to touch that...

It should be obvious..

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Next time you think you're perfect try walking on water.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb41cca.94910457@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8p6it$r8a$1@panix1.panix.com> <8a2d426e.0304302141.47b7b970@posting.google.com> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3eb1fde5.30851164@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[38 more quoted lines elided]…
>That, of course, depends on the someone.

There is another alternative, one that I've used (almost) all my career. It is
to get promoted to management, then throw dumb rules in the trash and get on
with problem solving.   8-)
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T21:03:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b91oti$qd9$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb1fde5.30851164@news.optonline.net> <b8to8h$qql$1@panix1.panix.com> <3eb41cca.94910457@news.optonline.net>`

```
In article <3eb41cca.94910457@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[42 more quoted lines elided]…
>There is another alternative, one that I've used (almost) all my career.

There are often other alternatives... the story, perhaps apochryphal, 
tells of behavioral scientists who designed a cage with four routes of 
escape into which they put an ape.  The scientists watched to see what 
method the ape took to escape; based on which way out the ape found the 
scientists hoped to make conclusions about how the ape was thinking and, 
by extension, how humans were thinking.

The ape found the fifth way out.

>It is
>to get promoted to management, then throw dumb rules in the trash and get on
>with problem solving.   8-)

Most managers I have met are too busy attending meetings to actually get 
any work done... but that is my own limited experience.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-01T10:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb0ddf9.569450184@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3eafd941.502695520@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[21 more quoted lines elided]…
>>>>because she finds the file drawer jammed shut. Within her narrow
perspective,
>>>>it's an 'unrecoverable error'. 
>>>>
…[33 more quoted lines elided]…
>>In environments with a formal methodology, there isn't a single 'program
spec'.
>>There are at least three levels of documentation, usually more:
>>
…[8 more quoted lines elided]…
>>often full of errors. When there is a question about what the change is
intended
>>to accomplish, the high level design is 'the bible'. If there is a conflict
>>between high level design and business requirement (this happens rarely), the
…[3 more quoted lines elided]…
>>authoritarian attitude you describe. 'Do as you're told and shut up' is found
in
>>UNstructued environments, where order comes from personal relationships
because
>>better tools are absent. 
>
…[7 more quoted lines elided]…
>matters would seem to be irrelevant.)

Management style is very relevant. 

>What do you think a programmer should do when given a clear, unambiguous,
>direct and legal instruction by a duly-authorised corporate superior?

The answer is tell him to check his calender; he might find it's running 30
years slow. Next tell his boss the guy's a tyrant, then look for another job and
encourage others to do the same. 

When dealing with intelligent workers, respect is reciprocal. Managers who don't
give it don't get any in return. They wind up with a crew of Dillards .. er,
dullards.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-01T14:10:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8r9s3$7vb$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net>`

```

On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >What do you think a programmer should do when given a clear, unambiguous,
> >direct and legal instruction by a duly-authorised corporate superior?
…[3 more quoted lines elided]…
> and encourage others to do the same.

You might want to check with a lawyer before encouraging other employees to quit
their job.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-02T06:32:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb202a3.32064816@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:
…[8 more quoted lines elided]…
>You might want to check with a lawyer before encouraging other employees to
quit
>their job.

That's FUD. Last time I checked, freedom of speech was still intact. In fact, US
Tort law in re slander makes communications about employment 'privileged'. If a
prospective employer calls for a reference on Joe Smith and you tell lies about
him, he has no legal recourse .. no cause of action. 

Contrary to widely held misbelief, that's the law.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-02T08:30:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8todv$rvi$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net>`

```
In article <3eb202a3.32064816@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"Howard Brazee" <howard@brazee.net> wrote:
>
…[13 more quoted lines elided]…
>That's FUD. Last time I checked, freedom of speech was still intact.

I am not sure about the 'last time' you did so, Mr Wagner, but I recall a 
time when you asserted that refusing to listen to someone was an 
infringement on their 'freedom of speech' as well... oh, and you might 
want to check and see what rights a private corporation (as opposed to a 
government body) has for limiting kinds of speech on its premises.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb41de4.95193173@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8todv$rvi$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3eb202a3.32064816@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[9 more quoted lines elided]…
>>>> years slow. Next tell his boss the guy's a tyrant, then look for another
job
>>>> and encourage others to do the same.
>>>
>>>You might want to check with a lawyer before encouraging other employees to
quit
>>>their job.
>>
…[6 more quoted lines elided]…
>government body) has for limiting kinds of speech on its premises.

What recourse do they have? Fire the person who's already resigned? Censor the
email and telephones of co-workers? As a practical matter, they have no
recourse.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T21:05:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b91p0h$r8v$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb202a3.32064816@news.optonline.net> <b8todv$rvi$1@panix1.panix.com> <3eb41de4.95193173@news.optonline.net>`

```
In article <3eb41de4.95193173@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[25 more quoted lines elided]…
>What recourse do they have?

You might want to check that, Mr Wagner, as suggested above... there might 
be things in Heaven and Earth not dreamt of in your philosophies.

DD
k
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:16:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95v8c$prl$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8todv$rvi$1@panix1.panix.com> <3eb41de4.95193173@news.optonline.net>`

```

On  3-May-2003, robert@wagner.net (Robert Wagner) wrote:

> What recourse do they have? Fire the person who's already resigned? Censor the
> email and telephones of co-workers? As a practical matter, they have no
> recourse.

In today's litigious society, how sure are you of this?   Are you sure you won't
have legal hassles and expenses that you won't regret?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T14:26:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tv7f$i8u$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net>`

```

On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >You might want to check with a lawyer before encouraging other employees to
> quit
…[8 more quoted lines elided]…
> Contrary to widely held misbelief, that's the law.

It could be.   I am not a lawyer, and don't pretend to be a lawyer.  But I do
believe in covering my but in this very litigious society.

Or do you trust the system that much?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb41f53.95559939@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:
…[16 more quoted lines elided]…
>Or do you trust the system that much?

The system sometimes doesn't follow its own rules. For instance, lawyers have
most people convinced there is a legal cause called Wrongful Termination. There
is no such thing in US or in most cases State law. A person can be fired for any
reason or no reason .. except those explicitly prohibited by civil rights
legislation and similar such as ADA. But lawyers have won cases based on
sympathy for the underdog rather than law. 

I trust the system to be predictable, not necessarily right. Courts tend to
favor people over big companies. If sympathy AND the law are both on your side,
there is no reason to fear lawyers. They know that, but they'll huff and puff in
the hope you don't. Citing case or legislative law quickly deflates their hot
air balloon.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:18:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95vcp$pru$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net>`

```

On  3-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >It could be.   I am not a lawyer, and don't pretend to be a lawyer.  But I do
> >believe in covering my but in this very litigious society.
…[3 more quoted lines elided]…
> The system sometimes doesn't follow its own rules.

Yep.
...


> I trust the system to be predictable, not necessarily right.

It can't be completely predictable if it "sometimes doesn't follow its own
rules".


> Courts tend to
> favor people over big companies. If sympathy AND the law are both on your
> side, there is no reason to fear lawyers.

But big companies can afford more lawyers and time than you can.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-06T08:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb763cf.112895639@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net> <b95vcp$pru$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  3-May-2003, robert@wagner.net (Robert Wagner) wrote:
>
>> >It could be.   I am not a lawyer, and don't pretend to be a lawyer.  But I
do
>> >believe in covering my but in this very litigious society.
>> >
…[15 more quoted lines elided]…
>But big companies can afford more lawyers and time than you can.

They'd be wasting their time and money going after small fish. The most they
could recover is a few thousand dollars.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-06T14:22:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b98geu$6tu$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net> <b95vcp$pru$1@peabody.colorado.edu> <3eb763cf.112895639@news.optonline.net>`

```

On  6-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >But big companies can afford more lawyers and time than you can.
>
> They'd be wasting their time and money going after small fish. The most they
> could recover is a few thousand dollars.

But the most they would gain is to deter future employees from doing what they
don't want done.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-06T17:28:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305061628.5899cac0@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net> <b95vcp$pru$1@peabody.colorado.edu> <3eb763cf.112895639@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> Courts tend to
> >> favor people over big companies. If sympathy AND the law are both on your
…[5 more quoted lines elided]…
> could recover is a few thousand dollars.

Simply not true.

Microsoft went after some small individual in New York.  He had
assembled a CD of some Jewish material and called it "The First
Electronic Jewish Bookshelf" and had some made and was selling them in
a small way.

Back in the late 80s Ampro had built a small A4 file box sized CP/M
machine which it called the 'Bookshelf Computer' and registered this
as a trademark.  MS challenged this in court claiming 'bookshelf' was
a generic term.  After Ampro went bust MS bought them and inhereted
the trademark.

They took the Jewish Bookshelf to court even though he had no money at
all and the trademark was for computers, not for collections of books
and MS refused to settle because they wanted the judgement.

Sympathy was against MS, one may even say that the trademark law was
too, but they prevailed because no defense was offered - it couldn't
be afforded.

Now MS had a basically uncontested precedent they could use to
threaten bigger companies.

This happens quite often because it is cheaper to persecute 'small
fish' and not bother to collect any imposed damages than it is to
chase the same issue against someone able to defend themselves.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-07T00:30:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-695559.00304007052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net> <b95vcp$pru$1@peabody.colorado.edu> <3eb763cf.112895639@news.optonline.net> <217e491a.0305061628.5899cac0@posting.google.com>`

```
In article <217e491a.0305061628.5899cac0@posting.google.com>,
 riplin@Azonic.co.nz (Richard) wrote:

> robert@wagner.net (Robert Wagner) wrote 
> 
…[35 more quoted lines elided]…
> chase the same issue against someone able to defend themselves.

That Micro$oft is able to postpone action indefinantly via an army of 
lawyers should in no way be construed to mean Micro$oft is correct.  In 
most (all) cases Micro$oft has avoided a jury because of that army of 
lawyers.

Remember what happened to Stac Technologies...not even a die-hard M$ 
worshiper can defend that sorry criminal event.

Did the Jewish Bookshelf actually get in front of a jury?  Or did the 
creator run out of funds to defend it and just give up?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T08:39:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba0dae.121612019@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <b8tv7f$i8u$1@peabody.colorado.edu> <3eb41f53.95559939@news.optonline.net> <b95vcp$pru$1@peabody.colorado.edu> <3eb763cf.112895639@news.optonline.net> <217e491a.0305061628.5899cac0@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>Microsoft went after some small individual in New York.  He had
>assembled a CD of some Jewish material and called it "The First
…[22 more quoted lines elided]…
>chase the same issue against someone able to defend themselves.

You make a good point in re precident, although it's not relevant to this
discussion. Lay people do not understand that court decisions, called "stare
decisis", have the force of law. If another case is brought in the same
jurisdiction with identical circumstances, the court is _required_ to decide the
same way. The prior decision is not a suggestion, it is an imperative, it has
become law.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-02T12:32:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305021132.6ef94bc9@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >You might want to check with a lawyer before encouraging other employees to
>  quit their job.
> 
> That's FUD. Last time I checked, freedom of speech was still intact. In fact,
> US Tort law in re slander makes communications about employment 'privileged'.

Contrary to what many Americans think, US Law does not apply in some
small remote and uncivilised parts of the world.  Something that Bush
is doing his best to rectify right now.

> If a prospective employer calls for a reference on Joe Smith and you tell 
> lies about him, he has no legal recourse .. no cause of action. 

In what way in this relevant to 'encouraging other employees to quit'
?

> Contrary to widely held misbelief, that's the law.

Well I had noticed your anecdote where you told the Lawyer that you
knew more about the Law than he did.  Sheesh, what's the point of
wasting time at a Law School and then 20 years in specialist practice
when Robert will give you the real answer here for free.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-03T11:43:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb3028c_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0305021132.6ef94bc9@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
…[4 more quoted lines elided]…
> when Robert will give you the real answer here for free.

"A man who conducts his own defence has a fool for a Lawyer."

I have conducted my own defence on a couple of occasions (both were trivial)
and I won one and lost one...<G> (However, I believe that even the one I
lost I came out of better than if I hadn't defended it at all...)

Neither of these experiences has led me to believe that Lawyers are
unnecessary when it comes to litigation.

I DO believe that adults of good will should be able to settle their
differences and disputes peacefully and fairly, and litigation should be a
LAST resort. Sadly, in the US it seems to be becoming a growth industry.

Next time I need legal advice I'll call Robert <G>.

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-03T13:25:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-73CBFF.13252603052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com> <3eb3028c_2@127.0.0.1>`

```
In article <3eb3028c_2@127.0.0.1>,
 "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> I DO believe that adults of good will should be able to settle their
…[5 more quoted lines elided]…
> Pete.

We do seem to have replaced the "rule of law" with the "rule of 
lawyerss".  

But this is perhaps a misunderstanding, easily understood, caused by 
your remote view of the US and its lawyers.  It is really only 99% of 
our lawyers giving the other %1 a bad name.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb4299e.98194947@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[8 more quoted lines elided]…
>is doing his best to rectify right now.

:) :)

Today Iraq, tomorrow the world. 

>> If a prospective employer calls for a reference on Joe Smith and you tell 
>> lies about him, he has no legal recourse .. no cause of action. 
>
>In what way in this relevant to 'encouraging other employees to quit'?

Both are communications 'about employment' so I think both should be protected
under the same legal theory. Granted, I have no substantiation, so don't quote
me as a source. <g>

>Well I had noticed your anecdote where you told the Lawyer that you
>knew more about the Law than he did.  Sheesh, what's the point of
>wasting time at a Law School and then 20 years in specialist practice
>when Robert will give you the real answer here for free.

He was a general practitioner; the case was in a specialized field where I was
more knowledgable. 

I too 'went to law school' -- via self-education and correspondence course --
then aced the first part of the bar exam. That was unusual in California, which
has the highest scoring curve in the US. They say 90% fail on the first attempt.
I didn't take all parts of the bar exam because I had no intention to be a
lawyer; I did it to show off to a girlfriend.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-04T10:54:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b91hd4$9ka$2@aklobs.kc.net.nz>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com> <3eb4299e.98194947@news.optonline.net>`

```
Robert Wagner wrote:

>>In what way in this relevant to 'encouraging other employees to quit'?
> 
> Both are communications 'about employment' so I think both should be
> protected under the same legal theory. Granted, I have no substantiation,
> so don't quote me as a source. <g>

Which seems to be quite different from "It is the Law".

Do you think that _anything_ you say should be treated as other than 
bullshit trying to impress people ?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T02:22:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb4718d.14422067@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com> <3eb4299e.98194947@news.optonline.net> <b91hd4$9ka$2@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Do you think that _anything_ you say should be treated as other than 
>bullshit trying to impress people ?

Let them judge for themselves. You don't speak for them. That's the beauty of
usenet.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-03T22:20:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305032120.77808c79@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com> <3eb4299e.98194947@news.optonline.net> <b91hd4$9ka$2@aklobs.kc.net.nz> <3eb4718d.14422067@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >Do you think that _anything_ you say should be treated as other than 
> >bullshit trying to impress people ?
> 
> Let them judge for themselves. 
> You don't speak for them. 

Was I trying to ?  Where for example ?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-03T23:30:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-D5DF7A.23305403052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eadb031.361090998@news.optonline.net> <b8lvl7$b5c$1@panix1.panix.com> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8r9s3$7vb$1@peabody.colorado.edu> <3eb202a3.32064816@news.optonline.net> <217e491a.0305021132.6ef94bc9@posting.google.com> <3eb4299e.98194947@news.optonline.net>`

```
In article <3eb4299e.98194947@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> 
> Today Iraq, tomorrow the world. 

Hell Yea!!!  Let's start with France again!

Where do I sign up?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T12:13:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rh39$q21$1@panix5.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net>`

```
In article <3eb0ddf9.569450184@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:

[snip]

>
>>What do you think a programmer should do when given a clear, unambiguous,
…[4 more quoted lines elided]…
>encourage others to do the same. 

How interesting... so you say that when dealing with an attitude which is 
abhorrent, said attitude being one of 'my way or the highway', on the part 
of a manager the appropriate response is for a subordinate to...

... assume an attitude which is abhorrent, one of 'my way or the highway'.

This is called in some circles, 'becoming one's enemy'... in other circles 
it is called a double-standard.

Thanks for the response though; I did not read this before I posed the 
question for the third time.

>
>When dealing with intelligent workers, respect is reciprocal.

I disagree, Mr Wagner; I would say that when dealing with *anyone* respect 
is earned.  Courtesy is granted as a matter of form... but respect is 
earned.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-01T16:49:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rj64$bs4$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com>`

```

On  1-May-2003, docdwarf@panix.com wrote:

> >When dealing with intelligent workers, respect is reciprocal.
>
> I disagree, Mr Wagner; I would say that when dealing with *anyone* respect
> is earned.  Courtesy is granted as a matter of form... but respect is
> earned.

And intelligence has little to do with it.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-01T14:02:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rngf$kgd$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu>`

```
In article <b8rj64$bs4$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-May-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>And intelligence has little to do with it.

I'm not sure... I dunno if I'm smart enough to say.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T03:03:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb2ffe7.21968168@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  1-May-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>And intelligence has little to do with it.

I disagree. I've seen the difference in truck stops and convenience stores, but
my current shop is fresher in my memory. We have low-paid, low-skilled clerks
(two thirds of them have been replaced by my software; that's another story.)
The other day a supervisor was seen walking to a coffee shop with a peon to get
their morning coffee. Clerks watching it said, "That's not right. A supervisor
shouldn't fraternize with workers." The comment shocked me. I thought an office
was supposed to be a brotherhood. 

Low paid people support the system that subjugates them. They expect to punch a
time clock and be fired when they screw up. They expect to live in relative
poverty. They expect to be treated like shit.  If someone treated them humanely,
they'd see it as a sign of weakness.

I've never seen 'knowledge workers' such as programmers, hold beliefs like that.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-03T21:40:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb38eb9_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb2ffe7.21968168@news.optonline.net...
> "Howard Brazee" <howard@brazee.net> wrote:
>
…[5 more quoted lines elided]…
> >> I disagree, Mr Wagner; I would say that when dealing with *anyone*
respect
> >> is earned.  Courtesy is granted as a matter of form... but respect is
> >> earned.
…[3 more quoted lines elided]…
> I disagree. I've seen the difference in truck stops and convenience
stores, but
> my current shop is fresher in my memory. We have low-paid, low-skilled
clerks
> (two thirds of them have been replaced by my software; that's another
story.)
> The other day a supervisor was seen walking to a coffee shop with a peon
to get
> their morning coffee. Clerks watching it said, "That's not right. A
supervisor
> shouldn't fraternize with workers." The comment shocked me. I thought an
office
> was supposed to be a brotherhood.
>
> Low paid people support the system that subjugates them. They expect to
punch a
> time clock and be fired when they screw up. They expect to live in
relative
> poverty. They expect to be treated like shit.  If someone treated them
humanely,
> they'd see it as a sign of weakness.

Jeez, Robert, there isn't much grey in your world, is there <G>?

I've been reprimanded for drinking in the "wrong bar" at lunchtime (I was
drinking with the shop floor, rather than the white collar guys (mainly
because I was working on the shop floor analysing their systems and,
besides, their conversation was much more interesting than that of the
Hooray Henry's who passed for "management" in this particular Dickensian
English establishment). I told the guy who reprimanded me, politely, that,
as I didn't bill him for my lunch time, it was my time and no concern of
his. He didn't like it but he needed my expertise so he had to swallow it.
(I never worked there again after the project completed, but that was
mutual.))

As for low-paid people supporting the system that subjugates them, there are
numerous instances on record of them kicking over the traces when the
conditions became outrageous (Have a look at England, 1640, Europe, 1838,
Russia, 1917, Mexico 1880s, England 1927, USA 1930s and the rise of
Unionism, just to name a few... . Ruling the peasants with an iron hand was
found to be workable, but only for a limited time. You might like to review
the collapse of the Feudal system in Europe. Printing presses disseminate
information, peasants learn to read, there goes the neighbourhood...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T10:06:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b90id9$3pv$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1>`

```
In article <3eb38eb9_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[27 more quoted lines elided]…
>Jeez, Robert, there isn't much grey in your world, is there <G>?

Mr Dashwood, didn't you know?  Some say that seeing things in 
black-and-white but to see shades of grey requires... intelligence!

DD
```

###### ↳ ↳ ↳ OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-03T19:15:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB411AF.F448D322@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1>`

```


"Peter E.C. Dashwood" wrote:

>

<Lottsa snippage>

>
> As for low-paid people supporting the system that subjugates them, there are
…[7 more quoted lines elided]…
>

1927 in UK ? That's the second time you've mentioned it; first time through it didn't
register, but now in above context  -  is that the General Strike of 1926 ?
I originally wrote above "Great Strike", but just to be sure, a Google search. gave :-

"Britain was paralysed for nine days, 3-12 May, during the 1926 General Strike"..

Google did give 'Great Strike 1877" - but that was in U.S.

As for Robert's lack of 'greyness' - it triggered in my mind the ONE film I would take
with me to a Desert Island. 'Lawrence of Arabia', a magnificent movie, particularly
for the magnificent international cast.....

Lawrence is assembled with his Arabs, having been, (presumably)  previously  sodomized
by a Turkish colonel,  (Jose Ferrer). They are looking down in contempt on the
retreating, bedraggled Turks. Some oily customer next to Lawrence says "El Aurens, no
prisoners ?". Comments Anthony Quinn, "This was Abdul's (?) village". Lawrence
(O'Toole), turns his face into a sheet of anger, raises his sword and screams,

"Take no prisoners !".

Then the beautiful scene after the carnage - one of my favourite actors, Arthur
Kennedy as the US reporter. He surveys the wholesale bloodshed. "Sweet Jesus". "Sweet
Jesus". And to Lawrence, "Let me take your bloody picture !"

For you youngsters in US who haven't seen it - get it from a video store. It covers
History, Middle East 101 - a prologue to Gulf Wars 1 and  2 !

Jimmy
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T00:31:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb457a5.7789156@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>"Peter E.C. Dashwood" wrote:

>> As for low-paid people supporting the system that subjugates them, there are
>> numerous instances on record of them kicking over the traces when the
…[5 more quoted lines elided]…
>> information, peasants learn to read, there goes the neighbourhood...<G>

The Puritan Revolution of 1640 was about religion, not economics. It triggered
the English Civil War of 1642-48 which ended with abolishment of the monarchy
(Charles I) and its replacement by Oliver Cromwell as head of state. This lasted
only ten years, after which Charles II was reinstated to the throne. 

Russia in 1917 was about political and anti-religious ideology more than
economics. They wanted to change how the world REGARDS workers rather than how
it TREATS THEM. Admittedly, the difference is subtle. 

Peasants who learned to read in feudal times didn't have supermarket tabloids
voiding their reading skill with fluff and nonsense. Nor did they have
television. Talk about "opiate of the masses" ... television personifies it more
than religion.
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-04T15:30:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb48981_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca> <3eb457a5.7789156@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb457a5.7789156@news.optonline.net...
> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
> >"Peter E.C. Dashwood" wrote:
>
> >> As for low-paid people supporting the system that subjugates them,
there are
> >> numerous instances on record of them kicking over the traces when the
> >> conditions became outrageous (Have a look at England, 1640, Europe,
1838,
> >> Russia, 1917, Mexico 1880s, England 1927, USA 1930s and the rise of
> >> Unionism, just to name a few... . Ruling the peasants with an iron hand
was
> >> found to be workable, but only for a limited time. You might like to
review
> >> the collapse of the Feudal system in Europe. Printing presses
disseminate
> >> information, peasants learn to read, there goes the neighbourhood...<G>
>
> The Puritan Revolution of 1640 was about religion, not economics.

Ostensibly, but not in actuality. Do some more digging.

The same could be said for the crusades. "Religion" has been a good cover
for war based on greed and economics throught history.

If I remember rightly (it WAS some time ago and my memory is becoming
porous, like Doc's) William of Normandy obtained a blessing from the Pope
before his historic invasion of England (the last successful one...) in
1066. He then used this to persuade his cronies it was a religious crusade
and nothing to do with a personal slight suffered through a broken promise.

(I tried to tell Harold not to go...wait and gather his resources...but he
was so flushed with the victory at Stamford Bridge he wouldn't listen...<G>
Off they trot, the length of England, and on a Summer afternoon in a field
in Southern England, 12,000 men (total combatants on both sides) changed the
course of history, and Harold ended up chopped into bits, identifiable only
by his poor wife who recognised an intimate birth mark... I still feel sorry
about it, but I did my best...<G>)

> It triggered
> the English Civil War of 1642-48 which ended with abolishment of the
monarchy
> (Charles I) and its replacement by Oliver Cromwell as head of state. This
lasted
> only ten years, after which Charles II was reinstated to the throne.
>
> Russia in 1917 was about political and anti-religious ideology more than
> economics.
>

The elite at the Czar's Court (who saw the peasants as less than dogs) would
not agree with you... They saw their lifestyle threatened. It was economic.


>They wanted to change how the world REGARDS workers rather than how
> it TREATS THEM. Admittedly, the difference is subtle.
>
The recorded writings of the people who were there don't reflect that. The
revolution was concerned with facts, not appearances.

> Peasants who learned to read in feudal times didn't have supermarket
tabloids
> voiding their reading skill with fluff and nonsense. Nor did they have
> television. Talk about "opiate of the masses" ... television personifies
it more
> than religion.

Interesting that you would end with a parody of Karl Marx, having just
dismissed the Revolution as being about perception rather than
practice...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-04T04:40:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB48F53.10B01873@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca> <3eb457a5.7789156@news.optonline.net> <3eb48981_2@127.0.0.1>`

```


"Peter E.C. Dashwood" wrote:

> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3eb457a5.7789156@news.optonline.net...
…[37 more quoted lines elided]…
> about it, but I did my best...<G>)

Bingo about Harold and Willie the Conk !

I always look sadly on how fate treated Harold after that tremendous trudge up north
to defeat the Vikings, then he marched his men down the hill again... (remember that
one <G>), and with an already exhausted army of thanes and villeins, (surely that's
not where he did his first draft of TYCI24H <G>), took on the Viking/Norsemen/Norman
cut throats. The decisive point in the battle was when Harold was mortally wounded by
an arrow in the eye.

My own version on Robert's take follows separately. Still it's not as good as "1066
And All That" <G>

Jimmy
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-03T23:35:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-DE9EDC.23352303052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca> <3eb457a5.7789156@news.optonline.net>`

```
In article <3eb457a5.7789156@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:
> 
> Russia in 1917 was about political and anti-religious ideology more than
> economics. They wanted to change how the world REGARDS workers rather than 
> how
> it TREATS THEM. Admittedly, the difference is subtle. 

I must admit, the differeence it too subtle for me.

Is it a step up in status for the workers to be regarded as reasonable 
targets of mass-murder.  Or is that just my inner running dog capitolist 
coming out?
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-05T05:43:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB5F65D.EB639FFD@shaw.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca> <3eb457a5.7789156@news.optonline.net>`

```


Robert Wagner wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[15 more quoted lines elided]…
>

Robert,

Going from memory, so don't look for specifics or dates.

That is close, but it is an oversimplification. It's much more complex, as most
things are, (even integers and sets <G>). It's like saying the N. Ireland problem is
Catholics v Protestants. Now translate that to the Middle East - Judaism v Islam. We
all know that's not true; it is also Jews v Arabs, although both are Semitic.
Complicate it even further by throwing in the Persians/Iranians, who while Islamists
are not semites, (I think) - Indo-European perhaps ?

Back to UK. Henry VIII anti Rome, (having already earned "Defender of the Faith"),
desperately wanted a male heir - hence the divorces which Rome refused because of
French/Spanish pressure, primarily from Spain, Henry's first wife was Catherine of
Aragon, Philip of Spain's aunt.. As an autocrat Henry ruthlessly put down a Cornish
protest for the old catholicism, but at the same time strongly disapproved of his
bishops marrying and sought out those attempting to translate from Latin into
English. I think I'm correct in saying he himself still attended catholic Latin
masses until his death.

Henry looked in horror from Southsea Castle as he saw his new flagship the 'Mary
Rose' capsize and sink off Portsmouth. For a further reference to Mary Rose - see
next paragraph but one.

Skip his teenage son Edward VI, dying horribly from TB at 16 (?), and Edward's
step-sister Mary, his oldest child, really both non-events and on to Elizabeth his
second child. Brought up as a Protestant she was also influenced by her circle of
ministers, already Protestants by belief or opportunism. In retrospect the first
great set of ministers England ever had. Elizabeth was not even rabidly
anti-Catholic; it was the zeal of the new Jesuit order coming into England, trained
on the Continent, which raised the ugly spectre of 'Papists'.

The absoluteness of monarchy was achieved in Elizabeth's reign. Sadly as she walked
around and lay dying at Richmond Palace, on the banks of the Thames,
( took her about a week to call it quits), those same faithful ministers silently
slipped away one by one, galloping like mad to Scotland to be the first to make
obeisance to James VI of Scotland (Henry VIII had a sister - Mary Rose, begat Mary
Queen of Scots, begat James VI who was educated as a Protestant).

  Aside : Could be a Trivia question. Which was the first royal residence to have a
biffy ? Answer : Richmond Palace, Surrey had a water closet installed for the Queen
(that's QE1,  Bill <G>), prior to 1601. Phew ! The Elizabethans stank. No wonder
they were always on royal tours sussing out new digs !

Essentially the early concepts of Puritanism, chapel people as opposed to the
established church, catholic or otherwise started in Scotland in Mary Queen of
Scot's reign - particularly influenced by John Knox.

James VI Scotland becomes James I of England. (He was definitely AC/DC, which I'm
told in the modern idiom is 'swinging both directions'). No longer quite absolute,
close but not quite - as he was the new boy on the block in a foreign country.

Puritanism was growing as both a cleansing from the idolatrous 'Papist Church', and
the 'Established Church', (Church of England) and also seeds of 'democracy'. Dates
escape me but we have various exodus from UK to the New World, Pilgrim Fathers,
Quakers, other religious groups, plus catholics to Maryland.

Charles I succeeds his father - tending to still play the 'absolute' role, and
getting involved in some Continental misadventures which required him to go back to
Parliament and demand more taxes to support his overseas 'projects'.. It is really
only in Charles' reign that Parliament comes to prominence. The aristocrats tended
to go with the king whereas the merchant class objected to being taxed, (so what's
new <G>). There were no political parties as we know them - at which stage Cromwell
eventually came to the fore because he was single minded, (much like Winston
Churchill in the void of the 1930s).

The Parliamentarians did not set out to commit regicide. They wanted a compromise
from the king. As a final act of desperation this led to the Civil War, Royal versus
Roundheads, (Parliamentarians). It was only when the king, having agreed to peace
treaties, was shown to be deviously plotting with Continental monarchies - Only then
did the Parliamentarians behead him publicly at Whitehall.

Then Oliver Cromwell took over - did a real number on my ancestors back in Ireland
and encouraged Protestant Scots, from the Lowlands,  to settle in what we now call
Ulster (N. Ireland). Certainly  Puritanism displaced the established church
(Protestant) during the Protectorate, but we were back to square one when Oliver
died and Charles'es son became Charles II, (conceivably a catholic ??), unlike the
future king, his brother James II, who had converted 'back' to catholicism.

Now politics and economics are very much intertwined - but if you review the above,
although it seeps like a cess pit in the background, essentially religion was not
the cause.

While for a short time Puritanism flourished, particularly during the Protectorate,
it fizzled and disappeared. Strangely catholicism never disappeared from the UK. The
Scottish Highlanders were predominantly catholic, hence their future support for
Bonnie Prince Charlie, (James II begat James the Old Pretender, begat Bonnie Prince
Charlie the Young Pretender). Further there was a strong enclave of catholics in the
north west in Lancashire. Interestingly the Senior Peer of the Realm (not sure of
exact title), is the catholic Duke of Norfolk, his 'home' being Arundel Castle in
Sussex and his family name - Howard as in Catherine Howard, Henry VIII's  fourth
wife. He had an Elizabethan ancestor, Philip Howard, who was executed and is called
'Blessed Philip Howard' in the UK catholic calendar. The Duke's main role is to act
as MC at a coronation - last time 1953.

Now when it comes to 'democracy' it actually took the UK a fair time to get there.
It wasn't until the Great Emancipation Act ( somewhere 1840-45) that catholics were
given (back) the right to vote. (Similarly with female emancipation - UK sometime in
the early 1920s, whereas, (trying to remember what Richard once wrote), either 1880s
or 1890s in N.Z, and 1890s here in Canada).

Interestingly contrast following. The US had it's first catholic president JFK back
in the sixties. Canada since I've been here, 1975,  has had a continuous line of
catholic PM's with one eight month break when female Kim Campbell took over from
Brian Mulroney and the PCs (Progressive Conservatives) were wiped out at the next
election - I think we have currently about 3 or 4 PC MPs. With all those Canuck
Papists around we have never once had a problem with 'Church and State'. The UK has
never had a catholic PM - the nearest you get is that Tony Blair is married to a
catholic. (Before anybody picks up on it - I'm not trying to suggest the 25 plus
years of catholics at the helm in Canada was a good thing - we have had more than
our fair share of dumbos <G>).

> Russia in 1917 was about political and anti-religious ideology more than
> economics. They wanted to change how the world REGARDS workers rather than how
> it TREATS THEM. Admittedly, the difference is subtle.

Again I contest it was politics and economics intertwined. No food, we want
political clout. Just like religion in the UK, the Russian orthodox church was part
of the detested establishment, but religion was not a major factor - that's unless
you want to take the hokey influence of Rasputin on the Czarina into account.

>
> Peasants who learned to read in feudal times didn't have supermarket tabloids
> voiding their reading skill with fluff and nonsense. Nor did they have
> television. Talk about "opiate of the masses" ... television personifies it more
> than religion.
```

###### ↳ ↳ ↳ Re: OT : 1927 and other : Was: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:26:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95vra$q2v$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1> <3EB411AF.F448D322@shaw.ca>`

```

On  3-May-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> For you youngsters in US who haven't seen it - get it from a video store. It
> covers
> History, Middle East 101 - a prologue to Gulf Wars 1 and  2 !

I saw it when it came out, saw a re-release about a decade ago, and have the
laser disk (which starts off with a blank screen and music - just like the
movie).

My most quotable scene - when Lawrence is letting the match extinguish itself
against his fingers.   A messenger tries to duplicate this "trick".   He says it
hurts, Lawrence replys "of course it hurts".   "Then what's the trick?"   "The
trick is not to mind".

One of the all time best entrances in film is when Omar Sharif shows up.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-03T19:00:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VsWcnXNqr-OpxSmjXTWJig@giganews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <3eb38eb9_2@127.0.0.1>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz>

> As for low-paid people supporting the system that subjugates them, there
are
> numerous instances on record of them kicking over the traces when the
> conditions became outrageous. Ruling the peasants with an iron hand was
> found to be workable, but only for a limited time.

It worked for about a thousand years in Europe. Still works in great parts
of the world (China, most of Africa, Massachusetts).
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:21:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95vht$q2a$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net>`

```

On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >> I disagree, Mr Wagner; I would say that when dealing with *anyone* respect
> >> is earned.  Courtesy is granted as a matter of form... but respect is
…[20 more quoted lines elided]…
> that.

So how does that support your disagreement with  "intelligence has little to do
with it"?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-06T08:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb7625f.112528091@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  2-May-2003, robert@wagner.net (Robert Wagner) wrote:
…[26 more quoted lines elided]…
>with it"?

Fraternization between managers and workers is acceptable in IT departments,
where there is no concept of class distinction.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-06T07:42:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b98hl0$1klg$1@si05.rsvl.unisys.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb7625f.112528091@news.optonline.net...

> Fraternization between managers and workers is acceptable in IT
departments,
> where there is no concept of class distinction.

Just out of curiosity, is that another one of those immutable and universal
truths?   ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-06T15:32:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b98khv$8ns$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com>`

```

On  6-May-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> > Fraternization between managers and workers is acceptable in IT
> > departments, where there is no concept of class distinction.
>
> Just out of curiosity, is that another one of those immutable and universal
> truths?   ;-)

There are IT departments with enlisted staff and officer managers.

But I have worked elsewhere where they had posted requirements about what kinds
of fraternization were acceptable between an employee and the person who reviews
his performance.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-07T03:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb875a1.17134914@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <b98khv$8ns$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  6-May-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
…[10 more quoted lines elided]…
>of fraternization were acceptable between an employee and the person who
reviews
>his performance. 


I don't dispute what you say, but I've never seen it. Except in the military.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-07T09:36:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9bcm2$jsa$1@si05.rsvl.unisys.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <b98khv$8ns$1@peabody.colorado.edu> <3eb875a1.17134914@news.optonline.net>`

```
I've seen it outside the military as well.

    -Chuck Stevens

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb875a1.17134914@news.optonline.net...
> "Howard Brazee" <howard@brazee.net> wrote:
>
…[6 more quoted lines elided]…
> >> Just out of curiosity, is that another one of those immutable and
universal
> >> truths?   ;-)
> >
> >There are IT departments with enlisted staff and officer managers.
> >
> >But I have worked elsewhere where they had posted requirements about what
kinds
> >of fraternization were acceptable between an employee and the person who
> reviews
…[3 more quoted lines elided]…
> I don't dispute what you say, but I've never seen it. Except in the
military.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-06T15:25:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305061425.77c79441@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> > Fraternization between managers and workers is acceptable in IT
>  departments,
…[3 more quoted lines elided]…
> truths?   ;-)

A 'wagnerism'.

It may be true if it had been said as:

"In ( IT departments where there is no concept of class distinction ),
fraternization between managers and workers is acceptable."

or even:

"In ( IT departments where fraternization between managers and workers
is acceptable ), fraternization between managers and workers is
acceptable."

But he seems to have based his conclusion on a staistical sample of 3
yet again.


Perhaps we should define 'wagnerism' to be 'a conclusion about the
whole world based on 3 samples and incompetent understanding of
statistics'.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-07T03:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb8746a.16824338@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[7 more quoted lines elided]…
>truths?   ;-)

It wasn't my invention, it came from low-level workers. THEY see a class
distinction where I do not. 

It wasn't at one place nor three, it was at dozens of places.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-07T00:57:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305062357.22ae0563@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> Fraternization between managers and workers is acceptable in IT
>  departments,
…[6 more quoted lines elided]…
> distinction where I do not. 

It would seem to me that use of a term 'low-level workers' indicates
somewhat that you are making a class distinction.

This may not only disprove your claim of not seeing a class
distinction, but also that one does not exist.

Not only that if 'THEY see a class distinction' then there must be one
to see - for example by being called 'low-level' by the IT department.
 
> It wasn't at one place nor three, it was at dozens of places.

I am sure that you did call others 'low-level' at dozens of places.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T08:39:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba10e1.122431343@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <217e491a.0305062357.22ae0563@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[17 more quoted lines elided]…
>to see - for example by being called 'low-level' by the IT department.

If I'd said the sky is blue, you'd twist it around to make me the bad guy. 

Your goal is not communication of ideas, it is discouraging me from posting.
```

###### ↳ ↳ ↳ OT Some friendly advice was:Re: "Go To" and "Structured programming"

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-08T23:42:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba4337_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <217e491a.0305062357.22ae0563@posting.google.com> <3eba10e1.122431343@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eba10e1.122431343@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
…[6 more quoted lines elided]…
> >> >Just out of curiosity, is that another one of those immutable and
universal
> >> >truths?   ;-)
> >>
> >> It wasn't my invention, it came from low-level workers. THEY see a
class
> >> distinction where I do not.
> >
…[11 more quoted lines elided]…
> Your goal is not communication of ideas, it is discouraging me from
posting.

Robert, I am neutral here (well that's not quite true...I tend to favour the
underdog and that would put me more in your court in this case.  But your
comments (on this occasion, at least..) are really not fair.)

You cannot dismiss the argument by saying that Richard is simply out to get
you, and whatever you say will be made wrong.

(Whether this is true or not <G>,  it doesn't address his reasoning based on
your original statement.)

The FACT is that you made a statement:

"> >> It wasn't my invention, it came from low-level workers. THEY see a
class
> >> distinction where I do not. "

This is such a fraught statement that it is hardly surprising it provoked a
response annihilating it from Richard.

I guess my message is as follows:

1. THINK before you write. (You have shown from your posts here that you are
far from stupid, yet you persist in posting sweeping generalisations as if
they were statements of fact... You need to really realise that the people
here are not a bunch of Cretans or imbeciles who will accept whatever you
say without question as if it were Holy Writ. (Jeez, if they won't do that
for me (and I've been here for the duration), they are hardly likely to do
it for you (a relative newcomer) <G>.))

2. DO NOT post generalisations as if they were facts. (Ask yourself: "Could
there be ONE low-level worker, who maybe I never met, but who DOESN'T see a
class distinction?" If the answer is "yes, possibly..." then your statement
needs modification BEFORE you post it.

3. Debate honourably. Even if you lose, you will gain respect. (Invoking
"Poor Me, they're picking on me again, doesn't matter what I say, I'm always
wrong..." is NOT honourable debate. Address the issues.

4. This is a forum of your peers (whether you accept that or not). They are
as bright as you, they are as nimble as you, and they are as experienced and
informed as you. What may get you by in other places won't wash here. Get it
right, or be told that you are wrong. (unfortunately, this may extend to
actual humiliation (born of resentment), and some pretty unworthy stuff on
the part of  your adversaries also... the people here have feelings and your
approach is hard to swallow; especially when you are wrong...) This may be a
hard pill to swallow, but once you do, you will have a much more enjoyable
time here.

(In your own mind you believe you are exceptional. This is probably true for
most of the places you have worked. So it has been reinforced by your
working with people who you see as "not as bright as me". You are certainly
"above average" and it is easy to become off-hand and supercilious with
people for whom you have little respect. In this forum that is no longer the
case. There are minds here that are greater than yours or mine, at least in
some respects. You need to make the necessary adjustment. When you do, the
group will respond accordingly and life will be a lot easier for all
concerned.

If you just stop and edit your posts before pressing send, I know you can
improve the quality of your contribution out of sight. You have something
worthwhile to contribute here and it is a pity to see it descend to the
level that is has done, simply because you "lead with your chin".

For the most part, I read and enjoy your posts.

But I have to confess to becoming tired of the endless pointless exchanges
they seem to be provoking. Make your posts more "watertight" and the threads
will be shorter and  we can cover more ground profitably for all concerned.

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT Some friendly advice was:Re: "Go To" and "Structured programming"

_(reply depth: 17)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-05-08T23:56:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c315bd$48ce7cc0$b695f243@chottel>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <217e491a.0305062357.22ae0563@posting.google.com> <3eba10e1.122431343@news.optonline.net> <3eba4337_2@127.0.0.1>`

```
Well since most companies are organized hierarchically, "low-level" may
only indicate where they appear on the organization chart.

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3eba4337_2@127.0.0.1>...
> 
> "Robert Wagner" <robert@wagner.net> wrote in message
…[26 more quoted lines elided]…
> > If I'd said the sky is blue, you'd twist it around to make me the bad
guy.
> >
> > Your goal is not communication of ideas, it is discouraging me from
> posting.
> 
> Robert, I am neutral here (well that's not quite true...I tend to favour
the
> underdog and that would put me more in your court in this case.  But your
> comments (on this occasion, at least..) are really not fair.)
> 
> You cannot dismiss the argument by saying that Richard is simply out to
get
> you, and whatever you say will be made wrong.
> 
> (Whether this is true or not <G>,  it doesn't address his reasoning based
on
> your original statement.)
> 
…[6 more quoted lines elided]…
> This is such a fraught statement that it is hardly surprising it provoked
a
> response annihilating it from Richard.
> 
> I guess my message is as follows:
> 
> 1. THINK before you write. (You have shown from your posts here that you
are
> far from stupid, yet you persist in posting sweeping generalisations as
if
> they were statements of fact... You need to really realise that the
people
> here are not a bunch of Cretans or imbeciles who will accept whatever you
> say without question as if it were Holy Writ. (Jeez, if they won't do
that
> for me (and I've been here for the duration), they are hardly likely to
do
> it for you (a relative newcomer) <G>.))
> 
> 2. DO NOT post generalisations as if they were facts. (Ask yourself:
"Could
> there be ONE low-level worker, who maybe I never met, but who DOESN'T see
a
> class distinction?" If the answer is "yes, possibly..." then your
statement
> needs modification BEFORE you post it.
> 
> 3. Debate honourably. Even if you lose, you will gain respect. (Invoking
> "Poor Me, they're picking on me again, doesn't matter what I say, I'm
always
> wrong..." is NOT honourable debate. Address the issues.
> 
> 4. This is a forum of your peers (whether you accept that or not). They
are
> as bright as you, they are as nimble as you, and they are as experienced
and
> informed as you. What may get you by in other places won't wash here. Get
it
> right, or be told that you are wrong. (unfortunately, this may extend to
> actual humiliation (born of resentment), and some pretty unworthy stuff
on
> the part of  your adversaries also... the people here have feelings and
your
> approach is hard to swallow; especially when you are wrong...) This may
be a
> hard pill to swallow, but once you do, you will have a much more
enjoyable
> time here.
> 
> (In your own mind you believe you are exceptional. This is probably true
for
> most of the places you have worked. So it has been reinforced by your
> working with people who you see as "not as bright as me". You are
certainly
> "above average" and it is easy to become off-hand and supercilious with
> people for whom you have little respect. In this forum that is no longer
the
> case. There are minds here that are greater than yours or mine, at least
in
> some respects. You need to make the necessary adjustment. When you do,
the
> group will respond accordingly and life will be a lot easier for all
> concerned.
…[8 more quoted lines elided]…
> But I have to confess to becoming tired of the endless pointless
exchanges
> they seem to be provoking. Make your posts more "watertight" and the
threads
> will be shorter and  we can cover more ground profitably for all
concerned.
> 
> Pete.
…[5 more quoted lines elided]…
> ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via
Encryption =---
>
```

###### ↳ ↳ ↳ Re: OT Some friendly advice was:Re: "Go To" and "Structured programming"

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T17:29:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebcedb6.159636108@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <217e491a.0305062357.22ae0563@posting.google.com> <3eba10e1.122431343@news.optonline.net> <3eba4337_2@127.0.0.1>`

```
Thanks for the dispassionately written advice. I'll try to heed it under MOST
circumstances when responding to MOST posters (with the possible exception of DD
and his hundred dictionary bookmarks). <G>

---------- history below ----------
>1. THINK before you write. (You have shown from your posts here that you are
>far from stupid, yet you persist in posting sweeping generalisations as if
…[38 more quoted lines elided]…
>level that is has done, simply because you "lead with your chin".
```

###### ↳ ↳ ↳ Re: OT Some friendly advice was:Re: "Go To" and "Structured programming"

_(reply depth: 18)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-11T11:44:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd8ec0_1@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <217e491a.0305062357.22ae0563@posting.google.com> <3eba10e1.122431343@news.optonline.net> <3eba4337_2@127.0.0.1> <3ebcedb6.159636108@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebcedb6.159636108@news.optonline.net...
> Thanks for the dispassionately written advice. I'll try to heed it under
MOST
> circumstances when responding to MOST posters (with the possible exception
of DD
> and his hundred dictionary bookmarks). <G>
>

Hahaha! That's more like it...<G>

Pete.

<snip>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-07T10:37:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9bg9f$mhb$1@si05.rsvl.unisys.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb8746a.16824338@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
…[8 more quoted lines elided]…
> >Just out of curiosity, is that another one of those immutable and
universal
> >truths?   ;-)
>
…[3 more quoted lines elided]…
> It wasn't at one place nor three, it was at dozens of places.

Did you maybe put a comma where you shouldn't have?  You seem to be arguing
something other than what you wrote.

The way you have written it, your argument is:  Because it was true at
dozens of IT departments, we are therefore required to conclude that *no*
corporate cultures or policies *anywhere* discourage fraternization between
"workers" and "managers" in the IT department, and that in *no* corporate
cultures is there any suggestion of a class distinction in the IT department
between "management" and "labor".  Another way of expressing the sentiment
you expressed is "There is never a concept of class distinction in IT
departments; fraternization between managers and workers is always
acceptable."   Neither generalization is supported, and either one is
rendered false by the very existence of a single counterexample.

If you DIDN'T mean the comma to be there, your sentiment is along the lines
of "In those IT departments in which there is no concept of class
distinction, fraternization between managers and workers is acceptable".
That allows for the possibility that somewhere there might actually exist an
IT department in which (a) there is a concept of class distinction and/or
(b) fraternization between managers and workers is *not* acceptable.

It seems to me you have two choices:  (a) change the argument to be
something other than what you originally stated it to be (I'm sure changing
the argument once more would be popular with the CLC readership), or (b)
admit that your argument is unsupportable in fact because it can be
disproven by a single counterexample.

Stated another way, I think you've checkmated yourself.  Again.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T08:39:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba0c87.121316612@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <b8rj64$bs4$1@peabody.colorado.edu> <3eb2ffe7.21968168@news.optonline.net> <b95vht$q2a$1@peabody.colorado.edu> <3eb7625f.112528091@news.optonline.net> <b98hl0$1klg$1@si05.rsvl.unisys.com> <3eb8746a.16824338@news.optonline.net> <b9bg9f$mhb$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[47 more quoted lines elided]…
>Stated another way, I think you've checkmated yourself.  Again.

You misinterpreted the subject "it", which referred to low-level workers at
dozens of places. THEY and their concept were the subject of the two previous
sentences. IT departments couldn't possibly be the predicate of "it" because I
didn't mention them in the message.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T03:03:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb304e3.23244831@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eafd941.502695520@news.optonline.net> <b8p6it$r8a$1@panix1.panix.com> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3eb0ddf9.569450184@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[9 more quoted lines elided]…
>>years slow. Next tell his boss the guy's a tyrant, then look for another job
and
>>encourage others to do the same. 
>
…[7 more quoted lines elided]…
>it is called a double-standard.

It's not a double standard. The manager, not I,  originated the proposition 'my
way or the highway'. I'm just following his precepts. 

>>When dealing with intelligent workers, respect is reciprocal.
>
>I disagree, Mr Wagner; I would say that when dealing with *anyone* respect 
>is earned.  Courtesy is granted as a matter of form... but respect is 
>earned.

Good point. I concur.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-03T10:09:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b90iiq$49h$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <3eb304e3.23244831@news.optonline.net>`

```
In article <3eb304e3.23244831@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[25 more quoted lines elided]…
>way or the highway'. I'm just following his precepts. 

This is what my Sainted Maternal Grandmother - may she sleep with the 
angels! - used to refer to as a 'Brooklyn Bridge defense', Mr Wagner... if 
the manager jumped off the Brooklyn Bridge then you would, too?  He does 
something that you find hateful so you do the same, hateful thing... this 
is called, in some circles, 'becoming one's enemy'.

>
>>>When dealing with intelligent workers, respect is reciprocal.
…[5 more quoted lines elided]…
>Good point. I concur. 

Gosh... I feel so *validated*!

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-05T03:48:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb53676_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb0ddf9.569450184@news.optonline.net> <b8rh39$q21$1@panix5.panix.com> <3eb304e3.23244831@news.optonline.net> <b90iiq$49h$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b90iiq$49h$1@panix1.panix.com...
> In article <3eb304e3.23244831@news.optonline.net>,
> Robert Wagner <robert@wagner.net> wrote:
…[3 more quoted lines elided]…
>

D'you mean like a parking ticket, Doc...?
(Limp, flimsy, and been through the machine...<G>)
or, like a Scientologist
(bright eyed, bushy tailed, and basking in the Theta flow...<G>)

Pete




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-04T12:01:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b93dg6$ppu$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <3eb304e3.23244831@news.optonline.net> <b90iiq$49h$1@panix1.panix.com> <3eb53676_2@127.0.0.1>`

```
In article <3eb53676_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b90iiq$49h$1@panix1.panix.com...
…[7 more quoted lines elided]…
>D'you mean like a parking ticket, Doc...?

That, at least, might have some value.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-29T14:21:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8m1op$r52$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net>`

```

On 28-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Perhaps someone higher up can recover from the condition by dispatching a
> repairperson (VERIFY). Perhaps the file was 'optional' and the program can
…[15 more quoted lines elided]…
> through the 'single' exit point.

There are advantages to this procedure.   But sometimes this obscures where the
real error occurred.  Sometimes it is nice to get an abend that showed you the
CoBOL line that aborted, and to have the formatted dump unchanged from when the
abend occurred.   I have seen called programs exit nicely with a return code
that doesn't tell us what the real problem is.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-30T17:20:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eafd186.500716200@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 28-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[23 more quoted lines elided]…
>that doesn't tell us what the real problem is.

I send a message to the error log (you do use error logs, right?). The message
contains some unique English text and the relevant data. A editor search on the
text will find the line. No two failure points issue the exact same descriptive
text. Warning messges issued shortly before the abend may help to explain the
cause. Using file open error as an example, the io module would report the error
as a warning and give the full path/file name. The high-level decision maker who
does the abend might give a more generic message. 

I haven't looked at a dump in 20 years, even the nicely formatted ones common on
mainframes. It shouldn't be necessary if the system is designed to report
errors. I have _never_ looked at a dump on Unix; PCs don't even give dumps. 

Using memory dumps to diagnose problems is another cultural difference between
IBM mainframe and other platforms.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-30T18:05:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8p3a4$nmk$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net>`

```

On 30-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> I send a message to the error log (you do use error logs, right?).

Not for non-database errors.   We have operators working in the middle of the
night.  They get an abend, check the operator instructions and do what we have
instructed them to do depending upon the error.   Anything less than an abend
usually gets missed.   We need them to know when there is an abend.

I changed a program a couple of months ago to make sure it aborted nice and
loudly when it failed.   Apparently it had been failing for some time, but
quietly and cleanly.   It copied the database to a VSAM file to run with
programs that were written before we had the database.  The conversion program
failed if that file was open, but failed quietly.  The next day people ran with
a day old VSAM file instead of the current one.   I made sure it aborted loudly
and wrote up instructions to vary that vsam file off-line (for a different CV)
and try again.

Some environments want a nice clean failure - giving a pretty message to the
user and creating an error log for the programmer.   Others don't.

> The message
> contains some unique English text and the relevant data. A editor search on
…[16 more quoted lines elided]…
> IBM mainframe and other platforms.

The dump will tell us which line had the data exception, table overflow,
mismatched file length, or whatever condition the programmer chose not to check.
   And it will allow the debugger to look at everything in working storage in a
nicely formatted way.

Sure we can check every single condition whether likely or not.    We have a
declaratives give a message when we have numeric overflow - and write code to
indicate which arithmetic statement caused this.   But the system does this
quite efficiently now.  Adding a lot of extra checks that will not likely happen
just slow down the program.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-01T10:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb0e7f9.572010790@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:


>Sure we can check every single condition whether likely or not.    We have a
>declaratives give a message when we have numeric overflow - and write code to
>indicate which arithmetic statement caused this.   But the system does this
>quite efficiently now.  Adding a lot of extra checks that will not likely
happen
>just slow down the program.

Twenty years ago we let the machine's inadequacies influence our programming
style and system design. Those days are over. Now, I worry about functionality
and let someone else worry about speed.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-01T14:12:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8ra0a$850$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu> <3eb0e7f9.572010790@news.optonline.net>`

```

On  1-May-2003, robert@wagner.net (Robert Wagner) wrote:

> >Sure we can check every single condition whether likely or not.    We have a
> >declaratives give a message when we have numeric overflow - and write code to
…[7 more quoted lines elided]…
> and let someone else worry about speed.

Still, checking every single statement adds more chances for error and gives me
nothing in return.   I know when an error can be handled so I check those
errors.  I know when the system's response will be as good, if not better than
mine.   When that happens I let the system respond.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-01T15:51:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305011451.2a92ef76@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu> <3eb0e7f9.572010790@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> Twenty years ago we let the machine's inadequacies influence our programming
> style and system design. Those days are over. Now, I worry about functionality
> and let someone else worry about speed.

Yet you contradict and invert this argument when you dismiss 'trees'
with 'too slow', even though they may be faster in a specific
application than serial searching.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-05-01T23:19:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c31037$f9f16b60$19caf943@chottel>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu> <3eb0e7f9.572010790@news.optonline.net> <217e491a.0305011451.2a92ef76@posting.google.com>`

```
Dilbert to RW: 

I did the analysis using your bad assumptions, then I applied your flawed
logic and arrived at your predetermned answer".

Richard <riplin@Azonic.co.nz> wrote in article
<217e491a.0305011451.2a92ef76@posting.google.com>...
> robert@wagner.net (Robert Wagner) wrote 
> 
> > Twenty years ago we let the machine's inadequacies influence our
programming
> > style and system design. Those days are over. Now, I worry about
functionality
> > and let someone else worry about speed.
> 
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T11:57:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb1b476_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu> <3eb0e7f9.572010790@news.optonline.net> <217e491a.0305011451.2a92ef76@posting.google.com> <01c31037$f9f16b60$19caf943@chottel>`

```
ROFL!

Pete.

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c31037$f9f16b60$19caf943@chottel...
> Dilbert to RW:
>
> I did the analysis using your bad assumptions, then I applied your flawed
> logic and arrived at your predetermned answer".
>
<snip>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T03:03:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb322da.30916661@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net> <b8m1op$r52$1@peabody.colorado.edu> <3eafd186.500716200@news.optonline.net> <b8p3a4$nmk$1@peabody.colorado.edu> <3eb0e7f9.572010790@news.optonline.net> <217e491a.0305011451.2a92ef76@posting.google.com>`

```
iplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> Twenty years ago we let the machine's inadequacies influence our programming
>> style and system design. Those days are over. Now, I worry about
functionality
>> and let someone else worry about speed.
>
>Yet you contradict and invert this argument when you dismiss 'trees'
>with 'too slow', even though they may be faster in a specific
>application than serial searching.

You said:
>> >In fact the issue of sorting a list is a moot one anyway.  Why not
>> >just create a tree and not only have it already sorted when complete,
>> >but also have fast access via the tree structure.

You were talking about tree-building as a sorting algorithm, like heap sort. I
have no objection to building trees for searching, and said so when you raised
the same point a month or two ago. You changed the subject from sorting to
searching. 

My personal preference is to sort with a high speed algorithm, then load  the
keys and pointers into a table upon which I could do a SEARCH ALL. That's
equivalent to a perfectly balanced binary tree.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** Gerry Wolfe <gerry.wolfe@sympatico.ca>
- **Date:** 2003-04-29T16:28:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pontavg5ten4f568gfs0gchhfivsonvipo@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <3eadb031.361090998@news.optonline.net>`

```
Not wanting to get into a pissing contest, but pls see imbedded
contents below...

On Tue, 29 Apr 2003 03:51:36 GMT, robert@wagner.net (Robert Wagner)
wrote:

>Gerry Wolfe <gerry.wolfe@sympatico.ca> wrote:
>
…[20 more quoted lines elided]…
>operate without it.

I would consider the VERIFY (file status = 97) and optional file (file
status = 35) to be file status (statii?) which can be programmed
around and probably could be resolved with program logic.  Major
returns such as 34 (boundary) or 39 (conflicting DCB attributes)
cannot be resolved internally.  

>
>Programs should be organized like corporations, with decisions made at high and
…[70 more quoted lines elided]…
>>
```

##### ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "anon" <no@no.com>
- **Date:** 2003-05-04T23:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z6hta.31126$yv1.2303844@news2.telusplanet.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com>`

```
Yep, I did the same thing for years as a mainframe programmer.  I've been a
windows programmer for about 5 years now -- but I still do get COBOL
contracts.

When I go back to COBOL (from Java, C++, Delphi or VB), the first thing I
notice is that COBOL paragraphs are way too long.  IMO this really affects
the "goto" issue.  It's a common Java/Delphi mantra to never use a return()
in the middle of a method (instead, set the return value and return it at
the end of the method).  But when you consider that the average OO method is
going to be less than a screen of code, AND it's performing a specific
function, the mantra isn't a big deal.  However in most COBOL code I've
changed/converted there is so much logic to avoid AFTER the coder knows he
needs to exit, that it would make it more confusing to not jump to the
end-of-paragraph.

I guess what I'm saying is: the more compartmentalized the code is -- the
less gotos I need.  So far in my experience with Java/Delphi (not so much
C++ however) the end of a method is normally reached without a goto --
because the logic structure is kept very simple (one
while-do/for-next/nested-if structure per method).  Once I find myself
needing to avoid big chunks of code to get to the end of the method it's
time to think about a new method or new procedure/function.

"Gerry Wolfe" <gerry.wolfe@sympatico.ca> wrote in message
news:uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com...
> Along those lines...
>
…[19 more quoted lines elided]…
> >What I stated in the other thread is that SOME (but not all) definitions
of
> >"structured" programming allow for a "Go To Exit of procedure" feature  -
> >such as the following structure
…[20 more quoted lines elided]…
> >definitions of "structured programming" - in that there is a "single
entry
> >and single exit" to each section of code - and there are no "crossing go
> >to's" or even "drop thru" logic.
…[9 more quoted lines elided]…
>http://www.marriottschool.byu.edu/teacher/ISYS540/Fall1997/Structured.htm#s
p
> > "Another key to structured programming is that each block of code (i.e.,
> >sequence of statements) has a single entry point and a single exit
point."
> >
> > - http://www.cusys.edu/pubs/cobgdln.html
…[7 more quoted lines elided]…
> >and if you use GOGGLE or equivalent, you will find many others.  It is
ALSO
> >possible to find a number of places that indicate that this usage DOES
> >violate the rules of "structured programming" - which is why I
(originally
> >and still) indicate that it may or may not be "valid" in structured
> >programming (depending upon your definition).
>
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-05T14:07:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb5c784_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <Z6hta.31126$yv1.2303844@news2.telusplanet.net>`

```
This is the most sensible defence of GO TO I have read.

Pete.

"anon" <no@no.com> wrote in message
news:Z6hta.31126$yv1.2303844@news2.telusplanet.net...
> Yep, I did the same thing for years as a mainframe programmer.  I've been
a
> windows programmer for about 5 years now -- but I still do get COBOL
> contracts.
…[3 more quoted lines elided]…
> the "goto" issue.  It's a common Java/Delphi mantra to never use a
return()
> in the middle of a method (instead, set the return value and return it at
> the end of the method).  But when you consider that the average OO method
is
> going to be less than a screen of code, AND it's performing a specific
> function, the mantra isn't a big deal.  However in most COBOL code I've
…[35 more quoted lines elided]…
> > >What I stated in the other thread is that SOME (but not all)
definitions
> of
> > >"structured" programming allow for a "Go To Exit of procedure"
eature  -
> > >such as the following structure
> > >
…[18 more quoted lines elided]…
> > >There are other ways that this may ALSO be coded, but this does meet
some
> > >definitions of "structured programming" - in that there is a "single
> entry
> > >and single exit" to each section of code - and there are no "crossing
go
> > >to's" or even "drop thru" logic.
> > >
…[3 more quoted lines elided]…
> > > "Programs should follow guidelines for 'structured' programming.
'GoTo's
> > >should be used primarily to 'go to' an exit of a performed routine."
> > >
…[5 more quoted lines elided]…
> > > "Another key to structured programming is that each block of code
(i.e.,
> > >sequence of statements) has a single entry point and a single exit
> point."
…[18 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-04T23:26:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-73B97C.23265404052003@corp.supernews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1>`

```
I'm certain I don't understand.  Are you saying that Cobol paragraphs 
SHOULD be more complicated because they have an easy GO TO available?

I would suggest it is an indictment of overly complex Cobol paragraphs...

In article <3eb5c784_2@127.0.0.1>,
 "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> This is the most sensible defence of GO TO I have read.
> 
…[118 more quoted lines elided]…
> > >
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-06T00:34:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb65a2d_2@127.0.0.1>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1> <joe_zitzelberger-73B97C.23265404052003@corp.supernews.com>`

```

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-73B97C.23265404052003@corp.supernews.com...
> I'm certain I don't understand.  Are you saying that Cobol paragraphs
> SHOULD be more complicated because they have an easy GO TO available?
>
No, of course not <G>

> I would suggest it is an indictment of overly complex Cobol paragraphs...
>

Possibly, but my comment was prompted by this:

" However in most COBOL code I've changed/converted there is so much logic
to avoid AFTER the coder knows he
needs to exit, that it would make it more confusing to not jump to the
end-of-paragraph."

I agree with this 100%. Not that it SHOULD be like that, but when you do
maintenance it very often IS like that <G>. I wouldn't hesitate to insert a
GO TO (assuming I didn't have the time to rewrite/re-structure the offending
code).

My justification for doing so is exactly that expressed above.

Pete.

<snip>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-05T08:46:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A1tta.1424$ER4.166611@news20.bellglobal.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3eb5c784_2@127.0.0.1...
> This is the most sensible defence of GO TO I have read.
>
> Pete.
>

I'd say the opposite.

First of all, I think he is right ... most people code paragraphs far too
long.  It seems to be some kind of contest amount Cobolists ... lets see who
can construct the longest inline sentence without a single new paragraph
name being introduced.  Once they have set that as their goal, then the
language starts to fail ... so next step is to make explicit scope
delimiters compulsary.

After you get all the scope delimiers in, and add extra indentation and such
so that you can tell which start-of-scope mates with which end-of-scope, the
sentences get so big that it is difficult to tell where the sentences start
and end.  So.  Next step ... lets remove all the sentence markers and add
extra white space to show what we have done.

What you end up with is as bad as LISP to read. Huge run-on sentences that
go on for pages that have to be decoded with four sets of coloured markers.
Sure you can cut and paste without a worry in the world ... as long as you
wrote the code and you did it within the last twenty minutes.

I'd rather keep the periods, use the odd delimiter to clarify things once or
twice a month, and use lots of meaningful paragraph names.  If I cannot fit
it on a screen, I break it into two (or heaven forbid sometimes even MORE
paragraphs)  The overhead of an extra level of parahraph names is just NOT
that high.

Donald

> "anon" <no@no.com> wrote in message
> news:Z6hta.31126$yv1.2303844@news2.telusplanet.net...
> > Yep, I did the same thing for years as a mainframe programmer.  I've
been
> a
> > windows programmer for about 5 years now -- but I still do get COBOL
> > contracts.
> >
> > When I go back to COBOL (from Java, C++, Delphi or VB), the first thing
I
> > notice is that COBOL paragraphs are way too long.  IMO this really
affects
> > the "goto" issue.  It's a common Java/Delphi mantra to never use a
> return()
> > in the middle of a method (instead, set the return value and return it
at
> > the end of the method).  But when you consider that the average OO
method
> is
> > going to be less than a screen of code, AND it's performing a specific
> > function, the mantra isn't a big deal.  However in most COBOL code I've
> > changed/converted there is so much logic to avoid AFTER the coder knows
he
> > needs to exit, that it would make it more confusing to not jump to the
> > end-of-paragraph.
> >
> > I guess what I'm saying is: the more compartmentalized the code is --
the
> > less gotos I need.  So far in my experience with Java/Delphi (not so
much
> > C++ however) the end of a method is normally reached without a goto --
> > because the logic structure is kept very simple (one
…[86 more quoted lines elided]…
> > > >and if you use GOGGLE or equivalent, you will find many others.  It
is
> > ALSO
> > > >possible to find a number of places that indicate that this usage
DOES
> > > >violate the rules of "structured programming" - which is why I
> > (originally
…[9 more quoted lines elided]…
> ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption
=---
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-07T08:14:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b96gqg$e1l$1@aklobs.kc.net.nz>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1> <A1tta.1424$ER4.166611@news20.bellglobal.com>`

```
Donald Tees wrote:

> The overhead of an extra level of parahraph names is just NOT
> that high.

It certainly isn't in my style of coding.  If I find a paragraph getting 
too long or too deeply indented, or contains a block of code that I can 
reuse, then it is split out and put, usually, immediately after the current 
one.  Key in a name, dupe line, add PERFORM (F9 P) mark block, move, shift 
block left.

However, many do think that 'an extra level' is high overhead. This is 
especially true where numbered sections are used.  To PERFORM a new 
procedure requires that a new number be created at the right 'level' and 
the code moved to that physical spot.  If SECTIONs are used then an exit 
paragraph must be added and a section header and the structure diagram must 
be amended.

Those brought up on:

          PERFORM 10000-INITIALISE
          PERFORM 20000-PROCESS
          PERFORM 30000-FINALISE
 
may also think that they need to have PERFORMs in blocks of 3.

*As an aside my record for one paragraph was 1500 lines (or was it 2700).  
It was, however, no problem at all.  It was just a nested EVALUATE in a 
Windows callback procedure and each WHEN (100 or so of them) acted as if it 
were a paragraph for the purposes of working on the code.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T20:56:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b96j5v$53m$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1> <A1tta.1424$ER4.166611@news20.bellglobal.com> <b96gqg$e1l$1@aklobs.kc.net.nz>`

```

On  6-May-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> If SECTIONs are used then an exit
> paragraph must be added and a section header and the structure diagram must
> be amended.

Why must exit paragraphs be used for people who use sections but not for people
who don't?

 I don't use structure diagrams - why do people who use sections need to change
 these but not people who use paragraphs?

My style is to use paragraphs with no THRU.   No drop down from paragraph to
paragraph.


> Those brought up on:
>
>           PERFORM 10000-INITIALISE
>           PERFORM 20000-PROCESS
>           PERFORM 30000-FINALISE

That's me!

> may also think that they need to have PERFORMs in blocks of 3.

Why?   Are there people who have that structure without other performs in the
program?   I doubt it.


> *As an aside my record for one paragraph was 1500 lines (or was it 2700).
> It was, however, no problem at all.  It was just a nested EVALUATE in a
> Windows callback procedure and each WHEN (100 or so of them) acted as if it
> were a paragraph for the purposes of working on the code.

My longest paragraph in modern times was a similar EVALUATE used in a conversion
program.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-05T20:23:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305051923.7397a0ae@posting.google.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <Z6hta.31126$yv1.2303844@news2.telusplanet.net> <3eb5c784_2@127.0.0.1> <A1tta.1424$ER4.166611@news20.bellglobal.com> <b96gqg$e1l$1@aklobs.kc.net.nz> <b96j5v$53m$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> Why must exit paragraphs be used for people who use sections but not for
> people who don't?

I usually try to qualify my statements with 'many who .. or 'may' or
'if', as in this case.  I referred to the 'many [that] do think that
'an extra level' is high overhead'. One of the overheads is the adding
of an exit paragraph.

The main difference between using perfomed sections, perform thru and
performed paragraphs (no thru) is that the first two allow 'go to
exit' while the last does not.

>  I don't use structure diagrams - why do people who use sections need to
>  change these but not people who use paragraphs?
 
Those that "do think that 'an extra level' is high overhead" ...
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T15:28:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95vvd$q34$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <uebqav46q73mv5spnk9qj72c1m44uab9du@4ax.com> <Z6hta.31126$yv1.2303844@news2.telusplanet.net>`

```

On  4-May-2003, "anon" <no@no.com> wrote:

> When I go back to COBOL (from Java, C++, Delphi or VB), the first thing I
> notice is that COBOL paragraphs are way too long.  IMO this really affects
…[10 more quoted lines elided]…
> less gotos I need.

Good point.   But remember that you are using programs that already have the
equivalent of the upcoming EXIT PARAGRAPH command.
```

#### ↳ Re: "Go To" and "Structured programming"

- **From:** docdwarf@panix.com
- **Date:** 2003-04-28T10:32:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8je17$e5k$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```
In article <b8if76$gdc$1@slb3.atl.mindspring.net>,
William M. Klein <wmklein@ix.netcom.com> wrote:
>As a follow-up on another thread ...
>
…[25 more quoted lines elided]…
>to's" or even "drop thru" logic.

I was taught, e'er-so-long ago, that modified Yourdon structure allows the 
use of GO TO under three conditions:

1) To the paragraph label that immediately precedes the statement.

2) To the -EXIT paragraph label that immediately follows the statement.
(this assumes/requires all paragraphs PERFORM THRU -EXIT)

3) To the program's -ABEND routine.

Quite honestly I am not sure if 3) is something I was taught or just 
picked up along the way; my earliest reference here:

<http://groups.google.com/groups?selm=4nl421%24kvj%40clarknet.clark.net&output=gplain>

... states:

--begin quoted text:

... modified Yourdon structuring (GO TO permitted only when directing 
execution to the paragraph which contains it or the exit of said 
paragraph)...

--end quoted text

... but shortly thereafter there is

<http://groups.google.com/groups?selm=34495454.2031%40erols.com&output=gplain>

--begin quoted text:

... the modified Yourdon structure which allows a GO TO under three 
conditions:

1) To the label of the paragraph containing the GO TO...

2) To the EXIT-paragraph of paragraph containin the GO TO...

3) To the ABEND paragraph to blow the program up...

--end quoted text

DD
```

##### ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T15:16:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jgju$d9d$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com>`

```

On 28-Apr-2003, docdwarf@panix.com wrote:

> I was taught, e'er-so-long ago, that modified Yourdon structure allows the
> use of GO TO under three conditions:
>
> 1) To the paragraph label that immediately precedes the statement.

I hate this.   There is no good reason for allowing this anymore.

> 2) To the -EXIT paragraph label that immediately follows the statement.
> (this assumes/requires all paragraphs PERFORM THRU -EXIT)

I will be be glad when there is no good reason to do this.   I don't do it.

> 3) To the program's -ABEND routine.

The only reason not to do this is if your compiler's optimizer changes when it
finds a "GO TO".

> Quite honestly I am not sure if 3) is something I was taught or just
> picked up along the way; my earliest reference here:

Yourdon was working with the tools of his time.   Things change.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** docdwarf@panix.com
- **Date:** 2003-04-28T11:40:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8ji13$9a9$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu>`

```
In article <b8jgju$d9d$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 28-Apr-2003, docdwarf@panix.com wrote:
…[6 more quoted lines elided]…
>I hate this.   There is no good reason for allowing this anymore.

It was never one of my favorites, either... although I would say that 
'hatred' is a bit much; as I posted a while back '(personal note: I try to 
avoid this)'.

>
>> 2) To the -EXIT paragraph label that immediately follows the statement.
>> (this assumes/requires all paragraphs PERFORM THRU -EXIT)
>
>I will be be glad when there is no good reason to do this.   I don't do it.

As I posted a while back, '(personal note: I use this'un, all the doo-dah 
day...'; it is probably a remnant of being twig-bent when I was but a 
sprout but it signals 'don't bother with the rest of the paragraph for 
this'.

>
>> 3) To the program's -ABEND routine.
…[7 more quoted lines elided]…
>Yourdon was working with the tools of his time.   Things change.

As the Germans say, 'plus ca change, plus c'est la meme chose'.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T17:32:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8joj0$gns$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu> <b8ji13$9a9$1@panix1.panix.com>`

```

On 28-Apr-2003, docdwarf@panix.com wrote:

> >
> >> 2) To the -EXIT paragraph label that immediately follows the statement.
…[7 more quoted lines elided]…
> this'.

Yep.  Those who want it for that purpose have a valid argument.   For now.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-29T09:36:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8lv5j$8ec$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8jgju$d9d$1@peabody.colorado.edu> <b8ji13$9a9$1@panix1.panix.com> <b8joj0$gns$1@peabody.colorado.edu>`

```
In article <b8joj0$gns$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 28-Apr-2003, docdwarf@panix.com wrote:
…[12 more quoted lines elided]…
>Yep.  Those who want it for that purpose have a valid argument.   For now.

In that 'Life is Temporary', Mr Brazee, *everything* might be seen as 'for 
now'; that qualification is, to some, as weighty as the 
suspiciously-intoned 'Yet...' or (what I call the Appeal to Universal 
Ignorance) the ominously-intoned 'You never knoooo-oooowww'.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T03:51:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eadb537.362376531@news.optonline.net>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:


>> 3) To the program's -ABEND routine.
>
>The only reason not to do this is if your compiler's optimizer changes when it
>finds a "GO TO".

You want your programs to abend FASTER .. is that it?
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-29T09:37:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8lv7f$8i2$1@panix1.panix.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu> <3eadb537.362376531@news.optonline.net>`

```
In article <3eadb537.362376531@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"Howard Brazee" <howard@brazee.net> wrote:
>
…[6 more quoted lines elided]…
>You want your programs to abend FASTER .. is that it? 

I cannot speak for Mr Brazee, Mr Wagner... but when I employ this 
technique no, that is not it.

DD
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-29T14:24:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8m1ul$r5e$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu> <3eadb537.362376531@news.optonline.net>`

```

On 28-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >> 3) To the program's -ABEND routine.
> >
…[4 more quoted lines elided]…
> You want your programs to abend FASTER .. is that it?

8^)

At least one optimizer do a quick pass to see if there is any GO TO code in the
program.   If it doesn't find any, it uses optimizing algorithms that are more
efficient than if no GO TO is found.
```

###### ↳ ↳ ↳ Re: "Go To" and "Structured programming"

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-04-29T11:30:14-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EAE8C76.BEBBA683@istar.ca>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net> <b8je17$e5k$1@panix1.panix.com> <b8jgju$d9d$1@peabody.colorado.edu> <3eadb537.362376531@news.optonline.net>`

```
Robert Wagner wrote:
> 
> "Howard Brazee" <howard@brazee.net> wrote:
…[6 more quoted lines elided]…
> You want your programs to abend FASTER .. is that it?

While I can't speak for Howard, since I am used to programming with the
same compiler in my case I don't want to lose the optimization that the
compiler can and does do.  Many PERFORMed paragraphs are moved in line
minimizing cache flushing.  I believe that some nested programs may also
be moved inline.  I would assume IBM Enterprise COBOL and at least some
COBOLs from other vendors might move nested objects inline.
```

#### ↳ Re: "Go To" and "Structured programming"

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T15:11:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jgb1$d8n$1@peabody.colorado.edu>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```

On 27-Apr-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> and if you use GOGGLE or equivalent, you will find many others.  It is ALSO
> possible to find a number of places that indicate that this usage DOES
> violate the rules of "structured programming" - which is why I (originally
> and still) indicate that it may or may not be "valid" in structured
> programming (depending upon your definition).

It isn't valid for my new code.   But I will accept it as being structured
enough until shops get EXIT PARAGRAPH commands available.   At that time my
standards will change so that I won't call GO TO EXIT "structured".

Standards change with the tools available.   "Structured" is not an absolute
term - anymore than "database" is.
```

#### ↳ Re: "Go To" and "Structured programming"

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-04-28T19:30:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<shrqavs5p4u3mp7jeqkrqdsohl5i3sat1m@4ax.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```
On Mon, 28 Apr 2003 00:46:00 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>As a follow-up on another thread ...
>
…[25 more quoted lines elided]…
>to's" or even "drop thru" logic.
An example from my own code, initially created with COBOL-74 where
evaluate was not available. 
So go ahead and kill me.

This is a bit of code I had in a few reporting programs.
Both variabels W-KEYS and W-ITEM1 had a input value from user choice
that decided what order a particular field would show on the report if
shown at all.

...
 perform strings varying w-index from 1 by 1 until w-index > 200.
    * build the key of the report
        PERFORM STRINGS THRU STRINGS-F
                VARYING YYY FROM 1 BY 1
                UNTIL YYY > 10
                OR W-KEYS(YYY) = 0.
        MOVE APONTA TO APONTA-CHAVES.
        MOVE KEY-BAT-2 TO L1-S.
    * build the lines of the report
        PERFORM STRINGS THRU STRINGS-F
                VARYING YYY FROM 1 BY 1
                UNTIL YYY > ULT-ITEM ****This had a maximum of 100
                OR W-ITEM1(YYY) = 0.

       STRINGS1.
           MOVE  W-KEYS(YYY) TO YY Y.
           GO SI1  SI2  SI3  SI4  SI5  SI6  SI7  SI8  SI9  SI10
              SI11 SI12 SI13 SI14 SI15 SI16 SI17 SI18 SI19 SI20
.....
   and all the remaining paragraphs
.....
           DEPENDING ON W-KEYS(YYY).
           GO STRINGS-F.
       STRINGS.
           MOVE W-ITEM1(YYY) TO Y.
           GO SI1  SI2  SI3  SI4  SI5  SI6  SI7  SI8  SI9  SI10
              SI11 SI12 SI13 SI14 SI15 SI16 SI17 SI18 SI19 SI20
.....
   and all the remaining paragraphs
.....
           DEPENDING ON W-ITEM1(YYY).
           GO STRINGS-F.
       SI1.
           MOVE MV-ARM   TO W-ARM.
           IF W-KEY(Y) NOT = 0
              MOVE W-KEY(Y) TO YY
              MOVE W-ARM TO BAT-KEY(YY)
              STRING GV 
                     W-ARM
                     DELIMITED BY SIZE INTO KEY-BAT-2 POINTER APONTA
           ELSE
              STRING GV 
                     W-ARM
                     DELIMITED BY SIZE INTO L1-S POINTER APONTA.
           GO STRINGS-F.
       SI2.
           MOVE MV-CODI  TO W-CODI.
           IF W-KEY(Y) NOT = 0
              MOVE W-KEY(Y) TO YY
              MOVE W-CODI TO BAT-KEY(YY)
              STRING GV 
                     W-CODI
                     DELIMITED BY SIZE INTO KEY-BAT-2 POINTER APONTA
           ELSE
              STRING GV 
                     W-CODI
                     DELIMITED BY SIZE INTO L1-S POINTER APONTA.
           GO STRINGS-F.
    ....
       and all the remaining paragraphs
    ....
       STRINGS-F. EXIT.

Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: "Go To" and "Structured programming"

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-28T15:03:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6UWdnaqC-dRlFTCjXTWcqA@giganews.com>`
- **References:** `<b8if76$gdc$1@slb3.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b8if76$gdc$1@slb3.atl.mindspring.net...
> As a follow-up on another thread ...

Great.

Another deja to discussion.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
