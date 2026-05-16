[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Job Control Language

_9 messages · 6 participants · 2002-02_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### Job Control Language

- **From:** "Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk>
- **Date:** 2002-02-07T20:19:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xjB88.5742$H9.1121688@news1.cableinet.net>`

```
Hi,
    Can anyone tell me anything about job control language, in the context
of which is the most widely used, I briefly encountered MVS/JCL whilst
learning COBOL at college but the material on it didnt go too deep. Whose
job is it to program JCL statements? Can anybody recommend a good book, with
a couple of examples, on the subject.

Thanks for your help
Bloggs
```

#### ↳ Re: Job Control Language

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2002-02-07T21:01:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net>`

```
In article <xjB88.5742$H9.1121688@news1.cableinet.net>, Bloggs
<bloggs.barney@NOSPAMblueyonder.co.uk> writes
>Hi,
>    Can anyone tell me anything about job control language, in the context
>of which is the most widely used, I briefly encountered MVS/JCL whilst
>learning COBOL at college but the material on it didnt go too deep.
JCL is a set of directions to the operating system by which you can
control the system. Essentially, and briefly, JCL links programs (on
EXEC statements) to the following datasets (on DD statements). There is
something called JES (usually JES 2 or JES 3) which permit further
control via statements like /*JOBPARM L=10. 

> Whose
>job is it to program JCL statements? 
Mine, yours and ops analysts. In most shops where I have worked, I was
responsible for writing new and amended JCL for live (production)
systems. I was also responsible for writing all test JCL. Only in one
shop has an ops analyst stepped in and done the live production work for
new systems only. So learn it.

>Can anybody recommend a good book, with
>a couple of examples, on the subject.
Wiley do a good MVS/JCL book. Sorry I don't know the name of it.
However, other posts on this news group have mentioned other books in
recent weeks. The best JCL book, IMHO, is the JCL manual. It contains
examples, too.

>
>Thanks for your help
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Job Control Language

- **From:** "Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk>
- **Date:** 2002-02-07T21:17:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z9C88.6055$H9.1134479@news1.cableinet.net>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk>`

```
Thanks Alistair :>)

Much appreciated reply.
 Bloggs.

"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk...
> In article <xjB88.5742$H9.1121688@news1.cableinet.net>, Bloggs
> <bloggs.barney@NOSPAMblueyonder.co.uk> writes
> >Hi,
> >    Can anyone tell me anything about job control language, in the
context
> >of which is the most widely used, I briefly encountered MVS/JCL whilst
> >learning COBOL at college but the material on it didnt go too deep.
…[47 more quoted lines elided]…
> (Throne of Blood, Akira Kurosawa)


---
Outgoing mail is certified Virus Free.
The sender accepts no responsibility for viruses not detected.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.320 / Virus Database: 179 - Release Date: 30/01/2002
```

###### ↳ ↳ ↳ Re: Job Control Language

- **From:** "Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk>
- **Date:** 2002-02-07T22:18:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2D88.6282$H9.1152316@news1.cableinet.net>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net>`

```
Alistair,
        Do you reckon the JCL Users Guide at
http://gozips.uakron.edu/is/clientserv/mvshelp/jcl/ is any good. I found it
on a search at Google just after I posted the question on this ng.
Interested in your opinion. Much appreciated.
Bloggs.
"Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk> wrote in message
news:z9C88.6055$H9.1134479@news1.cableinet.net...
> Thanks Alistair :>)
>
…[68 more quoted lines elided]…
>


---
Outgoing mail is certified Virus Free.
The sender accepts no responsibility for viruses not detected.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.320 / Virus Database: 179 - Release Date: 30/01/2002
```

###### ↳ ↳ ↳ Re: Job Control Language

_(reply depth: 4)_

- **From:** kedarnj@hotmail.com (Kedar)
- **Date:** 2002-02-08T01:48:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d5258c4e.0202080148.2e15ec7c@posting.google.com>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net> <D2D88.6282$H9.1152316@news1.cableinet.net>`

```
Boggs, what platform do you work on? If you are interested in knowing
about JCL I don't mind, but I think it would be hardly of any
practicle use if you are not working of OS/390. Anyways the following
link should be helpful..

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/iea1b540/CCONTENTS
 
This is the JCL user's guide. 

"Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk> wrote in message news:<D2D88.6282$H9.1152316@news1.cableinet.net>...
> Alistair,
>         Do you reckon the JCL Users Guide at
…[3 more quoted lines elided]…
> Bloggs.
```

###### ↳ ↳ ↳ Re: Job Control Language

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-02-08T13:53:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12321C967241E1B6.C7B712A35E1DB8C9.44DD456E88DE584A@lp.airnews.net>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net> <D2D88.6282$H9.1152316@news1.cableinet.net> <d5258c4e.0202080148.2e15ec7c@posting.google.com>`

```
On 8 Feb 2002 01:48:35 -0800, kedarnj@hotmail.com (Kedar) enlightened
us:

>Boggs, what platform do you work on? If you are interested in knowing
>about JCL I don't mind, but I think it would be hardly of any
…[13 more quoted lines elided]…
>> Bloggs.

As for books on the subject, go to Amazon.com and do a search on MVS
JCL or VSE JCL and a list of books should come back.  Best MVS book
I've used is by Doug Lowe who has written many technical books.  You
could do a search on his name as well.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I don't have a big ego, I'm way too cool for that.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Job Control Language

_(reply depth: 6)_

