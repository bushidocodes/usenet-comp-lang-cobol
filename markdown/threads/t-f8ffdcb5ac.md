[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT Java, C#, C++

_14 messages · 7 participants · 2008-01_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT Java, C#, C++

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-01-11T20:07:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I%Phj.255354$He.247582@fe08.news.easynews.com>`

```
Although still off-topic, I was just wondering, ...

In the threads on Java, it seems to me that some of those embracing OO are 
moving from Java to C# (not C++).

I know that the CLI run-time (I think that is what is still called outside 
Microsoft) is available on other platforms, but I was wondering how "portable" 
those using C# is in practice.

Are those using C# mostly doing Windows applications?

If you wanted to do OO for a "portable to where CLI isn't" environment, would 
you use Java or C++ - or something else (and why)?

Just curious.
```

#### ↳ Re: OT Java, C#, C++

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-12T13:01:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5uqebmF1j2oi5U1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:I%Phj.255354$He.247582@fe08.news.easynews.com...
> Although still off-topic, I was just wondering, ...
>
…[7 more quoted lines elided]…
> Are those using C# mostly doing Windows applications?

Speaking for myself, "Yes". (Its where the market is...)
>
> If you wanted to do OO for a "portable to where CLI isn't" environment, 
> would you use Java or C++ - or something else (and why)?

Possibly Java, but more likely C#. It has arguably better facilities than 
Java (although this is subjective; both languages are excellent), but I 
specifically like certain features of C# (better IDE and Debugging, FOREACH 
for iterating over collections... SO easy, and very easy-to-write event 
handlers. Mainly, I like the succinct, easy-to-read code and the fact that 
everything is typed. Stuff (even complex machine oriented stuff) just 
works...

If the User had Java already, and/or expressed a preference for NO C#, then 
I'd use Java.
>
> Just curious.
>

Based on a sample of one :-) written totally as an experiment, but a real 
application...:

1. C# developed on a Windows platform and NOT using unmanaged code 
(specifically, InterOp Services) or platform-specific Classes, runs 
perfectly on any Windows platform running the appropriate version of DotNET.

2. The SAME C# Assembly runs correctly on a machine running Mono/Linux, 
WITHOUT recompile or reconfiguring.

C# is accelerating in popularity for a number of reasons, and cross-platform 
capability is just one aspect of it.

I only wish I had got into it sooner; I could have saved myself a lot of 
aggravation with OO COBOL.

Pete.
```

##### ↳ ↳ Re: OT Java, C#, C++

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2008-01-11T19:18:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U8idnbEUQcjsvhXanZ2dnUVZ_q2hnZ2d@comcast.com>`
- **In-Reply-To:** `<5uqebmF1j2oi5U1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net>`

```
Pete Dashwood wrote:
>, but I 
> specifically like certain features of C# (better IDE and Debugging, FOREACH 
> for iterating over collections... SO easy,

You know that the latter is pretty easy in Java too, right?  :)

for (SomeObject oObj : oObjCollection) {
     // do something with the object
}

or

Iterator<ObjectType> iterObj = ObjectType.Iterator();

while (iterObj.hasNext()) {
     ObjectType oObj = iterObj.next();
     // do something with the object
}

Of course, the "for" is much less code.
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-14T02:12:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5uuh1vF1jo9n8U1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <U8idnbEUQcjsvhXanZ2dnUVZ_q2hnZ2d@comcast.com>`

```


"LX-i" <lxi0007@netscape.net> wrote in message 
news:U8idnbEUQcjsvhXanZ2dnUVZ_q2hnZ2d@comcast.com...
> Pete Dashwood wrote:
>>, but I specifically like certain features of C# (better IDE and 
…[3 more quoted lines elided]…
>
Yes :-)

But C#  FOREACH has more elegance...

(You CAN use the same "iterator" (enumerator) approach in C#, but I still 
prefer FOREACH.)

