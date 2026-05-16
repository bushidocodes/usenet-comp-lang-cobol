[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read Unknown Length record

_5 messages · 5 participants · 2004-12_

---

### Read Unknown Length record

- **From:** svaranas@hotmail.com
- **Date:** 2004-12-16T14:58:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`

```
Hi All,
We have file containing n*Records without any Line seperator.
This implies complete file will be in one line: Now, How do we read
this one line (nRecords with no seperator) in Cobol?

No. of Records in the file can vary from 2000-15000 and each record is
of size 60 bytes.

Would it be possible to read a file for X bytes without knowing the
complete length?

Can someone help me please !

-Vijay
```

#### ↳ Re: Read Unknown Length record

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2004-12-16T18:07:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103249221.926714.131930@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`
- **References:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`

```
> We have file containing n*Records without any Line seperator.
> This implies complete file will be in one line:

No, it does not imply that at all.  Not in Cobol, nor in any language.
The file is most likely in fixed length segments, the length of which
is known to be program.  The program just reads one chunk of n bytes
and then the next chunk of n bytes.

> No. of Records in the file can vary from 2000-15000 and
> each record is of size 60 bytes.

Exactly.   The program knows it is 60 byte records so the first read
just reads bytes 1 - 60 and advances the file pointer to 61.  The next
read gets bytes 61-120 and so on.
```

#### ↳ Re: Read Unknown Length record

- **From:** docdwarf@panix.com
- **Date:** 2004-12-16T21:09:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cptf55$qrc$1@panix5.panix.com>`
- **References:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`

```

- posted and emailed -

In article <1103237938.139278.319220@z14g2000cwz.googlegroups.com>,
 <svaranas@hotmail.com> wrote:
>Hi All,
>We have file containing n*Records without any Line seperator.

[snip]

>Can someone help me please !

This might be possible... but it would be good not to duplicate your own 
efforts; please post what you have coded so far for a solution.

DD
```

#### ↳ Re: Read Unknown Length record

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-12-16T20:15:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1OOdnTIN867E3F_cRVn-uQ@giganews.com>`
- **References:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`

```
svaranas@hotmail.com wrote:
> Hi All,
> We have file containing n*Records without any Line seperator.
…[9 more quoted lines elided]…
> Can someone help me please !

Allow me to rephrase: You have an indeterminate number of fixed-length 
60-byte records. Yes?

COBOL generally admits of two types of text files:

LINE SEQUENTIAL where the record is delimited by a carriage-return and the 
unused bytes of the FD are blank-filled on input and

SEQUENTIAL where the record is defined as the length specified in the FD.

Point being, there are TWO types of sequential files native to COBOL; you 
want the other one.

In your case:

   SELECT IN-FILE ASSIGN TO {something}
      ORGANIZATION IS SEQUENTIAL (or whatever your compiler uses)
      ...

FD  IN-FILE.
01  IN-REC   PIC X(60).

There is another way. Don't use it if you want the results before next 
Wednesday.

FD  IN-FILE.
01  IN-REC  PIC X.

PERFORM VARYING I FROM 1 BY 1 UNTIL I > 60
   READ IN-FILE
   END-PERFORM.

This last example burns CPU cycles like witches in Salem, but may sometimes 
be necessary if the record delimited is something goofy (like "?").
```

#### ↳ Re: Read Unknown Length record

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-12-17T05:40:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5s4s0pscuum9t80f8to6e6m4afhk7pktu@4ax.com>`
- **References:** `<1103237938.139278.319220@z14g2000cwz.googlegroups.com>`

```
On 16 Dec 2004 14:58:58 -0800, svaranas@hotmail.com wrote:

>Hi All,
>We have file containing n*Records without any Line seperator.
…[9 more quoted lines elided]…
>Can someone help me please !

It's normal for 'Cobol files' to not have a line seperator. Define it
as ORGANIZATION [RECORD] SEQUENTIAL with a record length (in the FD)
of 60 bytes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
