[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Mainframe JCL Conversion Tools

_54 messages · 26 participants · 2004-01 → 2005-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM Mainframe JCL Conversion Tools

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2004-01-29T16:09:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>`

```
Does anyone know of tools which will convert the horrible JCL construct 
COND= to IF ... THEN ... ELSE ... ENDIF?

We can't forbid the use of COND= in our JCL Standards Checker (which is 
written in COBOL, so that I'm not 100% off topic), because there is so 
much use of COND= in existing jobs.

If I could get all existing uses converted, then we could prohibit the 
keyword entirely.
Thanks,
Colin
```

#### ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** "Ron" <NoSpam@NoMoSpam.ORG>
- **Date:** 2004-01-30T21:15:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QcWdnRrW3Y5-gIbdRVn_vw@giganews.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>`

```
Just a question here. I love the ability to use IF
statements in JCL and do use them frequently. However,
I also routinely put COND=(0,NE) on just about every
step to prevent it from executing if a prior step
ended with a condition code greater than zero. I've
seen this in a lot of shops. It seems do me having
to enclose each step with an IF ENDIF sequence to
accomplish the same thing would be more confusing and
complicated than the COND parameter. Would you really
want to prevent COND from being used in that manner?
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-01-31T13:54:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3sOSb.6506$BA2.798@newssvr26.news.prodigy.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <QcWdnRrW3Y5-gIbdRVn_vw@giganews.com>`

```
"Ron" <NoSpam@NoMoSpam.ORG> wrote in message
news:QcWdnRrW3Y5-gIbdRVn_vw@giganews.com...
> Just a question here. I love the ability to use IF
> statements in JCL and do use them frequently. However,
…[7 more quoted lines elided]…
> want to prevent COND from being used in that manner?

Not sure ... but it seems to me mixing IF..ELSE with COND= in a single job
might make maintenance a real 'challenge' for the next poor schlub.

MCM
```

#### ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2004-02-03T10:43:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<401fcfaa$7@giga.realtime.net>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>`

```

"Volker Bandke" <vbandke@bsp-gmbh.com> wrote in message
news:2jgp10t0c7jbbrhl32ft6n9ioebfie3jm6@4ax.com...
> On Thu, 29 Jan 2004 16:09:55 -0800, Colin Campbell
> <cmcampb@adelphia.net_remove_this> wrote:
…[6 more quoted lines elided]…
> I am not aware of a mechanical/programmatical way of doing this

Not available off the shelf, but we build program transformation tools
for arbitrary languages.  We have a draft version of JCL available for
our tools.  This looks like a pretty easy transform to code.

See  http://www.semanticdesigns.com/Products/DMS/DMSToolkit.html.
```

#### ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-02-06T01:01:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0402060004.18dbea18@posting.google.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>`

```
Are you porting off the mainframe or just cleaning up and remaining on
the mainframe?

Colin Campbell <cmcampb@adelphia.net_remove_this> wrote in message news:<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>...
> Does anyone know of tools which will convert the horrible JCL construct 
> COND= to IF ... THEN ... ELSE ... ENDIF?
…[8 more quoted lines elided]…
> Colin
```

#### ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2004-08-20T14:46:55-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<zKWdnexlvbKyyLvcRVn-uw@comcast.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>`

```
In article <ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>, 
cmcampb@adelphia.net_remove_this wrote:

>Does anyone know of tools which will convert the horrible JCL construct 
>COND= to IF ... THEN ... ELSE ... ENDIF?
…[6 more quoted lines elided]…
>keyword entirely.

One can use IF ... THEN statements in JCL?
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-20T21:02:48+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000720.00884b75@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com>`

```
Ubiquitous,

> One can use IF ... THEN statements in JCL?

Yep. You wouldn't want to, but JCl is such a hideous construct, that 
there's no way it can be improved.

My advice is to get used to it. There are software packages which will 
generate JCL from sensible syntax, but IBM haven't provided any.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-20T20:28:04+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<cg5msk$ilt$1@peabody.colorado.edu>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org>`

```

On 20-Aug-2004, Doug Scott <dwscott@ieee.org> wrote:

> > One can use IF ... THEN statements in JCL?
>
> Yep. You wouldn't want to, but JCl is such a hideous construct, that
> there's no way it can be improved.

Why wouldn't we want to use IF ... THEN statements in JCL?   They're clear,
easy, and useful.

What does JCI stand for?  I infer by the "hideous construct" phrase that it has
something to do with the old COND logic.
```

###### ↳ ↳ ↳ Demo: Windows scripting

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-21T01:01:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu>`

```
On Fri, 20 Aug 2004 20:28:04 GMT, "Howard Brazee" <howard@brazee.net>
wrote:

>On 20-Aug-2004, Doug Scott <dwscott@ieee.org> wrote:
>
…[6 more quoted lines elided]…
>easy, and useful.

>What does JCI stand for? 

A lower case L in some fonts. When I told Agent to switch to Courier,
it showed up as an L. 

>  I infer by the "hideous construct" phrase that it has
>something to do with the old COND logic.

As a scripting language, JCL is horrid. Assuming you're running W2K or
later, you need look no further than the computer before you for
excellent scripting languages. It's amazing how many people think DOS
.bat file is the only MS script language, even 'professional'
administrators.  The full spec is at the URL at the end of this
message. Before you read it, I'll give two very simple demos. Copy and
paste this into a text file named demo1.vbs

Set wbemObjectSet = _
  GetObject("winmgmts:\\.").InstancesOf("Win32_Service")

For Each wbemObject In wbemObjectSet
    If wbemObject.State = "Running" Then
       WScript.Echo " Service: " & wbemObject.DisplayName
    End If
Next

Now run it by typing "cscript demo1.vbs". The output will show all
services running on your PC. The list might convince you you're not
running a 'toy computer'.

Next you might wonder what other information about a service, in
addition to DisplayName, is available. Look in the documentation? No,
look in the class definition. This is called 'introspection'. It's
available for ALL objects in object-land. Copy and paste this into a
text file named demo2.vbs and run it with "cscript demo2.vbs".

Set objClass = GetObject("winmgmts:\\.\root\cimv2:Win32_Service")

For Each objClassProperty In objClass.Properties_
    WScript.Echo objClassProperty.Name
Next

The output should look like this:

AcceptPause
AcceptStop
Caption
CheckPoint
CreationClassName
Description
DesktopInteract
DisplayName
ErrorControl
ExitCode
InstallDate
Name
PathName
ProcessId
ServiceSpecificExitCode
ServiceType
Started
StartMode
StartName
State
Status
SystemCreationClassName
SystemName
TagId
WaitHint

If you're on a MS network, replacing the dot with the name of another
machine will give the same information about that machine. You don't
have to log onto its command line. You can just as easily list methods
available against services. This is now software should work .. IMO.

VBScript offers variables, loops, case statement, if .. then .. else,
local functions, call, editing pictures, math functions, string
functions, access to the OS API and the world of OO. JCL doesn't offer
any of that .. except IF around whole steps in batch jobs. 

http://www.microsoft.com/downloads/details.aspx?FamilyId=01592C48-207D-4BE1-8A76-1C4099D7BBB9&displaylang=en
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 5)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-08-21T10:01:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CAIVc.38529$Tr.1951889@news20.bellglobal.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com...
> On Fri, 20 Aug 2004 20:28:04 GMT, "Howard Brazee" <howard@brazee.net>
> wrote:
…[8 more quoted lines elided]…
> >Why wouldn't we want to use IF ... THEN statements in JCL?   They're
clear,
> >easy, and useful.
>
…[12 more quoted lines elided]…
> administrators.
<SNIP>
> VBScript offers variables, loops, case statement, if .. then .. else,
> local functions, call, editing pictures, math functions, string
> functions, access to the OS API and the world of OO. JCL doesn't offer
> any of that .. except IF around whole steps in batch jobs.

