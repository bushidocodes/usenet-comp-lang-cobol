[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus Net Express��� with .NET

_19 messages · 8 participants · 2003-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus Net Express��� with .NET

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-05T17:43:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net>`

```
For more information on Micro Focus' .NET COBOL product, see:

     http://www.microfocus.com/products/netexpress/NetExpresswNET.asp

This is a "follow-up" on my note about the "First Friday" webcast on this
product, discussed at:

     http://www.microfocus.com/promotion/NAWCFRFR1003/
```

#### ↳ Re: Micro Focus Net Express��� with .NET

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-05T17:50:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zLaqb.1565$Z25.109@newsread4.news.pas.earthlink.net>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net>`

```
P.S.  I have no financial or other interest <G> in Micro Focus.  I do still
own a few shares of MERANT stock - but that has NOTHING to do with the "new"
Micro Focus!!!

P.P.S.  The first person who is actually ABLE to do an "impartial"
comparison between the Fujitsu and Micro Focus .NET products, will certainly
get some gratitude from me.  As I *read* the Micro Focus documentation, they
have "full" support for all the language supported in the older Net Express
product, but I haven't seen an LRM yet, so I don't know.
```

#### ↳ Re: Micro Focus Net Express® with .NET

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-05T17:53:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311051753.74d3255f@posting.google.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net>`

```
Bill,

I am writing this from the viewpoint of an interested individual.  I
have not seen the product and my information is based only on what I
have read on the website.

For me - what matters more is what's under the covers.

Is the .NET implementation fully .NET?  That is - is it entirely
managed code?

For example - the Fujitsu .NET compiler uses an interface to native
code for indexed file access.  This means that if I used indexed
files, I need to distribute the Fujitsu runtime for Windows (and own
that product).

In addition - even if I don't use indexed files, I need to distribute
certain Fujitsu dll's as part of my assembly in order to ensure that
the program will run under the CLR.

Fujitsu provides helper classes for handing (or specifically not
handling) conversion of data and type validation in calls and invokes.

An additional - and very "handy" feature or inter-language use with
Fujitus's .NET product is the automatic conversion of group level
items to System.String objects.  This allows reference via SET and a
whole host of things to work very seamlessly under .NET.

I'm curious how MF handled this.

Fujitsu - at least in the initial release - made concessions on the
COBOL side in favor of .NET compliance.  (Such as lack of a Factory
object, and no multiple inheritence with COBOL).  What did MicroFocus
do?

I noticed the web page specifically mentioned console application
templates.  That leads me to believe - since it's not mentioned (that
I could find) I don't think there is COBOL integration for Winforms
and Webforms --- YES I know the site mentions that the CLASSES for
Winforms and Webforms can be used but with Fujitsu COBOL one can use
the intergrated Forms Designer and create this from COBOL.  It remains
an event driven interlaced code system (and I instead us SP2 for my UI
even under .NET).

One thing Fujitsu has not done - as of yet - is offer a direct
migration of PowerCOBOL code to .NET.  I don't see a mention of Dialog
System to .NET on the web page - though other pages tell people to ask
about Dialog System and .NET.

I'm very anxious to see what's what here and what's really going on -
how much is native code and how much is managed?  How much of the
managed are helper classes provided by MicroFocus?   How easy is it to
distribute a system written using the COBOL for .NET?


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net>...
> For more information on Micro Focus' .NET COBOL product, see:
> 
…[5 more quoted lines elided]…
>      http://www.microfocus.com/promotion/NAWCFRFR1003/
```

##### ↳ ↳ Re: Micro Focus Net Express® with .NET

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-06T02:26:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FA9B0FA.E4BAE708@shaw.ca>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com>`

