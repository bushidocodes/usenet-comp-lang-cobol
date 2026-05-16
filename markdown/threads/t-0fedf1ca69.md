[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rebuild of microfocus

_8 messages · 4 participants · 2000-12 → 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### rebuild of microfocus

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-12-29T19:36:13
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92iqm6$mrt$1@venus.telepac.pt>`

```
I see in Microfocus support the resolution of the error Ic255-i that appears
when we run the rebuild. And the solution is make a "extract of fttext.lng
and idxcheck.lng from mflangf.lbr and put these files into the same
directory as rebuild.exe".

Is there somebody who could help me how can i extract a file from the
library file.

Thank you

Raimundo Carvalho
```

#### ↳ Re: rebuild of microfocus

- **From:** Fred Snyder <fpsnyder@bellsouth.net>
- **Date:** 2000-12-29T20:13:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A4D36A9.743729DB@bellsouth.net>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt>`

```
If your using the 32bit Character version F7 from the workbench will allow you
to load the library and then once loaded you can use additional function keys to
extract the files you want. Hope that gives you a starting point.

Raimundo Carvalho wrote:

> I see in Microfocus support the resolution of the error Ic255-i that appears
> when we run the rebuild. And the solution is make a "extract of fttext.lng
…[8 more quoted lines elided]…
> Raimundo Carvalho
```

##### ↳ ↳ Re: rebuild of microfocus

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-12-30T22:25:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92lnsj$10r$1@venus.telepac.pt>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net>`

```
I don�t use Workbench. I use Microfocus Netexpress 3.0 and in NE i can�t
load a library i suppose.

I am trying to run de file LIB.exe but with no success.

Thank you

Raimundo Carvalho

Fred Snyder <fpsnyder@bellsouth.net> escreveu na mensagem
news:3A4D36A9.743729DB@bellsouth.net...
> If your using the 32bit Character version F7 from the workbench will allow
you
> to load the library and then once loaded you can use additional function
keys to
> extract the files you want. Hope that gives you a starting point.
>
> Raimundo Carvalho wrote:
>
> > I see in Microfocus support the resolution of the error Ic255-i that
appears
> > when we run the rebuild. And the solution is make a "extract of
fttext.lng
> > and idxcheck.lng from mflangf.lbr and put these files into the same
> > directory as rebuild.exe".
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: rebuild of microfocus

- **From:** davidc18@my-deja.com
- **Date:** 2001-01-01T11:03:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92po5q$oj9$1@nnrp1.deja.com>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net> <92lnsj$10r$1@venus.telepac.pt>`

```
You can download the LIBMAN.ZIP file from the
Samples page. The LIBMAN.EXE program included in
this file will do the job




In article <92lnsj$10r$1@venus.telepac.pt>,
  "Raimundo Carvalho" <ray@mail.telepac.pt> wrote:
> I don�t use Workbench. I use Microfocus
Netexpress 3.0 and in NE i can�t
> load a library i suppose.
>
> I am trying to run de file LIB.exe but with no
success.
>
> Thank you
…[3 more quoted lines elided]…
> Fred Snyder <fpsnyder@bellsouth.net> escreveu
na mensagem
> news:3A4D36A9.743729DB@bellsouth.net...
> > If your using the 32bit Character version F7
from the workbench will allow
> you
> > to load the library and then once loaded you
can use additional function
> keys to
> > extract the files you want. Hope that gives
you a starting point.
> >
> > Raimundo Carvalho wrote:
> >
> > > I see in Microfocus support the resolution
of the error Ic255-i that
> appears
> > > when we run the rebuild. And the solution
is make a "extract of
> fttext.lng
> > > and idxcheck.lng from mflangf.lbr and put
these files into the same
> > > directory as rebuild.exe".
> > >
> > > Is there somebody who could help me how can
i extract a file from the
> > > library file.
> > >
…[5 more quoted lines elided]…
>



Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: rebuild of microfocus

- **From:** davidc18@my-deja.com
- **Date:** 2001-01-01T11:03:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92po5s$oja$1@nnrp1.deja.com>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net> <92lnsj$10r$1@venus.telepac.pt>`

```
You can download the LIBMAN.ZIP from the Samples
page. This file includes the program LIBMAN.EXE.
Among other options it includes the option to
extract files from LBR library


In article <92lnsj$10r$1@venus.telepac.pt>,
  "Raimundo Carvalho" <ray@mail.telepac.pt> wrote:
> I don�t use Workbench. I use Microfocus
Netexpress 3.0 and in NE i can�t
> load a library i suppose.
>
> I am trying to run de file LIB.exe but with no
success.
>
> Thank you
…[3 more quoted lines elided]…
> Fred Snyder <fpsnyder@bellsouth.net> escreveu
na mensagem
> news:3A4D36A9.743729DB@bellsouth.net...
> > If your using the 32bit Character version F7
from the workbench will allow
> you
> > to load the library and then once loaded you
can use additional function
> keys to
> > extract the files you want. Hope that gives
you a starting point.
> >
> > Raimundo Carvalho wrote:
> >
> > > I see in Microfocus support the resolution
of the error Ic255-i that
> appears
> > > when we run the rebuild. And the solution
is make a "extract of
> fttext.lng
> > > and idxcheck.lng from mflangf.lbr and put
these files into the same
> > > directory as rebuild.exe".
> > >
> > > Is there somebody who could help me how can
i extract a file from the
> > > library file.
> > >
…[5 more quoted lines elided]…
>



Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: rebuild of microfocus

_(reply depth: 4)_

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2001-01-01T21:05:39
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92qrv6$oig$1@venus.telepac.pt>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net> <92lnsj$10r$1@venus.telepac.pt> <92po5s$oja$1@nnrp1.deja.com>`

```
Thank you by your help.

I have download de libman.zip and i go verify it imediatly.

Thank you

Raimundo Carvalho

<davidc18@my-deja.com> escreveu na mensagem
news:92po5s$oja$1@nnrp1.deja.com...
> You can download the LIBMAN.ZIP from the Samples
> page. This file includes the program LIBMAN.EXE.
…[55 more quoted lines elided]…
> http://www.deja.com/
```

###### ↳ ↳ ↳ Re: rebuild of microfocus

- **From:** 098821430@doar.net
- **Date:** 2001-01-01T11:09:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92poh4$old$1@nnrp1.deja.com>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net> <92lnsj$10r$1@venus.telepac.pt>`

```
You can download the libman.zip file from the Samples page
http://pita.microfocus.com/prodsupp/adv/netx/nesamp.htm
This file includes LIBMAN.EXE program that will do the job.

In article <92lnsj$10r$1@venus.telepac.pt>,
  "Raimundo Carvalho" <ray@mail.telepac.pt> wrote:
> I don�t use Workbench. I use Microfocus Netexpress 3.0 and in NE i
can�t
> load a library i suppose.
>
…[8 more quoted lines elided]…
> > If your using the 32bit Character version F7 from the workbench
will allow
> you
> > to load the library and then once loaded you can use additional
function
> keys to
> > extract the files you want. Hope that gives you a starting point.
…[3 more quoted lines elided]…
> > > I see in Microfocus support the resolution of the error Ic255-i
that
> appears
> > > when we run the rebuild. And the solution is make a "extract of
> fttext.lng
> > > and idxcheck.lng from mflangf.lbr and put these files into the
same
> > > directory as rebuild.exe".
> > >
> > > Is there somebody who could help me how can i extract a file from
the
> > > library file.
> > >
…[5 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: rebuild of microfocus

_(reply depth: 4)_

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2001-01-01T21:05:51
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92qrvh$7ld$1@venus.telepac.pt>`
- **References:** `<92iqm6$mrt$1@venus.telepac.pt> <3A4D36A9.743729DB@bellsouth.net> <92lnsj$10r$1@venus.telepac.pt> <92poh4$old$1@nnrp1.deja.com>`

```
Thank you by your help.

I have download de libman.zip and i go verify it imediatly.

Thank you

Raimundo Carvalho

<098821430@doar.net> escreveu na mensagem
news:92poh4$old$1@nnrp1.deja.com...
> You can download the libman.zip file from the Samples page
> http://pita.microfocus.com/prodsupp/adv/netx/nesamp.htm
…[48 more quoted lines elided]…
> http://www.deja.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