Yes, but JCL isn't the only scripting language on z/OS.   Complex scripts
can easily be handled through TSO Rexx.
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-21T22:57:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com> <CAIVc.38529$Tr.1951889@news20.bellglobal.com>`

```
On Sat, 21 Aug 2004 10:01:08 -0400, "Don Leahy"
<leahydon@nospamplease.netscape.net> wrote:

>Yes, but JCL isn't the only scripting language on z/OS.   Complex scripts
>can easily be handled through TSO Rexx.

In the case of batch, Rexx writes the JCL and CA-7 executes it.
Running production programs running under Rexx is not in the culture.

This source says there are others, one being Python.
http://encyclopedia.thefreedictionary.com/Scripting%20language
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 7)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-08-21T22:49:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IQTVc.42497$Tr.2150355@news20.bellglobal.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com> <CAIVc.38529$Tr.1951889@news20.bellglobal.com> <q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com...
> On Sat, 21 Aug 2004 10:01:08 -0400, "Don Leahy"
> <leahydon@nospamplease.netscape.net> wrote:
…[5 more quoted lines elided]…
> Running production programs running under Rexx is not in the culture.

And your point is?
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-22T07:32:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71igi0hig6b2rjaf8tccmsbticiu23bue8@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com> <CAIVc.38529$Tr.1951889@news20.bellglobal.com> <q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com> <IQTVc.42497$Tr.2150355@news20.bellglobal.com>`

```
On Sat, 21 Aug 2004 22:49:15 -0400, "Don Leahy"
<leahydon@nospamplease.netscape.net> wrote:

>
>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
…[10 more quoted lines elided]…
>And your point is?

My point is what's permissible is more a function of culture than of
language.  The standard in the mainframe world is the Golden Age of
the '70s. They act like it might return any day. Pleasant dreams.
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 9)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-08-22T09:22:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F61Wc.1866$DG.35436@news20.bellglobal.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com> <CAIVc.38529$Tr.1951889@news20.bellglobal.com> <q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com> <IQTVc.42497$Tr.2150355@news20.bellglobal.com> <71igi0hig6b2rjaf8tccmsbticiu23bue8@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:71igi0hig6b2rjaf8tccmsbticiu23bue8@4ax.com...
> On Sat, 21 Aug 2004 22:49:15 -0400, "Don Leahy"
> <leahydon@nospamplease.netscape.net> wrote:
…[7 more quoted lines elided]…
> >> >Yes, but JCL isn't the only scripting language on z/OS.   Complex
scripts
> >> >can easily be handled through TSO Rexx.
> >>
…[8 more quoted lines elided]…
>
Nonsense.
```

###### ↳ ↳ ↳ Re: Windows scripting

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-23T09:04:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B8EDFD.09040423082004@knology.usenetserver.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <cg5msk$ilt$1@peabody.colorado.edu> <nu6di0t2tl9humgnuketrc4pode6mrs12q@4ax.com> <CAIVc.38529$Tr.1951889@news20.bellglobal.com> <q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com>`

