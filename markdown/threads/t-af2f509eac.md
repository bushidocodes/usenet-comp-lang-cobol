[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migration tool for moving to LE?

_4 messages · 4 participants · 1999-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Migration tool for moving to LE?

- **From:** tony.granata@gecapital.com
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77imgo$2r5$1@nnrp1.dejanews.com>`

```
  I was wondering if anyone out there knows of a tool that will scan COBOL
source and determine what changes will be necessary so that the module(s) in
question will compile under the LE environment.  Of particular interest is a
tool that will do this for both COBOL II and pre-COBOL II source modules.

  Please reply to tony.granata@gecapital.com

  Thanks.


-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Migration tool for moving to LE?

- **From:** Paul Hardy <paul.hardy.uhold@pwgsc.gc.ca>
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369CE1B8.9C5EB5E7@pwgsc.gc.ca>`
- **References:** `<77imgo$2r5$1@nnrp1.dejanews.com>`

```
Here we used a product call CCCA;

COBOL and CICS/VS command level Conversion Aid

Paul

tony.granata@gecapital.com wrote:

>   I was wondering if anyone out there knows of a tool that will scan COBOL
> source and determine what changes will be necessary so that the module(s) in
…[8 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Migration tool for moving to LE?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77lll1$fec@dfw-ixnews3.ix.netcom.com>`
- **References:** `<77imgo$2r5$1@nnrp1.dejanews.com>`

```
Another post mentions CCCA (also available - I think - as part of IBM's
professional edition (name?) PC product).  You will also want to look at a
program like Edge's Portfolio - for figuring out link-edit and other
inter-program issues (IMHO).
```

#### ↳ Re: Migration tool for moving to LE?

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369e8424$2$tfs$mr2ice@news>`
- **References:** `<77imgo$2r5$1@nnrp1.dejanews.com>`

```
In <77imgo$2r5$1@nnrp1.dejanews.com>, on 13 Jan 1999 at 17:52,
tony.granata@gecapital.com said:

>  I was wondering if anyone out there knows of a tool that will scan
>COBOL source and determine what changes will be necessary so that the
>module(s) in question will compile under the LE environment.  Of
>particular interest is a tool that will do this for both COBOL II and
>pre-COBOL II source modules.

There is about a dozen different tools that convert OS/VS COBOL (or DOS/VS
COBOL) to the current levels of COBOL (OS/390, VM and VSE).  Some of these
tools can also handle the conversion from VS COBOL II Release 2 (CMPR2) to
full ANSI 85 standard.  

If you don't use CMPR2 in COBOL II, converting the code to a more recent
level of COBOL is only a matter of changing two reserved words (one is
FUNCTION, the other is quite obscure and I can't think of it at the
moment).  There could be run-time problems when going from COBOL II to
COBOL for MVS though, but it's a different story.

Our company (AMS) provides conversion services (mostly VSE/MVS and COBOL)
using our own tools, which have been designed to perform "en masse", as
opposed to more traditional tools which process one program at a time. 
This allows us to convert, compile and link-edit up to 2000 programs an
hour: give us an entire inventory (1000s of programs, COPY books, etc) on
wednesday night, and your programmers can have a complete, consistent, set
of converted source and load-modules ready for testing thursday morning.

I you have any question, don't hesitate to contact me.

 Gilbert Saint-flour
 Technical Manager
 Automated Migration Services
 http://ams.atstaffing.com/ams/ams.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
