[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_56 messages · 11 participants · 2007-05 → 2007-06_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-21T23:25:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bddsqF2sd0m9U1@mid.individual.net>`

```
I've had a couple of private mails after responding publicly here to a 
request for help with accessing Web Services from COBOL.

Here is a VERY brief summary of the situation:

(Some parts of the following are reproduced from some documentation I wrote 
and attached to the example COBOL code, as a Fujitsu NetCOBOL project)

WEB SERVICES ROCK!

This is the next step on in the components arena. A web service exposes some 
or all of the properties and methods of a component to the Web. Why is that 
important? Because it means you can write a component and deploy it once. 
Anyone with access to your local intranet can access it, or, if you have 
delusions of grandeur (or work for an international company), expose it to 
the Internet and anyone on the planet can access it. And the responses, even 
across great distances, are very fast. (A round trip from NZ to California 
in under a second).

Instead of having to maintain packages you have issued and update them all, 
you do it once (on your Web server) and any package using the service is 
instantly using the new version.

Leaving aside the technicalities of it (which are quite awesome) this means 
that design can take legacy functions and even subsystems, wrap them as a 
Web service, and keep on using them until there is time to re-develop new 
stuff (which will also be developed as a series of web services so there is 
"overlap" and transparency.)

It means that currently disparate systems, possibly deployed on different 
platforms, can become a series of web services that are completely platform 
independent, but accessible by all. This facilitates better logical 
integration without the need for physically making systems talk to each 
other or access each other's data. (Data can be requested from a service; 
how it is provided is immaterial)

Bottom Line:

Offering business functions as web services is likely to be the way of the 
future. It is also a powerful way to integrate disparate systems.

GENERAL CONSIDERATIONS

What and why Web Services?

Web Services are the next step on from COM servers. They don't obviate COM 
servers because these can be embedded in many useful places, but they DO 
allow a piece of encapsulated functionality (a component) to be centralized 
and maintained in ONE place, then accessed from anywhere on the planet. 
(This has major implications when it comes to software distribution and 
updates; no more hundreds of copies to be updated, just one.)

A web Service is a component that exposes some or all of itself to the Web. 
Like all OO components it will have methods and properties, and it probably 
takes (and returns) parameters. Pretty straightforward and not mysterious. 
The clever bit is in HOW it is able to talk to any platform OS, on any 
hardware, and realise the dream of data interoperability.

It does it through the magic of XML and a protocol called SOAP. (Originally, 
"Simple Object Access Protocol", but now officially meaningless.)

But isn't SOAP obsolete?

Yes. It is being superseded by DotNET services. MS had hoped to stop 
supporting SOAP by  2003 but it is so useful and embedded in so many of 
their own products it has now been officially reprieved until 2008. Office 
2003 comes with its own SOAP libraries and if you have this version of 
Office you can use those libraries instead of standard SOAP. (Use 
MSOSOAP.SoapClient30 instead of MSSOAP.SoapClient30).

All new development SHOULD use the DotNET methods instead of SOAP, but, as 
NetCOBOL cannot use the DotNET libraries easily, that leaves most COBOL 
users out in the cold.

So, use SOAP until you get into C#. This allows you to leverage your 
existing COBOL code and also make use of web services. (When your COBOL is 
finally converted to whatever it will become, it is VERY easy to replace 
SOAP calls to a web service with DotNET calls to the same service.)

DotNET is where the future lies and it is being picked up for all OSes 
(including UNIX/Linux) and will run on all platforms (possibly even 
including mainframes).  It can do this because it is NOT object code or an 
API that would be machine/OS dependent; instead, it is intermediate code 
which is compiled for whatever platform it is running on, as it is loaded.

The specific example included below.

This is a small COBOL .EXE that accesses a Web Service called AVS (Address 
Validation Services). The web service is running (at time of writing; it 
could change, but it really doesn't matter anyway, as long as it is visible 
on a server somewhere.) on a server farm in San Francisco. You can access it 
from Australia, or Germany just as easily as I access it from NZ. Responses 
are immediate and the distances don't seem to matter.

AVS provides a fully selectable service of operations involving NZ postal 
addresses. It covers flats, apartments, urban, rural, PO Box and private 
bag, Post Restante,  Counter Delivery and postcode and locality encoding. As 
a bonus, it also returns a complete address from partial free-format data, 
formatted in compliance with NZPO requirements.

You can present data to it in fixed (each field is defined and filled in the 
interface block) or free format (a single string is passed in the ws-buffer 
field of the interface block. AVS analyses and parses it then returns all 
the fields and a formatted address).

 (Fixed input may not function for the web service, although it is OK if you 
are using AVS as a COM component). Just concatenate whatever fixed fields 
you have and present them as free-format data to the web service.

So how and where would I use it?

You would plug the service in to any point in an application where you need 
address services. Pass it what you have collected from the user, invoke it, 
and select whatever you want to display back, or update a database. It 
really is that simple.

It's a bit like "outsourcing" NZ postal address requirements. Fill in the 
blanks, get the post code, update changed localities, whatever you want to 
do.

Conclusion

Enabling your application for web services is a step towards the future.

It is no more complex to obtain the complete functionality described above, 
than it is to simply get a valid postcode.

There are HUGE pitfalls in address processing. It is nowhere near as simple 
as it first appears (the AVS engine took around 800 hours to write). 
Because of changes to the address coding in NZ, localities and postcodes now 
mean more than previously. A street and a postcode will uniquely identify an 
address, but streets, postcodes, and localities are not unique. And not 
everybody lives in town; the boxes and rural domains have their own 
idiosyncracies.

PROS:

1. Calling a web service is simple and facilitates future conversion.
2. It is easy to outsource the functionality and not have to maintain and 
update postal data as well as your application.
3. The interface is just as simple as calling a COM/ActiveX component.
4. No maintenance required.

CONS:

1. You must be online to use it.

HERE'S THE SAMPLE CODE IN FUJITSU NetCOBOL (Maybe someone can convert it to 
NE or ACUCOBOL so we can see the differences...?) ANY COBOL that can support 
accessing COM/ActiveX components can access the web service.

WARNING: You must have a SOAP library installed on your system. (It is the 
SOAP component that accesses the WSDL for the service, generates the 
required XML to transport your interface block and return it, and invokes 
the web service method. As you can see, NO KNOWLEDGE OF XML or SOAP is 
required to use the service, even though it would be impossible without 
these protocols.) If you have MS Office 2003, use the MSOSOAP.SoapClient30 
component, rather than the MSSOAP.SoapClient30 component. You can download 
the SOAP Toolkit from:
http://www.microsoft.com/downloads/details.aspx?FamilyId=C943C0DD-CEEC-4088-9753-86F052EC8450&displaylang=en

NOTE: DO NOT COMPILE AND RUN THIS CODE! You won't see anything and it will 
look as if it did nothing. Instead, compile it for debugging and step 
through it, then everything becomes clear.

000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. 'SOAPTest'.
000030*AUTHOR. Peter E. C. Dashwood.
000031*
000040* This program attempts to instantiate a SOAP Proxy class and
000050* access a Web Service using the new proxy...
000051*
000060*DATE_WRITTEN. May 2007.
000070 ENVIRONMENT DIVISION.
000080 configuration section.
000090 source-computer. IBM-PC.
000100 object-computer. IBM-PC.
000101 REPOSITORY.
000110     CLASS COM AS "*COM".
000120
000170
000200*------------------------  DATA   DIVISION  ---------------------
000210 DATA DIVISION.
000340*
000350 WORKING-STORAGE SECTION.
000360 01  in-interface-block pic x(8197).
000361 01  in-IB.
000362     12 in-ws-return   pic x(5).
000363        88 in-ws-OK            value '00000'.   *> will contain 
SQLSTATE if
000364                                 *> there is a DB error
000365     12 in-ws-message  pic x(256). *> will contain SQLMSG if
000366                                 *> there is a DB error
000367     12 in-ws-buffer   pic x(2048). *> holds free format address data
000368                                  *> this will be formatted on return
000369     12 in-ws-breakdown.
000370        15 in-ws-streetNo             pic x(20).
000371        15 in-ws-POBoxNo              pic x(15).
000372        15 in-ws-RDNo                 pic x(8).
000373        15 in-ws-street               pic x(150).
000374        15 in-ws-locality             pic x(150).
000375        15 in-ws-city                 pic x(50).
000376        15 in-ws-lobby                pic x(150).
000377        15 in-ws-postCode             pic x(4).
000378        15 in-ws-addressType          pic x(1).
000379        15 in-ws-streetSDX            pic x(4).
000380        15 in-ws-localitySDX          pic x(4).
000381        15 in-ws-lobbySDX             pic x(4).
000382        15 in-ws-prologue             pic x(100).
000383     12 in-ws-interface               pic x.
000384           88 in-free-format-input     value '1'.
000385           88 fixed-field-input        value '2'.
000386           88 XML-input                value '3'.
000387     12 in-ws-streetMatchFlag         pic x(1).
000388           88 street-fuzzy                  value '0'.
000389           88 street-exact                  value '1'.
000390     12 in-ws-localityMatchFlag       pic x(1).
000391           88 locality-fuzzy                  value '0'.
000392           88 locality-exact                  value '1'.
000393     12 in-ws-repeatLocalityFlag      pic x(1).
000394           88 no-Locality                  value '1'.
000395           88 repeatLocality               value '0'. *> used if 
Locality = City
000396     12 in-ws-ignoreInvalidPostcode   pic x(1).
000397           88 ignoreInvalidPostCode        value '1'.
000398           88 reportInvalidPostCode        value '0'. *>stops if Post 
Code is invalid
000399     12 in-ws-foreignFlag             pic x(1).
000400           88 foreign-address            value '1'. *>stops if foreign 
address detected
000401           88 NOT-foreign-address        value '0'.
000402
000403 01  out-interface-block pic x(8197).
000405 01  out-IB.
000406
000407     12 out-ws-return   pic x(5).
000408        88 out-ws-OK            value '00000'.   *> will contain 
SQLSTATE if
000409                                 *> there is a DB error
000410     12 out-ws-message  pic x(256). *> will contain SQLMSG if
000411                                 *> there is a DB error
000412     12 out-ws-buffer   pic x(2048). *> holds free format address data
000413                                  *> this will be formatted on return
000414     12 out-ws-breakdown.
000415        15 out-ws-streetNo             pic x(20).
000416        15 out-ws-POBoxNo              pic x(15).
000417        15 out-ws-RDNo                 pic x(8).
000418        15 out-ws-street               pic x(150).
000419        15 out-ws-locality             pic x(150).
000420        15 out-ws-city                 pic x(50).
000421        15 out-ws-lobby                pic x(150).
000422        15 out-ws-postCode             pic x(4).
000423        15 out-ws-addressType          pic x(1).
000424        15 out-ws-streetSDX            pic x(4).
000425        15 out-ws-localitySDX          pic x(4).
000426        15 out-ws-lobbySDX             pic x(4).
000427        15 out-ws-prologue             pic x(100).
000428     12 out-ws-interface               pic x.
000429           88 free-format-input        value '1'.
000430           88 fixed-field-input        value '2'.
000431           88 XML-input                value '3'.
000432     12 out-ws-streetMatchFlag         pic x(1).
000433           88 street-fuzzy                  value '0'.
000434           88 street-exact                  value '1'.
000435     12 out-ws-localityMatchFlag       pic x(1).
000436           88 locality-fuzzy                  value '0'.
000437           88 locality-exact                  value '1'.
000438     12 out-ws-repeatLocalityFlag      pic x(1).
000439           88 no-Locality                  value '1'.
000440           88 repeatLocality               value '0'. *> used if 
Locality = City
000441     12 out-ws-ignoreInvalidPostcode   pic x(1).
000442           88 ignoreInvalidPostCode        value '1'.
000443           88 reportInvalidPostCode        value '0'. *>stops if Post 
Code is invalid
000444     12 out-ws-foreignFlag             pic x(1).
000445           88 foreign-address            value '1'. *>stops if foreign 
address detected
000446           88 NOT-foreign-address        value '0'.
000447
000448
000449 01  WSDL-reference pic x(80) value
000450* WSDL to connect to the remote host (in San Francisco)
000451 
'http://primacomputing.co.nz/AVSWebService/AVSWebService.asmx?WSDL'.
000452* WSDL to connect to my IIS server on my new VAIO notebook machine 
over wireless LAN.
000453*     'http://bigblack/AVSWebService/AVSWebService.asmx?WSDL'.
000454*
000455* I have tested both of the above and they both work perfectly. Web 
services can
000456* be hosted anywhere you like and accessed from anywhere on Earth. 
It's magic...!!
000457* (Like DCOM+ on steroids...)
000458
000459 01  COMServer-ProgIDs.
000460     12 SOAP-ProgID           pic x(19) value
000461     "MSSOAP.SoapClient30".
000462
000463 01  COMServer-Objects.
000464     12 objSOAPClient    OBJECT REFERENCE COM.
000465
000466 01  subscripts usage comp-5.
000467     12 J                     pic s9(5).
000468     12 K                     pic s9(5).
000469
000470 01  end-flag                    pic x.
000471     88 not-finished             value zero.
000472     88 finished                 value '1'.
000473
000487
000490 PROCEDURE DIVISION.
000500 MAIN SECTION.
000510 a000.
000520     perform startup-housekeeping
000530     perform main-logic until finished
000540     perform close-down
000550     .
000560 a999.
000570     stop run.
000580*-----------------------------------------------------------
000590 STARTUP-HOUSEKEEPING            section.
000600 sh000.
000640     set not-finished to TRUE
000641* Instantiate SOAP COM Server...
000642     invoke COM "CREATE-OBJECT" using SOAP-ProgID
000643                                returning objSOAPClient
000644     end-invoke
000645* Initialize the SOAP Server and point it at the WSDL for the Web 
Service
000646     invoke objSOAPClient "mssoapinit"
000647            using WSDL-reference
000648     end-invoke
000649* At this point the objSOAPClient reference has become a proxy for the 
AVS Web Service...
000650* This means you can reference any of the methods/properties/events 
exposed by the Web Service,
000651* as if they belonged to the objSOAPClient object...
000652     .
000660 sh999.
000670     exit.
000680*-----------------------------------------------------------
000690 MAIN-LOGIC                      section.
000700 ml000.
000701*
000707*
000708* Now try the methods...
000709*
000710* The AVS Web Service only exposes one method, but the underlying COM 
object has several.
000711
000712* Set up an address string... (Not essential... if you
000714* pass a blank interface block to AVS it will return a message in the 
ws-message
000715* area telling you it was invalid...)
000716     move spaces to in-IB
000718     set in-free-format-input to TRUE
000719     move '97 21ST AVE TAURANGA' to in-ws-buffer *> A NZ address...
000720     move in-IB to in-interface-block
000721     *> Note that string parameters to COM objects must be 8197 bytes
000722     *> and must be elemental.
000723
000724     invoke objSOAPClient "ValidateNZaddress"
000725            using in-interface-block         *> input interface 
block...
000726            returning out-interface-block *> output interface block...
000727                                          *> Note that you could use 
just one block
000728                                          *> but you must reference it 
in and out because the
000729                                          *> Web Service expects in 
and out parameters.
000730
000731     end-invoke
000732*========================== SOAP XML Stringing error fix 
====================
000733* There is currently a problem with SOAP stripping out certain 
characters
000734* in the returned string. This causes fields to be aligned 
incorrectly. The
000735* following is a quick fix and won't be required once the service is 
released.
000736*
000737     move 1 to K *> output buffer pointer
000746    perform
000756        varying J *> input buffer pointer (for this process)
000757           from 1
000758             by 1
000759          until K > function LENGTH (out-IB)
000760             move out-interface-block (J:1) to out-IB (K:1)
000761             add 1 to K
000762             if out-interface-block (J:1) = x'0A'
000763                move space to out-IB (K:1)
000764                add 1 to K
000765             end-if
000766     end-perform
000769
000770*
000771* ALL of the above code would be replaced by:
000772*
000773*    move out-interface-block to out-IB
000774*
000775* ...once the COM server and SOAP wrapper are fixed. (I'm working on 
it... :-))
000776*
000777*========================  End of SOAP XML Stringing error fix 
==================
000778*
000779
000780*  Debugging Note
000781*
000782*  Now is a good time to look at out-ws-breakdown and out-ws-buffer...
000783*
000784* If you are stepping through this in the debugger, note that each 
field has been
000785* filled in, (street number, street, locality, region, and postcode) 
and the
000786* ws-buffer area now contains a properly formatted address which 
complies with
000787* NZPO requirements, and has been converted to mixed case.
000788*
000789     set finished to TRUE
000790
000791     .
001210 ml999.
001220     exit.
001230*----------------------------------------------------------
001240 CLOSE-DOWN                      section.
001250 cd000.
001260     set objSOAPClient to NULL *> Help the garbage collector ...
001340     .
001350 cd999.
001360     exit.
001370*----------------    END OF PROGRAM 'SOAPTEST' ----------------