```
In article <q4jfi05tbjpbga26igb6svo1993jsnrfqf@4ax.com>,
 Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

> On Sat, 21 Aug 2004 10:01:08 -0400, "Don Leahy"
> <leahydon@nospamplease.netscape.net> wrote:
…[5 more quoted lines elided]…
> Running production programs running under Rexx is not in the culture.

Rexx is useful -- but more as a replacement for CLIST that as a 
replacement for JCL.

There are some nice things about JCL.  The declaritiveness of it allows 
for repeatable, predictable, production runs without the iffy-ness that 
can show up from using a full-featured language for your scripts.  

(For example, a commonly used Rexx function might be changed to have 
subtle side-effects in production jobs -- JCL provides exactly what is 
request or a error.)

Finally, you can't run Rexx without JCL*, so your are still somewhat 
dependant upon some of its problems and oddities.





* Yes, yes, you could run it under CICS, but the you have the oddities 
of CICS and JCL to deal with.  Oh, you could run it under USS, but the 
you have the oddities of USS and JCL to deal with.  Well, you could run 
it from a master console -- but that would be very strange...
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2004-08-20T18:23:28-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<FfydndXmKcRtGrvcRVn-qg@comcast.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org>`

```
In article <VA.00000720.00884b75@ieee.org>, dwscott@ieee.org wrote:
>Ubiquitous,

>> One can use IF ... THEN statements in JCL?
>
>Yep. You wouldn't want to, but JCl is such a hideous construct, that 
>there's no way it can be improved.

I've used COND in mine from the begining but they're such a bear.
I was hoping there was an easier alternative.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-08-22T01:56:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7rggi0do28hqurmaj9g7dedeps87kog2hu@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org>`

```
Really, IMO, I think COND is a complete nightmare.  Probably more
relatable to those with assembly experience, though.  But a
counterintuitive nightmare for those of us who don't.

On Fri, 20 Aug 2004 21:02:48 +0100, Doug Scott <dwscott@ieee.org>
wrote:

>Ubiquitous,
>
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2004-08-22T18:24:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qUPLvnBGbNKBFwa$@ld50macca.demon.co.uk>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <7rggi0do28hqurmaj9g7dedeps87kog2hu@4ax.com>`

```
As a one-time Assembler 370 programmer, I still find the use of COND a 
nightmare, especially where people cond-code every step when they don't 
need to do so.

In message <7rggi0do28hqurmaj9g7dedeps87kog2hu@4ax.com>, Glenn Someone 
<dontspamme@whydoyouneedmyaddressspammers.com> writes
>Really, IMO, I think COND is a complete nightmare.  Probably more
>relatable to those with assembly experience, though.  But a
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 4)_

- **From:** Paul Knudsen <HughG@dodgeit.com>
- **Date:** 2004-08-24T02:18:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k79li0higvg2kdhbgqoa9ng2b5k4027dqi@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <VA.00000720.00884b75@ieee.org> <7rggi0do28hqurmaj9g7dedeps87kog2hu@4ax.com>`

```
On Sun, 22 Aug 2004 01:56:23 -0500, Glenn Someone
<dontspamme@whydoyouneedmyaddressspammers.com> wrote:

>Really, IMO, I think COND is a complete nightmare.  Probably more
>relatable to those with assembly experience, though.  But a
>counterintuitive nightmare for those of us who don't.

What's Assembler got to do with it?  I don't do assembler, but I
managed to master COND back when with a bit of careful study.  If you
can't, hire someone who can.
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-20T20:05:59+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<cg5lj6$cl3$1@peabody.colorado.edu>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com>`

```

On 20-Aug-2004, weberm@polaris.net (Ubiquitous) wrote:

> >Does anyone know of tools which will convert the horrible JCL construct
> >COND= to IF ... THEN ... ELSE ... ENDIF?
…[8 more quoted lines elided]…
> One can use IF ... THEN statements in JCL?

You might be surprised about how many people use JCL without knowing this.  
Give them the following link:

http://www.objectz.com/cobolreport/archives/TCR_jcl.htm
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-20T20:44:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vmci05liulctef7iujlnp6mksuikbvl15@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com>`

```
On Fri, 20 Aug 2004 14:46:55 -0500, weberm@polaris.net (Ubiquitous)
wrote:

>In article <ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>, 
>cmcampb@adelphia.net_remove_this wrote:
…[11 more quoted lines elided]…
>One can use IF ... THEN statements in JCL?

One can, but it's so crippled that it's unusable. The construct under
IF must be a complete STEP. One cannot say:

//  IF (RC LT 9) THEN
//   MYDD DD DSN='A'
// ELSE
//  MYDD DD DSN='B' 
// ENDIF

COND has the same limitation, it goes on the EXEC statement, so
converting COND to IF should be trivial. It could be written as an
ISPF macro, then submitted to batch with * filename  to convert all
JCL in a PDS.
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-21T14:35:43-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com>`

