[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Switches vs. Flags

_5 messages · 3 participants · 2000-05_

---

### Re: Switches vs. Flags

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392c9af3.1279684@news.cableamericahsa.com>`
- **References:** `<hs5T4.62242$WF.3496313@bgtnsc04-news.ops.worldnet.att.net> <8fluli$2eig$1@news.hitter.net> <391F002C.B8ECBF2A@swbell.net> <jc4vhsg5ff58fi1egrdgcotj2shlseq613@4ax.com> <8fobjv$242q$2@news.hitter.net> <5oqvhss27m0buh0sf9ld1ma7gtv1nt77od@4ax.com> <8fp3v6$30e1$1@news.hitter.net> <8fq9hv0ig4@enews4.newsguy.com> <8g5q81$27us$1@news.hitter.net> <8g9frd$1nri$1@newssvr03-int.news.prodigy.com>`

```
On Sun, 21 May 2000 15:09:01 -0500, "Terry Heinze"
<terryheinze@prodigy.net> wrote:

>
>I think of a switch as having one of two values and a flag as having one of
>more than 2.  My thinking, of course, is overridden by what the client's
>definition is!
>

I guess that I'm of another school of thought.  Switches and flags are
the same, using one of two values:  Yes/No, On/Off etc.

Code - has more than two values.



Tim Oxler
Teo Computer
http://www.teo-computer.com
```

#### ↳ Re: Switches vs. Flags

- **From:** shine98@my-deja.com
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gjpq9$jpf$1@nnrp1.deja.com>`
- **References:** `<hs5T4.62242$WF.3496313@bgtnsc04-news.ops.worldnet.att.net> <8fluli$2eig$1@news.hitter.net> <391F002C.B8ECBF2A@swbell.net> <jc4vhsg5ff58fi1egrdgcotj2shlseq613@4ax.com> <8fobjv$242q$2@news.hitter.net> <5oqvhss27m0buh0sf9ld1ma7gtv1nt77od@4ax.com> <8fp3v6$30e1$1@news.hitter.net> <8fq9hv0ig4@enews4.newsguy.com> <8g5q81$27us$1@news.hitter.net> <8g9frd$1nri$1@newssvr03-int.news.prodigy.com> <392c9af3.1279684@news.cableamericahsa.com>`

```


It's your indicators that have more than 2 values, switches are 'on'
and 'off' and flags are 'yes', 'no' and 'maybe'. Maybe its toggles that
are 'y' and 'n' and flags that are '0' '1' and '?'. Does COBOL have
a 'maybe' as in "set ws-toggle-sw-ind to maybe". Sometimes we use low
and high values for on and off, but is there a middle value? Oh, I just
get so confused. See your shop standards for details!

~shine


In article <392c9af3.1279684@news.cableamericahsa.com>,
  tim.oxler@NOSPAMteo-computer.com (Tim Oxler) wrote:
> On Sun, 21 May 2000 15:09:01 -0500, "Terry Heinze"
> <terryheinze@prodigy.net> wrote:
>
> >
> >I think of a switch as having one of two values and a flag as having
one of
> >more than 2.  My thinking, of course, is overridden by what the
client's
> >definition is!
> >
…[10 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Switches vs. Flags

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eQOZOaox$GA.328@cpmsnbbsa08>`
- **References:** `<hs5T4.62242$WF.3496313@bgtnsc04-news.ops.worldnet.att.net> <8fluli$2eig$1@news.hitter.net> <391F002C.B8ECBF2A@swbell.net> <jc4vhsg5ff58fi1egrdgcotj2shlseq613@4ax.com> <8fobjv$242q$2@news.hitter.net> <5oqvhss27m0buh0sf9ld1ma7gtv1nt77od@4ax.com> <8fp3v6$30e1$1@news.hitter.net> <8fq9hv0ig4@enews4.newsguy.com> <8g5q81$27us$1@news.hitter.net> <8g9frd$1nri$1@newssvr03-int.news.prodigy.com> <392c9af3.1279684@news.cableamericahsa.com> <8gjpq9$jpf$1@nnrp1.deja.com>`

```
There ain' any maybes in this business

<shine98@my-deja.com> wrote in message news:8gjpq9$jpf$1@nnrp1.deja.com...
>
>
…[36 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Switches vs. Flags

- **From:** shine98@my-deja.com
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8glu38$4am$1@nnrp1.deja.com>`
- **References:** `<hs5T4.62242$WF.3496313@bgtnsc04-news.ops.worldnet.att.net> <8fluli$2eig$1@news.hitter.net> <391F002C.B8ECBF2A@swbell.net> <jc4vhsg5ff58fi1egrdgcotj2shlseq613@4ax.com> <8fobjv$242q$2@news.hitter.net> <5oqvhss27m0buh0sf9ld1ma7gtv1nt77od@4ax.com> <8fp3v6$30e1$1@news.hitter.net> <8fq9hv0ig4@enews4.newsguy.com> <8g5q81$27us$1@news.hitter.net> <8g9frd$1nri$1@newssvr03-int.news.prodigy.com> <392c9af3.1279684@news.cableamericahsa.com> <8gjpq9$jpf$1@nnrp1.deja.com> <eQOZOaox$GA.328@cpmsnbbsa08>`

```
maybe so, maybe no.

I have used 'maybe' in the past (in a slightly humourous way) as an
indicator that no decision has been made yet or that a process has not
yet been carried out.

In article <eQOZOaox$GA.328@cpmsnbbsa08>,
  "brucepbarrett" <brucepbarrett@email.msn.com> wrote:
> There ain' any maybes in this business
>
> <shine98@my-deja.com> wrote in message news:8gjpq9
$jpf$1@nnrp1.deja.com...
> >
> >
> > It's your indicators that have more than 2 values, switches are 'on'
> > and 'off' and flags are 'yes', 'no' and 'maybe'. Maybe its toggles
that
> > are 'y' and 'n' and flags that are '0' '1' and '?'. Does COBOL have
> > a 'maybe' as in "set ws-toggle-sw-ind to maybe". Sometimes we use
low
> > and high values for on and off, but is there a middle value? Oh, I
just
> > get so confused. See your shop standards for details!
> >
…[9 more quoted lines elided]…
> > > >I think of a switch as having one of two values and a flag as
having
> > one of
> > > >more than 2.  My thinking, of course, is overridden by what the
…[4 more quoted lines elided]…
> > > I guess that I'm of another school of thought.  Switches and
flags are
> > > the same, using one of two values:  Yes/No, On/Off etc.
> > >
…[12 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Switches vs. Flags

_(reply depth: 4)_

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0V$7dyx$GA.186@cpmsnbbsa09>`
- **References:** `<hs5T4.62242$WF.3496313@bgtnsc04-news.ops.worldnet.att.net> <8fluli$2eig$1@news.hitter.net> <391F002C.B8ECBF2A@swbell.net> <jc4vhsg5ff58fi1egrdgcotj2shlseq613@4ax.com> <8fobjv$242q$2@news.hitter.net> <5oqvhss27m0buh0sf9ld1ma7gtv1nt77od@4ax.com> <8fp3v6$30e1$1@news.hitter.net> <8fq9hv0ig4@enews4.newsguy.com> <8g5q81$27us$1@news.hitter.net> <8g9frd$1nri$1@newssvr03-int.news.prodigy.com> <392c9af3.1279684@news.cableamericahsa.com> <8gjpq9$jpf$1@nnrp1.deja.com> <eQOZOaox$GA.328@cpmsnbbsa08> <8glu38$4am$1@nnrp1.deja.com>`

```
I am new to this newsgroup thing so I didn't understand.  Been around awhile
and learn quickly.

<shine98@my-deja.com> wrote in message news:8glu38$4am$1@nnrp1.deja.com...
> maybe so, maybe no.
>
…[59 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