```

Thane Hubbell wrote:

> Bill,
>
…[51 more quoted lines elided]…
>

Not an answer to your specific queries - but as a result of asking about OO drawing/painting, just days ago, unsolicited, the
following was included in the reply from M/F :-

"BTW - With the release of the .Net compiler today you can use
Winforms which has the new datagrid control. This allows editing of
data items but you need to move to .Net in order to use it. "

So much of this new fangled stuff comes along with an hurrah ! I think what should be more important to us developers is that
'enhanced' products contain backwards compatibility - how well either F/J or M/F have done that I have no idea. If you want an
analogy - if every five years we change a vehicle, we *do* expect it to be similar to what we were used to driving. If the new
'whiz bang' has the driver's seat placed in the back of the auto with a periscope to stare out - I don't think any of us is going
to be too thrilled.

My immediate concern is the emphasis on MICROSOFT just like Time Magazine ran those blurbs on the useless yuppies starting up
dot.coms until the flower wilted. No, I don't think MS is about to go belly up - but for 'shareholder' JerryMouse and his
reference to Linux cults - did he catch this piece in his local newspaper, roughly two weeks ago :-

Somewhat uncomfortable with MS "commercial power", both Japan and S.Korea are starting to plug Linux and are trying to bring the
People's Republic on board. It may never happen - BUT - if it does,  those three present a pretty significant number if you
starting counting all the zeroes in their population figures.

As for Bill's "performance query" - which nut is going to shell out the price for both compilers to find out <G>

Jimmy

>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net>...
…[7 more quoted lines elided]…
> >      http://www.microfocus.com/promotion/NAWCFRFR1003/
```

###### ↳ ↳ ↳ Re: Micro Focus Net Express® with .NET

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-06T03:04:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FA9B9CA.647C74E3@shaw.ca>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca>`

```
Thane,

Where I talked about "Microsoft power" - I should have also added the following.

I recently had a message from somebody, (more than just competent in OO COBOL and 'Webbing'),  who must have been working on a Beta
of the product. He's already mentioned about using C++ (in preference to Java).
Get the drift ? To put it bluntly - Microsoft don't give a SHIT just so long as it has 'MS' emblazoned all over it. There will, where
advantageous, be a tendency for COBOL developers to move into VB, C++ etc...- and then from there...... ?.

Ironically the greatest enemies of COBOL programmers are - IBM and Microsoft.
MS has been advertising in Canada to outsource to them letting them 'do your thing' in MS products. For the second time in a row the
papers picked up on yet another large company, (something like 200-300 developers) who have been outsourced to IBM - the complete
staff is switched over to the IBM payroll - then of course the attrition takes place. Sorry don't remember the names but one
reference was to a big accounting house - Price Waterhouse, I think.

If this is going on in Canada, then it's a fair bet it is ten-fold in the U.S.

On a 'funny' note - from the 'International Express' - two outfits in UK, one of them being what I would have referred to as British
Rail (in my time), are contemplating outsourcing their query desks to India. So you phone for the next train from Portsmouth to
London - "My goodness gracious, I yam havin' much difficulty pleese. How is it, how do you spell Plotsmeth ?

PS. Ever tried phoning a local/state/federal department with an enquiry - where the person on the other end of the phone has a thick
Indian(East) accent ?

