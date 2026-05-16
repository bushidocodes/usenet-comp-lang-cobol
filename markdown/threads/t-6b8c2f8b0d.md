[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Web Services (Retouch)

_24 messages · 13 participants · 2007-06 → 2007-07_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Web Services (Retouch)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-06-23T20:09:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com>`

```
I'm back again into the drawing board here :)

Tried Pete Dashwood/Jimmy Gavan web services Cobol codes and now
"fitting" my own WSDL files created into MS SOAP toolkit v3 (accessing
enterprise COM/COM+). It works perfectly well as I put it... thanks to
them. Tried it with 128kbps connectivity and it is processing in
1:09sec per trip (read/write/update).

The problem I had is when the connectivity shuts down in the middle...
the OLE GUI system return with a dialog box (or window) with a "Yes/
No" message. Of course it is needed to view detailed error of the
process, say error 65573... but then I do not need it. What I need is
my own dialog window saying the "Connectivity is disconnected...".

Could we possibly bypass the default window instead, and just abort
any processing if in case there is an offline connection?
```

#### ↳ Re: Web Services (Retouch)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-24T16:59:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e6c24F36a9ceU1@mid.individual.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1182654551.771351.181830@e9g2000prf.googlegroups.com...
> I'm back again into the drawing board here :)
>
…[4 more quoted lines elided]…
> 1:09sec per trip (read/write/update).

That's across an Enterprise LAN? Or via the Internet? You can make it 
quicker by making the web service "smarter". I just got mine down to under a 
second for batch access,  running a 16000 mile round trip across the 
Internet and 4000 lines of OO COBOL on the server (not all of which get 
executed, of course). Smarten up the Web Service so it only instantiates the 
COM object when it has to, and smarted up the client so it only instantiates 
a web service instance when it has to... Instantiation and DB connection 
(with consequent buffer loads) are the big time takers...
>
> The problem I had is when the connectivity shuts down in the middle...
…[7 more quoted lines elided]…
>

I think you're using MF so I don't know your environment intimately, but OLE 
doesn't have a GUI system as such. If you are seeing a dialog box you need 
to know where it is coming from. If the OLE support Class provided by MF 
raises it, then you should be able to trap it with COM/OLE Exception 
processing; if it is being raised on the Client when it detects that the 
connection is broken it should also be trappable.  Either way, find where it 
comes from and trap it with Exception Class processing, then issue your own 
Dialog.

HTH,

Pete.
```

##### ↳ ↳ Re: Web Services (Retouch)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-06-25T09:08:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182787717.416220.45890@m37g2000prh.googlegroups.com>`
- **In-Reply-To:** `<5e6c24F36a9ceU1@mid.individual.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <5e6c24F36a9ceU1@mid.individual.net>`

```
On Jun 23, 9:59 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> That's across an Enterprise LAN? Or via the Internet?
>
…[9 more quoted lines elided]…
> Pete.

Tried it via Internet. I did some record reading from my side
(client)... and updating or writing a record on the other end (web/
data server) and the processing time per record is 1:09sec. That is
from the indicated bandwidth that I mentioned.

Looking at the "original posted" code below, with a modified
"updateAcctRecord" method;


       *> This class adapated by James J. Gavan for Net Express V 3.1.
       *> If using later versions of Net Express then REPOSITORY
syntax
       *> can replace the 'Class-Control' entries below

 
*>---------------------------------------------------------------
       Class-id.        Soaptest.
       *>               Soaptest inherits from Base.

       *> Where no inheritance is specified it defaults to Base

       Class-Control.
           *> olebase          is class "olebase"
           oleexceptionmanager is class "oleexpt"
           Soaptest            is class "soaptest"
           Mssoap              is class "$OLE$MSSOAP.SoapClient30".

              :
              :
              :

        invoke objSOAPClient "updateAcctRecord"
          using by reference wIn-acctCode   *>input/output interface
block
                by reference wIn-acctName
                by reference wIn-otherData
                by reference wIn-sessionID
                   returning wOut-returnSw


somehow when the Internet connectivity is dead, when processing in the
middle of my "updateAcctRecord" loop... a window is appearing. Yes, Im
using N/E v3.10. From the code above, I guess the window is coming
from "oleexpt" class, or "$OLE$MSSOAP.SoapClient30". Tried overriding
this dialog window... but I can't seemed to removed it yet.
```

#### ↳ Re: Web Services (Retouch)

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-06-24T12:46:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P5yfi.5222$G9.4925@bignews6.bellsouth.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com>`

```
"Rene_Surop" <infodynamics_ph@yahoo.com> wrote:
> I'm back again into the drawing board here :) ...


I recently had use for accessing a web service from a Unisys A Series 
mainframe. Unfortunately, as far as we can tell from the Unisys 
documentation, it never occurred to Unisys that someone might want to access 
a web service from a Unisys A Series mainframe, instead of on one. We put 
the web service access in a PC based client, and transferred the data to the 
mainframe using named pipes. It works, but the Unisys documentation for 
named pipes is, to the extent that it even exists, very incomplete and 
inaccurate. I spent many happy years programming Burroughs/Unisys 
mainframes, and it saddens me to say that Unisys does not seem to know how 
to adapt to the current environment.
```

##### ↳ ↳ Re: Web Services (Retouch)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-26T10:57:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5eavjcF37e8q6U1@mid.individual.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:P5yfi.5222$G9.4925@bignews6.bellsouth.net...
> "Rene_Surop" <infodynamics_ph@yahoo.com> wrote:
>> I'm back again into the drawing board here :) ...
…[17 more quoted lines elided]…
>
Hi Judson (nice to see you back here... :-)).

From what you are describing, maybe there's a market there? If you have 
experimented in this area and got stuff working, you might be able to sell 
this knowledge on. Or package it so that people can easily use it?)

It is a certainty that Web Services will be part of the future (as more and 
more people cotton on to the advantages of SOA, it is likely that people 
currently bound by the mainframe will want to share in these services (just 
as you did)).

Pete.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-06-26T11:47:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oqbgi.3668$3G2.687@bigfe9.bellsouth.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[23 more quoted lines elided]…
> Pete.

Hello Pete, (it's nice to get a chance to check back in. :-)

We are developing the developing the technology, are using it in a second 
project now, and hope to use it in future applications. For the last several 
months I've been studying and developing in Visual Studio 2005, .NET 2.0, 
ASP.NET, etc. Working eyebrow deep in OO these days, but my opinions 
regarding OO haven't changed much. :-)  I'm impressed with how easy it is to 
go from writing Windows applications in VS 2005 to writing ASP.NET 
applications.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-27T13:53:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5edu86F364qj7U1@mid.individual.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:Oqbgi.3668$3G2.687@bigfe9.bellsouth.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
…[35 more quoted lines elided]…
> ASP.NET applications.

Ah, pleased to see you have finally come to the true path... :-)

VS 2005, ASP.NET ... makes you wonder what we could have done with COBOL if 
it had had such an IDE... :-)

(Probably not much more than we did anyway, but we certainly could have done 
it quicker...:-))

Generating Web Services, indeed, anything web related, in this environment 
is so easy... I'm working on a very complex web site that also includes Web 
Services, that in turn, wrap a COM component written in Fujitsu COBOL. The 
whole thing works seamlessly, thanks to InteropServices and the DotNET 
framework. I wouldn't have even considered the approach I have taken on this 
if I hadn't had VS 2005.

"Give us the tools and we will finish the job..." W. S. Churchill

(or, as someone on a team I once managed remarked..."Give us the job and we 
will finish the tools..." :-))

Pete.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-06-27T07:42:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net>`

```
On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>VS 2005, ASP.NET ... makes you wonder what we could have done with COBOL if 
>it had had such an IDE... :-)
>
>(Probably not much more than we did anyway, but we certainly could have done 
>it quicker...:-))

I'm thinking of how many people in the many shops I've worked in have
used interactive debuggers for CoBOL beyond trying them out.

That would be zero.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-27T14:29:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0vugi.107$eY.3@newssvr13.news.prodigy.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com...
> On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> That would be zero.

I think I've tried two or three mainframe COBOL debuggers. Genuine use: 0

I've tried one PC COBOL stepping debugger. Genuine use: 0

I tried one Unix COBOL stepping debugger. Genuine use: 0

I've tried one PC (MS-DOS) BASIC stepping debugger. Genuine use: maybe twice 
over ten ten years.

I've tried one PC (Windows) BASIC stepping debugger. Genuine use: 0

OTOH, I know programmers who START their testing/debugging by running via a 
stepping debugger, and swear  by them.

I'm probably not a good example, since I work almost 100% with my own code, 
which is written so that it *can* be tested and debugged *without* resorting 
to a stepping debugger. But I can see where one might be handy if you get 
thrown into a situation where you have to maintain some unstructured 
monstrosity.

MCM
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-06-27T23:41:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GACgi.1646$tj6.1632@newsread4.news.pas.earthlink.net>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com...
> On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> That would be zero.

I always use Intertest when testing CICS COBOL programs.  Before Intertest I 
think the one I used was called ADS (Advanced Debugging Syetem).  I do not 
think I have ever used batch Intertest which is not very "interactive" 
anyway. Display statements and the rare dump seem enough for batch.  I did 
use COBTEST a few times before they changed it.

When I programmed on VM in assembler they has something called "per" (not 
the hardware facility although it may have interacted with that facility). 
It was great.  You could tell it to watch an address range and it would stop 
you program and report whenever any storage in that range was modified.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-06-28T16:27:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4683E15E.6F0F.0085.0@efirstbank.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`

```
>>> On 6/27/2007 at 7:42 AM, in message
<j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>, Howard
Brazee<howard@brazee.net> wrote:
> On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> That would be zero.

I would hate to do CICS programming without a debugger.

We don't have a batch debugger, unfortunately, instead relying on a lot of
DISPLAY statements.  Yuck.

Debuggers are wonderful things.

Frank
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 7)_

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2007-06-30T03:09:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183198186.777122.162140@q69g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<4683E15E.6F0F.0085.0@efirstbank.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com> <4683E15E.6F0F.0085.0@efirstbank.com>`

```
Pardon my ignorance as I've never programmed on mainframe, but do you
(Mainframe programmers) not have access (even by now) to a good
debugger for testing? About 15 years ago I used DG ICOBOL and I think
to debug that I used DISPLAY statements. After that I used ANIMATOR
and that has been carried over into Netexpress. Without it, I can see
another piece of the argument for not using COBOL anymore.

No, could not survive without Netexpress/Animate.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-30T13:02:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f65k9p$r36$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com> <4683E15E.6F0F.0085.0@efirstbank.com> <1183198186.777122.162140@q69g2000hsb.googlegroups.com>`

```
In article <1183198186.777122.162140@q69g2000hsb.googlegroups.com>,
razor  <iruddock@blueyonder.co.uk> wrote:
>Pardon my ignorance as I've never programmed on mainframe, but do you
>(Mainframe programmers) not have access (even by now) to a good
>debugger for testing?

I know that I've never worked in a shop that had an installed, working, 
mainframe debugger for batch programs, no.  InterTest would be available 
for CICS and I remember a site or two that used Xpeditor for online code, 
as well.

For batch, though, it has always been DISPLAY and READY TRACE... until 
support for the latter was dropped.  Just the other day, though, I made 
use of one of those 'new-fangled' debugging options; a lot of code in this 
shop is built on a skeleton that contains:

DECLARATIVES.             
COBOL-II-DEBUG SECTION.   
    USE FOR DEBUGGING     
        ON ALL PROCEDURES.
COBOL-II-DEBUG-PARA.      
    SET TRACE-ON TO TRUE  
    IF TRACE-ON           
        DISPLAY DEBUG-NAME
    END-IF.               
END DECLARATIVES.         

... and I'm aware that COBOLII is no longer supported... but a bit of 
manual-searching (wonderful thing, this WorldWide Web) showed me

//STEP     EXEC PGM=PROGNAM,PARM='STUFF  ,/DEBUG'

... and it was almost like having IKFCBL00 back... brought a tear to my 
eye, it did.

DD
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 9)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-30T07:03:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183212207.762879.87440@m36g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f65k9p$r36$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com> <4683E15E.6F0F.0085.0@efirstbank.com> <1183198186.777122.162140@q69g2000hsb.googlegroups.com> <f65k9p$r36$1@reader2.panix.com>`

```
On 30 Jun, 14:02, docdw...@panix.com () wrote:
> In article <1183198186.777122.162...@q69g2000hsb.googlegroups.com>,
>
…[8 more quoted lines elided]…
> as well.

Xpeditor can be used to debug batch programs interactively.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-30T14:59:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f65r55$efu$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183198186.777122.162140@q69g2000hsb.googlegroups.com> <f65k9p$r36$1@reader2.panix.com> <1183212207.762879.87440@m36g2000hse.googlegroups.com>`

```
In article <1183212207.762879.87440@m36g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 30 Jun, 14:02, docdw...@panix.com () wrote:
>> In article <1183198186.777122.162...@q69g2000hsb.googlegroups.com>,
…[11 more quoted lines elided]…
>Xpeditor can be used to debug batch programs interactively.

I am aware of this, Mr Maclean, just as I am aware that COBTEST might be 
used similarly... I've just never worked in a shop where either was 
employed.

DD
```

###### ↳ ↳ ↳ Xpediter (was: Web Services (Retouch)

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-07-02T03:41:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2u_hi.70513$9X1.17512@fe03.news.easynews.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183198186.777122.162140@q69g2000hsb.googlegroups.com> <f65k9p$r36$1@reader2.panix.com> <1183212207.762879.87440@m36g2000hse.googlegroups.com> <f65r55$efu$1@reader2.panix.com>`

```
When I worked for ADS (before it became Centura - before Compuware bought it), 
there were not only shops that had Xpediter installed - but lots that DID use it 
for batch. (I first became aware of it as a user - at a large phone company when 
MVS was just going from 24-bit to 31-bit).  Later on when I worked for Micro 
Focus, we had a number of mainframe shops that would call in asking, "I can do 
xyz with Xpediter, how do I do that with the Animator".

I am WELL aware of a number of shops that "installed" but NEVER (rarely) used 
Xpediter (for batch).  However, I do think that at LEAST a 3rd of their 
customers that paid "maintenance costs" (not cheap), did actually use it for 
batch.  (The CICS and IMS features were "add-ons" - at least then).  My best 
guess is that about half of all their paying customers actually have SOME 
programmers that used it.

P.S.  Partially, this depends on what shops allowed to be "run in the 
foreground" - on TSO.  I don't recall many shops running BATCH Xpediter 
(although it was certainly supported).  I don't recall many (IMS shops - for 
example) that did NOT allow BTS in the foreground, but did allow Xpediter.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-02T07:44:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183387453.899018.42020@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f65r55$efu$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183198186.777122.162140@q69g2000hsb.googlegroups.com> <f65k9p$r36$1@reader2.panix.com> <1183212207.762879.87440@m36g2000hse.googlegroups.com> <f65r55$efu$1@reader2.panix.com>`

```
On 30 Jun, 15:59, docdw...@panix.com () wrote:
> In article <1183212207.762879.87...@m36g2000hse.googlegroups.com>,
>
…[20 more quoted lines elided]…
> DD

