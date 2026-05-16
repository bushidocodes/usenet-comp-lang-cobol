[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed Files in OUTPUT with appends...

_4 messages · 4 participants · 2002-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed Files in OUTPUT with appends...

- **From:** "Nicod���me" <maitrenicodeme@hotmail.com>
- **Date:** 2002-04-17T11:41:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9jg5d$una$1@s1.read.news.oleane.net>`

```
Hello,

First, I beg your pardon if my english is bad, I'm french...

A friend have a program in COBOL. He want to obtain an indexed file in
output, but in append... So he have use the command EXTENDS, but the
compiler make an error...
So, if someone could tell me how to use indexed file in output with append,
He will be nice :) !

Thanks,

Nicod�me.
```

#### ↳ Re: Indexed Files in OUTPUT with appends...

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2002-04-17T10:17:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65b0287c26bef7ec2a6bfd88036ed356.40368@mygate.mailgate.org>`
- **References:** `<a9jg5d$una$1@s1.read.news.oleane.net>`

```
Hi

You need to define a primary key and, if you want, add some alternate 
keys. 
Here is a little example of coding:

FILE-CONTROL.
    SELECT   DATAFILE   ASSIGN TO "DATA.INX"
                        ORGANIZATION INDEXED
                        ACCESS DYNAMIC
                        RECORD KEY KEY1
                        ALTERNATE RECORD KEY KEY2
                        DUPLICATES
                        FILE STATUS  IS FILE-STATUS.
...
...
DATA DIVISION.
FILE SECTION.

FD   DATAFILE
     LABEL RECORD STANDARD.

01   FD-REC.
     02  KEY1.
         05  CUSTOMER-KEY          PIC X(6).
     02  KEY2.
         05  CUSTOMER-NAME         PIC X(40).
...
...

Hope in this help
     
Gianni

"Nicodï¿½me" <maitrenicodeme@hotmail.com> wrote in message
news:a9jg5d$una$1@s1.read.news.oleane.net...

> Hello,
> 
…[10 more quoted lines elided]…
> Nicodï¿½me.
```

#### ↳ Re: Indexed Files in OUTPUT with appends...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-04-17T11:46:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgdv8.22313$bn2.2858@nwrddc01.gnilink.net>`
- **References:** `<a9jg5d$una$1@s1.read.news.oleane.net>`

```
Nicod�me <maitrenicodeme@hotmail.com> wrote in message
news:a9jg5d$una$1@s1.read.news.oleane.net...
> So, if someone could tell me how to use indexed file in output with
append,
> He will be nice :) !

To write to an indexed file you just open the file I-O, set the key (either
a relative key or key value) and do a WRITE. If the record does not exist in
the file, it will be added. If the record does exist, you will get an
INVALID KEY condition or the appropriate file status if you do not specify
an INVALID KEY clause in the WRITE.

OPEN APPEND only applies to sequential I-O and does not apply to files with
ORGANIZATION INDEXED or ORGANIZATION RELATIVE.  (This might be the cause of
the compile-time error).

MCM
```

#### ↳ Re: Indexed Files in OUTPUT with appends...

- **From:** "Alberto Magalh���es" <aamagalhaes@oninet.pt>
- **Date:** 2002-04-17T23:48:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9ku2q$dfm$1@news.oninet.pt>`
- **References:** `<a9jg5d$una$1@s1.read.news.oleane.net>`

```
Hi, Nicod�me, the OPEN EXTEND is for sequential files.
For you to make a append to an INDEX FILE, you only have to open it in
INPUT-OUTPUT, and write it, look at your keys, to see how records will be
'arrange it'.
AAM
"Nicod�me" <maitrenicodeme@hotmail.com> wrote in message
news:a9jg5d$una$1@s1.read.news.oleane.net...
> Hello,
>
…[5 more quoted lines elided]…
> So, if someone could tell me how to use indexed file in output with
append,
> He will be nice :) !
>
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