Jimmy
```

###### ↳ ↳ ↳ Re: Micro Focus Net Express��� with .NET

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-06T06:46:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T6mqb.111259$RP2.81894@twister.tampabay.rr.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3FA9B9CA.647C74E3@shaw.ca...
> Thane,
> Where I talked about "Microsoft power" - I should have also added the
following.
>
> I recently had a message from somebody, (more than just competent in OO
COBOL and 'Webbing'),  who must have been working on a Beta
> of the product. He's already mentioned about using C++ (in preference to
Java).
> Get the drift ? To put it bluntly - Microsoft don't give a SHIT just so
long as it has 'MS' emblazoned all over it. There will, where
> advantageous, be a tendency for COBOL developers to move into VB, C++
etc...- and then from there...... ?.
I've never worked at seen a company who does care about anything other than
itself...so your point is?  Sun doesn't care about Java unless it has Sun on
it.  IBM ensures that everyone calls their product IBM whatever...and not
whatever IBM.  It is not Websphere MQ from IBM but IBM Websphere MQ.  Dell
just changed its name to Dell so that people would see it cares about
business units and not just the home market.  My VW has a giant VW on the
front and my friends Lexus a large L and my other friends CIVIC has CI IC on
it.

> Ironically the greatest enemies of COBOL programmers are - IBM and
Microsoft.
The greatest enemy of COBOL programmers is, ironically, COBOL.

> MS has been advertising in Canada to outsource to them letting them 'do
your thing' in MS products. For the second time in a row the
> papers picked up on yet another large company, (something like 200-300
developers) who have been outsourced to IBM - the complete
> staff is switched over to the IBM payroll - then of course the attrition
takes place. Sorry don't remember the names but one
> reference was to a big accounting house - Price Waterhouse, I think.
> If this is going on in Canada, then it's a fair bet it is ten-fold in the
U.S.
Price Waterhouse was much bigger deal than 200-300 employees!  IBM bought
(not an outsource) PWC and 30,000 employees.

> On a 'funny' note - from the 'International Express' - two outfits in UK,
one of them being what I would have referred to as British
> Rail (in my time)
Isn't it British Rail again now? I thought that they were going to
"publicise" or buy back the rail from the private sector (no doubt including
a monetary incentive to the important investors).

> are contemplating outsourcing their query desks to India. So you phone for
the next train from Portsmouth to
> London - "My goodness gracious, I yam havin' much difficulty pleese. How
is it, how do you spell Plotsmeth ?
You are about 5 years behind.  Nowadays when you call a help desk the people
have been trained to talk just as you would expect them to.  That Chicago
accent is probably in Bangalore or Malaysia somewhere.  If they have an
accent that is indian then the company is "really" cheap....well this would
be the British government.

> PS. Ever tried phoning a local/state/federal department with an enquiry -
where the person on the other end of the phone has a thick
> Indian(East) accent ?
Whatever happened to all the Irish accents you used to hear?

JCE
```

###### ↳ ↳ ↳ (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-11-06T09:00:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bodumj$149j$1@si05.rsvl.unisys.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com>`

```
JCE wrote:

<<My VW has a giant VW on the front and my friends Lexus a large L and my
other friends CIVIC has CI IC on it.>>

Who else remembers the Austin Se7en variant of the Morris Mini?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 6)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-06T17:38:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com>`

```

Chuck Stevens <charles.stevens@unisys.com> wrote in message news:bodumj$149j$1@si05.rsvl.unisys.com...
> JCE wrote:
>
…[3 more quoted lines elided]…
> Who else remembers the Austin Se7en variant of the Morris Mini?

I remember them all.  My boss used to pick me up for work
in his green Cooper S.  Later, I owned the Austin Minivan,
until an unfortunate encounter with a concrete lamppost at 60 MPH.

My first car was an Austin 7, gifted to me by our IBM SE
who had just indulged himself with a Jag.

This isn't my car, but it looked a lot like it
http://www.austin7.org/AYC.BMP
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-11-07T15:00:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<boh860$f8n$1@si05.rsvl.unisys.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net...

> My first car was an Austin 7, gifted to me by our IBM SE
> who had just indulged himself with a Jag.
>
> This isn't my car, but it looked a lot like it
> http://www.austin7.org/AYC.BMP

Nice!   I can't see the emblem, but it does look to me like it reads "Austin
Seven".  What I was referring to is that the Mini version emblem actually
read "Se7en".  I believe this was immortalized in a recurrent topic in Walt
Kelly's famous comic strip "Pogo" along the lines of "How do you spell
that?"  "With a seven."

Did the spelling "Se7en" in the emblems on the vehicle identifying it as an
Austin Seven predate the Mini version?   I thought this was an innovation
introduced with the resurrection of the famous old name for the shared
Austin/Morris product.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 8)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-08T01:04:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com>`