It is something of an experience to be undertaken only in the direst
of circumstances.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-02T14:50:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6b3b0$kln$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183212207.762879.87440@m36g2000hse.googlegroups.com> <f65r55$efu$1@reader2.panix.com> <1183387453.899018.42020@k79g2000hse.googlegroups.com>`

```
In article <1183387453.899018.42020@k79g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 30 Jun, 15:59, docdw...@panix.com () wrote:
>> In article <1183212207.762879.87...@m36g2000hse.googlegroups.com>,
>>
>> Alistair  <alist...@ld50macca.demon.co.uk> wrote:

[snip]

>> >Xpeditor can be used to debug batch programs interactively.
>>
…[5 more quoted lines elided]…
>of circumstances.

That's all right, Mr Maclean... I'm up to the challenge, I just happen to 
have in my briefcase a Quick Reference guide for (rummage rummage rummage) 
XPEDITER (both /TSO and /IMS 5.3), printed on 13 Oct 1992.

Scarce old enough for peach-fuzz, aye.

DD
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 13)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-03T03:25:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183458328.379735.39950@k29g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<f6b3b0$kln$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183212207.762879.87440@m36g2000hse.googlegroups.com> <f65r55$efu$1@reader2.panix.com> <1183387453.899018.42020@k79g2000hse.googlegroups.com> <f6b3b0$kln$1@reader2.panix.com>`

```
On 2 Jul, 15:50, docdw...@panix.com () wrote:
> In article <1183387453.899018.42...@k79g2000hse.googlegroups.com>,
>
…[23 more quoted lines elided]…
> DD

