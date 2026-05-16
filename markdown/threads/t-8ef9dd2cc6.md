[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deleting "invalid" character from a file

_11 messages · 9 participants · 2003-05 → 2003-09_

---

### Deleting "invalid" character from a file

- **From:** datacraft@netzero.net (L V Squitin)
- **Date:** 2003-05-03T05:56:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```
I support an old PC application developed under Ryan Macfarland COBOL
vers 6.10. I am having a problem processing external input files that
contain the character hex 1A (decimal 26) ASCII right arrow.
As far as I can tell, RM/COBOL treats this character as an End-of-File
marker, and does not read beyond it.
The characted appears once every 15 records or so.
I would appreciate any suggestions on dealing programatically with
this problem. Manually editing the file to delete the offending char
is not an option.
```

#### ↳ Re: Deleting "invalid" character from a file

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-03T13:10:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IOicnYeWV6itmymjXTWJhQ@giganews.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```

"L V Squitin" <datacraft@netzero.net> wrote in message
news:be9d5d6a.0305030456.23e527e9@posting.google.com...
> I support an old PC application developed under Ryan Macfarland COBOL
> vers 6.10. I am having a problem processing external input files that
…[6 more quoted lines elided]…
> is not an option.

"1A" IS an end-of-file marker.

Can you get to the source code? If so, you might be able to redefine the
file attribute to be a non-text file, whereupon, I bet, the compiler will
use the length of the file as a limit instead of stopping at EOF.

Failing that, you might have to pre-process the file with another program to
change intermediate "1A" to a space.
```

##### ↳ ↳ Re: Deleting "invalid" character from a file

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-05-03T14:03:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b913q1$fco$1@ngspool-d02.news.aol.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com> <IOicnYeWV6itmymjXTWJhQ@giganews.com>`

```
There must be a way around this. x'1A' is also
decimal value 26. What if you had a field defined
as "pic 99 comp value 26."? You couldn't read the
data.
```

###### ↳ ↳ ↳ Re: Deleting "invalid" character from a file

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-03T18:55:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PvicnZuthMB2yymjXTWJiQ@giganews.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com> <IOicnYeWV6itmymjXTWJhQ@giganews.com> <b913q1$fco$1@ngspool-d02.news.aol.com>`

```

"Anon" <anon@anon.org> wrote in message
news:b913q1$fco$1@ngspool-d02.news.aol.com...
> There must be a way around this. x'1A' is also
> decimal value 26. What if you had a field defined
> as "pic 99 comp value 26."? You couldn't read the
> data.

Right. It can't be read. As a text file.

I bet you can't read a "1A" into Notepad or other text processor either.

No, I haven't tried it and don't really care. I'm just ruminating that "1A"
is not a valid text character and a program expecting text characters is
within its rights to treat "1A" as and end-of-file.
```

#### ↳ Re: Deleting "invalid" character from a file

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-03T15:50:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB42B95.5060109@Knology.net>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```
L V Squitin wrote:
> I support an old PC application developed under Ryan Macfarland COBOL
> vers 6.10. I am having a problem processing external input files that
…[6 more quoted lines elided]…
> is not an option.

My only guess would be to try putting "Block Contains 15 Records" on the 
FD of your input file.  However, I'll readily admit that it's just a 
stab in the dark...  :)  Good luck.
```

#### ↳ Re: Deleting "invalid" character from a file

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T22:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb43ba2.617122@news.optonline.net>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```
datacraft@netzero.net (L V Squitin) wrote:

>I support an old PC application developed under Ryan Macfarland COBOL
>vers 6.10. I am having a problem processing external input files that
…[6 more quoted lines elided]…
>is not an option.

I write a FILTER program which can remove them, or translate them to something
else. Send an email and I'll reply with a copy, including source. It's written
in COBOL. 

In the bad old days of DOS 1.0, 1A was the end of file marker on line sequential
files. 

Alternatively, you could define the file as record sequential, record size 512
(a disk sector), and parse records yourself using UNSTRING DELIMITED BY x'0D0A'.
```

##### ↳ ↳ Re: Deleting "invalid" character from a file

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-05-08T02:10:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MrOcnWkbrb98aSSjXTWcpg@comcast.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com> <3eb43ba2.617122@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb43ba2.617122@news.optonline.net...
> datacraft@netzero.net (L V Squitin) wrote:
>
…[10 more quoted lines elided]…
> I write a FILTER program which can remove them, or translate them to
something
> else. Send an email and I'll reply with a copy, including source. It's
written
> in COBOL.
>
> In the bad old days of DOS 1.0, 1A was the end of file marker on line
sequential
> files.
>
> Alternatively, you could define the file as record sequential, record size
512
> (a disk sector), and parse records yourself using UNSTRING DELIMITED BY
x'0D0A'.
>
        You would still need to consider Tabs.  Bother.
```

###### ↳ ↳ ↳ Re: Deleting "invalid" character from a file

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-09T02:03:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebae561.26410746@news.optonline.net>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com> <3eb43ba2.617122@news.optonline.net> <MrOcnWkbrb98aSSjXTWcpg@comcast.com>`

```
"Russell Styles" <RWS0202@comcast.net> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[28 more quoted lines elided]…
>        You would still need to consider Tabs.  Bother.

Actually, 'do it yourself expansion' is a FEATURE in re tabs. There are two tab
conventions, not one. COBOL uses the text-editor convention where there is a tab
every 8 cols. Files produced by spreadsheets and the like use a 'tab delimited'
format which has one tab between columns, no matter how far apart they are. 

How do you know where columns begin? You guess. I usually make them 10 or 20
cols wide.
```

#### ↳ Re: Deleting "invalid" character from a file

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-04T01:21:39+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6g8bv899f2nvcpudepbi7gjkoqq8p8pe8@4ax.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```
On 3 May 2003 05:56:49 -0700 datacraft@netzero.net (L V Squitin) wrote:

:>I support an old PC application developed under Ryan Macfarland COBOL
:>vers 6.10. I am having a problem processing external input files that
:>contain the character hex 1A (decimal 26) ASCII right arrow.
:>As far as I can tell, RM/COBOL treats this character as an End-of-File
:>marker, and does not read beyond it.
:>The characted appears once every 15 records or so.
:>I would appreciate any suggestions on dealing programatically with
:>this problem. Manually editing the file to delete the offending char
:>is not an option.

What does the SELECT and FD look like?
```

#### ↳ Re: Deleting "invalid" character from a file

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-09-24T19:07:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LXydnTCJb8M2rO-iU-KYgA@comcast.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com>`

```
In article <be9d5d6a.0305030456.23e527e9@posting.google.com>, 
datacraft@netzero.net wrote:

>I support an old PC application developed under Ryan Macfarland COBOL
>vers 6.10. I am having a problem processing external input files that
…[6 more quoted lines elided]…
>is not an option.

Perhaps you'd be better off investigating why that non-ASCII character
appears in the data file than adjusting your program to deal with it.
If you can't fix the file creation, perhaps an INSPECT REPLACING 
LOW_VALUES with SPACE on each record would do the trick?
```

##### ↳ ↳ Re: Deleting "invalid" character from a file

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-24T22:39:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309242139.39dfb3d1@posting.google.com>`
- **References:** `<be9d5d6a.0305030456.23e527e9@posting.google.com> <LXydnTCJb8M2rO-iU-KYgA@comcast.com>`

```
weberm@polaris.net (Ubiquitous) wrote 

> >I support an old PC application developed under Ryan Macfarland COBOL
> >vers 6.10. I am having a problem processing external input files that
> >contain the character hex 1A (decimal 26) ASCII right arrow.
> >As far as I can tell, RM/COBOL treats this character as an End-of-File
> >marker, and does not read beyond it.

hex 1A, Ctrl-Z, is the end of file marker.  This started in CP/M in
the mid 70s and was kept when MS bought a clone of CP/M from SCP which
they called MS-DOS.  While later versions of MS-DOS may not need this
file terminator many programs still recognise it.

> >The characted appears once every 15 records or so.
> >I would appreciate any suggestions on dealing programatically with
> >this problem. Manually editing the file to delete the offending char
> >is not an option.

You may need to run a filter on the file before Cobol gets to read it.
 If you are reading the file as LINE SEQUENTIAL then it should not
contain control characters other than tab, lf, cr.  ie if it has hex
1A in it and this is not eon of file then it is _NOT_ a line
sequential file.
 
If you read it as a binary sequential file with a one byte record file
you can deal with any byte values in the file and can assemble the
data using cr, lf to signal when a 'record' is complete.

> Perhaps you'd be better off investigating why that non-ASCII character
> appears in the data file than adjusting your program to deal with it.
> If you can't fix the file creation, perhaps an INSPECT REPLACING 
> LOW_VALUES with SPACE on each record would do the trick?

hex 1A is not low-values.  If it is treating hex 1A as end of file
then the program doesn't get to see the byte, so thinking they can be
replaced in the program is fruitless.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
