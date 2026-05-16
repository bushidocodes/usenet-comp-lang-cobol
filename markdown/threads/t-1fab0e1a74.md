[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Cobol With DLI/CICS Integrated Translator

_6 messages · 4 participants · 2004-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM Cobol With DLI/CICS Integrated Translator

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-10T21:35:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`

```
A problem/question has come up that I have no answer to.  I'm wondering 
if any of you have a creative idea to fix this.

The translator for CICS and DLI commands is one in the same.  When using 
the old preprocessor version, one would pass the "XOPTS(CICS)" or 
"XOPTS(DLI)" options to control what it would translate.

With the new integrated translator, the XOPTS parm is gone.  Now we have 
the CICS/NOCICS option.  So to do DLI translation, one passes the parm 
"CICS(DLI,NOLINKAGE)".  And it will also do CICS translation for you.  
After all, the CICS parm is on.

My problem is that my shop uses a great number of batch IMS BMP 
programs.  When we try to compile a batch program that will interact 
with IMS, we have to pass the parm CICS(DLI,NOLINKAGE).

The integrated translator 'assumes' that we are doing CICS as well and 
insists that we turn on NODYNAM.  But, since the separate translator 
allowed XOPTS(DLI) with DYNAM, we have a huge number of programs that do 
"CALL 'pgmname' USING...".

We really do not want to staticly interconnect all of our 58,000 
modules.  

We also do not want to edit/recompile/migrate a large number of the 58k 
modules to convert the CALL '' to CALL varname.

Does anyone have any good ideas?
```

#### ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2004-09-10T23:40:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iq-dnXDKNLtJAN_cRVn-oA@adelphia.com>`
- **In-Reply-To:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`
- **References:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:

>A problem/question has come up that I have no answer to.  I'm wondering 
>if any of you have a creative idea to fix this.
…[28 more quoted lines elided]…
>
The Enterprise COBOL Programming Guide (I'm guessing that might be the 
version you're using) says that the separate pre-processor is still 
supported, but not recommended (for some valid reasons, but you 
susrvived for a long time using the pre-processor, from what your 
original post says).

It also says you should use the COBOL3 option, which will insert a CBL 
statement containing RENT,NODYNAM,LIB, but that you can defeat this by 
using an option NOCBLCARD.  Probably, you did some or all of this 
already, before starting to use the integrated pre-processor.

All that said, it appears that IBM does not expect to have the COBOL 
compiler see programs which contain EXEC DLI and no EXEC CICS.  And I 
freely admit that I'm no CICS expert.  My shop wrote IMS programs (we 
were an IMS shop, with a smattering of CICS) using CALL statements.  I 
only learned about EXEC DLI when we had to support a little mfg. shop in 
the company that had migrated up from VSE.  But I would have recommended 
against using EXEC DLI in programs that weren't CICS (in other words, 
batch IMS), because that usage made them CICS pre-processor dependent.

Maybe you should look into doing a mass conversion.  Isn't that a happy 
prospect?

Also, I feel that you should open a problem with IBM, saying that you 
need to be able to compile programs which contain no CICS, but do 
contain EXEC DLI.  They'll probably fix the integrated pre-processor in 
a future release, so that you can do what you used to do with the 
separate pre-processor.
```

#### ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-11T17:37:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccd6k09plf2a9mtbeespb1ojoth1f22ct2@4ax.com>`
- **References:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`

```
On Fri, 10 Sep 2004 21:35:30 -0400, Joe Zitzelberger
<joe_zitzelberger@nospam.com> wrote:

>A problem/question has come up that I have no answer to.  I'm wondering 
>if any of you have a creative idea to fix this.
…[25 more quoted lines elided]…
>Does anyone have any good ideas?

Write 'wrappers' with the same names as called programs. A wrapper
program simply issues a dynamic call to the real target program.

Alternatively, put all wrappers in a single program containing lots of
ENTRY statements. Link it explicitly in your compilation job.
```

#### ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-09-13T17:33:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yRk1d.715527$ic1.74419@news.easynews.com>`
- **References:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`

```
Joe,
  I have sent a note to one of my "usually reliable" sources for comment on 
this, but I don't know how this does (or doesn't) fit in with using the 
CICS(EXCI) translator option.

Currently IBM does not *SUPPORT* compiling with CICS(EXCI) and using the 
integrated co-processor.  However, it has been reported that (at least in most 
cases) it works.  You might want to try compiling with that and DYNAM, and see 
what happens.
```

##### ↳ ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-14T18:39:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-CDCF03.18392414092004@knology.usenetserver.com>`
- **References:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com> <yRk1d.715527$ic1.74419@news.easynews.com>`

```
That is a great idea, I'll give that a shot.  Thanks for your help Bill.

I'll also see if I cannot find some documentation on DLI for BMP 
supported with DYNAM.  I know we have done it for 10 years with great 
results, but I cannot actually say that it was ever 'supported' by IBM.


In article <yRk1d.715527$ic1.74419@news.easynews.com>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> Joe,
>   I have sent a note to one of my "usually reliable" sources for comment on 
…[45 more quoted lines elided]…
>
```

#### ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-09-13T22:18:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1p1d.1318121$y4.232367@news.easynews.com>`
- **References:** `<joe_zitzelberger-635570.21353010092004@knology.usenetserver.com>`

```
Joe,
  After some private discussion, the question has come up whether it EVER was 
supported to compile with
  CICS(DLI)
     or
  XOPTS(DLI)

and the COBOL DYNAM compiler option.

Can you find anywhere that actually documented this as "legal" (which is NOT to 
say that it might have worked).

http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/dfhp3a00/1.4.5.1.2

certainly seems as if it is saying that the translator *ALWAYS* required NODYNAM 
"for CICS programs - whatever that means)- although

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfsapce3/1.4.2.2

is "silent" on the issue.

Personally, my "perception" is that as the documentation never SAYS that it 
illegal to use DYNAM for an EXEC DLI program that is used as a BMP (or batch) 
and that does NOT use the "CICS" option, then I would call  it legal. On the 
other hand, if you can find anyplace that says it *is* legal, that might help.

Finally,
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/3.1.2

makes it pretty clear (to me) that AS OF TODAY, if you use the integrated 
translator (coprocessor) that you MUST use NODYNAM.  However, if you/we can find 
someplace that "documents" that the (separate) translator supported DYNAM, we 
might create a "reasonable" SHARE requirement to add this support (in the 
future).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