I have a S/370 Assembler yellow card (before it became the yellow
booklet) dating from about 1982. What's the oldest that you have?
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-03T11:26:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6dbom$e7p$1@reader2.panix.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <1183387453.899018.42020@k79g2000hse.googlegroups.com> <f6b3b0$kln$1@reader2.panix.com> <1183458328.379735.39950@k29g2000hsd.googlegroups.com>`

```
In article <1183458328.379735.39950@k29g2000hsd.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 2 Jul, 15:50, docdw...@panix.com () wrote:

[snip]

>> That's all right, Mr Maclean... I'm up to the challenge, I just happen to
>> have in my briefcase a Quick Reference guide for (rummage rummage rummage)
…[5 more quoted lines elided]…
>booklet) dating from about 1982. What's the oldest that you have?

With all due respect, Mr Maclean, I reveal what I choose to reveal and 
that's about that; it is not my habit to indulge in bouts of 'mine is 
older/larger/smellier/more gem-encrusted than yours'.

DD
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-30T06:59:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183211994.784321.149310@n60g2000hse.googlegroups.com>`
- **In-Reply-To:** `<j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`

```
On 27 Jun, 14:42, Howard Brazee <how...@brazee.net> wrote:
> On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
>
…[10 more quoted lines elided]…
> That would be zero.

