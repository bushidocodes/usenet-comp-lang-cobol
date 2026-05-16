[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACUCOBOL HELP: OCX Registry is Crashed-Please Reinstall OCX

_4 messages · 3 participants · 2000-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### ACUCOBOL HELP: OCX Registry is Crashed-Please Reinstall OCX

- **From:** "Jonathan Laub" <laubj@lakesoft.net>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jt5hu$1a3o$1@shadow.skypoint.net>`

```
Help!

What .dll must I re-register in order to make OCX viable again??  Also, what
causes this???

Thanks In Advance

Jonathan
laubj@lakesoft.net
```

#### ↳ Re: ACUCOBOL HELP: OCX Registry is Crashed-Please Reinstall OCX

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39622c76.166163566@207.126.101.100>`
- **References:** `<8jt5hu$1a3o$1@shadow.skypoint.net>`

```
I'm not an AcuCOBOL user ... but... Normally you have to register the
activeX itself, including any dependancies -- oft times in reverse
order, dependancies first then the control.

What causes the loss of registration?  I do not know, I have never
experienced it.


On Tue, 4 Jul 2000 12:05:51 -0500, "Jonathan Laub"
<laubj@lakesoft.net> wrote:

>Help!
>
…[8 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: ACUCOBOL HELP: OCX Registry is Crashed-Please Reinstall OCX

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lBkC6qAldmY5IwB6@rcav8r.demon.co.uk>`
- **References:** `<8jt5hu$1a3o$1@shadow.skypoint.net>`

```
In article <8jt5hu$1a3o$1@shadow.skypoint.net>, Jonathan Laub 
<laubj@lakesoft.net> writes
>Help!
>
…[9 more quoted lines elided]…
>

Jonathan,

If you're getting this message from AcuBench version 4.x then you can 
try running 'initocxs.bat'. This can be found in (by default) 
C:\ACUCBL43\ACUSP.

I've seen this problem once, but I can't remember at present what the 
cause was.

If this doesn't solve your problem, or if you need more information then 
I'd recommend contacting your local support office. Alternatively please 
feel free to email me at <neaton@acucorp.com> and I'll do my best to 
help.

Best regards

Nigel
```

##### ↳ ↳ Re: ACUCOBOL HELP: OCX Registry is Crashed-Please Reinstall OCX

- **From:** "Jonathan Laub" <laubj@lakesoft.net>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kx395.3254$iN5.804505@ptah.visi.com>`
- **References:** `<8jt5hu$1a3o$1@shadow.skypoint.net> <lBkC6qAldmY5IwB6@rcav8r.demon.co.uk>`

```
Now I really feel like a "duh"!

Acucobol is "user profile" aware.  Being on a notebook I work with several
profiles.  Each profile has its own OCX settings... need I say more.  For
each profile I use, had to re-install to get those profile settings created.

Thanks Anyway

Jonathan

Nigel Eaton <nigele@rcav8r.demon.co.uk> wrote in message
news:lBkC6qAldmY5IwB6@rcav8r.demon.co.uk...
> In article <8jt5hu$1a3o$1@shadow.skypoint.net>, Jonathan Laub
> <laubj@lakesoft.net> writes
…[36 more quoted lines elided]…
> Views expressed do not necessarily reflect the views of Acucorp
Inc(especially the bit about otters)
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
