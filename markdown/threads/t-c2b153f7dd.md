[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

_6 messages · 5 participants · 1996-02_

---

### Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "broo..." <ua-author-895194@usenetarchives.gap>
- **Date:** 1996-02-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4g5vrn$bif@newsbf02.news.aol.com>`

```
I am working on a project that was developed using the above. Now I am
getting memory full errors from the compiler. This product is no longer
supported by Microsoft and I don't know it's history from there. I don't
have access to the manuals ( client doesn't have them). I need the
manuals, alternate compiler to use ( cheap!, I am really eatting it on
this one.), or any other assistance that might help.

Please email @AOL.COM.BROOKSG34.

Thanks for any help in advance.
```

#### ↳ Re: Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "brooksg" <ua-author-17086721@usenetarchives.gap>
- **Date:** 1996-02-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2b153f7dd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4g5vrn$bif@newsbf02.news.aol.com>`
- **References:** `<4g5vrn$bif@newsbf02.news.aol.com>`

```
bro··.@a··.com (BROOKSG34) wrote:
› I am working on a project that was developed using the above.  Now I am
› getting memory full errors from the compiler.  This product is no longer
…[7 more quoted lines elided]…
› Thanks for any help in advance.


Come to find out client was able to contact the original
programmer and come up with manuals. Now, I know why I am
getting memory full errors. Microsoft COBOL XENIX Release 2.20
has a 64K Data limit. The manuals suggest breaking up into
seperate modules and calling them. I am afraid that I will
still run in to a 64K barrier.

Did Microsoft make a 386 version of this compiler? Did Micro
Focus buy the distribuitions rights? How can I get over this
64K barrier without alot of expense. The customer I am doing
this for want spend any more money, and I personally hate
saying that I will do something then find out I am up against
a brick wall. Any suggestions, help, etc will be greatly
appreciated. New internet address is: bro··.@l··.net
```

##### ↳ ↳ Re: Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-02-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2b153f7dd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2b153f7dd-p2@usenetarchives.gap>`
- **References:** `<4g5vrn$bif@newsbf02.news.aol.com> <gap-c2b153f7dd-p2@usenetarchives.gap>`

```
Hmm, did you consider segmenting the code to overcome the 64K barrier?
Find some early COBOL textbooks in a college library that will explain
the procedure.

If it's possible on your machine and you got the source code, can you
find a Microsoft ver 5 compiler at a PC "roadshow" and upgrade? This
may mean migrating the data to a text file and reload it for direct
processing in the new version.

Hopes this helps,
Boyce Williams
```

###### ↳ ↳ ↳ Re: Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1996-02-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2b153f7dd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2b153f7dd-p3@usenetarchives.gap>`
- **References:** `<4g5vrn$bif@newsbf02.news.aol.com> <gap-c2b153f7dd-p2@usenetarchives.gap> <gap-c2b153f7dd-p3@usenetarchives.gap>`

```
In article <4gaede$b.··.@fre··u.edu>, bow··.@gem··u.edu says...
› 
› [snip]
…[3 more quoted lines elided]…
› processing in the new version.

Boyce:

MS COBOL version 3 through 5 was licensed from Micro Focus and will probably
compile the source, but if he wants to continue running on XENIX, he's going
to have to get a XENIX version of the compiler from Micro Focus. To my
knowledge, Microsoft never sold a XENIX version of COBOL after dropping
support for their 2.n version.

Microsoft/Micro Focus folks.... please correct me if I'm wrong.

Bob Wolfe
rtw··.@fle··s.com
```

##### ↳ ↳ Re: Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1996-02-19T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2b153f7dd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2b153f7dd-p2@usenetarchives.gap>`
- **References:** `<4g5vrn$bif@newsbf02.news.aol.com> <gap-c2b153f7dd-p2@usenetarchives.gap>`

```
In article <4g8ac0$7.··.@l··.net>, bro··.@l··.net says...

[snip]

› Did Microsoft make a 386 version of this compiler?  Did Micro 
› Focus buy the distribuitions rights?  How can I get over this 
…[4 more quoted lines elided]…
› appreciated.  New internet address is: bro··.@l··.net

Microsoft dropped support for Microsoft COBOL for XENIX and never released a
386 XENIX version. Their customers who wanted a 386 XENIX version were
referred to Micro Focus. The old version 2.n Microsoft compiler is not
the same as the Micro Focus version. Later versions of Microsoft COBOL
(version 3.n & above) were indeed licensed from Micro Focus.

I think that Micro Focus COBOL for XENIX may contain some Microsoft version
2.n compatibility switches, but you'll have to check with our buddies at
Micro Focus to verify that.

Good luck!

Bob Wolfe
rtw··.@fle··s.com
```

###### ↳ ↳ ↳ Re: Microsoft COBOL XENIX Release 2.20 ( 286 Jan '87)

- **From:** "bro..." <ua-author-17086806@usenetarchives.gap>
- **Date:** 1996-02-20T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2b153f7dd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2b153f7dd-p5@usenetarchives.gap>`
- **References:** `<4g5vrn$bif@newsbf02.news.aol.com> <gap-c2b153f7dd-p2@usenetarchives.gap> <gap-c2b153f7dd-p5@usenetarchives.gap>`

```
rtw··.@fle··s.com (Bob Wolfe) wrote:

› In article <4g8ac0$7.··.@l··.net>, bro··.@l··.net says...
 
› [snip]
 
›› Did Microsoft make a 386 version of this compiler?  Did Micro 
›› Focus buy the distribuitions rights?  How can I get over this 
…[4 more quoted lines elided]…
›› appreciated.  New internet address is: bro··.@l··.net
 
› Microsoft dropped support for Microsoft COBOL for XENIX and never released a 
› 386 XENIX version.  Their customers who wanted a 386 XENIX version were 
› referred to Micro Focus.  The old version 2.n Microsoft compiler is not 
› the same as the Micro Focus version.  Later versions of Microsoft COBOL 
› (version 3.n & above) were indeed licensed from Micro Focus.
 
› I think that Micro Focus COBOL for XENIX may contain some Microsoft version 
› 2.n compatibility switches, but you'll have to check with our buddies at 
› Micro Focus to verify that.
 
› Good luck!
 
› Bob Wolfe
› rtw··.@fle··s.com

Thanks everyone for the help. It appears that I need to contact Micro
Focus for pricing ( client will not want to spend money and will be
disappointed ). This has been a great learning experience for me.
When I first saw this application I thought this would be a great
application for Client/Server. But it was hard to justify to customer
that they needed to buy 5 PC's @ $1000.00 each when they are
supporting 5 users off of 1 PC and 4 dumb terminals now. I think I am
still bias to UNIX because of this, although I work with Windows and
NT 7 days a week.

Thanks again.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
