[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# converting files

_9 messages · 7 participants · 1998-12_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### converting files

- **From:** "Wayne Whitmore" <whitmore@gil.com.au>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au>`

```
Can files in a cobol written program be converted to be used by other
appllications?  Possibly windows based programs?
```

#### ↳ Re: converting files

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<74gktl$jvm$1@news.igs.net>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au>`

```
Wayne Whitmore wrote in message <74gis7$o7j8@iccu9.ipswich.gil.com.au>...
>Can files in a cobol written program be converted to be used by other
>appllications?  Possibly windows based programs?
>
Sure.  But then it is easier to just use Windows based Cobol.
```

#### ↳ Re: converting files

- **From:** "Simon Cordingley" <simonc@casegen.co.uk>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<366c2963.0@mercury.nildram.co.uk>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au>`

```
Wayne

Why not look at www.casegen.co.uk. Our Windows COBOL product will do
everthing you need and is only $50.

Wayne Whitmore wrote in message <74gis7$o7j8@iccu9.ipswich.gil.com.au>...
>Can files in a cobol written program be converted to be used by other
>appllications?  Possibly windows based programs?
>
>
```

#### ↳ Re: converting files

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<366D33A0.FDBEA4C6@home.com>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au>`

```
Wayne Whitmore wrote:
> 
> Can files in a cobol written program be converted to be used by other
> appllications?  Possibly windows based programs?

A file is a file.  Just make sure both applications (COBOL and the other
one) know the format of the file.
```

##### ↳ ↳ Re: converting files

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<74jja1$fbe$1@news.igs.net>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au> <366D33A0.FDBEA4C6@home.com>`

```

Howard Brazee wrote in message <366D33A0.FDBEA4C6@home.com>...

>A file is a file.  Just make sure both applications (COBOL and the other
>one) know the format of the file.

While that is true, I would be a bit leery of trying to read
an Isam file from another language.  All the other types
should be quite simple, as you say.
```

###### ↳ ↳ ↳ Re: converting files

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<74jn0r$p7n@sjx-ixn10.ix.netcom.com>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au> <366D33A0.FDBEA4C6@home.com> <74jja1$fbe$1@news.igs.net>`

```

Donald Tees wrote in message <74jja1$fbe$1@news.igs.net>...
>
>Howard Brazee wrote in message <366D33A0.FDBEA4C6@home.com>...
…[8 more quoted lines elided]…
>

Whether or not you can EASILY read and use an ISAM file across compiler
languages really depends on 2 things:

1) In some environments, the "ISAM" file system is a built-in part of the
operating system (for example on IBM's MVS - with VSAM - and several other
mainframe systems).  In these environments, every language has easy access
to them.

2) In some systems, a 3rd party file system (e.g. C-isam) is used through a
documented interface.  The same interface is used by COBOL, C, and any other
language that is able to use the required interface.  Again, this makes
inter-language use easy and safe.

Really, the only place where using ISAM is NOT (necessarily) safe is where
the ISAM system is "unique" to the COBOL run-time system - and even then,
many vendors make their interfaces "public" and other languages can use them
with little or no difficulty.
```

###### ↳ ↳ ↳ Re: converting files

- **From:** cadams@acucorp.com (Chris Adams)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<366d5d9c.59056588@news.acucorp.com>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au> <366D33A0.FDBEA4C6@home.com> <74jja1$fbe$1@news.igs.net>`

```
On Tue, 8 Dec 1998 11:27:32 -0500, "Donald Tees" <donald@willmack.com> wrote:

>>A file is a file.  Just make sure both applications (COBOL and the other
>>one) know the format of the file.

>While that is true, I would be a bit leery of trying to read
>an Isam file from another language.  All the other types
>should be quite simple, as you say.

Anyone contemplating this should definitely contact their vendor and see if they
can license the ISAM routines in a linkable format. It'll probably involve NDA
but it avoids enough grief to easily justify the hassle. 

I know that we've licensed our Vision routines in the past; obviously I cannot
speak for other vendors.

# Chris Adams <cadams@acucorp.com>
```

###### ↳ ↳ ↳ Re: converting files

_(reply depth: 4)_

- **From:** "Gerald Moull" <gerald@liant.co.uk>
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<913774860.9495.0.nnrp-05.9e981226@news.demon.co.uk>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au> <366D33A0.FDBEA4C6@home.com> <74jja1$fbe$1@news.igs.net> <366d5d9c.59056588@news.acucorp.com>`

```
The original question was about Windows based programs.  The answer must
therefore beto use a Windows standard.  This must be ODBC.  Any Windows tool
worth its money can use ODBC data.

What is required therefore is an ODBC driver for the COBOL data.  I'd
recommend you do a WEB search on ODBC and COBOL.

As for 'A file is a file' - !?!?!?!

Gerald Moull
gerald@liant.co.uk


Chris Adams wrote in message <366d5d9c.59056588@news.acucorp.com>...
>On Tue, 8 Dec 1998 11:27:32 -0500, "Donald Tees" <donald@willmack.com>
wrote:
>
>>>A file is a file.  Just make sure both applications (COBOL and the other
…[6 more quoted lines elided]…
>Anyone contemplating this should definitely contact their vendor and see if
they
>can license the ISAM routines in a linkable format. It'll probably involve
NDA
>but it avoids enough grief to easily justify the hassle.
>
>I know that we've licensed our Vision routines in the past; obviously I
cannot
>speak for other vendors.
>
># Chris Adams <cadams@acucorp.com>
```

###### ↳ ↳ ↳ Re: converting files

_(reply depth: 5)_

- **From:** cadams@acucorp.com (Chris Adams)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<3677e453.689274664@news.acucorp.com>`
- **References:** `<74gis7$o7j8@iccu9.ipswich.gil.com.au> <366D33A0.FDBEA4C6@home.com> <74jja1$fbe$1@news.igs.net> <366d5d9c.59056588@news.acucorp.com> <913774860.9495.0.nnrp-05.9e981226@news.demon.co.uk>`

```
On Wed, 16 Dec 1998 02:21:53 -0800, "Gerald Moull" <gerald@liant.co.uk> wrote:

>The original question was about Windows based programs.  The answer must
>therefore beto use a Windows standard.  This must be ODBC.  Any Windows tool
>worth its money can use ODBC data.

Here's the contents of the original post from
http://x15.dejanews.com/getdoc.xp?AN=419613779:
>Can files in a cobol written program be converted to be used by other
>appllications?  Possibly windows based programs?

I see two interpretations:
	1) They have datafiles from a COBOL app that they are trying to replace.
They want to move the existing data into the replacement system.
	2) They have an existing COBOL program and something new (A Windows-based
replacement?). They want to sync data between both applications.

If #1 is true, ODBC is probably the wrong answer - it almost certainly entails
entirely too much work for a one-time conversion, not to mention that licensing
an ODBC driver for a one-time task seems rather costly.

If #2 is true, ODBC is probably the right answer. If you have a need for many
programs to access this data ODBC is definitely the right choice. On the other
hand, if there is a relatively small and static set of programs that must access
this data, ODBC might involve too much additional programmer time and it will
introduce a new subsystem to the maintenance workload. This hinges on whether
their non-COBOL app is written in such a way that ODBC support would be easy to
add. Writing a general solution generally takes more time and planning than a
problem-specific solution and that extra time may not be available.


>As for 'A file is a file' - !?!?!?!

I believe this was directed to the wrong post. I was merely recommending that
someone contact their COBOL vendor before attempting to write their own ISAM
routines. This line was quoted three levels deep - any flames should go to Mr.
Brazee.


# Chris Adams <cadams@acucorp.com>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
