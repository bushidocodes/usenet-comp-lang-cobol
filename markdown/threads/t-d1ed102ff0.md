[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fill a comp-3 variable

_38 messages · 12 participants · 2006-07 → 2006-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Fill a comp-3 variable

- **From:** jferreira80@gmail.com
- **Date:** 2006-07-24T06:50:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com>`

```
Hi...just a hand-pocket question...... :)

i have a variable

01 ws-con-variable1      PIC 9(13)V9(02) COMP-3.

and i need to fill all the fields with value 9 .

I don't know why but if i defines de variable as

01 ws-con-variable1      PIC 9(13)V9(02) COMP-3 VALUE ALL 9.
 
it doesn't work...

any clue ?



 Cheers
```

#### ↳ Re: Fill a comp-3 variable

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-24T14:15:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oC4xg.11564$2v.11174@newssvr25.news.prodigy.net>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com>`

```
<jferreira80@gmail.com> wrote in message
news:1153749015.404152.23700@m79g2000cwm.googlegroups.com...
> Hi...just a hand-pocket question...... :)
>
…[12 more quoted lines elided]…
> any clue ?

VALUE "ALL <anything>" is (was?) only allowed for character (PIC X(n) or
A(n)) data items.
```

#### ↳ Re: Fill a comp-3 variable

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-24T09:23:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12c9lucfhu0lrf3@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com>`

```
jferreira80@gmail.com wrote:
> Hi...just a hand-pocket question...... :)
>
…[10 more quoted lines elided]…
> it doesn't work...

"ALL" works only on alphanumeric fields. You need:

PIC 9(13)V9(02) VALUE 9999999999999.99.
```

##### ↳ ↳ Re: Fill a comp-3 variable

- **From:** jferreira80@gmail.com
- **Date:** 2006-07-24T07:34:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153751643.438840.8060@b28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<12c9lucfhu0lrf3@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com>`

```

HeyBub escreveu:
> jferreira80@gmail.com wrote:
> > Hi...just a hand-pocket question...... :)
…[15 more quoted lines elided]…
> PIC 9(13)V9(02) VALUE 9999999999999.99.


Ok.....

but if your variable as 99 fields, like

01 ws-con-variable1      PIC 9(99)v9(02) COMP-3.

you don't define the value as 999.......999


any clues for this  problem??


cheers
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

- **From:** Donald Tees <donald_tees@donald-tees.ca>
- **Date:** 2006-07-24T10:37:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea2lt7$1rv$1@nntp.aioe.org>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com>`

```
jferreira80@gmail.com wrote:
> HeyBub escreveu:
> 
…[13 more quoted lines elided]…
> 

There are no such fields, by definition.

Donald
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-24T13:49:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ca5gv4gn3g0bb@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com>`

```
jferreira80@gmail.com wrote:
> HeyBub escreveu:
>> jferreira80@gmail.com wrote:
…[28 more quoted lines elided]…
> any clues for this  problem??

What do you mean "you don't define the value as 999....999"? Are you 
absolutely certain of that? It's not wise to venture an opinion whether 
something is or is not possible when you, yourself, don't know how to do it.


That said, COBOL doesn't permit numeric fields that big. And if COBOL did 
allow fields that big you DO define the initial value exactly as before 
(except for more digits, of course).

Just what are you trying to do anyway?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 4)_

- **From:** jferreira80@gmail.com
- **Date:** 2006-07-25T01:33:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153816428.234711.246510@p79g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<12ca5gv4gn3g0bb@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com>`

```
i reformulated my question....

i have a variable

01 ws-con-variable1      PIC 9(13)V9(02) COMP-3.

and i need that the initial value is all the fiels filled with nines.
i see the one solution is to use

PIC 9(13)V9(02) VALUE 9999999999999.99.

but my  question is when we got to fill this kind of variable with
larger fields.
even that cobol don't allow numerics fields so big, i think there is a
better solution than define the value with all the nines.


cheers...


HeyBub escreveu:
> jferreira80@gmail.com wrote:
> > HeyBub escreveu:
…[40 more quoted lines elided]…
> Just what are you trying to do anyway?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-25T09:19:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea4nnb$7u1$1@reader2.panix.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com> <1153816428.234711.246510@p79g2000cwp.googlegroups.com>`

