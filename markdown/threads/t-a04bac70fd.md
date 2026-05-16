[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Panvalet Files

_5 messages · 4 participants · 2003-12_

---

### Panvalet Files

- **From:** user@email.address.here (User)
- **Date:** 2003-12-17T00:26:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fdf9d01.304271203@netnews.att.net>`

```
I am working with a bunch of binary data files that were generated
(and still are generated) by programs written by people who left my
company a long time ago.  Nobody left around here knows much about the
computer programs or how they do what they do.  They merely know what
program they have to run for a specific task.

Scary.

I can't track down any information on the binary data file formats
that are used, but the name "Panvalet" keeps coming up.  Through much
reverse-engineering, a couple of us have written Matlab routines that
read and write these binary files, but as we dig deeper, it almost
looks like we're using a perversion of this file format.

It appears that the file format is designed to store a bunch of real
scalars (*REALS), integer scalars (*INTEGRS), alphanumeric scalars
(*ALPHAS), real vectors (*REALV), integer vectors (*INTEGRV),
alphanumeric vectors (*ALPHAV) and '*COMARY' (??? common array???),
which we're using to store a 2D array as a vector (with the i,k
dimensions stored as scalars elsewhere in the file).  A bunch of the
integer scalars are used to store the lengths of arrays, etc., but
these numbers are repeated deep inside the binary format where you'd
expect, them so storing them explicitly is probably a waste.  Some
strings are stored as single strings, and others are stored in pieces
as arrays of 4-byte strings.  (Some numbers are stored as 32-bit
reals, other numbers are stored as strings containing digits and
decimal points.  Our computer programs interpret these things
correctly, but I suspect that's merely one patch slapped on top of
another patch on top of another patch to make things work, and it make
adding/updating virtually impossible.  And to top it all off, most of
this stuff is written in Fortran 4.  (I'm only posting to a Cobol
newsgroup because Cobol came up a lot when I Googled "panvalet".)

We're trying to update things, and we're looking for binary file
format specifications for these files.  Does anybody know where I
might be able to find such a thing for "Panvalet" binary files?   Or
is this a cruel joke left behind by a bunch of retirees?

Thanks.
```

#### ↳ Re: Panvalet Files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-17T01:30:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2lODb.7384$Pg1.473@newsread1.news.pas.earthlink.net>`
- **References:** `<3fdf9d01.304271203@netnews.att.net>`

```
Panvalet (originally from Pansophic - but from Computer Associates for MANY
years now) is a system for storing files (often source code - but potentially
"anything") in a condensed format with automatic versioning / back-ups.

I doubt it will help much, but you could check out the current production
information - starting at:

 http://www3.ca.com/Solutions/Product.asp?ID=1431
```

#### ↳ Re: Panvalet Files

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-12-19T13:30:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0312191330.48596c80@posting.google.com>`
- **References:** `<3fdf9d01.304271203@netnews.att.net>`

```
What environment are these jobs running in? Do you have sources code?
If so, what language. How do you invoke the jobs that run the pgms? Do
you use a job control language? Code examples would help.

Regards, Jack.




user@email.address.here (User) wrote in message news:<3fdf9d01.304271203@netnews.att.net>...
> I am working with a bunch of binary data files that were generated
> (and still are generated) by programs written by people who left my
…[36 more quoted lines elided]…
> Thanks.
```

##### ↳ ↳ Re: Panvalet Files

- **From:** "Albert Paul" <alpaul1@optonline.net>
- **Date:** 2003-12-19T21:54:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4sKEb.298170$655.57436034@news4.srv.hcvlny.cv.net>`
- **References:** `<3fdf9d01.304271203@netnews.att.net> <8a2d426e.0312191330.48596c80@posting.google.com>`

```
Panvalet is a source program archival and updating system. It keeps track of
changes and who made them.

Contact some of your former Mainframers, its a simple system but it is
apparently beyond your ability.


"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0312191330.48596c80@posting.google.com...
> What environment are these jobs running in? Do you have sources code?
> If so, what language. How do you invoke the jobs that run the pgms? Do
…[7 more quoted lines elided]…
> user@email.address.here (User) wrote in message
news:<3fdf9d01.304271203@netnews.att.net>...
> > I am working with a bunch of binary data files that were generated
> > (and still are generated) by programs written by people who left my
…[36 more quoted lines elided]…
> > Thanks.
```

#### ↳ Re: Panvalet Files

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-12-19T13:39:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0312191339.8ba0621@posting.google.com>`
- **References:** `<3fdf9d01.304271203@netnews.att.net>`

```
Sorry. Didn't notice your mention of Fortran. Your best bet is ti
search the net for a Fortran group. I know that www.tek-tips.com has a
Fortran Forum.

Regards, Jack.


user@email.address.here (User) wrote in message news:<3fdf9d01.304271203@netnews.att.net>...
> I am working with a bunch of binary data files that were generated
> (and still are generated) by programs written by people who left my
…[36 more quoted lines elided]…
> Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
