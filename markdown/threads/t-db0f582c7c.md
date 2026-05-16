[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCOBOL data conversion

_4 messages · 4 participants · 2001-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### AcuCOBOL data conversion

- **From:** "Milton Bradley" <nospam@nospam.com>
- **Date:** 2001-06-01T10:45:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f8dh8$o4$1@news.chorus.net>`

```
Hello,

I am looking into the possibility of converting some legacy data from an
AIX/RS6000 system written in AcuCOBOL circa early 90's. Is there a way to
convert this data without source code or data definitions? A solution that
produces raw ASCII where I have to determine the columns would be
acceptable.

Another strategy I have been tossing around is to run a report from the
application to a file and then strip out the needed data. Is it
possible/easy to redirect a report to a file instead of a printer in AIX?
Thanks in advance...

Linda G
```

#### ↳ Re: AcuCOBOL data conversion

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-06-01T08:59:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B17BBEC.6148@paralynx.com>`
- **References:** `<9f8dh8$o4$1@news.chorus.net>`

```
Milton Bradley wrote:
> 
> Hello,
…[5 more quoted lines elided]…
> acceptable.

Take a look at ParseRat (http://www.guysoftware.com/parserat.htm).
```

#### ↳ Re: AcuCOBOL data conversion

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2001-06-02T16:58:35+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f9uut$jq5@newshost.fujitsu.com.au>`
- **References:** `<9f8dh8$o4$1@news.chorus.net>`

```
Hi,

I don't know what version of data files you have but we use the newer
versions of AcuCOBOL
and it comes with a utility called "vutil" which can (amoung other things)
unload a data file to a flat
text file.

You might also consider contacting AcuCorp for advise?

Ray Smith.



Milton Bradley <nospam@nospam.com> wrote in message
news:9f8dh8$o4$1@news.chorus.net...
> Hello,
>
…[13 more quoted lines elided]…
>
```

#### ↳ Re: AcuCOBOL data conversion

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-06-09T00:49:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B217302.117B5CD7@siber.com>`
- **References:** `<9f8dh8$o4$1@news.chorus.net>`

```
We have a converter from AcuCobol data files to 
flat files (CSV) or DDBF files.

Copybooks for the files are desirable
but they are not required.

More here: http://www.siber.com/sct/datafile/

Vadim Maslov

Milton Bradley wrote:
> 
> Hello,
…[12 more quoted lines elided]…
> Linda G
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
