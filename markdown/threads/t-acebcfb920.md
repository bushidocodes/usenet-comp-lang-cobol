[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Power Cobol 6

_4 messages · 4 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Power Cobol 6

- **From:** "David Engle" <dengle@choicefab.com>
- **Date:** 2001-04-12T11:21:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5DkB6.146307$lj4.4501779@news6.giganews.com>`

```
I am creating a main screen and wish to switch the menu bars from one to
another by clicking on a selection from the menu bar. I do not wish to
switch from one screen to another.

I have been told that this requires MDI (multiple document interface) but
find it hard to believe since I can do it in RM/Cobol.

Any help appreciated.

David Engle
```

#### ↳ Re: Fujitsu Power Cobol 6

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-04-12T21:29:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010412172949.01696.00001601@nso-fd.aol.com>`
- **References:** `<5DkB6.146307$lj4.4501779@news6.giganews.com>`

```
In article <5DkB6.146307$lj4.4501779@news6.giganews.com>, "David Engle"
<dengle@choicefab.com> writes:

>I am creating a main screen and wish to switch the menu bars from one to
>another by clicking on a selection from the menu bar. I do not wish to
…[5 more quoted lines elided]…
>

Sounds like you would define the menu bar in its fully expanded format
and have the VISIBLE property turned OFF until some Option is checked 
to make the related menu groups visible.
```

#### ↳ Re: Fujitsu Power Cobol 6

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2001-04-14T23:28:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9baj55$n4v$1@venus.telepac.pt>`
- **References:** `<5DkB6.146307$lj4.4501779@news6.giganews.com>`

```
You have the option of writing the name of the opening menu in a Form; but
you can change it just by moving the name of another menu to "MenubarName"
of the specified Form at runtime.

regards,
Paulo Vieira
David Engle <dengle@choicefab.com> escreveu na mensagem
news:5DkB6.146307$lj4.4501779@news6.giganews.com...
> I am creating a main screen and wish to switch the menu bars from one to
> another by clicking on a selection from the menu bar. I do not wish to
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Fujitsu Power Cobol 6

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-04-20T12:18:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ae028ec.120412446@news1.attglobal.net>`
- **References:** `<5DkB6.146307$lj4.4501779@news6.giganews.com>`

```
Which version/product of RM COBOL are you using to do this?

I can do this using COBOL sp2 from Flexus on a variety of compilers, I
was just curious about your use of it with RM.

On Thu, 12 Apr 2001 11:21:40 -0500, "David Engle"
<dengle@choicefab.com> wrote:

>I am creating a main screen and wish to switch the menu bars from one to
>another by clicking on a selection from the menu bar. I do not wish to
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
