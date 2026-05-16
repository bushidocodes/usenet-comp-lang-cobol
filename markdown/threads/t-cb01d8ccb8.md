[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Anyone ever heard of JSB?

_4 messages · 3 participants · 2003-08_

---

### Anyone ever heard of JSB?

- **From:** "Georgie" <kriweed@yahoo.com>
- **Date:** 2003-08-12T17:40:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f390a90$0$310$ba620e4c@reader0.news.skynet.be>`

```
I'm on to a new contract. In the required specs they mentioned that
knowledge of JSB was a plus. I don't have a clue of what JSB is. They only
mentioned it as some kind of COBOL generator (but I'm not sure of it)
It's in a DLI, COBOL II shop.

Thanks for helping me.
```

#### ↳ Re: Anyone ever heard of JSB?

- **From:** "Georgie" <kriweed@yahoo.com>
- **Date:** 2003-08-14T08:45:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f3b302c$0$886$ba620e4c@reader1.news.skynet.be>`
- **References:** `<3f390a90$0$310$ba620e4c@reader0.news.skynet.be>`

```
Well it was JSP (Jackson structured programming, by mr. Michael Jackson
;-))and not JSB.

"Georgie" <kriweed@yahoo.com> wrote in message
news:3f390a90$0$310$ba620e4c@reader0.news.skynet.be...
> I'm on to a new contract. In the required specs they mentioned that
> knowledge of JSB was a plus. I don't have a clue of what JSB is. They only
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Anyone ever heard of JSB?

- **From:** "Kjeld Hansen" <paabol@12mail.dk>
- **Date:** 2003-08-14T21:43:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f3be64c$0$32518$edfadb0f@dread16.news.tele.dk>`
- **References:** `<3f390a90$0$310$ba620e4c@reader0.news.skynet.be> <3f3b302c$0$886$ba620e4c@reader1.news.skynet.be>`

```
When I started working in professional IT-development 16 years ago, the
installation had some 40 source code modules done in Jackson Structured
Programming on IBM mainframe.

I didn't get training in JSP, since the organisation already had decided not
to do further development in this tool, but I did some maintenance work on
existing modules in 3-4 years.

Among the features (as I recall by heart, I don't have any documents on JSP
left) were:

The structuring tool enforced you to code processing in both the true (if)
and the false (else) conditions. It also featured a case structure.
You could generate structure diagrams of your modules, but that were in the
days were all host print were character based line printing, so even a
simple module produced more than 10 pages of  boxes and lines that quickly
became more difficult to navigate than the source code.

One of the major drawbacks was that the tool as a precompiler produced Cobol
code with lots of go to's. Even worse, since JSP not at that time supported
test and debugging on the JSP source, you had to do all debugging on the
Cobol not-so-structured code with a lot of JSP-generated paragraph names in
it.

A good thing was that JSP let you declare cobol sections where you could
code native Cobol to your hearts content. ;-)

  Good luck,
Kjeld P. Hansen
Systems Designer,
Fredericia, Denamrk


"Georgie" <kriweed@yahoo.com> skrev i en meddelelse
news:3f3b302c$0$886$ba620e4c@reader1.news.skynet.be...
> Well it was JSP (Jackson structured programming, by mr. Michael Jackson
> ;-))and not JSB.
…[4 more quoted lines elided]…
> > knowledge of JSB was a plus. I don't have a clue of what JSB is. They
only
> > mentioned it as some kind of COBOL generator (but I'm not sure of it)
> > It's in a DLI, COBOL II shop.
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Anyone ever heard of JSB?

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-08-15T16:31:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0308151531.173e8135@posting.google.com>`
- **References:** `<3f390a90$0$310$ba620e4c@reader0.news.skynet.be> <3f3b302c$0$886$ba620e4c@reader1.news.skynet.be> <3f3be64c$0$32518$edfadb0f@dread16.news.tele.dk>`

```
Bottom posting this time - snipped a bit

"Kjeld Hansen" <paabol@12mail.dk> wrote in message news:<3f3be64c$0$32518$edfadb0f@dread16.news.tele.dk>...
> When I started working in professional IT-development 16 years ago, the
> installation had some 40 source code modules done in Jackson Structured
…[36 more quoted lines elided]…
> > > It's in a DLI, COBOL II shop.

I think you slate JSP too much.  Michael Jackson was one of the first
proponents of avoiding the use of GO TO and his JSP was based around
that idea.  I admit I don't like using the method myself as I think
that the use of structure charts is unwieldy in much the same way as
you describe and makes it harder to see the logic.  However, in the
context of the time, it was probably an improvement on the way many
organisations used flowcharts.

I was taught to use paragraphs (sections weren't even considered,
though the original COBOL standard included them with what I thought
was brilliant foresight), the paragraph names were taken from the grid
identifiers on the flowchart (supplied by IBM).  An additional letter
or two was used to uniquely identify each flowchart page.  Notes were
discouraged on the grounds that they often weren't accurate,
especially after several amendments.  However, datanames were supposed
to be meaningful.  Flowcharts were supposed to be kept up-to-date, but
rarely were.  In mitigation of this method, programs were to be
subdivided into modules of no more than 400 lines of code and were to
fully specified to the point that a programmer could write them
without further reference to the author (usually!!).  Practice at
writing module specification was a useful step towards writing program
and system specifications.  Despite the handicap of using flowcharts
in this way, the resultant programs were fast and accurate, and were
produced quite quickly.  Maintaining them could be a pain though.

I think his idea of corresponding data and procedure structures was
worth investigating as a theoretical exploration, though it only works
effectively for fairly simple logic and doesn't work with sorts, etc. 
I think that another of the disadvantages of JSP was that it
unnecessarily discouraged many people from using internal sorts,
sometimes/often external sorts are more appropriate, but certainly not
always.

Michael Jackson also proposed the use of pseudo-code though with some
rather idiosyncratic names, again he probably wasn't the first, but
was a strong and influential advocate.

I suspect that many organisations adopted aspects and parts of his
techniques in ways of which he wouldn't approve.

Edsger Djikstra was the first published proponent of the avoidance of
the use of GO TOs, though one doesn't know for sure how many other
people were beginning to have similar ideas around the same time. 
Apart from having the idea he also propounded it very lucidly, to the
point that when in 1977 I was considering whether to buy his book
(actually a monograph, published in the same volume as two other
authors) or Michael Jackson's, I chose his, despite it being written
for an Algol type language when I had previously learned mainly COBOL,
a little Assembler, very little Fortran and no ALGOL.  Michael
Jackson's book on structured programming was written using COBOL to
illustrate his method, if you are interested, then his book is the
most authoritative source on his method, most organisations that say
they use JSP, only use bits of it, usually the structure charts in my
experience.

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
