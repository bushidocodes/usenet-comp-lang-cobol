[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# convert cobol

_5 messages · 3 participants · 2001-06_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Re: convert cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-11T19:44:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B252051.DEE77DF4@home.com>`

```


Bob Wolfe wrote:

> "James. J. Gavan" <jjgavan@home.com> wrote:
>
…[63 more quoted lines elided]…
>

Bob,

Thanks for comments and those from Kevin. I was somewhat 'loose' in my
definition of events being returned - and should have been more
specific, they give back 'results/text' as a result of a Windows event -
whereas I currently will take that event object and return it to the
Business Class as an object reference, pic 9 or pic x, as appropriate.

> COBOL sp2 also supports all of the other major compilers as well.  The
>
…[16 more quoted lines elided]…
>

Now a minor correction on yours above <G>. Pete Dashwood has
successfully developed component modules, (his DECLGEN he offered folks,
is a good case in point) and I can run it because he provides the
FREEBIE Fujitsu runtime (Hint ! Hint ! - somebody is missing out on a
potential market for their product). As yet I haven't used a component
of his 'linked' to Net Express, but there is absolutely no reason why
that shouldn't work either.

Now of course, if and when OO truly gets off the ground, there's no
reason, using a switch acknowledging different operating systems, that
you can't address a different OS. While your SP2 approach is to
acknowledge each different OS in one package,  I would suggest, that in
the majority of instances, most developers are coding primarily for one
platform. I know there will be exceptions, but again think they are
probably very much the minority. On the plus side both SP2 and Screen IO
both allow a developer to switch to his current vendor of choice without
extensive re-writes.

As an example can you visualize Howard coding in OO for Big Blue, but at
the same time producing, (or wanting) a version for PC desktops - which
pieces of furniture do I move out of the house to make way for his vast
disk/tape storage <G>

Jimmy
```

#### ↳ Re: convert cobol

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-12T17:30:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b25a8ca_6@Usenet.com>`
- **References:** `<3B252051.DEE77DF4@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B252051.DEE77DF4@home.com...
>
> Now a minor correction on yours above <G>. Pete Dashwood has
…[6 more quoted lines elided]…
>

The main objection to using Components at the moment is the requirement for
different run time systems.

If the component is written in VB it requires a VB runtime; C++ requires a
C++ runtime and so on...

These two are not so bad because many systems already have these run times
in their Windows\system directory with all the other Dynamic Link Libraries
that are necessary to implement Windows.

(If you don't know it's there then you don't grieve over it...<G>)

One reason why Java Components (Beans) are so effective is because they
DON'T require a "run time" as such (they do require the JVM, but anyone who
has a Browser, probably has this implemented already...)

The main impact of the forthcoming .NET will be its ability to run a single
set of intermediate code and thus remove the need for all these different
run times.

That is one reason why I believe the future belongs to component technology;
once the "inconvenience" of different run times is overcome, there will be
no stopping it.

(Even WITH this inconvenience, many of us are using Components effectively
and deriving great benefit from doing so...)

> Now of course, if and when OO truly gets off the ground, there's no
> reason, using a switch acknowledging different operating systems, that
…[12 more quoted lines elided]…
>

The exact scenario Jimmy describes above (coding OO COBOL simultaneously for
mainframe and PC platforms) should eventuate within the next few years as a
common runtime becomes available. It is very likely the .NET intermediate
code will be produced by mainframe platforms as well as PCs, and this will
lead to running components on the mainframe which may have been written in a
Language which won't even compile on the mainframe!

The Object Code will be all that matters, and this will be encapsulated into
functions and wrapped as Components.

Object Oriented COBOL is more than up to this task, but as long as we have
no standard for it, and no effective mechanism whereby we can define and
iteratively refine a base for it (other than individual vendor's
implementations) it is a sad reality that COBOL will probably "miss the bus"
in this area.

I am already reviewing whether I shall continue to develop components in
COBOL (even when it is definitely the best language for a particular task)
because I have become disillusioned with the constant bickering, pedantry,
and failure to actually achieve anything, which we have seen coming out of
J4. (despite their protestations regarding their heroic efforts).

Frankly, the thought that the Language I have known and loved for 35 years
is now in the hands of people who couldn't organise a piss up in a Brewery,
frightens me...

Maybe with a common run time and excellent vendor implementations (such as
we can expect from Merant and Fujitsu, to name but 2) there will still be a
case for using OO COBOL to develop business components, but it is by no
means certain.

I hope I'm wrong...only time will tell.

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: convert cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-12T22:00:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2691B8.694F4D5E@home.com>`
- **References:** `<3B252051.DEE77DF4@home.com> <3b25a8ca_6@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

>
> The main objection to using Components at the moment is the requirement for
…[8 more quoted lines elided]…
> <snip>

Lots of relevant stuff and I don't need to reiterate what Pete has already
written. To amplify what he has said I wanted to quote from two sources -  be
damned if I can find reference to them.

The first was a very relevant introductory paragraph on Java. So in a very bad
paraphrase, gong from memory, this is what it said :-

"When manufacturers design fridges, freezers, TVs, radios etc etc...... They can
start from ground zero - completely design from scratch. They don't. Having
arrived at an overall design, both due to time factor and cost, and one might
add a proven record that the component works, they look for component parts
which integrate with their design, available from allied industries"

Then the 'lost' quote went on to make the same point about the Java language
providing components........

The second - I believe from InfoWorld, originally passed from Thane to Pete,
then Pete to me :-

The article addresses the fact that the mainland states (is that the correct
phrase ?), are addressing the problem of re-inventing the wheel. They each have
auto/vehicle licensing systems. Parallel -  but local subtleties, because of
state legislation. However, so much of it is 'common components'. Simply put
they are going to design and swap components. Agreed this is an area tied into
one specific 'industry' - but reflect on its impact on programming, but not
constrained to one language, and when spread over all the various categories of
industry.........?

The article above doesn't say it - but COBOL, because of its business acumen -
is up there, front and centre !

Thane or Pete - the link please (Sounds like a Quiz program <G>)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: convert cobol

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-16T14:15:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2b69b9.227800247@news1.attglobal.net>`
- **References:** `<3B252051.DEE77DF4@home.com> <3b25a8ca_6@Usenet.com> <3B2691B8.694F4D5E@home.com>`

```
Jimmy - I don't have a clue what you are talking about as far as the
links go.

On Tue, 12 Jun 2001 22:00:38 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[49 more quoted lines elided]…
>
```

##### ↳ ↳ Re: convert cobol

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-16T14:24:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2b69ee.227853504@news1.attglobal.net>`
- **References:** `<3B252051.DEE77DF4@home.com> <3b25a8ca_6@Usenet.com>`

```
On Tue, 12 Jun 2001 17:30:29 +1200, "Peter E. C. Dashwood"
<dashwood@nospam.enternet.co.nz> wrote:


>The exact scenario Jimmy describes above (coding OO COBOL simultaneously for
>mainframe and PC platforms) should eventuate within the next few years as a
…[7 more quoted lines elided]…
>

Note: For those of you interested MSDN.MICROSOFT.COM and several
echoing sites (including www.adtools.com) are hosting the documents
that are created as part of the standardization process of not only C#
but also the intermediate runtime code.  This is the first time I am
aware of that something akin to object code has been standardized.

>Object Oriented COBOL is more than up to this task, but as long as we have
>no standard for it, and no effective mechanism whereby we can define and
…[3 more quoted lines elided]…
>

In the draf the base class is well defined.  If you are lamenting the
lack of a common class library, I understand,    Serious query:  What,
in your opinion should be included in such a common class library?

>I am already reviewing whether I shall continue to develop components in
>COBOL (even when it is definitely the best language for a particular task)
>because I have become disillusioned with the constant bickering, pedantry,
>and failure to actually achieve anything, which we have seen coming out of
>J4. (despite their protestations regarding their heroic efforts).

I see no "constant bickering" at J4 - and in fact the International
comments we received bear out the fact that we have a good, sound
document.  One interesting fact - The Japanese have always held a
critical eye to the OO portion of the draft.  They have always
submitted requests and clarifications and pointed out any errors or
pitfalls.  In there international comments, there was nary a mention
of anything about the OO portions of the draft.  I found this VERY
encouraging.

As far as your other comments - it doesn't matter at this point.  We
can regret the past all day long, but that gets us nowhere.  Let's
consider the future.  The draft is basically "Frozen" and has been
since we went to FCD.  We are in the "correction" stage at this point,
and the frequency of meetings has increased.  We have 2 more working
meetings before WG4 in November, at which time WG4 will make their
recommendation at to our comment resolution.  There will then be a
vote on the final document and it will be forwarded to ISO.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
