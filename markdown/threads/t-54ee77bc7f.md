[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL Migration

_6 messages · 2 participants · 2015-05 → 2015-08_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### PowerCOBOL Migration

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-05-25T19:44:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cshqejFnj3kU1@mid.individual.net>`

```
If you are a PowerCOBOL user you may be interested in what's happening at:
http://primacomputing.co.nz/primametro/pwrCOBMigration.aspx

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: PowerCOBOL Migration

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-06-14T22:16:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-54ee77bc7f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<cshqejFnj3kU1@mid.individual.net>`
- **References:** `<cshqejFnj3kU1@mid.individual.net>`

```
Pete Dashwood wrote:
› If you are a PowerCOBOL user you may be interested in what's
› happening at:
› http://primacomputing.co.nz/primametro/pwrCOBMigration.aspx
› Pete.

A first glimpse of the actual application is now available at the above
link...
Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: PowerCOBOL Migration

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-08-01T21:47:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-54ee77bc7f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<cshqejFnj3kU1@mid.individual.net>`
- **References:** `<cshqejFnj3kU1@mid.individual.net>`

```
Pete Dashwood wrote:
› If you are a PowerCOBOL user you may be interested in what's
› happening at:
› http://primacomputing.co.nz/primametro/pwrCOBMigration.aspx
This has been an "interesting" exercise which is now coming to completion.

Making the development public has led to some useful feedback and has
actually improved the final product.

This is the first time I have ever tried sharing the development process
with people; usually there are concerns about competitive advantage being
lost or embarrassment if schedules slip or problems can't be solved, and so
on...

In this case I decided that none of that really mattered. If someone else
wants to try the same exercise and they are assisted by my published
designs, well, ... good luck! :-) (I still have a considerable start on you
and a track record of delivering... :-))

As for embarrassment, I think it is unimportant. If things go wrong, it is
probably better to be open about it and maybe someone else can learn from it
as well as me.

We are now a couple of weeks away from delivering a full end-to-end solution
and it will be tight to meet the stated deadline of 23rd August.

I didn't HAVE to set a date (and certainly not publicly) but it has the
effect of focusing the mind... :-)

Many thanks to those who have been re-visitors on the link above; it is
encouraging to see the numbers and it has helped to sustain the effort, just
knowing there are people out there who are interested in this product. (Five
years ago, when I first started thinking about it, there was absolutely no
interest at all. Not a single response. I spoke with some PowerCOBOL users
who agreed they were stuck for the future but they believed the vendor at
the time (Alchemy Software) would probably offer something. (Instead, they
sold out to GT Software who currently have no interest in PowerCOBOL at all
and don't even list the product on their website as one of the products they
sell...)

It is a sad fact that PC COBOL developers have had a pretty rough time
historically...

Micro Focus shafted their Visual Object COBOL (VISOC) customer base (one of
the things that led me to Fujitsu) and Fujitsu has had a fairly sad history
of very poor customer support (at least under Alchemy; can't speak about GT
Software...). And yet both companies have excellent COBOL products. And
both companies are better now than they were then...

I was very impressed by PowerCOBOL and used it extensively back in the late
1990s for developing both applications and components. Like many other COBOL
programmers, I found PowerCOBOL to be an excellent platform for learning
about and understanding the interrupt driven paradigm, as opposed to the
traditional COBOL procedural paradigm, and it certainly eased the transition
into OO COBOL and component based design for me.

So why would the vendor abandon it and leave everyone who bought it with no
way to modernize?

I can only speculate, but I reckon they had it developed under contract in
Japan and the original designers and writers have moved on. There is a major
flaw in it, inasmuch as it is not possible to update PowerCOBOL projects
under program control (NetCOBOL projects keep the COBOL source separate from
the project wrapper, but PowerCOBOL projects don't...) so this prevents
batch updates of source. It is also showing its age in terms of the Form
controls that are available and Windows Forms with Visual Studio is a much
more powerful design surface for GUI development.

A great deal of thought has gone into the new PRIMA tool for migrating
PowerCOBOL and it will support both managed and unmanaged (native) COBOL in
the code-behind, as well as the .Net languages (C# and VB.Net) and C++. Java
can be supported, but it requires CORBA brokerage of COM components and it
is a bit "messier"...

With Visual Studio for the design surface and a mix of whatever languages
you want (including COBOL) for the code-behind, current PowerCOBOL users
will be well served to meet the future WITHOUT having to throw away their
current PowerCOBOL application code and WITHOUT having to re-build every
PowerCOBOL screen from scratch.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: PowerCOBOL Migration

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-08-02T10:26:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-54ee77bc7f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-54ee77bc7f-p3@usenetarchives.gap>`
- **References:** `<cshqejFnj3kU1@mid.individual.net> <gap-54ee77bc7f-p3@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:

[snip]

› So why would the vendor abandon it and leave everyone who bought it with no
› way to modernize?

As my Sainted Paternal Grandfather - may he sleep with the angels - used
to answer his son's progeny:

'Grampa, why did that store go out of business?'

'They went out of business because they were making soooooo much money
that they didn't have time to count it.'

DD
```

###### ↳ ↳ ↳ Re: PowerCOBOL Migration

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-08-02T20:20:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-54ee77bc7f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-54ee77bc7f-p4@usenetarchives.gap>`
- **References:** `<cshqejFnj3kU1@mid.individual.net> <gap-54ee77bc7f-p3@usenetarchives.gap> <gap-54ee77bc7f-p4@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[12 more quoted lines elided]…
› that they didn't have time to count it.'

I have no idea whether PowerCOBOL was profitable to the various vendors, but
I imagine it was.

I guess if you no longer have the wherewithal to support a product , you
might decide to drop it.

For myself, if I were in that sitaution, I would ensure that everybody who
bought it was offered a way out (at no or minimal cost to them) before I
would drop it.

In the case of PowerCOBOL they haven't even officially disavowed it... just
left a user base in limbo.

It is shabby treatment and it is unnecessary. They could have been up-front
and said something like: "We are no longer able to support this product and
recommend that you seek alternative ways to develop GUI applications.
(Suggested alternative products list: Windows Forms, WPF, Flexus
solutions... etc.)"

At least people would know where they stood and could plan for the future.

But that is tantamount to admitting that there are alternative FREE
products, as long as you move off COBOL... and COBOL vendors don't want you
doing that.

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: PowerCOBOL Migration

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2015-08-05T09:09:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-54ee77bc7f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-54ee77bc7f-p5@usenetarchives.gap>`
- **References:** `<cshqejFnj3kU1@mid.individual.net> <gap-54ee77bc7f-p3@usenetarchives.gap> <gap-54ee77bc7f-p4@usenetarchives.gap> <gap-54ee77bc7f-p5@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[16 more quoted lines elided]…
› I imagine it was.
 
› Many things can be imagined.
 
› I guess if you no longer have the wherewithal to support a product , you 
› might decide to drop it.

Many things can be guessed at.

At least two things are equally and absolutely certain:

1) It is very common to exit a line of business that is making so much
money that there's an inability to count it.

2) I am the King of England. God Save the Me!

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
