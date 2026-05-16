[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convert Rpt Carriage control?

_5 messages · 5 participants · 2002-03_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Convert Rpt Carriage control?

- **From:** fir@eskimo.com (Fir)
- **Date:** 2002-03-11T17:27:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6ipet$q1t$1@eskinews.eskimo.com>`

```
Converting VS Cobol pgms to Cobol 390 on IBM Mainframe.

These old batch report programs fill the first character 
of report lines with a carriage control figure and do a
write after positioning.  I'm looking to convert those
carriage control characters to "write after page", 
"write after 1", etc.

Is there a translation table somewhere for that carriage control
character in the first position of a report line?

Thank you.
```

#### ↳ Re: Convert Rpt Carriage control?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-11T13:22:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6j05h$61a$1@slb6.atl.mindspring.net>`
- **References:** `<a6ipet$q1t$1@eskinews.eskimo.com>`

```
Check your ADV/NOADV compiler option (on both the OLD and new compiler).
This works (basically) the same in all IBM mainframe compilers that I know
of.  If you set your compiler options correctly, you shouldn't need any
conversion.

NOTE: If you actually have OS/VS COBOL programs with
   WRITE ... AFTER POSITIONING

rather than AFTER ADVANCING, then you will want to look at the Migration
Guide at:

 http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3mg00/4.1.7?

for the section
 "WRITE AFTER POSITIONING statement"
```

#### ↳ Re: Convert Rpt Carriage control?

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-03-11T21:29:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6jsmj$gun$1@suaar1ab.prod.compuserve.com>`
- **References:** `<a6ipet$q1t$1@eskinews.eskimo.com>`

```
What I usually do with these things is just leave the carriage control alone.
Disturb the works as little as possible. Be sure you have NOADV when you compile.
Be sure you have RECFM=FBA in the JCL even if it's on a SYSOUT. Drop the
"after positioning" and just say "write record-name". It works the same.

Be glad you don't have any "before positioning" statements. It gets really fun then.

Anyway advancing,  '1' is top of page, space is 1 line, '0' is 2 lines, '-' is 3 lines.
There's a suppress advancing too, like "after advancing 0 lines". I'm not a 100%
sure but I think it must be a "+' sign.

=====================================================


"Fir" <fir@eskimo.com> wrote in message news:a6ipet$q1t$1@eskinews.eskimo.com...
> Converting VS Cobol pgms to Cobol 390 on IBM Mainframe.
>
…[9 more quoted lines elided]…
> Thank you.
```

##### ↳ ↳ Re: Convert Rpt Carriage control?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-03-13T00:50:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1ca29$0608e280$1634e641@chottel>`
- **References:** `<a6ipet$q1t$1@eskinews.eskimo.com> <a6jsmj$gun$1@suaar1ab.prod.compuserve.com>`

```
My "green" card lists the following for ANSI-Defined printer control
characters:

  Code    Action before printing record

  blank    Space 1 line
  zero     Space 2 lines 
  -          Space 3 lines
  +         Suppress space
  1         Skip to line 1 on new page

Ron <NoSoy@swbell.net> wrote in article
<a6jsmj$gun$1@suaar1ab.prod.compuserve.com>...
> What I usually do with these things is just leave the carriage control
alone.
> Disturb the works as little as possible. Be sure you have NOADV when you
compile.
> Be sure you have RECFM=FBA in the JCL even if it's on a SYSOUT. Drop the
> "after positioning" and just say "write record-name". It works the same.
> 
> Be glad you don't have any "before positioning" statements. It gets
really fun then.
> 
> Anyway advancing,  '1' is top of page, space is 1 line, '0' is 2 lines,
'-' is 3 lines.
> There's a suppress advancing too, like "after advancing 0 lines". I'm not
a 100%
> sure but I think it must be a "+' sign.
> 
…[3 more quoted lines elided]…
> "Fir" <fir@eskimo.com> wrote in message
news:a6ipet$q1t$1@eskinews.eskimo.com...
> > Converting VS Cobol pgms to Cobol 390 on IBM Mainframe.
> >
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Convert Rpt Carriage control?

- **From:** "ups" <upsi@hotmail.com>
- **Date:** 2002-03-13T03:12:53+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c8f8e81@news.alphalink.com.au>`
- **References:** `<a6ipet$q1t$1@eskinews.eskimo.com>`

```
Consider looking to see what channels have been defined in the FCB,
in case the program requires more than just channel "1".

If  the DCB shows "M" rather than "A" for the printer control (eg FBM rather
than FBA),
it may be using machine (ie printer) internal codes rather than ANSI control
codes.

I seem to remember having to look these up in a manual once,
but it was far too long ago for me to remember which one.

Just a thought, it probably doesn't apply - you would have to be very
unlucky to strike this.


"Fir" <fir@eskimo.com> wrote in message
news:a6ipet$q1t$1@eskinews.eskimo.com...
> Converting VS Cobol pgms to Cobol 390 on IBM Mainframe.
>
…[9 more quoted lines elided]…
> Thank you.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