So, there you have it. I hope this is of help to those of you (I believe it 
will be an increasing number over the next few years) who are trying to get 
to grips with Web Services.  Although this service is running and I have 
opened it to you all, it won't be that way forever. I will be requiring a 
logon and various authentications when the site hosting the service goes 
live. In other words, if you want to try this out, do it fairly quickly...

Please post questions/comments here, rather than privately.

Pete.
```

#### ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-21T08:17:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179760635.367415.76750@36g2000prm.googlegroups.com>`
- **In-Reply-To:** `<5bddsqF2sd0m9U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net>`

```
Hi Pete,

I'm quite fascinated by your code. Yes, web services really is an
online technology of the future.... but, do you have an "online" demo
of your Web Service application? Maybe on your Server so that we could
view how fast (or efficient) the execution is.
```

##### ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-22T09:15:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5begfuF2so8o3U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <1179760635.367415.76750@36g2000prm.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1179760635.367415.76750@36g2000prm.googlegroups.com...
> Hi Pete,
>
…[4 more quoted lines elided]…
>
Absolutely. That's what I posted. It will run against a live (24/7) web 
service. Step through it, it's fun :-)

I will be posting a downloadable desktop client (written in C#) to the web 
site within the next couple of weeks (I really am absolutely flat out at the 
moment). That will run a batch process on your desktop, accessing the remote 
web service in real time, while you watch. You will be able to SEE the 
addresses getting changed. I have it running currently on my notebook 
desktop and everyone who has seen it is blown away... it's actually fun to 
watch :-)

As you may have gathered, I am completely persuaded by web services, great 
stuff!

Pete.
```

#### ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-21T08:23:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179760294.146122.221870@u36g2000prd.googlegroups.com>`
- **In-Reply-To:** `<5bddsqF2sd0m9U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net>`

```
Hi Pete,

I'm quite fascinated by your code... do you have an "online" demo on
your Web Service? Maybe on your Server so that we could view how fast
(or efficient) the execution is.
```

#### ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-21T22:52:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5bddsqF2sd0m9U1@mid.individual.net...
> I've had a couple of private mails after responding publicly here to a 
> request for help with accessing Web Services from COBOL.
…[459 more quoted lines elided]…
>

Thanks for these postings on web services, Pete.

You make me want to jump into C# but one of my problems with the pc world of 
software has been maintaining my focus.  So for now I am still pursuring 
Java. Effective Java by Jousha Bloch is great and after that I believe I 
will be ready for Design Patterns by Gamma etc. I tried to read Design 
Patterns before but I kept having to consciously think about the meanings of 
the terms. A recent skim showed me that now I have internalized the concepts 
enough and have a more intuitive understanding when reading. I still have 
much to learn and Java keeps evolving and I am still not up to date on all 
the latest and greatest additions.

At some point where I feel I am prepared for anything I am called upon to do 
at work with Java, I will look into C#, I have Murach's C# book.
```

##### ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-22T11:24:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5beo1dF2s776oU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:5bddsqF2sd0m9U1@mid.individual.net...
>> I've had a couple of private mails after responding publicly here to a 
>> request for help with accessing Web Services from COBOL.
<snipped unreferenced previous>

>
> Thanks for these postings on web services, Pete.
>

I'm really happy to help. I think it is important that we all share 
solutions, rather than do it through private mail. (Besides, it is quicker 
for me to post here than respond individually.)

> You make me want to jump into C# but one of my problems with the pc world 
> of software has been maintaining my focus.  So for now I am still 
> pursuring Java.

Java is a very useful OO language. You won't regret learning it. I prefer C# 
because it embodies the good parts of Java, but is more straightforward. (It 
has also been influenced by C++, and, again, takes the better parts of that 
language...). Most importantly though, C# is dedicated to DotNET and is the 
most facile solution for unlocking the power of the DotNET FCL (Framework 
Class Library), which has around 80,000 classes in it... :-)

There is no point in getting emotional about computer programming 
languages... whatever works is good, but some languages are better suited to 
some environments than others.


> Effective Java by Jousha Bloch is great and after that I believe I will be 
> ready for Design Patterns by Gamma etc. I tried to read Design Patterns 
…[5 more quoted lines elided]…
>

Speaking of reading... I am working my way through "The Singularity is Near" 
as you recommended.  I find it stimulating and interesting. Will post my 
overall impressions when I've finished it. At 20 minutes a night, it may be 
some time...:-)

> At some point where I feel I am prepared for anything I am called upon to 
> do at work with Java, I will look into C#, I have Murach's C# book.

Don't know the book so cannot comment. I found the interactive videos were 
fantastic and got me up to speed with C# and VS 2005 very quickly (and 
painlessly...). I'm not sure if they are still being offered; sometimes, 
good offers don't last too long :-).

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-21T19:11:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179799892.138533.30050@n15g2000prd.googlegroups.com>`
- **In-Reply-To:** `<5beo1dF2s776oU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net>`

```
Quite interesting.

Web Service is a great prerequisite for automated client-side code
generation in the mainstream Java and .NET SOAP frameworks. It's a
multi-language technology tool really, it could be C#, Cobol, Java.

Just wonderin', is there anyone who could provide NetExpress Cobol
code (Microfocus) similar above??
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-22T05:18:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2v4i.206393$aG1.36136@pd7urf3no>`
- **In-Reply-To:** `<1179799892.138533.30050@n15g2000prd.googlegroups.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com>`

```
Rene_Surop wrote:
> Quite interesting.
> 
…[6 more quoted lines elided]…
>
Rene,

I could say 'Do your own bloody homework !" :-)

Can't remember do you only have N/E 3.1 or do you also have V 5.0 ?
If you have V 5.0 then I think the source should compile - whether yours 
works or not, that's another matter.

If you are still back at N/E V 3.1 then you have problems. You will 
probably need to use the ISO 2000 directive like I've shown as the first 
line of the source below. You might also need Repository directives - 
but I keep getting syntax errors. If you read up on Directives for 
2000/Repository, although you can simulate the *intended* COBOL 2000 
(ha, ha, bloody ha !), it doesn't do any conformance checking in N/E 3.1.

I've dickered around with Pete's source and at this point in time there 
are only three compiler errors :-

1 - doesn't like where I've placed my substitute Class-Control entry
2 - doesn't like Line 210 - but that's associated with # 1
3 - Line 642 doesn't recognize invoke COM - again back to #1 above ?

If you try other permutations I anticipate you will get a slightly 
different set of errors.

I don't know if you can get it working without Repository syntax - I 
doubt it - just have to suck and see. Anyway as is, the source is just 
down to three errors. So now you can take over :-) - you can zip me back 
a copy if you get it working with N/E 3.1 - no point if you only do it 
with N/E 5.0. (If for some unknown reason the source below wraps around, 
e-mail me and I'll send the N/E source file as a zip).

Note for Pete - what you transmitted - a bit of a pain in the butt, but 
not your intent :-). First I highlighted and pasted and each line was 
preceded by '>'. Then the problem with the wrap around comments. 
Probably OK if you were passing a source zipped file, but these damned 
e-mail programs aren't that clever. (My own style just using Columns 8 
thru 72 I enter '*>' in columns 8 and 9 - that allows me to highlight ( 
1 thru 72) and paste without wrap-arounds).

EDITED SOURCE :

       $set iso2000

        *> This 'PARTIAL' version for Net Express V 3.1 


000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. 'SOAPTest'.
000030*AUTHOR. Peter E. C. Dashwood.
000031*
000040* This program attempts to instantiate a SOAP Proxy class and
000050* access a Web Service using the new proxy...
000051*
000060*DATE_WRITTEN. May 2007.
000070 ENVIRONMENT DIVISION.
000080 configuration section.
000090 source-computer. IBM-PC.
000100 object-computer. IBM-PC.

        Class-Control.       COM Class is  "*com".

*      Three possibilities for Repository Directive, kept on getting
*      errors 'Can't use here' :-

*     $set Repository Off
*     $set Repository Update
*     $set Repository Checking


000101 *>REPOSITORY.
000110 *>    CLASS COM AS "*COM".
000120
000170
000200*------------------------  DATA   DIVISION  ---------------------
000210 DATA DIVISION.
000340*
000350 WORKING-STORAGE SECTION.
000360 01  in-interface-block pic x(8197).
000361 01  in-IB.
000362     12 in-ws-return   pic x(5).
000363        88 in-ws-OK   value '00000'. *> will contain SQKSTATE if
000364                                 *> there is a DB error
000365     12 in-ws-message  pic x(256). *> will contain SQLMSG if
000366                                 *> there is a DB error
000367     12 in-ws-buffer   pic x(2048). *> holds free format address
data
000368                                  *> this will be formatted on
return
000369     12 in-ws-breakdown.
000370        15 in-ws-streetNo             pic x(20).
000371        15 in-ws-POBoxNo              pic x(15).
000372        15 in-ws-RDNo                 pic x(8).
000373        15 in-ws-street               pic x(150).
000374        15 in-ws-locality             pic x(150).
000375        15 in-ws-city                 pic x(50).
000376        15 in-ws-lobby                pic x(150).
000377        15 in-ws-postCode             pic x(4).
000378        15 in-ws-addressType          pic x(1).
000379        15 in-ws-streetSDX            pic x(4).
000380        15 in-ws-localitySDX          pic x(4).
000381        15 in-ws-lobbySDX             pic x(4).
000382        15 in-ws-prologue             pic x(100).
000383     12 in-ws-interface               pic x.
000384           88 in-free-format-input     value '1'.
000385           88 fixed-field-input        value '2'.
000386           88 XML-input                value '3'.
000387     12 in-ws-streetMatchFlag         pic x(1).
000388           88 street-fuzzy                  value '0'.
000389           88 street-exact                  value '1'.
000390     12 in-ws-localityMatchFlag       pic x(1).
000391           88 locality-fuzzy                  value '0'.
000392           88 locality-exact                  value '1'.
000393     12 in-ws-repeatLocalityFlag      pic x(1).
000394           88 no-Locality                  value '1'.
000395           88 repeatLocality  value '0'.
                  *> used if Locality =  City
000396     12 in-ws-ignoreInvalidPostcode   pic x(1).
000397           88 ignoreInvalidPostCode        value '1'.
000398           88 reportInvalidPostCode        value '0'.
                  *>stops if Post Code is invalid
000399     12 in-ws-foreignFlag             pic x(1).
000400           88 foreign-address            value '1'.
                  *>stops if foreign address detected
000401           88 NOT-foreign-address        value '0'.
000402
000403 01  out-interface-block pic x(8197).
000405 01  out-IB.
000406
000407     12 out-ws-return   pic x(5).
000408        88 out-ws-OK            value '00000'.
                                        *> will contain SQLSTATE if
000409                                 *> there is a DB error
000410     12 out-ws-message  pic x(256). *> will contain SQLMSG if
000411                                 *> there is a DB error
000412     12 out-ws-buffer   pic x(2048).
                                      *> holds free format address data
000413                               *> this will be formatted on return
000414     12 out-ws-breakdown.
000415        15 out-ws-streetNo             pic x(20).
000416        15 out-ws-POBoxNo              pic x(15).
000417        15 out-ws-RDNo                 pic x(8).
000418        15 out-ws-street               pic x(150).
000419        15 out-ws-locality             pic x(150).
000420        15 out-ws-city                 pic x(50).
000421        15 out-ws-lobby                pic x(150).
000422        15 out-ws-postCode             pic x(4).
000423        15 out-ws-addressType          pic x(1).
000424        15 out-ws-streetSDX            pic x(4).
000425        15 out-ws-localitySDX          pic x(4).
000426        15 out-ws-lobbySDX             pic x(4).
000427        15 out-ws-prologue             pic x(100).
000428     12 out-ws-interface               pic x.
000429           88 free-format-input        value '1'.
000430           88 fixed-field-input        value '2'.
000431           88 XML-input                value '3'.
000432     12 out-ws-streetMatchFlag         pic x(1).
000433           88 street-fuzzy                  value '0'.
000434           88 street-exact                  value '1'.
000435     12 out-ws-localityMatchFlag       pic x(1).
000436           88 locality-fuzzy                  value '0'.
000437           88 locality-exact                  value '1'.
000438     12 out-ws-repeatLocalityFlag      pic x(1).
000439           88 no-Locality                  value '1'.
000440           88 repeatLocality               value '0'.
                  *> used if Locality = City
000441     12 out-ws-ignoreInvalidPostcode   pic x(1).
000442           88 ignoreInvalidPostCode        value '1'.
000443           88 reportInvalidPostCode        value '0'.
                  *> stops if Post Code is invalid
000444     12 out-ws-foreignFlag             pic x(1).
000445           88 foreign-address            value '1'.
                  *>stops if foreign address detected
000446           88 NOT-foreign-address        value '0'.
000447
000448
000449 01  WSDL-reference pic x(80) value
000450* WSDL to connect to the remote host (in San Francisco)
        'http://primacomputing.co.nz/AVSWebService/AVSWebService.asmx?WSD
       -'L'.
000451

000452* WSDL to connect to my IIS server on my new VAIO notebook
       * machine over wireless LAN.
000453*     'http://bigblack/AVSWebService/AVSWebService.asmx?WSDL'.
000454*
000455* I have tested both of the above and they both work perfectly.
       * Web services can
000456* be hosted anywhere you like and accessed from anywhere on Earth.
       * It's magic...!!
000457* (Like DCOM+ on steroids...)
000458
000459 01  COMServer-ProgIDs.
000460     12 SOAP-ProgID           pic x(19) value
000461     "MSSOAP.SoapClient30".
000462
000463 01  COMServer-Objects.
000464     12 objSOAPClient    OBJECT REFERENCE. *> COM.
000465
000466 01  subscripts usage comp-5.
000467     12 J                     pic s9(5).
000468     12 K                     pic s9(5).
000469
000470 01  end-flag                    pic x.
000471     88 not-finished             value zero.
000472     88 finished                 value '1'.
000473
000487
000490 PROCEDURE DIVISION.
000500 MAIN SECTION.
000510 a000.
000520     perform startup-housekeeping
000530     perform main-logic until finished
000540     perform close-down
000550     .
000560 a999.
000570     stop run.
000580*-----------------------------------------------------------
000590 STARTUP-HOUSEKEEPING            section.
000600 sh000.
000640     set not-finished to TRUE
000641* Instantiate SOAP COM Server...
000642     invoke COM "CREATE-OBJECT" using SOAP-ProgID
000643                                returning objSOAPClient
000644     end-invoke
000645* Initialize the SOAP Server and point it at the WSDL for the Web
       * Service
000646     invoke objSOAPClient "mssoapinit"
000647            using WSDL-reference
000648     end-invoke
000649* At this point the objSOAPClient reference has become a proxy for
       * the AVS Web Service...
000650* This means you can reference any of the methods/properties/events
       * exposed by the Web Service,
000651* as if they belonged to the objSOAPClient object...
000652     .
000660 sh999.
000670     exit.
000680*-----------------------------------------------------------
000690 MAIN-LOGIC                      section.
000700 ml000.
000701*
000707*
000708* Now try the methods...
000709*
000710* The AVS Web Service only exposes one method, but the underlying
       * COM object has several.
000711
000712* Set up an address string... (Not essential... if you
000714* pass a blank interface block to AVS it will return a message in
       * the ws-message
000715* area telling you it was invalid...)
000716     move spaces to in-IB
000718     set in-free-format-input to TRUE
000719     move '97 21ST AVE TAURANGA' to in-ws-buffer *> A NZ address...
000720     move in-IB to in-interface-block
000721     *> Note that string parameters to COM objects must be 8197
bytes
000722     *> and must be elemental.
000723
000724  invoke objSOAPClient "ValidateNZaddress"
000725    using in-interface-block      *> input interface block
000726    returning out-interface-block *> output interface block
000727    *> Note that you could use just one block
000728    *> but you must reference it in and out because the
000729    *> Web Service expects in and out parameters                  n
000730
000731     end-invoke
000732*========================== SOAP XML Stringing error fix
000733* There is currently a problem with SOAP stripping out certain
       * characters
000734* in the returned string. This causes fields to be aligned
       * incorrectly. The
000735* following is a quick fix and won't be required once the service
       *  is released.
000736*
000737     move 1 to K *> output buffer pointer
000746    perform
000756        varying J *> input buffer pointer (for this process)
000757           from 1
000758             by 1
000759          until K > function LENGTH (out-IB)
000760             move out-interface-block (J:1) to out-IB (K:1)
000761             add 1 to K
000762             if out-interface-block (J:1) = x'0A'
000763                move space to out-IB (K:1)
000764                add 1 to K
000765             end-if
000766     end-perform
000769
000770*
000771* ALL of the above code would be replaced by:
000772*
000773*    move out-interface-block to out-IB
000774*
000775* ...once the COM server and SOAP wrapper are fixed. (I'm working
       * on it... :-))
000776*
000777*============  End of SOAP XML Stringing error fix ===========
000778*
000779
000780*  Debugging Note
000781*
000782*  Now is a good time to look at out-ws-breakdown and
       *  out-ws-buffer...
000783*
000784* If you are stepping through this in the debugger, note that each
       * field has been
000785* filled in, (street number, street, locality, region, and postcode)
       * and the
000786* ws-buffer area now contains a properly formatted address which
       * complies with
000787* NZPO requirements, and has been converted to mixed case.
000788*
000789     set finished to TRUE
000790
000791     .
001210 ml999.
001220     exit.
001230*----------------------------------------------------------
001240 CLOSE-DOWN                      section.
001250 cd000.
001260     set objSOAPClient to NULL *> Help the garbage collector ...
001340     .
001350 cd999.
001360     exit.
001370*----------------    END OF PROGRAM 'SOAPTEST' ----------------
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 5)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-22T03:00:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179828059.278246.171550@u36g2000prd.googlegroups.com>`
- **In-Reply-To:** `<g2v4i.206393$aG1.36136@pd7urf3no>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no>`

