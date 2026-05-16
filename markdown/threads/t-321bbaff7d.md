[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Efficient timers in Net Express or Object COBOL

_14 messages · 7 participants · 2006-05 → 2006-06_

---

### Efficient timers in Net Express or Object COBOL

- **From:** "eselick" <eselick@gmail.com>
- **Date:** 2006-05-24T07:28:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com>`

```
Hi

I've been looking at the threads here and haven't found a clear answer
to the question:

Is there or is it possible to implement an efficient timer control,
class or algorithim in either of these products?

By efficient I mean something that does not use a hard loop and will
not eat CPU cycles. In most of the Microsoft family of Visual products
visual timer controls are part of the product offering and these seem
to be designed using system api's rather than loops so that overall
performance is not degraded.

Does Micro Focus have anything that's equivalent?

Thanks

Elliot
```

#### ↳ Re: Efficient timers in Net Express or Object COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-24T15:28:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com>`

```
"eselick" <eselick@gmail.com> wrote in message
news:1148480928.355811.205830@y43g2000cwc.googlegroups.com...
> I've been looking at the threads here and haven't found a clear answer
> to the question:
…[10 more quoted lines elided]…
> Does Micro Focus have anything that's equivalent?

If you are on Windows and you feel up to using the Windows' API directly,
the timer objects created by the CreateTimer and CeateWaitableTimer
functions are what the MS-Visual Anything 'native' functions use (see these
functions in your Windows' API reference).

Both utilize the normal thread-switching alogrithms of the Windows Operating
system, essentially checking timer status at the same time it is checking
that another thread may run.. that is, there is no "looping" other than what
the operating system does anyway to parcel out CPU time amongst all users.

No, I don't know how to implement these using the Microfocus / Net Express
product(s), but I'm sure you can make WinAPI calls, so there simply must be
a way to do it; perhaps someone here can point you in the right direction.

(FWIW, IMNSHO Microsoft Visual Anything is designed for those less capable
than the audience here).
```

##### ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

- **From:** "eselick" <eselick@gmail.com>
- **Date:** 2006-05-24T09:12:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148487127.608914.235600@i39g2000cwa.googlegroups.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net>`

```
Thanks Michael

Are you aware of any example code for doing API calls in general in Net
Exress?

Elliot
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-24T16:25:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6O%cg.14256$fb2.10414@newssvr27.news.prodigy.net>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com>`

```
"eselick" <eselick@gmail.com> wrote in message
news:1148487127.608914.235600@i39g2000cwa.googlegroups.com...
> Thanks Michael
>
> Are you aware of any example code for doing API calls in general in Net
> Exress?

Nah.

I ain't done no COBOL for more than five years, and all that was procedural
"batch-type" or "console display-accept" type code.

But if you can figure out how to call a standard DLL you can do it, because
that's all the WinAPIs are, a bunch (make that, "a **WHOLE** bunch) of
functions in a bunch of DLLs.

That said, if you are hooking into window procedures, then you may have to
watch out for 'compiler-specific' quirks... much as you have to do with
Microsoft Visual Anything.

(Adding a little shameless self-promotion)...let's say find what you need
for calling a function in a DLL, but are just not comfortable using all the
system objects... you could always contract with someone who does understand
those things, who could create for you a DLL with all the functions you need
using the syntax you want.... someone like, well, myself.

MCM
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2006-05-24T18:09:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12794ou7gtktde5@corp.supernews.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com>`

```

"eselick" <eselick@gmail.com> wrote in message 
news:1148487127.608914.235600@i39g2000cwa.googlegroups.com...
> Thanks Michael
>
> Are you aware of any example code for doing API calls in general in Net
> Exress?

Hi Elliot,

If you look under the Micro Focus SupportLine site at 
http://supportline.microfocus.com/examplesandutilities/nesamp.asp#Win32API , 
you will find a variety of examples of calling Windows APIs. (You may need 
to register/login to access this page).

Hope this helps.

SimonT.
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 4)_