```
In article <zKWdnexlvbKyyLvcRVn-uw@comcast.com>,
 weberm@polaris.net (Ubiquitous) wrote:

> In article <ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com>, 
> cmcampb@adelphia.net_remove_this wrote:
…[11 more quoted lines elided]…
> One can use IF ... THEN statements in JCL?

I can't think of a product -- but if you have an inhouse Cobol standards 
checker, why not make it into a preprocessor.  

The rules for converting a COND to an IF are simple as COND is only a 
single step.  Have your checker emit an IF/ENDIF around each step with a 
cond, and proper convert the COND condtion to an IF condtion.

It isn't perfect.  You will see two IFs with opposite conditons instead 
of an IF/ELSE/ENDIF.  But it doesn't totally suck either.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-21T22:08:20-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<E6UVc.28452$5s3.19593@fe40.usenetserver.com>`
- **In-Reply-To:** `<joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:
> In article <zKWdnexlvbKyyLvcRVn-uw@comcast.com>,
>  weberm@polaris.net (Ubiquitous) wrote:
…[27 more quoted lines elided]…
> of an IF/ELSE/ENDIF.  But it doesn't totally suck either.

I'll preface this by saying that I've never used JCL a nanosecond in my 
life - so this may not apply.  However, in the case you describe above, 
is it possible for the COND statement to modify the value it's checking 
if a true condition occurs?

This may not even be a factor, but I know there's a difference between 
this...

if myVar = "X"
     perform NextMyVar
else
     perform MyVarIsDone
end-if
.
NextMyVar.
     move "Y" to myVar.

...and this...

if myVar = "X"
     perform NextMyVar
end-if
if myVar not = "X"
     perform MyVarIsDone
end-if
.

In the first, MyVarIsDone is not performed - under the second, it is.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 4)_

- **From:** Lawrence H Greenwald <lgreenwa@cts.com>
- **Date:** 2004-08-22T09:16:45+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<lgreenwa-498FD1.02164422082004@chiapp18.algx.net>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com>`

```
In article <E6UVc.28452$5s3.19593@fe40.usenetserver.com>,
 LX-i <lxi0007@netscape.net> wrote:

> 
> I'll preface this by saying that I've never used JCL a nanosecond in my 
…[3 more quoted lines elided]…
> 

Having worked on IBM mainframes for over 20 years, I've seen COND and 
how bad it can be. Sorry, COND can only be used to check for a return 
code from a prior step or if a prior step has abended. The problem with 
COND is that it's bass-ackwards of what you would think would happen...

If you've never seen it, typical use (overly simplified to save space) 
is this...

//A EXEC PGM=AAA123
/*
//B EXEC PGM=XYZ456,COND=(12,GT,A)
/*

Now program AAA123 can set a return code (a value in register 15) just 
prior to exiting and step B will examine the value.

If A returns a return code of, say, 10...then the expression is "is 12 
greater than 10?", then the condition is evaluated as TRUE and (here's 
where it's bass-ackwards), step B is BYPASSED (program XYZ456 is NOT 
executed)!!!

If A returns a return code of, say, 14...then the condition is evaluated 
as FALSE and the step B (program XYZ456) is EXECUTED!! 

You think it's bad with one code, try it with multiple codes from 
multiple steps!!  Yech!!

There's also COND=ONLY, which means execute the step ONLY if a prior 
step ABENDED (divide by zero error, doing math on a field with invalid 
numeric data, ran out of space for an output file on disk, etc.)

There's also COND=EVEN, which means exeute the step EVEN if a prior step 
abended (usually steps after an abend are bypassed, unless the COND=ONLY 
or COND=EVEN is coded for a step or steps). 

MVS Version 4 (circa 1996 or so...don't quote me on this) added the 
IF...THEN...ELSE which makes life a lot easier.

--LG
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 5)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-22T17:42:18+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net>`

```
On Sun, 22 Aug 2004 09:16:45 GMT, Lawrence H Greenwald
<lgreenwa@cts.com> wrote:

>If you've never seen it, typical use (overly simplified to save space) 
>is this...
…[7 more quoted lines elided]…
>prior to exiting and step B will examine the value.

In three out of three mainframe shops where I worked recently, the
rule was one step per JCL. They used the scheduler to make decisions,
not JCL. When I tried to put two related steps in a single job, I was
told that's against the rules. 

When converting to Unix, which they hated, they insisted on knowing
how to make a job abend. The conversation went like this:

MF: How can we make the job abend?
me: Why do you want to stop the job? Just log the offending
transaction and keep running.
MF: Nobody looks at logs. We must get a human involved so the problem
will be noticed. Maybe we can divide by zero.
me: Ok, you can abend by saying CALL 'abort' RETURNING some-value.
MF: Where's it say that in the Cobol manual?
me: It doesn't. You're calling a C function.
MF: Huh? A C function? Can that be done? 

MF: Next question .. how do we read a dump?
me: Reading dumps is not in the Unix culture. Just log the offending
value and its key.
MF: No,  we've always read dumps. There might be other information we
didn't log. 
me: (Show them how to use coreadm so dumps don't overwrite each other.
Show them how to use anim to read a dump using source as a template.)
MF: This is great. We just point to a data name and it shows the
value.
me: Make sure you use the -g compiler option so it can relate
addresses to source. 

(Later notice some Standards Guy turned off -g for production
compilations.)
me: They won't be able to do production support without that option.
SG: We can't have people debugging programs in Production. They should
go to a test environment. 
me: Addresses won't match because you changed other compiler options.
SG: So copy the transaction file and recreate the problem.
me: The database isn't the same. Test environments don't have a full
production load or, if they do, it's not up to date.
SG: Let them figure it out. I'm not a programmer.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-22T22:00:48+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000723.02dcd129@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com>`

