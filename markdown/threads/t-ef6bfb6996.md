[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to hide cobol code

_10 messages · 6 participants · 2001-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to hide cobol code

- **From:** Ron Bell <ronbell@cais.com>
- **Date:** 2001-06-22T16:53:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B33B050.78A8609B@cais.com>`

```
William M. Klein" wrote:
> 
> What compiler and what operating system?
…[14 more quoted lines elided]…
> > ronbell@cais.com

I am using IBM mainframe OS/390 cobol.  Years ago I remember using
something like 'printoff' and 'printon' statements to stop/start the
display of code when it compiled, I will try that.  Copy statements are
easy to hide with the 'suppress' command.  My programs include a lot of
++include statements which generate a lot of CICS code (like 25,000
lines of compiled output), so I need to hide the ++include code.  Thanks
for your reply,
```

#### ↳ Re: How to hide cobol code

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-22T16:22:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h0ctv$3cd$1@nntp9.atl.mindspring.net>`
- **References:** `<3B33B050.78A8609B@cais.com>`

```
A few answers for you (for IBM mainframe environments)

A) ++includes are PANVALET, not COBOL syntax.  Therefore, you may want to
check their manuals for the best way to handle those statements

B) If you are using a currently supported COBOL (IBM COBOL for
this-and-that), then you may place a

  *CBL NOLIST
      or
   *CONTROL NOLIST

statement before code that you do not want to show in a listing.  For more
information, see:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igylr205/8.1.3?

C) If the code to be "hidden" is in a copybook (not ++include) then you can
(as suggested elsewhere) use the IBM extension of COPY SUPPRESSING.

    ***

All of these are ways to hide the source from the LISTING.  *None* of them
prevent a programmer from actually "looking" at the members via non-compile
methods.  For something like that you would want to use your security
package (e.g. RACF, ACF, etc).  However, you should be aware that the
compile process itself *must* have "read" access to the source code.
Therefore, I can't (easily) think of a way of preventing the programmer (who
really wants to) manually reading this source outside the compile process.
The only way that you could avoid this would be to REQUIRE that the
"average" programmer go thru a "security" person to submit compiles.  This
would be highly unusual and pretty user-unfriendly, but COULD theoretically
be done.

NOTE:
  Another thing you MIGHT want to think about is putting all of your
"secure" source code (to be copied in) in a separate (RACF protected)
library and always use the
   COPY xxx  OF yyy
format of the COPY statement.  In this way, the DDName (pointed to by YYY)
could have a "higher" security requirement than where normal source is
found.

If the thing that you want to "secure" is actually procedural code, then I
would suggest that you put it into a separate "callable" module that simply
has a "documented" interface.  (Or better yet, start thinking about OO COBOL
and "encapsulation").  In this way, all the "others" would need was access
to your "load module" - and would never see the code involved.
```

##### ↳ ↳ Re: How to hide cobol code

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-22T16:25:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h0d3e$ruq$1@slb1.atl.mindspring.net>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net>`

```
Correction to my samples, what you are interested in are:

   *CBL NOSOURCE   (not NOLIST)
```

##### ↳ ↳ Re: How to hide cobol code

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-22T22:03:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B33C04E.3D98E80D@home.com>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:

> If the thing that you want to "secure" is actually procedural code, then I
> would suggest that you put it into a separate "callable" module that simply
> has a "documented" interface.  (Or better yet, start thinking about OO COBOL
> and "encapsulation").  In this way, all the "others" would need was access
> to your "load module" - and would never see the code involved.

Well Bill - that's real neat. You've actually found an excuse for using OO with
a mainframe <G>. I can just see Howard running up one wall, across the ceiling
and down the other wall. "Encapsulation ?", he says. "You've got to be kidding.
How the hell can I test my modules without having access to the source ?".

Over to you Howard <G>

Jimmy
```

###### ↳ ↳ ↳ Re: How to hide cobol code

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-23T12:40:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<070Z6.77$UQ2.37774@dfiatx1-snr1.gtei.net>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net> <3B33C04E.3D98E80D@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:3B33C04E.3D98E80D@home.com...
> "William M. Klein" wrote:
>
> > If the thing that you want to "secure" is actually procedural code, then
I
> > would suggest that you put it into a separate "callable" module that
simply
> > has a "documented" interface.  (Or better yet, start thinking about OO
COBOL
> > and "encapsulation"). In this way, all the "others" would need was
access
> > to your "load module" - and would never see the code involved.
>
> Well Bill - that's real neat. You've actually found an excuse for using OO
with
> a mainframe <G>. I can just see Howard running up one wall, across the
ceiling
> and down the other wall. "Encapsulation ?", he says. "You've got to be
kidding.
> How the hell can I test my modules without having access to the source ?".
>
>
If you want to use this an excuse to introduce OO programming, you'll have
to contend with us proecedural dinosaurs, who will point out you don't need
'OO' to use a separate 'callable' module.

MCM
```

###### ↳ ↳ ↳ Re: How to hide cobol code

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-06-25T00:36:31+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B36170F.3080506@iinet.net.au>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net> <3B33C04E.3D98E80D@home.com>`

```
James J. Gavan wrote:

> 
> "William M. Klein" wrote:
…[13 more quoted lines elided]…
> 
Oh Balderdash!


You could do that without OO with just about any language.

OO is just a more formalised way of doing it. AND a callable module is NOT a 
major reason for OO on the mainframe. There are much better reasons as Peter 
Dashwood would point out that have to do with interfaces.
```

###### ↳ ↳ ↳ Re: How to hide cobol code

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-25T14:23:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b36a01e_2@Usenet.com>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net> <3B33C04E.3D98E80D@home.com> <3B36170F.3080506@iinet.net.au>`

```
"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
news:3B36170F.3080506@iinet.net.au...

> Oh Balderdash!

I understand your frustration, Joe.

There are a number of misconceptions (on both sides of the fence -
mainframers misinterpreting what OO is and what it is good for, and OO
people who don't really understand the mainframe environment...I'm not
suggesting this is the case for EVERYONE; there are others who have a very
good understanding of both sides.)

This is all pretty normal as a "new technology" emerges...

> You could do that without OO with just about any language.
>
> OO is just a more formalised way of doing it. AND a callable module is NOT
a
> major reason for OO on the mainframe. There are much better reasons as
Peter
> Dashwood would point out that have to do with interfaces.
>
Agreed.

I'm reproducing my response to some OO questions asked in another thread,
which may have been missed, and which deals with the similarities between
callable Mainframe modules and OO.

In response to Clark F. Morris.... I wrote:

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3B328EF5.707E3593@istar.ca...
> The COBOL dynamic call on the mainframe has exactly the same drawbacks
> of immediately changing for all invokers of a given called module when
…[4 more quoted lines elided]…
>
Don't confuse dynamic mainframe calls with instantiating Objects via a
constructor method. There is no comparison. The OO Factory method is already
loaded in memory and churns out instances of data when it is requested to
(via "NEW"). When Object methods are invoked they are applied to this
instance data, via the Object Reference which was returned from the
instantiation. Logically, the process can be visualised as similar to
dynamically loading a module, but that is where the similarity ends.
Physically the processes are quite dissimilar.

>>>
> 1.  What is the overhead of having separately loaded modules and does it
> matter for the target environment?  There is a measurable overhead but
> it is trivial for the applications that I have seen.
>
<<<
That isn't how it works... see above.

>>>
> 2.  How do we know that we have the sub-routine (object, etc.) and how
…[4 more quoted lines elided]…
>
<<<
When it is instantiated it returns an Object Reference to itself. If you
instantiate again you get another instance and another Object Reference. You
know "what it does" from its documented Methods and Properties. Hence you
access the Properties via the same Object Reference as you access the Object
Methods. It is like a Universal Pointer to ONE PARTICULAR instance of the
Object. There is nothing to stop you having an array of Object References
which all represent the same CLASS of Object. However, each one will
represent a different instance of it. Imagine a litho plate which prints a
picture; each print is numbered, but they are all identical. If you want to
mark one of the pictures you refer to it by its number. It is exactly the
same principle.

>>>
> 3.  Because of perceived greater flexibility in some ways, will there be
> more checking and conversion done at the inter-module boundary?
>
<<<
Yes. The new OO COBOL standard (grimace) calls for conformance checking at
compile time to ensure that the parameters passed to an Object's methods are
valid for it. (It is similar to the use of Header files in C++). OO COBOL
defines a Repository which enables it to do this checking, but (in my
opinion) a better way is to define Method Prototypes which can be used as
"stubs" while you are developing a system. (I don't know what the Standard
says about this, but it is common practice in other languages and Fujitsu OO
COBOL supports it, so it gets my vote...)

>>>
> 4.  From what I have seen, the general rule is to pass the elements
…[3 more quoted lines elided]…
> the number and weirdness varies by state (and other jurisdictions).
<<<
Well I can't comment on what you've seen, but I can assure you I have
objects which pass "structures" (Group Properties, if you like) when this is
desirable. If you wanted to make such Properties individually available as
Public Properties, you would need to define them as Public Properties and
set them within the Factory Method by moving elements of the passed
structure to the individual fields. (I don't do that, but it is quite
feasible and avoids the need to make every Property a separate parameter.)

You may have seen this process arise because of some misunderstandings
regarding the nature of COM objects. Many people believe that for a COM
object, every property must be defined and requires a GET or SET Method.
This rules out the passing of structures. However, this belief is fallacious
and I have COM components which pass structures as COM type VT_STRING and
work fine.

So to answer your question, what you have seen is not "wrong" but it is
unnecessary. A "large number of elements such as state tax calculations
where the number and weirdness varies by state (and other jurisdictions)"
could be passed as an array of type "String".

From the theoretical point of view it would be better if the Object went and
fetched them off a database or from a Collection; or maybe a "collector"
object could be invoked, depending on the jurisdiction, and then pass what
it collected as an array to the actual calculation module. This has to do
with encapsulation and visibility of data to processes which don't require
it.

Hope this helps,

Pete.





Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: How to hide cobol code

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-25T05:52:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B36D14D.F40E9BCE@home.com>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net> <3B33C04E.3D98E80D@home.com> <3B36170F.3080506@iinet.net.au>`

```


Joseph J Katnic wrote:

> James J. Gavan wrote:
>
…[23 more quoted lines elided]…
>

Joke Joe, joke <G>

Jimmy
```

###### ↳ ↳ ↳ Re: How to hide cobol code

_(reply depth: 5)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-06-25T23:42:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B375BF8.2070601@iinet.net.au>`
- **References:** `<3B33B050.78A8609B@cais.com> <9h0ctv$3cd$1@nntp9.atl.mindspring.net> <3B33C04E.3D98E80D@home.com> <3B36170F.3080506@iinet.net.au> <3B36D14D.F40E9BCE@home.com>`

```
James J. Gavan wrote:

> 
> Joke Joe, joke <G>
> 
> Jimmy
OOPs - it must be too late at night down here in OZ. I completely missed that one!
```

#### ↳ Re: How to hide cobol code

- **From:** Ron Bell <ronbell@cais.com>
- **Date:** 2001-06-25T20:18:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h8k92$2i4a$1@allthetime.news.cais.net>`
- **References:** `<3B33B050.78A8609B@cais.com>`

```
Ron Bell wrote:

> William M. Klein" wrote:
>> 
…[24 more quoted lines elided]…
> 
The *CBL NOSOURCE statement works great!  Thanks for everyone's help, my 
listing dropped from 25K lines of code to 7K lines.  Thanks again,
Ron Bell
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
