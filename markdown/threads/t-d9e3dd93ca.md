[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing Microsoft Word documents

_7 messages · 4 participants · 2000-05 → 2000-06_

---

### Accessing Microsoft Word documents

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eX8fXWxx$GA.350@cpmsnbbsa09>`

```
I need a working example of code opening a specific MS Word document with
Micro Focus 4.0.  I also use Dialog.
```

#### ↳ Re: Accessing Microsoft Word documents

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gn2lf$n68$1@news.inet.tele.dk>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09>`

```
The quick and dirty way is to define an OLE object in Dialog and connect it
to your Word document.

Regards
Ib
brucepbarrett skrev i meddelelsen ...
>I need a working example of code opening a specific MS Word document with
>Micro Focus 4.0.  I also use Dialog.
>
>
```

##### ↳ ↳ Re: Accessing Microsoft Word documents

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gp5pk$kg3$1@news.igs.net>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09> <8gn2lf$n68$1@news.inet.tele.dk>`

```
Speaking of which.

Has anybody run into a good reference work on OLE?  I would like to use
Excel and Word much more, but have not been able to find much beyond
primitive examples.

Ib Tanding wrote in message <8gn2lf$n68$1@news.inet.tele.dk>...
>The quick and dirty way is to define an OLE object in Dialog and connect it
>to your Word document.
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Accessing Microsoft Word documents

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ecx2ccKy$GA.272@cpmsnbbsa06>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09> <8gn2lf$n68$1@news.inet.tele.dk>`

```
I think the problem with that approach is that it requires the name of the
document at the time that the OLE is defined.  I want to open documents
dynamically.  The document id is known only at the time that the information
is needed i.e.  user looking at a specific part number in the inventory,
selects option to view document which contains detailed specifications which
is containd in a word document whose id is accessable withing the
application.

"Ib Tanding" <ib@tanding.dk> wrote in message
news:8gn2lf$n68$1@news.inet.tele.dk...
> The quick and dirty way is to define an OLE object in Dialog and connect
it
> to your Word document.
>
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accessing Microsoft Word documents

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h10ki$ojm$1@news.inet.tele.dk>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09> <8gn2lf$n68$1@news.inet.tele.dk> <ecx2ccKy$GA.272@cpmsnbbsa06>`

```
You're right, but the problem was exactly a 'specific document'. That's why
I made the primitive suggestion.
Regards
Ib
brucepbarrett skrev i meddelelsen ...
>I think the problem with that approach is that it requires the name of the
>document at the time that the OLE is defined.  I want to open documents
>dynamically.  The document id is known only at the time that the
information
>is needed i.e.  user looking at a specific part number in the inventory,
>selects option to view document which contains detailed specifications
which
>is containd in a word document whose id is accessable withing the
>application.
…[10 more quoted lines elided]…
>> >I need a working example of code opening a specific MS Word document
with
>> >Micro Focus 4.0.  I also use Dialog.
>> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accessing Microsoft Word documents

_(reply depth: 4)_

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OF12CKqy$GA.241@cpmsnbbsa06>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09> <8gn2lf$n68$1@news.inet.tele.dk> <ecx2ccKy$GA.272@cpmsnbbsa06> <8h10ki$ojm$1@news.inet.tele.dk>`

```
Surely someone has done this.

"Ib Tanding" <ib@tanding.dk> wrote in message
news:8h10ki$ojm$1@news.inet.tele.dk...
> You're right, but the problem was exactly a 'specific document'. That's
why
> I made the primitive suggestion.
> Regards
> Ib
> brucepbarrett skrev i meddelelsen ...
> >I think the problem with that approach is that it requires the name of
the
> >document at the time that the OLE is defined.  I want to open documents
> >dynamically.  The document id is known only at the time that the
…[9 more quoted lines elided]…
> >> The quick and dirty way is to define an OLE object in Dialog and
connect
> >it
> >> to your Word document.
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accessing Microsoft Word documents

_(reply depth: 5)_

- **From:** "Simon R Hart" <s.hart@mdfs.co.uk>
- **Date:** 2000-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h92ut$hcr$1@neptunium.btinternet.com>`
- **References:** `<eX8fXWxx$GA.350@cpmsnbbsa09> <8gn2lf$n68$1@news.inet.tele.dk> <ecx2ccKy$GA.272@cpmsnbbsa06> <8h10ki$ojm$1@news.inet.tele.dk> <OF12CKqy$GA.241@cpmsnbbsa06>`

```
lets get this right, all you want to do is simply pass a
word document over, which you know of at runtime and open it
using ms word am i right?
If this is true, then you can use a Winapi to achive this.
If you would like the full code to do so, please email me i will provide you
with
it.

Simon R Hart
MDF Systems
Norfolk.



brucepbarrett wrote in message ...
>Surely someone has done this.
>
…[41 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
