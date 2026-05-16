[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and ASP

_4 messages · 4 participants · 1999-07_

---

### COBOL and ASP

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379a95e8.87583881@news1.ibm.net>`

```
I was visiting my book in a B&N and picked up an ASP book and read
about it some.   What I found was that for CGI a separate instance of
the application is started - including any runtime setup overhead -
but for ASP a DLL is loaded in memory and used.  Has anyone here done
any COBOL and ASP work?  I'd like the hear more about it.
```

#### ↳ Re: COBOL and ASP

- **From:** "J.Reynaert" <newsreader@kjsgroup.com>
- **Date:** 1999-07-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<932906836.704.65@news.remarQ.com>`
- **References:** `<379a95e8.87583881@news1.ibm.net>`

```
Thane

Yes, I have done extensive work in this area.  Did you have
some specific question ?

Overhead, IHMO, not as much as running an SQL server.
COBOL compilers/runtimes tend to be very compact.
Convenience, well SQL or Access has some advantage here.
Reusable, if you have a lot of COBOL code (which presumably
if you are here, you do) then creating ASP front ends is not
that difficult depending of course on the code.

I found the simple Visual Object Cobol product from Microfocus
to be the cleanest to work with for this type of work.
 (I have looked at the eval of their Netexpress product,
but in the end didn't buy it. I felt I was not treated properly
on the Vis Ob Cob product. Since they abandoned it without
warning about the same time they cashed my cheque.)
There are some issues with the runtime of VisObCob.
I also have their full Version 4 WB.

As I don't visit here with any schedule, if you want to
know more e-mail me   kjs at kjsgroup dot com

John


Thane Hubbell <redsky@ibm.net> wrote in message
news:379a95e8.87583881@news1.ibm.net...
> I was visiting my book in a B&N and picked up an ASP book and read
> about it some.   What I found was that for CGI a separate instance of
…[3 more quoted lines elided]…
>
```

#### ↳ Re: COBOL and ASP

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-07-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GdNm3.4893$OP.53387@news1.frmt1.sfba.home.com>`
- **References:** `<379a95e8.87583881@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote in message
news:379a95e8.87583881@news1.ibm.net...
> I was visiting my book in a B&N and picked up an ASP book and read
> about it some.   What I found was that for CGI a separate instance of
> the application is started - including any runtime setup overhead -
> but for ASP a DLL is loaded in memory and used.  Has anyone here done
> any COBOL and ASP work?  I'd like the hear more about it.

the DLL in this case is likely to be plugged into the webserver (Microsoft's
IIS) as an ISAPI DLL (it's essentially a multi-threaded DLL that stays
loaded vs. something that is process based that is loaded and unloaded each
time).
```

#### ↳ Re: COBOL and ASP

- **From:** "Robert Kovacic" <rjk@bigpond.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<owQm3.13543$yD2.29961@newsfeeds.bigpond.com>`
- **References:** `<379a95e8.87583881@news1.ibm.net>`

```
If you have an ODBC driver for your COBOL data files then you can program
with ASP without restriction.

If you are interested in "Internet programming" and COBOL you should have a
look at what NetExpress 3.0 could offer you. For example, you could write
COBOL Internet programmes which take advantage of the ISAPI interface to the
MS Internet Server to give the efficiency advantages which I think you are
alluding to.

Thane Hubbell wrote in message <379a95e8.87583881@news1.ibm.net>...
>I was visiting my book in a B&N and picked up an ASP book and read
>about it some.   What I found was that for CGI a separate instance of
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
