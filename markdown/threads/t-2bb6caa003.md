[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Questions About COBOL 85

_4 messages · 4 participants · 1996-05_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Questions About COBOL 85

- **From:** "tony..." <ua-author-17087342@usenetarchives.gap>
- **Date:** 1996-05-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<319D9AAF.1064@singnet.com.sg>`

```

Hi everyone, I have a few interesting questions about COBOL 85.

1. Does COBOL 85 allow you to skip the inital paragraph name after the
PROCEDURE DIVISION?

eg PROCEDURE DIVISION.
OPEN INPUT ...
200-PROCESSING.

2. Is it "better" to have the INITIAL clause in the Program-ID when I
code a Called Program?

I am doing a project right now and there're mysterious happenings like
programs running okay alone by itself but when linked, it abends and
when a program is supposed to return control to a main menu, it goes out
to the OS.

Regards

Anthony
```

#### ↳ Re: Questions About COBOL 85

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-05-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bb6caa003-p2@usenetarchives.gap>`
- **In-Reply-To:** `<319D9AAF.1064@singnet.com.sg>`
- **References:** `<319D9AAF.1064@singnet.com.sg>`

```

Robert Mala wrote:

› However in a CICS environment the subprogram does not form part of the
› run unit if it is XCTLed too. As such the WS is not maintained. I'm
› unsure if this is the case when a program is LINKed too under CICS.
›

If I am wrong, I am sure someone will correct me. But I am pretty
certain it makes no difference whether you EXEC CICS XCTL to another
program or EXEC CICS LINK to it -- either way, the called program gets a
fresh copy of its working-storage.

The only difference is that if you LINK to the program, an EXEC CICS
RETURN takes you back to the program that LINK'ed to you, and if you got
there by an XCTL (transfer control) a CICS return takes you back to CICS,
therefore terminating you CICS transaction.

So you could say that a CICS program has an implied IS INITIAL in it.

Arnold Trembley
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Questions About COBOL 85

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-05-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bb6caa003-p3@usenetarchives.gap>`
- **In-Reply-To:** `<319D9AAF.1064@singnet.com.sg>`
- **References:** `<319D9AAF.1064@singnet.com.sg>`

```

Lots of dependancies on a particular implementation.

Some things are required in strict 85 COBOL, but are allowed in particular
implementations.

"Better" is relative, and again is dependant on implementation and even
options.

You could probably get much better answers by including environment - op
sys and compiler info.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Questions About COBOL 85

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-05-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bb6caa003-p4@usenetarchives.gap>`
- **In-Reply-To:** `<319D9AAF.1064@singnet.com.sg>`
- **References:** `<319D9AAF.1064@singnet.com.sg>`

```

In message <<319··.@sin··m.sg>> ton··.@sin··m.sg writes:
› 
› 1.  Does COBOL 85 allow you to skip the inital paragraph name after the
…[5 more quoted lines elided]…
› 
 
› Yes
 
› 2.  Is it "better" to have the INITIAL clause in the Program-ID when I 
› code a Called Program?
› 

That depends entirely on what the sub-program is doing. If it is
CALLed once then CANCELed it makes no difference. If it is CALLed
repeatedly and these expect the last-used state to apply then
do not use INITIAL. I have 'service' routines in my systems that
open files on the first call and then only close them when called
with a 'Z' parameter. Each other call expects the files to be open
as these are for accessing the control files.

The INITIAL clause would make these fail.

› I am doing a project right now and there're mysterious happenings like 
› programs running okay alone by itself but when linked, it abends and 
› when a program is supposed to return control to a main menu, it goes out 
› to the OS.

Perhaps you are not using EXIT PROGRAM or GOBACK.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
