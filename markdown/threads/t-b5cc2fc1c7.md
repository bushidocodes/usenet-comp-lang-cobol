[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic Allocation of files in an IBM Environment

_6 messages · 6 participants · 2005-09_

---

### Dynamic Allocation of files in an IBM Environment

- **From:** "Giulio Belrango" <giuliobelrango@rogers.com>
- **Date:** 2005-09-20T20:55:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
 
Does anyone know how to allocate DD statements or DSN=? within a COBOL 
program without using JCL.

Thanks...
```

#### ↳ Re: Dynamic Allocation of files in an IBM Environment

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2005-09-20T19:17:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W-KdnaNVaKE0X63eRVn-iw@adelphia.com>`
- **In-Reply-To:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`
- **References:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
Giulio Belrango wrote:

> 
>Does anyone know how to allocate DD statements or DSN=? within a COBOL 
…[5 more quoted lines elided]…
>
In my former shop, we used an Assembler Language subroutine to manage 
dynamic allocation.  The calling program would pass the information 
(DDname and DSName), the subroutine would call the operating system's 
dynamic allocation service (SVC 99), and the calling program could then 
open, process, and close the file.

COBOL has an option, CBLQDA, which allows or prohibits dynamic 
allocation depending on the setting of the option at run time.  However, 
it is extremely simple minded, and does not allow specifying a data set 
name.  It essentially allows creation of a temporary data set, which is 
deleted at the end of the run unit.

The Assembler Language subroutine is not very difficult to code.  I am 
now retired, but I might have a copy of the code, since I was the author.
```

#### ↳ Re: Dynamic Allocation of files in an IBM Environment

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-21T02:35:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9G3Ye.167446$AI1.51366@fe02.news.easynews.com>`
- **References:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
Assuming you are using a currently supported COBOL compiler, then you can  use 
(set and use) an "environment variable" to dynamically allocate files in COBOL. 
(Unlike CBLQDA, this allows for creating NEW files that are catalogued *and* 
accessing already catalogued files).

See among other references:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg30/1.9.4.1

  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg30/1.8.3

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr30/4.2.3.1

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg30/3.4.2.3
   shows how to set an environment variable, while

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr30/4.2.3.4
    and
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr30/4.2.3.2
  show what to put in the environment variables (for dynamic file allocations)
```

#### ↳ Re: Dynamic Allocation of files in an IBM Environment

- **From:** "news-server.tampabay.rr.com" <defaultuser@hotmail.com>
- **Date:** 2005-09-21T06:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b07Ye.101216$p_1.63029@tornado.tampabay.rr.com>`
- **References:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
BPXWDYN

"Giulio Belrango" <giuliobelrango@rogers.com> wrote in message 
news:o-SdnZr3M9YyMq3eRVn-iw@rogers.com...
>
> Does anyone know how to allocate DD statements or DSN=? within a COBOL 
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Dynamic Allocation of files in an IBM Environment

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-09-21T18:22:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<324a9$4331dd26$4f9c6d4$32372@DIALUPUSA.NET>`
- **References:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
Go to google groups and search comp.lang.cobol for "dynamic allocation". 
Several different methods have been posted in the past.

<top post - no more follows>

"Giulio Belrango" <giuliobelrango@rogers.com> wrote in message 
news:o-SdnZr3M9YyMq3eRVn-iw@rogers.com...
>
> Does anyone know how to allocate DD statements or DSN=? within a COBOL 
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Dynamic Allocation of files in an IBM Environment

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-09-22T23:29:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-963978.23294022092005@ispnews.usenetserver.com>`
- **References:** `<o-SdnZr3M9YyMq3eRVn-iw@rogers.com>`

```
In article <o-SdnZr3M9YyMq3eRVn-iw@rogers.com>,
 "Giulio Belrango" <giuliobelrango@rogers.com> wrote:

>  
> Does anyone know how to allocate DD statements or DSN=? within a COBOL 
> program without using JCL.
> 
> Thanks... 

On current versions of the Cobol compiler, you can invoke TSO services 
and pass a rexx/clist/tso style "allocate" command.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
