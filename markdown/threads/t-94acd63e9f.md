[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL to Perl

_7 messages · 6 participants · 2000-01_

---

### COBOL to Perl

- **From:** Augustine Daimler <perl.news@bigfoot.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386E8DF6.683B@bigfoot.com>`

```
Has anyone heard of a (Perl-)program that converts COBOL source code to
Perl?
```

#### ↳ Re: COBOL to Perl

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ic9v6ssinoh3fnmj1t3ad4v5723p79tisj@4ax.com>`
- **References:** `<386E8DF6.683B@bigfoot.com>`

```
Augustine Daimler <perl.news@bigfoot.com> wrote:

>Has anyone heard of a (Perl-)program that converts COBOL source code to
>Perl?

being the resident expert on practically anything computer, i can say
that there *might* be a product out there, but if you bought it, don't
count on it working for anything with less than perfect code.

and some constructs may not convert very well. the worst construct, i
could see, would be perl's associative arrays and cobols indexed
files. of course, it's been 1 year since i looked at perl, and maybe
it has indexed files now. then you have your go-tos, and alter
statements.

in any case, if you want to run mainframe code for the internet, go
for cobolhtml or some product, and skip the perl transformation.

using alternate news server source.
reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

##### ↳ ↳ Re: COBOL to Perl

- **From:** sitaram@dimensional.com (Sitaram Chamarty)
- **Date:** 2000-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn8740fa.8mk.sitaram@japh.unidata.com>`
- **References:** `<386E8DF6.683B@bigfoot.com> <ic9v6ssinoh3fnmj1t3ad4v5723p79tisj@4ax.com>`

```
On Sun, 02 Jan 2000 15:10:39 -0500, G Moore <gvwmoore@spam.ix.netcom.com> wrote:

>>Has anyone heard of a (Perl-)program that converts COBOL source code to
>>Perl?

>being the resident expert on practically anything computer, i can say
>that there *might* be a product out there, but if you bought it, don't

Highly unlikely :-)

>count on it working for anything with less than perfect code.

Agreed.

>and some constructs may not convert very well. the worst construct, i
>could see, would be perl's associative arrays and cobols indexed
>files. of course, it's been 1 year since i looked at perl, and maybe

Why would any Perl construct be an issue in converting _to_ perl?
IMO the biggest problems will be REDEFINES, RENAMES, and ALTER.
Followed by GOTO.  And all the "extensions" that many COBOLs have
will be in between somewhere.
```

###### ↳ ↳ ↳ Re: COBOL to Perl

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4ga7sk6c88tbo1csa1fvmti9lt741seog@4ax.com>`
- **References:** `<386E8DF6.683B@bigfoot.com> <ic9v6ssinoh3fnmj1t3ad4v5723p79tisj@4ax.com> <slrn8740fa.8mk.sitaram@japh.unidata.com>`

```
sitaram@dimensional.com (Sitaram Chamarty) wrote:

>>and some constructs may not convert very well. the worst construct, i
>>could see, would be perl's associative arrays and cobols indexed
>>files. of course, it's been 1 year since i looked at perl, and maybe

>Why would any Perl construct be an issue in converting _to_ perl?

because if you want to convert correctly with *any* chance of it
working at normal speed, it's bet to convert the indexed file
constructs to associative arrays (or, you could find a perl module
which works with indexed files, but then your perl programmers would
have to learn an extra module.). also, alternate keys with duplicates
would fail, so far as an associate array conversion.

it would be an interesting project, if anyone paid me to do it. but it
surely wouldn't make any money.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: COBOL to Perl

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387876B9.62CE3621@zip.com.au>`
- **References:** `<386E8DF6.683B@bigfoot.com> <ic9v6ssinoh3fnmj1t3ad4v5723p79tisj@4ax.com> <slrn8740fa.8mk.sitaram@japh.unidata.com> <i4ga7sk6c88tbo1csa1fvmti9lt741seog@4ax.com>`

```
G Moore wrote:
> 
> sitaram@dimensional.com (Sitaram Chamarty) wrote:
…[16 more quoted lines elided]…
> it surely wouldn't make any money.

I reviewed an article in the Cobol issue of some magazine.  There was
an interesting article on code conversion from one language to
another.

I basically said it was impossible to do an adequate job.  There are
too many decisions to the process.  How do you map pic 9(4) to Perl? 
If you use binary your get something close but not the same.

Automated conversions from one language structure to another leads to
bad results in two languages (is this deja vu?).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: COBOL to Perl

_(reply depth: 5)_

- **From:** x@wins.uva.null (X)
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85blbq$1q3@adam.wins.uva.nl>`
- **References:** `<386E8DF6.683B@bigfoot.com> <ic9v6ssinoh3fnmj1t3ad4v5723p79tisj@4ax.com> <slrn8740fa.8mk.sitaram@japh.unidata.com> <i4ga7sk6c88tbo1csa1fvmti9lt741seog@4ax.com> <387876B9.62CE3621@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> writes:

>How do you map pic 9(4) to Perl? 

Good question.  So let us try, by way of counter example, to convert the
following COBOL program to perl:

DATA DIVISION.
 01 A PIC S9V9999 VALUE -1.
PROCEDURE DIVISION.
 ADD 1.005 TO A.
 DISPLAY A.

the first intuition seems to be:

#!/bin/perl
$A = -1;
$A = $A + 1.005;
print $A, "\n";

but this yields:

0.00499999999999989

>Automated conversions from one language structure to another leads to
>bad results in two languages (is this deja vu?).

indeed.  For in order to get the above correct, you have to emulate the
data type of S9V9999, and the behavior of this data type wrt operations.

Then you hvae to emulate the DISPLAY statement as well, since the above
COBOL program has 

00050+

as its output.

Have fun coming up with a more correct perl program.  

  --XX

for more info read http://adam.wins.uva.nl/~x/con/con.html
```

#### ↳ Re: COBOL to Perl

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ltxb4.1172$W41.23291@dfiatx1-snr1.gtei.net>`
- **References:** `<386E8DF6.683B@bigfoot.com>`

```
Augustine Daimler wrote in message <386E8DF6.683B@bigfoot.com>...
>Has anyone heard of a (Perl-)program that converts COBOL source code to
>Perl?

Wouldn't that be like converting Cindy Crawford into Roseanne?

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
