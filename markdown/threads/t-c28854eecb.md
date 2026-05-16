[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# vsam algorithms?

_18 messages · 8 participants · 2003-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### vsam algorithms?

- **From:** Mike <Mike@mikee.ath.cx>
- **Date:** 2003-05-10T14:34:56
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
I want to implement my own vsam system. Where can I find the algorithms
that detail structure of the data, what fields, what blocks, how
written, how read, records added and deleted, and such?

Mike
```

#### ↳ Re: vsam algorithms?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-05-10T16:52:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c31714$56ea8260$71caf943@chottel>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
I believe VSAM files are a variation on the B-Tree file structure.  A good
data structure or file structure book should help get you started.

Mike <Mike@mikee.ath.cx> wrote in article
<vbq3gg54g6mdf3@corp.supernews.com>...
> I want to implement my own vsam system. Where can I find the algorithms
> that detail structure of the data, what fields, what blocks, how
…[3 more quoted lines elided]…
>
```

#### ↳ Re: vsam algorithms?

- **From:** "scarface" <scarface@scarface.com>
- **Date:** 2003-05-11T02:47:04+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2003.05.10.18.47.04.5664@scarface.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
On Sat, 10 May 2003 14:34:56 +0000, Mike wrote:

> I want to implement my own vsam system. Where can I find the algorithms
> that detail structure of the data, what fields, what blocks, how
> written, how read, records added and deleted, and such?
> 
> Mike

You can go to IBM.com. Try to download VSAM books and the
SoftCopy Reader.
```

#### ↳ Re: vsam algorithms?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-10T22:38:07+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<08lqbvo8qqf5ro47jf2q9j3vbs70o3blub@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
On Sat, 10 May 2003 14:34:56 -0000 Mike <Mike@mikee.ath.cx> wrote:

:>I want to implement my own vsam system. Where can I find the algorithms
:>that detail structure of the data, what fields, what blocks, how
:>written, how read, records added and deleted, and such?

Research "Control Interval Processing".
```

#### ↳ Re: vsam algorithms?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T20:08:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd4a27.183305146@news.optonline.net>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
Mike <Mike@mikee.ath.cx> wrote:

>I want to implement my own vsam system. Where can I find the algorithms
>that detail structure of the data, what fields, what blocks, how
>written, how read, records added and deleted, and such?

Why not use an ODBC driver?  You can find some links to them here:

http://ourworld.compuserve.com/homepages/Ken_North/odbcvend.htm

If you still want to write your own, almost all IBM manuals are available
online. Look here for instructions on how to find them:

http://www.xephon.com/updates/VSAMl.html
```

##### ↳ ↳ Re: vsam algorithms?

- **From:** Mike <Mike@mikee.ath.cx>
- **Date:** 2003-05-10T20:38:38
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbqoqe7rfdq10@corp.supernews.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net>`

```
In article <3ebd4a27.183305146@news.optonline.net>, Robert Wagner wrote:
> Mike <Mike@mikee.ath.cx> wrote:
> 
…[11 more quoted lines elided]…
> http://www.xephon.com/updates/VSAMl.html

I don't want the ODBC for it implies I have a much larger database hanging
around someplace. I want something like a very small VSAM or dbm for small
projects that don't require large databases, contract programs where I
don't want to admin their database, and hopefully it will be small enough
for embedded systems built with J2ME.

Mike
```

###### ↳ ↳ ↳ Re: vsam algorithms?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-10T23:52:36+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com>`

```
On Sat, 10 May 2003 20:38:38 -0000 Mike <Mike@mikee.ath.cx> wrote:

:>In article <3ebd4a27.183305146@news.optonline.net>, Robert Wagner wrote:

:>> Mike <Mike@mikee.ath.cx> wrote:
 
:>>>I want to implement my own vsam system. Where can I find the algorithms
:>>>that detail structure of the data, what fields, what blocks, how
:>>>written, how read, records added and deleted, and such?
 
:>> Why not use an ODBC driver?  You can find some links to them here:
 
:>> http://ourworld.compuserve.com/homepages/Ken_North/odbcvend.htm
 
:>> If you still want to write your own, almost all IBM manuals are available
:>> online. Look here for instructions on how to find them:
 
:>> http://www.xephon.com/updates/VSAMl.html

:>I don't want the ODBC for it implies I have a much larger database hanging
:>around someplace. I want something like a very small VSAM or dbm for small
:>projects that don't require large databases, contract programs where I
:>don't want to admin their database, and hopefully it will be small enough
:>for embedded systems built with J2ME.

Then why do you care about the structure?

VSAM is a base part of the operating system!
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 4)_

- **From:** Mike <Mike@mikee.ath.cx>
- **Date:** 2003-05-10T21:29:07
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbqrp3jgl16u5a@corp.supernews.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com>`

```
In article <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com>, Binyamin Dissen wrote:
> On Sat, 10 May 2003 20:38:38 -0000 Mike <Mike@mikee.ath.cx> wrote:
> 
…[25 more quoted lines elided]…
> VSAM is a base part of the operating system!

I care because I don't have a vsam library on unix or embedded devices.

Mike
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-11T01:05:33+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ptqbvos1gd6lhm0lp8j60i1shc7gkgl56@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com> <vbqrp3jgl16u5a@corp.supernews.com>`

```
On Sat, 10 May 2003 21:29:07 -0000 Mike <Mike@mikee.ath.cx> wrote:

:>In article <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com>, Binyamin Dissen wrote:

:>> On Sat, 10 May 2003 20:38:38 -0000 Mike <Mike@mikee.ath.cx> wrote:
 
:>>:>In article <3ebd4a27.183305146@news.optonline.net>, Robert Wagner wrote:
 
:>>:>> Mike <Mike@mikee.ath.cx> wrote:
  
:>>:>>>I want to implement my own vsam system. Where can I find the algorithms
:>>:>>>that detail structure of the data, what fields, what blocks, how
:>>:>>>written, how read, records added and deleted, and such?
  
:>>:>> Why not use an ODBC driver?  You can find some links to them here:
  
:>>:>> http://ourworld.compuserve.com/homepages/Ken_North/odbcvend.htm
  
:>>:>> If you still want to write your own, almost all IBM manuals are available
:>>:>> online. Look here for instructions on how to find them:
  
:>>:>> http://www.xephon.com/updates/VSAMl.html
 
:>>:>I don't want the ODBC for it implies I have a much larger database hanging
:>>:>around someplace. I want something like a very small VSAM or dbm for small
:>>:>projects that don't require large databases, contract programs where I
:>>:>don't want to admin their database, and hopefully it will be small enough
:>>:>for embedded systems built with J2ME.
 
:>> Then why do you care about the structure?
 
:>> VSAM is a base part of the operating system!

:>I care because I don't have a vsam library on unix or embedded devices.

Why do you wish to use the VSAM structure rather than some structure you
define yourself?

VSAM is a sort of jack-of-all-trades structure - you would be better off
defining something relevant to your application.
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 6)_

- **From:** Mike <Mike@mikee.ath.cx>
- **Date:** 2003-05-11T01:59:16
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbrbjkenrvi1d5@corp.supernews.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com> <vbqrp3jgl16u5a@corp.supernews.com> <3ptqbvos1gd6lhm0lp8j60i1shc7gkgl56@4ax.com>`

```
In article <3ptqbvos1gd6lhm0lp8j60i1shc7gkgl56@4ax.com>, Binyamin Dissen wrote:
> On Sat, 10 May 2003 21:29:07 -0000 Mike <Mike@mikee.ath.cx> wrote:
> 
…[37 more quoted lines elided]…
> defining something relevant to your application.

In reality I don't care if its vsam, isam, or something else. I really
want key/value pairs stored on disk such that the manipulating
code is small and the stored values are small. For embedded systems
I expect maybe a few thousand records with maybe 100 bytes of length
each. For small applications on my servers it could be more or less.
What I don't want is a full DBMS. If I could get a very light version
of unix dbm I'd be quite satisfied.

Mike
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-11T09:58:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8ED466.09581711052003@corp.supernews.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com> <vbqrp3jgl16u5a@corp.supernews.com> <3ptqbvos1gd6lhm0lp8j60i1shc7gkgl56@4ax.com> <vbrbjkenrvi1d5@corp.supernews.com>`

```
In article <vbrbjkenrvi1d5@corp.supernews.com>,
 Mike <Mike@mikee.ath.cx> wrote:
> 
> In reality I don't care if its vsam, isam, or something else. I really
…[7 more quoted lines elided]…
> Mike

Did you say you wanted this in J2ME?  Why not use a properties file?  
I'm only able in standard edition, does the ME no have the property 
object?
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 8)_

- **From:** Mike <Mike@mikee.ath.cx>
- **Date:** 2003-05-11T15:55:18
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbssj6i5rsv9b9@corp.supernews.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com> <vbqrp3jgl16u5a@corp.supernews.com> <3ptqbvos1gd6lhm0lp8j60i1shc7gkgl56@4ax.com> <vbrbjkenrvi1d5@corp.supernews.com> <joe_zitzelberger-8ED466.09581711052003@corp.supernews.com>`

```
In article <joe_zitzelberger-8ED466.09581711052003@corp.supernews.com>, wrote:
> In article <vbrbjkenrvi1d5@corp.supernews.com>,
>  Mike <Mike@mikee.ath.cx> wrote:
…[13 more quoted lines elided]…
> object?

The prefs objects seem to be slow and limited in size of items stored.
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-11T01:51:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebda012.205303517@news.optonline.net>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com> <vbqrp3jgl16u5a@corp.supernews.com>`

```
Mike <Mike@mikee.ath.cx> wrote:

>In article <4jpqbvo9rfud76rihjh1d1u2g75d9rrj3d@4ax.com>, Binyamin Dissen wrote:
>> On Sat, 10 May 2003 20:38:38 -0000 Mike <Mike@mikee.ath.cx> wrote:
…[28 more quoted lines elided]…
>I care because I don't have a vsam library on unix or embedded devices.

You want something like C-ISAM, owned by Informix which in turn is now owned by
IBM. 

You might find something useful at http://www.bytedesigns.com/ or try searching
on cisam or disam.
```

###### ↳ ↳ ↳ Re: vsam algorithms?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-11T01:51:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd7b87.195946839@news.optonline.net>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com>`

```
Mike <Mike@mikee.ath.cx> wrote:

>In article <3ebd4a27.183305146@news.optonline.net>, Robert Wagner wrote:
>> Mike <Mike@mikee.ath.cx> wrote:
…[18 more quoted lines elided]…
>for embedded systems built with J2ME.

In that case, get a COBOL compiler. They all come with a VSAM-like file system
out of the box. There is no need to write your own. 

Dave Sokol, one of the two authors of Realia COBOL, told me they spent more time
on the file system than on the COBOL compiler. Developing your own file system
is not a weekend project.
```

###### ↳ ↳ ↳ Re: vsam algorithms?

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-05-12T14:16:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k4bvbv0np2qru38vk5pvfbkh3e683gfk1r@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com> <3ebd7b87.195946839@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote:

>Mike <Mike@mikee.ath.cx> wrote:
>
…[27 more quoted lines elided]…
>is not a weekend project. 

Robert:

Minor correction.  His name is Marc Sokol, not Dave.  The other
gentleman was Ken Belcher.





Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: vsam algorithms?

- **From:** Alain Reymond <>
- **Date:** 2003-05-12T09:20:40+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odiubv4g17673cgs609dhhfh3t2ov3bmhs@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com> <3ebd4a27.183305146@news.optonline.net> <vbqoqe7rfdq10@corp.supernews.com>`

```
On Sat, 10 May 2003 20:38:38 -0000, Mike <Mike@mikee.ath.cx> wrote:

>In article <3ebd4a27.183305146@news.optonline.net>, Robert Wagner wrote:
>> Mike <Mike@mikee.ath.cx> wrote:
…[20 more quoted lines elided]…
>Mike

Have you heard about BTee/ISAM v3.1 from Softfocus. It might be what
you are looking for. I used the product for some small project. It was
very reliable and compact.

AFAIK, they do not have a web site. Here is an address, if they still
exist...
Softfocus, 1343 Stanbury Rd., Oakville, Ontario, L6L 2J5
Telephone:  (905) 825-0903 
info@softfocus.com

Best regards.

Alain Reymond
```

#### ↳ Re: vsam algorithms?

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-10T23:45:17+03:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<26pqbvkdibuerlvp9ucapq3h2i08hpppcd@4ax.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
On Sat, 10 May 2003 14:34:56 -0000 Mike <Mike@mikee.ath.cx> wrote:

:>I want to implement my own vsam system. Where can I find the algorithms
:>that detail structure of the data, what fields, what blocks, how
:>written, how read, records added and deleted, and such?

Research "Control Interval Processing".
```

#### ↳ Re: vsam algorithms?

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-05-11T22:38:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBF091C.6CD3861F@ix.netcom.com>`
- **References:** `<vbq3gg54g6mdf3@corp.supernews.com>`

```
Mike wrote:
> 
> I want to implement my own vsam system. Where can I find the algorithms
…[3 more quoted lines elided]…
> Mike

I've read the whole set of answers here and in ASM370.

I think what you want is BDAM, or Relative record
processing.

OTOH - If you use xSAM (where x is B or Q), and you have the
understanding of NOTE & POINT, you can build a key
record(s), read that into an incore table and before closing
the data set, write that table back out. This way you can
read direct and re-write the disk data.

HOWEVER, with 100 byte records, your DASD efficiency with
3380/90 type drives will be abysmal.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
