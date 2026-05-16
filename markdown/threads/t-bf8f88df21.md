[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading a non-COBOL file

_6 messages · 6 participants · 1999-06_

---

### Reading a non-COBOL file

- **From:** theisb@21st.dk
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ivvol$v87$1@nnrp1.deja.com>`

```
Hi there.

A file consists of 10 chars, and I'd like to read them into a variable
like:

01 names
  05 name1 pic X(5)
  05 name2 pic X(5)

BUT: COBOL willl only read from files made by COBOL programs ????

Hope there's some help out there...

Regards Theis (Denmark)


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Reading a non-COBOL file

- **From:** Moncho Castelo <moncho_castelo@my-deja.com>
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j02vc$6g$1@nnrp1.deja.com>`
- **References:** `<7ivvol$v87$1@nnrp1.deja.com>`

```
In article <7ivvol$v87$1@nnrp1.deja.com>,
  theisb@21st.dk wrote:
> Hi there.
>
…[15 more quoted lines elided]…
>


You can read a text file in COBOL without problem. You must process it
like a line sequential file.
```

##### ↳ ↳ Re: Reading a non-COBOL file

- **From:** grob99@my-deja.com
- **Date:** 1999-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j04s1$kq$1@nnrp1.deja.com>`
- **References:** `<7ivvol$v87$1@nnrp1.deja.com> <7j02vc$6g$1@nnrp1.deja.com>`

```
Thanks! That helped.

Theis

  Moncho Castelo <moncho_castelo@my-deja.com> wrote:
>
> You can read a text file in COBOL without problem. You must process it
> like a line sequential file.
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Reading a non-COBOL file

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-06-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37567DD3.7AE7656C@NOSPAMhome.com>`
- **References:** `<7ivvol$v87$1@nnrp1.deja.com>`

```
theisb@21st.dk wrote:
> 
> Hi there.
…[10 more quoted lines elided]…
> Hope there's some help out there...

COBOL will read any files.  As long as you understand the data within
the files, you can have COBOL handle those data.
```

##### ↳ ↳ Re: Reading a non-COBOL file

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ra063.1354$H21.5733@ozemail.com.au>`
- **References:** `<7ivvol$v87$1@nnrp1.deja.com> <37567DD3.7AE7656C@NOSPAMhome.com>`

```
Yes, you can read any file as if it was a sequential file with each record
being PIC X, or you can read it as line sequential if each record is
delimited by an end-of-line character, and you can read as if each record
has a structure (if you know the structure or can deduce the structure by
observing it in a text editor)
David

Howard Brazee wrote in message <37567DD3.7AE7656C@NOSPAMhome.com>...
>theisb@21st.dk wrote:
>>
…[14 more quoted lines elided]…
>the files, you can have COBOL handle those data.
```

###### ↳ ↳ ↳ Re: Reading a non-COBOL file

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37596CC8.9D1242E@earthlink.net>`
- **References:** `<7ivvol$v87$1@nnrp1.deja.com> <37567DD3.7AE7656C@NOSPAMhome.com> <Ra063.1354$H21.5733@ozemail.com.au>`

```
David Mowat wrote:
> 
> Yes, you can read any file as if it was a sequential file with each record
…[3 more quoted lines elided]…
> observing it in a text editor)

Right. COBOL can be made read any file as a sequence of bytes, yet the entire
purpose of reading is understanding the meaning of data. Sure, I can read a
Chinese text as a sequence of characters but it is futile if I do not know
Chinese. Deducing the structure of such a file by observing it in a text editor
is a formidable task, if possible at all. For example, from the standpoint of
OS, a SAS library is just a flat file with RECFM=FS, but try to make sense out
of its data by browsing it, even though the data are meaningful and valid.
Having engines that recognize a variety of special data structures (e.g. VSAM,
RDBSs), COBOL is unable to read (that is, understand) a lot of other file types.
This is one reason SAS able to transparently read,  understand, and write ANY
existing file format (including all proprietary ones, even SAP) is so
indispensable in clinical trial settings or any shop where data flow in and out
in every imaginable format. SAS is expensive to license, but one looking at a
single program (and I mean a real program, not a cluster of cryptic signs)
reading DB2 under OS/390, Oracle on UNIX, Excel on NT, SAS libraries on VAX,
flat files sitting on AS/400, processing all that, writing data back in the
native formats, and distributing user reports on the web, may think the price is
not too high.

Kind regards,
+++++++++++++++++
Paul M. Dorfman
Jacksonville, Fl
+++++++++++++++++
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