```
In article <1153816428.234711.246510@p79g2000cwp.googlegroups.com>,
 <jferreira80@gmail.com> wrote:
>i reformulated my question....
>
…[4 more quoted lines elided]…
>and i need that the initial value is all the fiels filled with nines.

The processing requirement - or 'job' - that generates this need is... 
what, pray tell?

>i see the one solution is to use
>
…[5 more quoted lines elided]…
>better solution than define the value with all the nines.

This is what caused me to ask the previous question.  You want to do 
something for fields so large 'even that cobol don't allow numerics fields 
so big' - never mind the facts about what the latest versions do or don't 
allow - because your processing needs are... what?

DD
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-25T12:42:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dloxg.135283$dW3.47143@newssvr21.news.prodigy.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com> <1153816428.234711.246510@p79g2000cwp.googlegroups.com>`

```
<jferreira80@gmail.com> wrote in message
news:1153816428.234711.246510@p79g2000cwp.googlegroups.com...
> i reformulated my question....
>
…[12 more quoted lines elided]…
> better solution than define the value with all the nines.


Yes, there is a better solution.  Don't even try to initialize the field
with a VALUE clause. Write appropriate code at the appropriate point in the
procedure dovision instead.

While I consider myself a fairly imaginative guy, seems to me initializing a
numeric *variable* (and "ws-con-variable1" sure sounds like a *variable*
rather than a *constant* ) to anything other than zero is silly.

Not to mention, "all nines" is a silly initial value for a numeric as it is
totally meaningless and useless.

MCM
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 6)_

- **From:** Jürgen Vetter <vetter@dokom.net>
- **Date:** 2006-07-25T21:28:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44c68d3d$1@news.knipp.de>`
- **In-Reply-To:** `<dloxg.135283$dW3.47143@newssvr21.news.prodigy.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com> <1153816428.234711.246510@p79g2000cwp.googlegroups.com> <dloxg.135283$dW3.47143@newssvr21.news.prodigy.com>`

```
Am 25.07.2006 14:42 schrieb Michael Mattias:

> 
> Yes, there is a better solution.  Don't even try to initialize the field
> with a VALUE clause. Write appropriate code at the appropriate point in the
> procedure dovision instead.

that's right! I use the value clause in the definition of variables only
if i want to use them as constants. Because cobol can't mace a differenz
between global and local variables i devide them be defining groups.

01 constants.
   05  var1           pic 9(4) value 1234.
01 workfields.
   05  var2           pic 9(4).
   05  var3           pic x(4).
...
   initialize workfields
...

> While I consider myself a fairly imaginative guy, seems to me initializing a
> numeric *variable* (and "ws-con-variable1" sure sounds like a *variable*
> rather than a *constant* ) to anything other than zero is silly.

it seems to me to silly. a numeric field is initialized to zero or if
you need a invalid value you fill it with a value which is not in the
possible range of values, maybe a value like -1 if you define it as
pic s9(nn).
```

###### ↳ ↳ ↳ Global / Local (was: Fill a comp-3 variable

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-25T19:44:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4wuxg.79754$js3.51809@fe04.news.easynews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com> <1153816428.234711.246510@p79g2000cwp.googlegroups.com> <dloxg.135283$dW3.47143@newssvr21.news.prodigy.com> <44c68d3d$1@news.knipp.de>`

```

"J�rgen Vetter" <vetter@dokom.net> wrote in message 
news:44c68d3d$1@news.knipp.de...
> Am 25.07.2006 14:42 schrieb Michael Mattias:
>
…[8 more quoted lines elided]…
>
<snipage>

HUH????

COBOL has supported local and global variables since the '85 Standard.  Now, if 
you don't USE nested programs, but just paragraphs or sections, this won't do 
you any good.  However, if YOU want to use such, they have been available for 
decades!!!
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-25T11:25:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12cchebct09d73@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <12ca5gv4gn3g0bb@news.supernews.com> <1153816428.234711.246510@p79g2000cwp.googlegroups.com>`

```
jferreira80@gmail.com wrote:
> i reformulated my question....
>
…[13 more quoted lines elided]…
>

