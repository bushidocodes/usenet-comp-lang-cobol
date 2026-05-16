[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to access a dataset with DSORG=DA

_6 messages · 4 participants · 2001-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to access a dataset with DSORG=DA

- **From:** "Steven Hughes" <sjhughes1@eircom.net>
- **Date:** 2001-05-17T17:47:41+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xhTM6.326$Fk7.1415@news.indigo.ie>`

```
Hi,
    I am trying to write a Cobol 370 program to access a dataset with a
DSORG of DA.

    I have defined the file in the program with a RELATIVE KEY IS relkey
clause, with relkey defined as PIC 9(04) COMP.  The OPEN INPUT statement
abends with a File-Status of 37.

    When I changed the file to a VSAM RRDS, it works fine.  Why can I not
access a DA dataset?

Thanks in advance,
                                Steven.
```

#### ↳ Re: How to access a dataset with DSORG=DA

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-17T15:28:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e1c7a$iee$1@slb5.atl.mindspring.net>`
- **References:** `<xhTM6.326$Fk7.1415@news.indigo.ie>`

```
I can't find any "explicit" statement that you can't use DSORG=DA files in
current COBOL

HOWEVER, the list of what *is* supported does not include them.

Check out,

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igypg205/1.7.2

which is "1.7.2 Choosing file organization and access mode" in the
Programming Guide
```

#### ↳ Re: How to access a dataset with DSORG=DA

- **From:** "Paul Pigott" <paul.pigott@worldnet.att.net>
- **Date:** 2001-05-17T21:10:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O6XM6.27921$t12.2114757@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<xhTM6.326$Fk7.1415@news.indigo.ie>`

```
I don't recall accessing a DA file, but if I recall correctly, DA stands for
direct access, which means you've got to specify such things as volume,
cylinder, head, track and sector to actually read the data.  I once did
something like that (if I recall correctly) on a VSE system, accessing a
third party date file to get calendar information.  The routine was actually
written in 370 Assembler because there was no way to do it in COBOL.  It's a
very hardware specific thing.

Paul


Steven Hughes <sjhughes1@eircom.net> wrote in message
news:xhTM6.326$Fk7.1415@news.indigo.ie...
> Hi,
>     I am trying to write a Cobol 370 program to access a dataset with a
…[12 more quoted lines elided]…
>
```

#### ↳ Re: How to access a dataset with DSORG=DA

- **From:** JD <pb@dazoo.com>
- **Date:** 2001-05-17T20:49:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0471AC.CB4BA710@dazoo.com>`
- **References:** `<xhTM6.326$Fk7.1415@news.indigo.ie>`

```


Steven Hughes wrote:

> Hi,
>     I am trying to write a Cobol 370 program to access a dataset with a
…[8 more quoted lines elided]…
>

DSORG=DA.  A direct access dataset.  Access methods are BDAM, EXCP.
Essentially, a relative record file.  Can be blocked or unblocked.  If
unblocked, relative block 1 and relative record 1 are the same.  If blocked,
you will probably need to manually unblock the logical records within the
physical record (at least in assembler, I've never accessed a BDAM with
COBOL, and don't know that you can).

>
> Thanks in advance,
>                                 Steven.
```

##### ↳ ↳ Re: How to access a dataset with DSORG=DA

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-18T11:02:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e3h22$ahj$1@slb5.atl.mindspring.net>`
- **References:** `<xhTM6.326$Fk7.1415@news.indigo.ie> <3B0471AC.CB4BA710@dazoo.com>`

```
For a discussion of BDAM (and *lack* of support in the current COBOL
compilers), see


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igymg202/4.1.4.2?
```

#### ↳ Re: How to access a dataset with DSORG=DA

- **From:** "Steven Hughes" <sjhughes1@eircom.net>
- **Date:** 2001-05-18T18:00:28+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HzcN6.569$Fk7.2903@news.indigo.ie>`
- **References:** `<xhTM6.326$Fk7.1415@news.indigo.ie>`

```
OK, I cheated.  Wrote it in PL/1.  Defined as REGIONAL(3) file.

Thanks to all.
                       Steven.

Steven Hughes wrote in message ...
>Hi,
>    I am trying to write a Cobol 370 program to access a dataset with a
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
