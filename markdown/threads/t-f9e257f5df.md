[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ORB Cobol

_11 messages · 7 participants · 1999-08 → 1999-09_

---

### ORB Cobol

- **From:** Jean-Marie MORAUX <jean-marie.moraux@sib.fr>
- **Date:** 1999-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C69E63.8C43B00A@sib.fr>`

```
        Hello,

I'm looking for a ORB that could offer a Cobol mapping, on Windows NT or
Unix.
As anybody head of something like that.

thanks
```

#### ↳ Re: ORB Cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c85781.241859357@news1.ibm.net>`
- **References:** `<37C69E63.8C43B00A@sib.fr>`

```
Fofgive my ignorance, but what is an ORB?

On Fri, 27 Aug 1999 16:19:16 +0200, Jean-Marie MORAUX
<jean-marie.moraux@sib.fr> wrote:

>        Hello,
>
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: ORB Cobol

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7q9nu0$47i@dfw-ixnews5.ix.netcom.com>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote in message
news:37c85781.241859357@news1.ibm.net...
> Fofgive my ignorance, but what is an ORB?
>

In the world of "a little knowledge is a dangerous thing" -

My knowledge - "ORB" is "Object Request Broker"

My ignorance - "I don't really know what that means"
```

##### ↳ ↳ Re: ORB Cobol

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G0_x3.15267$YB3.212097@news1.frmt1.sfba.home.com>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote:
> Fofgive my ignorance, but what is an ORB?

you are Fofgiven.

Object Request Broker (essentially, application middleware).

a coupla vendors:

http://www.borland.com/visibroker/
http://www.iona.com/products/orbixchoice.html

Jean-Marie MORAUX <jean-marie.moraux@sib.fr> wrote in message
news:37C69E63.8C43B00A@sib.fr...
> I'm looking for a ORB that could offer a Cobol mapping, on Windows NT or
> Unix.

i think MERANT Micro Focus (http://www.merant.com/ads/index.asp) has (at
times) provided bindings (via IDL) for various CORBA compliant ORB's, but i
don't know what the current status is.
```

##### ↳ ↳ Re: ORB Cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C8BFC4.B34E8B2B@home.com>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> Fofgive my ignorance, but what is an ORB?
…[5 more quoted lines elided]…
> >

ORB(Object Request Broker)

From the Micro Focus on-line glossary :-

ORBIX is a CORBA based middleware platform from Iona on which NetExpress
developers can create and run distributed applications. Orbix
applications can be written in a variety of different languages, such as
COBOL, C++, or Java, and interact together in a transparent manner at an
enterprise level across a broad range of different platforms. For
additional information about ORBIX, refer to the Iona ORBIX home page at
http://www.iona.com.

If you're reading this Warren - more $10 words !

Jimmy, Calgary AB
```

##### ↳ ↳ Re: ORB Cobol

- **From:** "Albert Ratzlaff R." <albert@conexion.com.py>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CA7A1D.68D7F41B@conexion.com.py>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> Forgive my ignorance, but what is an ORB?
> 

Object Request Broker. Best thing since bread and butter. :-)
You define object interfaces (assume that by this time everybody at
least has heard of objects - myself have only theoretical knowledge).
You use the interfaces methods (used to call them procedures) to do
things. The broker finds out on which machine, and in which language,
the object is implemented, and makes the connection. If there is a
result, you get it back. Your program can be written in COBOL, C, C++,
Java, Smalltalk, ADA (I think), and probabley some others. The object
itself also can be written in any of these languages, and run anywhere
on a network. You don't need to know where. You just talk to the
interface. There is a a IDL (interface definition language) which is
universal - it's something like C++, and a compiler which translates the
IDL to the particular language used.
CORBA means Common ORB Arquitecture. You can get more information at
www.omg.org. Definitely worth looking into.
Disclaimer: I don't have any practical experience with this. Just read a
bit.

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: ORB Cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cb246f.43156192@news1.ibm.net>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net> <37CA7A1D.68D7F41B@conexion.com.py>`

```
This whole topic intrigued me, so I found a source that explains it
ALL.

http://www.omb.org

It's very interesting stuff.

You can see by the data types that the broker uses, however, that is
is a bit "anti" COBOL.



On Mon, 30 Aug 1999 08:33:33 -0400, "Albert Ratzlaff R."
<albert@conexion.com.py> wrote:

>Thane Hubbell wrote:
>> 
…[22 more quoted lines elided]…
>Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: ORB Cobol

_(reply depth: 4)_

- **From:** "Albert Ratzlaff R." <albert@conexion.com.py>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CBB889.CEEE0CB7@conexion.com.py>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net> <37CA7A1D.68D7F41B@conexion.com.py> <37cb246f.43156192@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> This whole topic intrigued me, so I found a source that explains it
…[7 more quoted lines elided]…
> is a bit "anti" COBOL.

