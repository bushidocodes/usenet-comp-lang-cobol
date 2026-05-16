[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

_5 messages · 5 participants · 2000-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

- **From:** siroco_bcee@hotmail.com (Eric FELTZ)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391bbfd7.8380710@news.uunet.lu>`

```
Hi,

I got a problem using  Cobol-Sort on files bigger than 1Mb: The file
is not sorted!

Can anyone help?

Thanks in advance,
			Eric FELTZ
```

#### ↳ Re: Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fgjis$gfg$1@hyperion.mfltd.co.uk>`
- **References:** `<391bbfd7.8380710@news.uunet.lu>`

```
Eric,

This is a documented limit of the 4.0 product. Check the Programmer's Guide
to File Handling, Chapter 33 for confirmation.


Eric FELTZ <siroco_bcee@hotmail.com> wrote in message
news:391bbfd7.8380710@news.uunet.lu...
> Hi,
>
…[6 more quoted lines elided]…
> Eric FELTZ
```

##### ↳ ↳ Re: Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fglig$ujs$1@slb6.atl.mindspring.net>`
- **References:** `<391bbfd7.8380710@news.uunet.lu> <8fgjis$gfg$1@hyperion.mfltd.co.uk>`

```
And what Gael didn't mention is that there are several "more recent" products
than the 4.0 one.
```

#### ↳ Re: Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391D1566.7DB@Azonic.co.nz>`
- **References:** `<391bbfd7.8380710@news.uunet.lu>`

```
Eric FELTZ wrote:
> 
> Hi,
> 
> I got a problem using  Cobol-Sort on files bigger than 1Mb: The file
> is not sorted!

Is this on Unix ?

It may be a limit in your Cobol system or it may be that you Unix logon
may restrict file size to a default of 2 MBytes each and some
intermediate sort file requires more than that 2Mb limit.

There is a Unix command to raise the max file size limit for the user
but I can't remebeer it off hand.
```

##### ↳ ↳ Re: Problems with Cobol-Sort under Microfocus Object Cobol 4.0.38 for NT

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fj46s$j6b$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<391bbfd7.8380710@news.uunet.lu> <391D1566.7DB@Azonic.co.nz>`

```
    He said "M", not "G".


Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:391D1566.7DB@Azonic.co.nz...
> Eric FELTZ wrote:
> >
> > Hi,
> >
> > I got a problem using  Cobol-Sort on files bigger than 1Mb:
The file
> > is not sorted!
>
> Is this on Unix ?
>
> It may be a limit in your Cobol system or it may be that you
Unix logon
> may restrict file size to a default of 2 MBytes each and some
> intermediate sort file requires more than that 2Mb limit.
>
> There is a Unix command to raise the max file size limit for
the user
> but I can't remebeer it off hand.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
