[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II to Enterprise COBOL

_3 messages · 3 participants · 2006-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL II to Enterprise COBOL

- **From:** dibalok@gmail.com
- **Date:** 2006-02-13T09:58:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139853521.553312.25920@g14g2000cwa.googlegroups.com>`

```
Hi,

I need to change the some 1000 Program from COBOL II to Enterprise
COBOL. What are the essential difference between COBOL II to Enterprise
COBOL. How much can it affect my code ?
(There are not much DB2,CICS in my code)

Thanks,
Dib
```

#### ↳ Re: COBOL II to Enterprise COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-13T22:41:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PW7If.45003$ct7.28014@fe12.news.easynews.com>`
- **References:** `<1139853521.553312.25920@g14g2000cwa.googlegroups.com>`

```
If you are using the NOCMPR2 compiler option with your VS COBOL II compiler and 
you are using the LE run-time (with RES) then you will probably find that there 
is almost NO change required.  (a few new reserved words, but not many).

If you are using the VS COBOL II run-time and/or the NORES option, then you will 
need to do LOTS of testing for both changed behavior and performance.

If you are using the CMPR2 compiler option, then there are a list of things you 
need to look for (and/or use the FLAGMIG compiler option).

Have you read the COBOL and LE migration guides?  If not, that is where you 
should start.
```

#### ↳ Re: COBOL II to Enterprise COBOL

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-02-13T14:49:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rtqdnSUB4dSbkGzeRVn-pQ@adelphia.com>`
- **In-Reply-To:** `<1139853521.553312.25920@g14g2000cwa.googlegroups.com>`
- **References:** `<1139853521.553312.25920@g14g2000cwa.googlegroups.com>`

```
dibalok@gmail.com wrote:

>Hi,
>
…[9 more quoted lines elided]…
>
Start here:
<http://www-306.ibm.com/software/awdtools/cobol/zos/library/>

Download the PDF copy of the Migration Guide, and read it.  Get the 
other documents as well, of course.

One determinant of how much trouble you may encounter is your shop's 
default compiler and run time options.
=====
Examples:
If you have used VS COBOL II to compile unconverted OS/VS COBOL source, 
you'll likely need to get a Language Conversion Program.  There is (or 
was) an offering of the Enterprise COBOL compiler that includes an 
excellent interactive debug tool, and an LCP.

If you have used the NORES option, you'll have to recompile with RES, or 
relinkedit your load modules to substitute Language Environment (LE) 
versions of the run time modules.

If you have routinely used certain COBOL verbs, or IBM extensions, you 
will have to get rid of some of them.  ALTER, EXAMINE, EXHIBIT, and 
TRANSFORM are examples of verbs that were carried into IBM compilers, 
that are not in Enterprise COBOL.

There are literally dozens, maybe hundreds, of possible stumbling 
blocks.  The best way, in my opinion, to deal with them is to (1) 
contact Carl Gehr, who posts in this group as "CG", and see about 
obtaining his company's toolset, or (2) start recompiling some of your 
programs, and see what happens when you try to execute them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