I found Xpeditor extremely useful when I worked at FDR in Basildon
(UK). I also found the built-in debugger in Natural 3 very useful when
at Britannia Music.
```

###### ↳ ↳ ↳ Re: Web Services (Retouch)

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-02T19:33:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TdWdndVACKoWOhTbnZ2dnUVZ_r2onZ2d@comcast.com>`
- **In-Reply-To:** `<j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <P5yfi.5222$G9.4925@bignews6.bellsouth.net> <5eavjcF37e8q6U1@mid.individual.net> <Oqbgi.3668$3G2.687@bigfe9.bellsouth.net> <5edu86F364qj7U1@mid.individual.net> <j7q483harmef4b6kktj2kqrjb27ohomp3a@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 27 Jun 2007 13:53:09 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> That would be zero.

The Unisys IX (2200) mainframe has a nice debugging system called PADS 
(Programmer's Advanced Debugging System).  You could do stepping with 
it, or you could call it from a certain point in your program.  It also 
handles the Post-Mortem Dump (PMD) process for extended-mode programs. 
However, the way the environment has to be set up, for the most part, 
assumes you are the only one on the mainframe.  That just didn't work in 
our environment.

For a few weeks, we were actually at a Unisys facility, and when we were 
there, we had a mainframe all to ourselves.  I played with it a bit - it 
looked useful, but we couldn't use it in our normal development 
environment.  There was a feature of the compiler where you could 
compile with a MONITOR keyword.  When you executed the program, all the 
paragraph names appeared, and the before and after values for each 
variable were displayed.  All that was queued to a print file that we 
downloaded, and were able to parse through to at least *see* what the 
program was doing.

It's a shame we could never get PADS to work...
```