```
>
> I could say 'Do your own bloody homework !" :-)
…[4 more quoted lines elided]…
>

Haha.... was expecting that, well it is suppose to be a quote from
"docdwarf" :-)

Yap, you're right I'm still in N/E 3.1

Though I was given NetExpress with .NET evaluation copy, I didn't
really used it that much because MF suddenly released N/E 4.0.... and
to V5.0. Hoping I could have a copy of it. But until then, I am
preoccupied viewing their demo on Interface Mapping Toolkit.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-22T19:49:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FPH4i.206089$6m4.122172@pd7urf1no>`
- **In-Reply-To:** `<1179828059.278246.171550@u36g2000prd.googlegroups.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <1179828059.278246.171550@u36g2000prd.googlegroups.com>`

```
Rene_Surop wrote:
>>I could say 'Do your own bloody homework !" :-)
>>
…[15 more quoted lines elided]…
> 

Hang tight. See Pete's comments. Based on his observations I'll give it 
a go in N/E 3.1 and get back to you both.

Jimmy
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-23T00:19:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bg5eaF2r5gf5U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:g2v4i.206393$aG1.36136@pd7urf3no...
> Rene_Surop wrote:
>> Quite interesting.
…[10 more quoted lines elided]…
> I could say 'Do your own bloody homework !" :-)

I'd forgive you for doing so :-) It seems to me to be stretching the 
friendship to just sit back and let others do the work... Everything needed 
to convert my code to MicroFocus can be found on the web (see below).
>
> Can't remember do you only have N/E 3.1 or do you also have V 5.0 ?
> If you have V 5.0 then I think the source should compile - whether yours 
> works or not, that's another matter.

I'm very impressed that you would go to the trouble to do this, Jimmy.

So much so, I decided try and fix what you've posted, so it will work.

I don't have NE so I can't test the changes proposed below, but maybe you 
could?

There are also a few responses to your comments and some general comments on 
accessing COM servers from MicroFocus COBOL.

>
> If you are still back at N/E V 3.1 then you have problems. You will 
…[4 more quoted lines elided]…
> ha, bloody ha !), it doesn't do any conformance checking in N/E 3.1.

I don't think using repository is the best way to go (although it is for 
Fujitsu). I've used your Class-Control instead.
>
> I've dickered around with Pete's source and at this point in time there 
…[3 more quoted lines elided]…
> 2 - doesn't like Line 210 - but that's associated with # 1

I hope that giving it the proper MF COM interface will resolve this.

> 3 - Line 642 doesn't recognize invoke COM - again back to #1 above ?

It never could. COM is a Fujitsu Class used to interface to COM components. 
The equivalent in MF is $OLE$
>
> If you try other permutations I anticipate you will get a slightly 
…[3 more quoted lines elided]…
> it - just have to suck and see.

No, I believe it can work without Repository. It will be late bound anyway.

> Anyway as is, the source is just down to three errors. So now you can take 
> over :-) - you can zip me back a copy if you get it working with N/E 3.1 - 
…[6 more quoted lines elided]…
> preceded by '>'. Then the problem with the wrap around comments.

That's because I use free-format COBOL and some of the lines were more than 
76 bytes wide. Sorry.

Normally, I'd post it as COBOL source to a server and let people download 
it, but it was so small I thought it would be easier to post it here and 
hopefully stimulate some responses form people who tried using it.


> Probably OK if you were passing a source zipped file, but these damned 
> e-mail programs aren't that clever. (My own style just using Columns 8 
…[5 more quoted lines elided]…
>       $set iso2000  ooctrl(+p)

As we are accessing a COM server (The SOAP Component) you need the above MF 
directive...it ensures parameters are passed correctly to the MF Run Time.
>
>        *> This 'PARTIAL' version for Net Express V 3.1
…[4 more quoted lines elided]…
> Gavan.

> 000031*
> 000040* This program attempts to instantiate a SOAP Proxy class and
…[9 more quoted lines elided]…
> Fujitsu Class.)

             MSSOAP is class "$OLE$MSSOAP.SoapClient30"
>
> *      Three possibilities for Repository Directive, kept on getting
> *      errors 'Can't use here' :-

>
> *     $set Repository Off
…[113 more quoted lines elided]…
>       -'L'.

The above literal needs a z in front and removal of the picture (I think?) 
to indicate an ASCIIZ string, for MF.

I'm a bit worried about continuation of this string, Jimmy. It is critical 
that the string is presented intact. If it doesn't work when you step 
through it, try concatenating sections of the string, or STRING it into 
WSDL-reference.

> 000451
>
…[9 more quoted lines elided]…
> 000458

You don't need the following, because it is included in the Class-Control 
entry...
> 000459 01  COMServer-ProgIDs.
> 000460     12 SOAP-ProgID           pic x(19) value
> 000461     "MSSOAP.SoapClient30".


> 000462
> 000463 01  COMServer-Objects.
…[23 more quoted lines elided]…
> 000640     set not-finished to TRUE

This can't work because you have no established reference to COM
> 000641* Instantiate SOAP COM Server...
> 000642     invoke COM "CREATE-OBJECT" using SOAP-ProgID
> 000643                                returning objSOAPClient
> 000644     end-invoke

Try this instead...
                     invoke MSSOAP "new"
                                returning objSOAPClient
                     end-invoke


> 000645* Initialize the SOAP Server and point it at the WSDL for the Web
>       * Service
…[94 more quoted lines elided]…
> 001250 cd000.

Fujitsu is OK with NULL, but MF requires a specific invoke of the 
finalizer...
> 001260    *> set objSOAPClient to NULL *> Help the garbage collector ...

                invoke objSOAPClient "finalize" returning objSOAPClient

> 001340     .
> 001350 cd999.
> 001360     exit.
> 001370*----------------    END OF PROGRAM 'SOAPTEST' ----------------

I am hopeful that the above very minor changes will enable you to compile 
and run this code in the Animator/Debugger.

It will be cool if you get it to work. Remember, the service is running on a 
farm in San Francisco, let us know what your response is like.

Here are some other valid NZ addresses you could feed into it:

APT 510 GRACE JOEL VILLAGE   184 ST HELIERS BAY RD AUCKLAND
CARMELITE MONASTERY 52 HALSWELL RD CHCH
3/13A VOSPER ST MATAMATA
P O BOX 10042 TE MAI

(Valid postcodes and localites/regions should be returned for all of these. 
It is just to show the flexibility of the free format input.)

If you are still getting compile errors, please post here and I'll take 
another look at it.

Note to ALL:

Sometimes the action of finding out stuff is a very rewarding experience. I 
don't know NE and don't have it, but I was very interested to see why 
Jimmy's gallant attempt didn't work. It took me minutes to find what I 
needed on the web, and identify what the major differences are in accessing 
COM servers from Fujitsu and MF.

Having access to COM is a MAJOR feature of using OO. It seems that NE 
implements it just as well (although a little differently) as Fujitsu does. 
I hope some of you NE people are moved to try accessing some of the COM 
components that already exist on your systems...Sometimes these components 
are referred to as "Automation servers" They include things like ACCESS, 
Excel, Powerpoint, and MS Word, all easily accessible from your COBOL, as 
Automation or COM/OLE servers.

Once everyone is happy with ACCESSING a web service from COBOL, the next 
step is to BUILD one in COBOL.  One way is to take a COM component, wrap it 
in the required SOAP/XML, generate the WSDL, and post it on a server. Or, as 
in the case of AVS above, write a C# web service that wraps a COBOL COM 
component, and let VS 2005 generate all the WSDL, XML, and SOAP.

Today, if I was writing AVS again, I'd do it in C#, but at the time I 
started it, I was only just considering C# so I wrote the engine as a COBOL 
COM server instead. Notice that this component based approach has meant that 
even though I move away from COBOL, my COBOL legacy is still viable. BECAUSE 
it is a COM server it can be easily wrapped and handled by C# as "unmanaged" 
code in a web service. And it can be accessed in any language from anywhere 
on any platform that supports web services. Alternatively, it can be dropped 
as a COM component onto a web page or a desktop application and accessed 
locally as a COM object, or remotely over DCOM+ using RPC. (Web services are 
obsoleting this particular use of COM servers; they are more secure than 
DCOM+ and generally more stable.)

Encapsulating functionality into components makes as much sense today as it 
did 10 years ago. There are numerous spin offs from doing so.

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 6)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-22T19:33:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179887604.069942.171890@q66g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5bg5eaF2r5gf5U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net>`

```
>
> As we are accessing a COM server (The SOAP Component) you need the above MF
> directive...it ensures parameters are passed correctly to the MF Run Time.
>

Hi Pete,

Been using the DCOM/COM for several years now... hmm, way back 2002
and I've tried it to be very effective using Microfocus N/E v3.1. You
could see how this N/E Cobol COM works associated with ASP here in my
sample site;

http://infowaters.infodynamicsconsult.com

At first access, the server will activate the COM (.dll file created
in N/E)... once activated, it is now ready for user request. Try
entering "starting customer name" in the box and select the desired
customer name.

1st method: the .dll file is used for searching 10 records (per
display)
2nd method: if customer name is selected, the .dll file will again
retrieve the customer info
3rd method: after displaying customer info, it will display billing
history records

I used it 3years ago... well, that's is why Microfocus says "Cobol
Rocks" then.

Now you're saying Web Services rocks :-)
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-23T15:57:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bhse6F2shrgvU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1179887604.069942.171890@q66g2000hsg.googlegroups.com...
> >
>> As we are accessing a COM server (The SOAP Component) you need the above 
…[11 more quoted lines elided]…
>
 http://infowaters.infodynamicsconsult.com
>
> At first access, the server will activate the COM (.dll file created
…[15 more quoted lines elided]…
>
I've been using COM/DCOM+ MTS etc for over 10 years now.  And I've built web 
sites using ASP to activate COM components written in COBOL, and from COBOL 
CGI/ISAPI code.  It is an excellent component based technology. Web Services 
take it a step further...

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 8)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-22T22:09:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179896963.555487.99600@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5bhse6F2shrgvU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net>`