```
Robert,

> Let them figure it out. I'm not a programme

ROFL!

That whole sorry tale is a classic! And I'm sure it happens all over 
the world.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ IBM and "ABENDING" from COBOL (was: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-24T23:43:34+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com>`

```
The answer of how to "ABEND" from a COBOL program:

A) In any currently supported "mainframe" environment, (i.e. LE is available)
see CEE3ABD at:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3140/3.5.1

B) for pre-LE environments, see; ILBOABN0 at:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igya1101/3.15.1

None of this requires C functions (or even z/OS, MVS, whatever, service calls)
```

###### ↳ ↳ ↳ Re: IBM and "ABENDING" from COBOL (was: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-25T10:23:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net>`

```
On Tue, 24 Aug 2004 23:43:34 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>The answer of how to "ABEND" from a COBOL program:
>
…[7 more quoted lines elided]…
>None of this requires C functions (or even z/OS, MVS, whatever, service calls)

Next time I want to abend a Unix program I'll do a Remote Procedure
Call to a mainframe.
```

###### ↳ ↳ ↳ Re: IBM and "ABENDING" from COBOL (was: IBM Mainframe JCL Conversion Tools

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-25T16:04:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com>`

```
Tell me which compiler you are using on Unix - and I'll tell you which callable
service is available for that compiler.  Micro Focus (for example) provides
"emulations" of the CEE callable services with some (not all) of their
compilers.  IBM, of course, provides its own versions of many CEE callable
services with their AIX products.
```

###### ↳ ↳ ↳ Re: IBM and

_(reply depth: 9)_

- **From:** "kprasann" <ashprav@rediffmail.com>
- **Date:** 2005-01-07T02:44:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com> <BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net>`

```
Hello, I'm trying to abend a micro focus COBOL program in AIX. The COBOL
program was actually migrated from mainframes and has a CALL to ILBOABN0
IBM routine.
Thanks,
Krish.
```

###### ↳ ↳ ↳ Re: IBM and

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-01-07T12:19:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7vDd.5564$Vj3.5147@newssvr17.news.prodigy.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com> <BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net> <71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`

```
"kprasann" <ashprav@rediffmail.com> wrote in message
news:71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com...
> Hello, I'm trying to abend a micro focus COBOL program in AIX. The COBOL
> program was actually migrated from mainframes and has a CALL to ILBOABN0
> IBM routine.

Why not exit gracefully instead? ABEND on mainframe is usually done to let
the operating system "roll back" all the data created in a JCL steam.

Of course, you *could* force an abnormal termination....

instead of CALL 'ILBOAAN0'  you could...

DIVIDE X BY ZERO

MCM
```

###### ↳ ↳ ↳ Re: IBM and

_(reply depth: 10)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-07T06:36:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105108603.412982.42450@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com> <BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net> <71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`

```
What happens when it does this? Does the linkage fail or does the
program do something else unexpected but does not "bomb"?
Later,
Steve.T
```

###### ↳ ↳ ↳ Re: IBM and

_(reply depth: 10)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-07T15:52:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8vbtt0hlr6ups30d287jhu5grnq2ht97t2@4ax.com>`
- **References:** `<zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com> <BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net> <71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`

```
On Fri, 07 Jan 2005 02:44:22 -0500, "kprasann"
<ashprav@rediffmail.com> wrote:

>Hello, I'm trying to abend a micro focus COBOL program in AIX. The COBOL
>program was actually migrated from mainframes and has a CALL to ILBOABN0
>IBM routine.

call 'abort' using return-code

It will do the same as STOP RUN unless you set other options, such as
the one controlling memory dump.
```

###### ↳ ↳ ↳ Re: IBM and

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-07T16:06:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsyDd.345883$lR6.60588@news.easynews.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <i8jhi0lnnfq33io492caoaq08ls9njuenm@4ax.com> <GoQWc.12222$3O3.11918@newsread2.news.pas.earthlink.net> <kvpoi05spu0odple6vp8gh2sh7hv0sdnro@4ax.com> <BM2Xc.221$W_5.28@newsread1.news.pas.earthlink.net> <71345c8d9e1ad8ea8678fc2c7c99dd15@localhost.talkaboutprogramming.com>`

```
Micro Focus (on some platforms) provide LE callable services.  Check for the 
existence of a CEE3ABD routine (which should be used on current mainframes 
instead of ILBOABN0 anyway)

I am not certain if the AIX products do or don't have the LE callable routines 
available.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 5)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-22T22:00:45+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000722.02dcc743@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net>`

```
Lawrence,

Nice explanation :-)

I wonder what the guy was thinking when he dreamt that up. And no, I 
don't think I'd like to smoke what he's been smoking.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-22T22:39:58-03:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<2ot0a8Fe8gcsU1@uni-berlin.de>`
- **In-Reply-To:** `<VA.00000722.02dcc743@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <VA.00000722.02dcc743@ieee.org>`

```
Doug Scott wrote:

> Lawrence,
> 
…[3 more quoted lines elided]…
> don't think I'd like to smoke what he's been smoking.
I think it was done by someone comfortable with NAND (not and) and NOR 
(not or) gates.  Unix also has its convolutions.  That said, I agree 
that COND was an abomination that never should have seen the light of day.
> 
> ---
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-23T20:39:53+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000724.00cc4d1a@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <VA.00000722.02dcc743@ieee.org> <2ot0a8Fe8gcsU1@uni-berlin.de>`

