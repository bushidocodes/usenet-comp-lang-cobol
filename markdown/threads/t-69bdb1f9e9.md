[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Reengineering Tools

_6 messages · 5 participants · 1999-05_

---

### COBOL Reengineering Tools

- **From:** "Robert Williard" <rwilliard@home.com>
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com>`

```
Can anyone recommend COBOL reengineering tools that they have used (or stay
away from)?  I'm looking for tools that can help simplify the maintenance of
an old COBOL MVS application.

--Bob (RWilliard@Home.com)
```

#### ↳ Re: COBOL Reengineering Tools

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373D2F67.57239FCE@att.net>`
- **References:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com>`

```
Robert Williard wrote:
> 
> Can anyone recommend COBOL reengineering tools that they have used (or stay
…[3 more quoted lines elided]…
> --Bob (RWilliard@Home.com)

I did a lot of this about 10 years ago and liked Retool a lot. If memory
(not RAM) serves, the company was CDSI in Rockville, MD. I had a lot of
experience with the Peat, Marwick product (a companion to PATHVU) whose
name escapes me now - I was underwhelmed. 

I'm sure all these products have evolved greatly over the years
(although I still prefer the 1990 version of Retool to IBM's CSF , circa
1995, a lot).

Email me privately if you're interested, I'm pretty sure I still have
the CDSI president's business card, which might make a good starting
point.

Bill Lynch

PS: Regarding reengineering services companies, avoid anything to do
with the Mellingers and/or Allen Stern like the plague infected with
Ebola (last name I knew was Platform Reengineering ...).
```

##### ↳ ↳ Re: COBOL Reengineering Tools

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373E316C.A2C50721@worldnet.att.net>`
- **References:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com> <373D2F67.57239FCE@att.net>`

```
William Lynch wrote:
> 
> Robert Williard wrote:
…[15 more quoted lines elided]…
> (snip)

I had some experience with IBM's CSF (COBOL Structuring Facility) in the
early 1990's.  It was set up to run from panels in TSO, and they were a
lot of options you could specify to your own tastes.  You could reformat
a program with all paragraphs as sections for example, or set you
indentation to 3 columns instead of 4.  I think there was some option to
let you split the program in a main with subprograms, but I never tried
that out.

I would have preferred a pure batch job setup, due to my lack of
experience with TSO.  I actually did use IBM CSF to restructure a few
programs that were installed back to production.  CSF could convert from
OS/VS COBOL to COBOL II (batch or CICS).  It would eliminate all the
GOTO's and ALTER's from your program.  It could add comments to a
paragraph indicating where it was called from.  IBM strongly recommended
you test the generated program to verify it still did exactly what the
old program did, but I never found any problems with that.

CSF would remove dead code.  You generally ended up with fewer paragraph
names that in the spaghetti-code input.  My first thought was this was
great tool, but there are disadvantages.  CSF would produce a correctly
structured program, but if the datanames and paragraph names were
cryptic in the input they were still cryptic in the output.  I was
hoping it would create a beautiful program from a trashy one, but all it
did was get rid of the spaghetti control flow.  There's still some value
in that.

They finally dropped the license for IBM CSF, because they couldn't find
anyone who ever used it except me.

I think there was a product called RECODER in the same time frame that
did essentially the same thing.  I don't remember the name of the
vendor, because I never got to evaluate the product, just saw the
colorful brochure.
```

###### ↳ ↳ ↳ Re: COBOL Reengineering Tools

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3740FC86.D613864E@att.net>`
- **References:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com> <373D2F67.57239FCE@att.net> <373E316C.A2C50721@worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> William Lynch wrote:
> >
(snip)

> I would have preferred a pure batch job setup, due to my lack of
> experience with TSO.  I actually did use IBM CSF to restructure a few
…[5 more quoted lines elided]…
> old program did, but I never found any problems with that.

I had problems with CSF in which the restructured source gave me compile
errors. I experimented with & gave up on CSF more than once (the product
was upgraded & improved - I'm not that big a masochist).

> CSF would remove dead code.  You generally ended up with fewer paragraph
> names that in the spaghetti-code input.  My first thought was this was
…[13 more quoted lines elided]…
> colorful brochure.

IIRC, RECODER was one of the big four in COBOL restructuring tools,
which had a lot of play in the 2nd half of the 80's. I think RECODER
came from a company near Boston, whose name escapes me. It was heavily
oriented toward the application of algorithms to structure a program,
but the result wasn't very readable.

The Peat, Marwick product I couldn't remember was RETROFIT. The output
was pretty good, i.e., readable & structured; but the product didn't
handle some common problems, i.e., logic "knots".

SUPERSTRUCTURE was written by the guy (again, whose name escapes me) who
went on to produce RETOOL, after the original company was acquired by
CDSI. As I said before, I liked this product a lot.

The 4th entry was IBM's CSF.

Regards,
Bill Lynch
```

#### ↳ Re: COBOL Reengineering Tools

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3741753b.2226162@news.teo-computer.com>`
- **References:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com>`

```
On Sat, 15 May 1999 01:42:14 GMT, "Robert Williard"
<rwilliard@home.com> wrote:

>Can anyone recommend COBOL reengineering tools that they have used (or stay
>away from)?  I'm looking for tools that can help simplify the maintenance of
…[4 more quoted lines elided]…
>


ViaSoft has this capability.  It's been a long time (@5yrs) since I've
used it.   It can help in tactical maintenance needs, but always be
careful.  

Re-engineering should always be carried out by a knowledgable
programmer/analyst.  Any re-engineering tool, is just that:  A tool.
How it is used, and how well it is used will vary from programmer to
programmer.



Tim Oxler
Teo Computer
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

##### ↳ ↳ Re: COBOL Reengineering Tools

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3749A915.2C222C4A@semdesigns.com>`
- **References:** `<Wh4%2.57$Fz2.12@news.rdc1.az.home.com> <3741753b.2226162@news.teo-computer.com>`

```
Tim Oxler wrote:

> On Sat, 15 May 1999 01:42:14 GMT, "Robert Williard"
> <rwilliard@home.com> wrote:
…[5 more quoted lines elided]…
> >--Bob (RWilliard@Home.com)

We offer re-engineering tools usable for COBOL, and as a demonstration, have used
them to implement
a code clone detector and remover.   See http://www.semdesigns.com.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