```
>
> I've been using COM/DCOM+ MTS etc for over 10 years now.  And I've built web
…[3 more quoted lines elided]…
>

Didn't know there were COM ten (10) years back? NetExpress V3.1 came
along year 2000 (that was Merant then), although COM came prior to
that using the Object Cobol.

Well... coming from a 3rd world country :-)
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-23T22:02:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bihpvF2st47eU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1179896963.555487.99600@k79g2000hse.googlegroups.com...
> >
>> I've been using COM/DCOM+ MTS etc for over 10 years now.  And I've built 
…[8 more quoted lines elided]…
> Didn't know there were COM ten (10) years back?

It was Online Linking and Embedding (OLE). This then evolved into the Common 
Object Model.

Fujitsu has supported it since version 3 which I acquired in 1997. It was 
one of the first OO COBOL compilers. Fujitsu offered it free to people who 
were using MicroFocus COBOL. As this was the time of the great VISOC scam 
where MF simply abandoned their user base, I took up the offer and have been 
using Fujitsu ever since.

The made subsequent releases which steadily improved the product, but 
unfortunately, they dropped the ball with their support which became 
abysmal.  With Version 6 they added a crazy Copy Protection system which 
simply alienated the User base and by version 7, the Fujitsu NetCOBOL base 
was feeling  pretty much the way the MF Visoc base had felt some years 
before... abandoned.

The sample code I posted was written in Version 6, as I refused to continue 
paying maintenance for a service that was hopeless, and thus was unable to 
upgrade to V7. ( I think they have dropped support for V6 now, but in the 
interim I learned to support the product myself anyway, so I have no 
problems with it. Also, the documentation for V7 was a huge improvement over 
previous versions and this helped immensely; most of it applies equally well 
to V6)

By then Fujitsu had released NetCOBOL for .NET which, like all their 
previous releases, was of a very high standard, but expensive.  Committed to 
DotNET, but faced with stumping up several thousand dollars for this 
product, I decided to give it one last go with COBOL, and sent off an 
enquiry, with a view to buying it. It was never even acknowledged, and I had 
no intention of begging them to sell me their product, so it was obvious to 
me they didn't want/need my business. I therefore dropped COBOL and moved to 
C#.

Very happy I did. I saved several thousand dollars, don't have to deal with 
idiotic support, can get friendly and knowledgeable help for free whenever I 
want it, and have learned a heap of stuff I otherwise wouldn't have. The 
icing on the cake is that I can still use all my COBOL components from C# 
and ASP.All-in-all, a good result :-).


NetExpress V3.1 came
> along year 2000 (that was Merant then), although COM came prior to
> that using the Object Cobol.
>
> Well... coming from a 3rd world country :-)
>
Your web site is certainly not "third world". It is very impressive.

It looks almost like Access Forms. Is that what you used?

Pete
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 10)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-23T03:22:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179915769.146759.306300@p47g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<5bihpvF2st47eU1@mid.individual.net>`

```
>
> It looks almost like Access Forms. Is that what you used?
>

It is just an .ASP page, no fancy CSS/HTML codes for displaying and
formatting the page. Code it using HTML-Kit freeware.

For the customer name viewing which look like a listbox, I used
Javascript (AJAX) for that.

And the back-end is N/E v3.1 Cobol COM (.dll) for retrieving, updating
(and printing in actual production) which is accessed by a VBscript
code.

Working for now with Web Services... but needed more study on it yet.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 10)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-05-23T20:24:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179977091.567546.22670@n15g2000prd.googlegroups.com>`
- **In-Reply-To:** `<5bihpvF2st47eU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net>`

```
On May 23, 10:02 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> It was Online Linking and Embedding (OLE). This then evolved into the Common
> Object Model.
…[3 more quoted lines elided]…
> were using MicroFocus COBOL.

Version 3 did not have OO or OLE. As this version is still (? adtools
has gone) available it may mislead students into think that it does.

Version 4 introduced OO and OLE in 1998. I have both sets of paper
manuals.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-24T16:25:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bkie5F2sgf9rU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1179977091.567546.22670@n15g2000prd.googlegroups.com...
> On May 23, 10:02 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
>
Thanks Richard. I thought it did but was wrong.

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 12)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-24T04:59:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EY85i.214410$6m4.184311@pd7urf1no>`
- **In-Reply-To:** `<5bkie5F2sgf9rU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <5bkie5F2sgf9rU1@mid.individual.net>`

```
By George he's got it ! I think :-). Cut a long story short, I initially 
downloaded SOAP but doing that Registry check found I already had it. 
Whether or not that duplication was causing a problem ....???? Anyway 
deleted second.

I keep on saying I code, (or used to code)  in Classes so I have 
difficulty getting Procedurals to do exactly what I want without a lot 
of buggering around. Example : I used '$set sourceformt "free"' and for 
some inexplicable reason the compiler queried your line numbers. I had 
other irritating problems as well. So sod it. Use what you are 
comfortable with. I went with the Class format - same as you did but now 
your paragraphs become methods. Here goes :-

Give it a shot Rene and confirm that it works for you !

The code for both starts in Column 8 -

        *>----------------- soaptrigger.cbl ----------------------------

        *> Trigger PROCEDURAL program used here. Assume Soaptest was
        *> selected from a Mster Menu - then the Menu would invoke in a
        *> similar manner.

        Program-id.         SoapTrigger.

        Class-Control.      SoapTest is class "soaptest".

        WORKING-STORAGE SECTION.
        01 os-SoapTest             object reference value null.

        PROCEDURE DIVISION.

        invoke SoapTest    "new"      returning os-SoapTest
        invoke os-SoapTest "begin"
        invoke os-Soaptest "finalize" returning os-SoapTest

        *> Strictly speaking the 'finalize' above is not required -
        *> it is replaced by the STOP RUN

        STOP RUN.

        *>--------------------------------------------------------------


*>-----------------soaptest.cbl ------------------------------
$set sourceformat"free"
$set ooctrl(+p)
*>------------------------------------------------------------

*> Original Procedural program written by Peter E.C. Dashwood
*> in May 2007 using Fujitsu dotNetCOBOL invoking Soap

*> This class adapated by James J. Gavan for Net Express V 3.1.
*> If using later versions of Net Express then REPOSITORY syntax
*> can replace the 'Class-Control' entries below

*>---------------------------------------------------------------
Class-id.        Soaptest.
*>               Soaptest inherits from Base.

*> Where no inheritance is specified it defaults to Base

Class-Control.  *> olebase          is class "olebase"
                 oleexceptionmanager is class "oleexpt"
                 Soaptest            is class "soaptest"
                 Mssoap              is class "$OLE$MSSOAP.SoapClient30"
                 .

*> If having problems with OLE - you could use the N/E
*> OleExceptionManager with a callback method - see N/E
*> OO and OLE documentation

*>--------------------------------------------------------------
*> FACTORY.
*> END-FACTORY.
*>---------------------------------------------------------------
OBJECT.
*>---------------------------------------------------------------
WORKING-STORAGE SECTION.
01  in-interface-block pic x(8197).
01  in-IB.
     12 in-ws-return   pic x(5).
        88 in-ws-OK   value '00000'. *> will contain SQLSTATE if
                                     *> there is a DB error
     12 in-ws-message  pic x(256).   *> will contain SQLMSG if
                                     *> there is a DB error
     12 in-ws-buffer   pic x(2048).  *> holds free format address
                                     *> this will be formatted on

     12 in-ws-breakdown.
        15 in-ws-streetNo             pic x(20).
        15 in-ws-POBoxNo              pic x(15).
        15 in-ws-RDNo                 pic x(8).
        15 in-ws-street               pic x(150).
        15 in-ws-locality             pic x(150).
        15 in-ws-city                 pic x(50).
        15 in-ws-lobby                pic x(150).
        15 in-ws-postCode             pic x(4).
        15 in-ws-addressType          pic x(1).
        15 in-ws-streetSDX            pic x(4).
        15 in-ws-localitySDX          pic x(4).
        15 in-ws-lobbySDX             pic x(4).
        15 in-ws-prologue             pic x(100).
     12 in-ws-interface               pic x.
           88 in-free-format-input     value '1'.
           88 fixed-field-input        value '2'.
           88 XML-input                value '3'.
     12 in-ws-streetMatchFlag         pic x(1).
           88 street-fuzzy             value '0'.
           88 street-exact             value '1'.
     12 in-ws-localityMatchFlag       pic x(1).
           88 locality-fuzzy           value '0'.
           88 locality-exact           value '1'.
     12 in-ws-repeatLocalityFlag      pic x(1).
           88 no-Locality              value '1'.
           88 repeatLocality  value '0'.
           *> used if Locality =  City
     12 in-ws-ignoreInvalidPostcode   pic x(1).
           88 ignoreInvalidPostCode        value '1'.
           88 reportInvalidPostCode        value '0'.
           *>stops if Post Code is invalid
     12 in-ws-foreignFlag             pic x(1).
           88 foreign-address            value '1'.
           *>stops if foreign address detected
           88 NOT-foreign-address        value '0'.

01  out-interface-block pic x(8197).
01  out-IB.

     12 out-ws-return   pic x(5).
        88 out-ws-OK            value '00000'.
                                    *> will contain SQLSTATE if
                                    *> there is a DB error
     12 out-ws-message  pic x(256). *> will contain SQLMSG if
                                    *> there is a DB error
     12 out-ws-buffer   pic x(2048).
                               *> holds free format address data
                               *> this will be formatted on return
     12 out-ws-breakdown.
        15 out-ws-streetNo             pic x(20).
        15 out-ws-POBoxNo              pic x(15).
        15 out-ws-RDNo                 pic x(8).
        15 out-ws-street               pic x(150).
        15 out-ws-locality             pic x(150).
        15 out-ws-city                 pic x(50).
        15 out-ws-lobby                pic x(150).
        15 out-ws-postCode             pic x(4).
        15 out-ws-addressType          pic x(1).
        15 out-ws-streetSDX            pic x(4).
        15 out-ws-localitySDX          pic x(4).
        15 out-ws-lobbySDX             pic x(4).
        15 out-ws-prologue             pic x(100).
     12 out-ws-interface               pic x.
           88 free-format-input        value '1'.
           88 fixed-field-input        value '2'.
           88 XML-input                value '3'.
     12 out-ws-streetMatchFlag         pic x(1).
           88 street-fuzzy                  value '0'.
           88 street-exact                  value '1'.
     12 out-ws-localityMatchFlag       pic x(1).
           88 locality-fuzzy                  value '0'.
           88 locality-exact                  value '1'.
     12 out-ws-repeatLocalityFlag      pic x(1).
           88 no-Locality                  value '1'.
           88 repeatLocality               value '0'.
           *> used if Locality = City
     12 out-ws-ignoreInvalidPostcode   pic x(1).
           88 ignoreInvalidPostCode        value '1'.
           88 reportInvalidPostCode        value '0'.
           *> stops if Post Code is invalid
     12 out-ws-foreignFlag             pic x(1).
           88 foreign-address            value '1'.
           *>stops if foreign address detected
           88 NOT-foreign-address        value '0'.

*> OBJECTS.

01 objSoapClient        object reference value null.

*>--------------------------------------------------------------
Method-id. "begin".
*>--------------------------------------------------------------
*>
*> Interesting - I normally type :-
*>
*> invoke self (this instance) "startup-housekeeping"
*>
*> Guess the compiler knows I'm referring to 'self' !!!

invoke "startup-housekeeping"
invoke "main-logic"
invoke "finalize-objects"

End Method "begin".
*>---------------------------------------------------------------
Method-id. "startup-housekeeping".
*>--------------------------------------------------------------
WORKING-STORAGE SECTION.   *> Only allowed in Net Express

*>WSDL to connect to the remote host (in San Francisco)

*> NOTE : The compiler will tell you if your value (66 below)
*> doesn't equate to the size of the literal

01  WSDL-reference pic x(66) value
z'http://primacomputing.co.nz/AVSWebService/AVSWebService.asmx?WSDL'.

*> WSDL to connect to my IIS server on my new VAIO notebook
*> machine over wireless LAN.
*>
*>    'http://bigblack/AVSWebService/AVSWebService.asmx?WSDL'.
*>
*>I have tested both of the above and they both work perfectly.

  invoke MSSOAP "new" returning objSoapClient
  invoke objSOAPClient "mssoapinit"
            using WSDL-reference
End Method "startup-housekeeping".
*>--------------------------------------------------------------
Method-id. "main-logic".
*>--------------------------------------------------------------

  move spaces to in-IB
  set in-free-format-input to TRUE
*> move '97 21ST AVE TAURANGA' to in-ws-buffer *> A NZ address...
  move '48 35TH BLVD TOURONGA' to in-ws-buffer

*> The commented address above is valid, whereas the second
*> address being used is invalid

  move in-IB to in-interface-block

  *> Note that string parameters to COM objects must be 8197
  *> and must be elemental.

  invoke objSOAPClient "ValidateNZaddress"
    using in-interface-block      *> input interface block
    returning out-interface-block *> output interface block

    *> Note that you could use just one block
    *> but you must reference it in and out because the
    *> Web Service expects in and out parameters

  invoke self "error-fix"

*> Debugging Note
*>
*> Now is a good time to look at out-ws-breakdown and
*> out-ws-buffer...
*>
*> If you are stepping through this in the debugger, note that each
*> field has been filled in,
*> (street number, street, locality, region, and postcode)
*> and the ws-buffer area now contains a properly formatted address
*> which complies with NZPO requirements, and has been converted
*> to mixed case.
*>
*>  out-ws-breakdown
*>  out-ws-buffer

Exit Method.  *> Exit-Method is only really required when you
               *> have a conditional EXIT. Here I'm using
               *> 'Exit Method' as an Animator breakpoint so that
               *> I can view the above two variables

End Method "main-logic".
*>--------------------------------------------------------------
Method-id. "error-fix".
*>--------------------------------------------------------------
*>============== SOAP XML Stringing error fix
*> There is currently a problem with SOAP stripping out certain
*> characters in the returned string. This causes fields to be
*> aligned incorrectly. The following is a quick fix and won't
*> be required once the service is released.
*>

01 J        pic x(4) comp-5.
01 K        pic x(4) comp-5.

    move 1 to K *> output buffer pointer
    perform
        varying J *> input buffer pointer (for this process)
           from 1
             by 1
          until K > function LENGTH (out-IB)
             move out-interface-block (J:1) to out-IB (K:1)
             add 1 to K
             if out-interface-block (J:1) = x'0A'
                move space to out-IB (K:1)
                add 1 to K
             end-if
     end-perform

*>
*>ALL of the above code would be replaced by:
*>
*>   move out-interface-block to out-IB
*>
*>...once the COM server and SOAP wrapper are fixed. (I'm working
*>on it... :-))
*>
End Method "error-fix".
*>--------------------------------------------------------------
method-id. "finalize-objects".
*>---------------------------------------------------------------

  if ObjSoapClient <> null
     invoke ObjSoapClient "finalize" returning ObjSoapClient
  End-if

End Method "finalize-objects".
*>--------------------------------------------------------------
END OBJECT.

END CLASS SoapTest.

*>---------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-24T22:57:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bl9diF2t7s9tU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <5bkie5F2sgf9rU1@mid.individual.net> <EY85i.214410$6m4.184311@pd7urf1no>`

