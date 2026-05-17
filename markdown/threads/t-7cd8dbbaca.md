[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP ME, I'VE PROBLEMS WITH MY COMPILER !

_5 messages · 5 participants · 1997-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP ME, I'VE PROBLEMS WITH MY COMPILER !

- **From:** "di..." <ua-author-786271@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3370b998.1436148@news.ping.be>`

```

Hi,

I made a cbl-file and i've compiled it
I make an obj-file (with : COBOL filename)
next i try to link it (with mf-cobol or ms-cobol; LINK OBJfilename )
until here it works !
but when I try to run my EXE-file
it keeps asking for : ADISINIT.EXE

PLEASE HELP...
Can some one post or send me this exe-file ?

THANX
DIGIT... :))
```

#### ↳ Re: HELP ME, I'VE PROBLEMS WITH MY COMPILER !

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cd8dbbaca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3370b998.1436148@news.ping.be>`
- **References:** `<3370b998.1436148@news.ping.be>`

```

In message <<337··.@new··g.be>> DI··.@fre··l.nl writes:
› 
› I made a cbl-file and i've compiled it
…[7 more quoted lines elided]…
› Can some one post or send me this exe-file ?

The manual will tell you how to build ADIS.EXE containg ADIS.OBJ,
ADISINIT.OBJ and ADISKEYS.OBJ, or just link these in with your
program:

LINK program+adis+adisinit+adiskeys;

These are required because you are using the screen section or
accept display AT or CONSOLE IS CRT, or similar.

If you are using an ISAM file then you will also need to build
an EXTFH.EXE or include EXTFH.OBJ in the link.
```

#### ↳ Re: HELP ME, I'VE PROBLEMS WITH MY COMPILER !

- **From:** "clifford lane" <ua-author-2820384@usenetarchives.gap>
- **Date:** 1997-05-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cd8dbbaca-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3370b998.1436148@news.ping.be>`
- **References:** `<3370b998.1436148@news.ping.be>`

```

If I recall from my days of using MS-Cobol (repackaged MF Cobol) you need
to include several modules in the link step that provide access to runtime
modules.

You will have to look up the ADISINIT in your documentation. Also check
out some of the samples projects that are supplied, they should list these
files as part of your compile or link step.
Cliff Lane

DIGIT wrote in article
<337··.@new··g.be>...
› Hi,
› 
…[13 more quoted lines elided]…
›
```

#### ↳ Re: HELP ME, I'VE PROBLEMS WITH MY COMPILER !

- **From:** "a..." <ua-author-17071794@usenetarchives.gap>
- **Date:** 1997-05-08T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cd8dbbaca-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3370b998.1436148@news.ping.be>`
- **References:** `<3370b998.1436148@news.ping.be>`

```

DI··.@fre··l.nl (DIGIT) wrote:

› Hi,
 
› I made a cbl-file and i've compiled it
› I make an obj-file (with : COBOL filename)
…[3 more quoted lines elided]…
› it keeps asking for : ADISINIT.EXE

you need to either include the ADIS support modules in when you link
your program, e.g.
link myprog+adis+adiskey+adisinit
or link the adis modules to a separate exe (or dll depending on your
environment), which will be dynamically loaded 'under the covers'
provided it's on the path or in the same directory.




best
Al
remove the anti-spam hypen in a.··.@mic··s.com for my email address
```

#### ↳ Re: HELP ME, I'VE PROBLEMS WITH MY COMPILER !

- **From:** "mel..." <ua-author-6589066@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cd8dbbaca-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3370b998.1436148@news.ping.be>`
- **References:** `<3370b998.1436148@news.ping.be>`

```

DI··.@fre··l.nl (DIGIT) wrote:


Version MF Compiler ?
Regards
Daniel Fernandez



› Hi,
 
› I made a cbl-file and i've compiled it
› I make an obj-file (with : COBOL filename)
…[3 more quoted lines elided]…
› it keeps asking for : ADISINIT.EXE
 
› PLEASE HELP...
› Can some one post or send me this exe-file ?
 
› THANX
› DIGIT...  :))


E-mail: mel··.@sat··k.com
Comodoro Rivadavia - Chubut - Patagonia Argentina
Capital del viento
==================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
