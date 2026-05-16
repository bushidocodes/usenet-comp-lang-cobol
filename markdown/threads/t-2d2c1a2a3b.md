[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help creating a packed decimal file

_2 messages · 2 participants · 2000-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help creating a packed decimal file

- **From:** wax_man@my-deja.com
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87pgok$o4r$1@nnrp1.deja.com>`

```
Would someone please help me.  I need to create a packed decimal file
that I can ftp to a mainframe.  I'm working in a windows environment.
I currently have a file in ascii that I convert to ebcdic.  However, I
don't know how to get from ebcdic to packed decimal.  Would someone be
kind enough to explain how to perform this conversion?

Tia,

chris


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Help creating a packed decimal file

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A0528A.9DA4655B@cusys.edu>`
- **References:** `<87pgok$o4r$1@nnrp1.deja.com>`

```
wax_man@my-deja.com wrote:

> Would someone please help me.  I need to create a packed decimal file
> that I can ftp to a mainframe.  I'm working in a windows environment.
> I currently have a file in ascii that I convert to ebcdic.  However, I
> don't know how to get from ebcdic to packed decimal.  Would someone be
> kind enough to explain how to perform this conversion?

You FTP numbers in ASCII, converting them to EBCDIC, and then you use a
mainframe program to read it as display and convert it to whatever format
you need (packed).  COBOL will work fine to read your file and write out a
new file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
