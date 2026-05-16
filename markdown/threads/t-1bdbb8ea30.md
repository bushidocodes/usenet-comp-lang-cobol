[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol test suite from NIST

_5 messages · 4 participants · 2002-07_

---

### Cobol test suite from NIST

- **From:** "Holly Wilper" <holly.l.wilper@intel.com>
- **Date:** 2002-07-11T11:06:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agkalc$aoi@news.or.intel.com>`

```
I need a supply of Cobol tests. I downloaded the Cobol85 conformance suite
from NIST http://www.itl.nist.gov/div897/ctg/cobol_form.htm . Unfortunately
I've never used Cobol before in my life and I do not understand the
instructions for extracting the tests from the form. The site indicates:

"The COBOL Test Suite is a compressed file that must be extracted from a
UNIX system. Please rename the file as "filename" Z. To run the test suite,
you need to extract and set up the COBOL Executive routine program; execute
the COBOL Executive to select and prepare the test programs for compilation,
and then prepare the necessary job scripts to compile and execute the test
programs. "

It extracts into a single file and from there I am clueless. I extract it on
our UNIX system and then back over to Windows to try to compile with Fujitsu
Cobol for .NET, no go. I have tried to contact the contact person at NIST
listed on the page, but she has not returned my email (months ago).

Could anyone tell me how to extract this file to get individual Cobol tests?
Alternatively could you point me at another source for Cobol tests?

Thank you for your time and trouble.

Holly Wilper
```

#### ↳ Re: Cobol test suite from NIST

- **From:** docdwarf@panix.com
- **Date:** 2002-07-11T12:41:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agkcfe$li4$1@panix1.panix.com>`
- **References:** `<agkalc$aoi@news.or.intel.com>`

```
In article <agkalc$aoi@news.or.intel.com>,
Holly Wilper <holly.l.wilper@intel.com> wrote:
>I need a supply of Cobol tests. I downloaded the Cobol85 conformance suite
>from NIST http://www.itl.nist.gov/div897/ctg/cobol_form.htm . Unfortunately
>I've never used Cobol before in my life and I do not understand the
>instructions for extracting the tests from the form.

With all due respect... perhaps running such tests might not be the best 
place to start.

DD
```

##### ↳ ↳ Re: Cobol test suite from NIST

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2002-07-12T05:41:01+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2DDF4D.8AEAEEE2@melbpc.org.au>`
- **References:** `<agkalc$aoi@news.or.intel.com> <agkcfe$li4$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> In article <agkalc$aoi@news.or.intel.com>,
…[9 more quoted lines elided]…
> DD

The opencobol project on sourceforge.net has a Unix shell script to extract
the tests.

Tim Josling
```

##### ↳ ↳ Re: Cobol test suite from NIST

- **From:** "Holly Wilper" <holly.l.wilper@intel.com>
- **Date:** 2002-07-16T08:53:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ah18nu$bpt@news.or.intel.com>`
- **References:** `<agkalc$aoi@news.or.intel.com> <agkcfe$li4$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:agkcfe$li4$1@panix1.panix.com...
> In article <agkalc$aoi@news.or.intel.com>,
> Holly Wilper <holly.l.wilper@intel.com> wrote:
> >I need a supply of Cobol tests. I downloaded the Cobol85 conformance
suite
> >from NIST http://www.itl.nist.gov/div897/ctg/cobol_form.htm .
Unfortunately
> >I've never used Cobol before in my life and I do not understand the
> >instructions for extracting the tests from the form.
…[3 more quoted lines elided]…
>

Ordinarily that would certainly be true. For this application I need tests
in 8-10 languages to generate bytecode for further processing. Some of them
I am fluent in, some of them I have used, some of them I have never used.

Thanks to all for the help.

Holly Wilper
```

#### ↳ Re: Cobol test suite from NIST

- **From:** Bernard Giroud <bgiroud@free.fr>
- **Date:** 2002-07-11T21:34:54+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2DDDDE.829EB9C3@free.fr>`
- **References:** `<agkalc$aoi@news.or.intel.com>`

```
Holly Wilper a ï¿½crit :

> I need a supply of Cobol tests. I downloaded the Cobol85 conformance suite
> from NIST http://www.itl.nist.gov/div897/ctg/cobol_form.htm . Unfortunately
…[17 more quoted lines elided]…
>

Read the file Readme in
http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/tiny-cobol/development/test_suite/nist/
.
From there, you can use the tools from the same directory.

Alternatively, file README from
http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/cobol/cobol-testsuite/cobol85/,
thanks to Keisuke Nishida.

Hope this helps,

Bernard Giroud

>
> Thank you for your time and trouble.
>
> Holly Wilper
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
