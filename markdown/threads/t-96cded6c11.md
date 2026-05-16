[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HDD Number

_11 messages · 7 participants · 2008-08_

---

### HDD Number

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-08-05T04:25:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com>`

```
is there a function in cobol that i can get my HDD number, or chip
number or some other unique single user identification ?

tks a lot!
```

#### ↳ Re: HDD Number

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-08-05T08:33:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com>`

```
On Aug 5, 4:25 am, mario <mmc_vw1...@hotmail.com> wrote:
> is there a function in cobol that i can get my HDD number, or chip
> number or some other unique single user identification ?
>
> tks a lot!



Hi,

There are no COBOL functions that can get a unique system ID.
But, if you are willing and able to use the Windows Management
Instrumentation classes, then....

You can use the same installation ID of the operating system
to get a globally unique ID for a given machine.  The following
WMI class should help you out:

	Win32_WindowsProductActivation

Or, you can use the following WMI class to get the manufacturer's
serial number used to identify the physical media:

	Win32_PhysicalMedia

http://msdn2.microsoft.com/En-US/library/aa394520.aspx

http://msdn2.microsoft.com/en-us/library/Aa394346.aspx

Kellie.
```

##### ↳ ↳ Re: HDD Number

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-08-05T21:08:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com>`

```
On Aug 6, 3:33 am, Kellie Fitton <KELLIEFIT...@yahoo.com> wrote:
> On Aug 5, 4:25 am, mario <mmc_vw1...@hotmail.com> wrote:
>
…[15 more quoted lines elided]…
>         Win32_WindowsProductActivation

I suspect that this need not be 'globally unique'. For example in
corporates where machines are cloned with a corporate license will
they not be all the same ?


> Or, you can use the following WMI class to get the manufacturer's
> serial number used to identify the physical media:
>
>         Win32_PhysicalMedia

What happens when the OS is running on virtualised hardware ?


> http://msdn2.microsoft.com/En-US/library/aa394520.aspx
>
> http://msdn2.microsoft.com/en-us/library/Aa394346.aspx

Your suggestion is also a Windowsie thing and this may not be mario's
environment.
```

###### ↳ ↳ ↳ Re: HDD Number

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-08-06T08:42:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f67bdb25-5c15-4ad7-964f-d83d55d89db1@59g2000hsb.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com> <88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com>`

```
On Aug 5, 9:08 pm, Richard <rip...@azonic.co.nz> wrote:
>
> I suspect that this need not be 'globally unique'. For example in
…[4 more quoted lines elided]…
>



Hi Richard,

There are no truly unique machine identifiers,  PC and PC
compatible computers do not have unique IDs.  The serial
number of an ATA hard disc unit uniquely identifies that ATA
hard disc.  The serial number of an Intel CPU uniquely identifies
that CPU.  The "machine SID" created by Windows NT uniquely
identifies that installation of Windows NT.

In a network environment, the MAC address is unique on a given
network segment,  but duplications certainly can exist on different
segments.  Moreover, changing the MAC address is not so difficult,
maybe Mario should look into the commercial packages for software
licensing.

Kellie.
```

###### ↳ ↳ ↳ Re: HDD Number

_(reply depth: 4)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-08-06T12:24:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39d1ad11-6411-4520-9e90-5fc5c6ebe821@r15g2000prh.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com> <88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com> <f67bdb25-5c15-4ad7-964f-d83d55d89db1@59g2000hsb.googlegroups.com>`

```
On Aug 7, 3:42 am, Kellie Fitton <KELLIEFIT...@yahoo.com> wrote:
> On Aug 5, 9:08 pm, Richard <rip...@azonic.co.nz> wrote:
>
…[13 more quoted lines elided]…
> hard disc.

Only if the manufacturer has actually put a unique number in the ROM
of the drive. Many put a generic number by batch.

> The serial number of an Intel CPU uniquely identifies
> that CPU.  The "machine SID" created by Windows NT uniquely
> identifies that installation of Windows NT.

The question I asked was whether, in fact, it is unique when
corporates clone machines.

> In a network environment, the MAC address is unique on a given
> network segment,  but duplications certainly can exist on different
> segments.

The MAC address on a NIC is allocated to manufacturers by the IEEE and
is unique to every ethernet or WiFi card. It is burned on the card but
may, of course, be spoofed.

It has nothing to do with segments which is based on IP address which
is quite different.

> Moreover, changing the MAC address is not so difficult,

Nor any of the others.

> maybe Mario should look into the commercial packages for software
> licensing.
```

###### ↳ ↳ ↳ Re: HDD Number

_(reply depth: 5)_

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-08-08T00:03:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<de61a063-3f15-40f5-b505-d6fb968fe8c7@k13g2000hse.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com> <88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com> <f67bdb25-5c15-4ad7-964f-d83d55d89db1@59g2000hsb.googlegroups.com> <39d1ad11-6411-4520-9e90-5fc5c6ebe821@r15g2000prh.googlegroups.com>`

```
is there a way to get the mac-address via cobol??
```

###### ↳ ↳ ↳ Re: HDD Number

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-08T23:43:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g2pq7FdrtljU1@mid.individual.net>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com> <88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com> <f67bdb25-5c15-4ad7-964f-d83d55d89db1@59g2000hsb.googlegroups.com> <39d1ad11-6411-4520-9e90-5fc5c6ebe821@r15g2000prh.googlegroups.com> <de61a063-3f15-40f5-b505-d6fb968fe8c7@k13g2000hse.googlegroups.com>`

```


"mario" <mmc_vw1200@hotmail.com> wrote in message 
news:de61a063-3f15-40f5-b505-d6fb968fe8c7@k13g2000hse.googlegroups.com...
> is there a way to get the mac-address via cobol??

Yes. Richard posted it to this thread 3 days ago.

You can shell and run "ipconfig" (redirecting the output to a simple text 
file then reading the text file.) or you might consider running "ipconfig" 
directly through the windows API.

You never said whether you are running Windows or not, and you never stated 
which version of COBOL you are running. These things have a bearing on the 
solution.

Pete.
```

###### ↳ ↳ ↳ Re: HDD Number

_(reply depth: 7)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-08T08:25:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jRXmk.9364$vn7.9054@flpi147.ffdc.sbc.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com> <63fa1637-ce21-441c-969c-d143bbb23c18@d45g2000hsc.googlegroups.com> <88884916-307e-4f64-8af3-a7305050b049@w24g2000prd.googlegroups.com> <f67bdb25-5c15-4ad7-964f-d83d55d89db1@59g2000hsb.googlegroups.com> <39d1ad11-6411-4520-9e90-5fc5c6ebe821@r15g2000prh.googlegroups.com> <de61a063-3f15-40f5-b505-d6fb968fe8c7@k13g2000hse.googlegroups.com> <6g2pq7FdrtljU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6g2pq7FdrtljU1@mid.individual.net...
>
>
…[13 more quoted lines elided]…
>

Generic straight answer: there is no intrinsic COBOL function to get either 
"HDD number" or MAC address. You will have to call some kind of 
operating-system service or utility; or "possibly" the compiler publisher 
includes such a utility as an extension to its implementation of COBOL.

MCM
```

#### ↳ Re: HDD Number

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2008-08-05T11:51:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dotg945263t0rfr1j4h1ksj7pj7436g4ji@4ax.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com>`

```
On Tue, 5 Aug 2008 04:25:33 -0700 (PDT), mario
<mmc_vw1200@hotmail.com> wrote:

>is there a function in cobol that i can get my HDD number, or chip
>number or some other unique single user identification ?
>
>tks a lot!

Short answer- no.  

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"Bigamy is having one wife too many.  Monogamy is the
same."
--- Oscar Wilde
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: HDD Number

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2008-08-06T02:16:34+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4898991d$0$3489$a82e2bb9@reader.athenanews.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com>`

```

"mario" <mmc_vw1200@hotmail.com> wrote in message 
news:a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com...
> is there a function in cobol that i can get my HDD number, or chip
> number or some other unique single user identification ?
>
> tks a lot!

Presuming you're going through WINDOWS, would retrieving the value of 
USERNAME from the environment suit your purpose, or could you arrange for a 
unique environment variable to retrieve?
```

#### ↳ Re: HDD Number

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-08-05T12:32:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4690c6fa-3a4f-4124-a490-ac8e6c9333cf@v26g2000prm.googlegroups.com>`
- **References:** `<a031ca82-2711-4044-b02b-9e0cbb32a31e@a70g2000hsh.googlegroups.com>`

```
On Aug 5, 11:25 pm, mario <mmc_vw1...@hotmail.com> wrote:
> is there a function in cobol that i can get my HDD number, or chip
> number or some other unique single user identification ?

The MAC address on your NIC should be globally unique. On Linux /sbin/
ifconfig will list the network cards with the hardware address. On
Windows it may be ipconfig and this should give the 6 byte physical
address.

You should be able to use something like:

   CALL "SYSTEM" USING "ipconfig >networkdata" & x"00"

and then read the resulting file to extract the required item.

Warning: just because that number is burned onto the network card does
not mean that if/ip config actually gets it from there. There is a
driver between the utility and the card and anything can happen
between, and often does.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
