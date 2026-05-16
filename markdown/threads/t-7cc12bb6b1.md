[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# passing info

_9 messages · 5 participants · 2000-10 → 2000-11_

---

### passing info

- **From:** "Tom Wright" <twright@@larimore.net>
- **Date:** 2000-10-31T12:25:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<laEL5.1386$fv1.160585@news1.primary.net>`

```
I've written a cobol program (A) that uses CreateProcess to start another
cobol program(B).  How can I go about passing information from (A) to (B).
I'm trying to use pointers but I can't seem to get (B) to find anything in
that memory address.  Any thoughts

Tom Wright
twright@larimore.net
```

#### ↳ Re: passing info

- **From:** "Brad Prothero" <brad.prothero@clarica.com>
- **Date:** 2000-10-31T12:53:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MyEL5.118$1p2.20789@news.corpcomm.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net>`

```
There are two that come to mind right away.

1. Use a bridge file. In program (A) write out the information in a temp
file and have (B) read it in. This may work well and this is the easiest way
that I know of.

2. Since you are use to using API calls, you might look into pipes. I have
no experience with these but it is being looked at for one of our
applications to handle the situation that you just described.

I am no expert but these are the only two ways that I know of.

Brad Prothero

Tom Wright <twright@@larimore.net> wrote in message
news:laEL5.1386$fv1.160585@news1.primary.net...
> I've written a cobol program (A) that uses CreateProcess to start another
> cobol program(B).  How can I go about passing information from (A) to (B).
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: passing info

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-10-31T16:59:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CVIL5.1588$fP1.843@newsfeed.slurp.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <MyEL5.118$1p2.20789@news.corpcomm.net>`

```
Another would be shared memory - can be accessed via API calls.  Check
out the "CreateFileMapping" and "MapViewOfFile" Win32 API's.

TL

> Tom Wright <twright@@larimore.net> wrote in message
> news:laEL5.1386$fv1.160585@news1.primary.net...
> > I've written a cobol program (A) that uses CreateProcess to start
another
> > cobol program(B).  How can I go about passing information from (A)
to (B).
> > I'm trying to use pointers but I can't seem to get (B) to find
anything in
> > that memory address.  Any thoughts
```

#### ↳ Re: passing info

- **From:** "mangogwr" <mangogrower@telocity.co>
- **Date:** 2000-10-31T22:00:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net>`

```
How about the PLATFORM/COBOL Vendor, Tom?  That may help someone help you
more!


Tom Wright <twright@@larimore.net> wrote in message
news:laEL5.1386$fv1.160585@news1.primary.net...
> I've written a cobol program (A) that uses CreateProcess to start another
> cobol program(B).  How can I go about passing information from (A) to (B).
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: passing info

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-11-01T12:32:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net>`

```
Platform is immaterial: Addresses (pointers) in one Win/32 process are not
valid in another Win/32 process.

As suggested earlier by someone else, you need use the CreateFileMapping and
MapViewOfFile API calls to share data across address spaces. (Or one of the
other officially-sanctioned methods).

FOR REFERENCE....

Purchase a reprint of my article, "Data Sharing in 32-bit Windows"  which
appeared in the October, 1999 issue of "BASICally Speaking" magazine at the
IMS web Site at www.infoms.com. (Four bucks US; I don't receive any of
that).

While the code in the article is written in BASIC, the text covers the
concepts in a language-neutral manner.
```

###### ↳ ↳ ↳ Re: passing info

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-11-01T13:14:16
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tp8ph$qpc$1@hyperion.mfltd.co.uk>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net> <I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net...
> Platform is immaterial: Addresses (pointers) in one Win/32 process are not
> valid in another Win/32 process.
>

That is true, however...

> As suggested earlier by someone else, you need use the CreateFileMapping
and
> MapViewOfFile API calls to share data across address spaces. (Or one of
the
> other officially-sanctioned methods).
>

...if Tom is using a Merant product, the CBL_GET_SHMEM_PTR and
CBL_PUT_SHMEM_PTR APIs can be used in conjunction with the ability to create
shared memory via the CBL_ALLOC_MEM call. On Win32 that provides  the
CreateFileMapping and MapViewOfFile functionality between COBOl run-units,
which are implemented as processes.

In the example given, process a) would allocate shared memory and and use
CBL_PUT_SHMEM_PTR to associate a name with the memory block. If process b)
was executed via CBL_EXEC_RUN_UNIT it could use CBL_GET_SHMEM_PTR to get the
address back and then use linkage to access that memory.

Those calls are supported on Win32 and UNIX products from Merant ie they are
not platform specific.
```

###### ↳ ↳ ↳ Re: passing info

_(reply depth: 4)_

- **From:** "Tom Wright" <twright@@larimore.net>
- **Date:** 2000-11-02T09:34:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mSfM5.1546$fv1.175432@news1.primary.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net> <I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net> <8tp8ph$qpc$1@hyperion.mfltd.co.uk>`

```

"Gael Wilson" <gael.wilson@merant.com> wrote in message
news:8tp8ph$qpc$1@hyperion.mfltd.co.uk...
>
> "Michael Mattias" <michael.mattias@gte.net> wrote in message
> news:I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net...
> > Platform is immaterial: Addresses (pointers) in one Win/32 process are
not
> > valid in another Win/32 process.
> >
…[11 more quoted lines elided]…
> CBL_PUT_SHMEM_PTR APIs can be used in conjunction with the ability to
create
> shared memory via the CBL_ALLOC_MEM call. On Win32 that provides  the
> CreateFileMapping and MapViewOfFile functionality between COBOl run-units,
…[4 more quoted lines elided]…
> was executed via CBL_EXEC_RUN_UNIT it could use CBL_GET_SHMEM_PTR to get
the
> address back and then use linkage to access that memory.

True but one problem is that I can't pass any info in the linkage section
from one program the uses createprocess to another programs linkage section
that was spawned.  So really it doesn't matter what cobol platform I'm
programming on since whatever I use will have to be os specific.  But to
satisfy everyones need ....and I do apologize for not putting this in my
original posting......I'm using MF cobol 4.032.  On winnt /win9x.



> Those calls are supported on Win32 and UNIX products from Merant ie they
are
> not platform specific.
>
>
>
```

###### ↳ ↳ ↳ Re: passing info

- **From:** "mangogwr" <mangogrower@telocity.co>
- **Date:** 2000-11-01T17:54:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uf1M5.30228$Q8.6702568@newsrump.sjc.telocity.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net> <I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net>`

```
100 Percent INCORRECT.

WIN32 is the Platform!

The oiginal post could have been asking about
Win
Unix / Xenix
Linux
OS/2
MVS
MainFrame DOS
GCOS
Wang VS

Michael Mattias <michael.mattias@gte.net> wrote in message
news:I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net...
> Platform is immaterial: Addresses (pointers) in one Win/32 process are not
> valid in another Win/32 process.
>
> As suggested earlier by someone else, you need use the CreateFileMapping
and
> MapViewOfFile API calls to share data across address spaces. (Or one of
the
> other officially-sanctioned methods).
>
…[3 more quoted lines elided]…
> appeared in the October, 1999 issue of "BASICally Speaking" magazine at
the
> IMS web Site at www.infoms.com. (Four bucks US; I don't receive any of
> that).
…[13 more quoted lines elided]…
> > How about the PLATFORM/COBOL Vendor, Tom?  That may help someone help
you
> > more!
> >
…[7 more quoted lines elided]…
> > > I'm trying to use pointers but I can't seem to get (B) to find
anything
> in
> > > that memory address.  Any thoughts
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: passing info

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-11-03T13:02:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fHyM5.39$Mr2.23379@paloalto-snr1.gtei.net>`
- **References:** `<laEL5.1386$fv1.160585@news1.primary.net> <PLLL5.28133$Q8.6375743@newsrump.sjc.telocity.net> <I3UL5.81$i_5.38456@dfiatx1-snr1.gtei.net> <uf1M5.30228$Q8.6702568@newsrump.sjc.telocity.net>`

```
mangogwr <mangogrower@telocity.co> wrote in message
news:uf1M5.30228$Q8.6702568@newsrump.sjc.telocity.net...
> 100 Percent INCORRECT.
>
…[14 more quoted lines elided]…
> > Platform is immaterial: Addresses (pointers) in one Win/32 process are
not
> > valid in another Win/32 process.
> >

When the poster asked about a processes spawned with "CreateProcess", I took
a guess that Win/32 was the platform. You will also note my response was
qualified.

Perhaps "platform" was the wrong choice of words; what I thought it meant in
context was "which hardware and version of 32-bit Windows?"

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