Okay, if you think there's a better solution, pray tell us what it is. As of 
now, four people have told you there is one and only one way to initialize a 
COMP-3 field to all 9s. We four have, conservatively, over 150 man-years of 
collective COBOL programming experience. I, myself, teach COBOL at the 
university level. Others have literally "written the book" on COBOL, and 
some have even read the book.

In addition, many others have read your question and not seen fit to 
respond, probably because they don't have an answer either.

If there is such a mechanism, we've never seen it or heard of it. Don't 
count on a more economical way of initializing COMP-3 fields or it'll break 
your heart.

As an aside, current practice (at least here) is to avoid COMP-3 fields; the 
confusion and problems they generate are no longer offset by their 
efficiency of storage or computational speed.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

- **From:** Jürgen Vetter <vetter@dokom.net>
- **Date:** 2006-07-25T21:19:09+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44c68b1e$1@news.knipp.de>`
- **In-Reply-To:** `<1153751643.438840.8060@b28g2000cwb.googlegroups.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com>`

```
Am 24.07.2006 16:34 schrieb jferreira80@gmail.com:
> 
> Ok.....
…[5 more quoted lines elided]…
> you don't define the value as 999.......999

Do you know any compiler which can work with
more than pic 9(18)?

I don't know why you have to fill it with 9?
A numeric field is initialized by zero.

Which application need to fill a field with 9?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-25T13:41:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de>`

```
On Tue, 25 Jul 2006 21:19:09 +0200, Jï¿½rgen Vetter <vetter@dokom.net>
wrote:

>> 01 ws-con-variable1      PIC 9(99)v9(02) COMP-3.
>> 
…[3 more quoted lines elided]…
>more than pic 9(18)?

I don't , but I'm curious - is there any architecture which can handle
this?

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 5)_

- **From:** Joe Zitzelberger <zberger@knology.net>
- **Date:** 2006-07-25T19:42:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zberger-B0CBDF.19422125072006@ispnews.usenetserver.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com>`

```
In article <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com>,
 Howard Brazee <howard@brazee.net> wrote:

> On Tue, 25 Jul 2006 21:19:09 +0200, J�rgen Vetter <vetter@dokom.net>
> wrote:
…[9 more quoted lines elided]…
> this?

JVMs can.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-26T08:09:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com>`

```
On Tue, 25 Jul 2006 19:42:21 -0400, Joe Zitzelberger
<zberger@knology.net> wrote:

>> >> 01 ws-con-variable1      PIC 9(99)v9(02) COMP-3.
>> >> 
…[8 more quoted lines elided]…
>JVMs can.

COMP-3?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 7)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-26T16:23:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea7tsg$1rh$03$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com>`

```
AKA. PACKED-DECIMAL.

Roger

"Howard Brazee" <howard@brazee.net> schrieb im Newsbeitrag 
news:trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com...
> On Tue, 25 Jul 2006 19:42:21 -0400, Joe Zitzelberger
> <zberger@knology.net> wrote:
…[13 more quoted lines elided]…
> COMP-3?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-26T14:37:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message
news:ea7tsg$1rh$03$1@news.t-online.com...
> >>JVMs can.
> >
> > COMP-3?
>
> AKA. PACKED-DECIMAL.


Remember, COMP-3 is 'implementor-defined' so blanket statements about 'how
to fill' these data items are a tad iffy and should always be conditioned on
something...like the O/S and/or specific compiler....

MCM
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-26T14:42:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<obLxg.123271$vu2.19499@fe05.news.easynews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com>`

```
IBM can handle this (COMP-3 or Packed-Decimal) items up to 31-digits - with 
Enterprise COBOL on z/OS.

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg31/2.4.5
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 10)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-26T16:56:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea7vrj$cer$01$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com>`

```
And OpenCOBOL upto 36 with all numeric field types except binary  :-)
(And binary is on the way)

Incidentally Bill, now you can promote our
"BINARY-HUGE", better BINARY-LONG-LONG  :-)

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:obLxg.123271$vu2.19499@fe05.news.easynews.com...
> IBM can handle this (COMP-3 or Packed-Decimal) items up to 31-digits - 
> with Enterprise COBOL on z/OS.
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-26T09:16:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com>`

```
On Wed, 26 Jul 2006 14:42:29 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>IBM can handle this (COMP-3 or Packed-Decimal) items up to 31-digits - with 
>Enterprise COBOL on z/OS.


