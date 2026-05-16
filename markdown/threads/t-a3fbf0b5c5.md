[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL indentation source code/algorithm

_7 messages · 6 participants · 2003-09_

---

### COBOL indentation source code/algorithm

- **From:** tarun_bhardwaj <member22201@dbforums.com>
- **Date:** 2003-09-09T01:00:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3346333.1063083600@dbforums.com>`

```

Hi !



Could anyone kindly provide me with a source code or an algorithm for
indentation of an unindented COBOL program ? The input to the program
will be an unindented COBOL program and the output will be an indented
COBOL program.

For example, all the "IF's" will be starting in a particular column, all
"ELSE" in a specified column etc.



Iam working on an OS/390 platform.



I request you to kindly take out some time and please help me.

Waiting for your reply,

Regards,

Tarun.
```

#### ↳ Re: COBOL indentation source code/algorithm

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-09T14:45:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bjkp1j$9iv$1@peabody.colorado.edu>`
- **References:** `<3346333.1063083600@dbforums.com>`

```

On  8-Sep-2003, tarun_bhardwaj <member22201@dbforums.com> wrote:

> Could anyone kindly provide me with a source code or an algorithm for
> indentation of an unindented COBOL program ? The input to the program
…[4 more quoted lines elided]…
> "ELSE" in a specified column etc.

I'm curious.   How many programs do you want to do this to?   How valuable is
such indentation?

Have you considered creating editor macros?
```

##### ↳ ↳ Re: COBOL indentation source code/algorithm

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-09T20:20:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mCq7b.2680$c35.2255@newsread1.news.atl.earthlink.net>`
- **References:** `<3346333.1063083600@dbforums.com> <bjkp1j$9iv$1@peabody.colorado.edu>`

```
Also, if using a currently supported COBOL compiler on OS/390 (or z/OS), you
can tell "nesting" levels by looking at the LISTING - and use that (with
some multiplier, e.g. 2 or 4) and figure out how to indent "logically"
related lines.
```

##### ↳ ↳ Re: COBOL indentation source code/algorithm

- **From:** tarun_bhardwaj <member22201@dbforums.com>
- **Date:** 2003-09-10T04:57:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3351744.1063184268@dbforums.com>`
- **References:** `<3346333.1063083600@dbforums.com> <bjkp1j$9iv$1@peabody.colorado.edu>`

```

i haven't used any editor macros. i have to indent all the programs
lying in my current PDS.

this program will act as a filter for all the unindented cobol programs
that will be developed by me in the future. this program will help me to
save a lot of precious time which otherwise i would have "wasted" in
indenting the programs during development.



Originally posted by Howard Brazee 

> On  8-Sep-2003, tarun_bhardwaj <member22201@dbforums.com> wrote:

>

> > Could anyone kindly provide me with a source code or an
>     algorithm for

> > indentation of an unindented COBOL program ? The input to the
>     program

> > will be an unindented COBOL program and the output will be an
>     indented

> > COBOL program.

> > For example, all the "IF's" will be starting in a particular
>     column, all

> > "ELSE" in a specified column etc.

>

> I'm curious.   How many programs do you want to do this to?   How
> valuable is

> such indentation?

>

Have you considered creating editor macros? 
```

###### ↳ ↳ ↳ Re: COBOL indentation source code/algorithm

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-10T16:18:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m9I7b.136319$3o3.9692087@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3346333.1063083600@dbforums.com> <bjkp1j$9iv$1@peabody.colorado.edu> <3351744.1063184268@dbforums.com>`

```

"tarun_bhardwaj" <member22201@dbforums.com> wrote in message
news:3351744.1063184268@dbforums.com...
|
| i haven't used any editor macros. i have to indent all the programs
…[5 more quoted lines elided]…
| indenting the programs during development.

Then try the method William Kline suggested.
It's probably the easiest way to accomplish what you want.

|
|
…[36 more quoted lines elided]…
| Posted via http://dbforums.com
```

#### ↳ Re: COBOL indentation source code/algorithm

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2003-09-11T09:07:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f608014$1@giga.realtime.net>`
- **References:** `<3346333.1063083600@dbforums.com>`

```
"tarun_bhardwaj" <member22201@dbforums.com> wrote in message
news:3346333.1063083600@dbforums.com...
> Could anyone kindly provide me with a source code or an algorithm for
> indentation of an unindented COBOL program ? The input to the program
> will be an unindented COBOL program and the output will be an indented
> COBOL program.

See http://www.semdesigns.com/Products/Formatters/index.html.
There's a COBOL formatter there that will do that.
```

#### ↳ Re: COBOL indentation - OS/VS Cobol

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2003-09-11T20:46:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vacnbtaub4WuPyiXTWQlg@giganews.com>`
- **References:** `<3346333.1063083600@dbforums.com>`

```
If your shop happens to have the old IBM OS/VS Cobol compiler
lying around it had compile options to do just exactly what
your wanting. In fact this compiler as obsolete as it is had
a lot of useful stuff that later compilers do not.

If you use compile option FDECK along with LSTONLY or LSTCOMP
it will put to DD SYSPUNCH a reformatted source "deck" that
indents under the IF's , lines up the ELSE's, picture clauses,
level numbers and stuff, puts one verb on a line and so on.
It was a very handy little thing.

There are also options STATE and FLOW. These write debugging
information to DD SYSDBOUT. STATE prints the line of code that
abended and FLOW prints a trace of up to the previous 99
paragraphs names prior to the abend. Also, a handy little
thing.

This is probably useless information unless you have a really
old program. It likely would do nothing if it encountered
a "function" or an "end-if". Nevertheless, these were nice
features that I could still really use. I wish IBM would have
included them new compilers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
