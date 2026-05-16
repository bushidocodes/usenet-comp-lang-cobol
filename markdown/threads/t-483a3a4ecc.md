[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convert Fujitsu to DBASE files

_4 messages · 4 participants · 2003-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Convert Fujitsu to DBASE files

- **From:** "TeckDesign" <francis@teckdesign.com>
- **Date:** 2003-05-08T12:47:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bvrua.344$R86.457832@newsserver.ip.pt>`

```
I need a tool to convert Fujitsu Cobol files to Dbase.
I know a tool from the SiberSystem, but i  think that it is very expensive.
Who knows another process to convert indexed files in Fujitsu to Dbase.



Thanks
```

#### ↳ Re: Convert Fujitsu to DBASE files

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-08T07:12:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CKycnZYahvJh1CejXTWJjw@giganews.com>`
- **References:** `<Bvrua.344$R86.457832@newsserver.ip.pt>`

```

"TeckDesign" <francis@teckdesign.com> wrote in message
news:Bvrua.344$R86.457832@newsserver.ip.pt...
> I need a tool to convert Fujitsu Cobol files to Dbase.
> I know a tool from the SiberSystem, but i  think that it is very
expensive.
> Who knows another process to convert indexed files in Fujitsu to Dbase.

It shouldn't be too hard to write your own: Dbase files are mostly just a
text file with a single header record at the front defining the file layout.

We have a program to go the other way (Dbase to text) that we've often used
to convert customer files as input to our system.

For that matter, you can read your text file into Excel and have Excel save
the result as a DB2, 3, or 4 output. If your file is a Fujitsu indexed file,
you'll have to squirt it out to a text file first.
```

#### ↳ Re: Convert Fujitsu to DBASE files

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-05-08T13:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8itua.10075$%_3.5793455@newssrv26.news.prodigy.com>`
- **References:** `<Bvrua.344$R86.457832@newsserver.ip.pt>`

```
"TeckDesign" <francis@teckdesign.com> wrote in message
news:Bvrua.344$R86.457832@newsserver.ip.pt...
> I need a tool to convert Fujitsu Cobol files to Dbase.
> I know a tool from the SiberSystem, but i  think that it is very
expensive.
> Who knows another process to convert indexed files in Fujitsu to Dbase.


Start here...general advice on "COBOL-created data for non-COBOL
applications"

http://www.providerpaymentpartner.com/tsihome_html/downloads/C2IEEE.htm


MCM
(yes, that's my web site).
```

#### ↳ Re: Convert Fujitsu to DBASE files

- **From:** Ed Guy <ed_guy@shaw.ca>
- **Date:** 2003-05-08T21:02:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBAC5BC.C718CB05@shaw.ca>`
- **References:** `<Bvrua.344$R86.457832@newsserver.ip.pt>`

```
TeckDesign wrote:

> I need a tool to convert Fujitsu Cobol files to Dbase.
> I know a tool from the SiberSystem, but i  think that it is very expensive.
> Who knows another process to convert indexed files in Fujitsu to Dbase.

Try ParseRat (http://www.parserat.com/).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
