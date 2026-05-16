[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Tools" for COBOL FAQ

_7 messages · 7 participants · 2002-03_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### "Tools" for COBOL FAQ

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-08T21:45:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```
Dear CLC readers,

Among the notes in my (long) "to do" list was the following:

"Hello,
We've read your nice site.

At the moment we're working on few projects to convert cobol textual reports
to PDFs using our tools

txt2pdf

    http://www.sanface.com/txt2pdf.html

txt2pdf PRO

    htp://www.sanface.com/txt2pdfPRO.html

txt2pdf PRO + crypt

    http://www.sanface.com/txt2pdfPROcrypt.html

<snip>

Do you think your FAQ readers are interested to know of a similar
possibility?

We hope they're :)

<snip>"


  ***

I have just looked at their web-site and I don't see ANY references to
"COBOL".  On the other hand, I can (easily) imagine some COBOL
sites/programmers being interested in this type of "tool".

My question to CLC people is:

  Should I - or should I not - add "tools" that MIGHT be of interest, but
that don't actually "mention" COBOL in their own online documentation?  (I
have mixed feelings on this, but will "listen" to what others think)

Comments? Suggestions?
```

#### ↳ Re: "Tools" for COBOL FAQ

- **From:** Bernard Giroud <bgiroud@free.fr>
- **Date:** 2002-03-09T08:34:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C89BAE8.F393A149@free.fr>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```

"William M. Klein" a ï¿½crit :

> (...snip...)

> Do you think your FAQ readers are interested to know of a similar
> possibility?
…[18 more quoted lines elided]…
>

No, I think the file will be much too huge if every potentially interesting
tool is mentioned. Plus the fact that it will be harder to keep pace.

>
> --
> Bill Klein
>  wmklein <at> ix.netcom.com

Bernard Giroud
```

#### ↳ Re: "Tools" for COBOL FAQ

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-03-09T10:56:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mtoj8u80krjcjtlf16gook2p79dnkar7h0@4ax.com>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```
On Fri, 8 Mar 2002 21:45:34 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:
...
>
>I have just looked at their web-site and I don't see ANY references to
…[7 more quoted lines elided]…
>have mixed feelings on this, but will "listen" to what others think)
I think the following would be a good aproach on such decision.

1- If a product is one that is either written specifically to work
with COBOL, either by allowing an interaction with COBOL programs
(such as Flexus SP2) or with COBOL files (Liant's Relativity), or
supplies a set of "routines" that are called directly from COBOL using
normall "CALL" (I am ignoring OO for the moment) then I might include
it.

2- If it is only supplyed as a callable program (Perl on this case)
used as a "call "system" using command line" then I would not include
it.


I ignored OO, because in that case all applications that supply and
OCX/VBX/OLE aproach would be included. (and on this case it would be
better to include a link like
 "for more COBOL tools see www.tucows.com " !!!)


Just my 2 cent (Yes I also have them now)

Frederico Fonseca



Just as a minor note regarding the interest of PDF conversions there
is (at least) another company http://www.pdflib.com/ that supplies a
PDF tool that is included in option 1 above. (I have used it from
Liants'RM COBOL using normal call's to the supplied routines)
Example:
            call "PDF_translate"
                    USING P-PDF, temp1, temp1.
            call "PDF_setcolor"
                    USING P-PDF, "both", "rgb", 0, 0, 1, 0.
            call "PDF_save" USING P-PDF.
            call "PDF_setlinewidth" USING P-PDF, 2.
            perform varying temp1 from 0 by 6 until temp1 > 354
                call "PDF_rotate" USING P-PDF, 6
                call "PDF_moveto" USING P-PDF, radius, 0
                call "PDF_lineto" USING P-PDF, temp2, 0
                call "PDF_stroke" USING P-PDF
            end-perform.
```

#### ↳ Re: "Tools" for COBOL FAQ

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2002-03-09T11:11:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uZtFYCAa3ei8Ewd5@ld50macca.demon.co.uk>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```
Yes, please add tools to the FAQ. You could add Cobolscript to your
list.

In article <a6c0h7$otu$1@slb7.atl.mindspring.net>, William M. Klein
<wmklein@nospam.ix.netcom.com> writes
>Dear CLC readers,
>
…[48 more quoted lines elided]…
>
```

#### ↳ Re: "Tools" for COBOL FAQ

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-10T02:51:12+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c8a1538_6@Usenet.com>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:a6c0h7$otu$1@slb7.atl.mindspring.net...
>
> At the moment we're working on few projects to convert  *** cobol***
textual reports
> to PDFs using our tools
>
My vote says the word COBOL must be included SOMEWHERE.

In this case, it is (my asterisks), so I reckon this one passes.

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: "Tools" for COBOL FAQ

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-03-10T08:06:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020310030649.04468.00000670@mb-ms.aol.com>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net>`

```
>From: "William M. Klein" wmklein@nospam.ix.netcom.com 
>Date: 3/8/02 10:45 PM Eastern Standard Time

>
>  Should I - or should I not - add "tools" that MIGHT be of interest, but
…[3 more quoted lines elided]…
>Comments? Suggestions?

I get the impression from the 'commercial' that in the case of a mainframe the
output would be written to a file instead of a sysout and then passed through
this tool to obtain a pdf file.  While not exactly using COBOL (seems any
language would do) there probably are those who program who would be interested
in such a thing and any help would be nice.  I think putting such tools that
help in the performance of our jobs in the FAQ would be beneficial.
```

##### ↳ ↳ Re: "Tools" for COBOL FAQ

- **From:** sanface@sanface.com (SANFACE Software)
- **Date:** 2002-03-12T06:40:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18712ccd.0203120640.195edd6b@posting.google.com>`
- **References:** `<a6c0h7$otu$1@slb7.atl.mindspring.net> <20020310030649.04468.00000670@mb-ms.aol.com>`

```
This is SANFACE Software point of view :)
Our tools are not specific made for Cobol.
In the same way our tools are not specific made for OpenVMS (they work
on OpenVMS only using the perl code) but official VMS FAQ cointain a
link to our tools http://www.openvms.compaq.com/wizard/openvms_faq.html
.

A lot of tools and libraries can allow you to create PDFs.
Few can allow you to convert your old textual reports with a simple
pipe (our tools supports STDIN and STDOUT) into a pdf like
http://www.sanface.com/pdf/heraldbill.pdf
You've simply to design the background layer and put your data on it.

Obviously it's our point of view.

SANFACE Software team

P.S. We'll wait for your answer to post announces of new release of
our tools into cobol newsgroup :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
