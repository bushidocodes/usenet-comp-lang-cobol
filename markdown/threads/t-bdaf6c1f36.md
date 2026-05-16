[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and Windows NT

_7 messages · 7 participants · 1999-08_

---

### COBOL and Windows NT

- **From:** "Ralf Ciemilewski" <schimmi@soluter.de>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
I want to use an old Application with Windows NT.

When I start then Application in a DOS-BOX then following Error occurs:

'Cobol run time library not installed'

My question:
Is it possible to run COBOL-Applictions with Windows NT?
Where can I get the 'run time library'?
Is there anyting else I need to do?

Thanks
Ralf
```

#### ↳ Re: COBOL and Windows NT

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7oc1p9$ku5$1@hyperion.mfltd.co.uk>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
Ralf,

The problem you have hit, assuming you are referring to an application
created using a Micro Focus product, is likely to be as a result of the fact
that many applications are dual 16-bit DOS and OS/2 applications. Therefore
you need to add the directory containing COBLIB.DLL to the Os2LibPath
environment variable. Once you have done that it should work okay.

Ralf Ciemilewski wrote in message <01bedf28$2adf5d80$0181500a@ws066002>...
>I want to use an old Application with Windows NT.
>
…[10 more quoted lines elided]…
>Ralf
```

##### ↳ ↳ Re: COBOL and Windows NT

- **From:** SBrueggemann@gmx.net (Sven Brueggemann)
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37a9c8cb.177365157@news.btx.dtag.de>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002> <7oc1p9$ku5$1@hyperion.mfltd.co.uk>`

```
"Gael Wilson" <gael.wilson@merant.com> wrote:

>The problem you have hit, assuming you are referring to an application
>created using a Micro Focus product, is likely to be as a result of the fact
>that many applications are dual 16-bit DOS and OS/2 applications. Therefore
>you need to add the directory containing COBLIB.DLL to the Os2LibPath
>environment variable. Once you have done that it should work okay.

As it is an old DOS Application, he might not have the OS/2 libraries.
But I bet he has XM which is a 16-Bit DOS-EXE. With the startup line
"XM.EXE APPLICATION.EXE" it should work fine (at least until Jan.
1st...).

Best regards
```

#### ↳ Re: COBOL and Windows NT

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7oc19n$ghe$3@news.igs.net>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
It sounds like a MF or MS Cobol compiler for DOS.  If that is so, then you
need the file COBLIB.DLE.  That should get it to run in a DOS window for
you.

Ralf Ciemilewski wrote in message <01bedf28$2adf5d80$0181500a@ws066002>...
>I want to use an old Application with Windows NT.
>
…[10 more quoted lines elided]…
>Ralf
```

#### ↳ Re: COBOL and Windows NT

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990805093008.23716.00003284@ngol06.aol.com>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
In article <01bedf28$2adf5d80$0181500a@ws066002>, "Ralf Ciemilewski"
<schimmi@soluter.de> writes:

>My question:
>Is it possible to run COBOL-Applictions with Windows NT?
>Where can I get the 'run time library'?
>Is there anyting else I need to do?
>

sounds like the application had some support files that you did not copy over
to the NT system.   There is nothing intrinsic to any environment that
precludes it 
from running an application created in any language.
It depends on the platform the application was targeted for and whether the
application was self contained (only needs the EXE) or whether there are 
support files required (.OVL, RTL, .DLL).
```

#### ↳ Re: COBOL and Windows NT

- **From:** "IceBerg" <IceBerg@titanic.com>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7oc5b7$c29$1@nntp9.atl.mindspring.net>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
What you need is the 32-bit version of MF-Cobol. We switched to it for the
NT platform and it has been much faster and more stable. However, you need
to compile your code on an NT workstation (true 32-bit OS) in order to reap
all of the benefits! Good luck!



Ralf Ciemilewski <schimmi@soluter.de> wrote in message
news:01bedf28$2adf5d80$0181500a@ws066002...
> I want to use an old Application with Windows NT.
>
…[10 more quoted lines elided]…
> Ralf
```

#### ↳ Re: COBOL and Windows NT

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37aa41e1.341767400@news1.ibm.net>`
- **References:** `<01bedf28$2adf5d80$0181500a@ws066002>`

```
On 5 Aug 1999 08:44:38 GMT, "Ralf Ciemilewski" <schimmi@soluter.de>
wrote:

>I want to use an old Application with Windows NT.
>
…[3 more quoted lines elided]…
>

Try preceeding your command with FORCEDOS

Such as:  FORCEDOS MYPROGRAM.EXE

Also, DOS support is supposed to be gone from Windows 2000 so get
ready for that too.


>My question:
>Is it possible to run COBOL-Applictions with Windows NT?
…[4 more quoted lines elided]…
>Ralf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
