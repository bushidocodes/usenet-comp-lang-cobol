[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Yet another approach to the "Telco" challenge

_3 messages · 2 participants · 2004-05_

---

### Yet another approach to the "Telco" challenge

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-15T20:32:12+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<g7vpc.1587$H_3.67@newsread1.news.pas.earthlink.net>`

```
I have created (yet another) version of the COBOL "Telco" application.

This uses the "Standard" (I have stuck to the '85 Standard) "Report Writer"
feature.  For those, not familiar with the "debate" - this feature tends to be
"loved" or "hated" among many large COBOL shops.  The feature was optional in
the '85 Standard and some compilers don't have "native" support for it. It is,
however, a REQUIRED part of the ISO 2002 Standard.

I haven't (ever) created a production RW program using the Fujitsu compiler, so
some of the features that I thought I knew, didn't work quite as I expected, but
the posted version DOES work as required.  I have not posted "timing" results -
because with the way RW works, it is virtually impossible to separate out the
computations (for the running totals, for example) from the I/O.

I was pleasantly surprised that using the Fujitsu compiler, this added some -
but not much to the run-time of the program (with the million records).  For
those who look at it, "obviously" the data division is longer - but the
procedure division is relatively significantly reduced.   This is because this
is a "data driven" approach to the application specification.

The source code for this variation is available at:
   http://home.netcom.com/~wmklein/dox/TELCORW.TXT

Obviously (???) this type of approach would be most "cost-effective" with a
"real world" report output specification, i.e. one with page heading/footings;
control breaks and totals, etc.  However, I think that comparing this with the
other versions might be of interest to those comparing COBOL language
possibilities.

(I think this would "best" compare to something like a SAS solution to the
problem - rather than a "procedural language" solution)
```

#### ↳ Re: Yet another approach to the "Telco" challenge

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-15T17:09:14-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10ad54hffkvgb3c@corp.supernews.com>`
- **In-Reply-To:** `<g7vpc.1587$H_3.67@newsread1.news.pas.earthlink.net>`
- **References:** `<g7vpc.1587$H_3.67@newsread1.news.pas.earthlink.net>`

```
William M. Klein wrote:

> I have created (yet another) version of the COBOL "Telco" application.
> 
…[4 more quoted lines elided]…
> however, a REQUIRED part of the ISO 2002 Standard.

[snip]

> For
> those who look at it, "obviously" the data division is longer - but the
> procedure division is relatively significantly reduced.   This is because this
> is a "data driven" approach to the application specification.

This is precisely why I'm in the "love" category.  Report Writer takes 
all the formatting, extra moves, and line counting out of your procedure 
division, and lets you focus on obtaining the data and reporting on it.

About the only thing I would add would maybe be some functions that you 
could use in the "Source" statement, something like "SOURCE FUNCTION 
AVERAGE (myVar1  myVar2  myVar3)" - but it's not overly difficult to set 
up "extra" working-storage variables for these.  Most of the time, we 
need the data exactly as it is in the database.
```

##### ↳ ↳ Re: Yet another approach to the "Telco" challenge

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-15T22:28:28+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<gQwpc.1755$SZ4.1101@newsread2.news.pas.earthlink.net>`
- **References:** `<g7vpc.1587$H_3.67@newsread1.news.pas.earthlink.net> <10ad54hffkvgb3c@corp.supernews.com>`

```
The ISO 2002 Standard enhanced RW - so you MAY use FUNCTION (or even OO objects)
in SOURCE statements.  You may also use "generic" arithmetic expressions.  I
know of one implementation already supporting this - but I don't have it on my
computer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