```
Round of applause!!!

Really good stuff, Jimmy.

Some comments below...

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:EY85i.214410$6m4.184311@pd7urf1no...
> By George he's got it ! I think :-). Cut a long story short, I initially 
> downloaded SOAP but doing that Registry check found I already had it. 
…[5 more quoted lines elided]…
> buggering around.

Not sure how you are using "Procedural" here.Maybe MF have a specific 
meaning for it.

Example : I used '$set sourceformt "free"' and for
> some inexplicable reason the compiler queried your line numbers. I had 
> other irritating problems as well. So sod it. Use what you are comfortable 
> with. I went with the Class format - same as you did but now your 
> paragraphs become methods. Here goes :-
>

I like what you did very much. I have reservations about trigger programs 
but it works very well here.

> Give it a shot Rene and confirm that it works for you !
>
…[301 more quoted lines elided]…
> *>---------------------------------------------------------------


This is really cool, Jimmy :-)

I was really pleased to see that my assessment was right and the mssoapinit 
method didn't need the extra parameters. This works when the WSDL is 
referenced from the web service itself, as we did.

It is a signal lesson in checking carefully what you get from the web; the 
information offered was hopelessly out of date.

What I'd like to do is place the code in a 'downloads' directory on the 
server, along with my Fujitsu version and any other versions that people 
offer (maybe Java, C#, AcuCOBOL... whatever). As soon as I have time, I'll 
write an article about the whole process and place that there too, so anyone 
can see the story on accessing the service (or, indeed, any web service) 
from COBOL, or anything else. If you have no objection to this, could you 
mail me a zip of the MF project containing your code?

Finally, what was the response like? The first one would be a bit longer 
because the DB buffers have to be loaded. Also, I currently use a new 
instance of the service each time it is invoked and that takes time. I'm 
looking into that; it gets a bit tricky with DB connections and connection 
scope...

Thanks for spending the time to get this working, I'm sure a number of 
people will use your code.

Pete
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 14)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-24T16:22:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qZi5i.214632$DE1.57499@pd7urf2no>`
- **In-Reply-To:** `<5bl9diF2t7s9tU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <5bkie5F2sgf9rU1@mid.individual.net> <EY85i.214410$6m4.184311@pd7urf1no> <5bl9diF2t7s9tU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Round of applause!!!
> 
…[3 more quoted lines elided]…
> 

> Not sure how you are using "Procedural" here.Maybe MF have a specific 
> meaning for it.

Well you might not like it, but I would call your source 'Procedural' in 
that it is a PROGRAM source as opposed to a CLASS source, although you 
are still creating/accessing objects via invokes. I think the advantage 
of ALL classes is the ability to do a 'round robin' between the various 
classes because you can have an instance handle (object reference) to 
each. (My comment was not based on Micro Focus - they are silent on the 
topic).
> 
> I like what you did very much. I have reservations about trigger programs 
> but it works very well here.
> 
Well of course the early M/F OO examples all did/and still have a 
Trigger program. The main functions are :-

- Menu driven application - from the Trigger start the App(Business 
Logic) and the Master Menu. Return handles from both to the Trigger 
which passes them to the corresponding App and Menu instances

- call "apigui" which kick starts GUIing

This is the trigger for the Corrosion Testing application, which 
illustrates above :-

        *>--------------------ctbegin.cbl--------------------------

        PROGRAM-ID.       ctbegin.

        CLASS-CONTROL.    ctApplication      is class "ctapp"
                          ctMenu             is class "ctmenu"
                          EventManager       is class "p2emgr"
                          Module             is class "module"
                          .

        *>--------------------------------------------------------------
        OBJECT-STORAGE SECTION.
        copy "\copylib\sqlResult.cpy" replacing ==(tag)== by ==01 ws==.
        01 CtResourceID           pic x(10) value z"ctres.dll".

        01 os-App                    object reference.
        01 os-Desktop                object reference.
        01 os-EventManager           object reference.
        01 os-Menu                   object reference.
        01 os-Resource               object reference.

        PROCEDURE DIVISION.

         call "apigui"
         invoke EventManager      "new" returning os-EventManager
         invoke os-EventManager   "initialize"
         invoke os-EventManager   "getDesktop" returning os-Desktop
         invoke Module "newZ"     using CtResourceID
                                  returning os-Resource

         invoke ctApplication     "new"  returning os-App
         invoke ctMenu            "new"  using    os-Desktop
                                         returning os-Menu

         invoke os-App            "passHandles"  using os-Desktop
                                                       os-Menu
                                                       os-Resource
         invoke os-Menu           "passHandles"  using os-Desktop
                                                       os-EventManager
                                                       os-App
                                                       os-Resource
         invoke os-Menu           "createMenu"
         invoke os-Menu           "create"
         invoke os-App            "checkFiles" returning ws-SqlResult


         if    ResultOK
               invoke os-Menu           "show"
               invoke os-EventManager   "run"
         End-if


         STOP RUN.

        *>--------------------------------------------------------------


Now if you look at current M/F Dialog System examples they all start 
with a 'Procedural' which also tends to be the Business Logic. As it is 
Procedural they use entry-points to get at different Sections to handle 
results of different GUI events.

> What I'd like to do is place the code in a 'downloads' directory on the 
> server, along with my Fujitsu version and any other versions that people 
…[4 more quoted lines elided]…
> mail me a zip of the MF project containing your code?

No objections. I'll send you a zip.
> 
> Finally, what was the response like? The first one would be a bit longer 
…[4 more quoted lines elided]…
> 
Mere seconds. To keep it simple I'll have the SoapTrigger invoke my 
DateTime Class, (which I'll also send), to get the Date/Time (pic x 21) 
for start of Trigger and end of Trigger.

PS: Would you refer to your SoapTest.cbl as a standalone or would you 
categorize it as a component ?

Jimmy
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-25T11:26:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bml8iF2tdif2U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <5bkie5F2sgf9rU1@mid.individual.net> <EY85i.214410$6m4.184311@pd7urf1no> <5bl9diF2t7s9tU1@mid.individual.net> <qZi5i.214632$DE1.57499@pd7urf2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:qZi5i.214632$DE1.57499@pd7urf2no...
> Pete Dashwood wrote:
>> Round of applause!!!
…[14 more quoted lines elided]…
> comment was not based on Micro Focus - they are silent on the topic).

OK, that's fair enough.

>
>> I like what you did very much. I have reservations about trigger programs 
…[7 more quoted lines elided]…
> them to the corresponding App and Menu instances

Yes, I've read Wil Price's book. :-)

Similar things can happen with Fujitsu. For example, you may have a .EXE 
that invokes methods from a .DLL. (And, in my case at least, the .DLL is 
usually a COM Server.)

Of course, by encapsulating functionality into a COM Server, you don't need 
a Trigger; it can be dropped and used almost anywhere that supports OO, not 
just COBOL. This gets over the old grizzle we've always had about Class 
interoperability (or the lack of it) in COBOL. I have Java, C#,  COBOL, and 
ASP all using OO  Class methods and properties that are written in COBOL. 
COM empowers this; Web Services take it even further by making it global. 
(In the World sense, not the programming sense... :-))

I don't think it really matters what you call it.

>
> - call "apigui" which kick starts GUIing
…[74 more quoted lines elided]…
> No objections. I'll send you a zip.

Thanks.

>>
>> Finally, what was the response like? The first one would be a bit longer 
…[10 more quoted lines elided]…
> categorize it as a component ?

Definitely a standalone. It is really just a "harness" for testing the proxy 
Class. However the web service, although being around 4000 lines of OO COBOL 
code, I would consider to be a component. (I don't plan on maintaining this 
code, once it has completed all of its testing.) I can't publish the code as 
it is commercially sensitive, but I can tell you it has three main methods 
in the Class, which are supported by other smaller methods:

(Note, I have no qualms about describing these methods publicly, because 
they cannot be accessed directly. Using a web service you decide what will 
be exposed and what won't...)

1. ParseOnly.

This deals with stripping a free format address into words, and attempting 
to locate what is a street, a locality or lobby, a region, and a postcode. 
In my naivety I figured a COBOL UNSTRING would be the caper... I crashed and 
burned :-)  Here's the code that sets the input buffer up so it CAN be 
unstrung into words...

      *
      *   Prepare the data buffer...
      *   Get all words, separated by a single space
      *
           move zero to ws-return
           move spaces to stored-inrec
           move 1 to K
           perform
              varying J
                 from 1
                   by 1
                until J > function STORED-CHAR-LENGTH (ws-buffer)
                  if NOT (ws-buffer (J:1) ALPHABETIC OR ws-buffer (J:1) 
NUMERIC)
                     AND  NOT (ws-buffer (J:1) = '&'
                           OR ws-buffer (J:1) = '-'
                           OR ws-buffer (J:1) = '/'
                           OR (ws-buffer (J:1) = "'"
                           AND ws-buffer (J + 2:1) NOT = space))
                          move space to ws-buffer (J:1)
                          if ws-buffer (J:1) = space AND
                             Function UPPER-CASE (ws-buffer (J + 1:2)) = "S 
"
                             move ws-buffer (J + 1:2) to ws-buffer (J:2)
                          end-if
                          *> removes punctuation and line breaks
                          *> but allows &,-, ' (not apostrophe) and /
                          *> must allow "O'Neill" but not "Neil's"
                  end-if
                  if ws-buffer (J:1)  NOT = space
                     move ws-buffer (J:1) to stored-inrec (K:1)
                     add 1 to K
                     set expecting-space to TRUE
                  else
                     if expecting-space
                        move ws-buffer (J:1) to stored-inrec (K:1)
                        add 1 to K
                        set NOT-expecting-space to TRUE
                     end-if
                  end-if
           end-perform
      *
      * stored-inrec should now be a string of words separated by one 
space...
      *

(nothing is ever as easy as you think... :-) Today, I would write this in C# 
using Regular Expressions, but the COBOL above serves well.)

2.   FIB - Fill in the blanks

This makes sure that any missing address elements are located and validated 
if they can be.

3.   FormatAddress.

Places a correctly formatted address (in compliance with NZPO requirements) 
into the returned buffer. It is constructed from the decomposed elements 
provided by FIB.

So, 3 Major methods, 4000 lines of COBOL code, but the web service exposes 
only one method (ValidateNZaddress). This is a method of the service itself 
(which is also a Class and gets its own object instantiated). The service is 
written in C# but it can use the COBOL Class because the COBOL Class is a 
COM server. (So objects from almost ANY environment (including DotNET) can 
invoke it).

This is my point about components. Encapsulating functionality into a COM 
component (or a Web Service) means you have, in effect, "future proofed" it. 
As long as you need that functionality, it is available, anywhere you want 
it, any time you want it, as "pluggable" functionality.

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 13)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-24T20:48:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180064898.304146.170820@z28g2000prd.googlegroups.com>`
- **In-Reply-To:** `<EY85i.214410$6m4.184311@pd7urf1no>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <5bkie5F2sgf9rU1@mid.individual.net> <EY85i.214410$6m4.184311@pd7urf1no>`

```
On May 24, 12:59 pm, "James J. Gavan" <jgavandeletet...@shaw.ca>
wrote:
>
> Give it a shot Rene and confirm that it works for you !
>

It worked! Well... you did my homework. Thanks Jimmy.

But then I have to build my site for it.... data, COMs, WSDL for you
to view or experiment. I'm going to "emboss" your code and format it
as my template. After reading Price's OO Cobol book it teaches me OO
in Cobol, since then I never really look at procedural programming
anymore (in concept). Though procedurally speaking, all codes are
interpreted by the computer in sequence anyway.

I download the MS SOAP toolkit as well.... got it before it is posted
here from the PDF docs of Microfocus site. Got a few problems with the
COMxxx.OCX files which is "not" included in the downloaded file... but
you can download those OCXs from other sites anyway.

Great job Cobol coders!! Well, for some :)

I'm very thankful really.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-31T11:37:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180636643.671727.127390@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1179977091.567546.22670@n15g2000prd.googlegroups.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com>`

```
On 24 May, 04:24, Richard <rip...@Azonic.co.nz> wrote:
> On May 23, 10:02 pm, "Pete Dashwood"
>
…[12 more quoted lines elided]…
> manuals.

v3 was Event driven, as per VB.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-01T11:09:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c92spF2v23juU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <1180636643.671727.127390@k79g2000hse.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1180636643.671727.127390@k79g2000hse.googlegroups.com...
> On 24 May, 04:24, Richard <rip...@Azonic.co.nz> wrote:
>> On May 23, 10:02 pm, "Pete Dashwood"
…[19 more quoted lines elided]…
>

No, that was PowerCOBOL V3.

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 13)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-01T09:48:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180716506.641544.60940@u30g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<5c92spF2v23juU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <1180636643.671727.127390@k79g2000hse.googlegroups.com> <5c92spF2v23juU1@mid.individual.net>`

```
On 1 Jun, 00:09, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[32 more quoted lines elided]…
> - Show quoted text -

Yep. I thought, after I had just sent the email, that someone
(expletives deleted) would correct me on that.

It was indeed Powercobol v3.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-02T10:53:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cbmc2F2vhtghU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <1180636643.671727.127390@k79g2000hse.googlegroups.com> <5c92spF2v23juU1@mid.individual.net> <1180716506.641544.60940@u30g2000hsc.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1180716506.641544.60940@u30g2000hsc.googlegroups.com...
> On 1 Jun, 00:09, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[41 more quoted lines elided]…
>

Nothing personal... just in the interests of accuracy :-)

The expletives may well apply anyway :-)

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 15)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-02T05:16:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180786571.591765.14730@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<5cbmc2F2vhtghU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <1179896963.555487.99600@k79g2000hse.googlegroups.com> <5bihpvF2st47eU1@mid.individual.net> <1179977091.567546.22670@n15g2000prd.googlegroups.com> <1180636643.671727.127390@k79g2000hse.googlegroups.com> <5c92spF2v23juU1@mid.individual.net> <1180716506.641544.60940@u30g2000hsc.googlegroups.com> <5cbmc2F2vhtghU1@mid.individual.net>`

```
On 1 Jun, 23:53, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[52 more quoted lines elided]…
> - Show quoted text -

No, expletives were along the line of "oh, f****** **** I should have
said Powercobol; I bet that ******* **** ******** picks me up on
that." More in anger at myself than at anyone else. Mind you, if your
shoulders are broad enough....
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 8)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-24T21:02:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z3n5i.215000$DE1.77290@pd7urf2no>`
- **In-Reply-To:** `<5bhse6F2shrgvU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net>`

