[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT and FILE STATUS

_4 messages · 3 participants · 2007-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### SORT and FILE STATUS

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-01-24T09:24:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ep755i$g5v$03$1@news.t-online.com>`

```
Is FILE STATUS legal with a SORT file ?
Can't see anywhere in the standard that says it is not.
If so, when and under what conditions should the file
status be set in combination with the SORT/USING/GIVING/RELEASE/RETURN
statments.
The chapter 9.1.12 I-O status only refers to usual I/O statements.

Roger
```

#### ↳ Re: SORT and FILE STATUS

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-01-24T04:30:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12rea0an97lrq8f@corp.supernews.com>`
- **References:** `<ep755i$g5v$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:ep755i$g5v$03$1@news.t-online.com...
> Is FILE STATUS legal with a SORT file ?
> Can't see anywhere in the standard that says it is not.
…[3 more quoted lines elided]…
> The chapter 9.1.12 I-O status only refers to usual I/O statements.

ISO/IEC 1989:200x WD 1.6, 12.3.4.1 [File control
entry] General format, Format 4 (sort-merge), page 233,
contains no provision for a FILE STATUS clause.

12.3.4.2 [File control entry] Syntax rules, page 234,
"FORMAT 1
9) Format 1 shall be specified only for an indexed file.
The associated file description entry shall not be a
sort-merge file description entry.
FORMAT 2
10) Format 2 shall be specified only for a relative file.
The associated file description entry shall not be a
sort-merge file description entry.
...
FORMAT 3
12) Format 3 shall be specified only for a sequential
file or a report file. The associated file description entry
shall not be a sort-merge file description entry.
FORMAT 4
13) Format 4 shall be specified only for a sort-merge file.
The associated file description entry shall be a sort-merge
file description entry."

Formats 1, 2, and 3 (indexed, relative, and sequential,
respectively) have FILE STATUS clauses; but Format 4
does not.

Having a FILE STATUS clause with a sort-merge file
description entry would be an implementor extension.
Micro Focus allowed (allows) a SORT STATUS
clause (FILE STATUS was a synonym). Available
status keys were (are) 0/0 - Successful, 3/0 - Permanent
Error, and 9/nnn - Operating system error message
number. Status values were (are) updated after each
sort operation.

[I use a past (present) relation, above, because the
Micro Focus product I have will become a teenager
in a few months and information from the manuals I
have may not apply to current products.]
```

##### ↳ ↳ Re: SORT and FILE STATUS

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-01-24T12:40:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ep7gir$87h$03$1@news.t-online.com>`
- **References:** `<ep755i$g5v$03$1@news.t-online.com> <12rea0an97lrq8f@corp.supernews.com>`

```
OK.
Thanks Rick, I missed that.

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12rea0an97lrq8f@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[50 more quoted lines elided]…
>
```

#### ↳ Re: SORT and FILE STATUS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-01-24T16:25:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VLLth.4342$L62.3475@fe12.news.easynews.com>`
- **References:** `<ep755i$g5v$03$1@news.t-online.com>`

```
Rick gave the correct answer for the SD file itself.  It is worth noting, 
however, that one MAY specify a File Status clause for the Input/Output files. 
In fact, this is exactly why IBM says that using the FASTSRT compiler option 
(where their non-COBOL SORT utility does the I/O) is *not* ANSI/ISO conforming. 
They do NOT update the FS (or more importantly reach I/O Declaratives) if there 
is an I/O "problem" with Input/Output files during a SORT (without an 
Input/Output procedure) when FASTSRT is in effect.  They DO conform to the 
Standard when NOFASTSRT is specified.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
