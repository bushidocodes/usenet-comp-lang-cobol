[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Redesigning COBOL-Programs

_7 messages · 7 participants · 1997-09_

---

### Redesigning COBOL-Programs

- **From:** "rheo..." <ua-author-17072442@usenetarchives.gap>
- **Date:** 1997-09-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vgg6f$24g$1@news02.btx.dtag.de>`

```

Who knows a shareware-tool to structure existing cobol-sourcecode ? the
sourcecode is now written without normal layout.

for example :
IF A = B
MOVE C TO D
IF A NOT = B
GO TO FFF.

I would like :
IF A = B
MOVE C TO D
IF A NOT = B
GO TO FFF.

thank you for any help.
-----
mfg r.otto
rheodata gmbh, wiesbaden, germany
```

#### ↳ Re: Redesigning COBOL-Programs

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-09-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5vgg6f$24g$1@news02.btx.dtag.de>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de>`

```

In article <5vgg6f$24g$1.··.@new··g.de>,
Rainer Otto wrote:
› 
› Who knows a shareware-tool to structure existing cobol-sourcecode ? the
…[12 more quoted lines elided]…
›       GO TO FFF.

This tool is called CobolBeautifier (TM) or simply cbl-beau.

You can download it for free from http://www.siber.com/sct/

If you decide to purchase a full version,
you will be able to fully customize your beautification
by defining your own code generation table.

Vadim Maslov
Siber Systems
```

#### ↳ Re: Redesigning COBOL-Programs

- **From:** "mike reublin" <ua-author-15560592@usenetarchives.gap>
- **Date:** 1997-09-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5vgg6f$24g$1@news02.btx.dtag.de>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de>`

```

Rainer Otto wrote:
› 
› Who knows a shareware-tool to structure existing cobol-sourcecode ? the
…[17 more quoted lines elided]…
› rheodata gmbh, wiesbaden, germany

Can't help with a tool, but in the code snippet above, the GO TO will
never be executed.
Prehaps you meant
IF A = B
MOVE C TO D. <- punkt
IF A NOT = B
GO TO FFF.
or

IF A = B
MOVE C TO D
else
GO TO FFF.

Best, Mike
```

##### ↳ ↳ Re: Redesigning COBOL-Programs

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-09-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcd7fadf9a-p3@usenetarchives.gap>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de> <gap-dcd7fadf9a-p3@usenetarchives.gap>`

```

Mike Reublin wrote:
› 
› Rainer Otto wrote:
…[22 more quoted lines elided]…
› never be executed.

[snip]

You have a sharp eye. But if you want to get picky...

If A or B is a group item which contains D, or vice versa, then
MOVE C TO D could change the contents of A or B and thus change
the result of the comparison.

Sorry, I don't know of any relevant tools, either.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: Redesigning COBOL-Programs

- **From:** "e jon" <ua-author-17071971@usenetarchives.gap>
- **Date:** 1997-09-19T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcd7fadf9a-p3@usenetarchives.gap>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de> <gap-dcd7fadf9a-p3@usenetarchives.gap>`

```

Mike Reublin wrote:

› Rainer Otto wrote:
›› 
…[35 more quoted lines elided]…
› Best, Mike

Well, Mike, it depends....

Suppose, this:

01 A.
05 C pic .......

01 B.
05 F pic ........

77 D pic ......

Now, let's see that logic again....

Never underestimate the power of COBOL ... :)
```

###### ↳ ↳ ↳ Re: Redesigning COBOL-Programs

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-09-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcd7fadf9a-p5@usenetarchives.gap>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de> <gap-dcd7fadf9a-p3@usenetarchives.gap> <gap-dcd7fadf9a-p5@usenetarchives.gap>`

```

E Jon wrote in article <342··.@i··.net>...
› Mike Reublin wrote:
› 
…[55 more quoted lines elided]…
› 
Huh? You lost me.
```

###### ↳ ↳ ↳ Re: Redesigning COBOL-Programs

_(reply depth: 4)_

- **From:** "patrick henry" <ua-author-13505@usenetarchives.gap>
- **Date:** 1997-09-20T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcd7fadf9a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcd7fadf9a-p6@usenetarchives.gap>`
- **References:** `<5vgg6f$24g$1@news02.btx.dtag.de> <gap-dcd7fadf9a-p3@usenetarchives.gap> <gap-dcd7fadf9a-p5@usenetarchives.gap> <gap-dcd7fadf9a-p6@usenetarchives.gap>`

```

Joseph Lenz wrote:
› 
› E Jon  wrote in article <342··.@i··.net>...
…[58 more quoted lines elided]…
› Huh?  You lost me.

DUH!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
