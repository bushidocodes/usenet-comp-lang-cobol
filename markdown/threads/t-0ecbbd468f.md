[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mili/micro seconds in Cobol z/os

_10 messages · 8 participants · 2007-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### mili/micro seconds in Cobol z/os

- **From:** "Janek" <neuros@poczta.onet.pl>
- **Date:** 2007-07-20T16:00:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```
Hi

I'm looking for a function (not CICS function, not DB2 function) which 
returns time in miliseconds or microseconds.

thanks a lot

Jan
```

#### ↳ Re: mili/micro seconds in Cobol z/os

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-07-20T15:19:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Un4oi.9048$tj6.2990@newsread4.news.pas.earthlink.net>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```

"Janek" <neuros@poczta.onet.pl> wrote in message 
news:f7qfbe$l69$1@atlantis.news.tpi.pl...
> Hi
>
…[6 more quoted lines elided]…
>

You could search comp.lang.cobol for "hottel mainframe timer".  Sometime 
back there wasa difference of opinion abou the relative performance of 
Quicksort and Combsort and I timed a version of each with an assemble 
program that I wrote:



> //JOBNAME  JOB (ACCT,ROOM),'HOTTEL TASKTIME',MSGCLASS=S,CLASS=K //PROCLIB 
> JCLLIB ORDER=USERID.DVL.PROC //        SET TITLE1='PFX.TASKTIME' //OUTPUT 
…[28 more quoted lines elided]…
> DD * NAME TASKTIME(R)


The comments at the from show an example of how to call it from a COBOL 
program.
```

##### ↳ ↳ Re: mili/micro seconds in Cobol z/os

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-07-21T17:21:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xgroi.10534$Od7.1833@newsread1.news.pas.earthlink.net>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl> <Un4oi.9048$tj6.2990@newsread4.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:Un4oi.9048$tj6.2990@newsread4.news.pas.earthlink.net...
>
> "Janek" <neuros@poczta.onet.pl> wrote in message 
…[51 more quoted lines elided]…
>

Sorry I think I misunderstood what you are looking for.
```

#### ↳ Re: mili/micro seconds in Cobol z/os

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-07-20T08:40:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184946004.321188.6990@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```
On Jul 20, 7:00 am, "Janek" <neu...@poczta.onet.pl> wrote:
> Hi
>
…[5 more quoted lines elided]…
> Jan


Hi,

You can use the following Windows functions to get the system
time with milliseconds precision:

	GetTickCount()

	GetTickCount64()

	timeGetTime()

	GetSystemTime()

	QueryPerformanceCounter()

	QueryPerformanceFrequency()

http://msdn2.microsoft.com/en-us/library/ms724408.aspx

http://msdn2.microsoft.com/en-us/library/ms724411.aspx

http://msdn2.microsoft.com/en-us/library/ms713418.aspx

http://msdn2.microsoft.com/en-us/library/ms724390.aspx

http://msdn2.microsoft.com/en-us/library/ms644904.aspx

http://msdn2.microsoft.com/en-us/library/ms644905.aspx

Kellie.
```

##### ↳ ↳ Re: mili/micro seconds in Cobol z/os

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-07-21T05:11:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Agoi.139705$qT.124202@fe06.news.easynews.com>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl> <1184946004.321188.6990@k79g2000hse.googlegroups.com>`

```
The OP has "COBOL z/os" in the subject so a Windows solution probably will not 
work.  However, the other answer with an LE callable service will work.
```

#### ↳ Re: mili/micro seconds in Cobol z/os

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2007-07-20T11:46:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18l1a35p4mgkb1j0clh66clv3c0fpaflgh@4ax.com>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```
On Fri, 20 Jul 2007 16:00:36 +0200, "Janek" <neuros@poczta.onet.pl>
wrote:

>Hi
>
…[6 more quoted lines elided]…
>

Can't you use the existing function current-date and calculate mili or
micro seconds from the time yourself?

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I wanted to do something nice so I bought my mother-in-law a chair. 
Now they won't let me plug it in."
--Henry Youngman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: mili/micro seconds in Cobol z/os

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-07-20T16:56:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kP5oi.40136$Um6.3934@newssvr12.news.prodigy.net>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl> <18l1a35p4mgkb1j0clh66clv3c0fpaflgh@4ax.com>`

```
In article <18l1a35p4mgkb1j0clh66clv3c0fpaflgh@4ax.com>, SkippyPB <swiegand@nospam.neo.rr.com> wrote:
>On Fri, 20 Jul 2007 16:00:36 +0200, "Janek" <neuros@poczta.onet.pl>
>wrote:
…[4 more quoted lines elided]…
>micro seconds from the time yourself?

Nope. CURRENT-DATE resolves to hundredths of a second, and no finer.
```

#### ↳ Re: mili/micro seconds in Cobol z/os

- **From:** Gerry Palmer <gpalmer@pobox.com>
- **Date:** 2007-07-20T19:09:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q5g2a3tfpvrrjo98ljtlt3t5iq36rofqff@4ax.com>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```
On Fri, 20 Jul 2007 16:00:36 +0200, "Janek" <neuros@poczta.onet.pl>
wrote:

>Hi
>
…[6 more quoted lines elided]…
>

The LANGUAGE ENVIRONMENT CEELOCT Callable Service returns
the current local date or time in three formats:         
                                                         
-> LILIAN DATE (the number of days since 14 October 1582)
-> LILIAN SECONDS (the number of seconds since 00:00:00  
   14 October 1582)                                      
-> GREGORIAN character string (format YYYYMMDDHHMISS999) 

----------
CALL "CEELOCT" USING WS-CEELOCT-LILIAN,    
                     WS-CEELOCT-SECONDS,   
                     WS-CEELOCT-GREGORIAN, 
                     WS-CEE-FEEDBACK-CODE. 
----------

Gregorian string sample:

* GREGORIAN STRING: 20070720185206713
```

##### ↳ ↳ Re: mili/micro seconds in Cobol z/os

- **From:** "Janek" <neuros@poczta.onet.pl>
- **Date:** 2007-07-23T13:29:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f823na$akq$1@nemesis.news.tpi.pl>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl> <q5g2a3tfpvrrjo98ljtlt3t5iq36rofqff@4ax.com>`

```
Uzytkownik "Gerry Palmer" <gpalmer@pobox.com> napisal w wiadomosci 
news:q5g2a3tfpvrrjo98ljtlt3t5iq36rofqff@4ax.com...
> On Fri, 20 Jul 2007 16:00:36 +0200, "Janek" <neuros@poczta.onet.pl>
> wrote:
…[30 more quoted lines elided]…
>
BIG THANKS!!!
It is what I'm looking for.

Jan
```

#### ↳ Re: mili/micro seconds in Cobol z/os

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-07-21T10:48:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13a4alc37fg5aa7@news.supernews.com>`
- **References:** `<f7qfbe$l69$1@atlantis.news.tpi.pl>`

```
Janek wrote:
> Hi
>
> I'm looking for a function (not CICS function, not DB2 function) which
> returns time in miliseconds or microseconds.

Whatever you use, be sure to check the hardware specifications. The CPU 
clock may not resolve to microseconds so you'd get two events happening with 
a zero time interval.

I don't know your application, but it is often prudent to find the average 
time for many operations.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
