[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for some help to convert cobol data files to ascii, dbase, acces, ....

_9 messages · 6 participants · 2003-04_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** ufo@pandora.be
- **Date:** 2003-04-23T07:10:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com>`

```
hi,

We are on the verge of signing a new client but for that we have to be
able to convert his old databases to our system.

I'm pretty sure the old system was programmed in cobol and that the
file system that is used is also cobol files.

there are 2 files for every file : filename (without extention) and
filename.idx

I suppose the file without the extension has the data in it and that
the index is stored in the .idx file.

Now for my question is there any program available that can export
those type of files to ascii files ? or any of the more standard
database systems ? (like dbase, acces, ...)

Tx in advance

P.S. i don't have any cobol experience.

Jurgen
```

#### ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-04-23T12:51:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b85r5j$j28$1@reader10.wxs.nl>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com>`

```
You could try Data Junction. (www.datajunction.com).

Your assumption on the idx and data file is correct. Could be C-ISAM or
native (vendor) file system. RM/Cobol or MF/Cobol perhaps ?

Either way you do need the file descritions (FD's) in order to migrate the
files to ASCII or whatever format. Unless the data is not packed and there
is no multiple record definition for each file. Do you have access to the
source code of the cobol application ?

Regards, Danny.


<ufo@pandora.be> schreef in bericht
news:ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com...
> hi,
>
…[20 more quoted lines elided]…
> Jurgen
```

#### ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T11:30:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea67716.54510941@news.optonline.net>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com>`

```
The COBOL compiler came with a tool which does this conversion.

If the system is Unix, there is a good chance the base file is already ascii ..
almost. Try looking at it with a text editor such as vi. If columns line up, the
old application is using the default C-ISAM file system. I say 'almost' because
deleted records will have their newline replaced by null. You'll have to filter
those records out, or ask them to reorganize the file before they give it to
you.




ufo@pandora.be wrote:

>hi,
>
…[20 more quoted lines elided]…
>Jurgen
```

##### ↳ ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-23T06:42:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b85u7t$3bj$1@slb4.atl.mindspring.net>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com> <3ea67716.54510941@news.optonline.net>`

```
You also need to worry about "packed-decimal" and "comp-?" data items.
Without knowing the "layout" of the records (or using a tool like ParseRat),
you may or may NOT have serious problems understanding the data in such
files.
```

###### ↳ ↳ ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** ufo@pandora.be
- **Date:** 2003-04-23T13:46:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ce6davgh70rmjhlra73l4c4uin2emt21jp@4ax.com>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com> <3ea67716.54510941@news.optonline.net> <b85u7t$3bj$1@slb4.atl.mindspring.net>`

```
I don't have acces to the sources or the rekordlayout.

The operating system is windows NT 4 and i believe it was cobol for
windows (if that exists).

J.

On Wed, 23 Apr 2003 06:42:48 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>You also need to worry about "packed-decimal" and "comp-?" data items.
>Without knowing the "layout" of the records (or using a tool like ParseRat),
>you may or may NOT have serious problems understanding the data in such
>files.
```

###### ↳ ↳ ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

_(reply depth: 4)_

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-04-23T21:27:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86pch$6n4$1@reader10.wxs.nl>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com> <3ea67716.54510941@news.optonline.net> <b85u7t$3bj$1@slb4.atl.mindspring.net> <ce6davgh70rmjhlra73l4c4uin2emt21jp@4ax.com>`

```
You should be able to find out the cobol type by starting up the Cobol
application and then abend it by pressing CTRL-C or CTRL-Break. The runtime
system will display a message containing the info required. Or simply start
up <DEBUG name.cob> and examine the code by paging through the object code
looking for readable text in the right pane.....

Or just send me a sample .nothing .idx combination...I'll tell you.....

Regards, Danny.



<ufo@pandora.be> schreef in bericht
news:ce6davgh70rmjhlra73l4c4uin2emt21jp@4ax.com...
> I don't have acces to the sources or the rekordlayout.
>
…[9 more quoted lines elided]…
> >Without knowing the "layout" of the records (or using a tool like
ParseRat),
> >you may or may NOT have serious problems understanding the data in such
> >files.
>
```

###### ↳ ↳ ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** ufo@pandora.be
- **Date:** 2003-04-23T13:47:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5h6davc3ru77a6jcrp53jq475lsp249e1c@4ax.com>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com> <3ea67716.54510941@news.optonline.net> <b85u7t$3bj$1@slb4.atl.mindspring.net>`

```
Oeps forgot the most important thing

thank you very much for your replies.

J.

On Wed, 23 Apr 2003 06:42:48 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>You also need to worry about "packed-decimal" and "comp-?" data items.
>Without knowing the "layout" of the records (or using a tool like ParseRat),
>you may or may NOT have serious problems understanding the data in such
>files.
```

##### ↳ ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T13:18:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231218.2de33e08@posting.google.com>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com> <3ea67716.54510941@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> If the system is Unix, there is a good chance the base file is already ascii ..
> almost. Try looking at it with a text editor such as vi. If columns line up, the
…[3 more quoted lines elided]…
> you.

You also failed to warn that indexed files have no restriction at all
in data fields being defined as packed, binary or excess-3, and if
these have been used it will be nowhere near 'ascii'.  The files may
also be compressed or have key compression.

Even if the files are MF Level-II or C-ISAM there is no assurance that
they are ASCII or even close.

At least you've learnt about deleted records.
```

#### ↳ Re: Looking for some help to convert cobol data files to ascii, dbase, acces, ....

- **From:** Ed Guy <ed_guy@shaw.ca>
- **Date:** 2003-04-23T22:15:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA71034.67208E8C@shaw.ca>`
- **References:** `<ovecavcitohmeoih7tra9b6b2f9oh7mm0f@4ax.com>`

```
ufo@pandora.be wrote:

> hi,
>
…[14 more quoted lines elided]…
> database systems ? (like dbase, acces, ...)

Take a look at ParseRat (http://www.parserat.com/)

For $49.95 it will probably do all you want.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
