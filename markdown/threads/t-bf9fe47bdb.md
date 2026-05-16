[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help, Realia Cobol problem with "ACCEPT" (from DOS screen)

_4 messages · 3 participants · 2006-10 → 2007-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Help, Realia Cobol problem with "ACCEPT" (from DOS screen)

- **From:** "Joe M" <joemagiera@ameritech.net>
- **Date:** 2006-10-14T20:09:36+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<4ubYg.14820$6S3.7198@newssvr25.news.prodigy.net>`

```
I'm running Realia Cobol, version 4.201.  Things were fine and then I had a 
hard drive crash so I had to reload everything.  Now programs will still 
compile and run, but anything that asks for input via the ACCEPT verb from 
the dos screen window just hangs the system, I have to alt-ctrl-delete and 
kill the task.  I stripped the program down to the simplest version and the 
display's work fine, but the accept's just hang it.  The compile and link 
work fine.  I can run other programs with no problems, just accept's are not 
working.  Any ideas?  Here's an example of what will no longer work:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST2.
       AUTHOR.  JOE.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  FILLER.
           05  FILE-PATH                       PIC X(18).
           05  WS-IN-FILE-NAME                 PIC X(36) VALUE SPACES.
       PROCEDURE DIVISION.
       000-EXECUTIVE.
           DISPLAY 'ENTER FILE PATH'.
           ACCEPT FILE-PATH.
           STRING 'C:\FILE\' DELIMITED BY SIZE
               FILE-PATH DELIMITED BY SPACES
               '\FILE1.TXT' DELIMITED BY SIZE
                   INTO WS-IN-FILE-NAME.
           DISPLAY 'INPUT FILE NAME = ' WS-IN-FILE-NAME.
           GOBACK.

Am I missing some environmental variable somewhere in my autoexec.bat or 
something?  Please help, this is getting me crazy.  Thanks,

Joe (joemagiera at ameritech dot net)
joemagiera@ameritech.net
```

#### ↳ Re: Help, Realia Cobol problem with "ACCEPT" (from DOS screen)

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2007-07-19T08:35:41-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<ztGdnb7078X4wQLbnZ2dnUVZ_vihnZ2d@adelphia.com>`
- **References:** `<4ubYg.14820$6S3.7198@newssvr25.news.prodigy.net>`

```
Joe M wrote:

> DISPLAY 'INPUT FILE NAME = ' WS-IN-FILE-NAME.
> GOBACK.

Got it working in htcobol too. Your code is OK.  See previous suggestion.
```

#### ↳ Re: Help, Realia Cobol problem with "ACCEPT" (from DOS screen)

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2007-07-19T08:50:59-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<jOudnapIArBkwgLbnZ2dnUVZ_s3inZ2d@adelphia.com>`
- **References:** `<4ubYg.14820$6S3.7198@newssvr25.news.prodigy.net>`

```
Joe M wrote:

> I'm running Realia Cobol, version 4.201.  Things were fine and then I had
> a
…[37 more quoted lines elided]…
> joemagiera@ameritech.net
Works fine on Linux using Open Cobol. Had an obscure error in Tiny Cobol.
I would either reinstall Realia COBOL from original media or consider
switch to Open Cobol. 
```

##### ↳ ↳ Re: Help, Realia Cobol problem with "ACCEPT" (from DOS screen)

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-20T08:39:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184945999.458724.17410@n60g2000hse.googlegroups.com>`
- **In-Reply-To:** `<jOudnapIArBkwgLbnZ2dnUVZ_s3inZ2d@adelphia.com>`
- **References:** `<4ubYg.14820$6S3.7198@newssvr25.news.prodigy.net> <jOudnapIArBkwgLbnZ2dnUVZ_s3inZ2d@adelphia.com>`

```
On 19 Jul, 13:50, John Culleton <j...@wexfordpress.com> wrote:
> Joe M wrote:
> > I'm running Realia Cobol, version 4.201.  Things were fine and then I had
…[47 more quoted lines elided]…
> - Show quoted text -

Is Open Cobol a fully functional Cobol or is it a subset? I remember
being disppointed when looking at TinyCobol to find out that it seemed
to omit much of the basic functionality of Cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
