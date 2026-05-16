[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Where is CoBOL

_6 messages · 4 participants · 2009-06_

---

### Where is CoBOL

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-02T07:45:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com>`

```
In this language comparison?

http://gmarceau.qc.ca/blog/2009/05/speed-size-and-dependability-of.html
```

#### ↳ Re: Where is CoBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-03T03:31:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78kuu6F1mf9eqU1@mid.individual.net>`
- **References:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com>`

```
Howard Brazee wrote:
> In this language comparison?
>
> http://gmarceau.qc.ca/blog/2009/05/speed-size-and-dependability-of.html

It disappeared off the chart to the right :-)

I'm going to start learning Stalin... :-)

Pete.
```

#### ↳ Re: Where is CoBOL

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-02T11:40:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h03ili115tj@news7.newsguy.com>`
- **In-Reply-To:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com>`
- **References:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com>`

```
Howard Brazee wrote:
> In this language comparison?
> 
> http://gmarceau.qc.ca/blog/2009/05/speed-size-and-dependability-of.html

The author begins by confusing language and implementation - a
distinction which is important later in the article - and it doesn't
get much better. There's no serious acknowledgment that languages may
be better suited for some purposes rather than others, for example.
And he appears to assume that the implementation of a particular
solution in the data set represents a typical or ideal solution and
implementation in that language, when it may simply be that no one has
supplied the site with a good solution or implementation for that
particular benchmark-language pair.

And while the results are interesting, the author's claims for them
are rather overstated, particularly given the tremendously arbitrary
nature of his data and the subjective aspects of his methodology.

To answer Howard's question: the benchmarks here aren't well-suited to
COBOL. It's debatable whether the benchmarks are chosen well even for
their ostensible purpose - for example, they're run on a very
restricted class of machine, and the rules require that
implementations "avoid library use", which seems completely contrary
to the stated mission of the project. (What are libraries for? To
reduce code size and make good implementations of common functions
available. What's the benchmark project trying to measure? Code size
and performance.)

The benchmarks that I looked at in the suite are CPU-bound
compute-intensive tasks. They're all short programs. I don't think
they say much about how expressive a language is - there's just not
enough to do. Real applications are seldom a single page of code in
any language.
```

##### ↳ ↳ Re: Where is CoBOL

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-02T12:55:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ata25tosk1pgi23o68366nsi1vhl4jve5@4ax.com>`
- **References:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com> <h03ili115tj@news7.newsguy.com>`

```
On Tue, 02 Jun 2009 11:40:58 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>To answer Howard's question: the benchmarks here aren't well-suited to
>COBOL. It's debatable whether the benchmarks are chosen well even for
…[12 more quoted lines elided]…
>any language.

And certainly there are different efficiency needs in running p-code
like code on a PC than in running compiled code in a central computer.
Besides, CoBOL is as efficient as its compiler makes it to be.   How
do we compare XML with compiled Cobol?  And why?
```

###### ↳ ↳ ↳ Re: Where is CoBOL

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-03T11:26:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0674822kt8@news5.newsguy.com>`
- **In-Reply-To:** `<7ata25tosk1pgi23o68366nsi1vhl4jve5@4ax.com>`
- **References:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com> <h03ili115tj@news7.newsguy.com> <7ata25tosk1pgi23o68366nsi1vhl4jve5@4ax.com>`

```
Howard Brazee wrote:
> How do we compare XML with compiled Cobol?  And why?

There's no point in comparing XML with COBOL; XML isn't a programming
language. It's a data representation.

But - and I think this is the point we're both making - comparing
COBOL with another programming language in the fashion described in
this article isn't terribly useful either. There's no obvious
relationship between the lines of code needed to calculate the
Mandelbrot set, or the time it takes to do so, and the requirements of
most real applications.

Even the author's key theoretical innovation - the shape of the plot
of each implementation's results on the graph - can at best only show
whether the language is well-suited for all or only some of the
benchmarks in the set. That's one possible criterion for a programming
language, but not a necessary one. In many cases a domain-specific
language, or one with strengths in particular areas, is a better choice.

I have always (since I first studied them, in the mid-80s) been an
advocate of highly-expressive programming languages, even though most
of my work is in C and COBOL buys my bread. I was pleased to see some
old favorites like OCaml and Lua do well in the article's comparisons.
But it's not worth getting excited about. There are many, many
programming languages with features that make them arguably superior
to the dominant crop. There have been since the earliest days of
high-level languages; LISP is only a few years younger than FORTRAN.
But most software is still terrible, a bug-ridden mess. Better
languages have not fixed that yet.
```

#### ↳ Re: Where is CoBOL

- **From:** btiffin@canada.com
- **Date:** 2009-06-04T17:36:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edbaa1b2-b833-4bbc-9e3b-09fde05c999a@z19g2000vbz.googlegroups.com>`
- **References:** `<j7ba25hojc9v0l9ohu0otkppf0eiqrirgj@4ax.com>`

```
I'll opine that a capable, freely available COBOL hasn't yet had time
to take root, so developers that would feel the need to scratch the
shootout itch have not yet surfaced.  OpenCOBOL could be that ticket
to ride for gaining momentum in "at home" COBOL coding.  TinyCOBOL too
perhaps, but OpenCOBOL is becoming quite the robust system, even
though it lacks Object COBOL features for now.

It's a nice star chart though, given what it is.  But the author
seeing verbosity as a "bad thing" might hurt COBOL's chances at being
placed near the sweet spot of the ideal corner. I prefer grokking
through code once and find verbosity a boon, when compared to, say, 12
characters of Perl code that can take half an hour and four
experiments to come to grips with.   ;)

One coder's expressionism if oft another's puzzle.

Cheers,
Brian

On Jun 2, 9:45 am, Howard Brazee <how...@brazee.net> wrote:
> In this language comparison?
>
…[7 more quoted lines elided]…
> - James Madison
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