#### ↳ Re: Web Services (Retouch)

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-07-03T02:55:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%Uiii.80292$1i1.11139@pd7urf3no>`
- **In-Reply-To:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com>`

```
Rene_Surop wrote:
> I'm back again into the drawing board here :)
> 
…[14 more quoted lines elided]…
> 
I think if you want to do your 'own thing' when it comes to exceptions, 
you had better look at the OLE Exception Handling class and Exception 
Handling in general. From memory, and as a general principle, OLE or 
otherwise, on exceptions you trot off to your own Exception Error File 
(Line Sequential - error messages accessed by position).

For the N/E 5.0 on-line books use the global index and pick up on 
'Exception' topics. There are tutorials. (I don't much care for the 
concept of a global error file - too much maintenance to keep it in sync 
- and prefer the concept of going within the specific class to a method 
"ErrorMessages" where I can have literals which are concise messages.
Haven't checked the OLE Exceptions; you may need to introduce your own 
'MyExceptions' so you can override the normal behaviour for the OLE class.

If you are a bit leery about the latter suggestion - let me know and 
I'll take a look and I can point you at an example of overriding Listbox 
default sorting written by either Chris Glazier or David Sands.

Jimmy

Jimmy
```

##### ↳ ↳ Re: Web Services (Retouch)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-07-03T16:28:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183505304.359532.166970@i13g2000prf.googlegroups.com>`
- **In-Reply-To:** `<%Uiii.80292$1i1.11139@pd7urf3no>`
- **References:** `<1182654551.771351.181830@e9g2000prf.googlegroups.com> <%Uiii.80292$1i1.11139@pd7urf3no>`