Pete.
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2008-01-13T10:21:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oUqij.51733$_m.37436@bignews4.bellsouth.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <U8idnbEUQcjsvhXanZ2dnUVZ_q2hnZ2d@comcast.com> <5uuh1vF1jo9n8U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
> "LX-i" <lxi0007@netscape.net> wrote:
>> Pete Dashwood wrote:
…[8 more quoted lines elided]…
> (You CAN use the same "iterator" (enumerator) approach in C#, but I still prefer FOREACH.)

Do you see some difference between FOR EACH as implemented in C#
vs. VB?
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-14T10:23:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5uvdr6F1k457aU1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <U8idnbEUQcjsvhXanZ2dnUVZ_q2hnZ2d@comcast.com> <5uuh1vF1jo9n8U1@mid.individual.net> <oUqij.51733$_m.37436@bignews4.bellsouth.net>`

```


"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:oUqij.51733$_m.37436@bignews4.bellsouth.net...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>> "LX-i" <lxi0007@netscape.net> wrote:
…[14 more quoted lines elided]…
> vs. VB?

I think Anders probably realized that VB's "for each" is a very useful 
construct and included it in C# as a kind of high level "collection 
processor".

To answer your question, no, I see very little difference, but I'm not 
expert with VB. Certainly in C# automatic enumeration happens under the 
covers (as it probably does with VB). I like the syntax in C#.:-)

Pete.
```

##### ↳ ↳ Re: OT Java, C#, C++

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-01-11T21:19:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13og8tha2ue6n21@corp.supernews.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5uqebmF1j2oi5U1@mid.individual.net...
>
>
…[53 more quoted lines elided]…
>

Java has a similar idion for iterating over collections.  I think it came 
with version 5.
```

##### ↳ ↳ Re: OT Java, C#, C++

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-13T16:45:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net>`

```
On Jan 12, 1:01 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "William M. Klein" <wmkl...@nospam.netcom.com> wrote in messagenews:I%Phj.255354$He.247582@fe08.news.easynews.com...
>
…[41 more quoted lines elided]…
> WITHOUT recompile or reconfiguring.

While it is possible to write C# programs that will run identically on
both, it is also possible to write perfectly good programs which are
locked to 'Windows only'.

Partly this is because Mono will always be behind the latest Windows
stuff, but also because Mono doesn't/can't use the Windows API as can
be done.

If, however, one used the GTK+ windowing subsystem then it will run on
both.

> C# is accelerating in popularity for a number of reasons, and cross-platform
> capability is just one aspect of it.

When MS implemented their Java as J++ they added 'Windows Only' stuff
into it and failed to indicate that this was not cross-platform in the
expectation that they could have it both ways: alleged 'cross-
platform' _and_ Windows Only lockin.

Mono is supplying that for MS. In theory cross-platform, in practice
Windows only (unless special care is taken).

> I only wish I had got into it sooner; I could have saved myself a lot of
> aggravation with OO COBOL.
…[3 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-15T09:58:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5v20nqF1junmoU1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com...
> On Jan 12, 1:01 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[81 more quoted lines elided]…
>

I really don't know enough about Mono to argue this, Richard, and I accept 
what you say.

It seems a pity.

Not familiar with GTK+ either. How could I access this from a Windows 
environment in C# (thought I might give it a try...)?

Pete.
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 4)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-14T13:56:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9a8941c-9c19-44fe-9583-5bd3316405dd@i7g2000prf.googlegroups.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com> <5v20nqF1junmoU1@mid.individual.net>`

```
On Jan 15, 9:58 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Richard" <rip...@azonic.co.nz> wrote in message
>
…[90 more quoted lines elided]…
> environment in C# (thought I might give it a try...)?

http://www.mono-project.com/GtkSharp

I notice that it also supports the Glade interface designer. I use
Glade for python programs.
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 4)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-14T14:10:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83d2deaa-8d27-48d2-987e-ff53596b79f2@e6g2000prf.googlegroups.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com> <5v20nqF1junmoU1@mid.individual.net>`

```
On Jan 15, 9:58 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Richard" <rip...@azonic.co.nz> wrote in message
>
…[85 more quoted lines elided]…
> what you say.

> It seems a pity.

"""Support for Winforms 1.1 has been completed and was released in
Mono 1.2. It is now in a maintenance/bug fixing state. Support for
Winforms 2.0 is currently under development."""

