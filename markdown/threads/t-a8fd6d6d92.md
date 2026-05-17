[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol VS MF WorkBench

_4 messages · 4 participants · 1995-04 → 1995-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol VS MF WorkBench

- **From:** "ro..." <ua-author-12764400@usenetarchives.gap>
- **Date:** 1995-04-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o0hm2$3rh@news.cais.com>`

```
Hey all,

We are going to switch from CA to MF becuase Oracle no longer supports
CA for PRO*COBOL...

We are trying to decide to get either MF-COBOL or MF-WORKBENCH...CAn
anyone give be a brief breakdown on the differences? I assume the
Workbench is some kind on inagrated IDE or something? Can you make
Stand alone, Character mode programs with it, or does the finished
program EXE need a GUI to run...

Thanks
Ron
```

#### ↳ Re: MF Cobol VS MF WorkBench

- **From:** "rad..." <ua-author-5744355@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8fd6d6d92-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3o0hm2$3rh@news.cais.com>`
- **References:** `<3o0hm2$3rh@news.cais.com>`

```
Ron Olshavsky (ro··.@cai··s.com) wrote:
: Hey all,

: We are going to switch from CA to MF becuase Oracle no longer supports
: CA for PRO*COBOL...

: We are trying to decide to get either MF-COBOL or MF-WORKBENCH...CAn
: anyone give be a brief breakdown on the differences? I assume the
: Workbench is some kind on inagrated IDE or something? Can you make
: Stand alone, Character mode programs with it, or does the finished
: program EXE need a GUI to run...

: Thanks
: Ron

Get the workbench. It costs more but you'll be more satisfied since it
will include more.

I haven't worked with MF COBOL since somewhere around release 3.5.x.x.x
(or something in the middle threes) and at that time you could produce
character mode or GUI programs. It was much easier to create character
mode programs. GUI programming required the same manipulations that
writing a GUI program from scratch in "C" required. That may have changed
in the newer releases.

I also have never worked with MF COBOL w/o the full-blown workbench product.
I'm sure if you just bought the compiler you could produce character mode
programs. I hate the workbench editor anyway (coming from mainframe
background) and used SPF386/SPF2 instead.

Robert R. Radina
rad··.@vul··k.com
St. Louis, MO
```

##### ↳ ↳ Re: MF Cobol VS MF WorkBench

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-05-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8fd6d6d92-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8fd6d6d92-p2@usenetarchives.gap>`
- **References:** `<3o0hm2$3rh@news.cais.com> <gap-a8fd6d6d92-p2@usenetarchives.gap>`

```
In article <3o8un1$c.··.@new··k.com>, rad··.@vul··k.com says...
› 
› Get the workbench.  It costs more but you'll be more satisfied since it 
› will include more.
 
› ding, ding $$$. ;-)
 
› 
› I haven't worked with MF COBOL since somewhere around release 3.5.x.x.x
…[5 more quoted lines elided]…
› in the newer releases.                

Current product is 3.2.xx. Character mode programs will always be easier
than GUI - such is the nature of the beast. MF COBOL lets you write
direct windows/os2 api programs in the same style as C/C++ does with all
the problems of learning a new methodolgy yet keeping to a familiar
language.

With the Workbench you get Panels2 which abstracts the GUI underneath to
a more COBOL like environment to program in. You don't have to worry
about message loops for instance. Panels2 lets you write apps in a
portable across GUIs style too. The same program can work on DOS (GUI
emulation), Windows, NT, OS2 and even Motif. Further than that there is
Dialog system that abstracts the whole of the GUI logic away from the
program, like a database manager does for data handling.


› 
› I also have never worked with MF COBOL w/o the full-blown workbench 
…[4 more quoted lines elided]…
› background) and used SPF386/SPF2 instead.

The Workbench now has an integrated GUI editor/debugger (Animator2) where
you can edit, debug, view program structures, source information, etc all
at the same time. It's pretty neat but then I would say that wouldn't I.
;-)

Shaun.
```

#### ↳ Re: MF Cobol VS MF WorkBench

- **From:** "m..." <ua-author-1148957@usenetarchives.gap>
- **Date:** 1995-05-03T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8fd6d6d92-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3o0hm2$3rh@news.cais.com>`
- **References:** `<3o0hm2$3rh@news.cais.com>`

```
In article <3o0hm2$3.··.@new··s.com>,
ro··.@cai··s.com (Ron Olshavsky) wrote:
› 
›  We are trying to decide to get either MF-COBOL or MF-WORKBENCH...CAn 
…[4 more quoted lines elided]…
› 

There are many additional tools in Workbench but not in COBOL. Not least of
which are the GUI development environment (there is also a complete,
tightly integrated character environment), Animator V2, data tools and many
more.

The COBOL system is a linked EXE environment only, but Workbench gives you
access to using the proprietary INT and GNT code formats which can be
important when running large applications on 16bit environments (it also
makes the edit-check-debug cycle quicker). You still have the option to link
and create standard OBJs/EXEs of course. These apps can be character mode or
GUI running under Windows or OS/2.

For more information, I suggest you call the Micro Focus office in Philadelphia
on (601) 992 3400.

Mark Warren
Workbench Product Manager
Micro Focus
Newbury, Berks. UK
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
