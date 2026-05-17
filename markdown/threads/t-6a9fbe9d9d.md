[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Microfocus & Runtime

_5 messages · 4 participants · 1995-09 → 1995-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL Microfocus & Runtime

- **From:** "coc..." <ua-author-6042747@usenetarchives.gap>
- **Date:** 1995-09-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<445s03$31u@accursio.comune.bologna.it>`

```
We have to develop a new application using an old COBOL source, using
the MicroFocus COBOL 3.2 for Windows (16 bit).
The problem is that since we plan a wide deploy of this application on
our customers (it's a sort of demo) we cannot use the .GNT method that
MF license with a runtime.
1) If we generate the code in .DLLs, do we need the runtime?
2) Any other alternatives?
_________________
Nicola Martelli
Bologna, Italy
```

#### ↳ Re: COBOL Microfocus & Runtime

- **From:** "michael mcskeane" <ua-author-15668547@usenetarchives.gap>
- **Date:** 1995-09-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a9fbe9d9d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<445s03$31u@accursio.comune.bologna.it>`
- **References:** `<445s03$31u@accursio.comune.bologna.it>`

```
In article: <445s03$3.··.@acc··a.it>
coc··.@ipe··a.it (Nicola Martelli) writes:
› 
› We have to develop a new application using an old COBOL source, using
…[9 more quoted lines elided]…
› 
I used to work in a bank that would only compile MF cobol to .EXE's for
this very reason. The general view was that you did not need to license
EXE's. If this is not true then they owe MicroFocus one hell of a lot
of money.

=========================================================================
Michael McSkeane
m.··.@sch··o.uk
```

##### ↳ ↳ Re: COBOL Microfocus & Runtime

- **From:** "sarn..." <ua-author-15201208@usenetarchives.gap>
- **Date:** 1995-09-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a9fbe9d9d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a9fbe9d9d-p2@usenetarchives.gap>`
- **References:** `<445s03$31u@accursio.comune.bologna.it> <gap-6a9fbe9d9d-p2@usenetarchives.gap>`

```
If you use any of the OSX (Operating Systems Extensions), you have to pay
royalty. In the real life this means, you can compile to .OBJ-files,
then link them (to .EXE or .DLL), and then use the runtime for those
files (COBLIB.DL?). This will be free of charge on all PC-platforms
(DOS, Windows, OS/2).

If you compile to .GNT, you need the Runtime Environment (RTE), for which
you have to pay fees. With the RTE you get an advanced memory handling,
so you can run programs larger than available memory. When linking
to .EXE, you need XM (eXtended Memory handler). This is royalty-free,
and enables you to run programs in "extended memory", that is XMS, EMS,
DPMI etc. Then you are past the 640 K limit.

So says the licence agreement in the package and on the disks.

We have over the years developed some large PC-applications using MF Cobol,
all distributed as .EXE because of the royalty question. We are now
converting to GUI, and have looked at MicroFocus Dialog System.

Because of the Dialog System we decided to use Borland Delphi for future
development, because it was easier to design forms and so on. But after
getting to the "core code" we must realize, that Cobol IS for business
applications, and Delphi is not. In some other thread one says, that
he can do in five minutes in C what others will need weeks for using
Cobol. Well, I can do some datamanipulation and string handling
in five minutes in Cobol that we need two days to program in Delphi. So,
if we could combine Delpi and Cobol, that would be nice.




Michael McSkeane (M.··.@sch··o.uk) wrote:
: In article: <445s03$3.··.@acc··a.it>
: coc··.@ipe··a.it (Nicola Martelli) writes:
: >
: >We have to develop a new application using an old COBOL source, using
: >the MicroFocus COBOL 3.2 for Windows (16 bit).
: >The problem is that since we plan a wide deploy of this application on
: >our customers (it's a sort of demo) we cannot use the .GNT method that
: >MF license with a runtime.
: >1) If we generate the code in .DLLs, do we need the runtime?
: >2) Any other alternatives?
: >_________________
: >Nicola Martelli
: >Bologna, Italy
: >
: I used to work in a bank that would only compile MF cobol to .EXE's for
: this very reason. The general view was that you did not need to license
: EXE's. If this is not true then they owe MicroFocus one hell of a lot
: of money.

: =========================================================================
: Michael McSkeane
: m.··.@sch··o.uk
```

##### ↳ ↳ Re: COBOL Microfocus & Runtime

- **From:** "coc..." <ua-author-6042747@usenetarchives.gap>
- **Date:** 1995-10-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a9fbe9d9d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a9fbe9d9d-p2@usenetarchives.gap>`
- **References:** `<445s03$31u@accursio.comune.bologna.it> <gap-6a9fbe9d9d-p2@usenetarchives.gap>`

```
Michael McSkeane wrote:

› I used to work in a bank that would only compile MF cobol to .EXE's for 
› this very reason. The general view was that you did not need to license 
› EXE's. If this is not true then they owe MicroFocus one hell of a lot 
› of money.

Yes, that's what I understood too. What I don't know is this is true
when compiling to DLLs. The EXE only could end up too big.


_________________
Nicola Martelli
Bologna, Italy
```

###### ↳ ↳ ↳ Re: COBOL Microfocus & Runtime

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1995-10-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6a9fbe9d9d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6a9fbe9d9d-p4@usenetarchives.gap>`
- **References:** `<445s03$31u@accursio.comune.bologna.it> <gap-6a9fbe9d9d-p2@usenetarchives.gap> <gap-6a9fbe9d9d-p4@usenetarchives.gap>`

```
coc··.@ipe··a.it (Nicola Martelli) wrote:
› Michael McSkeane  wrote:
› 
…[9 more quoted lines elided]…
› Bologna, Italy

the way the run-time licensing works is that some parts of it are free and some parts of it
(OSX) are chargeable.

you are paying (or not as the case may be) for the functions, irrespective of how those
functions are packaged and shipped.

Crookie
g.··.@mfl··o.uk
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
