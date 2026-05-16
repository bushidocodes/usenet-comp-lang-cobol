[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC

_10 messages · 6 participants · 2003-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC

- **From:** "DLI" <equisoft@starband.net>
- **Date:** 2003-10-24T21:02:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Prgmb.1377$zd2.423938152@twister2.starband.net>`

```
Is there an ODBC driver available that would allow me to read COBOL dat
files from Crystal reports or MS Access?

TIA
```

#### ↳ Re: ODBC

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-10-24T16:43:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YnydnY0j04CTAASiU-KYhg@giganews.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net>`

```
DLI wrote:
> Is there an ODBC driver available that would allow me to read COBOL
> dat files from Crystal reports or MS Access?

There's no such thing as a "COBOL dat" file. A COBOL program can write files
in almost any format, but there are COBOL formats that are proprietary to
the COBOL compiler vendor.

You'll have to tell us what compiler vendor and what format. While text and
csv files are universal, relative, variable-length, and ISAM (Indexed
Sequential Access Method) files vary depending on the vendor.
```

##### ↳ ↳ Re: ODBC

- **From:** "DLI" <equisoft@starband.net>
- **Date:** 2003-10-26T17:04:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y8Tmb.1646$kr1.503606333@twister2.starband.net>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com>`

```
Thank you for the response.
My company is Equisoft, Inc.

Here is my situation. We provide software to the Equine industry. One of our
competitors has gone out of business. (The sole proprietor is deceased). The
competitor's name was EDMS (Equine Data Management Systems)

Their application was written in COBOL which appears to be a product vended
by
Liant Software Corporation

I have a copy of the folder that contains the COBOL source and data. The
files that contain the program information (based on their file dates and
size) have an extension of DAT

There is a reg file in the folder that contains references to
Liant Software Corporation

The potential customer would just like us to import the current list of
clients from the COBOL system into the product that we sell.

We have MS certified engineers in Access and SQL Server but none with
experience using COBOL.
I suspect that these files are ISAM but I have no way of knowing for sure.



"JerryMouse" <nospam@bisusa.com> wrote in message
news:YnydnY0j04CTAASiU-KYhg@giganews.com...
> DLI wrote:
> > Is there an ODBC driver available that would allow me to read COBOL
> > dat files from Crystal reports or MS Access?
>
> There's no such thing as a "COBOL dat" file. A COBOL program can write
files
> in almost any format, but there are COBOL formats that are proprietary to
> the COBOL compiler vendor.
>
> You'll have to tell us what compiler vendor and what format. While text
and
> csv files are universal, relative, variable-length, and ISAM (Indexed
> Sequential Access Method) files vary depending on the vendor.
>
>
```

###### ↳ ↳ ↳ Re: ODBC

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-10-26T13:12:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KJidnTpX6t40gQGiU-KYjQ@giganews.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com> <Y8Tmb.1646$kr1.503606333@twister2.starband.net>`

```
DLI wrote:
> Thank you for the response.
> My company is Equisoft, Inc.
…[23 more quoted lines elided]…
> sure.

There are a couple of possible solutions:
1. Assuming your prospect is still running the mysterious software, he can
probably export the data to some universal (text?) format. From this
intermediate reckoning, you can probably one-off an import program.

2. If the original owner is deceased, perhaps a modest fee to his estate
will get you access to the original source code.

3. If, by inspection, you can't make heads or tails out of the data file,
the data file is probably ISAM. If the data were a relative or
variable-length file, you'd see the data with an occassional "what's this?"
intersperced. Entering the terms: "liant cobol isam" into Google resulted in
almost 100 references, including several conversion tools.

The inherent difficulty in #3 is the specificity of the data. Here's the
number "000500." Is that a price? A length? Quantity sold last December?
Number of relatives with red hair?

Our company once bought out a competitor in a situation similar to yours -
it worked out well for everyone: us, the competitor, and the customers. We
paid nothing up front, and only paid as the customers converted to our
system (at less that our normal sales commission). Our costs were a
conversion program - we gained access to the competitor's source - and a
little technical support.
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-10-26T18:30:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H8WdndaoKPmh-gGiU-KYjA@giganews.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com> <Y8Tmb.1646$kr1.503606333@twister2.starband.net> <KJidnTpX6t40gQGiU-KYjQ@giganews.com>`

```
JerryMouse wrote:
> DLI wrote:
>> Thank you for the response.
…[51 more quoted lines elided]…
> competitor's source - and a little technical support.

Arghh! I overlooked your statement that you had the original source. That
being the case, anyone conversant with COBOL can tell the data layout. To
confirm you're dealing with an ISAM file, look at the beginning of each
source module for statements of the form:

SELECT something ASSIGN TO something
   ORGANIZATION IS INDEXED
   ACCESS IS something
   RECORD KEY IS something
   FILE STATUS IS  something.

Finding the above, you've got indexed files.
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 5)_

- **From:** "DLI" <equisoft@starband.net>
- **Date:** 2003-10-27T12:21:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A58nb.1746$rV3.543569010@twister2.starband.net>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com> <Y8Tmb.1646$kr1.503606333@twister2.starband.net> <KJidnTpX6t40gQGiU-KYjQ@giganews.com> <H8WdndaoKPmh-gGiU-KYjA@giganews.com>`

```
Thanks for the help. I will see if I can dig up a COBOL guru.
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 6)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-10-28T20:57:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q1mtpvkifb0e0kl55nadcj8ij62e5bjtkf@4ax.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com> <Y8Tmb.1646$kr1.503606333@twister2.starband.net> <KJidnTpX6t40gQGiU-KYjQ@giganews.com> <H8WdndaoKPmh-gGiU-KYjA@giganews.com> <A58nb.1746$rV3.543569010@twister2.starband.net>`

```
On Mon, 27 Oct 2003 12:21:30 GMT, "DLI" <equisoft@starband.net> wrote:

>Thanks for the help. I will see if I can dig up a COBOL guru.
>
You have one here!!!




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: ODBC

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2003-10-27T16:11:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4tbnb.1171$x41.11@newssvr24.news.prodigy.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net> <YnydnY0j04CTAASiU-KYhg@giganews.com> <Y8Tmb.1646$kr1.503606333@twister2.starband.net>`

```
"DLI" <equisoft@starband.net> wrote in message
news:Y8Tmb.1646$kr1.503606333@twister2.starband.net...
> Thank you for the response.
> My company is Equisoft, Inc.
>
> Here is my situation. We provide software to the Equine industry. One of
our
> competitors has gone out of business. (The sole proprietor is deceased).
The
> competitor's name was EDMS (Equine Data Management Systems)
>
> Their application was written in COBOL which appears to be a product
vended
> by Liant Software Corporation
>
> I have a copy of the folder that contains the COBOL source and data. The
> files that contain the program information (based on their file dates and
> size) have an extension of DAT

Since there is a prospect of converting a number of users of the defunct
EDMS application, I would suggest using Relativity.

Relativity uses the COBOL source files to extract the physical schema for
the data files and allows you to create an ODBC data source which you may
use directly from Access.

So, the answer to your original question is: Yes!
http://www.liant.com/products/relativity/

Best regards,
Tom Morrison
Liant Software COrporation
```

#### ↳ Re: ODBC

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-10-24T22:16:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4xhmb.6916$8x2.3693536@newssrv26.news.prodigy.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net>`

```
"DLI" <equisoft@starband.net> wrote in message
news:Prgmb.1377$zd2.423938152@twister2.starband.net...
> Is there an ODBC driver available that would allow me to read COBOL dat
> files from Crystal reports or MS Access?


http://ourworld.compuserve.com/homepages/Ken_North/odbcvend.htm

MCM
```

#### ↳ Re: ODBC

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-10-27T15:52:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3528449.1067287925@dbforums.com>`
- **References:** `<Prgmb.1377$zd2.423938152@twister2.starband.net>`

```

Originally posted by Dli 

> Is there an ODBC driver available that would allow me to read
> COBOL dat

> files from Crystal reports or MS Access?

>

> TIA 



YOU CAN  TRY  WWW.SIBER.COM

WORKS  FINE



cARLOS lAGES
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