```
Jr.,

> I think it was done by someone comfortable with NAND (not and) and NOR 
> (not or) gates.

Yes, I got that far in understanding it. It's obviously a hardware 
engineer who invented it. What I can't understand how - even back in the 
sixties - how anyone else could accept and adopt it. I know we had some 
weird languages around at the time, but Sheesh! It's worse than RPG!

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-22T16:42:00-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<Nq8Wc.29087$5s3.23216@fe40.usenetserver.com>`
- **In-Reply-To:** `<lgreenwa-498FD1.02164422082004@chiapp18.algx.net>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net>`

```
Lawrence H Greenwald wrote:
> 
> Having worked on IBM mainframes for over 20 years, I've seen COND and 
…[24 more quoted lines elided]…
> multiple steps!!  Yech!!

I've recently gotten into some more complex ECL (Executive Control 
Language, on the Unisys 2200-style mainframes), and their test condition 
is the same - it seems backwards from the way the 3GL languages do 
If/Else constructs.  I still don't have a good enough grasp of it 
(without the manual at my fingertips) to throw together a little example 
here...

Thanks for the explanation!
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-08-24T20:48:10-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<a/+KBpHpvO2N092yn@visi.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <Nq8Wc.29087$5s3.23216@fe40.usenetserver.com>`

```
Here in comp.lang.cobol, LX-i <lxi0007@netscape.net> spake unto us, saying:

>I've recently gotten into some more complex ECL (Executive Control 
>Language, on the Unisys 2200-style mainframes), and their test condition 
…[3 more quoted lines elided]…
>here...

That's one of the reasons I tended to use CALL macros for my own stuff
(with bits of ECL embedded in appropriate places as needed) instead of
using vanilla ECL runstreams.  It's a very powerful option.

Here's a little CALL code snippet as an example:

      if option('S') then   
         write '@fjtb'; 
         if parameter(1) = '' then  
            write 'COPY FLT::FLT*SYSERRSUMMRY.,FLT*SYSERRSUMMRY.,DDP';  
         else   
            write 'COPY FLT::FLT*SYSERRSUMMRY(-'||parameter(1)||
                  ').,FLT*SYSERRSUMMRY.,DDP';   
         endif; 
         write '@eof';  
         write '@copy,i flt*syserrsummry.,flt*syserr.'||start_date; 
         write '@eof';  
         if parameter(1) = '' then  
               print 'FLT*SYSERRSUMMRY from FLT will be copied to FLT*SYSERR.'  
                      ||start_date; 
         else   
               print 'FLT*SYSERRSUMMRY(-'||parameter(1)||'). from FLT will be'  
                     ||' copied to FLT*SYSERR.'||start_date;
         endif; 
      endif;
      if not option('X') then   
         print 'Note: Combined report has been written to '||   
               'TPF$.CONSCHK/REPORT';   
         query test1 with 'Do you want to view the full report (y/N)?'; 
         if test1 = 'Y' or test1 = 'y' then 
            if total_lines > 23 then
                write '@cshell*cshell.more tpf$.conschk/report';
            else
                write '@eof';   
            endif; 
         endif; 
      endif; 

If you've ever used OS2200 command-line tools like UEDIT, FINDREF, or
CSHELL, this is the macro language they are written in.  FWIW.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** santer1@juno.com (steve)
- **Date:** 2004-09-08T18:26:27-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<9dcb1b0f.0409081726.38b0c219@posting.google.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <Nq8Wc.29087$5s3.23216@fe40.usenetserver.com>`

```
Hey! I have extensive experience in UNISYS 2200 ECL. Who and where are
you? I'd like to contact someone else out there who is using this
stuff.

Steve

LX-i <lxi0007@netscape.net> wrote in message news:<Nq8Wc.29087$5s3.23216@fe40.usenetserver.com>...
> Lawrence H Greenwald wrote:
> > 
…[50 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-09-09T18:55:50-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<c460d.48135$5s3.25298@fe40.usenetserver.com>`
- **In-Reply-To:** `<9dcb1b0f.0409081726.38b0c219@posting.google.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <lgreenwa-498FD1.02164422082004@chiapp18.algx.net> <Nq8Wc.29087$5s3.23216@fe40.usenetserver.com> <9dcb1b0f.0409081726.38b0c219@posting.google.com>`

```
steve wrote:
> Hey! I have extensive experience in UNISYS 2200 ECL. Who and where are
> you? I'd like to contact someone else out there who is using this
> stuff.

Almost all the information you're after is either in my sig block, or 
easily obtainable through it...  :)
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-23T09:03:54-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com>`

```
In article <E6UVc.28452$5s3.19593@fe40.usenetserver.com>,
 LX-i <lxi0007@netscape.net> wrote:

> Joe Zitzelberger wrote:
> > In article <zKWdnexlvbKyyLvcRVn-uw@comcast.com>,
…[57 more quoted lines elided]…
> In the first, MyVarIsDone is not performed - under the second, it is.

JCL is completely declarative.  All IF and COND logic is syntax checked 
before execution begins.  Then, the only alterable variable is the 
return code of each step -- set after execution of said step is complete.

in the case above, myVAR will always be resolved prior to any step 
executing.  The only way it could be different is if the negated 
condition tried to resolve the return code for the first step.

However, such a construct could not be built going from COND to IF.

JCL is one of those places where IBM shows its age.  Imagine computing 
of the early 60's -- then imagine JCL.  They will be the same.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 5)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-23T20:39:55+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000725.00cc541b@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com>`

