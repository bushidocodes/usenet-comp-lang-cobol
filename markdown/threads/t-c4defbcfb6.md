[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TinyCobol and OpenCobol

_18 messages · 12 participants · 2002-12 → 2003-01_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### TinyCobol and OpenCobol

- **From:** "Vince Coen" <Vince_Coen@f609.n257.z2.fidonet.org>
- **Date:** 2002-12-31T21:16:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1041367537@f609.n257.z2.fidonet.ftn>`

```
Hello All!

Has anyone installed these products on Mandrake v9.0?

If so, How?


Vince
```

#### ↳ Re: TinyCobol and OpenCobol

- **From:** Billy O'Connor <billyoc@linuxfromscratch.org>
- **Date:** 2003-01-01T03:53:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81k7hpiw9y.fsf@dps10.oconnoronline.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn>`

```
"Vince Coen" <Vince_Coen@f609.n257.z2.fidonet.org> writes:

> Hello All!
> 
> Has anyone installed these products on Mandrake v9.0?
> 
> If so, How?

tinyCOBOL
Prerequistes are db-4.0.14.

http://umn.dl.sourceforge.net/sourceforge/tiny-cobol/tinycobol-0.59.tar.gz

You'll need the gcc rpms installed, gcc-cpp-3.2-1mdk, gcc-3.2-1mdk and
libgcc1-3.2-1mdk.  Note that there may be glibc-devel dependencies
here, the urpmi utility will detail them if so.

Extract the tarball, and run:
./configure --prefix=/usr &&
make &&
make install


OpenCOBOL
Prerequisites are gmp(The GNU Multi-precision library)
http://twtelecom.dl.sourceforge.net/sourceforge/open-cobol/open-cobol-0.10.tar.gz
building is the same as tinyCOBOL.

Enjoy!
```

#### ↳ Re: TinyCobol and OpenCobol

- **From:** CJ <exspecto2000@yahoo.com>
- **Date:** 2003-01-04T01:59:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QdrR9.549830$WL3.146824@rwcrnsc54>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn>`

```
good luck trying to compile from source.
your best best is to install db using the binary packages. tiny should 
comiple nicely after that.

Vince Coen wrote:

> Hello All!
> 
…[5 more quoted lines elided]…
> Vince
```

##### ↳ ↳ Re: TinyCobol and OpenCobol

- **From:** Billy O'Connor <billyoc@linuxfromscratch.org>
- **Date:** 2003-01-04T03:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81fzs9n826.fsf@dps10.oconnoronline.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54>`

```
CJ <exspecto2000@yahoo.com> writes:

> good luck trying to compile from source.
> your best best is to install db using the binary packages. tiny should 
> comiple nicely after that.

Try not to top post.  Are you saying not to install the Berkeley DB
from sources?  Or tinyCOBOL?
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2003-01-03T22:55:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<av5pgk$lrj$1@slb4.atl.mindspring.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net>`

```
Try not to require others to "bottom-post" as it is often more difficult for
many of us to see what is new in a post.

If you want to make it more difficult for those with "decent" thread viewing
newsgroup readers to read your posts, that's fine - but please don't suggest
it to others who create easier to read responses.
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-04T08:30:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v56dnZ1S7K6jbYujXTWckA@giganews.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com>

A. Top posting.

Q. What's the biggest irritant in newsgoups?
```

###### ↳ ↳ ↳ Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2003-01-04T13:11:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<av7bkj$fq9$1@slb9.atl.mindspring.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com>`

```
Q: What annoys people who have a "decent" thread reader for NG's?

A: Having to read thru a lot of "quoted material" before getting to the new
part in each reply.
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-01-04T21:22:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rgIR9.46891$an1.1773340@twister.austin.rr.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net>`

```
Amen!
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:av7bkj$fq9$1@slb9.atl.mindspring.net...
> Q: What annoys people who have a "decent" thread reader for NG's?
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 6)_

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2003-01-04T21:33:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.BA3D038C059EF6AD1849E120@news-east.usenetserver.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net>`

```
"JerryMouse" <nospam@bisusa.com> wrote
> A. Top posting.
>
> Q. What's the biggest irritant in newsgoups?

I'd say excess quoted material. Top-posting is just a special case. If 
the entire previous text is present, it's an irritant, top or bottom. 
If anything, bottom-posting without trimming the quote is worse than 
top-posting. Heresy, I know.

Edward
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@NOSPAM.neo.rr.com>
- **Date:** 2003-01-05T11:32:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A59148D61DE050A1.F6A0B351DCB81108.EDD7154F1E225F8A@lp.airnews.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net>`

```
On Sat, 4 Jan 2003 13:11:04 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> enlightened us:

>Q: What annoys people who have a "decent" thread reader for NG's?
>
>A: Having to read thru a lot of "quoted material" before getting to the new
>part in each reply.

Ever hear of CTRL + END?


          ////
         (o o)
-oOO--(_)--OOo-

Real Signs:

Hotel elevator, Paris:  

PLEASE LEAVE YOUR VALUES AT THE FRONT DESK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 7)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-01-05T17:21:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vQZR9.4$Bt3.973952@newssvr15.news.prodigy.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net> <A59148D61DE050A1.F6A0B351DCB81108.EDD7154F1E225F8A@lp.airnews.net>`

```
No keystrokes at all is 1 fewer than 1 keystroke.
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 8)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-01-06T07:59:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0301060759.2c8b4046@posting.google.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net> <A59148D61DE050A1.F6A0B351DCB81108.EDD7154F1E225F8A@lp.airnews.net> <vQZR9.4$Bt3.973952@newssvr15.news.prodigy.com>`

```
I am really finding it hard to believe that ya'll are


"Terry Heinze" <terryheinze@prodigy.net> wrote in message news:<vQZR9.4$Bt3.973952@newssvr15.news.prodigy.com>...
> No keystrokes at all is 1 fewer than 1 keystroke.


actually fighting about top or bottom posting.
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-06T16:14:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avca22$jqi$1@peabody.colorado.edu>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net> <A59148D61DE050A1.F6A0B351DCB81108.EDD7154F1E225F8A@lp.airnews.net> <vQZR9.4$Bt3.973952@newssvr15.news.prodigy.com> <dcedb8d0.0301060759.2c8b4046@posting.google.com>`

```

On  6-Jan-2003, jzitzelb@tsys.com (Joe Zitzelberger) wrote:

> I am really finding it hard to believe that ya'll are
>
…[6 more quoted lines elided]…
> actually fighting about top or bottom posting.

It's like some programming styles.   There are some good reasons for going for a
particular style - but people often forget the reasons and don't allow
exceptions - it is the style that becomes all important, not the results.

This isn't limited to programming - business is full of decisions made for
reasons of style.
```

###### ↳ ↳ ↳ Re: Top-/Bottom-Posting (was: TinyCobol and OpenCobol

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-06T14:58:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avc5hv$h65$1@peabody.colorado.edu>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com> <av7bkj$fq9$1@slb9.atl.mindspring.net> <A59148D61DE050A1.F6A0B351DCB81108.EDD7154F1E225F8A@lp.airnews.net>`

```

On  5-Jan-2003, SkippyPB <swiegand@NOSPAM.neo.rr.com> wrote:

> >A: Having to read thru a lot of "quoted material" before getting to the new
> >part in each reply.
>
> Ever hear of CTRL + END?

How do you know that there isn't message half way through?  Most people browse
with a finger on a key or mouse to do common functions, only moving their hands
to type a reply.

If you care about what you're communicating - review your format and make it
easy for whomever is browsing through to get to what you are trying to
communicate.  (and edit your reply)
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-04T12:59:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301041259.7dfc0473@posting.google.com>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> A. Top posting.
> 
> Q. What's the biggest irritant in newsgoups?

No. The biggest irritant is people arguing about 'top posting'.  I am 
adaptable, I don't care either way.
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-06T14:55:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avc5cp$gvk$1@peabody.colorado.edu>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <av5pgk$lrj$1@slb4.atl.mindspring.net> <v56dnZ1S7K6jbYujXTWckA@giganews.com>`

```

On  4-Jan-2003, "JerryMouse" <nospam@bisusa.com> wrote:


> Q. What's the biggest irritant in newsgoups?
>
> A. Top posting.


Posting according to some old standard instead of reading and editing the post
to facilitate communication.  Sometimes top posting communicates best and most
quickly, sometimes bottom posting, sometimes mid-posting.

If you have a reason to make a long post - PLEASE top post so that people don't
have to page down to find out what new was added.  Otherwise, lots of people
will just skip over your post.

If you are going to add a one-line reply to a one-line reply - edit the messages
to make it obvious to which you are replying to.
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

- **From:** CJ <exspecto2000@yahoo.com>
- **Date:** 2003-01-08T16:46:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MBYS9.611134$%m4.195752@rwcrnsc52.ops.asp.att.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net>`

```
wasn't try to "top post" lol. i reply to the thread which concerns me. as 
far as compiling from source and the difficulty therein, i was referring to 
the db sources. they were difficult to compile (on my machine anyways), and 
even if i could get a newer db version to compile, tiny wouldnt recognize 
it as usable.

Billy O'Connor wrote:

> CJ <exspecto2000@yahoo.com> writes:
> 
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: TinyCobol and OpenCobol

_(reply depth: 4)_

- **From:** Billy O'Connor <billyoc@linuxfromscratch.org>
- **Date:** 2003-01-08T17:59:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<818yxvfrqj.fsf@dps10.oconnoronline.net>`
- **References:** `<1041367537@f609.n257.z2.fidonet.ftn> <QdrR9.549830$WL3.146824@rwcrnsc54> <81fzs9n826.fsf@dps10.oconnoronline.net> <MBYS9.611134$%m4.195752@rwcrnsc52.ops.asp.att.net>`

```
CJ <exspecto2000@yahoo.com> writes:

> wasn't try to "top post" lol. i reply to the thread which concerns me. as 
> far as compiling from source and the difficulty therein, i was referring to 
…[3 more quoted lines elided]…
> 

What ./configure options did you use to compile Berkeley DB?  
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
