[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Testing a date age by month

_10 messages · 6 participants · 2002-08_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Re: Testing a date age by month

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-08-16T07:18:42+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3D5C9942.B92F8273@Azonic.co.nz>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> In the case where
> the application DOES want to treat this as "1 month" - then it is true that
> the Standard doesn't provide a solution.  

And it doesn't need to.  It is trivial to multiply year numbers by 12
and add the months for those that wish to do that. The date routines are
only required because the calculations are complex and difficult to get
right.

Back when we used Pounds shillings and pence there were routines
provided to take the difference between two, convert to pence and back. 
With Dollars and cents this is trivial and unrequired.
```

#### ↳ Re: Testing a date age by month

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-16T05:50:43+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3D5C93D6.62D608D3@shaw.ca>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz>`

```


Richard Plinston wrote:

> William M. Klein wrote:
> >
…[11 more quoted lines elided]…
> With Dollars and cents this is trivial and unrequired.

Ooh ! Wish they'd be around in '49 when I was trying to figure 2.5% of a pound
<G>
```

##### ↳ ↳ Re: Testing a date age by month

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-16T16:05:58-07:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0208161505.21ccf61b@posting.google.com>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote 

> Ooh ! Wish they'd be around in '49 when I was trying to figure 2.5% of a pound
> <G>

I've got '2.5% of a pound',
Jolly, jolly '2.5% of a pound',
I've got '2.5% of a pound',
To last me all my life.  ....
```

###### ↳ ↳ ↳ Re: Testing a date age by month

- **From:** "Hugh Candlin" <NoPersonalMailPlease@MyDot.Com>
- **Date:** 2002-08-16T23:15:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<XHf79.15201$Ke2.1265293@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message
news:217e491a.0208161505.21ccf61b@posting.google.com...
> "James J. Gavan" <jjgavan@shaw.ca> wrote
>
> > Ooh ! Wish they'd be around in '49 when I was trying to figure 2.5% of a
pound
> > <G>
>
…[3 more quoted lines elided]…
> To last me all my life.  ....

I've got point eight three repeater to lend
and point eight three repeater to spend
and point eight three repeater to take home to my wife.
```

###### ↳ ↳ ↳ Re: Testing a date age by month

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2002-08-16T20:48:21-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<ajk6gl$nok$1@panix1.panix.com>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com> <XHf79.15201$Ke2.1265293@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <XHf79.15201$Ke2.1265293@bgtnsc04-news.ops.worldnet.att.net>,
Hugh Candlin <NoPersonalMailPlease@MyDot.Com> wrote:
>
>Richard <riplin@Azonic.co.nz> wrote in message
…[16 more quoted lines elided]…
>

Hmmmm... no arithmeticals in this part so...

No cares have I to grieee-eeeve me,
No pretty little girls to de-cee-eeeive me,
I'm happy as a King, be-liee-eeeve me,
As we go rolling, rolling home!

DD
```

###### ↳ ↳ ↳ Re: Testing a date age by month

_(reply depth: 4)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-08-16T21:16:20-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Rth79.14088$EJ4.396951@news4.srv.hcvlny.cv.net>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com> <XHf79.15201$Ke2.1265293@bgtnsc04-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:
> Richard <riplin@Azonic.co.nz> wrote in message
> news:217e491a.0208161505.21ccf61b@posting.google.com...
…[18 more quoted lines elided]…
> and point eight three repeater to take home to my wife.

Is their rubber room ready yet?

:-)
```

###### ↳ ↳ ↳ Pre-decmilazation (was: Testing a date age by month

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-16T18:16:27-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<ajk1bo$ek4$1@slb5.atl.mindspring.net>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com>`

```
From the true world of "trivia".  IBM's COBOL compilers actually INCLUDED
full support for Pounds, Shilling, Pence as "USAGE DISPLAY-ST".  This
included support for the Report Writer "SUM" function.  This feature was
last documented in their ANS COBOL V4 product - but the support remained in
OS/VS COBOL *and* such programs still work when run with LE.   The most
interesting part of this (to me) was the distinction between upper- and
lower-case "D/d" in the PICTURE clause (and this was BEFORE other parts of
the source code could be lower-case).
```

###### ↳ ↳ ↳ Re: Pre-decmilazation (was: Testing a date age by month

_(reply depth: 4)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-08-16T21:17:17-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Luh79.14089$EJ4.396951@news4.srv.hcvlny.cv.net>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com> <ajk1bo$ek4$1@slb5.atl.mindspring.net>`

```
William M. Klein wrote:
> From the true world of "trivia".  IBM's COBOL compilers actually INCLUDED
> full support for Pounds, Shilling, Pence as "USAGE DISPLAY-ST".  This
…[5 more quoted lines elided]…
> the source code could be lower-case).

That's truly amazing, Bill. There's always something new in c.l.c.
```

###### ↳ ↳ ↳ Re: Pre-decmilazation (was: Testing a date age by month

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-17T01:59:35+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3D5DAF17.BB9325A5@shaw.ca>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <3D52A292.6C8A4E8F@shaw.ca> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com> <ajk1bo$ek4$1@slb5.atl.mindspring.net>`

```


"William M. Klein" wrote:

> From the true world of "trivia".  IBM's COBOL compilers actually INCLUDED
> full support for Pounds, Shilling, Pence as "USAGE DISPLAY-ST".  This
…[6 more quoted lines elided]…
>

Don't want the Standard's God rushing off researching - but - did IBM allow for
following in the character set :-

1/4d = farthing,  1/2d = halfpenny (ha'penny) and 3/4d = three farthings ?

Along with the pound symbol we had those three characters on our early printer
barrels.

You are probably 'happier' with Standard's God rather than Horace Rumpole <G>.
Poor old Horace - Australian actor Leo McKern at 82 has recently died in
Bristol. Apart from his lovable performance in Rumpole, great movie actor -
stubborn cardinal in 'Shoes of the Fisherman' along with another 'favourite',
Anthony Quinn as the Ukrainian Pope and Laurence Olivier. As the Tudor era
Thomas Cromwell, (no relation to Oliver), the prosecutor of Sir Thomas More in
one of my *very* favourite movies 'A Man for all Seasons'.

Seeing Doc's quote - made me think he was thinking of a different tune - not so
- for the 'Uniformed', the following from an American site WASP Songs (White
Anglo Saxon Protestants ?) :-

                        I've got sixpence, jolly, jolly sixpence,
                                 I've got sixpence to last me all my life.
                             I've got twopence to spend and twopence to lend
                            And twopence to send home to my wife, poor wife.

                         No cares have I to grieve me, no tall and handsome man
                            To deceive me, I'm happy as a queen, believe me,
                                    As we go rolling, rolling home.

                          Rolling home, rolling home, rolling home, rolling
home,
                                    By the light of the silvery moon,
                            Happy is the day when the Air Corps gets its pay,
                                    As we go rolling, rolling home.

                                I've got fourpence, jolly, jolly fourpence,
                                 I've got fourpence to last me all my life,
                            I've got twopence to spend and twopence to lend,
                            And no pence to send home to my wife, poor wife.

                                 I've got twopence, jolly, jolly twopence,
                                 I've got twopence to last me all my life,
                             I've got twopence to spend and no pence to lend,
                            And no pence to send home to my wife, poor wife!

***  'twopence' is pronounced 'Tuppence' in the UK.

Did I ever tell you about the lady who walked into the Debenhams store in
Taunton, two days after we switched to decimal currency, ('73 ?). She looked at
the handful of 'strange' change she was given and mumbled, "I'll give this
system about a month, before it blows up !".

What's all this got to do with COBOL ? Absolutely bugger all ! But it's FUN <g>

Jimmy




>
> --
…[13 more quoted lines elided]…
> > To last me all my life.  ....
```

###### ↳ ↳ ↳ Re: Pre-decmilazation (was: Testing a date age by month

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-17T14:05:42-07:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0208171305.14268326@posting.google.com>`
- **References:** `<20020808131830.17610.qmail@nym.alias.net> <aiu93r$2u3$1@slb6.atl.mindspring.net> <3D52B4AC.F2644D6E@shaw.ca> <VA.0000023b.03646ff3@ieee.org> <aiumjl$nmg$1@peabody.colorado.edu> <UfO49.20069$Z7.1112060@e3500-atl1.usenetserver.com> <3D54070E.B3CC96CE@shaw.ca> <aj1bgq$mb7$1@slb6.atl.mindspring.net> <3D5C9942.B92F8273@Azonic.co.nz> <3D5C93D6.62D608D3@shaw.ca> <217e491a.0208161505.21ccf61b@posting.google.com> <ajk1bo$ek4$1@slb5.atl.mindspring.net> <3D5DAF17.BB9325A5@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote i

> - for the 'Uniformed', the following from an American site WASP Songs 
> (White Anglo Saxon Protestants ?) :-

No: 
>> songs and lyrics of songs sung by the WASP (Women Airforce Service
Pilots) of WWII

It was a british song attributed to the RAF in the 1920s, or possibly
goes back to the RFC in WWI (RAF was formed in 1918).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
