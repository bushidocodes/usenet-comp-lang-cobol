[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Capturing HTML documents with NetExpress / CGI

_4 messages · 4 participants · 1998-05_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Capturing HTML documents with NetExpress / CGI

- **From:** "rg..." <ua-author-17084447@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3565ba74.10813593@news.global-one.at>`

```

Hi!

IÂ´m using NetExpress 2.0 for developing CGI programs running on
Microsoft Internet Information Server 4.0.

Question:

How can I "capture" a single HTML document - located on another
companyÂ´s server - and store it in a local file? This file must be
located on my web server.

Or is there another way to "cut out" certain strings from a HTML
document located on a remote server and "paste" it into my own
dynamically created HTML document?

The creation of my own dynamic HTML document is not the problem.

Any help would be appreciated - please reply with email to:

RG··.@nue··g.at

Thanks in advance,

R. Graf
```

#### ↳ Re: Capturing HTML documents with NetExpress / CGI

- **From:** "stephen gennard" <ua-author-6589616@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9deda8669d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3565ba74.10813593@news.global-one.at>`
- **References:** `<3565ba74.10813593@news.global-one.at>`

```

Hi,

If you need a command line tool for downloading file from web
servers, I know of two programs:
1 - w3c from http://www.w3c.org/ComLine/
to use: "w3c http://www.mfltd.co.uk -o newfile"

2 - lynx from http://www.fdisk.com/doslynx/lynxport.htm
to use: "lynx -source http://www.mfltd.co.uk >newfile"

Or if you want to use APIs from you application:
1 - use the generic APIs from http://www.w3c.org/LibWWW
2 - or use Microsoft own APIs (see HttpOpenRequest) in your
sdk documentation

Hope this helps..

Stephen

RÃ¼diger Graf wrote:
› 
› Hi!
…[9 more quoted lines elided]…
› see above
 
› Or is there another way to "cut out" certain strings from a HTML
› document located on a remote server and "paste" it into my own
…[10 more quoted lines elided]…
› R. Graf
```

##### ↳ ↳ Re: Capturing HTML documents with NetExpress / CGI

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9deda8669d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9deda8669d-p2@usenetarchives.gap>`
- **References:** `<3565ba74.10813593@news.global-one.at> <gap-9deda8669d-p2@usenetarchives.gap>`

```


›› How can I "capture" a single HTML document - located on another
›› companyï¿½s server - and store it in a local file? This file must be
›› located on my web server.


If you are using MSIE, go to the page, click View, then click Source,
then File, then Save As.
```

###### ↳ ↳ ↳ Re: Capturing HTML documents with NetExpress / CGI

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9deda8669d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9deda8669d-p3@usenetarchives.gap>`
- **References:** `<3565ba74.10813593@news.global-one.at> <gap-9deda8669d-p2@usenetarchives.gap> <gap-9deda8669d-p3@usenetarchives.gap>`

```

le··.@i··.net wrote:
› 
››› How can I "capture" a single HTML document - located on another
…[4 more quoted lines elided]…
› then File, then Save As.

Same deal for Netscape Comm... 4.05.

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
