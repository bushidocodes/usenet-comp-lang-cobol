[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How BIG is a mainframe?

_3 messages · 3 participants · 1999-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: How BIG is a mainframe?

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<384075E7.3CAC7FAF@att.net>`
- **References:** `<81126@news2.mia> <gnqh3s81jmoe1fgc236e5aqe506muk1du8@4ax.com> <81ddu6$o3v$1@nntp9.atl.mindspring.net> <e6fm3sk3d315osgfvua3n5t33tte62f4o0@4ax.com> <383B8876.9E337E19@att.net> <bedp3sohv7qf2vsho1ibgdammfshdiammq@4ax.com> <383DEC50.40E1A992@att.net> <bh5s3ssjkig2l21vj3lvjetnerhqs1g70t@4ax.com>`

```
G Moore wrote:
> 
(snip)
> 
> >somewhere. You really don't have a grasp of what we (mainframers) run
…[3 more quoted lines elided]…
> factory, or whatever, has it's doors open.

You weren't paying attention, were you. Any really global business
probably has an office open somewhere across the globe at any time Mon.
thru Fri.

> let me take a guess at what mainframes do daily, eh?

Sounds to me as though you don't have a very good handle on what
commercial banks (especially what are called "money center" banks) do. 

> a>cache database transactions
> b>update a global debit/credit variable, and borrow/loan based on
…[3 more quoted lines elided]…
> adds a fee (which the sending and recieving bank both get a chunk of)

You're really pissed off that banks make money, aren't you?

> e>keep a system log of hard drive errors (which are replaced in the
> morning)

Mainframes (IBM, anyway) do this on their own and notify IBM service.
Sometimes the first notice we have of a malfunction is when the CE shows
up and says there's a problem in a certain string of DASD.

> f>shadow drives, log transactions and then update to the defragmented
> drive

Defragmented drive? LOL

> g>put out reports of which customers aren't keeping payments
> h>send reports to the irs of transactions which match above $10k

Not in my application (securities movement & control). We have *few*
transactions as small as $10K, and nothing I'm aware of which must be
reported to the IRS. Maybe to the SEC or the Fed if we suspect fraud?

> am i close?

Not at all. You didn't mention determining if the transaction (i.e.,
securities trade) settles in same day funds or not, checking if it's US
or global and, if global, the market where the trade is executed vs. the
market where where it settles, how to determine the custodian and
subcustodian. how to match trades entered by our customers with the
confirms we get from DTC (automated & manual, of course), what to do if
the trade has tax lot information, is the security book entry or
physical, etc. Keep in mind that customers in the US buy non-US
securities and vice versa and that Singapore & Tokyo are working in
tomorrow, not today (they're across the international date line). But,
what it's an FX trade? Does it include any USD? Do they settle in the US
or globally? Don't think of this as an exhaustive list, BTW.

I'm not going to debate this notion any more, G Moore (not that I'm
pissed at you, or anything, but I think it's a waste of bandwidth at
this point),

Bill Lynch
```

#### ↳ Re: How BIG is a mainframe?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vwe04.510$cq6.5619@typhoon01.swbell.net>`
- **References:** `<81126@news2.mia> <gnqh3s81jmoe1fgc236e5aqe506muk1du8@4ax.com> <81ddu6$o3v$1@nntp9.atl.mindspring.net> <e6fm3sk3d315osgfvua3n5t33tte62f4o0@4ax.com> <383B8876.9E337E19@att.net> <bedp3sohv7qf2vsho1ibgdammfshdiammq@4ax.com> <383DEC50.40E1A992@att.net> <bh5s3ssjkig2l21vj3lvjetnerhqs1g70t@4ax.com> <384075E7.3CAC7FAF@att.net>`

```

William Lynch <WBLynch@att.net> wrote in message
news:384075E7.3CAC7FAF@att.net...
> G Moore wrote:
> >
> (snip)
> >
> > >somewhere. You really don't have a grasp of what we (mainframers)
run
> > >through our systems daily. What's a *physical* business?
> >
…[4 more quoted lines elided]…
> probably has an office open somewhere across the globe at any time
Mon.
> thru Fri.

There was a time, not so very long ago, that every time
Big Ben struck the hour, somewhere in the world, the British
Ensign was being raised to mark the beginning of another
day of enlightened English rule.

Today, every time the National Bureau of Standards atomic
clock sends a tick, another Microsoft boot-up logo appears
to herald the beginning of another productive session.

(giggle, giggle, giggle)
```

#### ↳ Re: How BIG is a mainframe?

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3842D0AF.2A6A8D31@NOSPAMhome.com>`
- **References:** `<81126@news2.mia> <gnqh3s81jmoe1fgc236e5aqe506muk1du8@4ax.com> <81ddu6$o3v$1@nntp9.atl.mindspring.net> <e6fm3sk3d315osgfvua3n5t33tte62f4o0@4ax.com> <383B8876.9E337E19@att.net> <bedp3sohv7qf2vsho1ibgdammfshdiammq@4ax.com> <383DEC50.40E1A992@att.net> <bh5s3ssjkig2l21vj3lvjetnerhqs1g70t@4ax.com> <384075E7.3CAC7FAF@att.net>`

```
William Lynch wrote:

> > f>shadow drives, log transactions and then update to the defragmented
> > drive
> 
> Defragmented drive? LOL

Actually this is very close to an irritant of mine.  IBM PDS members
have to be compressed by users, but users can't undelete files.  This
illustrates a PC type mentality on mainframes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
