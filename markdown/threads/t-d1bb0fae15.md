[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# print a rectangle

_7 messages · 4 participants · 2000-05 → 2000-06_

---

### print a rectangle

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-05-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h3kgq$26s$1@duke.telepac.pt>`

```
I need help printing a rectangle using Micro Focus 4.0 and Dialog.  What I
want to do is make a rectangle for example around the invoice number.  I
appreciate any help anyone can provide me.
```

#### ↳ Re: print a rectangle

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h62i1$cpt$1@news.cerf.net>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt>`

```
"Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
news:8h3kgq$26s$1@duke.telepac.pt...
> I need help printing a rectangle using Micro Focus 4.0 and Dialog.  What I
> want to do is make a rectangle for example around the invoice number.  I
> appreciate any help anyone can provide me.

I don't know what built in functions Micro Focus might have. But if you are
targeting a Windows App. The Windows API has the function Rectangle, look it
up in the MSDN (http://search.microsoft.com/us/SearchMS.asp)

Cheesle
```

##### ↳ ↳ Re: print a rectangle

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h69t8$bf8$1@duke.telepac.pt>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt> <8h62i1$cpt$1@news.cerf.net>`

```
YEs but i have some dificult to understand the language used i think that it
is a C language, I only know Cobol and i want to know the calls i must do to
make a rectangle.
I know the instructions to make the rectangle but nothinh happens , and it
is necessary to make a brush or a solid brush before and i don�t know how
can i do it in Cobol.

Thanks Raimundo Carvalho
Cheesle <cheesle@online.NoSpamPlease.no> wrote in message
news:8h62i1$cpt$1@news.cerf.net...
> "Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
> news:8h3kgq$26s$1@duke.telepac.pt...
> > I need help printing a rectangle using Micro Focus 4.0 and Dialog.  What
I
> > want to do is make a rectangle for example around the invoice number.  I
> > appreciate any help anyone can provide me.
>
> I don't know what built in functions Micro Focus might have. But if you
are
> targeting a Windows App. The Windows API has the function Rectangle, look
it
> up in the MSDN (http://search.microsoft.com/us/SearchMS.asp)
>
> Cheesle
>
>
```

###### ↳ ↳ ↳ Re: print a rectangle

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h8k2o$i1p$1@news.cerf.net>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt> <8h62i1$cpt$1@news.cerf.net> <8h69t8$bf8$1@duke.telepac.pt>`

```
"Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
news:8h69t8$bf8$1@duke.telepac.pt...
> YEs but i have some dificult to understand the language used i think that
it
> is a C language, I only know Cobol and i want to know the calls i must do
to
> make a rectangle.
> I know the instructions to make the rectangle but nothinh happens , and it
> is necessary to make a brush or a solid brush before and i don�t know how
> can i do it in Cobol.

It is most certainly written in C, and yes I agree, C can sometimes be
difficult to understand. Then again, how to translate C definitions and code
to Cobol depends heavily on you Cobol dialect. If I recall correctly, you
are using MicroFocus, which I unfortunately don't know. You would need
someone that knows MicroFocus Cobol to help you there. However, what I would
recommend is to try to find a complete C sample that shows how to draw a
rectangle (pretty sure there is some on MSDN), then try to translate this
one step by step into Cobol. Once you overcome the few basic differences
this is usually trivial. The most common trap people go into when dealing
with this is that C usually passes parameters by address rather than value.
Also pay attention to the call convention of the functions used. As of
WinAPI, this usually is pascal (WINAPI).

When this is said, I want to warn you a bit, doing gui at this level is
difficult, and there are a lot of stuff to do, and in a particular order.

Sorry I can't help you more.

Cheesle
```

###### ↳ ↳ ↳ Re: print a rectangle

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3937fd6f.150215479@news.cox-internet.com>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt> <8h62i1$cpt$1@news.cerf.net> <8h69t8$bf8$1@duke.telepac.pt> <8h8k2o$i1p$1@news.cerf.net>`

```
On Fri, 2 Jun 2000 08:36:25 -0700, "Cheesle"
<cheesle@online.NoSpamPlease.no> wrote:

>It is most certainly written in C, and yes I agree, C can sometimes be
>difficult to understand. Then again, how to translate C definitions and code
>to Cobol depends heavily on you Cobol dialect. 

Heheh... it's not C I have a problem with.  It's the MS API.  Just
recently I found an example that listed a return code literal value
(They are fond of DEFs) that WAS NOT IN THE HEADER FILES.  Anywhere.
And this from a fairly common API reference:

INVALID_SET_FILE_POINTER

As documented: 
http://msdn.microsoft.com/library/psdk/winbase/filesio_8iwi.htm

I run into things like this all the time.  It's not C - it's
Microsoft.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: print a rectangle

_(reply depth: 5)_

- **From:** "Greg Condon" <nospam@me.thanks>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Om2%4.31093$t8.514269@news.bc.tac.net>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt> <8h62i1$cpt$1@news.cerf.net> <8h69t8$bf8$1@duke.telepac.pt> <8h8k2o$i1p$1@news.cerf.net> <3937fd6f.150215479@news.cox-internet.com>`

```
Hi Thane -

Save yourself a lot of grief and download the latest "Microsoft Platform
SDK".  At a minimum you get all the include files and a bunch of other
stuff.  The total install size I have is 84MB but you can probably get it
down from there.

Here's where the definition lives - in Winbase.h.  Here's a snippet from the
file...

    #define INVALID_HANDLE_VALUE ((HANDLE)-1)
    #define INVALID_FILE_SIZE ((DWORD)0xFFFFFFFF)
    #define INVALID_SET_FILE_POINTER ((DWORD)-1)


Regards,

Greg Condon
[doing lots of Win32 programming from MF 4.0.38     "and loving it..."
:^)    ]


"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3937fd6f.150215479@news.cox-internet.com...
> On Fri, 2 Jun 2000 08:36:25 -0700, "Cheesle"
> <cheesle@online.NoSpamPlease.no> wrote:
>
> >It is most certainly written in C, and yes I agree, C can sometimes be
> >difficult to understand. Then again, how to translate C definitions and
code
> >to Cobol depends heavily on you Cobol dialect.
>
…[16 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: print a rectangle

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393d724f.155399092@207.126.101.100>`
- **References:** `<8h3kgq$26s$1@duke.telepac.pt> <8h62i1$cpt$1@news.cerf.net> <8h69t8$bf8$1@duke.telepac.pt> <8h8k2o$i1p$1@news.cerf.net> <3937fd6f.150215479@news.cox-internet.com> <Om2%4.31093$t8.514269@news.bc.tac.net>`

```
Hello Greg,

I have the Platform SDK - but it's about 8 months old.  Some of these
are in the mentioned header, but not all of them.  Interestingly, this
actually illustrates my other point.  Here's 3 different ways MS
indicates High-Values.  



On Tue, 6 Jun 2000 01:14:08 -0700, "Greg Condon" <nospam@me.thanks>
wrote:

>Hi Thane -
>
…[48 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
