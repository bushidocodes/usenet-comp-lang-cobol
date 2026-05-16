[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Develop Java class for COBOL/CICS

_11 messages · 5 participants · 2007-01_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Develop Java class for COBOL/CICS

- **From:** kenneykirk@gmail.com
- **Date:** 2007-01-03T13:37:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com>`

```
Is the any special rules required i.e. method signatures, imports or
objects required to Invoke a method on a java class under CICS.  Where
trying to add an interface from an existing CICS app to one of our LAN
based systems.  I have information on what the COBOL program must do
but not what the java class must implement in order to handle an
invocation from COBOL/CICS.  Any sample code would be greatly
appreciated.  We are using the laster CICS transction server.
```

#### ↳ Re: Develop Java class for COBOL/CICS

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-04T01:53:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enhmne$2u3$1@reader2.panix.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com>`

```
In article <1167860259.664125.99040@i12g2000cwa.googlegroups.com>,
 <kenneykirk@gmail.com> wrote:
>Is the any special rules required i.e. method signatures, imports or
>objects required to Invoke a method on a java class under CICS.

No special rules at all... just the usual one of 'hire someone who knows 
what they are doing, send someone you already have hired to a training 
class or deal with the results of having done neither.'

DD
```

##### ↳ ↳ Re: Develop Java class for COBOL/CICS

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-01-04T08:48:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <enhmne$2u3$1@reader2.panix.com>`

```
On Thu, 4 Jan 2007 01:53:50 +0000 (UTC), docdwarf@panix.com () wrote:

>No special rules at all... just the usual one of 'hire someone who knows 
>what they are doing, send someone you already have hired to a training 
>class or deal with the results of having done neither.'

But those are the choices that seem to be unacceptable to management.
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-04T18:41:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enjhod$1h5$1@reader2.panix.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <enhmne$2u3$1@reader2.panix.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>`

```
In article <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 4 Jan 2007 01:53:50 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
>But those are the choices that seem to be unacceptable to management.

Well, maybe that's because 'unacceptable' is not being used rigorously, or 
it's being used loosely... or maybe 'unacceptable' is, theoretically, 
acceptable... or maybe I just don't have the Big Picture.

DD
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-05T11:13:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<505cfsF1e20p8U1@mid.individual.net>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <enhmne$2u3$1@reader2.panix.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com> <enjhod$1h5$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:enjhod$1h5$1@reader2.panix.com...
> In article <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[13 more quoted lines elided]…
>

Or maybe you are just in dire need of a break and all of the above are true 
:-)?

Maybe there would be no universe without maybes. A number of physicists 
probably thought so, at least if history can be believed, which of course, 
it can't...:-)

'Nother beautiful day here, impossible to be unhappy. I'm driving for an 
hour and a quarter, in an open car, through idyllic scenery to an unspoilt 
Pacific beach to meet up with friends and enjoy the day and evening. The 
problems of COIs, CLC, and  even my current back-burner project seem 
irrelevant...

It is amazing how sunshine, good food, good company, and good wine, can 
change one's perspective...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-05T02:12:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enkc6c$9em$1@reader2.panix.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com> <enjhod$1h5$1@reader2.panix.com> <505cfsF1e20p8U1@mid.individual.net>`

```
In article <505cfsF1e20p8U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:enjhod$1h5$1@reader2.panix.com...
…[15 more quoted lines elided]…
>:-)?

That possibility has not been ruled out, Mr Dashwood... but neither my 
client nor I determined that the quality of my work has yet to be reduced 
by that need and so I continue to Do My Job, satisfying my client's 
requests.

[snip]

>It is amazing how sunshine, good food, good company, and good wine, can 
>change one's perspective...:-)

Likewise, Mr Dashwood, it might be equally amazing how having a job, 
satisfying a client and seeing your work make life easier for others can 
change one's perspective... now, if you'll excuse me, I have a job to do.

DD
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-06T02:40:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5072q2F1f1vmrU1@mid.individual.net>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com> <enjhod$1h5$1@reader2.panix.com> <505cfsF1e20p8U1@mid.individual.net> <enkc6c$9em$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:enkc6c$9em$1@reader2.panix.com...
> In article <505cfsF1e20p8U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[26 more quoted lines elided]…
> requests.

Sounds like the oldest profession in the world...  What's the money like? 
:-)


>
> [snip]
…[6 more quoted lines elided]…
> change one's perspective... now, if you'll excuse me, I have a job to do.

OK, but remember, no tongues... (unless they're  REALLY cute, of 
course...:-))

Pete.
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-05T14:28:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enlnak$4nt$1@reader2.panix.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <505cfsF1e20p8U1@mid.individual.net> <enkc6c$9em$1@reader2.panix.com> <5072q2F1f1vmrU1@mid.individual.net>`

```
In article <5072q2F1f1vmrU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:enkc6c$9em$1@reader2.panix.com...
…[31 more quoted lines elided]…
>:-)

Such 'sounds' might be deceptive, Mr Dashwood... after all, surgery might 
sound like assault in that both can involve sticking a knife into someone.  
As I am paid in US dollars the money's, like, green with pictures of dead 
Presidents on it.

>> [snip]
>>
…[8 more quoted lines elided]…
>course...:-))

I'll leave glossolalia for those inclined to it, then.

DD
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-06T11:33:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50821rF1epis5U1@mid.individual.net>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <505cfsF1e20p8U1@mid.individual.net> <enkc6c$9em$1@reader2.panix.com> <5072q2F1f1vmrU1@mid.individual.net> <enlnak$4nt$1@reader2.panix.com>`

```
LOL! Good stuff, Doc.:-)

Thanks for adding a new word to my vocabulary...

Guess I need to watch my tongue....

Pete.

TOP POST - no more below

<docdwarf@panix.com> wrote in message news:enlnak$4nt$1@reader2.panix.com...
> In article <5072q2F1f1vmrU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[60 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-05T11:02:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<505brdF1dvlkcU1@mid.individual.net>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <enhmne$2u3$1@reader2.panix.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com...
> On Thu, 4 Jan 2007 01:53:50 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
> But those are the choices that seem to be unacceptable to management.

If you can get someone to give you free advice, why would you pay for it?

It is one thing to help people who are making an effort to learn programming 
or whatever, it is quite another to provide key business support for 
nothing.

I was very tempted to respond to this mail when I first saw it but I decided 
to follow Doc's example and practise restraint....:-)

The OP should advise his/her COI that some professional support may be 
required to solve this problem.

Until people start doing that the 'unacceptable' choice won't become 
'acceptable'.

Pete.

(Who isn't grumpy or mean-spirited, and likes to help, but knows where the 
line is...)
```

###### ↳ ↳ ↳ Re: Develop Java class for COBOL/CICS

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-01-04T19:17:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6ee9$459da705$454920f8$21935@KNOLOGY.NET>`
- **In-Reply-To:** `<td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>`
- **References:** `<1167860259.664125.99040@i12g2000cwa.googlegroups.com> <enhmne$2u3$1@reader2.panix.com> <td8qp2l580q83v5nbse300nb5ceghq96eb@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 4 Jan 2007 01:53:50 +0000 (UTC), docdwarf@panix.com () wrote:
> 
…[4 more quoted lines elided]…
> But those are the choices that seem to be unacceptable to management.

Then, by default, they've selected the third choice, no?  :)  (I don't 
think that the answer above was particularly helpful - although those 
who know DD know that this was his way of warning them that one had 
better know what one is doing...)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