```
Joe,

> JCL is one of those places where IBM shows its age.  Imagine computing 
> of the early 60's -- then imagine JCL.  They will be the same.

Unfair. I was working with computers in the sixties, and JCL was 
incomprehensible from the day it came out. If you want to know the state 
of the art back then, you'd also need to consider Algol (which became 
Pascal).

But that wasn't IBM.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-23T13:14:33-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<cgdj79$14m1$1@si05.rsvl.unisys.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.00000725.00cc541b@ieee.org...

>  If you want to know the state
> of the art back then, you'd also need to consider Algol (which became
> Pascal).

While ALGOL may have *spawned* or even *inspired* Pascal, it didn't *become*
Pascal.  There are five different dialects of ALGOL ("base" ALGOL,
BDMSALGOL, DMALGOL, DCALGOL and NEWP) and two of Pascal (Pascal, available
to customers, and Pascal83, used for internal products but so far as I know
unavailable to users) in the Unisys MCP environment today.  NEWP includes
some features of Pascal not available in the ALGOLs (most notably enumerated
types).

> But that wasn't IBM.

Still isn't, so far as I know.      ;-)

WFL is ALGOL-based as well; some users think it's rather easier to use and
more powerful than JCL is, or was ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-23T21:32:27+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000727.00fc6bfd@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com>`

```
Chuck,

> While ALGOL may have *spawned* or even *inspired* Pascal, it didn't *become*
> Pascal.

It's called "poetic license". It's the precursor of all block-structured 
languages.

> two of Pascal

You've heard of Borland's Turbo Pascal, aka Delphi, I presume? Again, not pure 
Pascal, but a stronger (IMHO) derivative.

Burroughs went heavily for Pascal-type languages in its systems languages, so 
I'm not surprised that MCP still honours that tradition. I must admit that I 
didn't know MCP had survived.

> WFL is ALGOL-based as well; some users think it's rather easier to use and
> more powerful than JCL is, or was ...

WFL? Anyway ANYTHING is easier to use and more powerful than JCL.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-23T16:43:43-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<cgdvfg$1cpn$1@si05.rsvl.unisys.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com> <VA.00000727.00fc6bfd@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.00000727.00fc6bfd@ieee.org...

> You've heard of Borland's Turbo Pascal, aka Delphi, I presume? Again, not
pure
> Pascal, but a stronger (IMHO) derivative.

Yes, I have.

> Burroughs went heavily for Pascal-type languages in its systems languages,
so
> I'm not surprised that MCP still honours that tradition.

I think you've got the timing wrong.

Burroughs went heavily for block-structured languages, specifically in the
form of an extended version of ALGOL-60, a decade or more before Wirth
developed the first Pascal specification.  The Burroughs B5000 and its
descendants have been honoring that decision, and that dialect, since their
introduction in 1961.   Wirth didn't develop his Pascal specification until
1971.

While it can be argued that the Unisys MCP-based systems honor the
*contributions of Wirth* because of his contributions to ALGOL-60,  it is
anachronistic to say that ALGOL is "Pascal-like" and that therefore MCP
honors the tradition of Pascal-type languages.  It is as anachronistic as to
indicate that Unisys MCP systems honor the traditions established by PL/1 or
ADA by using an ALGOL-60 dialect, or that the music of J. S. Bach owes much
to the compositions of Felix Mendelssohn.

> WFL?

"Work Flow Language".   A block-structured language introduced with the
B5000 in 1961.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-24T21:35:57+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000072d.006297ed@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com> <VA.00000727.00fc6bfd@ieee.org> <cgdvfg$1cpn$1@si05.rsvl.unisys.com>`

```
Chuck,

> it is
> anachronistic to say that ALGOL is "Pascal-like" and that therefore MCP
> honors the tradition of Pascal-type languages.

Sigh. Did I say that? I might have said that the Burroughs stuff was based on 
Algol-type languages. I know very well that Pascal derives loosely from Algol.

> It is as anachronistic as to
> indicate that Unisys MCP systems honor the traditions established by PL/1 or
> ADA by using an ALGOL-60 dialect, or that the music of J. S. Bach owes much
> to the compositions of Felix Mendelssohn.

What planet are you from? Algol was the beginning. There were many 
derivatives, including Pascal and MCP (so I'm told). It would be stretching 
things to say that PL/I was derived from Algol - it merely borrowed a few 
constructs.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-24T14:51:02-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<cggd87$c9$1@si05.rsvl.unisys.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com> <VA.00000727.00fc6bfd@ieee.org> <cgdvfg$1cpn$1@si05.rsvl.unisys.com> <VA.0000072d.006297ed@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.0000072d.006297ed@ieee.org...

> > anachronistic to say that ALGOL is "Pascal-like" and that therefore MCP
> > honors the tradition of Pascal-type languages.
>
> Sigh. Did I say that? I might have said that the Burroughs stuff was based
on
> Algol-type languages.

What you wrote was "Burroughs went heavy for Pascal-like languages, so I'm
not surprised that MCP still honours that tradition."   Unisys MCP is not
"honoring the traditions" established by Pascal-like languages for the same
reason that Bach didn't honor the traditions established by Mendelssohn.

> I know very well that Pascal derives loosely from Algol.

Not all that loosely, by what I read in the historical record!

>    ... Algol was the beginning. There were many
> derivatives, including Pascal and MCP (so I'm told).

MCP is not a *derivative of* ALGOL, it is *written in* a derivative of ALGOL
(NEWP).

> It would be stretching
> things to say that PL/I was derived from Algol - it merely borrowed a few
> constructs.

I think the basic block/procedure structure of PL/1 did more than "borrow a
few constructs" from ALGOL.  From what I can tell, the language can
simplistically be characterized as a synthesis of the block structure and
loop-control mechanisms of ALGOL with the record declaration capabilities of
COBOL, while keeping a side-glance at the FORTRAN application.  All things
to all people.  Such the 1968-vintage language spec from IBM I have at hand
leads me to believe, anyway.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 8)_

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-08-25T08:01:18-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<g63pi01rlonljselmihb7kble46r15rsvm@4ax.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com> <VA.00000727.00fc6bfd@ieee.org>`