Which is less than a third of 
 01 ws-con-variable1      PIC 9(99)v9(02) COMP-3.

I was not familiar with any other implementations of COMP-3, and
haven't worked with CoBOL with a JVM.    I haven't even worked with
packed fields with Java.

But it makes sense that a JVM wouldn't be limited to the hardware
architecture.    I've been a proponent of a LARGE data type that is
virtually unlimited in size - that would be implementer designed - if
I say PIC 9(99)V9(02) LARGE.  The implementer can decide how to store
it.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 11)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-26T17:26:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea81jo$9ou$03$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com>`

```
Well, do you want to store a magnitude googol or even a googolplex ?
Cobol is a business language, I don't think we have need for these
magnitudes !
(Consider what these numbers count -
 number of atoms in the earth ? number of atoms in the universe ? -
 - research!)

Roger

"Howard Brazee" <howard@brazee.net> schrieb im Newsbeitrag 
news:1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com...
> On Wed, 26 Jul 2006 14:42:29 GMT, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
…[17 more quoted lines elided]…
> it.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 12)_

- **From:** Jürgen Vetter <vetter@dokom.net>
- **Date:** 2006-07-26T18:20:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44c7b2af$1@news.knipp.de>`
- **In-Reply-To:** `<ea81jo$9ou$03$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com>`

```
Am 26.07.2006 17:26 schrieb Roger While:
> Well, do you want to store a magnitude googol or even a googolplex ?
> Cobol is a business language, I don't think we have need for these
…[3 more quoted lines elided]…
>  - research!)

maybe you have to count bill gates salary :->
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 13)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-26T18:29:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea859c$hl6$03$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de>`

```
He-he, when BG approaches 18 digits then the world has a problem :-)

Roger

"Jï¿½rgen Vetter" <vetter@dokom.net> schrieb im Newsbeitrag 
news:44c7b2af$1@news.knipp.de...
> Am 26.07.2006 17:26 schrieb Roger While:
>> Well, do you want to store a magnitude googol or even a googolplex ?
…[6 more quoted lines elided]…
> maybe you have to count bill gates salary :->
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-26T10:34:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb6fc217uq4cvctl8if8bpni5r3a4gmnph@4ax.com>`
- **References:** `<1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de>`

```
On Wed, 26 Jul 2006 18:20:11 +0200, Jï¿½rgen Vetter <vetter@dokom.net>
wrote:

>
>maybe you have to count bill gates salary :->

I don't believe his salary is extraordinary.   He doesn't need a high
salary when he owns so much of the company.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 14)_

- **From:** Jürgen Vetter <vetter@dokom.net>
- **Date:** 2006-07-27T07:59:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44c872a9$1@news.knipp.de>`
- **In-Reply-To:** `<fb6fc217uq4cvctl8if8bpni5r3a4gmnph@4ax.com>`
- **References:** `<1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de> <fb6fc217uq4cvctl8if8bpni5r3a4gmnph@4ax.com>`

```
Am 26.07.2006 18:34 schrieb Howard Brazee:
> On Wed, 26 Jul 2006 18:20:11 +0200, Jï¿½rgen Vetter <vetter@dokom.net>
> wrote:
…[5 more quoted lines elided]…
> salary when he owns so much of the company.

hey, that was a joke. it seems hard to me, to translate it in english,
but i do my very best :-)
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 13)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-26T14:34:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12cfgta8nhfn89b@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de>`

```
J�rgen Vetter wrote:
> Am 26.07.2006 17:26 schrieb Roger While:
>> Well, do you want to store a magnitude googol or even a googolplex ?
…[6 more quoted lines elided]…
> maybe you have to count bill gates salary :->

Bill Gates annual salary is a mere $865,114. By corporate standards, he is 
significantly underpaid.

Gates, being mindful of the great position of trust invested in him, tries 
to keep his salary at a reasonable multiple (say, 4 times that of) the 
president.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 14)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-26T12:48:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153943307.650178.293670@m79g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<12cfgta8nhfn89b@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de> <12cfgta8nhfn89b@news.supernews.com>`

```

