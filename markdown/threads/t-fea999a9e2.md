[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Cobol With DLI/CICS Integrated Translator

_3 messages · 2 participants · 2004-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-17T01:09:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-E7D665.01090917092004@knology.usenetserver.com>`

```
Bill,

I can not find anyplace where IBM comes out and says DYNAM with DLI/BMP 
is supported.  As far as I have been able to find out, batch BMP regions 
(no mention of DLI) are/were supported with DYNAM.  But when using DLI  
it becomes quite silent, as you noted.

Every place IBM says they require NODYNAM is qualifed with CICS somehow.

I've tried compiling numerous ways.  That translation seems to go fine, 
but there seems to be a totally separate check for the CICS() option 
that will always turn on NYDYNAM.  Nothing worked.  I couldn't even get 
the EXCI option to run at all.

Do you know of other places impacted by this problem?
```

#### ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-09-17T18:32:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85G2d.1535724$y4.267902@news.easynews.com>`
- **References:** `<joe_zitzelberger-E7D665.01090917092004@knology.usenetserver.com>`

```
Joe,
   I don't personally know of any other shops impacted by this.  I did find one 
thing that *might* be relevant.  At:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfsaptf5/1.5.9.5

it says,  (referring to programs using CALL "CBLTDLI"

"If the COBOL compiler option NODYNAM is specified, you must link edit the 
language interface module, DFSLI000, with your compiled COBOL application 
program. If the COBOL compiler option DYNAM is specified, do not link edit 
DFSLI000 with your compiled COBOL program."

This certainly means that *other* types of IMS programs support DYNAM.

This, along with the fact that using the separate translator and the 
CICS(DLI,NOCBLCARD,NOLINKAGE) options allows for DYNAM makes me think this is a 
VERY reasonable requirement for IBM to "fix".

I suggest creating a SHARE requirement.  Roland already created a requirement 
against the integrated coprocessor supporting CICS(EXCI).  He submitted his 
requirement against CICS - but there weren't many votes on it.  I would suggest 
that you create this against COBOL.  Clearly it would require work from BOTH 
products development teams.

Also, if you are one of the shops that is lucky enough to have a "marketing" 
branch, you can/should create a "REQUEST" for it there.

For the time being, I suggest you just keep using the separate translator step.
```

##### ↳ ↳ Re: IBM Cobol With DLI/CICS Integrated Translator

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-17T20:21:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-847B04.20215617092004@knology.usenetserver.com>`
- **References:** `<joe_zitzelberger-E7D665.01090917092004@knology.usenetserver.com> <85G2d.1535724$y4.267902@news.easynews.com>`

```
I've never opened a SHARE requirement -- how do I go about doing that?

I think perhaps it might become a non-issue at my shop.  After some 
discussion we have identified ways to prevent unwanted static calls 
(e.g. not IMS, MQ, CICS, DB2 stubs) from entering the source control 
system.

So it will still be a pain, but it will not be a dangerous pain.

I do get the feeling that IBM is taking something away from us here.  
We've use EXEC DLI in BMPs for over a decade.  Though I was not there at 
the begining, some of the old-timers have said that it was IBM that 
originally suggested we use EXEC DLI in BMPs.

I appreciate your help with all of this.



In article <85G2d.1535724$y4.267902@news.easynews.com>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> Joe,
>    I don't personally know of any other shops impacted by this.  I did find 
…[54 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