```
Actually to be accurate, Turbo Pascal is not the same as Delphi.
While both are elementally "Pascal" in the language sense, Delphi
changed the language constructs to the point that Delphi could be
considered a descendent of Turbo Pascal and therefore technically a
different language with different skill sets.  While someone versed in
Delphi could go and use Turbo Pascal with very little adjustment,
someone versed in Turbo Pascal would be comfortable with the syntax
conventions of Delphi, but would have to re-learn most of the standard
constructs.

On Mon, 23 Aug 2004 21:32:27 +0100, Doug Scott <dwscott@ieee.org>
wrote:

>You've heard of Borland's Turbo Pascal, aka Delphi, I presume? Again, not pure 
>Pascal, but a stronger (IMHO) derivative.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 8)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-08-26T16:04:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgl1mm011ov@news2.newsguy.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com> <VA.00000727.00fc6bfd@ieee.org>`

```

In article <VA.00000727.00fc6bfd@ieee.org>, Doug Scott <dwscott@ieee.org> writes:
> 
> > WFL is ALGOL-based as well; some users think it's rather easier to use and
> > more powerful than JCL is, or was ...
> 
> WFL? Anyway ANYTHING is easier to use and more powerful than JCL.

I submit that OS/400 CL is harder to use and less powerful than JCL,
despite being the only IBM-supplied "scripting" mechanism included
with the OS.  At least for OS/400 V3 and earlier.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-23T22:19:27-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<217e491a.0408232119.618bb5ee@posting.google.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote

> >  If you want to know the state
> > of the art back then, you'd also need to consider Algol (which became
…[3 more quoted lines elided]…
> Pascal.  

There was a request for proposals for what was to be Algol-68. 
Various different proposals were made including what Wirth called
Algol-W (and also such things as RRE's Alogol-68R).  Wirth later
renamed his language as Pascal.

Of course Algol-W never was 'Algol' or 'Algol-68'.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-08-24T21:04:00-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<QO/KBpHpvi+R092yn@visi.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <cgdj79$14m1$1@si05.rsvl.unisys.com>`

```
Here in comp.lang.cobol,
"Chuck Stevens" <charles.stevens@unisys.com> spake unto us, saying:

>WFL is ALGOL-based as well; some users think it's rather easier to use and
>more powerful than JCL is, or was ...

I really liked what I saw of WFL when I played with it for a few months
at a client site.  Seems like a fairly flexible job control language.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-23T21:46:50-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<joe_zitzelberger-A06D93.21465023082004@knology.usenetserver.com>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org>`

```
I don't think JCL is incomprehensible -- just lame.  It lacks obvious 
features that IBM should have added about the time they went from paper 
tape to punch cards.  And even more features that should have shown up 
when direct access devices became common.

But all IBM ever did was add an IF statement and say 'use Rexx if you 
want something else'...


In article <VA.00000725.00cc541b@ieee.org>,
 Doug Scott <dwscott@ieee.org> wrote:

> Joe,
> 
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-08-24T21:35:58+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000072e.00629a09@ieee.org>`
- **References:** `<ohhSb.561$b77.1266@dfw-service2.ext.raytheon.com> <zKWdnexlvbKyyLvcRVn-uw@comcast.com> <joe_zitzelberger-76A5A2.14354321082004@knology.usenetserver.com> <E6UVc.28452$5s3.19593@fe40.usenetserver.com> <joe_zitzelberger-2DE865.09035423082004@knology.usenetserver.com> <VA.00000725.00cc541b@ieee.org> <joe_zitzelberger-A06D93.21465023082004@knology.usenetserver.com>`

```
Joe,

> I don't think JCL is incomprehensible -- just lame.

:-) OK. Lame it is.

> It lacks obvious 
> features that IBM should have added about the time they went from paper 
> tape to punch cards.

??? IBM were never into Paper tape. They ALSO supported paper tape, as 
80-column images. They had too much invested in punched card machinery - 
in fact, that's what held up the development of IBM computers - Thomas J 
could foresee that computers could signal the end of punched cards.

> But all IBM ever did was add an IF statement and say 'use Rexx if you 
> want something else'...

Wel, that's advancing a lot of years. REXX is a fine language. The best 
thing I like about it is that the author threw away the rule book on 
syntax/semantics, and implemented intuitive constructs.

---

Doug

dwscott@ieee.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