```
Pete Dashwood wrote:

Just in case you are itching to know runtimes based on following as 
modified, plus I also used your 'good address' :-

*>----------------- soaptrigger.cbl ----------------------------

*> Trigger PROCEDURAL program used here. Assume Soaptest was
*> selected from a Mster Menu - then the Menu would invoke in a
*> similar manner.

Program-id.         SoapTrigger.

Class-Control.      SoapTest        is class "soaptest"
                     DateAndTime     is class "datetime"
                     .
WORKING-STORAGE SECTION.
01 os-SoapTest             object reference value null.
01 os-DateTime             object reference value null.

01 DateTime-start          pic x(21).
01 DateTime-finish         pic x(21).

PROCEDURE DIVISION.

invoke DateAndTime "new"  returning os-DateTime

invoke os-DateTime "getDateAndTime21"
                               returning DateTime-start
invoke SoapTest    "new"      returning os-SoapTest
invoke os-SoapTest "begin"
invoke os-DateTime "getDateAndTime21"
                               returning DateTime-finish

display "Soap Demo       ccyymmddhhmmsshhGhhmm"
display "Start of demo : " DateTime-start
display "End   of demo : " DateTime-finish

STOP RUN.

*>--------------------------------------------------------------

         Soap Demo Results :-

        Soap Demo       ccyy mm dd hh mm ss hh G hhmm
        Start of demo : 2007 05 24 14 37 20 62 - 0700
        End   of demo : 2007 05 24 14 37 21 89 - 0700

        Soap Demo       ccyy mm dd hh mm ss hh G hhmm
        Start of demo : 2007 05 24 14 41 23 54 - 0700
        End   of demo : 2007 05 24 14 41 24 60 - 0700

        Soap Demo       ccyy mm dd hh mm ss hh G hhmm
        Start of demo : 2007 05 24 14 51 20 35 - 0700
        End   of demo : 2007 05 24 14 51 21 78 - 0700
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-25T11:36:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bmls7F2su2s5U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <1179799892.138533.30050@n15g2000prd.googlegroups.com> <g2v4i.206393$aG1.36136@pd7urf3no> <5bg5eaF2r5gf5U1@mid.individual.net> <1179887604.069942.171890@q66g2000hsg.googlegroups.com> <5bhse6F2shrgvU1@mid.individual.net> <Z3n5i.215000$DE1.77290@pd7urf2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:Z3n5i.215000$DE1.77290@pd7urf2no...
> Pete Dashwood wrote:
>
…[52 more quoted lines elided]…
>        End   of demo : 2007 05 24 14 51 21 78 - 0700

Thanks very much for that, Jimmy.

Always less than 1.5 seconds... acceptable. (I am working to improve it of 
course.)

This matches the results I am getting here pretty closely, so the distances 
don't seem to matter.

(I've seen local systems with worse performance than that, and some of those 
were on mainframes (TSO...and CICS))

It's pretty amazing really that the Net can be that fast.

I'll be posting a batch demo to the site soon... :-)

Pete.

PS I read somewhere that it is necessary to have IIS installed in order to 
run SOAP. I can't see why it would be, but can you confirm whether you have 
it installed on your version of XP? (Home Edition doesn't have it, XP Pro 
does not have it installed by default, you have to do it.)
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T00:46:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aM4i.14101$j63.2043@newsread2.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5beo1dF2s776oU1@mid.individual.net...
>
<snip>

> Speaking of reading... I am working my way through "The Singularity is 
> Near" as you recommended.  I find it stimulating and interesting. Will 
> post my overall impressions when I've finished it. At 20 minutes a night, 
> it may be some time...:-)
>
Good I am glad that you are enjoying it.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T00:55:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5beo1dF2s776oU1@mid.individual.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[27 more quoted lines elided]…
>
I have a feeling that I may never use Java at work, but then I am not good 
at predicting the future. I am still interested in a language for my 
retirement day's hobby programming and it could be Java but I think I should 
also conside C#. I have an interest in AI and have a shelf full of books I 
was saving for retirement, but after reading Kurzweil I have decide not to 
wait. I will probably learn Scheme and/or Lisp at some point.

I know it will probably not be C++ although I have a shelf of book on that 
as well.

I have learned far more about OO from learning Java than from C++ or OO 
COBOL books. It is no silver bullet but I can see how it improves some 
things.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-23T13:21:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bhj8jF2rrq02U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net...
>
<snip>
>
> I have learned far more about OO from learning Java than from C++ or OO 
> COBOL books. It is no silver bullet but I can see how it improves some 
> things.

Yes, I had exactly the same experience. OO is such an innate part of Java 
that it just seems completely natural.

For me, OO opens the way to component based design and programming. The code 
posted in this thread is a concrete example of what I have been talking 
about; the web service is simply a component exposed to the Internet. You 
can plug it into your applications and not need to maintain it or worry 
about it. (Conceptually it is just like an extension of the OS; you use it 
every day and expect it to work as specified. It does what it does.)

Components may be the keys to the kingdom, unlocking Lamba functions and 
functional programming and helping to move us toward Kurzweil's Singularity.

If you have a COBOL compiler on your home system, that supports OO, I would 
urge you to try the code. (We will have a MicroFocus version any time now, 
as well as the original Fujitsu NetCOBOL version which will work with ANY 
version of Fujitsu COBOL, right back to version 3.)

Why not attempt a Java Class to access it? (Kinda cool to have COBOL being 
invoked by Java across thousands of miles :-))

Researching how to access web services from Java is probably very useful for 
both your Java and your web services learning.

If you get stuck, I can help.

I would LOVE to see an AcuCOBOL or Websphere version. It really is fun to 
access web services, and very useful...

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-23T22:08:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vX25i.211534$DE1.22871@pd7urf2no>`
- **In-Reply-To:** `<5bhj8jF2rrq02U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
> news:6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net...
…[5 more quoted lines elided]…
>>things.

Charles, I recall Thane writing the same thing, sometime back, about
learning OO from Java. Exactly which OO COBOL books are you referring to   ?
> 
> <snip>> 
…[3 more quoted lines elided]…
> version of Fujitsu COBOL, right back to version 3.)

Well you might have an M/F version soon - perhaps ? :-). I gotta
problem. I have your WSDL-reference as one literal - so no problem
there, just that I'm curious why it has a ?(question mark) instead a
period.) before 'WSDL'.

Independently I've used the highlighted WSDL-Reference in Google abd 
with and without 'WSDL' I get your main AVS Web Service Page or your 
your WSDL file layout. So the literal is complete.

Problem seems to be with initializing SOAP; having referenced the SOAP
toolkit I tried both the methods "mssoapinit" and "mssoapinit2" - the
first gives a more verbose lists of errors - but essentially I don't
think it's finding SOAP :-

         set not-finished to TRUE
         invoke MSSOAP "new" returning objSoapClient
         move length of wsdl-reference to ls-length
         invoke objSOAPClient "mssoapinit"
                   using WSDL-reference

The length above was just checking the actual size of the literal.

I didn't want to get into all this SOAP SDK or M/F detail, but from 
viewing M/F demos I get the impression I have got to REGISTER SOAP and 
tell the application where it is on my disk. Any pointers ? As I'm using 
N/E V3.1 and you obviously were looking at M/F books before - see if the 
book 'Distributed Computing' can put me on right track :-

http://supportline.microfocus.com/documentation/books/nx31sp1/nx31indx.htm

Here's an extract from one of the M/F Demos, (which of course is not
on-line) :-
-------------------------------------------------------------------------------
    HOW TO RUN THIS DEMO

    ====================

    Load the project OBJECTS.APP, compile the client, and compile

    and link the server.



    Either:

    o Edit the registry file for the server so that the server

      directory is correct. Register the server by right-clicking

      on the .reg file and selecting "Register".



    Or:

    o Edit OBJECTSERVERTRIGGER.CBL so that the CommandLine

      contains the correct path to the application. Then rebuild

      the server and run it from the command line:

          objectserver /register



      You can also unregister the server using the command line:

          objectserver /unregister



    Running the client will start the server (if it is not already

    running).



    The client will pass the server a variety of object references

    and other data types using the method "PassObject".



    For each method call, the server will display the type and

    value(s) contained by the objects it receives.



    The objects passed to the server include character arrays,

    variants, SafeArrays and OLE objects.



    After each method call, the client will wait for a key press, so

    that you can check the server has received the data correctly.



    You can animate the demo in two ways:

    1) Animate the client by clicking on the "Step" button. The

       server will not animate as part of this session.

    2) Animate the server by right-clicking on "objectserver.exe" and

       selecting "Animate". The server will start animating in the

       trigger program. Select "run" so that the server becomes

       available to OLE clients. You may then run the client by

       executing

             "run objectclient"

       from within a Net Express command line. You should set a

       breakpoint within the method to enable stepping through the

       server code. As the server is linked as a character

       application, output is sent to a separate console window.



    WHAT TO DO IF SOMETHING GOES WRONG

    ==================================

    1. Make sure that you have correctly registered the server -

       in the registry file, directory names should be separated

       with '\\' (double back-slashes).

       Incorrect server registration is the most common error.



    2. Make sure that both objectclient.cbl and

       objectserver.cbl have been compiled with the

       directive ooctrl(+p).

       This allows the run-time to access parameter information.



    3. Check that the server has been linked as "Shared" and

       "Dynamic" as this allows the server to be run without

       COBOL environment variables.



    4. Check that the trigger program is linked within the

       server program, and is the first part of the server to

       execute (either by being first in the .obj list or by

       specifying it as the entry point name for the EXE).



    5. Check that all methods called have the correct parameters

       and return types according to the documentation.



------------------------------------------------------------------------
They compose this with a Wizard but this is the Objectserver.REG file :-

REGEDIT4



[HKEY_CLASSES_ROOT\objectserver]

@="COBOL objects demo server"



[HKEY_CLASSES_ROOT\objectserver\Clsid]

@="{E51CF674-C021-11D2-9637-00A0C906773E}"



[HKEY_CLASSES_ROOT\CLSID\{E51CF674-C021-11D2-9637-00A0C906773E}]

@="COBOL objects demo server"



[HKEY_CLASSES_ROOT\CLSID\{E51CF674-C021-11D2-9637-00A0C906773E}]

"AppID"="{E51CF674-C021-11D2-9637-00A0C906773E}"



[HKEY_CLASSES_ROOT\CLSID\{E51CF674-C021-11D2-9637-00A0C906773E}\ProgID]

@="cobol.demo.objectserver"



[HKEY_CLASSES_ROOT\CLSID\{E51CF674-C021-11D2-9637-00A0C906773E}\LocalServer32] 


@="C:\\netexpress\\base\\demo\\oledemos\\objects\\debug\\objectserver.exe"



[HKEY_CLASSES_ROOT\CLSID\{E51CF674-C021-11D2-9637-00A0C906773E}\InprocServer32] 


@=""


Where the line above starts with 'netexpress' - my direcotry hierarchy 
actually is :-

C:\\program files\\merant\\netexpress etc.....
--------------------------------------------------------------------------------

I would have thought if we get the correct link with the WSDL-Reference,
then the program probably works as sweet as a nut.

You know, there's nothing wrong with OO or COBOL - while important, it's 
all this extraneous crap, minute detail, permutations etc., that you 
have to get your head around for GUIs and Webbing - and it is not a 
quick 5-minute exercise to absorb this stuff. That's why I decided to 
call it quits with programming - I'm still enjoying and watching the 
grass grow, but bugger ! It's raining again and the grass needs cutting.

Meanwhile we have a N. American Robin (same size as an English Thrush), 
which has nested in the arm of one of our downpipes. Be fascinating to 
see if it stays the course and has babes.

Jimmy
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T23:58:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Fy45i.18424$3P3.8716@newsread3.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <vX25i.211534$DE1.22871@pd7urf2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:vX25i.211534$DE1.22871@pd7urf2no...
> Pete Dashwood wrote:
>> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[12 more quoted lines elided]…
>> <snip>>

Well the best one was "Object Orientation for COBOL Programming" by Ray 
Obin. It was good as far as it went but was pretty much an introduction.

The worst was "Object Oriented Development in COBOL" by Topper.

Somewhere in between was "Elements of Object Oriented COBOL" by Wilson 
Price. I remember finding a lot of erros such as code not matching examples 
etc. At one time I had a list of the errors but it has become irretrievably 
lost.

I was always hampered by not having a compiler to experiment with.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-24T01:47:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t865i.215729$aG1.51526@pd7urf3no>`
- **In-Reply-To:** `<Fy45i.18424$3P3.8716@newsread3.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <vX25i.211534$DE1.22871@pd7urf2no> <Fy45i.18424$3P3.8716@newsread3.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:vX25i.211534$DE1.22871@pd7urf2no...
…[31 more quoted lines elided]…
> 
Ray's book is the one I've recently been quoting from. I got it as soon 
as I was aware of its availability, but other than historically, I 
really didn't glean too much from the examples which were really just 
illustrating isolated syntax - still to be fair, I think that was the 
intent.

Our friend Andrew Topper - If not the worst, certainly the second worst 
- the one I always think of when I talk about theoretical books with 
graphs and tables - absolutely bloody useless.

Will Price book - never had the problems you are talking about, because 
I was just reading the examples to get his ideas. (I already had 
familiarity with Net Express, so what he was describing wasn't entirely 
new). I could have used his stuff with Net Express but really didn't 
need to. I enjoyed Will's book, as did others, Donald and Pete for two. 
He illustrated so much, but as he went topic by topic you didn't 
immediately get a handle on Design Patterns that you referred to; his 
examples started with a Procedural program invoking other Programs which 
were classes. Bear in mind the tutorial style. However, having asked 
him, in the real world he would for preference code solely in OO COBOL 
classes, with no use of Procedurals.

The book you sadly missed - Edmund Arranga/Frank Coyle. That's the very 
first I read, even before Will. As well as describing the syntax it 
finishes up with a coded in-house library application, and other than 
the Procedural trigger program the application is all classes. Certainly 
illustrates dividing the application up into logical units (classes) and 
covers the ground about Design Patterns relative to accessing databases.
This is the book that really got me going, supplemented by an extension 
of ideas in Will's book. (Arranga/Coyle - probably still available from 
amazon as a second-hand).

Even looking at the Arranga/Coyle application, I agree, it is real tough 
to get a handle on OO, the sequencing as it jumps(invokes) from one 
class to another - without a compiler to animate/debug and follow 
program flow. You've gone the Java route - but there's always that Net 
Express Personal Edition which you could download.

Jimmy
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-24T12:57:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bk67fF2sp5f6U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <vX25i.211534$DE1.22871@pd7urf2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:vX25i.211534$DE1.22871@pd7urf2no...
> Pete Dashwood wrote:
>> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[20 more quoted lines elided]…
> period.) before 'WSDL'.

The question mark is a standard way of posting parameters using HTTP POST 
and GET. It is required.
>
> Independently I've used the highlighted WSDL-Reference in Google abd with 
> and without 'WSDL' I get your main AVS Web Service Page or your your WSDL 
> file layout. So the literal is complete.

Yes, that is expected behaviour. You should be able to input the URL into a 
Browser and get the Web Service description.

http://primacomputing.co.nz/AVSWebService/AvsWebService.asmx

..brings up the description, and clicking on the method shows samples opf 
SOAP code that could be used at a very low level if you didn't have the SOAP 
toolkit and were doing everything manually. (It is really just XML in and 
XML out.)
>
> Problem seems to be with initializing SOAP; having referenced the SOAP
…[5 more quoted lines elided]…
>         invoke MSSOAP "new" returning objSoapClient

Have you checked objSOAPClient to make sure it instantiated SOAP correctly? 
If it didn't, you may not have SOAP installed on your system. This is where 
an Object Browser comes in Handy :-). If you don't have one, run RegEdt32. 
Do  "find" on "MSSOAP.SoapClient". If it doesn't find it, you will need to 
install the SOAP toolkit.

You can download it from:

http://www.microsoft.com/downloads/details.aspx?FamilyId=C943C0DD-CEEC-4088-9753-86F052EC8450&displaylang=en

It will install itself and you DON'T need to register it with Regsvr32 as it 
is self-registering.

Then try the code again and see if the Class instantiates.

>Problem seems to be with initializing SOAP; having referenced the SOAP
>toolkit I tried both the methods "mssoapinit" and "mssoapinit2" - the
>first gives a more verbose lists of errors - but essentially I don't
>think it's finding SOAP :-

mssoapinit2 should not be used for this; it has a different parameter list.

>
>        set not-finished to TRUE
…[9 more quoted lines elided]…
> tell the application where it is on my disk.

No. Not nowadays. (Registration tells anything that wants to use it, where 
it is)

All COM Servers need to be registered. This is done by a program called 
Regsvr32 which is in your windows/system32 directory. However, if you are 
reading docs that tell you to register SOAP, they must be very old. As noted 
above, it is self-registering.

If you really want to be sure, you can open a DOS box and type: regsvr32 
<path to mssoap.dll, for example: c:\windows\system32\mssoap.dll (check 
where this .dll is located; it may vary on different systems)>

You can de-register a COM server with the same program, using the -u 
parameter.

Registration makes the necessary entries in your system registry for the 
Class, and ensures that only one copy (the copy you have registered) gets 
used by anything that invokes it. You can overwrite the .dll (with a new 
version, for example) and you don't have to re-register it again.


 Any pointers ? As I'm using
> N/E V3.1 and you obviously were looking at M/F books before

No, I wasn't looking at MF Books; I simply located some MF code samples 
posted by other people.  Because I have a lot of experience at building and 
using COM servers, I knew what to look for.

- see if the
> book 'Distributed Computing' can put me on right track :-
>
> http://supportline.microfocus.com/documentation/books/nx31sp1/nx31indx.htm


I went and had a look and found...

http://supportline.microfocus.com/documentation/books/nx31sp1/wspubb.htm

This looks like it could have been the basis for the code I found. It is way 
out of date and SOAP 3.0 works differently.

This code shows the mssoapinit call as:

78  WSDL-Url value
     z"http://www.xmethods.net/sd/2001/CATrafficService.wsdl".
 01  WSML-Url pic x value x"00".

 procedure division.
     invoke MSSOAP "new" returning Soap
     invoke Soap "mssoapinit" using WSDL-Url
                                    z"CATrafficService"
                                    z"CATrafficPort"
                                    WSML-Url

mssoapinit for SOAP 3 does not need some of these parameters.
It may well be that COBOL passes the WSDL string without it needing to be 
specified as ASCIIZ also. (COBOL may add the null to the end of it under the 
covers). Not sure how MF COBOL passes strings to called routines.

You could try removing the z and simply passing the WSDL string as my code 
does.

I'd need to see the errors you are getting before I can be sure.



>
> Here's an extract from one of the M/F Demos, (which of course is not
> on-line) :-
> -------------------------------------------------------------------------------
>    HOW TO RUN THIS DEMO

This is a lot of sweat and totally not necessary for the instance we are 
looking at.

You would only do this if you were BUILDING the COM Server... (It makes me 
appreciate how much housekeeping Fujitsu do for you under the covers...)

I've snipped this as it is just muddying the water.

<snipped very tedious details that no one should have to wade through... 
:-)>
>
> I would have thought if we get the correct link with the WSDL-Reference,
> then the program probably works as sweet as a nut.

Yes, I hope so... :-) It certainly does when I run it.

I think you have put your finger on it, Jimmy. We need to get the mssoapinit 
call to function correctly.

I see the following steps:

1. Make sure you have the mssoap.dll installed as mentioned above.

2. Try defining the WSDL string with and without the z prefix.

I had a look around the web and SOAP 3 doesn't require the "extra" 
parameters in the sample above. You must have the URL correct and that means 
having the .asmx suffix and the question mark with WSDL after it.

If you can post the error messages you get (privately or here) I can 
probably pin it down better.

3. If all else fails try...

78  WSDL-Url value
     z"http://primacomputing.co.nz/AVSWebService/AVSWebService.asmx?WSDL".
01  WSML-Url pic x value x"00".

 procedure division.

     Having established a SOAP instance...(objSOAPClient is not null...)

     invoke  objSOAPClient  "mssoapinit" using WSDL-Url
                                    z"ValidateNZaddress"
                                    z""
                                    WSML-Url
     end-invoke


>
> You know, there's nothing wrong with OO or COBOL - while important, it's 
…[4 more quoted lines elided]…
> but bugger ! It's raining again and the grass needs cutting.

I completely agree. The mind numbing detail SHOULD be under the covers. (I 
was shocked when I read what was there...it looks like MF use their own 
registration process for servers when regsvr32 does it perfectly well. They 
would argue it's done by a wizard so there's no need for people to worry 
about it, and that is probably fair.)
>
> Meanwhile we have a N. American Robin (same size as an English Thrush), 
> which has nested in the arm of one of our downpipes. Be fascinating to see 
> if it stays the course and has babes.

No chance it will get washed away? (I'm thinking a miniature umbrella :-))

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T23:39:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5bhj8jF2rrq02U1@mid.individual.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[41 more quoted lines elided]…
>

I do not have any COBOL compiler on my PC.  Well I have CDs with some very 
old ones or university editions but I have not installed them.

I know Java has something called Java Webstart but it may not be the same as 
invoking a web service. I think it is more like having your app on one 
server and everybody runs it from there and you only update it there. Well I 
do not know the details.  Perhaps if Oliver reads this he can tell us. If I 
can find the time I will try to figure out how to do this in Java to see 
what I can learn.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-25T00:10:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[38 more quoted lines elided]…
>>
<snip>

Well I made an attempt at invoking your web service from Java, but I did not 
have much spare time so it was not completely successful.

I only have one book that talk about Java and web services: Just Java 2 6th 
edition and it is a little dated (2004).  Chapter 28, mostly talks about two 
beta programs through Amazon ans Google. While they looked straightforward 
enough I decided I did not have time for that approach.

There is also the Apache Axis package.  I think when I have more time I will 
try using it.

Basically they all process the WSDL and generate Java you can use in you 
program to access the web servive.

I googled  on "java invoke web service" and got more than 54 million hits 
and there is lots of good stuff but most of it too long for the remaining 
time I had left. At http://www.codeproject.com/soap/WSfromJava.asp I found 
what looked like something short enough to try. It was a simple applet that 
invoked a web service called ConcatWithSpace.  It takes two string as input 
and returns them concatenated with a space in the middle.  One drawback is 
it is for JDK 1.1. The entire web article is pretty short.

I downloaded the code, a Java program  for the applet, which also has a 
SoapRequestBuilder class, and a html page that invokes the applet and passes 
the required parameters. I thought I could figure out the parms from your 
WSDL and just change the web page to invoke your web service, but I must be 
doing something wrong. I tried many variations but I always get: "Error: 
access denied (java.net.SocketPermission)".  Well I realize I am not 
knowledgeable yet in this area of Java which is one reason for making the 
attempt. Anyway I am sure this approach is not the best in general and Axis 
is a better way to go. I see O''Reilly has a Java Web Services book.  Just 
what I need, another book added to my already very long list.

Here is the original html code for invoking the ConcatWithSpace service, 
which I assume worked:

<HTML><HEAD>
<TITLE>Applet HTML Page</TITLE>
</HEAD>

<BODY>
<H3><HR WIDTH="100%">Applet HTML Page<HR WIDTH="100%"></H3>

<applet code="SOAPexample" width=400 height=50>
<param name="server" value="127.0.0.1">
<param name="method" value="ConcatWithSpace">
<param name="xmlnamespace" value="http://tempuri.org/">
<param name="webservicepath" value="/SimpleService/Service1.asmx">
<param name="string1" value="David">
<param name="string2" value="Hobbs">
</applet>

<HR WIDTH="100%">
</BODY></HTML>

Here is the modified version of the html:

<HTML><HEAD>
<TITLE>Applet HTML Page</TITLE>
</HEAD>

<BODY>
<H3><HR WIDTH="100%">Applet HTML Page<HR WIDTH="100%"></H3>

<applet code="SOAPexample" width=400 height=50>
<param name="server" value="http://primacomputing.co.nz/AVSWebService/">
<param name="method" value="ValidateNZAddress">
<param name="xmlnamespace" 
value="http://primacomputing.co.nz/AVSWebService/">
<param name="webservicepath" value="/AVSWebService.asmx?WSDL">
<param name="string1" value="97 21ST AVE TAURANGA">
</applet>

<HR WIDTH="100%">
</BODY></HTML>

Here is the original Java code for the applet. I ran out of time ( I got 
interrupted) before I could try to modify it. One change it needs for 
certain is to comment out the logic for the second parameter being passed as 
your web service only expects one input paramter. I did try running it 
anyway in the hope that it would just ignore the second parameter. Perhaps 
you or someone here can get it running. I am so sure that it is not the best 
approach in general that I will wait until I can devote proper time to the 
Axis approach. Well there might be even better ways, after all I am just a 
couple hours into my investigations.

import java.applet.Applet;
import java.awt.*;
import java.net.*;
import java.util.*;
import java.io.*;

public class SOAPexample extends Applet {

  private String response = "Nothing";

  public void init() {
    SoapRequestBuilder s = new SoapRequestBuilder();
    s.Server = getParameter("server");
    s.MethodName = getParameter("method");
    s.XmlNamespace = getParameter("xmlnamespace");
    s.WebServicePath = getParameter("webservicepath");
    s.SoapAction = s.XmlNamespace+s.MethodName;
    s.AddParameter("one", getParameter("string1"));
    //s.AddParameter("two", getParameter("string2"));
    response = s.sendRequest();
    repaint();
  }

  public void paint(Graphics g) {
    g.setColor(Color.black);
    Font f = new Font("TimesRoman", 0, 20);
    g.setFont(f);
    g.drawString(response, 10, 20);
  }

  public void start() {
    repaint();
  }
}

class SoapRequestBuilder {
  String Server = "";
  String WebServicePath = "";
  String SoapAction = "";
  String MethodName = "";
  String XmlNamespace = "";
  private Vector ParamNames = new Vector();
  private Vector ParamData = new Vector();

  public void AddParameter(String Name, String Data) {
    ParamNames.addElement( (Object) Name);
    ParamData.addElement( (Object) Data);
  }

  public String sendRequest() {
    String retval = "";
    Socket socket = null;
    try {
      socket = new Socket(Server, 80);
    }
    catch (Exception ex1) {
      return ("Error: "+ex1.getMessage());
    }

    try {
      OutputStream os = socket.getOutputStream();
      boolean autoflush = true;
      PrintWriter out = new PrintWriter(socket.getOutputStream(), 
autoflush);
      BufferedReader in = new BufferedReader(new InputStreamReader(socket.
          getInputStream()));

      int length = 295 + (MethodName.length() * 2) + XmlNamespace.length();
      for (int t = 0; t < ParamNames.size(); t++) {
        String name = (String) ParamNames.elementAt(t);
        String data = (String) ParamData.elementAt(t);
        length += name.length();
        length += data.length();
      }

      // send an HTTP request to the web service
      out.println("POST " + WebServicePath + " HTTP/1.1");
      out.println("Host: localhost:80");
      out.println("Content-Type: text/xml; charset=utf-8");
      out.println("Content-Length: " + String.valueOf(length));
      out.println("SOAPAction: \"" + SoapAction + "\"");
      out.println("Connection: Close");
      out.println();

      out.println("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
      out.println("<soap:Envelope 
xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" 
xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" 
xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">");
      out.println("<soap:Body>");
      out.println("<" + MethodName + " xmlns=\"" + XmlNamespace + "\">");
      //Parameters passed to the method are added here
      for (int t = 0; t < ParamNames.size(); t++) {
        String name = (String) ParamNames.elementAt(t);
        String data = (String) ParamData.elementAt(t);
        out.println("<" + name + ">" + data + "</" + name + ">");
      }
      out.println("</" + MethodName + ">");
      out.println("</soap:Body>");
      out.println("</soap:Envelope>");
      out.println();

      // Read the response from the server ... times out if the response 
takes
      // more than 3 seconds
      String inputLine;
      StringBuffer sb = new StringBuffer(1000);

      int wait_seconds = 3;
      boolean timeout = false;
      long m = System.currentTimeMillis();
      while ( (inputLine = in.readLine()) != null && !timeout) {
        sb.append(inputLine + "\n");
        if ( (System.currentTimeMillis() - m) > (1000 * wait_seconds)) 
timeout = true;
      }
      in.close();

      // The StringBuffer sb now contains the complete result from the
      // webservice in XML format.  You can parse this XML if you want to
      // get more complicated results than a single value.

      if (!timeout) {
        String returnparam = MethodName + "Result";
        int start = sb.toString().indexOf("<" + returnparam + ">") +
            returnparam.length() + 2;
        int end = sb.toString().indexOf("</" + returnparam + ">");

        //Extract a singe return parameter
        retval = sb.toString().substring(start, end);
      }
      else {
        retval="Error: response timed out.";
      }

      socket.close();
    }
    catch (Exception ex) {
      return ("Error: cannot communicate.");
    }

    return retval;
  }
}
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 7)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-25T00:17:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zWp5i.13255$Ut6.9618@newsread1.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[276 more quoted lines elided]…
>

Sorry the web service is SimpleService/Service1.asmx and the method name is 
ConcatWithSpace.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-25T22:09:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bnqv4F2rp0c0U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net>`

