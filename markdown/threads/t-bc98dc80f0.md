[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol dat and idx files

_8 messages · 8 participants · 2001-08_

---

### cobol dat and idx files

- **From:** rurapenty@yahoo.com (Mike Wilson)
- **Date:** 2001-08-14T06:35:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```
i have some old dat and idx files that need to be converted to access,
dbase, or text.  i believe they are in ibm cobol format.  how would be
the best way to accomplish this conversion?  i do not have the
original source code for the program that produced these files.
thanks,
mike wilson
```

#### ↳ Re: cobol dat and idx files

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-08-14T14:19:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lbbvm$akm$1@peabody.colorado.edu>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```

On 14-Aug-2001, rurapenty@yahoo.com (Mike Wilson) wrote:

> i have some old dat and idx files that need to be converted to access,
> dbase, or text.  i believe they are in ibm cobol format.  how would be
> the best way to accomplish this conversion?  i do not have the
> original source code for the program that produced these files.
> thanks,

The easiest conversion is between cobol format and text, as they are the
same thing.   You may have some numbers that are binary or packed though.

The toughest part of your job is guessing what the data mean.  You can look
at it and infer that part of it is a name, part of it is a number, part of
it is a billing code, etc.  But you should have some ideas about what data
you want and expect - you aren't converting for the hell of it - there must
be something you're expecting to find and use.
```

##### ↳ ↳ Re: cobol dat and idx files

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-08-14T08:26:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B794316.3633@paralynx.com>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com> <9lbbvm$akm$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> On 14-Aug-2001, rurapenty@yahoo.com (Mike Wilson) wrote:
…[14 more quoted lines elided]…
> be something you're expecting to find and use.

The DAT files will contain the data, the IDX will contain only indexing. Whichever 
system you import into will want to re-index based on its own rules, so you can ignore 
it.

If the DAT contains any binary or packed decimal data you will need to unpack it.  You 
will also have to allow for any conversion which be needed (or may have happened) from 
EBCDIC.  If the file has come from an IBM mainframe system via IND$FILE, Kermit or 
similar, any binaries or packed will have been garbled since they will have been 
converted as if they were text characters.

Even in the latter circumstance, you might find ParseRat (http://www.parserat.com/) of 
assistance. It will be able to handle these files as "generic binary" and export to CSV, 
DBF, XML or several other formats. It can also "ungarble" binaries which have been 
garbled this way.
```

##### ↳ ↳ Re: cobol dat and idx files

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2001-08-15T01:22:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y9ke7.16396$1p1.1306838@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com> <9lbbvm$akm$1@peabody.colorado.edu>`

```
    If you have a MF compiler, try using the rebuild program to
see what the record length and key(s) start and length is.

    Once you have that you can either use the file loader application
to dump the file to a record sequential file, or write a cobol program
to do so.

    If you have the application (runable), try adding a record with known
values (Ie "AAAAAAAAAA" for first name).

    Don't try to use line sequential untill you know that there are no
binary
or packed fields.

    MF has used several different file formats for indexed files.  Some of
these
formats can be examined directly, some cannot.



Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:9lbbvm$akm$1@peabody.colorado.edu...
>
> On 14-Aug-2001, rurapenty@yahoo.com (Mike Wilson) wrote:
…[10 more quoted lines elided]…
> The toughest part of your job is guessing what the data mean.  You can
look
> at it and infer that part of it is a name, part of it is a number, part of
> it is a billing code, etc.  But you should have some ideas about what data
> you want and expect - you aren't converting for the hell of it - there
must
> be something you're expecting to find and use.
```

#### ↳ Re: cobol dat and idx files

- **From:** Colin Campbell <cmcampb@ibm.net>
- **Date:** 2001-08-14T11:26:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B796D67.C29C9501@ibm.net>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```
I believe it is likely that the files are part of an application
programmed using Micro Focus COBOL.  .DAT would be the data and .IDX the
index portion, as another note said.  If you have the Micro Focus
Workbench, you could look at the files as related units.

Without at least record descriptions, though, how do you know what to do
with the data?

One of my colleagues has a similar problem.  In her case, the application
is still running, but no one knows when, how, or by whom it was produced.

Good luck!
========
Mike Wilson wrote:

> i have some old dat and idx files that need to be converted to access,
> dbase, or text.  i believe they are in ibm cobol format.  how would be
…[3 more quoted lines elided]…
> mike wilson
```

#### ↳ Re: cobol dat and idx files

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2001-08-15T00:40:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Exje7.4195$5d4.1250536@monger.newsread.com>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```
Did they come from a Unix system?  They could be in C-ISAM format (see
www.informix.com - not sure if C-ISAM info is still there since IBM bought
that part of Informix).

If it is C-ISAM and if I recall correctly, the .dat portion of the file will
contain fixed length records containing the data.  But you will somehow need
to figure out the record length and the field layout inside the records.
That's defined in the program source code (and you don't have that).

"Mike Wilson" <rurapenty@yahoo.com> wrote in message
news:5a04687f.0108140535.26b2d982@posting.google.com...
> i have some old dat and idx files that need to be converted to access,
> dbase, or text.  i believe they are in ibm cobol format.  how would be
…[3 more quoted lines elided]…
> mike wilson
```

#### ↳ Re: cobol dat and idx files

- **From:** "Timothy" <timhillock@home.com>
- **Date:** 2001-08-15T23:11:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MkDe7.17080$hO5.3608162@news3.rdc1.on.home.com>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```
Well, I'm no expert for Cobol on a PC, but do you still have the old EXE's.
If you do, them maybe you can try to add 1 record.  You could rename the
existing dat and idx files and create empty files.  Then try running your
programs to create 1 dummy record.  Record what data you entered and then
you look at the Dat files to see how the data is kept.
```

#### ↳ Re: cobol dat and idx files

- **From:** Vadim Maslov <vm-spm@siber.com>
- **Date:** 2001-08-17T00:48:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B7C6A58.F564B64A@siber.com>`
- **References:** `<5a04687f.0108140535.26b2d982@posting.google.com>`

```
You can use Data2Flat tools for this.
And you also may need DataGuess if you do not have
a copybook with record layout.

Details sre here: http://www.siber.com/sct/datafile/

Vadim Maslov

Mike Wilson wrote:
> 
> i have some old dat and idx files that need to be converted to access,
…[4 more quoted lines elided]…
> mike wilson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
