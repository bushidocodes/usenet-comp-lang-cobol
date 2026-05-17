[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Flex, Bison, Ebcdic, IBM/MVS

_6 messages · 4 participants · 1996-10 → 1996-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Flex, Bison, Ebcdic, IBM/MVS

- **From:** "bruno...." <ua-author-17086621@usenetarchives.gap>
- **Date:** 1996-10-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<557d09$98m@news1.Belgium.EU.net>`

```

At company I work for, we are developing a tool to check cobol
coding standards. This tool was initially developed in a Windows
NT environment (with flex and bison and using a Microsoft C
compiler). We planned to port this tool to our IBM/MVS mainframe
environment (using the SAS C compiler). We are not yet running
Open Edition on our mainframe.

We were aware of the ASCII - EBCDIC conversion problem, but we
are been faced now with problems that seems quite difficult to
solve.

1. An alternative we investigated was to change, on the
mainframe, the input to flex from EBCDIC to ASCII, in order
to use the same version of flex on both platforms (WinNT +
IBM/MVS). The output of flex then needs again to be translated
back to EBCDIC. This poses us various problems. Flex passes
sometimes information to Bison that is not really what we expect
to be passed. The reason for this is that we suspect that the
ASCII-EBCDIC translation and back is not done on the right places.
This does also seem to be a not so elegant solution.

2. In one of the replies to a thread in the comp.compilers
newsgroup a while ago suggestion was made to port Flex to the target
machine and run it there to produce the scanner. We downloaded
the last flex source code (2.5.3). One of the files in the
distribution package discussses the changes to make to adapt
flex to run on an IBM mainframe. We did this. Several other
changes had to be made in the C programs, in order to cope with
the file system on the mainframe. The patches for flex in the
distribution package date back from the 2.3 release. We are
therefore not sure if they work for the last release. We did not
succeed in compiling the EBCDIC scanner program (scan.c)

I would like to ask if anyone has already succeeded in doing
what I described above. All guidance on this matter is welcome.

Thanks in advance,


Bruno Peeters
Gemeentekrediet
bru··.@gkb··b.be
```

#### ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c6aafb58b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<557d09$98m@news1.Belgium.EU.net>`
- **References:** `<557d09$98m@news1.Belgium.EU.net>`

```

bru··.@gkb··b.be (Bruno Peeters) wrote:

› At company I work for, we are developing a tool to check cobol
› coding standards. This tool was initially developed in a Windows
…[3 more quoted lines elided]…
› Open Edition on our mainframe.
 
› We were aware of the ASCII - EBCDIC conversion problem, but we
› are been faced now with problems that seems quite difficult to
› solve.

Why don't you write the checker program in COBOL in the MVS
environment? I did this for my company in 1991. I was able to port
it to Realia COBOL V4.2 for DOS and OS/2 with no changes whatsoever.

› 1. An alternative we investigated was to change, on the
› mainframe, the input to flex from EBCDIC to ASCII, in order
…[6 more quoted lines elided]…
› This does also seem to be a not so elegant solution.
 
› 2. In one of the replies to a thread in the comp.compilers 
› newsgroup a while ago suggestion was made to port Flex to the target
…[8 more quoted lines elided]…
› succeed in compiling the EBCDIC scanner program (scan.c)
 
› I would like to ask if anyone has already succeeded in doing
› what I described above. All guidance on this matter is welcome.
 
› Thanks in advance,
 
› Bruno Peeters
› Gemeentekrediet
› bru··.@gkb··b.be

Well, I did have to make two changes in the COBOL hosted COBOL checker
when I ported it to Realia COBOL 4.2. I had to set the compile-time
option to tell it the input source file was in ASCII. I also had to
add an edit for a null command-line, since this feature behaved
differently in MS-DOS from MVS/ESA, but I was able to make a simple
change which worked perfectly in either environment.

Of course, I have no familiarity with Flex and Bison, so I wrote a
monolithic COBOL program (now up to 6000 lines) with an integrated
scanner and no complicated syntax parsing. And not knowing your
coding standard requirements, my program may be a lot less ambitious
than yours. It operates in a character mode environment only, and
produces a report like a compile listing with diagnostic messages.

So, what's wrong with writing a COBOL checker in COBOL?

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "bruno...." <ua-author-17086621@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c6aafb58b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c6aafb58b-p2@usenetarchives.gap>`
- **References:** `<557d09$98m@news1.Belgium.EU.net> <gap-5c6aafb58b-p2@usenetarchives.gap>`

```

arn··.@wor··t.net (Arnold J. Trembley) wrote:

› Why don't you write the checker program in COBOL in the MVS
› environment? I did this for my company in 1991. I was able to port
› it to Realia COBOL V4.2 for DOS and OS/2 with no changes whatsoever.

We decided to do it with compiler compiler technology using lex/yacc
kind of tools. We had access to a partial cobol syntax. This solution
was in our eyes more flexibile and extendible than a hand written
parser/checker.

› Well, I did have to make two changes in the COBOL hosted COBOL checker
› when I ported it to Realia COBOL 4.2.  I had to set the compile-time
…[3 more quoted lines elided]…
› change which worked perfectly in either environment.
 
› Of course, I have no familiarity with Flex and Bison, so I wrote a
› monolithic COBOL program (now up to 6000 lines) with an integrated
…[3 more quoted lines elided]…
› produces a report like a compile listing with diagnostic messages.
 
› So, what's wrong with writing a COBOL checker in COBOL?

Nothing's wrong, we just thought that we would get a better
maintainable tool using our way. This decision was also based on
testimonies of previous experiences in other companies.

› Arnold Trembley
› Software Engineer I (just a job title, still a programmer)
› MasterCard International
› St. Louis, Missouri

Best regards,

Bruno
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "f 6419 mr john h lindsay" <ua-author-17086389@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c6aafb58b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c6aafb58b-p3@usenetarchives.gap>`
- **References:** `<557d09$98m@news1.Belgium.EU.net> <gap-5c6aafb58b-p2@usenetarchives.gap> <gap-5c6aafb58b-p3@usenetarchives.gap>`

```

Bruno Peeters wrote:
› 
› arn··.@wor··t.net (Arnold J. Trembley) wrote:
…[6 more quoted lines elided]…
› kind of tools. 

[Big snip]

Do consider either Snobol4 or Icon. Snobol4 is cheap enough, and runs
on
several platforms (the same source codes on them all!). Ask Catspaw
Computing for details. Icon is FREE, yes $0; download it for just about
as many platforms from Arizona U or Hobbes. The genius of both of them
is
string and data structure handling, and once you start using either,
you'll
wonder why on earth everybody doesn't rave about them. Actually,
they've
been beautifully hidden for years by putting them out in the open where
everybody can get and use them.

There are lots of routines in the Icon library for syntax analysis, and
just
about as many out there in various places for Snobol4. Icon is a
delight to
code, and Snobol4, once you get the hang of it, is an equal delight.

Check out the FAQ in comp.lang.icon.

John H. Lindsay (lin··.@r··.ca)
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c6aafb58b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c6aafb58b-p3@usenetarchives.gap>`
- **References:** `<557d09$98m@news1.Belgium.EU.net> <gap-5c6aafb58b-p2@usenetarchives.gap> <gap-5c6aafb58b-p3@usenetarchives.gap>`

```

bru··.@gkb··b.be (Bruno Peeters) wrote:

› arn··.@wor··t.net (Arnold J. Trembley) wrote:
 
›› Why don't you write the checker program in COBOL in the MVS
›› environment?  I did this for my company in 1991.  I was able to port
›› it to Realia COBOL V4.2 for DOS and OS/2 with no changes whatsoever.
 
› We decided to do it with compiler compiler technology using lex/yacc
› kind of tools. We had access to a partial cobol syntax. This solution
› was in our eyes more flexibile and extendible than a hand written
› parser/checker.
 
› Best regards,
 
› Bruno

Bruno, did you get any good solutions to your EBCDIC to ASCII
conversion problems?

I hope you have a successful product. I'm in favor of anything that
helps programmers write better COBOL programs.

Best wishes.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "vadim maslov" <ua-author-9434762@usenetarchives.gap>
- **Date:** 1996-11-11T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c6aafb58b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c6aafb58b-p3@usenetarchives.gap>`
- **References:** `<557d09$98m@news1.Belgium.EU.net> <gap-5c6aafb58b-p2@usenetarchives.gap> <gap-5c6aafb58b-p3@usenetarchives.gap>`

```

In article <55q1eu$6.··.@new··U.net>,
Bruno Peeters wrote:
› arn··.@wor··t.net (Arnold J. Trembley) wrote:
› 
…[8 more quoted lines elided]…
› 

I also do parsing with compiler technology, namely,
with btyacc -- backtracking yacc. You cannot parse COBOL with regular
yacc, cause you need to go back from time to time.
COBOL is such a language where standard yacc lookahead of 1
is not sufficient. I have 6 or 7 documented cases
where lookahead of 2 is needed.

In general, it took me a long time to write a decent lexer and parser,
and, as you may have guessed, lexer is more complicated than parser.
I would not dare to do it in lex -- there are many issues involved
(like COPY statements) that lex is not even close to handling.
Then syntax and lexics are too interconnected in COBOL
(consider PICTURE strings, for example). So, maybe, flex
will do the job, but, the part that flex can do is so puny
that I did not bother use lex/flex at all.

Anyway, I am writing all this to attract your attention to the fact
that I am selling a result of my work -- lexer and parser --
to companies like yours who want to enforce standards or are
in some kind of reengineering business.

The price is $1995 and the license allows for using the source
without reselling it or repackaging it.

That is, use it to get your job done, and don't invent
the wheel -- COBOL parser, that is.


Vadim Maslov
Siber Systems
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
