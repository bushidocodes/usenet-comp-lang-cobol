[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CGI Limitations with MicroFocus NetExpress?

_7 messages · 4 participants · 2004-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### CGI Limitations with MicroFocus NetExpress?

- **From:** dick@stillwater-mcmullens.net (Dick McMullen)
- **Date:** 2004-08-08T10:41:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9f9d170.0408080941.28409f56@posting.google.com>`

```
Can anyone point me to specs for MicroFocus's CGI support in
NetExpress?

I am finding a limitation of approximately 4K for ACCEPT verbs against
a CGI page with large textual input fields--not sure where the culprit
is, but I'm sure I should be able to extend that limitation.

I am running Apache on Windows2000, and I am developing the
server-side code using NetExpress.

Thanks.

Dick McMullen
```

#### ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-08-08T13:41:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<knsch094r21mm92h14seqta1o9avphrkqv@4ax.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com>`

```
Are you looking at all the other generated source files?  As I recall
there's two other source files that gets generated when you first
generate a page in your project and complete it.  Are you looking at
those?  I remember pushing a lot of data around in NetExpress, so I'm
not really sure exactly what is going on in your case.

My first thought is that it has a default receipt value in one of
these other files that you are exceeding.  Of course, there's other
possibilities, but if you want to ask any more questions, just reply.

Though I have several references here in hand, I don't know of any
online references or anything that I can point you to.  Sorry.

On 8 Aug 2004 10:41:57 -0700, dick@stillwater-mcmullens.net (Dick
McMullen) wrote:

>Can anyone point me to specs for MicroFocus's CGI support in
>NetExpress?
…[6 more quoted lines elided]…
>server-side code using NetExpress.
```

#### ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-08T20:11:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408081911.6012a462@posting.google.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com>`

```
dick@stillwater-mcmullens.net (Dick McMullen) wrote

> I am finding a limitation of approximately 4K for ACCEPT verbs against
> a CGI page with large textual input fields--not sure where the culprit
…[3 more quoted lines elided]…
> server-side code using NetExpress.

I would assume that you are using POST method as most browsers have a
lower limit than this for GET method - eg IE is limited to total of
2083 in the URL string.

Check your Apache configuration, for example for:

LimitRequestBody 
LimitRequestFields
```

#### ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-08-09T01:34:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<el6eh0tj2skthu0c9hostnph042eh7l5fg@4ax.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com>`

```
Now that I got to look at one of my old projects...

The other poster is right.  Look at whether you are using GET, or POST
as a CGI exec method.  There is a limitation on how many bytes can be
passed under GET method.

Look at your CPF file.  The fields there must match your CPY file.

On 8 Aug 2004 10:41:57 -0700, dick@stillwater-mcmullens.net (Dick
McMullen) wrote:

>Can anyone point me to specs for MicroFocus's CGI support in
>NetExpress?
```

#### ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2004-08-09T10:42:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf7gjg$4uh$1@hyperion.microfocus.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com>`

```
Hi Dick,

Which version (and FixPack level) of Net Express are you running? There was
an issue regarding a 4K limitation of data handled by CGI ACCEPT and DISPLAY
statements in the base release of Net Express 3.1, which was corrected in
the Accept/Display CGI Syntax Fixpack (acc00n31.exe).

If you're running the base release of Net Express 3.1, I would strongly
recommend upgrading to the very latest fix level -- you can download these
from http://supportline.microfocus.com/  .

SimonT.
```

##### ↳ ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** dick@stillwater-mcmullens.net (Dick McMullen)
- **Date:** 2004-08-10T13:48:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9f9d170.0408101248.fe34146@posting.google.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com> <cf7gjg$4uh$1@hyperion.microfocus.com>`

```
All,

1)  I am using POST, not GET, so I believe I am OK there;
2)  Apache reports the appropriate content_length after the POST, but
I will check the Apache config;
3)  The NetExpress 4K limitation sounds like it may be the cause.  I
will also check that.

Thanks to all of you for your ideas.

Dick

"Simon Tobias" <Simon.Tobias@nospam.microfocus.com> wrote in message news:<cf7gjg$4uh$1@hyperion.microfocus.com>...
> Hi Dick,
> 
…[9 more quoted lines elided]…
> SimonT.
```

##### ↳ ↳ Re: CGI Limitations with MicroFocus NetExpress?

- **From:** dick@stillwater-mcmullens.net (Dick McMullen)
- **Date:** 2004-08-10T13:49:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9f9d170.0408101249.79155230@posting.google.com>`
- **References:** `<d9f9d170.0408080941.28409f56@posting.google.com> <cf7gjg$4uh$1@hyperion.microfocus.com>`

```
All,

1)  I am using POST, not GET, so I believe I am OK there;
2)  Apache reports the appropriate content_length after the POST, but
I will check the Apache config;
3)  The NetExpress 4K limitation sounds like it may be the cause.  I
will also check that.

Thanks to all of you for your ideas.

Dick

"Simon Tobias" <Simon.Tobias@nospam.microfocus.com> wrote in message news:<cf7gjg$4uh$1@hyperion.microfocus.com>...
> Hi Dick,
> 
…[9 more quoted lines elided]…
> SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