HeyBub wrote:

> Bill Gates annual salary is a mere $865,114. By corporate standards, he is
> significantly underpaid.

I am sure that it is arranged by wizards to minimise his tax bills.

> Gates, being mindful of the great position of trust invested in him, tries
> to keep his salary at a reasonable multiple (say, 4 times that of) the
> president.

That is not to say that he considers himself to be as low as only 4
times as important as the president.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 14)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-26T21:14:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0XQxg.181102$F_3.108799@newssvr29.news.prodigy.net>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de> <12cfgta8nhfn89b@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
news:12cfgta8nhfn89b@news.supernews.com...

>Bill Gates annual salary is a mere $865,114. By corporate standards, he is
>significantly underpaid.

> Gates, being mindful of the great position of trust invested in him, tries
> to keep his salary at a reasonable multiple (say, 4 times that of) the
> president.

If you mean president of the USA, 865K is merely a little over twice the
$400K salary which went into effect for president of US I think in '01.

MCM
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 15)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-26T20:32:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12cg5sbrjion6c7@news.supernews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com> <44c7b2af$1@news.knipp.de> <12cfgta8nhfn89b@news.supernews.com> <0XQxg.181102$F_3.108799@newssvr29.news.prodigy.net>`

```
Michael Mattias wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
> news:12cfgta8nhfn89b@news.supernews.com...
…[11 more quoted lines elided]…
>
Ooooh! Thanks. I'm a bit behind the times.

Still, all is relative. The president's salary in 1909 ($75,000) was really 
$1,607,000 in current dollars.

According to Wikipedia.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 12)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-07-26T09:55:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153932941.827644.288190@i3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<ea81jo$9ou$03$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com> <ea81jo$9ou$03$1@news.t-online.com>`

```

Roger While wrote:
> Well, do you want to store a magnitude googol or even a googolplex ?
> Cobol is a business language, I don't think we have need for these
…[3 more quoted lines elided]…
>  - research!)

The number of times that the universe has run through to completion, so
far?
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-26T17:05:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yhNxg.386784$SQ6.218987@fe09.news.easynews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <ea7tsg$1rh$03$1@news.t-online.com> <r6Lxg.75679$Lm5.58228@newssvr12.news.prodigy.com> <obLxg.123271$vu2.19499@fe05.news.easynews.com> <1c1fc21cv66lvkeqouhtok0cth8lbthtkq@4ax.com>`

```
Sorry Howard,
  I must have missed when this thread got to:
   Pic 9(99)
(I was just thinking of "bigger than 18")

I do believe (as stated earlier) that one older COBOL *could* handle Pic 
9(100) - but I don't remember which one (and certainly don't remember if it 
supported either Comp-3 or Packed-Decimal.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 7)_

- **From:** Joe Zitzelberger <zberger@knology.net>
- **Date:** 2006-07-28T08:23:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zberger-D30DD6.08233728072006@ispnews.usenetserver.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com>`

```
In article <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com>,
 Howard Brazee <howard@brazee.net> wrote:

> On Tue, 25 Jul 2006 19:42:21 -0400, Joe Zitzelberger
> <zberger@knology.net> wrote:
…[13 more quoted lines elided]…
> COMP-3?

No, big decimals -- Pic 9(99)v9(02).  The internal representation of the 
data is not relevant.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-28T07:55:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o5kc2pskufpnbvhsvg7q2c8g31s439aig@4ax.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <zberger-D30DD6.08233728072006@ispnews.usenetserver.com>`

```
On Fri, 28 Jul 2006 08:23:38 -0400, Joe Zitzelberger
<zberger@knology.net> wrote:

>> >> I don't , but I'm curious - is there any architecture which can handle
>> >> this?
…[6 more quoted lines elided]…
>data is not relevant.

