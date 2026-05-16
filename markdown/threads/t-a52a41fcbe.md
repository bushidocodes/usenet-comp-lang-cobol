[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# .NET Programming or Teaching an Old Dinosaur New Tricks

_9 messages · 6 participants · 2002-01 → 2002-02_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future) · [`Tutorials, books, learning`](../topics.md#learning)

---

### .NET Programming or Teaching an Old Dinosaur New Tricks

- **From:** "Lee Unterreiner" <flu@nospam.flu-ent.com>
- **Date:** 2002-01-24T17:31:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2qcih$2r5$1@slb6.atl.mindspring.net>`

```
For those interested in this exciting new environment:

.NET introduces a number of new terms and concepts.  Even with a solid
knowledge of OO programming, you can get lost VERY quickly if you lack the
proper foundation.  I recently completed "Bertrand Meyer's .NET Training
Course".  It's a video training course on 3 CD's along with a workbook.  You
can order it at Amazon for about $50.  I STRONGLY recommend it to all.
```

#### ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-25T03:09:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C50CD5B.520649A9@shaw.ca>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net>`

```


Lee Unterreiner wrote:

> For those interested in this exciting new environment:
>
…[4 more quoted lines elided]…
> can order it at Amazon for about $50.  I STRONGLY recommend it to all.

"Even with a solid knowledge of OO programming, you can get lost VERY quickly
..........", and you aren't exactly a beginner, are you ?

So Lee, having put ".Net" aside, rather like many of us did with Windows,
(sticking with DOS until we 'had to'), what exactly is involved. I'm vague, so
some questions :-

    - is this .Net process like learning Windowing from scratch
    - you are of course using the Fujitsu new 'scripting' feature, (and I
believe,
        Net Express does provide something similar to get into .Net)
    -  what are the major things that really hit you as "pluses" when you use
.Net
    - Can you quickly summarize the advantages of .Net
    - How long can one ignore .Net,  (before you 'have to')
    - There's a price tag, (Microsoft)  for the .Net feature ?????? - and which
        Windows OS does it work with

Jimmy, Calgary AB
```

##### ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

- **From:** "Lee Unterreiner" <flu@nospam.flu-ent.com>
- **Date:** 2002-01-25T00:14:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2rce6$7c7$1@slb6.atl.mindspring.net>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca>`

```
I like to compare .NET to the Java Virtual Machine (JVM).  JVM is a
multi-platform/single language (Java) programming environment.  .NET is a
single platform/multi-language environment.  The single platform is Windows
XP/2000/CE for now.  .NET applications are always compiled to native code -
with JVM its optional.

>     - is this .Net process like learning Windowing from scratch

In many ways, yes.  It's really an OO layer on top of the OS.  No more
API's.  Everything is a method, property, or class.

>     - you are of course using the Fujitsu new 'scripting' feature, (and I
> believe,
>         Net Express does provide something similar to get into .Net)

No, I was not referring to Fujitsu's .NET offering in particular but to the
platform in general.  Many language vendors have 'ported' their compilers to
this new platform.  In addition, Microsoft allows for optional integration
into their Visual Studio (VS).  The only announced COBOL port (so far) is
from Fujitsu - they are also doing VS integration..  Interoperabilty with
.NET is easy and builtin, but you get virtually none of the benefits of .NET
unless the compiler vendor does a specific port to .NET.

Disclaimer:  For those who don't know me, I am an independent consultant
that has at one time or another has done work for most of the COBOL vendors.
Currently, Fujitsu is my biggest customer.  Those who do know me know I
shill for no one.  Much to the consternation of my past and previous
clients, I don't hestitate to recommend a competitor's product if I feel it
would be more appropriate.

>     -  what are the major things that really hit you as "pluses" when you
use
> .Net

1. Traditional, client server, and web server programming  - all in a
single, 'seamless', integrated, type safe environment, with a common set of
tools.
2. True multi-language support and binary transparency.  You can't tell what
language any given component is in, nor do you care.  Its really cool to run
a debug session that switches seamlessly between COBOL, C#, VB, Eiffel, etc.
3. Security to protect you from the outside world and vice versa.
4. Seamless components. Gone are COM and ActiveX.  .NET classes ARE
components.  Components are 'smart' objects. The runtime can do dynamic
binding - the debugger can interrogate them - the source code editor can
prevent coding mistakes - the IDE lets you 'drop' them on to forms.
5. Seamless communications. SOAP and XML are the protocols used.
6. The end of DLL hell.  The ONLY installer one needs is FTP or XCOPY.

I can't do this topic justice - thats why I recommend Meyer's course.

>     - Can you quickly summarize the advantages of .Net
>     - How long can one ignore .Net,  (before you 'have to')
>     - There's a price tag, (Microsoft)  for the .Net feature ?????? - and
which
>         Windows OS does it work with


The end user platform is free.  Its builtin to XP and beyond.  Its available
for 2000 and CE.  Yes, your favorite COBOL application running on a
hand-held or even a phone!

The development environment does not run on 9x.

The cheapest Visual Studio products (VB, C#, C++) from Microsoft are about
$100 US.    I have know idea of what any other language vendors are asking -
visit their websites.

As long as where you are is OK you can ignore .NET.  This is not a
replacement for Windows.  It's a programming model that sits on top of
Windows.  Microsoft no longer contain native code generators.  That function
is now performed by the Framework (on the end user's machine) .

Hope this gets you interested.

Lee
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-25T18:38:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C51A76B.24B4EA0D@shaw.ca>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net>`

```


Lee Unterreiner wrote:

> I like to compare .NET to the Java Virtual Machine (JVM).  JVM is a
> multi-platform/single language (Java) programming environment.  .NET is a
> single platform/multi-language environment.  The single platform is Windows
> XP/2000/CE for now.  .NET applications are always compiled to native code -
> with JVM its optional. <snip>,,,,,,

Thanks Lee,

Your reply was concise and informative.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-26T08:33:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C5269F5.BE5FB58B@Azonic.co.nz>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net>`

```
Lee Unterreiner wrote:
> 
> I like to compare .NET to the Java Virtual Machine (JVM). JVM is a
> multi-platform/single language (Java) programming environment.  

Not entirely true, for example JPython is Python that runs on the JVM.

> .NET is a single platform/multi-language environment.  

.NET is quite a bit more than just the run-time system.  It is primarily
a set of internet services which MS hope to charge for on a subscription
basis to supplement their current revenue model.

> The single platform is Windows XP/2000/CE for now.  .NET applications 
> are always compiled to native code - with JVM its optional.

Which may or may be advantageous.  It means that every handheld or
embedded device must have the compiler as well as the run-time, and must
cater for what all the languages may do for that device.  This is why
20Gb + 512Mb + 1MHz are no faster in doing actual work than a 486 in
1995.

As a comparison a subset Java, WABI, for the Palm runs with a 50Kb
interpreter.

> 3. Security to protect you from the outside world and vice versa.

That has yet to be demonstrated.  

> 4. Seamless components. Gone are COM and ActiveX.  

Are they 'gone' or just disguised by yet another layer of interfacing ? 
This has serious security (ActiveX are not secure) and performance
issues.

> 6. The end of DLL hell.  The ONLY installer one needs is FTP or XCOPY.

Only because they have a completely new set of .DLLs that replicate the
functions of the existing ones and both sets must be on the machine
leading to a bloat of many tens or hundreds of megabytes on disk and in
memory.

> The end user platform is free.  Its builtin to XP and beyond.  Its available
> for 2000 and CE.  Yes, your favorite COBOL application running on a
> hand-held or even a phone!

The services that will link the end-users and servers, will however, not
be free.
 
> The development environment does not run on 9x.

I doubt that there is any technical reason for this, it is just that MS
wants everyone to buy XP (see 'Revenue model').
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

_(reply depth: 4)_

- **From:** Gary Scott <scottg@flash.net>
- **Date:** 2002-01-26T00:33:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C51FA28.79F09C73@flash.net>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net> <3C5269F5.BE5FB58B@Azonic.co.nz>`

```
I've heard of some installing a recent version on Win98 with no
problems.

Richard Plinston wrote:
> 
> Lee Unterreiner wrote:
…[51 more quoted lines elided]…
> wants everyone to buy XP (see 'Revenue model').
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

_(reply depth: 4)_

- **From:** "Lee Unterreiner" <flu@nospam.flu-ent.com>
- **Date:** 2002-01-25T16:48:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2suel$hvu$1@nntp9.atl.mindspring.net>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net> <3C5269F5.BE5FB58B@Azonic.co.nz>`

```

"Richard Plinston  wrote:
> >
> > I like to compare .NET to the Java Virtual Machine (JVM). JVM is a
> > multi-platform/single language (Java) programming environment.
>
> Not entirely true, for example JPython is Python that runs on the JVM.

Agreed.  There are even COBOL to Java compilers

>
> > .NET is a single platform/multi-language environment.
…[3 more quoted lines elided]…
> basis to supplement their current revenue model.

I don't know which services you are refering to.  Are they content
providers?  The services I am talking about areWeb Services (ASP+
essentially), Data Services (ADO+), WebForms, and WinForms.  These services
are integral to what MS calls the .NET Framework.  No connection to MS is
required.


>
> > The single platform is Windows XP/2000/CE for now.  .NET applications
…[7 more quoted lines elided]…
>

All .NET languages compile what MS calls CLS or common language
specification.  The Framework for each platform come with one or more JITs
(just in time compilers).  The JITTER (I'm not making these terms up) for a
handheld device will have different properties than one used on a web
server.

I can't speak to your other points.  I don't even own a laptop. I like my
computers big (raised floor is optional).

> As a comparison a subset Java, WABI, for the Palm runs with a 50Kb
> interpreter.
…[3 more quoted lines elided]…
> That has yet to be demonstrated.

Granted.

>
> > 4. Seamless components. Gone are COM and ActiveX.
…[4 more quoted lines elided]…
>

Yes they are truly gone - although there is interoperability.  They are gone
because ALL non-abstract classes ARE components.  This is transparent to the
class writer.  The compiler generates CLS code plus Metadata (an XML based
IDL).  After it is 'compiled' to Metadata and CLS it is impossible to tell
what the original language was without a debugger.

It is the idea of 'instant components' that has me most excited.  Components
are 'smart' classes.  Within Visual Studio they can be used immediately to
enhance;the Forms designers and tool boxes; the editor prompts for the
correct usage when referencing the class, the debugger and the runtime can
dynamically resolve references without requiring registration

> > 6. The end of DLL hell.  The ONLY installer one needs is FTP or XCOPY.
>
…[3 more quoted lines elided]…
> memory.

I have no idea what the requirements are.  Also a second disclaimer: I am
not a fan of Microsoft in the same way I was not a fan of IBM in an earlier
era. But they are ubitiquous and I am a pragmatist.  Since all new computers
with an MS OS now come with it, I assume the hard disks can handle it.

>
> > The end user platform is free.  Its builtin to XP and beyond.  Its
available
> > for 2000 and CE.  Yes, your favorite COBOL application running on a
> > hand-held or even a phone!
>
> The services that will link the end-users and servers, will however, not
> be free.

Connectivity to content providers or to ISP may be chargeable.  But that
would be application specific.  Nothing in .NET Framework has anything
(inherently) to do with for-fee services.  You do not have to go through MS
or any of its cronies to use any of the features I've described.

>
> > The development environment does not run on 9x.
>
> I doubt that there is any technical reason for this, it is just that MS
> wants everyone to buy XP (see 'Revenue model').

You are probably right about the XP revenue model - Office will soon follow
suit.  But .NET is simply a programming model meant to make life easier for
those coding for MS platforms - and one that's open and available to COBOL
programmers.
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-01-26T08:19:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0201260819.25e24571@posting.google.com>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net> <3C5269F5.BE5FB58B@Azonic.co.nz> <a2suel$hvu$1@nntp9.atl.mindspring.net>`

```
One thing about the framework is very interesting to me.  One may - if
one chooses - invoke a method of a class, using it just like any other
method - and not only can be in created in some other language - it
might actually be a component that is running on a server in some
other country.

"Lee Unterreiner" <flu@nospam.flu-ent.com> wrote in message news:<a2suel$hvu$1@nntp9.atl.mindspring.net>...
> "Richard Plinston  wrote:
> > >
…[105 more quoted lines elided]…
> programmers.
```

###### ↳ ↳ ↳ Re: .NET Programming or Teaching an Old Dinosaur New Tricks

_(reply depth: 4)_

- **From:** "Guenter Tschech" <Guenter.Tschech@nospam.newline-software.net>
- **Date:** 2002-02-18T10:29:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4qh33$vb1$1@news1.transmedia.de>`
- **References:** `<a2qcih$2r5$1@slb6.atl.mindspring.net> <3C50CD5B.520649A9@shaw.ca> <a2rce6$7c7$1@slb6.atl.mindspring.net> <3C5269F5.BE5FB58B@Azonic.co.nz>`

```

Richard Plinston wrote:
> Lee Unterreiner wrote:
> >
…[9 more quoted lines elided]…
> basis to supplement their current revenue model.

.NET before everything else is a brand for "Microsoft in the new internet
age".
It applies to
* The Runtime (CLR), which indeed runs on multi-platform
* the .NET Servers, which are the well-known (both good and bad) MS server
products
* the Web Service architecture, which now is a standard served by IBM, SUN,
SAP and others (at least with words :)

You can of course work with .NET without using the internet at all; in my
eyes the great thing about it is
that you can write a COBOL program and deploy it using standard Internet
Browsers into your whole
company, so there is only ONE runtime for all programs, regardless of
language (as long as they support the CLR)
>
> > The single platform is Windows XP/2000/CE for now.  .NET applications
…[9 more quoted lines elided]…
>
This is true, but you can precompile your apps so no compiler will be
invoked when
the thing is copied to your device. This naturally limits the
platform-independence of
.NET, so you a re supposed to do this with care.
But .NET is designed with a JIT in mind, while java is not, so the java JIT
has a lot more
problems to solve than its .NET counterpart, so it's not a surprise that
.NET apps run
much faster than java compiled programs...
>
> > 3. Security to protect you from the outside world and vice versa.
>
> That has yet to be demonstrated.

It is demonstrated by the release of VisualStudio.NET, which is so secure
you cannot
even run your own app if it is run from a network share... (before you open
the security again)
the main problem here is that security is far too complex for the normal end
user
(and I's say even the normal programmer), so unsafe programs will arise
regardless of language...

>
> > 4. Seamless components. Gone are COM and ActiveX.
…[4 more quoted lines elided]…
>
When you follow MS, ActiveX is really! gone, for the CLR of .NET includes
features that
make ActiveX obsolete. With COM, it depends on your architecture. Using
plain .NET,
you don't need COM, either, but you'll find a lot of mixed environments (who
knows better
than COBOL programmers, that written code outlives any new technique...)

> > 6. The end of DLL hell.  The ONLY installer one needs is FTP or XCOPY.
>
…[4 more quoted lines elided]…
>
The .NET concept of "the end of DLL hell" is nothing new, it's just the
revival of
UNIX patterns that are known for a long time, so don't complain, the best
survives :-)

> > The end user platform is free.  Its builtin to XP and beyond.  Its
available
> > for 2000 and CE.  Yes, your favorite COBOL application running on a
> > hand-held or even a phone!
>
> The services that will link the end-users and servers, will however, not
> be free.

but again, .NET is not only about services, it's only the real NEW thing
that the
marketing people have understood (have you tried to explain technical
details of an
operating system to your marketing  staff ?)

> > The development environment does not run on 9x.
>
> I doubt that there is any technical reason for this, it is just that MS
> wants everyone to buy XP (see 'Revenue model').

There is technical reason for this: XP and NT is the same operating kernel
(XP is Windows NT 5.1),
whereas win98/winme sits on top of old DOS code.
But you can deploy .NET apps to Win98, and�be honest: would you like to
develop on a machine
where every program crashes the whole machine ?

- just my humble 2 cents (well, we do have cents in germany too, now :-)

Guenter <><
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