```
Hi Charlie,

I had a quick look at this but there are too many things wrong with it for 
me to fix it at the moment.

The Web Page is fine (I have one question on it but don't have time to check 
it out) but there are problems in the Java Applet. If the SOAP Class is 
invoked it shouldn't require a socket connection (it will make its own) and 
it looks to me as if you are doing something that is very low level (and 
unnecessary, if the SOAP COM server is used, as Jimmy and I did.)

I'm flat out this weekend doing a major address conversion with the AVS 
engine, but I'll have a look at it next week if none of the Java experts 
here have picked it up meanwhile, or if you haven't been able to do it 
yourself...

Thanks for having  a go... I bet you learned something :-)

Pete.

TOP POST - nothing new below.



"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[276 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-29T01:20:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net>`

```
Top Post not more below

Hi! Pete,

I downloaded Axis 1.4 and if it works as the documentation says I believe it 
would not be too difficult to do the few steps required to invoke a web 
service.
Not sure when I might get around to it though.

My wife is pregnant and we spent today in the emergency room as she was 
experiencing severe pain on her left side.  They think the cause of the pain 
is not a threat to the baby, but the sonogram showed a possible birth defect 
( a hole in the abdominal wall), something like a hernia. Tomorrow they will 
give us the name of a specialist.  If  this is the only problem and if the 
baby can develop long enough then he/she may have a chance. However 25% to 
40% of the babies with this problem have other birth defects. I am feeling 
kind of low and web services will have to take a back seat for quite a 
while.

Sorry to lay this on you.  I do not have a lot of friends and some of the 
ones I did have disapproved of my latest marraige and abandoned our 
friendship. I tried calling my two children but they are not home.  The 
people on this group are pretty much the closest thing I have to friends and 
I just had to let this out to someone.

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5bnqv4F2rp0c0U1@mid.individual.net...
> Hi Charlie,
>
…[306 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-28T21:28:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ridnQRtr-AqHMbbnZ2dnUVZ_vfinZ2d@golden.net>`
- **In-Reply-To:** `<6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> My wife is pregnant and we spent today in the emergency room as she was 

Some things are a lot more important than code.  For what it's worth, 
another semi-hermit send his best wishes, and a thumbs up for luck.

Donald
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-28T20:35:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66ydnbtKisA-DMbbnZ2dnUVZ_rrinZ2d@comcast.com>`
- **In-Reply-To:** `<6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> 
> My wife is pregnant and we spent today in the emergency room as she was 
…[13 more quoted lines elided]…
> I just had to let this out to someone.

You've got thoughts and prayers headed your way from Albuquerque.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-29T14:36:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c1hsnF2uuqhfU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net...
> Top Post not more below
>
…[17 more quoted lines elided]…
> Sorry to lay this on you.

Absolutely do NOT apologise... :-)  There isn't much any of us here can do, 
apart from give you moral support. Speaking only for myself, you have it.


> I do not have a lot of friends and some of the ones I did have disapproved 
> of my latest marraige and abandoned our friendship.

With "friends" like that, you don't need enemies. People who would judge you 
for your personal actions, which have nothing to do with anyone else, are 
people who you are probably better off without.

> I tried calling my two children but they are not home.  The people on this 
> group are pretty much the closest thing I have to friends and I just had 
> to let this out to someone.

I understand. Glad you did. I'm sure some here will know what you are going 
through, and most can empathise with the stress you  are under.

Don't worry at all about the web services :-)

My exercise over the weekend went very successfully and I am under less 
pressure now than I was, although I still have a huge amount of work to do 
on the AVS web site. (I spent most of this morning furthering my education 
via a Web Cast on Master Pages and Themes (all really good stuff; I am 
persuaded to stop with CSS and go to themes instead :-)))

On the web service from Java...
 I see the real problem as being able to access COM from Java (Once you 
establish connection to the SOAP COM proxy, the rest is just stamp 
collecting :-)). Bearing this in mind, I found that IBM are offering an 
approach that is free and looks very useful. I have downloaded their 
Bridge2Java software from the article "Bridging the gap to COM"

http://www.ibm.com/developerworks/java/library/j-bridge/

From my web searches I found a number of offerings that did the same; some 
of them were really excellent, but expensive...

If I can find some time and need a break from C# and Web stuff, I'll attempt 
to implement the Java link to the web service.

However, it might be interesting to compare the IBM approach with the Axis 
one, so please do it if you have time or need to bury yourself in something 
that may help to take your mind off your immmediate problems. (In the course 
of my life I have found working to be a very useful therapy when trauma 
strikes...but that might just be me.)

Meantime, very best wishes for a safe delivery with mother and child both 
fine. Try not to let it get you down.

Pete.



<previous unreferenced snipped>
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-28T20:51:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V7GdnePvfu-xCMbbnZ2dnUVZ_ualnZ2d@comcast.com>`
- **In-Reply-To:** `<5c1hsnF2uuqhfU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net>`

