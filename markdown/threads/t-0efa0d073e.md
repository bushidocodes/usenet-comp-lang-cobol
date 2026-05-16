[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (OT) Utility to conver Line Sequential (source) files

_6 messages · 5 participants · 2009-01_

---

### (OT) Utility to conver Line Sequential (source) files

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-27T20:27:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com>`

```
I am starting to try and get OpenCOBOL working on my Windows XP machine (with 
Cygwin).

I am aware of the difference between Unix/Linux vs Windows "line sequential" 
files (i.e. LF vs CRLF).  I still like some of my Windows editors and editing 
tools.

Therefore, I am wondering if there is a free tool or utility that can be run 
under Windows to "create" a Unix/Linux type LS file from a Windows file, i.e. 
remove the "CR".

I know that I could write such a utility in COBOL, but I was hoping that there 
would be such a tool freely available.  I tried a google search, but must have 
used "COBOL" type terminology because all I got back were COBOL type hits.
```

#### ↳ Re: (OT) Utility to conver Line Sequential (source) files

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-01-27T21:16:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60b8f6f3-875e-4b53-93df-defc9bd3c762@o4g2000pra.googlegroups.com>`
- **References:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com>`

```
On Jan 28, 3:27 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> I am starting to try and get OpenCOBOL working on my Windows XP machine (with
> Cygwin).
…[15 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

http://www.cyberciti.biz/faq/howto-unix-linux-convert-dos-newlines-cr-lf-unix-text-format/

http://www.vasudevaservice.com/documentation/how-to/converting_dos_and_unix_text_files
The cygutils package

The optional cygutils package contains miscellaneous tools that are
small enough to not require their own package. It is not included in a
default Cygwin install; select it from the Utils category in
setup.exe. Several of the cygutils tools are useful for interacting
with Windows.

One of the hassles of Unix-Windows interoperability is the different
line endings on text files. As mentioned in the section called “Text
and Binary modes”, Unix tools such as tr can convert between CRLF and
LF endings, but cygutils provides several dedicated programs: conv,
d2u, dos2unix, u2d, and unix2dos. Use the --help switch for usage
information.
```

##### ↳ ↳ Re: (OT) Utility to conver Line Sequential (source) files

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-28T00:39:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t4Tfl.212139$jv1.191118@en-nntp-09.dc1.easynews.com>`
- **References:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com> <60b8f6f3-875e-4b53-93df-defc9bd3c762@o4g2000pra.googlegroups.com>`

```
thanks.  That's what I was looking for
```

#### ↳ Re: (OT) Utility to conver Line Sequential (source) files

- **From:** David Essex <nospam@nobloodyspam.nospam>
- **Date:** 2009-01-30T07:17:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<311a9$4982f03a$d8fe9c07$16899@PRIMUS.CA>`
- **In-Reply-To:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com>`
- **References:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com>`

```
There are some editors which support both LS formats.

Have you tried PFE (Programmer's File Editor) [1].
A nice feature of this editor, among many, is the ability to read both
LS formats and write (save) in which ever format you choose.

It has not been updated since 1999, but it is free (binary only).

Hum, in this case, there is such a thing as a 'free lunch'.

1) The Latest Version (32-bit 1.01) of PFE (pfe101i.zip)
http://www.lancs.ac.uk/staff/steveb/cpaap/pfe/pfefiles.htm


William M. Klein wrote:
> I am starting to try and get OpenCOBOL working on my Windows XP machine (with 
> Cygwin).
…[11 more quoted lines elided]…
> used "COBOL" type terminology because all I got back were COBOL type hits.
```

##### ↳ ↳ Re: (OT) Utility to conver Line Sequential (source) files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-01-30T08:42:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt76o45i4hipdhscrkf73viijdn4ksk622@4ax.com>`
- **References:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com> <311a9$4982f03a$d8fe9c07$16899@PRIMUS.CA>`

```
On Fri, 30 Jan 2009 07:17:36 -0500, David Essex
<nospam@nobloodyspam.nospam> wrote:

>There are some editors which support both LS formats.

Particularly with Unix machines such as MacIntoshes.
```

#### ↳ Re: (OT) Utility to conver Line Sequential (source) files

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2009-01-31T01:42:49
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1233366169@f1.n250.z2.fidonet.ftn>`
- **References:** `<_nPfl.163331$9i5.110063@en-nntp-07.dc1.easynews.com>`

```
Hello William!

28 Jan 09 02:27, William M. Klein wrote to All:

 WMK> Therefore, I am wondering if there is a free tool or utility that can
 WMK> be run under Windows to "create" a Unix/Linux type LS file from a
 WMK> Windows file, i.e. remove the "CR".

There is under linux and therefore avail to any other platform 2 progs: 
dos2unix & unix2dos and they do just that remove or add the missing bits 
depending on running platform.

If you have a problem locating these and have access to a C compiler ie gcc 
etc shout or email me and I'm send you the sources.


Vince
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
