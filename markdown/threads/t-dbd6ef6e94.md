[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# been a long time

_10 messages · 6 participants · 2005-09_

---

### been a long time

- **From:** "Moe" <moesplace@moetele.com>
- **Date:** 2005-09-13T08:40:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com>`

```
It's been a long time since I've programmed in Cobol, and have a
question for the group.

We have a Pic X(32) field that we are filling with 8-10 characters.
No problem there.
What we need in the output file is those 8-10 characters followed by as
many spaces as are needed to get to the 32 char field length.

Any quick and easy way to do this?

Sorry for such a newbie question.
-Moe
```

#### ↳ Re: been a long time

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-09-13T18:45:20+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com>`

```
On 13 Sep 2005 08:40:36 -0700 "Moe" <moesplace@moetele.com> wrote:

:>It's been a long time since I've programmed in Cobol, and have a
:>question for the group.

:>We have a Pic X(32) field that we are filling with 8-10 characters.
:>No problem there.
:>What we need in the output file is those 8-10 characters followed by as
:>many spaces as are needed to get to the 32 char field length.

:>Any quick and easy way to do this?

It is automatic.

A move into a 32 character field will truncate longer fields and pad shorter
fields.
```

##### ↳ ↳ Re: been a long time

- **From:** "Moe" <moesplace@moetele.com>
- **Date:** 2005-09-13T09:28:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126628889.246690.25780@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com>`

```
But for some reason, it is ignoring the "spaces" when it writes the
record out...  any clues?
```

###### ↳ ↳ ↳ Re: been a long time

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-09-13T19:52:26+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2r0ei1prb24apnlpcq2o5kh5i9g4ncck5k@4ax.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com>`

```
On 13 Sep 2005 09:28:09 -0700 "Moe" <moesplace@moetele.com> wrote:

:>But for some reason, it is ignoring the "spaces" when it writes the
:>record out...  any clues?

What do you mean?

There is other data?

The record is short?

?
```

###### ↳ ↳ ↳ Re: been a long time

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-09-13T17:57:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com>`

```
On 13 Sep 2005 09:28:09 -0700, "Moe" <moesplace@moetele.com> wrote:

>But for some reason, it is ignoring the "spaces" when it writes the
>record out...  any clues?
Yes. 
This is dependent on the file format used, and on the compiler vendor
used, and on the OS used.

If using a line sequential file for example, trailing spaces are
removed.

So please post your SELECT, your FD and your vendor/version/OS used



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: been a long time

_(reply depth: 4)_

- **From:** "Moe" <moesplace@moetele.com>
- **Date:** 2005-09-13T10:20:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126632046.419760.86770@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com> <041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com>`

```
Sun Solaris 8 on SPARC  Using MicroFocus Cobol compiler.

SELECT APIFILE-FILE         ASSIGN TO DISK
ORGANIZATION                LINE SEQUENTIAL
STATUS                      WS-WORK-FILE-STATUS.

FD  APIFILE-FILE VALUE OF
FILE-ID APF-APIFILE-NAME.
01  APIFILE-REC                 PIC X(289).
```

###### ↳ ↳ ↳ Re: been a long time

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-13T18:08:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oAEVe.47842$yd.4821@fe11.news.easynews.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com> <041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com> <1126632046.419760.86770@g14g2000cwa.googlegroups.com>`

```
Can you show us the actual fields being moved and the MOVE statements?

If you move a 32-byte field to a 32-byte field, it will move the WHOLE "input" 
field, not just the non-blank data.  If you move an 8-byte field to a 32-byte 
field, it will ALWAYS "space pad".  If you have trailing spaces in a LINE 
SEQUENTIAL file it may (or may not, depends on lots of stuff) truncating 
trailing spaces.
```

###### ↳ ↳ ↳ Re: been a long time

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-13T11:33:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126636417.914058.8320@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1126632046.419760.86770@g14g2000cwa.googlegroups.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com> <041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com> <1126632046.419760.86770@g14g2000cwa.googlegroups.com>`

```
> ORGANIZATION                LINE SEQUENTIAL

If you want records that are of a particular size then you need to use
'sequential' (remove 'line' but you will have to add your own cr/lf
line terminators if these are required.  If the records are to be
various lengths then the system will probably add record headers as it
needs to know where each record starts and ends and this will probably
not be what you want.
```

###### ↳ ↳ ↳ Re: been a long time

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-09-13T13:34:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ie6tb9su8fc52@news.supernews.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com> <041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com> <1126632046.419760.86770@g14g2000cwa.googlegroups.com>`

```
Moe wrote:
> Sun Solaris 8 on SPARC  Using MicroFocus Cobol compiler.
>
…[6 more quoted lines elided]…
> 01  APIFILE-REC                 PIC X(289).

Some compilers (you evidently have one) believe that trailing spaces should 
be removed from "LINE SEQUENTIAL" files because the compiler-generated code 
will re-attach the spaces when the file is read. These compilers do this for 
the defensible reason of saving space.

Some compilers do not do this, writing the entire record even if the record 
is entirely blank.

Two solutions come to mind:

1. Change the ORGANIZATION to SEQUENTIAL. You will have to increase the 
record length by two bytes and manually add CR/LF bytes at the end (if those 
are the characters delimiting each record), or

2. Insert a special, non-confusing, terminal character (HIGH-VALUES?) as the 
last byte when the last byte is a blank and remove this sentinel charcter 
first thing when the file is read.
```

###### ↳ ↳ ↳ Re: been a long time

_(reply depth: 6)_

- **From:** "Moe" <moesplace@moetele.com>
- **Date:** 2005-09-13T12:01:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126637096.017464.69520@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<11ie6tb9su8fc52@news.supernews.com>`
- **References:** `<1126626036.840068.182540@z14g2000cwz.googlegroups.com> <husdi1lfqk0jk2nps8r17j3a9tt7snpfhk@4ax.com> <1126628889.246690.25780@g47g2000cwa.googlegroups.com> <041ei11900no6fos4t1n6rg16nkf7i9slp@4ax.com> <1126632046.419760.86770@g14g2000cwa.googlegroups.com> <11ie6tb9su8fc52@news.supernews.com>`

```
Yes, we want fixed-length records, just with about 22 or 23 (depending
on size of last field) spaces at the end of them.
I will try changing the ORG to SEQ and manually put on the CR/LF bytes.
Thanks...  Will let you know how it goes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
