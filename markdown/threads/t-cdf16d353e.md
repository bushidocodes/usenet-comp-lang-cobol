[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Differences between Cobol and Cobol II (Mainframe)

_10 messages · 8 participants · 2000-12 → 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Differences between Cobol and Cobol II (Mainframe)

- **From:** Nige <nigel@gofree.to>
- **Date:** 2000-12-19T00:11:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
Can anyone point me to an IBM Publication or can tell me the
difference between Cobol and Cobol II.

Thanks
Nige
```

#### ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** mike__c@my-deja.com
- **Date:** 2000-12-19T10:32:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91ndgd$gua$1@nnrp1.deja.com>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
Look for VS COBOL II V1R4.0 Migration Guide for MVS and CMS at
http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/FINDBOOK?filter=cobol

In article <ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>,
  Nige <nigel@gofree.to> wrote:
> Can anyone point me to an IBM Publication or can tell me the
> difference between Cobol and Cobol II.
…[4 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** Nige <nigel@gofree.to>
- **Date:** 2000-12-19T11:54:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2ju3tss9j4ghivr69b180n4mm5dab5qak@4ax.com>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com> <91ndgd$gua$1@nnrp1.deja.com>`

```
mike__c@my-deja.com wrote:

>Look for VS COBOL II V1R4.0 Migration Guide for MVS and CMS at
>http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/FINDBOOK?filter=cobol

Cheers Mike
Just what I wanted :-)

Nige
```

#### ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-12-19T14:17:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001219091749.10509.00001899@ng-fn1.aol.com>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
 nigel@gofree.to writes ...

>Can anyone point me to an IBM Publication or can tell me the
>difference between Cobol and Cobol II.
>


Here is a summary of our course "Beyond COBOL II" which covers what's new after
OS/VS COBOL. This two day course covers:

* COBOL II changes
  - mixed-case code, unnamed filler
  - packed-decimal, binary data types
  - changes to tables (sizes, dimensions, intialization)
  - reference modification and hex literals
  - pointers and addresses
  - nested programs
  - passing BY CONTENT
  - scope terminators (END-IF, etc.)
  - in-line PERFORM
  - SET ... TO TRUE construct
  - CONTINUE statement
  - INITIALIZE statement
  - EVALUATE statement
* COBOL/370 (V1R1) changes (mostly intrinsic functions)
* Brief introduction to LE (Language Environment), including 
  - full discussion of date and time LE services
  - overview of all services
  - sample code for condition handling and dynamic storage allocation
* COBOL for MVS & VM (V1R2) changes (mostly enhanced C interoperability)
  - Null-terminated literals
  - Euro support
  - local-storage section
  - recursive programs
  - RETURNING option on call and procedure header
  - pass arguments BY VALUE
  - introduction to Object Oriented COBOL
* COBOL for OS/390 & VM (V2R1) changes
  - DLL support
  - new intrinsic functions
  - new options for ACCEPT
  - Millenium Language Extensions (optional)
* COBOL for OS/390 & VM (V2R2) changes
  - ADDRESS OF for working-storage
  - comp-5 data
  - 31-digit numbers
  - line sequential files
  - OS/390 UNIX support
  - SQL co-processor support

Includes four hands on exercises.

That should get application programmers up to speed quickly.

More detail on our website: http://www.trainersfriend.com


Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-19T08:25:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91nr3j$3j5$1@slb0.atl.mindspring.net>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
If you are just now looking at these differences, are you aware that VS
COBOL II will "go out of service" in 3 months?  This is an (almost) obsolete
compiler.  It doesn't include intrinsic functions or much support for
4-digit years.  The current "strategic" IBM COBOL compiler is "IBM COBOL for
OS/390 & VM".  It has its own migration guide, if you are interested in
that.
```

#### ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** croxbo@my-deja.com
- **Date:** 2000-12-19T23:30:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91or1j$p32$1@nnrp1.deja.com>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
First difference is between COBOL 74 and COBOL 85.

The best book I know of is COBOL /370 for vs cobol and cobol II
programmers from Harvey Bookman / Mc Graw Hill. Harvey explains all the
differences in a great way between 4 different compilers: OSVS, COBOL
II version 1 and 2, COBOL 370.



Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-12-20T14:00:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001220090048.12169.00005446@ng-cj1.aol.com>`
- **References:** `<91or1j$p32$1@nnrp1.deja.com>`

```
croxbo@my-deja.com writes...

>First difference is between COBOL 74 and COBOL 85.
>
…[4 more quoted lines elided]…
>

Ah, but it is already clearly out of date by three compiler releases.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2001-01-01T07:01:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A502AF0.5090908@optonline.net>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com>`

```
Nige wrote:

> Can anyone point me to an IBM Publication or can tell me the
> difference between Cobol and Cobol II.
> 
> Thanks
> Nige

Ann Prince wrote a good book (I think it's called "VS COBOL II", of all 
things) on the differences, with coding examples.  It's published by 
Mike Murach.

LiamD
```

##### ↳ ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-06T09:22:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<937a95$sm5$1@news.igs.net>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com> <3A502AF0.5090908@optonline.net>`

```
Liam Devlin wrote in message <3A502AF0.5090908@optonline.net>...
>Nige wrote:
>
…[5 more quoted lines elided]…
>

Two ...
```

###### ↳ ↳ ↳ Re: Differences between Cobol and Cobol II (Mainframe)

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-06T13:10:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDF15C0BEC6C119.15212EB6DB4F2894.B6204B6344271A49@lp.airnews.net>`
- **References:** `<ps9t3tc1gu0tp1gta1i3of94enatj6mivj@4ax.com> <3A502AF0.5090908@optonline.net> <937a95$sm5$1@news.igs.net>`

```
On Sat, 6 Jan 2001 09:22:31 -0500, "donald tees" <donald@willmack.com>
enlightened us:

>Liam Devlin wrote in message <3A502AF0.5090908@optonline.net>...
>>Nige wrote:
…[10 more quoted lines elided]…
>
No Don that would have to be II...

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Today's subliminal thoughts are: 


Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
