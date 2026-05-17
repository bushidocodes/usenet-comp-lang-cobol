[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using C functions in Cobol

_2 messages · 2 participants · 1997-05_

---

### Using C functions in Cobol

- **From:** "10007..." <ua-author-11831916@usenetarchives.gap>
- **Date:** 1997-05-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc60af$a4a8cb00$5d608e93@bausch.isdn.uni-heidelberg.de>`

```

Hi,

I'm working for someone who uses Microfocus Cobol for DOS and I am trying
to implement some C functions with Watcom C for 16 bit DOS.

When I link the C generated obj-file with the Cobol obj-file I always get
the following linker errors:

"big code...."
"small code...."

concerning the c-module.

Any help would be highly appreciated.


Dirk Bausch
```

#### ↳ Re: Using C functions in Cobol

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d7fd6230ff-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc60af$a4a8cb00$5d608e93@bausch.isdn.uni-heidelberg.de>`
- **References:** `<01bc60af$a4a8cb00$5d608e93@bausch.isdn.uni-heidelberg.de>`

```

In message <<01bc60af$a4a8cb00$5d6··.@bau··g.de>> "Dirk Bausch" <100··.@com··e.com> writes:
› 
› I'm working for someone who uses Microfocus Cobol for DOS and I am trying
…[10 more quoted lines elided]…
› Any help would be highly appreciated.
The default for MF Cobol 16bit DOS is large model. You would, at
least, need to do this in Watcom. But I feel that you are
somewhat optimistic, interface routines are supplied for MS C
(and some others) but not, AFAIK, for Watcom. There would need
to be, at least, a fake start-up module that sets up the C
environment for Watcom as you will not be using the real start-up.

With, say, Windows, it would be easier because you would be able
to create a .DLL using Watcom and use it from Cobol, but in DOS
the .obj and all helper routines will be linked together and
need to be compatible.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
