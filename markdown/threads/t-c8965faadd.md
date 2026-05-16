[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/MVS and Quotes

_16 messages · 9 participants · 1999-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL/MVS and Quotes

- **From:** "Greg McDougall" <dougall@bigfoot.com>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c98ok$4bn$1@plug.news.pipex.net>`

```
We are currently moving from COBOL II to COBOL/MVS on MVS v5.2. One
thing we have noticed is that, unlike COBOL II which (depending on the
compiler directive) insisted on either quotes or apostrophes in the
code, COBOL/MVS seems not to care either way and allows the mixing of
these within a program.

The only seemingly relevant compiler option I can find talks about the
assumed literal in the ALLQUOTE statement (which I assume refers to
INSPECT?). We went through some degree of pain standardising on the
apostrophe - was this a waste of time? We would like the compiler to at
least flag any instances of these mixed usage.

Greg
```

#### ↳ Re: COBOL/MVS and Quotes

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990311160534.20208.00000926@ng119.aol.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net>`

```
Greg McDougall <dougall@bigfoot.com> writes ...

>We are currently moving from COBOL II to COBOL/MVS on MVS v5.2. One
>thing we have noticed is that, unlike COBOL II which (depending on the
>compiler directive) insisted on either quotes or apostrophes in the
>code, COBOL/MVS seems not to care either way and allows the mixing of
>these within a program.

This is correct. A non-numeric literal may now be bounded by single quotes or
double quotes, as long as the beginng and ending delimiters are the same. So
you can have "Bob's News" in one value clause and 'Department 515' in another
in the same program.


>
>The only seemingly relevant compiler option I can find talks about the
>assumed literal in the ALLQUOTE statement (which I assume refers to
>INSPECT?). 

Acutally, the compiler option now only impacts the figurative constant QUOTE
(also QUOTES). This constant may be used as a value, in a move, in a compare,
or in an INSPECT statement.


>We went through some degree of pain standardising on the
>apostrophe - was this a waste of time? We would like the compiler to at
>least flag any instances of these mixed usage.

It wasn't necessarily a waste of time at the time. It helped your shop be
consistent when it mattered.

I consider this new behavior as more liberating, saying, "it won't hurt you to
use either apaostrophes or quotes" (while still flagging you if your ending and
beginning delimiters aren't the same). You can still have your standard
(although I would tend to loosen up on that one), but the compiler will no
longer enforce it.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c9g6m$sf2@dfw-ixnews5.ix.netcom.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com>`

```
Just to add to what Steve has already said,

1) The APOST/QUOTE compiler option is STILL valid - but the only thing that
it controls is how the "QUOTE" figurative constant is set up.

2) The draft of the next Standard has this same extension (of allowing BOTH
single and double quotes - aka apostrophe and quotation marks - as the
delimiter for alphanumeric literals)

3) The history of "single-quote" and IBM (and IBM-compatible) compilers has
to do with what characters were "easy" to put on punch cards.  Hardly an
issue today.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e85c35@news3.us.ibm.net>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com>`

```
William M. Klein wrote in message <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com>...
>3) The history of "single-quote" and IBM (and IBM-compatible) compilers has
>to do with what characters were "easy" to put on punch cards.  Hardly an
>issue today.


But even today, APOST is lower case and QUOTE is upper case and thus a bit
harder to type... so this is a welcome change.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** "Greg McDougall" <dougall@bigfoot.com>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ceguq$ld2$1@plug.news.pipex.net>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com>`

```
Thank you to William, Steve, and the others who responded. I'll pass on
the clarifications.

Thanks,

Greg
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f2e5e4.11159386@netnews>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com>`

```
'Twas Thu, 11 Mar 1999 16:30:24 -0600, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

>3) The history of "single-quote" and IBM (and IBM-compatible) compilers has
>to do with what characters were "easy" to put on punch cards.  Hardly an
>issue today.

I have never been a fan of IBM, and I believe there are several ways the
COBOL standard is poorer because of them.  However, in this case IBM is
being trashed where they did _nothing_ wrong.

The early COBOL standards assumed that each vendor used their own
proprietary character set.  The vendor was required to choose some
character -- ANY character -- and call it the quote character.  They could
have used # or % or ^ or ? or even a two character code, but IBM happened
to choose ', because it was already on the keyboard of most keypunch
machines.  This was fully compliant with X3.23-1968, X3.23-1974, and
X3.23-1985, because none of them ever required that the quote character
map to any specific graphic.  

There is now a general consensus that the quote character should map to
Ascii character X"22", but even the current draft doesn't directly say
that.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d7oo8$ah8@dfw-ixnews10.ix.netcom.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com> <36f2e5e4.11159386@netnews>`

```
Randall,
  Are you certain of this?  The '74 and '85 Standards (I don't know about
the '68) all reference the ANSI and ISO Standards (648) in their definition
of the COBOL character set.  I know that this has some flexibility in it -
but I THINK that it does define what a "quote" is.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f8af1d.387504663@netnews>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <7c9g6m$sf2@dfw-ixnews5.ix.netcom.com> <36f2e5e4.11159386@netnews> <7d7oo8$ah8@dfw-ixnews10.ix.netcom.com>`

```
'Twas Tue, 23 Mar 1999 03:59:47 -0600, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

>Randall,
>  Are you certain of this?  The '74 and '85 Standards (I don't know about
>the '68) all reference the ANSI and ISO Standards (648) in their definition
>of the COBOL character set.  I know that this has some flexibility in it -
>but I THINK that it does define what a "quote" is.

Well, with COBOL-85 I'm not sure, because I never saw the final standard.
In COBOL-74  ASCII was referenced for data representation, but it didn't
really equate that with the COBOL character set used to specify the
program (what's called the character repetoire in the current draft).
COBOL-74 still had that stuff about two character symbols.
```

##### ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e8895f.771141440@news1.ibm.net>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com>`

```
On 11 Mar 1999 21:05:34 GMT, scomstock@aol.com (S Comstock) wrote:

>Greg McDougall <dougall@bigfoot.com> writes ...
>
…[10 more quoted lines elided]…
>

I'll have to check.  Some compiler option we are using (with the
latest COBOL for this and that) prevents me from mixing - I still have
to use Apostrophes with our directives.  I'll see if I can trace it
down for you. (and kill it <G>).
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cau3g$da@sjx-ixn6.ix.netcom.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net>`

```
Thane Hubbell wrote in message <36e8895f.771141440@news1.ibm.net>...
  <snip>
>
>I'll have to check.  Some compiler option we are using (with the
…[3 more quoted lines elided]…
>

Which EXACT compiler and release are you actually using?  I think this
change was NOT present in the original COBOL/370 - and I can't remember
whether it was added with COBOL for MVS & VM or only came in with COBOL for
OS/390 & VM.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-1iwdw2Z27YyY@Dwight_Miller.iix.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net> <7cau3g$da@sjx-ixn6.ix.netcom.com>`

```
On Fri, 12 Mar 1999 11:33:46, "William M. Klein" 
<wmklein@nospam.netcom.com> wrote:

> Thane Hubbell wrote in message <36e8895f.771141440@news1.ibm.net>...
>   <snip>
…[11 more quoted lines elided]…
>

Well, I get to eat crow.  With this release of the compiler mixing 
quotes and apostrophes (as long as opening and closing match) works 
just fine.

Here's the release:
PP 5648-A25 IBM COBOL for OS/390 & VM  2.1.1
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 5)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36EA00B4.8556234F@att.net>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net> <7cau3g$da@sjx-ixn6.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-1iwdw2Z27YyY@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
(sniped)
> 
> Well, I get to eat crow.  With this release of the compiler mixing
> quotes and apostrophes (as long as opening and closing match) works
> just fine.

Cool - just like REXX!

Bill Lynch
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 6)_

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d56fe$8p3$1@nnrp1.dejanews.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net> <7cau3g$da@sjx-ixn6.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-1iwdw2Z27YyY@Dwight_Miller.iix.com> <36EA00B4.8556234F@att.net>`

```
In article <36EA00B4.8556234F@att.net>,
  wblynch@worldnet.att.net wrote:
>
> Cool - just like REXX!
>
> Bill Lynch
>

Unfortunately, there is just one little thing which is very uncool: Both the
SQL- and the CICS-precompiler still need the option "APOST" or 'QUOTE'. And
they both treat a literal with the "wrong" delimiters as a data-name. The SQL
precompiler says that a colon is missing (invalid host variable). The CICS
precompiler accepts it, but does a call to 'DFHEI1' with the literal "by
reference" which is not accepted by the COBOL compiler.

So we have to distinguish between literals in 'pure' COBOL and between an
'EXEC' and the corresponding "END-EXEC".

Regards

Daniel
------------------------------------------------------------------------
visit us at http://www.winterthur.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e90c5a.804676924@news1.ibm.net>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net> <7cau3g$da@sjx-ixn6.ix.netcom.com>`

```
On Fri, 12 Mar 1999 05:33:46 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Thane Hubbell wrote in message <36e8895f.771141440@news1.ibm.net>...
>  <snip>
…[10 more quoted lines elided]…
>OS/390 & VM.

I'll let you know in a little bit.  I'll also try it again.  We have
been through the gamet - and my last "attempt" might very well have
been with the /370 version.  I'll try it again today and post the
results.
```

###### ↳ ↳ ↳ Re: COBOL/MVS and Quotes

_(reply depth: 4)_

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cb71t$adu$1@nnrp1.dejanews.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net> <19990311160534.20208.00000926@ng119.aol.com> <36e8895f.771141440@news1.ibm.net> <7cau3g$da@sjx-ixn6.ix.netcom.com>`

```
In article <7cau3g$da@sjx-ixn6.ix.netcom.com>,
  "William M. Klein" <wmklein at ix dot netcom dot com> wrote:
> Thane Hubbell wrote in message <36e8895f.771141440@news1.ibm.net>...
>   <snip>
…[16 more quoted lines elided]…
>

COBOL for MVS & VM V1R2M2 has QUOTE/APOST only as figurative constant, not as
literal delimiter. So this must have been changed either from release 1 to
release 2 of version 1 or from COBOL/370 to V1R1.

Regards

Daniel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: COBOL/MVS and Quotes

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DPXF2.3605$bk.10265633@storm.twcol.com>`
- **References:** `<7c98ok$4bn$1@plug.news.pipex.net>`

```
This may be overstating the obvious, but have you tried the "FLAG(I,I)"
compiler option? This should flag all informational level messages both
instream and at the end of the listing.

EX:

       PROCESS FLAG(I,I)
       IDENTIFICATION DIVISION.
       ......

OR
       CBL FLAG(I,I)
       IDENTIFICATION DIVISION.
       ........
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
