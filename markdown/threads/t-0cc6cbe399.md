[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOLScript

_4 messages · 2 participants · 2003-04_

---

### COBOLScript

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-25T21:52:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA9F472.2000409@Knology.net>`

```
Has anyone here ever used COBOLScript?
```

#### ↳ Re: COBOLScript

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-25T22:49:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304252149.31004d40@posting.google.com>`
- **References:** `<3EA9F472.2000409@Knology.net>`

```
LX-i <DanielJS@Knology.net> wrote 

> Has anyone here ever used COBOLScript?

Yes. I bought a copy for Linux and use it to prototype SQL stuff.  It
is not  Cobol but near enough to be useful.  Unfortunately it can't do
CALL/CANCEL of another CobolScript program so COPY is the only way to
build programs from standard parts.

But for simple scripting that looks like Cobol its OK.  Get the
professional for SQL, its cheap.

Oh yeah, it _requires_ full stops on every simple statement.
```

##### ↳ ↳ Re: COBOLScript

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-26T12:57:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EAAC870.7030505@Knology.net>`
- **References:** `<3EA9F472.2000409@Knology.net> <217e491a.0304252149.31004d40@posting.google.com>`

```
Richard wrote:
> LX-i <DanielJS@Knology.net> wrote 
> 
…[7 more quoted lines elided]…
> build programs from standard parts.

Well, with the other web scripting languages I've used, we pretty much 
had one "include" file that had our common functions in it, so Copy 
sounds like it would do pretty much the same thing.

> But for simple scripting that looks like Cobol its OK.  Get the
> professional for SQL, its cheap.

Someone suggested it as a way for us to utilize the COBOL coders' 
knowledge base, while writing web-based applications.  I looked into it, 
and as someone who already knows VBScript (ASP) and PHP, it looked like 
a lot of extra typing.  (Of course, comparatively, COBOL generally -is- 
a lot more typing that those other languages...)

Does it support SQL through ODBC, or are there native libraries for 
different databases?

> Oh yeah, it _requires_ full stops on every simple statement.

Did you notice how well it performed?  Did the site you built get 
stressed that much?  I'm curious as to its performance as compared with 
other languages.
```

###### ↳ ↳ ↳ Re: COBOLScript

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-26T15:35:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304261435.660c5bd2@posting.google.com>`
- **References:** `<3EA9F472.2000409@Knology.net> <217e491a.0304252149.31004d40@posting.google.com> <3EAAC870.7030505@Knology.net>`

```
LX-i <DanielJS@Knology.net> wrote 

> Well, with the other web scripting languages I've used, we pretty much 
> had one "include" file that had our common functions in it, so Copy 
> sounds like it would do pretty much the same thing.

It may be OK for some things but I use Python for my main scripting
and like the dynamic loading.

> Someone suggested it as a way for us to utilize the COBOL coders' 
> knowledge base, while writing web-based applications. 

Normal Cobol is easy to use for CGI, though obviously there is a bit
(quite a bit) needed to write the support routines - once, which are
then CALLed for whatever application is required.

> Does it support SQL through ODBC, or are there native libraries for 
> different databases?

ODBC.  It works fine with unixODBC to PostgreSQL and MySQL, I see no
reason why it can't be used with others.

> Did you notice how well it performed?  Did the site you built get 
> stressed that much?  I'm curious as to its performance as compared with 
> other languages.

I haven't used CobolScript for CGI, except as simple tests to see that
it does work.  My live sites are in MF Cobol and Python.  My CGI code
also can run in Fujitsu Cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