- **From:** "eselick" <eselick@gmail.com>
- **Date:** 2006-05-25T09:52:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148575967.527613.67520@j73g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<12794ou7gtktde5@corp.supernews.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com>`

```
Thanks for the help everyone.

I think I'm going to run my COBOL program from an external scheduler.
Why reinvent the wheel?

Elliot
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-25T17:29:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com>`

```
"eselick" <eselick@gmail.com> wrote in message
news:1148575967.527613.67520@j73g2000cwa.googlegroups.com...
>
> I think I'm going to run my COBOL program from an external scheduler.
> Why reinvent the wheel?

Because Real Men don't need no stinkin' external schedulers.

MCM
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 6)_

- **From:** "eselick" <eselick@gmail.com>
- **Date:** 2006-06-01T07:22:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149171778.449367.202680@c74g2000cwc.googlegroups.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com>`

```
Oh well I guess I'll just have to email you a nasty reply in hex ...

Michael Mattias wrote:
> "eselick" <eselick@gmail.com> wrote in message
> news:1148575967.527613.67520@j73g2000cwa.googlegroups.com...
…[6 more quoted lines elided]…
> MCM
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 7)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2006-06-01T10:42:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A1Dfg.2924$EF1.224851@news20.bellglobal.com>`
- **In-Reply-To:** `<1149171778.449367.202680@c74g2000cwc.googlegroups.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com> <1149171778.449367.202680@c74g2000cwc.googlegroups.com>`

```
eselick wrote:
> Oh well I guess I'll just have to email you a nasty reply in hex ...
> 
…[12 more quoted lines elided]…
> 

Is that the same as sending a hex by email?

Donald
;<)
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-06-01T14:53:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com> <1149171778.449367.202680@c74g2000cwc.googlegroups.com>`

```
"eselick" <eselick@gmail.com> wrote in message
news:1149171778.449367.202680@c74g2000cwc.googlegroups.com...
> Oh well I guess I'll just have to email you a nasty reply in hex ...

How nasty can you get restricted to the letters A, B, C, D, E and F?

(oh-oh, that was asking for it, wasn't it?)

MCM
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 8)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-06-27T22:44:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7scco02neo@news1.newsguy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com> <1149171778.449367.202680@c74g2000cwc.googlegroups.com> <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com>`

```

In article <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com>, "Michael Mattias" <michael.mattias@gte.net> writes:
> "eselick" <eselick@gmail.com> wrote in message
> news:1149171778.449367.202680@c74g2000cwc.googlegroups.com...
> > Oh well I guess I'll just have to email you a nasty reply in hex ...
> 
> How nasty can you get restricted to the letters A, B, C, D, E and F?

Time to resurrect my 1995 comp.unix.aix "hex words" post?

-----
Don McCrady wrote:
> I'm sure 0xdeadbeef is just a nice memorable garbage value to
> initialize registers to, so that if one is accidentally used as a
> pointer, you can be reasonably sure that it's going to cause a core
> dump.  Besides that, it's a lot more politically correct than
> 0xbabeface and 0xdeadbabe.

You left out 0xbabeabed (hey, he started it).

I don't remember anyone on this thread mentioning AIX's 0xbadca11 in
stack traces.  (I think someone did mention 0xdeadc0de.)

When you start using 1 as "l" and 0 as "o", and allowing shorter
words by omitting leading 0s (as in 0xbadca11), possibilites abound:

- 0xacc01ade, which you might initialize memory to if you want to
  reward your out-of-bounds checking code
- 0xb01dface to make those memory errors stand out
- 0xaffab1e if it's not really an important memory error
- 0xdebac1e if it is
- 0xbad1dea when it's a design error
- 0xa1fa1fa to 0xfeed all that 0xbeef before it dies
- 0xfa110ff when you trace the stack back a little too far...
- 0x0ff10ad if you're using an ICE
- 0xbabb1e because "GIGO" is tough to represent in hex[1]
- 0xc0ffee when it's time for an extra cup (try the 0xcafe)
- 0xc0bb1e, which is how you put your code together, unless
- 0xd00d1e and 0xdabb1e is
- 0xdec0de, since you didn't 0xc0de right in the first place
- 0xfacade and 0xfeeb1e -- more trenchant analysis

