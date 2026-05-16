[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data Representation in COBOL

_26 messages · 15 participants · 2006-01_

---

### Data Representation in COBOL

- **From:** raveendra_ibm <raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au>
- **Date:** 2006-01-07T08:14:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au>`

```

Hi all,

Here is a sample code...

A PIC X(04) VALUE IS 'KLMN'.
B REDEFINES A PIC S9(04).
ADD 1000 TO B.
DISPLAY B.

This gives 134E as answer.

Could anyone please let me know how the data is actually stored and how
this operation is actually performed.

Thanks and Regards,
Raveendra.
```

#### ↳ Re: Data Representation in COBOL

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2006-01-07T13:29:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8632a$43c0086e$4f9c696$32628@DIALUPUSA.NET>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au>`

```
Here is how I think it would work on an IBM mainframe which is an EBCDIC 
machine. However the result you gave is different from what I would expect 
so you may be using a different machine.

The EBCDIC  expression of 'KLMN' in hexadecimal is 'D2D3D4D5'. This must 
first be converted to packed decimal before arithmetic can be performed. The 
packed decimal equivalent of 'D2D3D4D5' is '02345D' which represents a minus 
2345 in three bytes.  The 'D' is treated as a minus sign here which is 
"lucky" because if there were an invalid sign you would receive a data 
exception on the addition. A positive 1000 in packed decimal is '01000C' 
where the 'C' is a plus sign. I would expect the addition to produce 
'01345D' or a minus 1345.  This will then be unpacked and the result placed 
into field B will be 'C1C3C4D5' which would display as '134N' not '134E'. 
The sign is preserved because field B is defined as containing a sign. If 
field B did not contain a sign the compiler would assume the result of the 
addition to be positive and would fix up the sign to give '01345C' which 
would display as your result of '134E'.

If you do not have an EBCDIC chart then see: 
http://www.legacyj.com/cobol/ebcdic.html
Top post no more below.

"raveendra_ibm" <raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> wrote 
in message news:raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au...
>
> Hi all,
…[20 more quoted lines elided]…
>
```

#### ↳ Re: Data Representation in COBOL

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-01-07T15:49:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11s0dr8sjq133ec@news.supernews.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au>`

```
raveendra_ibm wrote:
> Hi all,
>
…[10 more quoted lines elided]…
> how this operation is actually performed.

Don't have a green (yellow) card, eh?
```

##### ↳ ↳ Re: Data Representation in COBOL

- **From:** raveendra_ibm <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>
- **Date:** 2006-01-07T23:29:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com>`

```

Thank you Charles Hottel....

I was wondering if the result would be the same for 

A PIC X(04) VALUE IS 'BCDN'.
B REDEFINES A PIC S9(04).
ADD 1000 TO B.
DISPLAY B.

Could you please let me know how this conversion from unpacked to
packed decimal is actually performed. And how is 1000 represented while
addition is performed.

I am working on IBM Mainframes.

Thanks and Regards,
Raveendra.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-01-07T21:35:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136698530.912343.321270@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`

```
> A PIC X(04) VALUE IS 'BCDN'.
> B REDEFINES A PIC S9(04).
> ADD 1000 TO B.
> DISPLAY B.

> Could you please let me know how this conversion from unpacked to
> packed decimal is ...

It _isn't_ packed. There is no 'unpacked to packed conversion'. It is
all unpacked. The only 'conversion' is that the zone bits are zeroised.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-01-08T15:51:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gxawf.45482$dO2.2324@newssvr29.news.prodigy.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`

```
"raveendra_ibm" <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> wrote
in message news:raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au...
>
> A PIC X(04) VALUE IS 'BCDN'.
…[6 more quoted lines elided]…
> addition is performed.

That is 'implementor-defined' and not part of the COBOL language.

> I am working on IBM Mainframes.
I am sure IBM's compiler uses machine instructions appropriate to its
architecture, but so does each COBOL compiler publisher.

I "believe" the IBM compiler offers a compile-time option to generate an
assembly-language listing. If you use that and can read assembly language,
that will give you both your answers.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-01-08T21:04:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136698737.976576.257180@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`

```
> A PIC X(04) VALUE IS 'BCDN'.
> B REDEFINES A PIC S9(04).
> ADD 1000 TO B.
> DISPLAY B.

> Could you please let me know how this conversion from unpacked to
> packed decimal is ...

It _isn't_ packed. There is no 'unpacked to packed conversion'. It is
all unpacked. The only 'conversion' is that the zone bits are zeroised.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 4)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-01-09T00:41:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136796070.618183.276130@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1136698737.976576.257180@g44g2000cwa.googlegroups.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com>`

```

Richard wrote:
> > A PIC X(04) VALUE IS 'BCDN'.
> > B REDEFINES A PIC S9(04).
…[7 more quoted lines elided]…
> all unpacked. The only 'conversion' is that the zone bits are zeroised.

I was under the impression that all arithmetic on display values in an
IBM mainframe environment involved conversion to packed decimal and
back.  I don't know about other platforms.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 5)_

- **From:** raveendra_ibm <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>
- **Date:** 2006-01-09T08:28:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com>`

```

Hi Richard,

I wonder if there is any sort of conversion from unpacked to packed
format. But I believe zero'ing the zone bits would result in 134N but
it gives 134E as the answer.

The sample code is here...

A PIC X(04) VALUE IS 'KLMN'.
B REDEFINES A PIC S9(04).
ADD 1000 TO B.
DISPLAY B.

Could you please explain me the equivalent assembler code corresponding
to this.

Thanks and Regards,
Raveendra.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-09T14:24:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dptrmd$a4a$1@reader2.panix.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`

```
In article <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>,
raveendra_ibm  <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au> wrote:
>
>Hi Richard,
>
>I wonder if there is any sort of conversion from unpacked to packed
>format.

Do your own homework, please.

DD
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** epc8@juno.com
- **Date:** 2006-01-09T08:22:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136823727.901435.185880@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`

```

raveendra_ibm wrote:
> Hi Richard,
>
…[16 more quoted lines elided]…
>

Why not post this question in the newsgroup "comp.lang.asm370"? They
could use some message traffic. <grin>

BTW, both of your samples output 134N using the old Cobol650 compiler.
(This runs on the PC and uses the ASCII equivalents of the expected
EBCDIC characters for zoned decimals.)

-- Elliot
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-01-09T19:59:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sr85s15r9u1eq86ist8ed1lnkjgpmhjfpv@4ax.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`

```
On Mon, 9 Jan 2006 08:28:55 -0500 raveendra_ibm
<raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au> wrote:

:>I wonder if there is any sort of conversion from unpacked to packed
:>format. But I believe zero'ing the zone bits would result in 134N but
:>it gives 134E as the answer.

:>The sample code is here...

:>A PIC X(04) VALUE IS 'KLMN'.
:>B REDEFINES A PIC S9(04).
:>ADD 1000 TO B.
:>DISPLAY B.

:>Could you please explain me the equivalent assembler code corresponding
:>to this.

I would expect COBOL to generate:

         PACK   WorkField(at least 5),B
         AP     WorkField(at least 5),literal-packed-1000
         UNPK   B,Last-three-bytes-of-WorkField

There may be an intermediate workfield on the UNPK.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-01-10T01:11:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WQDwf.48783$dO2.12027@newssvr29.news.prodigy.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`

```
"raveendra_ibm" <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au> wrote
in message news:raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au...
> I wonder if there is any sort of conversion from unpacked to packed
> format.

In COBOL, that unpacking function is MOVE

MCM
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-01-09T21:50:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136872244.015766.52900@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <raveendra_ibm.21dekg@no-mx.forums.yourdomain.com.au>`

```
> Could you please explain me the equivalent assembler code corresponding
> to this. 

Only with 8085 assembler.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-01-09T13:30:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rztwf.14858$oW.10269@newssvr11.news.prodigy.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com>`

```
"Robert Jones" <rjones0@hotmail.com> wrote in message
news:1136796070.618183.276130@g44g2000cwa.googlegroups.com...

> I was under the impression that all arithmetic on display values in an
> IBM mainframe environment involved conversion to packed decimal and
> back.  I don't know about other platforms.

The specification for the COBOL DISPLAY verb is totally devoid of 'how' the
implementor is to accomplish the result; only the 'what' is part of the
COBOL language.

Earlier this thread I replied to OP re this: I believe the IBM mainframe
compiler offers a compiler option you can specify which will result in the
creation of an assembler list. If you can get that and read assembler, you
will be able to understand the 'how.'

MCM
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-09T13:41:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dptp6e$g6k$1@reader2.panix.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com>`

```
In article <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:

[snip]

>Earlier this thread I replied to OP re this: I believe the IBM mainframe
>compiler offers a compiler option you can specify which will result in the
>creation of an assembler list. If you can get that and read assembler, you
>will be able to understand the 'how.'

The option for the OldBOL compiler (IKFCBL00) was PMAP, for various 
versions of IGYCRCTL it is LIST.

DD
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-01-10T23:39:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42hh6cF1g2vp4U1@individual.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com> <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com> <dptp6e$g6k$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dptp6e$g6k$1@reader2.panix.com...
> In article <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com>,
> Michael Mattias <michael.mattias@gte.net> wrote:
…[12 more quoted lines elided]…
>
Your post stirred something in the deep dark recesses of what passes for my 
brain...

What does/did OPTION SYM do?

Pete.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-10T13:08:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dq0bjg$50q$1@reader2.panix.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com> <dptp6e$g6k$1@reader2.panix.com> <42hh6cF1g2vp4U1@individual.net>`

```
In article <42hh6cF1g2vp4U1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:dptp6e$g6k$1@reader2.panix.com...
…[16 more quoted lines elided]…
>What does/did OPTION SYM do?

I believe that's for IGYCRCTL and it creates SYMbolic records for the TEST 
option.

DD
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-01-10T22:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0NWwf.233699$H26.14998@fe07.news.easynews.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com> <dptp6e$g6k$1@reader2.panix.com> <42hh6cF1g2vp4U1@individual.net> <dq0bjg$50q$1@reader2.panix.com>`

```
For the OS/VS COBOL product (if this was in the "back of your mind"), this 
created a ".SYM" dataset that could be used by the TESTCOB debugger (a "barely" 
interactive debugger of the '70s).  This was the first part of the OS/VS COBOL 
product to "die" (as far as support goes) as it required an "unmovable" dataset 
that could not be handled in an SMS environment.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-01-12T01:10:22+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42katqF1jlro5U1@individual.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <Rztwf.14858$oW.10269@newssvr11.news.prodigy.com> <dptp6e$g6k$1@reader2.panix.com> <42hh6cF1g2vp4U1@individual.net> <dq0bjg$50q$1@reader2.panix.com> <0NWwf.233699$H26.14998@fe07.news.easynews.com>`

```
Thanks to both Bill and Doc.

I think it was the debugger thing I was thinking of... I remember looking at 
Assembler listings produced by it and, as I recall, they were interspersed 
with COBOL source.

Ah, happy days... :-)

Pete.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:0NWwf.233699$H26.14998@fe07.news.easynews.com...
> For the OS/VS COBOL product (if this was in the "back of your mind"), this 
> created a ".SYM" dataset that could be used by the TESTCOB debugger (a 
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-01-09T10:24:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11s53hc8hlpkqe3@news.supernews.com>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <1136698737.976576.257180@g44g2000cwa.googlegroups.com> <1136796070.618183.276130@g44g2000cwa.googlegroups.com>`

```
Robert Jones wrote:
> Richard wrote:
>>> A PIC X(04) VALUE IS 'BCDN'.
…[13 more quoted lines elided]…
> back.  I don't know about other platforms.

Your impression is wrong. Way wrong.

I got my start on a 360-44. It didn't even HAVE storage-to-storage 
operations (such as add packed or move character). To this day, 
register-to-register operations are binary, as they were from the beginning.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2006-01-11T23:20:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.01.12.06.20.56.355748@starband.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au>`

```
On Sat, 07 Jan 2006 23:29:30 -0500, raveendra_ibm wrote:

> 
> Thank you Charles Hottel....
…[15 more quoted lines elided]…
> Raveendra.

The pack and unpack convert zoned decimal to and from packed decimal which
is what the underlying machine language will do.

The ebcdic for BCDN is C2C3C4D5

Pack reverses the zone and numeric nibbles on the last byte and then takes
the numeric nibble for all other bytes.  So you get:

02345D in packed decimal format.  

I don't think that PACK will fail for invalid data.  PACK does not
evaluate the nibbles, only moves them.  Use of the supposed packed field
can fail if the packed data that was created is not in packed format.

Add 1000 gives 01345D.  Since D is a negative sign, adding 1000 to -2345
gives 1345.

Unpack reverses the process of the PACK essentially.  It reverses the last
byte's nibbles again and then moves the decimal nibbles into the numeric
nibble of the preceding bytes of the target.  Then moves X'F' to the zone
nibble giving:  F1F3F4D5 = 134N

The Display VERB simply displays the value with converting the D5 to a
numeric.  It is the numeric value with the sign from the packed decimal
since B is defined as a signed number.

Chris
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 4)_

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2006-01-12T08:49:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.01.12.15.48.58.321121@starband.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <pan.2006.01.12.06.20.56.355748@starband.net>`

```
On Wed, 11 Jan 2006 23:20:59 -0700, Christopher Pomasl wrote:

SNIP
 
> The Display VERB simply displays the value with converting the D5 to a
> numeric.  It is the numeric value with the sign from the packed decimal
> since B is defined as a signed number.
> 
> Chris
It should read "without converting the D5 to a numeric."
My bad.

The Pack and unpack assembler instructions do NOT fail for a data
exception.  Only a Access Exception is noted in my aging POP
hardcopy manual.  They are listed as general instructions and NOT decimal
instructions.  The description specifically states that they do not
evaluate the nibbles as they are being moved.

Chris
Always remember, you are unique...just like everyone else.
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 4)_

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2006-01-12T21:52:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7889$43c715cd$4f9c6b0$26312@DIALUPUSA.NET>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <pan.2006.01.12.06.20.56.355748@starband.net>`

```

"Christopher Pomasl" <pomasl-NOSpam@starband.net> wrote in message 
news:pan.2006.01.12.06.20.56.355748@starband.net...
> On Sat, 07 Jan 2006 23:29:30 -0500, raveendra_ibm wrote:
>
…[9 more quoted lines elided]…
>>

<snip>


> Unpack reverses the process of the PACK essentially.  It reverses the last
> byte's nibbles again and then moves the decimal nibbles into the numeric
> nibble of the preceding bytes of the target.  Then moves X'F' to the zone
> nibble giving:  F1F3F4D5 = 134N

<snip>

The unpack will not move X'F' to the zone. It simply switches the nibbles of 
the rightmost byte. If the COBOL field is defined with a sign then the work 
is done and the sign will reflect whether the result was plus or minus. If 
the COBOL field is defined without a sign the compiler will generate and OR 
Immediate instruct to fix the sign to be positive. (e.g.   OI   B+3,X'F0').
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 5)_

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2006-01-13T18:31:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2006.01.14.01.30.59.317296@starband.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <pan.2006.01.12.06.20.56.355748@starband.net> <7889$43c715cd$4f9c6b0$26312@DIALUPUSA.NET>`

```
On Thu, 12 Jan 2006 21:52:05 -0500, charles hottel wrote:
>> Unpack reverses the process of the PACK essentially.  It reverses the last
>> byte's nibbles again and then moves the decimal nibbles into the numeric
…[9 more quoted lines elided]…
> Immediate instruct to fix the sign to be positive. (e.g.   OI   B+3,X'F0').

It most certainly does, although to be most accurate, the documentation
states "Zone bits with coding of 1111 are supplied for all byte except the
rightmost byte."  Which is essentially the same thing I said.  I stated
that the rightmost byte was reversed and the.....Ahh I see what you
problem is.  The unpack does not move X'f' to all zone bytes of the
target, only all except the rightmost byte.  This is what I meant but
wasn't clear enough I guess.

The remainder of what you say is indeed likely true (I didn't check) but
as stated we are working with a defined signed field.

With "zoned decimal" in COBOL (usage is display), if the field is
signed the last byte will USUALLY be an alphabetic character in the Cx Dx
byte code range. (A-I being positive, J-R being negative)

Chris
```

###### ↳ ↳ ↳ Re: Data Representation in COBOL

_(reply depth: 6)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2006-01-14T21:42:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1137303776.679839.82430@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<pan.2006.01.14.01.30.59.317296@starband.net>`
- **References:** `<raveendra_ibm.219p90@no-mx.forums.yourdomain.com.au> <11s0dr8sjq133ec@news.supernews.com> <raveendra_ibm.21auxe@no-mx.forums.yourdomain.com.au> <pan.2006.01.12.06.20.56.355748@starband.net> <7889$43c715cd$4f9c6b0$26312@DIALUPUSA.NET> <pan.2006.01.14.01.30.59.317296@starband.net>`

```
The compiler options to list the Assembler code generated by IBM
Mainframe COBOL is LIST,NOOFF.  LIST is   rejected if OFFSET is also
selected.

You might also want to check the NUMPROC option for your compiler
version.  It has impact on sign processing.  That seems to be the only
point of disagreement between Charles' version and the problem version,
so that may provide an answer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
