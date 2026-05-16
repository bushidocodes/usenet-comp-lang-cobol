[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sequential Files in AIX

_5 messages · 4 participants · 2003-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sequential Files in AIX

- **From:** mpineyro <member45438@dbforums.com>
- **Date:** 2003-10-23T11:45:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3515722.1066923948@dbforums.com>`

```

Hi,

We are migrating an application from mainframe, VSE and Cobol II, to AIX
- Visual Age Cobol. We are going to share files between both "worlds",
through FTP, and have to make a decision about what kind of the
sequential files are going to use, here is our situation:



Line Sequential

Disadvantages:

Requires modification in the SELECT of our COBOL programs.

Records are limited for X"0A" (LF) (complicates a little the bin FTP).

Only supports plain text.



Sequential RSD

Advantages

Doesn't require modification in the SELECT of our COBOL programs.

Supports any kind of data.

Disadvantages:

Records are limited for X"0A" (LF) (complicates a little the bin FTP).

Only supports fix record length.



Sequential STL

Advantages

Doesn't require modification in the SELECT of our COBOL programs.

Supports any kind of data.

Records don't need to be limited for X"0A" (LF).

Records can be variable length

Disadvantages:

The file is generated with a header of 64 bytes, and each record with a
header and a trailer of 4 bytes with the length of itself.



Sequential DDM

Advantages

Doesn't require modification in the SELECT of our COBOL programs.

Supports any kind of data.

Records don't need to be limited for X"0A" (LF).

Records can be variable length

Disadvantages:

For each file, a second and hidden file (.DDMMEA) is generated, which
seems to have information about the file.



Any help, any experience, any advice will be appreciated.

Thanks, Mariela.
```

#### ↳ Re: Sequential Files in AIX

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-23T16:06:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310231506.5800587d@posting.google.com>`
- **References:** `<3515722.1066923948@dbforums.com>`

```
mpineyro <member45438@dbforums.com> wrote

> We are migrating an application from mainframe, VSE and Cobol II, to AIX
> [...]
> Records are limited for X"0A" (LF) (complicates a little the bin FTP).

Aren't 'Mainframe, VSE' EBCDIC and AIX ASCII ?

Surely you will be doing non-binary ftp.
```

##### ↳ ↳ Re: Sequential Files in AIX

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-24T00:05:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1_lb.3479$wc3.778@newsread3.news.pas.earthlink.net>`
- **References:** `<3515722.1066923948@dbforums.com> <217e491a.0310231506.5800587d@posting.google.com>`

```
This doesn't have to be a problem if one uses ONLY "usage display" and "sign
is separate" for numeric fields.  In such cases, one can do an FTP with an
"automatic" conversion between ASCII and EBCDIC.  If, on the other hand,
there are any COMP-n fields, there will be SIGNIFICANT conversion problems.
```

#### ↳ Re: Sequential Files in AIX

- **From:** mpineyro <member45438@dbforums.com>
- **Date:** 2003-10-24T09:38:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3519598.1067002702@dbforums.com>`
- **References:** `<3515722.1066923948@dbforums.com>`

```

We are using COMP fields, so we are doing the translation EBCDIC-ASCII
of the correspding fields (not de COMP ones) in the VSE and then, we
make a BIN FTP.
```

##### ↳ ↳ Re: Sequential Files in AIX

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-10-24T15:33:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8Dbmb.6751$8x2.3626515@newssrv26.news.prodigy.com>`
- **References:** `<3515722.1066923948@dbforums.com> <3519598.1067002702@dbforums.com>`

```
"mpineyro" <member45438@dbforums.com> wrote in message
news:3519598.1067002702@dbforums.com...
>
> We are using COMP fields, so we are doing the translation EBCDIC-ASCII
> of the correspding fields (not de COMP ones) in the VSE and then, we
> make a BIN FTP.

I thnk you need to read this:

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm


MCM
(author of same).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