The internal representation is what architecture is about.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 9)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-28T16:48:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ead82s$7a6$02$1@news.t-online.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de> <utscc2dvjtvld54ubt93792n7q29jph82l@4ax.com> <zberger-B0CBDF.19422125072006@ispnews.usenetserver.com> <trtec2hhk546vj8tnh6mbv0poksrr3cms0@4ax.com> <zberger-D30DD6.08233728072006@ispnews.usenetserver.com> <7o5kc2pskufpnbvhsvg7q2c8g31s439aig@4ax.com>`

```
In fact, OpenCOBOL could potentially deal with
pic 9(99), pic 9(999), ... (with/without COMP-3 AKA PACKED-DECIMAL)
As OpenCOBOL uses GMP, theoretically there is
no limit (See GMP home page) except machine/compiler
limits.

However, who needs this?  :-)

Roger

"Howard Brazee" <howard@brazee.net> schrieb im Newsbeitrag
news:7o5kc2pskufpnbvhsvg7q2c8g31s439aig@4ax.com...
> On Fri, 28 Jul 2006 08:23:38 -0400, Joe Zitzelberger
> <zberger@knology.net> wrote:
>
> >> >> I don't , but I'm curious - is there any architecture which can
handle
> >> >> this?
> >> >
…[7 more quoted lines elided]…
> The internal representation is what architecture is about.
```

###### ↳ ↳ ↳ Re: Fill a comp-3 variable

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-25T19:47:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3zuxg.97319$tQ4.26912@fe01.news.easynews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com> <12c9lucfhu0lrf3@news.supernews.com> <1153751643.438840.8060@b28g2000cwb.googlegroups.com> <44c68b1e$1@news.knipp.de>`

```
"J�rgen Vetter" <vetter@dokom.net> wrote in message 
news:44c68b1e$1@news.knipp.de...
> Am 24.07.2006 16:34 schrieb jferreira80@gmail.com:
<snip>
> Do you know any compiler which can work with
> more than pic 9(18)?
>

IBM has supported 31-digit numeric fields for several years now - in accordance 
with the '02 COBOL Standard.   I believe that Micro Focus already does as well, 
probably several others as well.

As I recall (and this is memory only) there was one vendor supporting 100+ digit 
numeric fields but NOT floating point MANY years ago.

Bottom-Line:
  If using LARGE numeric fields, do look at the HIGHEST-/Lowest-Algebraic 
intrinsic functions.  I am not certain which vendors currently support them, but 
they really do work for such fields.
```

#### ↳ Re: Fill a comp-3 variable

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-24T15:20:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oz5xg.352069$SQ6.66657@fe09.news.easynews.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com>`

```
Not (probably) a solution for this poster, but for those interested in this type 
of problem, check out the '02 Standard

   Highest-Algebraic

Intrinsic Function.  Also interesting is how that works compared to

  Lowest-Algebraic

for fields like this with no "S" in the Pic.
```

#### ↳ Re: Fill a comp-3 variable

- **From:** docdwarf@panix.com ()
- **Date:** 2006-08-03T17:12:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eatap7$f9b$1@reader2.panix.com>`
- **References:** `<1153749015.404152.23700@m79g2000cwm.googlegroups.com>`

```
In article <1153749015.404152.23700@m79g2000cwm.googlegroups.com>,
 <jferreira80@gmail.com> wrote:
>Hi...just a hand-pocket question...... :)
>
…[4 more quoted lines elided]…
>and i need to fill all the fields with value 9 .

[snip]

Well, it's been long enough so that this assignment should have been dealt 
with... so it's time for another example of 'Kids, Don't Try This At 
Home!' code.  Given the platform of Big Blue Iron and the compiler of IBM 
Enterprise COBOL for z/OS and OS/390 3.2.1 then how about...

01  PACKED-DEC PIC S9(13)V99 COMP-3 VALUE +0.
01  BIGGEST-PD-X-COMP3.
    05  FILLER PIC X(09) VALUE ALL X'99'.
    05  FILLER PIC X(01) VALUE     X'9C'.
01  BIGGEST-PD-X REDEFINES BIGGEST-PD-X-COMP3
                                         PIC S9(16)V99 COMP-3.
01  DISPLAY-Z PIC Z(15)9.99+ VALUE ZEROES.
...
PROCEDURE DIVISION.
    MOVE BIGGEST-PD-X TO PACKED-DEC.
    MOVE PACKED-DEC TO DISPLAY-Z.

... or a reasonable facsimile thereof.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
