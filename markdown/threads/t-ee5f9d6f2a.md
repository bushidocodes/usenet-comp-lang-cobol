[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to control a serial port (read/write data) ?

_9 messages · 9 participants · 1998-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to control a serial port (read/write data) ?

- **From:** "Georgios Terzis" <gnterzis@mail.otenet.gr>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tgg36$if4$1@ns1.otenet.gr>`

```
Does anybody know how can I read data incoming via a serial port (com1,
com2) as well as the status of that port, using mfcobol statements ?
Microfocus has not replied to my question, unfortunatelly !

        Yiorgo    gnterzis@mail.otenet.gr
```

#### ↳ Re: How to control a serial port (read/write data) ?

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tin4l$rpq$2@news00.btx.dtag.de>`
- **References:** `<6tgg36$if4$1@ns1.otenet.gr>`

```
Georgios Terzis schrieb:

> Does anybody know how can I read data incoming via a serial port
> (com1,
…[3 more quoted lines elided]…
>         Yiorgo    gnterzis@mail.otenet.gr

   There is no direct way to control COM-Ports, it is
difficult in C/Pascal/Assembler too. So you must
use external Sub-Progs to control the COM-Port
(but you can read/write Port's in MF-Cobol using X"0??"-Function's)

regards

AS
```

##### ↳ ↳ Re: How to control a serial port (read/write data) ?

- **From:** "Gene Webb" <gene.webb@newsguy.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tir7g$r3q@enews1.newsguy.com>`
- **References:** `<6tgg36$if4$1@ns1.otenet.gr> <6tin4l$rpq$2@news00.btx.dtag.de>`

```
If you need to do this in DOS you can get away with the X'xx' calls, but if
you are going to 95/NT you will need to use the WINAPIs to do this.  If you
know you are going to be going to 95/NT you are better off using the WINAPI
because converting is not a fun process.

Andreas Strzoda wrote in message <6tin4l$rpq$2@news00.btx.dtag.de>...
>Georgios Terzis schrieb:
>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: How to control a serial port (read/write data) ?

- **From:** tom@taltech.com (Thomas Lutz)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360e34c9.38922437@netnews.voicenet.com>`
- **References:** `<6tgg36$if4$1@ns1.otenet.gr>`

```
The company that I work for sells a serial communications program
called the Software Wedge that is designed to add serial I/O
capability to other applications without any modifications to the
other app. The program works by stuffing incoming serial data into the
keyboard buffer so that serial data looks like keyboard input.
If you are interested please visit http://www.taltech.com



On Sun, 13 Sep 1998 16:12:19 +0300, "Georgios Terzis"
<gnterzis@mail.otenet.gr> wrote:

>Does anybody know how can I read data incoming via a serial port (com1,
>com2) as well as the status of that port, using mfcobol statements ?
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How to control a serial port (read/write data) ?

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36084D9A.95AB4785@mindspring.com>`
- **References:** `<6tgg36$if4$1@ns1.otenet.gr> <360e34c9.38922437@netnews.voicenet.com>`

```
is that such a good idea?  how well will it work in an app that may have
to use a serial port while the user is pecking away at the keyboard? 
plus, knowing how temperamental windows can be, how does windows react
when you "max" it out?

Thomas Lutz wrote:
> 
> The company that I work for sells a serial communications program
…[14 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: How to control a serial port (read/write data) ?

- **From:** Frank Pohlmann <Frank.Pohlmann@baeurer.de>
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360B40E3.25121FCF@baeurer.de>`
- **References:** `<6tgg36$if4$1@ns1.otenet.gr> <360e34c9.38922437@netnews.voicenet.com> <36084D9A.95AB4785@mindspring.com>`

```
The easiest way is to use the Windows-API. It work's with 16-Bit and 32-Bit
Windows with MF Workbench 3.1, 3.4 and 4.0 (tested). If you have a
DOS-application, it's more difficult. You can access the ports directly, but
that not funny because the buffer of a COM-Port is only 16 Byte and you need a
good synchronisation.

Frank

skidmike schrieb:

> is that such a good idea?  how well will it work in an app that may have
> to use a serial port while the user is pecking away at the keyboard?
…[20 more quoted lines elided]…
> > >
```

###### ↳ ↳ ↳ Re: How to control a serial port (read/w

_(reply depth: 4)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298267.72483.12901@kcbbs.gen.nz>`
- **References:** `<360B40E3.25121FCF@baeurer.de>`

```
In message <<360B40E3.25121FCF@baeurer.de>> Frank Pohlmann <Frank.Pohlmann@baeurer.de> writes:
> Windows with MF Workbench 3.1, 3.4 and 4.0 (tested). If you have a
> DOS-application, it's more difficult. You can access the ports directly, but
> that not funny because the buffer of a COM-Port is only 16 Byte and you need a
> good synchronisation.
> 
Not quite, the buffer on a COM port on a PC is from 1 to 16 bytes
depending on the actual hardware capabilities and its settings.
```

###### ↳ ↳ ↳ Re: How to control a serial port (read/w

_(reply depth: 5)_

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn70o123.f4.cadams@cadams-ntw.acucorp.com>`
- **References:** `<360B40E3.25121FCF@baeurer.de> <3298267.72483.12901@kcbbs.gen.nz>`

```
On 25 Sep 98 20:08:03 GMT, Richard Plinston <riplin@kcbbs.gen.nz> wrote:
>> Windows with MF Workbench 3.1, 3.4 and 4.0 (tested). If you have a
>> DOS-application, it's more difficult. You can access the ports directly, but
…[3 more quoted lines elided]…
>depending on the actual hardware capabilities and its settings.

Of course, if you head out into Digiboard land you might end up with multi-K
buffers. If you still have to support DOS com ports, a FOSSIL driver is an
excellent means of preserving one's sanity around that point...

----
"Civilization won't *die* from Y2k. It'll be more like Civilization goes out
drinking and the next morning realizes the benefits of drinking gin from
smaller containers."
The opinions above are my own and may or may not match those of my employer.
```

###### ↳ ↳ ↳ Re: How to control a serial port (read/w

_(reply depth: 5)_

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360CD3C9.2F5693BA@infonet.com.py>`
- **References:** `<360B40E3.25121FCF@baeurer.de> <3298267.72483.12901@kcbbs.gen.nz>`

```


Richard Plinston wrote:

> In message <<360B40E3.25121FCF@baeurer.de>> Frank Pohlmann <Frank.Pohlmann@baeurer.de> writes:
> > Windows with MF Workbench 3.1, 3.4 and 4.0 (tested). If you have a
…[5 more quoted lines elided]…
> depending on the actual hardware capabilities and its settings.

I never used MF COBOL, but can't you just open COM1: as a (binary) sequential file with a record
size of 1 byte? In Unix (RM COBOL) it's a breeze.

Regards
Albert Ratzlaff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
