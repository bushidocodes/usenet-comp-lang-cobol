[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tool for editing flat-file data

_7 messages · 5 participants · 1999-04_

---

### Tool for editing flat-file data

- **From:** djwxyz@prj-cms.com (CMS)
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<37092612.1034615107@news.supernews.com>`

```

We are in serious need of a flat-file editing tool for our
Microfocus-based COBOL application (which works pretty well) operating
on AIX.

The need is similar to that of File-aid on the MVS/OS390 platform
whereby flat files can be edited and browsed directly or broken-down
using the COBOL copymember as a data dictionary of the records fields
(for validation and displacement).

FWIW, the UNIX files and COBOL definitions can be "seen" from the W98
developer PC's on the network so a pc based solution will probably
also work for us.

We looked briefly at Fileaid/CS products from Compuware and, while
they do have an inexpensive add-on Xwindows small unix tool for this
purpose (which is supposedly being designed-out), they bundle this in
with the other Fileaid/CS pieces (which we don't really need) to the
tune of $35K+ - excessive considering this is about the price of the
entire development environment and the P390 sitting beside it.
Fileaid/PC would also probably work, but it supposedly is being
withdrawn too.

I looked briefly at the InSync products that work similarly to the
File-aid line, but no unix or PC support. 

Does Microfocus have any tools (retired or otherwise) to copybook edit
flat files for the unix platform?

Any PC based product that does the file/copybook editing?

Any assistance or insight would be appreciated!

Thanks,

D. Williams

UCE countermeasures - please delete the
xyz from my username - thanks again
```

#### ↳ Re: Tool for editing flat-file data

- **From:** Michael Boudreau <mboudreau@cyberus.ca>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<370A95F5.A527B12D@cyberus.ca>`
- **References:** `<37092612.1034615107@news.supernews.com>`

```
If you have MS Access available from the PC and an ODBC connection to
the server you can link to the file from MS Access.  Access has a fairly
decent flat file mapping tool.  After it is mapped and linked you can
treat it as an Access table.





CMS wrote:
> 
> We are in serious need of a flat-file editing tool for our
…[11 more quoted lines elided]…
>[[snipped]]

Mike Boudreau
```

#### ↳ Re: Tool for editing flat-file data

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<37097469.702829554@news1.ibm.net>`
- **References:** `<37092612.1034615107@news.supernews.com>`

```
On Mon, 05 Apr 1999 21:28:43 GMT, djwxyz@prj-cms.com (CMS) wrote:


>Does Microfocus have any tools (retired or otherwise) to copybook edit
>flat files for the unix platform?

Hmmm using WFL and FORMS you should be able to "Generate" such an
application.  It will be some work though, and a program will be
needed for each file - and you are back in the same boat!  Why not
just write a COBOL program to do the maintenance!
```

##### ↳ ↳ Re: Tool for editing flat-file data

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<7ecs0r$pp8@dfw-ixnews11.ix.netcom.com>`
- **References:** `<37092612.1034615107@news.supernews.com> <37097469.702829554@news1.ibm.net>`

```
Thane Hubbell wrote in message <37097469.702829554@news1.ibm.net>...
>On Mon, 05 Apr 1999 21:28:43 GMT, djwxyz@prj-cms.com (CMS) wrote:
>
…[7 more quoted lines elided]…
>just write a COBOL program to do the maintenance!

Micro Focus has a "data file editor" that does what you want - but I think
*my* be a Windows only facility.  I am checking with my MF sources to see if
it is available for Unix.
```

##### ↳ ↳ Re: Tool for editing flat-file data

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<7ed045$mf7@dfw-ixnews10.ix.netcom.com>`
- **References:** `<37092612.1034615107@news.supernews.com> <37097469.702829554@news1.ibm.net>`

```
It looks like I am going to get two answers for this.  The "Unix only"
solution, I am still researching, but I did get the following reply from MF
related to accessing the Unix files via the PC/ developers workstation
(which you seemed to indicate would be an OK solution).

"There are two options, the first is to use the classic PC based GUI
Data File Editor running on a WinTel box accessing the data files through a
UNIX based Fileshare server. Instructions on how to do this are documented
in the latest 4.0 product."

The second option is the one that I am still researching.

If you have trouble finding the 4.0 "documentation" that they talk about,
let me know.
```

#### ↳ Re: Tool for editing flat-file data

- **From:** Michael Holzer <Michael_Holzer@hp.com>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<370C80F6.537B7AFB@hp.com>`
- **References:** `<37092612.1034615107@news.supernews.com>`

```


CMS wrote:

> We are in serious need of a flat-file editing tool for our
> Microfocus-based COBOL application (which works pretty well) operating
> on AIX.
>

I use Fujitsu COBOL 4.0 on NT (~500$) that includes Dataeditor.
Dataeditor has limitations as no REDEFINES of record definitions
are allowed but manuel workarounds are possible.

Hope this helps

Regards

Michael

PS: I saw an advertisement for a new tool in this category from a
    german software company called Sotware-Engineering Service GmbH (SES)
    priced at ~3500$
```

##### ↳ ↳ Re: Tool for editing flat-file data

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.unix.aix,bit.listserv.ibm-main,comp.lang.cobol,bit.listserv.aix-l
- **Message-ID:** `<7eihib$a5d@dfw-ixnews5.ix.netcom.com>`
- **References:** `<37092612.1034615107@news.supernews.com> <370C80F6.537B7AFB@hp.com>`

```
I have now heard back from Micro Focus on the original question:

1) If you are willing to do your file editing on WinTel - Windows type
machine (but keeping your files on UNIX) - then this is possible and
documented today - via FileShare access from Windows to Unix files - and
using the standard "data file editor" which has long been available from
Micro Focus.

2) To use data file editor on Unix directly, the answer is "watch this
space" - coming to a computer near you soon (VERY SOON).  If you need
details on this, send me a private email - with the name of your Micro Focus
marketing rep - and I think this can be progressed "quickly".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
