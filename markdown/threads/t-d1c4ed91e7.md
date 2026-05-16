[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Cobol "SLEEP" routine

_13 messages · 8 participants · 2007-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Cobol "SLEEP" routine

- **From:** "C C" <someone@atsbcglobal.net>
- **Date:** 2007-05-15T07:20:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`

```
Hello.

Is there a way in MF Cobol to pause program execution (sleep) for, let's 
say, 5 minutes???  My workaround is to call the AIX command "sleep 300".  I 
need a routine in Cobol itself so I may vary the time to pause in some 
programs.

Thanks in advance.
```

#### ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "Steve Rainbird" <news.nospam@rainbird.me.nospam.uk>
- **Date:** 2007-05-15T13:52:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5atoomF2qeibjU1@mid.individual.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`

```
"C C" <someone@atsbcglobal.net> wrote in message 
news:yAh2i.4627$UU.2661@newssvr19.news.prodigy.net...
> Hello.
>
…[6 more quoted lines elided]…
>


Not that I know of.

I use

call "system" using ws-sleep-call


Where ws-sleep-call is defined as

      01  ws-mss-sleep-call.
           03                                 pic x(6) value "sleep ".
           03  ws-mss-sleep         pic 9(15).999.
           03                                 pic x value x"00".

Works for me.
```

##### ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "C C" <someone@atsbcglobal.net>
- **Date:** 2007-05-15T08:28:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net>`

```
Thanks.  That's what I'm doing right now.  I just want to avoid having to 
call "system".  In AIX, a new-line is output by the system thus online 
sessions experience a shift on their screen.  This behavior still occurs 
even if my call "system" script re-directs output to /dev/null.


"Steve Rainbird" <news.nospam@rainbird.me.nospam.uk> wrote in message 
news:5atoomF2qeibjU1@mid.individual.net...
> "C C" <someone@atsbcglobal.net> wrote in message 
> news:yAh2i.4627$UU.2661@newssvr19.news.prodigy.net...
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** Vaclav Snajdr <snajdr.vaclav@t-online.de>
- **Date:** 2007-05-15T15:48:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2cdof$tbi$01$1@news.t-online.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net> <Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net>`

```
it is possible to use "accept with timeout xyz" instead call system ...
(in background programs too)



C C wrote:

> Thanks.  That's what I'm doing right now.  I just want to avoid having to
> call "system".  In AIX, a new-line is output by the system thus online
…[39 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

_(reply depth: 4)_

- **From:** "C C" <someone@atsbcglobal.net>
- **Date:** 2007-05-15T11:43:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cql2i.26$u56.13@newssvr22.news.prodigy.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net> <Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net> <f2cdof$tbi$01$1@news.t-online.com>`

```
I think "TIME-OUT" needs a SCREEN SECTION.  I don't want SCREEN SECTION in 
the sleep functionality I am trying to implement in programs under cron or 
batch control.

"Vaclav Snajdr" <snajdr.vaclav@t-online.de> wrote in message 
news:f2cdof$tbi$01$1@news.t-online.com...
> it is possible to use "accept with timeout xyz" instead call system ...
> (in background programs too)
…[52 more quoted lines elided]…
> Vaclav Snajdr
```

###### ↳ ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

_(reply depth: 5)_

- **From:** Vaclav Snajdr <snajdr.vaclav@t-online.de>
- **Date:** 2007-05-16T11:42:43+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2ejmp$bs2$01$1@news.t-online.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net> <Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net> <f2cdof$tbi$01$1@news.t-online.com> <Cql2i.26$u56.13@newssvr22.news.prodigy.net>`

```
no, accept with timeout need not the screen section.
The program using this is a background program and can be
run via cron too. In this case you need set the TERM to console
perhaps (so i had it under hp-ux) - because accept needs the ADIS.  

C C wrote:

> I think "TIME-OUT" needs a SCREEN SECTION.  I don't want SCREEN SECTION in
> the sleep functionality I am trying to implement in programs under cron or
…[59 more quoted lines elided]…
>> Vaclav Snajdr
```

###### ↳ ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

_(reply depth: 6)_

- **From:** "C C" <someone@atsbcglobal.net>
- **Date:** 2007-05-16T06:45:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I9C2i.158$4Y.94@newssvr19.news.prodigy.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net> <Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net> <f2cdof$tbi$01$1@news.t-online.com> <Cql2i.26$u56.13@newssvr22.news.prodigy.net> <f2ejmp$bs2$01$1@news.t-online.com>`

```
I had tried this but the compiler returns an error if there is no screen 
section! I don't know what directive I should use to compile the TIME-OUT 
without a screen section.

Anyway, I have successfully tested the "CALL "sleep" USING BY VALUE 300.". 
AND it does not return a newline to the running program thus NOT shifting 
the screen one line up.

"Vaclav Snajdr" <snajdr.vaclav@t-online.de> wrote in message 
news:f2ejmp$bs2$01$1@news.t-online.com...
> no, accept with timeout need not the screen section.
> The program using this is a background program and can be
…[72 more quoted lines elided]…
> Vaclav Snajdr
```

###### ↳ ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "Steve Rainbird" <news.nospam@rainbird.me.nospam.uk>
- **Date:** 2007-05-15T16:00:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5au08sF2qmoj4U1@mid.individual.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <5atoomF2qeibjU1@mid.individual.net> <Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net>`

```
"C C" <someone@atsbcglobal.net> wrote in message 
news:Pzi2i.3295$zj3.230@newssvr23.news.prodigy.net...
> Thanks.  That's what I'm doing right now.  I just want to avoid having to 
> call "system".  In AIX, a new-line is output by the system thus online 
…[41 more quoted lines elided]…
>


Have you tried call "SYSTEM" there is a difference but I can't remember 
offhand what it is.

Or maybe even CBL_EXEC_RUN_UNIT although I have never used this.
```

#### ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** Thomas <tmanal@gmx.de>
- **Date:** 2007-05-15T05:56:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179233766.083130.229620@n59g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`

```
On 15 Mai, 14:20, "C C" <some...@atsbcglobal.net> wrote:
> Hello.
>
…[5 more quoted lines elided]…
> Thanks in advance.

Hello,

I don't know a commando for sleep.

Either you write a loop with perform varying... or you use a loop with
checking out the time while it is looping.
But in both solutions the program/machine is (very) busy and not
sleeping!

Thomas
```

#### ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-05-15T13:48:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<znm2i.40$gC.98401@news.sisna.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`

```
Why just not to call it directly ?

           CALL 'sleep' USING BY VALUE 300.

Regards,
Sergey


"C C" <someone@atsbcglobal.net> wrote in message 
news:yAh2i.4627$UU.2661@newssvr19.news.prodigy.net...
> Hello.
>
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-05-15T19:32:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KVn2i.438596$c62.361592@fe07.news.easynews.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net>`

```
I don't know which versions it is and is not in, but check your documentation 
for the Micro Focus callable service

   CBL_THREAD_SLEEP

P.S.  I haven't actually used it myself, so "YMMV"
```

##### ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-15T20:36:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GRo2i.184799$DE1.31850@pd7urf2no>`
- **In-Reply-To:** `<KVn2i.438596$c62.361592@fe07.news.easynews.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <KVn2i.438596$c62.361592@fe07.news.easynews.com>`

```
William M. Klein wrote:
> I don't know which versions it is and is not in, but check your documentation 
> for the Micro Focus callable service
…[4 more quoted lines elided]…
> 
Out of curiosity I went looking, searching on 'WAIT', 'SLEEP' - no luck. 
Never thought of CBL_THREAD......

Here's the reference to it in Net Express V 5.0 :-

http://supportline.microfocus.com/supportline/documentation/books/nx50/nx50indx.htm

Jimmy
```

##### ↳ ↳ Re: Microfocus Cobol "SLEEP" routine

- **From:** "Gael Wilson" <gael.wilson@microfocusuk.com>
- **Date:** 2007-05-17T09:13:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<134o3o7ji07haaf@corp.supernews.com>`
- **In-Reply-To:** `<KVn2i.438596$c62.361592@fe07.news.easynews.com>`
- **References:** `<yAh2i.4627$UU.2661@newssvr19.news.prodigy.net> <KVn2i.438596$c62.361592@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:KVn2i.438596$c62.361592@fe07.news.easynews.com...
>I don't know which versions it is and is not in, but check your 
>documentation for the Micro Focus callable service
…[4 more quoted lines elided]…
>

Note that your application has to be threaded in order to use this API 
otherwise it returns immediately with a non-zero RETURN-CODE, as the 
CBL_THREAD_ APIs are only available in the threaded COBOL run-time.

Gael.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
