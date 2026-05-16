[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VisualAge or MicroFocus COBOL mainframe access

_4 messages · 4 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### VisualAge or MicroFocus COBOL mainframe access

- **From:** wtsquid@my-dejanews.com
- **Date:** 1999-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cmijm$tr8$1@nnrp1.dejanews.com>`

```
Has anyone used VisualAge COBOL or MicroFocus COBOL LAN developed
applications to access VSAM files on an IBM mainframe and other file types on
a file server?	From the IBM ads I'm not sure whether VisualAge can do it,
they either state or imply that it can but do not emphasize the fact. That
leads me to believe that it can but not well enough to develop apps with the
method. MicroFocus states emphatically that it can access files on multiple
platforms, including the IBM mainframe, but their verbage does not make it
sound like an easy process.

I would appreciate any experiences with these products anyone is willing to
share.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: VisualAge or MicroFocus COBOL mainframe access

- **From:** "Walter Willis" <wwillis1@uswest.net>
- **Date:** 1999-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<osdJ2.672$%u2.2712@news.uswest.net>`
- **References:** `<7cmijm$tr8$1@nnrp1.dejanews.com>`

```
To answer your question, Yes it is possible.  I am working on a project now
that essentially does this.  But it uses mainframe programs for the data
retrieval and related computations and sends the results back.  I believe it
uses a CICS type transaction to call the mainframe program from the GUI
interface.  I was not involved in this aspect of development.

One of the 'now' Microfocus products is XDB gateway which you can use to
test an application on the PC that access DB2 data on the mainframe.
```

##### ↳ ↳ Re: VisualAge or MicroFocus COBOL mainframe access

- **From:** Eric Andersen <eric.no.andersen@merant.spam.com>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F7B4E1.6AD8CEB6@merant.spam.com>`
- **References:** `<7cmijm$tr8$1@nnrp1.dejanews.com> <osdJ2.672$%u2.2712@news.uswest.net>`

```
Micro Focus Fileshare, with the Micro Focus Mainframe Access (MFA) Product for
VSAM access may be what you're looking for. Fileshare provides transparent
access to remote files using standard COBOL I/O syntax.  Redirection of I/O
requests is controlled outside of the program through an external
configuration file.  The redirector allows selection of the destination server
on a file-by-file basis, and fileshare servers run on a variety of platforms
so your need to access "other file types on a file server" may be covered here
too.  MFA evolved from the old Fileshare for Host Systems, and for your
purposes would provide transparent access to VSAM files on the host.  Whether
Fileshare servers on other platforms will fill the bill probably depends on
the target files.

Some product information is available at
http://www.merant.com/ads/md/products/mfa.asp and you can find some additonal
material by running "mainframe access" and "fileshare" through the site's
search engine.

Note that I'm not directly involved with the Fileshare team, so some of the
terminology may have changed, but in general the preceding should be accurate
- I hope this helps...

Eric


<wtsquid@my-dejanews.com> wrote in message
news:7cmijm$tr8$1@nnrp1.dejanews.com...
> Has anyone used VisualAge COBOL or MicroFocus COBOL LAN developed
> applications to access VSAM files on an IBM mainframe and other file types on
…[11 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
 

----------------------------------------------
- remove no and spam from my address to reply
```

#### ↳ Re: VisualAge or MicroFocus COBOL mainframe access

- **From:** djscubed@aol.com (Djscubed)
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990324211228.01606.00000725@ng-ft1.aol.com>`
- **References:** `<7cmijm$tr8$1@nnrp1.dejanews.com>`

```
Check out www.c-cubed.net their solution product has been running at FDR, DST,
ABBOT Labs, Flemming Foods, State of Nebraska, Bank of De Credito, Bank of
Lima, Ross Labs and many other companies doing much more that just easy file
access.  The performance is more than 8 times faster than the Micro Focus File
share product and is much less expensive.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