The end result, of course, is that you're going to 0xcedeface if
these show up in your code.
-----

[1] Though, after 11 years' sober reflection, it occurs to me that
x'6160' is a reasonable "GIGO".
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 9)_

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2006-06-27T18:11:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151453042_53899@sp6iad.superfeed.net>`
- **In-Reply-To:** `<e7scco02neo@news1.newsguy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com> <1149171778.449367.202680@c74g2000cwc.googlegroups.com> <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com> <e7scco02neo@news1.newsguy.com>`

```
Michael Wojcik wrote:
> In article <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com>, "Michael Mattias" <michael.mattias@gte.net> writes:
>> "eselick" <eselick@gmail.com> wrote in message
…[44 more quoted lines elided]…
> 

LOL!

The DEC (RIP) Alpha (RIP) SRM console has a background process that traps memory
errors. A PS (process status) display identifies these processes (there may be more
than one) as "BeefEater waiting on 0xdeadbeef".

Jeff Campbell
n8wxs@arrl.net


----== Posted via Newsfeeds.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 9)_

- **From:** "Vivian" <vsaegesser@infogix.com>
- **Date:** 2006-06-28T11:43:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151520188.857525.121740@b68g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e7scco02neo@news1.newsguy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <XY_cg.14226$fb2.3261@newssvr27.news.prodigy.net> <1148487127.608914.235600@i39g2000cwa.googlegroups.com> <12794ou7gtktde5@corp.supernews.com> <1148575967.527613.67520@j73g2000cwa.googlegroups.com> <1Qldg.33297$4L1.7797@newssvr11.news.prodigy.com> <1149171778.449367.202680@c74g2000cwc.googlegroups.com> <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com> <e7scco02neo@news1.newsguy.com>`

```
Ok, let's just say I wanted to initialize the value to 0xbad1dea,
because, well, we have that sense of humor...  How would I  get
MicroFocus to allow a multi-byte directive instead of DEFAULTBYTE"xx"?
Seems to be the best I can do from below is sound like a sheep with BA
(BABABABA).


Michael Wojcik wrote:
> In article <bcDfg.10558$VE1.9419@newssvr14.news.prodigy.com>, "Michael Mattias" <michael.mattias@gte.net> writes:
> > "eselick" <eselick@gmail.com> wrote in message
…[53 more quoted lines elided]…
>    -- Dick Selcer, coach of the Cinci Bengals
```

###### ↳ ↳ ↳ Re: Efficient timers in Net Express or Object COBOL

_(reply depth: 10)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-06-28T21:39:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7usu002f81@news1.newsguy.com>`
- **References:** `<1148480928.355811.205830@y43g2000cwc.googlegroups.com> <1151520188.857525.121740@b68g2000cwa.googlegroups.com>`

```

In article <1151520188.857525.121740@b68g2000cwa.googlegroups.com>, "Vivian" <vsaegesser@infogix.com> writes:
> Ok, let's just say I wanted to initialize the value to 0xbad1dea,
> because, well, we have that sense of humor...  How would I  get
> MicroFocus to allow a multi-byte directive instead of DEFAULTBYTE"xx"?
> Seems to be the best I can do from below is sound like a sheep with BA
> (BABABABA).

I think you'd have to use an explicit VALUE clause for each item
(with either x"bad1dea" or h"bad1dea", depending on the item's
definition, and truncated or repeated as necessary for length), or
you'd have to set it at runtime with MOVE (probably combined with
pointer operations and/or reference modification).

Pity, as I rather like the idea of a DEFAULTWORD directive.  Office
applications could have their areas initialized to "0ff1ce".  Timer
routines to "c1cada".  If you don't like your manager, tell the world
by initializing areas with "b00ba1de".  Do a little advertising for
"c0cac01a".  Implement runtime licensing with "addedfee".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
