[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL DB2 sub-program

_8 messages · 6 participants · 2003-03_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL DB2 sub-program

- **From:** "Klaus Sch���fer" <KSchaefer@nature-store.de>
- **Date:** 2003-03-22T21:22:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5igmp$54u$03$1@news.t-online.com>`

```
Hello,

I need to write a COBOL SUB-Programm for OS/390 environment that does EXEC
SQL to DB2 to do commit processing. This program must be CALLed from several
other COBOl-programs, so will be linked (static) to these programs and must
handle several call parameters.

Can someone give me a sample of how this SUB-program must look like? Do I
have to bind the SUB-program or does it take the DB2-environment from the
main program?

All help is appreciated very much!

Klaus
```

#### ↳ Re: COBOL DB2 sub-program

- **From:** docdwarf@panix.com
- **Date:** 2003-03-22T16:26:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5ike0$7j8$1@panix1.panix.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com>`

```
In article <b5igmp$54u$03$1@news.t-online.com>,
Klaus Sch�fer <KSchaefer@nature-store.de> wrote:
>Hello,
>
…[5 more quoted lines elided]…
>Can someone give me a sample of how this SUB-program must look like?

Yes, that 'someone' is a programmer with, oh, four years' worth of 
experience in COBOL and DB2.  Find such a person, supply a halfway 
competent set of specs, pay a decent rate and you'll be all set.

DD
```

#### ↳ Re: COBOL DB2 sub-program

- **From:** B Berman <bberman@netbox.com>
- **Date:** 2003-03-22T22:13:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E7CE1BE.B0D3AC2C@netbox.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com>`

```
"Klaus Schï¿½fer" wrote:

> I need to write a COBOL SUB-Programm for OS/390 environment that does EXEC
> SQL to DB2 to do commit processing. This program must be CALLed from several
…[5 more quoted lines elided]…
> main program?

Why would you want to use a static call and link the sub-program into each load
module that calls it ? If it were ever to need maintenance, every program that
referenced it would need to be relinked and re-bound. It seems to me that a
dynamic call would be the way to go, especially in an OS/390 environment.  In
that context (dynamic), yes, the sub-program would need a bind.

I won't even question why a separate module just for Commit logic...

Bob
```

#### ↳ Re: COBOL DB2 sub-program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-03-23T00:50:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43qp7vo0b8n70qh2k8fgfd89se1j7275qa@4ax.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com>`

```
On Sat, 22 Mar 2003 21:22:46 +0100 "Klaus Schï¿½fer" <KSchaefer@nature-store.de>
wrote:

:>I need to write a COBOL SUB-Programm for OS/390 environment that does EXEC
:>SQL to DB2 to do commit processing. This program must be CALLed from several
:>other COBOl-programs, so will be linked (static) to these programs and must
:>handle several call parameters.

:>Can someone give me a sample of how this SUB-program must look like? Do I
:>have to bind the SUB-program or does it take the DB2-environment from the
:>main program?

Your requirement does not make any sense.

Why would the subroutine be doing COMMITs alone?

Why is there a need of a subroutine to do COMMITs?
```

#### ↳ Re: COBOL DB2 sub-program

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-22T23:46:10
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7cf5c5$1_2@text-west.newsgroups.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com>`

```

"Klaus Sch�fer" <KSchaefer@nature-store.de> wrote in message
news:b5igmp$54u$03$1@news.t-online.com...
> Hello,
>
> I need to write a COBOL SUB-Programm for OS/390 environment that does EXEC
> SQL to DB2 to do commit processing. This program must be CALLed from
several
> other COBOl-programs, so will be linked (static) to these programs and
must
> handle several call parameters.
>
…[7 more quoted lines elided]…
>
Klaus,

review the design here.

Static linkage for a utility module is stupid.

It should be dynamic and it will need to be bound. (But really, you
shouldn't even do it...)

It looks to me as though you intend to call this module when you are
satisfied that the transaction is complete. A review of the overall
transaction design may cause you to change your mind about this.

(I hope so...<G>).

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: COBOL DB2 sub-program

- **From:** "Klaus Sch���fer" <KSchaefer@nature-store.de>
- **Date:** 2003-03-23T11:03:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5k0pi$dog$02$1@news.t-online.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com>`

```
Hello Guys,

thanks for your help.... it's a too funny story to explain why I will need
this as a sub-program. But I think you're right about dynamic vs static and
I'll implement it as a dynamic routine. It was important to me to get to
know that I have to bind this module to get it to work.

Thanks again
Klaus

"Klaus Schï¿½fer" <KSchaefer@nature-store.de> schrieb im Newsbeitrag
news:b5igmp$54u$03$1@news.t-online.com...
> Hello,
>
> I need to write a COBOL SUB-Programm for OS/390 environment that does EXEC
> SQL to DB2 to do commit processing. This program must be CALLed from
several
> other COBOl-programs, so will be linked (static) to these programs and
must
> handle several call parameters.
>
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL DB2 sub-program

- **From:** pakku@soccermail.com (Thomas Charles)
- **Date:** 2003-03-28T13:27:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89355d6f.0303281327.4d00bde5@posting.google.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com> <b5k0pi$dog$02$1@news.t-online.com>`

```
"Klaus Schï¿½fer" <KSchaefer@nature-store.de> wrote in message news:<b5k0pi$dog$02$1@news.t-online.com>...
> Hello Guys,
> 
…[27 more quoted lines elided]…
> >
The DB2 equivalent of dynamic linking is package binding.  If your
shop still does plan binding even if you don't have to relink for
every change to this subroutine, you will have to bind all the plans
using this.
```

###### ↳ ↳ ↳ Re: COBOL DB2 sub-program

- **From:** B Berman <bberman@netbox.com>
- **Date:** 2003-03-28T22:38:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E84D0CD.CE96C00@netbox.com>`
- **References:** `<b5igmp$54u$03$1@news.t-online.com> <b5k0pi$dog$02$1@news.t-online.com> <89355d6f.0303281327.4d00bde5@posting.google.com>`

```
Thomas Charles wrote:

> The DB2 equivalent of dynamic linking is package binding.  If your
> shop still does plan binding even if you don't have to relink for
> every change to this subroutine, you will have to bind all the plans
> using this.

Good point !
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