```
Pete Dashwood wrote:
> (I spent most of this morning furthering my education 
> via a Web Cast on Master Pages and Themes (all really good stuff; I am 
> persuaded to stop with CSS and go to themes instead :-)))

Nah - don't dump CSS.  Master pages with a good CSS file will work out well.

On a completely off-topic, unrelated topic - I just made a change to a 
theme (WordPress, not dotNet) using CSS and a custom image.  It's on my 
new "weekly devotions" site - anywhere there's a quote from the Bible, 
it's got a ribbon on the bottom that looks like a bookmark.  It's linked 
from my personal blog's home page under "Weekly Devotions".
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-29T17:29:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c1s1jF2smfauU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <V7GdnePvfu-xCMbbnZ2dnUVZ_ualnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:V7GdnePvfu-xCMbbnZ2dnUVZ_ualnZ2d@comcast.com...
> Pete Dashwood wrote:
>> (I spent most of this morning furthering my education via a Web Cast on 
…[4 more quoted lines elided]…
> well.

But Dan, I want to have a .skin file and name it "fore"...:-)
>
> On a completely off-topic, unrelated topic - I just made a change to a 
…[3 more quoted lines elided]…
> from my personal blog's home page under "Weekly Devotions".

Well, could you do the decent thing and post a link then, please... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 12)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-05-29T06:29:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BeOdne0jUO0ngcHbnZ2dnUVZ_silnZ2d@comcast.com>`
- **In-Reply-To:** `<5c1s1jF2smfauU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <V7GdnePvfu-xCMbbnZ2dnUVZ_ualnZ2d@comcast.com> <5c1s1jF2smfauU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:V7GdnePvfu-xCMbbnZ2dnUVZ_ualnZ2d@comcast.com...
…[7 more quoted lines elided]…
> But Dan, I want to have a .skin file and name it "fore"...:-)

You might want to be careful - I hear those files have a habit of being 
cut-off halfway...

>> On a completely off-topic, unrelated topic - I just made a change to a 
>> theme (WordPress, not dotNet) using CSS and a custom image.  It's on my 
…[4 more quoted lines elided]…
> Well, could you do the decent thing and post a link then, please... :-)

OK - I thought you had my other one already....

http://www.djs-consulting.com/personal - my personal blog
http://www.djs-consulting.com/devotions - the "weekly devotions" with 
the cool ribbon bookmark.

Here's the CSS that makes that work...

.bible {
	margin: 15px 30px 0 10px;
	padding: 0 10px 30px 10px;
	border: 0;
	border-top: solid 1px black;
	background: white url(images/ribbon.png) no-repeat bottom left;
}

(the "border: 0;" is needed to clear the borders that are already 
assigned to the <blockquote> tag)
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 10)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-05-29T12:28:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<465C1C50.6F0F.0085.0@efirstbank.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net>`

```
>>> On 5/28/2007 at 8:36 PM, in message
<5c1hsnF2uuqhfU1@mid.individual.net>,
Pete Dashwood<dashwood@removethis.enternet.co.nz> wrote:

> On the web service from Java...
>  I see the real problem as being able to access COM from Java (Once you 
…[22 more quoted lines elided]…
> strikes...but that might just be me.)
 
I've only been browsing this thread, so maybe I'm not understanding, but why
do you feel the need to use COM from Java to be able to do SOAP stuff? 
There is Java support out there for SOAP.  Specifically, the
org.apache.soap.* and org.apache.soap.rpc.* packages.  (I'm sure there are
others.)

My only experience with this is utilizing a simple demo to access a
mainframe SOAP service from my PC, but it works.

Frank
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have timeto write a proper article on it)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-30T13:46:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c43beF2tm0i9U1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <465C1C50.6F0F.0085.0@efirstbank.com>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:465C1C50.6F0F.0085.0@efirstbank.com...
>>>> On 5/28/2007 at 8:36 PM, in message
> <5c1hsnF2uuqhfU1@mid.individual.net>,
…[30 more quoted lines elided]…
> do you feel the need to use COM from Java to be able to do SOAP stuff?

That isn't exactly what I feel... :-) I feel the need to be able to use COM 
from Java so that the richness of the several thousand COM servers already 
on my machine can be unlocked and used by Java. The SOAP Toolkit is just ONE 
such COM server.

> There is Java support out there for SOAP.  Specifically, the
> org.apache.soap.* and org.apache.soap.rpc.* packages.  (I'm sure there are
> others.)
>
Yes, you COULD do it all with SOAP, yourself (after all, it's just XML...) 
but it is MUCH easier if you invoke the methods of the SOAP COM object, and 
it takes a lot less code). There are no worries with establishing socket 
connections, checking transfers, detecting errors, etc.  it is all provided 
by a COM server. Why re-invent the wheel? In a non Windows environment where 
you don't have the SOAP toolkit available, you don't have much option, other 
than to do it yourself. This is partly why SOAP is obsolete and DotNET 
services are replacing it; they run across most platforms.

> My only experience with this is utilizing a simple demo to access a
> mainframe SOAP service from my PC, but it works.

Sure. The nearest analogy I can think of quickly is: Why write Assembler 
when you can write COBOL?

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have timeto write a proper article on it)

_(reply depth: 12)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-05-30T11:40:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<465D62A6.6F0F.0085.0@efirstbank.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <465C1C50.6F0F.0085.0@efirstbank.com> <5c43beF2tm0i9U1@mid.individual.net>`

```
>>> On 5/29/2007 at 7:46 PM, in message
<5c43beF2tm0i9U1@mid.individual.net>,
Pete Dashwood<dashwood@removethis.enternet.co.nz> wrote:

> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
> news:465C1C50.6F0F.0085.0@efirstbank.com...
…[22 more quoted lines elided]…
>> I've only been browsing this thread, so maybe I'm not understanding, but

>> why
>> do you feel the need to use COM from Java to be able to do SOAP stuff?
…[34 more quoted lines elided]…
> when you can write COBOL?

OK.  I guess I'm just not sure what you are doing.  Here is the demo client
program for the Apache SOAP service.  Is calling the SOAP COM object from
Java simpler than this?

package samples.stockquote;

import java.io.*;
import java.net.*;
import java.util.*;
import org.apache.soap.*;
import org.apache.soap.rpc.*;

/**
 * See README for info.
 *
 * @author Sanjiva Weerawarana (sanjiva@watson.ibm.com)
 */
public class GetQuote {
  public static void main (String[] args) throws Exception {
    if (args.length != 2
        && (args.length != 3 || !args[0].startsWith ("-"))) {
      System.err.println ("Usage: java " + GetQuote.class.getName () +
                          " [-encodingStyleURI] SOAP-router-URL symbol");
      System.exit (1);
    }

    // Process the arguments.
    int offset = 3 - args.length;
    String encodingStyleURI = args.length == 3
                              ? args[0].substring(1)
                              : Constants.NS_URI_SOAP_ENC;
    URL url = new URL (args[1 - offset]);
    String symbol = args[2 - offset];

    // Build the call.
    Call call = new Call ();
    call.setTargetObjectURI ("urn:xmltoday-delayed-quotes");
    call.setMethodName ("getQuote");
    call.setEncodingStyleURI(encodingStyleURI);
    Vector params = new Vector ();
    params.addElement (new Parameter("symbol", String.class, symbol,
null));
    call.setParams (params);

    // make the call: note that the action URI is empty because the 
    // XML-SOAP rpc router does not need this. This may change in the
    // future.
    Response resp = call.invoke (/* router URL */ url, /* actionURI */ ""
);

    // Check the response.
    if (resp.generatedFault ()) {
      Fault fault = resp.getFault ();

      System.err.println("Generated fault: " + fault);
    } else {
      Parameter result = resp.getReturnValue ();
      System.out.println (result.getValue ());
    }
  }
}

Of course if you want to invoke other COM services than I certainly can see
the usefulness of that.

Frank
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't havetimeto write a proper article on it)

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-02T01:24:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cal0iF2vmhniU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <465C1C50.6F0F.0085.0@efirstbank.com> <5c43beF2tm0i9U1@mid.individual.net> <465D62A6.6F0F.0085.0@efirstbank.com>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:465D62A6.6F0F.0085.0@efirstbank.com...
>>>> On 5/29/2007 at 7:46 PM, in message
> <5c43beF2tm0i9U1@mid.individual.net>,
…[70 more quoted lines elided]…
>

Sorry I didn't get to answer this sooner, Frank.

The answer is "I don't know" and can't know until I see what it takes to do 
it using COM.

(That probably won't be for a little while yet; I am trying to get the Batch 
program that accesses the service, running as a demo, and it is a lot of 
work. It involves accessing resources that are part of the C# Assembly 
itself (reflection) and I haven't done this before, so I'm learning as I go 
:-))

Thanks for posting this code. As soon as I can, I'll do the Java COM 
solution.

Cheers,

Pete.
<Java code snipped>
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 10)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-31T17:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cJD7i.15340$Ut6.7789@newsread1.news.pas.earthlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5c1hsnF2uuqhfU1@mid.individual.net...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[78 more quoted lines elided]…
>

I have not spent a lot of time searching but I saw JACOB: JAva COm Bridge 
and something from IBM at www.alphaworks.ibm.com/tech/dtjcb

IIRC with Axis I just need to:

1.  add a path to the .jar files to my CLASSPATH
2. run wsdl2java program against the wsdl
3. write short java program to invoke the web services using the java 
generated in step 2

Well that is just from a quick glance at the documantation several days ago.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-01T11:19:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c93g5F2vvsnpU1@mid.individual.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net> <5c1hsnF2uuqhfU1@mid.individual.net> <cJD7i.15340$Ut6.7789@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:cJD7i.15340$Ut6.7789@newsread1.news.pas.earthlink.net...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[95 more quoted lines elided]…
>
Yes, the trick is to have something that generates proxy classes for COM 
access. Bridge2Java does this. It isn't just about web services, as noted 
elsewhere. Rather than generating code from the wsdl, you can generate code 
from a COM .olb or typelib. This gives you the interface to that COM 
component, and that  (using the SOAP Toolkit COM component 
(MSSOAP.SoapClient30) analyses the wsdl and does the web service call, 
exactly as the COBOL posted by Jimmy and myself.

There are a number of approaches to accessing a web service from Java 
(anything that works is pretty much all right... :-)) but using a standard 
component is my preferred one. I believe the code for this approach will be 
considerably less than with the direct approach, because there is more under 
the covers of the COM component. That's the whole point of components; they 
provide encapsulated functionality so you don't have to keep writing it.

I'm really deep into the AVS website, demos, and downloads currently so I 
can't really look at this right now, but I hope to later (certainly before 
the Singularity... :-))

Pete.

Pete.
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-29T09:18:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3gr4q$cjt$1@reader2.panix.com>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`

```
In article <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>,
Charles Hottel <chottel@earthlink.net> wrote:

[snip]

>If  this is the only problem and if the 
>baby can develop long enough then he/she may have a chance. However 25% to 
>40% of the babies with this problem have other birth defects.

Odds like this are given so that you may exult in beating them.  Best 
wishes, Mr Hottel, to all involved for a rapid convalesences and full 
recoveries.

DD
```

###### ↳ ↳ ↳ Re: Web Services and COBOL (Fairly long post, but I don't have time to write a proper article on it)

_(reply depth: 9)_

- **From:** "Paul Raulerson" <Paul.Raulerson@Gmail.com>
- **Date:** 2007-05-29T20:01:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<465cccda$0$4048$bbae4d71@news.suddenlink.net>`
- **References:** `<5bddsqF2sd0m9U1@mid.individual.net> <epp4i.13336$j63.3581@newsread2.news.pas.earthlink.net> <5beo1dF2s776oU1@mid.individual.net> <6iM4i.12447$Ut6.3969@newsread1.news.pas.earthlink.net> <5bhj8jF2rrq02U1@mid.individual.net> <%g45i.18421$3P3.8338@newsread3.news.pas.earthlink.net> <GPp5i.13254$Ut6.2582@newsread1.news.pas.earthlink.net> <5bnqv4F2rp0c0U1@mid.individual.net> <6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net>`

```
The people here have been here (a lot of us) for a decade or more. I cannot 
think of a better definition of a friend than someone you you can talk with. 
My daughter has a severe oxygen deprevation while she was being born, and as 
a result has a moderately severe retardation. She also suffers from 
epileptic seizures, which terrify all of us. She woke up the other night 
afraid she was going to die.

She has slept in our bed for the past week, and I have been ejoying the 
hospitality of the couch. (*sigh*) She is worth it, and even if your child 
has birthh defects, it won't really matter to you. Trust me on that.

Our prayers and best wishes are with you.

-Paul & Karen

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:6dL6i.16043$j63.2521@newsread2.news.pas.earthlink.net...
> Top Post not more below
>
…[337 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