```
I already did some testing with NEv3.1 Jimmy and found OLE exception
that helps (code below). It works so far for me. The callback
procedure will push if an OLE error will occur, or any disconnection
whatsoever from the WSDL server. Thanks Jimmy.


       class-control.
           entrycallback is class "entrycll"
           exceptMgr is class "exptnmgr"
           oleExceptMgr is class "oleexpt"
           MSSoap is class "$OLE$MSSOAP.SoapClient30".
                 :
                 :
                 :
       working-storage section.
       01  WSDL-uploadProduct pic x(70) value
           z'http://www.urlsite.com/myWeb.wsdl'.

       01  objSoapClient     object reference value null.
       01  osException       object reference value null.
       01  lnkNullReference  object reference value null.
       01  lnkErrorNumber    pic x(4) comp-5.
       01  lnkErrorObject    object reference.
       01  lnkErrorText      object reference.
       01  wTransKey         pic x.
                 :
                 :
                 :
       000-main-process section.
            *>
            *>Set up the exception handling
              invoke entrycallback "new" using z"onOleException"
                                     returning osException
              invoke exceptmgr "register" using oleExceptMgr
                                                osException
            *>
            *>Invoke the WSDL/XML command
              invoke MSSoap "new" returning objSoapClient
              invoke objSOAPClient "mssoapinit"
                        using WSDL-uploadProduct
                 :
                 :
                 :
            *>invoke the wdsl (via internet/DSL)
              invoke objSOAPClient "testProductWrite"
                       using by reference witemBarcode
                             by reference witemDesc
                             by reference wpriceCurrent
                             by reference wcostCurrent
                             by reference wprocessTime
                             returning wreturnSw
                 :
                 :
                 :
       000-callback section.
       entry "onOleException" using by reference lnkErrorObject
                                    by reference lnkErrorNumber
                                    by reference lnkErrorText.

           display "<<<<<Web Service (WSDL/XML) Error
Encountered>>>>>"
           display "<<The Error Number Was: " lnkErrorNumber
           if lnkErrorText not = null
              display "<<The Error Description Is: "
              invoke lnkErrorText "display"
              display
"<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>"
              display "<<Please press [ENTER] key to continue..."
                    with no advancing
              accept wTransKey
              display " "
           end-if.

           exit program returning lnkNullReference.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
