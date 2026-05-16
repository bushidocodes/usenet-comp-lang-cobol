[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating a Web Service with COBOL...

_6 messages · 3 participants · 2007-06 → 2007-07_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Creating a Web Service with COBOL...

- **From:** softWare design <sabraham@baxglobal.com>
- **Date:** 2007-06-26T13:10:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com>`

```
Hello,

Just read the following articles and I thought they were interesting,
however, I am wondering if I can create a Web Service by simply
using the Windows APIs (SDK development kit) ? I know that the
SOAP protocol uses the HTTP/HTTPS over the internet to support
interoperable machine to machine interaction.  So, is it possible to
use the listed below functions to send the needed XML messages
between clients and servers ?

Thanks for any comments....

	HttpOpenRequest()

	HttpSendRequestEx()

http://www.cobolportal.com/files/egilityedge.pdf

http://www.adtmag.com/article.aspx?id=7730&amp;page=

http://www.adtmag.com/article.aspx?id=9472&amp;page=
```

#### ↳ Re: Creating a Web Service with COBOL...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-27T13:30:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5edssuF37oamtU1@mid.individual.net>`
- **References:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com>`

```

"softWare design" <sabraham@baxglobal.com> wrote in message 
news:1182888614.062525.103150@q75g2000hsh.googlegroups.com...
> Hello,
>
…[6 more quoted lines elided]…
> between clients and servers ?

Your links didn't work for me, but I have a fair idea what you're talking 
about...

>
> Thanks for any comments....
…[10 more quoted lines elided]…
>
Yes, it is. But there are much easier ways of accessing Web Services and 
building them.

Have a look at the thread: "Web Services and COBOL (fairly long post..." , 
starting with the original post dated 27th May, 2007. It explains the SOAP 
Toolkit scenario and has sample code for both Fujitsu NetCOBOL and MF 
NetExpress. For BUILDING Web Services you can use the SOAP Toolkit to 
generate WSDL.

I have connected to SOAP services using the Toolkit, and the "manual" method 
(painstakingly building all the XML and WSDL myself, some years ago to 
access a banking service on a mainframe, remotely over the Internet from a 
PC in a different country.)

The Toolkit is better.

You should also bear in mind that the SOAP protocol is already obsolete and 
will no longer be supported by MS after next year. It is being replaced by 
DotNet Web Services (which provide richer facilities and error checking than 
SOAP does...)


Pete.
```

##### ↳ ↳ Re: Creating a Web Service with COBOL...

- **From:** softWare design <sabraham@baxglobal.com>
- **Date:** 2007-06-26T19:13:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182910437.457329.69930@c77g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5edssuF37oamtU1@mid.individual.net>`
- **References:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com> <5edssuF37oamtU1@mid.individual.net>`

```
On Jun 26, 6:30 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "softWare design" <sabra...@baxglobal.com> wrote in message
>
> news:1182888614.062525.103150@q75g2000hsh.googlegroups.com...
>

> Your links didn't work for me, but I have a fair idea what you're talking
> about...

> Pete.


Pete, thanks for your comment. See if you can access the links now.

http://216.239.51.104/search?q=cache:JFZTMPGZ5W0J:www.cobolportal.com/files/egilityedge.pdf+cobol+web+service&hl=en&ct=clnk&cd=10&gl=us

http://216.239.51.104/search?q=cache:kyloOiakJUMJ:www.adtmag.com/article.asp%3Fid%3D9472+cobol+web+service&hl=en&ct=clnk&cd=1&gl=us

http://216.239.51.104/search?q=cache:tR7JwXw62jQJ:www.adtmag.com/article.asp%3Fid%3D7730+cobol+web+service&hl=en&ct=clnk&cd=2&gl=us
```

###### ↳ ↳ ↳ Re: Creating a Web Service with COBOL...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-27T23:37:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ef0fpF379cm8U1@mid.individual.net>`
- **References:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com> <5edssuF37oamtU1@mid.individual.net> <1182910437.457329.69930@c77g2000hse.googlegroups.com>`

```

"softWare design" <sabraham@baxglobal.com> wrote in message 
news:1182910437.457329.69930@c77g2000hse.googlegroups.com...
> On Jun 26, 6:30 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
>
OK, I read this. Normally, I'm not too keen to waste time reading marketing 
stuff but most of this was sound, and it was generally sensible. I went off 
it when they quoted the usual Gartner bullshit from 7 years ago at the 
start, but I persevered and was generally pleased to see they are advocating 
component based solutions and recognise the importance of Web Services. I 
certainly don't disagree that leveraging existing COBOL into these 
environments is a useful thing to do and you can't blame MicroFocus for 
seeking to extend the useful life of COBOL in this way.

I think they are still going to hit the paradigm shift but at least existing 
stuff will be salvageable. This is of critical importance for many 
companies.

> http://216.239.51.104/search?q=cache:kyloOiakJUMJ:www.adtmag.com/article.asp%3Fid%3D9472+cobol+web+service&hl=en&ct=clnk&cd=1&gl=us

This one was a bit of a hodge-podge. Some pretty hyperbolic marketing claims 
("we are the ONLY people..." etc. when, in fact, if you're prepared to do it 
manually, ANYONE (with access to a network and (easily acquired) knowledge 
of XML/WSDL can produce and consume web services.)  It was lengthy, but 
there were some interesting nuggets in amongst the dross. The main value I 
see is in raising awareness in mainframe world that they better get with the 
action or they will be left behind. (However, "getting with the action" is 
not as difficult as some people who are trying to market products, would 
have you believe...)
>
> http://216.239.51.104/search?q=cache:tR7JwXw62jQJ:www.adtmag.com/article.asp%3Fid%3D7730+cobol+web+service&hl=en&ct=clnk&cd=2&gl=us
>
>
Not a lot of substance here and mainly a vehicle for MicroFocus to reprise 
the catchphrase of being the last chance for COBOL. (Nothing against MF; 
they very possibly are...) The company's commitment to the future of COBOL 
was restated (at least they see a future and are prepared to state it; more 
than the COBOL Guardians at J4 were able to do...) and they are doing what 
they can to see that COBOL gets to play in the brave new world of SOA. I 
hope it goes well for them. I believe their efforts could well extend the 
useful life of COBOL, but I'm still not prepared to extend the 2015 date...

The problems they will run into are:

1. Unless they can actually persuade the current user base to move to OO 
(and so far, that hasn't worked at all), their customer base will be eroded 
as more and more shops realise that maintaining computer programs line by 
line is just far too expensive and opt out.  (As someone pointed out in one 
of the above articles, it doesn't matter whether you are using Java, C++ or 
COBOL, as long as you are tied to source code line by line, you're screwed. 
The only reason more haven't already done so is because they are locked into 
their current COBOL investment. (Or think they are... actually, they are 
not, but as long as they continue developing with the status quo, there will 
be no progress. If there is no real progress, eventually the cost of 
in-house development will just get too expensive and the whole development 
department will simply collapse.) At this point companies outsource IT, or 
outsource a package solution, or simply buy the service.

2. Although they can provide bridges to CICS and IMS that will allow web 
services to be accessed from the mainframe, unless there is a radical 
rethink in the way things get done (development methodology, if you 
like...the Waterfall is still "state of the art" in many COBOL shops), no 
actual benefit will accrue. There's no point in having access to components 
if you don't understand how to build component based systems, and reuse 
existing objects. The whole concept of network infrastructure and object 
reuse is beyond the ken of most existing COBOL shops. Basically, they don't 
see anything broken, so there's nothing to fix.

3. As more sites DO start to cotton on to the real advantages of SOA they 
will realise that, even if COBOL CAN be used for OO it still isn't as facile 
as other languages that were designed to do so from the start.

(I loved OO COBOL and used it for nearly 10 years.Built loads of reusable 
components and tools with it, and thought it was great. But the simple fact 
is that in an OO environment, C# is simply light years ahead of it (so is 
Java). I wouldn't go back to OO COBOL development now, and  I use COBOL only 
for existing stuff until such time as I can get around to rewriting it.) The 
point is that as knowledge grows, and the scales fall from people's eyes, 
COBOL is revealed as a less attractive option, in the 21st century 
environment we are faced with.

Given all of 3 of the above (which can be summed up as the "paradigm shift") 
I believe MicroFocus are on a hiding to nothing long term.

Hope I'm wrong, but current trends seem to be bearing out what I say.

The three articles are well worth reading, but remember there is sludge in 
with the gold dust... :-)

Pete.
```

##### ↳ ↳ SOAP may not be obsolete was Re: Creating a Web Service with COBOL...

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-07-09T21:53:48-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u0m593d5mr5ns220mkakbt894uemc9k3u7@4ax.com>`
- **References:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com> <5edssuF37oamtU1@mid.individual.net>`

```
On Wed, 27 Jun 2007 13:30:04 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>"softWare design" <sabraham@baxglobal.com> wrote in message 
…[46 more quoted lines elided]…
>SOAP does...)

Of course .NET will work well on all of the Unix / Linux systems as
well as mainframes from any vendor left.  Maybe SOAP is out for
Microsoft but I suspect other vendors may view things differently as
might the Linux enthusiasts.
>
>
>Pete.
>
>
```

###### ↳ ↳ ↳ Re: SOAP may not be obsolete was Re: Creating a Web Service with COBOL...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-10T22:24:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fh52qF3cimdeU1@mid.individual.net>`
- **References:** `<1182888614.062525.103150@q75g2000hsh.googlegroups.com> <5edssuF37oamtU1@mid.individual.net> <u0m593d5mr5ns220mkakbt894uemc9k3u7@4ax.com>`

```

"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:u0m593d5mr5ns220mkakbt894uemc9k3u7@4ax.com...
> On Wed, 27 Jun 2007 13:30:04 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[55 more quoted lines elided]…
> well as mainframes from any vendor left.

Not sure if you are being sarcastic here. If you are, you should realise 
that the .NET equivalent for Unix/Linux systems is Mono and it is already 
enabling these OSes to use equivalent functionality to the .NET framework. I 
have already had some sample C# code which I developed under Windows and 
.NET, run on a Linux system under Mono without change. The code TRULY is 
transportable.

Perhaps this link may help... http://en.wikipedia.org/wiki/Mono_(software)

And yes, there is also a Mono implementation for S390.

>Maybe SOAP is out for
> Microsoft but I suspect other vendors may view things differently as
> might the Linux enthusiasts.
>>

Having used SOAP almost since its early inception, I am a big fan of this 
protocol and sorry to see it go. However, the rights to it are owned jointly 
by MicroSoft and IBM. W3C has been pressuring for them to make it open but 
so far they haven't. They maintain RAND licensing which means they CAN 
charge for it if they so decide. Should they do so, and given that Mono is 
already open and .NET is unlikely to become closed if it is to stay 
competitive, it isn't hard to see which way the wind is blowing. 
(Furthermore, .NET/Mono provides richer support for web services anyway...)

MicroSoft have openly stated they will not be supporting SOAP after 2008. 
(They wanted to drop it in 2006 and it is only the fact that many of their 
own products have it embedded  in them, that has caused them to extend its 
lifespan.) IBM are ominously silent, but probably have no problem with going 
Mono.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
