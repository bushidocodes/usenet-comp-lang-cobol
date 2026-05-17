[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Document, document

_4 messages · 4 participants · 1996-09_

---

### Document, document

- **From:** "moerk_..." <ua-author-6588907@usenetarchives.gap>
- **Date:** 1996-09-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1996Sep6.070906.281@multinet_host_name>`

```

Hi all :)

Doesn't anybody document anymore?

There have been numerous postings regarding "we have source code but
no idea what it's doing", or "we have running code, changes were made,
but nobody knows which or where"..

Even if I do understand that such is probably the result of the
much-invoked "human condition", I must admit that it makes me sick to
read this. Where is the documentation that makes all this
un-necessary?

Is it, in 1996 (or in 1990 :) ) really the case, that when you gotta
make a program, you sit down at the pc/terminal, hack along until you
lose the overview, and then repair from there on, until it works?

..making zero documentation? How can professionals defend this?
We all know how to make good programs.

1. think
2. write your thoughts down
3. have them checked.
4. think some more
5. diagram and specify the actions needed
6. when all this is in place, code the program, some 1 days work,
normally.

You dont have miscompiles, you dont have scandalous problems in the
programs, and you don't have very many, conveniently called, "bugs",
to excuse.

Try it. Contrary to popular belief, you use LESS time, doing it right.
But for some, a booooring prospect, when you can just type
in one mistake after another. Grump. :)=)

My 5 danish ore worth of opinion,
and thaks for reading this brain-ventilation :)

H
```

#### ↳ Re: Document, document

- **From:** "alc..." <ua-author-17086161@usenetarchives.gap>
- **Date:** 1996-09-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-228db7bd3f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1996Sep6.070906.281@multinet_host_name>`
- **References:** `<1996Sep6.070906.281@multinet_host_name>`

```

Well said! Second the motion.
David Webber

On Sep 06, 1996 11:01:59 in article ,
'moe··.@tan··m.com (Henrik P.Moerk)' wrote:
› Hi all :) 
› 
…[38 more quoted lines elided]…
›
```

#### ↳ Re: Document, document

- **From:** "arthur..." <ua-author-12798309@usenetarchives.gap>
- **Date:** 1996-09-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-228db7bd3f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1996Sep6.070906.281@multinet_host_name>`
- **References:** `<1996Sep6.070906.281@multinet_host_name>`

```

› 
›› Doesn't anybody document anymore?
…[15 more quoted lines elided]…
› Munich, Germany


My next job will be to restructure very, very old legacy programs
(dated from 1970, current OS: MVS) for an Insurance Co. The programs are
documented, indeed, but the client wants to have them now changed to
COBOL'85 style in order to add new functionality later on with less
effort.
I would like to have some restructuring support for this task, e.g. for
detecting groups of statements like
if ..
...
goto a
if ..
...
goto a

etc.

which could probably be changed to a block:

evaluate ...
when ..
...
when ..
...
etc.
end-evaluate

does anybody have an idea whether there exists software for this task
("Computer Aided COBOL Restructuring")
or perhaps done a similar job?

Thanks, Arthur
```

##### ↳ ↳ Re: Document, document

- **From:** "glenn a. mitchell" <ua-author-17072865@usenetarchives.gap>
- **Date:** 1996-09-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-228db7bd3f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-228db7bd3f-p3@usenetarchives.gap>`
- **References:** `<1996Sep6.070906.281@multinet_host_name> <gap-228db7bd3f-p3@usenetarchives.gap>`

```

Arthur Fichtl wrote:

› 
› My next job will be to restructure very, very old legacy programs
…[3 more quoted lines elided]…
› effort.
 
› 
› does anybody have an idea whether there exists software for this task
…[3 more quoted lines elided]…
› Thanks,  Arthur

Information on IBM's COBOL restructuring tool is available at:
http://www.software.ibm.com/ad/cobol/cobolwpl.htm#Header_58. It
purports to do exactly what you want to do.
Glenn A. Mitchell               mailto:mit··.@poa··c.org
Director, Computer Technology   http://www.mmc.org
Maine Medical Center            
Portland, ME  04101
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
