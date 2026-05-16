[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# XML generate

_8 messages · 7 participants · 2007-10 → 2007-11_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### XML generate

- **From:** Pakku <pakku@soccermail.com>
- **Date:** 2007-10-26T20:08:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`

```
Platform z/OS Enterprise Cobol
Just testing the waters on creating XML output from some flat files.
Choice is to use XML GENERATE command or hand-code.

Are there any known problems with XML GENERATE? Frequently with a lot
of IBM's newer releases there are teething problems.

Would like some input from people who are using this in a production
environment.
```

#### ↳ Re: XML generate

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-27T21:58:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fwOUi.263258$zt4.58039@fe08.news.easynews.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`

```
I have heard of no problems - if by that you mean "bugs in what is documented". 
However, the feature is limited - to some extent.  There are issues with 
"attributes" , underscores vs hyphens, and some other XML features not supported 
by this syntax.  Some of this ("work-arounds")  is dealt with at:

  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg32/5.2.2

There may also be "encoding" (codepage) issues - which you will also need to 
understand.  (As I recall, there may be problems if your site doesn't have the 
correct conversion services defined).

NOTE:
  I have not personally used this facility, so this is just a report on what I 
have "heard".

NOTE 2:
   Other compilers on other platforms use very DIFFERENT approaches to COBOL and 
XML, so this solution is NOT necessarily portable - if this may matter to your 
site in the future.
```

#### ↳ Re: XML generate

- **From:** CG <Carl.Gehr.ButNoSPAMStuff5@MCGCG.Com>
- **Date:** 2007-10-27T21:31:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ad77$4723e686$d06620ed$4909@FUSE.NET>`
- **In-Reply-To:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`

```
On 10/26/07 11:08 pm, Pakku wrote:
> Platform z/OS Enterprise Cobol
> Just testing the waters on creating XML output from some flat files.
…[6 more quoted lines elided]…
> environment.

Like Bill, I cannot comment from personal experience using the XML 
support, but as far as "IBM's newer releases...problems," consider that 
XML GENERATE was added in V3.3 [GA Feb-2004] and the current compiler 
V3.4 was GA in Jul-2005 [updated to V3.4.1 for non-XML changes in 
May-2006].  So, it is not quite a 'new' release.  It's been out in the 
'real world' for over two years now.

Carl
```

#### ↳ Re: XML generate

- **From:** cschneid_google@yahoo.com
- **Date:** 2007-10-28T10:30:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193592636.448048.214050@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`

```
On Oct 26, 10:08 pm, Pakku <pa...@soccermail.com> wrote:
> Platform z/OS Enterprise Cobol
> Just testing the waters on creating XML output from some flat files.
…[6 more quoted lines elided]…
> environment.

Bill Klein has given you an excellent reference, there are also SHARE
presentations on and including the topic of XML GENERATE in IBM's
Enterprise COBOL.

Where I work, we use XML GENERATE in a production environment.  Our
difficulties and how we worked around them were presented at SHARE in
San Diego is session 8247, starting at (I believe) slide 32.  See
http://shareew.prod.web.sba.com/proceedingmod/index.cfm.

You might also be interested in session 8236 presented in Tampa Bay.

Both of these are currently available to the public, but I don't know
how long it will be before you will need a SHARE userID and password
to access them.


In my experience, the feature works as documented.
```

##### ↳ ↳ Re: XML generate

- **From:** Pakku <pakku@soccermail.com>
- **Date:** 2007-10-29T06:36:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193664980.188871.97490@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<1193592636.448048.214050@k79g2000hse.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com> <1193592636.448048.214050@k79g2000hse.googlegroups.com>`

```
On Oct 28, 1:30 pm, cschneid_goo...@yahoo.com wrote:
> On Oct 26, 10:08 pm, Pakku <pa...@soccermail.com> wrote:
>
…[24 more quoted lines elided]…
> In my experience, the feature works as documented.

Thanks all, just what I wanted to know.  My company's investment in
IBM Big Iron is significant enough and growing that, it is unlikely
they will change platforms.  But thanks for pointing it out, we will
put the XML generation part in a different program.
For instance I understand that the DataPower appliance can convert
unformatted flat file text to XML using copybooks very efficiently.
So if we decide to "farm out" XML generation from the application
programs, we just need to remove the program from the job.
Rgds
```

###### ↳ ↳ ↳ Re: XML generate

- **From:** Sudhir.Jarajapu@gmail.com
- **Date:** 2007-11-13T09:38:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194975514.979394.168280@o3g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1193664980.188871.97490@y42g2000hsy.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com> <1193592636.448048.214050@k79g2000hse.googlegroups.com> <1193664980.188871.97490@y42g2000hsy.googlegroups.com>`

```
On Oct 29, 8:36 am, Pakku <pa...@soccermail.com> wrote:
> On Oct 28, 1:30 pm, cschneid_goo...@yahoo.com wrote:
>
…[42 more quoted lines elided]…
> - Show quoted text -

Hello All,
Am also using the XML Generate feature from IBM Enterprise Cobol.
Am facing problems converting MiXeD case names to XML Tag names.
Strange!!

If anyone has similar problems, please post a reply and we will
discuss further.
```

###### ↳ ↳ ↳ Re: XML generate

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-11-14T04:46:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1195044407.905233.243250@o3g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1194975514.979394.168280@o3g2000hsb.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com> <1193592636.448048.214050@k79g2000hse.googlegroups.com> <1193664980.188871.97490@y42g2000hsy.googlegroups.com> <1194975514.979394.168280@o3g2000hsb.googlegroups.com>`

```
On 13 Nov, 17:38, Sudhir.Jaraj...@gmail.com wrote:
> On Oct 29, 8:36 am, Pakku <pa...@soccermail.com> wrote:
>
…[50 more quoted lines elided]…
>

XML tag names should be in lower case. Is that your problem?
```

#### ↳ Re: XML generate

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-11-14T01:00:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1195030808.719468.266780@v23g2000prn.googlegroups.com>`
- **In-Reply-To:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`
- **References:** `<1193454520.506801.39460@50g2000hsm.googlegroups.com>`

```
On Oct 27, 4:08 pm, Pakku <pa...@soccermail.com> wrote:
> Platform z/OS Enterprise Cobol
> Just testing the waters on creating XML output from some flat files.
…[6 more quoted lines elided]…
> environment.

I create XML files using templating. Once a templating routine has
been built then it doesn't matter whether the output is XML, HTML,
CSV, EDIFAC, or printed report, it is all just a matter of stuffing
data items into places in the template.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
