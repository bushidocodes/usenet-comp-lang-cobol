[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OLE Automation, DCOM

_5 messages · 3 participants · 1999-08_

---

### OLE Automation, DCOM

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<934020499.25234.0.nnrp-13.c1edc1b5@news.demon.co.uk>`

```
Does anyone have experience of the above technology?
Im looking to call MS word with a file written from cobol
which word will be able to read and display/edit.
Including drawing lines etc.

Simon R Hart
Eaton.
```

#### ↳ Re: OLE Automation, DCOM

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ohv8a$4i0@dfw-ixnews8.ix.netcom.com>`
- **References:** `<934020499.25234.0.nnrp-13.c1edc1b5@news.demon.co.uk>`

```
Micro Focus used to (???) provide samples for doing this. That was several
years ago (about release 3.4) - but I think you might try there - IF that is
the compiler you are using.
```

##### ↳ ↳ Re: OLE Automation, DCOM

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<934056972.17100.0.nnrp-11.c1edc1b5@news.demon.co.uk>`
- **References:** `<934020499.25234.0.nnrp-13.c1edc1b5@news.demon.co.uk> <7ohv8a$4i0@dfw-ixnews8.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7ohv8a$4i0@dfw-ixnews8.ix.netcom.com...
> Micro Focus used to (???) provide samples for doing this. That was several
> years ago (about release 3.4) - but I think you might try there - IF that
is
> the compiler you are using.
>
> --
> Bill Klein
>     wmklein <at> ix dot netcom dot com

Bill,

I know how to call up a file and cut and paste basic stuff, but not how to
change font/size draw lines extra from a word document.

Simon R Hart
Eaton.
```

#### ↳ Re: OLE Automation, DCOM

- **From:** david.sands@tesco.net (David Sands)
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ad4bca.5002080@news.tesco.net>`
- **References:** `<934020499.25234.0.nnrp-13.c1edc1b5@news.demon.co.uk>`

```

Net Express has some samples on this in OLEdemos directory. And has
shows how to use Excel and Word together from COBOL.

The documentions on the OLE Automation Interface however is not
installed by default with WORD. To install this you need to select the
Visual Basic programmer reference.

The interface is complex and can be tricky to work out how to acheive
what you want. What I tend to do is RECORD a script in WORD of what I
want to do. This records in VB and tells me how to acheive the desired
functionality using the OLE Automation interface. Its then a simple
matter of doing the same from your COBOL module.

Regards
David.
```

##### ↳ ↳ Re: OLE Automation, DCOM

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<934116542.18446.0.nnrp-06.c1edc1b5@news.demon.co.uk>`
- **References:** `<934020499.25234.0.nnrp-13.c1edc1b5@news.demon.co.uk> <37ad4bca.5002080@news.tesco.net>`

```

David Sands <david.sands@tesco.net> wrote in message
news:37ad4bca.5002080@news.tesco.net...
>
> Net Express has some samples on this in OLEdemos directory. And has
…[13 more quoted lines elided]…
> David.


David,

I've have found a simple solution I have created a template in word
with labels very simular to the NetExpress samples, then i process my data
then move it to the word doc using the template pre-defined fonts,tables,
and
styles.

The reason I wish to do process a report this way is because the user
can/needs to edit the doc after processing if he/she wishes, also the
program will not need to be updated in future years all you have to do is
edit the template for desired results.

One thing I cannot see is how to change the font from OLE after selecting a
peice of text in the word doc, but this wont really be an issue.


Simon R Hart
Eaton.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