"""some applications (and especially third party controls)
occasionally bypass the API and P/Invoke straight to the Win32 API.
These calls will likely have to changed to work on Mono."""



> Not familiar with GTK+ either. How could I access this from a Windows
> environment in C# (thought I might give it a try...)?
…[3 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-15T11:43:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5v26smF1k0vh7U1@mid.individual.net>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com> <5v20nqF1junmoU1@mid.individual.net> <83d2deaa-8d27-48d2-987e-ff53596b79f2@e6g2000prf.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:83d2deaa-8d27-48d2-987e-ff53596b79f2@e6g2000prf.googlegroups.com...
> On Jan 15, 9:58 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[107 more quoted lines elided]…
>

I decided some time ago NOT to use P/Invoke unless there was an absolutely 
compelling reason (so far I haven't found one...)

>
>
>> Not familiar with GTK+ either. How could I access this from a Windows
>> environment in C# (thought I might give it a try...)?
>>

Thanks for the link. I'll check it out and have a dabble as soon as I clear 
the current workload.

Pete.
```

###### ↳ ↳ ↳ Re: OT Java, C#, C++

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-15T08:48:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5blpo356mdk394ndj9nv6ttq1l454uvnop@4ax.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com> <5uqebmF1j2oi5U1@mid.individual.net> <c870ef8d-4cd4-4f97-a757-fa706a81aaa4@l32g2000hse.googlegroups.com> <5v20nqF1junmoU1@mid.individual.net> <83d2deaa-8d27-48d2-987e-ff53596b79f2@e6g2000prf.googlegroups.com> <5v26smF1k0vh7U1@mid.individual.net>`

```
There are other programming technologies that I'd like to see
emphasized more - for instance table driven programming has the
potential to be very useful as we separate data from logic from
display.

Is there an OO APL available?
```

#### ↳ Re: OT Java, C#, C++

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2008-01-11T18:57:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aaydncd-AK4TgxXanZ2dnUVZ_qSonZ2d@comcast.com>`
- **In-Reply-To:** `<I%Phj.255354$He.247582@fe08.news.easynews.com>`
- **References:** `<I%Phj.255354$He.247582@fe08.news.easynews.com>`

```
William M. Klein wrote:
> Although still off-topic, I was just wondering, ...
> 
> In the threads on Java, it seems to me that some of those embracing OO are 
> moving from Java to C# (not C++).

But of course!  :)  (heh - I say that, but in my current job, we're 100% 
Java.  I had to write a batch job to run on a Windows server, so I wrote 
it in J#.)

> I know that the CLI run-time (I think that is what is still called outside 
> Microsoft) is available on other platforms, but I was wondering how "portable" 
> those using C# is in practice.

I have tried to do some development on Linux (a web application), but I 
couldn't get it to work.  Granted, this was a while back, and I haven't 
tried it since.  I believe that Pete has someone using one of his 
assemblies (that's the name for a .NET package) under Mono, the .NET 
runtime for *nix.

> If you wanted to do OO for a "portable to where CLI isn't" environment, would 
> you use Java or C++ - or something else (and why)?

I'd use Java.  It handles memory management itself, and the JVM converts 
types that aren't supported natively.  Oh yeah, one other reason - NO 
POINTERS!  :)  In my experience, C++ isn't portable; and, I've never 
read anything that claimed that it was.

I've mentioned before, I've really been impressed with PHP, especially 
with the enhancements in version 5.  It's fast!  And, anything I do 
outside work is oriented to the web.  It doesn't have to be installed, 
it can be accessed globally, and everyone pretty much already has a 
client.  And, portability then becomes moot as well - you can serve from 
whatever OS to whatever OS, and they all play nicely.

(Of course, economics comes into play here too.  My web host charges an 
extra $2/mo for Java support, and an extra $3/mo for .NET support (but 
only on Windows accounts, which mine is not).  PHP is free.  I asked 
them about Mono on Linux, and they said that they didn't even offer it 
because when they tested it, they couldn't support more than a few sites 
on the equivalent hardware without it really bogging down.  So, I pay my 
$6.95/mo, and use PHP.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