For one, you need pointers. That's not posible with the COBOL I use (RM
on Unix). But you can write a C server process that talks to a COBOL
program, so that would be an indirect way for interfacing to a "legacy"
system (or is "heritage" now the politicaly correct term? :).

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: ORB Cobol

_(reply depth: 4)_

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cc43fd@eeyore.callnetuk.com>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net> <37CA7A1D.68D7F41B@conexion.com.py> <37cb246f.43156192@news1.ibm.net>`

```
CORBA is the OMG Request Broker. MicroSoft's Common Object Model (COM) does
the same job and is the basis for .OCX and ActiveX controls. These controls,
if developed according to the COM standard, are language independent anyway
and remove the need for a CORBA type function. ActiveX controls can be
developed in ANY language and do NOT require a "broker" as such. It is
interesting that the OMG is about to embrace the COM model with CORBA (not
vice/versa). There has been some competition between the 2 standards for
some time and it is good to see it being resolved.

You can develop COM (and therefore, soon to be CORBA) compliant ActiveX
controls in Fujitsu PowerCOBOL which supports the COM model. This allows you
to produce re-usable pluggable controls with defined methods and properties.
These controls can be placed on your GUI windows just like any other
"button" and can be visible or invisible to the user. Fujitsu provide
standard ones for Database access (very VB like...), node lists, timers,
floating toolbars, and a whole plethora too numerous to mention. They claim
you can freely mix these with 3rd Party ActiveX controls (which may have
been written in any language) as long as they are COM compliant, including
controls you may have developed yourself. I thought this was a bit too good
to be true, so I tried it.... Guess What?

It works perfectly with no hassles.

I now have a re-usable scheduling engine which allocates resources and staff
to appointments for ANY application which requires an appointment book (you
have to set up a relational database with structures to support whatever
ACTIVITIES, STAFF, and RESOURCES you need, but this can easily be done in
co-operation with the User. There is no coding, just a data analysis and
entry. The scheduling (ActiveX) control does the rest (including all the DB
access and updating via the appropriate methods). Ideal for Hospitals,
Doctors, Dentists, even Restaurants or any professional service which needs
to have allocated appointments.) I have similar controls for handling
Clients, entering dates (all millennium compliant for the next 26,000
years...), interfacing to Crystal Reports, and so on...

Our systems no longer use COBOL access methods (apart from LINE Sequential)
no more ISAM or Relational access. Everything is via ODBC using re-usable
modules  (for mainframe and PC) or ActiveX controls (PC only). Once the
methods are written and de-bugged that's it. EVERYTHING is designed to be
low-maintenance and platform independent.

The net result is that we can "tailor" a system to a client very quickly.
It's like assembling cars from sub-components.

As you will have gleaned from the above, I am completely "sold" on the
object model for system development.

COBOL is an ideal language for developing commercial components. Fujitsu are
to be commended for providing a development environment which actively
encourages the use of COM compliant modules.

Pete.




Thane Hubbell wrote in message <37cb246f.43156192@news1.ibm.net>...
>This whole topic intrigued me, so I found a source that explains it
>ALL.
…[38 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ORB Cobol

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cd168a.170689546@news1.ibm.net>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net> <37CA7A1D.68D7F41B@conexion.com.py> <37cb246f.43156192@news1.ibm.net>`

```
On Tue, 31 Aug 1999 00:41:19 GMT, redsky@ibm.net (Thane Hubbell)
wrote:

>This whole topic intrigued me, so I found a source that explains it
>ALL.
…[4 more quoted lines elided]…
>

I messed that up.  http://www.omg.org
```

###### ↳ ↳ ↳ Re: ORB Cobol

_(reply depth: 5)_

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ce8b67@eeyore.callnetuk.com>`
- **References:** `<37C69E63.8C43B00A@sib.fr> <37c85781.241859357@news1.ibm.net> <37CA7A1D.68D7F41B@conexion.com.py> <37cb246f.43156192@news1.ibm.net> <37cd168a.170689546@news1.ibm.net>`

```

Thane Hubbell wrote in message <37cd168a.170689546@news1.ibm.net>...
>On Tue, 31 Aug 1999 00:41:19 GMT, redsky@ibm.net (Thane Hubbell)
>wrote:
…[3 more quoted lines elided]…
>>
http://www.omg.org
>
>
This is a very good site, but it does not explain it ALL...it explains it
from the CORBA point of view. MicroSoft have a competing standard called
COM. CORBA will shortly become COM compliant. Need we say more...? :-)

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
