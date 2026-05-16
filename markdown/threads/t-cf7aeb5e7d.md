[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student - packed decimal - Net Express

_2 messages · 2 participants · 1999-10_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Re: Student - packed decimal - Net Express

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FB478D.C681CA9F@zip.com.au>`
- **References:** `<37fbaf89.8279142@nntp.xsite.net>`

```
zennmaster wrote:
> 
> So my question is:  is this a product of EBCDIC/ASCII conflict on
> packed data and how can I resolve this?   Or are my fears unfounded
> and I'm just not processing the data correctly?
> 

Yes...

The download tanslates characters from one character set to another. 
hex 15 for example is tab in Ebcdic and hex 08 in ASCII.

Recommend you expand the file before download or else you will have a
painful time of translating each text field individually.

Does Net express have an open file in ebcdic mode?   If so download
the file in binary.

Ken
```

#### ↳ Re: Student - packed decimal - Net Express

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tCPK3.1593$nm.18984@dfiatx1-snr1.gtei.net>`
- **References:** `<37fbaf89.8279142@nntp.xsite.net> <37FB478D.C681CA9F@zip.com.au>`

```
Re my other post, the DLL I have will also do a EBCDIC-ASCII conversion. If
you tell it "input is EBCDIC" it will convert only the appropriate data
types; it will also handle the "special" sign adjustment you get on signed
USAGE IS DISPLAY.

Send e-mail for conversion info; still looking for testers.

I also have a document for you to read. It explains each step in the
conversion process. When I converted it to HTML, it looks kinda crummy and
the kind people (person?) (Bob Wolfe) at Flexus is trying to help me get it
"presentable." It has great info, but "visual presentation in HTML format"
is not one of my strengths.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
