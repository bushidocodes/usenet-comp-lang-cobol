[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WindowsNT - Mainframe Connection

_5 messages · 5 participants · 1998-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### WindowsNT - Mainframe Connection

- **From:** gonzalezv@my-dejanews.com
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72ooq7$ujc$1@nnrp1.dejanews.com>`

```
In the company I'm currently working, we need to connect our IBM mainframe
with a computer of another company. This computer is running SQL Server under
Windows NT.

In our Host we have running a program (a Cobol/Cics program)that must to
retrieve data from the SQL Server Database of the Windows NT computer.


A few months ago, we did a similar connection between our Host and another
Mainframe (instead of a NT).
In that occasion, we did an APPC connection from our Host to the target Host,
and I made a Cobol program using APPC verbs (Allocate, Connect
Process, Send, Receive, Free, etc.) to communicate my program with another
program in the other Host which retrieve data from its database and returned
them to my program.

Now, and similarly, we need to communicate our program with another program
who must be running in the Windows NT, so this way, we can retrieve data from
the Windows NT computer.

The questions (at last!) are the following:
1) Is it possible to do this?

2) If it is, can I do an APPC connection to the Windows NT (as I did with the
other mainframe)?.

3) Supposing the answer continues being affirmative, can I specify a
"WindowsNT' Program Name" in the "Connect Process" APPC' verb (as I specified
a "Transaction Name" when I connected to another Host)?.

4) Is there other ways to achieve my goal?

Thanks in advance.
V�ctor.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: WindowsNT - Mainframe Connection

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2LV32.694$5e4.268173@news.rdc1.on.wave.home.com>`
- **References:** `<72ooq7$ujc$1@nnrp1.dejanews.com>`

```

gonzalezv@my-dejanews.com wrote in message
<72ooq7$ujc$1@nnrp1.dejanews.com>...
>In the company I'm currently working, we need to connect our IBM mainframe
>with a computer of another company. This computer is running SQL Server
under
>Windows NT.
>
…[6 more quoted lines elided]…
>In that occasion, we did an APPC connection from our Host to the target
Host,
>and I made a Cobol program using APPC verbs (Allocate, Connect
>Process, Send, Receive, Free, etc.) to communicate my program with another
>program in the other Host which retrieve data from its database and
returned
>them to my program.
>
>Now, and similarly, we need to communicate our program with another program
>who must be running in the Windows NT, so this way, we can retrieve data
from
>the Windows NT computer.
>
>The questions (at last!) are the following:
>1) Is it possible to do this?

Yes.

>
>2) If it is, can I do an APPC connection to the Windows NT (as I did with
the
>other mainframe)?.

Both IBM and Microsoft sell SNA communications products. Microsoft's is
called SNA server. I can't remember what IBM is calling theirs today, it
used to be SNA Gateway or Communications Manager.

>
>3) Supposing the answer continues being affirmative, can I specify a
>"WindowsNT' Program Name" in the "Connect Process" APPC' verb (as I
specified
>a "Transaction Name" when I connected to another Host)?.

When you use APPC to communicate between two programs in a CICS region, then
CICS handles initiating the program. If you aren't planning to use CICS on
the PC, then you'll probably need a long-running task on the PC.

>
>4) Is there other ways to achieve my goal?

I would look at IBM's TX Series (CICS for Windows NT) and let CICS handle
the communications, 2-phase commit and all that other good stuff that comes
from a transaction manager. It's especially useful for production systems.
Other options include IBM's MQ Series or what they used to call DRDA which
is a data replication product. It depends on whether the transmission is a
batch process or not.


+
>
>Thanks in advance.
…[3 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: WindowsNT - Mainframe Connection

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36503f2f.4014873@news.freeserve.net>`
- **References:** `<72ooq7$ujc$1@nnrp1.dejanews.com> <2LV32.694$5e4.268173@news.rdc1.on.wave.home.com>`

```
On Mon, 16 Nov 1998 13:27:26 GMT, "Karl Wagner" <kewagner@home.com>
wrote:


>
>Both IBM and Microsoft sell SNA communications products. Microsoft's is
>called SNA server. I can't remember what IBM is calling theirs today, it
>used to be SNA Gateway or Communications Manager.

'Client Access' I believe is the family name now. If it follows the
same naming convention as the AS/400 product.

I used it last year for an AS/400 BPCS to Windows database (Interbase)
connection.

I found however that the SNA APPC route was really slow so went with
TCP/IP eventually.
```

###### ↳ ↳ ↳ Re: WindowsNT - Mainframe Connection

- **From:** "Vincent DiGioia" <vmdigioia@digioia.com>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<azY32.141$K4.261945@news.abs.net>`
- **References:** `<72ooq7$ujc$1@nnrp1.dejanews.com> <2LV32.694$5e4.268173@news.rdc1.on.wave.home.com> <36503f2f.4014873@news.freeserve.net>`

```
I am communicating to the Mainframe via TCP/IP;  there are several MVS
products available to interact with CICS/VSAM/DB2;

Vincent
```

#### ↳ Re: WindowsNT - Mainframe Connection

- **From:** "Simon Cordingley" <simonc@casegen.co.uk>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365066f2.0@mercury.nildram.co.uk>`
- **References:** `<72ooq7$ujc$1@nnrp1.dejanews.com>`

```
Simplest way is using CICS Client software. We communicate with mainframe
CICS this way with our CICS Client/Server Cobol tools generating Cobol for
both the CICS and "client" platform. We support Windows 95/98/NT as client
platforms.

We have examples in production.

Please email me if you need more info.

See www.casegen.co.uk



gonzalezv@my-dejanews.com wrote in message
<72ooq7$ujc$1@nnrp1.dejanews.com>...
>In the company I'm currently working, we need to connect our IBM mainframe
>with a computer of another company. This computer is running SQL Server
under
>Windows NT.
>
…[6 more quoted lines elided]…
>In that occasion, we did an APPC connection from our Host to the target
Host,
>and I made a Cobol program using APPC verbs (Allocate, Connect
>Process, Send, Receive, Free, etc.) to communicate my program with another
>program in the other Host which retrieve data from its database and
returned
>them to my program.
>
>Now, and similarly, we need to communicate our program with another program
>who must be running in the Windows NT, so this way, we can retrieve data
from
>the Windows NT computer.
>
…[3 more quoted lines elided]…
>2) If it is, can I do an APPC connection to the Windows NT (as I did with
the
>other mainframe)?.
>
>3) Supposing the answer continues being affirmative, can I specify a
>"WindowsNT' Program Name" in the "Connect Process" APPC' verb (as I
specified
>a "Transaction Name" when I connected to another Host)?.
>
…[6 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