- **From:** "Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk>
- **Date:** 2002-02-10T14:53:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hPv98.19217$H9.2447741@news1.cableinet.net>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net> <D2D88.6282$H9.1152316@news1.cableinet.net> <d5258c4e.0202080148.2e15ec7c@posting.google.com> <12321C967241E1B6.C7B712A35E1DB8C9.44DD456E88DE584A@lp.airnews.net>`

```
Thanks everyone for your help, it is much appreciated.
Bloggs.
"SkippyPB" <swiegand@neo.rr.com> wrote in message
news:12321C967241E1B6.C7B712A35E1DB8C9.44DD456E88DE584A@lp.airnews.net...
> On 8 Feb 2002 01:48:35 -0800, kedarnj@hotmail.com (Kedar) enlightened
> us:
…[7 more quoted lines elided]…
>http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/iea1b540/CCONTEN
TS
> >
> >This is the JCL user's guide.
> >
> >"Bloggs" <bloggs.barney@NOSPAMblueyonder.co.uk> wrote in message
news:<D2D88.6282$H9.1152316@news1.cableinet.net>...
> >> Alistair,
> >>         Do you reckon the JCL Users Guide at
> >> http://gozips.uakron.edu/is/clientserv/mvshelp/jcl/ is any good. I
found it
> >> on a search at Google just after I posted the question on this ng.
> >> Interested in your opinion. Much appreciated.
…[18 more quoted lines elided]…
> Steve


---
Outgoing mail is certified Virus Free.
The sender accepts no responsibility for viruses not detected.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.323 / Virus Database: 180 - Release Date: 08/02/2002
```

###### ↳ ↳ ↳ Re: Job Control Language

_(reply depth: 7)_

- **From:** Rick Overmaat <rover@none.nl>
- **Date:** 2002-02-11T03:41:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C672F50.97AE438@none.nl>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net> <D2D88.6282$H9.1152316@news1.cableinet.net> <d5258c4e.0202080148.2e15ec7c@posting.google.com> <12321C967241E1B6.C7B712A35E1DB8C9.44DD456E88DE584A@lp.airnews.net> <hPv98.19217$H9.2447741@news1.cableinet.net>`

```
Hi Bloggs,

I was amused when I read your questions and the answers.
As an experienced and well taught COBOL programmer, I would like
to add some general outlines.

Job Control Language (JCL) is the script language that belongs to
the standard operating systems of IBM mainframe (nowadays OS/390).
A mainframe is a very powerful type of computer. Most of the COBOL
programs on planet earth will be found on IBM mainframe, I guess.

But there are others:
CL (Control Language) for IBM's OS/400, the operating system of the
AS/400;
DCL (Digital Control Language) for Open VMS, the operating system of
DEC VAX and its successor, the Alpha;
and probably some more.

What do they do?
Suppose that you made a COBOL program called INVOICING.
The input comes from a file called SALES and the output is a file
called INVOICES.
In the ENVIRONMENT DIVISION you coded:
SELECT IN-SALES ASSIGN TO SALES
SELECT OUT-INVOICE ASSIGN TO INVOICES
IN-SALES and OUT-INVOICE are the names you prefer to use in your COBOL
program. But the script "knows" them as SALES and INVOICES.
The script then looks a bit like this:
   make memory for file SALES
   make memory for file INVOICES
   run INVOICING using input SALES output INVOICES
The user will not run your program INVOICING, but the script.

Do I need to have knowledge of them as a programmer? Well, often
I have to. How do you get the knowledge? From books and from having
a good look at existing scripts in the systems which I maintain.
Also from colleagues.

You wrote that you only received a rather superficial COBOL course,
at college. Then don't worry. If once you have to work professionally
with COBOL, there will be many things to learn. Not only the script
language of the operating system, but also file handling and screen
handling as they work on that OS.

For the OS that we started with, IBM's mainframe, for example,
this means: the about 450 pages book by Lowe on JCL, additional
information about the many MVS utilities, two equally big books on
DB2 file handling, two equally big book on IMS file handling, about
one book on VSAM files including AMS, and two on CICS screen handling,
if possible with good courses on all of these items.

So just finish college, I would say, and leave the rest to future and
fate  ;-)

Bye,
Rick

Bloggs wrote:
> 
> Thanks everyone for your help, it is much appreciated.
…[49 more quoted lines elided]…
> Version: 6.0.323 / Virus Database: 180 - Release Date: 08/02/2002
```

###### ↳ ↳ ↳ Re: Job Control Language

_(reply depth: 7)_

- **From:** "turin poste 10" <stage1@sb.tm.fr>
- **Date:** 2002-02-20T14:15:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a507ju$bro$1@s1.read.news.oleane.net>`
- **References:** `<xjB88.5742$H9.1121688@news1.cableinet.net> <ie0BVBAzsuY8EwsS@ld50macca.demon.co.uk> <z9C88.6055$H9.1134479@news1.cableinet.net> <D2D88.6282$H9.1152316@news1.cableinet.net> <d5258c4e.0202080148.2e15ec7c@posting.google.com> <12321C967241E1B6.C7B712A35E1DB8C9.44DD456E88DE584A@lp.airnews.net> <hPv98.19217$H9.2447741@news1.cableinet.net>`

```

Bloggs <bloggs.barney@NOSPAMblueyonder.co.uk> a �crit dans le message :
hPv98.19217$H9.2447741@news1.cableinet.net...
> Thanks everyone for your help, it is much appreciated.
> Bloggs.
…[52 more quoted lines elided]…
>I don't understand  what you say.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
