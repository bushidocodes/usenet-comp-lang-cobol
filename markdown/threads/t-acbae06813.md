[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting Cobol Database

_8 messages · 8 participants · 2006-07 → 2006-08_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases)

---

### Converting Cobol Database

- **From:** eyeman@gmail.com
- **Date:** 2006-07-15T21:42:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`

```
I have some old data files that are created by a cobol app that is no
longer supported.  The app was coded back in the early 90's and ran in
dos.  I believe it stores individual tables in a .dta file with a
corresponding .key file.

I want to migrate this data to another format (any will do) so that I
can retrieve my old data.  Any thoughts or suggestions???

Thanks!
-Brian
```

#### ↳ Re: Converting Cobol Database

- **From:** "Bruintje Beer" <me@knoware.nl>
- **Date:** 2006-07-16T10:25:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44b9f809$0$748$5fc3050@dreader2.news.tiscali.nl>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`

```

<eyeman@gmail.com> schreef in bericht 
news:1153024923.974849.253580@35g2000cwc.googlegroups.com...
>I have some old data files that are created by a cobol app that is no
> longer supported.  The app was coded back in the early 90's and ran in
…[8 more quoted lines elided]…
>
Hi,

1.Convert the file to a pipe symbol seperated file. Most database engines 
can read these files and import them in tables.
2. Build some xml structure

Johan
```

#### ↳ Re: Converting Cobol Database

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-07-17T01:19:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4husn9F1bd6rU1@individual.net>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`

```

<eyeman@gmail.com> wrote in message 
news:1153024923.974849.253580@35g2000cwc.googlegroups.com...
>I have some old data files that are created by a cobol app that is no
> longer supported.  The app was coded back in the early 90's and ran in
…[8 more quoted lines elided]…
>
Depends... If you have the source code of the app., and a development 
environment for it, it will tell you what the data structure is. You could 
then use this to read the files sequentially and write them to a simple flat 
file. (or a database if you want to be clever.)

If you don't have these, there are a number of utilities that will try and 
discover your data for you. Pack Rat is one that has been mentioned in this 
forum a few times.

Have a look through the old system and see if there is a utility called 
REBUILD. You can use this to create a sequential file from the ISAM used by 
COBOL.

Good luck!

Pete.
```

#### ↳ Re: Converting Cobol Database

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-16T13:21:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S3rug.66839$fb2.15484@newssvr27.news.prodigy.net>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`

```
<eyeman@gmail.com> wrote in message
news:1153024923.974849.253580@35g2000cwc.googlegroups.com...
> I have some old data files that are created by a cobol app that is no
> longer supported.  The app was coded back in the early 90's and ran in
…[4 more quoted lines elided]…
> can retrieve my old data.  Any thoughts or suggestions???


Start with this free tutorial from my web site:

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

This discusses the use of COBOL-created data in non-COBOL appliations.. the
most obvious such application is 'conversion.'

That will give you some basics about conversion, the first one of which is
"you need the COBOL file description".  Once you have the File Description,
there are many different routes to follow.
```

#### ↳ Re: Converting Cobol Database

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-07-24T15:45:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<563c$44c521eb$d0663079$8056@FUSE.NET>`
- **In-Reply-To:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com>`

```
If the data is being used now, then I would assume this
"runtime" to have some recovery procedures.  Identity the
runtime and find these utilities.  Sometimes these utilities
will have a routine to drop the Indexed files to a sequential
"flat" file.  From this flat file you could possible write
a routine to load this data into a data base using whatever
runtime or language you are most comfortable with.

And as mentioned, the FD's from the original source would
be most helpful.

good luck.

bob.

eyeman@gmail.com wrote:
> I have some old data files that are created by a cobol app that is no
> longer supported.  The app was coded back in the early 90's and ran in
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Converting Cobol Database

- **From:** "ShadowFox" <Fixit4you@comcast.net>
- **Date:** 2006-08-01T17:58:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bqadnc93yq7hU1LZnZ2dnUVZ_vydnZ2d@comcast.com>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com> <563c$44c521eb$d0663079$8056@FUSE.NET>`

```
Brian.
If you have a text editor look at the two files.
Some older compilers just had a flat file with fixed data in it and the 
index
was really just a file containing the file key and a relative record 
address.
I have converted some files in the past just by reading them as text fixed 
data
with whatever appliocation. Do you know what Cobol Compiler was used?

Bob.

"Bob Iles" <bobi@mikal.com> wrote in message 
news:563c$44c521eb$d0663079$8056@FUSE.NET...
> If the data is being used now, then I would assume this
> "runtime" to have some recovery procedures.  Identity the
…[24 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Converting Cobol Database

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-08-01T15:23:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154470985.210415.226830@p79g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<Bqadnc93yq7hU1LZnZ2dnUVZ_vydnZ2d@comcast.com>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com> <563c$44c521eb$d0663079$8056@FUSE.NET> <Bqadnc93yq7hU1LZnZ2dnUVZ_vydnZ2d@comcast.com>`

```

ShadowFox wrote:
> Brian.
> If you have a text editor look at the two files.

Note that editing the data and saving is usually not a good idea as the
editor may screw up the file entirely.  It can be changed with a hex
editor as long as the key fields are left alone.

> Some older compilers just had a flat file with fixed data in it and the
> index
> was really just a file containing the file key and a relative record
> address.

Old Microfocus CIS Cobol and Level II did this. You could tell MF
Cobol/2 and Microsoft 4.x and 5.x (and other MF derivitives) to use
this format with a compiler directive.

> I have converted some files in the past just by reading them as text fixed
> data with whatever appliocation.

This is usually a bad idea for Level II and C-ISAM format as deleted
records are still in the file marked with a terminatiing x"0D00" and
slack space may have junk in it.  You need to check each record for
having x"0D0A" as the last two bytes.
```

###### ↳ ↳ ↳ Re: Converting Cobol Database

_(reply depth: 4)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-08-02T12:41:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154547719.110255.262520@75g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1154470985.210415.226830@p79g2000cwp.googlegroups.com>`
- **References:** `<1153024923.974849.253580@35g2000cwc.googlegroups.com> <563c$44c521eb$d0663079$8056@FUSE.NET> <Bqadnc93yq7hU1LZnZ2dnUVZ_vydnZ2d@comcast.com> <1154470985.210415.226830@p79g2000cwp.googlegroups.com>`

```
message snipped

It is always a good idea to have a backup before manipulating files so
you can pick up the pieces if need be.

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
