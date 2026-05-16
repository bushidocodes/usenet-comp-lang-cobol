[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting MF Cobol pgms for international use

_4 messages · 4 participants · 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Converting MF Cobol pgms for international use

- **From:** jrinere@mindspring.com
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<880v3g$3c7$1@nnrp1.deja.com>`

```
We are starting down the road of converting 400+ MFCobol pgms to be
used in other languages.  The good news is that these are all batch
programs (reports), nothing interactive.  The bad news is that they
weren't designed/written with this in mind.

My current working idea is to implement a compile time solution by
isolating all headings, labels, literals, etc to working storage and
creating a copybook.  We would then create a copybook for each language
to be supported.  By altering the appropriate path's at compile time
and runtime, the correct binary will be compiled/executed.

The difficulty I'm facing now is how to provide a tool to non
programmers to do the translations to the copybooks.  They can't edit
them directly as they will have no concept of syntax, etc.  I'm
thinking about creating some kind of app that will display the English
language text and allow entry of the foreign text.

Anybody have any similar experience?  I would appreciate any
suggestions or comments.  This is not pretty but has to be done.

Thanx for any and all help.

Runtime environment: Microfocus Cobol/HP-UX.
Development: MF Netexpress/Windows NT.
The folks doing the translation will be Windows NT users.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Converting MF Cobol pgms for international use

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<881d2o$8ip$1@news.cerf.net>`
- **References:** `<880v3g$3c7$1@nnrp1.deja.com>`

```
<jrinere@mindspring.com> wrote in message
news:880v3g$3c7$1@nnrp1.deja.com...
> We are starting down the road of converting 400+ MFCobol pgms to be
> used in other languages.  The good news is that these are all batch
> ..
> Anybody have any similar experience?  I would appreciate any
> suggestions or comments.  This is not pretty but has to be done.

It would certainly help if you provided some sample of what your copy books
look like.

Cheesle
```

##### ↳ ↳ Re: Converting MF Cobol pgms for international use

- **From:** jrinere@my-deja.com
- **Date:** 2000-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<888r29$chh$1@nnrp1.deja.com>`
- **References:** `<880v3g$3c7$1@nnrp1.deja.com> <881d2o$8ip$1@news.cerf.net>`

```
Thanx for the reply.....

The copybooks would be pretty typical stuff, but since they've been
developed over a number of years by a number of programmers, they are
not consistent.

A simplified example of a heading layout might be:

01  heading-line-1.
    03  filler                   pic x(08)    value "Customer".
    03  filler                   pic x(18)    value spaces.
    03  filler                   pic x(07)    value "Address".
    03  filler                   pic x(19)    value spaces.
    03  filler                   pic x(05)    value "Phone".

01  heading-line-2.
    03  filler                   pic x(04)    value "Name".
    03  filler                   pic x(48)    value spaces.
    03  filler                   pic x(06)    value "Number".

But it may also be coded:

01  heading-line-1.
    03  filler                   pic x(08)
    value "Customer".
    03  filler                   pic x(18)
    value spaces.
    03  filler                   pic x(07)
    value "Address".
    03  filler                   pic x(19)
    value spaces.
    03  filler                   pic x(05)
    value "Phone".

01  heading-line-2.
    03  filler                   pic x(04)
    value "Name".
    03  filler                   pic x(48)
    value spaces.
    03  filler                   pic x(06)
    value "Number".

And a couple of folks thought this was clever:

01  heading-line-1.
    03  filler                   pic x(10)    value "Customer  ".
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value "     Addre".
    03  filler                   pic x(10)    value "ss        "
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value " Phone    ".

01  heading-line-2.
    03  filler                   pic x(10)    value "Name      ".
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value spaces.
    03  filler                   pic x(10)    value " Number   ".

(No, I'm not kidding!)

In addition, you might have subtotal lines:

01  subtotal-line-1.
    03  subtotal-lit             pic x(25).
    ...
and the associated literals:

01  literals.
    03  ws-customer-subtot-lit   pic x(25)
    value "Total for customer:".
    03  ws-style-subtot-lit   pic x(25)
    value "Total for style:".
    03  ws-color-subtot-lit   pic x(25)
    value "Total for color:".


In article <881d2o$8ip$1@news.cerf.net>,
  "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
> <jrinere@mindspring.com> wrote in message
> news:880v3g$3c7$1@nnrp1.deja.com...
…[6 more quoted lines elided]…
> It would certainly help if you provided some sample of what your copy
books
> look like.
>
> Cheesle
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Converting MF Cobol pgms for international use

- **From:** "Stephen Thomas" <talkingcats@gobble.clara.co.uk>
- **Date:** 2000-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34lp4.8261$uc.177644@nnrp4.clara.net>`
- **References:** `<880v3g$3c7$1@nnrp1.deja.com>`

```
jrinere@mindspring.com wrote in message <880v3g$3c7$1@nnrp1.deja.com>...
>We are starting down the road of converting 400+ MFCobol pgms to be
>used in other languages.  The good news is that these are all batch
…[27 more quoted lines elided]…
>Before you buy.
I developed and supported a large sales order entry system that ran in
France, Germany, Spain & UK, with screen handling and reporting in the
appropriate languages.  It was written in MF COBOL and Dialog System.  If
you want more information, please email directly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