```

Chuck Stevens <charles.stevens@unisys.com> wrote in message news:boh860$f8n$1@si05.rsvl.unisys.com...
>
> "Hugh Candlin" <no@spam.com> wrote in message
…[12 more quoted lines elided]…
> that?"  "With a seven."

I'm not sure, but they may be referring to the movie?
>
> Did the spelling "Se7en" in the emblems on the vehicle identifying it as an
> Austin Seven predate the Mini version?   I thought this was an innovation
> introduced with the resurrection of the famous old name for the shared
> Austin/Morris product.

The car was introduced as the Austin Seven and the Morris Mini Minor,
if I remember correctly, as there was a very popular car called the
Morris Minor, which looked like a bloated VW bug.  I think that there
was a larger version called the Morris Major, but I'm not sure.
I do not recall ever seeing a Se7en emblem.  I think that that nomenclature
was just used in the advertising copy.

Regardless, nobody ever called the Morris or the Austin
anything but "a Mini".
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 9)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-08T03:28:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MpZqb.25931$jW5.485194@twister.tampabay.rr.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message news:8iXqb.33321
> Regardless, nobody ever called the Morris or the Austin
> anything but "a Mini".
The morris minor was *always* a morris minor and never a mini.

But then the reliant robin was always called a robin reliant....go
figure....

JCE
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 10)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-08T04:22:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gc_qb.215045$0v4.16568912@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net> <MpZqb.25931$jW5.485194@twister.tampabay.rr.com>`

```

jce <defaultuser@hotmail.com> wrote in message news:MpZqb.25931$jW5.485194@twister.tampabay.rr.com...
> "Hugh Candlin" <no@spam.com> wrote in message news:8iXqb.33321
> > Regardless, nobody ever called the Morris or the Austin
> > anything but "a Mini".

> The morris minor was *always* a morris minor and never a mini.

Correct.  To be clear, let me rephrase slightly

Regardless, nobody ever called the Morris Mini Minor
or the Austin Mini anything but "a Mini".

How's that?
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express® with .NET

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-08T10:11:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311081011.30267bdf@posting.google.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net> <MpZqb.25931$jW5.485194@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote 

> The morris minor was *always* a morris minor 

Except when it was a Morris 1000.

> and never a mini.
 
> But then the reliant robin was always called a robin reliant....go
> figure....

It was ? By whom ?
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express® with .NET

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-07T22:40:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311072240.4857f8b9@posting.google.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote 

> I think that there
> was a larger version called the Morris Major, but I'm not sure.

There was, but (in time frame '50s and '60s) only in Australia.

The car was intended to replace the Minor with a 1200 cc motor, but
was only built in the UK as the Riley 1.5 and Wolsey 1500 with a 1500
cc motor.  It was built in Australia as the Morris Major and Austin
Lancer.
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 10)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-08T07:50:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bf1rb.34397$Ec1.2892964@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net> <217e491a.0311072240.4857f8b9@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message news:217e491a.0311072240.4857f8b9@posting.google.com...
> "Hugh Candlin" <no@spam.com> wrote
>
…[8 more quoted lines elided]…
> Lancer.

The larger version that I was thinking of was called the Morris Oxford
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2003-11-08T11:48:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<687qqvcnt6dsjdq0s8160cg35po81ngl4a@4ax.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net>`

