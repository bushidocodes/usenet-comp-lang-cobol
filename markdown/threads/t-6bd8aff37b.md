[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linking MF-Cobol programs (batch)

_3 messages · 3 participants · 1997-05 → 1997-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Linking MF-Cobol programs (batch)

- **From:** "niels chr. madsen" <ua-author-17072125@usenetarchives.gap>
- **Date:** 1997-05-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<338941C1.7B45@post4.tele.dk>`

```

Until now I have been using MF-Cobol version 3.2 running on OS/2. Now I
am changing to MF Object Cobol version 4.0.

In my procedure for compile and link of batch programs I have
the following statements:
'COBOL 'sfn'.CBL,,,,' DirFile || 'BATCH.DIR"' options
if rc > 0 then call QUIT

'LINK 'fn'+xfh2btr+obtrv+extfh+xfhname+externl+extsm/nod,'
fn'.EXE,,os2286+coblib+o:\lib\faaclib.lib, /PM:VIO/ST:4096;'

(My "batch" programs are accessing Btrieve files created by CICS/OS2)

What does I have to write for the new version ?
```

#### ↳ Re: Linking MF-Cobol programs (batch)

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6bd8aff37b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<338941C1.7B45@post4.tele.dk>`
- **References:** `<338941C1.7B45@post4.tele.dk>`

```

In message <<338··.@pos··e.dk>> "Niels Chr. Madsen" writes:
›
› What I am trying to illustrate is that the GOTO verb (as with any verb
› in COBOL) was designed and included in the language to perform a
› specific task, and SHOULD be used for that task.

Are you advocating that the GO TO should be compulsory ?

I have programs written without STRING, INSPECT or START.
Why should I not have some without GO TO ?
```

##### ↳ ↳ Re: Linking MF-Cobol programs (batch)

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1997-06-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6bd8aff37b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6bd8aff37b-p2@usenetarchives.gap>`
- **References:** `<338941C1.7B45@post4.tele.dk> <gap-6bd8aff37b-p2@usenetarchives.gap>`

```

Richard Plinston wrote:
› 
› In message <<338··.@pos··e.dk>> "Niels Chr. Madsen"  writes:
…[8 more quoted lines elided]…
› Why should I not have some without GO TO ?

Richard

What Niels was trying to say is that if there is a COBOL verb that is
designed for a specific purpose, and you need to use it for that purpose
then you SHOULD use it. Personally I believe that you MUST use it.

The use of a verb for the purpose it was designed for should be
encouraged. Whether it is the GOTO, or even the STRING, INSPECT or
START.

IF it WORKS and is MAINTAINABLE then use it !!!!!!!!!!!!!!!

Mike Rochford
-------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
