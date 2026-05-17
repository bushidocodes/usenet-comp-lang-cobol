[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for COBOL Charter

_6 messages · 6 participants · 1998-01_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Looking for COBOL Charter

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-01-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34c0ecc5.20452574@nntp.ix.netcom.com>`

```

Hi, all,
I'm trying to locate some software that can read multiple COBOL source
code and produce meaningful reports on file usage, copybook usage,
dataname crossreferences by 'use vs update', etc. I KNOW such
software must exist, but I've been away from software vendors for 8
years and don't have at my fingertips... sure hope you do and will
share. This is part of a year2000 project and I'm hoping I can find
some software to assist in the inventory process.... (YES, I admit
we're starting L-A-T-E... but management is management is
management...) Thanks for whatever you can share....
David

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: Looking for COBOL Charter

- **From:** "einar clementz" <ua-author-6588781@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f80effd868-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34c0ecc5.20452574@nntp.ix.netcom.com>`
- **References:** `<34c0ecc5.20452574@nntp.ix.netcom.com>`

```

Hi

This is an answer to both JCL and COBOL charter

We have at our shop REVOLVE from Microfocus. This tool is a very handy for
both JCL and COBOL.
It will give what You search. It reads JCL, COBOL and many related type of
code, SQL, BMS, PSB etc.
And the You can produce report in hundreds of ways. Graphical and text.

Regards,
Einar Clementz, Oslo, Norway


David wrote:

› Hi, all,
› I'm trying to locate some software that can read multiple COBOL source
…[11 more quoted lines elided]…
› ____________________________________
```

#### ↳ Re: Looking for COBOL Charter

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f80effd868-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34c0ecc5.20452574@nntp.ix.netcom.com>`
- **References:** `<34c0ecc5.20452574@nntp.ix.netcom.com>`

```

In article <34c··.@nnt··m.com>,
David wrote:
› Hi, all, 
› I'm trying to locate some software that can read multiple COBOL source
…[8 more quoted lines elided]…
› David

You can use CobolTransformer from Siber Systems to do necessary
reports and even write up your own converter for Year 2000.

CobolTransformer is a C++ toolkit which you can use to write reporting
tools, Y2K fixup tools, converters, and even Cobol compilers.

It consists of Cobol parser, expression tree transformation library,
and Cobol code generator.

In the newest Version 2.1.0 that will be released at the end of January
we have introduced Use-to-Definition links, which make doing
"dataname crossreferences" real easy. In fact, complete Cobol
Symbol Table implementation will be the biggest news for this release.

I admit, you would need to do some programming, but, hey,
you will not be limited by the narrow frame of the
more traditional vendor that gives you non-customizable tool.
You will be able to do any reports you like, and then program
your own fixup tool!

Details are available from http://www.siber.com/sct/


Best regards,
Vadim Maslov
```

##### ↳ ↳ Re: Looking for COBOL Charter

- **From:** "jim price" <ua-author-2338161@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f80effd868-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f80effd868-p3@usenetarchives.gap>`
- **References:** `<34c0ecc5.20452574@nntp.ix.netcom.com> <gap-f80effd868-p3@usenetarchives.gap>`

```

Take a look at Millennium Dynamics. Customize it to your hearts content.
Can be used for other than Y2K, such as Euro-Dollar, SSN expansion, etc.

Vadim Maslov wrote in message <69f5qn$r.··.@new··s.su>...
› In article <34c··.@nnt··m.com>,
› David  wrote:
…[3 more quoted lines elided]…
›› dataname crossreferences by 'use vs update', etc
```

###### ↳ ↳ ↳ Re: Looking for COBOL Charter

- **From:** "richard frankel" <ua-author-6589082@usenetarchives.gap>
- **Date:** 1998-01-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f80effd868-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f80effd868-p4@usenetarchives.gap>`
- **References:** `<34c0ecc5.20452574@nntp.ix.netcom.com> <gap-f80effd868-p3@usenetarchives.gap> <gap-f80effd868-p4@usenetarchives.gap>`

```

› Vadim Maslov wrote in message <69f5qn$r.··.@new··s.su>...
›› In article <34c··.@nnt··m.com>,
…[4 more quoted lines elided]…
››› dataname crossreferences by 'use vs update', etc

Take a look a ViaSoft VIA/Insight product set. it does everything you
want. I don't work for them either
I'm sick of SPAM
My proper Email addresss is: FRANKER at BOAT dot BT dot COM
Please retype it yourself. Thanks
```

###### ↳ ↳ ↳ Re: Looking for COBOL Charter

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1998-01-15T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f80effd868-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f80effd868-p4@usenetarchives.gap>`
- **References:** `<34c0ecc5.20452574@nntp.ix.netcom.com> <gap-f80effd868-p3@usenetarchives.gap> <gap-f80effd868-p4@usenetarchives.gap>`

```

On Tue, 13 Jan 1998 06:29:53 -1000, "Jim Price"
wrote:

› Take a look at Millennium Dynamics. Customize it to your hearts content.
› Can be used for other than Y2K, such as Euro-Dollar, SSN expansion, etc.

What is Euro-Dollar?


Charles F Hankel
------------------------------------------------------------------
COBOLs: IBM D, E, F, ANS v4, VS, COBOL 2, LE/370, AIX, S/38, OS/2,
PC/MS-DOS, Honeywell GCOS, Burroughs 7000, Tandem, HP3000
all to varying degrees over the past 25 years or so.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