```
On Sat, 08 Nov 2003 01:04:04 GMT, "Hugh Candlin" <no@spam.com>
enlightened us:

>
>Chuck Stevens <charles.stevens@unisys.com> wrote in message news:boh860$f8n$1@si05.rsvl.unisys.com...
…[32 more quoted lines elided]…
>

The car was launched to the public on the 26th of August 1959 through
both Austin and Morris franchises worldwide. Badged as the Austin
Seven and the Morris Mini Minor the car was priced at ï¿½496. The first
winter of production saw a host of problems for the little car.
Leaking sills, rotting carpets, water logged distributors (later cars
were fitted with a card sheet to try to keep the electrics dry) to
name but a few. At the launch of the Mini, eighty cars were loaned to
leading figures to try to tempt the public into buying a
"technological marvel". This culminated in the Queen being taken for a
drive around Windsor Park by Alec Issigonis of BMC, the designer of
the car.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


"I once wanted to become an atheist but I gave up.
They have no holidays."
..... Henny Youngman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: (OT) was Re: Micro Focus Net Express��� with .NET

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-11-17T09:25:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpb0ad$kuk$1@si05.rsvl.unisys.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca> <3FA9B9CA.647C74E3@shaw.ca> <T6mqb.111259$RP2.81894@twister.tampabay.rr.com> <bodumj$149j$1@si05.rsvl.unisys.com> <oGvqb.207541$0v4.16400626@bgtnsc04-news.ops.worldnet.att.net> <boh860$f8n$1@si05.rsvl.unisys.com> <8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:8iXqb.33321$Ec1.2859518@bgtnsc05-news.ops.worldnet.att.net...
>
> The car was introduced as the Austin Seven and the Morris Mini Minor,
…[3 more quoted lines elided]…
> I do not recall ever seeing a Se7en emblem.  I think that that
nomenclature
> was just used in the advertising copy.

No, that's just it.  It may have been an export-only issue, but we had a
local dealership that carried both the MiniMinor (and I remember it as
MiniMinor, not Mini Minor) and the Se7en upon their introduction to the US,
and I clearly remember the Austin's emblem *as imported here*.

This would have been sometime between September 1959 and June 1961 (and most
likely earlier than later in that period).  I visited the dealership at the
time and actually got to take one out -- probably the Morris variant -- for
a test drive!

I was out of the country (central Venezuela, of all places!) all summer in
'61, and by the following fall had my very own well-thrashed '52 MG TD
(those were the days -- my father paid the grand sum of $265 for it), so I
wasn't taking test drives on my visits to the dealership, only buying parts!
June 1961 is an absolute "terminus ad quem" for my introduction to the
MiniMinor variants; a more likely date would be not long after the release
data SkippyPB mentioned -- 26 August 1959.  It was big news back then, and
my visits to the dealership were at the height of the publicity about the
car.  Probably no later than November 1959.

I'm almost certain the Austin variant faded VERY quickly from the US market.

    -Chuck Stevens
```

###### ↳ ↳ ↳ [OT]Re: Micro Focus Net Express��� with .NET

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-06T06:52:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tcmqb.111307$RP2.84554@twister.tampabay.rr.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3FA9B0FA.E4BAE708@shaw.ca...
>
> Somewhat uncomfortable with MS "commercial power", both Japan and S.Korea
are starting to plug Linux and are trying to bring the
> People's Republic on board. It may never happen - BUT - if it does,  those
three present a pretty significant number if you
> starting counting all the zeroes in their population figures.

A billion people is a lot.  The fact that 950,000,000 of these don't have
their own PCs probably means that the impact is not as great as one would
imagine.

It is in the interest of the pursuers of globalization to closely regulate
the level of freedom that these individuals have.  I can rest assured
knowing that the Chinese government is about to give 1 billion people the
freedom to unionize, collect and be empowered.  (As much as Friedman
suggests that this is going to happen in his eutopian global world).

Half of microsoft products in the world are ripped off anyway.

This has nothing to do with COBOL of course.

JCE
```

###### ↳ ↳ ↳ Re: Micro Focus Net Express® with .NET

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-06T08:36:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311060836.23bba82b@posting.google.com>`
- **References:** `<TEaqb.1550$Z25.441@newsread4.news.pas.earthlink.net> <bfdfc3e8.0311051753.74d3255f@posting.google.com> <3FA9B0FA.E4BAE708@shaw.ca>`

```
Just one comment...

"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3FA9B0FA.E4BAE708@shaw.ca>...
> 
> 
…[6 more quoted lines elided]…
> starting counting all the zeroes in their population figures.

Well - while I doubt either compiler (Fujitsu or MF) can support them
because of the add on classes - there is a .NET implementation
(several actually) for Linux - and even Winforms with GNUDotNet.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
