[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# comp-2

_6 messages · 6 participants · 2000-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### comp-2

- **From:** smr1106 <_steve_roseNO_sSPAM@msn.com.invalid>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>`

```
I'm an oldtimer, and know what comp and comp-3 are, but comp-2 doesn't
ring a bell.  Any help would be much appreciated.


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: comp-2

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0iYk5.385$O16.110520@paloalto-snr1.gtei.net>`
- **References:** `<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>`

```
COMP-2 is "implementor-defined."

Often (e.g., Microfocus, IBM COBOL/390) it is "double precision floating
point," and often there in IEEE 32-bit float. IBM mainframe under L/E offers
FLOAT(IEEE) or FLOAT(HEX) or FLOAT(NATIVE) ( the last two mean the same
thing) as default installation options. I think you can override them at
either compile time or run-time, but for the life of me I don't know why you
would.
```

#### ↳ Re: comp-2

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n1nm7$vmf$1@slb6.atl.mindspring.net>`
- **References:** `<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>`

```
COMP-2 is an aligned Floating-Point Long Doubleword (Assembler "D").

HTH....

Cheers,

WOB

"smr1106" <_steve_roseNO_sSPAM@msn.com.invalid> wrote in message
news:0c122ab4.83c8d241@usw-ex0107-050.remarq.com...
> I'm an oldtimer, and know what comp and comp-3 are, but comp-2 doesn't
> ring a bell.  Any help would be much appreciated.
>
>
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

#### ↳ Re: comp-2

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n1ctp$4ga$1@slb6.atl.mindspring.net>`
- **References:** `<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>`

```
With IBM mainframe COBOLs (and those that emulate it),
   COMP-1 is "short floating-point"
   COMP-2 is "long floating-point"

If you aren't on an IBM mainframe (or something emulating it) let us know
which compiler you are using and someone in the group will probably know what
COMP-2 means there.
```

#### ↳ Re: comp-2

- **From:** "mike sheehan" <sheehan_mj@iolfree.ie>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uuhm5.1309$sa4.4012@news.iol.ie>`
- **References:** `<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>`

```
Basically COMP-2 is a large-floating-point-number.
No PIC clause is associated with it.
The Fujitsu compiler uses  eight bytes to represent the equivalent of a
Visual Basic "double" data type.
It is compatible with the IEEE floating-point format.
See page 763 of "Mastering COBOL" by C.Baroudi for more details re: IBM,
Microfocus.

Mike


smr1106 <_steve_roseNO_sSPAM@msn.com.invalid> wrote in message
<0c122ab4.83c8d241@usw-ex0107-050.remarq.com>...
>I'm an oldtimer, and know what comp and comp-3 are, but comp-2 doesn't
>ring a bell.  Any help would be much appreciated.
>
>
>* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
>The fastest and easiest way to search and participate in Usenet - Free!
>
```

##### ↳ ↳ Re: comp-2

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-08-16T02:59:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000815225907.02560.00000101@ng-df1.aol.com>`
- **References:** `<Uuhm5.1309$sa4.4012@news.iol.ie>`

```
Just a side note. On the mainframe, LE COBOL uses comp-2 data to hold Lilian
timestamps, useful in several LE date / time services.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
